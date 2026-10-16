"""Synthetic-only state/locking tests. No GFP checkpoint forward is executed."""
import base64
import contextlib
import copy
import fcntl
import hashlib
import importlib.util
import io
import json
from pathlib import Path
import sys
import tempfile
import threading
from types import SimpleNamespace
import unittest
from unittest import mock

SCRIPTS = Path(__file__).parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS))
import score_local_stride_gfp as scorer
import stride_gfp_cpu_oracle as runtime
import run_local_stride_gfp as runner

try:
    import torch
except ImportError:
    torch = None


def fixture_case(regime, index):
    return {"task_id": "P42", "case_id": f"p42:{regime}:{index:03d}",
        "protocol_variant": f"QWEN_GFP_QUALIFIED_{regime.upper()}_ENDPOINT_1_TO_3",
        "split": "fixed_publisher_anchor_generated_candidates", "sample_index": index, "seed": 42 + index,
        "messages": [{"role": "system", "content": "Synthetic system fixture"},
                     {"role": "user", "content": "Synthetic user fixture"}]}


def synthetic_cohort(folder, missing=None):
    source = "ACDEFG"
    cases = [fixture_case(regime, i) for regime in ("replace_only", "full_atomic") for i in range(100)]
    cfg = {"run_id": "synthetic_gfp_fixture", "model": runner.MODEL, "model_revision": runner.MODEL_REVISION,
        "generation": copy.deepcopy(runner.GENERATION), "tool_access": [], "variant": runner.VARIANT,
        "endpoint": "http://127.0.0.1:8033/v1", "oracle_runtime_sha256": "synthetic_runtime",
        "oracle_state_audit_sha256": "synthetic_audit", "interpretation": {"test": "synthetic only"}}
    runner.write_json(folder / "run_manifest.json", {"fixture": True})
    runner.write_json(folder / "case_inputs.json", cases)
    value = {"model": runner.MODEL, "choices": [{"message": {"content": '{"protein":"ACDEFA"}',
        "reasoning": "Synthetic reasoning fixture"}, "finish_reason": "stop"}]}
    raw = json.dumps(value).encode()
    wire = {"http_status": 200, "response": value, "raw_response_base64": base64.b64encode(raw).decode(),
        "raw_response_utf8": raw.decode(), "raw_response_sha256": hashlib.sha256(raw).hexdigest(), "transport_or_schema_error": None}
    statuses = {}
    with mock.patch.object(runner, "http_json", return_value=wire) as request:
        for number, case in enumerate(cases):
            statuses[case["case_id"]] = ("not_dispatched_after_error" if number == missing else
                runner.execute_one(case, cfg, folder, source, threading.Event()))
        assert request.call_count == 200 - (missing is not None)
    runner.seal_generation(folder, cfg, cases, statuses)
    return cfg, cases, source, {"oracle": {"assets": []}}


class SyntheticOracle:
    def __init__(self, folder, candidate_score=2.0, baseline=1.0):
        self.folder = folder; self.calls = []; self.candidate_score = candidate_score; self.baseline = baseline

    def predict(self, sequences):
        # This fake forward cannot start until all200 slots and original bytes
        # are immutable, including both missing files for an undispatched slot.
        lock = scorer.read(self.folder / "scoring_output_lock.json")
        assert lock["planned_cases"] == 200
        assert len(lock["files_sha256"]) == 404
        assert len(scorer.read(self.folder / "generation_artifact_lock.json")["slots"]) == 200
        for name, expected in lock["files_sha256"].items():
            path = self.folder / name
            assert (runtime.file_sha(path) if path.exists() else None) == expected
        self.calls.append(list(sequences))
        return [self.baseline if sequence == "ACDEFG" else self.candidate_score for sequence in sequences]


class TestQualifiedOracleScorer(unittest.TestCase):
    def run_score(self, folder, state, fake):
        def factory():
            self.assertTrue((folder / "scoring_output_lock.json").exists())
            return fake, {"synthetic": True}
        with mock.patch.object(scorer, "verify_frozen_run", return_value=state), contextlib.redirect_stdout(io.StringIO()):
            return scorer.score(folder, factory)

    def test_every_slot_locked_before_fake_forward_and_duplicates_map_back(self):
        with tempfile.TemporaryDirectory() as tmp:
            folder = Path(tmp); state = synthetic_cohort(folder); fake = SyntheticOracle(folder)
            result = self.run_score(folder, state, fake)
            self.assertEqual(fake.calls, [["ACDEFG"], ["ACDEFA"]])
            self.assertEqual(result["distinct_oracle_sequences_attempted"], 2)
            self.assertEqual(result["eligible_duplicate_slot_count"], 199)
            self.assertEqual(len(scorer.read(folder / "per_case_scores.json")), 200)
            for regime in ("replace_only", "full_atomic"):
                self.assertEqual(result["metrics"][regime]["qualified_oracle_success"], 1.0)
                self.assertEqual(result["metrics"][regime]["improved_sequence_uniqueness"], .01)
                self.assertIsNone(result["metrics"][regime]["native_novelty"])
            self.assertEqual(result["scoring_output_lock_sha256"], runtime.file_sha(folder / "scoring_output_lock.json"))
            # Completed immutable scoring is reusable without repeating a forward.
            again = self.run_score(folder, state, fake)
            self.assertEqual(again, result); self.assertEqual(len(fake.calls), 2)

    def test_missing_generation_preserves100_denominator_and_nonzero_generation(self):
        with tempfile.TemporaryDirectory() as tmp:
            folder = Path(tmp); state = synthetic_cohort(folder, missing=0); fake = SyntheticOracle(folder)
            result = self.run_score(folder, state, fake)
            self.assertEqual(result["metrics"]["replace_only"]["qualified_oracle_success"], .99)
            self.assertEqual(result["completed"], 199)
            self.assertIn("INCOMPLETE", result["case_scope"])
            self.assertEqual(scorer.read(folder / "oracle_scoring_completion.json")["generation_exit_code"], 1)
            self.assertEqual(len(scorer.read(folder / "per_case_scores.json")), 200)
            self.assertEqual(fake.calls, [["ACDEFG"], ["ACDEFA"]])

    def test_nonfinite_candidate_score_is_null_not_zero(self):
        with tempfile.TemporaryDirectory() as tmp:
            folder = Path(tmp); state = synthetic_cohort(folder); fake = SyntheticOracle(folder, candidate_score=float("nan"))
            result = self.run_score(folder, state, fake)
            self.assertFalse(result["qualified_proxy_metrics_complete"])
            self.assertIsNone(result["metrics"]["replace_only"]["qualified_oracle_success"])
            self.assertTrue(result["oracle_errors"])
            self.assertEqual(len(scorer.read(folder / "per_case_scores.json")), 200)

    def test_nonfinite_source_preserves_all_cases_without_improvement_claim(self):
        with tempfile.TemporaryDirectory() as tmp:
            folder = Path(tmp); state = synthetic_cohort(folder); fake = SyntheticOracle(folder, baseline=float("nan"))
            result = self.run_score(folder, state, fake)
            self.assertIsNone(result["source_oracle_score"])
            self.assertIsNone(result["metrics"]["full_atomic"]["qualified_oracle_success"])
            rows = scorer.read(folder / "per_case_scores.json")
            self.assertEqual(len(rows), 200)
            self.assertTrue(all(row["oracle_improved"] is None for row in rows))

    def test_raw_tampering_and_new_locked_missing_output_rejected_before_oracle(self):
        for change in ("bytes", "identity", "missing_appears"):
            with self.subTest(change=change), tempfile.TemporaryDirectory() as tmp:
                folder = Path(tmp); state = synthetic_cohort(folder, missing=0 if change == "missing_appears" else None)
                if change == "bytes":
                    path = next((folder / "responses").glob("*.json")); path.write_text(path.read_text() + " ")
                elif change == "identity":
                    seal = scorer.read(folder / "generation_artifact_lock.json"); seal["slots"][0]["seed"] = 99
                    scorer.save(folder / "generation_artifact_lock.json", seal)
                else:
                    case = state[1][0]
                    scorer.save(folder / "responses" / (runner.request_identity(case) + ".json"), {"unexpected": True})
                factory = mock.Mock()
                with mock.patch.object(scorer, "verify_frozen_run", return_value=state), self.assertRaises(ValueError): scorer.score(folder, factory)
                factory.assert_not_called()

    def test_resealed_wrong_case_response_rejected_before_oracle(self):
        with tempfile.TemporaryDirectory() as tmp:
            folder = Path(tmp); state = synthetic_cohort(folder)
            path = next((folder / "responses").glob("*.json")); value = scorer.read(path); value["case_id"] = "other_case"
            scorer.save(path, value)
            seal = scorer.read(folder / "generation_artifact_lock.json")
            for slot in seal["slots"]:
                if slot["response_file"] == str(path.relative_to(folder)): slot["response_file_sha256"] = runtime.file_sha(path)
            scorer.save(folder / "generation_artifact_lock.json", seal)
            factory = mock.Mock()
            with mock.patch.object(scorer, "verify_frozen_run", return_value=state), self.assertRaises(ValueError): scorer.score(folder, factory)
            factory.assert_not_called()

    def test_unfinished_prior_invocation_cannot_repeat_and_completed_scores_cannot_change(self):
        with tempfile.TemporaryDirectory() as tmp:
            folder = Path(tmp); state = synthetic_cohort(folder)
            scorer.save(folder / "oracle_scoring_invocation.json", {"prior": "interrupted"})
            factory = mock.Mock()
            with mock.patch.object(scorer, "verify_frozen_run", return_value=state), self.assertRaises(ValueError): scorer.score(folder, factory)
            factory.assert_not_called()
        with tempfile.TemporaryDirectory() as tmp:
            folder = Path(tmp); state = synthetic_cohort(folder); fake = SyntheticOracle(folder)
            self.run_score(folder, state, fake)
            path = folder / "scores.json"; value = scorer.read(path); value["source_oracle_score"] = 17.0; scorer.save(path, value)
            with self.assertRaises(ValueError): self.run_score(folder, state, fake)
            self.assertEqual(len(fake.calls), 2)

    def test_overlapping_scorer_processes_cannot_forward_twice(self):
        with tempfile.TemporaryDirectory() as tmp:
            folder = Path(tmp)
            with (folder / "oracle_scoring_worker.lock").open("a") as handle:
                fcntl.flock(handle, fcntl.LOCK_EX | fcntl.LOCK_NB)
                with self.assertRaises(BlockingIOError): scorer.score(folder, mock.Mock())


@unittest.skipIf(torch is None, "Run with .venv-oracles/bin/python for pinned CPU tensor tests")
class TestCpuStateRestoration(unittest.TestCase):
    def tensors(self):
        keys = ["base_model.model.classifier." + name for name in ("dense.weight", "dense.bias", "out_proj.weight", "out_proj.bias")]
        keys += ["base_model.model.synthetic.lora_A.weight", "base_model.model.synthetic.lora_B.weight"]
        saved = {key: torch.tensor([.125, -.75], dtype=torch.float16) for key in keys}
        return saved, {key: value.to(torch.float32) for key, value in saved.items()}

    def test_exact_fp16_checkpoint_to_fp32_runtime_including_trained_head(self):
        saved, restored = self.tensors(); report = runtime.compare_trained_tensors(saved, restored, torch)
        self.assertEqual(len(report), 6)
        self.assertTrue(all(row["checkpoint_dtype"] == "torch.float16" and row["runtime_dtype"] == "torch.float32" for row in report.values()))
        self.assertTrue(all(row["actual_fp32_sha256"] == row["expected_fp32_sha256"] for row in report.values()))

    def test_missing_random_corrupt_and_nonfinite_trained_state_rejected(self):
        for mode in ("missing", "random_head", "nan", "lora", "wrong_runtime_dtype"):
            with self.subTest(mode=mode):
                saved, restored = self.tensors(); key = "base_model.model.classifier.dense.bias"
                if mode == "missing": restored.pop(key)
                elif mode == "random_head": restored[key] = torch.zeros(2)
                elif mode == "nan": saved[key][0] = float("nan")
                elif mode == "lora": restored["base_model.model.synthetic.lora_A.weight"][0] += 1
                else: restored[key] = saved[key]
                with self.assertRaises(ValueError): runtime.compare_trained_tensors(saved, restored, torch)

    def test_all_trained_lora_routes_and_active_saved_classifier_required(self):
        modules = []; saved = {}
        for i in range(198):
            name = f"base_model.model.synthetic.layer{i}"
            modules.append((name, SimpleNamespace(lora_A={"default": object()}, lora_B={"default": object()},
                disable_adapters=False, merged=False, active_adapters=["default"])))
            saved[name + ".lora_A.weight"] = object(); saved[name + ".lora_B.weight"] = object()
        head = SimpleNamespace(active_adapter="default", disable_adapters=False, modules_to_save={"default": object()})
        model = SimpleNamespace(base_model=SimpleNamespace(model=SimpleNamespace(classifier=head)),
            active_adapters=["default"], named_modules=lambda: iter(modules), config=SimpleNamespace(position_embedding_type="rotary"))
        self.assertEqual(runtime.audit_active_routes(model, saved)["lora_module_count"], 198)
        head.disable_adapters = True
        with self.assertRaises(ValueError): runtime.audit_active_routes(model, saved)
        head.disable_adapters = False; modules[0][1].merged = True
        with self.assertRaises(ValueError): runtime.audit_active_routes(model, saved)
        modules[0][1].merged = False; saved.pop(next(iter(saved)))
        with self.assertRaises(ValueError): runtime.audit_active_routes(model, saved)

    def test_source_preprocessing_with_fake_model_and_tokenizer_only(self):
        spec = importlib.util.spec_from_file_location("synthetic_native_gfp_preprocessing", SCRIPTS.parent / runtime.NATIVE_SOURCE)
        native = importlib.util.module_from_spec(spec); spec.loader.exec_module(native)
        calls = []
        def tokenizer(formatted, **kwargs):
            calls.append((formatted, kwargs)); return {"input_ids": torch.tensor([[1, 2], [3, 4]])}
        def model(**kwargs):
            self.assertFalse(torch.is_grad_enabled()); self.assertEqual(kwargs["input_ids"].device.type, "cpu")
            return SimpleNamespace(logits=torch.tensor([[1.25], [-.5]], dtype=torch.float32))
        oracle = runtime.NativeOracle(tokenizer, model, native, torch)
        self.assertEqual(oracle.predict(["AC", "DE"]), [1.25, -.5])
        self.assertEqual(calls, [(["A#C#", "D#E#"], {"return_tensors": "pt", "padding": True, "truncation": True, "max_length": 1024})])
        with self.assertRaises(ValueError): oracle.predict(["A#C#"])


class TestWeightsOnlyBoundary(unittest.TestCase):
    def test_native_loads_forced_cpu_weights_only_and_original_restored(self):
        calls = []
        def original(*args, **kwargs): calls.append((args, kwargs)); return {"synthetic": True}
        fake = SimpleNamespace(load=original)
        with runtime.weights_only_cpu(fake):
            fake.load("synthetic_checkpoint", map_location="cuda:7")
            self.assertEqual(calls[-1][1], {"map_location": "cpu", "weights_only": True})
            with self.assertRaises(ValueError): fake.load("synthetic_checkpoint", weights_only=False)
        self.assertIs(fake.load, original)


if __name__ == "__main__": unittest.main()
