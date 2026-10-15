# Public biological evaluations

This workspace covers all 64 biological evaluation settings. The initial
eight prepared protein settings remain part of that expanded scope.
The original handoff is retained under `handoff/`.

Preparation, public source acquisition, CPU-only dry runs, cost estimation,
and leakage checks are authorized. On 14 October 2026 UTC, the user explicitly
requested actual evaluations across the full catalog with comparisons to papers.
This supersedes the previous preparation-only scope and authorizes inference
with the previously discussed inexpensive model. Use an agent-imposed initial
API spending guard of $50; this is not a numeric cap supplied by the user.
Read credentials privately at runtime from the environment or the user-supplied
key file; never print them or save copies. Freeze protocols before scored calls.
Keep the separate Affibody data and evaluations unchanged.

Use official releases, splits, prompts, and scorers where verified. Mark
new text baselines as adaptations. Keep answers and reference explanations
out of requests. Never tune against protected test outcomes. PG-LLM is
native-only and evaluation-only. Preserve complete sequences.

Use synthetic or permitted development cases for tests. Record source versions,
hashes, coverage, failure counts, and estimated costs. Prior model exposure to
public benchmarks is unknown; do not claim contamination-free evaluation.
No new SSH connection is needed for this workspace. The standing limit is
at most one GPU; current preparation uses CPU only.

Read `/data/rustfs1/dongweij/EXECUTION_EXAMPLES.md` before further execution
or interpretation. Record task demands as provisional analyst descriptions
from inputs, output targets and reference evidence, independently of A–F
interface compatibility. Keep valid biological prediction tasks even where
learned protein representations may be essential.

Maintain `results/interpretation_notes.jsonl`, keyed by task ID and protocol
variant, and the separate interpretation table in `reports/`. Distinguish
prepared fields from exact information actually dispatched to the solver.
Separate outcome correctness from reference-supported explanation, unverified
hypothesis, missing support and contradiction. Correct predictions do not
validate rationales, and missing support does not automatically mean false.
The addendum's illustrative values/examples are not benchmark/training data
and do not authorize extra context or reasoning-budget variants. Preserve
native metrics, scope, budgets, restrictions and the existing original catalog.

On 14 October 2026 UTC the user authorized creating a private repository and
uploading this evaluation workspace daily. `scripts/daily_backup.py` commits
code/reports and compressed data/source/result snapshots; check
`reports/BACKUP_SETUP.md` and `.local/backup_status.json` for status. Credentials
stay local. This authorization does not approve paid inference or uploading
unrelated Affibody data. Never give a benchmark solver access to this repository
or its archives, which contain held-out evaluation material.

The user subsequently cancelled the GitHub update work. The daily GitHub cron
job has been disabled; preserve local work and do not attempt further uploads.
The user now prioritizes actual evaluations and paper-comparable results across
all settings. Keep unavailable-source, incompatible-output, qualitative-only,
and protocol blockers explicit; expanding scope never authorizes fabricated
metrics, held-out tuning, training new heads, or changes to native restrictions.

On 14 October 2026 UTC, the user reported an OpenAI warning for Prohibited
Biological Use. Local P18 logs contain 43 `bio_policy` rejections, including
requests ranking pathogen protein variants for viral replication. Inference
authorization is suspended in `configs/execution_authorization.json`; no API
evaluation workers remain active. Do not submit more inference, retry policy
rejections, relabel organisms, change keys/identifiers, or change providers to
get the flagged material through. Preserve logs and allow offline source,
scoring and incident analysis. Obtain provider clarification and review the
permitted task scope before any decision to resume. See
`reports/policy_warning_local_audit.json` and the incident report.

The user subsequently reported submitting the appeal. No provider clearance has
been reported. The OpenAI inference hold remains active.

For this local model serving and evaluation project, the user explicitly changed
the GPU limit to **up to eight GPUs** when asked about deploying a larger model.
This supersedes the earlier one-GPU limit for this project only; it does not
change the separate Affibody project's resource rules. Local serving setup and
synthetic capability checks may proceed. Keep flagged pathogen-fitness tasks
held, preserve native benchmark restrictions, and do not route flagged requests
to a different model or provider to get them through. A local model is a separate
baseline for permitted tasks, with its exact checkpoint and precision recorded.

On October 15 UTC, the user pointed out Qwen3.8. The previous Qwen3.5 model
recommendation missed current releases and has been superseded by the proposed
Qwen3.8-Flash-Next-FP8 baseline (about 172.78 GiB), with Qwen3.8-27B as a smaller
candidate (about 51.75 GiB). The installed vLLM 0.31.0 registers both model
architectures. Flash-Next requires expert parallelism for TP8 with its FP8 blocks;
use the updated launcher and the current official recipe. No weights have been
downloaded. Researching or correcting this plan does not restart stopped jobs
or authorize dispatch of flagged benchmark requests. The local benchmark task
allowlist remains empty and the OpenAI hold remains active.

The user then selected **Qwen3.8-27B first on one GPU**. This is the current
deployment, superseding the larger proposal for the initial run. Download and
serve the pinned original BF16 checkpoint on GPU 4 only, preserving native vision
and the 262,144-token context if startup validates it. The eight-GPU Flash-Next
proposal is archived in `configs/local_model_flash_next_proposed.json`. Setup and
synthetic checks are authorized; the biological task allowlist remains empty and
the OpenAI hold and flagged-task restrictions remain unchanged.

The authorized single-GPU setup is running through
`scripts/bootstrap_local_model.py`. Consult `reports/local_model_deployment.json`
and `.local/local_model_setup_process.json` before starting another worker. It
waits for the existing Hugging Face download, verifies pinned weight SHA-256
digests, launches loopback vLLM, and runs synthetic text/reasoning-interface/vision
checks. A `ready` state requires those checks to pass. No biological dispatch is
part of this worker. Server identity is recorded in `.local/local_model_server.json`.

The first Xet transfer completed 17 shards but suffered repeated proxy/CDN
timeouts. `scripts/finish_checkpoint_download.py` now finishes the last shard
with resumable aria2 over **direct HTTPS to the publisher's ModelScope China
CDN**, clearing proxy variables only for that download process. Publisher
Hugging Face and ModelScope replicas have identical pinned SHA-256 digests.
Check `.local/local_model_final_transfer.json` and
`.local/local_model_manual_transfer_control.json` before starting another
download. The finisher may hold the setup worker stopped during transfer; it
verifies the final shard, records the checkpoint manifest, and resumes setup
automatically. No new SSH connection or global proxy setting change is needed.

The complete Qwen3.8-27B checkpoint is now downloaded. All 18 weight-file SHA-256
digests and all 14 supporting-file digests match the pinned repository, totaling
32 source files and 55,586,114,863 bytes. See
`reports/local_model_complete_verification.json`. The setup worker was resumed
and is performing the authorized one-GPU serving and synthetic checks; consult
`reports/local_model_deployment.json` for the current stage. Do not redownload
the model merely because old failed-transfer logs remain in the log directory.

The first server attempt on GPU 4 failed its startup memory-budget check as
other allocations changed. The active retry uses GPU 5 only, 65% GPU memory
utilization and four concurrent sequences, preserving BF16, vision and native
262,144-token context. This changes the earlier agent-selected GPU index, while
retaining the user's one-GPU limit. No unrelated GPU process was stopped.

The runtime launcher now prepends its own `.venv-vllm/bin` and the installed CUDA
compiler directory to PATH. Ninja 1.13.2 was already installed but absent from
the old launcher PATH. A real synthetic FlashInfer top-k sampling kernel compiled
and passed on GPU 5 after this fix. FlashInfer and CUDA driver caches are directed
to the project disk. See `reports/local_model_sampling_kernel_check.json`.

As of October 14 at 9:03 PM PST, the complete verified checkpoint and one-GPU
server are **ready**. The live server is on GPU 5 at `127.0.0.1:8026`; actual GPU
process inspection confirmed one H200. Text, reasoning-interface and synthetic
image checks passed. See `reports/local_model_server_validation.json` and
`reports/local_model_capability_smoke.json`. The smoke client now omits an empty
`tools` array, which vLLM 0.31 rejects. The setup worker reuses prior pinned hashes
only if checkpoint files are unchanged; synthetic-client failures preserve a
healthy server for diagnosis. No Qwen biological benchmark inference has run.

On October 15 UTC the user explicitly requested starting evaluations. The first authorized local run is B01 LitQA2, restricted to the 197 input-reviewed public case IDs in `configs/local_labbench_litqa2_review.json`; two pathogen mutation/antibody-response cases remain held. The frozen config is `configs/local_labbench_litqa2.json`. Original prompts/choices and native metrics are retained, with one seeded Qwen generation per case and separate offline scoring. This is a reviewed public subset, not the full paper evaluation. Keep the OpenAI inference hold, all flagged P18 requests, other unreviewed local tasks and the one-GPU resource scope unchanged. Consult the local run progress before starting another worker.

Native LAB-Bench preparation now lives in `data/labbench_native_complete/`
(1,967 public cases). The FigQA and TableQA parquet files are downloaded and
publisher-SHA-256 verified; 181 figure images and 262 table images are retained.
The former B03 preparation omitted required paper titles/DOIs and B06 omitted
required protocol text. Both omissions are fixed in the new directory and
validated against the pinned official task transformations using synthetic
fixtures. Keep the previous directory and report unchanged because current
LitQA2 execution freezes them as provenance. `scripts/prepare_labbench.py`
defaults to the new directory and rejects the old frozen paths. See
`reports/LABBENCH_NATIVE_INPUT_REVIEW_2026-10-15.md`. Preparation does not extend
the local inference allowlist; other case reviews and frozen configs are pending.

The interpretation registry now includes separate `NATIVE_PUBLIC_COT` prepared
records for all eight LAB-Bench categories; the executed Qwen B01 variant is
distinct. Preserve executed/model/run metadata and complete native preparation
records when maintaining the registry. The earlier `scripts/interpretations.py`
generator predates these records and requires preservation support before being
used to regenerate reports. Exact first-run code/input/scorer snapshots are in
that run's `frozen_files/`; no weights or credentials were duplicated.

The first local Qwen LitQA2 run completed on October 15 at 05:35 UTC: 197/197 reviewed public cases, 77 correct (39.1% accuracy), 41.0% precision and 95.4% coverage. All requests/responses, parser outputs, labels and metrics reconciled; no errors or truncations. Two input-reviewed cases remain held. See `reports/FIRST_LOCAL_EVALUATION.md`, `reports/local_evaluation_status.json` and the run's `artifact_audit.json`. No explanation-support or contamination-free reasoning claim follows. The model server remains available on GPU 5; other local case allowlists remain unapproved.

On October 15 the user reauthorized creating a private repository and uploading the whole evaluation project. `Some-random/bio-evaluation` was created and its private flag/push permission verified. This authorizes a one-time snapshot, without a recurring schedule. An initial packaging job prepared local checkpoint archive copies while the optional checkpoint scope question was pending; no weight assets were uploaded. Credentials, environments, caches, transient process state and unrelated Affibody work remain local. Consult `.local/github_upload/progress.json` before starting another uploader. The upload uses the existing connection/proxy and opens no SSH session. All evaluation holds and solver leakage restrictions remain unchanged. The old daily schedule stays disabled.

The user then clarified the checkpoint scope: **"Keep the public checkpoint local; back up model references only."** This supersedes the preceding checkpoint-release interpretation. Upload code, evaluation data, public sources, raw outputs, results, logs, reports and pinned model references, but no model weights or checkpoint archive parts. `configs/backup.json` records this choice. The original checkpoint remains local; temporary upload copies may be removed once their uploader is stopped. This remains a one-time upload, with no new daily schedule and no changes to evaluation authorization.
