# LiveProteinBench model results

Snapshot: November 4, 2026. This page brings together sequence-only LiveProteinBench model results. Test sets and evaluation settings differ between results. Accuracy measures agreement with the benchmark's saved answer. The benchmark paper results use all 1,797 questions; our full-set results cover 1,736 reviewed questions.

## Results

| Model or checkpoint | Accuracy | Setting |
|---|---:|---|
| Our trained Qwen checkpoints | | |
| Qwen3.5-4B, Flash-Next answer-blind low effort | 35.83% | 622/1,736; full context |
| Qwen3.5-4B, Flash-Next answer-blind xhigh effort | 30.24% | 525/1,736; full context |
| Qwen3.5-4B, Flash-Next answer and source shown | 22.41% | 389/1,736; 32K output |
| Qwen3.5-4B, Luna-generated solutions | 23.75% | 57/240; 32K output |
| Base and other models | | |
| [GPT-6 Luna](LIVEPROTEINBENCH_GPT6_LUNA_HIGH32K_RESULT.md) | 65.32% | High reasoning, 32K output |
| [GPT-5](https://arxiv.org/html/2512.22257v1#A4.T5) | 60.49% | Reported by the benchmark paper; reasoning effort not stated |
| [OpenAI o3](https://arxiv.org/html/2512.22257v1#A4.T5) | 56.04% | Reported by the benchmark paper; reasoning effort not stated |
| [Claude 3.7 Sonnet](https://arxiv.org/html/2512.22257v1#A4.T5) | 51.47% | Reported by the benchmark paper; thinking off |
| Qwen3.8-Flash-Next NVFP4 | 48.27% | Xhigh reasoning, full context |
| [Gemini 2.5 Pro](https://arxiv.org/html/2512.22257v1#A4.T5) | 43.85% | Reported by the benchmark paper; reasoning effort not stated |
| [Gemini 2.0 Flash](https://arxiv.org/html/2512.22257v1#A4.T5) | 43.07% | Reported by the benchmark paper; reasoning effort not stated |
| [GPT-4o](https://arxiv.org/html/2512.22257v1#A4.T5) | 38.39% | Reported by the benchmark paper; reasoning effort not stated |
| [Qwen3.8-27B](LIVEPROTEINBENCH_QWEN27B_OWN_OUTPUT_RESULT.md) | 34.56% | Earlier evaluation; see linked report |
| [Qwen2.5-VL-32B](https://arxiv.org/html/2512.22257v1#A4.T5) | 33.05% | Reported by the benchmark paper; reasoning effort not stated |
| Qwen3.5-4B before the new training | 31.16% | Thinking, full context |
| [InternVL3-78B](https://arxiv.org/html/2512.22257v1#A4.T5) | 23.37% | Reported by the benchmark paper; reasoning effort not stated |
| [Qwen3.5-4B-Base](LIVEPROTEINBENCH_QWEN35_4B_BASE_AUTHOR_SAMPLING_V2_RESULT.md) | 13.88% | One sampled response per question; thinking, 16K output; 918 invalid or missing answers |

The trained rows show the best evaluated checkpoint for each approach, selected after observing results. The Luna row uses a smaller 240-question pilot. Evaluation settings and cohorts differ. Final checks on the answer-blind scores remain open. LiveProteinBench has been used for development and is not a fresh blind test.

## How we made the training data

The [original dataset](https://huggingface.co/datasets/jiangdongwei/protein-sequence-reasoning-10k) contains 10,000 protein multiple-choice questions across 1,910 protein sequences and 25 task types. GPT-6 Luna wrote the questions and worked explanations using UniProt annotation context. Separate Luna calls and automated checks reviewed the questions; these are model-checked, not expert-verified, labels. The student was trained on the generated explanations and final answers conditioned on the sequence, question and choices; it did not receive the teacher's source annotations as input. Of the 10,000 training questions, 5,768 belong to 11 task categories with the same names as LiveProteinBench tasks. Another 139 concern temperature dependence, which is related to but distinct from the benchmark's temperature task. The remaining 4,093 questions use other protein-annotation task labels. All training questions use four-choice multiple-choice format; LiveProteinBench evaluates 12 core task categories.

For the later experiments, Flash-Next generated new solutions to these same questions. We tested different information provided to the teacher and different reasoning-effort settings, then fine-tuned separate Qwen3.5-4B models on the resulting solutions.

## Data-generation comparisons

### Answer and source shown versus answer-blind

| Flash-Next solution generation | Teacher sees answer key? | Teacher sees source annotations? | Training examples | Best trained Qwen result |
|---|---|---|---:|---:|
| Answer and source shown | Yes | Yes | 8,356 | 22.41% (389/1,736) |
| Answer-blind, low effort | No | No | 9,988 | 35.83% (622/1,736) |
| Answer-blind, xhigh effort | No | No | 9,880 | 30.24% (525/1,736) |

The source-aware solutions were reviewed before training; the answer-blind runs retained naturally completed nonempty solutions regardless of agreement with the saved answer key. These runs also differ in training data selection, context and evaluation settings, so they do not isolate the effect of showing the answer or source. The source-aware comparison used a 32K output limit; the answer-blind comparisons used a 262,144-token total context.

### Shorter versus longer teacher thinking

Both answer-blind conditions used the same original 10,000 questions, without the answer key or source annotations. The thinking lengths below are measured with the teacher's tokenizer on retained responses; the final answer is excluded.

| Flash-Next effort | Retained solutions | Mean thinking tokens | Median thinking tokens | Best trained Qwen result |
|---|---:|---:|---:|---:|
| Low | 9,988 | 1,621 | 1,053 | 35.83% (622/1,736) |
| Xhigh | 9,880 | 20,788 | 12,793 | 30.24% (525/1,736) |

The low-effort model scored higher in this comparison. Effort settings also change the teacher's instructions, and the retained examples and training context limits differ, so the comparison does not establish that thinking length alone caused the difference.

### Luna-generated versus Flash-Next-generated solutions

| Training solutions | Best trained Qwen result | Evaluation |
|---|---:|---|
| Luna-generated questions and worked explanations | 23.75% (57/240) | Balanced 240-question pilot, 32K output limit |
| Flash-Next, answer-blind low effort | 35.83% (622/1,736) | 1,736 questions, full context |

Luna generated the questions and explanations from annotation context. Flash-Next later produced answer-blind solutions for the same question set. The model, training setup and evaluation cohort differ between the rows, so this is not an isolated comparison of the two teachers.

[Benchmark paper](https://arxiv.org/abs/2512.22257) · [Benchmark repository](https://github.com/Rongdingyi/LiveProteinBench) · [Earlier biology evaluations page](OPENAI_ANTHROPIC_BIO_EVALUATIONS.md)
