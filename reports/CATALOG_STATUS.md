# Full retained catalog status

Observed **2026-10-20T13:34:51.795431-07:00** (America/Los_Angeles). Exactly **57 settings**, one row each.

Done means a defined score for the declared evaluated condition. It does not imply matched-paper replication, complete original-paper scope, or good performance. Saved responses alone do not count as done.

| Status | Count |
|---|---:|
| Done: defined score for the declared evaluated condition | 28 |
| Running generation | 3 |
| Queued for generation in the frozen runtime | 1 |
| Doable agent work not finished | 15 |
| Held at the user's request | 3 |
| Biological/provider interruption or restriction | 7 |
| Whole setting established impossible | 0 |

Doable agent work includes 15 implementation review preparation. These tasks are not all in a live generation queue.

**Dated runtime health observation (2026-10-20T13:15:23-07:00):** HTTP model/health checks timed out while multiple DFS readers and the server stalled in filesystem I/O. GPU activity did not establish healthy HTTP delivery. [Observation details](CATALOG_RUNTIME_IO_2026-10-20.json); current health requires a fresh check.

Current successor runtime job: 243499. Old predecessor drain exits remain historical evidence.

The existing controller was restarted under supervision around **12:31 PM PDT** after an `Errno 116` stale-file-handle crash. Its supervisor is fresh at 2026-10-20T13:34:46.688045-07:00; pool heartbeat fresh: **True**. This does not create a new protocol or extra inference scope.

Exceptions for training and replacement judges remain user-held. Biological/provider holds are separate and cannot be cleared by a simple continuation instruction. Exact native unavailability is tracked separately from whether an available adaptation can proceed.

## Every retained setting

| ID | Setting | Status | Saved/planned | Next action / decision | Evidence |
|---|---|---|---:|---|---|
| B01 | LAB-Bench / LitQA2 | Done | — | Preserve existing scores and qualifications; no new generation is pending for this setting. | [EVALUATION_DECISION_TABLE.json](../reports/EVALUATION_DECISION_TABLE.json) |
| B02 | LAB-Bench / DbQA | Done | — | Preserve existing scores and qualifications; no new generation is pending for this setting. | [EVALUATION_DECISION_TABLE.json](../reports/EVALUATION_DECISION_TABLE.json) |
| B03 | LAB-Bench / SuppQA | Done | — | Preserve existing scores and qualifications; no new generation is pending for this setting. | [EVALUATION_DECISION_TABLE.json](../reports/EVALUATION_DECISION_TABLE.json) |
| B04 | LAB-Bench / FigQA | Done | — | Preserve existing scores and qualifications; no new generation is pending for this setting. | [EVALUATION_DECISION_TABLE.json](../reports/EVALUATION_DECISION_TABLE.json) |
| B05 | LAB-Bench / TableQA | Done | — | Preserve existing scores and qualifications; no new generation is pending for this setting. | [EVALUATION_DECISION_TABLE.json](../reports/EVALUATION_DECISION_TABLE.json) |
| B06 | LAB-Bench / ProtocolQA | Provider held | — | Preserve completed evidence and holds; do not retry, rephrase or reroute the interrupted/flagged action. Continue only separate permitted offline metadata/scoring work. | [AGENTS.md](../AGENTS.md) |
| B07 | LAB-Bench / SeqQA | Done | — | Preserve existing scores and qualifications; no new generation is pending for this setting. | [EVALUATION_DECISION_TABLE.json](../reports/EVALUATION_DECISION_TABLE.json) |
| B08 | LAB-Bench / Cloning scenarios | Done | — | Preserve existing scores and qualifications; no new generation is pending for this setting. | [EVALUATION_DECISION_TABLE.json](../reports/EVALUATION_DECISION_TABLE.json) |
| P01 | Solubility — PEER | Done | — | Preserve existing scores and qualifications; no new generation is pending for this setting. | [EVALUATION_DECISION_TABLE.json](../reports/EVALUATION_DECISION_TABLE.json) |
| P02 | Binary localization — DeepLoc/PEER | Done | — | Preserve existing scores and qualifications; no new generation is pending for this setting. | [EVALUATION_DECISION_TABLE.json](../reports/EVALUATION_DECISION_TABLE.json) |
| P03 | Subcellular localization — DeepLoc | Done | — | Preserve existing scores and qualifications; no new generation is pending for this setting. | [EVALUATION_DECISION_TABLE.json](../reports/EVALUATION_DECISION_TABLE.json) |
| P04 | Beta-lactamase activity — PEER | Agent work | — | Inventory the acquired 520-case test LMDB, review assay eligibility, isolate targets and freeze a scalar delivery/scoring contract. | [CATALOG_STATUS.json](../reports/CATALOG_STATUS.json) |
| P05 | AAV variant fitness — FLIP | Agent work | — | Review the available FLIP AAV assay scope, isolate test inputs/targets and freeze scalar delivery and scoring. | [catalog_extended_preparation.json](../reports/catalog_extended_preparation.json) |
| P06 | Thermostability — FLIP/Meltome | Done | 1,366/1,366 | Preserve sealed predictions and score; reconcile/publicly publish this tracker and report metadata. | [scores.json](../results/runs/qwen38_27b_p06_full_test_nonthinking_regex256_2026-10-20_v1/scores.json) |
| P07 | GFP fluorescence — TAPE | Done | 27,217/27,217 | Preserve sealed predictions and score; reconcile/publicly publish this tracker and report metadata. | [scores.json](../results/runs/qwen38_27b_p07_full_test_nonthinking_scalar_2026-10-20_v1/scores.json) |
| P08 | Protein stability regression — TAPE | Done | 12,851/12,851 | Preserve sealed predictions and score; reconcile/publicly publish this tracker and report metadata. | [scores.json](../results/runs/qwen38_27b_p08_full_test_nonthinking_structured_scalar_2026-10-20_v1/scores.json) |
| P09 | Stability classification — NatureLM/PEER | Done | — | Preserve sealed predictions and score; reconcile/publicly publish this tracker and report metadata. | [scores.json](../results/runs/qwen38_27b_p09_scireason_gt1_from_p08_2026-10-20_v1/scores.json) |
| P10 | Human protein–protein interaction — PEER | Done | — | Preserve existing scores and qualifications; no new generation is pending for this setting. | [EVALUATION_DECISION_TABLE.json](../reports/EVALUATION_DECISION_TABLE.json) |
| P11 | Yeast protein–protein interaction — PEER | Done | — | Preserve existing scores and qualifications; no new generation is pending for this setting. | [EVALUATION_DECISION_TABLE.json](../reports/EVALUATION_DECISION_TABLE.json) |
| P12 | Enzyme Commission labels — DeepFRI split | Running | 984/1,919 | Continue the existing one-attempt cohort, seal every outcome, then run native offline scoring after closure. | [CATALOG_STATUS.json](../reports/CATALOG_STATUS.json) |
| P13 | GO biological process — DeepFRI split | Running | 272/3,416 | Continue the existing one-attempt cohort, seal every outcome, then run native offline scoring after closure. | [CATALOG_STATUS.json](../reports/CATALOG_STATUS.json) |
| P14 | GO molecular function — DeepFRI split | Running | 834/3,416 | Continue the existing one-attempt cohort, seal every outcome, then run native offline scoring after closure. | [CATALOG_STATUS.json](../reports/CATALOG_STATUS.json) |
| P15 | GO cellular component — DeepFRI split | Queued | 0/3,416 | Existing runtime starts this grant when a client slot opens; no new permission required. | [CATALOG_STATUS.json](../reports/CATALOG_STATUS.json) |
| P16 | Reaction class — zero-/few-shot | Done | — | Preserve existing scores and qualifications; no new generation is pending for this setting. | [EVALUATION_DECISION_TABLE.json](../reports/EVALUATION_DECISION_TABLE.json) |
| P17 | ProteinGym DMS substitution benchmark | Agent work | — | Review permissible assay scopes in the acquired ProteinGym release and implement a version-matched, full-denominator score adapter. | [CATALOG_STATUS.json](../reports/CATALOG_STATUS.json) |
| P18 | PG-LLM / ProteinGym-LLM ranking | Provider held | — | Preserve completed evidence and holds; do not retry, rephrase or reroute the interrupted/flagged action. Continue only separate permitted offline metadata/scoring work. | [AGENTS.md](../AGENTS.md) |
| P19 | PFArena T1: single-mutant generation | Agent work | — | Integrate the prepared 34-assay subset into the central runtime and pass its three synthetic delivery checks; independently review the remaining 77 assays while preserving 12 holds. | [CATALOG_STATUS.json](../reports/CATALOG_STATUS.json) |
| P20 | PFArena T2: measurement-free multi-mutant ranking | Provider held | — | Preserve completed evidence and holds; do not retry, rephrase or reroute the interrupted/flagged action. Continue only separate permitted offline metadata/scoring work. | [AGENTS.md](../AGENTS.md) |
| P21 | PFArena T3: anchor-informed ranking | Agent work | — | Prepare permitted T3 anchor and candidate inputs from the 67 acquired tables, isolate target scores, and validate complete ranking delivery. | [CATALOG_STATUS.json](../reports/CATALOG_STATUS.json) |
| P22 | PFArena T4: single-mutant-informed ranking | Agent work | — | Prepare permitted T4 component-context and candidate inputs from the 29 acquired pairs, isolate target scores, and validate complete ranking delivery. | [CATALOG_STATUS.json](../reports/CATALOG_STATUS.json) |
| P23 | Mol-Instructions: Protein function generation | Done | — | Preserve existing scores and qualifications; no new generation is pending for this setting. | [EVALUATION_DECISION_TABLE.json](../reports/EVALUATION_DECISION_TABLE.json) |
| P24 | Mol-Instructions: Catalytic activity generation | Done | — | Preserve existing scores and qualifications; no new generation is pending for this setting. | [EVALUATION_DECISION_TABLE.json](../reports/EVALUATION_DECISION_TABLE.json) |
| P25 | Mol-Instructions: Domain and motif generation | Done | — | Preserve existing scores and qualifications; no new generation is pending for this setting. | [EVALUATION_DECISION_TABLE.json](../reports/EVALUATION_DECISION_TABLE.json) |
| P26 | Mol-Instructions: Functional description generation | Done | — | Preserve existing scores and qualifications; no new generation is pending for this setting. | [EVALUATION_DECISION_TABLE.json](../reports/EVALUATION_DECISION_TABLE.json) |
| P27 | NatureLM protein description | Agent work | — | Freeze a defensible available protein-description adaptation with fixed cohort/reference preprocessing; retain exact temporal NatureLM condition as unavailable. | [CATALOG_STATUS.json](../reports/CATALOG_STATUS.json) |
| P30 | MutaDescribe mutation explanation | Provider held | — | Preserve completed evidence and holds; do not retry, rephrase or reroute the interrupted/flagged action. Continue only separate permitted offline metadata/scoring work. | [AGENTS.md](../AGENTS.md) |
| P31 | MutaDescribe mutation engineering — position supplied | Provider held | — | Preserve completed evidence and holds; do not retry, rephrase or reroute the interrupted/flagged action. Continue only separate permitted offline metadata/scoring work. | [AGENTS.md](../AGENTS.md) |
| P32 | MutaDescribe mutation engineering — position unknown | Provider held | — | Preserve completed evidence and holds; do not retry, rephrase or reroute the interrupted/flagged action. Continue only separate permitted offline metadata/scoring work. | [AGENTS.md](../AGENTS.md) |
| P33 | MutaPLM low-N fitness regression | User held | — | New head training remains held. Search already released matching heads and prepare metadata; a different training scope requires a user decision. | [AGENTS.md](../AGENTS.md) |
| P34 | MutaPLM iterative sequence optimization | Agent work | — | Integrate the acquired encoder and five existing heads with the released optimization/scoring contract and explicit failure handling; preserve the held sixth landscape. | [SOURCE_ACQUISITION_PROGRESS_2026-10-19.json](../reports/SOURCE_ACQUISITION_PROGRESS_2026-10-19.json) |
| P35 | ProtST text-to-protein retrieval | Agent work | — | Freeze the qualified corpus condition, run retained/rejected PDB accounting, review corpus scope and pass retrieval delivery checks using the acquired existing checkpoint. | [CATALOG_STATUS.json](../reports/CATALOG_STATUS.json) |
| P36 | BioT5+ description-guided protein design | Provider held | — | Preserve completed evidence and holds; do not retry, rephrase or reroute the interrupted/flagged action. Continue only separate permitted offline metadata/scoring work. | [AGENTS.md](../AGENTS.md) |
| P37 | NatureLM unconditional generation | Agent work | — | Assemble and validate an isolated OmegaFold2 runtime/checkpoint, then pass an independent development gate for the declared released-code condition. | [CATALOG_STATUS.json](../reports/CATALOG_STATUS.json) |
| P38 | NatureLM stability/solubility-conditioned generation | Agent work | — | Validate NetSolP-D runtime, acquire the available ProtT5 encoder for the separate thermal proxy, and freeze independent generation/delivery contracts without training heads. | [CATALOG_STATUS.json](../reports/CATALOG_STATUS.json) |
| P39 | NatureLM heme-binding case study | Agent work | — | Freeze a clearly labelled available structural case-study condition and its complete selection/denominator contract using acquired evaluator assets; report proxy evidence without invented binding accuracy. | [REMAINING_DESIGN_SOURCE_FEASIBILITY_2026-10-15.json](../reports/REMAINING_DESIGN_SOURCE_FEASIBILITY_2026-10-15.json) |
| P40 | RAbD CDR-H3 redesign | Agent work | — | Independently review the 60 cases and implement a solver adapter that preserves permitted geometric context while hiding target residue identities and coordinates. | [CATALOG_STATUS.json](../reports/CATALOG_STATUS.json) |
| P41 | Proteo-R1 all-CDR SAbDab holdout | Agent work | — | Assemble the available released-demo structural runtime and its masking/scoring adapter; document differences from the unreleased native holdout. | [REMAINING_DESIGN_SOURCE_FEASIBILITY_2026-10-15.json](../reports/REMAINING_DESIGN_SOURCE_FEASIBILITY_2026-10-15.json) |
| P42 | STRIDE GFP generated-candidate evaluation | Done | — | Preserve existing scores and qualifications; no new generation is pending for this setting. | [EVALUATION_DECISION_TABLE.json](../reports/EVALUATION_DECISION_TABLE.json) |
| P43 | Drug–target interaction — BioSNAP/Human/BindingDB | Done | — | Preserve existing scores and qualifications; no new generation is pending for this setting. | [EVALUATION_DECISION_TABLE.json](../reports/EVALUATION_DECISION_TABLE.json) |
| P44 | BioReason-Pro explanation assessment | User held | — | Replacement external judge remains held. Prepare available evidence/rubric metadata; a scoring/judge choice requires a user decision. | [AGENTS.md](../AGENTS.md) |
| V01 | VQA-RAD | Done | — | Preserve existing scores and qualifications; no new generation is pending for this setting. | [EVALUATION_DECISION_TABLE.json](../reports/EVALUATION_DECISION_TABLE.json) |
| V02 | SLAKE — English | Done | — | Preserve existing scores and qualifications; no new generation is pending for this setting. | [EVALUATION_DECISION_TABLE.json](../reports/EVALUATION_DECISION_TABLE.json) |
| V03 | PathVQA | Done | — | Preserve existing scores and qualifications; no new generation is pending for this setting. | [EVALUATION_DECISION_TABLE.json](../reports/EVALUATION_DECISION_TABLE.json) |
| V04 | ImageCLEF-VQA 2019 | Done | — | Preserve existing scores and qualifications; no new generation is pending for this setting. | [EVALUATION_DECISION_TABLE.json](../reports/EVALUATION_DECISION_TABLE.json) |
| V05 | PMC-VQA held-out evaluation | Done | — | Preserve existing scores and qualifications; no new generation is pending for this setting. | [EVALUATION_DECISION_TABLE.json](../reports/EVALUATION_DECISION_TABLE.json) |
| V06 | LLaVA-Med visual conversation | User held | — | Replacement external judge remains held. Solver packaging can proceed; a scoring/judge choice requires a user decision. | [AGENTS.md](../AGENTS.md) |
| V07 | Ryze extraction component tests | Agent work | — | Review the 2,215 question/full-deck scopes, run actual processor expansion and 20-image context checks, then pass the independent delivery gate. | [CATALOG_STATUS.json](../reports/CATALOG_STATUS.json) |

## Native-condition and scope qualifications

| ID | Availability / material qualification |
|---|---|
| B06 | Source availability is separate from this execution/review hold; no claim that the whole source corpus is prohibited or missing. Primary source has no embedded timestamp; this read verifies availability, not a fresh execution heartbeat. |
| B08 | A score for the declared evaluated scope does not establish matched-paper reproduction. reviewed_public_subset Separate uniform-16K 33-case proposal remains proposed/not dispatched; it is not an active remaining queue. |
| P04 | Source archive acquired; assay eligibility and runtime preparation remain unfinished. Already authorized agent work; an internal exact frozen grant is an engineering gate, not another broad user permission request. |
| P05 | Released inputs available; eligibility review and execution preparation unfinished. Already authorized agent work; an internal exact frozen grant is an engineering gate, not another broad user permission request. Primary source has no embedded timestamp; this read verifies availability, not a fresh execution heartbeat. |
| P09 | Original NatureLM binary conversion/test labels unavailable in inspected author releases. Completed declared >1.0 rule-derived adaptation reuses sealed P08 predictions. 53.28768189245972% accuracy (6848/12851); no extra model generation; not native NatureLM label certification. |
| P12 | Released test and native AP/Fmax scorer available; dense confidence-vector delivery is a separately frozen new condition. Current verified successor job 243499; predecessor drain exits remain historical operational evidence. |
| P13 | Released test and native AP/Fmax scorer available; dense confidence-vector delivery is a separately frozen new condition. Current verified successor job 243499; predecessor drain exits remain historical operational evidence. |
| P14 | Released test and native AP/Fmax scorer available; dense confidence-vector delivery is a separately frozen new condition. Current verified successor job 243499; predecessor drain exits remain historical operational evidence. |
| P15 | Released test and native AP/Fmax scorer available; dense confidence-vector delivery is a separately frozen new condition. Current verified successor job 243499; predecessor drain exits remain historical operational evidence. No progress is not proof of zero requests. This queue classification uses the frozen grant and absence of a started record, not filename response counts. |
| P17 | 217 released assay CSVs acquired; reviewed execution scope remains unfinished. Already authorized agent work; an internal exact frozen grant is an engineering gate, not another broad user permission request. |
| P18 | Source availability is separate from this execution/review hold; no claim that the whole source corpus is prohibited or missing. Primary source has no embedded timestamp; this read verifies availability, not a fresh execution heartbeat. |
| P19 | Required sources available; full coverage limited by unfinished review and existing case holds. Already authorized agent work; an internal exact frozen grant is an engineering gate, not another broad user permission request. |
| P20 | Source availability is separate from this execution/review hold; no claim that the whole source corpus is prohibited or missing. Primary source has no embedded timestamp; this read verifies availability, not a fresh execution heartbeat. |
| P21 | Required source tables acquired; eligibility, input isolation and runtime integration unfinished. Already authorized agent work; an internal exact frozen grant is an engineering gate, not another broad user permission request. |
| P22 | All 29 context/target pairs acquired; eligibility, isolation and runtime integration unfinished. Already authorized agent work; an internal exact frozen grant is an engineering gate, not another broad user permission request. |
| P27 | Exact native NCBI dates/accession manifest not found in audited author releases; labelled adaptation remains possible. Already authorized agent work; an internal exact frozen grant is an engineering gate, not another broad user permission request. |
| P30 | Source availability is separate from this execution/review hold; no claim that the whole source corpus is prohibited or missing. Primary source has no embedded timestamp; this read verifies availability, not a fresh execution heartbeat. |
| P31 | Source availability is separate from this execution/review hold; no claim that the whole source corpus is prohibited or missing. Primary source has no embedded timestamp; this read verifies availability, not a fresh execution heartbeat. |
| P32 | Source availability is separate from this execution/review hold; no claim that the whole source corpus is prohibited or missing. Primary source has no embedded timestamp; this read verifies availability, not a fresh execution heartbeat. |
| P33 | Required training/judge exception remains held; source or solver preparation does not itself complete the score. Primary source has no embedded timestamp; this read verifies availability, not a fresh execution heartbeat. |
| P34 | Existing evaluator assets acquired; released-code algorithm and runtime implementation unfinished; no new training. Already authorized agent work; an internal exact frozen grant is an engineering gate, not another broad user permission request. |
| P35 | Five released query rankings are feasible. The release provides no relevance gold or aggregate correctness metric; do not invent accuracy. Already authorized agent work; an internal exact frozen grant is an engineering gate, not another broad user permission request. Rankings can be produced. A new aggregate correctness metric would require a separate source-grounded research decision; qualitative evidence is not scored accuracy. |
| P36 | Source availability is separate from this execution/review hold; no claim that the whole source corpus is prohibited or missing. Only historical 59-response partial evidence is generated. Extension preserved 188 prepared inputs, with 5604 unreviewed; later interruption overrides the older continue-from-index-256 checkpoint instruction. Primary source has no embedded timestamp; this read verifies availability, not a fresh execution heartbeat. |
| P37 | Matching released-code evaluator assets acquired; exact native sampling and 50% clustering condition unavailable in inspected releases. Already authorized agent work; an internal exact frozen grant is an engineering gate, not another broad user permission request. Primary source has no embedded timestamp; this read verifies availability, not a fresh execution heartbeat. |
| P38 | Exact SFM property heads/reference cohort unavailable in inspected releases; distinct available proxy conditions prepared. Already authorized agent work; an internal exact frozen grant is an engineering gate, not another broad user permission request. |
| P39 | Exact native cohort, selection manifest and scoring contract unreleased in inspected sources; qualitative adaptation remains possible. Already authorized agent work; an internal exact frozen grant is an engineering gate, not another broad user permission request. Primary source has no embedded timestamp; this read verifies availability, not a fresh execution heartbeat. |
| P40 | 60 current-structure mappings/masks prepared; exact historical processed bytes not certified; current-structure adaptation available. Already authorized agent work; an internal exact frozen grant is an engineering gate, not another broad user permission request. |
| P41 | Released checkpoints/vendor assets and demos acquired; exact SAbDab holdout, masks and full benchmark aggregation unavailable in inspected releases. Already authorized agent work; an internal exact frozen grant is an engineering gate, not another broad user permission request. Primary source has no embedded timestamp; this read verifies availability, not a fresh execution heartbeat. |
| P44 | Required training/judge exception remains held; source or solver preparation does not itself complete the score. Primary source has no embedded timestamp; this read verifies availability, not a fresh execution heartbeat. |
| V06 | Required training/judge exception remains held; source or solver preparation does not itself complete the score. Primary source has no embedded timestamp; this read verifies availability, not a fresh execution heartbeat. |
| V07 | All 8,000 page identities materialized/hash-verified; mixed original/processed image adaptation available; exact Table 3 condition unavailable. Already authorized agent work; an internal exact frozen grant is an engineering gate, not another broad user permission request. |

The [JSON tracker](CATALOG_STATUS.json) includes per-setting source times, hashes, all evidence paths, runtime errors and score metadata. Historical metrics and their separate conditions remain in [the decision table](EVALUATION_DECISION_TABLE.md).

Regenerate with `python3 scripts/build_catalog_status.py`. This performs metadata reads and report writes only; it makes no inference calls or dispatch changes.
