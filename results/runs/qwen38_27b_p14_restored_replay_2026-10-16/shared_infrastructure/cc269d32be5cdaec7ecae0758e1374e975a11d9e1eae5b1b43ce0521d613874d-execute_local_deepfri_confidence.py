#!/usr/bin/env python3
"""Execute only explicitly activated DeepFRI confidence adaptations; proposals refuse."""
import argparse
import json
from pathlib import Path
import subprocess
import sys

from score_local_genomics import file_digest

ROOT = Path(__file__).resolve().parents[1]


def execute(config_path, score_only=False):
    config_path = Path(config_path).resolve()
    settings = json.loads(config_path.read_text())
    if settings.get("proposal_status") != "frozen_for_authorized_execution" or settings.get("enabled") is not True:
        raise ValueError("Disabled proposal has no local execution authorization")
    if (settings.get("approved_task_ids") not in (["P12"], ["P13"], ["P14"], ["P15"])
            or settings.get("runner") != "scripts/run_local_labbench_multimodal.py"
            or settings.get("scorer") != "scripts/score_local_deepfri_confidence.py"
            or settings.get("scorer_python") != ".venv-vllm/bin/python"):
        raise ValueError("Unexpected task/runner/scorer contract")
    for name, expected in settings["frozen_files_sha256"].items():
        if file_digest(ROOT / name) != expected:
            raise ValueError("Frozen file changed: " + name)
    description = subprocess.run([str(ROOT / settings["scorer_python"]), str(ROOT / settings["scorer"]), "--describe-protocol"],
                                 check=True, capture_output=True, text=True)
    described = json.loads(description.stdout)
    if (described["protocol_sha256"] != settings["scoring_protocol_sha256"]
            or described["runtime"] != json.loads((ROOT / settings["scoring_runtime_file"]).read_text())):
        raise ValueError("Scoring protocol/runtime differs before inference")
    generation = 0
    if not score_only:
        # This existing runner independently enforces central authorization and
        # pinned loopback server identity; the executor cannot extend either.
        generation = subprocess.run([sys.executable, "-u", str(ROOT / settings["runner"]), "--config", str(config_path)], cwd=ROOT).returncode
    folder = ROOT / "results/runs" / settings["run_id"]
    if not (folder / "run_manifest.json").exists():
        raise ValueError("No immutable run manifest to score")
    scoring = subprocess.run([str(ROOT / settings["scorer_python"]), "-u", str(ROOT / settings["scorer"]), "--run", settings["run_id"], "--config", str(config_path)], cwd=ROOT).returncode
    return generation or scoring


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", type=Path, required=True)
    parser.add_argument("--score-only", action="store_true")
    args = parser.parse_args()
    raise SystemExit(execute(args.config, args.score_only))
