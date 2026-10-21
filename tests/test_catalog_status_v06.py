"""Artificial aggregate records only: no cases, scheduler or model requests."""
from datetime import datetime, timedelta
import hashlib
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('catalog_v06_tracker_test', ROOT / 'scripts/build_catalog_status.py')
tracker = importlib.util.module_from_spec(spec)
spec.loader.exec_module(tracker)


class SeparateV06TrackerTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.base = Path('.local/catalog_execution_2026-10-20/tasks/V06/local_execution_v2')
        self.run = self.base / 'runtime/run_v1'
        self.now = datetime.now(tracker.PACIFIC)
        self.plan = {'task_id': 'V06', 'planned': 193, 'run_id': 'artificial-run',
                     'endpoint': 'http://127.0.0.1:1/v1', 'judge_declaration': {'model': 'artificial'}}
        plan = self.write(self.base / 'plan.json', self.plan)
        self.admission = {'admitted': True, 'task_id': 'V06', 'plan_sha256': self.sha(plan)}
        admitted = self.write(self.base / 'root_admission.json', self.admission)
        self.write(self.base / 'submission_receipt.json', {'task_id': 'V06', 'job_id': '123',
            'returncode': 0, 'plan_sha256': self.sha(plan), 'admission_sha256': self.sha(admitted)})
        self.identity = {'job_id': '123', 'plan_sha256': self.sha(plan),
            'admission_sha256': self.sha(admitted), 'endpoint': self.plan['endpoint']}

    @staticmethod
    def sha(path):
        return hashlib.sha256(path.read_bytes()).hexdigest()

    def write(self, path, value):
        target = self.root / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(json.dumps(value))
        return target

    def select(self):
        return tracker.v06_execution_evidence(self.root, self.now)

    def progress(self, stage='solver_generation', count=3, age=0):
        self.write(self.base / 'runtime/server_identity.json', self.identity)
        self.write(self.run / 'progress.json', {'at_pacific': (self.now - timedelta(seconds=age)).isoformat(),
            'stage': stage, 'solver': {'planned': 193, 'attempted_with_observed_outcome': count,
                'responses_saved': count, 'empty_finals': 0}})

    def test_submission_and_server_startup_do_not_establish_dispatch(self):
        self.assertEqual(self.select()['category'], 'queued')
        self.assertIsNone(self.select()['runtime'])
        self.write(self.base / 'runtime/status.json', {'job_id': '123',
            'stage': 'starting_independent_V06_server', 'at_pacific': self.now.isoformat()})
        self.assertEqual(self.select()['category'], 'queued')
        self.assertIn('starting its server', self.select()['status'])

    def test_prior_failed_v1_does_not_replace_admitted_v2(self):
        self.write(Path(str(self.base).replace('v2', 'v1')) / 'runtime/status.json',
            {'stage': 'stopped_for_review', 'job_id': 'old'})
        self.assertEqual(self.select()['category'], 'queued')

    def test_stale_startup_and_runtime_stop_do_not_stay_live_queued(self):
        self.write(self.base / 'runtime/status.json', {'job_id': '123',
            'stage': 'starting_independent_V06_server',
            'at_pacific': (self.now - timedelta(minutes=20)).isoformat()})
        self.assertEqual(self.select()['substatus'], 'V06_stale_startup_observation')
        self.write(self.base / 'runtime/status.json', {'stage': 'stopped_for_review',
            'at_pacific': self.now.isoformat()})
        self.assertEqual(self.select()['category'], 'agent_work')
        self.assertIsNone(self.select()['runtime'])

    def test_neutral_gate_is_development_only(self):
        self.write(self.base / 'runtime/server_identity.json', self.identity)
        self.write(self.run / 'progress.json', {'at_pacific': self.now.isoformat(), 'stage': 'neutral_delivery_gates'})
        row = self.select()
        self.assertEqual(row['category'], 'queued')
        self.assertIsNone(row['runtime']['responses_saved'])
        self.assertEqual(row['runtime']['phase'], 'neutral_development')

    def test_matching_live_progress_is_lower_bound_generation(self):
        self.progress()
        row = self.select()
        self.assertEqual(row['category'], 'running')
        self.assertEqual(row['runtime']['responses_saved'], 3)
        self.assertTrue(row['runtime']['unsealed_counts_are_lower_bounds'])

    def test_stale_or_wrong_identity_does_not_establish_running(self):
        self.progress(age=1200)
        self.assertEqual(self.select()['category'], 'agent_work')
        self.identity['job_id'] = 'foreign'
        self.write(self.base / 'runtime/server_identity.json', self.identity)
        self.assertEqual(self.select()['substatus'], 'V06_identity_reconciliation')

    def test_empty_attempt_progress_is_not_dispatch_proof(self):
        self.progress(count=0)
        self.assertNotEqual(self.select()['category'], 'running')

    def test_score_requires_locks_and_complete_full_denominator(self):
        self.progress()
        lock = {'closed': True, 'predictions_sha256': 'artificial'}
        lock_path = self.write(self.run / 'prediction_lock.json', lock)
        outcomes = self.write(self.run / 'judge_outcomes.json', [])
        judgements = self.write(self.run / 'judgements.json', [])
        self.write(self.run / 'judge_lock.json', {'closed': True, 'planned': 193,
            'prediction_lock_sha256': self.sha(lock_path), 'outcomes_sha256': self.sha(outcomes),
            'judgements_sha256': self.sha(judgements)})
        self.write(self.run / 'completion.json', {'at_pacific': self.now.isoformat(), 'stage': 'scored_terminal',
            'benchmark_primary_defined': True, 'prediction_lock_sealed': True, 'judge_outcome_lock_sealed': True,
            'released_mean_case_ratio_score': 80.0})
        score = {'judge_declaration': self.plan['judge_declaration'],
            'lock_sha256': hashlib.sha256(json.dumps(lock, sort_keys=True, separators=(',', ':')).encode()).hexdigest(),
            'groups': {'overall': {'planned': 193, 'valid': 193, 'complete': True,
                'released_mean_case_ratio_score': 80.0}}}
        self.write(self.run / 'scores.json', score)
        self.assertEqual(self.select()['category'], 'done')
        judgements.write_text('["changed"]')
        self.assertNotEqual(self.select()['category'], 'done')

    def test_changed_frozen_admission_is_rejected(self):
        self.plan['planned'] = 192
        self.write(self.base / 'plan.json', self.plan)
        self.assertIsNone(self.select())


if __name__ == '__main__':
    unittest.main()
