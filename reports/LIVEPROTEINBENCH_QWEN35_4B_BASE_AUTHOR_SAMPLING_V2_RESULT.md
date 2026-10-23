# LiveProteinBench — Qwen3.5-4B-Base

LiveProteinBench (2025), native sequence-only author-sampling condition: **1,736 completed reviewed cases across 12 tasks**. The source release contains 1,797 cases; 61 were not admitted.

| Task | Evaluated / source | Base accuracy |
|---|---:|---:|
| EC_number | 200 / 200 | 12.50% (25/200) |
| GO_biological_process | 187 / 193 | 18.72% (35/187) |
| GO_cellular_component | 196 / 196 | 20.41% (40/196) |
| GO_molecular_function | 192 / 195 | 9.90% (19/192) |
| active_site | 136 / 146 | 19.85% (27/136) |
| catalytic_activity | 187 / 200 | 15.51% (29/187) |
| cofactor | 184 / 186 | 14.67% (27/184) |
| motif_position | 49 / 52 | 8.16% (4/49) |
| pathway | 187 / 200 | 10.70% (20/187) |
| ph | 48 / 54 | 4.17% (2/48) |
| temperature | 37 / 41 | 2.70% (1/37) |
| transmembrane | 133 / 134 | 9.02% (12/133) |

**Overall: 241/1,736 = 13.8825% accuracy; mean task accuracy: 12.1922%.**

Qwen3.5-4B-Base uses BF16, thinking enabled and a 16,384-token output limit. The frozen author general-thinking sampling recipe was applied to Base; this does not establish an independent Base recommendation. The native four-choice accuracy metric uses the separately declared local `LPB_EXPLICIT_FINAL_ANSWER_V2` parser, rather than the released upstream parser. Explanations were not scored.

All 1,736 responses were saved. The scorer accepted 818 answers and counted 918 invalid answers as incorrect. Saved delivery metadata records 768 truncated empty finals and 647 responses without a generated thinking close; these overlapping counters do not replace the total invalid-answer count. HTTP, transport and response errors, and refusals, were all zero.

The separate Post author-sampling-v2 condition (`sequence_only_qwen35_4b_posttrained_author_sampling_v2`) failed its three-case artificial development delivery gate before benchmark dispatch. That specific condition has no benchmark accuracy.

A separately completed released Qwen3.5-4B Post baseline used NF4 weights, FP16 compute, greedy 16-token generation and thinking disabled, with no added SFT or LoRA adapter. It scored **579/1,736 = 33.3525% accuracy** (31.2694% mean task accuracy). Its generation and precision settings differ from this BF16 Base thinking16K condition. [Published baseline inputs and outputs](https://github.com/Some-random/bio-evaluation/blob/f65480e768941e09186a51fe9394d12fc07b871e/reports/LIVEPROTEINBENCH_QWEN35_4B_POSTTRAINED_ALL_CASES_FULL.md).

Public exports contain extracted generated A/B/C/D choices or null, typed delivery flags, aggregate metrics, admitted IDs, official links, opaque hashes and our publication projection helper source. Free-form generated text, token arrays, questions, choices, sequences, native/prepared requests, upstream code and reference labels are omitted. Complete native inputs and original outputs remain locally retained; these exports are not full trajectories.

[Paper](https://arxiv.org/abs/2512.22257) · [Pinned official source](https://github.com/Rongdingyi/LiveProteinBench/tree/8b9710932511f816651fc1a7e8a1bc85c3c77767)
