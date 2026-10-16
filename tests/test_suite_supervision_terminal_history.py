"""Terminal queue errors must not be confused with successful evaluations."""
from pathlib import Path
import json
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from supervise_local_suite import terminal_failed_run, completion_failed, aggregate_status


class TerminalHistoryTests(unittest.TestCase):
    def test_only_explicit_matching_nonzero_terminal_exit_is_a_failure(self):
        history = {'config': {'run_id': 'run', 'exit_code': 7}}
        self.assertTrue(terminal_failed_run('config', 'run', history))
        self.assertFalse(terminal_failed_run('config', 'other_run', history))
        self.assertFalse(terminal_failed_run('other_config', 'run', history))
        for code in [None, 0, False, True, '7']:
            self.assertFalse(terminal_failed_run('config', 'run', {'config': {'run_id': 'run', 'exit_code': code}}))

    def test_audited_pathvqa_shard_is_not_a_failed_full_scorer(self):
        record = {'generation_exit_code': 0, 'generation_audit_exit_code': 0,
                  'scoring_exit_code': None, 'case_scope': 'task_shard_only',
                  'shard_scoring_performed': False, 'status': 'generation_audited'}
        self.assertFalse(completion_failed(record))
        for patch in ({'generation_audit_exit_code': 1}, {'generation_exit_code': 1},
                      {'case_scope': 'whole_task'}, {'status': 'generation_audit_failed'}):
            self.assertTrue(completion_failed({**record, **patch}))
        self.assertTrue(completion_failed({'generation_exit_code': 0, 'scoring_exit_code': None}))

    def test_reporting_waits_for_full_union_after_last_shard(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            cfg = root / 'configs/local_pathvqa_seven_gpu_aggregate.json'
            cfg.parent.mkdir()
            cfg.write_text(json.dumps({'run_id': 'whole', 'approved_task_ids': ['V03']}))
            # Successful source termination cannot stand in for the aggregate.
            history = {'shard_cfg': {'run_id': 'shard', 'exit_code': 0}}
            self.assertEqual(aggregate_status(str(cfg.relative_to(root)), [('shard_cfg', 'shard')], history, root)['status'], 'pending')
            folder = root / 'results/runs/whole'
            folder.mkdir(parents=True)
            (folder / 'completion.json').write_text(json.dumps({'generation_exit_code': 0, 'scoring_exit_code': 0}))
            self.assertEqual(aggregate_status(str(cfg.relative_to(root)), [], history, root)['status'], 'complete')

    def test_missing_terminal_source_and_blocked_union_are_not_pending_forever(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            cfg = root / 'configs/local_description_p23_aggregate.json'
            cfg.parent.mkdir()
            cfg.write_text(json.dumps({'run_id': 'whole', 'approved_task_ids': ['P23']}))
            history = {'shard_cfg': {'run_id': 'shard', 'exit_code': 1}}
            result = aggregate_status(str(cfg.relative_to(root)), [('shard_cfg', 'shard')], history, root)
            self.assertEqual(result['status'], 'blocked')
            reports = root / 'reports'
            reports.mkdir()
            (reports / 'local_description_shard_aggregation.json').write_text(json.dumps({'tasks': {'P23': {'status': 'blocked', 'detail': 'source integrity failed'}}}))
            result = aggregate_status(str(cfg.relative_to(root)), [], {}, root)
            self.assertEqual(result['status'], 'blocked')
            self.assertEqual(result['reason'], 'source integrity failed')


if __name__ == '__main__':
    unittest.main()
