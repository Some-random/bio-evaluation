# Scoring compatibility repair

Updated 2026-10-19T04:33:35.795477-07:00 (America/Los_Angeles).

The original scorer stopped when an API response contained `content: null` but the saved text field contained `""`. Those fields both represent an absent final answer. The repaired provenance check accepts that exact equivalence; the answer still counts as invalid. No model response was regenerated, filled in, or removed.

| Dataset task | Saved cases | Valid final vectors | Invalid vectors | Full AP / Fmax |
| --- | ---: | ---: | ---: | --- |
| Enzyme annotation (P12; DeepFRI-derived released test) | 1,919 / 1,919 | 1,634 | 285 | Undefined |
| Biological-process annotation (P13; DeepFRI-derived released test) | 3,416 / 3,416 | 2,982 | 434 | Undefined |
| Molecular-function annotation (P14; DeepFRI-derived released test) | 3,416 / 3,416 | 3,120 | 296 | Undefined |
| Cellular-component annotation (P15; DeepFRI-derived released test) | 3,416 / 3,416 | 3,340 | 76 | Undefined |

Full-set AP/Fmax remain undefined because the frozen protocol requires a valid confidence vector for every case. The JSON record retains separately labeled parsed-only diagnostics, which are not full-test benchmark scores.

The original failed attempts, complete case sets, original 4K/16K output budgets, native metric formulas, and saved reasoning/final responses remain unchanged. New score IDs end in `scoring_null_equivalence_v1`. This remains a zero-shot sequence/confidence adaptation, not a matched specialist-model paper replication.

Exact native score files are preserved in the provenance archive. Where the native all-zero reference produces a nonfinite Fmax, public JSON uses `null` and records the original representation and metric path. All finite metric values are unchanged.

Pending original task/recovery: none.

[Structured results and correction records](SCORER_COMPATIBILITY_REPAIR_2026-10-19.json) · [Portable code and provenance](benchmark_assets/scorer_compatibility_repair_2026-10-19.tar.gz)
