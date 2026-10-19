import importlib.util
import json
from pathlib import Path
import tempfile
import unittest


SPEC = importlib.util.spec_from_file_location("request_identity", Path(__file__).resolve().parents[1] / "scripts/openai_request_identity.py")
identity = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(identity)


class StableIdentityTests(unittest.TestCase):
    def test_same_principal_across_tasks_without_mutating_original_payload(self):
        for task in ["toy_numeric", "toy_choice", "toy_json"]:
            original = {"input": task, "metadata": {"task": task}}
            actual = identity.with_safety_identifier(original, "stable-user-123")
            self.assertEqual(actual["safety_identifier"], "stable-user-123")
            self.assertNotIn("safety_identifier", original)

    def test_identity_switch_rejected(self):
        with self.assertRaises(ValueError):
            identity.with_safety_identifier({"safety_identifier": "other-user"}, "stable-user-123")

    def test_invalid_or_missing_config_fails_without_generating_a_replacement(self):
        with tempfile.TemporaryDirectory() as temp:
            p = Path(temp) / "identity.json"
            with self.assertRaises(FileNotFoundError):
                identity.load_safety_identifier(p)
            for value in [None, "", "x" * 129, "a\nb"]:
                p.write_text(json.dumps({"schema_version": 1, "safety_identifier": value}))
                with self.assertRaises(ValueError):
                    identity.load_safety_identifier(p)

    def test_config_reused_exactly(self):
        with tempfile.TemporaryDirectory() as temp:
            p = Path(temp) / "identity.json"
            p.write_text(json.dumps({"schema_version": 1, "safety_identifier": "stable-user-123"}))
            self.assertEqual(identity.load_safety_identifier(p), identity.load_safety_identifier(p))


if __name__ == "__main__":
    unittest.main()
