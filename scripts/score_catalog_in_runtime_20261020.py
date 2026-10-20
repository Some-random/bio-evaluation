#!/usr/bin/env python3
"""Run a hash-frozen offline scorer on CPUs inside the existing allocation."""
import argparse
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import socket
import subprocess

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / '.local/catalog_execution_2026-10-20'
COMMON = ROOT / '.local/shared_vllm_pool_2026-10-17_v3/runtime_common.py'
COMMON_SHA256 = '93611c2b597857222f6400bcf9151ce70ae7f8053c7871600bc49106e67370f4'


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def validate(plan_path, plan_sha, task):
    if sha(plan_path) != plan_sha:
        raise ValueError('Scoring plan changed')
    plan = json.loads(Path(plan_path).read_text())
    if sha(__file__) != plan['runtime_scoring_helper_sha256']:
        raise ValueError('Runtime scoring helper changed')
    entries = [e for e in plan['tasks'] if e['task_id'] == task]
    if len(entries) != 1 or entries[0].get('scoring_execution') != 'existing_allocation_cpu':
        raise ValueError('No unique CPU scoring entry')
    entry = entries[0]
    identity = json.loads((BASE / 'runtime/server_identity.json').read_text())
    pool = json.loads((BASE / 'runtime/status.json').read_text())
    if (os.environ.get('SLURM_JOB_ID') != identity['job_id']
            or pool['job_id'] != identity['job_id']
            or socket.gethostname() != identity['hostname']):
        raise ValueError('Scoring allocation identity differs')
    runtime = Path(pool['runtime'])
    if Path(identity['command'][0]) != runtime / 'python/bin/python3.12':
        raise ValueError('Scoring runtime differs from verified server runtime')
    scorer = Path(entry['scorer']).resolve()
    if not scorer.is_relative_to(ROOT) or sha(scorer) != entry['scorer_sha256']:
        raise ValueError('Frozen offline scorer changed')
    if sha(COMMON) != COMMON_SHA256:
        raise ValueError('Runtime environment helper changed')
    return entry, runtime


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--plan', type=Path, required=True)
    parser.add_argument('--plan-sha256', required=True)
    parser.add_argument('--task', required=True)
    args = parser.parse_args()
    entry, runtime = validate(args.plan, args.plan_sha256, args.task)
    spec = importlib.util.spec_from_file_location('frozen_runtime_common', COMMON)
    common = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(common)
    env = common.environment(runtime)
    for name in list(env):
        if name.upper().endswith(('API_KEY', 'API_TOKEN')):
            env.pop(name, None)
    env.update(CUDA_VISIBLE_DEVICES='', OMP_NUM_THREADS='1', MKL_NUM_THREADS='1')
    result = subprocess.run([str(runtime / 'python/bin/python3.12'), entry['scorer'],
                             *entry['scorer_argv']], cwd=ROOT, env=env, timeout=1800)
    raise SystemExit(result.returncode)


if __name__ == '__main__':
    main()
