# Proteo-R1 released demos: three-case all-CDR sequence recovery

Qwen3.8-27B reconstructs all Chothia antibody CDR sequences from complete released visible antibody/antigen backbone and sequence context. This is a separately declared structural-text input and sequence-output adaptation on three independently reviewed ordinary demo complexes.

| Model | Delivered/planned | Source total-CDR AAR | Declared macro AAR |
|---|---:|---:|---:|
| Qwen3.8-27B | 3/3 | 0.137681 | 0.155342 |

Primary AAR uses the released writer.py total masked-residue recovery calculation pooled over all three complete outputs. The equal-case mean is a declared secondary metric; the paper aggregation has not been verified. All three cases remain in the planned denominator; incomplete delivery makes the primary metric undefined. Two artificial exact-copy delivery checks precede benchmark dispatch.

The full SAbDab paper holdout and exact Loop-RMSD/IMP evaluator remain unavailable. No generated-coordinate, binding, biological-function, experimental-validation or paper replication result is claimed.

Material differences:

- Three independently metadata-reviewed ordinary complexes from the five released demos; neither full paper holdout nor a random sample.
- Released native Chothia all-CDR masks; case-sensitive author chain selection; complete released selected protein chains with no crop.
- Pinned Qwen reads losslessly compact visible backbone/sequence JSON, not Proteo-R1 learned structural tensors; missing source atoms explicitly remain null.
- Every target CDR identity and atom coordinate is withheld; target segments and native lengths are supplied.
- Positional all-CDR amino-acid recovery and macro aggregation are a separately declared adaptation; exact paper Loop-RMSD/IMP/evaluator/aggregation are unavailable.
- No binding, function, experimental-validation or contamination-free claim.
- Lossless serialization groups chain metadata and flattens all12 backbone coordinates; exact inverse reproduces every allowed source row.
- Prospective131,072-token model context accommodates all complete inputs plus the uniform16,384-token output budget; no input truncation or crop.
- Released optional antigen design-point hotspot files are not supplied; full released selected protein docking context is preserved.
- One prospective local Qwen output per fixed case after artificial2 delivery; no selective retry, target feedback or trained head.
- Public pretraining exposure is unknown; no contamination-free or explanation-support claim.

The downloadable [complete trajectory and executable source archive](https://github.com/Some-random/bio-evaluation/blob/main/results/trajectory_archives/qwen38_27b_p41_positive3_chothia_allCDR_20261021.tar.gz) contains all saved complete request/context packets and all3 planned outcome slots. No unmasked target amino-acid sequence or target coordinates are included.
