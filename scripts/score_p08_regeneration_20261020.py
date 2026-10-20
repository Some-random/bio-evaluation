"""Score a sealed new P08 run once, preserving native global Spearman.

No inference, output repair, sign change, score calibration or retry occurs.
All generation files must be hash-locked before scorer-only references open.
"""
from __future__ import annotations

import argparse
from collections import Counter
from datetime import datetime
import hashlib
import json
import math
from pathlib import Path
import re
from zoneinfo import ZoneInfo

from prepare_p08_regeneration_20261020 import (ARCHIVE_SHA, INPUT_SHA, REGEX,
    RESTORED, TASK, VARIANT, encode, immutable, sha)


REFERENCE = RESTORED / "data/catalog_extended/P08/scorer_references.jsonl"
REFERENCE_SHA = "bb6bc3a78b14ad195ebb2df56f968963d08006834130e1755152aa2824853427"


def ranks(values):
    """Average ranks for ties, exactly the conventional native Spearman ranks."""
    ordered = sorted(range(len(values)), key=values.__getitem__)
    result = [None] * len(values)
    i = 0
    while i < len(ordered):
        j = i + 1
        while j < len(ordered) and values[ordered[j]] == values[ordered[i]]:
            j += 1
        mean_rank = (i + 1 + j) / 2
        for k in range(i, j):
            result[ordered[k]] = mean_rank
        i = j
    return result


def spearman(targets, predictions):
    if len(targets) != len(predictions) or len(targets) < 2:
        return None
    if any(not math.isfinite(x) for x in targets + predictions):
        raise ValueError("Finite unchanged native values required")
    a, b = ranks(targets), ranks(predictions)
    a_mean, b_mean = sum(a) / len(a), sum(b) / len(b)
    ac = [x - a_mean for x in a]
    bc = [x - b_mean for x in b]
    denominator = math.sqrt(sum(x*x for x in ac) * sum(x*x for x in bc))
    if denominator == 0:
        return None
    return sum(x*y for x, y in zip(ac, bc)) / denominator


def metric_policy(targets, predictions):
    if len(targets) != len(predictions) or not targets:
        raise ValueError("Matching nonempty full planned arrays required")
    pairs = [(t, p) for t, p in zip(targets, predictions) if p is not None]
    value = spearman([t for t, _ in pairs], [p for _, p in pairs])
    complete = len(pairs) == len(targets)
    return {"planned": len(targets), "valid_predictions": len(pairs),
            "invalid_or_missing": len(targets) - len(pairs),
            "spearman": value if complete else None,
            "spearman_parsed_only": value if not complete else None,
            "undefined_constant_or_insufficient": value is None,
            "all_case_policy": "Every original planned case retained. No fabricated prediction fills invalid answers; incomplete parsed-only correlation is separate.",
            "aggregation": "one global average-tie Spearman; no shard-correlation averaging",
            "target_transform": "none", "prediction_transform": "none; no sign flip"}


def verify_locked_files(run_dir, files):
    for name, expected in files.items():
        path = (run_dir / name).resolve()
        if not path.is_relative_to(run_dir.resolve()) or sha(path.read_bytes()) != expected:
            raise ValueError("Sealed generation file differs: " + name)


def verify_seal(run_dir, config_path):
    config_raw = config_path.read_bytes()
    config = json.loads(config_raw)
    if (config["task_id"] != "P08" or config["protocol_variant"] != VARIANT
            or config["planned"] != 12851 or config["delivery_only"]):
        raise ValueError("Require the separately frozen full P08 condition")
    manifest = json.loads((run_dir / "run_manifest.json").read_text())
    if manifest["configuration"] != config or manifest["config_sha256"] != sha(config_raw):
        raise ValueError("Run configuration mismatch")
    completion = json.loads((run_dir / "completion.json").read_text())
    lock_path = run_dir / "prediction_lock.json"
    if completion["prediction_lock_sha256"] != sha(lock_path.read_bytes()):
        raise ValueError("Generation completion does not seal prediction lock")
    if (completion["phase"] != "benchmark_generation" or completion["planned"] != 12851
            or completion["terminal"] != 12851):
        raise ValueError("Require all planned terminal outcomes; no unsealed lower-bound scoring")
    lock = json.loads(lock_path.read_text())
    if lock["config_sha256"] != sha(config_raw) or lock["reference_labels_opened"] is not False:
        raise ValueError("Require pre-reference exact configuration/output lock")
    verify_locked_files(run_dir, lock["files_sha256"])
    input_path = Path(config["input_file"])
    if sha(input_path.read_bytes()) != config["input_sha256"]:
        raise ValueError("Frozen input changed")
    cases = [json.loads(line) for line in input_path.read_text().splitlines()]
    if [c["case_id"] for c in cases] != [f"stability:test:{i}" for i in range(12851)]:
        raise ValueError("Complete original source-order cohort required")
    for path, expected in config["files_sha256"].items():
        if sha(Path(path).read_bytes()) != expected:
            raise ValueError("Frozen preparation dependency changed")
    parser_path = Path(config["native_numeric_parser_file"])
    if sha(parser_path.read_bytes()) != config["native_numeric_parser_sha256"]:
        raise ValueError("Native parser snapshot changed")
    namespace = {}
    exec(parser_path.read_bytes(), namespace)
    parse = namespace["parse_number"]
    predictions, outcomes = [], []
    for case in cases:
        key = sha(case["case_id"].encode())
        name = "outcomes/" + key + ".json"
        path = run_dir / name
        if name not in lock["files_sha256"]:
            raise ValueError("Outcome absent from prediction seal")
        outcome = json.loads(path.read_text())
        if outcome["case_id"] != case["case_id"]:
            raise ValueError("Outcome identity mismatch")
        prediction = outcome.get("prediction") if outcome.get("delivery_passed") else None
        if prediction is not None:
            if not outcome["response_saved"] or not outcome["native_parse_pass"] or type(prediction) not in (int, float):
                raise ValueError("Accepted prediction lacks delivered/native-parse evidence")
            response_name = "responses/" + key + ".json"
            if response_name not in lock["files_sha256"]:
                raise ValueError("Accepted prediction lacks sealed response")
            body = json.loads((run_dir / response_name).read_text())
            choice = body["choices"][0]
            final = choice["message"].get("content")
            if (len(body["choices"]) != 1 or choice["finish_reason"] != "stop"
                    or not isinstance(final, str) or re.fullmatch(REGEX, final) is None
                    or parse(final) != prediction or not math.isfinite(prediction)
                    or choice["message"].get("reasoning", choice["message"].get("reasoning_content"))
                    or choice["message"].get("refusal") or choice["message"].get("tool_calls")):
                raise ValueError("Accepted value differs from unchanged native final parser")
        predictions.append(prediction)
        outcomes.append(outcome)
    return config, lock, completion, cases, predictions, outcomes


def score(run_dir, config_path, output_path):
    if output_path.exists():
        raise ValueError("Score path exists; no implicit score overwrite")
    config, lock, completion, cases, predictions, outcomes = verify_seal(run_dir, config_path)
    # This is the first reference access: no outcome can be replaced after seal.
    reference_bytes = REFERENCE.read_bytes()
    if sha(reference_bytes) != REFERENCE_SHA:
        raise ValueError("Scorer-only reference pin mismatch")
    refs = [json.loads(line) for line in reference_bytes.decode().splitlines()]
    if [r["case_id"] for r in refs] != [c["case_id"] for c in cases] or any(r["task"] != "P08" for r in refs):
        raise ValueError("Scorer reference cohort mismatch")
    targets = [r["target"] for r in refs]
    if any(type(t) not in (float, int) or not math.isfinite(t) for t in targets):
        raise ValueError("Invalid native target")
    report = {"task_id": "P08", "run_id": config["run_id"], "protocol_variant": VARIANT,
              "scored_at_pacific": datetime.now(ZoneInfo("America/Los_Angeles")).isoformat(),
              "model": config["model"], "model_revision": config["model_revision"],
              "configuration_sha256": sha(config_path.read_bytes()),
              "prediction_lock_sha256": sha((run_dir / "prediction_lock.json").read_bytes()),
              "reference_sha256": REFERENCE_SHA, "source_archive_sha256": ARCHIVE_SHA,
              "historical_input_sha256": INPUT_SHA, "metrics": metric_policy(targets, predictions),
              "statuses": dict(Counter(o["status"] for o in outcomes)),
              "transport_or_response_errors": sum(o["status"] in {"http_error", "transport_error", "response_error"} for o in outcomes),
              "truncations": sum(bool(o.get("truncated")) for o in outcomes),
              "empty_finals": sum(bool(o.get("empty_final")) for o in outcomes),
              "historical_results_unchanged": True, "new_model_calls_by_scorer": 0,
              "interpretation": "Biological outcome prediction on the12851-row released PyTorch stability test. Native experimental scale and Spearman preserved; generation delivery adaptation and training regime differ from paper specialist heads. Mechanism/rationale and contamination remain unassessed."}
    immutable(output_path, encode(report))
    print(json.dumps(report))
    return report


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--run", type=Path, required=True)
    parser.add_argument("--config", type=Path, default=TASK / "full_test_config.json")
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    score(args.run, args.config, args.output)
