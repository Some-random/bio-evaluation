"""Run a frozen batch of reviewed text benchmark shards on one Slurm GPU.

The vLLM process and its local runtime remain alive across the batch. Each
benchmark's own frozen executor/scorer owns its result format and aggregation.
This process never rewrites inputs, configs, labels, or native completion files.
"""
from __future__ import annotations

import argparse
import datetime as dt
import fcntl
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import re
import signal
import socket
import subprocess
import sys
import time
import zipfile

ROOT = Path(__file__).resolve().parents[2]
POOL = ROOT / '.local/remaining_evaluations'
ARTIFACTS = ROOT / '.local/litqa2_replay'
ALLOWED_TASKS = {'P03', 'P07', 'P08', 'P12', 'P13', 'P14', 'P15', 'P16', 'P28', 'P29'}
ALLOWED_PORTS = set(range(8026, 8034))
ACTIVE_CHILDREN = []


def sha(path):
    h = hashlib.sha256()
    with Path(path).open('rb') as handle:
        for block in iter(lambda: handle.read(8 * 1024 * 1024), b''):
            h.update(block)
    return h.hexdigest()


def digest(value):
    return hashlib.sha256(json.dumps(value, ensure_ascii=False, sort_keys=True,
                                    separators=(',', ':')).encode()).hexdigest()


def write(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + '.tmp')
    temporary.write_text(json.dumps(value, indent=2) + '\n')
    temporary.chmod(0o600)
    temporary.replace(path)


def load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def validate_plan(plan, worker_id):
    if plan.get('schema_version') != 1 or plan.get('execution_authorized') is not True:
        raise ValueError('A frozen authorized v1 batch plan is required')
    workers = plan.get('workers', [])
    if not 1 <= len(workers) <= 8:
        raise ValueError('The user-authorized ceiling is eight one-GPU workers')
    ids = [row['worker_id'] for row in workers]
    ports = [row['port'] for row in workers]
    if len(ids) != len(set(ids)) or len(ports) != len(set(ports)):
        raise ValueError('Worker IDs and loopback ports must be unique')
    if not set(ports) <= ALLOWED_PORTS:
        raise ValueError('Unexpected loopback port')
    run_ids = []
    for worker in workers:
        if worker.get('gpu_count') != 1 or worker.get('tensor_parallel_size') != 1:
            raise ValueError('Every worker must request exactly one GPU')
        if not 4096 < worker['max_model_len'] <= 262144:
            raise ValueError('Invalid bounded model context')
        if not worker.get('entries'):
            raise ValueError('Empty GPU batch')
        for entry in worker['entries']:
            if entry['task_id'] not in ALLOWED_TASKS:
                raise ValueError('Task has no reviewed text benchmark contract')
            if not re.fullmatch(r'[A-Za-z0-9_.-]+', entry['run_id']):
                raise ValueError('Run ID is not a safe isolated file component')
            run_ids.append(entry['run_id'])
            if not entry.get('commands') or any(not re.fullmatch(r'[a-z][a-z0-9_]*', command.get('label', '')) for command in entry['commands']):
                raise ValueError('Each entry needs named frozen commands')
            if entry.get('completion_file', 'completion.json') != 'completion.json':
                raise ValueError('Expected the native completion.json record')
    if len(run_ids) != len(set(run_ids)):
        raise ValueError('A run may belong to exactly one worker')
    chosen = [row for row in workers if row['worker_id'] == worker_id]
    if len(chosen) != 1:
        raise ValueError('Worker is not in the frozen plan')
    return chosen[0]


def validate_artifacts(plan):
    for path, expected in plan['infrastructure_files_sha256'].items():
        if sha(path) != expected:
            raise ValueError('Frozen infrastructure changed: ' + path)
    if str(Path(__file__).resolve()) not in plan['infrastructure_files_sha256']:
        raise ValueError('Worker source is not frozen in plan')
    for receipt_name, expected in plan['runtime_artifacts'].items():
        receipt = json.loads((ARTIFACTS / receipt_name).read_text())
        artifact = Path(receipt['archive_path'])
        stat = artifact.stat()
        if (receipt['sha256'] != expected['sha256']
                or (stat.st_size, stat.st_mtime_ns) != (expected['bytes'], expected['mtime_ns'])):
            raise ValueError('Verified runtime artifact changed')
    extra_pythonpath(plan)
    wheel_overlays(plan)


def extra_pythonpath(owner):
    extra = owner.get('cpu_extra_pythonpath')
    if not extra:
        return []
    receipt_path = Path(extra['receipt']).resolve()
    if not receipt_path.is_relative_to(POOL) or sha(receipt_path) != extra['receipt_sha256']:
        raise ValueError('Scoring dependency receipt changed')
    receipt = json.loads(receipt_path.read_text())
    target = Path(receipt['target_directory']).resolve()
    paths = [Path(path).resolve() for path in extra['paths']]
    if not target.is_relative_to(POOL) or not paths or any(not path.is_relative_to(target) for path in paths):
        raise ValueError('Scoring dependency path escapes the isolated project')
    for relative, expected in receipt['installed_files_sha256'].items():
        path = (target / relative).resolve()
        if not path.is_relative_to(target) or sha(path) != expected:
            raise ValueError('Scoring dependency file changed: ' + relative)
    return [str(path) for path in paths]


def wheel_overlays(owner, target=None):
    paths = []
    for record in owner.get('cpu_wheel_overlays', []):
        path = Path(record['path']).resolve()
        if not path.is_relative_to(POOL) or path.suffix != '.whl' or sha(path) != record['sha256']:
            raise ValueError('CPU wheel path or publisher hash mismatch')
        paths.append(path)
    if target is None or not paths:
        return []
    target = Path(target).resolve()
    target.mkdir(parents=True, exist_ok=True)
    for path in paths:
        with zipfile.ZipFile(path) as archive:
            for member in archive.infolist():
                relative = Path(member.filename)
                if relative.is_absolute() or '..' in relative.parts:
                    raise ValueError('Unsafe wheel member')
                # Wheels used here are ordinary site-packages distributions.
                # Refuse unsupported data-layout wheels instead of misinstalling.
                if any(part.endswith('.data') for part in relative.parts):
                    raise ValueError('CPU wheel requires an unsupported data install scheme')
            archive.extractall(target)
    return [str(target)]


def entry_path(entry, value):
    root = Path(entry['project_root']).resolve()
    if not root.is_relative_to(POOL) or root == POOL:
        raise ValueError('Project root must be an isolated remaining-evaluations project')
    path = Path(value)
    path = path.resolve() if path.is_absolute() else (root / path).resolve()
    if not path.is_relative_to(root):
        raise ValueError('Path escapes the isolated task project')
    return path


def prepare_entry(entry, worker, model_dir, common, folder):
    root = Path(entry['project_root']).resolve()
    config_path = entry_path(entry, entry['config_path'])
    if sha(config_path) != entry['config_sha256']:
        raise ValueError('Frozen configuration changed: ' + str(config_path))
    settings = json.loads(config_path.read_text())
    if (settings['run_id'] != entry['run_id']
            or settings['approved_task_ids'] != [entry['task_id']]
            or settings['gpu_ids'] != [0]
            or settings['endpoint'] != f"http://127.0.0.1:{worker['port']}/v1"
            or digest(settings['generation']) != entry['generation_sha256']
            or settings.get('tool_access', []) != []):
        raise ValueError('Configuration differs from the frozen worker/task/generation contract')
    if settings['model'] != worker['model'] or settings['model_revision'] != worker['model_revision']:
        raise ValueError('A batch must use the same verified checkpoint')
    if settings.get('concurrency') != 4:
        raise ValueError('Frozen inference concurrency must remain four')
    for name, expected in entry.get('command_files_sha256', {}).items():
        if sha(entry_path(entry, name)) != expected:
            raise ValueError('Frozen executor/scorer changed: ' + name)
    for command in entry['commands']:
        command_for(command, entry, Path('/isolated/python'))
    runner_path = entry_path(entry, settings['runner'])
    if sha(runner_path) != entry['runner_sha256']:
        raise ValueError('Frozen runner changed')
    prior = sys.path[:]
    sys.path.insert(0, str(root / 'scripts'))
    try:
        module = load_module('runner_' + entry['run_id'].replace('-', '_'), runner_path)
        checked, cases = module.read_frozen_config(config_path)
    finally:
        sys.path[:] = prior
    if checked != settings or len(cases) != entry['case_count']:
        raise ValueError('Native runner case validation changed the frozen task')
    if sha(entry_path(entry, settings['input_file'])) != entry['input_sha256']:
        raise ValueError('Full native input bytes differ')
    for case in cases:
        for message in case['messages']:
            parts = message['content']
            if isinstance(parts, list) and any(part.get('type') == 'image_url' for part in parts):
                raise ValueError('This batch is restricted to reviewed text-only tasks')
    result_dir = root / 'results/runs' / settings['run_id']
    if (result_dir / 'completion.json').exists():
        raise ValueError('Previously terminal run cannot be retried')
    # Existing requests could have executed without a saved response; never resample.
    if any(next((result_dir / kind).glob('*.json'), None) is not None for kind in ('requests', 'responses')):
        raise ValueError('Run already contains inference artifacts')
    context = common.context_preflight(cases, settings, model_dir, worker['max_model_len'], folder)
    record = entry_path(entry, settings.get('server_record_file', '.local/local_model_server.json'))
    return {'entry': entry, 'settings': settings, 'root': root, 'result_dir': result_dir,
            'record_path': record, 'context': context, 'case_identities': [(c['task'], c['variant'], c['case_id']) for c in cases]}


def command_for(spec, entry, python):
    argv = spec['argv']
    if len(argv) < 2 or argv[0] != '{python}' or any(not isinstance(arg, str) for arg in argv):
        raise ValueError('Commands require the isolated Python executable and a frozen script')
    index = 2 if argv[1] == '-u' else 1
    if len(argv) <= index or argv[index].startswith('-'):
        raise ValueError('Only frozen file-based Python commands are permitted')
    script = entry_path(entry, argv[index])
    names = entry.get('command_files_sha256', {})
    relative = str(script.relative_to(Path(entry['project_root']).resolve()))
    if relative not in names or sha(script) != names[relative]:
        raise ValueError('Command script not frozen')
    return [str(python), *argv[1:index], str(script), *argv[index + 1:]]


def stop_process(process):
    if process is not None and process.poll() is None:
        os.killpg(process.pid, signal.SIGTERM)
        try:
            process.wait(timeout=30)
        except subprocess.TimeoutExpired:
            os.killpg(process.pid, signal.SIGKILL)
            process.wait(timeout=10)


def run(args):
    if sha(args.plan) != args.plan_sha256:
        raise ValueError('Batch plan changed after submission')
    plan = json.loads(args.plan.read_text())
    worker = validate_plan(plan, args.worker_id)
    validate_artifacts(plan)
    local = args.runtime_dir.resolve()
    job_id = os.environ.get('SLURM_JOB_ID')
    if not job_id or not local.name.startswith('bio-remaining-') or not (local / 'python/bin/python3.12').is_file():
        raise ValueError('A private Slurm runtime is required')
    status_dir = POOL / 'status' / f"{worker['worker_id']}-{job_id}"
    status_dir.mkdir(parents=True, exist_ok=True)
    state = {'worker_id': worker['worker_id'], 'slurm_job_id': job_id, 'hostname': socket.gethostname(),
             'plan_sha256': args.plan_sha256, 'stage': 'preflight', 'entry_results': [],
             'benchmark_requests_started': False, 'updated_at_utc': dt.datetime.now(dt.timezone.utc).isoformat()}
    state_path = status_dir / 'worker_status.json'
    write(state_path, state)
    common_path = Path(plan.get('runtime_common_path', str(POOL / 'runtime_common.py')))
    if str(common_path) not in plan['infrastructure_files_sha256']:
        raise ValueError('Runtime helpers are not frozen')
    common = load_module('remaining_runtime_common', common_path)
    common.apply_overlay(local)
    env = common.environment(local)
    os.environ.clear(); os.environ.update(env)
    python = local / 'python/bin/python3.12'
    executor_env = dict(env, PYTHONDONTWRITEBYTECODE='1')
    paths = wheel_overlays(plan, local / 'scoring_overlay') + extra_pythonpath(plan)
    if paths:
        executor_env['PYTHONPATH'] = os.pathsep.join(paths)
    model_dir = common.validate_checkpoint(worker['model'], worker['model_revision'])
    locks = []
    prepared = []
    server = None
    try:
        identities = set()
        for entry in worker['entries']:
            lock_path = entry_path(entry, '.local/slurm_generation-' + entry['run_id'] + '.lock')
            lock_path.parent.mkdir(parents=True, exist_ok=True)
            lock = lock_path.open('a')
            fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB); locks.append(lock)
            checked = prepare_entry(entry, worker, model_dir, common, status_dir / entry['run_id'])
            current = set(checked.pop('case_identities'))
            if identities & current:
                raise ValueError('Duplicate native case in GPU batch')
            identities |= current; prepared.append(checked)
        code = "import json,torch,importlib.metadata as m; print(json.dumps({'visible_gpu_count':torch.cuda.device_count(),'device':torch.cuda.get_device_name(0),'torch':torch.__version__,'cuda':torch.version.cuda,'vllm':m.version('vllm')}))"
        packages = json.loads(subprocess.check_output([str(python), '-c', code], env=env, text=True))
        if packages['visible_gpu_count'] != 1:
            raise ValueError('Slurm must expose exactly one allocated GPU')
        write(status_dir / 'execution_environment.json', packages)
        sampler = "import json,torch,flashinfer; assert torch.cuda.device_count()==1; p=torch.zeros((4,128),device='cuda'); p[:,42]=1; s=flashinfer.top_k_top_p_sampling_from_probs(p,top_k=20,top_p=0.95,seed=42); torch.cuda.synchronize(); assert s.tolist()==[42]*4; print(json.dumps({'passed':True,'sampled_indices':s.tolist()}))"
        with (status_dir / 'sampling_check.log').open('w') as log:
            subprocess.run([str(python), '-c', sampler], env=env, stdout=log, stderr=subprocess.STDOUT, timeout=600, check=True)
        with socket.socket() as probe:
            probe.bind(('127.0.0.1', worker['port']))
        command = [str(python), '-m', 'vllm.entrypoints.cli.main', 'serve', str(model_dir),
                   '--served-model-name', worker['model'], '--host', '127.0.0.1', '--port', str(worker['port']),
                   '--dtype', 'bfloat16', '--tensor-parallel-size', '1', '--gpu-memory-utilization', '0.90',
                   '--max-model-len', str(worker['max_model_len']), '--max-num-seqs', '4',
                   '--reasoning-parser', 'qwen3', '--enable-prefix-caching',
                   '--limit-mm-per-prompt', '{"image": 1, "video": 0}']
        state['stage'] = 'starting_server'; write(state_path, state)
        with (status_dir / 'server.log').open('w') as log:
            server = subprocess.Popen(command, cwd=local, env=env, stdout=log, stderr=subprocess.STDOUT, start_new_session=True)
        ACTIVE_CHILDREN.append(server)
        endpoint = f"http://127.0.0.1:{worker['port']}/v1"
        deadline = time.monotonic() + 1200
        while time.monotonic() < deadline:
            if server.poll() is not None:
                raise RuntimeError('vLLM exited during startup')
            try:
                if any(row.get('id') == worker['model'] for row in common.call(endpoint, '/models').get('data', [])):
                    break
            except (OSError, ValueError):
                pass
            time.sleep(2)
        else:
            raise TimeoutError('vLLM startup exceeded20 minutes')
        gpu_processes = common.own_gpu_processes(server.pid)
        if len({row['gpu_uuid'] for row in gpu_processes}) != 1:
            raise RuntimeError('Expected exactly one observed allocated GPU')
        identity = {'pid': server.pid, 'proc_start_ticks': common.start_ticks(server.pid),
                    'model': worker['model'], 'revision': worker['model_revision'], 'gpu_ids': [0],
                    'host': '127.0.0.1', 'port': worker['port'], 'endpoint': endpoint,
                    'slurm_job_id': job_id, 'slurm_job_gpus': os.environ.get('SLURM_JOB_GPUS'),
                    'cuda_visible_devices': os.environ.get('CUDA_VISIBLE_DEVICES'), 'hostname': socket.gethostname(),
                    'observed_gpu_processes': gpu_processes, 'command': command,
                    'max_model_len': worker['max_model_len'], 'pool_worker_id': worker['worker_id']}
        write(status_dir / 'server_identity.json', identity)
        common.synthetic_serving(endpoint, worker['model'], status_dir)
        state['stage'] = 'ready'; write(state_path, state)
        for prepared_entry in prepared:
            entry = prepared_entry['entry']; result_dir = prepared_entry['result_dir']
            end = os.environ.get('SLURM_JOB_END_TIME')
            required = entry.get('estimated_max_seconds', 0) + 600
            if end and int(end) - time.time() < required:
                raise RuntimeError('Insufficient remaining wall time; next shard was not dispatched')
            if server.poll() is not None:
                raise RuntimeError('Serving process exited before next shard')
            write(prepared_entry['record_path'], identity)
            result_dir.mkdir(parents=True, exist_ok=True)
            write(result_dir / 'context_check.json', prepared_entry['context'])
            write(result_dir / 'server_identity.json', identity)
            entry_state = {'run_id': entry['run_id'], 'task_id': entry['task_id'], 'stage': 'executing',
                           'slurm_job_id': job_id, 'worker_id': worker['worker_id'], 'command_results': []}
            state.update(stage='executing', active_run_id=entry['run_id'], benchmark_requests_started=True)
            write(state_path, state); write(result_dir / 'slurm_worker_status.json', entry_state)
            for command_spec in entry['commands']:
                argv = command_for(command_spec, entry, python)
                log_path = result_dir / f"slurm_{command_spec['label']}.log"
                if log_path.exists():
                    raise ValueError('Command log already exists; refusing a possible repeat')
                with log_path.open('x') as log:
                    child = subprocess.Popen(argv, cwd=prepared_entry['root'], env=executor_env,
                                             stdout=log, stderr=subprocess.STDOUT, start_new_session=True)
                    ACTIVE_CHILDREN.append(child)
                    code = child.wait()
                    ACTIVE_CHILDREN.remove(child)
                entry_state['command_results'].append({'label': command_spec['label'], 'exit_code': code})
                write(result_dir / 'slurm_worker_status.json', entry_state)
                if code:
                    entry_state['stage'] = 'failed'; write(result_dir / 'slurm_worker_status.json', entry_state)
                    raise RuntimeError('Frozen executor/scorer failed: ' + entry['run_id'])
            completion = result_dir / entry.get('completion_file', 'completion.json')
            if not completion.is_file():
                raise ValueError('Frozen executor did not write its required completion record')
            entry_state.update(stage='completed', completion_sha256=sha(completion))
            write(result_dir / 'slurm_worker_status.json', entry_state)
            state['entry_results'].append(entry_state); write(state_path, state)
        state['stage'] = 'completed'
    except BaseException as error:
        state.update(stage='failed', error=f'{type(error).__name__}: {error}')
        raise
    finally:
        for process in list(reversed(ACTIVE_CHILDREN)):
            stop_process(process)
        state['updated_at_utc'] = dt.datetime.now(dt.timezone.utc).isoformat()
        write(state_path, state)
        for lock in locks:
            lock.close()


if __name__ == '__main__':
    def terminate(signum, frame):
        raise RuntimeError(f'Worker received termination signal{signum}')
    signal.signal(signal.SIGTERM, terminate)
    signal.signal(signal.SIGINT, terminate)
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--plan', required=True, type=Path)
    parser.add_argument('--plan-sha256', required=True)
    parser.add_argument('--worker-id', required=True)
    parser.add_argument('--runtime-dir', required=True, type=Path)
    run(parser.parse_args())
