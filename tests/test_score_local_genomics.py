import importlib.util
import json
from pathlib import Path
import shutil
import tempfile
import unittest
from unittest.mock import patch


SCRIPT = Path(__file__).resolve().parents[1] / "scripts/score_local_genomics.py"
spec = importlib.util.spec_from_file_location("score_local_genomics", SCRIPT)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)


def saved_response(final, reasoning=None):
    message = {"role": "assistant", "content": final}
    if reasoning is not None:
        message["reasoning"] = reasoning
    return {"text": final, "response": {"model": "SyntheticModel", "choices": [{"message": message}]}}


class GenomicNativeMetricTests(unittest.TestCase):
    def test_reasoning_is_native_continuation_but_never_strict_final(self):
        first, final1, _ = mod.continuation_fields(saved_response("Answer: benign", "Pathogenic considered."))
        second, final2, _ = mod.continuation_fields(saved_response("Answer: pathogenic", "Benign considered."))
        metrics, details, _, _ = mod.outcome_metrics("N02", ["pathogenic", "benign"], [first, second], [final1, final2], ["benign", "pathogenic"])
        self.assertEqual(metrics["accuracy"], 1.0)
        self.assertEqual(metrics["f1"], 1.0)
        self.assertEqual(metrics["STRICT_FINAL_LABEL"]["accuracy"], 0.0)
        self.assertEqual(details["native_ambiguous_completed"], 2)

    def test_exact_native_last_marker_and_fixed_global_macro(self):
        labels = ["synthetic disease a", "synthetic disease a"]
        vocabulary = ["synthetic disease a", "synthetic disease b", "synthetic absent class"]
        metrics, _, predictions, correct = mod.outcome_metrics("N01", labels,
            ["Answer: synthetic disease b.\nAnswer: Synthetic disease a!", "synthetic disease a"],
            ["Answer: Synthetic disease a!", "synthetic disease a"], vocabulary)
        self.assertEqual(correct, [True, False])
        self.assertEqual(metrics["accuracy"], 0.5)
        self.assertEqual(predictions, labels)
        self.assertAlmostEqual(metrics["STRICT_FINAL_LABEL"]["supplemental_macro_f1_fixed_global_vocabulary"], 1 / 3)
        self.assertEqual(mod.native_n01_answer("answer: synthetic disease a"), "")

    def test_missing_invalid_and_native_substring_oddity_are_explicit(self):
        metrics, details, parsed, correct = mod.outcome_metrics("N03", ["pathogenic", "benign", "pathogenic"],
            ["nonpathogenic", None, "benign and pathogenic"], ["nonpathogenic", None, "benign and pathogenic"], ["benign", "pathogenic"])
        self.assertEqual(correct, [True, False, True])
        self.assertEqual(metrics["accuracy"], 2 / 3)
        self.assertEqual(parsed, [None, None, None])
        self.assertEqual(details["strict_invalid_completed"], 2)
        self.assertEqual(details["missing_or_failed"], 1)

    def test_saved_field_conflicts_cannot_be_selected_away(self):
        response = saved_response("benign", "one")
        response["response"]["choices"][0]["message"]["reasoning_content"] = "two"
        with self.assertRaisesRegex(ValueError, "Ambiguous"):
            mod.continuation_fields(response)
        response = saved_response("benign")
        response["text"] = "pathogenic"
        with self.assertRaisesRegex(ValueError, "differs"):
            mod.continuation_fields(response)


class GenomicScoringArchiveTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.folder = self.root / "results/runs/synthetic_run"
        self.folder.mkdir(parents=True)
        (self.root / "scripts").mkdir()
        shutil.copyfile(SCRIPT, self.root / "scripts/score_local_genomics.py")
        (self.root / "scripts/synthetic_runner.py").write_text("# Synthetic fixture, never executed.\n")
        self.cases = [{"task": "N02", "case_id": f"synthetic_{i}", "variant": "SYNTHETIC", "split": "test",
                       "messages": [{"role": "user", "content": "Synthetic DNA AAAA. Classify benign or pathogenic."}]} for i in range(2)]
        self.write("inputs.jsonl", self.cases, jsonl=True)
        self.write("review.json", {"approved_case_ids": [c["case_id"] for c in self.cases], "held_cases": [], "input_review_only": True})
        self.write("vocabulary.json", {"classes": ["benign", "pathogenic"]})
        self.write("references.jsonl", [{"task": "N02", "case_id": case["case_id"], "source_answer": label,
                                        "normalized_label": label, "scorer_only": True} for case, label in zip(self.cases, ["pathogenic", "benign"])], jsonl=True)
        self.settings = {"run_id": "synthetic_run", "approved_task_ids": ["N02"], "variant": "SYNTHETIC",
                         "model": "SyntheticModel", "model_revision": "pinned-synthetic", "generation": {"n": 1, "max_tokens": 4096},
                         "input_file": "inputs.jsonl", "review_file": "review.json", "class_vocabulary_file": "vocabulary.json",
                         "scorer_reference_file": "references.jsonl", "scorer_reference_sha256": mod.file_digest(self.root / "references.jsonl"),
                         "runner": "scripts/synthetic_runner.py"}
        files = ["scripts/score_local_genomics.py", "scripts/synthetic_runner.py", "inputs.jsonl", "review.json", "vocabulary.json"]
        self.settings["frozen_files_sha256"] = {name: mod.file_digest(self.root / name) for name in files}
        self.config = self.root / "configs/synthetic.json"
        self.config.parent.mkdir()
        self.config.write_text(json.dumps(self.settings))
        manifest = {"configuration": self.settings, "configuration_sha256": mod.file_digest(self.config),
                    "runner_sha256": mod.file_digest(self.root / self.settings["runner"]),
                    "case_contract_sha256": mod.digest(self.cases), "planned_cases": len(self.cases),
                    "server": {"model": "SyntheticModel", "revision": "pinned-synthetic"}}
        self.write("results/runs/synthetic_run/run_manifest.json", manifest)

    def write(self, name, value, jsonl=False):
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("".join(json.dumps(row) + "\n" for row in value) if jsonl else json.dumps(value))

    def archive(self, index, final, reasoning=None):
        case = self.cases[index]
        identity = mod.digest([case["task"], case["variant"], case["case_id"]])
        payload = mod.expected_payload(case, self.settings)
        request = {**{key: case[key] for key in ("task", "case_id", "variant", "split")}, "payload": payload, "request_sha256": mod.digest(payload)}
        self.write(f"results/runs/synthetic_run/requests/{identity}.json", request)
        response = {**{key: case[key] for key in ("task", "case_id", "variant", "split")}, **saved_response(final, reasoning),
                    "status": "completed", "http_status": 200, "model": "SyntheticModel", "model_revision": "pinned-synthetic",
                    "request_sha256": request["request_sha256"], "finish_reason": "stop"}
        self.write(f"results/runs/synthetic_run/responses/{identity}.json", response)
        return self.folder / "responses" / (identity + ".json")

    def test_outputs_locked_before_labels_and_prompt_is_never_prepended(self):
        self.archive(0, "Unresolved")
        original = mod.load_references

        def assert_lock_then_load(*args):
            self.assertTrue((self.folder / "scoring_output_lock.json").exists())
            return original(*args)

        with patch.object(mod, "load_references", side_effect=assert_lock_then_load):
            summary = mod.score(self.folder, root=self.root)
        self.assertEqual(summary["metrics"]["accuracy"], 0.0)
        self.assertEqual(summary["planned"], 2)
        self.assertEqual(summary["finished"], 1)
        self.assertEqual(summary["completed"], 1)
        self.assertEqual(summary["missing_or_failed_outputs"], 1)
        self.assertFalse(summary["native_decode_byte_equivalence_claimed"])
        self.assertEqual(summary["scorer_sha256"], mod.file_digest(SCRIPT))
        self.assertEqual(summary, mod.score(self.folder, root=self.root))

    def test_changed_response_cannot_replace_locked_generation(self):
        path = self.archive(0, "Answer: pathogenic")
        mod.score(self.folder, root=self.root)
        row = json.loads(path.read_text()); row["text"] = "Answer: benign"; path.write_text(json.dumps(row))
        with self.assertRaisesRegex(ValueError, "output lock changed"):
            mod.score(self.folder, root=self.root)

    def test_changed_config_reference_and_model_fail_before_label_loading(self):
        self.archive(0, "Answer: pathogenic")
        with patch.object(mod, "load_references", side_effect=AssertionError("Labels must not be read")):
            original = self.config.read_bytes(); self.config.write_text("{}")
            with self.assertRaisesRegex(ValueError, "config matches"):
                mod.score(self.folder, root=self.root)
            self.config.write_bytes(original)
            path = self.root / "references.jsonl"; original = path.read_bytes(); path.write_text("{}\n")
            with self.assertRaisesRegex(ValueError, "reference checksum"):
                mod.score(self.folder, root=self.root)
            path.write_bytes(original)
            manifest_path = self.folder / "run_manifest.json"; manifest = json.loads(manifest_path.read_text())
            manifest["server"]["revision"] = "wrong"; manifest_path.write_text(json.dumps(manifest))
            with self.assertRaisesRegex(ValueError, "Serving snapshot"):
                mod.score(self.folder, root=self.root)


if __name__ == "__main__":
    unittest.main()
