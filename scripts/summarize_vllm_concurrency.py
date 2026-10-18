#!/usr/bin/env python3
"""Summarize dedicated synthetic vLLM measurements without reading eval data."""

from __future__ import annotations

import argparse
import csv
from datetime import datetime, timedelta
import hashlib
import json
from pathlib import Path
import statistics
from zoneinfo import ZoneInfo


PACIFIC = ZoneInfo("America/Los_Angeles")


def read_json(path: Path, default=None):
    return json.loads(path.read_text()) if path.is_file() else default


def parse_time(value):
    if not value:
        return None
    parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    return parsed.replace(tzinfo=PACIFIC) if parsed.tzinfo is None else parsed.astimezone(PACIFIC)


def digest(path: Path):
    return hashlib.sha256(path.read_bytes()).hexdigest() if path.is_file() else None


def preemption_count(path: Path):
    if not path.is_file():
        return None
    counters = []
    for line in path.read_text().splitlines():
        if not line or line.startswith("#"):
            continue
        metric, *tail = line.rsplit(None, 1)
        name = metric.split("{", 1)[0]
        if "preempt" in name and name.endswith("_total") and tail:
            try:
                counters.append(float(tail[0]))
            except ValueError:
                pass
    return sum(counters) if counters else None


def preemption_delta(directory: Path):
    before = preemption_count(directory / "metrics_before.prom")
    after = preemption_count(directory / "metrics_after.prom")
    delta = after - before if before is not None and after is not None and after >= before else None
    return {"before": before, "after": after, "delta": delta, "counter_reset_detected": before is not None and after is not None and after < before}


def gpu_uuids(directory: Path, capacity: int):
    identity = read_json(directory / f"server_capacity_{capacity}_gpu.json", [])
    if not isinstance(identity, list):
        return []
    uuids = sorted({row["gpu_uuid"] for row in identity if isinstance(row, dict) and row.get("gpu_uuid")})
    # Never infer the allocated GPU from a possibly full-node inventory.
    return uuids if len(uuids) == 1 else []


def numeric(value):
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def read_telemetry(path: Path):
    samples = []
    if not path.is_file():
        return samples
    for fields in csv.reader(path.read_text().splitlines()):
        if len(fields) < 9:
            continue
        fields = [field.strip() for field in fields]
        try:
            timestamp = datetime.strptime(fields[0], "%Y/%m/%d %H:%M:%S.%f").replace(tzinfo=PACIFIC)
        except ValueError:
            continue
        samples.append({"timestamp": timestamp, "gpu_uuid": fields[2], "gpu_utilization_percent": numeric(fields[3]), "memory_utilization_percent": numeric(fields[4]), "memory_used_mib": numeric(fields[5]), "memory_total_mib": numeric(fields[6]), "power_watts": numeric(fields[7]), "temperature_celsius": numeric(fields[8])})
    return samples


def telemetry_summary(samples, uuids, start=None, end=None):
    selected = [sample for sample in samples if sample["gpu_uuid"] in uuids and (start is None or sample["timestamp"] >= start) and (end is None or sample["timestamp"] <= end)]
    result = {"gpu_uuids": uuids, "samples": len(selected), "window_start": start.isoformat() if start else None, "window_end": end.isoformat() if end else None, "timestamp_time_zone_assumption": "nvidia-smi node-local timestamps interpreted as America/Los_Angeles", "measurement": "Sampled telemetry log values; sampled maxima are not continuous-time peaks."}
    for key in ("gpu_utilization_percent", "memory_utilization_percent", "memory_used_mib", "power_watts", "temperature_celsius"):
        values = [sample[key] for sample in selected if sample[key] is not None]
        result["sampled_max_" + key] = max(values) if values else None
        result["sampled_mean_" + key] = statistics.mean(values) if values else None
    return result


def stage_window(stage_directory: Path, summary: dict):
    starts, ends = [], []
    for path in stage_directory.glob("response_*.json"):
        response = read_json(path, {})
        start, end = parse_time(response.get("started_at")), parse_time(response.get("finished_at"))
        if start:
            starts.append(start)
        if end:
            ends.append(end)
    if starts and ends:
        return min(starts), max(ends)
    end = parse_time(summary.get("finished_at"))
    return (end - timedelta(seconds=summary["elapsed_seconds"]), end) if end and summary.get("elapsed_seconds") is not None else (None, None)


def group_name(step):
    if "quick" in step["name"]:
        return "quick_fixed_total_work"
    if "long_decode" in step["name"]:
        return "long_decode_full_batch"
    return "other"


def sampling_metadata(config, plan):
    actual = config.get("sampling")
    settings = actual if isinstance(actual, dict) and actual else plan.get("generation", {})
    settings = dict(settings)
    if "seed" not in settings and "generation_seed" in settings:
        settings["seed"] = settings["generation_seed"]
    selected = {key: settings[key] for key in ("temperature", "top_p", "top_k", "seed") if key in settings}
    return {"settings": selected, "source": "observed client config" if actual else "frozen plan" if selected else "unavailable"}


def sampling_description(sampling):
    settings = sampling.get("settings", {})
    if not settings:
        return "Sampling settings are not yet recorded."
    mode = "Greedy decoding" if settings.get("temperature") == 0 else "Sampled decoding"
    parameters = ", ".join(f"`{key}={value}`" for key, value in settings.items())
    return f"{mode}: {parameters} ({sampling['source']})."


def sampling_limitation(sampling):
    settings = sampling.get("settings", {})
    matched = settings.get("temperature") == 1 and settings.get("top_p") == .95 and settings.get("top_k") == 20 and settings.get("seed") == 42
    if matched:
        return "Sampling parameters match production (temperature 1, top_p 0.95, top_k 20, seed 42). The synthetic /v1/completions workload still differs from production chat/thinking prompts and natural stopping, so identical evaluation throughput or the same best concurrency is not established."
    if settings.get("temperature") == 0:
        return "Production uses chat/thinking prompts and sampled decoding (temperature 1, top_p 0.95, top_k 20, seed 42). This greedy completions test does not establish identical evaluation throughput or the same best concurrency under production sampling."
    return "Synthetic /v1/completions requests and forced output lengths differ from production chat/thinking prompts and natural stopping; identical evaluation throughput or the same best concurrency is not established."


def calculate_findings(rows):
    findings = {}
    for group in ("quick_fixed_total_work", "long_decode_full_batch"):
        candidates = [row for row in rows if row["group"] == group and row["eligible_best_tested_candidate"] and row.get("output_tokens_per_second") is not None and row.get("source_role") != "original_baseline"]
        findings[group + "_best_tested"] = max(candidates, key=lambda row: row["output_tokens_per_second"])["id"] if candidates else None
    baseline = next((row for row in rows if row["group"] == "quick_fixed_total_work" and row["server_capacity"] == 4 and row["client_concurrency"] == 4 and row["eligible_best_tested_candidate"]), None)
    changed_capacity = next((row for row in rows if row["group"] == "quick_fixed_total_work" and row["server_capacity"] == 32 and row["client_concurrency"] == 4 and row["eligible_best_tested_candidate"]), None)
    findings["capacity32_vs_capacity4_at_client4_quick_ratio"] = changed_capacity["output_tokens_per_second"] / baseline["output_tokens_per_second"] if baseline and changed_capacity and baseline["output_tokens_per_second"] else None
    return findings


def collect_report(directory: Path):
    plan = read_json(directory / "plan.json", {})
    if not plan.get("steps"):
        raise ValueError("A frozen plan.json with steps is required")
    environment = read_json(directory / "environment.json", {})
    status = read_json(directory / "status.json", {})
    samples = read_telemetry(directory / "gpu_telemetry.csv")
    capacities = sorted({step["server_capacity"] for step in plan["steps"]})
    allocated = {str(capacity): gpu_uuids(directory, capacity) for capacity in capacities}
    source_files = [directory / name for name in ("plan.json", "environment.json", "status.json", "gpu_telemetry.csv")]
    for capacity in capacities:
        source_files.extend([directory / f"server_capacity_{capacity}.json", directory / f"server_capacity_{capacity}_gpu.json"])
    rows = []
    for step in plan["steps"]:
        step_directory = directory / step["name"]
        result_path = step_directory / "results.json"
        result = read_json(result_path, {})
        config = read_json(step_directory / "config.json", result.get("config", {}))
        progress = read_json(step_directory / "progress.json", {})
        complete = {row["stage"]: row for row in result.get("stages", [])}
        # A completed stage summary may be written just before results.json.
        for path in step_directory.glob("repeat_*/summary.json"):
            stage = read_json(path, {})
            if stage.get("stage"):
                complete.setdefault(stage["stage"], stage)
        source_files.extend([result_path, step_directory / "config.json", step_directory / "progress.json"])
        repeats = config.get("repeats", 1)
        levels = [int(value) for value in step["concurrencies"].split(",")]
        for repeat in range(1, repeats + 1):
            order = levels if repeat % 2 else list(reversed(levels))
            for concurrency in order:
                stage_name = f"repeat_{repeat:02d}_concurrency_{concurrency:03d}"
                stage_directory = step_directory / stage_name
                measurement = complete.get(stage_name)
                partial_summary = progress.get("stage_partial_summary") or {}
                partial = measurement is None and progress.get("stage") == stage_name and progress.get("completed_requests", 0) > 0 and partial_summary.get("completed_requests") == progress.get("completed_requests")
                if partial:
                    measurement = progress["stage_partial_summary"]
                measurement = measurement or {}
                completed = measurement.get("completed_requests", 0)
                is_complete = stage_name in complete and completed == step["requests"]
                row_status = "complete" if is_complete else "partial" if measurement else "pending"
                if not is_complete and progress.get("state") in ("failed", "interrupted"):
                    row_status = progress["state"] if measurement or progress.get("stage") == stage_name else row_status
                preemptions = preemption_delta(stage_directory)
                start, end = stage_window(stage_directory, measurement)
                uuids = allocated[str(step["server_capacity"])]
                telemetry = telemetry_summary(samples, uuids, start, end) if start and end else telemetry_summary([], uuids)
                valid = is_complete and measurement.get("failed_requests") == 0 and measurement.get("fixed_workload_mismatch_requests") == 0 and measurement.get("successful_requests") == step["requests"] and measurement.get("comparable_fixed_workload") is True
                row = {"id": step["name"] + "/" + stage_name, "step": step["name"], "stage": stage_name, "group": group_name(step), "server_capacity": step["server_capacity"], "client_concurrency": concurrency, "repeat": repeat, "input_tokens_per_request": step["input_tokens"], "output_tokens_per_request": step["output_tokens"], "planned_requests": step["requests"], "completed_requests": completed, "status": row_status, "eligible_best_tested_candidate": valid, "preemptions": preemptions, "gpu_telemetry": telemetry, "sampling": sampling_metadata(config, plan)}
                for key in ("elapsed_seconds", "successful_requests", "failed_requests", "fixed_workload_mismatch_requests", "output_tokens_per_second", "requests_per_second", "actual_prompt_tokens", "actual_completion_tokens", "latency_seconds", "prefix_cache_policy", "prefix_cache_controlled"):
                    row[key] = measurement.get(key)
                row["requests_per_hour"] = row["requests_per_second"] * 3600 if row["requests_per_second"] is not None else None
                rows.append(row)
                source_files.extend([stage_directory / "summary.json", stage_directory / "metrics_before.prom", stage_directory / "metrics_after.prom"])
    findings = calculate_findings(rows)
    own_uuids = sorted({uuid for values in allocated.values() for uuid in values})
    observed = next((row["sampling"] for row in rows if row["sampling"]["source"] == "observed client config"), sampling_metadata({}, plan))
    return {"generated_at": datetime.now(PACIFIC).isoformat(), "time_zone": "America/Los_Angeles", "measurement_type": "synthetic serving throughput, not biological benchmark scores", "directory": str(directory), "plan": plan, "environment": environment, "sampling": observed, "server_configurations": {str(capacity): read_json(directory / f"server_capacity_{capacity}.json", {}) for capacity in capacities}, "run_status": {**status, "updated_at": parse_time(status.get("updated_at")).isoformat() if status.get("updated_at") else None}, "gpu_identities_by_server_capacity": allocated, "gpu_telemetry_all_run": telemetry_summary(samples, own_uuids), "rows": rows, "findings": findings, "limitations": ["Single ascending concurrency sweep is preliminary; no robust optimum is established.", "Quick sweep uses fixed total work. Long-decode checks use one full concurrent batch, so request count and total work increase with concurrency and are reported separately.", "Custom standard-library client uses /v1/completions with deterministic token-ID synthetic prompts, recorded sampling settings, ignore_eos, and forced output lengths; this is not the official vllm bench serve command and does not assess answer quality.", sampling_limitation(observed), "No extrapolation to P16: its roughly 44k-token shared-prefix prompts and B200 hardware differ from this A100 workload.", "GPU maxima come from sampled logs filtered to the observed server GPU UUID; missing telemetry is left unavailable. Node-local nvidia-smi timestamps are interpreted as Pacific time."], "source_files": {str(path.relative_to(directory)): digest(path) for path in source_files if path.is_file()}}


def add_original_baseline(report, baseline_directory: Path):
    baseline = collect_report(baseline_directory)
    imported = [dict(row) for row in baseline["rows"] if row["status"] == "complete" and row["eligible_best_tested_candidate"] and row["group"] == "quick_fixed_total_work" and row["server_capacity"] == 4 and row["client_concurrency"] == 4]
    if not imported:
        raise ValueError("Baseline directory has no complete, error-free capacity-four/client-four quick measurement")
    primary_name, baseline_name = Path(report["directory"]).name, baseline_directory.name
    for role, name, rows in (("primary", primary_name, report["rows"]), ("original_baseline", baseline_name, imported)):
        for row in rows:
            row.update(source_role=role, source_run=name, original_row_id=row["id"], id=name + "/" + row["id"])
    source_runs = []
    for role, source, selected in (("primary", report, report["rows"]), ("original_baseline", baseline, imported)):
        source_runs.append({"role": role, "directory": source["directory"], "run_status": source["run_status"], "environment": source["environment"], "sampling": source["sampling"], "selected_rows": [row["id"] for row in selected], "source_files": source["source_files"], "gpu_identities_by_server_capacity": source["gpu_identities_by_server_capacity"]})
    report["source_runs"] = source_runs
    report["rows"] = imported + report["rows"]
    report["findings"] = calculate_findings(report["rows"])
    baseline_uuids = sorted({uuid for row in imported for uuid in row["gpu_telemetry"]["gpu_uuids"]})
    primary_uuids = report["gpu_telemetry_all_run"]["gpu_uuids"]
    previous_status = baseline["run_status"].get("stage", "unknown")
    report["baseline_comparison"] = {"baseline_directory": str(baseline_directory), "baseline_run_status": previous_status, "baseline_host": baseline["environment"].get("hostname"), "primary_host": report["environment"].get("hostname"), "baseline_gpu_uuids": baseline_uuids, "primary_gpu_uuids": primary_uuids, "different_physical_gpu": bool(set(baseline_uuids) != set(primary_uuids)) if baseline_uuids and primary_uuids else None, "cross_run": True, "limitation": f"Original capacity-four baseline was imported from an earlier allocation whose overall run status is {previous_status}; only its completed valid baseline is included. The baseline ratio can include variation between physical GPUs or nodes and does not isolate a server-capacity effect. The capacity-32 concurrency comparisons use only the primary run."}
    report["limitations"].append(report["baseline_comparison"]["limitation"])
    return report


def number(value, digits=2):
    return f"{value:,.{digits}f}" if value is not None else "—"


def percent(value, digits=0):
    return number(value, digits) + "%" if value is not None else "—"


def measured_table(rows):
    lines = ["| Server capacity | Client concurrency | Input / output tokens | Requests done / planned | Output tokens/s | Requests/hour | p50 / p95 latency (s) | Errors | Token mismatches | Preemptions | State |", "|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|"]
    for row in rows:
        latency = row.get("latency_seconds") or {}
        lines.append(f"| {row['server_capacity']} | {row['client_concurrency']} | {row['input_tokens_per_request']:,} / {row['output_tokens_per_request']:,} | {row['completed_requests']} / {row['planned_requests']} | {number(row['output_tokens_per_second'])} | {number(row['requests_per_hour'])} | {number(latency.get('p50'))} / {number(latency.get('p95'))} | {number(row['failed_requests'], 0)} | {number(row['fixed_workload_mismatch_requests'], 0)} | {number(row['preemptions']['delta'], 0)} | {row['status']} |")
    return "\n".join(lines)


def main_finding(report):
    for group, label in (("long_decode_full_batch", "long-decode check"), ("quick_fixed_total_work", "quick fixed-work comparison")):
        identifier = report["findings"].get(group + "_best_tested")
        if not identifier:
            continue
        best = next(row for row in report["rows"] if row["id"] == identifier)
        baseline = next((row for row in report["rows"] if row["group"] == group and row["server_capacity"] == best["server_capacity"] and row["client_concurrency"] == 4 and row["eligible_best_tested_candidate"] and row.get("source_role") != "original_baseline"), None)
        text = f"The best completed point in the {label} is **{best['client_concurrency']} concurrent requests**, reaching **{number(best['output_tokens_per_second'])} output tokens/s**"
        if baseline and baseline["id"] != best["id"] and baseline["output_tokens_per_second"]:
            ratio = best["output_tokens_per_second"] / baseline["output_tokens_per_second"]
            text += f" — **{number(ratio)}×** the primary four-request baseline at the same server capacity"
        text += f". Each request has **{best['input_tokens_per_request']:,} synthetic input tokens** and {best['output_tokens_per_request']:,} forced output tokens."
        if group == "long_decode_full_batch":
            text += " The long-decode checks use one full concurrent batch per point."
        return text + " Production settings remain unchanged; longer inputs and P16 have not been validated by this test."
    return "Primary concurrency measurements are still in progress. Production settings remain unchanged; longer inputs and P16 have not been validated by this test."


def markdown(report, output_prefix: Path):
    generated = parse_time(report["generated_at"]).strftime("%B %d, %Y, %-I:%M %p %Z")
    environment = report["environment"]
    packages = environment.get("packages", {})
    plan = report["plan"]
    lines = ["# vLLM concurrency measurements", "", f"Updated {generated}. Run state: **{report['run_status'].get('stage', 'unknown')}**.", "", f"Dedicated **{packages.get('device', 'GPU identity pending')}** replica of **{plan.get('model', 'unknown model')}**, original BF16, tensor parallelism 1; vLLM {packages.get('vllm', 'unknown')}. Server context limit: {plan.get('max_model_len', 0):,} tokens. Checkpoint revision: `{plan.get('revision', 'unknown')}`.", "", "These are synthetic serving measurements, not biological evaluation scores. A custom Python standard-library client sends identical predetermined token-ID prompts across concurrency levels through `/v1/completions`, with `ignore_eos=true` and a fixed output-token count. Enabled production prefix caching is reset before every stage. Warmup is excluded from measurements.", "", sampling_description(report["sampling"]), "", "## Quick comparison: fixed total work", "", "Each point processes the same 32 requests with 192 input tokens and 512 forced output tokens each. The original server capacity of four is measured first; a separate server with capacity 32 then runs the concurrency sweep.", "", measured_table([row for row in report["rows"] if row["group"] == "quick_fixed_total_work"]), ""]
    lines[4:4] = [main_finding(report), ""]
    ratio = report["findings"]["capacity32_vs_capacity4_at_client4_quick_ratio"]
    cross_run = report.get("baseline_comparison")
    if cross_run:
        hardware = "different physical GPUs" if cross_run["different_physical_gpu"] else "separate allocations"
        lines.extend([f"The capacity-four baseline comes from earlier run `{Path(cross_run['baseline_directory']).name}`; that prior run ended **{cross_run['baseline_run_status']}**, after this valid baseline completed. The capacity-32 rows belong to the primary run. Baseline and primary measurements use {hardware} (hosts `{cross_run['baseline_host']}` and `{cross_run['primary_host']}`), so variation between GPUs or nodes may affect their ratio. Capacity-32 concurrency comparisons remain within the primary run.", ""])
    if ratio is not None:
        explanation = "This cross-run ratio does not isolate a server-capacity effect because physical GPU or node variation may contribute." if cross_run else "This comparison separates changing server capacity from increasing client load."
        lines.extend([f"At client concurrency four, the capacity-32 to capacity-four quick-workload throughput ratio is **{number(ratio)}×**. {explanation}", ""])
    lines.extend(["## Long decode: one full concurrent batch", "", "Each request has 192 input tokens and 4,096 forced output tokens. Request count equals client concurrency, so total work grows across rows. These full-batch checks are reported separately from the fixed-total-work quick sweep.", "", measured_table([row for row in report["rows"] if row["group"] == "long_decode_full_batch"]), "", "## Best tested points", ""])
    for group, label in (("quick_fixed_total_work", "Quick fixed-work sweep"), ("long_decode_full_batch", "Long full-batch check")):
        identifier = report["findings"][group + "_best_tested"]
        if identifier:
            row = next(row for row in report["rows"] if row["id"] == identifier)
            lines.append(f"- **{label}:** server capacity {row['server_capacity']}, client concurrency {row['client_concurrency']} achieved {number(row['output_tokens_per_second'])} output tokens/s with zero request errors and zero token-count mismatches. This is the best tested point among completed measurements.")
        else:
            lines.append(f"- **{label}:** no complete, error-free measurement with exact token counts is available yet.")
    lines.extend(["", "A single ascending sweep is preliminary and does not establish a robust optimum. Pending or partial rows do not qualify as recommendations. " + sampling_limitation(report["sampling"]) + " These results do not establish a faster setting for P16, whose roughly 44k-token shared-prefix prompts run on different B200 hardware.", "", "## GPU telemetry from the sampled log", "", "Only the server's observed GPU UUID is included. Sampled maxima come from `gpu_telemetry.csv`, rather than before/after snapshots; brief peaks between samples can be missed. NVIDIA timestamps are interpreted in Pacific time.", "", "| Step / client concurrency | Samples during measured requests | Sampled maximum memory (MiB) | Sampled maximum GPU utilization | Mean GPU utilization |", "|---|---:|---:|---:|---:|"])
    for row in report["rows"]:
        if row["status"] == "pending":
            continue
        telemetry = row["gpu_telemetry"]
        lines.append(f"| {row['step']} / {row['client_concurrency']} | {telemetry['samples']} | {number(telemetry['sampled_max_memory_used_mib'], 0)} | {percent(telemetry['sampled_max_gpu_utilization_percent'])} | {percent(telemetry['sampled_mean_gpu_utilization_percent'], 2)} |")
    overall = report["gpu_telemetry_all_run"]
    scope = "Primary-run allocated" if cross_run else "Allocated"
    lines.extend(["", f"{scope} GPU UUID(s): {', '.join('`' + uuid + '`' for uuid in overall['gpu_uuids']) or 'not observed yet'}. Across its startup, warmup and measured stages, the log contains {overall['samples']:,} matching samples; sampled maximum memory is {number(overall['sampled_max_memory_used_mib'], 0)} MiB and sampled maximum GPU utilization is {percent(overall['sampled_max_gpu_utilization_percent'])}.", "", "Latency is measured from dispatch to the complete response, excluding client queue time. Throughput divides successful responses or their actual output tokens by full stage wall time, including failures. Preemptions are differences in the vLLM counter between stage snapshots; unavailable counters remain blank. Forced output lengths describe a controlled compute workload, not natural answer lengths or answer quality.", "", "## Artifacts and provenance", "", f"[Machine-readable measurements and provenance]({output_prefix.name}.json). Methodology reference: [vLLM 0.31.0 serving benchmark options](https://docs.vllm.ai/en/v0.31.0/cli/bench/serve/). This run uses our custom client rather than the official benchmark command.", ""])
    if report.get("artifact_archive"):
        lines.extend([f"[Download the benchmark artifacts](<{report['artifact_archive']}>).", ""])
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--directory", type=Path, required=True)
    parser.add_argument("--baseline-directory", type=Path, help="Earlier run containing the completed original capacity-four quick baseline")
    parser.add_argument("--archive-link", help="Relative link to the published benchmark artifact archive")
    parser.add_argument("--output-prefix", type=Path, required=True)
    args = parser.parse_args()
    report = collect_report(args.directory.resolve())
    if args.baseline_directory:
        report = add_original_baseline(report, args.baseline_directory.resolve())
    if args.archive_link:
        if Path(args.archive_link).is_absolute() or "://" in args.archive_link or "\n" in args.archive_link:
            raise ValueError("--archive-link must be a relative path")
        report["artifact_archive"] = args.archive_link
    args.output_prefix.parent.mkdir(parents=True, exist_ok=True)
    args.output_prefix.with_suffix(".json").write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    args.output_prefix.with_suffix(".md").write_text(markdown(report, args.output_prefix))
    print(json.dumps({"rows": len(report["rows"]), "complete": sum(row["status"] == "complete" for row in report["rows"]), "run_state": report["run_status"].get("stage"), "findings": report["findings"]}, indent=2))


if __name__ == "__main__":
    main()
