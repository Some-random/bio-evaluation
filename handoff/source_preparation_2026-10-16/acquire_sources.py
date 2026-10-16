import concurrent.futures, datetime, hashlib, json, pathlib, urllib.request
ROOT=pathlib.Path(__file__).resolve().parent
entries=[]
def fetch(path,url,expected_blob=None):
    out=ROOT/path
    out.parent.mkdir(parents=True,exist_ok=True)
    with urllib.request.urlopen(urllib.request.Request(url,headers={"User-Agent":"bio-evaluation-source-audit"}),timeout=60) as response:
        raw=response.read(5000000)
        if len(raw)>=5000000: raise ValueError("Metadata asset too large")
        status=response.status
    blob=hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\x00"+raw).hexdigest()
    if expected_blob and expected_blob!=blob: raise ValueError("Git blob hash mismatch "+path)
    publisher_lfs_sha256=None
    if raw.startswith(b"version https://git-lfs.github.com/spec/v1\n"):
        pointer=raw
        fields=dict(line.split(" ",1) for line in raw.decode().splitlines()[1:])
        publisher_lfs_sha256=fields["oid"].removeprefix("sha256:")
        resolved=url.replace("raw.githubusercontent.com/","media.githubusercontent.com/media/")
        with urllib.request.urlopen(urllib.request.Request(resolved,headers={"User-Agent":"bio-evaluation-source-audit"}),timeout=60) as response:
            raw=response.read(5000000)
        if len(raw)!=int(fields["size"]) or hashlib.sha256(raw).hexdigest()!=publisher_lfs_sha256: raise ValueError("LFS payload digest mismatch")
        out.with_suffix(out.suffix+".lfs-pointer").write_bytes(pointer)
        if out.exists() and out.read_bytes()==pointer: out.unlink()
    if out.exists() and out.read_bytes()!=raw: raise ValueError("Refusing overwrite changed source "+path)
    out.write_bytes(raw)
    entry={"path":path,"url":url,"bytes":len(raw),"sha256":hashlib.sha256(raw).hexdigest(),"git_blob_sha1":blob,"publisher_blob_verified":bool(expected_blob),"http_status":status,"publisher_lfs_sha256":publisher_lfs_sha256}
    entries.append(entry)
    return json.loads(raw) if path.endswith("git_tree.json") else raw
repos={"llava_main":("microsoft/LLaVA-Med","30697ca50b5c29a8e955c99330b259776aef27b9"),"llava_v1":("microsoft/LLaVA-Med","b9a98a736d2ef05bcf5ff345be6403fb3a664eaf"),"ryze":("Chivier/Ryze","41b2d77ec0651b9f51b657f524415ee3cc38e115"),"naturelm":("microsoft/SFM","bcb1351bc6490d4a98cae74e7eead30a028fae00")}
for key,(repo,rev) in repos.items():
    tree=fetch("sources/"+key+"/git_tree.json",f"https://api.github.com/repos/{repo}/git/trees/{rev}?recursive=1")
    if tree.get("truncated"): raise ValueError("Truncated source tree")
    choices=[]
    for item in tree["tree"]:
        remote=item["path"]
        if item["type"]!="blob": continue
        if key.startswith("llava"):
            selected=remote in ["README.md","LICENSE","llava/data/download_images.py","llava/eval/eval_multimodal_chat_gpt_score.py","llava/eval/summarize_gpt_review.py","llava/eval/llm.py","llava/eval/model_vqa.py","data/llava_med_test_image_urls.jsonl"] or ("qa50" in remote and "eval" in remote)
        elif key=="ryze":
            selected=remote in ["LICENSE","README.md","src/ryze/eval/benchmark.py","src/ryze/eval/evaluator.py","src/ryze/eval/metrics.py","src/ryze/data/ocr.py"]
        else:
            selected=remote=="LICENSE" or (remote.startswith("NatureLM/") and (remote.endswith(".md") or remote.endswith(".ipynb")))
        if selected and item.get("size",0)<5000000:
            choices.append(("sources/"+key+"/"+remote,f"https://raw.githubusercontent.com/{repo}/{rev}/{remote}",item["sha"]))
    with concurrent.futures.ThreadPoolExecutor(max_workers=6) as executor:
        for value in executor.map(lambda values:fetch(*values),choices): pass
    print(key,rev,len(choices),flush=True)
(ROOT/"source_manifest.json").write_text(json.dumps({"created_at_utc":datetime.datetime.now(datetime.timezone.utc).isoformat(),"repository_pins":repos,"artifacts":sorted(entries,key=lambda x:x["path"]),"inference_performed":False,"provider_keys_read":False},indent=2)+"\n")
