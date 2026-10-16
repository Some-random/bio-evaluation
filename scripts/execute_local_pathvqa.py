"""Execute one frozen source-qualified PathVQA image run, then score offline."""
import argparse
import datetime as dt
import json
from pathlib import Path
import subprocess
import sys

from run_local_labbench_multimodal import ROOT, write_json


def execute(config_path):
    settings = json.loads(config_path.read_text())
    if settings["approved_task_ids"] != ["V03"] or settings["scorer"] != "scripts/score_local_pathvqa.py":
        raise ValueError("Wrong source-qualified PathVQA contract")
    folder = ROOT / "results/runs" / settings["run_id"]
    if (folder / "completion.json").exists():
        raise ValueError("Finished run cannot be resampled")
    generation = subprocess.run([sys.executable, "-u", "scripts/run_local_labbench_multimodal.py", "--config", str(config_path)], cwd=ROOT)
    if not (folder / "run_manifest.json").exists():
        return generation.returncode or 1
    scoring = subprocess.run([sys.executable, "-u", settings["scorer"], "--run", settings["run_id"]], cwd=ROOT)
    write_json(folder / "completion.json", {"generation_exit_code": generation.returncode, "scoring_exit_code": scoring.returncode,
        "finished_at_utc": dt.datetime.now(dt.timezone.utc).isoformat(), "retry_or_resampling": False})
    return generation.returncode or scoring.returncode


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", type=Path, required=True)
    raise SystemExit(execute(parser.parse_args().config))
