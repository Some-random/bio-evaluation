"""Freeze reviewed benign property-prediction baselines with original test rows."""
import argparse
import datetime as dt
import json
from pathlib import Path

from run_local_labbench import ROOT, file_digest, write_json

TASKS = {"P01", "P02", "P06", "P10", "P11"}


def prepare(task, gpu):
    if task not in TASKS or gpu not in {4, 6, 7}:
        raise ValueError("Unknown reviewed task/replica")
    source = ROOT / "data/catalog_sequence_tasks" / task / "model_inputs.jsonl"
    rows = [json.loads(s) for s in source.read_text().splitlines()]
    if not rows or any(r["task"] != task or r["system"] for r in rows):
        raise ValueError("Input task/system differs from reviewed contract")
    if len({r["case_id"] for r in rows}) != len(rows) or len({r["variant"] for r in rows}) != 1:
        raise ValueError("Duplicate IDs or mixed protocols")
    for row in rows:
        if file_digest_value(row["prompt"].encode()) != row["prompt_sha256"]:
            raise ValueError("Prepared prompt changed")
        for name, value in row["fields"].items():
            if name.startswith("Protein") or name == "sequence":
                if not value or any(not ("A" <= letter <= "Z") for letter in value) or value not in row["prompt"]:
                    raise ValueError("Complete input sequence was not retained")
    review_path = ROOT / f"configs/local_catalog_{task.lower()}_review.json"
    review = {"task_id": task, "input_review_only": True,
              "reviewed_at_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
              "source_input_path": str(source.relative_to(ROOT)), "source_input_sha256": file_digest(source),
              "basis": "All input records validated against the fixed full-sequence property-prediction contract. Fixed task definition and source context reviewed; no test labels or model outcomes used to select cases. No claim of per-residue manual inspection.",
              "scope": "Generic solubility/membrane association, human/yeast interactions, or human-cell thermal property prediction. No mutation proposals, pathogen phenotype optimization, or operational protocols.",
              "approved_case_ids": [r["case_id"] for r in rows], "held_cases": [],
              "approved_cases": len(rows), "full_public_cases": len(rows), "selection_based_on_model_outputs": False,
              "provisional_task_demands": ["learned biological outcome prediction", "sequence representation"],
              "classification_is_provisional": True, "flagged_requests_transferred": False}
    if review_path.exists():
        raise ValueError("Review already frozen")
    write_json(review_path, review)
    target = ROOT / "data/local_catalog_suite" / task / "model_inputs.jsonl"
    if target.exists():
        raise ValueError("Execution inputs already frozen")
    target.parent.mkdir(parents=True, exist_ok=True)
    cases = [{"task": task, "case_id": r["case_id"], "variant": r["variant"], "split": r["split"],
              "messages": [{"role": "user", "content": r["prompt"]}]} for r in rows]
    target.write_text("".join(json.dumps(c, ensure_ascii=False) + "\n" for c in cases))
    local = json.loads((ROOT / "configs/local_model.json").read_text())
    if task not in local["approved_task_ids"]:
        raise ValueError("Task authorization not recorded")
    serving_path = ROOT / f"configs/local_model_gpu{gpu}.json"
    serving = json.loads(serving_path.read_text())
    settings = json.loads((ROOT / "configs/local_labbench_b07.json").read_text())
    settings.update(run_id=f"qwen38_27b_{task.lower()}_original_test_2026-10-15",
                    frozen_at_utc=dt.datetime.now(dt.timezone.utc).isoformat(),
                    approved_task_ids=[task], variant=rows[0]["variant"],
                    input_file=str(target.relative_to(ROOT)), review_file=str(review_path.relative_to(ROOT)),
                    runner="scripts/run_local_labbench_multimodal.py",
                    serving_config_file=str(serving_path.relative_to(ROOT)),
                    server_record_file=f".local/local_model_server_gpu{gpu}.json", gpu_ids=[gpu],
                    endpoint=f"http://127.0.0.1:{serving['port']}/v1",
                    scorer_reference_file=f"data/catalog_sequence_tasks/{task}/scorer_references.jsonl",
                    model_facing_fields=sorted(rows[0]["fields"]), input_modalities=["amino_acid_sequence", "task_instruction"],
                    paper_comparison="Verified original test rows and native task metric; prompted zero-shot full-sequence Qwen adaptation versus trained specialist/multitask systems. Same labels/split do not imply matched training or information resources.")
    settings.pop("source_code_revision", None)
    settings["source_dataset_revision"] = ("d5c35cc716ca93c3c74a0b43eef5b60cbf88521f" if task == "P06"
                                            else "9f70da9e8f0df32e7e62846f7ad78a829b00c0fd")
    settings["prompt_policy"] = "Pinned source task definition and complete decoded sequence(s); fixed zero-shot user prompt. Numeric assay objective and units fixed before inference. No LAB-Bench prompt or choice template is used."
    settings["metric_policy"] = "Native task accuracy for categorical outcomes; native Spearman for the numerical assay split. Invalid/missing outputs remain explicit; no label-dependent repairs or invented numerical replacements."
    settings["scorer_reference_sha256"] = file_digest(ROOT / settings["scorer_reference_file"])
    files = [str(source.relative_to(ROOT)), settings["input_file"], settings["review_file"],
             settings["runner"], "scripts/score_local_catalog_tasks.py", "scripts/catalog_metric_helpers.py",
             "scripts/prepare_local_catalog_run.py", "scripts/execute_local_catalog.py",
             "reports/catalog_split_identity_2026-10-15.json"]
    settings["frozen_files_sha256"] = {f: file_digest(ROOT / f) for f in sorted(set(files))}
    path = ROOT / f"configs/local_catalog_{task.lower()}.json"
    if path.exists():
        raise ValueError("Run config already frozen")
    write_json(path, settings)
    print(json.dumps({"task": task, "cases": len(cases), "gpu": gpu, "config": str(path.relative_to(ROOT))}))


def file_digest_value(raw):
    import hashlib
    return hashlib.sha256(raw).hexdigest()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--task", required=True)
    parser.add_argument("--gpu", required=True, type=int)
    args = parser.parse_args()
    prepare(args.task, args.gpu)
