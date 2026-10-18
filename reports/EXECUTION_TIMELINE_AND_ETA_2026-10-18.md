# Evaluation execution timeline and completion estimate

Snapshot: October 18, 2026, 11:54 AM UTC-07:00. Human-readable times are Pacific time. This is an operational report; the advisor-facing task overview stays separate.

**Latest planning estimate: about 24 more hours for generation, finishing around Mon Oct 19, 11:54 AM UTC-07:00.** Use a **20–30 hour range** (Mon Oct 19, 07:54 AM UTC-07:00 to Mon Oct 19, 05:54 PM UTC-07:00). Allow another **1–3 hours for scoring and publication as a planning allowance**, whose duration has not been measured for the remaining full tasks. This points to Monday afternoon for the final reports, with meaningful uncertainty.

**54,669 / 83,690 responses saved; 29,021 remain.** All eight endpoints were healthy and making progress in the snapshot; saved transport/server errors: 0. These counts track response generation. Native benchmark metrics require complete source unions and separate scoring.

| When (PDT) | Serving setup | Timing evidence and effect on the estimate |
|---|---|---|
| Oct 14 evening | 1 H200; vLLM 0.31.0; 4 requests/GPU; 65% memory | The first 197-case LitQA2 trial finished in 20.46 minutes. It was a different small workload, so it does not forecast the expanded suite. |
| Oct 15, 12:15 AM | 4 independent TP1 replicas; 4 requests/GPU | More replicas served the expanded queues, with shallow batching. No defensible saved full-suite ETA was found. |
| Oct 15, 1:56–2:11 AM | 7 independent TP1 replicas; 4 requests/GPU | Seven replicas existed before the later four-GPU shared pool. The earlier queue inventory also had a different scope. |
| Oct 15–17 | Separate Slurm task/shard workers; primarily 4-request batches and per-worker queues | Extra GPUs alone did not resolve shallow batching or task-specific queue fragmentation. The current 83,690-case campaign is distinct from the earlier 130,083 queued-case inventory, which included completed work and additional settings. |
| Oct 17, 11:13 PM to Oct 18, 11:05 AM | Shared pool of 4 A100 80GB; vLLM 0.31.0; 32/16/8/4 requests/GPU depending on prompt length; 90% memory | Actual native throughput averaged about 1,040 responses/hour. With 29,821 remaining at the pause, keeping this configuration implies about 28.7 additional hours, to Mon Oct 19, 03:46 PM UTC-07:00. This is a reconstruction, not a previously recorded forecast. |
| Oct 18, 11:21–11:28 AM onward | 8 A100 80GB on two hosts; vLLM 0.32.0; 64 queued HTTP requests/GPU; engine capacity 128; 95% memory | All eight began actual evaluation work. Latest estimate uses the per-pool native response rates below, yielding the rounded 24-hour generation forecast. |

The model remains Qwen3.8-27B original BF16. Prompts, sampling, native scorers and the 4,096-token output budget are unchanged across the latest serving migration. The table records throughput changes rather than changes to scientific evaluation protocols.

The original concurrency benchmark increased synthetic short-prompt throughput from 110.55 to 661.98 output tokens/second at concurrency 4 to 32. The newest short-input benchmark increased 651.2 to 1,026.2 at 32 to 64; 128 was slower. On 1,536 input / 4,096 output tokens, 64 was 2.9% slower than 32. These synthetic speedups cannot be multiplied into a full-suite completion forecast. See the [initial concurrency benchmark](VLLM_CONCURRENCY_BENCHMARK_2026-10-17.md), [shared execution report](SHARED_VLLM_EXECUTION_2026-10-17.md), and [eight-GPU upgrade report](VLLM_SATURATION_UPGRADE_2026-10-18.md).

The current hosts own **fixed, disjoint work groups**. The last host to finish controls generation completion; the forecast does not assume its remaining work will automatically move to the other host. Rates below use actual elapsed durations between snapshots nearest the requested window.

| Pool | Remaining responses | About 15-minute rate/hour | Linear remaining time | Linear finish (PDT) |
|---|---:|---:|---:|---|
| ampere3 / 4 GPUs | 13,719 | 695 | 19.7 hours | Mon Oct 19, 07:38 AM UTC-07:00 |
| ampere5 / 4 GPUs | 15,302 | 943 | 16.2 hours | Mon Oct 19, 04:06 AM UTC-07:00 |

| Observation window | Ampere3 responses/hour | Ampere5 responses/hour | Latest projected pool finish (PDT) |
|---|---:|---:|---|
| About 5 minutes | 793 | 794 | Mon Oct 19, 07:09 AM UTC-07:00 |
| About 10 minutes | 677 | 824 | Mon Oct 19, 08:09 AM UTC-07:00 |
| About 15 minutes | 695 | 943 | Mon Oct 19, 07:38 AM UTC-07:00 |
| About 20 minutes | 648 | 1,042 | Mon Oct 19, 09:03 AM UTC-07:00 |

Only about half an hour of the new eight-GPU deployment is available. Recent rates vary, prompts range from short questions to roughly 45,000 tokens, output lengths differ, and cache eviction/recomputation is occurring. The 20–30 hour range reflects those uncertainties and is not a statistical confidence interval. The combined remaining-count / combined-rate calculation can look faster while hiding the slower host's drain time. Earlier primary reports deliberately gave no full-suite ETA from synthetic rates; this report does not invent earlier promises.

The CPU watcher currently has 1 completed/reused scoring task and 10 waiting for generation. One historical 2,773-case P03 aggregation/scoring job took about 6 minutes 11 seconds; it does not establish how long all remaining tasks will take. The added 1–3 hour allowance above is explicitly a planning assumption.

[Calculation inputs, window endpoints, source snapshot hashes and forecast assumptions](EXECUTION_TIMELINE_AND_ETA_2026-10-18.json). The report uses read-only progress records and launches no inference, benchmark sweep or runtime change.
