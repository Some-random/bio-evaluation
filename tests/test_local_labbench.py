import ast
import copy
import importlib.util
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import run_local_labbench as runner
import score_local_labbench as scoring


class LocalEvaluationContractTests(unittest.TestCase):
    def setUp(self):
        self.settings = {"model": "synthetic-model", "approved_task_ids": ["B01"], "variant": "SYNTHETIC",
                         "generation": {"max_tokens": 100, "temperature": 1, "top_p": .95,
                                        "top_k": 20, "seed": 42, "n": 1,
                                        "chat_template_kwargs": {"enable_thinking": True, "reasoning_effort": "medium"}}}
        self.case = {"task": "B01", "case_id": "synthetic-1", "variant": "SYNTHETIC", "split": "synthetic",
                     "messages": [{"role": "user", "content": "Synthetic question\n(A) one\n(B) two"}]}

    def test_labels_and_unreviewed_tasks_fail_before_dispatch(self):
        bad = copy.deepcopy(self.case)
        bad["target_choice"] = "A"
        with self.assertRaises(ValueError):
            runner.payload_for(bad, self.settings)
        bad = copy.deepcopy(self.case)
        bad["task"] = "P18"
        with self.assertRaises(ValueError):
            runner.payload_for(bad, self.settings)

    def test_only_original_message_and_generation_fields_reach_model(self):
        payload = runner.payload_for(self.case, self.settings)
        self.assertEqual(payload["messages"], self.case["messages"])
        self.assertNotIn("case_id", payload)
        self.assertNotIn("tools", payload)
        self.assertNotIn("api_key", payload)

    def test_provider_urls_and_credential_urls_rejected(self):
        runner.validate_endpoint("http://127.0.0.1:8026/v1")
        for endpoint in ["https://api.openai.com/v1", "http://user:key@127.0.0.1:8026/v1",
                         "http://127.0.0.1:8026/v1?target=remote", "http://127.0.0.1:8027/v1"]:
            with self.assertRaises(ValueError):
                runner.validate_endpoint(endpoint)

    def test_review_allowlist_rejects_held_duplicate_and_reordered_cases(self):
        review = {"approved_case_ids": ["synthetic-1"], "held_cases": []}
        runner.validate_cases([self.case], self.settings, review)
        review["held_cases"] = [{"case_id": "synthetic-1"}]
        with self.assertRaises(ValueError):
            runner.validate_cases([self.case], self.settings, review)
        with self.assertRaises(ValueError):
            runner.validate_cases([self.case, self.case], self.settings, review)

    def test_tool_and_multiple_completion_settings_rejected(self):
        for key, value in [("tools", []), ("n", 2)]:
            settings = copy.deepcopy(self.settings)
            settings["generation"][key] = value
            with self.assertRaises(ValueError):
                runner.payload_for(self.case, settings)

    def test_metrics_match_pinned_official_function(self):
        tree = ast.parse((ROOT / "sources/lab__labbench__evaluator.py").read_text())
        cls = next(n for n in tree.body if isinstance(n, ast.ClassDef) and n.name == "Evaluator")
        function = copy.deepcopy(next(n for n in cls.body if isinstance(n, ast.FunctionDef) and n.name == "compute_metrics"))
        function.decorator_list = []
        namespace = {}
        exec(compile(ast.fix_missing_locations(ast.Module(body=[function], type_ignores=[])), "native-metrics", "exec"), namespace)
        native = namespace["compute_metrics"]
        groups = [[], [{"correct": True, "sure": True}],
                  [{"correct": True, "sure": True}, {"correct": False, "sure": False},
                   {"correct": False, "sure": True}]]
        for rows in groups:
            ours = scoring.metrics_for(rows)
            self.assertEqual({k: ours[k] for k in native(rows)}, native(rows))

    def test_invalid_output_is_not_abstention(self):
        answer = scoring.lab_answer("An answer without the required tag or letter.", 5)
        self.assertIsNone(answer)
        values = scoring.metrics_for([{"correct": answer == "A", "sure": answer != "B"}])
        self.assertEqual(values["coverage"], 1)
        self.assertEqual(values["accuracy"], 0)


if __name__ == "__main__":
    unittest.main()
