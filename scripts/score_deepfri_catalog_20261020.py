#!/usr/bin/env python3
"""Score one sealed new dense-confidence condition using pinned native formulas.

CPU only. Does not initialize a model, call an endpoint, train, repair outputs,
select cases, or open reference labels before verifying the complete output lock.
Run in the centrally frozen Torch runtime used by the project.
"""
from __future__ import annotations

import argparse
import ast
from collections import Counter
import json
from pathlib import Path
import platform

from run_deepfri_catalog_20261020 import (
    ROOT, TASKS, atomic, canonical, load_contract, parse_delivery, payload,
    resolve, sha, stamp,
)

METRIC_SOURCE_SHA256 = "760f376d4125ab2cc9332c9e83b944d4464da51aea577d75266d9247aca81776"
METRIC_FUNCTIONS = {"area_under_prc", "f1_max"}
METRIC_POLICY = {
    "native_source_revision": "DeepGraphLearning/torchdrug@6066fbd82360abb5f270cba1eca560af01b8cc90",
    "native_functions": ["area_under_prc", "f1_max"],
    "dtype": "torch.float32 scores; torch.int64 binary targets",
    "device": "cpu", "num_threads": 1, "num_interop_threads": 1,
    "case_order": "exact reviewed complete released test95 source order",
    "class_order": "complete released annotation-header order",
    "tie_order": "native torch.argsort defaults in recorded runtime; no gold-derived rearrangement",
    "score_propagation": "none; source target annotation closure retained",
    "all_case_primary_gate": "all planned outcomes must contain valid vectors; otherwise full primary metrics are null",
    "invalid_replacement_or_case_drop": False,
    "confidence_serialization": "model-supplied fixed-order dense numeric array, at most three decimal places",
}


def native_functions(source_path):
    import torch
    if sha(source_path) != METRIC_SOURCE_SHA256:
        raise ValueError("Pinned TorchDrug metric source differs")
    tree = ast.parse(Path(source_path).read_text())
    nodes = [node for node in tree.body if isinstance(node, ast.FunctionDef) and node.name in METRIC_FUNCTIONS]
    if {node.name for node in nodes} != METRIC_FUNCTIONS:
        raise ValueError("Native metric function namespace differs")
    for node in nodes:
        node.decorator_list = []
    namespace = {"torch": torch}
    exec(compile(ast.Module(body=nodes, type_ignores=[]), str(source_path), "exec"), namespace)
    return namespace


def matrix_metrics(vectors, positives, class_count, functions):
    if len(vectors) != len(positives) or not vectors:
        raise ValueError("Prediction/reference cohort mismatch")
    valid = [i for i, vector in enumerate(vectors) if vector is not None]
    diagnostics = {"planned": len(vectors), "valid_vectors": len(valid),
                   "invalid_or_missing_vectors": len(vectors)-len(valid),
                   "all_zero_vectors": sum(not any(v) for v in vectors if v is not None),
                   "score_based_case_filtering": False}
    if len(valid) != len(vectors):
        return {"auprc@micro": None, "f1_max": None}, diagnostics
    import torch
    scores = torch.tensor(vectors, dtype=torch.float32, device="cpu")
    targets = torch.zeros((len(vectors), class_count), dtype=torch.int64, device="cpu")
    if scores.shape != targets.shape:
        raise ValueError("Dense matrix shape differs from fixed vocabulary")
    for index, ids in enumerate(positives):
        targets[index, ids] = 1
    result = {"auprc@micro": float(functions["area_under_prc"](scores.flatten(), targets.flatten())),
              "f1_max": float(functions["f1_max"](scores, targets))}
    diagnostics["unique_float32_confidences"] = int(scores.unique().numel())
    return result, diagnostics


def verify_locked_generation(config_path, folder):
    config, cases, _ = load_contract(config_path)
    if config["split"] != "official_test":
        raise ValueError("Development panels must not be biologically scored")
    folder = Path(folder)
    completion = json.loads((folder/"completion.json").read_text())
    lock_path = folder/"prediction_lock.json"
    if sha(lock_path) != completion["prediction_lock_sha256"]:
        raise ValueError("Sealed prediction lock differs")
    lock = json.loads(lock_path.read_text())
    if completion["config_sha256"] != sha(config_path) or lock["config_sha256"] != sha(config_path):
        raise ValueError("Sealed configuration identity differs")
    if lock.get("reference_labels_opened") is not False or completion.get("biological_correctness_assessed") is not False:
        raise ValueError("Generation phase has unexpected reference/scoring access")
    for name, expected in lock["files_sha256"].items():
        path = folder/name
        if not path.resolve().is_relative_to(folder.resolve()) or sha(path) != expected:
            raise ValueError("Changed or foreign locked generation file: " + name)
    manifest = json.loads((folder/"run_manifest.json").read_text())
    if manifest["configuration"] != config or manifest["config_sha256"] != sha(config_path):
        raise ValueError("Manifest configuration differs")
    if manifest["runner_sha256"] != sha(ROOT/"scripts/run_deepfri_catalog_20261020.py"):
        raise ValueError("Runner differs from sealed manifest")
    expected_ids = {case["case_id"] for case in cases}
    if completion["planned"] != len(cases) or completion["terminal"] != len(cases):
        raise ValueError("Generation cohort has not reached terminal closure")
    import hashlib
    vectors, per_case, observed = [], [], set()
    for case in cases:
        key = hashlib.sha256(case["case_id"].encode()).hexdigest()+".json"
        outcome_name = "outcomes/"+key
        if outcome_name not in lock["files_sha256"]:
            raise ValueError("Missing terminal outcome in prediction lock")
        outcome = json.loads((folder/outcome_name).read_text())
        if outcome["case_id"] != case["case_id"]:
            raise ValueError("Outcome case identity differs")
        observed.add(case["case_id"])
        request_name, response_name = "requests/"+key, "responses/"+key
        vector = None
        if request_name in lock["files_sha256"]:
            request = json.loads((folder/request_name).read_text())
            if request != payload(case, config):
                raise ValueError("Saved request differs from frozen isolated payload")
            if outcome.get("request_sha256") not in (None, lock["files_sha256"][request_name]):
                raise ValueError("Outcome request hash differs")
        if response_name in lock["files_sha256"]:
            if request_name not in lock["files_sha256"]:
                raise ValueError("Response has no corresponding request")
            body = json.loads((folder/response_name).read_text())
            if outcome.get("response_sha256") != lock["files_sha256"][response_name]:
                raise ValueError("Outcome response hash differs")
            parsed = parse_delivery(body, config["class_count"])
            if any(outcome.get(k) != parsed[k] for k in ("prediction", "delivery_passed", "finish_reason", "empty_final", "truncated", "refusal")):
                raise ValueError("Saved output interpretation differs from strict frozen parser")
            if parsed["delivery_passed"]:
                vector = parsed["prediction"]
        elif outcome.get("delivery_passed"):
            raise ValueError("Outcome claims prediction without locked response")
        vectors.append(vector)
        per_case.append({"case_id": case["case_id"], "valid_confidence_vector": vector is not None,
                         "status": outcome["status"], "finish_reason": outcome.get("finish_reason")})
    if observed != expected_ids:
        raise ValueError("Case cohort differs")
    for category in ("requests", "responses", "outcomes", "errors"):
        actual = {str(p.relative_to(folder)) for p in (folder/category).iterdir() if p.is_file()}
        locked = {n for n in lock["files_sha256"] if n.startswith(category+"/")}
        if actual != locked:
            raise ValueError("Unsealed generation file in "+category)
    return config, cases, vectors, per_case, lock


def score(config_path, folder, output):
    config_path, folder, output = Path(config_path), Path(folder), Path(output)
    if output.exists():
        raise FileExistsError("Preserve existing score; no repeated scoring attempt")
    config, cases, vectors, per_case, lock = verify_locked_generation(config_path, folder)
    # All payloads, missing slots and output interpretations verified before the
    # first scorer-reference file read below. Hash is frozen in task config.
    reference_path = resolve(config["scorer_reference_file"])
    if sha(reference_path) != config["scorer_reference_sha256"]:
        raise ValueError("Scorer references differ from frozen source")
    vocabulary = json.loads(resolve(config["vocabulary_file"]).read_text())
    class_ids = [row["class_id"] for row in vocabulary["classes"]]
    references = {}
    for line in reference_path.read_text().splitlines():
        row = json.loads(line)
        indices, ids = row["positive_class_indices"], row["positive_class_ids"]
        if row.get("scorer_only") is not True or row.get("task_id") != config["task_id"] or row["case_id"] in references:
            raise ValueError("Invalid scorer-only reference identity")
        if len(indices) != len(ids) or len(set(indices)) != len(indices) or any(type(i) is not int or not 0 <= i < len(class_ids) or class_ids[i] != t for i,t in zip(indices,ids)):
            raise ValueError("Reference indices differ from frozen global class order")
        references[row["case_id"]] = indices
    if set(references) != {case["case_id"] for case in cases}:
        raise ValueError("Reference cohort differs from all planned cases")
    import torch
    torch.set_num_threads(1)
    torch.set_num_interop_threads(1)
    runtime = {"python": platform.python_version(), "torch": torch.__version__,
               "device": "cpu", "dtype": "float32", "num_threads": torch.get_num_threads(),
               "num_interop_threads": torch.get_num_interop_threads()}
    if runtime != config.get("expected_scoring_runtime"):
        raise ValueError("CPU scoring runtime differs from the pre-inference frozen contract")
    source = resolve(config["metric_source_file"])
    if config["metric_source_sha256"] != METRIC_SOURCE_SHA256:
        raise ValueError("Unexpected native metric source hash")
    functions = native_functions(source)
    metrics, diagnostics = matrix_metrics(vectors, [references[c["case_id"]] for c in cases], len(class_ids), functions)
    result = {"task_id": config["task_id"], "run_id": config["run_id"], "at_pacific": stamp(),
              "model": config["model"], "model_revision": config["model_revision"],
              "protocol_variant": config["variant"], "reporting_protocol_kind": "adapted",
              "planned": len(cases), "parsed": diagnostics["valid_vectors"],
              "invalid_or_missing": diagnostics["invalid_or_missing_vectors"],
              "metrics": metrics, "full_planned_primary_metrics_valid": all(v is not None for v in vectors),
              "native_metric_policy": METRIC_POLICY, "runtime": runtime, "confidence_diagnostics": diagnostics,
              "config_sha256": sha(config_path), "prediction_lock_sha256": sha(folder/"prediction_lock.json"),
              "scorer_sha256": sha(__file__), "reference_sha256": sha(reference_path),
              "metric_source_sha256": sha(source), "predictions_locked_before_reference_read": True,
              "case_scope": config.get("case_scope"), "paper_comparison": config.get("paper_comparison"),
              "explanation_support_assessed": False, "public_pretraining_exposure": "unknown"}
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("xb") as handle:
        handle.write(canonical(result))
    with output.with_name(output.stem+".per_case.json").open("xb") as handle:
        handle.write(canonical(per_case))
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", type=Path)
    parser.add_argument("--run-folder", type=Path)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--synthetic-check-only", type=Path, metavar="PINNED_METRIC_SOURCE")
    args = parser.parse_args()
    if args.synthetic_check_only:
        import math
        import torch
        torch.set_num_threads(1)
        torch.set_num_interop_threads(1)
        functions = native_functions(args.synthetic_check_only)
        examples = [([[.9,.1],[.2,.8]],[[0],[1]]),
                    ([[.9,.8,.1],[.2,.7,.6]],[[0,1],[1]])]
        for vectors, positives in examples:
            result,_ = matrix_metrics(vectors,positives,len(vectors[0]),functions)
            if any(abs(value-1)>1e-6 for value in result.values()):
                raise ValueError("Pinned metric failed artificial perfect-ranking fixture")
        tied,_ = matrix_metrics([[0.,0.],[0.,0.]],[[0],[1]],2,functions)
        if any(not math.isfinite(value) for value in tied.values()):
            raise ValueError("Pinned metric rejected valid tied all-zero fixture")
        invalid,counts = matrix_metrics([[.1,.5],None],[[0],[1]],2,functions)
        if invalid != {"auprc@micro":None,"f1_max":None} or counts["planned"]!=2:
            raise ValueError("Invalid case passed the all-case primary gate")
        print(json.dumps({"synthetic_checks_passed":4,"at_pacific":stamp(),
                          "native_source_sha256":sha(args.synthetic_check_only),
                          "torch":torch.__version__,"python":platform.python_version(),
                          "device":"cpu","threads":1,"real_cases_scored":0,
                          "reference_labels_opened":False,"model_calls":0}))
        return
    if not all((args.config,args.run_folder,args.output)):
        parser.error("--config, --run-folder and --output are required for sealed test scoring")
    print(json.dumps(score(args.config, args.run_folder, args.output)))


if __name__ == "__main__":
    main()
