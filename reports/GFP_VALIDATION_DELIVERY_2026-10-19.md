# GFP validation: answer-delivery pilot

Immutable snapshot: October 19, 2026, 12:00 PM PDT; latest included response finished at 11:58:27 AM PDT. This is a twelve-case **validation-only** format test, not a benchmark accuracy result.

The model is the pinned Qwen3.8-27B BF16 checkpoint, with reasoning enabled and a 16,384-token output cap. Each request uses a complete 237-amino-acid GFP sequence from the official TAPE validation split. Reference fluorescence labels were not supplied or scored.

| Snapshot measure | Count |
|---|---:|
| Planned validation cases | 12 |
| Finalized raw responses included | 4 |
| Normal finish with a parseable finite-number final | 3 |
| Output-cap finishes | 1 |
| Empty final answers | 1 |
| Transport/server errors in these four responses | 0 |

The truncated response and empty final refer to the same case. The other eight planned cases are outside this snapshot; this is not a count of missing or failed requests. The snapshot is preserved as an intermediate record even when later responses arrive.

Passing this delivery check establishes only that a normal stop produced a number accepted by the frozen native P07 parser. It does not establish that the predicted number is biologically correct. All responses, including the failure, are retained. No selective retry or change to historical P07 outputs is part of this snapshot.

[Manifest and planned case identity](../results/development_pilots/qwen38_27b_gfp_validation_16k_2026-10-19/snapshots/20261019_1200_PDT/manifest.json) · [Source run manifest](../results/development_pilots/qwen38_27b_gfp_validation_16k_2026-10-19/snapshots/20261019_1200_PDT/run_manifest.json)

| Validation case | Finish | Final-answer delivery | Request | Raw response | Status |
|---|---|---|---|---|---|
| fluorescence:valid:698 | length | Failed: empty final at output cap | [JSON](../results/development_pilots/qwen38_27b_gfp_validation_16k_2026-10-19/snapshots/20261019_1200_PDT/requests/a3aebb78b39a59c7f21ff9a47b806ca3db58c7a9dae8a99ef8a3a86792e08916.json) | [JSON](../results/development_pilots/qwen38_27b_gfp_validation_16k_2026-10-19/snapshots/20261019_1200_PDT/responses/a3aebb78b39a59c7f21ff9a47b806ca3db58c7a9dae8a99ef8a3a86792e08916.json) | [JSON](../results/development_pilots/qwen38_27b_gfp_validation_16k_2026-10-19/snapshots/20261019_1200_PDT/case_status/a3aebb78b39a59c7f21ff9a47b806ca3db58c7a9dae8a99ef8a3a86792e08916.json) |
| fluorescence:valid:1332 | stop | Passed | [JSON](../results/development_pilots/qwen38_27b_gfp_validation_16k_2026-10-19/snapshots/20261019_1200_PDT/requests/7b718b0f328eb24b517cabd42375796ebf684e002e16e00f94139c04dd3b30e1.json) | [JSON](../results/development_pilots/qwen38_27b_gfp_validation_16k_2026-10-19/snapshots/20261019_1200_PDT/responses/7b718b0f328eb24b517cabd42375796ebf684e002e16e00f94139c04dd3b30e1.json) | [JSON](../results/development_pilots/qwen38_27b_gfp_validation_16k_2026-10-19/snapshots/20261019_1200_PDT/case_status/7b718b0f328eb24b517cabd42375796ebf684e002e16e00f94139c04dd3b30e1.json) |
| fluorescence:valid:1547 | stop | Passed | [JSON](../results/development_pilots/qwen38_27b_gfp_validation_16k_2026-10-19/snapshots/20261019_1200_PDT/requests/269a5cc14ee1d9a7fe594cd44957f7efa35742bfadccf0235edea17a04b8d541.json) | [JSON](../results/development_pilots/qwen38_27b_gfp_validation_16k_2026-10-19/snapshots/20261019_1200_PDT/responses/269a5cc14ee1d9a7fe594cd44957f7efa35742bfadccf0235edea17a04b8d541.json) | [JSON](../results/development_pilots/qwen38_27b_gfp_validation_16k_2026-10-19/snapshots/20261019_1200_PDT/case_status/269a5cc14ee1d9a7fe594cd44957f7efa35742bfadccf0235edea17a04b8d541.json) |
| fluorescence:valid:1607 | stop | Passed | [JSON](../results/development_pilots/qwen38_27b_gfp_validation_16k_2026-10-19/snapshots/20261019_1200_PDT/requests/14ffad2782de83b741fe758fbb7de6a720701b988439102d2d8c9257d90c93ff.json) | [JSON](../results/development_pilots/qwen38_27b_gfp_validation_16k_2026-10-19/snapshots/20261019_1200_PDT/responses/14ffad2782de83b741fe758fbb7de6a720701b988439102d2d8c9257d90c93ff.json) | [JSON](../results/development_pilots/qwen38_27b_gfp_validation_16k_2026-10-19/snapshots/20261019_1200_PDT/case_status/14ffad2782de83b741fe758fbb7de6a720701b988439102d2d8c9257d90c93ff.json) |

The manifest records SHA-256 digests for all copied requests, responses and statuses. Its twelve-case identity is checked against the frozen request-file digest; each included request payload matches that file. Source files and raw responses were copied unchanged.
