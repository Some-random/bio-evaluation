"""Check report selection, metric deltas and GPU identity isolation."""

import importlib.util
import json
from pathlib import Path
import tempfile
import unittest


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "summarize_vllm_concurrency.py"
SPEC = importlib.util.spec_from_file_location("summarize_vllm_concurrency", SCRIPT)
SUMMARY = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(SUMMARY)


def write(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data))


def measurement(concurrency, tps, count=32):
    return {"stage": f"repeat_01_concurrency_{concurrency:03d}", "concurrency": concurrency, "completed_requests": count, "successful_requests": count, "failed_requests": 0, "fixed_workload_mismatch_requests": 0, "comparable_fixed_workload": True, "output_tokens_per_second": tps, "requests_per_second": tps / 512, "latency_seconds": {"p50": 3, "p95": 4}, "finished_at": "2026-10-17T21:01:00-07:00", "elapsed_seconds": 60}


class SummaryTests(unittest.TestCase):
    def test_main_finding_compares_completed_primary_points_and_excludes_partial(self):
        rows = []
        for name, concurrency, throughput, valid, role in (("baseline", 4, 100, True, "primary"), ("best", 16, 385, True, "primary"), ("partial", 32, 999, False, "primary"), ("other_gpu", 4, 9999, True, "original_baseline")):
            rows.append({"id": name, "group": "long_decode_full_batch", "server_capacity": 32, "client_concurrency": concurrency, "output_tokens_per_second": throughput, "eligible_best_tested_candidate": valid, "source_role": role, "input_tokens_per_request": 192, "output_tokens_per_request": 4096})
        finding = SUMMARY.main_finding({"rows": rows, "findings": SUMMARY.calculate_findings(rows)})
        self.assertIn("**16 concurrent requests**", finding)
        self.assertIn("**3.85×**", finding)
        self.assertIn("192 synthetic input tokens", finding)
        self.assertIn("Production settings remain unchanged", finding)
        self.assertNotIn("999", finding)

    def test_imported_valid_baseline_keeps_failed_run_provenance_and_primary_recommendation(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            for name, capacity, throughput, state, uuid in (("baseline", 4, 200, "failed", "GPU-baseline"), ("primary", 32, 100, "benchmarking", "GPU-primary")):
                folder = root / name
                step = {"name": f"capacity{capacity}_quick", "server_capacity": capacity, "concurrencies": "4", "requests": 32, "input_tokens": 192, "output_tokens": 512}
                write(folder / "plan.json", {"steps": [step], "model": "synthetic-model", "max_model_len": 32768})
                write(folder / "environment.json", {"hostname": name + "-node"})
                write(folder / "status.json", {"stage": state})
                write(folder / f"server_capacity_{capacity}_gpu.json", [{"gpu_uuid": uuid}])
                write(folder / step["name"] / "results.json", {"stages": [measurement(4, throughput)]})
            report = SUMMARY.add_original_baseline(SUMMARY.collect_report(root / "primary"), root / "baseline")
            self.assertEqual(report["run_status"]["stage"], "benchmarking")
            self.assertEqual(len(report["rows"]), 2)
            self.assertEqual(report["rows"][0]["source_role"], "original_baseline")
            self.assertEqual(report["source_runs"][1]["run_status"]["stage"], "failed")
            self.assertTrue(report["baseline_comparison"]["different_physical_gpu"])
            self.assertEqual(report["findings"]["capacity32_vs_capacity4_at_client4_quick_ratio"], .5)
            self.assertTrue(report["findings"]["quick_fixed_total_work_best_tested"].startswith("primary/"))
            rendered = SUMMARY.markdown(report, Path("report"))
            self.assertIn("prior run ended **failed**", rendered)
            self.assertIn("does not isolate a server-capacity effect", rendered)
            self.assertIn("different physical GPUs", rendered)

    def test_sampling_uses_observed_config_before_plan_and_labels_sampled_mode(self):
        plan = {"generation": {"temperature": 1, "top_p": .95, "top_k": 20, "seed": 42}}
        planned = SUMMARY.sampling_metadata({}, plan)
        self.assertEqual(planned["settings"]["seed"], 42)
        self.assertIn("Sampled decoding", SUMMARY.sampling_description(planned))
        self.assertIn("match production", SUMMARY.sampling_limitation(planned))
        self.assertNotIn("greedy", SUMMARY.sampling_limitation(planned))
        observed = SUMMARY.sampling_metadata({"sampling": {"temperature": 0, "seed": 3, "max_tokens": 512}}, plan)
        self.assertEqual(observed["source"], "observed client config")
        self.assertEqual(observed["settings"], {"temperature": 0, "seed": 3})
        self.assertIn("Greedy decoding", SUMMARY.sampling_description(observed))

    def test_preemption_delta_detects_counter_reset_and_missing_metrics(self):
        with tempfile.TemporaryDirectory() as temporary:
            folder = Path(temporary)
            self.assertIsNone(SUMMARY.preemption_delta(folder)["delta"])
            (folder / "metrics_before.prom").write_text('vllm:num_preemptions_total{model_name="demo"} 12\n')
            (folder / "metrics_after.prom").write_text('vllm:num_preemptions_total{model_name="demo"} 15\n')
            self.assertEqual(SUMMARY.preemption_delta(folder)["delta"], 3)
            (folder / "metrics_after.prom").write_text('vllm:num_preemptions_total{model_name="demo"} 1\n')
            self.assertTrue(SUMMARY.preemption_delta(folder)["counter_reset_detected"])
            self.assertIsNone(SUMMARY.preemption_delta(folder)["delta"])

    def test_partial_fast_stage_does_not_win_and_other_gpus_do_not_enter_peaks(self):
        with tempfile.TemporaryDirectory() as temporary:
            folder = Path(temporary)
            steps = [
                {"name": "production_capacity4_quick", "server_capacity": 4, "concurrencies": "4", "requests": 32, "input_tokens": 192, "output_tokens": 512},
                {"name": "capacity32_quick_sweep", "server_capacity": 32, "concurrencies": "4,8", "requests": 32, "input_tokens": 192, "output_tokens": 512},
                {"name": "long_decode_full_batch_c8", "server_capacity": 32, "concurrencies": "8", "requests": 8, "input_tokens": 192, "output_tokens": 4096},
            ]
            write(folder / "plan.json", {"steps": steps, "model": "synthetic-model", "max_model_len": 32768})
            write(folder / "status.json", {"stage": "benchmarking", "updated_at": "2026-10-18T04:01:00+00:00"})
            for capacity in (4, 32):
                write(folder / f"server_capacity_{capacity}_gpu.json", [{"gpu_uuid": "GPU-own", "pid": 123}])
            (folder / "gpu_telemetry.csv").write_text(
                "2026/10/17 21:00:30.000, 0, GPU-own, 50, 30, 100, 80000, 120, 50\n"
                "2026/10/17 21:00:30.000, 1, GPU-other, 99, 99, 99999, 100000, 999, 90\n"
            )
            write(folder / steps[0]["name"] / "results.json", {"stages": [measurement(4, 100)]})
            write(folder / steps[0]["name"] / "config.json", {"sampling": {"temperature": 0, "seed": 20261017}})
            write(folder / steps[1]["name"] / "results.json", {"stages": [measurement(4, 102), measurement(8, 200)]})
            partial = measurement(8, 1000, 4)
            write(folder / steps[2]["name"] / "progress.json", {"state": "running", "stage": partial["stage"], "completed_requests": 4, "stage_partial_summary": partial})
            report = SUMMARY.collect_report(folder)
            self.assertEqual(len(report["rows"]), 4)
            self.assertEqual(report["rows"][-1]["status"], "partial")
            self.assertFalse(report["rows"][-1]["eligible_best_tested_candidate"])
            self.assertIsNone(report["findings"]["long_decode_full_batch_best_tested"])
            self.assertIn("concurrency_008", report["findings"]["quick_fixed_total_work_best_tested"])
            self.assertAlmostEqual(report["findings"]["capacity32_vs_capacity4_at_client4_quick_ratio"], 1.02)
            self.assertEqual(report["gpu_telemetry_all_run"]["sampled_max_memory_used_mib"], 100)
            self.assertEqual(report["gpu_telemetry_all_run"]["sampled_max_gpu_utilization_percent"], 50)
            self.assertEqual(report["rows"][0]["gpu_telemetry"]["samples"], 1)
            self.assertEqual(report["run_status"]["updated_at"], "2026-10-17T21:01:00-07:00")
            rendered = SUMMARY.markdown(report, Path("report"))
            self.assertIn("fixed total work", rendered)
            self.assertIn("one full concurrent batch", rendered)
            self.assertIn("partial", rendered)
            self.assertIn("sampled decoding", rendered)
            self.assertNotIn("GPU-other", rendered)
            write(folder / steps[2]["name"] / "progress.json", {"state": "running", "stage": partial["stage"], "completed_requests": 0, "stage_partial_summary": partial})
            stale = SUMMARY.collect_report(folder)["rows"][-1]
            self.assertEqual(stale["status"], "pending")
            self.assertEqual(stale["completed_requests"], 0)
            self.assertIsNone(stale["output_tokens_per_second"])

    def test_node_inventory_is_not_an_identity_fallback(self):
        with tempfile.TemporaryDirectory() as temporary:
            folder = Path(temporary)
            write(folder / "environment.json", {"gpu_inventory": "GPU-unrelated"})
            self.assertEqual(SUMMARY.gpu_uuids(folder, 4), [])
            write(folder / "server_capacity_4_gpu.json", [{"gpu_uuid": "GPU-one"}, {"gpu_uuid": "GPU-two"}])
            self.assertEqual(SUMMARY.gpu_uuids(folder, 4), [])


if __name__ == "__main__":
    unittest.main()
