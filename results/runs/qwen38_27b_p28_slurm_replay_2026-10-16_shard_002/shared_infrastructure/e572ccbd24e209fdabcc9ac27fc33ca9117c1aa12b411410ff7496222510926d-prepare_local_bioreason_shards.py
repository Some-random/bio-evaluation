"""Prepare eight disabled source-order P28 jobs; no inference/allowlist changes."""
import argparse
import datetime as dt
import json

import bioreason_pro_contract as protocol
import local_bioreason_shards as common

ROOT=common.ROOT
SCRIPTS=[common.RUNNER,"scripts/run_local_labbench_multimodal.py",common.SCORER,"scripts/bioreason_pro_contract.py","scripts/prepare_catalog_bioreason_pro.py",
    "scripts/local_bioreason_shards.py","scripts/prepare_local_bioreason_shards.py","scripts/execute_local_bioreason_shard.py","scripts/aggregate_local_bioreason_shards.py"]
INCOMPLETE_POLICY="Wait for every planned shard terminal; preserve all eligible missing/failed/empty predictions as empty GO sets in one global metric. Nonzero source generation remains nonzero aggregate generation; invalid provenance blocks. No retry/resampling or successful-only selection."


def write_new(name,value,jsonl=False):
    path=ROOT/name
    if path.exists():raise ValueError("Refuse replacement of frozen prospective asset: "+name)
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text("".join(json.dumps(r,ensure_ascii=False)+"\n" for r in value) if jsonl else json.dumps(value,ensure_ascii=False,indent=2)+"\n")
    path.chmod(0o600)


def prepare():
    if (ROOT/common.PLAN_FILE).exists():raise ValueError("P28 plan already frozen")
    if common.file_sha(ROOT/common.RUNNER)!=common.RUNNER_SHA256:raise ValueError("Root-reviewed expanded runner hash changed")
    folder="data/catalog_bioreason_pro/P28";prepared=json.loads((ROOT/folder/"preparation.json").read_text())
    if common.file_sha(ROOT/common.FULL_INPUT)!=prepared["eligible_input_sha256"] or prepared["native_eligible_cases"]!=common.EXPECTED_CASES:raise ValueError("Stable native eligible release changed")
    cases=[json.loads(s) for s in (ROOT/common.FULL_INPUT).read_text().splitlines() if s]
    ids=[c["case_id"] for c in cases]
    if len(cases)!=common.EXPECTED_CASES or ids!=json.loads((ROOT/folder/"ordered_eligible_case_ids.json").read_text()) or len(ids)!=len(set(ids)):raise ValueError("Original ordered eligible IDs changed")
    if any(c["task"]!="P28" or c["variant"]!=protocol.VARIANT or c["split"]!="released_temporal_test_native_exclusions" or set(c)!={"task","case_id","variant","split","messages"} for c in cases):raise ValueError("Original native case contract changed")
    groups=[cases[i:i+common.SHARD_SIZE] for i in range(0,len(cases),common.SHARD_SIZE)]
    union=common.ordered_union(cases,groups)
    base_name="configs/local_labbench_b07.json";base=json.loads((ROOT/base_name).read_text())
    if base["generation"]["max_tokens"]!=4096:raise ValueError("Only existing4096-token baseline is proposed")
    timestamp=dt.datetime.now(dt.timezone.utc).isoformat()
    review={"task_id":"P28","reviewed":True,"input_review_only":True,"reviewed_at_utc":timestamp,
        "source_input_path":common.FULL_INPUT,"source_input_sha256":common.file_sha(ROOT/common.FULL_INPUT),
        "basis":"Exact complete sequence and source-native label-independent organism/InterPro/STRING/GO-GPT input allowlist verified by frozen preparation. Generic protein annotation prediction; no biological optimization or operational protocols. Original temporal exclusion IDs only; no target- or output-based case selection.",
        "approved_case_ids":ids,"held_cases":[],"approved_cases":len(cases),"released_cases":8630,"native_excluded_cases":471,
        "classification_is_provisional":True,"execution_authorized_by_this_review":False}
    write_new(common.FULL_REVIEW,review)
    frozen=protocol.verified_sources()
    for name in SCRIPTS+[base_name,common.FULL_INPUT,common.FULL_REVIEW,folder+"/preparation.json",folder+"/ordered_eligible_case_ids.json",
        folder+"/excluded_native_case_ids.json",folder+"/ordered_released_case_ids.json",folder+"/input_provenance.json",
        "reports/bioreason_pro_native_contract_audit.json","reports/BIOREASON_PRO_NATIVE_CONTRACT_AUDIT.md"]:
        frozen[name]=common.file_sha(ROOT/name)
    reference=folder+"/scorer_references.jsonl"
    reference_hash=prepared["files"]["scorer_references.jsonl"]["sha256"]
    full=dict(base)
    full.update(run_id="qwen38_27b_p28_full_native_eligible_parallel_2026-10-15",frozen_at_utc=timestamp,
        execution_authorized=False,input_review_complete=True,approved_task_ids=["P28"],variant=protocol.VARIANT,
        input_file=common.FULL_INPUT,review_file=common.FULL_REVIEW,runner=common.RUNNER,
        scorer_reference_file=reference,scorer_reference_sha256=reference_hash,
        source_dataset_revision=protocol.DATA_REVISION,source_code_revision=protocol.CODE_REVISION,
        model_facing_fields=prepared["model_facing_fields"],input_modalities=["complete_amino_acid_sequence","organism","native_predictor_derived_text_context"],
        prompt_policy="Exact frozen source question/context with complete sequence and label-independent all3-aspect/fixed-summary instructions; one unchanged user turn. No gold annotation, teacher trace, prompt-context-as-prediction or extra retrieval.",
        metric_policy="One global native CAFA Fmax and IA-weighted Fmax per BP/MF/CC after exact8159eligible case union. Shards compute no CAFA metric and never read references. Missing/failed/noGO predictions are empty sets; no averaged shard Fmax.",
        paper_comparison=prepared["native_model_difference"]+" "+" ".join(prepared["published_protocol_differences"]),
        full_test_case_count=len(cases),released_test_case_count=8630,native_excluded_case_count=471,shard_count=len(groups),shard_size=common.SHARD_SIZE,
        aggregate_only=True,generator_execution_allowed=False,endpoint="aggregate-only://offline",case_scope="aggregate_only_full_native_eligible_test",
        shard_plan_file=common.PLAN_FILE,incomplete_output_policy=INCOMPLETE_POLICY,frozen_files_sha256=frozen)
    for k in ["gpu_ids","serving_config_file","server_record_file"]:full.pop(k,None)
    entries=[]
    for index,group in enumerate(groups):
        gpu,port=common.REPLICAS[index%len(common.REPLICAS)]
        input_name=f"data/local_bioreason_shards/P28/shard_{index:03d}/model_inputs.jsonl"
        review_name=f"configs/local_bioreason_p28_shard_{index:03d}_review.json"
        config_name=f"configs/local_bioreason_p28_shard_{index:03d}.json"
        start,stop=index*common.SHARD_SIZE,min((index+1)*common.SHARD_SIZE,len(cases))
        write_new(input_name,group,jsonl=True)
        write_new(review_name,{**review,"approved_case_ids":[r["case_id"] for r in group],"approved_cases":len(group),
            "case_scope":"task_shard_only","source_start_index":start,"source_stop_index":stop,"whole_task_review_file":common.FULL_REVIEW,
            "whole_task_review_sha256":common.file_sha(ROOT/common.FULL_REVIEW)})
        shard={**full,"run_id":full["run_id"]+f"_shard_{index:03d}","aggregate_only":False,"generator_execution_allowed":True,
            "input_file":input_name,"review_file":review_name,"endpoint":f"http://127.0.0.1:{port}/v1","gpu_ids":[gpu],
            "serving_config_file":f"configs/local_model_gpu{gpu}.json" if gpu!=5 else "configs/local_model.json",
            "server_record_file":f".local/local_model_server_gpu{gpu}.json" if gpu!=5 else ".local/local_model_server.json",
            "shard_index":index,"source_start_index":start,"source_stop_index":stop,"aggregate_config_file":common.FULL_CONFIG,
            "full_input_file":common.FULL_INPUT,"full_input_sha256":common.file_sha(ROOT/common.FULL_INPUT),
            "full_review_file":common.FULL_REVIEW,"full_review_sha256":common.file_sha(ROOT/common.FULL_REVIEW),"case_scope":"task_shard_only"}
        shard["frozen_files_sha256"]={**frozen,input_name:common.file_sha(ROOT/input_name),review_name:common.file_sha(ROOT/review_name)}
        write_new(config_name,shard)
        entries.append({"config_file":config_name,"config_sha256":common.file_sha(ROOT/config_name),"run_id":shard["run_id"],"shard_index":index,"cases":len(group),"gpu_ids":[gpu],"endpoint":shard["endpoint"]})
    full.update(shard_configs=entries,full_test_id_union_validation=union)
    write_new(common.FULL_CONFIG,full)
    plan={"task_id":"P28","frozen_at_utc":timestamp,"source_recipe_file":base_name,"source_recipe_sha256":common.file_sha(ROOT/base_name),
        "model":base["model"],"model_revision":base["model_revision"],"generation":base["generation"],"concurrency":base["concurrency"],
        "aggregate_config_file":common.FULL_CONFIG,"aggregate_config_sha256":common.file_sha(ROOT/common.FULL_CONFIG),"aggregate_run_id":full["run_id"],
        "full_test_case_count":len(cases),"released_test_case_count":8630,"native_excluded_case_count":471,"shard_size":common.SHARD_SIZE,"shard_count":len(groups),
        "shards":entries,"full_test_id_union_validation":union,"replica_order":[{"gpu_ids":[g],"port":p} for g,p in common.REPLICAS],
        "partition_policy":"Consecutive source-order1024 slices after native471ID exclusions; every eligible row once, no labels/outcomes used.",
        "incomplete_output_policy":INCOMPLETE_POLICY,"global_metric_policy":"Compute native CAFA metrics ONCE from full combined predictions; no shard Fmax or IA-weighted Fmax averaging.",
        "inference_dispatched":False,"authorizations_or_queues_modified":False}
    write_new(common.PLAN_FILE,plan)
    write_new(common.APPROVAL_FILE,{"execution_authorized":False,"approved_task_ids":[],"model":base["model"],"model_revision":base["model_revision"],
        "generation_sha256":common.digest(base["generation"]),"plan_sha256":common.file_sha(ROOT/common.PLAN_FILE),"approved_config_sha256":{},"incomplete_output_policy":INCOMPLETE_POLICY,
        "activation_order":"Review exact frozen plan/configs and authorize this approval before centralP28allowlist activation; run only through gated shard executor. Generic runner ignores perconfig execution_authorized false."})
    print(json.dumps({"plan":common.PLAN_FILE,"sha256":common.file_sha(ROOT/common.PLAN_FILE),"shards":len(groups),"cases":len(cases),"execution_authorized":False}));return plan


if __name__=="__main__":argparse.ArgumentParser(description=__doc__).parse_args();prepare()
