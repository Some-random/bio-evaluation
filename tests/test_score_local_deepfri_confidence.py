import importlib.util
import json
from pathlib import Path
import shutil
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
spec = importlib.util.spec_from_file_location("score_local_deepfri_confidence", ROOT / "scripts/score_local_deepfri_confidence.py")
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)


class DeepFRIScoringTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.frozen_runtime = mod.runtime()
        cls.functions = mod.native_functions(ROOT, mod.SOURCE_SHA256)

    def test_source_native_rank_ap_and_tie_grouped_ap_remain_distinct(self):
        import torch
        metrics = mod.metrics_for(torch.tensor([[0.0, 0.0]]), torch.tensor([[1, 0]]), self.functions)
        self.assertAlmostEqual(metrics["auprc@micro"], 1.0)
        self.assertAlmostEqual(metrics["TIE_GROUPED_AP_DIAGNOSTIC"]["sklearn_micro_average_precision"], 0.5)
        self.assertIn("f1_max", metrics)

    def test_invalid_slot_keeps_full_metrics_null_without_zero_imputation(self):
        metrics, counts = mod.matrix_metrics([{"A": 0.8}, None], [[0], [1]], ["A", "B"], self.functions)
        self.assertIsNone(metrics["auprc@micro"])
        self.assertIsNone(metrics["f1_max"])
        self.assertEqual(metrics["PARSED_ONLY_DIAGNOSTIC"]["valid_cases"], 1)
        self.assertFalse(metrics["OFFLINE_ALL_ZERO_REFERENCE"]["is_model_prediction"])
        self.assertEqual(counts["valid_vectors"], 1)
        self.assertFalse(counts["score_based_case_filtering"])

    def test_explicit_empty_numeric_vector_is_valid_all_zero(self):
        metrics, counts = mod.matrix_metrics([{}, {"B": 0}], [[0], [1]], ["A", "B"], self.functions)
        self.assertIsNotNone(metrics["auprc@micro"])
        self.assertEqual(counts["all_zero_vectors"], 2)
        self.assertEqual(counts["explicit_empty_vectors"], 1)

    def fixture(self, bad_model=False, malformed=False):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        root = Path(temp.name)
        names = ["scripts/score_local_deepfri_confidence.py", "scripts/score_local_genomics.py", "scripts/prepare_local_deepfri_proposals.py", mod.SOURCE, mod.TIE_HELPER, "scripts/run_local_labbench_multimodal.py"]
        for name in names:
            target = root / name
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(ROOT / name, target)
        task = "P12"
        classes = [{"index": i, "class_id": f"C{i:03d}", "description": "synthetic"} for i in range(538)]
        case = {"task": task, "case_id": "synthetic-case", "variant": "QWEN_ZERO_SHOT_SYNTHETIC", "split": "test", "messages": [{"role": "user", "content": "Synthetic benign annotation input."}]}
        values = {"data/inputs.jsonl": json.dumps(case) + "\n", "data/review.json": json.dumps({"input_review_only": True, "approved_case_ids": [case["case_id"]], "held_cases": []}), "data/vocabulary.json": json.dumps({"classes": classes}), "data/references.jsonl": json.dumps({"task_id": task, "case_id": case["case_id"], "scorer_only": True, "positive_class_indices": [0], "positive_class_ids": ["C000"]}) + "\n", "data/runtime.json": json.dumps(self.frozen_runtime)}
        for name, text in values.items():
            path = root / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(text)
        settings = {"run_id": "synthetic", "approved_task_ids": [task], "model": "SyntheticModel", "model_revision": "pinned", "variant": case["variant"], "planned": 1, "generation": {"max_tokens": 4096, "n": 1}, "tool_access": [], "runner": "scripts/run_local_labbench_multimodal.py", "input_file": "data/inputs.jsonl", "review_file": "data/review.json", "class_vocabulary_file": "data/vocabulary.json", "scorer_reference_file": "data/references.jsonl", "scoring_runtime_file": "data/runtime.json", "input_modalities": ["protein_sequence_text"], "case_scope": "synthetic_only", "paper_comparison": "Synthetic test, no benchmark result."}
        settings["scorer_reference_sha256"] = mod.file_digest(root / settings["scorer_reference_file"])
        settings["frozen_files_sha256"] = {name: mod.file_digest(root / name) for name in names + list(values)}
        config = root / "configs/synthetic.json"
        config.parent.mkdir()
        config.write_text(json.dumps(settings))
        folder = root / "results/runs/synthetic"
        (folder / "requests").mkdir(parents=True)
        (folder / "responses").mkdir()
        manifest = {"configuration": settings, "configuration_sha256": mod.file_digest(config), "case_contract_sha256": mod.digest([case]), "planned_cases": 1, "runner_sha256": settings["frozen_files_sha256"][settings["runner"]]}
        (folder / "run_manifest.json").write_text(json.dumps(manifest))
        payload = mod.expected_payload(case, settings)
        request = {**{key: case[key] for key in ["task", "case_id", "variant", "split"]}, "payload": payload, "request_sha256": mod.digest(payload)}
        final = "A label list is invalid" if malformed else '{"scores":{"C000":0.75}}'
        response = {**{key: case[key] for key in ["task", "case_id", "variant", "split"]}, "model": "WrongModel" if bad_model else settings["model"], "model_revision": settings["model_revision"], "request_sha256": request["request_sha256"], "status": "completed", "http_status": 200, "text": final, "finish_reason": "stop", "response": {"model": settings["model"], "choices": [{"message": {"content": final, "reasoning": "Synthetic reasoning ignored by final-only parser."}, "finish_reason": "stop"}]}}
        identity = mod.digest([task, case["variant"], case["case_id"]]) + ".json"
        (folder / "requests" / identity).write_text(json.dumps(request))
        (folder / "responses" / identity).write_text(json.dumps(response))
        return root, folder, config

    def test_locked_end_to_end_summary_and_changed_response_rejected(self):
        root, folder, config = self.fixture()
        score = mod.score(folder, root, config)
        self.assertTrue(score["predictions_locked_before_reference_read"])
        self.assertTrue(score["full_planned_primary_metrics_valid"])
        self.assertEqual(score["planned"], 1)
        path = next((folder / "responses").glob("*.json"))
        path.write_text(path.read_text() + " ")
        with self.assertRaisesRegex(ValueError, "output lock changed"):
            mod.score(folder, root, config)

    def test_wrong_model_fails_before_scoring_and_malformed_has_null_primaries(self):
        root, folder, config = self.fixture(bad_model=True)
        with self.assertRaisesRegex(ValueError, "provenance mismatch"):
            mod.score(folder, root, config)
        self.assertTrue((folder / "scoring_output_lock.json").exists())
        self.assertFalse((folder / "scores.json").exists())
        root, folder, config = self.fixture(malformed=True)
        score = mod.score(folder, root, config)
        self.assertFalse(score["full_planned_primary_metrics_valid"])
        self.assertIsNone(score["metrics"]["auprc@micro"])
        self.assertEqual(score["invalid_outputs"], 1)

    def test_new_explicitly_frozen_runner_path_keeps_identical_payload_contract(self):
        root, folder, config = self.fixture()
        settings = json.loads(config.read_text())
        alternate = "scripts/run_local_labbench_eight_gpu.py"
        shutil.copyfile(root / settings["runner"], root / alternate)
        settings["runner"] = alternate
        settings["frozen_files_sha256"][alternate] = mod.file_digest(root / alternate)
        config.write_text(json.dumps(settings))
        manifest_path = folder / "run_manifest.json"
        manifest = json.loads(manifest_path.read_text())
        manifest["configuration"] = settings
        manifest["configuration_sha256"] = mod.file_digest(config)
        manifest["runner_sha256"] = settings["frozen_files_sha256"][alternate]
        manifest_path.write_text(json.dumps(manifest))
        self.assertTrue(mod.score(folder, root, config)["full_planned_primary_metrics_valid"])


if __name__ == "__main__":
    unittest.main()
