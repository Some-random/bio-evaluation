#!/usr/bin/env python3
"""Acquire pinned evaluation fixtures and vendor files without loading models."""
import concurrent.futures as futures
from datetime import datetime
import fcntl
import hashlib
import json
import math
import os
from pathlib import Path
import threading
import time
import urllib.request
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / '.local/source_recovery_round2_2026-10-19/structural'
OLD = ROOT / '.local/source_acquisition_2026-10-19/protocols'
CHUNK = 32 * 1024 * 1024
GUARD = threading.Lock()


def now():
    return datetime.now(ZoneInfo('America/Los_Angeles')).isoformat()


def save(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + '.tmp')
    tmp.write_text(json.dumps(data, indent=2, sort_keys=True) + '\n')
    tmp.replace(path)


def get(url, headers=None):
    return urllib.request.urlopen(urllib.request.Request(url, headers={
        'User-Agent': 'bio-evaluation-author-asset-recovery/1.0', **(headers or {})}), timeout=90)


def git_item(item):
    dest = BASE / item['relative_path']
    dest.parent.mkdir(parents=True, exist_ok=True)
    try:
        if dest.is_file():
            raw = dest.read_bytes()
        else:
            with get(item['url']) as response:
                raw = response.read(item['expected_bytes'] + 1)
        assert len(raw) == item['expected_bytes'], 'Git source size mismatch'
        blob = hashlib.sha1(b'blob ' + str(len(raw)).encode() + b'\0' + raw).hexdigest()
        assert blob == item['publisher_git_blob'], 'Git source identity mismatch'
        tmp = dest.with_suffix(dest.suffix + '.partial')
        tmp.write_bytes(raw)
        tmp.replace(dest)
        return {**item, 'state': 'downloaded_verified', 'bytes': len(raw),
                'sha256': hashlib.sha256(raw).hexdigest(), 'publisher_git_blob_verified': True}
    except Exception as error:
        return {**item, 'state': 'failed', 'error_type': type(error).__name__,
                'http_status': getattr(error, 'code', None)}


def verify_file(path, item):
    sha = hashlib.sha256()
    parts = []
    with path.open('rb') as stream:
        for block in iter(lambda: stream.read(16 * 1024 * 1024), b''):
            sha.update(block)
            parts.append(hashlib.md5(block).digest())
    assert path.stat().st_size == item['expected_bytes'], 'Vendor size mismatch'
    digest = sha.hexdigest()
    if item.get('publisher_sha256'):
        assert digest == item['publisher_sha256'], 'Publisher SHA256 mismatch'
    etag = str(item.get('etag') or '').strip('"')
    multipart = hashlib.md5(b''.join(parts)).hexdigest() + '-' + str(len(parts))
    verified_etag = bool(etag and '-' in etag and multipart == etag)
    if etag.rsplit('-', 1)[-1] == str(len(parts)):
        assert verified_etag, 'Publisher multipart ETag mismatch'
    return {'bytes': path.stat().st_size, 'sha256': digest,
            'publisher_sha256_verified': bool(item.get('publisher_sha256')),
            'publisher_multipart_etag_verified': verified_etag,
            'multipart_etag_16mib': multipart,
            'source_identity_note': 'Pinned HF SHA256 where available; other files have local SHA256 and publisher HTTP identity. No pickle or model loading.'}


def transfer_range(fd, item, start, end):
    headers = {'Range': f'bytes={start}-{end}'}
    if item.get('etag'):
        headers['If-Match'] = item['etag']
    began = time.monotonic()
    with get(item['url'], headers) as response:
        assert response.status == 206, 'Source did not honor exact range'
        assert response.headers.get('Content-Range') == f'bytes {start}-{end}/{item["expected_bytes"]}', 'Range identity mismatch'
        offset = start
        sha = hashlib.sha256()
        while True:
            if time.monotonic() - began > 120:
                raise TimeoutError('Range exceeded its total time budget')
            block = response.read1(min(2 * 1024 * 1024, end - offset + 2))
            if not block:
                break
            assert offset + len(block) <= end + 1, 'Oversized range'
            written = 0
            while written < len(block):
                written += os.pwrite(fd, block[written:], offset + written)
            sha.update(block)
            offset += len(block)
        assert offset == end + 1, 'Short range'
    return {'bytes': offset - start, 'sha256': sha.hexdigest()}


def recheck_chunks(path, expected_bytes, claimed):
    """Reuse only ranges whose receipt still matches the actual partial bytes."""
    if not path.is_file():
        return {}
    verified = {}
    with path.open('rb') as stream:
        for key, receipt in claimed.items():
            if not key.isdecimal() or str(int(key)) != key:
                continue
            start = int(key) * CHUNK
            size = min(CHUNK, expected_bytes - start)
            if size <= 0 or receipt.get('bytes') != size:
                continue
            stream.seek(start)
            remaining = size
            sha = hashlib.sha256()
            while remaining:
                block = stream.read(min(1024 * 1024, remaining))
                if not block:
                    break
                sha.update(block)
                remaining -= len(block)
            if remaining == 0 and sha.hexdigest() == receipt.get('sha256'):
                verified[key] = receipt
    return verified


def reuse_complete(path, item):
    if not path.is_file():
        return None
    return {**item, **verify_file(path, item), 'state': 'downloaded_verified',
            'verified_chunk_bytes': item['expected_bytes'],
            'reused_complete_file': True, 'finished_at_pacific': now()}


def main():
    BASE.mkdir(parents=True, exist_ok=True)
    with (BASE / 'worker.lock').open('a') as lock:
        fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        state = {'started_at_pacific': now(), 'updated_at_pacific': now(), 'pid': os.getpid(),
                 'stage': 'acquiring_pinned_source_fixtures', 'inference_calls': 0,
                 'training': False, 'model_weights_loaded': False,
                 'downloaded_files': 0, 'downloaded_bytes': 0, 'assets': []}
        def publish():
            with GUARD:
                state['updated_at_pacific'] = now()
                done = [a for a in state['assets'] if a.get('state') == 'downloaded_verified']
                state['downloaded_files'] = len(done)
                state['downloaded_bytes'] = sum(a.get('bytes', 0) for a in done)
                state['verified_vendor_chunk_bytes'] = sum(a.get('verified_chunk_bytes', 0) for a in state['assets'])
                save(BASE / 'manifest.json', state)
                save(BASE / 'status.json', {k: v for k, v in state.items() if k != 'assets'})
        items = []
        repos = [('smiles724/Proteo-R1', 'ffaa787bce5f30e4cb41e2de5d0b0daab0059243'),
                 ('THUNLP-MT/MEAN', 'a510ceef282cc24c8f658c14c2bfca10a95c23c0')]
        for repo, revision in repos:
            directory = repo.replace('/', '__')
            tree = json.loads((OLD / directory / 'tree.json').read_text())['tree']
            for entry in tree:
                name = entry['path']
                selected = (name.startswith(('data/', 'pretrained/')) or name == '.gitmodules') if 'Proteo-R1' in repo else (
                    name.startswith(('data/', 'evaluation/')) or name in (
                    'scripts/prepare_data_rabd.sh', 'scripts/prepare_data_kfold.sh',
                    'scripts/setup.sh', 'rabd_test.sh', 'generate.py',
                    'checkpoints/ckpt/rabd_cdrh3_mean.ckpt', 'checkpoints/train_config.json'))
                if entry['type'] == 'blob' and selected:
                    items.append({'repo': repo, 'revision': revision,
                        'relative_path': 'source/' + directory + '/' + name,
                        'expected_bytes': entry['size'], 'publisher_git_blob': entry['sha'],
                        'url': 'https://raw.githubusercontent.com/' + repo + '/' + revision + '/' + name})
        state['planned_source_files'] = len(items)
        publish()
        with futures.ThreadPoolExecutor(6) as pool:
            for result in pool.map(git_item, items):
                state['assets'].append(result)
                publish()
        state['stage'] = 'acquiring_vendor_files'
        metadata = json.loads((BASE / 'vendor_http_metadata.json').read_text())['assets']
        vendor = []
        for item in metadata:
            if item.get('http_status') != 200 or not item.get('expected_bytes'):
                continue
            vendor.append({**item, 'relative_path': 'vendor/' + item['url'].rsplit('/', 1)[-1]})
        hf = json.loads((BASE / 'boltz_ccd_publisher_metadata.json').read_text())
        for entry in hf['siblings']:
            if entry['rfilename'] == 'model/ccd.pkl':
                vendor.append({'id': 'boltz_ccd', 'relative_path': 'vendor/boltz_ccd.pkl',
                    'expected_bytes': entry['size'], 'publisher_sha256': entry['lfs']['sha256'],
                    'url': 'https://huggingface.co/clorf6/MF-Design/resolve/' + hf['sha'] + '/model/ccd.pkl'})
        assert sum(v['expected_bytes'] for v in vendor) < 20 * 1024 ** 3
        state['planned_vendor_files'] = len(vendor)
        state['planned_vendor_bytes'] = sum(v['expected_bytes'] for v in vendor)
        handles = {}
        journals = {}
        jobs = []
        for item in vendor:
            path = BASE / item['relative_path']
            path.parent.mkdir(exist_ok=True)
            journal = path.with_suffix(path.suffix + '.chunks.json')
            prior = json.loads(journal.read_text()) if journal.is_file() else {}
            pin = hashlib.sha256(json.dumps(item, sort_keys=True).encode()).hexdigest()
            assert not prior or prior.get('source_pin_sha256') == pin, 'Source changed since partial transfer'
            complete = reuse_complete(path, item)
            if complete is not None:
                state['assets'].append(complete)
                publish()
                continue
            temp = path.with_suffix(path.suffix + '.partial')
            claimed = prior.get('verified_chunks', {})
            done = recheck_chunks(temp, item['expected_bytes'], claimed)
            rec = {**item, 'state': 'downloading',
                   'cached_chunks_rejected_after_disk_check': len(claimed) - len(done),
                   'verified_chunk_bytes': sum(x['bytes'] for x in done.values())}
            state['assets'].append(rec)
            fd = os.open(temp, os.O_CREAT | os.O_RDWR, 0o600)
            os.ftruncate(fd, item['expected_bytes'])
            handles[item['id']] = (fd, item, rec, temp, path)
            journals[item['id']] = {'source_pin_sha256': pin, 'verified_chunks': done}
            for index, start in enumerate(range(0, item['expected_bytes'], CHUNK)):
                if str(index) not in done:
                    jobs.append((item['id'], index, start, min(start + CHUNK, item['expected_bytes']) - 1))
        publish()

        def one(job):
            ident, index, start, end = job
            fd, item, rec, temp, path = handles[ident]
            for attempt in range(3):
                try:
                    return ident, str(index), transfer_range(fd, item, start, end)
                except Exception:
                    if attempt == 2:
                        raise
                    time.sleep(1)
        try:
            with futures.ThreadPoolExecutor(16) as pool:
                for result in futures.as_completed([pool.submit(one, job) for job in jobs]):
                    ident, index, receipt = result.result()
                    journal = journals[ident]
                    journal['verified_chunks'][index] = receipt
                    fd, item, rec, temp, path = handles[ident]
                    rec['verified_chunk_bytes'] = sum(x['bytes'] for x in journal['verified_chunks'].values())
                    save(path.with_suffix(path.suffix + '.chunks.json'), journal)
                    publish()
            state['stage'] = 'verifying_vendor_files'
            publish()
            for ident, (fd, item, rec, temp, path) in handles.items():
                os.fsync(fd)
                os.close(fd)
                rec.update(verify_file(temp, item), state='downloaded_verified', finished_at_pacific=now())
                temp.replace(path)
                publish()
        finally:
            for fd, *_ in handles.values():
                try:
                    os.close(fd)
                except OSError:
                    pass
        state.update(stage='acquisition_terminal', finished_at_pacific=now(),
                     full_paper_test_cohort_recovered=False,
                     all_selected_files_verified=all(a['state'] == 'downloaded_verified' for a in state['assets']))
        publish()
        save(BASE / 'completion.json', state)
        print(json.dumps({k: state[k] for k in ['stage', 'downloaded_files', 'downloaded_bytes', 'all_selected_files_verified']}))


if __name__ == '__main__':
    try:
        main()
    except Exception as error:
        failure = {'stage': 'failed_or_partial', 'updated_at_pacific': now(),
                   'error_type': type(error).__name__, 'inference_calls': 0, 'pid': os.getpid()}
        save(BASE / 'worker_error.json', failure)
        save(BASE / 'status.json', failure)
        raise
