"""Prepare exact released P29 ID/OOD rows using input-only native RL formatting."""
import csv
import hashlib
import json
from collections import Counter

import posttrain_protein_contract as protocol


def prepare():
    if protocol.OUTPUT.exists():
        raise ValueError("P29 preparation already exists; refuse replacement")
    sources = protocol.verified_sources()
    prepared = {}
    all_ids = {}
    for split, (source_name, expected_count, sha) in protocol.SPLITS.items():
        source = protocol.SOURCE / ("protein__" + source_name + ".csv")
        if protocol.file_sha(source) != sha:
            raise ValueError("Exact author Drive test CSV changed")
        folder = protocol.OUTPUT / split
        folder.mkdir(parents=True)
        ids, species, provenance, lengths, prompt_bytes = [], Counter(), [], [], []
        with source.open() as handle, (folder / "model_inputs.jsonl").open("w") as output:
            reader = csv.DictReader(handle)
            if "protein_name" in reader.fieldnames:
                raise ValueError("Native optional name field unexpectedly present")
            for index, row in enumerate(reader):
                # The formatter receives only the allowlist, before reference
                # parsing; no annotation can select a case, aspect or branch.
                supplied = {key: row[key] for key in protocol.INPUT_COLUMNS}
                case = protocol.model_case(index, split, supplied)
                output.write(json.dumps(case, ensure_ascii=False) + "\n")
                ids.append(case["case_id"]); species[row["organism"]] += 1
                lengths.append(len(row["sequence"]))
                prompt_bytes.append(len(case["messages"][0]["content"].encode()))
                provenance.append({"case_id": case["case_id"], "source_index": index,
                    "prompt_sha256": hashlib.sha256(case["messages"][0]["content"].encode()).hexdigest(),
                    "supplied_fields_sha256": {key: protocol.digest(supplied[key]) for key in protocol.INPUT_COLUMNS}})
        if len(ids) != expected_count or len(ids) != len(set(ids)):
            raise ValueError("Complete original source-order ID count changed")
        input_hash = protocol.file_sha(folder / "model_inputs.jsonl")
        augmented = 0
        seed_stats = Counter()
        ontology = protocol.native_ontology()
        with source.open() as handle, (folder / "scorer_references.jsonl").open("w") as output:
            for index, row in enumerate(csv.DictReader(handle)):
                reference = protocol.reference(index, split, row)
                if reference["case_id"] != ids[index]:
                    raise ValueError("Reference order mismatch")
                output.write(json.dumps(reference, ensure_ascii=False) + "\n")
                augmented += bool(reference["predictor_go_terms_added_to_native_target"])
                seed = protocol.native_api().extract_go_ids(row["go_pred"])
                native_target = set(reference["native_augmented_go_terms"])
                curated_target = set(reference["curated_only_go_terms_diagnostic"])
                seed_stats["supplied_predictor_term_count"] += len(seed)
                seed_stats["native_target_direct_overlap_term_count"] += len(seed & native_target)
                seed_stats["curated_target_direct_overlap_term_count"] += len(seed & curated_target)
                seed_stats["cases_with_supplied_predictor_native_target_overlap"] += bool(seed & native_target)
                seed_stats["cases_with_supplied_predictor_curated_target_overlap"] += bool(seed & curated_target)
                overlap_scores = protocol.score_prediction(seed, reference, ontology)
                seed_stats["native_augmented_F1_sum"] += overlap_scores["native_augmented_F1"]
                seed_stats["curated_only_F1_sum_diagnostic"] += overlap_scores["curated_only_F1_diagnostic"]
        protocol.save(folder / "ordered_case_ids.json", ids)
        protocol.save(folder / "input_provenance.json", provenance)
        protocol.save(folder / "organism_counts.json", dict(species))
        all_ids[split] = {identity.split(":", 2)[2] for identity in ids}
        prepared[split] = {"source_file": str(source.relative_to(protocol.ROOT)), "source_sha256": sha,
            "cases": len(ids), "ordered_case_ids_sha256": protocol.digest(ids), "organism_counts": dict(species),
            "complete_sequence_lengths": {"min": min(lengths), "max": max(lengths), "above_native_2000_crop": sum(n > 2000 for n in lengths)},
            "largest_complete_prompt_utf8_bytes": max(prompt_bytes), "conservative_context_token_bound_including_1024_controls_and_4096_output": max(prompt_bytes) + 5120,
            "input_sha256": input_hash, "predictor_augmented_reference_cases": augmented,
            "seed_predictor_overlap": {**{k: v for k, v in seed_stats.items() if not k.endswith("_sum") and "_sum_" not in k},
                "seed_context_only_native_augmented_mean_propagated_F1": seed_stats["native_augmented_F1_sum"] / len(ids),
                "seed_context_only_curated_mean_propagated_F1_diagnostic": seed_stats["curated_only_F1_sum_diagnostic"] / len(ids),
                "interpretation": "Offline input/reference dependence audit using exactly GO IDs already supplied in go_pred. This is not a Qwen inference result or context ablation. Native target augmentation can reward recovery/copying of supplied predictions; curated annotations also overlap input predictions, whose historical training/data independence is unknown."},
            "files": {p.name: {"sha256": protocol.file_sha(p), "bytes": p.stat().st_size} for p in folder.iterdir() if p.is_file()}}
        if max(prompt_bytes) + 5120 > 262144:
            raise ValueError("Complete prompt conservative context bound exceeds pinned model")
    if all_ids["id"] & all_ids["ood"]:
        raise ValueError("Original ID/OOD protein IDs overlap")
    report = {"task_id": "P29", "variant": protocol.VARIANT, "source_code_revision": protocol.CODE_REVISION,
        "source_dataset": "Exact public author Drive protein/{id-test.csv,ood-test.csv}; tied to pinned author data/download.sh",
        "source_data_version": "Drive object IDs and folder-advertised byte counts with locally frozen SHA256; no immutable publisher content hash is advertised by Drive",
        "splits": prepared, "id_ood_protein_id_overlap_count": 0, "case_selection": "All original source-order ID6989 and species-held-out OOD7883; no label or output based filtering, no P28 temporal substitution.",
        "input_allowlist_source_columns": protocol.INPUT_COLUMNS,
        "model_facing_fields": ["complete_original_amino_acid_sequence", "organism", "native_InterPro_context", "native_GO_GPT_predictions", "exact_released_RL_instruction"],
        "forbidden_solver_fields": ["protein_names", "protein_function", "subcellular_location", "go_ids", "go_bp", "go_mf", "go_cc", "go_bp_leaf", "go_mf_leaf", "go_cc_leaf", "go_pred_leaf", "reasoning", "final_answer"],
        "native_prompt_flags": {"go_gpt_predictions_column": "go_pred", "interpro_in_prompt": True, "ppi_in_prompt": False,
            "ask_all_go_aspects": True, "append_uniprot_suffix": False, "go_summary_tags_in_prompt": True},
        "native_metric": "Unmodified author SFT-aligned continuation GO extractor; ontology is_a/part_of closure including roots and unknown-ID self terms; uniform weight per propagated term; arithmetic mean of per-protein P/R/F1 across all planned cases.",
        "native_target_augmentation": "Author resolve_gold_terms_from_row unions curated leaf/ancestor fields AND go_pred_leaf while go_pred is supplied as context. Native reference and input are dependent: the metric can reward recovery/copying of supplied predictions and does not isolate novel function inference. Preserve that augmented target as primary; curated-only reference union is a separate fixed diagnostic, also with predictor overlap and unknown historical independence. Never select the more favorable metric or remove native context.",
        "metric_units": "fractions0–1; propagated mean set-F1, not P28 CAFA Fmax or information-weighted Fmax; paper figure captions call protein scores Fmax, while released eval code computes fixed-set mean F1.",
        "source_disagreements": ["Published paper describes protein ESM3/projector-conditioned SFT and RL; released train_protein_grpo.py instead loads standalone AutoModelForCausalLM and full text sequence/context without an ESM3 encoder.",
            "Released SFT evaluator chooses hf_reasoning loader; these CSVs lack explicit user/system columns, so that path uses generic default instructions and omits metadata. This prospective baseline follows the separate released RL prompt, not that SFT path.",
            "Paper describes PPI and includes a name-header example; released RL eval explicitly disables PPI, and optional singular protein_name is absent. Plural protein_names is scorer-only and never substituted.",
            "Released RL evaluator default512newtokens/T0.7 differs from fixed4096-token Qwen recipe. No outcome-guided change, no checkpoint selection or training is performed.",
            "Original RL tokenizer decodes continuation with skip_special_tokens=True; Qwen3.8 API exposes generated reasoning/final channels. Only generated channels are reconstructed for native extraction, with no prompt context; tokenizer-level byte identity is not claimed.",
            "Source prompt is preserved verbatim inside a single user message, using pinned Qwen3.8 chat template rather than author's raw tokenizer call. Complete sequences retained, no native SFT2000-residue truncation."],
        "interpretation": {"task_demands": {"labels": ["learned biological prediction", "sequence representation", "permitted predictor-context integration", "ontology mapping"], "classification_is_provisional": True},
            "actually_supplied": "Complete sequence, organism, full native InterPro and GO-GPT predicted context, exact released RL prompt/summary-tag instruction. No names, curated GO, teacher trace, expression, structures or PPI.",
            "reference_answer_source": "Primary native union of curated GO plus predictor go_pred_leaf, dependent on supplied go_pred context; curated-only diagnostic has predictor overlap too, with historical independence unverified. Both references scorer-only.",
            "good_score_establishes": "Agreement with the frozen augmented target, potentially by recovering/copying supplied predictor GO terms; not isolated novel function inference. Curated-only diagnostic separately measures recorded annotation recovery with declared input overlap.",
            "bad_score_establishes": "Limited recovery under the chosen full-sequence/context interface; does not isolate reasoning, rule out unannotated functions, or dismiss learned specialist representations.",
            "explanation_correctness": "Unassessed independently. Correct GO predictions do not validate rationales; missing support does not automatically mean false."},
        "paper_source": "https://arxiv.org/html/2606.16517v1", "paper_locators": ["§3.1", "AppendixA.3/A.4", "AppendixB.1/B.4", "AppendixTable9"],
        "contamination": "No gold/teacher fields in requests, no training, model/output selection or test-feedback tuning. Public pretraining exposure and upstream predictor histories remain unknown; species split does not prove pretraining decontamination.",
        "explanation_support_score": None, "verified_source_files_sha256": sources,
        "execution_authorized": False, "inference_dispatched": 0}
    protocol.save(protocol.OUTPUT / "preparation.json", report)
    protocol.save(protocol.ROOT / "reports/catalog_posttrain_protein_preparation.json", report)
    print(json.dumps({"task_id": "P29", "cases": {k: v["cases"] for k, v in prepared.items()}, "execution_authorized": False}))
    return report


if __name__ == "__main__":
    prepare()
