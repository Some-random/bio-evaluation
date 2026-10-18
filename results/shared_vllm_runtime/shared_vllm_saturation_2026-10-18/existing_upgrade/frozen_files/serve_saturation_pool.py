"""Start additional isolated TP1 replicas; dispatch only after reviewed gates.

Signals stop new dispatcher admissions and wait for all outstanding requests.
There is deliberately no local deadline that kills a scored HTTP call.
"""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import re
import signal
import socket
import subprocess
import time
import urllib.request


def sha(path):
    value = hashlib.sha256()
    with Path(path).open('rb') as stream:
        for block in iter(lambda: stream.read(8 * 1024 * 1024), b''):
            value.update(block)
    return value.hexdigest()


def write(path, value):
    path = Path(path)
    temporary = path.with_suffix(path.suffix + '.tmp')
    temporary.write_text(json.dumps(value, indent=2) + '\n')
    temporary.chmod(0o600)
    temporary.replace(path)


def module(path):
    spec = importlib.util.spec_from_file_location('saturation_serving_common', path)
    value = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(value)
    return value


def verify_files(files):
    if not files:
        raise ValueError('A reviewed gate must pin its dependencies')
    for name, expected in files.items():
        if sha(name) != expected:
            raise ValueError('Pinned dependency changed: ' + name)


def checked_command(gate, python):
    verify_files(gate['files_sha256'])
    command = [str(python) if arg == '{python}' else arg for arg in gate['command']]
    if not command or command[0] != str(python):
        raise ValueError('Dispatcher must use the verified private Python')
    return command


def server_command(python, checkpoint, plan, port):
    return [str(python), '-m', 'vllm.entrypoints.cli.main', 'serve', str(checkpoint),
        '--served-model-name', plan['model'], '--host', '127.0.0.1', '--port', str(port),
        '--dtype', 'bfloat16', '--tensor-parallel-size', '1',
        '--gpu-memory-utilization', str(plan['gpu_memory_utilization']),
        '--max-model-len', str(plan['max_model_len']),
        '--max-num-seqs', str(plan['max_num_seqs']),
        '--max-num-batched-tokens', str(plan['max_num_batched_tokens']),
        '--reasoning-parser', 'qwen3', '--enable-prefix-caching',
        '--limit-mm-per-prompt', '{"image": 1, "video": 0}']


def parse_queue_metrics(raw):
    values = {'running': [], 'waiting': []}
    for line in raw.splitlines():
        for state in values:
            if re.match(r'vllm:num_requests_' + state + r'(?:\{|\s)', line):
                values[state].append(float(line.split()[-1]))
    if any(not values[state] for state in values):
        raise ValueError('Server metrics do not expose both request counters')
    return {state: sum(rows) for state, rows in values.items()}


def queue_metrics(endpoint):
    opener = urllib.request.build_opener(urllib.request.ProxyHandler({}))
    with opener.open(endpoint.removesuffix('/v1') + '/metrics', timeout=10) as response:
        return parse_queue_metrics(response.read().decode())


def validate_plan(plan):
    if not 1 <= plan['replicas'] <= 4:
        raise ValueError('This additive pool supports at most four spare GPUs')
    if (plan['model'] != 'Qwen/Qwen3.8-27B'
            or plan['revision'] != '1d4bf0f2ff6012fd82039f2fa52739d0dd7c60c0'
            or plan['max_model_len'] != 65536 or plan['max_num_seqs'] not in (128, 256)
            or plan['max_num_batched_tokens'] != 8192
            or plan['gpu_memory_utilization'] != 0.95):
        raise ValueError('Serving plan differs from the authorized infrastructure profile')
    if plan['existing_project_gpu_count'] + plan['replicas'] > 8:
        raise ValueError('Planned project GPUs exceed eight')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--directory', type=Path, required=True)
    parser.add_argument('--plan-sha256', required=True)
    parser.add_argument('--runtime-dir', type=Path, required=True)
    args = parser.parse_args()
    directory, local = args.directory.resolve(), args.runtime_dir.resolve()
    plan_path = directory / 'saturation_serving_plan.json'
    if sha(plan_path) != args.plan_sha256:
        raise ValueError('Serving plan changed')
    plan = json.loads(plan_path.read_text())
    validate_plan(plan)
    verify_files(plan['code_sha256'])
    if (not os.environ.get('SLURM_JOB_ID') or not local.name.startswith('bio-saturation-')
            or (directory / 'serving_status.json').exists()):
        raise ValueError('Expected a fresh private Slurm saturation runtime')
    visible = os.environ.get('CUDA_VISIBLE_DEVICES', '').split(',')
    if len(visible) != plan['replicas'] or any(not item for item in visible) or len(set(visible)) != len(visible):
        raise ValueError('Slurm GPU visibility differs from independent replica count')
    common = module(plan['runtime_common'])
    env = common.environment(local)
    python = local / 'python/bin/python3.12'
    checkpoint = common.validate_checkpoint(plan['model'], plan['revision'])
    package_code = "import importlib.metadata as m,json,sys,torch;print(json.dumps({'python':sys.version,'torch_build':torch.__version__,'torch_cuda':torch.version.cuda,'visible_gpu_count':torch.cuda.device_count(),'devices':[{'name':torch.cuda.get_device_name(i),'total_memory':torch.cuda.get_device_properties(i).total_memory,'capability':list(torch.cuda.get_device_capability(i))} for i in range(torch.cuda.device_count())],'packages':{n:m.version(n) for n in ['vllm','torch','transformers','triton','flashinfer-python']}}))"
    packages = json.loads(subprocess.check_output([str(python), '-c', package_code], env=env, text=True))
    if packages['packages']['vllm'] != plan['expected_vllm_version'] or packages['visible_gpu_count'] != plan['replicas']:
        raise ValueError('Runtime version or observed GPU count differs from plan')
    write(directory / 'saturation_execution_environment.json', packages)
    servers, child, telemetry = [], None, None
    stopping, signal_sent = False, False
    state = {'schema_version': 1, 'hostname': socket.gethostname(),
             'slurm_job_id': os.environ['SLURM_JOB_ID'], 'plan_sha256': args.plan_sha256,
             'runtime_directory': str(local), 'replicas': plan['replicas'], 'endpoints': []}

    def status(stage, **extra):
        state.update(stage=stage, updated_at=dt.datetime.now(dt.timezone.utc).isoformat(), **extra)
        write(directory / 'serving_status.json', state)
        print(json.dumps(state), flush=True)

    def terminate(signum, frame):
        nonlocal stopping
        stopping = True
        write(directory / 'stop_dispatch.json', {'signal': signum, 'at': dt.datetime.now(dt.timezone.utc).isoformat()})

    def idle_servers():
        rows = []
        for server, replica, port in servers:
            if server.poll() is None:
                rows.append(queue_metrics(f'http://127.0.0.1:{port}/v1'))
        return all(row['running'] == row['waiting'] == 0 for row in rows)

    for signum in (signal.SIGTERM, signal.SIGINT, signal.SIGUSR1):
        signal.signal(signum, terminate)
    try:
        status('starting_servers')
        with (directory / 'saturation_gpu_telemetry.csv').open('x') as log:
            telemetry = subprocess.Popen(['nvidia-smi', '--query-gpu=timestamp,index,uuid,utilization.gpu,memory.used,memory.total,power.draw', '--format=csv,noheader,nounits', '--loop=5'], stdout=log, stderr=subprocess.STDOUT, start_new_session=True)
        for slot, gpu in enumerate(visible):
            replica = directory / f'saturation_replica_{slot}'
            replica.mkdir()
            replica_env = dict(env, CUDA_VISIBLE_DEVICES=gpu, OMP_NUM_THREADS='8', MKL_NUM_THREADS='8', MAX_JOBS='2', VLLM_SERVER_DEV_MODE='1')
            for key, suffix in [('VLLM_CACHE_ROOT', 'vllm'), ('TRITON_CACHE_DIR', 'triton'), ('FLASHINFER_WORKSPACE_BASE', 'flashinfer')]:
                replica_env[key] = str(local / 'cache' / f'saturation_replica_{slot}' / suffix)
            port = plan['first_port'] + slot
            with socket.socket() as probe:
                probe.bind(('127.0.0.1', port))
            command = server_command(python, checkpoint, plan, port)
            with (replica / 'server.log').open('x') as log:
                server = subprocess.Popen(command, cwd=local, env=replica_env, stdout=log, stderr=subprocess.STDOUT, start_new_session=True)
            servers.append((server, replica, port))
            write(replica / 'launch.json', {'command': command, 'pid': server.pid, 'cuda_visible_devices': gpu})
        ready, deadline = set(), time.monotonic() + 1800
        while len(ready) != plan['replicas']:
            if stopping:
                return
            for slot, (server, replica, port) in enumerate(servers):
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
                    raise ValueError('Each replica must own exactly one observed GPU')
                identity = {'model': plan['model'], 'revision': plan['revision'], 'dtype': 'bfloat16',
                    'tensor_parallel_size': 1, 'max_model_len': plan['max_model_len'],
                    'max_num_seqs': plan['max_num_seqs'], 'max_num_batched_tokens': plan['max_num_batched_tokens'],
                    'gpu_memory_utilization': plan['gpu_memory_utilization'], 'vllm_version': packages['packages']['vllm'],
                    'runtime_environment_sha256': sha(directory / 'saturation_execution_environment.json'),
                    'endpoint': endpoint, 'gpu_uuids': uuids, 'hostname': socket.gethostname(),
                    'pid': server.pid, 'proc_start_ticks': common.start_ticks(server.pid),
                    'slurm_job_id': os.environ['SLURM_JOB_ID'], 'observed_gpu_processes': processes,
                    'command': json.loads((replica / 'launch.json').read_text())['command']}
                write(replica / 'server_identity.json', identity)
                common.synthetic_serving(endpoint, plan['model'], replica)
                state['endpoints'].append({'endpoint_id': f'saturation_{slot}', 'endpoint': endpoint,
                    'server_identity_file': str(replica / 'server_identity.json'),
                    'server_identity_sha256': sha(replica / 'server_identity.json')})
                ready.add(slot)
                status('starting_servers', ready_replicas=len(ready))
            if time.monotonic() > deadline:
                raise TimeoutError('Replica readiness exceeded thirty minutes')
            time.sleep(2)
        if len({uuid for row in state['endpoints'] for uuid in json.loads(Path(row['server_identity_file']).read_text())['gpu_uuids']}) != plan['replicas']:
            raise ValueError('Replica GPU UUIDs overlap')
        state['endpoints'].sort(key=lambda row: row['endpoint_id'])
        endpoint_file = directory / 'saturation_endpoints.json'
        write(endpoint_file, state['endpoints'])
        status('ready_for_benchmark', endpoints_sha256=sha(endpoint_file))
        while not (directory / 'benchmarks_passed.json').is_file():
            if stopping:
                return
            if any(server.poll() is not None for server, *_ in servers):
                raise RuntimeError('Replica exited before benchmark acceptance')
            time.sleep(2)
        gate = json.loads((directory / 'benchmarks_passed.json').read_text())
        if gate.get('passed') is not True or gate.get('endpoints_sha256') != sha(endpoint_file):
            raise ValueError('Benchmark gate does not accept these exact endpoints')
        verify_files(gate['files_sha256'])
        status('ready_for_dispatch', benchmark_gate_sha256=sha(directory / 'benchmarks_passed.json'))
        while not (directory / 'saturation_dispatch.json').is_file():
            if stopping:
                return
            if any(server.poll() is not None for server, *_ in servers):
                raise RuntimeError('Replica exited while awaiting dispatch')
            time.sleep(2)
        dispatch_path = directory / 'saturation_dispatch.json'
        command = checked_command(json.loads(dispatch_path.read_text()), python)
        if not idle_servers():
            raise ValueError('Inference is already queued on a proposed dispatch endpoint')
        with (directory / 'saturation_dispatch.log').open('x') as log:
            child = subprocess.Popen(command, cwd=plan['root'], env=env, stdout=log, stderr=subprocess.STDOUT, start_new_session=True)
        status('evaluating', dispatch_pid=child.pid, dispatch_gate_sha256=sha(dispatch_path))
        while child.poll() is None:
            if any(server.poll() is not None for server, *_ in servers):
                stopping = True
            if stopping and not signal_sent:
                os.killpg(child.pid, signal.SIGTERM)
                signal_sent = True
                status('draining', drain_policy='stop_new_admissions_then_wait_for_all_http_calls')
            time.sleep(2)
        status('dispatch_returned', dispatcher_exit_code=child.returncode)
        if child.returncode:
            raise RuntimeError(f'Dispatcher exited {child.returncode}; preserved outputs are not retried')
        status('completed_or_paused', dispatcher_exit_code=0)
    except BaseException as error:
        status('failed', error=f'{type(error).__name__}: {error}')
        raise
    finally:
        if child is not None and child.poll() is None:
            if not signal_sent:
                os.killpg(child.pid, signal.SIGTERM)
            child.wait()  # Never discard a scored response after a local timeout.
        # A failed startup/synthetic call may leave a queued request. Preserve it
        # until idle rather than terminating the engine under an active call.
        while True:
            try:
                if idle_servers():
                    break
            except (OSError, ValueError):
                if all(server.poll() is not None for server, *_ in servers):
                    break
            time.sleep(2)
        for server, *_ in reversed(servers):
            if server.poll() is None:
                os.killpg(server.pid, signal.SIGTERM)
                server.wait()
        if telemetry is not None and telemetry.poll() is None:
            os.killpg(telemetry.pid, signal.SIGTERM)
            telemetry.wait()


if __name__ == '__main__':
    main()
