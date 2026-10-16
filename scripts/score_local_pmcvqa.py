"""Offline PMC-VQA clean2000 TD source score and separate output diagnostics."""
import argparse
from collections import Counter
import csv
import hashlib
import json
from pathlib import Path

import pmcvqa_clean_protocol as protocol
from run_local_labbench_multimodal import payload_for,validate_content

ROOT=protocol.ROOT


def lock_outputs(folder,cases):
    files={"run_manifest.json":protocol.file_sha(folder/"run_manifest.json")}
    for case in cases:
        identity=protocol.digest([case["task"],case["variant"],case["case_id"]])+".json"
        for kind in ["requests","responses"]:
            name=kind+"/"+identity;path=folder/name;files[name]=protocol.file_sha(path) if path.exists() else None
    lock={"files_sha256":files,"contract_sha256":protocol.digest(files),"policy":"Every raw output and missing slot locked before gold reads; no output selection, reference-driven repair or retry."}
    path=folder/"scoring_output_lock.json"
    if path.exists() and json.loads(path.read_text())!=lock:raise ValueError("Pre-scoring raw output lock changed")
    if not path.exists():protocol.save_json(path,lock)
    return lock


def locked_record(folder,name,lock):
    path=folder/name;expected=lock["files_sha256"][name]
    if expected is None:
        if path.exists():raise ValueError("Raw output appeared after missing slot lock")
        return None
    raw=path.read_bytes()
    if hashlib.sha256(raw).hexdigest()!=expected:raise ValueError("Raw output changed after lock")
    return json.loads(raw)


def expected_payload(case,settings):
    if settings["generation"]!=protocol.GENERATION or settings["variant"]!=protocol.VARIANT:raise ValueError("Fixed baseline generation/variant changed")
    payload=payload_for(case,settings);parts=case["messages"][0]["content"]
    if not isinstance(parts,list) or len(parts)!=2 or parts[0].get("type")!="text" or parts[1].get("type")!="image_url":raise ValueError("Required TD prompt and original image missing")
    return payload


def score(folder):
    manifest=json.loads((folder/"run_manifest.json").read_text());cfg=manifest["configuration"]
    if cfg["approved_task_ids"]!=["V05"] or cfg["variant"]!=protocol.VARIANT:raise ValueError("Not this fixed V05 protocol")
    reference_path=ROOT/cfg["scorer_reference_file"]
    if manifest.get("solver_tools")!=[] or manifest.get("answer_keys_available_to_solver") is not False or manifest.get("model_selection_on_test") is not False:raise ValueError("Historical solver leakage/tool contract changed")
    mandatory=["scripts/pmcvqa_clean_protocol.py","scripts/score_local_pmcvqa.py",*[r["path"] for r in protocol.native_sources()],
        cfg["input_file"],cfg["review_file"],"data/pmcvqa_clean_native/input_contracts.jsonl"]
    if any(n not in cfg["frozen_files_sha256"] for n in mandatory):raise ValueError("Missing mandatory pre-inference source/input hash")
    deferred=[]
    for name,expected in cfg["frozen_files_sha256"].items():
        if (ROOT/name).resolve()==reference_path.resolve():deferred.append(expected)
        elif protocol.file_sha(ROOT/name)!=expected:raise ValueError("Frozen source/input changed: "+name)
    cases=[json.loads(s) for s in (ROOT/cfg["input_file"]).read_text().splitlines() if s]
    if not cases or manifest["planned_cases"]!=len(cases) or manifest["case_contract_sha256"]!=protocol.digest(cases):raise ValueError("Frozen planned case contract changed")
    review=json.loads((ROOT/cfg["review_file"]).read_text());ids=[c["case_id"] for c in cases]
    if review.get("reviewed") is not True or ids!=review["approved_case_ids"] or len(set(ids))!=len(ids) or review.get("held_cases"):raise ValueError("Exact whole-task review changed")
    contracts=[json.loads(s) for s in (ROOT/"data/pmcvqa_clean_native/input_contracts.jsonl").read_text().splitlines() if s]
    by_id={r["case_id"]:r for r in contracts}
    for case in cases:
        expected_payload(case,cfg)
        if case["messages"][0]["content"][0]["text"]!=by_id[case["case_id"]]["prompt"]:raise ValueError("Model question/choices differ from source TD formatting")
    output_lock=lock_outputs(folder,cases)
    raw_refs=reference_path.read_bytes();reference_sha=hashlib.sha256(raw_refs).hexdigest()
    if reference_sha!=cfg["scorer_reference_sha256"] or any(reference_sha!=h for h in deferred):raise ValueError("Scorer-only reference hash changed")
    # The original CSV contains gold; hash it only after every prediction is locked.
    if cfg.get("source_csv_file") and protocol.file_sha(ROOT/cfg["source_csv_file"])!=cfg["source_csv_sha256"]:raise ValueError("Source gold CSV changed")
    references={}
    for ref in map(json.loads,raw_refs.decode().splitlines()):
        if ref["case_id"] in references or ref["task"]!="V05":raise ValueError("Duplicate/wrong source reference")
        if protocol.native_scorer()(ref["native_choices"],ref["target_answer"])!=ref["native_target_index"]:raise ValueError("Native source target mapping differs")
        references[ref["case_id"]]=ref
    rows=[];statuses=Counter();finishes=Counter();usage=Counter();requests=responses=0
    for case in cases:
        identity=protocol.digest([case["task"],case["variant"],case["case_id"]])+".json"
        request=locked_record(folder,"requests/"+identity,output_lock);response=locked_record(folder,"responses/"+identity,output_lock)
        payload=expected_payload(case,cfg);images=validate_content(case["messages"][0]["content"]);requests+=request is not None;responses+=response is not None
        if request is not None:
            if request["request_sha256"]!=protocol.digest(payload) or protocol.digest(request["payload"])!=request["request_sha256"] or request.get("supplied_fields")!=cfg["model_facing_fields"] or request.get("image_sha256")!=[r["sha256"] for r in images]:raise ValueError("Raw request differs from original prompt/image/generation")
            if any(request.get(k)!=case[k] for k in ["task","case_id","variant","split"]):raise ValueError("Raw request identity mismatch")
        if response is not None:
            if request is None:raise ValueError("Response without archived request")
            values={**{k:case[k] for k in ["task","case_id","variant","split"]},"model":cfg["model"],"model_revision":cfg["model_revision"],"request_sha256":request["request_sha256"]}
            if any(response.get(k)!=v for k,v in values.items()):raise ValueError("Response provenance mismatch")
        status=response.get("status") if response else ("interrupted_unknown_completion" if request else "not_dispatched")
        statuses[status]+=1;completed=status=="completed";text=None;finish=response.get("finish_reason") if response else None
        if completed:
            api=response["response"];choices=api.get("choices",[])
            if response.get("http_status")!=200 or api.get("model")!=cfg["model"] or len(choices)!=1:raise ValueError("Completed output violates one local completion contract")
            choice=choices[0]
            if response.get("text")!=(choice.get("message",{}).get("content") or "") or finish!=choice.get("finish_reason"):raise ValueError("Saved final text/finish differs from raw response")
            text=response["text"];finishes[str(finish)]+=1
            for k in ["prompt_tokens","completion_tokens","total_tokens"]:usage[k]+=api.get("usage",{}).get(k,0) or 0
        ref=references[case["case_id"]]
        if ref["variant"]!=case["variant"] or ref["split"]!=case["split"] or ref["image_sha256"]!=images[0]["sha256"]:raise ValueError("Reference input/image identity mismatch")
        predictions=protocol.score_text(text,ref,completed)
        rows.append({"task":"V05","case_id":case["case_id"],"status":status,"completed":completed,
            "parsed":bool(completed and isinstance(text,str) and text.strip()),"raw_text":text,"parsed_predictions":predictions,
            "native_target_index":ref["native_target_index"],"target_label":ref["target_label"],"target_answer":ref["target_answer"],
            "native_target_agrees_with_released_label":ref["native_target_agrees_with_released_label"],
            "finish_reason":finish,"truncated":completed and finish=="length","request_sha256":request["request_sha256"] if request else None})
    completed=sum(r["completed"] for r in rows);full_inputs=ids==[r["case_id"] for r in contracts] and len(ids)==2000
    metrics=protocol.metric_summary(rows)
    summary={"run_id":cfg["run_id"],"task_id":"V05","model":cfg["model"],"model_revision":cfg["model_revision"],"protocol_variant":protocol.VARIANT,
        "planned":len(cases),"completed":completed,"parsed":sum(r["parsed"] for r in rows),"requests_saved":requests,"responses_saved":responses,
        "invalid_outputs":sum(r["completed"] and not r["parsed"] for r in rows),"missing_or_failed_outputs":len(rows)-completed,
        "truncated_outputs":sum(r["truncated"] for r in rows),"statuses":dict(statuses),"finish_reasons":dict(finishes),"token_usage":dict(usage),
        "case_scope":"full_native_clean2000" if full_inputs and completed==2000 else "INCOMPLETE_frozen_clean2000_case_set",
        "full_native_test_inputs":full_inputs,"native_full_test_case_count":2000,"metrics":metrics,
        "primary_metric":"native_td_final_character_accuracy","metric_units":"fraction_0_1","input_modalities":["image","question_all_choices_text"],
        "native_target_vs_released_label_mismatches":sum(not r["native_target_agrees_with_released_label"] for r in rows),
        "native_undefined_mapping_count":sum(not r["parsed_predictions"]["native_score_defined"] for r in rows),
        "full_text_undefined_mapping_count":sum(not r["parsed_predictions"]["full_text_score_defined"] for r in rows),
        "strict_final_label_parsed_count":sum(r["parsed_predictions"]["strict_final_label"] is not None for r in rows),
        "scoring_output_lock_sha256":output_lock["contract_sha256"],"predictions_locked_before_reference_read":True,"request_response_hash_audit":"passed",
        "explanation_support_score":None,"publisher_full_archive_sha256_verified":False,
        "metric_implementation":"AST-extracted original TD difflib.SequenceMatcher functions unchanged; native final-character and separate full-text adaptation/strict label diagnostics. No lowercasing or label-assisted parsing.",
        "comparison_to_paper":cfg["paper_comparison"],"failure_policy":"All frozen cases in each denominator. Missing/failed/empty outputs score0; no retries, reference-derived fill or selection. Truncated raw content retained/scored and disclosed.",
        "interpretation":{"likely_demands":{"labels":["visual_evidence_interpretation","medical_knowledge","multiple_choice_question_answering"],"status":"provisional analyst description, not internal-computation evidence"},"actually_supplied":"Exact source TD Question/all four choices prompt and original JPEG bytes; no caption, answer or answer-label field","reference_answer_source":"Pinned clean2000 Answer mapped through native choices, plus separate released Answer_label diagnostic","good_score_establishes":"Recovery of reference choices under this declared vision/output extraction/scoring system","bad_score_establishes":"Limited choice recovery; does not isolate reasoning or establish clinical competence","explanation_correctness":"Unassessed separately from answers; absent support is not automatic falsity"},
        "contamination":"Solver receives no gold labels, training, retrieval or test-feedback prompt changes. Public pretraining exposure unknown."}
    protocol.save_json(folder/"per_case_scores.json",rows);protocol.save_json(folder/"scores.json",summary)
    with (folder/"metrics.csv").open("w",newline="") as handle:
        writer=csv.DictWriter(handle,fieldnames=["run_id","task_id","protocol_variant","metric","value","planned","completed","case_scope"]);writer.writeheader()
        for name,value in metrics.items():writer.writerow({**{k:summary[k] for k in ["run_id","task_id","protocol_variant","planned","completed","case_scope"]},"metric":name,"value":value})
    print(json.dumps(summary,ensure_ascii=False));return summary


if __name__=="__main__":
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument("--run",required=True);args=parser.parse_args();score(ROOT/"results/runs"/args.run)
