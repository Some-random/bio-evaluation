#!/usr/bin/env python3
"""Publish separate 16k continuation trajectories; never infer, score or retry.

Uses the frozen existing raw-archive/Git helpers with its own checkout, batches,
release cursor and status. All remote writers share evaluation_publication.lock.
Check-only mode neither creates release assets nor changes GitHub or run links.
"""
from __future__ import annotations

import argparse
from collections import Counter
import copy
from datetime import datetime
import fcntl
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import re
import signal
import tempfile
import time
import urllib.error
from zoneinfo import ZoneInfo

CONDITION = "MIXED_BUDGET_4K16K_CONTINUATION"
MODEL = "Qwen/Qwen3.8-27B"
REVISION = "1d4bf0f2ff6012fd82039f2fa52739d0dd7c60c0"
TASKS = {"P07", "P08", "P12", "P13", "P14", "P15", "P16"}
RUNTIME_RELATIVE = "results/evaluation_revisions/output_budget_2026-10-18"
TAG = "output-budget-revision-2026-10-18-trajectories"
SCORING_CONDITIONS = {CONDITION, "RETAINED_4K_COMPLETE_UNDER_BUDGET_REVISION", "PROSPECTIVE_16K_FULL_TASK"}
SCORE_METADATA = ("completion.json", "scores.json", "native_scores_unmodified.json", "per_case_scores.json",
                  "metrics.csv", "run_manifest.json", "per_case_budget_map.json", "mixed_budget_output_lock.json",
                  "mixed_scoring_spec.json", "native_scorer_invocation.json", "native_scorer.log")
PINS = {
    ".local/remaining_evaluations/pool_supervisor_final_v2.py": "a242714f8aecd8ab254b02e21639f5e3c014e22176d00000632a271d6160242b",
    ".local/remaining_evaluations/pool_worker.py": "369a08ae7d22f40b16675ee5532e2e1b339a59f69a0914b7538e6465e3fa284b",
    ".local/litqa2_replay/incremental_upload.py": "194f143fa81d2409c3f72403c5664f7f9c64b9ca3cc46af9603de0d044cf0160",
    ".local/litqa2_replay/parallel_upload.py": "afcd36eaf7abb8d26ace19c2baa5ade470998bfa98ecc95626ae76e756bc38cd",
    ".local/shared_vllm_saturation_2026-10-18/publish_saturation_artifacts.py": "c67e8c1c448ecd86be575f52a22dfd93c232fdc24786741768394b53d9259557",
    "scripts/publication_destination.py": "7af9309f3b860b69301abae590a6c9ac4f03c1d81a6b3269b86fc077b6a10f4a",
    "scripts/daily_backup.py": "528735e220dd6a2b5ab3d5b6b51ec7143b5ffa891fdfcfc211d2a8099ce7093d",
}
STOP = False


def stamp():
    return datetime.now(ZoneInfo("America/Los_Angeles")).isoformat()


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def digest(value):
    return hashlib.sha256(json.dumps(value, ensure_ascii=False, sort_keys=True,
                                    separators=(",", ":")).encode()).hexdigest()


def read(path, default=None):
    return json.loads(Path(path).read_text()) if Path(path).is_file() else default


def write(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name + ".tmp")
    temporary.write_text(json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n")
    temporary.replace(path)


def module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result


def owned(root, path, directory=None):
    source = Path(path)
    resolved = source.resolve()
    if source.is_symlink() or not resolved.is_relative_to((directory or root).resolve()):
        raise ValueError("Publication source leaves its owned directory")
    return resolved


def pinned(root, pin):
    source = owned(root, pin["path"])
    if not re.fullmatch(r"[0-9a-f]{64}", pin.get("sha256", "")) or sha(source) != pin["sha256"]:
        raise ValueError("Pinned publication source changed")
    return source


def load_helpers(root, state):
    for name, expected in PINS.items():
        if sha(root / name) != expected:
            raise ValueError("Frozen publication helper changed: " + name)
    bridge = module("budget_publication_frozen_bridge", root / ".local/shared_vllm_saturation_2026-10-18/publish_saturation_artifacts.py")
    native = module("budget_publication_native_archives", root / ".local/remaining_evaluations/pool_supervisor_final_v2.py")
    native.HERE = state
    native.CHECKOUT = state / "upload_checkout"
    native.helpers.CHECKOUT = native.CHECKOUT
    def forbidden(*args, **kwargs):
        raise RuntimeError("This publication bridge may not infer, aggregate or score")
    native.aggregate_ready = forbidden
    native.refresh_reports = forbidden
    native.release = lambda part=None: release(native, state, part)
    scanner = module("budget_publication_scanner", root / "scripts/daily_backup.py")
    return native, bridge, scanner


def release(native, state, part=None):
    """Dedicated public release series and cursor; no legacy writer state."""
    cursor = state / "upload_release_cursor.json"
    part = (read(cursor, {}).get("part", 1) if part is None else part)
    if type(part) is not int or part < 1:
        raise ValueError("Invalid output-budget release part")
    tag = TAG if part == 1 else TAG + "-part" + str(part).zfill(3)
    base = "https://api.github.com/repos/Some-random/bio-evaluation/releases"
    try:
        record = native.remote.api(base + "/tags/" + tag)
    except urllib.error.HTTPError as exc:
        if exc.code != 404:
            raise
        record = native.remote.api(base, "POST", {
            "tag_name": tag, "target_commitish": "main", "draft": False,
            "prerelease": True, "name": "16k output-budget continuation trajectories" + (" part " + str(part) if part > 1 else ""),
            "body": "Public incremental trajectories for MIXED_BUDGET_4K16K_CONTINUATION. "
                    "Only previously undispatched cases receive a 16384-token output budget; retained original cases keep their 4096-token outputs. "
                    "Assets preserve exact requests, responses, reasoning, failures and usage. "
                    "Per-run indexes on main contain member hashes and source/cohort provenance. "
                    "Saved responses are generation artifacts, not completed benchmark metrics. No weights, credentials, environments or caches."})
    assets, page = {}, 1
    while True:
        values = native.remote.api(record["assets_url"] + "?per_page=100&page=" + str(page))
        assets.update({item["name"]: item for item in values})
        if len(values) < 100:
            break
        page += 1
    record["_part"] = part
    write(cursor, {"part": part, "tag": tag, "release_id": record["id"], "updated_at_pacific": stamp()})
    return record, assets


def load_runs(root, plan_pins):
    budget = root / ".local/evaluation_revision_2026-10-18/budget_queue"
    runs, plans, selected = {}, [], set()
    for pin in plan_pins:
        path = pinned(root, pin)
        plan = read(path)
        if (path.parent != budget or path.name not in {"plan_existing_pool.json", "plan_new_pool.json"}
                or plan.get("kind") != "explicit_output_budget_revision"
                or plan.get("execution_authorized") is not True or plan.get("condition") != CONDITION
                or plan.get("output_budget") != 16384 or plan.get("original_output_budget") != 4096
                or plan.get("model") != MODEL or plan.get("model_revision") != REVISION
                or plan.get("retries_or_resampling_of_previously_executed_cases") is not False
                or plan.get("original_model_inputs_and_sampling_preserved_except_max_tokens") is not True
                or not plan.get("runs") or not plan.get("authorization_quote")
                or sha(budget / "run_budget_revision.py") != plan.get("code_sha256")):
            raise ValueError("Not an exact authorized, separately labeled output-budget plan")
        plans.append({"path": path, "sha256": pin["sha256"], "plan": plan})
        for item in plan["runs"]:
            entry = item["entry"]
            if entry["task_id"] not in TASKS or not re.fullmatch(r"[A-Za-z0-9_.-]+", entry["run_id"]):
                raise ValueError("Run is outside the retained reviewed task scope")
            name = entry["run_id"] + "_output16384_v1"
            folder = owned(root, item["output_directory"], budget / "results/runs")
            if folder != budget / "results/runs" / name or name in runs:
                raise ValueError("Duplicate or redirected output-budget run")
            project = owned(root, entry["project_root"])
            config_path = pinned(root, {"path": project / entry["config_path"], "sha256": entry["config_sha256"]})
            original = read(config_path)
            if (original.get("run_id") != entry["run_id"] or original.get("approved_task_ids") != [entry["task_id"]]
                    or original.get("model") != MODEL or original.get("model_revision") != REVISION
                    or original.get("generation", {}).get("max_tokens") != 4096):
                raise ValueError("Source configuration differs from original 4k condition")
            revised = copy.deepcopy(original)
            revised["generation"]["max_tokens"] = 16384
            checkpoint_path = pinned(root, item["parent_checkpoint"])
            checkpoint = read(checkpoint_path)
            ids = item["selected_case_ids"]
            if (item.get("case_scope") != "all_never_dispatched_at_clean_pause" or not ids
                    or len(ids) != len(set(ids)) or digest(ids) != item.get("ordered_case_ids_sha256")
                    or checkpoint.get("condition") != CONDITION or checkpoint.get("ambiguous_files") != []
                    or checkpoint.get("ordered_pending_case_ids") != ids
                    or checkpoint.get("original_source_run_id") != entry["run_id"]
                    or checkpoint.get("selection_uses_correctness_or_finish_reason") is not False):
                raise ValueError("Prospective cohort differs from clean, answer-blind parent checkpoint")
            identities = {(entry["task_id"], original["variant"], case_id) for case_id in ids}
            if selected & identities:
                raise ValueError("Duplicated case across revision plans")
            selected.update(identities)
            runs[name] = {"run_id": name, "source_run_id": entry["run_id"], "task_id": entry["task_id"],
                          "folder": folder, "project_root": project, "config_path": config_path,
                          "original": original, "revised": revised, "planned": len(ids), "ids": set(ids),
                          "plan_path": path, "plan_sha256": pin["sha256"], "plan": plan,
                          "checkpoint_path": checkpoint_path, "checkpoint": checkpoint, "item": item}
    return plans, runs


def validate_manifest(spec):
    path = spec["folder"] / "run_manifest.json"
    if not path.is_file():
        return False
    manifest = read(path)
    if (manifest.get("condition") != CONDITION or manifest.get("aggregate_budget_condition") != CONDITION
            or manifest.get("plan_sha256") != spec["plan_sha256"]
            or manifest.get("planned_cases") != spec["planned"]
            or manifest.get("source_entry") != spec["item"]["entry"]
            or manifest.get("configuration") != spec["revised"]
            or manifest.get("original_configuration") != spec["original"]
            or manifest.get("parent_checkpoint") != spec["item"]["parent_checkpoint"]
            or manifest.get("parent_run_directory") != spec["checkpoint"]["parent_run_directory"]
            or manifest.get("original_artifacts_modified") is not False
            or manifest.get("model_outcome_based_selection") is not False):
        raise ValueError("New condition manifest differs from frozen prospective plan")
    return True


def outcome(spec):
    marker = read(spec["folder"] / "generation_completion.json")
    result = {"generation_terminal": False, "native_metrics_valid": None,
              "scored_benchmark_completed": False, "scoring_pending": True}
    if marker:
        statuses = marker.get("statuses", {})
        if (marker.get("condition") != CONDITION or marker.get("plan_sha256") != spec["plan_sha256"]
                or marker.get("planned") != spec["planned"]
                or any(type(n) is not int or n < 0 for n in statuses.values())
                or sum(statuses.values()) != spec["planned"]
                or marker.get("scoring_performed") is not False):
            raise ValueError("New generation completion marker differs from frozen cohort")
        result.update(generation_terminal=True, generation_exit_code=marker.get("generation_exit_code"),
                      execution_success=marker.get("generation_exit_code") == 0 and statuses.get("completed") == spec["planned"])
    return result


def load_scoring_views(root, state, plan_pins):
    """Discover the exact seven frozen offline views; never run their scorer."""
    directory = root / ".local/evaluation_revision_2026-10-18/scoring"
    registry_path = directory / "watch_plan_v1.json"
    if not registry_path.is_file():
        return None, {}
    checksum = sha(registry_path)
    activation = state / "activated_scoring_watch_plan.json"
    previous = read(activation)
    if previous and (previous.get("path") != str(registry_path) or previous.get("sha256") != checksum):
        raise ValueError("Previously activated scoring watch registry changed")
    registry = read(registry_path)
    if (registry.get("condition") != CONDITION or registry.get("old_outputs_modified") is not False
            or not registry.get("spec_files") or not registry.get("code_files_sha256")):
        raise ValueError("Scoring registry is not the unchanged-native derived condition")
    for name, expected in registry["code_files_sha256"].items():
        pinned(root, {"path": name, "sha256": expected})
    expected_plans = {(str(Path(p["path"]).resolve()), p["sha256"]) for p in plan_pins}
    views, tasks = {}, set()
    for pin in registry["spec_files"]:
        source = pinned(root, pin)
        spec = read(source)
        task = spec.get("task_id")
        if (source.parent != directory or source.name != str(task).lower() + "_mixed_scoring_v1.json"
                or task not in TASKS or task in tasks or spec.get("generation_budget_condition") != CONDITION
                or {(str(Path(p["path"]).resolve()), p["sha256"]) for p in spec.get("revision_plans", [])} != expected_plans):
            raise ValueError("Derived scoring spec has duplicated/unsupported tasks or different source plans")
        project = owned(root, spec["project_root"])
        full_path = pinned(root, {"path": project / spec["full_config_file"], "sha256": spec["full_config_sha256"]})
        full = read(full_path)
        name = full["run_id"] + "_mixed_4k16k_scoring_v1"
        if (spec.get("output_run_id") != name or not re.fullmatch(r"[A-Za-z0-9_.-]+", name)
                or full.get("model") != MODEL or full.get("model_revision") != REVISION
                or full.get("approved_task_ids") != [task]):
            raise ValueError("Derived scoring identity differs from the original native task")
        pinned(root, {"path": project / spec["scorer_file"], "sha256": spec["scorer_sha256"]})
        pinned(root, {"path": spec["revision_runner_file"], "sha256": spec["revision_runner_sha256"]})
        planned = full.get("full_test_case_count", full.get("planned"))
        if type(planned) is not int or planned < 1:
            review = pinned(root, {"path": project / full["review_file"],
                                   "sha256": full["frozen_files_sha256"][full["review_file"]]})
            planned = len(read(review)["approved_case_ids"])
        views[name] = {"run_id": name, "task_id": task, "project_root": project,
                       "folder": project / "results/runs" / name, "planned": planned,
                       "config_path": project / "configs" / (name + ".json"),
                       "full": full, "spec": spec, "spec_path": source, "spec_sha256": pin["sha256"]}
        tasks.add(task)
    if tasks != TASKS:
        raise ValueError("Require the exact seven retained native scoring tasks")
    return {"path": registry_path, "sha256": checksum, "registry": registry}, views


def ensure_new_run_links(root, runs):
    """Add unique new aliases only; never replace original or conflicting paths."""
    directory = root / "results/runs"
    directory.mkdir(parents=True, exist_ok=True)
    for name, spec in runs.items():
        if not re.fullmatch(r"[A-Za-z0-9_.-]+(?:_output16384_v1|_mixed_4k16k_scoring_v1)", name):
            raise ValueError("Only new revision run aliases are authorized")
        target = owned(root, spec["folder"])
        if target.name != name or not target.is_dir():
            continue
        if name.endswith("_mixed_4k16k_scoring_v1") and not (target / "completion.json").is_file():
            continue
        link = directory / name
        if link.is_symlink():
            if link.resolve() != target:
                raise ValueError("New run alias points at another source")
        elif link.exists():
            raise ValueError("New run alias conflicts with an existing original path")
        else:
            link.symlink_to(target, target_is_directory=True)


def derived_score_status(view):
    folder, spec = view["folder"], view["spec"]
    marker = read(folder / "completion.json")
    pending = {"task_id": view["task_id"], "run_id": view["run_id"], "kind": "derived_native_scoring",
               "generation_budget_condition": None, "planned": view["planned"], "terminal": False,
               "native_metrics_valid": None, "scored_benchmark_completed": False}
    if not marker:
        return pending
    manifest = read(folder / "run_manifest.json", {})
    cfg = read(view["config_path"], {})
    union = marker.get("full_test_id_union_validation", {})
    condition = marker.get("condition")
    if (condition not in SCORING_CONDITIONS or marker.get("spec_sha256") != digest(spec)
            or marker.get("configuration_sha256") != sha(view["config_path"])
            or marker.get("run_manifest_sha256") != sha(folder / "run_manifest.json")
            or cfg.get("run_id") != view["run_id"] or manifest.get("configuration") != cfg
            or manifest.get("configuration_sha256") != marker["configuration_sha256"]
            or manifest.get("planned_cases") != view["planned"]
            or manifest.get("generation_budget_condition") != condition
            or cfg.get("mixed_budget_scoring", {}).get("condition") != condition
            or cfg["mixed_budget_scoring"].get("original_full_configuration_sha256") != spec["full_config_sha256"]
            or union.get("complete") is not True or union.get("union_matches_full_test_ids") is not True
            or union.get("expected_test_case_count") != view["planned"]
            or union.get("unique_observed_case_count") != view["planned"]
            or any(union.get(k) != 0 for k in ["missing_case_count", "extra_case_count", "duplicate_case_count"])
            or marker.get("native_labels_and_denominator_unchanged") is not True
            or marker.get("retry_or_resampling") is not False):
        raise ValueError("Derived completion/config/manifest differs from exact native mixed-budget union")
    if marker.get("scoring_exit_code") != 0:
        return {**pending, "terminal": True, "execution_success": False,
                "generation_budget_condition": condition, "scoring_exit_code": marker.get("scoring_exit_code")}
    scores_path = folder / "scores.json"
    scores = read(scores_path, {})
    budget_path = folder / "per_case_budget_map.json"
    budget_map = read(budget_path, {}).get("budgets_by_raw_filename", {})
    output_lock_path = folder / "mixed_budget_output_lock.json"
    output_lock = read(output_lock_path, {})
    invocation = read(folder / "native_scorer_invocation.json", {})
    values = set(budget_map.values())
    actual = (CONDITION if values == {4096, 16384} else "RETAINED_4K_COMPLETE_UNDER_BUDGET_REVISION"
              if values == {4096} else "PROSPECTIVE_16K_FULL_TASK" if values == {16384} else None)
    counts = dict(Counter(map(str, budget_map.values())))
    if (sha(scores_path) != marker.get("scores_sha256") or scores.get("planned") != view["planned"]
            or scores.get("generation_budget_condition") != condition or actual != condition
            or len(budget_map) != view["planned"] or scores.get("generation", {}).get("output_budget_counts") != counts
            or scores.get("protocol_variant") != view["full"]["variant"] + "__" + condition
            or scores.get("native_parser_and_metric_implementation_unchanged") is not True
            or scores.get("original_case_denominator_unchanged") is not True
            or read(folder / "mixed_scoring_spec.json") != spec
            or output_lock.get("spec_sha256") != digest(spec) or output_lock.get("native_denominator") != view["planned"]
            or output_lock.get("per_case_budget_map_sha256") != sha(budget_path)
            or invocation.get("output_lock_sha256") != sha(output_lock_path)
            or cfg["mixed_budget_scoring"].get("per_case_budget_map", {}).get("sha256") != sha(budget_path)):
        raise ValueError("Derived score changed its budget label, source denominator or native-parser contract")
    return {**pending, "terminal": True, "execution_success": marker.get("generation_exit_code") == 0,
            "generation_budget_condition": condition, "output_budget_counts": counts,
            "scoring_exit_code": 0, "scores_sha256": marker["scores_sha256"]}


def publish_scoring_views(root, state, registry_record, views, destination_root, bridge, scanner, native):
    if registry_record is None:
        return {}
    runtime = destination_root / RUNTIME_RELATIVE / "scoring"
    registry_path = registry_record["path"]
    copy_pin(root, bridge, scanner, registry_path, runtime / registry_path.name, registry_record["sha256"])
    for name, expected in registry_record["registry"]["code_files_sha256"].items():
        source = Path(name)
        copy_pin(root, bridge, scanner, source, runtime / "shared_infrastructure" / (expected + "-" + source.name), expected)
    watcher = read(Path(registry_record["registry"]["state_file"]), {})
    summaries = {}
    for name, view in views.items():
        copy_pin(root, bridge, scanner, view["spec_path"], runtime / view["spec_path"].name, view["spec_sha256"])
        result = derived_score_status(view)
        observed = watcher.get("tasks", {}).get(view["task_id"], {}).get("result", {})
        if not result["terminal"] and observed.get("state") == "existing_native4k_completed_unchanged":
            original_folder = view["project_root"] / "results/runs" / view["full"]["run_id"]
            result.update(reused_original_native4k=True, reused_run_id=view["full"]["run_id"],
                          terminal=True,
                          generation_budget_condition="RETAINED_4K_COMPLETE_UNDER_BUDGET_REVISION",
                          original_completion_sha256=sha(original_folder / "completion.json"),
                          original_scores_sha256=sha(original_folder / "scores.json"))
            original_status = native.outcome_status({**view, "folder": original_folder, "kind": "full_test"})
            result.update(native_metrics_valid=original_status.get("native_metrics_valid"),
                          scored_benchmark_completed=original_status.get("native_metrics_valid") is True,
                          native_metric_issues=original_status.get("native_metric_issues", []))
        if result["terminal"] and not result.get("reused_original_native4k"):
            if result.get("scoring_exit_code") == 0:
                native_status = native.outcome_status({**view, "kind": "full_test"})
                result.update(native_metrics_valid=native_status.get("native_metrics_valid"),
                              scored_benchmark_completed=native_status.get("native_metrics_valid") is True,
                              native_metric_issues=native_status.get("native_metric_issues", []))
            destination = destination_root / "results/runs" / name
            for filename in SCORE_METADATA:
                source = view["folder"] / filename
                if source.is_file():
                    copy_pin(root, bridge, scanner, source, destination / filename, max_bytes=90 * 1024 * 1024)
            copy_pin(root, bridge, scanner, view["config_path"], destination / "frozen_config.json", max_bytes=90 * 1024 * 1024)
            write(destination / "upload_snapshot.json", result)
            (destination / "README.md").write_text("# " + view["task_id"] + " — native scoring of retained and prospective outputs\n\n"
                 + "Budget condition: **" + result["generation_budget_condition"] + "**. "
                   "The complete original case denominator, native parser and metrics are retained.\n\n"
                 + "[Scores](scores.json) · [Unmodified native summary](native_scores_unmodified.json) · [Per-case scores](per_case_scores.json) · [Budget map](per_case_budget_map.json) · [Run manifest](run_manifest.json) · [Completion](completion.json)\n\n"
                 + "This folder contains a derived scoring view. Original trajectories remain in their source runs; no second raw-trajectory archive is created here.\n")
        summaries[name] = result
    write(runtime / "scoring_views.json", summaries)
    return summaries


def validate_pair(spec, item):
    """Validate new-condition identity; defer the brief response/receipt race."""
    req = read(item["request_path"])
    filename = digest([spec["task_id"], spec["original"]["variant"], req["case_id"]]) + ".json"
    if (req["case_id"] not in spec["ids"] or item["filename"] != filename
            or req.get("task") != spec["task_id"] or req.get("variant") != spec["original"]["variant"]
            or req.get("request_sha256") != digest(req["payload"])
            or req["payload"].get("model") != MODEL
            or set(req["payload"]) != {"model", "messages", *spec["revised"]["generation"]}
            or any(req["payload"].get(k) != v for k, v in spec["revised"]["generation"].items())):
        raise ValueError("Raw request differs from the frozen 16k condition")
    receipt = read(spec["folder"] / "dispatch" / filename, {})
    if (receipt.get("condition") != CONDITION or receipt.get("plan_sha256") != spec["plan_sha256"]
            or receipt.get("case_id") != req["case_id"] or receipt.get("request_sha256") != req["request_sha256"]
            or receipt.get("output_budget") != 16384
            or receipt.get("server_identity_sha256") not in {e["server_identity_sha256"] for e in spec["plan"]["endpoints"]}):
        raise ValueError("Dispatch receipt differs from frozen plan or GPU identity")
    if item.get("response_path"):
        resp = read(item["response_path"])
        if (resp.get("condition") != CONDITION or resp.get("model") != MODEL or resp.get("model_revision") != REVISION
                or any(resp.get(k) != req.get(k) for k in ("task", "variant", "case_id", "split"))
                or resp.get("request_sha256") != req["request_sha256"]
                or resp.get("status") not in {"completed", "transport_error", "server_error"}):
            raise ValueError("Response belongs to another condition or original request")
        if resp.get("status") == "completed":
            api = resp.get("response", {})
            choices = api.get("choices", [])
            if (resp.get("http_status") != 200 or api.get("model") != MODEL or len(choices) != 1
                    or resp.get("text") != (choices[0].get("message", {}).get("content") or "")
                    or resp.get("finish_reason") != choices[0].get("finish_reason")):
                raise ValueError("Saved final differs from the original completed API envelope")
        if receipt.get("response_sha256") is None:
            return False
        if receipt["response_sha256"] != sha(item["response_path"]):
            raise ValueError("Completed receipt response bytes changed")
    return True


def copy_pin(root, bridge, scanner, source, destination, expected=None, max_bytes=16 * 1024 * 1024):
    source = owned(root, source)
    if (source.suffix not in {".json", ".jsonl", ".py", ".md", ".csv", ".txt", ".sh", ".sbatch", ".log"}
            or scanner.secret_filename(Path(source.name)) or source.stat().st_size > max_bytes):
        raise ValueError("Unsafe or oversized publication source")
    return bridge.copy_scanned(source, destination, scanner, expected)


def publish_dispatch(spec, destination, index, bridge, scanner):
    groups, records = {}, []
    raw_groups = {r["filename"]: r.get("archive_sha256", "pending") for r in index}
    for source in sorted((spec["folder"] / "dispatch").glob("*.json")):
        raw = source.read_bytes()
        scanner.scan_bytes(raw)
        value = json.loads(raw)
        expected = digest([spec["task_id"], spec["original"]["variant"], value.get("case_id")]) + ".json"
        if (source.name != expected or value.get("case_id") not in spec["ids"]
                or value.get("condition") != CONDITION or value.get("plan_sha256") != spec["plan_sha256"]):
            raise ValueError("Dispatch provenance leaves the new cohort")
        group = raw_groups.get(source.name, "pending")
        member = "dispatch/" + source.name
        groups.setdefault(group, {})[member] = raw
        records.append({"filename": source.name, "case_id": value["case_id"], "sha256": hashlib.sha256(raw).hexdigest(),
                        "saved_response_sha256": value.get("response_sha256"), "group": group, "member": member})
    paths = {}
    for group, files in groups.items():
        raw = bridge.metadata_archive(files)
        checksum = hashlib.sha256(raw).hexdigest()
        relative = "dispatch_metadata_batches/" + checksum + ".tar.gz"
        target = destination / relative
        if target.is_file() and target.read_bytes() != raw:
            raise ValueError("Previously published content-addressed receipt archive changed")
        if not target.exists():
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(raw)
            scanner.scan_file(target)
        paths[group] = {"archive": relative, "archive_sha256": checksum}
    for row in records:
        row.update(paths[row.pop("group")])
    if read(destination / "dispatch_index.json") != records:
        write(destination / "dispatch_index.json", records)


def publish_metadata(root, state, plans, runs, destination_root, bridge, scanner):
    runtime = destination_root / RUNTIME_RELATIVE
    for record in plans:
        plan = record["plan"]
        copy_pin(root, bridge, scanner, record["path"], runtime / record["path"].name, record["sha256"])
        for endpoint in plan["endpoints"]:
            path = pinned(root, {"path": endpoint["server_identity_file"], "sha256": endpoint["server_identity_sha256"]})
            copy_pin(root, bridge, scanner, path, runtime / "server_identities" / (endpoint["server_identity_sha256"] + ".json"), endpoint["server_identity_sha256"])
    code = {**PINS, str((state / "publish_budget_revision.py").relative_to(root)): sha(state / "publish_budget_revision.py")}
    tests = state / "test_budget_publication.py"
    if tests.is_file():
        code[str(tests.relative_to(root))] = sha(tests)
    budget = root / ".local/evaluation_revision_2026-10-18/budget_queue"
    for record in plans:
        code[str((budget / "run_budget_revision.py").relative_to(root))] = record["plan"]["code_sha256"]
    dependencies = []
    for name, expected in sorted(code.items()):
        source = root / name
        relative = "shared_infrastructure/" + expected + "-" + source.name
        copy_pin(root, bridge, scanner, source, runtime / relative, expected)
        dependencies.append({"source": name, "sha256": expected, "browsable_copy": relative})
    write(runtime / "publication_dependencies.json", dependencies)
    for name, spec in runs.items():
        if not validate_manifest(spec):
            continue
        destination = destination_root / "results/runs" / name
        for filename in ("run_manifest.json", "progress.json", "generation_completion.json"):
            source = spec["folder"] / filename
            if source.is_file():
                copy_pin(root, bridge, scanner, source, destination / filename)
        copy_pin(root, bridge, scanner, spec["config_path"], destination / "source_frozen_config_4096.json", spec["item"]["entry"]["config_sha256"])
        write(destination / "frozen_config_16384.json", spec["revised"])
        cp = spec["checkpoint_path"]
        copy_pin(root, bridge, scanner, cp, destination / "parent_4096_checkpoint.json", spec["item"]["parent_checkpoint"]["sha256"])
        copy_pin(root, bridge, scanner, spec["plan_path"], destination / "output_budget_revision_plan.json", spec["plan_sha256"])
        index = read(destination / "trajectory_index.json", [])
        publish_dispatch(spec, destination, index, bridge, scanner)


def run_snapshot(spec, index, status):
    return {"task_id": spec["task_id"], "run_id": spec["run_id"], "source_run_id": spec["source_run_id"],
            "condition": CONDITION, "this_cohort_output_budget": 16384, "retained_parent_output_budget": 4096,
            "case_scope": "all_never_dispatched_at_clean_pause", "planned_cohort_cases": spec["planned"],
            "original_source_cases": spec["item"]["entry"]["case_count"],
            "uploaded_trajectories": len(index), "uploaded_saved_responses": sum(r.get("response_sha256") is not None for r in index),
            "response_status_counts": dict(Counter(r.get("status", "unknown") for r in index)),
            "plan_sha256": spec["plan_sha256"], "parent_checkpoint_sha256": spec["item"]["parent_checkpoint"]["sha256"],
            "whole_task_metrics_require_original4k_and_new16k_union": True,
            "raw_saved_responses_are_not_benchmark_metrics": True, **status}


def publish_once(root, state, native, bridge, scanner, plan_pins, *, check_only=False, prepare_checkout=False):
    plans, runs = load_runs(root, plan_pins)
    scoring_registry, scoring_views = load_scoring_views(root, state, plan_pins)
    ready = {name: spec for name, spec in runs.items() if validate_manifest(spec)}
    if check_only:
        counts = {}
        with tempfile.TemporaryDirectory(prefix="budget-publication-preflight-") as temporary:
            publish_metadata(root, state, plans, runs, Path(temporary), bridge, scanner)
            publish_scoring_views(root, state, scoring_registry, scoring_views, Path(temporary), bridge, scanner, native)
            for name, spec in ready.items():
                items = native.new_trajectories(spec["folder"], set(), outcome(spec)["generation_terminal"])
                valid = [item for item in items if validate_pair(spec, item)]
                for item in valid:
                    for kind in ("request", "response"):
                        if item.get(kind + "_path"):
                            scanner.scan_file(item[kind + "_path"])
                counts[name] = {"planned": spec["planned"], "ready_saved_pairs": len(valid), "deferred_receipt_updates": len(items) - len(valid)}
        if prepare_checkout:
            native.helpers.confirm_destination()
            bridge.initialize_checkout(native, state, {**runs, **scoring_views})
            native.git("sparse-checkout", "add", "--no-cone", "/" + RUNTIME_RELATIVE + "/")
        return {"stage": "checked_without_publication", "ready": True, "runs": counts,
                "registered_new_runs": len(runs), "remote_mutation_performed": False,
                "registered_derived_scoring_views": len(scoring_views),
                "checkout_prepared": prepare_checkout, "original_publishers_untouched": True}
    privacy = native.helpers.confirm_destination()
    bridge.initialize_checkout(native, state, {**runs, **scoring_views})
    native.git("sparse-checkout", "add", "--no-cone", "/" + RUNTIME_RELATIVE + "/")
    ensure_new_run_links(root, {**runs, **scoring_views})
    if scoring_registry:
        write(state / "activated_scoring_watch_plan.json", {"path": str(scoring_registry["path"]),
              "sha256": scoring_registry["sha256"], "registered_derived_scoring_views": len(scoring_views)})
    snapshots, release_record, assets = {}, None, {}
    for name, spec in ready.items():
        destination = native.CHECKOUT / "results/runs" / name
        index_path = destination / "trajectory_index.json"
        index = read(index_path, [])
        uploaded = {r["filename"] for r in index if r.get("response_sha256") is not None or not (spec["folder"] / "responses" / r["filename"]).is_file()}
        status = outcome(spec)
        pending = native.new_trajectories(spec["folder"], uploaded, status["generation_terminal"])
        pending = [item for item in pending if validate_pair(spec, item)]
        for offset in range(0, len(pending), 50):
            batch = pending[offset:offset + 50]
            for item in batch:
                for kind in ("request", "response"):
                    path = item.get(kind + "_path")
                    if path:
                        scanner.scan_file(path)
                        if sha(path) != item[kind + "_sha256"]:
                            raise ValueError("Raw trajectory bytes changed before archival")
            if release_record is None:
                release_record, assets = native.release()
            index = bridge.merge_index(index, native.archive_batch(name, batch, release_record, assets, destination))
        if pending:
            write(index_path, index)
        snapshot = run_snapshot(spec, index, status)
        write(destination / "upload_snapshot.json", snapshot)
        parent_name = Path(spec["checkpoint"]["parent_run_directory"]).name
        text = ("# " + spec["task_id"] + " — 16,384-token continuation\n\n"
                + "**" + CONDITION + "**. " + str(snapshot["uploaded_saved_responses"]) + "/" + str(spec["planned"]) + " new-cohort responses archived.\n\n"
                + "Only cases never dispatched at the clean pause enter this folder. "
                  "[Original 4,096-token source](../" + parent_name + ") and its raw outputs remain preserved. "
                  "Full-task metrics require the original and new case union and must carry the mixed-budget label.\n\n"
                + "[Case index](trajectory_index.json) · [Run manifest](run_manifest.json) · [Revision plan](output_budget_revision_plan.json) · [Parent checkpoint](parent_4096_checkpoint.json) · [Dispatch receipts](dispatch_index.json)\n\n"
                + "Release archives preserve exact request/response JSON, including reasoning, usage and failures. "
                  "Generation artifacts do not establish completed benchmark metrics. No retries or resampling of previously executed cases.\n")
        (destination / "README.md").write_text(text)
        snapshots[name] = snapshot
    publish_metadata(root, state, plans, runs, native.CHECKOUT, bridge, scanner)
    score_snapshots = publish_scoring_views(root, state, scoring_registry, scoring_views, native.CHECKOUT, bridge, scanner, native)
    owned_paths = ["results/runs/" + name for name in {**runs, **scoring_views}] + [RUNTIME_RELATIVE]
    existing = [name for name in owned_paths if (native.CHECKOUT / name).exists()]
    if existing:
        native.git("add", "-f", "--sparse", "--", *existing)
    staged = native.git("diff", "--cached", "--name-only").stdout.splitlines()
    if any(not any(name.startswith(prefix + "/") for prefix in owned_paths) for name in staged):
        raise ValueError("Publication staged a path outside this new condition")
    for name in staged:
        path = native.CHECKOUT / name
        if path.is_file():
            scanner.scan_file(path)
    if staged:
        bridge.check_staged_whitespace(native, staged)
        native.git("commit", "-m", "Publish separately labeled 16k continuation trajectories")
    ahead = int(native.git("rev-list", "--count", "refs/remotes/origin/main..HEAD").stdout.strip())
    if ahead:
        for _ in range(8):
            native.helpers.confirm_destination()
            if native.git("push", "origin", "HEAD:refs/heads/main", allow_failure=True).returncode == 0:
                break
            native.git("fetch", "--filter=blob:none", "origin", "main")
            native.git("rebase", "FETCH_HEAD")
        else:
            raise RuntimeError("New-condition publication push did not complete")
    return {"stage": "watching", "ready": True, "updated_at_pacific": stamp(), "condition": CONDITION,
            "commit_sha": native.git("rev-parse", "HEAD").stdout.strip(), "repository_visibility": privacy["visibility"],
            "destination_policy_sha256": privacy["destination_policy_sha256"], "runs": snapshots,
            "registered_new_runs": len(runs), "original_publishers_untouched": True,
            "derived_scoring_views": score_snapshots,
            "generation_or_scoring_performed": False, "raw_saved_responses_are_not_benchmark_metrics": True}


def main():
    global STOP
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, required=True)
    parser.add_argument("--plan", type=Path, action="append", required=True)
    parser.add_argument("--plan-sha256", action="append", required=True)
    parser.add_argument("--check-only", action="store_true")
    parser.add_argument("--prepare-checkout", action="store_true", help="Read-only GitHub verification/fetch in check-only mode")
    parser.add_argument("--once", action="store_true")
    parser.add_argument("--interval", type=int, default=60)
    args = parser.parse_args()
    if len(args.plan) != len(args.plan_sha256) or (args.prepare_checkout and not args.check_only):
        parser.error("Require matching plan/hash arguments; prepare-checkout is check-only")
    root = args.root.resolve()
    state = root / ".local/evaluation_revision_2026-10-18/publication"
    state.mkdir(parents=True, exist_ok=True)
    plans = [{"path": str(path.resolve()), "sha256": expected} for path, expected in zip(args.plan, args.plan_sha256)]
    native, bridge, scanner = load_helpers(root, state)
    def stop(signum, frame):
        global STOP
        STOP = True
    signal.signal(signal.SIGTERM, stop)
    signal.signal(signal.SIGINT, stop)
    with (state / "publisher.lock").open("a") as own_lock:
        fcntl.flock(own_lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        while not STOP:
            try:
                with (root / ".local/evaluation_publication.lock").open("a") as global_lock:
                    deadline = time.monotonic() + 45
                    while True:
                        try:
                            fcntl.flock(global_lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
                            break
                        except BlockingIOError:
                            if time.monotonic() >= deadline:
                                raise TimeoutError("Another publication writer owns the shared lock")
                            time.sleep(.25)
                    receipt = publish_once(root, state, native, bridge, scanner, plans,
                                           check_only=args.check_only, prepare_checkout=args.prepare_checkout)
                receipt.update(pid=os.getpid(), gpu_allocation=0)
            except Exception as exc:
                detail = str(exc)[:1000]
                try:
                    scanner.scan_bytes(detail.encode())
                except Exception:
                    detail = "Error detail withheld by credential scanner"
                receipt = {**read(state / "status.json", {}), "stage": "retry_pending", "ready": False,
                           "last_retry_at_pacific": stamp(), "error_type": type(exc).__name__, "error_message": detail,
                           "generation_or_scoring_performed": False, "original_publishers_untouched": True}
            write(state / "status.json", receipt)
            print(json.dumps({key: receipt.get(key) for key in ("stage", "ready", "commit_sha", "error_type", "error_message")}), flush=True)
            if args.once or args.check_only:
                return 0 if receipt["ready"] else 1
            for _ in range(max(1, args.interval)):
                if STOP:
                    break
                time.sleep(1)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
