"""Offline native LAB-Bench metrics for a frozen local run of any category."""
import argparse
from collections import Counter
import csv
import hashlib
import json
from pathlib import Path

from run_local_labbench import ROOT, digest, file_digest, write_json
from score_results import lab_answer


def metrics_for(rows):
    n = len(rows)
    correct = sum(r["correct"] for r in rows)
    sure = sum(r["sure"] for r in rows)
    return {"accuracy": correct / n if n else None,
            "precision": correct / sure if sure else 0.0,
            "coverage": sure / n if n else None,
            "n_total": n, "n_correct": correct, "n_sure": sure}


def score(folder):
    manifest = json.loads((folder / "run_manifest.json").read_text())
    settings = manifest["configuration"]
    for name, expected in settings["frozen_files_sha256"].items():
        if file_digest(ROOT / name) != expected:
            raise ValueError("Frozen file changed: " + name)
    cases = [json.loads(s) for s in (ROOT / settings["input_file"]).read_text().splitlines() if s]
    if digest(cases) != manifest["case_contract_sha256"]:
        raise ValueError("Input contract changed")
    reference_path = ROOT / settings["scorer_reference_file"]
    if file_digest(reference_path) != settings["scorer_reference_sha256"]:
        raise ValueError("Scorer reference checksum changed")
    # Lock all existing output hashes before reading any answer labels.
    lock = {p.name: file_digest(p) for p in sorted((folder / "responses").glob("*.json"))}
    write_json(folder / "predictions_lock.json", {"files": lock, "sha256": digest(lock)})
    references = {(r["task"], r["case_id"]): r for r in
                  map(json.loads, reference_path.read_text().splitlines())}
    statuses, finishes, scored = Counter(), Counter(), []
    for case in cases:
        identity = digest([case["task"], case["variant"], case["case_id"]])
        output = folder / "responses" / (identity + ".json")
        if not output.exists():
            statuses["missing"] += 1
            continue
        row = json.loads(output.read_text())
        request = json.loads((folder / "requests" / (identity + ".json")).read_text())
        expected_payload = {"model": settings["model"], "messages": case["messages"], **settings["generation"]}
        if (row["case_id"] != case["case_id"] or row["model"] != settings["model"]
                or digest(request["payload"]) != request["request_sha256"]
                or row["request_sha256"] != request["request_sha256"]
                or request["request_sha256"] != digest(expected_payload)):
            raise ValueError("Request/response provenance mismatch")
        statuses[row["status"]] += 1
        if row["status"] != "completed":
            continue
        ref = references[(case["task"], case["case_id"])]
        answer = lab_answer(row["text"], ref["choice_count"])
        finishes[row.get("finish_reason")] += 1
        scored.append({"task": case["task"], "case_id": case["case_id"], "subtask": ref["subtask"],
                       "answer": answer, "correct": answer == ref["target_choice"],
                       "sure": answer != ref["unsure_choice"], "parsed": answer is not None,
                       "finish_reason": row.get("finish_reason")})
    review = json.loads((ROOT / settings["review_file"]).read_text())
    summary = {"run_id": settings["run_id"], "task_id": settings["approved_task_ids"][0],
               "model": settings["model"], "model_revision": settings["model_revision"],
               "protocol_variant": settings["variant"], "planned": len(cases),
               "completed": len(scored), "parsed": sum(r["parsed"] for r in scored),
               "invalid_outputs": sum(not r["parsed"] for r in scored),
               "statuses": dict(statuses), "finish_reasons": dict(finishes),
               "case_scope": "reviewed_public_subset" if len(scored) == len(cases) else "INCOMPLETE_completed_cases_only",
               "held_before_inference": len(review.get("held_cases", [])),
               "metrics": metrics_for(scored), "explanation_support_score": None,
               "comparison_to_paper": settings["paper_comparison"],
               "pretraining_exposure": "unknown", "request_response_hash_audit": "passed",
               "predictions_locked_before_reference_read": True}
    summary["metrics_by_subtask"] = {
        task: metrics_for([r for r in scored if r["subtask"] == task])
        for task in sorted({r["subtask"] for r in scored})}
    write_json(folder / "scores.json", summary)
    write_json(folder / "per_case_scores.json", scored)
    with (folder / "metrics.csv").open("w", newline="") as handle:
        columns = ["run_id", "task_id", "protocol_variant", "model", "metric", "value", "planned", "completed", "case_scope"]
        writer = csv.DictWriter(handle, fieldnames=columns)
        writer.writeheader()
        for name in ["accuracy", "precision", "coverage"]:
            writer.writerow({**{k: summary[k] for k in ["run_id", "task_id", "model", "planned", "completed", "case_scope"]},
                             "protocol_variant": settings["variant"], "metric": name, "value": summary["metrics"][name]})
    print(json.dumps(summary), flush=True)
    return summary


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--run", required=True)
    args = parser.parse_args()
    score(ROOT / "results/runs" / args.run)
