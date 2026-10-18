"""Run frozen reviewed native text/image LAB-Bench inputs on loopback vLLM.

This process reads model inputs and execution metadata only, never answer keys.
Each case has one generation; errors and truncated completions are retained.
"""
import argparse
import base64
import binascii
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


def validate_endpoint(endpoint, serving=None):
    url = urllib.parse.urlsplit(endpoint)
    allowed_ports = {8026, 8027, 8028, 8029, 8030, 8031, 8032, 8033}
    port = serving["port"] if serving is not None else 8026
    host = serving["host"] if serving is not None else "127.0.0.1"
    if (host != "127.0.0.1" or type(port) is not int or port not in allowed_ports
            or url.scheme != "http" or url.hostname != host or url.port != port
            or url.path != "/v1" or url.username or url.password or url.query or url.fragment):
        raise ValueError("Only the predeclared loopback vLLM serving endpoint is permitted")


def validate_serving_contract(settings, authority, serving):
    """The central authorization is authoritative; replicas cannot expand it."""
    if (not authority.get("benchmark_inference_authorized")
            or settings["model"] != authority["model"]
            or settings["model_revision"] != authority["revision"]
            or serving["model"] != authority["model"]
            or serving["revision"] != authority["revision"]
            or not set(settings["approved_task_ids"]) <= set(authority["approved_task_ids"])):
        raise ValueError("Local model execution scope does not authorize this run")
    validate_endpoint(settings["endpoint"], serving)
    gpu_ids = serving["gpu_ids"]
    if (not isinstance(gpu_ids, list) or len(gpu_ids) != 1
            or type(gpu_ids[0]) is not int or gpu_ids[0] != 0
            or not isinstance(settings.get("gpu_ids"), list) or len(settings["gpu_ids"]) != 1
            or type(settings["gpu_ids"][0]) is not int
            or settings.get("gpu_ids") != gpu_ids or serving["tensor_parallel_size"] != 1):
        raise ValueError("Run GPU IDs differ from the predeclared single-GPU replica")
    if serving["port"] not in {8026, 8027, 8028, 8029, 8030, 8031, 8032, 8033}:
        raise ValueError("Serving port is outside the frozen Slurm endpoint range")
    for field in ("model_directory", "checkpoint_precision"):
        if serving.get(field) != authority.get(field):
            raise ValueError("Serving replica differs from the pinned checkpoint: " + field)
    if not 1 <= settings["concurrency"] <= min(4, serving["max_num_seqs"]):
        raise ValueError("Concurrency exceeds the frozen serving budget")


def project_file(name, directory):
    if not isinstance(name, str):
        raise ValueError("Serving metadata paths must be project-local strings")
    path = ROOT / name
    if Path(name).is_absolute() or not path.resolve().is_relative_to((ROOT / directory).resolve()):
        raise ValueError("Serving metadata path is outside its allowed project directory")
    return path


def serving_context(settings):
    authority = json.loads((ROOT / "configs/local_model.json").read_text())
    serving_name = settings.get("serving_config_file", "configs/local_model.json")
    record_name = settings.get("server_record_file", ".local/local_model_server.json")
    serving = json.loads(project_file(serving_name, "configs").read_text())
    record_path = project_file(record_name, ".local")
    validate_serving_contract(settings, authority, serving)
    return serving, record_path


def validate_server_identity(server, settings, serving, actual_start_ticks):
    if (str(actual_start_ticks) != str(server["proc_start_ticks"])
            or server["model"] != settings["model"]
            or server["revision"] != settings["model_revision"]
            or server.get("gpu_ids") != settings["gpu_ids"]
            or server["gpu_ids"] != serving["gpu_ids"]):
        raise ValueError("Server process identity differs from the pinned model/GPUs")
    if "endpoint" in server and server["endpoint"] != settings["endpoint"]:
        raise ValueError("Server record endpoint differs from the frozen run")
    for field in ("host", "port"):
        if field in server and server[field] != serving[field]:
            raise ValueError("Server record differs from its serving configuration")


def server_start_ticks(pid):
    # The comm field may contain spaces; starttime is field22 after the final ') '.
    return Path(f"/proc/{pid}/stat").read_text().rsplit(") ", 1)[1].split()[19]


def validate_content(content):
    """Validate the native message without rewriting text or image data URLs."""
    if isinstance(content, str):
        return []
    if not isinstance(content, list) or not content:
        raise ValueError("Content must be original text or a nonempty native part list")
    images = []
    has_text = False
    for index, part in enumerate(content):
        if not isinstance(part, dict):
            raise ValueError("Every message part must be an allowlisted object")
        if part.get("type") == "text":
            if set(part) != {"type", "text"} or not isinstance(part["text"], str):
                raise ValueError("Unexpected text-part fields; annotations cannot be dispatched")
            has_text = True
        elif part.get("type") == "image_url":
            if set(part) != {"type", "image_url"} or not isinstance(part["image_url"], dict):
                raise ValueError("Unexpected image-part fields")
            spec = part["image_url"]
            if (set(spec) not in ({"url"}, {"url", "detail"})
                    or ("detail" in spec and spec["detail"] not in ("auto", "low", "high"))):
                raise ValueError("Unexpected image URL fields or detail level")
            url = spec["url"]
            if not isinstance(url, str):
                raise ValueError("Image URL must contain original inline image bytes")
            prefix, separator, encoded = url.partition(",")
            if not separator or prefix not in ("data:image/png;base64", "data:image/jpeg;base64"):
                raise ValueError("Only inline base64 PNG/JPEG images are permitted")
            try:
                raw = base64.b64decode(encoded, validate=True)
            except (binascii.Error, ValueError) as exc:
                raise ValueError("Image base64 is invalid") from exc
            mime = prefix[len("data:"):].split(";")[0]
            signature_matches = (raw.startswith(b"\x89PNG\r\n\x1a\n") if mime == "image/png"
                                 else raw.startswith(b"\xff\xd8\xff"))
            if not signature_matches:
                raise ValueError("Image bytes do not match the declared PNG/JPEG MIME type")
            images.append({"message_index": 0, "part_index": index, "mime_type": mime,
                           "bytes": len(raw), "sha256": hashlib.sha256(raw).hexdigest()})
        else:
            raise ValueError("Unsupported message part; tools and extra annotations are forbidden")
    if not has_text:
        raise ValueError("Native multimodal input must preserve its question text")
    return images


def supplied_fields_for(settings):
    fields = settings.get("model_facing_fields")
    if (not isinstance(fields, list) or not fields
            or any(not isinstance(field, str) or not field for field in fields)
            or len(fields) != len(set(fields))):
        raise ValueError("Frozen settings must declare unique model_facing_fields")
    return fields.copy()


def payload_for(case, settings):
    generation_fields = {"max_tokens", "temperature", "top_p", "top_k", "seed", "n", "chat_template_kwargs"}
    if (set(settings["generation"]) != generation_fields
            or type(settings["generation"]["n"]) is not int or settings["generation"]["n"] != 1
            or "tools" in settings or settings.get("tool_access", []) != []):
        raise ValueError("Generation settings differ from the one-completion tool-free contract")
    if not isinstance(case, dict) or set(case) != {"task", "case_id", "variant", "split", "messages"}:
        raise ValueError("Unexpected input fields; labels/metadata cannot be dispatched")
    if case["task"] not in settings["approved_task_ids"]:
        raise ValueError("Task is outside the reviewed allowlist")
    if (case["variant"] != settings["variant"] or not isinstance(case["messages"], list)
            or len(case["messages"]) != 1):
        raise ValueError("Unexpected protocol or conversation")
    message = case["messages"][0]
    if (not isinstance(message, dict) or set(message) != {"role", "content"}
            or message["role"] != "user"):
        raise ValueError("This protocol supplies exactly one original native user message")
    validate_content(message["content"])
    return {"model": settings["model"], "messages": case["messages"],
            **settings["generation"]}


def request_record(case, settings):
    """Keep record compatibility while declaring exact dispatched fields/images."""
    payload = payload_for(case, settings)
    images = validate_content(case["messages"][0]["content"])
    metadata = {key: case[key] for key in ["task", "case_id", "variant", "split"]}
    return {**metadata, "request_sha256": digest(payload), "payload": payload,
            "supplied_fields": supplied_fields_for(settings),
            "image_sha256": [item["sha256"] for item in images], "supplied_images": images}


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
    supplied_fields_for(settings)
    serving_context(settings)
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
    serving, server_record_path = serving_context(settings)
    server = json.loads(server_record_path.read_text())
    validate_server_identity(server, settings, serving, server_start_ticks(server["pid"]))
    serving_snapshot = {key: serving[key] for key in (
        "host", "port", "gpu_ids", "model", "revision", "tensor_parallel_size",
        "model_directory", "checkpoint_precision", "max_num_seqs")}
    manifest = {"configuration": settings, "configuration_sha256": file_digest(config_path),
                "runner_sha256": file_digest(Path(__file__)), "case_contract_sha256": digest(cases),
                "planned_cases": len(cases), "model_selection_on_test": False,
                "solver_tools": [], "answer_keys_available_to_solver": False,
                "serving_configuration": serving_snapshot, "server": server}
    manifest_path = folder / "run_manifest.json"
    if manifest_path.exists() and json.loads(manifest_path.read_text()) != manifest:
        raise ValueError("Run manifest changed; existing results cannot be reused")
    write_json(manifest_path, manifest)
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
        write_json(request_path, request_record(case, settings))
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
