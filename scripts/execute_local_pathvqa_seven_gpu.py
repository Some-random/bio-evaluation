"""Execute one exact approved PathVQA shard; audit generations without labels.

The full original native scorer is reserved for the offline union. Shard
completion preserves failed/missing generation slots instead of retrying them.
"""
import argparse
import datetime as dt
import json
from pathlib import Path
import subprocess
import sys

from prepare_local_pathvqa_seven_gpu import (ROOT, RUNNER, RUNNER_SHA256,
    cases_for, file_digest, raw_audit, require_approval)
from run_local_labbench_eight_gpu import write_json


def execute(config_path):
    config_path = config_path.resolve()
    name = str(config_path.relative_to(ROOT))
    settings = json.loads(config_path.read_text())
    plan = require_approval(ROOT, name)
    if (settings.get("aggregate_only") is not False or settings.get("generator_execution_allowed") is not True
            or settings.get("case_scope") != "task_shard_only" or settings.get("runner") != RUNNER
            or settings.get("approved_task_ids") != ["V03"]):
        raise ValueError("Only a preregistered executable PathVQA shard is permitted")
    entries = [row for row in plan["shards"] if row["config_file"] == name]
    if len(entries) != 1 or entries[0]["run_id"] != settings["run_id"]:
        raise ValueError("Shard does not belong to exact approved plan")
    cases = cases_for(ROOT, settings)
    folder = ROOT / "results/runs" / settings["run_id"]
    if (folder / "completion.json").exists():
        raise ValueError("Terminal shard cannot be rerun/resampled")
    generation_code = None
    audit_code = None
    error = None
    try:
        generation = subprocess.run([sys.executable, "-u", str(ROOT / RUNNER), "--config", str(config_path)], cwd=ROOT)
        generation_code = generation.returncode
        if (folder / "run_manifest.json").exists():
            raw_audit(ROOT, folder, cases, settings, file_digest(config_path))
            audit_code = 0
        else:
            error = "No immutable execution manifest; source server/generations cannot be validated"
    except Exception as exc:
        audit_code = 1
        error = type(exc).__name__ + ": " + str(exc)
    folder.mkdir(parents=True, exist_ok=True)
    record = {"generation_exit_code": generation_code, "generation_audit_exit_code": audit_code,
              "scoring_exit_code": None, "shard_scoring_performed": False,
              "status": "generation_audited" if audit_code == 0 else "generation_audit_failed",
              "finished_at_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
              "config_file": name, "configuration_sha256": file_digest(config_path),
              "runner_sha256": RUNNER_SHA256, "executor_sha256": file_digest(Path(__file__)),
              "case_scope": "task_shard_only", "shard_index": settings["shard_index"],
              "shard_count": settings["shard_count"], "planned": len(cases),
              "retry_or_resampling": False,
              "failure_policy": "Preserve actual source exit code and every missing/failed slot for the single full native group-denominator scorer; absent execution provenance blocks aggregation."}
    for filename, field in [("run_manifest.json", "run_manifest_sha256"), ("generation_output_lock.json", "generation_output_lock_sha256")]:
        if (folder / filename).exists():
            record[field] = file_digest(folder / filename)
    if error:
        record["error"] = error
    write_json(folder / "completion.json", record)
    return generation_code or (0 if audit_code == 0 else 1)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", required=True, type=Path)
    raise SystemExit(execute(parser.parse_args().config))
