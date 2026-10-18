P16 is prepared from the original ProtST Reaction release: 5,651 numeric LMDB test
keys, all original complete sequences, integer labels0–383 and a fixed384-class
global ontology. The publisher archive matches MD5
`d1c20341616ad3890349247017a34d68` and SHA256
`ec4c8cc70cebca87165f6aeca10f319762bbe9ae0a75b7c8bdd6bb4f40967a80`.
Only the test LMDB is opened. No training/dev examples, shots or trained heads
are used. All prepared prompt/reference rows were reconciled against that LMDB.

The class table and code are pinned to ProtST commit
`db53a76ed2430eb66dd9c8134ace99fd60980fb3`. All four original tables have exactly
IDs0–383 in order. Their Git blob hashes match the original tree. Each class ID
joins to one EC number, source name, alternative names, hierarchy and comment.
Every bare-name field equals `name + ' ' + alter_name`; the pretraining-name field
adds `FUNCTION: `; the complete pretraining-description adds ` ' ' + comment`.
No names, synonyms or comments are shortened, normalized or inferred from test
labels. The source LMDB contains integer labels and no separate EC field, so the
author's jointly released loader/evaluator/table contract defines the mapping;
this is not an independent biochemical reconstruction of its annotations.
See the pinned [class tables](https://github.com/DeepGraphLearning/ProtST/tree/db53a76ed2430eb66dd9c8134ace99fd60980fb3/data/zero_shot_classification),
[dataset loader](https://github.com/DeepGraphLearning/ProtST/blob/db53a76ed2430eb66dd9c8134ace99fd60980fb3/protst/dataset.py#L137)
and [zero-shot evaluator](https://github.com/DeepGraphLearning/ProtST/blob/db53a76ed2430eb66dd9c8134ace99fd60980fb3/script/run_zero_shot.py#L99).

Native ProtST selects one TSV and field per run, encodes that text independently
for each class with max_length128/truncation, normalizes protein/text embeddings,
then takes the highest scaled dot product. The three template styles are
alternatives, not a prompt ensemble. The separate supervised ensemble computes
`alpha * zero_logits + supervised_logits`, or the corresponding sum after both
softmaxes, followed by argmax; its default alpha is1. It requires a supervised
checkpoint and is not used here. See the pinned
[ensemble implementation](https://github.com/DeepGraphLearning/ProtST/blob/db53a76ed2430eb66dd9c8134ace99fd60980fb3/script/run_supervised_with_zero.py#L176).
The native protein model also has an input-length truncation branch; the Qwen
baseline retains all raw sequences, including the longest1,119 residues.

The closest published full-description contextual reference is **21.91%**
accuracy, rounded as printed in [ProtST Table11, printed page15](https://proceedings.mlr.press/v202/xu23t/xu23t.pdf#page=15).
The **29.85%** value uses the pretraining-name variant. The README's example uses
bare names, another separate variant. Qwen generates a class ID from the full raw
sequence and all complete class descriptions jointly; native ProtST uses learned
protein/text embedding similarity and separately truncated descriptions. These
are explicit representation, architecture, context and pretraining differences,
not a matched reproduction or evidence about the model's internal computation.

The frozen input places the objective and all384 full source descriptions before
the varying complete sequence, allowing reuse of the common prefix per replica.
The fixed context is44,542 Qwen tokens. The largest complete input by bytes has
45,208 actual chat-template tokens without truncation; with4,096 output tokens it
uses49,304 of262,144 tokens. All5,651 input byte lengths were checked, and the
conservative bound using one byte per BPE token plus1,024 chat/control tokens and
4,096 output tokens is150,292. This proves every preserved input fits. The audit
is CPU tokenizer-only; no model inference is involved. Full detail and source
digests are in `reports/catalog_reaction_{preparation,validation,context_validation}.json`.

The offline scorer uses native top1 accuracy with the original global IDs.
Every test row stays in the denominator; invalid/missing final classes count
incorrect. It locks all raw predictions before opening gold references and
retains invalid, transport, missing and truncation counts. Accuracy validates
agreement with source annotations; explanation support remains null and public
pretraining exposure remains unknown.

The prospective execution plan has six fixed consecutive shards of at most1,024
cases, on GPUs6,4,7,5,6,4 / ports8027,8029,8028,8026,8027,8029. It retains the pinned
BF16 checkpoint, seed42, concurrency4, medium thinking and4,096 total output
tokens. Every config remains `execution_authorized:false`. Aggregate-only configs
have an invalid offline endpoint. Exact union/provenance checks precede one full
native accuracy call, without averaging shard metrics or resampling.

After root review, activate without editing frozen configs:

1. Verify `reports/local_reaction_shard_plan.json`, all six config hashes, the
   full and shard input reviews, full test-ID coverage, frozen native class
   context/scorer/code/source/reference hashes, and context-fit audit.
2. Create `configs/local_reaction_execution_approval.json` once, with
   `execution_authorized:true`, the exact `plan_sha256`, pinned `model` and
   `model_revision`, `generation_sha256` from canonical JSON SHA256 of the frozen
   generation dict, `approved_task_ids:["P16"]`, and `approved_config_sha256`
   mapping each approved project-relative shard config path to its exact digest.
   Keep this approval record unchanged; every completion/provenance records it.
3. Then enable P16 in central `configs/local_model.json`, preserving holds and
   existing authorizations. The unchanged generic runner does not read the new
   prospective authorization flag, so use only the gated Reaction executor.
4. Append plan shards to their declared GPU queue as
   `{"config":"<config_file>","executor":"scripts/execute_local_reaction_shard.py"}`.
   Do not queue aggregate configs. The standalone equivalent is
   `.venv/bin/python -u scripts/execute_local_reaction_shard.py --config <config_file>`.
5. Start the offline watcher with
   `.venv/bin/python -u scripts/aggregate_local_reaction_shards.py --watch --plan reports/local_reaction_shard_plan.json`.
   Failed shards explicitly block the aggregate. Shard scores/CSV rows stay
   `task_shard_only`; only the exact completed union receives the full-test scope.

No P16 task authorization, approval record, queue entry or model request is
created by preparation. Source code uses Apache2.0; the downloaded data archive
has no separate license file, so an independent dataset-license claim is not made.
