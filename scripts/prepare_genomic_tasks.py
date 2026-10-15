#!/usr/bin/env python3
"""Offline preparation of pinned public BioReason human-genomic inputs.

No inference, training, provider client, configuration change or response read.
Run with the workspace .venv, which already contains pyarrow. Source parquet
files are verified against the publisher-digest download manifest before use.
"""
from __future__ import annotations

import argparse
from collections import Counter
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re


SOURCE_DIR = Path("sources/genomic_contract_audit_2026-10-15")
CODE_REVISION = "684ff7c09eb1d65e70925c114a7a05a1fcc0403f"
VARIANT = "NATIVE_LLM_INTERFACE_FULL_RELEASE_WINDOWS_PREPARED"
TASKS = {
    "N01": {"dataset": "wanglab/kegg", "revision": "9f0ef941a362f0e308e11861ed82c36338e23586",
            "files": ["kegg__data__test-00000-of-00001.parquet", "kegg__data__val-00000-of-00001.parquet"],
            "splits": ["test", "val"], "expected_counts": [146, 144], "variant_column": "variant_sequence",
            "native_metrics": ["accuracy", "macro_f1", "macro_precision", "macro_recall"],
            "split_evidence": "Pinned official eval_kegg_dna_vllm.py:40-43 concatenates test then val (146+144=290). This resolves released evaluator count/order, without proving archived author predictions or exact paper-run identity."},
    "N02": {"dataset": "wanglab/variant_effect_coding", "revision": "7684ab820d728fb5362328757079a1390a3f43bb",
            "files": ["variant_effect_coding__test-00000-of-00001.parquet"], "splits": ["test"],
            "expected_counts": [1233], "variant_column": "variant_sequence", "native_metrics": ["accuracy", "f1"],
            "split_evidence": "Pinned official train_dna_qwen.py:513-523 uses the released test split; all 1,233 question contexts identify chromosome 8, matching the chromosome-heldout contract."},
    "N03": {"dataset": "wanglab/variant_effect_non_snv", "revision": "aeba75d031b8cb507b3962ab486aa22700afa31c",
            "files": ["variant_effect_non_snv__test-00000-of-00001.parquet"], "splits": ["test"],
            "expected_counts": [873], "variant_column": "mutated_sequence", "native_metrics": ["accuracy", "f1"],
            "split_evidence": "Pinned official train_dna_qwen.py:530-547 uses the released test split and renames mutated_sequence to variant_sequence; 873 rows match the reported non-SNV test size."},
}


def digest_bytes(raw):
    return hashlib.sha256(raw).hexdigest()


def canonical(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def normalize_reference_label(task_id, answer):
    """Scorer-side source normalization; never used for prompt construction."""
    if task_id == "N01":
        return answer.strip().lower()
    if task_id == "N03":
        answer = answer.replace("[", "").replace("]", "").replace("'", "").replace("_", " ").strip()
    return answer.split(";")[0].strip().lower()


def build_record(task_id, row, index, source):
    """Separate allowed input fields from hidden labels/teacher explanations."""
    spec = TASKS[task_id]
    fields = {key: row[key] for key in ("question", "reference_sequence", spec["variant_column"])}
    if not all(isinstance(value, str) and value for value in fields.values()):
        raise ValueError(f"{task_id} row {index}: missing required string input")
    # The official LLM formatter uses this single user text; training-only
    # assistant labels/reasoning and DNA placeholders for separate encoders are
    # not included in the text-only inference preparation.
    user = (f"Reference sequence: {fields['reference_sequence']}\n"
            f"Variant sequence: {fields[spec['variant_column']]}\n"
            f"Question: {fields['question']}").strip()
    native_id = row.get("ID", row.get("__index_level_0__"))
    case_id = str(native_id) if task_id == "N02" and native_id is not None else f"{task_id}:{source['split']}:{index:06d}"
    prepared = {"task": task_id, "case_id": case_id, "variant": VARIANT, "split": source["split"],
                "messages": [{"role": "user", "content": user}]}
    provenance = {"task": task_id, "case_id": case_id, "source_dataset": spec["dataset"],
                  "source_dataset_revision": spec["revision"], "source_file": source["path"],
                  "source_file_sha256": source["sha256"], "source_split": source["split"],
                  "source_row_index": index, "original_source_id": native_id, "source_fields": fields,
                  "source_input_fields_sha256": digest_bytes(canonical(fields).encode()),
                  "model_input_sha256": digest_bytes(canonical(prepared).encode()),
                  "sequence_transformation": "none; complete released windows retained",
                  "source_variant_column": spec["variant_column"], "source_code_revision": CODE_REVISION}
    reference = {"task": task_id, "case_id": case_id, "source_split": source["split"],
                 "source_row_index": index, "source_answer": row["answer"],
                 "normalized_label": normalize_reference_label(task_id, row["answer"]),
                 "scorer_only": True}
    if "reasoning" in row:
        reference["source_teacher_reasoning"] = row["reasoning"]
        reference["teacher_reasoning_is_independently_verified_mechanism"] = False
    if "cleaned_pathogenicity" in row:
        reference["source_cleaned_pathogenicity"] = row["cleaned_pathogenicity"]
    return prepared, provenance, reference


def write_json(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")


def prepare(root):
    import pyarrow.parquet as pq

    root = Path(root)
    manifest = json.loads((root / SOURCE_DIR / "download_manifest.json").read_text())
    manifests = {Path(row["local_path"]).name: row for row in manifest}
    vocabulary_file = root / SOURCE_DIR / "kegg_class_vocabulary.json"
    vocabulary = json.loads(vocabulary_file.read_text())["labels"]
    if len(vocabulary) != 37:
        raise ValueError("Expected the fixed 37-class released KEGG vocabulary")
    report = {"created_at_utc": datetime.now(timezone.utc).isoformat(), "source_code_revision": CODE_REVISION,
              "tasks": [], "inference_performed": False, "training_performed": False,
              "source_reference_answers_exposed_to_solver": False,
              "N04_N05_substitution": False, "existing_configs_authorizations_results_changed": False}
    code_manifest = root / SOURCE_DIR / "source_code_manifest.json"
    if code_manifest.exists():
        report["source_code_files"] = json.loads(code_manifest.read_text())
    report["source_class_vocabulary_sha256"] = digest_bytes(vocabulary_file.read_bytes())
    for task_id, spec in TASKS.items():
        destination = root / "data/catalog_genomic_tasks" / task_id
        if destination.exists():
            raise FileExistsError(f"Preserve prior preparation; destination already exists: {destination}")
        inputs, provenances, references = [], [], []
        split_counts, chromosomes, sequence_lengths, source_records = {}, Counter(), {}, []
        for name, split, expected in zip(spec["files"], spec["splits"], spec["expected_counts"]):
            metadata = manifests[name]
            path = root / SOURCE_DIR / name
            actual = digest_bytes(path.read_bytes())
            if metadata.get("revision") != spec["revision"] or metadata["sha256"] != actual or metadata.get("publisher_lfs_sha256") != actual:
                raise ValueError(f"Pinned publisher source digest mismatch: {path}")
            rows = pq.read_table(path).to_pylist()
            if len(rows) != expected:
                raise ValueError(f"Unexpected {task_id}/{split} row count")
            split_counts[split] = len(rows)
            source_records.append(metadata)
            for index, row in enumerate(rows):
                prepared, provenance, reference = build_record(task_id, row, index, {"split": split, "path": str(SOURCE_DIR / name), "sha256": actual})
                inputs.append(prepared); provenances.append(provenance); references.append(reference)
                found = re.search(r"chromosome(?: number)?\s*[: ]\s*([0-9XY]+)", row["question"], re.I)
                chromosomes[found.group(1) if found else "unparsed"] += 1
                for field in ("reference_sequence", spec["variant_column"]):
                    sequence_lengths.setdefault(field, []).append(len(row[field]))
        if len({row["case_id"] for row in inputs}) != len(inputs):
            raise ValueError(f"Non-unique prepared source case IDs: {task_id}")
        if task_id == "N02" and chromosomes != {"8": len(inputs)}:
            raise ValueError("N02 is not exclusively the declared chromosome-8 holdout")
        classes = vocabulary if task_id == "N01" else ["benign", "pathogenic"]
        if any(row["normalized_label"] not in classes for row in references):
            raise ValueError(f"Reference outside fixed class vocabulary: {task_id}")
        destination.mkdir(parents=True)
        output_hashes = {}
        for name, records in (("model_inputs.jsonl", inputs), ("input_provenance.jsonl", provenances), ("scorer_references.jsonl", references)):
            raw = "".join(canonical(row) + "\n" for row in records).encode()
            (destination / name).write_bytes(raw)
            output_hashes[name] = digest_bytes(raw)
        write_json(destination / "class_vocabulary.json", {"classes": classes,
            "supplied_in_model_messages": False, "source": "Released source class namespace; no per-case class association is supplied to solver."})
        summary = {"task_id": task_id, "prepared_case_count": len(inputs), "prepared_variant": VARIANT,
                   "source_dataset": spec["dataset"], "source_dataset_revision": spec["revision"],
                   "source_code_revision": CODE_REVISION, "source_splits_in_order": spec["splits"], "split_counts": split_counts,
                   "split_evidence": spec["split_evidence"], "source_files": source_records,
                   "native_required_inputs": ["reference DNA window", "variant DNA window", "original question with native gene/chromosome context"] + (["complete pathway/network/gene context within question"] if task_id == "N01" else []),
                   "prepared_model_input_fields": ["messages.user.content"], "input_modalities": ["text", "DNA_sequence_text"],
                   "learned_encoder_required_for_source_DNA_LLM_specialist": True,
                   "learned_encoder_required_for_source_LLM_only_interface": False,
                   "native_metric_names": spec["native_metrics"], "class_vocabulary_count": len(classes),
                   "positive_class_for_VEP_f1": "pathogenic" if task_id != "N01" else None,
                   "scorer_only_fields": ["answer", "normalized_label"] + (["reasoning"] if task_id == "N01" else ["disease annotations within answer"]),
                   "sequence_length_ranges": {field: {"min": min(v), "max": max(v)} for field, v in sequence_lengths.items()},
                   "chromosome_context_counts": dict(chromosomes), "output_sha256": output_hashes,
                   "source_rows_retained": "All declared source rows, in source order; no label/outcome-based filtering.",
                   "input_scope": "Published human-genomic clinical-variant interpretation and disease prediction; no engineering or pathogen-fitness objective. Source question scaffolds/context were inspected separately from held-out answers; labels are exported only to the scorer side.",
                   "inference_status": "prepared_not_dispatched", "paper_reproduction": False,
                   "protocol_caveats": [
                       "Full released DNA windows are retained. Official DNA/hybrid evaluator defaults crop 1024 bases from each end for long windows; exact paper preprocessing varies by path. This full-window preparation is not an assertion of identical paper inputs.",
                       "Source LLM-only baselines use task fine-tuning; a future prompted Qwen run has a different training regime and must record its own frozen decoder and output protocol.",
                       "The released N01 evaluator reports multiclass substring accuracy only; paper macro-F1/precision/recall require an explicitly frozen multiclass scorer, class set and answer normalization.",
                       "The released VEP test hook searches the complete generated text for the ground-truth class. This can credit ambiguous answers and rationale mentions; strict final-label scoring is a separately labeled adaptation.",
                       "Paper temperature-0 statement and released VEP temperature-0.6 generation code differ; neither author run identity nor same-case predictions is archived here.",
                       "Correct disease/class predictions do not verify teacher or generated mechanisms. KEGG teacher rationales are scorer-only generated references; independent explanation support is unassessed.",
                       "Prior pretraining exposure is unknown. N01's original BioReason release is not a replacement for N04's network holdout, and none of N01–N03 replaces N05's expression-conditioned inputs.",
                   ]}
        write_json(destination / "preparation.json", summary)
        report["tasks"].append(summary)
    write_json(root / "reports/GENOMIC_NATIVE_INPUT_AUDIT_2026-10-15.json", report)
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    report = prepare(args.root)
    print(json.dumps({"prepared": {row["task_id"]: row["prepared_case_count"] for row in report["tasks"]},
                      "report": "reports/GENOMIC_NATIVE_INPUT_AUDIT_2026-10-15.json", "inference_performed": False}))


if __name__ == "__main__":
    main()
