# Frozen P29 execution proposal

All files below are frozen before inference. They contain15disabled source-order shards for14,872cases: ID6,989 in7shards and OOD7,883 in8shards, size1024 except final845/715. Global roundrobin is GPUs[1,2,3,4,5,6,7], repeated; GPU0 is absent. No model calls, queue changes or central task authorizations were performed by this proposal.

Plan `reports/local_posttrain_protein_shard_plan.json` SHA256:
`ba54d8bdafef53efd9d471eb2a777804ac6b0c20ddfe03e9e80ff1466347e26b`.

Disabled approval `configs/local_posttrain_protein_execution_approval.json` initial SHA256:
`91f7fa32ff11242003499d5ec8858b1735b9a53f7983101c16b6668e1fb5258c`.

Root-reviewed eight-GPU runner SHA256:
`de0c69b2eea33d618a7674791d6ae448fd8c086a7ba081e948dafdfdcaed4493`.

| Whole-split aggregate config | SHA256 |
|---|---|
| configs/local_posttrain_protein_p29_id_aggregate.json | c331d1384b1e497a6950a8f85bd3f0c4458674fb64e48cfdd0ff5f0ca3b610ab |
| configs/local_posttrain_protein_p29_ood_aggregate.json | c1a076cc381a86bd96dfa41f6441c1e9dfcc0bbe71c767cd242435ffabd50fbd |

Before activation, review `reports/POSTTRAIN_NATIVE_GAP_AUDIT.md` and `reports/catalog_posttrain_protein_preparation.json`. Native references union `go_pred_leaf` into curated targets while `go_pred` is supplied as context. This reference/input dependence can reward recovery or copying of supplied predictions; it does not isolate novel function inference. The fixed seed-context-only audit is native augmented F1 ID0.9842095347/OOD0.9893526590; curated diagnostic ID0.7012768060/OOD0.6316645518. These are offline input/reference measurements, not Qwen results or evidence about Qwen's internal computation. The same audit and caveats are frozen into full configs and global score outputs. Curated-only metrics stay separately named; native context remains complete.

Activation order, owned by root:

1. Verify the plan hash and all15 `config_file`/`config_sha256` pairs in `plan.shards`.
2. Authorize the separate exact-plan approval: set `execution_authorized=true`, `approved_task_ids=["P29"]`, and `approved_config_sha256` to the exact mapping from plan shards. Preserve its model, revision, generation hash, plan hash and incomplete-output policy. Do not edit per-shard configs, whose `execution_authorized=false` is part of the frozen prospective contract.
3. Add P29 to the central reviewed task scope only after exact approval. Queue only the gated executor below. The generic frozen runner does not enforce the separate exact-plan approval by itself.
4. Add each exact plan shard to its GPU queue using:

   ```bash
   .venv/bin/python -u scripts/execute_local_posttrain_protein_shard.py --config configs/local_posttrain_protein_p29_id_shard_000.json
   ```

   Replace the config argument with each existing exact `plan.shards[].config_file`; do not directly queue the generic runner or either aggregate config.

5. Start one offline watcher:

   ```bash
   .venv/bin/python -u scripts/aggregate_local_posttrain_protein_shards.py --watch --poll-seconds 30
   ```

Shard execution performs only label-free raw provenance/denominator accounting and writes `case_scope=task_shard_only`, `metrics={}`. Each original ID/OOD set is scored globally once after every shard for that split is terminal and its ordered union is exact. Global scoring locks all raw outputs and missing slots before labels, preserves every failure, uses the unmodified native extractor/ontology/uniform mean per-case GO score, records organism subgroups and separate curated-only diagnostics, and never averages shard metrics. Nonzero generation status remains nonzero in aggregate completion even when all-case offline scoring succeeds. A blocked split does not prevent the watcher waiting for the other split. No retries, resampling or test-guided changes are authorized.

Validation:14synthetic tests passed for exact native prompt/input allowlist, augmented versus curated references, hierarchy/extraction/continuation boundary, missing-case penalties and lock-before-labels, exact union, approvals, raw provenance, once-only global scoring and completed-artifact tamper rejection. Every prepared full input/review/reference/config/runner/source hash and all15exact disjoint slices were also verified offline.
