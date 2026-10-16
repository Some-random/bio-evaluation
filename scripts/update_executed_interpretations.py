"""Append executed protocol interpretations without regenerating older records.

Offline reporting only. Existing task/variant/split records are preserved exactly;
conflicting executions need a separately named variant, never replacement.
"""
import argparse
import copy
import csv
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, ensure_ascii=False,
                                    separators=(",", ":")).encode()).hexdigest()


def file_digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def registry_key(row):
    return row["task_id"], row["protocol_variant"], row.get("native_split")


def executed_record(base, folder):
    scores = json.loads((folder / "scores.json").read_text())
    done = json.loads((folder / "completion.json").read_text())
    manifest = json.loads((folder / "run_manifest.json").read_text())
    config = manifest["configuration"]
    if done.get("generation_exit_code") != 0 or done.get("scoring_exit_code") != 0:
        return None
    if config.get("case_scope") == "task_shard_only" or scores.get("case_scope") == "task_shard_only":
        return None
    if scores.get("completed") != scores.get("planned"):
        return None
    if config.get("aggregate_only"):
        union = scores.get("full_test_id_union_validation", {})
        if not union.get("complete") or not union.get("union_matches_full_test_ids"):
            return None
    request_path = next((folder / "requests").glob("*.json"), None)
    if request_path is None:
        return None
    request = json.loads(request_path.read_text())
    if digest(request["payload"]) != request["request_sha256"]:
        raise ValueError("Saved request payload hash mismatch: " + str(request_path))
    # The native scorer already audited the complete request/response contract.
    audited = (scores.get("request_response_hash_audit") == "passed"
               or (folder / "scoring_output_lock.json").is_file())
    if not audited:
        raise ValueError("No scored prediction audit: " + str(folder))
    row = copy.deepcopy(base)
    row.update(protocol_variant=scores.get("protocol_variant", config["variant"]),
               model=config["model"], model_revision=config["model_revision"],
               run_id=config["run_id"], prepared_case_count=scores["planned"],
               outcome_score=scores["metrics"], explanation_support_score=None,
               score_status="completed_with_invalid_outputs" if scores.get("invalid_outputs", 0) else "completed",
               execution_scope_status="user_authorized_reviewed_local_evaluation")
    if scores.get("native_split", config.get("native_split")) is not None:
        row["native_split"] = scores.get("native_split", config.get("native_split"))
        row["execution_coverage"] = "Complete declared native split only; other required splits remain separate and are not implied complete."
    fields = request.get("supplied_fields", config.get("model_facing_fields", []))
    row["prepared_model_facing_fields"] = fields
    row["required_inputs"] = fields
    modalities = config.get("input_modalities", scores.get("input_modalities", ["text"]))
    row["input_interface"] = "Archived native/adapted user prompt; modalities: " + ", ".join(modalities) + "; no solver tools"
    row["actual_supplied_information"] = {
        "status": "dispatched", "benchmark_requests_submitted": scores["completed"],
        "observed_model_input_fields": fields, "run_id": config["run_id"],
        "request_directory": str(folder.relative_to(ROOT) / "requests"),
        "request_hashes_verified": True, "reference_answers_or_explanations_supplied": False,
        "solver_tools": [], "full_request_contract_audit_source": str(folder.relative_to(ROOT) / "scores.json"),
        "representative_request_sha256": file_digest(request_path),
        "native_required_images_preserved": any("image" in str(item).lower() for item in modalities),
        "generation": config["generation"],
    }
    interpretation = scores.get("interpretation", {})
    if not isinstance(interpretation, dict):
        row["execution_interpretation_note"] = interpretation
        interpretation = {}
    aliases = {"reference_answer_source": "reference_evidence",
               "good_score_establishes": "good_score", "bad_score_establishes": "bad_score"}
    for key, fallback in aliases.items():
        value = interpretation.get(key, interpretation.get(fallback))
        if value:
            row[key] = value
    demands = interpretation.get("task_demands", interpretation.get("likely_demands"))
    if demands is None and isinstance(interpretation.get("likely_demands_provisional"), list):
        demands = {"labels": interpretation["likely_demands_provisional"]}
    if isinstance(demands, dict):
        row["task_demands"] = {**demands,
            "status": "provisional_analyst_inference", "internal_model_computation_established": False}
    if config.get("approved_task_ids") == ["P29"]:
        row["actual_supplied_information"].update(
            reference_answers_or_explanations_supplied=True,
            direct_curated_reference_files_or_teacher_explanations_supplied=False,
            native_predictor_context_contributes_to_scoring_target=True,
            reference_input_dependence=scores.get("native_reference_qualification"))
        row["input_reference_dependence"] = scores.get("native_reference_qualification")
    row["mechanism_reference_available"] = "not_independently_assessed"
    row["mechanism_reference_note"] = "Outcome scoring does not validate generated explanations. Unsupported claims are not automatically false."
    row["explanation_support"] = {**row.get("explanation_support", {}),
        "status": "not_assessed", "correct_outcome_validates_rationale": False,
        "missing_mechanism_evidence_means_false": False, "native_metric_replaced": False}
    row["source_caveat"] = scores.get("comparison_to_paper", config.get("paper_comparison", "Protocol qualifications retained in the frozen configuration."))
    row["classification_basis"] = {**row.get("classification_basis", {}),
        "verification_status": "Frozen source inputs and executed requests audited by offline scorer; task demands remain analyst inferences.",
        "demands_inferred_from_compatibility_code": False}
    row["output_validity"] = {k: scores.get(k) for k in ("planned", "completed", "parsed", "invalid_outputs", "finish_reasons", "case_scope")}
    if scores.get("invalid_outputs", 0):
        row["source_caveat"] += " Invalid/truncated outputs remain in native denominators; low scores can reflect output delivery rather than incorrect biological predictions."
    if scores.get("finish_reasons", {}).get("length") == scores["planned"] and scores.get("parsed") == 0:
        row["bad_score_establishes"] = "Every request exhausted the frozen output-token limit without a parseable final answer. This condition failed to deliver usable answers; it does not establish that all biological predictions were wrong."
        row["source_caveat"] += " Native coverage can count invalid non-abstentions; coverage1 does not mean usable answers."
    row["execution_artifacts"] = {"scores_file": str(folder.relative_to(ROOT) / "scores.json"),
        "scores_sha256": file_digest(folder / "scores.json"),
        "run_manifest_sha256": file_digest(folder / "run_manifest.json")}
    return row


def merge_records(records, additions):
    result = list(records)
    index = {registry_key(row): row for row in records}
    if len(index) != len(records):
        raise ValueError("Duplicate task/variant registry key")
    for row in additions:
        key = registry_key(row)
        if key in index:
            if index[key].get("run_id") != row.get("run_id"):
                raise ValueError("Protocol variant collision requires separate naming: " + str(key))
            continue
        result.append(row)
        index[key] = row
    return result


def cell(value):
    if isinstance(value, (dict, list)):
        value = json.dumps(value, ensure_ascii=False)
    return str(value if value is not None else "").replace("|", "\\|").replace("\n", " ")


def write_tables(records):
    columns = list(dict.fromkeys(key for row in records for key in row))
    with (ROOT / "reports/interpretation_table.csv").open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=columns)
        writer.writeheader()
        for row in records:
            writer.writerow({k: json.dumps(v, ensure_ascii=False) if isinstance(v, (dict, list)) else v for k, v in row.items()})
    lines = ["# Interpretation alongside evaluation results", "",
        "All original catalog/preparation records are retained. Executed variants below describe actual supplied information and outcome scores. Task-demand labels are provisional analyst descriptions; they do not establish a model's internal computation.", "",
        "A correct prediction does not validate its explanation. Missing support does not establish that a mechanistic claim is false. Public benchmark training exposure remains unknown. Native protocols and separately named adaptations retain their own metrics and restrictions.", "",
        "| Task / executed variant | Likely demands (provisional) | Information actually supplied | Reference answer source | Outcome / validity | Good score establishes | Bad score establishes |",
        "| --- | --- | --- | --- | --- | --- | --- |"]
    for row in records:
        if not row.get("run_id"):
            continue
        supplied = row["actual_supplied_information"]
        values = [row["task_id"] + " / " + row["protocol_variant"] + (" / split " + row["native_split"] if row.get("native_split") else ""),
            row["task_demands"], supplied.get("observed_model_input_fields", []),
            row["reference_answer_source"],
            {"score": row["outcome_score"], "validity": row.get("output_validity"), "explanation_support": "not assessed"},
            row["good_score_establishes"], row["bad_score_establishes"]]
        lines.append("| " + " | ".join(cell(value) for value in values) + " |")
    lines += ["", "The complete catalog, prepared variants, explanation-support distinctions, source qualifications, run IDs and hashes are in [interpretation_table.csv](interpretation_table.csv) and [interpretation_notes.jsonl](../results/interpretation_notes.jsonl).", ""]
    (ROOT / "reports/INTERPRETATION_TABLE.md").write_text("\n".join(lines))


def update():
    path = ROOT / "results/interpretation_notes.jsonl"
    records = [json.loads(line) for line in path.read_text().splitlines() if line]
    existing = {registry_key(row): row for row in records}
    additions = []
    for folder in sorted((ROOT / "results/runs").glob("qwen38*")):
        if not all((folder / name).is_file() for name in ("scores.json", "completion.json", "run_manifest.json")):
            continue
        scores = json.loads((folder / "scores.json").read_text())
        task = scores.get("task_id")
        if not task:
            continue  # Earlier frozen B01 record remains exactly as recorded.
        if task == "P43" and scores.get("dataset"):
            continue  # Three native datasets share one whole-setting registry key.
        key = task, scores.get("protocol_variant"), scores.get("native_split")
        if key in existing and existing[key].get("run_id") == folder.name:
            continue
        base = existing.get((task, "NATIVE_PUBLIC_COT", None)) or existing.get((task, "NATIVE", None))
        if base is None:
            raise ValueError("No original interpretation contract: " + task)
        row = executed_record(base, folder)
        if row:
            additions.append(row)
    merged = merge_records(records, additions)
    if merged != records:
        tmp = path.with_suffix(".tmp")
        tmp.write_text("".join(json.dumps(row, ensure_ascii=False) + "\n" for row in merged))
        tmp.replace(path)
    write_tables(merged)
    print(json.dumps({"records_preserved": len(records), "executed_variants_added": len(merged)-len(records), "total_records": len(merged)}))


if __name__ == "__main__":
    argparse.ArgumentParser(description=__doc__).parse_args()
    update()
