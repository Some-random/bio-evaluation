"""Input-only shard contracts, exact-plan gate and label-free raw audits for P28."""
from collections import Counter
import json
from pathlib import Path

import bioreason_pro_contract as protocol
from run_local_labbench_multimodal import payload_for,request_record

ROOT=protocol.ROOT
RUNNER="scripts/run_local_labbench_eight_gpu.py"
RUNNER_SHA256="de0c69b2eea33d618a7674791d6ae448fd8c086a7ba081e948dafdfdcaed4493"
SCORER="scripts/score_local_bioreason_pro.py"
PLAN_FILE="reports/local_bioreason_shard_plan.json"
APPROVAL_FILE="configs/local_bioreason_execution_approval.json"
FULL_CONFIG="configs/local_bioreason_p28_aggregate.json"
FULL_INPUT="data/catalog_bioreason_pro/P28/model_inputs.jsonl"
FULL_REVIEW="configs/local_bioreason_p28_review.json"
SHARD_SIZE=1024
EXPECTED_CASES=8159
REPLICAS=((1,8031),(2,8032),(3,8033),(4,8029),(5,8026),(6,8027),(7,8028))
digest=protocol.digest
file_sha=protocol.file_sha
save=protocol.save
META=("shard_index","shard_count","shard_size","full_test_case_count","source_start_index","source_stop_index",
      "aggregate_config_file","full_input_file","full_input_sha256","full_review_file","full_review_sha256")


def metadata(settings):return {k:settings[k] for k in META}


def recipe(settings):
    return {k:settings[k] for k in ["model","model_revision","checkpoint_precision","generation","concurrency","variant",
        "model_facing_fields","prompt_policy","scorer_reference_file","scorer_reference_sha256"]}


def ordered_union(full,groups):
    observed=[r for group in groups for r in group];ids=[r["case_id"] for r in observed];expected=[r["case_id"] for r in full]
    if observed!=full or len(ids)!=len(set(ids)) or len(expected)!=len(set(expected)):raise ValueError("Shard union differs from exact complete ordered eligible input cases")
    return {"complete":True,"union_matches_full_test_ids":True,"expected_test_case_count":len(full),
        "unique_observed_case_count":len(set(ids)),"missing_case_count":0,"extra_case_count":0}


def approval_for(config_path,settings):
    if settings.get("execution_authorized") is not False or settings.get("input_review_complete") is not True:raise ValueError("Require unchanged reviewed prospective config")
    plan_path=ROOT/settings["shard_plan_file"];plan=json.loads(plan_path.read_text());approval_path=ROOT/APPROVAL_FILE
    approval=json.loads(approval_path.read_text());relative=str(config_path.resolve().relative_to(ROOT.resolve()))
    entries=[r for r in plan["shards"] if r["config_file"]==relative]
    if (approval.get("execution_authorized") is not True or approval.get("plan_sha256")!=file_sha(plan_path)
        or approval.get("approved_task_ids")!=["P28"] or approval.get("model")!=settings["model"]
        or approval.get("model_revision")!=settings["model_revision"] or approval.get("generation_sha256")!=digest(settings["generation"])
        or len(entries)!=1 or entries[0]["config_sha256"]!=file_sha(config_path)
        or approval.get("approved_config_sha256",{}).get(relative)!=file_sha(config_path)
        or approval.get("incomplete_output_policy")!=plan["incomplete_output_policy"]):
        raise ValueError("No exact P28 plan/model/recipe/config/incomplete-policy execution approval")
    return {"approval_file":APPROVAL_FILE,"approval_sha256":file_sha(approval_path),"plan_sha256":file_sha(plan_path)}


def cases_for(settings):
    reference=(ROOT/settings["scorer_reference_file"]).resolve()
    for name,expected in settings["frozen_files_sha256"].items():
        if (ROOT/name).resolve()==reference:raise ValueError("Scorer-only reference must not enter generator preflight hash reads")
        if file_sha(ROOT/name)!=expected:raise ValueError("Frozen dependency changed: "+name)
    cases=[json.loads(s) for s in (ROOT/settings["input_file"]).read_text().splitlines() if s]
    review=json.loads((ROOT/settings["review_file"]).read_text());ids=[c["case_id"] for c in cases]
    if not cases or review.get("reviewed") is not True or ids!=review["approved_case_ids"] or len(ids)!=len(set(ids)) or review.get("held_cases"):raise ValueError("Reviewed source-order cases changed")
    for case in cases:payload_for(case,settings)
    return cases


def lock_raw(folder,cases):
    hashes={"run_manifest.json":file_sha(folder/"run_manifest.json")}
    for case in cases:
        identity=digest([case["task"],case["variant"],case["case_id"]])+".json"
        for kind in ["requests","responses"]:
            name=kind+"/"+identity;path=folder/name;hashes[name]=file_sha(path) if path.exists() else None
    lock={"files_sha256":hashes,"contract_sha256":digest(hashes),"labels_read":False,
        "policy":"Raw shard outputs and every missing slot frozen before any labels; native CAFA metrics deferred until whole ordered union."}
    path=folder/"scoring_output_lock.json"
    if path.exists() and json.loads(path.read_text())!=lock:raise ValueError("Shard raw output/missing-slot lock changed")
    if not path.exists():save(path,lock)
    return lock


def audit_raw(folder,cases,settings,config_sha256,require_lock=False):
    if require_lock and not (folder/"scoring_output_lock.json").exists():raise ValueError("Terminal shard lacks pre-label raw lock")
    manifest=json.loads((folder/"run_manifest.json").read_text())
    if (manifest["configuration"]!=settings or manifest["configuration_sha256"]!=config_sha256
        or manifest["case_contract_sha256"]!=digest(cases) or manifest["planned_cases"]!=len(cases)
        or manifest["runner_sha256"]!=settings["frozen_files_sha256"][RUNNER]
        or manifest.get("solver_tools")!=[] or manifest.get("answer_keys_available_to_solver") is not False
        or manifest.get("model_selection_on_test") is not False):raise ValueError("Shard manifest/input/provenance mismatch")
    server,serving=manifest["server"],manifest["serving_configuration"]
    gpu,port=REPLICAS[settings["shard_index"]%len(REPLICAS)]
    if (settings["gpu_ids"]!=[gpu] or settings["endpoint"]!=f"http://127.0.0.1:{port}/v1"
        or server.get("model")!=settings["model"] or server.get("revision")!=settings["model_revision"]
        or server.get("gpu_ids")!=[gpu] or not server.get("pid") or not server.get("proc_start_ticks")
        or server.get("port",port)!=port or server.get("endpoint",settings["endpoint"])!=settings["endpoint"]
        or serving.get("host")!="127.0.0.1" or serving.get("port")!=port or serving.get("gpu_ids")!=[gpu]
        or serving.get("model")!=settings["model"] or serving.get("revision")!=settings["model_revision"]):raise ValueError("Historical exact local server/replica identity mismatch")
    names={digest([c["task"],c["variant"],c["case_id"]])+".json" for c in cases}
    for kind in ["requests","responses"]:
        if not {p.name for p in (folder/kind).glob("*.json")}<=names:raise ValueError("Extra shard raw output identity")
    lock=lock_raw(folder,cases);states=Counter();finishes=Counter();completed=parsed=request_count=response_count=0
    for case in cases:
        identity=digest([case["task"],case["variant"],case["case_id"]])+".json"
        records=[]
        for kind in ["requests","responses"]:
            name=kind+"/"+identity;path=folder/name;expected=lock["files_sha256"][name]
            if expected is not None and file_sha(path)!=expected:raise ValueError("Raw shard artifact changed after locking")
            if expected is None and path.exists():raise ValueError("Raw output appeared after locked missing slot")
            records.append(json.loads(path.read_text()) if expected is not None else None)
        request,response=records;request_count+=request is not None;response_count+=response is not None
        if request is not None and request!=request_record(case,settings):raise ValueError("Raw request differs from full original input/recipe")
        if response is not None:
            if request is None:raise ValueError("Raw response without request")
            values={**{k:case[k] for k in ["task","case_id","variant","split"]},"model":settings["model"],"model_revision":settings["model_revision"],"request_sha256":request["request_sha256"]}
            if any(response.get(k)!=v for k,v in values.items()):raise ValueError("Raw response identity/model/prompt mismatch")
        status=response.get("status") if response else ("interrupted_unknown_completion" if request else "not_dispatched")
        states[status]+=1
        if status=="completed":
            if response["response"].get("model")!=settings["model"]:raise ValueError("Raw API model mismatch")
            continuation,_,_=protocol.generated_continuation(response);completed+=1;parsed+=bool(protocol.extract_go(continuation));finishes[str(response.get("finish_reason"))]+=1
    return {"task_id":"P28","run_id":settings["run_id"],"case_scope":"task_shard_only","planned":len(cases),"completed":completed,"parsed":parsed,
        "requests_saved":request_count,"responses_saved":response_count,"invalid_outputs":completed-parsed,"missing_or_failed_outputs":len(cases)-completed,
        "statuses":dict(states),"finish_reasons":dict(finishes),"metrics":{},"native_metric_scoring":"deferred_global_only_no_shard_CAFA",
        "scoring_output_lock_sha256":lock["contract_sha256"],"labels_read":False,**metadata(settings)},lock
