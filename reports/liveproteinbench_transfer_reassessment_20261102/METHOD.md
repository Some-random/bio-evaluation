# Method and coverage

## Questions and reviewer visibility

This report contains 1,328 selected questions from the admitted 1,736-question cohort. Selection targeted questions flagged as lookup-dependent or uncertain in an initial screening, rather than a random sample. The other [408 questions](NOT_REASSESSED.md) and the 61 source questions excluded from the admitted cohort are outside this report. Percentages describe this selected subset.

Both reviewers received the same complete question instructions, protein sequence, ordered choices, expected answer and reviewer-only source evidence. They did not receive an evaluated model's response, its correctness, the other reviewer's judgment, or the screening judgments. There is one system message and one user message, with no developer message. [Exact instructions](REVIEWER_PROMPTS.md), [input messages](inputs/), [settings](CONDITIONS.json), [selection](selection.jsonl) and [source credits](THIRD_PARTY_NOTICES.md) are available.

## Meaning of the judgments

Reasoning-supported permits concrete, probabilistic inference using transferable knowledge of related proteins, families, homologs, conserved sequence features, structures, mechanisms, analogies and learned biological patterns. The inference must meaningfully distinguish the actual offered alternatives. It need not be derived from first principles or prove every experimental detail. Lookup-dependent means a particular fact about the exact target protein is necessary and absent from the original inputs. Uncertainty or difficulty alone does not establish lookup dependence.

Expected-answer support is assessed separately against the supplied source evidence. Target-specific facts shown only to reviewers cannot be credited as original benchmark-solving inputs. The exact prompt defines the full criteria.

## Usable and unusable reviews

Each reviewer made one attempt per selected question in the assessment reported here. Only completed outputs satisfying the existing format, supplied evidence-ID, option-ID and input requirements enter scientific-label distributions. Invalid outputs remain visible and are counted separately. No JSON, missing field, citation or empty final is repaired in this presentation update. Private reasoning, headers, credentials and private provider identifiers are not published or substituted for visible answers.

Each model's label counts use its usable reviews: 1,308 for Luna and 1,305 for Qwen. Cross-reviewer scientific comparisons use the 1,287 questions with two usable reviews. The headline five-category table uses all 1,328 questions and includes the 41 incomplete pairs explicitly. An output failure is not a finding that a question or its answer is wrong.

## Execution settings

The assessment shown here ran on November 2, 2026. [CONDITIONS.json](CONDITIONS.json) retains the exact dispatched model and runtime settings. Both reviewers used a combined reasoning-and-final output limit of 16,384 tokens, with an input gate of 49,152 within the project's 65,536-token total ceiling; there were no separate thinking and final limits. These are the settings of the saved reviews, not a claim that a recovery run has completed. There was no prompt truncation.

Qwen used the pinned native chat template with thinking enabled and medium effort; it trims boundary whitespace and adds the assistant `<think>` prefix without an extra natural-language effort instruction. Luna's provider revision, precision, hardware and internal chat formatting are unavailable. Luna's input gate combined a conservative UTF-8 bound with authoritative provider counts for 32 flagged packets; not every input had an exact provider count.

Actual observed token usage and termination counts are in [summary.json](summary.json). Exact Luna total charges are unknown because the returned cache-retention metadata lacks matching documented cache-write billing here. Qwen's local API has no per-request charge; GPU allocation charges are unknown.

## Evidence and interpretation

All source evidence is reused unchanged. Source identity, exact-sequence checks, historical UniSave versions and computational/experimental qualifiers remain on each question page. The exact author database snapshot is unknown. Accession identity came from dataset image-path metadata absent from the original benchmark-solving input. The supplied GO ontology postdates the benchmark, and supplied graph paths use only is_a and part_of. Missing annotation does not establish falsehood. Primary papers were not comprehensively independently adjudicated.

These are AI question reviews with shared source evidence. Agreement is not expert confirmation, proof of contamination, or a causal test of reasoning faithfulness. Contradictions remain review flags rather than accepted replacement answers. This presentation update makes no new scientific judgments and changes no question, key, saved model output or benchmark score.
