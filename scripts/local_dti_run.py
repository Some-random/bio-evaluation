"""Authorized frozen local DTI likelihood requests; never reads answer labels."""
import argparse
from collections import Counter
import concurrent.futures as cf
import datetime as dt
import fcntl
import json
import os
from pathlib import Path
import threading
import time

from local_dti_common import (ROOT, MODEL, REVISION, VARIANT, call, digest, extract_score,
                              file_digest, payload_for, validate_server, write_json)


def read_config(config_path):
    settings = json.loads(config_path.read_text())
    local = json.loads((ROOT / "configs/local_model.json").read_text())
    if (not settings.get("execution_authorized") or not local.get("benchmark_inference_authorized")
            or "P43" not in local["approved_task_ids"] or local["model"] != MODEL or local["revision"] != REVISION):
        raise ValueError("P43 requires root review/freeze and local dispatch authorization")
    if not 1 <= settings["concurrency"] <= 4:
        raise ValueError("Concurrency exceeds the serving budget")
    mandatory = {settings["input_file"], settings["review_file"], settings["scorer_reference_file"],
                 "scripts/local_dti_common.py", "scripts/local_dti_run.py", "scripts/local_dti_score.py"}
    if not mandatory <= set(settings["frozen_files_sha256"]):
        raise ValueError("Input/review/scoring protocol not completely frozen")
    for name, expected in settings["frozen_files_sha256"].items():
        if name == settings["scorer_reference_file"]:
            # The offline scorer verifies this pre-inference hash. The request
            # worker does not open the answer file, even for hashing.
            continue
        if file_digest(ROOT / name) != expected:
            raise ValueError("Frozen file changed: " + name)
    review = json.loads((ROOT / settings["review_file"]).read_text())
    if not review.get("reviewed") or review["dataset"] != settings["dataset"]:
        raise ValueError("Input review not completed for this dataset")
    cases = [json.loads(s) for s in (ROOT / settings["input_file"]).read_text().splitlines() if s]
    ids = [c["case_id"] for c in cases]
    if not cases or ids != review["approved_case_ids"] or len(set(ids)) != len(ids):
        raise ValueError("Cases differ from exact ordered reviewed scope")
    if set(ids) & {r["case_id"] for r in review.get("held_cases", [])}:
        raise ValueError("Held case found")
    for case in cases:
        if not case["case_id"].startswith(settings["dataset"] + ":"):
            raise ValueError("Case belongs to another source dataset")
        payload_for(case, settings)
    server = json.loads((ROOT / settings["server_state_file"]).read_text())
    validate_server(server, settings)
    return settings, cases, server


def run(config_path):
    settings, cases, server = read_config(config_path)
    code, models = call(settings["endpoint"] + "/models", timeout=15)
    if code != 200 or not any(r["id"] == MODEL for r in models.get("data", [])):
        raise ValueError("Pinned model unavailable")
    folder = ROOT / "results/runs" / settings["run_id"]
    folder.mkdir(parents=True, exist_ok=True)
    lock = (folder / "worker.lock").open("a")
    fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
    manifest = {"configuration": settings, "configuration_sha256": file_digest(config_path),
                "case_contract_sha256": digest(cases), "runner_sha256": file_digest(Path(__file__)),
                "planned_cases": len(cases), "solver_tools": [], "answer_keys_available_to_solver": False,
                "server": server, "model_selection_on_test": False}
    path = folder / "run_manifest.json"
    if path.exists() and json.loads(path.read_text()) != manifest:
        raise ValueError("Existing run contract changed")
    write_json(path, manifest)
    write_json(folder / "worker_process.json", {"pid": os.getpid(), "started_at_utc": dt.datetime.now(dt.timezone.utc).isoformat(), "server": server})
    stopped = threading.Event()
    states = Counter()
    started = time.monotonic()

    def execute(case):
        identity = digest([case["task"], case["variant"], case["case_id"]])
        req_path = folder / "requests" / (identity + ".json")
        res_path = folder / "responses" / (identity + ".json")
        if res_path.exists():
            return json.loads(res_path.read_text())["status"]
        if req_path.exists():
            return "interrupted_unknown_completion"
        if stopped.is_set():
            return "not_dispatched_after_error"
        payload = payload_for(case, settings)
        metadata = {key: case[key] for key in ["task", "case_id", "variant", "split"]}
        request_hash = digest(payload)
        write_json(req_path, {**metadata, "payload": payload, "request_sha256": request_hash,
                             "supplied_fields": ["source_definition", "full_SELFIES", "complete_protein_sequence"], "dataset": settings["dataset"]})
        before = time.monotonic()
        code, response = call(settings["endpoint"] + "/chat/completions", payload)
        record = {**metadata, "model": MODEL, "model_revision": REVISION, "request_sha256": request_hash,
                  "http_status": code, "response": response, "elapsed_seconds": time.monotonic() - before,
                  "saved_at_utc": dt.datetime.now(dt.timezone.utc).isoformat()}
        if code == 200:
            try:
                score = extract_score(response)
                record.update(status="completed", score=score, text=response["choices"][0]["message"]["content"], finish_reason=response["choices"][0]["finish_reason"])
            except (ValueError, KeyError, TypeError):
                record["status"] = "invalid_likelihood_output"
                stopped.set()
        else:
            record["status"] = "transport_error" if code == 0 else "server_error"
            stopped.set()
        write_json(res_path, record)
        return record["status"]

    def progress(stage):
        value = {"run": settings["run_id"], "dataset": settings["dataset"], "stage": stage, "planned": len(cases),
                 "finished": sum(states.values()), "statuses": dict(states), "elapsed_seconds": time.monotonic() - started,
                 "updated_at_utc": dt.datetime.now(dt.timezone.utc).isoformat()}
        write_json(folder / "progress.json", value);print(json.dumps(value), flush=True)

    progress("running")
    with cf.ThreadPoolExecutor(max_workers=settings["concurrency"]) as pool:
        for future in cf.as_completed([pool.submit(execute, case) for case in cases]):
            try:
                states[future.result()] += 1
            except Exception:
                states["worker_exception"] += 1;stopped.set()
            progress("running")
    complete = states["completed"] == len(cases)
    progress("generation_complete" if complete else "incomplete")
    return 0 if complete else 1


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", type=Path, required=True)
    args = parser.parse_args()
    raise SystemExit(run(args.config))
