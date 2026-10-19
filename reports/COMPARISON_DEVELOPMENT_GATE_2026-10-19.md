# Comparison delivery checks: independent development inputs

Prepared October 19, 2026, Pacific time. **The 4,096-token budget is a candidate condition; it has not yet been validated on these tasks for either OpenAI model.** This preparation made zero inference calls.

The initial check now has concrete independent inputs: twelve newly authored biology multiple-choice questions and twelve authentic protein-localization validation sequences. Model requests and authoring/scoring references are separate files. These inputs do not replace or modify the 279 LitQA2/SuppQA benchmark cases or the 2,773 P03 test cases.

| Check | Prepared inputs | What they cover | Current result |
|---|---:|---|---|
| LitQA2-like closed-book biology QA | 6 new questions | GFP maturation, ER retention, RNA interference, protein translocation, water-channel function, and autophagosome formation | Prepared; no model outputs |
| SuppQA-like closed-book paper-specific QA | 6 new questions | The same six primary papers; paper title and DOI supplied, with a different paper-specific question and fixed choices | Prepared; no model outputs |
| P03 localization | 12 official validation sequences | Complete published sequences from 40 through 1,000 residues; unchanged ten-class prompt and class IDs | Prepared; no model outputs |

The text questions use the exact archived LAB-Bench multiple-choice scaffold, including its instruction to think step by step, a single `[ANSWER]` letter, and an explicit insufficient-information option. They do not supply a paper, supplement, answer-bearing passage, reference explanation, or prior model output. They are newly authored development questions, **not official LAB-Bench examples**. In particular, the SuppQA-like panel uses facts from the named main papers; it does not demonstrate supplementary-material reading.

## Why the public LAB-Bench rows are not the development set

At the pinned release, the 199 LitQA2 and 82 SuppQA rows are stored in partitions named `train`, but the publisher identifies the release as an evaluation dataset. Those rows overlap the proposed comparison cohort; they cannot be relabeled as independent development examples. No separate official development partition was verified in that release. [Pinned dataset card](https://huggingface.co/datasets/futurehouse/lab-bench/blob/5c77cec648430f30611808808861eb86f81d5eaa/README.md).

The new question IDs and normalized question texts are disjoint from all 279 frozen benchmark requests. None of the six source-paper DOIs occurs in those benchmark prompts. A recorded nearest-text check has a maximum normalized sequence-match ratio of 0.457; this is an overlap diagnostic, not proof of semantic novelty or absence from model training.

These are classic cell-biology questions with deliberately checked answer semantics. Their prompts contain approximately 983–1,277 characters, compared with 638–1,356 across the selected benchmark prompts. The panel covers actual scientific content rather than repeated neutral padding, but twelve questions do not reproduce the benchmark's entire topic or difficulty distribution.

## Protein validation provenance and coverage

P03 uses the **validation** LMDB inside the same official source archive that supplied the frozen test condition. Its archive SHA-256 is `8c3cf116b7e82779a7cd6b280cf50d8d69d826ef88667ed3a29fda5751184a66`; its MD5 also matches the official dataset loader. That loader names distinct train, valid, and test partitions. [Official loader](https://torchdrug.ai/docs/_modules/torchdrug/datasets/subcellular_localization.html).

The actual pinned validation LMDB contains 2,811 records; source-code documentation displays different summary counts, so this preparation records the observed archive count explicitly. Twelve cases were chosen by evenly spaced sequence-length ranks, with original index breaking ties. Selection uses neither localization labels nor model correctness. All selected sequences are disjoint from the frozen test cohort by exact sequence hash.

Selected sequence lengths are **40, 125, 197, 261, 323, 380, 447, 522, 617, 754, 1,000, and 1,000 residues**. The test input range is also 40–1,000. The sequence-plus-ontology scaffold is unchanged; only the sequence is replaced with its validation counterpart. Every request retains the entire sequence present in the published record.

Source records are decoded in the preparation process and contain labels, but the generator neither uses those labels for selection nor exports them to requests. The eventual dispatcher should receive only the frozen model payloads and minimal execution ledger. Biological correctness is not part of this P03 delivery check.

## Requirements before benchmark inference

Run the candidate 4,096-token, medium-reasoning condition separately for each named model under the reviewed comparison authorization. Preserve every request, output, refusal, error, truncation, token count, and latency. Verify the actual outbound hashes and fresh, single-user contexts through the isolated dispatcher.

For text QA, check native parsing and separately require a single unambiguous in-range answer-tag value. Selecting the insufficient-information option is valid delivery, not evidence of a substantive or correct answer. For P03, check the frozen integer-class parser and require one unambiguous ID from 0 through 9.

**Do not mark the budget ready from preparation or synthetic checks.** Inspect the complete development results first and freeze the budget, ambiguity rule, and residual-failure policy before held-out correctness is examined. Any failed delivery remains visible. A revised budget or prompt becomes a newly named condition; it cannot selectively replace failed benchmark outputs. Even twelve successful development answers would be an initial check, not a guarantee for every benchmark case.

The earlier simple synthetic checks and the unrelated real-GFP pilot do not establish readiness for these QA/localization tasks. This record does not claim a provider response, lift flagged-task holds, or itself authorize dispatch.

## Primary sources for the new questions

- [Heim, Prasher and Tsien: GFP maturation and spectral variants](https://pubmed.ncbi.nlm.nih.gov/7809066/).
- [Munro and Pelham: a terminal signal for ER residence](https://www.sciencedirect.com/science/article/pii/0092867487900869).
- [Montgomery, Xu and Fire: post-transcriptional RNA interference](https://pubmed.ncbi.nlm.nih.gov/9860998/).
- [Blobel and Dobberstein: heterologous rough-microsome reconstitution](https://rupress.org/jcb/article-abstract/67/3/852/48431/Transfer-of-proteins-across-membranes-II).
- [Preston and colleagues: CHIP28 water-channel activity](https://pubmed.ncbi.nlm.nih.gov/1373524/).
- [Mizushima and colleagues: Apg5 and autophagosome formation](https://pubmed.ncbi.nlm.nih.gov/11266458/).

The [readiness record](COMPARISON_DEVELOPMENT_GATE_2026-10-19.json) gives request-file hashes, source pins, case-selection evidence and remaining checks. No development score or biological-capability claim is reported.
