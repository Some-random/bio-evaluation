# RAbD: reviewed38 masked-backbone sequence recovery

Qwen3.8-27B reconstructs CDRH3 sequences from current official SAbDab IMGT context. This is a separately declared backbone-text adaptation on38of the60released entries, not a trained MEAN or full historical-cohort replication.

| Model | Cases delivered/planned | Sequence recovery AAR (fraction0–1) |
|---|---:|---:|
| Qwen3.8-27B | 38/38 | 0.161658 |

Both artificial long-context exact-copy delivery checks passed before benchmark dispatch. Native AAR is the equal-weight mean of positional sequence recovery per case. Missing complete outputs retain the entire38-case denominator and make the primary metric undefined. No RMSD, TMscore, perplexity, binding or biological-function result is claimed.

Material differences:

- Independently reviewed38 of original60 source entries; remaining22 outside this declared condition.
- Current official SAbDab IMGT coordinates are not certified historical processed MEAN bytes or graph equivalence.
- Qwen consumes losslessly compact JSON backbone context, not a trained MEAN coordinate graph.
- Target amino-acid identities and all target atom coordinates are withheld; input carries fixed CDRH3 length.
- Native source48-nearest antigen context indices are reused; these indices were computed from the experimental complex, including native target context, as in the released preparation.
- Only sequence recovery is scored; no generated-coordinate RMSD, TMscore, likelihood or functional-binding result is claimed.
- One prospective local-Qwen output per fixed case; no selective retry or trained head.
- Current public benchmark pretraining exposure is unknown; no contamination-free or explanation-support claim.
