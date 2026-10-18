#!/usr/bin/env python3
"""Add shared-pool provenance to native trajectory publication; never infer/score.

The frozen publisher is imported for validated registry, archive and Git helpers.
Its cycle, aggregation and report-generation functions are never called here.
All writers serialize through the existing evaluation publication lock.
"""

from __future__ import annotations

import argparse
from collections import Counter
from datetime import datetime
import fcntl
import gzip
import hashlib
import importlib.util
import io
import json
import os
from pathlib import Path
import re
import signal
import tarfile
import tempfile
import time
from zoneinfo import ZoneInfo


NATIVE_SHA256 = "a242714f8aecd8ab254b02e21639f5e3c014e22176d00000632a271d6160242b"
EXTRA_METADATA = ("shared_vllm_amendment.json", "shared_vllm_generation_completion.json", "shared_vllm_fork_manifest.json", "shared_vllm_scoring_output_lock.json", "native_scorer_invocation.json", "native_scorer.log")
STOP = False


def stamp():
    return datetime.now(ZoneInfo("America/Los_Angeles")).isoformat()


def read(path, default=None):
    return json.loads(Path(path).read_text()) if Path(path).is_file() else default


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def write(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name + ".tmp")
    temporary.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n")
    temporary.replace(path)


def module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    value = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(value)
    return value


def load_native(root):
    path = root / ".local/remaining_evaluations/pool_supervisor_final_v2.py"
    if sha(path) != NATIVE_SHA256:
        raise ValueError("Frozen native publisher changed")
    native = module("shared_artifact_native_helpers", path)
    # Defense against accidental future use of the frozen model/scorer hooks.
    def forbidden(*args, **kwargs):
        raise RuntimeError("This process may not aggregate, score or refresh reports")
    native.aggregate_ready = forbidden
    native.refresh_reports = forbidden
    return native


def copy_scanned(source, destination, scanner, expected=None):
    source, destination = Path(source), Path(destination)
    raw = source.read_bytes()
    actual = hashlib.sha256(raw).hexdigest()
    if expected is not None and actual != expected:
        raise ValueError("Pinned publication dependency changed: " + source.name)
    scanner.scan_bytes(raw)
    if destination.is_file() and sha(destination) == actual:
        return False
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_bytes(raw)
    return True


def add_scoring_views(runs):
    result = dict(runs)
    for name, spec in list(runs.items()):
        if spec["task_id"] not in {"P12", "P13", "P14", "P15"}:
            continue
        original = read(spec["config_path"], {})
        path = spec["project_root"] / "configs" / (name + "_shared_scoring.json")
        if not path.is_file():
            continue
        view = read(path)
        allowed = {"run_id", "runner", "frozen_files_sha256", "shared_vllm_scoring_view"}
        binding = view.get("shared_vllm_scoring_view", {})
        if (view.get("run_id") != name + "_shared_scoring" or binding.get("original_run_id") != name or binding.get("original_configuration_sha256") != sha(spec["config_path"]) or any(view.get(key) != original.get(key) for key in set(view) | set(original) if key not in allowed)):
            raise ValueError("Shared DeepFRI view changed the biological configuration")
        result[view["run_id"]] = {**spec, "run_id": view["run_id"], "folder": spec["project_root"] / "results/runs" / view["run_id"], "config_path": path, "kind": "full_test", "shared_scoring_view": True, "original_run_id": name}
    return result


def add_continuation_runs(runs, amendment):
    result = dict(runs)
    for logical_id, directory in amendment.get("continuation_run_directories", {}).items():
        original = runs[logical_id]
        folder = Path(directory).resolve()
        if folder.parent != original["folder"].resolve().parent or folder.name == logical_id or folder.name in result:
            raise ValueError("Continuation folder is duplicated or leaves the original result directory")
        result[folder.name] = {**original, "run_id": folder.name, "logical_run_id": logical_id, "folder": folder, "continuation_view": True}
        result[logical_id] = {**original, "retained_partial_source": True}
    return result


def generation_outcome(native, spec):
    folder = spec["folder"]
    sidecar = read(folder / "shared_vllm_amendment.json")
    if not sidecar:
        return native.outcome_status(spec)
    done = read(folder / "shared_vllm_generation_completion.json")
    if not done:
        return {"terminal": False, "generation_terminal": False, "execution_success": False, "native_metrics_valid": None, "actual_serving": "shared_vllm", "scoring_pending": True}
    if done.get("run_id") != spec.get("logical_run_id", spec["run_id"]) or done.get("planned") != spec["planned"] or done.get("amendment_sha256") != sidecar.get("amendment_sha256"):
        raise ValueError("Shared generation marker differs from its frozen run")
    success = done.get("generation_exit_code") == 0 and done.get("statuses", {}).get("completed") == spec["planned"]
    return {"terminal": True, "generation_terminal": True, "execution_success": success, "generation_exit_code": done.get("generation_exit_code"), "scoring_exit_code": None, "native_metrics_valid": None, "actual_serving": "shared_vllm", "generation_completion_sha256": sha(folder / "shared_vllm_generation_completion.json"), "scoring_pending": True}


def merge_index(existing, incoming):
    """Upgrade request-only slots once; never replace a saved output."""
    records = {row["filename"]: row for row in existing}
    if len(records) != len(existing):
        raise ValueError("Existing trajectory index contains duplicate filenames")
    for row in incoming:
        previous = records.get(row["filename"])
        if previous:
            if previous["request_sha256"] != row["request_sha256"]:
                raise ValueError("Previously published request bytes changed")
            if previous.get("response_sha256") is not None and previous["response_sha256"] != row.get("response_sha256"):
                raise ValueError("Previously published response bytes changed")
            if previous.get("response_sha256") is None and row.get("response_sha256") is not None:
                row = {**row, "previous_request_only_archive": {key: previous.get(key) for key in ("asset", "archive_sha256", "request_member")}}
        records[row["filename"]] = row
    return sorted(records.values(), key=lambda row: row["filename"])


def metadata_archive(files):
    output = io.BytesIO()
    with gzip.GzipFile(fileobj=output, mode="wb", filename="", mtime=0) as compressed:
        with tarfile.open(fileobj=compressed, mode="w|") as archive:
            for name, raw in sorted(files.items()):
                info = tarfile.TarInfo(name)
                info.size, info.mtime, info.mode = len(raw), 0, 0o644
                archive.addfile(info, io.BytesIO(raw))
    return output.getvalue()


def publish_dispatch(source, destination, index, scanner):
    groups, records = {}, []
    raw_groups = {row["filename"]: row.get("archive_sha256", "pending") for row in index}
    for path in sorted((source / "shared_vllm_dispatch").glob("*.json")):
        raw = path.read_bytes()
        scanner.scan_bytes(raw)
        data = json.loads(raw)
        if data.get("filename") != path.name:
            raise ValueError("Dispatch receipt filename differs from its case slot")
        group = raw_groups.get(path.name, "pending")
        groups.setdefault(group, {})["shared_vllm_dispatch/" + path.name] = raw
        records.append({"filename": path.name, "sha256": hashlib.sha256(raw).hexdigest(), "status": data.get("status"), "group": group, "member": "shared_vllm_dispatch/" + path.name})
    paths = {}
    changed = False
    for group, files in groups.items():
        signature = hashlib.sha256(json.dumps({name: hashlib.sha256(raw).hexdigest() for name, raw in sorted(files.items())}, sort_keys=True).encode()).hexdigest()
        relative = "shared_vllm_metadata_batches/" + ("pending" if group == "pending" else signature) + ".tar.gz"
        path = destination / relative
        raw = metadata_archive(files)
        if not path.is_file() or path.read_bytes() != raw:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(raw)
            scanner.scan_file(path)
            changed = True
        paths[group] = {"archive": relative, "archive_sha256": hashlib.sha256(raw).hexdigest()}
    for record in records:
        record.update(paths[record.pop("group")])
    if records:
        target = destination / "shared_vllm_dispatch_index.json"
        if read(target) != records:
            write(target, records)
            changed = True
    return changed


def publish_pins(root, sidecar, destination, scanner):
    amendment_path = Path(sidecar["amendment_path"])
    pins = [("infrastructure_amendment", amendment_path, sidecar["amendment_sha256"])]
    amendment = read(amendment_path)
    pins += [("adapter_code", Path(name), expected) for name, expected in amendment.get("adapter_files_sha256", {}).items()]
    for key in ("capacity_evidence_files", "negative_execution_receipts", "source_plans"):
        pins += [(key, (root / item["path"]).resolve(), item["sha256"]) for item in amendment.get(key, [])]
    context = amendment.get("run_context_checks", {}).get(sidecar["run_id"])
    if context:
        pins.append(("run_context_check", Path(context["path"]), context["sha256"]))
    pins += [("actual_server", Path(item["server_identity_file"]), item["server_identity_sha256"]) for item in amendment.get("endpoints", [])]
    manifest, changed = [], False
    for kind, source, expected in pins:
        source = source.resolve()
        if not source.is_relative_to(root) or source.suffix not in {".json", ".jsonl", ".py", ".md", ".sh", ".sbatch", ".csv", ".txt"} or scanner.secret_filename(Path(source.name)) or source.stat().st_size > 16 * 1024 * 1024:
            raise ValueError("Unsafe or oversized pinned infrastructure dependency: " + source.name)
        relative = "shared_infrastructure/" + expected + "-" + source.name
        changed |= copy_scanned(source, destination / relative, scanner, expected)
        manifest.append({"kind": kind, "source": str(source.relative_to(root)), "sha256": expected, "browsable_copy": relative})
    target = destination / "shared_infrastructure_manifest.json"
    if read(target) != manifest:
        write(target, manifest)
        changed = True
    return changed


def publish_dependencies(root, spec, destination, scanner):
    config = read(spec["config_path"])
    manifest, changed = {}, False
    for name, expected in config.get("frozen_files_sha256", {}).items():
        source = (spec["project_root"] / name).resolve()
        if not source.is_relative_to(root):
            raise ValueError("A frozen reproduction dependency leaves the workspace")
        copied = None
        if source.is_file() and source.suffix in {".py", ".json", ".md", ".txt", ".csv", ".sh"} and source.stat().st_size <= 16 * 1024 * 1024:
            copied = "shared_infrastructure/" + expected + "-" + source.name
            changed |= copy_scanned(source, destination / copied, scanner, expected)
        manifest[name] = {"expected_sha256": expected, "browsable_copy": copied}
    scoring_source = read(spec["folder"] / "source_shard_manifest.json", {})
    if scoring_source.get("adapter_file") and scoring_source.get("adapter_sha256"):
        source = Path(scoring_source["adapter_file"]).resolve()
        expected = scoring_source["adapter_sha256"]
        if not source.is_relative_to(root) or source.suffix != ".py":
            raise ValueError("Scoring adapter provenance leaves the reviewed workspace")
        copied = "shared_infrastructure/" + expected + "-" + source.name
        changed |= copy_scanned(source, destination / copied, scanner, expected)
        manifest["actual_scoring_adapter"] = {"expected_sha256": expected, "browsable_copy": copied}
    path = destination / "shared_frozen_dependencies_manifest.json"
    if read(path) != manifest:
        write(path, manifest)
        changed = True
    return changed


def pool_health(directory):
    state = read(directory / "status.json", {})
    time_value = state.get("updated_at") or state.get("updated_at_utc")
    age = None
    if time_value:
        parsed = datetime.fromisoformat(time_value.replace("Z", "+00:00"))
        age = max(0, datetime.now(parsed.tzinfo).timestamp() - parsed.timestamp())
    return {"directory": str(directory), "stage": state.get("stage", "not_started"), "status_age_seconds": age, "status_fresh": age is not None and age <= 180, "slurm_job_id": state.get("slurm_job_id"), "health_basis": "Read-only pool status metadata; no inference request or remote loopback probe."}


def check_staged_whitespace(native, staged):
    """Preserve pinned upstream whitespace while checking every other change.

    An exemption requires both the SHA256 encoded in the published dependency
    filename and the Git index blob to match its exact bytes. Generated metadata
    and edited source never receive this exemption.
    """
    result = native.git("diff", "--cached", "--check", allow_failure=True)
    if result.returncode == 0:
        return []
    failures = set()
    for line in result.stdout.splitlines():
        match = re.match(r"^(results/.+):[0-9]+: ", line)
        if match:
            failures.add(match.group(1))
    if not failures or not failures <= set(staged):
        raise ValueError("Git whitespace check failed outside the reviewed staged paths")
    index = {}
    for record in native.git("ls-files", "--stage", "-z", "--", *sorted(failures)).stdout.split("\0"):
        if record:
            metadata, relative = record.split("\t", 1)
            mode, oid, stage = metadata.split()
            if stage != "0":
                raise ValueError("Unmerged publication index entry")
            index[relative] = oid
    object_format = native.git("rev-parse", "--show-object-format").stdout.strip()
    for relative in sorted(failures):
        path = Path(relative)
        expected = path.name.split("-", 1)[0]
        if path.parent.name != "shared_infrastructure" or not re.fullmatch(r"[0-9a-f]{64}", expected):
            raise ValueError("Whitespace violation outside an immutable upstream dependency: " + relative)
        raw = (native.CHECKOUT / path).read_bytes()
        blob = b"blob " + str(len(raw)).encode() + b"\0" + raw
        if hashlib.sha256(raw).hexdigest() != expected or hashlib.new(object_format, blob).hexdigest() != index.get(relative):
            raise ValueError("Immutable whitespace exemption differs from its source or staged blob: " + relative)
    native.git("diff", "--cached", "--check", "--", ".", *[":(literal,exclude)" + name for name in sorted(failures)])
    return sorted(failures)


def publish_once(root, native, scanner, pool_directory, *, dry_run=False, amendment_path=None):
    registry = native.read(native.HERE / "supervisor_plan.json")
    plans, base = native.validate_registry(registry)
    amendment = read(amendment_path, {}) if amendment_path else {}
    if amendment and (amendment.get("kind") != "shared_vllm_infrastructure_amendment" or amendment.get("execution_authorized") is not True or amendment.get("scientific_protocol_changes") != []):
        raise ValueError("A protocol-preserving authorized amendment is required")
    runs = add_continuation_runs(add_scoring_views(base), amendment)
    # Retain every native registered run so this bridge also publishes original
    # aggregate score artifacts after the old uploader is eventually retired.
    selected = runs
    health = pool_health(pool_directory)
    if dry_run:
        # Exercise the same marker and pinned-dependency checks as publication.
        # Scratch copies leave the real checkout, Git history and links intact.
        with tempfile.TemporaryDirectory(prefix="shared-publication-preflight-") as scratch:
            for name, spec in selected.items():
                link, target = root / "results/runs" / name, spec["folder"].resolve()
                if (link.is_symlink() and link.resolve() != target) or (link.exists() and not link.is_symlink()):
                    raise ValueError("Central run link conflicts with publication source: " + name)
                destination = Path(scratch) / name
                generation_outcome(native, spec)
                publish_dependencies(root, spec, destination, scanner)
                sidecar = read(spec["folder"] / "shared_vllm_amendment.json")
                if sidecar:
                    publish_pins(root, sidecar, destination, scanner)
                for filename in (*native.METADATA, *EXTRA_METADATA):
                    source = spec["folder"] / filename
                    if source.is_file():
                        scanner.scan_file(source)
        return {"stage": "checked_without_publication", "selected_runs": list(selected), "shared_scoring_views": [name for name, spec in selected.items() if spec.get("shared_scoring_view")], "validated_pinned_dependencies": True, "pool_health": health, "generation_or_scoring_performed": False, "remote_mutation_performed": False}
    privacy = native.helpers.confirm_destination()
    native.ensure_run_links(runs)
    native.initialize(runs)
    runtime_relative = "results/shared_vllm_runtime/" + pool_directory.name
    native.git("sparse-checkout", "add", "--no-cone", "/" + runtime_relative + "/")
    snapshots, changed = {}, False
    release_record, assets = None, {}
    for name, spec in selected.items():
        source = spec["folder"]
        destination = native.CHECKOUT / "results/runs" / name
        index_path = destination / "trajectory_index.json"
        index = read(index_path, [])
        outcome = generation_outcome(native, spec)
        # An older terminal upload may contain a request-only slot that later
        # receives its first response after a proved no-execution drain.
        uploaded = {row["filename"] for row in index if row.get("response_sha256") is not None or not (source / "responses" / row["filename"]).is_file()}
        pending = native.new_trajectories(source, uploaded, outcome["terminal"])
        for offset in range(0, len(pending), 50):
            batch = pending[offset:offset + 50]
            for item in batch:
                for kind in ("request", "response"):
                    path = item.get(kind + "_path")
                    if path:
                        scanner.scan_file(path)
                        if sha(path) != item[kind + "_sha256"]:
                            raise ValueError("Raw artifact changed before archival")
            if release_record is None:
                release_record, assets = native.release()
            index = merge_index(index, native.archive_batch(name, batch, release_record, assets, destination))
            changed = True
        destination.mkdir(parents=True, exist_ok=True)
        if pending:
            write(index_path, index)
        changed |= copy_scanned(spec["config_path"], destination / "frozen_config.json", scanner)
        changed |= publish_dependencies(root, spec, destination, scanner)
        for filename in (*native.METADATA, *EXTRA_METADATA):
            if (source / filename).is_file():
                changed |= copy_scanned(source / filename, destination / filename, scanner)
        for path in (source / "shared_vllm_segments").glob("*.json"):
            changed |= copy_scanned(path, destination / "shared_vllm_segments" / path.name, scanner)
        sidecar = read(source / "shared_vllm_amendment.json")
        if sidecar:
            changed |= publish_pins(root, sidecar, destination, scanner)
        changed |= publish_dispatch(source, destination, index, scanner)
        statuses = Counter(row.get("status", "unknown") for row in index)
        kind = "full_test" if spec.get("shared_scoring_view") else "retained_partial_source" if spec.get("retained_partial_source") else "generation_source" if sidecar or spec.get("continuation_view") else spec["kind"]
        snapshot = {"task_id": spec["task_id"], "run_id": name, "logical_run_id": spec.get("logical_run_id", name), "kind": kind, "planned": spec["planned"], "uploaded_trajectories": len(index), "uploaded_saved_responses": sum(row.get("response_sha256") is not None for row in index), "response_status_counts": dict(statuses), "requests_saved": len(list((source / "requests").glob("*.json"))), "responses_saved": len(list((source / "responses").glob("*.json"))), **outcome, "github_url": "https://github.com/Some-random/bio-evaluation/tree/main/results/runs/" + name, "scored_benchmark_completed": outcome.get("native_metrics_valid") is True}
        snapshots[name] = snapshot
        if read(destination / "shared_vllm_upload_snapshot.json") != snapshot:
            write(destination / "shared_vllm_upload_snapshot.json", snapshot)
            changed = True
    runtime_destination = native.CHECKOUT / runtime_relative
    runtime_files = [pool_directory / name for name in ("plan.json", "status.json", "endpoints.json", "dispatch.json", "submission.json", "health_public.json", "health_plan.json")]
    runtime_files += list(pool_directory.glob("replica_*/server_identity.json"))
    runtime_files += list(pool_directory.glob("replica_*/length_benchmark/measured_concurrency_by_input_length.json"))
    runtime_files += list(pool_directory.glob("replica_*/length_benchmark/results.json"))
    if amendment_path:
        changed |= copy_scanned(amendment_path, runtime_destination / "infrastructure_amendment.json", scanner)
    for path in runtime_files:
        if path.is_file():
            changed |= copy_scanned(path, runtime_destination / path.relative_to(pool_directory), scanner)
    runtime_plan = read(pool_directory / "plan.json", {})
    code_pins = dict(runtime_plan.get("code_sha256", {}))
    code_pins.update(read(pool_directory / "health_plan.json", {}).get("code_files_sha256", {}))
    for name, expected in code_pins.items():
        path = Path(name).resolve()
        if not path.is_relative_to(root) or path.suffix not in {".py", ".json"}:
            raise ValueError("Runtime code dependency leaves the reviewed workspace")
        changed |= copy_scanned(path, runtime_destination / "frozen_files" / path.name, scanner, expected)
    owned = ["results/runs/" + name for name in selected] + [runtime_relative]
    existing_owned = [relative for relative in owned if (native.CHECKOUT / relative).exists()]
    if existing_owned:
        native.git("add", "-f", "--sparse", "--", *existing_owned)
    staged = native.git("diff", "--cached", "--name-only").stdout.splitlines()
    if any(not any(path.startswith(prefix + "/") for prefix in owned) for path in staged):
        raise ValueError("Publication checkout contains an unexpected staged path")
    if staged:
        check_staged_whitespace(native, staged)
        native.git("commit", "-m", "Publish shared vLLM generation provenance and native scoring views")
    ahead = int(native.git("rev-list", "--count", "refs/remotes/origin/main..HEAD").stdout.strip())
    if ahead:
        for attempt in range(8):
            native.helpers.confirm_destination()
            if native.git("push", "origin", "HEAD:refs/heads/main", allow_failure=True).returncode == 0:
                break
            native.git("fetch", "--filter=blob:none", "origin", "main")
            native.git("rebase", "FETCH_HEAD")
        else:
            raise RuntimeError("Shared artifact push did not complete")
    return {"stage": "watching", "updated_at_pacific": stamp(), "repository_visibility": privacy["visibility"], "destination_policy_sha256": privacy["destination_policy_sha256"], "commit_sha": native.git("rev-parse", "HEAD").stdout.strip(), "runs": snapshots, "pool_health": health, "publication_writer": "shared_vllm_additive_bridge_v1", "generation_or_scoring_performed": False, "original_uploader_untouched": True, "raw_saved_responses_are_not_benchmark_metrics": True}


def main():
    global STOP
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, required=True)
    parser.add_argument("--pool-directory", type=Path, required=True)
    parser.add_argument("--amendment", type=Path, help="Frozen dispatch amendment, including any separate continuation folders")
    parser.add_argument("--interval", type=int, default=60)
    parser.add_argument("--once", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    root = args.root.resolve()
    pool_directory = args.pool_directory.resolve()
    if not pool_directory.is_relative_to(root / ".local"):
        raise ValueError("Pool directory must remain inside this project's local state")
    if args.amendment and not args.amendment.resolve().is_relative_to(root / ".local"):
        raise ValueError("Dispatch amendment must remain inside the project's local state")
    state = root / ".local/shared_vllm_publication"
    state.mkdir(parents=True, exist_ok=True)
    native = load_native(root)
    scanner = module("shared_publication_secret_scanner", root / "scripts/daily_backup.py")
    def stop(signum, frame):
        global STOP
        STOP = True
    signal.signal(signal.SIGTERM, stop)
    signal.signal(signal.SIGINT, stop)
    with (state / "publisher.lock").open("a") as own_lock:
        fcntl.flock(own_lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        while not STOP:
            try:
                with (root / ".local/evaluation_publication.lock").open("a") as lock:
                    deadline = time.monotonic() + 45
                    while True:
                        try:
                            fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
                            break
                        except BlockingIOError:
                            if time.monotonic() >= deadline:
                                raise TimeoutError("Existing publication writer still owns the shared lock")
                            time.sleep(.25)
                    receipt = publish_once(root, native, scanner, pool_directory, dry_run=args.dry_run, amendment_path=args.amendment)
                receipt.update(pid=os.getpid(), gpu_allocation=0, ready=True)
            except Exception as error:
                detail = str(error)[:1000]
                try:
                    scanner.scan_bytes(detail.encode())
                except Exception:
                    detail = "Error detail withheld by credential scanner"
                receipt = {**read(state / "status.json", {}), "stage": "retry_pending", "ready": False, "last_retry_at_pacific": stamp(), "error_type": type(error).__name__, "error_message": detail, "generation_or_scoring_performed": False}
            write(state / "status.json", receipt)
            print(json.dumps({key: receipt.get(key) for key in ("stage", "ready", "commit_sha", "error_type", "error_message")}), flush=True)
            if args.once or args.dry_run:
                return 0 if receipt["ready"] else 1
            for _ in range(max(1, args.interval)):
                if STOP:
                    break
                time.sleep(1)


if __name__ == "__main__":
    raise SystemExit(main())
