"""Synthetic P29 native prompt, augmented reference, ontology and gold boundary."""
import copy
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest import mock

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import posttrain_protein_contract as p
import score_local_posttrain_protein as scorer
from run_local_labbench_multimodal import request_record


class ContractTests(unittest.TestCase):
    def supplied(self):
        return {"protein_id": "SYN", "sequence": "ACDEFG", "length": "6.0", "organism": "Synthetic organism",
                "interpro_formatted": "Synthetic input domain", "go_pred": "Synthetic prior GO:9999999"}

    def test_exact_released_rl_prompt_full_sequence_and_input_only(self):
        row = self.supplied(); build, cfg = p.native_prompt_api(); case = p.model_case(0, "ood", row)
        source = {k: row[k] for k in ["sequence", "organism", "interpro_formatted", "go_pred"]}
        self.assertEqual(case["messages"][0]["content"], build(source, cfg))
        self.assertIn("Sequence: ACDEFG", case["messages"][0]["content"])
        self.assertNotIn("Protein name:", case["messages"][0]["content"])
        self.assertTrue(cfg.ask_all_go_aspects); self.assertFalse(cfg.ppi_in_prompt)
        for key in ["protein_names", "final_answer", "reasoning", "go_bp", "go_pred_leaf"]:
            with self.assertRaisesRegex(ValueError, "allowlist"):
                p.model_case(0, "ood", {**row, key: "GOLD_ONLY_SENTINEL"})

    def test_reference_augmentation_preserved_and_diagnostic_separate(self):
        row = {**self.supplied(), "go_ids": "GO:0000001", "go_pred_leaf": "GO:0000002", "reasoning": "GO:0000003",
               "final_answer": "GO:0000004", "protein_names": "GOLD_ONLY_SENTINEL"}
        ref = p.reference(0, "ood", row)
        self.assertEqual(ref["native_augmented_go_terms"], ["GO:0000001", "GO:0000002"])
        self.assertEqual(ref["curated_only_go_terms_diagnostic"], ["GO:0000001"])
        self.assertEqual(ref["predictor_go_terms_added_to_native_target"], ["GO:0000002"])

    def test_native_extractor_hierarchy_unknown_and_empty_score(self):
        api = p.native_api()
        text = "GO:0000009 <|GO_SUMMARY_START|>GO:0000002<|GO_SUMMARY_END|> Answer: GO:0000008"
        self.assertEqual(api.extract_go_ids_sft_aligned(text), {"GO:0000002"})
        ontology = api.GeneOntology({"GO:0000002": {"GO:0000001"}})
        self.assertEqual(ontology.propagate(["GO:9999999"]), {"GO:9999999"})
        ref = {"native_augmented_go_terms": ["GO:0000002"], "curated_only_go_terms_diagnostic": ["GO:0000001"]}
        metric = p.score_prediction({"GO:0000002"}, ref, ontology)
        self.assertEqual(metric["native_augmented_F1"], 1)
        self.assertAlmostEqual(metric["curated_only_F1_diagnostic"], 2 / 3)
        self.assertEqual(p.score_prediction(set(), ref, ontology)["native_augmented_F1"], 0)

    def test_generated_channels_exclude_prompt_and_preserve_native_summary(self):
        response = {"http_status": 200, "text": "<|GO_SUMMARY_START|>GO:0000002<|GO_SUMMARY_END|>", "finish_reason": "stop",
            "response": {"choices": [{"finish_reason": "stop", "message": {"reasoning": "Possible GO:0000001", "content": "<|GO_SUMMARY_START|>GO:0000002<|GO_SUMMARY_END|>"}}]}}
        continuation, _, _ = p.generated_continuation(response)
        self.assertEqual(p.native_api().extract_go_ids_sft_aligned(continuation), {"GO:0000002"})
        response["prompt"] = "INPUT_ONLY_GO:9999999"
        self.assertNotIn("9999999", p.generated_continuation(response)[0])

    def test_scorer_locks_every_output_before_gold_and_retains_missing(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary); folder = root / "run"; folder.mkdir()
            cases = [p.model_case(i, "ood", {**self.supplied(), "protein_id": "SYN" + str(i)}) for i in range(2)]
            p.save(root / "review.json", {"approved_case_ids": [c["case_id"] for c in cases], "held_cases": []})
            (root / "input.jsonl").write_text("".join(json.dumps(c) + "\n" for c in cases))
            references = [{"task": "P29", "case_id": c["case_id"], "native_split": "ood", "organism": "Synthetic organism",
                "native_augmented_go_terms": ["GO:0000001", "GO:0000002"], "curated_only_go_terms_diagnostic": ["GO:0000002"],
                "predictor_go_terms_added_to_native_target": ["GO:0000001"]} for c in cases]
            ref_path = root / "refs.jsonl"; ref_path.write_text("".join(json.dumps(r) + "\n" for r in references))
            cfg = {"approved_task_ids": ["P29"], "variant": p.VARIANT, "native_split": "ood", "input_file": "input.jsonl",
                "review_file": "review.json", "scorer_reference_file": "refs.jsonl", "scorer_reference_sha256": p.file_sha(ref_path),
                "frozen_files_sha256": {"input.jsonl": p.file_sha(root / "input.jsonl"), "review.json": p.file_sha(root / "review.json")},
                "model": "synthetic", "model_revision": "synthetic-revision", "model_facing_fields": ["synthetic_input"], "run_id": "synthetic",
                "generation": {"max_tokens": 4096, "temperature": 1.0, "top_p": 0.95, "top_k": 20, "seed": 42, "n": 1,
                    "chat_template_kwargs": {"enable_thinking": True, "reasoning_effort": "medium"}},
                "paper_comparison": "Synthetic", "source_contract_disagreements": [], "prospective_interpretation": {}, "seed_predictor_overlap": {}}
            p.save(folder / "run_manifest.json", {"configuration": cfg, "case_contract_sha256": p.digest(cases), "planned_cases": 2})
            case = cases[0]; identity = p.digest([case["task"], case["variant"], case["case_id"]]) + ".json"; request = request_record(case, cfg)
            p.save(folder / "requests" / identity, request)
            p.save(folder / "responses" / identity, {**{k: case[k] for k in ["task", "case_id", "variant", "split"]}, "model": "synthetic",
                "model_revision": "synthetic-revision", "request_sha256": request["request_sha256"], "status": "completed", "http_status": 200,
                "text": "GO:0000001", "finish_reason": "stop", "response": {"model": "synthetic", "choices": [{"finish_reason": "stop",
                "message": {"content": "GO:0000001"}}]}})
            read_bytes = Path.read_bytes
            def guarded(path):
                if path == ref_path: self.assertTrue((folder / "scoring_output_lock.json").exists())
                return read_bytes(path)
            with mock.patch.object(scorer, "ROOT", root), mock.patch.object(Path, "read_bytes", guarded), mock.patch.object(p, "native_ontology", return_value=p.native_api().GeneOntology({})):
                result = scorer.score(folder)
            self.assertEqual(result["planned"], 2); self.assertEqual(result["completed"], 1)
            self.assertAlmostEqual(result["metrics"]["native_augmented_F1"], 1 / 3)
            self.assertEqual(result["curated_only_diagnostic_metrics"]["curated_only_F1_diagnostic"], 0)
            self.assertEqual(result["missing_or_failed_outputs"], 1)
            missing = cases[1]; missing_identity = p.digest([missing["task"], missing["variant"], missing["case_id"]]) + ".json"
            p.save(folder / "requests" / missing_identity, request_record(missing, cfg))
            with self.assertRaisesRegex(ValueError, "lock changed"):
                scorer.lock_outputs(folder, cases)


if __name__ == "__main__": unittest.main()
