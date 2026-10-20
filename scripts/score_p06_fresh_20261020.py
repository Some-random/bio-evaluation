"""Score locked fresh P06 predictions offline; labels never enter the runner."""
from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import json
import math
from pathlib import Path

from run_scalar_catalog_20261020 import ROOT, canonical, create, load_contract, parse_delivery, payload, resolve, sha, stamp


def score(run_dir):
    run_dir = Path(run_dir).resolve()
    if (run_dir / "scores.json").exists():
        raise ValueError("Fresh scores already sealed; no implicit rescoring")
    manifest = json.loads((run_dir / "run_manifest.json").read_text())
    config = manifest["configuration"]
    if config["task_id"] != "P06" or config["split"] != "official_test":
        raise ValueError("Only the new P06 test condition may be scored")
    done = json.loads((run_dir / "completion.json").read_text())
    lock_path = run_dir / "prediction_lock.json"
    if sha(lock_path) != done["prediction_lock_sha256"]:
        raise ValueError("Prediction lock changed")
    lock = json.loads(lock_path.read_text())
    if not (manifest["config_sha256"] == done["config_sha256"] == lock["config_sha256"]):
        raise ValueError("Generation/config identity mismatch")
    if hashlib.sha256(canonical(config)).hexdigest() != manifest["config_sha256"]:
        raise ValueError("Manifest is not the frozen canonical task config")
    for relative, expected in lock["files_sha256"].items():
        if sha(run_dir / relative) != expected:
            raise ValueError("Frozen output changed: " + relative)
    for field, expected_key in [("input_file", "input_sha256"), ("review_file", "review_sha256"),
                                ("native_numeric_parser_file", "native_numeric_parser_sha256")]:
        if sha(resolve(config[field])) != config[expected_key]:
            raise ValueError("Frozen task file changed: " + field)
    cases = [json.loads(line) for line in resolve(config["input_file"]).read_text().splitlines() if line]
    if len(cases) != config["planned"] or len(cases) != done["planned"]:
        raise ValueError("Full denominator mismatch")
    # Reuse the exact parser but do not import a source loader or scorer labels.
    import importlib.util
    spec = importlib.util.spec_from_file_location("p06_frozen_parser", resolve(config["native_numeric_parser_file"]))
    module = importlib.util.module_from_spec(spec); spec.loader.exec_module(module)
    parser = getattr(module, config["native_numeric_parser_function"])
    predictions, records, counts = [], [], Counter()
    for case in cases:
        key = hashlib.sha256(case["case_id"].encode()).hexdigest()
        req_name = f"requests/{key}.json"; response_name = f"responses/{key}.json"; outcome_name = f"outcomes/{key}.json"
        value = None
        status = "not_dispatched"
        if req_name in lock["files_sha256"]:
            counts["attempted"] += 1
            if (run_dir / req_name).read_bytes() != canonical(payload(case)):
                raise ValueError("Saved request differs from isolated frozen input")
            status = "attempted_without_valid_final"
        if outcome_name in lock["files_sha256"]:
            outcome = json.loads((run_dir/outcome_name).read_text())
            if outcome["case_id"] != case["case_id"]:
                raise ValueError("Outcome case identity mismatch")
            counts["terminal"] += 1
            status = outcome["status"]
        if response_name in lock["files_sha256"]:
            counts["responses_saved"] += 1
            checked = parse_delivery(json.loads((run_dir/response_name).read_text()), parser)
            for flag in ["empty_final", "truncated", "refusal", "reasoning_present"]:
                counts[flag] += checked[flag]
            if checked["delivery_passed"]:
                value = checked["prediction"]
                counts["valid_predictions"] += 1
        predictions.append(value)
        records.append({"case_id": case["case_id"], "status": status, "prediction": value})
    # Only after the complete raw-output lock and reparse are verified do labels open.
    ref_path = resolve(config["scorer_reference_file"])
    if sha(ref_path) != config["scorer_reference_sha256"]:
        raise ValueError("Reference hash mismatch")
    references = [json.loads(line) for line in ref_path.read_text().splitlines() if line]
    if [row["case_id"] for row in references] != [row["case_id"] for row in cases]:
        raise ValueError("Scorer references differ from the complete ordered cohort")
    targets = [float(row["target_source_string"]) for row in references]
    if not all(math.isfinite(value) for value in targets):
        raise ValueError("Nonfinite reference")
    pairs = [(target, prediction) for target, prediction in zip(targets, predictions) if prediction is not None]
    constant = len(pairs) < 2 or len({target for target, _ in pairs}) < 2 or len({prediction for _, prediction in pairs}) < 2
    correlation = None
    if not constant:
        from scipy.stats import spearmanr
        result = float(spearmanr([target for target, _ in pairs], [prediction for _, prediction in pairs]).statistic)
        correlation = result if math.isfinite(result) else None
    all_valid = len(pairs) == len(cases)
    scores = {"task_id": "P06", "run_id": config["run_id"], "protocol_variant": config["protocol_variant"],
              "scored_at_pacific": stamp(), "config_sha256": manifest["config_sha256"],
              "prediction_lock_sha256": sha(lock_path), "reference_sha256": sha(ref_path),
              "planned": len(cases), "counts": dict(counts), "missing_or_invalid": len(cases)-len(pairs),
              "native_metric": "Spearman correlation", "spearman": correlation if all_valid else None,
              "spearman_parsed_only": correlation if not all_valid else None,
              "undefined_constant_or_insufficient": constant, "all_case_primary_available": all_valid and correlation is not None,
              "historical_results_unchanged": True, "new_inference_calls_by_scorer": 0,
              "interpretation": "Experimental human-cell thermal outcome prediction from complete sequences under a nonthinking constrained-decimal zero-shot adaptation. No specialist fitted head, biological mechanism or matched-training reproduction claim.",
              "failure_policy": "No invented numeric fill values, label-guided extraction or selective retry. Full primary requires every planned final to be finite and normally stopped."}
    create(run_dir/"scores.json", scores)
    print(json.dumps(scores), flush=True)
    return scores


if __name__ == "__main__":
    args = argparse.ArgumentParser(description=__doc__)
    args.add_argument("--run-dir", required=True, type=Path)
    score(args.parse_args().run_dir)
