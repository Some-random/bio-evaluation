"""Offline AUROC/AP from frozen raw two-label conditional likelihoods."""
import argparse
from collections import Counter
import csv
import importlib.metadata
import json
import math

from local_dti_common import (ROOT, MODEL, REVISION, digest, extract_score, file_digest, payload_for, write_json)


def binary_metrics(targets, scores):
    from sklearn.metrics import average_precision_score, roc_auc_score
    if not targets or len(targets) != len(scores) or any(t not in {0, 1} for t in targets):
        raise ValueError("Require matching native binary labels and continuous score slots")
    if any(not isinstance(s, (float, int)) or not math.isfinite(s) or not 0 <= s <= 1 for s in scores):
        raise ValueError("Require finite continuous positive-label scores")
    if len(set(targets)) != 2:
        return {"auroc": None, "auprc": None, "undefined_single_class": True}
    return {"auroc": float(roc_auc_score(targets, scores)),
            "auprc": float(average_precision_score(targets, scores)), "undefined_single_class": False}


def lock_outputs(folder, cases):
    files = {"run_manifest.json": file_digest(folder / "run_manifest.json")}
    for case in cases:
        identity = digest([case["task"], case["variant"], case["case_id"]])
        for category in ["requests", "responses"]:
            name = category + "/" + identity + ".json"
            path = folder / name
            files[name] = file_digest(path) if path.exists() else None
    record = {"files_sha256": files, "contract_sha256": digest(files),
              "policy": "Raw requests/responses and missing slots locked before scorer labels; no score selection, repair or missing-score fill"}
    path = folder / "scoring_output_lock.json"
    if path.exists() and json.loads(path.read_text()) != record:
        raise ValueError("Pre-scoring output lock changed")
    if not path.exists():
        write_json(path, record)
    return record


def score(folder):
    manifest = json.loads((folder / "run_manifest.json").read_text())
    settings = manifest["configuration"]
    for name, expected in settings["frozen_files_sha256"].items():
        if file_digest(ROOT / name) != expected:
            raise ValueError("Frozen file changed: " + name)
    cases = [json.loads(s) for s in (ROOT / settings["input_file"]).read_text().splitlines() if s]
    if not cases or digest(cases) != manifest["case_contract_sha256"]:
        raise ValueError("Frozen case contract changed")
    review = json.loads((ROOT / settings["review_file"]).read_text())
    ids = [c["case_id"] for c in cases]
    if not review.get("reviewed") or review["dataset"] != settings["dataset"] or ids != review["approved_case_ids"] or len(set(ids)) != len(ids):
        raise ValueError("Cases differ from ordered reviewed dataset")
    if set(ids) & {r["case_id"] for r in review.get("held_cases", [])}:
        raise ValueError("Held case found")
    output_lock = lock_outputs(folder, cases)
    ref_path = ROOT / settings["scorer_reference_file"]
    if file_digest(ref_path) != settings["scorer_reference_sha256"]:
        raise ValueError("Reference file differs from pre-inference hash")
    references = {}
    for ref in map(json.loads, ref_path.read_text().splitlines()):
        if ref["task"] != "P43":
            raise ValueError("Unexpected source task")
        if ref["case_id"] in references:
            raise ValueError("Duplicate reference identity")
        references[ref["case_id"]] = ref
    states, finishes, usage = Counter(), Counter(), Counter()
    scored, request_count = [], 0
    for case in cases:
        identity = digest([case["task"], case["variant"], case["case_id"]])
        req_path, res_path = [folder / group / (identity + ".json") for group in ["requests", "responses"]]
        request = json.loads(req_path.read_text()) if req_path.exists() else None
        response = json.loads(res_path.read_text()) if res_path.exists() else None
        payload = payload_for(case, settings)
        request_count += int(request is not None)
        if request is not None and (digest(request["payload"]) != request["request_sha256"] or request["request_sha256"] != digest(payload)):
            raise ValueError("Archived payload differs from exact score protocol")
        if response is not None:
            if request is None:
                raise ValueError("Response missing its request")
            for name, value in [("task", "P43"), ("case_id", case["case_id"]), ("variant", case["variant"]),
                                ("model", MODEL), ("model_revision", REVISION), ("request_sha256", request["request_sha256"])]:
                if response.get(name) != value:
                    raise ValueError("Response provenance mismatch: " + name)
        status = response.get("status") if response else ("interrupted_unknown_completion" if request else "not_dispatched")
        states[status] += 1
        completed = status == "completed"
        values = extract_score(response["response"]) if completed else None
        if completed and values != response["score"]:
            raise ValueError("Saved derived score disagrees with raw token likelihoods")
        ref = references[case["case_id"]]
        if ref["dataset"] != settings["dataset"]:
            raise ValueError("Reference belongs to another dataset; do not pool scores")
        if completed:
            finishes[str(response.get("finish_reason"))] += 1
            for key in ["prompt_tokens", "completion_tokens", "total_tokens"]:
                usage[key] += response.get("response", {}).get("usage", {}).get(key, 0) or 0
        scored.append({"task": "P43", "case_id": case["case_id"], "dataset": settings["dataset"], "status": status,
                       "completed": completed, "target": ref["target_binary"], "positive_score": values["positive_score"] if values else None,
                       "token_likelihoods": values, "raw_sampled_label": response.get("text") if response else None,
                       "request_sha256": request["request_sha256"] if request else None})
    valid = [r for r in scored if r["completed"]]
    complete = len(valid) == len(cases)
    result = binary_metrics([r["target"] for r in valid], [r["positive_score"] for r in valid]) if valid else None
    metrics = {key: result[key] if complete else None for key in ["auroc", "auprc"]}
    if not complete:
        metrics.update({key + "_completed_only": result[key] if result else None for key in ["auroc", "auprc"]})
    summary = {"run_id": settings["run_id"], "task_id": "P43", "dataset": settings["dataset"], "model": MODEL, "model_revision": REVISION,
               "protocol_variant": settings["variant"], "planned": len(cases), "requests_saved": request_count,
               "completed": len(valid), "parsed": len(valid), "invalid_outputs": states["invalid_likelihood_output"],
               "missing_or_failed_outputs": len(cases) - len(valid), "statuses": dict(states), "finish_reasons": dict(finishes),
               "token_usage": dict(usage), "metrics": metrics, "undefined_single_class": result["undefined_single_class"] if result else None,
               "case_scope": "full_frozen_reviewed_dataset" if complete else "INCOMPLETE_completed_only_not_full_test",
               "held_before_inference": len(review.get("held_cases", [])), "input_modalities": ["SELFIES", "amino_acid_sequence", "text"],
               "scoring_output_lock_sha256": output_lock["contract_sha256"], "metric_implementation": {"auroc": "sklearn.metrics.roc_auc_score", "auprc": "sklearn.metrics.average_precision_score (noninterpolated AP)", "scikit_learn_version": importlib.metadata.version("scikit-learn")},
               "comparison_to_paper": "Original released dataset and standard AUROC/AP; fixed first-token Qwen likelihood adapter differs from trained DrugBAN/BioT5 architectures and BioT5 raw-score ratio. No test threshold fitting or exact paper reproduction claim.",
               "explanation_support_score": None,
               "interpretation": {"likely_demands": {"labels": ["drug_target_interaction_prediction", "learned_chemical_and_protein_representation"], "status": "provisional analyst description; internal computation not inferred"},
                  "actually_supplied": "Original source definition, complete source SELFIES and full protein sequence. Fixed Yes/No output vocabulary; no measured labels, tools or extra chemical context.",
                  "reference_answer_source": "Pinned source interaction/affinity-derived binary labels, scorer-only",
                  "good_score_establishes": "Ranking agreement with source interaction labels under this fixed zero-shot scoring system",
                  "bad_score_establishes": "Limited interaction-label ranking for the declared input/regime; does not isolate reasoning or representation failure",
                  "unsupported_claims": "No physical binding affinity, clinical efficacy, verified mechanism, explanation correctness or contamination-free claim follows."}}
    write_json(folder / "scores.json", summary);write_json(folder / "per_case_scores.json", scored)
    with (folder / "metrics.csv").open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["run_id", "task_id", "dataset", "protocol_variant", "model", "metric", "value", "planned", "completed", "parsed", "case_scope"])
        writer.writeheader()
        for name, value in metrics.items():
            writer.writerow({"run_id": settings["run_id"], "task_id": "P43", "dataset": settings["dataset"], "protocol_variant": settings["variant"], "model": MODEL,
                             "metric": name, "value": value, "planned": len(cases), "completed": len(valid), "parsed": len(valid), "case_scope": summary["case_scope"]})
    print(json.dumps(summary));return summary


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--run", required=True)
    args = parser.parse_args()
    score(ROOT / "results/runs" / args.run)
