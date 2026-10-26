# RAbD remaining22: current-backbone sequence recovery

| Model | Delivered/planned | Macro CDRH3 AAR (fraction) | Macro CDRH3 AAR (%) |
|---|---:|---:|---:|
| Qwen3.8-27B | 22/22 | 0.10058052 | 10.0581 |

This retrospective masked-CDRH3 reconstruction condition uses the fixed remaining 22 cases from the original 60-entry source panel. The original 38 run remains a separate condition; no combined 60-case score is reported.

Both artificial long-context exact-copy controls passed before any of the 22 benchmark requests. All 22 responses were delivered once, with zero transport, HTTP, schema, empty-final, truncation or refusal failures. The once-only native scorer computes positional recovery per case and takes the equal-case mean.

The pinned Qwen3.8-27B checkpoint ran locally in BF16 with TP1, vLLM 0.32.0, temperature 0, top_p 1, seed 42, a 16,384-token output budget, a 65,536-token context and thinking disabled. Slurm job 252764 completed 0:0; its owned server stopped.

The [complete sealed archive](https://github.com/Some-random/bio-evaluation/blob/main/results/trajectory_archives/qwen38_27b_p40_remaining22_current_backbone_AAR_20261026.tar.gz) preserves all 24 actual full question/context packets, all 24 raw outcomes, prediction seals, scores, frozen executable sources and the full native MEAN MIT license (109 members). It excludes the protected native reference file, unmasked target coordinates, weights, environments, credentials and full account GPU inventories.

Material qualifications:

- Independently reviewed remaining22 of original60 source entries; old38 is a disjoint previously completed condition; no scores pooled.
- Current official SAbDab IMGT coordinates are not certified historical processed MEAN bytes or graph equivalence.
- Qwen consumes losslessly compact JSON backbone context, not a trained MEAN coordinate graph.
- Target amino-acid identities and all target atom coordinates are withheld; input carries fixed CDRH3 length.
- Native source48-nearest antigen context indices are reused; these indices were computed from the experimental complex, including native target context, as in the released preparation.
- Only sequence recovery is scored; no generated-coordinate RMSD, TMscore, likelihood or functional-binding result is claimed.
- One prospective local-Qwen output per fixed case; no selective retry or trained head.
- Current public benchmark pretraining exposure is unknown; no contamination-free or explanation-support claim.

[Exact scores](https://github.com/Some-random/bio-evaluation/blob/main/results/runs/qwen38_27b_p40_remaining22_current_backbone_AAR_20261026/scores.json) · [Result row](https://github.com/Some-random/bio-evaluation/blob/main/results/runs/qwen38_27b_p40_remaining22_current_backbone_AAR_20261026/result_row.json) · [Execution provenance](https://github.com/Some-random/bio-evaluation/blob/main/results/runs/qwen38_27b_p40_remaining22_current_backbone_AAR_20261026/execution_provenance.json) · [Source notice](https://github.com/Some-random/bio-evaluation/blob/main/results/runs/qwen38_27b_p40_remaining22_current_backbone_AAR_20261026/source_notice.json)
