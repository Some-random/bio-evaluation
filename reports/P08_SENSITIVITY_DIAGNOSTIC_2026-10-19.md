# P08 protein-stability sensitivity diagnostic

The archived run contains **12,851 responses, 12,616 accepted numerical predictions and 235 invalid finals**. Recomputing average-rank Spearman correlation on the accepted subset gives **−0.1215879684**, exactly matching the archived diagnostic. The native full-test correlation remains **undefined**.

Missing-answer handling cannot by itself make these predictions positively correlated with the references. Holding the 12,616 accepted predictions fixed, **every possible assignment of finite numbers to all 235 invalid slots has full-test Spearman correlation at most −0.0677995705**. This is a mathematical upper bound, not an imputed score, an achieved maximum, or a new benchmark result.

No model inference, selective retry, reference-assisted answer extraction, sign reversal, or replacement of an accepted prediction occurred. The source run remains a mixed-budget continuation: 7,303 original 4K-output cases and 5,548 remaining 16K-output cases.

## Final-answer formats

Rules were written and hash-frozen before reading the archived per-case records. They receive only the final text and finish reason. The original numerical parser was independently reproduced and agrees with every archived prediction/parse flag.

| Final format | Cases | Interpretation |
|---|---:|---|
| Native finite scalar | 12,616 | Accepted predictions; preserved exactly |
| Otherwise-native scalar using Unicode minus `−` | 11 | Clear formatting-only candidates; no revised score substituted |
| Abstention, insufficient-information or qualified prose | 212 | Includes explicit refusals and tentative/placeholder estimates |
| Truncated invalid final | 8 | All have empty final text |
| Normally stopped empty final | 4 | No delivered final answer |
| **Total** | **12,851** | Original denominator retained |

The frozen lexical classifier separates the 212 prose cases into 210 abstention/insufficient-information cases and two uncertainty/prose cases. This is a descriptive classification, not an assessment of biological correctness. Two prose cases say “not able,” a phrase not covered by the classifier's abstention expression, so their uncertainty label should not be interpreted as evidence that they committed to predictions.

Of these 212 prose responses, **54 contain a scalar-looking standalone line** under the same frozen format rules. Such a line is not necessarily an unqualified answer: some responses explicitly call the number a placeholder or guess. For example, `stability:test:63` supplies `0.0` while describing it as a placeholder; `stability:test:514` supplies `-2.3` with a similar qualification. This audit does **not** claim every prose answer is unrecoverable. It preserves the distinction between an unambiguous whole-final scalar and a number appearing inside a refusal or qualified explanation. No reference label was used to classify or choose a proposed number.

All 235 invalid slots are allowed arbitrary finite replacements in the upper-bound calculation, including the eleven formatting candidates and every ambiguous prose response. Thus the negative bound does not depend on classifying those cases pessimistically.

## Conservative bound, including ties

Let $n=12851$, $k=12616$, and $m=235$. Let $b_i$ be each reference's **full-test average rank**, centered at $(n+1)/2$. For the accepted predictions, let $a_i$ be their average ranks within the accepted subset, centered at $(k+1)/2$.

The fixed term is

$$C_0=\sum_{i\in V} a_i b_i=-20,783,784,910.25.$$

After inserting $m$ finite predictions, an accepted prediction's rank increases by a value between zero and $m$, including when inserted values join a tie. Its centered rank therefore changes by at most $m/2$ in either direction. Each inserted prediction's centered average rank is bounded by $(n-1)/2$ in magnitude. Consequently the full rank-covariance numerator satisfies

$$C\le C_0+\frac m2\sum_{i\in V}|b_i|+\frac{n-1}{2}\sum_{i\in M}|b_i|=U.$$

| Quantity | Recomputed value |
|---|---:|
| Accepted-prediction rank-shift allowance | 4,777,763,615 |
| Invalid-slot rank allowance | 4,015,368,000 |
| Numerator upper bound $U$ | **−11,990,653,295.25** |
| Reference rank sum of squares | 176,848,868,082 |
| Maximum predictor rank sum of squares | 176,859,959,850 |
| Maximum denominator $D_{max}$ | 176,854,413,879.04477 |

The maximum predictor sum of squares is $n(n^2-1)/12$; replacing tied ranks by their average can only reduce it. Since $C\le U<0$ and $0<D\le D_{max}$,

$$\rho=C/D\le U/D\le U/D_{max}=\mathbf{-0.06779957046167201}.$$

The negativity matters: dividing a **positive** numerator bound by a denominator upper bound would not give a valid correlation upper bound. The implementation explicitly avoids that error. The accepted predictions are nonconstant, so any permitted completion has a nonzero predictor-rank denominator.

## Independent, tighter cross-check

Average ranks also obey the identity

$$C=\frac12\sum_{i<j}\operatorname{sign}(p_i-p_j)(b_i-b_j).$$

The accepted–accepted pair contribution is fixed at $C_0$. Bounding every pair involving an invalid slot by $|b_i-b_j|/2$ gives a numerator upper bound of **−14,839,222,209.25**, hence the independently derived tighter correlation upper bound **−0.0839064284**. Prediction/reference ties are included through the zero sign and average ranks. This bound also need not be attainable; it is presented as a cross-check, not a replacement headline score.

Two implementations—sorted-block ranks with prefix-distance sums, and counting ranks with direct pair-distance enumeration—agree to better than $10^{-14}$. Nine synthetic tests cover numerical parsing, Unicode signs, refusals, tied ranks, the pair identity, exhaustive finite completions including ties, a nontrivial negative-bound case, and the positive-numerator denominator trap. These checks use synthetic values rather than benchmark-answer tuning.

## What the target means

The [TAPE dataset loader](https://github.com/songlab-cal/tape/blob/6d345c2b2bbf52cd32cf179325c222afd92aec7e/tape/datasets.py#L496) returns the released `stability_score[0]` directly. The [TorchDrug/PEER loader](https://github.com/DeepGraphLearning/torchdrug/blob/6066fbd82360abb5f270cba1eca560af01b8cc90/torchdrug/datasets/stability.py#L29) selects the same field. Neither reviewed loader supplies a sign reversal for this endpoint.

[Rocklin et al.](https://pmc.ncbi.nlm.nih.gov/articles/PMC5568797/) define an experimentally measured protease-resistance score relative to a predicted unfolded-state baseline. A one-unit score increase corresponds to a tenfold change in the measured-to-unfolded EC50 ratio. **Higher scores indicate greater resistance relative to that baseline.** This is not a melting temperature, probability, or directly measured folding free energy. [TAPE](https://arxiv.org/html/1906.08230#A1.SS5) uses these measurements as a regression/ranking task and holds out neighborhoods of promising designs.

The audit does not reconstruct every released target from the original raw assay tables, establish exact historical preprocessing equivalence, or infer why the model produced negative association. Ordinary increasing changes of numerical units cannot change Spearman rank correlation. Reversing the score direction after seeing outcomes would change the prediction rule and is not applied here.

The archived model prompt names the original TAPE/Rocklin `stability_score` scale and resistance to unfolding, but does not explicitly define which direction is higher or give the numerical score formula. A scale misunderstanding therefore remains a possible interface explanation. The bound concerns agreement with the archived native targets under that prompt; it does not establish absent biological knowledge. Any clarification of the score definition belongs to a separately frozen future protocol.

## Evidence and interpretation limits

The result supports a narrow statement: **the accepted predictions in this fixed Qwen setup have weak negative rank association with this released stability test, and resolving only the 235 invalid finals cannot reverse that association.** It does not bound performance from another model, prompt, budget, new generation run, or changes to the accepted predictions. It does not validate or invalidate the responses' biological explanations.

The PyTorch release has 12,851 test rows; the original TAPE paper lists 12,839. The existing version qualification remains in force. No clean 4K-versus-16K treatment effect follows from the mixed-budget run.

Reproduction files: [analysis and proof code](../results/offline_diagnostics/p08_sensitivity_2026-10-19/analyze.py), [synthetic checks](../results/offline_diagnostics/p08_sensitivity_2026-10-19/test_analyze.py), [independent calculation](../results/offline_diagnostics/p08_sensitivity_2026-10-19/independent_check.py), [structured report](P08_SENSITIVITY_DIAGNOSTIC_2026-10-19.json), and [evidence manifest](../results/offline_diagnostics/p08_sensitivity_2026-10-19/evidence_manifest.json). The portable evidence includes an unchanged compressed copy of the original per-case records and original score/completion files.

Original per-case SHA-256: `2c6f6bbe41878d63412649d8588f3bd5fee5d235cce19152643460b3843cf473`. The original score file's hash matches its completion receipt. All original predictions, scores and case denominators remain unchanged.
