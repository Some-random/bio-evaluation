"""Prepare the original FLIP human_cell test split for zero-shot prediction.

Only input rendering is adapted to Qwen. No training, tuning or inference occurs.
"""
import csv
import hashlib
import io
import json
import math
from pathlib import Path
import zipfile

ROOT = Path(__file__).resolve().parents[1]
MD5 = "0f8b1e848568f7566713d53594c0ca90"
REVISION = "d5c35cc716ca93c3c74a0b43eef5b60cbf88521f"
VARIANT = "QWEN_ZERO_SHOT_FULL_SEQUENCE_FLIP_HUMAN_CELL"
OBJECTIVE = ("Predict the experimentally measured protein melting temperature in degrees Celsius "
             "for the FLIP Meltome human_cell assay.\nReturn a single numerical value.\nProtein sequence:\n")


def transform(rows):
    inputs, refs = [], []
    for index, row in enumerate(rows):
        if set(row) != {"sequence", "target", "set", "validation"}:
            raise ValueError("Unexpected native columns")
        if row["set"] not in {"train", "test"} or row["validation"] not in {"True", "False"}:
            raise ValueError("Unrecognized source split designation")
        if row["set"] != "test":
            continue
        if row["validation"] != "False":
            raise ValueError("Test row marked as validation")
        sequence = row["sequence"]
        if not sequence or any(not ("A" <= x <= "Z") for x in sequence):
            raise ValueError("Non-sequence content requires review; do not silently clean")
        value = float(row["target"])
        if not math.isfinite(value):
            raise ValueError("Non-finite experimental target")
        common = {"task": "P06", "case_id": f"human_cell:{index}", "dataset": "FLIP_Meltome_human_cell",
                  "split": "official_test", "variant": VARIANT, "source_index": index}
        prompt = OBJECTIVE + sequence
        inputs.append({**common, "system": "", "prompt": prompt,
                       "fields": {"sequence": sequence, "assay": "FLIP Meltome human_cell", "target_units": "degrees Celsius"},
                       "prompt_sha256": hashlib.sha256(prompt.encode()).hexdigest()})
        refs.append({**common, "target": value, "target_source_string": row["target"]})
    return inputs, refs


def main():
    source = ROOT / "sources/catalog_meltome.zip"
    payload = source.read_bytes()
    if hashlib.md5(payload).hexdigest() != MD5:
        raise ValueError("FLIP archive does not match the publisher digest pinned by ProtST")
    with zipfile.ZipFile(io.BytesIO(payload)) as archive:
        rows = list(csv.DictReader(io.TextIOWrapper(archive.open("splits/human_cell.csv"))))
    inputs, refs = transform(rows)
    if len(rows) != 7158 or len(inputs) != 1366:
        raise ValueError("Unexpected original split counts")
    folder = ROOT / "data/catalog_sequence_tasks/P06"
    folder.mkdir(parents=True, exist_ok=True)
    for name, records in [("model_inputs.jsonl", inputs), ("scorer_references.jsonl", refs)]:
        with (folder / name).open("w") as handle:
            for record in records:
                handle.write(json.dumps(record) + "\n")
        (folder / name).chmod(0o600)
    report = {"task": "P06", "protocol_variant": VARIANT, "cases": len(inputs), "native_metric": "Spearman correlation",
              "model_training_regime": "zero-shot full-sequence prediction; no head fitted",
              "source_split": "human_cell.csv, set=test and validation=False", "native_split_preserved": True,
              "full_sequences_preserved": True, "scorer_labels_excluded_from_inputs": True,
              "source_file": "sources/catalog_meltome.zip", "source_sha256": hashlib.sha256(payload).hexdigest(),
              "publisher_md5_matched": MD5, "revision": REVISION,
              "source_url": f"https://raw.githubusercontent.com/J-SNACKKB/FLIP/{REVISION}/splits/meltome/splits.zip",
              "information_supplied": "Complete amino-acid sequence, fixed assay name and requested numeric unit. No target measurements, training rows, protein names or annotations supplied.",
              "reference_evidence": "Original experimental Meltome measurements distributed in the FLIP human_cell split",
              "likely_task_demands": ["learned biological outcome prediction", "sequence representation"],
              "task_demand_status": "provisional analyst description; no inference about model computation",
              "comparison_limit": "Native data/split/metric with a new prompted zero-shot Qwen baseline. ProtST fitted supervised regression heads; training regimes differ.",
              "allowed_claim": "Correlation with held-out human_cell melting measurements under the declared zero-shot baseline",
              "unsupported_claim": "No validated mechanism, general reasoning score, experimental optimization or contamination-free claim follows.",
              "safety_case_review": "Human proteome thermal property prediction; root agent must freeze the case scope before dispatch.",
              "files": {p.name: {"bytes": p.stat().st_size, "sha256": hashlib.sha256(p.read_bytes()).hexdigest()} for p in folder.glob("*.jsonl")}}
    (folder / "preparation.json").write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({"task": "P06", "cases": len(inputs), "output": str(folder)}))


if __name__ == "__main__":
    main()
