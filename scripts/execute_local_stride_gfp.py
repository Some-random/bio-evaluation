#!/usr/bin/env python3
"""Gated GFP-only200-slot generator then isolated offline CPU scorer."""
import argparse
import datetime as dt
import json
from pathlib import Path
import subprocess
import sys
import run_local_stride_gfp as runner


def validate_activation(path):
    settings,cases,_,_=runner.read_frozen_config(path)
    name=settings['scorer_python']
    if not isinstance(name,str) or Path(name).is_absolute() or '..' in Path(name).parts:
        raise ValueError('Invalid scorer interpreter path')
    python=runner.ROOT/name
    if not python.parent.resolve().is_relative_to(runner.ROOT.resolve()):
        raise ValueError('Scorer runtime escaped the project')
    if (python.parent.name!='bin' or not python.name.startswith('python')
            or python.parent.parent.name in {'.venv','.venv-vllm'}
            or not python.is_file()):
        raise ValueError('Oracle scoring requires the frozen separate CPU runtime')
    if settings.get('scorer')!=runner.SCORER or settings.get('oracle_forward_authorized') is not True:
        raise ValueError('Qualified GFP oracle scope not activated')
    runtime=runner.local_file(settings['oracle_runtime_file'],'reports')
    if runner.file_digest(runtime)!=settings['oracle_runtime_sha256']:
        raise ValueError('Frozen oracle runtime manifest changed')
    audit=runner.local_file(settings['oracle_state_audit_file'],'reports')
    if runner.file_digest(audit)!=settings['oracle_state_audit_sha256']:
        raise ValueError('Frozen trained-head restoration audit changed')
    return settings


def execute(path):
    settings=validate_activation(path);root=runner.ROOT
    result=subprocess.run([sys.executable,'-u',str(root/runner.RUNNER),'--config',str(path)],cwd=root)
    folder=root/'results/runs'/settings['run_id'];sealed=folder/'generation_artifact_lock.json'
    if not sealed.exists():return result.returncode or 1
    # The scorer must independently verify the lock and all raw payloads before
    # loading its trained oracle. No candidate or baseline forward occurs here.
    scoring=subprocess.run([str(root/settings['scorer_python']),'-u',str(root/runner.SCORER),
                            '--run',settings['run_id']],cwd=root)
    completion={'generation_exit_code':result.returncode,'scoring_exit_code':scoring.returncode,
                'finished_at_utc':dt.datetime.now(dt.timezone.utc).isoformat(),
                'generation_artifact_lock_sha256':runner.file_digest(sealed),
                'native_paper_replication':False}
    if scoring.returncode==0:
        if not (folder/'scores.json').exists() or not (folder/'scoring_output_lock.json').exists():
            raise ValueError('Scorer returned success without frozen score artifacts')
        completion['scores_sha256']=runner.file_digest(folder/'scores.json')
        completion['scoring_output_lock_sha256']=runner.file_digest(folder/'scoring_output_lock.json')
    runner.write_json(folder/'completion.json',completion)
    return result.returncode or scoring.returncode

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--config',type=Path,required=True)
    args=parser.parse_args();raise SystemExit(execute(args.config))
