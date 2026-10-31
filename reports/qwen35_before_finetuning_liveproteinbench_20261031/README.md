# Qwen3.5-4B before fine-tuning: LiveProteinBench evaluation

**[Browse all 1,736 results and full responses](ALL_RESULTS.md)** · [Download the results CSV](results.csv) · [Download all responses](original_model_all_responses.tar.gz)

This is the original post-trained Qwen3.5-4B checkpoint **before our supervised fine-tuning**, with no adapter. It scored 524/1,736 (30.18%); 21 responses reached the 32,768-token output limit. The benchmark was previously observed, so this is not a fresh blind test.

Each case page includes the complete input, scored and benchmark choices, and the full saved response once, including native thinking and any final answer. Reference answers were not provided during generation. Agreement with the answer is not an independent validation of the reasoning.

The [epoch-5 V2 results](../qwen35_epoch5_liveproteinbench_20261031/README.md) use the same questions and 32K output limit but a different sampler and seed policy. For a matched older seeded comparison, this original model scored 30.18% and epoch 5 scored 22.41%.

| Task | Cases | Correct | Hit 32K |
|---|---:|---:|---:|
| EC_number | 200 | 56 | 0 |
| GO_biological_process | 187 | 64 | 0 |
| GO_cellular_component | 196 | 51 | 2 |
| GO_molecular_function | 192 | 53 | 4 |
| active_site | 136 | 63 | 2 |
| catalytic_activity | 187 | 61 | 1 |
| cofactor | 184 | 50 | 4 |
| motif_position | 49 | 10 | 1 |
| pathway | 187 | 33 | 2 |
| ph | 48 | 11 | 0 |
| temperature | 37 | 5 | 0 |
| transmembrane | 133 | 67 | 5 |

## Source and settings

- Checkpoint: original post-trained Qwen3.5-4B, revision `851bf6e806efd8d0a36b00ddf55e13ccb7b8cd0a`; no additional fine-tuning adapter.
- Generation: B200, FP16, vLLM torch sampler, native thinking enabled, 32,768-token output allowance, temperature 1.0, top-p 0.95, top-k 20, presence penalty 1.5, deterministic per-question seeds.
- Original benchmark: [LiveProteinBench](https://github.com/Rongdingyi/LiveProteinBench), its [paper](https://arxiv.org/abs/2512.22257), and [dataset release](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/tree/8428f64e33d53330f7745376d9c45de2d2c37eaf); dataset credited to the LiveProteinBench contributors and reused under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Protein sequences originate from [UniProt](https://www.uniprot.org/).
- Includes the complete 1,736-case previously approved subset; other cases are outside this run.
- [Run provenance](manifest.json), [page hashes](verification.json), and [independent page verification](verification_independent.json).
