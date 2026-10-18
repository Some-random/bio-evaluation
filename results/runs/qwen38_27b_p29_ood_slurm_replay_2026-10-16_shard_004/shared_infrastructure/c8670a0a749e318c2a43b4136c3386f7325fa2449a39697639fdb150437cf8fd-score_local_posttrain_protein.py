"""Offline P29 native augmented-target mean GO-F1 and fixed curated diagnostic."""
import argparse
from collections import Counter, defaultdict
import csv
import hashlib
import json

import posttrain_protein_contract as protocol
from run_local_labbench_multimodal import payload_for, request_record
from score_local_bioreason_pro import lock_outputs, locked_record

ROOT = protocol.ROOT


def score(folder):
    manifest = json.loads((folder / "run_manifest.json").read_text()); cfg = manifest["configuration"]
    split = cfg["native_split"]
    if cfg["approved_task_ids"] != ["P29"] or cfg["variant"] != protocol.VARIANT or split not in protocol.SPLITS:
        raise ValueError("Require preregistered released RL P29 ID/OOD adaptation")
    reference_path = ROOT / cfg["scorer_reference_file"]
    deferred = []
    for name, expected in cfg["frozen_files_sha256"].items():
        if (ROOT / name).resolve() == reference_path.resolve(): deferred.append(expected)
        elif protocol.file_sha(ROOT / name) != expected: raise ValueError("Frozen dependency changed: " + name)
    cases = [json.loads(line) for line in (ROOT / cfg["input_file"]).read_text().splitlines() if line]
    review = json.loads((ROOT / cfg["review_file"]).read_text()); ids = [c["case_id"] for c in cases]
    if (not cases or ids != review["approved_case_ids"] or len(ids) != len(set(ids)) or review.get("held_cases")
            or manifest["case_contract_sha256"] != protocol.digest(cases) or manifest["planned_cases"] != len(cases)):
        raise ValueError("Complete frozen ordered source input contract changed")
    for case in cases: payload_for(case, cfg)
    lock = lock_outputs(folder, cases)
    # Every output and missing slot is immutable before this first label read.
    raw = reference_path.read_bytes(); sha = hashlib.sha256(raw).hexdigest()
    if sha != cfg["scorer_reference_sha256"] or any(expected != sha for expected in deferred):
        raise ValueError("Scorer-only references changed")
    refs = {}
    for row in map(json.loads, raw.decode().splitlines()):
        if row["task"] != "P29" or row["native_split"] != split or row["case_id"] in refs:
            raise ValueError("Wrong or duplicate source reference")
        refs[row["case_id"]] = row
    if not set(ids) <= set(refs): raise ValueError("Missing native reference")
    api = protocol.native_api(); ontology = protocol.native_ontology()
    rows, states, finishes, usage = [], Counter(), Counter(), Counter()
    requests = responses = 0
    for case in cases:
        identity = protocol.digest([case["task"], case["variant"], case["case_id"]]) + ".json"
        request = locked_record(folder, "requests/" + identity, lock)
        response = locked_record(folder, "responses/" + identity, lock)
        requests += request is not None; responses += response is not None
        if request is not None and request != request_record(case, cfg): raise ValueError("Archived request mismatch")
        if response is not None:
            if request is None: raise ValueError("Response without request")
            expected = {**{k: case[k] for k in ("task", "case_id", "variant", "split")},
                "model": cfg["model"], "model_revision": cfg["model_revision"], "request_sha256": request["request_sha256"]}
            if any(response.get(k) != v for k, v in expected.items()): raise ValueError("Response provenance mismatch")
        status = response.get("status") if response else ("interrupted_unknown_completion" if request else "not_dispatched")
        states[status] += 1; completed = status == "completed"
        continuation = content = reasoning = ""; finish = response.get("finish_reason") if response else None
        if completed:
            if response["response"].get("model") != cfg["model"]: raise ValueError("Raw API model mismatch")
            continuation, content, reasoning = protocol.generated_continuation(response)
            finishes[str(finish)] += 1
            for key in ("prompt_tokens", "completion_tokens", "total_tokens"):
                usage[key] += response["response"].get("usage", {}).get(key, 0) or 0
        predicted = api.extract_go_ids_sft_aligned(continuation)
        ref = refs[case["case_id"]]; metric = protocol.score_prediction(predicted, ref, ontology)
        rows.append({"task": "P29", "case_id": case["case_id"], "native_split": split, "organism": ref["organism"],
            "status": status, "completed": completed, "parsed": bool(predicted), "finish_reason": finish,
            "truncated": completed and finish == "length", "raw_generated_continuation": continuation if completed else None,
            "raw_final_content": content if completed else None, "raw_reasoning_channel": reasoning if completed else None,
            "predicted_go_terms": sorted(predicted), "final_only_go_terms_diagnostic": sorted(api.extract_go_ids_sft_aligned(content)),
            "native_augmented_go_terms": ref["native_augmented_go_terms"],
            "curated_only_go_terms_diagnostic": ref["curated_only_go_terms_diagnostic"],
            "predictor_go_terms_added_to_native_target": ref["predictor_go_terms_added_to_native_target"],
            "request_sha256": request["request_sha256"] if request else None, **metric})
    means = protocol.mean_metrics(rows)
    groups = defaultdict(list)
    for row in rows: groups[row["organism"]].append(row)
    completed = sum(row["completed"] for row in rows); full_n = protocol.SPLITS[split][1]
    scope = ("full_released_species_" + split + "_test" if completed == len(rows) else "INCOMPLETE_released_species_" + split + "_test_all_case_penalty") if len(rows) == full_n else "task_shard_only"
    summary = {"task_id": "P29", "run_id": cfg["run_id"], "model": cfg["model"], "model_revision": cfg["model_revision"],
        "protocol_variant": protocol.VARIANT, "native_split": split, "case_scope": scope,
        "planned": len(rows), "completed": completed, "parsed": sum(row["parsed"] for row in rows), "requests_saved": requests,
        "responses_saved": responses, "invalid_outputs": sum(row["completed"] and not row["parsed"] for row in rows),
        "missing_or_failed_outputs": len(rows) - completed, "truncated_outputs": sum(row["truncated"] for row in rows),
        "statuses": dict(states), "finish_reasons": dict(finishes), "token_usage": dict(usage),
        "generation_completeness": "complete" if completed == len(rows) else "incomplete_all_planned_failures_retained",
        "metrics": {k: v for k, v in means.items() if not k.endswith("_diagnostic")},
        "curated_only_diagnostic_metrics": {k: v for k, v in means.items() if k.endswith("_diagnostic")},
        "organism_subgroup_metrics": {name: {"planned": len(group), "completed": sum(row["completed"] for row in group),
            "native_augmented_metrics": {k: v for k, v in protocol.mean_metrics(group).items() if not k.endswith("_diagnostic")},
            "curated_only_diagnostic_metrics": {k: v for k, v in protocol.mean_metrics(group).items() if k.endswith("_diagnostic")}} for name, group in groups.items()},
        "metric_units": "fraction0–1; arithmetic mean per-case propagated GO set P/R/F1, separate ID/OOD and organisms; not CAFA Fmax or IA-weighted Fmax",
        "native_reference_qualification": "Native resolve_gold_terms_from_row unions curated annotations and go_pred_leaf while go_pred is supplied. Reference/input dependence can reward recovery/copying of supplied predictions; native score does not isolate novel function inference. Curated-only reference also has input overlap and unknown historical independence. Both scores fixed beforehand; no cherry-picked metric or context removal.",
        "seed_predictor_overlap": cfg["seed_predictor_overlap"],
        "native_predictor_augmented_target_cases": sum(bool(row["predictor_go_terms_added_to_native_target"]) for row in rows),
        "metric_contract": {"source_file": str(protocol.GO_SOURCE.relative_to(protocol.ROOT)), "source_revision": protocol.CODE_REVISION,
            "source_sha256": protocol.file_sha(protocol.GO_SOURCE), "ontology_sha256": protocol.file_sha(protocol.ONTOLOGY),
            "ontology_version": "2023-01-01", "relations": ["is_a", "part_of"], "weights": "None: uniform1", "roots_and_unknown_self_terms": "Preserved source behavior",
            "extractor": "Unmodified extract_go_ids_sft_aligned; GO_SUMMARY blocks preferred, then aspect blocks, then final-answer heuristic",
            "aggregation": "Arithmetic mean per-case fixed-set score over every original planned row, once from exact combined predictions",
            "obonet": "1.1.1", "networkx": "3.4.2", "historical_dependency_versions": "Unpinned in author code; frozen prospectively, historical equality not established"},
        "predictions_locked_before_reference_read": True, "scoring_output_lock_sha256": lock["contract_sha256"],
        "continuation_boundary": "Generated API reasoning channel then final content only; never source request, go_pred context, teacher trace or gold. Final-only GO set is unscored diagnostic. API/tokenizer byte identity with historical skip_special_tokens decoding is not claimed.",
        "input_modalities": ["complete_amino_acid_sequence", "organism", "native_InterPro_text", "native_GO_GPT_predictions"],
        "comparison_to_paper": cfg["paper_comparison"], "source_contract_disagreements": cfg["source_contract_disagreements"],
        "interpretation": cfg["prospective_interpretation"], "explanation_support_score": None,
        "failure_policy": "All planned missing, transport, empty, noGO and invalid completions retained; empty prediction set contributes zero P/R/F1. No retries/resampling, output selection or success-only filtering.",
        "contamination": "Gold/teachers excluded from requests and no test-guided tuning; public exposure and upstream predictor histories unknown."}
    protocol.save(folder / "per_case_scores.json", rows); protocol.save(folder / "scores.json", summary)
    with (folder / "metrics.csv").open("w", newline="") as handle:
        fields = ["run_id", "task_id", "protocol_variant", "model", "native_split", "metric_family", "metric", "value", "planned", "completed", "parsed", "case_scope"]
        writer = csv.DictWriter(handle, fieldnames=fields); writer.writeheader()
        for family, values in [("native_augmented_reference", summary["metrics"]), ("curated_only_diagnostic", summary["curated_only_diagnostic_metrics"])]:
            for key, value in values.items(): writer.writerow({**{k: summary[k] for k in fields if k in summary}, "metric_family": family, "metric": key, "value": value})
    print(json.dumps({"task_id": "P29", "native_split": split, "planned": len(rows), "completed": completed, "metrics": summary["metrics"]}))
    return summary


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__); parser.add_argument("--run", required=True)
    score(ROOT / "results/runs" / parser.parse_args().run)
