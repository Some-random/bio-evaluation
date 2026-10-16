"""Synthetic-only protocol tests. No real gold sequences or inference."""
import copy
import json
from pathlib import Path
import shutil
import tempfile
import unittest
from unittest import mock

import p36_contract as contract
import prepare_p36
import run_p36
import score_p36


class ProtocolTests(unittest.TestCase):
    def test_target_never_enters_source_prompt(self):
        instance = {"instruction": "Perform a synthetic string task", "input": "VISIBLE INPUT", "output": ["SECRET GOLD"]}
        prompt = prepare_p36.transform(instance, {"prompt_input": "{instruction}\n{input}"})
        self.assertEqual(prompt, "Perform a synthetic string task\nVISIBLE INPUT")
        self.assertNotIn("SECRET", prompt)
        changed = copy.deepcopy(instance)
        changed["output"] = ["ANOTHER SECRET"]
        self.assertEqual(prompt, prepare_p36.transform(changed, {"prompt_input": "{instruction}\n{input}"}))

    def test_exact_paired_reference_source_behavior(self):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "output.tsv"
            paired = contract.paired_rouge(["context words"], [["different gold", "context words"]], path)
            gold_only_equivalent = contract.paired_rouge(["context words"], [["different gold", "different gold"]], path)
            self.assertEqual(paired["rougeL"], 1.0)
            self.assertEqual(gold_only_equivalent["rougeL"], 0.0)

    def test_serialization_overlap_is_not_residue_alignment(self):
        with tempfile.TemporaryDirectory() as temp:
            result = contract.paired_rouge(["<bop><p>A<p>A<eop>"], [["<bop><p>W<p>W<eop>", ""]], Path(temp) / "output.tsv")
            self.assertGreater(result["rougeL"], 0.0)
            self.assertTrue(contract.serialization_diagnostic("<bop><p>A<eop>")["valid_native_protein_serialization"])
            self.assertFalse(contract.serialization_diagnostic(" <bop><p>A<eop>")["valid_native_protein_serialization"])

    def test_no_approval_means_no_network(self):
        with tempfile.TemporaryDirectory() as temp:
            temp = Path(temp)
            config, approval = temp / "config.json", temp / "approval.json"
            contract.write_json(config, {})
            contract.write_json(approval, {"execution_authorized": False})
            with mock.patch("urllib.request.urlopen") as network:
                with self.assertRaisesRegex(ValueError, "execution approval"):
                    run_p36.execute(config, approval, "http://127.0.0.1:8026/v1", temp / "run")
                network.assert_not_called()

    def synthetic_fixture(self, root):
        (root / "sources").mkdir()
        for name in ["hf_rouge_pinned.py", "biot5_plus__metrics__pro_understand_metrics__pro_understand_metrics.py"]:
            shutil.copyfile(contract.ROOT / "sources" / name, root / "sources" / name)
        cases = [{"task": "P36", "case_id": "SYNTHETIC:" + str(i), "variant": contract.VARIANT, "split": "synthetic",
                  "messages": [{"role": "system", "content": contract.FORMAT}, {"role": "user", "content": "synthetic input"}]}
                 for i in range(2)]
        (root / "inputs.jsonl").write_text("".join(json.dumps(x) + "\n" for x in cases))
        refs = [{"case_id": x["case_id"], "target": "alpha beta", "source_prompt": "unrelated context"} for x in cases]
        (root / "refs.jsonl").write_text("".join(json.dumps(x) + "\n" for x in refs))
        contract.write_json(root / "review.json", {"approved_case_ids": [x["case_id"] for x in cases],
                           "held_cases": [], "full_source_case_count": 5876})
        config = {"model": contract.MODEL, "model_revision": contract.REVISION, "generation": contract.GENERATION,
                  "variant": contract.VARIANT, "input_file": "inputs.jsonl", "review_file": "review.json",
                  "frozen_files_sha256": {}, "case_contract_sha256": contract.digest(cases),
                  "scorer_reference_file": "refs.jsonl", "scorer_reference_sha256": contract.file_digest(root / "refs.jsonl"),
                  "metric_contract": {"synthetic": True}, "comparison_qualification": "Synthetic only"}
        run = root / "run"
        run.mkdir()
        contract.write_json(run / "run_manifest.json", {"configuration": config, "case_contract_sha256": contract.digest(cases)})
        case = cases[0]
        identity = contract.digest([case["task"], case["variant"], case["case_id"]])
        body = contract.payload(case, config)
        provenance = {"task": "P36", "case_id": case["case_id"], "variant": case["variant"], "model": contract.MODEL,
                      "model_revision": contract.REVISION, "request_sha256": contract.digest(body)}
        contract.write_json(run / "requests" / (identity + ".json"), {**provenance, "payload": body})
        contract.write_json(run / "responses" / (identity + ".json"), {**provenance, "status": "completed", "text": "alpha beta",
                            "finish_reason": "length", "response": {"choices": [{"message": {"content": "alpha beta"}}]}})
        return run, identity

    def test_missing_slots_retained_and_invalid_raw_content_not_repaired(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            run, _ = self.synthetic_fixture(root)
            with mock.patch.object(contract, "ROOT", root), mock.patch.object(score_p36, "ROOT", root):
                result = score_p36.score(run)
            self.assertEqual(result["planned"], 2)
            self.assertEqual(result["completed"], 1)
            self.assertEqual(result["missing_or_failed_slots"], 1)
            self.assertEqual(result["valid_native_serializations"], 0)
            self.assertEqual(result["metrics"]["rougeL"], 0.5)
            self.assertFalse(result["full_benchmark_complete"])
            self.assertEqual(result["finish_reasons"], {"length": 1})

    def test_output_lock_rejects_mutated_outputs(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            run, identity = self.synthetic_fixture(root)
            with mock.patch.object(contract, "ROOT", root), mock.patch.object(score_p36, "ROOT", root):
                score_p36.score(run)
                response_path = run / "responses" / (identity + ".json")
                response = json.loads(response_path.read_text())
                response["text"] = "changed output"
                response["response"]["choices"][0]["message"]["content"] = "changed output"
                contract.write_json(response_path, response)
                with self.assertRaisesRegex(ValueError, "Outputs changed"):
                    score_p36.score(run)


if __name__ == "__main__":
    unittest.main()
