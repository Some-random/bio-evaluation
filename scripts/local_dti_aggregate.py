"""Offline P43 completion watch: validate all three tests without pooling scores."""
import argparse
from collections import Counter
import datetime as dt
import fcntl
import json
import os
from pathlib import Path
import shutil
import time

from local_dti_common import ROOT, MODEL, REVISION, VARIANT, GENERATION, digest, extract_score, file_digest, payload_for, write_json
from local_dti_score import binary_metrics

RUN_ID = "qwen38_27b_p43_all_native_tests_2026-10-15"
SOURCE_INPUT = "data/catalog_sequence_tasks/P43/model_inputs.jsonl"
COUNTS = {"human": 1200, "biosnap": 5493, "bindingdb": 9840}
CONFIGS = {"human": "606206a59af611e3cd0203f6e3774f208e1408b2f5356cf637b32f4dae7926c7",
           "biosnap": "ed5caf9c4e50be5252408f2c0e2fb1bdaf1d0a6cc91a5c3742a07b0a398eba54",
           "bindingdb": "3b4f54100ab5a4ef8934ffebdf51b3ec786e524fdb3a3e98717e4b4a67122b73"}
RUNNER = "scripts/local_dti_run.py"


class Pending(Exception):
    pass


def ordered_union(original, groups):
    expected = [row["case_id"] for row in original]
    observed = [row["case_id"] for row in groups]
    if len(expected) != len(set(expected)) or len(observed) != len(set(observed)) or expected != observed:
        raise ValueError("Three-dataset union differs from the exact original ordered case IDs")
    return {"complete": True, "union_matches_full_test_ids": True, "expected_test_case_count": len(expected),
            "unique_observed_case_count": len(set(observed)), "missing_case_count": 0, "extra_case_count": 0}


def configurations():
    result = {}
    for dataset, expected in CONFIGS.items():
        path = ROOT / f"configs/local_dti_{dataset}.json"
        if file_digest(path) != expected:
            raise ValueError("Final reviewed config changed: " + dataset)
        cfg = json.loads(path.read_text())
        if (cfg["dataset"] != dataset or cfg["approved_task_ids"] != ["P43"] or cfg["model"] != MODEL
                or cfg["model_revision"] != REVISION or cfg["generation"] != GENERATION or cfg["variant"] != VARIANT
                or cfg.get("execution_authorized") is not True):
            raise ValueError("Final config task/model/variant/score recipe mismatch")
        result[dataset] = cfg
    return result


def validate_dataset(dataset, cfg, original, references):
    for name, expected in cfg["frozen_files_sha256"].items():
        if file_digest(ROOT / name) != expected:
            raise ValueError("Frozen source changed: " + name)
    cases = [json.loads(s) for s in (ROOT / cfg["input_file"]).read_text().splitlines() if s]
    source = [r for r in original if r["dataset"] == dataset]
    expected_cases = [{"task": "P43", "case_id": r["case_id"], "variant": VARIANT,
                       "split": "official_BioT5_export_" + dataset + "_test",
                       "messages": [{"role": "user", "content": r["prompt"]}]} for r in source]
    if len(cases) != COUNTS[dataset] or cases != expected_cases:
        raise ValueError("Dataset differs from every original ordered test input")
    review = json.loads((ROOT / cfg["review_file"]).read_text())
    if (review.get("reviewed") is not True or review["dataset"] != dataset or review["held_cases"]
            or review["approved_case_ids"] != [c["case_id"] for c in cases]):
        raise ValueError("Native full-test review/ordered case list changed")
    folder = ROOT / "results/runs" / cfg["run_id"]
    done = json.loads((folder / "completion.json").read_text())
    manifest = json.loads((folder / "run_manifest.json").read_text())
    scores = json.loads((folder / "scores.json").read_text())
    if (manifest["configuration"] != cfg or manifest["configuration_sha256"] != CONFIGS[dataset]
            or manifest["case_contract_sha256"] != digest(cases) or manifest["planned_cases"] != len(cases)
            or manifest["runner_sha256"] != cfg["frozen_files_sha256"][RUNNER]
            or manifest.get("solver_tools") != [] or manifest.get("answer_keys_available_to_solver") is not False
            or manifest.get("model_selection_on_test") is not False):
        raise ValueError("Historical run manifest differs from frozen protocol")
    server = manifest["server"]
    if (server["model"] != MODEL or server["revision"] != REVISION or server["gpu_ids"] != cfg["gpu_ids"]
            or not server.get("pid") or not server.get("proc_start_ticks")
            or cfg["endpoint"] != f"http://127.0.0.1:{server.get('port',8026)}/v1"):
        raise ValueError("Historical exact local server identity mismatch")
    expected_names = {digest(["P43", VARIANT, c["case_id"]]) + ".json" for c in cases}
    for kind in ["requests", "responses"]:
        if {p.name for p in (folder / kind).glob("*.json")} != expected_names:
            raise ValueError("Missing/extra raw output slots: " + dataset)
    per_case = json.loads((folder / "per_case_scores.json").read_text())
    if [r["case_id"] for r in per_case] != [c["case_id"] for c in cases]:
        raise ValueError("Scored case identity/order mismatch")
    raw_hashes = {"run_manifest.json": file_digest(folder / "run_manifest.json")}
    targets, predictions = [], []
    for case, scored in zip(cases, per_case):
        identity = digest(["P43", VARIANT, case["case_id"]]) + ".json"
        req_path, res_path = [folder / group / identity for group in ["requests", "responses"]]
        request, response = json.loads(req_path.read_text()), json.loads(res_path.read_text())
        payload = payload_for(case, cfg)
        expected_request = {**{k: case[k] for k in ["task", "case_id", "variant", "split"]},
                            "payload": payload, "request_sha256": digest(payload), "dataset": dataset,
                            "supplied_fields": ["source_definition", "full_SELFIES", "complete_protein_sequence"]}
        if request != expected_request:
            raise ValueError("Raw request differs from exact prompt/channel/recipe")
        for key, expected in {**{k:case[k] for k in ["task","case_id","variant","split"]},
                              "model": MODEL, "model_revision": REVISION, "request_sha256": digest(payload),
                              "status": "completed", "http_status": 200}.items():
            if response.get(key) != expected:
                raise ValueError("Raw response provenance mismatch: " + key)
        values = extract_score(response["response"])
        ref = references[case["case_id"]]
        if (response["score"] != values or response["text"] != values["sampled_label"]
                or ref["dataset"] != dataset or scored.get("target") != ref["target_binary"]
                or scored.get("positive_score") != values["positive_score"] or scored.get("token_likelihoods") != values
                or scored.get("request_sha256") != digest(payload) or scored.get("completed") is not True
                or scored.get("status") != "completed" or scored.get("dataset") != dataset):
            raise ValueError("Derived/scored values differ from frozen raw likelihoods/references")
        targets.append(ref["target_binary"]);predictions.append(values["positive_score"])
        raw_hashes["requests/" + identity] = file_digest(req_path)
        raw_hashes["responses/" + identity] = file_digest(res_path)
    lock = json.loads((folder / "scoring_output_lock.json").read_text())
    if lock["files_sha256"] != raw_hashes or lock["contract_sha256"] != digest(raw_hashes):
        raise ValueError("Source raw-output lock mismatch")
    expected_metric = binary_metrics(targets, predictions)
    if (scores.get("task_id") != "P43" or scores.get("dataset") != dataset or scores.get("model") != MODEL
            or scores.get("model_revision") != REVISION or scores.get("protocol_variant") != VARIANT
            or scores.get("planned") != len(cases) or scores.get("completed") != len(cases) or scores.get("parsed") != len(cases)
            or scores.get("invalid_outputs") != 0 or scores.get("missing_or_failed_outputs") != 0
            or scores.get("scoring_output_lock_sha256") != lock["contract_sha256"]):
        raise ValueError("Dataset summary is incomplete or inconsistent")
    if any(scores["metrics"].get(name) != expected_metric[name] for name in ["auroc", "auprc"]):
        raise ValueError("Dataset metric differs from independent raw-score recomputation")
    evidence = {"dataset": dataset, "run_id": cfg["run_id"], "config_file": f"configs/local_dti_{dataset}.json",
                "config_sha256": CONFIGS[dataset], "cases": len(cases), "server": server, "raw_files_sha256": raw_hashes,
                "files_sha256": {name:file_digest(folder/name) for name in ["completion.json","run_manifest.json","scores.json","per_case_scores.json","metrics.csv","scoring_output_lock.json"]}}
    return cases, scores, evidence


def install(source, target, expected):
    if file_digest(source) != expected:
        raise ValueError("Source changed after validation")
    target.parent.mkdir(parents=True, exist_ok=True)
    if target.exists():
        if file_digest(target) != expected:
            raise ValueError("Existing aggregate raw file changed")
        return
    try:os.link(source, target)
    except OSError:shutil.copyfile(source, target)
    if file_digest(target) != expected:raise ValueError("Aggregate raw copy hash mismatch")


def aggregate():
    configs = configurations()
    pending = []
    for dataset, cfg in configs.items():
        path = ROOT / "results/runs" / cfg["run_id"] / "completion.json"
        if not path.exists():pending.append(dataset);continue
        done = json.loads(path.read_text())
        if done.get("generation_exit_code") != 0 or done.get("scoring_exit_code") != 0:
            raise ValueError("Failed dataset blocks entire P43 task: " + dataset)
    if pending:raise Pending("Datasets pending: " + ", ".join(pending))
    original_path = ROOT / SOURCE_INPUT
    if any(file_digest(original_path) != c["source_input_sha256"] for c in configs.values()):
        raise ValueError("Original full source input hash changed")
    original = [json.loads(s) for s in original_path.read_text().splitlines()]
    if Counter(r["dataset"] for r in original) != COUNTS or len(original) != sum(COUNTS.values()):
        raise ValueError("Original three-test union/count changed")
    ref_paths = {c["scorer_reference_file"] for c in configs.values()}
    ref_hashes = {c["scorer_reference_sha256"] for c in configs.values()}
    if len(ref_paths) != 1 or len(ref_hashes) != 1:raise ValueError("Mixed reference release")
    ref_path = ROOT / next(iter(ref_paths))
    if file_digest(ref_path) != next(iter(ref_hashes)):raise ValueError("Native reference release changed")
    reference_rows = list(map(json.loads,ref_path.read_text().splitlines()))
    references = {r["case_id"]:r for r in reference_rows}
    if len(references) != len(reference_rows):raise ValueError("Duplicate source reference ID")
    groups, summaries, sources = {}, {}, []
    for dataset, cfg in configs.items():
        cases, scores, evidence = validate_dataset(dataset,cfg,original,references)
        groups[dataset] = {r["case_id"]:r for r in cases};summaries[dataset]=scores;sources.append(evidence)
    ordered = [groups[r["dataset"]][r["case_id"]] for r in original]
    union = ordered_union(original,ordered)
    folder = ROOT / "results/runs" / RUN_ID
    folder.mkdir(parents=True,exist_ok=True)
    inputs_path=folder/"case_inputs.json"
    if inputs_path.exists() and json.loads(inputs_path.read_text())!=ordered:raise ValueError("Archived full ordered input cases changed")
    if not inputs_path.exists():write_json(inputs_path,ordered)
    provenance = {"source_input_file":SOURCE_INPUT,"source_input_sha256":file_digest(original_path),"sources":sources,
                  "full_test_id_union_validation":union,"policy":"Three native tests remain separate: no pooled AUROC/AP, no mean of dataset metrics or score replacement."}
    config = {"run_id":RUN_ID,"model":MODEL,"model_revision":REVISION,"generation":GENERATION,"variant":VARIANT,
              "approved_task_ids":["P43"],"aggregate_only":True,"generator_execution_allowed":False,
              "endpoint":"aggregate-only://offline","source_run_ids":[c["run_id"] for c in configs.values()],
              "input_file":str(inputs_path.relative_to(ROOT)),"input_sha256":file_digest(inputs_path),
              "input_modalities":["molecule_SELFIES","amino_acid_sequence","text"],
              "model_facing_fields":["source_definition","full_SELFIES","complete_protein_sequence"]}
    manifest = {"configuration":config,"configuration_sha256":digest(config),"runner_sha256":next(iter(configs.values()))["frozen_files_sha256"][RUNNER],
                "aggregate_builder_sha256":file_digest(Path(__file__)),"case_contract_sha256":digest(ordered),"planned_cases":len(ordered),
                "model_selection_on_test":False,"solver_tools":[],"answer_keys_available_to_solver":False,"aggregate_only":True,
                "source_dataset_provenance_sha256":digest(provenance)}
    for name,value in [("run_manifest.json",manifest),("source_dataset_manifest.json",provenance)]:
        path=folder/name
        if path.exists() and json.loads(path.read_text())!=value:raise ValueError("Aggregate provenance changed; refuse replacement")
        if not path.exists():write_json(path,value)
    done_path=folder/"completion.json"
    if done_path.exists():
        done=json.loads(done_path.read_text())
        for name,field in [("scores.json","scores_sha256"),("run_manifest.json","run_manifest_sha256"),("source_dataset_manifest.json","source_manifest_sha256"),("scoring_output_lock.json","scoring_output_lock_sha256"),("case_inputs.json","case_inputs_sha256")]:
            if file_digest(folder/name)!=done[field]:raise ValueError("Completed aggregate artifact hash changed: "+name)
        if done.get("source_dataset_provenance_sha256")!=digest(provenance) or done.get("scoring_exit_code")!=0:raise ValueError("Aggregate completion contract changed")
        raw_lock=json.loads((folder/"scoring_output_lock.json").read_text())
        if raw_lock.get("contract_sha256")!=digest(raw_lock["files_sha256"]):raise ValueError("Aggregate raw lock contract changed")
        for name,expected in raw_lock["files_sha256"].items():
            if file_digest(folder/name)!=expected:raise ValueError("Completed aggregate raw artifact changed: "+name)
        return done
    raw_hashes={"run_manifest.json":file_digest(folder/"run_manifest.json")}
    for source in sources:
        source_folder=ROOT/"results/runs"/source["run_id"]
        for name,expected in source["raw_files_sha256"].items():
            if name=="run_manifest.json":continue
            install(source_folder/name,folder/name,expected);raw_hashes[name]=expected
    write_json(folder/"scoring_output_lock.json",{"files_sha256":raw_hashes,"contract_sha256":digest(raw_hashes),"source_dataset_provenance_sha256":digest(provenance)})
    metrics={dataset:{name:summaries[dataset]["metrics"][name] for name in ["auroc","auprc"]} for dataset in CONFIGS}
    counts={dataset:summaries[dataset]["planned"] for dataset in CONFIGS}
    summary={"run_id":RUN_ID,"task_id":"P43","model":MODEL,"model_revision":REVISION,"protocol_variant":VARIANT,
             "planned":len(ordered),"completed":len(ordered),"parsed":len(ordered),"invalid_outputs":0,"missing_or_failed_outputs":0,
             "metrics":metrics,"dataset_metrics":metrics,"dataset_case_counts":counts,"source_run_ids":config["source_run_ids"],
             "case_scope":"complete_three_native_tests_separate_metrics","full_test_id_union_validation":union,
             "request_response_hash_audit":"passed","aggregation_policy":provenance["policy"],"explanation_support_score":None,
             "input_modalities":config["input_modalities"],"finish_reasons":dict(sum((Counter(s["finish_reasons"]) for s in summaries.values()),Counter())),
             "interpretation":summaries["human"]["interpretation"],"comparison_to_paper":summaries["human"]["comparison_to_paper"],
             "source_dataset_provenance_sha256":digest(provenance)}
    write_json(folder/"scores.json",summary)
    done={"generation_exit_code":0,"scoring_exit_code":0,"finished_at_utc":dt.datetime.now(dt.timezone.utc).isoformat(),"aggregate_only":True,
          "source_dataset_provenance_sha256":digest(provenance),"full_test_id_union_validation":union,
          "scores_sha256":file_digest(folder/"scores.json"),"run_manifest_sha256":file_digest(folder/"run_manifest.json"),
          "case_inputs_sha256":file_digest(inputs_path),
          "source_manifest_sha256":file_digest(folder/"source_dataset_manifest.json"),"scoring_output_lock_sha256":file_digest(folder/"scoring_output_lock.json")}
    write_json(done_path,done);return done


def watch(continuous=False,poll_seconds=30):
    if not 1<=poll_seconds<=60:raise ValueError("Poll interval must be1-60seconds")
    lock_path=ROOT/".local/local_dti_aggregate.lock";lock_path.parent.mkdir(parents=True,exist_ok=True)
    with lock_path.open("a") as lock:
        fcntl.flock(lock,fcntl.LOCK_EX|fcntl.LOCK_NB)
        while True:
            try:
                result=aggregate();state={"status":"complete","run_id":RUN_ID,"completion":result};code=0
            except Pending as exc:state={"status":"pending","detail":str(exc)};code=2
            except Exception as exc:state={"status":"blocked","detail":str(exc),"inference_dispatched":False};code=1
            write_json(ROOT/"reports/local_dti_aggregation.json",state)
            print(json.dumps(state),flush=True)
            if not continuous or code!=2:return code
            time.sleep(poll_seconds)


if __name__=="__main__":
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument("--watch",action="store_true");parser.add_argument("--poll-seconds",type=int,default=30)
    args=parser.parse_args();raise SystemExit(watch(args.watch,args.poll_seconds))
