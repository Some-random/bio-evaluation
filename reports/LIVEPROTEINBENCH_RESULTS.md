# LiveProteinBench model results

Snapshot: **November 2, 2026**. This page collects our existing sequence-only LiveProteinBench results and the paper's published reference scores.

Our evaluations use **1,736 questions across 12 tasks** from the benchmark's 1,797-question release. Accuracy is the number of answers matching the benchmark's saved choice divided by all evaluated questions; unparsed and empty answers count as incorrect in the recorded scores. The benchmark has been used in previous experiments, and answer agreement does not by itself evaluate the scientific reasoning.

## Our model results

| Model or checkpoint | Correct / questions | Recorded accuracy | Setting |
|---|---:|---:|---|
| [GPT-6 Luna](LIVEPROTEINBENCH_GPT6_LUNA_HIGH32K_RESULT.md) | 1,134 / 1,736 | 65.32% | High reasoning, 32K output |
| Qwen3.8-Flash-Next NVFP4 | 838 / 1,736 | 48.27% | Xhigh, full context |
| [Qwen3.8-27B](LIVEPROTEINBENCH_QWEN27B_OWN_OUTPUT_RESULT.md) | 600 / 1,736 | 34.56% | Earlier project run |
| [Qwen3.5-4B, thinking off](LIVEPROTEINBENCH_QWEN35_4B_POSTTRAINED_EXISTING_OUTPUTS.md) | 579 / 1,736 | 33.35% | Earlier project run |
| Qwen3.5-4B before our new training | 541 / 1,736 | 31.16% | Thinking, full context |
| Qwen3.5-4B, low-effort training, epoch 1 | 496 / 1,736 | 28.57%* | Thinking, full context |
| Qwen3.5-4B, low-effort training, epoch 2 | 559 / 1,736 | 32.20%* | Thinking, full context |
| Qwen3.5-4B, low-effort training, epoch 3 | 577 / 1,736 | 33.24%* | Thinking, full context |

\* **Provisional parser-based scores.** The scorer failed to extract choices from some nonempty checkpoint responses, including responses that explicitly selected the saved answer. The figures shown are the original recorded counts; rescoring is pending. Epochs 4 and 5 and the xhigh-trained checkpoints are not included in this snapshot.

### Delivery and parsing for the current full-context runs

| Model or checkpoint | Unparsed, including empty | Nonempty but unparsed | Reached context limit |
|---|---:|---:|---:|
| Flash-Next xhigh | 28 | 0 | 27 |
| Original Qwen3.5-4B | 27 | 0 | 26 |
| Low-effort epoch 1 | 29 | 21 | 7 |
| Low-effort epoch 2 | 28 | 25 | 3 |
| Low-effort epoch 3 | 19 | 15 | 4 |

The original 4B and low-effort checkpoints use the same benchmark cases, task instructions and sampling settings. They use a 262,144-token total context, with the prompt occupying part of that allowance, on vLLM `0.32.0rc1.dev100+g77154ca61.cu129`. Sampling is temperature 1.0, top-p 0.95, top-k 20, min-p 0, presence penalty 1.5, frequency penalty 0 and repetition penalty 1.0. No per-request seed was supplied; the server's default seed was 0. Flash-Next uses xhigh reasoning and the same sampling values except for a presence penalty of 0. Earlier project runs used different model and inference settings; their linked reports contain their settings.

The low-effort checkpoints were trained on **9,988** naturally completed, nonempty Flash-Next responses generated without the saved answer keys. The training set added 124 repeated examples to fill batches. No examples were filtered by answer-key agreement. The xhigh training run is in progress.

## Earlier 32K training experiment

For an earlier, separate experiment, a matched seeded evaluation on the same 1,736 cases with a 32,768-token output allowance recorded **524/1,736 (30.2%)** before training, **318/1,736 (18.3%)** after epoch 1, and **389/1,736 (22.4%)** after epoch 5. These are not the new full-context runs above.

## Published reference scores

The [LiveProteinBench paper, Table 5](https://arxiv.org/html/2512.22257v1#A4.T5), reports the following sequence-only scores on the full **1,797-question** release:

| Model | Paper-reported accuracy |
|---|---:|
| GPT-5 | 60.49% |
| OpenAI o3 | 56.04% |
| Claude 3.7 Sonnet | 51.47% |
| GPT-4o | 38.39% |

The paper's full release and our 1,736-question subset differ, as do model and inference settings.

## Available response collections

- [GPT-6 Luna questions, answers and visible explanations](LIVEPROTEINBENCH_GPT6_LUNA_EXPLANATIONS.md).
- [Original Qwen3.5-4B responses from the earlier seeded 32K evaluation](qwen35_before_finetuning_liveproteinbench_20261031/README.md).
- [Qwen3.5-4B epoch-5 responses from a separate 32K evaluation](qwen35_epoch5_liveproteinbench_20261031/README.md). This V2 run used a different sampler and seed policy and scored 21.66%; it is distinct from the matched seeded epoch-5 score of 22.4% above.

The new full-context run's per-case responses are retained locally; they are not included in this page.

[Benchmark paper](https://arxiv.org/abs/2512.22257) · [Benchmark repository](https://github.com/Rongdingyi/LiveProteinBench) · [Earlier biology evaluations page](OPENAI_ANTHROPIC_BIO_EVALUATIONS.md)
