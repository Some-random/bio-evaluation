# Protein-first cost and execution plan

Prepared 13 October 2026. No paid model call has been made. Work is in
`/data/rustfs1/dongweij/bio-evaluation` and uses CPU only.

## Verified input inventory

| Setting | Prepared requests | Source / scope |
|---|---:|---|
| P18 | 651 | Frozen PG-LLM v1.2 primary N=50, 217 assays × 3 seeds |
| P23 | 3,494 | Protein function, released BioT5+ Mol-Instructions test |
| P24 | 1,601 | Catalytic activity, released test |
| P25 | 1,400 | Domain/motif, released test |
| P26 | 2,633 | General function, released test |
| P30 | 2,859 | Mutation explanations: 460 Easy, 384 Medium, 404 Hard, 1,611 temporal |
| P31 | 2,859 | Position supplied; same source cases |
| P32 | 2,859 | Position unknown; same source cases |
| Total | 18,356 | One response per setting/case; settings are not independent datasets |

P18 uses the reviewed, pinned official prompt renderer. Archive, authenticated
manifest, and every installed member passed the published SHA-256 checks.
P23–P26 preserve source instructions and every amino acid, converting the BioT5
markers back to ordinary sequences. This is a TEXT adapter, not a reproduction
of BioT5's trained model or its 512-token truncation.
P30–P32 have draft task-specific text renderers and input checks. Their exact
official text-baseline protocol still needs review before execution. P30's
one-call draft differs from MutaPLM's native two-stage model; reproducing that
two-stage system would add calls. Scorers and paid-run orchestration are pending.

## Model and costs

The recommended inexpensive baseline is `gpt-6-luna`. Current
[official pricing](https://developers.openai.com/api/docs/pricing) is $0.10 per
million input tokens and $0.50 per million output tokens. Batch costs half of
Standard. `gpt-6.1-sol` is a stronger alternative to predeclare separately,
priced at $2 / $10 per million Standard input/output tokens.

| Model / scope | Standard scenario | Batch scenario | Batch output-cap planning bound |
|---|---:|---:|---:|
| Luna, 100 cases per task (800 requests) | $0.91–$2.60 | $0.46–$1.30 | $4.09 |
| Luna, all eight settings | $14.03–$45.22 | $7.01–$22.61 | $40.78 |
| Sol, 100 cases per task | $18.23–$52.03 | $9.12–$26.01 | $81.82 |
| Sol, all eight settings | $280.55–$904.44 | $140.27–$452.22 | $815.53 |

These are planning scenarios, not observed bills or confidence intervals.
For input, each UTF-8 byte is conservatively counted as one token plus 256
formatting tokens per request. This proxy needs replacement by the
[official token counting endpoint](https://developers.openai.com/api/docs/guides/token-counting)
before execution. Protein strings must not use the usual English characters/4
shortcut. Long-context rates are included if the proxy exceeds 272K; none of
these initial requests does. No caching discount is assumed.

Output assumptions include reasoning tokens: P18 4,096–16,384 per response,
other tasks 1,024–4,096. The planning bound instead lets every PG-LLM response
use all 128,000 output tokens and every other response use 4,096. Actual
reasoning length is unknown and errors/truncations must remain visible.
Retries, paid judges, additional models, auxiliary-context variants, and new
fresh-holdout work are excluded. Allow approximately 20% contingency if these
are authorized. Recommended initial application-level cap: $5 for the Luna
Batch pilot; proposed full-run reserve: $50. Neither amount is approved yet.

## Next execution prerequisites

Finish official text-protocol review, scorer wrappers and a resumable runner
that checks the remaining application budget before submission. Confirm exact
model access and count the frozen payloads. Debug with synthetic or permitted
development fixtures, not held-out answer quality. Freeze model, prompts,
case selection and budgets. PG-LLM cannot be used to select a model or tune
prompts. Do not silently change the model when access fails.

For paid execution, configure `OPENAI_API_KEY` in the runner's environment.
Never paste a key into chat or put it in a tracked config. Preparation needs
no key. Keep data-sharing opt-in disabled; API data is not used for training
by default ([OpenAI data controls](https://developers.openai.com/api/docs/guides/your-data)).

## Verification

All eight leakage/serialization tests passed. All source mutation positions
passed wild-type/numbering/no-op checks. All 9,128 Mol-Instructions serialized
inputs round-trip exactly. `cost_estimate.json` contains per-split counts and
reproducible calculations. `per_task_readiness.csv` retains all 64 original IDs.

Commands to reproduce current offline preparation:

```bash
cd /data/rustfs1/dongweij/bio-evaluation
python3 -m unittest discover -s tests -v
python3 scripts/preflight.py
```
