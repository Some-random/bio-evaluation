#!/usr/bin/env python3
"""Read-only shared-pool health and response-format monitoring, without scoring.

Only GET /models and /metrics are called. Response text is used solely to test
whether the final field is empty; text, reasoning, prompts and labels are never
copied to monitoring state or reports. No retry or protocol change is performed.
"""

from __future__ import annotations

import argparse
from collections import Counter
from datetime import datetime
import fcntl
import hashlib
import json
import os
from pathlib import Path
import signal
import socket
import time
from urllib.parse import urlsplit
from urllib.request import ProxyHandler, build_opener
from zoneinfo import ZoneInfo


STOP = False
PACIFIC = ZoneInfo("America/Los_Angeles")


def now():
    return datetime.now(PACIFIC).isoformat()


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read(path):
    return json.loads(Path(path).read_text())


def write(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name + ".tmp")
    temporary.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n")
    temporary.chmod(0o600)
    temporary.replace(path)


def pinned(path, expected):
    if sha(path) != expected:
        raise ValueError("A frozen health-monitor dependency changed: " + Path(path).name)
    return read(path)


def scopes_from_amendment(root, amendment):
    scopes = {}
    selected = set(amendment["run_ids"]) if amendment.get("run_ids") is not None else None
    for source in amendment["source_plans"]:
        source_path = (root / source["path"]).resolve()
        if not source_path.is_relative_to(root):
            raise ValueError("A source plan leaves the monitored workspace")
        plan = pinned(source_path, source["sha256"])
        for worker in plan["workers"]:
            for entry in worker["entries"]:
                logical = entry["run_id"]
                if selected is not None and logical not in selected:
                    continue
                if logical in scopes:
                    raise ValueError("Duplicate logical run would double-count responses")
                project = Path(entry["project_root"]).resolve()
                default = project / "results/runs" / logical
                directory = Path(amendment.get("continuation_run_directories", {}).get(logical, default)).resolve()
                if not directory.is_relative_to(root) or directory.parent != default.parent:
                    raise ValueError("Health response scope leaves its frozen source project")
                scopes[logical] = {"logical_run_id": logical, "storage_run_id": directory.name, "run_directory": str(directory), "task_id": entry["task_id"], "planned": entry["case_count"],
                                   "requires_saturation": amendment.get("execution_variant") == "saturation_native_queue_v1"}
    if selected is not None and set(scopes) != selected:
        raise ValueError("Health scopes differ from the frozen amendment's logical run IDs")
    return list(scopes.values())


def metric_values(raw):
    mapping = {"vllm:num_requests_running": "running", "vllm:num_requests_waiting": "waiting", "vllm:kv_cache_usage_perc": "kv_fraction", "vllm:num_preemptions_total": "preemptions", "vllm:generation_tokens_total": "generation_tokens", "vllm:prompt_tokens_total": "prompt_tokens"}
    collected = {}
    for line in raw.splitlines():
        if not line or line.startswith("#"):
            continue
        try:
            metric, value = line.rsplit(None, 1)
            key = mapping.get(metric.split("{", 1)[0])
            if key:
                collected.setdefault(key, []).append(float(value))
        except ValueError:
            continue
    return {key: (max(values) if key == "kv_fraction" else sum(values)) for key, values in collected.items()}


def process_ticks(pid):
    fields = (Path("/proc") / str(pid) / "stat").read_text().rsplit(")", 1)[1].split()
    if fields[0] in {"Z", "T", "t"}:
        raise ValueError("The API process is stopped or dead")
    return fields[19]


def observe_endpoint(endpoint, pool_plan, opener):
    identity = pinned(endpoint["server_identity_file"], endpoint["server_identity_sha256"])
    if (identity.get("model") != pool_plan["model"] or identity.get("revision") != pool_plan["revision"] or identity.get("dtype") not in {"bf16", "bfloat16"} or identity.get("tensor_parallel_size") != 1 or identity.get("endpoint") != endpoint["endpoint"] or identity.get("max_model_len") != pool_plan["max_model_len"] or identity.get("max_num_seqs") != pool_plan["max_num_seqs"]):
        raise ValueError("Endpoint identity differs from the frozen BF16 pool")
    if identity.get("hostname") not in {socket.gethostname(), socket.getfqdn()} or str(identity.get("proc_start_ticks")) != process_ticks(identity["pid"]):
        raise ValueError("Endpoint host/PID identity does not match this pool host")
    uuids = identity.get("gpu_uuids", [])
    if len(uuids) != 1 or not all(isinstance(value, str) and value.startswith("GPU-") for value in uuids):
        raise ValueError("Replica must have one observed GPU UUID")
    url = urlsplit(endpoint["endpoint"])
    if url.scheme != "http" or url.hostname != "127.0.0.1" or url.path != "/v1" or url.username or url.password or url.query or url.fragment:
        raise ValueError("Only declared loopback endpoints may be observed")
    with opener.open(endpoint["endpoint"] + "/models", timeout=5) as response:
        models = json.load(response)
    if not any(row.get("id") == pool_plan["model"] for row in models.get("data", [])):
        raise ValueError("The API is not serving the pinned model identifier")
    with opener.open(endpoint["endpoint"].removesuffix("/v1") + "/metrics", timeout=5) as response:
        metrics = metric_values(response.read().decode())
    if not {"running", "waiting", "kv_fraction", "preemptions"} <= set(metrics):
        raise ValueError("Required running/waiting/KV/preemption metrics are missing")
    return {"endpoint_id": endpoint["endpoint_id"], "server_identity_sha256": endpoint["server_identity_sha256"], "gpu_uuids": uuids, "healthy": True, "metrics": metrics}


def response_metadata(raw):
    record = json.loads(raw)
    response = record.get("response") or {}
    choices = response.get("choices") or []
    choice = choices[0] if choices else {}
    final = (choice.get("message") or {}).get("content")
    empty = not final.strip() if isinstance(final, str) else not bool(final)
    usage = response.get("usage") or {}
    saved = record.get("saved_at_utc") or record.get("saved_at_pacific")
    saved_at = datetime.fromisoformat(saved.replace("Z", "+00:00")).astimezone(PACIFIC).isoformat() if saved else None
    return {"status": record.get("status"), "http_status": record.get("http_status"), "finish_reason": record.get("finish_reason") or choice.get("finish_reason"), "empty_final": empty, "saved_at_pacific": saved_at, "completion_tokens": usage.get("completion_tokens"), "prompt_tokens": usage.get("prompt_tokens")}


def scan_response_metadata(scopes, cache):
    runs, events, flags = [], [], []
    for scope in scopes:
        folder = Path(scope["run_directory"])
        response_names = {path.name for path in (folder / "responses").glob("*.json")}
        request_count = sum(1 for _ in (folder / "requests").glob("*.json"))
        shared_names = {path.name for kind in ("shared_vllm_dispatch", "shared_vllm_saturation_dispatch")
                        for path in (folder / kind).glob("*.json")}
        for filename in sorted(response_names & shared_names):
            path = folder / "responses" / filename
            info = path.stat()
            key = scope["logical_run_id"] + "/" + filename
            signature = [info.st_size, info.st_mtime_ns]
            previous = cache.get(key)
            if previous and previous["signature"] == signature:
                continue
            raw = path.read_bytes()
            checksum = hashlib.sha256(raw).hexdigest()
            if previous and previous["sha256"] != checksum:
                flags.append({"type": "immutable_response_changed", "logical_run_id": scope["logical_run_id"], "filename": filename})
                continue
            metadata = response_metadata(raw)
            cache[key] = {"signature": signature, "sha256": checksum, "logical_run_id": scope["logical_run_id"], "filename": filename, "metadata": metadata}
            if previous is None:
                events.append({"logical_run_id": scope["logical_run_id"], "filename": filename, **metadata})
        entries = [value["metadata"] for key, value in cache.items() if value["logical_run_id"] == scope["logical_run_id"]]
        finishes = Counter(str(value["finish_reason"]) for value in entries)
        statuses = Counter(str(value["http_status"]) for value in entries)
        saved_times = [value["saved_at_pacific"] for value in entries if value["saved_at_pacific"]]
        done_name = ("shared_vllm_saturation_generation_completion.json"
                     if scope.get("requires_saturation") or (folder / "shared_vllm_saturation_amendment.json").exists()
                     else "shared_vllm_generation_completion.json")
        done_path = folder / done_name
        done = read(done_path) if done_path.is_file() else None
        terminal = bool(done and done.get("run_id") == scope["logical_run_id"] and done.get("planned") == scope["planned"])
        runs.append({key: scope[key] for key in ("logical_run_id", "storage_run_id", "task_id", "planned")} | {"requests_saved": request_count, "responses_saved": len(response_names), "shared_response_metadata_scanned": len(entries), "historical_responses_not_scanned": len(response_names - shared_names), "generation_terminal": terminal, "generation_exit_code": done.get("generation_exit_code") if terminal else None, "finish_reasons": dict(finishes), "http_statuses": dict(statuses), "empty_final_count": sum(value["empty_final"] for value in entries), "latest_shared_response_at_pacific": max(saved_times) if saved_times else None})
    return runs, events, flags


def cycle(plan_path, expected_hash):
    plan = pinned(plan_path, expected_hash)
    if plan.get("schema_version") != 1 or not 1 <= plan.get("interval_seconds", 60) <= 60:
        raise ValueError("Require a frozen v1 health plan with interval at most 60 seconds")
    root, pool = Path(plan["root"]).resolve(), Path(plan["pool_directory"]).resolve()
    if not pool.is_relative_to(root / ".local") or not Path(plan["endpoints_file"]).resolve().is_relative_to(pool) or not Path(plan["amendment_path"]).resolve().is_relative_to(root / ".local"):
        raise ValueError("Pool identity sources must remain inside declared project-local state")
    for name, expected in plan.get("code_files_sha256", {}).items():
        if sha(name) != expected:
            raise ValueError("Frozen health watcher code changed")
    pool_plan = pinned(pool / plan.get("pool_plan_filename", "plan.json"), plan["pool_plan_sha256"])
    endpoints = pinned(plan["endpoints_file"], plan["endpoints_sha256"])
    amendment = pinned(plan["amendment_path"], plan["amendment_sha256"])
    if amendment.get("kind") != "shared_vllm_infrastructure_amendment" or amendment.get("execution_authorized") is not True or amendment.get("scientific_protocol_changes") != []:
        raise ValueError("Health scopes require an authorized protocol-preserving amendment")
    if amendment.get("model") != pool_plan["model"] or amendment.get("model_revision") != pool_plan["revision"]:
        raise ValueError("Health amendment and pool refer to different checkpoints")
    for evidence in amendment.get("capacity_evidence_files", []):
        if sha((root / evidence["path"]).resolve()) != evidence["sha256"]:
            raise ValueError("Frozen capacity evidence changed")
    scopes = scopes_from_amendment(root, amendment)
    state_file = Path(plan["state_file"])
    if not state_file.resolve().is_relative_to(root / ".local"):
        raise ValueError("Private health cache must stay in project-local state")
    if plan.get("public_output_file") and not any(Path(plan["public_output_file"]).resolve().is_relative_to(allowed) for allowed in (root / "reports", root / "results", pool)):
        raise ValueError("Public health output is outside the declared artifact locations")
    previous = read(state_file) if state_file.is_file() else {"plan_sha256": expected_hash, "response_cache": {}, "endpoint_history": {}}
    if previous.get("plan_sha256") != expected_hash:
        raise ValueError("Health state belongs to another frozen plan")
    epoch = time.time()
    flags, observed = [], []
    opener = build_opener(ProxyHandler({}))
    for endpoint in endpoints:
        try:
            row = observe_endpoint(endpoint, pool_plan, opener)
            metrics = row["metrics"]
            old = previous["endpoint_history"].get(row["endpoint_id"], {})
            old_metrics = old.get("metrics", {})
            row["preemption_delta"] = metrics["preemptions"] - old_metrics["preemptions"] if old_metrics.get("preemptions") is not None and metrics["preemptions"] >= old_metrics["preemptions"] else None
            progressed = metrics.get("generation_tokens", 0) > old_metrics.get("generation_tokens", 0) or metrics.get("prompt_tokens", 0) > old_metrics.get("prompt_tokens", 0)
            busy = metrics["running"] + metrics["waiting"] > 0
            was_busy = old_metrics.get("running", 0) + old_metrics.get("waiting", 0) > 0
            last_activity = epoch if progressed or not old or not busy or not was_busy else old.get("last_activity_epoch", epoch)
            row["seconds_without_token_progress"] = max(0, epoch - last_activity)
            if row["preemption_delta"] and row["preemption_delta"] > 0:
                flags.append({"type": "preemptions_increased", "endpoint_id": row["endpoint_id"], "delta": row["preemption_delta"]})
            if metrics["kv_fraction"] >= plan.get("thresholds", {}).get("high_kv_fraction", .95):
                flags.append({"type": "high_kv_usage", "endpoint_id": row["endpoint_id"], "fraction": metrics["kv_fraction"]})
            if busy and {"generation_tokens", "prompt_tokens"} & set(metrics) and row["seconds_without_token_progress"] >= plan.get("thresholds", {}).get("stall_seconds", 600):
                flags.append({"type": "inflight_without_observed_token_progress", "endpoint_id": row["endpoint_id"], "seconds": row["seconds_without_token_progress"]})
            previous["endpoint_history"][row["endpoint_id"]] = {"metrics": metrics, "last_activity_epoch": last_activity}
        except Exception as error:
            row = {"endpoint_id": endpoint["endpoint_id"], "healthy": False, "error_type": type(error).__name__, "reason": str(error)[:200]}
            flags.append({"type": "endpoint_health_failed", "endpoint_id": endpoint["endpoint_id"], "error_type": type(error).__name__})
        observed.append(row)
    uuids = [uuid for row in observed for uuid in row.get("gpu_uuids", [])]
    if len(uuids) != len(set(uuids)) or len(uuids) != pool_plan["replicas"]:
        flags.append({"type": "gpu_identity_overlap_or_missing_replica"})
    runs, events, response_flags = scan_response_metadata(scopes, previous["response_cache"])
    flags += response_flags
    metadata = [value["metadata"] for value in previous["response_cache"].values()]
    errors = sum(value["http_status"] != 200 or value["status"] != "completed" for value in metadata)
    truncated = sum(value["finish_reason"] == "length" for value in metadata)
    minimum = plan.get("thresholds", {}).get("minimum_responses_for_format_warning", 20)
    if errors:
        flags.append({"type": "saved_transport_or_server_errors", "count": errors})
    if len(metadata) >= minimum and truncated / len(metadata) >= plan.get("thresholds", {}).get("high_truncation_fraction", .5):
        flags.append({"type": "high_length_finish_fraction", "fraction": truncated / len(metadata), "responses": len(metadata)})
    status_path = pool / plan.get("pool_status_filename", "status.json")
    pool_state = read(status_path) if status_path.is_file() else {}
    if pool_state.get("stage") in {"failed", "benchmark_failed"}:
        flags.append({"type": "pool_reports_failure", "stage": pool_state["stage"]})
    pool_updated = datetime.fromisoformat(pool_state["updated_at"].replace("Z", "+00:00")).astimezone(PACIFIC) if pool_state.get("updated_at") else None
    report = {"schema_version": 1, "updated_at_pacific": now(), "plan_sha256": expected_hash, "pool_stage": pool_state.get("stage", "unknown"), "pool_stage_source_updated_at_pacific": pool_updated.isoformat() if pool_updated else None, "pool_stage_source_age_seconds": max(0, epoch - pool_updated.timestamp()) if pool_updated else None, "pool_stage_timestamp_is_not_a_runtime_heartbeat": True, "logical_scope_count": len(scopes), "planned_native_cases": sum(scope["planned"] for scope in scopes), "saved_responses_unique_logical_sources": sum(run["responses_saved"] for run in runs), "endpoints": observed, "runs": runs, "response_format": {"shared_response_metadata_scanned": len(metadata), "new_responses_since_last_check": len(events), "length_finish_count": truncated, "empty_final_count": sum(value["empty_final"] for value in metadata), "transport_or_server_error_count": errors}, "recent_response_metadata": events[-20:], "flags": flags, "automatic_actions": [], "inference_scoring_or_native_parsing_performed": False, "interpretation": "Operational and output-format checks only; saved responses and nonempty final fields are not benchmark scores or correctness judgments."}
    previous.update(updated_at_pacific=report["updated_at_pacific"], last_report=report)
    write(state_file, previous)
    if plan.get("public_output_file"):
        write(plan["public_output_file"], report)
    return report, plan.get("interval_seconds", 60)


def watch(args):
    global STOP
    def stop(signum, frame):
        global STOP
        STOP = True
    signal.signal(signal.SIGTERM, stop)
    signal.signal(signal.SIGINT, stop)
    while not STOP:
        try:
            report, interval = cycle(args.plan, args.plan_sha256)
            print(json.dumps({"updated_at_pacific": report["updated_at_pacific"], "saved_responses": report["saved_responses_unique_logical_sources"], "flag_types": [flag["type"] for flag in report["flags"]]}), flush=True)
        except Exception as error:
            # Preserve the previous successful response cache and report.
            write(args.plan.with_suffix(".health_error.json"), {"updated_at_pacific": now(), "error_type": type(error).__name__, "last_successful_report_preserved": True, "automatic_actions": []})
            if args.once:
                return 1
            interval = 60
        if args.once:
            return 0
        for _ in range(interval):
            if STOP:
                break
            time.sleep(1)
    return 0


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--plan", type=Path, required=True)
    parser.add_argument("--plan-sha256", required=True)
    parser.add_argument("--once", action="store_true")
    args = parser.parse_args()
    with args.plan.with_suffix(".health.lock").open("a") as lock:
        fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        return watch(args)


if __name__ == "__main__":
    raise SystemExit(main())
