"""Run an isolated synthetic serving benchmark inside one Slurm GPU allocation.

This is infrastructure measurement, never a scored biological evaluation.
The production model, precision, context cap and serving flags are retained.
Only the dedicated server's sequence capacity and synthetic client load vary.
"""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import signal
import socket
import subprocess
import sys
import time
import urllib.request


def write(path, data):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + '.tmp')
    tmp.write_text(json.dumps(data, indent=2) + '\n')
    tmp.replace(path)


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def stop(process):
    if process is None or process.poll() is not None:
        return
    os.killpg(process.pid, signal.SIGTERM)
    try:
        process.wait(timeout=45)
    except subprocess.TimeoutExpired:
        os.killpg(process.pid, signal.SIGKILL)
        process.wait(timeout=15)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--directory', type=Path, required=True)
    parser.add_argument('--runtime-dir', type=Path, required=True)
    args = parser.parse_args()
    folder = args.directory.resolve()
    plan_path = folder / 'plan.json'
    deadline = time.monotonic() + 900
    while not plan_path.exists():
        if time.monotonic() > deadline:
            raise TimeoutError('Benchmark plan was not finalized within15 minutes')
        time.sleep(2)
    plan = json.loads(plan_path.read_text())
    for filename, expected in plan['code_sha256'].items():
        if digest(folder / filename) != expected:
            raise ValueError('Frozen performance code changed: ' + filename)
    if not os.environ.get('SLURM_JOB_ID'):
        raise ValueError('A dedicated Slurm allocation is required')
    spec = importlib.util.spec_from_file_location('benchmark_runtime', folder / 'runtime_common.py')
    common = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(common)
    common.apply_overlay(args.runtime_dir)
    env = common.environment(args.runtime_dir)
    # Only this disposable loopback benchmark server exposes cache-reset APIs.
    # Evaluation servers retain their existing environment and endpoints.
    env['VLLM_SERVER_DEV_MODE'] = '1'
    python = args.runtime_dir / 'python/bin/python3.12'
    model_dir = common.validate_checkpoint(plan['model'], plan['revision'])
    gpu = subprocess.check_output(['nvidia-smi', '--query-gpu=index,uuid,name,memory.total',
                                   '--format=csv,noheader'], text=True)
    packages = subprocess.check_output([str(python), '-c',
        "import json,torch,importlib.metadata as m; print(json.dumps({'visible_gpu_count':torch.cuda.device_count(),'device':torch.cuda.get_device_name(0),'torch':torch.__version__,'cuda':torch.version.cuda,'vllm':m.version('vllm')}))"], env=env, text=True)
    if json.loads(packages)['visible_gpu_count'] != 1:
        raise ValueError('Exactly one allocated GPU is required')
    write(folder / 'environment.json', {'packages': json.loads(packages), 'gpu_inventory': gpu,
        'slurm_job_id': os.environ['SLURM_JOB_ID'], 'hostname': socket.gethostname(),
        'cuda_visible_devices': os.environ.get('CUDA_VISIBLE_DEVICES'), 'plan_sha256': digest(plan_path)})
    state = {'stage': 'prepared', 'completed_steps': [], 'slurm_job_id': os.environ['SLURM_JOB_ID']}
    server = None
    telemetry = None
    client = None
    def status(stage, **extra):
        state.update(stage=stage, updated_at=dt.datetime.now(dt.timezone.utc).isoformat(), **extra)
        write(folder / 'status.json', state)
        print(json.dumps(state), flush=True)
    def serve(capacity):
        nonlocal server
        stop(server)
        bind_deadline = time.monotonic() + 30
        while True:
            try:
                with socket.socket() as probe:
                    # Uvicorn uses SO_REUSEADDR too. A closed prior listener's
                    # TIME_WAIT connections must not masquerade as a live server.
                    probe.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                    probe.bind(('127.0.0.1', plan['port']))
                break
            except OSError:
                if time.monotonic() >= bind_deadline:
                    raise
                time.sleep(1)
        command = [str(python), '-m', 'vllm.entrypoints.cli.main', 'serve', str(model_dir),
            '--served-model-name', plan['model'], '--host', '127.0.0.1', '--port', str(plan['port']),
            '--dtype', 'bfloat16', '--tensor-parallel-size', '1', '--gpu-memory-utilization', '0.90',
            '--max-model-len', str(plan['max_model_len']), '--max-num-seqs', str(capacity),
            '--reasoning-parser', 'qwen3', '--enable-prefix-caching',
            '--limit-mm-per-prompt', '{"image": 1, "video": 0}']
        status('starting_server', server_capacity=capacity)
        log = (folder / f'server_capacity_{capacity}.log').open('x')
        server = subprocess.Popen(command, cwd=folder, env=env, stdout=log,
                                  stderr=subprocess.STDOUT, start_new_session=True)
        log.close()
        write(folder / f'server_capacity_{capacity}.json', {'command': command, 'pid': server.pid})
        endpoint = f"http://127.0.0.1:{plan['port']}"
        opener = urllib.request.build_opener(urllib.request.ProxyHandler({}))
        limit = time.monotonic() + 1200
        while time.monotonic() < limit:
            if server.poll() is not None:
                raise RuntimeError('Dedicated benchmark server failed to start; see log')
            try:
                with opener.open(endpoint + '/v1/models', timeout=3) as response:
                    rows = json.load(response)['data']
                if any(row.get('id') == plan['model'] for row in rows):
                    break
            except (OSError, ValueError):
                pass
            time.sleep(2)
        else:
            raise TimeoutError('Dedicated server startup exceeded20 minutes')
        identity = common.own_gpu_processes(server.pid)
        if len({row['gpu_uuid'] for row in identity}) != 1:
            raise ValueError('Server must use exactly one observed GPU')
        write(folder / f'server_capacity_{capacity}_gpu.json', identity)
        status('server_ready', server_capacity=capacity)
    def run_step(step):
        nonlocal client
        if state.get('server_capacity') != step['server_capacity']:
            serve(step['server_capacity'])
        status('benchmarking', active_step=step['name'])
        command = [str(python), str(folder / 'benchmark_vllm_concurrency.py'),
            '--base-url', f"http://127.0.0.1:{plan['port']}", '--model', plan['model'],
            '--output-dir', str(folder / step['name']), '--concurrencies', step['concurrencies'],
            '--requests', str(step['requests']), '--input-tokens', str(step['input_tokens']),
            '--output-tokens', str(step['output_tokens']), '--warmup-requests', '4',
            '--prefix-cache-policy', 'reset-between-levels']
        if plan.get('generation'):
            generation = plan['generation']
            command += ['--temperature', str(generation['temperature']),
                        '--top-p', str(generation['top_p']),
                        '--top-k', str(generation['top_k']),
                        '--generation-seed', str(generation['seed'])]
        with (folder / (step['name'] + '.log')).open('x') as log:
            client = subprocess.Popen(command, cwd=folder, env=env, stdout=log,
                stderr=subprocess.STDOUT, start_new_session=True)
            rc = client.wait()
            client = None
        state['completed_steps'].append({'name': step['name'], 'exit_code': rc})
        if rc:
            raise RuntimeError('Synthetic benchmark client failed: ' + step['name'])
        status('step_completed')
    try:
        with (folder / 'gpu_telemetry.csv').open('x') as log:
            telemetry = subprocess.Popen(['nvidia-smi',
                '--query-gpu=timestamp,index,uuid,utilization.gpu,utilization.memory,memory.used,memory.total,power.draw,temperature.gpu',
                '--format=csv,noheader,nounits', '--loop=2'], stdout=log,
                stderr=subprocess.STDOUT, start_new_session=True)
        for step in plan['steps']:
            run_step(step)
        status('completed')
    except BaseException as error:
        status('failed', error=f'{type(error).__name__}: {error}')
        raise
    finally:
        stop(client)
        stop(server)
        stop(telemetry)


if __name__ == '__main__':
    def terminate(signum, frame):
        raise RuntimeError('Benchmark received signal ' + str(signum))
    signal.signal(signal.SIGTERM, terminate)
    signal.signal(signal.SIGINT, terminate)
    main()
