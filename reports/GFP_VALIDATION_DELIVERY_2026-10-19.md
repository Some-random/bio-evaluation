# GFP validation: completed answer-delivery pilot

Completed October 19, 2026, **12:14 PM PDT**. All **12/12** planned requests returned and were retained. **10/12** finished normally with a finite numeric final; **2/12** reached the 16,384-token cap with an empty final. There were **zero transport/server errors**. The two truncations and two empty finals are the same two cases.

This is an official TAPE **validation-split delivery check**, not a fluorescence accuracy evaluation. No reference fluorescence values were supplied to the model or scored. The checkpoint was Qwen3.8-27B BF16 with reasoning enabled, one A100 and four concurrent requests.

**The task-specific delivery gate did not pass.** Raising the allowance to 16K did not ensure a final answer for all twelve validation cases. This run does not establish a reliable full 27,217-case numerical-prediction procedure; even twelve successes would not certify such reliability. The local completeness policy and handling of residual failures must be fixed before a new full run. The historical P07 generations and metrics remain unchanged.

The calls ran from 11:48:16 AM to 12:14:09 PM PDT (about 25 minutes 53 seconds, excluding runtime setup), producing 161,268 completion tokens. Per-case latency and token usage are retained in the manifest. This small four-request-concurrency experiment is not an estimate of eight-GPU production throughput.

[Complete manifest and per-case records](../results/development_pilots/qwen38_27b_gfp_validation_16k_2026-10-19/snapshots/20261019_1214_PDT/manifest.json) · [Original completion receipt](../results/development_pilots/qwen38_27b_gfp_validation_16k_2026-10-19/snapshots/20261019_1214_PDT/completion.json) · [Frozen source code and inputs](../results/development_pilots/qwen38_27b_gfp_validation_16k_2026-10-19/snapshots/20261019_1214_PDT/code/)

| Validation case | Finish | Delivery gate | Output tokens | Raw response |
|---|---|---|---:|---|
| fluorescence:valid:698 | length | Fail: empty final at cap | 16,384 | [JSON](../results/development_pilots/qwen38_27b_gfp_validation_16k_2026-10-19/snapshots/20261019_1214_PDT/responses/a3aebb78b39a59c7f21ff9a47b806ca3db58c7a9dae8a99ef8a3a86792e08916.json) |
| fluorescence:valid:1332 | stop | Pass | 11,987 | [JSON](../results/development_pilots/qwen38_27b_gfp_validation_16k_2026-10-19/snapshots/20261019_1214_PDT/responses/7b718b0f328eb24b517cabd42375796ebf684e002e16e00f94139c04dd3b30e1.json) |
| fluorescence:valid:1547 | stop | Pass | 14,189 | [JSON](../results/development_pilots/qwen38_27b_gfp_validation_16k_2026-10-19/snapshots/20261019_1214_PDT/responses/269a5cc14ee1d9a7fe594cd44957f7efa35742bfadccf0235edea17a04b8d541.json) |
| fluorescence:valid:1607 | stop | Pass | 15,260 | [JSON](../results/development_pilots/qwen38_27b_gfp_validation_16k_2026-10-19/snapshots/20261019_1214_PDT/responses/14ffad2782de83b741fe758fbb7de6a720701b988439102d2d8c9257d90c93ff.json) |
| fluorescence:valid:1793 | stop | Pass | 13,982 | [JSON](../results/development_pilots/qwen38_27b_gfp_validation_16k_2026-10-19/snapshots/20261019_1214_PDT/responses/e33ac3fb6252a11115fd5f4b44ba875642b53b15db1219bbfcc909b4fbecd831.json) |
| fluorescence:valid:2090 | stop | Pass | 13,621 | [JSON](../results/development_pilots/qwen38_27b_gfp_validation_16k_2026-10-19/snapshots/20261019_1214_PDT/responses/17b1404cac1349384c8b6a9cf456754254d51651eabd54ea0cbca4995f53e6ea.json) |
| fluorescence:valid:2764 | stop | Pass | 10,367 | [JSON](../results/development_pilots/qwen38_27b_gfp_validation_16k_2026-10-19/snapshots/20261019_1214_PDT/responses/f4cd9f87f98836ba1434ea2f4c4acc75c8fb8b181aeee62fda0f2e5c4a6c1b46.json) |
| fluorescence:valid:3514 | stop | Pass | 6,717 | [JSON](../results/development_pilots/qwen38_27b_gfp_validation_16k_2026-10-19/snapshots/20261019_1214_PDT/responses/bc57e7f83f94583d786b046b81d6612803c09052af037c4168bacc9dcf3626be.json) |
| fluorescence:valid:4122 | length | Fail: empty final at cap | 16,384 | [JSON](../results/development_pilots/qwen38_27b_gfp_validation_16k_2026-10-19/snapshots/20261019_1214_PDT/responses/23e0db1d19e4c67643a3cf5b588e11484b20b6d0af77f1043fce064f674be117.json) |
| fluorescence:valid:4225 | stop | Pass | 15,015 | [JSON](../results/development_pilots/qwen38_27b_gfp_validation_16k_2026-10-19/snapshots/20261019_1214_PDT/responses/da17ffec3321a2d67fdc0ef8c802a305b42d1a8231f67ce879d4ef04410607f1.json) |
| fluorescence:valid:4253 | stop | Pass | 12,887 | [JSON](../results/development_pilots/qwen38_27b_gfp_validation_16k_2026-10-19/snapshots/20261019_1214_PDT/responses/63ffc5d970cc8fb2afd30af1ff172b02887e0311f8172b41c527a11b1874cab9.json) |
| fluorescence:valid:4812 | stop | Pass | 14,475 | [JSON](../results/development_pilots/qwen38_27b_gfp_validation_16k_2026-10-19/snapshots/20261019_1214_PDT/responses/d636a8c74cb7db9d74f203b0d2244282806808be0e72fab81b7b187e543cdc0e.json) |

Every request/response pair is hash-checked against the frozen input and saved status. All outputs, including failures, remain in the denominator; no selective retry was performed.

The earlier [four-response snapshot](../results/development_pilots/qwen38_27b_gfp_validation_16k_2026-10-19/snapshots/20261019_1200_PDT/manifest.json) remains unchanged. [Task-specific future-run requirements](TASK_SPECIFIC_DELIVERY_GATES_2026-10-19.md).
