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

    def continuation(self, complete=True):
        canonical = lambda data: hashlib.sha256(json.dumps(data, sort_keys=True, separators=(',', ':'), ensure_ascii=False).encode()).hexdigest()
        base = self.base.parent / 'untouched_judge_continuation_v1'
        run = base / 'runtime/run_v1'
        manifest_path = self.base.parent / 'real_input_preparation_v1/packets/manifest.json'
        manifest = [{'question_id': qid} for qid in range(193)]
        predictions = [{'question_id': qid, 'status': 'completed', 'text': 'Artificial answer.'} for qid in range(193)]
        self.write(manifest_path, manifest)
        prediction_lock = {'generation_closed': True, 'planned': 193, 'terminal_records': 193,
                           'manifest_sha256': canonical(manifest), 'predictions_sha256': canonical(predictions)}
        original_lock = self.write(self.run / 'prediction_lock.json', prediction_lock)
        self.write(self.run / 'predictions.json', predictions)
        old_outcomes = [{'question_id': qid, 'status': 'completed' if qid < 161 else
                         ('response_error' if qid == 161 else 'not_dispatched_after_stop'),
                         'request_sha256': canonical({'request': qid}),
                         'raw_response_sha256': canonical({'response': qid})} for qid in range(193)]
        original_outcomes = self.write(self.run / 'judge_outcomes.json', old_outcomes)
        original_judgements = self.write(self.run / 'judgements.json', [])
        self.write(self.run / 'judge_lock.json', {'closed': True, 'planned': 193,
            'prediction_lock_sha256': self.sha(original_lock), 'outcomes_sha256': self.sha(original_outcomes),
            'judgements_sha256': self.sha(original_judgements)})
        configuration = {'max_tokens': 16384, 'chat_template_kwargs': {'enable_thinking': False}}
        self.plan.update(model_configuration=configuration, manifest=str(self.root / manifest_path))
        source_plan = self.write(self.base / 'plan.json', self.plan)
        plan = {**self.plan, 'run_id': 'artificial-continuation', 'condition': 'ARTIFICIAL_REPAIR',
                'execution_scope': 'retained_V06_judge_untouched31_full193closure',
                'new_judge_planned': 31, 'new_solver_calls_planned': 0, 'gpus_requested': 1,
                'source_plan_path': str(source_plan), 'source_plan_sha256': self.sha(source_plan),
                'source_output_root': str(self.root / self.run), 'output_root': str(self.root / run)}
        plan_path = self.write(base / 'plan.json', plan)
        admission = self.write(base / 'root_admission.json', {'admitted': True, 'task_id': 'V06',
            'plan_sha256': self.sha(plan_path), 'gpu_count': 1, 'project_gpu_ceiling': 8,
            'scope': 'judge_untouched31_once_reuse_locked193solver_and162judge'})
        self.write(base / 'submission_receipt.json', {'task_id': 'V06', 'job_id': '456', 'returncode': 0,
            'plan_sha256': self.sha(plan_path), 'admission_sha256': self.sha(admission)})
        self.write(base / 'runtime/server_identity.json', {'job_id': '456', 'plan_sha256': self.sha(plan_path),
            'admission_sha256': self.sha(admission), 'endpoint': plan['endpoint']})
        if not complete:
            return base, run
        copied_lock = self.write(run / 'source_prediction_lock.json', prediction_lock)
        outcomes = self.write(run / 'judge_outcomes.json', [{**row, 'status': 'completed'} for row in old_outcomes])
        judgements = [{'question_id': qid, 'reference_score': 6, 'candidate_score': 4, 'comment': 'Artificial assessment.',
                       'judge_declaration_sha256': canonical(plan['judge_declaration'])} for qid in range(193)]
        judgement_path = self.write(run / 'judgements.json', judgements)
        self.write(run / 'judge_lock.json', {'closed': True, 'planned': 193, 'reused_raw_responses': 162,
            'execution_condition': plan['condition'], 'source_prediction_lock_sha256': self.sha(copied_lock),
            'judge_declaration_sha256': canonical(plan['judge_declaration']),
            'outcomes_sha256': self.sha(outcomes), 'judgements_sha256': self.sha(judgement_path)})
        value = 100 * sum(4.0 / 6.0 for _ in range(193)) / 193
        self.write(run / 'scores.json', {'execution_condition': plan['condition'],
            'judge_declaration': plan['judge_declaration'], 'lock_sha256': canonical(prediction_lock),
            'groups': {'overall': {'planned': 193, 'valid': 193, 'complete': True,
                'released_mean_case_ratio_score': value}}})
        completion = {'at_pacific': self.now.isoformat(), 'stage': 'scored_terminal',
            'execution_condition': plan['condition'], 'benchmark_primary_defined': True,
            'released_mean_case_ratio_score': value, 'source_solver_responses_reused': 193,
            'source_judge_responses_reused': 162, 'new_solver_calls': 0,
            'judge': {'planned': 193, 'responses_saved': 193},
            'new_judge': {'planned': 31, 'attempted_with_observed_outcome': 31, 'responses_saved': 31}}
        completion_path = self.write(run / 'completion.json', completion)
        self.write(base / 'runtime/terminal_receipt.json', {'job_id': '456', 'completion': completion,
            'completion_sha256': self.sha(completion_path)})
        return base, run

    def test_admitted_complete_continuation_preferred_with_combined_source_locks(self):
        base, run = self.continuation()
        row = self.select()
        self.assertEqual(row['category'], 'done')
        self.assertEqual(row['substatus'], 'defined_V06_untouched_judge_continuation_score')
        self.assertEqual(row['runtime']['active_job_id'], '456')
        self.assertEqual(row['runtime']['responses_saved'], 193)
        self.assertIn(str(run / 'source_prediction_lock.json'), row['evidence_paths'])

    def test_continuation_submission_without_progress_is_not_dispatch(self):
        self.continuation(complete=False)
        row = self.select()
        self.assertEqual(row['category'], 'queued')
        self.assertIsNone(row['runtime'])

    def test_corrupt_combined_judge_lock_cannot_fall_back_to_done(self):
        _, run = self.continuation()
        self.write(run / 'judgements.json', [])
        row = self.select()
        self.assertEqual(row['category'], 'agent_work')
        self.assertEqual(row['substatus'], 'V06_continuation_lock_or_score_reconciliation')

    def test_changed_source_lock_binding_rejects_complete_claim(self):
        _, run = self.continuation()
        self.write(run / 'source_prediction_lock.json', {'foreign': True})
        self.assertEqual(self.select()['category'], 'agent_work')

    def test_incomplete_continuation_never_promotes_saved_replies(self):
        base, run = self.continuation()
        completion = json.loads((self.root / run / 'completion.json').read_text())
        completion.update(benchmark_primary_defined=False, stage='terminal_incomplete_primary_undefined')
        completion['new_judge']['responses_saved'] = 30
        self.write(run / 'completion.json', completion)
        self.assertEqual(self.select()['category'], 'agent_work')

    def test_unadmitted_continuation_is_reconciled_not_historical_done(self):
        base, _ = self.continuation()
        self.write(base / 'root_admission.json', {'admitted': False})
        self.assertEqual(self.select()['category'], 'agent_work')


if __name__ == '__main__':
    unittest.main()
