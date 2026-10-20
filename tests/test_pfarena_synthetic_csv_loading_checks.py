"""Additional pinned-native CSV checks using artificial temporary files only.

The published builder/permutation suite remains separate and unchanged. This
suite exercises upstream discovery/loaders and records their request arguments;
it does not import API setup, call a model or read a real dataset table.
"""

import argparse
import ast
import asyncio
from collections import Counter
from contextlib import contextmanager
import copy
import csv
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
import tempfile
import types
import unittest
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "pfarena_published_synthetic_contract_tests",
    ROOT / "tests/test_pfarena_output_contract_checks.py",
)
contracts = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = contracts
SPEC.loader.exec_module(contracts)

CSV_FUNCTIONS = (
    "read_mutants", "read_assay_contexts", "relative_output_path",
    "output_task_prefix", "mutation_generation_relative_path",
    "mutation_generation_output_path", "read_candidate_assay_index",
    "read_single_mutant_dms_scores", "rank_assay_csv_path",
    "discover_generation_tasks", "discover_rank_tasks", "discover_tasks",
)
TASK_DIRS = {
    "1": "T1_single_mutant_generation",
    "2": "T2_measurement_free_multi_mutant_ranking",
    "3": "T3_anchor_informed_multi_mutant_ranking",
    "4": "T4_single_mutant_informed_multi_mutant_ranking",
}
SCORER_FIELDS = ("DMS_score", "reference_answer", "reference_explanation", "qwen_prediction", "qwen_correct")
CHECK_RECORDS = []
CHARACTERIZATION_RECORDS = []


def load_exact_native_csv_pipeline():
    namespace = contracts.load_exact_native_builders()
    source = contracts.NATIVE_SOURCE / "llm/infer_api_mutation.py"
    data = source.read_bytes()
    if hashlib.sha256(data).hexdigest() != contracts.PINNED_SHA256["llm/infer_api_mutation.py"]:
        raise AssertionError("Pinned upstream loader source changed")
    tree = ast.parse(data.decode(), filename="llm/infer_api_mutation.py")
    selected = [node for node in tree.body if isinstance(node, ast.FunctionDef) and node.name in CSV_FUNCTIONS]
    if {node.name for node in selected} != set(CSV_FUNCTIONS):
        raise AssertionError("A required upstream CSV function is absent")
    namespace["csv"] = csv
    exec(compile(ast.Module(body=selected, type_ignores=[]), "llm/infer_api_mutation.py", "exec"), namespace)
    return namespace


def write_rows(path, rows, fields=None):
    path.parent.mkdir(parents=True, exist_ok=True)
    if fields is None:
        fields = list(dict.fromkeys(key for row in rows for key in row))
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


@unittest.skipUnless(contracts.NATIVE_SOURCE.is_dir(), "Pinned native source is unavailable; no adapter loader is substituted")
class NativeCSVLoadingTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.native = load_exact_native_csv_pipeline()

    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="pfarena_artificial_csv_")
        self.addCleanup(self.temp.cleanup)
        self.work = Path(self.temp.name).resolve()

    def fixture(self, task_id):
        directory = self.work / TASK_DIRS[task_id]
        relative = {
            "1": "norm_data/synthetic_assay.csv",
            "2": "norm_data/synthetic_assay_random_multi.csv",
            "3": "norm_data/synthetic_assay/anchor_successor.csv",
            "4": "norm_data/synthetic_assay/single_context_combo.csv",
        }[task_id]
        common = {
            "reference_answer": "SCORER_ONLY_ORIGINAL_REFERENCE",
            "reference_explanation": "SCORER_ONLY_ORIGINAL_EXPLANATION",
            "qwen_prediction": "PRIOR_QWEN_OUTPUT_NOT_INPUT",
            "qwen_correct": "true",
        }
        metadata = [{
            "assay_id": "synthetic_assay_T" + task_id,
            "uniprot_id": "ARTIFICIAL_ID_NOT_A_PROTEIN",
            "primary_task_class": "artificial CSV fixture",
            "fitness_type": "invented scalar",
            "readout_subclass": "synthetic measurement label",
            "wildtype_sequence": "ACDEFGHIKL", "sequence_length": "10",
            "DMS_filename": relative, "DMS_score": "987654.125",
            "anchor_mutant": "A1V", "anchor_DMS_score": "0.125", **common,
        }]
        candidates = ("A1V", "C2D", "D3E") if task_id in ("1", "2") else ("A1V+C2D", "A1V+D3E", "A1V+E4F")
        target_rows = [
            {"mutant": candidate, "mutated_sequence": "VCDEFGHIKL", "DMS_score": str(11 + index), **common}
            for index, candidate in enumerate(candidates)
        ]
        context_rows = [
            {"mutant": candidate, "mutated_sequence": "VCDEFGHIKL", "DMS_score": score, **common}
            for candidate, score in zip(("A1V", "C2D", "D3E", "E4F"), ("0.125", "0.25", "0.375", "0.5"))
        ]
        result = types.SimpleNamespace(
            task_id=task_id, directory=directory, metadata=metadata,
            metadata_path=directory / "assay.csv", target_path=directory / relative,
            target_rows=target_rows, context_rows=context_rows,
            context_path=(directory / relative).parent / "single_mutant_context.csv",
            auxiliary_path=directory / "norm_data/scorer_only_prior_outputs.csv",
        )
        result.args = argparse.Namespace(
            task_id=task_id, model="synthetic-no-model", max_completion_tokens=128,
            input_dir=result.metadata_path if task_id == "1" else directory / "norm_data",
            output_root=self.work / "outputs", force=False, max_files=None,
        )
        self.flush(result)
        return result

    def flush(self, fixture):
        write_rows(fixture.metadata_path, fixture.metadata)
        write_rows(fixture.target_path, fixture.target_rows)
        if fixture.task_id == "4":
            write_rows(fixture.context_path, fixture.context_rows)
        # This intentionally has no mutant column. A generic all-CSV loader
        # would fail; native discovery must skip files absent from its index.
        write_rows(fixture.auxiliary_path, [{"reference_answer": "SCORER_ONLY_AUXILIARY_NOT_INPUT"}])

    def capture(self, fixture):
        reads = []
        calls = []
        function_calls = set()
        original_open = Path.open

        def guarded_open(path, *args, **kwargs):
            resolved = path.resolve()
            if not resolved.is_relative_to(self.work):
                raise AssertionError("Synthetic loader attempted a file outside its artificial temp directory")
            reads.append(resolved)
            return original_open(path, *args, **kwargs)

        def profile(frame, event, arg):
            if event == "call" and frame.f_code.co_filename == "llm/infer_api_mutation.py":
                function_calls.add(frame.f_code.co_name)

        previous_profile = sys.getprofile()
        try:
            sys.setprofile(profile)
            with patch.object(Path, "open", guarded_open):
                tasks = self.native["discover_tasks"](fixture.args)
                for task in tasks:
                    client = contracts.RecordingClient()
                    asyncio.run(self.native["create_chat_completion"](client, task, fixture.args))
                    self.assertEqual(len(client.calls), 1)
                    payload = client.calls[0]
                    self.assertEqual(set(payload), {"model", "messages", "max_completion_tokens", "stream"})
                    self.assertEqual(len(payload["messages"]), 1)
                    self.assertEqual(payload["messages"][0]["role"], "user")
                    calls.append(payload)
        finally:
            sys.setprofile(previous_profile)
        return tasks, calls, reads, function_calls

    def invariant(self, task_id):
        fixture = self.fixture(task_id)
        tasks, baseline, baseline_reads, functions = self.capture(fixture)
        self.assertEqual(len(tasks), 1)
        for row in fixture.metadata + fixture.target_rows:
            row.update(DMS_score="-987654.875", reference_answer="SCORER_ONLY_CHANGED_REFERENCE", reference_explanation="changed", qwen_prediction="changed", qwen_correct="false")
        for row in fixture.context_rows:
            for key in SCORER_FIELDS:
                if key != "DMS_score":
                    row[key] = "SCORER_ONLY_CHANGED_CONTEXT_EXTRA"
        self.flush(fixture)
        _, mutated, mutated_reads, functions2 = self.capture(fixture)
        for row in fixture.metadata + fixture.target_rows:
            for key in SCORER_FIELDS:
                row.pop(key, None)
        for row in fixture.context_rows:
            for key in SCORER_FIELDS:
                if key != "DMS_score":
                    row.pop(key, None)
        self.flush(fixture)
        _, removed, removed_reads, functions3 = self.capture(fixture)
        before = contracts.payload_bytes(baseline)
        self.assertEqual(before, contracts.payload_bytes(mutated))
        self.assertEqual(before, contracts.payload_bytes(removed))
        self.assertNotIn("SCORER_ONLY", before.decode())
        self.assertNotIn("PRIOR_QWEN", before.decode())
        self.assertNotIn(fixture.auxiliary_path.resolve(), baseline_reads + mutated_reads + removed_reads)
        CHECK_RECORDS.append({
            "task_id": "T" + task_id,
            "baseline_request_sha256": hashlib.sha256(before).hexdigest(),
            "mutated_scorer_request_sha256": hashlib.sha256(contracts.payload_bytes(mutated)).hexdigest(),
            "removed_scorer_request_sha256": hashlib.sha256(contracts.payload_bytes(removed)).hexdigest(),
            "byte_invariance_passed": True,
            "unindexed_scorer_csv_was_not_opened": True,
            "opened_paths_restricted_to_artificial_temp_directory": True,
            "upstream_functions_observed": sorted(functions | functions2 | functions3),
            "real_requests_sent": 0,
        })

    def test_t1_actual_csv_loader_scorer_invariance(self): self.invariant("1")
    def test_t2_actual_csv_loader_scorer_invariance(self): self.invariant("2")
    def test_t3_actual_csv_loader_scorer_invariance(self): self.invariant("3")
    def test_t4_actual_csv_loader_scorer_invariance(self): self.invariant("4")

    def test_t1_does_not_open_scorer_target_table(self):
        fixture = self.fixture("1")
        fixture.target_path.write_bytes(b"not even a CSV: scorer-only artificial bytes")
        tasks, payloads, reads, _ = self.capture(fixture)
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0].ground_truth_path, fixture.target_path)
        self.assertNotIn(fixture.target_path.resolve(), reads)
        self.assertEqual(len(payloads), 1)

    def test_t4_context_is_loaded_once_and_not_dispatched_as_a_candidate(self):
        fixture = self.fixture("4")
        tasks, payloads, reads, _ = self.capture(fixture)
        self.assertEqual(len(tasks), 1)
        self.assertEqual(Counter(reads)[fixture.context_path.resolve()], 1)
        self.assertIn("A1V: 0.125", payloads[0]["messages"][0]["content"])

    def test_t3_provided_anchor_score_changes_request(self):
        fixture = self.fixture("3")
        _, baseline, _, _ = self.capture(fixture)
        fixture.metadata[0]["anchor_DMS_score"] = "0.625"
        self.flush(fixture)
        _, changed, _, _ = self.capture(fixture)
        self.assertNotEqual(contracts.payload_bytes(baseline), contracts.payload_bytes(changed))
        self.assertIn("0.625", changed[0]["messages"][0]["content"])

    def test_t4_provided_component_score_changes_request(self):
        fixture = self.fixture("4")
        _, baseline, _, _ = self.capture(fixture)
        fixture.context_rows[0]["DMS_score"] = "0.875"
        self.flush(fixture)
        _, changed, _, _ = self.capture(fixture)
        self.assertNotEqual(contracts.payload_bytes(baseline), contracts.payload_bytes(changed))
        self.assertIn("A1V: 0.875", changed[0]["messages"][0]["content"])

    def test_candidate_csv_order_changes_ranking_requests(self):
        for task_id in ("2", "3", "4"):
            with self.subTest(task=task_id):
                fixture = self.fixture(task_id)
                _, baseline, _, _ = self.capture(fixture)
                fixture.target_rows.reverse()
                self.flush(fixture)
                _, changed, _, _ = self.capture(fixture)
                self.assertNotEqual(contracts.payload_bytes(baseline), contracts.payload_bytes(changed))

    def test_legitimate_sequence_metadata_changes_requests(self):
        for task_id in ("1", "2", "3", "4"):
            with self.subTest(task=task_id):
                fixture = self.fixture(task_id)
                _, baseline, _, _ = self.capture(fixture)
                fixture.metadata[0]["wildtype_sequence"] = "ACDEFGHIKM"
                self.flush(fixture)
                _, changed, _, _ = self.capture(fixture)
                self.assertNotEqual(contracts.payload_bytes(baseline), contracts.payload_bytes(changed))

    def test_multiple_assays_keep_their_metadata_associated_by_id(self):
        fixture = self.fixture("2")
        second = copy.deepcopy(fixture.metadata[0])
        second.update(assay_id="synthetic_second_T2", uniprot_id="ARTIFICIAL_SECOND_ONLY", DMS_filename="norm_data/second_random_multi.csv")
        fixture.metadata.insert(0, second)
        self.flush(fixture)
        second_path = fixture.directory / second["DMS_filename"]
        write_rows(second_path, [{"mutant": "E4F", "DMS_score": "123"}])
        expected = {
            fixture.target_path.resolve(): (
                fixture.metadata[1]["assay_id"], fixture.metadata[1]["uniprot_id"],
                tuple(row["mutant"] for row in fixture.target_rows),
            ),
            second_path.resolve(): (second["assay_id"], second["uniprot_id"], ("E4F",)),
        }
        tasks, payloads, _, _ = self.capture(fixture)
        self.assertEqual(len(tasks), 2)
        self.assertEqual({task.input_path.resolve() for task in tasks}, set(expected))
        for task, payload in zip(tasks, payloads):
            assay_id, uniprot_id, candidates = expected[task.input_path.resolve()]
            self.assertEqual(task.context.assay_id, assay_id)
            self.assertEqual(task.context.uniprot_id, uniprot_id)
            self.assertEqual(task.mutants, candidates)
            text = payload["messages"][0]["content"]
            self.assertIn(uniprot_id, text)
            for candidate in candidates:
                self.assertIn(candidate, text)

    def test_empty_candidate_table_fails_native_loading(self):
        fixture = self.fixture("2")
        write_rows(fixture.target_path, [], fields=["mutant", "DMS_score"])
        with self.assertRaisesRegex(ValueError, "no candidate mutants"):
            self.capture(fixture)

    def test_missing_assay_identity_header_fails_native_loading(self):
        fixture = self.fixture("2")
        write_rows(fixture.metadata_path, [{"unrelated_header": "synthetic"}])
        with self.assertRaisesRegex(ValueError, "missing required assay_id column"):
            self.capture(fixture)

    def test_missing_t4_context_file_fails_instead_of_being_fabricated(self):
        fixture = self.fixture("4")
        fixture.context_path.unlink()
        with self.assertRaises(FileNotFoundError):
            self.capture(fixture)

    def test_missing_t3_anchor_field_fails_instead_of_being_fabricated(self):
        fixture = self.fixture("3")
        fixture.metadata[0].pop("anchor_DMS_score")
        self.flush(fixture)
        with self.assertRaises(KeyError):
            self.capture(fixture)

    def test_nonempty_header_only_output_is_skipped_by_upstream(self):
        # Characterize native resume behavior without changing it. A nonempty
        # file is not proof of parsed/completed predictions.
        for task_id in ("1", "2", "3", "4"):
            with self.subTest(task=task_id):
                fixture = self.fixture(task_id)
                tasks, _, _, _ = self.capture(fixture)
                output = tasks[0].output_path
                output.parent.mkdir(parents=True, exist_ok=True)
                output.write_text("assay,mutant,rank\n")
                skipped, payloads, _, _ = self.capture(fixture)
                self.assertEqual(skipped, [])
                self.assertEqual(payloads, [])
        CHARACTERIZATION_RECORDS.append({
            "finding": "All four native discovery paths skip any nonempty output file when force=False, including a header-only CSV.",
            "scope": "Observed only on artificial files; no existing prediction or protocol was changed.",
            "delivery_or_scoring_success_established": False,
        })


if __name__ == "__main__":
    unittest.main()
