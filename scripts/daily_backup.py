#!/usr/bin/env python3
"""Commit this evaluation workspace and push only to its verified private repo.

No inference calls. Credentials are handled by the GitHub CLI and never copied
into this repository. Large evaluation directories use deterministic archives.
"""

import argparse
import datetime as dt
import fcntl
import gzip
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import tarfile
import tempfile
import zipfile


ROOT = Path(__file__).resolve().parents[1]
PST = dt.timezone(dt.timedelta(hours=-8))
MAX_GIT_FILE = 90 * 1024 * 1024
MAX_ARCHIVE_SCAN = 256 * 1024 * 1024
SECRET_PATTERNS = (
    re.compile(rb"\bsk-(?:proj-)?[A-Za-z0-9_-]{32,}"),
    re.compile(rb"\bgh[pousr]_[A-Za-z0-9]{30,}"),
    re.compile(rb"\bgithub_pat_[A-Za-z0-9_]{40,}"),
    re.compile(rb"\bhf_[A-Za-z0-9]{30,}"),
    re.compile(rb"-----BEGIN (?:RSA |EC |OPENSSH |DSA )?PRIVATE KEY-----"),
    re.compile(rb"\bAKIA[A-Z0-9]{16}\b"),
)
EXCLUDED_DIRS = {".git", ".local", ".venv", ".venv-vllm", ".cache", "models", "__pycache__", ".ssh"}
SENSITIVE_NAMES = {
    ".git-credentials", "credentials.json", "secrets.json", "secrets.yml",
    "secrets.yaml", "token.txt", "github_token", "github_token.txt",
}


class BackupError(RuntimeError):
    pass


def secret_filename(path):
    p = Path(path)
    name = p.name.lower()
    return (
        any(part in EXCLUDED_DIRS for part in p.parts)
        or (name.startswith(".env") and name != ".env.example")
        or "openai_key" in name
        or name in SENSITIVE_NAMES
        or p.suffix.lower() in {".pem", ".key", ".p12", ".pfx"}
    )


def safe_archive_member(name):
    p = Path(name)
    if p.is_absolute() or ".." in p.parts or secret_filename(p):
        raise BackupError("An archive contains an unsafe or credential-bearing filename.")


def scan_bytes(data):
    if any(pattern.search(data) for pattern in SECRET_PATTERNS):
        raise BackupError("A possible credential was found; upload stopped. No secret was logged.")


def scan_file(path):
    """Scan plain files and archive members without extracting them onto disk."""
    with path.open("rb") as stream:
        carry = b""
        while chunk := stream.read(1024 * 1024):
            scan_bytes(carry + chunk)
            carry = chunk[-1024:]
    if zipfile.is_zipfile(path):
        with zipfile.ZipFile(path) as archive:
            total = 0
            for member in archive.infolist():
                safe_archive_member(member.filename)
                total += member.file_size
                if total > MAX_ARCHIVE_SCAN:
                    raise BackupError("An archive is too large for the secret scan.")
                if not member.is_dir():
                    scan_bytes(archive.read(member))
    elif path.name.endswith((".tar.gz", ".tgz", ".tar")):
        with tarfile.open(path, "r:*") as archive:
            total = 0
            for member in archive:
                safe_archive_member(member.name)
                if member.isdir():
                    continue
                if not member.isfile():
                    raise BackupError("An archive contains a link or special file.")
                total += member.size
                if total > MAX_ARCHIVE_SCAN:
                    raise BackupError("An archive is too large for the secret scan.")
                scan_bytes(archive.extractfile(member).read())
    elif path.suffix == ".gz":
        with gzip.open(path, "rb") as stream:
            data = stream.read(MAX_ARCHIVE_SCAN + 1)
            if len(data) > MAX_ARCHIVE_SCAN:
                raise BackupError("A gzip file is too large for the secret scan.")
            scan_bytes(data)


def run(argv, *, input_text=None, timeout=180):
    env = os.environ.copy()
    env.update(GIT_TERMINAL_PROMPT="0", GH_PROMPT_DISABLED="1")
    if argv[0] == "gh":
        for name in ["HTTP_PROXY", "HTTPS_PROXY", "ALL_PROXY", "http_proxy", "https_proxy", "all_proxy"]:
            value = env.get(name, "")
            if value.startswith("socks5h://"):
                env[name] = "socks5://" + value[len("socks5h://"):]
    try:
        result = subprocess.run(
            argv, cwd=ROOT, env=env, input=input_text, capture_output=True,
            text=True, timeout=timeout,
        )
    except (OSError, subprocess.TimeoutExpired):
        raise BackupError("A backup command was unavailable or timed out.") from None
    return result


def checked(argv, **kwargs):
    result = run(argv, **kwargs)
    if result.returncode:
        # Git/gh messages can contain URLs with credentials; keep them private.
        raise BackupError("A " + argv[0] + " command failed; upload did not complete.")
    return result.stdout.strip()


def config():
    value = json.loads((ROOT / "configs/backup.json").read_text())
    if value.get("visibility") != "private":
        raise BackupError("This backup supports private repositories only.")
    for name in [value["repo_name"], value.get("owner")]:
        if name is not None and not re.fullmatch(r"[A-Za-z0-9_.-]+", name):
            raise BackupError("Invalid GitHub repository or account name.")
    return value


def inventory(settings):
    archived, direct = [], []
    folders = set(settings["archive_directories"])
    for base, dirs, files in os.walk(ROOT, followlinks=False):
        base = Path(base)
        dirs[:] = sorted(d for d in dirs if d not in EXCLUDED_DIRS and d != "artifacts")
        for directory in dirs:
            if (base / directory).is_symlink():
                raise BackupError("A workspace symlink needs review before backup.")
        for name in sorted(files):
            path = base / name
            relative = path.relative_to(ROOT)
            if secret_filename(relative) or name.endswith((".pyc", ".pyo")):
                continue
            if path.is_symlink() or not path.is_file():
                raise BackupError("A workspace link or special file needs review before backup.")
            scan_file(path)
            if relative.parts[0] in folders:
                archived.append((relative, path))
            else:
                if path.stat().st_size > MAX_GIT_FILE:
                    raise BackupError("A large file outside data/sources/results needs archive placement.")
                direct.append((relative, path))
    return archived, direct


def build_archive(entries):
    target = ROOT / "artifacts"
    target.mkdir(exist_ok=True)
    for previous in target.iterdir():
        if previous.name != "manifest.json" and not re.fullmatch(r"evaluation-assets\.tar\.gz\.part\d{4}", previous.name):
            raise BackupError("An unexpected artifact needs review before backup.")
    manifest = []
    for relative, path in sorted(entries):
        raw = path.read_bytes()
        manifest.append({"path":relative.as_posix(), "bytes":len(raw), "sha256":hashlib.sha256(raw).hexdigest()})
    fd, temporary = tempfile.mkstemp(prefix=".tmp-", dir=target)
    try:
        with os.fdopen(fd, "wb") as stream:
            with gzip.GzipFile(fileobj=stream, mode="wb", filename="", mtime=0, compresslevel=1) as compressed:
                with tarfile.open(fileobj=compressed, mode="w|", format=tarfile.PAX_FORMAT) as archive:
                    for relative, path in sorted(entries):
                        info = tarfile.TarInfo(relative.as_posix())
                        info.size = path.stat().st_size
                        info.mode = 0o644
                        info.mtime = 0
                        with path.open("rb") as source:
                            archive.addfile(info, source)
        archive_sha = hashlib.sha256(Path(temporary).read_bytes()).hexdigest()
        part_names = []
        with open(temporary, "rb") as stream:
            part = 0
            while chunk := stream.read(MAX_GIT_FILE):
                name = f"evaluation-assets.tar.gz.part{part:04d}"
                part_path = target / name
                if not part_path.exists() or part_path.read_bytes() != chunk:
                    part_path.write_bytes(chunk)
                part_names.append(name)
                part += 1
        for old in target.glob("evaluation-assets.tar.gz.part*"):
            if old.name not in part_names:
                old.unlink()
        value = {"format":"concatenated gzip tar parts", "parts":part_names,
                 "archive_sha256":archive_sha, "files":manifest,
                 "contains_evaluation_material":True,
                 "use_restriction":"Backup only. Never use held-out evaluation material for training, solver retrieval or test-driven tuning."}
        (target / "manifest.json").write_text(json.dumps(value, indent=2) + "\n")
        return {"archived_files":len(manifest), "archive_parts":len(part_names),
                "archive_sha256":archive_sha, "archive_bytes":Path(temporary).stat().st_size}
    finally:
        Path(temporary).unlink(missing_ok=True)


def local_commit():
    if not (ROOT / ".git").exists():
        checked(["git", "init", "-b", "main"])
        checked(["git", "config", "user.name", "Evaluation workspace backup"])
        checked(["git", "config", "user.email", "evaluation-backup@localhost"])
    verified = ROOT / ".local/backup_verified_commit"
    head = run(["git", "rev-parse", "--verify", "HEAD"])
    if head.returncode == 0 and (not verified.exists() or head.stdout.strip() != verified.read_text().strip()):
        raise BackupError("Unreviewed Git commits exist; inspect their history before automatic upload.")
    checked(["git", "add", "--all"])
    tracked = checked(["git", "ls-files", "-z"]).split("\0")
    for name in filter(None, tracked):
        if secret_filename(name):
            raise BackupError("A credential-bearing filename is tracked; upload stopped.")
        if (ROOT / name).stat().st_size > MAX_GIT_FILE:
            raise BackupError("A tracked file exceeds the upload size limit.")
    changes = run(["git", "diff", "--cached", "--quiet"])
    if changes.returncode == 1:
        stamp = dt.datetime.now(PST).strftime("%Y-%m-%d %H:%M PST")
        checked(["git", "commit", "-m", "Evaluation workspace backup " + stamp])
    elif changes.returncode:
        raise BackupError("Git could not inspect staged changes.")
    commit = checked(["git", "rev-parse", "HEAD"])
    verified.write_text(commit + "\n")
    return commit


def private_remote(settings):
    auth = run(["gh", "api", "user", "--jq", ".login"], timeout=45)
    if auth.returncode:
        raise BackupError("GitHub authentication is required on this server; local commit retained.")
    login = auth.stdout.strip()
    if not re.fullmatch(r"[A-Za-z0-9-]+", login):
        raise BackupError("Unexpected GitHub account response.")
    owner = settings.get("owner") or login
    slug = owner + "/" + settings["repo_name"]
    remote_url = "https://github.com/" + slug + ".git"
    existing = run(["git", "remote", "get-url", "origin"])
    if existing.returncode == 0:
        if existing.stdout.strip() != remote_url:
            raise BackupError("The existing Git remote differs from the configured backup repository.")
    else:
        # Creation without --push lets us verify privacy before sending any file.
        creation_record = ROOT / ".local/remote_creation.json"
        previous = json.loads(creation_record.read_text()) if creation_record.exists() else {}
        if previous.get("repo") != slug:
            checked(["gh", "repo", "create", slug, "--private", "--description", settings["description"]], timeout=60)
            creation_record.write_text(json.dumps({"repo":slug}) + "\n")
        info = json.loads(checked(["gh", "api", "repos/" + slug], timeout=45))
        if info.get("private") is not True or info.get("full_name", "").lower() != slug.lower():
            raise BackupError("GitHub did not confirm the requested private repository.")
        checked(["git", "remote", "add", "origin", remote_url])
    info = json.loads(checked(["gh", "api", "repos/" + slug], timeout=45))
    if info.get("private") is not True:
        raise BackupError("The remote repository is not private; upload stopped.")
    return slug


def remote_refs(*patterns):
    """Read private remote refs using the same scoped login as the push."""
    return checked(["git", "-c", "credential.helper=", "-c",
                    "credential.helper=!gh auth git-credential", "ls-remote", "origin", *patterns], timeout=90)


def push():
    # A per-command credential helper avoids shared/global Git configuration.
    helper = "!gh auth git-credential"
    checked(["git", "-c", "credential.helper=", "-c", "credential.helper=" + helper,
             "push", "--set-upstream", "origin", "HEAD:main"], timeout=1800)


def backup(local_only=False):
    settings = config()
    entries, direct = inventory(settings)
    details = build_archive(entries)
    details["direct_files"] = len(direct)
    details["commit"] = local_commit()
    if local_only:
        details["status"] = "local_backup_complete"
    else:
        details["repo"] = private_remote(settings)
        push()
        details["status"] = "uploaded"
    return details


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--local-only", action="store_true")
    args = parser.parse_args()
    local = ROOT / ".local"
    local.mkdir(exist_ok=True, mode=0o700)
    os.chmod(local, 0o700)
    environment = local / "backup_environment.json"
    if environment.is_file():
        values = json.loads(environment.read_text())
        allowed = {"HTTP_PROXY", "HTTPS_PROXY", "ALL_PROXY", "NO_PROXY", "http_proxy", "https_proxy", "all_proxy", "no_proxy"}
        for name, value in values.items():
            if name in allowed and isinstance(value, str):
                os.environ.setdefault(name, value)
    with (local / "backup.lock").open("a") as lock:
        try:
            fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            print(json.dumps({"status":"already_running"}))
            return 0
        try:
            status = backup(args.local_only)
            success = True
        except (BackupError, ValueError, OSError, tarfile.TarError, zipfile.BadZipFile) as exc:
            status = {"status":"blocked", "message":str(exc) if isinstance(exc, BackupError) else "A local backup file could not be validated."}
            success = False
        status["checked_at_pst"] = dt.datetime.now(PST).isoformat()
        (local / "backup_status.json").write_text(json.dumps(status, indent=2) + "\n")
        print(json.dumps(status))
        return 0 if success else 1


if __name__ == "__main__":
    raise SystemExit(main())
