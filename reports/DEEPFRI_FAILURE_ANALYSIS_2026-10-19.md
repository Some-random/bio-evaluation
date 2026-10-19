# Protein-function confidence outputs: failure analysis and matched references

This is an **offline analysis of the existing P12–P15 outputs**. The published null-versus-empty compatibility repairs are complete. No new inference, altered prediction, normalization, selective retry, or replacement score is introduced here. The full-test primary scores remain undefined under the local completeness policy.

The remaining problems differ substantially across tasks. P12 is dominated by output truncation. P13–P15 need an audit of the permitted label vocabulary and duplicate keys before more protein-function inference; simply allowing longer answers would leave most of their observed errors unresolved.

## Exact failure partition

Each case appears in one column of the following partition. A token-limit finish takes priority even when its partial final text also has malformed JSON; duplicate failures precede unknown identifiers. Crosscut counts below preserve those overlaps.

| Task | Valid / planned | Token limit | Empty final, normal stop | Malformed JSON, normal stop | Unknown identifier | Identical-only duplicate keys | Conflicting duplicate keys |
|---|---:|---:|---:|---:|---:|---:|---:|
| P12 — Enzyme Commission | 1,634 / 1,919 | 239 | 5 | 0 | 39 | 2 | 0 |
| P13 — Biological process | 2,982 / 3,416 | 88 | 20 | 3 | 271 | 49 | 3 |
| P14 — Molecular function | 3,120 / 3,416 | 89 | 7 | 0 | 197 | 3 | 0 |
| P15 — Cellular component | 3,340 / 3,416 | 22 | 2 | 0 | 44 | 6 | 2 |

The native parser's combined “unknown class or nonnumeric confidence” category is **entirely unknown identifiers in these records**: 39, 271, 197 and 44 cases respectively. No case in that combined category is caused by a numeric string, another wrong confidence-value type, nonnumeric string, nonfinite numeric value, or an out-of-range number. Those conditions are tested explicitly, rather than inferred from the combined error message.

“Unknown” means absent from the task's exact frozen vocabulary. It can include an incomplete EC identifier, a misspelled GO identifier, or a valid ontology term not in that task's released vocabulary. This analysis does not replace any identifier with a guessed intended label.

| Overlapping observation | P12 | P13 | P14 | P15 |
|---|---:|---:|---:|---:|
| Empty final, any finish | 234 | 94 | 91 | 18 |
| Malformed JSON, including truncated finals | 9 | 17 | 5 | 6 |
| Unknown identifier, including duplicate-key cases | 39 | 280 | 197 | 45 |
| Any identical duplicate | 2 | 50 | 3 | 6 |
| Any conflicting duplicate | 0 | 3 | 0 | 2 |
| Identical duplicate is the only detected violation | 2 | 41 | 3 | 5 |

One P13 response has both an identical and a conflicting duplicate. Eight other P13 identical-only duplicate cases also have unknown identifiers; the mixed duplicate case has unknown identifiers too. One P15 identical-only duplicate case also has an unknown identifier. Thus even a future conservative identical-duplicate normalization could not simply count every duplicate response as recovered. No such normalization or rescoring is applied here.

## Matched-subset comparison

The model and reference below use **exactly the same original parsed case IDs, in the same order, with the same complete class vocabulary and scorer-only targets**. The reference assigns zero to every class. It does not fill in invalid model outputs and is not a trained baseline.

| Task | Matched cases | Source AP: model / all-zero | Tie-grouped AP: model / all-zero | Source Fmax: model / all-zero |
|---|---:|---:|---:|---:|
| P12 | 1,634 | 0.005649 / 0.004438 | 0.005122 / 0.004376 | 0.027645 / undefined |
| P13 | 2,982 | 0.038287 / 0.034547 | 0.035367 / 0.033627 | 0.181724 / undefined |
| P14 | 3,120 | 0.024694 / 0.018158 | 0.022279 / 0.018077 | 0.110729 / undefined |
| P15 | 3,340 | 0.076526 / 0.037064 | 0.067172 / 0.036555 | 0.236779 / 0.071082 |

The source AP formula sorts individual tied scores and depends on the fixed Torch sorting behavior. The separately named tie-grouped AP groups identical score values; its all-zero reference equals the positive-label prevalence on that subset. Both are retained, without selecting the more favorable result. The all-zero source Fmax is undefined for P12–P14 because the native tied-score computation encounters a zero denominator; these values remain `null`, not zero. On the matched P15 subset the same native formula returns 0.071082. These source-tie effects are a reason to retain the separately named tie-grouped AP alongside the source result.

The previously published `OFFLINE_ALL_ZERO_REFERENCE` used the **full** case set, while model `PARSED_ONLY_DIAGNOSTIC` used the parsed subset. Those two numbers alone were not a matched comparison. The new table fixes that scope mismatch without changing either historical number. A selected parsed subset still does not establish full-test performance or an improvement over trained specialist systems.

## Method and provenance

The classifier and ten synthetic tests were frozen before this analysis read reference labels. Its diagnoses use final-answer content only; no reasoning-channel content supplies predictions. It verified the original manifest and configuration bytes, exact ordered case contract and reviewed IDs, vocabulary, per-case output budgets, request payloads, model/revision identities, and every original request/response hash. It reproduced every corrected parser-valid count and native error count. Every valid saved confidence vector was also checked against the exact final JSON object.

The metric stage opened only the hash-locked original scorer references, verified the exact full case-ID set and class-index mapping, then selected the already frozen parsed IDs. It reran the pinned source AP/Fmax functions and independently calculated the tie-grouped AP; all original parsed-only values were reproduced before calculating the matched all-zero reference.

The requirement that **all planned model vectors parse before publishing a full-test primary score is this evaluation's completeness policy**, not a restriction inherent to the numerical AP/Fmax formulas. Clearly labeled subset comparisons remain possible. A formula accepting an array does not justify silently treating absent model answers as zero predictions.

Portable evidence includes all per-case output diagnoses, request/response hash inventories, exact matched subset IDs, unchanged sparse predictions, scorer-only labels and the pinned metric source. The material contains evaluation answers and must not be exposed to a benchmark solver.

- [Structured report](DEEPFRI_FAILURE_ANALYSIS_2026-10-19.json)
- [Portable evidence](../results/offline_diagnostics/deepfri_failure_analysis_2026-10-19/)
- [Output-only classifier and local-source replay](../scripts/analyze_deepfri_failures.py)
- [Portable metric verifier](../scripts/verify_deepfri_matched_subset.py)
- [Synthetic classifier tests](../tests/test_analyze_deepfri_failures.py)
- [Completed compatibility repairs](SCORER_COMPATIBILITY_REPAIR_2026-10-19.md)

```bash
python -m unittest discover -s tests -p test_analyze_deepfri_failures.py -v
# Original local archives: freeze output-only diagnoses, then read labels.
python scripts/analyze_deepfri_failures.py classify
python scripts/analyze_deepfri_failures.py metrics
# Public evidence bundle: replay the matched subset without local archives.
python scripts/verify_deepfri_matched_subset.py
```

Use the exact recorded Torch/NumPy CPU versions for metric reproduction. The classifier uses the Python standard library. Original model generations, mixed 4K/16K budget provenance, original scores, and the full planned denominators remain unchanged.
