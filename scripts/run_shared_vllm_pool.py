"""Serve a frozen set of TP1 replicas in one Slurm allocation.

The model and generation contract are unchanged.  A separate, hashed migration
amendment controls which remaining cases may use these loopback replicas.
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
import time


def sha(path):
    h = hashlib.sha256()
    with Path(path).open('rb') as stream:
        for block in iter(lambda: stream.read(8 * 1024 * 1024), b''):
            h.update(block)
    return h.hexdigest()


def write(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + '.tmp')
    temporary.write_text(json.dumps(value, indent=2) + '\n')
    temporary.chmod(0o600)
    temporary.replace(path)


def stop(child, timeout=30):
    if child is None or child.poll() is not None:
        return
    os.killpg(child.pid, signal.SIGTERM)
    try:
        child.wait(timeout=timeout)
    except subprocess.TimeoutExpired:
        os.killpg(child.pid, signal.SIGKILL)
        child.wait(timeout=10)


def load_module(path):
    spec = importlib.util.spec_from_file_location('shared_pool_runtime', path)
    value = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(value)
    return value


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--directory', type=Path, required=True)
    parser.add_argument('--plan-sha256', required=True)
    parser.add_argument('--runtime-dir', type=Path, required=True)
    args = parser.parse_args()
    directory = args.directory.resolve()
    plan_path = directory / 'plan.json'
    if sha(plan_path) != args.plan_sha256:
        raise ValueError('Shared-pool plan changed')
    plan = json.loads(plan_path.read_text())
    if not os.environ.get('SLURM_JOB_ID') or plan['replicas'] not in (4, 8):
        raise ValueError('A single-node four/eight GPU Slurm allocation is required')
    for path, expected in plan['code_sha256'].items():
        if sha(path) != expected:
            raise ValueError('Shared-pool source changed: ' + path)
    local = args.runtime_dir.resolve()
    if not local.name.startswith('bio-shared-'):
        raise ValueError('Expected a private disposable Slurm runtime')
    visible = os.environ.get('CUDA_VISIBLE_DEVICES', '').split(',')
    if len(visible) != plan['replicas'] or any(not item for item in visible):
        raise ValueError('Slurm GPU visibility differs from replica count')
    common = load_module(plan['runtime_common'])
    common.apply_overlay(local)
    base_env = common.environment(local)
    python = local / 'python/bin/python3.12'
    model_directory = common.validate_checkpoint(plan['model'], plan['revision'])
    servers, clients = [], []
    telemetry = None
    stopping = False
    stop_path = directory / 'stop_dispatch.json'
    state = {'slurm_job_id': os.environ['SLURM_JOB_ID'], 'hostname': socket.gethostname(),
             'replicas': plan['replicas'], 'plan_sha256': args.plan_sha256,
             'stage': 'preflight', 'endpoints': []}

    def status(stage, **fields):
        state.update(stage=stage, updated_at=dt.datetime.now(dt.timezone.utc).isoformat(), **fields)
        write(directory / 'status.json', state)
        print(json.dumps(state), flush=True)

    def terminate(signum, frame):
        nonlocal stopping
        stopping = True
        write(stop_path, {'signal': signum, 'at': dt.datetime.now(dt.timezone.utc).isoformat()})

    signal.signal(signal.SIGTERM, terminate)
    signal.signal(signal.SIGINT, terminate)
    signal.signal(signal.SIGUSR1, terminate)
    try:
        status('starting_servers')
        with (directory / 'gpu_telemetry.csv').open('x') as log:
            telemetry = subprocess.Popen(['nvidia-smi',
                '--query-gpu=timestamp,index,uuid,utilization.gpu,memory.used,memory.total,power.draw',
                '--format=csv,noheader,nounits', '--loop=5'], stdout=log,
                stderr=subprocess.STDOUT, start_new_session=True)
        for slot, selected in enumerate(visible):
            replica = directory / f'replica_{slot}'
            replica.mkdir()
            env = dict(base_env, CUDA_VISIBLE_DEVICES=selected, OMP_NUM_THREADS='8',
                       MKL_NUM_THREADS='8', MAX_JOBS='2', VLLM_SERVER_DEV_MODE='1')
            # Separate compilation caches prevent competing replica startups.
            for key, suffix in [('VLLM_CACHE_ROOT', 'vllm'), ('TRITON_CACHE_DIR', 'triton'),
                                ('FLASHINFER_WORKSPACE_BASE', 'flashinfer')]:
                env[key] = str(local / 'cache' / f'replica_{slot}' / suffix)
            port = plan['first_port'] + slot
            with socket.socket() as probe:
                probe.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                probe.bind(('127.0.0.1', port))
            command = [str(python), '-m', 'vllm.entrypoints.cli.main', 'serve', str(model_directory),
                '--served-model-name', plan['model'], '--host', '127.0.0.1', '--port', str(port),
                '--dtype', 'bfloat16', '--tensor-parallel-size', '1', '--gpu-memory-utilization', '0.90',
                '--max-model-len', str(plan['max_model_len']), '--max-num-seqs', str(plan['max_num_seqs']),
                '--reasoning-parser', 'qwen3', '--enable-prefix-caching',
                '--limit-mm-per-prompt', '{"image": 1, "video": 0}']
            with (replica / 'server.log').open('x') as log:
                server = subprocess.Popen(command, cwd=local, env=env, stdout=log,
                                          stderr=subprocess.STDOUT, start_new_session=True)
            servers.append((server, replica, port, env))
            write(replica / 'launch.json', {'command': command, 'pid': server.pid,
                                           'cuda_visible_devices': selected})
        deadline = time.monotonic() + 1500
        ready = set()
        while len(ready) != plan['replicas']:
            if stopping:
                raise RuntimeError('Allocation stopped during setup')
            for slot, (server, replica, port, env) in enumerate(servers):
                if server.poll() is not None:
                    raise RuntimeError(f'Replica {slot} exited during startup')
                if slot in ready:
                    continue
                endpoint = f'http://127.0.0.1:{port}/v1'
                try:
                    models = common.call(endpoint, '/models')
                except (OSError, ValueError):
                    continue
                if not any(row.get('id') == plan['model'] for row in models.get('data', [])):
                    continue
                processes = common.own_gpu_processes(server.pid)
                uuids = sorted({row['gpu_uuid'] for row in processes})
                if len(uuids) != 1:
                    raise ValueError('Replica must own exactly one observed GPU')
                identity = {'model': plan['model'], 'revision': plan['revision'], 'dtype': 'bfloat16',
                    'tensor_parallel_size': 1, 'max_model_len': plan['max_model_len'],
                    'max_num_seqs': plan['max_num_seqs'], 'endpoint': endpoint, 'gpu_uuids': uuids,
                    'hostname': socket.gethostname(), 'pid': server.pid,
                    'proc_start_ticks': common.start_ticks(server.pid), 'slurm_job_id': os.environ['SLURM_JOB_ID'],
                    'observed_gpu_processes': processes,
                    'command': json.loads((replica / 'launch.json').read_text())['command']}
                write(replica / 'server_identity.json', identity)
                common.synthetic_serving(endpoint, plan['model'], replica)
                state['endpoints'].append({'endpoint_id': f'replica_{slot}', 'endpoint': endpoint,
                    'server_identity_file': str(replica / 'server_identity.json'),
                    'server_identity_sha256': sha(replica / 'server_identity.json')})
                ready.add(slot)
                status('starting_servers', ready_replicas=len(ready))
            if time.monotonic() > deadline:
                raise TimeoutError('Shared-pool replica startup exceeded25 minutes')
            time.sleep(2)
        if len({uuid for row in state['endpoints']
                for uuid in json.loads(Path(row['server_identity_file']).read_text())['gpu_uuids']}) != plan['replicas']:
            raise ValueError('Replica GPU UUIDs are not disjoint')
        state['endpoints'].sort(key=lambda row: row['endpoint_id'])
        write(directory / 'endpoints.json', state['endpoints'])
        status('ready_for_benchmark')
        for slot, profile in enumerate(plan.get('benchmark_profiles', [])):
            replica = directory / f'replica_{slot}'
            command = [str(python), plan['length_benchmark_script'], '--plan',
                plan['length_benchmark_plan'], '--profile', str(profile), '--base-url',
                f"http://127.0.0.1:{plan['first_port'] + slot}", '--output-dir',
                str(replica / 'length_benchmark'), '--client-path', plan['benchmark_client']]
            with (replica / 'length_benchmark.log').open('x') as log:
                child = subprocess.Popen(command, cwd=plan['root'], env=base_env, stdout=log,
                                         stderr=subprocess.STDOUT, start_new_session=True)
            clients.append(child)
        if clients:
            status('benchmarking_input_lengths')
            while any(child.poll() is None for child in clients):
                if stopping or any(server.poll() is not None for server, *_ in servers):
                    raise RuntimeError('Allocation stopped during synthetic validation')
                status('benchmarking_input_lengths', benchmark_exit_codes=[child.poll() for child in clients])
                time.sleep(10)
            failed = [child.returncode for child in clients if child.returncode]
            clients.clear()
            # Preserve a healthy server pool for inspection if one synthetic
            # client fails; the dispatch gate still requires a reviewed plan.
            status('benchmark_failed' if failed else 'benchmarks_completed',
                   benchmark_exit_codes=failed)
        # The root creates a frozen dispatch command only after synthetic checks
        # and the migration amendment have passed.  No solver call occurs here.
        while not (directory / 'dispatch.json').is_file():
            if stopping:
                status('drained_before_dispatch')
                return
            if any(server.poll() is not None for server, *_ in servers):
                raise RuntimeError('A replica exited while waiting for dispatch')
            status('ready_for_dispatch')
            time.sleep(10)
        dispatch = json.loads((directory / 'dispatch.json').read_text())
        for path, expected in dispatch['files_sha256'].items():
            if sha(path) != expected:
                raise ValueError('Frozen dispatch dependency changed: ' + path)
        command = [str(python) if arg == '{python}' else arg for arg in dispatch['command']]
        if command[0] != str(python):
            raise ValueError('Dispatch must use the private verified runtime')
        with (directory / 'dispatch.log').open('x') as log:
            child = subprocess.Popen(command, cwd=plan['root'], env=base_env, stdout=log,
                                     stderr=subprocess.STDOUT, start_new_session=True)
        clients.append(child)
        status('evaluating')
        drain_deadline = None
        while child.poll() is None:
            if any(server.poll() is not None for server, *_ in servers):
                write(stop_path, {'reason': 'replica_exited'})
                stopping = True
            if stopping:
                if drain_deadline is None:
                    os.killpg(child.pid, signal.SIGTERM)
                    drain_deadline = time.monotonic() + 105
                    status('draining')
                if time.monotonic() >= drain_deadline:
                    raise TimeoutError('Dispatch drain exceeded preemption grace')
            time.sleep(2)
        if child.returncode:
            raise RuntimeError(f'Shared dispatch exited {child.returncode}')
        status('completed')
    except BaseException as error:
        status('failed', error=f'{type(error).__name__}: {error}')
        raise
    finally:
        for child in reversed(clients):
            stop(child, timeout=5)
        for server, *_ in reversed(servers):
            stop(server, timeout=10)
        stop(telemetry, timeout=5)


if __name__ == '__main__':
    main()
