#!/usr/bin/env python3
"""Build the public results view and a payload-free preparation tracker."""
import csv
from datetime import datetime
import hashlib
import io
import json
from pathlib import Path
import re
import subprocess
from urllib.parse import urljoin
from zoneinfo import ZoneInfo

from markdown_it import MarkdownIt

ROOT = Path(__file__).resolve().parents[1]
RUN = ROOT / '.local/catalog_execution_2026-10-20'
PUBLIC = 'https://github.com/Some-random/bio-evaluation/blob/main/reports/'
SITE = 'https://some-random.github.io/bio-evaluation/'
TASKS = ['P04', 'P05', 'P17', 'P19', 'P21', 'P22', 'P27', 'P34',
         'P35', 'P37', 'P38', 'P39', 'P40', 'P41', 'V07']
PASSED = {
 'P04': 'input_reference_scalar_contract_synthetic_passed',
 'P05': 'input_reference_scalar_contract_synthetic_passed',
 'P17': 'release_inventory_and_scoring_contract_synthetic_passed',
 'P19': 'full_reviewed34_and_synthetic3_cpu_tokenizer_and_inactive_admission_checks_passed',
 'P21': 'native_input_isolation_and_ranking_adapter_synthetic_passed',
 'P22': 'native_input_isolation_and_ranking_adapter_synthetic_passed',
 'P27': r'available_cross_benchmark_package_and\d+synthetic_checks_complete_native_cohort_unavailable',
 'P34': 'released_heads_bound_and_synthetic_accounting_passed',
 'P37': 'combined_native_weight_binding_and_synthetic_io_passed',
 'P38': 'synthetic_cpu_evaluator_delivery_passed',
 'P39': r'pinned_complex_packaging_interface_and\d+synthetic_checks_complete',
 'P40': 'target_isolated_structural_packet_and_aar_synthetic_checks_passed',
 'P41': 'released_masking_helpers_and_synthetic_geometry_contract_passed',
}
NEXT = {
 'P04': 'Complete permitted-input review and test-data preparation; freeze and validate the prediction run.',
 'P05': 'Resolve the historical archive/crop comparison; complete permitted-input review and test preparation.',
 'P17': 'Finish the permitted assay roster and prepare separate inputs/references; validate the prediction run.',
 'P19': 'Integrate the separate runtime entry and pass actual development delivery before the reviewed subset can run.',
 'P21': 'Review permitted assays/context, prepare real inputs and pass tokenizer and ranking delivery checks.',
 'P22': 'Review permitted assays/context, prepare real inputs and pass tokenizer and ranking delivery checks.',
 'P27': 'The recovered alternative overlaps P26; resolve an independent evaluation cohort before claiming new coverage.',
 'P34': 'Assemble the encoder/tokenizer, review starting cases and validate the proposal interface.',
 'P35': 'Finish corpus preparation and permitted-input review, then validate retrieval. Numerical accuracy needs relevance labels.',
 'P37': 'Validate actual folding delivery and complete permitted-input/development checks.',
 'P38': 'Integrate the validated evaluators with reviewed generation and development delivery checks.',
 'P39': 'Resolve missing author-case details and validate an explicitly declared alternative case study; no measured binding score is available.',
 'P40': 'Review real cases and validate structural input serialization and model delivery.',
 'P41': 'Finish the numbering/CIF runtime, review released demonstrations and resolve the scoring configuration.',
 'V07': 'Finish full CPU image processing, then permitted-content review and actual model delivery checks.',
}
LATEST = {
 'P04': 'Input/reference separation and scalar output checks passed; native correlation fixtures checked.',
 'P05': 'Input/reference separation and scalar output checks passed; historical archive/crop mismatch documented.',
 'P17': 'All 217 archive/metadata entries matched; scoring and full-coverage checks passed.',
 'P19': 'All 34 reviewed inputs and 3 artificial development inputs passed CPU tokenizer checks; runtime package remains disabled.',
 'P21': 'Native input builder, reference isolation and complete-ranking checks passed on artificial fixtures.',
 'P22': 'Native input builder, reference isolation and complete-ranking checks passed on artificial fixtures.',
 'P27': '2,633 alternative inputs packaged; this cohort overlaps P26 and does not add an independently completed setting.',
 'P34': 'Five released scoring heads loaded exactly; synthetic accounting checks passed. Encoder delivery remains untested.',
 'P35': 'Building a candidate corpus on CPU; these records are prepared data, not model responses.',
 'P37': 'All 3,252 checkpoint tensors bound exactly; synthetic I/O checks passed. No folding forward was run.',
 'P38': 'Both alternative property evaluators passed CPU synthetic delivery; no benchmark generation.',
 'P39': 'Source-based case packaging and synthetic interface checks passed; exact author cohort is unavailable.',
 'P40': 'Target-isolated structural packet and recovery-metric helper passed synthetic checks; real cases remain unprepared.',
 'P41': 'Released masking/index helpers passed synthetic checks; full paper holdout and scorer equivalence remain unverified.',
 'V07': 'Two artificial 20-image cases passed; full-dataset CPU image processing is underway. No model inference.',
}

def now():
    return datetime.now(ZoneInfo('America/Los_Angeles')).isoformat()

def atomic(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_name(path.name + '.tmp')
    tmp.write_text(text)
    tmp.replace(path)

def read(path):
    try:
        return json.loads(path.read_text())
    except (OSError, ValueError):
        return {}

def number(value):
    return f'{value:,}' if isinstance(value, int) and not isinstance(value, bool) else 'unavailable'

def cells(line):
    return [v.strip().replace('\\|', '|') for v in re.split(r'(?<!\\)\|', line)[1:-1]]

def absolute_links(tokens):
    for token in tokens:
        if token.type == 'link_open':
            href = token.attrGet('href')
            if href and not href.startswith(('https://', 'http://', '#', 'mailto:')):
                token.attrSet('href', urljoin(PUBLIC, href))
        if token.children:
            absolute_links(token.children)

def build():
    report_path = ROOT / 'reports/RESULTS_AND_REMAINING_WORK.md'
    report = report_path.read_text()
    prefix = ('[Full-width results table](' + SITE + ') · '
              '[Track the 15 preparation tasks](' + SITE + '#progress) · '
              '[Markdown tracker](ENGINEERING_PROGRESS.md)\n\n')
    if '[Full-width results table]' not in report:
        report = report.replace('*October 20, 2026*\n\n', '*October 20, 2026*\n\n' + prefix, 1)
        atomic(report_path, report)
    source_path = ROOT / 'reports/RESULTS_AND_REMAINING_WORK.sources.json'
    sources = read(source_path)
    names = {}
    for old, new in sources['presentation_display_names'].items():
        match = re.search(r'\(([BPV]\d\d)\)', old)
        if match:
            names[match[1]] = new
    queues = read(RUN / 'engineering_resume_20261020/worker_queues.json')['queues']
    owners = {task: ('Main agent' if agent == '/root' else
                    'Worker ' + str(i + 1), agent)
              for i, (agent, tasks) in enumerate(queues.items()) for task in tasks}
    jobids = []
    raw = {}
    for task in TASKS:
        status = read(RUN / 'tasks' / task / 'engineering_20261020/status.json')
        raw[task] = status
        job = status.get('cpu_job_id') or status.get('slurm_job_id') or status.get('job_id')
        if job:
            jobids.append(str(job))
    job_states = {}
    if jobids:
        try:
            result = subprocess.run(['squeue', '-h', '-j', ','.join(jobids), '-o', '%i|%T'],
                                    text=True, capture_output=True, timeout=20)
            if result.returncode == 0:
                job_states = dict(line.split('|', 1) for line in result.stdout.splitlines() if '|' in line)
        except (OSError, subprocess.TimeoutExpired):
            pass
    records = []
    observed = now()
    for task in TASKS:
        s = raw[task]
        stage = s.get('stage', '')
        passed = bool(re.fullmatch(PASSED.get(task, r'(?!)'), stage))
        latest = LATEST[task] if passed else 'No verified passing milestone is recorded for the current preparation stage.'
        if not s:
            latest = 'No task-local engineering status was available at this observation.'
        next_step = NEXT[task]
        state = 'Preparation milestone passed' if passed else 'Preparation status needs review'
        if not s:
            state = 'Assigned; evidence unavailable'
        detail = []
        updated = s.get('updated_at_pacific')
        active = False
        job = str(s.get('cpu_job_id') or s.get('slurm_job_id') or s.get('job_id') or '')
        if task == 'P35' and stage == 'projecting_complete_source_order':
            active = job_states.get(job) == 'RUNNING'
            try:
                pid = int(s['pid'])
                command = Path('/proc') / str(pid) / 'cmdline'
                active = active or 'project_corpus.py' in command.read_bytes().decode(errors='replace')
            except (OSError, KeyError, ValueError):
                pass
            state = 'CPU preparation running' if active else 'CPU progress recorded; process unverified'
            latest = LATEST[task]
            detail.append(f"{number(s.get('processed'))} / {number(s.get('candidate_count'))} candidates processed")
            detail.append(f"{number(s.get('retained'))} retained; {number(s.get('rejected'))} rejected by parser")
        elif (task == 'P35' and stage == 'complete_qualified_corpus_projection_and_validation_not_inference'
              and read(RUN / 'tasks/P35/engineering_20261020/validation.json').get('stage') == 'passed'):
            state = 'Preparation milestone passed'
            latest = 'Full source-order corpus projection and artifact checks completed on CPU; this is prepared data, not retrieval predictions.'
            retention = s.get('retention', {})
            detail.append(f"{number(retention.get('candidate_count'))} candidates checked; {number(retention.get('retained_count'))} retained; {number(retention.get('rejected_count'))} parser rejections")
            next_step = 'Complete permitted-input review and validate retrieval delivery. Numerical accuracy additionally needs relevance labels.'
        elif task == 'P35' and stage == 'complete_cpu_projection_not_review_or_inference':
            state = 'Corpus projection finished; validation pending'
            latest = 'CPU corpus projection finished; independent artifact checks are still pending. No retrieval predictions.'
            next_step = 'Finish artifact validation, then permitted-input review and retrieval delivery checks.'
        elif task == 'P35' and stage == 'cpu_projection_resume_submitted_after_external_sigterm':
            active = job_states.get(job) == 'RUNNING'
            state = 'CPU preparation running' if active else 'CPU resume submitted; execution unverified'
            latest = 'Interrupted CPU preparation is resuming untouched source records; earlier artifacts are preserved. No model requests.'
        elif task == 'V07':
            latest = LATEST[task]
            active = job_states.get(job) == 'RUNNING'
            if active:
                state = 'CPU preparation running'
            elif s.get('full_processor_all_cases_passed') is True or stage in ('full_cpu_processor_preflight_passed', 'full_processor_preflight_passed'):
                state = 'Preparation milestone passed'
                latest = 'Full-dataset CPU image processing passed. Permitted-content review and actual model delivery remain.'
                next_step = 'Complete permitted-content review and separately admitted actual model delivery checks.'
            else:
                state = 'CPU progress recorded; check latest job state'
            detail.append(f"{number(s.get('full_processor_valid_case_records'))} / {number(s.get('full_processor_planned'))} processor records")
            detail.append('20 images per case; processor records are not model outputs')
        elif task == 'P38' and not ('passed' in stage or 'complete' in stage):
            active = job_states.get(job) == 'RUNNING'
            state = 'CPU evaluator validation running' if active else 'Evaluator preparation; check latest evidence'
            latest = 'CPU evaluator validation in progress; benchmark generation has not started.'
        tests = s.get('synthetic_tests_passed', s.get('synthetic_checks_passed'))
        if isinstance(tests, int):
            detail.append(f'{tests} synthetic checks passed')
        if isinstance(s.get('native_metric_synthetic_fixtures_passed'), int):
            detail.append(f"{s['native_metric_synthetic_fixtures_passed']} native-metric fixtures passed")
        if isinstance(s.get('synthetic_evaluator_forwards'), int):
            detail.append(f"{s['synthetic_evaluator_forwards']} synthetic evaluator forwards; no benchmark generation")
        if 'failed' in stage or stage.endswith('_error'):
            state = 'Preparation needs attention'
            active = False
            latest = 'The latest preparation check did not reach a verified passing completion.'
        if job and job in job_states:
            detail.append('CPU job ' + job + ': ' + job_states[job].lower())
        if not detail:
            detail.append('See latest verified result')
        records.append({'task_id': task, 'evaluation': names[task],
                        'worker': owners[task][0], 'agent': owners[task][1],
                        'state': state, 'active_cpu_work_verified': active,
                        'latest_result': latest, 'progress': '; '.join(detail),
                        'next_step': next_step, 'evidence_at_pacific': updated,
                        'benchmark_completed_by_this_preparation': False,
                        'engineering_status_available': bool(s)})
    payload = {'schema_version': 1, 'generated_at_pacific': observed,
               'timezone': 'America/Los_Angeles',
               'scope': '15 preparation tasks; separate from benchmark generation and scores',
               'publication_target_interval_seconds': 600,
               'refresh_note': 'Publication targets every 10 minutes while the local updater is running. Check the evidence timestamps; this is not a live agent-console connection.',
               'worker_note': 'Three assigned engineering workers plus the main agent; tasks are handled in queues, not 15 simultaneous subagents.',
               'task_count': len(records), 'tasks': records}
    encoded = json.dumps(payload, ensure_ascii=False, indent=2) + '\n'
    atomic(ROOT / 'reports/ENGINEERING_PROGRESS.json', encoded)
    atomic(ROOT / 'docs/progress.json', encoded)
    md = ['# Progress of the 15 preparation tasks', '',
          '[Full-width progress tracker](' + SITE + '#progress) · [Results table](' + SITE + ')', '',
          'Snapshot: **' + observed + '** (America/Los_Angeles).', '',
          payload['worker_note'], '', payload['refresh_note'], '',
          '**A preparation milestone is not a completed benchmark or a new benchmark score.**', '',
          '| Evaluation | Assigned worker | State | Latest verified result / progress | What remains | Evidence time (PDT) |',
          '|---|---|---|---|---|---|']
    for r in records:
        values = [r['evaluation'], r['worker'], r['state'], r['latest_result'] + '<br>' + r['progress'],
                  r['next_step'], r['evidence_at_pacific'] or 'Unavailable']
        md.append('| ' + ' | '.join(str(x).replace('|', '\\|').replace('\n', ' ') for x in values) + ' |')
    atomic(ROOT / 'reports/ENGINEERING_PROGRESS.md', '\n'.join(md) + '\n')
    lines = [line for line in report.splitlines() if line.startswith('|')]
    header = cells(lines[0])
    data = [cells(line) for line in lines[2:]]
    assert len(header) == 9 and len(data) == 45 and all(len(row) == 9 for row in data)
    csv_buffer = io.StringIO(newline='')
    writer = csv.writer(csv_buffer, lineterminator='\n')
    writer.writerow(header)
    writer.writerows(data)
    atomic(ROOT / 'docs/results.csv', csv_buffer.getvalue())
    renderer = MarkdownIt('commonmark', {'html': True}).enable('table')
    tokens = renderer.parse(report)
    absolute_links(tokens)
    rendered = renderer.renderer.render(tokens, renderer.options, {})
    template = (ROOT / 'scripts/progress_view_template.html').read_text()
    embedded = json.dumps(payload, ensure_ascii=False).replace('<', '\\u003c')
    page = template.replace('<!-- RESULTS -->', rendered).replace('/* INITIAL_PROGRESS */ null', embedded)
    atomic(ROOT / 'docs/index.html', page)
    atomic(ROOT / 'docs/.nojekyll', '')
    digest = hashlib.sha256(report.encode()).hexdigest()
    if sources['report_sha256'] != digest or 'presentation_links' not in sources:
        sources['report_sha256'] = digest
        sources['presentation_links'] = {'full_width_results': SITE, 'preparation_tracker': SITE + '#progress'}
        sources['full_width_view_added_at_pacific'] = observed
        atomic(source_path, json.dumps(sources, indent=2, ensure_ascii=False) + '\n')
    print(json.dumps({'generated_at_pacific': observed, 'preparation_tasks': len(records),
                      'active_cpu_checks_verified': sum(x['active_cpu_work_verified'] for x in records),
                      'results_rows': len(data), 'results_columns': len(header)}))

if __name__ == '__main__':
    build()
