# Method and limits

The review covers the frozen cohort of 1,736 admitted, sequence-only LiveProteinBench questions. The 61 earlier exclusions were not regenerated or restored. Each review received the full original system instructions, full question sequence and ordered choices, author expected answer, and explicitly reviewer-only source evidence. No evaluated model response, correctness result, or another reviewer’s judgment was provided.

GPT-6 Luna independently assessed (1) whether the author key was supported, contradicted, or unresolved by the supplied evidence and (2) whether general biological reasoning could meaningfully distinguish the choices, or selection depended on a protein-specific external fact. Recognizing an exact sequence and remembering its database annotation did not count as reasoning. Exact logical reviewer instructions are in [REVIEWER_PROMPTS.md](REVIEWER_PROMPTS.md).

The review used the Responses API with medium reasoning effort and a 16,384 total output-token limit, including internal reasoning. These pages publish only the saved visible review fields. The provider’s internal reasoning, API response identifiers, headers, credentials, safety identifiers, and local runtime metadata are not part of this report. There were no automatic model retries. The one citation-invalid result was not rerun or converted into a valid review.

## Reading the results

- **Expected-answer support:** `supported`, `contradicted`, or `uncertain` (the saved `cannot_determine`). These are model judgments about the key, not independently confirmed scientific truth.
- **Reasoning / lookup:** `reasoning-supported`, `lookup-dependent` (the saved `lookup_or_memorization_dependent`), or `uncertain`. Predictive difficulty alone does not establish a missing item-specific fact. A source annotation can support a key while the question still depends on lookup.
- **Invalid citation:** the saved labels and all visible reasons remain available, but that record is excluded from the 1,735 format-valid totals. `source_applicability` was a metadata object, not an assigned evidence ID.

Original author keys and original benchmark scores are unchanged. These are AI reviews and AI-assisted project source checks, not independent expert adjudication. The 31 `contradicted` labels are flags for further scientific assessment, not 31 confirmed key errors. No Qwen question reviews are available, and no cross-model comparison is claimed.

## Source evidence and applicability

Official UniProtKB records and UniSave archives were checked for all 635 accession identities. The accession was recovered from dataset image-path metadata and was absent from the original evaluated model input. All 1,736 supplied question sequences match the selected archived records released no later than 2026-05-07. That cutoff approximates the pinned source repository date; the authors’ actual data-construction date and exact database snapshot remain unknown.

Current UniProt sequences match 1,730 questions. Four G2X0L1 questions have a newer, differing current sequence; their matching historical record is retained. Current Q5AV79 retrieval was unavailable for two questions after recorded server failures; their matching historical evidence is retained. These source differences are explicitly visible on the relevant pages.

Annotations can reflect experiments, computational inference, or transfer by similarity. Evidence codes and qualifiers remain in the cited excerpts. Primary papers were not comprehensively retrieved or independently assessed. Selected source excerpts can omit relevant facts, and absence of an annotation does not establish falsehood. Current Gene Ontology data are from release 2026-07-26, newer than the benchmark repository date; the exact historical ontology is unknown. Supplied ontology paths use only `is_a` and `part_of` edges, retaining obsolete-term qualifications.

## Project source checks

All 31 Luna contradicted-key claims were traced to supplied sources, and all 1,735 format-valid reviews passed structured citation-membership checks. Those checks do not constitute complete semantic validation of every argument or citation. Case pages include all 44 project source-check notes and the separate invalid-citation note, without changing saved model verdicts or author keys.

Some checks found mistakes in reviewer premises: residue assertions in `active_site_0032` and `active_site_0106`, and a four-residue assertion in `transmembrane_0107`. Other notes qualify nested GO terms, close coordinate alternatives, competing annotations, or uncertainty that does not prove multiple actual activities. The source note and remaining uncertainty sit alongside the unchanged visible review.

## Public export

Each case page includes the complete original user question, optional original system instructions, author key, all saved visible review fields, source qualifications, project notes, and the official excerpts cited by the review or notes. Question text and keyed option text are reproduced unchanged; Markdown presentation is added. Annotation excerpts are selected from the exact cached source objects or literal source lines and retain source URLs, locators, versions where available, and hashes.

The CSV is a compact label index. The JSONL contains only allowlisted question, visible-review, source, and project-note fields. The provenance and file manifest bind the public export to frozen inputs without exposing local paths. No model weights, full source cache, private API traces, or original evaluated model responses are included. Credits and source licenses are in [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).
