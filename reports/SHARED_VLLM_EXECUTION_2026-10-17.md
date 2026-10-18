# Shared vLLM evaluation execution

Prepared 2026-10-17 23:20:41 PDT.

Native evaluation dispatch has started on the shared pool.

The pool uses four NVIDIA A100 GPUs on one host (ampere3.stanford.edu), with one vLLM replica per GPU. Each replica serves the original BF16 Qwen3.8-27B checkpoint with tensor parallel size 1 and a 65,536-token context limit. The native evaluation output budget remains 4,096 tokens.

The table shows the fastest accepted **tested** concurrency at each exact synthetic input length. Every request decoded exactly 4,096 tokens. These are full batches: the number of requests equals concurrency, so total work differs between rows. They measure serving capacity, not biological accuracy.

| Input tokens/request | Tested concurrency | Requests | Output tokens/s | p50 / p95 latency (s) | Sampled peak KV |
|---:|---:|---:|---:|---:|---:|
| 192 | 32 | 32 | 640.35 | 203.38 / 203.42 | 77.2% |
| 1,536 | 16 | 16 | 351.25 | 179.74 / 179.99 | 47.2% |
| 7,000 | 16 | 16 | 302.45 | 215.29 / 216.44 | 78.0% |
| 16,384 | 8 | 8 | 153.92 | 211.34 / 212.57 | 65.1% |
| 45,056 | 4 | 4 | 70.77 | 229.86 / 231.28 | 70.8% |
| 49,152 | 4 | 4 | 67.82 | 239.69 / 241.30 | 76.4% |

Accepted points have zero request failures, token-count mismatches and measured preemptions. Admission also requires idle queue boundaries, server token-counter deltas matching the exact batch, and live queue samples containing at most that batch's requests. KV peaks are sampled; brief peaks can be missed. Higher loads skipped by the memory guard remain unmeasured.

The measurements use a single ascending sweep, synthetic token IDs, the completions API, prefix-cache resets between points, and sampling temperature 1, top_p 0.95, top_k 20, seed 42. They do not reproduce native chat/thinking prompts or prove an optimum. P16's shared-prefix workload can behave differently from independent synthetic long prompts.

Length-aware dispatch uses the frozen amendment's measured caps and a global queue shared by the four replicas. As capacity opens, replicas take requests across evaluation settings. Native requests retain their original prompts, generation settings and scorers. Requests longer than the measured admission range remain blocked pending evidence.

Frozen dispatch limits: up to 192 input tokens: 32 in flight per replica; up to 1,536 input tokens: 16 in flight per replica; up to 7,000 input tokens: 16 in flight per replica; up to 16,384 input tokens: 8 in flight per replica; up to 45,056 input tokens: 4 in flight per replica; up to 49,152 input tokens: 4 in flight per replica.

A separate health watcher checks replica identity, queue/KV/preemption metrics, transport failures and response metadata. It records truncation and empty final answers without calling the model, biological scorer or changing output budgets. Native scorers run only after generation and preserve each benchmark's own metric and denominator. The additive uploader saves raw request/response trajectories, dispatch receipts, provenance and completed scoring views.

Three earlier P08 shard drains caused their native wrapper to score partial output. Those partial scores, completion records and locks remain immutable. Continuation writes use separate derived folders that pin the original history; the logical shard IDs stay the same so copied history is not counted twice. The corrected drain helper stops the executor parent before draining, then prevents it from automatically scoring during termination.

The original 4,096-token generation limit is unchanged. A response ending at that limit can be truncated and may lack a usable final answer; improved throughput does not resolve that quality limitation. Saved responses and completed benchmark scores remain separate quantities. No completion-time estimate is inferred from these synthetic rates.

An evidence review caught two overlapping long-input sweeps on replica 3: an extra 49,152-token sweep started before the original 45,056-token sweep finished. Both are excluded from capacity admission, even where the client originally marked a point eligible. The first 192-token attempt failed its busy-server preflight before generation. All three attempts remain in the archive. Clean reruns use distinct idle replicas after the original sweeps closed.

The benchmark client originally checked exclusivity only once and did not own the endpoint across gaps between points. Its results file was a per-point checkpoint, so its existence did not prove a whole sweep had finished. The public source now holds an exclusive endpoint lock for the full profile; the measurements retain their original frozen source and hashes. A CPU test verifies that a second process is refused until the first releases ownership.

[Download closed synthetic evidence and frozen pool sources](benchmark_assets/vllm_length_and_pool_2026-10-17.tar.gz). The JSON report records every measured/skipped point, exclusions, file hashes and the exact source hashes. The archive contains no live server/GPU logs, model weights, environment, caches or unrelated data.

Pool plan SHA-256: `3fde69cfc346fba55b6cb47016155e597da7eb8fc6da4513f482714b14297b90`.
Archive SHA-256: `bbb558ff9ec6ae7af01727ec13c5ab85059cf3c5d72e81581cd895f804ceea5c`.
