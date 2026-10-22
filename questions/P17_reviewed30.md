# P17: one complete evaluated ProteinGym question

[ProteinGym: Large-Scale Benchmarks for Protein Fitness Prediction and Design (NeurIPS 2023)](https://proceedings.neurips.cc/paper_files/paper/2023/file/cac723e5ff29f65e3fcbb0739ae91bee-Paper-Datasets_and_Benchmarks.pdf). The evaluated data were the official [ProteinGym v1.3 substitution release](https://marks.hms.harvard.edu/proteingym/ProteinGym_v1.3/DMS_ProteinGym_substitutions.zip). This question belongs to the declared pointwise folding-stability adaptation evaluated on 30 of the release’s 217 assays.

**Evaluated case:** `P17::AMFR_HUMAN_Tsuboyama_2023_4G3O::000003::A10H`.

The sealed request contains one user message. That message is copied verbatim and in full below, including both complete supplied sequences, the substitution and the requested output format.

```text
Predict the folding-stability effect of this complete isolated vertebrate protein-domain variant relative to its reference sequence. Return one numerical score: larger means greater folding stability. The score is an uncalibrated prediction for retrospective ranking; it is not a measured free energy or a validated biological function. Do not supply an explanation.

Reference domain sequence:
YFQGQLNAMAHQIQEMFPQVPYHLVLQDLQLTRSVEITTDNILEGRI

Native substitutions:
A10H

Complete variant domain sequence:
YFQGQLNAMHHQIQEMFPQVPYHLVLQDLQLTRSVEITTDNILEGRI

Return exactly a compact JSON object with the single key "score" and a finite number.
```

Source: [published original source and trajectory archive](https://github.com/Some-random/bio-evaluation/blob/9f8568e7dcd05b07aa0975b038ec69a178e9f90e/results/trajectory_archives/qwen38_27b_p17_reviewed30_pointwise_stability_20261021_v2.tar.gz), member `benchmark/requests/b2b31ccf4ad9020f6f6fb810f963a19d3f3b9828fc886ac2df344bb3fe7fb2b9.json`; request SHA-256 `f7235766923d2baa05fa97315bc6db0d76f2d7c5b63966806aa0df061aedf1bd`.
