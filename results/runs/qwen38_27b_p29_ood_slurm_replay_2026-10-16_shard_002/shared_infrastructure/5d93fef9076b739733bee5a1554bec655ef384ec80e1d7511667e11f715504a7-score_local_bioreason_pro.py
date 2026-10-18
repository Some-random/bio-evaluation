"""Offline native CAFA Fmax/IA-weighted Fmax on locked eligible P28 outputs."""
import argparse
from collections import Counter
import csv
import hashlib
import json

import bioreason_pro_contract as protocol
from run_local_labbench_multimodal import payload_for, request_record

ROOT = protocol.ROOT


def lock_outputs(folder, cases):
    files = {"run_manifest.json": protocol.file_sha(folder / "run_manifest.json")}
    for case in cases:
        identity = protocol.digest([case["task"], case["variant"], case["case_id"]]) + ".json"
        for kind in ("requests", "responses"):
            name = kind + "/" + identity
            path = folder / name
            files[name] = protocol.file_sha(path) if path.exists() else None
    lock = {"files_sha256": files, "contract_sha256": protocol.digest(files),
            "policy": "Every eligible raw generation and missing slot locked before any reference loading. Fixedk1, no best-of-k/oracle selection, teacher fallback, prompt-context concatenation or retries."}
    path = folder / "scoring_output_lock.json"
    if path.exists() and json.loads(path.read_text()) != lock:
        raise ValueError("Pre-scoring output lock changed")
    if not path.exists():
        protocol.save(path, lock)
    return lock


def locked_record(folder, name, lock):
    path = folder / name
    expected = lock["files_sha256"][name]
    if expected is None:
        if path.exists():
            raise ValueError("Output appeared after missing slot locked")
        return None
    raw = path.read_bytes()
    if hashlib.sha256(raw).hexdigest() != expected:
        raise ValueError("Raw generation changed after output lock")
    return json.loads(raw)


def score(folder):
    manifest = json.loads((folder / "run_manifest.json").read_text())
    cfg = manifest["configuration"]
    if cfg["approved_task_ids"] != ["P28"] or cfg["variant"] != protocol.VARIANT:
        raise ValueError("Require fixed P28 contextual adaptation")
    reference_path = ROOT / cfg["scorer_reference_file"]
    deferred = []
    for name, expected in cfg["frozen_files_sha256"].items():
        if (ROOT / name).resolve() == reference_path.resolve():
            deferred.append(expected)
        elif protocol.file_sha(ROOT / name) != expected:
            raise ValueError("Frozen input/source changed: " + name)
    cases = [json.loads(line) for line in (ROOT / cfg["input_file"]).read_text().splitlines() if line]
    review = json.loads((ROOT / cfg["review_file"]).read_text())
    ids = [case["case_id"] for case in cases]
    if (not cases or ids != review["approved_case_ids"] or len(set(ids)) != len(ids)
            or set(ids) & {item["case_id"] for item in review.get("held_cases", [])}
            or manifest["case_contract_sha256"] != protocol.digest(cases) or manifest["planned_cases"] != len(cases)):
        raise ValueError("Exact frozen ordered eligible case contract changed")
    for case in cases:
        payload_for(case, cfg)
    lock = lock_outputs(folder, cases)
    references_raw = reference_path.read_bytes()
    reference_hash = hashlib.sha256(references_raw).hexdigest()
    if reference_hash != cfg["scorer_reference_sha256"] or any(h != reference_hash for h in deferred):
        raise ValueError("Scorer-only references changed")
    references = {}
    for ref in map(json.loads, references_raw.decode().splitlines()):
        if ref["task"] != "P28" or ref["case_id"] in references:
            raise ValueError("Duplicate/wrong native reference identity")
        references[ref["case_id"]] = ref
    rows, predictions, states, finishes, usage = [], {}, Counter(), Counter(), Counter()
    request_count = response_count = 0
    for case in cases:
        identity = protocol.digest([case["task"], case["variant"], case["case_id"]]) + ".json"
        request = locked_record(folder, "requests/" + identity, lock)
        response = locked_record(folder, "responses/" + identity, lock)
        request_count += request is not None; response_count += response is not None
        if request is not None and request != request_record(case, cfg):
            raise ValueError("Archived request differs from exact frozen input/generation")
        if response is not None:
            if request is None:
                raise ValueError("Response without its archived request")
            expected = {**{key: case[key] for key in ("task", "case_id", "variant", "split")},
                        "model": cfg["model"], "model_revision": cfg["model_revision"], "request_sha256": request["request_sha256"]}
            if any(response.get(key) != value for key, value in expected.items()):
                raise ValueError("Raw response provenance mismatch")
        status = response.get("status") if response else ("interrupted_unknown_completion" if request else "not_dispatched")
        completed = status == "completed"
        states[status] += 1
        continuation = content = reasoning = ""
        finish = response.get("finish_reason") if response else None
        if completed:
            if response["response"].get("model") != cfg["model"]:
                raise ValueError("Raw API model differs from frozen baseline")
            continuation, content, reasoning = protocol.generated_continuation(response)
            finishes[str(finish)] += 1
            for key in ("prompt_tokens", "completion_tokens", "total_tokens"):
                usage[key] += response["response"].get("usage", {}).get(key, 0) or 0
        predicted = protocol.extract_go(continuation)
        predictions[case["case_id"]] = predicted
        rows.append({"task": "P28", "case_id": case["case_id"], "status": status, "completed": completed,
            "parsed": bool(predicted), "raw_generated_continuation": continuation if completed else None,
            "raw_final_content": content if completed else None, "raw_reasoning_channel": reasoning if completed else None,
            "predicted_go_terms": sorted(predicted), "final_content_go_terms_diagnostic": sorted(protocol.extract_go(content)),
            "target_aspects": references[case["case_id"]]["target_aspects"], "finish_reason": finish,
            "truncated": completed and finish == "length", "empty_generated_continuation": completed and not continuation.strip(),
            "request_sha256": request["request_sha256"] if request else None})
    # One global native metric call; no shard-level Fmax averaging.
    metric, contract = protocol.native_metrics(predictions, [references[identity] for identity in ids], folder / "native_cafa")
    completed = sum(row["completed"] for row in rows)
    summary = {"run_id": cfg["run_id"], "task_id": "P28", "model": cfg["model"], "model_revision": cfg["model_revision"],
        "protocol_variant": protocol.VARIANT, "planned": len(cases), "requests_saved": request_count, "responses_saved": response_count,
        "completed": completed, "parsed": sum(row["parsed"] for row in rows),
        "invalid_outputs": sum(row["completed"] and not row["parsed"] for row in rows),
        "missing_or_failed_outputs": len(cases) - completed, "truncated_outputs": sum(row["truncated"] for row in rows),
        "statuses": dict(states), "finish_reasons": dict(finishes), "token_usage": dict(usage), "metrics": metric,
        "metric_units": "fraction0–1, per GO aspect", "metric_contract": contract,
        "case_scope": ("full_frozen_native_eligible_temporal_test" if completed == len(cases) else "INCOMPLETE_native_eligible_temporal_test_with_all_case_penalty") if len(cases) == 8159 else "task_shard_only",
        "generation_completeness": "complete" if completed == len(cases) else "incomplete_with_all_eligible_failures_retained",
        "released_test_case_count": 8630, "native_excluded_case_count": 471, "full_native_eligible_test_case_count": 8159,
        "input_modalities": ["complete_amino_acid_sequence", "organism", "native_predictor_derived_text_context"],
        "scoring_output_lock_sha256": lock["contract_sha256"], "predictions_locked_before_reference_read": True,
        "continuation_boundary": "Only raw API assistant generated reasoning channel followed by final content. No request/prompt/go_pred context, teacher trace or target fallback. Primary released evaluator extracts all continuation GO IDs; final-content-only GO sets are unscored diagnostics.",
        "failure_policy": "Every planned eligible case remains in native ground truth; missing/failed/empty/no-GO output has an empty prediction set, with zero recall contribution. No success-only filtering or fabricated terms.",
        "native_model_difference": "Full-sequence zero-shot Qwen with verified source organism/InterPro/STRING/GO-GPT context; trained ESM3/projectors and GOgraph encoder are not replicated. These learned representations may be essential; poor performance does not isolate reasoning.",
        "comparison_to_paper": cfg["paper_comparison"], "explanation_support_score": None,
        "interpretation": {"likely_demands": {"labels": ["learned biological prediction", "sequence representation", "context integration", "ontology mapping"], "classification_is_provisional": True},
            "actually_supplied": "Complete original amino-acid sequence plus exact native source organism, InterPro, STRING and GO-GPT predicted context, with fixed all3-aspect/native-summary instructions. No gold function/GO annotations, names, subcellular annotation or teacher traces.",
            "reference_answer_source": "Pinned native temporal-test curated GO annotations, scorer-only; official source ontology/IA propagation",
            "good_score_establishes": "Recovery of recorded annotations under this declared full-sequence contextual zero-shot system",
            "bad_score_establishes": "Limited annotation recovery; does not isolate reasoning or show absence of unannotated biological functions",
            "explanation_correctness": "Unassessed. Correct predicted GO IDs do not validate the rationale; missing reference support is not automatic falsity."},
        "contamination": "Reference/teacher fields excluded, model/protocol frozen before inference, no training or outcome-guided variants. Prior public exposure and predictor context training histories remain unknown."}
    protocol.save(folder / "per_case_scores.json", rows); protocol.save(folder / "scores.json", summary)
    with (folder / "metrics.csv").open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["run_id", "task_id", "protocol_variant", "model", "metric", "value", "planned", "completed", "parsed", "case_scope"])
        writer.writeheader()
        for key, value in metric.items():
            writer.writerow({**{name: summary[name] for name in ("run_id", "task_id", "protocol_variant", "model", "planned", "completed", "parsed", "case_scope")}, "metric": key, "value": value})
    print(json.dumps(summary)); return summary


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--run", required=True)
    score(ROOT / "results/runs" / parser.parse_args().run)
