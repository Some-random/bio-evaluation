# Qwen3.5-4B matched thinking16K classification

These are the unchanged Base and released Post conditions. Each retains the full P03 (2,773) and P01 (1,999) denominators.
Immutable old responses and only previously untouched-case continuation responses form each native score. Truncated, empty and ambiguous outcomes remain invalid; none were regenerated.

| Model | Task | Planned | Native metrics |
| --- | --- | ---: | --- |
| base | P03 | 2773 | `{"accuracy": 0.1709340064911648, "all_case_rule": "Every frozen planned case remains in denominator; missing, transport, exception and invalid final outputs count incorrect.", "correct": 474, "invalid_or_missing": 680, "parsed": 2093, "planned": 2773, "statuses": {"completed": 2492, "response_error": 281}}` |
| base | P01 | 1999 | `{"accuracy": 0.4117058529264632, "all_case_rule": "Every frozen planned case remains in denominator; missing, transport, exception and invalid final outputs count incorrect.", "correct": 823, "invalid_or_missing": 434, "parsed": 1565, "planned": 1999, "statuses": {"completed": 1999}}` |
| posttrained | P03 | 2773 | `{"accuracy": 0.16696718355571583, "all_case_rule": "Every frozen planned case remains in denominator; missing, transport, exception and invalid final outputs count incorrect.", "correct": 463, "invalid_or_missing": 747, "parsed": 2026, "planned": 2773, "statuses": {"completed": 2463, "response_error": 310}}` |
| posttrained | P01 | 1999 | `{"accuracy": 0.48574287143571787, "all_case_rule": "Every frozen planned case remains in denominator; missing, transport, exception and invalid final outputs count incorrect.", "correct": 971, "invalid_or_missing": 48, "parsed": 1951, "planned": 1999, "statuses": {"completed": 1998, "response_error": 1}}` |

The individual score files retain native delivery and invalid-output counts. Outcome accuracy does not establish explanation support. Public pretraining exposure is unknown.

Raw reviewed inputs, visible generated text/token IDs, requests/responses, frozen source and exact upstream license/attribution metadata are preserved in byte-reconstructable archive parts. Reference rows, weights, environments and private resource inventories are excluded.
General-thinking sampling is matched across checkpoints at 16,384 output tokens (temperature 1.0, top-p 0.95, top-k 20, presence penalty 1.5, seed 42). Guidance comes from the released Post model; no separate Base recommendation or specialist-head reproduction is claimed.
Dataset, ontology and upstream publication attribution with the exact applicable publisher declarations are included under licenses/SOURCE_ATTRIBUTION.json; no functional or experimental validation follows.
