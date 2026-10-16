import csv
import hashlib
import importlib.util
import io
import json
from pathlib import Path
import tempfile
import unittest
from unittest import mock


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
        self.assertEqual(report["coverage"]["settings_with_completed_adapted_variant"], 0)
        self.assertFalse(run["full_planned_primary_metrics_valid"])
        self.assertEqual(next(t for t in report["tasks"] if t["task_id"] == "P07")["state"], "scored_primary_metrics_undefined")
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

    def test_p43_completed_dataset_requires_exact_three_test_union(self):
        catalog = json.loads((self.root / mod.CATALOG).read_text())
        catalog["tasks"].append({"id": "P43", "task": "Synthetic three-dataset ranking", "family": "Protein prediction", "metrics": "AUROC; AP"})
        self.write(mod.CATALOG, catalog)
        component = {"task_id": "P43", "run_id": "biosnap", "dataset": "BioSNAP",
                     "protocol_variant": "QWEN_DTI_FIRST_TOKEN_CONDITIONAL_TEST",
                     "planned": 5493, "completed": 5493,
                     "metrics": {"AUROC": 0.5, "AP": 0.5}}
        self.write("results/runs/biosnap/scores.json", component)
        report = self.report()
        task = next(t for t in report["tasks"] if t["task_id"] == "P43")
        run = next(r for r in report["runs"] if r["run_id"] == "biosnap")
        self.assertEqual(run["state"], "completed_scored")
        self.assertFalse(run["task_coverage_complete"])
        self.assertEqual(task["state"], "partial_task_coverage")
        self.assertFalse(task["adapted_variant_completed"])
        aggregate = {**component, "run_id": "all_tests", "dataset": None,
                     "planned": 16533, "completed": 16533,
                     "case_scope": "native_source_test_union_separate_dataset_metrics",
                     "metrics": {"BioSNAP": {"AUROC": 0.5, "AP": 0.5}, "BindingDB": {"AUROC": 0.5, "AP": 0.5}, "Human": {"AUROC": 0.5, "AP": 0.5}},
                     "full_test_id_union_validation": {"complete": True, "union_matches_full_test_ids": True,
                         "expected_test_case_count": 16533, "unique_observed_case_count": 16533,
                         "missing_case_count": 0, "extra_case_count": 0}}
        self.write("results/runs/all_tests/scores.json", aggregate)
        self.assertTrue(next(t for t in self.report()["tasks"] if t["task_id"] == "P43")["adapted_variant_completed"])
        self.assertEqual(next(t for t in self.report()["tasks"] if t["task_id"] == "P43")["state"], "completed_adapted_variant_native_incomplete")
        aggregate["case_scope"] = "complete_three_native_tests_separate_metrics"
        self.write("results/runs/all_tests/scores.json", aggregate)
        self.assertTrue(next(t for t in self.report()["tasks"] if t["task_id"] == "P43")["adapted_variant_completed"])
        aggregate["full_test_id_union_validation"]["expected_test_case_count"] = 5493
        aggregate["full_test_id_union_validation"]["unique_observed_case_count"] = 5493
        self.write("results/runs/all_tests/scores.json", aggregate)
        self.assertFalse(next(t for t in self.report()["tasks"] if t["task_id"] == "P43")["adapted_variant_completed"])

    def test_offline_reference_diagnostics_do_not_complete_undefined_primary_scores(self):
        self.write("results/runs/undefined/scores.json", {"task_id": "P07", "run_id": "undefined",
            "protocol_variant": "QWEN_ZERO_SHOT_SYNTHETIC", "planned": 2, "completed": 2,
            "full_planned_primary_metrics_valid": False, "invalid_outputs": 1,
            "metrics": {"auprc@micro": None, "f1_max": None, "OFFLINE_ALL_ZERO_REFERENCE": {"auprc@micro": 0.5}}})
        report = self.report()
        task = next(t for t in report["tasks"] if t["task_id"] == "P07")
        self.assertFalse(task["adapted_variant_completed"])
        self.assertEqual(task["state"], "scored_primary_metrics_undefined")
        rows = list(csv.DictReader(io.StringIO(mod.render_metrics_csv(report))))
        self.assertIn("OFFLINE_ALL_ZERO_REFERENCE.auprc@micro", {row["metric_name"] for row in rows})

    def test_legacy_p06_null_full_spearman_preserves_completed_execution_only(self):
        catalog = json.loads((self.root / mod.CATALOG).read_text())
        catalog["tasks"].append({"id": "P06", "task": "Synthetic legacy regression", "family": "Protein prediction", "metrics": "Spearman"})
        self.write(mod.CATALOG, catalog)
        name = "results/runs/legacy_p06/scores.json"
        self.write(name, {"task_id": "P06", "run_id": "legacy_p06", "protocol_variant": "QWEN_ZERO_SHOT_FULL_SEQUENCE_FLIP_HUMAN_CELL",
            "planned": 1366, "completed": 1366, "parsed": 1354, "invalid_outputs": 12,
            "statuses": {"completed": 1366}, "metrics": {"spearman": None, "spearman_parsed_only": 0.025374030047975442,
                "planned": 1366, "parsed": 1354, "missing": 0, "invalid": 12,
                "undefined_constant_or_insufficient": False, "all_case_rule": "Full Spearman requires every planned output."}})
        original = (self.root / name).read_bytes()
        report = self.report()
        run = next(row for row in report["runs"] if row["run_id"] == "legacy_p06")
        task = next(row for row in report["tasks"] if row["task_id"] == "P06")
        self.assertEqual(run["state"], "completed_scored_with_failures")
        self.assertEqual(run["completed"], 1366)
        self.assertEqual(run["parsed"], 1354)
        self.assertEqual(run["invalid_outputs"], 12)
        self.assertIsNone(run["reported_full_planned_primary_metrics_valid"])
        self.assertFalse(run["full_planned_primary_metrics_valid"])
        self.assertIn("Legacy full-test Spearman", run["primary_metric_validity_basis"])
        self.assertFalse(task["adapted_variant_completed"])
        self.assertEqual(task["state"], "scored_primary_metrics_undefined")
        self.assertIsNone(run["metrics"]["spearman"])
        self.assertEqual(run["metrics"]["spearman_parsed_only"], 0.025374030047975442)
        self.assertIn("does not count as valid benchmark completion", mod.render_markdown(report))
        self.assertEqual((self.root / name).read_bytes(), original)

    def test_qualified_native_metric_subset_cannot_complete_full_native_protocol(self):
        self.write("results/runs/qualified/scores.json", {"task_id": "P07", "run_id": "qualified", "protocol_variant": "NATIVE",
            "planned": 100, "completed": 100, "full_planned_primary_metrics_valid": True,
            "full_native_metric_set_complete": False, "metrics": {"success_fraction": 0.25, "uniqueness": 1.0},
            "native_novelty": None})
        report = self.report()
        run = next(row for row in report["runs"] if row["run_id"] == "qualified")
        task = next(row for row in report["tasks"] if row["task_id"] == "P07")
        self.assertEqual(run["state"], "completed_scored")
        self.assertTrue(run["full_planned_primary_metrics_valid"])
        self.assertFalse(task["native_variant_completed"])
        self.assertEqual(task["state"], "scored_native_metric_set_incomplete")
        self.assertIn("native_metric_set_incomplete", {row["kind"] for row in task["native_completion_blockers"]})

    def test_legacy_all_primary_null_ignores_finite_counts_and_diagnostic_namespaces(self):
        score = {"task_id": "P07", "run_id": "legacy_null", "protocol_variant": "QWEN_ZERO_SHOT_SYNTHETIC", "planned": 2, "completed": 2,
            "metrics": {"accuracy": None, "correct": 2, "planned": 2, "n_total": 2, "eligible": 2,
                "all_case_rule": "No invented primary metric.", "undefined_constant_or_insufficient": False,
                "OFFLINE_ALL_ZERO_REFERENCE": {"accuracy": 0.5}, "STRICT_FINAL_LABEL": {"accuracy": 0.75},
                "PARSED_ONLY_DIAGNOSTIC": {"accuracy": 1.0}}}
        self.write("results/runs/legacy_null/scores.json", score)
        report = self.report()
        run = next(row for row in report["runs"] if row["run_id"] == "legacy_null")
        self.assertEqual(run["state"], "completed_scored")
        self.assertFalse(run["full_planned_primary_metrics_valid"])
        self.assertFalse(next(row for row in report["tasks"] if row["task_id"] == "P07")["adapted_variant_completed"])
        score["metrics"]["accuracy"] = 0.0
        self.write("results/runs/legacy_null/scores.json", score)
        report = self.report()
        self.assertTrue(next(row for row in report["runs"] if row["run_id"] == "legacy_null")["full_planned_primary_metrics_valid"])
        self.assertTrue(next(row for row in report["tasks"] if row["task_id"] == "P07")["adapted_variant_completed"])

    def test_p29_requires_both_exact_source_split_unions_same_model_protocol(self):
        catalog = json.loads((self.root / mod.CATALOG).read_text())
        catalog["tasks"].append({"id": "P29", "task": "Synthetic two-split GO", "family": "Protein", "metrics": "GO set F1"})
        self.write(mod.CATALOG, catalog)
        def split_score(split, count):
            return {"task_id": "P29", "run_id": "p29_" + split, "native_split": split,
                "model": "fixed-model", "model_revision": "fixed-revision", "protocol_variant": "QWEN_ZERO_SHOT_P29",
                "planned": count, "completed": count, "metrics": {"native_mean_f1": 0.5},
                "shard_count": 7 if split == "id" else 8, "aggregated_from_shards": True,
                "full_test_id_union_validation": {"complete": True, "union_matches_full_test_ids": True,
                    "expected_test_case_count": count, "unique_observed_case_count": count,
                    "missing_case_count": 0, "extra_case_count": 0, "duplicate_case_count": 0}}
        self.write("results/runs/p29_id/scores.json", split_score("id", 6989))
        report = self.report()
        self.assertFalse(next(row for row in report["tasks"] if row["task_id"] == "P29")["adapted_variant_completed"])
        self.assertTrue(next(row for row in report["runs"] if row["run_id"] == "p29_id")["native_split_coverage_complete"])
        self.write("results/runs/p29_ood/scores.json", split_score("ood", 7800))
        self.assertFalse(next(row for row in self.report()["tasks"] if row["task_id"] == "P29")["adapted_variant_completed"])
        ood = split_score("ood", 7883)
        self.write("results/runs/p29_ood/scores.json", ood)
        report = self.report()
        self.assertTrue(next(row for row in report["tasks"] if row["task_id"] == "P29")["adapted_variant_completed"])
        for run in [row for row in report["runs"] if row["task_ids"] == ["P29"]]:
            self.assertEqual(run["full_setting_split_coverage_validation"]["full_setting_case_count"], 14872)
            self.assertEqual(run["metrics"], {"native_mean_f1": 0.5})
        ood["model_revision"] = "different-revision"
        self.write("results/runs/p29_ood/scores.json", ood)
        self.assertFalse(next(row for row in self.report()["tasks"] if row["task_id"] == "P29")["adapted_variant_completed"])

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

    def test_v04_zero_strict_match_keeps_format_qualification_and_score_unchanged(self):
        catalog = json.loads((self.root / mod.CATALOG).read_text())
        catalog["tasks"].append({"id": "V04", "task": "Synthetic image QA", "family": "Vision", "metrics": "Strict accuracy"})
        self.write(mod.CATALOG, catalog)
        path = "results/runs/v04/scores.json"
        self.write(path, {"task_id": "V04", "run_id": "v04", "protocol_variant": "NATIVE_TEST_QUESTION_IMAGE_LOCAL_ZERO_SHOT",
                          "planned": 500, "completed": 500, "metrics": {"strict_accuracy": 0.0}})
        original = (self.root / path).read_bytes()
        qualification = {"task_id": "V04", "run_id": "v04", "score_sha256": hashlib.sha256(original).hexdigest(),
                         "native_qualified_strict_accuracy": 0.0, "raw_score_preserved": True,
                         "prediction_only_format_audit": {"count": 500, "multiline": 500, "reference_answers_read_for_format_audit": False}}
        self.write("reports/v04_output_format_qualification.json", qualification)
        report = self.report()
        task = next(t for t in report["tasks"] if t["task_id"] == "V04")
        self.assertTrue(task["native_variant_completed"])
        caveat = task["result_qualifications"][0]
        self.assertTrue(caveat["score_sha256_matches"])
        self.assertIn("does not establish 500 incorrect", caveat["display_caveat"])
        self.assertIn("Result qualification", mod.render_markdown(report))
        self.assertIn("whole-final strict exact", mod.render_metrics_csv(report))
        self.assertEqual((self.root / path).read_bytes(), original)
        qualification["score_sha256"] = "different"
        self.write("reports/v04_output_format_qualification.json", qualification)
        self.assertTrue(any("score hash" in row for row in self.report()["warnings"]))

    def test_interrupted_mixed_source_review_is_unreviewed_held_without_zero_scores(self):
        catalog = json.loads((self.root / mod.CATALOG).read_text())
        for task in ["P30", "P31", "P32"]:
            catalog["tasks"].append({"id": task, "task": "Synthetic unreviewed scope", "family": "Protein prediction", "metrics": "Native metric pending"})
        self.write(mod.CATALOG, catalog)
        self.write("reports/mutadescribe_source_review_hold.json", {"task_ids": ["P30", "P31", "P32"],
            "stage": "source_review_interrupted_by_biological_safety_check", "exact_trigger_case_unknown": True,
            "inference_dispatched": False, "actual_model_generations": 0, "scope_status": "not_fully_reviewed_not_authorized",
            "reason": "Unreviewed scope held; this does not classify all released descriptive cases as prohibited."})
        report = self.report()
        for task in [row for row in report["tasks"] if row["task_id"] in {"P30", "P31", "P32"}]:
            self.assertEqual(task["state"], "unreviewed_source_scope_held")
            self.assertTrue(task["qualified_source_review_hold"]["exact_trigger_case_unknown"])
            self.assertFalse(task["native_variant_completed"])
            self.assertEqual(task["run_ids"], [])
            self.assertIn("does not classify every", task["qualified_source_review_hold"]["classification_qualification"])
        rows = [row for row in csv.DictReader(io.StringIO(mod.render_metrics_csv(report))) if row["task_id"] in {"P30", "P31", "P32"}]
        self.assertTrue(all(row["metric_value_json"] == "" for row in rows))

    def test_terminal_queue_failure_before_manifest_is_not_queued_or_complete(self):
        config = "configs/failed.json"
        self.write(config, {"run_id": "failed_before_manifest", "approved_task_ids": ["P07"], "variant": "NATIVE",
                            "input_file": "must-not-be-opened.jsonl"})
        # The job may already have been removed from the current queue. Its
        # exact config/run terminal history must still preserve the failure.
        self.write(".local/local_benchmark_queue_gpu6/progress.json", {"finished": {config: {"run_id": "failed_before_manifest", "exit_code": 7}}})
        report = self.report()
        run = next(row for row in report["runs"] if row["run_id"] == "failed_before_manifest")
        self.assertEqual(run["state"], "failed_or_stopped")
        self.assertEqual(run["terminal_queue_history"][0]["exit_code"], 7)
        self.assertIsNone(run["planned"])
        self.assertEqual(next(row for row in report["tasks"] if row["task_id"] == "P07")["state"], "failed_or_stopped")
        self.assertIn("nonzero exit code", mod.render_markdown(report))
        self.write(".local/local_benchmark_queue_gpu6/progress.json", {"finished": {config: {"run_id": "different_run", "exit_code": 7}}})
        self.write("configs/local_benchmark_queue_gpu6.json", {"jobs": [{"config": config}]})
        report = self.report()
        self.assertEqual(next(row for row in report["runs"] if row["run_id"] == "failed_before_manifest")["state"], "queued")
        self.assertTrue(any("history run/config mismatch" in warning for warning in report["warnings"]))

    def test_vision_compact_qualification_is_hash_matched_and_does_not_open_case_proofs(self):
        catalog = json.loads((self.root / mod.CATALOG).read_text())
        catalog["tasks"].append({"id": "B04", "task": "Synthetic figure QA", "family": "QA", "metrics": "Accuracy"})
        self.write(mod.CATALOG, catalog)
        name = "results/runs/figqa/scores.json"
        self.write(name, {"task_id": "B04", "run_id": "figqa", "protocol_variant": "NATIVE_PUBLIC_COT",
                          "planned": 181, "completed": 181, "metrics": {"accuracy": 0.5}})
        original = (self.root / name).read_bytes()
        compact = {"source_audit": {"path": "reports/synthetic_case_proofs.json", "sha256": "declared-source-hash"},
            "source_encoding_diagnostic": {"path": "reports/synthetic_pixel_proofs.json", "sha256": "declared-encoding-hash"},
            "audited_runs": [{"task_id": "B04", "run_id": "figqa", "cases": 181,
                "score_sha256": hashlib.sha256(original).hexdigest(), "source_choices_and_target_mapping_verified": True,
                "actual_request_provenance_verified": True, "no_extra_reference_fields_detected": True, "publisher_images_verified": True}],
            "B04_native_wrapper_encoding": {"cases": 181, "encoded_bytes_changed": 181, "decoded_pixels_changed": 181,
                "diagnostic_pillow_version": "9.0.1", "accuracy_effect": "unassessed"}}
        self.write(mod.VISION_INTEGRITY, compact)
        forbidden = {self.root / compact["source_audit"]["path"], self.root / compact["source_encoding_diagnostic"]["path"]}
        original_bytes, original_text = Path.read_bytes, Path.read_text
        def guard_bytes(path, *args, **kwargs):
            self.assertNotIn(path, forbidden)
            return original_bytes(path, *args, **kwargs)
        def guard_text(path, *args, **kwargs):
            self.assertNotIn(path, forbidden)
            return original_text(path, *args, **kwargs)
        with mock.patch.object(Path, "read_bytes", guard_bytes), mock.patch.object(Path, "read_text", guard_text):
            report = self.report()
        task = next(row for row in report["tasks"] if row["task_id"] == "B04")
        qualification = task["result_qualifications"][0]
        self.assertTrue(qualification["score_sha256_matches"])
        self.assertTrue(qualification["source_checks_all_passed"])
        self.assertIn("decoded RGB pixels for 181/181", qualification["display_caveat"])
        self.assertIn("accuracy effect is unassessed", mod.render_markdown(report))
        self.assertIn("does not explain the score gap", mod.render_metrics_csv(report))
        self.assertEqual((self.root / name).read_bytes(), original)
        compact["audited_runs"][0]["score_sha256"] = "changed"
        self.write(mod.VISION_INTEGRITY, compact)
        report = self.report()
        qualification = next(row for row in report["tasks"] if row["task_id"] == "B04")["result_qualifications"][0]
        self.assertFalse(qualification["score_sha256_matches"])
        self.assertIn("Historical", qualification["display_caveat"])
        self.assertTrue(any("Vision input-integrity qualification score hash mismatch" in warning for warning in report["warnings"]))

    def test_terminal_failed_scorer_and_mismatched_score_hash_exclude_completion(self):
        path = f"results/runs/{self.first_run}/completion.json"
        self.write(path, {"generation_exit_code": 0, "scoring_exit_code": 8})
        report = self.report()
        self.assertEqual(report["coverage"]["settings_with_completed_native_variant"], 0)
        self.assertEqual(report["runs"][0]["state"], "failed_or_stopped")
        self.assertEqual(report["runs"][0]["metrics"]["accuracy"], 0.4)
        self.write(path, {"generation_exit_code": 0, "scoring_exit_code": 0, "scores_sha256": "changed"})
        report = self.report()
        self.assertEqual(report["coverage"]["settings_with_completed_native_variant"], 0)
        self.assertTrue(any("Terminal score hash mismatch" in warning for warning in report["warnings"]))
        expected = hashlib.sha256((self.root / f"results/runs/{self.first_run}/scores.json").read_bytes()).hexdigest()
        self.write(path, {"generation_exit_code": 0, "scoring_exit_code": 0, "scores_sha256": expected})
        self.assertEqual(self.report()["coverage"]["settings_with_completed_native_variant"], 1)

    def test_source_recovery_qualifies_gated_releases_and_corrects_native_gaps(self):
        catalog = json.loads((self.root / mod.CATALOG).read_text())
        ids = ["P09", "P19", "P20", "P21", "P22", "P27", "V07", "N04", "N05"]
        for task_id in ids:
            catalog["tasks"].append({"id": task_id, "task": "Old Cell2Sentence name" if task_id == "N05" else "Old source contract",
                                     "family": "Synthetic", "metrics": "Old metric", "model_input": "Old modality"})
        catalog["counts"]["biological_evaluation_settings"] = 3 + len(ids)
        self.write(mod.CATALOG, catalog)
        protected = (self.root / mod.CATALOG).read_bytes()
        self.write(mod.SOURCE_RECOVERY, {"created_at_utc": "synthetic", "tasks": [
            {"task_id": task_id, "status": "official_release_found_gated_access_and_case_review_pending" if task_id in {"P19", "P20", "P21", "P22"} else "source_protocol_unresolved",
             "required_native_information": "Full original native inputs", "native_metric": "Exact native metric",
             "native_cases_verified": 0, "blockers": ["Exact native contract unrecovered"], "execution_authorized": False,
             "official_release": {"gated": "auto", "unauthenticated_schema_HEAD_http_status": 401}}
            for task_id in ids if task_id.startswith("P") or task_id == "V07"]})
        self.write(mod.POSTTRAIN_GAPS, {"date_utc": "synthetic", "source_code_repository": "https://example.org/official-posttrain", "N04": {"status": "Drive_auth_blocked",
            "required_input_contract": "Complete paired DNA windows and pathway context", "missing": ["Exact network split CSVs"],
            "author_release_link": "https://drive.google.com/example", "execution_authorized": False},
            "N05": {"status": "adapted_split_vector_alignment_unreleased", "task_identity": "MEDEA fixed candidate target selection",
                "required_inputs": "Original five candidates plus aligned normal/disease TranscriptFormer vectors",
                "native_metric_from_paper": "Exact normalized target match; native normalizer unrecovered",
                "missing": ["Adapted test manifest and vector alignment"], "execution_authorized": False}})
        report = self.report()
        rows = {row["task_id"]: row for row in report["tasks"]}
        self.assertEqual(rows["P19"]["state"], "source_access_gated_case_review_pending")
        self.assertEqual(rows["N04"]["state"], "source_access_authentication_blocked")
        self.assertEqual(rows["N05"]["task_name"], "Bio-posttrain MEDEA target selection")
        self.assertEqual(rows["N05"]["original_catalog_contract"]["task"], "Old Cell2Sentence name")
        self.assertEqual(rows["N05"]["source_url"], "https://example.org/official-posttrain")
        self.assertIn("TranscriptFormer", rows["N05"]["native_input_contract"])
        self.assertEqual(rows["P09"]["state"], "source_protocol_unresolved")
        markdown = mod.render_markdown(report)
        self.assertIn("HTTP 401", markdown)
        self.assertIn("synthetic placeholder", markdown)
        self.assertIn(mod.POSTTRAIN_GAPS, markdown)
        self.assertEqual((self.root / mod.CATALOG).read_bytes(), protected)
        self.assertTrue(all(not rows[task_id]["native_variant_completed"] for task_id in ids))

    def test_source_feasibility_is_not_execution_and_preserves_native_tasks(self):
        ids = ["P34", "P35", "P36", "P37", "P38", "P39", "P40", "P41"]
        catalog = json.loads((self.root / mod.CATALOG).read_text())
        catalog["tasks"].extend({"id": task_id, "task": "Valid native setting", "family": "Protein generation",
                                 "metrics": "Original metric", "model_input": "Original native context"} for task_id in ids)
        catalog["counts"]["biological_evaluation_settings"] = 3 + len(ids)
        self.write(mod.CATALOG, catalog)
        original = (self.root / mod.CATALOG).read_bytes()
        self.write(mod.P34_FEASIBILITY, {
            "task_id": "P34", "status": "prospective_adapter_only", "allowed_landscapes": ["a", "b", "c", "d", "e"],
            "entire_six_landscape_paper_setting_completed": False,
            "conclusion": {"prediction_task_retained": True, "missing_learned_qwen_joint_head_is_not_a_task_exclusion": True,
                           "qualified_adapter_mathematically_possible": True},
            "oracle_and_metrics": {"metrics": "Fixed proxy trajectory", "reference_source": "Released trained oracle",
                                   "full_five_budget_if_complete": {"oracle_scalar_values": 20100}},
            "remaining_blockers_or_decisions": ["Freeze native sampler/prior and likelihood interface; no forward performed."],
        })
        self.write(mod.NATURE_GENERATION_FEASIBILITY, {"native_tasks_retained": True, "inference_performed": False, "tasks": [
            {"task_id": task_id, "status": "sampling_or_oracle_contract_unrecovered", "native_metrics": {"native_proxy": {"value": None}},
             "source_prompt_or_input": {"native_generation_case_count": None, "source_condition_counts": {"illustrations": 30},
                                       "illustrative_source_prompts_not_benchmark_cases": True},
             "interpretation": {"information_supplied_to_solver": "Native condition only; none dispatched",
                                "reference_answer_source": "Frozen external predictor"},
             "residual_blockers": ["Exact sampling cohort and predictor unrecovered"]} for task_id in ["P37", "P38"]]})
        self.write(mod.DESIGN_FEASIBILITY, {"tasks": [
            {"task_id": task_id, "status": "public_source_with_prospective_protocol", "reporting_state": "native_protocol_setup_pending" if task_id == "P36" else "source_protocol_unresolved",
             "required_native_information": "Full framework/antigen/3D context", "native_metric": "Native metric, not a substitute",
             "reference_answer_source": "Native targets stay scorer-only", "prediction_task_retained": True,
             "artifact_availability": {"case_count": 5876 if task_id == "P36" else None,
                                       "raw_path": "data/DO_NOT_OPEN_unreviewed_cases.json"},
             "blockers": ["Input review and prospective exact evaluator freeze required"],
             "execution_authorized": False, "inference_performed": False, "prepared_model_cases": 0}
            for task_id in ["P35", "P36", "P39", "P40", "P41"]]})
        original_read = Path.read_bytes
        def metadata_only(path):
            if "DO_NOT_OPEN" in str(path):
                raise AssertionError("Reporter followed raw source instead of aggregate metadata")
            return original_read(path)
        with mock.patch.object(Path, "read_bytes", metadata_only):
            report = self.report()
        rows = {t["task_id"]: t for t in report["tasks"]}
        self.assertEqual(report["coverage"]["catalog_settings"], 11)
        self.assertEqual(report["coverage"]["settings_with_completed_native_variant"], 1)
        self.assertEqual(rows["P36"]["state"], "native_protocol_setup_pending")
        self.assertEqual(rows["P34"]["qualified_native_source_review"]["full_five_budget_if_complete"]["oracle_scalar_values"], 20100)
        self.assertFalse(rows["P34"]["qualified_native_source_review"]["entire_six_landscape_paper_setting_completed"])
        self.assertTrue(rows["P34"]["qualified_native_source_review"]["missing_learned_head_is_not_task_exclusion"])
        self.assertIn("Illustrative prompts are not benchmark cases", rows["P38"]["native_split_contract"])
        for task_id in ids:
            review = rows[task_id]["qualified_native_source_review"]
            self.assertFalse(rows[task_id]["native_variant_completed"])
            self.assertFalse(review["execution_authorized"])
            self.assertEqual(review["prepared_model_cases"], 0)
            self.assertEqual(len(review["source_sha256"]), 64)
            self.assertTrue(rows[task_id]["native_completion_blockers"])
        self.assertEqual((self.root / mod.CATALOG).read_bytes(), original)

    def test_live_completed_native_result_takes_precedence_over_pending_source_audit(self):
        self.write(mod.DESIGN_FEASIBILITY, {"tasks": [{"task_id": "P35", "status": "dated_pending",
            "reporting_state": "source_acquisition_pending", "blockers": ["Earlier source gap"],
            "prediction_task_retained": True, "execution_authorized": False}]})
        catalog = json.loads((self.root / mod.CATALOG).read_text())
        catalog["tasks"].append({"id": "P35", "task": "Native retrieval", "family": "Protein prediction"})
        catalog["counts"]["biological_evaluation_settings"] = 4
        self.write(mod.CATALOG, catalog)
        self.write("results/runs/later_native/scores.json", {"run_id": "later_native", "task_id": "P35",
            "protocol_variant": "NATIVE", "planned": 4, "completed": 4, "metrics": {"accuracy": 0.0}})
        row = next(t for t in self.report()["tasks"] if t["task_id"] == "P35")
        self.assertEqual(row["state"], "completed_native_variant")
        self.assertTrue(row["native_variant_completed"])
        self.assertEqual(row["native_completion_blockers"], [])
        self.assertEqual(row["qualified_native_source_review"]["status"], "dated_pending")


if __name__ == "__main__":
    unittest.main()
