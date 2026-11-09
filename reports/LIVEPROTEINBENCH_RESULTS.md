# LiveProteinBench model results

| Model or training approach | Training examples (rounded) | Teacher | Reviewer-adjusted accuracy | Paper-reported accuracy |
|---|---:|---|---:|---:|
| **Our trained Qwen3.5-4B** | | | | |
| Scaled questions | 124,000 | Qwen3.8 Flash-Next, low | 42.83% | |
| Original questions | 10,000 | Qwen3.8 Flash-Next, low | 37.63% | |
| Original questions | 10,000 | Qwen3.8 Flash-Next, xhigh | 32.32% | |
| Skill-guided: 5,000 standard + 5,000 skill-guided questions | 10,000 | Qwen3.8 Flash-Next, low | | |
| **Other models: our evaluations** | | | | |
| [GPT-6 Luna, high](LIVEPROTEINBENCH_GPT6_LUNA_HIGH32K_RESULT.md) | | | 68.28% | |
| Qwen3.8 Flash-Next, xhigh | | | 50.96% | |
| Qwen3.8 Flash-Next, low | | | | |
| [Qwen3.8-27B, thinking off](LIVEPROTEINBENCH_QWEN27B_OWN_OUTPUT_RESULT.md) | | | 35.84% | |
| Qwen3.5-4B | | | 32.62% | |
| **Other models: reported by the benchmark paper** | | | | |
| [GPT-5](https://arxiv.org/html/2512.22257v1#A4.T5) | | | | 60.49% |
| [OpenAI o3](https://arxiv.org/html/2512.22257v1#A4.T5) | | | | 56.04% |
| [Claude 3.7 Sonnet, thinking off](https://arxiv.org/html/2512.22257v1#A4.T5) | | | | 51.47% |
| [Gemini 2.5 Pro](https://arxiv.org/html/2512.22257v1#A4.T5) | | | | 43.85% |
| [Gemini 2.0 Flash](https://arxiv.org/html/2512.22257v1#A4.T5) | | | | 43.07% |
| [GPT-4o](https://arxiv.org/html/2512.22257v1#A4.T5) | | | | 38.39% |
| [Qwen2.5-VL-32B](https://arxiv.org/html/2512.22257v1#A4.T5) | | | | 33.05% |
| [InternVL3-78B](https://arxiv.org/html/2512.22257v1#A4.T5) | | | | 23.37% |

## Future work

- Generate synthetic questions and paragraphs for biological reasoning.
- Develop question- and answer-informed synthetic documents for post-training and mid-training, inspired by [Synthetic Mixed Training](https://arxiv.org/abs/2603.23562).
- Explore whether code-based training data can improve biological reasoning.
