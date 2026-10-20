#!/usr/bin/env python3
"""Wait for the frozen complete P08 seal, then score P09 once without inference."""
import datetime
import fcntl
import hashlib
import json
from pathlib import Path
import subprocess
import time
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parents[1]
TASK = ROOT / '.local/catalog_execution_2026-10-20/tasks/P09'
P08 = TASK.parent / 'P08/runtime/benchmark'


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def stamp():
    return datetime.datetime.now(ZoneInfo('America/Los_Angeles')).isoformat()


def write(path, data):
    temporary = path.with_suffix('.tmp')
    temporary.write_text(json.dumps(data, indent=2) + '\n')
    temporary.replace(path)


def ready():
    path = P08 / 'completion.json'
    if not path.exists():
        return False
    completion = json.loads(path.read_text())
    if completion['planned'] != 12851 or completion['terminal'] != 12851:
        raise ValueError('P08 terminal cohort is incomplete; no automatic retry')
    if completion['prediction_lock_sha256'] != sha(P08 / 'prediction_lock.json'):
        raise ValueError('P08 prediction seal changed')
    return True


def main():
    import argparse
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--command-sha256', required=True)
    parser.add_argument('--scorer-sha256', required=True)
    args = parser.parse_args()
    command = TASK / 'scoring_command.json'
    status = TASK / 'scoring_watcher_status.json'
    with (TASK / 'scoring_watcher.lock').open('a') as handle:
        fcntl.flock(handle, fcntl.LOCK_EX | fcntl.LOCK_NB)
        if (TASK / 'scoring_attempt.json').exists():
            return
        while not (TASK / 'STOP_SCORING').exists():
            if sha(command) != args.command_sha256 or sha(TASK / 'score.py') != args.scorer_sha256:
                raise ValueError('Frozen P09 scoring command or implementation changed')
            if ready():
                request = json.loads(command.read_text())
                with (TASK / 'scoring_attempt.json').open('x') as record:
                    json.dump({'started_at_pacific': stamp(), 'command_sha256': sha(command),
                               'p08_prediction_lock_sha256': sha(P08 / 'prediction_lock.json')}, record)
                write(status, {'updated_at_pacific': stamp(), 'stage': 'one_offline_attempt_running',
                               'new_inference_calls': 0})
                with (TASK / 'scoring_watcher.log').open('x') as log:
                    result = subprocess.run(request['argv'], cwd=ROOT, stdout=log,
                                            stderr=subprocess.STDOUT, timeout=1800)
                output = TASK / 'scores.json'
                write(status, {'updated_at_pacific': stamp(), 'stage': 'scored_terminal' if result.returncode == 0 and output.exists() else 'failed_no_automatic_retry',
                               'exit_code': result.returncode, 'score_sha256': sha(output) if output.exists() else None,
                               'new_inference_calls': 0, 'full_retained_catalog_complete': False})
                return
            write(status, {'updated_at_pacific': stamp(), 'stage': 'waiting_for_complete_P08_prediction_lock',
                           'new_inference_calls': 0, 'benchmark_generation_by_this_watcher': False})
            time.sleep(30)


if __name__ == '__main__':
    main()
