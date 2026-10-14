# Contamination and memorization protocol

Prior exposure to these public benchmarks is UNKNOWN. A prompt cannot erase
information already learned by a closed model, and a negative black-box audit
does not establish that exposure never happened. Current detection methods
have substantial limitations ([Samuel et al., COLING 2025](https://aclanthology.org/2025.coling-main.338/)).

## Controls implemented in preparation

- Store evaluation data separately from future training/retrieval corpora.
- Render from task-specific input allowlists rather than complete source rows.
- Keep reference descriptions out of explanation requests. For engineering,
  the desired effect is intentionally a required input; the replacement residue
  and unknown target position are withheld as appropriate.
- Never provide the mutant sequence or mutation-bearing accession/entry to
  unknown-position engineering. Preserve complete wild-type sequences.
- Do not copy Mol-Instructions gold outputs or few-shot reference examples.
- Use the official PG-LLM prompt, candidate order and full sequences. Its label
  files are checked as bytes for integrity but never parsed into requests.
- Keep solver tools disabled. Select pilot case IDs without labels.
- Freeze the future paid-run configuration before any outcome-based evaluation.
- Mark the present MutaDescribe text prompts as drafts, not official reproduction.

## What to do about existing model memorization

Run two separately reported tracks:

1. **Official public benchmarks:** retain the native protocols for comparability,
   with prior model exposure marked unknown. Do not claim clean leaderboard
   eligibility without evidence satisfying the benchmark's rules.
2. **Fresh holdout:** source genuinely new measured outcomes or newly curated
   annotation records published after a pinned model's data cutoff. Confirm
   the underlying outcomes are new; a newly packaged old dataset is insufficient.
   Select records and predeclare temporal/assay/family or sequence-cluster
   holdouts before looking at predictions. Store labels with the scorer and
   lock predictions before opening outcomes. Keep the fresh set out of tuning,
   model selection, training and solver retrieval.

For protein generalization, group homologous sequences and related assays so
near-duplicate families cannot straddle our own development/test tracks. Use
task-appropriate identity/coverage criteria and document them, rather than
inventing one universal identity threshold. Do not overwrite an official split
with this diagnostic split and call it a reproduction. For closed provider
models we cannot inspect or de-duplicate their full pretraining corpus.

Model aliases can change. Record requested and returned model IDs, documented
cutoff, run date, all input hashes and source versions; prefer a frozen snapshot
when one is actually offered. A published cutoff is useful provenance, not a
proof of zero prior exposure. The MutaDescribe temporal test was released with
the 2024 work, so the word "temporal" alone does not make it new to a 2026 model.

Do not scramble protein sequences, create random mutations without ground
truth, or paraphrase official protected evaluations to claim cleanliness.
Changing wording or removing protein names cannot remove factual memorization.
Any permitted name-blind/wording diagnostic belongs in a separate preregistered
track; no such variants are authorized for PG-LLM here. Its
[evaluation-only policy](https://github.com/rohitarorayyc/proteingym-llm/blob/main/BENCHMARK_USE_POLICY.md)
prohibits benchmark-specific tuning and retrieval augmentation.

## Provider data handling

Keep API training-data sharing opt-in disabled. API data is not used for
training by default ([OpenAI data controls](https://developers.openai.com/api/docs/guides/your-data)).
This prevents our requests from being used for provider training by default;
it does not remove prior contamination. Do not send private unpublished lab or
collaboration data without separate authorization. A fresh measured holdout
has not yet been acquired or evaluated in this workspace.
