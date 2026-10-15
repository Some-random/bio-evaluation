"""One-time offline suite reporting while the already authorized queues run.

Does not start/retry inference, change queues, approve tasks, or contact providers.
Stops after all queued jobs have completion records and queues are sealed.
"""
import datetime as dt
import fcntl
import json
import os
from pathlib import Path
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parents[1]


def run():
    state = ROOT / ".local/local_suite_supervision"
    state.mkdir(parents=True, exist_ok=True)
    lock = (state / "worker.lock").open("a")
    fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
    previous_signature = None
    while True:
        queues = sorted((ROOT / "configs").glob("local_benchmark_queue*.json"))
        planned, finished, failures = [], [], []
        sealed = True
        for path in queues:
            queue = json.loads(path.read_text())
            sealed &= not queue.get("accept_more", False)
            for job in queue["jobs"]:
                config = json.loads((ROOT / job["config"]).read_text())
                run_id = config["run_id"]
                planned.append(run_id)
                completion = ROOT / "results/runs" / run_id / "completion.json"
                if completion.exists():
                    result = json.loads(completion.read_text())
                    finished.append(run_id)
                    if result.get("generation_exit_code") != 0 or result.get("scoring_exit_code") != 0:
                        failures.append(run_id)
        # Metadata only: never open model prompts, references or raw outputs here.
        artifacts = list((ROOT / "results/runs").glob("qwen38*/scores.json"))
        artifacts += list((ROOT / "results/runs").glob("qwen38*/progress.json"))
        signature = [(str(p), p.stat().st_mtime_ns, p.stat().st_size) for p in sorted(artifacts)]
        report_status = {}
        if signature != previous_signature:
            for script in ("update_executed_interpretations.py", "summarize_local_suite.py"):
                result = subprocess.run([sys.executable, str(ROOT / "scripts" / script)],
                                        cwd=ROOT, capture_output=True, text=True)
                report_status[script] = {"exit_code": result.returncode,
                    "stdout": result.stdout[-1500:], "stderr": result.stderr[-1500:]}
            previous_signature = signature
        record = {"pid": os.getpid(), "updated_at_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
            "scope": "Offline reporting only for existing one-time authorized queues",
            "queued_jobs": len(planned), "finished_jobs": len(finished),
            "failed_run_ids": failures, "queues_sealed": sealed,
            "inference_started_or_retried_by_supervisor": False,
            "report_status": report_status,
            "stage": "complete" if sealed and len(finished) == len(planned) else "monitoring"}
        path = ROOT / "reports/local_suite_supervision.json"
        temporary = path.with_suffix(".tmp")
        temporary.write_text(json.dumps(record, indent=2) + "\n")
        temporary.replace(path)
        if record["stage"] == "complete":
            return
        time.sleep(30)


if __name__ == "__main__":
    run()
