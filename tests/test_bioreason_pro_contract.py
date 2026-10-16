"""Synthetic input/gold boundaries, generated-channel extraction and native CAFA."""
import contextlib
import copy
import io
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import bioreason_pro_contract as protocol
import run_local_labbench_multimodal as runner
import score_local_bioreason_pro as scorer


def row(identity="artificial"):
    return {"protein_id": identity, "sequence": "MAGZX", "length": 5, "organism": "Synthetic organism",
            "interpro_formatted": "Synthetic domain input", "ppi_formatted": "Synthetic partner input",
            "go_pred": "Synthetic predictor speculation GO:9999999"}


def tiny_ontology(folder):
    obo, ia = folder / "ontology.obo", folder / "ia.tsv"
    obo.write_text("format-version: 1.2\n\n" + "\n\n".join(
        "[Term]\nid: " + term + "\nname: synthetic\nnamespace: " + namespace + ("\nis_a: " + parent if parent else "")
        for term, namespace, parent in [("GO:0008150", "biological_process", None),
            ("GO:0000001", "biological_process", "GO:0008150"), ("GO:0000002", "biological_process", "GO:0000001"),
            ("GO:0003674", "molecular_function", None), ("GO:0000003", "molecular_function", "GO:0003674")]) + "\n")
    ia.write_text("GO:0008150\t0\nGO:0000001\t1\nGO:0000002\t3\nGO:0003674\t0\nGO:0000003\t2\n")
    return obo, ia


class BioReasonProTests(unittest.TestCase):
    def test_exact_native_context_and_full_sequence_no_gold(self):
        source = row()
        case = protocol.model_case(0, source)
        prompt = case["messages"][0]["content"]
        for key in ("sequence", "organism", "interpro_formatted", "ppi_formatted", "go_pred"):
            self.assertIn(source[key], prompt)
        self.assertIn("Molecular Function, Biological Process, Cellular Component", prompt)
        self.assertIn("Summarize in UniProt format.", prompt)
        for key in ("go_mf", "go_cc", "go_bp", "protein_function", "reasoning", "protein_names"):
            with self.assertRaisesRegex(ValueError, "allowlist"):
                protocol.model_case(0, {**source, key: "SECRET_GOLD"})
        long = {**source, "sequence": "M" * 10986, "length": 10986}
        self.assertIn(long["sequence"], protocol.model_case(0, long)["messages"][0]["content"])

    def test_native_fixed_flags_are_label_independent(self):
        native = protocol.native_formatter()
        kwargs = dict(go_gpt_predictions_column="go_pred", interpro_in_prompt=True, ppi_in_prompt=True,
                      add_uniprot_summary=True, ask_all_go_aspects=True, force_uniprot_summary=True)
        one = native(row(), **kwargs)["prompt"]
        two = native({**row(), "go_bp": ["GO:0000001"], "go_cc": ["GO:0000003"], "protein_function": "SECRET_GOLD", "reasoning": "SECRET_TEACHER"}, **kwargs)["prompt"]
        self.assertEqual((one["system"], one["user"]), (two["system"], two["user"]))
        self.assertNotIn("SECRET", one["system"] + one["user"])

    def test_generated_continuation_never_includes_prompt_or_teacher(self):
        response = {"http_status": 200, "input_prompt": "GO:1111111", "teacher_reasoning": "GO:2222222",
            "text": "Final GO:0000003", "finish_reason": "stop", "response": {"choices": [{"message": {
                "reasoning": "Generated hypothesis GO:0000001", "content": "Final GO:0000003"}, "finish_reason": "stop"}]}}
        continuation, final, reasoning = protocol.generated_continuation(response)
        self.assertEqual(protocol.extract_go(continuation), {"GO:0000001", "GO:0000003"})
        self.assertEqual(protocol.extract_go(final), {"GO:0000003"})
        response["response"]["choices"][0]["message"]["reasoning_content"] = "conflicting"
        with self.assertRaisesRegex(ValueError, "Conflicting"):
            protocol.generated_continuation(response)

    def test_official_native_hierarchy_ia_and_missing_aspect(self):
        with tempfile.TemporaryDirectory() as tmp:
            folder = Path(tmp); obo, ia = tiny_ontology(folder)
            references = [{"case_id": "one", "target_aspects": {"BP": ["GO:0000002"], "MF": [], "CC": []}},
                          {"case_id": "two", "target_aspects": {"BP": ["GO:0000002"], "MF": ["GO:0000003"], "CC": []}}]
            with patch.object(protocol, "ONTOLOGY", obo), patch.object(protocol, "IA", ia):
                metrics, contract = protocol.native_metrics({"one": {"GO:0000001"}, "two": set()}, references, folder / "metric")
                empty, _ = protocol.native_metrics({"one": set(), "two": set()}, references, folder / "empty")
            self.assertAlmostEqual(metrics["BP_Fmax"], .5)
            self.assertAlmostEqual(metrics["BP_IA_weighted_Fmax"], 2 / 9)
            self.assertEqual(metrics["MF_Fmax"], 0)
            self.assertEqual(empty["BP_Fmax"], 0)
            self.assertEqual(empty["MF_IA_weighted_Fmax"], 0)
            self.assertEqual(contract["native_ontology_eligible_counts_by_aspect"], {"BP": 2, "MF": 1, "CC": 0})
            # Same pinned original top-level CAFA implementation agrees whenever
            # predictions are present; absent-prediction MF is explicitly kept0.
            from cafaeval.evaluation import cafa_eval
            pred_dir = folder / "pred_dir"; pred_dir.mkdir()
            (pred_dir / "pred.tsv").write_bytes((folder / "metric/predictions.tsv").read_bytes())
            official, _ = cafa_eval(str(obo), str(pred_dir), str(folder / "metric/ground_truth.tsv"), str(ia), th_step=.99)
            bp = official.reset_index().query("ns == 'biological_process'").iloc[0]
            self.assertEqual(float(bp["f"]), metrics["BP_Fmax"])
            self.assertEqual(float(bp["f_w"]), metrics["BP_IA_weighted_Fmax"])

    def test_scorer_locks_before_labels_and_retains_missing_row(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp); folder = root / "results/runs/artificial"; folder.mkdir(parents=True)
            cases = [protocol.model_case(i, row(str(i))) for i in range(2)]
            refs = [{"task": "P28", "case_id": case["case_id"], "target_aspects": {"BP": ["GO:0000002"], "MF": [], "CC": []}} for case in cases]
            for name, values in (("inputs.jsonl", cases), ("refs.jsonl", refs)):
                (root / name).write_text("".join(json.dumps(value) + "\n" for value in values))
            protocol.save(root / "review.json", {"approved_case_ids": [case["case_id"] for case in cases], "held_cases": []})
            generation = {"max_tokens": 4096, "temperature": 1., "top_p": .95, "top_k": 20, "seed": 42, "n": 1,
                          "chat_template_kwargs": {"enable_thinking": True, "reasoning_effort": "medium"}}
            cfg = {"run_id": "artificial", "approved_task_ids": ["P28"], "variant": protocol.VARIANT, "model": "synthetic", "model_revision": "fake",
                "generation": generation, "model_facing_fields": ["sequence", "native_context"], "input_file": "inputs.jsonl", "review_file": "review.json",
                "scorer_reference_file": "refs.jsonl", "scorer_reference_sha256": protocol.file_sha(root / "refs.jsonl"), "frozen_files_sha256": {}, "paper_comparison": "Synthetic only"}
            protocol.save(folder / "run_manifest.json", {"configuration": cfg, "case_contract_sha256": protocol.digest(cases), "planned_cases": 2})
            case = cases[0]; identity = protocol.digest([case["task"], case["variant"], case["case_id"]]) + ".json"
            request = runner.request_record(case, cfg); protocol.save(folder / "requests" / identity, request)
            api = {"model": "synthetic", "choices": [{"message": {"reasoning": "Generated GO:0000001", "content": ""}, "finish_reason": "length"}]}
            response = {**{key: case[key] for key in ("task", "case_id", "variant", "split")}, "model": "synthetic", "model_revision": "fake",
                "request_sha256": request["request_sha256"], "status": "completed", "http_status": 200, "text": "", "finish_reason": "length", "response": api}
            protocol.save(folder / "responses" / identity, response)
            native = protocol.native_metrics
            obo, ia = tiny_ontology(root)
            def metric(predictions, references, destination):
                self.assertTrue((folder / "scoring_output_lock.json").exists())
                with patch.object(protocol, "ONTOLOGY", obo), patch.object(protocol, "IA", ia):
                    return native(predictions, references, destination)
            read = Path.read_bytes
            def check_read(path):
                if path == root / "refs.jsonl": self.assertTrue((folder / "scoring_output_lock.json").exists())
                return read(path)
            with patch.object(scorer, "ROOT", root), patch.object(protocol, "native_metrics", metric), patch.object(Path, "read_bytes", check_read), contextlib.redirect_stdout(io.StringIO()):
                summary = scorer.score(folder)
            self.assertEqual((summary["planned"], summary["completed"], summary["missing_or_failed_outputs"], summary["truncated_outputs"]), (2, 1, 1, 1))
            self.assertAlmostEqual(summary["metrics"]["BP_Fmax"], .5)
            self.assertIsNone(summary["explanation_support_score"])


if __name__ == "__main__":
    unittest.main()
