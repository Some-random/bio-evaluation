# LiveProteinBench model results

Snapshot: **November 2, 2026**. This page brings together sequence-only LiveProteinBench model results. Test sets and evaluation settings differ between results. Accuracy measures agreement with the benchmark's saved answer.

## Results

| Model or checkpoint | Accuracy | Setting |
|---|---:|---|
| **Our trained Qwen checkpoints** | | |
| Qwen3.5-4B, low-effort training, epoch 5 | 35.43%* | Thinking, full context |
| Qwen3.5-4B, low-effort training, epoch 4 | 34.91%* | Thinking, full context |
| Qwen3.5-4B, low-effort training, epoch 3 | 33.24%* | Thinking, full context |
| Qwen3.5-4B, low-effort training, epoch 2 | 32.20%* | Thinking, full context |
| Qwen3.5-4B, low-effort training, epoch 1 | 28.57%* | Thinking, full context |
| Qwen3.5-4B, earlier training, epoch 5 | 22.41% | Earlier matched seeded 32K evaluation |
| [Qwen3.5-4B, earlier training, epoch 5 V2](qwen35_epoch5_liveproteinbench_20261031/README.md) | 21.66% | Separate 32K evaluation, different sampler and seed policy |
| Qwen3.5-4B, earlier training, epoch 1 | 18.32% | Earlier matched seeded 32K evaluation |
| **Base and other models** | | |
| [GPT-6 Luna](LIVEPROTEINBENCH_GPT6_LUNA_HIGH32K_RESULT.md) | 65.32% | High reasoning, 32K output |
| [GPT-5](https://arxiv.org/html/2512.22257v1#A4.T5) | 60.49% | Sequence only |
| [OpenAI o3](https://arxiv.org/html/2512.22257v1#A4.T5) | 56.04% | Sequence only |
| [Claude 3.7 Sonnet](https://arxiv.org/html/2512.22257v1#A4.T5) | 51.47% | Sequence only |
| Qwen3.8-Flash-Next NVFP4 | 48.27% | Xhigh reasoning, full context |
| [Gemini 2.5 Pro](https://arxiv.org/html/2512.22257v1#A4.T5) | 43.85% | Sequence only |
| [Gemini 2.0 Flash](https://arxiv.org/html/2512.22257v1#A4.T5) | 43.07% | Sequence only |
| [GPT-4o](https://arxiv.org/html/2512.22257v1#A4.T5) | 38.39% | Sequence only |
| [Qwen3.8-27B](LIVEPROTEINBENCH_QWEN27B_OWN_OUTPUT_RESULT.md) | 34.56% | Earlier evaluation; see linked report |
| [Qwen3.5-4B, thinking off](LIVEPROTEINBENCH_QWEN35_4B_POSTTRAINED_EXISTING_OUTPUTS.md) | 33.35% | Earlier evaluation; see linked report |
| [Qwen2.5-VL-32B](https://arxiv.org/html/2512.22257v1#A4.T5) | 33.05% | Sequence only |
| Qwen3.5-4B before the new training | 31.16% | Thinking, full context |
| [Qwen3.5-4B before the earlier training](qwen35_before_finetuning_liveproteinbench_20261031/README.md) | 30.18% | Earlier matched seeded 32K evaluation |
| [Qwen3.5-4B, thinking, 32K](LIVEPROTEINBENCH_QWEN35_4B_POST_NATIVE_THINKING32K_V3_RESULT.md) | 28.92% | Earlier evaluation; see linked report |
| [InternVL3-78B](https://arxiv.org/html/2512.22257v1#A4.T5) | 23.37% | Sequence only |
| [Qwen3.5-4B-Base](LIVEPROTEINBENCH_QWEN35_4B_BASE_AUTHOR_SAMPLING_V2_RESULT.md) | 13.88% | Earlier 16K evaluation; many answers were not delivered in a scorable form |

* **Provisional scores:** the current scorer missed the selected choice in some nonempty checkpoint responses, which were counted as incorrect. Rescoring is pending. The xhigh-trained checkpoints are still in progress.

## How we made the training data

The [original question set](https://huggingface.co/datasets/jiangdongwei/protein-sequence-reasoning-10k) contains **10,000 protein multiple-choice questions**, covering 1,910 protein sequences and 25 task types. GPT-6 Luna wrote the questions from UniProt annotations, and a separate Luna call and automated checks reviewed them. These are model-checked labels rather than expert-human labels. Some questions require biological knowledge beyond what can be deduced from the sequence alone.

For this experiment, Flash-Next answered each question twice, once with low reasoning effort and once with xhigh reasoning effort. It did not receive the saved answer key or the source annotations. For each answer, we saved its thinking and final response for training.

We kept every response that finished naturally and had a nonempty final answer, regardless of whether it matched the saved key or the scorer could extract its choice. This left **9,988 low-effort** and **9,880 xhigh** responses. To fill training batches, we repeated 124 and 104 examples respectively. There was no answer-key-based filtering. The two datasets train separate Qwen3.5-4B models using LoRA; each is evaluated on LiveProteinBench after each epoch. Low-effort training is complete; xhigh training is in progress.

<details>
<summary>Context limits, answer parsing, and run settings</summary>

### Current full-context benchmark runs

| Model or checkpoint | Unparsed, including empty | Nonempty but unparsed | Reached context limit |
|---|---:|---:|---:|
| Flash-Next xhigh | 28 | 0 | 27 |
| Original Qwen3.5-4B | 27 | 0 | 26 |
| Low-effort epoch 1 | 29 | 21 | 7 |
| Low-effort epoch 2 | 28 | 25 | 3 |
| Low-effort epoch 3 | 19 | 15 | 4 |
| Low-effort epoch 4 | 39 | 31 | 9 |
| Low-effort epoch 5 | 28 | 23 | 6 |

Unparsed and empty answers count as incorrect in the recorded scores. Some nonempty responses explicitly select an answer that the current parser did not extract, so the starred scores can change after rescoring.

The original 4B and low-effort checkpoints use the same benchmark cases, task instructions, and sampling settings. They use a **262,144-token total context**, with the prompt occupying part of that allowance, on vLLM `0.32.0rc1.dev100+g77154ca61.cu129`. Sampling is temperature 1.0, top-p 0.95, top-k 20, min-p 0, presence penalty 1.5, frequency penalty 0, and repetition penalty 1.0. No per-request seed was supplied; the server's default seed was 0. Flash-Next uses xhigh reasoning and the same sampling values except for a presence penalty of 0. Earlier evaluation; see linked reports used different model and inference settings; their linked reports describe them.

### Training data and length settings

Flash-Next generation used a 262,144-token total context. The low-effort training context is 65,536 tokens and the xhigh training context is 131,072 tokens. No retained training sequence exceeded its respective training context, and none was silently truncated. The training sets include the teacher's thinking and final answer. We compared generated choices with the saved keys for reporting, not selection; the xhigh comparison remains incomplete because the scorer missed many choices.

Both models use veRL supervised fine-tuning, LoRA rank 16 and alpha 32, a training batch of 128, and five epochs. The low-effort set has 10,112 rows after padding; the xhigh set has 9,984.

</details>

## Available response collections

- [GPT-6 Luna questions, answers and visible explanations](LIVEPROTEINBENCH_GPT6_LUNA_EXPLANATIONS.md).
- [Original Qwen3.5-4B responses from the earlier seeded 32K evaluation](qwen35_before_finetuning_liveproteinbench_20261031/README.md).
- [Qwen3.5-4B epoch-5 responses from a separate 32K evaluation](qwen35_epoch5_liveproteinbench_20261031/README.md).

The new full-context runs' per-case responses are retained locally; they are not included in this page.

[Benchmark paper](https://arxiv.org/abs/2512.22257) · [Benchmark repository](https://github.com/Rongdingyi/LiveProteinBench) · [Earlier biology evaluations page](OPENAI_ANTHROPIC_BIO_EVALUATIONS.md)
