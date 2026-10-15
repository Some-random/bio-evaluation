"""Prepare and serve the pinned local baseline; never dispatch benchmark cases."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import urllib.request

ROOT = Path(__file__).resolve().parents[1]


def config():
    return json.loads((ROOT / "configs/local_model.json").read_text())


def environment(settings):
    env = dict(os.environ)
    env.update({
        "CUDA_VISIBLE_DEVICES": ",".join(map(str, settings["gpu_ids"])),
        "HF_HOME": str(ROOT / ".cache/huggingface"),
        "HF_HUB_DISABLE_XET": "0" if settings.get("download_transport") == "hf_xet" else "1",
        "HF_XET_CHUNK_CACHE_SIZE_BYTES": "0",
        "HF_XET_NUM_CONCURRENT_RANGE_GETS": str(settings.get("download_range_concurrency", 8)),
        "UV_CACHE_DIR": str(ROOT / ".cache/uv"),
        "UV_PYTHON_INSTALL_DIR": str(ROOT / ".local/python"),
        "UV_SYSTEM_CERTS": "true",
        "TMPDIR": str(ROOT / ".cache/tmp"),
        "XDG_CACHE_HOME": str(ROOT / ".cache"),
        "TRITON_CACHE_DIR": str(ROOT / ".cache/triton"),
        "TORCHINDUCTOR_CACHE_DIR": str(ROOT / ".cache/torchinductor"),
        "TORCH_HOME": str(ROOT / ".cache/torch"),
        "FLASHINFER_WORKSPACE_BASE": str(ROOT),
        "CUDA_CACHE_PATH": str(ROOT / ".cache/cuda"),
        "MAX_JOBS": "8",
        "VLLM_CACHE_ROOT": str(ROOT / ".cache/vllm"),
        "VLLM_NO_USAGE_STATS": "1",
        "DO_NOT_TRACK": "1",
        "HF_HUB_DISABLE_TELEMETRY": "1",
    })
    binaries = [str(ROOT / ".venv-vllm/bin")]
    if Path("/usr/local/cuda/bin/nvcc").is_file():
        binaries.append("/usr/local/cuda/bin")
    env["PATH"] = os.pathsep.join(binaries + [env.get("PATH", "")])
    # This independent local setup has no reason to inherit provider credentials.
    for name in ("OPENAI_API_KEY", "ANTHROPIC_API_KEY", "HF_TOKEN", "HUGGING_FACE_HUB_TOKEN"):
        env.pop(name, None)
    return env


def directory_for(args, settings):
    value = args.model_dir or settings.get("model_directory")
    if not value:
        raise SystemExit("A model directory with sufficient space is required; storage selection is pending.")
    return Path(value).expanduser().resolve()


def validate_checkpoint(directory, settings):
    manifest = directory / "bio_evaluation_checkpoint.json"
    if not manifest.is_file():
        raise SystemExit("Checkpoint has not completed the pinned download and validation.")
    recorded = json.loads(manifest.read_text())
    if (recorded.get("model"), recorded.get("revision")) != (settings["model"], settings["revision"]):
        raise SystemExit("Checkpoint identity differs from the configured baseline.")
    weights = list(directory.glob("*.safetensors"))
    if len(weights) != settings["weight_files"] or sum(p.stat().st_size for p in weights) != settings["weights_bytes"]:
        raise SystemExit("Checkpoint shards are incomplete or their total size differs from the pinned source.")
    for name, expected in recorded.get("small_file_sha256", {}).items():
        path = directory / name
        if not path.is_file() or hashlib.sha256(path.read_bytes()).hexdigest() != expected:
            raise SystemExit("A checkpoint configuration/tokenizer file differs from its download manifest.")


def serve_command(directory, settings):
    gpu_ids = settings["gpu_ids"]
    if not gpu_ids or len(set(gpu_ids)) != len(gpu_ids) or len(gpu_ids) > settings["user_authorized_gpu_limit"]:
        raise SystemExit("Configured GPU list exceeds the user's resource scope or contains duplicates.")
    if settings["tensor_parallel_size"] != len(gpu_ids):
        raise SystemExit("Tensor parallel size must match the explicit GPU list.")
    if settings["host"] != "127.0.0.1" or settings.get("solver_tools"):
        raise SystemExit("This setup supports loopback serving without solver tools.")
    command = [
        str(ROOT / ".venv-vllm/bin/vllm"), "serve", str(directory),
        "--served-model-name", settings["model"],
        "--host", settings["host"], "--port", str(settings["port"]),
        "--tensor-parallel-size", str(settings["tensor_parallel_size"]),
        "--gpu-memory-utilization", str(settings["gpu_memory_utilization"]),
        "--max-model-len", str(settings["max_model_len"]),
        "--max-num-seqs", str(settings["max_num_seqs"]),
        "--reasoning-parser", "qwen3", "--enable-prefix-caching",
        "--mm-encoder-tp-mode", "data",
    ]
    if settings.get("enable_expert_parallel"):
        command.append("--enable-expert-parallel")
    for field, flag in (("moe_backend", "--moe-backend"), ("kv_cache_dtype", "--kv-cache-dtype"),
                        ("indexer_kv_dtype", "--attention-config.indexer_kv_dtype")):
        if settings.get(field):
            command.extend([flag, settings[field]])
    if "engram_cpu_offload" in settings:
        command.extend(["--engram-config", json.dumps({"cpu_offload": settings["engram_cpu_offload"]})])
    return command


def install(settings, env):
    uv = ROOT / ".local/tooling/bin/uv"
    if not uv.is_file():
        raise SystemExit("Install the pinned uv tool into .local/tooling before bootstrapping.")
    for folder in (ROOT / ".cache/tmp", ROOT / ".cache/uv"):
        folder.mkdir(parents=True, exist_ok=True)
    if not (ROOT / ".venv-vllm/bin/python").is_file():
        subprocess.run([str(uv), "venv", "--python", settings["python_version"], "--managed-python",
                        str(ROOT / ".venv-vllm")], env=env, check=True)
    subprocess.run([str(uv), "pip", "install", "--python", str(ROOT / ".venv-vllm/bin/python"),
                    "vllm==" + settings["vllm_version"], "httpx[socks]", "requests[socks]",
                    "--torch-backend=auto"], env=env, check=True)


def download(directory, settings, env):
    directory.mkdir(parents=True, exist_ok=True)
    if (directory / "bio_evaluation_checkpoint.json").is_file():
        validate_checkpoint(directory, settings)
        print(json.dumps({"checkpoint_downloaded": True, "already_present": True,
                          "directory": str(directory), "model": settings["model"]}))
        return
    present = sum(p.stat().st_size for p in directory.glob("*.safetensors"))
    reserve = max(10 * 1024 ** 3, settings["weights_bytes"] // 20)
    if shutil.disk_usage(directory).free < max(0, settings["weights_bytes"] - present) + reserve:
        raise SystemExit("Insufficient space for the checkpoint and a 5%/10-GiB reserve.")
    helper = """
import sys
from huggingface_hub import snapshot_download
snapshot_download(repo_id=sys.argv[1], revision=sys.argv[2], local_dir=sys.argv[3],
                  allow_patterns=['*.json', '*.jinja', '*.txt', '*.md', 'LICENSE', '*.safetensors'],
                  max_workers=int(sys.argv[4]), token=False)
"""
    subprocess.run([str(ROOT / ".venv-vllm/bin/python"), "-c", helper,
                    settings["model"], settings["revision"], str(directory),
                    str(settings.get("download_workers", 2))], env=env, check=True)
    finalize_checkpoint(directory, settings)


def finalize_checkpoint(directory, settings):
    """Record a complete checkpoint; full official weight hashes are checked by bootstrap."""
    weights = list(directory.glob("*.safetensors"))
    if len(weights) != settings["weight_files"] or sum(p.stat().st_size for p in weights) != settings["weights_bytes"]:
        raise SystemExit("The pinned checkpoint did not download completely.")
    metadata = {"model": settings["model"], "revision": settings["revision"],
                "weights_bytes": settings["weights_bytes"], "weight_files": len(weights),
                "precision": settings["checkpoint_precision"],
                "small_file_sha256": {p.name: hashlib.sha256(p.read_bytes()).hexdigest()
                    for p in directory.iterdir() if p.is_file() and p.suffix in {".json", ".jinja"}
                    and p.name != "bio_evaluation_checkpoint.json"}}
    (directory / "bio_evaluation_checkpoint.json").write_text(json.dumps(metadata, indent=2) + "\n")
    print(json.dumps({"checkpoint_downloaded": True, "directory": str(directory), "model": settings["model"]}))


def smoke(settings):
    # The client bypasses proxies and has no configurable external host or input.
    client = urllib.request.build_opener(urllib.request.ProxyHandler({}))
    base = "http://127.0.0.1:" + str(settings["port"])
    with client.open(base + "/v1/models", timeout=10) as response:
        models = json.load(response)
    if settings["model"] not in {m["id"] for m in models.get("data", [])}:
        raise SystemExit("Local server advertises a different model.")
    payload = {"model": settings["model"], "messages": [{"role": "user", "content": "Reply exactly READY."}],
               "max_tokens": 16, "temperature": 0,
               "chat_template_kwargs": {"enable_thinking": False}}
    request = urllib.request.Request(base + "/v1/chat/completions", json.dumps(payload).encode(),
                                     {"Content-Type": "application/json"})
    with client.open(request, timeout=180) as response:
        value = json.load(response)
    text = value["choices"][0]["message"].get("content")
    record = {"model": value.get("model"), "text": text, "usage": value.get("usage"),
              "finish_reason": value["choices"][0].get("finish_reason"),
              "test_type": "synthetic connectivity check; not a benchmark result"}
    (ROOT / "reports/local_model_smoke.json").write_text(json.dumps(record, indent=2) + "\n")
    print(json.dumps(record))
    if text is None or text.strip() != "READY":
        raise SystemExit("Synthetic local response did not match READY.")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("action", choices=["plan", "install", "download", "serve", "smoke"])
    parser.add_argument("--model-dir")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    if args.dry_run and args.action != "serve":
        parser.error("--dry-run is supported only for the serve command")
    settings = config()
    env = environment(settings)
    if args.action == "plan":
        print(json.dumps(settings, indent=2))
    elif args.action == "install":
        install(settings, env)
    elif args.action == "smoke":
        smoke(settings)
    else:
        directory = directory_for(args, settings)
        if args.action == "download":
            download(directory, settings, env)
        else:
            command = serve_command(directory, settings)
            if args.dry_run:
                print(json.dumps({"argv": command, "CUDA_VISIBLE_DEVICES": env["CUDA_VISIBLE_DEVICES"]}, indent=2))
                return
            validate_checkpoint(directory, settings)
            if not (ROOT / ".venv-vllm/bin/vllm").is_file():
                raise SystemExit("vLLM runtime installation has not completed.")
            os.execve(command[0], command, env)


if __name__ == "__main__":
    main()
