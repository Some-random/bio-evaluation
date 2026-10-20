"""Freeze the separate complete P14 MF condition without inference or labels.

The historical input-only approval is inherited for its exact complete cohort.
Only full amino-acid sequences and the fixed public vocabulary enter prompts.
Twelve official validation inputs, selected by length before model calls, form
an unscored delivery gate. No annotation rows or historical model answers are
read by this preparation.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import re

from run_deepfri_catalog_20261020 import MODEL, REVISION, VARIANT, dense_prompt, generation_for


ROOT = Path(__file__).resolve().parents[1]
TASK = ROOT / ".local/catalog_execution_2026-10-20/tasks/P14"
RESTORED = ROOT / ".local/evaluation_revision_2026-10-18/scoring/null_equivalence_recovery_v1/prepared_v2/p14/project"
DATA = RESTORED / "data/catalog_deepfri_tasks/P14"
INPUT = DATA / "model_inputs.jsonl"
INPUT_SHA = "9d276def7c1590e4f20acfac066fa84b911492a1b295a60b56f5b1666b2b6bc5"
VOCAB = DATA / "class_vocabulary.json"
VOCAB_SHA = "889a08bd972c17299c85e0a81d06de4114f3baeab2df8882737b81254766379f"
PROVENANCE = DATA / "input_provenance.jsonl"
PROVENANCE_SHA = "e8f2a00f6faeb94afde6dc548598008823e91379479b99435d6d8b795d7b533c"
REVIEW = ROOT / "configs/local_deepfri_p14_review.json"
REVIEW_SHA = "2ef8b0b1bb3c88a9ef0ae56efbb1058ef35dc094497c4f907dbd19fc47faae8c"
REFERENCES = DATA / "scorer_references.jsonl"
REFERENCE_SHA = "9ea2a7a6f19ea21b37ad46fdc12fd5fe8e330c5d3578cb35fe2aeed19b5a4b0e"
METRIC = RESTORED / "sources/deepfri_contract_audit_2026-10-15/torchdrug__torchdrug__metrics__metric.py"
METRIC_SHA = "760f376d4125ab2cc9332c9e83b944d4464da51aea577d75266d9247aca81776"
GO_SOURCE = ROOT / ".local/catalog_execution_2026-10-20/tasks/P13/source"
VALID_IDS = GO_SOURCE / "nrPDB-GO_valid.txt"
VALID_IDS_SHA = "d72bf584d50ae1dd215fad031ccdada0399a32659ea753c2679756dba3fa1bf1"
FASTA = GO_SOURCE / "nrPDB-GO_sequences.fasta"
FASTA_SHA = "4cabd881a5dac1594726f8f5d0bf952978e732ec2599a60ab940a4314fe7d1be"
TEST_FASTA = GO_SOURCE / "nrPDB-GO_test_sequences.fasta"
TEST_FASTA_SHA = "1f48b7265fdc540df77f3bb3d4f0fec0e68d0b301d7487c569efbf8333bd607e"
TEST_IDS = GO_SOURCE / "nrPDB-GO_test.txt"
TEST_IDS_SHA = "753e6741bf8c9b178b0b15eb293daaa32c0036fb13ae3bca43352f66579a19ec"
CLASS_COUNT = 489


def sha_bytes(value):
    return hashlib.sha256(value).hexdigest()


def sha(path):
    return sha_bytes(Path(path).read_bytes())


def encode(value):
    return (json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2) + "\n").encode()


def encode_rows(rows):
    return b"".join((json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n").encode() for row in rows)


def immutable(path, data):
    path = Path(path)
    if path.exists():
        if path.read_bytes() != data:
            raise ValueError("Frozen preparation differs: " + str(path))
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("xb") as handle:
        handle.write(data)
    path.chmod(0o600)


def fasta_records(text):
    rows, key = {}, None
    for line in text.splitlines():
        if line.startswith(">"):
            key = line[1:].split()[0]
            if key in rows:
                raise ValueError("Duplicate FASTA identity")
            rows[key] = ""
        elif line:
            if key is None or not re.fullmatch(r"[A-Z]+", line):
                raise ValueError("Unexpected FASTA content")
            rows[key] += line
    if not rows or any(not value for value in rows.values()):
        raise ValueError("Missing FASTA sequences")
    return rows


def extracted_historical_sequence(row):
    if set(row) != {"task", "case_id", "variant", "split", "messages"} or row["task"] != "P14":
        raise ValueError("Unexpected historical model-input fields")
    messages = row["messages"]
    if len(messages) != 1 or messages[0]["role"] != "user" or set(messages[0]) != {"role", "content"}:
        raise ValueError("Unexpected historical prompt context")
    content = messages[0]["content"]
    marker = "\n\nComplete amino acid sequence:\n"
    tail = "\n\nFixed global class vocabulary (class ID followed by description):\n"
    if content.count(marker) != 1 or content.count(tail) != 1:
        raise ValueError("Historical sequence markers differ")
    sequence = content.split(marker, 1)[1].split(tail, 1)[0]
    if not re.fullmatch(r"[A-Z]+", sequence):
        raise ValueError("Complete source amino-acid string required")
    return sequence


def model_case(case_id, sequence, classes):
    return {"task_id": "P14", "case_id": case_id,
            "messages": [{"role": "user", "content": dense_prompt("P14", sequence, classes)}]}


def select_validation(validation_ids, sequences, test_ids, test_sequences, count=12):
    """Length quantiles including shortest/longest; never outcomes or labels."""
    if len(validation_ids) != len(set(validation_ids)):
        raise ValueError("Duplicate validation identity")
    test_ids, test_sequences = set(test_ids), set(test_sequences)
    if set(validation_ids) & test_ids:
        raise ValueError("Official validation/test identity overlap")
    eligible = [(len(sequences[key]), ordinal, key) for ordinal, key in enumerate(validation_ids)
                if sequences[key] not in test_sequences]
    eligible.sort()
    if len(eligible) < count or count < 2:
        raise ValueError("Insufficient disjoint official validation inputs")
    selected = [eligible[(i * (len(eligible) - 1)) // (count - 1)] for i in range(count)]
    return [{"case_id": key, "source_ordinal": ordinal, "sequence_length": size,
             "full_sequence_sha256": sha_bytes(sequences[key].encode())}
            for size, ordinal, key in selected], len(eligible)


def make_review(cases, split, inherited):
    return {"task_id": "P14", "input_review_only": True,
            "approved_case_ids": [row["case_id"] for row in cases], "held_cases": [],
            "source_split": split, "reviewed": True,
            "basis": "Natural protein molecular-function annotation from full sequence and one common public class vocabulary. No engineering, fitness optimization, operational instructions, targets or teacher explanations enter the request.",
            "scope": "Whole-task input-goal/schema approval, not manual function attribution to each sequence.",
            "inherited_exact_full_test_review": inherited,
            "selection_based_on_model_outputs": False, "reference_labels_read": False}


def make_config(folder, name, cases):
    is_test = name == "full_test"
    inp, review = folder / f"{name}_inputs.jsonl", folder / f"{name}_review.json"
    config = {"schema_version": 1, "task_id": "P14", "class_count": CLASS_COUNT,
              "run_id": f"qwen38_27b_p14_{name}_dense3dp_nonthinking16k_2026-10-20_v1",
              "variant": VARIANT, "model": MODEL, "model_revision": REVISION,
              "split": "official_test" if is_test else "official_validation",
              "planned": len(cases), "generation": generation_for(CLASS_COUNT),
              "input_file": str(inp), "input_sha256": sha(inp),
              "review_file": str(review), "review_sha256": sha(review),
              "vocabulary_file": str(VOCAB), "vocabulary_sha256": VOCAB_SHA,
              "files_sha256": {str(Path(__file__).resolve()): sha(__file__)},
              "delivery_only": not is_test, "biological_correctness_assessed": False,
              "native_scoring": "Exact pinned TorchDrug micro AUPRC and Fmax; float32 scores/int64 targets; no ontology propagation, calibration, threshold tuning or target-derived ordering.",
              "invalid_output_policy": "No fabricated vectors, selective retries or missing-row replacement. Incomplete full cohort has undefined full primary metrics, plus explicitly scoped diagnostics.",
              "reference_visibility": "No per-case labels or reference explanations in solver inputs; references opened only after output seal by offline scorer.",
              "historical_run_policy": "Separate whole reviewed 3416-case condition; all old requests/outputs/metrics immutable.",
              "comparison_limit": "Prompted zero-shot raw-full-FASTA annotation adaptation, not trained-head/native PDB crop reproduction. Dense fixed-order 3dp serialization and nonthinking replace historical sparse reasoning output; no biological performance claim follows from delivery checks.",
              "endpoint": None}
    if is_test:
        config.update({"development_config_sha256": sha(folder / "validation_delivery_config.json"),
                       "metric_source_file": str(METRIC), "metric_source_sha256": METRIC_SHA,
                       "scorer_reference_file": str(REFERENCES), "scorer_reference_sha256": REFERENCE_SHA})
    return config


def prepare(folder=TASK):
    pins = {INPUT: INPUT_SHA, VOCAB: VOCAB_SHA, PROVENANCE: PROVENANCE_SHA,
            REVIEW: REVIEW_SHA, VALID_IDS: VALID_IDS_SHA, FASTA: FASTA_SHA,
            TEST_FASTA: TEST_FASTA_SHA, TEST_IDS: TEST_IDS_SHA, METRIC: METRIC_SHA}
    for path, expected in pins.items():
        if sha(path) != expected:
            raise ValueError("Pinned source differs: " + str(path))
    # The reference file is not opened, hashed or parsed by preparation.
    if not REFERENCES.is_file():
        raise ValueError("Frozen scorer-reference file unavailable")
    vocab = json.loads(VOCAB.read_text())
    classes = vocab["classes"]
    if (vocab["branch"] != "MF" or len(classes) != CLASS_COUNT
            or [row["index"] for row in classes] != list(range(CLASS_COUNT))):
        raise ValueError("Complete source global MF vocabulary changed")
    originals = [json.loads(line) for line in INPUT.read_text().splitlines()]
    provenance = [json.loads(line) for line in PROVENANCE.read_text().splitlines()]
    inherited = json.loads(REVIEW.read_text())
    test_ids = TEST_IDS.read_text().splitlines()
    test_fasta = fasta_records(TEST_FASTA.read_text())
    ids = [row["case_id"] for row in originals]
    if len(originals) != 3416 or ids != inherited["approved_case_ids"] or ids != test_ids or inherited["held_cases"]:
        raise ValueError("Exact reviewed full-test cohort/order differs")
    cases, sequence_hashes = [], []
    for row, evidence in zip(originals, provenance, strict=True):
        sequence = extracted_historical_sequence(row)
        if (row["case_id"] != evidence["case_id"] or sequence != test_fasta[row["case_id"]]
                or len(sequence) != evidence["sequence_length"]
                or sha_bytes(sequence.encode()) != evidence["full_sequence_sha256"]):
            raise ValueError("Complete source sequence differs")
        sequence_hashes.append(sha_bytes(sequence.encode()))
        cases.append(model_case(row["case_id"], sequence, classes))
    seqs = fasta_records(FASTA.read_text())
    valid_ids = VALID_IDS.read_text().splitlines()
    selection, eligible = select_validation(valid_ids, seqs, ids, test_fasta.values())
    development = [model_case(row["case_id"], seqs[row["case_id"]], classes) for row in selection]
    for name, rows in [("validation_delivery", development), ("full_test", cases)]:
        immutable(folder / f"{name}_inputs.jsonl", encode_rows(rows))
        immutable(folder / f"{name}_review.json", encode(make_review(rows, name, REVIEW_SHA if name == "full_test" else None)))
        immutable(folder / f"{name}_config.json", encode(make_config(folder, name, rows)))
    source = {"task_id": "P14", "source_files_sha256": {str(path): value for path, value in pins.items()},
              "source_class_order": "All 489 MF classes in exact released 2019.06.18 annotation-header order",
              "source_vocabulary_sha256": VOCAB_SHA, "source_vocabulary_uses_test_positive_selection": False,
              "full_test_planned": len(cases), "full_sequences_match_all_original_reviewed_inputs": True,
              "full_test_sequence_order_sha256": sha_bytes(encode(sequence_hashes)),
              "validation_source_count": len(valid_ids), "validation_sequence_disjoint_eligible_count": eligible,
              "validation_selection": "12 length-quantile inputs including shortest/longest; source order breaks ties; sequence-identical test inputs excluded; fixed before calls",
              "validation_cases": selection, "reference_values_inspected": False,
              "reference_file_read_during_preparation": False, "new_inference_calls": 0,
              "native_metric_source_sha256": METRIC_SHA,
              "maximum_prompt_bytes": max(len(row["messages"][0]["content"].encode()) for row in cases + development),
              "maximum_compact_vector_bytes": len('{"scores":[') + CLASS_COUNT * len("0.999") + (CLASS_COUNT - 1) + len("]}"),
              "output_budget_tokens": 16384,
              "budget_note": "Fixed 489 bounded decimal values require at most 2946 ASCII bytes; actual tokenizer/context checks are still enforced by runner before dispatch."}
    immutable(folder / "source_provenance.json", encode(source))
    return {"task_id": "P14", "full_test_planned": len(cases), "validation_delivery_planned": len(development),
            "class_count": CLASS_COUNT, "new_inference_calls": 0,
            "full_config_sha256": sha(folder / "full_test_config.json"),
            "development_config_sha256": sha(folder / "validation_delivery_config.json"),
            "source_provenance_sha256": sha(folder / "source_provenance.json")}


if __name__ == "__main__":
    print(json.dumps(prepare(), sort_keys=True))
