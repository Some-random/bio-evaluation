"""Private immutable backup of one reviewed P36 condition and source preparation.

No inference, rescoring, job submission or master completion updates. Merely
importing this module reads no credentials and makes no network requests.
"""
from __future__ import annotations

import argparse
from contextlib import contextmanager
from datetime import datetime, timezone
import fcntl
import gzip
import hashlib
import importlib.util
import io
import json
import math
import os
from pathlib import Path
import signal
import tarfile
import time
import urllib.error
import urllib.parse
import urllib.request

REPOSITORY = "Some-random/bio-evaluation"
RUN_ID = "p36-qwen3.8-27b-biot5-reviewed59-20261016"
RUN_POINTER = Path("results/runs") / RUN_ID
SOURCE_POINTER = Path("artifacts/source-preparation-2026-10-16")
TAG = "continuation-2026-10-16-reviewed-p36-and-source-preparation"
VARIANT = "QWEN_FULLTEXT_BIOT5_DESIGN_PAIRED_SOURCE_ROUGE_PARTIAL"
REVISION = "1d4bf0f2ff6012fd82039f2fa52739d0dd7c60c0"
SOURCE_SHA = "63ff12232b04294201ac9b46ea717a930774f5010e0999abebf70dc20778e4bb"
GENERATION = {"max_tokens": 4096, "temperature": 1.0, "top_p": 0.95,
              "top_k": 20, "seed": 42, "n": 1,
              "chat_template_kwargs": {"enable_thinking": True, "reasoning_effort": "medium"}}
STOP = False


class ValidationError(RuntimeError):
    pass


class PublicationDeferred(ValidationError):
    pass


def stamp():
    return datetime.now(timezone.utc).isoformat()


@contextmanager
def publication_lock(root):
    """Coordinate only the new publishers; the original uploader is untouched."""
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


def stable_publication_pointer(value, previous):
    previous_value = {key: item for key, item in previous.items()
                      if key not in {"updated_at_utc", "commit_sha"}}
    updated = previous.get("updated_at_utc") if previous_value == value else None
    return {**value, "updated_at_utc": updated or stamp()}


def canonical(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode()


def digest(value):
    return hashlib.sha256(canonical(value)).hexdigest()


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def read(path):
    return json.loads(Path(path).read_bytes())


def write(path, value, immutable=False):
    path = Path(path)
    raw = (json.dumps(value, ensure_ascii=False, indent=2) + "\n").encode()
    if path.exists() and path.read_bytes() == raw:
        return False
    if immutable and path.exists():
        raise ValidationError("Previously recorded immutable manifest changed")
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_bytes(raw)
    tmp.chmod(0o600)
    tmp.replace(path)
    return True


def module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result


def within(folder, relative):
    value = Path(relative)
    path = (folder / value).resolve()
    if value.is_absolute() or ".." in value.parts or not path.is_relative_to(folder.resolve()):
        raise ValidationError("Artifact path exceeds the frozen project")
    return path


def load_condition(config_path, run_dir):
    config_path, run_dir = Path(config_path).resolve(), Path(run_dir).resolve()
    project = config_path.parent
    config = read(config_path)
    if (config.get("task_id") != "P36" or config.get("variant") != VARIANT
            or config.get("model") != "Qwen/Qwen3.8-27B"
            or config.get("model_revision") != REVISION
            or config.get("generation") != GENERATION):
        raise ValidationError("Uploader is restricted to the exact partial P36 baseline")
    for relative, expected in config["frozen_files_sha256"].items():
        if sha(within(project, relative).read_bytes()) != expected:
            raise ValidationError("Frozen reproduction dependency hash changed")
    cases = [json.loads(line) for line in within(project, config["input_file"]).read_text().splitlines() if line]
    review = read(within(project, config["review_file"]))
    ids = [case["case_id"] for case in cases]
    if (len(ids) != 59 or len(set(ids)) != 59 or ids != review.get("approved_case_ids")
            or review.get("full_source_case_count") != 5876
            or digest(cases) != config.get("case_contract_sha256")
            or set(ids) & {row["case_id"] for row in review.get("held_cases", [])}):
        raise ValidationError("Reviewed partial case scope or input contract changed")
    expected = {}
    for case in cases:
        if case.get("task") != "P36" or case.get("variant") != VARIANT:
            raise ValidationError("Model input is outside the reviewed P36 condition")
        filename = digest(["P36", VARIANT, case["case_id"]]) + ".json"
        payload = {"model": config["model"], "messages": case["messages"], **config["generation"]}
        expected[filename] = {"case_id": case["case_id"], "payload_sha256": digest(payload)}
    config_sha = sha(config_path.read_bytes())
    manifest_path = run_dir / "run_manifest.json"
    if manifest_path.is_file():
        manifest = read(manifest_path)
        if (manifest.get("configuration_sha256") != config_sha
                or manifest.get("configuration") != config
                or manifest.get("case_contract_sha256") != config["case_contract_sha256"]):
            raise ValidationError("Run manifest differs from the frozen condition")
    return {"config": config, "config_path": config_path, "config_sha256": config_sha,
            "project": project, "run_dir": run_dir, "expected": expected, "review": review}


def terminal_state(run_dir):
    run_dir = Path(run_dir)
    dispatch = run_dir / "dispatch_summary.json"
    completion = run_dir / "completion.json"
    generation_terminal = dispatch.is_file() or completion.is_file()
    scoring_terminal = generation_terminal and all((run_dir / name).is_file() for name in
        ("scores.json", "per_case_scores.json", "scoring_output_lock.json", "native_metric_output.tsv"))
    return {"generation_terminal": generation_terminal,
            "scoring_terminal": completion.is_file() or scoring_terminal,
            "scoring_artifacts_present": scoring_terminal}


def scoring_success(condition, state):
    """Validate saved scorer evidence; never compute or promote a native metric."""
    if not state["scoring_artifacts_present"]:
        return False
    folder = condition["run_dir"]
    scores_raw = (folder / "scores.json").read_bytes()
    if (folder / "completion.json").is_file():
        completion = read(folder / "completion.json")
        if completion.get("status") in {"scoring_failed_no_retry", "failed_no_retry", "interrupted_no_retry", "scoring_failed"}:
            return False
        if any(completion.get(key) is not None and completion[key] != 0
               for key in ("scoring_exit_code", "scorer_exit_code")):
            return False
        metadata = completion.get("metadata")
        if (isinstance(metadata, dict) and "scores_sha256" in metadata
                and metadata["scores_sha256"] != sha(scores_raw)):
            return False
    scores = json.loads(scores_raw)
    if (scores.get("task_id") != "P36" or scores.get("planned") != 59
            or scores.get("full_source_cases") != 5876
            or scores.get("protocol_variant") != VARIANT
            or scores.get("model_revision") != REVISION
            or scores.get("full_benchmark_complete") is not False):
        return False
    value = scores.get("metrics", {}).get("rougeL")
    if type(value) not in (int, float) or not math.isfinite(value) or not 0 <= value <= 1:
        return False
    lock = read(folder / "scoring_output_lock.json")
    locked = lock.get("files_sha256", {})
    expected_lock = {"run_manifest.json"} | {kind + "/" + name
        for name in condition["expected"] for kind in ("requests", "responses")}
    if (not locked or lock.get("contract_sha256") != digest(locked)
            or scores.get("scoring_output_lock_sha256") != digest(locked)
            or set(locked) != expected_lock
            or not isinstance(locked.get("run_manifest.json"), str)):
        return False
    for relative, checksum in locked.items():
        path = within(folder, relative)
        if (sha(path.read_bytes()) if path.is_file() else None) != checksum:
            return False
    slots = read(folder / "per_case_scores.json")
    ids = [row.get("case_id") for row in slots]
    return len(ids) == 59 and ids == condition["review"]["approved_case_ids"]


def collect_trajectories(condition, terminal):
    run_dir, expected = condition["run_dir"], condition["expected"]
    files = set(p.name for kind in ("requests", "responses") for p in (run_dir / kind).glob("*.json"))
    result = []
    for filename in sorted(files):
        if filename not in expected:
            raise ValidationError("Saved trajectory is outside the reviewed case allowlist")
        request_path, response_path = run_dir / "requests" / filename, run_dir / "responses" / filename
        if not request_path.is_file():
            raise ValidationError("Saved response lacks its original request")
        request_raw = request_path.read_bytes()
        request = json.loads(request_raw)
        target = expected[filename]
        config = condition["config"]
        required = {"task": "P36", "case_id": target["case_id"], "variant": VARIANT,
                    "model": config["model"], "model_revision": config["model_revision"],
                    "request_sha256": target["payload_sha256"]}
        if any(request.get(key) != value for key, value in required.items()):
            raise ValidationError("Request provenance differs from reviewed frozen input")
        if digest(request["payload"]) != target["payload_sha256"]:
            raise ValidationError("Request payload differs from frozen input")
        response_raw = response_path.read_bytes() if response_path.is_file() else None
        response = json.loads(response_raw) if response_raw is not None else None
        if response is not None and any(response.get(key) != value for key, value in required.items()):
            raise ValidationError("Response/request identity or payload hash mismatch")
        complete = bool(response and response.get("status") == "completed" and response.get("http_status") == 200)
        if complete:
            choices = response.get("response", {}).get("choices", [])
            if (len(choices) != 1 or not isinstance(response.get("text"), str)
                    or choices[0].get("message", {}).get("content") != response["text"]
                    or choices[0].get("finish_reason") != response.get("finish_reason")
                    or json.loads(response.get("raw_response_body", "null")) != response["response"]):
                raise ValidationError("Completed response does not preserve the original API content")
        if response is None and not terminal:
            continue
        if response is not None and response.get("status") not in {
                "completed", "http_error_no_retry", "error_or_unknown_completion_no_retry"}:
            raise ValidationError("Saved response is not a recognized terminal response record")
        result.append({"filename": filename, "case_id": target["case_id"],
            "status": response.get("status") if response else "ambiguous_dispatch_no_saved_response",
            "complete_pair": complete, "payload_sha256": target["payload_sha256"],
            "request_sha256": sha(request_raw), "response_sha256": sha(response_raw) if response_raw else None,
            "request_raw": request_raw, "response_raw": response_raw})
    return result


def pack_archive(folder, kind, files, config_sha=None, cases=None):
    """Content-addressed, deterministic tar bytes; no filesystem metadata leaks."""
    for name in files:
        path = Path(name)
        if path.is_absolute() or ".." in path.parts or name == "manifest.json":
            raise ValidationError("Unsafe or reserved archive member name")
    manifest = {"schema_version": 1, "kind": kind, "task_id": "P36", "variant": VARIANT,
        "full_benchmark_complete": False, "planned_reviewed_subset": 59,
        "configuration_sha256": config_sha,
        "files": [{"path": name, "bytes": len(raw), "sha256": sha(raw)} for name, raw in sorted(files.items())],
        "cases": cases or []}
    signature = digest(manifest)
    name = RUN_ID + "-" + kind + "-" + signature[:24] + ".tar.gz"
    path = Path(folder) / name
    content = {**files, "manifest.json": canonical(manifest) + b"\n"}
    output = io.BytesIO()
    with gzip.GzipFile(fileobj=output, filename="", mode="wb", mtime=0, compresslevel=6) as zipped:
        with tarfile.open(fileobj=zipped, mode="w", format=tarfile.PAX_FORMAT) as archive:
            for member, raw in sorted(content.items()):
                info = tarfile.TarInfo(member)
                info.size, info.mode, info.mtime = len(raw), 0o644, 0
                archive.addfile(info, io.BytesIO(raw))
    raw = output.getvalue()
    if path.exists() and path.read_bytes() != raw:
        raise ValidationError("Existing content-addressed archive changed")
    path.parent.mkdir(parents=True, exist_ok=True)
    if not path.exists():
        path.write_bytes(raw)
    return path, manifest


def trajectory_batches(items):
    for complete in (True, False):
        batch, size = [], 0
        for item in (row for row in items if row["complete_pair"] is complete):
            length = len(item["request_raw"]) + len(item["response_raw"] or b"")
            if length > 20 * 1024 * 1024:
                raise ValidationError("Single trajectory exceeds the bounded archive limit")
            if batch and (len(batch) >= 100 or size + length > 20 * 1024 * 1024):
                yield batch
                batch, size = [], 0
            batch.append(item)
            size += length
        if batch:
            yield batch


class NoRedirectCredentials(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, request, fp, code, message, headers, newurl):
        result = super().redirect_request(request, fp, code, message, headers, newurl)
        if result is not None:
            result.remove_header("Authorization")
        return result


class GitHub:
    def __init__(self, root, checkout):
        self.root, self.checkout = root, checkout
        self.helpers = module("continuation_upload_git_helpers", root / ".local/litqa2_replay/incremental_upload.py")
        self.helpers.CHECKOUT = checkout
        self.scanner = module("continuation_upload_scanner", root / "scripts/daily_backup.py")
        self.record, self.assets = None, {}

    def private(self):
        result = self.helpers.confirm_destination()
        if result.get("publication_authorized") is not True or result.get("push_permission") is not True:
            raise ValidationError("Authorized repository and push permission must be verified")
        return result

    def git(self, *args, **kwargs):
        kwargs.setdefault("cwd", self.checkout)
        return self.helpers.git(*args, **kwargs)

    def headers(self, accept="application/vnd.github+json"):
        import yaml
        account = yaml.safe_load((Path.home() / ".config/gh/hosts.yml").read_text())["github.com"]
        token = account.get("oauth_token") or account["users"][account["user"]]["oauth_token"]
        return {"Authorization": "Bearer " + token, "Accept": accept,
                "User-Agent": "bio-evaluation-reviewed-continuation-backup"}

    def api(self, url, method="GET", value=None, binary=None):
        parsed = urllib.parse.urlparse(url)
        if (parsed.scheme != "https" or parsed.netloc not in {"api.github.com", "uploads.github.com"}
                or not parsed.path.startswith("/repos/" + REPOSITORY + "/")):
            raise ValidationError("GitHub API destination exceeds the authorized repository")
        if method != "GET":
            self.private()
        data = canonical(value) if value is not None else None
        headers = self.headers()
        if binary is not None:
            self.scanner.scan_file(binary)
            data = binary.read_bytes()
            headers["Content-Type"] = "application/gzip"
        elif data is not None:
            headers["Content-Type"] = "application/json"
        request = urllib.request.Request(url, data=data, headers=headers, method=method)
        with urllib.request.urlopen(request, timeout=60) as response:
            return json.load(response)

    def release(self):
        if self.record is not None:
            return self.record
        base = "https://api.github.com/repos/" + REPOSITORY + "/releases"
        try:
            self.record = self.api(base + "/tags/" + TAG)
        except urllib.error.HTTPError as error:
            if error.code != 404:
                raise
            self.record = self.api(base, "POST", {"tag_name": TAG, "target_commitish": "main",
                "draft": False, "prerelease": True, "name": "Reviewed P36 partial run and source preparation",
                "body": "Immutable original request/response batches for one 59-case reviewed P36 adaptation, plus public-source recovery. This is not full benchmark completion, paper Smith-Waterman scoring or biological design validation. No weights or credentials."})
        page = 1
        while True:
            values = self.api(self.record["assets_url"] + f"?per_page=100&page={page}")
            for asset in values:
                if asset["name"] in self.assets:
                    raise ValidationError("Duplicate immutable release asset name")
                self.assets[asset["name"]] = asset
            if len(values) < 100:
                break
            page += 1
        return self.record

    def ensure_asset(self, path):
        record = self.release()
        name, raw = path.name, path.read_bytes()
        checksum = sha(raw)
        asset = self.assets.get(name)
        if asset is None:
            if len(self.assets) >= 900:
                raise ValidationError("Reviewed continuation release asset limit reached")
            self.private()
            target = record["upload_url"].split("{", 1)[0] + "?name=" + urllib.parse.quote(name)
            asset = self.api(target, "POST", binary=path)
            self.assets[name] = asset
        if asset.get("size") != len(raw):
            raise ValidationError("Remote immutable asset size differs")
        remote_digest = asset.get("digest")
        if remote_digest:
            if remote_digest != "sha256:" + checksum:
                raise ValidationError("Remote immutable asset digest differs")
        else:
            # Older assets can omit digest. Verify downloaded bytes, stripping
            # credentials on any signed-storage redirect.
            request = urllib.request.Request(asset["url"], headers=self.headers("application/octet-stream"))
            opener = urllib.request.build_opener(NoRedirectCredentials())
            with opener.open(request, timeout=60) as response:
                downloaded = response.read(len(raw) + 1)
            if sha(downloaded) != checksum:
                raise ValidationError("Remote immutable asset download hash differs")
        return {"name": name, "asset_id": asset["id"], "asset_url": asset["browser_download_url"],
                "archive_sha256": checksum, "archive_bytes": len(raw)}

    def initialize(self):
        if not (self.checkout / ".git").is_dir():
            self.checkout.mkdir(parents=True, exist_ok=True)
            self.git("init")
            self.git("remote", "add", "origin", self.helpers.URL)
            self.git("config", "remote.origin.promisor", "true")
            self.git("config", "remote.origin.partialclonefilter", "blob:none")
            self.git("sparse-checkout", "init", "--no-cone")
            self.git("sparse-checkout", "set", "--no-cone", "/" + RUN_POINTER.as_posix() + "/",
                     "/" + SOURCE_POINTER.as_posix() + "/")
            self.git("fetch", "--filter=blob:none", "--depth=1", "origin", "main")
            self.git("checkout", "--detach", "FETCH_HEAD")
        for name, fallback in (("user.name", "Codex"), ("user.email", "codex@localhost")):
            value = self.git("config", "--get", name, cwd=self.root, allow_failure=True).stdout.strip() or fallback
            self.git("config", name, value)

    def push(self):
        for relative in (RUN_POINTER, SOURCE_POINTER):
            self.git("add", "-f", "--", relative.as_posix())
        staged = self.git("diff", "--cached", "--name-only").stdout.splitlines()
        if any(not any(path.startswith(folder.as_posix() + "/") for folder in (RUN_POINTER, SOURCE_POINTER)) for path in staged):
            raise ValidationError("Staged path exceeds the authorized pointer scope")
        ahead = int(self.git("rev-list", "--count", "refs/remotes/origin/main..HEAD").stdout.strip())
        self.published_this_cycle = False
        if not staged and not ahead:
            return self.git("rev-parse", "HEAD").stdout.strip()
        with publication_lock(self.root):
            if original_publication_backlog(self.root):
                raise PublicationDeferred("Yielding to the original trajectory publisher's recent non-fast-forward backlog")
            if staged:
                self.git("commit", "-m", "Back up reviewed partial P36 trajectories and source recovery")
            # A failed previous push remains pending even if inputs are unchanged.
            for attempt in range(3):
                self.private()
                result = self.git("push", "origin", "HEAD:refs/heads/main", allow_failure=True)
                if result.returncode == 0:
                    self.published_this_cycle = True
                    return self.git("rev-parse", "HEAD").stdout.strip()
                self.git("fetch", "--filter=blob:none", "origin", "main")
                self.git("rebase", "FETCH_HEAD")
            raise ValidationError("Pointer push could not catch up with concurrent main updates")


def metadata_files(condition, state):
    project, run_dir, config = condition["project"], condition["run_dir"], condition["config"]
    files = {"frozen_config.json": condition["config_path"].read_bytes(),
             "input_review.json": within(project, config["review_file"]).read_bytes()}
    for name in ("source_manifest.json", "PREPARATION_AUDIT_2026-10-16.json", "runtime_package_versions.json", "requirements.lock.txt"):
        if (project / name).is_file():
            files["preparation/" + name] = (project / name).read_bytes()
    for name in ("run_manifest.json", "dispatch_summary.json", "completion.json"):
        if (run_dir / name).is_file():
            files[name] = (run_dir / name).read_bytes()
    if (run_dir / "run_manifest.json").is_file():
        approval_hash = read(run_dir / "run_manifest.json").get("approval_sha256")
        approval = project / "execution_authorization.json"
        if approval.is_file() and sha(approval.read_bytes()) == approval_hash:
            files["execution_authorization.json"] = approval.read_bytes()
    if state["scoring_artifacts_present"]:
        for name in ("scores.json", "per_case_scores.json", "scoring_output_lock.json", "native_metric_output.tsv"):
            files[name] = (run_dir / name).read_bytes()
        scores = json.loads(files["scores.json"])
        if (scores.get("task_id") != "P36" or scores.get("planned") != 59
                or scores.get("protocol_variant") != VARIANT or scores.get("full_benchmark_complete") is not False):
            raise ValidationError("Scorer metadata misstates the reviewed partial condition")
    frozen = {}
    for relative, checksum in config["frozen_files_sha256"].items():
        path = within(project, relative)
        frozen[relative] = {"sha256": checksum, "bytes": path.stat().st_size}
        if not relative.startswith("data/") and path.suffix in {".py", ".yaml", ".yml", ".json", ".txt", ".sh"}:
            files["frozen_files/" + relative] = path.read_bytes()
    files["frozen_dependencies_manifest.json"] = canonical(frozen) + b"\n"
    return files


def verify_existing_index(index, trajectories):
    present = {item["filename"]: item for item in trajectories}
    for row in index:
        current = present.get(row["filename"])
        if current is None or any(row.get(key) != current.get(key) for key in
                ("case_id", "request_sha256", "response_sha256", "payload_sha256", "complete_pair", "status")):
            raise ValidationError("Previously uploaded immutable trajectory disappeared or changed")


def upload_cycle(root, run_dir, config_path, github=None):
    root = Path(root).resolve()
    here = root / ".local/continuation_2026-10-16"
    condition = load_condition(config_path, run_dir)
    state = terminal_state(run_dir)
    state["scoring_success"] = scoring_success(condition, state)
    score_fields = {}
    if state["scoring_success"]:
        scores = read(condition["run_dir"] / "scores.json")
        score_fields = {key: scores[key] for key in ("metrics", "metric_label", "comparison_qualification",
            "valid_native_serializations", "completed", "missing_or_failed_slots", "finish_reasons", "statuses") if key in scores}
    trajectories = collect_trajectories(condition, state["generation_terminal"])
    root_pointer_path = root / RUN_POINTER / "upload_status.json"
    previous_pointer = read(root_pointer_path) if root_pointer_path.is_file() else {}
    initial_pointer = {**previous_pointer, "task_id": "P36", "planned": 59,
        "uploaded_trajectories": previous_pointer.get("uploaded_trajectories", 0),
        "uploaded_completed_pairs": previous_pointer.get("uploaded_completed_pairs", 0),
        "saved_completed_pairs": sum(row["complete_pair"] for row in trajectories),
        "status": "upload_cycle_in_progress", **state, "full_source_cases": 5876,
        "full_benchmark_complete": False, "protocol_variant": VARIANT,
        "configuration_sha256": condition["config_sha256"], "updated_at_utc": stamp()}
    for key in ("metrics", "metric_label", "comparison_qualification", "valid_native_serializations",
                "completed", "missing_or_failed_slots", "finish_reasons", "statuses"):
        initial_pointer.pop(key, None)
    initial_pointer.update(score_fields)
    # Keep the public root pointer stable during local polling. Polling itself
    # is recorded only in .local/upload_status.json; it is not benchmark news.
    if not previous_pointer:
        write(root_pointer_path, initial_pointer)
    lock = {"configuration_sha256": condition["config_sha256"], "run_directory": str(condition["run_dir"]),
            "reviewed_case_ids": condition["review"]["approved_case_ids"], "source_bundle_sha256": SOURCE_SHA}
    write(here / "upload_condition.json", lock, immutable=True)
    github = github or GitHub(root, here / "upload_checkout")
    privacy = github.private()
    github.initialize()
    destination = github.checkout / RUN_POINTER
    source_destination = github.checkout / SOURCE_POINTER
    index_path = destination / "trajectory_index.json"
    index = read(index_path) if index_path.is_file() else []
    verify_existing_index(index, trajectories)
    uploaded = {item["filename"] for item in index}
    for batch in trajectory_batches([row for row in trajectories if row["filename"] not in uploaded]):
        files, cases = {}, []
        for item in batch:
            files["requests/" + item["filename"]] = item["request_raw"]
            if item["response_raw"] is not None:
                files["responses/" + item["filename"]] = item["response_raw"]
            cases.append({key: value for key, value in item.items() if not key.endswith("_raw")})
        kind = ("completed-pairs" if batch[0]["complete_pair"] else
                "terminal-dispatch-evidence" if any(item["response_raw"] is None for item in batch)
                else "saved-response-evidence")
        archive, manifest = pack_archive(here / "upload_batches", kind, files, condition["config_sha256"], cases)
        asset = github.ensure_asset(archive)
        write(destination / "trajectory_batches" / (archive.name + ".json"), {**asset, "manifest": manifest}, immutable=True)
        for item in cases:
            index.append({**item, **asset, "request_member": "requests/" + item["filename"],
                          "response_member": "responses/" + item["filename"] if item["response_sha256"] else None})
        write(index_path, sorted(index, key=lambda row: row["filename"]))
    write(index_path, sorted(index, key=lambda row: row["filename"]))
    metadata_content = metadata_files(condition, state)
    archive, manifest = pack_archive(here / "upload_batches", "metadata", metadata_content, condition["config_sha256"])
    metadata = github.ensure_asset(archive)
    write(destination / "metadata_batches" / (archive.name + ".json"), {**metadata, "manifest": manifest}, immutable=True)
    write(destination / "latest_metadata.json", {**metadata, "manifest": manifest})
    for name in ("frozen_config.json", "input_review.json", "run_manifest.json", "dispatch_summary.json", "completion.json", "scores.json"):
        raw = metadata_content.get(name)
        if raw is not None:
            target = destination / name
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(raw)
    bundle = here / "source_prep/source_prep_bundle.tar.gz"
    if sha(bundle.read_bytes()) != SOURCE_SHA:
        raise ValidationError("Source recovery bundle differs from the reviewed immutable snapshot")
    source_asset = github.ensure_asset(bundle)
    write(source_destination / "manifest.json", {**source_asset, "source_bundle_sha256": SOURCE_SHA,
        "source_audit": "reports/SOURCE_PREPARATION_2026-10-16.json", "contains_model_weights": False,
        "contains_credentials": False, "contains_browser_challenge_pages": False}, immutable=True)
    source_destination.mkdir(parents=True, exist_ok=True)
    (source_destination / "README.md").write_text("# Public-source recovery snapshot\n\n"
        "[Download the source bundle](" + source_asset["asset_url"] + ") · [SHA-256 manifest](manifest.json)\n\n"
        "QA50: 193 official questions; 19/50 original images recovered (73 questions). Native GPT-4 judging remains held. "
        "Ryze component manifests and NatureLM temporal test remain unavailable. No inference was performed for source recovery.\n")
    completed = sum(row["complete_pair"] for row in index)
    saved_pairs = sum(row["response_sha256"] is not None for row in index)
    errors = sum(row["response_sha256"] is not None and not row["complete_pair"] for row in index)
    snapshot = {"task_id": "P36", "protocol_variant": VARIANT, "planned_reviewed_subset": 59,
        "full_source_cases": 5876, "uploaded_completed_pairs": completed,
        "uploaded_saved_response_pairs": saved_pairs, "uploaded_error_response_pairs": errors,
        "uploaded_ambiguous_request_records": len(index) - saved_pairs,
        "uploaded_terminal_failure_or_ambiguous_records": len(index) - completed,
        **state, "configuration_sha256": condition["config_sha256"],
        "full_benchmark_complete": False, "biological_function_validated": False,
        "subset_scoring_artifacts_archived": state["scoring_artifacts_present"],
        "metric": "Qualified released-code paired-reference ROUGE; not paper normalized Smith-Waterman",
        "repository_private_verified": privacy["private"],
        "repository_visibility": privacy.get("visibility"),
        "publication_authorized": privacy.get("publication_authorized"),
        "latest_metadata_asset": metadata["asset_url"]}
    snapshot.update(score_fields)
    write(destination / "upload_snapshot.json", snapshot)
    pointer_value = {**snapshot, "planned": 59, "uploaded_trajectories": saved_pairs,
        "saved_completed_pairs": sum(row["complete_pair"] for row in trajectories),
        "status": ("terminal_snapshot_uploaded" if state["scoring_terminal"] else "incremental_snapshot_uploaded")}
    pointer_path = destination / "upload_status.json"
    previous_published = read(pointer_path) if pointer_path.is_file() else {}
    pointer = stable_publication_pointer(pointer_value, previous_published)
    write(destination / "upload_status.json", pointer)
    (destination / "README.md").write_text("# P36 — reviewed 59-case Qwen baseline\n\n"
        f"{saved_pairs}/59 saved request/response pairs archived: {completed} completed, {errors} error responses. "
        + ("Subset scoring artifacts are available.\n\n" if state["scoring_artifacts_present"] else "Incremental backup; subset scoring remains pending.\n\n")
        + "[Case index](trajectory_index.json) · [Trajectory SHA manifests](trajectory_batches) · [Latest metadata archive](latest_metadata.json) · [Frozen condition](frozen_config.json)\n\n"
        + "This is a partial zero-shot adaptation of the BioT5+ released paired-reference ROUGE condition: 59 input-reviewed cases from 5,876 source cases. "
        + "It is not full P36 completion, paper normalized Smith-Waterman scoring or biological function validation. "
        + "Original requests and responses include reasoning, usage, malformed output and truncation. "
        + "Saved error responses are preserved immediately and counted separately. "
        + "Ambiguous request-only dispatch records are archived only once generation is terminal.\n")
    # Scan every staged candidate, not only compressed assets.
    for folder in (destination, source_destination):
        for path in folder.rglob("*"):
            if path.is_file():
                github.scanner.scan_file(path)
    commit = github.push()
    status = {**snapshot, "stage": "terminal_snapshot_uploaded" if state["scoring_artifacts_present"] else "watching",
              "updated_at_utc": stamp(), "commit_sha": commit,
              "last_published_at_utc": pointer["updated_at_utc"],
              "published_this_cycle": getattr(github, "published_this_cycle", False),
              "github_url": "https://github.com/" + REPOSITORY + "/tree/main/" + RUN_POINTER.as_posix()}
    write(here / "upload_status.json", status)
    write(root_pointer_path, {**pointer, "commit_sha": commit})
    return status


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument("--run-dir", type=Path, required=True)
    parser.add_argument("--config", type=Path, required=True)
    parser.add_argument("--once", action="store_true")
    parser.add_argument("--interval", type=float, default=60)
    args = parser.parse_args(argv)
    if args.interval <= 0:
        parser.error("--interval must be positive")
    here = args.root.resolve() / ".local/continuation_2026-10-16"
    here.mkdir(parents=True, exist_ok=True)
    def stop(signum, frame):
        global STOP
        STOP = True
    for name in (signal.SIGTERM, signal.SIGINT):
        signal.signal(name, stop)
    with (here / "upload_continuation.lock").open("a") as lock:
        fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        while not STOP:
            try:
                status = upload_cycle(args.root, args.run_dir, args.config)
                print(json.dumps({key: status[key] for key in
                    ("stage", "uploaded_completed_pairs", "uploaded_terminal_failure_or_ambiguous_records", "commit_sha")}), flush=True)
            except Exception as error:
                previous = read(here / "upload_status.json") if (here / "upload_status.json").is_file() else {}
                status = {**previous, "stage": "publication_deferred" if isinstance(error, PublicationDeferred) else "retrying", "updated_at_utc": stamp(),
                    "error_type": type(error).__name__, "http_status": getattr(error, "code", None)}
                if isinstance(error, ValidationError):
                    status["validation_error"] = str(error)
                write(here / "upload_status.json", status)
                print(json.dumps({key: status[key] for key in ("stage", "error_type", "http_status")}), flush=True)
                if args.once:
                    return 1
            if args.once:
                break
            deadline = time.monotonic() + args.interval
            while not STOP and time.monotonic() < deadline:
                time.sleep(min(1, max(0, deadline - time.monotonic())))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
