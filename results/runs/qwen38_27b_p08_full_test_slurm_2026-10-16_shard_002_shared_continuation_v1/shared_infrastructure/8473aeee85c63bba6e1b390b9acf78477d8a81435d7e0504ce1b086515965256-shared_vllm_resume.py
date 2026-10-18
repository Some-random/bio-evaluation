"""Additive infrastructure continuation; original v2 provenance is immutable.

Model-facing configuration and payload construction remain owned by the frozen
native runner.  This module changes only the HTTP queue and transport timeout.
"""
from __future__ import annotations

from collections import Counter
from fractions import Fraction
import hashlib
import importlib.util
from pathlib import Path
import socket
import threading
import time
import uuid

PARENT_CORE_SHA256 = "58a753c4322f17e0fcec4a8fb41a5e6fb57af27bd7268bb4832fa25cc813699b"
_PARENT_PATH = Path(__file__).resolve().parents[2] / "scripts/shared_vllm_resume.py"
if hashlib.sha256(_PARENT_PATH.read_bytes()).hexdigest() != PARENT_CORE_SHA256:
    raise RuntimeError("The immutable v2 provenance implementation changed")
_spec = importlib.util.spec_from_file_location("immutable_shared_vllm_resume_v2", _PARENT_PATH)
v2 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(v2)
for _name in ("MODEL", "REVISION", "ResumeError", "stamp", "digest", "file_sha", "read",
              "atomic_write", "local_path", "frozen_helper", "raw_inventory", "negative_execution_records"):
    globals()[_name] = getattr(v2, _name)

SIDECAR = "shared_vllm_saturation_amendment.json"
SEGMENTS = "shared_vllm_saturation_segments"
RECEIPTS = "shared_vllm_saturation_dispatch"
COMPLETION = "shared_vllm_saturation_generation_completion.json"
PROGRESS = "shared_vllm_saturation_progress.json"
CHECKPOINT = "shared_vllm_saturation_parent_checkpoint.json"
POLICY = "vllm_native_bounded_queue"
TRANSPORT_TIMEOUT = 14400


def _parent(amendment):
    source = amendment.get("parent_amendment", {})
    if not source.get("path") or file_sha(source["path"]) != source.get("sha256"):
        raise ResumeError("The exact original execution amendment must be pinned")
    value = read(source["path"])
    if value.get("model") not in (None, MODEL) or value.get("model_revision") not in (None, REVISION):
        raise ResumeError("The parent amendment changes the checkpoint")
    return value, source["sha256"]


def validate_endpoint(entry, model=MODEL, revision=REVISION, *, live=True):
    # Reuse original identity/PID/GPU/context checks with an informational
    # capacity descriptor.  Native queue limits are independently checked below.
    if (entry.get("scheduler_policy") != POLICY
            or type(entry.get("queue_limit")) is not int
            or entry["queue_limit"] != entry.get("max_inflight")
            or not 1 <= entry["queue_limit"] <= 256
            or type(entry.get("max_num_seqs")) is not int
            or not 1 <= entry["max_num_seqs"] <= 256):
        raise ResumeError("Explicit native server and HTTP queue capacities are required")
    adapted = {**entry, "max_inflight": min(entry["queue_limit"], entry["max_num_seqs"]),
               "length_limits": [{"max_prompt_tokens": entry["max_model_len"] - 4096,
                                  "max_inflight": min(entry["queue_limit"], entry["max_num_seqs"])}]}
    verified = v2.validate_endpoint(adapted, model, revision, live=live)
    if verified["server_identity"].get("max_num_seqs") != entry["max_num_seqs"]:
        raise ResumeError("Declared native sequence capacity differs from the actual server")
    return {**entry, "server_identity": verified["server_identity"]}


def admission_weight(endpoint, prompt_tokens):
    """Informational HTTP occupancy only; the dispatcher uses native queuing."""
    if prompt_tokens + 4096 > endpoint["max_model_len"]:
        raise ResumeError("A complete unchanged prompt exceeds serving context")
    return Fraction(1, endpoint["queue_limit"])


def _parent_files(run_dir):
    result = raw_inventory(run_dir)
    for name in (v2.SIDECAR, "shared_vllm_generation_completion.json", "progress.json", v2.FORK_MANIFEST):
        p = Path(run_dir) / name
        if p.exists():
            result[name] = file_sha(p)
    for kind in (v2.SEGMENTS, v2.RECEIPTS):
        for p in (Path(run_dir) / kind).glob("*.json"):
            result[kind + "/" + p.name] = file_sha(p)
    return result


def _check_checkpoint(run_dir, sidecar):
    checkpoint_path = Path(run_dir) / CHECKPOINT
    if file_sha(checkpoint_path) != sidecar["parent_checkpoint_sha256"]:
        raise ResumeError("The immutable original-execution checkpoint changed")
    checkpoint = read(checkpoint_path)
    for name, expected in checkpoint["files_sha256"].items():
        if file_sha(local_path(run_dir, name)) != expected:
            raise ResumeError("An original execution artifact changed: " + name)
    for kind in (v2.SEGMENTS, v2.RECEIPTS):
        if {kind + "/" + p.name for p in (Path(run_dir) / kind).glob("*.json")} != {
                name for name in checkpoint["files_sha256"] if name.startswith(kind + "/")}:
            raise ResumeError("The closed parent producer added or lost provenance records")
    return checkpoint


def validate_resume_provenance(run_dir, settings, cases, *, require_terminal=False):
    """Verify both producer generations and every exact frozen request once."""
    run_dir = Path(run_dir)
    if not (run_dir / SIDECAR).exists():
        return v2.validate_resume_provenance(run_dir, settings, cases, require_terminal=require_terminal)
    sidecar = read(run_dir / SIDECAR)
    if sidecar.get("schema_version") != 1 or sidecar.get("run_id") != settings["run_id"]:
        raise ResumeError("Unknown saturation provenance schema/run")
    if file_sha(run_dir / v2.SIDECAR) != sidecar["parent_sidecar_sha256"]:
        raise ResumeError("Original v2 sidecar changed")
    old = read(run_dir / v2.SIDECAR)
    amendment_path = Path(sidecar["amendment_path"])
    if file_sha(amendment_path) != sidecar["amendment_sha256"]:
        raise ResumeError("Saturation execution amendment changed")
    amendment = read(amendment_path)
    if (sidecar.get("adapter_files_sha256") != amendment.get("adapter_files_sha256")
            or amendment.get("adapter_files_sha256", {}).get(str(Path(__file__).resolve())) != file_sha(__file__)):
        raise ResumeError("The actual saturation core is not pinned by its execution amendment")
    parent, parent_sha = _parent(amendment)
    if parent_sha != old["amendment_sha256"] or parent_sha != sidecar["parent_amendment_sha256"]:
        raise ResumeError("The additive chain is attached to a different original execution")
    if (amendment.get("execution_variant") != "saturation_native_queue_v1"
            or amendment.get("scheduler_policy") != POLICY
            or amendment.get("scientific_protocol_changes") != []
            or amendment.get("transport_timeout_seconds") != TRANSPORT_TIMEOUT):
        raise ResumeError("Saturation amendment changes the frozen scientific protocol")
    for pins in (old["adapter_files_sha256"], sidecar["adapter_files_sha256"]):
        for path, expected in pins.items():
            if file_sha(path) != expected:
                raise ResumeError("An immutable producer implementation changed")
    project = Path(old["project_root"])
    if (read(local_path(project, old["config_path"])) != settings
            or file_sha(local_path(project, old["config_path"])) != old["frozen_configuration_sha256"]
            or old["case_contract_sha256"] != digest(cases)):
        raise ResumeError("Frozen configuration or exact ordered cases changed")
    checkpoint = _check_checkpoint(run_dir, sidecar)
    if (checkpoint.get("run_id") != settings["run_id"]
            or checkpoint.get("parent_amendment_sha256") != parent_sha
            or checkpoint.get("parent_sidecar_sha256") != sidecar["parent_sidecar_sha256"]
            or checkpoint.get("parent_proof", {}).get("ambiguous_files") != []
            or checkpoint.get("parent_proof", {}).get("all_saved_responses_verified") is not True):
        raise ResumeError("The parent checkpoint does not attest a clean native execution boundary")
    baseline = {k: v for k, v in checkpoint["files_sha256"].items()
                if k == "run_manifest.json" or k.startswith(("requests/", "responses/"))}
    manifest = read(run_dir / "run_manifest.json")
    if (manifest.get("configuration") != settings
            or manifest.get("configuration_sha256") != old["frozen_configuration_sha256"]
            or manifest.get("case_contract_sha256") != digest(cases)
            or manifest.get("planned_cases") != len(cases)
            or manifest.get("solver_tools") != []
            or manifest.get("answer_keys_available_to_solver") is not False
            or manifest.get("model_selection_on_test") is not False):
        raise ResumeError("The preserved manifest changes the frozen input contract")
    fork_proof = v2.validate_fork(run_dir, settings, parent, parent_sha)
    helper = frozen_helper(project, old["frozen_runner"], old["frozen_runner_sha256"])
    contexts = parent["run_context_checks"][settings["run_id"]]
    if amendment["run_context_checks"][settings["run_id"]] != contexts or file_sha(contexts["path"]) != contexts["sha256"]:
        raise ResumeError("The unchanged per-case context evidence changed")
    prompt_counts = {v["case_id"]: v["prompt_tokens"] for v in read(contexts["path"])["per_case"]}
    segments = {}; endpoint_map = {v["endpoint_id"]: v for v in amendment["endpoints"]}
    for path in (run_dir / SEGMENTS).glob("*.json"):
        segment = read(path)
        if (segment.get("amendment_sha256") != sidecar["amendment_sha256"]
                or segment.get("segment_id") != path.stem
                or segment.get("actual_runner_sha256") != file_sha(__file__)
                or segment.get("scheduler_policy") != POLICY
                or segment.get("transport_timeout_seconds") != TRANSPORT_TIMEOUT
                or segment.get("parent_checkpoint_sha256") != sidecar["parent_checkpoint_sha256"]):
            raise ResumeError("A new producer segment differs from its exact chained implementation")
        for endpoint in segment["endpoints"]:
            declared = endpoint_map.get(endpoint["endpoint_id"])
            if declared is None or endpoint != validate_endpoint(declared, live=False):
                raise ResumeError("New segment server identity differs from the amendment")
        segments[path.stem] = segment
    counts = Counter(); expected_names = set(); dispatches = []; ambiguous = []; receipts = {}; actual_servers = {}
    for case in cases:
        name = digest([case["task"], case["variant"], case["case_id"]]) + ".json"; expected_names.add(name)
        reqp, respp, rp = run_dir / "requests" / name, run_dir / "responses" / name, run_dir / RECEIPTS / name
        request = read(reqp) if reqp.exists() else None; response = read(respp) if respp.exists() else None
        expected_request = helper.request_record(case, settings)
        if request is not None and request != expected_request:
            raise ResumeError("A request differs from the unchanged original payload")
        if response is not None:
            if request is None: raise ResumeError("A saved response has no request")
            v2._validate_response(response, request, case, settings); counts[response.get("status", "unknown_saved_response")] += 1
        elif request is not None or rp.exists():
            counts["interrupted_unknown_completion"] += 1; ambiguous.append(name)
        else: counts["not_dispatched_after_error"] += 1
        historical_request = "requests/" + name in baseline; historical_response = "responses/" + name in baseline
        if rp.exists():
            receipt = read(rp); segment = segments.get(receipt.get("segment_id")); receipts[name] = file_sha(rp)
            if (segment is None or receipt.get("amendment_sha256") != sidecar["amendment_sha256"]
                    or receipt.get("filename") != name or receipt.get("case_id") != case["case_id"]
                    or receipt.get("request_sha256") != expected_request["request_sha256"]
                    or receipt.get("parent_checkpoint_sha256") != sidecar["parent_checkpoint_sha256"]
                    or receipt.get("scheduler_policy") != POLICY
                    or receipt.get("transport_timeout_seconds") != TRANSPORT_TIMEOUT
                    or receipt.get("prompt_tokens") != prompt_counts[case["case_id"]]):
                raise ResumeError("A saturation dispatch differs from its frozen case/chain contract")
            if historical_request or historical_response:
                raise ResumeError("A saturation dispatch attempted to regenerate a retained case")
            endpoint = next((e for e in segment["endpoints"] if e["endpoint_id"] == receipt.get("endpoint_id")), None)
            if (endpoint is None or receipt.get("server_identity_sha256") != endpoint["server_identity_sha256"]
                    or receipt.get("queue_limit") != endpoint["queue_limit"]
                    or receipt.get("server_max_num_seqs") != endpoint["max_num_seqs"]):
                raise ResumeError("A dispatch does not identify the actual server/queue")
            if request is not None and receipt.get("request_file_sha256") != file_sha(reqp):
                raise ResumeError("A new request file changed")
            if response is not None and (receipt.get("status") != "response_saved" or receipt.get("response_file_sha256") != file_sha(respp)):
                raise ResumeError("A new response differs from its completed dispatch")
            actual_servers[(endpoint["endpoint_id"], endpoint["server_identity_sha256"])] = endpoint; dispatches.append(name)
        elif (request is not None and not historical_request) or (response is not None and not historical_response):
            raise ResumeError("New raw records lack new producer provenance")
    for kind in ("requests", "responses", RECEIPTS):
        if {p.name for p in (run_dir / kind).glob("*.json")} - expected_names:
            raise ResumeError("Unexpected raw or dispatch slots")
    if require_terminal:
        if any(s["stage"] not in {"terminal", "paused"} for s in segments.values()) or not (run_dir / COMPLETION).is_file():
            raise ResumeError("Saturation generation is not terminal")
        done = read(run_dir / COMPLETION)
        if (done.get("run_id") != settings["run_id"] or done.get("amendment_sha256") != sidecar["amendment_sha256"]
                or done.get("planned") != len(cases) or done.get("statuses") != dict(counts)
                or done.get("retry_or_resampling") is not False
                or done.get("generation_exit_code") != (0 if counts["completed"] == len(cases) else 1)):
            raise ResumeError("Saturation terminal marker does not match the complete native denominator")
    return {"schema_version": 1, "amendment_sha256": sidecar["amendment_sha256"],
            "sidecar_sha256": file_sha(run_dir / SIDECAR), "generation_completion_sha256": file_sha(run_dir / COMPLETION) if (run_dir / COMPLETION).exists() else None,
            "original_run_manifest_sha256": file_sha(run_dir / "run_manifest.json"), "retained_files": baseline,
            "dispatched_files": dispatches, "ambiguous_files": ambiguous,
            "segment_files_sha256": {name + ".json": file_sha(run_dir / SEGMENTS / (name + ".json")) for name in segments},
            "receipt_files_sha256": receipts, "actual_servers": list(actual_servers.values()),
            "all_saved_responses_verified": True, "status_counts": dict(counts),
            "generation_exit_code": 0 if counts["completed"] == len(cases) else 1,
            "parent_amendment_sha256": parent_sha, "parent_sidecar_sha256": sidecar["parent_sidecar_sha256"],
            "parent_checkpoint_sha256": sidecar["parent_checkpoint_sha256"], "parent_provenance": checkpoint["parent_proof"], **fork_proof}


class Run:
    acquire = v2.Run.acquire
    close = v2.Run.close

    def __init__(self, entry, root, amendment, amendment_path, amendment_sha256):
        self.entry, self.root = entry, Path(root); self.project = local_path(root, entry["project_root"])
        self.config_path = local_path(self.project, entry["config_path"])
        if file_sha(self.config_path) != entry["config_sha256"]: raise ResumeError("Frozen run configuration changed")
        self.helper = frozen_helper(self.project, entry["runner"], entry["runner_sha256"])
        self.settings, self.cases = self.helper.read_frozen_config(self.config_path)
        if (self.settings["run_id"] != entry["run_id"] or self.settings["model"] != MODEL or self.settings["model_revision"] != REVISION
                or self.settings["generation"]["max_tokens"] != 4096 or digest(self.settings["generation"]) != entry["generation_sha256"]
                or self.settings.get("approved_task_ids") != [entry["task_id"]] or entry["task_id"] in {"B06", "P18"}
                or self.settings.get("runner", entry["runner"]) != entry["runner"]
                or len(self.cases) != entry["case_count"] or file_sha(self.project / self.settings["input_file"]) != entry["input_sha256"]):
            raise ResumeError("A saturation run changes the frozen scientific input contract")
        self.source_run = self.project / "results/runs" / self.settings["run_id"]
        self.run = Path(amendment.get("continuation_run_directories", {}).get(self.settings["run_id"], self.source_run)).resolve()
        if not self.run.is_relative_to((self.project / "results/runs").resolve()): raise ResumeError("Run storage leaves the native project")
        self.case_contract = digest(self.cases); self.amendment, self.amendment_path, self.amendment_sha256 = amendment, Path(amendment_path), amendment_sha256
        if (file_sha(self.amendment_path) != amendment_sha256 or read(self.amendment_path) != amendment
                or amendment.get("execution_variant") != "saturation_native_queue_v1"
                or amendment.get("scheduler_policy") != POLICY or amendment.get("scientific_protocol_changes") != []
                or amendment.get("transport_timeout_seconds") != TRANSPORT_TIMEOUT
                or amendment.get("adapter_files_sha256", {}).get(str(Path(__file__).resolve())) != file_sha(__file__)):
            raise ResumeError("The new execution contract must pin this exact infrastructure-only implementation")
        parent, self.parent_sha = _parent(amendment)
        context_source = amendment["run_context_checks"][self.settings["run_id"]]
        if context_source != parent["run_context_checks"][self.settings["run_id"]] or file_sha(context_source["path"]) != context_source["sha256"]:
            raise ResumeError("Frozen per-case context report changed")
        context = read(context_source["path"]); per_case = context["per_case"]
        if (context["case_count"] != len(self.cases) or context["output_budget"] != 4096 or context["all_prompts_fit"] is not True
                or [v["case_id"] for v in per_case] != [c["case_id"] for c in self.cases]
                or any(type(v["prompt_tokens"]) is not int or v["prompt_tokens"] < 1 for v in per_case)):
            raise ResumeError("Context report does not cover the exact ordered frozen cases")
        self.prompt_tokens = {v["case_id"]: v["prompt_tokens"] for v in per_case}
        if any(not any(e["max_model_len"] >= n + 4096 for e in amendment["endpoints"]) for n in self.prompt_tokens.values()):
            raise ResumeError("No unchanged serving context covers a complete prompt")
        self.statuses = Counter(); self.mutex, self.locks = threading.Lock(), []; self.started = time.monotonic()
        self.dispatched = 0; self.finished_result = None; self.segment_id = uuid.uuid4().hex; self.segment = None; self.baseline = {}

    def inventory(self):
        result = Counter(); expected = set()
        for case in self.cases:
            name = digest([case["task"], case["variant"], case["case_id"]]) + ".json"; expected.add(name)
            req, resp, receipt = self.run / "requests" / name, self.run / "responses" / name, self.run / RECEIPTS / name
            if resp.exists():
                if not req.exists() or read(req) != self.helper.request_record(case, self.settings): raise ResumeError("Saved response lacks its exact frozen request")
                value = read(resp); v2._validate_response(value, read(req), case, self.settings); result[value.get("status", "unknown_saved_response")] += 1
            elif req.exists() or receipt.exists(): result["interrupted_unknown_completion"] += 1
            else: result["undispatched"] += 1
        for kind in ("requests", "responses", RECEIPTS):
            if {p.name for p in (self.run / kind).glob("*.json")} - expected: raise ResumeError("Extra raw or dispatch slots")
        return result

    def prepare(self, endpoints):
        if (self.run / COMPLETION).exists(): raise ResumeError("A terminal saturation generation cannot be extended")
        if not (self.run / v2.SIDECAR).is_file(): raise ResumeError("Saturation continuation requires the immutable v2 source sidecar")
        old = read(self.run / v2.SIDECAR)
        if old["amendment_sha256"] != self.parent_sha: raise ResumeError("This run belongs to a different original execution amendment")
        sidecar_path = self.run / SIDECAR
        if sidecar_path.exists():
            self.sidecar = read(sidecar_path)
            if self.sidecar["amendment_sha256"] != self.amendment_sha256: raise ResumeError("Another saturation amendment owns this run")
            validate_resume_provenance(self.run, self.settings, self.cases)
            for p in (self.run / SEGMENTS).glob("*.json"):
                s = read(p)
                if s["stage"] == "running":
                    s.update(stage="paused", closed_at_utc=stamp(), interrupted_producer_no_retry=True); atomic_write(p, s)
        else:
            proof = v2.validate_resume_provenance(self.run, self.settings, self.cases, require_terminal=True)
            if proof["ambiguous_files"]: raise ResumeError("Original producer has ambiguous calls; continuation must not regenerate them")
            if proof["status_counts"].get("not_dispatched_proven_never_executed", 0):
                raise ResumeError("Unused original no-execution exceptions require a separately reviewed continuation; they cannot be silently omitted")
            checkpoint = {"schema_version": 1, "run_id": self.settings["run_id"], "parent_amendment_sha256": self.parent_sha,
                          "parent_sidecar_sha256": file_sha(self.run / v2.SIDECAR), "files_sha256": _parent_files(self.run), "parent_proof": proof}
            cp = self.run / CHECKPOINT
            if cp.exists():
                if read(cp) != checkpoint: raise ResumeError("Existing immutable parent checkpoint differs")
            else: atomic_write(cp, checkpoint, exclusive=True)
            self.sidecar = {"schema_version": 1, "run_id": self.settings["run_id"], "amendment_path": str(self.amendment_path),
                            "amendment_sha256": self.amendment_sha256, "parent_amendment_sha256": self.parent_sha,
                            "parent_sidecar_sha256": file_sha(self.run / v2.SIDECAR), "parent_checkpoint_sha256": file_sha(cp),
                            "adapter_files_sha256": self.amendment["adapter_files_sha256"], "created_at_utc": stamp()}
            atomic_write(sidecar_path, self.sidecar, exclusive=True)
        self.baseline = raw_inventory(self.run); self.statuses = self.inventory(); self.statuses.pop("undispatched", None)
        self.segment = {"schema_version": 1, "segment_id": self.segment_id, "stage": "running", "started_at_utc": stamp(),
                        "amendment_sha256": self.amendment_sha256, "actual_runner_sha256": file_sha(__file__), "endpoints": endpoints,
                        "parent_checkpoint_sha256": self.sidecar["parent_checkpoint_sha256"], "scheduler_policy": POLICY,
                        "transport_timeout_seconds": TRANSPORT_TIMEOUT, "protocol_changes": [], "baseline_statuses": dict(self.statuses)}
        atomic_write(self.run / SEGMENTS / (self.segment_id + ".json"), self.segment, exclusive=True); self.progress()

    def pending(self):
        for case in self.cases:
            name = digest([case["task"], case["variant"], case["case_id"]]) + ".json"
            if not any((self.run / kind / name).exists() for kind in ("requests", "responses", RECEIPTS, v2.RECEIPTS)): yield case, name

    def dispatch(self, case, name, endpoint, stopped):
        if stopped.is_set(): return
        reqp, respp, rp = self.run / "requests" / name, self.run / "responses" / name, self.run / RECEIPTS / name
        if any(p.exists() for p in (reqp, respp, rp)): raise ResumeError("No saved or ambiguous case may be regenerated")
        request = self.helper.request_record(case, self.settings)
        receipt = {"schema_version": 1, "segment_id": self.segment_id, "amendment_sha256": self.amendment_sha256,
                   "parent_checkpoint_sha256": self.sidecar["parent_checkpoint_sha256"], "filename": name, "case_id": case["case_id"],
                   "request_sha256": request["request_sha256"], "endpoint_id": endpoint["endpoint_id"], "server_identity_sha256": endpoint["server_identity_sha256"],
                   "status": "claimed", "claimed_at_utc": stamp(), "prompt_tokens": self.prompt_tokens[case["case_id"]], "scheduler_policy": POLICY,
                   "queue_limit": endpoint["queue_limit"], "server_max_num_seqs": endpoint["max_num_seqs"], "transport_timeout_seconds": TRANSPORT_TIMEOUT}
        atomic_write(rp, receipt, exclusive=True); atomic_write(reqp, request, exclusive=True)
        receipt.update(status="request_saved", request_file_sha256=file_sha(reqp)); atomic_write(rp, receipt)
        before = time.monotonic(); code, response = self.helper.call(endpoint["endpoint"] + "/chat/completions", request["payload"], timeout=TRANSPORT_TIMEOUT)
        record = {**{k: case[k] for k in ("task", "case_id", "variant", "split")}, "model": self.settings["model"], "model_revision": self.settings["model_revision"],
                  "request_sha256": request["request_sha256"], "http_status": code, "response": response, "elapsed_seconds": round(time.monotonic() - before, 3), "saved_at_utc": stamp()}
        if code == 200 and response.get("model") == self.settings["model"] and len(response.get("choices", [])) == 1:
            choice = response["choices"][0]; record.update(status="completed", text=choice["message"].get("content") or "", finish_reason=choice.get("finish_reason"))
        else: record["status"] = "transport_error" if code == 0 else "server_error"; stopped.set()
        atomic_write(respp, record, exclusive=True); receipt.update(status="response_saved", response_file_sha256=file_sha(respp), finished_at_utc=stamp()); atomic_write(rp, receipt)
        with self.mutex: self.statuses[record["status"]] += 1; self.dispatched += 1; self.progress()

    def progress(self, terminal=False):
        atomic_write(self.run / PROGRESS, {"run": self.settings["run_id"], "stage": "generation_complete" if terminal and self.statuses["completed"] == len(self.cases) else "incomplete" if terminal else "running",
                     "planned": len(self.cases), "finished": sum(self.statuses.values()), "statuses": dict(self.statuses), "requests_saved": len(list((self.run / "requests").glob("*.json"))),
                     "elapsed_seconds": round(time.monotonic() - self.started, 3), "updated_at_utc": stamp(), "infrastructure_amendment_sha256": self.amendment_sha256})

    def finish(self):
        with self.mutex:
            if self.finished_result is not None: return self.finished_result
            self.statuses = self.inventory(); n = self.statuses.pop("undispatched", 0)
            if n: self.statuses["not_dispatched_after_error"] += n
            self.segment.update(stage="terminal", finished_at_utc=stamp(), dispatched=self.dispatched, statuses=dict(self.statuses)); atomic_write(self.run / SEGMENTS / (self.segment_id + ".json"), self.segment)
            self.progress(terminal=True)
            result = {"schema_version": 1, "run_id": self.settings["run_id"], "finished_at_utc": stamp(), "amendment_sha256": self.amendment_sha256,
                      "generation_exit_code": 0 if self.statuses["completed"] == len(self.cases) else 1, "planned": len(self.cases), "statuses": dict(self.statuses), "retry_or_resampling": False}
            atomic_write(self.run / COMPLETION, result, exclusive=True); self.finished_result = result; return result

    def pause(self):
        with self.mutex:
            if self.finished_result is not None: return self.finished_result
            self.statuses = self.inventory(); self.segment.update(stage="paused", closed_at_utc=stamp(), dispatched=self.dispatched, statuses=dict(self.statuses))
            atomic_write(self.run / SEGMENTS / (self.segment_id + ".json"), self.segment)
            value = {"stage": "paused", "run_id": self.settings["run_id"], "segment_id": self.segment_id, "amendment_sha256": self.amendment_sha256, "statuses": dict(self.statuses), "paused_at_utc": stamp(), "retry_or_resampling": False}
            atomic_write(self.run / "shared_vllm_saturation_pauses" / (self.segment_id + ".json"), value, exclusive=True)
            return value

    def finish_if_complete(self):
        with self.mutex: complete = sum(self.statuses.values()) == len(self.cases)
        if complete: self.finish(); self.close()
