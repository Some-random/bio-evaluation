"""Offline native LAB-Bench scoring for exactly one frozen local-model run."""
import argparse
from collections import Counter
import copy
import csv
import json
from pathlib import Path

from run_local_labbench import ROOT, digest, file_digest, payload_for, write_json
from score_results import lab_answer


def metrics_for(rows):
    n = len(rows)
    correct = sum(r["correct"] for r in rows)
    sure = sum(r["sure"] for r in rows)
    return {"accuracy": correct / n if n else 0.0,
            "precision": correct / sure if sure else 0.0,
            "coverage": sure / n if n else 0.0, "n_total": n,
            "n_correct": correct, "n_sure": sure}


def update_interpretation(settings, summary, request_count):
    path = ROOT / "results/interpretation_notes.jsonl"
    rows = [json.loads(s) for s in path.read_text().splitlines() if s]
    record = copy.deepcopy(next(r for r in rows if r["task_id"] == "B01" and r["protocol_variant"] == "NATIVE"))
    record.update(protocol_variant=settings["variant"], model=settings["model"], run_id=settings["run_id"],
                  model_revision=settings["model_revision"], prepared_case_count=summary["planned"],
                  prepared_model_facing_fields=["question", "shuffled_choices", "native_COT_instructions"],
                  input_interface="Original public MCQ text; one user message; closed book; no tools",
                  required_inputs=["question", "shuffled_choices", "native_COT_instructions"],
                  reference_answer_source="Pinned futurehouse/lab-bench creator-curated ideal and distractor answers; scorer-only choice mapping",
                  reference_evidence_type=["curated_reference_answer"],
                  mechanism_reference_available="no",
                  mechanism_reference_note="No independent explanation-support rubric was executed. MCQ labels do not validate generated explanations.",
                  score_status="completed" if summary["completed"] == summary["planned"] else "incomplete",
                  outcome_score=summary["metrics"], explanation_support_score=None,
                  execution_scope_status="user_authorized_local_reviewed_public_subset",
                  source_caveat="Two cases held before inference based on input review; public subset only; one seeded run, not the paper's three-run full-set mean. Public training exposure unknown.")
    record["task_demands"] = {
        "labels": ["biological_knowledge_use", "answer_selection", "possible_recall_or_inference"],
        "rationale": "Only question and choices are supplied. No papers or retrieval tools are provided. Recall, distractor elimination and biological inference can each contribute; their contributions cannot be identified from scores.",
        "status": "provisional_analyst_inference", "internal_model_computation_established": False}
    record["actual_supplied_information"] = {
        "status": "dispatched", "benchmark_requests_submitted": request_count,
        "observed_model_input_fields": ["question", "shuffled_choices", "native_COT_instructions"],
        "run_id": settings["run_id"], "request_hashes_verified": True,
        "reference_answers_or_explanations_supplied": False, "solver_tools": [],
        "request_directory": f"results/runs/{settings['run_id']}/requests"}
    record["good_score_establishes"] = "Agreement with curated answers on these reviewed public questions under the frozen closed-book resources. It does not distinguish recall, elimination and inference."
    record["bad_score_establishes"] = "Limited answer recovery with question/choices only; missing source information, abstention, model knowledge and inference remain possible contributors."
    record["allowed_result_claim"] = record["good_score_establishes"]
    record["classification_basis"]["verification_status"] = "Pinned public inputs, official prompt, choice shuffle, parser and metric inspected; exact dispatched requests saved"
    rows = [r for r in rows if not (r["task_id"] == "B01" and r["protocol_variant"] == settings["variant"])]
    rows.append(record)
    path.write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in rows))
    table = ROOT / "reports/interpretation_table.csv"
    with table.open(newline="") as handle:
        columns = list(csv.DictReader(handle).fieldnames)
    for extra in ["model", "run_id", "model_revision"]:
        if extra not in columns:
            columns.append(extra)
    with table.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=columns)
        writer.writeheader()
        for r in rows:
            writer.writerow({c: json.dumps(r.get(c), ensure_ascii=False) if isinstance(r.get(c), (dict, list)) else r.get(c) for c in columns})
    report = ROOT / "reports/INTERPRETATION_TABLE.md"
    text = report.read_text()
    text = text.replace("No biological inference scores exist yet; prepared inputs have not been submitted to a solver.",
                        "Executed local results are described below; catalog-only rows remain provisional task contracts.")
    marker = "\n## Executed local LitQA2 baseline\n"
    text = text.split(marker)[0].rstrip()
    m = summary["metrics"]
    text += marker + "\n| Run / outcome | Likely demands (provisional) | Actually supplied | Reference answer source | Score interpretation |\n|---|---|---|---|---|\n"
    text += (f"| {settings['run_id']}; {summary['completed']}/{summary['planned']} completed; "
             f"accuracy {m['accuracy']:.4f}, precision {m['precision']:.4f}, coverage {m['coverage']:.4f} | "
             "Biological knowledge, answer selection; recall and inference contributions unresolved | "
             f"{request_count} original question/choice prompts and native COT instructions; no papers, retrieval tools or answer keys | "
             "Creator-curated public labels, pinned and scorer-only | Good: agreement under these resources. Bad: limited answer recovery; does not isolate knowledge versus reasoning. Explanations unassessed. |\n")
    text += "\nTwo input-reviewed cases were held before inference. This is a public-subset result with native prompts and metrics, not the full paper evaluation. Prior exposure to the public dataset is unknown.\n"
    report.write_text(text)


def score(folder):
    manifest = json.loads((folder / "run_manifest.json").read_text())
    settings = manifest["configuration"]
    for name, expected in settings["frozen_files_sha256"].items():
        if file_digest(ROOT / name) != expected:
            raise ValueError("Frozen file changed: " + name)
    cases = [json.loads(s) for s in (ROOT / settings["input_file"]).read_text().splitlines() if s]
    if digest(cases) != manifest["case_contract_sha256"]:
        raise ValueError("Input contract changed")
    if file_digest(ROOT / "data/labbench/scorer_references.jsonl") != settings["scorer_reference_sha256"]:
        raise ValueError("Scorer references differ from their pre-inference hash")
    references = {(r["task"], r["case_id"]): r for r in map(json.loads, (ROOT / "data/labbench/scorer_references.jsonl").read_text().splitlines())}
    statuses, finishes, scored = Counter(), Counter(), []
    for case in cases:
        identity = digest([case["task"], case["variant"], case["case_id"]])
        output = folder / "responses" / (identity + ".json")
        if not output.exists():
            statuses["missing"] += 1
            continue
        row = json.loads(output.read_text())
        request = json.loads((folder / "requests" / (identity + ".json")).read_text())
        if row["case_id"] != case["case_id"] or row["model"] != settings["model"]:
            raise ValueError("Response provenance mismatch")
        if (digest(request["payload"]) != request["request_sha256"]
                or row["request_sha256"] != request["request_sha256"]
                or request["request_sha256"] != digest(payload_for(case, settings))):
            raise ValueError("Request/response hash mismatch")
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
    completed = len(scored)
    metrics = metrics_for(scored)
    scope = "reviewed_public_subset" if completed == len(cases) else "INCOMPLETE_completed_cases_only"
    summary = {"run_id": settings["run_id"], "model": settings["model"],
               "model_revision": settings["model_revision"], "protocol_variant": settings["variant"],
               "planned": len(cases), "completed": completed, "parsed": sum(r["parsed"] for r in scored),
               "invalid_outputs": sum(not r["parsed"] for r in scored), "statuses": dict(statuses),
               "finish_reasons": dict(finishes), "case_scope": scope, "metrics": metrics,
               "held_before_inference": 2, "total_public_LitQA2": 199, "explanation_support_score": None,
               "comparison_to_paper": "Native public questions, COT prompt, shuffle algorithm and deterministic parser/metrics. Two cases held; one seeded Qwen run, not the original three-run mean or full private/public set. No model-based answer-extraction fallback.",
               "contamination": "No reference labels sent; frozen before generation; no tools, retrieval, fine-tuning or test-guided changes. Pretraining exposure unknown."}
    write_json(folder / "scores.json", summary)
    write_json(folder / "per_case_scores.json", scored)
    with (folder / "metrics.csv").open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["run_id", "task_id", "protocol_variant", "model", "metric", "value", "planned", "completed", "case_scope"])
        writer.writeheader()
        for name in ["accuracy", "precision", "coverage"]:
            writer.writerow({"run_id": settings["run_id"], "task_id": "B01", "protocol_variant": settings["variant"],
                             "model": settings["model"], "metric": name, "value": metrics[name],
                             "planned": len(cases), "completed": completed, "case_scope": scope})
    update_interpretation(settings, summary, len(list((folder / "requests").glob("*.json"))))
    print(json.dumps(summary, ensure_ascii=False))
    return summary


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--run", required=True)
    args = parser.parse_args()
    score(ROOT / "results/runs" / args.run)
