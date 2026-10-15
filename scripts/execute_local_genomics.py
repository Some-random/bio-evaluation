#!/usr/bin/env python3
"""Execute an explicitly frozen authorized local genomic run, then score offline.

Proposed configurations are refused. The existing loopback runner independently
checks central task authorization and pinned serving identity before inference.
This module performs no work when imported.
"""
import argparse
from datetime import datetime, timezone
import json
from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]


def execute(config_path, score_only=False):
    config_path = Path(config_path).resolve()
    settings = json.loads(config_path.read_text())
    if settings.get("proposal_status") != "frozen_for_authorized_execution":
        raise ValueError("Proposed genomic config is not an authorized frozen execution config")
    if (settings.get("runner") != "scripts/run_local_labbench_multimodal.py"
            or settings.get("scorer") != "scripts/score_local_genomics.py"
            or settings.get("approved_task_ids") not in (["N01"], ["N02"], ["N03"])):
        raise ValueError("Unexpected genomic runner/scorer/task contract")
    folder = ROOT / "results/runs" / settings["run_id"]
    generation_code = None
    if not score_only:
        generation_code = subprocess.run([sys.executable, "-u", str(ROOT / settings["runner"]),
                                          "--config", str(config_path)], cwd=ROOT).returncode
    if not (folder / "run_manifest.json").exists():
        raise ValueError("No immutable local run manifest exists for offline scoring")
    scoring_code = subprocess.run([sys.executable, "-u", str(ROOT / settings["scorer"]),
                                  "--run", settings["run_id"], "--config", str(config_path)], cwd=ROOT).returncode
    path = folder / "completion.json"
    temporary = path.with_suffix(".json.tmp")
    temporary.write_text(json.dumps({"generation_exit_code": generation_code, "scoring_exit_code": scoring_code,
                                     "score_only": score_only, "finished_at_utc": datetime.now(timezone.utc).isoformat()}, indent=2) + "\n")
    temporary.chmod(0o600)
    temporary.replace(path)
    return (generation_code or 0) or scoring_code


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", type=Path, required=True)
    parser.add_argument("--score-only", action="store_true")
    args = parser.parse_args()
    raise SystemExit(execute(args.config, args.score_only))
