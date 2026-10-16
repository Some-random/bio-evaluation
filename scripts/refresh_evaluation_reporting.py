#!/usr/bin/env python3
"""Refresh catalog presentation from existing score and supervisor metadata.

No inference, scoring, benchmark payload reads, scheduler changes, or frozen-plan
edits occur here. Uploaded trajectory counts are never called saved responses.
"""
from __future__ import annotations

import argparse
import copy
from datetime import datetime, timezone
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import re
import tempfile


CATALOG = "reports/TASK_HIERARCHY_DATA.json"
SCORES = "reports/RESULTS_AT_A_GLANCE.json"
VERIFIED_SCORES = "reports/VERIFIED_RESULTS_SNAPSHOT_2026-10-16T042525.json"
VERIFIED_SCORES_SHA256 = "bbc45d078704958137b4ea308b47f15163c72ba357d624f4dd145b5818791451"
SUPERVISOR = ".local/remaining_evaluations/supervisor_status.json"
UPLOAD = ".local/remaining_evaluations/upload_status.json"
PROGRESS = "reports/EVALUATION_PROGRESS.json"
HEARTBEAT_LIMIT = 300
HELD = {"B06", "P18"}


def encoded(value):
    return (json.dumps(value, ensure_ascii=False, indent=2, allow_nan=False) + "\n").encode()


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def timestamp(value):
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
        return parsed if parsed.tzinfo is not None else None
    except (AttributeError, TypeError, ValueError):
        return None


def formatter():
    # Reuse display-only helpers without running the scorer/report generator.
    path = Path(__file__).with_name("update_results_at_a_glance.py")
    spec = importlib.util.spec_from_file_location("evaluation_score_display", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def heartbeat(status, now):
    value = status.get("updated_at_utc")
    parsed = timestamp(value)
    if not value:
        state = "missing"
    elif parsed is None or parsed > now:
        state = "invalid"
    else:
        state = "stale" if (now - parsed).total_seconds() > HEARTBEAT_LIMIT else "fresh"
    # Do not persist a continuously changing age: unchanged input stays idempotent.
    return {"status": state, "updatedAt": value, "staleAfterSeconds": HEARTBEAT_LIMIT}


def count(value):
    return value if type(value) is int and value >= 0 else None


def score_key(row):
    """A source-defined evaluation condition, independent of its run directory."""
    return tuple(row.get(name) for name in ("task_id", "protocol_variant", "dataset", "native_split"))


def row_digest(row):
    return digest(json.dumps(row, ensure_ascii=False, sort_keys=True,
        separators=(",", ":"), allow_nan=False).encode())


def merge_score_snapshots(root, current, current_sha, prior_catalog=None):
    """Retain verified history when old run directories are not mounted.

    This combines report metadata, never scores or case data. Current rows win
    for the same condition, including diagnostic-only replacements. Completion
    claims survive only while their supporting conditions retain valid rows.
    """
    baseline_path = root / VERIFIED_SCORES
    previous = (prior_catalog or {}).get("meta", {})
    history_required = ((count(previous.get("historicalResultRows")) or 0) > 0
        or any(isinstance(source, dict) and source.get("path") == VERIFIED_SCORES
            for source in previous.get("scoreSnapshotSources", [])))
    if history_required and not baseline_path.is_file():
        raise ValueError("Previously retained historical score snapshot is missing; existing reporting outputs preserved")
    snapshots = []
    if baseline_path.is_file():
        raw = baseline_path.read_bytes()
        if digest(raw) != VERIFIED_SCORES_SHA256:
            raise ValueError("Verified historical score snapshot hash mismatch")
        snapshots.append((json.loads(raw), VERIFIED_SCORES, digest(raw), True))
    retained, provenance, sources, claims = {}, {}, [], {}

    def add_snapshot(report, path, sha, historical):
        source = {"path": path, "sha256": sha,
            "snapshotAt": report.get("generated_at_utc"), "historical": historical,
            "note": "Retained verified report metadata; not a fresh rerun." if historical
                    else "Current score-report metadata; report refresh does not rerun evaluation."}
        sources.append(source)
        for category in ("completed_rows", "diagnostic_only_finished_runs"):
            # Diagnostics deliberately follow completed rows, so an invalid
            # current condition cannot resurrect a historical valid score.
            for row in report.get(category, []):
                key = score_key(row)
                retained[key] = (copy.deepcopy(row), category)
                provenance[key] = {**source, "rowCategory": category,
                    "sourceScores": row.get("source_scores"),
                    "sourceScoresSha256": row.get("scores_sha256")}
        for task_id in report.get("completed_whole_declared_setting_ids", []):
            if task_id == "P43" and report.get("P43", {}).get("whole_setting_complete") is not True:
                continue
            supporting = [list(score_key(row)) for row in report.get("completed_rows", [])
                if row.get("task_id") == task_id
                and row.get("completion_scope") != "diagnostic_only_primary_metrics_invalid"]
            if supporting:
                claim = {"taskId": task_id, "supportingConditions": supporting,
                    "source": copy.deepcopy(source)}
                if task_id == "P43":
                    claim["aggregateMetadata"] = copy.deepcopy(report.get("P43", {}))
                claims[row_digest([task_id, supporting])] = claim

    for snapshot in snapshots:
        add_snapshot(*snapshot)

    # Canonical raw rows retain newly verified conditions (such as P03) after
    # their mounted run directory disappears. A rendered metric string alone
    # is never accepted as a recoverable source row.
    prior_keys = set()
    for group in (prior_catalog or {}).get("groups", []):
        for result in group.get("results", []):
            if "verifiedSourceRow" not in result:
                continue
            row = result["verifiedSourceRow"]
            source = result.get("scoreProvenance", {})
            category = source.get("rowCategory")
            if (result.get("verifiedSourceRowSha256") != row_digest(row)
                    or row.get("task_id") != result.get("taskId")
                    or category not in {"completed_rows", "diagnostic_only_finished_runs"}
                    or not source.get("path") or not source.get("sha256")):
                raise ValueError("Prior verified score row or provenance is invalid")
            key = score_key(row)
            prior_keys.add(key)
            if (source.get("path") == VERIFIED_SCORES
                    and source.get("sha256") == VERIFIED_SCORES_SHA256
                    and key in retained and row_digest(retained[key][0]) == row_digest(row)):
                continue
            retained[key] = (copy.deepcopy(row), category)
            provenance[key] = {**copy.deepcopy(source), "retainedFromCatalog": True,
                "note": "Retained from the prior verified catalog with its original source hash/date; not a fresh rerun."}
    for claim in previous.get("verifiedCompletionClaims", []):
        keys = claim.get("supportingConditions", [])
        if (not claim.get("taskId") or not isinstance(keys, list)
                or any(not isinstance(key, list) or len(key) != 4 or key[0] != claim["taskId"] for key in keys)
                or not claim.get("source", {}).get("sha256")):
            raise ValueError("Prior verified completion claim is invalid")
        supporting = {tuple(key) for key in keys}
        if supporting and supporting <= prior_keys:
            claims[row_digest([claim["taskId"], claim["supportingConditions"]])] = copy.deepcopy(claim)
    # Current valid or diagnostic evidence has final precedence over both
    # dated baseline rows and verified rows carried by the previous catalog.
    add_snapshot(current, SCORES, current_sha, False)
    valid_keys = {key for key, (row, category) in retained.items()
        if category == "completed_rows"
        and row.get("completion_scope") != "diagnostic_only_primary_metrics_invalid"}
    valid_claims = [claim for claim in claims.values()
        if {tuple(key) for key in claim["supportingConditions"]} <= valid_keys]
    completed = {claim["taskId"] for claim in valid_claims}
    merged = copy.deepcopy(current)
    for category in ("completed_rows", "diagnostic_only_finished_runs"):
        merged[category] = [row for row, kind in retained.values() if kind == category]
    merged["completed_whole_declared_setting_ids"] = sorted(completed)
    merged["_verified_completion_claims"] = valid_claims
    # P43's three component rows do not independently prove aggregate coverage.
    # Keep the source's verified aggregate record, qualified by its own date,
    # when all supporting component conditions still have valid retained rows.
    for claim in valid_claims:
        if claim["taskId"] == "P43" and claim.get("aggregateMetadata", {}).get("whole_setting_complete") is True:
            merged["P43"] = copy.deepcopy(claim["aggregateMetadata"])
    if "P43" not in completed and "P43" in merged:
        merged["P43"]["whole_setting_complete"] = False
    for source in provenance.values():
        if source.get("retainedFromCatalog"):
            summary = {key: source[key] for key in ("path", "sha256", "snapshotAt", "historical", "note")}
            summary["retainedFromCatalog"] = True
            if not any(item["path"] == summary["path"] and item["sha256"] == summary["sha256"] for item in sources):
                sources.append(summary)
    return merged, provenance, sources


def run_bearing(value):
    """Transient retry receipts are not execution-registry snapshots."""
    if not isinstance(value, dict):
        return False
    runs = value.get("runs")
    rows = list(runs.values()) if isinstance(runs, dict) else runs if isinstance(runs, list) else []
    return (bool(rows) and all(isinstance(row, dict) and isinstance(row.get("task_id"), str)
        and count(row.get("planned")) is not None for row in rows)
        and any(row.get("kind") != "aggregate" for row in rows))


def select_run_snapshot(root):
    records, hashes, errors = [], {}, []
    for name in [SUPERVISOR, UPLOAD]:
        path = root / name
        raw = path.read_bytes() if path.is_file() else None
        hashes[name] = digest(raw) if raw is not None else None
        try:
            value = json.loads(raw) if raw is not None else None
        except (json.JSONDecodeError, UnicodeDecodeError):
            value = None
        valid = run_bearing(value)
        if not valid:
            errors.append({"source": name, "reason": "missing_metadata" if raw is None else "no_valid_run_snapshot"})
        records.append({"path": name, "value": value, "valid": valid})
    candidates = [record for record in records if record["valid"]]
    if not candidates:
        # Fail before either output is written. Existing catalog/progress remain
        # available with their original dates instead of becoming an empty plan.
        raise ValueError("No valid run-bearing supervisor or upload snapshot; existing reporting outputs preserved")
    oldest = datetime.min.replace(tzinfo=timezone.utc)
    selected = max(candidates, key=lambda record: timestamp(record["value"].get("updated_at_utc")) or oldest)
    status = copy.deepcopy(selected["value"])
    provenance = {"path": selected["path"], "snapshotAt": status.get("updated_at_utc"),
        "fallback": selected["path"] != SUPERVISOR, "selection": "most_recent_valid_run_snapshot"}
    newer_failure = None
    for record in records:
        value = record["value"]
        if (not record["valid"] and isinstance(value, dict) and value.get("stage") == "retry_pending"
                and (timestamp(value.get("updated_at_utc")) or oldest) >= (timestamp(status.get("updated_at_utc")) or oldest)):
            newer_failure = {"source": record["path"], "stage": "retry_pending",
                "updatedAt": value.get("updated_at_utc"),
                "note": "The supervisor reported a transient metadata/publication failure; progress uses the last successful run snapshot."}
    return status, hashes, provenance, errors, newer_failure


def build_progress(status, report, source_hashes, now):
    tasks = {}
    runs = status.get("runs", {})
    if isinstance(runs, list):
        runs = {row["run_id"]: row for row in runs}
    for run_id, run in runs.items():
        if run.get("kind") == "aggregate":
            continue
        task_id = run.get("task_id")
        if not task_id:
            continue
        task = tasks.setdefault(task_id, {"taskId": task_id, "planned": 0,
            "uploaded": 0, "saved": 0, "generationRuns": 0, "terminalRuns": 0,
            "allTerminal": True, "nativeMetricsValid": None,
            "progressSource": "uploaded_trajectories", "runIds": []})
        task["generationRuns"] += 1
        task["runIds"].append(run_id)
        task["planned"] += count(run.get("planned")) or 0
        task["uploaded"] += count(run.get("uploaded_trajectories")) or 0
        saved = count(run.get("saved_response_records", run.get("saved_responses")))
        task["saved"] = task["saved"] + saved if task["saved"] is not None and saved is not None else None
        terminal = run.get("terminal") is True
        task["terminalRuns"] += terminal
        task["allTerminal"] = task["allTerminal"] and terminal
    for task in tasks.values():
        # Only whole-test records or explicit aggregate records establish native
        # validity. A collection of finished shards cannot complete a benchmark.
        whole = [row for row in runs.values() if row.get("task_id") == task["taskId"]
                 and row.get("kind") in {"aggregate", "full_test"}]
        if whole and all(row.get("terminal") is True for row in whole):
            values = [row.get("native_metrics_valid") for row in whole]
            task["nativeMetricsValid"] = (all(value is True for value in values)
                if all(value is not None for value in values) else None)
        task["runIds"].sort()
    ordered = [tasks[key] for key in sorted(tasks)]
    scheduler = status.get("scheduler", [])
    # The supervisor's scheduler list contains only its GPU pools. Defensive CPU
    # exclusions support metadata exported with an explicit resource descriptor.
    active = sum(row.get("state") == "RUNNING"
                 and "supervisor" not in str(row.get("name", "")).lower()
                 and not str(row.get("partition", "")).endswith("cpu")
                 and row.get("gpu_count", 1) != 0
                 for row in scheduler) if "scheduler" in status else None
    saved = sum(task["saved"] for task in ordered) if ordered and all(task["saved"] is not None for task in ordered) else None
    snapshots = [value for value in [status.get("updated_at_utc"), report.get("generated_at_utc")]
                 if timestamp(value) is not None]
    generated = max(snapshots, key=timestamp) if snapshots else None
    return {"generatedAt": generated, "scoreSnapshotAt": report.get("generated_at_utc"),
        "runSnapshotAt": status.get("updated_at_utc"), "heartbeat": heartbeat(status, now),
        "sourceHashes": source_hashes, "uploader": {
            "stage": status.get("stage", "unavailable"), "commitSha": status.get("commit_sha"),
            "repositoryPrivateVerified": status.get("repository_private_verified")},
        "scheduler": {"activeWorkers": active, "jobs": scheduler},
        "registrySealed": status.get("registry_sealed"),
        "allTerminal": status.get("all_terminal"),
        "allSuccessfulNativeMetrics": status.get("all_successful_native_metrics"),
        "totals": {"planned": sum(task["planned"] for task in ordered),
            "uploaded": sum(task["uploaded"] for task in ordered), "saved": saved,
            "scheduledSettings": len(ordered), "generationRuns": sum(task["generationRuns"] for task in ordered)},
        "tasks": ordered,
        "countNote": "Progress counts exclude aggregate runs. Uploaded counts reflect archived trajectories at the uploader heartbeat; saved is unknown unless explicitly reported. Counts do not establish benchmark completion."}


def result_record(row, report, display, github, provenance=None):
    reference = row.get("selected_published_reference") or {}
    incomplete = (display.incomplete_evaluation(row, report)
                  or row.get("completion_scope") == "diagnostic_only_primary_metrics_invalid")
    source = row.get("source_scores")
    result = {"taskId": row["task_id"],
        "title": row["task_name"] + (" · " + row["dataset"] if row.get("dataset") else ""),
        "metricText": display.local_display(row),
        "publishedText": re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", display.published_display(row)),
        "publishedUrl": reference.get("source_url"), "counts": copy.deepcopy(row["counts"]),
        "incomplete": incomplete,
        "sourceUrl": github + "/blob/main/" + source if source else None,
        "protocol": row["protocol_variant"], "caveats": copy.deepcopy(row.get("caveats", [])),
        "comparison": row.get("comparison_to_paper"), "metrics": copy.deepcopy(row["metrics"]),
        "finishedAt": row.get("finished_at_utc"), "completionScope": row["completion_scope"],
        "caseScope": row["case_scope"],
        "publishedReferences": copy.deepcopy(row.get("all_published_references", []))}
    if provenance is not None:
        result["scoreProvenance"] = copy.deepcopy(provenance)
        result["scoreSnapshotAt"] = provenance["snapshotAt"]
        result["verifiedSourceRow"] = copy.deepcopy(row)
        result["verifiedSourceRowSha256"] = row_digest(row)
    return result


def build_outputs(root, now=None):
    root = Path(root)
    now = now or datetime.now(timezone.utc)
    catalog_raw = (root / CATALOG).read_bytes()
    score_raw = (root / SCORES).read_bytes()
    catalog = json.loads(catalog_raw)
    report, score_provenance, score_sources = merge_score_snapshots(root, json.loads(score_raw), digest(score_raw), catalog)
    supervisor, run_hashes, provenance, metadata_errors, newer_failure = select_run_snapshot(root)
    score_hashes = {source["path"]: source["sha256"] for source in score_sources}
    # Several retained generations can share the native report path. Its main
    # source hash always describes the current file; older hashes remain in
    # each row's provenance and the separate scoreSnapshotSources records.
    score_hashes[SCORES] = digest(score_raw)
    progress = build_progress(supervisor, report, {**score_hashes, **run_hashes}, now)
    progress["scoreSnapshotSources"] = score_sources
    progress["runSnapshotSource"] = provenance
    progress["metadataErrors"] = metadata_errors
    if newer_failure:
        progress["uploader"]["stage"] = "retry_pending"
        progress["metadataNotice"] = newer_failure
    display = formatter()
    rows = report.get("completed_rows", []) + report.get("diagnostic_only_finished_runs", [])
    mapped = [task_id for group in catalog["groups"] for task_id in group["taskIds"]]
    if len(mapped) != len(set(mapped)):
        raise ValueError("Catalog task IDs must be unique across groups")
    if len(mapped) != catalog["meta"].get("registrySettings", len(mapped)):
        raise ValueError("Catalog registry coverage changed")
    if not {row["task_id"] for row in rows} <= set(mapped):
        raise ValueError("Score report contains an unmapped catalog task")
    github = catalog["meta"].get("githubUrl", "https://github.com/Some-random/bio-evaluation").rstrip("/")
    by_task = {}
    for row in rows:
        by_task.setdefault(row["task_id"], []).append(result_record(row, report, display, github,
            score_provenance[score_key(row)]))
    # Native report generation owns primary-metric validation. Do not reinterpret
    # optional undefined diagnostics as invalid primary scores (e.g. P42 novelty
    # when no successful improved sequences exist). Diagnostic-only rows never
    # promote an ID, even if an inconsistent ID list contains that task.
    valid_row_tasks = {row["task_id"] for row in report.get("completed_rows", [])
        if row.get("completion_scope") != "diagnostic_only_primary_metrics_invalid"}
    completed = set(report.get("completed_whole_declared_setting_ids", [])) & valid_row_tasks
    active = {task["taskId"]: task for task in progress["tasks"]}
    blockers = {task_id: blocker for blocker in report.get("blockers", []) for task_id in blocker["task_ids"]}
    previous_statuses = {protocol["taskId"]: protocol.get("status")
        for group in catalog["groups"] for protocol in group.get("protocols", [])}

    def task_status(task_id, previous=None):
        previous = previous if previous is not None else previous_statuses.get(task_id)
        if task_id in HELD:
            return "Deferred / held"
        current = active.get(task_id)
        if current and not current["allTerminal"]:
            return "Running / queued"
        if current and current["allTerminal"] and current["nativeMetricsValid"] is not True:
            return "Partial"
        results = by_task.get(task_id, [])
        if results:
            return "Results available" if task_id in completed and not any(row["incomplete"] for row in results) else "Partial"
        if task_id in blockers or previous == "Source-blocked":
            return "Source-blocked"
        if current and current["allTerminal"]:
            return "Partial"
        return "Deferred / held" if previous == "Deferred / held" else "Status unverified"

    def group_status(values, previous):
        if not values:
            return previous
        if "Running / queued" in values:
            return "Running / queued"
        if all(value == "Results available" for value in values):
            return "Results available"
        if any(value in {"Results available", "Partial"} for value in values):
            return "Partial"
        if len(set(values)) == 1:
            return values[0]
        return "Status unverified"

    for group in catalog["groups"]:
        old = {row["taskId"]: row for row in group.get("protocols", [])}
        group["results"] = [row for task_id in group["taskIds"] for row in by_task.get(task_id, [])]
        for protocol in group.get("protocols", []):
            task_id = protocol["taskId"]
            protocol["status"] = task_status(task_id, protocol.get("status"))
            if task_id in blockers:
                blocker = blockers[task_id]
                protocol["blocker"] = blocker.get("description", protocol.get("blocker"))
                if blocker.get("source_report"):
                    protocol["evidenceUrl"] = github + "/blob/main/" + blocker["source_report"]
        group["status"] = group_status([task_status(task_id, old.get(task_id, {}).get("status"))
                                       for task_id in group["taskIds"]], group.get("status", "Status unverified"))
    if sum(len(group["results"]) for group in catalog["groups"]) != len(rows):
        raise ValueError("Score report rows failed catalog reconciliation")
    names = {protocol["taskId"]: protocol["title"] for group in catalog["groups"] for protocol in group.get("protocols", [])}
    previous_runs = {row["taskId"]: row for row in catalog.get("runs", [])}
    catalog["runs"] = []
    for task in progress["tasks"]:
        run = copy.deepcopy(previous_runs.get(task["taskId"], {}))
        run.update(taskId=task["taskId"], dataset=names.get(task["taskId"], task["taskId"]),
            status=task_status(task["taskId"]), planned=task["planned"], uploaded=task["uploaded"],
            saved=task["saved"], completed=task["saved"], lengthStopped=None,
            progressSource=task["progressSource"], sourceUrl=github + "/blob/main/" + PROGRESS)
        catalog["runs"].append(run)
    meta = catalog["meta"]
    meta.update(generatedAt=progress["generatedAt"], scoreSnapshotAt=report.get("generated_at_utc"),
        runSnapshotAt=progress["runSnapshotAt"], completedSettings=len(completed), localResultRows=len(rows),
        activeWorkers=progress["scheduler"]["activeWorkers"], scheduledSettings=len(active),
        plannedCases=progress["totals"]["planned"], savedResponses=progress["totals"]["saved"],
        uploadedResponses=progress["totals"]["uploaded"], heartbeat=progress["heartbeat"],
        runSnapshotSource=progress["runSnapshotSource"], metadataErrors=progress["metadataErrors"],
        metadataNotice=progress.get("metadataNotice"),
        scoreSnapshotSources=score_sources,
        verifiedCompletionClaims=copy.deepcopy(report["_verified_completion_claims"]),
        historicalResultRows=sum(score_provenance[score_key(row)]["historical"] for row in rows),
        priorVerifiedResultRows=sum(score_provenance[score_key(row)].get("retainedFromCatalog", False)
            and not score_provenance[score_key(row)]["historical"] for row in rows),
        currentResultRows=sum(not score_provenance[score_key(row)]["historical"]
            and not score_provenance[score_key(row)].get("retainedFromCatalog", False) for row in rows),
        taskStatusCounts={state: sum(task_status(task_id) == state for task_id in mapped)
            for state in ["Results available", "Partial", "Running / queued", "Source-blocked", "Deferred / held", "Status unverified"]})
    progress_raw = encoded(progress)
    meta.setdefault("sourceHashes", {}).update({**score_hashes, PROGRESS: digest(progress_raw), **run_hashes})
    return {PROGRESS: progress_raw, CATALOG: encoded(catalog)}


def atomic_write(path, raw):
    path.parent.mkdir(parents=True, exist_ok=True)
    mode = path.stat().st_mode & 0o777 if path.exists() else 0o644
    temporary = None
    try:
        with tempfile.NamedTemporaryFile(dir=path.parent, prefix="." + path.name + ".", delete=False) as handle:
            temporary = Path(handle.name)
            handle.write(raw)
            handle.flush()
            os.fsync(handle.fileno())
        temporary.chmod(mode)
        temporary.replace(path)
    finally:
        if temporary is not None and temporary.exists():
            temporary.unlink()


def refresh(root, check=False, now=None):
    changed = []
    for relative, raw in build_outputs(root, now).items():
        path = Path(root) / relative
        if not path.is_file() or path.read_bytes() != raw:
            changed.append(relative)
            if not check:
                atomic_write(path, raw)
    return changed


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--check", action="store_true", help="Exit 1 when refreshed metadata would differ; write nothing")
    args = parser.parse_args()
    changed = refresh(args.root, args.check)
    print(json.dumps({"changed": changed, "check": args.check}))
    return 1 if args.check and changed else 0


if __name__ == "__main__":
    raise SystemExit(main())
