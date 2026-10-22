# PFArena T3: separate five-assay stability condition

Qwen3.8-27B ranked all candidates for five independently reviewed eukaryote isolated-domain stability assays from the native67-assay panel: algal centrin, social-amoeba MlcC, frog calmodulin and two chicken-spectrin-derived SH3 chimeras. Complete native67–72-residue fragments, all114candidate IDs and legitimate anchor measurements were preserved. Source PDB chains differ and were not substituted.

| Model | Spearman | NDCG | NMS@5 | Recall@5 | Assays |
|---|---:|---:|---:|---:|---:|
| Qwen3.8-27B | 0.241139 | 0.889126 | 0.870668 | 0.400000 | 5/67 |

All five responses contained complete native candidate permutations with zero transport/response errors, empty finals or truncations. Three artificial delivery checks passed before benchmark dispatch. One native scoring attempt ran after the complete immutable prediction seal. The prompt's supplied anchor measurement was retained; candidate outcome measurements stayed scorer-only.

The declared baseline uses pinned original BF16 Qwen3.8-27B, one A100, nonthinking uniform16,384-token output, unchanged native prompts/scoring formulas and a declared mandatory full-permutation JSON constraint retaining every ranking order. This is retrospective agreement with existing stability measurements, not experimental validation, mechanism assessment or matched-paper reproduction. Public pretraining exposure is unknown.

This new five-assay condition is separate from the previously scored eight-assay condition. No pooled score is reported. Together they cover13distinct native assays;54native inputs remain unreviewed. The full67-assay setting remains incomplete. GPT models were not evaluated on this subset.

- [Exact native scores](scores.json)
- [Exact raw requests and responses](../../trajectory_archives/P21_stability5_qwen38_27b_v1_20261021.tar.gz)
- [Exact execution and scoring source](../../protocol_artifacts/P21_stability5_qwen38_27b_v1_source_20261021.tar.gz)
