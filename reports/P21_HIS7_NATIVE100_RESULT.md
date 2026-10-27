# PFArena T3: separate HIS7 native100 result

Qwen3.8-27B ranked all 100 supplied candidates for one separately adopted HIS7 yeast assay, using its complete 220-residue reference, unchanged native question and legitimate supplied anchor measurement. This is one assay, not 100 independent questions.

| Model | Native Spearman | NDCG | NMS@5 | Recall@5 | Coverage |
| --- | ---: | ---: | ---: | ---: | --- |
| Qwen3.8-27B | 0.153401 | 0.950888 | 0.775829 | 0.000000 | 1 assay, all 100 candidates |

All three fresh artificial delivery controls passed before the single native request. The response contained every supplied identifier exactly once: no missing, unknown or duplicate candidates. HTTP, transport and response errors, truncations, empty finals and refusals were zero. The complete raw outcome was sealed before the owned model server stopped and the original once-only native scorer accessed the held-out measurements. No generation or scoring was repeated.

The run used the pinned original BF16 checkpoint, one B200, vLLM 0.32.0, a 65,536-token context and a 16,384-token output cap. Sampling was temperature 1.0, top-p 0.95, top-k 20, seed 42, n=1, with thinking disabled. A declared JSON schema and mandatory full-permutation prefix constraint controlled delivery; all candidate orderings remained available. The native minimum-five partial-ranking scoring rule was unchanged and distinct from full100 delivery; this output delivered all100.

The source identifier is HIS7_YEAST_Pokusaeva_2019; the underlying [Pokusaeva et al. (2019) study](https://doi.org/10.1371/journal.pgen.1008079) refers to His3. This result measures agreement with the source growth/fitness proxy. It does not establish catalytic kinetics, a mechanism, wet-lab success or historical benchmark equivalence. Prior model exposure to public benchmarks is unknown.

The earlier 8-, 5- and 11-assay P21 conditions remain separate from this new singleton. No pooled 25-assay metric or full67 result is reported. Earlier FULL3 preparation does not define this scientific cohort; its two excluded endpoints were not dispatched in this condition. Original results, interruption boundaries, claims and private evidence are preserved.

The public package contains numerical aggregates, nonrevealing provenance hashes and three exact project-authored delivery modules. The complete native input, requests, responses and ranking remain privately preserved because redistribution rights for the full candidate set have not been established. No protected measurement values, upstream source code, gated data, credentials, environment archives or model weights are published. This limits public trajectory-level reproduction; opaque hashes document the preserved evidence but do not replace it. ProteinGym's software license and the article license are not asserted to license all downstream data.

- [Full-precision aggregate scores](../results/runs/qwen38_27b_p21_HIS7_native100_full_permutation16k_20261026_v1/scores.json)
- [Coverage and error counts](../results/runs/qwen38_27b_p21_HIS7_native100_full_permutation16k_20261026_v1/completion.json)
- [Condition and evidence provenance](../results/runs/qwen38_27b_p21_HIS7_native100_full_permutation16k_20261026_v1/execution_provenance.json)
- [Source and publication boundary](../results/runs/qwen38_27b_p21_HIS7_native100_full_permutation16k_20261026_v1/source_notice.json)
- [Project-authored code](../results/runs/qwen38_27b_p21_HIS7_native100_full_permutation16k_20261026_v1/project_code/permutation_core.py)
