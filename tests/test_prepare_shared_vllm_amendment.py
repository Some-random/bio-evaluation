import json
from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from prepare_shared_vllm_amendment import measured_limits, checked_context, excluded_capacity_evidence, CAPACITY_EXCLUSIONS
from shared_vllm_resume import MODEL, REVISION, ResumeError, file_sha


class CapacityEvidenceTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)

    def profile(self, length, cap, *, folder=None, mismatch=0, benchmark_name="length_benchmark"):
        folder = self.root / (folder or ("replica_" + str(length))) / benchmark_name
        folder.mkdir(parents=True)
        rows = [{"input_tokens": length, "concurrency": c, "state": "measured", "eligible": True,
                 "measured": {"failed_requests": 0, "fixed_workload_mismatch_requests": mismatch,
                              "successful_requests": c, "planned_requests": c, "actual_prompt_tokens": length * c,
                              "actual_completion_tokens": 4096 * c, "comparable_fixed_workload": True},
                 "monitoring": {"preemption_delta": 0}} for c in [1, 2, 4, 8, 16, 32] if c <= cap]
        for row in rows:
            metrics = {metric + '{engine="0"}': 0 for metric in ["vllm:prompt_tokens_total", "vllm:generation_tokens_total", "vllm:num_requests_running", "vllm:num_requests_waiting"]}
            row["measured"]["metrics_before"] = {"selected": dict(metrics)}
            metrics['vllm:prompt_tokens_total{engine="0"}'] = row["measured"]["actual_prompt_tokens"]
            metrics['vllm:generation_tokens_total{engine="0"}'] = row["measured"]["actual_completion_tokens"]
            row["measured"]["metrics_after"] = {"selected": metrics}
        (folder / "results.json").write_text(json.dumps({"plan": {"model": MODEL, "revision": REVISION, "output_tokens": 4096, "synthetic_only": True}, "rows": rows}))
        (folder / "measured_concurrency_by_input_length.json").write_text(json.dumps({"points": [{"tested_input_tokens": length, "tested_output_tokens": 4096, "best_tested_concurrency": cap}]}))
        (folder / "progress.json").write_text('{"state":"completed"}')
        return folder

    def test_missing_profiles_are_explicitly_not_ready(self):
        self.profile(1536, 32)
        limits, _, missing = measured_limits(self.root)
        self.assertEqual(limits[0]["max_prompt_tokens"], 1536)
        self.assertIn("input_tokens=45056", missing)

    def test_extra_measured_49152_profile_is_accepted_without_extrapolation(self):
        for length, cap in [(192, 32), (1536, 32), (7000, 16), (16384, 8), (45056, 4), (49152, 2)]:
            self.profile(length, cap)
        limits, evidence, missing = measured_limits(self.root)
        self.assertEqual(missing, [])
        self.assertEqual([(p["max_prompt_tokens"], p["max_inflight"]) for p in limits], [(192, 32), (1536, 32), (7000, 16), (16384, 8), (45056, 4), (49152, 2)])
        self.assertEqual(len(evidence), 18)

    def test_token_mismatch_cannot_support_an_admission_cap(self):
        self.profile(1536, 32, mismatch=1)
        with self.assertRaises(ResumeError):
            measured_limits(self.root)

    def test_summary_cannot_select_an_unmeasured_concurrency(self):
        folder = self.profile(1536, 8)
        path = folder / "measured_concurrency_by_input_length.json"
        value = json.loads(path.read_text())
        value["points"][0]["best_tested_concurrency"] = 32
        path.write_text(json.dumps(value))
        with self.assertRaises(ResumeError):
            measured_limits(self.root)

    def test_new_deepfri_context_preflight_is_discovered_by_task(self):
        path = self.root / ".local/shared_vllm_migration_2026-10-17/context_checks/P12/context_check.json"
        path.parent.mkdir(parents=True)
        path.write_text(json.dumps({"case_count": 1, "output_budget": 4096, "all_prompts_fit": True,
                                    "max_prompt_tokens": 500, "per_case": [{"case_id": "synthetic", "prompt_tokens": 500}]}))
        result = checked_context(self.root, self.root / "project", {"run_id": "synthetic-run", "approved_task_ids": ["P12"]}, 1, {})
        self.assertEqual(result["path"], str(path))

    def test_explicit_exclusions_preserve_and_pin_bad_attempts_but_use_clean_replacements(self):
        bad = [self.profile(45056, 32, folder="replica_3"),
               self.profile(49152, 32, folder="replica_3", benchmark_name="length_benchmark_49152")]
        failed = self.root / "replica_2/length_benchmark_192"
        failed.mkdir(parents=True)
        (failed / "progress.json").write_text('{"state":"failed","error":"synthetic idle failure"}')
        bad.append(failed)
        original_hashes = {str(p): file_sha(p) for directory in bad for p in directory.rglob("*") if p.is_file()}
        for length, cap in [(1536, 16), (7000, 16), (16384, 8)]:
            self.profile(length, cap)
        self.profile(192, 32, folder="replica_2", benchmark_name="length_benchmark_clean_192")
        self.profile(45056, 4, folder="replica_0", benchmark_name="length_benchmark_clean_45056")
        self.profile(49152, 2, folder="replica_3", benchmark_name="length_benchmark_clean_49152")
        limits, evidence, missing = measured_limits(self.root)
        self.assertEqual(missing, [])
        self.assertEqual(limits[-1]["max_inflight"], 2)
        self.assertFalse(any('/'.join(Path(e["path"]).relative_to(self.root).parts[:2]) in CAPACITY_EXCLUSIONS for e in evidence))
        exclusions = excluded_capacity_evidence(self.root)
        self.assertEqual({e["relative_directory"] for e in exclusions}, set(CAPACITY_EXCLUSIONS))
        self.assertTrue(all(e["files_sha256"] for e in exclusions))
        for path, expected in original_hashes.items():
            self.assertEqual(file_sha(path), expected)

    def test_results_file_does_not_make_in_progress_measurement_eligible(self):
        directory = self.profile(1536, 16)
        (directory / "progress.json").write_text('{"state":"measuring"}')
        limits, evidence, missing = measured_limits(self.root)
        self.assertEqual(limits, [])
        self.assertEqual(evidence, [])
        self.assertIn(str(directory), missing)

    def test_other_workload_token_counters_cannot_support_admission(self):
        directory = self.profile(1536, 16)
        path = directory / "results.json"
        result = json.loads(path.read_text())
        result["rows"][-1]["measured"]["metrics_after"]["selected"]['vllm:generation_tokens_total{engine="0"}'] += 100
        path.write_text(json.dumps(result))
        with self.assertRaisesRegex(ResumeError, "concurrent work"):
            measured_limits(self.root)

    def test_nonidle_boundary_cannot_support_admission(self):
        directory = self.profile(1536, 16)
        path = directory / "results.json"
        result = json.loads(path.read_text())
        result["rows"][-1]["measured"]["metrics_before"]["selected"]['vllm:num_requests_running{engine="0"}'] = 1
        path.write_text(json.dumps(result))
        with self.assertRaises(ResumeError):
            measured_limits(self.root)

    def test_live_sampler_rejects_more_requests_than_measured_batch(self):
        directory = self.profile(1536, 16)
        sample = directory / "sample.jsonl"
        sample.write_text('{"running":17,"waiting":0}\n')
        path = directory / "results.json"
        result = json.loads(path.read_text())
        result["rows"][-1]["monitoring"]["sample_file"] = str(sample)
        path.write_text(json.dumps(result))
        with self.assertRaises(ResumeError):
            measured_limits(self.root)


if __name__ == "__main__":
    unittest.main()
