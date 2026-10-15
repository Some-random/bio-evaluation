"""Run one frozen ImageCLEF2019 baseline once, then score offline."""
import argparse
import datetime as dt
import json
from pathlib import Path
import subprocess
import sys
from run_local_labbench_multimodal import ROOT, write_json


def execute(path):
    settings = json.loads(path.read_text())
    if settings["approved_task_ids"] != ["V04"]:
        raise ValueError("Wrong benchmark")
    folder = ROOT / "results/runs" / settings["run_id"]
    if (folder / "completion.json").exists():
        raise ValueError("Existing completion cannot be resampled")
    generation = subprocess.run([sys.executable, "-u", "scripts/run_local_labbench_multimodal.py", "--config", str(path)], cwd=ROOT)
    scoring = subprocess.run([sys.executable, "-u", "scripts/score_vqamed2019_native.py", "--run", settings["run_id"]], cwd=ROOT) if (folder / "run_manifest.json").exists() else None
    write_json(folder / "completion.json", {"generation_exit_code": generation.returncode, "scoring_exit_code": scoring.returncode if scoring else None,
        "finished_at_utc": dt.datetime.now(dt.timezone.utc).isoformat(), "retry_or_resampling": False})
    return generation.returncode or (scoring.returncode if scoring else 1)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", type=Path, required=True)
    raise SystemExit(execute(parser.parse_args().config))
