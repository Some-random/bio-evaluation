"""Finish the last pinned checkpoint shard with resumable HTTP; resume setup after verification."""
from datetime import datetime, timedelta, timezone
import hashlib
import json
import os
from pathlib import Path
import shutil
import signal
import subprocess

import local_vllm


ROOT = local_vllm.ROOT


def write_json(path, value):
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(value, indent=2) + "\n")
    temporary.replace(path)


def main():
    settings = local_vllm.config()
    assert settings["model"] == "Qwen/Qwen3.8-27B"
    model = Path(settings["model_directory"])
    source = ROOT / "sources/local_model" / settings["revision"]
    expected = next(f for f in json.loads((source / "weights_manifest.json").read_text())["files"]
                    if f["name"] == "model-00018-of-00018.safetensors")
    replica = next(f for f in json.loads((source / "modelscope_files.json").read_text())["Data"]["Files"]
                   if f.get("Name") == expected["name"])
    assert (replica["Size"], replica["Sha256"]) == (expected["bytes"], expected["sha256"])
    cache = ROOT / ".cache/final_shard_transfer"
    cache.mkdir(exist_ok=True)
    destination = cache / expected["name"]
    # Xet writes a contiguous reconstructed prefix. Resume that owned prefix;
    # the complete official SHA-256 is mandatory before installing the result.
    if not destination.exists():
        partials = [f for f in (model / ".cache/huggingface/download").glob("*.incomplete")
                    if f".{expected['sha256']}." in f.name]
        if partials:
            prefix = max(partials, key=lambda f: f.stat().st_size)
            with prefix.open("rb") as stream:
                first_hole = os.lseek(stream.fileno(), 0, os.SEEK_HOLE)
            if first_hole >= prefix.stat().st_size:
                shutil.copyfile(prefix, destination)
                print(json.dumps({"resumed_prefix_bytes": destination.stat().st_size}), flush=True)
    urls = [f"https://modelscope.cn/api/v1/models/{settings['model']}/repo?Revision={replica['Revision']}&FilePath={expected['name']}"]
    input_file = cache / "sources.txt"
    input_file.write_text("\t".join(urls) + "\n"
                          + " dir=" + str(cache) + "\n"
                          + " out=" + expected["name"] + "\n"
                          + " checksum=sha-256=" + expected["sha256"] + "\n")
    input_file.chmod(0o600)
    env = local_vllm.environment(settings)
    for key in ("HTTP_PROXY", "HTTPS_PROXY", "ALL_PROXY", "http_proxy", "https_proxy", "all_proxy"):
        env.pop(key, None)
    command = ["aria2c", "--all-proxy=", "--async-dns=false",
               "--check-certificate=true", "--continue=true", "--check-integrity=true",
               "--checksum=sha-256=" + expected["sha256"], "--file-allocation=none",
               "--max-concurrent-downloads=1", "--split=16", "--max-connection-per-server=8",
               "--min-split-size=8M", "--max-tries=20", "--retry-wait=3",
               "--connect-timeout=15", "--timeout=30", "--lowest-speed-limit=128K",
               "--allow-overwrite=true", "--auto-file-renaming=false", "--summary-interval=10",
               "--dir=" + str(cache), "--out=" + expected["name"], "--input-file=" + str(input_file)]
    with (ROOT / "logs/local_model/qwen38_27b_final_aria2.log").open("a") as log:
        transfer = subprocess.Popen(command, cwd=ROOT, env=env, stdout=log, stderr=subprocess.STDOUT)
        write_json(ROOT / ".local/local_model_final_transfer.json",
                   {"finisher_pid": os.getpid(), "transfer_pid": transfer.pid,
                    "model": settings["model"], "revision": settings["revision"],
                    "expected_bytes": expected["bytes"], "expected_sha256": expected["sha256"],
                    "started_at_PST": datetime.now(timezone(timedelta(hours=-8))).isoformat(),
                    "sources": urls, "maximum_connections": 16,
                    "network_route": "direct HTTPS to publisher ModelScope China CDN; no proxy"})
        code = transfer.wait()
    if code != 0:
        raise RuntimeError(f"Resumable transfer exited with code {code}; partial data/control file retained.")
    digest = hashlib.sha256()
    with destination.open("rb") as stream:
        for chunk in iter(lambda: stream.read(8 * 1024**2), b""):
            digest.update(chunk)
    if destination.stat().st_size != expected["bytes"] or digest.hexdigest() != expected["sha256"]:
        raise RuntimeError("Final shard differs from the pinned official SHA-256 or size.")
    destination.replace(model / expected["name"])
    write_json(ROOT / "reports/local_model_last_shard_verification.json",
               {"file": expected["name"], "bytes": expected["bytes"], "sha256": digest.hexdigest(),
                "matched": True, "permitted_replica_sources": urls,
                "source_note": "Publisher repositories have identical SHA-256; exact pinned weights retained."})
    local_vllm.finalize_checkpoint(model, settings)
    control = json.loads((ROOT / ".local/local_model_manual_transfer_control.json").read_text())
    pid = control["setup_pid"]
    proc = Path("/proc") / str(pid)
    if proc.exists() and proc.joinpath("stat").read_text().rsplit(")", 1)[1].split()[19] == control["setup_proc_start_ticks"]:
        os.kill(pid, signal.SIGCONT)
        control["setup_resumed"] = True
        write_json(ROOT / ".local/local_model_manual_transfer_control.json", control)
    else:
        raise RuntimeError("Checkpoint complete, but original setup worker identity changed; restart setup separately.")
    print(json.dumps({"all_18_weight_files_present": True, "final_shard_sha256_matched": True,
                      "setup_worker_resumed": True}), flush=True)


if __name__ == "__main__":
    main()
