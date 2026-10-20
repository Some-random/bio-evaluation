# Follow-up recovery of evaluation inputs and tools

Snapshot: 2026-10-19T20:06:35.472075-07:00 (America/Los_Angeles).

The initial bulk transfers were not the end of source recovery. This follow-up checked author histories, supplements, public original-image copies and tool dependencies. No new benchmark inference, training or model forwards were run.

| Area | Additional recovery | Exact remaining limit |
|---|---|---|
| PFArena | Authenticated official dataset: 772/772 publisher-verified files (1825005675 bytes), plus 247 verified source/history artifacts. User-enabled access resolved the former 401 prerequisite. | Dataset availability is resolved. Native preparation/input review and strict scorer coverage remain necessary; the default lenient evaluator fabricates missing-assay substitutes and must not be used for reported scores. |
| SlideVQA | Processed 1024px same-deck/page copies: 300/300. Additionally, 7 original-name native-resolution academic copies, 40 current deck renderings and 9 academic alternate renderings are separately archived. | The processed corpus re-encodes images: 0/860 available overlaps were byte/pixel-identical. All seven independent native-resolution copies matched the correct processed page in the identity check. This closes missing page availability, while exact historical image encoding remains unresolved. |
| NatureLM / SFM | Complete paper/supplement sources, official daily PDF, all 30 property prompts, 20 historical author revisions and a published SciReasoner reproduction with data/evaluator code recovered. | Exact binary target mapping, absolute temporal cohort, fine-tuned property heads and 1,000-reference IDs remain unlocated. The reproduction's threshold/wiring do not establish the native mapping; its 99% clustering differs from the paper's 50% condition. |
| Proteo-R1 / MEAN tools | Complete pinned repository archives verified against 173 and 73 Git blobs; pinned Protenix submodule acquired; 83 fixture/helper/evaluator files materialized. All five official demo fixture sets pass presence and NPZ CRC checks. Vendor files verified: 5/5. | Five public demo cases are not the full paper holdout. Model execution and native full-cohort identity remain separate work. |
| RAbD / P40 | Recovered the current official SAbDab2 structures for the exact 60-entry roster, plus a publisher-verified 60-reference PDB bundle from AAMFM. Released IMGT numbering code defines deterministic CDR-H3 masks. Validation stage: source_recovery_terminal_native_identity_qualifications_preserved. | 57 current official structures have straightforward legacy-chain compatibility; three scFv entries split older chain identities. AAMFM uses cropped inputs and changes 15 original chain contracts. Neither bundle is silently substituted for exact historical MEAN inputs. |
| Ryze / V07 | 26 additional artifacts and 32 reverified author code files; complete histories and released mapping inventories checked. An isolated, synthetic-tested preparation patch preserves all questions sharing a figure instead of overwriting 45,601 mappings. | Released entrypoints differ in image-plus-OCR versus OCR-only input, decoding and system labels. No certified ChartQA implementation, original Table 3 cohort or aggregation records were located. The patch does not change original source or benchmark outputs. |

## Current tool transfer

Stage: acquisition_terminal. Verified range bytes: 12797417932 / 12797417932. Sparse file size is never counted as transferred or verified data. Final file SHA256 and publisher SHA256 or multipart ETag checks are recorded separately.

## Precise paper-protocol gaps

NatureLM/SFM recovery includes 75 HTTP artifacts (22,776,793 bytes), the 30 official property prompts and the published reproduction. The reproduction supplies a numerical threshold but wires a different evaluator cascade and uses 99% rather than the paper's 50% clustering. Its code cannot certify the native binary mapping, temporal cohort or property-head contract. These are specific unresolved artifacts, rather than a claim that useful source code is unavailable.

Ryze's released mapping inventories cover 100,000 ArxivQA questions over 54,399 figures and 2,215 SlideVQA questions over 400 decks. They identify released inputs, not the exact membership of the Table 3 runs. A single binary outcome over all 2,215 SlideVQA cases cannot reproduce two reported percentages under ordinary rounding; another cohort or aggregation could explain them. No paper-error claim follows. The recovered protocol receipt records the differing entrypoints, absent ChartQA implementation and missing original execution records.

The ArxivQA fanout patch is frozen separately with synthetic checks for shared-image questions, existing outputs and dry-run behavior. It is a preparation correction, not a new score. Source recovery alone does not authorize benchmark dispatch.

[Preparation patch](../scripts/source_preparation/ryze_arxiv_fanout_20261019.patch) · [Synthetic patch-check receipt](SOURCE_PREPARATION_REPAIR_2026-10-19.json). Seven additional local transport tests cover exact ranges, response lengths, corruption detection and completed-file reuse; they made no network or model calls.

## Offline input preflight begun at 8 PM PDT

These are newly timestamped checks from the 8 PM update, not evidence of intervening background evaluation between 6 and 8 PM. No inference, scoring or protocol adoption occurred.

PFArena: T1 123, T2 74, T3 67, T4 29 = 293 task tables, with all pinned target paths present and nonempty and all 29 T4 context pairs available. These are file/table counts, not model calls or benchmark cases. Ten source files pass syntax checks. Input/reference isolation, a frozen case-scoped configuration and runtime/delivery checks remain unfinished.

The direct LLM branch does not inherently require PLM or AlphaFold calls. The native strict scorer checks assay coverage and minimum top-k counts, but does not enforce a complete candidate permutation; missing ranking tails are assigned deterministic ranks. Strict scoring alone must not be described as full answer delivery. Native formulas remain unchanged, and no actual prediction coverage or score effect has been assessed.

SlideVQA: verified 44300 ordered case-to-page links across 8000 page identities and 400 decks. An explicitly prospective condition using 7,700 originals plus 300 processed copies covers 2215/2215 questions with all 20 images, compared with 2,125 using only the first acquisition. Missing, duplicate, foreign and reordered page references are zero. This establishes input availability for that distinct encoding condition; it has not been adopted or dispatched and does not establish the paper's exact Ryze recipe.

## Source and publication boundaries

Original acquisition receipts and frozen Qwen outputs are preserved. Image archives, restricted SlideVQA material, raw reproduction data, source files with unreviewed credential-like comments and model weights stay local. This page exports aggregate counts and provenance only.

[Initial acquisition](SOURCE_ACQUISITION_PROGRESS_2026-10-19.md) · [Official PFArena](https://github.com/AMix-Bio/PFArena) · [Proteo-R1](https://github.com/smiles724/Proteo-R1) · [MEAN](https://github.com/THUNLP-MT/MEAN) · [NatureLM resources](https://github.com/NatureLM/Resources) · [Ryze-Data](https://github.com/Chivier/Ryze-Data)

Live aggregate receipts feed the existing two-hour progress schedule. A completed source search is not a completed benchmark score.
