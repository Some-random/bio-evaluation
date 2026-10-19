#!/usr/bin/env python3
"""Acquire existing upstream RAbD coordinate files; no design or inference."""
import concurrent.futures
import datetime
import gzip
import hashlib
import json
from pathlib import Path
import urllib.error
import urllib.request
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / '.local/source_acquisition_2026-10-19/structural_context'
SOURCE = ROOT / '.local/source_acquisition_2026-10-19/protocols/THUNLP-MT__MEAN/files/summaries/rabd_summary.jsonl'


def now():
    return datetime.datetime.now(ZoneInfo('America/Los_Angeles')).isoformat()


def acquire(pdb):
    pdb = pdb.lower()
    if len(pdb) != 4 or not pdb.isalnum():
        raise ValueError('Unexpected PDB identifier')
    url = 'https://files.rcsb.org/download/' + pdb.upper() + '.pdb.gz'
    path = BASE / (pdb + '.pdb.gz')
    record = {'pdb_id': pdb, 'url': url, 'observed_at_pacific': now(), 'publisher_digest_available': False}
    try:
        if path.exists():
            data = path.read_bytes()
        else:
            request = urllib.request.Request(url, headers={'User-Agent': 'bio-evaluation-source-acquisition/1.0'})
            with urllib.request.urlopen(request, timeout=60) as response:
                data = response.read(50 * 1024 * 1024 + 1)
            if len(data) > 50 * 1024 * 1024:
                raise ValueError('Coordinate file exceeds acquisition limit')
        coordinates = gzip.decompress(data)
        if not coordinates.startswith(b'HEADER') or pdb.upper().encode() not in coordinates.splitlines()[0]:
            raise ValueError('Coordinate header identity mismatch')
        if not path.exists():
            tmp = path.with_suffix(path.suffix + '.part')
            tmp.write_bytes(data)
            tmp.replace(path)
        record.update(status='downloaded_current_rcsb_coordinates', bytes=len(data),
                      sha256=hashlib.sha256(data).hexdigest(), gzip_crc_valid=True,
                      header_identifier_verified=True)
    except Exception as error:
        record.update(status='unavailable', error_type=type(error).__name__)
        if isinstance(error, urllib.error.HTTPError):
            record['http_status'] = error.code
    return record


def main():
    BASE.mkdir(parents=True, exist_ok=True)
    source_bytes = SOURCE.read_bytes()
    rows = [json.loads(line) for line in source_bytes.splitlines() if line.strip()]
    ids = [row['pdb'] for row in rows]
    if len(ids) != 60 or len(set(ids)) != 60:
        raise ValueError('Unexpected upstream case roster')
    manifest = {'started_at_pacific': now(), 'stage': 'acquiring', 'planned': 60, 'assets': [],
                'upstream_id_source': str(SOURCE.relative_to(ROOT)), 'source_sha256': hashlib.sha256(source_bytes).hexdigest(),
                'task_ids': ['P40'], 'inference_calls': 0, 'generation_calls': 0,
                'not_target_paper_processed_holdout': True, 'masks_numbering_and_sampling_unresolved': True,
                'historical_coordinate_bytes_not_certified': True}
    def save():
        tmp = BASE / 'manifest.json.tmp'
        tmp.write_text(json.dumps(manifest, indent=2, sort_keys=True) + '\n')
        tmp.replace(BASE / 'manifest.json')
    save()
    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as pool:
        for record in pool.map(acquire, ids):
            manifest['assets'].append(record)
            manifest['updated_at_pacific'] = now()
            save()
    manifest.update(stage='acquisition_terminal', finished_at_pacific=now(),
                    downloaded=sum(x['status'].startswith('downloaded') for x in manifest['assets']),
                    downloaded_bytes=sum(x.get('bytes', 0) for x in manifest['assets']))
    save()
    print(json.dumps({k: manifest[k] for k in ['stage', 'downloaded', 'downloaded_bytes', 'finished_at_pacific']}))


if __name__ == '__main__':
    main()
