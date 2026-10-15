"""CPU-only comparison of source DrugBAN graphs/test rows to BioT5 exports."""
from collections import Counter
import csv
import hashlib
import importlib.metadata
import json
from pathlib import Path

from local_dti_common import ROOT, digest, file_digest, write_json

SOURCES = {
    "human": "b8d9664fc15e3bbc6abf6a82cc1e12ba512c33d31f06baf25b95786911d4f005",
    "biosnap": "27cd0e8fce7225540a5fda9744b8990ffc60b2c0bec206b4b33255026b08b6d1",
    "bindingdb": "6c4b810ae1fb91b1f2f497fa898d336d9c775bab0671ebb0f42cf66c2ad8ad67",
}


def canonical(smiles):
    from rdkit import Chem
    molecule = Chem.MolFromSmiles(smiles)
    if molecule is None:
        raise ValueError("Source chemical string cannot be parsed")
    return Chem.MolToSmiles(molecule, canonical=True, isomericSmiles=True)


def main():
    import selfies
    from rdkit import RDLogger
    RDLogger.DisableLog("rdApp.warning")
    RDLogger.DisableLog("rdApp.error")
    inputs = [json.loads(s) for s in (ROOT / "data/catalog_sequence_tasks/P43/model_inputs.jsonl").read_text().splitlines()]
    refs = {r["case_id"]: r for r in map(json.loads, (ROOT / "data/catalog_sequence_tasks/P43/scorer_references.jsonl").read_text().splitlines())}
    records = []
    for dataset, expected in SOURCES.items():
        path = ROOT / f"sources/local_dti_drugban_{dataset}_test.csv"
        if file_digest(path) != expected:
            raise ValueError("Pinned author test CSV changed")
        native = list(csv.DictReader(path.open()))
        export = [r for r in inputs if r["dataset"] == dataset]
        if len(native) != len(export):
            raise ValueError("Native/export test counts differ")
        first, second, errors = [], [], []
        sequence_equal, labels_equal, graph_equal = 0, 0, 0
        cache = {}
        def graph(text):
            if text not in cache:
                cache[text] = canonical(text)
            return cache[text]
        for index, (n, e) in enumerate(zip(native, export)):
            target = refs[e["case_id"]]["target_binary"]
            native_value = float(n["Y"])
            if native_value not in {0.0, 1.0}:
                raise ValueError("Native label outside binary vocabulary")
            native_target = int(native_value)
            sequence_equal += n["Protein"] == e["fields"]["Protein"]
            labels_equal += native_target == target
            try:
                cg_native = graph(n["SMILES"])
                cg_export = graph(selfies.decoder(e["fields"]["molecule_selfies"]))
                graph_equal += cg_native == cg_export
                first.append((cg_native, n["Protein"], native_target))
                second.append((cg_export, e["fields"]["Protein"], target))
            except Exception as exc:
                errors.append({"source_index": index, "case_id": e["case_id"], "type": type(exc).__name__})
        same = not errors and first == second
        records.append({"dataset": dataset, "cases": len(export), "source_csv": str(path.relative_to(ROOT)), "source_sha256": expected,
                        "source_revision": "9923f8c99959e00263103ff9ac61ba0eaccc8e02", "source_split": f"DrugBAN datasets/{dataset}/random/test.csv",
                        "ordered_full_protein_sequences_equal": sequence_equal == len(native), "ordered_labels_equal": labels_equal == len(native),
                        "ordered_isomeric_graph_matches": graph_equal, "chemical_parse_failures": len(errors), "parse_failure_details": errors,
                        "ordered_graph_sequence_and_label_equal": same,
                        "complete_graph_sequence_label_multiset_equal": not errors and Counter(first) == Counter(second),
                        "native_canonical_row_sha256": digest(first), "export_canonical_row_sha256": digest(second),
                        "chemical_standardization": "RDKit parse and canonical isomeric SMILES only; preserve salts/charges/stereochemistry, no component removal or gold-derived repair",
                        "solver_inputs_changed": False, "no_inference": True})
        print(json.dumps({k: v for k, v in records[-1].items() if k not in {"parse_failure_details"}}), flush=True)
    report = {"source": "Author DrugBAN random test splits, pinned immutable revision", "packages": {p: importlib.metadata.version(p) for p in ["selfies", "rdkit"]},
              "selfies_module_version_attribute": selfies.__version__, "datasets": records,
              "interpretation": "Identity verification is scorer-side provenance only, not new predictive context or label-based case selection. Any mismatches stay explicit; no scored inputs are repaired."}
    write_json(ROOT / "reports/local_dti_source_identity.json", report)


if __name__ == "__main__":
    main()
