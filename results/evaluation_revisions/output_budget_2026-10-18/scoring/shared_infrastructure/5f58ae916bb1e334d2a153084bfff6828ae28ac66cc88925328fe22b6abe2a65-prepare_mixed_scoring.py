"""Freeze new seven-task native scoring specs after prospective cohorts exist."""
from __future__ import annotations

import json
from pathlib import Path
import sys

import mixed_budget_scoring as scoring


def prepare():
    root = scoring.REPOSITORY
    here = Path(__file__).resolve().parent
    previous = root / '.local/shared_vllm_saturation_2026-10-18/scoring/watch_plan_v1.json'
    original_plan = scoring.read(previous)
    producer = root / '.local/evaluation_revision_2026-10-18/budget_queue/run_budget_revision.py'
    bindings = []
    closed_bindings = []
    for group in ('existing_pool', 'new_pool'):
        path = producer.parent / ('plan_' + group + '.json')
        plan = scoring.read(path)
        if plan['code_sha256'] != scoring.file_sha(producer):
            raise scoring.ScoringError('Prospective execution plan does not pin current producer')
        bindings.append({'path': str(path), 'sha256': scoring.file_sha(path)})
        preparation = scoring.read(producer.parent / ('preparation_' + group + '.json'))
        if preparation['plan_sha256'] != scoring.file_sha(path):
            raise scoring.ScoringError('Preparation receipt differs from its frozen execution plan')
        for row in preparation['source_runs']:
            checkpoint_path = producer.parent / 'checkpoints' / (row['run_id'] + '.json')
            scoring.pinned(checkpoint_path, row['parent_checkpoint_sha256'])
            closed_bindings.append({'run_id': row['run_id'], 'task_id': row['task_id'],
                'path': str(checkpoint_path), 'sha256': row['parent_checkpoint_sha256']})
    specs = []
    for old in original_plan['spec_files']:
        spec = scoring.pinned(old['path'], old['sha256'])
        if spec['task_id'] not in scoring.SUPPORTED:
            continue
        spec.update(schema_version=2, generation_budget_condition=scoring.CONDITION,
            revision_plans=bindings, revision_runner_file=str(producer),
            revision_runner_sha256=scoring.file_sha(producer),
            closed_4k_checkpoints=[row for row in closed_bindings if row['task_id'] == spec['task_id']])
        full = scoring.base.checked_config(Path(spec['project_root']), spec['full_config_file'], spec['full_config_sha256'])
        spec['output_run_id'] = full['run_id'] + '_mixed_4k16k_scoring_v1'
        path = here / (spec['task_id'].lower() + '_mixed_scoring_v1.json')
        scoring.base.immutable_json(path, spec)
        specs.append({'path': str(path), 'sha256': scoring.file_sha(path)})
    if {scoring.read(row['path'])['task_id'] for row in specs} != scoring.SUPPORTED:
        raise scoring.ScoringError('Require exactly all seven retained native tasks')
    dependencies = [Path(scoring.__file__), here / 'watch_mixed_budget_scoring.py', Path(__file__),
        scoring.BASE_PATH, scoring.BASE_PATH.with_name('shared_vllm_resume.py'), root / 'scripts/shared_vllm_resume.py', producer]
    plan = {'schema_version': 1, 'condition': scoring.CONDITION, 'poll_seconds': 20,
        'spec_files': specs, 'state_file': str(here / 'watcher_status_v1.json'),
        'code_files_sha256': {str(path.resolve()): scoring.file_sha(path) for path in dependencies},
        'native_cpu_job_id': 237730,
        'python': '/tmp/bio-cpu-supervisor-237730-6G6tNR/python/bin/python3.10',
        'scope': 'Exact original full native unions; historical4k and prospective16k; seven separate derived result directories.',
        'old_outputs_modified': False, 'old_scorer_attempts_retried': False}
    path = here / 'watch_plan_v1.json'
    scoring.base.immutable_json(path, plan)
    print(json.dumps({'plan_path': str(path), 'plan_sha256': scoring.file_sha(path), 'task_count': len(specs)}))


if __name__ == '__main__':
    prepare()
