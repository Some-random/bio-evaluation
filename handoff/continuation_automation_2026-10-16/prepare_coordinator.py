"""Freeze a reviewable CPU coordinator config and its Slurm submission script."""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import json
from pathlib import Path
import shlex

from coordinator import save, sha


def prepare(root, scorer_archive, scorer_receipt, run_dir):
    root = Path(root).resolve()
    state = root / ".local/continuation_2026-10-16"
    base = state / "p36_preparation"
    existing_path = root / ".local/remaining_evaluations/cpu_supervisor_final_v2_bootstrap.json"
    existing = json.loads(existing_path.read_text())
    scorer_archive = Path(scorer_archive).resolve()
    scorer_receipt = Path(scorer_receipt).resolve()
    run_dir = Path(run_dir).resolve()
    if not run_dir.is_relative_to(state / "runs") or not (run_dir / "run_manifest.json").is_file():
        raise ValueError("Expected the existing P36 continuation run")
    scorer_report = json.loads(scorer_receipt.read_text())
    archive = {"path": str(scorer_archive), "sha256": sha(scorer_archive)}
    if (scorer_report.get("status") != "ready" or scorer_report.get("archive_sha256") != archive["sha256"]
            or scorer_report.get("all_frozen_dependency_versions_preserved") is not True
            or scorer_report.get("relocation_verified") is not True
            or scorer_report.get("launcher") != "score_python.sh"):
        raise ValueError("Portable P36 scorer receipt is not verified and relocatable")
    wheels = [record for record in existing["wheels"] if Path(record["path"]).name.startswith("PyYAML-")]
    if len(wheels) != 1:
        raise ValueError("Expected one existing pinned PyYAML wheel")
    for record in [existing["archive"], *wheels]:
        if sha(record["path"]) != record["sha256"]:
            raise ValueError("Existing CPU runtime receipt does not match its artifact")
    names = [state / "coordinator.py", state / "bootstrap_coordinator.py", state / "prepare_coordinator.py",
        state / "upload_continuation.py", root / "scripts/watch_evaluation_reporting.py",
        root / "scripts/refresh_evaluation_reporting.py", root / "scripts/update_grouped_evaluation_reports.py",
        root / "scripts/publication_destination.py", root / "configs/publication_destination.json",
        root / "scripts/update_results_at_a_glance.py", root / "scripts/daily_backup.py",
        root / ".local/litqa2_replay/incremental_upload.py", root / ".local/litqa2_replay/github_credential_helper.py",
        root / ".local/litqa2_replay/parallel_upload.py", existing_path, scorer_receipt,
        base / "proposed_config.json", base / "proposed_authorization.json",
        base / "score_p36.py", base / "p36_contract.py", run_dir / "run_manifest.json"]
    config = {"created_at_utc": datetime.now(timezone.utc).isoformat(), "root": str(root),
        "state_dir": str(state), "run_dir": str(run_dir), "planned_cases": 59,
        "archive": existing["archive"], "wheels": wheels,
        "coordinator_script": str(state / "coordinator.py"),
        "files_sha256": {str(path): sha(path) for path in names},
        "scorer": {"archive": archive, "receipt": str(scorer_receipt),
            "launcher_relative": "score_python.sh", "launcher_sha256": scorer_report["launcher_sha256"],
            "script": str(base / "score_p36.py")},
        "restart_delay_seconds": 60,
        "children": {
            "reporting": [str(root / "scripts/watch_evaluation_reporting.py"), "--root", str(root), "--interval", "300"],
            "continuation_upload": [str(state / "upload_continuation.py"), "--root", str(root),
                "--run-dir", str(run_dir), "--config", str(base / "proposed_config.json"), "--interval", "60"]},
        "resources": {"partition": "il-cpu", "qos": "il-cpu", "cpus": 2, "memory_gb": 4,
            "wall_time": "14-00:00:00", "gpus": 0},
        "restrictions": ["Never launch or retry generation", "Never modify existing supervisor/worker plans or runtimes",
            "One frozen P36 offline score attempt; failures and interruptions are not retried", "Reporting and trajectory publishing only through the two isolated children to the explicitly authorized repository visibility"]}
    config_path = state / "coordinator_config.json"
    save(config_path, config)
    (state / "logs").mkdir(exist_ok=True)
    sbatch_path = state / "coordinator.sbatch"
    sbatch_path.write_text("\n".join([
        "#!/bin/bash", "#SBATCH --partition=il-cpu", "#SBATCH --qos=il-cpu", "#SBATCH --cpus-per-task=2",
        "#SBATCH --mem=4G", "#SBATCH --time=14-00:00:00", "#SBATCH --job-name=bio-eval-reporting",
        "#SBATCH --output=" + str(state / "logs/coordinator-%j.log"), "set -euo pipefail", "umask 077",
        'local_base="${SLURM_TMPDIR:-/tmp}"',
        'runtime_dir="$(mktemp -d "$local_base/bio-eval-continuation-${SLURM_JOB_ID}-XXXXXX")"',
        'trap \'rm -rf -- "$runtime_dir"\' EXIT',
        "python3 " + shlex.quote(str(state / "bootstrap_coordinator.py")) + " --config " + shlex.quote(str(config_path))
            + " --config-sha256 " + sha(config_path) + ' --runtime-dir "$runtime_dir"', ""]))
    sbatch_path.chmod(0o700)
    receipt = {"config": str(config_path), "config_sha256": sha(config_path),
        "sbatch": str(sbatch_path), "sbatch_sha256": sha(sbatch_path),
        "submission_command": "sbatch --parsable " + shlex.quote(str(sbatch_path)),
        "submitted": False, "resources": config["resources"]}
    save(state / "coordinator_preparation.json", receipt)
    return receipt


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument("--scorer-archive", type=Path)
    parser.add_argument("--scorer-receipt", type=Path)
    parser.add_argument("--run-dir", type=Path)
    args = parser.parse_args()
    state = args.root / ".local/continuation_2026-10-16"
    portable = state / "p36_preparation/portable_runtime"
    receipt = prepare(args.root,
        args.scorer_archive or portable / "p36-scoring-py310.tar.gz",
        args.scorer_receipt or portable / "runtime_report.json",
        args.run_dir or state / "runs/p36-qwen3.8-27b-biot5-reviewed59-20261016")
    print(json.dumps(receipt, indent=2))


if __name__ == "__main__":
    main()
