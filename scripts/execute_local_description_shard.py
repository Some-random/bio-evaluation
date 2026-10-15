"""Execute an explicitly approved description shard once, then score offline."""
import argparse
import csv
import datetime as dt
import json
from pathlib import Path
import subprocess
import sys

from prepare_local_extended_shards import shard_metadata
from prepare_local_description_shards import ROOT, RUNNER, SCORER, file_digest, approval_for
from run_local_labbench_multimodal import write_json


def mark_shard_scores(folder, settings):
    metadata = shard_metadata(settings)
    path = folder / "scores.json"
    summary = json.loads(path.read_text())
    if summary["planned"] != settings["source_stop_index"] - settings["source_start_index"]:
        raise ValueError("Scored shard count differs from frozen range")
    summary.update(case_scope="task_shard_only", **metadata,
                   shard_metric_interpretation="Partial task only. Full-test native ROUGE is computed separately from the complete union of raw predictions; shard bootstrap metric values must never be averaged.")
    write_json(path, summary)
    csv_path = folder / "metrics.csv"
    with csv_path.open(newline="") as handle:
        reader = csv.DictReader(handle)
        fields = list(reader.fieldnames)
        rows = list(reader)
    additions = {name: value for name, value in metadata.items() if not isinstance(value, (dict, list))}
    fields += [name for name in additions if name not in fields]
    with csv_path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for row in rows:
            writer.writerow({**row, "case_scope": "task_shard_only", **additions})
    return summary


def execute(config_path):
    settings = json.loads(config_path.read_text())
    if (settings.get("aggregate_only") is not False or settings.get("generator_execution_allowed") is not True
            or settings.get("case_scope") != "task_shard_only" or settings.get("runner") != RUNNER):
        raise ValueError("Only executable frozen task shards are permitted")
    authorization = approval_for(config_path, settings)
    shard_metadata(settings)
    aggregate_path = ROOT / settings["aggregate_config_file"]
    aggregate = json.loads(aggregate_path.read_text())
    matching = [entry for entry in aggregate["shard_configs"] if entry["shard_index"] == settings["shard_index"]]
    if len(matching) != 1 or matching[0]["config_sha256"] != file_digest(config_path):
        raise ValueError("Shard config differs from preregistered aggregate manifest")
    folder = ROOT / "results/runs" / settings["run_id"]
    # Do not turn a previously finished/failed job into a new generation attempt.
    if (folder / "completion.json").exists():
        raise ValueError("Shard already finished; no retries/resampling permitted")
    generation = subprocess.run([sys.executable, "-u", str(ROOT / RUNNER), "--config", str(config_path)], cwd=ROOT)
    scoring_code = None
    error = None
    if (folder / "run_manifest.json").exists():
        scoring = subprocess.run([sys.executable, "-u", str(ROOT / SCORER), "--run", settings["run_id"]], cwd=ROOT)
        scoring_code = scoring.returncode
        if scoring_code == 0:
            try:
                mark_shard_scores(folder, settings)
            except Exception as exc:
                scoring_code, error = 1, str(exc)
    folder.mkdir(parents=True, exist_ok=True)
    record = {"generation_exit_code": generation.returncode, "scoring_exit_code": scoring_code,
              "finished_at_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
              "config_file": str(config_path.resolve().relative_to(ROOT)),
              "configuration_sha256": file_digest(config_path), "case_scope": "task_shard_only",
              "retry_or_resampling": False, "execution_approval": authorization, **shard_metadata(settings)}
    if error:
        record["error"] = error
    if (folder / "run_manifest.json").exists():
        record["run_manifest_sha256"] = file_digest(folder / "run_manifest.json")
    if (folder / "scores.json").exists():
        record["scores_sha256"] = file_digest(folder / "scores.json")
    write_json(folder / "completion.json", record)
    return generation.returncode or scoring_code or (0 if scoring_code == 0 else 1)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", required=True, type=Path)
    raise SystemExit(execute(parser.parse_args().config))
