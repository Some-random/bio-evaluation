"""Selectively acquire and prepare ONLY the complete benign ProteinGym GFP assay."""
from __future__ import annotations

import argparse
from collections import Counter
import csv
import hashlib
import io
import json
import math
from pathlib import Path
import re
import struct
import zlib

ROOT = Path(__file__).resolve().parents[1]
ASSAY = "GFP_AEQVI_Sarkisyan_2016"
VARIANT = "QWEN_CAUSAL_SEQUENCE_LOGLIKELIHOOD_GFP"
EXPECTED_COUNT = 51714
CURRENT_URL = "https://marks.hms.harvard.edu/proteingym/ProteinGym_v1.3/DMS_ProteinGym_substitutions.zip"
DATA = ROOT / "data/catalog_proteingym_gfp/P17"
SOURCE = ROOT / "sources/proteingym_gfp_feasibility_2026-10-15"
AA20 = frozenset("ACDEFGHIKLMNPQRSTVWY")


def sha(data): return hashlib.sha256(data).hexdigest()


def save(path, value):
    path = Path(path); path.parent.mkdir(parents=True, exist_ok=True)
    encoded = json.dumps(value, indent=2, ensure_ascii=False, allow_nan=False) + "\n"
    if path.exists() and path.read_text() != encoded: raise ValueError("Refuse to replace an existing prepared artifact: " + str(path))
    if not path.exists(): path.write_text(encoded)


def range_bytes(session, url, requested, expected_identity=None):
    """Reject ignored ranges before body access; never download a whole archive."""
    headers = {"Range": "bytes=" + requested, "Accept-Encoding": "identity"}
    if expected_identity and expected_identity.get("etag"): headers["If-Match"] = expected_identity["etag"]
    with session.get(url, headers=headers, stream=True, timeout=(20, 60)) as response:
        match = re.fullmatch(r"bytes ([0-9]+)-([0-9]+)/([0-9]+)", response.headers.get("Content-Range", ""))
        if response.status_code != 206 or match is None or response.headers.get("Content-Encoding") not in (None, "identity"):
            raise ValueError("Server did not honor the exact unencoded byte range; response body was not read")
        start, end, total = map(int, match.groups())
        if requested.startswith("-"):
            expected_start, expected_end = max(0, total - int(requested[1:])), total - 1
        else: expected_start, expected_end = map(int, requested.split("-"))
        if (start, end) != (expected_start, expected_end) or end - start + 1 > 8 * 1024 * 1024:
            raise ValueError("Unexpected range bounds or oversized selective member")
        identity = {"url": response.url, "total_bytes": total, "etag": response.headers.get("ETag"), "last_modified": response.headers.get("Last-Modified")}
        if expected_identity and identity != expected_identity: raise ValueError("Remote archive identity changed between selective ranges")
        body = response.raw.read(end - start + 2, decode_content=False)
        if len(body) != end - start + 1: raise ValueError("Incomplete or oversized byte-range response")
        return body, identity


def parse_directory(data, expected_count):
    entries = []; offset = 0
    while offset < len(data):
        if offset + 46 > len(data): raise ValueError("Incomplete ZIP directory record")
        fields = struct.unpack_from("<4s6H3I5H2I", data, offset)
        if fields[0] != b"PK\x01\x02": raise ValueError("Unexpected ZIP directory signature")
        flag, method, crc, compressed, size = fields[3], fields[4], fields[7], fields[8], fields[9]
        n, extra, comment = fields[10:13]
        end = offset + 46 + n + extra + comment
        if end > len(data): raise ValueError("Incomplete ZIP directory name")
        name = data[offset + 46:offset + 46 + n].decode("utf-8" if flag & 2048 else "cp437")
        if size == 0xFFFFFFFF or compressed == 0xFFFFFFFF or fields[16] == 0xFFFFFFFF: raise ValueError("ZIP64 archive needs an explicitly reviewed implementation")
        entries.append({"name": name, "flags": flag, "method": method, "crc32": f"{crc:08x}",
            "compressed_bytes": compressed, "uncompressed_bytes": size, "local_header_offset": fields[16]})
        offset = end
    if len(entries) != expected_count: raise ValueError("ZIP directory entry count differs")
    return entries


def acquire(session, output_directory=DATA, metadata_directory=SOURCE):
    end, identity = range_bytes(session, CURRENT_URL, "-22")
    fields = struct.unpack("<4s4H2IH", end)
    if fields[0] != b"PK\x05\x06" or fields[1] or fields[2] or fields[3] != fields[4] or fields[7]:
        raise ValueError("Only ordinary single-disk ZIP with no end comment is admitted")
    count, directory_size, directory_offset = fields[4], fields[5], fields[6]
    if directory_size > 1024 * 1024 or directory_offset + directory_size + 22 != identity["total_bytes"]:
        raise ValueError("ZIP directory bounds differ from source archive")
    directory, same = range_bytes(session, CURRENT_URL, f"{directory_offset}-{directory_offset + directory_size - 1}", identity)
    entries = parse_directory(directory, count)
    allowed_names = {ASSAY + ".csv", "DMS_ProteinGym_substitutions/" + ASSAY + ".csv"}
    selected = [row for row in entries if row["name"] in allowed_names]
    if len(selected) != 1: raise ValueError("Exact GFP member absent or ambiguous; no other member may be acquired")
    member = selected[0]
    if member["flags"] & 1 or member["method"] not in (0, 8) or member["uncompressed_bytes"] > 32 * 1024 * 1024:
        raise ValueError("Unsupported encrypted/compressed/oversized GFP member")
    start = member["local_header_offset"]
    local, _ = range_bytes(session, CURRENT_URL, f"{start}-{start + 29}", identity)
    header = struct.unpack("<4s5H3I2H", local)
    if header[0] != b"PK\x03\x04" or header[2] != member["flags"] or header[3] != member["method"]:
        raise ValueError("Local GFP header differs from verified central entry")
    name_length, extra_length = header[-2:]
    payload_start = start + 30
    payload_end = payload_start + name_length + extra_length + member["compressed_bytes"] - 1
    payload, _ = range_bytes(session, CURRENT_URL, f"{payload_start}-{payload_end}", identity)
    encoded_name = payload[:name_length].decode("utf-8" if member["flags"] & 2048 else "cp437")
    if encoded_name != member["name"]: raise ValueError("Selected ZIP local filename differs")
    compressed = payload[name_length + extra_length:]
    raw = zlib.decompress(compressed, -15) if member["method"] == 8 else compressed
    if len(raw) != member["uncompressed_bytes"] or f"{zlib.crc32(raw) & 0xFFFFFFFF:08x}" != member["crc32"]:
        raise ValueError("GFP member CRC or byte count differs")
    output_directory = Path(output_directory); output_directory.mkdir(parents=True, exist_ok=True)
    path = output_directory / (ASSAY + ".native.csv")
    if path.exists() and path.read_bytes() != raw: raise ValueError("Existing native GFP member differs")
    if not path.exists(): path.write_bytes(raw)
    metadata_directory = Path(metadata_directory); metadata_directory.mkdir(parents=True, exist_ok=True)
    save(metadata_directory / "current_zip_directory.json", {"archive": identity, "entry_count": count,
        "directory_sha256": sha(directory), "entries": entries, "raw_other_members_acquired": False})
    receipt = {"task_id": "P17", "assay": ASSAY, "release": "v1.3", "source_url": CURRENT_URL,
        "archive": identity, "directory_sha256": sha(directory), "selected_member": member, "native_member_sha256": sha(raw),
        "native_member_file": str(path.relative_to(ROOT)) if path.is_relative_to(ROOT) else str(path),
        "all_range_bytes_sha256": {"eocd": sha(end), "directory": sha(directory), "local_header": sha(local), "GFP_local_name_extra_and_compressed_payload": sha(payload)},
        "only_GFP_member_inflated": True, "other_assay_sequence_or_reference_files_acquired": False,
        "publisher_full_archive_sha256_verified": False, "integrity": "Primary publisher HTTPS ranges, unchanged ETag/size/Last-Modified, exact member path, byte count, ZIP CRC32 and local SHA256. Full archive was never downloaded."}
    save(output_directory / "acquisition.json", receipt)
    return path, receipt


def prepare(native_path, acquisition, output_directory=DATA, expected_count=EXPECTED_COUNT):
    native_path = Path(native_path); output_directory = Path(output_directory)
    raw = native_path.read_bytes()
    if sha(raw) != acquisition["native_member_sha256"] or acquisition["assay"] != ASSAY: raise ValueError("Native GFP source identity differs")
    # First pass uses only source inputs, not fitness labels, to retain every row.
    records = list(csv.DictReader(io.StringIO(raw.decode("utf-8-sig"))))
    if not records or set(records[0]) != {"mutant", "mutated_sequence", "DMS_score", "DMS_score_bin"}:
        raise ValueError("Native processed GFP schema changed")
    inputs = []; mutants = []; sequences = []; source_wildtype = None; depths = Counter()
    for row in records:
        mutant, sequence = row["mutant"], row["mutated_sequence"]
        if not mutant or not sequence or any(aa not in AA20 for aa in sequence): raise ValueError("Incomplete or non-native GFP sequence")
        wildtype = list(sequence); used = set(); components = mutant.split(":")
        for part in components:
            match = re.fullmatch(r"([ACDEFGHIKLMNPQRSTVWY])([1-9][0-9]*)([ACDEFGHIKLMNPQRSTVWY])", part)
            if match is None: raise ValueError("Native substitution key changed")
            original, position, altered = match.groups(); index = int(position) - 1
            if index in used or index >= len(sequence) or sequence[index] != altered or original == altered:
                raise ValueError("Substitution key and full sequence disagree")
            used.add(index); wildtype[index] = original
        reconstructed = "".join(wildtype)
        if source_wildtype is None: source_wildtype = reconstructed
        if reconstructed != source_wildtype: raise ValueError("Native rows do not share the same exact WT backbone")
        inputs.append({"task_id": "P17", "case_id": ASSAY + ":" + mutant, "variant": VARIANT, "sequence": sequence})
        mutants.append(mutant); sequences.append(sequence); depths[len(components)] += 1
    if (len(inputs) != expected_count or len(set(mutants)) != expected_count or len(set(sequences)) != expected_count
            or len({len(sequence) for sequence in sequences}) != 1): raise ValueError("Complete unique native GFP case set/count/length differs")
    encoded_inputs = "".join(json.dumps(row, ensure_ascii=False, separators=(",", ":")) + "\n" for row in inputs).encode()
    # The complete ordered inputs are fixed before any label is read for scoring.
    output_directory.mkdir(parents=True, exist_ok=True)
    path = output_directory / "model_inputs.jsonl"
    if path.exists() and path.read_bytes() != encoded_inputs: raise ValueError("Existing frozen model inputs differ")
    if not path.exists(): path.write_bytes(encoded_inputs)
    references = []
    for row, case in zip(records, inputs):
        fitness = float(row["DMS_score"])
        if not math.isfinite(fitness) or row["DMS_score_bin"] not in {"0", "1"}: raise ValueError("Nonfinite/invalid native scorer label")
        references.append({"case_id": case["case_id"], "fitness": fitness})
    encoded_references = "".join(json.dumps(row, ensure_ascii=False, separators=(",", ":"), allow_nan=False) + "\n" for row in references).encode()
    path = output_directory / "scorer_reference.jsonl"
    if path.exists() and path.read_bytes() != encoded_references: raise ValueError("Existing frozen scorer references differ")
    if not path.exists(): path.write_bytes(encoded_references)
    contract = {"task_id": "P17", "assay": ASSAY, "variant": VARIANT, "release": "ProteinGym_v1.3",
        "scope": "complete_single_native_GFP_assay_component_only", "native_all_assays_completed": False,
        "planned_case_count": len(inputs), "native_source_case_order_preserved": True, "unique_mutant_keys": len(set(mutants)),
        "unique_complete_variant_sequences": len(set(sequences)), "duplicate_mutant_or_sequence_rows_removed": 0,
        "sequence_length_distribution": dict(Counter(map(len, sequences))), "mutation_depth_distribution": dict(sorted(depths.items())),
        "native_member_sha256": sha(raw), "model_inputs_file": "data/catalog_proteingym_gfp/P17/model_inputs.jsonl",
        "model_inputs_sha256": sha(encoded_inputs), "scorer_reference_file": "data/catalog_proteingym_gfp/P17/scorer_reference.jsonl",
        "scorer_reference_sha256": sha(encoded_references), "ordered_case_ids_sha256": sha(json.dumps([row["case_id"] for row in inputs], separators=(",", ":")).encode()),
        "backbone_reconstructed_from_source_input_annotations_only": True, "backbone_sha256": sha(source_wildtype.encode()),
        "backbone_sequence_length": len(source_wildtype), "backbone_supplied_to_solver": False,
        "source_raw_score_field": "DMS_score", "higher_native_score_means": "higher fluorescent-reporter activity / fitness under this assay",
        "raw_directionality_inversion_needed": False, "primary_metric": "Spearman rank correlation over all native rows",
        "metric_unit": "correlation coefficient -1..1", "invalid_missing_prediction_policy": "Any missing/nonfinite prediction makes full-assay primary Spearman undefined; no case dropping or zero imputation.",
        "scoring_is_offline_after_prediction_lock": True, "label_fields_available_to_solver": [],
        "experimental_labels_used_for_input_selection_or_partition": False, "source_input_scope_review": "Benign GFP fluorescent-reporter activity, exact complete public assay; no other raw assay or broad WT reference acquired.",
        "prospective_solver_score": "Qwen fixed-prefix full-sequence causal loglikelihood of every actual variant token, no EOS, token-length normalization or WT centering; distinct from trained ProtST masked/protein representations.",
        "explanation_support_score": None, "native_paper_replication": False, "execution_authorized": False}
    save(output_directory / "native_contract.json", contract)
    return contract


def main():
    parser = argparse.ArgumentParser(description=__doc__); parser.add_argument("--acquire", action="store_true"); parser.add_argument("--prepare", action="store_true")
    args = parser.parse_args()
    if args.acquire:
        import requests
        acquire(requests.Session())
    if args.prepare:
        contract = prepare(DATA / (ASSAY + ".native.csv"), json.loads((DATA / "acquisition.json").read_text()))
        print(json.dumps({key: contract[key] for key in ["assay", "planned_case_count", "sequence_length_distribution", "model_inputs_sha256", "scorer_reference_sha256"]}))
    if not args.acquire and not args.prepare: parser.error("Choose --acquire and/or --prepare; no inference is implemented")


if __name__ == "__main__": main()
