#!/usr/bin/env python3
"""Frozen text comparison dispatch. Preparation/dry-run never calls an API.

prepare converts reviewed dedicated payloads + a pinned minimal case roster into
an immutable minimal bundle. dry-run and run start a fresh Python worker using
Linux Landlock; that worker cannot read the repository, reference files, Qwen
outputs, home credentials, or arbitrary /tmp files. Live run additionally needs
explicit, hash-pinned scoped authorization and task-specific development gates.
No scoring, shared conversation, tools, retries, or resume is implemented here.

Example (all hashes must come from reviewed artifacts):
  prepare --requests ROWS --requests-sha256 SHA --roster ROSTER \
    --roster-sha256 SHA --protocol PROTOCOL --protocol-sha256 SHA \
    --protocol-id ID --model gpt-6-luna --bundle BUNDLE
  dry-run --bundle BUNDLE --bundle-sha256 MANIFEST_SHA --output NEW_DIR
  run --bundle BUNDLE --bundle-sha256 MANIFEST_SHA --output NEW_DIR \
    --authorization AUTH --authorization-sha256 SHA \
    --development-gate GATE --development-gate-sha256 SHA \
    --reviewed-input-receipt INPUT_REVIEW --risk-review-receipt RISK_REVIEW \
    --development-evidence DEV_PREDICTIONS_LOCK

The live command cannot broadly resume the repository's held historical scope. It
loads OPENAI_API_KEY and the existing private stable safety identifier only after
all gates pass. Its secret pipe is closed before the Landlock restriction. The
identifier value and API key are never written to artifacts; hashes of the actual
submitted body and a separately archived identity-redacted body are recorded.
"""
from __future__ import annotations

import argparse
import concurrent.futures
import ctypes
import datetime as dt
import encodings.idna  # preload DNS codec before restricting filesystem reads
import hashlib
import http.client
import json
import os
from pathlib import Path
import re
import socket
import ssl
import subprocess
import sys
import time
import urllib.error
import urllib.request
from zoneinfo import ZoneInfo

PACIFIC = ZoneInfo("America/Los_Angeles")
ENDPOINT = "https://api.openai.com/v1/responses"
MODELS = {"gpt-6-luna", "gpt-6.1-sol"}
TASKS = {"B01", "B03", "P03"}
BUNDLE_FILES = {"manifest.json", "requests.jsonl", "dispatcher.py"}
PAYLOAD_KEYS = {"model", "input", "reasoning", "max_output_tokens", "service_tier", "store"}


def now():
    return dt.datetime.now(PACIFIC).isoformat()


def canonical(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False).encode("utf-8")


def sha(data):
    return hashlib.sha256(data).hexdigest()


def read_pinned(path, expected):
    path = Path(path)
    if path.is_symlink() or not path.is_file():
        raise ValueError("Pinned input must be a regular, nonsymlink file")
    data = path.read_bytes()
    if not re.fullmatch("[0-9a-f]{64}", expected or "") or sha(data) != expected:
        raise ValueError("Pinned file SHA-256 mismatch")
    return data


def reject_duplicate_keys(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError("Duplicate JSON key")
        result[key] = value
    return result


def parse_json(data):
    return json.loads(data, object_pairs_hook=reject_duplicate_keys, parse_constant=lambda value: (_ for _ in ()).throw(ValueError("Nonfinite JSON constant")))


def validate_payload(payload, model):
    """Allow exactly one fresh user text input and the frozen 4K condition."""
    if not isinstance(payload, dict) or set(payload) != PAYLOAD_KEYS:
        raise ValueError("Unexpected or missing model-facing payload fields")
    if model not in MODELS or payload["model"] != model:
        raise ValueError("Model mismatch")
    if payload["reasoning"] != {"effort": "medium"}:
        raise ValueError("Reasoning condition mismatch")
    if type(payload["max_output_tokens"]) is not int or payload["max_output_tokens"] != 4096:
        raise ValueError("Output allowance mismatch")
    if payload["service_tier"] != "default" or payload["store"] is not False:
        raise ValueError("Tier/storage mismatch")
    items = payload["input"]
    if not isinstance(items, list) or len(items) != 1:
        raise ValueError("Exactly one independent user input is required")
    item = items[0]
    if not isinstance(item, dict) or set(item) != {"role", "content"} or item["role"] != "user":
        raise ValueError("Only a user role is permitted")
    content = item["content"]
    if not isinstance(content, list) or len(content) != 1:
        raise ValueError("Exactly one text item is required")
    text = content[0]
    if not isinstance(text, dict) or set(text) != {"type", "text"} or text["type"] != "input_text":
        raise ValueError("This dispatcher supports the frozen text stage only")
    if not isinstance(text["text"], str) or not text["text"].strip():
        raise ValueError("Empty input text")
    return canonical(payload)


def prepare_rows(request_bytes, roster, protocol_id, model):
    if roster.get("protocol_id") != protocol_id or roster.get("model") != model:
        raise ValueError("Roster protocol/model mismatch")
    expected = roster.get("cases")
    if not isinstance(expected, list) or not expected:
        raise ValueError("Missing exact ordered case roster")
    rows = [parse_json(line) for line in request_bytes.splitlines() if line.strip()]
    if len(rows) != len(expected):
        raise ValueError("Case count mismatch")
    clean, seen = [], set()
    for row, case in zip(rows, expected):
        key = (row.get("task_id"), row.get("case_id"))
        if key != (case.get("task_id"), case.get("case_id")) or key in seen:
            raise ValueError("Case identity/order mismatch or duplicate")
        if key[0] not in TASKS or not isinstance(key[1], str) or not key[1]:
            raise ValueError("Unreviewed task or invalid case identity")
        seen.add(key)
        # Deliberately never consume any other field from the surrounding row.
        payload = row.get("payload_without_private_safety_identifier")
        payload_bytes = validate_payload(payload, model)
        digest = sha(payload_bytes)
        if digest != case.get("payload_sha256"):
            raise ValueError("Frozen payload hash mismatch")
        clean.append({"task_id": key[0], "case_id": key[1], "payload_sha256": digest,
                      "payload_without_private_safety_identifier": payload})
    return clean


def write_new(path, data):
    fd = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    with os.fdopen(fd, "wb") as stream:
        stream.write(data)
        stream.flush()
        os.fsync(stream.fileno())


def prepare_bundle(args):
    request_bytes = read_pinned(args.requests, args.requests_sha256)
    protocol = parse_json(read_pinned(args.protocol, args.protocol_sha256))
    expected_generation = {"max_output_tokens": 4096, "reasoning": {"effort": "medium"}, "service_tier": "default", "store": False}
    if protocol.get("protocol_id") != args.protocol_id or args.model not in protocol.get("allowed_models", []) or protocol.get("generation") != expected_generation:
        raise ValueError("Frozen protocol identity/model/generation mismatch")
    roster = parse_json(read_pinned(args.roster, args.roster_sha256))
    rows = prepare_rows(request_bytes, roster, args.protocol_id, args.model)
    if not {r["task_id"] for r in rows}.issubset(set(protocol.get("task_ids", []))):
        raise ValueError("Frozen protocol task scope mismatch")
    bundle = Path(args.bundle).resolve()
    bundle.mkdir(mode=0o700, parents=False, exist_ok=False)
    request_data = b"".join(canonical(row) + b"\n" for row in rows)
    code = Path(__file__).read_bytes()
    manifest = {"schema_version": 1, "protocol_id": args.protocol_id, "model": args.model,
                "frozen_protocol_sha256": args.protocol_sha256,
                "case_count": len(rows), "requests_sha256": sha(request_data),
                "dispatcher_sha256": sha(code), "source_request_file_sha256": args.requests_sha256,
                "source_roster_sha256": args.roster_sha256,
                "cases": [{k: row[k] for k in ("task_id", "case_id", "payload_sha256")} for row in rows],
                "endpoint": ENDPOINT, "dispatch_authorized": False,
                "mode": "frozen_text_4k_no_tools_no_retries"}
    for name, data in (("requests.jsonl", request_data), ("dispatcher.py", code), ("manifest.json", canonical(manifest) + b"\n")):
        write_new(bundle / name, data)
        (bundle / name).chmod(0o444)
    bundle.chmod(0o555)
    return {"bundle": str(bundle), "bundle_sha256": sha((bundle / "manifest.json").read_bytes()),
            "case_count": len(rows), "new_inference_calls": 0}


def load_bundle(bundle, manifest_sha):
    bundle = Path(bundle).resolve()
    if set(p.name for p in bundle.iterdir()) != BUNDLE_FILES or any(p.is_symlink() for p in bundle.iterdir()):
        raise ValueError("Unexpected bundle file or symlink")
    manifest = parse_json(read_pinned(bundle / "manifest.json", manifest_sha))
    if manifest.get("schema_version") != 1 or manifest.get("endpoint") != ENDPOINT:
        raise ValueError("Unsupported execution manifest")
    read_pinned(bundle / "dispatcher.py", manifest["dispatcher_sha256"])
    data = read_pinned(bundle / "requests.jsonl", manifest["requests_sha256"])
    rows = prepare_rows(data, {"protocol_id": manifest["protocol_id"], "model": manifest["model"],
                               "cases": manifest["cases"]}, manifest["protocol_id"], manifest["model"])
    if len(rows) != manifest["case_count"]:
        raise ValueError("Incomplete bundle")
    return manifest, rows


def check_execution_gates(auth, gate, manifest, development=False):
    """Narrow new reviewed scope; never rewrite historical warning/appeal facts."""
    required = {"schema_version": 1, "dispatch_authorized": True,
                "scope_review_passed": True, "prior_flagged_requests_excluded": True,
                "no_broad_resume": True,
                "purpose": "development_delivery_only" if development else "frozen_benchmark_comparison"}
    if any(auth.get(k) != v for k, v in required.items()):
        raise ValueError("Missing explicit scoped authorization; historical holds remain")
    if not isinstance(auth.get("current_user_authorization_source"), str) or not auth["current_user_authorization_source"].strip():
        raise ValueError("Current user authorization source is required")
    tasks = {r["task_id"] for r in manifest["cases"]}
    if manifest["model"] not in auth.get("allowed_models", []) or manifest["protocol_id"] not in auth.get("allowed_protocol_ids", []):
        raise ValueError("This model/protocol is not explicitly authorized")
    if not tasks.issubset(set(auth.get("allowed_tasks", []))):
        raise ValueError("Task scope is not explicitly authorized")
    pins = {"frozen_roster_sha256": manifest["source_roster_sha256"],
            "frozen_protocol_sha256": manifest["frozen_protocol_sha256"]}
    if any(auth.get(k) != v for k, v in pins.items()):
        raise ValueError("Authorization does not match the exact frozen inputs/protocol")
    for key in ("reviewed_input_receipt_sha256", "risk_review_receipt_sha256"):
        if re.fullmatch("[0-9a-f]{64}", auth.get(key, "")) is None:
            raise ValueError("Scoped authorization has no pinned input/risk review")
    guard, estimate = auth.get("spending_guard_usd"), auth.get("estimated_max_run_cost_usd")
    if type(guard) not in (int, float) or type(estimate) not in (int, float) or not 0 < estimate <= guard <= 50:
        raise ValueError("A reviewed run-cost estimate within the initial $50 spending guard is required")
    if development:
        return
    required_gate = {"schema_version": 1, "protocol_id": manifest["protocol_id"], "model": manifest["model"],
                     "reviewed": True, "delivery_passed": True, "biological_correctness_assessed": False,
                     "max_output_tokens": 4096, "reasoning_effort": "medium", "dispatch_authorized": True,
                     "frozen_protocol_sha256": manifest["frozen_protocol_sha256"],
                     "dispatcher_sha256": manifest["dispatcher_sha256"]}
    if not isinstance(gate, dict) or any(gate.get(k) != v for k, v in required_gate.items()) or not tasks.issubset(set(gate.get("task_ids", []))):
        raise ValueError("Missing reviewed task-specific development delivery gate")
    if re.fullmatch("[0-9a-f]{64}", gate.get("development_evidence_sha256", "")) is None:
        raise ValueError("Development gate has no pinned completed evidence")


def verify_review_receipts(auth, manifest, reviewed_input_path, risk_review_path):
    """Hash real reviewed documents, then bind both to this exact model roster."""
    expected = {"protocol_id": manifest["protocol_id"], "model": manifest["model"],
                "frozen_roster_sha256": manifest["source_roster_sha256"],
                "frozen_protocol_sha256": manifest["frozen_protocol_sha256"],
                "case_count": manifest["case_count"]}
    expected_tasks = {row["task_id"] for row in manifest["cases"]}
    hashes = {}
    for key, source in (("reviewed_input_receipt_sha256", reviewed_input_path),
                        ("risk_review_receipt_sha256", risk_review_path)):
        if not source:
            raise ValueError("Actual input and risk review receipts are required")
        raw = read_pinned(source, auth[key])
        receipt = parse_json(raw)
        if receipt.get("scope_review_passed") is not True or receipt.get("prior_flagged_requests_excluded") is not True:
            raise ValueError("Input/risk review receipt did not pass scoped review")
        matches = [row for row in receipt.get("reviewed_bundles", [])
                   if isinstance(row, dict) and all(row.get(k) == v for k, v in expected.items())
                   and set(row.get("task_ids", [])) == expected_tasks]
        if len(matches) != 1:
            raise ValueError("Review receipt does not bind this exact case roster/model/protocol")
        hashes[key] = sha(raw)
    return hashes


def verify_development_evidence(gate, manifest, evidence_path):
    """Inspect the actual sealed development outputs before benchmark credentials."""
    if not evidence_path:
        raise ValueError("Actual completed development evidence is required")
    path = Path(evidence_path)
    lock = parse_json(read_pinned(path, gate["development_evidence_sha256"]))
    seal = path.with_suffix(".sha256")
    if not seal.is_file() or seal.read_text().strip() != gate["development_evidence_sha256"]:
        raise ValueError("Development evidence is not sealed")
    expected = {"model": manifest["model"], "protocol_id": gate.get("development_protocol_id"),
                "frozen_protocol_sha256": gate.get("development_protocol_sha256"),
                "frozen_roster_sha256": gate.get("development_roster_sha256"),
                "frozen_request_file_sha256": gate.get("development_request_file_sha256"),
                "dispatcher_sha256": manifest["dispatcher_sha256"], "mode": "live",
                "scoring_performed": False, "no_retries": True}
    if any(value is None or lock.get(key) != value for key, value in expected.items()):
        raise ValueError("Wrong development model/protocol/code or unreviewed evidence")
    rows = lock.get("rows", [])
    count = gate.get("development_case_count")
    if type(count) is not int or count <= 0 or count != lock.get("case_count") or count != len(rows) or lock.get("new_inference_calls") != count:
        raise ValueError("Incomplete development case set")
    tasks = {row["task_id"] for row in manifest["cases"]}
    if not tasks.issubset({row.get("task_id") for row in rows}):
        raise ValueError("Development evidence does not cover benchmark tasks")
    seen = set()
    for row in rows:
        key = (row.get("task_id"), row.get("case_id"))
        if key in seen or any(row.get(k) != lock.get(k) for k in ("model", "protocol_id", "run_id")):
            raise ValueError("Development identity mismatch or duplicate case")
        seen.add(key)
        if row.get("terminal_status") != "completed" or row.get("http_status") != 200 or row.get("empty_final") is not False or row.get("truncated") is not False or row.get("refused") is not False:
            raise ValueError("Development did not reliably deliver every answer")
        artifacts = {}
        for name in ("request", "response", "visible_final"):
            relative = row.get(name + "_path")
            if not isinstance(relative, str):
                raise ValueError("Missing development artifact path")
            artifact_path = path.parent / relative
            if not artifact_path.resolve().is_relative_to(path.parent.resolve()):
                raise ValueError("Development artifact leaves sealed output directory")
            artifacts[name] = read_pinned(artifact_path, row.get(name + "_sha256"))
        request = parse_json(artifacts["request"])
        public = validate_payload(request.get("payload_without_private_safety_identifier"), manifest["model"])
        if sha(public) != row.get("payload_sha256") or sha(public) != request.get("payload_sha256"):
            raise ValueError("Development actual request payload mismatch")
        response = parse_json(artifacts["response"])
        text, refused = extract_visible(response)
        if response.get("model") != manifest["model"] or response.get("status") != "completed" or refused or not text.strip() or artifacts["visible_final"] != text.encode("utf-8"):
            raise ValueError("Development raw response does not establish usable delivery")
    return gate["development_evidence_sha256"]


def stop_for_provider_error(status, raw, terminal):
    if status in {401, 403} or terminal == "refusal":
        return True
    if status in (None, 200):
        return False
    try:
        error = parse_json(raw).get("error", {})
        code = str(error.get("code", "")).lower()
        kind = str(error.get("type", "")).lower()
    except (ValueError, AttributeError, TypeError):
        code, kind = "", ""
    access_codes = {"model_not_found", "model_access_denied", "access_denied", "permission_denied", "insufficient_permissions", "account_deactivated"}
    if code in access_codes or kind in access_codes:
        return True
    lowered = raw.lower()
    return any(word in lowered for word in (b"policy_violation", b"bio_policy", b"content_policy", b"account_deactivated"))


# Linux Landlock ABI, from linux/landlock.h. No privilege or root helper needed.
READ_FILE, READ_DIR, EXECUTE = 1 << 2, 1 << 3, 1
WRITE_FILE = 1 << 1
FS_V1_ALL = (1 << 13) - 1
REFER, TRUNCATE = 1 << 13, 1 << 14


def restrict_filesystem(bundle, output):
    """Irreversibly deny reads outside a minimal runtime allowlist; fail closed."""
    if sys.platform != "linux":
        raise RuntimeError("Linux Landlock isolation is required")
    libc = ctypes.CDLL(None, use_errno=True)
    abi = libc.syscall(444, 0, 0, 1)
    if abi < 1:
        raise RuntimeError("Landlock unavailable; refusing an unisolated worker")
    handled = FS_V1_ALL | (REFER if abi >= 2 else 0) | (TRUNCATE if abi >= 3 else 0)
    class Ruleset(ctypes.Structure):
        _fields_ = [("handled_access_fs", ctypes.c_uint64)]
    class Beneath(ctypes.Structure):
        _pack_ = 1
        _fields_ = [("allowed_access", ctypes.c_uint64), ("parent_fd", ctypes.c_int)]
    ruleset = libc.syscall(444, ctypes.byref(Ruleset(handled)), ctypes.sizeof(Ruleset), 0)
    if ruleset < 0:
        raise OSError(ctypes.get_errno(), "Cannot create Landlock ruleset")
    readonly = READ_FILE | READ_DIR
    allowed = [(Path(bundle), readonly), (Path(output), handled & ~EXECUTE)]
    # Only interpreter/system code and TLS/DNS resources, never home, /dfs,
    # /data, /tmp, current working directory or the evaluation repository.
    for item in ("/usr/lib", "/usr/local/lib", "/lib", "/lib64", "/etc/ssl", "/etc/hosts",
                 "/etc/resolv.conf", "/etc/nsswitch.conf", "/etc/gai.conf", "/dev/urandom", "/dev/null"):
        path = Path(item)
        if path.exists():
            rights = readonly if path.is_dir() else READ_FILE
            allowed.append((path.resolve(), rights))
    try:
        for path, rights in allowed:
            fd = os.open(path, os.O_PATH | os.O_CLOEXEC)
            try:
                if libc.syscall(445, ruleset, 1, ctypes.byref(Beneath(rights, fd)), 0) != 0:
                    raise OSError(ctypes.get_errno(), "Cannot install Landlock path rule")
            finally:
                os.close(fd)
        if libc.prctl(38, 1, 0, 0, 0) != 0 or libc.syscall(446, ruleset, 0) != 0:
            raise OSError(ctypes.get_errno(), "Cannot restrict worker filesystem")
    finally:
        os.close(ruleset)
    return int(abi)


def extract_visible(response):
    chunks, refused = [], False
    for item in response.get("output", []):
        if isinstance(item, dict) and item.get("type") == "refusal":
            refused = True
        if not isinstance(item, dict) or item.get("type") != "message" or item.get("role") != "assistant":
            continue
        for part in item.get("content", []):
            if part.get("type") == "output_text" and isinstance(part.get("text"), str):
                chunks.append(part["text"])
            elif part.get("type") == "refusal":
                refused = True
    return "\n".join(chunks), refused


def live_transport(body, key):
    request = urllib.request.Request(ENDPOINT, data=body, method="POST",
                                     headers={"Authorization": "Bearer " + key, "Content-Type": "application/json"})
    # Do not inherit an HTTP proxy that could redirect this frozen endpoint.
    class NoRedirect(urllib.request.HTTPRedirectHandler):
        def redirect_request(self, request, fp, code, message, headers, url):
            return None
    opener = urllib.request.build_opener(urllib.request.ProxyHandler({}), NoRedirect())
    try:
        with opener.open(request, timeout=180) as reply:
            return reply.status, reply.read(), {"request_id": reply.headers.get("x-request-id")}
    except urllib.error.HTTPError as error:
        return error.code, error.read(), {"request_id": error.headers.get("x-request-id")}


def run_cases(manifest, rows, output, run_id, identifier, transport, dry_run=False, workers=4):
    """Transport receives only verified final body bytes, never the source row."""
    output = Path(output)
    started = now()
    records = [None] * len(rows)
    calls = [0]
    if not 1 <= workers <= 8:
        raise ValueError("Concurrency must be between one and eight")

    def execute(index, row):
        stem = f"case_{index:05d}"
        payload = row["payload_without_private_safety_identifier"]
        public_bytes = validate_payload(payload, manifest["model"])
        if sha(public_bytes) != row["payload_sha256"]:
            raise ValueError("Payload changed immediately before submission")
        actual = dict(payload, safety_identifier=identifier)
        actual_bytes = canonical(actual)
        request_name, response_name, final_name = stem + ".request.json", stem + ".response.json", stem + ".final.txt"
        # Archive only the dedicated public payload. Never archive identifier.
        public_request = {"payload_without_private_safety_identifier": payload,
                          "private_safety_identifier_added": True,
                          "actual_submitted_payload_sha256": sha(actual_bytes),
                          "payload_sha256": sha(public_bytes)}
        request_bytes = canonical(public_request) + b"\n"
        write_new(output / request_name, request_bytes)
        receipt = {"task_id": row["task_id"], "case_id": row["case_id"], "protocol_id": manifest["protocol_id"],
                   "run_id": run_id, "model": manifest["model"], "payload_sha256": sha(public_bytes),
                   "actual_submitted_payload_sha256": sha(actual_bytes), "prepared_at_pacific": now(),
                   "mode": "dry_run_zero_network" if dry_run else "live", "attempt": 1}
        # fsync the wire hash receipt immediately before handing exact bytes to
        # transport. No code may append history or mutate payload after this.
        write_new(output / (stem + ".dispatch_receipt.json"), canonical(receipt) + b"\n")
        begin = time.monotonic()
        status, raw, response_metadata, usage, response_id = None, None, {}, None, None
        terminal, finish, text, refused, truncated = "transport_error", None, "", False, False
        try:
            result = transport(actual_bytes)
            status, raw = result[:2]
            if len(result) == 3:
                response_metadata = result[2]
            if not isinstance(raw, bytes):
                raise TypeError("Transport must return raw bytes")
        except Exception as error:
            raw = canonical({"local_transport_error_type": type(error).__name__}) + b"\n"
        if status is not None:
            terminal = "http_error" if status != 200 else "response_error"
            if status == 200:
                try:
                    response = parse_json(raw)
                    if not isinstance(response, dict) or response.get("model") != manifest["model"]:
                        raise ValueError("Unexpected response model")
                    usage, response_id = response.get("usage"), response.get("id")
                    finish = response.get("status")
                    text, refused = extract_visible(response)
                    truncated = finish == "incomplete" and response.get("incomplete_details", {}).get("reason") == "max_output_tokens"
                    terminal = "refusal" if refused else "truncated" if truncated else "empty_final" if finish == "completed" and not text.strip() else "completed" if finish == "completed" else "response_error"
                except (ValueError, TypeError, AttributeError):
                    terminal = "response_error"
        write_new(output / response_name, raw)
        final_bytes = text.encode("utf-8")
        write_new(output / final_name, final_bytes)
        record = {k: receipt[k] for k in ("task_id", "case_id", "protocol_id", "run_id", "model", "payload_sha256")}
        record.update(request_path=request_name, request_sha256=sha(request_bytes), response_path=response_name,
                      response_sha256=sha(raw), visible_final_path=final_name, visible_final_sha256=sha(final_bytes),
                      terminal_status=terminal, finish_status=finish, empty_final=not text.strip(), truncated=truncated,
                      refused=refused, http_status=status, latency_seconds=time.monotonic() - begin,
                      request_id=response_metadata.get("request_id"), response_id=response_id, usage=usage, attempted=True)
        write_new(output / (stem + ".status.json"), canonical(record) + b"\n")
        policy_error = stop_for_provider_error(status, raw, terminal)
        return index, record, policy_error

    stopped = False
    next_index = 0
    with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as pool:
        pending = {}
        while pending or (next_index < len(rows) and not stopped):
            while not stopped and next_index < len(rows) and len(pending) < workers:
                future = pool.submit(execute, next_index, rows[next_index])
                pending[future] = next_index
                next_index += 1
                calls[0] += 1
            done, _ = concurrent.futures.wait(pending, return_when=concurrent.futures.FIRST_COMPLETED)
            for future in done:
                pending.pop(future)
                index, record, policy_error = future.result()
                records[index] = record
                stopped = stopped or policy_error
    for index in range(next_index, len(rows)):
        row = rows[index]
        stem = f"case_{index:05d}"
        public_bytes = validate_payload(row["payload_without_private_safety_identifier"], manifest["model"])
        public_request = {"payload_without_private_safety_identifier": row["payload_without_private_safety_identifier"],
                          "private_safety_identifier_added": False, "actual_submitted_payload_sha256": None,
                          "payload_sha256": sha(public_bytes)}
        request_bytes = canonical(public_request) + b"\n"
        raw = canonical({"not_dispatched": "stopped_after_provider_policy_or_access_error", "attempt": 0}) + b"\n"
        record = {"task_id": row["task_id"], "case_id": row["case_id"], "protocol_id": manifest["protocol_id"],
                  "run_id": run_id, "model": manifest["model"], "payload_sha256": row["payload_sha256"],
                  "request_path": stem + ".request.json", "request_sha256": sha(request_bytes),
                  "response_path": stem + ".response.json", "response_sha256": sha(raw),
                  "visible_final_path": stem + ".final.txt", "visible_final_sha256": sha(b""),
                  "terminal_status": "not_dispatched", "finish_status": None, "empty_final": True,
                  "truncated": False, "refused": False, "http_status": None, "latency_seconds": 0, "request_id": None, "response_id": None, "usage": None, "attempted": False}
        write_new(output / record["request_path"], request_bytes)
        write_new(output / record["response_path"], raw)
        write_new(output / record["visible_final_path"], b"")
        write_new(output / (stem + ".status.json"), canonical(record) + b"\n")
        records[index] = record
    lock = {"schema_version": 1, "protocol_id": manifest["protocol_id"], "model": manifest["model"], "run_id": run_id,
            "case_count": len(rows), "started_at_pacific": started, "completed_at_pacific": now(),
            "scoring_performed": False, "mode": "dry_run_zero_network" if dry_run else "live",
            "new_inference_calls": 0 if dry_run else calls[0], "no_retries": True, "rows": records,
            "frozen_request_file_sha256": manifest["requests_sha256"], "frozen_protocol_sha256": manifest["frozen_protocol_sha256"],
            "frozen_roster_sha256": manifest["source_roster_sha256"], "dispatcher_sha256": manifest["dispatcher_sha256"],
            "stopped_after_provider_policy_or_access_error": stopped, "concurrency": workers}
    lock_bytes = canonical(lock) + b"\n"
    write_new(output / "predictions_lock.json", lock_bytes)
    write_new(output / "predictions_lock.sha256", (sha(lock_bytes) + "\n").encode())
    for path in output.iterdir():
        if path.is_file():
            path.chmod(0o444)
    return {"saved": sum(r["terminal_status"] != "not_dispatched" for r in records), "planned": len(rows), "not_dispatched": sum(r["terminal_status"] == "not_dispatched" for r in records), "transport_or_response_errors": sum(r["terminal_status"] in {"transport_error", "http_error", "response_error"} for r in records),
            "truncations": sum(r["truncated"] for r in records), "empty_finals": sum(r["empty_final"] for r in records),
            "refusals": sum(r["refused"] for r in records), "stopped_after_provider_policy_or_access_error": stopped, "predictions_lock_sha256": sha(lock_bytes), "new_inference_calls": lock["new_inference_calls"]}


def worker(args):
    with os.fdopen(args.secret_fd, "rb") as secret_stream:
        secret_bytes = secret_stream.read(262145)
    if len(secret_bytes) > 262144:
        raise ValueError("Oversized runtime control message")
    secrets = parse_json(secret_bytes)
    abi = restrict_filesystem(args.bundle, args.output)
    try:
        Path(args.denial_probe).read_bytes()
    except PermissionError:
        denied = True
    else:
        raise RuntimeError("Filesystem isolation probe unexpectedly readable")
    manifest, rows = load_bundle(args.bundle, args.bundle_sha256)
    output = Path(args.output)
    write_new(output / "isolation_receipt.json", canonical({"mechanism": "Linux Landlock", "abi": abi,
              "repository_read_probe_denied": denied, "unrelated_files_denied_by_default": True,
              "mode": args.mode, "secret_fd_closed_before_isolation": True}) + b"\n")
    if args.mode in {"run", "run-development"}:
        check_execution_gates(secrets["authorization"], secrets.get("development_gate"), manifest, development=args.mode == "run-development")
        if secrets.get("verified_review_receipts") != {k: secrets["authorization"][k] for k in ("reviewed_input_receipt_sha256", "risk_review_receipt_sha256")}:
            raise ValueError("Missing parent-verified actual input/risk receipt hashes")
        if args.mode == "run" and secrets.get("verified_development_evidence_sha256") != secrets["development_gate"]["development_evidence_sha256"]:
            raise ValueError("Missing actual completed development evidence verification")
        key, identifier = secrets["api_key"], secrets["safety_identifier"]
        transport = lambda body: live_transport(body, key)
    else:
        identifier = "synthetic-dry-run-identifier"
        def transport(body):
            value = parse_json(body)
            return 200, canonical({"model": value["model"], "status": "completed", "output": [
                {"type": "message", "role": "assistant", "content": [{"type": "output_text", "text": "[ANSWER]A[/ANSWER]"}]}]})
    return run_cases(manifest, rows, output, args.run_id, identifier, transport, dry_run=args.mode == "dry-run", workers=args.workers)


def launch(args):
    bundle = Path(args.bundle).resolve()
    manifest, _ = load_bundle(bundle, args.bundle_sha256)
    secrets = {}
    if args.command in {"run", "run-development"}:
        if not all((args.authorization, args.authorization_sha256)) or (args.command == "run" and not all((args.development_gate, args.development_gate_sha256))):
            raise ValueError("Pinned authorization and reviewed development gate are required")
        auth = parse_json(read_pinned(args.authorization, args.authorization_sha256))
        gate = parse_json(read_pinned(args.development_gate, args.development_gate_sha256)) if args.command == "run" else None
        check_execution_gates(auth, gate, manifest, development=args.command == "run-development")
        verified_reviews = verify_review_receipts(auth, manifest, args.reviewed_input_receipt, args.risk_review_receipt)
        verified_development = verify_development_evidence(gate, manifest, args.development_evidence) if args.command == "run" else None
        # Only now, after every gate, may the runtime inspect private identity.
        identity_path = Path.home() / ".config/openai/request_identity.json"
        identity = parse_json(identity_path.read_bytes())
        identifier = identity.get("safety_identifier")
        if identity.get("schema_version") != 1 or re.fullmatch(r"[A-Za-z0-9_-]{1,128}", identifier or "") is None:
            raise ValueError("Existing stable safety identifier is not configured")
        key = os.environ.get("OPENAI_API_KEY")
        if not key:
            raise ValueError("OPENAI_API_KEY must be supplied privately at runtime")
        secrets = {"api_key": key, "safety_identifier": identifier, "authorization": auth, "development_gate": gate, "verified_review_receipts": verified_reviews, "verified_development_evidence_sha256": verified_development}
    output = Path(args.output).resolve()
    if output == bundle or bundle in output.parents or output in bundle.parents:
        raise ValueError("Output must be separate from the immutable bundle")
    output.mkdir(mode=0o700, parents=False, exist_ok=False)
    # Probe outside all allowed trees; verifies actual repository denial after
    # the OS restriction, rather than merely promising not to open references.
    probe = output.parent / (".comparison-denial-probe-" + str(os.getpid()))
    write_new(probe, b"synthetic outside-bundle probe; no biological data\n")
    read_fd, write_fd = os.pipe()
    secret_bytes = canonical(secrets)
    if len(secret_bytes) > 4096:
        os.close(read_fd)
        os.close(write_fd)
        raise ValueError("Runtime authorization/control message exceeds private pipe limit")
    os.write(write_fd, secret_bytes)
    os.close(write_fd)
    run_id = args.run_id or manifest["protocol_id"] + "_" + args.command
    try:
        command = [sys.executable, "-I", "-B", str(bundle / "dispatcher.py"), "_worker", "--bundle", str(bundle),
                   "--bundle-sha256", args.bundle_sha256, "--output", str(output), "--run-id", run_id,
                   "--mode", args.command, "--secret-fd", str(read_fd), "--denial-probe", str(probe), "--workers", str(args.workers)]
        child = subprocess.run(command, cwd=bundle, env={"PATH": "/usr/bin:/bin", "LANG": "C.UTF-8", "HOME": "/nonexistent"},
                               pass_fds=(read_fd,), close_fds=True, capture_output=True, text=True)
    finally:
        os.close(read_fd)
        probe.unlink()
    if child.returncode:
        raise RuntimeError("Isolated worker failed: " + child.stderr[-1500:])
    return parse_json(child.stdout)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    commands = parser.add_subparsers(dest="command", required=True)
    prep = commands.add_parser("prepare")
    for field in ("requests", "requests-sha256", "roster", "roster-sha256", "protocol", "protocol-sha256", "protocol-id", "model", "bundle"):
        prep.add_argument("--" + field, required=True)
    for name in ("dry-run", "run", "run-development", "_worker"):
        sub = commands.add_parser(name)
        for field in ("bundle", "bundle-sha256", "output"):
            sub.add_argument("--" + field, required=True)
        sub.add_argument("--run-id")
        sub.add_argument("--workers", type=int, default=4, choices=range(1, 9))
        if name in {"run", "run-development"}:
            for field in ("authorization", "authorization-sha256", "development-gate", "development-gate-sha256", "reviewed-input-receipt", "risk-review-receipt", "development-evidence"):
                sub.add_argument("--" + field)
        if name == "_worker":
            sub.add_argument("--mode", choices=("run", "run-development", "dry-run"), required=True)
            sub.add_argument("--secret-fd", type=int, required=True)
            sub.add_argument("--denial-probe", required=True)
    args = parser.parse_args(argv)
    if args.command == "prepare":
        result = prepare_bundle(args)
    elif args.command == "_worker":
        result = worker(args)
    else:
        result = launch(args)
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
