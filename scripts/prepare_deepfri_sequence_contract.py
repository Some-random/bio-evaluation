#!/usr/bin/env python3
"""Prepare source-only DeepFRI test sequence contracts; never call a model.

Run with the project's .venv Python (RDKit). Released full FASTA sequences and
PDB-modeled residue sequences remain distinct. Current-RDKit parsing is a
qualified reconstruction, not a claim about unpublished author caches.
"""
import argparse
import collections
import csv
import hashlib
import json
import pathlib
import re
import string
import tempfile
import zipfile


RESIDUE_SYMBOLS = dict(zip(
    "GLY ALA SER PRO VAL THR CYS ILE LEU ASN ASP GLN LYS GLU MET HIS PHE ARG TYR TRP".split(),
    "GASPVTCILNDQKEMHFRYW",
))
ALPHABET = set(" " + string.ascii_uppercase + string.ascii_lowercase + string.digits)
TASKS = {
    "P12": ("EnzymeCommission", "EC_2020.04", "EC", None),
    "P13": ("GeneOntology", "GO_2019.06.18", "BP", 1),
    "P14": ("GeneOntology", "GO_2019.06.18", "MF", 0),
    "P15": ("GeneOntology", "GO_2019.06.18", "CC", 2),
}


def sha256(path):
    digest = hashlib.sha256()
    with pathlib.Path(path).open("rb") as stream:
        while chunk := stream.read(8 * 1024 * 1024):
            digest.update(chunk)
    return digest.hexdigest()


def write_json(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n")


def write_jsonl(path, rows):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w") as stream:
        for row in rows:
            stream.write(json.dumps(row, ensure_ascii=False) + "\n")


def read_fasta(path):
    records = {}
    case_id = None
    parts = []
    for line in path.read_text().splitlines():
        if line.startswith(">"):
            if case_id is not None:
                records[case_id] = "".join(parts)
            case_id = line[1:].split()[0]
            if case_id in records:
                raise ValueError("Duplicate FASTA case ID")
            parts = []
        elif line.strip():
            if case_id is None:
                raise ValueError("Sequence before FASTA header")
            parts.append(line.strip())
    if case_id is not None:
        if case_id in records:
            raise ValueError("Duplicate FASTA case ID")
        records[case_id] = "".join(parts)
    return records


def read_split(path):
    with path.open() as stream:
        reader = csv.DictReader(stream)
        rows = list(reader)
    if "<95%" not in reader.fieldnames:
        raise ValueError("Missing fixed 95% cutoff column")
    ids = [row["PDB-chain"] for row in rows if row["<95%"] == "1"]
    if len(ids) != len(set(ids)):
        raise ValueError("Duplicate test CSV case ID")
    if any(row["<95%"] not in {"0", "1"} for row in rows):
        raise ValueError("Unknown test cutoff flag")
    return ids, [row["PDB-chain"] for row in rows if row["<95%"] == "0"]


def ec_names(directory):
    """Supplemental 2026 names; no protein annotation rows are consulted."""
    names = {}
    accession = None
    pieces = []
    for line in (directory / "expasy__enzyme.dat").read_text().splitlines():
        if line.startswith("ID   "):
            accession = line[5:].strip()
            pieces = []
        elif line.startswith("DE   "):
            pieces.append(line[5:].strip())
        elif line == "//" and accession:
            names[accession] = " ".join(pieces)
            accession = None
    for line in (directory / "expasy__enzclass.txt").read_text().splitlines():
        match = re.match(r"^([0-9-]+)\.\s*([0-9-]+)\.\s*([0-9-]+)\.([0-9-]+)\s+(.+)$", line)
        if match:
            names[".".join(match.groups()[:4])] = match.group(5)
    return names


def vocabulary(directory, stem, branch, index):
    annotation = directory / ("deepfri__preprocessing__data__nrPDB-" + stem + "_annot.tsv")
    with annotation.open() as stream:
        reader = csv.reader(stream, delimiter="\t")
        header = [next(reader) for _ in range(3 if index is None else 12)]
    terms = header[1 if index is None else index * 4 + 1]
    if len(terms) != len(set(terms)):
        raise ValueError("Duplicate vocabulary term")
    if index is None:
        supplemental = ec_names(directory)
        names = [supplemental.get(term) for term in terms]
        description_source = "ExPASy ENZYME 02-Sep-2026 supplemental display names; not a verified 2020 author prompt or vocabulary revision"
    else:
        names = header[index * 4 + 3]
        if len(names) != len(terms):
            raise ValueError("GO name/term header length mismatch")
        description_source = "Exact released 2019.06.18 annotation header"
    return {
        "branch": branch, "class_count": len(terms),
        "selection_rule": "Complete global released annotation-header vocabulary in exact source order; no test-positive selection",
        "source_annotation_path": str(annotation), "source_annotation_sha256": sha256(annotation),
        "description_source": description_source,
        "classes": [{"index": i, "class_id": term, "description": names[i]} for i, term in enumerate(terms)],
    }


def read_references(annotation, index, selected_ids, term_to_index):
    selected_ids = set(selected_ids)
    references = {}
    with annotation.open() as stream:
        reader = csv.reader(stream, delimiter="\t")
        for _ in range(3 if index is None else 13):
            next(reader)
        for row in reader:
            if not row or row[0] not in selected_ids:
                continue
            column = 1 if index is None else index + 1
            terms = row[column].split(",") if len(row) > column and row[column] else []
            if any(term not in term_to_index for term in terms):
                raise ValueError("Reference outside frozen global class vocabulary")
            references[row[0]] = {
                "case_id": row[0], "scorer_only": True,
                "positive_class_ids": terms,
                "positive_class_indices": [term_to_index[term] for term in terms],
            }
    return references


def modeled_sequence(mol):
    """Source residue traversal + allowed-bond connected components, no tensors.

    Mirrors the pinned Protein.from_molecule residue normalization and
    Protein.to_sequence. It deliberately retains the source canonical-residue
    key (number, insertion code, residue name), which excludes chain ID.
    Full TorchDrug graph/features are not executed, so native equivalence is
    qualified even when all published dataset counts happen to agree.
    """
    symbols = []
    atom_to_residue = []
    last = None
    unknown = collections.Counter()
    chains = set()
    for atom in mol.GetAtoms():
        info = atom.GetPDBResidueInfo()
        if info is None:
            return {"status": "missing_pdb_residue_info"}
        name = info.GetResidueName().strip()
        key = (info.GetResidueNumber(), info.GetInsertionCode(), name)
        if key != last:
            last = key
            if info.GetInsertionCode() not in ALPHABET:
                return {"status": "invalid_insertion_code"}
            if info.GetChainId() not in ALPHABET:
                return {"status": "invalid_chain_id"}
            chains.add(info.GetChainId())
            if name not in RESIDUE_SYMBOLS:
                unknown[name] += 1
            symbols.append(RESIDUE_SYMBOLS.get(name, "G"))
        atom_to_residue.append(len(symbols) - 1)
    if not symbols:
        return {"status": "empty_modeled_residues"}
    parent = list(range(len(symbols)))

    def find(item):
        while parent[item] != item:
            parent[item] = parent[parent[item]]
            item = parent[item]
        return item

    for bond in mol.GetBonds():
        if str(bond.GetBondType()) not in {"SINGLE", "DOUBLE", "TRIPLE", "AROMATIC"}:
            continue
        left = find(atom_to_residue[bond.GetBeginAtomIdx()])
        right = find(atom_to_residue[bond.GetEndAtomIdx()])
        parent[max(left, right)] = min(left, right)
    roots = [find(i) for i in range(len(symbols))]
    dotted = "".join(("." if i > 0 and roots[i] > roots[i - 1] else "") + symbol for i, symbol in enumerate(symbols))
    return {
        "status": "retained_current_rdkit_residue_projection",
        "full_modeled_residue_sequence": "".join(symbols),
        "native_to_sequence_reconstruction": dotted,
        "modeled_residue_count": len(symbols), "connected_component_count": len(set(roots)),
        "unknown_residue_names_mapped_to_glycine": dict(unknown),
        "chain_ids": sorted(chains),
    }


def audit_structure_test(directory, dataset, fasta, excluded_ids, output):
    from rdkit import Chem, RDLogger, rdBase
    # Suppress case-specific chemical logs from the console; statuses remain in
    # the immutable per-case audit. This is not selection by task outcomes.
    RDLogger.DisableLog("rdApp.*")
    archive = directory / (dataset + ".test.zip")
    provenance = json.loads(archive.with_suffix(".zip.provenance.json").read_text())
    if sha256(archive) != provenance["sha256"]:
        raise ValueError("Test ZIP differs from frozen acquisition provenance")
    audit = []
    with zipfile.ZipFile(archive) as source, tempfile.TemporaryDirectory(prefix="deepfri-test-pdb-") as tmp:
        local = pathlib.Path(tmp) / "case.pdb"
        for filename in sorted(name for name in source.namelist() if name.startswith("test/") and name.endswith(".pdb") and name.count("/") == 1):
            raw = source.read(filename)  # zipfile verifies each member CRC
            case_id = pathlib.PurePosixPath(filename).name.split("_")[0]
            row = {"case_id": case_id, "native_pdb_member": filename, "pdb_sha256": hashlib.sha256(raw).hexdigest(), "pdb_bytes": len(raw)}
            local.write_bytes(raw)
            mol = Chem.MolFromPDBFile(str(local))
            row.update(modeled_sequence(mol) if mol is not None else {"status": "rdkit_MolFromPDBFile_returned_None"})
            row["excluded_by_test95_csv"] = case_id in excluded_ids
            sequence = fasta.get(case_id)
            row["released_full_fasta_available"] = sequence is not None
            row["released_fasta_sha256"] = hashlib.sha256(sequence.encode()).hexdigest() if sequence is not None else None
            if "full_modeled_residue_sequence" in row:
                row["modeled_equals_released_fasta"] = row["full_modeled_residue_sequence"] == sequence if sequence is not None else None
            audit.append(row)
    write_jsonl(output, audit)
    retained = [row for row in audit if row["status"] == "retained_current_rdkit_residue_projection" and not row["excluded_by_test95_csv"]]
    return audit, retained, {"rdkit_version": rdBase.rdkitVersion, "python_projection_sha256": sha256(__file__), "test_zip_sha256": provenance["sha256"], "test_zip_bytes": provenance["bytes"]}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-directory", type=pathlib.Path, default=pathlib.Path("sources/deepfri_contract_audit_2026-10-15"))
    parser.add_argument("--output-directory", type=pathlib.Path, default=pathlib.Path("data/catalog_deepfri_tasks"))
    args = parser.parse_args()
    directory = args.source_directory
    datasets = {}
    for dataset, stem in [("EnzymeCommission", "EC_2020.04"), ("GeneOntology", "GO_2019.06.18")]:
        prefix = "deepfri__preprocessing__data__nrPDB-" + stem
        fasta = read_fasta(directory / (prefix + "_test_sequences.fasta"))
        split_ids, excluded_ids = read_split(directory / (prefix + "_test.csv"))
        test_list = (directory / (prefix + "_test.txt")).read_text().split()
        if set(split_ids) != set(test_list):
            raise ValueError("95% CSV and released test list disagree")
        audit, retained, parser_metadata = audit_structure_test(directory, dataset, fasta, set(excluded_ids), args.output_directory / dataset / "pdb_parser_audit.jsonl")
        datasets[dataset] = (fasta, split_ids, audit, retained, parser_metadata)
    summaries = []
    for task_id, (dataset, stem, branch, index) in TASKS.items():
        out = args.output_directory / task_id
        fasta, split_ids, audit, retained, parser_metadata = datasets[dataset]
        vocab = vocabulary(directory, stem, branch, index)
        write_json(out / "class_vocabulary.json", vocab)
        terms = {row["class_id"]: row["index"] for row in vocab["classes"]}
        annotation = pathlib.Path(vocab["source_annotation_path"])
        all_ids = set(split_ids) | {row["case_id"] for row in retained}
        references = read_references(annotation, index, all_ids, terms)
        write_jsonl(out / "scorer_references.jsonl", ({"task_id": task_id, **references[case_id]} for case_id in sorted(references)))
        released = [{"task_id": task_id, "case_id": case_id, "split": "test95", "variant": "DEEPFRI_RELEASED_FASTA_TEST95_FULL_SEQUENCE_PREPARED", "full_protein_sequence": fasta[case_id]} for case_id in split_ids if case_id in fasta]
        write_jsonl(out / "released_fasta_inputs.jsonl", released)
        # Missing labels do not remove an input: the failure is explicit and
        # blocks evaluation rather than changing the denominator after scoring.
        modeled = [{"task_id": task_id, "case_id": row["case_id"], "split": "test95", "variant": "RECONSTRUCTED_CURRENT_RDKIT_PDB_TEST95_FULL_MODELED_RESIDUES_PREPARED", "full_modeled_residue_sequence": row["full_modeled_residue_sequence"], "native_to_sequence_reconstruction": row["native_to_sequence_reconstruction"]} for row in retained]
        write_jsonl(out / "pdb_parser_inputs.jsonl", modeled)
        pdb_ids = {row["case_id"] for row in audit}
        retained_ids = [row["case_id"] for row in retained]
        summary = {
            "task_id": task_id, "dataset": dataset, "branch": branch, "test_cutoff": 0.95,
            "status": "source_only_prepared_confidence_adapter_not_frozen",
            "counts": {"global_classes": len(terms), "released_fasta_headers": len(fasta), "test95_csv_ids": len(split_ids), "released_test95_full_sequences": len(released), "archive_pdbs": len(audit), "current_rdkit_projection_retained": len(retained), "current_rdkit_projection_rejected": len(audit) - len(retained), "modeled_equal_released_fasta": sum(row.get("modeled_equals_released_fasta") is True for row in retained), "modeled_different_from_released_fasta": sum(row.get("modeled_equals_released_fasta") is False for row in retained), "retained_without_released_fasta": sum(not row["released_full_fasta_available"] for row in retained), "modeled_sequences_over_native_550_limit": sum(row["modeled_residue_count"] > 550 for row in retained)},
            "membership": {"fasta_outside_test95_csv": sorted(set(fasta) - set(split_ids)), "test95_csv_missing_fasta": sorted(set(split_ids) - set(fasta)), "test95_csv_missing_archive_pdb": sorted(set(split_ids) - pdb_ids), "archive_pdb_outside_test95_csv": sorted(pdb_ids - set(split_ids)), "retained_without_scorer_reference": sorted(set(retained_ids) - set(references))},
            "parser_rejection_counts": dict(collections.Counter(row["status"] for row in audit if row["status"] != "retained_current_rdkit_residue_projection")),
            "ordered_current_rdkit_retained_case_ids": retained_ids,
            "parser_metadata": parser_metadata,
            "native_input_modalities": ["protein modeled residue identities from native PDB graph (sequence encoder)", "PDB coordinates/connectivity available in source archive; not equivalent to supplying complete SEQRES FASTA"],
            "native_transform": "Pinned ProtST annotation config applies residue view and deterministic first-550 modeled-residue truncation; both prepared source representations retain complete sequences, without applying that transform.",
            "qualification": "Source-only artifacts. Current-RDKit residue projection does not execute all TorchDrug graph/features, does not identify the author's unpublished processed pickle or dependency versions, and is not claimed to reproduce the printed native test cardinality or author case identity.",
            "score_requirement": "A genuine finite confidence/logit for every case/class pair in fixed global order. No hard-label substitution, missing-score fabrication, label-guided extraction, new head training, provider calls or inference performed.",
            "interpretation_caveats": ["Multilabel annotation recovery is prediction evidence; explanations/mechanisms are not scored.", "Released annotations are incomplete; an absent annotation is not established biological absence.", "Public pretraining exposure is unknown.", "A prompted full-sequence text confidence adapter would be a zero-shot adaptation of trained specialist heads and source truncation, with its own frozen protocol."],
        }
        summary["files_sha256"] = {path.name: sha256(path) for path in [out / "class_vocabulary.json", out / "released_fasta_inputs.jsonl", out / "pdb_parser_inputs.jsonl", out / "scorer_references.jsonl"]}
        write_json(out / "preparation.json", summary)
        summaries.append(summary)
        print(json.dumps({"task_id": task_id, "counts": summary["counts"], "membership": summary["membership"], "parser_rejection_counts": summary["parser_rejection_counts"]}), flush=True)
    write_json(args.output_directory / "preparation_summary.json", {"tasks": summaries, "no_inference": True, "no_authorization_or_queue_changes": True})


if __name__ == "__main__":
    main()
