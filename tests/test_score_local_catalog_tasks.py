"""End-to-end synthetic provenance, missing-case and parser accounting."""
import contextlib
import importlib.util
import io
import json
from pathlib import Path
import sys
import tempfile
import unittest

SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS))
spec = importlib.util.spec_from_file_location("catalog_run_score", SCRIPTS / "score_local_catalog_tasks.py")
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)


class LocalCatalogScoringTests(unittest.TestCase):
    def fixture(self, root, task, outputs):
        folder = root / "results/runs/synthetic"
        (folder / "responses").mkdir(parents=True)
        (folder / "requests").mkdir()
        cases = [{"task": task, "case_id": str(i), "variant": "SYNTHETIC", "split": "synthetic",
                  "messages": [{"role": "user", "content": "Artificial fixture " + str(i)}]} for i in range(3)]
        (root / "inputs.jsonl").write_text("".join(json.dumps(r) + "\n" for r in cases))
        (root / "review.json").write_text(json.dumps({"approved_case_ids": ["0", "1", "2"], "held_cases": []}))
        refs = [{"task": task, "case_id": str(i), "target_binary": i % 2, "target": float(i)} for i in range(3)]
        (root / "refs.jsonl").write_text("".join(json.dumps(r) + "\n" for r in refs))
        settings = {"run_id": "synthetic", "approved_task_ids": [task], "variant": "SYNTHETIC", "model": "synthetic-model",
                    "model_revision": "synthetic-revision", "generation": {"n": 1, "max_tokens": 10},
                    "input_file": "inputs.jsonl", "review_file": "review.json", "scorer_reference_file": "refs.jsonl",
                    "scorer_reference_sha256": mod.file_digest(root / "refs.jsonl"),
                    "frozen_files_sha256": {"inputs.jsonl": mod.file_digest(root / "inputs.jsonl"), "review.json": mod.file_digest(root / "review.json")}}
        (folder / "run_manifest.json").write_text(json.dumps({"configuration": settings, "case_contract_sha256": mod.digest(cases)}))
        for case, text in zip(cases, outputs):
            if text is None:
                continue
            identity = mod.digest([task, case["variant"], case["case_id"]])
            payload = mod.expected_payload(case, settings)
            request_hash = mod.digest(payload)
            (folder / "requests" / (identity + ".json")).write_text(json.dumps({"payload": payload, "request_sha256": request_hash}))
            (folder / "responses" / (identity + ".json")).write_text(json.dumps({**case, "model": settings["model"],
                "model_revision": settings["model_revision"], "request_sha256": request_hash, "status": "completed", "text": text,
                "finish_reason": "stop"}))
        return folder

    def score(self, root, folder):
        original = mod.ROOT
        try:
            mod.ROOT = root
            with contextlib.redirect_stdout(io.StringIO()):
                return mod.score(folder)
        finally:
            mod.ROOT = original

    def test_binary_preserves_invalid_and_missing_denominator(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            folder = self.fixture(root, "P11", ["No.", "Yes and No", None])
            result = self.score(root, folder)
            self.assertAlmostEqual(result["metrics"]["accuracy"], 1 / 3)
            self.assertEqual((result["completed"], result["parsed"], result["invalid_outputs"]), (2, 1, 1))
            cases = json.loads((folder / "per_case_scores.json").read_text())
            self.assertEqual(cases[1]["raw_text"], "Yes and No")
            self.assertEqual(cases[2]["status"], "not_dispatched")

    def test_numeric_native_metric_and_provenance_mismatch(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            folder = self.fixture(root, "P06", ["3", "2", "1"])
            self.assertAlmostEqual(self.score(root, folder)["metrics"]["spearman"], -1)
            response = next((folder / "responses").glob("*.json"))
            row = json.loads(response.read_text()); row["model_revision"] = "different"
            response.write_text(json.dumps(row))
            with self.assertRaisesRegex(ValueError, "output lock changed"):
                self.score(root, folder)

    def test_reference_changes_are_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            folder = self.fixture(root, "P06", ["3", "2", "1"])
            with (root / "refs.jsonl").open("a") as handle:
                handle.write("\n")
            with self.assertRaisesRegex(ValueError, "references differ"):
                self.score(root, folder)


if __name__ == "__main__":
    unittest.main()
