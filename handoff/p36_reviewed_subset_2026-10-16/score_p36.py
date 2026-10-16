"""Offline released-code paired-reference ROUGE; no paper Smith-Waterman claim."""
import argparse
from collections import Counter
from datetime import datetime, timezone
import json
from pathlib import Path

from p36_contract import (ROOT, digest, file_digest, paired_rouge, payload, read_jsonl,
                          serialization_diagnostic, validate_cases, write_json)


def score(run_dir):
    manifest_path = run_dir / "run_manifest.json"
    manifest = json.loads(manifest_path.read_text())
    config = manifest["configuration"]
    cases, review = validate_cases(config)
    if manifest["case_contract_sha256"] != digest(cases):
        raise ValueError("Run input contract changed")
    locked = {"run_manifest.json": file_digest(manifest_path)}
    slots = []
    for case in cases:
        identity = digest([case["task"], case["variant"], case["case_id"]])
        paths = {kind: run_dir / kind / (identity + ".json") for kind in ["requests", "responses"]}
        for kind, path in paths.items():
            locked[str(path.relative_to(run_dir))] = file_digest(path) if path.exists() else None
        request = json.loads(paths["requests"].read_text()) if paths["requests"].exists() else None
        response = json.loads(paths["responses"].read_text()) if paths["responses"].exists() else None
        expected = digest(payload(case, config))
        if request and (request["request_sha256"] != expected or digest(request["payload"]) != expected):
            raise ValueError("Saved request differs from frozen prompt")
        if response:
            if request is None:
                raise ValueError("Response lacks saved request")
            for field, value in {"task": "P36", "case_id": case["case_id"], "variant": case["variant"],
                                 "model": config["model"], "model_revision": config["model_revision"],
                                 "request_sha256": expected}.items():
                if response.get(field) != value:
                    raise ValueError("Response provenance differs: " + field)
        status = response["status"] if response else ("ambiguous_dispatch_no_retry" if request else "not_dispatched")
        completed = bool(response and status == "completed")
        text = response.get("text") if completed else ""
        if not isinstance(text, str):
            raise ValueError("Final content is not a string")
        if completed and text != response["response"]["choices"][0]["message"]["content"]:
            raise ValueError("Saved final content changed")
        slots.append({"case_id": case["case_id"], "status": status, "completed": completed,
                      "raw_final_content": text, "finish_reason": response.get("finish_reason") if response else None,
                      **serialization_diagnostic(text)})
    lock = {"files_sha256": locked, "contract_sha256": digest(locked),
            "policy": "Lock all declared outputs/missing slots before opening targets; no retries, selection, cleanup or repair."}
    lock_path = run_dir / "scoring_output_lock.json"
    if lock_path.exists() and json.loads(lock_path.read_text()) != lock:
        raise ValueError("Outputs changed after scoring lock")
    if not lock_path.exists():
        write_json(lock_path, lock)
    # Gold is opened only after every output and missing slot has been locked.
    reference_path = ROOT / config["scorer_reference_file"]
    if file_digest(reference_path) != config["scorer_reference_sha256"]:
        raise ValueError("Scorer-only references changed")
    references = read_jsonl(reference_path)
    if [x["case_id"] for x in references] != [x["case_id"] for x in cases]:
        raise ValueError("Reference order differs from declared scope")
    pairs = [[r["target"], r["source_prompt"]] for r in references]
    result = paired_rouge([r["raw_final_content"] for r in slots], pairs, run_dir / "native_metric_output.tsv")
    completed = sum(r["completed"] for r in slots)
    report = {"created_at_utc": datetime.now(timezone.utc).isoformat(), "task_id": "P36",
              "model": config["model"], "model_revision": config["model_revision"],
              "protocol_variant": config["variant"], "planned": len(cases), "completed": completed,
              "full_source_cases": review["full_source_case_count"], "case_scope": "PARTIAL_input_reviewed_first64_subset",
              "full_benchmark_complete": False, "all_declared_subset_outputs_saved": completed == len(cases),
              "metrics": result, "metric_label": "qualified_released_code_paired_reference_rougeL",
              "statuses": dict(Counter(r["status"] for r in slots)),
              "finish_reasons": dict(Counter(str(r["finish_reason"]) for r in slots if r["completed"])),
              "valid_native_serializations": sum(r["valid_native_protein_serialization"] for r in slots),
              "missing_or_failed_slots": len(cases) - completed,
              "missing_slot_policy": f"Empty prediction in every missing/failed slot; all {len(cases)} planned subset slots remain in metric denominator.",
              "invalid_or_truncated_output_policy": "Raw final content retained and scored without repair, even if malformed or length-stopped; format validity is diagnostic only.",
              "metric_contract": config["metric_contract"], "comparison_qualification": config["comparison_qualification"],
              "paper_normalized_smith_waterman": None, "biological_function_validated": False,
              "explanation_support_score": None, "scoring_output_lock_sha256": lock["contract_sha256"]}
    write_json(run_dir / "scores.json", report)
    write_json(run_dir / "per_case_scores.json", slots)
    return report


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--run-dir", type=Path, required=True)
    print(json.dumps(score(parser.parse_args().run_dir), indent=2))
