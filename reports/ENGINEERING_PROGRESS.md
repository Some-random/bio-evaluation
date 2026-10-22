# Evaluation workers and handoffs

Checked **2026-10-21T21:15:15.022082-07:00** (America/Los_Angeles). This is a manual coordination snapshot.

[Results, release years and complete example questions](RESULTS_AND_REMAINING_WORK.md) · [Original catalog](CATALOG_STATUS.md) · [Worker snapshot JSON](WORKER_ACTIVITY.json)

**Capacity: 16 worker agents plus one coordinator. GPU ceiling: eight.** Review helpers use worker slots; an active thread is not proof of model inference.

When a worker finishes a bounded deliverable, the coordinator checks it and either continues that evaluation or explicitly hands the worker another task. A finished review, CPU package or agent turn is not a finished benchmark. Job submission, generation, scoring and publication are separate stages.

| Evaluation / role | Worker | Current stage | Last verified deliverable | Next action / blocker |
|---|---|---|---|---|
| ProteinGym substitutions | /root/p17_execution | Generating | More than 10,000 of 59,581 responses delivered at 21:03 PDT; no score yet. | Owner monitors exact job 245782; CPU packaging waits for terminal output. |
| PFArena T1 single-mutant generation | /root/p19_remaining_review | Independent admission | Prior 34 scored; separate nine-case plan adopted; final plan and CPU checks ready. | Roster-valid independent admission, then actual delivery; held 12 and other 67 stay excluded. |
| PFArena T3 anchor-informed ranking | /root/p21_remaining_review | Submitted | Prior eight scored; separate five-case plan adopted and peer-admitted; job 245880 submitted. | Three artificial delivery checks before five real calls; owner retains scoring/publication. |
| PFArena T4 single-mutant-informed ranking | /root/p22_remaining_review | Stopped after interruption | Prior four-case result preserved. Additional eight-case preparation encountered a biological-risk interruption. | Preserve checkpoints; no retry, reroute, further extension review or dispatch. Exact trigger unknown. |
| NatureLM unconditional generation | /root/p37_delivery | Generating | Job 245811: 12 of 1,000 responses saved at 21:10 PDT; unsealed, not a benchmark score. | Finish unchanged generation and declared folding/scoring; owner retains publication. |
| NatureLM conditional generation | /root/p38_generation | Offline scoring repair | All 30 generations sealed; zero observed delivery errors/truncations. A metadata filename collision stopped the worker before benchmark proxy scoring. | Independently review a CPU-only scoring continuation over the same sealed outputs; no regeneration. |
| Proteo-R1 structural demonstration | /root/p41_structure | Waiting for GPU allocation | Three-case full-backbone adaptation adopted and independently admitted; job 245881 submitted. | Actual 131K one-GPU memory and neutral delivery gates before three cases; no model delivery claimed. |
| BioReason-Pro explanations | /root/p44_explanation | Waiting for GPU allocation | Reviewed 12-case local solver/judge condition adopted and admitted; job 245877 pending. | Four artificial delivery checks, then 12-case solver/judge workflow. This cannot close the 8,630-case release. |
| SlideVQA | /root/v07_execution | Preparing and reviewing | All 400 decks have OCR/contact aids; actual full-deck review and backend schema compatibility work continue. | Finish exact input eligibility and supported-schema CPU gate; model delivery remains unproven. |
| BiomniBench-DA | /root/new2026_biomni | CPU preparation | All 50 workspaces available; hard workspace quota and confined R prototype work on neutral fixtures. | CPU validation, task-method compatibility and independent exact-code review. No new-suite inference authority. |
| BixBench3 | /root/new2026_bixbench | CPU preparation | Dedicated owner attached; additive portable harness/scorer and resource-budget work underway. | Independent reviewer checks exact adapter and recording tests. No model calls. |
| GeneBench-Pro | /root/v07_execution/v07_runtime_audit | CPU preparation | Worker handed off the completed V07 guard audit and recorded GeneBench ownership. | Make the scientific environment portable; freeze once-only recording/scorer harness. No model calls. |
| LABBench2 | /root/new2026_labbench2 | Preparation complete; worker reassigned | All 1,211 requests audited; 36 neutral checks independently passed; completion sealed. | New-suite dispatch authority and actual 128K/52-image/local-judge delivery remain. Worker now reviews Biomni code. |
| Independent review coordination | /root/independent_review | Reviewing | Own SlideVQA deck partition plus exact implementation reviews; does not own every evaluation run. | Seal bounded review receipts and coordinate non-overlapping partitions. |
| BixBench3 independent technical review | /root/independent_review/v07_question_prefilter_b | Reviewing | Finished 50 complete SlideVQA decks / 242 cases; handed off that receipt. | Now reviews BixBench3 adapter/harness; identified neutral cleanup and import-order defects. |
| PFArena T1 independent technical review | /root/p19_remaining_review/metadata_provenance_audit/stability9_peer_check | Reviewing | P19 nine-case code/synthetic preflight passed 47 tests; P22 review stopped separately. | Review exact P19 freeze under existing scope; no P22 continuation. |
| PFArena T3 / SlideVQA independent review | /root/p05_scope | Reviewing | Finished FLIP scope audit and Proteo-R1 input review; then admitted exact PFArena T3 five-case plan. | Now resumes assigned SlideVQA decks 030–049; prior 000–024 receipts retained and overlap reconciled. |

**Recent worker handoffs**

- `/root/p05_scope`: FLIP metadata/scope audit, then Proteo-R1 input audit, then PFArena T3 technical admission → SlideVQA exact deck partition (accepted).
- `/root/independent_review/v07_question_prefilter_b`: SlideVQA 50-deck full-content review / 242 cases → BixBench3 independent technical review (accepted).
- `/root/v07_execution/v07_runtime_audit`: V07 bounded runtime/scorer guard audit → GeneBench-Pro portable CPU/recording preparation (ownership recorded).
- `/root/new2026_labbench2`: LABBench2 authorized CPU preparation → BiomniBench-DA independent technical review (accepted).
- `/root/p19_remaining_review`: Nine-case input/provenance review milestone → Own separate nine-case execution preparation through closure (continued ownership).
- `/root/p22_remaining_review`: No normal completion: biological-risk interruption → No retry or handoff of the interrupted action (stopped).

The existing DeepFRI GPU queue is monitored separately by the coordinator. Qualified subset and demonstration results remain distinct from full native evaluations. See the results table for scores; this page tracks who does the work.

LABBench2 and BixBench3 access is resolved. scBench remains deferred. New head training and paid/OpenAI benchmark calls remain excluded. Websites and recurring conversation updates remain disabled.

This snapshot replaces the obsolete three-worker queue. It does not automatically refresh after every message; its timestamp identifies the last reconciliation. Task-local immutable run/score artifacts remain the execution record.
