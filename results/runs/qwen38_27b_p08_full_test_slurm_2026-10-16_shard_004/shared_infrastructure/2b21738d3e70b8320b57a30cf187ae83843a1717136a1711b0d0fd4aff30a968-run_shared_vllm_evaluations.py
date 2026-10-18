#!/usr/bin/env python3
"""Run unchanged frozen payloads through an explicitly amended local vLLM pool.

No server, scheduler job, scorer, uploader, source plan or frozen config is
started or modified here.  ``--check-only`` is a read-only migration inventory.
"""
from __future__ import annotations

import argparse
import concurrent.futures
from collections import Counter
import fcntl
import json
from pathlib import Path
import signal
import sys
import threading
from fractions import Fraction
import urllib.request

from shared_vllm_resume import (MODEL, REVISION, ResumeError, Run, atomic_write,
                               file_sha, read, stamp, validate_endpoint,
                               negative_execution_records, admission_weight)


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


def load_amendment(root, path, expected_sha256, *, live=False):
    root, path = Path(root).resolve(), Path(path).resolve()
    if not path.is_relative_to(root) or file_sha(path) != expected_sha256:
        raise ResumeError("Infrastructure amendment path/hash mismatch")
    amendment = read(path)
    if (amendment.get("schema_version") != 1
            or amendment.get("kind") != "shared_vllm_infrastructure_amendment"
            or amendment.get("execution_authorized") is not True
            or amendment.get("infrastructure_only") is not True
            or amendment.get("scientific_protocol_changes") != []
            or amendment.get("model") != MODEL or amendment.get("model_revision") != REVISION):
        raise ResumeError("Infrastructure amendment is not explicitly authorized and protocol preserving")
    pins = amendment.get("adapter_files_sha256", {})
    for code in (Path(__file__).resolve(), Path(__file__).with_name("shared_vllm_resume.py").resolve()):
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
        counts = state.inventory()
        inventory.append({"run_id": entry["run_id"], "task_id": entry["task_id"], "planned": len(state.cases),
                          "minimum_context_tokens": entry["minimum_context_tokens"], "case_states": dict(counts)})
        runs.append(state)
    if check_only:
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
        for state in runs:
            state.prepare(endpoints)
            state.finish_if_complete()
        stopped = threading.Event()
        def stop(signum, frame):
            stopped.set()
        old_signals = {sig: signal.signal(sig, stop) for sig in (signal.SIGTERM, signal.SIGINT)}
        scheduler_mutex = threading.Condition()
        pending = [iter(state.pending()) for state in runs]
        heads = {}
        exhausted = set()
        cursor = [0]
        reserved = {e["endpoint_id"]: Fraction(0) for e in endpoints}
        waiting_tickets = {}
        errors = []
        def take(endpoint):
            with scheduler_mutex:
                while not stopped.is_set():
                    endpoint_id = endpoint["endpoint_id"]
                    ticket = waiting_tickets.get(endpoint_id)
                    if ticket is not None:
                        state, case, name, weight = ticket
                        if reserved[endpoint_id] + weight <= 1:
                            reserved[endpoint_id] += weight
                            del waiting_tickets[endpoint_id]
                            return ticket
                        # This endpoint's next case owns the next admission.
                        # Other workers must not refill its released fractions
                        # with short requests while a long prompt is waiting.
                        # No claim/request file is written until it is admitted.
                        scheduler_mutex.wait(timeout=1)
                        continue
                    eligible_remaining = False
                    for _ in range(len(runs)):
                        index = cursor[0] % len(runs)
                        cursor[0] += 1
                        if index in exhausted or endpoint["max_model_len"] < runs[index].entry["minimum_context_tokens"]:
                            continue
                        if index not in heads:
                            try:
                                heads[index] = next(pending[index])
                            except StopIteration:
                                exhausted.add(index)
                                continue
                        case, name = heads[index]
                        count = runs[index].prompt_tokens[case["case_id"]]
                        try:
                            weight = admission_weight(endpoint, count)
                        except ResumeError:
                            continue
                        if count + 4096 > endpoint["max_model_len"]:
                            continue
                        eligible_remaining = True
                        if reserved[endpoint["endpoint_id"]] + weight <= 1:
                            reserved[endpoint["endpoint_id"]] += weight
                            del heads[index]
                            return runs[index], case, name, weight
                        waiting_tickets[endpoint_id] = (runs[index], case, name, weight)
                        del heads[index]
                        # The case is now exclusive to this endpoint in RAM;
                        # other endpoints can advance this run's global iterator.
                        break
                    if not eligible_remaining:
                        return None
                    scheduler_mutex.wait(timeout=1)
                return None
        def worker(endpoint):
            while not stopped.is_set():
                selected = take(endpoint)
                if selected is None:
                    return
                state, case, name, weight = selected
                try:
                    state.dispatch(case, name, endpoint, stopped)
                except Exception as error:
                    # Never retry after an exception.  A saved claim/request is
                    # retained as ambiguous and will fail closed on continuation.
                    stopped.set()
                    with scheduler_mutex:
                        errors.append(type(error).__name__)
                    return
                finally:
                    with scheduler_mutex:
                        reserved[endpoint["endpoint_id"]] -= weight
                        scheduler_mutex.notify_all()
                    state.finish_if_complete()
        try:
            capacity = sum(e["max_inflight"] for e in endpoints)
            with concurrent.futures.ThreadPoolExecutor(max_workers=capacity) as pool:
                futures = [pool.submit(worker, endpoint) for endpoint in endpoints for _ in range(endpoint["max_inflight"])]
                for future in futures:
                    future.result()
            finished = [state.finish() for state in runs]
        finally:
            for sig, previous in old_signals.items():
                signal.signal(sig, previous)
        return {"stage": "generation_terminal", "amendment_sha256": expected_sha256, "finished_at_utc": stamp(),
                "runs": finished, "terminal_runs_skipped": skipped, "infrastructure_error_types": errors,
                "generation_exit_code": 1 if errors or any(r["generation_exit_code"] for r in finished) else 0,
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
    except (ResumeError, ValueError, OSError) as error:
        print(json.dumps({"stage": "refused", "error_type": type(error).__name__, "reason": str(error)}), flush=True)
        return 1
    print(json.dumps(result, indent=2), flush=True)
    return result.get("generation_exit_code", 0)


if __name__ == "__main__":
    raise SystemExit(main())
