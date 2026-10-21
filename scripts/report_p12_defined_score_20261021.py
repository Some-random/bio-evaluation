#!/usr/bin/env python3
"""Add the sealed P12 result and its exact saved input to presentation reports."""
from datetime import datetime
import hashlib
import json
from pathlib import Path
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parents[1]
RUN = 'qwen38_27b_p12_dense3dp_nonthinking16k_test_2026-10-20_v1'
SCORE_SHA = '03a01681d1ef58037a814c0b16edbf9c6632f03fc3d1f37671b020a538138852'
LOCK_SHA = '4f2b4709159c1d69b3545b0a08995ec6c6ede3cb9ec239dc2fa6bac37d7d6587'
REQUEST = 'requests/0022b61c26d16035f9e1bbe2216ecc921241eb194d4e1d7772ff6ca613db67d7.json'


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read(path):
    return json.loads(path.read_text())


def main():
    stamp = datetime.now(ZoneInfo('America/Los_Angeles')).isoformat()
    folder = ROOT / '.local/catalog_execution_2026-10-20/tasks/P12/runtime/benchmark'
    score_path = ROOT / 'results/runs' / RUN / 'scores.json'
    assert sha(score_path) == SCORE_SHA and sha(folder / 'prediction_lock.json') == LOCK_SHA
    lock = read(folder / 'prediction_lock.json')
    request_path = folder / REQUEST
    assert sha(request_path) == lock['files_sha256'][REQUEST]
    request = read(request_path)
    assert len(request['messages']) == 1 and request['messages'][0]['role'] == 'user'
    prompt = request['messages'][0]['content']
    assert isinstance(prompt, str) and prompt.startswith('Predict Enzyme Commission reaction-class annotation')
    page = ROOT / 'reports/questions/P12.md'
    page.write_text('# DeepFRI / ProtST: Enzyme Commission classification — complete question and input\n\n'
        'This is the complete text sent to Qwen for one evaluated case, including the complete amino-acid sequence and all 538 ordered EC descriptions. No reference labels or model answer are included.\n\n'
        'Case: `3W4P-A`. Source: the sealed 1,919-case full-FASTA test95 run.\n\n'
        '## User message\n\n```text\n' + prompt + '\n```\n\n'
        '[Back to results](../RESULTS_AND_REMAINING_WORK.md)\n')
    report_path = ROOT / 'reports/RESULTS_AND_REMAINING_WORK.md'
    report = report_path.read_text()
    report = report.replace('*October 20, 2026*', '*October 21, 2026*')
    report = report.replace('[Track the 15 preparation tasks]', '[Track preparation and runtime progress]')
    report = report.replace('**28 of 57 evaluation settings**', '**29 of 57 evaluation settings**')
    report = report.replace('The table also includes the **15 evaluations in preparation**, release years, real example questions, and published model results.',
                            'The table also lists evaluations in preparation, release years, real example questions, and published model results.')
    row = '| DeepFRI / ProtST: Enzyme Commission classification | [2021](https://doi.org/10.1038/s41467-021-23303-9); ProtST [2023](https://proceedings.mlr.press/v202/xu23t.html) | “Predict Enzyme Commission reaction-class annotation for the protein from its complete amino acid sequence.”<br>[Full question, sequence and 538 EC descriptions](questions/P12.md) | AUPRC / Fmax | 0.0046 / 0.0126 | — | — | [ProtST-ESM-2: 0.898 / 0.878 (Table 3)](https://proceedings.mlr.press/v202/xu23t/xu23t.pdf)<br>full-model supervised tuning; our full-FASTA text baseline differs. | — |'
    if '| DeepFRI / ProtST: Enzyme Commission classification |' not in report:
        needle = '| IEConv / ProtST: Enzyme reaction classification |'
        assert needle in report
        report = report.replace(needle, row + '\n' + needle, 1)
    else:
        report = '\n'.join(row if line.startswith('| DeepFRI / ProtST: Enzyme Commission classification |') else line for line in report.split('\n'))
    qualifier = '**Enzyme Commission classification:** Qwen scored all 1,919 released test95 sequences using a fixed 538-label, three-decimal confidence output. The native AP/Fmax formulas are retained; this is a zero-shot full-sequence text adaptation, not reproduction of the trained ProtST model or the PDB-modeled input subset.'
    if qualifier not in report:
        report = report.replace('**†** Stability classification', qualifier + '\n\n**†** Stability classification')
    report_path.write_text(report)
    source_path = ROOT / 'reports/RESULTS_AND_REMAINING_WORK.sources.json'
    source = read(source_path)
    table = read(ROOT / 'reports/EVALUATION_DECISION_TABLE.json')
    record = next(row for row in table['rows'] if row['task_id'] == 'P12' and row['run_id'] == RUN)
    exported = next(row for row in read(ROOT / 'reports/CATALOG_NEW_SCORES_2026-10-20.json')['completed_rows'] if row['task_id'] == 'P12')
    record.update(condition_id='Q_P12_20261021', is_primary_table=True,
        classification='native_formula_on_zero_shot_adapted_model', evidence_level='score_bytes_verified',
        old_undefined_full_metric=False, raw_response_reverified_by_this_audit=False,
        score_source={'path': str(score_path.relative_to(ROOT)), 'local_present': True,
            'local_sha256': SCORE_SHA, 'recorded_sha256': SCORE_SHA, 'local_hash_matches_recorded': True,
            'remote_at_verified_commit': None, 'remote_hash_matches_recorded': None,
            'note': 'New P12 publication is recorded independently in its byte-verified publication receipt.'},
        new_score_export=exported)
    source['qwen']['records'] = [r for r in source['qwen']['records'] if r.get('run_id') != RUN] + [record]
    source['qwen']['defined_setting_ids'] = sorted(set(source['qwen']['defined_setting_ids']) | {'P12'})
    source['qwen']['defined_setting_count'] = len(source['qwen']['defined_setting_ids'])
    source['qwen']['primary_condition_count'] = sum(r.get('is_primary_table') is True for r in source['qwen']['records'])
    source['qwen']['generated_at_pacific'] = stamp
    for r in source['qwen'].get('sources', []):
        path = ROOT / r['path']
        if r['path'] in {'reports/EVALUATION_DECISION_TABLE.json', 'reports/CATALOG_NEW_SCORES_2026-10-20.json'}:
            r['sha256'] = sha(path)
    question_record = {'task_id': 'P12', 'id': 'P12', 'page_id': 'P12', 'page_path': str(page.relative_to(ROOT)),
        'dataset': 'DeepFRI enzyme classification test95 / ProtST', 'case_id': '3W4P-A',
        'status': 'complete_saved_evaluated_input', 'complete_question_or_input': True,
        'page_sha256': sha(page), 'page_bytes': page.stat().st_size,
        'source_path': str(request_path.relative_to(ROOT)), 'source_sha256': sha(request_path),
        'prediction_lock_sha256': LOCK_SHA, 'reference_answers_included': False,
        'new_case_reviews': 0}
    source['verified_questions'] = [r for r in source['verified_questions'] if r.get('task_id') != 'P12'] + [question_record]
    pages = source['question_pages']['protein_and_generation']
    pages['records'] = [r for r in pages['records'] if r.get('task_id') != 'P12'] + [question_record]
    best = {'task_id': 'P12', 'best_model': 'ProtST-ESM-2', 'display': 'ProtST-ESM-2: AUPR 0.898; Fmax 0.878',
        'metric': 'AUPR / Fmax', 'values': {'aupr': 0.898, 'fmax': 0.878},
        'source_url': 'https://proceedings.mlr.press/v202/xu23t/xu23t.pdf', 'source_locator': 'Table 3, printed p.6',
        'comparability': 'Full-model supervised tuning; Qwen uses full released test95 FASTA text and fixed EC descriptions without a trained head. Native first-550 PDB-modeled inputs are not reproduced.',
        'value_status': 'verified_primary_source_printed',
        'selection': 'Highest AUPR among main Table 3 task-comparison models; tied highest Fmax. Not a current leaderboard claim.',
        'verified_at_pacific': stamp}
    refs = source['published_model_references']
    refs['records'] = [r for r in refs['records'] if r.get('task_id') != 'P12'] + [best]
    source.update(generated_at_pacific=stamp, report_sha256=sha(report_path), p12_result_added_at_pacific=stamp,
        p12_defined_score_source={'path': str(score_path.relative_to(ROOT)), 'sha256': SCORE_SHA,
            'prediction_lock_sha256': LOCK_SHA, 'new_inference_calls_by_reporting': 0, 'new_scoring_calls_by_reporting': 0})
    source_path.write_text(json.dumps(source, indent=2, ensure_ascii=False) + '\n')
    assert report.count('| DeepFRI / ProtST: Enzyme Commission classification |') == 1
    assert len([line for line in report.splitlines() if line.startswith('| Evaluation |')]) == 1
    print(json.dumps({'defined_settings': source['qwen']['defined_setting_count'],
        'score_sha256': SCORE_SHA, 'complete_question_bytes': page.stat().st_size,
        'report_sha256': sha(report_path), 'new_model_calls': 0, 'new_scoring_calls': 0}))


if __name__ == '__main__':
    main()
