"""Prepare input-only Qwen baselines from pinned public BioT5+ test exports.

This preserves native serialized inputs alongside an explicit full-sequence text
adaptation. It does not launch inference, approve cases, or alter any registry.
"""
import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
DATA_REVISION = "9f70da9e8f0df32e7e62846f7ad78a829b00c0fd"
VARIANT = "QWEN_FULL_SEQUENCE_TEXT_BIOT5_TEST"
TASKS = {
    "P01": [("solubility", "task177_solubility_peer_test.json", 1999)],
    "P02": [("binary_localization", "task180_binloc_peer_test.json", 1749)],
    "P10": [("human_ppi", "task174_human_ppi_peer_test.json", 237)],
    "P11": [("yeast_ppi", "task171_yeast_ppi_peer_test.json", 394)],
    "P43": [("bindingdb", "task18_bindingdb_drugban_dti_test.json", 9840),
            ("biosnap", "task21_biosnap_drugban_dti_test.json", 5493),
            ("human", "task24_human_drugban_dti_test.json", 1200)],
}
PROTEIN = re.compile(r"<bop>(?:<p>[A-Z])+<eop>")


def digest(value):
    return hashlib.sha256(value).hexdigest()


def decode_sequence(tokenized):
    if PROTEIN.fullmatch(tokenized) is None:
        raise ValueError("Unrecognized protein serialization; no silent cleaning")
    sequence = tokenized[5:-5].replace("<p>", "")
    if "<bop>" + "".join("<p>" + x for x in sequence) + "<eop>" != tokenized:
        raise ValueError("Protein round trip failed")
    return sequence


def adapt_input(task, serialized):
    expected_names = ["Protein_A", "Protein_B"] if task in {"P10", "P11"} else ["Protein"]
    lines = serialized.split("\n")
    fields = {}
    adapted = []
    if task == "P43":
        if len(lines) != 2 or not lines[0].startswith("Molecule: <bom>") or not lines[0].endswith("<eom>"):
            raise ValueError("Expected the complete native SELFIES/protein pair")
        molecule = lines.pop(0)[len("Molecule: <bom>"):-len("<eom>")]
        # A dot is the native SELFIES disconnected-component separator.
        if not molecule or re.fullmatch(r"(?:\[[^\[\]\s]+\]|\.)+", molecule) is None:
            raise ValueError("Unrecognized SELFIES serialization")
        fields["molecule_selfies"] = molecule
        adapted.append("Molecule (SELFIES): " + molecule)
    if len(lines) != len(expected_names):
        raise ValueError("Required full protein inputs missing or extra")
    for name, line in zip(expected_names, lines):
        prefix = name + ": "
        if not line.startswith(prefix):
            raise ValueError("Unexpected input field or ordering")
        sequence = decode_sequence(line[len(prefix):])
        fields[name] = sequence
        adapted.append(prefix + sequence)
    return "\n".join(adapted), fields


def transform(task, dataset, filename, obj, source_sha256):
    definitions = obj.get("Definition")
    if not isinstance(definitions, list) or len(definitions) != 1 or not isinstance(definitions[0], str):
        raise ValueError("Freeze the exact definition selection before execution")
    definition = definitions[0]
    model, native, refs = [], [], []
    ids = set()
    for index, instance in enumerate(obj["Instances"]):
        # Source outputs and all metadata are deliberately excluded from prompts.
        if set(instance) != {"id", "input", "output"}:
            raise ValueError("Unexpected source fields require explicit review")
        if instance["id"] in ids:
            raise ValueError("Duplicate source case ID")
        ids.add(instance["id"])
        case_id = dataset + ":" + instance["id"]
        adapted, fields = adapt_input(task, instance["input"])
        metadata = {"task": task, "case_id": case_id, "dataset": dataset,
                    "split": "official_BioT5_export_test", "variant": VARIANT,
                    "source_file": filename, "source_index": index,
                    "source_sha256": source_sha256}
        prompt = definition + "\n" + adapted
        model.append({**metadata, "system": "", "prompt": prompt,
                      "fields": {"definition": definition, **fields},
                      "prompt_sha256": digest(prompt.encode())})
        native.append({**metadata, "definition": definition,
                       "native_serialized_input": instance["input"],
                       "native_input_sha256": digest(instance["input"].encode())})
        if not isinstance(instance["output"], list) or len(instance["output"]) != 1 or instance["output"][0] not in {"Yes.", "No."}:
            raise ValueError("Unexpected source label vocabulary")
        refs.append({**metadata, "target": instance["output"][0],
                     "target_binary": int(instance["output"][0] == "Yes.")})
    return model, native, refs


def write_jsonl(path, records):
    with path.open("w") as handle:
        for record in records:
            handle.write(json.dumps(record, ensure_ascii=False) + "\n")
    path.chmod(0o600)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--task", choices=sorted(TASKS), action="append")
    parser.add_argument("--output", type=Path, default=ROOT / "data/catalog_sequence_tasks")
    args = parser.parse_args()
    report = {"mode": "offline_preparation_no_dispatch", "protocol_variant": VARIANT,
              "data_repository": "QizhiPei/BioT5_finetune_dataset", "revision": DATA_REVISION,
              "native_serialization_preserved": True, "source_to_PEER_row_identity_verified": False,
              "comparison_limit": "Same public BioT5+ export test; Qwen text adaptation, not a native BioT5 architecture or supervised-head reproduction. Original PEER/DrugBAN row identity remains to verify.",
              "safety_case_review": "pending; this script does not approve inference", "tasks": []}
    for task in args.task or TASKS:
        folder = args.output / task
        folder.mkdir(parents=True, exist_ok=True)
        model, native, refs = [], [], []
        datasets = []
        for dataset, filename, count in TASKS[task]:
            source = ROOT / "sources" / ("biot5_data__tasks_plus__" + filename)
            payload = source.read_bytes()
            obj = json.loads(payload)
            if len(obj["Instances"]) != count:
                raise ValueError("Unexpected pinned source count")
            m, n, r = transform(task, dataset, filename, obj, digest(payload))
            model.extend(m); native.extend(n); refs.extend(r)
            datasets.append({"dataset": dataset, "cases": len(m), "file": str(source.relative_to(ROOT)),
                             "sha256": digest(payload), "url": f"https://huggingface.co/datasets/QizhiPei/BioT5_finetune_dataset/resolve/{DATA_REVISION}/tasks_plus/{filename}"})
        for name, records in [("model_inputs.jsonl", model), ("native_serialized_inputs.jsonl", native), ("scorer_references.jsonl", refs)]:
            write_jsonl(folder / name, records)
        record = {"task": task, "cases": len(model), "datasets": datasets,
                  "sequence_count": sum(sum(k.startswith("Protein") for k in r["fields"]) for r in model),
                  "complete_sequences_retained": True, "scorer_labels_excluded_from_input": True,
                  "files": {p.name: {"bytes": p.stat().st_size, "sha256": digest(p.read_bytes())} for p in folder.glob("*.jsonl")}}
        report["tasks"].append(record)
    (args.output / "preparation.json").write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({"tasks": {r["task"]: r["cases"] for r in report["tasks"]}, "output": str(args.output)}))


if __name__ == "__main__":
    main()
