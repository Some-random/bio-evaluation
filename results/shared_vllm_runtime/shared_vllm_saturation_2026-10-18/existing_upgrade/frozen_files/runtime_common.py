"""One isolated Slurm GPU, one frozen LAB-Bench run, local-only serving."""
from __future__ import annotations
import argparse
import base64
import copy
import fcntl
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import signal
import socket
import struct
import subprocess
import sys
import tarfile
import time
import urllib.request
import zlib

ROOT = Path(__file__).resolve().parents[2]
POOL = ROOT / '.local/parallel_labbench'
ARTIFACTS = ROOT / '.local/litqa2_replay'


def sha(path):
    h = hashlib.sha256()
    with Path(path).open('rb') as f:
        for chunk in iter(lambda: f.read(8 * 1024 * 1024), b''):
            h.update(chunk)
    return h.hexdigest()


def write(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + '.tmp')
    tmp.write_text(json.dumps(value, indent=2) + '\n')
    tmp.chmod(0o600)
    tmp.replace(path)


def start_ticks(pid):
    return Path(f'/proc/{pid}/stat').read_text().rsplit(') ', 1)[1].split()[19]


def apply_overlay(local):
    receipt = json.loads((ARTIFACTS / 'cuda_overlay_archive.json').read_text())
    base = json.loads((ARTIFACTS / 'runtime_archive.json').read_text())
    deletions = json.loads((ARTIFACTS / 'cuda_overlay_deletions.json').read_text())
    if deletions['base_archive_sha256'] != base['sha256'] or sha(receipt['archive_path']) != receipt['sha256']:
        raise ValueError('Runtime overlay does not match the verified archive')
    for name in deletions['files'] + deletions['directories']:
        rel = Path(name)
        path = local / rel
        if rel.is_absolute() or '..' in rel.parts or rel.parts[0] != 'python' or not path.resolve().is_relative_to(local):
            raise ValueError('Unsafe overlay deletion')
        if path.is_symlink() or path.is_file():
            path.unlink()
        elif path.is_dir():
            import shutil
            shutil.rmtree(path)
    with tarfile.open(receipt['archive_path']) as archive:
        archive.extractall(local, filter='data')
    return {'base': base['sha256'], 'overlay': receipt['sha256']}


def environment(local):
    prefix = local / 'python'
    env = dict(os.environ)
    for name in ('OPENAI_API_KEY', 'ANTHROPIC_API_KEY', 'HF_TOKEN', 'HUGGING_FACE_HUB_TOKEN', 'PYTHONHOME', 'VIRTUAL_ENV'):
        env.pop(name, None)
    cache = local / 'cache'
    (cache / 'tmp').mkdir(parents=True, exist_ok=True)
    env.update(HF_HUB_OFFLINE='1', TRANSFORMERS_OFFLINE='1', HF_HOME=str(cache / 'hf'),
               XDG_CACHE_HOME=str(cache), TRITON_CACHE_DIR=str(cache / 'triton'),
               VLLM_CACHE_ROOT=str(cache / 'vllm'), CUDA_CACHE_PATH=str(cache / 'cuda'),
               FLASHINFER_WORKSPACE_BASE=str(cache / 'flashinfer'), TMPDIR=str(cache / 'tmp'),
               VLLM_NO_USAGE_STATS='1', DO_NOT_TRACK='1', MAX_JOBS='4', PYTHONNOUSERSITE='1',
               OMP_NUM_THREADS='8', MKL_NUM_THREADS='8')
    toolkit = prefix / 'lib/python3.12/site-packages/nvidia/cu13'
    if not (toolkit / 'bin/nvcc').is_file():
        raise ValueError('Verified CUDA compiler is missing')
    if not (toolkit / 'lib64').exists():
        (toolkit / 'lib64').symlink_to('lib', target_is_directory=True)
    if not (toolkit / 'lib/libcudart.so').exists():
        (toolkit / 'lib/libcudart.so').symlink_to('libcudart.so.13')
    env['CUDA_HOME'] = str(toolkit)
    env['PATH'] = os.pathsep.join([str(prefix / 'bin'), str(toolkit / 'bin'), env.get('PATH', '')])
    env['LD_LIBRARY_PATH'] = os.pathsep.join([str(toolkit / 'lib'), env.get('LD_LIBRARY_PATH', '')]).rstrip(os.pathsep)
    return env


def validate_checkpoint(model, revision):
    audit = json.loads((ARTIFACTS / 'checkpoint_verification.json').read_text())
    if not (audit.get('all_weight_hashes_match') or audit.get('all_weights_match') or audit.get('all_matched')):
        raise ValueError('Complete checkpoint verification is missing')
    directory = Path(audit['checkpoint_directory'])
    if audit['recorded_model'] != model or audit['recorded_revision'] != revision:
        raise ValueError('Checkpoint identity differs from frozen model')
    for record in audit['files']:
        if record.get('optional_for_inference'):
            continue
        st = (directory / record['file']).stat()
        if record.get('state') != 'verified' or (st.st_size, st.st_mtime_ns) != (record['bytes'], record['mtime_ns']):
            raise ValueError('Checkpoint changed since complete hash verification')
    publisher = json.loads((ARTIFACTS / 'publisher_verification.json').read_text())
    if publisher.get('status') != 'verified' or publisher.get('publisher_revision') != revision:
        raise ValueError('Publisher identity verification failed')
    return directory


def frozen_runner(run_root, config):
    path = run_root / 'scripts/run_local_labbench_multimodal.py'
    spec = importlib.util.spec_from_file_location('frozen_multimodal_runner', path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    settings, cases = module.read_frozen_config(config)
    return settings, cases


def context_preflight(cases, settings, model_dir, cap, folder):
    from transformers import AutoProcessor
    processor = AutoProcessor.from_pretrained(model_dir, local_files_only=True)
    rows = []
    for case in cases:
        # This processor normalizes image_url parts in-place; never give it the
        # original message objects later dispatched by the frozen runner.
        messages = copy.deepcopy(case['messages'])
        count = sum(part.get('type') == 'image_url' for msg in case['messages']
                    for part in (msg['content'] if isinstance(msg['content'], list) else []))
        encoded = processor.apply_chat_template(messages, tokenize=True, return_dict=True,
                    return_tensors='pt', add_generation_prompt=True,
                    **settings['generation']['chat_template_kwargs'])
        length = int(encoded['input_ids'].shape[-1])
        grids = encoded.get('image_grid_thw')
        if count and (grids is None or len(grids) != count):
            raise ValueError('Image-expanded preflight omitted a native image')
        rows.append({'case_id': case['case_id'], 'prompt_tokens': length, 'images': count})
        del encoded
    largest = max(row['prompt_tokens'] for row in rows)
    budget = settings['generation']['max_tokens']
    result = {'case_count': len(rows), 'max_prompt_tokens': largest, 'output_budget': budget,
              'serving_context_cap': cap, 'max_images': max(row['images'] for row in rows),
              'all_prompts_fit': largest + budget <= cap, 'per_case': rows}
    write(folder / 'context_check.json', result)
    if not result['all_prompts_fit']:
        raise ValueError('Complete native inputs plus unchanged output budget exceed serving context')
    return result


def call(base, path, payload=None):
    opener = urllib.request.build_opener(urllib.request.ProxyHandler({}))
    data = None if payload is None else json.dumps(payload).encode()
    request = urllib.request.Request(base + path, data=data, headers={'Content-Type': 'application/json'})
    with opener.open(request, timeout=300 if payload else 3) as response:
        return json.load(response)


def red_image_url():
    def chunk(kind, data):
        return struct.pack('!I', len(data)) + kind + data + struct.pack('!I', zlib.crc32(kind + data) & 0xffffffff)
    size = 256
    png = b'\x89PNG\r\n\x1a\n' + chunk(b'IHDR', struct.pack('!2I5B', size, size, 8, 2, 0, 0, 0))
    png += chunk(b'IDAT', zlib.compress((b'\0' + b'\xff\0\0' * size) * size)) + chunk(b'IEND', b'')
    return 'data:image/png;base64,' + base64.b64encode(png).decode()


def synthetic_serving(base, model, folder):
    outputs = {}
    text = {'model': model, 'messages': [{'role': 'user', 'content': 'What is 2 + 2? Reply with only the digit.'}],
            'temperature': 0, 'max_tokens': 32, 'chat_template_kwargs': {'enable_thinking': False}}
    outputs['text'] = call(base, '/chat/completions', text)
    write(folder / 'synthetic_serving_checks.json', outputs)
    if outputs['text']['choices'][0]['message'].get('content', '').strip() != '4':
        raise ValueError('Synthetic text check failed')
    visual = dict(text, messages=[{'role': 'user', 'content': [
        {'type': 'text', 'text': 'What is the dominant color of this image? Reply with only the color name.'},
        {'type': 'image_url', 'image_url': {'url': red_image_url()}}]}])
    outputs['image'] = call(base, '/chat/completions', visual)
    color = outputs['image']['choices'][0]['message'].get('content', '').strip().lower().rstrip('.')
    write(folder / 'synthetic_serving_checks.json', outputs)
    if color != 'red':
        raise ValueError('Synthetic native-image check failed')


def own_gpu_processes(server_pid):
    descendants = {server_pid}
    parents = {}
    for process in Path('/proc').iterdir():
        if not process.name.isdigit():
            continue
        try:
            fields = (process / 'stat').read_text().rsplit(')', 1)[1].split()
            parents[int(process.name)] = int(fields[1])
        except (OSError, ValueError, IndexError):
            pass
    for _ in range(len(parents)):
        extra = {pid for pid, parent in parents.items() if parent in descendants} - descendants
        if not extra:
            break
        descendants.update(extra)
    raw = subprocess.check_output(['nvidia-smi', '--query-compute-apps=pid,gpu_uuid,used_memory', '--format=csv,noheader'], text=True)
    records = []
    for line in raw.splitlines():
        parts = [v.strip() for v in line.split(',')]
        if parts and parts[0].isdigit() and int(parts[0]) in descendants:
            records.append({'pid': int(parts[0]), 'gpu_uuid': parts[1], 'used_memory': parts[2]})
    return records


def run(args):
    plan = json.loads(args.plan.read_text())
    if sha(args.plan) != args.plan_sha256 or sha(__file__) != plan['worker_sha256']:
        raise ValueError('Infrastructure plan or worker changed after submission')
    for name, expected in plan['artifacts'].items():
        receipt = json.loads((ARTIFACTS / name).read_text())
        stat = Path(receipt['archive_path']).stat()
        if (receipt['sha256'] != expected['sha256']
                or (stat.st_size, stat.st_mtime_ns) != (expected['bytes'], expected['mtime_ns'])):
            raise ValueError('Runtime artifact changed after submission')
    task = next(item for item in plan['tasks'] if item['task_id'] == args.task)
    local = args.runtime_dir.resolve()
    if not os.environ.get('SLURM_JOB_ID') or not local.name.startswith('bio-labbench-') or not (local / 'python/bin/python3.12').is_file():
        raise ValueError('A private Slurm runtime is required')
    run_root = Path(task['project_root']).resolve()
    if not run_root.is_relative_to(POOL / 'runs') or task['port'] not in {8027, 8028, 8029}:
        raise ValueError('Unexpected run root or serving port')
    (run_root / '.local').mkdir(exist_ok=True)
    lock = (run_root / '.local/slurm_worker.lock').open('a')
    fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
    if sha(task['config_path']) != task['config_sha256']:
        raise ValueError('Frozen configuration changed')
    receipts = apply_overlay(local)
    env = environment(local)
    os.environ.clear()
    os.environ.update(env)
    settings, cases = frozen_runner(run_root, Path(task['config_path']))
    if (settings['approved_task_ids'] != [args.task] or settings['gpu_ids'] != [0]
            or settings['endpoint'] != f"http://127.0.0.1:{task['port']}/v1"):
        raise ValueError('Frozen run scope differs from allocated worker')
    model_dir = validate_checkpoint(settings['model'], settings['model_revision'])
    authority = json.loads((run_root / 'configs/local_model.json').read_text())
    if Path(authority['model_directory']).resolve() != model_dir.resolve():
        raise ValueError('Frozen authority selects another checkpoint')
    folder = run_root / 'results/runs' / settings['run_id']
    folder.mkdir(parents=True, exist_ok=True)
    if (folder / 'completion.json').exists():
        raise ValueError('This run already has a completion record')
    state = {'stage': 'preflight', 'task_id': args.task, 'run_id': settings['run_id'],
             'slurm_job_id': os.environ['SLURM_JOB_ID'], 'hostname': socket.gethostname(),
             'endpoint': settings['endpoint'], 'runtime_receipts': receipts, 'benchmark_worker_started': False}
    write(folder / 'slurm_worker_status.json', state)
    python = local / 'python/bin/python3.12'
    try:
        package_code = "import importlib.metadata as m,json,torch,sys; print(json.dumps({'python':sys.version,'torch_build':torch.__version__,'torch_cuda':torch.version.cuda,'visible_gpu_count':torch.cuda.device_count(),'packages':{n:m.version(n) for n in ['vllm','torch','transformers','triton','flashinfer-python']}}))"
        package_info = json.loads(subprocess.check_output([str(python), '-c', package_code], env=env, text=True))
        if package_info['visible_gpu_count'] != 1:
            raise ValueError('Slurm must expose exactly one GPU to this worker')
        write(folder / 'execution_environment.json', {**package_info, **state,
              'model_directory': str(model_dir), 'checkpoint_audit_sha256': sha(ARTIFACTS / 'checkpoint_verification.json')})
        context = context_preflight(cases, settings, model_dir, task['max_model_len'], folder)
        sampler = "import json,torch,flashinfer; assert torch.cuda.device_count()==1; p=torch.zeros((4,128),device='cuda',dtype=torch.float32); p[:,42]=1; s=flashinfer.top_k_top_p_sampling_from_probs(p,top_k=20,top_p=0.95,seed=42); torch.cuda.synchronize(); assert s.tolist()==[42]*4; print(json.dumps({'passed':True,'device':torch.cuda.get_device_name(0),'sampled_indices':s.tolist()}))"
        with (folder / 'sampling_check.log').open('w') as log:
            subprocess.run([str(python), '-c', sampler], env=env, stdout=log, stderr=subprocess.STDOUT, timeout=600, check=True)
    except Exception as error:
        state.update(stage='preflight_failed', error=f'{type(error).__name__}: {error}')
        write(folder / 'slurm_worker_status.json', state)
        raise
    command = [str(python), '-m', 'vllm.entrypoints.cli.main', 'serve', str(model_dir),
               '--served-model-name', settings['model'], '--host', '127.0.0.1', '--port', str(task['port']),
               '--dtype', 'bfloat16', '--tensor-parallel-size', '1', '--gpu-memory-utilization', '0.90',
               '--max-model-len', str(task['max_model_len']), '--max-num-seqs', '4',
               '--reasoning-parser', 'qwen3', '--enable-prefix-caching',
               '--limit-mm-per-prompt', json.dumps({'image': max(1, context['max_images']), 'video': 0})]
    with socket.socket() as probe:
        probe.bind(('127.0.0.1', task['port']))
    server = None
    try:
        state['stage'] = 'starting_server'; write(folder / 'slurm_worker_status.json', state)
        with (folder / 'server.log').open('w') as log:
            server = subprocess.Popen(command, cwd=local, env=env, stdout=log, stderr=subprocess.STDOUT, start_new_session=True)
        identity = {'pid': server.pid, 'proc_start_ticks': start_ticks(server.pid), 'model': settings['model'],
                    'revision': settings['model_revision'], 'gpu_ids': [0], 'host': '127.0.0.1',
                    'port': task['port'], 'endpoint': settings['endpoint'], 'slurm_job_id': os.environ['SLURM_JOB_ID'],
                    'slurm_job_gpus': os.environ.get('SLURM_JOB_GPUS'), 'cuda_visible_devices': os.environ.get('CUDA_VISIBLE_DEVICES'),
                    'hostname': socket.gethostname(), 'command': command, 'max_model_len': task['max_model_len']}
        write(run_root / '.local/local_model_server.json', identity)
        deadline = time.monotonic() + 1200
        while time.monotonic() < deadline:
            if server.poll() is not None:
                raise RuntimeError('vLLM exited during startup')
            try:
                models = call(settings['endpoint'], '/models')
                if any(row.get('id') == settings['model'] for row in models.get('data', [])):
                    break
            except (OSError, ValueError):
                pass
            time.sleep(2)
        else:
            raise TimeoutError('vLLM did not become ready in 20 minutes')
        identity['observed_gpu_processes'] = own_gpu_processes(server.pid)
        if len({row['gpu_uuid'] for row in identity['observed_gpu_processes']}) != 1:
            raise RuntimeError('Expected exactly one observed allocated GPU')
        write(run_root / '.local/local_model_server.json', identity)
        write(folder / 'server_identity.json', identity)
        synthetic_serving(settings['endpoint'], settings['model'], folder)
        state['stage'] = 'ready'; write(folder / 'slurm_worker_status.json', state)
        if not args.execute:
            return
        state.update(stage='generating', benchmark_worker_started=True); write(folder / 'slurm_worker_status.json', state)
        with (folder / 'generation.log').open('w') as log:
            generation = subprocess.run([str(python), '-u', str(run_root / 'scripts/run_local_labbench_multimodal.py'), '--config', task['config_path']], cwd=run_root, env=env, stdout=log, stderr=subprocess.STDOUT)
        state.update(stage='scoring', generation_exit_code=generation.returncode); write(folder / 'slurm_worker_status.json', state)
        with (folder / 'scoring.log').open('w') as log:
            scoring = subprocess.run([str(python), str(run_root / task['scorer']), '--run', settings['run_id']], cwd=run_root, env=env, stdout=log, stderr=subprocess.STDOUT)
        state.update(scoring_exit_code=scoring.returncode, stage='completed' if generation.returncode == scoring.returncode == 0 else 'failed_or_incomplete')
        write(folder / 'completion.json', state)
        if state['stage'] != 'completed':
            raise RuntimeError('Generation or scoring did not complete cleanly')
    except Exception as error:
        state.update(stage='failed', error=f'{type(error).__name__}: {error}')
        raise
    finally:
        if server is not None and server.poll() is None:
            os.killpg(server.pid, signal.SIGTERM)
            try:
                server.wait(timeout=30)
            except subprocess.TimeoutExpired:
                os.killpg(server.pid, signal.SIGKILL)
        write(folder / 'slurm_worker_status.json', state)


if __name__ == '__main__':
    def terminate(signum, frame):
        raise RuntimeError(f'Worker received termination signal {signum}')
    signal.signal(signal.SIGTERM, terminate)
    signal.signal(signal.SIGINT, terminate)
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--plan', type=Path, required=True)
    parser.add_argument('--plan-sha256', required=True)
    parser.add_argument('--task', choices=['B03', 'B04', 'B05'], required=True)
    parser.add_argument('--runtime-dir', type=Path, required=True)
    parser.add_argument('--execute', action='store_true')
    run(parser.parse_args())
