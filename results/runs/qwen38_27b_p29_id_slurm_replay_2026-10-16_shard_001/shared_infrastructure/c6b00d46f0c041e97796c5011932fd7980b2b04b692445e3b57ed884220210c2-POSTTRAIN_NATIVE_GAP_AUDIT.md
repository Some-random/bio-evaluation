# Bio-posttrain native gap audit, 15 October2026

P29 now has exact released ID/OOD inputs and a qualified prospective Qwen baseline. N04 and N05 remain blocked by specific source artifacts. No inference, training, author contact, central authorization or queue change was performed in this audit. P28 and other frozen files remain unchanged.

The pinned author repository is [mims-harvard/bio-posttrain@03c872d](https://github.com/mims-harvard/bio-posttrain/tree/03c872d3a1f38993f98786f774beb738df55a7be). Downloads, verified Git blob/SHA256 manifests and unauthenticated release-link responses are in `sources/posttrain_gap_audit_2026-10-15/`. The structured record is `reports/posttrain_native_gap_audit.json`.

## P29 exact species ID/OOD release

The original author `data/download.sh` links a [public protein folder](https://drive.google.com/drive/folders/1Frm1o4zzFOpnA8n8GdJieYAt57poLpxk). Both original CSVs were downloaded without authentication and match the folder-advertised byte sizes; their contents are locally frozen by SHA256. Drive advertises no immutable publisher content hash, so a publisher-certified SHA256 is not claimed.

| Native artifact | Cases | Bytes | SHA256 |
|---|---:|---:|---|
| id-test.csv | 6,989 | 84,155,171 | 22ac86ba5007958cca20c67b578ecc30d5a0b1ff8acc90b5a7337888a93229b9 |
| ood-test.csv | 7,883 | 81,784,045 | 33eea7afc2e7656907aa4820926e5e8c8cd32c799bfae24b121a18d9f8b5d2d4 |

OOD contains4,084 *Schizosaccharomyces pombe* and3,799 *Trypanosoma brucei brucei*. Protein IDs are unique within each file and disjoint between ID/OOD. Native author file membership is preserved; the1.16GB training CSV was not needed/downloaded for zero-shot inference, so independent reconstruction of the holdout against training is not claimed. P28 temporal IDs are never substituted.

The prospective prompt follows the separate [released RL evaluator](https://github.com/mims-harvard/bio-posttrain/blob/03c872d3a1f38993f98786f774beb738df55a7be/BioReason-Pro/train_protein_grpo.py), with full sequence, organism, full InterPro text, `go_pred` predictions, all3 aspects and exact summary-tag instruction. PPI is disabled by that native launcher. The source's optional singular `protein_name` is absent from both CSVs; plural answer-bearing `protein_names` is never substituted. Gold annotations, names, teacher reasoning and final answers remain scorer-only. Sequences are complete: ID11–26,931residues, OOD25–8,214. Conservative complete-prompt context bounds, including controls and4096output tokens, are36,042 ID/19,728 OOD, below262,144.

The native [GO reward code](https://github.com/mims-harvard/bio-posttrain/blob/03c872d3a1f38993f98786f774beb738df55a7be/BioReason-Pro/bioreason2/utils/go_reward.py) prefers GO-summary blocks, then aspect blocks, then a final-answer heuristic. It propagates `is_a`/`part_of` using the original January2023ontology, retains native roots/unknown-ID self terms, and averages per-protein set precision/recall/F1 with uniform weights. This is not P28 CAFA Fmax/IA-weighted Fmax. Every planned failed/missing/no-GO output contributes an empty prediction set. Only generated continuation channels are parsed; prompt or predictor context is never concatenated to model outputs.

**Material input/reference dependence:** native `resolve_gold_terms_from_row` unions `go_pred_leaf` into the target alongside curated annotations while `go_pred` is supplied to the model. This augments6,212/7,883OOD and4,785/6,989ID targets beyond curated terms. The native score can reward recovering or copying supplied predictions and does not isolate novel function inference. The prespecified curated-only diagnostic is separate and also has predictor overlap with unknown historical independence. No metric cherry-picking or context ablation is permitted.

| Offline supplied-predictor overlap audit | ID | OOD |
|---|---:|---:|
| Cases with input GO IDs overlapping native target | 6,989/6,989 | 7,883/7,883 |
| Cases with input GO IDs overlapping curated target | 6,989/6,989 | 7,883/7,883 |
| Seed-context-only native augmented mean propagated F1 | 0.984210 | 0.989353 |
| Seed-context-only curated mean propagated F1 diagnostic | 0.701277 | 0.631665 |

These are deterministic input/reference dependence measurements, **not Qwen results or new inference conditions**. Complete model inputs stayed byte-identical when this audit was added.

The [paper](https://arxiv.org/html/2606.16517v1) AppendixD.3/Table9 reports rounded ID0.935/OOD0.956 for its Qwen3-4B-Thinking, GRPOβ=0.001,1epoch/4Kexample condition. These are contextual published comparisons, not matched-system claims. Source disagreements are explicit: paper ESM3/projector descriptions versus released standalone text RL code; SFT's generic hf_reasoning defaults versus RL's richer prompt; Fmax captions versus actual mean set-F1; different historical decoding and zero-shot27B4096-token chat wrapper. Exact archived author per-case predictions have not been found.

## N04 network-held-out KEGG

The native launcher requires `train_network_split.csv`, `id_test_network_split.csv` and `ood_test_network_split.csv`. The [author genomics release folder](https://drive.google.com/drive/folders/1lz00_m0mASxLggnPtBCtxJQ3hvMeS5XP) redirected unauthenticated HTTP to Google sign-in on15October; the response is preserved. No account login or alternate authentication was attempted. This observation establishes current access failure, not whether the link was deleted, restricted or otherwise unavailable.

Exact adapted IDs, row order, network membership and counts remain unavailable. `train_dna_qwen.py::_load_kegg_dataset` silently falls back to original `wanglab/kegg` if any local CSV is absent. That fallback would change the task and was not executed. Native inputs require both original DNA windows plus original pathway/gene question context; no random290-case N01 or guessed repartition is a substitute. Source label matching/accuracy code was acquired, but the missing split blocks a paper-comparable run.

## N05 hepatoblastoma target selection

This is the paper's fixed-input **MEDEA** adaptation, not a Cell2Sentence cell-type task. The pinned241-file repository only vendors Cell2Sentence tutorials and releases protein/genomics download links; no adapted RNA test manifest, expression alignment adapter or native RNA scorer was found. The paper requires disease/cell context, exact five candidates and aligned normal/disease TranscriptFormer representations in candidate order. It also describes gene-symbol normalized final-answer accuracy; exact implementation is unavailable.

Useful upstream artifacts do exist. [Medea@49a7abb](https://github.com/mims-harvard/Medea/tree/49a7abbfddd7c713add0f7b8ba77bc94a9af2c15) publicly releases60hepatoblastoma query rows for each of seeds42/43/44. [MedeaDB@b94d025](https://huggingface.co/datasets/mims-harvard/MedeaDB/tree/b94d02500b0c887912001e0acda96da54d7d83dc) releases TranscriptFormer stores; pinned hepatoblastoma metadata describes16,794genes,2048dimensions and15groups. Small source/query CSVs, metadata, native upstream lookup code and licenses were acquired and verified. Large matrices were not downloaded because exact posttrain case membership, ordering, vector transformation/projection and missing-state handling remain unverified.

Those180upstream queries are not asserted to equal the adapted posttrain test. Running upstream full agent queries or a gene-list-only substitute would change required information and protocol. Required next artifacts are the exact adapted split IDs/order/questions, candidate-to-normal/disease vector mapping, source preprocessing and gene-normalization evaluator, plus original learned projection/checkpoint if full native model replication is intended. The learned biological representations may be essential; their absence does not invalidate the prediction task.
