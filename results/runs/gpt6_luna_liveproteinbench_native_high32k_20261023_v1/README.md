# GPT-6 Luna: LiveProteinBench native-text result

The reviewed 1,736-case condition scored **65.3226%** micro accuracy (1134/1736) and **63.2794%** mean task accuracy.

GPT-6 Luna used high reasoning effort, a 32,768-token output limit, the Responses API, no tools, and `store:false`. Native reviewed message text was retained. The original 64 and untouched-only 128 concurrency segments used identical scientific inputs and settings; 801 and 935 LPB responses respectively form this full-cohort score. No attempted case was retried.

Coverage is **1,736/1,797 source cases** across 12 tasks; all 61 prior exclusions remain excluded. This is not a full 1,797-case result. The final-choice parser is a pinned local adaptation, not an upstream released parser. Invalid outputs count as incorrect; explanation correctness was not scored.

Delivery: 0 truncations, 0 empty finals, 0 refusals. Status counts: `{"status_completed": 1736}`.

Recorded LPB usage: 1,002,718 input and 4,933,692 output tokens; 0 cases lack complete usage. The standard uncached estimate for recorded usage is $2.567118; this is not an invoice. The conservative reserved LPB maximum was $29.324348. The shared Luna run retained a $50 guard including development and LABBench2 calls.

| Task | Correct | Cases | Accuracy |
|---|---:|---:|---:|
| EC_number | 117 | 200 | 58.5000% |
| GO_biological_process | 125 | 187 | 66.8449% |
| GO_cellular_component | 140 | 196 | 71.4286% |
| GO_molecular_function | 141 | 192 | 73.4375% |
| active_site | 121 | 136 | 88.9706% |
| catalytic_activity | 145 | 187 | 77.5401% |
| cofactor | 114 | 184 | 61.9565% |
| motif_position | 35 | 49 | 71.4286% |
| pathway | 47 | 187 | 25.1337% |
| ph | 23 | 48 | 47.9167% |
| temperature | 11 | 37 | 29.7297% |
| transmembrane | 115 | 133 | 86.4662% |

Source credit: Copyright (c) 2026 LiveProteinBench contributors. The matched [Hugging Face dataset release](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/tree/8428f64e33d53330f7745376d9c45de2d2c37eaf) is pinned at `8428f64e33d53330f7745376d9c45de2d2c37eaf` and distributed under [CC-BY-4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). See the [LiveProteinBench paper](https://arxiv.org/abs/2512.22257) and [implementation](https://github.com/Rongdingyi/LiveProteinBench), pinned commit `8b9710932511f816651fc1a7e8a1bc85c3c77767`. Public benchmark exposure during pretraining is unknown.

Original native prompt text was retained; content items were encoded in the Responses API envelope. Public response copies redact private identifier metadata and opaque encrypted reasoning metadata; visible reasoning and final text are unchanged, as documented by per-case original/public hashes.

Eight trajectory archives retain the reviewed LPB requests, metadata-redacted API response copies, visible finals, records and dispatch receipts. Original response bytes remain private; provenance records both original and public hashes and names each redacted metadata field. Gold reference rows, private identities/keys, model weights and unrelated LABBench2 outputs are omitted.
