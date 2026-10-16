import concurrent.futures, datetime, hashlib, html.parser, json, pathlib, urllib.parse, urllib.request
ROOT=pathlib.Path(__file__).resolve().parent
previous=json.loads((ROOT/"v06_image_acquisition.json").read_text())
class Images(html.parser.HTMLParser):
    def __init__(self): super().__init__(); self.urls=[]
    def handle_starttag(self,tag,attrs):
        data=dict(attrs)
        if tag=="img" and "src" in data: self.urls.append(data["src"])
        if tag=="a" and "href" in data: self.urls.append(data["href"])
def fetch(url,limit):
    with urllib.request.urlopen(urllib.request.Request(url,headers={"User-Agent":"bio-evaluation-public-source-recovery/1.0"}),timeout=35) as response:
        raw=response.read(limit+1)
        if len(raw)>limit: raise ValueError("Bounded acquisition size exceeded")
        return raw
def recover(old):
    row=dict(old)
    pmc_id=pathlib.PurePosixPath(row["image_file_path"]).parts[0]
    image_basename=pathlib.PurePosixPath(row["image_file_path"]).name
    page_url="https://pmc.ncbi.nlm.nih.gov/articles/"+pmc_id+"/"
    row["original_package_acquisition"]={k:old[k] for k in ["status","error_type","error"] if k in old}
    try:
        page=fetch(page_url,2000000)
        page_path=ROOT/"sources/llava_main/pmc_pages"/(pmc_id+".html")
        page_path.parent.mkdir(parents=True,exist_ok=True)
        page_path.write_bytes(page)
        parser=Images();parser.feed(page.decode("utf-8"))
        candidates=sorted(set(urllib.parse.urljoin(page_url,url) for url in parser.urls if urllib.parse.urlparse(url).netloc=="cdn.ncbi.nlm.nih.gov" and pathlib.PurePosixPath(urllib.parse.urlparse(url).path).name==image_basename))
        if len(candidates)!=1: raise ValueError("Exact source filename URL count is "+str(len(candidates)))
        raw=fetch(candidates[0],16*1024*1024)
        if not raw.startswith((b"\xff\xd8\xff",b"\x89PNG\r\n\x1a\n")):raise ValueError("Native image is neither JPEG nor PNG")
        destination=ROOT/"data/V06/images"/(row["pair_id"]+".jpg")
        destination.parent.mkdir(parents=True,exist_ok=True)
        if destination.exists() and destination.read_bytes()!=raw: raise ValueError("Refusing image overwrite")
        destination.write_bytes(raw)
        for key in ["error_type","error"]:row.pop(key,None)
        row.update(status="recovered_from_exact_original_pmc_image_filename",image_path=str(destination.relative_to(ROOT)),image_url=candidates[0],image_bytes=len(raw),image_sha256=hashlib.sha256(raw).hexdigest(),pmc_page_url=page_url,pmc_page_path=str(page_path.relative_to(ROOT)),pmc_page_sha256=hashlib.sha256(page).hexdigest(),exact_article_id_and_filename_matched=True,historical_publisher_image_digest_verified=False)
    except Exception as error:row.update(status="blocked",error_type=type(error).__name__,error=str(error),pmc_page_url=page_url)
    return row
results=[]
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
    for row in executor.map(recover,previous["images"]):
        results.append(row)
        print(row["pair_id"],row["status"],row.get("image_bytes",row.get("error","")),flush=True)
        (ROOT/"v06_image_recovery.json").write_text(json.dumps({"created_at_utc":datetime.datetime.now(datetime.timezone.utc).isoformat(),"source_manifest":"sources/llava_main/data/llava_med_test_image_urls.jsonl","current_pmc_assets_not_publisher_historical_hash_verified":True,"inference_performed":False,"attempted":len(results),"recovered":sum(x["status"].startswith("recovered") for x in results),"images":results},indent=2)+"\n")
