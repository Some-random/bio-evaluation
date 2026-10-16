# Public-source preparation update — 16 October 2026

No model inference, judge calls, training or frozen-run changes were made.

| Setting | Progress | Remaining blocker |
|---|---|---|
| LLaVA-Med visual conversation (QA50) | Publisher-verified 193 questions for 50 images, full teacher/context metadata and native judge scripts recovered. 19 original image files recovered, covering 73 questions. | All 50 legacy archive URLs return 404; 31 remaining PMC pages present a browser/reCAPTCHA challenge. Native score also requires the held external GPT-4 judge. |
| Ryze document extraction | Pinned source tree and 5 relevant implementation files restored; publisher commit unchanged. | Exact ArXivQA/SlideVQA/ChartQA component manifests and Table 3 pipeline/answer/scoring contract are unrecovered. Synthetic fallback rows are invalid benchmark data. |
| NatureLM temporal protein descriptions | Pinned source tree and 3 NatureLM files restored; publisher commit unchanged. | Exact temporal case list, sequence/reference snapshots, cutoff and ROUGE-L preprocessing remain unavailable in inspected release. |

LLaVA-Med's 193 questions comprise 143 conversation and 50 detailed-description prompts. The input-only question export contains only question ID, source image ID, image filename and original question text. Teacher answers, captions and inline mentions remain in the original scorer-side source files. The recovered images match each original article ID and exact source image filename; their current bytes are hashed, but no historical publisher image digest is available. Image acquisition stopped at the access challenge.

The native LLaVA-Med scorer asks GPT-4-0314 to grade the teacher answer and candidate answer with caption/inline context. Its relative score is the mean of per-question candidate/teacher score ratios, multiplied by 100. A substitute judge would change the evaluation. Qwen vision compatibility alone does not remove this external-evaluator blocker.

`audit.json` records exact counts, source pins, blockers and validation; `source_manifest.json` records source URLs and SHA-256 checks. `v06_image_recovery.json` records image provenance and acquisition failures. The source bundle excludes article HTML/browser-challenge responses and contains no credentials or weights.

Sources: [official LLaVA-Med evaluation](https://github.com/microsoft/LLaVA-Med/blob/30697ca50b5c29a8e955c99330b259776aef27b9/README.md#evaluation), [judge](https://github.com/microsoft/LLaVA-Med/blob/30697ca50b5c29a8e955c99330b259776aef27b9/llava/eval/eval_multimodal_chat_gpt_score.py), [native aggregation](https://github.com/microsoft/LLaVA-Med/blob/30697ca50b5c29a8e955c99330b259776aef27b9/llava/eval/summarize_gpt_review.py), [Ryze source](https://github.com/Chivier/Ryze/tree/41b2d77ec0651b9f51b657f524415ee3cc38e115), [NatureLM source](https://github.com/microsoft/SFM/tree/bcb1351bc6490d4a98cae74e7eead30a028fae00/NatureLM).

The [reproducible handoff](../handoff/source_preparation_2026-10-16/README.md) contains source-acquisition scripts and provenance manifests. Raw inputs and images remain in the local source bundle for a private release.
