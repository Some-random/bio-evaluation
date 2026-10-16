"""Prepare complete native public test splits for three zero-shot Qwen baselines.

Author release bytes and target ontologies are pinned before reading test labels.
No training, model selection, head fitting or model inference occurs here.
"""
import argparse
import csv
import hashlib
import json
import math
from pathlib import Path
import pickle
import tarfile

ROOT = Path(__file__).resolve().parents[1]
LABEL_PATH = "sources/catalog_extended__protst__data__zero_shot_classification__subloc_language.tsv"
LABEL_SHA256 = "6816a996802ea328f57a6bac201e14d8632dee670e00eb735081758bc7b1a44e"
SPECS = {
    "P03": {"dataset": "subcellular_localization", "target_field": "localization", "test_count": 2773,
            "md5": "37cb6138b8d4603512530458b7c8a77d", "sha256": "8c3cf116b7e82779a7cd6b280cf50d8d69d826ef88667ed3a29fda5751184a66",
            "source_url": "https://miladeepgraphlearningproteindata.s3.us-east-2.amazonaws.com/peerdata/subcellular_localization.tar.gz",
            "native_metric": "accuracy", "variant": "QWEN_ZERO_SHOT_FULL_SEQUENCE_DEEPLOC_NATIVE_LABELS",
            "objective": "Predict the subcellular location of this protein. Use the original DeepLoc/ProtST class IDs and descriptions below. Return only one integer class ID from 0 through 9.",
            "target_definition": "Original ten-compartment DeepLoc curated localization class; integer mapping from pinned official ProtST subloc_language.tsv, independently of test labels.",
            "units": "native integer class ID 0-9", "source_loader": "sources/torchdrug__subcellular_localization.py",
            "reference_type": "curated subcellular annotation", "split_caveat": "Actual publisher-MD5-matched test LMDB has2773 rows; loader docstring2768 is stale. Pinned load_lmdbs/load_sequence performs no row filtering."},
    "P07": {"dataset": "fluorescence", "target_field": "log_fluorescence", "test_count": 27217,
            "md5": "d63d1d51ec8c20ff0d981e4cbd67457a", "sha256": "20c9d114234a5136c4087920480e7fa2d586a653061f0cd141f626a984ede8bd",
            "source_url": "https://s3.amazonaws.com/songlabdata/proteindata/data_pytorch/fluorescence.tar.gz",
            "native_metric": "Spearman correlation", "variant": "QWEN_ZERO_SHOT_FULL_SEQUENCE_TAPE_FLUORESCENCE_PYTORCH",
            "objective": "Predict the log-fluorescence intensity of this green fluorescent protein variant on the original TAPE/Sarkisyan experimental scale (the log_fluorescence target). Return only one finite numerical value.",
            "target_definition": "Source TAPE log_fluorescence[0], corresponding to experimental GFP log-fluorescence intensity; no log-base conversion or target rescaling is performed.",
            "units": "native TAPE log-fluorescence scale; no invented physical unit or base conversion", "source_loader": "sources/torchdrug__fluorescence.py",
            "reference_type": "experimental GFP fluorescence measurement", "split_caveat": "Original complete released PyTorch test LMDB; source-defined distant-mutation test split,27217 rows."},
    "P08": {"dataset": "stability", "target_field": "stability_score", "test_count": 12851,
            "md5": "aa1e06eb5a59e0ecdae581e9ea029675", "sha256": "0580bc854e13701431dbbaf942756b8611598e3422599104bc7b0a151b6ec38f",
            "source_url": "https://s3.amazonaws.com/songlabdata/proteindata/data_pytorch/stability.tar.gz",
            "native_metric": "Spearman correlation", "variant": "QWEN_ZERO_SHOT_FULL_SEQUENCE_TAPE_STABILITY_PYTORCH",
            "objective": "Predict the continuous protein-folding stability score of this sequence on the original TAPE/Rocklin experimental scale (the stability_score target), which measures resistance to unfolding under the source assay. Return only one finite numerical value.",
            "target_definition": "Source TAPE stability_score[0], an experimental proxy for intrinsic folding stability under the source concentration-threshold assay. The released numerical scale is preserved without conversion.",
            "units": "native TAPE stability_score scale; no conversion to melting temperature or energy", "source_loader": "sources/torchdrug__stability.py",
            "reference_type": "experimental protein folding-stability measurement", "split_caveat": "Publisher-MD5-matched PyTorch/ProtST release has12851 test rows. Original2019 TAPE paper table lists12839; do not claim historical paper-split identity."},
}


def sha256(data):
    return hashlib.sha256(data).hexdigest()


def native_labels():
    payload = (ROOT / LABEL_PATH).read_bytes()
    if sha256(payload) != LABEL_SHA256:
        raise ValueError("Native label ontology changed")
    rows = list(csv.DictReader(payload.decode().splitlines(), delimiter="\t"))
    if [int(r["id"]) for r in rows] != list(range(10)):
        raise ValueError("Native ontology must have exactly the original ten IDs")
    return rows


def transform(task, index, row, labels=None):
    spec = SPECS[task]
    sequence = row["primary"]
    if not isinstance(sequence, str) or not sequence or any(not ("A" <= c <= "Z") for c in sequence):
        raise ValueError("Sequence outside the source uppercase representation; do not clean silently")
    prompt = spec["objective"]
    if task == "P03":
        if labels is None or [int(r["id"]) for r in labels] != list(range(10)):
            raise ValueError("Native label definitions required")
        prompt += "\n\n" + "\n".join(r["id"] + ": " + r["name"] + ". " + r["description"] for r in labels)
    prompt += "\n\nComplete protein sequence:\n" + sequence
    common = {"task": task, "case_id": spec["dataset"] + ":test:" + str(index),
              "variant": spec["variant"], "split": "official_released_test", "dataset": spec["dataset"], "source_index": index}
    # Only primary enters the solver input. Parent/topology/mutation counts and
    # every target field remain outside the prompt, independently of label value.
    model = {**common, "system": "", "prompt": prompt,
             "fields": {"sequence": sequence, "objective": spec["objective"],
                        **({"native_label_ontology": labels} if task == "P03" else {})},
             "prompt_sha256": sha256(prompt.encode())}
    value = row[spec["target_field"]]
    if task == "P03":
        if not isinstance(value, int) or not 0 <= value <= 9:
            raise ValueError("Reference outside fixed native ontology")
        target = value
    else:
        if getattr(value, "size", 1) != 1:
            raise ValueError("Native target must be scalar")
        target = float(value.item() if hasattr(value, "item") else value)
        if not math.isfinite(target):
            raise ValueError("Nonfinite native target")
    ref = {**common, "target": target, "target_field": spec["target_field"]}
    return model, ref


def lmdb_rows(task):
    import lmdb
    spec = SPECS[task]
    archive_path = ROOT / f"sources/catalog_extended__{task}.tar.gz"
    payload = archive_path.read_bytes()
    if hashlib.md5(payload).hexdigest() != spec["md5"] or sha256(payload) != spec["sha256"]:
        raise ValueError("Author release digest mismatch")
    member = f"{spec['dataset']}/{spec['dataset']}_test.lmdb/data.mdb"
    extracted = ROOT / ".local/catalog_extended_lmdb" / member
    with tarfile.open(archive_path) as archive:
        source = archive.extractfile(member)
        expected = source.read()
    if not extracted.exists() or sha256(extracted.read_bytes()) != sha256(expected):
        extracted.parent.mkdir(parents=True, exist_ok=True)
        extracted.write_bytes(expected)
    env = lmdb.open(str(extracted.parent), readonly=True, lock=False, readahead=False, meminit=False, max_readers=1)
    try:
        with env.begin() as transaction:
            count = pickle.loads(transaction.get(b"num_examples"))
            if count != spec["test_count"]:
                raise ValueError("Native released test count changed")
            for index in range(count):
                row = pickle.loads(transaction.get(str(index).encode()))
                yield index, row
    finally:
        env.close()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--task", choices=sorted(SPECS), action="append")
    args = parser.parse_args()
    tasks = args.task or ["P03", "P08", "P07"]
    report_path = ROOT / "reports/catalog_extended_preparation.json"
    prior = json.loads(report_path.read_text()).get("tasks", []) if report_path.exists() else []
    records = {r["task"]: r for r in prior}
    for task in tasks:
        spec = SPECS[task]
        labels = native_labels() if task == "P03" else None
        folder = ROOT / "data/catalog_extended" / task
        folder.mkdir(parents=True, exist_ok=True)
        lengths, full_sequences, references = [], [], []
        for index, row in lmdb_rows(task):
            model, ref = transform(task, index, row, labels)
            full_sequences.append(model); references.append(ref)
            lengths.append(len(row["primary"]))
        for name, items in [("model_inputs.jsonl", full_sequences), ("scorer_references.jsonl", references)]:
            with (folder / name).open("w") as handle:
                for item in items:
                    handle.write(json.dumps(item, ensure_ascii=False) + "\n")
            (folder / name).chmod(0o600)
        record = {"task": task, **spec, "cases": len(full_sequences), "original_test_rows_retained": True,
                  "full_sequence_lengths": {"min": min(lengths), "max": max(lengths)},
                  "training_rows_read": 0, "label_based_selection": False, "inference_dispatched": 0,
                  "input_interface": "Complete amino-acid sequence and fixed objective; native class ontology additionally supplied for P03",
                  "likely_demands": {"labels": ["biological_outcome_prediction", "sequence_representation"], "status": "provisional description; no internal-computation inference"},
                  "reference_evidence": spec["reference_type"],
                  "good_score_establishes": "Outcome agreement on this released test under the fixed zero-shot full-sequence protocol",
                  "bad_score_establishes": "Limited outcome recovery in this representation/regime; not an isolated measure of general reasoning",
                  "explanation_score": None, "mechanism_reference": "not evaluated; correct prediction does not certify explanation",
                  "regime_comparison": "New prompted zero-shot Qwen baseline; native-trained TAPE/ProtST heads are a different training regime. Same released data/metric is not full historical-paper reproduction.",
                  "native_label_source": LABEL_PATH if task == "P03" else None,
                  "protocol_evidence": [spec["source_loader"], "sources/catalog_extended__torchdrug__data__dataset.py",
                                        "sources/catalog_extended__tape__datasets.py" if task != "P03" else LABEL_PATH],
                  "paper_definition_source": "https://arxiv.org/html/1906.08230#S4.SS2" if task != "P03" else "https://github.com/DeepGraphLearning/ProtST/tree/db53a76ed2430eb66dd9c8134ace99fd60980fb3/data/zero_shot_classification",
                  "files": {p.name: {"bytes": p.stat().st_size, "sha256": sha256(p.read_bytes())} for p in folder.glob("*.jsonl")}}
        records[task] = record
        (folder / "preparation.json").write_text(json.dumps(record, ensure_ascii=False, indent=2) + "\n")
        report_path.write_text(json.dumps({"mode": "offline_preparation", "tasks": list(records.values()), "new_head_training": False,
                                          "native_metrics_preserved": True, "safety_case_scope": "Generic localization, GFP fluorescence and non-pathogen folding-stability outcome prediction; no operational protocols or pathogen-fitness dispatch.",
                                          "data_records": "sources/catalog_extended_data_fetch.json", "label_records": "sources/catalog_extended_protocol_fetch.json"}, ensure_ascii=False, indent=2) + "\n")
        print(json.dumps({"task": task, "cases": len(full_sequences), "output": str(folder)}), flush=True)


if __name__ == "__main__":
    main()
