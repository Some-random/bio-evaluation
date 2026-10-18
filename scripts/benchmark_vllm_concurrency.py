#!/usr/bin/env python3
"""Measure a dedicated local vLLM replica using fixed synthetic token workloads.

This is a serving benchmark, not a biological evaluation. It sends only generated
synthetic text to a loopback server; it never reads benchmark examples or labels.
Retain production prefix caching and reset it between paired comparison stages.
"""

from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime
import hashlib
import ipaddress
import json
import math
from pathlib import Path
import random
import statistics
import sys
import time
from urllib.error import HTTPError, URLError
from urllib.parse import urlsplit
from urllib.request import ProxyHandler, Request, build_opener
from zoneinfo import ZoneInfo


def now() -> str:
    return datetime.now(ZoneInfo("America/Los_Angeles")).isoformat()


def write_json(path: Path, value) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name + ".tmp")
    temporary.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n")
    temporary.replace(path)


def canonical_hash(value) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def percentile(values: list[float], quantile: float):
    """Linearly interpolated percentile, including the one-observation case."""
    if not values:
        return None
    ordered = sorted(values)
    position = (len(ordered) - 1) * quantile
    low, high = math.floor(position), math.ceil(position)
    return ordered[low] + (ordered[high] - ordered[low]) * (position - low)


def validate_base_url(value: str) -> str:
    parsed = urlsplit(value)
    try:
        loopback = parsed.hostname == "localhost" or ipaddress.ip_address(parsed.hostname or "").is_loopback
    except ValueError:
        loopback = False
    if parsed.scheme != "http" or not loopback or parsed.username or parsed.password or parsed.query or parsed.fragment:
        raise ValueError("base URL must be a credential-free HTTP loopback endpoint")
    if parsed.path.rstrip("/") not in ("", "/v1"):
        raise ValueError("base URL path must be empty or /v1")
    return value.rstrip("/").removesuffix("/v1")


class Client:
    def __init__(self, base_url: str, timeout: float):
        self.base_url = validate_base_url(base_url)
        self.timeout = timeout
        # A synthetic local serving benchmark must never follow environment
        # proxy settings and route request bodies outside the machine.
        self.opener = build_opener(ProxyHandler({}))

    def request(self, path: str, payload=None, method=None):
        request = Request(
            self.base_url + path,
            data=None if payload is None else json.dumps(payload).encode(),
            headers={"Content-Type": "application/json"},
            method=method or ("GET" if payload is None else "POST"),
        )
        with self.opener.open(request, timeout=self.timeout) as response:
            raw = response.read().decode("utf-8")
            return json.loads(raw) if raw.strip() else {"http_status": response.status}

    def snapshot_metrics(self, path: Path) -> dict:
        try:
            with self.opener.open(self.base_url + "/metrics", timeout=min(self.timeout, 20)) as response:
                raw = response.read().decode("utf-8")
            path.write_text(raw)
            # Keep all raw metrics; surface counters/gauges relevant to saturation.
            selected = {}
            needles = ("preempt", "cache_usage", "num_requests_running", "num_requests_waiting", "generation_tokens", "prompt_tokens", "prefix_cache")
            for line in raw.splitlines():
                if not line or line.startswith("#") or not any(part in line for part in needles):
                    continue
                try:
                    metric, value = line.rsplit(None, 1)
                    selected[metric] = float(value)
                except (ValueError, TypeError):
                    continue
            return {"captured_at": now(), "path": str(path), "selected": selected}
        except Exception as error:
            return {"captured_at": now(), "error": f"{type(error).__name__}: {error}"}


def reset_prefix_cache(client: Client, path: Path):
    response = client.request("/reset_prefix_cache", method="POST")
    write_json(path, {"captured_at": now(), "response": response})
    if response is False or isinstance(response, dict) and response.get("error"):
        raise RuntimeError("Dedicated server refused to reset its prefix cache")
    return response


def make_workload(client: Client, model: str, count: int, input_tokens: int, seed: int) -> dict:
    prompts = []
    # Deliberately neutral, meaningless fragments, rather than biological examples.
    # The exact token IDs are reused across all levels; /tokenize runs untimed.
    for index in range(count):
        generator = random.Random(seed + index)
        fragments = ["".join(generator.choices("abcdefghjkmnpqrstuvwxyz23456789", k=10)) for _ in range(input_tokens)]
        text = "Synthetic serving performance test. Continue with arbitrary neutral text.\n" + " ".join(fragments)
        tokenized = client.request("/tokenize", {"model": model, "prompt": text, "add_special_tokens": False})
        tokens = tokenized.get("tokens")
        if not isinstance(tokens, list) or len(tokens) < input_tokens or not all(isinstance(token, int) for token in tokens):
            raise RuntimeError(f"/tokenize did not return at least {input_tokens} token IDs for request {index}")
        prompts.append({"index": index, "prompt_token_ids": tokens[:input_tokens]})
    return {"synthetic_only": True, "seed": seed, "input_tokens_per_request": input_tokens, "requests": prompts}


def run_request(client: Client, payload: dict, request_index: int, directory: Path) -> dict:
    record = {"request_index": request_index, "started_at": now(), "request_sha256": canonical_hash(payload)}
    started = time.perf_counter()
    try:
        response = client.request("/v1/completions", payload)
        record["response"] = response
        usage = response.get("usage") or {}
        choices = response.get("choices") or []
        record.update({
            "success": not response.get("error") and bool(choices) and isinstance(usage.get("completion_tokens"), int),
            "prompt_tokens": usage.get("prompt_tokens"),
            "completion_tokens": usage.get("completion_tokens"),
            "finish_reasons": [choice.get("finish_reason") for choice in choices],
        })
        if not record["success"]:
            record["error"] = "Missing choices or completion usage, or API error in response"
    except HTTPError as error:
        record.update({"success": False, "http_status": error.code, "error": str(error), "response_body": error.read().decode("utf-8", errors="replace")})
    except (URLError, TimeoutError, OSError, ValueError) as error:
        record.update({"success": False, "error": f"{type(error).__name__}: {error}"})
    except Exception as error:
        record.update({"success": False, "error": f"{type(error).__name__}: {error}"})
    record.update({"elapsed_seconds": time.perf_counter() - started, "finished_at": now()})
    write_json(directory / f"response_{request_index:05d}.json", record)
    return record


def sampling_settings(args) -> dict:
    settings = {"temperature": args.temperature, "seed": args.generation_seed if args.generation_seed is not None else args.seed, "ignore_eos": True, "max_tokens": args.output_tokens}
    if args.top_p is not None:
        settings["top_p"] = args.top_p
    if args.top_k is not None:
        settings["top_k"] = args.top_k
    return settings


def summarize(records: list[dict], elapsed_seconds: float, input_tokens: int, output_tokens: int) -> dict:
    successful = [record for record in records if record.get("success")]
    latencies = [record["elapsed_seconds"] for record in successful]
    completion_count = sum(record["completion_tokens"] for record in successful)
    prompt_count = sum(record.get("prompt_tokens") or 0 for record in successful)
    mismatch = sum(record.get("prompt_tokens") != input_tokens or record["completion_tokens"] != output_tokens for record in successful)
    return {
        "completed_requests": len(records), "successful_requests": len(successful),
        "failed_requests": len(records) - len(successful),
        "fixed_workload_mismatch_requests": mismatch,
        "elapsed_seconds": elapsed_seconds,
        "requests_per_second": len(successful) / elapsed_seconds if elapsed_seconds > 0 else None,
        "output_tokens_per_second": completion_count / elapsed_seconds if elapsed_seconds > 0 else None,
        "input_tokens_per_second": prompt_count / elapsed_seconds if elapsed_seconds > 0 else None,
        "actual_prompt_tokens": prompt_count, "actual_completion_tokens": completion_count,
        "latency_seconds": {"p50": percentile(latencies, .5), "p95": percentile(latencies, .95), "mean": statistics.mean(latencies) if latencies else None, "max": max(latencies) if latencies else None},
        "comparable_fixed_workload": len(successful) == len(records) and len(records) > 0 and mismatch == 0,
        "latency_definition": "request dispatch to complete nonstreamed response; excludes client queue time",
        "throughput_definition": "successful requests or their actual usage tokens divided by entire stage wall time, including failed requests",
    }


def run_stage(client: Client, stage: str, concurrency: int, payloads: list[dict], output_dir: Path, input_tokens: int, output_tokens: int, progress: dict, prefix_cache_policy: str) -> dict:
    directory = output_dir / stage
    directory.mkdir(parents=True, exist_ok=False)
    for index, payload in enumerate(payloads):
        write_json(directory / f"request_{index:05d}.json", payload)
    cache_reset = None
    if prefix_cache_policy == "reset-between-levels":
        cache_reset = reset_prefix_cache(client, directory / "prefix_cache_reset.json")
    metrics_before = client.snapshot_metrics(directory / "metrics_before.prom")
    progress.pop("stage_partial_summary", None)
    progress.update({"state": "running", "stage": stage, "concurrency": concurrency, "completed_requests": 0, "updated_at": now()})
    write_json(output_dir / "progress.json", progress)
    records = []
    started = time.perf_counter()
    with ThreadPoolExecutor(max_workers=concurrency) as executor:
        futures = [executor.submit(run_request, client, payload, index, directory) for index, payload in enumerate(payloads)]
        for future in as_completed(futures):
            records.append(future.result())
            partial = summarize(records, time.perf_counter() - started, input_tokens, output_tokens)
            progress.update({"completed_requests": len(records), "stage_partial_summary": partial, "updated_at": now()})
            write_json(output_dir / "progress.json", progress)
    elapsed = time.perf_counter() - started
    summary = summarize(records, elapsed, input_tokens, output_tokens)
    summary.update({"stage": stage, "concurrency": concurrency, "planned_requests": len(payloads), "finished_at": now(), "prefix_cache_policy": prefix_cache_policy, "prefix_cache_reset": cache_reset, "prefix_cache_controlled": prefix_cache_policy != "uncontrolled", "metrics_before": metrics_before, "metrics_after": client.snapshot_metrics(directory / "metrics_after.prom")})
    write_json(directory / "summary.json", summary)
    print(json.dumps({key: summary[key] for key in ("stage", "concurrency", "successful_requests", "failed_requests", "output_tokens_per_second", "requests_per_second", "latency_seconds", "comparable_fixed_workload")}), flush=True)
    return summary


def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base-url", required=True)
    parser.add_argument("--model", required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--concurrencies", default="4,8,16,32")
    parser.add_argument("--requests", type=int, default=32)
    parser.add_argument("--input-tokens", type=int, default=2048)
    parser.add_argument("--output-tokens", type=int, default=512)
    parser.add_argument("--warmup-requests", type=int, default=4)
    parser.add_argument("--warmup-output-tokens", type=int, default=64, help="Separate, unmeasured decode length for warmup")
    parser.add_argument("--repeats", type=int, default=1)
    parser.add_argument("--seed", type=int, default=20261017)
    parser.add_argument("--generation-seed", type=int, help="Optional sampling seed independent of the synthetic workload seed")
    parser.add_argument("--temperature", type=float, default=0)
    parser.add_argument("--top-p", type=float)
    parser.add_argument("--top-k", type=int)
    parser.add_argument("--request-timeout", type=float, default=3600)
    parser.add_argument("--prefix-cache-policy", choices=("reset-between-levels", "disabled", "uncontrolled"), default="reset-between-levels", help="Reset enabled production cache before every warmup/measurement stage, or explicitly declare disabled/uncontrolled caching")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    levels = [int(value) for value in args.concurrencies.split(",")]
    if not levels or len(levels) != len(set(levels)) or min(levels) < 1 or min(args.requests, args.input_tokens, args.output_tokens, args.warmup_output_tokens, args.repeats) < 1 or args.warmup_requests < 0:
        raise ValueError("All workload dimensions and concurrency levels must be positive")
    if args.requests < max(levels):
        raise ValueError("--requests must be at least the largest concurrency level")
    if args.temperature < 0 or args.top_p is not None and not 0 < args.top_p <= 1 or args.top_k is not None and args.top_k != -1 and args.top_k < 1:
        raise ValueError("Invalid temperature, top-p or top-k sampling setting")
    output_dir = args.output_dir.resolve()
    output_dir.mkdir(parents=True, exist_ok=True)
    if any(output_dir.iterdir()):
        raise ValueError("Output directory must be empty, to avoid overwriting prior measurement records")
    client = Client(args.base_url, args.request_timeout)
    config = {key: str(value) if isinstance(value, Path) else value for key, value in vars(args).items()}
    sampling = sampling_settings(args)
    config.update({"created_at": now(), "synthetic_only": True, "concurrency_levels": levels, "sampling": sampling, "prefix_cache_policy_is_operator_declaration": args.prefix_cache_policy != "reset-between-levels", "protocol": "Exact token-ID prompts reused across levels; fixed forced decode length; no benchmark records read; one request attempt, no retries; nonstreaming completion API; saturation with immediate worker replenishment.", "time_zone": "America/Los_Angeles"})
    write_json(output_dir / "config.json", config)
    progress = {"state": "preparing_synthetic_workload", "updated_at": now(), "completed_stages": []}
    write_json(output_dir / "progress.json", progress)
    try:
        models = client.request("/v1/models")
        write_json(output_dir / "server_models.json", models)
        if args.prefix_cache_policy == "reset-between-levels":
            # Verify the operator enabled vLLM's gated development endpoint
            # before preparing all tokenized requests or performing warmup.
            reset_prefix_cache(client, output_dir / "prefix_cache_preflight.json")
        workload = make_workload(client, args.model, max(args.requests, args.warmup_requests), args.input_tokens, args.seed)
        write_json(output_dir / "workload.json", workload)
        payloads = [{"model": args.model, "prompt": row["prompt_token_ids"], **sampling, "stream": False} for row in workload["requests"]]
        config["workload_sha256"] = canonical_hash(workload)
        write_json(output_dir / "config.json", config)
        if args.warmup_requests:
            warmup_payloads = [dict(payload, max_tokens=args.warmup_output_tokens) for payload in payloads[:args.warmup_requests]]
            warmup = run_stage(client, "warmup", min(max(levels), args.warmup_requests), warmup_payloads, output_dir, args.input_tokens, args.warmup_output_tokens, progress, args.prefix_cache_policy)
            if warmup["failed_requests"] or not warmup["comparable_fixed_workload"]:
                raise RuntimeError("Warmup failed or the server did not honor the exact token workload; see saved responses")
        results = []
        for repeat in range(args.repeats):
            # Reversing alternate sweeps reduces a simple monotonic time-order bias.
            order = levels if repeat % 2 == 0 else list(reversed(levels))
            for concurrency in order:
                stage = f"repeat_{repeat + 1:02d}_concurrency_{concurrency:03d}"
                result = run_stage(client, stage, concurrency, payloads[:args.requests], output_dir, args.input_tokens, args.output_tokens, progress, args.prefix_cache_policy)
                results.append(result)
                progress["completed_stages"].append(stage)
                write_json(output_dir / "results.json", {"config": config, "stages": results, "finished_at": now()})
                if result["failed_requests"] or not result["comparable_fixed_workload"]:
                    raise RuntimeError("Measurement stage failed or violated fixed workload; stopping sweep without retrying or discarding records")
        progress.update({"state": "completed", "updated_at": now()})
        write_json(output_dir / "progress.json", progress)
        return 0
    except BaseException as error:
        progress.update({"state": "interrupted" if isinstance(error, KeyboardInterrupt) else "failed", "error": f"{type(error).__name__}: {error}", "updated_at": now()})
        write_json(output_dir / "progress.json", progress)
        raise


if __name__ == "__main__":
    sys.exit(main())
