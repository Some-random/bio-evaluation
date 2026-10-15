"""Cache public source metadata/docs without model calls or credentials."""
import concurrent.futures
import hashlib
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
URLS = {
    "pg_release.json": "https://api.github.com/repos/rohitarorayyc/proteingym-llm/releases/tags/eval-data-v1.2",
    "pg_tree.json": "https://api.github.com/repos/rohitarorayyc/proteingym-llm/git/trees/main?recursive=1",
    "pg_DATA.md": "https://raw.githubusercontent.com/rohitarorayyc/proteingym-llm/main/DATA.md",
    "pg_README.md": "https://raw.githubusercontent.com/rohitarorayyc/proteingym-llm/main/README.md",
    "mol_tree.json": "https://api.github.com/repos/zjunlp/Mol-Instructions/git/trees/main?recursive=1",
    "biot5_tree.json": "https://api.github.com/repos/QizhiPei/BioT5/git/trees/main?recursive=1",
    "muta_tree.json": "https://api.github.com/repos/PharMolix/MutaPLM/git/trees/main?recursive=1",
    "muta_hf.json": "https://huggingface.co/api/datasets/PharMolix/MutaDescribe",
    "muta_files.json": "https://huggingface.co/api/datasets/PharMolix/MutaDescribe/tree/main?recursive=true",
    "openai_pricing.md": "https://developers.openai.com/api/docs/pricing.md",
    "openai_luna.md": "https://developers.openai.com/api/docs/models/gpt-6-luna.md",
    "openai_token_counting.md": "https://developers.openai.com/api/docs/guides/token-counting.md",
}

def fetch(item):
    name, url = item
    path = ROOT / "sources" / name
    if path.exists():
        return {"file": name, "url": url, "cached": True, "bytes": path.stat().st_size,
                "sha256": hashlib.sha256(path.read_bytes()).hexdigest()}
    temporary = path.with_suffix(path.suffix + ".part")
    run = subprocess.run(["curl", "--fail", "--location", "--silent", "--show-error",
                          "--max-time", "45", "--output", str(temporary), url],
                         capture_output=True, text=True)
    if run.returncode:
        temporary.unlink(missing_ok=True)
        return {"file": name, "url": url, "error": run.stderr.strip()}
    temporary.replace(path)
    return {"file": name, "url": url, "bytes": path.stat().st_size,
            "sha256": hashlib.sha256(path.read_bytes()).hexdigest()}

if __name__ == "__main__":
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        records = list(pool.map(fetch, URLS.items()))
    (ROOT / "sources" / "source_fetch_manifest.json").write_text(
        json.dumps(records, indent=2) + "\n")
    for record in records:
        print(json.dumps(record))
