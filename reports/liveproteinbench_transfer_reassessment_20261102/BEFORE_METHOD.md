# Method and limits

## Frozen cohort and separate judgments

This report covers all 1,736 original admitted sequence-only LiveProteinBench questions; 61 earlier exclusions remain excluded. Both reviewers received the same logical system message and rendered user message from the same frozen packet set: complete original question instructions, complete sequence and ordered choices, author expected answer, and explicitly reviewer-only evidence. Original task instructions and sources were quoted data. No original evaluated model response, correctness outcome, or other reviewer’s judgment was supplied. The reviews assess author-key support and reasoning-versus-lookup dependence. Original benchmark generation and reasoning faithfulness are not evaluated here.

The author key is a claim to assess, not guaranteed truth. Recognizing an exact sequence and recalling its database entry does not count as reasoning-supported. Source annotation support can support a key while selection still depends on a missing protein-specific fact. Model judgments and agreement are not independent scientific truth or expert adjudication. No consensus label, changed key, rescore, or new model-based scientific review was created.

## Reviewer conditions

| Setting | GPT-6 Luna | Qwen3.8-Flash-Next-NVFP4 |
|---|---|---|
| Model | `gpt-6-luna`, Responses API | `nvidia/Qwen3.8-Flash-Next-NVFP4`, revision `fc694b54fb0174e0913e6adf86691ef85a4ead47` |
| Precision / resources | Provider precision, hardware and exact revision undisclosed | Published NVFP4 weights / BF16 compute, TP2 on two A100 GPUs |
| Reasoning | Medium | Native thinking, explicit medium effort |
| Total output-token cap | 16,384 including internal reasoning | 16,384 including native thinking |
| Sampling | Sampling/seed/penalty options omitted | Temperature 0.6; top-p 0.95; top-k 20; min-p 0; presence/frequency penalties 0; repetition penalty 1; seed 42 |
| Maximum client concurrency | 128 | 128 |
| Input ceiling | 49,152 tokens | 49,152 tokens; 65,536 total context |

The logical messages/evidence packets match. The Qwen native chat-template markers and undisclosed API formatting differ, so wire prompts and sampling are not claimed identical or matched. The existing authorized runs were reused. No new generation, download, retry, or scientific model review was performed to build this report. A separate arithmetic startup control is outside the 1,736-question cohort.

## Validity, invalids, and aggregation

Each page and the JSONL preserve both actual saved statuses, complete parsed visible reviews, and exact saved visible final text. Invalid parsed JSON nulls, wrong option-ID values, nonexistent citations, and missing visible finals remain explicit. Missing fields are not filled; invalid labels are not salvaged into a usable review. Internal `reasoning` / `reasoning_content` provider fields are never used as a replacement final review and are not published. Raw provider records, response IDs, headers, identity metadata, local paths, credentials and server addresses are excluded by content allowlists.

Each model’s label distribution uses only that model’s format-valid reviews, with its own denominator shown. Cross-tabs, agreement on key support, agreement on reasoning/lookup, both-axes agreement, and labels assigned by both models use only jointly valid pairs. All 1,736 question rows remain visible; invalid/missing cases are not recoded as uncertain and are excluded from paired statistics. “Uncertain” displays the saved `cannot_determine`; “lookup-dependent” displays `lookup_or_memorization_dependent`.

## Sources and project notes

Official records were checked for all 635 accession identities, recovered from dataset image-path metadata that was absent from the original evaluated question. All 1,736 sequences match selected historical UniSave records released by 2026-05-07, approximating the pinned source repository date. The exact author data-construction date and source snapshot remain unknown. Current records match 1,730 question sequences; four G2X0L1 questions differ from the newer current sequence, and current Q5AV79 retrieval was unavailable for two questions. Matching historical records remain available for all of them.

Both reviewers could see experimental, computational and similarity-based annotations, with evidence qualifiers retained. Primary papers were not comprehensively independently assessed. Missing selected annotations do not prove falsehood. GO data are from release 2026-07-26, newer than the benchmark; exact historical ontology is unknown. Supplied graph paths use only `is_a` and `part_of`.

The existing 44 project source-check notes plus the separate invalid-citation note were prepared for Luna claims; they are reproduced without changing verdicts and are explicitly not new validation of Qwen claims. All 31 Luna contradicted-key claims were traced to supplied sources, but are not 31 confirmed key errors. Notes identify incorrect residue premises in some Luna arguments, competing annotations, ambiguity qualifications and remaining uncertainty. No additional semantic adjudication was added for this comparison.

## Public export and provenance

The complete original question text and keys are unchanged. Markdown presentation escapes chemical brackets to preserve literal answer text. Case pages retain both complete visible reviews and cited official excerpts; the JSONL retains exact saved visible final-text strings and parsed objects separately. Source credits and licenses are preserved in THIRD_PARTY_NOTICES.md. No full source cache, downloaded weights, raw API metadata or private model reasoning is redistributed. A final export is frozen only after the client owner verifies the exact terminal 1,736-case execution scope. The earlier published Luna-only report remains unchanged.
