# Flash-Next xhigh: 36 long-context LiveProteinBench responses

The 36 selected questions below were each answered once by **NVIDIA Qwen3.8-Flash-Next-NVFP4** using `xhigh` thinking. Open a question to see its original input, the complete saved thinking, and the final response separately.

All 36 responses finished naturally. Mean thinking length: **24,267 tokens**; mean final-response length: **248 tokens**. Final-response length includes the explanation after native thinking. Ten thinking traces exceeded 32,768 tokens; the longest contained 62,800 thinking tokens.

No reference answers or source annotations were given to the model. The answers and reasoning have not been checked for correctness. These are 36 selected questions, not a full-benchmark accuracy result.

| # | Question | Thinking tokens | Final-response tokens |
|---:|---|---:|---:|
| 1 | [EC_number_0050](cases/01_EC_number_0050.md) | 49,459 | 243 |
| 2 | [EC_number_0100](cases/02_EC_number_0100.md) | 33,983 | 242 |
| 3 | [EC_number_0150](cases/03_EC_number_0150.md) | 54,764 | 260 |
| 4 | [GO_biological_process_0046](cases/04_GO_biological_process_0046.md) | 21,360 | 177 |
| 5 | [GO_biological_process_0096](cases/05_GO_biological_process_0096.md) | 667 | 140 |
| 6 | [GO_biological_process_0144](cases/06_GO_biological_process_0144.md) | 7,849 | 224 |
| 7 | [GO_cellular_component_0049](cases/07_GO_cellular_component_0049.md) | 11,726 | 178 |
| 8 | [GO_cellular_component_0098](cases/08_GO_cellular_component_0098.md) | 2,373 | 148 |
| 9 | [GO_cellular_component_0147](cases/09_GO_cellular_component_0147.md) | 17,190 | 201 |
| 10 | [GO_molecular_function_0048](cases/10_GO_molecular_function_0048.md) | 12,566 | 216 |
| 11 | [GO_molecular_function_0096](cases/11_GO_molecular_function_0096.md) | 2,467 | 182 |
| 12 | [GO_molecular_function_0144](cases/12_GO_molecular_function_0144.md) | 18,873 | 140 |
| 13 | [active_site_0034](cases/13_active_site_0034.md) | 17,405 | 259 |
| 14 | [active_site_0072](cases/14_active_site_0072.md) | 2,666 | 182 |
| 15 | [active_site_0110](cases/15_active_site_0110.md) | 44,969 | 220 |
| 16 | [catalytic_activity_0053](cases/16_catalytic_activity_0053.md) | 39,886 | 357 |
| 17 | [catalytic_activity_0103](cases/17_catalytic_activity_0103.md) | 8,749 | 227 |
| 18 | [catalytic_activity_0152](cases/18_catalytic_activity_0152.md) | 18,608 | 272 |
| 19 | [cofactor_0046](cases/19_cofactor_0046.md) | 3,449 | 200 |
| 20 | [cofactor_0093](cases/20_cofactor_0093.md) | 5,322 | 225 |
| 21 | [cofactor_0139](cases/21_cofactor_0139.md) | 13,631 | 222 |
| 22 | [motif_position_0015](cases/22_motif_position_0015.md) | 56,413 | 268 |
| 23 | [motif_position_0027](cases/23_motif_position_0027.md) | 62,800 | 207 |
| 24 | [motif_position_0039](cases/24_motif_position_0039.md) | 13,080 | 133 |
| 25 | [pathway_0048](cases/25_pathway_0048.md) | 32,744 | 220 |
| 26 | [pathway_0098](cases/26_pathway_0098.md) | 18,767 | 225 |
| 27 | [pathway_0149](cases/27_pathway_0149.md) | 18,580 | 248 |
| 28 | [ph_0013](cases/28_ph_0013.md) | 50,508 | 411 |
| 29 | [ph_0027](cases/29_ph_0027.md) | 16,460 | 249 |
| 30 | [ph_0041](cases/30_ph_0041.md) | 16,902 | 241 |
| 31 | [temperature_0009](cases/31_temperature_0009.md) | 58,108 | 241 |
| 32 | [temperature_0021](cases/32_temperature_0021.md) | 29,045 | 206 |
| 33 | [temperature_0030](cases/33_temperature_0030.md) | 31,083 | 237 |
| 34 | [transmembrane_0033](cases/34_transmembrane_0033.md) | 27,163 | 522 |
| 35 | [transmembrane_0066](cases/35_transmembrane_0066.md) | 15,501 | 549 |
| 36 | [transmembrane_0100](cases/36_transmembrane_0100.md) | 38,508 | 453 |

## Run details

- Model: [`nvidia/Qwen3.8-Flash-Next-NVFP4`](https://huggingface.co/nvidia/Qwen3.8-Flash-Next-NVFP4), revision `fc694b54fb0174e0913e6adf86691ef85a4ead47`.
- Context: 262,144 tokens shared by input and output; each request could use the remaining context for output. These are new independent responses, not continuations of the earlier 32K run.
- The original benchmark messages requested step-by-step analysis. The model chat template additionally instructed the `xhigh` model to think carefully, validate assumptions, consider alternatives, and prioritize correctness and clarity.
- Sampling: temperature 1.0, top-p 0.95, top-k 20, presence penalty 1.5, repetition penalty 1.0; no per-request seed. The presence penalty differs from the model's recommended thinking-mode setting.
- Thinking tokens are vLLM-reported reasoning tokens. Final-response text was re-tokenized with the model tokenizer; counts exclude special control tokens.
- Original benchmark: [LiveProteinBench](https://github.com/Rongdingyi/LiveProteinBench), [paper](https://arxiv.org/abs/2512.22257), and [dataset release](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/tree/8428f64e33d53330f7745376d9c45de2d2c37eaf), credited to the LiveProteinBench contributors and reused under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Protein sequences originate from [UniProt](https://www.uniprot.org/).
- [Per-case provenance and hashes](manifest.json).
