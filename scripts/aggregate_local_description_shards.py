"""Validate approved description shards and compute complete gold-only ROUGE.

Never invokes inference. A failed shard blocks its task without retrying it.
"""
import argparse
import datetime as dt
import fcntl
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import time

from prepare_local_extended_shards import (REPLICAS, RUNNER, SHARD_SIZE,
    digest, file_digest, ordered_union, recipe, shard_metadata)
from run_local_labbench_multimodal import request_record, write_json
from prepare_local_description_shards import ROOT, SCORER, PLAN_FILE, approval_for


class Pending(Exception):
    pass


def load_checked(name, expected):
    path = ROOT / name
    if file_digest(path) != expected:
        raise ValueError("Frozen file changed: " + name)
    return json.loads(path.read_text())


def cases_for(settings):
    for name, expected in settings["frozen_files_sha256"].items():
        if file_digest(ROOT / name) != expected:
            raise ValueError("Frozen dependency changed: " + name)
    cases = [json.loads(line) for line in (ROOT / settings["input_file"]).read_text().splitlines() if line]
    review = json.loads((ROOT / settings["review_file"]).read_text())
    if [case["case_id"] for case in cases] != review["approved_case_ids"] or review["held_cases"]:
        raise ValueError("Exact ordered input-only review changed")
    return cases


def validate_recipe(full, shard, base):
    if recipe(full) != recipe(shard):
        raise ValueError("Shard model/revision/generation/prompt recipe mismatch")
    for key in ("model", "model_revision", "checkpoint_precision", "generation", "concurrency"):
        if full[key] != base[key]:
            raise ValueError("Recipe differs from frozen B07 generation: " + key)
    if full["aggregate_only"] is not True or full["endpoint"] != "aggregate-only://offline":
        raise ValueError("Full config must be offline aggregate-only")
    if shard["aggregate_only"] is not False or shard["case_scope"] != "task_shard_only":
        raise ValueError("Executable shard scope missing")
    if shard["approved_task_ids"] != full["approved_task_ids"]:
        raise ValueError("Mixed task shard")


def validate_raw(folder, cases, settings, manifest):
    expected_names = {digest([c["task"], c["variant"], c["case_id"]]) + ".json" for c in cases}
    hashes = {}
    for kind in ("requests", "responses"):
        actual = {path.name for path in (folder / kind).glob("*.json")}
        if actual != expected_names:
            raise ValueError("Missing/extra raw " + kind + " slots")
    for case in cases:
        identity = digest([case["task"], case["variant"], case["case_id"]])
        names = {kind: kind + "/" + identity + ".json" for kind in ("requests", "responses")}
        records = {kind: json.loads((folder / name).read_text()) for kind, name in names.items()}
        if records["requests"] != request_record(case, settings):
            raise ValueError("Raw request differs from exact original prompt/generation/identity")
        response, request = records["responses"], records["requests"]
        for key, value in {**{k: case[k] for k in ("task", "case_id", "variant", "split")},
                           "model": settings["model"], "model_revision": settings["model_revision"],
                           "request_sha256": request["request_sha256"]}.items():
            if response.get(key) != value:
                raise ValueError("Raw response provenance mismatch: " + key)
        raw = response.get("response", {})
        choices = raw.get("choices", [])
        if (response.get("status") != "completed" or response.get("http_status") != 200
                or raw.get("model") != settings["model"] or len(choices) != 1
                or response.get("text") != (choices[0].get("message", {}).get("content") or "")
                or response.get("finish_reason") != choices[0].get("finish_reason")):
            raise ValueError("Incomplete/altered/multiple-completion raw response")
        for name in names.values():
            hashes[name] = file_digest(folder / name)
    lock = json.loads((folder / "scoring_output_lock.json").read_text())
    expected_lock = {"run_manifest.json": file_digest(folder / "run_manifest.json"), **hashes}
    if lock["files_sha256"] != expected_lock or lock["contract_sha256"] != digest(expected_lock):
        raise ValueError("Shard prediction lock does not match raw provenance")
    if manifest["case_contract_sha256"] != digest(cases) or manifest["planned_cases"] != len(cases):
        raise ValueError("Shard manifest input/count mismatch")
    return hashes


def validate_task(entry, plan):
    full = load_checked(entry["aggregate_config_file"], entry["aggregate_config_sha256"])
    if full["shard_configs"] != entry["shards"] or full["full_test_case_count"] != entry["full_test_case_count"]:
        raise ValueError("Plan and aggregate manifest disagree")
    base = load_checked(plan["source_recipe_file"], plan["source_recipe_sha256"])
    full_cases = cases_for(full)
    if len(full_cases) != full["full_test_case_count"]:
        raise ValueError("Full test count mismatch")
    groups, sources = [], []
    pending = []
    # First detect every finished failure, even when an earlier shard is pending.
    for item in entry["shards"]:
        completion_path = ROOT / "results/runs" / item["run_id"] / "completion.json"
        if not completion_path.exists():
            pending.append(item["run_id"])
        else:
            completion = json.loads(completion_path.read_text())
            if completion.get("generation_exit_code") != 0 or completion.get("scoring_exit_code") != 0:
                raise ValueError("Failed shard blocks full aggregate: " + item["run_id"])
    if pending:
        raise Pending(str(len(pending)) + " shards pending")
    for index, item in enumerate(entry["shards"]):
        shard = load_checked(item["config_file"], item["config_sha256"])
        validate_recipe(full, shard, base)
        authorization = approval_for(ROOT / item["config_file"], shard)
        if (item["shard_index"] != index or shard["shard_index"] != index
                or shard["shard_count"] != len(entry["shards"]) or shard["shard_size"] != SHARD_SIZE
                or shard["full_test_case_count"] != len(full_cases)
                or shard["aggregate_config_file"] != entry["aggregate_config_file"]
                or shard["full_input_file"] != full["input_file"]
                or shard["full_input_sha256"] != file_digest(ROOT / full["input_file"])
                or shard["full_review_file"] != full["review_file"]
                or shard["full_review_sha256"] != file_digest(ROOT / full["review_file"])):
            raise ValueError("Shard range/full-test metadata mismatch")
        gpu, port = REPLICAS[shard["assignment_index"] % len(REPLICAS)]
        if shard["gpu_ids"] != [gpu] or shard["endpoint"] != f"http://127.0.0.1:{port}/v1":
            raise ValueError("Replica roundrobin assignment changed")
        start, stop = index * SHARD_SIZE, min((index + 1) * SHARD_SIZE, len(full_cases))
        cases = cases_for(shard)
        if shard["source_start_index"] != start or shard["source_stop_index"] != stop or cases != full_cases[start:stop]:
            raise ValueError("Shard is not its exact frozen source-order slice")
        folder = ROOT / "results/runs" / shard["run_id"]
        completion = json.loads((folder / "completion.json").read_text())
        if (completion.get("configuration_sha256") != item["config_sha256"]
                or completion.get("run_manifest_sha256") != file_digest(folder / "run_manifest.json")
                or completion.get("scores_sha256") != file_digest(folder / "scores.json")
                or completion.get("case_scope") != "task_shard_only"
                or any(completion.get(key) != value for key, value in shard_metadata(shard).items())):
            raise ValueError("Shard completion/config/manifest hash mismatch")
        if completion.get("execution_approval") != authorization:
            raise ValueError("Historical shard execution approval mismatch")
        scores = json.loads((folder / "scores.json").read_text())
        if (scores.get("case_scope") != "task_shard_only" or scores.get("planned") != len(cases)
                or scores.get("completed") != len(cases)):
            raise ValueError("Shard score is incomplete or mislabeled full test")
        manifest = json.loads((folder / "run_manifest.json").read_text())
        if (manifest["configuration"] != shard or manifest["configuration_sha256"] != item["config_sha256"]
                or manifest["runner_sha256"] != shard["frozen_files_sha256"][RUNNER]
                or manifest.get("solver_tools") != [] or manifest.get("answer_keys_available_to_solver") is not False
                or manifest.get("model_selection_on_test") is not False):
            raise ValueError("Shard execution manifest mismatch")
        server, serving = manifest["server"], manifest["serving_configuration"]
        if (server.get("gpu_ids") != [gpu] or server.get("model") != shard["model"]
                or server.get("revision") != shard["model_revision"] or not server.get("pid")
                or not server.get("proc_start_ticks") or serving.get("gpu_ids") != [gpu]
                or serving.get("host") != "127.0.0.1" or serving.get("port") != port
                or serving.get("model") != shard["model"] or serving.get("revision") != shard["model_revision"]):
            raise ValueError("Historical server identity/replica mismatch")
        raw_hashes = validate_raw(folder, cases, shard, manifest)
        groups.append(cases)
        sources.append({**item, "run_manifest_sha256": file_digest(folder / "run_manifest.json"),
                        "completion_sha256": file_digest(folder / "completion.json"),
                        "scoring_output_lock_sha256": file_digest(folder / "scoring_output_lock.json"),
                        "server": server, "serving_configuration": serving, "raw_files_sha256": raw_hashes,
                        "execution_approval": authorization})
    union = ordered_union(full_cases, groups)
    return full, full_cases, sources, union


def install_raw(source, target, expected):
    if file_digest(source) != expected:
        raise ValueError("Source output changed after provenance validation")
    target.parent.mkdir(parents=True, exist_ok=True)
    if target.exists():
        if file_digest(target) != expected:
            raise ValueError("Existing aggregate output differs; refuse replacement")
        return
    try:
        os.link(source, target)
    except OSError:
        shutil.copyfile(source, target)
    if file_digest(target) != expected:
        raise ValueError("Aggregate raw output copy/hash mismatch")


def aggregate(entry, plan, plan_sha256):
    full, cases, sources, union = validate_task(entry, plan)
    folder = ROOT / "results/runs" / full["run_id"]
    folder.mkdir(parents=True, exist_ok=True)
    provenance = {"plan_sha256": plan_sha256, "aggregate_config_sha256": entry["aggregate_config_sha256"],
                  "full_test_id_union_validation": union, "sources": sources,
                  "policy": "Exact full source-order union of unique locked generations; no selection/retries; global scorer invoked once on combined predictions."}
    manifest = {"configuration": full, "configuration_sha256": entry["aggregate_config_sha256"],
                "runner_sha256": full["frozen_files_sha256"][RUNNER],
                "aggregate_builder_sha256": file_digest(Path(__file__)),
                "case_contract_sha256": digest(cases), "planned_cases": len(cases),
                "model_selection_on_test": False, "solver_tools": [], "answer_keys_available_to_solver": False,
                "aggregate_only": True, "source_shard_provenance_sha256": digest(provenance)}
    for name, value in (("run_manifest.json", manifest), ("source_shard_manifest.json", provenance)):
        path = folder / name
        if path.exists() and json.loads(path.read_text()) != value:
            raise ValueError("Existing aggregate provenance changed")
        if not path.exists():
            write_json(path, value)
    for source in sources:
        source_folder = ROOT / "results/runs" / source["run_id"]
        for name, expected in source["raw_files_sha256"].items():
            install_raw(source_folder / name, folder / name, expected)
    expected_names = {digest([case["task"], case["variant"], case["case_id"]]) + ".json" for case in cases}
    for kind in ("requests", "responses"):
        if {path.name for path in (folder / kind).glob("*.json")} != expected_names:
            raise ValueError("Aggregate contains missing/extra raw output")
    parallel = {"mode": "independent TP1 replicas of one pinned checkpoint", "gpu_ids": sorted({gpu for source in sources for gpu in source["gpu_ids"]}),
                "replica_count": len({tuple(source["gpu_ids"]) for source in sources}),
                "shard_count": len(sources), "per_replica_concurrency": full["concurrency"],
                "servers": [{key: source[key] for key in ("run_id", "gpu_ids", "endpoint", "server")} for source in sources]}
    completion_path = folder / "completion.json"
    if completion_path.exists():
        done = json.loads(completion_path.read_text())
        if done.get("scoring_exit_code") != 0 or done.get("source_shard_provenance_sha256") != digest(provenance):
            raise ValueError("Previous aggregate failed or provenance changed; no replacement")
        if (done.get("scores_sha256") != file_digest(folder / "scores.json")
                or done.get("run_manifest_sha256") != file_digest(folder / "run_manifest.json")):
            raise ValueError("Completed aggregate score/manifest hash changed")
        return done
    # Stable native scorer locks every combined raw prediction before it reads labels.
    scoring = subprocess.run([sys.executable, "-u", str(ROOT / SCORER), "--run", full["run_id"]], cwd=ROOT)
    if scoring.returncode == 0:
        path = folder / "scores.json"
        summary = json.loads(path.read_text())
        if summary["planned"] != len(cases) or summary["completed"] != len(cases):
            raise ValueError("Global scorer did not cover complete union")
        summary.update(full_test_id_union_validation=union, parallel_gpu_metadata=parallel,
                       source_shard_provenance_sha256=digest(provenance),
                       aggregation_policy="Native gold-only ROUGE computed once globally from all original test predictions; shard bootstrap metrics never averaged.")
        write_json(path, summary)
    record = {"generation_exit_code": 0, "scoring_exit_code": scoring.returncode,
              "finished_at_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
              "aggregate_only": True, "full_test_id_union_validation": union, "parallel_gpu_metadata": parallel,
              "source_shard_provenance_sha256": digest(provenance),
              "configuration_sha256": entry["aggregate_config_sha256"],
              "run_manifest_sha256": file_digest(folder / "run_manifest.json"),
              "case_scope": "full_frozen_reviewed_BioT5_export_test", "retry_or_resampling": False}
    if (folder / "scores.json").exists():
        record["scores_sha256"] = file_digest(folder / "scores.json")
    write_json(completion_path, record)
    if scoring.returncode:
        raise ValueError("Stable native aggregate scorer failed")
    return record


def watch(plan_path, continuous=False, poll_seconds=30):
    if not 1 <= poll_seconds <= 60:
        raise ValueError("Polling interval must be1-60 seconds")
    plan_sha256 = file_digest(plan_path)
    plan = json.loads(plan_path.read_text())
    report_path = ROOT / "reports/local_description_shard_aggregation.json"
    lock_path = ROOT / ".local/local_description_shard_aggregation.lock"
    lock_path.parent.mkdir(parents=True, exist_ok=True)
    with lock_path.open("a") as lock:
        fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        states = {}
        while True:
            if file_digest(plan_path) != plan_sha256:
                raise ValueError("Frozen plan changed while watching")
            for entry in plan["tasks"]:
                task = entry["task_id"]
                if states.get(task, {}).get("status") in ("complete", "blocked"):
                    continue
                try:
                    aggregate(entry, plan, plan_sha256)
                    states[task] = {"status": "complete", "run_id": entry["aggregate_run_id"]}
                except Pending as exc:
                    states[task] = {"status": "pending", "detail": str(exc)}
                except Exception as exc:
                    states[task] = {"status": "blocked", "detail": str(exc), "retry_or_resampling": False}
            write_json(report_path, {"plan_sha256": plan_sha256, "tasks": states,
                       "updated_at_utc": dt.datetime.now(dt.timezone.utc).isoformat(), "inference_dispatched": False})
            if not continuous or all(value["status"] != "pending" for value in states.values()):
                return 1 if any(value["status"] == "blocked" for value in states.values()) else 0
            time.sleep(poll_seconds)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--plan", type=Path, default=ROOT / PLAN_FILE)
    parser.add_argument("--watch", action="store_true")
    parser.add_argument("--poll-seconds", type=int, default=30)
    args = parser.parse_args()
    raise SystemExit(watch(args.plan, args.watch, args.poll_seconds))
