# Reaction classification: fixed answer-extraction diagnostic

Reviewed October 19, 2026, at 1:04 AM PDT. This is a separate **post-run formatting diagnostic**, `P16_NORMAL_STOP_TERMINAL_CLASS_DIAGNOSTIC_V1`; the original score remains unchanged.

| Condition | Accepted answers / 5,651 | Correct / 5,651 | Full-test accuracy |
|---|---:|---:|---:|
| Original strict final-label parser | 1,120 | 9 | 0.1593% |
| Fixed terminal-label diagnostic | 1,970 | 12 | 0.2124% |

The fixed rule recovers **850 answer labels**, adding **three correct predictions**. Answer formatting materially changes coverage, but this particular repair changes full-test accuracy very little. These results describe this sequence-to-reaction classification interface; they do not isolate general reasoning ability or validate biological explanations.

The rule retains every originally accepted prediction. For an originally invalid answer that finished normally (`stop`), it checks only the final nonempty line of the saved final text. That line must be a standalone class integer, `Answer: integer`, or balanced Markdown `**integer**`, in the original 0–383 range. Optional terminal periods follow the frozen configuration. It rejects ambiguous lines, prose on the final line, empty finals and length-capped answers. It never extracts an answer from separate reasoning.

The earlier audit found 851 rejected terminal class labels. One belongs to a length-capped response and is deliberately excluded here; the remaining 850 meet the fixed normal-stop rule. No new inference or selective regeneration occurred, and the original prompts, outputs, references and strict score were not edited.

| Preserved output budget | Cases | Original accepted | Diagnostic accepted | Original correct | Diagnostic correct |
|---|---:|---:|---:|---:|---:|
| 4,096 tokens | 4,419 | 817 | 964 | 8 | 11 |
| 16,384 tokens | 1,232 | 303 | 1,006 | 1 | 1 |
| Combined | 5,651 | 1,120 | 1,970 | 9 | 12 |

The cohorts contain different cases and remain a mixed-budget continuation, not a controlled comparison of output budgets. All 5,651 cases stay in both denominators, including 3,595 length finishes and 3,627 empty final texts; those categories overlap.

The exact user-specified rule and code were frozen at **1:04:45 AM PDT on October 19**, with 12 synthetic checks passing before references were opened by this diagnostic. All source bytes are hash-pinned. A clean-directory replay reproduced the counts and byte-identical per-case diagnostic output. The rule was not tuned after inspecting its scored result.

[Structured summary](REACTION_EXTRACTION_DIAGNOSTIC_2026-10-19.json) · [Reproduction code, frozen inputs and per-case decisions](benchmark_assets/reaction_extraction_diagnostic_2026-10-19.tar.gz) · [Original strict score](../results/runs/qwen38_27b_p16_slurm_replay_2026-10-16_mixed_4k16k_scoring_v1/scores.json) · [Integrity audit](EVALUATION_INTEGRITY_AUDIT_2026-10-18.md)
