"""Watch frozen shared-serving task specs and perform native CPU scoring once.

Run independently inside the retained CPU-supervisor allocation. Original pool
plans and source completion records stay unchanged. Migrated generation closes
with its distinct terminal marker; the full aggregate's native completion then
makes the original supervisor recognize that aggregate as already terminal.
"""
from __future__ import annotations

import argparse
import fcntl
import json
import os
from pathlib import Path
import time

import shared_vllm_scoring as scoring


def write_state(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(value, indent=2) + "\n")
    temporary.replace(path)


def frozen_plan(path):
    plan = scoring.read(path)
    if plan.get("schema_version") != 1 or not plan.get("spec_files"):
        raise scoring.ScoringError("Require a nonempty frozen v1 scoring-watch plan")
    if not 1 <= plan.get("poll_seconds", 20) <= 60:
        raise scoring.ScoringError("CPU watcher polling must be 1–60 seconds")
    code = plan.get("code_files_sha256", {})
    for name, expected in code.items():
        if not Path(name).is_absolute() or scoring.file_sha(name) != expected:
            raise scoring.ScoringError("Frozen watcher/adapter code changed: " + name)
    required = {str(Path(__file__).resolve()), str(Path(scoring.__file__).resolve()),
                str(Path(scoring.__file__).with_name("shared_vllm_resume.py").resolve())}
    if not required <= set(code):
        raise scoring.ScoringError("Watcher, scoring adapter and resume validator must all be pinned")
    paths = [str(Path(row["path"]).resolve()) for row in plan["spec_files"]]
    if len(paths) != len(set(paths)):
        raise scoring.ScoringError("Duplicate scoring specification")
    specs = []
    for row, path in zip(plan["spec_files"], paths):
        if scoring.file_sha(path) != row["sha256"]:
            raise scoring.ScoringError("Frozen task scoring specification changed: " + path)
        spec = scoring.read(path)
        specs.append((path, spec))
    return plan, specs


def legacy_aggregation_running(spec):
    """An explicit legacy coordinator binding avoids concurrent native calls."""
    binding = spec.get("legacy_aggregation_watch")
    if not binding:
        return False
    path = Path(binding["status_file"])
    if not path.exists():
        return False
    state = scoring.read(path)
    return any(state.get(name, {}).get("stage") == "running" for name in binding["names"])


def generation_ready(spec):
    root = Path(spec["project_root"]).resolve()
    full = scoring.checked_config(root, spec["full_config_file"], spec["full_config_sha256"])
    if (root / "results/runs" / full["run_id"] / "completion.json").exists():
        return True, "original_full_result_terminal"
    if legacy_aggregation_running(spec):
        return False, "legacy_native_aggregation_running"
    for source in spec["sources"]:
        cfg = scoring.checked_config(root, source["config_file"], source["config_sha256"])
        folder = scoring.generation_folder(root, cfg, source)
        if (folder / "shared_vllm_amendment.json").exists():
            if not (folder / "shared_vllm_generation_completion.json").exists():
                return False, "shared_generation_pending:" + cfg["run_id"]
        elif not (folder / "completion.json").exists():
            return False, "original_generation_pending:" + cfg["run_id"]
    return True, "all_sources_terminal"


def cycle(plan_path, expected_plan_sha, *, score_function=scoring.score_spec):
    if scoring.file_sha(plan_path) != expected_plan_sha:
        raise scoring.ScoringError("Scoring-watch plan changed after launch")
    plan, specs = frozen_plan(plan_path)
    state_path = Path(plan["state_file"])
    state = scoring.read(state_path) if state_path.exists() else {
        "schema_version": 1, "plan_sha256": expected_plan_sha, "tasks": {},
        "inference_dispatched": False, "native_scorers_unchanged": True}
    if state.get("plan_sha256") != expected_plan_sha:
        raise scoring.ScoringError("Existing watcher state belongs to a different frozen plan")
    for path, spec in specs:
        previous = state["tasks"].get(path, {})
        if previous.get("stage") in ("completed", "failed"):
            continue
        ready, reason = generation_ready(spec)
        if not ready:
            state["tasks"][path] = {"stage": "pending", "reason": reason, "updated_at_pacific": scoring.now()}
            continue
        state["tasks"][path] = {"stage": "validating_or_scoring", "updated_at_pacific": scoring.now()}
        write_state(state_path, state)
        try:
            result = score_function(spec)
            state["tasks"][path] = {"stage": "completed", "result": result,
                                   "updated_at_pacific": scoring.now()}
        except scoring.Pending as error:
            state["tasks"][path] = {"stage": "pending", "reason": str(error), "updated_at_pacific": scoring.now()}
        except Exception as error:
            # Native scorer attempts and source/provenance failures are retained;
            # an unattended watcher must never retry or select another score.
            state["tasks"][path] = {"stage": "failed", "error": type(error).__name__ + ": " + str(error),
                                   "automatic_retry": False, "updated_at_pacific": scoring.now()}
        state["updated_at_pacific"] = scoring.now()
        write_state(state_path, state)
    state["updated_at_pacific"] = scoring.now()
    state["all_terminal"] = all(state["tasks"].get(path, {}).get("stage") in ("completed", "failed") for path, spec in specs)
    state["all_completed"] = all(state["tasks"].get(path, {}).get("stage") == "completed" for path, spec in specs)
    write_state(state_path, state)
    return state, plan.get("poll_seconds", 20)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--plan", required=True, type=Path)
    parser.add_argument("--plan-sha256", required=True)
    parser.add_argument("--once", action="store_true")
    args = parser.parse_args()
    lock_path = args.plan.with_suffix(args.plan.suffix + ".worker.lock")
    lock_path.parent.mkdir(parents=True, exist_ok=True)
    with lock_path.open("a") as lock:
        fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        while True:
            state, poll = cycle(args.plan, args.plan_sha256)
            print(json.dumps({"updated_at_pacific": state["updated_at_pacific"],
                              "all_terminal": state["all_terminal"], "all_completed": state["all_completed"],
                              "task_stages": {name: row["stage"] for name, row in state["tasks"].items()}}), flush=True)
            if args.once or state["all_terminal"]:
                return 0 if state["all_completed"] else 1 if state["all_terminal"] else 0
            time.sleep(poll)


if __name__ == "__main__":
    raise SystemExit(main())
