#!/usr/bin/env python3
"""Export exact P14 code, isolated inputs and completed continuation provenance."""
from datetime import datetime
import hashlib
import importlib.util
import io
import json
from pathlib import Path
import tarfile
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT/'.local/catalog_execution_2026-10-20'
RUN = 'qwen38_27b_p14_full_test_dense3dp_nonthinking16k_2026-10-20_v1'
CONFIG_SHA = 'aaa7d1fbdbcd3a1d1c2ed38026c542f44259659d3c1232f8c631ed44e9c48f2d'
CONTINUATION_SHA = '64b1f81dfa7a138458905736545ecb93f592c7cd85dc8528b6621ca125b260d4'


def sha(path):
    h = hashlib.sha256()
    with path.open('rb') as stream:
        for block in iter(lambda: stream.read(8*1024*1024), b''):
            h.update(block)
    return h.hexdigest()


def read(path):
    return json.loads(path.read_text())


def load_scanner():
    spec = importlib.util.spec_from_file_location('p14_protocol_secret_scanner', ROOT/'scripts/daily_backup.py')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def export_score_and_trajectory():
    """Add P14 alone, preserving every other independently published condition."""
    spec = importlib.util.spec_from_file_location('p14_reuse_catalog_export', ROOT/'scripts/export_catalog_scores_20261020.py')
    helper = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(helper)
    process = read(BASE/'control/driver_process.json')
    plan_path = Path(process['plan_path'])
    if sha(plan_path) != process['plan_sha256']:
        raise ValueError('Frozen dispatch plan changed')
    entry = next(r for r in read(plan_path)['tasks'] if r['task_id'] == 'P14')
    folder = BASE/'tasks/P14/runtime/benchmark'
    config_path, score_path = Path(entry['benchmark_config']), Path(entry['score_output'])
    config, done, score = read(config_path), read(folder/'completion.json'), read(score_path)
    lock_path = folder/'prediction_lock.json'
    if (config['run_id'] != RUN or sha(config_path) != CONFIG_SHA or
            sha(config_path) != entry['benchmark_config_sha256'] or sha(Path(entry['scorer'])) != entry['scorer_sha256'] or
            score['config_sha256'] != CONFIG_SHA or score['prediction_lock_sha256'] != sha(lock_path) or
            done['prediction_lock_sha256'] != sha(lock_path) or done['planned'] != 3416 or done['terminal'] != 3416 or
            score['planned'] != 3416 or score['parsed'] != 3416 or score['invalid_or_missing'] != 0 or
            score['full_planned_primary_metrics_valid'] is not True or not helper.all_finite(score['metrics'])):
        raise ValueError('Require complete pinned P14 score with finite full metrics')
    scanner = load_scanner()
    scanner.scan_file(score_path)
    public_score = ROOT/'results/runs'/RUN/'scores.json'
    public_score.parent.mkdir(parents=True, exist_ok=True)
    if public_score.exists() and public_score.read_bytes() != score_path.read_bytes():
        raise ValueError('Existing immutable public P14 score changed')
    public_score.write_bytes(score_path.read_bytes())
    archive, archive_sha = helper.trajectory(folder,RUN,read(lock_path),scanner)
    row = {'task_id':'P14','run_id':RUN,'protocol_variant':config['variant'],
        'protocol_description':'nonthinking dense ordered three-decimal confidence vector, 16K budget',
        'new_complete_generation':True,'full_benchmark_complete':True,'full_primary_metric_defined':True,
        'counts':{'planned':3416,'completed':3416,'parsed':3416,'invalid_outputs':0,
            'missing_or_failed_outputs':3416-done['responses_saved']},
        'finish_reasons':{'length':done['truncations'],'stop':done['responses_saved']-done['truncations']},
        'generation':config['generation'],'metrics':score['metrics'],
        'source_scores':str(public_score.relative_to(ROOT)),'scores_sha256':sha(public_score),
        'prediction_lock_sha256':sha(lock_path),'config_sha256':CONFIG_SHA,
        'case_scope':'Complete released 3,416-case test95 full-FASTA molecular-function cohort; fixed 489 GO descriptions.',
        'interpretation':'Zero-shot full-sequence annotation adaptation; native metric formulas preserved. No matched trained-head or PDB/crop reproduction claim.',
        'trajectory_archive':{'path':archive,'sha256':archive_sha}}
    output = ROOT/'reports/CATALOG_NEW_SCORES_2026-10-20.json'
    document = read(output)
    prior = [r for r in document['completed_rows'] if r.get('run_id') == RUN]
    if prior and prior != [row]:
        raise ValueError('Existing P14 export row changed')
    document['completed_rows'] = [r for r in document['completed_rows'] if r.get('run_id') != RUN]+[row]
    document['generated_at_pacific'] = datetime.now(ZoneInfo('America/Los_Angeles')).isoformat()
    temporary = output.with_suffix('.json.tmp')
    temporary.write_text(json.dumps(document,indent=2,allow_nan=False)+'\n')
    temporary.replace(output)
    return row


def export():
    task = BASE/'tasks/P14'
    folder = task/'runtime/benchmark'
    config_path = task/'full_test_config.json'
    config, score, done = read(config_path), read(folder/'scores.json'), read(folder/'completion.json')
    status = read(BASE/'control/P14_scoring_status.json')
    lock_sha = sha(folder/'prediction_lock.json')
    repair = folder/'offline_scoring_repair_v1'
    repair_members = {}
    if status.get('stage') == 'failed_no_retry' and (repair/'completion.json').is_file():
        recovered, review = read(repair/'completion.json'), read(repair/'root_review.json')
        if (recovered.get('stage') != 'native_score_completed_after_wrapper_repair' or
                recovered.get('exit_code') != 0 or recovered.get('model_calls') != 0 or
                recovered.get('native_scorer_changed') is not False or
                recovered.get('original_failed_wrapper_evidence_preserved') is not True or
                recovered.get('score_sha256') != sha(folder/'scores.json') or
                recovered.get('prediction_lock_sha256') != lock_sha or
                review.get('original_failed_status_sha256') != sha(BASE/'control/P14_scoring_status.json') or
                review.get('original_failed_log_sha256') != sha(BASE/'control/P14_scoring.log') or
                review.get('repair_script_sha256') != sha(repair/'run.py') or
                review.get('scoring_helper_sha256') != sha(ROOT/'scripts/score_catalog_in_runtime_20261020.py') or
                review.get('predecessor_terminal_receipt_sha256') != sha(BASE/'continuation_v1/runtime/predecessor_terminal_receipt.json')):
            raise ValueError('Offline wrapper repair does not verify unchanged native scoring')
        # The original failed status/log remain untouched and are exported below.
        status = {'stage':'completed', 'score_sha256':recovered['score_sha256']}
        repair_members = {'offline_scoring_repair/'+name:repair/name
                          for name in ('run.py','root_review.json','attempt.json','completion.json')}
    if (sha(config_path) != CONFIG_SHA or config['run_id'] != RUN or
            done['planned'] != 3416 or done['terminal'] != 3416 or done['responses_saved'] != 3416 or
            done['prediction_lock_sha256'] != lock_sha or score['prediction_lock_sha256'] != lock_sha or
            score['planned'] != 3416 or score['parsed'] != 3416 or score['invalid_or_missing'] != 0 or
            score['full_planned_primary_metrics_valid'] is not True or
            status['stage'] != 'completed' or status['score_sha256'] != sha(folder/'scores.json')):
        raise ValueError('Completed unchanged 3,416-case P14 generation and sole scoring receipt required')
    continuation = BASE/'continuation_v1'
    if sha(continuation/'manifest.json') != CONTINUATION_SHA:
        raise ValueError('Frozen continuation changed')
    manifest = read(continuation/'manifest.json')
    boundary = read(continuation/'runtime/P14_boundary.json')
    grant = read(continuation/'runtime/queue/P14_benchmark_continuation1.grant.json')
    finished = read(continuation/'runtime/queue/P14_benchmark_continuation1.finished.json')
    if (boundary['config_sha256'] != CONFIG_SHA or grant['config_sha256'] != CONFIG_SHA or
            grant['task_id'] != 'P14' or grant['run_id'] != RUN or grant['authorized'] is not True or
            grant['continuation_boundary_sha256'] != sha(continuation/'runtime/P14_boundary.json') or
            grant['server_identity_sha256'] != sha(continuation/'runtime/server_identity.json') or
            finished['exit_code'] != 0 or
            finished['grant_sha256'] != sha(continuation/'runtime/queue/P14_benchmark_continuation1.grant.json')):
        raise ValueError('Task-local continuation identity, boundary or terminal worker differs')
    for name, digest in manifest['files_sha256'].items():
        if sha(Path(name)) != digest:
            raise ValueError('Changed frozen continuation source')
    for name, digest in config['files_sha256'].items():
        if sha(Path(name)) != digest:
            raise ValueError('Changed frozen task source')
    pairs = {
        'task/full_test_config.json':config_path,
        'task/full_test_inputs.jsonl':Path(config['input_file']),
        'task/full_test_review.json':Path(config['review_file']),
        'task/class_vocabulary.json':Path(config['vocabulary_file']),
        'sources/native_torchdrug_metric.py':Path(config['metric_source_file']),
    }
    pairs.update(repair_members)
    for key, digest_key in [('input_file','input_sha256'),('review_file','review_sha256'),
                            ('vocabulary_file','vocabulary_sha256'),('metric_source_file','metric_source_sha256')]:
        if sha(Path(config[key])) != config[digest_key]:
            raise ValueError('Changed exact isolated task source')
    for name in ('prepare_p14_catalog_20261020.py','run_deepfri_catalog_20261020.py',
                 'score_deepfri_catalog_20261020.py','score_catalog_in_runtime_20261020.py',
                 'serve_catalog_20261020.py','continue_seven_catalog_20261020.py',
                 'export_catalog_scores_20261020.py','export_p14_protocol_20261021.py',
                 'report_p14_defined_score_20261021.py'):
        pairs['scripts/'+name] = ROOT/'scripts'/name
    for name in ('manifest.json','pool_plan.json','pool.sbatch','submission_receipt.json',
                 'request_permission_drain.json','runtime/predecessor_terminal_receipt.json',
                 'runtime/runtime_version_manifest.json','runtime/server_identity.json',
                 'runtime/P14_boundary.json','runtime/queue/P14_benchmark_continuation1.grant.json',
                 'runtime/queue/P14_benchmark_continuation1.started.json',
                 'runtime/queue/P14_benchmark_continuation1.finished.json'):
        pairs['continuation/'+name] = continuation/name
    for name in ('P14_scoring_status.json','P14_scoring.log','seven_dispatch_plan_v3.json'):
        pairs['control/'+name] = BASE/'control'/name
    forbidden = Path(config['scorer_reference_file']).resolve()
    scanner = load_scanner()
    digests = {}
    for name, path in pairs.items():
        if (path.is_symlink() or not path.is_file() or path.resolve() == forbidden or
                Path(name).is_absolute() or '..' in Path(name).parts or
                'scorer_reference' in name or 'credential' in name):
            raise ValueError('Unexpected or reference-bearing protocol member')
        scanner.scan_file(path)
        digests[name] = sha(path)
    archive = ROOT/'results/protocol_artifacts'/(RUN+'_source.tar.gz')
    receipt = archive.with_suffix('.manifest.json')
    if receipt.exists():
        prior = read(receipt)
        if (prior['files_sha256'] != digests or prior['archive_sha256'] != sha(archive) or
                prior['prediction_lock_sha256'] != lock_sha):
            raise ValueError('Existing immutable P14 source export changed')
        return archive, receipt
    if archive.exists():
        raise FileExistsError('Unsealed P14 source archive requires inspection')
    readme = ('P14 / DeepFRI molecular-function annotation\n\n'
        'Exact 3,416 released test95 full-FASTA inputs, 489 fixed ordered GO-MF descriptions, '
        'uniform 16,384-token outputs and independently declared zero-shot Qwen adaptation. '
        'The archive retains exact frozen solver/scorer/source bytes and P14 continuation identity, '
        'permission-drain, boundary, grant, completion and once-only scoring evidence. '
        'The separate trajectory archive contains all original benchmark requests, responses and outcomes.\n\n'
        'Scorer target values, model weights, credentials and installed runtime environments are excluded. '
        'Configuration files preserve original source paths and hashes: relocation is required to reproduce '
        'the filesystem layout, and scorer references must be obtained separately from their pinned release. '
        'This does not reproduce trained DeepFRI/ProtST heads or its PDB-modeled subset. '
        'No model calls or scoring attempts are made by export/publication.\n').encode()
    archive.parent.mkdir(parents=True, exist_ok=True)
    temporary = archive.with_suffix('.tmp')
    with tarfile.open(temporary,'w:gz') as tar:
        for name in sorted(pairs):
            tar.add(pairs[name],arcname=name,recursive=False)
        info = tarfile.TarInfo('README.txt');info.size=len(readme)
        tar.addfile(info,io.BytesIO(readme))
    scanner.scan_file(temporary)
    temporary.replace(archive)
    scanner.scan_file(archive)
    document = {'schema_version':1,'run_id':RUN,'task_id':'P14',
        'captured_at_pacific':datetime.now(ZoneInfo('America/Los_Angeles')).isoformat(),
        'archive_sha256':sha(archive),'archive_bytes':archive.stat().st_size,'member_count':len(pairs)+1,
        'files_sha256':digests,'readme_sha256':hashlib.sha256(readme).hexdigest(),
        'prediction_lock_sha256':lock_sha,'score_sha256':sha(folder/'scores.json'),
        'continuation_manifest_sha256':CONTINUATION_SHA,
        'full_denominator':3416,'fixed_class_count':489,'reference_labels_included':False,
        'model_weights_included':False,'credentials_included':False,'runtime_environment_included':False,
        'existing_archives_modified':False,'new_inference_calls':0,'new_scoring_attempts':0}
    with receipt.open('x') as handle:
        json.dump(document,handle,indent=2,sort_keys=True);handle.write('\n')
    return archive, receipt


if __name__ == '__main__':
    export_score_and_trajectory()
    archive, receipt = export()
    print(json.dumps({'archive':str(archive.relative_to(ROOT)), 'manifest':str(receipt.relative_to(ROOT)),
        'archive_sha256':sha(archive),'new_model_calls':0,'new_scoring_calls':0}))
