"""Incrementally back up exact multimodal requests as private release batches."""
from datetime import datetime, timezone
import fcntl
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import shutil
import tarfile
import time
import urllib.error
import urllib.parse
import urllib.request
import yaml

ROOT = Path(__file__).resolve().parents[2]
STATE = ROOT / ".local/litqa2_replay"
TAG = "parallel-labbench-replay-2026-10-16-trajectories"
REPOSITORY = "Some-random/bio-evaluation"
RUNS = {task: "qwen38_27b_" + task.lower() + "_slurm_replay_2026-10-16" for task in ("B03", "B04", "B05")}
EXPECTED = {"B03": 82, "B04": 181, "B05": 244}
CHECKOUT = STATE / "parallel_upload_checkout"
METADATA = ("run_manifest.json", "progress.json", "completion.json", "scores.json",
            "per_case_scores.json", "metrics.csv", "server_identity.json", "execution_environment.json",
            "context_check.json", "synthetic_check.json", "replay_status.json", "comparison.json")
SPEC = importlib.util.spec_from_file_location("litqa2_upload_helpers", STATE / "incremental_upload.py")
helpers = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(helpers)
helpers.CHECKOUT = CHECKOUT


def git(*args, **kwargs):
    kwargs.setdefault("cwd", CHECKOUT)
    return helpers.git(*args, **kwargs)


def stamp():
    return datetime.now(timezone.utc).isoformat()


def sha(path):
    result = hashlib.sha256()
    with path.open("rb") as stream:
        while data := stream.read(1024 * 1024):
            result.update(data)
    return result.hexdigest()


def read(path):
    return json.loads(path.read_text())


def api(url, method="GET", value=None, binary=None):
    account = yaml.safe_load((Path.home() / ".config/gh/hosts.yml").read_text())["github.com"]
    token = account.get("oauth_token") or account["users"][account["user"]]["oauth_token"]
    headers = {"Authorization": "Bearer " + token, "Accept": "application/vnd.github+json",
               "User-Agent": "bio-evaluation-incremental-backup"}
    data = None
    if value is not None:
        data = json.dumps(value).encode()
        headers["Content-Type"] = "application/json"
    if binary is not None:
        data = binary.read_bytes()
        headers["Content-Type"] = "application/gzip"
    request = urllib.request.Request(url, data=data, method=method, headers=headers)
    with urllib.request.urlopen(request, timeout=300) as response:
        return json.load(response)


def release():
    base = "https://api.github.com/repos/" + REPOSITORY + "/releases"
    try:
        return api(base + "/tags/" + TAG)
    except urllib.error.HTTPError as error:
        if error.code != 404:
            raise
    return api(base, "POST", {"tag_name": TAG, "target_commitish": "main", "draft": False,
        "prerelease": True, "name": "LAB-Bench replay request trajectories (incremental)",
        "body": "Incremental private backup for the 2026-10-16 B03/B04/B05 replays. "
        "Each gzip tar asset contains original request JSON files with all image data intact. "
        "Per-run trajectory_index.json and request_batches/ manifests on main map cases to assets and SHA-256 digests. "
        "Raw responses are browsable in each run's responses directory. Completion status is recorded per run."})


def initialize():
    if not (CHECKOUT / ".git").is_dir():
        CHECKOUT.mkdir(parents=True, exist_ok=True)
        git("init")
        git("remote", "add", "origin", helpers.URL)
        git("config", "remote.origin.promisor", "true")
        git("config", "remote.origin.partialclonefilter", "blob:none")
        git("sparse-checkout", "init", "--no-cone")
        git("sparse-checkout", "set", "--no-cone", *["/results/runs/" + run + "/" for run in RUNS.values()])
        git("fetch", "--filter=blob:none", "--depth=1", "origin", "main")
        git("checkout", "--detach", "FETCH_HEAD")
    for name, fallback in (("user.name", "Codex"), ("user.email", "codex@localhost")):
        value = git("config", "--get", name, cwd=ROOT, allow_failure=True).stdout.strip() or fallback
        git("config", name, value)


def upload_batch(run_id, pending, release_record, destination):
    signature = hashlib.sha256("\n".join(name + ":" + sha(path) for name, path, response in pending).encode()).hexdigest()
    name = run_id + "-requests-" + signature[:20] + ".tar.gz"
    archive = STATE / "parallel_request_batches" / run_id / name
    archive.parent.mkdir(parents=True, exist_ok=True)
    if not archive.exists():
        temporary = archive.with_suffix(".tmp")
        with tarfile.open(temporary, "w:gz", compresslevel=6) as tar:
            for filename, path, response in pending:
                tar.add(path, arcname="requests/" + filename, recursive=False)
        temporary.replace(archive)
    checksum = sha(archive)
    assets = api(release_record["assets_url"] + "?per_page=100")
    asset = next((item for item in assets if item["name"] == name), None)
    if asset is None:
        target = release_record["upload_url"].split("{", 1)[0] + "?name=" + urllib.parse.quote(name)
        asset = api(target, "POST", binary=archive)
    if asset["size"] != archive.stat().st_size:
        raise RuntimeError("Uploaded request batch size differs")
    if asset.get("digest") and asset["digest"] != "sha256:" + checksum:
        raise RuntimeError("Uploaded request batch digest differs")
    entries = []
    for filename, path, response in pending:
        obj = read(path)
        entries.append({"case_id": obj["case_id"], "filename": filename,
            "request_member": "requests/" + filename, "request_sha256": sha(path),
            "payload_sha256": obj["request_sha256"], "request_asset": asset["browser_download_url"],
            "request_archive_sha256": checksum, "response": "responses/" + filename,
            "response_sha256": sha(response)})
    manifest = {"run_id": run_id, "asset": asset["browser_download_url"], "asset_id": asset["id"],
        "archive_sha256": checksum, "archive_bytes": archive.stat().st_size, "cases": entries,
        "raw_request_json_preserved": True, "image_data_preserved": True,
        "server_digest": asset.get("digest"), "created_at_utc": stamp()}
    manifests = destination / "request_batches"
    manifests.mkdir(parents=True, exist_ok=True)
    (manifests / (name + ".json")).write_text(json.dumps(manifest, indent=2) + "\n")
    return entries


def cycle():
    helpers.confirm_private()
    initialize()
    release_record = None
    status = {}
    changed = False
    for task, run_id in RUNS.items():
        source = ROOT / "results/runs" / run_id
        destination = CHECKOUT / "results/runs" / run_id
        if not source.is_dir():
            status[task] = {"run_id": run_id, "uploaded_pairs": 0, "planned": EXPECTED[task], "complete": False}
            continue
        index_file = destination / "trajectory_index.json"
        index = read(index_file) if index_file.is_file() else []
        uploaded = {item["filename"] for item in index}
        pending = []
        batch_bytes = 0
        batches = []
        for response in sorted((source / "responses").glob("*.json")):
            if response.name in uploaded:
                continue
            obj = read(response)
            request = source / "requests" / response.name
            if obj.get("status") != "completed" or obj.get("http_status") != 200 or not request.is_file():
                continue
            req = read(request)
            if (obj.get("case_id") != req.get("case_id") or obj.get("request_sha256") != req.get("request_sha256")
                    or req.get("request_sha256") != helpers.digest(req["payload"])):
                raise RuntimeError("Parallel replay trajectory provenance mismatch")
            size = request.stat().st_size
            if pending and (len(pending) >= 20 or batch_bytes + size > 40 * 1024 * 1024):
                batches.append(pending)
                pending, batch_bytes = [], 0
            pending.append((response.name, request, response))
            batch_bytes += size
        if pending:
            batches.append(pending)
        for batch in batches:
            if release_record is None:
                release_record = release()
            index.extend(upload_batch(run_id, batch, release_record, destination))
            for filename, request, response in batch:
                target = destination / "responses" / filename
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(response, target)
            changed = True
        if index:
            destination.mkdir(parents=True, exist_ok=True)
            index.sort(key=lambda entry: entry["filename"])
            index_file.write_text(json.dumps(index, indent=2) + "\n")
            for name in METADATA:
                if (source / name).is_file():
                    shutil.copyfile(source / name, destination / name)
        completion = read(source / "completion.json") if (source / "completion.json").is_file() else {}
        complete = (len(index) == EXPECTED[task] and completion.get("generation_exit_code") == 0
                    and completion.get("scoring_exit_code") == 0 and (source / "scores.json").is_file())
        snapshot = {"task_id": task, "run_id": run_id, "uploaded_pairs": len(index),
            "planned": EXPECTED[task], "complete": complete, "request_storage": "immutable private release assets",
            "response_storage": "browsable JSON files", "github_url": "https://github.com/" + REPOSITORY + "/tree/main/results/runs/" + run_id}
        status[task] = snapshot
        if index:
            old_snapshot = read(destination / "upload_snapshot.json") if (destination / "upload_snapshot.json").exists() else {}
            changed = changed or snapshot != old_snapshot
            (destination / "upload_snapshot.json").write_text(json.dumps(snapshot, indent=2) + "\n")
            (destination / "README.md").write_text("# " + task + " replay trajectories\n\n"
                + str(len(index)) + "/" + str(EXPECTED[task]) + " finalized pairs uploaded. "
                + ("Generation and scoring complete.\n\n" if complete else "Incremental snapshot; run incomplete.\n\n")
                + "[Raw responses](responses) · [Case index](trajectory_index.json) · [Request batch manifests](request_batches)\n\n"
                + "The case index links original request JSONs to immutable private release assets. "
                + "Extract the named member from its gzip tar batch. Every request field, including full base64 image data, is preserved. "
                + "The manifest records both archive and individual-file SHA-256 digests. Raw responses retain all API reasoning fields.\n")
    if changed:
        for run_id in RUNS.values():
            relative = "results/runs/" + run_id
            if (CHECKOUT / relative).exists():
                git("add", "-f", "--", relative)
        staged = git("diff", "--cached", "--name-only").stdout.splitlines()
        if any(not any(path.startswith("results/runs/" + run + "/") for run in RUNS.values()) for path in staged):
            raise RuntimeError("Parallel upload staged unrelated paths")
        if staged:
            git("commit", "-m", "Back up parallel LAB-Bench replay trajectories")
            pushed = git("push", "origin", "HEAD:refs/heads/main", allow_failure=True)
            if pushed.returncode:
                git("fetch", "--filter=blob:none", "origin", "main")
                git("rebase", "FETCH_HEAD")
                git("push", "origin", "HEAD:refs/heads/main")
    summary = {"updated_at_utc": stamp(), "repository_private_verified": True,
        "commit_sha": git("rev-parse", "HEAD").stdout.strip(), "runs": status,
        "all_complete": all(item["complete"] for item in status.values())}
    out = STATE / "parallel_upload_status.json"
    temp = out.with_suffix(".tmp")
    temp.write_text(json.dumps(summary, indent=2) + "\n")
    temp.chmod(0o600)
    temp.replace(out)
    print(json.dumps(summary), flush=True)
    return summary["all_complete"]


if __name__ == "__main__":
    lock = (STATE / "parallel_upload.lock").open("a")
    fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
    while not cycle():
        time.sleep(60)
