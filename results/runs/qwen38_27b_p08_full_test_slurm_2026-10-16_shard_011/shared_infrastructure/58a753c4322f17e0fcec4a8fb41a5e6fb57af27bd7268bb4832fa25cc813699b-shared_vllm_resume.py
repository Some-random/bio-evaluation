"""Infrastructure-only continuation of immutable, reviewed local evaluations.

This module never reads scorer references and never changes model-facing data.
Original request/response files and existing run manifests are immutable.  A
request saved without its response is ambiguous and is never dispatched again.
"""
from __future__ import annotations

import concurrent.futures
from collections import Counter
import datetime as dt
import fcntl
from fractions import Fraction
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import socket
import shutil
import subprocess
import sys
import threading
import time
import urllib.parse
import uuid


MODEL = "Qwen/Qwen3.8-27B"
REVISION = "1d4bf0f2ff6012fd82039f2fa52739d0dd7c60c0"
SIDECAR = "shared_vllm_amendment.json"
RECEIPTS = "shared_vllm_dispatch"
SEGMENTS = "shared_vllm_segments"
FORK_MANIFEST = "shared_vllm_fork_manifest.json"


class ResumeError(RuntimeError):
    pass


def stamp():
    return dt.datetime.now(dt.timezone.utc).isoformat()


def digest(value):
    return hashlib.sha256(json.dumps(value, ensure_ascii=False, sort_keys=True,
                                    separators=(",", ":")).encode()).hexdigest()


def file_sha(path):
    value = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            value.update(block)
    return value.hexdigest()


def read(path):
    path = Path(path)
    if path.is_symlink() or not path.is_file():
        raise ResumeError("A regular non-symlink metadata file is required: " + str(path))
    return json.loads(path.read_text())


def atomic_write(path, value, *, exclusive=False):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.parent / ("." + path.name + "." + uuid.uuid4().hex + ".tmp")
    try:
        with temporary.open("x") as stream:
            json.dump(value, stream, ensure_ascii=False, indent=2)
            stream.write("\n")
            stream.flush()
            os.fsync(stream.fileno())
        temporary.chmod(0o600)
        if exclusive:
            os.link(temporary, path)
        else:
            if path.is_symlink():
                raise ResumeError("Refusing a symlink metadata destination")
            os.replace(temporary, path)
    finally:
        temporary.unlink(missing_ok=True)


def local_path(root, name):
    path = (Path(root) / name).resolve()
    if not path.is_relative_to(Path(root).resolve()):
        raise ResumeError("Path leaves its declared project")
    return path


def frozen_helper(project, relative, expected):
    path = local_path(project, relative)
    if file_sha(path) != expected:
        raise ResumeError("Frozen payload runner changed")
    name = "frozen_shared_payload_" + expected
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    if Path(module.ROOT).resolve() != Path(project).resolve():
        raise ResumeError("Frozen payload runner has a different project root")
    return module


def raw_inventory(run_dir):
    run_dir = Path(run_dir)
    result = {}
    for name in ("run_manifest.json",):
        path = run_dir / name
        if path.exists():
            if path.is_symlink():
                raise ResumeError("Raw manifest is a symlink")
            result[name] = file_sha(path)
    for kind in ("requests", "responses"):
        directory = run_dir / kind
        if directory.is_symlink():
            raise ResumeError("Raw directory is a symlink")
        for path in directory.glob("*.json"):
            if path.is_symlink() or not path.is_file():
                raise ResumeError("Raw record is not a regular file")
            result[kind + "/" + path.name] = file_sha(path)
    return result


def negative_execution_records(amendment, *, live=False):
    """Accept only explicitly pinned, terminal OS-drain no-execution proofs.

    The exception concerns a request proven never to have executed, not an
    unknown completion, failed call, truncated answer, or unsatisfactory result.
    """
    records, jobs = {}, set()
    terminal = {"COMPLETED", "FAILED", "CANCELLED", "TIMEOUT", "NODE_FAIL", "OUT_OF_MEMORY", "PREEMPTED", "BOOT_FAIL", "DEADLINE", "REVOKED"}
    for source in amendment.get("negative_execution_receipts", []):
        path = Path(source["path"])
        if file_sha(path) != source["sha256"]:
            raise ResumeError("Negative execution receipt changed")
        value = read(path)
        proof = value.get("proof", {})
        accounting = value.get("terminal_accounting", {})
        job = str(value.get("old_job_id", ""))
        state = str(accounting.get("state", "")).split()[0].rstrip("+")
        # The first three frozen drain receipts predate the schema_version key;
        # their full proof fields and exact pinned bytes remain authoritative.
        if (value.get("schema_version") not in (None, 1)
                or value.get("kind") != "shared_vllm_negative_execution_drain"
                or value.get("stage") != "drained_and_job_terminal"
                or not job.isdigit() or str(accounting.get("job_id")) != job or state not in terminal
                or any(proof.get(name) is not True for name in (
                    "api_stopped_before_new_requests", "api_killed_while_stopped",
                    "api_dead_before_client_kill", "api_dead_before_job_cancellation",
                    "client_killed_while_stopped", "all_pre_stop_requests_paired"))):
            raise ResumeError("Request-only exception lacks a complete terminal no-execution proof")
        jobs.add(job)
        protocol_version = value.get("drain_protocol_version", 1)
        if protocol_version not in (1, 2):
            raise ResumeError("Unknown OS-drain protocol version")
        if protocol_version == 2 and any(proof.get(name) is not True for name in (
                "executor_stopped_before_client_stop", "executor_stopped_until_client_killed",
                "executor_killed_while_stopped", "executor_killed_after_client_dead")):
            raise ResumeError("Version-two drain lacks its executor-parent stop/kill proof")
        for item in value.get("request_records", []):
            if (item.get("request_created_after_api_stop") is not True
                    or item.get("server_stopped_at_creation") is not True
                    or len(item.get("request_file_sha256", "")) != 64
                    or len(item.get("payload_sha256", "")) != 64):
                raise ResumeError("A negative execution request lacks exact immutable evidence")
            if protocol_version == 1 and item["run_id"] not in amendment.get("continuation_run_directories", {}):
                raise ResumeError("Legacy drain exceptions require a derived view preserving partial native scoring history")
            key = (str(Path(item["project_root"]).resolve()), item["run_id"], item["filename"])
            if key in records:
                raise ResumeError("Duplicate negative execution request evidence")
            records[key] = {**item, "negative_execution_receipt_sha256": source["sha256"], "old_job_id": job}
    if live and jobs:
        result = subprocess.run(["sacct", "-X", "-j", ",".join(sorted(jobs)), "-n", "-P", "--format=JobIDRaw,State,ExitCode"],
                                check=True, capture_output=True, text=True, timeout=30)
        observed = {}
        for line in result.stdout.splitlines():
            fields = line.split("|")
            if len(fields) >= 3 and fields[0] in jobs:
                observed[fields[0]] = fields[1].split()[0].rstrip("+")
        if set(observed) != jobs or any(state not in terminal for state in observed.values()):
            raise ResumeError("An old generation job is not independently terminal")
    return records


def validate_source_snapshot(snapshot, source_run, settings, case_count):
    source_run = Path(source_run).resolve()
    if Path(snapshot["source_run_directory"]).resolve() != source_run:
        raise ResumeError("Derived continuation points to another original source")
    files = snapshot["files_sha256"]
    required = {"run_manifest.json", "completion.json", "scores.json", "scoring_output_lock.json"}
    if not required <= set(files):
        raise ResumeError("Derived continuation must pin every original scoring boundary")
    for name, expected in files.items():
        path = local_path(source_run, name)
        if path.is_symlink() or file_sha(path) != expected:
            raise ResumeError("An immutable original partial-run artifact changed")
    completion, scores = read(source_run / "completion.json"), read(source_run / "scores.json")
    if (completion.get("generation_exit_code") in (None, 0) or completion.get("scoring_exit_code") != 0
            or scores.get("planned") != case_count or not 0 <= scores.get("completed", -1) < case_count):
        raise ResumeError("Only an explicitly interrupted, partially scored source may use a derived continuation")
    if (completion.get("run_manifest_sha256") != files["run_manifest.json"]
            or completion.get("scores_sha256") != files["scores.json"]):
        raise ResumeError("Original partial native completion does not match its manifest and scores")
    output_lock = read(source_run / "scoring_output_lock.json")
    locked_files = output_lock.get("files_sha256", {})
    if (output_lock.get("contract_sha256") != digest(locked_files)
            or locked_files.get("run_manifest.json") != files["run_manifest.json"]
            or any(sum(name.startswith(kind + "/") for name in locked_files) != case_count for kind in ("requests", "responses"))):
        raise ResumeError("Original native output lock does not preserve every planned slot")
    for name, expected in locked_files.items():
        if files.get(name) != expected:
            raise ResumeError("An originally locked output or missing slot changed")
    if any(name.startswith(("requests/", "responses/")) and name.endswith(".json") and name not in locked_files for name in files):
        raise ResumeError("Original partial source has raw files outside its native output lock")
    if read(source_run / "run_manifest.json").get("configuration") != settings:
        raise ResumeError("Derived source has a different frozen model-facing configuration")
    return files


def validate_fork(run_dir, settings, amendment, amendment_sha256):
    run_dir = Path(run_dir).resolve()
    override = amendment.get("continuation_run_directories", {}).get(settings["run_id"])
    if override is None:
        if (run_dir / FORK_MANIFEST).exists():
            raise ResumeError("Unexpected derived continuation marker")
        return {}
    if Path(override).resolve() != run_dir:
        raise ResumeError("Derived continuation directory differs from its amendment")
    snapshot = amendment["continuation_source_snapshots"][settings["run_id"]]
    source_run = Path(snapshot["source_run_directory"])
    files = validate_source_snapshot(snapshot, source_run, settings, read(run_dir / "run_manifest.json")["planned_cases"])
    marker = read(run_dir / FORK_MANIFEST)
    expected = {"schema_version": 1, "logical_run_id": settings["run_id"], "source_run_directory": str(source_run.resolve()),
                "continuation_run_directory": str(run_dir), "source_files_sha256": files,
                "source_scoring_output_lock_sha256": files["scoring_output_lock.json"],
                "source_completion_sha256": files["completion.json"], "source_scores_sha256": files["scores.json"],
                "amendment_sha256": amendment_sha256}
    if marker != expected:
        raise ResumeError("Derived continuation marker differs from the pinned original source inventory")
    for name, expected_hash in files.items():
        if name == "run_manifest.json" or (name.startswith(("requests/", "responses/")) and name.endswith(".json")):
            if file_sha(local_path(run_dir, name)) != expected_hash:
                raise ResumeError("A retained original raw record changed in the derived continuation")
    return {"fork_manifest_sha256": file_sha(run_dir / FORK_MANIFEST),
            "original_source_folder": str(source_run.resolve()),
            "parent_scoring_output_lock_sha256": files["scoring_output_lock.json"],
            "parent_completion_sha256": files["completion.json"],
            "parent_scores_sha256": files["scores.json"]}


def _validate_response(response, request, case, settings):
    for key, expected in {**{k: case[k] for k in ("task", "case_id", "variant", "split")},
                          "model": settings["model"], "model_revision": settings["model_revision"],
                          "request_sha256": request["request_sha256"]}.items():
        if response.get(key) != expected:
            raise ResumeError("Saved response provenance differs: " + key)
    if response.get("status") == "completed":
        raw = response.get("response", {})
        choices = raw.get("choices", [])
        if (response.get("http_status") != 200 or raw.get("model") != settings["model"]
                or len(choices) != 1
                or response.get("text") != (choices[0].get("message", {}).get("content") or "")
                or response.get("finish_reason") != choices[0].get("finish_reason")):
            raise ResumeError("Saved successful response is inconsistent with its raw response")


def validate_resume_provenance(run_dir, settings, cases, *, require_terminal=False):
    """Validate old/new raw records without reading labels or rewriting metadata.

    ``cases`` is the exact ordered input list, and ``settings`` is the unchanged
    original configuration.  Return hashes and actual server records suitable
    for a versioned native aggregate's source-provenance manifest.
    """
    run_dir = Path(run_dir)
    sidecar = read(run_dir / SIDECAR)
    if sidecar.get("schema_version") != 1 or sidecar.get("run_id") != settings["run_id"]:
        raise ResumeError("Unknown continuation provenance schema or run")
    project = Path(sidecar["project_root"])
    config = local_path(project, sidecar["config_path"])
    if (file_sha(config) != sidecar["frozen_configuration_sha256"] or read(config) != settings
            or sidecar.get("case_contract_sha256") != digest(cases)):
        raise ResumeError("Frozen configuration or case order changed")
    amendment_path = Path(sidecar["amendment_path"])
    if file_sha(amendment_path) != sidecar["amendment_sha256"]:
        raise ResumeError("Infrastructure amendment changed")
    amendment = read(amendment_path)
    fork_proof = validate_fork(run_dir, settings, amendment, sidecar["amendment_sha256"])
    negatives = negative_execution_records(amendment)
    declared_endpoints = {e["endpoint_id"]: e for e in amendment["endpoints"]}
    context_source = amendment["run_context_checks"][settings["run_id"]]
    if file_sha(context_source["path"]) != context_source["sha256"]:
        raise ResumeError("Per-case context evidence changed")
    prompt_counts = {v["case_id"]: v["prompt_tokens"] for v in read(context_source["path"])["per_case"]}
    for name, expected in sidecar["adapter_files_sha256"].items():
        if file_sha(name) != expected:
            raise ResumeError("Continuation implementation changed")
    helper = frozen_helper(project, sidecar["frozen_runner"], sidecar["frozen_runner_sha256"])
    inventory = raw_inventory(run_dir)
    baseline = sidecar["baseline_files_sha256"]
    for name, expected in baseline.items():
        if inventory.get(name) != expected:
            raise ResumeError("A retained historical file disappeared or changed: " + name)
    original_manifest = sidecar.get("original_run_manifest_sha256")
    if original_manifest is not None and inventory.get("run_manifest.json") != original_manifest:
        raise ResumeError("Original run manifest changed")
    manifest = read(run_dir / "run_manifest.json")
    if (manifest.get("configuration") != settings
            or manifest.get("configuration_sha256") != sidecar["frozen_configuration_sha256"]
            or manifest.get("case_contract_sha256") != digest(cases)
            or manifest.get("planned_cases") != len(cases)
            or manifest.get("solver_tools") != []
            or manifest.get("answer_keys_available_to_solver") is not False
            or manifest.get("model_selection_on_test") is not False):
        raise ResumeError("Run manifest is incompatible with frozen inputs")
    if original_manifest is None and (manifest.get("runner_sha256") != file_sha(Path(__file__))
                                      or manifest.get("frozen_runner_sha256") != sidecar["frozen_runner_sha256"]
                                      or manifest.get("infrastructure_amendment_sha256") != sidecar["amendment_sha256"]):
        raise ResumeError("New manifest must identify the actual continuation implementation")
    segments = {}
    for path in (run_dir / SEGMENTS).glob("*.json"):
        value = read(path)
        if (value.get("amendment_sha256") != sidecar["amendment_sha256"]
                or value.get("segment_id") != path.stem
                or value.get("actual_runner_sha256") != file_sha(Path(__file__))):
            raise ResumeError("Segment provenance differs from infrastructure amendment")
        for endpoint in value.get("endpoints", []):
            declared = declared_endpoints.get(endpoint["endpoint_id"])
            if declared is None:
                raise ResumeError("Segment names an undeclared endpoint")
            verified = validate_endpoint(declared, settings["model"], settings["model_revision"], live=False)
            if endpoint != verified:
                raise ResumeError("Segment actual server differs from its immutable identity")
        segments[path.stem] = value
    receipt_hashes, dispatches, ambiguous, expected_names, actual_servers = {}, [], [], set(), {}
    status_counts = Counter()
    for case in cases:
        name = digest([case["task"], case["variant"], case["case_id"]]) + ".json"
        expected_names.add(name)
        request_path, response_path = run_dir / "requests" / name, run_dir / "responses" / name
        receipt_path = run_dir / RECEIPTS / name
        request = read(request_path) if request_path.exists() else None
        response = read(response_path) if response_path.exists() else None
        negative = negatives.get((str(project.resolve()), settings["run_id"], name))
        expected_request = helper.request_record(case, settings)
        if request is not None and request != expected_request:
            raise ResumeError("Saved request differs from the exact frozen payload")
        if response is not None:
            if request is None:
                raise ResumeError("Saved response has no request")
            _validate_response(response, request, case, settings)
            status_counts[response.get("status", "unknown_saved_response")] += 1
        elif request is not None and negative is not None and not receipt_path.exists():
            status_counts["not_dispatched_proven_never_executed"] += 1
        elif request is not None or receipt_path.exists():
            status_counts["interrupted_unknown_completion"] += 1
        else:
            status_counts["not_dispatched_after_error"] += 1
        new_request = request is not None and "requests/" + name not in baseline
        new_response = response is not None and "responses/" + name not in baseline
        if negative is not None and (request is None or file_sha(request_path) != negative["request_file_sha256"]
                                     or request["request_sha256"] != negative["payload_sha256"]):
            raise ResumeError("Proven-unexecuted request bytes differ from the drain receipt")
        if receipt_path.exists():
            receipt = read(receipt_path)
            receipt_hashes[name] = file_sha(receipt_path)
            segment = segments.get(receipt.get("segment_id"))
            if (segment is None or receipt.get("amendment_sha256") != sidecar["amendment_sha256"]
                    or receipt.get("filename") != name or receipt.get("case_id") != case["case_id"]
                    or receipt.get("request_sha256") != expected_request["request_sha256"]):
                raise ResumeError("Dispatch receipt is outside the exact input/segment contract")
            endpoint = next((e for e in segment["endpoints"] if e["endpoint_id"] == receipt.get("endpoint_id")), None)
            if endpoint is None or receipt.get("server_identity_sha256") != endpoint["server_identity_sha256"]:
                raise ResumeError("Dispatch receipt does not name its actual server")
            if (receipt.get("prompt_tokens") != prompt_counts[case["case_id"]]
                    or receipt.get("admission_weight") != str(admission_weight(endpoint, prompt_counts[case["case_id"]]))):
                raise ResumeError("Dispatch admission differs from its unchanged per-case token check")
            if request is not None and receipt.get("request_file_sha256") != file_sha(request_path):
                raise ResumeError("Dispatch request file hash changed")
            if response is not None and (receipt.get("status") != "response_saved"
                    or receipt.get("response_file_sha256") != file_sha(response_path)):
                raise ResumeError("Dispatch response file hash changed or receipt is incomplete")
            if receipt.get("negative_execution_receipt_sha256") is not None:
                if negative is None or receipt["negative_execution_receipt_sha256"] != negative["negative_execution_receipt_sha256"]:
                    raise ResumeError("Historical request exception does not match its pinned no-execution receipt")
            elif negative is not None and not new_request:
                raise ResumeError("Historical request continuation omits its negative execution evidence")
            claimed_without_request = request is None and response is None and receipt.get("status") == "claimed"
            if (not new_request and negative is None and not claimed_without_request) or (response is not None and not new_response):
                raise ResumeError("A new dispatch attempts to claim a historical raw record")
            key = (receipt["endpoint_id"], receipt["server_identity_sha256"])
            actual_servers[key] = endpoint
            dispatches.append(name)
        elif new_request or new_response:
            raise ResumeError("A new raw file has no immutable dispatch provenance")
        if (request is not None or receipt_path.exists()) and response is None and not (negative is not None and not receipt_path.exists()):
            ambiguous.append(name)
    for kind in ("requests", "responses", RECEIPTS):
        if {p.name for p in (run_dir / kind).glob("*.json")} - expected_names:
            raise ResumeError("Unexpected raw/dispatch case slots")
    if require_terminal and (any(s.get("stage") != "terminal" for s in segments.values())
                             or not (run_dir / "shared_vllm_generation_completion.json").is_file()):
        raise ResumeError("Shared-pool generation is not terminal")
    if require_terminal:
        done = read(run_dir / "shared_vllm_generation_completion.json")
        if (done.get("run_id") != settings["run_id"] or done.get("amendment_sha256") != sidecar["amendment_sha256"]
                or done.get("planned") != len(cases) or done.get("retry_or_resampling") is not False
                or done.get("statuses") != dict(status_counts)
                or done.get("generation_exit_code") != (0 if status_counts["completed"] == len(cases) else 1)):
            raise ResumeError("Shared generation terminal marker is inconsistent")
    return {"schema_version": 1, "amendment_sha256": sidecar["amendment_sha256"],
            "sidecar_sha256": file_sha(run_dir / SIDECAR),
            "generation_completion_sha256": file_sha(run_dir / "shared_vllm_generation_completion.json") if (run_dir / "shared_vllm_generation_completion.json").exists() else None,
            "original_run_manifest_sha256": original_manifest,
            "retained_files": baseline, "dispatched_files": dispatches, "ambiguous_files": ambiguous,
            "segment_files_sha256": {name + ".json": file_sha(run_dir / SEGMENTS / (name + ".json")) for name in segments},
            "receipt_files_sha256": receipt_hashes, "actual_servers": list(actual_servers.values()),
            "all_saved_responses_verified": True, "status_counts": dict(status_counts),
            "generation_exit_code": 0 if status_counts["completed"] == len(cases) else 1, **fork_proof}


def validate_endpoint(entry, model=MODEL, revision=REVISION, *, live=True):
    url = urllib.parse.urlsplit(entry["endpoint"])
    if (url.scheme != "http" or url.hostname != "127.0.0.1" or url.path != "/v1"
            or url.username or url.password or url.query or url.fragment or not url.port
            or not 1024 <= url.port <= 65535):
        raise ResumeError("Shared endpoints must be credential-free loopback HTTP /v1")
    identity = read(entry["server_identity_file"])
    if file_sha(entry["server_identity_file"]) != entry["server_identity_sha256"]:
        raise ResumeError("Shared server identity changed")
    if (identity.get("model") != model or identity.get("revision") != revision
            or identity.get("dtype") not in {"bfloat16", "bf16"}
            or identity.get("tensor_parallel_size") != entry["tensor_parallel_size"]
            or identity.get("max_model_len") != entry["max_model_len"]
            or identity.get("max_num_seqs", 0) < entry["max_inflight"]
            or identity.get("endpoint") != entry["endpoint"]):
        raise ResumeError("Shared server differs from the pinned BF16 serving contract")
    uuids = identity.get("gpu_uuids", [])
    if (len(uuids) != entry["tensor_parallel_size"] or len(set(uuids)) != len(uuids)
            or not all(isinstance(v, str) and v.startswith("GPU-") for v in uuids)
            or entry["max_inflight"] < 1 or entry["max_model_len"] < 4097):
        raise ResumeError("Shared server GPU/concurrency/context identity is invalid")
    limits = entry.get("length_limits", [])
    if (not limits or any(type(p.get("max_prompt_tokens")) is not int or p["max_prompt_tokens"] < 1
                         or type(p.get("max_inflight")) is not int or not 1 <= p["max_inflight"] <= entry["max_inflight"] for p in limits)
            or [p["max_prompt_tokens"] for p in limits] != sorted({p["max_prompt_tokens"] for p in limits})
            or any(a["max_inflight"] < b["max_inflight"] for a, b in zip(limits, limits[1:]))):
        raise ResumeError("Verified length-aware capacity limits are missing or inconsistent")
    if live:
        if identity.get("hostname") not in {socket.gethostname(), socket.getfqdn()}:
            raise ResumeError("Loopback identity belongs to another host")
        try:
            ticks = Path('/proc/' + str(identity['pid']) + '/stat').read_text().rsplit(')', 1)[1].split()[19]
        except (OSError, KeyError, IndexError) as error:
            raise ResumeError("Shared server process is not alive locally") from error
        if str(ticks) != str(identity.get("proc_start_ticks")):
            raise ResumeError("Shared server PID was reused")
    return {**entry, "server_identity": identity}


def admission_weight(endpoint, prompt_tokens):
    for profile in endpoint["length_limits"]:
        if prompt_tokens <= profile["max_prompt_tokens"]:
            return Fraction(1, profile["max_inflight"])
    raise ResumeError("No verified concurrency profile covers this full prompt")


class Run:
    def __init__(self, entry, root, amendment, amendment_path, amendment_sha256):
        self.entry, self.root = entry, root
        self.project = local_path(root, entry["project_root"])
        self.config_path = local_path(self.project, entry["config_path"])
        if file_sha(self.config_path) != entry["config_sha256"]:
            raise ResumeError("Run config differs from the frozen plan")
        self.helper = frozen_helper(self.project, entry["runner"], entry["runner_sha256"])
        self.settings, cases = self.helper.read_frozen_config(self.config_path)
        if (self.settings["run_id"] != entry["run_id"] or self.settings["model"] != MODEL
                or self.settings["model_revision"] != REVISION
                or set(self.settings["approved_task_ids"]) & {"B06", "P18"}
                or self.settings["generation"]["max_tokens"] != 4096
                or digest(self.settings["generation"]) != entry["generation_sha256"]
                or self.settings.get("approved_task_ids") != [entry["task_id"]]
                or self.settings.get("runner", entry["runner"]) != entry["runner"]
                or len(cases) != entry["case_count"]
                or file_sha(self.project / self.settings["input_file"]) != entry["input_sha256"]):
            raise ResumeError("Run changes a frozen model, scope, generation or input contract")
        self.source_run = self.project / "results/runs" / self.settings["run_id"]
        override = amendment.get("continuation_run_directories", {}).get(self.settings["run_id"])
        self.run = Path(override).resolve() if override else self.source_run
        if override and (not self.run.is_relative_to((self.project / "results/runs").resolve()) or self.run == self.source_run.resolve()):
            raise ResumeError("Derived continuation storage must be a separate project-local run directory")
        self.source_snapshot = amendment.get("continuation_source_snapshots", {}).get(self.settings["run_id"])
        if override:
            if self.source_snapshot is None:
                raise ResumeError("Derived continuation lacks its immutable original source inventory")
            validate_source_snapshot(self.source_snapshot, self.source_run, self.settings, len(cases))
        self.case_contract = digest(cases)
        self.cases = cases
        context_source = amendment.get("run_context_checks", {}).get(self.settings["run_id"])
        if not context_source or file_sha(context_source["path"]) != context_source["sha256"]:
            raise ResumeError("An unchanged per-case token/context check is required")
        context = read(context_source["path"])
        per_case = context.get("per_case", [])
        if (context.get("case_count") != len(cases) or context.get("output_budget") != 4096
                or context.get("all_prompts_fit") is not True
                or [v.get("case_id") for v in per_case] != [c["case_id"] for c in cases]
                or any(type(v.get("prompt_tokens")) is not int or v["prompt_tokens"] < 1 for v in per_case)
                or max((v["prompt_tokens"] for v in per_case), default=0) != context.get("max_prompt_tokens")):
            raise ResumeError("Per-case token check does not cover the exact frozen input order")
        self.prompt_tokens = {v["case_id"]: v["prompt_tokens"] for v in per_case}
        for count in self.prompt_tokens.values():
            if not any(e["max_model_len"] >= count + 4096 and admission_weight(e, count) <= 1
                       for e in amendment["endpoints"]):
                raise ResumeError("No verified shared capacity profile covers a complete prompt")
        self.baseline = raw_inventory(self.run)
        self.statuses = Counter()
        self.mutex, self.locks = threading.Lock(), []
        self.dispatched = 0
        self.amendment, self.amendment_path, self.amendment_sha256 = amendment, amendment_path, amendment_sha256
        self.segment_id = uuid.uuid4().hex
        self.segment = None
        self.finished_result = None
        all_negatives = negative_execution_records(amendment)
        self.negatives = {name: value for (project, rid, name), value in all_negatives.items()
                          if project == str(self.project) and rid == self.settings["run_id"]}
        self.started = time.monotonic()

    def acquire(self):
        paths = [self.project / ".local" / ("slurm_generation-" + self.settings["run_id"] + ".lock"), self.source_run / "worker.lock"]
        if self.run != self.source_run:
            paths.append(self.run / "worker.lock")
        for path in paths:
            path.parent.mkdir(parents=True, exist_ok=True)
            lock = path.open("a")
            try:
                fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
            except BlockingIOError as error:
                lock.close()
                self.close()
                raise ResumeError("Original generation still owns the run lock") from error
            self.locks.append(lock)

    def close(self):
        for lock in reversed(self.locks):
            lock.close()
        self.locks = []

    def inventory(self):
        folder = self.source_run if self.source_snapshot is not None and not (self.run / FORK_MANIFEST).exists() else self.run
        expected = set()
        result = Counter()
        for case in self.cases:
            name = digest([case["task"], case["variant"], case["case_id"]]) + ".json"
            expected.add(name)
            req, resp = folder / "requests" / name, folder / "responses" / name
            if resp.exists():
                if not req.exists() or read(req) != self.helper.request_record(case, self.settings):
                    raise ResumeError("Historical response has no exact frozen request")
                value = read(resp)
                _validate_response(value, read(req), case, self.settings)
                result[value.get("status", "unknown_saved_response")] += 1
            elif req.exists() or (self.run / RECEIPTS / name).exists():
                if req.exists() and read(req) != self.helper.request_record(case, self.settings):
                    raise ResumeError("Historical ambiguous request differs from frozen payload")
                negative = self.negatives.get(name)
                if negative is not None and not (self.run / RECEIPTS / name).exists():
                    if (file_sha(req) != negative["request_file_sha256"]
                            or read(req)["request_sha256"] != negative["payload_sha256"]):
                        raise ResumeError("Proven-unexecuted request differs from its drain receipt")
                    result["undispatched_proven_never_executed"] += 1
                else:
                    result["interrupted_unknown_completion"] += 1
            else:
                result["undispatched"] += 1
        for kind in ("requests", "responses", RECEIPTS):
            directory = self.run / kind if kind == RECEIPTS else folder / kind
            if {p.name for p in directory.glob("*.json")} - expected:
                raise ResumeError("Extra raw case slots before continuation")
        return result

    def prepare(self, endpoints):
        if (self.run / "completion.json").exists():
            raise ResumeError("Terminal native runs cannot be resumed")
        if (self.run / "scoring_output_lock.json").exists() or (self.run / "scores.json").exists():
            raise ResumeError("Already-scored predictions cannot be extended")
        if self.source_snapshot is not None:
            files = validate_source_snapshot(self.source_snapshot, self.source_run, self.settings, len(self.cases))
            for name, expected in files.items():
                if name != "run_manifest.json" and not (name.startswith(("requests/", "responses/")) and name.endswith(".json")):
                    continue
                source, target = local_path(self.source_run, name), local_path(self.run, name)
                target.parent.mkdir(parents=True, exist_ok=True)
                if target.exists():
                    if file_sha(target) != expected:
                        raise ResumeError("Existing derived original raw snapshot changed")
                else:
                    try:
                        os.link(source, target)
                    except OSError:
                        with source.open("rb") as src, target.open("xb") as dst:
                            shutil.copyfileobj(src, dst)
                            dst.flush()
                            os.fsync(dst.fileno())
                    if file_sha(target) != expected:
                        raise ResumeError("Derived original raw snapshot was not copied byte-for-byte")
            marker = {"schema_version": 1, "logical_run_id": self.settings["run_id"],
                      "source_run_directory": str(self.source_run.resolve()), "continuation_run_directory": str(self.run.resolve()),
                      "source_files_sha256": files, "source_scoring_output_lock_sha256": files["scoring_output_lock.json"],
                      "source_completion_sha256": files["completion.json"], "source_scores_sha256": files["scores.json"],
                      "amendment_sha256": self.amendment_sha256}
            marker_path = self.run / FORK_MANIFEST
            if marker_path.exists():
                if read(marker_path) != marker:
                    raise ResumeError("Existing derived continuation source provenance changed")
            else:
                atomic_write(marker_path, marker, exclusive=True)
        # Re-read after acquiring the original locks, rather than trusting a
        # planning snapshot collected while old clients were still running.
        self.baseline = raw_inventory(self.run)
        if (self.run / "run_manifest.json").exists():
            previous_manifest = read(self.run / "run_manifest.json")
            if (previous_manifest.get("configuration") != self.settings
                    or previous_manifest.get("configuration_sha256") != self.entry["config_sha256"]
                    or previous_manifest.get("case_contract_sha256") != self.case_contract
                    or previous_manifest.get("planned_cases") != len(self.cases)
                    or previous_manifest.get("solver_tools") != []
                    or previous_manifest.get("answer_keys_available_to_solver") is not False
                    or previous_manifest.get("model_selection_on_test") is not False):
                raise ResumeError("Existing manifest does not describe the frozen inputs")
        self.statuses = self.inventory()
        self.statuses.pop("undispatched", None)
        self.statuses.pop("undispatched_proven_never_executed", None)
        self.run.mkdir(parents=True, exist_ok=True)
        sidecar_path = self.run / SIDECAR
        if sidecar_path.exists():
            old = read(sidecar_path)
            if old.get("amendment_sha256") != self.amendment_sha256:
                raise ResumeError("A different infrastructure amendment already owns this run")
            validate_resume_provenance(self.run, self.settings, self.cases)
            # A previous producer cannot still own these runs because both
            # original generation locks are held by this process.  Close its
            # unfinished metadata segment; requests without responses remain
            # ambiguous and are never dispatched again.
            for path in (self.run / SEGMENTS).glob("*.json"):
                previous = read(path)
                if previous.get("stage") != "terminal":
                    previous.update(stage="terminal", closed_at_utc=stamp(),
                                    interrupted_producer_no_retry=True)
                    atomic_write(path, previous)
        else:
            sidecar = {"schema_version": 1, "run_id": self.settings["run_id"], "project_root": str(self.project),
                       "config_path": self.entry["config_path"], "frozen_configuration_sha256": self.entry["config_sha256"],
                       "frozen_runner": self.entry["runner"], "frozen_runner_sha256": self.entry["runner_sha256"],
                       "case_contract_sha256": self.case_contract, "amendment_path": str(self.amendment_path),
                       "amendment_sha256": self.amendment_sha256, "adapter_files_sha256": self.amendment["adapter_files_sha256"],
                       "baseline_files_sha256": self.baseline, "original_run_manifest_sha256": self.baseline.get("run_manifest.json"),
                       "created_at_utc": stamp(), "policy": "Preserve all historical bytes; never redispatch saved requests, including errors, truncations and ambiguous calls."}
            atomic_write(sidecar_path, sidecar, exclusive=True)
        manifest_path = self.run / "run_manifest.json"
        if not manifest_path.exists():
            manifest = {"configuration": self.settings, "configuration_sha256": self.entry["config_sha256"],
                        "runner_sha256": file_sha(Path(__file__)), "frozen_runner_sha256": self.entry["runner_sha256"],
                        "actual_runner_file": str(Path(__file__).resolve()),
                        "case_contract_sha256": self.case_contract, "planned_cases": len(self.cases),
                        "model_selection_on_test": False, "solver_tools": [], "answer_keys_available_to_solver": False,
                        "infrastructure_amendment_sha256": self.amendment_sha256,
                        "serving_configuration": {"mode": "versioned_shared_pool", "actual_routing": SEGMENTS},
                        "server": {"mode": "versioned_shared_pool", "actual_routing": SEGMENTS}}
            atomic_write(manifest_path, manifest, exclusive=True)
        self.segment = {"schema_version": 1, "segment_id": self.segment_id, "amendment_sha256": self.amendment_sha256,
                        "started_at_utc": stamp(), "stage": "running", "endpoints": endpoints,
                        "protocol_changes": [], "actual_runner_sha256": file_sha(Path(__file__)),
                        "baseline_statuses": dict(self.statuses)}
        atomic_write(self.run / SEGMENTS / (self.segment_id + ".json"), self.segment, exclusive=True)
        self.progress()

    def progress(self, terminal=False):
        value = {"run": self.settings["run_id"], "stage": "generation_complete" if terminal and self.statuses["completed"] == len(self.cases) else "incomplete" if terminal else "running",
                 "planned": len(self.cases), "finished": sum(self.statuses.values()), "statuses": dict(self.statuses),
                 "requests_saved": len(list((self.run / "requests").glob("*.json"))),
                 "elapsed_seconds": round(time.monotonic() - self.started, 3), "updated_at_utc": stamp(),
                 "infrastructure_amendment_sha256": self.amendment_sha256}
        atomic_write(self.run / "progress.json", value)

    def pending(self):
        for case in self.cases:
            name = digest([case["task"], case["variant"], case["case_id"]]) + ".json"
            proven_only = name in self.negatives and (self.run / "requests" / name).exists() and not any(
                (self.run / kind / name).exists() for kind in ("responses", RECEIPTS))
            if proven_only or not any((self.run / kind / name).exists() for kind in ("requests", "responses", RECEIPTS)):
                yield case, name

    def dispatch(self, case, name, endpoint, stopped):
        if stopped.is_set():
            return
        request = self.helper.request_record(case, self.settings)
        receipt_path = self.run / RECEIPTS / name
        request_path, response_path = self.run / "requests" / name, self.run / "responses" / name
        receipt = {"schema_version": 1, "segment_id": self.segment_id, "amendment_sha256": self.amendment_sha256,
                   "filename": name, "case_id": case["case_id"], "request_sha256": request["request_sha256"],
                   "endpoint_id": endpoint["endpoint_id"], "server_identity_sha256": endpoint["server_identity_sha256"],
                   "status": "claimed", "claimed_at_utc": stamp()}
        receipt.update(prompt_tokens=self.prompt_tokens[case["case_id"]],
                       admission_weight=str(admission_weight(endpoint, self.prompt_tokens[case["case_id"]])))
        negative = self.negatives.get(name)
        if request_path.exists():
            if (negative is None or file_sha(request_path) != negative["request_file_sha256"]
                    or request != read(request_path) or request["request_sha256"] != negative["payload_sha256"]):
                raise ResumeError("A saved request cannot be dispatched without exact no-execution proof")
            receipt["negative_execution_receipt_sha256"] = negative["negative_execution_receipt_sha256"]
        atomic_write(receipt_path, receipt, exclusive=True)
        if not request_path.exists():
            atomic_write(request_path, request, exclusive=True)
        receipt.update(status="request_saved", request_file_sha256=file_sha(request_path))
        atomic_write(receipt_path, receipt)
        before = time.monotonic()
        code, response = self.helper.call(endpoint["endpoint"] + "/chat/completions", request["payload"])
        metadata = {k: case[k] for k in ("task", "case_id", "variant", "split")}
        record = {**metadata, "model": self.settings["model"], "model_revision": self.settings["model_revision"],
                  "request_sha256": request["request_sha256"], "http_status": code, "response": response,
                  "elapsed_seconds": round(time.monotonic() - before, 3), "saved_at_utc": stamp()}
        if code == 200 and response.get("model") == self.settings["model"] and len(response.get("choices", [])) == 1:
            choice = response["choices"][0]
            record.update(status="completed", text=choice["message"].get("content") or "", finish_reason=choice.get("finish_reason"))
        else:
            record["status"] = "transport_error" if code == 0 else "server_error"
            stopped.set()
        atomic_write(response_path, record, exclusive=True)
        receipt.update(status="response_saved", response_file_sha256=file_sha(response_path), finished_at_utc=stamp())
        atomic_write(receipt_path, receipt)
        with self.mutex:
            self.statuses[record["status"]] += 1
            self.dispatched += 1
            self.progress()

    def finish(self):
        with self.mutex:
            if self.finished_result is not None:
                return self.finished_result
            # Classify interrupted claims without dispatching them again.
            self.statuses = self.inventory()
            undispatched = self.statuses.pop("undispatched", 0)
            if undispatched:
                self.statuses["not_dispatched_after_error"] += undispatched
            proven_undispatched = self.statuses.pop("undispatched_proven_never_executed", 0)
            if proven_undispatched:
                self.statuses["not_dispatched_proven_never_executed"] += proven_undispatched
            self.segment.update(stage="terminal", finished_at_utc=stamp(), dispatched=self.dispatched,
                                statuses=dict(self.statuses))
            atomic_write(self.run / SEGMENTS / (self.segment_id + ".json"), self.segment)
            self.progress(terminal=True)
            result = {"schema_version": 1, "run_id": self.settings["run_id"], "finished_at_utc": stamp(),
                      "amendment_sha256": self.amendment_sha256, "generation_exit_code": 0 if self.statuses["completed"] == len(self.cases) else 1,
                      "planned": len(self.cases), "statuses": dict(self.statuses), "retry_or_resampling": False}
            atomic_write(self.run / "shared_vllm_generation_completion.json", result)
            self.finished_result = result
            return result

    def finish_if_complete(self):
        with self.mutex:
            complete = sum(self.statuses.values()) == len(self.cases)
        if complete:
            self.finish()
            self.close()
