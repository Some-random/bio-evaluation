# Biological evaluation agent handoff — 13 October 2026

## What to give the execution agent

Attach this complete ZIP, extract it, and send the prompts in COPY_PASTE_PROMPTS.md in order.

- PROJECT_CONTEXT.md: research context and the two independent “text” comparisons.
- BUILD_AGENT_PROMPT.md: source verification, implementation, dry-run and cost estimation.
- RUN_AGENT_PROMPT.md: frozen, budget-controlled execution and reporting.
- TASK_RULES.md: native metrics, context restrictions and blockers covering all 64 task IDs.
- task_registry.json: original catalog + compatibility rows + explicitly labeled proposed execution fields.
- task_execution_matrix.csv: spreadsheet-readable row-wise operation/scoring/context instructions.
- runtime_config.template.json: dry-run-only placeholders. Supply real model IDs and approved budgets in the execution environment.
- references/: both current workbooks, original catalog JSON/CSV, compatibility CSV and original guide, copied without modification.
- SHA256SUMS.txt / VALIDATION.json: local integrity and coverage checks.

## Scope and evidence

The original catalog has 64 biological settings and 14 general control groups. This handoff prioritizes 14 biological settings for initial implementation; it does not collapse them into independent datasets or authorize all possible runs. Categories A–F preserve the previous classification: 26 existing text interfaces, 16 text adapters, 4 generation/scorer settings, 9 visual settings, 2 structural settings and 7 special/unresolved settings.

Original catalog entries are prior assistant-produced source-linked notes. For actual reproduction, the official release/paper/scorer controls. New work-order, context-variant and engineering rules here are proposals, not instructions quoted from Yejin, Fang or the benchmark authors. Record corrections with supporting sources. Task URLs have not been freshly re-audited during this drafting task.

Current source files were readable and are included. Some older uploads have expired; a missing older source must be re-uploaded if it is needed. Do not invent its content or let one missing attachment block unrelated available work.

## Not included / not done

No raw benchmark payloads, model weights, API credentials, model outputs, paid calls, trained models, or working evaluation harness are included. This is a context/prompt package for the agent that will implement and run the work. Cost and model identifiers are intentionally unset.

No private lab data are included. This does not modify the separate LibB/LibD handoff, wet-lab procedures, or candidate selection. No source files in the user's Library or Dropbox were changed.

## First implementation wave

P18; P23–P26; P30–P32; B01–B03; B06–B08.

Native protocol first. With/without OPTIONAL biological text is a separate, authorized ablation—not a reason to remove essential task inputs. PG-LLM is native-only in the initial handoff. The same solver can be evaluated in TEXT mode even if it supports vision in other use.

Everything can be prepared and dry-tested without a paid model call. Actual inference requires the user environment's model identifiers and resource approval.
