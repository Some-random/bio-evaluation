#!/usr/bin/env python3
"""CPU-only RAbD numbering/chain preparation. Never emits residue identities.

The full acquired coordinate files remain scorer-side provenance. This script
does not create a solver request, classify biological eligibility, or dispatch.
"""
from __future__ import annotations

import argparse
import ast
import csv
import hashlib
import json
import sys
import tarfile
from datetime import datetime
from pathlib import Path
from types import SimpleNamespace
from zoneinfo import ZoneInfo

PDB_UTILS_SHA256 = "a3a1cc86b1ddbfd3913802e56cb61d8761669c5c8159cb21c35471d37ecaa4b0"
ROSTER_SHA256 = "f1c43fd1cdca4e24b913ca701f3a5569d161179798842d59e5557a76323a0c6e"
STANDARD = set("GLY ALA VAL LEU ILE PHE TRP TYR ASP HIS ASN GLU LYS GLN MET ARG SER THR CYS PRO SEC UNK".split())


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def save(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, allow_nan=False) + "\n")


def stamp():
    return datetime.now(ZoneInfo("America/Los_Angeles")).isoformat()


class Residue:
    """Private transient values needed by the pinned parser definition."""
    def __init__(self, number, insertion, name, point=None):
        self.number, self.insertion, self.name, self.point = number, insertion, name, point

    def get_id(self):
        return self.number, self.insertion

    def get_symbol(self):
        return self.name


class Chain:
    def __init__(self, name, residues):
        self.name, self.residues = name, list(residues)

    def __len__(self):
        return len(self.residues)

    def get_residue(self, index):
        return self.residues[index]

    def get_span(self, start, end):
        return Chain(self.name, self.residues[start:end])

    def set_id(self, name):
        self.name = name

    def get_id(self):
        return self.name

    def get_ca_pos(self, index):
        return self.residues[index].point


def native_method(source, name, namespace):
    """Load only a hash-pinned upstream pure structural method, without imports."""
    if hashlib.sha256(source).hexdigest() != PDB_UTILS_SHA256:
        raise ValueError("upstream numbering source hash mismatch")
    tree = ast.parse(source)
    cls = next(n for n in tree.body if isinstance(n, ast.ClassDef) and n.name == "AAComplex")
    method = next(n for n in cls.body if isinstance(n, ast.FunctionDef) and n.name == name)
    if any(isinstance(n, (ast.Import, ast.ImportFrom)) for n in ast.walk(method)):
        raise ValueError("numbering method unexpectedly imports code")
    exec(compile(ast.fix_missing_locations(ast.Module(body=[method], type_ignores=[])), "pinned_native_numbering", "exec"), namespace)
    return namespace[method.name]


def native_mask_function(source):
    return native_method(source, "_extract_antibody_info", {"VOCAB": SimpleNamespace(abrv_to_symbol=lambda name: name)})


def resolve_chains(original, current_rows, available):
    """Use direct IDs, or a unique publisher-declared split-chain contract."""
    heavy, light = original["heavy_chain"], original["light_chain"]
    antigen = list(original["antigen_chains"])
    if all(c in available for c in [heavy, light, *antigen]) and heavy != light:
        return heavy, light, antigen, {"kind": "original_chain_ids_present"}
    candidates = []
    for row in current_rows:
        h, l = row["Hchain"], row["Lchain"]
        row_antigen = row["antigen_chain"].split("|")
        prefix_match = h.startswith(heavy) and l.startswith(light)
        original_antigen_retained = set(antigen).issubset(row_antigen)
        split_declared = row["chainsharing_construct"] == "SCFV" and heavy == light
        if prefix_match and original_antigen_retained and split_declared and h != l and all(c in available for c in [h, l, *antigen]):
            candidates.append((h, l, antigen, {"kind": "publisher_current_split_scfv_metadata", "instance": row["INSTANCE"], "current_Hchain": h, "current_Lchain": l, "original_antigen_subset_of_current_row": True}))
    if len(candidates) != 1:
        raise ValueError(f"split-chain contract has {len(candidates)} matching current records")
    return candidates[0]


def parse_chains(path, gemmi):
    structure = gemmi.read_structure(str(path))
    if len(structure) != 1:
        raise ValueError("exactly one coordinate model is required")
    structure.merge_chain_parts()
    parsed, rejected = {}, {}
    for chain in structure[0]:
        residues, unknown = [], False
        for r in chain:
            if r.het_flag != "A":
                continue
            if r.name not in STANDARD:
                unknown = True
                break
            atoms = [a for a in r if a.element.name != "H"]
            if not atoms:
                raise ValueError("standard residue has no non-hydrogen atoms")
            ca = next((a for a in atoms if a.name == "CA"), atoms[0])
            point = (ca.pos.x, ca.pos.y, ca.pos.z)
            residues.append(Residue(r.seqid.num, r.seqid.icode.strip(), r.name, point))
        if unknown:
            rejected[chain.name] = "nonstandard_ATOM_residue"
        elif residues:
            parsed[chain.name] = Chain(chain.name, residues)
    return parsed, rejected


def masked_metadata(chain, bounds):
    start, end = bounds
    if not (0 <= start <= end < len(chain)):
        raise ValueError("invalid CDR index interval")
    keys = [{"number": r.number, "insertion_code": r.insertion} for r in chain.residues]
    if len({(r.number, r.insertion) for r in chain.residues}) != len(keys):
        raise ValueError("duplicate residue numbering within selected chain")
    return {"fv_residue_count": len(chain), "cdrh3_zero_based_inclusive": [start, end], "cdrh3_residue_count": end - start + 1, "fv_numbering": keys, "target_mask": [start <= i <= end for i in range(len(chain))]}


def native_interface_indices(antigen_chains, antibody_chains, numpy):
    """Upstream distance/argpartition operation, including its output ordering."""
    antibody = [numpy.array([r.point for r in c.residues]) for c in antibody_chains if len(c)]
    distances, ids = [], []
    for c in antigen_chains:
        xa = numpy.array([r.point for r in c.residues])
        minima = [numpy.min(numpy.linalg.norm(xa[:, None, :] - xb[None, :, :], axis=-1), axis=1) for xb in antibody]
        if not minima:
            raise ValueError("no antibody coordinates")
        minimum = minima[0] if len(minima) == 1 else numpy.minimum(*minima)
        distances.extend(minimum)
        ids.extend((c.name, i) for i in range(len(minimum)))
    dists = numpy.array(distances)
    topk = min(len(dists), 48)
    if topk == 0:
        raise ValueError("no antigen coordinates")
    selected = numpy.argpartition(-dists, -topk)[-topk:]
    result = {}
    for i in selected:
        name, index = ids[i]
        result.setdefault(name, []).append(index)
    return result


def prepare(root, output):
    root, output = Path(root).resolve(), Path(output).resolve()
    recovered = root / ".local/source_recovery_round2_2026-10-19/rabd_imgt"
    sys.path.insert(0, str(recovered / "python_deps"))
    import gemmi
    import numpy

    roster_path = root / ".local/source_acquisition_2026-10-19/protocols/THUNLP-MT__MEAN/files/summaries/rabd_summary.jsonl"
    if digest(roster_path) != ROSTER_SHA256:
        raise ValueError("original roster hash mismatch")
    roster = [json.loads(line) for line in roster_path.read_text().splitlines()]
    if len(roster) != 60 or len({r["pdb"] for r in roster}) != 60:
        raise ValueError("original roster is not 60 unique entries")
    archive = root / ".local/source_recovery_round2_2026-10-19/structural/source_archives/THUNLP-MT__MEAN.tar.gz"
    with tarfile.open(archive) as tf:
        member = next(m for m in tf.getmembers() if m.name.endswith("/data/pdb_utils.py"))
        source = tf.extractfile(member).read()
    numbering = native_mask_function(source)
    current_path = recovered / "scorer_only/current_sabdab_summary.csv"
    fields = ("INSTANCE", "PDB", "Hchain", "Lchain", "antigen_chain", "chainsharing_construct")
    # Read only source metadata fields; sequence/function/organism columns are unused.
    with current_path.open() as f:
        current = [{k: row[k] for k in fields} for row in csv.DictReader(f)]
    acquired = {r["pdb_id"]: r for r in json.loads((recovered / "manifest.json").read_text())["files"]}
    rows, reference_rows, failures = [], [], []
    for ordinal, original in enumerate(roster):
        pdb = original["pdb"].lower()
        a = acquired[pdb]
        coordinate_path = recovered / a["coordinate_path"]
        if digest(coordinate_path) != a["coordinate_sha256"]:
            raise ValueError(f"coordinate hash mismatch for {pdb}")
        try:
            chains, rejected = parse_chains(coordinate_path, gemmi)
            metadata = [r for r in current if r["PDB"].lower().endswith(pdb)]
            h, l, antigen, mapping = resolve_chains(original, metadata, chains)
            selected, cdr = numbering(SimpleNamespace(heavy_chain=h, light_chain=l), chains, "imgt")
            if h not in selected or l not in selected:
                raise ValueError("numbering did not select both antibody chains")
            heavy = masked_metadata(selected[h], cdr["CDR-H3"])
            interface = native_interface_indices([chains[c] for c in antigen], [selected[h], selected[l]], numpy)
            if sum(map(len, interface.values())) != min(48, sum(len(chains[c]) for c in antigen)):
                raise ValueError("interface index count mismatch")
            rows.append({"task_id": "P40", "case_id": pdb, "source_roster_ordinal": ordinal, "original_chain_contract": original, "current_chain_contract": {"heavy_chain": h, "light_chain": l, "antigen_chains": antigen}, "mapping_evidence": mapping, "numbering": "current_official_IMGT", "heavy_chain": heavy, "light_chain_fv_residue_count": len(selected[l]), "all_six_cdr_indices": {k: list(v) for k, v in cdr.items()}, "antigen_interface_zero_based_indices": interface, "antigen_interface_count": sum(map(len, interface.values())), "unselected_nonstandard_chain_count": len(rejected), "structural_metadata_validation_passed": True, "biological_input_eligibility_reviewed": False, "dispatch_authorized": False})
            reference_rows.append({"case_id": pdb, "full_unmasked_coordinate_path": str(coordinate_path.relative_to(root)), "sha256": a["coordinate_sha256"], "bytes": a["coordinate_bytes"], "role": "scorer_only_full_reference_contains_target_identity_and_coordinates", "historical_publisher_byte_identity_verified": False})
        except (ValueError, AssertionError, KeyError) as e:
            failures.append({"case_id": pdb, "error_type": type(e).__name__, "reason": str(e)})
    save(output / "metadata/current_structure_index.json", {"role": "structural_metadata_only_not_solver_requests", "cases": rows})
    save(output / "scorer_only/reference_coordinate_manifest.json", {"role": "scorer_only_never_send_unmasked_files_to_solver", "cases": reference_rows})
    condition = {"task_id": "P40", "condition_id": "RABD60_CURRENT_OFFICIAL_IMGT_CHAIN_METADATA_V1", "status": "prepared_structural_metadata_not_dispatch_ready", "native_source_commit": "a510ceef282cc24c8f658c14c2bfca10a95c23c0", "numbering_function_sha256": PDB_UTILS_SHA256, "original_roster_sha256": ROSTER_SHA256, "current_chain_metadata_sha256": digest(current_path), "coordinate_source": "current official SAbDab2 IMGT experimental structures acquired October 19", "material_differences": ["Current official coordinates are not certified byte-identical to the paper's processed coordinates.", "Three source scFv chain pairs are mapped using current publisher metadata and retain separate heavy/light chains.", "Original roster order is retained; exact historical processed-test artifact order is not certified.", "Gemmi parses current mmCIF coordinates; the historical implementation used Bio.PDB with PDB files. Historical coordinate rounding, alternate-location selection and tied-neighbour selection are not certified equivalent.", "No cropped AAMFM coordinates are substituted."], "reference_isolation": {"full_unmasked_coordinates": "scorer_only", "emitted_metadata_contains_residue_identity": False, "emitted_metadata_contains_coordinate_values": False, "solver_request_created": False}, "software": {"python": sys.version.split()[0], "gemmi": gemmi.__version__, "numpy": numpy.__version__}, "new_inference_calls": 0, "model_forwards": 0, "training": False}
    save(output / "current_structure_condition.json", condition)
    status = {"task_id": "P40", "stage": "cpu_structural_metadata_preparation_complete" if not failures else "cpu_structural_metadata_preparation_partial", "updated_at_pacific": stamp(), "planned_cases": 60, "coordinate_hashes_verified": 60, "chain_mapping_passed": len(rows), "direct_original_chain_cases": sum(r["mapping_evidence"]["kind"] == "original_chain_ids_present" for r in rows), "publisher_declared_split_chain_cases": sum(r["mapping_evidence"]["kind"] == "publisher_current_split_scfv_metadata" for r in rows), "cdrh3_masks_and_native_numbering_checks_passed": len(rows), "native48_context_indices_prepared": len(rows), "remaining_mapping_cases": [r["case_id"] for r in failures], "failures": failures, "biological_eligibility_review_complete": False, "solver_input_packaging_complete": False, "native_benchmark_dispatch_ready": False, "new_inference_calls": 0, "model_forward_calls": 0, "training": False, "exact_historical_condition_certified": False, "entire_task_unavailable": False, "blockers": ["Independent per-case eligibility review and reference-isolated solver packaging are still required before any dispatch.", "The pinned Qwen text interface does not by itself consume native coordinate tensors; any usable input adapter must be explicitly declared and checked.", "Exact historical processed coordinate bytes and processed test ordering have not been recovered; the available current-structure condition is separately labelled."], "next_concrete_action": "Review case eligibility independently, then implement and validate a solver input adapter that hides target residue identities and target coordinates while retaining permitted geometric context.", "artifacts": {str(p.relative_to(output)): digest(p) for p in [output / "metadata/current_structure_index.json", output / "scorer_only/reference_coordinate_manifest.json", output / "current_structure_condition.json"]}}
    save(output / "status.json", status)
    return status


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    ap.add_argument("--output", type=Path)
    args = ap.parse_args()
    output = args.output or args.root / ".local/catalog_execution_2026-10-20/tasks/P40"
    result = prepare(args.root, output)
    print(json.dumps({k: result[k] for k in ["task_id", "stage", "planned_cases", "chain_mapping_passed", "direct_original_chain_cases", "publisher_declared_split_chain_cases", "remaining_mapping_cases", "new_inference_calls"]}))


if __name__ == "__main__":
    main()
