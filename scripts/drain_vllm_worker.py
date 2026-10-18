#!/usr/bin/env python3
"""Drain buffered completions before terminating one explicitly identified worker.

Only an explicit commit kills processes. Before that irreversible boundary,
every failure resumes the original processes. New request-only files are proved
unexecuted by stopping, then killing, the API before the client can be killed or
Slurm can resume either process. Terminal accounting is a separate final step.
"""

from __future__ import annotations

import argparse
from datetime import datetime
import hashlib
import ipaddress
import json
import os
from pathlib import Path
import signal
import subprocess
import time
from urllib.parse import urlsplit
from urllib.request import ProxyHandler, build_opener
from zoneinfo import ZoneInfo


PROOF_FIELDS = ("api_stopped_before_new_requests", "api_killed_while_stopped", "api_dead_before_client_kill", "api_dead_before_job_cancellation", "client_killed_while_stopped", "all_pre_stop_requests_paired", "executor_stopped_before_client_stop", "executor_stopped_until_client_killed", "executor_killed_while_stopped", "executor_killed_after_client_dead")
TERMINAL = {"COMPLETED", "FAILED", "CANCELLED", "TIMEOUT", "OUT_OF_MEMORY", "NODE_FAIL", "PREEMPTED", "BOOT_FAIL", "DEADLINE", "REVOKED"}


def now():
    return datetime.now(ZoneInfo("America/Los_Angeles")).isoformat()


def digest(value):
    return hashlib.sha256(json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def file_digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name + ".tmp")
    temporary.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n")
    temporary.chmod(0o600)
    temporary.replace(path)


def process(pid):
    try:
        folder = Path("/proc") / str(pid)
        tail = (folder / "stat").read_text().rsplit(")", 1)[1].split()
        return {"pid": pid, "parent_pid": int(tail[1]), "state": tail[0], "start_ticks": int(tail[19]), "uid": folder.stat().st_uid}
    except (FileNotFoundError, ProcessLookupError):
        return None


def verify_process(pid, start_ticks, stopped=None):
    value = process(pid)
    if not value or value["start_ticks"] != start_ticks or value["state"] == "Z" or value["uid"] != os.geteuid():
        raise ValueError(f"Process identity changed or is not an owned live process: {pid}")
    if stopped is not None and (value["state"] in {"T", "t"}) != stopped:
        raise ValueError(f"Unexpected stopped state for process {pid}: {value['state']}")
    return value


def change_state(pid, ticks, operation, stopped):
    verify_process(pid, ticks)
    os.kill(pid, operation)
    deadline = time.monotonic() + 3
    while time.monotonic() < deadline:
        value = verify_process(pid, ticks)
        if (value["state"] in {"T", "t"}) == stopped:
            return
        time.sleep(.01)
    raise TimeoutError(f"Process {pid} did not reach the requested stop state")


def dead(pid, ticks):
    value = process(pid)
    return value is None or value["start_ticks"] != ticks or value["state"] == "Z"


def kill_stopped(pid, ticks):
    verify_process(pid, ticks, stopped=True)
    os.kill(pid, signal.SIGKILL)
    deadline = time.monotonic() + 5
    while time.monotonic() < deadline:
        if dead(pid, ticks):
            return
        time.sleep(.01)
    raise TimeoutError(f"SIGKILL did not retire stopped process {pid}")


def listener_owned(pid, port):
    inodes = set()
    for path in (Path("/proc") / str(pid) / "fd").iterdir():
        try:
            link = os.readlink(path)
            if link.startswith("socket:["):
                inodes.add(link[8:-1])
        except FileNotFoundError:
            pass
    for name in ("tcp", "tcp6"):
        for line in (Path("/proc") / str(pid) / "net" / name).read_text().splitlines()[1:]:
            fields = line.split()
            if len(fields) > 9 and fields[3] == "0A" and int(fields[1].rsplit(":", 1)[1], 16) == port and fields[9] in inodes:
                return True
    return False


def endpoint(value):
    parsed = urlsplit(value)
    try:
        local = parsed.hostname == "localhost" or ipaddress.ip_address(parsed.hostname or "").is_loopback
    except ValueError:
        local = False
    if parsed.scheme != "http" or not local or parsed.username or parsed.password or parsed.query or parsed.fragment or parsed.path.rstrip("/") not in ("", "/v1"):
        raise ValueError("Only credential-free loopback HTTP endpoints are accepted")
    return value.rstrip("/").removesuffix("/v1"), parsed.port or 80


def metrics(base_url):
    opener = build_opener(ProxyHandler({}))
    with opener.open(base_url + "/metrics", timeout=5) as response:
        raw = response.read().decode()
    values = {"running": [], "waiting": []}
    for line in raw.splitlines():
        if not line or line.startswith("#"):
            continue
        metric, value = line.rsplit(None, 1)
        name = metric.split("{", 1)[0]
        if name == "vllm:num_requests_running":
            values["running"].append(float(value))
        if name == "vllm:num_requests_waiting":
            values["waiting"].append(float(value))
    if not values["running"] or not values["waiting"]:
        raise ValueError("Required vLLM request queue metrics are unavailable")
    return {"captured_at": now(), "running": sum(values["running"]), "waiting": sum(values["waiting"])}


def accounting(job_id):
    raw = subprocess.check_output(["sacct", "-n", "-P", "-j", str(job_id), "--format=JobIDRaw,State,ExitCode"], text=True, timeout=30)
    for line in raw.splitlines():
        fields = line.strip().split("|")
        if len(fields) >= 3 and fields[0] == str(job_id):
            return {"job_id": str(job_id), "state": fields[1].split()[0].rstrip("+"), "exit_code": fields[2], "captured_at": now()}
    raise ValueError("No exact parent-job accounting row was returned")


def names(folder):
    return {path.name for path in folder.glob("*.json")}


def request_record(args, filename):
    path = args.run_directory / "requests" / filename
    data = json.loads(path.read_text())
    payload_hash = digest(data["payload"])
    if data.get("request_sha256") != payload_hash:
        raise ValueError("Saved request payload hash does not match its record: " + filename)
    return {"project_root": str(args.project_root.resolve()), "run_id": args.run_id, "filename": filename, "request_file_sha256": file_digest(path), "payload_sha256": payload_hash}


def paired(args, filename):
    response_path = args.run_directory / "responses" / filename
    if not response_path.is_file():
        return False
    request = request_record(args, filename)
    response = json.loads(response_path.read_text())
    if response.get("request_sha256") != request["payload_sha256"]:
        raise ValueError("Response is not paired with the exact saved request: " + filename)
    return True


def drain(args, query_accounting=accounting):
    if not args.commit_after_drain:
        raise ValueError("--commit-after-drain is required; no process has been signaled")
    base_url, port = endpoint(args.base_url)
    args.run_directory = args.run_directory.resolve()
    if not (args.run_directory / "requests").is_dir() or not (args.run_directory / "responses").is_dir():
        raise ValueError("Run directory must contain requests/ and responses/")
    if args.receipt.exists():
        raise ValueError("Refusing to replace an existing receipt")
    if len({args.client_pid, args.api_pid, args.executor_pid, os.getpid()}) != 4:
        raise ValueError("Client, executor, API and drain helper must be distinct processes")
    client_identity = verify_process(args.client_pid, args.client_start_ticks, stopped=False)
    api_identity = verify_process(args.api_pid, args.api_start_ticks, stopped=False)
    executor_identity = verify_process(args.executor_pid, args.executor_start_ticks, stopped=False)
    if client_identity["parent_pid"] != args.executor_pid:
        raise ValueError("The supplied executor must be the client's direct parent that can automatically score after exit")
    if not listener_owned(args.api_pid, port):
        raise ValueError("The supplied API process does not own this listening port")
    before_accounting = query_accounting(args.old_job_id)
    if before_accounting["state"] != "RUNNING":
        raise ValueError("Old job must still be RUNNING before any process signal")
    receipt = {"schema_version": 1, "kind": "shared_vllm_negative_execution_drain", "drain_protocol_version": 2, "stage": "starting", "old_job_id": str(args.old_job_id), "run_directory": str(args.run_directory), "project_root": str(args.project_root.resolve()), "run_id": args.run_id, "created_at": now(), "client_identity": client_identity, "api_identity": api_identity, "executor_identity": executor_identity, "initial_accounting": before_accounting, "proof": {"client_pid": args.client_pid, "client_start_ticks": args.client_start_ticks, "api_pid": args.api_pid, "api_start_ticks": args.api_start_ticks, "executor_pid": args.executor_pid, "executor_start_ticks": args.executor_start_ticks, **{field: False for field in PROOF_FIELDS}}, "request_records": [], "drain_metrics": []}
    api_kill_started = False
    try:
        # Native wrappers run their scorer after subprocess.run(client) returns.
        # Freeze that wrapper before touching the child, including its failure
        # path; killing only the child would otherwise score an incomplete run.
        change_state(args.executor_pid, args.executor_start_ticks, signal.SIGSTOP, True)
        receipt["proof"]["executor_stopped_before_client_stop"] = True
        change_state(args.client_pid, args.client_start_ticks, signal.SIGSTOP, True)
        requests_before = names(args.run_directory / "requests")
        responses_before = names(args.run_directory / "responses")
        if not responses_before <= requests_before:
            raise ValueError("Orphan response files prevent a complete pairing proof")
        outstanding = requests_before - responses_before
        first_metrics = metrics(base_url)
        receipt["drain_metrics"].append(first_metrics)
        if len(outstanding) != args.expected_inflight or first_metrics["running"] != len(outstanding) or first_metrics["waiting"] != 0:
            raise ValueError("Outstanding saved requests do not exactly equal the expected running server requests with an empty wait queue")
        pre_stop_records = [request_record(args, name) for name in sorted(outstanding)]
        receipt.update(stage="client_stopped_waiting_for_engine_idle", pre_stop_outstanding_records=pre_stop_records, pre_stop_request_filenames=sorted(requests_before))
        write(args.receipt, receipt)
        deadline, idle_since = time.monotonic() + args.drain_timeout, None
        while time.monotonic() < deadline:
            verify_process(args.executor_pid, args.executor_start_ticks, stopped=True)
            verify_process(args.client_pid, args.client_start_ticks, stopped=True)
            sample = metrics(base_url)
            receipt["drain_metrics"].append(sample)
            if sample["waiting"] != 0:
                raise ValueError("Unexpected queued request while the client is stopped")
            if sample["running"] == 0:
                idle_since = idle_since or time.monotonic()
                if time.monotonic() - idle_since >= args.idle_seconds:
                    break
            else:
                idle_since = None
            time.sleep(args.poll_interval)
        else:
            raise TimeoutError("The stopped client's running requests did not drain")
        change_state(args.api_pid, args.api_start_ticks, signal.SIGSTOP, True)
        receipt["api_stopped_at"] = now()
        receipt["proof"]["api_stopped_before_new_requests"] = True
        if names(args.run_directory / "requests") != requests_before:
            raise ValueError("Request files changed while the only client was stopped")
        change_state(args.client_pid, args.client_start_ticks, signal.SIGCONT, False)
        deadline = time.monotonic() + args.flush_timeout
        while time.monotonic() < deadline:
            verify_process(args.executor_pid, args.executor_start_ticks, stopped=True)
            verify_process(args.api_pid, args.api_start_ticks, stopped=True)
            if all(paired(args, name) for name in outstanding):
                break
            time.sleep(args.poll_interval)
        else:
            raise TimeoutError("Buffered pre-stop completions were not saved in time")
        change_state(args.client_pid, args.client_start_ticks, signal.SIGSTOP, True)
        if not all(paired(args, name) for name in requests_before):
            raise ValueError("Some pre-stop requests remain unpaired")
        for original in pre_stop_records:
            if request_record(args, original["filename"]) != original:
                raise ValueError("A pre-stop saved request changed during drain")
        receipt["proof"]["all_pre_stop_requests_paired"] = True
        post_stop = names(args.run_directory / "requests") - requests_before
        if post_stop & names(args.run_directory / "responses"):
            raise ValueError("A post-stop request already has an output; preserve it and inspect without replay")
        receipt["request_records"] = [{**request_record(args, name), "request_created_after_api_stop": True, "server_stopped_at_creation": True, "creation_proof": "Absent from the frozen request filename set before API stop; created only after the stopped API was verified and the client resumed."} for name in sorted(post_stop)]
        receipt.update(stage="verified_both_processes_stopped_before_commit", buffered_completions_saved=len(outstanding), pending_unexecuted_requests=len(post_stop), updated_at=now())
        write(args.receipt, receipt)
        verify_process(args.executor_pid, args.executor_start_ticks, stopped=True)
        verify_process(args.client_pid, args.client_start_ticks, stopped=True)
        # SIGKILL itself is the irreversible boundary, even if observing the
        # process's death subsequently fails. Never resume a client after it.
        api_kill_started = True
        kill_stopped(args.api_pid, args.api_start_ticks)
        receipt["proof"].update(api_killed_while_stopped=True, api_dead_before_client_kill=True)
        receipt["api_killed_at"] = now()
        still_running = query_accounting(args.old_job_id)
        receipt["accounting_after_api_kill_before_client_kill"] = still_running
        if still_running["state"] != "RUNNING":
            raise ValueError("Job was not confirmed RUNNING after API death and before client kill")
        receipt["proof"]["api_dead_before_job_cancellation"] = True
        write(args.receipt, receipt)
        verify_process(args.executor_pid, args.executor_start_ticks, stopped=True)
        kill_stopped(args.client_pid, args.client_start_ticks)
        receipt["proof"]["client_killed_while_stopped"] = True
        verify_process(args.executor_pid, args.executor_start_ticks, stopped=True)
        receipt["proof"]["executor_stopped_until_client_killed"] = True
        kill_stopped(args.executor_pid, args.executor_start_ticks)
        receipt["proof"].update(executor_killed_while_stopped=True, executor_killed_after_client_dead=True)
        receipt.update(stage="drained_processes_killed_waiting_job_terminal", client_killed_at=now(), updated_at=now())
        write(args.receipt, receipt)
        return receipt
    except BaseException as error:
        if not api_kill_started:
            for pid, ticks in ((args.api_pid, args.api_start_ticks), (args.client_pid, args.client_start_ticks), (args.executor_pid, args.executor_start_ticks)):
                if not dead(pid, ticks):
                    os.kill(pid, signal.SIGCONT)
            receipt["stage"] = "failed_rolled_back_original_processes"
        else:
            # Resuming a client against an irreversibly killed API would turn
            # proved pending slots into transport-error outputs. Leave it held.
            receipt["stage"] = "commit_failed_api_kill_started_client_held_for_recovery"
        receipt.update(error=f"{type(error).__name__}: {error}", updated_at=now())
        write(args.receipt, receipt)
        raise


def finalize(path, query_accounting=accounting):
    receipt = json.loads(path.read_text())
    if receipt.get("kind") != "shared_vllm_negative_execution_drain" or receipt.get("stage") != "drained_processes_killed_waiting_job_terminal" or not all(receipt.get("proof", {}).get(field) is True for field in PROOF_FIELDS):
        raise ValueError("Only an intact committed drain can be finalized")
    terminal = query_accounting(receipt["old_job_id"])
    if terminal["state"] not in TERMINAL:
        raise ValueError("The exact original Slurm job is not terminal")
    receipt["prepared_receipt_sha256"] = file_digest(path)
    receipt.update(stage="drained_and_job_terminal", terminal_accounting=terminal, finalized_at=now())
    write(path, receipt)
    return receipt


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    run = commands.add_parser("drain")
    for name in ("client-pid", "client-start-ticks", "api-pid", "api-start-ticks", "executor-pid", "executor-start-ticks"):
        run.add_argument("--" + name, required=True, type=int)
    for name in ("run-directory", "project-root", "receipt"):
        run.add_argument("--" + name, required=True, type=Path)
    for name in ("run-id", "old-job-id", "base-url"):
        run.add_argument("--" + name, required=True)
    run.add_argument("--expected-inflight", type=int, default=4)
    run.add_argument("--drain-timeout", type=float, default=1200)
    run.add_argument("--flush-timeout", type=float, default=20)
    run.add_argument("--idle-seconds", type=float, default=1)
    run.add_argument("--poll-interval", type=float, default=.1)
    run.add_argument("--commit-after-drain", action="store_true")
    finish = commands.add_parser("finalize")
    finish.add_argument("--receipt", type=Path, required=True)
    args = parser.parse_args()
    receipt = drain(args) if args.command == "drain" else finalize(args.receipt)
    print(json.dumps({"stage": receipt["stage"], "old_job_id": receipt["old_job_id"], "negative_execution_records": len(receipt["request_records"]), "receipt": str(args.receipt), "sha256": file_digest(args.receipt)}, indent=2))


if __name__ == "__main__":
    main()
