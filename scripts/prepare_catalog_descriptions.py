"""Prepare pinned protein-description test exports without labels in prompts."""
import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
REVISION = "9f70da9e8f0df32e7e62846f7ad78a829b00c0fd"
TEMPLATE_FILE = "sources/catalog_descriptions__biot5__utils__templates__alpaca.json"
TEMPLATE_SHA256 = "853c698d1e733655a429232100e31a33beeab2a29d0b98ba63232c90e0f379de"
VARIANT = "QWEN_FULL_SEQUENCE_BIOT5_EXPORT_MOLINST_GOLD_ONLY_ROUGE"
TASKS = {
    "P23": {"filename": "task228_protein_function_molinst_pro_test.json", "split_name": "protein_protein_function", "count": 3494,
            "sha256": "7a984a304f7764056e789470e16797a75c120c1d13143cd1eb03728f2512c744", "split_sha256": "7d4e2316137dd5d7c5c58e46c520e9f75df5dbf3498dbc778bb59825a93edcaa"},
    "P24": {"filename": "task222_catalytic_activity_molinst_pro_test.json", "split_name": "protein_catalytic_activity", "count": 1601,
            "sha256": "8f53b17f74fcc3e0b32f1e68d8374405d70c1187ceb23db48665f19874e9d4e1", "split_sha256": "54ef39bb379d43370cdacfe309f5dd9a5a220260adc4c2a61b7557018f06f9fe"},
    "P25": {"filename": "task225_domain_motif_molinst_pro_test.json", "split_name": "protein_domain_motif", "count": 1400,
            "sha256": "b504bf077617661f855a2ad811e25edb1aeb7e98a8d636966c21e7baa02f6f46", "split_sha256": "14cb406c2396f3553ca80bc5e3fe75c1e4c7832ca44bfa3e955902e3b24c7b31"},
    "P26": {"filename": "task231_general_function_molinst_pro_test.json", "split_name": "protein_general_function", "count": 2633,
            "sha256": "eba4893a25e35a1467f67897402365aaf69fbdad9b1bf8abbc5c32723c6d04e6", "split_sha256": "8ce98b25534c15694895aedb7cd6e348269147a061f254c11993a906f93d5f82"},
}


def sha256(data):
    return hashlib.sha256(data).hexdigest()


def decode_sequence(serialized):
    if not isinstance(serialized, str) or not re.fullmatch(r"<bop>(?:<p>[A-Z])+<eop>", serialized):
        raise ValueError("Unrecognized source protein serialization; no silent cleaning")
    sequence = serialized[len("<bop>"):-len("<eop>")].replace("<p>", "")
    if "<bop>" + "".join("<p>" + aa for aa in sequence) + "<eop>" != serialized:
        raise ValueError("Complete sequence round trip failed")
    return sequence


def transform(task, index, instance, template):
    if set(instance) != {"id", "instruction", "input", "output"}:
        raise ValueError("Unexpected fields require explicit review")
    if not isinstance(instance["instruction"], str) or not instance["instruction"].strip():
        raise ValueError("Missing native instance instruction")
    outputs = instance["output"]
    if not isinstance(outputs, list) or len(outputs) != 1 or not isinstance(outputs[0], str) or not outputs[0]:
        raise ValueError("Expected one native target; no random or favorable reference choice")
    sequence = decode_sequence(instance["input"])
    prompt = template["prompt_input"].format(instruction=instance["instruction"], input=sequence)
    native_prompt = template["prompt_input"].format(instruction=instance["instruction"], input=instance["input"])
    common = {"task": task, "case_id": TASKS[task]["filename"] + ":" + str(index),
              "variant": VARIANT, "split": "official_BioT5_export_task_test", "source_index": index,
              "source_instance_id": instance["id"]}
    model = {**common, "system": "", "prompt": prompt,
             "fields": {"instruction": instance["instruction"], "sequence": sequence},
             "prompt_sha256": sha256(prompt.encode())}
    native = {**common, "instruction": instance["instruction"], "native_serialized_input": instance["input"],
              "native_untruncated_prompt": native_prompt, "native_prompt_sha256": sha256(native_prompt.encode())}
    ref = {**common, "target": outputs[0]}
    return model, native, ref


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--task", choices=sorted(TASKS), action="append")
    args = parser.parse_args()
    payload = (ROOT / TEMPLATE_FILE).read_bytes()
    if sha256(payload) != TEMPLATE_SHA256:
        raise ValueError("Native source prompt template changed")
    template = json.loads(payload)
    report_path = ROOT / "reports/catalog_description_preparation.json"
    report = json.loads(report_path.read_text()) if report_path.exists() else {"tasks": []}
    records = {r["task"]: r for r in report["tasks"]}
    for task in args.task or ["P25", "P24", "P26", "P23"]:
        spec = TASKS[task]
        source_path = ROOT / ("sources/biot5_data__tasks_plus__" + spec["filename"])
        source_bytes = source_path.read_bytes()
        split_path = ROOT / ("sources/biot5_data__splits_plus__molinst__eval__" + spec["split_name"] + "__test_tasks.txt")
        split_bytes = split_path.read_bytes()
        if sha256(source_bytes) != spec["sha256"] or sha256(split_bytes) != spec["split_sha256"]:
            raise ValueError("Pinned task source or native test-task list changed")
        if split_bytes.decode().splitlines() != [spec["filename"].removesuffix(".json")]:
            raise ValueError("Official task-specific test list differs")
        obj = json.loads(source_bytes)
        if len(obj["Instances"]) != spec["count"]:
            raise ValueError("Pinned test case count changed")
        model, native, refs, lengths, instruction_counts = [], [], [], [], Counter()
        for index, instance in enumerate(obj["Instances"]):
            m, n, r = transform(task, index, instance, template)
            model.append(m); native.append(n); refs.append(r)
            lengths.append(len(m["fields"]["sequence"]))
            instruction_counts[instance["instruction"]] += 1
        if len({r["source_instance_id"] for r in model}) != len(model):
            raise ValueError("Duplicate native instance IDs")
        folder = ROOT / "data/catalog_descriptions" / task
        folder.mkdir(parents=True, exist_ok=True)
        for name, items in [("model_inputs.jsonl", model), ("native_serialized_inputs.jsonl", native), ("scorer_references.jsonl", refs)]:
            with (folder / name).open("w") as handle:
                for row in items:
                    handle.write(json.dumps(row, ensure_ascii=False) + "\n")
            (folder / name).chmod(0o600)
        record = {"task": task, "cases": len(model), "variant": VARIANT, "source_file": str(source_path.relative_to(ROOT)),
                  "source_revision": REVISION, "source_sha256": spec["sha256"], "test_list_file": str(split_path.relative_to(ROOT)),
                  "test_list_sha256": spec["split_sha256"], "source_url": f"https://huggingface.co/datasets/QizhiPei/BioT5_finetune_dataset/resolve/{REVISION}/tasks_plus/{spec['filename']}",
                  "exact_official_BioT5_export_test": True, "original_Mol_Instructions_raw_archive_identity_verified": False,
                  "instruction_selection": "Exact per-instance instruction, as in pinned DataCollatorForMolinstNI; no task Definition substitution or random prompt selection",
                  "prompt_template": TEMPLATE_FILE, "native_template_sha256": TEMPLATE_SHA256,
                  "native_serialization_retained": True, "full_sequences_retained": True,
                  "sequence_lengths": {"min": min(lengths), "max": max(lengths)}, "native_unique_instruction_count": len(instruction_counts),
                  "input_allowlist": ["instruction", "complete decoded amino-acid sequence"], "scorer_only_fields": ["output"],
                  "native_protocol_adaptations": ["BioT5 amino-acid special tokens decoded for Qwen", "Complete sequences retained instead of native512-token encoder truncation", "Zero-shot Qwen rather than fitted BioT5/Mol-Instructions specialist"],
                  "metric_protocol": "Official Mol-Instructions gold-only HuggingFace ROUGE defaults: default tokenizer, use_stemmer=False, all four default ROUGE types, BootstrapAggregator mid.fmeasure; fixed scoring RNG seed42 disclosed",
                  "BioT5_metric_source_caveat": "Pinned BioT5+ wrapper computes references_new but passes [gold, decoded_input] pairs to ROUGE. This is not silently corrected or claimed equivalent; exact BioT5-paper metric comparison is unresolved.",
                  "likely_task_demands": {"labels": ["biological_annotation_prediction", "sequence_representation", "reference_description_generation"], "status": "provisional; no internal model computation inferred"},
                  "reference_answer_source": "Native task output description, separate from solver inputs",
                  "allowed_score_claim": "Lexical agreement with source reference descriptions under the fixed zero-shot full-sequence baseline",
                  "unsupported_score_claim": "ROUGE does not verify every functional fact, causal mechanism, independent rationale or lack of pretraining exposure",
                  "explanation_support_score": None, "inference_dispatched": 0, "training_or_head_fitting": False,
                  "files": {p.name: {"bytes": p.stat().st_size, "sha256": sha256(p.read_bytes())} for p in folder.glob("*.jsonl")}}
        (folder / "preparation.json").write_text(json.dumps(record, ensure_ascii=False, indent=2) + "\n")
        records[task] = record
        report = {"mode": "offline_preparation_no_inference", "tasks": list(records.values()), "source_code_revision": "cf65ae6dff63fdea8883dd17d46728a61bba386c",
                  "scorer_source": "sources/mol__evaluation__protein__eval.py", "rouge_source": "sources/catalog_descriptions__hf__rouge_pinned.py",
                  "rouge_revision": "1bc20e7e9df922e5dfb597c31a4ea8467a89caff", "rouge_score_version": "0.1.2",
                  "P27": {"status": "distinct_temporal_split_not_recovered", "basis": "NatureLM paper section4.4 uses NCBI sequence/annotation pairs with temporal division. Pinned official SFM/NatureLM tree and README expose models/notebooks but no frozen description test release or cutoff IDs.",
                          "source": "https://arxiv.org/html/2502.07527v3#S4.SS4", "substitution_with_P26_permitted": False,
                          "remaining": "Obtain author-released temporal test artifact, cutoff and metric configuration; P26 is not this split."}}
        report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n")
        print(json.dumps({"task": task, "cases": len(model), "output": str(folder)}), flush=True)


if __name__ == "__main__":
    main()
