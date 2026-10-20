"""Separately frozen publication repair; no inference, scoring or retries."""
from datetime import datetime
import argparse
import fcntl
import hashlib
import importlib.util
import io
import json
import os
from pathlib import Path
import signal
import subprocess
import tarfile
import time
from zoneinfo import ZoneInfo

ROOT = Path('/dfs/scratch0/dongweij/bio-evaluation')
BASE = ROOT / '.local/catalog_execution_2026-10-20'
WORK = BASE / 'publication_repair_continuation_v1'
OLD = BASE / 'publication_watcher'
RECEIPT = ROOT / '.local/catalog_resume_2026-10-19/publication/catalog_p07_p08_continuation_reporting_repair_20261020_publication_receipt.json'
MANIFEST_SHA = '64b1f81dfa7a138458905736545ecb93f592c7cd85dc8528b6621ca125b260d4'


def stamp():
    return datetime.now(ZoneInfo('America/Los_Angeles')).isoformat()


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def read(path):
    return json.loads(Path(path).read_text())


def save(path, value):
    temp = path.with_suffix('.tmp')
    temp.write_text(json.dumps(value, indent=2, sort_keys=True) + '\n')
    temp.replace(path)


def status(stage, **extra):
    save(WORK / 'status.json', {'role': 'separate_report_accuracy_and_publication_repair_only',
        'stage': stage, 'updated_at_pacific': stamp(), 'pid': os.getpid(),
        'new_inference_calls': 0, 'new_scoring_attempts': 0,
        'original_inference_protocols_changed': False, **extra})


def process(pid):
    path = Path('/proc') / str(pid)
    try:
        fields = (path / 'stat').read_text().split(') ', 1)[1].split()
        return {'state': fields[0], 'start_ticks': fields[19],
                'exit_code': int(fields[49]), 'cmdline': (path / 'cmdline').read_bytes()}
    except FileNotFoundError:
        return None


def module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result


def run(argv, name):
    with (WORK / (name + '.log')).open('x') as log:
        child = subprocess.Popen(argv, cwd=ROOT, stdout=log, stderr=subprocess.STDOUT)
        while child.poll() is None:
            status('repair_step_running', step=name, child_pid=child.pid)
            time.sleep(10)
        if child.returncode:
            raise RuntimeError('Report-only step failed: ' + name)


def provenance():
    """Export a separately named hash-linked continuation metadata sidecar."""
    base = BASE / 'continuation_v1'
    assert sha((base / 'manifest.json').read_bytes()) == MANIFEST_SHA
    names = ['manifest.json', 'submission_receipt.json', 'request_permission_drain.json',
             'runtime/predecessor_terminal_receipt.json', 'runtime/server_identity.json',
             'runtime/runtime_version_manifest.json']
    for task in ('P12', 'P13', 'P14', 'P15'):
        names += ['runtime/' + task + '_boundary.json',
                  'runtime/queue/' + task + '_benchmark_continuation1.grant.json']
        for suffix in ('started', 'finished'):
            relative = 'runtime/queue/' + task + '_benchmark_continuation1.' + suffix + '.json'
            if (base / relative).is_file():
                names.append(relative)
    raw = {name: (base / name).read_bytes() for name in names}
    hashes = {name: sha(content) for name, content in raw.items()}
    digest = sha(json.dumps(hashes, sort_keys=True).encode())
    relative = Path('results/protocol_artifacts') / ('catalog_continuation_20261020_' + digest[:12] + '_provenance.tar.gz')
    archive = ROOT / relative
    manifest = archive.with_suffix('.manifest.json')
    assert not archive.exists() and not manifest.exists()
    archive.parent.mkdir(parents=True, exist_ok=True)
    with tarfile.open(archive, 'w:gz') as handle:
        for name, content in sorted(raw.items()):
            info = tarfile.TarInfo(name)
            info.size = len(content)
            info.mtime = 0
            handle.addfile(info, io.BytesIO(content))
    save(manifest, {'schema_version': 1, 'captured_at_pacific': stamp(),
        'role': 'separate_continuation_identity_grant_and_boundary_provenance',
        'continuation_manifest_sha256': MANIFEST_SHA, 'source_files_sha256': hashes,
        'archive_sha256': sha(archive.read_bytes()), 'member_count': len(raw),
        'new_inference_calls': 0, 'new_scoring_attempts': 0,
        'scorer_references_included': False, 'model_weights_included': False,
        'credentials_included': False, 'prior_trajectory_archives_modified': False})
    return [str(relative), str(manifest.relative_to(ROOT))]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--manifest-sha256', required=True)
    args = parser.parse_args()
    config_path = WORK / 'manifest.json'
    assert sha(config_path.read_bytes()) == args.manifest_sha256
    config = read(config_path)
    with (WORK / 'worker.lock').open('a') as singleton:
        fcntl.flock(singleton, fcntl.LOCK_EX | fcntl.LOCK_NB)
        if RECEIPT.exists():
            status('already_published_terminal', publication_receipt=str(RECEIPT))
            return
        if (WORK / 'attempt_started.json').exists():
            status('prior_repair_attempt_preserved_no_automatic_retry')
            return
        # The predecessor observer remains stopped while its export child
        # completes. No scorer, inference client, GPU or export child is killed.
        while True:
            child = process(config['export_child_pid'])
            if child is None or child['state'] == 'Z':
                if child and child['exit_code'] != 0:
                    raise RuntimeError('Original export child failed; preserve its evidence')
                break
            status('waiting_for_existing_export_child', child_pid=config['export_child_pid'],
                   child_state=child['state'])
            time.sleep(15)
        exported = read(ROOT / 'reports/CATALOG_NEW_SCORES_2026-10-20.json')
        exported_ids = {r['task_id'] for r in exported['completed_rows'] + exported.get('diagnostic_only_finished_runs', [])}
        assert {'P07', 'P08'} <= exported_ids
        old = process(config['observer_pid'])
        if old:
            assert old['start_ticks'] == config['observer_start_ticks'] and old['state'] == 'T'
            assert b'publication_watcher/worker.py' in old['cmdline']
            os.kill(config['observer_pid'], signal.SIGKILL)
        save(WORK / 'observer_retirement_receipt.json', {
            'at_pacific': stamp(), 'retired_observer_pid': config['observer_pid'],
            'retired_start_ticks': config['observer_start_ticks'],
            'export_child_finished_before_retirement': True,
            'old_observer_code_config_logs_and_attempt_preserved': True,
            'scorer_inference_and_gpu_processes_touched': False})
        with (ROOT / '.local/catalog_report_generation.lock').open('a') as generator:
            fcntl.flock(generator, fcntl.LOCK_EX)
            for name, expected in config['files_sha256'].items():
                assert sha(Path(name).read_bytes()) == expected, 'Frozen report-repair support changed'
            save(WORK / 'attempt_started.json', {'at_pacific': stamp(),
                'role': 'one_attempt_report_accuracy_repair_and_publication',
                'new_inference_calls': 0, 'new_scoring_attempts': 0})
            run(['/usr/bin/python3', '-m', 'unittest', '-v', 'tests/test_catalog_status_continuation.py'], 'tests')
            run(['/usr/bin/python3', str(ROOT / 'scripts/update_evaluation_decision_table.py')], 'decision_table')
            run(['/usr/bin/python3', str(ROOT / 'scripts/build_catalog_status.py')], 'tracker')
            extras = provenance()
            publisher = module('separate_catalog_report_repair_publisher', OLD / 'publish.py')
            publisher.STATIC = tuple(publisher.STATIC) + tuple(extras) + (
                'reports/CATALOG_RUNTIME_IO_2026-10-20.json',
                'scripts/repair_catalog_publication_20261020.py',
                'tests/test_catalog_status_continuation.py')
            status('publishing_repaired_tracker_and_completed_scores')
            publisher.publish(RECEIPT, ['P07', 'P08'])
        receipt = read(RECEIPT)
        assert receipt['remote_bytes_verified'] is True
        status('published_terminal', commit_sha=receipt['commit_sha'],
            publication_receipt=str(RECEIPT), tracker_counts=receipt['tracker_counts'],
            public_tracker_url=receipt['public_tracker_url'], remote_bytes_verified=True,
            continuation_provenance_paths=extras)


if __name__ == '__main__':
    try:
        main()
    except Exception as error:
        status('failed_report_repair_preserved_no_automatic_retry', error_type=type(error).__name__)
        raise
