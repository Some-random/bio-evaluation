#!/usr/bin/env python3
"""Offline output-only diagnosis; never repairs predictions or dispatches inference.

Stage `classify` freezes all output diagnoses before opening scorer references.
Stage `metrics` uses that immutable evidence to compare the original parsed
subset with an all-zero reference on exactly the same case/class positions.
"""
from __future__ import annotations
import argparse
import ast
from collections import Counter
from datetime import datetime
import gzip
import hashlib
import json
import math
from pathlib import Path
import re
import sys
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parents[1]
DEST = ROOT / "results/offline_diagnostics/deepfri_failure_analysis_2026-10-19"
PREPARED = ROOT / ".local/evaluation_revision_2026-10-18/scoring/null_equivalence_recovery_v1/prepared_v2"
TASKS = ("P12", "P13", "P14", "P15")
SOURCE = "sources/deepfri_contract_audit_2026-10-15/torchdrug__torchdrug__metrics__metric.py"
SOURCE_SHA = "760f376d4125ab2cc9332c9e83b944d4464da51aea577d75266d9247aca81776"
RULES = {
    "version": "DEEPFRI_OUTPUT_FAILURE_PARTITION_V1",
    "no_prediction_repair": True,
    "reference_blind": True,
    "partition_precedence": ["valid", "unfinished_nonstop", "empty_final", "malformed_json", "duplicate_conflicting", "duplicate_identical_only", "wrong_schema", "unknown_identifier", "numeric_string", "wrong_value_type", "nonnumeric_string", "nonfinite_numeric", "out_of_range_numeric"],
    "crosscuts": "All syntactically observable violations are retained even when another violation has partition priority; completed nonempty length-finished JSON is inspected but never made valid.",
    "numeric_string": "String matching optional ASCII sign, decimal/scientific notation, and outer whitespace; no conversion applied.",
    "duplicates": "All JSON objects inspected. Equal finite JSON numbers compare numerically; booleans are distinct from numbers. Object pairs and order retained; conflicting and identical duplicates may coexist.",
    "missing_reference_policy": "Fail closed; no guessed case labels or baseline.",
    "subset_policy": "Use original corrected scorer's valid case IDs and vectors unchanged. All-zero baseline uses those exact ordered case IDs and full original class order.",
    "completeness_policy": "Requiring every planned vector before a full-test primary score is local evaluation policy, separate from the underlying AP/Fmax formulas.",
}
NUMERIC = re.compile(r"^[+-]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][+-]?\d+)?$")

def digest(obj):
    return hashlib.sha256(json.dumps(obj, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode()).hexdigest()

def sha(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as f:
        for block in iter(lambda: f.read(8 * 1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()

def read(path):
    return json.loads(Path(path).read_text())

def write(path, obj):
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    Path(path).write_text(json.dumps(obj, ensure_ascii=False, indent=2, allow_nan=False) + "\n")

def jsonl_gz(path, rows):
    with Path(path).open("wb") as raw:
        with gzip.GzipFile(filename="", fileobj=raw, mode="wb", mtime=0) as f:
            for row in rows:
                f.write((json.dumps(row, ensure_ascii=False, allow_nan=False) + "\n").encode())

def load_gz(path):
    with gzip.open(path, "rt") as f:
        return [json.loads(line) for line in f]

class Pairs(list):
    """Keep object pairs distinct from JSON arrays, including duplicate keys."""

def same(a, b):
    if isinstance(a, bool) or isinstance(b, bool):
        return type(a) is type(b) and a == b
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return a == b
    if type(a) is not type(b):
        return False
    return a == b

def classify(text, finish, permitted):
    flags, details = set(), {"unknown_identifiers": [], "numeric_string_keys": [], "wrong_value_types": [], "nonnumeric_string_keys": [], "nonfinite_numeric_keys": [], "out_of_range_keys": [], "duplicate_identical_keys": [], "duplicate_conflicting_keys": []}
    if finish != "stop":
        flags.add("unfinished_nonstop")
    if not isinstance(text, str) or not text.strip():
        flags.add("empty_final")
        return {"partition": "unfinished_nonstop" if finish != "stop" else "empty_final", "flags": sorted(flags), "details": details}
    try:
        value = json.loads(text, object_pairs_hook=Pairs)
    except (ValueError, TypeError):
        flags.add("malformed_json")
        return {"partition": "unfinished_nonstop" if finish != "stop" else "malformed_json", "flags": sorted(flags), "details": details}

    def walk(obj, path):
        if isinstance(obj, Pairs):
            seen = {}
            for key, val in obj:
                loc = path + "." + key
                if key in seen:
                    kind = "duplicate_identical_keys" if same(seen[key], val) else "duplicate_conflicting_keys"
                    details[kind].append(loc)
                seen[key] = val
                walk(val, loc)
        elif isinstance(obj, list):
            for index, val in enumerate(obj):
                walk(val, path + f"[{index}]")
    walk(value, "$")
    if details["duplicate_conflicting_keys"]:
        flags.add("duplicate_conflicting")
    if details["duplicate_identical_keys"]:
        flags.add("duplicate_identical_only")
    if not isinstance(value, Pairs) or len(value) != 1 or value[0][0] != "scores" or not isinstance(value[0][1], Pairs):
        flags.add("wrong_schema")
    else:
        for key, val in value[0][1]:
            if key not in permitted:
                details["unknown_identifiers"].append(key)
                flags.add("unknown_identifier")
            if isinstance(val, str):
                kind = "numeric_string" if NUMERIC.fullmatch(val.strip()) else "nonnumeric_string"
                details[kind + "_keys"].append(key)
                flags.add(kind)
            elif isinstance(val, bool) or not isinstance(val, (int, float)):
                details["wrong_value_types"].append({"key": key, "type": "object" if isinstance(val, Pairs) else type(val).__name__})
                flags.add("wrong_value_type")
            elif not math.isfinite(val):
                details["nonfinite_numeric_keys"].append(key)
                flags.add("nonfinite_numeric")
            elif not 0 <= val <= 1:
                details["out_of_range_keys"].append(key)
                flags.add("out_of_range_numeric")
    partition = next((item for item in RULES["partition_precedence"] if item in flags), "valid")
    return {"partition": partition, "flags": sorted(flags), "details": details}

def locked(path, expected):
    if not expected or sha(path) != expected:
        raise ValueError(f"Locked bytes changed: {path}")
    return read(path)

def locate(task):
    project = PREPARED / task.lower() / "project"
    runs = list((project / "results/runs").glob("*null_equivalence_v1"))
    if len(runs) != 1:
        raise ValueError("Require one exact corrected run")
    return project, runs[0]

def classify_stage(dest):
    dest.mkdir(parents=True, exist_ok=True)
    frozen_rules = {"rules": RULES, "rules_sha256": digest(RULES), "script_sha256": sha(__file__), "tests_sha256": sha(ROOT / "tests/test_analyze_deepfri_failures.py")}
    if (dest / "classification_rules.json").exists() and read(dest / "classification_rules.json") != frozen_rules:
        raise ValueError("Classification already frozen with different rules/code")
    write(dest / "classification_rules.json", frozen_rules)
    summaries = []
    for task in TASKS:
        project, run = locate(task)
        manifest = read(run / "run_manifest.json")
        cfg = manifest["configuration"]
        lock = read(run / "scoring_output_lock.json")
        if digest(lock["files_sha256"]) != lock["contract_sha256"]:
            raise ValueError("Original output lock corrupt")
        hashes = lock["files_sha256"]
        if sha(run / "run_manifest.json") != hashes["run_manifest.json"]:
            raise ValueError("Run manifest changed")
        configuration_path = project / "configs" / (cfg["run_id"] + ".json")
        if sha(configuration_path) != manifest["configuration_sha256"] or read(configuration_path) != cfg or cfg["approved_task_ids"] != [task]:
            raise ValueError("Run configuration changed")
        input_path = project / cfg["input_file"]
        if sha(input_path) != hashes["frozen_source/input_file"]:
            raise ValueError("Input bytes changed")
        cases = [json.loads(line) for line in input_path.read_text().splitlines()]
        if digest(cases) != manifest["case_contract_sha256"] or len(cases) != manifest["planned_cases"]:
            raise ValueError("Original ordered case contract changed")
        review = locked(project / cfg["review_file"], hashes["frozen_source/review_file"])
        ids = [case["case_id"] for case in cases]
        if len(set(ids)) != len(ids) or ids != review["approved_case_ids"]:
            raise ValueError("Reviewed case IDs changed")
        vocab = locked(project / cfg["class_vocabulary_file"], hashes["frozen_source/class_vocabulary_file"])
        classes = [row["class_id"] for row in vocab["classes"]]
        scores = read(run / "scores.json")
        completion = read(run / "completion.json")
        if sha(run / "scores.json") != completion["scores_sha256"]:
            raise ValueError("Corrected score bytes changed")
        original = read(run / "per_case_scores.json")
        if [row["case_id"] for row in original] != ids:
            raise ValueError("Original scored case IDs changed")
        by_id = {row["case_id"]: row for row in original}
        budget = read(run / "per_case_budget_map.json")["budgets_by_raw_filename"]
        rows, inventory = [], []
        for case in cases:
            name = digest([case["task"], case["variant"], case["case_id"]]) + ".json"
            request = locked(run / "requests" / name, hashes["requests/" + name])
            response = locked(run / "responses" / name, hashes["responses/" + name])
            if any(request.get(k) != case[k] for k in ("task", "case_id", "variant", "split")) or digest(request["payload"]) != request["request_sha256"]:
                raise ValueError("Request association changed")
            expected_payload = {"model": cfg["model"], "messages": case["messages"], **cfg["generation"]}
            expected_payload["max_tokens"] = budget[name]
            if request["payload"] != expected_payload:
                raise ValueError("Request differs from frozen prompt/generation/budget")
            expected_identity = {"task": task, "case_id": case["case_id"], "variant": case["variant"], "split": case["split"], "model": cfg["model"], "model_revision": cfg["model_revision"], "request_sha256": request["request_sha256"]}
            if any(response.get(k) != v for k, v in expected_identity.items()) or response["status"] != "completed" or response["http_status"] != 200:
                raise ValueError("Response association/completion changed")
            raw = response["response"]
            if raw["model"] != cfg["model"] or len(raw["choices"]) != 1:
                raise ValueError("Raw response model/count changed")
            choice = raw["choices"][0]
            text = choice["message"].get("content")
            if ("" if text is None else text) != response["text"] or choice["finish_reason"] != response["finish_reason"]:
                raise ValueError("Raw and saved final differ beyond approved null/empty equivalence")
            diagnosis = classify(text, choice["finish_reason"], set(classes))
            saved = by_id[case["case_id"]]
            if (diagnosis["partition"] == "valid") != saved["valid_confidence_vector"]:
                raise ValueError("Diagnostic validity disagrees with native corrected scorer")
            rows.append({"task_id": task, "case_id": case["case_id"], "final_text": text, "finish_reason": choice["finish_reason"], "output_budget": budget[name], "native_valid": saved["valid_confidence_vector"], "native_error": saved["parse_error"], "sparse_scores": saved["sparse_scores"], **diagnosis})
            inventory.append({"case_id": case["case_id"], "filename": name, "request_sha256": hashes["requests/" + name], "response_sha256": hashes["responses/" + name], "payload_sha256": request["request_sha256"]})
        path = dest / f"{task}_output_diagnoses.jsonl.gz"
        jsonl_gz(path, rows)
        jsonl_gz(dest / f"{task}_source_inventory.jsonl.gz", inventory)
        # Reference paths/digests are locked, but no labels are read at this stage.
        item = {"task_id": task, "run_id": cfg["run_id"], "planned": len(rows), "valid": sum(r["native_valid"] for r in rows), "invalid": sum(not r["native_valid"] for r in rows), "partition": dict(Counter(r["partition"] for r in rows)), "crosscuts": dict(Counter(flag for r in rows for flag in r["flags"])), "finish_reasons": dict(Counter(r["finish_reason"] for r in rows)), "native_error_counts": dict(Counter(r["native_error"] for r in rows if r["native_error"])), "diagnoses_sha256": sha(path), "inventory_sha256": sha(dest / f"{task}_source_inventory.jsonl.gz"), "reference_sha256": hashes["frozen_source/scorer_reference_file"], "class_ids": classes, "class_vocabulary_sha256": hashes["frozen_source/class_vocabulary_file"], "case_contract_sha256": manifest["case_contract_sha256"], "ordered_case_ids_sha256": digest(ids), "manifest_sha256": sha(run / "run_manifest.json"), "score_sha256": sha(run / "scores.json"), "original_parsed_metrics": scores["metrics"]["PARSED_ONLY_DIAGNOSTIC"], "original_full_set_all_zero_reference": scores["metrics"]["OFFLINE_ALL_ZERO_REFERENCE"], "duplicate_crosscuts": {kind: sum(bool(r["details"][kind]) for r in rows) for kind in ("duplicate_identical_keys", "duplicate_conflicting_keys")}}
        if item["valid"] != scores["parsed"] or item["native_error_counts"] != scores["parse_error_counts"]:
            raise ValueError("Original score counts not reproduced")
        summaries.append(item)
    frozen = {"version": RULES["version"], "stage": "output_classification_frozen_before_reference_read", "frozen_at_pacific": datetime.now(ZoneInfo("America/Los_Angeles")).isoformat(), "reference_labels_read": False, **frozen_rules, "tasks": summaries}
    write(dest / "classification_frozen.json", frozen)
    print(json.dumps({"stage": frozen["stage"], "sha256": sha(dest / "classification_frozen.json"), "tasks": [{k: t[k] for k in ("task_id", "valid", "invalid", "partition", "duplicate_crosscuts")} for t in summaries]}))

def clean_numbers(value):
    if isinstance(value, float) and not math.isfinite(value):
        return None
    if isinstance(value, dict):
        return {k: clean_numbers(v) for k, v in value.items()}
    if isinstance(value, list):
        return [clean_numbers(v) for v in value]
    return value

def metrics_stage(dest):
    import torch
    import numpy as np
    import platform
    torch.set_num_threads(1)
    torch.set_num_interop_threads(1)
    frozen_path = dest / "classification_frozen.json"
    frozen = read(frozen_path)
    if frozen["rules_sha256"] != digest(RULES) or frozen["script_sha256"] != sha(__file__):
        raise ValueError("Classification rule/code changed after freeze")
    results = []
    for item in frozen["tasks"]:
        task = item["task_id"]
        project, run = locate(task)
        cfg = read(run / "run_manifest.json")["configuration"]
        if sha(run / "run_manifest.json") != item["manifest_sha256"] or sha(run / "scores.json") != item["score_sha256"]:
            raise ValueError("Original provenance changed")
        if sha(dest / f"{task}_output_diagnoses.jsonl.gz") != item["diagnoses_sha256"]:
            raise ValueError("Output diagnoses changed since freeze")
        rows = load_gz(dest / f"{task}_output_diagnoses.jsonl.gz")
        ref_path = project / cfg["scorer_reference_file"]
        if sha(ref_path) != item["reference_sha256"]:
            raise ValueError("Locked references changed")
        refs = {}
        for ref in map(json.loads, ref_path.read_text().splitlines()):
            inds, terms = ref["positive_class_indices"], ref["positive_class_ids"]
            if ref["task_id"] != task or ref["scorer_only"] is not True or ref["case_id"] in refs or len(inds) != len(terms) or len(set(inds)) != len(inds) or any(type(i) is not int or not 0 <= i < len(item["class_ids"]) or item["class_ids"][i] != t for i, t in zip(inds, terms)):
                raise ValueError("Reference identity/index contract changed")
            refs[ref["case_id"]] = inds
        if set(refs) != {r["case_id"] for r in rows}:
            raise ValueError("Reference case set differs from exact output case set")
        source = project / SOURCE
        if sha(source) != SOURCE_SHA:
            raise ValueError("Native metric source changed")
        tree = ast.parse(source.read_text())
        nodes = [n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name in ("area_under_prc", "f1_max")]
        if len(nodes) != 2:
            raise ValueError("Native metric source incomplete")
        for n in nodes:
            n.decorator_list = []
        namespace = {"torch": torch}
        exec(compile(ast.Module(body=nodes, type_ignores=[]), str(source), "exec"), namespace)
        valid = [r for r in rows if r["native_valid"]]
        lookup = {c: i for i, c in enumerate(item["class_ids"])}
        scores = torch.zeros((len(valid), len(lookup)), dtype=torch.float32)
        target = torch.zeros_like(scores, dtype=torch.int64)
        for index, row in enumerate(valid):
            target[index, refs[row["case_id"]]] = 1
            for key, val in row["sparse_scores"].items():
                scores[index, lookup[key]] = val
        def tied_ap(values):
            # Threshold/group definition equivalent to sklearn micro AP.
            s, y = values.numpy().ravel(), target.numpy().ravel()
            order = np.argsort(s, kind="mergesort")[::-1]
            s, y = s[order], y[order]
            ends = np.r_[np.flatnonzero(np.diff(s)), len(s) - 1]
            tp = np.cumsum(y)[ends]
            precision = tp / (ends + 1)
            increments = np.diff(np.r_[0, tp])
            return float(np.sum(precision * increments) / int(y.sum()))
        def metrics(values):
            return clean_numbers({"source_auprc_micro": float(namespace["area_under_prc"](values.flatten(), target.flatten())), "source_f1_max": float(namespace["f1_max"](values, target)), "tie_grouped_micro_ap": tied_ap(values)})
        model = metrics(scores)
        old = item["original_parsed_metrics"]
        if not math.isclose(model["source_auprc_micro"], old["auprc@micro"], rel_tol=1e-7, abs_tol=1e-10) or not math.isclose(model["source_f1_max"], old["f1_max"], rel_tol=1e-7, abs_tol=1e-10) or not math.isclose(model["tie_grouped_micro_ap"], old["TIE_GROUPED_AP_DIAGNOSTIC"]["sklearn_micro_average_precision"], rel_tol=1e-7, abs_tol=1e-10):
            raise ValueError("Model metrics do not reproduce original parsed subset")
        matched = metrics(torch.zeros_like(scores))
        case_rows = [{"task_id": task, "case_id": row["case_id"], "sparse_scores": row["sparse_scores"], "positive_class_indices": refs[row["case_id"]]} for row in valid]
        jsonl_gz(dest / f"{task}_matched_subset.jsonl.gz", case_rows)
        result = {**item, "matched_subset_case_ids_sha256": digest([r["case_id"] for r in valid]), "matched_subset_evidence_sha256": sha(dest / f"{task}_matched_subset.jsonl.gz"), "model_parsed_subset": model, "matched_subset_all_zero_reference": matched, "same_case_count": len(valid), "same_class_count": len(lookup), "positive_pairs": int(target.sum()), "total_pairs": int(target.numel()), "positive_prevalence": float(target.sum()) / target.numel(), "full_test_primary_metrics": {"source_auprc_micro": None, "source_f1_max": None}, "full_test_primary_status": "undefined_under_local_all_vectors_complete_policy"}
        results.append(result)
    out = {"version": "DEEPFRI_FAILURE_ANALYSIS_2026_10_19", "updated_at_pacific": datetime.now(ZoneInfo("America/Los_Angeles")).isoformat(), "new_inference_calls": 0, "predictions_repaired": 0, "original_scores_overwritten": False, "classification_frozen_sha256": sha(frozen_path), "rules": RULES, "runtime": {"python": platform.python_version(), "torch": torch.__version__, "numpy": np.__version__, "device": "cpu", "dtype": "float32", "threads": 1}, "native_metric_source_sha256": SOURCE_SHA, "tasks": results, "tie_grouped_implementation": "Distinct-score threshold groups, micro precision times recall increments; reproduced archived sklearn AP on each unchanged model subset."}
    out = clean_numbers(out)
    write(DEST / "analysis.json", out)
    write(ROOT / "reports/DEEPFRI_FAILURE_ANALYSIS_2026-10-19.json", out)
    print(json.dumps({"stage": "completed", "tasks": [{"task_id": t["task_id"], "model": t["model_parsed_subset"], "matched_zero": t["matched_subset_all_zero_reference"]} for t in results]}))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("stage", choices=("classify", "metrics"))
    parser.add_argument("--output", type=Path, default=DEST)
    args = parser.parse_args()
    (classify_stage if args.stage == "classify" else metrics_stage)(args.output)
