"""Render a decision table from aggregate results and verified subset metadata.

No raw requests, answers, labels, inference, scoring or existing report mutation.
Every retained setting appears; repeated runs and extraction conditions stay
separate. A missing verified score is never interpreted as an unattempted task.
"""
from __future__ import annotations

import argparse
import copy
from datetime import datetime
import hashlib
import json
import math
from pathlib import Path
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parents[1]
SCORES = 'reports/RESULTS_AT_A_GLANCE.json'
CATALOG = 'reports/TASK_HIERARCHY_DATA.json'
REACTION_DIAGNOSTIC = 'reports/REACTION_EXTRACTION_DIAGNOSTIC_2026-10-19.json'
RECOVERED_SUBSET_EVIDENCE = 'reports/RECOVERED_SUBSET_EVIDENCE_2026-10-19.json'
OUTPUT_JSON = 'reports/EVALUATION_DECISION_TABLE.json'
OUTPUT_MD = 'reports/EVALUATION_DECISION_TABLE.md'
ARCHIVE_IDS = {'N01', 'N02', 'N03', 'N04', 'N05', 'P28', 'P29'}
COUNT_METRICS = {'correct', 'planned', 'parsed', 'missing', 'invalid', 'total', 'invalid_outputs', 'missing_or_failed_outputs', 'undefined_constant_or_insufficient', 'valid_cases', 'planned_cases', 'case_count'}
PERCENT_METRICS = {'accuracy', 'strict_accuracy', 'precision', 'coverage', 'closed_accuracy', 'closed_accuracy_corrected', 'strict_final_label_accuracy', 'native_td_final_character_accuracy', 'adapted_full_text_closest_choice_accuracy', 'adapted_full_text_released_label_accuracy'}
INPUTS = {
    'P01': 'Protein sequence → Yes/No; zero-shot',
    'P02': 'Protein sequence → binary localization; zero-shot',
    'P03': 'Protein sequence → localization class; zero-shot',
    'P07': 'Protein sequence → fluorescence scalar; zero-shot',
    'P08': 'Protein sequence → stability scalar; zero-shot',
    'P12': 'Protein sequence → enzyme-label confidence scores; zero-shot',
    'P13': 'Protein sequence → biological-process confidence scores; zero-shot',
    'P14': 'Protein sequence → molecular-function confidence scores; zero-shot',
    'P15': 'Protein sequence → cellular-component confidence scores; zero-shot',
    'P16': 'Protein sequence + reaction descriptions → class ID; zero-shot',
    'P19': 'Reference protein + objective → single substitutions',
    'P20': 'Reference + objective + candidate combinations; no measured targets',
    'P21': 'Measured anchor mutant + extending candidate combinations',
    'P22': 'Single-mutant measurements + candidate combinations',
    'P31': 'Protein + desired effect + supplied mutation position',
    'P32': 'Protein + desired effect; mutation position unknown',
    'P34': 'Protein + optimization objective; iterative proposals',
    'P35': 'Functional description + protein retrieval collection',
    'P36': 'Functional description → protein sequence',
    'P37': 'Unconditional protein-sequence generation',
    'P38': 'Requested stability/solubility property → protein sequence',
    'P39': 'Heme-related conditioning → protein sequence',
    'P44': 'Generated explanation + reference evidence; review contract unverified',
    'P42': 'Reference protein → candidate JSON; zero-shot',
    'P43': 'Molecule + protein → conditional Yes/No likelihood',
    'B01': 'Question + choices; native CoT, no tools',
    'B02': 'Question + choices; native CoT, no tools',
    'B03': 'Question + paper metadata + choices; native CoT, no tools',
    'B04': 'Figure image + question + choices; native CoT, no tools',
    'B05': 'Table images + question + choices; native CoT, no tools',
    'B06': 'Full protocol + scenario + question + choices',
    'B07': 'Sequence + question + choices; native CoT, no tools',
    'B08': 'Cloning scenario + choices; native CoT, no tools',
    'V01': 'Radiology image + question; zero-shot',
    'V02': 'Medical image + English question; zero-shot',
    'V03': 'Pathology image + question; zero-shot; 6,719-row released mirror',
    'V04': 'Medical image + question; whole-final exact-match scoring',
    'V05': 'Scientific figure + question + four choices; zero-shot',
    'V07': 'Document / figure → extracted information',
}


def finite(value):
    return isinstance(value, (int, float)) and not isinstance(value, bool) and math.isfinite(value)


def pacific(value):
    if not value:
        return 'unrecorded'
    moment = datetime.fromisoformat(value.replace('Z', '+00:00'))
    if moment.tzinfo is None:
        raise ValueError('Source timestamp needs a timezone')
    return moment.astimezone(ZoneInfo('America/Los_Angeles')).strftime('%Y-%m-%d %H:%M %Z')


def metric_items(metrics, prefix=''):
    for key, value in metrics.items():
        name = prefix + key
        if key in COUNT_METRICS or key.startswith('n_') or isinstance(value, bool):
            continue
        if isinstance(value, dict):
            yield from metric_items(value, name + '.')
        elif value is None or finite(value):
            yield name, value


def metric_text(metrics):
    values = []
    for name, value in metric_items(metrics):
        if value is None:
            formatted = 'undefined'
        elif name.split('.')[-1] in PERCENT_METRICS:
            formatted = f'{value * 100:.2f}%'
        else:
            formatted = f'{value:.4f}'
        values.append(name + ' ' + formatted)
    return '; '.join(values) if values else 'No verified native score'


def budget(row):
    gen = row.get('generation') or {}
    counts = gen.get('output_budget_counts') or {}
    if counts:
        return '; '.join(f'{int(cap):,} × {count:,}' for cap, count in sorted(counts.items(), key=lambda pair: int(pair[0]))) + ' (mixed)'
    cap = gen.get('max_tokens')
    if type(cap) is int:
        return f'{cap:,}' + (' (likelihood only)' if cap == 1 else '')
    return 'Not recorded'


def usable(row, task):
    counts = row.get('counts') or {}
    planned, parsed = counts.get('planned'), counts.get('parsed')
    if type(planned) is not int or planned <= 0 or type(parsed) is not int:
        return {'value': None, 'display': 'Not established', 'definition': 'No verified parse counts'}
    ratio = parsed / planned
    text = f'{parsed:,}/{planned:,} ({100 * ratio:.1f}%)'
    if task in {'P23', 'P24', 'P25', 'P26'}:
        return {'value': None, 'display': 'Not established; ' + text + ' string records', 'definition': 'Parsed counts include empty text; not usable complete annotations', 'string_record_fraction': ratio}
    if task in {'V01', 'V02', 'V03', 'V04', 'V05'}:
        return {'value': None, 'display': text + ' nonempty only', 'definition': 'Nonempty final text does not establish valid extracted answers', 'nonempty_fraction': ratio}
    if task == 'P43':
        return {'value': ratio, 'display': text + ' valid scores', 'definition': 'Valid one-token conditional-likelihood scores, not generated answers'}
    return {'value': ratio, 'display': text, 'definition': 'Native parser-valid outputs divided by all planned cases'}


def evidence(task, row, condition='native'):
    counts = row.get('counts') or {}; n = counts.get('planned'); parsed = counts.get('parsed')
    truncations = (row.get('finish_reasons') or {}).get('length')
    if condition != 'native':
        return {'category': 'Separate extraction diagnostic', 'detail': 'Offline extraction condition; retains the same full denominator and cannot replace the native score.'}
    if row.get('scorer_recovery'):
        undefined = any(value is None for _, value in metric_items(row.get('metrics') or {}))
        return {'category': 'Scorer repaired; metric incomplete' if undefined else 'Scorer compatibility repaired',
                'detail': 'The original crash is preserved as a separate attempt. Missing confidence vectors remain invalid; native formulas and all original generations are unchanged.'}
    if task in {'B01', 'B04', 'B05'}:
        detail = 'Measured label accuracy under this scope; no matched paper-ranking or rationale-validity claim.'
        held = counts.get('held_before_inference')
        if type(held) is int and held > 0:
            detail += f' {n:,} evaluated; {held:,} held before inference.'
        return {'category': 'Useful positive example', 'detail': detail}
    if task in {'P03', 'P16', 'P43'}:
        detail = 'Weak measured result under a zero-shot adaptation; specialist training and representations differ.'
        if task == 'P16':
            detail += ' Native class-ID extraction loses many outputs; a separate correction must retain its own label.'
        return {'category': 'Weak result, qualified scope', 'detail': detail}
    if task == 'B02':
        return {'category': 'Partly delivery-limited', 'detail': f'{truncations:,}/{n:,} outputs hit the cap; invalid outputs remain in accuracy.' if type(truncations) is int and type(n) is int else 'Output truncation affects the native score.'}
    if task in {'B07', 'B08', 'P07', 'P42'}:
        detail = 'Output delivery limits interpretation; invalid outputs remain in the original denominator.'
        if type(truncations) is int and type(n) is int:
            detail = f'{truncations:,}/{n:,} cap finishes. ' + detail
        if task == 'P07':detail += ' Full-test correlation is undefined.'
        if task == 'P42':detail += ' No accepted candidate; this does not isolate design quality.'
        return {'category': 'Delivery-limited', 'detail': detail}
    if task in {'V01', 'V02', 'V03'}:
        return {'category': 'Metric / extraction-limited', 'detail': 'CLOSED uses substring Yes/No matching; OPEN is token recall. Verbose or ambiguous text can receive credit; not strict answer accuracy.'}
    if task == 'V04':
        return {'category': 'Metric / extraction-limited', 'detail': 'Whole-final exact matching rejects verbose answers; zero score does not establish wrong clinical predictions.'}
    if task == 'V05':
        return {'category': 'Metric / extraction-limited', 'detail': 'Native score uses only the final character; full-text and strict-label diagnostics are separate conditions.'}
    if task == 'P01':
        return {'category': 'Metric / extraction-limited', 'detail': 'Strict whole-final Yes/No extraction rejects many outputs; historical raw recovery is needed for a separate diagnostic.'}
    if task in {'P23', 'P24', 'P25', 'P26'}:
        detail = 'Lexical ROUGE, not factual correctness; string-record counts do not prove usable annotations.'
        if type(truncations) is int and type(n) is int:detail += f' {truncations:,}/{n:,} cap finishes.'
        return {'category': 'Metric / delivery-limited', 'detail': detail}
    if any(value is None for _, value in metric_items(row.get('metrics') or {})):
        return {'category': 'Incomplete native metric', 'detail': 'A finished execution with an undefined metric is not a complete quality evaluation.'}
    if type(parsed) is int and type(n) is int and parsed < n:
        return {'category': 'Measured with output loss', 'detail': 'Invalid outputs remain in the native denominator; training and protocol scope differ from paper models.'}
    return {'category': 'Measured, contextual scope', 'detail': 'Use only under the declared input, output and training conditions; no controlled model-ranking claim.'}


def conditions(row):
    """Split already reported conditions; do not derive or recompute a score."""
    metrics = row.get('metrics') or {}
    if row['task_id'] == 'V05':
        groups = [('native', 'Native final-character extraction', ['native_td_final_character_accuracy']),
                  ('full_text', 'Offline full-text similarity extraction', ['adapted_full_text_closest_choice_accuracy', 'adapted_full_text_released_label_accuracy']),
                  ('strict_label', 'Offline strict final-label extraction', ['strict_final_label_accuracy'])]
        return [(kind, name, {key: metrics[key] for key in keys if key in metrics}) for kind, name, keys in groups if any(key in metrics for key in keys)]
    if row['task_id'] == 'P42' and all(isinstance(metrics.get(key), dict) for key in ['replace_only', 'full_atomic']):
        return [('native', 'Replace-only candidate condition', metrics['replace_only']),
                ('native', 'Insert/delete/replace candidate condition', metrics['full_atomic'])]
    return [('native', 'Native declared score', metrics)]


def catalog_map(catalog, excluded):
    mapping = {}
    for group in catalog.get('groups', []):
        for task in group.get('taskIds', []):
            if task in excluded:continue
            protocol = next((p for p in group.get('protocols', []) if p.get('taskId') == task), {})
            if task in mapping:
                raise ValueError('Duplicate retained task mapping: ' + task)
            mapping[task] = {'group': group, 'protocol': protocol}
    return mapping


def reaction_condition(rows, diagnostic):
    """Accept only a complete, identity-matched, separately frozen diagnostic."""
    if not diagnostic:return None
    required = {'post_run_diagnostic': True, 'native_score_replaced': False,
        'native_artifacts_modified': False, 'inference_or_regeneration': False,
        'reference_labels_used_to_select_rule': False, 'clean_directory_reproduction_verified': True}
    if any(diagnostic.get(key) is not value for key, value in required.items()):
        raise ValueError('Reaction diagnostic is incomplete or changes its native condition')
    if not (diagnostic.get('synthetic_tests') or {}).get('passed'):
        raise ValueError('Reaction diagnostic lacks frozen-rule validation')
    source = next((row for row in rows if row['task_id'] == 'P16' and row['condition_kind'] == 'native'
        and row['run_id'] == diagnostic.get('source_native_run_id')), None)
    if (source is None or source['source_score_sha256'] != diagnostic.get('source_scores_sha256')
            or source['protocol_variant'] != diagnostic.get('source_native_protocol_variant')):
        raise ValueError('Reaction diagnostic does not match the retained native score identity')
    counts = diagnostic['counts']; n = diagnostic['full_original_denominator']
    if (type(n) is not int or n <= 0 or n != source['counts'].get('planned') or n != counts.get('planned')
            or counts.get('original_accepted') != source['counts'].get('parsed')
            or diagnostic['native_accuracy_unchanged'] != source['native_score'].get('accuracy')
            or diagnostic['native_accuracy_unchanged'] != counts['original_correct'] / n
            or diagnostic['diagnostic_accuracy'] != counts['diagnostic_correct'] / n
            or counts['diagnostic_accepted'] - counts['original_accepted'] != counts['recovered']
            or counts['diagnostic_correct'] - counts['original_correct'] != counts['recovered_correct']
            or not 0 <= counts['diagnostic_correct'] <= counts['diagnostic_accepted'] <= n):
        raise ValueError('Reaction diagnostic counts or unchanged native score do not reconcile')
    result = copy.deepcopy(source)
    result.update(condition='Offline terminal-class extraction; same mixed 4K/16K cohort',
        condition_kind='post_run_terminal_class', protocol_variant=diagnostic['diagnostic_variant'],
        native_score=None, diagnostic_score={'accuracy': diagnostic['diagnostic_accuracy']},
        score_display=metric_text({'accuracy': diagnostic['diagnostic_accuracy']}),
        source_native_scores=source['source_scores'], source_scores=REACTION_DIAGNOSTIC,
        source_native_score_sha256=source['source_score_sha256'],
        source_score_sha256=None, diagnostic_result_sha256=diagnostic.get('diagnostic_result_sha256'),
        counts={'planned': n, 'parsed': counts['diagnostic_accepted'], 'correct': counts['diagnostic_correct']},
        source_original_counts=copy.deepcopy(source['counts']),
        usable_answer_rate={'value': counts['diagnostic_accepted'] / n,
            'display': f"{counts['diagnostic_accepted']:,}/{n:,} ({100 * counts['diagnostic_accepted'] / n:.1f}%)",
            'definition': 'Separate frozen-format diagnostic accepted outputs divided by the full original denominator'},
        evidence={'category': 'Weak result, corrected extraction',
            'detail': f"{counts['recovered']:,} additional finals recovered; {counts['recovered_correct']:,} additional correct answers. Same full cohort; separate diagnostic, not a native-score replacement."})
    return result


def recovered_subset_rows(document, mapping):
    """Describe recovered P36 evidence without treating it as a full task score.

    The portable input records an already audited archive. This renderer never
    reads raw generations or reinterprets a legacy dispatch-error status.
    """
    if document is None:return []
    if document.get('schema_version') != 1 or not isinstance(document.get('entries'), list):
        raise ValueError('Unsupported recovered-subset evidence schema')
    rows = []; seen = set()
    for entry in document['entries']:
        task = entry.get('task_id'); counts = entry.get('counts') or {}
        planned = counts.get('planned'); full_count = entry.get('full_source_cases')
        parsed = counts.get('parsed'); final_strings = counts.get('completed')
        empty = counts.get('empty_final_fields'); invalid = counts.get('invalid_outputs')
        finishes = entry.get('finish_reasons') or {}; metric = entry.get('archived_lexical_metric') or {}
        if task != 'P36' or task not in mapping:
            raise ValueError('Recovered subset is not a supported retained task')
        if (entry.get('status') != 'verified_archived_subset'
                or entry.get('full_benchmark_complete') is not False
                or entry.get('inference_performed') is not False
                or entry.get('raw_hashes_verified') is not True):
            raise ValueError('Recovered subset lacks verified, non-complete provenance')
        if (any(type(value) is not int for value in
                [planned, full_count, parsed, final_strings, empty, invalid])
                or not 0 < planned < full_count or parsed != 0
                or not 0 <= final_strings <= planned or empty + final_strings != planned
                or invalid != planned or counts.get('raw_responses') != planned
                or counts.get('missing_or_failed_outputs') != 0
                or any(type(value) is not int or value < 0 for value in finishes.values())
                or sum(finishes.values()) != planned):
            raise ValueError('Recovered subset counts omit failures or imply unverified completion')
        if (metric.get('name') != 'ROUGE-L' or not finite(metric.get('value'))
                or metric.get('text_strings') != final_strings or metric.get('denominator') != planned):
            raise ValueError('Archived lexical metric has a mismatched scope')
        for field in ['scores_sha256', 'completion_sha256', 'evidence_manifest_sha256', 'archive_sha256']:
            digest = entry.get(field, '')
            if not isinstance(digest, str) or len(digest) != 64 or any(c not in '0123456789abcdef' for c in digest):
                raise ValueError('Recovered subset lacks a valid ' + field)
        run_id = entry.get('run_id'); key = (task, run_id)
        if not run_id or key in seen:raise ValueError('Missing or duplicate recovered subset run')
        if not entry.get('source_evidence'):raise ValueError('Recovered subset lacks an evidence link')
        seen.add(key); info = mapping[task]; group = info['group']; protocol = info['protocol']
        rows.append({'task_id': task, 'task': protocol.get('title') or group['task'],
            'category': group['category'], 'dataset': protocol.get('title') or group['dataset'],
            'condition': f'Archived reviewed subset: {planned:,} of {full_count:,} source cases',
            'condition_kind': 'recovered_subset', 'run_id': run_id,
            'result_type': 'recovered_subset_attempt', 'protocol_variant': entry.get('protocol_variant'),
            'input_protocol': INPUTS[task], 'output_budget': budget(entry),
            'usable_answer_rate': {'value': 0.0, 'display': f'0/{planned:,} native-valid; {empty:,} empty finals',
                'definition': 'Native protein-serialization-valid outputs divided by the complete reviewed subset; all raw responses were delivered'},
            'native_score': None, 'diagnostic_score': None,
            'archived_lexical_metric': copy.deepcopy(metric),
            'score_display': f"No full-task score; archived ROUGE-L {metric['value']:.4f} ({planned:,} slots; {final_strings:,} final strings)",
            'evidence': {'category': 'Recovered subset; output / format failure',
                'detail': f'{planned:,}/{planned:,} raw responses verified; {finishes.get("length", 0):,} hit the cap. '
                    'No valid native protein sequence was delivered. Lexical overlap does not establish design quality; the full source benchmark remains unevaluated.'},
            'counts': copy.deepcopy(counts), 'finish_reasons': copy.deepcopy(finishes),
            'source_scores': None, 'source_score_sha256': entry['scores_sha256'],
            'source_evidence': entry['source_evidence'], 'source_row_category': 'recovered_subset_evidence',
            'evidence_manifest_sha256': entry['evidence_manifest_sha256'],
            'archive_sha256': entry['archive_sha256'], 'completion_sha256': entry['completion_sha256'],
            'source_protocol_url': protocol.get('sourceUrl') or group.get('sourceUrl'),
            'case_scope': 'reviewed_subset_only', 'full_source_cases': full_count,
            'full_benchmark_complete': False, 'native_metrics_recomputed': False})
    return rows


def build(scores, catalog, generated_at=None, source_hashes=None, reaction_diagnostic=None, recovered_subset_evidence=None):
    excluded = set((scores.get('main_report_scope') or {}).get('excluded_task_ids', ARCHIVE_IDS))
    mapping = catalog_map(catalog, excluded)
    expected = scores.get('main_catalog_settings')
    if type(expected) is int and len(mapping) != expected:
        raise ValueError('Retained task-ID coverage differs from declared catalog count')
    rows = []; observed = set(); seen = set()
    for category in ['completed_rows', 'diagnostic_only_finished_runs']:
        for raw in scores.get(category, []):
            task = raw['task_id']
            if task in excluded:continue
            if task not in mapping:raise ValueError('Scored task missing from retained catalog: ' + task)
            key = (task, raw['run_id'], raw.get('protocol_variant'), raw.get('dataset'), raw.get('native_split'))
            if key in seen:raise ValueError('Duplicate aggregate condition')
            seen.add(key); observed.add(task); info = mapping[task]; group = info['group']; protocol = info['protocol']
            run_note = 'replay' if 'replay' in raw['run_id'] else 'original run'
            if raw.get('generation_budget_condition') == 'MIXED_BUDGET_4K16K_CONTINUATION':run_note = 'mixed 4K/16K continuation'
            if raw.get('scorer_recovery'):run_note = 'offline compatibility repair; ' + run_note
            for condition, label, metrics in conditions(raw):
                source = raw.get('source_scores')
                answer_rate = usable(raw, task)
                evidence_status = evidence(task, raw, condition)
                if task == 'P42':
                    answer_rate['display'] = 'Per-condition unavailable; ' + answer_rate['display'] + ' across both conditions'
                    answer_rate['definition'] += '; aggregate counts cover both candidate regimes'
                    answer_rate['value'] = None
                    evidence_status['detail'] += ' Displayed delivery counts cover both candidate regimes.'
                rows.append({'task_id': task, 'task': protocol.get('title') or raw.get('task_name') or group['task'],
                    'category': group['category'], 'dataset': raw.get('dataset') or raw.get('native_split') or protocol.get('title') or group['dataset'],
                    'condition': label + '; ' + run_note, 'condition_kind': condition, 'run_id': raw['run_id'],
                    'result_type': 'offline_scorer_compatibility_repair' if raw.get('scorer_recovery') else ('original_or_replay' if condition == 'native' else 'offline_extraction_diagnostic'),
                    'protocol_variant': raw.get('protocol_variant'), 'input_protocol': INPUTS.get(task, group.get('inputInterface') or protocol.get('scientificQuestion') or 'Required input not specified in catalog'),
                    'output_budget': budget(raw), 'usable_answer_rate': answer_rate,
                    'native_score': copy.deepcopy(metrics) if condition == 'native' else None,
                    'diagnostic_score': copy.deepcopy(metrics) if condition != 'native' else None,
                    'score_display': metric_text({key: metrics.get(key) for key in ('auprc@micro','f1_max')}) if task in {'P12','P13','P14','P15'} else metric_text(metrics), 'evidence': evidence_status,
                    'counts': copy.deepcopy(raw.get('counts') or {}), 'finish_reasons': copy.deepcopy(raw.get('finish_reasons') or {}),
                    'source_scores': source, 'source_score_sha256': raw.get('scores_sha256'), 'source_row_category': category,
                    'source_protocol_url': protocol.get('sourceUrl') or group.get('sourceUrl'),
                    'case_scope': raw.get('case_scope'), 'native_metrics_recomputed': False})
    subset_rows = recovered_subset_rows(recovered_subset_evidence, mapping)
    rows.extend(subset_rows); observed.update(row['task_id'] for row in subset_rows)
    excluded_runs = scores.get('excluded_or_not_yet_terminal_runs', [])
    for task, info in mapping.items():
        if task in observed:continue
        group, protocol = info['group'], info['protocol']; blocker = protocol.get('blocker')
        source_state = protocol.get('status') or group.get('status')
        if blocker or source_state == 'Source-blocked':
            status, detail = 'Source / input blocked', blocker or 'Catalog records a source/input blocker; no verified result.'
        elif source_state == 'Deferred / held':
            status, detail = 'Held', 'Execution remains held; no verified retained result.'
        elif task in {'P12', 'P13', 'P14', 'P15'}:
            status, detail = 'Scoring unresolved', 'No verified whole-task native metric; scorer repair / completion remains pending.'
        elif task == 'P08':
            status, detail = 'Whole-task metric pending', 'No verified whole-task native score in the aggregate snapshot.'
        else:
            status, detail = 'No verified result', 'Current aggregate metadata provides no completed score; this does not prove the task was never attempted.'
        reasons = sorted({r.get('reason') for r in excluded_runs if r.get('task_id') == task and r.get('reason')})
        rows.append({'task_id': task, 'task': protocol.get('title') or group['task'], 'category': group['category'],
            'dataset': protocol.get('title') or group['dataset'], 'condition': 'Catalog contract; no verified scored condition', 'condition_kind': 'unverified',
            'run_id': None, 'protocol_variant': None, 'input_protocol': INPUTS.get(task, group.get('inputInterface') or protocol.get('scientificQuestion') or 'Required input not specified in catalog'),
            'output_budget': 'Not established', 'usable_answer_rate': {'value': None, 'display': 'Not established', 'definition': 'No verified full-run parse counts'},
            'native_score': None, 'diagnostic_score': None, 'score_display': 'No verified native score',
            'evidence': {'category': status, 'detail': detail}, 'counts': {}, 'finish_reasons': {}, 'source_scores': None,
            'source_score_sha256': None, 'source_row_category': None, 'source_protocol_url': protocol.get('sourceUrl') or group.get('sourceUrl'),
            'case_scope': protocol.get('nativeSplit'), 'excluded_run_reasons': reasons, 'native_metrics_recomputed': False})
    if {r['task_id'] for r in rows} != set(mapping):raise AssertionError('Decision table omitted a retained setting')
    if 'P16' in mapping:
        correction = reaction_condition(rows, reaction_diagnostic)
        if correction:
            correction['source_score_sha256'] = (source_hashes or {}).get(REACTION_DIAGNOSTIC)
            rows.append(correction)
    category_order = {}
    for group in catalog.get('groups', []):
        category_order.setdefault(group['category'], len(category_order))
    rows.sort(key=lambda r: (category_order[r['category']], r['task_id'], r['dataset'], r['run_id'] or '', r['condition']))
    return {'schema_version': 1, 'generated_at_pacific': generated_at or datetime.now(ZoneInfo('America/Los_Angeles')).isoformat(),
        'score_snapshot_at': scores.get('generated_at_utc'), 'catalog_snapshot_at': (catalog.get('meta') or {}).get('generatedAt'),
        'retained_setting_count': len(mapping), 'retained_setting_ids': sorted(mapping), 'excluded_setting_ids': sorted(excluded),
        'row_count': len(rows), 'rows': rows, 'source_sha256': source_hashes or {},
        'recovered_subset_setting_ids': sorted({row['task_id'] for row in subset_rows}),
        'policy': 'Aggregate and verified archived-subset metadata only. All retained settings included; runs, datasets and extraction conditions remain separate. Recovered subsets do not count as completed full benchmarks. No pooled averages, score recomputation, raw answers, labels or inference. Parse counts are qualified by their native meaning; missing verified scores remain unknown.',
        'model': (catalog.get('meta') or {}).get('model', {}).get('name')}


def cell(value):return str(value).replace('|', '\\|').replace('\n', '<br>')


def render(report, root=ROOT):
    text = ['# Evaluation decision table', '',
        f"Generated {pacific(report['generated_at_pacific'])}; score snapshot {pacific(report['score_snapshot_at'])}.", '',
        f"All **{report['retained_setting_count']} retained settings** appear below. Each source dataset, run or extraction condition stays separate; there is no overall average. Native scores remain unchanged. A saved or nonempty response is not necessarily a usable answer.", '',
        '“Positive” identifies a useful measured example, not a controlled win over paper models. Unknown entries do not mean never attempted. [Integrity audit](EVALUATION_INTEGRITY_AUDIT_2026-10-18.md) · [Original score summary](RESULTS_AT_A_GLANCE.md).', '',
        'Links for unavailable original score files open retained aggregate metadata. The structured table preserves their original paths and hashes; this does not restore missing originals.', '']
    current = None
    for row in report['rows']:
        if current != row['category']:
            if current is not None:text.append('')
            current = row['category'];text += ['## ' + current, '', '| Setting / dataset | Input / protocol / condition | Output tokens | Usable-answer rate | Native score / separate diagnostic | Evidence status |', '|---|---|---|---|---|---|']
        label = row['task_id'] + ' ' + row['task']
        if row.get('source_evidence'):
            label = '[' + label + '](' + row['source_evidence'] + ')'
        elif row.get('source_scores'):
            href = '../' + row['source_scores'] if (Path(root) / row['source_scores']).is_file() else 'RESULTS_AT_A_GLANCE.json'
            label = '[' + label + '](' + href + ')'
        elif row.get('source_protocol_url'):label = '[' + label + '](' + row['source_protocol_url'] + ')'
        if row['dataset'] != row['task']:label += '<br>' + row['dataset']
        state = '**' + row['evidence']['category'] + '**<br>' + row['evidence']['detail']
        if row['condition_kind'] not in {'native', 'unverified', 'recovered_subset'}:score = 'Diagnostic: ' + row['score_display']
        else:score = row['score_display']
        text.append('| ' + ' | '.join(cell(x) for x in [label, row['input_protocol'] + '<br>' + row['condition'], row['output_budget'], row['usable_answer_rate']['display'], score, state]) + ' |')
    text += ['', 'Archived BioReason settings remain in [their separate records](ARCHIVED_EVALUATIONS.md). Task inputs, explanations and reference labels are not reproduced here.', '']
    return '\n'.join(text)


def generate(root=ROOT):
    root = Path(root); docs = {}; hashes = {}
    for name in [SCORES, CATALOG]:
        raw = (root / name).read_bytes();docs[name] = json.loads(raw);hashes[name] = hashlib.sha256(raw).hexdigest()
    if (root / REACTION_DIAGNOSTIC).is_file():
        raw = (root / REACTION_DIAGNOSTIC).read_bytes();docs[REACTION_DIAGNOSTIC] = json.loads(raw);hashes[REACTION_DIAGNOSTIC] = hashlib.sha256(raw).hexdigest()
    if (root / RECOVERED_SUBSET_EVIDENCE).is_file():
        raw = (root / RECOVERED_SUBSET_EVIDENCE).read_bytes();docs[RECOVERED_SUBSET_EVIDENCE] = json.loads(raw);hashes[RECOVERED_SUBSET_EVIDENCE] = hashlib.sha256(raw).hexdigest()
    result = build(docs[SCORES], docs[CATALOG], source_hashes=hashes,
        reaction_diagnostic=docs.get(REACTION_DIAGNOSTIC), recovered_subset_evidence=docs.get(RECOVERED_SUBSET_EVIDENCE))
    for name, content in [(OUTPUT_JSON, json.dumps(result, ensure_ascii=False, indent=2, allow_nan=False) + '\n'), (OUTPUT_MD, render(result, root))]:
        path = root / name;path.parent.mkdir(parents=True, exist_ok=True);temporary = path.with_suffix(path.suffix + '.tmp');temporary.write_text(content);temporary.replace(path)
    return result


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__);parser.add_argument('--root', type=Path, default=ROOT);args = parser.parse_args()
    result = generate(args.root);print(json.dumps({'rows': result['row_count'], 'retained_settings': result['retained_setting_count'], 'outputs': [OUTPUT_MD, OUTPUT_JSON]}))
