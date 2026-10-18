"""Prepare all released P28 rows and native eligible inputs with no gold context."""
from collections import Counter
import json
from pathlib import Path

import bioreason_pro_contract as protocol


def prepare():
    import pyarrow.parquet as pq
    root, output = protocol.ROOT, protocol.OUTPUT
    if output.exists():
        raise ValueError("P28 preparation already exists; refuse replacement")
    sources = protocol.verified_sources()
    if protocol.file_sha(root / protocol.DATA_FILE) != protocol.DATA_SHA256:
        raise ValueError("Publisher-LFS-pinned test parquet changed")
    rows = pq.read_table(root / protocol.DATA_FILE, columns=protocol.INPUT_COLUMNS).to_pylist()
    excluded = set(protocol.EXCLUSIONS.read_text().splitlines())
    ids = [row["protein_id"] for row in rows]
    if len(rows) != 8630 or len(set(ids)) != 8630 or len(excluded) != 471 or not excluded <= set(ids):
        raise ValueError("Native released/excluded/eligible ID scope changed")
    output.mkdir(parents=True)
    eligible_ids, input_provenance = [], []
    with (output / "released_model_inputs.jsonl").open("w") as all_inputs, (output / "model_inputs.jsonl").open("w") as inputs:
        for index, row in enumerate(rows):
            case = protocol.model_case(index, row)
            serialized = json.dumps(case, ensure_ascii=False) + "\n"
            all_inputs.write(serialized)
            included = row["protein_id"] not in excluded
            if included:
                inputs.write(serialized); eligible_ids.append(case["case_id"])
            input_provenance.append({"case_id": case["case_id"], "source_index": index, "included_native_scope": included,
                "prompt_sha256": __import__("hashlib").sha256(case["messages"][0]["content"].encode()).hexdigest(),
                "supplied_input_field_sha256": {key: protocol.digest(row[key]) for key in protocol.INPUT_COLUMNS if key not in ("protein_id", "length")}})
    # Inputs and eligibility are fixed before reference columns are parsed.
    input_sha256 = protocol.file_sha(output / "model_inputs.jsonl")
    references = pq.read_table(root / protocol.DATA_FILE, columns=["protein_id", "go_bp", "go_mf", "go_cc"]).to_pylist()
    with (output / "scorer_references.jsonl").open("w") as handle:
        for index, row in enumerate(references):
            if row["protein_id"] != ids[index]:
                raise ValueError("Reference/source ID order differs")
            handle.write(json.dumps(protocol.reference(index, row), ensure_ascii=False) + "\n")
    for name, value in [("ordered_released_case_ids.json", ["P28:" + identity for identity in ids]),
                        ("ordered_eligible_case_ids.json", eligible_ids), ("excluded_native_case_ids.json", ["P28:" + identity for identity in ids if identity in excluded]),
                        ("input_provenance.json", input_provenance)]:
        protocol.save(output / name, value)
    report = {"task_id": "P28", "variant": protocol.VARIANT, "source_code_revision": protocol.CODE_REVISION,
              "source_data_revision": protocol.DATA_REVISION, "source_parquet": protocol.DATA_FILE, "source_parquet_sha256": protocol.DATA_SHA256,
              "released_cases": 8630, "native_excluded_cases": 471, "native_eligible_cases": len(eligible_ids),
              "native_exclusion_file": str(protocol.EXCLUSIONS.relative_to(root)), "native_exclusion_sha256": protocol.file_sha(protocol.EXCLUSIONS),
              "case_selection_policy": "Original public release IDs in original order minus pinned author common_proteins471 list, independent of labels/model outputs. Excluded cases prepared only, never scheduled.",
              "model_facing_fields": ["complete_original_amino_acid_sequence", "organism", "native_InterPro_context", "native_STRING_PPI_context", "native_GO_GPT_predictions", "native_label_independent_instruction"],
              "input_allowlist_source_columns": protocol.INPUT_COLUMNS,
              "forbidden_solver_fields": ["protein_names", "protein_function", "subcellular_location", "go_ids", "go_bp", "go_mf", "go_cc", "teacher reasoning", "teacher final_answer"],
              "native_flags": {"ask_all_go_aspects": True, "force_uniprot_summary": True, "interpro_in_prompt": True,
                    "ppi_in_prompt": True, "go_gpt_predictions_column": "go_pred", "add_uniprot_summary": True, "split_go_aspects": False,
                    "pass_at_k": 1, "apply_go_filtering_to_val_test": False},
              "source_input_nonempty_counts": {key: sum(bool(row[key]) for row in rows) for key in protocol.INPUT_COLUMNS},
              "complete_sequence_lengths": {"min": min(len(row["sequence"]) for row in rows), "max": max(len(row["sequence"]) for row in rows)},
              "all_sequences_uppercase_and_lengths_match": True,
              "native_model_difference": "Raw complete sequence replaces learned ESM3 layer37/protein projection; trained GOgraph encoder/projector200tokens is not replicated by Qwen. Native current eval passes no structure coordinates. This is a zero-shot system adaptation, not native full-model reproduction; native learned representations may be essential.",
              "published_protocol_differences": ["Author current label-independent all3-aspect/fixed-summary flags replace published gold-aspect-presence/summary-presence hints.",
                   "Fixed one generation, no oracle best-of-k selection; every eligible failure stays in denominator.",
                   "Complete source sequences retained rather than native2000-residue crop; frozen Qwen4096-token recipe differs from native/paper generation settings.",
                   "Released scorer extracts entire generated continuation at hardscore1; paper methods describe final-block extraction. Raw input and GO-GPT prompt context are never concatenated to outputs.",
                   "Native cafaeval dependency is unpinned; official1.3.0 source is frozen before Qwen calls, with native IA/ontology/propagation and explicit all-case completeness."],
              "temporal_contract": {"source": "https://www.biorxiv.org/content/10.64898/2026.03.19.712954v1.full", "locator": "Methods4.1.3",
                   "training_annotation_cutoff": "before November2022", "target_new_annotation_window": "March2023–February2024, no prior experimental annotation in target aspect",
                   "source_snapshots_described": "November2022 and February2024 GOA", "verification": "Published contract plus exact pinned released IDs; annotation timestamps absent from final parquet, so no independent reconstruction claimed. Extended214→226/2025 notebook is a different artifact, not substituted."},
              "reference_evidence": "Curated source GO annotations, kept scorer-only; unknown/absent function is not established negative biology",
              "likely_demands": {"labels": ["learned biological prediction", "sequence representation", "integration of permitted predictor context", "ontology mapping"], "classification_is_provisional": True},
              "good_score_establishes": "Recovery of recorded held-out GO annotations under the declared full-sequence contextual zero-shot system",
              "bad_score_establishes": "Limited annotation recovery; does not isolate reasoning or rule out unannotated biological functions",
              "explanation_support_score": None, "contamination": "Public model exposure and predictor/context snapshot histories are not proven contamination-free; no gold/teacher context or feedback tuning.",
              "P29_substitution": False, "execution_authorized": False, "inference_dispatched": 0,
              "verified_source_files_sha256": sources, "eligible_input_sha256": input_sha256,
              "files": {path.name: {"sha256": protocol.file_sha(path), "bytes": path.stat().st_size} for path in output.iterdir() if path.is_file()}}
    protocol.save(output / "preparation.json", report)
    protocol.save(root / "reports/catalog_bioreason_pro_preparation.json", report)
    print(json.dumps({"task_id": "P28", "released": 8630, "eligible": len(eligible_ids), "excluded": 471,
                      "input_sha256": input_sha256, "execution_authorized": False}))
    return report


if __name__ == "__main__":
    prepare()
