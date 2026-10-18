# vLLM concurrency measurements

Updated October 17, 2026, 10:04 PM PDT. Run state: **completed**.

The best completed point in the long-decode check is **32 concurrent requests**, reaching **661.98 output tokens/s** — **5.99×** the primary four-request baseline at the same server capacity. Each request has **192 synthetic input tokens** and 4,096 forced output tokens. The long-decode checks use one full concurrent batch per point. Production settings remain unchanged; longer inputs and P16 have not been validated by this test.

Dedicated **NVIDIA A100-SXM4-80GB** replica of **Qwen/Qwen3.8-27B**, original BF16, tensor parallelism 1; vLLM 0.31.0. Server context limit: 32,768 tokens. Checkpoint revision: `1d4bf0f2ff6012fd82039f2fa52739d0dd7c60c0`.

These are synthetic serving measurements, not biological evaluation scores. A custom Python standard-library client sends identical predetermined token-ID prompts across concurrency levels through `/v1/completions`, with `ignore_eos=true` and a fixed output-token count. Enabled production prefix caching is reset before every stage. Warmup is excluded from measurements.

Sampled decoding: `temperature=1.0`, `top_p=0.95`, `top_k=20`, `seed=42` (observed client config).

## Quick comparison: fixed total work

Each point processes the same 32 requests with 192 input tokens and 512 forced output tokens each. The original server capacity of four is measured first; a separate server with capacity 32 then runs the concurrency sweep.

| Server capacity | Client concurrency | Input / output tokens | Requests done / planned | Output tokens/s | Requests/hour | p50 / p95 latency (s) | Errors | Token mismatches | Preemptions | State |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 4 | 4 | 192 / 512 | 32 / 32 | 105.91 | 744.67 | 18.54 / 21.52 | 0 | 0 | 0 | complete |
| 32 | 4 | 192 / 512 | 32 / 32 | 107.84 | 758.25 | 18.49 / 18.55 | 0 | 0 | 0 | complete |
| 32 | 8 | 192 / 512 | 32 / 32 | 193.29 | 1,359.06 | 19.33 / 21.48 | 0 | 0 | 0 | complete |
| 32 | 16 | 192 / 512 | 32 / 32 | 341.49 | 2,401.11 | 23.37 / 26.14 | 0 | 0 | 0 | complete |
| 32 | 32 | 192 / 512 | 32 / 32 | 534.69 | 3,759.53 | 26.65 / 26.69 | 0 | 0 | 0 | complete |

The capacity-four baseline comes from earlier run `concurrency_benchmark_2026-10-17_v2`; that prior run ended **failed**, after this valid baseline completed. The capacity-32 rows belong to the primary run. Baseline and primary measurements use different physical GPUs (hosts `ampere3.stanford.edu` and `ampere5.stanford.edu`), so variation between GPUs or nodes may affect their ratio. Capacity-32 concurrency comparisons remain within the primary run.

At client concurrency four, the capacity-32 to capacity-four quick-workload throughput ratio is **1.02×**. This cross-run ratio does not isolate a server-capacity effect because physical GPU or node variation may contribute.

## Long decode: one full concurrent batch

Each request has 192 input tokens and 4,096 forced output tokens. Request count equals client concurrency, so total work grows across rows. These full-batch checks are reported separately from the fixed-total-work quick sweep.

| Server capacity | Client concurrency | Input / output tokens | Requests done / planned | Output tokens/s | Requests/hour | p50 / p95 latency (s) | Errors | Token mismatches | Preemptions | State |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 32 | 4 | 192 / 4,096 | 4 / 4 | 110.55 | 97.16 | 147.85 / 147.85 | 0 | 0 | 0 | complete |
| 32 | 8 | 192 / 4,096 | 8 / 8 | 208.32 | 183.10 | 154.97 / 154.98 | 0 | 0 | 0 | complete |
| 32 | 16 | 192 / 4,096 | 16 / 16 | 385.01 | 338.38 | 166.52 / 166.56 | 0 | 0 | 0 | complete |
| 32 | 32 | 192 / 4,096 | 32 / 32 | 661.98 | 581.82 | 196.60 / 196.64 | 0 | 0 | 0 | complete |

## Best tested points

- **Quick fixed-work sweep:** server capacity 32, client concurrency 32 achieved 534.69 output tokens/s with zero request errors and zero token-count mismatches. This is the best tested point among completed measurements.
- **Long full-batch check:** server capacity 32, client concurrency 32 achieved 661.98 output tokens/s with zero request errors and zero token-count mismatches. This is the best tested point among completed measurements.

A single ascending sweep is preliminary and does not establish a robust optimum. Pending or partial rows do not qualify as recommendations. Sampling parameters match production (temperature 1, top_p 0.95, top_k 20, seed 42). The synthetic /v1/completions workload still differs from production chat/thinking prompts and natural stopping, so identical evaluation throughput or the same best concurrency is not established. These results do not establish a faster setting for P16, whose roughly 44k-token shared-prefix prompts run on different B200 hardware.

## GPU telemetry from the sampled log

Only the server's observed GPU UUID is included. Sampled maxima come from `gpu_telemetry.csv`, rather than before/after snapshots; brief peaks between samples can be missed. NVIDIA timestamps are interpreted in Pacific time.

| Step / client concurrency | Samples during measured requests | Sampled maximum memory (MiB) | Sampled maximum GPU utilization | Mean GPU utilization |
|---|---:|---:|---:|---:|
| production_capacity4_quick / 4 | 77 | 71,737 | 100% | 96.35% |
| capacity32_quick_sweep / 4 | 75 | 71,667 | 100% | 98.73% |
| capacity32_quick_sweep / 8 | 42 | 71,939 | 100% | 96.12% |
| capacity32_quick_sweep / 16 | 24 | 72,255 | 100% | 91.67% |
| capacity32_quick_sweep / 32 | 14 | 72,385 | 100% | 92.86% |
| long_decode_full_batch_c4 / 4 | 74 | 72,385 | 100% | 98.84% |
| long_decode_full_batch_c8 / 8 | 78 | 72,385 | 100% | 99.99% |
| long_decode_full_batch_c16 / 16 | 83 | 72,385 | 100% | 100.00% |
| long_decode_full_batch_c32 / 32 | 98 | 72,385 | 100% | 99.99% |

Primary-run allocated GPU UUID(s): `GPU-a9e4977f-3666-ba49-d780-55b4191e7f07`. Across its startup, warmup and measured stages, the log contains 655 matching samples; sampled maximum memory is 72,385 MiB and sampled maximum GPU utilization is 100%.

Latency is measured from dispatch to the complete response, excluding client queue time. Throughput divides successful responses or their actual output tokens by full stage wall time, including failures. Preemptions are differences in the vLLM counter between stage snapshots; unavailable counters remain blank. Forced output lengths describe a controlled compute workload, not natural answer lengths or answer quality.

## Artifacts and provenance

[Machine-readable measurements and provenance](VLLM_CONCURRENCY_BENCHMARK_2026-10-17.json). Methodology reference: [vLLM 0.31.0 serving benchmark options](https://docs.vllm.ai/en/v0.31.0/cli/bench/serve/). This run uses our custom client rather than the official benchmark command.

[Download the benchmark artifacts](<benchmark_assets/vllm_concurrency_2026-10-17.tar.gz>).
