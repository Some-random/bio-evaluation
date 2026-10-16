# Published examples of protein-model tool use

These four cases were actually reported in the catalog's papers. The numbers below are **published reference results, not new local runs**.

**What AlphaFold does:** AlphaFold2 predicts a protein's three-dimensional structure from its amino-acid sequence, using alignment and optional template evidence. It also estimates confidence. Its pLDDT score runs from 0 to 100; it is **prediction confidence, not experimentally measured stability or function**. [AF2 paper](https://www.nature.com/articles/s41586-021-03819-2), [official output documentation](https://github.com/google-deepmind/alphafold#alphafold-output).

| Published evaluation | Actual model chain | Verified result and conditions |
|---|---|---|
| ProteinBench inverse folding | Target backbone → ProteinMPNN sequence → **AlphaFold2** structure comparison | At 100 residues: median scTM **0.962**, pLDDT **94.14**. Ten RFdiffusion backbones per length; sampling temperature 0.1. [§§2.1.1, 3.1.1; Table 2](https://arxiv.org/html/2409.06744v2#S3.SS1.SSS1) |
| ProteinBench backbone generation | RFdiffusion backbone → **ProteinMPNN** sequence → **ESMFold** refolding | At 100 residues: scRMSD **0.48 ± 0.56 Å**, as printed. Generated sample count not verified. [§§2.1.2, 3.1.2; Table 3](https://arxiv.org/html/2409.06744v2#S3.SS1.SSS2) |
| ProteinBench sequence generation | DPLM-650M sequence → **AlphaFold2** confidence | At 100 residues: pLDDT **85.38 ± 14.20**; 50 sequences per model/length. [§3.1.3; Table 4](https://arxiv.org/html/2409.06744v2#S3.SS1.SSS3) |
| NatureLM unconditional generation (P37) | NatureLM-8x7B sequence → **OmegaFold** confidence | Mean pLDDT **75.9** for the subset shorter than 100 residues; generation starts with `<protein>`. [§4.1; Table 8](https://arxiv.org/html/2502.07527v3#S4.SS1) |

In these examples, the bold models are offline evaluators or evaluation helpers. The papers used them to compute results; these cases do not establish that an LLM autonomously chose and called tools.

ProteinBench's methods mention both AF2 and ESMFold; Table 4 explicitly labels pLDDT as AF2. Table 3's printed ± notation is retained. NatureLM's value concerns the short-sequence subset.

The [machine-readable evidence](PUBLISHED_TOOL_USE_EXAMPLES.json) records the exact source versions, roles, conditions, numerical fields and qualifications.
