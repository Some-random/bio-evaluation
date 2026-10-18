#!/usr/bin/env python3
"""An explicit, separately stored prospective budget revision; preserves 4k runs.

Payload construction remains the hash-pinned native helper. The only permitted
model-facing delta is max_tokens=16384. Only cleanly never-dispatched cases are
eligible. The full-task union is explicitly mixed4k/16k; old cases are not rerun.
No correctness, truncation or reference field is used to choose this cohort.
"""
from __future__ import annotations

import argparse
from collections import Counter, deque
import copy
import fcntl
import hashlib
import importlib.util
import json
from pathlib import Path
import signal
import sys
import threading
import time
import uuid

ROOT = Path(__file__).resolve().parents[3]
BASE = ROOT / '.local/shared_vllm_saturation_2026-10-18'
PINS = {
    'shared_vllm_resume.py': '8473aeee85c63bba6e1b390b9acf78477d8a81435d7e0504ce1b086515965256',
    'native_queue_scheduler.py': '340139bf587a92ecbaa97454a554a7b58276c3b021c639f37a5a2e288933bc69',
    'run_shared_vllm_evaluations.py': '495b8a91f7cc0b8ad6de14bd06ad6c3812a3aa712e20277f9a69b579127ce447',
}
for _name, _expected in PINS.items():
    if hashlib.sha256((BASE / _name).read_bytes()).hexdigest() != _expected:
        raise RuntimeError('Pinned parent infrastructure changed: ' + _name)
sys.path.insert(0, str(BASE))
from shared_vllm_resume import (MODEL, REVISION, ResumeError, atomic_write, digest,
                               file_sha, frozen_helper, local_path, read, stamp,
                               validate_endpoint)
from run_shared_vllm_evaluations import require_idle_endpoint
from native_queue_scheduler import NativeTaskQueue, drive_bounded_queue

CONDITION = 'MIXED_BUDGET_4K16K_CONTINUATION'
BUDGET = 16384
EXCLUDED = {'B06', 'P18', 'P28', 'P29', 'N01', 'N02', 'N03', 'N04', 'N05'}


def revised_settings(settings):
    result = copy.deepcopy(settings)
    if result['generation']['max_tokens'] != 4096:
        raise ResumeError('The exact original 4096-token configuration is required')
    result['generation']['max_tokens'] = BUDGET
    return result


def revised_request(helper, case, original):
    before = helper.request_record(case, original)
    after = helper.request_record(case, revised_settings(original))
    expected = copy.deepcopy(before)
    expected['payload']['max_tokens'] = BUDGET
    expected['request_sha256'] = digest(expected['payload'])
    if after != expected:
        raise ResumeError('More than the explicitly authorized output budget changed')
    return after


class RevisionTaskQueue(NativeTaskQueue):
    """Retain native queue behavior with an explicitly pinned new budget."""
    def __init__(self, runs, endpoints):
        self.runs = list(runs)
        self.pending = [iter(state.pending()) for state in self.runs]
        self.heads, self.exhausted = {}, set()
        self.mutex = threading.Lock()
        grouped = {}
        for index, state in enumerate(self.runs):
            grouped.setdefault(state.entry['task_id'], deque()).append(index)
            if state.settings['generation']['max_tokens'] != BUDGET:
                raise ResumeError('The separately reported condition requires exactly 16384 tokens')
            count = max(state.prompt_tokens.values(), default=0)
            if not any(endpoint['max_model_len'] >= state.entry['minimum_context_tokens']
                       and count + BUDGET <= endpoint['max_model_len'] for endpoint in endpoints):
                raise ResumeError('Complete inputs plus the new output budget exceed context')
        self.tasks, self.groups = deque(grouped), grouped
        self.selected_by_task, self.selected_by_run = Counter(), Counter()


class RevisionRun:
    def __init__(self, item, plan, plan_sha):
        self.entry = item['entry']
        self.plan, self.plan_sha = plan, plan_sha
        self.project = local_path(ROOT, self.entry['project_root'])
        self.config_path = local_path(self.project, self.entry['config_path'])
        if file_sha(self.config_path) != self.entry['config_sha256']:
            raise ResumeError('Original frozen configuration changed')
        self.helper = frozen_helper(self.project, self.entry['runner'], self.entry['runner_sha256'])
        self.original_settings, self.source_cases = self.helper.read_frozen_config(self.config_path)
        self.settings = revised_settings(self.original_settings)
        if (self.entry['task_id'] in EXCLUDED
                or self.original_settings['model'] != MODEL
                or self.original_settings['model_revision'] != REVISION
                or self.original_settings['run_id'] != self.entry['run_id']
                or self.original_settings['approved_task_ids'] != [self.entry['task_id']]
                or digest(self.original_settings['generation']) != self.entry['generation_sha256']
                or len(self.source_cases) != self.entry['case_count']
                or file_sha(self.project / self.settings['input_file']) != self.entry['input_sha256']):
            raise ResumeError('Source scope/model/input differs from the frozen contract')
        checkpoint_pin = item['parent_checkpoint']
        checkpoint_path = local_path(ROOT, checkpoint_pin['path'])
        if file_sha(checkpoint_path) != checkpoint_pin['sha256']:
            raise ResumeError('Frozen clean-pause parent checkpoint changed')
        self.checkpoint = read(checkpoint_path)
        self.parent_run = local_path(ROOT, self.checkpoint['parent_run_directory'])
        self.source_run = self.project / 'results/runs' / self.entry['run_id']
        selected = item['selected_case_ids']
        selected_set = set(selected)
        self.cases = [c for c in self.source_cases if c['case_id'] in selected_set]
        if (item['case_scope'] != 'all_never_dispatched_at_clean_pause'
                or [c['case_id'] for c in self.cases] != selected
                or self.checkpoint['ordered_pending_case_ids'] != selected
                or item['ordered_case_ids_sha256'] != digest(selected)
                or self.checkpoint['source_case_contract_sha256'] != digest(self.source_cases)
                or self.checkpoint['ambiguous_files'] != []):
            raise ResumeError('The revision must include exactly all clean never-dispatched cases')
        self.parent_checkpoint_pin = checkpoint_pin
        context_pin = item['context_check']
        context_path = local_path(ROOT, context_pin['path'])
        if file_sha(context_path) != context_pin['sha256']:
            raise ResumeError('Pinned input token accounting changed')
        context = read(context_path)
        if (context['case_count'] != len(self.source_cases)
                or context['output_budget'] != 4096
                or [x['case_id'] for x in context['per_case']] != [c['case_id'] for c in self.source_cases]):
            raise ResumeError('Context report does not cover complete source scope')
        self.prompt_tokens = {x['case_id']: x['prompt_tokens'] for x in context['per_case']
                              if x['case_id'] in selected_set}
        if any(type(n) is not int or n < 1 for n in self.prompt_tokens.values()):
            raise ResumeError('Invalid per-case input token accounting')
        self.run = local_path(ROOT, item['output_directory'])
        if (self.run == self.project / 'results/runs' / self.entry['run_id']
                or not self.run.is_relative_to((ROOT / '.local/evaluation_revision_2026-10-18').resolve())
                or self.run.name != self.entry['run_id'] + '_output16384_v1'):
            raise ResumeError('New condition must use its independent output namespace')
        self.mutex = threading.Lock()
        self.locks = []
        self.started = time.monotonic()
        self.finished_result = None
        self.statuses = Counter()

    def acquire(self):
        self.run.mkdir(parents=True, exist_ok=True)
        paths = [self.project / '.local' / ('slurm_generation-' + self.entry['run_id'] + '.lock'),
                 self.source_run / 'worker.lock', self.parent_run / 'worker.lock', self.run / 'worker.lock']
        for path in dict.fromkeys(paths):
            path.parent.mkdir(parents=True, exist_ok=True)
            h = path.open('a')
            try:
                fcntl.flock(h, fcntl.LOCK_EX | fcntl.LOCK_NB)
            except Exception:
                h.close()
                self.close()
                raise ResumeError('Original or revised producer still owns a source run')
            self.locks.append(h)

    def close(self):
        for h in self.locks:
            h.close()
        self.locks = []

    def name(self, case):
        return digest([case['task'], case['variant'], case['case_id']]) + '.json'

    def inventory(self):
        counts = Counter()
        expected = set()
        for case in self.cases:
            name = self.name(case)
            expected.add(name)
            req, resp = self.run / 'requests' / name, self.run / 'responses' / name
            if resp.exists():
                if not req.exists() or read(req) != revised_request(self.helper, case, self.original_settings):
                    raise ResumeError('Saved response lacks its exact separately budgeted request')
                r = read(resp)
                receipt = read(self.run / 'dispatch' / name)
                if (r['request_sha256'] != read(req)['request_sha256'] or r.get('condition') != CONDITION
                        or r.get('model') != MODEL or r.get('model_revision') != REVISION
                        or any(r.get(k) != case[k] for k in ('task', 'case_id', 'variant', 'split'))
                        or receipt.get('response_sha256') != file_sha(resp)
                        or receipt.get('request_sha256') != r['request_sha256']
                        or receipt.get('plan_sha256') != self.plan_sha):
                    raise ResumeError('Response belongs to another condition or request')
                counts[r['status']] += 1
            elif req.exists() or (self.run / 'dispatch' / name).exists():
                counts['interrupted_unknown_completion'] += 1
            else:
                counts['undispatched'] += 1
        for kind in ('requests', 'responses', 'dispatch'):
            if {p.name for p in (self.run / kind).glob('*.json')} - expected:
                raise ResumeError('Unaccounted raw slot in the new condition')
        return counts

    def prepare(self):
        # The old producer holds these same locks. Recheck journal closure after
        # acquiring them so a stale freeze can never authorize a simultaneous
        # old producer, or unaccounted extra parent records.
        retained = self.checkpoint['retained_files_sha256']
        for kind in ('requests', 'responses', 'shared_vllm_segments', 'shared_vllm_dispatch',
                     'shared_vllm_saturation_segments', 'shared_vllm_saturation_dispatch',
                     'shared_vllm_saturation_pauses'):
            current = {kind + '/' + p.name for p in (self.parent_run / kind).glob('*.json')}
            declared = {name for name in retained if name.startswith(kind + '/')}
            if current != declared:
                raise ResumeError('An old producer added or lost records after cohort freeze')
        for p in (self.parent_run / 'shared_vllm_saturation_segments').glob('*.json'):
            if read(p)['stage'] not in {'paused', 'terminal'}:
                raise ResumeError('An old source segment is still running')
        for name, expected in self.checkpoint['retained_files_sha256'].items():
            if file_sha(local_path(self.parent_run, name)) != expected:
                raise ResumeError('An immutable 4k parent artifact changed')
        for case in self.cases:
            name = self.name(case)
            if any((self.parent_run / k / name).exists() for k in
                   ('requests', 'responses', 'shared_vllm_dispatch', 'shared_vllm_saturation_dispatch')):
                raise ResumeError('A previously claimed case cannot enter the prospective16k cohort')
        manifest = {
            'schema_version': 1, 'condition': CONDITION, 'plan_sha256': self.plan_sha,
            'source_entry': self.entry, 'planned_cases': len(self.cases),
            'original_configuration': self.original_settings, 'configuration': self.settings,
            'case_scope': 'all_never_dispatched_at_clean_pause', 'ordered_cases_sha256': digest(self.cases),
            'parent_run_directory': str(self.parent_run),
            'parent_checkpoint': next(x['parent_checkpoint'] for x in self.plan['runs']
                                      if x['entry']['run_id'] == self.entry['run_id']),
            'original_whole_source_case_count': len(self.source_cases),
            'aggregate_budget_condition': CONDITION,
            'model_facing_changes': [{'field': 'max_tokens', 'before': 4096, 'after': BUDGET}],
            'original_artifacts_modified': False, 'model_outcome_based_selection': False,
        }
        path = self.run / 'run_manifest.json'
        if path.exists():
            if read(path) != manifest:
                raise ResumeError('New condition manifest changed')
        else:
            atomic_write(path, manifest, exclusive=True)
        self.statuses = self.inventory()
        if self.statuses.get('interrupted_unknown_completion'):
            raise ResumeError('Ambiguous calls are never retried')
        self.statuses.pop('undispatched', None)
        done = self.run / 'generation_completion.json'
        if done.exists():
            value = read(done)
            if (value.get('condition') != CONDITION or value.get('plan_sha256') != self.plan_sha
                    or value.get('planned') != len(self.cases)
                    or value.get('statuses') != dict(self.statuses)
                    or sum(self.statuses.values()) != len(self.cases)):
                raise ResumeError('Existing new-condition completion marker differs')
            self.finished_result = value
        self.progress()

    def pending(self):
        for case in self.cases:
            name = self.name(case)
            if not any((self.run / k / name).exists() for k in ('requests', 'responses', 'dispatch')):
                yield case, name

    def dispatch(self, case, name, endpoint, stopped):
        if stopped.is_set():
            return
        if any((self.parent_run / k / name).exists() for k in
               ('requests', 'responses', 'shared_vllm_dispatch', 'shared_vllm_saturation_dispatch')):
            raise ResumeError('A case has already been claimed by a previous producer')
        request = revised_request(self.helper, case, self.original_settings)
        receipt = {'condition': CONDITION, 'plan_sha256': self.plan_sha, 'case_id': case['case_id'],
                   'request_sha256': request['request_sha256'], 'claimed_at_utc': stamp(),
                   'endpoint_id': endpoint['endpoint_id'],
                   'server_identity_sha256': endpoint['server_identity_sha256'],
                   'prompt_tokens': self.prompt_tokens[case['case_id']], 'output_budget': BUDGET}
        atomic_write(self.run / 'dispatch' / name, receipt, exclusive=True)
        atomic_write(self.run / 'requests' / name, request, exclusive=True)
        before = time.monotonic()
        code, response = self.helper.call(endpoint['endpoint'] + '/chat/completions',
                                         request['payload'], timeout=14400)
        record = {**{k: case[k] for k in ('task', 'case_id', 'variant', 'split')},
                  'condition': CONDITION, 'model': MODEL, 'model_revision': REVISION,
                  'request_sha256': request['request_sha256'], 'http_status': code,
                  'response': response, 'elapsed_seconds': round(time.monotonic() - before, 3),
                  'saved_at_utc': stamp()}
        if code == 200 and response.get('model') == MODEL and len(response.get('choices', [])) == 1:
            choice = response['choices'][0]
            record.update(status='completed', text=choice['message'].get('content') or '',
                          finish_reason=choice.get('finish_reason'))
        else:
            record['status'] = 'transport_error' if code == 0 else 'server_error'
            stopped.set()
        atomic_write(self.run / 'responses' / name, record, exclusive=True)
        receipt.update(response_sha256=file_sha(self.run / 'responses' / name), finished_at_utc=stamp())
        atomic_write(self.run / 'dispatch' / name, receipt)
        with self.mutex:
            self.statuses[record['status']] += 1
            self.progress()

    def progress(self):
        atomic_write(self.run / 'progress.json', {'condition': CONDITION, 'plan_sha256': self.plan_sha,
                     'run_id': self.run.name, 'planned': len(self.cases), 'statuses': dict(self.statuses),
                     'finished': sum(self.statuses.values()), 'updated_at_utc': stamp()})

    def finish_if_complete(self):
        with self.mutex:
            if self.finished_result is not None or sum(self.statuses.values()) != len(self.cases):
                return
            value = {'condition': CONDITION, 'plan_sha256': self.plan_sha, 'planned': len(self.cases),
                     'statuses': dict(self.statuses), 'generation_exit_code': 0 if self.statuses['completed'] == len(self.cases) else 1,
                     'finished_at_utc': stamp(), 'retry_or_resampling': False, 'scoring_performed': False}
            atomic_write(self.run / 'generation_completion.json', value, exclusive=True)
            self.finished_result = value


def load_plan(path, expected, live=False):
    path = local_path(ROOT, path)
    if file_sha(path) != expected:
        raise ResumeError('New budget plan digest changed')
    plan = read(path)
    if (plan.get('schema_version') != 1 or plan.get('kind') != 'explicit_output_budget_revision'
            or plan.get('execution_authorized') is not True or plan.get('condition') != CONDITION
            or plan.get('model') != MODEL or plan.get('model_revision') != REVISION
            or plan.get('output_budget') != BUDGET or plan.get('original_output_budget') != 4096
            or plan.get('code_sha256') != file_sha(__file__)
            or plan.get('excluded_task_ids') != sorted(EXCLUDED)
            or not plan.get('authorization_quote') or not plan.get('runs')):
        raise ResumeError('Explicit user authorization, new condition and complete source scope required')
    endpoints = [validate_endpoint(e, live=live) for e in plan['endpoints']]
    uuids = [u for e in endpoints for u in e['server_identity']['gpu_uuids']]
    if not endpoints or len(uuids) > 8 or len(set(uuids)) != len(uuids):
        raise ResumeError('New condition must retain disjoint servers within the eight-GPU ceiling')
    return plan, endpoints


def run(path, expected, check_only=False):
    plan, endpoints = load_plan(path, expected, live=not check_only)
    states = [RevisionRun(item, plan, expected) for item in plan['runs']]
    identities = [(c['task'], c['variant'], c['case_id']) for s in states for c in s.cases]
    if len(identities) != len(set(identities)):
        raise ResumeError('Duplicate case in the separate condition')
    queue = RevisionTaskQueue(states, endpoints)
    inventory = [{'run_id': s.run.name, 'task_id': s.entry['task_id'], 'planned': len(s.cases),
                  'max_prompt_tokens': max(s.prompt_tokens.values(), default=0), 'output_budget': BUDGET}
                 for s in states]
    if check_only:
        return {'stage': 'checked_not_executed', 'condition': CONDITION, 'runs': inventory}
    locks = []
    old_signals = {}
    try:
        for endpoint in sorted(endpoints, key=lambda e: e['server_identity_sha256']):
            p = ROOT / '.local/shared_vllm_endpoint_locks' / (endpoint['server_identity_sha256'] + '.lock')
            p.parent.mkdir(parents=True, exist_ok=True)
            h = p.open('a')
            try:
                fcntl.flock(h, fcntl.LOCK_EX | fcntl.LOCK_NB)
            except Exception:
                h.close()
                raise ResumeError('Existing dispatcher still owns a selected endpoint')
            locks.append(h)
            require_idle_endpoint(endpoint)
        for s in states:
            s.acquire()
            s.prepare()
        stopped = threading.Event()
        def pause(signum, frame):
            stopped.set()
        old_signals = {sig: signal.signal(sig, pause) for sig in (signal.SIGTERM, signal.SIGINT)}
        metrics = drive_bounded_queue(queue, endpoints, stopped,
            lambda s, c, n, e, event: s.dispatch(c, n, e, event), lambda s: s.finish_if_complete())
        for s in states:
            s.progress()
        failed = bool(metrics['infrastructure_error_types']) or any(
            s.statuses.get(k) for s in states for k in ('transport_error', 'server_error', 'interrupted_unknown_completion'))
        return {'stage': 'paused' if stopped.is_set() else 'generation_terminal',
                'condition': CONDITION, 'plan_sha256': expected, 'scheduler': metrics,
                'generation_exit_code': 1 if failed else 0, 'scoring_performed': False, 'runs': inventory}
    finally:
        for sig, handler in old_signals.items():
            signal.signal(sig, handler)
        for s in states:
            s.close()
        for h in locks:
            h.close()


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--plan', required=True, type=Path)
    p.add_argument('--plan-sha256', required=True)
    p.add_argument('--check-only', action='store_true')
    args = p.parse_args()
    try:
        result = run(args.plan, args.plan_sha256, args.check_only)
        print(json.dumps(result, indent=2), flush=True)
        return result.get('generation_exit_code', 0)
    except (ResumeError, ValueError, OSError) as e:
        print(json.dumps({'stage': 'refused', 'error_type': type(e).__name__, 'reason': str(e)}), flush=True)
        return 1


if __name__ == '__main__':
    raise SystemExit(main())
