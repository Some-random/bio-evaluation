#!/usr/bin/env python3
"""Build the 57-setting status tracker from aggregate evidence; no model calls."""
from __future__ import annotations

import argparse
from collections import Counter
from datetime import datetime
import hashlib
import json
import math
from pathlib import Path
from zoneinfo import ZoneInfo

PACIFIC = ZoneInfo("America/Los_Angeles")
CATEGORIES = {
    "done": "Done: defined score for the declared evaluated condition",
    "running": "Running generation",
    "queued": "Queued for generation in the frozen runtime",
    "agent_work": "Doable agent work not finished",
    "user_held": "Held at the user's request",
    "provider_held": "Biological/provider interruption or restriction",
    "impossible": "Whole setting established impossible",
}
SHORT_LABELS = {"done": "Done", "running": "Running", "queued": "Queued", "agent_work": "Agent work", "user_held": "User held", "provider_held": "Provider held", "impossible": "Impossible"}
AGENT_ACTIONS = {
    "P04": ("Inventory the acquired 520-case test LMDB, review assay eligibility, isolate targets and freeze a scalar delivery/scoring contract.", ".local/source_acquisition_2026-10-19/prediction_datasets/summary.json", "Source archive acquired; assay eligibility and runtime preparation remain unfinished."),
    "P05": ("Review the available FLIP AAV assay scope, isolate test inputs/targets and freeze scalar delivery and scoring.", "reports/catalog_extended_preparation.json", "Released inputs available; eligibility review and execution preparation unfinished."),
    "P17": ("Review permissible assay scopes in the acquired ProteinGym release and implement a version-matched, full-denominator score adapter.", ".local/source_acquisition_2026-10-19/prediction_datasets/summary.json", "217 released assay CSVs acquired; reviewed execution scope remains unfinished."),
    "P19": ("Integrate the prepared 34-assay subset into the central runtime and pass its three synthetic delivery checks; independently review the remaining 77 assays while preserving 12 holds.", ".local/catalog_execution_2026-10-20/tasks/P19/readiness.json", "Required sources available; full coverage limited by unfinished review and existing case holds."),
    "P21": ("Prepare permitted T3 anchor and candidate inputs from the 67 acquired tables, isolate target scores, and validate complete ranking delivery.", ".local/source_recovery_round2_2026-10-19/pfarena/native_preflight/status.json", "Required source tables acquired; eligibility, input isolation and runtime integration unfinished."),
    "P22": ("Prepare permitted T4 component-context and candidate inputs from the 29 acquired pairs, isolate target scores, and validate complete ranking delivery.", ".local/source_recovery_round2_2026-10-19/pfarena/native_preflight/status.json", "All 29 context/target pairs acquired; eligibility, isolation and runtime integration unfinished."),
    "P27": ("Freeze a defensible available protein-description adaptation with fixed cohort/reference preprocessing; retain exact temporal NatureLM condition as unavailable.", ".local/source_recovery_round2_2026-10-19/paper_artifacts/PUBLIC_SUMMARY.json", "Exact native NCBI dates/accession manifest not found in audited author releases; labelled adaptation remains possible."),
    "P34": ("Integrate the acquired encoder and five existing heads with the released optimization/scoring contract and explicit failure handling; preserve the held sixth landscape.", "reports/SOURCE_ACQUISITION_PROGRESS_2026-10-19.json", "Existing evaluator assets acquired; released-code algorithm and runtime implementation unfinished; no new training."),
    "P35": ("Freeze the qualified corpus condition, run retained/rejected PDB accounting, review corpus scope and pass retrieval delivery checks using the acquired existing checkpoint.", ".local/catalog_execution_2026-10-20/tasks/P35/readiness.json", "Five released query rankings are feasible. The release provides no relevance gold or aggregate correctness metric; do not invent accuracy."),
    "P37": ("Assemble and validate an isolated OmegaFold2 runtime/checkpoint, then pass an independent development gate for the declared released-code condition.", ".local/catalog_execution_2026-10-20/tasks/P37/readiness.json", "Matching released-code evaluator assets acquired; exact native sampling and 50% clustering condition unavailable in inspected releases."),
    "P38": ("Validate NetSolP-D runtime, acquire the available ProtT5 encoder for the separate thermal proxy, and freeze independent generation/delivery contracts without training heads.", ".local/catalog_execution_2026-10-20/tasks/P38/readiness.json", "Exact SFM property heads/reference cohort unavailable in inspected releases; distinct available proxy conditions prepared."),
    "P39": ("Freeze a clearly labelled available structural case-study condition and its complete selection/denominator contract using acquired evaluator assets; report proxy evidence without invented binding accuracy.", "reports/REMAINING_DESIGN_SOURCE_FEASIBILITY_2026-10-15.json", "Exact native cohort, selection manifest and scoring contract unreleased in inspected sources; qualitative adaptation remains possible."),
    "P40": ("Independently review the 60 cases and implement a solver adapter that preserves permitted geometric context while hiding target residue identities and coordinates.", ".local/catalog_execution_2026-10-20/tasks/P40/status.json", "60 current-structure mappings/masks prepared; exact historical processed bytes not certified; current-structure adaptation available."),
    "P41": ("Assemble the available released-demo structural runtime and its masking/scoring adapter; document differences from the unreleased native holdout.", "reports/REMAINING_DESIGN_SOURCE_FEASIBILITY_2026-10-15.json", "Released checkpoints/vendor assets and demos acquired; exact SAbDab holdout, masks and full benchmark aggregation unavailable in inspected releases."),
    "V07": ("Review the 2,215 question/full-deck scopes, run actual processor expansion and 20-image context checks, then pass the independent delivery gate.", ".local/catalog_execution_2026-10-20/tasks/V07/status.json", "All 8,000 page identities materialized/hash-verified; mixed original/processed image adaptation available; exact Table 3 condition unavailable."),
}
USER_HOLDS = {
    "P33": "New head training remains held. Search already released matching heads and prepare metadata; a different training scope requires a user decision.",
    "V06": "Replacement external judge remains held. Solver packaging can proceed; a scoring/judge choice requires a user decision.",
    "P44": "Replacement external judge remains held. Prepare available evidence/rubric metadata; a scoring/judge choice requires a user decision.",
}
PROVIDER_HOLDS = {"P18", "B06", "P20", "P30", "P31", "P32", "P36"}


def load(path: Path):
    return json.loads(path.read_text()) if path.is_file() else None


def timestamp(data):
    if not isinstance(data, dict):
        return None
    return next((data[k] for k in ("scored_at_pacific", "updated_at_pacific", "at_pacific", "finished_at_pacific", "generated_at_pacific", "frozen_at_pacific", "observed_at_pacific") if data.get(k)), None)


def age_seconds(value, now):
    if not value:
        return None
    try:
        dt = datetime.fromisoformat(value.replace("Z", "+00:00"))
        return round((now - dt).total_seconds()) if dt.tzinfo else None
    except (TypeError, ValueError):
        return None


def score_defined(data):
    if not isinstance(data, dict):
        return False
    if any(data.get(key) is False for key in ("all_case_primary_available", "full_primary_metric_defined", "full_benchmark_score_defined", "full_planned_primary_metrics_valid")):
        return False
    metrics = data.get("metrics", data)
    values = [metrics.get(key) for key in ("spearman", "accuracy_percent", "accuracy", "auroc", "average_precision", "fmax", "ap", "AP", "Fmax", "auprc@micro", "f1_max")]
    values.append(data.get("primary_metric_value"))
    if "auprc@micro" in metrics or "f1_max" in metrics:
        return all(isinstance(metrics.get(key), (int, float)) and not isinstance(metrics.get(key), bool) and math.isfinite(metrics[key]) for key in ("auprc@micro", "f1_max"))
    return any(isinstance(value, (int, float)) and not isinstance(value, bool) and math.isfinite(value) for value in values)


def build(root: Path):
    now = datetime.now(PACIFIC)
    table_path = root / "reports/EVALUATION_DECISION_TABLE.json"
    table = load(table_path)
    retained = table["retained_setting_ids"]
    assert len(retained) == len(set(retained)) == 57
    table_rows = table["rows"]
    names = {r["task_id"]: r["task"] for r in table_rows}
    task_root = root / ".local/catalog_execution_2026-10-20/tasks"
    queue = root / ".local/catalog_execution_2026-10-20/runtime/queue"
    pool_path = root / ".local/catalog_execution_2026-10-20/runtime/status.json"
    pool = load(pool_path) or {}
    pool_age = age_seconds(timestamp(pool), now)
    pool_fresh = pool_age is not None and pool_age <= 180 and pool.get("stage") == "serving_task_queue"
    historic_done = {r["task_id"] for r in table_rows if r.get("source_row_category") == "completed_rows"}
    evidence_records = {}

    def evidence(relative):
        path = root / relative
        if relative not in evidence_records:
            raw = path.read_bytes() if path.is_file() else None
            data = load(path) if raw and path.suffix == ".json" else None
            evidence_records[relative] = {
                "path": relative,
                "available": raw is not None,
                "sha256": hashlib.sha256(raw).hexdigest() if raw else None,
                "recorded_at_pacific": timestamp(data),
                "observed_at_pacific": now.isoformat(),
            }
        return evidence_records[relative]

    def relative(path):
        return str(path.relative_to(root))

    rows = []
    for task in retained:
        metadata = task_root / task
        completion_path = metadata / "runtime/benchmark/completion.json"
        progress_path = metadata / "runtime/benchmark/progress.json"
        completion, progress = load(completion_path), load(progress_path)
        direct = completion or progress
        row = {
            "task_id": task,
            "task_name": names[task],
            "category": None,
            "substatus": None,
            "status": None,
            "next_action": None,
            "decision_needed": None,
            "exact_native_condition_availability": "A score for the declared evaluated scope does not establish matched-paper reproduction.",
            "whole_setting_established_impossible": False,
            "observed_at_pacific": now.isoformat(),
            "evidence_recorded_at_pacific": None,
            "evidence_paths": [],
            "runtime": None,
            "prepared_benchmark_planned": {"P06": 1366, "P07": 27217, "P08": 12851, "P12": 1919, "P13": 3416, "P14": 3416, "P15": 3416}.get(task),
            "score": None,
            "scope_notes": [],
        }
        if direct:
            row["runtime"] = {k: direct.get(k) for k in ("run_id", "planned", "attempted_confirmed", "terminal", "responses_saved", "delivery_passed", "transport_errors", "http_errors", "response_errors", "truncations", "empty_finals", "refusals", "prediction_lock_sha256")}
            row["runtime"]["recorded_at_pacific"] = timestamp(direct)
            row["runtime"]["age_seconds_at_observation"] = age_seconds(timestamp(direct), now)
            row["runtime"]["sealed_complete"] = completion is not None
            row["runtime"]["unsealed_counts_are_lower_bounds"] = completion is None
            row["evidence_paths"].append(relative(completion_path if completion else progress_path))

        score_candidates = [metadata / "runtime/benchmark/scores.json", metadata / "runtime/benchmark/scoring_repair_v1/scores.json", metadata / "scores.json"]
        def consistent_score(path):
            candidate = load(path)
            if not score_defined(candidate):
                return False
            if completion:
                planned = completion.get("planned")
                if not isinstance(planned, int) or not planned or completion.get("all_passed") is not True:
                    return False
                if any(completion.get(key) != planned for key in ("terminal", "responses_saved", "delivery_passed")):
                    return False
                if candidate.get("prediction_lock_sha256") != completion.get("prediction_lock_sha256"):
                    return False
                lock_path = metadata / "runtime/benchmark/prediction_lock.json"
                if not lock_path.is_file() or hashlib.sha256(lock_path.read_bytes()).hexdigest() != completion.get("prediction_lock_sha256"):
                    return False
                if candidate.get("config_sha256") and completion.get("config_sha256") and candidate["config_sha256"] != completion["config_sha256"]:
                    return False
                for container in (candidate, candidate.get("metrics", {})):
                    if container.get("planned") is not None and container["planned"] != planned:
                        return False
                    if any(container.get(key) is not None and container[key] != planned for key in ("parsed", "valid_predictions", "valid_vectors")):
                        return False
                    if any(container.get(key, 0) != 0 for key in ("invalid", "missing", "invalid_or_missing", "invalid_or_missing_vectors")):
                        return False
            elif task == "P09":
                source_completion = load(task_root / "P08/runtime/benchmark/completion.json") or {}
                source_lock = task_root / "P08/runtime/benchmark/prediction_lock.json"
                metrics = candidate.get("metrics", {})
                if not source_lock.is_file() or hashlib.sha256(source_lock.read_bytes()).hexdigest() != candidate.get("prediction_lock_sha256"):
                    return False
                if source_completion.get("prediction_lock_sha256") != candidate.get("prediction_lock_sha256") or source_completion.get("all_passed") is not True:
                    return False
                if candidate.get("prediction_source_config_sha256") != source_completion.get("config_sha256"):
                    return False
                if metrics.get("planned") != source_completion.get("planned") or metrics.get("valid_predictions") != metrics.get("planned") or metrics.get("invalid_or_missing") != 0:
                    return False
            return True

        score_path = next((p for p in score_candidates if consistent_score(p)), None)
        if score_path:
            score = load(score_path)
            row.update(category="done", substatus="defined_score", status="Scored complete declared condition.", next_action="Preserve sealed predictions and score; reconcile/publicly publish this tracker and report metadata.")
            row["score"] = {k: score.get(k) for k in ("run_id", "protocol_variant", "scored_at_pacific", "planned", "spearman", "metrics", "all_case_primary_available", "prediction_lock_sha256", "interpretation") if k in score}
            row["evidence_paths"].append(relative(score_path))
            row["evidence_paths"].append(relative(metadata / "runtime/benchmark/prediction_lock.json") if completion else ".local/catalog_execution_2026-10-20/tasks/P08/runtime/benchmark/prediction_lock.json")
            score_run = score.get("run_id")
            public_score = root / "results/runs" / str(score_run) / "scores.json"
            public_matching_rows = [r for r in table_rows if r["task_id"] == task and r.get("run_id") == score_run and r.get("source_scores") and (root / r["source_scores"]).is_file()]
            row["public_evidence_path"] = public_matching_rows[0]["source_scores"] if public_matching_rows else (relative(public_score) if public_score.is_file() else "reports/CATALOG_STATUS.json")
            if task == "P09":
                row["exact_native_condition_availability"] = "Original NatureLM binary conversion/test labels unavailable in inspected author releases. Completed declared >1.0 rule-derived adaptation reuses sealed P08 predictions."
                row["scope_notes"].append("53.28768189245972% accuracy (6848/12851); no extra model generation; not native NatureLM label certification.")
        elif task in historic_done:
            originals = [r for r in table_rows if r["task_id"] == task and r.get("source_row_category") == "completed_rows"]
            row.update(category="done", substatus="retained_declared_score", status="Defined retained score for the declared evaluated condition.", next_action="Preserve existing scores and qualifications; no new generation is pending for this setting.")
            row["score"] = [{k: r.get(k) for k in ("run_id", "dataset", "protocol_variant", "score_display", "case_scope", "source_scores", "source_score_sha256")} for r in originals]
            row["evidence_paths"].append("reports/EVALUATION_DECISION_TABLE.json")
            row["evidence_paths"].extend(r["source_scores"] for r in originals if r.get("source_scores"))
            row["scope_notes"] = sorted({r.get("case_scope", "Declared evaluated scope") for r in originals})
            if task in {"P01", "V01", "V02", "V03", "V04", "V05"}:
                row["scope_notes"].append("Retained metrics exist; missing historical raw archives limit further recovery/diagnostics, not the existence of the retained score.")
            if task == "B08":
                row["scope_notes"].append("Separate uniform-16K 33-case proposal remains proposed/not dispatched; it is not an active remaining queue.")
        elif task in {"P07", "P08"} and completion:
            row.update(category="agent_work", substatus="offline_scoring_repair", status="Complete new generation sealed; defined score still needs an offline scoring repair.", next_action="Complete once-only offline scoring against the sealed prediction lock, preserving failed attempt evidence; no regeneration.")
            row["exact_native_condition_availability"] = "Released full test and native correlation formula available; new nonthinking constrained-scalar condition is separate from historical generation."
        elif task in {"P12", "P13", "P14", "P15"}:
            grant = queue / f"10_{task}_benchmark.grant.json"
            started = queue / f"10_{task}_benchmark.started.json"
            finished = queue / f"10_{task}_benchmark.finished.json"
            row["exact_native_condition_availability"] = "Released test and native AP/Fmax scorer available; dense confidence-vector delivery is a separately frozen new condition."
            progress_fresh = direct and age_seconds(timestamp(direct), now) is not None and age_seconds(timestamp(direct), now) <= 600
            pool_client_active = pool_fresh and f"10_{task}_benchmark" in pool.get("active_clients", [])
            if direct and not completion and started.exists() and not finished.exists() and (progress_fresh or pool_client_active):
                row.update(category="running", substatus="generation_live_evidence", status="Direct generation progress and frozen started grant; recent progress or fresh pool active-client evidence confirms activity.", next_action="Continue the existing one-attempt cohort, seal every outcome, then run native offline scoring after closure.")
                row["evidence_paths"].append(relative(started))
                if pool_client_active:
                    row["evidence_paths"].append(relative(pool_path))
            elif grant.exists() and not started.exists():
                row.update(category="queued", substatus="frozen_grant_not_started", status="Frozen authorized runtime grant queued; no started record or progress observed.", next_action="Existing runtime starts this grant when a client slot opens; no new permission required.")
                row["evidence_paths"].append(relative(grant))
                row["scope_notes"].append("No progress is not proof of zero requests. This queue classification uses the frozen grant and absence of a started record, not filename response counts.")
            else:
                row.update(category="agent_work", substatus="runtime_observation_or_scoring_needed", status="Runtime evidence needs reconciliation; do not infer current running state from the old controller.", next_action="Inspect direct runner/process and seal evidence; resume only the existing authorized one-attempt queue or score a completed seal.")
        elif task in AGENT_ACTIONS:
            action, source, availability = AGENT_ACTIONS[task]
            row.update(category="agent_work", substatus="implementation_review_preparation", status="Doable preparation/implementation remains unfinished; not in the live generation queue.", next_action=action, exact_native_condition_availability=availability)
            row["evidence_paths"].append(source)
            row["scope_notes"].append("Already authorized agent work; an internal exact frozen grant is an engineering gate, not another broad user permission request.")
            if task == "P35":
                row["scope_notes"].append("Rankings can be produced. A new aggregate correctness metric would require a separate source-grounded research decision; qualitative evidence is not scored accuracy.")
            if task == "V07":
                row["evidence_paths"].append(".local/catalog_execution_2026-10-20/tasks/V07/materialization_resume_20261020_v1/completion.json")
        elif task in USER_HOLDS:
            row.update(category="user_held", substatus="explicit_exception_held", status="User explicitly left this exception on hold.", next_action=USER_HOLDS[task], decision_needed=USER_HOLDS[task])
            row["exact_native_condition_availability"] = "Required training/judge exception remains held; source or solver preparation does not itself complete the score."
            row["evidence_paths"] = ["AGENTS.md", f".local/catalog_execution_2026-10-20/tasks/{task}/task.json"]
        elif task in PROVIDER_HOLDS:
            row.update(category="provider_held", substatus="no_retry_or_reroute", status="Biological/provider restriction or interrupted review remains held.", next_action="Preserve completed evidence and holds; do not retry, rephrase or reroute the interrupted/flagged action. Continue only separate permitted offline metadata/scoring work.", decision_needed="Requires resolution of the applicable provider/scope restriction; a simple user continuation instruction does not remove it.")
            row["exact_native_condition_availability"] = "Source availability is separate from this execution/review hold; no claim that the whole source corpus is prohibited or missing."
            row["evidence_paths"] = ["AGENTS.md", f".local/catalog_execution_2026-10-20/tasks/{task}/task.json"]
            status = metadata / "status.json"
            if status.exists():
                row["evidence_paths"].append(relative(status))
            if task == "P36":
                row["scope_notes"].append("Only historical 59-response partial evidence is generated. Extension preserved 188 prepared inputs, with 5604 unreviewed; later interruption overrides the older continue-from-index-256 checkpoint instruction.")
                row["evidence_paths"].append(".local/catalog_execution_2026-10-20/tasks/P36/review_summary_v2.json")
        else:
            raise AssertionError(f"Unclassified retained setting: {task}")

        row["evidence_paths"] = list(dict.fromkeys(row["evidence_paths"]))
        for item in row["evidence_paths"]:
            evidence(item)
        primary = evidence_records[row["evidence_paths"][0]]
        row["evidence_recorded_at_pacific"] = primary["recorded_at_pacific"]
        if row["runtime"]:
            row["evidence_recorded_at_pacific"] = row["runtime"]["recorded_at_pacific"]
        if row["evidence_recorded_at_pacific"] is None:
            row["scope_notes"].append("Primary source has no embedded timestamp; this read verifies availability, not a fresh execution heartbeat.")
        if not row.get("public_evidence_path"):
            row["public_evidence_path"] = next((item for item in row["evidence_paths"] if not item.startswith(".local/") and evidence_records[item]["available"]), "reports/CATALOG_STATUS.json")
        rows.append(row)

    counts = {key: sum(row["category"] == key for row in rows) for key in CATEGORIES}
    assert sum(counts.values()) == len(rows) == 57
    assert {row["task_id"] for row in rows} == set(retained)
    assert all(row["category"] in CATEGORIES and row["next_action"] and row["evidence_paths"] for row in rows)
    controller = load(root / ".local/catalog_execution_2026-10-20/control/status.json")
    controller_time = timestamp(controller)
    supervisor_path = root / ".local/catalog_execution_2026-10-20/control/driver_supervisor_status.json"
    supervisor = load(supervisor_path) or {}
    supervisor_age = age_seconds(timestamp(supervisor), now)
    result = {
        "schema_version": 1,
        "generated_at_pacific": now.isoformat(),
        "timezone": "America/Los_Angeles",
        "role": "exhaustive_57_setting_evidence_tracker_not_dispatch_authorization",
        "retained_setting_count": 57,
        "counts": counts,
        "category_definitions": CATEGORIES,
        "agent_work_breakdown": dict(Counter(row["substatus"] for row in rows if row["category"] == "agent_work")),
        "full_catalog_complete": counts["done"] == 57,
        "definitions": {
            "done": "At least one retained defined score for that setting's declared evaluated condition; does not mean every published case, native paper replication, high performance, or rationale validity.",
            "queued": "An exact frozen generation grant exists and no started record/progress is observed; an assignment in a planning registry is not an execution queue.",
            "agent_work": "The next listed step can be advanced under existing authority. It can include review and a later exclusion; it is not a promise that every case is eligible or all native artifacts exist.",
            "impossible": "Requires evidence that the whole setting cannot be pursued; missing exact native artifacts alone do not make a labelled available adaptation impossible.",
            "counts": "Each retained setting appears once. Development panels, OpenAI comparison conditions, archived BioReason settings and the historical 17145-case continuation are not additional settings.",
            "runtime": "Direct progress/completion contents are used; unsealed counts are lower bounds. Missing progress is unknown, not zero calls. No response filename counts used.",
        },
        "freshness": {
            "old_decision_table_generated_at_pacific": table.get("generated_at_pacific"),
            "controller_recorded_at_pacific": controller_time,
            "controller_age_seconds": age_seconds(controller_time, now),
            "controller_is_live_evidence_only_if_recent": age_seconds(controller_time, now) is not None and age_seconds(controller_time, now) <= 180,
            "pool_recorded_at_pacific": timestamp(pool),
            "pool_is_fresh": pool_fresh,
            "pool_active_clients": pool.get("active_clients"),
            "supervisor_recorded_at_pacific": timestamp(supervisor),
            "supervisor_is_fresh": supervisor_age is not None and supervisor_age <= 180,
            "supervisor_stage": supervisor.get("stage"),
            "supervised_controller_pid": supervisor.get("child_pid"),
            "controller_repair_note": "Original controller exited with Errno 116 (stale file handle). Root restarted the existing exact controller under supervision at about 12:31 PM PDT; old aggregate status may remain stale while the supervised controller rechecks seals.",
            "note": "This tracker reads direct task evidence and does not promote the old controller or planning registry to live execution.",
        },
        "rows": rows,
        "evidence": list(evidence_records.values()),
        "validation": {"exactly_57_rows": True, "no_duplicate_setting_ids": True, "exact_retained_id_set": True, "categories_mutually_exclusive": True, "counts_sum_to_57": True},
    }
    return result


def markdown(data):
    def esc(value):
        return str(value).replace("|", "\\|").replace("\n", " ")

    lines = ["# Full retained catalog status", "", f"Observed **{data['generated_at_pacific']}** (America/Los_Angeles). Exactly **57 settings**, one row each.", "", "Done means a defined score for the declared evaluated condition. It does not imply matched-paper replication, complete original-paper scope, or good performance. Saved responses alone do not count as done.", "", "| Status | Count |", "|---|---:|"]
    for key, label in CATEGORIES.items():
        lines.append(f"| {label} | {data['counts'][key]} |")
    breakdown = data["agent_work_breakdown"]
    if breakdown:
        lines += ["", "Doable agent work includes " + ", ".join(f"{value} {key.replace('_', ' ')}" for key, value in breakdown.items()) + ". These tasks are not all in a live generation queue."]
    if not data["freshness"]["controller_is_live_evidence_only_if_recent"]:
        lines += ["", f"**Stale aggregate metadata:** the old controller record is from {data['freshness']['controller_recorded_at_pacific']}. Direct per-task progress/completion/score evidence below takes precedence."]
    if data["freshness"]["supervisor_is_fresh"]:
        lines += ["", f"The existing controller was restarted under supervision around **12:31 PM PDT** after an `Errno 116` stale-file-handle crash. Its supervisor is fresh at {data['freshness']['supervisor_recorded_at_pacific']}; pool heartbeat fresh: **{data['freshness']['pool_is_fresh']}**. This does not create a new protocol or extra inference scope."]
    lines += ["", "Exceptions for training and replacement judges remain user-held. Biological/provider holds are separate and cannot be cleared by a simple continuation instruction. Exact native unavailability is tracked separately from whether an available adaptation can proceed.", "", "## Every retained setting", "", "| ID | Setting | Status | Saved/planned | Next action / decision | Evidence |", "|---|---|---|---:|---|---|"]
    for row in data["rows"]:
        runtime = row["runtime"]
        saved = f"{runtime['responses_saved']:,}/{runtime['planned']:,}" if runtime and isinstance(runtime.get("responses_saved"), int) and isinstance(runtime.get("planned"), int) else (f"Unknown/{row['prepared_benchmark_planned']:,}" if row.get("prepared_benchmark_planned") else "—")
        evidence = row["public_evidence_path"]
        label = SHORT_LABELS[row["category"]]
        if row["substatus"] == "offline_scoring_repair":
            label = "Agent work: scoring repair"
        lines.append(f"| {row['task_id']} | {esc(row['task_name'])} | {esc(label)} | {saved} | {esc(row['next_action'])} | [{esc(Path(evidence).name)}](../{evidence}) |")
    lines += ["", "## Native-condition and scope qualifications", "", "| ID | Availability / material qualification |", "|---|---|"]
    for row in data["rows"]:
        if row["category"] != "done" or row["task_id"] in {"P09", "B08"}:
            extra = " ".join(row["scope_notes"])
            lines.append(f"| {row['task_id']} | {esc(row['exact_native_condition_availability'] + ' ' + extra)} |")
    lines += ["", "The [JSON tracker](CATALOG_STATUS.json) includes per-setting source times, hashes, all evidence paths, runtime errors and score metadata. Historical metrics and their separate conditions remain in [the decision table](EVALUATION_DECISION_TABLE.md).", "", "Regenerate with `python3 scripts/build_catalog_status.py`. This performs metadata reads and report writes only; it makes no inference calls or dispatch changes.", ""]
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    root = args.root.resolve()
    data = build(root)
    report = root / "reports/CATALOG_STATUS.json"
    report.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    (root / "reports/CATALOG_STATUS.md").write_text(markdown(data))
    print(json.dumps({"generated_at_pacific": data["generated_at_pacific"], "counts": data["counts"], "validation": data["validation"]}))


if __name__ == "__main__":
    main()
