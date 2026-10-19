#!/usr/bin/env python3
"""Run the twelve frozen validation-only GFP delivery requests, exactly once."""
from __future__ import annotations

import argparse
import concurrent.futures
from datetime import datetime
import hashlib
import json
from pathlib import Path
import threading
import time
import urllib.error
import urllib.parse
import urllib.request
from zoneinfo import ZoneInfo

from native_numeric_parser import parse_number

HERE = Path(__file__).resolve().parent
REQUEST_SHA256 = "ca610e0ef8354c76deff92da9a49f8212b33a20a48b1a43595e264c1b6d75a7d"
SETTINGS_SHA256 = "b12907572f4f4e9f1f53207a03272181ee59d2e5b180d1fa5acfe8eac71039bb"
PARSER_SHA256 = "317c8260921fbe3646c22bf61ee90b188a7f2e63319f2e88dde65ac01a173035"
MODEL = "Qwen/Qwen3.8-27B"
REVISION = "1d4bf0f2ff6012fd82039f2fa52739d0dd7c60c0"
ENDPOINT = "http://127.0.0.1:8261/v1"
CONCURRENCY = 4
CONTEXT = 65536
GENERATION = {"max_tokens": 16384, "temperature": 1.0, "top_p": .95, "top_k": 20,
              "seed": 42, "n": 1,
              "chat_template_kwargs": {"enable_thinking": True, "reasoning_effort": "medium"}}


def stamp():
    return datetime.now(ZoneInfo("America/Los_Angeles")).isoformat()


def sha(data):
    return hashlib.sha256(data).hexdigest()


def encoded(value):
    return (json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2) + "\n").encode()


def save(path, value):
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_bytes(encoded(value))
    tmp.replace(path)


def load_cases():
    raw = (HERE / "gfp_validation_requests.jsonl").read_bytes()
    settings_raw = (HERE / "gfp_validation_settings.json").read_bytes()
    if sha(raw) != REQUEST_SHA256 or sha(settings_raw) != SETTINGS_SHA256:
        raise ValueError("Frozen case/settings hash mismatch")
    if sha((HERE / "native_numeric_parser.py").read_bytes()) != PARSER_SHA256:
        raise ValueError("Native numeric parser changed")
    cases = [json.loads(line) for line in raw.decode().splitlines() if line]
    settings = json.loads(settings_raw)
    if len(cases) != 12 or settings["model_revision"] != REVISION or settings["generation"] != GENERATION:
        raise ValueError("Frozen pilot identity mismatch")
    if len({c["case_id"] for c in cases}) != 12:
        raise ValueError("Duplicate case IDs")
    for c in cases:
        p = c["payload"]
        if c["task"] != "P07" or c["split"] != "official_validation" or ":valid:" not in c["case_id"]:
            raise ValueError("Non-validation case")
        if set(p) != {"model", "messages", *GENERATION} or p["model"] != MODEL:
            raise ValueError("Unexpected payload fields")
        if any(p[k] != v for k, v in GENERATION.items()):
            raise ValueError("Sampling setting changed")
        if len(p["messages"]) != 1 or set(p["messages"][0]) != {"role", "content"} or p["messages"][0]["role"] != "user":
            raise ValueError("Unexpected message schema")
        prompt = p["messages"][0]["content"]
        if not isinstance(prompt, str) or sha(prompt.encode()) != c["prompt_sha256"]:
            raise ValueError("Prompt mismatch")
    return cases, settings


def validate_identity(identity, endpoint):
    parsed = urllib.parse.urlparse(endpoint)
    if endpoint != ENDPOINT or parsed.hostname not in {"127.0.0.1", "localhost"}:
        raise ValueError("Only the dedicated approved local endpoint is allowed")
    if (identity.get("model") != MODEL or identity.get("revision") != REVISION
            or identity.get("dtype") != "bfloat16" or identity.get("endpoint") != endpoint
            or identity.get("dedicated_gpu_count") != 1 or not identity.get("pid")):
        raise ValueError("Dedicated server identity mismatch")
    if identity.get("max_model_len", CONTEXT) != CONTEXT:
        raise ValueError("Server context mismatch")


def token_count(tokenizer, payload):
    ids = tokenizer.apply_chat_template(payload["messages"], tokenize=True,
        add_generation_prompt=True, **payload["chat_template_kwargs"])
    ids = ids["input_ids"] if hasattr(ids, "keys") else ids
    if ids and isinstance(ids[0], list):
        if len(ids) != 1:
            raise ValueError("Unexpected tokenizer batch")
        ids = ids[0]
    length = len(ids)
    if length + payload["max_tokens"] > CONTEXT:
        raise ValueError("Prompt plus output exceeds frozen 65536 context")
    return length


def check_delivery(body):
    if not isinstance(body, dict) or body.get("model") != MODEL:
        return {"passed": False, "reason": "model_identity_or_response_schema"}
    choices = body.get("choices")
    if not isinstance(choices, list) or len(choices) != 1:
        return {"passed": False, "reason": "completion_count"}
    choice = choices[0]
    if not isinstance(choice, dict):
        return {"passed": False, "reason": "choice_schema"}
    message = choice.get("message") or {}
    if not isinstance(message, dict):
        return {"passed": False, "reason": "message_schema"}
    final = message.get("content")
    empty = not isinstance(final, str) or not final.strip()
    value = None if empty else parse_number(final)
    stop = choice.get("finish_reason")
    reasoning = message.get("reasoning", message.get("reasoning_content"))
    return {
        "passed": stop == "stop" and not empty and value is not None,
        "finish_reason": stop, "empty_final": empty, "finite_final_number": value is not None,
        "separate_reasoning_present": isinstance(reasoning, str) and bool(reasoning.strip()),
        "usage": body.get("usage"),
        "biological_correctness_assessed": False,
    }


def execute_once(cases, output, endpoint, counts, plan_sha256, opener_factory=None):
    """Persist before POST; abort queued work on transport ambiguity, with no retry."""
    for folder in ("requests", "responses", "case_status"):
        (output / folder).mkdir()
    stopped = threading.Event()
    guard = threading.Lock()
    outcomes = {}
    opener_factory = opener_factory or (lambda: urllib.request.build_opener(urllib.request.ProxyHandler({})))

    def work(case):
        key = sha(case["case_id"].encode())
        start = time.monotonic()
        if stopped.is_set():
            return {"case_id": case["case_id"], "status": "not_dispatched_after_transport_failure", "passed": False}
        payload_bytes = encoded(case["payload"])
        request_record = {"case_id": case["case_id"], "attempt_started_at_pacific": stamp(),
            "plan_sha256": plan_sha256, "payload_sha256": sha(payload_bytes), "payload": case["payload"],
            "prompt_tokens": counts[case["case_id"]], "attempt": 1}
        save(output / "requests" / (key + ".json"), request_record)
        result = {"case_id": case["case_id"], "payload_sha256": sha(payload_bytes),
                  "prompt_tokens": counts[case["case_id"]], "attempt": 1}
        try:
            req = urllib.request.Request(endpoint + "/chat/completions", data=payload_bytes,
                headers={"Content-Type": "application/json"}, method="POST")
            with opener_factory().open(req, timeout=1800) as response:
                body_bytes = response.read()
                status = response.status
            (output / "responses" / (key + ".json")).write_bytes(body_bytes)
            result["response_sha256"] = sha(body_bytes)
            body = json.loads(body_bytes)
            result.update(status="response_saved", http_status=status, response_sha256=sha(body_bytes), **check_delivery(body))
        except Exception as exc:
            stopped.set()
            if isinstance(exc, urllib.error.HTTPError):
                body_bytes = exc.read()
                (output / "responses" / (key + ".http_error")).write_bytes(body_bytes)
                result.update(http_status=exc.code, response_sha256=sha(body_bytes))
            result.update(status="transport_or_response_error_no_retry", passed=False,
                          error_type=type(exc).__name__, error=str(exc))
        result.update(finished_at_pacific=stamp(), elapsed_seconds=round(time.monotonic()-start, 3))
        save(output / "case_status" / (key + ".json"), result)
        return result

    with concurrent.futures.ThreadPoolExecutor(max_workers=CONCURRENCY) as pool:
        futures = {pool.submit(work, c): c for c in cases}
        for f in concurrent.futures.as_completed(futures):
            result = f.result()
            with guard:
                outcomes[result["case_id"]] = result
                save(output / "progress.json", {"at_pacific": stamp(), "plan_sha256": plan_sha256,
                    "planned": len(cases), "terminal": len(outcomes),
                    "outcomes": [outcomes[c["case_id"]] for c in cases if c["case_id"] in outcomes]})
            print(json.dumps({"case_id": result["case_id"], "status": result["status"], "passed": result["passed"]}), flush=True)
    return [outcomes[c["case_id"]] for c in cases]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--endpoint", default=ENDPOINT)
    parser.add_argument("--identity-file", type=Path, default=HERE / "runtime/server_identity.json")
    parser.add_argument("--model-path", default="/dfs/scratch0/tchen/models/Qwen3.8-27B")
    parser.add_argument("--output", type=Path, default=HERE / "runtime/run_v1")
    parser.add_argument("--preflight-only", action="store_true")
    args = parser.parse_args()
    if args.output.exists():
        raise ValueError("Output already exists; no implicit retries or overwrites are permitted")
    cases, settings = load_cases()
    identity_raw = args.identity_file.read_bytes()
    identity = json.loads(identity_raw)
    validate_identity(identity, args.endpoint)
    from transformers import AutoTokenizer
    tokenizer = AutoTokenizer.from_pretrained(args.model_path, local_files_only=True)
    counts = {c["case_id"]: token_count(tokenizer, c["payload"]) for c in cases}
    opener = urllib.request.build_opener(urllib.request.ProxyHandler({}))
    with opener.open(args.endpoint + "/models", timeout=15) as response:
        listed = json.load(response)
    if MODEL not in {m["id"] for m in listed["data"]}:
        raise ValueError("Pinned model absent from endpoint")
    plan = {"created_at_pacific": stamp(), "configuration": settings,
        "server_identity": identity, "server_identity_sha256": sha(identity_raw),
        "runner_sha256": sha(Path(__file__).read_bytes()),
        "native_parser_sha256": sha((HERE / "native_numeric_parser.py").read_bytes()),
        "frozen_requests_sha256": REQUEST_SHA256, "concurrency": CONCURRENCY, "context_limit": CONTEXT,
        "prompt_tokens": counts, "planned": len(cases), "preflight_only": args.preflight_only,
        "retry_policy": "none; ambiguous errors stop queued dispatch and are never retried",
        "biological_correctness_assessed": False}
    if args.preflight_only:
        print(json.dumps(plan, indent=2))
        return
    args.output.mkdir(parents=True)
    plan_raw = encoded(plan)
    (args.output / "run_manifest.json").write_bytes(plan_raw)
    outcomes = execute_once(cases, args.output, args.endpoint, counts, sha(plan_raw))
    identity_unchanged = sha(args.identity_file.read_bytes()) == sha(identity_raw)
    completion = {"finished_at_pacific": stamp(), "plan_sha256": sha(plan_raw),
        "planned": len(cases), "terminal": len(outcomes),
        "responses_saved": sum(o["status"] == "response_saved" for o in outcomes),
        "delivery_passed": sum(o["passed"] for o in outcomes),
        "transport_or_response_errors": sum(o["status"] == "transport_or_response_error_no_retry" for o in outcomes),
        "not_dispatched": sum(o["status"].startswith("not_dispatched") for o in outcomes),
        "identity_unchanged": identity_unchanged,
        "all_delivered": identity_unchanged and all(o["passed"] for o in outcomes),
        "biological_correctness_assessed": False, "outcomes": outcomes}
    save(args.output / "completion.json", completion)
    if not completion["all_delivered"]:
        raise SystemExit(2)


if __name__ == "__main__":
    main()
