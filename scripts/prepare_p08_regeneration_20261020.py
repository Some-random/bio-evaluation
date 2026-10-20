"""Freeze the separate full P08 scalar-delivery experiment without model calls.

Only source inputs enter requests. The full test is not sampled or selected by
historical outcomes. Twelve validation inputs provide a delivery-only gate.
"""
from __future__ import annotations

import argparse
import ast
from datetime import datetime
import hashlib
import json
from pathlib import Path
import pickle
import re
import sys
import tarfile
from zoneinfo import ZoneInfo


ROOT = Path(__file__).resolve().parents[1]
TASK = ROOT / ".local/catalog_execution_2026-10-20/tasks/P08"
RESTORED = ROOT / ".local/remaining_evaluations/extended"
INPUT = RESTORED / "data/catalog_extended/P08/model_inputs.jsonl"
REVIEW = ROOT / "configs/local_extended_p08_review.json"
ARCHIVE = RESTORED / "sources/catalog_extended__P08.tar.gz"
INPUT_SHA = "068d4d951f3e6e220514cabdcef151afcf82108d635ddbe82a0ce9b18ceb0f4d"
REVIEW_SHA = "5bfa787092fe43eb47b43103c7b966a9e4ebce56793b47557861d3b3477a7b43"
ARCHIVE_SHA = "0580bc854e13701431dbbaf942756b8611598e3422599104bc7b0a151b6ec38f"
PARSER_SOURCE = ROOT / "scripts/score_local_catalog_extended.py"
OBJECTIVE = ("Predict the continuous protein-folding stability score of this sequence "
             "on the original TAPE/Rocklin experimental scale (the stability_score target), "
             "which measures resistance to unfolding under the source assay. "
             "Return only one finite numerical value.")
UNIT = "native TAPE stability_score scale; no conversion to melting temperature or energy"
VARIANT = "QWEN_FULL_SEQUENCE_TAPE_STABILITY_PYTORCH_NONTHINKING_STRUCTURED_SCALAR_20261020_V1"
REGEX = r"[+-]?[0-9]{1,12}(\.[0-9]{1,12})?([eE][+-]?[0-9]{1,2})?"
GENERATION = {"max_tokens": 256, "temperature": 1.0, "top_p": 0.95,
              "top_k": 20, "seed": 42, "n": 1,
              "chat_template_kwargs": {"enable_thinking": False},
              "structured_outputs": {"regex": REGEX}}


def sha(value):
    return hashlib.sha256(value).hexdigest()


def encode(value):
    return (json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2) + "\n").encode()


def rows_bytes(rows):
    return b"".join((json.dumps(row, sort_keys=True, ensure_ascii=False) + "\n").encode() for row in rows)


def immutable(path, payload):
    """A repeated preparation may verify existing bytes but never replace them."""
    if path.exists():
        if path.read_bytes() != payload:
            raise ValueError("Frozen preparation differs: " + str(path))
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("xb") as handle:
        handle.write(payload)
    path.chmod(0o600)


def sequence_prompt(sequence):
    if not isinstance(sequence, str) or not re.fullmatch("[A-Z]+", sequence):
        raise ValueError("Complete unmodified source sequence required")
    return OBJECTIVE + "\n\nComplete protein sequence:\n" + sequence


def test_case(source, index):
    """Validate an already-reviewed input and discard every non-model field."""
    if source["task"] != "P08" or source["case_id"] != f"stability:test:{index}":
        raise ValueError("Task/source order changed")
    if source["source_index"] != index or source["split"] != "official_released_test":
        raise ValueError("Source index/split changed")
    fields = source["fields"]
    if set(fields) != {"objective", "sequence"} or fields["objective"] != OBJECTIVE:
        raise ValueError("Unexpected model fields or objective")
    prompt = sequence_prompt(fields["sequence"])
    if source["system"] != "" or source["prompt"] != prompt or source["prompt_sha256"] != sha(prompt.encode()):
        raise ValueError("Reviewed complete prompt changed")
    return {"task_id": "P08", "case_id": source["case_id"],
            "messages": [{"role": "user", "content": prompt}]}


def pinned_parser():
    text = PARSER_SOURCE.read_text()
    tree = ast.parse(text)
    node = next(node for node in tree.body if isinstance(node, ast.FunctionDef) and node.name == "parse_number")
    function = ast.get_source_segment(text, node)
    return ("\"\"\"Exact native scalar parser snapshot; no dataset access.\"\"\"\nimport math\nimport re\n\n" + function + "\n").encode(), sha(function.encode())


def validation_cases(task_dir):
    """Read only primary values from twelve pinned official validation rows.

    Native pickle rows contain scorer values but those fields are never accessed
    or copied. No test LMDB or training LMDB is opened here.
    """
    packages = ROOT / ".local/catalog_resume_2026-10-19/development/packages"
    if packages.is_dir():
        sys.path.insert(0, str(packages))
    import lmdb
    member = "stability/stability_valid.lmdb/data.mdb"
    with tarfile.open(ARCHIVE) as archive:
        data = archive.extractfile(member).read()
    lmdb_path = task_dir / "source_validation_lmdb/data.mdb"
    immutable(lmdb_path, data)
    env = lmdb.open(str(lmdb_path.parent), readonly=True, lock=False, readahead=False, meminit=False)
    try:
        with env.begin() as txn:
            count = pickle.loads(txn.get(b"num_examples"))
            rows, metadata = [], []
            for index in range(12):
                primary = pickle.loads(txn.get(str(index).encode()))["primary"]
                prompt = sequence_prompt(primary)
                rows.append({"task_id": "P08", "case_id": f"stability:valid:{index}",
                             "messages": [{"role": "user", "content": prompt}]})
                metadata.append({"case_id": rows[-1]["case_id"], "source_index": index,
                                 "sequence_sha256": sha(primary.encode()), "sequence_length": len(primary)})
    finally:
        env.close()
    return rows, {"source_split": "official_released_validation", "source_rows": count,
                  "selected_source_indices": list(range(12)), "selection": "first twelve source-order validation inputs; fixed before new model calls",
                  "reference_fields_accessed": False, "source_pickle_rows_deserialized": True,
                  "source_lmdb_sha256": sha(data), "cases": metadata}


def make_config(task_dir, name, cases, review_path, parser_path):
    is_test = name == "full_test"
    input_path = task_dir / (name + "_inputs.jsonl")
    config = {
        "schema_version": 1, "task_id": "P08",
        "run_id": "qwen38_27b_p08_" + name + "_nonthinking_structured_scalar_2026-10-20_v1",
        "protocol_variant": VARIANT + ("" if is_test else "_VALIDATION_DELIVERY_ONLY"),
        "model": "Qwen/Qwen3.8-27B", "model_revision": "1d4bf0f2ff6012fd82039f2fa52739d0dd7c60c0",
        "checkpoint_precision": "original pinned BF16; no quantization",
        "input_file": str(input_path), "input_sha256": sha(input_path.read_bytes()),
        "planned": len(cases), "split": "official_test" if is_test else "official_validation",
        "source_split": "official_released_test" if is_test else "official_released_validation_delivery_only",
        "generation": GENERATION, "review_file": str(review_path), "review_sha256": sha(review_path.read_bytes()),
        "native_numeric_parser_file": str(parser_path), "native_numeric_parser_sha256": sha(parser_path.read_bytes()),
        "native_numeric_parser_function": "parse_number", "files_sha256": {},
        "native_objective": OBJECTIVE, "native_units": UNIT,
        "reference_visibility": "No reference or target values in solver files or messages; offline scorer only.",
        "native_scoring": "One global Spearman on the unchanged native stability_score target; no sign flip, calibration or target transform.",
        "invalid_output_policy": "Abstention, empty, nonfinite, malformed and truncated finals remain invalid; no invented values or selective retries.",
        "historical_run_policy": "Independent full ordered cohort. Historical responses, negative parsed-only score and all original metrics remain immutable.",
        "comparison_limit": "Released PyTorch test12851 differs from historical2019 paper12839. Nonthinking/structured scalar delivery is a named text-model adaptation, not a trained-head replication.",
        "delivery_only": not is_test,
        "benchmark_scoring_authorized": is_test,
        "endpoint": None,
    }
    if is_test:
        config["development_config_sha256"] = sha((task_dir / "validation_delivery_config.json").read_bytes())
    for path in [Path(__file__), ROOT / "tests/test_prepare_p08_regeneration_20261020.py", parser_path]:
        config["files_sha256"][str(path)] = sha(path.read_bytes())
    return config


def prepare(task_dir=TASK):
    for path, expected in [(INPUT, INPUT_SHA), (REVIEW, REVIEW_SHA), (ARCHIVE, ARCHIVE_SHA)]:
        if sha(path.read_bytes()) != expected:
            raise ValueError("Pinned source changed: " + str(path))
    source_rows = [json.loads(line) for line in INPUT.read_text().splitlines()]
    if len(source_rows) != 12851:
        raise ValueError("Need complete12851-case released test")
    cases = [test_case(source, i) for i, source in enumerate(source_rows)]
    reviewed = json.loads(REVIEW.read_text())
    if reviewed["approved_case_ids"] != [case["case_id"] for case in cases] or reviewed["held_cases"]:
        raise ValueError("Exact reviewed case scope differs")
    parser, function_sha = pinned_parser()
    parser_path = task_dir / "native_numeric_parser.py"
    immutable(parser_path, parser)
    dev, dev_provenance = validation_cases(task_dir)
    for name, cohort in [("validation_delivery", dev), ("full_test", cases)]:
        immutable(task_dir / (name + "_inputs.jsonl"), rows_bytes(cohort))
        review_path = task_dir / (name + "_review.json")
        immutable(review_path, encode({"task_id": "P08", "approved_case_ids": [c["case_id"] for c in cohort], "held_cases": [],
            "basis": "Existing full-input benign folding-stability scope, unmodified complete sequences and native objective; no outcome-based case selection.",
            "original_review_file": str(REVIEW), "original_review_sha256": REVIEW_SHA,
            "new_test_labels_inspected": False, "model_outputs_used_for_selection": False}))
        immutable(task_dir / (name + "_config.json"), encode(make_config(task_dir, name, cohort, review_path, parser_path)))
    immutable(task_dir / "source_provenance.json", encode({
        "task_id": "P08", "source_input_sha256": INPUT_SHA, "source_review_sha256": REVIEW_SHA,
        "archive_sha256": ARCHIVE_SHA, "source_release_url": "https://s3.amazonaws.com/songlabdata/proteindata/data_pytorch/stability.tar.gz",
        "native_parser_source_file": str(PARSER_SOURCE), "native_parser_source_file_sha256": sha(PARSER_SOURCE.read_bytes()),
        "native_parser_function_sha256": function_sha, "validation": dev_provenance,
        "full_test": {"planned": len(cases), "sequence_length_min": min(len(r["fields"]["sequence"]) for r in source_rows),
                      "sequence_length_max": max(len(r["fields"]["sequence"]) for r in source_rows),
                      "ordered_ids_sha256": sha(encode([c["case_id"] for c in cases])),
                      "complete_source_sequences_preserved": True, "test_reference_values_inspected": False},
        "scorer_only": {"reference_file": str(RESTORED / "data/catalog_extended/P08/scorer_references.jsonl"),
                        "reference_sha256": "bb6bc3a78b14ad195ebb2df56f968963d08006834130e1755152aa2824853427",
                        "reference_values_loaded_by_preparation": False},
        "new_inference_calls": 0,
    }))
    status = {"task_id": "P08", "updated_at_pacific": datetime.now(ZoneInfo("America/Los_Angeles")).isoformat(),
              "stage": "prepared_waiting_shared_endpoint_synthetic_and_validation_delivery_checks",
              "planned": 12851, "responses_saved": None, "attempted_confirmed": None,
              "dispatch_evidence": "No task runtime exists; preparation alone does not establish dispatch or zero attempted requests outside this preparation.",
              "new_inference_calls_by_preparation": 0, "validation_delivery_planned": 12,
              "native_scoring_status": "not_started_for_new_condition", "historical_results_unchanged": True,
              "remaining": ["Root shared-endpoint grant", "Synthetic scalar transport/schema checks", "Twelve official-validation delivery checks with no labels or scoring", "Fresh full-cohort generation and sealed offline global Spearman"]}
    (task_dir / "status.json").write_bytes(encode(status))
    print(json.dumps({"task_id": "P08", "prepared": len(cases), "validation_delivery_planned": len(dev), "new_inference_calls": 0, "task_directory": str(task_dir)}))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--task-directory", type=Path, default=TASK)
    args = parser.parse_args()
    prepare(args.task_directory)
