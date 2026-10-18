# Results at a glance

Snapshot: 2026-10-16 06:49 PDT. Fixed local Qwen3.8-27B baseline; 5 of 57 main settings have completed evaluations of their declared scope. This does not mean full paper replication. Finished shards and incomplete runs are excluded below.

BioReason, BioReason-Pro and Bio-posttrain settings are set aside from the main comparison. [Archived settings and original records](ARCHIVED_EVALUATIONS.md) remain available; the structured report preserves all original scores and denominators.

These are contextual comparisons: the local baseline is zero-shot; BioT5+/medical systems use task training. LAB references below use the public-set GPT-5.2 column; prompt/decoding/repeat differences remain. B01 covers 197/199 public cases with two held before inference. No superiority or significance claim follows. Generated-answer output caps in this snapshot: 4,096 tokens; P43 instead uses a prespecified one-token conditional likelihood score. Paper ± values preserve reported dispersion; its definition and repeat counts are not always established.

| Setting | Local score | Published reference | Qualification |
|---|---|---|---|
| [B01 LitQA2*](../results/runs/qwen38_27b_litqa2_replay_2026-10-16/scores.json) | accuracy 39.1%; precision 41.0%; coverage 95.4% | GPT-5.2: accuracy 45.7%; n=199; [Table 1](https://arxiv.org/html/2606.00902v1) | Public release 197/199; one seeded run, no tools; published decoder/repeats differ. 197/199 public cases; two held before inference. Original LAB paper includes private cases and means over three runs. |
| [B03 SuppQA](../results/runs/qwen38_27b_b03_slurm_replay_2026-10-16/scores.json) | accuracy 37.8%; precision 39.2%; coverage 96.3% | GPT-5.2: accuracy 48.8%; n=82; [Table 1](https://arxiv.org/html/2606.00902v1) | Public release 82/82; one seeded run, no tools; published decoder/repeats differ. |
| [B04 FigQA](../results/runs/qwen38_27b_b04_slurm_replay_2026-10-16/scores.json) | accuracy 72.4%; precision 72.8%; coverage 99.4% | GPT-5.2: accuracy 36.5%; n=181; [Table 1](https://arxiv.org/html/2606.00902v1) | Public release 181/181; one seeded run, no tools; published decoder/repeats differ. |
| [B05 TableQA](../results/runs/qwen38_27b_b05_slurm_replay_2026-10-16/scores.json) | accuracy 88.1%; precision 90.0%; coverage 98.0% | GPT-5.2: accuracy 36.9%; n=244; [Table 1](https://arxiv.org/html/2606.00902v1) | Public release 244/244; one seeded run, no tools; published decoder/repeats differ. |
| [P03 Subcellular localization — DeepLoc](../results/runs/qwen38_27b_p03_full_test_slurm_2026-10-16/scores.json) | accuracy 26.1% | ProtST-ESM-1b: fixed encoder.accuracy 82.0%; full model tuning.accuracy 78.73%; [Table 2, printed p.6](https://proceedings.mlr.press/v202/xu23t/xu23t.pdf) | Declared local variant; input, training and scoring qualifications in linked result and JSON. |

\* Incomplete benchmark coverage or scoring. Case counts and parsing details remain in the [structured report](RESULTS_AT_A_GLANCE.json).

Genuine source blockers: [P19/P20/P21/P22](remaining_native_source_recovery_2026-10-15.md): PFArena official release found; publisher dataset access is gated and original assay/case review remains pending. [Publisher release](https://huggingface.co/datasets/AMix-Bio/PFArena/tree/5be3973dd45a9d7d33572f016be18f8ef941f2ff).

Outcome scores do not validate explanations or identify internal reasoning; public pretraining exposure is unknown. Undefined metrics remain undefined. [Full coverage/provenance](LOCAL_SUITE_RESULTS.md) · [Structured concise report](RESULTS_AT_A_GLANCE.json).
