"""Validate mixed serving provenance and invoke an unchanged native scorer once.

This offline adapter reads no labels itself, dispatches no model requests, and
never rewrites an execution config, historical manifest, raw output or score.
An explicit scoring view joins the exact original cases and retains missing or
ambiguous generations in the native denominator. Infrastructure changes live
in separate provenance records; they are never attributed to an old runner.
"""
from __future__ import annotations

import argparse
from collections import Counter
from contextlib import contextmanager
import datetime as dt
import fcntl
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
from zoneinfo import ZoneInfo

SUPPORTED = {"P03", "P07", "P08", "P12", "P13", "P14", "P15", "P16", "P28", "P29"}
DEEPFRI = {"P12", "P13", "P14", "P15"}
SCORERS = {
    **{key: "scripts/score_local_catalog_extended.py" for key in ("P03", "P07", "P08")},
    "P16": "scripts/score_local_reaction.py", "P28": "scripts/score_local_bioreason_pro.py",
    "P29": "scripts/score_local_posttrain_protein.py",
    **{key: "scripts/score_local_deepfri_confidence.py" for key in DEEPFRI},
}


class ScoringError(ValueError):
    pass


class Pending(ScoringError):
    pass


def digest(value):
    return hashlib.sha256(json.dumps(value, ensure_ascii=False, sort_keys=True,
                                    separators=(",", ":")).encode()).hexdigest()


def file_sha(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as handle:
        for chunk in iter(lambda: handle.read(8 * 1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def read(path):
    return json.loads(Path(path).read_text())


def now():
    return dt.datetime.now(ZoneInfo("America/Los_Angeles")).isoformat()


def immutable_json(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        if read(path) != value:
            raise ScoringError("Existing immutable scoring artifact differs: " + str(path))
        return
    # Exclusive creation prevents an independent scorer silently replacing it.
    with path.open("x") as handle:
        json.dump(value, handle, indent=2, ensure_ascii=False)
        handle.write("\n")


def project_path(root, name):
    path = (root / name).resolve()
    if not path.is_relative_to(root):
        raise ScoringError("Input/config path escapes its project: " + str(name))
    return path


def checked_config(root, name, expected):
    path = project_path(root, name)
    if file_sha(path) != expected:
        raise ScoringError("Frozen configuration hash differs: " + str(name))
    cfg = read(path)
    if not re.fullmatch(r"[A-Za-z0-9_.-]+", cfg.get("run_id", "")):
        raise ScoringError("Unsafe or missing run ID")
    return cfg


def generation_folder(root, cfg, source):
    original = root / "results/runs" / cfg["run_id"]
    folder = project_path(root, source.get("generation_folder", str(original)))
    if not folder.is_relative_to(root / "results/runs"):
        raise ScoringError("Generation folder is outside the project run namespace")
    return folder


def validate_fork_identity(root, cfg, folder, proof):
    original = root / "results/runs" / cfg["run_id"]
    if folder == original:
        return
    marker_path = folder / "shared_vllm_fork_manifest.json"
    if not marker_path.is_file() or proof.get("kind") != "shared_serving_amendment":
        raise ScoringError("Alternate generation folder lacks an audited continuation fork")
    marker = read(marker_path)
    if (marker.get("logical_run_id") != cfg["run_id"]
            or Path(marker.get("source_run_directory", "")).resolve() != original
            or Path(marker.get("continuation_run_directory", "")).resolve() != folder
            or proof.get("fork_manifest_sha256") != file_sha(marker_path)
            or Path(proof.get("original_source_folder", "")).resolve() != original):
        raise ScoringError("Continuation fork identity/provenance differs")
    for filename, marker_key, proof_key in (
        ("scoring_output_lock.json", "source_scoring_output_lock_sha256", "parent_scoring_output_lock_sha256"),
        ("completion.json", "source_completion_sha256", "parent_completion_sha256"),
        ("scores.json", "source_scores_sha256", "parent_scores_sha256"),
    ):
        expected = file_sha(original / filename)
        if marker.get(marker_key) != expected or proof.get(proof_key) != expected:
            raise ScoringError("Continuation fork changed its immutable parent lock/completion")


def input_cases(root, cfg):
    # References are deliberately deferred to the native scorer after output
    # locking. Other original dependencies must remain byte-identical.
    reference = (root / cfg["scorer_reference_file"]).resolve()
    for name, expected in cfg["frozen_files_sha256"].items():
        path = (root / name).resolve()
        if path != reference and file_sha(path) != expected:
            raise ScoringError("Frozen input/code dependency changed: " + name)
    cases = [json.loads(line) for line in project_path(root, cfg["input_file"]).read_text().splitlines() if line]
    review = read(project_path(root, cfg["review_file"]))
    identities = [c["case_id"] for c in cases]
    held = {c["case_id"] for c in review.get("held_cases", [])}
    if (not cases or identities != review["approved_case_ids"]
            or len(identities) != len(set(identities)) or held.intersection(identities)):
        raise ScoringError("Exact original ordered input review differs")
    return cases


def load_frozen_runner(root, cfg):
    path = project_path(root, cfg["runner"])
    if file_sha(path) != cfg["frozen_files_sha256"][cfg["runner"]]:
        raise ScoringError("Original input-only runner differs")
    name = "shared_scoring_frozen_runner_" + file_sha(path)[:12]
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def validate_raw(root, cfg, cases, folder):
    """Validate exact native requests and response identity, without labels."""
    runner = load_frozen_runner(root, cfg)
    expected = {digest([c["task"], c["variant"], c["case_id"]]) + ".json" for c in cases}
    hashes, states = {}, Counter()
    for kind in ("requests", "responses"):
        actual = {p.name for p in (folder / kind).glob("*.json")}
        if not actual <= expected:
            raise ScoringError("Extra raw case identity in " + kind)
    for case in cases:
        identity = digest([case["task"], case["variant"], case["case_id"]]) + ".json"
        paths = {kind: folder / kind / identity for kind in ("requests", "responses")}
        request, response = (read(paths[k]) if paths[k].exists() else None for k in ("requests", "responses"))
        for kind, path in paths.items():
            hashes[kind + "/" + identity] = file_sha(path) if path.exists() else None
        if request is not None and request != runner.request_record(case, cfg):
            raise ScoringError("Raw request differs from complete original prompt/generation")
        if response is not None:
            if request is None:
                raise ScoringError("Response without its exact request")
            fields = {**{k: case[k] for k in ("task", "case_id", "variant", "split")},
                      "model": cfg["model"], "model_revision": cfg["model_revision"],
                      "request_sha256": request["request_sha256"]}
            if any(response.get(k) != value for k, value in fields.items()):
                raise ScoringError("Response model/case/request provenance differs")
            if response.get("status") == "completed":
                raw = response.get("response") or {}
                choices = raw.get("choices") or []
                if (response.get("http_status") != 200 or raw.get("model") != cfg["model"]
                        or len(choices) != 1 or response.get("finish_reason") != choices[0].get("finish_reason")
                        or response.get("text") != (choices[0].get("message", {}).get("content") or "")):
                    raise ScoringError("Completed response is inconsistent with saved raw API output")
        states[response.get("status") if response else "interrupted_unknown_completion" if request else "not_dispatched"] += 1
    return hashes, dict(states)


def validate_legacy(folder, cfg, cases, config_sha):
    if not (folder / "completion.json").exists():
        raise Pending("Original source is not terminal: " + cfg["run_id"])
    if not (folder / "scoring_output_lock.json").is_file():
        raise ScoringError("Original terminal source lacks its pre-label raw-output lock")
    completion = read(folder / "completion.json")
    manifest = read(folder / "run_manifest.json")
    if (completion.get("configuration_sha256") != config_sha
            or completion.get("scoring_exit_code") != 0
            or manifest.get("configuration") != cfg
            or manifest.get("configuration_sha256") != config_sha
            or manifest.get("case_contract_sha256") != digest(cases)
            or manifest.get("planned_cases") != len(cases)
            or manifest.get("runner_sha256") != cfg["frozen_files_sha256"][cfg["runner"]]
            or manifest.get("solver_tools") != []
            or manifest.get("answer_keys_available_to_solver") is not False
            or manifest.get("model_selection_on_test") is not False):
        raise ScoringError("Original source manifest/completion contract differs")
    for snapshot in (manifest.get("server", {}), manifest.get("serving_configuration", {})):
        if not snapshot or snapshot.get("model") != cfg["model"] or snapshot.get("revision") != cfg["model_revision"]:
            raise ScoringError("Original server model/revision snapshot differs")
    server = manifest["server"]
    if not server.get("pid") or not server.get("proc_start_ticks"):
        raise ScoringError("Original historical server process identity is missing")
    for filename, field in (("run_manifest.json", "run_manifest_sha256"), ("scores.json", "scores_sha256"),
                            ("scoring_output_lock.json", "scoring_output_lock_sha256")):
        if field in completion and file_sha(folder / filename) != completion[field]:
            raise ScoringError("Historical terminal artifact changed: " + filename)
    return {"kind": "original_terminal", "completion_sha256": file_sha(folder / "completion.json"),
            "original_run_manifest_sha256": file_sha(folder / "run_manifest.json"),
            "actual_servers": [manifest["server"]] if manifest.get("server") else []}


def resume_validator():
    path = Path(__file__).with_name("shared_vllm_resume.py")
    spec = importlib.util.spec_from_file_location("shared_scoring_resume_validator", path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module.validate_resume_provenance


def validate_sources(spec, validator=None):
    root = Path(spec["project_root"]).resolve()
    task = spec["task_id"]
    if task not in SUPPORTED or spec["scorer_file"] != SCORERS[task]:
        raise ScoringError("Unsupported task/native scorer pairing")
    full = checked_config(root, spec["full_config_file"], spec["full_config_sha256"])
    if full["approved_task_ids"] != [task]:
        raise ScoringError("Full configuration task differs")
    scorer = project_path(root, spec["scorer_file"])
    if (file_sha(scorer) != spec["scorer_sha256"]
            or full["frozen_files_sha256"].get(spec["scorer_file"]) != spec["scorer_sha256"]):
        raise ScoringError("Native scorer is not the original frozen implementation")
    full_cases = input_cases(root, full)
    runner = load_frozen_runner(root, full)
    full_requests = {digest([c["task"], c["variant"], c["case_id"]]): runner.request_record(c, full) for c in full_cases}
    groups, sources, identities = [], [], set()
    for source in spec["sources"]:
        cfg = checked_config(root, source["config_file"], source["config_sha256"])
        if cfg["approved_task_ids"] != [task]:
            raise ScoringError("Cross-task source supplied")
        cases = input_cases(root, cfg)
        if any(cfg.get(k) != full.get(k) for k in ("model", "model_revision", "checkpoint_precision", "generation", "variant", "scorer_reference_file", "scorer_reference_sha256")):
            raise ScoringError("Source biological/generation/reference recipe differs")
        source_runner = load_frozen_runner(root, cfg)
        for case in cases:
            key = digest([case["task"], case["variant"], case["case_id"]])
            if key in identities:
                raise ScoringError("A native case appears in multiple source runs")
            identities.add(key)
            if source_runner.request_record(case, cfg) != full_requests.get(key):
                raise ScoringError("Source request bytes differ from full original recipe")
        folder = generation_folder(root, cfg, source)
        if (folder / "shared_vllm_amendment.json").exists():
            if not (folder / "shared_vllm_generation_completion.json").exists():
                raise Pending("Shared generation is not terminal: " + cfg["run_id"])
            proof = (validator or resume_validator())(folder, cfg, cases, require_terminal=True)
            if proof.get("all_saved_responses_verified") is not True:
                raise ScoringError("Shared-serving output provenance is not verified")
            if spec.get("execution_amendment_sha256") and proof.get("amendment_sha256") != spec["execution_amendment_sha256"]:
                raise ScoringError("Shared-serving provenance belongs to a different execution amendment")
            proof = {**proof, "kind": "shared_serving_amendment"}
        else:
            if folder != root / "results/runs" / cfg["run_id"]:
                raise ScoringError("Alternate generation folder is not a shared continuation")
            proof = validate_legacy(folder, cfg, cases, source["config_sha256"])
        validate_fork_identity(root, cfg, folder, proof)
        hashes, states = validate_raw(root, cfg, cases, folder)
        if (folder / "scoring_output_lock.json").exists():
            old_lock = read(folder / "scoring_output_lock.json")
            if old_lock.get("contract_sha256") != digest(old_lock.get("files_sha256")):
                raise ScoringError("Original raw-output lock contract differs")
            if old_lock["files_sha256"].get("run_manifest.json") != file_sha(folder / "run_manifest.json"):
                raise ScoringError("Originally locked execution manifest changed")
            for name, expected in old_lock.get("files_sha256", {}).items():
                if name in hashes and hashes[name] != expected:
                    raise ScoringError("An originally locked output/missing slot changed")
            if not set(hashes) <= set(old_lock["files_sha256"]):
                raise ScoringError("Original lock omitted a native output/missing slot")
        groups.append(cases)
        sources.append({**source, "run_id": cfg["run_id"], "case_count": len(cases),
                        "generation_folder": str(folder),
                        "raw_files_sha256": hashes, "statuses": states, "provenance": proof})
    # The declared source order must be precisely the native full source order.
    if [case for group in groups for case in group] != full_cases:
        raise ScoringError("Source union is not the exact ordered complete native case set")
    expected_count = full.get("full_test_case_count", full.get("planned", len(full_cases)))
    if expected_count != len(full_cases):
        raise ScoringError("Original full native denominator differs")
    union = {"complete": True, "union_matches_full_test_ids": True,
             "expected_test_case_count": len(full_cases), "unique_observed_case_count": len(identities),
             "missing_case_count": 0, "extra_case_count": 0}
    return root, full, full_cases, sources, union


def install_raw(source, target, expected):
    if expected is None:
        if source.exists() or target.exists():
            raise ScoringError("Frozen missing output slot appeared")
        return
    if file_sha(source) != expected:
        raise ScoringError("Source changed after provenance validation")
    target.parent.mkdir(parents=True, exist_ok=True)
    if target.exists():
        if file_sha(target) != expected:
            raise ScoringError("Scoring view would replace an existing output")
        return
    try:
        os.link(source, target)
    except OSError:
        shutil.copyfile(source, target)
    if file_sha(target) != expected:
        raise ScoringError("Scoring view copy differs")


def deepfri_view(root, full, spec, sources):
    """A distinct, honestly attributed config satisfying the native scorer API."""
    if len(sources) != 1:
        raise ScoringError("DeepFRI requires one complete native source run")
    actual = Path(spec["execution_runner_file"]).resolve()
    if file_sha(actual) != spec["execution_runner_sha256"]:
        raise ScoringError("Actual shared execution adapter differs")
    original = read(Path(sources[0].get("generation_folder", root / "results/runs" / sources[0]["run_id"])) / "run_manifest.json")
    if original.get("runner_sha256") != spec["execution_runner_sha256"]:
        raise ScoringError("DeepFRI view cannot attribute generation to a different runner")
    cfg = json.loads(json.dumps(full))
    cfg["run_id"] = full["run_id"] + "_shared_scoring"
    relative = os.path.relpath(actual, root)
    cfg["runner"] = relative
    cfg["frozen_files_sha256"][relative] = spec["execution_runner_sha256"]
    cfg["shared_vllm_scoring_view"] = {
        "original_configuration_sha256": spec["full_config_sha256"],
        "original_run_id": full["run_id"], "actual_execution_runner_sha256": spec["execution_runner_sha256"],
        "adapter_sha256": file_sha(__file__), "generation_and_native_scoring_unchanged": True,
    }
    allowed = {"run_id", "runner", "frozen_files_sha256", "shared_vllm_scoring_view"}
    if any(cfg.get(k) != full.get(k) for k in set(cfg) | set(full) if k not in allowed):
        raise ScoringError("A biological or scoring field changed in the scoring view")
    path = root / "configs" / (cfg["run_id"] + ".json")
    immutable_json(path, cfg)
    return cfg, path


def existing_completion(folder, expected_config_sha):
    completion = folder / "completion.json"
    if not completion.exists():
        return None
    done = read(completion)
    if (done.get("scoring_exit_code") != 0 or done.get("configuration_sha256") != expected_config_sha
            or done.get("scores_sha256") != file_sha(folder / "scores.json")
            or done.get("run_manifest_sha256") != file_sha(folder / "run_manifest.json")):
        raise ScoringError("Existing terminal score is failed or its provenance changed; no retry")
    return {"state": "existing_completed_unchanged", "run_id": folder.name,
            "completion_sha256": file_sha(completion), "scores_sha256": file_sha(folder / "scores.json")}


def native_environment(spec):
    environment = dict(os.environ)
    for name in ("OPENAI_API_KEY", "ANTHROPIC_API_KEY", "HF_TOKEN", "HUGGING_FACE_HUB_TOKEN", "PYTHONHOME", "VIRTUAL_ENV"):
        environment.pop(name, None)
    environment["CUDA_VISIBLE_DEVICES"] = ""
    if spec.get("runtime_receipt_file"):
        # The CPU coordinator uses Python 3.10; its optional overlays must not
        # leak binary packages into the distinct pinned Python 3.12 scorer.
        environment.pop("PYTHONPATH", None)
        path = Path(spec["runtime_receipt_file"])
        if file_sha(path) != spec["runtime_receipt_sha256"]:
            raise ScoringError("Frozen native CPU runtime receipt changed")
        receipt = read(path)
        if (receipt.get("state") != "ready" or receipt.get("python") != spec["python"]
                or file_sha(spec["python"]) != receipt["python_sha256"]
                or receipt["observed_versions"].get("visible_gpu_count") != 0):
            raise ScoringError("Native CPU interpreter differs from its prepared receipt")
        allowed = {"CUDA_VISIBLE_DEVICES", "OMP_NUM_THREADS", "MKL_NUM_THREADS", "OPENBLAS_NUM_THREADS",
                   "CUDA_HOME", "LD_LIBRARY_PATH", "PATH", "PYTHONNOUSERSITE"}
        if not set(receipt["environment"]) <= allowed or receipt["environment"].get("CUDA_VISIBLE_DEVICES") != "":
            raise ScoringError("Unexpected environment fields in native CPU receipt")
        environment.update(receipt["environment"])
    return environment


def _score_spec_unlocked(spec, *, validate_only=False, validator=None, run_command=subprocess.run):
    root = Path(spec["project_root"]).resolve()
    cfg = checked_config(root, spec["full_config_file"], spec["full_config_sha256"])
    original_folder = root / "results/runs" / cfg["run_id"]
    # A completed original full result is authoritative and is never recomputed.
    old = existing_completion(original_folder, spec["full_config_sha256"])
    if old is not None:
        return old
    root, full, cases, sources, union = validate_sources(spec, validator)
    if validate_only:
        return {"state": "validated", "planned": len(cases), "full_test_id_union_validation": union,
                "source_count": len(sources), "inference_dispatched": False, "labels_read": False}
    config_path = project_path(root, spec["full_config_file"])
    score_cfg = full
    if spec["task_id"] in DEEPFRI:
        score_cfg, config_path = deepfri_view(root, full, spec, sources)
    folder = root / "results/runs" / score_cfg["run_id"]
    folder.mkdir(parents=True, exist_ok=True)
    config_sha = file_sha(config_path)
    lock_path = root / ".local" / ("shared-scoring-" + score_cfg["run_id"] + ".lock")
    lock_path.parent.mkdir(parents=True, exist_ok=True)
    with lock_path.open("a") as lock:
        fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        old = existing_completion(folder, config_sha)
        if old is not None:
            return old
        if (folder / "native_scorer_invocation.json").exists() or (folder / "scores.json").exists():
            raise ScoringError("Native scorer already attempted; refuse repeat/replacement")
        provenance = {"schema_version": 1, "adapter_file": str(Path(__file__).resolve()),
                      "adapter_sha256": file_sha(__file__), "spec_sha256": digest(spec),
                      "original_full_configuration_sha256": spec["full_config_sha256"],
                      "native_scorer_file": spec["scorer_file"], "native_scorer_sha256": spec["scorer_sha256"],
                      "full_test_id_union_validation": union, "sources": sources,
                      "policy": "Exact original ordered case union; per-case request bytes and actual serving segments verified; original artifacts unchanged; one native scorer call; no retries, output selection or shard metric averaging."}
        manifest = {"configuration": score_cfg, "configuration_sha256": config_sha,
                    "case_contract_sha256": digest(cases), "planned_cases": len(cases),
                    "runner_sha256": spec["execution_runner_sha256"] if spec["task_id"] in DEEPFRI else file_sha(__file__),
                    "runner_role": "actual_shared_generation_runner" if spec["task_id"] in DEEPFRI else "offline_scoring_view_builder",
                    "aggregate_builder_sha256": file_sha(__file__), "aggregate_only": True,
                    "source_shard_provenance_sha256": digest(provenance),
                    "solver_tools": [], "answer_keys_available_to_solver": False, "model_selection_on_test": False,
                    "actual_generation_provenance": "source_shard_manifest.json"}
        immutable_json(folder / "run_manifest.json", manifest)
        immutable_json(folder / "source_shard_manifest.json", provenance)
        hashes = {}
        for source in sources:
            source_folder = Path(source["generation_folder"])
            for name, expected in source["raw_files_sha256"].items():
                if name in hashes:
                    raise ScoringError("Duplicate raw slot while assembling scoring view")
                install_raw(source_folder / name, folder / name, expected)
                hashes[name] = expected
        for kind in ("requests", "responses"):
            if {str(p.relative_to(folder)) for p in (folder / kind).glob("*.json")} != {name for name, h in hashes.items() if name.startswith(kind + "/") and h is not None}:
                raise ScoringError("Scoring view contains missing/extra raw files")
        output_lock = {"files_sha256": {"run_manifest.json": file_sha(folder / "run_manifest.json"),
                                       "source_shard_manifest.json": file_sha(folder / "source_shard_manifest.json"), **hashes},
                       "original_full_configuration_sha256": spec["full_config_sha256"], "native_scorer_sha256": spec["scorer_sha256"],
                       "all_missing_slots_retained": True, "labels_read": False}
        output_lock["contract_sha256"] = digest(output_lock)
        immutable_json(folder / "shared_vllm_scoring_output_lock.json", output_lock)
        command = [spec.get("python", sys.executable), "-u", str(project_path(root, spec["scorer_file"])), "--run", score_cfg["run_id"]]
        if spec["task_id"] in DEEPFRI:
            command.extend(["--config", str(config_path)])
        environment = native_environment(spec)
        immutable_json(folder / "native_scorer_invocation.json", {"started_at_pacific": now(), "argv": command,
                       "source_shard_provenance_sha256": digest(provenance), "native_scorer_sha256": spec["scorer_sha256"],
                       "output_lock_sha256": file_sha(folder / "shared_vllm_scoring_output_lock.json"),
                       "planned_denominator": len(cases), "native_metric_calls_planned": 1})
        # Recheck immutable raw bytes immediately before the first label-aware call.
        for name, expected in hashes.items():
            path = folder / name
            if (file_sha(path) if path.exists() else None) != expected:
                raise ScoringError("Raw scoring input changed after locking")
        with (folder / "native_scorer.log").open("x") as log:
            result = run_command(command, cwd=root, env=environment, stdout=log, stderr=subprocess.STDOUT)
        done = {"schema_version": 1, "shared_vllm_scoring_adapter": True,
                "generation_exit_code": 0 if all(sum(s["statuses"].values()) == s["statuses"].get("completed", 0) for s in sources) else 1,
                "scoring_exit_code": result.returncode, "finished_at_pacific": now(),
                "configuration_sha256": config_sha, "run_manifest_sha256": file_sha(folder / "run_manifest.json"),
                "source_shard_provenance_sha256": digest(provenance), "full_test_id_union_validation": union,
                "original_execution_run_ids": [s["run_id"] for s in sources], "retry_or_resampling": False,
                "native_scorer_sha256": spec["scorer_sha256"], "native_labels_and_denominator_unchanged": True}
        if result.returncode == 0:
            summary = read(folder / "scores.json")
            if summary.get("planned") != len(cases):
                raise ScoringError("Native scorer changed the original full denominator")
            # Preserve native scores verbatim; migration notes remain separate.
            done.update(scores_sha256=file_sha(folder / "scores.json"), case_scope=summary.get("case_scope"))
        immutable_json(folder / "completion.json", done)
        if result.returncode:
            raise ScoringError("Unchanged native scorer failed; preserved attempt, no automatic retry")
        return {"state": "completed", "run_id": score_cfg["run_id"], "completion": done}


@contextmanager
def source_worker_locks(spec):
    """Exclude any producer throughout provenance checks and native scoring."""
    root = Path(spec["project_root"]).resolve()
    handles = []
    try:
        folders = []
        for source in spec["sources"]:
            cfg = checked_config(root, source["config_file"], source["config_sha256"])
            folders.append(generation_folder(root, cfg, source))
        for folder in sorted(set(folders)):
            if not folder.is_dir():
                raise Pending("Source has not started: " + folder.name)
            handle = (folder / "worker.lock").open("a")
            try:
                fcntl.flock(handle, fcntl.LOCK_EX | fcntl.LOCK_NB)
            except BlockingIOError:
                handle.close()
                raise Pending("Source worker is still active: " + folder.name)
            handles.append(handle)
        yield
    finally:
        for handle in reversed(handles):
            handle.close()


def score_spec(spec, *, validate_only=False, validator=None, run_command=subprocess.run):
    root = Path(spec["project_root"]).resolve()
    full = checked_config(root, spec["full_config_file"], spec["full_config_sha256"])
    # Preserve old completed full scores without requiring their producer locks.
    old = existing_completion(root / "results/runs" / full["run_id"], spec["full_config_sha256"])
    if old is not None:
        return old
    with source_worker_locks(spec):
        return _score_spec_unlocked(spec, validate_only=validate_only,
                                    validator=validator, run_command=run_command)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--spec", required=True, type=Path)
    parser.add_argument("--validate-only", action="store_true")
    args = parser.parse_args()
    try:
        result = score_spec(read(args.spec), validate_only=args.validate_only)
    except Pending as error:
        print(json.dumps({"state": "pending", "detail": str(error), "inference_dispatched": False}))
        return 2
    print(json.dumps(result))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
