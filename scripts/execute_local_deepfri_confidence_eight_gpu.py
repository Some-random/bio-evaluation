#!/usr/bin/env python3
"""Execute activated DeepFRI confidence adaptations with the new strict eight-GPU runner."""
import argparse
from datetime import datetime, timezone
import json
from pathlib import Path
import subprocess
import sys

from score_local_genomics import file_digest, write_json

ROOT = Path(__file__).resolve().parents[1]


def execute(config_path, score_only=False):
    config_path = Path(config_path).resolve()
    settings = json.loads(config_path.read_text())
    if settings.get("proposal_status") != "frozen_for_authorized_execution" or settings.get("enabled") is not True:
        raise ValueError("Disabled proposal has no local execution authorization")
    if (settings.get("approved_task_ids") not in (["P12"], ["P13"], ["P14"], ["P15"])
            or settings.get("runner") != "scripts/run_local_labbench_eight_gpu.py"
            or settings.get("scorer") != "scripts/score_local_deepfri_confidence.py"
            or settings.get("scorer_python") != ".venv-vllm/bin/python"):
        raise ValueError("Unexpected task/runner/scorer contract")
    folder = ROOT / "results/runs" / settings["run_id"]
    completion = folder / "completion.json"
    if completion.exists():
        raise ValueError("Run already has a terminal completion record; no reruns/resampling")
    for name, expected in settings["frozen_files_sha256"].items():
        if file_digest(ROOT / name) != expected:
            raise ValueError("Frozen file changed: " + name)
    description = subprocess.run([str(ROOT / settings["scorer_python"]), str(ROOT / settings["scorer"]), "--describe-protocol"],
                                 check=True, capture_output=True, text=True)
    described = json.loads(description.stdout)
    if (described["protocol_sha256"] != settings["scoring_protocol_sha256"]
            or described["runtime"] != json.loads((ROOT / settings["scoring_runtime_file"]).read_text())):
        raise ValueError("Scoring protocol/runtime differs before inference")
    generation = scoring = None
    error = None
    started = datetime.now(timezone.utc).isoformat()
    try:
        if not score_only:
            # The runner independently enforces central authorization and
            # pinned loopback identity; the executor cannot extend either.
            generation = subprocess.run([sys.executable, "-u", str(ROOT / settings["runner"]), "--config", str(config_path)], cwd=ROOT).returncode
        if not (folder / "run_manifest.json").exists():
            raise ValueError("No immutable run manifest to score")
        scoring = subprocess.run([str(ROOT / settings["scorer_python"]), "-u", str(ROOT / settings["scorer"]), "--run", settings["run_id"], "--config", str(config_path)], cwd=ROOT).returncode
        if scoring == 0 and not (folder / "scores.json").exists():
            raise ValueError("Scorer returned success without a score artifact")
    except Exception as exc:
        error = type(exc).__name__ + ": " + str(exc)
    record = {"run_id": settings["run_id"], "task_id": settings["approved_task_ids"][0],
              "status": "completed" if generation in (None, 0) and scoring == 0 and error is None else "failed",
              "generation_exit_code": generation, "scoring_exit_code": scoring, "score_only": score_only,
              "started_at_utc": started, "finished_at_utc": datetime.now(timezone.utc).isoformat(),
              "configuration_sha256": file_digest(config_path),
              "runner_sha256": file_digest(ROOT / settings["runner"]),
              "scorer_sha256": file_digest(ROOT / settings["scorer"]),
              "scoring_protocol_sha256": settings["scoring_protocol_sha256"],
              "retry_or_resampling": False}
    if error:
        record["error"] = error
    for name in ("run_manifest.json", "scores.json", "scoring_output_lock.json"):
        if (folder / name).exists():
            record[name.removesuffix(".json") + "_sha256"] = file_digest(folder / name)
    write_json(completion, record)
    return (generation or 0) or (scoring or 0) or (1 if record["status"] != "completed" else 0)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", type=Path, required=True)
    parser.add_argument("--score-only", action="store_true")
    args = parser.parse_args()
    raise SystemExit(execute(args.config, args.score_only))
