# ProteinGym reviewed30 isolated-domain stability

Qwen3.8-27B produced all **59,581/59,581** scalar outputs in the fixed **30/217** independently reviewed vertebrate isolated-domain stability assays. Native Spearman: **-0.01406667** (completed_native_scored_reviewed_subset). The other 187 assays remain unadmitted.

The native formula rounds each assay Spearman to three decimals before averaging by UniProt and selection type. All 30 selected assays belong to Stability and have distinct UniProt groups. The metric compares pointwise text predictions with experimental stability measurements; it does not validate explanations or show contamination-free reasoning.

This declared pointwise Qwen adaptation supplies complete reference and variant sequences, mutation identities, and the stability objective. Temperature 0, seed 42, 16,384-token output ceiling, thinking disabled, original pinned BF16 checkpoint, one TP1 GPU. Three artificial exact-copy checks passed before benchmark dispatch. Every admitted variant was attempted once; the sealed cohort was scored once. No training or paid model calls occurred. Native experimental labels stayed outside solver requests.

The earlier allocation 245776 failed before model dispatch because SciPy was absent. Its original traceback, worker and closure are retained in the trajectory archive. Allocation 245782 used the independently reviewed runtime-only repair with isolated CPU NumPy 1.26.4 / SciPy 1.14.1 scoring libraries.

This completes the frozen reviewed30 condition. It does not complete the full 217-assay ProteinGym benchmark or reproduce the historical ProtST/GEMME condition. No directly matched paper scalar is established for this fixed subset. Prior public pretraining exposure is unknown.

[Native scoring source](https://github.com/OATML-Markslab/ProteinGym/blob/1f8de974dead8ff7501eff087b725d14a965e9f9/proteingym/performance_DMS_benchmarks.py). [Exact scores](../../runs/qwen38_27b_p17_reviewed30_pointwise_stability_20261021_v2/scores.json), [result](../../runs/qwen38_27b_p17_reviewed30_pointwise_stability_20261021_v2/result.json), [complete original requests, responses, outcomes and source archive](../../trajectory_archives/qwen38_27b_p17_reviewed30_pointwise_stability_20261021_v2.tar.gz), [archive member hashes](../../trajectory_archives/qwen38_27b_p17_reviewed30_pointwise_stability_20261021_v2.manifest.json).
