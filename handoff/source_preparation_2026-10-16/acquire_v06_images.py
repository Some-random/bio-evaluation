import concurrent.futures, datetime, hashlib, io, json, pathlib, tarfile, urllib.request
ROOT=pathlib.Path(__file__).resolve().parent
rows=[json.loads(line) for line in (ROOT/"sources/llava_main/data/llava_med_test_image_urls.jsonl").read_text().splitlines()]
results=[]
MAX_PACKAGE=32*1024*1024
MAX_IMAGE=16*1024*1024

def get_image(row):
    result={**row,"checked_at_utc":datetime.datetime.now(datetime.timezone.utc).isoformat()}
    destination=ROOT/"data/V06/images"/(row["pair_id"]+".jpg")
    try:
        if destination.exists():
            raw=destination.read_bytes()
            result.update(status="recovered",bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest(),image_path=str(destination.relative_to(ROOT)),reused=True)
            return result
        with urllib.request.urlopen(urllib.request.Request(row["pmc_tar_url"],headers={"User-Agent":"bio-evaluation-public-source-recovery/1.0"}),timeout=35) as response:
            body=response.read(MAX_PACKAGE+1)
            if len(body)>MAX_PACKAGE: raise ValueError("PMC archive exceeds bounded acquisition limit")
            result["pmc_archive_sha256"]=hashlib.sha256(body).hexdigest()
            result["pmc_archive_bytes"]=len(body)
            result["http_status"]=response.status
        with tarfile.open(fileobj=io.BytesIO(body),mode="r:gz") as archive:
            member=archive.getmember(row["image_file_path"])
            if not member.isfile() or member.size>MAX_IMAGE: raise ValueError("Source image not a permitted regular file")
            raw=archive.extractfile(member).read(MAX_IMAGE+1)
        if not raw.startswith((b"\xff\xd8\xff",b"\x89PNG\r\n\x1a\n")): raise ValueError("Source image is neither native JPEG nor PNG")
        destination.parent.mkdir(parents=True,exist_ok=True)
        destination.write_bytes(raw)
        result.update(status="recovered",bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest(),image_path=str(destination.relative_to(ROOT)))
    except Exception as error:
        result.update(status="blocked",error_type=type(error).__name__,error=str(error))
    return result

with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
    for result in executor.map(get_image,rows):
        results.append(result)
        print(result["pair_id"],result["status"],result.get("bytes",result.get("error","")),flush=True)
        (ROOT/"v06_image_acquisition.json").write_text(json.dumps({"created_at_utc":datetime.datetime.now(datetime.timezone.utc).isoformat(),"source_manifest":"sources/llava_main/data/llava_med_test_image_urls.jsonl","current_pmc_assets_not_publisher_historical_hash_verified":True,"inference_performed":False,"attempted":len(results),"recovered":sum(x["status"]=="recovered" for x in results),"images":results},indent=2)+"\n")
