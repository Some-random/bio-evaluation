"""Acquire only images required by the source-defined PMC-VQA clean2000 test.

Pinned publisher ZIP ranges/CRCs/image hashes are recorded; this does not claim
verification of the entire19GB archive's SHA256. No inference or label selection.
"""
import concurrent.futures as cf
import csv
import hashlib
import json
from pathlib import Path
import struct
import threading
import time
import zipfile
import zlib

import requests
from http_range_zip import HTTPRangeFile

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "sources/pmcvqa_native"
OUTPUT = ROOT / "data/pmcvqa_clean_native/images"
REVISION = "b56ae594f794867893143b337b4118a835794647"
URL = f"https://huggingface.co/datasets/xmcmic/PMC-VQA/resolve/{REVISION}/images.zip"
ARCHIVE_SIZE = 18945102275
ARCHIVE_PUBLISHER_SHA256 = "cc9f909d6804d0b58111ec8aa7c7b564eece237f24fdcb701916c47beec8285e"
CSV_SHA256 = "8523073108666b8f5231c3d40004a7b74a57381ea54ec9a3019edf1b33eab8f7"
THREAD_LOCAL = threading.local()


class ResponseView:
    def __init__(self, response):
        self.response = response
        self.status, self.headers = response.status_code, response.headers

    def read(self, amount):
        return self.response.raw.read(amount)

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.response.close()


def opener(request, timeout):
    if not hasattr(THREAD_LOCAL, "session"):
        THREAD_LOCAL.session = requests.Session()
    return ResponseView(THREAD_LOCAL.session.get(request.full_url, headers=dict(request.header_items()), stream=True, timeout=timeout))


def remote_file():
    return HTTPRangeFile(URL, ARCHIVE_SIZE, cache_bust_parameter="_bio_eval_range",
                         max_read_bytes=64 * 1024**2, timeout=90, opener=opener)


def save_json(path, value):
    tmp = path.with_suffix(".tmp")
    tmp.write_text(json.dumps(value, indent=2) + "\n")
    tmp.replace(path)


def acquire():
    raw = (SOURCE / "test_clean.csv").read_bytes()
    if hashlib.sha256(raw).hexdigest() != CSV_SHA256:
        raise ValueError("Frozen full clean test changed")
    rows = list(csv.DictReader(raw.decode().splitlines()))
    names = sorted({row["Figure_path"] for row in rows})
    if len(rows) != 2000 or len(names) != 1440:
        raise ValueError("Original clean test identity count changed")
    OUTPUT.mkdir(parents=True, exist_ok=True)
    metadata_path = SOURCE / "selected_image_zip_metadata.json"
    metadata_ranges = []
    if metadata_path.exists():
        metadata = json.loads(metadata_path.read_text())
    else:
        remote = remote_file()
        with zipfile.ZipFile(remote) as archive:
            entries = {Path(info.filename).name: info for info in archive.infolist() if not info.is_dir()}
            missing = set(names) - set(entries)
            if missing:
                raise ValueError("Required clean images absent from original archive")
            metadata = {name: {key: getattr(entries[name], key) for key in ["filename", "header_offset", "compress_size", "file_size", "CRC", "compress_type", "flag_bits"]} for name in names}
        metadata_ranges = remote.acquired_ranges
        save_json(metadata_path, metadata)
        save_json(SOURCE / "zip_metadata_acquired_ranges.json", metadata_ranges)
    if set(metadata) != set(names):
        raise ValueError("Source-order image selection changed")
    records_path = SOURCE / "clean_image_acquisition.jsonl"
    existing = {row["image_name"]: row for row in map(json.loads, records_path.read_text().splitlines())} if records_path.exists() else {}
    pending = []
    for name in names:
        if name in existing:
            path = OUTPUT / name
            if not path.exists() or hashlib.sha256(path.read_bytes()).hexdigest() != existing[name]["sha256"]:
                raise ValueError("Already acquired original image changed")
        else:
            pending.append(name)

    def fetch(name):
        info = metadata[name]
        for attempt in range(3):
            try:
                remote = remote_file()
                remote.seek(info["header_offset"])
                # One bounded range per JPEG includes its variable local header.
                raw = remote.read(min(info["compress_size"] + 2048, ARCHIVE_SIZE-info["header_offset"]))
                fields = struct.unpack_from("<4s5H3L2H", raw)
                start = 30 + fields[-2] + fields[-1]
                if fields[0] != b"PK\x03\x04" or fields[3] != info["compress_type"]:
                    raise ValueError("ZIP local header method/identity mismatch")
                encoding = "utf-8" if info["flag_bits"] & 0x800 else "cp437"
                if raw[30:30+fields[-2]].decode(encoding) != info["filename"]:
                    raise ValueError("ZIP local filename mismatch")
                compressed = raw[start:start+info["compress_size"]]
                if len(compressed) != info["compress_size"]:
                    raise ValueError("Local header exceeds acquisition bound")
                if info["compress_type"] == zipfile.ZIP_STORED:
                    data = compressed
                elif info["compress_type"] == zipfile.ZIP_DEFLATED:
                    data = zlib.decompress(compressed, -15)
                else:
                    raise ValueError("Unsupported original JPEG compression method")
                if len(data) != info["file_size"] or zlib.crc32(data) & 0xffffffff != info["CRC"] or not data.startswith(b"\xff\xd8\xff"):
                    raise ValueError("Original image CRC/length/JPEG signature mismatch")
                path = OUTPUT / name
                tmp = path.with_suffix(".download")
                tmp.write_bytes(data)
                tmp.replace(path)
                return {"image_name": name, "sha256": hashlib.sha256(data).hexdigest(), "bytes": len(data),
                    "publisher_archive_member": info["filename"], "source_ranges": remote.acquired_ranges,
                    "publisher_zip_crc32": info["CRC"], "attempts": attempt+1}
            except (requests.RequestException, OSError, ValueError, zlib.error):
                if attempt == 2:
                    raise
                time.sleep(2)

    completed = len(existing)
    with records_path.open("a") as journal, cf.ThreadPoolExecutor(max_workers=2) as pool:
        futures = {pool.submit(fetch, name): name for name in pending}
        for future in cf.as_completed(futures):
            record = future.result()
            journal.write(json.dumps(record) + "\n")
            journal.flush()
            completed += 1
            if completed % 25 == 0 or completed == len(names):
                save_json(ROOT / "reports/pmcvqa_clean_image_acquisition.json", {
                    "stage": "complete" if completed == len(names) else "acquiring_original_images",
                    "required_images": len(names), "completed_images": completed,
                    "source_revision": REVISION, "source_archive_bytes": ARCHIVE_SIZE,
                    "publisher_full_archive_sha256_expected": ARCHIVE_PUBLISHER_SHA256,
                    "full_archive_sha256_verified": False,
                    "integrity": "Exact HTTP206ranges, pinned publisher ZIP member/CRC, per-range/image SHA256; full archive not downloaded.",
                    "inference_dispatched": False})
                print(json.dumps({"completed_images": completed, "required_images": len(names)}), flush=True)


if __name__ == "__main__":
    acquire()
