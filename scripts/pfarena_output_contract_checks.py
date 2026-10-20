"""Separate delivery audit for PFArena T2–T4 closed-set rankings.

This module never extracts an answer, changes the native parser or computes a
benchmark score. Pass the JSON ``ranking`` value before the native parser's
string coercion. IDs must be copied exactly from the frozen candidate list.
T1 is open generation and is outside this full-permutation contract.
"""

from collections import Counter
from dataclasses import dataclass
from typing import Any, Sequence


def _malformed_identifier(value: Any) -> bool:
    """Check string-token shape only; do not interpret biological mutations."""
    return (
        not isinstance(value, str)
        or not value
        or any(char.isspace() or ord(char) < 32 or ord(char) == 127 for char in value)
    )


@dataclass(frozen=True)
class RankingAudit:
    complete_permutation: bool
    expected_count: int
    delivered_count: int | None
    errors: tuple[str, ...]
    missing_ids: tuple[str, ...]
    duplicate_ids: tuple[str, ...]
    unknown_ids: tuple[str, ...]
    malformed_item_indices: tuple[int, ...]


def audit_full_ranking(candidate_ids: Sequence[str], ranking: Any) -> RankingAudit:
    """Audit a parsed JSON list without coercion, repair or reference access.

    An invalid frozen input contract raises ``ValueError``. An invalid answer
    produces an audit result. This does not replace native metric semantics.
    """
    if isinstance(candidate_ids, (str, bytes)) or not candidate_ids:
        raise ValueError("Expected a nonempty frozen candidate-ID sequence")
    expected = tuple(candidate_ids)
    if any(_malformed_identifier(value) for value in expected):
        raise ValueError("Frozen candidate IDs must be nonempty string tokens")
    if len(set(expected)) != len(expected):
        raise ValueError("Frozen candidate IDs must be unique")

    if not isinstance(ranking, list):
        return RankingAudit(False, len(expected), None, ("ranking_not_json_list",), expected, (), (), ())

    malformed = tuple(index for index, value in enumerate(ranking) if _malformed_identifier(value))
    tokens = [value for value in ranking if not _malformed_identifier(value)]
    counts = Counter(tokens)
    expected_set = set(expected)
    missing = tuple(value for value in expected if counts[value] == 0)
    duplicates = tuple(value for value, count in counts.items() if count > 1)
    unknown = tuple(value for value in counts if value not in expected_set)
    errors = []
    if len(ranking) != len(expected):
        errors.append("length_mismatch")
    if malformed:
        errors.append("malformed_identifiers")
    if missing:
        errors.append("missing_candidates")
    if duplicates:
        errors.append("duplicate_candidates")
    if unknown:
        errors.append("unknown_candidates")
    return RankingAudit(not errors, len(expected), len(ranking), tuple(errors), missing, duplicates, unknown, malformed)


def audit_ranking_object(candidate_ids: Sequence[str], answer: Any) -> RankingAudit:
    """Audit an already-decoded JSON object; perform no text extraction."""
    if not isinstance(answer, dict) or "ranking" not in answer:
        result = audit_full_ranking(candidate_ids, None)
        error = "answer_not_json_object" if not isinstance(answer, dict) else "missing_ranking_field"
        return RankingAudit(
            False, result.expected_count, None, (error,), result.missing_ids, (), (), ()
        )
    return audit_full_ranking(candidate_ids, answer["ranking"])
