"""Central dispatch must reject task/scope/hash/gate substitutions before calls."""
import copy
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

spec = importlib.util.spec_from_file_location('catalog_pool', Path(__file__).resolve().parents[1] / 'scripts/serve_catalog_20261020.py')
pool = importlib.util.module_from_spec(spec)
spec.loader.exec_module(pool)


class DispatchGrantTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.original = pool.ROOT, pool.BASE
        self.addCleanup(self.restore)
        pool.ROOT = Path(self.temp.name)
        pool.BASE = pool.ROOT / '.local/catalog_execution_2026-10-20/runtime'
        pool.BASE.mkdir(parents=True)
        self.task = pool.ROOT / '.local/catalog_execution_2026-10-20/tasks/P06'
        self.task.mkdir(parents=True)
        self.runner = pool.ROOT / 'scripts/runner.py'
        self.runner.parent.mkdir()
        self.runner.write_text('synthetic runner fixture')
        self.config = self.task / 'config.json'
        self.config.write_text('{}')
        self.identity = pool.BASE / 'server_identity.json'
        self.identity.write_text('{}')
        self.plan = {'authorized_task_ids': ['P06'], 'allowed_runner_paths': ['scripts/runner.py'],
                     'endpoint': 'http://127.0.0.1:8270/v1'}
        self.grant = {'authorized': True, 'task_id': 'P06', 'runner': str(self.runner), 'runner_sha256': pool.sha(self.runner),
                      'config': str(self.config), 'config_sha256': pool.sha(self.config), 'phase': 'development',
                      'endpoint': self.plan['endpoint'], 'server_identity_file': str(self.identity),
                      'server_identity_sha256': pool.sha(self.identity), 'argv': ['--config', str(self.config)]}

    def restore(self):
        pool.ROOT, pool.BASE = self.original

    def test_exact_development_grant_passes(self):
        self.assertEqual(pool.validate_grant(self.grant, self.plan), self.runner)

    def test_preparation_without_authorization_is_rejected(self):
        self.grant['authorized'] = False
        with self.assertRaises(ValueError): pool.validate_grant(self.grant, self.plan)

    def test_held_task_cannot_use_another_tasks_grant(self):
        self.grant['task_id'] = 'P18'
        with self.assertRaises(ValueError): pool.validate_grant(self.grant, self.plan)

    def test_changed_runner_is_rejected(self):
        self.runner.write_text('different code')
        with self.assertRaises(ValueError): pool.validate_grant(self.grant, self.plan)

    def test_foreign_config_is_rejected_even_with_matching_hash(self):
        other = self.task.parent / 'P07'
        other.mkdir()
        config = other / 'config.json'
        config.write_text('{}')
        self.grant.update(config=str(config), config_sha256=pool.sha(config), argv=['--config', str(config)])
        with self.assertRaises(ValueError): pool.validate_grant(self.grant, self.plan)

    def test_endpoint_substitution_is_rejected(self):
        self.grant['endpoint'] = 'https://api.example.com/v1'
        with self.assertRaises(ValueError): pool.validate_grant(self.grant, self.plan)

    def benchmark_grant(self, passed):
        done = self.task / 'completion.json'
        done.write_text(json.dumps({'phase': 'development', 'planned': 12,
            'delivery_passed': 12 if passed else 11, 'all_passed': passed,
            'empty_finals': 0 if passed else 1, 'truncations': 0,
            'transport_or_response_errors': 0}))
        grant = copy.deepcopy(self.grant)
        grant.update(phase='benchmark', development_completion=str(done), development_completion_sha256=pool.sha(done))
        return grant

    def test_failed_development_cannot_dispatch_benchmark(self):
        with self.assertRaises(ValueError): pool.validate_grant(self.benchmark_grant(False), self.plan)

    def test_passing_sealed_development_allows_new_benchmark_condition(self):
        self.assertEqual(pool.validate_grant(self.benchmark_grant(True), self.plan), self.runner)

    def test_changed_development_evidence_is_rejected(self):
        grant = self.benchmark_grant(True)
        Path(grant['development_completion']).write_text('{}')
        with self.assertRaises(ValueError): pool.validate_grant(grant, self.plan)


if __name__ == '__main__':
    unittest.main()
