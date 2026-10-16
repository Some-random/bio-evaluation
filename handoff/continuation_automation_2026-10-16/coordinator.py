"""CPU-only report/uploader supervision and one-shot frozen P36 scoring."""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import fcntl
import hashlib
import json
import math
import os
from pathlib import Path
import signal
import subprocess
import sys
import tempfile
import time


STOP = False


def stamp():
    return datetime.now(timezone.utc).isoformat()


def sha(path):
    result = hashlib.sha256()
    with Path(path).open("rb") as handle:
        for chunk in iter(lambda: handle.read(8 * 1024 * 1024), b""):
            result.update(chunk)
    return result.hexdigest()


def save(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = None
    try:
        with tempfile.NamedTemporaryFile(dir=path.parent, prefix="." + path.name + ".", delete=False) as handle:
            temporary = Path(handle.name)
            handle.write((json.dumps(value, indent=2, allow_nan=False) + "\n").encode())
            handle.flush()
            os.fsync(handle.fileno())
        temporary.chmod(0o600)
        temporary.replace(path)
    finally:
        if temporary is not None and temporary.exists():
            temporary.unlink()


def read(path):
    return json.loads(Path(path).read_text())


def validate_pins(config):
    for name, expected in config["files_sha256"].items():
        if sha(name) != expected:
            raise ValueError("Pinned continuation source changed: " + str(Path(name).name))


class Coordinator:
    def __init__(self, config, runtime, popen=subprocess.Popen, clock=time.monotonic):
        self.config = config
        self.root = Path(config["root"])
        self.state = Path(config["state_dir"])
        self.run = Path(config["run_dir"])
        self.runtime = Path(runtime)
        self.popen = popen
        self.clock = clock
        self.children = {}
        self.score_process = None
        self.score_log = None
        self.scoring_path = self.state / "scoring_status.json"
        self.scoring = read(self.scoring_path) if self.scoring_path.is_file() else {"stage": "waiting_for_dispatch"}
        interrupted = self.scoring.get("stage") == "running"
        if interrupted:
            # A previous coordinator died after recording its one allowed
            # attempt. It is unsafe to repeat a possibly completed scorer.
            self.scoring.update(stage="interrupted_no_retry", updated_at_utc=stamp())
            save(self.scoring_path, self.scoring)
        self.state.mkdir(parents=True, exist_ok=True)
        (self.state / "logs").mkdir(exist_ok=True)
        for name in config["children"]:
            self.children[name] = {"process": None, "log": None, "restart_at": 0,
                "restarts": 0, "stage": "not_started", "last_exit_code": None}
        if interrupted:
            existing = (self.run / "scores.json").is_file()
            self.score_completion(None, existing=existing)
            self.scoring.update(interruption_recorded=True)
            if not existing:
                self.scoring["stage"] = "interrupted_no_retry"
            save(self.scoring_path, self.scoring)

    def environment(self):
        env = dict(os.environ)
        for key in ("PYTHONHOME", "PYTHONPATH", "VIRTUAL_ENV", "OPENAI_API_KEY", "ANTHROPIC_API_KEY", "HF_TOKEN", "HUGGING_FACE_HUB_TOKEN"):
            env.pop(key, None)
        env.update(PYTHONNOUSERSITE="1", PYTHONDONTWRITEBYTECODE="1",
            CUDA_VISIBLE_DEVICES="", OMP_NUM_THREADS="1", MKL_NUM_THREADS="1", OPENBLAS_NUM_THREADS="1")
        env["PATH"] = str(self.runtime / "python/bin") + os.pathsep + env.get("PATH", "")
        return env

    def maintain_child(self, name):
        child = self.children[name]
        process = child["process"]
        if process is not None:
            exit_code = process.poll()
            if exit_code is None:
                return
            child.update(process=None, last_exit_code=exit_code, stage="restart_wait",
                restart_at=self.clock() + self.config.get("restart_delay_seconds", 60), exited_at_utc=stamp())
            child["log"].close()
            child["log"] = None
            return
        if self.clock() < child["restart_at"]:
            return
        try:
            validate_pins(self.config)
            log = (self.state / "logs" / (name + ".log")).open("ab")
            argv = [str(self.runtime / "python/bin/python3.10"), "-u", *self.config["children"][name]]
            try:
                process = self.popen(argv, cwd=self.root, env=self.environment(),
                    stdout=log, stderr=subprocess.STDOUT, start_new_session=True)
            except Exception:
                log.close()
                raise
            child.update(process=process, log=log, stage="running", started_at_utc=stamp())
            child["restarts"] += 1
        except Exception as error:
            child.update(stage="restart_wait", restart_at=self.clock() + self.config.get("restart_delay_seconds", 60),
                error="Child startup failed (" + type(error).__name__ + ")")

    def score_completion(self, exit_code, existing=False):
        scores = self.run / "scores.json"
        valid = False
        metadata = {}
        if scores.is_file():
            try:
                value = read(scores)
                metric = value.get("metrics", {}).get("rougeL")
                valid = (value.get("task_id") == "P36" and value.get("planned") == self.config["planned_cases"]
                    and value.get("full_benchmark_complete") is False and type(metric) in (int, float)
                    and math.isfinite(metric))
                metadata = {key: value.get(key) for key in ["task_id", "planned", "completed", "case_scope",
                    "full_benchmark_complete", "all_declared_subset_outputs_saved", "missing_or_failed_slots", "metric_label"]}
                metadata["scores_sha256"] = sha(scores)
            except Exception:
                metadata = {"scores_readable": False}
        successful = valid and (existing or exit_code == 0)
        completion = {"run_id": self.run.name, "task_id": "P36", "finished_at_utc": stamp(),
            "status": "scored_partial_subset" if successful else "scoring_failed_no_retry",
            "scorer_exit_code": exit_code, "existing_scores_reused": existing,
            "full_benchmark_complete": False, "planned": self.config["planned_cases"],
            "metadata": metadata, "policy": "One frozen offline score attempt; no generation, retry, output repair, or full-benchmark completion claim."}
        completion_path = self.run / "completion.json"
        if not completion_path.exists():
            save(completion_path, completion)
        self.scoring.update(stage="completed_partial_subset" if successful else "failed_no_retry",
            scorer_exit_code=exit_code, updated_at_utc=stamp(), result_metadata=metadata,
            existing_scores_reused=existing)
        save(self.scoring_path, self.scoring)

    def maintain_scoring(self):
        if self.score_process is not None:
            exit_code = self.score_process.poll()
            if exit_code is None:
                return
            self.score_log.close()
            self.score_log = None
            self.score_process = None
            self.score_completion(exit_code)
            return
        if self.scoring.get("stage") in {"completed_partial_subset", "failed_no_retry", "interrupted_no_retry"}:
            return
        if (self.run / "scores.json").is_file():
            self.score_completion(None, existing=True)
            return
        dispatch = self.run / "dispatch_summary.json"
        if not dispatch.is_file():
            return
        self.scoring = {"stage": "running", "started_at_utc": stamp(),
            "dispatch_summary_sha256": sha(dispatch), "planned": self.config["planned_cases"],
            "attempts": 1, "automatic_retry": False}
        save(self.scoring_path, self.scoring)
        try:
            validate_pins(self.config)
            launcher = self.runtime / "scorer" / self.config["scorer"]["launcher_relative"]
            argv = [str(launcher), self.config["scorer"]["script"], "--run-dir", str(self.run)]
            self.score_log = (self.state / "logs/p36_scoring.log").open("ab")
            self.score_process = self.popen(argv, cwd=self.root, env=self.environment(),
                stdout=self.score_log, stderr=subprocess.STDOUT, start_new_session=True)
            self.scoring["pid"] = self.score_process.pid
            save(self.scoring_path, self.scoring)
        except Exception as error:
            if self.score_log is not None:
                self.score_log.close()
                self.score_log = None
            self.scoring["error"] = "Scorer startup failed (" + type(error).__name__ + ")"
            self.score_completion(None)

    def tick(self):
        for name in self.children:
            self.maintain_child(name)
        self.maintain_scoring()
        children = {name: {key: value for key, value in child.items()
            if key not in {"process", "log", "restart_at"}} | {
                "pid": child["process"].pid if child["process"] is not None else None,
                "restart_delay_remaining_seconds": max(0, round(child["restart_at"] - self.clock()))}
            for name, child in self.children.items()}
        ready = all(child["stage"] == "running" for child in self.children.values())
        status = {"stage": "watching" if ready else "degraded", "ready": ready, "updated_at_utc": stamp(),
            "slurm_job_id": os.environ.get("SLURM_JOB_ID"), "hostname": os.uname().nodename,
            "pid": os.getpid(), "python": sys.executable, "runtime_dir": str(self.runtime),
            "gpu_allocation": 0, "children": children, "scoring": self.scoring,
            "generation_policy": "Never launch or retry model generation."}
        save(self.state / "coordinator_status.json", status)
        return status

    def shutdown(self):
        processes = [child["process"] for child in self.children.values() if child["process"] is not None]
        if self.score_process is not None:
            processes.append(self.score_process)
        for process in processes:
            if process.poll() is None:
                try:
                    os.killpg(process.pid, signal.SIGTERM)
                except ProcessLookupError:
                    pass
        deadline = time.monotonic() + 15
        while any(process.poll() is None for process in processes) and time.monotonic() < deadline:
            time.sleep(0.2)
        for process in processes:
            if process.poll() is None:
                try:
                    os.killpg(process.pid, signal.SIGKILL)
                except ProcessLookupError:
                    pass


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", type=Path, required=True)
    parser.add_argument("--runtime-dir", type=Path, required=True)
    args = parser.parse_args()
    if not os.environ.get("SLURM_JOB_ID") or os.environ.get("SLURM_JOB_GPUS"):
        raise ValueError("Continuation coordinator requires a CPU-only Slurm allocation")
    config = read(args.config)
    validate_pins(config)
    state = Path(config["state_dir"])
    state.mkdir(parents=True, exist_ok=True)
    with (state / "coordinator.lock").open("a") as lock:
        fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        coordinator = Coordinator(config, args.runtime_dir)
        def stop(signum, frame):
            global STOP
            STOP = True
        signal.signal(signal.SIGTERM, stop)
        signal.signal(signal.SIGINT, stop)
        try:
            while not STOP:
                coordinator.tick()
                for _ in range(10):
                    if STOP:
                        break
                    time.sleep(1)
        finally:
            coordinator.shutdown()
            save(state / "coordinator_stop.json", {"stopped_at_utc": stamp(), "slurm_job_id": os.environ.get("SLURM_JOB_ID")})


if __name__ == "__main__":
    main()
