# LABBench2 BASIC542 — Qwen3.8-27B and GPT-6 Luna

Accuracy under the fixed local Qwen3.8-27B judge, using the same 542 reviewed native question-only inputs. The selected categories contain 620 source cases; 78 remain excluded. No retrieval, tools or images were added.

| Solver | Accuracy | Invalid solver outputs |
|---|---:|---:|
| Qwen3.8-27B | 8.30% (45/542) | 313 |
| GPT-6 Luna | 17.53% (95/542) | 0 |

Qwen3.8-27B uses the pinned BF16 checkpoint, its native chat template, thinking enabled and a 16,384-token output budget. GPT-6 Luna uses high reasoning effort and the same 16,384-token output cap. Their weights, serving systems and decoding differ.

Qwen generation preserved eight attempts from the original worker and assigned the remaining 534 cases once across seven disjoint replicas. The replicas retained the same checkpoint, native prompts, precision, sampling settings, output cap and batch size of four. Six earlier replica allocations failed before any model call and are recorded as startup history.

Both complete solver cohorts were sealed before reference access. The judge uses the unchanged native category rubrics and binary score mapping, thinking disabled, temperature 0 and 2,048 output tokens. It replaces the author’s Claude Sonnet 4.5 judge; Qwen’s result additionally uses the same model family for solving and judging. These are declared evaluation conditions, not a paper-equivalent judge or proof of explanation quality.

Invalid or truncated solver/judge outputs remain in the full denominator and receive zero credit. Public files contain numerical outcomes and opaque provenance only; questions, reference answers, free-form outputs, reasoning and private API metadata are omitted.

[Official source](https://github.com/EdisonScientific/labbench2/tree/a490cd40379edd603fb8b6b6d3fe47ebb0712e8d) · [Pinned dataset](https://huggingface.co/datasets/EdisonScientific/labbench2/tree/3678e7e38748477d0606407468db9cd7e2f2e667) · [Paper](https://arxiv.org/html/2604.09554v2). Source attribution: Edison Scientific, LABBench2 (CC-BY-SA-4.0 metadata).
