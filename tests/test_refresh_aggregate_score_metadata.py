"""Synthetic metadata retention and mixed-budget reporting regressions."""
import copy
import json
from pathlib import Path
import shutil
import sys
import tempfile
import unittest
from unittest import mock

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import refresh_aggregate_score_metadata as refresh
import update_results_at_a_glance as scores


class AggregateMetadataTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.write(scores.COMPARISONS, {"task_count": 64, "tasks": [
            {"task_id": "P10", "task": "Synthetic interaction", "published_baselines": []}]})

    def write(self, name, value):
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(value) + "\n")
        return path

    def emit(self, run, task="P10", variant="SYNTHETIC", metric=.5, condition=None, budgets=None, dataset=None):
        base = "results/runs/" + run
        score = {"run_id": run, "task_id": task, "protocol_variant": variant,
            "planned": 3, "completed": 3, "parsed": 3, "invalid_outputs": 0,
            "metrics": {"accuracy": metric}, "case_scope": "full_synthetic_test"}
        if condition:
            score.update(generation_budget_condition=condition,
                generation={"max_tokens": None, "output_budget_counts": budgets})
        if dataset:
            score["dataset"] = dataset
        source = self.write(base + "/scores.json", score)
        manifest = self.write(base + "/run_manifest.json", {"configuration": {
            "approved_task_ids": [task], "generation": {"max_tokens": 4096, "temperature": 1.0},
            "input_file": "NEVER_OPEN/inputs.jsonl", "scorer_reference_file": "NEVER_OPEN/labels.jsonl"}})
        self.write(base + "/completion.json", {"generation_exit_code": 0, "scoring_exit_code": 0,
            "scores_sha256": scores.sha(source.read_bytes()),
            "run_manifest_sha256": scores.sha(manifest.read_bytes()),
            "finished_at_utc": "2026-10-18T20:00:00+00:00"})

    def build(self):
        return scores.build_report(self.root, generated_at="2026-10-18T21:00:00+00:00")

    def collect(self):
        return refresh.collect(self.root, generated_at="2026-10-18T21:00:00+00:00")

    def test_unmounted_old_valid_and_undefined_rows_survive_new_mixed_result(self):
        self.emit("old_native")
        self.emit("old_undefined", task="P06", metric=None)
        previous = self.build()
        self.write(refresh.REPORT, previous)
        shutil.rmtree(self.root / "results/runs")
        self.emit("new_mixed", variant="SYNTHETIC__MIXED_BUDGET_4K16K_CONTINUATION",
            condition="MIXED_BUDGET_4K16K_CONTINUATION", budgets={"4096": 2, "16384": 1})
        value = self.collect()
        self.assertEqual({row["run_id"] for row in value["completed_rows"]}, {"old_native", "new_mixed"})
        diagnostic = value["diagnostic_only_finished_runs"][0]
        self.assertEqual(diagnostic["run_id"], "old_undefined")
        self.assertIsNone(diagnostic["metrics"]["accuracy"])
        old = next(row for row in value["completed_rows"] if row["run_id"] == "old_native")
        self.assertEqual(old["scores_sha256"], previous["completed_rows"][0]["scores_sha256"])
        self.assertEqual(old["counts"], previous["completed_rows"][0]["counts"])
        mixed = next(row for row in value["completed_rows"] if row["run_id"] == "new_mixed")
        self.assertIsNone(mixed["generation"]["max_tokens"])
        self.assertEqual(mixed["generation"]["output_budget_counts"], {"4096": 2, "16384": 1})
        self.assertEqual(mixed["generation"]["temperature"], 1.0)
        text = scores.render_markdown(value)
        self.assertIn("Mixed 4K/16K continuation", text)
        self.assertIn("2 original cases retain 4,096", text)
        self.assertIn("1 previously undispatched cases use 16,384", text)
        self.assertIn("4,096/16,384 tokens", text)
        self.assertNotIn("P06", value["completed_whole_declared_setting_ids"])

    def test_exact_identity_replaces_category_but_other_run_remains(self):
        self.emit("same_identity")
        self.emit("other_run")
        previous = self.build()
        shutil.rmtree(self.root / "results/runs")
        self.emit("same_identity", metric=None)
        current = self.build()
        value = refresh.merged_report(current, [(previous, "historical.json", "a" * 64)])
        self.assertEqual([row["run_id"] for row in value["completed_rows"]], ["other_run"])
        self.assertEqual([row["run_id"] for row in value["diagnostic_only_finished_runs"]], ["same_identity"])
        self.assertEqual(value["completed_whole_declared_setting_ids"], ["P10"])
        only_same = copy.deepcopy(previous)
        only_same["completed_rows"] = [row for row in only_same["completed_rows"] if row["run_id"] == "same_identity"]
        self.assertEqual(refresh.merged_report(current, [(only_same, "old.json", "b" * 64)])["completed_whole_declared_setting_ids"], [])

    def test_archive_filters_display_only_and_repeat_collection_is_idempotent(self):
        self.emit("old_archive", task="N03")
        self.emit("old_main")
        previous = self.build()
        self.write(refresh.REPORT, previous)
        shutil.rmtree(self.root / "results/runs")
        self.write(scores.MAIN_SCOPE, {"excluded_task_ids": ["N03"], "excluded_family": "Synthetic archive",
            "archive_report": "ARCHIVED_EVALUATIONS.md"})
        first = self.collect()
        self.assertEqual(len(first["completed_rows"]), 2)
        self.assertEqual(first["main_completed_whole_declared_setting_ids"], ["P10"])
        self.assertNotIn("N03", scores.render_markdown(first))
        scores.write_report(self.root, first)
        second = refresh.collect(self.root, generated_at="2026-10-19T22:00:00+00:00")
        self.assertEqual(first, second)

    def test_verified_history_requires_pinned_digest_and_never_opens_raw_files(self):
        self.emit("history")
        previous = self.build()
        historical = self.write(refresh.VERIFIED_HISTORY, previous)
        checksum = scores.sha(historical.read_bytes())
        shutil.rmtree(self.root / "results/runs")
        original = Path.read_bytes
        def guarded(path):
            if any(part in {"requests", "responses", "NEVER_OPEN"} for part in path.parts):
                raise AssertionError("Raw case, answer or target read")
            return original(path)
        with mock.patch.object(refresh, "VERIFIED_HISTORY_SHA256", checksum), mock.patch.object(Path, "read_bytes", guarded):
            value = self.collect()
        self.assertEqual(value["completed_rows"][0]["run_id"], "history")
        with self.assertRaisesRegex(ValueError, "historical.*hash mismatch"):
            self.collect()

    def test_same_condition_keeps_all_run_ids_but_compact_display_uses_latest(self):
        self.emit("older")
        previous = self.build()
        previous["completed_rows"][0]["finished_at_utc"] = "2026-10-17T20:00:00+00:00"
        shutil.rmtree(self.root / "results/runs")
        self.emit("newer")
        value = refresh.merged_report(self.build(), [(previous, "old.json", "c" * 64)])
        self.assertEqual({row["run_id"] for row in value["completed_rows"]}, {"older", "newer"})
        text = scores.render_markdown(value, self.root)
        self.assertIn("runs/newer/scores.json", text)
        self.assertNotIn("runs/older/scores.json", text)

    def test_old_validated_three_dataset_proof_and_individual_metrics_survive(self):
        self.emit("human", task="P43", dataset="human")
        previous = self.build()
        row = previous["completed_rows"][0]
        row.update(dataset="human", completion_scope="dataset_component")
        proof = copy.deepcopy(row)
        proof.update(run_id="full_three_dataset", completion_scope="verified_three_dataset_aggregate",
            full_test_id_union_validation={"complete": True, "union_matches_full_test_ids": True,
                "expected_test_case_count": 16533, "unique_observed_case_count": 16533,
                "missing_case_count": 0, "extra_case_count": 0})
        previous["P43"]["validated_aggregate_containers"] = [proof]
        previous["P43"]["whole_setting_complete"] = True
        shutil.rmtree(self.root / "results/runs")
        value = refresh.merged_report(self.build(), [(previous, "old.json", "d" * 64)])
        self.assertTrue(value["P43"]["whole_setting_complete"])
        self.assertIn("P43", value["completed_whole_declared_setting_ids"])
        self.assertEqual(value["completed_rows"][0]["metrics"], row["metrics"])


if __name__ == "__main__":
    unittest.main()
