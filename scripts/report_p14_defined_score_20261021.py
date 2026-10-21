#!/usr/bin/env python3
"""Present the sealed P14 score and one complete saved, reference-free input."""
from datetime import datetime
import hashlib
import json
from pathlib import Path
import re
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parents[1]
RUN = 'qwen38_27b_p14_full_test_dense3dp_nonthinking16k_2026-10-20_v1'
CONFIG_SHA = 'aaa7d1fbdbcd3a1d1c2ed38026c542f44259659d3c1232f8c631ed44e9c48f2d'


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read(path):
    return json.loads(path.read_text())


def main():
    stamp = datetime.now(ZoneInfo('America/Los_Angeles')).isoformat()
    folder = ROOT / '.local/catalog_execution_2026-10-20/tasks/P14/runtime/benchmark'
    score_path = ROOT / 'results/runs' / RUN / 'scores.json'
    score, completion, lock = read(score_path), read(folder/'completion.json'), read(folder/'prediction_lock.json')
    lock_sha, score_sha = sha(folder/'prediction_lock.json'), sha(score_path)
    if (score['run_id'] != RUN or score['config_sha256'] != CONFIG_SHA or
            score['planned'] != 3416 or score['parsed'] != 3416 or score['invalid_or_missing'] != 0 or
            score['full_planned_primary_metrics_valid'] is not True or
            completion['planned'] != 3416 or completion['terminal'] != 3416 or
            completion['prediction_lock_sha256'] != lock_sha or score['prediction_lock_sha256'] != lock_sha):
        raise ValueError('Require the sealed, defined full P14 score')
    config_path = folder.parents[1] / 'full_test_config.json'
    config = read(config_path)
    if sha(config_path) != CONFIG_SHA or sha(Path(config['input_file'])) != config['input_sha256']:
        raise ValueError('Frozen P14 input identity changed')
    with Path(config['input_file']).open() as handle:
        case = json.loads(handle.readline())
    request_name = 'requests/' + hashlib.sha256(case['case_id'].encode()).hexdigest() + '.json'
    request_path = folder/request_name
    if sha(request_path) != lock['files_sha256'][request_name]:
        raise ValueError('Saved example differs from its generation lock')
    request = read(request_path)
    if (request['messages'] != case['messages'] or len(request['messages']) != 1 or
            request['messages'][0]['role'] != 'user'):
        raise ValueError('Unexpected reference-free saved question')
    prompt = request['messages'][0]['content']
    heading = 'Predict Gene Ontology molecular-function annotation for the protein from its complete amino acid sequence.'
    if not isinstance(prompt, str) or not prompt.startswith(heading):
        raise ValueError('Unexpected molecular-function prompt')
    page = ROOT/'reports/questions/P14.md'
    page.write_text('# DeepFRI / ProtST: Gene Ontology molecular function — complete question and input\n\n'
        'This is the complete text sent to Qwen for one evaluated case, including its complete amino-acid sequence and all 489 ordered molecular-function descriptions. No reference labels or model answer are included.\n\n'
        f"Case: `{case['case_id']}`. Source: the sealed 3,416-case full-FASTA test95 run.\n\n"
        '## User message\n\n```text\n' + prompt + '\n```\n\n'
        '[Back to results](../RESULTS_AND_REMAINING_WORK.md)\n')
    table = read(ROOT/'reports/EVALUATION_DECISION_TABLE.json')
    record = next(r for r in table['rows'] if r['task_id'] == 'P14' and r['run_id'] == RUN)
    exported = next(r for r in read(ROOT/'reports/CATALOG_NEW_SCORES_2026-10-20.json')['completed_rows'] if r['task_id'] == 'P14')
    metrics = score['metrics']
    row = ('| DeepFRI / ProtST: Gene Ontology molecular function | '
        '[2021](https://doi.org/10.1038/s41467-021-23303-9); ProtST [2023](https://proceedings.mlr.press/v202/xu23t.html) | '
        f'“{heading}”<br>[Full question, sequence and 489 GO descriptions](questions/P14.md) | AUPRC / Fmax | '
        f"{metrics['auprc@micro']:.4f} / {metrics['f1_max']:.4f} | — | — | "
        '[ProtST-ESM-2: 0.647 / 0.668 (Table 3)](https://proceedings.mlr.press/v202/xu23t/xu23t.pdf)'
        '<br>full-model supervised tuning; our full-FASTA text baseline differs. | — |')
    report_path = ROOT/'reports/RESULTS_AND_REMAINING_WORK.md'
    report = report_path.read_text()
    title = '| DeepFRI / ProtST: Gene Ontology molecular function |'
    if title in report:
        report = '\n'.join(row if line.startswith(title) else line for line in report.split('\n'))
    else:
        anchor = '| IEConv / ProtST: Enzyme reaction classification |'
        if anchor not in report:
            raise ValueError('Presentation insertion anchor missing')
        report = report.replace(anchor, row+'\n'+anchor, 1)
    source_path = ROOT/'reports/RESULTS_AND_REMAINING_WORK.sources.json'
    source = read(source_path)
    defined_count = len(set(source['qwen']['defined_setting_ids'])|{'P14'})
    report = re.sub(r'\*\*\d+ of 57 evaluation settings\*\*', f'**{defined_count} of 57 evaluation settings**', report)
    qualifier = ('**Molecular-function annotation:** Qwen scored all 3,416 released test95 sequences using a fixed 489-label, '
        'three-decimal confidence output. Native AP/Fmax formulas are retained. This zero-shot full-sequence text adaptation '
        'differs from the trained ProtST model and its PDB-modeled input subset.')
    if qualifier not in report:
        report = report.replace('**Enzyme Commission classification:**', qualifier+'\n\n**Enzyme Commission classification:**', 1)
    report_path.write_text(report)
    record.update(condition_id='Q_P14_20261021', is_primary_table=True,
        classification='native_formula_on_zero_shot_adapted_model', evidence_level='score_bytes_verified',
        old_undefined_full_metric=False, raw_response_reverified_by_this_audit=False,
        score_source={'path':str(score_path.relative_to(ROOT)), 'local_present':True,
            'local_sha256':score_sha, 'recorded_sha256':score_sha, 'local_hash_matches_recorded':True,
            'remote_at_verified_commit':None, 'remote_hash_matches_recorded':None,
            'note':'Publication bytes are recorded independently in the P14 publication receipt.'},
        new_score_export=exported)
    source['qwen']['records'] = [r for r in source['qwen']['records'] if r.get('run_id') != RUN]+[record]
    source['qwen']['defined_setting_ids'] = sorted(set(source['qwen']['defined_setting_ids'])|{'P14'})
    source['qwen']['defined_setting_count'] = len(source['qwen']['defined_setting_ids'])
    source['qwen']['primary_condition_count'] = sum(r.get('is_primary_table') is True for r in source['qwen']['records'])
    source['qwen']['generated_at_pacific'] = stamp
    for r in source['qwen'].get('sources', []):
        if r['path'] in {'reports/EVALUATION_DECISION_TABLE.json','reports/CATALOG_NEW_SCORES_2026-10-20.json'}:
            r['sha256'] = sha(ROOT/r['path'])
    question = {'task_id':'P14','id':'P14','page_id':'P14','page_path':str(page.relative_to(ROOT)),
        'dataset':'DeepFRI molecular-function annotation test95 / ProtST','case_id':case['case_id'],
        'status':'complete_saved_evaluated_input','complete_question_or_input':True,
        'page_sha256':sha(page),'page_bytes':page.stat().st_size,
        'source_path':str(request_path.relative_to(ROOT)),'source_sha256':sha(request_path),
        'prediction_lock_sha256':lock_sha,'reference_answers_included':False,'new_case_reviews':0}
    source['verified_questions'] = [r for r in source['verified_questions'] if r.get('task_id') != 'P14']+[question]
    pages = source['question_pages']['protein_and_generation']
    pages['records'] = [r for r in pages['records'] if r.get('task_id') != 'P14']+[question]
    best = {'task_id':'P14','best_model':'ProtST-ESM-2','display':'ProtST-ESM-2: AUPR 0.647; Fmax 0.668',
        'metric':'AUPR / Fmax','values':{'aupr':0.647,'fmax':0.668},
        'source_url':'https://proceedings.mlr.press/v202/xu23t/xu23t.pdf','source_locator':'Table 3, printed p.6',
        'comparability':'Full-model supervised tuning; Qwen uses complete released test95 FASTA text and fixed GO-MF descriptions without a trained head. Native PDB-modeled input subset is not reproduced.',
        'value_status':'verified_primary_source_printed','selection':'Highest AUPR and Fmax among main Table 3 task-comparison models; not a current leaderboard claim.',
        'verified_at_pacific':stamp}
    refs = source['published_model_references']
    refs['records'] = [r for r in refs['records'] if r.get('task_id') != 'P14']+[best]
    source.update(generated_at_pacific=stamp,report_sha256=sha(report_path),p14_result_added_at_pacific=stamp,
        p14_defined_score_source={'path':str(score_path.relative_to(ROOT)),'sha256':score_sha,
            'prediction_lock_sha256':lock_sha,'new_inference_calls_by_reporting':0,'new_scoring_calls_by_reporting':0})
    source_path.write_text(json.dumps(source,indent=2,ensure_ascii=False)+'\n')
    if report.count(title) != 1 or len([line for line in report.splitlines() if line.startswith('| Evaluation |')]) != 1:
        raise ValueError('Require one clean presentation table and one P14 row')
    print(json.dumps({'defined_settings':defined_count,'score_sha256':score_sha,
        'question_bytes':page.stat().st_size,'report_sha256':sha(report_path),'new_model_calls':0,'new_scoring_calls':0}))


if __name__ == '__main__':
    main()
