#!/usr/bin/env python3
"""Run unchanged frozen payloads through an explicitly amended local vLLM pool.

No server, scheduler job, scorer, uploader, source plan or frozen config is
started or modified here.  ``--check-only`` is a read-only migration inventory.
"""
from __future__ import annotations

import argparse
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
import fcntl
import json
from pathlib import Path
import signal
import sys
import threading
import urllib.request

from native_queue_scheduler import (NativeTaskQueue, QueueError,
                                    drive_bounded_queue, queue_limit)

from shared_vllm_resume import (MODEL, REVISION, ResumeError, Run, atomic_write,
                               file_sha, read, stamp, validate_endpoint,
                               negative_execution_records)


def normalize_plan_entry(root, original, worker):
    """Resolve infrastructure fields without modifying a frozen plan/config.

    The extended plans pin the runner digest in each entry but put its path
    only in the frozen configuration.  Other plans repeat the runner path.
    Context capacity and port may be declared once at worker level.
    """
    root = Path(root).resolve()
    entry = dict(original)
    required = ("task_id", "project_root", "config_path", "config_sha256", "run_id",
                "runner_sha256", "input_sha256", "generation_sha256", "case_count")
    inherited = {}
    for key in required:
        if key not in entry and key in worker:
            entry[key] = worker[key]
            inherited[key] = "worker"
        if key not in entry:
            raise ResumeError("Frozen source plan entry does not declare required field: " + key)
    project = (root / entry["project_root"]).resolve()
    config_path = (project / entry["config_path"]).resolve()
    if (not project.is_relative_to(root) or not config_path.is_relative_to(project)
            or file_sha(config_path) != entry["config_sha256"]):
        raise ResumeError("Frozen source configuration path/hash mismatch during entry normalization")
    config = read(config_path)
    if not entry.get("runner"):
        if worker.get("runner"):
            entry["runner"] = worker["runner"]
            inherited["runner"] = "worker"
        elif config.get("runner"):
            entry["runner"] = config["runner"]
            inherited["runner"] = "frozen_configuration"
        else:
            raise ResumeError("Frozen source configuration does not declare its runner")
    runner_path = (project / entry["runner"]).resolve()
    if (config.get("runner", entry["runner"]) != entry["runner"]
            or not runner_path.is_relative_to(project) or not runner_path.is_file()
            or file_sha(runner_path) != entry["runner_sha256"]):
        raise ResumeError("Normalized runner path/digest differs from the frozen configuration")
    context = entry.get("max_model_len", worker.get("max_model_len"))
    if type(context) is not int or context < 4097:
        raise ResumeError("Frozen source plan does not declare its context capacity")
    if "max_model_len" not in entry:
        inherited["max_model_len"] = "worker"
        entry["max_model_len"] = context
    if "port" not in entry and "port" in worker:
        entry["port"] = worker["port"]
        inherited["port"] = "worker"
    entry["minimum_context_tokens"] = context
    entry["inherited_field_sources"] = inherited
    return entry


def require_idle_endpoint(endpoint):
    """Refuse unaccounted work from an interrupted or independent client."""
    url = endpoint["endpoint"].removesuffix("/v1") + "/metrics"
    opener = urllib.request.build_opener(urllib.request.ProxyHandler({}))
    with opener.open(url, timeout=15) as response:
        raw = response.read(8 * 1024 * 1024).decode()
    counts = {"vllm:num_requests_running": [], "vllm:num_requests_waiting": []}
    for line in raw.splitlines():
        if line and not line.startswith("#"):
            fields = line.rsplit(None, 1)
            if len(fields) == 2 and fields[0].split("{", 1)[0] in counts:
                counts[fields[0].split("{", 1)[0]].append(float(fields[1]))
    if any(not values or sum(values) != 0 for values in counts.values()):
        raise ResumeError("A shared endpoint has active/unaccounted work or lacks idle counters")


def prepare_runs(runs, endpoints):
    """Join every independent preparation before allowing any model request.

    Helpers and all original run/endpoint locks are acquired by the caller.
    Each preparation touches only its own generation directory.  Waiting for
    every future also keeps locks held until all preparation writes stop if
    any sibling fails validation.
    """
    def prepare_one(state):
        state.prepare(endpoints)
        state.finish_if_complete()

    with ThreadPoolExecutor(max_workers=4, thread_name_prefix="run-prepare") as executor:
        futures = [executor.submit(prepare_one, state) for state in runs]
        failures = []
        for future in futures:
            try:
                future.result()
            except Exception as error:
                failures.append(error)
    if failures:
        raise ResumeError("Run preparation failed before any dispatch ("
                          + str(len(failures)) + " failed): " + str(failures[0])) from failures[0]


def load_amendment(root, path, expected_sha256, *, live=False):
    root, path = Path(root).resolve(), Path(path).resolve()
    if not path.is_relative_to(root) or file_sha(path) != expected_sha256:
        raise ResumeError("Infrastructure amendment path/hash mismatch")
    amendment = read(path)
    if (amendment.get("schema_version") != 1
            or amendment.get("kind") != "shared_vllm_infrastructure_amendment"
            or amendment.get("execution_authorized") is not True
            or amendment.get("infrastructure_only") is not True
            or amendment.get("execution_variant") != "saturation_native_queue_v1"
            or amendment.get("scheduler_policy") != "vllm_native_bounded_queue"
            or amendment.get("fairness") != "task_round_robin_then_run_round_robin"
            or amendment.get("scientific_protocol_changes") != []
            or amendment.get("model") != MODEL or amendment.get("model_revision") != REVISION):
        raise ResumeError("Infrastructure amendment is not explicitly authorized and protocol preserving")
    parent = amendment.get("parent_amendment", {})
    parent_path = (root / parent.get("path", "")).resolve()
    if not parent_path.is_relative_to(root) or not parent_path.is_file() or file_sha(parent_path) != parent.get("sha256"):
        raise ResumeError("The immutable parent amendment is not exactly pinned")
    parent_value = read(parent_path)
    for key in ("model", "model_revision", "source_registry", "source_plans", "run_context_checks",
                "continuation_run_directories", "continuation_source_snapshots", "negative_execution_receipts"):
        if amendment.get(key) != parent_value.get(key):
            raise ResumeError("Saturation changes the frozen parent scientific/source contract: " + key)
    selected = amendment.get("run_ids", [])
    if not selected or len(selected) != len(set(selected)) or not set(selected) <= set(parent_value.get("run_ids", [])):
        raise ResumeError("Each host requires an explicit nonempty subset of the frozen parent runs")
    if amendment.get("transport_timeout_seconds") != 14400:
        raise ResumeError("The native bounded queue requires its explicit 14400-second transport timeout")
    pins = amendment.get("adapter_files_sha256", {})
    for code in (Path(__file__).resolve(), Path(__file__).with_name("shared_vllm_resume.py").resolve(),
                 Path(__file__).with_name("native_queue_scheduler.py").resolve()):
        if pins.get(str(code)) != file_sha(code):
            raise ResumeError("Both actual continuation source files must be hash-pinned")
    for name, expected in pins.items():
        if not Path(name).resolve().is_relative_to(root) or file_sha(name) != expected:
            raise ResumeError("Pinned continuation source changed")
    evidence = amendment.get("capacity_evidence_files", [])
    if not evidence:
        raise ResumeError("Reviewed synthetic length/concurrency evidence must be hash-pinned")
    for item in evidence:
        path = (root / item["path"]).resolve()
        if not path.is_relative_to(root) or file_sha(path) != item["sha256"]:
            raise ResumeError("Capacity benchmark evidence changed")
    negative_execution_records(amendment, live=live)
    endpoints = [validate_endpoint(e, live=live) for e in amendment["endpoints"]]
    for endpoint in endpoints:
        queue_limit(endpoint)
    policy_pin = amendment.get("queue_policy", {})
    policy_path = (root / policy_pin.get("path", "")).resolve()
    if (not policy_path.is_relative_to(root) or not policy_path.is_file()
            or file_sha(policy_path) != policy_pin.get("sha256")):
        raise ResumeError("The reviewed queue policy must be exactly pinned")
    policy = read(policy_path)
    if (policy.get("schema_version") != 1 or policy.get("kind") != "shared_vllm_reviewed_queue_policy"
            or policy.get("reviewed") is not True or policy.get("scheduler_policy") != "vllm_native_bounded_queue"
            or policy.get("scientific_protocol_changes") != []
            or not str(policy.get("rationale", "")).strip()
            or any(e["queue_limit"] != policy.get("queue_limit")
                   or e["max_num_seqs"] != policy.get("server_max_num_seqs") for e in endpoints)
            or not any(item["sha256"] == policy.get("benchmark_summary_sha256") for item in evidence)
            or not any((root / item["path"]).resolve() == policy_path
                       and item["sha256"] == policy_pin["sha256"] for item in evidence)):
        raise ResumeError("Declared endpoint queues must match the reviewed benchmark policy")
    if not endpoints or len({e["endpoint_id"] for e in endpoints}) != len(endpoints):
        raise ResumeError("Shared endpoint identities must be nonempty and unique")
    uuids = [u for e in endpoints for u in e["server_identity"]["gpu_uuids"]]
    if len(uuids) != len(set(uuids)) or len(uuids) > 8:
        raise ResumeError("Shared endpoints overlap GPUs or exceed the eight-GPU ceiling")
    entries = []
    for source in amendment["source_plans"]:
        source_path = (root / source["path"]).resolve()
        if not source_path.is_relative_to(root) or file_sha(source_path) != source["sha256"]:
            raise ResumeError("An original source plan changed")
        plan = read(source_path)
        if plan.get("execution_authorized") is not True:
            raise ResumeError("Original source plan does not authorize execution")
        for worker in plan["workers"]:
            for original in worker["entries"]:
                if amendment.get("run_ids") is not None and original["run_id"] not in amendment["run_ids"]:
                    continue
                entry = {**normalize_plan_entry(root, original, worker),
                         "source_plan": str(source_path), "source_plan_sha256": source["sha256"]}
                if not any(e["max_model_len"] >= entry["minimum_context_tokens"] for e in endpoints):
                    raise ResumeError("No shared endpoint preserves the frozen run's context capacity")
                entries.append(entry)
    ids = [e["run_id"] for e in entries]
    if len(ids) != len(set(ids)) or (amendment.get("run_ids") is not None and set(ids) != set(amendment["run_ids"])):
        raise ResumeError("Continuation run scope is duplicated or not in the frozen plans")
    return amendment, endpoints, entries


def run(root, amendment_path, expected_sha256, *, check_only=False):
    root, amendment_path = Path(root).resolve(), Path(amendment_path).resolve()
    amendment, endpoints, entries = load_amendment(root, amendment_path, expected_sha256, live=not check_only)
    runs, skipped, inventory, case_identities = [], [], [], set()
    for entry in entries:
        folder = root / entry["project_root"] / "results/runs" / entry["run_id"]
        if (folder / "completion.json").exists() and entry["run_id"] not in amendment.get("continuation_run_directories", {}):
            skipped.append(entry["run_id"])
            continue
        state = Run(entry, root, amendment, amendment_path, expected_sha256)
        current = {(c["task"], c["variant"], c["case_id"]) for c in state.cases}
        if case_identities.intersection(current):
            raise ResumeError("A native case appears in multiple selected generation runs")
        case_identities.update(current)
        runs.append(state)
    if check_only:
        for state in runs:
            counts = state.inventory()
            inventory.append({"run_id": state.entry["run_id"], "task_id": state.entry["task_id"],
                              "planned": len(state.cases),
                              "minimum_context_tokens": state.entry["minimum_context_tokens"],
                              "case_states": dict(counts)})
        return {"stage": "checked_not_executed", "active_or_pending_runs": inventory,
                "terminal_runs_skipped": skipped, "endpoints": len(endpoints),
                "gpu_count": sum(e["tensor_parallel_size"] for e in endpoints),
                "checks_do_not_prove_old_clients_drained": True}
    # Acquire every original generation/worker lock before creating any new
    # provenance or contacting an inference endpoint.
    endpoint_locks = []
    try:
        for endpoint in sorted(endpoints, key=lambda e: e["server_identity_sha256"]):
            lock_path = root / ".local/shared_vllm_endpoint_locks" / (endpoint["server_identity_sha256"] + ".lock")
            lock_path.parent.mkdir(parents=True, exist_ok=True)
            handle = lock_path.open("a")
            try:
                fcntl.flock(handle, fcntl.LOCK_EX | fcntl.LOCK_NB)
            except BlockingIOError as error:
                handle.close()
                raise ResumeError("A shared endpoint already belongs to another dispatcher") from error
            endpoint_locks.append(handle)
        for state in runs:
            state.acquire()
        for endpoint in endpoints:
            require_idle_endpoint(endpoint)
            if runs:
                code, response = runs[0].helper.call(endpoint["endpoint"] + "/models", timeout=15)
                if code != 200 or not any(m.get("id") == MODEL for m in response.get("data", [])):
                    raise ResumeError("Pinned model is unavailable on a declared shared endpoint")
        prepare_runs(runs, endpoints)
        stopped = threading.Event()
        operator_pause = threading.Event()
        def pause_signal(signum, frame):
            operator_pause.set()
            stopped.set()
        old_signals = {sig: signal.signal(sig, pause_signal) for sig in (signal.SIGTERM, signal.SIGINT)}
        queue = NativeTaskQueue(runs, endpoints)
        try:
            metrics = drive_bounded_queue(queue, endpoints, stopped,
                lambda state, case, name, endpoint, event: state.dispatch(case, name, endpoint, event),
                lambda state: state.finish_if_complete())
            results = []
            for state in runs:
                counts = state.inventory()
                pending = counts.get("undispatched", 0) + counts.get("undispatched_proven_never_executed", 0)
                results.append(state.pause() if pending else state.finish())
        finally:
            for sig, previous in old_signals.items():
                signal.signal(sig, previous)
        failed = bool(metrics["infrastructure_error_types"]) or any(
            state.statuses.get(key, 0) for state in runs
            for key in ("transport_error", "server_error", "interrupted_unknown_completion", "unknown_saved_response"))
        paused = any(value.get("stage") == "paused" for value in results)
        if paused and not operator_pause.is_set():
            failed = True
        return {"stage": "generation_paused" if paused else "generation_terminal",
                "amendment_sha256": expected_sha256, "finished_at_utc": stamp(),
                "runs": results, "terminal_runs_skipped": skipped, "scheduler": metrics,
                "operator_pause": operator_pause.is_set(), "generation_exit_code": 1 if failed else 0,
                "generation_protocol_changes": [], "scoring_performed": False}

    finally:
        for state in runs:
            state.close()
        for handle in reversed(endpoint_locks):
            handle.close()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, required=True)
    parser.add_argument("--amendment", type=Path, required=True)
    parser.add_argument("--amendment-sha256", required=True)
    parser.add_argument("--check-only", action="store_true")
    args = parser.parse_args()
    try:
        result = run(args.root, args.amendment, args.amendment_sha256, check_only=args.check_only)
    except (ResumeError, QueueError, ValueError, OSError) as error:
        print(json.dumps({"stage": "refused", "error_type": type(error).__name__, "reason": str(error)}), flush=True)
        return 1
    print(json.dumps(result, indent=2), flush=True)
    return result.get("generation_exit_code", 0)


if __name__ == "__main__":
    raise SystemExit(main())
