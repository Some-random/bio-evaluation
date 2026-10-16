"""Publish existing native-run artifacts without executing or scoring a model.

Runs alongside the original CPU supervisor, which retains its own aggregation
runtime and lock. Only this uploader writes the public upload checkpoint.
"""
import argparse
from datetime import datetime, timezone
import fcntl
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import signal
import time

SUPERVISOR_SHA256 = "a242714f8aecd8ab254b02e21639f5e3c014e22176d00000632a271d6160242b"
STOP = False


def stamp():
    return datetime.now(timezone.utc).isoformat()


def read(path):
    return json.loads(path.read_text()) if path.is_file() else {}


def write(path, value):
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(value, indent=2) + "\n")
    temporary.chmod(0o600)
    temporary.replace(path)


def install_upload_only_callbacks(native):
    # The frozen publisher calls these hooks before publication. Replace both
    # with metadata reads; never call its CPU scorer or report generator.
    native.aggregate_ready = lambda registry, runs: read(native.HERE / "aggregation_status.json")
    native.refresh_reports = lambda runs: read(native.HERE / "report_update_status.json")


def load_native(root):
    path = root / ".local/remaining_evaluations/pool_supervisor_final_v2.py"
    if hashlib.sha256(path.read_bytes()).hexdigest() != SUPERVISOR_SHA256:
        raise ValueError("Frozen native supervisor source changed")
    spec = importlib.util.spec_from_file_location("native_artifact_publisher", path)
    native = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(native)
    install_upload_only_callbacks(native)
    return native


def publish_once(native, root):
    privacy = native.helpers.confirm_destination()
    lock_path = root / ".local/evaluation_publication.lock"
    with lock_path.open("a") as lock:
        fcntl.flock(lock, fcntl.LOCK_EX)
        status = native.cycle(native.HERE / "supervisor_plan.json")
        status.update(repository_private_verified=privacy["private"],
            repository_visibility=privacy["visibility"], publication_authorized=True,
            destination_policy_sha256=privacy["destination_policy_sha256"],
            publication_writer="upload_only_publication_worker",
            generation_or_scoring_performed=False)
        write(native.HERE / "upload_status.json", status)
        return status


def main():
    global STOP
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, required=True)
    parser.add_argument("--interval", type=int, default=60)
    parser.add_argument("--once", action="store_true")
    args = parser.parse_args()
    root = args.root.resolve()
    state = root / ".local/remaining_evaluations"
    native = load_native(root)
    status_path = state / "public_upload_status.json"
    with (state / "public_upload_only.lock").open("a") as own_lock:
        fcntl.flock(own_lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        def stop(signum, frame):
            global STOP
            STOP = True
        signal.signal(signal.SIGTERM, stop)
        signal.signal(signal.SIGINT, stop)
        while not STOP:
            try:
                status = publish_once(native, root)
                receipt = {**status, "pid": os.getpid(), "slurm_job_id": os.environ.get("SLURM_JOB_ID"),
                    "slurm_step_id": os.environ.get("SLURM_STEP_ID"), "ready": True,
                    "original_supervisor_untouched": True, "gpu_allocation": 0}
            except Exception as error:
                # Preserve the last successful run-bearing upload checkpoint.
                # A retry timestamp must not masquerade as fresher run data.
                receipt = {**read(status_path), "stage": "retry_pending", "ready": False,
                    "last_retry_at_utc": stamp(), "error_type": type(error).__name__,
                    "pid": os.getpid(), "slurm_job_id": os.environ.get("SLURM_JOB_ID"),
                    "original_supervisor_untouched": True, "gpu_allocation": 0}
            write(status_path, receipt)
            print(json.dumps({key: receipt.get(key) for key in ("stage", "ready", "updated_at_utc", "last_retry_at_utc", "error_type")}), flush=True)
            if args.once:
                return
            for _ in range(max(1, args.interval)):
                if STOP:
                    break
                time.sleep(1)


if __name__ == "__main__":
    main()
