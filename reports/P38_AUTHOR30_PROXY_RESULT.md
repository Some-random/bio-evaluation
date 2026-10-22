# P38: 30 author-template outputs under a constrained proxy condition

Pinned local Qwen3.8-27B produced 30/30 valid deliveries. Released substitute evaluators scored 30/30 complete outputs. All 30 slots remain in the denominators; each property has ten planned templates.

| Requested property | Evaluated / planned | Full-group proxy mean | Complete length: mean; range |
|---|---:|---:|---:|
| Soluble | 10/10 | 0.532369 | 33.6; 1–212 |
| Insoluble | 10/10 | 0.484780 | 23.9; 1–61 |
| Stable | 10/10 | 57.795223 °C predicted Tm | 46.3; 1–201 |

Solubility means use NetSolP-D probability for soluble prompts and one minus that probability for insoluble prompts. The stability value is DeepSTABp predicted melting temperature under a shared hypothetical 37°C growth/Lysate context. A missing full-group mean is undefined because coverage is incomplete.

The exact published question wording was retained, with one generation per template and a prospective 16,384-token output budget. A bare canonical amino-acid output of 1–1022 residues was imposed by grammar. This changes the generation distribution; format validity is imposed and is not a capability score. Complete outputs were retained without cropping or selective retries.

The acceptance rule admits one-residue strings, and each requested-property group contains such an output. Successful delivery and predictor execution do not validate a full functional protein; predictor applicability to these very short strings is unassessed.

After all 30 generations were sealed and the own Qwen server stopped, a duplicate audit filename caused the generation allocation to exit. A separately reviewed CPU-only continuation passed a fresh artificial resource gate and scored the same locked outputs once; no sequence was regenerated.

These are substitute predictor outputs. The inspected release did not supply the original NatureLM property heads, natural-control cohort or generation allocation. This condition does not reproduce the native NatureLM score or a matched paper comparison, and does not establish experimental stability, solubility or biological function. Without a natural or unconditional control, these values do not measure gains from conditioning. Public pretraining exposure is unknown.

[Complete source and protocol](https://github.com/Some-random/bio-evaluation/blob/main/results/protocol_artifacts/qwen38_27b_p38_author30_canonical1022_netsolpd_deepstabp_proxy_20261021_source.tar.gz) · [All saved trajectories](https://github.com/Some-random/bio-evaluation/blob/main/results/trajectory_archives/qwen38_27b_p38_author30_canonical1022_netsolpd_deepstabp_proxy_20261021_trajectories.tar.gz)
