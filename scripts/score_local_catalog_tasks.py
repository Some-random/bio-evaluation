"""Score one frozen local protein-property run, entirely offline.

Only the scorer reads held-out labels. No registry, runner, or input is changed.
"""
import argparse
from collections import Counter
import csv
import hashlib
import json
from pathlib import Path

from catalog_metric_helpers import (classification_accuracy, parse_binary_answer,
                                    parse_numeric_answer, regression_spearman)

ROOT = Path(__file__).resolve().parents[1]
BINARY_TASKS = {"P01", "P02", "P10", "P11"}
TASKS = BINARY_TASKS | {"P06"}


def digest(value):
    return hashlib.sha256(json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def file_digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write_json(path, value):
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n")
    temporary.chmod(0o600)
    temporary.replace(path)


def expected_payload(case, settings):
    if set(case) != {"task", "case_id", "variant", "split", "messages"}:
        raise ValueError("Frozen case includes unexpected fields")
    if case["task"] not in settings["approved_task_ids"] or case["variant"] != settings["variant"]:
        raise ValueError("Case differs from frozen task/variant")
    if len(case["messages"]) != 1 or set(case["messages"][0]) != {"role", "content"}:
        raise ValueError("Require a single reviewed user input")
    if case["messages"][0]["role"] != "user" or not isinstance(case["messages"][0]["content"], str):
        raise ValueError("Unexpected message modality")
    return {"model": settings["model"], "messages": case["messages"], **settings["generation"]}


def lock_outputs(folder, cases):
    """Freeze observed raw records before opening the scorer references."""
    files = {"run_manifest.json": file_digest(folder / "run_manifest.json")}
    for case in cases:
        identity = digest([case["task"], case["variant"], case["case_id"]])
        for category in ["requests", "responses"]:
            name = category + "/" + identity + ".json"
            path = folder / name
            files[name] = file_digest(path) if path.exists() else None
    record = {"files_sha256": files, "contract_sha256": digest(files),
              "policy": "Raw requests, outputs and missing slots locked before reading references; no response selection, repair or scoring retries."}
    path = folder / "scoring_output_lock.json"
    if path.exists() and json.loads(path.read_text()) != record:
        raise ValueError("Pre-scoring output lock changed; archived outputs cannot be silently replaced")
    if not path.exists():
        write_json(path, record)
    return record


def score(folder):
    manifest = json.loads((folder / "run_manifest.json").read_text())
    settings = manifest["configuration"]
    approved = settings["approved_task_ids"]
    if len(approved) != 1 or approved[0] not in TASKS:
        raise ValueError("This scorer supports exactly one reviewed protein-property task")
    task = approved[0]
    for name, expected in settings["frozen_files_sha256"].items():
        if file_digest(ROOT / name) != expected:
            raise ValueError("Frozen file changed: " + name)
    cases = [json.loads(line) for line in (ROOT / settings["input_file"]).read_text().splitlines() if line]
    if not cases or digest(cases) != manifest["case_contract_sha256"]:
        raise ValueError("Frozen case contract changed or empty")
    review = json.loads((ROOT / settings["review_file"]).read_text())
    if [c["case_id"] for c in cases] != review["approved_case_ids"]:
        raise ValueError("Execution cases differ from ordered approved review")
    if len({c["case_id"] for c in cases}) != len(cases):
        raise ValueError("Duplicate execution case IDs")
    if {c["case_id"] for c in cases} & {r["case_id"] for r in review.get("held_cases", [])}:
        raise ValueError("Held case found in scored run")
    output_lock = lock_outputs(folder, cases)
    ref_path = ROOT / settings["scorer_reference_file"]
    if file_digest(ref_path) != settings["scorer_reference_sha256"]:
        raise ValueError("Scorer references differ from their pre-inference hash")
    references = {}
    for row in map(json.loads, ref_path.read_text().splitlines()):
        key = (row["task"], row["case_id"])
        if key in references:
            raise ValueError("Duplicate reference identity")
        references[key] = row
    statuses, finishes, scored = Counter(), Counter(), []
    request_count, usage = 0, Counter()
    for case in cases:
        identity = digest([case["task"], case["variant"], case["case_id"]])
        output = folder / "responses" / (identity + ".json")
        request_path = folder / "requests" / (identity + ".json")
        payload = expected_payload(case, settings)
        request = json.loads(request_path.read_text()) if request_path.exists() else None
        request_count += int(request is not None)
        if request is not None and (digest(request["payload"]) != request["request_sha256"]
                                    or request["request_sha256"] != digest(payload)):
            raise ValueError("Dispatched request differs from frozen case")
        row = json.loads(output.read_text()) if output.exists() else None
        if row is not None:
            if request is None:
                raise ValueError("Response has no saved request")
            for field, expected in [("task", task), ("case_id", case["case_id"]), ("variant", case["variant"]),
                                    ("model", settings["model"]), ("model_revision", settings["model_revision"]),
                                    ("request_sha256", request["request_sha256"])]:
                if row.get(field) != expected:
                    raise ValueError("Response provenance mismatch: " + field)
        status = row.get("status") if row else ("interrupted_unknown_completion" if request else "not_dispatched")
        statuses[status] += 1
        completed = status == "completed"
        text = row.get("text", "") if completed else None
        parser = parse_binary_answer if task in BINARY_TASKS else parse_numeric_answer
        parsed = parser(text)
        ref = references[(task, case["case_id"])]
        target = ref["target_binary"] if task in BINARY_TASKS else ref["target"]
        if completed:
            finishes[str(row.get("finish_reason"))] += 1
            for name in ["prompt_tokens", "completion_tokens", "total_tokens"]:
                usage[name] += row.get("response", {}).get("usage", {}).get(name, 0) or 0
        scored.append({"task": task, "case_id": case["case_id"], "dataset": ref.get("dataset"),
                       "status": status, "completed": completed, "raw_text": text,
                       "prediction": parsed, "parsed": parsed is not None, "target": target,
                       "correct": parsed is not None and parsed == target if task in BINARY_TASKS else None,
                       "finish_reason": row.get("finish_reason") if row else None,
                       "request_sha256": request["request_sha256"] if request else None})
    targets = [r["target"] for r in scored]
    texts = [r["raw_text"] for r in scored]
    metrics = classification_accuracy(targets, texts) if task in BINARY_TASKS else regression_spearman(targets, texts)
    completed = sum(r["completed"] for r in scored)
    scope = "full_frozen_reviewed_case_set" if completed == len(cases) else "INCOMPLETE_frozen_reviewed_case_set"
    summary = {"run_id": settings["run_id"], "task_id": task, "model": settings["model"],
               "model_revision": settings["model_revision"], "protocol_variant": settings["variant"],
               "input_modalities": ["amino_acid_sequence", "text"],
               "scoring_output_lock_sha256": output_lock["contract_sha256"],
               "planned": len(cases), "requests_saved": request_count, "completed": completed,
               "parsed": sum(r["parsed"] for r in scored),
               "invalid_outputs": sum(r["completed"] and not r["parsed"] for r in scored),
               "missing_or_failed_outputs": sum(not r["completed"] for r in scored),
               "statuses": dict(statuses), "finish_reasons": dict(finishes), "token_usage": dict(usage),
               "case_scope": scope, "held_before_inference": len(review.get("held_cases", [])), "metrics": metrics,
               "explanation_support_score": None,
               "comparison_to_paper": "Native source outcome, data split and metric when separately verified; prompted zero-shot full-sequence Qwen baseline, not matched specialist training. No native BioT5 special-token architecture or fitted regression/classification head reproduced.",
               "interpretation": {"task_demands": {"labels": ["biological_outcome_prediction", "sequence_representation"],
                                     "status": "provisional analyst description; computation not inferred from benchmark name"},
                                  "actually_supplied": "Exactly the archived user prompts with complete sequence(s), fixed objective and output instructions; no scorer references or tools.",
                                  "reference_answer_source": "Pinned public source's experimental/curated outcome labels, independently hashed before inference and read only by this scorer.",
                                  "good_score_establishes": "Held-out outcome recovery under this declared input and zero-shot regime.",
                                  "bad_score_establishes": "Limited outcome recovery under this input and regime; does not establish poor general reasoning.",
                                  "explanation_correctness": "Unassessed. A correct outcome does not validate a rationale; missing evidence does not imply a mechanistic claim is false."},
               "contamination": "Reference labels excluded from requests; no tools, retrieval, fine-tuning or test-feedback prompt changes. Public pretraining exposure unknown."}
    write_json(folder / "scores.json", summary)
    write_json(folder / "per_case_scores.json", scored)
    with (folder / "metrics.csv").open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["run_id", "task_id", "protocol_variant", "model", "metric", "value", "planned", "completed", "parsed", "case_scope"])
        writer.writeheader()
        for name in (["accuracy"] if task in BINARY_TASKS else ["spearman", "spearman_parsed_only"]):
            writer.writerow({"run_id": settings["run_id"], "task_id": task, "protocol_variant": settings["variant"],
                             "model": settings["model"], "metric": name, "value": metrics[name], "planned": len(cases),
                             "completed": completed, "parsed": summary["parsed"], "case_scope": scope})
    print(json.dumps(summary, ensure_ascii=False))
    return summary


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--run", required=True)
    args = parser.parse_args()
    score(ROOT / "results/runs" / args.run)
