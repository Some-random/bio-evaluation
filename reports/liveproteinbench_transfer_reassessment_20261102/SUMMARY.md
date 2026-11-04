# LiveProteinBench question-review results

**Scope: 1,328 selected questions.** Percentages below use all 1,328 questions.

| Assessment | Questions | Share of 1,328 |
|---|---:|---:|
| Both reviewers: reasoning-supported | 969 | 72.97% |
| One reasoning-supported, one lookup-dependent | 217 | 16.34% |
| Both reviewers: lookup-dependent | 87 | 6.55% |
| At least one uncertain; both reviews usable | 14 | 1.05% |
| One or both reviews unusable | 41 | 3.09% |

The reviewers supplied usable judgments for **1,287 questions**. The 41 incomplete pairs contain 43 unusable reviewer outputs; two questions have failures from both reviewers.

## Each reviewer

| Reviewer | Reasoning-supported | Lookup-dependent | Uncertain | Unusable |
|---|---:|---:|---:|---:|
| GPT-6 Luna | 999 | 294 | 15 | 20 |
| Qwen3.8-Flash-Next-NVFP4 | 1201 | 104 | 0 | 23 |

Scientific-label counts include only usable reviews: 1,308 for Luna and 1,305 for Qwen. An unusable review does not establish that the question or expected answer is wrong.

## Agreement between reviewers

Rows are Luna judgments; columns are Qwen judgments. This table includes only the 1,287 questions with two usable reviews.

| Luna / Qwen | Reasoning-supported | Lookup-dependent | Uncertain |
|---|---:|---:|---:|
| Reasoning-supported | 969 | 14 | 0 |
| Lookup-dependent | 203 | 87 | 0 |
| Uncertain | 11 | 3 | 0 |

## Support for the expected answer

| Assessment | Questions |
|---|---:|
| Both reviewers support the key | 1234 |
| Both reviewers flag a contradiction | 12 |
| Other disagreement or unresolved evidence, both reviews usable | 41 |
| One or both reviews unusable | 41 |

Expected-answer support and reasoning-versus-lookup dependence are separate judgments. Reviewer agreement does not independently establish biological truth. Full status, visible text and evidence are available on every question page and in [reviews.jsonl](reviews.jsonl).

[Browse questions](README.md) · [Method and limitations](METHOD.md)
