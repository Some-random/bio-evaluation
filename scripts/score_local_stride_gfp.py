"""Offline qualified GFP proxy scoring, after locking every one of200 slots."""
from __future__ import annotations

import argparse
import base64
from collections import Counter
import csv
import datetime as dt
import fcntl
import json
import math
from pathlib import Path

import run_local_stride_gfp as runner
import stride_gfp_qualified_contract as contract
import stride_gfp_cpu_oracle as oracle_runtime

ROOT = Path(__file__).resolve().parents[1]
ORACLE_HELPER = "scripts/stride_gfp_cpu_oracle.py"
SOURCE_CONTRACT = "data/proxy_generation_native/P42/native_reference_contract.json"
digest = oracle_runtime.digest
file_sha = oracle_runtime.file_sha
save = oracle_runtime.save


def read(path): return json.loads(Path(path).read_text())


def verify_frozen_run(folder):
    manifest = read(folder / "run_manifest.json"); cfg = manifest["configuration"]
    runner.validate_settings(cfg)
    if (cfg.get("oracle_forward_authorized") is not True or cfg.get("scorer_python") != ".venv-oracles/bin/python"
            or cfg.get("oracle_runtime_file") != oracle_runtime.RUNTIME_FILE
            or cfg.get("oracle_state_audit_file") != oracle_runtime.AUDIT_FILE
            or cfg.get("native_oracle_source_file") != oracle_runtime.NATIVE_SOURCE
            or cfg.get("native_oracle_source_sha256") != oracle_runtime.NATIVE_SHA256):
        raise ValueError("Concrete isolated CPU oracle scope is disabled or changed")
    frozen = cfg["frozen_files_sha256"]
    required = {runner.RUNNER, runner.EXECUTOR, runner.SCORER, ORACLE_HELPER, SOURCE_CONTRACT,
        "scripts/stride_gfp_qualified_contract.py", cfg["source_proposal_file"], cfg["input_file"], cfg["review_file"],
        cfg["oracle_runtime_file"], cfg["oracle_state_audit_file"], oracle_runtime.NATIVE_SOURCE}
    if not required <= set(frozen): raise ValueError("Scorer/helper/runtime/source/input/review must all be frozen")
    for name, expected in frozen.items():
        path = ROOT / name
        if not path.resolve().is_relative_to(ROOT.resolve()) or file_sha(path) != expected:
            raise ValueError("Frozen run dependency changed: " + name)
    for name, key in [(cfg["oracle_runtime_file"], "oracle_runtime_sha256"), (cfg["oracle_state_audit_file"], "oracle_state_audit_sha256"),
                      (cfg["source_proposal_file"], "source_proposal_sha256")]:
        if file_sha(ROOT / name) != cfg[key]: raise ValueError("Dedicated frozen metadata hash changed: " + name)
    proposal = read(ROOT / cfg["source_proposal_file"])
    expected = []
    for part in proposal["inputs"]:
        if file_sha(ROOT / part["path"]) != part["sha256"]: raise ValueError("Original regime input changed")
        expected += [json.loads(line) for line in (ROOT / part["path"]).read_text().splitlines() if line]
    cases = read(folder / "case_inputs.json")
    configured_cases = [json.loads(line) for line in (ROOT / cfg["input_file"]).read_text().splitlines() if line]
    review = read(ROOT / cfg["review_file"])
    if (len(cases) != 200 or cases != expected or cases != configured_cases
            or len({c["case_id"] for c in cases}) != 200 or review.get("reviewed") is not True
            or review.get("approved_case_ids") != [c["case_id"] for c in cases] or review.get("held_cases") != []
            or review.get("approved_task_ids") != ["P42"] or manifest.get("case_contract_sha256") != digest(cases)
            or manifest.get("planned_cases") != 200 or manifest.get("runner_sha256") != frozen[runner.RUNNER]):
        raise ValueError("Exact complete200 case/input/review/manifest identity changed")
    if manifest.get("solver_tools", []) != [] or manifest.get("answer_keys_available_to_solver", False):
        raise ValueError("Unexpected solver reference/tool access")
    source = read(ROOT / SOURCE_CONTRACT)
    if (source["task_id"] != "P42" or source["sequence_sha256"] != cfg["source_sequence_sha256"]
            or __import__("hashlib").sha256(source["sequence"].encode()).hexdigest() != source["sequence_sha256"]
            or len(source["sequence"]) != source["length"]): raise ValueError("Original complete benign GFP source changed")
    for case in cases: runner.payload_for(case, cfg)
    return cfg, cases, source["sequence"], proposal


def lock_generation(folder, cfg, cases):
    """Verify source generation seal, then create an independent immutable lock."""
    seal = read(folder / "generation_artifact_lock.json"); terminal = read(folder / "generation_completion.json")
    if (seal.get("schema_version") != 1 or seal.get("run_id") != cfg["run_id"] or seal.get("planned_cases") != 200
            or len(seal.get("slots", [])) != 200 or seal.get("oracle_forward_performed") is not False
            or seal.get("run_manifest_sha256") != file_sha(folder / "run_manifest.json")
            or seal.get("case_inputs_sha256") != file_sha(folder / "case_inputs.json")
            or seal.get("generation_completion_sha256") != file_sha(folder / "generation_completion.json")
            or terminal.get("run_id") != cfg["run_id"] or terminal.get("planned_cases") != 200
            or terminal.get("oracle_forward_performed") is not False or terminal.get("scoring_complete") is not False):
        raise ValueError("All200 generation slots must be sealed before oracle scoring")
    names = {runner.request_identity(case) + ".json" for case in cases}
    for kind in ("requests", "responses"):
        if not {path.name for path in (folder / kind).glob("*.json")} <= names: raise ValueError("Extra raw generation identity")
    hashes = {name: file_sha(folder / name) for name in ["run_manifest.json", "case_inputs.json", "generation_completion.json", "generation_artifact_lock.json"]}
    statuses = Counter()
    allowed_statuses = {"completed", "transport_error", "server_error", "response_schema_error", "interrupted_unknown_completion", "not_dispatched_after_error", "worker_exception"}
    for case, slot in zip(cases, seal["slots"]):
        identity = runner.request_identity(case)
        expected = {"case_id": case["case_id"], "regime": runner.case_regime(case), "sample_index": case["sample_index"],
            "seed": case["seed"], "identity": identity}
        if any(slot.get(key) != value for key, value in expected.items()): raise ValueError("Sealed candidate identity/order changed")
        if slot.get("status") not in allowed_statuses: raise ValueError("Unknown terminal generation status")
        statuses[slot["status"]] += 1
        for kind, prefix in [("requests", "request"), ("responses", "response")]:
            name = kind + "/" + identity + ".json"; path = folder / name
            actual = file_sha(path) if path.exists() else None
            if slot.get(prefix + "_file_sha256") != actual or slot.get(prefix + "_file") != (name if actual is not None else None):
                raise ValueError("Raw artifact or locked missing slot changed")
            hashes[name] = actual
    complete = statuses["completed"] == 200
    if (dict(statuses) != terminal.get("statuses") or complete != terminal.get("generation_complete")
            or complete != seal.get("generation_complete") or type(terminal.get("generation_exit_code")) is not int
            or terminal["generation_exit_code"] != (0 if complete else 1)):
        raise ValueError("Terminal status denominator/completeness changed")
    lock = {"files_sha256": hashes, "contract_sha256": digest(hashes), "planned_cases": 200,
        "policy": "All original200 requests/responses and every missing slot immutable before any source/candidate oracle forward. No resampling/selection, source once then unique eligible computational cache only.",
        "generation_complete": complete, "generation_exit_code": terminal["generation_exit_code"]}
    path = folder / "scoring_output_lock.json"
    if path.exists() and read(path) != lock: raise ValueError("Scoring output lock changed")
    if not path.exists(): save(path, lock)
    return lock, seal["slots"]


def locked_record(folder, name, lock):
    path = folder / name; expected = lock["files_sha256"][name]
    if expected is None:
        if path.exists(): raise ValueError("Raw output appeared in locked missing slot")
        return None
    if file_sha(path) != expected: raise ValueError("Raw artifact changed after scoring lock")
    return read(path)


def validated_samples(folder, cfg, cases, source, lock, slots):
    samples = {regime: [] for regime in contract.REGIMES}; seen_sequences = set(); unique = []
    for case, slot in zip(cases, slots):
        identity = runner.request_identity(case); regime = runner.case_regime(case)
        request = locked_record(folder, "requests/" + identity + ".json", lock)
        response = locked_record(folder, "responses/" + identity + ".json", lock)
        metadata = {key: case[key] for key in ("task_id", "case_id", "protocol_variant", "split", "sample_index", "seed")}
        expected = {**metadata, "task": "P42", "variant": case["protocol_variant"], "regime": regime}
        payload = runner.payload_for(case, cfg)
        if request is not None:
            body = json.dumps(payload, ensure_ascii=False)
            if (any(request.get(key) != value for key, value in expected.items()) or request.get("payload") != payload
                    or request.get("request_sha256") != digest(payload) or request.get("wire_request_body_utf8") != body
                    or request.get("wire_request_body_sha256") != __import__("hashlib").sha256(body.encode()).hexdigest()):
                raise ValueError("Archived request identity/native roles/recipe/wire bytes changed")
        final = reasoning = finish = None
        if response is not None:
            if request is None or any(response.get(key) != value for key, value in expected.items()): raise ValueError("Raw response identity/request missing")
            if (response.get("model") != cfg["model"] or response.get("model_revision") != cfg["model_revision"]
                    or response.get("request_sha256") != digest(payload) or response.get("status") != slot["status"]):
                raise ValueError("Raw response model/recipe/status mismatch")
            wire = base64.b64decode(response["raw_response_base64"], validate=True)
            if (__import__("hashlib").sha256(wire).hexdigest() != response["raw_response_sha256"]
                    or wire.decode("utf-8", errors="replace") != response["raw_response_utf8"]): raise ValueError("Raw response bytes changed")
            if slot["status"] == "completed":
                if response.get("http_status") != 200 or response.get("transport_or_schema_error") is not None or json.loads(wire) != response["response"]:
                    raise ValueError("Completed response is not its successful original wire object")
                channels = runner.extract_choice(response["response"])
                if any(response.get(key) != value for key, value in channels.items()): raise ValueError("Generated reasoning/final channels changed")
                final, reasoning, finish = channels["final_text"], channels["reasoning_text"], channels["finish_reason"]
                parsed = contract.parse_channels(final, reasoning)
                if response.get("candidate_extraction") != {**parsed, **contract.validate_endpoint(source, parsed["protein"], regime)}:
                    raise ValueError("Archived extraction differs from frozen parser/endpoint contract")
        elif slot["status"] == "completed": raise ValueError("Completed slot lacks response")
        error = slot["status"] != "completed"
        parsed = contract.parse_channels(final, reasoning); valid = contract.validate_endpoint(source, parsed["protein"], regime)
        eligible = not error and parsed["valid_format"] and valid["eligible"]
        if eligible and parsed["protein"] not in seen_sequences:
            seen_sequences.add(parsed["protein"]); unique.append(parsed["protein"])
        samples[regime].append({"sample_index": case["sample_index"], "case_id": case["case_id"], "regime": regime, "seed": case["seed"],
            "final_text": final, "reasoning_text": reasoning, "finish_reason": finish, "status": slot["status"],
            "generation_error": slot["status"] if error else None, "oracle_score": None,
            "eligible_before_oracle": bool(eligible), "candidate_sequence": parsed["protein"] if eligible else None})
    if any(len(samples[regime]) != 100 for regime in contract.REGIMES) or len(unique) > 200:
        raise ValueError("Fixed100-per-regime budget changed")
    return samples, unique


def evaluate_unique(source, unique, oracle, folder, lock_sha, batch_size=8):
    """One source plus <=200 unique eligible endpoints, no selection feedback."""
    if len(unique) > 200 or len(unique) != len(set(unique)) or source in unique or batch_size != 8:
        raise ValueError("Invalid fixed unique candidate oracle plan")
    invocation = folder / "oracle_scoring_invocation.json"
    if invocation.exists(): raise ValueError("Oracle scoring was already invoked; no automatic repeat/retry")
    order = [source, *unique]
    save(invocation, {"scoring_output_lock_sha256": lock_sha, "source_plus_unique_sequence_count": len(order),
        "ordered_sequence_sha256": [__import__("hashlib").sha256(sequence.encode()).hexdigest() for sequence in order],
        "batch_size": 8, "device": "cpu", "dtype": "float32", "started_at_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
        "deduplication_policy": "Computational cache only; every duplicate maps back to its original slot/denominator. No feedback/resampling."})
    cache, errors = {}, []
    for batch in [[source]] + [unique[start:start + 8] for start in range(0, len(unique), 8)]:
        try:
            values = oracle.predict(batch)
            if len(values) != len(batch): raise ValueError("Oracle batch output count differs")
            for sequence, value in zip(batch, values):
                if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value):
                    cache[sequence] = None; errors.append({"sequence_sha256": __import__("hashlib").sha256(sequence.encode()).hexdigest(), "error": "nonfinite_or_invalid_oracle_scalar"})
                else: cache[sequence] = float(value)
        except Exception as exc:
            for sequence in batch: cache[sequence] = None
            errors.append({"batch_sequence_sha256": [__import__("hashlib").sha256(sequence.encode()).hexdigest() for sequence in batch], "error_type": type(exc).__name__, "retry": False})
    records = [{"sequence": sequence, "sequence_sha256": __import__("hashlib").sha256(sequence.encode()).hexdigest(),
        "role": "source" if index == 0 else "unique_eligible_candidate", "oracle_score": cache[sequence]} for index, sequence in enumerate(order)]
    save(folder / "oracle_sequence_scores.json", {"ordered_scores": records, "errors": errors, "distinct_sequences_attempted": len(order),
        "maximum_allowed_distinct_sequences": 201, "batch_size": 8, "scoring_output_lock_sha256": lock_sha})
    return cache, errors


def score(folder, oracle_factory=None):
    # A second direct scorer process cannot run the same fixed cohort twice.
    with (folder / "oracle_scoring_worker.lock").open("a") as worker_lock:
        fcntl.flock(worker_lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        return _score_locked(folder, oracle_factory)


def _score_locked(folder, oracle_factory=None):
    cfg, cases, source, proposal = verify_frozen_run(folder)
    lock, slots = lock_generation(folder, cfg, cases)
    lock_file_sha = file_sha(folder / "scoring_output_lock.json")
    samples, unique = validated_samples(folder, cfg, cases, source, lock, slots)
    done_path = folder / "oracle_scoring_completion.json"
    if done_path.exists():
        done = read(done_path)
        if done["scoring_output_lock_sha256"] != lock_file_sha: raise ValueError("Completed oracle cohort changed")
        for name, expected in done["files_sha256"].items():
            if file_sha(folder / name) != expected: raise ValueError("Completed oracle score artifact changed")
        return read(folder / "scores.json")
    if (folder / "oracle_scoring_invocation.json").exists(): raise ValueError("Interrupted prior oracle evaluation; preserve outputs, no automatic repeat")
    # A factory is injectable only for synthetic unit tests. The CLI has no
    # alternate scorer, checkpoint, threshold or candidate-selection option.
    if oracle_factory is None:
        oracle, restoration = oracle_runtime.load_oracle(proposal["oracle"]["assets"], cfg["oracle_runtime_sha256"], cfg["oracle_state_audit_sha256"])
    else: oracle, restoration = oracle_factory()
    cache, errors = evaluate_unique(source, unique, oracle, folder, lock_file_sha)
    baseline = cache[source]; by_regime = {}; per_case = []
    for regime in contract.REGIMES:
        for sample in samples[regime]:
            if sample["eligible_before_oracle"]: sample["oracle_score"] = cache[sample["candidate_sequence"]]
        if baseline is None:
            result = {"regime": regime, "planned_samples": 100, "scoring_complete": False,
                "qualified_oracle_success": None, "improved_sequence_uniqueness": None, "native_novelty": None,
                "withheld_reason": "source_oracle_score_missing_or_nonfinite", "trajectory_correctness": "unassessed", "mechanistic_rationale_correctness": "unassessed"}
            details = []
            for sample in sorted(samples[regime], key=lambda row: row["sample_index"]):
                parsed = contract.parse_channels(sample["final_text"], sample["reasoning_text"])
                validity = contract.validate_endpoint(source, parsed["protein"], regime)
                if sample["generation_error"]: validity.update(eligible=False, reason="generation_error")
                elif not parsed["valid_format"]: validity.update(eligible=False, reason="invalid_source_format_after_declared_channel_reconstruction")
                details.append({"sample_index": sample["sample_index"], **parsed, **validity,
                    "oracle_score": sample["oracle_score"], "oracle_improved": None})
            result["sample_details"] = details
        else: result = contract.summarize(source, regime, samples[regime], baseline, expected_samples=100)
        details = result.pop("sample_details", [])
        for sample, detail in zip(sorted(samples[regime], key=lambda row: row["sample_index"]), details):
            per_case.append({"case_id": sample["case_id"], "regime": regime, "seed": sample["seed"], "status": sample["status"], **detail})
        by_regime[regime] = result
    generation_complete = lock["generation_complete"]
    finite_oracle_complete = baseline is not None and all(result["scoring_complete"] for result in by_regime.values())
    metrics = {regime: {key: result[key] for key in ["qualified_oracle_success", "improved_sequence_uniqueness", "native_novelty"]} for regime, result in by_regime.items()}
    statuses = Counter(slot["status"] for slot in slots); completed = statuses["completed"]
    summary = {"run_id": cfg["run_id"], "task_id": "P42", "model": cfg["model"], "model_revision": cfg["model_revision"],
        "protocol_variant": cfg["variant"], "protocol_kind": "qualified_adaptation", "native_paper_replication": False,
        "planned": 200, "completed": completed, "parsed": sum(contract.parse_channels(row["final_text"], row["reasoning_text"])["valid_format"] for group in samples.values() for row in group),
        "invalid_outputs": sum(not row["eligible_before_oracle"] for group in samples.values() for row in group),
        "missing_or_failed_outputs": 200 - completed, "statuses": dict(statuses),
        "finish_reasons": dict(Counter(row["finish_reason"] for group in samples.values() for row in group if row["status"] == "completed")),
        "case_scope": "qualified_full200_two_endpoint_regimes_native_novelty_withheld" if generation_complete else "INCOMPLETE_generation_all200_slots_retained",
        "generation_completeness": "complete" if generation_complete else "incomplete_failures_retained_no_fullcompletion_claim",
        "qualified_proxy_metrics_complete": finite_oracle_complete, "full_native_metric_set_complete": False,
        "full_planned_primary_metrics_valid": finite_oracle_complete,
        "primary_metric_names": [regime + ".qualified_oracle_success" for regime in contract.REGIMES],
        "metrics": metrics, "metric_units": "Fractions0–1; success over100 original slots per regime, uniqueness over improved sample count; undefined remainsnull",
        "regime_summaries": by_regime, "source_oracle_score": baseline, "distinct_oracle_sequences_attempted": 1 + len(unique),
        "oracle_unique_eligible_candidate_count": len(unique), "oracle_forward_budget_max_distinct_sequences": 201,
        "eligible_duplicate_slot_count": sum(row["eligible_before_oracle"] for group in samples.values() for row in group) - len(unique),
        "oracle_errors": errors, "oracle_runtime_sha256": cfg["oracle_runtime_sha256"], "oracle_state_restoration_sha256": cfg["oracle_state_audit_sha256"],
        "scoring_output_lock_sha256": lock_file_sha, "generation_artifact_contract_sha256": lock["contract_sha256"],
        "all200_generations_locked_before_oracle_forward": True,
        "native_novelty": None, "native_novelty_withheld_reason": "Exact positive SFT training membership D+ unavailable; no substitute corpus",
        "oracle_qualification": "Pinned original SaProt650M + trained fluorescence LoRA and active trained classifier; native AA# masking/EsmTokenizer max1024/padding/truncation; FP32CPU eval/no_grad,8intra/1inter-op threads,batch8. Historical device/library equality unverified.",
        "native_protocol_qualification": "Qualified endpoint1..3 budget, explicit distinct HTTP seeds, native system/user roles, declared reasoning/final reconstruction; no native edit-trajectory or native-paper replication claim. Source once, first-occurrence unique eligible candidate cache only; duplicates remain in100-slot denominators.",
        "interpretation": cfg["interpretation"], "explanation_support_score": None, "trajectory_correctness": "unassessed", "mechanistic_rationale_correctness": "unassessed",
        "reference_evidence": "Fixed trained fluorescence predictor proxy, not new laboratory measurements", "contamination": "Prior exposure to public GFP data and oracle training overlap unknown"}
    save(folder / "per_case_scores.json", per_case); save(folder / "scores.json", summary)
    with (folder / "metrics.csv").open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["run_id", "task_id", "protocol_variant", "regime", "metric", "value", "planned", "completed", "case_scope"])
        writer.writeheader()
        for regime, values in metrics.items():
            for name, value in values.items(): writer.writerow({"run_id": cfg["run_id"], "task_id": "P42", "protocol_variant": cfg["variant"],
                "regime": regime, "metric": name, "value": value, "planned": 100, "completed": sum(row["status"] == "completed" for row in samples[regime]), "case_scope": summary["case_scope"]})
    names = ["scores.json", "per_case_scores.json", "metrics.csv", "oracle_sequence_scores.json", "oracle_scoring_invocation.json", "scoring_output_lock.json"]
    save(done_path, {"scoring_output_lock_sha256": lock_file_sha, "generation_exit_code": lock["generation_exit_code"],
        "qualified_proxy_metrics_complete": finite_oracle_complete, "full_native_metric_set_complete": False,
        "files_sha256": {name: file_sha(folder / name) for name in names}, "oracle_forward_retries": False,
        "finished_at_utc": dt.datetime.now(dt.timezone.utc).isoformat()})
    print(json.dumps({"task_id": "P42", "planned": 200, "completed": completed, "metrics": metrics, "native_novelty": None}))
    return summary


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__); parser.add_argument("--run", required=True)
    args = parser.parse_args()
    if not __import__("re").fullmatch(r"[A-Za-z0-9_.-]+", args.run): parser.error("Invalid run ID")
    result = score(ROOT / "results/runs" / args.run)
    raise SystemExit(0 if result["qualified_proxy_metrics_complete"] else 1)
