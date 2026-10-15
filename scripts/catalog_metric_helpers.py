"""Fixed parsers and metric accounting for the new local catalog baselines.

Pure offline functions. Missing/invalid values are never filled from labels.
"""
import math
import re


def parse_binary_answer(text):
    if not isinstance(text, str):
        return None
    match = re.fullmatch(r"\s*(?:Answer\s*:\s*)?(Yes|No)\.?\s*", text, re.IGNORECASE)
    return int(match.group(1).lower() == "yes") if match else None


def parse_numeric_answer(text):
    if not isinstance(text, str):
        return None
    match = re.fullmatch(r"\s*(?:Answer\s*:\s*)?([+-]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][+-]?\d+)?)\s*", text, re.IGNORECASE)
    if not match:
        return None
    value = float(match.group(1))
    return value if math.isfinite(value) else None


def classification_accuracy(targets, texts):
    if len(targets) != len(texts) or not targets or any(x not in {0, 1} for x in targets):
        raise ValueError("Require one valid binary reference and one response slot per planned case")
    parsed = [parse_binary_answer(text) for text in texts]
    correct = sum(prediction is not None and prediction == target for prediction, target in zip(parsed, targets))
    return {"accuracy": correct / len(targets), "correct": correct, "planned": len(targets),
            "parsed": sum(x is not None for x in parsed), "missing": sum(x is None for x in texts),
            "invalid": sum(t is not None and p is None for t, p in zip(texts, parsed)),
            "all_case_rule": "Missing or invalid model answers count as incorrect; report transport failures separately."}


def regression_spearman(targets, texts):
    from scipy.stats import spearmanr
    if len(targets) != len(texts) or not targets or any(not math.isfinite(x) for x in targets):
        raise ValueError("Require one finite reference and one response slot per planned case")
    parsed = [parse_numeric_answer(text) for text in texts]
    pairs = [(t, p) for t, p in zip(targets, parsed) if p is not None]
    constant = len(pairs) < 2 or len({p for _, p in pairs}) < 2 or len({t for t, _ in pairs}) < 2
    value = None if constant else float(spearmanr([x[0] for x in pairs], [x[1] for x in pairs]).correlation)
    return {"spearman": value if len(pairs) == len(targets) else None,
            "spearman_parsed_only": value if len(pairs) != len(targets) else None,
            "planned": len(targets), "parsed": len(pairs), "missing": sum(x is None for x in texts),
            "invalid": sum(t is not None and p is None for t, p in zip(texts, parsed)),
            "undefined_constant_or_insufficient": constant,
            "all_case_rule": "No invented numeric replacement. Full-test Spearman requires all outputs to parse; otherwise parsed-only correlation is explicitly incomplete."}
