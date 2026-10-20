"""The automatic handoff may advance only completed, successful development."""
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

spec = importlib.util.spec_from_file_location('catalog_driver', Path(__file__).resolve().parents[1] / 'scripts/drive_catalog_20261020.py')
driver = importlib.util.module_from_spec(spec)
spec.loader.exec_module(driver)


class HandoffTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.old = driver.BASE
        self.addCleanup(setattr, driver, 'BASE', self.old)
        driver.BASE = Path(self.temp.name)
        self.folder = driver.BASE / 'tasks/P06/runtime'
        for phase in ('development', 'benchmark'):
            (self.folder / phase).mkdir(parents=True)
        self.dev = driver.BASE / 'dev.json'
        self.full = driver.BASE / 'full.json'
        self.dev.write_text(json.dumps({'planned': 12}))
        self.full.write_text(json.dumps({'planned': 1366}))
        self.entry = {'task_id': 'P06', 'development_config': str(self.dev),
                      'development_config_sha256': driver.sha(self.dev),
                      'benchmark_config': str(self.full)}

    def observe(self, ready=True):
        return driver.observe(self.entry, ready, {}, Path('identity.json'), 'http://127.0.0.1:8270/v1')

    def finish_dev(self, passed=True):
        (self.folder / 'development/completion.json').write_text(json.dumps({
            'phase': 'development', 'planned': 12, 'delivery_passed': 12 if passed else 11,
            'all_passed': passed, 'config_sha256': driver.sha(self.dev)}))

    def test_pending_pool_is_not_dispatch_or_zero_request_evidence(self):
        with patch.object(driver, 'grant') as grant:
            row = self.observe(False)
        grant.assert_not_called()
        self.assertIsNone(row['development'])
        self.assertIsNone(row['benchmark'])

    def test_ready_pool_starts_development_first(self):
        with patch.object(driver, 'grant') as grant:
            self.observe()
        self.assertEqual(grant.call_args.args[1], 'development')

    def test_failed_development_blocks_benchmark(self):
        self.finish_dev(False)
        with patch.object(driver, 'grant') as grant:
            row = self.observe()
        grant.assert_not_called()
        self.assertEqual(row['stage'], 'development_delivery_failed_benchmark_not_dispatched')

    def test_successful_development_advances_the_separate_condition(self):
        self.finish_dev()
        with patch.object(driver, 'grant') as grant:
            self.observe()
        self.assertEqual(grant.call_args.args[1], 'benchmark')

    def test_an_incomplete_full_cohort_is_not_scored_or_retried(self):
        self.finish_dev()
        (self.folder / 'benchmark/completion.json').write_text(json.dumps({'planned': 1366, 'terminal': 40}))
        with patch.object(driver, 'grant') as grant, patch.object(driver.subprocess, 'run') as scorer:
            row = self.observe()
        grant.assert_not_called()
        scorer.assert_not_called()
        self.assertEqual(row['stage'], 'generation_stopped_incomplete_no_automatic_retry')

    def test_runtime_scoring_is_cpu_only_in_the_existing_allocation(self):
        helper = driver.ROOT / 'scripts/score_catalog_in_runtime_20261020.py'
        entry = dict(self.entry, scoring_execution='existing_allocation_cpu',
                     runtime_scoring_helper_sha256=driver.sha(helper),
                     dispatch_plan='/frozen/plan.json', dispatch_plan_sha256='frozen')
        command = driver.scoring_command(entry, {'job_id': '243179'})
        self.assertIn('--jobid=243179', command)
        self.assertIn('--gres=none', command)
        self.assertIn('--cpu-bind=none', command)
        self.assertIn('--plan-sha256', command)

    def test_runtime_scoring_rejects_changed_helper(self):
        entry = dict(self.entry, scoring_execution='existing_allocation_cpu',
                     runtime_scoring_helper_sha256='wrong')
        with self.assertRaisesRegex(ValueError, 'helper changed'):
            driver.scoring_command(entry, {'job_id': '243179'})

    def test_new_vector_development_precedes_queued_vector_benchmark(self):
        entry = {'task_id': 'P12', 'prioritize_development': True}
        self.assertLess(driver.queue_key(dict(entry, task_id='P15'), 'development'),
                        driver.queue_key(entry, 'benchmark'))
        self.assertEqual(driver.queue_key({'task_id': 'P06'}, 'benchmark'), 'P06_benchmark')


if __name__ == '__main__':
    unittest.main()
