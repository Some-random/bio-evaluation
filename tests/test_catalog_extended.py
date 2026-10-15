"""Synthetic fixtures for native target separation, parsers and provenance."""
import contextlib
import importlib.util
import io
import json
from pathlib import Path
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]


def load(name, filename):
    spec = importlib.util.spec_from_file_location(name, ROOT / "scripts" / filename)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


prep = load("extended_prepare", "prepare_catalog_extended.py")
scorer = load("extended_score", "score_local_catalog_extended.py")


class ExtendedTests(unittest.TestCase):
    def test_original_ontology_and_gold_separation(self):
        labels = [{"id": str(i), "name": f"Synthetic class{i}", "description": "Fixed synthetic definition"} for i in range(10)]
        model, ref = prep.transform("P03", 5, {"primary": "MABZX", "localization": 7, "reference_explanation": "SECRET_GOLD"}, labels)
        self.assertTrue(model["prompt"].endswith("MABZX"))
        self.assertEqual(ref["target"], 7)
        self.assertNotIn("SECRET_GOLD", str(model))
        self.assertNotIn("target", model)
        with self.assertRaises(ValueError):
            prep.transform("P03", 0, {"primary": "MA", "localization": 10}, labels)

    def test_native_numeric_scale_and_extra_metadata_separate(self):
        model, ref = prep.transform("P08", 2, {"primary": "MAG", "stability_score": 42.73, "parent": "SECRET_PARENT", "topology": "SECRET_TOPOLOGY"})
        self.assertEqual(ref["target"], 42.73)
        self.assertNotIn("42.73", model["prompt"])
        self.assertNotIn("SECRET", str(model))
        with self.assertRaises(ValueError):
            prep.transform("P07", 0, {"primary": "M A", "log_fluorescence": 2.0})

    def test_class_parser_keeps_invalid_and_missing(self):
        result = scorer.outcome_metrics("P03", [0, 9, 3, 2], ["0", "Answer: 9.", "3 or 2", None])
        self.assertEqual(result["accuracy"], 0.5)
        self.assertEqual((result["parsed"], result["invalid"], result["missing"]), (2, 1, 1))
        for text in ["10", "-1", "Nucleus", "9.0"]:
            self.assertIsNone(scorer.parse_class_id(text))

    def test_native_spearman_ties_incomplete_and_constant(self):
        result = scorer.outcome_metrics("P07", [1., 1., 4., 9.], ["9", "9", "4", "1"])
        self.assertAlmostEqual(result["spearman"], -1)
        partial = scorer.outcome_metrics("P08", [1., 2., 3.], ["3", None, "1"])
        self.assertIsNone(partial["spearman"])
        self.assertAlmostEqual(partial["spearman_parsed_only"], -1)
        self.assertIsNone(scorer.outcome_metrics("P08", [1., 2.], ["5", "5"])["spearman"])
        for text in ["NaN", "1e999", "7 or 8", "7C"]:
            self.assertIsNone(scorer.parse_number(text))

    def fixture(self, root):
        cases = [{"task": "P03", "case_id": str(i), "variant": "SYNTHETIC", "split": "fixture", "messages": [{"role": "user", "content": "Artificial case" + str(i)}]} for i in range(2)]
        (root / "inputs.jsonl").write_text("".join(json.dumps(r) + "\n" for r in cases))
        (root / "review.json").write_text(json.dumps({"approved_case_ids": ["0", "1"], "held_cases": []}))
        refs = [{"task": "P03", "case_id": str(i), "target": i} for i in range(2)]
        (root / "refs.jsonl").write_text("".join(json.dumps(r) + "\n" for r in refs))
        settings = {"run_id": "synthetic", "approved_task_ids": ["P03"], "variant": "SYNTHETIC", "model": "synthetic", "model_revision": "fake",
                    "generation": {"n": 1}, "input_file": "inputs.jsonl", "review_file": "review.json", "scorer_reference_file": "refs.jsonl",
                    "scorer_reference_sha256": scorer.file_digest(root / "refs.jsonl"), "frozen_files_sha256": {"inputs.jsonl": scorer.file_digest(root / "inputs.jsonl")}}
        folder = root / "run"
        (folder / "requests").mkdir(parents=True)
        (folder / "responses").mkdir()
        (folder / "run_manifest.json").write_text(json.dumps({"configuration": settings, "case_contract_sha256": scorer.digest(cases)}))
        case = cases[0]
        identity = scorer.digest([case["task"], case["variant"], case["case_id"]])
        payload = scorer.expected_payload(case, settings)
        request_hash = scorer.digest(payload)
        (folder / "requests" / (identity + ".json")).write_text(json.dumps({"payload": payload, "request_sha256": request_hash}))
        response = {**case, "model": settings["model"], "model_revision": settings["model_revision"], "request_sha256": request_hash, "status": "completed", "text": "0", "finish_reason": "stop"}
        (folder / "responses" / (identity + ".json")).write_text(json.dumps(response))
        return folder

    def score(self, root, folder):
        original = scorer.ROOT
        try:
            scorer.ROOT = root
            with contextlib.redirect_stdout(io.StringIO()):
                return scorer.score(folder)
        finally:
            scorer.ROOT = original

    def test_full_run_missing_case_and_output_lock(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            folder = self.fixture(root)
            summary = self.score(root, folder)
            self.assertEqual(summary["metrics"]["accuracy"], 0.5)
            self.assertEqual(summary["completed"], 1)
            raw = json.loads((folder / "per_case_scores.json").read_text())
            self.assertEqual(raw[0]["raw_text"], "0")
            self.assertEqual(raw[1]["status"], "not_dispatched")
            path = next((folder / "responses").glob("*.json"))
            row = json.loads(path.read_text());row["text"] = "1";path.write_text(json.dumps(row))
            with self.assertRaisesRegex(ValueError, "output lock"):
                self.score(root, folder)

    def test_preinference_reference_hash_enforced(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            folder = self.fixture(root)
            with (root / "refs.jsonl").open("a") as handle:
                handle.write("\n")
            with self.assertRaisesRegex(ValueError, "reference changed"):
                self.score(root, folder)


if __name__ == "__main__":
    unittest.main()
