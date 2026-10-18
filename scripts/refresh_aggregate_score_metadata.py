#!/usr/bin/env python3
"""Add terminal aggregate metadata without losing unmounted historical results.

Only aggregate scores, completion/manifest records and report metadata are read.
This collector never reads cases, raw answers or labels, or invokes a scorer.
"""
from __future__ import annotations

import argparse
import copy
import hashlib
import json
from pathlib import Path
import re

import update_results_at_a_glance as scores


REPORT = "reports/RESULTS_AT_A_GLANCE.json"
VERIFIED_HISTORY = "reports/VERIFIED_RESULTS_SNAPSHOT_2026-10-16T042525.json"
VERIFIED_HISTORY_SHA256 = "bbc45d078704958137b4ea308b47f15163c72ba357d624f4dd145b5818791451"
CATEGORIES = ("completed_rows", "diagnostic_only_finished_runs")


def identity(row):
    key = tuple(row.get(name) for name in ("run_id", "task_id", "protocol_variant"))
    if (not all(isinstance(value, str) and value for value in key[:2])
            or key[2] is not None and not isinstance(key[2], str)
            or not isinstance(row.get("metrics"), dict)
            or not isinstance(row.get("counts"), dict)
            or not isinstance(row.get("source_scores"), str)
            or not re.fullmatch(r"[0-9a-f]{64}", row.get("scores_sha256", ""))):
        raise ValueError("Historical aggregate row has incomplete identity or score provenance")
    return key


def merged_report(fresh, history):
    """Historical rows retain their identity; fresh rows win only that identity.

    History entries are (report, source path, source SHA-256), ordered oldest
    first. Category changes replace the exact run/variant only. Archived task
    families remain in structured metadata and are filtered only for display.
    """
    result = copy.deepcopy(fresh)
    retained = {}
    provenance = {}
    containers = {}
    blockers = {}
    seed_audit = None
    catalog_count = fresh.get("catalog_settings")
    for report, source, checksum in history:
        if not isinstance(report, dict):
            raise ValueError("Historical aggregate report is not an object")
        for category in CATEGORIES:
            values = report.get(category, [])
            if not isinstance(values, list):
                raise ValueError("Historical aggregate row category is not a list")
            for row in values:
                key = identity(row)
                value = copy.deepcopy(row)
                value.setdefault("aggregate_snapshot_provenance", {
                    "path": source, "sha256": checksum,
                    "note": "Retained aggregate metadata with its original score hash; no new scoring or raw-output verification."})
                retained[key] = (category, value)
        provenance.update(report.get("source_sha256", {}))
        for row in report.get("P43", {}).get("validated_aggregate_containers", []):
            containers[identity(row)] = copy.deepcopy(row)
        for item in report.get("blockers", []):
            blockers[(tuple(item.get("task_ids", [])), item.get("source_report"))] = copy.deepcopy(item)
        if report.get("P29_seed_only_offline_audit"):
            seed_audit = copy.deepcopy(report["P29_seed_only_offline_audit"])
        if catalog_count is None:
            catalog_count = report.get("catalog_settings")
    historical_keys = set(retained)
    fresh_keys = set()
    for category in CATEGORIES:
        for row in fresh.get(category, []):
            key = identity(row)
            fresh_keys.add(key)
            retained[key] = (category, copy.deepcopy(row))
    for category in CATEGORIES:
        result[category] = sorted([row for kind, row in retained.values() if kind == category],
            key=lambda row: (row["task_id"], row.get("dataset") or row.get("native_split") or "", row["run_id"], row.get("protocol_variant") or ""))
    provenance.update(fresh.get("source_sha256", {}))
    result["source_sha256"] = provenance
    for row in fresh.get("P43", {}).get("validated_aggregate_containers", []):
        containers[identity(row)] = copy.deepcopy(row)
    p43 = copy.deepcopy(fresh.get("P43", {}))
    p43["validated_aggregate_containers"] = list(containers.values())
    p43["whole_setting_complete"] = any(
        row.get("completion_scope") == "verified_three_dataset_aggregate"
        and scores.valid_union(row.get("full_test_id_union_validation") or {}, 16533)
        for row in containers.values())
    p43["completed_components"] = sorted({row["dataset"] for row in result["completed_rows"]
        if row["task_id"] == "P43" and row.get("dataset")})
    result["P43"] = p43
    whole = {row["task_id"] for row in result["completed_rows"]
        if row.get("completion_scope") == "completed_declared_run"}
    if p43["whole_setting_complete"]:
        whole.add("P43")
    splits = {row.get("native_split") for row in result["completed_rows"] if row["task_id"] == "P29"}
    if splits == {"id", "ood"}:
        whole.add("P29")
    result["completed_whole_declared_setting_ids"] = sorted(whole)
    result["catalog_settings"] = catalog_count
    for item in fresh.get("blockers", []):
        blockers[(tuple(item.get("task_ids", [])), item.get("source_report"))] = copy.deepcopy(item)
    result["blockers"] = list(blockers.values())
    result["P29_seed_only_offline_audit"] = fresh.get("P29_seed_only_offline_audit") or seed_audit
    result["metadata_history_retention"] = {
        "identity_key": ["run_id", "task_id", "protocol_variant"],
        "retained_unmounted_row_count": len(historical_keys - fresh_keys),
        "rows_preserved_separately_for_original_and_derived_runs": True,
        "current_row_replacement": "Exact same run, task and protocol variant only; categories and undefined metrics are preserved.",
        "compact_display": "Latest completed run for the same task/protocol/dataset/split/coverage; all run records remain in this JSON.",
        "no_inference_or_scoring_performed": True}
    return scores.apply_main_scope(scores.clean(result), fresh.get("main_report_scope", {}))


def collect(root, generated_at=None):
    root = Path(root)
    history = []
    verified = root / VERIFIED_HISTORY
    if verified.is_file():
        raw = verified.read_bytes()
        checksum = hashlib.sha256(raw).hexdigest()
        if checksum != VERIFIED_HISTORY_SHA256:
            raise ValueError("Verified historical aggregate report hash mismatch")
        history.append((json.loads(raw), VERIFIED_HISTORY, checksum))
    previous = root / REPORT
    previous_report = None
    if previous.is_file():
        raw = previous.read_bytes()
        previous_report = json.loads(raw)
        history.append((previous_report, REPORT, hashlib.sha256(raw).hexdigest()))
    result = merged_report(scores.build_report(root, generated_at=generated_at), history)
    if previous_report is not None:
        before = {key: value for key, value in previous_report.items() if key != "generated_at_utc"}
        after = {key: value for key, value in result.items() if key != "generated_at_utc"}
        if before == after:
            result["generated_at_utc"] = previous_report["generated_at_utc"]
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    report = collect(args.root)
    outputs = scores.write_report(args.root, report)
    print(json.dumps({"outputs": outputs, "completed_rows": len(report["completed_rows"]),
        "diagnostic_rows": len(report["diagnostic_only_finished_runs"]),
        "retained_unmounted_rows": report["metadata_history_retention"]["retained_unmounted_row_count"],
        "inference_or_scoring_performed": False}))


if __name__ == "__main__":
    main()
