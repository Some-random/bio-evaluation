#!/usr/bin/env python3
"""Observe acquisition receipts without inference or dispatch authority."""
import argparse
import datetime
import fcntl
import hashlib
import json
import os
from pathlib import Path
import time
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / '.local/source_acquisition_2026-10-19'
SOURCES = {
    'prediction_datasets': 'prediction_datasets/summary.json',
    'protocol_sources': 'protocols/manifest.json',
    'rabd_coordinates': 'structural_context/manifest.json',
    'chartqa_images': 'vision/chartqa/completion.json',
    'llava_med_images': 'vision/v06/completion.json',
    'evaluator_transfers': 'evaluators/status.json',
    'protst_transfer': 'evaluators/protst_parallel_transfer.json',
    'proteor1_checkpoints': 'proteor1_checkpoints/manifest.json',
    'proteor1_resume': 'proteor1_checkpoints/resume_status.json',
    'mutadescribe_sources': 'mutadescribe_sources/schema_and_counts.json',
    'b06_input_review': 'b06_review/review_receipt.json',
    'b06_review_interruption': 'b06_review/review_interruption.json',
    'p18_preparation_interruption': 'p18_gfp_candidate/review_interruption.json',
    'arxivqa_assets': 'vision/arxivqa/completion.json',
    'slidevqa_images': 'vision/slidevqa/spooled_progress.json',
    'slidevqa_process': 'vision/slidevqa/spool_watcher_status.json',
}
FIELDS = (
    'stage', 'state', 'status', 'role', 'pid', 'updated_at_pacific', 'finished_at_pacific',
    'updated_at_utc', 'finished_at_utc', 'planned_source_files', 'downloaded_files',
    'downloaded_bytes', 'unavailable_files', 'planned', 'downloaded', 'planned_files',
    'verified_files', 'verified_bytes', 'expected_bytes', 'compressed_archive_bytes',
    'planned_images', 'verified_images', 'failed_images', 'expected_images', 'blocked_images',
    'case_count', 'cases_with_verified_image', 'questions', 'questions_with_verified_images',
    'source_case_count', 'reviewed_ordinary_benign_candidate_count', 'remaining_independent_unreviewed_count',
    'full_benchmark_review_complete', 'native_benchmark_dispatch_ready', 'all_downloads_complete',
    'errors', 'verified', 'failed', 'completed', 'total', 'image_count', 'planned_urls',
    'successful', 'downloaded_images', 'newly_recovered_previously_blocked_images',
    'new_bytes_completed', 'contiguous_original_prefix_bytes', 'measured_bytes_per_second',
    'all_files_verified', 'exact_trigger_case_unknown', 'completed_review_receipt_preserved',
    'new_inference_calls', 'remaining_independent_unreviewed_count',
    'source_asset_count', 'evaluation_csv_file_count', 'total_downloaded_bytes',
    'holds_lifted', 'raw_rows_displayed',
)


def scalar(data):
    return {key: data[key] for key in FIELDS if key in data and
            (data[key] is None or type(data[key]) in (bool, int, float, str))}


def snapshot():
    result = {'updated_at_pacific': datetime.datetime.now(ZoneInfo('America/Los_Angeles')).isoformat(),
              'role': 'read_only_source_acquisition_observer_not_benchmark_execution',
              'observer_pid': os.getpid(), 'poll_seconds': 60, 'inference_calls_by_observer': 0,
              'training_by_observer': False, 'workers': [],
              'downloaded_assets_are_not_completed_benchmark_scores': True}
    for name, rel in SOURCES.items():
        path = BASE / rel
        item = {'name': name, 'source_path': str(path.relative_to(ROOT))}
        try:
            raw = path.read_bytes()
            if len(raw) > 8 * 1024 * 1024:
                raise ValueError('Receipt too large')
            data = json.loads(raw)
            item.update(source_available=True, source_sha256=hashlib.sha256(raw).hexdigest(),
                        source_age_seconds=round(time.time() - path.stat().st_mtime), summary=scalar(data))
            if name == 'prediction_datasets':
                item['tasks'] = {task: {key: rec[key] for key in ('status', 'updated_at_pacific', 'native_split_counts_from_publisher_loader') if key in rec}
                                 for task, rec in data.get('tasks', {}).items()}
            if name in ['proteor1_checkpoints', 'proteor1_resume', 'protocol_sources']:
                assets = data.get('assets', [])
                done = [a for a in assets if a.get('state', a.get('status', '')).startswith('downloaded')]
                item['summary']['observed_verified_file_count'] = len(done)
                item['summary']['observed_verified_bytes'] = sum(a.get('bytes', 0) for a in done)
            if name == 'evaluator_transfers':
                item['assets'] = [{key: a[key] for key in ('id', 'state', 'bytes', 'actual_bytes',
                    'observed_transferred_bytes', 'recent_measured_bytes_per_second', 'publisher_digest_verified') if key in a}
                    for a in data.get('assets', [])]
            pid = data.get('pid')
            if type(pid) is int:
                item['process_exists'] = (Path('/proc') / str(pid)).exists()
        except FileNotFoundError:
            item.update(source_available=False, reason='receipt_not_available_counts_unknown')
        except Exception as error:
            item.update(source_available=False, reason=type(error).__name__)
        result['workers'].append(item)
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--watch', action='store_true')
    args = parser.parse_args()
    BASE.mkdir(parents=True, exist_ok=True)
    with (BASE / 'observer.lock').open('a') as lock:
        fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        while True:
            data = snapshot()
            tmp = BASE / 'status.json.tmp'
            tmp.write_text(json.dumps(data, indent=2, sort_keys=True) + '\n')
            tmp.replace(BASE / 'status.json')
            if not args.watch:
                print(json.dumps({'status_path': str(BASE / 'status.json'), 'observer_pid': os.getpid()}))
                return
            time.sleep(60)


if __name__ == '__main__':
    main()
