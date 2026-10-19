# P36: exact format versus outer-whitespace diagnostic

Verified October 19, 2026, Pacific time. This is offline extraction on the same 59 reviewed cases; no model calls, new sequences or native-score replacement.

**The original exact parser accepts 0/59 outputs. Removing only surrounding whitespace recovers 5/59 complete standard-amino-acid serializations (8.47%).** All five ended normally and contain 70–201 residues. The other 54 cases remain invalid under this diagnostic.

| Measure | Count |
|---|---:|
| Reviewed subset / full source benchmark | 59 / 5,876 |
| Hash-verified raw request/response pairs | 59 / 59 |
| Nonempty final strings | 17 |
| Empty finals | 42 |
| Normal stops / output-cap finishes | 33 / 26 |
| Exact native serialization | 0 / 59 |
| Separate outer-whitespace diagnostic | 5 / 59 |

The rule was frozen before application: apply `str.strip()` to visible final text, require a normal stop, then require the original `<bop>(<p>[A-Z])+<eop>` grammar and the standard 20-amino-acid alphabet. It does not remove internal spaces, correct tags, remove markdown, change residues, inspect reasoning or consult reference sequences.

| Recovered case | Residues | Finish |
|---|---:|---|
| `P36:234-2b227f4cab7944afb37c21739294e612` | 167 | stop |
| `P36:234-d5f95da13c6e414bbf59b36a7f143032` | 163 | stop |
| `P36:234-86a73e092a1a49c3bea3ac29dc6c4613` | 155 | stop |
| `P36:234-96071b9605a74aaab1050ac5f31030ee` | 70 | stop |
| `P36:234-4f685322a30b40f4b02f98bde6444063` | 201 | stop |

These are syntactically complete candidate strings. Recovery establishes no functional activity, similarity to the target or successful biological design. The 59-case reviewed subset is not the full 5,876-case benchmark.

## What the archived ROUGE measures

The archived score remains **ROUGE-L 0.12347117664198978 over all 59 slots**. The frozen scorer passes two references per case: **the full serialized target sequence and the full original Alpaca user prompt**. The source ROUGE implementation chooses the reference with greatest F-measure for each ROUGE type. Consequently, input-text overlap can earn credit; this metric cannot be interpreted as sequence-design quality. The diagnostic above does not recompute or replace it.

The references are identified by inspected frozen scorer/configuration code, not supplied to the whitespace extractor. Raw finals and all original artifacts remain unchanged.

[Structured diagnostic](P36_WHITESPACE_DIAGNOSTIC_2026-10-19.json) · [Frozen script, input/hash evidence and tests](benchmark_assets/p36_whitespace_diagnostic_2026-10-19.tar.gz) · [Original archived metadata](https://github.com/Some-random/bio-evaluation/releases/download/continuation-2026-10-16-reviewed-p36-and-source-preparation/p36-qwen3.8-27b-biot5-reviewed59-20261016-metadata-e68bc40942c2bc64c4045413.tar.gz)
