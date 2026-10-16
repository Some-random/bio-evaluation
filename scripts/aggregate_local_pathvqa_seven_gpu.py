"""Score one audited full PathVQA shard union with the unchanged native scorer.

No inference, no shard scoring, and no metric averages. Actual failed/missing
slots retain the original scorer's planned native group denominators.
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

from prepare_local_pathvqa_seven_gpu import (ROOT, PLAN, ORIGINAL_CONFIG, RUNNER,
    RUNNER_SHA256, SCORER, EXECUTOR, REPLICAS, SHARD_SIZE, cases_for, digest,
    file_digest, ordered_union, raw_audit, require_approval)
from run_local_labbench_eight_gpu import write_json


class Pending(Exception):
    pass


def load_checked(name, expected):
    path = ROOT / name
    if file_digest(path) != expected:
        raise ValueError("Frozen artifact changed: " + name)
    return json.loads(path.read_text())


def validate(plan):
    if require_approval(ROOT, plan["aggregate_config_file"]) != plan:
        raise ValueError("Plan differs from exact root-approved routing")
    full = load_checked(plan["aggregate_config_file"], plan["aggregate_config_sha256"])
    original = load_checked(ORIGINAL_CONFIG, plan["original_config_sha256"])
    if (full.get("aggregate_only") is not True or full.get("generator_execution_allowed") is not False
            or full.get("endpoint") != "aggregate-only://offline" or any(key in full for key in ["gpu_ids", "server_record_file", "serving_config_file"])
            or full["shard_configs"] != plan["shards"] or full["shard_count"] != len(plan["shards"])):
        raise ValueError("Aggregate must be offline and cannot impersonate a single source server")
    retained = ["model", "model_revision", "checkpoint_precision", "generation", "concurrency", "variant",
                "approved_task_ids", "input_file", "review_file", "scorer_reference_file", "scorer_reference_sha256",
                "model_facing_fields", "metric_policy", "source_dataset_revision", "source_code_revision", "paper_comparison"]
    if any(full[key] != original[key] for key in retained):
        raise ValueError("Original full input/model/recipe/source/native metric contract changed")
    full_cases = cases_for(ROOT, full)
    if len(full_cases) != full["full_test_case_count"] or len(full_cases) != plan["full_test_case_count"]:
        raise ValueError("Full source-order test count changed")
    pending = []
    for item in plan["shards"]:
        path = ROOT / "results/runs" / item["run_id"] / "completion.json"
        if not path.exists():
            pending.append(item["run_id"])
        elif json.loads(path.read_text()).get("generation_audit_exit_code") != 0:
            raise ValueError("Terminal shard has unauditable execution provenance: " + item["run_id"])
    if pending:
        raise Pending(str(len(pending)) + " shards awaiting terminal generation audit")
    groups, sources = [], []
    for index, item in enumerate(plan["shards"]):
        shard = load_checked(item["config_file"], item["config_sha256"])
        gpu, port = REPLICAS[index % len(REPLICAS)]
        start, stop = index * SHARD_SIZE, min((index + 1) * SHARD_SIZE, len(full_cases))
        recipe_keys = [key for key in retained if key not in ["input_file", "review_file"]]
        if (any(shard[key] != original[key] for key in recipe_keys)
                or shard["shard_index"] != index or item["shard_index"] != index
                or shard["shard_count"] != len(plan["shards"]) or shard["shard_size"] != SHARD_SIZE
                or shard["full_test_case_count"] != len(full_cases) or shard["aggregate_only"] is not False
                or shard["generator_execution_allowed"] is not True or shard["case_scope"] != "task_shard_only"
                or shard["aggregate_config_file"] != plan["aggregate_config_file"]
                or shard["full_input_file"] != original["input_file"] or shard["full_review_file"] != original["review_file"]
                or shard["source_start_index"] != start or shard["source_stop_index"] != stop
                or shard["gpu_ids"] != [gpu] or shard["endpoint"] != f"http://127.0.0.1:{port}/v1"
                or shard["runner"] != RUNNER or shard["executor"] != EXECUTOR):
            raise ValueError("Shard differs from original recipe, fixed ordered range or routing")
        cases = cases_for(ROOT, shard)
        if cases != full_cases[start:stop] or len(cases) != item["cases"]:
            raise ValueError("Shard changes exact original questions/image bytes/order")
        folder = ROOT / "results/runs" / shard["run_id"]
        completion = json.loads((folder / "completion.json").read_text())
        if (completion.get("configuration_sha256") != item["config_sha256"]
                or completion.get("run_manifest_sha256") != file_digest(folder / "run_manifest.json")
                or completion.get("generation_output_lock_sha256") != file_digest(folder / "generation_output_lock.json")
                or completion.get("runner_sha256") != RUNNER_SHA256
                or completion.get("executor_sha256") != file_digest(ROOT / EXECUTOR)
                or completion.get("scoring_exit_code") is not None or completion.get("shard_scoring_performed") is not False
                or completion.get("case_scope") != "task_shard_only" or completion.get("planned") != len(cases)
                or completion.get("shard_index") != index or completion.get("shard_count") != len(plan["shards"])
                or type(completion.get("generation_exit_code")) is not int):
            raise ValueError("Shard terminal record/config/raw audit hashes differ")
        if (folder / "scores.json").exists():
            raise ValueError("Unexpected shard scores; this protocol scores only the full union")
        lock = raw_audit(ROOT, folder, cases, shard, item["config_sha256"])
        completed_count = lock["statuses"].get("completed", 0)
        if completion["generation_exit_code"] == 0 and completed_count != len(cases):
            raise ValueError("Actual generation exit code contradicts archived terminal statuses")
        groups.append(cases)
        sources.append({**item, "run_manifest_sha256": file_digest(folder / "run_manifest.json"),
                        "completion_sha256": file_digest(folder / "completion.json"),
                        "generation_exit_code": completion["generation_exit_code"],
                        "generation_output_lock_sha256": file_digest(folder / "generation_output_lock.json"),
                        "raw_files_sha256": {name: value for name, value in lock["files_sha256"].items() if name != "run_manifest.json"},
                        "statuses": lock["statuses"], "server": lock["server"], "serving_configuration": lock["serving_configuration"]})
    union = ordered_union(full_cases, groups)
    if union != full["full_test_id_union_validation"] or union != plan["full_test_id_union_validation"]:
        raise ValueError("Precommitted full ordered union validation changed")
    return full, full_cases, sources, union


def install_raw(source, target, expected):
    if expected is None:
        if source.exists() or target.exists():
            raise ValueError("An absent source slot appeared after terminal lock")
        return
    if file_digest(source) != expected:
        raise ValueError("Source generation changed after raw lock")
    target.parent.mkdir(parents=True, exist_ok=True)
    if target.exists():
        if file_digest(target) != expected:
            raise ValueError("Existing aggregate output differs; never replace predictions")
        return
    try:
        os.link(source, target)
    except OSError:
        shutil.copyfile(source, target)
    if file_digest(target) != expected:
        raise ValueError("Aggregate raw copy hash differs")


def aggregate(plan, plan_sha256):
    if file_digest(ROOT / PLAN) != plan_sha256:
        raise ValueError("Aggregate plan hash differs from exact on-disk plan")
    full, cases, sources, union = validate(plan)
    folder = ROOT / "results/runs" / full["run_id"]
    folder.mkdir(parents=True, exist_ok=True)
    provenance = {"plan_sha256": plan_sha256, "aggregate_config_sha256": plan["aggregate_config_sha256"],
                  "full_test_id_union_validation": union, "sources": sources,
                  "policy": "All original ordered questions/images and terminal actual source generations, including locked absent/failed slots; no selection, retry, answer repair or shard scoring."}
    manifest = {"configuration": full, "configuration_sha256": plan["aggregate_config_sha256"],
                "runner_sha256": RUNNER_SHA256, "aggregate_builder_sha256": file_digest(Path(__file__)),
                "case_contract_sha256": digest(cases), "planned_cases": len(cases),
                "model_selection_on_test": False, "solver_tools": [], "answer_keys_available_to_solver": False,
                "aggregate_only": True, "source_shard_provenance_sha256": digest(provenance)}
    for name, value in [("run_manifest.json", manifest), ("source_shard_manifest.json", provenance)]:
        path = folder / name
        if path.exists() and json.loads(path.read_text()) != value:
            raise ValueError("Existing aggregate provenance changed")
        if not path.exists():
            write_json(path, value)
    expected_hashes = {}
    for source in sources:
        source_folder = ROOT / "results/runs" / source["run_id"]
        for name, expected in source["raw_files_sha256"].items():
            if name in expected_hashes:
                raise ValueError("Duplicate aggregate raw slot")
            expected_hashes[name] = expected
            install_raw(source_folder / name, folder / name, expected)
    for category in ["requests", "responses"]:
        expected = {name.split("/", 1)[1] for name, value in expected_hashes.items() if name.startswith(category + "/") and value is not None}
        if {path.name for path in (folder / category).glob("*.json")} != expected:
            raise ValueError("Extra/missing combined raw slot")
    parallel = {"mode": "independent TP1 replicas of one pinned checkpoint; offline full-union scoring",
                "gpu_ids": sorted({gpu for source in sources for gpu in source["gpu_ids"]}),
                "replica_count": len({tuple(source["gpu_ids"]) for source in sources}), "shard_count": len(sources),
                "per_replica_concurrency": full["concurrency"],
                "servers": [{key: source[key] for key in ["run_id", "gpu_ids", "endpoint", "server", "generation_exit_code"]} for source in sources]}
    completion_path = folder / "completion.json"
    if completion_path.exists():
        done = json.loads(completion_path.read_text())
        if (done.get("scoring_exit_code") != 0 or done.get("source_shard_provenance_sha256") != digest(provenance)
                or done.get("scores_sha256") != file_digest(folder / "scores.json")):
            raise ValueError("Terminal aggregate failed or changed; no rescoring")
        return done
    # Precommit the single invocation. An interrupted scorer remains blocked,
    # rather than silently running a second scorer attempt after restart.
    if (folder / "scores.json").exists() or (folder / "scoring_output_lock.json").exists():
        raise ValueError("Prior full scoring artifacts lack terminal completion; no rescoring")
    attempt_path = folder / "native_scoring_attempt.json"
    with attempt_path.open("x") as stream:
        json.dump({"scorer_sha256": file_digest(ROOT / SCORER), "source_shard_provenance_sha256": digest(provenance),
                   "configuration_sha256": plan["aggregate_config_sha256"], "started_at_utc": dt.datetime.now(dt.timezone.utc).isoformat()}, stream)
        stream.write("\n")
    scoring_code, error = None, None
    try:
        scoring = subprocess.run([sys.executable, "-u", str(ROOT / SCORER), "--run", full["run_id"]], cwd=ROOT)
        scoring_code = scoring.returncode
        if scoring_code == 0:
            summary = json.loads((folder / "scores.json").read_text())
            if (summary["planned"] != len(cases) or summary["completed"] != sum(source["statuses"].get("completed", 0) for source in sources)
                    or set(summary["metrics"]) != {"open_token_recall", "closed_accuracy_corrected"}):
                raise ValueError("Original full scorer count/metric contract changed")
            summary.update(primary_metric_names=["open_token_recall", "closed_accuracy_corrected"],
                           full_planned_primary_metrics_valid=all(isinstance(value, (int, float)) for value in summary["metrics"].values()),
                           shard_count=len(sources), aggregated_from_shards=True, full_test_id_union_validation=union,
                           parallel_gpu_metadata=parallel, source_shard_provenance_sha256=digest(provenance),
                           source_generation_exit_codes={source["run_id"]: source["generation_exit_code"] for source in sources},
                           aggregation_policy="Original full native OPEN/CLOSED scorer invoked once on exact audited full union. Planned native group denominators and corrected/bug-compatible diagnostics unchanged; no shard metric averages.")
            write_json(folder / "scores.json", summary)
    except Exception as exc:
        scoring_code, error = 1, type(exc).__name__ + ": " + str(exc)
    generation_code = 0 if all(source["generation_exit_code"] == 0 for source in sources) else 1
    done = {"generation_exit_code": generation_code, "source_generation_exit_codes": {source["run_id"]: source["generation_exit_code"] for source in sources},
            "scoring_exit_code": scoring_code, "aggregate_only": True, "retry_or_resampling": False,
            "status": "completed" if scoring_code == 0 and generation_code == 0 else "completed_with_generation_failures" if scoring_code == 0 else "scoring_failed",
            "finished_at_utc": dt.datetime.now(dt.timezone.utc).isoformat(), "configuration_sha256": plan["aggregate_config_sha256"],
            "scorer_sha256": file_digest(ROOT / SCORER), "aggregate_builder_sha256": file_digest(Path(__file__)),
            "run_manifest_sha256": file_digest(folder / "run_manifest.json"), "source_shard_provenance_sha256": digest(provenance),
            "native_scoring_attempt_sha256": file_digest(attempt_path), "full_test_id_union_validation": union,
            "parallel_gpu_metadata": parallel, "case_scope": "complete_publisher_mirror_test6719_native_identity_qualified"}
    for name in ["scores.json", "scoring_output_lock.json"]:
        if (folder / name).exists():
            done[name.replace(".json", "_sha256")] = file_digest(folder / name)
    if error:
        done["error"] = error
    write_json(completion_path, done)
    if scoring_code != 0:
        raise ValueError("Single original full native scorer failed; no rescore: " + str(error))
    return done


def watch(plan_path, continuous=False, poll_seconds=30):
    if not 1 <= poll_seconds <= 60:
        raise ValueError("Polling interval must be 1–60 seconds")
    plan_sha256 = file_digest(plan_path)
    plan = json.loads(plan_path.read_text())
    if require_approval(ROOT) != plan:
        raise ValueError("Plan differs from root-approved fixed plan")
    lock_path = ROOT / ".local/local_pathvqa_seven_gpu_aggregation.lock"
    lock_path.parent.mkdir(parents=True, exist_ok=True)
    with lock_path.open("a") as lock:
        fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        while True:
            if file_digest(plan_path) != plan_sha256:
                raise ValueError("Plan changed while watching")
            try:
                result = aggregate(plan, plan_sha256)
                state = {"status": "complete", "run_id": plan["aggregate_run_id"], "completion": result}
            except Pending as exc:
                state = {"status": "pending", "detail": str(exc)}
            except Exception as exc:
                state = {"status": "blocked", "detail": str(exc), "retry_or_resampling": False}
            write_json(ROOT / "reports/local_pathvqa_seven_gpu_aggregation.json", state)
            if not continuous or state["status"] != "pending":
                return 1 if state["status"] == "blocked" else 0
            time.sleep(poll_seconds)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--plan", type=Path, default=ROOT / PLAN)
    parser.add_argument("--watch", action="store_true")
    parser.add_argument("--poll-seconds", type=int, default=30)
    args = parser.parse_args()
    raise SystemExit(watch(args.plan, args.watch, args.poll_seconds))
