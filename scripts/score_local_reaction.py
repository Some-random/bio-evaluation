"""Offline fixed384-class native Reaction accuracy; lock outputs before labels."""
import argparse
from collections import Counter
import csv
import hashlib
import json
import math
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
TASKS = {"P16"}
from prepare_catalog_reaction import parse_class_id, accuracy


def digest(value):
    return hashlib.sha256(json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def file_digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write_json(path, value):
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n")
    temporary.chmod(0o600)
    temporary.replace(path)


def outcome_metrics(task, targets, texts):
    if task != "P16":
        raise ValueError("Require frozen native Reaction task")
    return accuracy(targets, texts)


def expected_payload(case, settings):
    if set(case) != {"task", "case_id", "variant", "split", "messages"}:
        raise ValueError("Unexpected case fields")
    if case["task"] not in settings["approved_task_ids"] or case["variant"] != settings["variant"]:
        raise ValueError("Case outside frozen scope")
    if len(case["messages"]) != 1 or set(case["messages"][0]) != {"role", "content"}:
        raise ValueError("Require one original user string")
    message = case["messages"][0]
    if message["role"] != "user" or not isinstance(message["content"], str):
        raise ValueError("Unexpected message modality")
    return {"model": settings["model"], "messages": case["messages"], **settings["generation"]}


def output_lock(folder, cases):
    files = {"run_manifest.json": file_digest(folder / "run_manifest.json")}
    for case in cases:
        identity = digest([case["task"], case["variant"], case["case_id"]])
        for category in ["requests", "responses"]:
            name = category + "/" + identity + ".json"
            path = folder / name
            files[name] = file_digest(path) if path.exists() else None
    record = {"files_sha256": files, "contract_sha256": digest(files),
              "policy": "All raw outputs/missing slots locked before reference loading; no gold-based replacement, selection or completion retries."}
    path = folder / "scoring_output_lock.json"
    if path.exists() and json.loads(path.read_text()) != record:
        raise ValueError("Pre-scoring output lock changed")
    if not path.exists():
        write_json(path, record)
    return record


def score(folder):
    manifest = json.loads((folder / "run_manifest.json").read_text())
    settings = manifest["configuration"]
    if len(settings["approved_task_ids"]) != 1 or settings["approved_task_ids"][0] not in TASKS:
        raise ValueError("Require one supported frozen task")
    task = settings["approved_task_ids"][0]
    for name, expected in settings["frozen_files_sha256"].items():
        if file_digest(ROOT / name) != expected:
            raise ValueError("Frozen file changed: " + name)
    cases = [json.loads(s) for s in (ROOT / settings["input_file"]).read_text().splitlines() if s]
    if digest(cases) != manifest["case_contract_sha256"]:
        raise ValueError("Frozen input contract changed")
    review = json.loads((ROOT / settings["review_file"]).read_text())
    case_ids = [r["case_id"] for r in cases]
    if case_ids != review["approved_case_ids"] or len(set(case_ids)) != len(case_ids):
        raise ValueError("Cases differ from exact ordered allowlist")
    if set(case_ids) & {c["case_id"] for c in review.get("held_cases", [])}:
        raise ValueError("Held case found in execution set")
    lock = output_lock(folder, cases)
    reference_path = ROOT / settings["scorer_reference_file"]
    if file_digest(reference_path) != settings["scorer_reference_sha256"]:
        raise ValueError("Scorer reference changed from pre-inference hash")
    references = {}
    for ref in map(json.loads, reference_path.read_text().splitlines()):
        key = (ref["task"], ref["case_id"])
        if key in references:
            raise ValueError("Duplicate reference identity")
        references[key] = ref
    states, finishes, usage = Counter(), Counter(), Counter()
    scored, requests = [], 0
    for case in cases:
        identity = digest([case["task"], case["variant"], case["case_id"]])
        request_path = folder / "requests" / (identity + ".json")
        response_path = folder / "responses" / (identity + ".json")
        payload = expected_payload(case, settings)
        request = json.loads(request_path.read_text()) if request_path.exists() else None
        response = json.loads(response_path.read_text()) if response_path.exists() else None
        requests += int(request is not None)
        if request is not None and (digest(request["payload"]) != request["request_sha256"] or request["request_sha256"] != digest(payload)):
            raise ValueError("Archived payload differs from frozen input")
        if response is not None:
            if request is None:
                raise ValueError("Response missing its request")
            for key, value in [("task", task), ("case_id", case["case_id"]), ("variant", settings["variant"]),
                               ("model", settings["model"]), ("model_revision", settings["model_revision"]),
                               ("request_sha256", request["request_sha256"])]:
                if response.get(key) != value:
                    raise ValueError("Response provenance mismatch: " + key)
        status = response.get("status") if response else ("interrupted_unknown_completion" if request else "not_dispatched")
        states[status] += 1
        completed = status == "completed"
        text = response.get("text", "") if completed else None
        prediction = parse_class_id(text)
        ref = references[(task, case["case_id"])]
        if completed:
            finishes[str(response.get("finish_reason"))] += 1
            for key in ["prompt_tokens", "completion_tokens", "total_tokens"]:
                usage[key] += response.get("response", {}).get("usage", {}).get(key, 0) or 0
        scored.append({"task": task, "case_id": case["case_id"], "status": status, "completed": completed,
                       "raw_text": text, "prediction": prediction, "target": ref["target"], "parsed": prediction is not None,
                       "correct": prediction is not None and prediction == ref["target"],
                       "finish_reason": response.get("finish_reason") if response else None,
                       "request_sha256": request["request_sha256"] if request else None})
    metrics = outcome_metrics(task, [r["target"] for r in scored], [r["raw_text"] for r in scored])
    completed = sum(r["completed"] for r in scored)
    scope = "full_frozen_reviewed_ProtST_Reaction_test" if completed == len(cases) else "INCOMPLETE_frozen_reviewed_ProtST_Reaction_test"
    summary = {"run_id": settings["run_id"], "task_id": task, "model": settings["model"],
               "model_revision": settings["model_revision"], "protocol_variant": settings["variant"],
               "planned": len(cases), "requests_saved": requests, "completed": completed, "parsed": metrics["parsed"],
               "invalid_outputs": metrics["invalid"], "missing_or_failed_outputs": sum(not r["completed"] for r in scored),
               "statuses": dict(states), "finish_reasons": dict(finishes), "token_usage": dict(usage), "metrics": metrics,
               "input_modalities": ["amino_acid_sequence", "text"], "scoring_output_lock_sha256": lock["contract_sha256"],
               "case_scope": scope, "held_before_inference": len(review.get("held_cases", [])), "explanation_support_score": None,
               "comparison_to_paper": "Native released Reaction test and384-class top1 accuracy; prompted Qwen has different representation/context/pretraining from ProtST. Closest native full-description comparator21.91% accuracy, ProtST Table11 printedp15 (rounded); paper pretraining-name29.85% is a separate label-text variant. Native text embeddings truncate each description at128tokens; Qwen receives all complete descriptions jointly.",
               "interpretation": {"likely_demands": {"labels": ["biological_outcome_prediction", "sequence_representation"], "status": "provisional analyst description; internal computation unknown"},
                                  "actually_supplied": "Archived full original amino-acid sequence, fixed classification objective and all384 complete source pretraining-template descriptions, including alternative names/comments. No per-protein target label, retrieval, tools or fewshot examples.",
                                  "reference_answer_source": "Pinned native EC-derived Reaction integer class0..383 from original held-out LMDB; fixed global ontology constructed from official public class tables independently of test labels. Reference file hashed before inference and opened after output lock.",
                                  "good_score_establishes": "Recovery of source outcomes on the declared released test under the fixed zero-shot protocol.",
                                  "bad_score_establishes": "Limited outcome recovery for this input/regime; does not independently establish deficient general reasoning.",
                                  "explanation_correctness": "Unassessed; correct prediction does not certify rationale and unsupported mechanism is not automatically false."},
               "contamination": "Reference labels excluded, inputs frozen, outputs hash-locked before scoring, no training or test-guided changes. Prior exposure to public source data unknown."}
    write_json(folder / "scores.json", summary)
    write_json(folder / "per_case_scores.json", scored)
    with (folder / "metrics.csv").open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["run_id", "task_id", "protocol_variant", "model", "metric", "value", "planned", "completed", "parsed", "case_scope"])
        writer.writeheader()
        for name in ["accuracy"]:
            writer.writerow({"run_id": settings["run_id"], "task_id": task, "protocol_variant": settings["variant"], "model": settings["model"],
                             "metric": name, "value": metrics[name], "planned": len(cases), "completed": completed,
                             "parsed": metrics["parsed"], "case_scope": scope})
    print(json.dumps(summary, ensure_ascii=False))
    return summary


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--run", required=True)
    args = parser.parse_args()
    score(ROOT / "results/runs" / args.run)
