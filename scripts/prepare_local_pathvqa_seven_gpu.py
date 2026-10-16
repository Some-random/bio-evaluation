#!/usr/bin/env python3
"""Freeze NEW disabled routing for an unstarted full PathVQA mirror run.

Case/image/question bytes, model recipe, source proof and native scorer stay
unchanged. This module never opens scorer references or calls a model.
"""
import argparse
from collections import Counter
import copy
import datetime as dt
import hashlib
import json
from pathlib import Path

import run_local_labbench_multimodal as original_runner
import run_local_labbench_eight_gpu as runner

ROOT = Path(__file__).resolve().parents[1]
ORIGINAL_CONFIG = "configs/local_pathvqa.json"
PLAN = "reports/local_pathvqa_seven_gpu_plan.json"
APPROVAL = "configs/local_pathvqa_seven_gpu_execution_approval.json"
AUDIT = "reports/local_pathvqa_seven_gpu_unstarted_audit.json"
FULL_CONFIG = "configs/local_pathvqa_seven_gpu_aggregate.json"
RUNNER = "scripts/run_local_labbench_eight_gpu.py"
RUNNER_SHA256 = "de0c69b2eea33d618a7674791d6ae448fd8c086a7ba081e948dafdfdcaed4493"
SCORER = "scripts/score_local_pathvqa.py"
PREPARER = "scripts/prepare_local_pathvqa_seven_gpu.py"
EXECUTOR = "scripts/execute_local_pathvqa_seven_gpu.py"
AGGREGATOR = "scripts/aggregate_local_pathvqa_seven_gpu.py"
REPLICAS = ((1, 8031), (2, 8032), (3, 8033), (4, 8029), (5, 8026), (6, 8027), (7, 8028))
SHARD_SIZE = 1024


def digest(value):
    return hashlib.sha256(json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def file_digest(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as stream:
        while data := stream.read(8 * 1024 * 1024):
            h.update(data)
    return h.hexdigest()


def write_new(path, value, jsonl=False):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("x") as stream:
        if jsonl:
            for row in value:
                stream.write(json.dumps(row, ensure_ascii=False) + "\n")
        else:
            json.dump(value, stream, ensure_ascii=False, indent=2)
            stream.write("\n")
    path.chmod(0o600)


def cases_for(root, settings):
    for name, expected in settings["frozen_files_sha256"].items():
        if file_digest(root / name) != expected:
            raise ValueError("Frozen dependency changed: " + name)
    with (root / settings["input_file"]).open() as stream:
        cases = [json.loads(line) for line in stream if line.strip()]
    review = json.loads((root / settings["review_file"]).read_text())
    if ([case["case_id"] for case in cases] != review["approved_case_ids"]
            or len({case["case_id"] for case in cases}) != len(cases) or review.get("held_cases")):
        raise ValueError("Unique ordered input review changed")
    return cases


def ordered_union(full, groups):
    flat = [case for group in groups for case in group]
    ids = [case["case_id"] for case in flat]
    if flat != full or len(ids) != len(set(ids)):
        raise ValueError("Shard union changes/misses/duplicates/reorders original cases or image bytes")
    return {"complete": True, "union_matches_full_test_ids": True, "expected_test_case_count": len(full),
            "unique_observed_case_count": len(ids), "missing_case_count": 0, "extra_case_count": 0,
            "duplicate_case_count": 0, "ordered_case_ids_sha256": digest(ids)}


def original_unstarted(root, settings):
    folder = root / "results/runs" / settings["run_id"]
    result = {"run_id": settings["run_id"], "run_folder_exists": folder.exists(),
              "manifest_exists": (folder / "run_manifest.json").exists(),
              "request_files": len(list((folder / "requests").glob("*"))),
              "response_files": len(list((folder / "responses").glob("*"))),
              "scores_exist": (folder / "scores.json").exists(),
              "completion_exists": (folder / "completion.json").exists()}
    if result["run_folder_exists"]:
        raise ValueError("Original PathVQA run started/reserved; never migrate")
    return result


def require_approval(root=ROOT, config_name=None):
    plan_path = root / PLAN
    plan = json.loads(plan_path.read_text())
    approval = json.loads((root / APPROVAL).read_text())
    expected = {plan["aggregate_config_file"]: plan["aggregate_config_sha256"],
                **{row["config_file"]: row["config_sha256"] for row in plan["shards"]}}
    if (approval.get("approved") is not True or approval.get("plan_file") != PLAN
            or approval.get("plan_sha256") != file_digest(plan_path)
            or approval.get("approved_config_sha256") != expected):
        raise ValueError("PathVQA seven-GPU plan disabled or exact root approval differs")
    if config_name is not None and (config_name not in expected or file_digest(root / config_name) != expected[config_name]):
        raise ValueError("Config differs from approved exact plan")
    if file_digest(root / ORIGINAL_CONFIG) != plan["original_config_sha256"] or file_digest(root / RUNNER) != RUNNER_SHA256:
        raise ValueError("Original config or fixed runner changed")
    original_unstarted(root, json.loads((root / ORIGINAL_CONFIG).read_text()))
    return plan


def raw_audit(root, folder, cases, settings, config_hash):
    """Verify/lock generations and absent slots without labels or scoring."""
    manifest_path = folder / "run_manifest.json"
    manifest = json.loads(manifest_path.read_text())
    if (manifest["configuration"] != settings or manifest["configuration_sha256"] != config_hash
            or manifest["runner_sha256"] != RUNNER_SHA256
            or manifest["case_contract_sha256"] != digest(cases) or manifest["planned_cases"] != len(cases)
            or manifest.get("solver_tools") != [] or manifest.get("answer_keys_available_to_solver") is not False
            or manifest.get("model_selection_on_test") is not False):
        raise ValueError("Immutable shard manifest/input/runner identity mismatch")
    server, serving = manifest["server"], manifest["serving_configuration"]
    gpu = settings["gpu_ids"][0]
    port = dict(REPLICAS)[gpu]
    if (server.get("gpu_ids") != [gpu] or any(type(value) is not int for value in server.get("gpu_ids", []))
            or type(server.get("pid")) is not int or server["pid"] <= 0 or not server.get("proc_start_ticks")
            or serving.get("gpu_ids") != [gpu] or serving.get("host") != "127.0.0.1" or serving.get("port") != port
            or any(type(value) is not int for value in serving.get("gpu_ids", []))
            or type(serving.get("port")) is not int
            or any(row.get("model") != settings["model"] or row.get("revision") != settings["model_revision"] for row in [server, serving])):
        raise ValueError("Historical actual server/replica mismatch")
    expected_names = {digest([case["task"], case["variant"], case["case_id"]]) + ".json" for case in cases}
    for category in ["requests", "responses"]:
        if {path.name for path in (folder / category).glob("*.json")} - expected_names:
            raise ValueError("Unexpected alternate raw case/completion")
    hashes = {"run_manifest.json": file_digest(manifest_path)}
    statuses = Counter()
    for case in cases:
        name = digest([case["task"], case["variant"], case["case_id"]]) + ".json"
        records = {}
        for category in ["requests", "responses"]:
            relative = category + "/" + name
            path = folder / relative
            raw = path.read_bytes() if path.exists() else None
            hashes[relative] = hashlib.sha256(raw).hexdigest() if raw is not None else None
            records[category] = json.loads(raw) if raw is not None else None
        request, response = records["requests"], records["responses"]
        if request is not None and request != runner.request_record(case, settings):
            raise ValueError("Request differs from unchanged original question/image/model payload")
        if response is not None:
            if request is None or any(response.get(key) != value for key, value in {
                **{key: case[key] for key in ["task", "case_id", "variant", "split"]},
                "model": settings["model"], "model_revision": settings["model_revision"],
                "request_sha256": request["request_sha256"]}.items()):
                raise ValueError("Response provenance differs from frozen request")
            if response.get("status") == "completed":
                api = response.get("response", {})
                choices = api.get("choices", [])
                if (response.get("http_status") != 200 or api.get("model") != settings["model"] or len(choices) != 1
                        or response.get("text") != (choices[0].get("message", {}).get("content") or "")
                        or response.get("finish_reason") != choices[0].get("finish_reason")):
                    raise ValueError("Completed raw answer/finish/server identity mismatch")
        statuses[response.get("status") if response else "interrupted_unknown_completion" if request else "not_dispatched"] += 1
    record = {"files_sha256": hashes, "contract_sha256": digest(hashes), "statuses": dict(statuses),
              "server": server, "serving_configuration": serving,
              "policy": "Generation-only provenance lock before any reference read; missing slots retained; no repair/resampling/shard scoring."}
    path = folder / "generation_output_lock.json"
    if path.exists() and json.loads(path.read_text()) != record:
        raise ValueError("Locked raw generation/missing slot changed")
    if not path.exists():
        runner.write_json(path, record)
    return record


def prepare(root=ROOT, expected_cases=6719):
    root = Path(root).resolve()
    if any((root / name).exists() for name in [PLAN, APPROVAL, AUDIT, FULL_CONFIG]):
        raise ValueError("Preserve existing routing version")
    if file_digest(root / RUNNER) != RUNNER_SHA256:
        raise ValueError("Strict runner pin changed")
    original_path = root / ORIGINAL_CONFIG
    original = json.loads(original_path.read_text())
    audit = original_unstarted(root, original)
    cases = cases_for(root, original)
    if len(cases) != expected_cases or original["approved_task_ids"] != ["V03"]:
        raise ValueError("Original full mirror case count/task changed")
    review = json.loads((root / original["review_file"]).read_text())
    timestamp = dt.datetime.now(dt.timezone.utc).isoformat()
    hashes = {**original["frozen_files_sha256"], **{name: file_digest(root / name) for name in [RUNNER, SCORER, PREPARER, EXECUTOR, AGGREGATOR, ORIGINAL_CONFIG]}}
    full = copy.deepcopy(original)
    full.update(run_id=original["run_id"] + "_seven_gpu", runner=RUNNER, executor=EXECUTOR,
                endpoint="aggregate-only://offline", aggregate_only=True, generator_execution_allowed=False,
                case_scope="aggregate_only_full_publisher_mirror_test", full_test_case_count=len(cases),
                shard_size=SHARD_SIZE, shard_count=(len(cases) + SHARD_SIZE - 1) // SHARD_SIZE,
                routing_plan_file=PLAN, execution_approval_file=APPROVAL, frozen_at_utc=timestamp,
                original_unstarted_run_id=original["run_id"], frozen_files_sha256=hashes)
    for field in ["gpu_ids", "serving_config_file", "server_record_file"]:
        full.pop(field, None)
    groups, entries, payload_proofs = [], [], []
    for index, start in enumerate(range(0, len(cases), SHARD_SIZE)):
        group = cases[start:start + SHARD_SIZE]
        groups.append(group)
        gpu, port = REPLICAS[index % len(REPLICAS)]
        input_name = f"data/local_pathvqa_seven_gpu/shard_{index:03d}/model_inputs.jsonl"
        review_name = f"configs/local_pathvqa_seven_gpu_shard_{index:03d}_review.json"
        config_name = f"configs/local_pathvqa_seven_gpu_shard_{index:03d}.json"
        write_new(root / input_name, group, True)
        write_new(root / review_name, {**review, "approved_case_ids": [case["case_id"] for case in group],
                                      "approved_cases": len(group), "case_scope": "task_shard_only",
                                      "whole_task_review_file": original["review_file"],
                                      "whole_task_review_sha256": file_digest(root / original["review_file"])})
        shard = {**full, "run_id": full["run_id"] + f"_shard_{index:03d}", "input_file": input_name,
                 "review_file": review_name, "aggregate_only": False, "generator_execution_allowed": True,
                 "case_scope": "task_shard_only", "shard_index": index, "source_start_index": start,
                 "source_stop_index": start + len(group), "aggregate_config_file": FULL_CONFIG,
                 "full_input_file": original["input_file"], "full_review_file": original["review_file"],
                 "gpu_ids": [gpu], "endpoint": f"http://127.0.0.1:{port}/v1",
                 "serving_config_file": f"configs/local_model_gpu{gpu}.json" if gpu != 5 else "configs/local_model.json",
                 "server_record_file": f".local/local_model_server_gpu{gpu}.json" if gpu != 5 else ".local/local_model_server.json",
                 "frozen_files_sha256": {**hashes, input_name: file_digest(root / input_name), review_name: file_digest(root / review_name)}}
        for case in group:
            old_payload = original_runner.request_record(case, original)
            new_payload = runner.request_record(case, shard)
            if old_payload != new_payload:
                raise ValueError("Routing alters original image/question/model payload")
            payload_proofs.append({"case_id": case["case_id"], "request_sha256": old_payload["request_sha256"], "image_sha256": old_payload["image_sha256"]})
        write_new(root / config_name, shard)
        entries.append({"config_file": config_name, "config_sha256": file_digest(root / config_name),
                        "run_id": shard["run_id"], "shard_index": index, "cases": len(group), "gpu_ids": [gpu], "endpoint": shard["endpoint"]})
    union = ordered_union(cases, groups)
    full["shard_configs"] = entries
    full["full_test_id_union_validation"] = union
    write_new(root / FULL_CONFIG, full)
    original_unstarted(root, original)
    if file_digest(original_path) != hashes[ORIGINAL_CONFIG] or any(file_digest(root / name) != expected for name, expected in original["frozen_files_sha256"].items()):
        raise ValueError("Original frozen artifacts changed during preparation")
    audit.update(checked_at_utc=timestamp, original_config_file=ORIGINAL_CONFIG, original_config_sha256=hashes[ORIGINAL_CONFIG],
                 original_frozen_files_sha256=original["frozen_files_sha256"], all_model_payloads_identical=True,
                 payload_proof_sha256=digest(payload_proofs), case_count=len(cases), full_test_id_union_validation=union)
    write_new(root / AUDIT, audit)
    plan = {"frozen_at_utc": timestamp, "task_id": "V03", "original_config_file": ORIGINAL_CONFIG,
            "original_config_sha256": hashes[ORIGINAL_CONFIG], "original_unstarted_run_id": original["run_id"],
            "aggregate_config_file": FULL_CONFIG, "aggregate_config_sha256": file_digest(root / FULL_CONFIG),
            "aggregate_run_id": full["run_id"], "full_test_case_count": len(cases), "shard_size": SHARD_SIZE,
            "shard_count": len(entries), "shards": entries, "full_test_id_union_validation": union,
            "runner": RUNNER, "runner_sha256": RUNNER_SHA256, "scorer": SCORER,
            "execution_approval_file": APPROVAL, "unstarted_payload_audit_file": AUDIT,
            "unstarted_payload_audit_sha256": file_digest(root / AUDIT), "inference_dispatched": False,
            "authorizations_or_queues_modified": False, "metric_policy": original["metric_policy"],
            "source_qualification": original["paper_comparison"],
            "aggregation_policy": "One original full-case scorer call after exact ordered case/image/payload union and terminal raw provenance audit. No shard metric averages; native corrected/bug diagnostics unchanged; actual source servers retained."}
    write_new(root / PLAN, plan)
    approved = {FULL_CONFIG: plan["aggregate_config_sha256"], **{row["config_file"]: row["config_sha256"] for row in entries}}
    write_new(root / APPROVAL, {"approved": False, "plan_file": PLAN, "plan_sha256": file_digest(root / PLAN),
                              "approved_config_sha256": approved, "root_activation_required": True})
    return {"plan": PLAN, "plan_sha256": file_digest(root / PLAN), "approval_file": APPROVAL, "approved": False,
            "cases": len(cases), "shards": len(entries), "shard_case_counts": [row["cases"] for row in entries], "all_original_payloads_identical": True}


if __name__ == "__main__":
    argparse.ArgumentParser(description=__doc__).parse_args()
    print(json.dumps(prepare()))
