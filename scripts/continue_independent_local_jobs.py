"""Continue authorized queues after a terminal task failure; never retry cases.

Healthy or uncertain active jobs are never stopped or restarted. This one-time
controller ends once every queue is sealed and drained, including failures.
"""
import datetime as dt
import fcntl
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parents[1]


def save(path, value):
    temporary = path.with_suffix('.tmp')
    temporary.write_text(json.dumps(value, indent=2) + '\n')
    temporary.replace(path)


def eligible(progress):
    """A vanished active worker is uncertain; only explicit terminal errors qualify."""
    if progress.get('stage') != 'stopped_after_run_error':
        return False
    active = progress.get('active_run')
    return bool(active and progress.get('active_config_sha256') and any(
        row.get('run_id') == active and type(row.get('exit_code')) is int
        and row['exit_code'] != 0 for row in progress.get('finished', {}).values()))


def alive(pid):
    path = Path(f'/proc/{pid}/stat')
    if not path.exists():
        return False
    return path.read_text().rsplit(') ', 1)[1].split()[0] != 'Z'


def run():
    state = ROOT / '.local/local_queue_continuation'
    state.mkdir(parents=True, exist_ok=True)
    lock = (state / 'controller.lock').open('a')
    fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
    report_path = ROOT / 'reports/local_queue_continuation.json'
    prior = json.loads(report_path.read_text()) if report_path.exists() else {}
    attempts = prior.get('terminal_events_resumed', {})
    while True:
        states = {}
        queues = sorted((ROOT / 'configs').glob('local_benchmark_queue*.json'))
        drained = bool(queues)
        for queue_path in queues:
            queue = json.loads(queue_path.read_text())
            suffix = queue_path.stem.removeprefix('local_benchmark_queue')
            directory = ROOT / ('.local/local_benchmark_queue' + suffix)
            progress_path = directory / 'progress.json'
            if not progress_path.exists():
                states[queue_path.name] = 'no_worker_history_no_automatic_start'
                drained = False
                continue
            raw = progress_path.read_bytes()
            progress = json.loads(raw)
            keys = {job['config'] for job in queue['jobs']}
            finished = set(progress.get('finished', {}))
            drained &= not queue.get('accept_more', False) and keys <= finished
            process_path = directory / 'worker_process.json'
            process = json.loads(process_path.read_text()) if process_path.exists() else {}
            if alive(process.get('pid', -1)):
                states[queue_path.name] = 'existing_worker_untouched'
                continue
            event = hashlib.sha256(raw).hexdigest()
            if not eligible(progress):
                states[queue_path.name] = 'terminal_or_uncertain_no_automatic_restart'
                continue
            if event in attempts:
                states[queue_path.name] = 'continuation_already_attempted_no_duplicate'
                continue
            active_config = next((name for name, row in progress['finished'].items()
                                  if row.get('run_id') == progress['active_run']), None)
            if (active_config not in keys or hashlib.sha256((ROOT / active_config).read_bytes()).hexdigest()
                    != progress['active_config_sha256']):
                states[queue_path.name] = 'terminal_identity_changed_no_automatic_restart'
                continue
            log = ROOT / 'logs/local_suite' / (queue_path.stem + '_continuation.log')
            with log.open('ab') as handle:
                child = subprocess.Popen([sys.executable, '-u', str(ROOT / 'scripts/run_local_benchmark_queue_replicas.py'),
                    '--queue', str(queue_path), '--state-dir', str(directory)], cwd=ROOT,
                    stdin=subprocess.DEVNULL, stdout=handle, stderr=subprocess.STDOUT, start_new_session=True)
            attempts[event] = {'queue': queue_path.name, 'new_worker_pid': child.pid,
                'failed_run_preserved_not_retried': progress['active_run'],
                'continued_at_utc': dt.datetime.now(dt.timezone.utc).isoformat()}
            states[queue_path.name] = 'independent_remaining_jobs_continued'
        save(report_path, {'pid': os.getpid(), 'updated_at_utc': dt.datetime.now(dt.timezone.utc).isoformat(),
            'stage': 'drained' if drained else 'monitoring_existing_one_time_queues',
            'terminal_events_resumed': attempts, 'queue_states': states,
            'failed_or_uncertain_generations_retried': False, 'healthy_workers_stopped': False,
            'new_evaluation_scope_added': False, 'provider_calls': False})
        if drained:
            return
        time.sleep(30)


if __name__ == '__main__':
    run()
