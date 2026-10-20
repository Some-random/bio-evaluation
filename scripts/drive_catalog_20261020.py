#!/usr/bin/env python3
"""Dispatch only pre-frozen task entries, development first, with no model API calls."""
import argparse
import datetime
import fcntl
import hashlib
import json
import os
from pathlib import Path
import subprocess
import time
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / '.local/catalog_execution_2026-10-20'


def sha(path):
    h = hashlib.sha256()
    with Path(path).open('rb') as f:
        for b in iter(lambda: f.read(8 * 1024 * 1024), b''):
            h.update(b)
    return h.hexdigest()


def stamp():
    return datetime.datetime.now(ZoneInfo('America/Los_Angeles')).isoformat()


def read(path):
    return json.loads(Path(path).read_text()) if Path(path).is_file() else None


def atomic(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temp = path.with_suffix(path.suffix + '.tmp')
    temp.write_text(json.dumps(value, indent=2) + '\n')
    temp.chmod(0o600)
    temp.replace(path)


def progress(folder):
    return read(Path(folder) / 'completion.json') or read(Path(folder) / 'progress.json')


def queue_key(entry, phase):
    key = entry['task_id'] + '_' + phase
    if entry.get('prioritize_development'):
        key = ('00_' if phase == 'development' else '10_') + key
    return key


def grant(entry, phase, identity, identity_path, endpoint):
    config = Path(entry[phase + '_config'])
    if sha(config) != entry[phase + '_config_sha256'] or sha(entry['runner']) != entry['runner_sha256']:
        raise ValueError('Frozen task code/configuration changed')
    settings = read(config)
    if settings['task_id'] != entry['task_id']:
        raise ValueError('Task/config mismatch')
    folder = BASE / 'tasks' / entry['task_id'] / 'runtime' / phase
    folder.parent.mkdir(parents=True, exist_ok=True)
    path = BASE / 'runtime/queue' / (queue_key(entry, phase) + '.grant.json')
    argv = ['--config', str(config), '--output', str(folder), '--grant', str(path),
            '--concurrency', str(entry.get('concurrency', 4))]
    value = {'authorized': True, 'task_id': entry['task_id'], 'run_id': settings['run_id'],
             'phase': phase, 'runner': entry['runner'], 'runner_sha256': entry['runner_sha256'],
             'config': str(config), 'config_sha256': entry[phase + '_config_sha256'],
             'endpoint': endpoint, 'server_identity_file': str(identity_path),
             'server_identity_sha256': sha(identity_path), 'argv': argv,
             'created_at_pacific': stamp(), 'historical_results_immutable': True}
    if phase == 'benchmark':
        completion = folder.parent / 'development/completion.json'
        value.update(development_completion=str(completion),
                     development_completion_sha256=sha(completion))
        argv += ['--development-completion', str(completion)]
    if not path.exists():
        with path.open('x') as f:
            json.dump(value, f, indent=2)
            f.write('\n')
        path.chmod(0o600)
    return path


def scoring_command(entry, identity):
    if entry.get('scoring_execution') == 'existing_allocation_cpu':
        helper = ROOT / 'scripts/score_catalog_in_runtime_20261020.py'
        if sha(helper) != entry['runtime_scoring_helper_sha256']:
            raise ValueError('Frozen CPU scoring helper changed')
        return ['srun', '--jobid=' + identity['job_id'], '--overlap', '--exact',
                '--cpu-bind=none', '--gres=none', '--ntasks=1', '--cpus-per-task=1',
                '--mem=12G', '--immediate=20', '/usr/bin/python3', str(helper),
                '--plan', entry['dispatch_plan'], '--plan-sha256', entry['dispatch_plan_sha256'],
                '--task', entry['task_id']]
    return ['/usr/bin/python3', entry['scorer'], *entry['scorer_argv']]


def observe(entry, pool_ready, identity, identity_path, endpoint):
    task = entry['task_id']
    folder = BASE / 'tasks' / task / 'runtime'
    dev = progress(folder / 'development')
    full = progress(folder / 'benchmark')
    row = {'task_id': task, 'development': dev, 'benchmark': full,
           'prepared_development_planned': read(entry['development_config'])['planned'],
           'prepared_benchmark_planned': read(entry['benchmark_config'])['planned'],
           'stage': 'waiting_for_shared_runtime', 'native_scoring_status': 'not_started'}
    for phase in ('development', 'benchmark'):
        prefix = BASE / 'runtime/queue' / queue_key(entry, phase)
        failure = read(str(prefix) + '.rejected.json')
        finished = read(str(prefix) + '.finished.json')
        if failure or (finished and finished['exit_code'] != 0):
            row.update(stage=phase + '_worker_failed_no_automatic_retry', error=failure or finished)
            return row
    if not pool_ready:
        return row
    if dev is None or not (folder / 'development/completion.json').exists():
        grant(entry, 'development', identity, identity_path, endpoint)
        row['stage'] = 'development_queued_or_running'
        return row
    if (dev.get('phase') != 'development' or dev.get('all_passed') is not True
            or dev.get('delivery_passed') != dev.get('planned')
            or dev.get('config_sha256') != entry['development_config_sha256']):
        row['stage'] = 'development_delivery_failed_benchmark_not_dispatched'
        return row
    if full is None or not (folder / 'benchmark/completion.json').exists():
        grant(entry, 'benchmark', identity, identity_path, endpoint)
        row['stage'] = 'benchmark_queued_or_running'
        return row
    if full['terminal'] != full['planned']:
        row['stage'] = 'generation_stopped_incomplete_no_automatic_retry'
        return row
    row['stage'] = 'generation_terminal_scoring_pending'
    score = Path(entry['score_output'])
    score_status = BASE / 'control' / (task + '_scoring_status.json')
    if score.exists():
        row.update(stage='scored_terminal', native_scoring_status='score_artifact_present',
                   score_path=str(score), score_sha256=sha(score))
        return row
    if score_status.exists():
        row['native_scoring_status'] = read(score_status)
        return row
    if sha(entry['scorer']) != entry['scorer_sha256']:
        raise ValueError('Frozen scorer changed')
    env = dict(os.environ)
    for key in list(env):
        if key.upper().endswith(('API_KEY', 'API_TOKEN')) or key in ('HF_TOKEN', 'HUGGING_FACE_HUB_TOKEN'):
            env.pop(key, None)
    if entry.get('scoring_pythonpath'):
        env['PYTHONPATH'] = entry['scoring_pythonpath']
    if entry.get('scoring_requires'):
        check = 'import importlib,json; print(json.dumps({n:importlib.import_module(n).__version__ for n in ' + repr(entry['scoring_requires']) + '}))'
        dependency = subprocess.run(['/usr/bin/python3', '-c', check], env=env,
                                    capture_output=True, text=True, timeout=120)
        if dependency.returncode:
            row['native_scoring_status'] = 'waiting_for_scorer_dependencies_no_score_attempt'
            return row
        row['scoring_dependency_versions'] = json.loads(dependency.stdout)
        if (entry.get('scoring_dependency_versions')
                and row['scoring_dependency_versions'] != entry['scoring_dependency_versions']):
            raise ValueError('Scoring dependency versions differ from frozen task runtime')
    atomic(score_status, {'stage': 'one_attempt_started', 'started_at_pacific': stamp(),
                         'prediction_lock_sha256': sha(folder / 'benchmark/prediction_lock.json')})
    with (BASE / 'control' / (task + '_scoring.log')).open('x') as log:
        result = subprocess.run(scoring_command(entry, identity),
                                cwd=ROOT, env=env, stdout=log, stderr=subprocess.STDOUT, timeout=1800)
    atomic(score_status, {'stage': 'completed' if result.returncode == 0 and score.exists() else 'failed_no_retry',
                         'finished_at_pacific': stamp(), 'exit_code': result.returncode,
                         'score_sha256': sha(score) if score.exists() else None})
    row['native_scoring_status'] = read(score_status)
    return row


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--plan', type=Path, required=True)
    parser.add_argument('--plan-sha256', required=True)
    parser.add_argument('--once', action='store_true')
    args = parser.parse_args()
    if sha(args.plan) != args.plan_sha256:
        raise ValueError('Dispatch plan changed')
    plan = read(args.plan)
    if sha(__file__) != plan['driver_sha256']:
        raise ValueError('Dispatch driver changed')
    control = BASE / 'control'
    control.mkdir(exist_ok=True)
    with (control / 'driver.lock').open('a') as lock:
        fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        while not (control / 'STOP').exists():
            pool = read(BASE / 'runtime/status.json')
            submission = read(BASE / 'runtime/submission_receipt.json')
            identity_path = BASE / 'runtime/server_identity.json'
            identity = read(identity_path)
            fresh = bool(pool and time.time() - (BASE / 'runtime/status.json').stat().st_mtime < 90)
            ready = bool(fresh and pool.get('stage') == 'serving_task_queue' and identity
                         and pool['job_id'] == submission['job_id'] == identity['job_id'])
            rows = []
            for entry in plan['tasks']:
                try:
                    runtime_entry = dict(entry, dispatch_plan=str(args.plan.resolve()),
                                         dispatch_plan_sha256=args.plan_sha256)
                    rows.append(observe(runtime_entry, ready, identity, identity_path, plan['endpoint']))
                except Exception as error:
                    rows.append({'task_id': entry['task_id'], 'stage': 'control_validation_failed',
                                 'error_type': type(error).__name__, 'error': str(error)})
            atomic(control / 'status.json', {'updated_at_pacific': stamp(), 'pid': os.getpid(),
                   'role': 'frozen_local_task_dispatch_and_one_attempt_scoring_controller',
                   'pool_runtime_ready': ready, 'pool_observation': pool,
                   'new_inference_calls_by_controller': 0, 'tasks': rows,
                   'prepared_without_runtime_counts_remain_unknown': True,
                   'full_catalog_complete': False})
            if args.once:
                break
            time.sleep(10)


if __name__ == '__main__':
    main()
