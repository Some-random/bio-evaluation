"""One-time private workspace backup with model references only by default.

No inference and no schedule changes. Reuses the existing GitHub login and proxy.
Credentials/environments/caches are excluded. Public weights stay local unless
checkpoint release upload is explicitly enabled in the backup configuration.
"""
import concurrent.futures as cf
import datetime as dt
import fcntl
import hashlib
import io
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import tarfile
import tempfile
import threading
import time

import daily_backup as backup

ROOT = Path(__file__).resolve().parents[1]
STATE = ROOT / ".local/github_upload"
PART_BYTES = 512 * 1024 * 1024
TAG = "snapshot-2026-10-15"
PROGRESS_LOCK = threading.Lock()
PROGRESS = {}


def write_json(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(value, indent=2) + "\n")
    tmp.chmod(0o600)
    tmp.replace(path)


def status(**values):
    with PROGRESS_LOCK:
        PROGRESS.update(values, updated_at_utc=dt.datetime.now(dt.timezone.utc).isoformat())
        write_json(STATE / "progress.json", PROGRESS)
        print(json.dumps(PROGRESS), flush=True)


def checked(args, timeout=180):
    return backup.checked(args, timeout=timeout)


def api(path, method=None):
    args = ["gh", "api", path]
    if method:
        args += ["--method", method]
    text = checked(args, timeout=60)
    return json.loads(text) if text else None


def verify_private(info, slug):
    if info.get("private") is not True or info.get("full_name", "").lower() != slug.lower():
        raise backup.BackupError("Requested private repository could not be verified")
    if not info.get("permissions", {}).get("push"):
        raise backup.BackupError("The authenticated account lacks repository push permission")


class PartsWriter:
    def __init__(self, directory, limit=PART_BYTES):
        self.directory, self.limit = directory, limit
        directory.mkdir(parents=True, exist_ok=True)
        self.handle = None
        self.parts = []
        self.bytes = 0
        self.total_hash = hashlib.sha256()

    def _finish(self):
        if self.handle:
            self.handle.close()
            self.parts.append({"name": self.path.name, "bytes": self.part_bytes,
                               "sha256": self.part_hash.hexdigest()})
            self.handle = None

    def write(self, data):
        self.total_hash.update(data)
        self.bytes += len(data)
        view = memoryview(data)
        count = len(data)
        while view:
            if self.handle is None:
                self.path = self.directory / f"qwen-checkpoint.tar.part{len(self.parts):04d}"
                self.handle = self.path.open("wb")
                self.part_hash, self.part_bytes = hashlib.sha256(), 0
            n = min(len(view), self.limit - self.part_bytes)
            block = view[:n]
            self.handle.write(block)
            self.part_hash.update(block)
            self.part_bytes += n
            view = view[n:]
            if self.part_bytes == self.limit:
                self._finish()
        return count

    def flush(self):
        if self.handle:
            self.handle.flush()

    def close(self):
        self._finish()


class HashReader:
    def __init__(self, handle, size):
        self.handle = handle
        self.sha256 = hashlib.sha256()
        self.git_sha1 = hashlib.sha1(f"blob {size}\0".encode())

    def read(self, n=-1):
        block = self.handle.read(n)
        self.sha256.update(block)
        self.git_sha1.update(block)
        return block


def checkpoint_archive():
    manifest_path = ROOT / "reports/qwen_checkpoint_release_manifest.json"
    directory = STATE / "model_parts"
    if manifest_path.exists():
        old = json.loads(manifest_path.read_text())
        stamp = manifest_path.stat().st_mtime_ns
        if all((directory / p["name"]).exists()
               and (directory / p["name"]).stat().st_size == p["bytes"]
               and (directory / p["name"]).stat().st_mtime_ns <= stamp
               and (directory / p["name"]).stat().st_ctime_ns <= stamp for p in old["parts"]):
            status(stage="checkpoint_archive_reused", checkpoint_parts=len(old["parts"]))
            return old
    receipt = json.loads((ROOT / "reports/local_model_complete_verification.json").read_text())
    expected = {r["file"]: r for r in receipt["files"]}
    model_dir = Path(receipt["checkpoint_directory"])
    files = sorted(p for p in model_dir.iterdir() if p.is_file())
    if set(p.name for p in files) != set(expected) | {"bio_evaluation_checkpoint.json"}:
        raise backup.BackupError("Checkpoint contents differ from the verified public file set")
    if shutil.disk_usage(ROOT).free < sum(p.stat().st_size for p in files) + 3 * 1024**3:
        raise backup.BackupError("Insufficient project-disk space for the checkpoint upload archive")
    directory.mkdir(parents=True, exist_ok=True)
    for old in directory.glob("qwen-checkpoint.tar.part[0-9][0-9][0-9][0-9]"):
        old.unlink()
    writer = PartsWriter(directory)
    records = []
    status(stage="packaging_checkpoint", checkpoint_files=len(files), checkpoint_bytes_written=0)
    with tarfile.open(fileobj=writer, mode="w|", bufsize=8 * 1024 * 1024,
                      copybufsize=8 * 1024 * 1024, format=tarfile.PAX_FORMAT) as archive:
        for path in files:
            before = path.stat()
            rel = path.relative_to(ROOT)
            if path.name not in expected:
                backup.scan_file(path)
            info = tarfile.TarInfo(rel.as_posix())
            info.size, info.mode, info.mtime = before.st_size, 0o644, 0
            with path.open("rb") as handle:
                reader = HashReader(handle, before.st_size)
                archive.addfile(info, reader)
            after = path.stat()
            if (before.st_size, before.st_mtime_ns) != (after.st_size, after.st_mtime_ns):
                raise backup.BackupError("A checkpoint file changed during snapshot creation")
            if path.name in expected:
                source = expected[path.name]
                actual = reader.sha256.hexdigest() if source["digest_type"] == "sha256" else reader.git_sha1.hexdigest()
                if actual != source["digest"] or before.st_size != source["bytes"]:
                    raise backup.BackupError("A checkpoint digest differs from the publisher verification")
            records.append({"path": rel.as_posix(), "bytes": before.st_size,
                            "sha256": reader.sha256.hexdigest()})
            status(checkpoint_files_packaged=len(records), checkpoint_bytes_written=writer.bytes)
    writer.close()
    value = {"format": "concatenated uncompressed tar parts", "release_tag": TAG,
             "model": receipt["model"], "revision": receipt["revision"],
             "archive_sha256": writer.total_hash.hexdigest(), "archive_bytes": writer.bytes,
             "parts": writer.parts, "files": records,
             "original_license_preserved": True, "source_files_publisher_digest_verified": len(expected),
             "excluded": ["credentials", "virtual environments", "package/download/build caches", "transient process state"]}
    write_json(manifest_path, value)
    return value


def scan_history():
    status(stage="scanning_git_history")
    objects = checked(["git", "rev-list", "--objects", "HEAD"]).splitlines()
    blobs = 0
    with tempfile.TemporaryDirectory(dir=STATE) as directory:
        for row in objects:
            oid, _, name = row.partition(" ")
            kind = checked(["git", "cat-file", "-t", oid])
            if kind != "blob":
                continue
            if backup.secret_filename(name):
                raise backup.BackupError("A credential-bearing or excluded filename exists in Git history")
            result = subprocess.run(["git", "cat-file", "blob", oid], cwd=ROOT, capture_output=True)
            if result.returncode:
                raise backup.BackupError("A Git history blob could not be inspected")
            multipart = re.fullmatch(r"artifacts/evaluation-assets\.tar\.gz\.part\d{4}", name)
            # A gzip stream can span multiple Git blobs. Scan each raw part now,
            # then join the exact historical parts below before inspecting tar.
            suffix = ".bin" if multipart else ".tar.gz" if result.stdout.startswith(b"\x1f\x8b") else Path(name).suffix
            path = Path(directory) / (oid + suffix)
            path.write_bytes(result.stdout)
            backup.scan_file(path)
            blobs += 1
        archive_hashes = set()
        versions = checked(["git", "log", "--format=%H", "--", "artifacts/manifest.json"]).splitlines()
        for version in versions:
            manifest = json.loads(checked(["git", "show", f"{version}:artifacts/manifest.json"]))
            digest = manifest["archive_sha256"]
            if digest in archive_hashes:
                continue
            parts = manifest["parts"]
            if not parts or any(not re.fullmatch(r"evaluation-assets\.tar\.gz\.part\d{4}", p) for p in parts):
                raise backup.BackupError("Historical evaluation archive part names are invalid")
            joined = Path(directory) / "joined-evaluation-assets.tar.gz"
            sha, size = hashlib.sha256(), 0
            with joined.open("wb") as handle:
                for part in parts:
                    result = subprocess.run(["git", "show", f"{version}:artifacts/{part}"], cwd=ROOT, capture_output=True)
                    if result.returncode:
                        raise backup.BackupError("A historical evaluation archive part is missing")
                    size += len(result.stdout)
                    if size > 2 * 1024**3:
                        raise backup.BackupError("A historical evaluation archive exceeds the scan limit")
                    sha.update(result.stdout)
                    handle.write(result.stdout)
            if sha.hexdigest() != digest:
                raise backup.BackupError("A historical evaluation archive checksum differs from its manifest")
            previous_limit = backup.MAX_ARCHIVE_SCAN
            try:
                # This outer workspace snapshot is larger than individual source
                # archives; retain a finite bound while inspecting its members.
                backup.MAX_ARCHIVE_SCAN = 4 * 1024**3
                backup.scan_file(joined)
            finally:
                backup.MAX_ARCHIVE_SCAN = previous_limit
            archive_hashes.add(digest)
    status(history_blobs_scanned=blobs)


def configured_checkpoint(settings):
    if settings.get("include_checkpoint_in_private_release") is True:
        return checkpoint_archive()
    return None


def release_assets(slug, release_id):
    rows, page = [], 1
    while True:
        batch = api(f"repos/{slug}/releases/{release_id}/assets?per_page=100&page={page}")
        rows.extend(batch)
        if len(batch) < 100:
            return {r["name"]: r for r in rows}
        page += 1


def asset_matches(remote, item):
    return bool(remote and remote.get("state") == "uploaded" and remote.get("size") == item["bytes"]
                and remote.get("digest") == "sha256:" + item["sha256"])


def publish(model):
    record = json.loads((STATE / "repo.json").read_text())
    slug = record["repo"]
    verify_private(api("repos/" + slug), slug)
    status(stage="scanning_workspace", repo=slug)
    settings = backup.config()
    archived, direct = backup.inventory(settings)
    # Freeze live server logs without stopping the server or changing originals.
    stable = []
    for rel, path in archived:
        if rel.parts[0] == "logs":
            copy = STATE / "log_snapshot" / rel
            copy.parent.mkdir(parents=True, exist_ok=True)
            with path.open("rb") as source, copy.open("wb") as dest:
                shutil.copyfileobj(source, dest)
            stable.append((rel, copy))
        else:
            stable.append((rel, path))
    status(stage="packaging_evaluation_files", archived_files=len(stable), direct_files=len(direct))
    details = backup.build_archive(stable)
    status(stage="committing_code_and_evaluation_files", **details)
    commit = backup.local_commit()
    verify_private(api("repos/" + slug), slug)
    backup.private_remote(settings)
    status(stage="pushing_code_and_evaluation_files", commit=commit)
    backup.push()
    remote_head = checked(["git", "ls-remote", "origin", "refs/heads/main"]).split()[0]
    if remote_head != commit:
        raise backup.BackupError("Remote main does not match the uploaded workspace commit")
    status(stage="code_and_evaluation_files_uploaded", code_uploaded=True, commit=commit)
    # Re-read the scope after the potentially long Git push. A user can narrow
    # the backup while it is running without authorizing any weight upload.
    if model is None or backup.config().get("include_checkpoint_in_private_release") is not True:
        verify_private(api("repos/" + slug), slug)
        status(stage="complete", all_uploaded=True, private_verified=True,
               repo_url=record["url"], model_references_only=True,
               checkpoint_assets_uploaded=0, scheduled_uploads_enabled=False)
        return
    existing = backup.run(["gh", "api", f"repos/{slug}/releases/tags/{TAG}"], timeout=60)
    if existing.returncode:
        notes = STATE / "release_notes.md"
        notes.write_text("Complete pinned Qwen3.8-27B BF16 checkpoint backup. Join parts in manifest order and verify SHA-256 before extraction. Code, evaluation data, sources, raw results and logs are preserved by the repository snapshot. Credentials, environments and caches are excluded. One-time private backup; no scheduled uploads.\n")
        checked(["gh", "release", "create", TAG, "--repo", slug, "--draft", "--target", commit,
                 "--title", "Complete evaluation workspace and Qwen checkpoint — 2026-10-15",
                 "--notes-file", str(notes)], timeout=60)
        release = api(f"repos/{slug}/releases/tags/{TAG}")
    else:
        release = json.loads(existing.stdout)
    parts = [dict(p, path=str(STATE / "model_parts" / p["name"])) for p in model["parts"]]
    manifest = ROOT / "reports/qwen_checkpoint_release_manifest.json"
    items = [{"name": manifest.name, "path": str(manifest), "bytes": manifest.stat().st_size,
              "sha256": hashlib.sha256(manifest.read_bytes()).hexdigest()}, *parts]
    remote = release_assets(slug, release["id"])
    done = {item["name"] for item in items if asset_matches(remote.get(item["name"]), item)}
    active = set()
    started = time.monotonic()

    def update():
        complete_bytes = sum(i["bytes"] for i in items if i["name"] in done)
        status(stage="uploading_checkpoint", checkpoint_assets_uploaded=len(done), checkpoint_assets_total=len(items),
               checkpoint_bytes_uploaded=complete_bytes, checkpoint_bytes_total=sum(i["bytes"] for i in items),
               active_uploads=sorted(active), upload_elapsed_seconds=round(time.monotonic() - started, 1))

    update()

    def upload(item):
        with PROGRESS_LOCK:
            active.add(item["name"])
        update()
        for attempt in range(1, 4):
            current = release_assets(slug, release["id"]).get(item["name"])
            if asset_matches(current, item):
                break
            if current:
                if current.get("state") == "starter" or current.get("size") == 0:
                    api(f"repos/{slug}/releases/assets/{current['id']}", "DELETE")
                else:
                    raise backup.BackupError("A release asset exists with a different size or digest")
            try:
                backup.run(["gh", "release", "upload", TAG, item["path"], "--repo", slug], timeout=900)
            except backup.BackupError:
                # Reconcile an uncertain completion before deciding to retry.
                pass
            current = release_assets(slug, release["id"]).get(item["name"])
            if asset_matches(current, item):
                break
            if attempt == 3:
                raise backup.BackupError("A checkpoint asset upload did not pass GitHub size/SHA-256 verification")
        with PROGRESS_LOCK:
            done.add(item["name"])
            active.discard(item["name"])
        update()

    # Prove authenticated asset upload and GitHub's digest reporting on a small
    # manifest before transferring any multi-hundred-MiB checkpoint part.
    if items[0]["name"] not in done:
        upload(items[0])
    with cf.ThreadPoolExecutor(max_workers=2) as pool:
        futures = [pool.submit(upload, i) for i in items if i["name"] not in done]
        for future in cf.as_completed(futures):
            future.result()
    remote = release_assets(slug, release["id"])
    if not all(asset_matches(remote.get(i["name"]), i) for i in items):
        raise backup.BackupError("Final release verification did not match all expected assets")
    verify_private(api("repos/" + slug), slug)
    checked(["gh", "release", "edit", TAG, "--repo", slug, "--draft=false"], timeout=60)
    status(stage="complete", all_uploaded=True, active_uploads=[], private_verified=True,
           repo_url=record["url"], release_url=f"{record['url']}/releases/tag/{TAG}",
           release_asset_count=len(items), model_source_file_count=len(model["files"]),
           archive_and_asset_sha256_verified=True, scheduled_uploads_enabled=False)


def main():
    STATE.mkdir(parents=True, exist_ok=True)
    lock = (STATE / "snapshot.lock").open("a")
    fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
    try:
        scan_history()
        model = configured_checkpoint(backup.config())
        publish(model)
    except Exception as error:
        status(stage="failed", error_type=type(error).__name__,
               message=str(error) if isinstance(error, backup.BackupError) else "Snapshot operation failed; inspect local state before resuming")
        raise SystemExit(1)


if __name__ == "__main__":
    main()
