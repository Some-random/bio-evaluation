# Eight-GPU vLLM throughput upgrade

Prepared 2026-10-18 11:33:32 PDT. All human-readable times use Pacific time.

On the 192-input/1,024-output synthetic workload, concurrency 64 reached **1,026.2 output tokens/s per GPU**, 57.6% above concurrency 32. Concurrency 128 was slower. On the 1,536-input/**4,096-output** workload, concurrency 32 reached **605.8 tokens/s**, while concurrency 64 was 2.9% slower. More concurrency did not improve every workload.

Deployment snapshot: At 2026-10-18 11:28:12 PDT, all 8 replicas were processing unchanged native evaluation requests. Each GPU had 64 bounded HTTP requests feeding its 128-sequence engine. Per-host health, combined progress and native CPU scoring watches were active. The snapshot recorded 53,906 saved responses and 29,784 remaining task-cases across the original 83,690-case scope. Saved responses are generation progress, not completed benchmark metrics.

The target pool has eight NVIDIA A100-SXM4-80GB GPUs across ampere3 and ampere5, with one complete model replica per GPU. The model remains **Qwen3.8-27B, original BF16**, revision `1d4bf0f2ff6012fd82039f2fa52739d0dd7c60c0`, with tensor parallel size 1. Serving changes preserve the frozen prompts, sampling settings, native scorers and **4,096-token evaluation output budget**.

| Setting | Original four-GPU pool | Upgraded profile |
|---|---|---|
| vLLM | 0.31.0 | 0.32.0 |
| Engine sequence capacity/GPU | 32 | 128 |
| GPU memory budget | 90% | 95% |
| Batched token budget | Original resolved configuration | 8,192 |
| Context capacity | 65,536 tokens | 65,536 tokens |
| Admission | Static length-weighted fractions | Bounded native vLLM queue |
| Task choice | A long selected request could block short admissions | Round robin across tasks, then runs |

The reviewed HTTP queue cap is **64 per replica**, pinned separately from the engine's 128-sequence capacity. This selects the measured short-input peak while keeping the complete-output tradeoff above visible. A deep mixed-work queue lets vLLM admit requests according to actual cache capacity; its rescheduling cost is included in the measured throughput.

## Closed synthetic measurements

Each profile ran on one dedicated replica. Request totals and exact token-ID prompts stayed fixed across that profile's ascending concurrency sweep. Every timed request generated the prescribed output length, with temperature 1, top_p 0.95, top_k 20, seed 42 and ignore_eos. Prefix caches were reset between levels; separate warmup used 64 output tokens.

| Input / output tokens | Requests/level | Concurrency | Output tokens/s | p50 / p95 latency (s) | Preemptions | Sampled peak KV |
|---:|---:|---:|---:|---:|---:|---:|
| 192 / 1,024 | 128 | 32 | 651.2 | 49.2 / 52.4 | 0 | 39.5% |
| 192 / 1,024 | 128 | 64 | 1026.2 | 62.4 / 63.8 | 20 | 100.0% |
| 192 / 1,024 | 128 | 128 | 973.6 | 84.8 / 133.6 | 59 | 100.0% |
| 1,536 / 4,096 | 64 | 32 | 605.8 | 215.5 / 220.0 | 0 | 86.9% |
| 1,536 / 4,096 | 64 | 64 | 588.5 | 292.1 / 445.1 | 54 | 100.0% |
| 7,000 / 1,024 | 64 | 16 | 230.0 | 70.4 / 81.7 | 0 | 56.0% |
| 7,000 / 1,024 | 64 | 32 | 232.2 | 122.0 / 172.1 | 25 | 99.8% |
| 7,000 / 1,024 | 64 | 64 | 230.8 | 236.7 / 276.9 | 28 | 99.8% |
| 45,056 / 1,024 | 16 | 4 | 43.5 | 94.0 / 117.3 | 0 | 61.5% |
| 45,056 / 1,024 | 16 | 8 | 47.1 | 152.3 / 255.3 | 0 | 92.1% |
| 45,056 / 1,024 | 16 | 16 | 47.1 | 270.8 / 347.7 | 0 | 92.1% |

All 752 timed requests across 11 points closed with zero failed requests and zero prompt/output token mismatches. Saved request hashes, raw usage and server token-counter deltas agree; engine queues were idle at timing boundaries. Preemptions are cache-driven rescheduling/recomputation events, and are reported even when every request succeeds. KV peaks are sampled and may miss brief peaks.

The 7,000-token input profile was nearly flat: 230.0, 232.2 and 230.8 output tokens/s at concurrency 16, 32 and 64. The 45,056-token profile reached 43.5, 47.1 and 47.1 at concurrency 4, 8 and 16. Its larger two queues produced essentially equal throughput with different latency.

These are custom stdlib harness measurements using the completions API and forced decode lengths. They do not reproduce native chat/thinking prompts, biological answer lengths or shared-prefix patterns. One ascending sweep does not establish a robust optimum. The previous runtime, memory fraction, scheduling and batch settings changed together, so these results do not isolate a vLLM-version speedup or establish a full-suite speedup/ETA. [Earlier measurements](SHARED_VLLM_EXECUTION_2026-10-17.md).

## Runtime and handoff record

vLLM 0.32.0 was released on October 17 at 11:50 PM PDT. Its Qwen M-RoPE change reduces memory used by positional caches. The release also changes context/output-limit handling, while this adapter retains the original requirement that prompt plus the full 4,096-token budget fits 65,536. [Official release](https://github.com/vllm-project/vllm/releases/tag/v0.32.0), [Qwen cache change](https://github.com/vllm-project/vllm/pull/59853), [context-limit change](https://github.com/vllm-project/vllm/pull/57035).

The installed stack reports Python 3.12.15, PyTorch 2.13.0/CUDA 13.0, Transformers 5.17.0, Triton 3.7.1 and FlashInfer 0.7.0.post1. Release/package metadata and actual serving identities are archived. [PyPI metadata](https://pypi.org/pypi/vllm/0.32.0/json).

The original dispatcher drained all active HTTP calls and saved their responses before retiring its servers. Closed parent markers, raw files and previous partial score history remain immutable. One staged assignment gives the hosts disjoint whole-run scopes, so a ready host can resume while the other starts. Four independent run preparations validate concurrently under all original run and endpoint locks; any failed preparation blocks every new model request.

New sidecars, segments, dispatch receipts and completion markers pin the parent checkpoint, exact adapter and serving identity. A clean pause writes a pause record without a full terminal generation marker. Native scoring retains the full benchmark denominator and waits for the new terminal proof; health monitoring reads metrics/response metadata without generating or scoring. The uploader preserves old and new namespaces, including the three immutable P08 partial-score forks.

An earlier bootstrap failed before serving. The original host's first upgrade startup inherited one physical CPU, and its next 32-CPU startup still inherited an 8 GiB RAM limit. Both were startup failures before biological inference and remain preserved separately. The replacement requests 32 CPUs and 320 GiB RAM explicitly. Recovery receipts and closed failed-startup evidence remain in the archive. The generation cap stays 4,096; answer truncation remains a quality limitation rather than an infrastructure setting silently changed here.

[Machine-readable report](VLLM_SATURATION_UPGRADE_2026-10-18.json) · [Code, plans and raw synthetic evidence](benchmark_assets/vllm_saturation_2026-10-18.tar.gz). The archive contains a SHA256 inventory and passed the existing recursive credential scanner. Runtime environments, caches, weights, live append logs and credentials are excluded.
