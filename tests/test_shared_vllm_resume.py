"""Synthetic-only checks for provenance-preserving shared-server continuation."""
import copy
from fractions import Fraction
from collections import Counter
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
import tempfile
import threading
import time
import unittest
from unittest import mock

SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS))
import shared_vllm_resume as resume
import run_shared_vllm_evaluations as launcher


HELPER = '''from pathlib import Path
import json,hashlib
ROOT=Path(__file__).resolve().parents[1]
calls=[]
def digest(v):
 return hashlib.sha256(json.dumps(v,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def read_frozen_config(p):
 s=json.loads(p.read_text());return s,[json.loads(l) for l in (ROOT/s['input_file']).read_text().splitlines()]
def request_record(c,s):
 p={'model':s['model'],'messages':c['messages'],**s['generation']}
 return {**{k:c[k] for k in ('task','case_id','variant','split')},'request_sha256':digest(p),'payload':p,'supplied_fields':['sequence'],'image_sha256':[],'supplied_images':[]}
def call(endpoint,payload=None,timeout=900):
 if payload is None:return 200,{'data':[{'id':'Qwen/Qwen3.8-27B'}]}
 calls.append(payload)
 return 200,{'model':payload['model'],'choices':[{'message':{'content':'0.5'},'finish_reason':'stop'}],'usage':{'prompt_tokens':100,'completion_tokens':3,'total_tokens':103}}
'''


class Fixture:
    def __init__(self, root, count=3):
        self.root = Path(root)
        self.project = self.root / "project"
        (self.project / "scripts").mkdir(parents=True)
        self.helper = self.project / "scripts/frozen_runner.py"
        self.helper.write_text(HELPER)
        self.cases = [{"task": "P08", "case_id": "synthetic-" + str(i), "variant": "SYNTHETIC_ONLY",
                       "split": "synthetic", "messages": [{"role": "user", "content": "Neutral synthetic sequence slot " + str(i)}]} for i in range(count)]
        inp = self.project / "inputs.jsonl"
        inp.write_text("".join(json.dumps(c) + "\n" for c in self.cases))
        self.settings = {"run_id": "synthetic-run", "model": resume.MODEL, "model_revision": resume.REVISION,
                         "approved_task_ids": ["P08"], "variant": "SYNTHETIC_ONLY", "input_file": "inputs.jsonl",
                         "generation": {"max_tokens": 4096, "seed": 42, "n": 1, "temperature": 1.0,
                                        "top_p": 0.95, "top_k": 20, "chat_template_kwargs": {"enable_thinking": True, "reasoning_effort": "medium"}}}
        self.config = self.project / "config.json"
        self.config.write_text(json.dumps(self.settings))
        identity_path = self.root / "synthetic_server_identity.json"
        identity_path.write_text(json.dumps({"model": resume.MODEL, "revision": resume.REVISION, "dtype": "bfloat16",
                                            "tensor_parallel_size": 1, "max_model_len": 65536, "max_num_seqs": 32,
                                            "endpoint": "http://127.0.0.1:8989/v1", "gpu_uuids": ["GPU-synthetic"]}))
        declared_endpoint = {"endpoint_id": "synthetic", "endpoint": "http://127.0.0.1:8989/v1",
                             "server_identity_file": str(identity_path), "server_identity_sha256": resume.file_sha(identity_path),
                             "tensor_parallel_size": 1, "max_inflight": 32, "max_model_len": 65536,
                             "length_limits": [{"max_prompt_tokens": 1536, "max_inflight": 32},
                                               {"max_prompt_tokens": 45056, "max_inflight": 8}]}
        self.endpoint = resume.validate_endpoint(declared_endpoint, live=False)
        self.entry = {"task_id": "P08", "project_root": str(self.project), "config_path": "config.json", "config_sha256": resume.file_sha(self.config),
                      "runner": "scripts/frozen_runner.py", "runner_sha256": resume.file_sha(self.helper), "run_id": "synthetic-run",
                      "generation_sha256": resume.digest(self.settings["generation"]), "case_count": count,
                      "input_sha256": resume.file_sha(inp), "minimum_context_tokens": 32768}
        self.context = self.project / "context.json"
        self.context.write_text(json.dumps({"case_count": count, "max_prompt_tokens": 100, "output_budget": 4096,
                                            "all_prompts_fit": True, "per_case": [{"case_id": c["case_id"], "prompt_tokens": 100} for c in self.cases]}))
        self.amendment_path = self.root / "amendment.json"
        self.amendment = {"adapter_files_sha256": {str(Path(resume.__file__)): resume.file_sha(resume.__file__)},
                          "endpoints": [declared_endpoint], "run_context_checks": {"synthetic-run": {"path": str(self.context), "sha256": resume.file_sha(self.context)}}}
        self.run_dir = self.project / "results/runs/synthetic-run"
        self.refresh_amendment()

    def refresh_amendment(self):
        self.amendment_path.write_text(json.dumps(self.amendment))
        self.amendment_sha = resume.file_sha(self.amendment_path)

    def state(self):
        return resume.Run(self.entry, self.root, self.amendment, self.amendment_path, self.amendment_sha)

    def name(self, index):
        c = self.cases[index]
        return resume.digest([c["task"], c["variant"], c["case_id"]]) + ".json"

    def request(self, index):
        return self.state().helper.request_record(self.cases[index], self.settings)

    def save_request(self, index):
        p = self.run_dir / "requests" / self.name(index)
        resume.atomic_write(p, self.request(index), exclusive=True)
        return p

    def save_response(self, index, *, finish="stop", text="0.5", status="completed"):
        request = self.request(index)
        c = self.cases[index]
        record = {**{k: c[k] for k in ("task", "case_id", "variant", "split")},
                  "model": resume.MODEL, "model_revision": resume.REVISION, "request_sha256": request["request_sha256"],
                  "status": status, "http_status": 200, "text": text, "finish_reason": finish,
                  "response": {"model": resume.MODEL, "choices": [{"message": {"content": text}, "finish_reason": finish}]}}
        path = self.run_dir / "responses" / self.name(index)
        resume.atomic_write(path, record, exclusive=True)
        return path

    def old_manifest(self):
        value = {"configuration": self.settings, "configuration_sha256": self.entry["config_sha256"],
                 "runner_sha256": self.entry["runner_sha256"], "case_contract_sha256": resume.digest(self.cases),
                 "planned_cases": len(self.cases), "model_selection_on_test": False,
                 "solver_tools": [], "answer_keys_available_to_solver": False,
                 "server": {"pid": 123, "historical": True}}
        resume.atomic_write(self.run_dir / "run_manifest.json", value, exclusive=True)

    def negative(self, index):
        path = self.run_dir / "requests" / self.name(index)
        receipt = {"schema_version": 1, "drain_protocol_version": 2, "kind": "shared_vllm_negative_execution_drain", "stage": "drained_and_job_terminal",
                   "old_job_id": "12345", "terminal_accounting": {"job_id": "12345", "state": "CANCELLED", "exit_code": "0:15"},
                   "proof": {k: True for k in ("api_stopped_before_new_requests", "api_killed_while_stopped", "api_dead_before_client_kill", "api_dead_before_job_cancellation", "client_killed_while_stopped", "all_pre_stop_requests_paired", "executor_stopped_before_client_stop", "executor_stopped_until_client_killed", "executor_killed_while_stopped", "executor_killed_after_client_dead")},
                   "request_records": [{"project_root": str(self.project), "run_id": "synthetic-run", "filename": self.name(index),
                                        "request_file_sha256": resume.file_sha(path), "payload_sha256": self.request(index)["request_sha256"],
                                        "request_created_after_api_stop": True, "server_stopped_at_creation": True}]}
        p = self.root / "negative.json"
        p.write_text(json.dumps(receipt))
        self.amendment["negative_execution_receipts"] = [{"path": str(p), "sha256": resume.file_sha(p)}]
        self.refresh_amendment()
        return p


class ResumeTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.f = Fixture(self.temp.name)

    def prepare(self):
        state = self.f.state()
        state.acquire()
        self.addCleanup(state.close)
        state.prepare([self.f.endpoint])
        return state

    def test_resume_preserves_old_bytes_and_never_resamples_ambiguous_or_truncated(self):
        self.f.old_manifest()
        self.f.save_request(0)
        self.f.save_response(0, finish="length", text="")
        self.f.save_request(1)
        before = resume.raw_inventory(self.f.run_dir)
        state = self.prepare()
        pending = list(state.pending())
        self.assertEqual([c[0]["case_id"] for c in pending], ["synthetic-2"])
        state.dispatch(*pending[0], self.f.endpoint, threading.Event())
        result = state.finish()
        for name, expected in before.items():
            self.assertEqual(resume.file_sha(self.f.run_dir / name), expected)
        self.assertEqual(result["statuses"], {"completed": 2, "interrupted_unknown_completion": 1})
        value = resume.validate_resume_provenance(self.f.run_dir, self.f.settings, self.f.cases, require_terminal=True)
        self.assertEqual(value["dispatched_files"], [self.f.name(2)])
        self.assertEqual(value["ambiguous_files"], [self.f.name(1)])

    def test_new_manifest_names_actual_adapter_and_original_payload_source(self):
        state = self.prepare()
        manifest = resume.read(self.f.run_dir / "run_manifest.json")
        self.assertEqual(manifest["runner_sha256"], resume.file_sha(resume.__file__))
        self.assertEqual(manifest["frozen_runner_sha256"], self.f.entry["runner_sha256"])
        self.assertEqual(manifest["configuration"], self.f.settings)

    def test_proven_unexecuted_request_can_execute_without_rewriting_request(self):
        path = self.f.save_request(1)
        old = path.read_bytes()
        self.f.negative(1)
        state = self.prepare()
        pending = dict((c["case_id"], (c, name)) for c, name in state.pending())
        state.dispatch(*pending["synthetic-1"], self.f.endpoint, threading.Event())
        self.assertEqual(path.read_bytes(), old)
        proof = resume.validate_resume_provenance(self.f.run_dir, self.f.settings, self.f.cases)
        self.assertEqual(proof["dispatched_files"], [self.f.name(1)])
        receipt = resume.read(self.f.run_dir / resume.RECEIPTS / self.f.name(1))
        self.assertEqual(receipt["negative_execution_receipt_sha256"], self.f.amendment["negative_execution_receipts"][0]["sha256"])

    def test_negative_exception_rejects_merely_stopped_api(self):
        self.f.save_request(1)
        path = self.f.negative(1)
        value = resume.read(path)
        value["proof"]["api_killed_while_stopped"] = False
        path.write_text(json.dumps(value))
        self.f.amendment["negative_execution_receipts"][0]["sha256"] = resume.file_sha(path)
        self.f.refresh_amendment()
        with self.assertRaises(resume.ResumeError):
            self.f.state()

    def test_negative_exception_rejects_changed_request(self):
        path = self.f.save_request(1)
        self.f.negative(1)
        path.write_text(path.read_text() + " ")
        with self.assertRaises(resume.ResumeError):
            self.prepare()

    def test_legacy_negative_receipt_cannot_append_original_run(self):
        self.f.save_request(1)
        path = self.f.negative(1)
        value = resume.read(path)
        value.pop("drain_protocol_version")
        path.write_text(json.dumps(value))
        self.f.amendment["negative_execution_receipts"][0]["sha256"] = resume.file_sha(path)
        self.f.refresh_amendment()
        with self.assertRaises(resume.ResumeError):
            self.f.state()

    def test_derived_continuation_preserves_partial_native_lock_and_all_parent_bytes(self):
        self.f.old_manifest()
        self.f.save_request(0)
        self.f.save_response(0)
        self.f.save_request(1)
        negative_path = self.f.negative(1)
        lock_files = {"run_manifest.json": resume.file_sha(self.f.run_dir / "run_manifest.json")}
        for i in range(3):
            for kind in ("requests", "responses"):
                name = kind + "/" + self.f.name(i)
                path = self.f.run_dir / name
                lock_files[name] = resume.file_sha(path) if path.exists() else None
        resume.atomic_write(self.f.run_dir / "scoring_output_lock.json", {"files_sha256": lock_files, "contract_sha256": resume.digest(lock_files)})
        resume.atomic_write(self.f.run_dir / "scores.json", {"planned": 3, "completed": 1, "metric": "synthetic fixture only"})
        resume.atomic_write(self.f.run_dir / "completion.json", {"generation_exit_code": -9, "scoring_exit_code": 0,
                           "run_manifest_sha256": resume.file_sha(self.f.run_dir / "run_manifest.json"),
                           "scores_sha256": resume.file_sha(self.f.run_dir / "scores.json")})
        temporary_request = self.f.run_dir / "requests/interrupted.json.tmp"
        temporary_request.write_text("an interrupted atomic write, never dispatched")
        snapshot = {p.relative_to(self.f.run_dir).as_posix(): resume.file_sha(p) for p in self.f.run_dir.rglob("*") if p.is_file()}
        derived = self.f.run_dir.with_name("synthetic-run_shared_continuation_v1")
        self.f.amendment["continuation_run_directories"] = {"synthetic-run": str(derived)}
        self.f.amendment["continuation_source_snapshots"] = {"synthetic-run": {"source_run_directory": str(self.f.run_dir), "files_sha256": snapshot}}
        negative = resume.read(negative_path)
        negative.pop("schema_version")
        negative.pop("drain_protocol_version")
        negative_path.write_text(json.dumps(negative))
        self.f.amendment["negative_execution_receipts"][0]["sha256"] = resume.file_sha(negative_path)
        self.f.refresh_amendment()
        state = self.prepare()
        self.assertEqual(state.run, derived)
        self.assertEqual([c["case_id"] for c, _ in state.pending()], ["synthetic-1", "synthetic-2"])
        for case, name in state.pending():
            state.dispatch(case, name, self.f.endpoint, threading.Event())
        state.finish()
        proof = resume.validate_resume_provenance(derived, self.f.settings, self.f.cases, require_terminal=True)
        self.assertEqual(proof["status_counts"], {"completed": 3})
        self.assertEqual(proof["parent_scoring_output_lock_sha256"], snapshot["scoring_output_lock.json"])
        for name, expected in snapshot.items():
            self.assertEqual(resume.file_sha(self.f.run_dir / name), expected)
        self.assertFalse((self.f.run_dir / "responses" / self.f.name(1)).exists())
        self.assertFalse((derived / "requests/interrupted.json.tmp").exists())

    def test_existing_worker_lock_blocks_handoff_before_provenance_writes(self):
        first = self.f.state()
        first.acquire()
        self.addCleanup(first.close)
        second = self.f.state()
        with self.assertRaises(resume.ResumeError):
            second.acquire()
        self.assertFalse((self.f.run_dir / resume.SIDECAR).exists())

    def test_scored_output_lock_prevents_extension(self):
        self.f.run_dir.mkdir(parents=True)
        (self.f.run_dir / "scoring_output_lock.json").write_text("{}")
        with self.assertRaises(resume.ResumeError):
            self.prepare()

    def test_old_manifest_configuration_mismatch_refuses_resume(self):
        self.f.old_manifest()
        path = self.f.run_dir / "run_manifest.json"
        value = resume.read(path)
        value["configuration"]["generation"]["max_tokens"] = 16384
        path.write_text(json.dumps(value))
        with self.assertRaises(resume.ResumeError):
            self.prepare()

    def test_mutated_retained_record_is_detected(self):
        request = self.f.save_request(0)
        self.f.save_response(0)
        self.prepare()
        request.write_text(request.read_text() + " ")
        with self.assertRaises(resume.ResumeError):
            resume.validate_resume_provenance(self.f.run_dir, self.f.settings, self.f.cases)

    def test_new_response_without_dispatch_provenance_is_rejected(self):
        self.prepare()
        self.f.save_request(0)
        self.f.save_response(0)
        with self.assertRaises(resume.ResumeError):
            resume.validate_resume_provenance(self.f.run_dir, self.f.settings, self.f.cases)

    def test_extra_response_slot_is_rejected(self):
        self.prepare()
        resume.atomic_write(self.f.run_dir / "responses/extra.json", {})
        with self.assertRaises(resume.ResumeError):
            resume.validate_resume_provenance(self.f.run_dir, self.f.settings, self.f.cases)

    def test_claim_without_request_is_retained_as_ambiguous(self):
        state = self.prepare()
        c = self.f.cases[0]
        receipt = {"segment_id": state.segment_id, "amendment_sha256": self.f.amendment_sha,
                   "filename": self.f.name(0), "case_id": c["case_id"],
                   "request_sha256": self.f.request(0)["request_sha256"], "endpoint_id": "synthetic",
                   "server_identity_sha256": self.f.endpoint["server_identity_sha256"], "status": "claimed", "prompt_tokens": 100,
                   "admission_weight": "1/32"}
        resume.atomic_write(self.f.run_dir / resume.RECEIPTS / self.f.name(0), receipt)
        proof = resume.validate_resume_provenance(self.f.run_dir, self.f.settings, self.f.cases)
        self.assertEqual(proof["ambiguous_files"], [self.f.name(0)])
        self.assertNotIn(c["case_id"], [case["case_id"] for case, _ in state.pending()])

    def test_terminal_proof_requires_generation_marker(self):
        state = self.prepare()
        with self.assertRaises(resume.ResumeError):
            resume.validate_resume_provenance(self.f.run_dir, self.f.settings, self.f.cases, require_terminal=True)
        state.finish()
        resume.validate_resume_provenance(self.f.run_dir, self.f.settings, self.f.cases, require_terminal=True)

    def test_context_review_must_match_full_order_and_output_budget(self):
        context = resume.read(self.f.context)
        context["per_case"].reverse()
        self.f.context.write_text(json.dumps(context))
        self.f.amendment["run_context_checks"]["synthetic-run"]["sha256"] = resume.file_sha(self.f.context)
        self.f.refresh_amendment()
        with self.assertRaises(resume.ResumeError):
            self.f.state()

    def test_length_aware_capacity_uses_exact_fractional_weights(self):
        self.assertEqual(resume.admission_weight(self.f.endpoint, 1536), Fraction(1, 32))
        self.assertEqual(resume.admission_weight(self.f.endpoint, 1537), Fraction(1, 8))
        self.assertEqual(16 * resume.admission_weight(self.f.endpoint, 100) + 4 * resume.admission_weight(self.f.endpoint, 40000), 1)
        with self.assertRaises(resume.ResumeError):
            resume.admission_weight(self.f.endpoint, 45057)

    def test_amendment_protocol_changes_fail_closed(self):
        self.f.amendment.update(schema_version=1, kind="shared_vllm_infrastructure_amendment", execution_authorized=True,
                                infrastructure_only=True, scientific_protocol_changes=["more output tokens"], model=resume.MODEL, model_revision=resume.REVISION)
        self.f.refresh_amendment()
        with self.assertRaises(resume.ResumeError):
            launcher.load_amendment(self.f.root, self.f.amendment_path, self.f.amendment_sha)

    def test_check_only_does_not_create_run_directory(self):
        with mock.patch.object(launcher, "load_amendment", return_value=(self.f.amendment, [self.f.endpoint], [self.f.entry])):
            report = launcher.run(self.f.root, self.f.amendment_path, self.f.amendment_sha, check_only=True)
        self.assertEqual(report["stage"], "checked_not_executed")
        self.assertFalse(self.f.run_dir.exists())

    def test_source_plan_uses_worker_context_when_entry_has_no_context_field(self):
        plan = self.f.root / "source_plan.json"
        plan.write_text(json.dumps({"execution_authorized": True, "workers": [{"max_model_len": 32768, "entries": [self.f.entry]}]}))
        evidence = self.f.root / "capacity_evidence.json"
        evidence.write_text('{"synthetic_only":true}')
        self.f.amendment.update(schema_version=1, kind="shared_vllm_infrastructure_amendment", execution_authorized=True,
                                infrastructure_only=True, scientific_protocol_changes=[], model=resume.MODEL, model_revision=resume.REVISION,
                                capacity_evidence_files=[{"path": str(evidence), "sha256": resume.file_sha(evidence)}],
                                source_plans=[{"path": str(plan), "sha256": resume.file_sha(plan)}])
        self.f.amendment["adapter_files_sha256"] = {str(Path(m.__file__).resolve()): resume.file_sha(m.__file__) for m in (resume, launcher)}
        self.f.refresh_amendment()
        _, _, entries = launcher.load_amendment(Path('/'), self.f.amendment_path, self.f.amendment_sha)
        self.assertEqual(entries[0]["minimum_context_tokens"], 32768)

    def test_six_frozen_plan_shapes_resolve_runner_path_and_worker_context(self):
        self.f.settings["runner"] = self.f.entry["runner"]
        self.f.config.write_text(json.dumps(self.f.settings))
        config_sha = resume.file_sha(self.f.config)
        for name in ("extended_fast", "extended_bulk", "p28", "p29", "p16", "deepfri"):
            with self.subTest(plan=name):
                entry = {**self.f.entry, "config_sha256": config_sha}
                worker = {"worker_id": name, "max_model_len": 65536 if name == "p16" else 32768, "port": 8026}
                if name.startswith("extended"):
                    entry.pop("runner")
                else:
                    entry["max_model_len"] = worker["max_model_len"]
                    entry["port"] = worker["port"]
                before = copy.deepcopy(entry)
                normalized = launcher.normalize_plan_entry(self.f.root, entry, worker)
                self.assertEqual(entry, before)
                self.assertEqual(normalized["runner"], self.f.entry["runner"])
                self.assertEqual(normalized["runner_sha256"], self.f.entry["runner_sha256"])
                self.assertEqual(normalized["minimum_context_tokens"], worker["max_model_len"])
                if name.startswith("extended"):
                    self.assertEqual(normalized["inherited_field_sources"]["runner"], "frozen_configuration")

    def test_normalized_worker_runner_must_match_pinned_frozen_configuration(self):
        entry = dict(self.f.entry)
        entry.pop("runner")
        self.f.settings["runner"] = "scripts/frozen_runner.py"
        self.f.config.write_text(json.dumps(self.f.settings))
        entry["config_sha256"] = resume.file_sha(self.f.config)
        normalized = launcher.normalize_plan_entry(self.f.root, entry, {"max_model_len": 32768, "runner": "scripts/frozen_runner.py"})
        self.assertEqual(normalized["inherited_field_sources"]["runner"], "worker")
        with self.assertRaises(resume.ResumeError):
            launcher.normalize_plan_entry(self.f.root, entry, {"max_model_len": 32768, "runner": "scripts/other.py"})

    def test_missing_frozen_entry_field_fails_explicitly(self):
        entry = dict(self.f.entry)
        entry.pop("case_count")
        with self.assertRaisesRegex(resume.ResumeError, "required field: case_count"):
            launcher.normalize_plan_entry(self.f.root, entry, {"max_model_len": 32768})

    def test_full_pool_mixed_lengths_never_exceeds_fractional_capacity(self):
        fixture = Fixture(Path(self.temp.name) / "mixed", count=40)
        context = resume.read(fixture.context)
        for i, item in enumerate(context["per_case"]):
            item["prompt_tokens"] = 40000 if i < 20 else 100
        context["max_prompt_tokens"] = 40000
        fixture.context.write_text(json.dumps(context))
        fixture.amendment["run_context_checks"]["synthetic-run"]["sha256"] = resume.file_sha(fixture.context)
        fixture.refresh_amendment()
        mutex = threading.Lock()
        used, peak = [Fraction(0)], [Fraction(0)]
        original = resume.Run.dispatch
        def measured(state, case, name, endpoint, stopped):
            weight = resume.admission_weight(endpoint, state.prompt_tokens[case["case_id"]])
            with mutex:
                used[0] += weight
                peak[0] = max(peak[0], used[0])
                self.assertLessEqual(used[0], 1)
            try:
                time.sleep(0.01)
                return original(state, case, name, endpoint, stopped)
            finally:
                with mutex:
                    used[0] -= weight
        with mock.patch.object(launcher, "load_amendment", return_value=(fixture.amendment, [fixture.endpoint], [fixture.entry])), mock.patch.object(resume.Run, "dispatch", measured), mock.patch.object(launcher, "require_idle_endpoint"):
            result = launcher.run(fixture.root, fixture.amendment_path, fixture.amendment_sha)
        self.assertEqual(result["generation_exit_code"], 0)
        self.assertGreater(peak[0], Fraction(1, 2))
        self.assertLessEqual(peak[0], 1)
        proof = resume.validate_resume_provenance(fixture.run_dir, fixture.settings, fixture.cases, require_terminal=True)
        self.assertEqual(proof["status_counts"], {"completed": 40})

    def test_waiting_long_case_starts_before_continuous_short_stream_finishes(self):
        endpoint = copy.deepcopy(self.f.endpoint)
        endpoint["length_limits"][-1]["max_inflight"] = 1
        events, lock = [], threading.Lock()
        short_finished = [0]
        class SchedulerOnlyRun:
            def __init__(state, entry, *args):
                state.entry = {**entry, "minimum_context_tokens": 32768}
                state.settings = {"run_id": entry["run_id"]}
                state.cases = [{"task": "synthetic", "variant": entry["run_id"],
                                "case_id": entry["run_id"] + "-" + str(i)} for i in range(entry["count"])]
                state.prompt_tokens = {c["case_id"]: entry["prompt_tokens"] for c in state.cases}
                state.helper = type("SyntheticMetadataClient", (), {"call": staticmethod(lambda *a, **k: (200, {"data": [{"id": resume.MODEL}]}))})
            def inventory(state):
                return Counter(undispatched=len(state.cases))
            def acquire(state):
                pass
            def close(state):
                pass
            def prepare(state, endpoints):
                pass
            def finish_if_complete(state):
                pass
            def pending(state):
                return ((c, c["case_id"]) for c in state.cases)
            def dispatch(state, case, name, endpoint, stopped):
                with lock:
                    if state.entry["run_id"] == "long":
                        events.append(("long_started", short_finished[0]))
                time.sleep(0.003)
                with lock:
                    if state.entry["run_id"] == "short":
                        short_finished[0] += 1
            def finish(state):
                return {"run_id": state.entry["run_id"], "generation_exit_code": 0}
        entries = [{"run_id": "short", "task_id": "synthetic", "project_root": str(self.f.project), "count": 200, "prompt_tokens": 100},
                   {"run_id": "long", "task_id": "synthetic", "project_root": str(self.f.project), "count": 1, "prompt_tokens": 40000}]
        for entry in entries:
            entry["minimum_context_tokens"] = 32768
        with mock.patch.object(launcher, "load_amendment", return_value=(self.f.amendment, [endpoint], entries)), mock.patch.object(launcher, "Run", SchedulerOnlyRun), mock.patch.object(launcher, "require_idle_endpoint"):
            result = launcher.run(self.f.root, self.f.amendment_path, self.f.amendment_sha)
        self.assertEqual(result["generation_exit_code"], 0)
        self.assertEqual(short_finished[0], 200)
        self.assertEqual(len(events), 1)
        self.assertLess(events[0][1], 200)
        self.assertLessEqual(events[0][1], 1)


if __name__ == "__main__":
    unittest.main()
