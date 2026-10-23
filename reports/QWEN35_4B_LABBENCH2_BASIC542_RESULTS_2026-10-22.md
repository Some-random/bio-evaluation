# Qwen3.5 4B and 4B-Base: LABBench2 BASIC text QA (2026)

Completed paired evaluation of 542 reviewed cases per model in the author-supported BASIC closed-book question-only condition. The five source categories contain 620 rows; 78 prior exclusions remain excluded. Figures, tables, tools, retrieved documents and attachments were outside this condition.

| Task | Selected/source rows | Qwen3.5-4B-Base accuracy | Qwen3.5-4B accuracy |
| --- | ---: | ---: | ---: |
| LitQA3 | 154/168 | 11.69% (18/154) | 9.74% (15/154) |
| TrialQA | 120/120 | 12.50% (15/120) | 12.50% (15/120) |
| DbQA2 | 83/86 | 1.20% (1/83) | 3.61% (3/83) |
| PatentQA | 106/121 | 9.43% (10/106) | 10.38% (11/106) |
| SuppQA2 | 79/125 | 1.27% (1/79) | 6.33% (5/79) |
| Pooled selected cases | 542/620 | 8.30% (45/542) | 9.04% (49/542) |

Per-category binary accuracy preserves the native scorer. The pooled row is a descriptive weighted accuracy over this selected subset. These results cover 542 selected cases, with no full-release or retrieval-performance claim. The release has 1912 configuration rows, including alternate conditions; 1373 ordinary candidate rows and 1211 prepared packets are separate preparation denominators.

Base saved 542 outputs (5 truncated; 5 empty finals). Posttrained saved 542 outputs (9 truncated; 26 empty finals). Both whole-cohort seals preceded reference access. The fixed local Qwen3.8-27B judge made 1053 real judgments and 2 predeclared artificial checks; 1 real judgments were invalid. Candidate errors, empty finals and invalid judgments score zero under the frozen policy. No selective retries were used.

Both original BF16 checkpoints used the same native template, thinking enabled, temperature 1.0, top_p 0.95, top_k 20, presence penalty 1.5 and seed 42. The 16,384-token output cap includes reasoning and final text, with 65,536-token context. This cap is below the post-trained card's 32,768-token recommendation and the source BASIC harness's 64,000-token limit. The post-trained general-thinking recipe was applied identically to Base; no separate Base recommendation is claimed.

Judging uses the original category rubrics with fixed local Qwen3.8-27B, replacing native Claude Sonnet 4.5. This is an adapted local-judge condition. Reference-supported answer grading does not independently validate the model's reasoning. Public pretraining exposure is unknown.

Inputs and protocol: [publisher dataset](https://huggingface.co/datasets/EdisonScientific/labbench2), [pinned author code](https://github.com/EdisonScientific/labbench2/tree/a490cd40379edd603fb8b6b6d3fe47ebb0712e8d), [paper](https://arxiv.org/html/2604.09554v2). Publisher metadata identifies CC-BY-SA-4.0; attribution: Edison Scientific, LABBench2. Question text, references, prompt-bearing claims, raw answers and judge rationales remain outside this public numeric package.

Artifacts: [numeric report](QWEN35_4B_LABBENCH2_BASIC542_RESULTS_2026-10-22.json), [per-case scores](../results/runs/qwen35_4b_labbench2_basic542_author_general_thinking16k_20261022_v2/per_case_scores.json), [protocol](../results/runs/qwen35_4b_labbench2_basic542_author_general_thinking16k_20261022_v2/protocol.json), [completion](../results/runs/qwen35_4b_labbench2_basic542_author_general_thinking16k_20261022_v2/completion.json).
