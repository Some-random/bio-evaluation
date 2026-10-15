"""Run a frozen, explicitly reviewed LAB-Bench subset on loopback vLLM.

This process reads model inputs and execution metadata only, never answer keys.
Each case has one generation; errors and truncated completions are retained.
"""
import argparse
import concurrent.futures as cf
from collections import Counter
import datetime as dt
import fcntl
import hashlib
import json
from pathlib import Path
import threading
import time
import urllib.error
import urllib.parse
import urllib.request

ROOT = Path(__file__).resolve().parents[1]


def digest(value):
    return hashlib.sha256(json.dumps(value, ensure_ascii=False, sort_keys=True,
                                    separators=(",", ":")).encode()).hexdigest()


def file_digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write_json(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n")
    tmp.chmod(0o600)
    tmp.replace(path)


def validate_endpoint(endpoint):
    url = urllib.parse.urlsplit(endpoint)
    if (url.scheme != "http" or url.hostname != "127.0.0.1" or url.port != 8026
            or url.path != "/v1" or url.username or url.password or url.query or url.fragment):
        raise ValueError("Only the configured loopback vLLM endpoint is permitted")


def payload_for(case, settings):
    generation_fields = {"max_tokens", "temperature", "top_p", "top_k", "seed", "n", "chat_template_kwargs"}
    if set(settings["generation"]) != generation_fields or settings["generation"]["n"] != 1:
        raise ValueError("Generation settings differ from the one-completion tool-free contract")
    if set(case) != {"task", "case_id", "variant", "split", "messages"}:
        raise ValueError("Unexpected input fields; labels/metadata cannot be dispatched")
    if case["task"] not in settings["approved_task_ids"]:
        raise ValueError("Task is outside the reviewed allowlist")
    if case["variant"] != settings["variant"] or len(case["messages"]) != 1:
        raise ValueError("Unexpected protocol or conversation")
    message = case["messages"][0]
    if set(message) != {"role", "content"} or message["role"] != "user" or not isinstance(message["content"], str):
        raise ValueError("This reviewed protocol supplies exactly one original text prompt")
    return {"model": settings["model"], "messages": case["messages"],
            **settings["generation"]}


def validate_cases(cases, settings, review):
    identities = [c["case_id"] for c in cases]
    if len(set(identities)) != len(identities) or identities != review["approved_case_ids"]:
        raise ValueError("Cases differ from the frozen, ordered review allowlist")
    if set(identities) & {c["case_id"] for c in review["held_cases"]}:
        raise ValueError("A held case reached the execution set")
    for case in cases:
        payload_for(case, settings)


def read_frozen_config(config_path):
    settings = json.loads(config_path.read_text())
    validate_endpoint(settings["endpoint"])
    local = json.loads((ROOT / "configs/local_model.json").read_text())
    if (not local.get("benchmark_inference_authorized") or settings["model"] != local["model"]
            or settings["model_revision"] != local["revision"]
            or not set(settings["approved_task_ids"]) <= set(local["approved_task_ids"])):
        raise ValueError("Local model execution scope does not authorize this run")
    if not 1 <= settings["concurrency"] <= min(4, local["max_num_seqs"]):
        raise ValueError("Concurrency exceeds the frozen serving budget")
    for name, expected in settings["frozen_files_sha256"].items():
        if file_digest(ROOT / name) != expected:
            raise ValueError("Frozen file changed: " + name)
    cases = [json.loads(s) for s in (ROOT / settings["input_file"]).read_text().splitlines() if s]
    review = json.loads((ROOT / settings["review_file"]).read_text())
    validate_cases(cases, settings, review)
    return settings, cases


def call(endpoint, payload=None, timeout=900):
    # Ignore proxy and credential environment variables. No provider SDK is used.
    opener = urllib.request.build_opener(urllib.request.ProxyHandler({}))
    data = json.dumps(payload, ensure_ascii=False).encode() if payload is not None else None
    request = urllib.request.Request(endpoint, data=data,
                                     headers={"Content-Type": "application/json"})
    try:
        with opener.open(request, timeout=timeout) as response:
            raw = response.read()
            return response.status, json.loads(raw) if raw else {}
    except urllib.error.HTTPError as error:
        return error.code, {"error": {"type": "HTTPError"}}
    except (urllib.error.URLError, TimeoutError, OSError, ValueError) as error:
        return 0, {"error": {"type": type(error).__name__}}


def run(config_path):
    settings, cases = read_frozen_config(config_path)
    folder = ROOT / "results/runs" / settings["run_id"]
    folder.mkdir(parents=True, exist_ok=True)
    lock = (folder / "worker.lock").open("a")
    fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
    manifest = {"configuration": settings, "configuration_sha256": file_digest(config_path),
                "runner_sha256": file_digest(Path(__file__)), "case_contract_sha256": digest(cases),
                "planned_cases": len(cases), "model_selection_on_test": False,
                "solver_tools": [], "answer_keys_available_to_solver": False}
    manifest_path = folder / "run_manifest.json"
    if manifest_path.exists() and json.loads(manifest_path.read_text()) != manifest:
        raise ValueError("Run manifest changed; existing results cannot be reused")
    write_json(manifest_path, manifest)
    server = json.loads((ROOT / ".local/local_model_server.json").read_text())
    ticks = Path(f"/proc/{server['pid']}/stat").read_text().split()[21]
    if ticks != server["proc_start_ticks"] or server["model"] != settings["model"] or server["revision"] != settings["model_revision"]:
        raise ValueError("Server process identity differs from the pinned model")
    status, models = call(settings["endpoint"] + "/models", timeout=15)
    if status != 200 or not any(m["id"] == settings["model"] for m in models.get("data", [])):
        raise ValueError("Pinned model is not available from the local server")
    write_json(folder / "worker_process.json", {"pid": __import__("os").getpid(),
               "started_at_utc": dt.datetime.now(dt.timezone.utc).isoformat(), "server": server})
    stopped = threading.Event()
    started = time.monotonic()
    statuses = Counter()

    def execute(case):
        identity = digest([case["task"], case["variant"], case["case_id"]])
        output = folder / "responses" / (identity + ".json")
        if output.exists():
            return json.loads(output.read_text())["status"]
        if stopped.is_set():
            return "not_dispatched_after_error"
        payload = payload_for(case, settings)
        request_hash = digest(payload)
        request_path = folder / "requests" / (identity + ".json")
        if request_path.exists():
            # An interrupted call might have executed. Never silently resample it.
            return "interrupted_unknown_completion"
        metadata = {k: case[k] for k in ["task", "case_id", "variant", "split"]}
        write_json(request_path, {**metadata, "request_sha256": request_hash, "payload": payload,
                                 "supplied_fields": ["question", "shuffled_choices", "native_COT_instructions"]})
        before = time.monotonic()
        code, response = call(settings["endpoint"] + "/chat/completions", payload)
        record = {**metadata, "model": settings["model"], "model_revision": settings["model_revision"],
                  "request_sha256": request_hash, "http_status": code, "response": response,
                  "elapsed_seconds": round(time.monotonic() - before, 3),
                  "saved_at_utc": dt.datetime.now(dt.timezone.utc).isoformat()}
        if code == 200 and response.get("model") == settings["model"] and len(response.get("choices", [])) == 1:
            choice = response["choices"][0]
            record.update(status="completed", text=choice["message"].get("content") or "",
                          finish_reason=choice.get("finish_reason"))
        else:
            record["status"] = "transport_error" if code == 0 else "server_error"
            stopped.set()
        write_json(output, record)
        return record["status"]

    def progress(stage):
        value = {"run": settings["run_id"], "stage": stage, "planned": len(cases),
                 "finished": sum(statuses.values()), "statuses": dict(statuses),
                 "requests_saved": len(list((folder / "requests").glob("*.json"))),
                 "elapsed_seconds": round(time.monotonic() - started, 2),
                 "updated_at_utc": dt.datetime.now(dt.timezone.utc).isoformat()}
        write_json(folder / "progress.json", value)
        print(json.dumps(value), flush=True)

    progress("running")
    with cf.ThreadPoolExecutor(max_workers=settings["concurrency"]) as pool:
        futures = [pool.submit(execute, case) for case in cases]
        for future in cf.as_completed(futures):
            try:
                statuses[future.result()] += 1
            except Exception:
                stopped.set()
                statuses["worker_exception"] += 1
            progress("running")
    progress("generation_complete" if statuses["completed"] == len(cases) else "incomplete")
    return 0 if statuses["completed"] == len(cases) else 1


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", type=Path, required=True)
    args = parser.parse_args()
    raise SystemExit(run(args.config))
