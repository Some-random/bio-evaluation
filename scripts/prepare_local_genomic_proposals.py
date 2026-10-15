#!/usr/bin/env python3
"""Write reviewable genomic configs without inference, queues or authorizations.

Existing files are never overwritten. The 4096-token baseline recipe is copied
exactly from the frozen original local baseline, without outcomes or tuning.
"""
import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def file_digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def write_new(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("x") as handle:
        json.dump(value, handle, ensure_ascii=False, indent=2)
        handle.write("\n")


def prepare(root=ROOT, gpu=4):
    root = Path(root)
    if gpu not in {4, 5, 6, 7}:
        raise ValueError("Choose an existing pinned local replica")
    baseline = json.loads((root / "configs/local_labbench_b07.json").read_text())
    if baseline["generation"]["max_tokens"] != 4096 or baseline["generation"]["n"] != 1:
        raise ValueError("Existing baseline is not the requested fixed 4096-token recipe")
    serving_path = f"configs/local_model_gpu{gpu}.json" if gpu != 5 else "configs/local_model.json"
    server_path = f".local/local_model_server_gpu{gpu}.json" if gpu != 5 else ".local/local_model_server.json"
    serving = json.loads((root / serving_path).read_text())
    if serving["model"] != baseline["model"] or serving["revision"] != baseline["model_revision"]:
        raise ValueError("Replica is not the same pinned model")
    outputs = []
    for task in ("N01", "N02", "N03"):
        directory = f"data/catalog_genomic_tasks/{task}"
        input_name, reference_name, vocabulary_name = (f"{directory}/{name}" for name in ("model_inputs.jsonl", "scorer_references.jsonl", "class_vocabulary.json"))
        preparation_name = f"{directory}/preparation.json"
        preparation = json.loads((root / preparation_name).read_text())
        cases = [json.loads(line) for line in (root / input_name).read_text().splitlines() if line]
        if (len(cases) != preparation["prepared_case_count"] or len({case["case_id"] for case in cases}) != len(cases)
                or any(case["task"] != task or case["variant"] != preparation["prepared_variant"] for case in cases)):
            raise ValueError("Genomic source input contract changed")
        if file_digest(root / input_name) != preparation["output_sha256"]["model_inputs.jsonl"]:
            raise ValueError("Prepared original input hash changed")
        if any(len(case["messages"]) != 1 or case["messages"][0]["role"] != "user" or not isinstance(case["messages"][0]["content"], str) for case in cases):
            raise ValueError("Prepared native dialogue changed")
        review_name = f"configs/local_genomics_{task.lower()}_review.json"
        config_name = f"configs/local_genomics_{task.lower()}_proposed.json"
        if (root / review_name).exists() or (root / config_name).exists():
            raise FileExistsError("Preserve prior genomic reviews/proposals")
        review = {"task_id": task, "reviewed_at_utc": datetime.now(timezone.utc).isoformat(), "input_review_only": True,
                  "source_input_path": input_name, "source_input_sha256": file_digest(root / input_name),
                  "approved_case_ids": [case["case_id"] for case in cases], "held_cases": [],
                  "approved_cases": len(cases), "full_public_cases": len(cases), "held_case_count": 0,
                  "selection_based_on_model_outputs": False,
                  "basis": "Input-only task-goal and public-source contract review: published human clinical-variant interpretation/disease prediction with complete DNA and source gene/chromosome/pathway context. Source question scaffolds and context were inspected; source IDs/order/required fields were validated. No claim of manual inspection of every nucleotide. Held-out labels, teacher reasoning and model outcomes were not used for case selection.",
                  "review_findings": ["No engineering, pathogen-fitness enhancement, immune-evasion optimization or operational pathogen protocol objective is present in this source task contract.",
                                      "Clinical pathogenic/benign interpretation concerns human alleles; organism names or the word pathogenic alone are not grounds for exclusion.",
                                      "N01 preserves test then val as the released official evaluation construction; N02 preserves chromosome-8 test; N03 preserves its original non-SNV test and source indel representation.",
                                      "Original questions and complete DNA windows are unchanged; teacher rationales and labels remain solely in scorer references. N04/N05 are separate contracts."],
                  "review_scope": "Proposed local Qwen baseline only. No inference is launched, task allowlist extended or queue edited by this review.",
                  "previously_flagged_requests_transferred": False}
        write_new(root / review_name, review)
        settings = {"run_id": f"qwen38_27b_{task.lower()}_full_windows_2026-10-15",
                    "proposal_status": "proposed_requires_root_authorization", "created_at_utc": datetime.now(timezone.utc).isoformat(),
                    "model": baseline["model"], "model_revision": baseline["model_revision"],
                    "checkpoint_precision": baseline["checkpoint_precision"], "gpu_ids": [gpu],
                    "endpoint": f"http://127.0.0.1:{serving['port']}/v1", "serving_config_file": serving_path, "server_record_file": server_path,
                    "approved_task_ids": [task], "variant": preparation["prepared_variant"], "input_file": input_name, "review_file": review_name,
                    "concurrency": baseline["concurrency"], "generation": baseline["generation"],
                    "runner": "scripts/run_local_labbench_multimodal.py", "executor": "scripts/execute_local_genomics.py", "scorer": "scripts/score_local_genomics.py",
                    "scorer_reference_file": reference_name, "scorer_reference_sha256": file_digest(root / reference_name),
                    "class_vocabulary_file": vocabulary_name, "source_dataset_revision": preparation["source_dataset_revision"],
                    "source_code_revision": preparation["source_code_revision"], "tool_access": [],
                    "input_modalities": ["DNA_sequence_text", "text"], "model_facing_fields": ["reference_sequence", "variant_sequence", "question"] + (["pathway_network_and_gene_context_in_question"] if task == "N01" else []),
                    "case_scope": "official_released_test_then_val_290" if task == "N01" else "official_released_test",
                    "prompt_policy": "Original source LLM user string and complete released DNA windows; no additional output instruction, class list, label, teacher rationale, retrieval or tool.",
                    "metric_policy": "Primary source predicates on qualified reasoning+final continuation, never prompt text. STRICT_FINAL_LABEL is a separate final-content diagnostic; N01 global37 zero-division0 macro scores supplemental. Scorer code freezes all details before outcomes.",
                    "paper_comparison": "Full released windows and prompted Qwen differ from specialist representations/SFT, some source cropping and author decoding. Native decoded-byte equivalence is not claimed. N04 network holdout and N05 expression measurement contracts are not replaced."}
        files = [input_name, review_name, vocabulary_name, preparation_name, f"{directory}/input_provenance.jsonl",
                 settings["runner"], settings["scorer"], settings["executor"], "scripts/prepare_local_genomic_proposals.py"]
        settings["frozen_files_sha256"] = {name: file_digest(root / name) for name in sorted(files)}
        write_new(root / config_name, settings)
        outputs.append({"task_id": task, "cases": len(cases), "review": review_name, "proposed_config": config_name})
    return outputs


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--gpu", type=int, default=4)
    args = parser.parse_args()
    print(json.dumps({"proposals": prepare(gpu=args.gpu), "inference_performed": False, "authorizations_changed": False}))
