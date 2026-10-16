"""Synthetic completion/union, null, provenance and output-format reporting tests."""
import copy
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest import mock

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import update_results_at_a_glance as report


class ReportTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory(); self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.write(report.COMPARISONS, {"task_count": 64, "tasks": [
            {"task_id": "P10", "task": "Synthetic PPI", "published_baselines": [{"model": "BioT5+", "metrics": {"accuracy_percent": 80.0}, "source_url": "https://example.org/primary", "source_locator": "Synthetic table"}]},
            {"task_id": "P43", "task": "Synthetic DTI", "published_baselines": [{"model": "BioT5+", "metrics": {"human_auroc": .9, "biosnap_auroc": .8, "bindingdb_auroc": .7}, "source_url": "https://example.org/primary", "source_locator": "Synthetic table"}]}]})

    def write(self, name, value):
        path = self.root / name; path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(value) + "\n"); return path

    def emit(self, run, task="P10", planned=2, metrics=None, score_extra=None, config_extra=None, completion_extra=None):
        base = "results/runs/" + run
        score = {"task_id": task, "run_id": run, "model": "Qwen/Qwen3.8-27B", "model_revision": "synthetic",
            "protocol_variant": "SYNTHETIC", "planned": planned, "completed": planned, "parsed": planned,
            "invalid_outputs": 0, "case_scope": "full_synthetic_test", "metrics": {"accuracy": .5} if metrics is None else metrics,
            "finish_reasons": {"stop": planned}, **(score_extra or {})}
        config = {"approved_task_ids": [task], "model": score["model"], "generation": {"max_tokens": 4096},
            "input_file": "NEVER_OPEN/model_inputs.jsonl", "scorer_reference_file": "NEVER_OPEN/gold.jsonl", **(config_extra or {})}
        source = self.write(base + "/scores.json", score)
        manifest = self.write(base + "/run_manifest.json", {"configuration": config})
        self.write(base + "/completion.json", {"generation_exit_code": 0, "scoring_exit_code": 0,
            "scores_sha256": report.sha(source.read_bytes()), "run_manifest_sha256": report.sha(manifest.read_bytes()), **(completion_extra or {})})
        return score, source

    def build(self): return report.build_report(self.root, generated_at="synthetic_snapshot")

    def test_shard_or_unverified_union_never_whole_task_completion(self):
        self.emit("shard", task="P03", score_extra={"case_scope": "task_shard_only", "shard_index": 0})
        self.emit("unverified_aggregate", task="P07", config_extra={"shard_count": 2})
        self.emit("diagnostic", task="N01", score_extra={"full_planned_primary_metrics_valid": False})
        value = self.build()
        self.assertEqual(value["completed_rows"], [])
        self.assertEqual(value["completed_whole_declared_setting_ids"], [])
        self.assertEqual({r["reason"] for r in value["excluded_or_not_yet_terminal_runs"]},
            {"shard_only", "unverified_shard_aggregate", "diagnostic_only_primary_metrics_invalid"})

    def test_validated_future_full_aggregate_appears_without_metric_reinterpretation(self):
        union = {"complete": True, "union_matches_full_test_ids": True, "expected_test_case_count": 2,
                 "unique_observed_case_count": 2, "missing_case_count": 0, "extra_case_count": 0}
        self.emit("full_future", task="P07", metrics={"Spearman": .12345}, config_extra={"shard_count": 2},
                  score_extra={"full_test_id_union_validation": union, "metric_units": "native Spearman correlation"})
        value = self.build(); self.assertEqual(value["completed_whole_declared_setting_ids"], ["P07"])
        self.assertEqual(value["completed_rows"][0]["metrics"], {"Spearman": .12345})
        self.assertIn("Spearman 0.1235", report.render_markdown(value))

    def test_union_proof_count_must_match_planned_denominator(self):
        union = {"complete": True, "union_matches_full_test_ids": True, "expected_test_case_count": 1,
                 "unique_observed_case_count": 1, "missing_case_count": 0, "extra_case_count": 0}
        self.emit("wrong_union_count", task="P07", config_extra={"shard_count": 2}, score_extra={"full_test_id_union_validation": union})
        value = self.build(); self.assertEqual(value["completed_rows"], [])
        self.assertEqual(value["excluded_or_not_yet_terminal_runs"][0]["reason"], "unverified_shard_aggregate")

    def test_three_dti_components_require_explicit_validated_aggregate_no_pooling(self):
        component_metrics = {}
        for index, (dataset, count) in enumerate(report.P43_COUNTS.items()):
            metric = {"auroc": .4 + index / 10, "auprc": .3 + index / 10}; component_metrics[dataset] = metric
            self.emit(dataset, task="P43", planned=count, metrics=metric, score_extra={"dataset": dataset})
        value = self.build(); self.assertFalse(value["P43"]["whole_setting_complete"])
        self.assertNotIn("P43", value["completed_whole_declared_setting_ids"])
        self.assertEqual(len(value["completed_rows"]), 3)
        self.assertIn("whole setting remains incomplete", report.render_markdown(value))
        union = {"complete": True, "union_matches_full_test_ids": True, "expected_test_case_count": 16533,
                 "unique_observed_case_count": 16533, "missing_case_count": 0, "extra_case_count": 0}
        self.emit("all_datasets", task="P43", planned=16533, metrics=component_metrics,
            score_extra={"case_scope": "complete_three_native_tests_separate_metrics", "full_test_id_union_validation": union,
                         "dataset_case_counts": report.P43_COUNTS, "dataset_metrics": component_metrics})
        value = self.build(); self.assertTrue(value["P43"]["whole_setting_complete"])
        self.assertEqual(len(value["completed_rows"]), 3)
        self.assertEqual({r["dataset"]: r["metrics"] for r in value["completed_rows"]}, component_metrics)
        self.assertEqual(value["completed_whole_declared_setting_ids"], ["P43"])

    def test_null_stays_undefined_and_real_zero_remains_zero(self):
        self.emit("undefined", metrics={"accuracy": None})
        value = self.build(); self.assertEqual(value["completed_rows"], [])
        self.assertIsNone(value["diagnostic_only_finished_runs"][0]["metrics"]["accuracy"])
        self.assertEqual(value["completed_whole_declared_setting_ids"], [])
        text = report.render_markdown(value); self.assertIn("accuracy undefined", text); self.assertNotIn("accuracy 0.0%", text)
        self.assertEqual(report.format_value("accuracy", 0), "0.0%")
        self.assertIsNone(report.clean(float("nan")))

    def test_legacy_regression_parsed_only_cannot_complete_full_benchmark(self):
        self.emit("p06", task="P06", planned=1366,
                  metrics={"spearman": None, "spearman_parsed_only": .025374, "planned": 1366, "parsed": 1354},
                  score_extra={"parsed": 1354, "invalid_outputs": 12})
        value = self.build()
        self.assertEqual(value["completed_whole_declared_setting_ids"], [])
        self.assertEqual(value["completed_rows"], [])
        diagnostic = value["diagnostic_only_finished_runs"][0]
        self.assertIsNone(diagnostic["metrics"]["spearman"])
        self.assertEqual(diagnostic["metrics"]["spearman_parsed_only"], .025374)
        self.assertIn("incomplete diagnostics", report.render_markdown(value))

    def test_terminal_hash_mismatch_or_nonzero_status_excluded(self):
        _, source = self.emit("tampered"); value = json.loads(source.read_text()); value["metrics"]["accuracy"] = 1
        source.write_text(json.dumps(value))
        self.emit("failure", completion_extra={"generation_exit_code": 1})
        value = self.build(); self.assertEqual(value["completed_rows"], [])
        self.assertEqual({r["reason"] for r in value["excluded_or_not_yet_terminal_runs"]},
                         {"terminal_score_hash_mismatch", "missing_or_nonzero_terminal_completion"})

    def test_zero_format_conditions_never_become_wrong_biology_claims(self):
        self.emit("b08", task="B08", planned=33, metrics={"accuracy": 0, "precision": 0, "coverage": 1},
                  score_extra={"parsed": 0, "invalid_outputs": 33, "finish_reasons": {"length": 33}})
        _, source = self.emit("v04", task="V04", planned=500, metrics={"strict_accuracy": 0})
        self.write("reports/v04_output_format_qualification.json", {"run_id": "v04", "score_sha256": report.sha(source.read_bytes())})
        text = report.render_markdown(self.build())
        self.assertIn("zero parsed answers", text); self.assertIn("does not establish wrong biological predictions", text)
        self.assertIn("verbose answer format is material", text); self.assertIn("does not establish wrong clinical predictions", text)

    def test_only_aggregate_metadata_read_no_reference_or_input_following(self):
        self.emit("safe")
        original = Path.read_bytes
        def guarded(path):
            if "NEVER_OPEN" in path.parts or path.name in {"per_case_scores.json", "model_inputs.jsonl", "gold.jsonl"}:
                raise AssertionError("Reporter attempted a raw input/output/reference read")
            return original(path)
        with mock.patch.object(Path, "read_bytes", guarded): value = self.build()
        self.assertEqual(len(value["completed_rows"]), 1)

    def test_p29_seed_context_audit_is_separate_from_model_results(self):
        self.write("reports/catalog_posttrain_protein_preparation.json", {"native_target_augmentation": "Synthetic input/reference dependence",
            "splits": {"ood": {"seed_predictor_overlap": {"seed_context_only_native_augmented_mean_propagated_F1": .9,
                "seed_context_only_curated_mean_propagated_F1_diagnostic": .6}}}})
        value = self.build(); self.assertEqual(value["completed_rows"], [])
        self.assertNotIn("P29", value["completed_whole_declared_setting_ids"])
        self.assertIn("not Qwen results", report.render_markdown(value))


if __name__ == "__main__": unittest.main()
