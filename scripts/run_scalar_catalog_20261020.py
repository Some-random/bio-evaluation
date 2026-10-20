"""One-attempt local scalar generations; no source labels, scoring or server launch.

Prospective nonthinking, grammar-constrained condition for P06/P07/P08. A root
execution grant and task-specific development delivery lock are required before
test calls. A saved request is an attempt, never permission to retry that case.
"""
from __future__ import annotations

import argparse
from collections import Counter
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime
import fcntl
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import re
import threading
import time
import urllib.error
import urllib.parse
import urllib.request
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parents[1]
MODEL = "Qwen/Qwen3.8-27B"
REVISION = "1d4bf0f2ff6012fd82039f2fa52739d0dd7c60c0"
REGEX = r"[+-]?[0-9]{1,12}(\.[0-9]{1,12})?([eE][+-]?[0-9]{1,2})?"
GENERATION = {"max_tokens": 256, "temperature": 1.0, "top_p": .95,
              "top_k": 20, "seed": 42, "n": 1,
              "chat_template_kwargs": {"enable_thinking": False},
              "structured_outputs": {"regex": REGEX}}


def stamp():
    return datetime.now(ZoneInfo("America/Los_Angeles")).isoformat()


def canonical(value):
    return (json.dumps(value, sort_keys=True, ensure_ascii=False, indent=2,
                       allow_nan=False) + "\n").encode()


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def resolve(path):
    value = Path(path)
    return value if value.is_absolute() else ROOT / value


def atomic(path, value):
    temp = Path(str(path) + ".tmp")
    temp.write_bytes(canonical(value))
    temp.replace(path)


def create(path, value):
    with Path(path).open("xb") as handle:
        handle.write(canonical(value))


def load_contract(config_path):
    config = json.loads(Path(config_path).read_text())
    if config.get("schema_version") != 1 or config.get("task_id") not in {"P06", "P07", "P08"}:
        raise ValueError("Unknown scalar task contract")
    if config.get("model") != MODEL or config.get("model_revision") != REVISION:
        raise ValueError("Model differs from the pinned local baseline")
    if config.get("split") not in {"official_test", "official_validation"}:
        raise ValueError("Unknown phase/split cannot bypass the development delivery gate")
    if config.get("generation") != GENERATION:
        raise ValueError("Generation differs from the separately named scalar condition")
    for key, hash_key in [("input_file", "input_sha256"), ("review_file", "review_sha256"),
                          ("native_numeric_parser_file", "native_numeric_parser_sha256")]:
        if sha(resolve(config[key])) != config[hash_key]:
            raise ValueError("Changed frozen file: " + key)
    for path, expected in config["files_sha256"].items():
        if sha(resolve(path)) != expected:
            raise ValueError("Changed frozen dependency: " + path)
    cases = [json.loads(line) for line in resolve(config["input_file"]).read_text().splitlines() if line]
    review = json.loads(resolve(config["review_file"]).read_text())
    ids = [case["case_id"] for case in cases]
    if len(cases) != config["planned"] or not cases or len(set(ids)) != len(ids):
        raise ValueError("Empty, duplicate or incomplete cohort")
    if ids != review["approved_case_ids"] or review.get("task_id") != config["task_id"]:
        raise ValueError("Ordered case cohort differs from input review")
    held_ids = {row["case_id"] if isinstance(row, dict) else row for row in review.get("held_cases", [])}
    if set(ids) & held_ids:
        raise ValueError("Held case present in solver cohort")
    for case in cases:
        if set(case) != {"task_id", "case_id", "messages"} or case["task_id"] != config["task_id"]:
            raise ValueError("Unexpected input fields; only isolated requests may reach the solver")
        messages = case["messages"]
        if len(messages) != 1 or set(messages[0]) != {"role", "content"} or messages[0]["role"] != "user":
            raise ValueError("Require one fresh user message without history or tools")
        if not isinstance(messages[0]["content"], str) or not messages[0]["content"]:
            raise ValueError("Empty/nontext prompt")
    spec = importlib.util.spec_from_file_location("frozen_native_scalar_parser", resolve(config["native_numeric_parser_file"]))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    parser = getattr(module, config.get("native_numeric_parser_function", "parse_number"))
    return config, cases, parser


def payload(case):
    return {"model": MODEL, "messages": case["messages"], **GENERATION}


def parse_delivery(body, native_parser):
    choices = body.get("choices", [])
    if len(choices) != 1:
        raise ValueError("Require exactly one completion choice")
    choice = choices[0]
    message = choice["message"]
    final = message.get("content")
    reasoning = message.get("reasoning", message.get("reasoning_content"))
    refusal = message.get("refusal")
    finish = choice.get("finish_reason")
    empty = not isinstance(final, str) or not final.strip()
    grammar_pass = isinstance(final, str) and re.fullmatch(REGEX, final) is not None
    native_value = native_parser(final) if isinstance(final, str) else None
    finite = (type(native_value) in (int, float) and math.isfinite(native_value))
    passed = (finish == "stop" and grammar_pass and finite and not reasoning
              and not refusal and not message.get("tool_calls"))
    return {"finish_reason": finish, "empty_final": empty,
            "truncated": finish == "length", "refusal": bool(refusal),
            "reasoning_present": bool(reasoning), "grammar_pass": grammar_pass,
            "native_parse_pass": finite, "prediction": native_value if finite else None,
            "delivery_passed": bool(passed), "usage": body.get("usage", {})}


def validate_grant(grant_path, config_path, config):
    grant = json.loads(Path(grant_path).read_text())
    if grant.get("authorized") is not True or grant.get("config_sha256") != sha(config_path):
        raise ValueError("Missing exact centralized execution grant")
    if grant.get("task_id") != config["task_id"] or grant.get("run_id") != config["run_id"]:
        raise ValueError("Grant belongs to another task/run")
    parts = urllib.parse.urlsplit(grant["endpoint"])
    if parts.scheme != "http" or parts.hostname not in {"127.0.0.1", "localhost", "::1"} or parts.path.rstrip("/") != "/v1":
        raise ValueError("Only the centrally allocated loopback vLLM endpoint is allowed")
    identity_path = resolve(grant["server_identity_file"])
    if sha(identity_path) != grant["server_identity_sha256"]:
        raise ValueError("Server identity hash mismatch")
    identity = json.loads(identity_path.read_text())
    if identity.get("model") != MODEL or identity.get("revision", identity.get("model_revision")) != REVISION:
        raise ValueError("Server model/revision mismatch")
    if identity.get("dtype") not in {"bfloat16", "bf16"}:
        raise ValueError("Server must preserve original BF16 checkpoint")
    return grant, identity


def validate_development(config, completion_path):
    if config["split"] != "official_test":
        return
    if completion_path is None:
        raise ValueError("Full test requires sealed task-specific development delivery evidence")
    done = json.loads(Path(completion_path).read_text())
    if done.get("task_id") != config["task_id"] or done.get("config_sha256") != config["development_config_sha256"]:
        raise ValueError("Development evidence does not match frozen task/condition")
    if done.get("generation") != GENERATION or done.get("biological_correctness_assessed") is not False:
        raise ValueError("Development evidence has an unexpected protocol or correctness assessment")
    if not done.get("delivery_passed_all") or not (done["planned"] == done["terminal"] == done["responses_saved"] == done["delivery_passed"]):
        raise ValueError("Development delivery gate failed")
    for key in ["transport_errors", "http_errors", "response_errors", "truncations", "empty_finals", "refusals", "reasoning_present"]:
        if done[key] != 0:
            raise ValueError("Nonzero development delivery failure: " + key)
    lock_path = Path(completion_path).parent / "prediction_lock.json"
    if sha(lock_path) != done["prediction_lock_sha256"]:
        raise ValueError("Development output lock differs")
    for path, expected in json.loads(lock_path.read_text())["files_sha256"].items():
        if sha(Path(completion_path).parent / path) != expected:
            raise ValueError("Development evidence file changed: " + path)


def count_tokens(config, cases, model_path, context_limit):
    from transformers import AutoTokenizer
    tokenizer = AutoTokenizer.from_pretrained(model_path, local_files_only=True)
    counts = []
    for case in cases:
        result = tokenizer.apply_chat_template(case["messages"], tokenize=True,
                                              add_generation_prompt=True, **GENERATION["chat_template_kwargs"])
        ids = result["input_ids"] if hasattr(result, "keys") else result
        if ids and isinstance(ids[0], list):
            if len(ids) != 1:
                raise ValueError("Unexpected tokenizer batch")
            ids = ids[0]
        if len(ids) + GENERATION["max_tokens"] > context_limit:
            raise ValueError("Full input plus output exceeds context: " + case["case_id"])
        counts.append({"case_id": case["case_id"], "prompt_tokens": len(ids)})
    return {"at_pacific": stamp(), "task_id": config["task_id"], "planned": len(cases),
            "full_inputs_preserved": True, "context_limit": context_limit,
            "max_prompt_tokens": max(row["prompt_tokens"] for row in counts), "counts": counts}


def run(args):
    config_path = args.config.resolve()
    config, cases, native_parser = load_contract(config_path)
    if args.check_only:
        print(json.dumps({"task_id": config["task_id"], "planned": len(cases), "config_sha256": sha(config_path), "no_model_calls": True}))
        return
    if args.grant is None:
        raise ValueError("Central root execution grant required")
    grant, identity = validate_grant(args.grant, config_path, config)
    validate_development(config, args.development_completion)
    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=True)
    with (output / ".runner.lock").open("a") as lock_handle:
        fcntl.flock(lock_handle, fcntl.LOCK_EX | fcntl.LOCK_NB)
        return run_locked(args, config_path, config, cases, native_parser, grant, identity, output)


def run_locked(args, config_path, config, cases, native_parser, grant, identity, output):
    manifest = output / "run_manifest.json"
    if manifest.exists():
        if not args.resume_unattempted or json.loads(manifest.read_text())["config_sha256"] != sha(config_path):
            raise ValueError("Output already exists; explicit untouched-case continuation required")
        if (output / "completion.json").exists():
            raise ValueError("Completed cohort is sealed")
    else:
        create(manifest, {"created_at_pacific": stamp(), "config_sha256": sha(config_path),
                         "configuration": config, "server_identity": identity,
                         "grant_sha256": sha(args.grant), "generation": GENERATION,
                         "runner_sha256": sha(Path(__file__)), "biological_correctness_assessed": False})
    preflight = count_tokens(config, cases, args.model_path, args.context_limit)
    atomic(output / "tokenizer_preflight.json", preflight)
    opener = urllib.request.build_opener(urllib.request.ProxyHandler({}))
    with opener.open(grant["endpoint"].rstrip("/") + "/models", timeout=30) as response:
        if MODEL not in {item["id"] for item in json.load(response)["data"]}:
            raise ValueError("Local endpoint model ID mismatch")
    for name in ["requests", "responses", "outcomes", "errors"]:
        (output / name).mkdir(exist_ok=True)
    stop = threading.Event()
    write_lock = threading.Lock()
    outcomes = {}
    attempted = set()
    for case in cases:
        key = hashlib.sha256(case["case_id"].encode()).hexdigest()
        path = output / "outcomes" / (key + ".json")
        if (output / "requests" / (key + ".json")).exists():
            attempted.add(case["case_id"])
        if path.exists():
            outcomes[case["case_id"]] = json.loads(path.read_text())
        elif (output / "requests" / (key + ".json")).exists():
            # Never infer an absent response means an absent attempt.
            row = {"case_id": case["case_id"], "status": "ambiguous_attempt_not_retried", "delivery_passed": False}
            create(path, row)
            outcomes[case["case_id"]] = row

    totals = Counter()

    def tally(row):
        totals["terminal"] += 1
        totals["responses_saved"] += bool(row.get("response_saved"))
        totals["delivery_passed"] += bool(row.get("delivery_passed"))
        for output_key, status in [("transport_errors", "transport_error"), ("http_errors", "http_error"),
                                   ("response_errors", "response_error"), ("ambiguous_attempts", "ambiguous_attempt_not_retried")]:
            totals[output_key] += row.get("status") == status
        for output_key, row_key in [("truncations", "truncated"), ("empty_finals", "empty_final"),
                                    ("refusals", "refusal"), ("reasoning_present", "reasoning_present")]:
            totals[output_key] += bool(row.get(row_key))

    for row in outcomes.values():
        tally(row)

    def progress():
        values = {"at_pacific": stamp(), "task_id": config["task_id"], "run_id": config["run_id"],
                  "config_sha256": sha(config_path), "planned": len(cases),
                  "phase": "benchmark_generation" if config["split"] == "official_test" else "development",
                  **{key: totals[key] for key in ["terminal", "responses_saved", "delivery_passed", "transport_errors",
                     "http_errors", "response_errors", "ambiguous_attempts", "truncations", "empty_finals", "refusals", "reasoning_present"]},
                  "attempted_confirmed": len(attempted),
                  "transport_or_response_errors": totals["transport_errors"] + totals["http_errors"] + totals["response_errors"],
                  "not_dispatched": len(cases) - len(attempted),
                  "biological_correctness_assessed": False}
        atomic(output / "progress.json", values)
        return values

    def one(case):
        if stop.is_set():
            return
        case_id = case["case_id"]
        key = hashlib.sha256(case_id.encode()).hexdigest()
        raw_request = canonical(payload(case))
        request_path = output / "requests" / (key + ".json")
        with request_path.open("xb") as handle:
            handle.write(raw_request)
        with write_lock:
            attempted.add(case_id)
        started = time.monotonic()
        row = {"case_id": case_id, "request_sha256": sha(request_path), "started_at_pacific": stamp(), "delivery_passed": False}
        try:
            request = urllib.request.Request(grant["endpoint"].rstrip("/") + "/chat/completions", data=raw_request,
                                            headers={"Content-Type": "application/json"}, method="POST")
            with opener.open(request, timeout=args.timeout) as response:
                raw = response.read()
            response_path = output / "responses" / (key + ".json")
            with response_path.open("xb") as handle:
                handle.write(raw)
            row.update(response_saved=True, response_sha256=sha(response_path))
            body = json.loads(raw)
            row.update(parse_delivery(body, native_parser), status="response_saved")
            if row["refusal"]:
                stop.set()  # Preserve provider refusal and stop new submissions.
        except urllib.error.HTTPError as exc:
            raw = exc.read()
            with (output / "errors" / (key + ".http")).open("xb") as handle:
                handle.write(raw)
            row.update(status="http_error", http_status=exc.code)
            stop.set()  # Policy/access/server errors require review; never retry.
        except (urllib.error.URLError, TimeoutError, ConnectionError, OSError) as exc:
            row.update(status="transport_error", error_type=type(exc).__name__)
            stop.set()
        except (ValueError, KeyError, TypeError, IndexError) as exc:
            row.update(status="response_error", error_type=type(exc).__name__)
            stop.set()
        row.update(elapsed_seconds=round(time.monotonic()-started, 3), finished_at_pacific=stamp())
        create(output / "outcomes" / (key + ".json"), row)
        with write_lock:
            outcomes[case_id] = row
            tally(row)
            progress()
        return row

    progress()
    pending = [case for case in cases if case["case_id"] not in outcomes]
    with ThreadPoolExecutor(max_workers=args.concurrency) as executor:
        futures = [executor.submit(one, case) for case in pending]
        for future in as_completed(futures):
            future.result()
    values = progress()
    files = {str(p.relative_to(output)): sha(p) for category in ["requests", "responses", "outcomes", "errors"]
             for p in sorted((output/category).iterdir()) if p.is_file()}
    files["run_manifest.json"] = sha(manifest)
    files["tokenizer_preflight.json"] = sha(output / "tokenizer_preflight.json")
    create(output / "prediction_lock.json", {"sealed_at_pacific": stamp(), "files_sha256": files,
                                            "config_sha256": sha(config_path), "reference_labels_opened": False})
    values.update(generation=GENERATION, prediction_lock_sha256=sha(output / "prediction_lock.json"),
                  delivery_passed_all=values["delivery_passed"] == len(cases),
                  all_passed=values["delivery_passed"] == len(cases),
                  status="terminal_complete_cohort" if values["terminal"] == len(cases) else "stopped_incomplete_cohort")
    create(output / "completion.json", values)
    print(json.dumps(values), flush=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", required=True, type=Path)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--grant", type=Path)
    parser.add_argument("--development-completion", type=Path)
    parser.add_argument("--model-path", default="/dfs/scratch0/tchen/models/Qwen3.8-27B")
    parser.add_argument("--context-limit", type=int, default=65536)
    parser.add_argument("--concurrency", type=int, default=4)
    parser.add_argument("--timeout", type=int, default=900)
    parser.add_argument("--resume-unattempted", action="store_true")
    parser.add_argument("--check-only", action="store_true")
    args = parser.parse_args()
    if not args.check_only and args.output is None:
        parser.error("--output required for execution")
    if not 1 <= args.concurrency <= 32:
        parser.error("--concurrency must be 1..32 under centralized coordination")
    run(args)


if __name__ == "__main__":
    main()
