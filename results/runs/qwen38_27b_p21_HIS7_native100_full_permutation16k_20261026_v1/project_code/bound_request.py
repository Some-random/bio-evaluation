"""Bind the full native prompt and exact candidate list to a frozen request."""
from __future__ import annotations
import copy
import hashlib
import json
from input_contract import BASE_GENERATION, CONDITION, canonical_sha256, validate_input_context

MODEL = 'Qwen/Qwen3.8-27B'


def build_bound_request(case, context, base_generation, *, case_sha256,
                        context_sha256, base_generation_sha256):
    for value, expected in [(case, case_sha256), (context, context_sha256),
                            (base_generation, base_generation_sha256)]:
        if canonical_sha256(value) != expected:
            raise ValueError('changed_frozen_input_context_or_generation')
    if base_generation != BASE_GENERATION:
        raise ValueError('changed_base_sampling_condition')
    validate_input_context(context)
    if set(case) != {'task_id', 'case_id', 'messages'} or case['task_id'] != 'P21':
        raise ValueError('unexpected_case_fields_or_task')
    if case['case_id'] != context['case_id']:
        raise ValueError('case_context_identity_mismatch')
    messages = case['messages']
    if (not isinstance(messages, list) or len(messages) != 1
            or set(messages[0]) != {'role', 'content'} or messages[0]['role'] != 'user'):
        raise ValueError('exact_fresh_native_user_message_required')
    text = messages[0]['content']
    expected_tail = ('4. CANDIDATE MUTATIONS TO RANK (Total Candidates: '
        + str(len(context['candidate_ids'])) + ')\n' + '\n'.join(context['candidate_ids']))
    if (not isinstance(text, str) or ('`'+context['wildtype_sequence']+'`') not in text
            or '- **Anchor Mutant**: '+context['anchor_mutant'] not in text
            or '- **Anchor DMS Score**: '+context['anchor_DMS_score'] not in text
            or not text.rstrip().endswith(expected_tail)):
        raise ValueError('complete_native_sequence_anchor_or_candidate_list_mismatch')
    result = {'model': MODEL, 'messages': copy.deepcopy(messages), **copy.deepcopy(base_generation)}
    candidates = context['candidate_ids']
    result['structured_outputs'] = {'json': {'type': 'object', 'properties': {
        'ranking': {'type': 'array', 'minItems': len(candidates), 'maxItems': len(candidates),
                    'items': {'type': 'string', 'enum': candidates}}},
        'required': ['ranking'], 'additionalProperties': False}}
    candidate_json = json.dumps(candidates, ensure_ascii=False, separators=(',', ':'))
    result['vllm_xargs'] = {'p21_permutation_condition': CONDITION,
        'p21_candidate_ids_json': candidate_json,
        'p21_candidate_ids_sha256': hashlib.sha256(candidate_json.encode()).hexdigest()}
    return result
