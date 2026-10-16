"""Replay the archived reviewed LitQA2 run without changing its frozen artifacts."""
from __future__ import annotations

import argparse
from collections import Counter
from datetime import datetime, timezone
import fcntl
import hashlib
import importlib
import json
import os
from pathlib import Path
import shutil
import socket
import subprocess
import sys
import time
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
STATE = ROOT / ".local/litqa2_replay"
OLD_RUN = "qwen38_27b_litqa2_public_reviewed_2026-10-15"
MODEL_DIR = Path("/dfs/scratch0/tchen/models/Qwen3.8-27B")


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def write(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(value, indent=2) + "\n")
    temporary.chmod(0o600)
    temporary.replace(path)


def prepare(run_id):
    if not run_id or Path(run_id).name != run_id or run_id in {".", "..", OLD_RUN}:
        raise ValueError("Replay requires a distinct, simple run ID")
    baseline = STATE / "baseline/results/runs" / OLD_RUN
    source = baseline / "frozen_files"
    original = json.loads((source / "configs/local_labbench_litqa2.json").read_text())
    for name, expected in original["frozen_files_sha256"].items():
        if sha(source / name) != expected:
            raise ValueError("Archived frozen file mismatch: " + name)
    references = source / "data/labbench/scorer_references.jsonl"
    if sha(references) != original["scorer_reference_sha256"]:
        raise ValueError("Archived reference file mismatch")
    runtime = STATE / "runtimes" / run_id
    if runtime.exists() or (ROOT / "results/runs" / run_id).exists():
        raise ValueError("Replay destination already exists; use a distinct run ID")
    shutil.copytree(source, runtime)
    (ROOT / "results/runs").mkdir(parents=True, exist_ok=True)
    (runtime / "results").mkdir()
    (runtime / "results/runs").symlink_to(ROOT / "results/runs", target_is_directory=True)
    settings = dict(original, run_id=run_id, gpu_ids=[0])
    settings["replay_provenance"] = {
        "archived_run": OLD_RUN, "archived_directory": str(baseline),
        "original_config_sha256": sha(source / "configs/local_labbench_litqa2.json"),
        "original_requests_unchanged": True,
        "serving_difference": "New Slurm GPU allocation; runtime context cap 16384 instead of 262144; same complete prompts and generation parameters.",
    }
    config = runtime / "configs/litqa2_replay.json"
    write(config, settings)
    write(runtime / "configs/local_model.json", {
        "model": original["model"], "revision": original["model_revision"],
        "benchmark_inference_authorized": True, "approved_task_ids": ["B01"],
        "max_num_seqs": 4, "model_directory": str(MODEL_DIR),
        "scope": "Explicit user request to replay the previously reviewed 197-case LitQA2 run.",
    })
    # Import only the archived input-only runner for preflight. Reference labels
    # and prior answers are not read while preparing the requests.
    sys.path.insert(0, str(runtime / "scripts"))
    runner = importlib.import_module("run_local_labbench")
    runner.ROOT = runtime
    settings, cases = runner.read_frozen_config(config)
    request_files = sorted((baseline / "requests").glob("*.json"))
    if len(cases) != 197 or len(request_files) != 197:
        raise ValueError("Expected exactly the archived 197 reviewed cases")
    for case in cases:
        identity = runner.digest([case["task"], case["variant"], case["case_id"]])
        old_request = json.loads((baseline / "requests" / (identity + ".json")).read_text())
        payload = runner.payload_for(case, settings)
        if payload != old_request["payload"] or runner.digest(payload) != old_request["request_sha256"]:
            raise ValueError("Replay request differs from archived request")
    plan = {
        "run_id": run_id, "runtime": str(runtime), "config": str(config),
        "baseline": str(baseline), "model_directory": str(MODEL_DIR),
        "model": settings["model"], "model_revision": settings["model_revision"],
        "planned": len(cases), "all_request_payloads_match_archive": True,
        "generation": settings["generation"], "max_model_len": 16384,
        "created_at_utc": datetime.now(timezone.utc).isoformat(),
    }
    write(STATE / "plan.json", plan)
    print(json.dumps(plan))


def compare(plan):
    folder = ROOT / "results/runs" / plan["run_id"]
    baseline = Path(plan["baseline"])
    old_score = json.loads((baseline / "scores.json").read_text())
    new_score = json.loads((folder / "scores.json").read_text())
    old_cases = {r["case_id"]: r for r in json.loads((baseline / "per_case_scores.json").read_text())}
    new_cases = {r["case_id"]: r for r in json.loads((folder / "per_case_scores.json").read_text())}
    if set(old_cases) != set(new_cases):
        raise ValueError("Replay case set differs from the archived run")
    transitions = Counter()
    for case_id in old_cases.keys() & new_cases.keys():
        transitions[(bool(old_cases[case_id]["correct"]), bool(new_cases[case_id]["correct"]))] += 1
    result = {
        "baseline_run": OLD_RUN, "replay_run": plan["run_id"],
        "same_request_payloads": plan["all_request_payloads_match_archive"],
        "baseline_metrics": old_score["metrics"], "replay_metrics": new_score["metrics"],
        "baseline_cases": len(old_cases), "replay_cases": len(new_cases),
        "identical_case_set": set(old_cases) == set(new_cases),
        "same_parsed_answer": sum(old_cases[k]["answer"] == new_cases[k]["answer"] for k in old_cases.keys() & new_cases.keys()),
        "correctness_transitions": {str(k): v for k, v in transitions.items()},
        "qualification": "Same frozen requests and seed; hardware/runtime differences can change sampled outputs. This compares answer outcomes, not explanation validity.",
    }
    write(folder / "comparison.json", result)
    print(json.dumps(result))


def run():
    lock = (STATE / "run.lock").open("a")
    fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
    plan = json.loads((STATE / "plan.json").read_text())
    audit = json.loads((STATE / "checkpoint_verification.json").read_text())
    # The verifier's explicit terminal success is required, not just matching
    # filenames or a model advertised by a server.
    if not (audit.get("all_weight_hashes_match") or audit.get("all_weights_match") or audit.get("all_matched")):
        raise ValueError("Full checkpoint hash verification has not passed")
    if (Path(audit["checkpoint_directory"]).resolve() != MODEL_DIR.resolve()
            or audit["recorded_model"] != plan["model"] or audit["recorded_revision"] != plan["model_revision"]):
        raise ValueError("Checkpoint audit belongs to a different model")
    for record in audit["files"]:
        if record.get("optional_for_inference"):
            continue
        stat = (MODEL_DIR / record["file"]).stat()
        if record.get("state") != "verified" or (stat.st_size, stat.st_mtime_ns) != (record["bytes"], record["mtime_ns"]):
            raise ValueError("Checkpoint changed after verification: " + record["file"])
    publisher = json.loads((STATE / "publisher_verification.json").read_text())
    if (publisher.get("status") != "verified" or publisher.get("matched_weight_files") != 18
            or publisher.get("publisher_revision") != plan["model_revision"]):
        raise ValueError("Pinned publisher weight digests have not been independently confirmed")
    runtime = Path(plan["runtime"])
    folder = ROOT / "results/runs" / plan["run_id"]
    folder.mkdir(parents=True, exist_ok=True)
    environment = dict(os.environ)
    for key in ("OPENAI_API_KEY", "ANTHROPIC_API_KEY", "HF_TOKEN", "HUGGING_FACE_HUB_TOKEN"):
        environment.pop(key, None)
    for key in ("PYTHONHOME", "VIRTUAL_ENV"):
        environment.pop(key, None)
    cache = Path(os.environ.get("BIO_REPLAY_CACHE", str(ROOT / ".cache/litqa2_replay")))
    cache.mkdir(parents=True, exist_ok=True)
    environment.update({"HF_HUB_OFFLINE": "1", "TRANSFORMERS_OFFLINE": "1", "HF_HOME": str(cache / "hf"),
                        "XDG_CACHE_HOME": str(cache), "TRITON_CACHE_DIR": str(cache / "triton"),
                        "VLLM_CACHE_ROOT": str(cache / "vllm"), "CUDA_CACHE_PATH": str(cache / "cuda"),
                        "FLASHINFER_WORKSPACE_BASE": str(cache / "flashinfer"),
                        "VLLM_NO_USAGE_STATS": "1", "DO_NOT_TRACK": "1", "MAX_JOBS": "4", "PYTHONNOUSERSITE": "1"})
    python = Path(os.environ.get("BIO_REPLAY_PYTHON", str(ROOT / ".venv-vllm/bin/python")))
    prefix = python.parent.parent
    binaries = [str(path) for path in prefix.glob("lib/python*/site-packages/ninja/data/bin")]
    binaries.append(str(python.parent))
    for pattern in ("lib/python*/site-packages/nvidia/cuda_nvcc/bin", "lib/python*/site-packages/nvidia/cu13/bin"):
        binaries.extend(str(path) for path in prefix.glob(pattern))
    for toolkit in prefix.glob("lib/python*/site-packages/nvidia/cu13"):
        if (toolkit / "bin/nvcc").is_file() and (toolkit / "include/cuda.h").is_file():
            # NVIDIA's wheels use lib/ and a versioned runtime soname; the
            # extension builder expects the conventional CUDA toolkit layout.
            if (toolkit / "lib").is_dir() and not (toolkit / "lib64").exists():
                (toolkit / "lib64").symlink_to("lib", target_is_directory=True)
            if (toolkit / "lib/libcudart.so.13").is_file() and not (toolkit / "lib/libcudart.so").exists():
                (toolkit / "lib/libcudart.so").symlink_to("libcudart.so.13")
            environment["CUDA_HOME"] = str(toolkit)
            environment["LD_LIBRARY_PATH"] = os.pathsep.join(
                [str(toolkit / "lib"), environment.get("LD_LIBRARY_PATH", "")]).rstrip(os.pathsep)
    if Path("/usr/local/cuda/bin/nvcc").is_file():
        binaries.append("/usr/local/cuda/bin")
    environment["PATH"] = os.pathsep.join(binaries + [environment.get("PATH", "")])
    gpu = subprocess.check_output(["nvidia-smi", "--query-gpu=uuid,name,memory.total,driver_version", "--format=csv,noheader"], text=True)
    package_info = json.loads(subprocess.check_output([str(python), "-c",
        "import importlib.metadata as m,json,sys,torch; print(json.dumps({'python':sys.version,'torch_build':torch.__version__,'torch_cuda':torch.version.cuda,'packages':{n:m.version(n) for n in ['vllm','torch','transformers','triton','flashinfer-python']}}))"],
        env=environment, text=True))
    write(folder / "execution_environment.json", {"hostname": socket.gethostname(),
          "slurm_job_id": os.environ.get("SLURM_JOB_ID"), "cuda_visible_devices": os.environ.get("CUDA_VISIBLE_DEVICES"),
          "gpu_inventory": gpu, "checkpoint_audit_sha256": sha(STATE / "checkpoint_verification.json"),
          "publisher_audit_sha256": sha(STATE / "publisher_verification.json"),
          "model_directory": str(MODEL_DIR), "max_model_len": plan["max_model_len"], **package_info})
    # Exercise the actual GPU sampler with artificial probabilities before
    # spending time loading weights or dispatching any benchmark request.
    sampling_check = (
        "import json,torch,flashinfer; "
        "p=torch.zeros((4,128),device='cuda',dtype=torch.float32); p[:,42]=1; "
        "s=flashinfer.top_k_top_p_sampling_from_probs(p,top_k=20,top_p=0.95,seed=42); "
        "torch.cuda.synchronize(); assert s.tolist()==[42]*4; "
        "print(json.dumps({'passed':True,'sampled_indices':s.tolist(),'device':torch.cuda.get_device_name(0)}))"
    )
    with (folder / "sampling_check.log").open("w") as log:
        sampling = subprocess.run([str(python), "-c", sampling_check], env=environment,
                                  stdout=log, stderr=subprocess.STDOUT, timeout=300)
    if sampling.returncode:
        raise RuntimeError("Synthetic GPU sampler check failed; inspect sampling_check.log")
    # Ensure the shorter serving cap cannot remove any part of a benchmark prompt.
    token_check = (
        "import json; from transformers import AutoTokenizer; "
        f"t=AutoTokenizer.from_pretrained({str(MODEL_DIR)!r},local_files_only=True); "
        f"rows=[json.loads(s) for s in open({str(runtime / 'data/local_labbench_litqa2/model_inputs.jsonl')!r})]; "
        "longest=max(len(t.encode(t.apply_chat_template(r['messages'],tokenize=False,add_generation_prompt=True,enable_thinking=True,reasoning_effort='medium'),add_special_tokens=False)) for r in rows); "
        f"assert longest+4096<={plan['max_model_len']}; print(json.dumps({{'max_prompt_tokens':longest,'output_budget':4096}}))"
    )
    token_info = subprocess.check_output([str(python), "-c", token_check], env=environment, text=True)
    write(folder / "context_check.json", json.loads(token_info))
    command = [str(python), "-m", "vllm.entrypoints.cli.main", "serve", str(MODEL_DIR),
               "--served-model-name", plan["model"], "--host", "127.0.0.1", "--port", "8026",
               "--dtype", "bfloat16", "--tensor-parallel-size", "1", "--gpu-memory-utilization", "0.90",
               "--max-model-len", str(plan["max_model_len"]), "--max-num-seqs", "4",
               "--reasoning-parser", "qwen3", "--enable-prefix-caching",
               "--limit-mm-per-prompt", '{"image":0,"video":0}']
    probe = socket.socket()
    try:
        probe.bind(("127.0.0.1", 8026))
    finally:
        probe.close()
    server = None
    outcome = {"stage": "starting", "generation_exit_code": None, "scoring_exit_code": None}
    write(folder / "replay_status.json", outcome)
    try:
        with (folder / "server.log").open("w") as log:
            server = subprocess.Popen(command, cwd=runtime, env=environment, stdout=log, stderr=subprocess.STDOUT, start_new_session=True)
        ticks = Path(f"/proc/{server.pid}/stat").read_text().split()[21]
        identity = {"pid": server.pid, "proc_start_ticks": ticks, "model": plan["model"],
                    "revision": plan["model_revision"], "command": command, "checkpoint": str(MODEL_DIR)}
        write(runtime / ".local/local_model_server.json", identity)
        write(folder / "server_identity.json", identity)
        opener = urllib.request.build_opener(urllib.request.ProxyHandler({}))
        deadline = time.monotonic() + 900
        while time.monotonic() < deadline:
            if server.poll() is not None:
                raise RuntimeError("vLLM exited during startup; inspect server.log")
            try:
                with opener.open("http://127.0.0.1:8026/v1/models", timeout=2) as response:
                    models = json.load(response)
                if any(m.get("id") == plan["model"] for m in models.get("data", [])):
                    break
            except (OSError, ValueError):
                pass
            time.sleep(2)
        else:
            raise TimeoutError("vLLM startup exceeded 15 minutes")
        descendants = {server.pid}
        parents = {}
        for process in Path("/proc").iterdir():
            if process.name.isdigit():
                try:
                    fields = (process / "stat").read_text().rsplit(")", 1)[1].split()
                    parents[int(process.name)] = int(fields[1])
                except (OSError, ValueError, IndexError):
                    pass
        for _ in range(len(parents)):
            additions = {pid for pid, parent in parents.items() if parent in descendants} - descendants
            if not additions:
                break
            descendants.update(additions)
        apps = subprocess.check_output(["nvidia-smi", "--query-compute-apps=pid,gpu_uuid,used_memory", "--format=csv,noheader"], text=True)
        own_gpu_processes = []
        for line in apps.splitlines():
            fields = [field.strip() for field in line.split(",")]
            if fields and fields[0].isdigit() and int(fields[0]) in descendants:
                own_gpu_processes.append({"pid": int(fields[0]), "gpu_uuid": fields[1], "used_memory": fields[2]})
        identity["observed_gpu_processes"] = own_gpu_processes
        identity["observed_gpu_count"] = len({row["gpu_uuid"] for row in own_gpu_processes})
        write(folder / "server_identity.json", identity)
        if identity["observed_gpu_count"] > 1:
            raise RuntimeError("Server used more than the allocated one GPU")
        synthetic = {"model": plan["model"], "messages": [{"role": "user", "content": "What is 2 + 2? Reply with only the digit."}],
                     "temperature": 0, "max_tokens": 32, "chat_template_kwargs": {"enable_thinking": False}}
        request = urllib.request.Request("http://127.0.0.1:8026/v1/chat/completions",
                                         data=json.dumps(synthetic).encode(), headers={"Content-Type": "application/json"})
        with opener.open(request, timeout=300) as response:
            synthetic_response = json.load(response)
        write(folder / "synthetic_check.json", {"request": synthetic, "response": synthetic_response})
        if synthetic_response.get("choices", [{}])[0].get("message", {}).get("content", "").strip() != "4":
            raise RuntimeError("Synthetic text serving check failed before benchmark dispatch")
        outcome["stage"] = "generating"
        write(folder / "replay_status.json", outcome)
        with (folder / "generation.log").open("w") as log:
            generation = subprocess.run([str(python), "-u", str(runtime / "scripts/run_local_labbench.py"),
                                         "--config", plan["config"]], cwd=runtime, env=environment, stdout=log, stderr=subprocess.STDOUT)
        outcome["generation_exit_code"] = generation.returncode
        outcome["stage"] = "scoring"
        write(folder / "replay_status.json", outcome)
        # Preserve the archived scorer; suppress only its legacy project-wide
        # report writes. All score files stay in this new run's directory.
        code = "import sys; sys.path.insert(0,sys.argv[1]); import score_local_labbench as s; s.update_interpretation=lambda *a:None; s.score(s.ROOT/'results/runs'/sys.argv[2])"
        with (folder / "scoring.log").open("w") as log:
            scoring = subprocess.run([str(python), "-c", code, str(runtime / "scripts"), plan["run_id"]],
                                     cwd=runtime, env=environment, stdout=log, stderr=subprocess.STDOUT)
        outcome["scoring_exit_code"] = scoring.returncode
        if generation.returncode == 0 and scoring.returncode == 0:
            compare(plan)
            outcome["stage"] = "completed"
        else:
            outcome["stage"] = "failed_or_incomplete"
    except Exception as error:
        outcome.update(stage="failed", error=f"{type(error).__name__}: {error}")
        raise
    finally:
        outcome["finished_at_utc"] = datetime.now(timezone.utc).isoformat()
        write(folder / "replay_status.json", outcome)
        completion = {key: outcome[key] for key in ("generation_exit_code", "scoring_exit_code", "finished_at_utc")}
        for filename, field in (("scores.json", "scores_sha256"), ("run_manifest.json", "run_manifest_sha256")):
            if (folder / filename).is_file():
                completion[field] = sha(folder / filename)
        write(folder / "completion.json", completion)
        if server is not None and server.poll() is None:
            import signal
            os.killpg(server.pid, signal.SIGTERM)
            try:
                server.wait(timeout=30)
            except subprocess.TimeoutExpired:
                os.killpg(server.pid, signal.SIGKILL)
    if outcome["stage"] != "completed":
        raise SystemExit(1)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="action", required=True)
    preparation = subparsers.add_parser("prepare")
    preparation.add_argument("--run-id", required=True)
    subparsers.add_parser("run")
    args = parser.parse_args()
    if args.action == "prepare":
        prepare(args.run_id)
    else:
        run()
