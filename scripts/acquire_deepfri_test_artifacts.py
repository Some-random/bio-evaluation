#!/usr/bin/env python3
"""Acquire only native DeepFRI test ZIP members via verified HTTP byte ranges.

The parent archives also contain large training/validation structures. This
utility never fetches those members and does not run models or make requests
to model providers. Previously saved archive indexes pin offsets and CRCs.
"""
import argparse
import hashlib
import json
import pathlib
import struct
import urllib.request
import zlib


def fetch_range(url, start, size, total):
    end = start + size - 1
    request = urllib.request.Request(
        url + f"?deepfri_test_range={start}-{end}",
        headers={"Range": f"bytes={start}-{end}"},
    )
    with urllib.request.urlopen(request, timeout=180) as response:
        if response.status != 206 or response.headers.get("Content-Range") != f"bytes {start}-{end}/{total}":
            raise ValueError("Server did not honor the exact bounded range")
        data = response.read(size + 1)
        if len(data) != size:
            raise ValueError("Incorrect range body length")
    return data


def acquire(directory, name, chunk_size=8 * 1024 * 1024):
    index_path = directory / (name + ".zip.index.json")
    index = json.loads(index_path.read_text())
    member = next(item for item in index["files"] if item["filename"] == name + "/test.zip")
    if member["compression"] != 0 or member["compressed_size"] != member["file_size"]:
        raise ValueError("Selective nested acquisition requires a stored test ZIP")
    header = fetch_range(index["url"], member["local_header_offset"], 30, index["size"])
    fields = struct.unpack("<4s5H3L2H", header)
    if fields[0] != b"PK\x03\x04" or fields[3] != 0:
        raise ValueError("Stored-member local header mismatch")
    data_start = member["local_header_offset"] + 30 + fields[-2] + fields[-1]
    output = directory / (name + ".test.zip")
    partial = output.with_suffix(output.suffix + ".partial")
    if not output.exists():
        offset = partial.stat().st_size if partial.exists() else 0
        if offset > member["file_size"]:
            raise ValueError("Partial artifact exceeds frozen member size")
        with partial.open("ab") as stream:
            while offset < member["file_size"]:
                count = min(chunk_size, member["file_size"] - offset)
                data = fetch_range(index["url"], data_start + offset, count, index["size"])
                stream.write(data)
                stream.flush()
                offset += count
                print(json.dumps({"artifact": output.name, "bytes": offset, "total": member["file_size"]}), flush=True)
        partial.rename(output)
    crc = 0
    digest = hashlib.sha256()
    count = 0
    with output.open("rb") as stream:
        while data := stream.read(chunk_size):
            crc = zlib.crc32(data, crc)
            digest.update(data)
            count += len(data)
    if count != member["file_size"] or crc != member["crc32"]:
        raise ValueError("Acquired nested ZIP fails publisher-container size/CRC")
    metadata = {
        "artifact": str(output), "sha256": digest.hexdigest(), "bytes": count,
        "crc32": f"{crc:08x}", "source_url": index["url"],
        "parent_archive_bytes": index["size"], "parent_member": member["filename"],
        "parent_member_data_offset": data_start,
        "parent_archive_index_sha256": hashlib.sha256(index_path.read_bytes()).hexdigest(),
        "integrity_qualification": "Member CRC/size and bounded ranges verified; complete parent archive MD5 not verified because training/validation members were not downloaded.",
        "no_training_or_validation_structures_acquired": True,
    }
    output.with_suffix(output.suffix + ".provenance.json").write_text(json.dumps(metadata, indent=2) + "\n")
    return metadata


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--directory", type=pathlib.Path, default=pathlib.Path("sources/deepfri_contract_audit_2026-10-15"))
    parser.add_argument("--dataset", choices=["EnzymeCommission", "GeneOntology", "all"], default="all")
    args = parser.parse_args()
    for name in (["EnzymeCommission", "GeneOntology"] if args.dataset == "all" else [args.dataset]):
        print(json.dumps(acquire(args.directory, name)), flush=True)


if __name__ == "__main__":
    main()
