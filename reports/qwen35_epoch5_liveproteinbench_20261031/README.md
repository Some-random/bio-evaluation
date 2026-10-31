# Qwen3.5-4B epoch-5 LiveProteinBench evaluation

**[Browse all 1,736 results and full responses](ALL_RESULTS.md)** · [Download the results CSV](results.csv) · [Download all responses](epoch5_all_responses.tar.gz)

This is the complete saved **vLLM V2 epoch-5** evaluation: 376/1,736 correct (21.66%), with 156 responses reaching the 32,768-token output limit. The benchmark was previously observed; this is not a fresh blind test.

Each case page includes the complete original input, the scored and reference choices, the originally parsed final answer, and the full saved native output, including unfinished responses. Correctness reflects agreement with the reference choice, not a review of the scientific reasoning. Reference answers were not provided to the model during generation.

| Task | Cases | Correct | Hit 32K |
|---|---:|---:|---:|
| EC_number | 200 | 55 | 7 |
| GO_biological_process | 187 | 38 | 4 |
| GO_cellular_component | 196 | 50 | 3 |
| GO_molecular_function | 192 | 44 | 6 |
| active_site | 136 | 16 | 38 |
| catalytic_activity | 187 | 36 | 10 |
| cofactor | 184 | 47 | 7 |
| motif_position | 49 | 8 | 17 |
| pathway | 187 | 30 | 5 |
| ph | 48 | 9 | 2 |
| temperature | 37 | 10 | 3 |
| transmembrane | 133 | 33 | 54 |

## Source and settings

- Model: Qwen3.5-4B after supervised fine-tuning, epoch 5, checkpoint step 325; teacher Qwen3.8-Flash-Next-NVFP4.
- Generation: B200, vLLM V2, native thinking enabled, 32,768-token output allowance, temperature 1.0, top-p 0.95, top-k 20, presence penalty 1.5, no per-request seed.
- Original benchmark: [LiveProteinBench](https://github.com/Rongdingyi/LiveProteinBench), its [paper](https://arxiv.org/abs/2512.22257), and [dataset release](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/tree/8428f64e33d53330f7745376d9c45de2d2c37eaf); dataset credited to the LiveProteinBench contributors and reused under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Protein sequences originate from [UniProt](https://www.uniprot.org/).
- The full 1,736-case previously approved subset is included; other benchmark cases are outside this run.
- [Run provenance](manifest.json) and [page-by-page verification](verification.json).
