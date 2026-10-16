"""Acquire only identified public evaluator assets; never run an oracle or solver."""
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import zipfile

ROOT=Path(__file__).resolve().parents[1]
SOURCE=ROOT/"sources/proxy_generation_native"


def sha(path):
    h=hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda:f.read(1024*1024),b""):h.update(chunk)
    return h.hexdigest()


def report(value):
    p=ROOT/"reports/proxy_oracle_acquisition.json";tmp=p.with_suffix(".tmp");tmp.write_text(json.dumps(value,indent=2)+"\n");tmp.replace(p)
    print(json.dumps({k:v for k,v in value.items() if k!="assets"}),flush=True)


def acquire_heads():
    from http_range_zip import HTTPRangeFile
    from acquire_pmcvqa_clean_images import opener
    meta=json.loads((SOURCE/"pex_landscape_zip_metadata.json").read_text())
    allowed={"AMIE","avGFP","E4B","LGK","UBE2I"}
    remote=HTTPRangeFile(meta["source_url"],meta["archive_bytes"],cache_bust_parameter="_proxy_evaluator_range",max_read_bytes=64*1024**2,timeout=90,opener=opener)
    records=[]
    with zipfile.ZipFile(remote) as archive:
        for task in sorted(allowed):
            for name in ["decoder.pt","starting_sequence.json"]:
                member=f"landscape_params/esm1b_landscape/{task}/{name}";info=archive.getinfo(member)
                target=ROOT/(f"models/proxy_generation_native/pex_esm1b_heads/{task}/{name}" if name.endswith(".pt") else f"data/proxy_generation_native/P34/{task}/{name}")
                target.parent.mkdir(parents=True,exist_ok=True)
                if not target.exists():
                    raw=archive.read(member);tmp=target.with_suffix(target.suffix+".download");tmp.write_bytes(raw);tmp.replace(target)
                # ZIP CRC verifies both newly acquired and resumed local members.
                import zlib
                if target.stat().st_size!=info.file_size or zlib.crc32(target.read_bytes())&0xffffffff!=info.CRC:raise ValueError("Original PEX member CRC/length mismatch")
                records.append({"task_id":"P34","landscape":task,"path":str(target.relative_to(ROOT)),"sha256":sha(target),"bytes":target.stat().st_size,
                    "publisher_archive_member":member,"publisher_zip_crc32":info.CRC,"whole_archive_sha256_verified":False})
    record={"source_url":meta["source_url"],"archive_bytes":meta["archive_bytes"],"acquired_ranges":remote.acquired_ranges,"assets":records,"AAV_held":True,"inference_dispatched":False}
    (SOURCE/"pex_selected_assets_receipt.json").write_text(json.dumps(record,indent=2)+"\n")
    return records


def acquire():
    assets=acquire_heads();plan=json.loads((SOURCE/"necessary_oracle_assets_plan.json").read_text())["assets"]
    for entry in plan:
        path=ROOT/entry["target"];path.parent.mkdir(parents=True,exist_ok=True)
        report({"stage":"acquiring_public_frozen_evaluator","current_file":entry["target"],"inference_dispatched":False,"assets":assets})
        if not path.exists():
            temporary=path.with_suffix(path.suffix+".download")
            result=subprocess.run(["curl","-fLsS","-C","-","--retry","2","--max-time","1800",entry["url"],"-o",str(temporary)])
            if result.returncode:raise RuntimeError("Public evaluator transfer failed; resumable partial remains: "+entry["target"])
            if temporary.stat().st_size!=entry["bytes"]:raise ValueError("Evaluator publisher size mismatch")
            temporary.replace(path)
        actual=sha(path)
        if entry["sha256"]:
            if actual!=entry["sha256"]:raise ValueError("Evaluator publisher LFS SHA256 mismatch")
        else:
            raw=path.read_bytes()
            if hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()!=entry["git_blob_sha1"]:raise ValueError("Evaluator publisher Git blob mismatch")
        assets.append({**entry,"sha256":actual,"publisher_digest_verified":True})
    report({"stage":"complete_public_evaluator_assets","inference_dispatched":False,"assets":assets})


if __name__=="__main__":
    try:acquire()
    except Exception as exc:
        report({"stage":"acquisition_failed_resumable","error":str(exc),"inference_dispatched":False});raise
