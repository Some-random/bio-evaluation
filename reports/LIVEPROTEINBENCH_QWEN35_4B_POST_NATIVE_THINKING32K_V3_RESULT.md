# LiveProteinBench — Qwen3.5-4B native thinking32K V3

This separate post-trained BF16 condition evaluates **1,736 reviewed sequence-only cases** from the 1,797-case 2025 release. All 61 exclusions remain. Source revision: 2026.

| Task | Evaluated / source | Accuracy |
|---|---:|---:|
| EC_number | 200 / 200 | 26.50% (53/200) |
| GO_biological_process | 187 / 193 | 29.95% (56/187) |
| GO_cellular_component | 196 / 196 | 23.98% (47/196) |
| GO_molecular_function | 192 / 195 | 26.56% (51/192) |
| active_site | 136 / 146 | 40.44% (55/136) |
| catalytic_activity | 187 / 200 | 29.95% (56/187) |
| cofactor | 184 / 186 | 27.72% (51/184) |
| motif_position | 49 / 52 | 24.49% (12/49) |
| pathway | 187 / 200 | 14.44% (27/187) |
| ph | 48 / 54 | 29.17% (14/48) |
| temperature | 37 / 41 | 13.51% (5/37) |
| transmembrane | 133 / 134 | 56.39% (75/133) |

Overall accuracy: **28.92%**; mean task accuracy: **28.59%**.

Native input text and the thinking template are preserved, with a 32,768-token output limit. Every truncated, invalid, failed or missing-think-close response is incorrect under this frozen condition. The local explicit-final extractor is not an official released parser. Explanations are not scored.

The full condition combines 932 and 406 preserved historical attempts with 398 once-only untouched continuation attempts. All historical invalids remain invalid. This is not a matched comparison with the older Base 16K condition. No old failed control or other model result is pooled into these scores.

Public records contain extracted generated A/B/C/D labels or null, typed delivery metadata, admitted source IDs, official links and hashes. Native questions, options, sequences, prompts, token arrays, free-form generated text, raw responses, per-case correctness, reference labels and operational metadata remain local. The source archive contains only our pure projector.

[Paper](https://arxiv.org/abs/2512.22257) · [Official source](https://github.com/Rongdingyi/LiveProteinBench/tree/8b9710932511f816651fc1a7e8a1bc85c3c77767)
