#!/usr/bin/env python3
"""Measure synthetic prompt lengths on an exclusive already-running replica.

No scheduler submission, GPU allocation, model download or production config
mutation occurs here. The caller coordinates resources and server ownership.
"""

from __future__ import annotations

import argparse
from datetime import datetime
import hashlib
import importlib.util
import json
from pathlib import Path
import random
import threading
import time
from zoneinfo import ZoneInfo


def load_client(path):
    spec = importlib.util.spec_from_file_location("length_benchmark_client", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def now():
    return datetime.now(ZoneInfo("America/Los_Angeles")).isoformat()


def parse_metrics(raw):
    values = {"kv_fraction": [], "preemptions": [], "running": [], "waiting": []}
    names = {"vllm:kv_cache_usage_perc": "kv_fraction", "vllm:gpu_cache_usage_perc": "kv_fraction", "vllm:num_preemptions_total": "preemptions", "vllm:num_requests_running": "running", "vllm:num_requests_waiting": "waiting"}
    for line in raw.splitlines():
        if not line or line.startswith("#"):
            continue
        try:
            metric, value = line.rsplit(None, 1)
            key = names.get(metric.split("{", 1)[0])
            if key:
                values[key].append(float(value))
        except ValueError:
            continue
    return {key: (max(items) if key == "kv_fraction" else sum(items)) if items else None for key, items in values.items()}


def fetch_metrics(client):
    with client.opener.open(client.base_url + "/metrics", timeout=10) as response:
        return parse_metrics(response.read().decode("utf-8"))


def make_synthetic_workload(client, model, count, input_tokens, seed):
    """Tokenize bounded chunks, avoiding huge untruncated tokenizer requests."""
    prefix = client.request("/tokenize", {"model": model, "prompt": "Synthetic serving performance test. Continue with arbitrary neutral text.\n", "add_special_tokens": False})["tokens"]
    if len(prefix) >= input_tokens:
        raise ValueError("Requested synthetic length is too short for its neutral prefix")
    generator = random.Random(seed)
    pool, stride = [], 64
    required = input_tokens - len(prefix) + (count - 1) * stride
    while len(pool) < required:
        fragments = ["".join(generator.choices("abcdefghjkmnpqrstuvwxyz23456789", k=10)) for _ in range(1024)]
        tokens = client.request("/tokenize", {"model": model, "prompt": " ".join(fragments), "add_special_tokens": False}).get("tokens")
        if not isinstance(tokens, list) or not tokens or not all(isinstance(token, int) for token in tokens):
            raise ValueError("Tokenizer did not return a nonempty list of token IDs")
        pool.extend(tokens)
    prompts = [{"index": index, "prompt_token_ids": prefix + pool[index * stride:index * stride + input_tokens - len(prefix)]} for index in range(count)]
    return {"synthetic_only": True, "seed": seed, "input_tokens_per_request": input_tokens, "construction": "Bounded random-fragment tokenization, common neutral prefix, deterministic distinct 64-token-offset windows; all exact IDs preserved.", "requests": prompts}


class MetricsSampler:
    def __init__(self, client, path, interval):
        self.client, self.path, self.interval = client, path, interval
        self.samples = []
        self.stop_event = threading.Event()
        self.thread = threading.Thread(target=self.run, daemon=True)

    def sample(self):
        try:
            value = {"captured_at": now(), **fetch_metrics(self.client)}
        except Exception as error:
            value = {"captured_at": now(), "error": f"{type(error).__name__}: {error}"}
        self.samples.append(value)
        with self.path.open("a") as output:
            output.write(json.dumps(value, sort_keys=True) + "\n")

    def run(self):
        while not self.stop_event.is_set():
            self.sample()
            self.stop_event.wait(self.interval)

    def start(self):
        self.thread.start()

    def finish(self):
        self.stop_event.set()
        self.thread.join(timeout=15)
        self.sample()
        peaks = [row["kv_fraction"] for row in self.samples if row.get("kv_fraction") is not None]
        preemptions = [row["preemptions"] for row in self.samples if row.get("preemptions") is not None]
        return {"sample_count": len(self.samples), "usable_kv_samples": len(peaks), "sampled_peak_kv_fraction": max(peaks) if peaks else None, "preemptions_before": preemptions[0] if preemptions else None, "preemptions_after": preemptions[-1] if preemptions else None, "preemption_delta": preemptions[-1] - preemptions[0] if len(preemptions) >= 2 and preemptions[-1] >= preemptions[0] else None, "sample_file": str(self.path), "measurement": "Sampled live KV gauge; short peaks between samples may be missed."}


def next_projection(previous, concurrency, plan):
    if previous is None:
        return {"admit": concurrency == min(plan["concurrencies"]), "projected_peak_kv_fraction": None, "reason": "initial smallest-concurrency pilot"}
    peak = previous.get("sampled_peak_kv_fraction")
    if not previous.get("eligible") or peak is None:
        return {"admit": False, "projected_peak_kv_fraction": None, "reason": "previous point failed exact-workload, preemption or live-KV checks"}
    projected = peak * concurrency / previous["concurrency"] * plan["projection_safety_multiplier"]
    return {"admit": projected <= plan["maximum_measured_kv_fraction"], "projected_peak_kv_fraction": projected, "reason": "projected from the last measured point, with the declared safety multiplier"}


def validate_plan(plan):
    if plan.get("synthetic_only") is not True:
        raise ValueError("Synthetic-only plan is required")
    if plan["concurrencies"] != sorted(set(plan["concurrencies"])) or min(plan["concurrencies"]) < 1:
        raise ValueError("Concurrencies must be unique and ascending")
    if min(plan["input_tokens"]) < 1 or plan["output_tokens"] < 1:
        raise ValueError("Positive input and output lengths are required")
    if max(plan["input_tokens"]) + plan["output_tokens"] > plan["required_server"]["max_model_len"]:
        raise ValueError("Prompt plus output would exceed the required context limit")
    if max(plan["concurrencies"]) > plan["required_server"]["max_num_seqs"]:
        raise ValueError("Client load exceeds the declared server sequence capacity")
    if not 0 < plan["maximum_measured_kv_fraction"] < 1 or plan["projection_safety_multiplier"] < 1:
        raise ValueError("A positive KV headroom and conservative projection multiplier are required")


def benchmark(args):
    plan = json.loads(args.plan.read_text())
    if args.profile is not None:
        if args.profile not in plan["input_tokens"]:
            raise ValueError("--profile must select an input length from the frozen plan")
        plan["input_tokens"] = [args.profile]
    validate_plan(plan)
    if args.validate_plan:
        print(json.dumps({"plan_valid": True, "lengths": plan["input_tokens"], "candidate_concurrencies": plan["concurrencies"], "maximum_requests_if_all_admitted": len(plan["input_tokens"]) * sum(plan["concurrencies"]), "maximum_forced_output_tokens_if_all_admitted": len(plan["input_tokens"]) * sum(plan["concurrencies"]) * plan["output_tokens"]}, indent=2))
        return
    if not args.base_url or not args.output_dir:
        raise ValueError("--base-url and --output-dir are required for actual measurements")
    output = args.output_dir.resolve()
    output.mkdir(parents=True, exist_ok=True)
    if any(output.iterdir()):
        raise ValueError("Output directory must be empty")
    harness = load_client(args.client_path)
    write = harness.write_json
    client = harness.Client(args.base_url, plan["request_timeout_seconds"])
    write(output / "plan.json", plan)
    provenance = {"created_at": now(), "plan_sha256": hashlib.sha256(args.plan.read_bytes()).hexdigest(), "client_sha256": hashlib.sha256(args.client_path.read_bytes()).hexdigest(), "launcher_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(), "base_url": client.base_url, "sampling": plan["generation"], "synthetic_only": True}
    write(output / "provenance.json", provenance)
    state = {"state": "preflight", "updated_at": now(), "rows": []}
    write(output / "progress.json", state)
    try:
        idle = fetch_metrics(client)
        write(output / "preflight_metrics.json", idle)
        if idle["running"] is None or idle["waiting"] is None or idle["running"] != 0 or idle["waiting"] != 0:
            raise ValueError("An idle exclusive server with request-queue metrics is required")
        write(output / "server_models.json", client.request("/v1/models"))
        harness.reset_prefix_cache(client, output / "prefix_cache_preflight.json")
        workload = make_synthetic_workload(client, plan["model"], max(plan["concurrencies"]), max(plan["input_tokens"]), plan["workload_seed"])
        write(output / "synthetic_workload.json", workload)
        generation = plan["generation"]
        sampling = {"temperature": generation["temperature"], "top_p": generation["top_p"], "top_k": generation["top_k"], "seed": generation["seed"], "ignore_eos": True, "stream": False}
        rows = []
        for input_tokens in plan["input_tokens"]:
            length_directory = output / f"input_{input_tokens:06d}"
            length_directory.mkdir()
            payloads = [{"model": plan["model"], "prompt": row["prompt_token_ids"][:input_tokens], "max_tokens": plan["output_tokens"], **sampling} for row in workload["requests"]]
            stage_progress = {"completed_stages": []}
            warmups = [dict(payload, max_tokens=plan["warmup_output_tokens"]) for payload in payloads[:plan["warmup_requests"]]]
            warmup = harness.run_stage(client, "warmup", min(plan["concurrencies"]), warmups, length_directory, input_tokens, plan["warmup_output_tokens"], stage_progress, "reset-between-levels")
            if not warmup["comparable_fixed_workload"]:
                raise RuntimeError("Warmup failed; exact artifacts retained")
            previous = None
            blocked = False
            for concurrency in plan["concurrencies"]:
                admission = next_projection(previous, concurrency, plan)
                row = {"input_tokens": input_tokens, "output_tokens": plan["output_tokens"], "concurrency": concurrency, "planned_requests": concurrency, "projection": admission}
                if blocked or not admission["admit"]:
                    row.update(state="skipped_unmeasured", eligible=False, reason="A lower point exhausted declared KV headroom or failed checks" if blocked else admission["reason"])
                    rows.append(row)
                    blocked = True
                    continue
                state.update(state="measuring", input_tokens=input_tokens, concurrency=concurrency, updated_at=now(), rows=rows)
                write(output / "progress.json", state)
                sampler = MetricsSampler(client, length_directory / f"concurrency_{concurrency:03d}_live_metrics.jsonl", plan["metrics_interval_seconds"])
                sampler.start()
                try:
                    measured = harness.run_stage(client, f"concurrency_{concurrency:03d}", concurrency, payloads[:concurrency], length_directory, input_tokens, plan["output_tokens"], stage_progress, "reset-between-levels")
                finally:
                    monitored = sampler.finish()
                peak = monitored["sampled_peak_kv_fraction"]
                eligible = measured["comparable_fixed_workload"] and measured["failed_requests"] == 0 and monitored["preemption_delta"] == 0 and monitored["usable_kv_samples"] >= 2 and peak is not None and 0 < peak <= plan["maximum_measured_kv_fraction"]
                row.update(state="measured", measured=measured, monitoring=monitored, sampled_peak_kv_fraction=peak, eligible=eligible)
                rows.append(row)
                previous = row
                if not measured["comparable_fixed_workload"] or measured["failed_requests"]:
                    raise RuntimeError("Exact-workload or transport failure; no retry or discarded output")
                write(output / "results.json", {"plan": plan, "provenance": provenance, "rows": rows, "updated_at": now()})
                if not eligible:
                    blocked = True
            write(output / "results.json", {"plan": plan, "provenance": provenance, "rows": rows, "updated_at": now()})
        selected = []
        for input_tokens in plan["input_tokens"]:
            candidates = [row for row in rows if row["input_tokens"] == input_tokens and row["eligible"]]
            best = max(candidates, key=lambda row: row["measured"]["output_tokens_per_second"]) if candidates else None
            selected.append({"tested_input_tokens": input_tokens, "tested_output_tokens": plan["output_tokens"], "best_tested_concurrency": best["concurrency"] if best else None, "output_tokens_per_second": best["measured"]["output_tokens_per_second"] if best else None, "sampled_peak_kv_fraction": best["sampled_peak_kv_fraction"] if best else None})
        write(output / "measured_concurrency_by_input_length.json", {"points": selected, "provenance": provenance, "restriction": "Measured synthetic points on this server; no production configuration was changed and no robust optimum or other hardware/workload result is claimed."})
        state.update(state="completed", updated_at=now(), rows=rows)
        write(output / "progress.json", state)
        print(json.dumps(selected, indent=2), flush=True)
    except BaseException as error:
        state.update(state="failed", error=f"{type(error).__name__}: {error}", updated_at=now())
        write(output / "progress.json", state)
        raise


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--plan", type=Path, required=True)
    parser.add_argument("--base-url")
    parser.add_argument("--profile", type=int, help="Measure just this input-token length from the frozen plan")
    parser.add_argument("--output-dir", type=Path)
    parser.add_argument("--client-path", type=Path, default=Path(__file__).with_name("benchmark_vllm_concurrency.py"))
    parser.add_argument("--validate-plan", action="store_true")
    benchmark(parser.parse_args())


if __name__ == "__main__":
    main()
