#!/usr/bin/env python3
"""Prepare a reviewed report/archive and explicit publish manifest; never push.

Only closed synthetic benchmark directories and explicitly frozen pool files
enter the archive. Live server logs, GPU logs, model files and environments do
not. The caller confirms native activation separately after reviewing evidence.
"""
from __future__ import annotations

import argparse
from datetime import datetime
import gzip
import hashlib
import importlib.util
import io
import json
import math
import os
from pathlib import Path
import tarfile
from zoneinfo import ZoneInfo


PACIFIC = ZoneInfo("America/Los_Angeles")
REQUIRED_INPUT_PROFILES = (192, 1536, 7000, 16384, 45056, 49152)
EXCLUSIONS = {
    "replica_2/length_benchmark_192": "Failed idle-server preflight before generation; no measured capacity result.",
    "replica_3/length_benchmark": "The original 45056-token sweep overlapped the prematurely started 49152-token sweep on the same endpoint.",
    "replica_3/length_benchmark_49152": "Started before the original 45056-token sweep closed; shared-server token counters and queues prove unrelated concurrent work.",
}
PUBLIC_SOURCES = (
    "configs/local_vllm_length_benchmark.json",
    "scripts/benchmark_vllm_concurrency.py", "scripts/benchmark_vllm_prompt_lengths.py",
    "scripts/drain_vllm_worker.py", "scripts/prepare_shared_vllm_amendment.py",
    "scripts/run_shared_vllm_evaluations.py", "scripts/run_shared_vllm_pool.py",
    "scripts/shared_vllm_resume.py", "scripts/shared_vllm_scoring.py",
    "scripts/watch_shared_vllm_scoring.py", "scripts/watch_shared_vllm_health.py",
    "scripts/publish_shared_vllm_artifacts.py", "scripts/prepare_shared_vllm_publication.py",
    "tests/test_benchmark_vllm_concurrency.py", "tests/test_benchmark_vllm_prompt_lengths.py",
    "tests/test_drain_vllm_worker.py", "tests/test_prepare_shared_vllm_amendment.py",
    "tests/test_shared_vllm_resume.py", "tests/test_shared_vllm_scoring.py",
    "tests/test_watch_shared_vllm_scoring.py", "tests/test_watch_shared_vllm_health.py",
    "tests/test_publish_shared_vllm_artifacts.py", "tests/test_prepare_shared_vllm_publication.py",
)


def read(path):
    return json.loads(Path(path).read_text())


def digest(data):
    return hashlib.sha256(data).hexdigest()


def write_json(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name + ".tmp")
    temporary.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n")
    temporary.replace(path)


def pacific(value):
    return datetime.fromisoformat(value.replace("Z", "+00:00")).astimezone(PACIFIC).strftime("%Y-%m-%d %H:%M:%S %Z")


def counter(measured, side, prefix):
    values = [v for k, v in measured.get(side, {}).get("selected", {}).items()
              if k.split("{", 1)[0] == prefix]
    if not values or any(not isinstance(v, (int, float)) or not math.isfinite(v) for v in values):
        return None
    return sum(values)


def isolation_check(row, directory):
    """Use total server work, idle boundaries and queues, not client success alone."""
    measured, reasons = row["measured"], []
    for name, expected in (("vllm:prompt_tokens_total", measured["actual_prompt_tokens"]),
                           ("vllm:generation_tokens_total", measured["actual_completion_tokens"])):
        before, after = (counter(measured, side, name) for side in ("metrics_before", "metrics_after"))
        if before is None or after is None or after - before != expected:
            reasons.append(name + " did not match this batch's exact token usage")
    for side in ("metrics_before", "metrics_after"):
        for name in ("vllm:num_requests_running", "vllm:num_requests_waiting"):
            if counter(measured, side, name) != 0:
                reasons.append(side + " was not idle: " + name)
    source = row.get("monitoring", {}).get("sample_file")
    path = Path(source).resolve() if source else None
    if path is None or not path.is_relative_to(directory.resolve()) or not path.is_file():
        reasons.append("Missing owned live queue sample file")
    else:
        for line in path.read_text().splitlines():
            sample = json.loads(line)
            running, waiting = sample.get("running"), sample.get("waiting")
            if running is None or waiting is None or running < 0 or waiting < 0 or running + waiting > row["concurrency"]:
                reasons.append("Live queue contained more requests than this client batch or lacked queue data")
                break
    return {"passed": not reasons, "reasons": reasons}


def collect_measurements(pool):
    attempts, rows = [], []
    directories = sorted({p.parent for p in pool.glob("replica_*/*/progress.json")
                          if "benchmark" in p.parent.name})
    for directory in directories:
        relative = directory.relative_to(pool).as_posix()
        progress = read(directory / "progress.json")
        closed = progress.get("state") in {"completed", "failed"}
        attempt = {"directory": relative, "state": progress.get("state"), "closed": closed,
                   "updated_at_pacific": pacific(progress["updated_at"]),
                   "excluded_from_capacity": relative in EXCLUSIONS,
                   "exclusion_reason": EXCLUSIONS.get(relative), "error": progress.get("error")}
        attempts.append(attempt)
        if not (directory / "results.json").is_file():
            continue
        result = read(directory / "results.json")
        for source in result["rows"]:
            row = {"directory": relative, "state": source["state"],
                   "input_tokens": source["input_tokens"], "output_tokens": source["output_tokens"],
                   "concurrency": source["concurrency"], "planned_requests": source["planned_requests"],
                   "projection": source.get("projection"), "closed_attempt": closed,
                   "attempt_exclusion": EXCLUSIONS.get(relative)}
            if source["state"] != "measured":
                row.update(accepted=False, reason=source.get("reason"))
            else:
                measured = source["measured"]
                check = isolation_check(source, directory)
                row.update(
                    accepted=bool(closed and progress["state"] == "completed" and source.get("eligible")
                                  and relative not in EXCLUSIONS and check["passed"]),
                    harness_eligible=source.get("eligible"), isolation=check,
                    requests=measured["completed_requests"], failures=measured["failed_requests"],
                    token_mismatches=measured["fixed_workload_mismatch_requests"],
                    actual_prompt_tokens=measured["actual_prompt_tokens"],
                    actual_completion_tokens=measured["actual_completion_tokens"],
                    output_tokens_per_second=measured["output_tokens_per_second"],
                    elapsed_seconds=measured["elapsed_seconds"], latency_seconds=measured["latency_seconds"],
                    sampled_peak_kv_fraction=source["sampled_peak_kv_fraction"],
                    preemption_delta=source["monitoring"]["preemption_delta"],
                    finished_at_pacific=pacific(measured["finished_at"]),
                    sampling=result["plan"]["generation"],
                    frozen_launcher_sha256=result["provenance"]["launcher_sha256"],
                )
            rows.append(row)
    best = []
    for length in sorted({row["input_tokens"] for row in rows if row["accepted"]}):
        candidates = [row for row in rows if row["accepted"] and row["input_tokens"] == length]
        best.append(max(candidates, key=lambda row: row["output_tokens_per_second"]))
    return attempts, rows, best


def frozen_files(pool, attempts):
    files = {}
    def add(path, expected=None):
        source = Path(path)
        path = source.resolve()
        if source.is_symlink() or not path.is_relative_to(pool) or not path.is_file():
            raise ValueError("Archive source must be a regular owned pool file")
        data = path.read_bytes()
        if expected is not None and digest(data) != expected:
            raise ValueError("Frozen pool source hash mismatch: " + path.name)
        files["pool/" + pool.name + "/" + path.relative_to(pool).as_posix()] = data
    plan = read(pool / "plan.json")
    if (pool / "plan.sha256").read_text().strip() != digest((pool / "plan.json").read_bytes()):
        raise ValueError("Pool plan no longer matches its frozen hash")
    for name in ("plan.json", "plan.sha256", "pool.sbatch", "endpoints.json"):
        add(pool / name)
    for source, expected in plan["code_sha256"].items():
        add(source, expected)
    for source in pool.glob("*benchmark*plan.json"):
        add(source)
    for endpoint in read(pool / "endpoints.json"):
        add(endpoint["server_identity_file"], endpoint["server_identity_sha256"])
    for attempt in attempts:
        if not attempt["closed"]:
            continue
        directory = pool / attempt["directory"]
        before = digest((directory / "progress.json").read_bytes())
        for source in sorted(directory.rglob("*")):
            if source.is_symlink():
                raise ValueError("Benchmark evidence contains a symlink")
            if source.is_file() and source.suffix != ".tmp":
                if source.suffix not in {".json", ".jsonl", ".prom"}:
                    raise ValueError("Unexpected benchmark archive extension: " + source.name)
                add(source)
        if digest((directory / "progress.json").read_bytes()) != before:
            raise ValueError("Closed benchmark changed while preparing archive")
    return files


def build_archive(path, files, scanner):
    members = [{"path": name, "bytes": len(data), "sha256": digest(data)} for name, data in sorted(files.items())]
    if sum(row["bytes"] for row in members) > scanner.MAX_ARCHIVE_SCAN - 1024 * 1024:
        raise ValueError("Evidence exceeds the existing recursive credential scanner limit")
    files = dict(files)
    files["MANIFEST.json"] = (json.dumps({"schema_version": 1, "members": members}, indent=2, sort_keys=True) + "\n").encode()
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name + ".pending.tar.gz")
    try:
        with temporary.open("wb") as raw:
            with gzip.GzipFile(filename="", fileobj=raw, mode="wb", mtime=0) as compressed:
                with tarfile.open(fileobj=compressed, mode="w") as archive:
                    for name, data in sorted(files.items()):
                        scanner.safe_archive_member(name)
                        scanner.scan_bytes(data)
                        info = tarfile.TarInfo(name)
                        info.size, info.mode, info.mtime = len(data), 0o644, 0
                        archive.addfile(info, io.BytesIO(data))
        scanner.scan_file(temporary)
        if temporary.stat().st_size > scanner.MAX_GIT_FILE:
            raise ValueError("Archive exceeds the existing Git file size guard")
        temporary.replace(path)
    finally:
        temporary.unlink(missing_ok=True)
    return {"sha256": digest(path.read_bytes()), "bytes": path.stat().st_size,
            "member_count": len(files), "members": members,
            "credential_scan": "passed for every uncompressed member and the complete archive"}


def markdown(report, archive_link):
    best, active = report["best_tested_points"], report["native_pool_start_confirmed"]
    lines = ["# Shared vLLM evaluation execution", "", "Prepared " + report["prepared_at_pacific"] + ".", "",
             ("Native evaluation dispatch has started on the shared pool." if active else
              "Synthetic capacity checks are being prepared for the shared pool; native dispatch has not been confirmed for this report."), "",
             "The pool uses four NVIDIA A100 GPUs on one host (" + report["hostname"] +
             "), with one vLLM replica per GPU. Each replica serves the original BF16 Qwen3.8-27B checkpoint with tensor parallel size 1 and a 65,536-token context limit. The native evaluation output budget remains 4,096 tokens.", "",
             "The table shows the fastest accepted **tested** concurrency at each exact synthetic input length. Every request decoded exactly 4,096 tokens. These are full batches: the number of requests equals concurrency, so total work differs between rows. They measure serving capacity, not biological accuracy.", "",
             "| Input tokens/request | Tested concurrency | Requests | Output tokens/s | p50 / p95 latency (s) | Sampled peak KV |", "|---:|---:|---:|---:|---:|---:|"]
    for row in best:
        latency = row["latency_seconds"]
        lines.append(f"| {row['input_tokens']:,} | {row['concurrency']} | {row['requests']} | {row['output_tokens_per_second']:.2f} | {latency['p50']:.2f} / {latency['p95']:.2f} | {row['sampled_peak_kv_fraction']:.1%} |")
    if not best:
        lines.append("| No closed, isolated measurement accepted yet | — | — | — | — | — |")
    lines += ["", "Accepted points have zero request failures, token-count mismatches and measured preemptions. Admission also requires idle queue boundaries, server token-counter deltas matching the exact batch, and live queue samples containing at most that batch's requests. KV peaks are sampled; brief peaks can be missed. Higher loads skipped by the memory guard remain unmeasured.", "",
              "The measurements use a single ascending sweep, synthetic token IDs, the completions API, prefix-cache resets between points, and sampling temperature 1, top_p 0.95, top_k 20, seed 42. They do not reproduce native chat/thinking prompts or prove an optimum. P16's shared-prefix workload can behave differently from independent synthetic long prompts.", "",
              "Length-aware dispatch uses the frozen amendment's measured caps and a global queue shared by the four replicas. As capacity opens, replicas take requests across evaluation settings. Native requests retain their original prompts, generation settings and scorers. Requests longer than the measured admission range remain blocked pending evidence.", ""]
    if report.get("active_length_limits"):
        lines += ["Frozen dispatch limits: " + "; ".join(f"up to {r['max_prompt_tokens']:,} input tokens: {r['max_inflight']} in flight per replica" for r in report["active_length_limits"]) + ".", ""]
    lines += ["A separate health watcher checks replica identity, queue/KV/preemption metrics, transport failures and response metadata. It records truncation and empty final answers without calling the model, biological scorer or changing output budgets. Native scorers run only after generation and preserve each benchmark's own metric and denominator. The additive uploader saves raw request/response trajectories, dispatch receipts, provenance and completed scoring views.", "",
              "Three earlier P08 shard drains caused their native wrapper to score partial output. Those partial scores, completion records and locks remain immutable. Continuation writes use separate derived folders that pin the original history; the logical shard IDs stay the same so copied history is not counted twice. The corrected drain helper stops the executor parent before draining, then prevents it from automatically scoring during termination.", "",
              "The original 4,096-token generation limit is unchanged. A response ending at that limit can be truncated and may lack a usable final answer; improved throughput does not resolve that quality limitation. Saved responses and completed benchmark scores remain separate quantities. No completion-time estimate is inferred from these synthetic rates.", "",
              "An evidence review caught two overlapping long-input sweeps on replica 3: an extra 49,152-token sweep started before the original 45,056-token sweep finished. Both are excluded from capacity admission, even where the client originally marked a point eligible. The first 192-token attempt failed its busy-server preflight before generation. All three attempts remain in the archive. Clean reruns use distinct idle replicas after the original sweeps closed.", "",
              "The benchmark client originally checked exclusivity only once and did not own the endpoint across gaps between points. Its results file was a per-point checkpoint, so its existence did not prove a whole sweep had finished. The public source now holds an exclusive endpoint lock for the full profile; the measurements retain their original frozen source and hashes. A CPU test verifies that a second process is refused until the first releases ownership.", "",
              f"[Download closed synthetic evidence and frozen pool sources]({archive_link}). The JSON report records every measured/skipped point, exclusions, file hashes and the exact source hashes. The archive contains no live server/GPU logs, model weights, environment, caches or unrelated data.", ""]
    if report["open_benchmark_directories"]:
        lines += ["**Draft:** still-open benchmark directories are excluded from the archive: " + ", ".join(report["open_benchmark_directories"]) + ".", ""]
    if report["missing_accepted_input_profiles"]:
        lines += ["**Draft:** accepted capacity evidence is still missing for input lengths " + ", ".join(map(str, report["missing_accepted_input_profiles"])) + ".", ""]
    lines += ["Pool plan SHA-256: `" + report["pool_plan_sha256"] + "`.",
              "Archive SHA-256: `" + report["archive"]["sha256"] + "`.", ""]
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--pool-directory", required=True, type=Path)
    parser.add_argument("--output-prefix", required=True, type=Path)
    parser.add_argument("--archive", required=True, type=Path)
    parser.add_argument("--publication-manifest", required=True, type=Path)
    parser.add_argument("--baseline-commit", required=True)
    parser.add_argument("--amendment", type=Path)
    parser.add_argument("--native-start-confirmed", action="store_true")
    parser.add_argument("--extra-public-file", action="append", default=[])
    args = parser.parse_args()
    root, pool = args.root.resolve(), args.pool_directory.resolve()
    if len(args.baseline_commit) != 40 or any(c not in "0123456789abcdef" for c in args.baseline_commit):
        raise ValueError("A reviewed latest-remote 40-character commit is required")
    spec = importlib.util.spec_from_file_location("public_artifact_scanner", root / "scripts/daily_backup.py")
    scanner = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(scanner)
    attempts, rows, best = collect_measurements(pool)
    archive_path = (root / args.archive).resolve()
    prefix = (root / args.output_prefix).resolve()
    if not archive_path.is_relative_to(root / "reports") or not prefix.is_relative_to(root / "reports"):
        raise ValueError("Public report and archive destinations must be under reports/")
    archive = build_archive(archive_path, frozen_files(pool, attempts), scanner)
    identities = [read(pool / f"replica_{i}/server_identity.json") for i in range(4)]
    if len({row["hostname"] for row in identities}) != 1 or len({uuid for row in identities for uuid in row["gpu_uuids"]}) != 4:
        raise ValueError("Expected four unique GPU replicas on one host")
    amendment = read(args.amendment) if args.amendment else None
    open_directories = [row["directory"] for row in attempts if not row["closed"]]
    missing_profiles = sorted(set(REQUIRED_INPUT_PROFILES) - {row["input_tokens"] for row in best})
    now = datetime.now(PACIFIC)
    report = {"schema_version": 1, "prepared_at_pacific": now.strftime("%Y-%m-%d %H:%M:%S %Z"),
              "native_pool_start_confirmed": args.native_start_confirmed,
              "ready_for_publication": bool(args.native_start_confirmed and amendment and not open_directories and not missing_profiles),
              "hostname": identities[0]["hostname"], "slurm_job_id": identities[0]["slurm_job_id"],
              "pool_plan_sha256": digest((pool / "plan.json").read_bytes()),
              "server_identities": identities, "attempts": attempts, "rows": rows,
              "best_tested_points": best, "open_benchmark_directories": open_directories,
              "missing_accepted_input_profiles": missing_profiles,
              "archive": {"path": archive_path.relative_to(root).as_posix(), **archive},
              "frozen_benchmark_launcher_sha256": read(pool / "plan.json")["code_sha256"][str(pool / "benchmark_vllm_prompt_lengths.py")],
              "public_benchmark_launcher_sha256": digest((root / "scripts/benchmark_vllm_prompt_lengths.py").read_bytes()),
              "active_length_limits": amendment["endpoints"][0]["length_limits"] if amendment else None,
              "amendment_sha256": digest(args.amendment.read_bytes()) if args.amendment else None,
              "public_scope": "Serving execution and provenance only; no new biological scores or ETA inferred."}
    write_json(prefix.with_suffix(".json"), report)
    prefix.with_suffix(".md").write_text(markdown(report, os.path.relpath(archive_path, prefix.parent)))
    paths = list(PUBLIC_SOURCES) + args.extra_public_file + [str(prefix.with_suffix(ext).relative_to(root)) for ext in (".md", ".json")] + [archive_path.relative_to(root).as_posix()]
    paths = sorted(set(paths))
    hashes = {}
    for relative in paths:
        path = Path(relative)
        if path.is_absolute() or ".." in path.parts or not (root / path).is_file():
            raise ValueError("Missing or unsafe explicit publication source: " + relative)
        scanner.scan_file(root / path)
        hashes[relative] = digest((root / path).read_bytes())
    write_json(args.publication_manifest, {"baseline_commit": args.baseline_commit,
               "message": "Record measured shared vLLM capacity and preserve evaluation continuation provenance",
               "files": paths, "source_sha256": hashes, "ready_for_publication": report["ready_for_publication"],
               "prepared_at_pacific": report["prepared_at_pacific"],
               "publication_method": "Existing publish_continuation.py under the shared publication lock; explicit paths and upstream baseline protection; root confirms activation before publishing."})
    print(json.dumps({"report": str(prefix.with_suffix(".md")), "archive": str(archive_path),
                      "ready_for_publication": report["ready_for_publication"],
                      "best_tested_points": len(best), "open_benchmark_directories": open_directories}))


if __name__ == "__main__":
    main()
