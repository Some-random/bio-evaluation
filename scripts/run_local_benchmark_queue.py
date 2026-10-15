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
    process = {"pid": os.getpid(), "started_at_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
               "queue": str(queue_path), "gpu_ids": [5], "openai_calls": False}
    write_json(state / "worker_process.json", process)
    finished = {}
    while True:
        queue = json.loads(queue_path.read_text())
        jobs = queue["jobs"]
        pending = [j for j in jobs if j["config"] not in finished]
        if not pending:
            write_json(state / "progress.json", {**process, "stage": "waiting_for_prepared_tasks" if queue["accept_more"] else "completed",
                       "finished": finished, "updated_at_utc": dt.datetime.now(dt.timezone.utc).isoformat()})
            if not queue["accept_more"]:
                return
            time.sleep(5)
            continue
        job = pending[0]
        config = ROOT / job["config"]
        settings = json.loads(config.read_text())
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
            # Preserve uncertain requests for audit; never silently resample.
            write_json(state / "progress.json", {**process, "stage": "stopped_after_run_error",
                       "active_run": settings["run_id"], "finished": finished,
                       "updated_at_utc": dt.datetime.now(dt.timezone.utc).isoformat()})
            return


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--queue", type=Path, required=True)
    parser.add_argument("--state-dir", type=Path)
    args = parser.parse_args()
    run(args.queue, args.state_dir)
