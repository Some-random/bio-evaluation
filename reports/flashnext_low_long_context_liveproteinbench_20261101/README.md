# Flash-Next low: 36 long-context LiveProteinBench responses

The 36 selected questions below were each answered once by **NVIDIA Qwen3.8-Flash-Next-NVFP4** using `low` thinking. Open a question to see its original input, the complete saved thinking, and the final response separately.

All 36 responses finished naturally. Mean thinking length: **3,289 tokens**; mean final-response length: **403 tokens**. Final-response length includes the explanation after native thinking. The longest thinking trace contained 17,047 tokens.

No reference answers or source annotations were given to the model. The answers and reasoning have not been checked for correctness. These are 36 selected questions, not a full-benchmark accuracy result.

[Compare with the `xhigh` responses to the same 36 questions](../flashnext_xhigh_long_context_liveproteinbench_20261101/README.md).

| # | Question | Thinking tokens | Final-response tokens |
|---:|---|---:|---:|
| 1 | [EC_number_0050](cases/01_EC_number_0050.md) | 1,147 | 410 |
| 2 | [EC_number_0100](cases/02_EC_number_0100.md) | 1,314 | 418 |
| 3 | [EC_number_0150](cases/03_EC_number_0150.md) | 4,019 | 425 |
| 4 | [GO_biological_process_0046](cases/04_GO_biological_process_0046.md) | 699 | 348 |
| 5 | [GO_biological_process_0096](cases/05_GO_biological_process_0096.md) | 1,022 | 460 |
| 6 | [GO_biological_process_0144](cases/06_GO_biological_process_0144.md) | 976 | 381 |
| 7 | [GO_cellular_component_0049](cases/07_GO_cellular_component_0049.md) | 1,329 | 388 |
| 8 | [GO_cellular_component_0098](cases/08_GO_cellular_component_0098.md) | 652 | 347 |
| 9 | [GO_cellular_component_0147](cases/09_GO_cellular_component_0147.md) | 2,459 | 392 |
| 10 | [GO_molecular_function_0048](cases/10_GO_molecular_function_0048.md) | 1,506 | 369 |
| 11 | [GO_molecular_function_0096](cases/11_GO_molecular_function_0096.md) | 800 | 346 |
| 12 | [GO_molecular_function_0144](cases/12_GO_molecular_function_0144.md) | 772 | 371 |
| 13 | [active_site_0034](cases/13_active_site_0034.md) | 9,110 | 416 |
| 14 | [active_site_0072](cases/14_active_site_0072.md) | 962 | 356 |
| 15 | [active_site_0110](cases/15_active_site_0110.md) | 8,810 | 435 |
| 16 | [catalytic_activity_0053](cases/16_catalytic_activity_0053.md) | 1,042 | 362 |
| 17 | [catalytic_activity_0103](cases/17_catalytic_activity_0103.md) | 1,015 | 324 |
| 18 | [catalytic_activity_0152](cases/18_catalytic_activity_0152.md) | 1,099 | 555 |
| 19 | [cofactor_0046](cases/19_cofactor_0046.md) | 742 | 396 |
| 20 | [cofactor_0093](cases/20_cofactor_0093.md) | 511 | 316 |
| 21 | [cofactor_0139](cases/21_cofactor_0139.md) | 1,187 | 373 |
| 22 | [motif_position_0015](cases/22_motif_position_0015.md) | 15,899 | 549 |
| 23 | [motif_position_0027](cases/23_motif_position_0027.md) | 17,047 | 175 |
| 24 | [motif_position_0039](cases/24_motif_position_0039.md) | 7,364 | 321 |
| 25 | [pathway_0048](cases/25_pathway_0048.md) | 703 | 451 |
| 26 | [pathway_0098](cases/26_pathway_0098.md) | 1,886 | 413 |
| 27 | [pathway_0149](cases/27_pathway_0149.md) | 1,888 | 434 |
| 28 | [ph_0013](cases/28_ph_0013.md) | 1,151 | 349 |
| 29 | [ph_0027](cases/29_ph_0027.md) | 1,723 | 634 |
| 30 | [ph_0041](cases/30_ph_0041.md) | 1,197 | 399 |
| 31 | [temperature_0009](cases/31_temperature_0009.md) | 2,066 | 370 |
| 32 | [temperature_0021](cases/32_temperature_0021.md) | 1,054 | 402 |
| 33 | [temperature_0030](cases/33_temperature_0030.md) | 1,252 | 370 |
| 34 | [transmembrane_0033](cases/34_transmembrane_0033.md) | 9,288 | 487 |
| 35 | [transmembrane_0066](cases/35_transmembrane_0066.md) | 8,236 | 523 |
| 36 | [transmembrane_0100](cases/36_transmembrane_0100.md) | 6,458 | 451 |

## Run details

- Model: [`nvidia/Qwen3.8-Flash-Next-NVFP4`](https://huggingface.co/nvidia/Qwen3.8-Flash-Next-NVFP4), revision `fc694b54fb0174e0913e6adf86691ef85a4ead47`.
- Context: 262,144 tokens shared by input and output; each request could use the remaining context for output. These are new independent responses, not continuations of the earlier 32K run.
- The original benchmark messages requested step-by-step analysis. The model chat template additionally instructed the `low` model to keep thinking brief and focused and move directly to a conclusion.
- Sampling: temperature 1.0, top-p 0.95, top-k 20, presence penalty 1.5, repetition penalty 1.0; no per-request seed. The presence penalty differs from the model's recommended thinking-mode setting.
- Thinking tokens are vLLM-reported reasoning tokens. Final-response text was re-tokenized with the model tokenizer; counts exclude special control tokens.
- Original benchmark: [LiveProteinBench](https://github.com/Rongdingyi/LiveProteinBench), [paper](https://arxiv.org/abs/2512.22257), and [dataset release](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/tree/8428f64e33d53330f7745376d9c45de2d2c37eaf), credited to the LiveProteinBench contributors and reused under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Protein sequences originate from [UniProt](https://www.uniprot.org/).
- [Per-case provenance and hashes](manifest.json).
