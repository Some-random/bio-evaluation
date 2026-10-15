"""Offline native VQA-RAD/SLAKE headline metrics for a frozen local vision run.

Requests and responses (including missing slots) are locked before labels are
parsed. Source normalization and native open/closed rules remain unchanged.
"""
import argparse
from collections import Counter
import csv
import hashlib
import json
from pathlib import Path

import prepare_medical_vqa as preparation
from run_local_labbench_multimodal import payload_for, validate_content

ROOT = Path(__file__).resolve().parents[1]
NATIVE_GROUPS = {'V01': {'OPEN': 179, 'CLOSED': 272}, 'V02': {'OPEN': 645, 'CLOSED': 416}}


def digest(value):
    return hashlib.sha256(json.dumps(value, ensure_ascii=False, sort_keys=True,
                                    separators=(',', ':')).encode()).hexdigest()


def file_digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write_json(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + '.tmp')
    temporary.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')
    temporary.chmod(0o600)
    temporary.replace(path)


def expected_payload(case, settings):
    payload = payload_for(case, settings)
    content = case['messages'][0]['content']
    if (not isinstance(content, list) or len(content) != 2
            or content[0].get('type') != 'text' or content[1].get('type') != 'image_url'):
        raise ValueError('Medical VQA requires its original question and one original image')
    return payload


def lock_outputs(folder, cases):
    files = {'run_manifest.json': file_digest(folder / 'run_manifest.json')}
    for case in cases:
        identity = digest([case['task'], case['variant'], case['case_id']])
        for category in ['requests', 'responses']:
            name = category + '/' + identity + '.json'
            path = folder / name
            files[name] = file_digest(path) if path.exists() else None
    record = {'files_sha256': files, 'contract_sha256': digest(files),
              'policy': 'Raw requests, responses and missing slots locked before labels are read; no response selection, answer repair or scoring retries.'}
    path = folder / 'scoring_output_lock.json'
    if path.exists() and json.loads(path.read_text()) != record:
        raise ValueError('Pre-scoring output lock changed; predictions cannot be silently replaced')
    if not path.exists():
        write_json(path, record)
    return record


def locked_record(folder, name, output_lock):
    path = folder / name
    expected = output_lock['files_sha256'][name]
    if expected is None:
        if path.exists():
            raise ValueError('An output appeared after the pre-label lock')
        return None
    raw = path.read_bytes()
    if hashlib.sha256(raw).hexdigest() != expected:
        raise ValueError('An archived output changed after the pre-label lock')
    return json.loads(raw)


def metrics_for(rows):
    metrics, by_group = {}, {}
    for group, metric, item_metric in [('OPEN', 'open_token_recall', 'open_token_recall'),
                                        ('CLOSED', 'closed_accuracy', 'closed_native_hit')]:
        eligible = [row for row in rows if row['answer_type'] == group]
        value = sum(row['native_scores'].get(item_metric, 0.0) for row in eligible) / len(eligible) if eligible else None
        metrics[metric] = value
        by_group[group] = {'metric': metric, 'value': value, 'units': 'fraction_0_1',
                           'eligible': len(eligible), 'completed': sum(row['completed'] for row in eligible),
                           'parsed': sum(row['parsed'] for row in eligible),
                           'invalid_outputs': sum(row['completed'] and not row['parsed'] for row in eligible),
                           'missing_or_failed_outputs': sum(not row['completed'] for row in eligible),
                           'truncated_outputs': sum(row['truncated'] for row in eligible)}
    return metrics, by_group


def score(folder):
    manifest = json.loads((folder / 'run_manifest.json').read_text())
    settings = manifest['configuration']
    approved = settings['approved_task_ids']
    if len(approved) != 1 or approved[0] not in NATIVE_GROUPS:
        raise ValueError('This scorer supports exactly one frozen V01 or V02 run')
    task = approved[0]
    reference_path = ROOT / settings['scorer_reference_file']
    deferred_reference_hashes = []
    for name, expected in settings['frozen_files_sha256'].items():
        if (ROOT / name).resolve() == reference_path.resolve():
            deferred_reference_hashes.append(expected)
        elif file_digest(ROOT / name) != expected:
            raise ValueError('Frozen file changed: ' + name)
    for key in ['input_file', 'review_file']:
        if settings[key] not in settings['frozen_files_sha256']:
            raise ValueError('Missing pre-inference hash for ' + key)
    cases = [json.loads(line) for line in (ROOT / settings['input_file']).read_text().splitlines() if line]
    if not cases or digest(cases) != manifest['case_contract_sha256'] or len(cases) != manifest['planned_cases']:
        raise ValueError('Frozen input contract or planned count changed')
    review = json.loads((ROOT / settings['review_file']).read_text())
    case_ids = [case['case_id'] for case in cases]
    if case_ids != review['approved_case_ids'] or len(set(case_ids)) != len(case_ids):
        raise ValueError('Execution cases differ from the unique ordered review allowlist')
    if set(case_ids) & {row['case_id'] for row in review.get('held_cases', [])}:
        raise ValueError('Held case reached scoring')
    for case in cases:
        expected_payload(case, settings)
    # Label parsing starts only after every raw output/missing slot is locked.
    output_lock = lock_outputs(folder, cases)
    raw_references = reference_path.read_bytes()
    reference_sha256 = hashlib.sha256(raw_references).hexdigest()
    if (reference_sha256 != settings['scorer_reference_sha256']
            or any(reference_sha256 != expected for expected in deferred_reference_hashes)):
        raise ValueError('Scorer references differ from their pre-inference hash')
    references = {}
    for line in raw_references.decode('utf-8').splitlines():
        if not line:
            continue
        ref = json.loads(line)
        identity = (ref['task'], ref['case_id'])
        if identity in references:
            raise ValueError('Duplicate scorer reference identity')
        references[identity] = ref
    statuses, finishes, usage, rows = Counter(), Counter(), Counter(), []
    requests_saved = responses_saved = 0
    for case in cases:
        identity = digest([case['task'], case['variant'], case['case_id']])
        request = locked_record(folder, 'requests/' + identity + '.json', output_lock)
        response = locked_record(folder, 'responses/' + identity + '.json', output_lock)
        requests_saved += int(request is not None)
        responses_saved += int(response is not None)
        payload = expected_payload(case, settings)
        images = validate_content(case['messages'][0]['content'])
        if request is not None:
            if (request.get('request_sha256') != digest(payload)
                    or digest(request.get('payload')) != request['request_sha256']
                    or request.get('supplied_fields') != settings['model_facing_fields']
                    or request.get('image_sha256') != [item['sha256'] for item in images]):
                raise ValueError('Archived request differs from frozen native input')
            for field in ['task', 'case_id', 'variant', 'split']:
                if request.get(field) != case[field]:
                    raise ValueError('Request identity mismatch: ' + field)
        if response is not None:
            if request is None:
                raise ValueError('Response has no corresponding saved request')
            for field, expected in [('task', task), ('case_id', case['case_id']), ('variant', case['variant']),
                                    ('split', case['split']), ('model', settings['model']),
                                    ('model_revision', settings['model_revision']),
                                    ('request_sha256', request['request_sha256'])]:
                if response.get(field) != expected:
                    raise ValueError('Response provenance mismatch: ' + field)
        status = response.get('status') if response is not None else ('interrupted_unknown_completion' if request else 'not_dispatched')
        statuses[status] += 1
        completed = status == 'completed'
        text, finish = None, response.get('finish_reason') if response else None
        if completed:
            api = response.get('response', {})
            choices = api.get('choices', [])
            if response.get('http_status') != 200 or api.get('model') != settings['model'] or len(choices) != 1:
                raise ValueError('Completed record violates single-completion server contract')
            choice = choices[0]
            if response.get('text') != (choice.get('message', {}).get('content') or '') or finish != choice.get('finish_reason'):
                raise ValueError('Saved assistant text/finish reason differs from raw response')
            text = response.get('text')
            finishes[str(finish)] += 1
            for key in ['prompt_tokens', 'completion_tokens', 'total_tokens']:
                usage[key] += api.get('usage', {}).get(key, 0) or 0
        parsed = completed and isinstance(text, str) and bool(text.strip())
        ref = references[(task, case['case_id'])]
        if (ref['answer_type'] not in {'OPEN', 'CLOSED'} or ref.get('variant') != case['variant']
                or ref.get('split') != case['split'] or ref.get('image_sha256') != images[0]['sha256']):
            raise ValueError('Scorer reference group/protocol/image mismatch')
        native_scores = preparation.score_answer(text if parsed else '', ref)
        rows.append({'task': task, 'case_id': case['case_id'], 'status': status, 'completed': completed,
                     'parsed': parsed, 'raw_text': text, 'target_answer': ref['target_answer'],
                     'answer_type': ref['answer_type'], 'native_scores': native_scores, 'finish_reason': finish,
                     'truncated': completed and finish == 'length',
                     'request_sha256': request['request_sha256'] if request else None})
    metrics, by_group = metrics_for(rows)
    completed = sum(row['completed'] for row in rows)
    full_native = {group: data['eligible'] for group, data in by_group.items()} == NATIVE_GROUPS[task] and not review.get('held_cases')
    scope = ('full_native_test' if full_native else 'frozen_reviewed_test_subset') if completed == len(cases) else 'INCOMPLETE_frozen_reviewed_case_set'
    summary = {'run_id': settings['run_id'], 'task_id': task, 'model': settings['model'],
               'model_revision': settings['model_revision'], 'protocol_variant': settings['variant'],
               'input_modalities': ['image', 'question_text'], 'planned': len(cases),
               'native_full_test_case_count': sum(NATIVE_GROUPS[task].values()),
               'full_native_test_inputs': full_native,
               'requests_saved': requests_saved, 'responses_saved': responses_saved,
               'completed': completed, 'parsed': sum(row['parsed'] for row in rows),
               'invalid_outputs': sum(row['completed'] and not row['parsed'] for row in rows),
               'missing_or_failed_outputs': sum(not row['completed'] for row in rows),
               'truncated_outputs': sum(row['truncated'] for row in rows),
               'statuses': dict(statuses), 'finish_reasons': dict(finishes), 'token_usage': dict(usage),
               'case_scope': scope, 'held_before_inference': len(review.get('held_cases', [])),
               'metrics': metrics, 'metrics_by_answer_type': by_group, 'metric_units': 'fraction_0_1; multiply by100 for paper percentages',
               'scoring_output_lock_sha256': output_lock['contract_sha256'],
               'predictions_locked_before_reference_read': True, 'request_response_hash_audit': 'passed',
               'explanation_support_score': None,
               'failure_policy': 'Every frozen eligible case remains in its native group denominator; missing, failed and empty/nontext final outputs score0. Truncated final text is scored as observed under native rules and reported separately.',
               'parser_policy': 'Full final assistant content; no answer-key-assisted extraction, reference-based response selection, candidate remapping or paid grader.',
               'native_scoring_quirks': 'Official OPEN headline is normalized token recall. CLOSED uses the original yes/no substring rule, including ambiguous/substring matches; it is not strict exact match. No combined overall accuracy mixes these unlike metrics.',
               'comparison_to_paper': 'Original native test split/images/questions and pinned LLaVA-Medv1 normalization/scoring; Qwen is a declared zero-shot vision baseline with its own chat template/generation and no downstream tuning. Compare OPEN recall and CLOSED accuracy separately; full-test claim requires complete native inputs and outputs.',
               'interpretation': {'task_demands': {'labels': ['visual_evidence_interpretation', 'medical_knowledge', 'question_answering'],
                                    'status': 'provisional analyst description; no inference about internal computation'},
                                  'actually_supplied': 'Archived original question text and original image bytes only; no label group, answer options, reference captions, tool calls or scorer labels.',
                                  'reference_answer_source': 'Clinician-authored public VQA-RAD/SLAKE annotations, hashed before inference and parsed only by offline scorer.',
                                  'good_score_establishes': 'Recovery of reference answers under the declared visual input and native group metric.',
                                  'bad_score_establishes': 'Limited recovery under this input/scoring regime; does not isolate general reasoning or establish clinical usefulness.',
                                  'explanation_correctness': 'Unassessed; correct answer recovery does not validate its rationale, and absent support does not establish falsity.'},
               'contamination': 'No labels in requests, training, retrieval or test-feedback prompt changes; pretraining exposure to these public benchmarks remains unknown.'}
    write_json(folder / 'scores.json', summary)
    write_json(folder / 'per_case_scores.json', rows)
    with (folder / 'metrics.csv').open('w', newline='') as handle:
        columns = ['run_id', 'task_id', 'protocol_variant', 'model', 'answer_type', 'metric', 'value',
                   'units', 'eligible', 'planned', 'completed', 'parsed', 'invalid_outputs',
                   'missing_or_failed_outputs', 'truncated_outputs', 'case_scope']
        writer = csv.DictWriter(handle, fieldnames=columns)
        writer.writeheader()
        for group, values in by_group.items():
            writer.writerow({**{key: summary[key] for key in ['run_id', 'task_id', 'protocol_variant', 'model', 'planned', 'case_scope']},
                             'answer_type': group, **values})
    print(json.dumps(summary, ensure_ascii=False), flush=True)
    return summary


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--run', required=True)
    args = parser.parse_args()
    score(ROOT / 'results/runs' / args.run)
