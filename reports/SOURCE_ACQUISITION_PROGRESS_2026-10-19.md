# Official-source acquisition

Snapshot: 2026-10-19T15:48:12.673173-07:00 (America/Los_Angeles).

**Three previously missing prediction archives, all LLaVA-Med images, full upstream ChartQA images, ArxivQA assets and60upstream RAbD structures have been acquired. Other downloads continue.**

These are source/data/evaluator acquisitions, not newly completed biological benchmark scores. Existing Qwen generations and scientific scores are preserved. Model weights remain local.

| Setting | Asset | Acquisition | Remaining work |
|---|---|---|---|
| P04 | PEER beta-lactamase | Official archive downloaded; publisher MD5 matches. | Assay/case eligibility and frozen input/scoring preparation remain unfinished. |
| P05 | FLIP AAV | Official splits archive and exact two_vs_many CSV/FASTA downloaded; pinned Git blob verified. | Input-only eligibility review and a frozen Qwen protocol remain unfinished. |
| P17 | ProteinGym substitutions | Official v1.3 archive downloaded; all217 assay CSV member CRCs passed. | Assay eligibility and release-specific prediction/scoring protocol remain unfinished; flagged assays remain held. |
| V06 | LLaVA-Med images | All50 original images recovered, covering193questions, including31previously missing. | Native GPT-4-0314 judge access/execution is unresolved and outside the Luna-only comparison scope. |
| V07/upstream | ChartQA | All1509 official images verified against pinned Git blob hashes;2500questions covered. | This is upstream ChartQA, not certification of the exact Ryze Table3 condition. |
| V07/upstream | ArxivQA | Official100000-row JSON and7.95GB image archive publisher SHA256s verified; non-label mapping matches Ryze-Data. | Exact paper Table3 roster/run correspondence remains unverified. |
| V07/source | Ryze-Data | New official author repository acquired:151 Git blobs at ea5c0de8fbb495abaab882f395f8e84d7e056019. | Real loaders, prompts, downstream Qwen3-VL-8B QA and scorers are recovered; exact Table3 and ChartQA branch remain unresolved. |
| V07/upstream | SlideVQA | Public author-linked original images are downloading under a bounded durable worker; read live receipts. | Some original URLs return404. Hugging Face mirror requires legitimate account access. Raw assets and annotations stay internal under source license. |
| P34 | Optimization evaluator | ESM1b encoder and five previously permitted heads/start assets recovered; inspect integrity receipts. | Qwen likelihood/search adapter and source-versus-paper execution contract remain unfinished. No model forward or held landscape. |
| P35 | ProtST retrieval | Complete GO corpus acquired and publisher MD5 verified;8.53GB checkpoint final verification continues; pinned source files recovered. | Full retained corpus inventory and a declared Qwen ranking interface/relevance evaluation remain unfinished. |
| P37 | Generation structure evaluator | OmegaFold checkpoint downloaded and locally hashed; pinned source recovered; final source-integrity receipt is authoritative. | Native sampling/filter/clustering/folding settings and cohort remain unresolved. |
| P40 | RAbD structural context | All60 upstream PDB coordinate files acquired from RCSB; gzip CRC/header identities checked and local hashes recorded. | These are current upstream coordinates, not a certified processed paper holdout. Exact masks, numbering and evaluation settings remain unresolved. |
| P41 | Proteo-R1 checkpoints | Public understanding/generation checkpoints are being acquired as opaque files, with publisher LFS SHA256 checks. | Exact test holdout, preprocessing and complete runtime/scoring contract remain unresolved. No checkpoint loading. |
| P09/P27/P38 | NatureLM missing artifacts | Current official source was reacquired and hashed; original generator weights are distinct from evaluation artifacts. | Binary stability conversion, temporal test manifest, exact property heads and reference cohort were not found in inspected author releases. |
| P19-P22 | PFArena | Current official code and metadata acquired. Exact dataset access probe still returns401. | Legitimate Hugging Face dataset access is needed; no gate terms were accepted or access controls bypassed. |
| P30-P32/source | MutaDescribe | Six official test/validation CSVs and45official/reproduction source files acquired and publisher-hash checked;35.4MBtotal. Test splits contain1248structural and1611temporal cases. | Original interrupted source review and execution holds are not lifted by downloading files. Exact old trigger remains unknown; original two-stage interface differs from reproduction-provided context. |

## Input-review scope

The B06 worker continued independent input review after excluding the previously identified held case before content inspection. Its completed receipt currently records 59 ordinary benign candidates out of108source cases. These are input-review candidates, not dispatched or scored cases.

An automatic biological-safety check interrupted that review again; the exact new trigger was not returned. Completed records and the prior hold are preserved. The blocked content was not retried or forwarded to Qwen. This does not establish that every ProtocolQA or MutaDescribe case is prohibited.

Previously rejected P18 material remains held. P30-P32 source acquisition keeps mutation content opaque and does not resume the interrupted review or authorize inference.

## Sources and live evidence

[Official Ryze-Data](https://github.com/Chivier/Ryze-Data), [ChartQA](https://github.com/vis-nlp/ChartQA), [NCBI distribution documentation](https://pmc.ncbi.nlm.nih.gov/tools/pmcaws/), [PFArena](https://huggingface.co/datasets/AMix-Bio/PFArena), [SlideVQA](https://huggingface.co/datasets/NTT-hil-insight/SlideVQA).

The companion JSON records receipt hashes and a source-runtime snapshot. Fresh worker status is under `.local/source_acquisition_2026-10-19/status.json`; the existing hourly updater reads that observer. No duplicate hourly schedule was installed.

SlideVQA raw annotations, scripts, image URLs and images are not redistributed here. Public acquisition notes contain aggregate counts and provenance only.
