import csv
import importlib.util
import io
import json
from pathlib import Path
import tempfile
import unittest


spec = importlib.util.spec_from_file_location(
    "summarize_local_suite", Path(__file__).resolve().parents[1] / "scripts/summarize_local_suite.py"
)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)


class LocalSuiteReportingTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.write(mod.CATALOG, {
            "counts": {"biological_evaluation_settings": 3},
            "tasks": [
                {"id": "B01", "task": "Synthetic literature QA", "family": "QA", "model_input": "Text", "metrics": "Accuracy; precision; coverage"},
                {"id": "P07", "task": "Synthetic scalar task", "family": "Protein prediction", "model_input": "Sequence", "metrics": "Spearman correlation"},
                {"id": "P18", "task": "Synthetic held task", "family": "Protein prediction", "model_input": "Sequence", "metrics": "Ranking"},
                {"id": "G01", "task": "Excluded control", "family": "General LLM controls"},
            ],
        })
        p = self.root / "reports/per_task_readiness.csv"
        p.parent.mkdir(parents=True)
        p.write_text("id,task,readiness,prepared_case_count,notes\nB01,QA,prepared_case_review_pending,5,review pending\nP07,Scalar,native_local_execution_not_prepared,0,not prepared\nP18,Held,policy_hold_no_local_dispatch,0,flagged requests remain held\n")
        self.write("configs/local_benchmark_queue.json", {"jobs": []})
        self.first_run = "original_litqa2"
        entries = [
            {"task_id": "B01", "protocol_variant": "NATIVE", "score_status": "not_run"},
            {"task_id": "B01", "protocol_variant": "NATIVE_PUBLIC_COT_LOCAL_REVIEWED", "run_id": self.first_run,
             "model": "SyntheticModel", "model_revision": "pinned-original", "score_status": "completed",
             "actual_supplied_information": {"status": "dispatched", "run_id": self.first_run,
                                             "observed_model_input_fields": ["question", "shuffled_choices"]}},
        ]
        p = self.root / "results/interpretation_notes.jsonl"
        p.parent.mkdir(parents=True)
        p.write_text("\n".join(json.dumps(e) for e in entries) + "\n")
        self.write(f"results/runs/{self.first_run}/scores.json", {
            "run_id": self.first_run, "model": "SyntheticModel", "model_revision": "pinned-original",
            "protocol_variant": "NATIVE_PUBLIC_COT_LOCAL_REVIEWED", "planned": 5, "completed": 5,
            "statuses": {"completed": 5}, "case_scope": "reviewed_public_subset", "held_before_inference": 1,
            "metrics": {"accuracy": 0.4, "precision": 0.5, "coverage": 0.8, "n_total": 5},
        })

    def write(self, name, data):
        p = self.root / name
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(json.dumps(data))

    def report(self):
        return mod.build_report(self.root, generated_at="synthetic-fixture")

    def test_original_b01_join_variants_and_files_are_preserved(self):
        protected = [self.root / "results/interpretation_notes.jsonl", self.root / f"results/runs/{self.first_run}/scores.json"]
        before = [p.read_bytes() for p in protected]
        report = self.report()
        mod.write_report(self.root, report)
        b01 = next(t for t in report["tasks"] if t["task_id"] == "B01")
        self.assertEqual(b01["state"], "completed_native_variant")
        self.assertEqual(b01["run_ids"], [self.first_run])
        self.assertEqual([v["protocol_variant"] for v in b01["interpretation_variants"]], ["NATIVE", "NATIVE_PUBLIC_COT_LOCAL_REVIEWED"])
        self.assertEqual(report["runs"][0]["model_revision"], "pinned-original")
        self.assertEqual(report["runs"][0]["input_modalities"], ["text"])
        self.assertEqual(report["runs"][0]["held_before_inference"], 1)
        self.assertEqual([p.read_bytes() for p in protected], before)
        self.assertEqual(report["coverage"]["catalog_settings"], 3)
        self.assertEqual(report["coverage"]["settings_with_completed_native_variant"], 1)
        self.assertEqual(next(t for t in report["tasks"] if t["task_id"] == "P18")["state"], "prohibited_or_held")
        self.assertEqual(report, self.report())

    def test_partial_scored_and_generation_complete_are_not_completed_scores(self):
        self.write("results/runs/partial/scores.json", {
            "task_id": "P07", "run_id": "partial", "protocol_variant": "NATIVE", "planned": 10,
            "completed": 4, "statuses": {"completed": 4}, "metrics": {"spearman": 1.0},
        })
        report = self.report()
        run = next(r for r in report["runs"] if r["run_id"] == "partial")
        self.assertEqual(run["state"], "partial_scored")
        self.assertEqual(report["coverage"]["settings_with_completed_native_variant"], 1)
        self.write("configs/local_benchmark_queue.json", {"jobs": [{"config": "configs/pending.json"}]})
        self.write("configs/pending.json", {"run_id": "pending", "approved_task_ids": ["P07"], "variant": "NATIVE"})
        self.write("results/runs/pending/progress.json", {"run": "pending", "planned": 3, "finished": 3, "stage": "generation_complete"})
        pending = next(r for r in self.report()["runs"] if r["run_id"] == "pending")
        self.assertEqual(pending["state"], "generation_complete_unscored")

    def test_final_scores_override_stale_progress_and_keep_exact_metric_names(self):
        self.write("results/runs/scalar/scores.json", {
            "task_id": "P07", "run_id": "scalar", "protocol_variant": "ADAPTED_SEQUENCE_TEXT_NUMERIC",
            "model": "SyntheticModel", "model_revision": "scalar-pinned", "planned": 10, "completed": 9,
            "statuses": {"completed": 9, "transport_error": 1}, "invalid_outputs": 0,
            "metrics": {"spearman": None, "spearman_parsed_only": 0.25, "by_split": {"test_MAE": 3.5}},
        })
        self.write("results/runs/scalar/progress.json", {"run": "scalar", "planned": 10, "finished": 2, "stage": "running"})
        report = self.report()
        run = next(r for r in report["runs"] if r["run_id"] == "scalar")
        self.assertEqual(run["state"], "completed_scored_with_failures")
        self.assertEqual(run["finished"], 10)
        self.assertEqual(run["failure_count"], 1)
        self.assertEqual(report["coverage"]["settings_with_completed_native_variant"], 1)
        self.assertEqual(report["coverage"]["settings_with_completed_adapted_variant"], 1)
        rows = [r for r in csv.DictReader(io.StringIO(mod.render_metrics_csv(report))) if r["run_id"] == "scalar"]
        self.assertEqual({r["metric_name"] for r in rows}, {"spearman", "spearman_parsed_only", "by_split.test_MAE"})
        self.assertEqual(next(r for r in rows if r["metric_name"] == "spearman")["metric_value_json"], "null")
        self.assertEqual(json.loads(next(r for r in rows if r["metric_name"] == "by_split.test_MAE")["metric_path_json"]), ["by_split", "test_MAE"])

    def test_queue_metadata_and_comparator_training_caveats_remain_separate(self):
        self.write("configs/local_benchmark_queue.json", {"jobs": [{"config": "configs/vision.json"}]})
        self.write("configs/vision.json", {"run_id": "vision", "approved_task_ids": ["P07"], "variant": "NATIVE",
                                          "model_facing_fields": ["question", "images_sha256"],
                                          "input_file": "must-not-be-opened.json", "prompt": "DO NOT COPY THIS FIELD"})
        self.write(mod.COMPARISONS, {"tasks": [{"task_id": "B01", "comparison_status": "contextual_only",
            "published_baselines": [{"model": "SyntheticTrainedModel", "metrics": {"accuracy_percent": 40.0},
                                     "protocol": "supervised training; different paper split", "test_case_count": 9,
                                     "run_count": 3, "reported_std": {"accuracy_percent": 1.0},
                                     "uncertainty_note": "synthetic dispersion caveat"}],
            "comparability_requirements": ["Synthetic reviewed subset differs from full set."],
            "local_model_result_in_this_report": {"accuracy": 99}}]})
        report = self.report()
        run = next(r for r in report["runs"] if r["run_id"] == "vision")
        self.assertEqual(run["state"], "queued")
        self.assertIsNone(run["input_modalities"])
        self.assertEqual(run["configured_input_modalities"], ["text", "image"])
        self.assertNotIn("DO NOT COPY THIS FIELD", json.dumps(report))
        markdown = mod.render_markdown(report)
        self.assertIn("supervised training; different paper split", markdown)
        self.assertIn("synthetic dispersion caveat", markdown)
        self.assertIn("Synthetic reviewed subset differs from full set.", markdown)
        self.assertNotIn("local_model_result_in_this_report", json.dumps(report))

    def test_multiple_queues_and_qualified_holds(self):
        self.write("configs/local_benchmark_queue_gpu6.json", {"jobs": [{"config": "configs/gpu6.json"}]})
        self.write("configs/gpu6.json", {"run_id": "gpu6", "approved_task_ids": ["P07"], "variant": "NATIVE"})
        self.write(".local/local_benchmark_queue_gpu6/progress.json", {"active_run": "gpu6", "stage": "running", "gpu_ids": [6]})
        self.write("results/runs/gpu6/progress.json", {"run_id": "gpu6", "stage": "running", "planned": 10, "finished": 2})
        self.write("reports/catalog_execution_review_2026-10-15.json", {"tasks": [{"id": "P18", "status": "native_test_available_context_and_scorer_pending", "blockers": ["Exact assay context remains unresolved."]}]})
        self.write("reports/labbench_protocol_review_hold.json", {"task_id": "P18", "stage": "input_review_blocked_no_local_dispatch",
                   "reason": "Synthetic review hold", "review_complete": False, "remaining_cases": "Unreviewed; not all classified as prohibited."})
        report = self.report()
        self.assertEqual(len(report["queues"]["configurations"]), 2)
        run = next(r for r in report["runs"] if r["run_id"] == "gpu6")
        self.assertEqual(run["source_queues"], ["configs/local_benchmark_queue_gpu6.json"])
        self.assertEqual(next(t for t in report["tasks"] if t["task_id"] == "P07")["state"], "running")
        held = next(t for t in report["tasks"] if t["task_id"] == "P18")
        self.assertEqual(held["state"], "prohibited_or_held")
        self.assertFalse(held["qualified_input_review_hold"]["review_complete"])
        self.assertIn("not all classified", held["native_completion_blockers"][0]["qualification"])

    def test_finished_shards_require_validated_full_test_union(self):
        for index in (0, 1):
            self.write(f"results/runs/shard{index}/scores.json", {
                "run_id": f"shard{index}", "task_id": "P07", "protocol_variant": "NATIVE",
                "planned": 5, "completed": 5, "metrics": {"spearman": 0.5},
                "shard_index": index, "shard_count": 2, "case_scope": "shard",
            })
        report = self.report()
        p07 = next(t for t in report["tasks"] if t["task_id"] == "P07")
        self.assertFalse(p07["native_variant_completed"])
        self.assertEqual(p07["state"], "partial_task_coverage")
        self.assertEqual(len(p07["completed_shard_run_ids"]), 2)
        aggregate = {"run_id": "full_union", "task_id": "P07", "protocol_variant": "NATIVE",
                     "planned": 10, "completed": 10, "metrics": {"spearman": 0.5},
                     "shard_count": 2, "aggregated_from_shards": True}
        self.write("results/runs/full_union/scores.json", aggregate)
        self.assertFalse(next(t for t in self.report()["tasks"] if t["task_id"] == "P07")["native_variant_completed"])

        aggregate["full_test_id_union_validation"] = {"complete": True, "union_matches_full_test_ids": True,
            "expected_test_case_count": 10, "unique_observed_case_count": 10, "missing_case_count": 0, "extra_case_count": 0}
        self.write("results/runs/full_union/scores.json", aggregate)
        p07 = next(t for t in self.report()["tasks"] if t["task_id"] == "P07")
        self.assertTrue(p07["native_variant_completed"])
        self.assertEqual(p07["state"], "completed_native_variant")
        aggregate["full_test_id_union_validation"]["missing_case_count"] = 1
        self.write("results/runs/full_union/scores.json", aggregate)
        self.assertFalse(next(t for t in self.report()["tasks"] if t["task_id"] == "P07")["native_variant_completed"])

    def test_subset_assay_hold_is_not_blanket_task_prohibition(self):
        self.write("reports/catalog_execution_review_2026-10-15.json", {"tasks": [
            {"id": "P07", "status": "native_data_and_assay_scope_pending",
             "blockers": ["Selected flagged assays remain held; other assays require scope review."]}
        ]})
        task = next(t for t in self.report()["tasks"] if t["task_id"] == "P07")
        self.assertEqual(task["state"], "assay_scope_review_pending")
        self.assertIn("Selected flagged assays", task["native_completion_blockers"][0]["evidence"])

    def test_declared_qwen_adaptation_names_preserve_native_metrics_and_diagnostics(self):
        self.write("results/runs/qwen_text/scores.json", {
            "task_id": "P07", "run_id": "qwen_text", "protocol_variant": "QWEN_FULL_SEQUENCE_TEXT_BIOT5_TEST",
            "planned": 2, "completed": 2, "metrics": {"accuracy": 0.5, "STRICT_FINAL_LABEL": {"accuracy": 0.0}},
            "primary_metric_status": "source_rule_on_protocol_qualified_saved_continuation", "native_decode_byte_equivalence_claimed": False,
        })
        report = self.report()
        run = next(r for r in report["runs"] if r["run_id"] == "qwen_text")
        self.assertEqual(run["protocol_kind"], "adapted")
        self.assertEqual(report["coverage"]["settings_with_completed_adapted_variant"], 1)
        self.assertEqual(run["primary_metric_status"], "source_rule_on_protocol_qualified_saved_continuation")
        rows = [r for r in csv.DictReader(io.StringIO(mod.render_metrics_csv(report))) if r["run_id"] == "qwen_text"]
        self.assertEqual({r["metric_name"] for r in rows}, {"accuracy", "STRICT_FINAL_LABEL.accuracy"})
        self.assertEqual(mod._protocol_kind("QWEN_DTI_FIRST_TOKEN_CONDITIONAL_YES_NO_LIKELIHOOD"), "adapted")
        self.assertEqual(mod._protocol_kind("QWEN_ZERO_SHOT_PROTEIN_DESCRIPTION"), "adapted")
        self.assertEqual(mod._protocol_kind("NATIVE_TEST_QUESTION_IMAGE_LOCAL_ZERO_SHOT"), "native")


if __name__ == "__main__":
    unittest.main()
