"""Start identical TP1 replicas on previously authorized, currently idle GPUs.

The original GPU5 server and every unrelated GPU process are left untouched.
Only fixed synthetic checks are submitted by this setup worker.
"""
import datetime as dt
import fcntl
import json
import os
from pathlib import Path
import socket
import subprocess
import time
import urllib.request

import local_vllm
from run_local_labbench import write_json

ROOT = local_vllm.ROOT
PLAN = [(0, 8030), (1, 8031), (2, 8032), (3, 8033)]


def process_start(pid):
    try:
        text = Path(f"/proc/{pid}/stat").read_text()
        fields = text[text.rfind(")") + 2:].split()
        return None if fields[0] == "Z" else fields[19]
    except OSError:
        return None


def main():
    lock = (ROOT / ".local/local_model_remaining_replicas.lock").open("a")
    fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
    base = local_vllm.config()
    if base["gpu_ids"] != [5] or base["tensor_parallel_size"] != 1:
        raise ValueError("The original approved TP1 server changed")
    local_vllm.validate_checkpoint(Path(base["model_directory"]), base)
    client = urllib.request.build_opener(urllib.request.ProxyHandler({}))
    report = {"model": base["model"], "revision": base["revision"], "original_server_unchanged": True,
              "total_user_authorized_gpu_limit": 8, "planned_project_gpus": [0, 1, 2, 3, 4, 5, 6, 7],
              "source_weights_shared_read_only": True, "new_checkpoint_copies": 0, "replicas": {}}
    report_path = ROOT / "reports/local_model_remaining_replica_deployment.json"

    def status(gpu, **values):
        report["replicas"].setdefault(str(gpu), {}).update(values)
        report["updated_at_utc"] = dt.datetime.now(dt.timezone.utc).isoformat()
        write_json(report_path, report)
        print(json.dumps({"gpu": gpu, **values}), flush=True)

    for gpu, port in PLAN:
        identity_path = ROOT / f".local/local_model_server_gpu{gpu}.json"
        if identity_path.exists():
            identity = json.loads(identity_path.read_text())
            if process_start(identity["pid"]) == identity["proc_start_ticks"]:
                status(gpu, stage="existing_server_retained", port=port, pid=identity["pid"])
                continue
        raw = subprocess.check_output(["nvidia-smi", "--query-gpu=index,memory.used", "--format=csv,noheader,nounits"], text=True)
        used = {int(row.split(",")[0]): int(row.split(",")[1]) for row in raw.splitlines()}
        if used[gpu] > 512:
            status(gpu, stage="skipped_gpu_no_longer_idle", memory_used_mib=used[gpu])
            continue
        with socket.socket() as probe:
            probe.bind(("127.0.0.1", port))
        settings = dict(base, gpu_ids=[gpu], port=port, tensor_parallel_size=1,
                        user_authorized_gpu_limit=1,
                        serving_resource_note="One identical TP1 replica, within prior eight-GPU project allowance; only idle GPU selected; original server remains unchanged.")
        write_json(ROOT / f"configs/local_model_gpu{gpu}.json", settings)
        env = local_vllm.environment(settings)
        env.update(HF_HUB_OFFLINE="1", TRANSFORMERS_OFFLINE="1")
        log_path = ROOT / f"logs/local_model/qwen38_27b_server_gpu{gpu}.log"
        with log_path.open("a") as log:
            server = subprocess.Popen(local_vllm.serve_command(Path(settings["model_directory"]), settings),
                                      cwd=ROOT, env=env, stdin=subprocess.DEVNULL,
                                      stdout=log, stderr=subprocess.STDOUT, start_new_session=True)
        identity = {"pid": server.pid, "proc_start_ticks": process_start(server.pid),
                    "model": settings["model"], "revision": settings["revision"], "gpu_ids": [gpu],
                    "port": port, "server_log": str(log_path.relative_to(ROOT))}
        write_json(identity_path, identity)
        status(gpu, stage="starting", port=port, pid=server.pid)
        deadline = time.monotonic() + 1800
        while time.monotonic() < deadline:
            if server.poll() is not None:
                status(gpu, stage="startup_failed", exit_code=server.returncode)
                break
            try:
                with client.open(f"http://127.0.0.1:{port}/v1/models", timeout=2) as response:
                    models = json.load(response)
                if any(m["id"] == settings["model"] for m in models.get("data", [])):
                    payload = {"model": settings["model"], "messages": [{"role": "user", "content": "Reply exactly READY."}],
                               "max_tokens": 16, "temperature": 0, "chat_template_kwargs": {"enable_thinking": False}}
                    request = urllib.request.Request(f"http://127.0.0.1:{port}/v1/chat/completions",
                                                     json.dumps(payload).encode(), {"Content-Type": "application/json"})
                    with client.open(request, timeout=120) as response:
                        value = json.load(response)
                    text = value["choices"][0]["message"].get("content") or ""
                    if text.strip().rstrip(".") != "READY":
                        raise ValueError("Synthetic replica response differed from READY")
                    status(gpu, stage="ready", endpoint=f"http://127.0.0.1:{port}/v1",
                           synthetic_check="passed", benchmark_cases_dispatched=0)
                    break
            except (OSError, ValueError):
                pass
            time.sleep(5)
        else:
            status(gpu, stage="startup_timeout", pid=server.pid)


if __name__ == "__main__":
    main()
