P23–P26 are prospective local zero-shot annotation-description baselines, covering
3,494, 1,601, 1,400 and 2,633 source-export test cases respectively. Preparation
creates eleven consecutive source-order shards of at most 1,024 cases. Assignment
cycles through GPUs6,4,7,5 at ports8027,8029,8028,8026. The same pinned BF16 model,
seed42, concurrency4, medium thinking and total4,096 output tokens are retained.

All configs and input reviews remain `execution_authorized:false`. A completed
input review does not activate inference. The executor requires a separate exact
plan approval record, and the unchanged runner independently checks the central
task authorization and the actual local server identity. Aggregate-only configs
use an invalid offline endpoint and cannot dispatch through that runner.

The supplied information is the original per-instance instruction and complete
decoded amino-acid sequence inside the pinned Alpaca template. Source special
token decoding, removal of the native512-token encoder limit, zero-shot Qwen and
the absence of task training are declared adaptations. All unique instruction
templates concern annotation, localization, catalytic reaction descriptions,
domains/motifs or general properties. No tool, retrieval, target description,
teacher explanation, sequence optimization or experimental protocol is supplied.

ROUGE uses only the separate flat gold description. The pinned official HF
implementation uses rouge-score0.1.2, default tokenization without stemming,
all four ROUGE types and the native BootstrapAggregator mid.fmeasure. The scoring
RNG seed is fixed at42 and restored afterward. The full task scorer locks all
combined raw predictions before opening the reference file, then computes the
native metric once over the exact complete ordered union. It never averages shard
bootstrap metrics. Annotation word overlap is separate from explanation support,
which remains unassessed. The pinned BioT5+ wrapper computes `references_new` but
passes `[gold,decoded_input]` pairs to ROUGE; these jobs use the native Mol gold-only
protocol and do not claim exact BioT5+ paper metric equivalence.

After root review, activation requires these concrete steps:

1. Verify `reports/local_description_shard_plan.json`, its eleven config hashes,
   four full input-only reviews, source/test-list/reference hashes, and all frozen
   script/metric hashes. Keep this plan and every prepared config unchanged.
2. Create `configs/local_description_execution_approval.json` with
   `execution_authorized:true`, `plan_sha256` equal to the actual frozen plan
   digest, `model`, `model_revision`, `generation_sha256` equal to canonical JSON
   SHA256 of the frozen generation dict, `approved_task_ids`, and
   `approved_config_sha256` mapping every approved shard's project-relative
   `config_file` to its frozen `config_sha256`. Add reviewer/date metadata if
   desired. Create this record once before the first job and keep it unchanged;
   its digest is retained in every shard completion and aggregate provenance.
3. Only after exact-plan approval, record the approved task IDs in the central
   `configs/local_model.json`, preserving existing holds/authorizations. Replica
   configs cannot authorize a task. The unchanged generic runner does not inspect
   the new prospective authorization flag; use only the gated description
   executor below and enable central scope only after approval.
4. Append each approved plan shard to its declared GPU queue as
   `{"config": "<config_file>", "executor": "scripts/execute_local_description_shard.py"}`.
   The standalone equivalent is
   `.venv/bin/python -u scripts/execute_local_description_shard.py --config <config_file>`.
   Do not enqueue an aggregate config or use the generic catalog executor.
5. Start the offline watcher with
   `.venv/bin/python -u scripts/aggregate_local_description_shards.py --watch --plan reports/local_description_shard_plan.json`.
   It waits for every shard of each task to finish with both exit codes0. Failed
   shards block that aggregate explicitly. No worker or watcher resamples outputs.

Full score/completion artifacts contain exact test-ID union validation, source
shard hashes, per-server process/GPU identity and parallel replica metadata.
Shard scores/CSV rows are always labeled `case_scope:task_shard_only`; they are
partial diagnostics and cannot be used as full-task results. Public benchmark
pretraining exposure remains unknown.
