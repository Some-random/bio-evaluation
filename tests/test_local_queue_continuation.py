"""Synthetic process mocks verify terminal failures never trigger resampling."""
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import continue_independent_local_jobs as controller
import run_local_benchmark_queue_replicas as worker


class ContinuationTests(unittest.TestCase):
    def fixture(self, root):
        (root / 'configs').mkdir()
        (root / 'scripts').mkdir()
        (root / 'scripts/executor.py').write_text('# synthetic mock only\n')
        jobs = []
        for i in [0, 1]:
            name = f'configs/task{i}.json'
            (root / name).write_text(json.dumps({'run_id': f'synthetic{i}', 'gpu_ids': [2]}))
            jobs.append({'config': name, 'executor': 'scripts/executor.py'})
        queue = root / 'configs/queue.json'
        queue.write_text(json.dumps({'jobs': jobs, 'accept_more': False}))
        return queue, root / '.local/queue'

    def test_failure_continues_other_job_and_both_are_never_resubmitted(self):
        with tempfile.TemporaryDirectory() as name:
            root = Path(name)
            queue, state = self.fixture(root)
            codes = iter([7, 0])
            def result(*args, **kwargs):
                return type('Result', (), {'returncode': next(codes)})()
            with patch.object(worker, 'ROOT', root), patch.object(worker.subprocess, 'run', side_effect=result) as call:
                worker.run(queue, state)
                self.assertEqual(call.call_count, 2)
                progress = json.loads((state / 'progress.json').read_text())
                self.assertEqual(progress['finished']['configs/task0.json']['exit_code'], 7)
                self.assertEqual(progress['gpu_ids'], [2])
                self.assertEqual(progress['stage'], 'completed')
                worker.run(queue, state)
                self.assertEqual(call.call_count, 2)

    def test_legacy_terminal_failure_without_manifest_is_preserved(self):
        with tempfile.TemporaryDirectory() as name:
            root = Path(name)
            queue, state = self.fixture(root)
            state.mkdir(parents=True)
            (state / 'progress.json').write_text(json.dumps({'queue': str(queue), 'finished': {
                'configs/task0.json': {'run_id': 'synthetic0', 'exit_code': 9}}}))
            with patch.object(worker, 'ROOT', root), patch.object(worker.subprocess, 'run', return_value=type('Result', (), {'returncode': 0})()) as call:
                worker.run(queue, state)
                self.assertEqual(call.call_count, 1)
                self.assertTrue(call.call_args.args[0][-1].endswith('task1.json'))

    def test_uncertain_active_process_never_qualifies_for_automatic_restart(self):
        terminal = {'stage': 'stopped_after_run_error', 'active_run': 'synthetic', 'active_config_sha256': 'frozen',
                    'finished': {'config': {'run_id': 'synthetic', 'exit_code': 7}}}
        self.assertTrue(controller.eligible(terminal))
        self.assertFalse(controller.eligible({**terminal, 'stage': 'running'}))
        self.assertFalse(controller.eligible({**terminal, 'finished': {}}))
        self.assertFalse(controller.eligible({**terminal, 'active_config_sha256': None}))


if __name__ == '__main__':
    unittest.main()
