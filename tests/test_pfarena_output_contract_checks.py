"""Artificial fixtures only; no benchmark data or network/model execution."""

import argparse
import ast
import asyncio
import copy
from dataclasses import dataclass
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import re
import types
import unittest


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("pfarena_output_contract_checks", ROOT / "scripts/pfarena_output_contract_checks.py")
audit = importlib.util.module_from_spec(SPEC)
# dataclasses resolves its defining module when annotations are evaluated.
import sys
sys.modules[SPEC.name] = audit
SPEC.loader.exec_module(audit)

PINNED_REVISION = "e8f8b3c404d39783a43eaa96ae461f313730114d"
NATIVE_SOURCE = Path(os.environ.get(
    "PFARENA_NATIVE_SOURCE",
    ROOT / ".local/source_recovery_round2_2026-10-19/pfarena/official_code/code",
))
PINNED_SHA256 = {
    "llm/infer_api_mutation.py": "242a8a36503860ecd3ac9c2609516d07860b66be37cd7f9d7c983a400e9d6ad4",
    "router.py": "f1ce2e22dec4efdd6051706289c5e108b0f569c44bc71655c12844b91688ce18",
    "prompts/single_mutant_generation.py": "18457c36c4bfd565534783a98520343f02dff3dbed7636ba6c8e9b642266560f",
    "prompts/multi_mutant_ranking.py": "647afb6b6cc3138af1e127da581363bc8acccd21b2c2a132056a6d5b3590acc2",
    "prompts/multi_mutant_ranking_anchor.py": "b9b42655d35e83f41f91342f58f08b356121e371eb89b9646aad3cf2d54b4405",
    "prompts/multi_mutant_ranking_mutation.py": "4db6b6e95575cdb75317eab85761ecd093ae89a9658609cab1239759b07678e4",
}
SYNTHETIC_RECORDS = []
SYNTHETIC_RANKING_RECORDS = []


def payload_bytes(payload):
    return json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()


def load_exact_native_builders():
    """Execute exact hash-pinned pure builders, not imports/CLI/API setup.

    AST extraction leaves each selected upstream function/class unchanged.
    Its real native prompt factories and router selection are also executed.
    A recording client stands in for transport at the upstream call boundary.
    """
    namespace = {
        "argparse": argparse, "dataclass": dataclass, "Path": Path,
        "json": json, "re": re, "AsyncOpenAI": object,
        "__name__": "synthetic_pfarena_native_builders",
    }
    nodes = {}
    for name, expected in PINNED_SHA256.items():
        data = (NATIVE_SOURCE / name).read_bytes()
        if hashlib.sha256(data).hexdigest() != expected:
            raise AssertionError(f"Pinned upstream source changed: {name}")
        nodes[name] = ast.parse(data.decode(), filename=name)
    factories = [
        ("prompts/single_mutant_generation.py", "single_mutant_generation_template"),
        ("prompts/multi_mutant_ranking.py", "multi_mutant_ranking_template"),
        ("prompts/multi_mutant_ranking_anchor.py", "multi_mutant_ranking_anchor_template"),
        ("prompts/multi_mutant_ranking_mutation.py", "multi_mutant_ranking_mutation_template"),
    ]
    for filename, name in factories:
        node = next(n for n in nodes[filename].body if isinstance(n, ast.FunctionDef) and n.name == name)
        exec(compile(ast.Module(body=[node], type_ignores=[]), filename, "exec"), namespace)
    router_nodes = [
        n for n in nodes["router.py"].body
        if (isinstance(n, ast.Assign) and any(isinstance(t, ast.Name) and t.id == "PROMPT_TEMPLATE_FACTORIES" for t in n.targets))
        or (isinstance(n, ast.FunctionDef) and n.name == "get_prompt_template")
    ]
    exec(compile(ast.Module(body=router_nodes, type_ignores=[]), "router.py", "exec"), namespace)
    selected = {"AssayContext", "MutationTask", "context_from_assay_row", "build_prompt", "create_chat_completion", "extract_balanced_json", "parse_rank_mode_mutants"}
    source_nodes = [n for n in nodes["llm/infer_api_mutation.py"].body if isinstance(n, (ast.ClassDef, ast.FunctionDef, ast.AsyncFunctionDef)) and n.name in selected]
    exec(compile(ast.Module(body=source_nodes, type_ignores=[]), "llm/infer_api_mutation.py", "exec"), namespace)
    return namespace


class RecordingClient:
    def __init__(self):
        self.calls = []
        self.chat = types.SimpleNamespace(completions=types.SimpleNamespace(create=self.create))

    async def create(self, **kwargs):
        self.calls.append(copy.deepcopy(kwargs))
        return {"synthetic_recorded": True}


class RankingContractTests(unittest.TestCase):
    IDS = ("candidate_01", "candidate_02", "candidate_03")

    def test_complete_permutation_in_any_order(self):
        self.assertTrue(audit.audit_full_ranking(self.IDS, list(reversed(self.IDS))).complete_permutation)

    def test_missing_candidate_is_flagged(self):
        result = audit.audit_full_ranking(self.IDS, list(self.IDS[:2]))
        self.assertFalse(result.complete_permutation)
        self.assertEqual(result.missing_ids, ("candidate_03",))

    def test_duplicate_candidate_is_flagged(self):
        result = audit.audit_full_ranking(self.IDS, ["candidate_01", "candidate_01", "candidate_03"])
        self.assertEqual(result.duplicate_ids, ("candidate_01",))
        self.assertIn("missing_candidates", result.errors)

    def test_unknown_candidate_is_flagged(self):
        result = audit.audit_full_ranking(self.IDS, ["candidate_01", "candidate_02", "other"])
        self.assertEqual(result.unknown_ids, ("other",))
        self.assertFalse(result.complete_permutation)

    def test_non_list_answers_are_rejected_without_coercion(self):
        for value in (None, self.IDS, "candidate_01", {"ranking": []}, 1):
            with self.subTest(value_type=type(value).__name__):
                self.assertEqual(audit.audit_full_ranking(self.IDS, value).errors, ("ranking_not_json_list",))

    def test_malformed_identifiers_are_flagged(self):
        for value in ("", " candidate_01", "candidate_01 ", "candidate_01\n", "candidate\x00_01", 1, None, {}, []):
            with self.subTest(value_type=type(value).__name__, repr=repr(value)):
                result = audit.audit_full_ranking(self.IDS, [value, "candidate_02", "candidate_03"])
                self.assertEqual(result.malformed_item_indices, (0,))
                self.assertFalse(result.complete_permutation)

    def test_whitespace_is_not_silently_repaired(self):
        result = audit.audit_full_ranking(self.IDS, ["candidate_01 ", "candidate_02", "candidate_03"])
        self.assertEqual(result.missing_ids, ("candidate_01",))

    def test_integer_is_not_coerced_to_candidate_id(self):
        result = audit.audit_full_ranking(("1", "2"), [1, "2"])
        self.assertFalse(result.complete_permutation)
        self.assertEqual(result.missing_ids, ("1",))

    def test_invalid_frozen_candidate_contract_is_rejected(self):
        for expected in ((), "candidate_01", ("a", "a"), ("a", ""), ("a", 1)):
            with self.subTest(expected=repr(expected)):
                with self.assertRaises(ValueError):
                    audit.audit_full_ranking(expected, [])

    def test_missing_ranking_field_is_explicit(self):
        self.assertEqual(audit.audit_ranking_object(self.IDS, {}).errors, ("missing_ranking_field",))

    def test_non_object_structured_answer_is_explicit(self):
        self.assertEqual(audit.audit_ranking_object(self.IDS, list(self.IDS)).errors, ("answer_not_json_object",))

    def test_audit_does_not_mutate_input_or_answer(self):
        candidates = list(self.IDS)
        answer = {"ranking": list(reversed(self.IDS))}
        before = copy.deepcopy((candidates, answer))
        audit.audit_ranking_object(candidates, answer)
        self.assertEqual((candidates, answer), before)


@unittest.skipUnless(NATIVE_SOURCE.is_dir(), "Pinned native source is not available; set PFARENA_NATIVE_SOURCE to the verified code directory")
class NativeSyntheticSeparationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.native = load_exact_native_builders()

    def fixture(self, task_id):
        return {
            "native_inputs": {
                "assay_id": "synthetic_assay", "uniprot_id": "SYNTHETIC_NOT_A_PROTEIN_ID",
                "primary_task_class": "artificial formatting fixture", "fitness_type": "synthetic scalar",
                "readout_subclass": "invented test label", "wildtype_sequence": "ACDEFGHIKL", "sequence_length": "10",
                "DMS_score": "GOLD_ONLY_SENTINEL_A", "reference_ranking": ["GOLD_ONLY_SENTINEL_B"],
                "qwen_prediction": "PRIOR_OUTPUT_SENTINEL_A", "qwen_correct": True,
            },
            "candidate_ids": () if task_id == "1" else (
                ("A1V", "C2D", "D3E") if task_id == "2" else ("A1V+C2D", "A1V+D3E", "A1V+E4F")
            ),
            "anchor_mutant": "A1V" if task_id == "3" else "",
            "anchor_dms_score": "0.125" if task_id == "3" else "",
            "single_mutant_dms_scores": "A1V: 0.125\nC2D: 0.25\nD3E: 0.375\nE4F: 0.5" if task_id == "4" else "",
            "ground_truth_path": "/synthetic/scorer_only/original.csv",
            "scorer_only": {"target_scores": [901, 902, 903], "prior_qwen_outputs": ["PRIOR_OUTPUT_SENTINEL_B"]},
        }

    def capture(self, task_id, fixture):
        context = self.native["context_from_assay_row"](fixture["native_inputs"], Path("/synthetic/assay.csv"))
        task = self.native["MutationTask"](
            input_path=Path("/synthetic/native/input.csv"), output_path=Path("/synthetic/output/predictions.csv"),
            context=context, mutants=fixture["candidate_ids"], ground_truth_path=Path(fixture["ground_truth_path"]),
            anchor_mutant=fixture["anchor_mutant"], anchor_dms_score=fixture["anchor_dms_score"],
            single_mutant_dms_scores=fixture["single_mutant_dms_scores"],
        )
        args = argparse.Namespace(task_id=task_id, model="synthetic-no-model", max_completion_tokens=128)
        client = RecordingClient()
        asyncio.run(self.native["create_chat_completion"](client, task, args))
        self.assertEqual(len(client.calls), 1)
        return client.calls[0]

    def check_scorer_invariance(self, task_id):
        fixture = self.fixture(task_id)
        baseline = self.capture(task_id, fixture)
        mutated = copy.deepcopy(fixture)
        mutated["native_inputs"].update(DMS_score="GOLD_ONLY_SENTINEL_CHANGED", reference_ranking=["changed"], qwen_prediction="changed", qwen_correct=False)
        mutated["scorer_only"] = {"target_scores": [-999, 0, 999], "prior_qwen_outputs": ["changed"]}
        mutated["ground_truth_path"] = "/synthetic/scorer_only/different.csv"
        changed = self.capture(task_id, mutated)
        removed = copy.deepcopy(mutated)
        for name in ("DMS_score", "reference_ranking", "qwen_prediction", "qwen_correct"):
            removed["native_inputs"].pop(name)
        removed.pop("scorer_only")
        removed_payload = self.capture(task_id, removed)
        self.assertEqual(payload_bytes(baseline), payload_bytes(changed))
        self.assertEqual(payload_bytes(baseline), payload_bytes(removed_payload))
        serialized = payload_bytes(baseline).decode()
        self.assertNotIn("GOLD_ONLY_SENTINEL", serialized)
        self.assertNotIn("PRIOR_OUTPUT_SENTINEL", serialized)
        SYNTHETIC_RECORDS.append({
            "task_id": "T" + task_id, "native_builder_executed": True,
            "baseline_payload_sha256": hashlib.sha256(payload_bytes(baseline)).hexdigest(),
            "mutated_scorer_payload_sha256": hashlib.sha256(payload_bytes(changed)).hexdigest(),
            "removed_scorer_payload_sha256": hashlib.sha256(payload_bytes(removed_payload)).hexdigest(),
            "byte_invariance_passed": True, "real_requests_sent": 0,
        })

    def test_t1_genuine_builder_scorer_invariance(self): self.check_scorer_invariance("1")
    def test_t2_genuine_builder_scorer_invariance(self): self.check_scorer_invariance("2")
    def test_t3_genuine_builder_scorer_invariance(self): self.check_scorer_invariance("3")
    def test_t4_genuine_builder_scorer_invariance(self): self.check_scorer_invariance("4")

    def test_t3_legitimate_anchor_context_remains_visible(self):
        fixture = self.fixture("3")
        baseline = self.capture("3", fixture)
        self.assertIn("0.125", baseline["messages"][0]["content"])
        fixture["anchor_dms_score"] = "0.625"
        changed = self.capture("3", fixture)
        self.assertNotEqual(payload_bytes(baseline), payload_bytes(changed))
        self.assertIn("0.625", changed["messages"][0]["content"])

    def test_t4_legitimate_component_context_remains_visible(self):
        fixture = self.fixture("4")
        baseline = self.capture("4", fixture)
        self.assertIn("A1V: 0.125", baseline["messages"][0]["content"])
        fixture["single_mutant_dms_scores"] = fixture["single_mutant_dms_scores"].replace("0.125", "0.875")
        changed = self.capture("4", fixture)
        self.assertNotEqual(payload_bytes(baseline), payload_bytes(changed))
        self.assertIn("A1V: 0.875", changed["messages"][0]["content"])

    def test_candidate_order_is_a_real_input_positive_control(self):
        fixture = self.fixture("2")
        baseline = self.capture("2", fixture)
        fixture["candidate_ids"] = tuple(reversed(fixture["candidate_ids"]))
        self.assertNotEqual(payload_bytes(baseline), payload_bytes(self.capture("2", fixture)))

    def test_real_request_builder_has_fresh_single_user_context(self):
        for task_id in ("1", "2", "3", "4"):
            with self.subTest(task=task_id):
                payload = self.capture(task_id, self.fixture(task_id))
                self.assertEqual(set(payload), {"model", "messages", "max_completion_tokens", "stream"})
                self.assertEqual(len(payload["messages"]), 1)
                self.assertEqual(payload["messages"][0]["role"], "user")
                self.assertIsInstance(payload["messages"][0]["content"], str)
                self.assertEqual(payload["max_completion_tokens"], 128)
                self.assertFalse(payload["stream"])

    def test_native_partial_list_acceptance_stays_separate_from_audit(self):
        raw = '{"ranking": ["A1V"]}'
        self.assertEqual(self.native["parse_rank_mode_mutants"](raw), ("A1V",))
        result = audit.audit_ranking_object(("A1V", "C2D", "D3E"), json.loads(raw))
        self.assertFalse(result.complete_permutation)
        self.assertEqual(result.missing_ids, ("C2D", "D3E"))

    def test_each_ranking_task_has_separate_full_set_checks(self):
        for task_id in ("2", "3", "4"):
            with self.subTest(task=task_id):
                expected = self.fixture(task_id)["candidate_ids"]
                complete = list(reversed(expected))
                encoded = json.dumps({"ranking": complete})
                self.assertEqual(self.native["parse_rank_mode_mutants"](encoded), tuple(complete))
                self.assertTrue(audit.audit_ranking_object(expected, json.loads(encoded)).complete_permutation)
                for broken in (complete[:-1], [complete[0], complete[0], complete[2]], [complete[0], complete[1], "UNKNOWN_SYNTHETIC_ID"]):
                    self.assertFalse(audit.audit_full_ranking(expected, broken).complete_permutation)
                SYNTHETIC_RANKING_RECORDS.append({
                    "task_id": "T" + task_id, "synthetic_expected_count": len(expected),
                    "complete_permutation_accepted": True,
                    "missing_duplicate_unknown_rejected": True,
                    "native_parser_preserved": True,
                })

    def test_native_string_coercion_is_not_used_by_separate_audit(self):
        encoded = '{"ranking": [1, "2"]}'
        self.assertEqual(self.native["parse_rank_mode_mutants"](encoded), ("1", "2"))
        self.assertFalse(audit.audit_ranking_object(("1", "2"), json.loads(encoded)).complete_permutation)


if __name__ == "__main__":
    unittest.main()
