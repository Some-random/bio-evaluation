"""Memory gating uses synthetic live metrics rather than evaluation outcomes."""

import importlib.util
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "benchmark_vllm_prompt_lengths.py"
SPEC = importlib.util.spec_from_file_location("benchmark_vllm_prompt_lengths", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class LengthBenchmarkTests(unittest.TestCase):
    def test_profile_lock_refuses_second_process_through_idle_gaps(self):
        with tempfile.TemporaryDirectory() as directory:
            code = ("import importlib.util,sys; "
                    "s=importlib.util.spec_from_file_location('bench',sys.argv[1]); "
                    "m=importlib.util.module_from_spec(s); s.loader.exec_module(m); "
                    "lock=m.exclusive_endpoint_lock('http://localhost:8050/v1',sys.argv[2]); "
                    "lock.__enter__(); print('owned')")
            with MODULE.exclusive_endpoint_lock("http://127.0.0.1:8050", directory):
                refused = subprocess.run([sys.executable, "-c", code, str(SCRIPT), directory], capture_output=True, text=True)
                self.assertNotEqual(refused.returncode, 0)
                self.assertIn("Another synthetic profile owns this endpoint", refused.stderr)
                # Independent replica ports remain available.
                with MODULE.exclusive_endpoint_lock("http://localhost:8051", directory):
                    pass
            accepted = subprocess.run([sys.executable, "-c", code, str(SCRIPT), directory], capture_output=True, text=True)
            self.assertEqual(accepted.returncode, 0, accepted.stderr)
            self.assertEqual(accepted.stdout.strip(), "owned")

    def test_long_workload_uses_bounded_tokenization_and_exact_distinct_prompts(self):
        class Tokenizer:
            def __init__(self):
                self.lengths = []

            def request(self, path, payload):
                self.lengths.append(len(payload["prompt"]))
                return {"tokens": [ord(character) for character in payload["prompt"]]}

        client = Tokenizer()
        first = MODULE.make_synthetic_workload(client, "synthetic", 3, 45056, 42)
        second = MODULE.make_synthetic_workload(Tokenizer(), "synthetic", 3, 45056, 42)
        self.assertEqual(first, second)
        self.assertTrue(all(len(row["prompt_token_ids"]) == 45056 for row in first["requests"]))
        self.assertNotEqual(first["requests"][0], first["requests"][1])
        self.assertLess(max(client.lengths), 12000)

    def test_gauges_and_counters_ignore_histograms_and_missing_values(self):
        metrics = MODULE.parse_metrics('''
vllm:kv_cache_usage_perc{engine="0"} 0.4
vllm:num_preemptions_total{engine="0"} 2
vllm:request_num_preemptions_count{engine="0"} 999
vllm:num_requests_running{engine="0"} 16
vllm:num_requests_waiting{engine="0"} 0
''')
        self.assertEqual(metrics, {"kv_fraction": .4, "preemptions": 2, "running": 16, "waiting": 0})
        self.assertIsNone(MODULE.parse_metrics("")["kv_fraction"])

    def test_projected_high_load_is_skipped_and_failed_pilot_cannot_admit(self):
        plan = {"concurrencies": [4, 8, 16, 32], "projection_safety_multiplier": 1.1, "maximum_measured_kv_fraction": .85}
        self.assertTrue(MODULE.next_projection(None, 4, plan)["admit"])
        previous = {"concurrency": 16, "sampled_peak_kv_fraction": .4, "eligible": True}
        candidate = MODULE.next_projection(previous, 32, plan)
        self.assertAlmostEqual(candidate["projected_peak_kv_fraction"], .88)
        self.assertFalse(candidate["admit"])
        previous["eligible"] = False
        self.assertFalse(MODULE.next_projection(previous, 16, plan)["admit"])
        previous.update(eligible=True, sampled_peak_kv_fraction=None)
        self.assertFalse(MODULE.next_projection(previous, 16, plan)["admit"])


if __name__ == "__main__":
    unittest.main()
