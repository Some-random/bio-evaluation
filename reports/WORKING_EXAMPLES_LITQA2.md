# Three saved LitQA2 examples

**Qwen3.8-27B: 77/197 correct (39.1%).** All 197 responses parsed and ended normally (`stop`); zero invalid outputs.

The published [Table 1](https://arxiv.org/html/2606.00902v1#S3.T1) reports **38.7% for Qwen3-VL-8B** (a 0.39 percentage-point gap) and **45.7% for GPT-5.2**. This is a numerical comparison, not a reproduction: our run uses 197 of 199 public cases, with a different model, decoder and repeat settings.

These are **three selected correct examples**, not a representative sample. The saved-answer boxes reproduce only the exact answer tags from the final responses. Explanations are omitted and unassessed.

## 1. Olfactory receptor contacts

Active olfactory receptor genes increase their contacts with greek island regions by what factor in mouse olfactory neurons?

- **(A)** 27 fold
- **(B)** 2.7 fold
- **(C)** 1.7 fold
- **(D)** 3.0 fold
- **(E)** 2.0 fold
- **(F)** Insufficient information to answer the question

**Saved final-answer excerpt:** `[ANSWER]B[/ANSWER]`

**Native expected choice:** B — 2.7 fold. **Per-case scorer:** correct.

## 2. Nav1.6 oligosaccharide density

At which amino acid position is a large oligosaccharide density observed in the cryo-EM map of Nav1.6?

- **(A)** Trp324
- **(B)** Leu288
- **(C)** Insufficient information to answer the question
- **(D)** Asn326
- **(E)** Phe302

**Saved final-answer excerpt:** `[ANSWER]D[/ANSWER]`

**Native expected choice:** D — Asn326. **Per-case scorer:** correct.

## 3. Myotendinous junction myonuclei

Based on single-nuclei RNA sequencing data, myotendinous junction myonuclei are enriched for genes involved in which of the following functions?

- **(A)** synaptic transmission
- **(B)** signal transduction
- **(C)** Insufficient information to answer the question
- **(D)** cell–matrix interactions
- **(E)** protein synthesis

**Saved final-answer excerpt:** `[ANSWER]D[/ANSWER]`

**Native expected choice:** D — cell–matrix interactions. **Per-case scorer:** correct.

## Saved records

Each link opens the original saved record. The answer excerpts above omit the remaining response text.

| Example | Record | SHA-256 |
|---|---|---|
| 1 | [request](../results/runs/qwen38_27b_litqa2_replay_2026-10-16/requests/4a27cff2f3f6541679935df8ca4e70602334c42b9db464f182dd222a71234e78.json) | `66f2190ba7a40c35fd647ecfe7cfd00dd11873ea62c97a8162e5ff56f7925e62` |
| 1 | [response](../results/runs/qwen38_27b_litqa2_replay_2026-10-16/responses/4a27cff2f3f6541679935df8ca4e70602334c42b9db464f182dd222a71234e78.json) | `2c97cc25e8908026304bba7cbb906449041e30f69ea5997124fa5e6ad4b66132` |
| 2 | [request](../results/runs/qwen38_27b_litqa2_replay_2026-10-16/requests/a6aafe0b7c9b625dd73f024c3a3e6ba89160e415ba7a202f49e54282d5cc6634.json) | `5a3187d801fb7bd6b9b310ea9298aa23d7e15590fd6a8cce334dd91290b64cda` |
| 2 | [response](../results/runs/qwen38_27b_litqa2_replay_2026-10-16/responses/a6aafe0b7c9b625dd73f024c3a3e6ba89160e415ba7a202f49e54282d5cc6634.json) | `c423bc1b97d674ee09c018096f611fd0906da40060fd8fa2740654796a3cf8da` |
| 3 | [request](../results/runs/qwen38_27b_litqa2_replay_2026-10-16/requests/e9aafc33c850efbc807af98561260c3fd5633389474720b802f2976182c3c080.json) | `1e546c5be91a073ba88bf9a4a57a49875d333202559e75c50ad215d057428f51` |
| 3 | [response](../results/runs/qwen38_27b_litqa2_replay_2026-10-16/responses/e9aafc33c850efbc807af98561260c3fd5633389474720b802f2976182c3c080.json) | `92f8bc27b5d5b542154442b116f768e2bdcd26fe895a7c97a691db5eb3db323d` |

Expected choices were checked directly against `target_choice` in the archived native scorer references and against [per-case results](../results/runs/qwen38_27b_litqa2_replay_2026-10-16/per_case_scores.json). The [JSON companion](WORKING_EXAMPLES_LITQA2.json) records case IDs, paths and source hashes.
