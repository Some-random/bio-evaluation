# DeepFRI / ProtST: biological-process annotation

Qwen3.8-27B BF16 reached terminal closure for all 3,416 released test95 cases. 3412 valid confidence vectors; 4 invalid or missing.

Micro AUPRC and Fmax: **undefined under the native all-case policy**. Four historical ambiguous attempts remain invalid; they were preserved without retries or omission. No valid-only replacement score is reported.

The original scoring subprocess failed during a sibling import before native entry. Its failed status, log and STOP remain preserved. A separately reviewed CPU wrapper performed the first unchanged native score once; generation was not repeated.

[Complete evaluated input](questions/P13_dense_confidence_v1.md). One generation per case with seed 42, nonthinking mode, 16,384 maximum output tokens and the fixed ordered three-decimal confidence vector. Operational continuations and three disjoint whole-model replicas preserved the original payload bytes, model/revision/BF16, sampling and all 3,416 cases.

Native TorchDrug micro AUPRC/Fmax formulas and float32 tie ordering are preserved. This zero-shot full-FASTA text adaptation differs from trained DeepFRI/ProtST representations and the paper’s PDB-modeled/cropped inputs. [DeepFRI (2021)](https://doi.org/10.1038/s41467-021-23303-9); [ProtST (2023)](https://proceedings.mlr.press/v202/xu23t.html). Explanation support is unassessed; pretraining exposure is unknown.
