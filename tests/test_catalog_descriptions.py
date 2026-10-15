"""Synthetic-only source-field, exact ROUGE and frozen-output validation."""
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


prep = load("description_prepare", "prepare_catalog_descriptions.py")
scorer = load("description_score", "score_local_descriptions.py")


class DescriptionTests(unittest.TestCase):
    def test_source_instruction_and_gold_separation(self):
        instance = {"id": "synthetic", "instruction": "Describe this synthetic sequence.", "input": "<bop><p>M<p>Z<p>X<eop>", "output": ["SECRET_GOLD"]}
        template = {"prompt_input": "Instruction: {instruction}\nInput: {input}\nResponse:"}
        model, native, ref = prep.transform("P25", 0, instance, template)
        self.assertEqual(model["prompt"], "Instruction: Describe this synthetic sequence.\nInput: MZX\nResponse:")
        self.assertNotIn("SECRET_GOLD", str(model))
        self.assertNotIn("SECRET_GOLD", str(native))
        self.assertEqual(ref["target"], "SECRET_GOLD")
        self.assertEqual(native["native_serialized_input"], instance["input"])
        instance["teacher_explanation"] = "leak"
        with self.assertRaises(ValueError):
            prep.transform("P25", 0, instance, template)

    def test_no_reference_choice_or_sequence_cleaning(self):
        with self.assertRaises(ValueError):
            prep.decode_sequence("<bop><p>M <p>A<eop>")
        instance = {"id": "s", "instruction": "Synthetic", "input": "<bop><p>M<eop>", "output": ["one", "two"]}
        with self.assertRaises(ValueError):
            prep.transform("P25", 0, instance, {"prompt_input": "{instruction}{input}"})

    def test_official_default_no_stemming_and_lcs(self):
        result = scorer.lexical_metrics(["A, C! B"], ["a b c"])
        self.assertEqual(result["rouge1"], 1.)
        self.assertAlmostEqual(result["rougeL"], 2 / 3)
        self.assertEqual(scorer.lexical_metrics(["cats running"], ["cat run"])["rougeL"], 0.)
        self.assertEqual(scorer.lexical_metrics([""], ["synthetic reference"])["rougeL"], 0.)

    def test_rng_restored_and_multi_reference_input_not_accepted(self):
        import numpy as np
        before = np.random.get_state()
        one = scorer.lexical_metrics(["alpha", "gamma"], ["alpha", "beta"])
        after = np.random.get_state()
        self.assertEqual(before[0], after[0]);self.assertTrue(np.array_equal(before[1], after[1]))
        self.assertEqual(before[2:], after[2:])
        self.assertEqual(one, scorer.lexical_metrics(["alpha", "gamma"], ["alpha", "beta"]))
        with self.assertRaises(ValueError):
            scorer.lexical_metrics(["synthetic input"], [["gold annotation", "synthetic input"]])

    def fixture(self, root):
        metric = root / scorer.METRIC_PATH
        metric.parent.mkdir(parents=True)
        metric.write_bytes((ROOT / scorer.METRIC_PATH).read_bytes())
        cases = [{"task": "P25", "case_id": str(i), "variant": "SYNTHETIC", "split": "fixture", "messages": [{"role": "user", "content": "Artificial input" + str(i)}]} for i in range(2)]
        (root / "inputs.jsonl").write_text("".join(json.dumps(r) + "\n" for r in cases))
        (root / "review.json").write_text(json.dumps({"approved_case_ids": ["0", "1"], "held_cases": []}))
        refs = [{"task": "P25", "case_id": str(i), "target": "synthetic annotation"} for i in range(2)]
        (root / "refs.jsonl").write_text("".join(json.dumps(r) + "\n" for r in refs))
        settings = {"run_id": "synthetic", "approved_task_ids": ["P25"], "variant": "SYNTHETIC", "model": "synthetic", "model_revision": "fake", "generation": {"n": 1},
                    "input_file": "inputs.jsonl", "review_file": "review.json", "scorer_reference_file": "refs.jsonl", "scorer_reference_sha256": scorer.file_digest(root / "refs.jsonl"),
                    "frozen_files_sha256": {"inputs.jsonl": scorer.file_digest(root / "inputs.jsonl")}}
        folder = root / "run"
        (folder / "requests").mkdir(parents=True);(folder / "responses").mkdir()
        (folder / "run_manifest.json").write_text(json.dumps({"configuration": settings, "case_contract_sha256": scorer.digest(cases)}))
        case = cases[0]
        identity = scorer.digest([case["task"], case["variant"], case["case_id"]])
        payload = scorer.expected_payload(case, settings);request_hash = scorer.digest(payload)
        (folder / "requests" / (identity + ".json")).write_text(json.dumps({"payload": payload, "request_sha256": request_hash}))
        response = {**case, "model": settings["model"], "model_revision": settings["model_revision"], "request_sha256": request_hash, "status": "completed", "text": "synthetic annotation", "finish_reason": "stop"}
        (folder / "responses" / (identity + ".json")).write_text(json.dumps(response))
        return folder

    def score(self, root, folder):
        original = scorer.ROOT
        try:
            scorer.ROOT = root;scorer.official_metric_function.cache_clear()
            with contextlib.redirect_stdout(io.StringIO()):
                return scorer.score(folder)
        finally:
            scorer.ROOT = original;scorer.official_metric_function.cache_clear()

    def test_completed_only_score_and_raw_output_lock(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp);folder = self.fixture(root)
            result = self.score(root, folder)
            self.assertIsNone(result["metrics"]["rougeL"])
            self.assertEqual(result["metrics"]["rougeL_completed_only"], 1.)
            self.assertEqual((result["planned"], result["completed"]), (2, 1))
            path = next((folder / "responses").glob("*.json"))
            row = json.loads(path.read_text());row["text"] = "other";path.write_text(json.dumps(row))
            with self.assertRaisesRegex(ValueError, "output lock"):
                self.score(root, folder)

    def test_reference_hash_enforced(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp);folder = self.fixture(root)
            with (root / "refs.jsonl").open("a") as handle:handle.write("\n")
            with self.assertRaisesRegex(ValueError, "reference differs"):
                self.score(root, folder)


if __name__ == "__main__":
    unittest.main()
