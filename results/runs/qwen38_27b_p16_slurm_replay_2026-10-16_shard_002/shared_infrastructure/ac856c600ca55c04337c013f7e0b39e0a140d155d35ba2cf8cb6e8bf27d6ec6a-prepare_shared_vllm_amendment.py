#!/usr/bin/env python3
"""Assemble a new immutable infrastructure amendment from existing evidence.

No inference, scoring, scheduler actions, source edits or publication occurs.
Use --check-only while pool benchmarks or missing context preflights run.
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
import sys

from shared_vllm_resume import (MODEL, REVISION, ResumeError, atomic_write,
                               file_sha, negative_execution_records, read,
                               stamp, validate_endpoint)


CAPACITY_EXCLUSIONS = {
    "replica_2/length_benchmark_192": "Failed its idle-server preflight; no valid measured capacity point.",
    "replica_3/length_benchmark": "Original 45056-token benchmark overlapped the prematurely started 49152-token client; token counters prove concurrent unrelated work.",
    "replica_3/length_benchmark_49152": "Prematurely started while the original 45056-token benchmark was active; boundary and token counters prove concurrent unrelated work.",
}
REQUIRED_CAPACITY_PROFILES = (192, 1536, 7000, 16384, 45056, 49152)


def pinned(path):
    path = Path(path).resolve()
    return {"path": str(path), "sha256": file_sha(path)}


def excluded_capacity_evidence(pool_dir):
    """Record excluded attempts byte-for-byte without deleting or repairing them."""
    root = Path(pool_dir).resolve()
    result = []
    for relative, reason in CAPACITY_EXCLUSIONS.items():
        directory = root / relative
        if not directory.exists():
            continue
        files = {}
        for path in sorted(directory.rglob("*")):
            if path.is_symlink():
                raise ResumeError("Excluded benchmark evidence contains a symbolic link")
            if path.is_file():
                files[path.relative_to(directory).as_posix()] = file_sha(path)
        result.append({"directory": str(directory), "relative_directory": relative,
                       "excluded_from_admission": True, "reason": reason, "files_sha256": files})
    return result


def exclusive_measurement(row, directory):
    """Require measured token counters and queue boundaries to match this batch."""
    measured = row["measured"]
    def value(side, metric):
        values = [v for k, v in measured.get(side, {}).get("selected", {}).items()
                  if k.startswith(metric + "{")]
        if not values or any(not isinstance(v, (int, float)) or not math.isfinite(v) for v in values):
            return None
        return sum(values)
    for metric, expected in (("vllm:prompt_tokens_total", measured["actual_prompt_tokens"]),
                             ("vllm:generation_tokens_total", measured["actual_completion_tokens"])):
        before, after = value("metrics_before", metric), value("metrics_after", metric)
        if before is None or after is None or after - before != expected:
            return False, []
    for side in ("metrics_before", "metrics_after"):
        for metric in ("vllm:num_requests_running", "vllm:num_requests_waiting"):
            if value(side, metric) != 0:
                return False, []
    samples = row.get("monitoring", {}).get("sample_file")
    evidence = []
    if samples:
        path = Path(samples).resolve()
        if not path.is_relative_to(Path(directory).resolve()) or not path.is_file():
            return False, []
        for line in path.read_text().splitlines():
            sample = json.loads(line)
            running, waiting = sample.get("running"), sample.get("waiting")
            if (running is None or waiting is None or running < 0 or waiting < 0
                    or running + waiting > row["concurrency"]):
                return False, []
        evidence.append(pinned(path))
    return True, evidence


def measured_limits(pool_dir):
    """Use completed eligible measured points, with conservative monotone caps."""
    pool_dir = Path(pool_dir)
    profiles, evidence, missing = {}, [], []
    for directory in sorted(p for p in pool_dir.glob("replica_*/length_benchmark*") if p.is_dir()):
        if directory.relative_to(pool_dir).as_posix() in CAPACITY_EXCLUSIONS:
            continue
        result_path = directory / "results.json"
        summary_path = directory / "measured_concurrency_by_input_length.json"
        progress_path = directory / "progress.json"
        if not all(p.is_file() for p in (result_path, summary_path, progress_path)):
            missing.append(str(directory))
            continue
        if read(progress_path).get("state") != "completed":
            missing.append(str(directory))
            continue
        result, summary = read(result_path), read(summary_path)
        plan = result["plan"]
        if (plan.get("model") != MODEL or plan.get("revision") != REVISION
                or plan.get("output_tokens") != 4096 or plan.get("synthetic_only") is not True):
            raise ResumeError("Capacity evidence changes model or the fixed synthetic output budget")
        evidence.extend([pinned(result_path), pinned(summary_path), pinned(progress_path)])
        for point in summary["points"]:
            length, cap = point["tested_input_tokens"], point.get("best_tested_concurrency")
            if point.get("tested_output_tokens") != 4096 or type(cap) is not int or not 1 <= cap <= 32:
                raise ResumeError("A length profile has no eligible measured concurrency")
            valid = {}
            for candidate in result["rows"]:
                if candidate.get("input_tokens") == length and candidate.get("state") == "measured" and candidate.get("eligible") is True:
                    exclusive, sample_evidence = exclusive_measurement(candidate, directory)
                    if exclusive:
                        valid[candidate["concurrency"]] = candidate
                        evidence.extend(sample_evidence)
            row = valid.get(cap)
            if row is None:
                raise ResumeError("A recommended capacity point is unmeasured, ineligible or has evidence of other concurrent work")
            measured, monitoring = row["measured"], row["monitoring"]
            if (measured.get("failed_requests") != 0 or measured.get("fixed_workload_mismatch_requests") != 0
                    or measured.get("successful_requests") != cap or measured.get("planned_requests") != cap
                    or measured.get("actual_prompt_tokens") != length * cap
                    or measured.get("actual_completion_tokens") != 4096 * cap
                    or measured.get("comparable_fixed_workload") is not True
                    or monitoring.get("preemption_delta") != 0):
                raise ResumeError("A selected capacity point failed its request/token/counter checks")
            if length in profiles:
                raise ResumeError("Duplicate measured capacity profile; choose an explicit evidence set")
            profiles[length] = {"cap": cap, "valid_caps": set(valid), "evidence_sha256": file_sha(result_path)}
    expected = REQUIRED_CAPACITY_PROFILES
    if not set(expected) <= set(profiles):
        missing.extend("input_tokens=" + str(length) for length in expected if length not in profiles)
    limits, previous = [], 32
    for length in sorted(profiles):
        profile = profiles[length]
        cap = min(previous, profile["cap"])
        if cap not in profile["valid_caps"]:
            raise ResumeError("A conservative monotone cap has not itself been measured")
        limits.append({"max_prompt_tokens": length, "max_inflight": cap,
                       "capacity_evidence_sha256": profile["evidence_sha256"]})
        previous = cap
    return limits, evidence, missing


def context_index(path):
    if path is None:
        return {}
    value = read(path)
    if isinstance(value, dict) and "runs" in value:
        result = {}
        for run in value["runs"]:
            reports = [r for r in run.get("context_reports", []) if r.get("complete_per_case_tokens")]
            if reports:
                result[run["run_id"]] = {k: reports[0][k] for k in ("path", "sha256")}
        return result
    return value


def checked_context(root, project, cfg, count, index):
    run_id = cfg["run_id"]
    record = index.get(run_id)
    if record is None:
        candidates = [project / "results/runs" / run_id / "context_check.json"]
        candidates += sorted((root / ".local/remaining_evaluations/status").glob("*/" + run_id + "/context_check.json"))
        candidates += [root / ".local/remaining_evaluations" / (project.name + "_preflight") / run_id / "context_check.json"]
        candidates += [root / ".local/shared_vllm_migration_2026-10-17/context_checks" / task / "context_check.json"
                       for task in cfg.get("approved_task_ids", [])]
        source = next((p for p in candidates if p.is_file()), None)
        if source is None:
            return None
        record = pinned(source)
    path = Path(record["path"])
    if file_sha(path) != record["sha256"]:
        raise ResumeError("A context inventory file changed")
    value = read(path)
    rows = value.get("per_case", [])
    if (value.get("case_count") != count or value.get("output_budget") != 4096
            or value.get("all_prompts_fit") is not True or len(rows) != count
            or len({v["case_id"] for v in rows}) != count
            or any(type(v.get("prompt_tokens")) is not int or v["prompt_tokens"] < 1 for v in rows)):
        raise ResumeError("A context report lacks complete per-case token counts")
    return {"path": str(path.resolve()), "sha256": record["sha256"]}


def assemble(root, pool_dir, registry, *, contexts=None, negative_receipts=None, run_ids=None, endpoints_file=None):
    root, pool_dir = Path(root).resolve(), Path(pool_dir).resolve()
    registry_path = Path(registry).resolve()
    registry_value = read(registry_path)
    if registry_value.get("sealed") is not True:
        raise ResumeError("Original run registry is not sealed")
    index = context_index(contexts)
    selected, skipped, sources, per_case_contexts = [], [], [], {}
    receipts = list(negative_receipts or [])
    if not receipts:
        receipts = sorted((root / ".local/shared_vllm_migration_2026-10-17/drains").glob("*.json"))
    receipt_values = [(path, read(path)) for path in receipts]
    proven_run_ids = {record["run_id"] for _, receipt in receipt_values if receipt.get("stage") == "drained_and_job_terminal"
                      for record in receipt.get("request_records", [])}
    continuation_directories, continuation_snapshots = {}, {}
    missing_context = []
    requested = set(run_ids) if run_ids else None
    for source in registry_value["pool_plans"]:
        path = Path(source["path"])
        if file_sha(path) != source["sha256"]:
            raise ResumeError("An original pool plan changed")
        value = read(path)
        if value.get("execution_authorized") is not True:
            raise ResumeError("Original source plan is not execution authorized")
        sources.append(dict(source))
        for worker in value["workers"]:
            for entry in worker["entries"]:
                if requested is not None and entry["run_id"] not in requested:
                    continue
                project = Path(entry["project_root"])
                cfg_path = project / entry["config_path"]
                if not project.resolve().is_relative_to(root) or file_sha(cfg_path) != entry["config_sha256"]:
                    raise ResumeError("Frozen config path/hash changed")
                cfg = read(cfg_path)
                original_run = project / "results/runs" / entry["run_id"]
                if (original_run / "completion.json").exists():
                    completion = read(original_run / "completion.json")
                    partial = (entry["run_id"] in proven_run_ids and completion.get("generation_exit_code") not in (None, 0)
                               and completion.get("scoring_exit_code") == 0 and (original_run / "scoring_output_lock.json").is_file())
                    if not partial:
                        skipped.append(entry["run_id"])
                        continue
                    files = {}
                    for file in sorted(original_run.rglob("*")):
                        if file.is_symlink():
                            raise ResumeError("A partially scored source contains a symbolic link")
                        if file.is_file():
                            files[file.relative_to(original_run).as_posix()] = file_sha(file)
                    continuation_directories[entry["run_id"]] = str(original_run.with_name(original_run.name + "_shared_continuation_v1"))
                    continuation_snapshots[entry["run_id"]] = {"source_run_directory": str(original_run), "files_sha256": files}
                if cfg["model"] != MODEL or cfg["model_revision"] != REVISION or cfg["generation"]["max_tokens"] != 4096:
                    raise ResumeError("An unfinished source changes the frozen scientific recipe")
                selected.append({"run_id": entry["run_id"], "task_id": entry["task_id"], "planned": entry["case_count"]})
                context = checked_context(root, project, cfg, entry["case_count"], index)
                if context is None:
                    missing_context.append(entry["run_id"])
                else:
                    per_case_contexts[entry["run_id"]] = context
    if requested is not None and requested != {e["run_id"] for e in selected} | set(skipped):
        raise ResumeError("Requested runs are not in the original sealed registry")
    lengths, evidence, missing_bench = measured_limits(pool_dir)
    excluded_evidence = excluded_capacity_evidence(pool_dir)
    covered_length = max((p["max_prompt_tokens"] for p in lengths), default=0)
    uncovered = [{"run_id": rid, "max_prompt_tokens": read(record["path"])["max_prompt_tokens"],
                  "max_measured_prompt_tokens": covered_length}
                 for rid, record in per_case_contexts.items()
                 if read(record["path"])["max_prompt_tokens"] > covered_length]
    endpoint_path = Path(endpoints_file) if endpoints_file else pool_dir / "endpoints.json"
    missing_endpoints = not endpoint_path.is_file()
    endpoints = []
    if not missing_endpoints:
        value = read(endpoint_path)
        raw_endpoints = value.get("endpoints", []) if isinstance(value, dict) else value
        if not raw_endpoints:
            raise ResumeError("Pool endpoint registry is empty")
        for original in raw_endpoints:
            identity = read(original["server_identity_file"])
            entry = {**original, "max_inflight": identity["max_num_seqs"], "max_model_len": identity["max_model_len"],
                     "tensor_parallel_size": identity["tensor_parallel_size"], "length_limits": lengths}
            if lengths:
                validate_endpoint(entry, live=False)
            endpoints.append(entry)
    pinned_receipts, pending_receipts = [], []
    selected_ids = {e["run_id"] for e in selected}
    for path, value in receipt_values:
        if not any(r.get("run_id") in selected_ids for r in value.get("request_records", [])):
            continue
        if value.get("stage") != "drained_and_job_terminal":
            pending_receipts.append(str(path))
        else:
            pinned_receipts.append(pinned(path))
    amendment = {"schema_version": 1, "kind": "shared_vllm_infrastructure_amendment", "execution_authorized": True,
                 "infrastructure_only": True, "scientific_protocol_changes": [], "created_at_utc": stamp(),
                 "model": MODEL, "model_revision": REVISION, "project_gpu_ceiling": 8,
                 "adapter_files_sha256": {str(p.resolve()): file_sha(p) for p in [Path(__file__).with_name("shared_vllm_resume.py"), Path(__file__).with_name("run_shared_vllm_evaluations.py"), Path(__file__)]},
                 "source_registry": pinned(registry_path), "source_plans": sources,
                 "run_ids": [e["run_id"] for e in selected], "run_context_checks": per_case_contexts,
                 "continuation_run_directories": continuation_directories,
                 "continuation_source_snapshots": continuation_snapshots,
                 "endpoints": endpoints, "capacity_evidence_files": evidence,
                 "excluded_capacity_evidence": excluded_evidence,
                 "negative_execution_receipts": pinned_receipts,
                 "policy": "Infrastructure-only routing and measured length-aware admission; original model, BF16, complete prompt/sequence, thinking, 4096-output budget, sampling, one attempt and native scorers unchanged. Existing responses and unknown calls are never retried. Only exact request slots proven unexecuted by a pinned terminal API-kill drain receipt may be dispatched using their existing request bytes."}
    negative = negative_execution_records(amendment)
    ready = not (missing_context or missing_bench or missing_endpoints or pending_receipts or uncovered)
    report = {"ready": ready, "selected_generation_runs": len(selected), "planned_cases_in_selected_runs": sum(e["planned"] for e in selected),
              "terminal_runs_skipped": len(skipped), "per_case_context_reports": len(per_case_contexts),
              "missing_context_run_ids": missing_context, "missing_pool_endpoints": missing_endpoints,
              "missing_capacity_evidence": missing_bench, "pending_negative_receipts": pending_receipts,
              "excluded_capacity_directories": [v["relative_directory"] for v in excluded_evidence],
              "uncovered_prompt_run_ids": uncovered,
              "proven_unexecuted_request_slots": len(negative), "length_limits": lengths,
              "derived_continuation_directories": continuation_directories,
              "task_ids": sorted({e["task_id"] for e in selected}), "pool_directory": str(pool_dir)}
    return amendment, report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--pool-dir", type=Path, required=True)
    parser.add_argument("--registry", type=Path)
    parser.add_argument("--context-index", type=Path)
    parser.add_argument("--negative-receipt", action="append", type=Path)
    parser.add_argument("--run-id", action="append")
    parser.add_argument("--endpoints", type=Path)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--check-only", action="store_true")
    args = parser.parse_args()
    registry = args.registry or args.root / ".local/remaining_evaluations/supervisor_plan.json"
    contexts = args.context_index
    if contexts is None:
        default = args.root / ".local/shared_vllm_migration_2026-10-17/scoring/context_index.json"
        contexts = default if default.is_file() else None
    amendment, report = assemble(args.root, args.pool_dir, registry, contexts=contexts,
                                 negative_receipts=args.negative_receipt, run_ids=args.run_id, endpoints_file=args.endpoints)
    if not args.check_only and report["ready"]:
        if args.output is None:
            parser.error("--output is required when writing a ready amendment")
        atomic_write(args.output, amendment, exclusive=True)
        report.update(amendment=str(args.output.resolve()), amendment_sha256=file_sha(args.output))
    print(json.dumps(report, indent=2), flush=True)
    return 0 if report["ready"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
