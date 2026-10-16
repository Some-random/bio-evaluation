"""Offline inventory and integrity audit of the authorized local queues.

Parses configuration/review/process metadata and hashes frozen files as opaque
bytes. Never parses case payloads or credentials, or dispatches inference.
"""
from __future__ import annotations

import hashlib
import json
import os
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read(path):
    return json.loads((ROOT / path).read_text())


def digest(path):
    h = hashlib.sha256()
    with (ROOT / path).open("rb") as stream:
        for block in iter(lambda: stream.read(8 * 1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def write(path, value):
    target = ROOT / path
    temporary = target.with_name(target.name + f".{os.getpid()}.tmp")
    temporary.write_text(json.dumps(value, indent=2) + "\n")
    temporary.replace(target)


def main():
    timestamp = datetime.now(timezone.utc).isoformat()
    rows, manifest_rows, mismatches, queues = [], [], [], []
    hashes, counts, run_ids = {}, Counter(), set()
    for queue_path in sorted((ROOT / "configs").glob("local_benchmark_queue*.json")):
        queue = json.loads(queue_path.read_text())
        queues.append({"path": str(queue_path.relative_to(ROOT)),
                       "accept_more": queue.get("accept_more"),
                       "jobs": len(queue["jobs"])})
        for job in queue["jobs"]:
            cfg = read(job["config"])
            run_id = cfg["run_id"]
            if run_id in run_ids:
                raise ValueError(f"Duplicate queued run: {run_id}")
            run_ids.add(run_id)
            review = read(cfg["review_file"])
            cases = len(review["approved_case_ids"])
            task_ids = cfg["approved_task_ids"]
            if len(task_ids) != 1:
                raise ValueError(f"Ambiguous task scope: {job['config']}")
            task = task_ids[0]
            counts[task] += cases
            tools = cfg.get("tool_access", cfg.get("solver_tools"))
            if tools != []:
                mismatches.append({"config": job["config"], "issue": "nonempty_or_missing_tool_access", "value": tools})
            for path, expected in cfg["frozen_files_sha256"].items():
                if path not in hashes:
                    hashes[path] = digest(path)
                if hashes[path] != expected:
                    mismatches.append({"config": job["config"], "path": path,
                                       "expected": expected, "actual": hashes[path]})
            run_dir = ROOT / "results/runs" / run_id
            manifest_path = run_dir / "run_manifest.json"
            completion_path = run_dir / "completion.json"
            manifest = json.loads(manifest_path.read_text()) if manifest_path.exists() else None
            completion = json.loads(completion_path.read_text()) if completion_path.exists() else None
            if manifest:
                summary = {key: manifest.get(key) for key in
                           ("solver_tools", "answer_keys_available_to_solver", "model_selection_on_test")}
                manifest_rows.append({"run_id": run_id, **summary})
                if summary != {"solver_tools": [], "answer_keys_available_to_solver": False,
                               "model_selection_on_test": False}:
                    mismatches.append({"run_id": run_id, "issue": "manifest_access_declaration", "value": summary})
                if manifest.get("configuration_sha256") != digest(job["config"]):
                    mismatches.append({"run_id": run_id, "issue": "manifest_configuration_hash"})
            rows.append({"task_id": task, "run_id": run_id, "config": job["config"],
                         "configuration_sha256": digest(job["config"]),
                         "gpu_ids": cfg["gpu_ids"], "planned_cases": cases,
                         "manifest_present": bool(manifest), "terminal": bool(completion),
                         "terminal_status": completion.get("status") if completion else None,
                         "frozen_dependency_count": len(cfg["frozen_files_sha256"]),
                         "solver_tools": tools})
    inventory = {
        "scope": "Current fixed local Qwen baseline only; excludes earlier OpenAI incident traffic and unrelated projects.",
        "recorded_at_utc": timestamp, "queued_job_count": len(rows),
        "queued_case_count": sum(counts.values()), "task_count": len(counts),
        "task_case_counts": dict(sorted(counts.items())), "queues": queues,
        "cases_partitioned_by_frozen_source_order": True,
        "case_selection_based_on_model_outputs": False,
        "inference_rerouted_from_policy_rejections": False,
        "user_openai_evaluation_api_calls": 0, "checkpoints_duplicated": False,
        "all_64_settings_complete": False,
        "counting_note": "Queue totals include finished jobs and disjoint shards, exclude earlier B01; units vary by task and must not be pooled as one accuracy.",
        "runs": rows,
    }
    authorization = read("configs/execution_authorization.json")
    leakage = {
        "scope": "Current fixed local Qwen baseline only; excludes earlier OpenAI incident traffic and unrelated projects.",
        "audited_at_utc": timestamp, "queued_runs": len(rows),
        "queued_cases": sum(counts.values()), "queued_task_ids": sorted(counts),
        "unique_frozen_files_checked": len(hashes), "frozen_file_mismatches": mismatches,
        "audit_method": "Actual SHA256 of every unique frozen dependency, read as opaque bytes; only configuration/review/manifest JSON is parsed. No manual validation of every sequence/image or runtime information-flow proof.",
        "solver_access": "Frozen messages and generation parameters only; tools disabled, no reference/repository access or test-selected training.",
        "native_reference_input_independence": "Not guaranteed: P29 native predicted-GO context contributes to scoring targets. This dependence is retained and disclosed, with a separate curated-only diagnostic and fixed context-only offline audit.",
        "direct_reference_files_in_payload": False,
        "pretraining_contamination": "UNKNOWN. Public tests and temporal/species splits do not prove absence from Qwen pretraining.",
        "review_scope": "Task goals/native-input contracts, not manual biological validation of every sequence or image.",
        "selection_policy": "Approved source order/full permitted sets and preinference holds; no outcome-based deletion, tuning, score selection or failed-call resampling.",
        "prohibited_or_unreviewed_holds_not_rerouted": ["P18 prior bio_policy calls", "B06 interrupted operational-protocol review", "P30-P32 interrupted mixed mutation source review"],
        "user_openai_api_evaluation_inference_authorized": authorization.get("inference_authorized"),
        "user_openai_evaluation_api_calls": 0, "manifests": manifest_rows,
        "runs": rows,
    }
    write("reports/local_execution_queue_inventory.json", inventory)
    write("reports/local_suite_leakage_controls.json", leakage)
    print(json.dumps({"jobs": len(rows), "slots": sum(counts.values()), "tasks": len(counts),
                      "unique_frozen_dependencies": len(hashes), "mismatches": mismatches}))
    return int(bool(mismatches))


if __name__ == "__main__":
    raise SystemExit(main())
