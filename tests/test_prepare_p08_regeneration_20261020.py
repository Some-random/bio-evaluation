"""Synthetic P08 input preservation and native-scale contract tests."""
import copy
import hashlib
import importlib.util
import json
from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("prepare_p08_new", ROOT / "scripts/prepare_p08_regeneration_20261020.py")
p08 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(p08)


def synthetic_row():
    prompt = p08.sequence_prompt("ACDEFGHIKL")
    return {"task": "P08", "case_id": "stability:test:0", "source_index": 0,
            "split": "official_released_test", "system": "", "prompt": prompt,
            "prompt_sha256": p08.sha(prompt.encode()),
            "fields": {"sequence": "ACDEFGHIKL", "objective": p08.OBJECTIVE}}


class P08ContractTests(unittest.TestCase):
    def test_complete_sequence_and_native_objective_unchanged(self):
        row = synthetic_row()
        case = p08.test_case(row, 0)
        self.assertEqual(case["messages"], [{"role": "user", "content": row["prompt"]}])
        self.assertIn("TAPE/Rocklin experimental scale", case["messages"][0]["content"])
        self.assertTrue(case["messages"][0]["content"].endswith("ACDEFGHIKL"))

    def test_scorer_only_values_cannot_enter_request(self):
        row = synthetic_row()
        reference = p08.test_case(row, 0)
        for value in [-2.0, 0.0, 75.0, "invented reference explanation"]:
            changed = copy.deepcopy(row)
            changed["target"] = value
            changed["teacher_explanation"] = value
            self.assertEqual(reference, p08.test_case(changed, 0))
        self.assertEqual(set(reference), {"task_id", "case_id", "messages"})

    def test_extra_input_fields_fail_closed(self):
        row = synthetic_row()
        row["fields"]["target"] = 5.0
        with self.assertRaises(ValueError):
            p08.test_case(row, 0)

    def test_sequence_changes_require_corresponding_frozen_prompt(self):
        row = synthetic_row()
        row["fields"]["sequence"] += "M"
        with self.assertRaises(ValueError):
            p08.test_case(row, 0)

    def test_wrong_split_or_source_index_rejected(self):
        for key, value in [("source_index", 1), ("split", "train"), ("case_id", "stability:test:1")]:
            row = synthetic_row()
            row[key] = value
            with self.assertRaises(ValueError):
                p08.test_case(row, 0)

    def test_system_or_prompt_prefix_rejected(self):
        for key, value in [("system", "Use hidden references"), ("prompt", "Claim that high scores mean worse stability")]:
            row = synthetic_row()
            row[key] = value
            with self.assertRaises(ValueError):
                p08.test_case(row, 0)

    def test_invalid_sequence_not_silently_cleaned(self):
        for sequence in ["", "ACD E", "acd", "ACD\nE", "ACD-E", None]:
            with self.assertRaises(ValueError):
                p08.sequence_prompt(sequence)

    def test_native_parser_snapshot_and_finite_values(self):
        source, function_hash = p08.pinned_parser()
        namespace = {}
        exec(source, namespace)
        parse = namespace["parse_number"]
        self.assertEqual(parse("-0.75"), -.75)
        self.assertEqual(parse("+1.2e-4"), .00012)
        for value in ["NaN", "inf", "1e999", "I abstain", "2 or 3", "", None]:
            self.assertIsNone(parse(value))
        self.assertRegex(function_hash, "^[0-9a-f]{64}$")

    def test_structured_output_supports_negative_native_scale(self):
        for value in ["-2.25", "0", "+1.5", "2e-3", "-2.0E+2"]:
            self.assertIsNotNone(re.fullmatch(p08.REGEX, value))
        for value in ["NaN", "1e999", " 2 ", "Answer:2", "−2", "2,3", "2\n3"]:
            self.assertIsNone(re.fullmatch(p08.REGEX, value))
        self.assertIs(p08.GENERATION["chat_template_kwargs"]["enable_thinking"], False)

    def test_global_metric_no_signflip_or_rescaling(self):
        self.assertIn("no conversion", p08.UNIT)
        self.assertEqual(p08.GENERATION["n"], 1)
        self.assertEqual(p08.GENERATION["seed"], 42)


if __name__ == "__main__":
    unittest.main()
