# Synthetic output-delivery pilot

Completed October 19, 2026 at 01:28 AM PDT: **12/12 fixed checks passed**. Each response stopped normally and returned a nonempty final answer; no truncations or request failures occurred. This generated **zero biological benchmark answers**.

Qwen3.8-27B, original BF16, vLLM 0.32.0; one dedicated A100; serial requests; 16,384 output-token allowance and 65,536-token context. Six toy interfaces were tested with short inputs (53–77 tokens) and long inputs (31,553–31,577 tokens). API token counts agree with corrected local counts.

| Output interface | Short input | Long input |
|---|---|---|
| One numeric scalar | Pass; 16.56 s | Pass; 10.88 s |
| Yes/No | Pass; 1.98 s | Pass; 2.55 s |
| Tagged answer choice | Pass; 2.26 s | Pass; 2.25 s |
| Integer class ID | Pass; 2.69 s | Pass; 4.39 s |
| Confidence JSON | Pass; 2.96 s | Pass; 4.14 s |
| Toy string-edit JSON | Pass; 3.06 s | Pass; 4.35 s |

The allocation lasted **00:12:57**. Cold loading, compilation and startup took **709 seconds** before readiness; the twelve request wall times sum to **58.06 seconds**. Repeated neutral padding and prefix caching can reduce work on later long requests, so these are not benchmark throughput or ETA measurements.

The first attempt entered the shared evaluation queue: one request was dispatched, no response was saved, and its outcome remains unknown. The dedicated run is a separately named development iteration with the same twelve payloads. The original tokenizer bookkeeping incorrectly counted two mapping keys; an independent input-ID audit corrected the counts. During dedicated-server startup, only its verified readiness-check process was paused/resumed to allow compilation/cache waits to finish. The server and frozen requests were preserved.

This checks answer delivery and simple formatting. Toy answers are supplied or trivial; it does not establish biological accuracy, reliability on real datasets, or establish that the full-evaluation configuration is ready. The protein check uses the native parser, which permits extra JSON keys; none appeared. Final answers and separate reasoning are archived, but answers are never recovered from reasoning.

[Machine-readable audit](OUTPUT_DELIVERY_PILOT_2026-10-19.json) · [Offline reproduction bundle](benchmark_assets/output_delivery_pilot_2026-10-19.tar.gz). The bundle includes all twelve raw requests/responses and a Python-only verifier; weights and credentials are excluded.
