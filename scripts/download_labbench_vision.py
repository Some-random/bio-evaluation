"""Fetch pinned native LAB-Bench image data without changing any frozen inputs."""
import datetime as dt
import hashlib
import json
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[1]


def main():
    metadata = json.loads((ROOT / "reports/labbench_vision_source_metadata.json").read_text())
    outcomes = []
    for item in metadata["files"]:
        subset = item["subset"]
        if item.get("status") != 200 or len(item.get("files", [])) != 1:
            outcomes.append({"subset": subset, "state": "metadata_unavailable"})
            continue
        source = item["files"][0]
        expected = source["lfs"]["oid"]
        target = ROOT / "sources" / f"lab_data__{subset}__train-00000-of-00001.parquet"
        partial = target.with_suffix(target.suffix + ".download")
        url = f"https://huggingface.co/datasets/futurehouse/lab-bench/resolve/{metadata['revision']}/{source['path']}"
        if target.exists():
            candidate = target
        else:
            candidate = partial
            for attempt in range(1, 5):
                result = subprocess.run(["curl", "--fail", "--location", "--continue-at", "-",
                    "--silent", "--show-error", "--connect-timeout", "10", "--max-time", "55",
                    "--retry", "0", "--output", str(partial), url],
                    stdout=subprocess.DEVNULL, stderr=subprocess.PIPE, text=True)
                size = partial.stat().st_size if partial.exists() else 0
                print(json.dumps({"subset": subset, "attempt": attempt,
                                  "bytes": size, "expected_bytes": source["size"],
                                  "curl_exit_code": result.returncode}), flush=True)
                if size == source["size"]:
                    break
        if not candidate.exists() or candidate.stat().st_size != source["size"]:
            outcomes.append({"subset": subset, "state": "incomplete", "path": str(candidate),
                             "bytes": candidate.stat().st_size if candidate.exists() else 0,
                             "expected_bytes": source["size"]})
            continue
        hasher = hashlib.sha256()
        with candidate.open("rb") as handle:
            while block := handle.read(8 * 1024 * 1024):
                hasher.update(block)
        if hasher.hexdigest() != expected:
            outcomes.append({"subset": subset, "state": "sha256_mismatch"})
            continue
        if candidate != target:
            candidate.replace(target)
        outcomes.append({"subset": subset, "state": "verified", "path": str(target),
                         "bytes": source["size"], "sha256": expected, "url": url})
    report = {"checked_at_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
              "revision": metadata["revision"], "outcomes": outcomes,
              "frozen_benchmark_inputs_modified": False, "model_cases_dispatched": 0}
    (ROOT / "reports/labbench_vision_data_verification.json").write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report), flush=True)


if __name__ == "__main__":
    main()
