#!/usr/bin/env python3
"""Export sealed local conditions and reference-free trajectories for reporting."""
import argparse
import datetime
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import tarfile
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / '.local/catalog_execution_2026-10-20'
OUTPUT = ROOT / 'reports/CATALOG_NEW_SCORES_2026-10-20.json'


def sha(path):
    h = hashlib.sha256()
    with Path(path).open('rb') as handle:
        for chunk in iter(lambda: handle.read(8 * 1024 * 1024), b''):
            h.update(chunk)
    return h.hexdigest()


def read(path):
    return json.loads(Path(path).read_text())


def metrics_for(task, score):
    if task == 'P06':
        return {'spearman': score['spearman']}, score['counts']['valid_predictions']
    if task == 'P07':
        return {'spearman': score['primary_metric_value']}, score['metrics']['parsed']
    if task == 'P08':
        return {'spearman': score['metrics']['spearman']}, score['metrics']['valid_predictions']
    return score['metrics'], score['parsed']


def all_finite(metrics):
    values = list(metrics.values())
    return bool(values) and all(type(x) in (int, float) and math.isfinite(x) for x in values)


def derived_p09(scanner):
    """Export the sealed rule-derived condition without claiming new generation."""
    folder = BASE / 'tasks/P09'
    score_path = folder / 'scores.json'
    if not score_path.exists():
        return []
    score, config = read(score_path), read(folder / 'adaptation_config.json')
    source = Path(config['p08_expected_run'])
    completion = read(source / 'completion.json')
    n = config['planned']
    if (score['configuration_sha256'] != sha(folder / 'adaptation_config.json')
            or score['prediction_lock_sha256'] != sha(source / 'prediction_lock.json')
            or completion['prediction_lock_sha256'] != score['prediction_lock_sha256']
            or completion['terminal'] != n or completion['planned'] != n
            or score['metrics']['planned'] != n
            or score['metrics']['valid_predictions'] != n
            or score['metrics']['invalid_or_missing'] != 0
            or score['new_model_calls_by_scorer'] != 0
            or score['historical_runs_modified'] is not False
            or not all_finite({'accuracy_percent': score['metrics']['accuracy_percent']})):
        raise ValueError('P09 derived score differs from its frozen complete source')
    public = ROOT / 'results/runs' / config['run_id'] / 'scores.json'
    public.parent.mkdir(parents=True, exist_ok=True)
    scanner.scan_file(score_path)
    if public.exists() and public.read_bytes() != score_path.read_bytes():
        raise ValueError('Existing P09 score export changed')
    public.write_bytes(score_path.read_bytes())
    return [{'task_id': 'P09', 'run_id': config['run_id'],
        'protocol_variant': config['protocol_variant'],
        'protocol_description': 'declared >1.0 rule derived offline from sealed P08 scalar predictions',
        'new_complete_generation': False, 'derived_from_sealed_generation': True,
        'new_inference_calls': 0, 'full_benchmark_complete': True,
        'full_primary_metric_defined': True,
        'counts': {'planned': n, 'completed': n, 'parsed': n, 'invalid_outputs': 0,
                   'missing_or_failed_outputs': 0},
        'metrics': {'accuracy_percent': score['metrics']['accuracy_percent']},
        'source_scores': str(public.relative_to(ROOT)), 'scores_sha256': sha(public),
        'prediction_lock_sha256': score['prediction_lock_sha256'],
        'config_sha256': score['configuration_sha256'],
        'prediction_source_task_id': 'P08',
        'prediction_source_run_id': score['prediction_source_run_id'],
        'material_differences': score['material_differences'],
        'case_scope': 'Complete released 12,851-case stability split; derived adaptation, not native NatureLM labels',
        'interpretation': score['interpretation']}]


def trajectory(folder, run_id, lock, scanner):
    destination = ROOT / 'results/trajectory_archives' / (run_id + '.tar.gz')
    receipt = destination.with_suffix('.manifest.json')
    lock_sha = sha(folder / 'prediction_lock.json')
    if receipt.exists():
        prior = read(receipt)
        if prior['prediction_lock_sha256'] != lock_sha or sha(destination) != prior['archive_sha256']:
            raise ValueError('Existing trajectory export differs from its immutable seal')
        return str(destination.relative_to(ROOT)), prior['archive_sha256']
    if destination.exists():
        raise ValueError('Unsealed archive already exists; inspect instead of overwriting')
    files = dict(lock['files_sha256'])
    for name in files:
        path = Path(name)
        if path.is_absolute() or '..' in path.parts or path.parts[0] not in {
                'requests', 'responses', 'outcomes', 'errors', 'run_manifest.json', 'tokenizer_preflight.json'}:
            raise ValueError('Unexpected trajectory member; scorer references must stay separate')
        local = folder / path
        if local.is_symlink() or sha(local) != files[name]:
            raise ValueError('Locked trajectory member changed')
        scanner.scan_file(local)
    for name in ('prediction_lock.json', 'completion.json', 'scores.json'):
        scanner.scan_file(folder / name)
        files[name] = sha(folder / name)
    destination.parent.mkdir(parents=True, exist_ok=True)
    temporary = destination.with_suffix('.tmp')
    with tarfile.open(temporary, 'w:gz') as archive:
        for name in sorted(files):
            archive.add(folder / name, arcname=name, recursive=False)
    temporary.replace(destination)
    document = {'schema_version': 1, 'run_id': run_id,
        'prediction_lock_sha256': lock_sha, 'archive_sha256': sha(destination),
        'archive_bytes': destination.stat().st_size, 'member_count': len(files),
        'files_sha256': files, 'scorer_references_included': False,
        'model_weights_included': False, 'credentials_included': False}
    receipt.write_text(json.dumps(document, indent=2) + '\n')
    return str(destination.relative_to(ROOT)), document['archive_sha256']


def export(archive=True):
    process = read(BASE / 'control/driver_process.json')
    plan_path = Path(process['plan_path'])
    if sha(plan_path) != process['plan_sha256']:
        raise ValueError('Execution plan changed')
    spec = importlib.util.spec_from_file_location('catalog_export_scanner', ROOT / 'scripts/daily_backup.py')
    scanner = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(scanner)
    completed, undefined = [], []
    for entry in read(plan_path)['tasks']:
        task = entry['task_id']
        folder = BASE / 'tasks' / task / 'runtime/benchmark'
        completion, score_path = folder / 'completion.json', Path(entry['score_output'])
        if not completion.exists() or not score_path.exists():
            continue
        done, score = read(completion), read(score_path)
        config_path = Path(entry['benchmark_config'])
        config = read(config_path)
        lock_path = folder / 'prediction_lock.json'
        if (done['terminal'] != done['planned'] or done['planned'] != config['planned']
                or sha(config_path) != entry['benchmark_config_sha256']
                or sha(entry['scorer']) != entry['scorer_sha256']
                or score.get('config_sha256', score.get('configuration_sha256')) != sha(config_path)
                or done['prediction_lock_sha256'] != sha(lock_path)
                or score['prediction_lock_sha256'] != sha(lock_path)):
            raise ValueError('Score identity differs from complete generation: ' + task)
        metrics, parsed = metrics_for(task, score)
        public_score = ROOT / 'results/runs' / config['run_id'] / 'scores.json'
        public_score.parent.mkdir(parents=True, exist_ok=True)
        if public_score.exists() and public_score.read_bytes() != score_path.read_bytes():
            raise ValueError('Existing public score copy changed')
        scanner.scan_file(score_path)
        public_score.write_bytes(score_path.read_bytes())
        row = {'task_id': task, 'run_id': config['run_id'],
            'protocol_variant': config.get('protocol_variant', config.get('variant')),
            'protocol_description': 'nonthinking constrained scalar, 256 output tokens' if task in {'P06','P07','P08'} else 'nonthinking dense ordered three-decimal confidence vector, 16K budget',
            'new_complete_generation': True, 'full_benchmark_complete': True,
            'full_primary_metric_defined': parsed == done['planned'] and all_finite(metrics),
            'counts': {'planned': done['planned'], 'completed': done['terminal'], 'parsed': parsed,
                'invalid_outputs': done['planned']-parsed,
                'missing_or_failed_outputs': done['planned']-done['responses_saved']},
            'finish_reasons': {'length': done['truncations'], 'stop': done['responses_saved']-done['truncations']},
            'generation': config['generation'], 'metrics': metrics,
            'source_scores': str(public_score.relative_to(ROOT)), 'scores_sha256': sha(public_score),
            'prediction_lock_sha256': sha(lock_path), 'config_sha256': sha(config_path),
            'case_scope': score.get('case_scope', 'complete previously reviewed original test cohort; new independent condition'),
            'interpretation': score.get('interpretation') or score.get('paper_comparison') or 'Zero-shot full-sequence annotation adaptation; native metric formulas preserved. No matched trained-head or PDB/crop reproduction claim.'}
        if archive:
            path, digest = trajectory(folder, config['run_id'], read(lock_path), scanner)
            row['trajectory_archive'] = {'path': path, 'sha256': digest}
        (completed if row['full_primary_metric_defined'] else undefined).append(row)
    document = {'schema_version': 1,
        'generated_at_pacific': datetime.datetime.now(ZoneInfo('America/Los_Angeles')).isoformat(),
        'historical_artifacts_modified': False, 'new_inference_calls_by_exporter': 0,
        'completed_rows': completed, 'diagnostic_only_finished_runs': undefined,
        'derived_completed_rows': derived_p09(scanner)}
    temporary = OUTPUT.with_suffix('.json.tmp')
    temporary.write_text(json.dumps(document, indent=2, allow_nan=False) + '\n')
    temporary.replace(OUTPUT)
    return document


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--without-archives', action='store_true')
    args = parser.parse_args()
    document = export(not args.without_archives)
    print(json.dumps({'completed_conditions': len(document['completed_rows']),
                      'undefined_conditions': len(document['diagnostic_only_finished_runs'])}))
