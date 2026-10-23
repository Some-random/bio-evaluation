# LiveProteinBench — Qwen3.8-27B sequence-only results

LiveProteinBench was introduced in 2025; this evaluation uses the pinned May 2026 public code release. The reviewed condition completed **1,736 questions across 12 tasks**, from the 1,797-question public release. The other 61 questions were not admitted to this run. This result covers the reviewed subset.

**Accuracy: 34.56% (600/1,736)**, using every evaluated question, including invalid or failed responses. Explanations were not scored.

| Task | Correct / evaluated | Accuracy | Public source questions |
|---|---:|---:|---:|
| Enzyme classification | 57 / 200 | 28.50% | 200 |
| Biological process | 63 / 187 | 33.69% | 193 |
| Cellular component | 102 / 196 | 52.04% | 196 |
| Molecular function | 53 / 192 | 27.60% | 195 |
| Active site | 76 / 136 | 55.88% | 146 |
| Catalytic activity | 51 / 187 | 27.27% | 200 |
| Cofactor | 58 / 184 | 31.52% | 186 |
| Motif position | 16 / 49 | 32.65% | 52 |
| Pathway | 29 / 187 | 15.51% | 200 |
| Optimal pH | 4 / 48 | 8.33% | 54 |
| Optimal temperature | 6 / 37 | 16.22% | 41 |
| Transmembrane region | 85 / 133 | 63.91% | 134 |

The reported average is count-weighted accuracy. Every question received one attempt. The original sequence-only prompt builder, complete sequences and four options were retained. The released builder omits the Question Text field for the Gene Ontology tasks; that behavior was preserved. Qwen used temperature 0.2, a 10,240-token output cap, seed 42 and hidden thinking disabled; the native prompt still requests reasoning in ordinary final content. A prospectively fixed local final-answer extractor was used because the public release does not include the paper’s scorer. These subset results are not a matched-cohort reproduction of the paper.

Delivery: 1736/1,736 saved responses; 0 transport, 0 HTTP and 0 response errors; 132 truncations, 0 empty finals and 0 refusals. Invalid outputs receive no accuracy credit. A truncated output can earn credit only when its saved final content contains one unambiguous choice.

[Paper](https://arxiv.org/abs/2512.22257) · [Pinned source](https://github.com/Rongdingyi/LiveProteinBench/tree/8b9710932511f816651fc1a7e8a1bc85c3c77767) · [Public extracted-answer and delivery records](https://github.com/Some-random/bio-evaluation/blob/main/results/trajectory_archives/qwen38_27b_liveproteinbench_sequence_only_no_hidden_thinking_delivery_repair_20261022_v1_own_output_publication_v4.manifest.json)

Public per-case records contain only extracted answer choices, delivery metadata, opaque local artifact hashes and official source links. Free-form generated text, all token arrays, native questions/options/sequences/prompts, requests, copied upstream code and protected reference labels are omitted. The complete original native requests, generated outputs and sealed evidence remain local and unchanged. These archives are derived records, not complete raw trajectories.
