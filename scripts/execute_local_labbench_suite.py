"""Run one pre-frozen LAB category, then score in a separate process."""
import argparse
import datetime as dt
import json
from pathlib import Path
import subprocess
import sys

from run_local_labbench import ROOT, write_json


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", type=Path, required=True)
    args = parser.parse_args()
    settings = json.loads(args.config.read_text())
    runner = settings.get("runner", "scripts/run_local_labbench.py")
    generation = subprocess.run([sys.executable, "-u", str(ROOT / runner), "--config", str(args.config)], cwd=ROOT)
    folder = ROOT / "results/runs" / settings["run_id"]
    if not (folder / "run_manifest.json").exists():
        raise SystemExit(generation.returncode or 1)
    scoring = subprocess.run([sys.executable, "-u", str(ROOT / "scripts/score_local_labbench_suite.py"),
                              "--run", settings["run_id"]], cwd=ROOT)
    write_json(folder / "completion.json", {"generation_exit_code": generation.returncode,
               "scoring_exit_code": scoring.returncode, "finished_at_utc": dt.datetime.now(dt.timezone.utc).isoformat()})
    raise SystemExit(generation.returncode or scoring.returncode)
