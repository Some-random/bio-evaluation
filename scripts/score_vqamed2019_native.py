"""Offline organizer-protocol strict accuracy; historical BLEU remains withheld."""
import argparse
from collections import Counter
import json
import re
import string

from run_local_labbench_multimodal import ROOT, digest, file_digest, payload_for, write_json
from score_local_medical_vqa import lock_outputs, locked_record


def normalize(text):
    # Organizer: lower case, remove punctuation, tokenize words. No articles,
    # synonyms, gold-assisted substring extraction, or reasoning fallback.
    return " ".join(text.lower().translate(str.maketrans("", "", string.punctuation)).split())


def reference_alternatives(answer):
    values = []
    for alternative in answer.split("#"):
        parts = re.split(r"(\([^()]*\))", alternative)
        if "(" in "".join(part for part in parts if not (part.startswith("(") and part.endswith(")"))):
            raise ValueError("Unresolved nested/unbalanced optional reference syntax")
        candidates = [""]
        for part in parts:
            if part.startswith("(") and part.endswith(")"):
                candidates = [prefix + suffix for prefix in candidates for suffix in ["", part[1:-1]]]
            else:
                candidates = [prefix + part for prefix in candidates]
        values.extend(normalize(value) for value in candidates)
    if not values or any(not value for value in values):
        raise ValueError("Empty reference answer")
    return set(values)


def score(folder):
    manifest = json.loads((folder / "run_manifest.json").read_text())
    settings = manifest["configuration"]
    if settings["approved_task_ids"] != ["V04"]:
        raise ValueError("Wrong benchmark")
    for name, expected in settings["frozen_files_sha256"].items():
        if file_digest(ROOT / name) != expected:
            raise ValueError("Frozen input/scoring dependency changed: " + name)
    cases = [json.loads(line) for line in (ROOT / settings["input_file"]).read_text().splitlines()]
    if len(cases) != 500 or digest(cases) != manifest["case_contract_sha256"]:
        raise ValueError("Original complete test contract changed")
    if file_digest(ROOT / settings["scorer_reference_file"]) != settings["scorer_reference_sha256"]:
        raise ValueError("Frozen references changed")
    output_lock = lock_outputs(folder, cases)
    labels = {row["case_id"]: row for row in map(json.loads, (ROOT / settings["scorer_reference_file"]).read_text().splitlines())}
    if set(labels) != {c["case_id"] for c in cases}:
        raise ValueError("Reference/test identity mismatch")
    rows, states, finishes = [], Counter(), Counter()
    for case in cases:
        identity = digest([case["task"], case["variant"], case["case_id"]]) + ".json"
        request = locked_record(folder, "requests/" + identity, output_lock)
        response = locked_record(folder, "responses/" + identity, output_lock)
        if request and (digest(request["payload"]) != request["request_sha256"] or request["request_sha256"] != digest(payload_for(case, settings))):
            raise ValueError("Dispatched input differs from original question/image")
        status = response.get("status") if response else "missing_or_failed"
        states[status] += 1
        text = None
        if status == "completed":
            for key, value in {"task": "V04", "case_id": case["case_id"], "variant": case["variant"], "model": settings["model"], "model_revision": settings["model_revision"]}.items():
                if response.get(key) != value:
                    raise ValueError("Output identity mismatch")
            if not request or response.get("request_sha256") != request["request_sha256"]:
                raise ValueError("Output lacks its original request")
            raw = response["response"]
            if response.get("http_status") != 200 or raw.get("model") != settings["model"] or len(raw.get("choices", [])) != 1:
                raise ValueError("Unexpected completion/model/transport")
            text = raw["choices"][0]["message"].get("content") or ""
            if text != response["text"]:
                raise ValueError("Saved final answer differs from response")
            finishes[response.get("finish_reason")] += 1
        label = labels[case["case_id"]]
        rows.append({"case_id": case["case_id"], "category": label["category"], "status": status,
            "final_answer": text, "parsed": bool(text and normalize(text)),
            "correct": bool(text and normalize(text) in reference_alternatives(label["reference_answer"]))})
    metrics = {"strict_accuracy": sum(row["correct"] for row in rows) / len(rows)}
    summary = {"run_id": settings["run_id"], "task_id": "V04", "model": settings["model"], "model_revision": settings["model_revision"],
        "protocol_variant": settings["variant"], "planned": len(rows), "completed": states["completed"],
        "parsed": sum(r["parsed"] for r in rows), "invalid_outputs": sum(r["status"] == "completed" and not r["parsed"] for r in rows),
        "statuses": dict(states), "finish_reasons": dict(finishes), "metrics": metrics,
        "metrics_by_category": {cat: {"strict_accuracy": sum(r["correct"] for r in rows if r["category"] == cat) / sum(r["category"] == cat for r in rows)} for cat in sorted({r["category"] for r in rows})},
        "case_scope": "original_complete_test500", "held_before_inference": 0,
        "explanation_support_score": None, "pretraining_exposure": "unknown",
        "request_response_hash_audit": "passed", "predictions_locked_before_reference_read": True,
        "scoring_output_lock_sha256": output_lock["contract_sha256"],
        "comparison_to_paper": settings["paper_comparison"],
        "native_metric_qualification": "Organizer-defined strict exact matching with documented alternative/optional gold syntax; fixed ASCII punctuation removal/whitespace word tokenization. Historical2019 executable not recovered, so not asserted byte-identical. BLEU withheld pending verification.",
        "withheld_metrics": {"bleu": "Original2019 implementation/smoothing/aggregation unresolved; no fabricated or later-year replacement value."}}
    write_json(folder / "scores.json", summary)
    write_json(folder / "per_case_scores.json", rows)
    print(json.dumps(summary))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--run", required=True)
    score(ROOT / "results/runs" / parser.parse_args().run)
