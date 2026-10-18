"""Offline scorer for frozen P03/P07/P08 local runs; no training or inference."""
import argparse
from collections import Counter
import csv
import hashlib
import json
import math
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
TASKS = {"P03", "P07", "P08"}


def digest(value):
    return hashlib.sha256(json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def file_digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write_json(path, value):
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n")
    temporary.chmod(0o600)
    temporary.replace(path)


def parse_class_id(text):
    match = re.fullmatch(r"\s*(?:Answer\s*:\s*)?([0-9])\.?\s*", text or "", re.IGNORECASE)
    return int(match.group(1)) if match else None


def parse_number(text):
    match = re.fullmatch(r"\s*(?:Answer\s*:\s*)?([+-]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][+-]?\d+)?)\s*", text or "", re.IGNORECASE)
    if not match:
        return None
    value = float(match.group(1))
    return value if math.isfinite(value) else None


def outcome_metrics(task, targets, texts):
    if task not in TASKS or not targets or len(targets) != len(texts):
        raise ValueError("Require matching nonempty planned reference/response slots")
    parsed = [(parse_class_id if task == "P03" else parse_number)(text) for text in texts]
    result = {"planned": len(targets), "parsed": sum(p is not None for p in parsed),
              "missing": sum(t is None for t in texts),
              "invalid": sum(t is not None and p is None for t, p in zip(texts, parsed))}
    if task == "P03":
        if any(not isinstance(t, int) or not 0 <= t <= 9 for t in targets):
            raise ValueError("Reference outside native ten-class ontology")
        correct = sum(p is not None and p == t for p, t in zip(parsed, targets))
        result.update(accuracy=correct / len(targets), correct=correct,
                      all_case_rule="Invalid/missing classes count incorrect; all planned rows stay in denominator.")
    else:
        from scipy.stats import spearmanr
        if any(not math.isfinite(t) for t in targets):
            raise ValueError("Reference must be finite on native unchanged scale")
        pairs = [(t, p) for t, p in zip(targets, parsed) if p is not None]
        undefined = len(pairs) < 2 or len({t for t, _ in pairs}) < 2 or len({p for _, p in pairs}) < 2
        value = None if undefined else float(spearmanr([t for t, _ in pairs], [p for _, p in pairs]).correlation)
        complete = len(pairs) == len(targets)
        result.update(spearman=value if complete else None, spearman_parsed_only=value if not complete else None,
                      undefined_constant_or_insufficient=undefined,
                      all_case_rule="No invented prediction for failures. Full-test Spearman requires every output to parse; incomplete valid-only correlation is separately labeled.")
    return result


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
        prediction = (parse_class_id if task == "P03" else parse_number)(text)
        ref = references[(task, case["case_id"])]
        if completed:
            finishes[str(response.get("finish_reason"))] += 1
            for key in ["prompt_tokens", "completion_tokens", "total_tokens"]:
                usage[key] += response.get("response", {}).get("usage", {}).get(key, 0) or 0
        scored.append({"task": task, "case_id": case["case_id"], "status": status, "completed": completed,
                       "raw_text": text, "prediction": prediction, "target": ref["target"], "parsed": prediction is not None,
                       "correct": prediction is not None and prediction == ref["target"] if task == "P03" else None,
                       "finish_reason": response.get("finish_reason") if response else None,
                       "request_sha256": request["request_sha256"] if request else None})
    metrics = outcome_metrics(task, [r["target"] for r in scored], [r["raw_text"] for r in scored])
    completed = sum(r["completed"] for r in scored)
    scope = "full_frozen_reviewed_released_test" if completed == len(cases) else "INCOMPLETE_frozen_reviewed_released_test"
    summary = {"run_id": settings["run_id"], "task_id": task, "model": settings["model"],
               "model_revision": settings["model_revision"], "protocol_variant": settings["variant"],
               "planned": len(cases), "requests_saved": requests, "completed": completed, "parsed": metrics["parsed"],
               "invalid_outputs": metrics["invalid"], "missing_or_failed_outputs": sum(not r["completed"] for r in scored),
               "statuses": dict(states), "finish_reasons": dict(finishes), "token_usage": dict(usage), "metrics": metrics,
               "input_modalities": ["amino_acid_sequence", "text"], "scoring_output_lock_sha256": lock["contract_sha256"],
               "case_scope": scope, "held_before_inference": len(review.get("held_cases", [])), "explanation_support_score": None,
               "comparison_to_paper": "Original released public test data and native outcome/metric; zero-shot Qwen prompt/representation/training regime differs from native-trained TAPE/ProtST heads."
                    + (" PyTorch stability release12851 differs from original2019 paper12839 and is explicitly version-qualified." if task == "P08" else ""),
               "interpretation": {"likely_demands": {"labels": ["biological_outcome_prediction", "sequence_representation"], "status": "provisional analyst description; internal computation unknown"},
                                  "actually_supplied": "Archived complete-sequence user prompts and fixed objective; original class ontology supplied for P03. No measurement labels, parent/topology metadata, mutation counts, explanations, retrieval or tools.",
                                  "reference_answer_source": "Pinned native DeepLoc curated localization classes or TAPE experimental GFP/folding-stability measurements; scorer-only reference file hashed before inference.",
                                  "good_score_establishes": "Recovery of source outcomes on the declared released test under the fixed zero-shot protocol.",
                                  "bad_score_establishes": "Limited outcome recovery for this input/regime; does not independently establish deficient general reasoning.",
                                  "explanation_correctness": "Unassessed; correct prediction does not certify rationale and unsupported mechanism is not automatically false."},
               "contamination": "Reference labels excluded, inputs frozen, outputs hash-locked before scoring, no training or test-guided changes. Prior exposure to public source data unknown."}
    write_json(folder / "scores.json", summary)
    write_json(folder / "per_case_scores.json", scored)
    with (folder / "metrics.csv").open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["run_id", "task_id", "protocol_variant", "model", "metric", "value", "planned", "completed", "parsed", "case_scope"])
        writer.writeheader()
        for name in (["accuracy"] if task == "P03" else ["spearman", "spearman_parsed_only"]):
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
