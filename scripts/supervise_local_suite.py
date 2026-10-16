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


def terminal_failed_run(config_name, run_id, history):
    result = history.get(config_name, {})
    return (result.get("run_id") == run_id and type(result.get("exit_code")) is int
            and result["exit_code"] != 0)


def completion_failed(result):
    if type(result.get("generation_exit_code")) is not int or result["generation_exit_code"] != 0:
        return True
    codes = [value for key, value in result.items() if key.endswith("_exit_code") and value is not None]
    if any(type(code) is not int or code != 0 for code in codes):
        return True
    if result.get("scoring_exit_code") == 0:
        return False
    # PathVQA deliberately scores only its full union, after generation audits.
    return not (result.get("case_scope") == "task_shard_only"
                and result.get("shard_scoring_performed") is False
                and result.get("generation_audit_exit_code") == 0
                and result.get("status") == "generation_audited")


def aggregate_status(config_name, source_jobs, history, root=ROOT):
    cfg = json.loads((root / config_name).read_text())
    run_id = cfg["run_id"]
    completion = root / "results/runs" / run_id / "completion.json"
    if completion.exists():
        result = json.loads(completion.read_text())
        return {"run_id": run_id, "status": "failed" if completion_failed(result) else "complete"}
    for source_name, source_run in source_jobs:
        source_done = root / "results/runs" / source_run / "completion.json"
        if not source_done.exists() and terminal_failed_run(source_name, source_run, history):
            return {"run_id": run_id, "status": "blocked", "reason": "source_terminal_failure_without_execution_artifacts"}
    prefixes = {
        "local_description_": "local_description_shard_aggregation.json",
        "local_reaction_": "local_reaction_shard_aggregation.json",
        "local_extended_seven_gpu_": "local_extended_seven_gpu_aggregation.json",
        "local_bioreason_": "local_bioreason_shard_aggregation.json",
        "local_posttrain_protein_": "local_posttrain_protein_shard_aggregation.json",
        "local_pathvqa_seven_gpu_": "local_pathvqa_seven_gpu_aggregation.json",
    }
    for prefix, filename in prefixes.items():
        if not Path(config_name).name.startswith(prefix):
            continue
        path = root / "reports" / filename
        if not path.exists():
            break
        report = json.loads(path.read_text())
        task = cfg.get("task_id") or cfg.get("approved_task_ids", [None])[0]
        state = report.get("tasks", {}).get(task, report)
        if "states" in report:
            state = next((entry for entry in report["states"]
                          if entry.get("native_split") == cfg.get("native_split")), {})
        if state.get("status") == "blocked":
            return {"run_id": run_id, "status": "blocked", "reason": state.get("detail")}
        break
    return {"run_id": run_id, "status": "pending"}


def run():
    state = ROOT / ".local/local_suite_supervision"
    state.mkdir(parents=True, exist_ok=True)
    lock = (state / "worker.lock").open("a")
    fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
    previous_signature = None
    while True:
        queues = sorted((ROOT / "configs").glob("local_benchmark_queue*.json"))
        planned, finished, failures, unscored_terminal_failures = [], [], [], []
        aggregates = {}
        history = {}
        for path in (ROOT / ".local").glob("local_benchmark_queue*/progress.json"):
            history.update(json.loads(path.read_text()).get("finished", {}))
        sealed = True
        for path in queues:
            queue = json.loads(path.read_text())
            sealed &= not queue.get("accept_more", False)
            for job in queue["jobs"]:
                config = json.loads((ROOT / job["config"]).read_text())
                run_id = config["run_id"]
                planned.append(run_id)
                if config.get("aggregate_config_file"):
                    aggregates.setdefault(config["aggregate_config_file"], []).append((job["config"], run_id))
                completion = ROOT / "results/runs" / run_id / "completion.json"
                if completion.exists():
                    result = json.loads(completion.read_text())
                    finished.append(run_id)
                    if completion_failed(result):
                        failures.append(run_id)
                elif terminal_failed_run(job["config"], run_id, history):
                    # An executor can fail before it writes a run manifest.
                    # This is terminal queue evidence, never a fabricated score
                    # or completed biological evaluation.
                    finished.append(run_id)
                    failures.append(run_id)
                    unscored_terminal_failures.append(run_id)
        aggregate_states = [aggregate_status(name, jobs, history) for name, jobs in sorted(aggregates.items())]
        aggregates_terminal = all(item["status"] != "pending" for item in aggregate_states)
        aggregate_failures = [item["run_id"] for item in aggregate_states if item["status"] in ("failed", "blocked")]
        drained = sealed and len(finished) == len(planned) and aggregates_terminal
        # Metadata only: never open model prompts, references or raw outputs here.
        artifacts = list((ROOT / "results/runs").glob("qwen38*/scores.json"))
        artifacts += list((ROOT / "results/runs").glob("qwen38*/progress.json"))
        artifacts += list((ROOT / "results/runs").glob("qwen38*/completion.json"))
        artifacts += queues + list((ROOT / ".local").glob("local_benchmark_queue*/progress.json"))
        artifacts += list((ROOT / "reports").glob("local_*aggregation.json"))
        signature = [(str(p), p.stat().st_mtime_ns, p.stat().st_size) for p in sorted(artifacts)]
        report_status = {}
        if signature != previous_signature or drained:
            for script in ("update_executed_interpretations.py", "summarize_local_suite.py", "update_results_at_a_glance.py"):
                result = subprocess.run([sys.executable, str(ROOT / "scripts" / script)],
                                        cwd=ROOT, capture_output=True, text=True)
                report_status[script] = {"exit_code": result.returncode,
                    "stdout": result.stdout[-1500:], "stderr": result.stderr[-1500:]}
            previous_signature = signature
        record = {"pid": os.getpid(), "updated_at_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
            "scope": "Offline reporting only for existing one-time authorized queues",
            "queued_jobs": len(planned), "finished_jobs": len(finished),
            "failed_run_ids": failures, "queues_sealed": sealed,
            "terminal_failures_without_scores": unscored_terminal_failures,
            "aggregate_states": aggregate_states,
            "aggregate_failures": aggregate_failures,
            "inference_started_or_retried_by_supervisor": False,
            "report_status": report_status,
            "stage": ("complete_with_failures" if failures or aggregate_failures else "complete") if drained else "monitoring"}
        path = ROOT / "reports/local_suite_supervision.json"
        temporary = path.with_suffix(".tmp")
        temporary.write_text(json.dumps(record, indent=2) + "\n")
        temporary.replace(path)
        if record["stage"] in ("complete", "complete_with_failures"):
            return
        time.sleep(30)


if __name__ == "__main__":
    run()
