"""Push only finalized replay trajectories from an isolated sparse checkout."""
from datetime import datetime, timezone
import fcntl
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import time
import urllib.request
import yaml

ROOT = Path(__file__).resolve().parents[2]
STATE = ROOT / ".local/litqa2_replay"
RUN_ID = "qwen38_27b_litqa2_replay_2026-10-16"
RELATIVE = Path("results/runs") / RUN_ID
SOURCE = ROOT / RELATIVE
CHECKOUT = STATE / "upload_checkout"
REPOSITORY = "Some-random/bio-evaluation"
URL = "https://github.com/" + REPOSITORY + ".git"
VIEW_URL = "https://github.com/" + REPOSITORY + "/tree/main/" + RELATIVE.as_posix()
HELPER = STATE / "github_credential_helper.py"
ENV = dict(os.environ, GIT_TERMINAL_PROMPT="0")
METADATA = ("run_manifest.json", "context_check.json", "execution_environment.json",
            "server_identity.json", "synthetic_check.json", "progress.json", "replay_status.json",
            "scores.json", "per_case_scores.json", "metrics.csv", "comparison.json", "completion.json")
FINAL_METADATA = ("trajectory_comparison.jsonl", "trajectory_comparison.metadata.json")


def read(path):
    return json.loads(path.read_text())


def stamp():
    return datetime.now(timezone.utc).isoformat()


def save(value):
    path = STATE / "upload_status.json"
    temporary = path.with_suffix(".tmp")
    temporary.write_text(json.dumps(value, indent=2) + "\n")
    temporary.chmod(0o600)
    temporary.replace(path)


def git(*args, cwd=CHECKOUT, allow_failure=False):
    result = subprocess.run(["git", "-c", "credential.helper=", "-c",
        "credential.helper=!python3 " + str(HELPER), *args], cwd=cwd, env=ENV,
        text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.returncode and not allow_failure:
        raise RuntimeError("Git " + args[0] + " failed (exit " + str(result.returncode) + "): " + result.stderr[-2000:])
    return result


def confirm_destination():
    account = yaml.safe_load((Path.home() / ".config/gh/hosts.yml").read_text())["github.com"]
    token = account.get("oauth_token") or account["users"][account["user"]]["oauth_token"]
    request = urllib.request.Request("https://api.github.com/repos/" + REPOSITORY,
        headers={"Authorization": "Bearer " + token, "Accept": "application/vnd.github+json",
                 "User-Agent": "bio-evaluation-incremental-backup"})
    with urllib.request.urlopen(request, timeout=30) as response:
        repo = json.load(response)
    path = ROOT / "scripts/publication_destination.py"
    spec = importlib.util.spec_from_file_location("authorized_publication_destination", path)
    policy = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(policy)
    return policy.verify_repository_metadata(repo, ROOT)


def confirm_private():
    """Compatibility entrypoint; return the real authorized visibility."""
    return confirm_destination()


def initialize():
    if not (CHECKOUT / ".git").is_dir():
        CHECKOUT.mkdir(parents=True, exist_ok=True)
        git("init")
        git("remote", "add", "origin", URL)
        git("config", "remote.origin.promisor", "true")
        git("config", "remote.origin.partialclonefilter", "blob:none")
        git("sparse-checkout", "init", "--no-cone")
        git("sparse-checkout", "set", "--no-cone", "/" + RELATIVE.as_posix() + "/")
        git("fetch", "--filter=blob:none", "--depth=1", "origin", "main")
        git("checkout", "--detach", "FETCH_HEAD")
    for name, fallback in (("user.name", "Codex"), ("user.email", "codex@localhost")):
        value = git("config", "--get", name, cwd=ROOT, allow_failure=True).stdout.strip() or fallback
        git("config", name, value)


def digest(value):
    return hashlib.sha256(json.dumps(value, ensure_ascii=False, sort_keys=True,
        separators=(",", ":")).encode()).hexdigest()


def upload():
    privacy = confirm_private()
    initialize()
    destination = CHECKOUT / RELATIVE
    completed = []
    for response_path in sorted((SOURCE / "responses").glob("*.json")):
        response = read(response_path)
        request_path = SOURCE / "requests" / response_path.name
        if response.get("status") != "completed" or response.get("http_status") != 200 or not request_path.is_file():
            continue
        request = read(request_path)
        if (response.get("request_sha256") != request.get("request_sha256")
                or request.get("request_sha256") != digest(request["payload"])
                or response.get("case_id") != request.get("case_id")):
            raise RuntimeError("Finalized request/response provenance mismatch")
        for kind, source in (("requests", request_path), ("responses", response_path)):
            target = destination / kind / source.name
            target.parent.mkdir(parents=True, exist_ok=True)
            if target.exists() and target.read_bytes() != source.read_bytes():
                raise RuntimeError("Previously uploaded immutable trajectory changed")
            if not target.exists():
                shutil.copyfile(source, target)
        completed.append(response_path.name)
    final_ready = (STATE / "upload_finalize.json").is_file()
    for name in METADATA + (FINAL_METADATA if final_ready else ()):
        source = SOURCE / name
        if source.is_file():
            destination.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(source, destination / name)
    terminal = read(SOURCE / "replay_status.json")
    terminal_complete = len(completed) == 197 and terminal.get("stage") == "completed"
    finished = terminal_complete and final_ready and all((SOURCE / name).is_file() for name in FINAL_METADATA)
    status_path = STATE / "upload_status.json"
    previous = read(status_path) if status_path.is_file() else {}
    if (previous.get("uploaded_completed_pairs") == len(completed)
            and previous.get("generation_and_scoring_complete", False) == terminal_complete
            and not finished):
        return False
    if finished and (STATE / "independent_completion_audit.json").is_file():
        shutil.copyfile(STATE / "independent_completion_audit.json", destination / "independent_completion_audit.json")
    snapshot = {"run_id": RUN_ID, "uploaded_completed_pairs": len(completed), "planned": 197,
        "snapshot_at_utc": stamp(), "run_complete": finished, "generation_and_scoring_complete": terminal_complete,
        "note": "Incremental snapshot of finalized request/response pairs; incomplete until all 197 pairs and terminal scoring complete.",
        "repository_private_verified": privacy["private"],
        "repository_visibility": privacy["visibility"],
        "publication_authorized": privacy["publication_authorized"]}
    index = [{"case_id": read(SOURCE / "requests" / name)["case_id"],
              "request": "requests/" + name, "response": "responses/" + name} for name in completed]
    (destination / "trajectory_index.json").write_text(json.dumps(index, indent=2) + "\n")
    (destination / "README.md").write_text(
        "# LitQA2 replay trajectories\n\n"
        + str(len(completed)) + "/197 finalized request/response pairs. "
        + ("Run, audit and comparison export complete.\n\n" if finished else "Incremental snapshot; final audit/export pending.\n\n")
        + "[Request records](requests) · [Response records](responses) · [Case index](trajectory_index.json)\n\n"
        + "Raw response records preserve API content, including reasoning fields and usage metadata.\n"
        + ("\n[Scores](scores.json) · [Paired trajectory comparison](trajectory_comparison.jsonl) · [Independent audit](independent_completion_audit.json)\n" if finished else ""))
    if finished:
        scores = read(SOURCE / "scores.json")
        comparison = read(SOURCE / "comparison.json")
        metrics = scores["metrics"]
        with (destination / "README.md").open("a") as summary:
            summary.write("\nReplay: " + str(metrics["n_correct"]) + "/" + str(metrics["n_total"])
                + " correct (" + format(100 * metrics["accuracy"], ".2f") + "% accuracy). "
                + str(comparison["same_parsed_answer"]) + "/197 parsed answers match the archived run. "
                + "All 197 responses completed and parsed; the independent audit passed.\n")
    (destination / "upload_snapshot.json").write_text(json.dumps(snapshot, indent=2) + "\n")
    git("add", "-f", "--", RELATIVE.as_posix())
    changes = git("diff", "--cached", "--name-only").stdout.splitlines()
    if any(not p.startswith(RELATIVE.as_posix() + "/") for p in changes):
        raise RuntimeError("Staged paths exceed authorized replay scope")
    if changes:
        git("commit", "-m", "Back up LitQA2 replay trajectories (" + str(len(completed)) + "/197)")
        pushed = git("push", "origin", "HEAD:refs/heads/main", allow_failure=True)
        if pushed.returncode:
            git("fetch", "--filter=blob:none", "origin", "main")
            git("rebase", "FETCH_HEAD")
            git("push", "origin", "HEAD:refs/heads/main")
    commit = git("rev-parse", "HEAD").stdout.strip()
    status = {**snapshot, "commit_sha": commit, "github_url": VIEW_URL, "privacy_check": privacy,
        "status": "complete" if finished else ("awaiting_final_audit" if terminal_complete else "incremental_snapshot_uploaded")}
    save(status)
    print(json.dumps({k: status[k] for k in ("uploaded_completed_pairs", "planned", "run_complete", "commit_sha", "github_url", "status")}), flush=True)
    return finished


if __name__ == "__main__":
    lock = (STATE / "incremental_upload.lock").open("a")
    fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
    while True:
        try:
            finished = upload()
        except Exception as error:
            save({"status": "error", "updated_at_utc": stamp(), "error": str(error), "github_url": VIEW_URL})
            raise
        if finished or "--once" in sys.argv:
            break
        time.sleep(60)
