#!/usr/bin/env python3
"""Publish generated reports to the explicitly authorized repository visibility.

This watcher refreshes metadata and presentation only. It never scores runs,
reads benchmark cases, submits work, or uses the trajectory uploader's checkout.
"""
from __future__ import annotations

import argparse
from contextlib import contextmanager
from datetime import datetime, timezone
import fcntl
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import subprocess
import re
import sys
import tempfile
import time


OWNED = (
    "reports/EVALUATION_PROGRESS.json",
    "reports/TASK_HIERARCHY_DATA.json",
    "reports/EVALUATION_OVERVIEW.md",
    "reports/WORKED_EXAMPLES.md",
    "reports/TASK_HIERARCHY_COMPLETE.md",
    "reports/RESULTS_GROUPED.md",
    "reports/ARCHIVED_EVALUATIONS.md",
    "reports/TASK_COVERAGE_MAP.csv",
)
SCORE_PAIR = ("reports/RESULTS_AT_A_GLANCE.md", "reports/RESULTS_AT_A_GLANCE.json")


class ReportingError(RuntimeError):
    """An upload failure with a safe, credential-free explanation."""


def module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result


def stamp():
    return datetime.now(timezone.utc).isoformat()


@contextmanager
def publication_lock(root):
    path = Path(root) / ".local/evaluation_publication.lock"
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a") as handle:
        fcntl.flock(handle, fcntl.LOCK_EX)
        yield


def original_publication_backlog(root, now=None):
    path = Path(root) / ".local/remaining_evaluations/supervisor_status.json"
    if not path.is_file():
        return None
    try:
        value = json.loads(path.read_bytes())
        updated = datetime.fromisoformat(value["updated_at_utc"].replace("Z", "+00:00"))
        age = ((now or datetime.now(timezone.utc)) - updated).total_seconds()
    except (KeyError, TypeError, ValueError, OSError):
        return None
    error = str(value.get("error", "")).lower()
    if (value.get("stage") == "retry_pending" and 0 <= age <= 1800
            and ("non-fast-forward" in error or "fetch first" in error)):
        return {"stage": "retry_pending", "updated_at_utc": value["updated_at_utc"],
                "reason": "Original trajectory publisher is catching up with main"}
    return None


def publication_fingerprint(snapshot):
    """Ignore clock-only refreshes while retaining results, errors and layout."""
    volatile = {"generatedAt", "updatedAt", "updated_at_utc", "scoreSnapshotAt", "runSnapshotAt", "snapshotAt"}
    def clean(value):
        if isinstance(value, list):
            return [clean(item) for item in value]
        if not isinstance(value, dict):
            return value
        result = {}
        for key, item in value.items():
            if key in volatile:
                continue
            if key == "sourceHashes" and isinstance(item, dict):
                item = {name: checksum for name, checksum in item.items()
                        if not name.startswith(".local/") and not name.endswith("/upload_status.json")
                        and name != "reports/EVALUATION_PROGRESS.json"}
            result[key] = clean(item)
        return result
    normalized = {}
    for name, raw in snapshot.items():
        if name.endswith(".json"):
            try:
                normalized[name] = clean(json.loads(raw))
                continue
            except (ValueError, UnicodeDecodeError):
                pass
        text = raw.decode(errors="replace")
        if name.endswith(".md"):
            text = re.sub(r"\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d(?:\.\d+)?(?:Z|[+-]\d\d:\d\d)", "<snapshot-time>", text)
            text = re.sub(r"\d{4}-\d\d-\d\d \d\d:\d\d(?:[:]\d\d)? (?:UTC|PST|PDT)", "<snapshot-time>", text)
        normalized[name] = text
    return sha(json.dumps(normalized, sort_keys=True, ensure_ascii=False, separators=(",", ":")).encode())


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def atomic_json(path, value):
    raw = (json.dumps(value, indent=2, allow_nan=False) + "\n").encode()
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = None
    try:
        with tempfile.NamedTemporaryFile(dir=path.parent, prefix="." + path.name + ".", delete=False) as handle:
            temporary = Path(handle.name)
            handle.write(raw)
            handle.flush()
            os.fsync(handle.fileno())
        temporary.chmod(0o600)
        temporary.replace(path)
    finally:
        if temporary is not None and temporary.exists():
            temporary.unlink()


class Publisher:
    def __init__(self, root, include_score_reports=False, helper=None, scanner=None, runner=None):
        self.root = Path(root).resolve()
        self.state = self.root / ".local/reporting_updater"
        self.checkout = self.state / "upload_checkout"
        self.status_path = self.state / "status.json"
        self.paths = OWNED + (SCORE_PAIR if include_score_reports else ())
        self.helper = helper or module("reporting_git_helpers", self.root / ".local/litqa2_replay/incremental_upload.py")
        self.scanner = scanner or module("reporting_secret_scanner", self.root / "scripts/daily_backup.py")
        self.runner = runner or self.command
        self.receipt = json.loads(self.status_path.read_text()) if self.status_path.is_file() else {}
        previous_paths = self.receipt.get("ownedPaths")
        if previous_paths is not None and previous_paths != list(self.paths):
            raise ReportingError("Owned report paths changed; a reviewed baseline migration is required")
        self.baseline = self.receipt.get("baselineBlobs")
        self.state.mkdir(parents=True, exist_ok=True)

    def git(self, *args, allow_failure=False):
        try:
            result = self.helper.git(*args, cwd=self.checkout, allow_failure=allow_failure)
        except Exception as error:
            raise ReportingError("Git operation failed: " + args[0]) from error
        if result.returncode and not allow_failure:
            raise ReportingError("Git operation failed: " + args[0])
        return result

    def privacy(self):
        try:
            privacy = self.helper.confirm_destination()
        except Exception as error:
            raise ReportingError("Authorized repository visibility and push permission could not be verified") from error
        if privacy.get("publication_authorized") is not True or privacy.get("push_permission") is not True:
            raise ReportingError("Authorized repository and push permission were not verified")
        return privacy

    def save(self, **values):
        self.receipt.update(values)
        self.receipt.update(updatedAt=stamp(), ownedPaths=list(self.paths), baselineBlobs=self.baseline)
        atomic_json(self.status_path, self.receipt)

    def command(self, argv):
        result = subprocess.run(argv, cwd=self.root, text=True, stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE)
        if result.returncode:
            raise ReportingError("Generated report command/check failed: " + Path(argv[1]).name)

    def refresh_and_check(self):
        refresh = [sys.executable, str(self.root / "scripts/refresh_evaluation_reporting.py"), "--root", str(self.root)]
        render = [sys.executable, str(self.root / "scripts/update_grouped_evaluation_reports.py")]
        self.runner(refresh)
        self.runner(render)
        self.runner(refresh + ["--check"])
        self.runner(render + ["--check"])

    def read_snapshot(self):
        result = {}
        for name in self.paths:
            path = self.root / name
            if path.is_symlink() or not path.is_file() or not path.resolve().is_relative_to(self.root / "reports"):
                raise ReportingError("An owned report is absent or is not a regular report file: " + name)
            result[name] = path.read_bytes()
        # Check consistency after reading as well: the score publisher can finish
        # a task while the renderer is working. Such a cycle is retried intact.
        self.runner([sys.executable, str(self.root / "scripts/refresh_evaluation_reporting.py"),
                     "--root", str(self.root), "--check"])
        self.runner([sys.executable, str(self.root / "scripts/update_grouped_evaluation_reports.py"), "--check"])
        if any((self.root / name).read_bytes() != raw for name, raw in result.items()):
            raise ReportingError("Generated reports changed while taking their snapshot")
        if SCORE_PAIR[0] in result:
            report = json.loads(result[SCORE_PAIR[1]])
            catalog = json.loads(result["reports/TASK_HIERARCHY_DATA.json"])
            source_hash = catalog["meta"].get("sourceHashes", {}).get(SCORE_PAIR[1])
            display = module("reporting_score_pair_display", self.root / "scripts/update_results_at_a_glance.py")
            if source_hash != sha(result[SCORE_PAIR[1]]) or display.render_markdown(report).encode() != result[SCORE_PAIR[0]]:
                raise ReportingError("Optional score report pair does not match the validated source snapshot")
        return result

    def initialize(self):
        if not (self.checkout / ".git").is_dir():
            if self.checkout.exists() and any(self.checkout.iterdir()):
                raise ReportingError("Reserved reporting checkout is not empty")
            self.checkout.mkdir(parents=True, exist_ok=True)
            self.git("init", "--quiet")
            self.git("remote", "add", "origin", self.helper.URL)
            self.git("config", "remote.origin.promisor", "true")
            self.git("config", "remote.origin.partialclonefilter", "blob:none")
            self.git("sparse-checkout", "init", "--no-cone")
        elif self.git("remote", "get-url", "origin").stdout.strip() != self.helper.URL:
            raise ReportingError("Reporting checkout origin differs from the verified destination")
        self.git("sparse-checkout", "set", "--no-cone", *["/" + path for path in self.paths])
        for name, fallback in [("user.name", "Codex"), ("user.email", "codex@localhost")]:
            self.git("config", name, fallback)
        self.git("fetch", "--filter=blob:none", "origin", "main")
        # This directory is exclusively disposable publication state. The root
        # working tree and the running trajectory checkout are never reset.
        self.git("checkout", "--detach", "--force", "FETCH_HEAD")

    def remote_blobs(self):
        result = dict.fromkeys(self.paths)
        output = self.git("ls-tree", "-z", "FETCH_HEAD", "--", *self.paths).stdout
        for entry in output.split("\0"):
            if not entry:
                continue
            metadata, name = entry.split("\t", 1)
            mode, kind, blob = metadata.split()
            if mode not in {"100644", "100755"} or kind != "blob":
                raise ReportingError("Owned upstream report is not a regular blob: " + name)
            result[name] = blob
        return result

    def guard_ownership(self, remote, desired):
        changed = [name for name in self.paths if remote[name] != self.baseline.get(name)
                   and remote[name] != desired[name]]
        if changed:
            raise ReportingError("Upstream edits changed owned reports; publication stopped: " + ", ".join(changed))

    def publish_once(self):
        self.refresh_and_check()
        snapshot = self.read_snapshot()
        with publication_lock(self.root):
            backlog = original_publication_backlog(self.root)
            if backlog:
                self.save(stage="yielding_to_trajectory_publication", pushed=False, changedPaths=[],
                          deferredForOriginalSupervisor=backlog, error=None)
                return self.receipt
            return self.publish_snapshot(snapshot)

    def publish_snapshot(self, snapshot):
        privacy = self.privacy()
        self.initialize()
        remote = self.remote_blobs()
        remote_snapshot = {name: (self.checkout / name).read_bytes() for name in self.paths
                           if (self.checkout / name).is_file()}
        if self.baseline is None:
            # Initial ownership of exactly these generated artifacts is an
            # explicit setup decision; future upstream edits are guarded.
            self.baseline = remote.copy()
            self.save(stage="baseline_initialized", baselineInitializedAt=stamp())
        desired = {}
        for name, raw in snapshot.items():
            destination = self.checkout / name
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_bytes(raw)
            try:
                self.scanner.scan_file(destination)
            except Exception as error:
                raise ReportingError("Selected report failed the credential scan: " + name) from error
            desired[name] = self.git("hash-object", str(destination)).stdout.strip()
        self.guard_ownership(remote, desired)
        if publication_fingerprint(snapshot) == publication_fingerprint(remote_snapshot):
            self.baseline = remote.copy()
            self.save(stage="watching", pushed=False, changedPaths=[],
                      metadataOnlyRefreshSkipped=True, deferredForOriginalSupervisor=None,
                      sourceHashes={name: sha(raw) for name, raw in remote_snapshot.items()},
                      observedSourceHashes={name: sha(raw) for name, raw in snapshot.items()},
                      privacy=privacy, error=None)
            return self.receipt
        self.git("add", "--sparse", "-f", "--", *self.paths)
        staged = self.git("diff", "--cached", "--name-only").stdout.splitlines()
        if any(name not in self.paths for name in staged):
            raise ReportingError("Staged paths exceed reporting ownership")
        pushed = False
        if staged:
            self.git("commit", "-m", "Refresh evaluation overview and progress")
            for attempt in range(5):
                privacy = self.privacy()
                result = self.git("push", "origin", "HEAD:refs/heads/main", allow_failure=True)
                if result.returncode == 0:
                    pushed = True
                    break
                self.git("fetch", "--filter=blob:none", "origin", "main")
                self.guard_ownership(self.remote_blobs(), desired)
                result = self.git("rebase", "FETCH_HEAD", allow_failure=True)
                if result.returncode:
                    self.git("rebase", "--abort", allow_failure=True)
                    raise ReportingError("Concurrent upstream changes could not be rebased safely")
            if not pushed:
                raise ReportingError("Concurrent GitHub updates prevented publication after five attempts")
        commit = self.git("rev-parse", "HEAD").stdout.strip()
        self.baseline = desired
        progress = json.loads(snapshot["reports/EVALUATION_PROGRESS.json"])
        self.save(stage="watching", commitSha=commit, pushed=pushed, changedPaths=staged,
            metadataOnlyRefreshSkipped=False, deferredForOriginalSupervisor=None,
            sourceHashes={name: sha(raw) for name, raw in snapshot.items()}, privacy=privacy,
            scoreSnapshotAt=progress.get("scoreSnapshotAt"), runSnapshotAt=progress.get("runSnapshotAt"),
            heartbeat=progress.get("heartbeat"), totals=progress.get("totals"),
            error=None)
        return self.receipt

    def cycle(self):
        try:
            return self.publish_once()
        except Exception as error:
            # Never store credential helper exceptions or captured subprocess
            # stderr in the receipt. Only our own safe explanations are copied.
            safe = str(error) if isinstance(error, ReportingError) else "Reporting metadata update failed (" + type(error).__name__ + ")"
            self.save(stage="retry_pending", error=safe)
            raise


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--once", action="store_true")
    parser.add_argument("--interval", type=int, default=300)
    parser.add_argument("--include-score-reports", action="store_true", help="Also own and publish the validated, consistent score Markdown/JSON pair")
    args = parser.parse_args()
    if args.interval < 1:
        parser.error("--interval must be positive")
    state = args.root.resolve() / ".local/reporting_updater"
    state.mkdir(parents=True, exist_ok=True)
    with (state / "watcher.lock").open("a") as lock:
        fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        publisher = Publisher(args.root, args.include_score_reports)
        while True:
            try:
                receipt = publisher.cycle()
                print(json.dumps({key: receipt.get(key) for key in ["stage", "updatedAt", "commitSha", "pushed"]}), flush=True)
                failed = False
            except Exception:
                print(json.dumps({"stage": "retry_pending", "statusPath": str(publisher.status_path)}), flush=True)
                failed = True
            if args.once:
                return 1 if failed else 0
            # Short sleeps keep termination and interactive steering responsive.
            for _ in range(args.interval):
                time.sleep(1)


if __name__ == "__main__":
    raise SystemExit(main())
