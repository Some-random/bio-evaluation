"""Reference-blind P08 final-text categories, frozen before archived rows are read.

This classifier is descriptive. It never changes a saved prediction or a score.
"""
import math
import re

NUMBER = r"[+-]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][+-]?\d+)?"
NATIVE = re.compile(r"\s*(?:Answer\s*:\s*)?(" + NUMBER + r")\s*", re.I)
PREFIX = re.compile(r"^(?:final\s+answer|answer|prediction|predicted\s+(?:stability|score)|stability(?:\s+score)?)\s*:\s*", re.I)
ABSTENTION = re.compile(r"\b(?:cannot|can't|unable|impossible|insufficient|not enough|do not have|don't have|not possible|not available|cannot be determined|cannot accurately|cannot reliably)\b", re.I)
QUALIFICATION = re.compile(r"\b(?:estimate|estimated|approximately|approx|roughly|around|about|likely|perhaps|guess|tentative|uncertain|plausible|assum(?:e|ing)|would|could|might|may)\b|[~≈±]", re.I)


def native_number(text):
    if not isinstance(text, str):
        return None
    match = NATIVE.fullmatch(text)
    if not match:
        return None
    value = float(match.group(1))
    return value if math.isfinite(value) else None


def classify(text, finish_reason):
    """No target/reference argument exists, intentionally."""
    if native_number(text) is not None:
        return {"category": "native_scalar", "format_value": native_number(text)}
    if finish_reason == "length":
        return {"category": "truncated_invalid", "format_value": None}
    if not isinstance(text, str) or not text.strip():
        return {"category": "empty_final", "format_value": None}
    stripped = text.strip()
    normalized = stripped.replace("−", "-")
    if normalized != stripped and native_number(normalized) is not None:
        return {"category": "unicode_minus_only_scalar", "format_value": native_number(normalized)}
    # Only whole-final deterministic wrappers; never inspect a rationale for a number.
    unwrapped = PREFIX.sub("", normalized)
    for left, right in [("**", "**"), ("`", "`"), ("\\boxed{", "}"), ("(", ")")]:
        if unwrapped.startswith(left) and unwrapped.endswith(right):
            unwrapped = unwrapped[len(left):-len(right)].strip()
            break
    if native_number(unwrapped) is not None and unwrapped != normalized:
        return {"category": "whole_final_scalar_wrapper", "format_value": native_number(unwrapped)}
    # An explicit refusal/insufficiency statement remains an abstention even if
    # it mentions hypothetical numbers. Qualified guesses remain separate.
    if ABSTENTION.search(stripped):
        return {"category": "abstention_or_insufficient_information", "format_value": None}
    if QUALIFICATION.search(stripped):
        return {"category": "qualified_estimate_or_uncertainty", "format_value": None}
    return {"category": "other_malformed_or_prose", "format_value": None}
