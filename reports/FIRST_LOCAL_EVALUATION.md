# First local evaluation: LAB-Bench LitQA2

**Completed:** 197/197 reviewed public questions on Qwen3.8-27B, one H200, in 20.46 minutes. **77 correct**, 111 incorrect answered questions, 9 abstentions; zero parser, transport or truncation failures.

| Metric | Result | Count |
|---|---:|---|
| Accuracy | 39.1% | 77 / 197 questions |
| Precision among non-abstaining outputs | 41.0% | 77 / 188 answered questions |
| Coverage | 95.4% | 188 / 197 questions answered |

All 197 saved request/response pairs and per-case labels reconcile with the metrics. The exact frozen files are archived with the run. Raw outputs, scores and audit are in `../results/runs/qwen38_27b_litqa2_public_reviewed_2026-10-15/`. These are answer-agreement results; explanation support is unassessed and public-benchmark training exposure is unknown.

The first Qwen evaluation is the input-reviewed public LitQA2 subset: **197 of 199 questions**. Two case IDs are held in `configs/local_labbench_litqa2_review.json` before inference because their questions select pathogen spike mutations in an antibody-response context. No P18 requests are transferred. The OpenAI inference hold remains active.

The model receives the exact prepared native multiple-choice prompt, shuffled choices and “Think step by step” instruction, with no added system prompt. It receives no reference answer labels, papers, source-only metadata, tools or retrieval. The runner reads only inputs and execution metadata. A separate process reads reference labels after outputs have been recorded and uses the pinned deterministic LAB-Bench/ChemBench parser and native accuracy, precision and coverage. Parser failures count incorrect and non-abstaining; transport failures are disclosed separately. An interrupted uncertain generation is never silently resampled.

Qwen/Qwen3.8-27B is pinned at `1d4bf0f2ff6012fd82039f2fa52739d0dd7c60c0`, original BF16, one H200 (physical GPU 5), vLLM 0.31.0. The frozen run uses publisher sampling defaults (temperature 1, top-p .95, top-k 20), seed 42, medium thinking, one completion and 4096 total output tokens per question. No protected outcomes were used to choose these settings, and they will not be changed in response to test results.

## Interpretation

| Evaluation | Likely demands (provisional) | Actually supplied | Reference source | What scores establish |
|---|---|---|---|---|
| B01 / NATIVE_PUBLIC_COT_LOCAL_REVIEWED | Biological knowledge and answer selection; recall, distractor elimination and inference can all contribute | Each dispatched request contains only the original question/choices and native instructions; exact payload hashes saved in the run directory | Creator-curated public LAB-Bench ideal/distractor labels, separated into scorer references | High: agreement with these curated answers under closed-book resources. Low: limited recovery under these inputs; does not isolate knowledge, reasoning or source availability. Neither score validates explanations. |

This is a single-run public-subset baseline using native prompts and metrics. It is **not** the paper's full 248-question LitQA2 evaluation, nor a three-run mean. Five public B01 questions were previously completed with another model; their presence is disclosed in the review record and their IDs remain recorded in the earlier run. No Qwen prompt/model selection uses those outcomes. Prior model training exposure to this public benchmark remains unknown; no claim of contamination-free reasoning is warranted. No explanation-support score is computed.

Source: [LAB-Bench paper](https://arxiv.org/html/2407.10362v3), official code revision `998a8e0a40cf116c80e1b0e7a805ebb5fb9fa838`, dataset revision `5c77cec648430f30611808808861eb86f81d5eaa`. Native model baselines in the paper were also tool-free; human baselines had different resource access. Any paper headline number must be labeled contextual rather than an identical-sample comparison.

Run: `results/runs/qwen38_27b_litqa2_public_reviewed_2026-10-15/`. Progress, raw requests/responses, scores, per-case parser outcomes, token use and elapsed times are preserved locally. The detached worker completed generation and automatically ran offline scoring successfully. No GitHub upload is scheduled.

Validation: seven synthetic contract checks passed, including answer-key rejection, task/case allowlists, local-only endpoint restriction, one-completion/tool-free fields, parser failure treatment and agreement with the pinned official metric function. No benchmark example was used as a development test.

## Historical paper context

The paper reports these rounded LitQA2 values in Tables 2–4. These are full-set three-run model means, shown for context; they are not measured on our identical 197-case subset. No claim of an item-matched improvement or contamination-free reasoning follows.

| Historical model | Accuracy | Precision | Coverage |
|---|---:|---:|---:|
| GPT-4o | 27% | 46% | 58% |
| Llama 3 70B Instruct | 35% | 38% | 92% |
| Claude 3.5 Sonnet (20240620) | 6% | 47% | 12% |

[Paper Tables 2–4](https://arxiv.org/html/2407.10362v3) report 248 public/private questions and means over three model runs. Our config records one seeded run, 197 reviewed public questions, medium Qwen thinking and a fixed output cap. The paper describes a Claude-2 answer-extraction fallback; our pinned public-code deterministic parser has no configured model fallback. Any unparsed output is disclosed and scored according to that deterministic path. Historic human scores are omitted from this table because humans had retrieval and other tools. The numeric source ledger is `published_litqa2_context.json`.
