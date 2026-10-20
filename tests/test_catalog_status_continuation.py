"""Synthetic successor metadata only; no inference, scoring or scheduler calls."""
from datetime import datetime, timedelta
import hashlib
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('catalog_status_continuation_test', ROOT / 'scripts/build_catalog_status.py')
tracker = importlib.util.module_from_spec(spec)
spec.loader.exec_module(tracker)


class ContinuationTrackerTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.base = Path('.local/catalog_execution_2026-10-20/continuation_v1')
        self.now = datetime.now(tracker.PACIFIC)
        self.tasks = ('P12', 'P13', 'P14', 'P15')
        manifest = self.write(self.base / 'manifest.json', {
            'task_ids': list(self.tasks), 'original_job_id': '243179'})
        self.manifest_sha = self.sha(manifest)
        self.write(self.base / 'submission_receipt.json', {'job_id': '243499'})
        identity = self.write(self.base / 'runtime/server_identity.json', {'job_id': '243499'})
        self.identity_sha = self.sha(identity)
        self.write(self.base / 'runtime/predecessor_terminal_receipt.json', {
            'successor_job_id': '243499', 'original_job_id': '243179', 'original_job_state': 'TIMEOUT'})
        self.pool = {'stage': 'serving_task_queue', 'job_id': '243499',
            'updated_at_pacific': self.now.isoformat(),
            'active_clients': [task + '_benchmark_continuation1' for task in self.tasks[:3]]}
        self.write(self.base / 'runtime/status.json', self.pool)
        self.direct = {}
        for task in self.tasks:
            boundary = self.write(self.base / 'runtime' / (task + '_boundary.json'), {'config_sha256': 'frozen-config'})
            self.write(self.base / 'runtime/queue' / (task + '_benchmark_continuation1.grant.json'), {
                'authorized': True, 'task_id': task, 'run_id': 'run-' + task,
                'config_sha256': 'frozen-config', 'server_identity_sha256': self.identity_sha,
                'continuation_boundary_sha256': self.sha(boundary)})
            if task != 'P15':
                self.write(self.base / 'runtime/queue' / (task + '_benchmark_continuation1.started.json'), {'pid': 123})
            for suffix in ('grant', 'started', 'finished'):
                self.write(Path('.local/catalog_execution_2026-10-20/runtime/queue') /
                    ('10_' + task + '_benchmark.' + suffix + '.json'), {'exit_code': 1, 'historical_permission_drain': True})
            self.direct[task] = {'run_id': 'run-' + task, 'config_sha256': 'frozen-config',
                'planned': 100, 'responses_saved': 0 if task == 'P15' else 10,
                'at_pacific': self.now.isoformat()}
            self.write(Path('.local/catalog_execution_2026-10-20/tasks') / task /
                'runtime/benchmark/progress.json', self.direct[task])

    def write(self, relative, value):
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(value))
        return path

    @staticmethod
    def sha(path):
        return hashlib.sha256(path.read_bytes()).hexdigest()

    def selected(self, task='P12'):
        with patch.object(tracker, 'CONTINUATION_MANIFEST_SHA256', self.manifest_sha):
            return tracker.task_queue_evidence(self.root, task, self.direct[task], self.now)

    def test_successor_grant_ignores_predecessor_permission_drain_exit(self):
        row = self.selected()
        self.assertTrue(row['continuation'])
        self.assertEqual(row['job_id'], '243499')
        self.assertTrue(row['started'].is_file())
        self.assertFalse(row['finished'].exists())
        self.assertTrue(row['active_client'])

    def test_pending_successor_is_queued_despite_old_finished_marker(self):
        row = self.selected('P15')
        self.assertTrue(row['continuation'])
        self.assertTrue(row['grant'].is_file())
        self.assertFalse(row['started'].exists())
        self.assertFalse(row['active_client'])

    def test_stale_pool_is_not_promoted_to_live_successor(self):
        self.pool['updated_at_pacific'] = (self.now - timedelta(minutes=10)).isoformat()
        self.write(self.base / 'runtime/status.json', self.pool)
        self.assertFalse(self.selected()['continuation'])

    def test_identity_or_boundary_hash_mismatch_does_not_select_successor(self):
        self.write(self.base / 'runtime/server_identity.json', {'job_id': 'foreign'})
        self.assertFalse(self.selected()['continuation'])

    def test_full_tracker_counts_running_and_queued_from_successor(self):
        retained = ([f'P{i:02}' for i in range(1, 45) if i not in (28, 29)]
            + [f'B{i:02}' for i in range(1, 9)] + [f'V{i:02}' for i in range(1, 8)])
        rows = [{'task_id': task, 'task': 'Synthetic setting ' + task,
                 'source_row_category': 'completed_rows' if task not in self.tasks else 'unrun'}
                for task in retained]
        self.write('reports/EVALUATION_DECISION_TABLE.json', {'retained_setting_ids': retained,
            'rows': rows, 'generated_at_pacific': self.now.isoformat()})
        # Dense-output generation can have quiet intervals; a fresh matching
        # successor's active-client record remains independent runtime evidence.
        self.direct['P13']['at_pacific'] = (self.now - timedelta(minutes=20)).isoformat()
        self.write('.local/catalog_execution_2026-10-20/tasks/P13/runtime/benchmark/progress.json', self.direct['P13'])
        with patch.object(tracker, 'CONTINUATION_MANIFEST_SHA256', self.manifest_sha):
            data = tracker.build(self.root)
        self.assertEqual(data['counts']['running'], 3)
        self.assertEqual(data['counts']['queued'], 1)
        self.assertEqual(data['counts']['agent_work'], 0)
        self.assertEqual(data['counts']['done'], 53)
        self.assertEqual(sum(data['counts'].values()), 57)
        p13 = next(row for row in data['rows'] if row['task_id'] == 'P13')
        self.assertEqual(p13['runtime']['active_job_id'], '243499')
        self.assertIn('predecessor drain exits remain historical', ' '.join(p13['scope_notes']))


if __name__ == '__main__':
    unittest.main()
