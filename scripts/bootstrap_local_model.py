"""Complete the authorized checkpoint setup and synthetic checks, without benchmarks."""
import argparse
from datetime import datetime, timedelta, timezone
import fcntl
import hashlib
import json
import os
from pathlib import Path
import signal
import socket
import subprocess
import sys
import time
import urllib.request

import local_vllm


ROOT = local_vllm.ROOT
STATUS = ROOT / "reports/local_model_deployment.json"


def process_start(pid):
    try:
        fields = Path(f"/proc/{pid}/stat").read_text().rsplit(")", 1)[1].split()
        return None if fields[0] == "Z" else fields[19]
    except (FileNotFoundError, ProcessLookupError):
        return None


def write_json(path, value):
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(value, indent=2) + "\n")
    temporary.replace(path)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--existing-download-pid", type=int)
    args = parser.parse_args()
    (ROOT / ".local").mkdir(exist_ok=True)
    lock = (ROOT / ".local/local_model_setup.lock").open("w")
    fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
    settings = local_vllm.config()
    if len(settings["gpu_ids"]) != 1 or settings["tensor_parallel_size"] != 1:
        raise SystemExit("This initial setup is limited to one GPU.")
    model_dir = Path(settings["model_directory"])
    env = local_vllm.environment(settings)
    state = {"model": settings["model"], "revision": settings["revision"],
             "gpu_ids": settings["gpu_ids"], "setup_pid": os.getpid(),
             "model_server_started": False, "weights_downloaded": False,
             "benchmark_cases_dispatched": 0,
             "scope": "checkpoint setup and fixed synthetic checks only"}

    def status(stage, **fields):
        state.update(fields)
        state.update(stage=stage, updated_at_PST=datetime.now(timezone(timedelta(hours=-8))).isoformat())
        write_json(STATUS, state)
        print(json.dumps({"stage": stage, **fields}), flush=True)

    server = None
    try:
        if args.existing_download_pid:
            pid = args.existing_download_pid
            start = process_start(pid)
            command = Path(f"/proc/{pid}/cmdline").read_bytes().split(b"\0") if start else []
            if start and not (b"scripts/local_vllm.py" in command and b"download" in command
                              and Path(f"/proc/{pid}/cwd").resolve() == ROOT):
                raise RuntimeError("Existing download process identity differs from this workspace.")
            status("waiting_for_existing_download", download_pid=pid)
            while start and process_start(pid) == start:
                time.sleep(5)
        if not (model_dir / "bio_evaluation_checkpoint.json").is_file():
            status("downloading")
            for attempt in range(1, 4):
                with (ROOT / "logs/local_model/qwen38_27b_download.log").open("a") as log:
                    value = subprocess.run([sys.executable, "scripts/local_vllm.py", "download"],
                                           cwd=ROOT, env=env, stdout=log, stderr=subprocess.STDOUT)
                if value.returncode == 0:
                    break
                status("download_retry", attempt=attempt, returncode=value.returncode)
                if attempt == 3:
                    raise RuntimeError("Checkpoint download failed after three attempts; partial files retained.")
                time.sleep(15)
        local_vllm.validate_checkpoint(model_dir, settings)
        status("verifying_weights", weights_downloaded=True)
        source = ROOT / "sources/local_model" / settings["revision"] / "weights_manifest.json"
        manifest = json.loads(source.read_text())
        assert (manifest["model"], manifest["revision"]) == (settings["model"], settings["revision"])
        verification_path = ROOT / "reports/local_model_weight_verification.json"
        cached = json.loads(verification_path.read_text()) if verification_path.exists() else {}
        cached_files = {f["file"]: f for f in cached.get("files", [])}
        verified_at = verification_path.stat().st_mtime_ns if verification_path.exists() else 0
        reuse = (cached.get("all_matched") is True
                 and (cached.get("model"), cached.get("revision")) == (settings["model"], settings["revision"])
                 and len(cached_files) == len(manifest["files"]))
        for expected in manifest["files"]:
            stat = (model_dir / expected["name"]).stat()
            record = cached_files.get(expected["name"], {})
            reuse = reuse and (record.get("matched") is True
                              and record.get("sha256") == expected["sha256"]
                              and stat.st_size == expected["bytes"]
                              and stat.st_mtime_ns <= verified_at and stat.st_ctime_ns <= verified_at)
        checks = cached["files"] if reuse else []
        for expected in ([] if reuse else manifest["files"]):
            path = model_dir / expected["name"]
            digest = hashlib.sha256()
            with path.open("rb") as stream:
                for chunk in iter(lambda: stream.read(8 * 1024**2), b""):
                    digest.update(chunk)
            matched = path.stat().st_size == expected["bytes"] and digest.hexdigest() == expected["sha256"]
            checks.append({"file": path.name, "sha256": digest.hexdigest(), "matched": matched})
            if not matched:
                raise RuntimeError("A weight shard does not match the pinned official digest.")
        if not reuse:
            write_json(verification_path,
                       {"model": settings["model"], "revision": settings["revision"], "all_matched": True,
                        "weight_bytes": settings["weights_bytes"], "files": checks})
        status("weights_verified", weight_verification_reused=bool(reuse), weight_sha256_verified=True)
        probe = socket.socket()
        try:
            probe.bind(("127.0.0.1", settings["port"]))
        finally:
            probe.close()
        status("starting_server", weight_sha256_verified=True)
        env.update(HF_HUB_OFFLINE="1", TRANSFORMERS_OFFLINE="1")
        with (ROOT / "logs/local_model/qwen38_27b_server.log").open("a") as log:
            server = subprocess.Popen([sys.executable, "scripts/local_vllm.py", "serve"], cwd=ROOT,
                                      env=env, stdout=log, stderr=subprocess.STDOUT, start_new_session=True)
        identity = {"pid": server.pid, "proc_start_ticks": process_start(server.pid),
                    "model": settings["model"], "revision": settings["revision"],
                    "gpu_ids": settings["gpu_ids"], "server_log": "logs/local_model/qwen38_27b_server.log"}
        write_json(ROOT / ".local/local_model_server.json", identity)
        status("waiting_for_server", server_pid=server.pid)
        client = urllib.request.build_opener(urllib.request.ProxyHandler({}))
        deadline = time.monotonic() + 1800
        while time.monotonic() < deadline:
            if server.poll() is not None:
                raise RuntimeError(f"Local server exited during startup with code {server.returncode}.")
            try:
                with client.open(f'http://127.0.0.1:{settings["port"]}/v1/models', timeout=2) as response:
                    models = json.load(response)
                if settings["model"] in {m["id"] for m in models.get("data", [])}:
                    break
            except (OSError, ValueError):
                pass
            time.sleep(5)
        else:
            raise RuntimeError("Local server did not become ready within 30 minutes.")
        status("synthetic_checks", model_server_started=True)
        with (ROOT / "logs/local_model/qwen38_27b_smoke.log").open("a") as log:
            subprocess.run([sys.executable, "scripts/local_vllm.py", "smoke"],
                           cwd=ROOT, env=env, stdout=log, stderr=subprocess.STDOUT, check=True)
            subprocess.run([sys.executable, "scripts/local_model_capability_smoke.py"],
                           cwd=ROOT, env=env, stdout=log, stderr=subprocess.STDOUT, check=True)
        if server.poll() is not None:
            raise RuntimeError("Local server exited after the synthetic checks.")
        review_path = ROOT / "reports/local_model_checkpoint_review.json"
        review = json.loads(review_path.read_text())
        review.update(weights_downloaded=True, download_status="complete", weight_sha256_verified=True,
                      model_server_started=True, synthetic_checks_passed=True)
        write_json(review_path, review)
        status("ready", synthetic_checks_passed=True, endpoint=f'http://127.0.0.1:{settings["port"]}/v1',
               context_limit=settings["max_model_len"], gpu_memory_utilization=settings["gpu_memory_utilization"])
    except BaseException as error:
        if (isinstance(error, subprocess.CalledProcessError)
                and state.get("model_server_started") and server is not None and server.poll() is None):
            status("synthetic_checks_failed", error_type=type(error).__name__,
                   diagnostic="Local server remains available for diagnosis; see smoke log. No benchmark requests submitted.")
            raise
        if server is not None and server.poll() is None:
            os.killpg(server.pid, signal.SIGTERM)
            try:
                server.wait(timeout=15)
            except subprocess.TimeoutExpired:
                os.killpg(server.pid, signal.SIGKILL)
                server.wait()
        status("failed", model_server_started=False, error_type=type(error).__name__,
               diagnostic="See local download/server/smoke logs; no benchmark requests were submitted.")
        raise


if __name__ == "__main__":
    main()
