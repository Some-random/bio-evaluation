"""Offline exact P29 shard union and a single global native GO-F1 scorer call."""
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

import local_posttrain_protein_shards as common
from score_local_posttrain_protein import lock_outputs as lock_global_outputs


class Pending(Exception):pass


def checked(name,expected):
    path=common.ROOT/name
    if common.file_sha(path)!=expected:raise ValueError("Frozen config/source changed: "+name)
    return json.loads(path.read_text())


def validate_plan(plan):
    full=checked(plan["aggregate_config_file"],plan["aggregate_config_sha256"])
    base=checked(plan["source_recipe_file"],plan["source_recipe_sha256"])
    cases=common.cases_for(full)
    if (len(cases)!=common.protocol.SPLITS[full["native_split"]][1] or full["full_test_case_count"]!=len(cases) or full["shard_configs"]!=plan["shards"]
        or full.get("aggregate_only") is not True or full.get("generator_execution_allowed") is not False
        or full["endpoint"]!="aggregate-only://offline" or full["incomplete_output_policy"]!=plan["incomplete_output_policy"]):raise ValueError("Plan/full source input contract mismatch")
    if any(full[k]!=base[k] for k in ["model","model_revision","checkpoint_precision","generation","concurrency"]) or full["generation"]["max_tokens"]!=4096:raise ValueError("Recipe differs from original fixed4096B07 baseline")
    terminal=[];pending=[]
    for item in plan["shards"]:
        path=common.ROOT/"results/runs"/item["run_id"]/"completion.json"
        if not path.exists():pending.append(item["run_id"])
        else:
            record=json.loads(path.read_text())
            if record.get("raw_audit_exit_code")!=0 or record.get("scoring_exit_code")!=0:raise ValueError("Shard raw provenance/audit failed; no score or generation retry")
            if type(record.get("generation_exit_code")) is not int:raise ValueError("Shard lacks terminal generation status")
            terminal.append(record)
    if pending:raise Pending(str(len(pending))+" of "+str(len(plan["shards"]))+" planned shards pending")
    groups=[];sources=[]
    for index,(item,completion) in enumerate(zip(plan["shards"],terminal)):
        shard=checked(item["config_file"],item["config_sha256"]);approval=common.approval_for(common.ROOT/item["config_file"],shard)
        if (common.recipe(full)!=common.recipe(shard) or shard.get("aggregate_only") is not False
            or shard.get("generator_execution_allowed") is not True or shard["shard_index"]!=index
            or shard["shard_count"]!=len(plan["shards"]) or shard["shard_size"]!=common.SHARD_SIZE
            or shard["aggregate_config_file"]!=plan["aggregate_config_file"] or shard["full_input_file"]!=full["input_file"]
            or shard["full_input_sha256"]!=common.file_sha(common.ROOT/full["input_file"])
            or shard["full_review_file"]!=full["review_file"] or shard["full_review_sha256"]!=common.file_sha(common.ROOT/full["review_file"])
            or shard["incomplete_output_policy"]!=plan["incomplete_output_policy"]
            or shard["global_shard_index"]!=plan["global_shard_start_index"]+index):raise ValueError("Shard model/recipe/full-input contract mismatch")
        start,stop=index*common.SHARD_SIZE,min((index+1)*common.SHARD_SIZE,len(cases));group=common.cases_for(shard)
        if (shard["source_start_index"]!=start or shard["source_stop_index"]!=stop or group!=cases[start:stop]
            or len(group)!=item["cases"]):raise ValueError("Shard differs from exact source-order slice")
        folder=common.ROOT/"results/runs"/shard["run_id"]
        for name,field in [("run_manifest.json","run_manifest_sha256"),("scores.json","scores_sha256"),("scoring_output_lock.json","scoring_output_lock_sha256")]:
            if common.file_sha(folder/name)!=completion.get(field):raise ValueError("Terminal shard artifact hash changed: "+name)
        if completion.get("configuration_sha256")!=item["config_sha256"] or completion.get("execution_approval")!=approval or any(completion.get(k)!=v for k,v in common.metadata(shard).items()):raise ValueError("Terminal shard approval/config/range contract changed")
        audit,lock=common.audit_raw(folder,group,shard,item["config_sha256"],require_lock=True)
        if json.loads((folder/"scores.json").read_text())!=audit:raise ValueError("Label-free shard accounting differs from raw output audit")
        manifest=json.loads((folder/"run_manifest.json").read_text())
        groups.append(group);sources.append({**item,"generation_exit_code":completion["generation_exit_code"],"completed":audit["completed"],"planned":len(group),
            "completion_sha256":common.file_sha(folder/"completion.json"),"run_manifest_sha256":common.file_sha(folder/"run_manifest.json"),
            "scores_sha256":common.file_sha(folder/"scores.json"),"scoring_output_lock_sha256":common.file_sha(folder/"scoring_output_lock.json"),
            "raw_files_sha256":{k:v for k,v in lock["files_sha256"].items() if k!="run_manifest.json"},
            "server":manifest["server"],"serving_configuration":manifest["serving_configuration"],"execution_approval":approval})
    return full,cases,sources,common.ordered_union(cases,groups)


def install_raw(source,target,expected):
    if expected is None:
        if source.exists() or target.exists():raise ValueError("Frozen missing output slot appeared")
        return
    if common.file_sha(source)!=expected:raise ValueError("Source raw output changed after validation")
    target.parent.mkdir(parents=True,exist_ok=True)
    if target.exists():
        if common.file_sha(target)!=expected:raise ValueError("Aggregate raw output changed")
    else:
        try:os.link(source,target)
        except OSError:shutil.copyfile(source,target)
    if common.file_sha(target)!=expected:raise ValueError("Aggregate raw output copy mismatch")


def run_native_scorer(full):
    return subprocess.run([sys.executable,"-u",str(common.ROOT/common.SCORER),"--run",full["run_id"]],cwd=common.ROOT).returncode


def aggregate(plan,plan_sha):
    full,cases,sources,union=validate_plan(plan);folder=common.ROOT/"results/runs"/full["run_id"];folder.mkdir(parents=True,exist_ok=True)
    provenance={"plan_sha256":plan_sha,"aggregate_config_sha256":plan["aggregate_config_sha256"],"full_test_id_union_validation":union,"sources":sources,
        "policy":plan["global_metric_policy"],"incomplete_output_policy":plan["incomplete_output_policy"]}
    manifest={"configuration":full,"configuration_sha256":plan["aggregate_config_sha256"],"runner_sha256":full["frozen_files_sha256"][common.RUNNER],
        "aggregate_builder_sha256":common.file_sha(Path(__file__)),"case_contract_sha256":common.digest(cases),"planned_cases":len(cases),
        "solver_tools":[],"answer_keys_available_to_solver":False,"model_selection_on_test":False,"aggregate_only":True,"source_shard_provenance_sha256":common.digest(provenance)}
    for name,value in [("run_manifest.json",manifest),("source_shard_manifest.json",provenance)]:
        path=folder/name
        if path.exists() and json.loads(path.read_text())!=value:raise ValueError("Aggregate historical provenance changed")
        if not path.exists():common.save(path,value)
    for source in sources:
        source_folder=common.ROOT/"results/runs"/source["run_id"]
        for name,expected in source["raw_files_sha256"].items():install_raw(source_folder/name,folder/name,expected)
    for kind in ["requests","responses"]:
        expected={Path(name).name for src in sources for name,h in src["raw_files_sha256"].items() if name.startswith(kind+"/") and h is not None}
        if {p.name for p in (folder/kind).glob("*.json")}!=expected:raise ValueError("Extra/missing available aggregate raw files")
    # This is exactly the stable core scorer's own output lock, not another
    # policy variant. No reference bytes have been read by this process.
    output_lock=lock_global_outputs(folder,cases)
    done_path=folder/"completion.json"
    if done_path.exists():
        done=json.loads(done_path.read_text())
        if done.get("scoring_exit_code")!=0 or done.get("source_shard_provenance_sha256")!=common.digest(provenance):raise ValueError("Existing terminal aggregate failed/changed; no repeat scorer")
        for name,field in [("scores.json","scores_sha256"),("run_manifest.json","run_manifest_sha256"),("source_shard_manifest.json","source_manifest_sha256"),("scoring_output_lock.json","scoring_output_lock_sha256")]:
            if common.file_sha(folder/name)!=done[field]:raise ValueError("Completed aggregate artifact hash changed: "+name)
        return done
    invocation=folder/"global_scoring_invocation.json"
    if invocation.exists():raise ValueError("Global scorer already invoked without terminal record; preserve outputs and require offline recovery, no automatic repeat")
    common.save(invocation,{"started_at_utc":dt.datetime.now(dt.timezone.utc).isoformat(),"source_shard_provenance_sha256":common.digest(provenance),
        "global_output_lock_sha256":output_lock["contract_sha256"],"native_metric_calls_planned":1,"shard_metrics_averaged":False})
    code=run_native_scorer(full)
    generation_code=0 if all(src["generation_exit_code"]==0 and src["completed"]==src["planned"] for src in sources) else 1
    summary_path=folder/"scores.json"
    if code==0:
        summary=json.loads(summary_path.read_text())
        if summary["planned"]!=len(cases) or summary["completed"]!=sum(src["completed"] for src in sources):raise ValueError("Global scorer eligible denominator/completion mismatch")
        parallel={"mode":"independent identical TP1 replicas","gpu_ids":sorted({g for s in sources for g in s["gpu_ids"]}),"replica_count":len({(s["server"].get("slurm_job_id"),s["server"].get("hostname"),s["server"].get("pid")) for s in sources}),"shard_count":len(sources),
            "servers":[{k:s[k] for k in ["run_id","gpu_ids","endpoint","server"]} for s in sources]}
        summary.update(full_test_id_union_validation=union,parallel_gpu_metadata=parallel,source_shard_provenance_sha256=common.digest(provenance),
            request_response_hash_audit="passed",native_global_metric_call_count=1,aggregation_policy=plan["global_metric_policy"],
            source_generation_failure_count=sum(s["generation_exit_code"]!=0 for s in sources))
        # Preserve the core scorer's INCOMPLETE scope even when input ID union
        # is complete. Native CAFA uses all eligible GT, including failures.
        common.save(summary_path,summary)
    done={"generation_exit_code":generation_code,"scoring_exit_code":code,"finished_at_utc":dt.datetime.now(dt.timezone.utc).isoformat(),"aggregate_only":True,
        "configuration_sha256":plan["aggregate_config_sha256"],"source_shard_provenance_sha256":common.digest(provenance),"full_test_id_union_validation":union,
        "source_generation_failure_count":sum(s["generation_exit_code"]!=0 for s in sources),"retry_or_resampling":False,
        "evaluation_status":"complete" if generation_code==0 and code==0 else "incomplete_allcase_scored" if code==0 else "native_scoring_failed",
        "run_manifest_sha256":common.file_sha(folder/"run_manifest.json"),"source_manifest_sha256":common.file_sha(folder/"source_shard_manifest.json"),
        "scoring_output_lock_sha256":common.file_sha(folder/"scoring_output_lock.json")}
    if summary_path.exists():done.update(scores_sha256=common.file_sha(summary_path),case_scope=json.loads(summary_path.read_text())["case_scope"])
    common.save(done_path,done)
    if code:raise ValueError("Global native scorer failed; outputs retained, no automatic repeat")
    return done


def watch(plan_path,continuous=False,poll_seconds=30):
    if not 1<=poll_seconds<=60:raise ValueError("Polling must be1-60seconds")
    plan_sha=common.file_sha(plan_path);plan=json.loads(plan_path.read_text());lock_path=common.ROOT/".local/local_posttrain_protein_aggregation.lock";lock_path.parent.mkdir(parents=True,exist_ok=True)
    with lock_path.open("a") as lock:
        fcntl.flock(lock,fcntl.LOCK_EX|fcntl.LOCK_NB)
        while True:
            if common.file_sha(plan_path)!=plan_sha:raise ValueError("Plan changed while watching")
            states=[];pending=False;failed=False
            for group in plan["aggregates"]:
                try:
                    result=aggregate(group,plan_sha)
                    state={"status":result["evaluation_status"],"native_split":group["native_split"],"run_id":group["aggregate_run_id"],"completion":result}
                    failed|=result["generation_exit_code"]!=0
                except Pending as exc:state={"status":"pending","native_split":group["native_split"],"detail":str(exc)};pending=True
                except Exception as exc:state={"status":"blocked","native_split":group["native_split"],"detail":str(exc),"retry_or_resampling":False};failed=True
                states.append(state)
            common.save(common.ROOT/"reports/local_posttrain_protein_shard_aggregation.json",{"states":states,"inference_dispatched":False,"plan_sha256":plan_sha})
            print(json.dumps(states),flush=True)
            if not continuous or not pending:return 1 if failed else 2 if pending else 0
            time.sleep(poll_seconds)


if __name__=="__main__":
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument("--plan",type=Path,default=common.ROOT/common.PLAN_FILE);parser.add_argument("--watch",action="store_true");parser.add_argument("--poll-seconds",type=int,default=30)
    args=parser.parse_args();raise SystemExit(watch(args.plan,args.watch,args.poll_seconds))
