#!/usr/bin/env python3
"""Acquire pinned public source files and access receipts; never run them."""
import concurrent.futures
import datetime
import hashlib
import json
import pathlib
import urllib.error
import urllib.parse
import urllib.request
from zoneinfo import ZoneInfo

ROOT = pathlib.Path(__file__).resolve().parents[1]
DEST = ROOT / '.local/source_acquisition_2026-10-19/protocols'
HEADERS = {'User-Agent': 'bio-evaluation-source-acquisition/1.0', 'Accept': 'application/vnd.github+json'}


def now():
    return datetime.datetime.now(ZoneInfo('America/Los_Angeles')).isoformat()


def write_json(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + '.tmp')
    tmp.write_text(json.dumps(data, indent=2, sort_keys=True) + '\n')
    tmp.replace(path)


def fetch(url):
    with urllib.request.urlopen(urllib.request.Request(url, headers=HEADERS), timeout=45) as response:
        body = response.read(64 * 1024 * 1024 + 1)
        if len(body) > 64 * 1024 * 1024:
            raise ValueError('Source file exceeds 64 MiB acquisition limit')
        return body


def acquire(item):
    path = DEST / item['relative_path']
    rec = {**item, 'observed_at_pacific': now()}
    try:
        data = path.read_bytes() if path.is_file() else fetch(item['url'])
        git_hash = hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest()
        if item.get('git_blob_sha') and git_hash != item['git_blob_sha']:
            raise ValueError('Git blob checksum mismatch')
        path.parent.mkdir(parents=True, exist_ok=True)
        if not path.is_file():
            tmp = path.with_suffix(path.suffix + '.part')
            tmp.write_bytes(data)
            tmp.replace(path)
        rec.update(status='downloaded_verified' if item.get('git_blob_sha') else 'downloaded_local_hash_only',
                   bytes=len(data), sha256=hashlib.sha256(data).hexdigest(), git_blob_computed=git_hash,
                   publisher_digest_verified=bool(item.get('git_blob_sha')))
    except Exception as error:
        rec.update(status='unavailable', error_type=type(error).__name__)
        if isinstance(error, urllib.error.HTTPError):
            rec['http_status'] = error.code
    return rec


def main():
    DEST.mkdir(parents=True, exist_ok=True)
    manifest = {'started_at_pacific': now(), 'stage': 'acquiring', 'inference_calls': 0,
                'downloaded_source_not_executed': True, 'repositories': [], 'assets': [],
                'gated_terms_accepted': False, 'credentials_read': False}
    # Download source/code and explicit split metadata, never model weights or arbitrary data trees.
    repos = [
        ('microsoft/SFM', lambda p: p.startswith('NatureLM/')),
        ('AMix-Bio/PFArena', lambda p: p.endswith(('.py', '.sh', '.yaml', '.yml', '.toml')) or p.rsplit('/', 1)[-1].lower() in ['readme.md', 'license']),
        ('bowang-lab/BioReason-Pro', lambda p: p.endswith(('.py', '.sh', '.yaml', '.yml', '.toml', '.md', '.txt')) and not p.startswith(('data/', 'datasets/'))),
        ('smiles724/Proteo-R1', lambda p: p.endswith(('.py', '.sh', '.yaml', '.yml', '.toml', '.md', '.txt')) and not p.startswith(('data/', 'datasets/'))),
        ('THUNLP-MT/MEAN', lambda p: p == 'summaries/rabd_summary.jsonl' or p.startswith(('evaluation/', 'data/')) and p.endswith('.py') or p in ['README.md', 'requirements.txt']),
    ]
    items = []
    for repo, select in repos:
        try:
            repo_info = json.loads(fetch('https://api.github.com/repos/' + repo))
            branch = repo_info['default_branch']
            commit = json.loads(fetch('https://api.github.com/repos/' + repo + '/commits/' + urllib.parse.quote(branch, safe='')))['sha']
            tree_url = 'https://api.github.com/repos/' + repo + '/git/trees/' + commit + '?recursive=1'
            raw_tree = fetch(tree_url)
            tree = json.loads(raw_tree)
            if tree.get('truncated'):
                raise ValueError('Truncated repository tree')
            slug = repo.replace('/', '__')
            tree_item = {'relative_path': slug + '/tree.json', 'url': tree_url}
            tree_path = DEST / tree_item['relative_path']
            write_json(tree_path, tree)
            manifest['repositories'].append({'repository': repo, 'commit': commit, 'tree_url': tree_url,
                'tree_sha256': hashlib.sha256(raw_tree).hexdigest(), 'tree_entries': len(tree['tree']), 'truncated': False})
            for entry in tree['tree']:
                path = entry['path']
                if entry['type'] == 'blob' and entry.get('size', 0) < 4 * 1024 * 1024 and select(path):
                    items.append({'repository': repo, 'commit': commit, 'relative_path': slug + '/files/' + path,
                        'url': 'https://raw.githubusercontent.com/' + repo + '/' + commit + '/' + urllib.parse.quote(path, safe='/'),
                        'git_blob_sha': entry['sha']})
        except Exception as error:
            manifest['repositories'].append({'repository': repo, 'status': 'unavailable', 'error_type': type(error).__name__,
                'http_status': error.code if isinstance(error, urllib.error.HTTPError) else None})
        write_json(DEST / 'manifest.json', manifest)
    # An unauthenticated access check only. No gate acceptance, auth token, or private source.
    items.extend([
        {'relative_path': 'PFArena/dataset_metadata.json', 'url': 'https://huggingface.co/api/datasets/AMix-Bio/PFArena'},
        {'relative_path': 'PFArena/dataset_tree.json', 'url': 'https://huggingface.co/api/datasets/AMix-Bio/PFArena/tree/main?recursive=true&limit=1000'},
        {'relative_path': 'PFArena/schema_access.md', 'url': 'https://huggingface.co/datasets/AMix-Bio/PFArena/resolve/5be3973dd45a9d7d33572f016be18f8ef941f2ff/assay_columns.md'},
        {'relative_path': 'NatureLM/publisher_datasets.json', 'url': 'https://huggingface.co/api/datasets?author=microsoft&search=NatureLM&limit=100'},
    ])
    manifest['planned_source_files'] = len(items)
    write_json(DEST / 'manifest.json', manifest)
    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as pool:
        futures = [pool.submit(acquire, item) for item in items]
        for future in concurrent.futures.as_completed(futures):
            manifest['assets'].append(future.result())
            manifest['updated_at_pacific'] = now()
            write_json(DEST / 'manifest.json', manifest)
    manifest['stage'] = 'source_acquisition_terminal'
    manifest['finished_at_pacific'] = now()
    manifest['downloaded_files'] = sum(x['status'].startswith('downloaded') for x in manifest['assets'])
    manifest['downloaded_bytes'] = sum(x.get('bytes', 0) for x in manifest['assets'])
    manifest['unavailable_files'] = sum(x['status'] == 'unavailable' for x in manifest['assets'])
    write_json(DEST / 'manifest.json', manifest)
    print(json.dumps({k: manifest[k] for k in ['stage', 'downloaded_files', 'downloaded_bytes', 'unavailable_files', 'finished_at_pacific']}), flush=True)


if __name__ == '__main__':
    main()
