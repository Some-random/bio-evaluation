"""Reference-isolated native T3 inputs and complete-permutation delivery checks."""
from __future__ import annotations

from collections import Counter
import hashlib
import json
import math
import re

AMINO_ACIDS = 'ACDEFGHIKLMNPQRSTVWY'
CONDITION = 'PFARENA_T3_REVIEWED_MAMMAL_DOMAIN_FULL_PERMUTATION_V1'
BASE_GENERATION = {
    'max_tokens': 16384, 'temperature': 1.0, 'top_p': 0.95, 'top_k': 20,
    'seed': 42, 'n': 1, 'chat_template_kwargs': {'enable_thinking': False},
    'structured_outputs': {'json': {'type': 'object', 'properties': {
        'ranking': {'type': 'array', 'minItems': 1, 'items': {'type': 'string'}}},
        'required': ['ranking'], 'additionalProperties': False}},
}
CONTEXT_KEYS = {'case_id', 'wildtype_sequence', 'sequence_length', 'candidate_ids',
                'anchor_mutant', 'anchor_DMS_score'}


def canonical_sha256(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, ensure_ascii=False,
        separators=(',', ':'), allow_nan=False).encode()).hexdigest()


def mutation_parts(value):
    if not isinstance(value, str) or not value or any(c.isspace() for c in value):
        raise ValueError('exact_nonempty_mutation_ID_required')
    parts = value.split('+')
    if any(re.fullmatch(r'([ACDEFGHIKLMNPQRSTVWY])([1-9][0-9]*)([ACDEFGHIKLMNPQRSTVWY])', p) is None for p in parts):
        raise ValueError('native_plus_joined_mutation_syntax_required')
    return parts


def validate_input_context(context):
    if set(context) != CONTEXT_KEYS:
        raise ValueError('unexpected_context_fields_or_target_score_payload')
    seq = context['wildtype_sequence']
    if (not isinstance(seq, str) or not seq or set(seq) - set(AMINO_ACIDS)
            or len(seq) != context['sequence_length']):
        raise ValueError('complete_native_sequence_required')
    candidates = context['candidate_ids']
    if (not isinstance(candidates, list) or not candidates or len(candidates) > 1000
            or len(set(candidates)) != len(candidates)):
        raise ValueError('complete_unique_native_candidate_list_required')
    anchor = mutation_parts(context['anchor_mutant'])
    try:
        finite = math.isfinite(float(context['anchor_DMS_score']))
    except (ValueError, TypeError):
        finite = False
    if not finite:
        raise ValueError('finite_legitimate_native_anchor_score_required')
    for value in [context['anchor_mutant'], *candidates]:
        positions = set()
        for part in mutation_parts(value):
            match = re.fullmatch(r'([A-Z])([0-9]+)([A-Z])', part)
            before, position, after = match.groups(); position = int(position)
            if (not 1 <= position <= len(seq) or seq[position-1] != before
                    or before == after or position in positions):
                raise ValueError('invalid_native_input_mutation_or_duplicate_position')
            positions.add(position)
    if any(not set(anchor) <= set(mutation_parts(value)) for value in candidates):
        raise ValueError('every_native_candidate_must_include_legitimate_anchor')
    return context


def audit_ranking(context, raw_final):
    validate_input_context(context)
    errors = []
    try:
        obj = json.loads(raw_final) if isinstance(raw_final, str) else None
    except (ValueError, TypeError):
        obj = None
    if not isinstance(obj, dict) or set(obj) != {'ranking'} or not isinstance(obj.get('ranking'), list):
        errors.append('strict_native_JSON_ranking_object_required'); ranking = []
    else:
        ranking = obj['ranking']
    if any(not isinstance(x, str) for x in ranking):
        errors.append('exact_string_IDs_required')
    counts = Counter(x for x in ranking if isinstance(x, str))
    expected = set(context['candidate_ids'])
    missing = sorted(expected - set(counts)); unknown = sorted(set(counts) - expected)
    duplicates = sum(max(0, n-1) for n in counts.values())
    if len(ranking) != len(expected): errors.append('full_fixed_candidate_count_required')
    if missing: errors.append('omitted_candidates')
    if unknown: errors.append('unknown_or_altered_candidates')
    if duplicates: errors.append('duplicate_candidates')
    return {'delivery_passed': not errors, 'candidate_count': len(expected),
        'returned_count': len(ranking), 'missing_count': len(missing),
        'unknown_count': len(unknown), 'duplicate_count': duplicates, 'errors': errors}
