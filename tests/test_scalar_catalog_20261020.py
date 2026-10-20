"""Synthetic-only checks for scalar delivery, leakage guards and one-attempt I/O."""
import argparse
import hashlib
import importlib.util
import io
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import run_scalar_catalog_20261020 as runner
import prepare_p06_fresh_20261020 as p06


def native(text):
    try:
        value = float(text)
        return value if __import__("math").isfinite(value) else None
    except (ValueError, TypeError):
        return None


def response(text="52.25", finish="stop", **extra):
    return {"choices": [{"finish_reason": finish, "message": {"content": text, **extra}}],
            "usage": {"prompt_tokens": 50, "completion_tokens": 4}}


class DeliveryTests(unittest.TestCase):
    def test_finite_scalar_sign_decimal_exponent(self):
        for text in ["0", "-7.5", "+12", "999999999999.123456789012e+99"]:
            self.assertTrue(runner.parse_delivery(response(text), native)["delivery_passed"])

    def test_ambiguous_extra_text_invalid(self):
        for text in ["", " 42 ", "Answer:42", "42 degrees", "4 2", "NaN", "Infinity", "1e999", "1." , ".5", "1\n2"]:
            self.assertFalse(runner.parse_delivery(response(text), native)["delivery_passed"])

    def test_truncated_number_remains_invalid(self):
        result = runner.parse_delivery(response("52", "length"), native)
        self.assertFalse(result["delivery_passed"])
        self.assertTrue(result["truncated"])

    def test_reasoning_and_refusal_cannot_pass(self):
        for extra in [{"reasoning": "hidden argument"}, {"reasoning_content": "argument"},
                      {"refusal": "refuse"}, {"tool_calls": [{"id": "tool"}]}]:
            self.assertFalse(runner.parse_delivery(response(**extra), native)["delivery_passed"])

    def test_native_parser_must_accept(self):
        self.assertFalse(runner.parse_delivery(response(), lambda _: None)["delivery_passed"])

    def test_multiple_choices_rejected(self):
        body = response(); body["choices"] *= 2
        with self.assertRaises(ValueError):
            runner.parse_delivery(body, native)


class InputTests(unittest.TestCase):
    def test_p06_targets_do_not_affect_requests_or_dev_selection(self):
        rows = [{"sequence": "ACDEFGHIKL"*(i+1), "target": "SECRET_TARGET", "set": "train", "validation": "True"} for i in range(32)]
        before = p06.select_development(rows)
        requests = [p06.input_row(i, row) for i, row in enumerate(rows)]
        for row in rows:
            row["target"] = "REPLACED_SECRET"
        self.assertEqual(before, p06.select_development(rows))
        self.assertEqual(requests, [p06.input_row(i, row) for i, row in enumerate(rows)])
        self.assertNotIn("SECRET", json.dumps(requests))

    def test_full_sequence_is_retained(self):
        sequence = "ACDEFGHIKLMNPQRSTVWY"*2000
        request = p06.input_row(7, {"sequence": sequence})
        self.assertTrue(request["messages"][0]["content"].endswith(sequence))
        self.assertEqual(request["messages"][0]["content"].count(sequence), 1)

    def test_unreviewed_nonsequence_text_is_rejected(self):
        with self.assertRaises(ValueError):
            p06.input_row(0, {"sequence": "ABC heldout=42"})


class PipelineTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.base = Path(self.temp.name)
        self.parser = self.base/"parser.py"
        self.parser.write_text("import math\ndef parse_number(text):\n try:\n  value=float(text)\n  return value if math.isfinite(value) else None\n except (TypeError,ValueError): return None\n")
        self.cases = [{"task_id": "P06", "case_id": "toy:1", "messages": [{"role": "user", "content": "Toy arithmetic: 50+2.25. Return a number."}]}]
        self.inputs = self.base/"inputs.jsonl"
        self.inputs.write_text(json.dumps(self.cases[0])+"\n")
        self.review = self.base/"review.json"
        self.review.write_text(json.dumps({"task_id": "P06", "approved_case_ids": ["toy:1"]}))
        self.config = {"schema_version": 1, "task_id": "P06", "run_id": "toy-development", "protocol_variant": "toy",
                       "model": runner.MODEL, "model_revision": runner.REVISION,
                       "input_file": str(self.inputs), "input_sha256": runner.sha(self.inputs),
                       "review_file": str(self.review), "review_sha256": runner.sha(self.review),
                       "native_numeric_parser_file": str(self.parser), "native_numeric_parser_sha256": runner.sha(self.parser),
                       "native_numeric_parser_function": "parse_number", "files_sha256": {},
                       "planned": 1, "split": "official_validation", "generation": runner.GENERATION}
        self.config_path = self.base/"config.json"
        self.write_config()
        self.identity = self.base/"identity.json"
        self.identity.write_text(json.dumps({"model": runner.MODEL,"revision": runner.REVISION,"dtype":"bfloat16"}))
        self.grant = self.base/"grant.json"
        self.grant.write_text(json.dumps({"authorized": True, "task_id":"P06","run_id":"toy-development",
              "config_sha256":runner.sha(self.config_path),"endpoint":"http://127.0.0.1:1234/v1",
              "server_identity_file":str(self.identity),"server_identity_sha256":runner.sha(self.identity)}))

    def tearDown(self):
        self.temp.cleanup()

    def write_config(self):
        self.config_path.write_text(json.dumps(self.config))

    def args(self):
        return argparse.Namespace(config=self.config_path, output=self.base/"run", grant=self.grant,
             development_completion=None, model_path="unused", context_limit=65536, concurrency=1,
             timeout=1, resume_unattempted=False, check_only=False)

    def test_label_field_in_solver_record_is_rejected(self):
        self.cases[0]["target"] = 99
        self.inputs.write_text(json.dumps(self.cases[0])+"\n")
        self.config["input_sha256"] = runner.sha(self.inputs); self.write_config()
        with self.assertRaises(ValueError): runner.load_contract(self.config_path)

    def test_mutated_frozen_input_rejected(self):
        self.inputs.write_text("{}\n")
        with self.assertRaises(ValueError): runner.load_contract(self.config_path)

    def test_altered_sampling_rejected(self):
        self.config["generation"] = {**runner.GENERATION,"max_tokens": 4096}; self.write_config()
        with self.assertRaises(ValueError): runner.load_contract(self.config_path)

    def test_unapproved_endpoint_rejected(self):
        grant=json.loads(self.grant.read_text());grant["endpoint"]="https://api.example.com/v1";self.grant.write_text(json.dumps(grant))
        with self.assertRaises(ValueError): runner.validate_grant(self.grant,self.config_path,self.config)

    def test_full_test_requires_task_development_gate(self):
        config={**self.config,"split":"official_test","development_config_sha256":"missing"}
        with self.assertRaises(ValueError): runner.validate_development(config,None)

    def test_unknown_phase_cannot_bypass_development_gate(self):
        self.config["split"]="official_released_test";self.write_config()
        with self.assertRaises(ValueError):runner.load_contract(self.config_path)

    def test_held_case_cannot_enter_solver_cohort(self):
        self.review.write_text(json.dumps({"task_id":"P06","approved_case_ids":["toy:1"],"held_cases":[{"case_id":"toy:1"}]}))
        self.config["review_sha256"]=runner.sha(self.review);self.write_config()
        with self.assertRaises(ValueError):runner.load_contract(self.config_path)

    def test_end_to_end_mocked_output_lock_and_no_retry(self):
        calls=[]
        class Opener:
            def open(inner, request, **kwargs):
                calls.append(request)
                if isinstance(request,str):return io.BytesIO(json.dumps({"data":[{"id":runner.MODEL}]}).encode())
                return io.BytesIO(json.dumps(response()).encode())
        with patch.object(runner.urllib.request,"build_opener",return_value=Opener()),patch.object(runner,"count_tokens",return_value={"counts":[{"case_id":"toy:1","prompt_tokens":12}]}):
            runner.run(self.args())
            self.assertEqual(len(calls),2)
            done=json.loads((self.base/"run/completion.json").read_text())
            self.assertTrue(done["delivery_passed_all"])
            self.assertFalse(done["biological_correctness_assessed"])
            self.assertEqual(done["responses_saved"],1)
            runner.validate_development({**self.config,"split":"official_test","development_config_sha256":runner.sha(self.config_path)},self.base/"run/completion.json")
            with self.assertRaises(ValueError):runner.run(self.args())
            self.assertEqual(len(calls),2)
            request_path=next((self.base/"run/requests").iterdir())
            request_path.write_text("changed")
            with self.assertRaises(ValueError):runner.validate_development({**self.config,"split":"official_test","development_config_sha256":runner.sha(self.config_path)},self.base/"run/completion.json")


if __name__ == "__main__":
    unittest.main()
