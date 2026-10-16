#!/usr/bin/env python3
"""Create a NEW gated seven-replica routing plan for wholly unstarted shards.

Original inputs, reviews, plan, configurations and code remain untouched.
No providers, inference, queue edits, process control or label parsing occurs.
"""
import argparse
import copy
import datetime as dt
import json
from pathlib import Path

from prepare_local_extended_shards import (digest, file_digest, ordered_union,
    recipe, shard_metadata, SHARD_SIZE, TASK_ORDER, SCORER, write_new)

ROOT = Path(__file__).resolve().parents[1]
RUNNER = "scripts/run_local_labbench_eight_gpu.py"
RUNNER_SHA256 = "de0c69b2eea33d618a7674791d6ae448fd8c086a7ba081e948dafdfdcaed4493"
REPLICAS = ((1, 8031), (2, 8032), (3, 8033), (4, 8029), (5, 8026), (6, 8027), (7, 8028))
OLD_PLAN = "reports/local_extended_shard_plan.json"
PLAN = "reports/local_extended_seven_gpu_plan.json"
APPROVAL = "configs/local_extended_seven_gpu_execution_approval.json"
AUDIT = "reports/local_extended_seven_gpu_unstarted_audit.json"
EXECUTOR = "scripts/execute_local_extended_seven_gpu.py"
AGGREGATOR = "scripts/aggregate_local_extended_seven_gpu.py"
PREPARER = "scripts/prepare_local_extended_seven_gpu.py"
ROUTING_FIELDS = {"run_id", "gpu_ids", "endpoint", "serving_config_file", "server_record_file",
                  "runner", "executor", "frozen_files_sha256", "frozen_at_utc", "assignment_index",
                  "aggregate_config_file", "shard_configs", "routing_plan_file", "execution_approval_file",
                  "supersedes_unstarted_run_id", "supersedes_config_file", "supersedes_config_sha256"}


def unstarted_audit(root, old_plan, expected_shards=43):
    shards = [item for task in old_plan["tasks"] for item in task["shards"]]
    if len(shards) != expected_shards:
        raise ValueError("Unexpected original shard count")
    rows = []
    for task in old_plan["tasks"]:
        for run_id, kind in [(task["aggregate_run_id"], "aggregate")] + [(item["run_id"], "shard") for item in task["shards"]]:
            folder = root / "results/runs" / run_id
            rows.append({"task_id": task["task_id"], "run_id": run_id, "kind": kind,
                         "run_folder_exists": folder.exists(), "manifest_exists": (folder / "run_manifest.json").exists(),
                         "request_file_count": len(list((folder / "requests").glob("*"))),
                         "response_file_count": len(list((folder / "responses").glob("*"))),
                         "scores_exist": (folder / "scores.json").exists(), "completion_exists": (folder / "completion.json").exists()})
    started = [row["run_id"] for row in rows if row["run_folder_exists"]]
    if started:
        raise ValueError("Original run started or reserved; never migrate: " + ", ".join(started))
    return {"checked_at_utc": dt.datetime.now(dt.timezone.utc).isoformat(), "original_shard_count": len(shards),
            "checked_run_count_including_aggregates": len(rows), "all_original_runs_unstarted": True, "runs": rows}


def require_approval(root=ROOT, plan_name=PLAN, config_name=None):
    plan_path = root / plan_name
    plan = json.loads(plan_path.read_text())
    if plan.get("execution_approval_file") != APPROVAL:
        raise ValueError("Unexpected plan approval location")
    approval = json.loads((root / APPROVAL).read_text())
    expected = {task["aggregate_config_file"]: task["aggregate_config_sha256"] for task in plan["tasks"]}
    expected.update({item["config_file"]: item["config_sha256"] for task in plan["tasks"] for item in task["shards"]})
    if (approval.get("approved") is not True or approval.get("plan_file") != plan_name
            or approval.get("plan_sha256") != file_digest(plan_path)
            or approval.get("approved_config_sha256") != expected):
        raise ValueError("Seven-GPU plan remains disabled or exact root approval differs")
    if config_name is not None and (config_name not in expected or file_digest(root / config_name) != expected[config_name]):
        raise ValueError("Config is not an exactly approved plan member")
    if file_digest(root / plan["supersedes_unused_plan_file"]) != plan["supersedes_unused_plan_sha256"]:
        raise ValueError("Original unused plan changed")
    old = json.loads((root / plan["supersedes_unused_plan_file"]).read_text())
    unstarted_audit(root, old, sum(task["shard_count"] for task in plan["tasks"]))
    if file_digest(root / RUNNER) != RUNNER_SHA256:
        raise ValueError("Pinned seven-GPU admission runner changed")
    return plan


def cases_checked(root, settings):
    for name, expected in settings["frozen_files_sha256"].items():
        if file_digest(root / name) != expected:
            raise ValueError("Frozen original dependency changed: " + name)
    cases = [json.loads(line) for line in (root / settings["input_file"]).read_text().splitlines() if line]
    review = json.loads((root / settings["review_file"]).read_text())
    if [case["case_id"] for case in cases] != review["approved_case_ids"] or review["held_cases"]:
        raise ValueError("Original exact reviewed IDs changed")
    return cases


def route_config(old, old_name, old_hash, new_run, hashes, timestamp):
    new = copy.deepcopy(old)
    new.update(run_id=new_run, runner=RUNNER, executor=EXECUTOR, frozen_at_utc=timestamp,
               routing_plan_file=PLAN, execution_approval_file=APPROVAL,
               supersedes_unstarted_run_id=old["run_id"], supersedes_config_file=old_name,
               supersedes_config_sha256=old_hash)
    new["frozen_files_sha256"].update(hashes)
    new["frozen_files_sha256"][old_name] = old_hash
    return new


def validate_routing_only(old, new):
    if recipe(old) != recipe(new):
        raise ValueError("Routing must not alter prompt/model/generation/scoring recipe")
    if {key: value for key, value in old.items() if key not in ROUTING_FIELDS} != {key: value for key, value in new.items() if key not in ROUTING_FIELDS}:
        raise ValueError("Unapproved nonrouting configuration change")


def prepare(root=ROOT, expected_shards=43):
    root = Path(root).resolve()
    if any((root / name).exists() for name in (PLAN, APPROVAL, AUDIT)):
        raise ValueError("Preserve existing new routing artifacts")
    if file_digest(root / RUNNER) != RUNNER_SHA256:
        raise ValueError("Final strict runner hash differs")
    old_plan = json.loads((root / OLD_PLAN).read_text())
    if [task["task_id"] for task in old_plan["tasks"]] != list(TASK_ORDER):
        raise ValueError("Original task order changed")
    audit = unstarted_audit(root, old_plan, expected_shards)
    timestamp = audit["checked_at_utc"]
    hashes = {name: file_digest(root / name) for name in (RUNNER, PREPARER, EXECUTOR, AGGREGATOR, OLD_PLAN)}
    preserved = {OLD_PLAN: file_digest(root / OLD_PLAN)}
    tasks, assignment = [], 0
    for entry in old_plan["tasks"]:
        task = entry["task_id"]
        aggregate_name = f"configs/local_extended_seven_gpu_{task.lower()}_aggregate.json"
        old_full_path = root / entry["aggregate_config_file"]
        if file_digest(old_full_path) != entry["aggregate_config_sha256"]:
            raise ValueError("Old aggregate config changed")
        old_full = json.loads(old_full_path.read_text())
        full_cases = cases_checked(root, old_full)
        full = route_config(old_full, entry["aggregate_config_file"], entry["aggregate_config_sha256"], old_full["run_id"] + "_seven_gpu", hashes, timestamp)
        new_entries, groups = [], []
        for item in entry["shards"]:
            old_path = root / item["config_file"]
            if file_digest(old_path) != item["config_sha256"]:
                raise ValueError("Old shard config changed")
            old = json.loads(old_path.read_text())
            cases = cases_checked(root, old)
            groups.append(cases)
            index = old["shard_index"]
            gpu, port = REPLICAS[assignment % len(REPLICAS)]
            shard_name = f"configs/local_extended_seven_gpu_{task.lower()}_shard_{index:03d}.json"
            shard = route_config(old, item["config_file"], item["config_sha256"], full["run_id"] + f"_shard_{index:03d}", hashes, timestamp)
            shard.update(aggregate_config_file=aggregate_name, assignment_index=assignment,
                         gpu_ids=[gpu], endpoint=f"http://127.0.0.1:{port}/v1",
                         serving_config_file=f"configs/local_model_gpu{gpu}.json" if gpu != 5 else "configs/local_model.json",
                         server_record_file=f".local/local_model_server_gpu{gpu}.json" if gpu != 5 else ".local/local_model_server.json")
            validate_routing_only(old, shard)
            write_new(root / shard_name, shard)
            new_entries.append({"config_file": shard_name, "config_sha256": file_digest(root / shard_name), "run_id": shard["run_id"],
                                "shard_index": index, "cases": len(cases), "gpu_ids": [gpu], "endpoint": shard["endpoint"]})
            assignment += 1
            preserved[item["config_file"]] = item["config_sha256"]
            preserved.update(old["frozen_files_sha256"])
        validation = ordered_union(full_cases, groups)
        if validation != old_full["full_test_id_union_validation"] or len(full_cases) != entry["full_test_case_count"]:
            raise ValueError("Original full ordered union/count changed")
        full["shard_configs"] = new_entries
        validate_routing_only(old_full, full)
        write_new(root / aggregate_name, full)
        tasks.append({"task_id": task, "aggregate_config_file": aggregate_name, "aggregate_config_sha256": file_digest(root / aggregate_name),
                      "aggregate_run_id": full["run_id"], "full_test_case_count": len(full_cases), "shard_count": len(new_entries), "shards": new_entries})
        preserved[entry["aggregate_config_file"]] = entry["aggregate_config_sha256"]
        preserved.update(old_full["frozen_files_sha256"])
    # Recheck start/byte identity after preparation and before freezing the new
    # plan. Root must repeat this check before replacing unused queue jobs.
    unstarted_audit(root, old_plan, expected_shards)
    if any(file_digest(root / name) != expected for name, expected in preserved.items()):
        raise ValueError("Original frozen artifact changed during routing preparation")
    audit.update(original_plan_file=OLD_PLAN, original_plan_sha256=file_digest(root / OLD_PLAN),
                 preserved_original_artifacts_sha256=preserved, no_started_run_migration=True)
    write_new(root / AUDIT, audit)
    plan = {**old_plan, "frozen_at_utc": timestamp, "tasks": tasks,
            "replica_order": [{"gpu_ids": [gpu], "port": port} for gpu, port in REPLICAS],
            "assignment_policy": "Roundrobin across P03/P07/P08 source-order shards on physical GPUs1-7; GPU0 excluded.",
            "runner": RUNNER, "runner_sha256": RUNNER_SHA256, "executor": EXECUTOR, "aggregator": AGGREGATOR,
            "execution_approval_file": APPROVAL, "supersedes_unused_plan_file": OLD_PLAN,
            "supersedes_unused_plan_sha256": file_digest(root / OLD_PLAN), "unstarted_audit_file": AUDIT,
            "unstarted_audit_sha256": file_digest(root / AUDIT), "inference_dispatched": False,
            "authorizations_or_queues_modified": False,
            "configuration_change_policy": "Routing IDs/allocation/serving/runner/executor and dependency/approval provenance only; original case files/messages/model/recipe/variant/scorer unchanged."}
    write_new(root / PLAN, plan)
    approved_hashes = {task["aggregate_config_file"]: task["aggregate_config_sha256"] for task in tasks}
    approved_hashes.update({item["config_file"]: item["config_sha256"] for task in tasks for item in task["shards"]})
    write_new(root / APPROVAL, {"approved": False, "plan_file": PLAN, "plan_sha256": file_digest(root / PLAN),
                              "approved_config_sha256": approved_hashes, "root_activation_required": True,
                              "policy": "Only root may approve the exact new unused plan after atomic queue replacement; no migration of any started original run, no generation recipe changes or retries."})
    return {"plan": PLAN, "plan_sha256": file_digest(root / PLAN), "approval_file": APPROVAL, "approved": False,
            "old_shards_unstarted": expected_shards, "new_shards": assignment, "tasks": [{"task_id": task["task_id"], "cases": task["full_test_case_count"], "shards": task["shard_count"]} for task in tasks]}


if __name__ == "__main__":
    argparse.ArgumentParser(description=__doc__).parse_args()
    print(json.dumps(prepare()))
