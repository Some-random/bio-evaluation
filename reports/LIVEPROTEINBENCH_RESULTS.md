# LiveProteinBench model results

| Model or training approach | Training examples | Teacher | Accuracy |
|---|---:|---|---:|
| **Our trained Qwen3.5-4B** | | |  |
| Original questions | 10,000 | GPT-6-Luna | 33.32% |
| Original questions | 10,000 | Flash-Next, xhigh | 36.32% |
| Original questions | 10,000 | Flash-Next, low | 39.63% |
| Skill-guided: 5,000 standard + 5,000 skill-guided questions | 10,000 | Flash-Next, low | 42.53% |
| Scaled questions | 124,000 | Flash-Next, low | 45.83% |
| **Off-the-shelf models: our evaluations** | | |  |
| Qwen3.5-4B (student) | | | 32.62% |
| Qwen3.8 Flash-Next, low (teacher) | | | 51.14% |
| Qwen3.8 Flash-Next, xhigh (teacher) | | | 50.96% |
| Qwen3.8-27B, thinking off | | | 35.84% |
| GPT-6 Luna, high | | | 68.28% |
| **Other models: reported by the benchmark paper** | | |  |
| [GPT-5](https://arxiv.org/html/2512.22257v1#A4.T5) | | | 60.49% |
| [OpenAI o3](https://arxiv.org/html/2512.22257v1#A4.T5) | | | 56.04% |
| [Claude 3.7 Sonnet, thinking off](https://arxiv.org/html/2512.22257v1#A4.T5) | | | 51.47% |
| [Gemini 2.5 Pro](https://arxiv.org/html/2512.22257v1#A4.T5) | | | 43.85% |
| [Gemini 2.0 Flash](https://arxiv.org/html/2512.22257v1#A4.T5) | | | 43.07% |
| [GPT-4o](https://arxiv.org/html/2512.22257v1#A4.T5) | | | 38.39% |
| [Qwen2.5-VL-32B](https://arxiv.org/html/2512.22257v1#A4.T5) | | | 33.05% |
| [InternVL3-78B](https://arxiv.org/html/2512.22257v1#A4.T5) | | | 23.37% |

## Next steps

- **Apply skill-guided training on scaled questions** Keep the same amount of total QA pairs and see if skill-guided QA training also helps for larger scales
- **Inject more biological knowledge** Generate (synthetic) documents from our existing resources (PMC papers, the bio collection, FineWeb-Edu) for mid-training or post-training. Maybe try something like [Synthetic Mixed Training](https://arxiv.org/abs/2603.23562)?
- **A random thought** Code is heavily used in language model training and seems to be generalize across reasoning domains. Could we do something similar for biological reasoning?
