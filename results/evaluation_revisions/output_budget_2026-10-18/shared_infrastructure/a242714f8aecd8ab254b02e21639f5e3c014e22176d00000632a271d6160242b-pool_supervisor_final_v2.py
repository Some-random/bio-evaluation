"""Persist reviewed batch uploads and deterministic CPU aggregation.

Only the explicit registry is followed. This program does not submit inference,
restart generation, change benchmark inputs, or upload environments/weights.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import fcntl
import hashlib
import importlib.util
import json
import math
import os
from pathlib import Path
import shutil
import signal
import subprocess
import sys
import tarfile
import time
import urllib.error
import urllib.parse

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
CHECKOUT = HERE / 'upload_checkout'
TAG = 'remaining-evaluations-2026-10-16-trajectories'
REPOSITORY = 'Some-random/bio-evaluation'
METADATA = ('run_manifest.json', 'progress.json', 'completion.json', 'scores.json',
            'per_case_scores.json', 'metrics.csv', 'server_identity.json', 'execution_environment.json',
            'context_check.json', 'slurm_worker_status.json', 'scoring_output_lock.json',
            'predictions_lock.json', 'aggregate_manifest.json', 'artifact_audit.json',
            'source_shard_manifest.json')
STOP = False


def module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    result = importlib.util.module_from_spec(spec); spec.loader.exec_module(result)
    return result


worker = module('pool_worker_validation', HERE / 'pool_worker.py')
helpers = module('remaining_upload_git_helpers', ROOT / '.local/litqa2_replay/incremental_upload.py')
remote = module('remaining_upload_api_helpers', ROOT / '.local/litqa2_replay/parallel_upload.py')
helpers.CHECKOUT = CHECKOUT


def stamp():
    return datetime.now(timezone.utc).isoformat()


def read(path):
    return json.loads(Path(path).read_text())


def save(path, value):
    worker.write(path, value)


def git(*args, **kwargs):
    kwargs.setdefault('cwd', CHECKOUT)
    return helpers.git(*args, **kwargs)


def copy_changed(source, destination):
    if not source.is_file():
        return False
    destination.parent.mkdir(parents=True, exist_ok=True)
    if destination.is_file() and worker.sha(source) == worker.sha(destination):
        return False
    shutil.copyfile(source, destination)
    return True


def validate_registry(registry):
    runs = {}
    plans = []
    for record in registry.get('pool_plans', []):
        path = Path(record['path']).resolve()
        if not path.is_relative_to(HERE) or worker.sha(path) != record['sha256']:
            raise ValueError('Registry pool plan path/hash mismatch')
        plan = read(path)
        for batch in plan['workers']:
            worker.validate_plan(plan, batch['worker_id'])
            for entry in batch['entries']:
                root = Path(entry['project_root']).resolve()
                if not root.is_relative_to(HERE) or entry['run_id'] in runs:
                    raise ValueError('Registry run scope is duplicated or outside project')
                config = worker.entry_path(entry, entry['config_path'])
                if worker.sha(config) != entry['config_sha256']:
                    raise ValueError('Registry config hash mismatch')
                whole_test = entry.get('full_task_native_scoring') is True
                if whole_test and (entry['task_id'] not in {'P12', 'P13', 'P14', 'P15'}
                                   or read(config).get('case_scope') == 'task_shard_only'):
                    raise ValueError('Only declared full DeepFRI tests use the full-test report trigger')
                runs[entry['run_id']] = {'task_id': entry['task_id'], 'run_id': entry['run_id'],
                    'project_root': root, 'config_path': config, 'planned': entry['case_count'],
                    'folder': root / 'results/runs' / entry['run_id'],
                    'kind': 'full_test' if whole_test else 'shard_or_test'}
        plans.append((path, plan))
    for aggregation in registry.get('aggregations', []):
        root = Path(aggregation['project_root']).resolve()
        if not root.is_relative_to(HERE) or aggregation['run_id'] in runs:
            raise ValueError('Aggregate run scope is duplicated or outside project')
        config = root / aggregation['config_path']
        if not config.resolve().is_relative_to(root) or worker.sha(config) != aggregation['config_sha256']:
            raise ValueError('Aggregate configuration hash changed')
        if not set(aggregation['required_run_ids']) <= set(runs):
            raise ValueError('Aggregate has unregistered source runs')
        runs[aggregation['run_id']] = {'task_id': aggregation['task_id'], 'run_id': aggregation['run_id'],
            'project_root': root, 'config_path': config, 'planned': aggregation['case_count'],
            'folder': root / 'results/runs' / aggregation['run_id'], 'kind': 'aggregate'}
    return plans, runs


def initialize(run_ids):
    if not (CHECKOUT / '.git').is_dir():
        CHECKOUT.mkdir(parents=True, exist_ok=True)
        git('init'); git('remote', 'add', 'origin', helpers.URL)
        git('config', 'remote.origin.promisor', 'true')
        git('config', 'remote.origin.partialclonefilter', 'blob:none')
        git('sparse-checkout', 'init', '--no-cone')
        git('sparse-checkout', 'set', '--no-cone', *['/results/runs/' + name + '/' for name in run_ids])
        git('fetch', '--filter=blob:none', '--depth=1', 'origin', 'main')
        git('checkout', '--detach', 'FETCH_HEAD')
    patterns = ['/' + 'results/runs/' + name + '/' for name in run_ids]
    pattern_file = HERE / 'upload_sparse_patterns.json'
    previous = read(pattern_file) if pattern_file.is_file() else []
    if previous != patterns:
        git('sparse-checkout', 'set', '--no-cone', *patterns)
        save(pattern_file, patterns)
    for name, fallback in (('user.name', 'Codex'), ('user.email', 'codex@localhost')):
        value = git('config', '--get', name, cwd=ROOT, allow_failure=True).stdout.strip() or fallback
        git('config', name, value)


def ensure_run_links(runs):
    directory = ROOT / 'results/runs'
    directory.mkdir(parents=True, exist_ok=True)
    for run_id, spec in runs.items():
        link = directory / run_id
        target = spec['folder'].resolve()
        if link.is_symlink():
            if link.resolve() != target:
                raise ValueError('Central run link points elsewhere: ' + run_id)
        elif link.exists():
            raise ValueError('Central run path already exists; refusing overwrite: ' + run_id)
        else:
            link.symlink_to(target, target_is_directory=True)


def refresh_reports(runs):
    contract_path = HERE / 'report_update_contract.json'
    if not contract_path.is_file():
        return {'stage': 'not_configured'}
    contract = read(contract_path)
    source = Path(contract['script']).resolve()
    if source != ROOT / 'scripts/update_results_at_a_glance.py' or worker.sha(source) != contract['sha256']:
        return {'stage': 'blocked_source_hash_changed'}
    state_path = HERE / 'report_update_status.json'
    previous = read(state_path) if state_path.is_file() else {}
    fingerprints = {}
    for name, spec in runs.items():
        folder = spec['folder']
        if spec['kind'] in ('aggregate', 'full_test') and (folder / 'completion.json').is_file() and (folder / 'scores.json').is_file():
            fingerprints[name] = worker.digest({'completion': worker.sha(folder / 'completion.json'),
                                                'scores': worker.sha(folder / 'scores.json')})
    if fingerprints == previous.get('terminal_score_fingerprints', previous.get('aggregate_fingerprints', {})):
        return previous or {'stage': 'waiting_for_completed_aggregate'}
    result = subprocess.run([sys.executable, str(source), '--root', str(ROOT)], cwd=ROOT,
                            capture_output=True, text=True)
    status = {'stage': 'updated' if result.returncode == 0 else 'failed', 'exit_code': result.returncode,
              'updated_at_utc': stamp(), 'script_sha256': contract['sha256'],
              'stdout': result.stdout[-3000:], 'stderr': result.stderr[-3000:]}
    if result.returncode == 0:
        status['terminal_score_fingerprints'] = fingerprints
    save(state_path, status)
    return status


def outcome_status(spec):
    folder = spec['folder']
    completion_path = folder / 'completion.json'
    if not completion_path.is_file():
        return {'terminal': False, 'execution_success': False, 'native_metrics_valid': None}
    completion = read(completion_path)
    success = (completion.get('generation_exit_code') == 0 and completion.get('scoring_exit_code') == 0
               and completion.get('status') not in {'failed', 'failed_or_incomplete'})
    result = {'terminal': True, 'execution_success': success,
              'generation_exit_code': completion.get('generation_exit_code'),
              'scoring_exit_code': completion.get('scoring_exit_code'), 'native_metrics_valid': None}
    if spec['kind'] not in ('aggregate', 'full_test'):
        return result
    scores_path = folder / 'scores.json'
    valid = success and scores_path.is_file()
    reasons = []
    if not valid:
        reasons.append('Execution failed or native score artifact is missing')
    if scores_path.is_file():
        scores = read(scores_path)
        if scores.get('planned') is not None and scores['planned'] != spec['planned']:
            valid = False; reasons.append('Native planned denominator differs from frozen scope')
        if scores.get('full_planned_primary_metrics_valid') is False:
            valid = False; reasons.append('Native scorer reports invalid full-planned primary metrics')
        union = scores.get('full_test_id_union_validation')
        if isinstance(union, dict) and union.get('complete') is False:
            valid = False; reasons.append('Native scorer reports an incomplete test union')
        metrics = scores.get('metrics', {})
        keys = {'P03': ['accuracy'], 'P07': ['spearman'], 'P08': ['spearman'],
                'P12': ['auprc@micro', 'f1_max'], 'P13': ['auprc@micro', 'f1_max'],
                'P14': ['auprc@micro', 'f1_max'], 'P15': ['auprc@micro', 'f1_max'],
                'P16': ['accuracy'],
                'P28': [aspect + suffix for aspect in ('BP', 'MF', 'CC')
                        for suffix in ('_Fmax', '_IA_weighted_Fmax')],
                'P29': ['native_augmented_precision', 'native_augmented_recall',
                        'native_augmented_F1']}.get(spec['task_id'], [])
        if not keys or any(type(metrics.get(key)) not in (int, float)
                           or not math.isfinite(metrics[key]) for key in keys):
            valid = False; reasons.append('A required native primary metric is missing, undefined or nonfinite')
    result.update(native_metrics_valid=bool(valid), native_metric_issues=reasons)
    return result


def release(part=None):
    cursor_path = HERE / 'upload_release_cursor.json'
    if part is None:
        part = read(cursor_path).get('part', 1) if cursor_path.is_file() else 1
    if type(part) is not int or part < 1:
        raise ValueError('Invalid trajectory release part')
    tag = TAG if part == 1 else TAG + '-part' + f'{part:03d}'
    base = 'https://api.github.com/repos/' + REPOSITORY + '/releases'
    try:
        record = remote.api(base + '/tags/' + tag)
    except urllib.error.HTTPError as error:
        if error.code != 404:
            raise
        record = remote.api(base, 'POST', {'tag_name': tag, 'target_commitish': 'main',
            'draft': False, 'prerelease': True, 'name': 'Remaining evaluation trajectories' + (f' part {part}' if part > 1 else ''),
            'body': 'Incremental private backup of reviewed frozen evaluation runs. Assets preserve complete original request/response JSON, including reasoning and failures. Case indexes and SHA256 manifests link every archived member. No model weights or credentials.'})
    assets = {}
    page = 1
    while True:
        values = remote.api(record['assets_url'] + f'?per_page=100&page={page}')
        assets.update({asset['name']: asset for asset in values})
        if len(values) < 100:
            break
        page += 1
    record['_part'] = part
    save(cursor_path, {'part': part, 'tag': tag, 'release_id': record['id'], 'updated_at_utc': stamp()})
    return record, assets


def archive_batch(run_id, items, release_record, assets, destination):
    signature = worker.digest([{k: item[k] for k in ('filename', 'request_sha256', 'response_sha256')} for item in items])
    name = run_id + '-trajectories-' + signature[:20] + '.tar.gz'
    archive = HERE / 'upload_batches' / run_id / name
    archive.parent.mkdir(parents=True, exist_ok=True)
    if not archive.exists():
        temp = archive.with_suffix('.tmp')
        with tarfile.open(temp, 'w:gz', compresslevel=3) as handle:
            for item in items:
                for kind in ('request', 'response'):
                    if item[kind + '_path'] is not None:
                        handle.add(item[kind + '_path'], arcname=kind + 's/' + item['filename'], recursive=False)
        temp.replace(archive)
    checksum = worker.sha(archive)
    manifest_path = destination / 'trajectory_batches' / (name + '.json')
    if manifest_path.is_file():
        previous = read(manifest_path)
        if (previous.get('archive_sha256') == checksum and previous.get('archive_bytes') == archive.stat().st_size
                and previous.get('run_id') == run_id):
            return previous['cases']
    asset = assets.get(name)
    if asset is None:
        # GitHub limits a release to 1,000 assets. Leave headroom and advance
        # before each new upload; existing archive URLs remain unchanged.
        while len(assets) >= 900:
            next_record, next_assets = release(release_record['_part'] + 1)
            release_record.clear(); release_record.update(next_record)
            assets.clear(); assets.update(next_assets)
        target = release_record['upload_url'].split('{', 1)[0] + '?name=' + urllib.parse.quote(name)
        asset = remote.api(target, 'POST', binary=archive); assets[name] = asset
    if asset['size'] != archive.stat().st_size or (asset.get('digest') and asset['digest'] != 'sha256:' + checksum):
        raise RuntimeError('Remote trajectory archive integrity mismatch')
    result = []
    for item in items:
        result.append({k: v for k, v in item.items() if not k.endswith('_path')})
        result[-1].update(asset=asset['browser_download_url'], archive_sha256=checksum,
                          request_member='requests/' + item['filename'],
                          response_member=('responses/' + item['filename']) if item['response_path'] else None)
    manifest = {'run_id': run_id, 'asset': asset['browser_download_url'], 'asset_id': asset['id'],
        'archive_sha256': checksum, 'archive_bytes': archive.stat().st_size,
        'server_digest': asset.get('digest'), 'raw_request_response_json_preserved': True, 'cases': result}
    save(manifest_path, manifest)
    return result


def new_trajectories(source, uploaded, terminal):
    request_dir = source / 'requests'; response_dir = source / 'responses'
    files = sorted(request_dir.glob('*.json')) if terminal else sorted(response_dir.glob('*.json'))
    result = []
    for file in files:
        filename = file.name
        request = request_dir / filename; response = response_dir / filename
        if filename in uploaded:
            continue
        if not request.is_file() or (not terminal and not response.is_file()):
            continue
        req = read(request); resp = read(response) if response.is_file() else None
        if req['request_sha256'] != worker.digest(req['payload']):
            raise ValueError('Request payload hash mismatch')
        if resp and (resp['request_sha256'] != req['request_sha256'] or resp['case_id'] != req['case_id']):
            raise ValueError('Request/response provenance mismatch')
        result.append({'filename': filename, 'case_id': req['case_id'], 'request_path': request,
            'response_path': response if resp else None, 'request_sha256': worker.sha(request),
            'response_sha256': worker.sha(response) if resp else None,
            'payload_sha256': req['request_sha256'], 'status': resp.get('status') if resp else 'request_without_saved_response'})
    return result


def child_alive(record):
    try:
        fields = Path('/proc/' + str(record['pid']) + '/stat').read_text().rsplit(')', 1)[1].split()
        return fields[0] != 'Z' and fields[19] == record['start_ticks']
    except (OSError, KeyError, IndexError):
        return False


def aggregate_ready(registry, runs):
    status_path = HERE / 'aggregation_status.json'
    status = read(status_path) if status_path.is_file() else {}
    for spec in registry.get('aggregations', []):
        name = spec['name']; dest = runs[spec['run_id']]['folder']; current = status.get(name, {})
        if (dest / 'completion.json').is_file():
            current.update(stage='terminal', completion_sha256=worker.sha(dest / 'completion.json'))
            status[name] = current; continue
        if current.get('stage') == 'running' and child_alive(current):
            continue
        if current.get('stage') in ('running', 'failed'):
            current.update(stage='failed', error='CPU aggregation exited without native completion; inspect its log')
            status[name] = current; continue
        if not all((runs[run]['folder'] / 'completion.json').is_file() for run in spec['required_run_ids']):
            status[name] = {'stage': 'waiting_for_shards'}; continue
        python = Path(spec['python'])
        if not python.is_file():
            status[name] = {'stage': 'waiting_for_scoring_runtime'}; continue
        root = Path(spec['project_root']).resolve()
        for filename, expected in spec['command_files_sha256'].items():
            path = (root / filename).resolve()
            if not path.is_relative_to(root) or worker.sha(path) != expected:
                raise ValueError('Aggregate command source hash mismatch')
        argv = list(spec['argv']); script = (root / argv[0]).resolve()
        if str(script.relative_to(root)) not in spec['command_files_sha256']:
            raise ValueError('Aggregate script is not frozen')
        log_path = HERE / 'logs' / ('aggregate-' + name + '.log')
        log_path.parent.mkdir(parents=True, exist_ok=True)
        with log_path.open('a') as log:
            env = dict(os.environ, PYTHONNOUSERSITE='1', PYTHONDONTWRITEBYTECODE='1', OMP_NUM_THREADS='4', MKL_NUM_THREADS='4')
            for key in ('PYTHONPATH', 'PYTHONHOME', 'VIRTUAL_ENV', 'OPENAI_API_KEY', 'ANTHROPIC_API_KEY'):
                env.pop(key, None)
            extra = worker.extra_pythonpath(spec)
            if extra:
                env['PYTHONPATH'] = os.pathsep.join(extra)
            child = subprocess.Popen([str(python), '-u', str(script), *argv[1:]], cwd=root,
                env=env, stdin=subprocess.DEVNULL, stdout=log, stderr=subprocess.STDOUT, start_new_session=True)
        ticks = Path('/proc/' + str(child.pid) + '/stat').read_text().rsplit(')', 1)[1].split()[19]
        status[name] = {'stage': 'running', 'pid': child.pid, 'start_ticks': ticks,
                        'started_at_utc': stamp(), 'log': str(log_path)}
    save(status_path, status)
    return status


def scheduler_snapshot(plans):
    jobs = []
    for path, plan in plans:
        receipt = path.with_name(path.stem + '.submissions.json')
        if receipt.is_file():
            jobs.extend(row['job_id'] for row in read(receipt).get('jobs', []))
    if not jobs:
        return []
    query = subprocess.run(['squeue', '-h', '-j', ','.join(jobs), '-o', '%i|%T|%R'], capture_output=True, text=True)
    if query.returncode:
        return [{'query_error': 'squeue exit' + str(query.returncode)}]
    rows = []
    seen = set()
    for line in query.stdout.splitlines():
        parts = line.split('|', 2)
        if len(parts) == 3:
            rows.append({'job_id': parts[0], 'state': parts[1], 'node_or_reason': parts[2]}); seen.add(parts[0])
    rows.extend({'job_id': job, 'state': 'not_in_active_queue'} for job in jobs if job not in seen)
    return rows


def cycle(registry_path):
    registry = read(registry_path); plans, runs = validate_registry(registry)
    ensure_run_links(runs)
    scheduler = scheduler_snapshot(plans)
    aggregation = aggregate_ready(registry, runs)
    reports = refresh_reports(runs)
    if not runs:
        return {'stage': 'waiting_for_frozen_plans', 'updated_at_utc': stamp(), 'all_complete': False}
    privacy = helpers.confirm_private(); initialize(runs)
    release_record = None; assets = {}; snapshots = {}; changed = False
    for run_id, spec in runs.items():
        source = spec['folder']; destination = CHECKOUT / 'results/runs' / run_id
        index_path = destination / 'trajectory_index.json'
        index = read(index_path) if index_path.is_file() else []
        outcome = outcome_status(spec)
        terminal = outcome['terminal']
        pending = new_trajectories(source, {row['filename'] for row in index}, terminal)
        batches = []; batch = []; size = 0
        for item in pending:
            item_size = item['request_path'].stat().st_size + (item['response_path'].stat().st_size if item['response_path'] else 0)
            if batch and (len(batch) >= 100 or size + item_size > 20 * 1024 * 1024):
                batches.append(batch); batch = []; size = 0
            batch.append(item); size += item_size
        if batch:
            batches.append(batch)
        for batch in batches:
            if release_record is None:
                release_record, assets = release()
            index.extend(archive_batch(run_id, batch, release_record, assets, destination)); changed = True
        if index or terminal:
            destination.mkdir(parents=True, exist_ok=True)
            if batches:
                save(index_path, sorted(index, key=lambda row: row['filename']))
            changed |= copy_changed(spec['config_path'], destination / 'frozen_config.json')
            config = read(spec['config_path'])
            dependencies = dict(config.get('frozen_files_sha256', {}))
            for key in ('shard_plan_file', 'aggregate_config_file', 'execution_approval_file'):
                if config.get(key):
                    path = spec['project_root'] / config[key]
                    if path.is_file():
                        dependencies[config[key]] = worker.sha(path)
            # Gate approvals are intentionally not in the generation file hash set
            # when that would create a circular plan/config digest dependency.
            extra_files = ['configs/local_model.json', config.get('serving_config_file')]
            approval_names = {'P28': 'configs/local_bioreason_execution_approval.json',
                              'P29': 'configs/local_posttrain_protein_execution_approval.json',
                              'P16': 'configs/local_reaction_execution_approval.json'}
            extra_files.append(approval_names.get(spec['task_id']))
            for name in extra_files:
                if name:
                    path = (spec['project_root'] / name).resolve()
                    if path.is_relative_to(spec['project_root']) and path.is_file():
                        dependencies[name] = worker.sha(path)
            manifest = {}
            for relative, expected in dependencies.items():
                source_file = (spec['project_root'] / relative).resolve()
                if not source_file.is_relative_to(spec['project_root']) or not source_file.is_file():
                    raise ValueError('Frozen reproduction dependency is missing or unsafe')
                copied = (relative.startswith(('scripts/', 'configs/', 'reports/', 'sources/'))
                          and source_file.stat().st_size <= 2 * 1024 * 1024
                          and source_file.suffix in {'.py', '.json', '.md', '.txt', '.toml', '.yaml', '.yml', '.sh', '.tsv', '.csv'})
                if copied:
                    if worker.sha(source_file) != expected:
                        raise ValueError('Frozen reproduction dependency changed: ' + relative)
                    changed |= copy_changed(source_file, destination / 'frozen_files' / relative)
                manifest[relative] = {'sha256': expected, 'bytes': source_file.stat().st_size,
                                      'browsable_copy': ('frozen_files/' + relative) if copied else None}
            manifest_path = destination / 'frozen_dependencies_manifest.json'
            if not manifest_path.is_file() or read(manifest_path) != manifest:
                save(manifest_path, manifest); changed = True
            for filename in METADATA:
                changed |= copy_changed(source / filename, destination / filename)
        snapshot = {'task_id': spec['task_id'], 'run_id': run_id, 'kind': spec['kind'],
            'uploaded_trajectories': len(index), 'planned': spec['planned'], **outcome,
            'complete_raw_coverage': terminal and len(index) == spec['planned'],
            'github_url': 'https://github.com/' + REPOSITORY + '/tree/main/results/runs/' + run_id}
        snapshots[run_id] = snapshot
        if index or terminal:
            old = read(destination / 'upload_snapshot.json') if (destination / 'upload_snapshot.json').is_file() else None
            if snapshot != old:
                save(destination / 'upload_snapshot.json', snapshot); changed = True
                (destination / 'README.md').write_text('# ' + spec['task_id'] + ' evaluation artifacts\n\n'
                    + str(len(index)) + '/' + str(spec['planned']) + ' raw trajectories archived. '
                    + ('Execution is terminal.\n\n' if terminal else 'Incremental snapshot; execution is ongoing.\n\n')
                    + '[Case index](trajectory_index.json) · [Archive manifests](trajectory_batches) · [Frozen config](frozen_config.json)\n\n'
                    + 'Private release assets preserve original full request and response JSON, including reasoning fields, usage, errors, and input text. Extract the named members listed in the case index. SHA256 hashes cover archives and individual files. Scores and native completion records are copied when available.\n')
    if changed:
        for run_id in runs:
            relative = 'results/runs/' + run_id
            if (CHECKOUT / relative).exists():
                git('add', '-f', '--', relative)
        staged = git('diff', '--cached', '--name-only').stdout.splitlines()
        if any(not any(path.startswith('results/runs/' + name + '/') for name in runs) for path in staged):
            raise ValueError('Upload staged an unregistered path')
        if staged:
            git('commit', '-m', 'Back up frozen remaining-evaluation trajectories')
    # A prior cycle may have committed successfully but failed its network push.
    # Retry unpublished commits even when no new trajectories appeared this cycle.
    ahead = int(git('rev-list', '--count', 'refs/remotes/origin/main..HEAD').stdout.strip())
    if ahead:
        result = git('push', 'origin', 'HEAD:refs/heads/main', allow_failure=True)
        if result.returncode:
            git('fetch', '--filter=blob:none', 'origin', 'main')
            git('rebase', 'FETCH_HEAD'); git('push', 'origin', 'HEAD:refs/heads/main')
    all_terminal = all(row['terminal'] for row in snapshots.values())
    primary = [row for row in snapshots.values() if row['kind'] in ('aggregate', 'full_test')]
    all_success = bool(primary) and all(row['native_metrics_valid'] for row in primary) and all(row['execution_success'] for row in snapshots.values())
    done = bool(registry.get('sealed')) and all_terminal
    summary = {'stage': ('completed' if all_success else 'terminal_with_failures') if done else 'watching',
        'updated_at_utc': stamp(), 'repository_private_verified': privacy['private'],
        'commit_sha': git('rev-parse', 'HEAD').stdout.strip(), 'runs': snapshots, 'aggregations': aggregation,
        'scheduler': scheduler, 'report_update': reports,
        'registry_sealed': bool(registry.get('sealed')), 'all_terminal': all_terminal,
        'all_successful_native_metrics': all_success, 'all_complete': done and all_success}
    save(HERE / 'upload_status.json', summary)
    return summary


def main(args):
    lock = (HERE / 'supervisor.lock').open('a')
    if args.ready_file:
        ready_file = args.ready_file.resolve()
        if not ready_file.is_relative_to(HERE):
            raise ValueError('Readiness marker must be local to this supervisor')
        save(ready_file, {'stage': 'waiting_for_handoff_lock', 'pid': os.getpid(),
                         'python': sys.executable, 'slurm_job_id': os.environ.get('SLURM_JOB_ID'),
                         'started_at_utc': stamp()})
    fcntl.flock(lock, fcntl.LOCK_EX | (0 if args.wait_for_lock else fcntl.LOCK_NB))
    def stop(signum, frame):
        global STOP
        STOP = True
    signal.signal(signal.SIGTERM, stop); signal.signal(signal.SIGINT, stop)
    while not STOP:
        try:
            status = cycle(args.registry)
        except Exception as error:
            status = {'stage': 'retry_pending', 'error': f'{type(error).__name__}: {error}',
                      'updated_at_utc': stamp(), 'all_complete': False}
        status.update(supervisor_pid=os.getpid(), supervisor_start_ticks=Path('/proc/self/stat').read_text().rsplit(')', 1)[1].split()[19])
        save(HERE / 'supervisor_status.json', status)
        print(json.dumps({key: status[key] for key in ('stage', 'updated_at_utc', 'all_complete')}), flush=True)
        if (status.get('registry_sealed') and status.get('all_terminal')) or args.once:
            break
        for _ in range(12):
            if STOP:
                break
            time.sleep(5)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--registry', type=Path, default=HERE / 'supervisor_plan.json')
    parser.add_argument('--once', action='store_true')
    parser.add_argument('--wait-for-lock', action='store_true')
    parser.add_argument('--ready-file', type=Path)
    main(parser.parse_args())
