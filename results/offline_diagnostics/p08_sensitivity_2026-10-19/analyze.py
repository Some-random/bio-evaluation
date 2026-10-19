#!/usr/bin/env python3
"""Offline P08 native-parser reproduction and universal finite-imputation bounds.

No predictions are filled, repaired, or generated. Standard library only.
"""
import argparse
from bisect import bisect_left
from collections import Counter
from datetime import datetime
import hashlib
import json
import math
from pathlib import Path
from zoneinfo import ZoneInfo

from format_rules import classify, native_number

HERE = Path(__file__).resolve().parent


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def midranks(values):
    """One-based average ranks, including ties, independently implemented."""
    order = sorted(range(len(values)), key=values.__getitem__)
    result = [0.0] * len(values)
    i = 0
    while i < len(order):
        j = i + 1
        while j < len(order) and values[order[j]] == values[order[i]]:
            j += 1
        rank = (i + 1 + j) / 2
        for idx in order[i:j]:
            result[idx] = rank
        i = j
    return result


def spearman(x, y):
    if len(x) != len(y) or len(x) < 2:
        return None
    a, b = midranks(x), midranks(y)
    mean = (len(x) + 1) / 2
    a, b = [v - mean for v in a], [v - mean for v in b]
    denom = math.sqrt(sum(v*v for v in a) * sum(v*v for v in b))
    return None if denom == 0 else sum(u*v for u, v in zip(a, b)) / denom


def absolute_cross_sum(x, y):
    """Sum |x-y|, using prefix sums rather than an n-by-m distance matrix."""
    ordered = sorted(x)
    prefixes = [0.0]
    for value in ordered:
        prefixes.append(prefixes[-1] + value)
    total = 0.0
    for value in y:
        k = bisect_left(ordered, value)
        total += value*k - prefixes[k]
        total += prefixes[-1] - prefixes[k] - value*(len(ordered)-k)
    return total


def finite_imputation_bounds(predictions, targets):
    """Upper bounds for every finite completion preserving accepted predictions.

    Missing is None. Target ranks are fixed full-test midranks. If the numerator
    bound is nonpositive, dividing by the largest possible predictor rank norm
    yields a valid correlation upper bound. A positive numerator bound returns
    only the trivial bound 1; the denominator inequality must not be reversed.
    """
    if len(predictions) != len(targets) or len(targets) < 2:
        raise ValueError("Require matching full-test vectors")
    if any(not math.isfinite(v) for v in targets):
        raise ValueError("Targets must be finite")
    observed = [i for i, p in enumerate(predictions) if p is not None]
    absent = [i for i, p in enumerate(predictions) if p is None]
    if len(observed) < 2 or len({predictions[i] for i in observed}) < 2:
        raise ValueError("At least two distinct accepted predictions required")
    n, k, m = len(targets), len(observed), len(absent)
    target_ranks = midranks(targets)
    b = [value - (n+1)/2 for value in target_ranks]
    valid_ranks = midranks([predictions[i] for i in observed])
    centered_valid = [value - (k+1)/2 for value in valid_ranks]
    base = sum(value*b[idx] for value, idx in zip(centered_valid, observed))
    target_ss = sum(value*value for value in b)
    predictor_ss_upper = n*(n*n-1)/12
    denominator_upper = math.sqrt(target_ss * predictor_ss_upper)
    if denominator_upper == 0:
        raise ValueError("Constant target ranks")
    # Each accepted midrank moves between 0 and m positions after insertion.
    valid_shift_bound = m/2 * sum(abs(b[i]) for i in observed)
    missing_rank_bound = (n-1)/2 * sum(abs(b[i]) for i in absent)
    rectangle_numerator = base + valid_shift_bound + missing_rank_bound
    # Midrank covariance identity: 1/2 sum_{i<j} sign(p_i-p_j)(b_i-b_j).
    # All valid-valid pairs are fixed. Every pair touching an absent value
    # contributes at most |b_i-b_j|/2, including any future prediction ties.
    cross = absolute_cross_sum([b[i] for i in observed], [b[i] for i in absent]) / 2
    missing_sorted = sorted(b[i] for i in absent)
    within = sum((2*i-m+1)*v for i, v in enumerate(missing_sorted)) / 2
    pair_numerator = base + cross + within
    bound = lambda numerator: numerator/denominator_upper if numerator <= 0 else 1.0
    return {
        "n": n, "accepted": k, "invalid": m, "accepted_fixed_covariance": base,
        "target_rank_sum_squares": target_ss,
        "predictor_rank_sum_squares_upper": predictor_ss_upper,
        "denominator_upper": denominator_upper,
        "rectangle": {"valid_rank_shift_term": valid_shift_bound,
            "invalid_rank_term": missing_rank_bound,
            "numerator_upper": rectangle_numerator,
            "correlation_upper": bound(rectangle_numerator)},
        "pairwise": {"valid_invalid_absolute_term": cross,
            "invalid_invalid_absolute_term": within,
            "numerator_upper": pair_numerator,
            "correlation_upper": bound(pair_numerator)},
        "a_filled_or_repaired_score": False,
    }


def run(source, output):
    freeze = json.loads((HERE/'format_rules_freeze.json').read_text())
    if freeze['classifier_sha256'] != sha(HERE/'format_rules.py'):
        raise ValueError("Reference-blind format rules changed")
    raw = source.read_bytes()
    rows = json.loads(raw)
    if len({row['case_id'] for row in rows}) != len(rows):
        raise ValueError("Duplicate archived case IDs")
    # Classification calls receive raw final text and finish reason only.
    classifications = [classify(r.get('raw_text'), r.get('finish_reason')) for r in rows]
    predictions = [native_number(r.get('raw_text')) for r in rows]
    if any(p != r['prediction'] or (p is not None) != r['parsed'] for p, r in zip(predictions, rows)):
        raise ValueError("Independent parser disagrees with archived predictions")
    targets = [r['target'] for r in rows]
    pairs = [(p, y) for p, y in zip(predictions, targets) if p is not None]
    rho = spearman([p for p,y in pairs], [y for p,y in pairs])
    counts = Counter(item['category'] for item in classifications)
    # Reuse the same frozen classifier on individual prose lines, solely to
    # describe tentative numeric proposals. A scalar-looking line inside an
    # abstention does not turn the whole final into an unambiguous prediction.
    scalar_categories = {'native_scalar','unicode_minus_only_scalar','whole_final_scalar_wrapper'}
    scalar_lines = [sum(classify(line,'stop')['category'] in scalar_categories
                        for line in (r.get('raw_text') or '').splitlines() if line.strip())
                    for r in rows]
    evidence = [{"case_id": r['case_id'], "category": c['category'],
                 "finish_reason": r.get('finish_reason'),
                 "scalar_looking_line_count": count,
                 "raw_text_sha256": hashlib.sha256((r.get('raw_text') or '').encode()).hexdigest(),
                 "reference_used_for_classification": False,
                 "original_prediction_remains_invalid": True}
                for r,c,count in zip(rows, classifications,scalar_lines) if not r['parsed']]
    bounds = finite_imputation_bounds(predictions, targets)
    result = {
        "created_at_pacific": datetime.now(ZoneInfo('America/Los_Angeles')).isoformat(),
        "task_id": "P08", "experiment": "offline_sensitivity_existing_mixed_4k16k_outputs",
        "source_file": str(source), "source_sha256": hashlib.sha256(raw).hexdigest(),
        "classifier_sha256": freeze['classifier_sha256'],
        "planned": len(rows), "parsed": len(pairs), "invalid": len(rows)-len(pairs),
        "native_parser_reproduction_matches_every_row": True,
        "full_test_spearman": None, "parsed_only_spearman_recomputed": rho,
        "format_categories": dict(counts), "bounds": bounds,
        "prose_with_scalar_looking_lines": sum(count>0 and c['category'] in {
            'abstention_or_insufficient_information','qualified_estimate_or_uncertainty'}
            for c,count in zip(classifications,scalar_lines)),
        "scalar_line_is_not_a_commitment_or_scoring_repair": True,
        "format_only_candidates": counts['unicode_minus_only_scalar']+counts['whole_final_scalar_wrapper'],
        "original_predictions_changed": False, "new_inference_calls": 0,
        "targets_used_for_format_classification": False,
        "target_use": "Reproducing archived correlation and worst-case sensitivity bounds only",
        "sign_flip_or_rescaling_applied": False,
    }
    output.mkdir(parents=True, exist_ok=True)
    (output/'invalid_format_inventory.json').write_text(json.dumps(evidence,indent=2)+'\n')
    result['invalid_inventory_sha256'] = sha(output/'invalid_format_inventory.json')
    if source.read_bytes() != raw:
        raise ValueError("Original archived records changed during the audit")
    (output/'analysis.json').write_text(json.dumps(result,indent=2)+'\n')
    return result


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source',type=Path,required=True)
    parser.add_argument('--output',type=Path,default=HERE)
    args = parser.parse_args()
    print(json.dumps(run(args.source,args.output),indent=2))
