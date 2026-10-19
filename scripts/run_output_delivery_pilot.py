"""Fixed synthetic delivery checks; no benchmark cases, oracles or test labels."""
from __future__ import annotations

import argparse
from datetime import datetime
import hashlib
import importlib.util
import json
from pathlib import Path
import re
import time
import urllib.request
from zoneinfo import ZoneInfo


ROOT = Path(__file__).resolve().parents[1]
MODEL = "Qwen/Qwen3.8-27B"
REVISION = "1d4bf0f2ff6012fd82039f2fa52739d0dd7c60c0"
GENERATION = {"max_tokens": 16384, "temperature": 1.0, "top_p": .95,
    "top_k": 20, "seed": 42, "n": 1,
    "chat_template_kwargs": {"enable_thinking": True, "reasoning_effort": "medium"}}
EXERCISES = {
    "scalar": "Compute the arithmetic mean of 0.2 and 0.8. Return only one finite decimal number.",
    "binary": "Apply this toy rule: label YES when x is positive, otherwise NO. x=3. Return only YES or NO.",
    "choice": "Which equals 2+2? A:3; B:4; C:5; D:6. Return only [ANSWER]B[/ANSWER] if B is your choice, using that answer-tag format.",
    "class_index": "A toy class set has integer IDs 0 through 383. Select the ID equal to 40 minus 3. Return only the integer ID.",
    "confidence": 'Return only a JSON object assigning probability 0.75 to class T:0001 and 0.25 to class T:0002. Both keys must appear, and no other keys.',
    "protein": 'This is a toy string-editing task, not functional protein design. Start with ACDEFGHIKL and replace the last character L with M. Return only a JSON object with one string field called protein.',
}


def stamp():
    return datetime.now(ZoneInfo("America/Los_Angeles")).isoformat()


def sha(data):
    return hashlib.sha256(data).hexdigest()


def encode(value):
    return (json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2) + "\n").encode()


def atomic(path, value):
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_bytes(encode(value))
    temporary.replace(path)


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError("Duplicate key")
        result[key] = value
    return result


def check(kind, final, reasoning, finish, protein_contract):
    if finish != "stop" or not isinstance(final, str) or not final.strip():
        return False
    text = final.strip()
    try:
        if kind == "scalar":
            return re.fullmatch(r"[+-]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][+-]?\d+)?", text) is not None and float(text) == .5
        if kind == "binary":
            return text.lower() == "yes"
        if kind == "choice":
            return text == "[ANSWER]B[/ANSWER]"
        if kind == "class_index":
            return re.fullmatch(r"\d+", text) is not None and int(text) == 37
        if kind == "confidence":
            value = json.loads(text, object_pairs_hook=unique_object)
            return value == {"T:0001": .75, "T:0002": .25} and all(type(v) in (int, float) for v in value.values())
        if kind == "protein":
            value = protein_contract.parse_channels(final, reasoning)
            return value["valid_format"] and value["protein"] == "ACDEFGHIKM" and protein_contract.validate_endpoint("ACDEFGHIKL", value["protein"], "replace_only")["eligible"]
    except (ValueError, TypeError):
        return False
    return False


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--endpoint", default="http://127.0.0.1:8250/v1")
    parser.add_argument("--model-path", default="/dfs/scratch0/tchen/models/Qwen3.8-27B")
    parser.add_argument("--identity-file", type=Path, default=ROOT / ".local/shared_vllm_saturation_2026-10-18/existing_upgrade/saturation_replica_0/server_identity.json")
    parser.add_argument("--dedicated-server", action="store_true")
    args = parser.parse_args()
    if args.output.exists():
        raise ValueError("Pilot output already exists; no implicit retry or overwrite")
    from transformers import AutoTokenizer
    tokenizer = AutoTokenizer.from_pretrained(args.model_path, local_files_only=True)
    source = ROOT / "scripts/stride_gfp_qualified_contract.py"
    spec = importlib.util.spec_from_file_location("pilot_protein_contract", source)
    contract = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(contract)
    opener = urllib.request.build_opener(urllib.request.ProxyHandler({}))
    with opener.open(args.endpoint + "/models", timeout=15) as response:
        assert MODEL in {item["id"] for item in json.load(response)["data"]}
    cases = []
    for length, repetitions in [("short", 0), ("long", 3500)]:
        for kind, exercise in EXERCISES.items():
            padding = "Neutral archive record: placeholder data only.\n" * repetitions
            prompt = "Synthetic interface exercise. Ignore the neutral padding records and answer the final exercise.\n" + padding + "\nFinal exercise:\n" + exercise
            messages = [{"role": "user", "content": prompt}]
            tokens = tokenizer.apply_chat_template(messages, tokenize=True, add_generation_prompt=True, **GENERATION["chat_template_kwargs"])
            token_ids = tokens["input_ids"] if hasattr(tokens, "keys") else tokens
            if token_ids and isinstance(token_ids[0], list):
                assert len(token_ids) == 1
                token_ids = token_ids[0]
            if len(token_ids) + GENERATION["max_tokens"] > 65536:
                raise ValueError("Synthetic prompt plus output budget exceeds frozen server context")
            cases.append({"id": kind + "_" + length, "kind": kind, "prompt_tokens": len(token_ids),
                "payload": {"model": MODEL, "messages": messages, **GENERATION}})
    identity_path = args.identity_file
    identity_bytes = identity_path.read_bytes()
    identity = json.loads(identity_bytes)
    assert identity["model"] == MODEL and identity["revision"] == REVISION and identity["dtype"] == "bfloat16"
    args.output.mkdir(parents=True)
    (args.output / "requests").mkdir()
    (args.output / "responses").mkdir()
    plan = {"created_at_pacific": stamp(), "model": MODEL, "model_revision": REVISION,
        "generation": GENERATION, "endpoint": args.endpoint,
        "server_identity": identity, "server_identity_sha256": sha(identity_bytes),
        "runner_sha256": sha(Path(__file__).read_bytes()), "protein_contract_sha256": sha(source.read_bytes()),
        "acceptance": "All twelve normally stopped, nonempty final answers must satisfy their frozen toy contract. No post-output rule changes.",
        "interpretation": "Synthetic delivery checks only; no biological-quality or full-rerun-readiness claim. Real development-case validation is still needed.",
        "co_resident_requests": not args.dedicated_server,
        "new_gpus": 1 if args.dedicated_server else 0, "concurrency": 1, "cases": cases}
    (args.output / "plan.json").write_bytes(encode(plan))
    plan_sha = sha((args.output / "plan.json").read_bytes())
    outcomes = []
    for case in cases:
        request_bytes = encode(case["payload"])
        (args.output / "requests" / (case["id"] + ".json")).write_bytes(request_bytes)
        started = time.monotonic()
        try:
            request = urllib.request.Request(args.endpoint + "/chat/completions", data=request_bytes,
                headers={"Content-Type": "application/json"}, method="POST")
            with opener.open(request, timeout=900) as response:
                raw = response.read()
            (args.output / "responses" / (case["id"] + ".json")).write_bytes(raw)
            body = json.loads(raw)
            choice = body["choices"][0]
            message = choice["message"]
            reasoning = message.get("reasoning", message.get("reasoning_content"))
            final = message.get("content")
            outcome = {"case_id": case["id"], "prompt_tokens": case["prompt_tokens"],
                "usage": body.get("usage"), "finish_reason": choice.get("finish_reason"),
                "empty_final": not bool(final), "separate_reasoning_present": isinstance(reasoning, str),
                "passed": check(case["kind"], final, reasoning, choice.get("finish_reason"), contract),
                "response_sha256": sha(raw), "request_sha256": sha(request_bytes)}
        except Exception as exc:
            outcome = {"case_id": case["id"], "passed": False, "error_type": type(exc).__name__}
            outcomes.append(outcome)
            atomic(args.output / "progress.json", {"at_pacific": stamp(), "plan_sha256": plan_sha, "outcomes": outcomes, "stopped_after_error": True})
            raise  # Ambiguous calls are never silently retried.
        outcome["elapsed_seconds"] = round(time.monotonic() - started, 3)
        outcomes.append(outcome)
        atomic(args.output / "progress.json", {"at_pacific": stamp(), "plan_sha256": plan_sha, "outcomes": outcomes})
        print(json.dumps(outcome), flush=True)
    assert sha(identity_path.read_bytes()) == plan["server_identity_sha256"]
    atomic(args.output / "completion.json", {"at_pacific": stamp(), "plan_sha256": plan_sha,
        "planned": len(cases), "completed": len(outcomes), "passed": sum(o["passed"] for o in outcomes),
        "all_passed": all(o["passed"] for o in outcomes), "new_benchmark_generations": 0})


if __name__ == "__main__":
    main()
