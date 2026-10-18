"""CPU-only one-attempt scoring after each complete original mixed-budget union."""
from __future__ import annotations

import argparse
import fcntl
import json
import os
from pathlib import Path
import socket
import sys
import time

import mixed_budget_scoring as scoring


def atomic(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + '.tmp')
    temporary.write_text(json.dumps(value, indent=2) + '\n')
    temporary.replace(path)


def ready(spec):
    root = Path(spec['project_root']).resolve()
    revisions = scoring.revision_index(spec)
    closed = scoring.closed_checkpoint_index(spec)
    for source in spec['sources']:
        cfg = scoring.base.checked_config(root, source['config_file'], source['config_sha256'])
        revised = revisions.get((str(root), cfg['run_id']))
        if revised:
            if not (Path(revised[2]['output_directory']) / 'generation_completion.json').is_file():
                return False, 'prospective16k_pending:' + cfg['run_id']
        else:
            folder = scoring.base.generation_folder(root, cfg, source)
            if cfg['run_id'] in closed:
                continue
            if not any((folder / name).is_file() for name in ('completion.json',
                    'shared_vllm_generation_completion.json', 'shared_vllm_saturation_generation_completion.json')):
                return False, 'historical4k_not_terminal:' + cfg['run_id']
    return True, 'complete_original_union_available'


def frozen(path, expected):
    plan = scoring.pinned(path, expected)
    if (plan.get('schema_version') != 1 or plan.get('condition') != scoring.CONDITION
            or not 1 <= plan.get('poll_seconds', 20) <= 60 or not plan.get('spec_files')):
        raise scoring.ScoringError('Invalid mixed-budget scoring watcher plan')
    required = {str(Path(__file__).resolve()), str(Path(scoring.__file__).resolve()),
        str(scoring.BASE_PATH.resolve())}
    if not required <= set(plan['code_files_sha256']):
        raise scoring.ScoringError('Watcher and both adapters must be frozen')
    for name, sha in plan['code_files_sha256'].items():
        if scoring.file_sha(name) != sha:
            raise scoring.ScoringError('Frozen mixed scoring dependency changed: ' + name)
    specs = [(row['path'], scoring.pinned(row['path'], row['sha256'])) for row in plan['spec_files']]
    tasks = [spec['task_id'] for _, spec in specs]
    if len(tasks) != len(set(tasks)) or not set(tasks) <= scoring.SUPPORTED:
        raise scoring.ScoringError('Duplicate or unsupported native task')
    return plan, specs


def cycle(path, expected, score_function=scoring.score_spec):
    plan, specs = frozen(path, expected)
    state_path = Path(plan['state_file'])
    state = scoring.read(state_path) if state_path.exists() else {
        'schema_version': 1, 'plan_sha256': expected, 'condition': scoring.CONDITION,
        'tasks': {}, 'inference_dispatched': False, 'native_parsers_and_metrics_unchanged': True}
    if state.get('plan_sha256') != expected:
        raise scoring.ScoringError('Watcher state belongs to another plan')
    state['worker'] = {'pid': os.getpid(), 'hostname': socket.gethostname(),
        'proc_start_ticks': Path('/proc/self/stat').read_text().split(') ', 1)[1].split()[19],
        'python': sys.executable, 'slurm_job_id': os.environ.get('SLURM_JOB_ID'),
        'logical_cpu_affinity_count': len(os.sched_getaffinity(0))}
    for spec_path, spec in specs:
        previous = state['tasks'].get(spec['task_id'], {})
        if previous.get('stage') in {'completed', 'failed'}:
            continue
        try:
            is_ready, reason = ready(spec)
            if not is_ready:
                state['tasks'][spec['task_id']] = {'stage': 'pending', 'reason': reason}
                continue
            state['tasks'][spec['task_id']] = {'stage': 'validating_or_scoring', 'updated_at_pacific': scoring.base.now()}
            atomic(state_path, state)
            result = score_function(spec)
            state['tasks'][spec['task_id']] = {'stage': 'completed', 'result': result}
        except scoring.Pending as error:
            state['tasks'][spec['task_id']] = {'stage': 'pending', 'reason': str(error)}
        except Exception as error:
            state['tasks'][spec['task_id']] = {'stage': 'failed', 'error': type(error).__name__ + ': ' + str(error),
                'automatic_retry': False}
        state['tasks'][spec['task_id']]['updated_at_pacific'] = scoring.base.now()
        state['updated_at_pacific'] = scoring.base.now()
        atomic(state_path, state)
    stages = [state['tasks'].get(spec['task_id'], {}).get('stage') for _, spec in specs]
    state.update(updated_at_pacific=scoring.base.now(), all_terminal=all(s in {'completed', 'failed'} for s in stages),
        all_completed=all(s == 'completed' for s in stages))
    atomic(state_path, state)
    return state, plan.get('poll_seconds', 20)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--plan', type=Path, required=True)
    parser.add_argument('--plan-sha256', required=True)
    parser.add_argument('--once', action='store_true')
    args = parser.parse_args()
    with args.plan.with_suffix('.worker.lock').open('a') as lock:
        fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        while True:
            state, pause = cycle(args.plan, args.plan_sha256)
            print(json.dumps({'updated_at_pacific': state['updated_at_pacific'],
                'all_terminal': state['all_terminal'],
                'tasks': {k: v['stage'] for k, v in state['tasks'].items()}}), flush=True)
            if args.once or state['all_terminal']:
                return 0 if state['all_completed'] or not state['all_terminal'] else 1
            time.sleep(pause)


if __name__ == '__main__':
    raise SystemExit(main())
