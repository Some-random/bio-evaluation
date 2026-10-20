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

On October 15 the user explicitly expanded local evaluation to all other benchmark settings and requested continuing until they are evaluated and compared with public results. This supersedes the earlier B01-only execution scope for permitted tasks. Use the existing pinned local Qwen server on GPU 5; no OpenAI calls, paid model APIs, new model/head training, test-guided tuning, or transfer of flagged requests. Task/case input reviews and frozen native/adapted protocols remain necessary and can be completed autonomously. Do not treat unavailable native structural/oracle/measurement protocols as completed by a text adaptation; report exact blockers. The first completed LitQA2 artifacts and code snapshots remain frozen.

For the expanded all-benchmark run, retain the prior user-authorized ceiling of eight GPUs. The initial27B run used one GPU; identical independent TP1 replicas may now use the observed idle GPUs6,7,4 in addition to the unchanged GPU5 server. Leave occupied GPUs0-3 and all unrelated jobs untouched. Share the same verified BF16 checkpoint without additional disk copies; freeze each run's serving endpoint, physical GPU and server identity. This is throughput scaling of one fixed baseline, not test-driven model selection.

For the expanded suite, the central local allowlist now includes reviewed
B02/B03/B04/B05/B07/B08, P01/P02/P03/P06/P07/P08/P10/P11/P23-P26/P43,
V01/V02 and N01-N03 in addition to completed B01. Consult the exact frozen
configs and queue dispatch reports; this does not authorize B06 or held P18.
Four identical TP1 replicas use GPUs4-7 and share the original pinned BF16
checkpoint. The 73 queued jobs cover 79,815 cases across24 additional settings;
counts include completed jobs and native dataset-specific/sharded runs.

P03/P07/P08 use43 disjoint source-order shards and offline global metrics;
P23-P26 use11 approved description shards and one full-task native Mol ROUGE
calculation per task. Exact-plan approval is in
`configs/local_description_execution_approval.json`; queued description jobs
must use their gated executor. P43 uses three exact DrugBAN test sets and a
separately frozen one-token Yes/No conditional-likelihood adapter for native
AUROC/AP. Never use sampled hard labels as ranking scores or tune thresholds.
N01-N03 retain full released DNA windows and native source question scaffolds;
permissive native continuation scoring and strict final-label diagnostics
remain separate. These zero-shot adaptations do not reproduce trained heads
or specialist representations. All permits were reviewed before dispatch;
no OpenAI calls, paid inference, training or flagged-request transfer occurs.

The optional16,384-output-token reasoning condition is proposed only in
`configs/proposed_long_reasoning_protocol.json`. A user answer is still pending;
it must not be run without affirmative authorization. Existing4,096-token
runs continue unchanged. Preserve all outputs, including truncated or invalid
responses, and their native denominators.

`scripts/update_executed_interpretations.py` appends completed whole-task
interpretations while preserving every original catalog/preparation record
and the frozen B01 record. Do not use the old destructive interpretation
generator. Explanation support remains unassessed independently of outcome
scores. Public pretraining exposure remains unknown.

On October 16, after being told that GitHub now reports this repository as
public and that the private-only uploader blocked the prepared examples, the
user explicitly instructed: "prepare everytying publicly". Public publication
of this evaluation project's reports, code, permitted source/data records and
saved trajectories to `Some-random/bio-evaluation` is now authorized. This
supersedes the earlier private-destination restriction. Verify the exact
repository identity, actual visibility and push permission before publishing;
record the real visibility rather than asserting that it remains private.
The earlier exclusions for model weights, credentials, environments, caches
and unrelated Affibody data remain in force. This changes publication only,
not frozen inference protocols, biological input reviews or compute limits.

On October 18, 2026 Pacific time, the user explicitly requested increasing the
limit behind truncated answers, authorized simple parsing fixes or leaving
unrecoverable outputs invalid, and authorized dropping problematic BioReason
evaluations. This authorizes a **prospective 16,384-token output budget** for
all not-yet-dispatched cases of the retained active tasks, replacing the previous
4,096-token budget for those future calls. The existing 65,536-token server
context accommodates the reviewed inputs plus this output budget; no larger
input context or model change is required. Keep every completed or ambiguous
old call immutable and never selectively regenerate failed/truncated answers.
Freeze the exact undispatched cohort after a clean drain, preserve per-case
budget/provenance, and explicitly label combined task results as a mixed
4K/16K-budget continuation rather than a uniform-16K condition or matched paper
replication. The earlier proposed whole-case 16K rerun remains unexecuted; the
current instruction is to finish the remaining work without duplicating old
calls. Other prompts, sampling settings, inputs and native metric formulas
remain unchanged. The ceiling remains eight GPUs.

Archive BioReason/Bio-posttrain settings N01–N05, P28 and P29 from the main
advisor-facing view and stop further P28/P29 dispatch after outstanding calls
drain. Retain their original catalog entries, raw outputs, scores and audits.
Do not replace the native scorers with favorable diagnostics or silently omit
invalid cases from retained tasks. Formatting-only parser revisions must be
separately named, frozen before application, tested on synthetic examples and
reported against the same full denominators; ambiguous/absent final answers
stay invalid. No held-out answer may guide an extraction rule. All unrelated
execution holds and biological input reviews remain unchanged.

On October 19 Pacific time, the user requested implementing the audit repair
plan. Offline rescoring of existing outputs may proceed under separately named,
frozen extraction or compatibility corrections, preserving all original scores,
raw outputs and full denominators. The immediate scope also includes a small
synthetic/permitted-development output-delivery pilot with the same Qwen
checkpoint, reasoning enabled and a 16,384-token cap. A synthetic format check
does not establish biological performance or authorize selective replacement
of failed cases. Proposed full-task reruns remain separate experiments requiring
a reviewed, frozen protocol; never splice their results into historical runs.

The user also specifically authorized configuring the documented OpenAI
`safety_identifier` and testing a few neutral requests. A single persistent
opaque end-user identifier is stored privately outside this repository and
attached by `scripts/openai_request_identity.py`; never rotate it to bypass
restrictions. Three neutral smoke tests completed successfully. This narrow
test authorization does not resume OpenAI benchmark inference, remove the
biological policy hold, or authorize retrying the flagged material. Credentials
and the private identity configuration must not be published.

The October 19 scorer repair is complete for P12/P14/P15. Consult
`reports/SCORER_COMPATIBILITY_REPAIR_2026-10-19.json` and
`results/scoring_corrections/`, alongside the original failed attempts. Their
full AP/Fmax remain undefined because invalid confidence vectors remain.
The original scoring watcher's failed statuses are historical and must not
be described as a still-unrepaired software crash for these three tasks.

A single P13 offline recovery watcher is active under
`.local/evaluation_revision_2026-10-18/scoring/null_equivalence_recovery_v1/p13_watcher_v2/`.
Read its `status.json` before acting. It waits for the original scoring attempt,
skips a successful original, and permits exactly one separately named recovery
only for the verified null/empty compatibility defect. Do not start a duplicate.
It exports new score metadata for the existing report collector, but does not
itself push GitHub changes. Subsequent reporting should refresh and publish the
decision table and new correction artifacts when this task becomes terminal.
The synthetic delivery pilot completed 12/12 checks and released its GPU;
this establishes simple format delivery, not biological predictive performance.

On October 19, the user clarified again that finishing the seven-setting
continuation does not finish the full catalog. Continue permitted work across
the 57 retained settings; the seven archived BioReason settings stay archived.
The original P13 compatibility recovery is now terminal and published alongside
P12/P14/P15; consult the correction report rather than restarting its watcher.
The current continuation work is recorded under
`.local/catalog_resume_2026-10-19/`. It includes recovered P36 subset evidence
(59 raw responses, not a full benchmark), further source recovery, a separately
frozen 12-case GFP validation delivery pilot, and preparation of a separate
uniform-16K B08 protocol. Job 242190 requests one A100 for the validation pilot;
read its runtime status and Slurm state before any further launch. No validation
labels are used or scored. This does not authorize selective retries, changes to
frozen historical runs, held tasks, new head training, or OpenAI benchmark calls.

The user reaffirmed hourly progress updates for the resumed work. The active
scheduler is `.local/hourly_evaluation_updates/catalog_2026-10-19/`, with a
top-of-hour cron entry queuing this conversation. It covers the full retained
catalog, uses Pacific display times, and does not automatically disable when
one batch or pilot finishes. The older seven-task scheduler state remains
disabled historical evidence. Consult the new schedule receipt/state/history;
do not install duplicate schedulers or revive the old batch-specific updater.

On October 19 at midday, the user challenged the estimate that counted the
33,701-case proposed rerun list as remaining catalog work. Keep these scopes
separate: uncompleted catalog settings, offline corrections to saved outputs,
and optional fresh full-task repetitions. The proposed B08/P42/B07/P16/P07
reruns have not been launched and are not an active remaining-case queue.
Do not quote their size or extrapolate the four-request development pilot as
the completion time for the full catalog. Prioritize explaining and advancing
the unfinished catalog work; retain existing results and use saved outputs for
offline repairs wherever possible.

The October 19 follow-up review requires focused offline P36/P08 diagnostics,
P12–P15 failure taxonomy with same-case reference baselines, and strict original
case/run/request provenance in the historical extraction tool. Preserve the
original metrics. The shared synthetic pilot is not a full-run readiness gate.
Use `configs/task_specific_delivery_gates_2026-10-19.json` and its report for
task-specific review requirements. No optional full-task repetition is started
by that configuration. The real GFP development pilot finished 12/12 calls,
with ten numeric final answers and two truncated empty finals; it did not pass
complete-delivery requirements. Its GPU was released after completion.

The user then requested identifying stable evaluation tasks for GPT-6-luna versus
Qwen3.8 comparisons. Offline preparation now records exact archived Qwen
conditions, case/request/response hashes and matching scorer references in
`reports/GPT6_LUNA_QWEN_COMPARISON_PLAN_2026-10-19.md` and the proposed config.
Start with the 279 LitQA2/SuppQA cases for delivery reliability; do not replace
their replay baselines with historical headline scores. This preparation made
no new inference calls and did not change the recorded OpenAI account-scope
hold. The user has been asked whether the appeal received a response. No answer
or provider clarification has been recorded yet. Preserve the two held B01
cases, flagged-task holds, original Qwen generations and all full denominators.

The user subsequently said "let's go for this openai eval" and supplied a
specific execution review. This authorizes the new, narrowly reviewed comparison
and its independent development checks, including GPT-6-luna and GPT-6.1 Sol.
It does not authorize retrying the previously flagged P18 traffic, restoring
held B01 cases, or broadly resuming the old all-catalog OpenAI job. Preserve the
old global disabled authorization as historical state; use a separately hashed,
case-scoped authorization with the current user instruction and input review.
Do not claim a provider appeal response or resolved warning that was not given.
The initial 279 cases remain LitQA2/SuppQA with their archived Qwen baselines.
P03 is a committed second stage with its own development/input checks; vision
is separate. Actual dispatch must pass isolation/leakage tests and the relevant
development delivery check, retain the existing stable safety identifier, and
stop new submissions on a provider policy/access rejection. Score only after
predictions lock. Keep the agent's recorded spending guard and actual usage
ledger explicit; no new training, selective retries or larger GPU allocation.

The scoped OpenAI comparison is now actually executing under
`.local/comparison_execution_2026-10-19/`. All four independent 12-case QA/P03
development delivery panels passed without biological correctness scoring.
Both 279-case QA model conditions are closed and scored: Luna B01 97/197,
B03 44/82; Sol B01 112/197, B03 46/82. Native and strict scores agree and all
558 responses are normally finished, parsed and error-free. The Qwen replay
baselines remain 77/197 and 31/82; they were not regenerated. Luna's full
2,773-case P03 condition is running. Sol P03 has not been dispatched: the user
was asked asynchronously about its conservative $125 ceiling, exceeding the
agent-imposed initial $50 guard. No approval is recorded; elapsed time does
not authorize it. The user then asked why Sol was included and what the task
means; this was a clarification request, not budget approval. Sol is an extra
GPT-6.1 reference model from the supplied review; the original requested
comparison was Luna versus Qwen. Continue Luna and retain Sol P03 as pending.
Existing held cases and the old global disabled scope stay held.

Read `control/status.json`, `analysis/publicqa_scoring_status.json` and
`analysis/localization_scoring_status.json` under that execution directory.
The singleton read-only runtime monitor and separate one-attempt offline
scoring watchers are already active; do not duplicate inference or scoring.
Current publication state belongs in `publication_watcher/status.json` and
the catalog publication receipt, not in stale aggregate reporting files.

Provider responses echo the private safety identifier and contain opaque
encrypted state. Preserve exact originals and locks locally. Public exports
must redact non-null safety_identifier, encrypted_content and legacy user
metadata, preserve final answers, and carry original/public hash mappings.
The early public archives were corrected at current HEAD; older Git history
remains unchanged and contained this identifier metadata, not API credentials.
Do not rotate the stable identifier or rewrite Git history to hide this issue.
Use the reviewed version-2 privacy export and its pinned helper; response
hashes in original locks refer to private original bytes, not redacted files.

On October 19 Pacific time, the user explicitly instructed: **"just do luna now please"**. Continuing OpenAI comparison inference is now **GPT-6 Luna only**. Preserve the already completed GPT-6.1 Sol QA/development outputs and scores, but do not launch any further Sol inference; Sol P03 was not dispatched. Continue the existing Luna P03 run. `configs/openai_comparison_model_scope_2026-10-19.json` is the prospective model-scope override. It does not alter frozen v2 protocols, answer policy, candidates, original generations or prediction locks. All flagged-task holds, held B01 cases, identity and no-retry rules remain unchanged.

The user subsequently requested downloading the unfinished official assets
together and finding published evaluation implementations for missing pieces.
Parallel source/data/evaluator acquisition is active under
`.local/source_acquisition_2026-10-19/`. This includes public evaluation
checkpoints, with no new training or model forwards. Check the per-worker
manifests and processes before launching duplicate transfers. Preserve exact
publisher identities, original splits and hashes; distinguish publisher-verified
digests from newly calculated local digests. Store inputs and references
separately before any future solver dispatch. Do not publish downloaded model
weights or credentials. Source recovery is authorized without another general
permission question; gated terms and access challenges must not be bypassed.

The user's stated research purpose is recorded. Do not treat an interrupted
review as a finding that every case in a benchmark is prohibited. Identify
previously rejected material and keep it separate; metadata-first preparation
and independent review of other cases may continue. This does not authorize
rephrasing, forwarding or rerunning the previously flagged requests through
Qwen or another provider. Keep actual execution reviews and frozen per-case
scopes distinct from permission to download a source corpus.

During this new acquisition work, an independent B06 input review (excluding
its previously identified held case before content inspection) was again
interrupted by an automatic biological-safety check. Preserve
`.local/source_acquisition_2026-10-19/b06_review/review_receipt.json` and
`review_interruption.json`; completed candidate records are not dispatch
approval or full-benchmark completion. A subsequent GFP-only P18 metadata/
contract preparation attempt also received an automatic biological-safety
block, recorded under `p18_gfp_candidate/review_interruption.json`. Exact
triggers were not returned. Do not retry or reroute those interrupted actions.
These events do not classify every benchmark case or GFP research as unsafe;
other already-running ordinary source/evaluator downloads continue.

The user subsequently changed evaluation progress messages from hourly to
**every two hours**. Keep the existing full-catalog scheduler and history under
`.local/hourly_evaluation_updates/catalog_2026-10-19/`; the historical directory
name is unchanged. It now reports at even-numbered Pacific hours, with the next
scheduled message at 6 PM PDT on October 19. This supersedes earlier hourly
reporting instructions, does not stop ongoing work, and does not change any
inference authorization, held cases or benchmark protocols.

The user then explicitly requested continuing recovery of PFArena, missing
SlideVQA images and paper-specific artifacts. Further source recovery is active
under `.local/source_recovery_round2_2026-10-19/`; the existing source observer
and two-hour progress schedule read its aggregate receipts. Check current
workers before duplicating downloads. This authorizes ordinary author-release,
history, supplement and public-reproduction searches and downloads, including
missing evaluation-tool vendor assets; it does not authorize gate bypass,
accepting access terms for the user, new inference, training, arbitrary native
artifact substitutes, or retrying interrupted biological reviews. A 401 from
PFArena is an external access requirement, while available source/code and
other tasks should continue independently. Preserve the original acquisition
receipts and distinguish exact original images from current author renderings.

The follow-up recovery acquired all five missing Proteo-R1 vendor dependencies
with full publisher SHA256 or multipart-ETag verification, plus 83 source/fixture
files. Missing SlideVQA pages now have processed copies from a public academic
corpus; preserve their distinct encoding condition and the original acquisition.
The user enabled PFArena dataset access and supplied an existing private token
file for authenticated acquisition. Read that credential only privately at
runtime; do not copy it into this repository, logs or public artifacts. Current
authenticated corpus progress belongs under the round-two PFArena receipts.
This resolves an access prerequisite, not any inference/input-review hold.

Authenticated PFArena acquisition is now terminal: all 772 pinned dataset
files (1,825,005,675 bytes) passed publisher digests; previous 401 evidence is
preserved. All 300 missing SlideVQA page identities have decoded processed
copies, with image-encoding provenance kept separate. Read the round-two
completion receipts and follow-up report before treating a download as pending.
Exact native protocol/input compatibility and historical-byte identity remain
separate checks; no new inference was performed by this recovery.
