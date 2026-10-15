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
from pathlib import Path
import tempfile


CATALOG = "handoff/bio_eval_agent_handoff_2026-10-13/references/evaluation_catalog.json"
COMPARISONS = "reports/PUBLISHED_BENCHMARK_COMPARISONS_2026-10-15.json"
SUCCESS_STATUSES = {"completed", "cached", "success", "ok"}
FINAL_STATES = {"completed_scored", "completed_scored_with_failures"}
COUNT_METRICS = {"planned", "completed", "parsed", "invalid", "invalid_outputs", "missing", "held", "total"}
CONFIG_FIELDS = {
    "run_id", "task_id", "task_ids", "approved_task_ids", "model",
    "model_revision", "protocol_variant", "variant", "checkpoint_precision",
    "input_modalities", "model_facing_fields", "source_dataset_revision",
    "source_code_revision", "case_scope", "gpu_ids", "frozen_at_utc",
    "shard_count", "shard_index", "shard_id", "parent_run_id",
    "aggregated_from_shards", "source_shard_run_ids",
    "reporting_protocol_kind",
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
    return isinstance(metrics, dict) and any(
        key not in COUNT_METRICS and not key.startswith("n_") for key in metrics
    )


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
                   and validation.get("missing_case_count") == 0 and validation.get("extra_case_count") == 0)
    return {
        **metadata, "uses_shards": uses_shards, "full_test_id_union_validation": validation,
        "complete_aggregate_union_verified": valid_union,
        "task_coverage_complete": not uses_shards or valid_union,
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
    comparison_doc = read_json(COMPARISONS, {}) or {}
    comparisons = {}
    for entry in comparison_doc.get("tasks", []):
        comparisons[entry["task_id"]] = _pick(entry, {
            "published_baselines", "comparison_status", "comparability_requirements",
            "unverified_or_missing", "published_full_case_count", "released_public_case_count",
        })

    score_docs, progress_docs, score_paths = {}, {}, {}
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
    known_runs = set(score_docs) | set(configs_by_run) | set(registry_by_run)
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
        planned = _first(_number(score.get("planned")), _number(progress.get("planned")))
        statuses = score.get("statuses", progress.get("statuses", {}))
        status_total = sum(v for v in statuses.values() if _number(v) is not None) if statuses else None
        # A final scorer can be newer than the worker's last progress snapshot.
        terminal = _first(_number(score.get("finished")),
                          status_total if score.get("statuses") else None,
                          _number(score.get("completed")),
                          _number(progress.get("finished")), status_total)
        state, failures = _run_state(score, progress, planned, terminal, metrics)
        supplied = registry.get("actual_supplied_information", {})
        observed_fields = supplied.get("observed_model_input_fields", score.get("observed_model_input_fields", []))
        observed_interface = registry.get("input_interface") if supplied.get("status") == "dispatched" else None
        observed_modalities = _first(score.get("input_modalities"), _modalities(observed_fields, observed_interface))
        configured_modalities = _first(config.get("input_modalities"), _modalities(config.get("model_facing_fields", [])))
        sharding = _shard_coverage(score, config, progress)
        run = {
            "run_id": run_id, "task_ids": task_ids, "protocol_variant": variant,
            "protocol_kind": _first(score.get("reporting_protocol_kind"), config.get("reporting_protocol_kind"), _protocol_kind(variant)), "state": state,
            "protocol_classification_basis": "Explicit repository reporting nomenclature or frozen reporting_protocol_kind metadata; no task-demand/internal-computation inference.",
            "task_specific_metrics": len(task_ids) == 1 and _has_metrics(metrics),
            "task_coverage_complete": sharding["task_coverage_complete"],
            "sharding": sharding, "source_queues": run_queues.get(run_id, []),
            "model": _first(score.get("model"), config.get("model"), registry.get("model"), status.get("model")),
            "model_revision": _first(score.get("model_revision"), config.get("model_revision"), registry.get("model_revision")),
            "checkpoint_precision": _first(score.get("checkpoint_precision"), config.get("checkpoint_precision")),
            "case_scope": _first(score.get("case_scope"), config.get("case_scope"), "unspecified; consult frozen run protocol"),
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

    tasks = []
    for source in source_tasks:
        task_id = source["id"]
        ready = readiness.get(task_id, {})
        task_runs = [r for r in runs if task_id in r["task_ids"]]
        complete = [r for r in task_runs if r["state"] in FINAL_STATES and r["task_specific_metrics"] and r["task_coverage_complete"]]
        completed_shards = [r for r in task_runs if r["state"] in FINAL_STATES and not r["task_coverage_complete"]]
        native = [r for r in complete if r["protocol_kind"] == "native"]
        adapted = [r for r in complete if r["protocol_kind"] == "adapted"]
        execution = execution_by_task.get(task_id, {})
        qualified_hold = _pick(protocol_hold, {"task_id", "stage", "total_public_cases", "review_complete", "reason", "known_held_case_ids", "remaining_cases", "provider_hold_unchanged"}) if protocol_hold.get("task_id") == task_id else None
        blocker = _catalog_blocker(execution) if execution else _native_blocker(ready.get("readiness", ""), ready.get("notes", ""))
        if qualified_hold:
            blocker = "prohibited_or_held"
        if blocker == "prohibited_or_held":
            state = blocker
        elif native:
            state = "completed_native_variant"
        elif any(r["state"] in {"running", "partial_scored"} for r in task_runs):
            state = "running"
        elif any(r["state"] == "generation_complete_unscored" for r in task_runs):
            state = "generation_complete_unscored"
        elif any(r["state"] == "queued" for r in task_runs):
            state = "queued"
        elif completed_shards:
            state = "partial_task_coverage"
        elif adapted:
            state = "completed_adapted_variant_native_incomplete"
        elif any(r["state"] == "failed_or_stopped" for r in task_runs):
            state = "failed_or_stopped"
        elif blocker in {"external_evaluator_unavailable", "external_evaluator_pending", "protocol_unavailable", "source_unavailable", "source_protocol_mismatch", "source_protocol_unresolved", "source_acquisition_pending", "native_training_regime_blocked", "native_protocol_setup_pending", "assay_scope_review_pending", "blocked"}:
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
            if qualified_hold:
                native_blockers.append({"kind": "input_review_hold", "evidence": qualified_hold.get("reason"), "source": "reports/labbench_protocol_review_hold.json", "qualification": qualified_hold.get("remaining_cases")})
            if completed_shards:
                native_blockers.append({"kind": "shard_union_not_validated", "evidence": "Finished shards do not establish the full test-ID union; a completed validated aggregate score is required."})
            if execution.get("blockers"):
                native_blockers.extend({"kind": blocker or "dated_execution_review_blocker", "evidence": note,
                                        "source": "reports/catalog_execution_review_2026-10-15.json", "qualified_metadata": True,
                                        "current_execution_takes_precedence": bool(task_runs)} for note in execution["blockers"])
            elif blocker and not qualified_hold:
                native_blockers.append({"kind": blocker, "evidence": ready.get("notes") or ready.get("readiness")})
            if not native_blockers:
                native_blockers.append({"kind": "no_completed_native_task_score", "evidence": "No completed task-specific native aggregate score in this snapshot."})
        tasks.append({
            "task_id": task_id, "task_name": source["task"], "state": state,
            "native_variant_completed": bool(native), "adapted_variant_completed": bool(adapted),
            "completed_native_variants": [r["protocol_variant"] for r in native],
            "completed_adapted_variants": [r["protocol_variant"] for r in adapted],
            "run_ids": [r["run_id"] for r in task_runs],
            "completed_shard_run_ids": [r["run_id"] for r in completed_shards],
            "execution_review": _pick(execution, {"status", "blockers", "next_step", "prepared_or_downloaded_case_count", "native_dataset_identity_verified", "prepared_input_file", "comparison_limit"}),
            "qualified_input_review_hold": qualified_hold,
            "native_metric": source.get("metrics"), "native_input_contract": source.get("model_input"),
            "native_split_contract": source.get("split_configuration"),
            "native_reference_evidence": source.get("reference_evidence"),
            "source_access_status": source.get("access_status"), "source_url": source.get("access_url"),
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
            "declared variant scope" if run["task_coverage_complete"] else "shard only; full test-ID union unverified",
        ])) + " |")
    lines += ["", "Queues: " + _cell([q["source_path"] for q in report["queues"]["configurations"]]) + ". "
              + report["queues"]["gpu_metadata_caveat"], ""]
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
        lines += [""]
    lines += ["## Coverage and blockers for every catalog setting", "",
              "Current aggregate scores/progress take precedence over older readiness snapshots. Preparation alone does not establish dispatch or completion. Native contracts below do not establish what was actually dispatched; exact observed/configured fields remain separate in the JSON.", "",
              "| ID | Setting | Current state | Native input contract / metric | Native completion blocker | Published comparison |",
              "| --- | --- | --- | --- | --- | --- |"]
    for task in report["tasks"]:
        blockers = "; ".join(b["kind"] + ": " + str(b["evidence"]) for b in task["native_completion_blockers"]) or "none for this completed variant; paper-scope caveats remain"
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
    fields = ["task_id", "task_name", "task_state", "run_id", "run_state", "protocol_variant", "protocol_kind", "task_coverage_complete", "sharding", "source_queues",
              "model", "model_revision", "checkpoint_precision", "case_scope", "planned", "finished", "completed",
              "parsed", "invalid_outputs", "failure_count", "held_before_inference", "native_metric", "input_modalities",
              "observed_model_input_fields", "configured_model_input_fields", "metric_name", "metric_path_json", "metric_value_json",
              "comparison_status", "published_baseline_count", "native_completion_blockers", "source_scores"]
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
                           native_completion_blockers=task["native_completion_blockers"])
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
