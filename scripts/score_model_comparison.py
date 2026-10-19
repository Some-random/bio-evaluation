"""Offline paired scoring. Validate complete prediction locks before reading labels.

No networking, inference, retries, model-output repair or mutation of original runs.
The scoring plan pins candidates, case manifest, answer policy, actual request file,
and both complete prediction locks by file SHA-256. Source references are opened
only after all model artifacts and their case/run/request associations validate.
"""
import argparse
import ast
from collections import Counter, defaultdict
from datetime import datetime
import hashlib
import json
import math
from pathlib import Path
import random
import re
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parents[1]
LAB_TASKS = {'B01', 'B03', 'B04', 'B05'}
# Vision requires a separate image-byte/order contract before this scorer enables it.
SUPPORTED = {'B01', 'B03', 'P03'}


def canonical(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(',', ':')).encode()


def digest(value):
    return hashlib.sha256(canonical(value)).hexdigest()


def file_sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read_json(path):
    return json.loads(Path(path).read_text())


def artifact(root, record):
    """Read only a pinned real artifact; paths may be repository-relative."""
    path = Path(record['path'])
    path = path if path.is_absolute() else Path(root) / path
    if not path.is_file() or file_sha(path) != record['sha256']:
        raise ValueError('Missing or hash-mismatched artifact: ' + str(path))
    return path


def inside(root, name):
    path = (Path(root) / name).resolve()
    if not path.is_relative_to(Path(root).resolve()):
        raise ValueError('Prediction artifact leaves sealed directory')
    return path


def native_lab_answer(text, n, pattern):
    """Exact deterministic port of frozen score_results.lab_answer."""
    if not 1 <= n <= 26:
        raise ValueError('Invalid LAB choice count')
    alphabet = [chr(i) for i in range(65, 91)]
    matches = sorted(set(re.findall(pattern, text, re.DOTALL)))
    if matches:
        prepared = str(matches)
    elif text in alphabet:
        prepared = text
    elif ',' in text:
        split = text.split(',')
        prepared = ','.join(split) if all(x.strip() in alphabet for x in split) else ''
    elif ' ' in text:
        split = text.split(' ')
        prepared = ','.join(split) if all(x.strip() in alphabet for x in split) else ''
    else:
        prepared = ''
    found = re.search('[' + ''.join(alphabet[:n]) + ']', prepared)
    return found.group(0) if found else None


def unambiguous_lab_answer(text, n):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'[:n]
    # Marker pairs must match. Catch malformed or unsupported answer markers too.
    marker = re.compile(r'\[/?(?:ANSWER|ANS)\]|</?(?:ANSWER|ANS|ans)>')
    tokens = list(marker.finditer(text))
    pairs = {'[ANSWER]': '[/ANSWER]', '[ANS]': '[/ANS]',
             '<ANSWER>': '</ANSWER>', '<ANS>': '</ANS>', '<ans>': '</ans>'}
    if not tokens:
        return text if text in alphabet and len(text) == 1 else None
    if len(tokens) % 2:
        return None
    answers = []
    for opening, closing in zip(tokens[::2], tokens[1::2]):
        if pairs.get(opening.group()) != closing.group():
            return None
        value = text[opening.end():closing.start()].strip()
        if len(value) != 1 or value not in alphabet:
            return None
        answers.append(value)
    return answers[0] if len(set(answers)) == 1 else None


def p03_answer(text):
    found = re.fullmatch(r'\s*(?:Answer\s*:\s*)?([0-9])\.?\s*', text, re.IGNORECASE)
    return int(found.group(1)) if found else None


def extract_response(raw, style):
    """Read final channel only, deriving failure flags from actual raw response."""
    if style == 'qwen_archive':
        body = raw.get('response')
        if not isinstance(body, dict):
            return '', False, False, False, raw.get('http_status'), 'missing_response'
        choices = body.get('choices', [])
        if len(choices) != 1:
            raise ValueError('Require one archived response choice')
        choice = choices[0]
        message = choice.get('message') or {}
        final = message.get('content') or ''
        if not isinstance(final, str):
            raise ValueError('Nontext visible final')
        finish = choice.get('finish_reason')
        refused = bool(message.get('refusal'))
        truncated = finish == 'length'
        complete = raw.get('status') == 'completed' and finish == 'stop'
        return final, complete, truncated, refused, raw.get('http_status'), finish
    if style != 'openai_responses':
        raise ValueError('Unknown response format')
    outputs = raw.get('output', [])
    final_parts, refused = [], False
    for output in outputs:
        if output.get('type') == 'refusal':
            refused = True
        if output.get('type') == 'message':
            if output.get('role') != 'assistant':
                raise ValueError('Unexpected output role')
            for content in output.get('content', []):
                if content.get('type') == 'output_text':
                    final_parts.append(content.get('text', ''))
                elif content.get('type') == 'refusal':
                    refused = True
    final = '\n'.join(final_parts)
    status = raw.get('status')
    incomplete = (raw.get('incomplete_details') or {}).get('reason')
    truncated = status == 'incomplete' and incomplete == 'max_output_tokens'
    return final, status == 'completed', truncated, refused, None, status


def load_selection(root, candidates, manifest, tasks):
    """Verify original case manifests and source run identities without labels."""
    if not tasks or not set(tasks) <= SUPPORTED:
        raise ValueError('Unsupported or empty comparison task list')
    selected = {t['task_id']: t for t in candidates['tasks'] if t['task_id'] in tasks}
    if set(selected) != set(tasks):
        raise ValueError('Missing candidate task')
    cases = [row for row in manifest if row['task_id'] in tasks]
    keys = [(r['task_id'], r['case_id']) for r in cases]
    if len(keys) != len(set(keys)):
        raise ValueError('Duplicate case manifest entry')
    for task, candidate in selected.items():
        run_path = artifact(root, candidate['run_artifacts']['run_manifest.json'])
        source = read_json(run_path)
        config = source['configuration']
        if config['run_id'] != candidate['source_qwen_run_id']:
            raise ValueError('Wrong original run')
        if config['variant'] != candidate['source_protocol_variant']:
            raise ValueError('Wrong original protocol')
        if config['model'] != candidate['model'] or config['model_revision'] != candidate['model_revision']:
            raise ValueError('Wrong original model identity')
        input_path = artifact(root, candidate['frozen_input_artifact'])
        inputs = [json.loads(line) for line in input_path.read_text().splitlines() if line]
        task_inputs = [r for r in inputs if r.get('task', r.get('task_id')) == task]
        # Some aggregate P03 manifests pin a case contract at the aggregate level.
        if digest(inputs) != candidate['frozen_case_contract_sha256']:
            raise ValueError('Original input contract mismatch')
        expected = [r['case_id'] for r in task_inputs]
        observed = [r['case_id'] for r in cases if r['task_id'] == task]
        if expected != observed or len(expected) != candidate['counts']['planned']:
            raise ValueError('Exact source case set/order mismatch')
        if digest(expected) != candidate['source_case_ids_sha256']:
            raise ValueError('Original ordered case identity hash mismatch')
        # Bind label archive hash to original frozen config, not a reconstructed label file.
        if config.get('scorer_reference_sha256') != candidate['source_reference_archive']['sha256']:
            raise ValueError('Reference hash not pinned by original run')
    for case in cases:
        case['source_model_revision'] = selected[case['task_id']]['model_revision']
        if case['task_id'] == 'B03':
            source = selected['B03']['frozen_input_artifact']
            # DOI is legitimate frozen task metadata, not selected using answer labels.
            if 'b03_dois' not in locals():
                b03_dois = {}
                for line in artifact(root, source).read_text().splitlines():
                    item = json.loads(line)
                    messages = item.get('messages', [])
                    text = messages[0].get('content', '') if messages else ''
                    match = re.search(r'^DOI:\s*(\S+)\s*$', text, re.MULTILINE)
                    b03_dois[item['case_id']] = match.group(1).lower().rstrip('/') if match else None
            case['comparison_group_id'] = b03_dois[case['case_id']]
    return selected, cases


def validate_lock(root, lock_artifact, cases, expected, request_rows=None):
    """Must finish for both models before any source-reference file is opened."""
    path = artifact(root, lock_artifact)
    seal = path.with_suffix('.sha256')
    if not seal.is_file() or seal.read_text().strip().split()[0] != lock_artifact['sha256']:
        raise ValueError('Missing or inconsistent prediction-lock seal')
    lock = read_json(path)
    if lock.get('scoring_performed') is not False:
        raise ValueError('Prediction set must be locked before scoring')
    for key in ('run_id', 'model', 'protocol_id'):
        if lock.get(key) != expected[key]:
            raise ValueError('Wrong locked ' + key)
    keys = [(c['task_id'], c['case_id']) for c in cases]
    rows = lock.get('rows', [])
    if lock.get('case_count') != len(keys) or [(r['task_id'], r['case_id']) for r in rows] != keys:
        raise ValueError('Incomplete, reordered or substituted prediction set')
    verified = []
    for row, case in zip(rows, cases):
        for key in ('run_id', 'model', 'protocol_id'):
            if row.get(key) != lock[key]:
                raise ValueError('Wrong per-case locked identity')
        files = {}
        for name in ('request', 'response', 'visible_final'):
            file = inside(path.parent, row[name + '_path'])
            if not file.is_file() or file_sha(file) != row[name + '_sha256']:
                raise ValueError('Missing or hash-mismatched locked ' + name)
            files[name] = file
        request = read_json(files['request'])
        terminal = row['terminal_status']
        style = expected['response_style']
        raw = read_json(files['response']) if style == 'qwen_archive' or terminal not in {'transport_error', 'http_error', 'response_error', 'not_dispatched'} else {}
        if style == 'qwen_archive':
            payload = request['payload']
            if request.get('task') != case['task_id'] or request.get('case_id') != case['case_id']:
                raise ValueError('Wrong original request case')
            if raw.get('task') != case['task_id'] or raw.get('case_id') != case['case_id']:
                raise ValueError('Wrong original response case')
            if row.get('original_run_id') != case['source_qwen_run_id'] or raw.get('model_revision') != case['source_model_revision']:
                raise ValueError('Wrong archived run/model revision')
            if raw.get('model') != lock['model'] or raw.get('variant') != case['source_protocol_variant']:
                raise ValueError('Wrong original response model/protocol')
            if request['request_sha256'] != digest(payload) or raw.get('request_sha256') != digest(payload):
                raise ValueError('Original request/response association mismatch')
            if row['request_sha256'] != case['request_artifact']['sha256'] or row['response_sha256'] != case['response_artifact']['sha256']:
                raise ValueError('Archived response substitution')
            expected_hash = case['request_payload_sha256']
        else:
            payload = request.get('payload_without_private_safety_identifier')
            if payload is None:
                raise ValueError('Submitted payload record missing')
            frozen = request_rows[(case['task_id'], case['case_id'])]
            expected_hash = frozen.get('payload_sha256', frozen.get('draft_payload_sha256'))
            if payload != frozen['payload_without_private_safety_identifier']:
                raise ValueError('Actual submitted request differs from frozen payload')
            if payload.get('model') != lock['model']:
                raise ValueError('Wrong payload model')
        if digest(payload) != expected_hash or row['payload_sha256'] != expected_hash:
            raise ValueError('Wrong locked payload hash')
        final = files['visible_final'].read_text()
        # Transport/HTTP errors are recorded as error artifacts, never parsed as answers.
        terminal = row['terminal_status']
        if terminal in {'transport_error', 'http_error', 'response_error', 'not_dispatched'}:
            if final and terminal in {'transport_error', 'http_error', 'not_dispatched'}:
                raise ValueError('Non-response error artifact contains a final')
            complete, truncated, refused, http, finish = False, False, False, row.get('http_status'), terminal
        else:
            if style == 'openai_responses' and raw.get('model') not in expected.get('response_models', [lock['model']]):
                raise ValueError('Wrong actual response model')
            extracted, complete, truncated, refused, http, finish = extract_response(raw, style)
            if final != extracted:
                raise ValueError('Saved final differs from actual response final')
            if bool(row.get('truncated')) != truncated or bool(row.get('refused')) != refused:
                raise ValueError('Response failure flags inconsistent with raw body')
            if style == 'qwen_archive' and http != row.get('http_status'):
                raise ValueError('HTTP status mismatch')
        if bool(row.get('empty_final')) != (not bool(final.strip())):
            raise ValueError('Empty-final field mismatch')
        good = complete and not truncated and not refused and row.get('http_status') == 200 and bool(final.strip())
        verified.append(dict(row, text=final, delivery_valid=good,
                             observed_truncated=truncated, observed_refused=refused, observed_finish=finish))
    return lock, verified


def load_references(root, selected, cases, policy):
    """Only call after complete prediction-lock validation for both models."""
    references = {}
    pins = []
    for task, candidate in selected.items():
        reference_path = artifact(root, candidate['source_reference_archive'])
        pins.append(candidate['source_reference_archive'])
        task_refs = [json.loads(line) for line in reference_path.read_text().splitlines() if line]
        for row in task_refs:
            if row.get('task') == task:
                key = (task, row['case_id'])
                if key in references:
                    raise ValueError('Duplicate source reference')
                references[key] = row
        if task in LAB_TASKS:
            # Original frozen constants and their AST literal must agree with the policy.
            run = read_json(artifact(root, candidate['run_artifacts']['run_manifest.json']))
            expected = run['configuration']['frozen_files_sha256']['sources/chembench_constant.py']
            if expected != policy['native_lab']['constant_sha256']:
                raise ValueError('Native scorer constant changed across conditions')
    selected_refs = []
    for case in cases:
        key = (case['task_id'], case['case_id'])
        if key not in references:
            raise ValueError('Missing original reference: ' + str(key))
        row = references[key]
        if case['task_id'] == 'P03':
            if type(row.get('target')) is not int or not 0 <= row['target'] <= 9:
                raise ValueError('Invalid P03 class reference')
        else:
            n = row.get('choice_count')
            if type(n) is not int or not 1 <= n <= 26:
                raise ValueError('Invalid choice count')
            allowed = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'[:n]
            if row.get('target_choice') not in allowed or row.get('unsure_choice') not in allowed:
                raise ValueError('Invalid native target/abstention reference')
        selected_refs.append(row)
    return selected_refs, pins


def score_one(rows, references, pattern):
    result = []
    for row, ref in zip(rows, references):
        task = row['task_id']
        valid = row['delivery_valid']
        if task == 'P03':
            native = p03_answer(row['text']) if valid else None
            strict = native
            target, unsure = ref['target'], None
        else:
            native = native_lab_answer(row['text'], ref['choice_count'], pattern) if valid else None
            strict = unambiguous_lab_answer(row['text'], ref['choice_count']) if valid else None
            target, unsure = ref['target_choice'], ref['unsure_choice']
        result.append({'task_id': task, 'case_id': row['case_id'],
                       'native_answer': native, 'unambiguous_answer': strict,
                       'native_correct': native is not None and native == target,
                       'unambiguous_correct': strict is not None and strict == target,
                       'parsed_abstention': native is not None and native == unsure,
                       'delivery_valid': valid, 'truncated': row['observed_truncated'],
                       'refused': row['observed_refused'], 'empty_final': row['empty_final'],
                       'terminal_status': row['terminal_status'], 'http_status': row['http_status'],
                       'group_id': ref.get('group_id')})
    return result


def metrics(rows):
    n = len(rows)
    if n == 0:
        raise ValueError('Empty task cannot be scored')
    correct = sum(r['native_correct'] for r in rows)
    strict_correct = sum(r['unambiguous_correct'] for r in rows)
    parsed = sum(r['native_answer'] is not None for r in rows)
    strict = sum(r['unambiguous_answer'] is not None for r in rows)
    abstain = sum(r['parsed_abstention'] for r in rows)
    # Native LAB coverage counts invalid answers as non-abstaining; do not call it usability.
    sure = n - abstain
    return {'planned': n, 'native_correct': correct, 'native_accuracy': correct / n,
            'unambiguous_correct': strict_correct, 'unambiguous_accuracy': strict_correct / n,
            'native_parsed': parsed, 'usable_answer_rate': parsed / n,
            'unambiguous_parsed': strict, 'unambiguous_answer_rate': strict / n,
            'explicit_parsed_abstentions': abstain,
            'native_non_abstention_coverage': sure / n if rows[0]['task_id'] in LAB_TASKS else None,
            'native_non_abstention_precision': (correct / sure if sure else 0.0) if rows[0]['task_id'] in LAB_TASKS else None,
            'transport_or_server_errors': sum(r['terminal_status'] in {'transport_error', 'http_error', 'response_error'} or (r['http_status'] is not None and r['http_status'] != 200) for r in rows),
            'not_dispatched': sum(r['terminal_status'] == 'not_dispatched' for r in rows),
            'truncations': sum(r['truncated'] for r in rows),
            'empty_finals': sum(r['empty_final'] for r in rows),
            'refusals': sum(r['refused'] for r in rows),
            'denominator_policy': 'Every declared case; failures/invalid answers incorrect, explicit abstentions parsed.'}


def exact_mcnemar(openai_only, qwen_only):
    n = openai_only + qwen_only
    if not n:
        return 1.0
    # Sum in log space: avoid underflow/overflow for large discordance counts.
    k = min(openai_only, qwen_only)
    terms = [math.lgamma(n + 1) - math.lgamma(i + 1) - math.lgamma(n - i + 1) - n * math.log(2) for i in range(k + 1)]
    peak = max(terms)
    return min(1.0, 2 * math.exp(peak) * sum(math.exp(t - peak) for t in terms))


def quantile(values, p):
    pos = (len(values) - 1) * p
    low, high = math.floor(pos), math.ceil(pos)
    return values[low] + (values[high] - values[low]) * (pos - low)


def paired_analysis(qwen, openai, key, *, replicates=10000, seed=20261019, confidence=.95, grouping='case'):
    if len(qwen) != len(openai) or not qwen:
        raise ValueError('Nonempty exact paired case set required')
    counts = Counter()
    differences, groups = [], defaultdict(list)
    for i, (left, right) in enumerate(zip(qwen, openai)):
        if (left['task_id'], left['case_id']) != (right['task_id'], right['case_id']):
            raise ValueError('Paired case identity mismatch')
        a, b = bool(left[key]), bool(right[key])
        counts['both_correct' if a and b else 'openai_only_correct' if b else 'qwen_only_correct' if a else 'both_wrong'] += 1
        differences.append(int(b) - int(a))
        group = left.get('group_id')
        if grouping == 'group' and (group is None or right.get('group_id') != group):
            raise ValueError('Complete matching group metadata required for clustered uncertainty')
        groups[group if grouping == 'group' else i].append(i)
    if grouping not in {'case', 'group'} or replicates < 100 or not 0 < confidence < 1:
        raise ValueError('Invalid frozen uncertainty settings')
    units = list(groups.values())
    rng, bootstrap = random.Random(seed), []
    # Resample matched units, preserve both models within each sampled case/group.
    for _ in range(replicates):
        sample = [index for _ in units for index in rng.choice(units)]
        bootstrap.append(sum(differences[i] for i in sample) / len(sample))
    bootstrap.sort()
    alpha = (1 - confidence) / 2
    return {**{name: counts[name] for name in ('both_correct', 'openai_only_correct', 'qwen_only_correct', 'both_wrong')},
            'openai_minus_qwen_accuracy': sum(differences) / len(differences),
            'mcnemar_exact_two_sided_p': exact_mcnemar(counts['openai_only_correct'], counts['qwen_only_correct']),
            'mcnemar_scope': 'Conditional exact paired discordance test; case-independence assumption is not guaranteed by public benchmarks.',
            'paired_bootstrap_percentile_interval': [quantile(bootstrap, alpha), quantile(bootstrap, 1 - alpha)],
            'bootstrap_replicates': replicates, 'seed': seed, 'confidence': confidence,
            'resampling_unit': 'scorer_group_id' if grouping == 'group' else 'case', 'resampling_unit_count': len(units),
            'uncertainty_scope': 'Fixed selected benchmark and one generation per model; not training-contamination assurance, independent biological experiments, or across-run variance.'}


def score_comparison(plan_path, root=ROOT):
    plan_path = Path(plan_path)
    plan = read_json(plan_path)
    candidates = read_json(artifact(root, plan['candidates']))
    case_file = artifact(root, plan['case_manifest'])
    cases_all = [json.loads(line) for line in case_file.read_text().splitlines() if line]
    policy_path = artifact(root, plan['answer_policy'])
    policy = read_json(policy_path)
    if not policy.get('frozen_before_new_benchmark_inference') or policy.get('references_used_to_select_rule'):
        raise ValueError('Answer policy not frozen without test-label guidance')
    selected, cases = load_selection(root, candidates, cases_all, plan['tasks'])
    if set(plan['tasks']) & LAB_TASKS:
        constant_path = artifact(root, plan['native_constant'])
        if file_sha(constant_path) != policy['native_lab']['constant_sha256']:
            raise ValueError('Frozen native constant hash mismatch')
        patterns = [ast.literal_eval(node.value) for node in ast.parse(constant_path.read_text()).body
                    if isinstance(node, ast.Assign) and any(isinstance(x, ast.Name) and x.id == 'MCQ_REGEX_TEMPLATE_1' for x in node.targets)]
        if patterns != [policy['native_lab']['regex']]:
            raise ValueError('Policy parser differs from frozen native constant')
    protocol_path = artifact(root, plan['frozen_protocol'])
    frozen_protocol = read_json(protocol_path)
    if frozen_protocol.get('protocol_id') != plan['openai']['protocol_id']:
        raise ValueError('Wrong original frozen protocol')
    request_path = artifact(root, plan['frozen_request_file'])
    requests = [json.loads(line) for line in request_path.read_text().splitlines() if line]
    request_rows = {(r['task_id'], r['case_id']): r for r in requests}
    if len(request_rows) != len(requests) or list(request_rows) != [(c['task_id'], c['case_id']) for c in cases]:
        raise ValueError('Frozen request cohort differs from exact selected cases')
    for row in requests:
        if digest(row['payload_without_private_safety_identifier']) != row.get('payload_sha256', row.get('draft_payload_sha256')):
            raise ValueError('Frozen request payload hash mismatch')
    qlock, qrows = validate_lock(root, plan['qwen']['lock'], cases, plan['qwen'])
    olock, orows = validate_lock(root, plan['openai']['lock'], cases, plan['openai'], request_rows)
    if olock.get('frozen_protocol_sha256') != plan['frozen_protocol']['sha256']:
        raise ValueError('Prediction lock belongs to a different frozen protocol')
    if olock.get('frozen_request_file_sha256') != plan['frozen_request_file']['sha256']:
        raise ValueError('Prediction lock belongs to a different frozen request file')
    for case, qrow in zip(cases, qrows):
        original = read_json(inside(Path(artifact(root, plan['qwen']['lock'])).parent, qrow['request_path']))['payload']
        messages = original.get('messages')
        frozen = request_rows[(case['task_id'], case['case_id'])]['payload_without_private_safety_identifier']
        if (not isinstance(messages, list) or len(messages) != 1 or messages[0].get('role') != 'user'
                or not isinstance(messages[0].get('content'), str)):
            raise ValueError('Separate modality protocol required for original request')
        expected_input = [{'role': 'user', 'content': [{'type': 'input_text', 'text': messages[0]['content']}]}]
        if frozen.get('input') != expected_input:
            raise ValueError('Frozen provider input differs from original user prompt/choice order')
    # No references have been opened before this exact point.
    references, reference_pins = load_references(root, selected, cases, policy)
    references = [dict(ref, group_id=case.get('comparison_group_id', ref.get('group_id'))) for ref, case in zip(references, cases)]
    qscored = score_one(qrows, references, policy['native_lab']['regex'])
    oscored = score_one(orows, references, policy['native_lab']['regex'])
    uncertainty = policy['uncertainty']
    output = {'schema_version': 1, 'comparison_id': plan['comparison_id'],
              'scored_at_pacific': datetime.now(ZoneInfo('America/Los_Angeles')).isoformat(),
              'source_plan_sha256': file_sha(plan_path), 'answer_policy_sha256': file_sha(policy_path),
              'reference_artifacts': reference_pins, 'predictions_locked_before_references_opened': True,
              'qwen_prediction_lock_sha256': plan['qwen']['lock']['sha256'],
              'openai_prediction_lock_sha256': plan['openai']['lock']['sha256'],
              'qwen_run_id': qlock['run_id'], 'openai_run_id': olock['run_id'],
              'new_inference_calls': 0, 'original_scores_modified': False, 'tasks': {},
              'interpretation': 'Matched fixed-input public-task comparison. Inference-time answer separation can be audited; prior benchmark exposure is unknown for both models. Explanations and novel-protein generalization unassessed.'}
    for task in plan['tasks']:
        qtask = [r for r in qscored if r['task_id'] == task]
        otask = [r for r in oscored if r['task_id'] == task]
        default_grouping = 'group' if all(r.get('group_id') is not None for r in qtask) else 'case'
        group_policy = plan.get('uncertainty_grouping', {}).get(task, default_grouping)
        options = dict(replicates=uncertainty['bootstrap_replicates'], seed=uncertainty['seed'], confidence=uncertainty['confidence'], grouping=group_policy)
        output['tasks'][task] = {'qwen': metrics(qtask), 'openai': metrics(otask),
             'native_paired': paired_analysis(qtask, otask, 'native_correct', **options),
             'unambiguous_paired': paired_analysis(qtask, otask, 'unambiguous_correct', **options),
             'per_case': [{'task_id': task, 'case_id': q['case_id'], 'qwen': q, 'openai': o} for q, o in zip(qtask, otask)]}
    return output



def export_qwen_lock(candidates_path, manifest_path, tasks, output_dir, *, root=ROOT,
                     protocol_id='openai_qwen_publicqa_4k_2026-10-19_v2',
                     run_id='archived_qwen_publicqa_panel_2026-10-19_v2'):
    """Copy and seal exact archived prediction artifacts, without opening labels.

    Input file hashes belong in the subsequently frozen scoring plan. Never feed
    this analysis-side bundle or the case manifest to the evaluated model.
    """
    candidates, all_cases = read_json(candidates_path), []
    for line in Path(manifest_path).read_text().splitlines():
        if line:
            all_cases.append(json.loads(line))
    selected, cases = load_selection(root, candidates, all_cases, tasks)
    models = {c['model'] for c in selected.values()}
    if len(models) != 1:
        raise ValueError('Archived panel contains different models')
    output = Path(output_dir)
    if output.exists():
        raise FileExistsError('Refuse to replace archived prediction lock')
    output.mkdir(parents=True)
    model = next(iter(models))
    rows = []
    for i, case in enumerate(cases):
        request_path = artifact(root, case['request_artifact'])
        response_path = artifact(root, case['response_artifact'])
        request, response = read_json(request_path), read_json(response_path)
        final, complete, truncated, refused, http, finish = extract_response(response, 'qwen_archive')
        prefix = 'artifacts/' + str(i).zfill(6)
        target = output / prefix
        target.mkdir(parents=True)
        for name, source in [('request.json', request_path), ('response.json', response_path)]:
            (target / name).write_bytes(source.read_bytes())
        (target / 'final.txt').write_text(final)
        row = dict(task_id=case['task_id'], case_id=case['case_id'], protocol_id=protocol_id,
                   model=model, run_id=run_id, original_run_id=case['source_qwen_run_id'],
                   payload_sha256=digest(request['payload']),
                   terminal_status='http_error' if http != 200 else 'completed',
                   finish_status=finish, empty_final=not bool(final.strip()),
                   truncated=truncated, refused=refused, http_status=http)
        for name, filename in [('request', 'request.json'), ('response', 'response.json'), ('visible_final', 'final.txt')]:
            row[name + '_path'] = prefix + '/' + filename
            row[name + '_sha256'] = file_sha(target / filename)
            (target / filename).chmod(0o444)
        rows.append(row)
    lock = dict(schema_version=1, protocol_id=protocol_id, model=model, run_id=run_id,
                case_count=len(rows), completed_at_pacific=datetime.now(ZoneInfo('America/Los_Angeles')).isoformat(),
                scoring_performed=False, archive_only_no_inference=True,
                original_case_manifest_sha256=file_sha(manifest_path),
                original_candidates_sha256=file_sha(candidates_path), rows=rows)
    lock_path = output / 'predictions_lock.json'
    lock_path.write_text(json.dumps(lock, ensure_ascii=False, indent=2) + '\n')
    lock_sha = file_sha(lock_path)
    lock_path.with_suffix('.sha256').write_text(lock_sha + '\n')
    lock_path.chmod(0o444)
    lock_path.with_suffix('.sha256').chmod(0o444)
    return {'path': str(lock_path), 'sha256': lock_sha, 'case_count': len(rows)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--plan', required=True)
    parser.add_argument('--output', required=True)
    parser.add_argument('--root', type=Path, default=ROOT)
    args = parser.parse_args()
    output = Path(args.output)
    if output.exists():
        raise FileExistsError('Refuse to replace existing comparison score')
    scored = score_comparison(args.plan, args.root)
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open('x') as stream:
        json.dump(scored, stream, ensure_ascii=False, indent=2)
        stream.write('\n')
    print(json.dumps({'output': str(output), 'sha256': file_sha(output), 'task_ids': list(scored['tasks'])}))


if __name__ == '__main__':
    main()
