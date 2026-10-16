# P42 GFP source contract and qualified execution proposal

A concrete200-slot local condition is prepared and disabled. It preserves100 candidates per regime and the trained fluorescence proxy, while explicitly declaring prospective endpoint rules and HTTP sampling differences. Exact native novelty remains unavailable. No model generation, predictor load, forward pass or training occurred in this audit.

| Metric | Feasible result | Remaining limitation |
| --- | --- | --- |
| Success | Strict oracle improvement over the source, retaining100 slots per regime | New model, declared endpoint constraints and sampling interface differ from the original run |
| Uniqueness | Distinct improved AA strings divided by improved samples | Preserve every duplicate; a zero improved denominator is undefined |
| Native novelty | Withheld | Exact positive SFT training membership D+ is absent |
| Edit/rationale correctness | Unassessed | A short endpoint distance does not validate the generated edit program or mechanism |

The [v1 paper](https://arxiv.org/html/2603.03573v1) defines the metric targets. Its [v2 revision](https://arxiv.org/html/2603.03573v2) explicitly calls full-action GFP scores an oracle stress test, and fixes the displayed uniqueness denominator. The conditions and versions must remain separate when comparing published values.

The pinned [generation CLI](https://github.com/daiheng-zhang/STRIDE/blob/1e331e8c6d80677fcf446d84bb2de8811dfecc09/scripts/eval/infer_protein_vllm.py) does not distinguish the two action spaces or enforce an edit budget. It expects a thinking delimiter followed by protein JSON; separate Qwen channels therefore require the declared interface reconstruction. No malformed output is repaired or recovered from reasoning-only JSON.

The exact D+ set cannot be reconstructed from the public scaffolds: [default preprocessing](https://github.com/daiheng-zhang/STRIDE/blob/1e331e8c6d80677fcf446d84bb2de8811dfecc09/scripts/data/prepare_gfp_delta.py) uses a non-strict threshold, and [augmentation](https://github.com/daiheng-zhang/STRIDE/blob/1e331e8c6d80677fcf446d84bb2de8811dfecc09/scripts/data/augment_gfp_random_edit.py) writes unscored random rows without the required retained-membership or partition manifest. These defaults do not establish the arguments used in the published training run. [Issue1](https://github.com/daiheng-zhang/STRIDE/issues/1) asks for processed artifacts and has no replies in the captured metadata. Neither all TAPE train rows nor fresh random augmentation will be substituted.

The disabled [execution candidate](../configs/local_stride_gfp_p42.candidate.json) preserves both native roles and appends the stated regime constraints. It uses seeds42–141 within each regime,1024 output tokens,temperature0.7 and top-p0.9. This replaces persistent multi-choice RNG with a declared per-slot schedule; all duplicates, invalids and uncertain calls remain visible. Endpoint checks use Hamming distance for replacements and Levenshtein distance for the full action space, with a prospective1–3 bound.

The new specialized runner writes full request bodies, parsed/raw HTTP responses, separate reasoning/final strings, model/server/config hashes, candidate extraction and terminal missing-slot records. It seals the complete200-slot cohort before the independent CPU oracle scorer can run. The existing generic runner, original proposal, checkpoint and frozen benchmark artifacts were left unchanged.

All200 inputs passed a tokenizer-only audit:304/309 prompt tokens and1328/1333 including the1024 output allowance, below the source4096 context bound. The corrected audit explicitly counts input_ids and cross-checks independently encoded rendered chats. An earlier mapping-key count is preserved as superseded and must not be used. Fifteen synthetic contract/runner tests pass, with no biological inference.

Root activation still requires the isolated predictor runtime, trained-head restoration proof, final scorer hashes and complete task/input review. The resulting success/uniqueness values concern this fixed trained proxy; they would not demonstrate measured fluorescence, verified biological mechanisms, or contamination-free evaluation.

Exact file hashes, public source observations, access failures, protocol deltas and per-metric status are in the [JSON report](stride_gfp_native_contract_recovery_2026-10-15.json).
