#!/usr/bin/env python3
"""Prospective GFP endpoint contract; no generation, oracle load or forward pass.

This is a qualified Qwen baseline, not an exact STRIDE paper replication.
Trajectory correctness is not inferred from endpoint validity or oracle success.
"""
from __future__ import annotations
import json
import math
from collections import Counter
from typing import Any

AA_ALPHABET = frozenset('ACDEFGHIKLMNPQRSTVWY')
REGIMES = ('replace_only', 'full_atomic')


def levenshtein(left: str, right: str) -> int:
    previous = list(range(len(right) + 1))
    for i, a in enumerate(left, 1):
        current = [i]
        for j, b in enumerate(right, 1):
            current.append(min(current[-1] + 1, previous[j] + 1,
                               previous[j - 1] + (a != b)))
        previous = current
    return previous[-1]


def parse_channels(final_text: str | None, reasoning_text: str | None) -> dict[str, Any]:
    """Preserve the source parser's delimiter/JSON rule across explicit channels.

    A supplied reasoning field is wrapped with literal think delimiters for the
    source-format parser. This is a declared interface reconstruction, never a
    claim that those exact delimiters occurred in the archived final channel.
    Without a reasoning field, the original final must contain its own delimiter.
    No JSON is recovered from reasoning or repaired from malformed final output.
    """
    result = {'valid_format': False, 'protein': None,
              'channel_reconstruction': reasoning_text is not None}
    if not isinstance(final_text, str):
        return result
    if reasoning_text is not None and not isinstance(reasoning_text, str):
        return result
    text = (f'<think>{reasoning_text}</think>{final_text}'
            if reasoning_text is not None else final_text).strip()
    if '</think>' not in text:
        return result
    _, remainder = text.split('</think>', 1)
    try:
        obj = json.loads(remainder.strip())
    except (ValueError, TypeError):
        return result
    if isinstance(obj, dict) and isinstance(obj.get('protein'), str):
        result.update(valid_format=True, protein=obj['protein'])
    return result


def validate_endpoint(source: str, candidate: str | None, regime: str) -> dict[str, Any]:
    if regime not in REGIMES:
        raise ValueError('Unknown GFP regime')
    if not source or any(a not in AA_ALPHABET for a in source):
        raise ValueError('Source must be a complete uppercase AA20 sequence')
    result = {'eligible': False, 'distance': None, 'has_length_change': False,
              'reason': None, 'trajectory_correctness': 'unassessed'}
    if not isinstance(candidate, str) or not candidate:
        result['reason'] = 'missing_or_empty_sequence'
        return result
    if any(a not in AA_ALPHABET for a in candidate):
        result['reason'] = 'outside_uppercase_AA20'
        return result
    result['has_length_change'] = len(candidate) != len(source)
    # Native candidate horizon is declared prospectively as an endpoint bound.
    # Early length rejection protects the dynamic program from arbitrary output.
    if abs(len(source) - len(candidate)) > 3:
        result['reason'] = 'endpoint_distance_above_three'
        return result
    if regime == 'replace_only':
        if len(candidate) != len(source):
            result['reason'] = 'length_change_in_replace_only'
            return result
        distance = sum(a != b for a, b in zip(source, candidate))
    else:
        distance = levenshtein(source, candidate)
    result['distance'] = distance
    if not 1 <= distance <= 3:
        result['reason'] = 'endpoint_distance_not_one_to_three'
        return result
    result.update(eligible=True, reason=None)
    return result


def summarize(source: str, regime: str, samples: list[dict[str, Any]],
              baseline_oracle_score: float, expected_samples: int = 100) -> dict[str, Any]:
    """Evaluate fixed slots against already supplied oracle values, offline only.

    Generation failures remain in N. Missing/nonfinite scores on eligible
    candidates withhold the primary metric; they are not invented failures.
    """
    if not isinstance(expected_samples, int) or expected_samples <= 0:
        raise ValueError('Expected sample count must be positive')
    if len(samples) != expected_samples:
        raise ValueError('Every fixed candidate slot must be present')
    ids = [r.get('sample_index') for r in samples]
    if any(type(i) is not int for i in ids) or sorted(ids) != list(range(expected_samples)):
        raise ValueError('Candidate slot identity must be unique and complete')
    if isinstance(baseline_oracle_score, bool) or not isinstance(baseline_oracle_score, (int, float)) or not math.isfinite(baseline_oracle_score):
        raise ValueError('A finite measured oracle baseline is required')
    improved = []
    details = []
    invalid_reasons = Counter()
    oracle_missing = 0
    length_finished = 0
    eligible_count = 0
    for sample in sorted(samples, key=lambda r: r['sample_index']):
        if sample.get('finish_reason') == 'length':
            length_finished += 1
        parsed = parse_channels(sample.get('final_text'), sample.get('reasoning_text'))
        validation = validate_endpoint(source, parsed['protein'], regime)
        if sample.get('generation_error'):
            validation.update(eligible=False, reason='generation_error')
        elif not parsed['valid_format']:
            validation.update(eligible=False, reason='invalid_source_format_after_declared_channel_reconstruction')
        row = {'sample_index': sample['sample_index'], **parsed, **validation,
               'oracle_score': sample.get('oracle_score'), 'oracle_improved': None}
        if not validation['eligible']:
            invalid_reasons[validation['reason']] += 1
        else:
            eligible_count += 1
            score = sample.get('oracle_score')
            if isinstance(score, bool) or not isinstance(score, (int, float)) or not math.isfinite(score):
                oracle_missing += 1
            else:
                row['oracle_improved'] = score > baseline_oracle_score
                if row['oracle_improved']:
                    improved.append(parsed['protein'])
        details.append(row)
    complete_oracle = oracle_missing == 0
    unique_count = len(set(improved))
    return {
        'protocol_kind': 'qualified_adaptation', 'native_paper_replication': False,
        'regime': regime, 'planned_samples': expected_samples,
        'eligible_endpoints': eligible_count, 'invalid_generation_or_endpoint_count': sum(invalid_reasons.values()),
        'invalid_reasons': dict(invalid_reasons), 'length_finished_samples': length_finished,
        'eligible_samples_without_finite_oracle_score': oracle_missing,
        'scoring_complete': complete_oracle,
        'qualified_oracle_success': len(improved) / expected_samples if complete_oracle else None,
        'improved_samples': len(improved) if complete_oracle else None,
        'unique_improved_sequences': unique_count if complete_oracle else None,
        'improved_sequence_uniqueness': (unique_count / len(improved)) if complete_oracle and improved else None,
        'native_novelty': None,
        'native_novelty_withheld_reason': 'Exact positive SFT training membership D+ was not recovered; no replacement corpus is used.',
        'trajectory_correctness': 'unassessed', 'mechanistic_rationale_correctness': 'unassessed',
        'biological_measurement_status': 'Fixed trained-oracle proxy only; no new fluorescence experiment.',
        'sample_details': details,
    }
