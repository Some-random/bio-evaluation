"""One-time sequential queue of frozen local evaluation jobs; no provider calls."""
import argparse
import datetime as dt
import fcntl
import json
import os
from pathlib import Path
import subprocess
import sys
import time

from run_local_labbench import ROOT, file_digest, write_json


def run(queue_path, state_directory=None):
    state = state_directory or ROOT / ".local/local_benchmark_queue"
    state.mkdir(parents=True, exist_ok=True)
    lock = (state / "queue.lock").open("a")
    fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
    initial_queue = json.loads(queue_path.read_text())
    gpu_sets = {tuple(json.loads((ROOT / job["config"]).read_text())["gpu_ids"]) for job in initial_queue["jobs"]}
    if len(gpu_sets) != 1:
        raise ValueError("Queue must contain exactly one physical GPU assignment")
    queue_gpus = list(next(iter(gpu_sets)))
    if len(queue_gpus) != 1 or type(queue_gpus[0]) is not int:
        raise ValueError("Invalid physical GPU assignment")
    history = state / "progress.json"
    prior = json.loads(history.read_text()) if history.exists() else {}
    if prior and Path(prior["queue"]).resolve() != queue_path.resolve():
        raise ValueError("Previous terminal history belongs to another queue")
    process = {"pid": os.getpid(), "started_at_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
               "queue": str(queue_path), "gpu_ids": queue_gpus, "openai_calls": False}
    write_json(state / "worker_process.json", process)
    finished = prior.get("finished", {}).copy()
    # Preserve every prior terminal failure, even without a run manifest.
    # Resume independent queued jobs; never resubmit an uncertain/failed case.
    while True:
        queue = json.loads(queue_path.read_text())
        jobs = queue["jobs"]
        pending = [j for j in jobs if j["config"] not in finished]
        if not pending:
            write_json(state / "progress.json", {**process, "stage": "waiting_for_prepared_tasks" if queue["accept_more"] else "completed",
                       "finished": finished, "updated_at_utc": dt.datetime.now(dt.timezone.utc).isoformat()})
            if not queue["accept_more"]:
                lock.close()
                return
            time.sleep(5)
            continue
        job = pending[0]
        config = ROOT / job["config"]
        settings = json.loads(config.read_text())
        if settings.get("gpu_ids") != process["gpu_ids"]:
            raise ValueError("Queue GPU differs from frozen run GPU")
        folder = ROOT / "results/runs" / settings["run_id"]
        completion = folder / "completion.json"
        if completion.exists():
            result = json.loads(completion.read_text())
            finished[job["config"]] = {"run_id": settings["run_id"], "reused_existing_completion": True, **result}
            continue
        executor = ROOT / job["executor"]
        if executor.parent != ROOT / "scripts" or not executor.is_file():
            raise ValueError("Executor is outside the reviewed workspace scripts")
        log = ROOT / "logs/local_suite" / (settings["run_id"] + ".log")
        log.parent.mkdir(parents=True, exist_ok=True)
        write_json(state / "progress.json", {**process, "stage": "running", "active_run": settings["run_id"],
                   "active_config_sha256": file_digest(config), "finished": finished,
                   "log": str(log.relative_to(ROOT)), "updated_at_utc": dt.datetime.now(dt.timezone.utc).isoformat()})
        with log.open("a") as handle:
            result = subprocess.run([sys.executable, "-u", str(executor), "--config", str(config)],
                                    cwd=ROOT, stdin=subprocess.DEVNULL, stdout=handle, stderr=handle)
        finished[job["config"]] = {"run_id": settings["run_id"], "exit_code": result.returncode,
                                   "finished_at_utc": dt.datetime.now(dt.timezone.utc).isoformat()}
        if result.returncode:
            # Preserve uncertain requests; continue independent authorized jobs.
            # This failed config remains in durable finished history forever.
            write_json(state / "progress.json", {**process, "stage": "stopped_after_run_error",
                       "active_run": settings["run_id"], "finished": finished,
                       "updated_at_utc": dt.datetime.now(dt.timezone.utc).isoformat()})
            continue


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--queue", type=Path, required=True)
    parser.add_argument("--state-dir", type=Path)
    args = parser.parse_args()
    run(args.queue, args.state_dir)
