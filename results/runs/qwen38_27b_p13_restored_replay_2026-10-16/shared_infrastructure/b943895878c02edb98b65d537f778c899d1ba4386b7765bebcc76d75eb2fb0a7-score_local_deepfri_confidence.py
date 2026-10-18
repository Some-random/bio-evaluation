#!/usr/bin/env python3
"""Offline, output-locked native-formula scoring of frozen sparse confidences.

Use .venv-vllm/bin/python. This does not load model weights, use GPUs, repair
predictions, call providers, train heads, or dispatch requests.
"""
import argparse
import ast
from collections import Counter
import hashlib
import json
from pathlib import Path
import platform
import subprocess
import tempfile

from prepare_local_deepfri_proposals import parse_sparse_confidence, OUTPUT_CONTRACT
from score_local_genomics import digest, file_digest, write_json, find_config, expected_payload, read_locked_json

ROOT = Path(__file__).resolve().parents[1]
TASKS = {"P12": 538, "P13": 1943, "P14": 489, "P15": 320}
SOURCE = "sources/deepfri_contract_audit_2026-10-15/torchdrug__torchdrug__metrics__metric.py"
SOURCE_SHA256 = "760f376d4125ab2cc9332c9e83b944d4464da51aea577d75266d9247aca81776"
TIE_HELPER = "scripts/score_local_deepfri_tie_grouped.py"
PROTOCOL = {
    "version": "deepfri_sparse_confidence_v1",
    "output": OUTPUT_CONTRACT,
    "native_metric_names": ["auprc@micro", "f1_max"],
    "native_source": SOURCE,
    "native_source_revision": "6066fbd82360abb5f270cba1eca560af01b8cc90",
    "native_functions": ["area_under_prc", "f1_max"],
    "native_dtype_device_threads": "torch.float32 scores; torch.int64 binary targets; CPU; one intraop and interop thread",
    "case_order": "exact ordered frozen input/review IDs",
    "class_order": "exact complete released annotation-header order",
    "tie_rule": "source torch.argsort default unstable rank ordering under frozen runtime; no gold-derived reordering; author historical GPU/device tie equivalence unknown",
    "ontology_score_propagation": "none",
    "full_primary_metric_gate": "all planned cases valid; otherwise both native primary values null",
    "supplemental_metric": "TIE_GROUPED_AP_DIAGNOSTIC.sklearn_micro_average_precision; retain separately, never choose better score",
    "all_zero_reference": "OFFLINE_ALL_ZERO_REFERENCE: predeclared all-zero matrix in identical full case/class order; never model predictions or invalid-output replacements",
    "parsed_only": "PARSED_ONLY_DIAGNOSTIC namespace, exact valid/planned counts, never a full-test primary metric",
}


def runtime():
    import torch
    import numpy
    torch.set_num_threads(1)
    if torch.get_num_interop_threads() != 1:
        torch.set_num_interop_threads(1)
    helper = subprocess.run([str(ROOT / ".venv/bin/python"), str(ROOT / TIE_HELPER), "--describe-runtime"], check=True, capture_output=True, text=True)
    return {"python": platform.python_version(), "torch": torch.__version__, "numpy": numpy.__version__, "tie_grouped_sklearn_runtime": json.loads(helper.stdout), "device": "cpu", "dtype": "float32", "num_threads": torch.get_num_threads(), "num_interop_threads": torch.get_num_interop_threads()}


def native_functions(root, expected_source_hash):
    import torch
    path = Path(root) / SOURCE
    if expected_source_hash != SOURCE_SHA256 or file_digest(path) != SOURCE_SHA256:
        raise ValueError("Native metric source changed")
    tree = ast.parse(path.read_text())
    functions = [node for node in tree.body if isinstance(node, ast.FunctionDef) and node.name in PROTOCOL["native_functions"]]
    if {node.name for node in functions} != set(PROTOCOL["native_functions"]):
        raise ValueError("Native metric function namespace changed")
    for node in functions:
        node.decorator_list = []
    namespace = {"torch": torch}
    exec(compile(ast.Module(body=functions, type_ignores=[]), str(path), "exec"), namespace)
    return namespace


def metrics_for(scores, targets, functions):
    import numpy
    # Use the existing isolated sklearn environment, without changing any
    # package in the active vLLM serving environment. No pickle is exchanged.
    with tempfile.TemporaryDirectory(prefix="deepfri-tie-ap-") as temporary:
        path = Path(temporary) / "matrix.npz"
        numpy.savez(path, scores=scores.numpy(), targets=targets.numpy())
        output = subprocess.run([str(ROOT / ".venv/bin/python"), str(ROOT / TIE_HELPER)],
                                input=json.dumps({"matrix_path": str(path), "sha256": file_digest(path)}),
                                check=True, capture_output=True, text=True)
        tie_grouped = json.loads(output.stdout)["sklearn_micro_average_precision"]
    return {
        "auprc@micro": float(functions["area_under_prc"](scores.flatten(), targets.flatten())),
        "f1_max": float(functions["f1_max"](scores, targets)),
        "TIE_GROUPED_AP_DIAGNOSTIC": {"sklearn_micro_average_precision": tie_grouped},
    }


def matrix_metrics(vectors, positive_indices, class_ids, functions):
    import torch
    targets = torch.zeros((len(vectors), len(class_ids)), dtype=torch.int64, device="cpu")
    for i, positives in enumerate(positive_indices):
        targets[i, positives] = 1
    ids = {term: i for i, term in enumerate(class_ids)}
    scores = torch.zeros(targets.shape, dtype=torch.float32, device="cpu")
    valid = [i for i, vector in enumerate(vectors) if vector is not None]
    for i in valid:
        for term, probability in vectors[i].items():
            scores[i, ids[term]] = probability
    complete = len(valid) == len(vectors)
    # Invalid model rows are never passed to a full-set model metric. The zero
    # matrix below is a separately frozen offline reference, independent of it.
    model = metrics_for(scores, targets, functions) if complete else {"auprc@micro": None, "f1_max": None, "TIE_GROUPED_AP_DIAGNOSTIC": {"sklearn_micro_average_precision": None}}
    if valid and not complete:
        model["PARSED_ONLY_DIAGNOSTIC"] = {**metrics_for(scores[valid], targets[valid], functions), "valid_cases": len(valid), "planned_cases": len(vectors)}
    model["OFFLINE_ALL_ZERO_REFERENCE"] = {**metrics_for(torch.zeros_like(scores), targets, functions), "case_count": len(vectors), "is_model_prediction": False}
    diagnostics = {"valid_vectors": len(valid), "planned_vectors": len(vectors), "explicit_empty_vectors": sum(vector == {} for vector in vectors if vector is not None), "all_zero_vectors": sum(not any(vector.values()) for vector in vectors if vector is not None), "binary_only_vectors": sum(all(value in (0, 1) for value in vector.values()) for vector in vectors if vector is not None), "all_zero_confidence_reference_is_model_prediction": False, "model_score_pair_count": len(valid) * len(class_ids), "model_zero_score_pair_count": int((scores[valid] == 0).sum()) if valid else 0, "model_unique_float32_confidences": int(scores[valid].unique().numel()) if valid else 0, "score_based_case_filtering": False}
    return model, diagnostics


def lock_outputs(root, folder, cases, config_path, settings):
    files = {"run_manifest.json": file_digest(folder / "run_manifest.json"), "frozen_config": file_digest(config_path), "scoring_protocol": digest(PROTOCOL)}
    names = set()
    for case in cases:
        name = digest([case["task"], case["variant"], case["case_id"]]) + ".json"
        names.add(name)
        for category in ("requests", "responses"):
            path = folder / category / name
            files[category + "/" + name] = file_digest(path) if path.exists() else None
    for category in ("requests", "responses"):
        if {path.name for path in (folder / category).glob("*.json")} - names:
            raise ValueError("Alternate output/request archive is not allowed")
    for key in ("input_file", "review_file", "class_vocabulary_file", "scorer_reference_file"):
        files["frozen_source/" + key] = file_digest(root / settings[key])
    record = {"files_sha256": files, "contract_sha256": digest(files), "policy": "All raw requests/responses and absent slots locked before labels; no repair, selection, retry or missing-vector imputation."}
    path = folder / "scoring_output_lock.json"
    if path.exists() and json.loads(path.read_text()) != record:
        raise ValueError("Pre-label output lock changed")
    if not path.exists():
        write_json(path, record)
    return record


def score(folder, root=ROOT, config_path=None):
    root, folder = Path(root).resolve(), Path(folder).resolve()
    manifest = json.loads((folder / "run_manifest.json").read_text())
    settings = manifest["configuration"]
    task = settings["approved_task_ids"][0]
    if settings["approved_task_ids"] != [task] or task not in TASKS or not settings.get("model_revision"):
        raise ValueError("Require one exact supported task/model revision")
    config_path = find_config(root, manifest, config_path)
    frozen = settings["frozen_files_sha256"]
    required = {"scripts/score_local_deepfri_confidence.py", "scripts/score_local_genomics.py", "scripts/prepare_local_deepfri_proposals.py", TIE_HELPER, SOURCE, settings["input_file"], settings["review_file"], settings["class_vocabulary_file"], settings["scorer_reference_file"], settings["scoring_runtime_file"]}
    if not required <= set(frozen) or any(file_digest(root / name) != value for name, value in frozen.items()):
        raise ValueError("A required pre-inference frozen source/scorer/input/config hash changed")
    if frozen["scripts/score_local_deepfri_confidence.py"] != file_digest(__file__) or manifest.get("runner_sha256") != frozen.get(settings["runner"]):
        raise ValueError("Running scorer/runner differs from frozen manifest")
    if runtime() != json.loads((root / settings["scoring_runtime_file"]).read_text()):
        raise ValueError("Scoring CPU/runtime/thread contract changed")
    for snapshot in (manifest.get("server", {}), manifest.get("serving_configuration", {})):
        if snapshot and (snapshot.get("model") != settings["model"] or snapshot.get("revision") != settings["model_revision"]):
            raise ValueError("Serving snapshot differs from pinned model")
    cases = [json.loads(line) for line in (root / settings["input_file"]).read_text().splitlines()]
    if digest(cases) != manifest["case_contract_sha256"] or manifest["planned_cases"] != len(cases) or settings["planned"] != len(cases):
        raise ValueError("Exact planned input contract changed")
    review = json.loads((root / settings["review_file"]).read_text())
    if review.get("input_review_only") is not True or [row["case_id"] for row in cases] != review["approved_case_ids"] or len({row["case_id"] for row in cases}) != len(cases):
        raise ValueError("Exact ordered input review changed")
    lock = lock_outputs(root, folder, cases, config_path, settings)
    vocabulary = read_locked_json(root / settings["class_vocabulary_file"], lock["files_sha256"]["frozen_source/class_vocabulary_file"])
    class_ids = [row["class_id"] for row in vocabulary["classes"]]
    if len(class_ids) != TASKS[task] or len(set(class_ids)) != len(class_ids) or [row["index"] for row in vocabulary["classes"]] != list(range(len(class_ids))):
        raise ValueError("Global source class order changed")
    states, finishes, errors = Counter(), Counter(), Counter()
    vectors, per_case = [], []
    for case in cases:
        name = digest([case["task"], case["variant"], case["case_id"]]) + ".json"
        request = read_locked_json(folder / "requests" / name, lock["files_sha256"]["requests/" + name])
        response = read_locked_json(folder / "responses" / name, lock["files_sha256"]["responses/" + name])
        if request is not None and (request.get("request_sha256") != digest(expected_payload(case, settings)) or digest(request["payload"]) != request["request_sha256"] or any(request.get(k) != case[k] for k in ("task", "case_id", "variant", "split"))):
            raise ValueError("Request differs from frozen payload/identity")
        if response is not None and (request is None or any(response.get(k) != v for k, v in {"task": task, "case_id": case["case_id"], "variant": case["variant"], "split": case["split"], "model": settings["model"], "model_revision": settings["model_revision"], "request_sha256": request["request_sha256"]}.items())):
            raise ValueError("Response model/input/request provenance mismatch")
        status = response.get("status") if response else "interrupted_unknown_completion" if request else "not_dispatched"
        states[status] += 1
        vector, error = None, None
        if status == "completed":
            if response.get("http_status") != 200 or response.get("response", {}).get("model") != settings["model"]:
                raise ValueError("Completed response server identity mismatch")
            if len(response.get("response", {}).get("choices", [])) != 1:
                raise ValueError("Require exactly the frozen single completion")
            choice = response["response"]["choices"][0]
            final = choice["message"].get("content")
            if final != response.get("text") or choice.get("finish_reason") != response.get("finish_reason"):
                raise ValueError("Saved final/finish fields conflict")
            finishes[str(response.get("finish_reason"))] += 1
            try:
                vector = parse_sparse_confidence(final, class_ids, response.get("finish_reason"))
            except (ValueError, TypeError, OverflowError) as exc:
                error = str(exc)
                errors[error] += 1
        vectors.append(vector)
        per_case.append({"task_id": task, "case_id": case["case_id"], "status": status, "valid_confidence_vector": vector is not None, "parse_error": error, "sparse_scores": vector})
    # Reference labels are opened only after all predictions/missing slots and
    # payload/model identities have been frozen and parsed without any gold.
    reference_path = root / settings["scorer_reference_file"]
    raw = reference_path.read_bytes()
    if hashlib.sha256(raw).hexdigest() != lock["files_sha256"]["frozen_source/scorer_reference_file"] or hashlib.sha256(raw).hexdigest() != settings["scorer_reference_sha256"]:
        raise ValueError("Locked scorer references changed")
    refs = {}
    for row in map(json.loads, raw.decode().splitlines()):
        if row.get("task_id") != task or row.get("scorer_only") is not True or row["case_id"] in refs or len(set(row["positive_class_indices"])) != len(row["positive_class_indices"]) or any(isinstance(index, bool) or not isinstance(index, int) or not 0 <= index < len(class_ids) or class_ids[index] != term for index, term in zip(row["positive_class_indices"], row["positive_class_ids"])) or len(row["positive_class_indices"]) != len(row["positive_class_ids"]):
            raise ValueError("Reference identity/global vocabulary mismatch")
        refs[row["case_id"]] = row["positive_class_indices"]
    positives = [refs[case["case_id"]] for case in cases]
    functions = native_functions(root, frozen[SOURCE])
    metrics, diagnostics = matrix_metrics(vectors, positives, class_ids, functions)
    valid = diagnostics["valid_vectors"]
    missing = len(cases) - states["completed"]
    summary = {"task_id": task, "run_id": settings["run_id"], "model": settings["model"], "model_revision": settings["model_revision"], "protocol_variant": settings["variant"], "reporting_protocol_kind": "adapted", "checkpoint_precision": settings.get("checkpoint_precision"), "planned": len(cases), "finished": sum(count for state, count in states.items() if state not in {"not_dispatched", "not_dispatched_after_error", "interrupted_unknown_completion"}), "completed": states["completed"], "parsed": valid, "invalid_outputs": states["completed"] - valid, "missing_outputs": missing, "statuses": dict(states), "finish_reasons": dict(finishes), "parse_error_counts": dict(errors), "metrics": metrics, "primary_metric_names": ["auprc@micro", "f1_max"], "full_planned_primary_metrics_valid": valid == len(cases), "primary_metric_status": "source_formula_on_protocol_qualified_adaptation" if valid == len(cases) else "undefined_invalid_or_missing_planned_vectors", "metric_protocol": PROTOCOL, "confidence_diagnostics": diagnostics, "scoring_runtime": runtime(), "scorer_sha256": file_digest(__file__), "scoring_protocol_sha256": digest(PROTOCOL), "configuration_sha256": manifest["configuration_sha256"], "scoring_output_lock_sha256": lock["contract_sha256"], "predictions_locked_before_reference_read": True, "input_modalities": settings["input_modalities"], "case_scope": settings["case_scope"], "class_vocabulary_size": len(class_ids), "held_before_inference": len(review.get("held_cases", [])), "explanation_support_score": None, "comparison_to_paper": settings["paper_comparison"], "interpretation": "Annotation-confidence prediction only; no calibrated probability, biological absence, reference-supported explanation or mechanism validation. Public pretraining exposure unknown. All-zero reference is an offline diagnostic, never model predictions. Native tied-rank equivalence to author runtime is unverified."}
    write_json(folder / "scores.json", summary)
    write_json(folder / "per_case_scores.json", per_case)
    return summary


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--run")
    parser.add_argument("--config", type=Path)
    parser.add_argument("--describe-protocol", action="store_true")
    args = parser.parse_args()
    if args.describe_protocol:
        print(json.dumps({"protocol": PROTOCOL, "protocol_sha256": digest(PROTOCOL), "scorer_sha256": file_digest(__file__), "runtime": runtime()}))
    elif args.run:
        print(json.dumps(score(ROOT / "results/runs" / args.run, config_path=args.config)))
    else:
        parser.error("--run or --describe-protocol is required")
