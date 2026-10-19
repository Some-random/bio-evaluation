#!/usr/bin/env python3
"""Download public official checkpoints as opaque files, without loading them."""
import concurrent.futures
import datetime
import hashlib
import json
import os
from pathlib import Path
import time
import urllib.error
import urllib.parse
import urllib.request
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parents[1]
DEST = ROOT / '.local/source_acquisition_2026-10-19/proteor1_checkpoints'
REPOS = ['thinking-bio-lab/proteor1-understand', 'thinking-bio-lab/proteor1-generate']


def now():
    return datetime.datetime.now(ZoneInfo('America/Los_Angeles')).isoformat()


def save(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + '.tmp')
    tmp.write_text(json.dumps(value, indent=2, sort_keys=True) + '\n')
    tmp.replace(path)


def digest(path):
    h = hashlib.sha256()
    with path.open('rb') as stream:
        for block in iter(lambda: stream.read(4 * 1024 * 1024), b''):
            h.update(block)
    return h.hexdigest()


def download(item):
    rec = {**item, 'started_at_pacific': now(), 'state': 'downloading'}
    path = DEST / item['relative_path']
    progress_path = path.with_name(path.name + '.transfer.json')
    path.parent.mkdir(parents=True, exist_ok=True)
    part = path.with_name(path.name + '.part')
    try:
        if not path.exists():
            for attempt in range(12):
                start = part.stat().st_size if part.exists() else 0
                headers = {'User-Agent': 'bio-evaluation-public-checkpoint-acquisition/1.0'}
                if start:
                    headers['Range'] = 'bytes=' + str(start) + '-'
                request = urllib.request.Request(item['url'], headers=headers)
                try:
                    with urllib.request.urlopen(request, timeout=60) as response:
                        if start and response.status == 206:
                            expected = 'bytes ' + str(start) + '-'
                            if not response.headers.get('Content-Range', '').startswith(expected):
                                raise ValueError('Resume range identity mismatch')
                        elif start and response.status == 200:
                            start = 0
                        last = time.monotonic()
                        with part.open('ab' if start else 'wb') as out:
                            count = start
                            while True:
                                block = response.read(2 * 1024 * 1024)
                                if not block:
                                    break
                                out.write(block)
                                count += len(block)
                                if count > item['expected_bytes']:
                                    raise ValueError('Checkpoint larger than pinned size')
                                if time.monotonic() - last > 15:
                                    save(progress_path, {**rec, 'updated_at_pacific': now(), 'transferred_bytes': count})
                                    last = time.monotonic()
                    if part.stat().st_size == item['expected_bytes']:
                        break
                    # A normally closed short response is not a complete checkpoint.
                    # Retain its contiguous prefix and request the next exact range.
                    if attempt == 11:
                        raise ValueError('Checkpoint transfer remained incomplete')
                except (urllib.error.URLError, TimeoutError, ConnectionError):
                    if attempt == 11:
                        raise
                    time.sleep(1)
            if part.stat().st_size != item['expected_bytes']:
                raise ValueError('Checkpoint size mismatch')
            got = digest(part)
            if item.get('publisher_sha256') and got != item['publisher_sha256']:
                raise ValueError('Publisher LFS SHA256 mismatch')
            part.replace(path)
        else:
            got = digest(path)
            if path.stat().st_size != item['expected_bytes'] or item.get('publisher_sha256') and got != item['publisher_sha256']:
                raise ValueError('Existing checkpoint identity mismatch')
        rec.update(state='downloaded_verified', bytes=path.stat().st_size, sha256=got,
                   publisher_sha256_verified=bool(item.get('publisher_sha256')), finished_at_pacific=now())
    except Exception as error:
        rec.update(state='failed_or_partial', error_type=type(error).__name__, finished_at_pacific=now())
        if isinstance(error, ValueError):
            rec['validation_failure'] = str(error)
        if isinstance(error, urllib.error.HTTPError):
            rec['http_status'] = error.code
    save(progress_path, rec)
    return rec


def main():
    DEST.mkdir(parents=True, exist_ok=True)
    manifest = {'started_at_pacific': now(), 'pid': os.getpid(), 'stage': 'acquiring',
                'task_ids': ['P41'], 'model_loads': 0, 'inference_calls': 0, 'training': False,
                'original_paper_holdout_and_runtime_still_unresolved': True, 'repositories': [], 'assets': []}
    items = []
    for repo in REPOS:
        url = 'https://huggingface.co/api/models/' + repo + '?blobs=true'
        with urllib.request.urlopen(url, timeout=45) as response:
            meta = json.load(response)
        if meta.get('private') or meta.get('gated'):
            raise ValueError('Expected public ungated official checkpoint')
        revision = meta['sha']
        manifest['repositories'].append({'repo': repo, 'revision': revision, 'metadata_url': url})
        save(DEST / repo.split('/')[-1] / 'publisher_metadata.json', meta)
        for file in meta['siblings']:
            name = file['rfilename']
            if name.endswith(('.bin', '.safetensors', '.json', '.txt', '.model', '.yaml', '.yml')):
                items.append({'repo': repo, 'revision': revision,
                    'relative_path': repo.split('/')[-1] + '/' + name,
                    'expected_bytes': file['size'], 'publisher_sha256': (file.get('lfs') or {}).get('sha256'),
                    'url': 'https://huggingface.co/' + repo + '/resolve/' + revision + '/' + urllib.parse.quote(name, safe='/')})
    manifest['planned_files'] = len(items)
    manifest['expected_bytes'] = sum(x['expected_bytes'] for x in items)
    if manifest['expected_bytes'] > 20 * 1024 ** 3:
        raise ValueError('Unexpectedly large official checkpoint selection')
    save(DEST / 'manifest.json', manifest)
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        for future in concurrent.futures.as_completed([pool.submit(download, item) for item in items]):
            manifest['assets'].append(future.result())
            manifest['updated_at_pacific'] = now()
            save(DEST / 'manifest.json', manifest)
    manifest.update(stage='acquisition_terminal', finished_at_pacific=now(),
                    verified_files=sum(x['state'] == 'downloaded_verified' for x in manifest['assets']),
                    verified_bytes=sum(x.get('bytes', 0) for x in manifest['assets']))
    save(DEST / 'manifest.json', manifest)
    print(json.dumps({k: manifest[k] for k in ['stage', 'planned_files', 'verified_files', 'verified_bytes', 'finished_at_pacific']}))


if __name__ == '__main__':
    main()
