"""One offline P19 score after a complete immutable prediction lock.

Uses unchanged upstream PFArena T1 metric functions on exactly the frozen subset.
Reference rows are opened only after all output bytes and native coverage pass.
Native missing-query random imputation is never enabled.
"""
from __future__ import annotations

import argparse
import ast
from collections import Counter
from datetime import datetime
import hashlib
import json
from pathlib import Path
import sys
import tempfile
import types
from zoneinfo import ZoneInfo

from p19_generation_contract_20261020 import audit_generation

ROOT = Path(__file__).resolve().parents[1]


def stamp():
    return datetime.now(ZoneInfo("America/Los_Angeles")).isoformat()


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def resolve(path):
    path = Path(path)
    return path if path.is_absolute() else ROOT / path


def load_native(path, router_path):
    """Only remove the registry import; all native scorer function ASTs are intact."""
    registry = ast.parse(router_path.read_text())
    inputs = [ast.literal_eval(node.value) for node in registry.body
              if isinstance(node, ast.Assign) and any(isinstance(target, ast.Name) and target.id == "DATASET_INPUTS"
                                                     for target in node.targets)]
    if len(inputs) != 1:
        raise ValueError("Pinned native registry assignment differs")
    tree = ast.parse(path.read_text())
    tree.body = [node for node in tree.body if not (isinstance(node, ast.ImportFrom) and node.module == "router")]
    name = "_p19_pinned_native_scorer"
    module = types.ModuleType(name)
    module.__file__ = str(path)
    module.DATASET_INPUTS = inputs[0]
    sys.modules[name] = module
    exec(compile(tree, str(path), "exec"), module.__dict__)
    return module


def load_native_parser(path):
    names = {"extract_balanced_json", "parse_generation_mode_mutants"}
    tree = ast.parse(path.read_text())
    selected = ast.Module(body=[node for node in tree.body if isinstance(node, ast.FunctionDef) and node.name in names], type_ignores=[])
    import re
    namespace = {"re": re, "json": json}
    exec(compile(selected, str(path), "exec"), namespace)
    return namespace["parse_generation_mode_mutants"]


def verify_prediction_lock(run, config_path, expected_count):
    completion = json.loads((run / "completion.json").read_text())
    if completion["task_id"] != "P19" or completion["config_sha256"] != sha(config_path):
        raise ValueError("Completion belongs to another frozen condition")
    if completion["planned"] != expected_count or completion["terminal"] != expected_count:
        raise ValueError("A partial/unsealed cohort is not a complete score")
    lock_path = run / "prediction_lock.json"
    if sha(lock_path) != completion["prediction_lock_sha256"]:
        raise ValueError("Prediction lock changed")
    lock = json.loads(lock_path.read_text())
    if lock["config_sha256"] != sha(config_path) or lock.get("reference_labels_opened") is not False:
        raise ValueError("Prediction lock scope/reference isolation differs")
    for relative, expected in lock["files_sha256"].items():
        path = (run / relative).resolve()
        if not path.is_relative_to(run.resolve()) or sha(path) != expected:
            raise ValueError("Prediction lock member changed: " + relative)
    return completion, sha(lock_path), set(lock["files_sha256"])


def score(run, config_path, reference_path, output):
    config = json.loads(config_path.read_text())
    if config.get("task_id") != "P19" or config.get("split") != "reviewed_benchmark_subset":
        raise ValueError("Refuse scoring a development panel or another task")
    for path, expected in config["files_sha256"].items():
        if sha(resolve(path)) != expected:
            raise ValueError("Frozen scorer/runner dependency changed")
    for key, expected in [("input_file", config["input_sha256"]),
                          ("delivery_context_file", config["delivery_context_sha256"]),
                          ("review_file", config["review_sha256"])]:
        if sha(resolve(config[key])) != expected:
            raise ValueError("Frozen input/review changed")
    cases = [json.loads(line) for line in resolve(config["input_file"]).read_text().splitlines() if line]
    if len(cases) != config["planned"]:
        raise ValueError("Cohort length differs")
    completion, lock_sha, locked_files = verify_prediction_lock(run, config_path, len(cases))
    if sha(reference_path) != config["scorer_only_manifest_sha256"]:
        raise ValueError("Frozen scorer manifest changed")
    manifest = json.loads(reference_path.read_text())
    if manifest["task_id"] != "P19" or manifest["missing_query_random_fallback_enabled"] is not False:
        raise ValueError("Unexpected scorer/imputation protocol")
    for field in ["native_scorer", "native_router", "native_parser"]:
        if sha(resolve(manifest[field + "_file"])) != manifest[field + "_sha256"]:
            raise ValueError("Pinned upstream code changed: " + field)
    context_rows = json.loads(resolve(config["delivery_context_file"]).read_text())["cases"]
    contexts = {row["case_id"]: row["wildtype_sequence"] for row in context_rows}
    reference_rows = manifest["cases"]
    if [row["case_id"] for row in reference_rows] != [row["case_id"] for row in cases]:
        raise ValueError("References differ from ordered frozen cases")
    parser = load_native_parser(resolve(manifest["native_parser_file"]))
    parsed, audits = {}, []
    for case in cases:
        case_id = case["case_id"]
        key = hashlib.sha256(case_id.encode()).hexdigest()
        outcome_path = run / "outcomes" / (key + ".json")
        if str(outcome_path.relative_to(run)) not in locked_files:
            raise ValueError("Terminal record is outside sealed lock")
        if not outcome_path.is_file() or json.loads(outcome_path.read_text()).get("case_id") != case_id:
            raise ValueError("Missing/mismatched sealed terminal record")
        response_path = run / "responses" / (key + ".json")
        final = None
        if response_path.is_file():
            if str(response_path.relative_to(run)) not in locked_files:
                raise ValueError("Response was added after prediction sealing")
            body = json.loads(response_path.read_text())
            if len(body.get("choices", [])) == 1:
                final = body["choices"][0].get("message", {}).get("content")
        values = parser(final) if isinstance(final, str) else None
        parsed[case_id] = values
        audits.append({"case_id": case_id, **audit_generation(contexts[case_id], final).to_dict()})
    short = [case_id for case_id, values in parsed.items() if values is None or len(values) < 40]
    result = {"scored_at_pacific": stamp(), "task_id": "P19", "condition": config["condition"],
              "planned_assays": len(cases), "native_panel_assays": 123,
              "full_native_benchmark_complete": False, "prediction_lock_sha256": lock_sha,
              "configuration_sha256": sha(config_path), "scorer_manifest_sha256": sha(reference_path),
              "biological_measurement_inference": "Scores compare proposals to pre-existing assay measurements; no experimental validation of generated proposals.",
              "delivery_audits": audits,
              "strict_delivery_passed": sum(row["delivery_passed"] for row in audits),
              "transport_or_response_errors": completion["transport_or_response_errors"],
              "empty_finals": completion["empty_finals"], "truncations": completion["truncations"],
              "missing_query_random_fallback_enabled": False}
    if short:
        result.update(native_scoring_status="undefined_native_strict_coverage_failure",
                      undefined_case_ids=short, native_metrics=None, reference_rows_opened=False)
    else:
        native = load_native(resolve(manifest["native_scorer_file"]), resolve(manifest["native_router_file"]))
        with tempfile.TemporaryDirectory(prefix="p19-frozen-reference-view-") as directory:
            truth_dir = Path(directory)
            for row in reference_rows:
                source = resolve(row["target_path"])
                if sha(source) != row["sha256"]:
                    raise ValueError("Protected target asset changed")
                (truth_dir / (row["native_truth_id"] + ".csv")).symlink_to(source)
            setting = "T1_single_mutant_generation"
            truth = native.load_full_ground_truth(truth_dir, nested_groups=False, item_column="mutant", setting=setting)
            predictions = {
                row["native_truth_id"]: [native.PredictionRow(row["native_truth_id"], mutant, float(index), index - 1, "sealed_raw_native_parser")
                                         for index, mutant in enumerate(parsed[row["case_id"]], 1)]
                for row in reference_rows
            }
            native._validate_predictions(truth, predictions, top_k=40, strict=True, setting=setting)
            per_assay = [native.evaluate_one_assay(truth=assay, pred_rows=predictions[name], top_k=40, setting=setting)
                         for name, assay in sorted(truth.items())]
            summary = native.summarize_full_results(per_assay, truth=truth, predictions=predictions,
                                                    setting=setting, ground_truth_dir=Path("frozen_34_assay_reference_view"),
                                                    predictions_path=run, top_k=40, strict=True)
        result.update(native_scoring_status="completed_native_scored_reviewed_subset",
                      native_metrics=summary["metrics"], native_summary=summary,
                      per_assay=per_assay, reference_rows_opened=True)
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("x") as handle:
        json.dump(result, handle, sort_keys=True, indent=2, allow_nan=False)
        handle.write("\n")
    print(json.dumps({"task_id": "P19", "native_scoring_status": result["native_scoring_status"],
                      "native_metrics": result["native_metrics"], "output_sha256": sha(output)}))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--run", type=Path, required=True)
    parser.add_argument("--config", type=Path, required=True)
    parser.add_argument("--references", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    score(args.run, args.config, args.references, args.output)
