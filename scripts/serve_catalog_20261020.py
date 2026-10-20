#!/usr/bin/env python3
"""One owned Slurm GPU serves separately frozen, root-queued catalog tasks."""
import argparse
import datetime
import fcntl
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import signal
import socket
import subprocess
import sys
import tarfile
import tempfile
import time
import urllib.request
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / '.local/catalog_execution_2026-10-20/runtime'


def stamp():
    return datetime.datetime.now(ZoneInfo('America/Los_Angeles')).isoformat()


def sha(path):
    h = hashlib.sha256()
    with Path(path).open('rb') as f:
        for chunk in iter(lambda: f.read(8 * 1024 * 1024), b''):
            h.update(chunk)
    return h.hexdigest()


def write(path, value):
    path = Path(path)
    tmp = path.with_suffix(path.suffix + '.tmp')
    tmp.write_text(json.dumps(value, indent=2) + '\n')
    tmp.chmod(0o600)
    tmp.replace(path)


def load_common(plan):
    path = Path(plan['runtime_common'])
    if sha(path) != plan['runtime_common_sha256']:
        raise ValueError('Runtime support changed')
    spec = importlib.util.spec_from_file_location('catalog_runtime_common', path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def environment(common, runtime):
    env = common.environment(runtime)
    for key in list(env):
        upper = key.upper()
        if upper.endswith(('API_KEY', 'API_TOKEN')) or upper in {
            'HF_TOKEN', 'HUGGING_FACE_HUB_TOKEN', 'OPENAI_BASE_URL',
            'OPENAI_ORG_ID', 'OPENAI_ORGANIZATION', 'OPENAI_PROJECT_ID',
            'PYTHONPATH', 'PYTHONHOME', 'VIRTUAL_ENV', 'AZURE_OPENAI_ENDPOINT',
        }:
            env.pop(key, None)
    env.update(HF_HUB_OFFLINE='1', TRANSFORMERS_OFFLINE='1',
               PYTHONNOUSERSITE='1', OMP_NUM_THREADS='10', MKL_NUM_THREADS='10')
    return env


def package_identity(python, env, gpu=False):
    code = "import importlib.metadata as m,json,platform; x={'python':platform.python_version(),'packages':{n:m.version(n) for n in ['vllm','torch','transformers','triton','flashinfer-python']}}; "
    if gpu:
        code += "import torch; x.update(gpu_count=torch.cuda.device_count(),gpu_name=torch.cuda.get_device_name(0),torch_cuda=torch.version.cuda); "
    code += 'print(json.dumps(x))'
    return json.loads(subprocess.check_output([str(python), '-c', code], env=env, text=True, timeout=120))


def obtain_runtime(plan, common):
    candidates = [Path(p) for p in plan['reusable_runtime_paths']]
    candidates += sorted(Path('/tmp').glob('bio-gfp-development-*'))
    for runtime in candidates:
        python = runtime / 'python/bin/python3.12'
        if not python.is_file() or runtime.stat().st_uid != os.getuid():
            continue
        try:
            env = environment(common, runtime)
            info = package_identity(python, env)
            if info['packages']['vllm'] != '0.32.0':
                continue
            subprocess.run([str(python), '-m', 'pip', 'check'], env=env,
                           stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
                           timeout=120, check=True)
            return runtime, env, {'source': 'verified_cached_runtime', **info}
        except (OSError, ValueError, subprocess.SubprocessError):
            continue
    runtime = Path(tempfile.mkdtemp(prefix='bio-catalog-' + os.environ['SLURM_JOB_ID'] + '-',
                                   dir=os.environ.get('SLURM_TMPDIR', '/tmp')))
    runtime.chmod(0o700)
    for key in ('base_runtime', 'cuda_overlay'):
        if sha(plan[key]['path']) != plan[key]['sha256']:
            raise ValueError('Runtime archive changed: ' + key)
    with tarfile.open(plan['base_runtime']['path']) as archive:
        archive.extractall(runtime, filter='data')
    overlay = common.apply_overlay(runtime)
    env = environment(common, runtime)
    python = runtime / 'python/bin/python3.12'
    with (BASE / 'runtime_install.log').open('x') as log:
        subprocess.run([str(python), '-m', 'pip', 'install', '--index-url',
                        'https://pypi.org/simple', '--only-binary=:all:',
                        '--break-system-packages', '--upgrade', 'vllm==0.32.0',
                        'torch==2.13.0', 'transformers==5.17.0', 'triton==3.7.1',
                        'flashinfer-python==0.7.0.post1', '--report',
                        str(BASE / 'pip_install_report.json')], env=env,
                       stdout=log, stderr=subprocess.STDOUT, check=True, timeout=2400)
    with (BASE / 'pip_check.log').open('x') as log:
        subprocess.run([str(python), '-m', 'pip', 'check'], env=env,
                       stdout=log, stderr=subprocess.STDOUT, check=True, timeout=120)
    return runtime, env, {'source': 'verified_archive_and_pinned_install',
                          'overlay': overlay, **package_identity(python, env)}


def call(endpoint, suffix, payload=None):
    opener = urllib.request.build_opener(urllib.request.ProxyHandler({}))
    data = None if payload is None else json.dumps(payload).encode()
    request = urllib.request.Request(endpoint + suffix, data=data,
                                     headers={'Content-Type': 'application/json'})
    with opener.open(request, timeout=120 if payload else 5) as response:
        return json.load(response)


def validate_grant(grant, plan):
    if grant.get('authorized') is not True:
        raise ValueError('Explicit exact-task execution grant required')
    if grant['task_id'] not in plan['authorized_task_ids']:
        raise ValueError('Task is not in the authorized seven')
    runner = Path(grant['runner']).resolve()
    if str(runner.relative_to(ROOT)) not in plan['allowed_runner_paths']:
        raise ValueError('Runner not allowlisted')
    config = Path(grant['config']).resolve()
    expected_dir = ROOT / '.local/catalog_execution_2026-10-20/tasks' / grant['task_id']
    if not config.is_relative_to(expected_dir):
        raise ValueError('Task config outside its separate directory')
    if sha(runner) != grant['runner_sha256'] or sha(config) != grant['config_sha256']:
        raise ValueError('Frozen runner or configuration changed')
    if grant['phase'] not in ('development', 'benchmark'):
        raise ValueError('Unknown phase')
    if grant['phase'] == 'benchmark':
        completion = Path(grant['development_completion'])
        if not completion.resolve().is_relative_to(expected_dir):
            raise ValueError('Development evidence outside task directory')
        if sha(completion) != grant['development_completion_sha256']:
            raise ValueError('Development gate changed')
        result = json.loads(completion.read_text())
        if (result.get('phase') != 'development' or result.get('all_passed') is not True
                or not result.get('planned')
                or result['delivery_passed'] != result['planned']
                or any(result.get(k, 0) for k in ('empty_finals', 'truncations', 'transport_or_response_errors'))):
            raise ValueError('Task development delivery did not pass')
    argv = grant['argv']
    if not isinstance(argv, list) or any(type(x) is not str for x in argv):
        raise ValueError('Expected literal runner argument list')
    if str(config) not in argv or grant.get('endpoint') != plan['endpoint']:
        raise ValueError('Runner arguments omit frozen config or grant selects another endpoint')
    if Path(grant['server_identity_file']).resolve() != BASE / 'server_identity.json':
        raise ValueError('Grant does not use the owned server identity')
    if sha(grant['server_identity_file']) != grant['server_identity_sha256']:
        raise ValueError('Server identity changed')
    return runner


def execute(args):
    os.umask(0o077)
    if sha(args.plan) != args.plan_sha256:
        raise ValueError('Infrastructure plan changed')
    plan = json.loads(args.plan.read_text())
    if sha(__file__) != plan['worker_sha256']:
        raise ValueError('Infrastructure code changed after submission')
    if not os.environ.get('SLURM_JOB_ID') or plan['gpus_requested'] != 1:
        raise ValueError('Dedicated one-GPU Slurm allocation required')
    lock = (BASE / 'pool.lock').open('a')
    fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
    if (BASE / 'execution_started.json').exists():
        raise ValueError('Pool already started; no implicit restart')
    write(BASE / 'execution_started.json', {'at_pacific': stamp(), 'job_id': os.environ['SLURM_JOB_ID'],
          'plan_sha256': args.plan_sha256})
    state = {'stage': 'runtime_preparation', 'job_id': os.environ['SLURM_JOB_ID'],
             'hostname': socket.gethostname(), 'updated_at_pacific': stamp(),
             'benchmark_calls_by_pool_controller': 0, 'gpus_requested': 1}
    write(BASE / 'status.json', state)
    common = load_common(plan)
    model = common.validate_checkpoint(plan['model'], plan['revision'])
    runtime, env, info = obtain_runtime(plan, common)
    python = runtime / 'python/bin/python3.12'
    gpu = package_identity(python, env, gpu=True)
    if gpu['gpu_count'] != 1 or 'A100' not in gpu['gpu_name']:
        raise ValueError('Expected exactly one allocated A100')
    write(BASE / 'runtime_version_manifest.json', {**info, **gpu,
          'runtime': str(runtime), 'recorded_at_pacific': stamp(), 'api_credentials_removed': True})
    with socket.socket() as probe:
        probe.bind(('127.0.0.1', plan['port']))
    command = [str(python), '-m', 'vllm.entrypoints.cli.main', 'serve', str(model),
               '--served-model-name', plan['model'], '--host', '127.0.0.1',
               '--port', str(plan['port']), '--dtype', 'bfloat16',
               '--tensor-parallel-size', '1', '--gpu-memory-utilization', '0.95',
               '--max-model-len', '65536', '--max-num-seqs', '128',
               '--max-num-batched-tokens', '8192', '--enable-prefix-caching',
               '--reasoning-parser', 'qwen3']
    server = None
    clients = {}
    try:
        state.update(stage='starting_server', updated_at_pacific=stamp())
        write(BASE / 'status.json', state)
        with (BASE / 'server.log').open('x') as log:
            server = subprocess.Popen(command, cwd=runtime, env=env, stdout=log,
                                      stderr=subprocess.STDOUT, start_new_session=True)
        deadline = time.monotonic() + 1500
        while time.monotonic() < deadline:
            if server.poll() is not None:
                raise RuntimeError('Server exited during startup')
            try:
                listed = call(plan['endpoint'], '/models')
                if plan['model'] in {x['id'] for x in listed['data']}:
                    break
            except (OSError, ValueError, KeyError):
                pass
            time.sleep(2)
        else:
            raise TimeoutError('Local server startup deadline')
        identity = {'model': plan['model'], 'revision': plan['revision'], 'dtype': 'bfloat16',
                    'endpoint': plan['endpoint'], 'hostname': socket.gethostname(),
                    'job_id': os.environ['SLURM_JOB_ID'], 'pid': server.pid,
                    'proc_start_ticks': common.start_ticks(server.pid), 'dedicated_gpu_count': 1,
                    'max_model_len': 65536, 'command': command, 'recorded_at_pacific': stamp()}
        write(BASE / 'server_identity.json', identity)
        synthetic = call(plan['endpoint'], '/chat/completions', {
            'model': plan['model'], 'messages': [{'role': 'user', 'content': 'Return the number -1.25 only.'}],
            'temperature': 0, 'max_tokens': 32, 'chat_template_kwargs': {'enable_thinking': False},
            'structured_outputs': {'regex': r'-?[0-9]+(?:\.[0-9]+)?'}})
        write(BASE / 'synthetic_delivery.json', synthetic)
        choice = synthetic['choices'][0]
        if choice['finish_reason'] != 'stop' or choice['message'].get('content', '').strip() != '-1.25':
            raise ValueError('Synthetic nonthinking structured output check failed')
        queue = Path(plan['queue_root'])
        while not (BASE / 'STOP').exists():
            if server.poll() is not None:
                raise RuntimeError('Local server exited')
            for key, item in list(clients.items()):
                process = item['process']
                if process.poll() is not None:
                    item['log'].close()
                    write(queue / (key + '.finished.json'), {'exit_code': process.returncode,
                          'finished_at_pacific': stamp(), 'grant_sha256': item['grant_sha256']})
                    del clients[key]
            for path in sorted(queue.glob('*.grant.json')):
                if len(clients) >= plan['max_simultaneous_clients']:
                    break
                key = path.name.removesuffix('.grant.json')
                if (queue / (key + '.started.json')).exists() or (queue / (key + '.rejected.json')).exists():
                    continue
                try:
                    grant = json.loads(path.read_text())
                    runner = validate_grant(grant, plan)
                    digest = sha(path)
                    write(queue / (key + '.started.json'), {'started_at_pacific': stamp(),
                          'grant_sha256': digest, 'task_id': grant['task_id'], 'phase': grant['phase']})
                    log = (queue / (key + '.log')).open('x')
                    process = subprocess.Popen([str(python), str(runner), *grant['argv']],
                                               cwd=ROOT, env=env, stdout=log, stderr=subprocess.STDOUT,
                                               start_new_session=True)
                    clients[key] = {'process': process, 'log': log, 'grant_sha256': digest}
                except Exception as error:
                    write(queue / (key + '.rejected.json'), {'at_pacific': stamp(),
                          'error_type': type(error).__name__, 'error': str(error)})
            state.update(stage='serving_task_queue', updated_at_pacific=stamp(),
                         active_clients=list(clients), endpoint=plan['endpoint'],
                         runtime=str(runtime), server_pid=server.pid)
            write(BASE / 'status.json', state)
            time.sleep(5)
        state.update(stage='stopped_by_control', updated_at_pacific=stamp())
        write(BASE / 'status.json', state)
    finally:
        for item in clients.values():
            process = item['process']
            if process.poll() is None:
                os.killpg(process.pid, signal.SIGTERM)
        if server is not None and server.poll() is None:
            os.killpg(server.pid, signal.SIGTERM)
            try:
                server.wait(timeout=30)
            except subprocess.TimeoutExpired:
                os.killpg(server.pid, signal.SIGKILL)
                server.wait(timeout=15)
        write(BASE / 'cleanup.json', {'at_pacific': stamp(), 'owned_processes_only': True,
              'server_exit_code': None if server is None else server.poll()})


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--plan', type=Path, required=True)
    parser.add_argument('--plan-sha256', required=True)
    args = parser.parse_args()
    def stop(_signal, _frame):
        raise SystemExit('Stopped by Slurm or operator')
    signal.signal(signal.SIGTERM, stop)
    signal.signal(signal.SIGINT, stop)
    try:
        execute(args)
    except Exception as error:
        write(BASE / 'error.json', {'at_pacific': stamp(), 'error_type': type(error).__name__,
              'error': str(error)})
        raise


if __name__ == '__main__':
    main()
