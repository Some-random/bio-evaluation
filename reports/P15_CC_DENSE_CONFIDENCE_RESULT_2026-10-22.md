# P15: Gene Ontology cellular-component annotation

**Qwen3.8-27B BF16: micro AUPRC 0.0370570570230484; Fmax 0.07158192247152328.** All 3,416 released test95 cases scored; 3,416 valid confidence vectors and zero invalid or missing outputs.

The model received complete FASTA sequences and 320 fixed, ordered GO descriptions, with one nonthinking generation per case and a 16,384-token output cap. Native TorchDrug micro AUPRC and Fmax formulas, float32 scores and native tie order are preserved. No threshold tuning, ontology score propagation or case filtering was applied.

[Complete saved question, sequence and 320 GO descriptions](questions/P15.md). [Exact score](../results/runs/qwen38_27b_p15_full_test_dense3dp_nonthinking16k_2026-10-20_v1/scores.json), [source and raw trajectory archive](../results/trajectory_archives/qwen38_27b_p15_full_test_dense3dp_nonthinking16k_2026-10-20_v1.tar.gz) and [member manifest](../results/trajectory_archives/qwen38_27b_p15_full_test_dense3dp_nonthinking16k_2026-10-20_v1.manifest.json).

This is a zero-shot full-FASTA text adaptation. It does not reproduce trained DeepFRI/ProtST heads, learned representations or the native PDB-modeled input subset. The common metric formulas permit a qualified comparison; the input and training protocols differ. [DeepFRI (2021)](https://doi.org/10.1038/s41467-021-23303-9); [ProtST (2023)](https://proceedings.mlr.press/v202/xu23t.html). Explanation support is unassessed and prior pretraining exposure is unknown.

The original scoring launcher failed before loading the native scorer because its predecessor job had left Slurm’s live cache. A separately recorded, root-reviewed launch repair used the unchanged scorer once, on CPUs inside the existing successor allocation. Original failed evidence and all prediction seals are retained. No additional model calls or output repairs were made.
