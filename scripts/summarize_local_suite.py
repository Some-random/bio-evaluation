#!/usr/bin/env python3
"""Rebuild an offline, aggregate-only view of local evaluation coverage.

This module never opens case inputs, requests, responses, scorer references, or
model weights, and has no provider client. It does not update interpretation
records, readiness, inference configuration, or the frozen first-run artifacts.
"""

from __future__ import annotations

import argparse
import csv
from datetime import datetime, timezone
import hashlib
import io
import json
import math
from pathlib import Path
import tempfile


CATALOG = "handoff/bio_eval_agent_handoff_2026-10-13/references/evaluation_catalog.json"
COMPARISONS = "reports/PUBLISHED_BENCHMARK_COMPARISONS_2026-10-15.json"
SOURCE_RECOVERY = "reports/remaining_native_source_recovery_2026-10-15.json"
POSTTRAIN_GAPS = "reports/posttrain_native_gap_audit.json"
P34_FEASIBILITY = "reports/p34_five_landscape_feasibility_2026-10-15.json"
NATURE_GENERATION_FEASIBILITY = "reports/naturelm_generation_feasibility_2026-10-15.json"
DESIGN_FEASIBILITY = "reports/REMAINING_DESIGN_SOURCE_FEASIBILITY_2026-10-15.json"
VISION_INTEGRITY = "reports/labbench_vision_aggregate_integrity_qualification.json"
SUCCESS_STATUSES = {"completed", "cached", "success", "ok"}
FINAL_STATES = {"completed_scored", "completed_scored_with_failures"}
COUNT_METRICS = {"planned", "completed", "parsed", "correct", "invalid", "invalid_outputs", "missing", "held", "total",
                 "eligible", "denominator", "requests_saved", "responses_saved", "failed", "truncated", "truncated_outputs",
                 "missing_or_failed_outputs", "test_case_count", "case_count", "class_count", "label_count"}
CONFIG_FIELDS = {
    "run_id", "task_id", "task_ids", "approved_task_ids", "model",
    "model_revision", "protocol_variant", "variant", "checkpoint_precision",
    "input_modalities", "model_facing_fields", "source_dataset_revision",
    "source_code_revision", "case_scope", "gpu_ids", "frozen_at_utc",
    "shard_count", "shard_index", "shard_id", "parent_run_id",
    "aggregated_from_shards", "source_shard_run_ids",
    "reporting_protocol_kind", "dataset", "native_split", "full_native_metric_set_complete",
}
INTERPRETATION_FIELDS = {
    "task_id", "protocol_variant", "input_interface", "required_inputs",
    "prepared_model_facing_fields", "prepared_case_count", "task_demands",
    "reference_evidence_type", "allowed_result_claim", "unsupported_result_claim",
    "native_metric", "metric_scope", "source_caveat", "score_status",
    "execution_scope_status", "model", "model_revision", "run_id",
    "outcome_score", "explanation_support_score", "explanation_support",
}
CAVEATS = [
    "Completed means the reported local protocol variant completed on its declared cases; it does not mean all 64 settings or a full paper evaluation were reproduced.",
    "Reviewed public subsets, held cases, private/full paper sets, and single seeded runs versus repeated paper means have different scope. Published values are contextual unless case IDs, inputs, training and scoring protocols match; no superiority or significance claim follows from this report.",
    "Task-trained models, learned protein encoders plus trained heads, and prompted local models use different training and representations. Their scores are not a matched-training comparison; no new head training is implied.",
    "Outcome prediction metrics do not validate explanations, establish a causal mechanism, or isolate internal reasoning. Explanation support remains unassessed unless separately scored against suitable reference evidence; missing support does not mean false.",
    "Prior pretraining exposure to public benchmarks is unknown. Do not describe these results as contamination-free.",
    "Native input modalities, restrictions, split units and metric names remain distinct. An adapted text result does not complete a native structural, embedding, image, measurement or external-evaluator setting.",
    "The reporter reads aggregate files only, performs no inference, retries or provider calls, and changes no inference configurations or frozen results. Its view is a snapshot while workers may continue.",
    "A finished shard is partial task coverage. Whole-task completion from shards requires an explicit completed aggregate score whose offline validation proves the unique case-ID union matches the full declared test set, with no missing or extra cases.",
    "Execution can complete while full-planned primary metrics remain undefined. Parsed-only, strict-label, offline reference and other diagnostics remain separate and cannot establish valid whole-task benchmark completion.",
]


def _pick(obj, keys):
    return {key: obj[key] for key in keys if key in obj}


def _number(value):
    return value if isinstance(value, (int, float)) and not isinstance(value, bool) else None


def _first(*values):
    return next((v for v in values if v is not None and v != ""), None)


def _task_ids(obj):
    value = _first(obj.get("task_id"), obj.get("task_ids"), obj.get("approved_task_ids"))
    return [value] if isinstance(value, str) else list(value or [])


def _protocol_kind(variant):
    variant = str(variant or "").upper()
    if "ADAPT" in variant:
        return "adapted"
    if variant == "NATIVE" or variant.startswith("NATIVE_"):
        return "native"
    # These are declared repository baseline names, not inferred biological
    # demands or claims about internal computation. Root verified this naming
    # convention for full-sequence, zero-shot description and DTI likelihood
    # adaptations; native-required-image QA retains its NATIVE_* namespace.
    if variant.startswith(("QWEN_FULL_SEQUENCE_TEXT_", "QWEN_ZERO_SHOT_",
                           "QWEN_DTI_FIRST_TOKEN_CONDITIONAL_")):
        return "adapted"
    return "unknown"


def _has_metrics(metrics):
    return isinstance(metrics, dict) and any(_metric_leaves(metrics))


def _metric_leaves(metrics):
    """Reported scalar scores (including undefined ones), excluding counts/prose."""
    for path, value in _flatten_metrics(metrics):
        leaf = path[-1].lower()
        if (leaf in COUNT_METRICS or leaf.startswith(("n_", "num_")) or leaf.endswith(("_count", "_counts"))
                or isinstance(value, bool)):
            continue
        if value is None or _number(value) is not None:
            yield path, value


def _primary_metric_validity(score):
    """Resolve old/new score contracts without promoting diagnostics to primary.

    This is reporting metadata only: original score fields and metric values
    remain unchanged. Legacy full-test Spearman cannot be rescued by a finite
    parsed-only correlation, another auxiliary metric, or numeric case counts.
    """
    if not score:
        return None, "No aggregate score artifact."
    declared = score.get("full_planned_primary_metrics_valid")
    if declared is False:
        return False, "Frozen scorer explicitly marks full-planned primary metrics invalid."
    if declared is not None and declared is not True:
        return False, "Frozen primary-validity flag is not a boolean true/false contract."
    metrics = score.get("metrics", {})
    if not isinstance(metrics, dict):
        return False, "Aggregate contains no scalar primary metric object."
    leaves = list(_metric_leaves(metrics))
    primary = [(path, value) for path, value in leaves if not any(
        "parsed_only" in part.lower() or "diagnostic" in part.lower()
        or part.upper().startswith("OFFLINE_") or part.upper() == "STRICT_FINAL_LABEL" for part in path)]
    names = score.get("primary_metric_names")
    if names:
        if not isinstance(names, list) or any(not isinstance(name, str) for name in names):
            return False, "Declared primary metric names are not a fixed string list."
        selected = []
        for name in names:
            matches = [(path, value) for path, value in primary if ".".join(path) == name or path[-1] == name]
            if not matches:
                return False, "A declared primary metric is missing from the reported scalar metrics: " + name
            selected.extend(matches)
        primary = selected
        basis = "Declared fixed primary metric names, excluding diagnostic/count namespaces."
    elif any(key.lower() == "spearman" for key in metrics):
        primary = [(path, value) for path, value in primary if len(path) == 1 and path[0].lower() == "spearman"]
        basis = "Legacy full-test Spearman contract; parsed-only and auxiliary values cannot complete it."
    else:
        basis = "Legacy reported primary scalar metrics, excluding diagnostic/count/prose namespaces."
    valid = bool(primary) and all(_number(value) is not None and math.isfinite(value) for _, value in primary)
    return valid, basis


def _modalities(fields, description=""):
    """Conservative interface labels from field names, never native-task guesses."""
    text = " ".join(map(str, fields or [])) + " " + str(description or "")
    text = text.lower()
    labels = []
    for term, label in (("image", "image"), ("structure", "structure"),
                        ("embedding", "embedding"), ("expression", "expression"),
                        ("sequence", "sequence_text")):
        if term in text:
            labels.append(label)
    if any(term in text for term in ("question", "choice", "text", "instructions", "mcq", "user message")):
        labels.insert(0, "text")
    return labels or None


def _flatten_metrics(metrics, prefix=()):
    for key, value in metrics.items():
        path = prefix + (key,)
        if isinstance(value, dict):
            yield from _flatten_metrics(value, path)
        else:
            yield path, value


def _native_blocker(readiness, notes):
    text = f"{readiness} {notes}".lower()
    if any(term in text for term in ("policy_hold", "prohibited", "no_local_dispatch", "flagged", "safety_hold", "risk_hold", "review_blocked", "no_redispatch")):
        return "prohibited_or_held"
    unavailable = any(term in text for term in ("unavailable", "missing", "not_available", "blocked", "not downloaded"))
    if unavailable and any(term in text for term in ("external evaluator", "external_evaluator", "oracle", "evaluator unavailable")):
        return "external_evaluator_unavailable"
    if unavailable and any(term in text for term in ("protocol", "scorer", "native metric")):
        return "protocol_unavailable"
    if unavailable and any(term in text for term in ("source", "dataset", "release", "artifact", "download")):
        return "source_unavailable"
    if "adapter_required" in text or "adapter required" in text:
        return "adapter_required"
    if "case_review_pending" in text or "case review" in text and "pending" in text:
        return "case_review_pending"
    if "not_prepared" in text or "not prepared" in text:
        return "native_execution_not_prepared"
    if unavailable:
        return "blocked"
    return None


def _catalog_blocker(entry):
    """Qualify dated analyst metadata without treating it as new authority."""
    status = str(entry.get("status", "")).lower()
    notes = " ".join(entry.get("blockers", []))
    inferred = _native_blocker(status, notes)
    # A note can hold only particular assays. Do not turn that into a blanket
    # task prohibition unless the source explicitly assigns a task-level hold.
    if _native_blocker(status, "") == "prohibited_or_held":
        return "prohibited_or_held"
    if "paper_test_mismatch" in status:
        return "source_protocol_mismatch"
    if "bundle_unavailable" in status:
        return "source_unavailable"
    if any(term in status for term in ("proxy", "evaluator", "judge")) and "pending" in status:
        return "external_evaluator_pending"
    if "supervised_regime_not_authorized" in status:
        return "native_training_regime_blocked"
    if "assay" in status and ("scope" in status or "review" in status):
        return "assay_scope_review_pending"
    if any(term in status for term in ("data_acquisition_pending", "test_acquisition_pending", "data_and_mapping_acquisition_pending")):
        return "source_acquisition_pending"
    if "unresolved" in status or "holdout_pending" in status:
        return "source_protocol_unresolved"
    if status.startswith("prepared_verified") or "prepared_execution" in status:
        return None
    if "adapter" in status:
        return "adapter_required"
    return (inferred if inferred != "prohibited_or_held" else None) or ("native_protocol_setup_pending" if "pending" in status or "blocker" in status else None)


def _shard_coverage(score, config, progress):
    metadata = {}
    for field in ("shard_count", "shard_index", "shard_id", "parent_run_id", "aggregated_from_shards", "source_shard_run_ids"):
        value = _first(score.get(field), config.get(field), progress.get(field))
        if value is not None:
            metadata[field] = value
    scope = str(_first(score.get("case_scope"), config.get("case_scope"), "")).lower()
    uses_shards = ((_number(metadata.get("shard_count")) or 1) > 1 or "shard" in scope
                   or bool(metadata.get("aggregated_from_shards")) or bool(metadata.get("source_shard_run_ids")))
    validation = _pick(score.get("full_test_id_union_validation", {}), {
        "complete", "union_matches_full_test_ids", "expected_test_case_count", "unique_observed_case_count",
        "missing_case_count", "extra_case_count", "duplicate_case_count", "full_test_ids_sha256", "observed_union_ids_sha256",
    })
    expected = _number(validation.get("expected_test_case_count"))
    valid_union = (validation.get("complete") is True and validation.get("union_matches_full_test_ids") is True
                   and expected is not None and expected > 0 and validation.get("unique_observed_case_count") == expected
                   and validation.get("missing_case_count") == 0 and validation.get("extra_case_count") == 0
                   and validation.get("duplicate_case_count", 0) == 0)
    # P43 is one catalog setting with three separately scored native source
    # tests. A completed dataset remains a component even without shard flags.
    # The dedicated aggregate validates all 16,533 exact IDs, while preserving
    # dataset-specific AUROC/AP instead of inventing a pooled paper metric.
    component_setting = "P43" in (_task_ids(score) or _task_ids(config))
    dataset = _first(score.get("dataset"), config.get("dataset"))
    component_union = (valid_union and expected == 16533
                       and scope in {"native_source_test_union_separate_dataset_metrics",
                                     "complete_three_native_tests_separate_metrics"})
    coverage_complete = ((not uses_shards or valid_union)
                         and (not component_setting or component_union))
    return {
        **metadata, "uses_shards": uses_shards, "full_test_id_union_validation": validation,
        "uses_dataset_components": component_setting, "dataset_component": dataset,
        "complete_aggregate_union_verified": valid_union,
        "task_coverage_complete": coverage_complete,
        "partial_coverage_reason": ("P43 dataset component; complete 16,533-ID three-test union unverified"
                                    if component_setting and not component_union else
                                    "shard only; full test-ID union unverified" if not coverage_complete else None),
    }


def _run_state(scores, progress, planned, terminal, metrics):
    all_terminal = planned is not None and terminal is not None and terminal >= planned
    has_metrics = _has_metrics(metrics)
    statuses = scores.get("statuses", progress.get("statuses", {}))
    failures = sum(v for k, v in statuses.items() if k not in SUCCESS_STATUSES and _number(v) is not None)
    failures = max(failures, _number(scores.get("invalid_outputs")) or 0)
    stage = str(progress.get("stage", scores.get("stage", ""))).lower()
    if scores and has_metrics and all_terminal:
        return ("completed_scored_with_failures" if failures else "completed_scored"), failures
    if scores and has_metrics:
        return "partial_scored", failures
    if all_terminal or stage in {"generation_complete", "completed", "complete", "scored"}:
        return "generation_complete_unscored", failures
    if stage in {"failed", "error", "stopped", "cancelled", "blocked"}:
        return "failed_or_stopped", failures
    if progress:
        return "running" if stage == "running" or terminal else "pending", failures
    return "queued", failures


def _qualify_p29_split_coverage(runs):
    """One setting needs both fixed source splits; their metrics stay separate."""
    expected = {"id": 6989, "ood": 7883}
    groups = {}
    for run in runs:
        if run["task_ids"] != ["P29"]:
            continue
        split = run.get("native_split")
        validation = run["sharding"]["full_test_id_union_validation"]
        component_complete = (split in expected and run["task_coverage_complete"]
            and run["sharding"]["complete_aggregate_union_verified"]
            and validation.get("expected_test_case_count") == expected[split]
            and validation.get("unique_observed_case_count") == expected[split]
            and run["planned"] == expected[split] and run["completed"] == expected[split]
            and run["state"] in FINAL_STATES and run["task_specific_metrics"])
        run["native_split_coverage_complete"] = component_complete
        run["task_coverage_complete"] = run["sharding"]["task_coverage_complete"] = False
        run["sharding"]["partial_coverage_reason"] = "P29 needs both exact full ID6,989 and OOD7,883 source unions (14,872 total); one split or shard is partial setting coverage."
        identity = tuple(run.get(key) for key in ["model", "model_revision", "protocol_variant", "protocol_kind"])
        if component_complete and all(identity):
            groups.setdefault(identity, {}).setdefault(split, []).append(run)
    for splits in groups.values():
        # Never pick a better same-split run if multiple eligible executions
        # appear. Root can reconcile their identities without outcome selection.
        if set(splits) != set(expected) or any(len(values) != 1 for values in splits.values()):
            continue
        components = [splits[split][0] for split in expected]
        record = {"complete": True, "required_native_split_counts": expected,
                  "full_setting_case_count": sum(expected.values()),
                  "source_split_unions": {run["native_split"]: {"run_id": run["run_id"],
                      "validation": run["sharding"]["full_test_id_union_validation"]} for run in components},
                  "policy": "Both fixed source split unions validated separately under the same model/revision/variant. ID/OOD metrics remain separate; no pooled metric or average is created."}
        for run in components:
            run["task_coverage_complete"] = run["sharding"]["task_coverage_complete"] = True
            run["sharding"]["partial_coverage_reason"] = None
            run["full_setting_split_coverage_validation"] = record


def build_report(root: Path, generated_at: str | None = None):
    """Read only catalog/registry metadata, queue metadata and aggregate results."""
    root = Path(root)
    provenance, warnings = {}, []

    def read_json(path, default=None):
        path = Path(path)
        try:
            raw = (root / path).read_bytes()
        except FileNotFoundError:
            return default
        provenance[str(path)] = hashlib.sha256(raw).hexdigest()
        try:
            return json.loads(raw)
        except (ValueError, UnicodeDecodeError):
            warnings.append(f"Unreadable JSON snapshot: {path}; rerun after the writer completes.")
            return default

    catalog = read_json(CATALOG)
    if not isinstance(catalog, dict) or not isinstance(catalog.get("tasks"), list):
        raise ValueError(f"Missing or invalid source catalog: {CATALOG}")
    source_tasks = [t for t in catalog["tasks"] if t.get("family") != "General LLM controls" and not str(t.get("id", "")).startswith("G")]
    expected = catalog.get("counts", {}).get("biological_evaluation_settings", len(source_tasks))
    if len(source_tasks) != expected:
        warnings.append(f"Catalog biological task count {len(source_tasks)} differs from declared {expected}.")
    readiness_path = root / "reports/per_task_readiness.csv"
    readiness = {}
    if readiness_path.exists():
        raw = readiness_path.read_bytes()
        provenance["reports/per_task_readiness.csv"] = hashlib.sha256(raw).hexdigest()
        readiness = {r["id"]: r for r in csv.DictReader(io.StringIO(raw.decode()))}
    registry_path = root / "results/interpretation_notes.jsonl"
    interpretations = []
    if registry_path.exists():
        raw = registry_path.read_bytes()
        provenance["results/interpretation_notes.jsonl"] = hashlib.sha256(raw).hexdigest()
        for number, line in enumerate(raw.decode().splitlines(), 1):
            if not line.strip():
                continue
            try:
                entry = json.loads(line)
            except ValueError:
                warnings.append(f"Invalid interpretation metadata line {number}; skipped.")
                continue
            entry = _pick(entry, INTERPRETATION_FIELDS | {"actual_supplied_information"})
            entry["actual_supplied_information"] = _pick(entry.get("actual_supplied_information", {}), {
                "status", "benchmark_requests_submitted", "observed_model_input_fields", "run_id",
                "reference_answers_or_explanations_supplied", "request_hashes_verified", "solver_tools",
            })
            interpretations.append(entry)
    registry_by_run = {}
    for entry in interpretations:
        run_id = _first(entry.get("run_id"), entry.get("actual_supplied_information", {}).get("run_id"))
        if run_id:
            registry_by_run.setdefault(run_id, []).append(entry)

    queue_docs = {str(p.relative_to(root)): read_json(p.relative_to(root), {}) or {}
                  for p in sorted((root / "configs").glob("local_benchmark_queue*.json"))}
    queue_progress_docs = {str(p.relative_to(root)): read_json(p.relative_to(root), {}) or {}
                           for p in sorted((root / ".local").glob("local_benchmark_queue*/progress.json"))}
    queue = queue_docs.get("configs/local_benchmark_queue.json", {})
    queue_progress = queue_progress_docs.get(".local/local_benchmark_queue/progress.json", {})
    first_status = read_json("reports/local_evaluation_status.json", {}) or {}
    execution_review = read_json("reports/catalog_execution_review_2026-10-15.json", {}) or {}
    execution_by_task = {entry.get("id", entry.get("task_id")): entry for entry in execution_review.get("tasks", [])}
    protocol_hold = read_json("reports/labbench_protocol_review_hold.json", {}) or {}
    source_review_hold = read_json("reports/mutadescribe_source_review_hold.json", {}) or {}
    v04_qualification = read_json("reports/v04_output_format_qualification.json", {}) or {}
    vision_doc = read_json(VISION_INTEGRITY, {}) or {}
    recovery_doc = read_json(SOURCE_RECOVERY, {}) or {}
    gap_doc = read_json(POSTTRAIN_GAPS, {}) or {}
    p34_doc = read_json(P34_FEASIBILITY, {}) or {}
    nature_generation_doc = read_json(NATURE_GENERATION_FEASIBILITY, {}) or {}
    design_doc = read_json(DESIGN_FEASIBILITY, {}) or {}
    source_reviews = {}
    for entry in recovery_doc.get("tasks", []):
        task_id = entry.get("task_id")
        if task_id in {"P09", "P19", "P20", "P21", "P22", "P27", "V07"}:
            review = _pick(entry, {"task_id", "status", "task", "required_native_information", "reference_answer_source",
                "native_metric", "native_cases_verified", "official_release", "verified_facts", "blockers", "resolution",
                "execution_authorized", "inference_performed", "prepared_model_cases"})
            review.update(source_file=SOURCE_RECOVERY, source_sha256=provenance[SOURCE_RECOVERY],
                          report_created_at_utc=recovery_doc.get("created_at_utc"))
            source_reviews[task_id] = review
    for task_id in ["N04", "N05"]:
        entry = gap_doc.get(task_id)
        if isinstance(entry, dict):
            review = _pick(entry, {"status", "task_identity", "required_artifacts", "author_release_link", "required_input_contract",
                "metric_contract", "source_locator", "split_fallback_hazard", "missing", "no_substitution", "execution_authorized",
                "required_inputs", "native_metric_from_paper", "author_code_tree_audit", "upstream_artifacts_verified"})
            review.update(task_id=task_id, source_file=POSTTRAIN_GAPS, source_sha256=provenance[POSTTRAIN_GAPS],
                          report_date_utc=gap_doc.get("date_utc"),
                          publisher_source=_pick(gap_doc, {"source_code_repository", "source_code_revision", "paper_source"}))
            if entry.get("unauthenticated_observation"):
                review["unauthenticated_observation"] = _pick(entry["unauthenticated_observation"], {"url", "http_status", "sha256", "checked_utc"})
            source_reviews[task_id] = review
    if p34_doc.get("task_id") == "P34":
        oracle = p34_doc.get("oracle_and_metrics", {})
        source_reviews["P34"] = {
            "task_id": "P34", "status": p34_doc.get("status"),
            "reporting_state": "source_protocol_unresolved",
            "source_file": P34_FEASIBILITY, "source_sha256": provenance[P34_FEASIBILITY],
            "report_date_utc": p34_doc.get("date"),
            "required_native_information": "Full current protein, fixed source function/objective, native ESM-token position axis and all33 residue classes; exact source proposal/prior/sampler and fixed trained landscape oracle. A Qwen replacement head needs a prospectively frozen likelihood interface.",
            "native_metric": oracle.get("metrics"),
            "reference_answer_source": oracle.get("reference_source"),
            "native_split_contract": "Five permitted landscapes are a qualified subset; the sixth remains held. No full six-landscape completion is established.",
            "allowed_landscapes": p34_doc.get("allowed_landscapes", []),
            "entire_six_landscape_paper_setting_completed": p34_doc.get("entire_six_landscape_paper_setting_completed", False),
            "prediction_task_retained": p34_doc.get("conclusion", {}).get("prediction_task_retained", True),
            "missing_learned_head_is_not_task_exclusion": p34_doc.get("conclusion", {}).get("missing_learned_qwen_joint_head_is_not_a_task_exclusion"),
            "qualified_adapter_mathematically_possible": p34_doc.get("conclusion", {}).get("qualified_adapter_mathematically_possible"),
            "source_paper_protocol_differences": p34_doc.get("source_paper_protocol_differences", []),
            "full_five_budget_if_complete": oracle.get("full_five_budget_if_complete"),
            "likelihood_runtime_cost": _pick(p34_doc.get("likelihood_runtime_cost", {}), {
                "status", "exact_expression", "conditional_all_five_initial_length_unchanged_complete_label_evaluations",
                "conditional_all_five_initial_length_unchanged_prefix_free_event_evaluations", "http_qualification", "wall_clock", "base_weights_if_later_authorized_bytes"}),
            "blockers": p34_doc.get("remaining_blockers_or_decisions", []),
            "execution_authorized": False, "inference_performed": False, "prepared_model_cases": 0,
            "source_only_audit_not_execution": True,
        }
    for entry in nature_generation_doc.get("tasks", []):
        task_id = entry.get("task_id")
        if task_id not in {"P37", "P38"}:
            continue
        interpretation = entry.get("interpretation", {})
        review = _pick(entry, {"task_id", "status", "native_metrics", "natural_reference", "partial_native_metric_feasibility", "source_prompt_or_input"})
        review.update({
            "reporting_state": "source_protocol_unresolved",
            "source_file": NATURE_GENERATION_FEASIBILITY, "source_sha256": provenance[NATURE_GENERATION_FEASIBILITY],
            "report_date_utc": nature_generation_doc.get("created_at_utc"),
            "required_native_information": interpretation.get("information_supplied_to_solver"),
            "native_metric": "; ".join(entry.get("native_metrics", {}).keys()),
            "reference_answer_source": interpretation.get("reference_answer_source"),
            "native_split_contract": "Native generated cohort counts, sampling manifest and exact reference snapshot remain unrecovered. Illustrative prompts are not benchmark cases or a generation budget.",
            "blockers": entry.get("residual_blockers", []),
            "prediction_task_retained": nature_generation_doc.get("native_tasks_retained", True),
            "execution_authorized": False, "inference_performed": nature_generation_doc.get("inference_performed", False),
            "prepared_model_cases": 0, "source_only_audit_not_execution": True,
        })
        source_reviews[task_id] = review
    for entry in design_doc.get("tasks", []):
        task_id = entry.get("task_id")
        if task_id not in {"P35", "P36", "P39", "P40", "P41"}:
            continue
        review = _pick(entry, {"task_id", "status", "reporting_state", "task", "required_native_information", "native_metric",
            "reference_answer_source", "native_split_contract", "artifact_availability", "blockers", "prospective_feasibility", "publisher_source",
            "prediction_task_retained", "execution_authorized", "inference_performed", "prepared_model_cases", "native_dispatch_ready"})
        review.update(source_file=DESIGN_FEASIBILITY, source_sha256=provenance[DESIGN_FEASIBILITY],
                      report_created_at_utc=design_doc.get("created_at_utc"), source_only_audit_not_execution=True)
        source_reviews[task_id] = review
    configs_by_run, config_paths, run_queues = {}, {}, {}
    jobs = [(queue_path, job) for queue_path, document in queue_docs.items() for job in document.get("jobs", [])]
    for queue_path, job in jobs:
        path = job.get("config")
        if not path:
            continue
        # Configuration files are parsed for field names and metadata only. Never
        # follow input_file/review_file/scorer_reference_file or copy prompts.
        config = _pick(read_json(path, {}) or {}, CONFIG_FIELDS)
        if config.get("run_id"):
            configs_by_run[config["run_id"]] = config
            config_paths[config["run_id"]] = path
            run_queues.setdefault(config["run_id"], []).append(queue_path)
    # Terminal queue history also covers failures before a run manifest exists.
    # A historical row must match the config's exact run ID before it can alter
    # status; it never authorizes retries or changes inference configuration.
    queue_history = {}
    for progress_path, document in queue_progress_docs.items():
        finished = document.get("finished", {})
        if not isinstance(finished, dict):
            continue
        for config_path, record in finished.items():
            if not isinstance(record, dict) or _number(record.get("exit_code")) is None:
                continue
            config = _pick(read_json(config_path, {}) or {}, CONFIG_FIELDS)
            run_id = config.get("run_id")
            if not run_id or record.get("run_id") != run_id:
                warnings.append(f"Terminal queue history run/config mismatch: {progress_path}: {config_path}; status not applied.")
                continue
            configs_by_run.setdefault(run_id, config)
            config_paths.setdefault(run_id, config_path)
            queue_history.setdefault(run_id, []).append({"source_path": progress_path, "config_file": config_path,
                **_pick(record, {"run_id", "exit_code", "finished_at_utc"})})
    comparison_doc = read_json(COMPARISONS, {}) or {}
    comparisons = {}
    for entry in comparison_doc.get("tasks", []):
        comparisons[entry["task_id"]] = _pick(entry, {
            "published_baselines", "comparison_status", "comparability_requirements",
            "unverified_or_missing", "published_full_case_count", "released_public_case_count",
        })

    score_docs, progress_docs, score_paths, completion_docs = {}, {}, {}, {}
    for path in sorted((root / "results/runs").glob("*/scores.json")):
        relative = path.relative_to(root)
        doc = read_json(relative, {}) or {}
        run_id = doc.get("run_id", path.parent.name)
        score_docs[run_id] = doc
        score_paths[run_id] = str(relative)
    for path in sorted((root / "results/runs").glob("*/progress.json")):
        doc = read_json(path.relative_to(root), {}) or {}
        run_id = _first(doc.get("run_id"), doc.get("run"), path.parent.name)
        progress_docs[run_id] = doc
    for path in sorted((root / "results/runs").glob("*/completion.json")):
        completion_docs[path.parent.name] = read_json(path.relative_to(root), {}) or {}
    known_runs = set(score_docs) | set(configs_by_run) | set(registry_by_run) | set(queue_history)
    if first_status.get("run_id"):
        known_runs.add(first_status["run_id"])
    # Historic API progress lacks local model/task metadata and is not a local
    # completion. Preserve its existence without calling it an active local job.
    known_runs.update(k for k, v in progress_docs.items() if _task_ids(v) and v.get("model"))
    excluded = [
        {"run_id": k, "reason": "Progress has no exact local run/task metadata; excluded from local coverage.",
         "statuses": v.get("statuses", {})}
        for k, v in progress_docs.items() if k not in known_runs
    ]
    runs = []
    for run_id in sorted(known_runs):
        score = score_docs.get(run_id, {})
        progress = progress_docs.get(run_id, {})
        config = configs_by_run.get(run_id, {})
        registry_entries = registry_by_run.get(run_id, [])
        registry = registry_entries[0] if registry_entries else {}
        status = first_status if first_status.get("run_id") == run_id else {}
        task_ids = _task_ids(score) or _task_ids(config) or _task_ids(progress) or sorted({e["task_id"] for e in registry_entries})
        variant = _first(score.get("protocol_variant"), score.get("variant"), config.get("protocol_variant"), config.get("variant"), registry.get("protocol_variant"))
        metrics = score.get("metrics", {})
        primary_valid, primary_validity_basis = _primary_metric_validity(score)
        planned = _first(_number(score.get("planned")), _number(progress.get("planned")))
        statuses = score.get("statuses", progress.get("statuses", {}))
        status_total = sum(v for v in statuses.values() if _number(v) is not None) if statuses else None
        # A final scorer can be newer than the worker's last progress snapshot.
        terminal = _first(_number(score.get("finished")),
                          status_total if score.get("statuses") else None,
                          _number(score.get("completed")),
                          _number(progress.get("finished")), status_total)
        state, failures = _run_state(score, progress, planned, terminal, metrics)
        completion = completion_docs.get(run_id, {})
        terminal_checks = []
        if any(record["exit_code"] != 0 for record in queue_history.get(run_id, [])):
            terminal_checks.append("Matching terminal queue history records a nonzero exit code; this config is not retried.")
        if completion:
            if completion.get("generation_exit_code") is not None and completion["generation_exit_code"] != 0:
                terminal_checks.append("Terminal generation exit code is nonzero; available scored outputs remain visible as incomplete execution.")
            if completion.get("scoring_exit_code") is not None and completion["scoring_exit_code"] != 0:
                terminal_checks.append("Terminal completion records a failed scorer.")
            if score and completion.get("scoring_exit_code") is None:
                terminal_checks.append("Scores exist but terminal completion does not verify successful scoring.")
            expected_score = completion.get("scores_sha256")
            if expected_score and expected_score != provenance.get(score_paths.get(run_id)):
                terminal_checks.append("Terminal scores SHA-256 differs from the current aggregate score file.")
                warnings.append(f"Terminal score hash mismatch for {run_id}; completed coverage excluded.")
            expected_config = completion.get("configuration_sha256")
            if expected_config and config_paths.get(run_id) and expected_config != provenance.get(config_paths[run_id]):
                terminal_checks.append("Terminal configuration SHA-256 differs from the current queued config.")
                warnings.append(f"Terminal configuration hash mismatch for {run_id}; completed coverage excluded.")
        if terminal_checks:
            state = "failed_or_stopped"
        supplied = registry.get("actual_supplied_information", {})
        observed_fields = supplied.get("observed_model_input_fields", score.get("observed_model_input_fields", []))
        observed_interface = registry.get("input_interface") if supplied.get("status") == "dispatched" else None
        observed_modalities = _first(score.get("input_modalities"), _modalities(observed_fields, observed_interface))
        configured_modalities = _first(config.get("input_modalities"), _modalities(config.get("model_facing_fields", [])))
        sharding = _shard_coverage(score, config, progress)
        format_qualification = None
        if v04_qualification.get("run_id") == run_id and v04_qualification.get("task_id") in task_ids:
            format_qualification = _pick(v04_qualification, {
                "task_id", "run_id", "native_qualified_strict_accuracy", "prediction_only_format_audit",
                "protocol", "interpretation", "explanation_correctness", "raw_score_preserved", "score_sha256", "source",
            })
            format_qualification["source_file"] = "reports/v04_output_format_qualification.json"
            format_qualification["score_sha256_matches"] = v04_qualification.get("score_sha256") == provenance.get(score_paths.get(run_id))
            format_qualification["display_caveat"] = (
                "V04's zero score measures whole-final strict exact matching under the frozen original question-plus-image condition. "
                "The prediction-only format audit found 500 multiline final answers, 15–263 words each (median 70), with 487 using bold Markdown. "
                "This does not establish 500 incorrect clinical predictions or absence of visual evidence use. Explanation correctness is unassessed; score and parser remain unchanged."
            )
            if not format_qualification["score_sha256_matches"]:
                format_qualification["display_caveat"] = "Historical V04 output-format qualification has a score-hash mismatch with the current aggregate; reconcile versions before applying its 500-answer interpretation. This reporter performed no rescoring or score changes."
                warnings.append(f"Output-format qualification score hash does not match current aggregate for {run_id}; qualification requires version reconciliation.")
        input_integrity_qualification = None
        vision_rows = [row for row in vision_doc.get("audited_runs", []) if row.get("run_id") == run_id and row.get("task_id") in task_ids]
        if len(vision_rows) == 1:
            row = vision_rows[0]
            matches = row.get("score_sha256") == provenance.get(score_paths.get(run_id))
            input_integrity_qualification = {**row, "qualification_kind": "vision_source_and_request_integrity",
                "source_file": VISION_INTEGRITY, "source_sha256": provenance[VISION_INTEGRITY],
                "source_audit": vision_doc.get("source_audit"), "score_sha256_matches": matches,
                "pretraining_exposure": vision_doc.get("pretraining_exposure"),
                "evidence_read": "Compact aggregate metadata only; per-case proofs, original inputs, requests, answers and model reasoning are not opened by this reporter."}
            check_names = ["source_choices_and_target_mapping_verified", "actual_request_provenance_verified",
                           "no_extra_reference_fields_detected", "publisher_images_verified"]
            checks_passed = all(row.get(name) is True for name in check_names)
            input_integrity_qualification["source_checks_all_passed"] = checks_passed
            caveat = (f"Source choices/target mapping, publisher images and saved request provenance reconciled for {row.get('cases')} cases; no extra scorer-reference fields were detected in requests. "
                      if checks_passed else "The aggregate input-integrity audit reports unresolved source checks; inspect its recorded evidence. ")
            if row.get("task_id") == "B04":
                encoding = vision_doc.get("B04_native_wrapper_encoding", {})
                input_integrity_qualification["source_encoding_diagnostic"] = vision_doc.get("source_encoding_diagnostic")
                input_integrity_qualification["native_wrapper_encoding"] = encoding
                caveat += ("Local FigQA retained original publisher JPEG bytes. The pinned native author wrapper re-encodes images using PIL Image.save(); "
                           f"a diagnostic Pillow {encoding.get('diagnostic_pillow_version')} replay changed encoded bytes for {encoding.get('encoded_bytes_changed')}/{encoding.get('cases')} images "
                           f"and decoded RGB pixels for {encoding.get('decoded_pixels_changed')}/{encoding.get('cases')}. "
                           "Historical runtime/encoding equality is unknown and the accuracy effect is unassessed; this does not explain the score gap. ")
            else:
                caveat += "TableQA retained original publisher PNG images; no local case/image/target mapping mismatch was detected. "
            caveat += "Public pretraining exposure remains unknown, and these checks do not validate explanations or establish stronger reasoning."
            if not matches:
                caveat = "Historical vision source-integrity qualification has a score-hash mismatch with the current aggregate; reconcile versions before applying its case checks or encoding diagnosis. No rescoring was performed."
                warnings.append(f"Vision input-integrity qualification score hash mismatch for {run_id}; qualification requires version reconciliation.")
            input_integrity_qualification["display_caveat"] = caveat
        run = {
            "run_id": run_id, "task_ids": task_ids, "protocol_variant": variant,
            "protocol_kind": _first(score.get("reporting_protocol_kind"), config.get("reporting_protocol_kind"), _protocol_kind(variant)), "state": state,
            "protocol_classification_basis": "Explicit repository reporting nomenclature or frozen reporting_protocol_kind metadata; no task-demand/internal-computation inference.",
            "task_specific_metrics": len(task_ids) == 1 and _has_metrics(metrics) and primary_valid is True,
            "task_coverage_complete": sharding["task_coverage_complete"],
            "sharding": sharding, "source_queues": run_queues.get(run_id, []),
            "terminal_queue_history": queue_history.get(run_id, []), "terminal_status_qualifications": terminal_checks,
            "terminal_completion": _pick(completion, {"generation_exit_code", "generation_audit_exit_code", "scoring_exit_code",
                "finished_at_utc", "status", "configuration_sha256", "run_manifest_sha256", "scores_sha256", "retry_or_resampling"}),
            "model": _first(score.get("model"), config.get("model"), registry.get("model"), status.get("model")),
            "model_revision": _first(score.get("model_revision"), config.get("model_revision"), registry.get("model_revision")),
            "checkpoint_precision": _first(score.get("checkpoint_precision"), config.get("checkpoint_precision")),
            "case_scope": _first(score.get("case_scope"), config.get("case_scope"), "unspecified; consult frozen run protocol"),
            "native_split": _first(score.get("native_split"), config.get("native_split")),
            "planned": planned, "finished": terminal, "completed": _first(score.get("completed"), statuses.get("completed")),
            "parsed": score.get("parsed"), "invalid_outputs": score.get("invalid_outputs"),
            "failure_count": failures, "statuses": statuses, "finish_reasons": score.get("finish_reasons", {}),
            "held_before_inference": score.get("held_before_inference"),
            "metrics": metrics, "explanation_support_score": score.get("explanation_support_score"),
            "input_modalities": observed_modalities,
            "configured_input_modalities": configured_modalities,
            "modalities_basis": "explicit_score_metadata" if score.get("input_modalities") else "observed_field/interface_metadata_inference" if observed_modalities else "actual_dispatch_modality_unverified",
            "observed_model_input_fields": observed_fields,
            "configured_model_input_fields": config.get("model_facing_fields", []),
            "observed_input_interface": observed_interface,
            "source_scores": score_paths.get(run_id),
            "source_progress": f"results/runs/{run_id}/progress.json" if progress else None,
            "source_config": config_paths.get(run_id),
            "source_dataset_revision": _first(score.get("source_dataset_revision"), config.get("source_dataset_revision")),
            "source_code_revision": _first(score.get("source_code_revision"), config.get("source_code_revision")),
            "comparison_to_paper": score.get("comparison_to_paper"),
            "metric_protocol": score.get("metric_protocol"),
            "metric_counts": score.get("metric_counts"),
            "primary_metric_names": score.get("primary_metric_names"),
            "primary_metric_status": score.get("primary_metric_status"),
            "full_planned_primary_metrics_valid": primary_valid,
            "reported_full_planned_primary_metrics_valid": score.get("full_planned_primary_metrics_valid"),
            "primary_metric_validity_basis": primary_validity_basis,
            "full_native_metric_set_complete": _first(score.get("full_native_metric_set_complete"), config.get("full_native_metric_set_complete")),
            "confidence_diagnostics": score.get("confidence_diagnostics"),
            "output_format_qualification": format_qualification,
            "input_integrity_qualification": input_integrity_qualification,
            "strict_diagnostic_namespace": score.get("strict_diagnostic_namespace"),
            "native_decode_byte_equivalence_claimed": score.get("native_decode_byte_equivalence_claimed"),
            "scorer_sha256": score.get("scorer_sha256"),
            "scoring_protocol_sha256": score.get("scoring_protocol_sha256"),
            "contamination": score.get("contamination", "Pretraining exposure unknown."),
            "uncertainty": _pick(score, {"run_count", "repeats", "standard_error", "confidence_interval", "reported_std", "uncertainty_note"}),
            "progress_updated_at_utc": progress.get("updated_at_utc"),
            "scope_counts": {k: v for k, v in score.items() if k.startswith("total_public_") or k in {"public_case_count", "reviewed_case_count"}},
            "additional_failure_counts": {k: v for k, v in score.items() if k in {"errors", "error_count", "failed", "missing_outputs", "truncated", "truncations", "transport_errors"} and _number(v) is not None},
        }
        if not task_ids:
            warnings.append(f"Run {run_id} has no exact task ID join and is excluded from task completion counts.")
        if len(task_ids) > 1 and metrics:
            warnings.append(f"Run {run_id} has aggregate metrics across multiple tasks; no per-task completion inferred.")
        runs.append(run)

    _qualify_p29_split_coverage(runs)

    tasks = []
    for source in source_tasks:
        task_id = source["id"]
        ready = readiness.get(task_id, {})
        task_runs = [r for r in runs if task_id in r["task_ids"]]
        complete = [r for r in task_runs if r["state"] in FINAL_STATES and r["task_specific_metrics"] and r["task_coverage_complete"]]
        completed_shards = [r for r in task_runs if r["state"] in FINAL_STATES and not r["task_coverage_complete"]]
        native = [r for r in complete if r["protocol_kind"] == "native" and r.get("full_native_metric_set_complete") is not False]
        adapted = [r for r in complete if r["protocol_kind"] == "adapted"]
        execution = execution_by_task.get(task_id, {})
        reviewed_source = source_reviews.get(task_id)
        qualified_hold = _pick(protocol_hold, {"task_id", "stage", "total_public_cases", "review_complete", "reason", "known_held_case_ids", "remaining_cases", "provider_hold_unchanged"}) if protocol_hold.get("task_id") == task_id else None
        qualified_source_hold = None
        if task_id in source_review_hold.get("task_ids", []):
            qualified_source_hold = _pick(source_review_hold, {
                "recorded_at_utc", "task_ids", "stage", "triggered_agent", "exact_trigger_case_unknown",
                "inference_dispatched", "scope_status", "reason", "actual_model_generations",
            })
            qualified_source_hold["source_file"] = "reports/mutadescribe_source_review_hold.json"
            qualified_source_hold["classification_qualification"] = "Unreviewed source scope remains held; the exact triggering case is unknown. This hold does not classify every released descriptive case as prohibited."
        blocker = _catalog_blocker(execution) if execution else _native_blocker(ready.get("readiness", ""), ready.get("notes", ""))
        if reviewed_source:
            blocker = (reviewed_source.get("reporting_state") or
                       ("source_access_gated_case_review_pending" if task_id in {"P19", "P20", "P21", "P22"}
                        else "source_access_authentication_blocked" if task_id == "N04" else "source_protocol_unresolved"))
        if qualified_hold:
            blocker = "prohibited_or_held"
        if qualified_source_hold:
            blocker = state = "unreviewed_source_scope_held"
        elif blocker == "prohibited_or_held":
            state = blocker
        elif native:
            state = "completed_native_variant"
        elif any(r["state"] in {"running", "partial_scored"} for r in task_runs):
            state = "running"
        elif any(r["state"] == "generation_complete_unscored" for r in task_runs):
            state = "generation_complete_unscored"
        elif any(r["state"] == "queued" for r in task_runs):
            state = "queued"
        elif adapted:
            state = "completed_adapted_variant_native_incomplete"
        elif completed_shards:
            state = "partial_task_coverage"
        elif any(r["state"] in FINAL_STATES and r.get("full_planned_primary_metrics_valid") is False for r in task_runs):
            state = "scored_primary_metrics_undefined"
        elif any(r["state"] in FINAL_STATES and r.get("full_native_metric_set_complete") is False for r in task_runs):
            state = "scored_native_metric_set_incomplete"
        elif any(r["state"] == "failed_or_stopped" for r in task_runs):
            state = "failed_or_stopped"
        elif blocker in {"external_evaluator_unavailable", "external_evaluator_pending", "protocol_unavailable", "source_unavailable", "source_protocol_mismatch", "source_protocol_unresolved", "source_acquisition_pending", "native_training_regime_blocked", "native_protocol_setup_pending", "assay_scope_review_pending", "source_access_gated_case_review_pending", "source_access_authentication_blocked", "blocked"}:
            state = blocker
        elif str(execution.get("status", "")).startswith("prepared_verified") or "prepared_execution" in str(execution.get("status", "")):
            state = "prepared"
        elif "prepar" in ready.get("readiness", "") and blocker != "native_execution_not_prepared":
            state = "prepared"
        elif blocker == "adapter_required":
            state = "adapter_required"
        else:
            state = "not_prepared"
        native_blockers = []
        if not native:
            for run in task_runs:
                if run["terminal_status_qualifications"]:
                    native_blockers.append({"kind": "terminal_execution_failure", "run_id": run["run_id"],
                        "evidence": " ".join(run["terminal_status_qualifications"]),
                        "terminal_queue_history": run["terminal_queue_history"], "source": "Aggregate completion and matching queue terminal history only; no retry performed."})
            if qualified_source_hold:
                native_blockers.append({"kind": "unreviewed_source_scope_held", "evidence": qualified_source_hold.get("reason"),
                                        "source": qualified_source_hold["source_file"], "qualification": qualified_source_hold["classification_qualification"]})
            if qualified_hold:
                native_blockers.append({"kind": "input_review_hold", "evidence": qualified_hold.get("reason"), "source": "reports/labbench_protocol_review_hold.json", "qualification": qualified_hold.get("remaining_cases")})
            if completed_shards:
                native_blockers.append({"kind": "partial_source_coverage", "evidence": "Finished shards or dataset components do not establish the full test-ID union; a completed validated aggregate score is required."})
            for run in task_runs:
                if run.get("full_native_metric_set_complete") is False:
                    native_blockers.append({"kind": "native_metric_set_incomplete", "run_id": run["run_id"],
                        "evidence": "Only the declared qualified metric subset is available; unscored required native metrics remain null. This does not complete the full native protocol."})
                if run["state"] in FINAL_STATES and run["full_planned_primary_metrics_valid"] is False:
                    native_blockers.append({"kind": "full_planned_primary_metrics_undefined", "run_id": run["run_id"],
                        "evidence": "Execution completed on the declared cases but full-planned primary scoring is invalid/undefined. Finite parsed-only, strict-label, offline reference, auxiliary or count values do not complete the primary benchmark contract.",
                        "validity_basis": run["primary_metric_validity_basis"]})
            if reviewed_source:
                source_notes = reviewed_source.get("blockers", reviewed_source.get("missing", []))
                native_blockers.extend({"kind": blocker, "evidence": note, "source": reviewed_source["source_file"],
                                        "source_sha256": reviewed_source["source_sha256"], "qualified_metadata": True} for note in source_notes)
                if task_id in {"P19", "P20", "P21", "P22"}:
                    native_blockers.insert(0, {"kind": blocker, "evidence": "Official PFArena release recovered; unauthenticated schema access returned HTTP 401. No gated raw data downloaded or access terms accepted; task/case review remains pending.",
                                              "source": reviewed_source["source_file"], "qualified_metadata": True})
                if task_id == "V07":
                    native_blockers.append({"kind": "synthetic_fallback_not_benchmark_data", "evidence": "The source BenchmarkRunner creates synthetic placeholder rows if a benchmark JSON is absent. These are not valid Ryze component test data and cannot complete V07.", "source": reviewed_source["source_file"]})
                if task_id == "N04":
                    native_blockers.insert(0, {"kind": blocker, "evidence": "The author Drive release redirects unauthenticated access to Google sign-in. HTTP 200 is the sign-in page, not the native CSV test release; no random-split fallback or N01 substitution.", "source": reviewed_source["source_file"]})
            elif execution.get("blockers"):
                native_blockers.extend({"kind": blocker or "dated_execution_review_blocker", "evidence": note,
                                        "source": "reports/catalog_execution_review_2026-10-15.json", "qualified_metadata": True,
                                        "current_execution_takes_precedence": bool(task_runs)} for note in execution["blockers"])
            elif blocker and not qualified_hold:
                native_blockers.append({"kind": blocker, "evidence": ready.get("notes") or ready.get("readiness")})
            if not native_blockers:
                native_blockers.append({"kind": "no_completed_native_task_score", "evidence": "No completed task-specific native aggregate score in this snapshot."})
        tasks.append({
            "task_id": task_id, "task_name": ("Bio-posttrain MEDEA target selection" if task_id == "N05" and reviewed_source else source["task"]), "state": state,
            "native_variant_completed": bool(native), "adapted_variant_completed": bool(adapted),
            "completed_native_variants": list(dict.fromkeys(r["protocol_variant"] for r in native)),
            "completed_adapted_variants": list(dict.fromkeys(r["protocol_variant"] for r in adapted)),
            "run_ids": [r["run_id"] for r in task_runs],
            "completed_shard_run_ids": [r["run_id"] for r in completed_shards],
            "execution_review": _pick(execution, {"status", "blockers", "next_step", "prepared_or_downloaded_case_count", "native_dataset_identity_verified", "prepared_input_file", "comparison_limit"}),
            "qualified_input_review_hold": qualified_hold,
            "qualified_source_review_hold": qualified_source_hold,
            "qualified_native_source_review": reviewed_source,
            "result_qualifications": [qualification for r in task_runs for qualification in
                [r.get("output_format_qualification"), r.get("input_integrity_qualification")] if qualification],
            "native_metric": (_first(reviewed_source.get("native_metric"), reviewed_source.get("native_metric_from_paper"), reviewed_source.get("metric_contract"), source.get("metrics")) if reviewed_source else source.get("metrics")),
            "native_input_contract": (_first(reviewed_source.get("required_native_information"), reviewed_source.get("required_inputs"), reviewed_source.get("required_input_contract"), source.get("model_input")) if reviewed_source else source.get("model_input")),
            "native_split_contract": (_first(reviewed_source.get("native_split_contract"),
                "Exact adapted split/case-order manifest unresolved; see qualified native source review." if task_id in {"N04", "N05"} else None,
                source.get("split_configuration")) if reviewed_source else source.get("split_configuration")),
            "native_reference_evidence": (_first(reviewed_source.get("reference_answer_source"), "Exact adapted split/references are unrecovered; see qualified native source review.") if reviewed_source else source.get("reference_evidence")),
            "source_access_status": reviewed_source.get("status") if reviewed_source else source.get("access_status"),
            "source_url": (_first(reviewed_source.get("official_release", {}).get("dataset_url"), reviewed_source.get("author_release_link"),
                                   reviewed_source.get("publisher_source", {}).get("source_code_repository"), source.get("access_url")) if reviewed_source else source.get("access_url")),
            "original_catalog_contract": _pick(source, {"task", "metrics", "model_input", "split_configuration", "reference_evidence", "access_status", "access_url"}),
            "original_readiness": ready.get("readiness"), "readiness_notes": ready.get("notes"),
            "prepared_case_count": ready.get("prepared_case_count"),
            "native_completion_blockers": native_blockers,
            "interpretation_variants": [e for e in interpretations if e.get("task_id") == task_id],
            "published_comparison": comparisons.get(task_id, {"comparison_status": "not_available"}),
        })
    state_counts = {}
    for task in tasks:
        state_counts[task["state"]] = state_counts.get(task["state"], 0) + 1
    return {
        "schema_version": 1,
        "generated_at_utc": generated_at or datetime.now(timezone.utc).isoformat(),
        "scope": "All biological catalog settings; general controls excluded. Offline aggregate reporting only.",
        "coverage": {
            "catalog_settings": len(tasks), "expected_catalog_settings": expected,
            "settings_with_completed_native_variant": sum(t["native_variant_completed"] for t in tasks),
            "settings_with_completed_adapted_variant": sum(t["adapted_variant_completed"] for t in tasks),
            "settings_without_completed_native_variant": sum(not t["native_variant_completed"] for t in tasks),
            "settings_with_any_aggregate_scores": sum(any(r["source_scores"] for r in runs if t["task_id"] in r["task_ids"]) for t in tasks),
            "state_counts": state_counts,
        },
        "runs": runs, "tasks": tasks,
        "queue": {"configuration": _pick(queue, {"scope", "accept_more", "jobs"}),
                  "progress": _pick(queue_progress, {"stage", "active_run", "finished", "updated_at_utc", "gpu_ids", "openai_calls"})},
        "queues": {
            "configurations": [{"source_path": path, **_pick(doc, {"scope", "accept_more", "jobs"})} for path, doc in queue_docs.items()],
            "progress": [{"source_path": path, **_pick(doc, {"stage", "active_run", "finished", "updated_at_utc", "gpu_ids", "openai_calls", "queue"})} for path, doc in queue_progress_docs.items()],
            "gpu_metadata_caveat": "These are recorded queue/config GPU IDs; this offline reporter does not inspect live device allocation.",
        },
        "excluded_unmapped_progress": excluded,
        "published_comparison_source": COMPARISONS if comparison_doc else None,
        "published_comparison_references": comparison_doc.get("references", {}),
        "published_comparison_global_rules": comparison_doc.get("global_rules", []),
        "caveats": CAVEATS, "warnings": warnings, "source_sha256": provenance,
    }


def _cell(value):
    if value is None:
        return "unknown"
    if isinstance(value, (dict, list)):
        value = json.dumps(value, ensure_ascii=False, sort_keys=True)
    return str(value).replace("|", "\\|").replace("\n", " ")


def render_markdown(report):
    coverage = report["coverage"]
    lines = [
        "# Local biological evaluation results", "",
        f"Snapshot: {report['generated_at_utc']}", "",
        f"{coverage['settings_with_completed_native_variant']}/{coverage['catalog_settings']} settings have a completed native protocol variant; "
        f"{coverage['settings_with_completed_adapted_variant']} have a completed adaptation. "
        f"{coverage['settings_without_completed_native_variant']} still lack a completed native variant. These counts do not establish full paper replication.", "",
        "State counts: " + _cell(coverage["state_counts"]), "",
        "## Local runs", "",
        "| Task IDs | Run / variant | State | Model / revision | Terminal / planned | Failures / invalid / held | Task coverage |",
        "| --- | --- | --- | --- | --- | --- | --- |",
    ]
    for run in report["runs"]:
        lines.append("| " + " | ".join(map(_cell, [
            run["task_ids"], f"{run['run_id']} / {run['protocol_variant']}", run["state"],
            f"{run['model']} / {run['model_revision']}", f"{run['finished']} / {run['planned']}",
            f"{run['failure_count']} / {run['invalid_outputs']} / {run['held_before_inference']}",
            "declared variant scope" if run["task_coverage_complete"] else run["sharding"]["partial_coverage_reason"],
        ])) + " |")
    lines += ["", "Queues: " + _cell([q["source_path"] for q in report["queues"]["configurations"]]) + ". "
              + report["queues"]["gpu_metadata_caveat"], ""]
    for run in report["runs"]:
        if run["terminal_status_qualifications"]:
            lines += [f"- Terminal qualification for `{run['run_id']}`: {_cell(' '.join(run['terminal_status_qualifications']))} Queue history: {_cell(run['terminal_queue_history'])}."]
        if run["state"] in FINAL_STATES and run["full_planned_primary_metrics_valid"] is False:
            lines += [f"- `{run['run_id']}` completed execution; its full-planned primary score is undefined/invalid and does not count as valid benchmark completion. {_cell(run['primary_metric_validity_basis'])} Reported diagnostic values remain separate."]
    lines += ["", "Metrics retain their original names and units. Partial runs remain partial; undefined values remain null. Counts inside a metric object are retained as counts.", "",
              "| Task IDs | Run | Metric path | Value |", "| --- | --- | --- | --- |"]
    for run in report["runs"]:
        for path, value in _flatten_metrics(run["metrics"]):
            lines.append("| " + " | ".join(map(_cell, [run["task_ids"], run["run_id"], ".".join(path), json.dumps(value, ensure_ascii=False)])) + " |")
    lines += ["", "## Published comparisons for scored settings", ""]
    scored_ids = {task_id for run in report["runs"] if run["source_scores"] for task_id in run["task_ids"]}
    for task in report["tasks"]:
        if task["task_id"] not in scored_ids:
            continue
        comparison = task["published_comparison"]
        lines += [f"### {task['task_id']} — {task['task_name']}", "", f"Comparison status: {_cell(comparison.get('comparison_status'))}.", ""]
        for baseline in comparison.get("published_baselines", []):
            source = baseline.get("source_url")
            cite = f"[{baseline.get('source_locator', 'source')}]({source})" if source else "source unavailable"
            lines += [f"- {_cell(baseline.get('model'))}: `{json.dumps(baseline.get('metrics', {}), ensure_ascii=False, sort_keys=True)}`. "
                      f"Protocol/training: {_cell(baseline.get('protocol'))}. "
                      f"Cases: {_cell(baseline.get('test_case_count'))}; runs: {_cell(baseline.get('run_count'))}; "
                      f"reported dispersion: {_cell(baseline.get('reported_std'))}. {cite}."]
            for key in ("scope_note", "uncertainty_note"):
                if baseline.get(key):
                    lines += [f"  {_cell(baseline[key])}"]
        for note in comparison.get("comparability_requirements", []) + comparison.get("unverified_or_missing", []):
            lines += [f"- {_cell(note)}"]
        for run in report["runs"]:
            if task["task_id"] in run["task_ids"] and run["comparison_to_paper"]:
                lines += [f"- Local run scope: {_cell(run['comparison_to_paper'])}"]
            if task["task_id"] in run["task_ids"] and run.get("primary_metric_status"):
                lines += [f"- Primary scoring status: {_cell(run['primary_metric_status'])}; diagnostic namespace: {_cell(run.get('strict_diagnostic_namespace'))}. Native decoded-byte equivalence claimed: {_cell(run.get('native_decode_byte_equivalence_claimed'))}."]
            if task["task_id"] in run["task_ids"] and run.get("output_format_qualification"):
                lines += [f"- Result qualification: {_cell(run['output_format_qualification']['display_caveat'])}"]
            if task["task_id"] in run["task_ids"] and run.get("input_integrity_qualification"):
                lines += [f"- Source/input qualification: {_cell(run['input_integrity_qualification']['display_caveat'])}"]
        lines += [""]
    lines += ["## Coverage and blockers for every catalog setting", "",
              "Current aggregate scores/progress and matching terminal failure records take precedence over older readiness snapshots. Dated source-recovery audits qualify corrected native source contracts; the immutable original catalog fields and source hashes remain in the JSON. Preparation alone does not establish dispatch or completion. Native contracts below do not establish what was actually dispatched; exact observed/configured fields remain separate in the JSON.", "",
              "| ID | Setting | Current state | Native input contract / metric | Native completion blocker / result qualification | Published comparison |",
              "| --- | --- | --- | --- | --- | --- |"]
    for task in report["tasks"]:
        blockers = "; ".join(b["kind"] + ": " + str(b["evidence"]) for b in task["native_completion_blockers"]) or "none for this completed variant; paper-scope caveats remain"
        if task["result_qualifications"]:
            blockers += "; Result qualification: " + " ".join(row["display_caveat"] for row in task["result_qualifications"])
        if task["qualified_native_source_review"]:
            review = task["qualified_native_source_review"]
            blockers += "; Qualified source review: " + review["source_file"] + " (SHA-256 " + review["source_sha256"] + ")"
        comparison = task["published_comparison"]
        lines.append("| " + " | ".join(map(_cell, [task["task_id"], task["task_name"], task["state"],
            f"{task['native_input_contract']} / {task['native_metric']}", blockers,
            f"{comparison.get('comparison_status')}; {len(comparison.get('published_baselines', []))} published baselines"])) + " |")
    lines += ["", "## Interpretation and uncertainty", ""]
    lines.extend(f"- {note}" for note in report["caveats"])
    if report["warnings"]:
        lines += ["", "Snapshot warnings:", ""] + [f"- {warning}" for warning in report["warnings"]]
    lines += ["", "The JSON retains each executed/prepared interpretation variant, exact model revision, count/error metadata, observed versus configured input fields, source hashes and public comparison details. The original interpretation registry and first LitQA2 results are unchanged.", ""]
    return "\n".join(lines)


def render_metrics_csv(report):
    fields = ["task_id", "task_name", "task_state", "run_id", "run_state", "protocol_variant", "protocol_kind", "native_split",
              "task_coverage_complete", "native_split_coverage_complete", "full_setting_split_coverage_validation", "sharding", "source_queues",
              "model", "model_revision", "checkpoint_precision", "case_scope", "planned", "finished", "completed",
              "parsed", "invalid_outputs", "failure_count", "held_before_inference", "full_planned_primary_metrics_valid",
              "reported_full_planned_primary_metrics_valid", "primary_metric_validity_basis", "native_metric", "input_modalities",
              "full_native_metric_set_complete",
              "observed_model_input_fields", "configured_model_input_fields", "metric_name", "metric_path_json", "metric_value_json",
              "comparison_status", "published_baseline_count", "native_completion_blockers", "result_qualifications", "source_scores",
              "terminal_queue_history", "terminal_status_qualifications", "terminal_completion", "qualified_native_source_review"]
    buf = io.StringIO(newline="")
    writer = csv.DictWriter(buf, fieldnames=fields)
    writer.writeheader()
    for task in report["tasks"]:
        task_runs = [r for r in report["runs"] if task["task_id"] in r["task_ids"]] or [{}]
        for run in task_runs:
            metrics = list(_flatten_metrics(run.get("metrics", {}))) or [((), None)]
            for path, value in metrics:
                row = {key: run.get(key) for key in fields if key in run}
                row.update(task_id=task["task_id"], task_name=task["task_name"], task_state=task["state"],
                           run_state=run.get("state"), native_metric=task["native_metric"],
                           metric_name=".".join(path), metric_path_json=json.dumps(path),
                           metric_value_json=json.dumps(value, ensure_ascii=False) if path else "",
                           comparison_status=task["published_comparison"].get("comparison_status"),
                           published_baseline_count=len(task["published_comparison"].get("published_baselines", [])),
                           native_completion_blockers=task["native_completion_blockers"], result_qualifications=task["result_qualifications"],
                           qualified_native_source_review=task["qualified_native_source_review"])
                writer.writerow({key: json.dumps(value, ensure_ascii=False, sort_keys=True) if isinstance(value, (dict, list)) else value for key, value in row.items()})
    return buf.getvalue()


def write_report(root: Path, report):
    outputs = {
        "reports/LOCAL_SUITE_RESULTS.json": json.dumps(report, indent=2, ensure_ascii=False, sort_keys=True) + "\n",
        "reports/LOCAL_SUITE_RESULTS.md": render_markdown(report),
        "results/local_suite_metrics.csv": render_metrics_csv(report),
    }
    for name, content in outputs.items():
        path = Path(root) / name
        path.parent.mkdir(parents=True, exist_ok=True)
        with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", dir=path.parent, delete=False) as tmp:
            tmp.write(content)
            temporary = Path(tmp.name)
        temporary.replace(path)
    return list(outputs)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    report = build_report(args.root)
    outputs = write_report(args.root, report)
    print(json.dumps({"coverage": report["coverage"], "outputs": outputs, "warnings": report["warnings"]}, ensure_ascii=False))


if __name__ == "__main__":
    main()
