"""Additive native scoring of an explicitly mixed historical4k/prospective16k union.

No inference and no prediction repair. Original raw files, configurations and
scores remain unchanged. Only native payload validation selects the frozen
per-case output budget; original parser and metric implementations run intact.
"""
from __future__ import annotations

import argparse
from collections import Counter
from contextlib import contextmanager
import copy
import fcntl
import importlib.util
import json
import os
from pathlib import Path
import subprocess
import sys

REPOSITORY = Path(__file__).resolve().parents[3]
BASE_PATH = REPOSITORY / '.local/shared_vllm_saturation_2026-10-18/shared_vllm_scoring.py'
BASE_SHA256 = 'fa7675cb0997cf3171b61954f24c1f4124e231506b56d9be33c93d8de6506d18'
import hashlib
if hashlib.sha256(BASE_PATH.read_bytes()).hexdigest() != BASE_SHA256:
    raise RuntimeError('Frozen historical scoring adapter changed')
_spec = importlib.util.spec_from_file_location('mixed_budget_original_scoring', BASE_PATH)
base = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(base)

ScoringError, Pending = base.ScoringError, base.Pending
read, file_sha, digest = base.read, base.file_sha, base.digest
CONDITION = 'MIXED_BUDGET_4K16K_CONTINUATION'
SUPPORTED = {'P07', 'P08', 'P12', 'P13', 'P14', 'P15', 'P16'}


def module(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result


def pinned(path, expected):
    path = Path(path).resolve()
    if file_sha(path) != expected:
        raise ScoringError('Pinned mixed-budget metadata/code changed: ' + str(path))
    return read(path)


def case_name(case):
    return digest([case['task'], case['variant'], case['case_id']]) + '.json'


def actual_budget_condition(budgets):
    values = set(budgets.values())
    if values == {4096}:
        return 'RETAINED_4K_COMPLETE_UNDER_BUDGET_REVISION'
    if values == {16384}:
        return 'PROSPECTIVE_16K_FULL_TASK'
    if values == {4096, 16384}:
        return CONDITION
    raise ScoringError('Require nonempty exact4096/16384 budget cohorts')


def revision_index(spec):
    result = {}
    for binding in spec['revision_plans']:
        plan = pinned(binding['path'], binding['sha256'])
        if (plan.get('schema_version') != 1 or plan.get('condition') != CONDITION
                or plan.get('execution_authorized') is not True
                or plan.get('output_budget') != 16384 or plan.get('original_output_budget') != 4096
                or plan.get('retries_or_resampling_of_previously_executed_cases') is not False
                or plan.get('whole_task_metrics_require_original4k_and_new16k_union') is not True
                or plan.get('code_sha256') != spec['revision_runner_sha256']):
            raise ScoringError('Revision plan changed its prospective-only mixed-budget contract')
        if file_sha(spec['revision_runner_file']) != spec['revision_runner_sha256']:
            raise ScoringError('Actual 16k producer code changed')
        for item in plan['runs']:
            identity = (str(Path(item['entry']['project_root']).resolve()), item['entry']['run_id'])
            if identity in result:
                raise ScoringError('Source run appears in multiple revision plans')
            result[identity] = (plan, binding, item)
    return result


def closed_checkpoint_index(spec):
    result = {}
    for binding in spec.get('closed_4k_checkpoints', []):
        run_id = binding['run_id']
        if run_id in result:
            raise ScoringError('Duplicate closed historical checkpoint')
        checkpoint = pinned(binding['path'], binding['sha256'])
        if checkpoint.get('original_source_run_id') != run_id:
            raise ScoringError('Closed checkpoint belongs to another source')
        result[run_id] = binding
    return result


def validate_checkpoint(root, cfg, cases, folder, item, validator):
    checkpoint = pinned(item['parent_checkpoint']['path'], item['parent_checkpoint']['sha256'])
    selected = item['selected_case_ids']
    eligible = [case['case_id'] for case in cases if case['case_id'] in set(selected)]
    if (checkpoint.get('condition') != CONDITION or checkpoint.get('ambiguous_files') != []
            or checkpoint.get('source_case_contract_sha256') != digest(cases)
            or checkpoint.get('ordered_pending_case_ids') != selected
            or item.get('ordered_case_ids_sha256') != digest(selected)
            or item.get('case_scope') != 'all_never_dispatched_at_clean_pause'
            or Path(checkpoint['parent_run_directory']).resolve() != folder
            or eligible != selected or len(selected) != len(set(selected))
            or checkpoint.get('selection_uses_correctness_or_finish_reason') is not False):
        raise ScoringError('16k cohort is not the exact clean never-dispatched selection')
    for name, expected in checkpoint['retained_files_sha256'].items():
        if file_sha(base.project_path(folder, name)) != expected:
            raise ScoringError('An immutable historical 4k artifact changed')
    for case in cases:
        name = case_name(case)
        if case['case_id'] in set(selected):
            if any((folder / kind / name).exists() for kind in
                   ('requests', 'responses', 'shared_vllm_dispatch', 'shared_vllm_saturation_dispatch')):
                raise ScoringError('A previously claimed case entered the 16k cohort')
        elif not (folder / 'responses' / name).exists():
            raise ScoringError('The cohort omitted a historical missing or ambiguous case')
    proof = validator(folder, cfg, cases, require_terminal=False)
    if proof != checkpoint['parent_proof'] or proof.get('all_saved_responses_verified') is not True:
        raise ScoringError('Historical provenance no longer matches its frozen clean pause')
    return checkpoint, {**proof, 'kind': 'shared_serving_amendment'}


def validate_new_cohort(root, cfg, cases, folder, plan, binding, item):
    selected = set(item['selected_case_ids'])
    cohort = [case for case in cases if case['case_id'] in selected]
    output = Path(item['output_directory']).resolve()
    if output == folder or output.name != cfg['run_id'] + '_output16384_v1':
        raise ScoringError('Revised outputs do not have their own run namespace')
    done_path = output / 'generation_completion.json'
    if not done_path.is_file():
        raise Pending('Prospective 16k cohort is not terminal: ' + cfg['run_id'])
    revised = copy.deepcopy(cfg)
    if revised['generation']['max_tokens'] != 4096:
        raise ScoringError('Historical output budget differs from exactly 4096')
    revised['generation']['max_tokens'] = 16384
    manifest = read(output / 'run_manifest.json')
    if (manifest.get('condition') != CONDITION or manifest.get('plan_sha256') != binding['sha256']
            or manifest.get('source_entry') != item['entry']
            or manifest.get('configuration') != revised or manifest.get('original_configuration') != cfg
            or manifest.get('planned_cases') != len(cohort)
            or manifest.get('ordered_cases_sha256') != digest(cohort)
            or manifest.get('parent_checkpoint') != item['parent_checkpoint']
            or Path(manifest['parent_run_directory']).resolve() != folder
            or manifest.get('original_artifacts_modified') is not False
            or manifest.get('model_outcome_based_selection') is not False):
        raise ScoringError('The new producer manifest differs from its approved cohort')
    hashes, states = base.validate_raw(root, revised, cohort, output)
    endpoints = {e['endpoint_id']: e for e in plan['endpoints']}
    expected_names = {case_name(case) for case in cohort}
    if {p.name for p in (output / 'dispatch').glob('*.json')} != expected_names:
        raise ScoringError('Revised dispatch archive does not cover exactly its cohort')
    for case in cohort:
        name = case_name(case)
        request = read(output / 'requests' / name)
        response = read(output / 'responses' / name)
        receipt = read(output / 'dispatch' / name)
        endpoint = endpoints.get(receipt.get('endpoint_id'))
        if (response.get('condition') != CONDITION or receipt.get('condition') != CONDITION
                or receipt.get('plan_sha256') != binding['sha256']
                or receipt.get('case_id') != case['case_id']
                or receipt.get('output_budget') != 16384
                or receipt.get('request_sha256') != request['request_sha256']
                or receipt.get('response_sha256') != file_sha(output / 'responses' / name)
                or endpoint is None
                or receipt.get('server_identity_sha256') != endpoint['server_identity_sha256']):
            raise ScoringError('New response lacks its exact budget/server/dispatch provenance')
        identity_path = endpoint.get('server_identity_file') or endpoint.get('identity_file')
        if identity_path and file_sha(identity_path) != endpoint['server_identity_sha256']:
            raise ScoringError('New serving identity record changed')
    done = read(done_path)
    if (done.get('condition') != CONDITION or done.get('plan_sha256') != binding['sha256']
            or done.get('planned') != len(cohort) or done.get('statuses') != states
            or done.get('retry_or_resampling') is not False
            or sum(states.values()) != len(cohort)
            or any(state in states for state in ('not_dispatched', 'interrupted_unknown_completion'))
            or done.get('generation_exit_code') != (0 if states.get('completed', 0) == len(cohort) else 1)):
        raise ScoringError('New completion does not describe the complete frozen cohort')
    return output, hashes, states


def validate_sources(spec, validator=None):
    root = Path(spec['project_root']).resolve()
    task = spec['task_id']
    if task not in SUPPORTED or spec['scorer_file'] != base.SCORERS[task]:
        raise ScoringError('Unsupported mixed-budget task/native scorer pairing')
    full = base.checked_config(root, spec['full_config_file'], spec['full_config_sha256'])
    if (full['approved_task_ids'] != [task]
            or full['generation']['max_tokens'] != 4096
            or file_sha(root / spec['scorer_file']) != spec['scorer_sha256']
            or full['frozen_files_sha256'].get(spec['scorer_file']) != spec['scorer_sha256']):
        raise ScoringError('Original native full configuration/scorer changed')
    full_cases = base.input_cases(root, full)
    full_runner = base.load_frozen_runner(root, full)
    full_requests = {case_name(c): full_runner.request_record(c, full) for c in full_cases}
    revisions = revision_index(spec)
    closed = closed_checkpoint_index(spec)
    all_cases, sources, slots, budgets, identities = [], [], {}, {}, set()
    for source in spec['sources']:
        cfg = base.checked_config(root, source['config_file'], source['config_sha256'])
        cases = base.input_cases(root, cfg)
        if any(cfg.get(k) != full.get(k) for k in ('model', 'model_revision', 'checkpoint_precision',
                'generation', 'variant', 'scorer_reference_file', 'scorer_reference_sha256')):
            raise ScoringError('Source biology, model, sampling or reference recipe differs')
        runner = base.load_frozen_runner(root, cfg)
        for case in cases:
            name = case_name(case)
            if name in identities or runner.request_record(case, cfg) != full_requests.get(name):
                raise ScoringError('Source case overlaps or differs from the original full prompt')
            identities.add(name)
        folder = base.generation_folder(root, cfg, source)
        revision = revisions.get((str(root), cfg['run_id']))
        if revision:
            plan, binding, item = revision
            if item['entry']['config_sha256'] != source['config_sha256']:
                raise ScoringError('Revision is attached to a different frozen source config')
            checkpoint, proof = validate_checkpoint(root, cfg, cases, folder, item,
                validator or base.resume_validator())
            new_folder, new_hashes, new_states = validate_new_cohort(root, cfg, cases, folder, plan, binding, item)
            selected = set(item['selected_case_ids'])
        else:
            selected = set()
            if cfg['run_id'] in closed:
                binding = closed[cfg['run_id']]
                item = {'selected_case_ids': [], 'ordered_case_ids_sha256': digest([]),
                    'case_scope': 'all_never_dispatched_at_clean_pause',
                    'parent_checkpoint': {'path': binding['path'], 'sha256': binding['sha256']}}
                checkpoint, proof = validate_checkpoint(root, cfg, cases, folder, item,
                    validator or base.resume_validator())
            elif (folder / 'shared_vllm_amendment.json').exists():
                proof = (validator or base.resume_validator())(folder, cfg, cases, require_terminal=True)
                proof = {**proof, 'kind': 'shared_serving_amendment'}
            else:
                proof = base.validate_legacy(folder, cfg, cases, source['config_sha256'])
            new_hashes, new_states = {}, {}
        base.validate_fork_identity(root, cfg, folder, proof)
        old_hashes, old_states = base.validate_raw(root, cfg, cases, folder)
        if (folder / 'scoring_output_lock.json').exists():
            lock = read(folder / 'scoring_output_lock.json')
            if lock.get('contract_sha256') != digest(lock.get('files_sha256')):
                raise ScoringError('Historical native pre-label output lock changed')
            for name, expected in lock['files_sha256'].items():
                if name in old_hashes and old_hashes[name] != expected:
                    raise ScoringError('Historical locked output/missing slot changed')
        for case in cases:
            name = case_name(case)
            is_new = case['case_id'] in selected
            budget = 16384 if is_new else 4096
            budgets[name] = budget
            location = new_folder if is_new else folder
            hashes = new_hashes if is_new else old_hashes
            for kind in ('requests', 'responses'):
                relative = kind + '/' + name
                slots[relative] = {'source': str(location / relative), 'sha256': hashes[relative]}
        all_cases.extend(cases)
        sources.append({**source, 'run_id': cfg['run_id'], 'case_count': len(cases),
            'generation_folder': str(folder), 'historical_provenance': proof,
            'historical_raw_files_sha256': old_hashes, 'historical_states': old_states,
            'revision': {'plan': binding, 'item': item, 'states': new_states} if revision else None})
    if all_cases != full_cases or len(identities) != len(full_cases):
        raise ScoringError('Mixed source union is not the exact ordered original full test')
    if full.get('full_test_case_count', full.get('planned', len(full_cases))) != len(full_cases):
        raise ScoringError('Original full denominator differs')
    actual_budget_condition(budgets)
    union = {'complete': True, 'union_matches_full_test_ids': True,
        'expected_test_case_count': len(full_cases), 'unique_observed_case_count': len(identities),
        'missing_case_count': 0, 'extra_case_count': 0, 'duplicate_case_count': 0}
    return root, full, full_cases, sources, slots, budgets, union


def payload_selector(original, runner, budgets):
    def expected_payload(case, settings):
        name = case_name(case)
        if name not in budgets:
            raise ScoringError('Native scorer encountered an unplanned case')
        selected = copy.deepcopy(original)
        selected['generation']['max_tokens'] = budgets[name]
        return runner.request_record(case, selected)['payload']
    return expected_payload


def invoke_native(spec, config_path, folder):
    """Run in the pinned native CPU interpreter; leave source code untouched."""
    root = Path(spec['project_root']).resolve()
    cfg = read(config_path)
    budget_pin = cfg['mixed_budget_scoring']['per_case_budget_map']
    budgets = pinned(budget_pin['path'], budget_pin['sha256'])['budgets_by_raw_filename']
    original = base.checked_config(root, spec['full_config_file'], spec['full_config_sha256'])
    path = root / spec['scorer_file']
    if file_sha(path) != spec['scorer_sha256']:
        raise ScoringError('Native scorer changed before invocation')
    sys.path.insert(0, str(root / 'scripts'))
    native = module(path, 'mixed_budget_native_' + spec['task_id'].lower())
    native.ROOT = root
    native.expected_payload = payload_selector(original, base.load_frozen_runner(root, original), budgets)
    if spec['task_id'] in base.DEEPFRI:
        result = native.score(folder, root=root, config_path=config_path)
    else:
        result = native.score(folder)
    # Save the original native summary as produced, then add protocol metadata
    # to the derived result only. No scalar metric or prediction is replaced.
    base.immutable_json(folder / 'native_scores_unmodified.json', result)
    summary = copy.deepcopy(result)
    actual_condition = actual_budget_condition(budgets)
    summary.update(native_protocol_variant=result.get('protocol_variant'),
        protocol_variant=original['variant'] + '__' + actual_condition,
        generation_budget_condition=actual_condition, execution_amendment_condition=CONDITION,
        generation={'max_tokens': next(iter(set(budgets.values()))) if len(set(budgets.values())) == 1 else None,
            'output_budget_counts': dict(Counter(map(str, budgets.values())))},
        full_test_id_union_validation=cfg['mixed_budget_scoring']['full_test_id_union_validation'],
        native_parser_and_metric_implementation_unchanged=True,
        original_case_denominator_unchanged=True, prior_outputs_rerun=False)
    summary['comparison_to_paper'] = str(result.get('comparison_to_paper') or '') + (
        f' Output-budget condition: {actual_condition}; '
        f"{sum(value == 4096 for value in budgets.values())} historical cases retain4096 tokens and "
        f"{sum(value == 16384 for value in budgets.values())} clean never-dispatched cases receive16384 tokens. "
        'Original invalid/truncated cases remain included. '
        + ('This is not a uniform16k evaluation or a matched budget comparison.'
           if actual_condition == CONDITION else 'The actual single-budget cohort is recorded explicitly.'))
    temporary = folder / 'scores.json.tmp'
    temporary.write_text(json.dumps(summary, ensure_ascii=False, indent=2, allow_nan=False) + '\n')
    temporary.replace(folder / 'scores.json')
    return summary


@contextmanager
def source_locks(spec):
    root = Path(spec['project_root']).resolve()
    revisions = revision_index(spec)
    paths = set()
    for source in spec['sources']:
        cfg = base.checked_config(root, source['config_file'], source['config_sha256'])
        paths.add(base.generation_folder(root, cfg, source) / 'worker.lock')
        item = revisions.get((str(root), cfg['run_id']))
        if item:
            paths.add(Path(item[2]['output_directory']) / 'worker.lock')
    handles = []
    try:
        for path in sorted(paths):
            if not path.parent.is_dir():
                raise Pending('Generation source has not started: ' + str(path.parent))
            handle = path.open('a')
            try:
                fcntl.flock(handle, fcntl.LOCK_EX | fcntl.LOCK_NB)
            except BlockingIOError:
                handle.close()
                raise Pending('Generation source remains active: ' + str(path.parent))
            handles.append(handle)
        yield
    finally:
        for handle in handles:
            handle.close()


def score_spec(spec, validate_only=False, validator=None, run_command=subprocess.run):
    root = Path(spec['project_root']).resolve()
    original = base.checked_config(root, spec['full_config_file'], spec['full_config_sha256'])
    original_folder = root / 'results/runs' / original['run_id']
    if (original_folder / 'completion.json').is_file():
        existing = base.existing_completion(original_folder, spec['full_config_sha256'])
        manifest = read(original_folder / 'run_manifest.json')
        scores = read(original_folder / 'scores.json')
        full_cases = base.input_cases(root, original)
        if (scores.get('planned') == len(full_cases) and scores.get('completed') == len(full_cases)
                and manifest.get('case_contract_sha256') == digest(full_cases)
                and manifest.get('planned_cases') == len(full_cases)):
            return {**existing, 'state': 'existing_native4k_completed_unchanged',
                'generation_budget_condition': 'RETAINED_4K_COMPLETE_UNDER_BUDGET_REVISION'}
    output = root / 'results/runs' / spec['output_run_id']
    output.mkdir(parents=True, exist_ok=True)
    if output.name == read(root / spec['full_config_file'])['run_id']:
        raise ScoringError('Mixed scoring must use a separate derived result directory')
    with (output / 'mixed_scoring_worker.lock').open('a') as lock:
        fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        if (output / 'completion.json').exists():
            done = read(output / 'completion.json')
            if (done.get('scoring_exit_code') != 0 or done.get('spec_sha256') != digest(spec)
                    or done.get('scores_sha256') != file_sha(output / 'scores.json')):
                raise ScoringError('Existing mixed score failed or changed; no retry')
            return {'state': 'existing_completed_unchanged', 'run_id': output.name}
        if (output / 'native_scorer_invocation.json').exists():
            raise ScoringError('Native mixed scorer already attempted; no repeat')
        with source_locks(spec):
            root, original, cases, sources, slots, budgets, union = validate_sources(spec, validator)
            if validate_only:
                return {'state': 'validated', 'planned': len(cases), 'union': union,
                    'output_budget_counts': dict(Counter(map(str, budgets.values()))), 'labels_read': False}
            budget_path = output / 'per_case_budget_map.json'
            base.immutable_json(budget_path, {'condition': CONDITION, 'budgets_by_raw_filename': budgets,
                'selection': 'All cases never dispatched at the clean pause receive16384; all retained historical cases keep4096.'})
            cfg = copy.deepcopy(original)
            cfg.update(run_id=output.name, runner=os.path.relpath(Path(__file__).resolve(), root))
            actual_condition = actual_budget_condition(budgets)
            cfg['generation']['max_tokens'] = next(iter(set(budgets.values()))) if len(set(budgets.values())) == 1 else None
            cfg['frozen_files_sha256'][cfg['runner']] = file_sha(__file__)
            cfg['mixed_budget_scoring'] = {'condition': actual_condition, 'execution_amendment_condition': CONDITION,
                'per_case_budget_map': {'path': str(budget_path), 'sha256': file_sha(budget_path)},
                'original_full_configuration_sha256': spec['full_config_sha256'],
                'original_run_id': original['run_id'], 'native_metrics_and_parsers_unchanged': True,
                'full_test_id_union_validation': union, 'sources': sources}
            config_path = root / 'configs' / (output.name + '.json')
            base.immutable_json(config_path, cfg)
            manifest = {'configuration': cfg, 'configuration_sha256': file_sha(config_path),
                'case_contract_sha256': digest(cases), 'planned_cases': len(cases),
                'runner_sha256': file_sha(__file__), 'runner_role': 'offline_mixed_budget_scoring_bridge',
                'aggregate_only': True, 'generation_budget_condition': actual_condition,
                'solver_tools': [], 'answer_keys_available_to_solver': False, 'model_selection_on_test': False}
            base.immutable_json(output / 'run_manifest.json', manifest)
            for name, slot in slots.items():
                base.install_raw(Path(slot['source']), output / name, slot['sha256'])
            for kind in ('requests', 'responses'):
                if {str(p.relative_to(output)) for p in (output / kind).glob('*.json')} != {
                        name for name, slot in slots.items() if name.startswith(kind + '/') and slot['sha256'] is not None}:
                    raise ScoringError('Derived raw-output union contains missing or extra files')
            output_lock = {'files_sha256': {name: slot['sha256'] for name, slot in slots.items()},
                'per_case_budget_map_sha256': file_sha(budget_path), 'manifest_sha256': file_sha(output / 'run_manifest.json'),
                'spec_sha256': digest(spec), 'all_original_invalid_and_missing_slots_retained': True,
                'labels_read': False, 'native_denominator': len(cases)}
            base.immutable_json(output / 'mixed_budget_output_lock.json', output_lock)
            spec_path = output / 'mixed_scoring_spec.json'
            base.immutable_json(spec_path, spec)
            command = [spec.get('python', sys.executable), '-u', str(Path(__file__).resolve()),
                '--native-only-spec', str(spec_path), '--native-config', str(config_path), '--native-folder', str(output)]
            base.immutable_json(output / 'native_scorer_invocation.json', {'argv': command,
                'started_at_pacific': base.now(), 'native_calls_planned': 1, 'spec_sha256': digest(spec),
                'native_scorer_sha256': spec['scorer_sha256'], 'output_lock_sha256': file_sha(output / 'mixed_budget_output_lock.json')})
            for name, slot in slots.items():
                p = output / name
                if (file_sha(p) if p.exists() else None) != slot['sha256']:
                    raise ScoringError('Derived scoring input changed after locking')
            with (output / 'native_scorer.log').open('x') as log:
                result = run_command(command, cwd=root, env=base.native_environment(spec), stdout=log, stderr=subprocess.STDOUT)
            completion = {'scoring_exit_code': result.returncode, 'generation_exit_code': 0,
                'finished_at_pacific': base.now(), 'condition': actual_condition, 'spec_sha256': digest(spec),
                'configuration_sha256': file_sha(config_path), 'run_manifest_sha256': file_sha(output / 'run_manifest.json'),
                'full_test_id_union_validation': union, 'native_labels_and_denominator_unchanged': True,
                'retry_or_resampling': False}
            if result.returncode == 0:
                scores = read(output / 'scores.json')
                if scores['planned'] != len(cases):
                    raise ScoringError('Native mixed scorer changed the original denominator')
                completion['scores_sha256'] = file_sha(output / 'scores.json')
                completion['generation_exit_code'] = 0 if scores.get('completed') == len(cases) else 1
            base.immutable_json(output / 'completion.json', completion)
            if result.returncode:
                raise ScoringError('Native mixed scorer failed; attempt preserved, no automatic retry')
            return {'state': 'completed', 'run_id': output.name, 'completion': completion}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--spec', type=Path)
    parser.add_argument('--validate-only', action='store_true')
    parser.add_argument('--native-only-spec', type=Path)
    parser.add_argument('--native-config', type=Path)
    parser.add_argument('--native-folder', type=Path)
    args = parser.parse_args()
    if args.native_only_spec:
        result = invoke_native(read(args.native_only_spec), args.native_config, args.native_folder)
    elif args.spec:
        result = score_spec(read(args.spec), validate_only=args.validate_only)
    else:
        parser.error('--spec or --native-only-spec is required')
    print(json.dumps(result, ensure_ascii=False))


if __name__ == '__main__':
    main()
