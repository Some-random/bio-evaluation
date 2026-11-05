# LiveProteinBench question review: handoff for evaluation

This handoff records a proposed use of the saved question reviews. It is not an expert adjudication or a change to the original benchmark. The source is the 1,736-question merged review set; 61 of 1,797 original questions were outside that set. Both reviewers were GPT-6 Luna and Qwen3.8 Flash-Next. Their reviews combine earlier and November 4 rounds, rather than a uniform rerun. Source merged JSONL SHA-256: `bc5265af615f04ff0689507e7ec320291d29121063f14b3ed9525789940248ec`.

## Recommended handling

1. **Original benchmark:** retain the author key and report the original score unchanged as a baseline.
2. **Reasoning-focused view:** exclude the 52 questions below where both reviewers labeled the question lookup-dependent. This is a conservative filter based on model judgments, not proof that the questions cannot be answered by transferable biological reasoning. Removing 52 from the reviewed set leaves 1,684; that does not mean the remaining questions have been independently verified.
3. **Possible multiple correct choices:** inspect the 86 questions below. Both reviewers listed at least two options as defensible, but that can mean either multiple choices are biologically correct or that the reviewer could not distinguish them from the input. Options shown here are proposed by reviewers, not approved answer keys. Check the underlying source and the question semantics before accepting an additional answer; record each decision and its evidence.
4. **Overlap:** two questions are in both lists; 84 of the 86 are outside the 52-question exclusion. If the exclusion is applied first, the remaining set contains 84 multiple-choice flags. Avoid double-counting them.
5. **Reporting:** describe the exact population, exclusion IDs, accepted answers, evidence and adjudication status. Report the original and any adjusted result separately. There is no automatic rescoring or verified multi-answer key in this handoff.

Four of the 86 cases have fewer than two options in common between the two reviewers’ lists. Both having listed multiple options is not necessarily agreement on exactly which options.

## 52 proposed reasoning-focused exclusions

Each case link opens the original question, key, and both saved visible reviewer explanations.

- [EC_number_0005](../reports/liveproteinbench_transfer_reassessment_20261102/lookup_dependent_52_20261104.md#case-ec_number_0005)
- [EC_number_0006](../reports/liveproteinbench_transfer_reassessment_20261102/lookup_dependent_52_20261104.md#case-ec_number_0006)
- [EC_number_0020](../reports/liveproteinbench_transfer_reassessment_20261102/lookup_dependent_52_20261104.md#case-ec_number_0020)
- [EC_number_0021](../reports/liveproteinbench_transfer_reassessment_20261102/lookup_dependent_52_20261104.md#case-ec_number_0021)
- [EC_number_0024](../reports/liveproteinbench_transfer_reassessment_20261102/lookup_dependent_52_20261104.md#case-ec_number_0024)
- [EC_number_0035](../reports/liveproteinbench_transfer_reassessment_20261102/lookup_dependent_52_20261104.md#case-ec_number_0035)
- [EC_number_0049](../reports/liveproteinbench_transfer_reassessment_20261102/lookup_dependent_52_20261104.md#case-ec_number_0049)
- [EC_number_0051](../reports/liveproteinbench_transfer_reassessment_20261102/lookup_dependent_52_20261104.md#case-ec_number_0051)
- [EC_number_0056](../reports/liveproteinbench_transfer_reassessment_20261102/lookup_dependent_52_20261104.md#case-ec_number_0056)
- [EC_number_0071](../reports/liveproteinbench_transfer_reassessment_20261102/lookup_dependent_52_20261104.md#case-ec_number_0071)
- [EC_number_0076](../reports/liveproteinbench_transfer_reassessment_20261102/lookup_dependent_52_20261104.md#case-ec_number_0076)
- [EC_number_0082](../reports/liveproteinbench_transfer_reassessment_20261102/lookup_dependent_52_20261104.md#case-ec_number_0082)
- [EC_number_0083](../reports/liveproteinbench_transfer_reassessment_20261102/lookup_dependent_52_20261104.md#case-ec_number_0083)
- [EC_number_0087](../reports/liveproteinbench_transfer_reassessment_20261102/lookup_dependent_52_20261104.md#case-ec_number_0087)
- [EC_number_0093](../reports/liveproteinbench_transfer_reassessment_20261102/lookup_dependent_52_20261104.md#case-ec_number_0093)
- [EC_number_0105](../reports/liveproteinbench_transfer_reassessment_20261102/lookup_dependent_52_20261104.md#case-ec_number_0105)
- [EC_number_0107](../reports/liveproteinbench_transfer_reassessment_20261102/lookup_dependent_52_20261104.md#case-ec_number_0107)
- [EC_number_0119](../reports/liveproteinbench_transfer_reassessment_20261102/lookup_dependent_52_20261104.md#case-ec_number_0119)
- [EC_number_0144](../reports/liveproteinbench_transfer_reassessment_20261102/lookup_dependent_52_20261104.md#case-ec_number_0144)
- [EC_number_0149](../reports/liveproteinbench_transfer_reassessment_20261102/lookup_dependent_52_20261104.md#case-ec_number_0149)
- [EC_number_0151](../reports/liveproteinbench_transfer_reassessment_20261102/lookup_dependent_52_20261104.md#case-ec_number_0151)
- [EC_number_0154](../reports/liveproteinbench_transfer_reassessment_20261102/lookup_dependent_52_20261104.md#case-ec_number_0154)
- [EC_number_0174](../reports/liveproteinbench_transfer_reassessment_20261102/lookup_dependent_52_20261104.md#case-ec_number_0174)
- [GO_biological_process_0089](../reports/liveproteinbench_transfer_reassessment_20261102/lookup_dependent_52_20261104.md#case-go_biological_process_0089)
- [GO_biological_process_0144](../reports/liveproteinbench_transfer_reassessment_20261102/lookup_dependent_52_20261104.md#case-go_biological_process_0144)
- [GO_biological_process_0166](../reports/liveproteinbench_transfer_reassessment_20261102/lookup_dependent_52_20261104.md#case-go_biological_process_0166)
- [GO_biological_process_0187](../reports/liveproteinbench_transfer_reassessment_20261102/lookup_dependent_52_20261104.md#case-go_biological_process_0187)
- [GO_cellular_component_0004](../reports/liveproteinbench_transfer_reassessment_20261102/lookup_dependent_52_20261104.md#case-go_cellular_component_0004) — also in the 86-choice list
- [GO_cellular_component_0061](../reports/liveproteinbench_transfer_reassessment_20261102/lookup_dependent_52_20261104.md#case-go_cellular_component_0061)
- [GO_cellular_component_0109](../reports/liveproteinbench_transfer_reassessment_20261102/lookup_dependent_52_20261104.md#case-go_cellular_component_0109)
- [GO_cellular_component_0155](../reports/liveproteinbench_transfer_reassessment_20261102/lookup_dependent_52_20261104.md#case-go_cellular_component_0155)
- [GO_cellular_component_0193](../reports/liveproteinbench_transfer_reassessment_20261102/lookup_dependent_52_20261104.md#case-go_cellular_component_0193)
- [GO_molecular_function_0091](../reports/liveproteinbench_transfer_reassessment_20261102/lookup_dependent_52_20261104.md#case-go_molecular_function_0091) — also in the 86-choice list
- [GO_molecular_function_0160](../reports/liveproteinbench_transfer_reassessment_20261102/lookup_dependent_52_20261104.md#case-go_molecular_function_0160)
- [catalytic_activity_0051](../reports/liveproteinbench_transfer_reassessment_20261102/lookup_dependent_52_20261104.md#case-catalytic_activity_0051)
- [motif_position_0013](../reports/liveproteinbench_transfer_reassessment_20261102/lookup_dependent_52_20261104.md#case-motif_position_0013)
- [pathway_0084](../reports/liveproteinbench_transfer_reassessment_20261102/lookup_dependent_52_20261104.md#case-pathway_0084)
- [pathway_0090](../reports/liveproteinbench_transfer_reassessment_20261102/lookup_dependent_52_20261104.md#case-pathway_0090)
- [pathway_0117](../reports/liveproteinbench_transfer_reassessment_20261102/lookup_dependent_52_20261104.md#case-pathway_0117)
- [pathway_0140](../reports/liveproteinbench_transfer_reassessment_20261102/lookup_dependent_52_20261104.md#case-pathway_0140)
- [pathway_0148](../reports/liveproteinbench_transfer_reassessment_20261102/lookup_dependent_52_20261104.md#case-pathway_0148)
- [ph_0002](../reports/liveproteinbench_transfer_reassessment_20261102/lookup_dependent_52_20261104.md#case-ph_0002)
- [ph_0022](../reports/liveproteinbench_transfer_reassessment_20261102/lookup_dependent_52_20261104.md#case-ph_0022)
- [ph_0046](../reports/liveproteinbench_transfer_reassessment_20261102/lookup_dependent_52_20261104.md#case-ph_0046)
- [temperature_0006](../reports/liveproteinbench_transfer_reassessment_20261102/lookup_dependent_52_20261104.md#case-temperature_0006)
- [temperature_0007](../reports/liveproteinbench_transfer_reassessment_20261102/lookup_dependent_52_20261104.md#case-temperature_0007)
- [temperature_0008](../reports/liveproteinbench_transfer_reassessment_20261102/lookup_dependent_52_20261104.md#case-temperature_0008)
- [temperature_0012](../reports/liveproteinbench_transfer_reassessment_20261102/lookup_dependent_52_20261104.md#case-temperature_0012)
- [temperature_0019](../reports/liveproteinbench_transfer_reassessment_20261102/lookup_dependent_52_20261104.md#case-temperature_0019)
- [temperature_0020](../reports/liveproteinbench_transfer_reassessment_20261102/lookup_dependent_52_20261104.md#case-temperature_0020)
- [temperature_0023](../reports/liveproteinbench_transfer_reassessment_20261102/lookup_dependent_52_20261104.md#case-temperature_0023)
- [temperature_0028](../reports/liveproteinbench_transfer_reassessment_20261102/lookup_dependent_52_20261104.md#case-temperature_0028)

## 86 cases with candidate alternatives

The author key and reviewer option lists below preserve the review records. They are **not** instructions to accept every option without adjudication.

| Question | Author key | Luna listed | Qwen listed | Also in 52 exclusions? |
|---|---|---|---|---|
| [GO_biological_process_0131](../reports/liveproteinbench_transfer_reassessment_20261102/multiple_defensible_by_both_86_20261104.md#case-go_biological_process_0131) | C | B, C | B, C | No |
| [GO_biological_process_0137](../reports/liveproteinbench_transfer_reassessment_20261102/multiple_defensible_by_both_86_20261104.md#case-go_biological_process_0137) | C | A, C | A, C | No |
| [GO_cellular_component_0004](../reports/liveproteinbench_transfer_reassessment_20261102/multiple_defensible_by_both_86_20261104.md#case-go_cellular_component_0004) | D | C, D | C, D | Yes |
| [GO_cellular_component_0023](../reports/liveproteinbench_transfer_reassessment_20261102/multiple_defensible_by_both_86_20261104.md#case-go_cellular_component_0023) | D | A, D | A, D | No |
| [GO_cellular_component_0029](../reports/liveproteinbench_transfer_reassessment_20261102/multiple_defensible_by_both_86_20261104.md#case-go_cellular_component_0029) | A | A, C | A, C | No |
| [GO_cellular_component_0032](../reports/liveproteinbench_transfer_reassessment_20261102/multiple_defensible_by_both_86_20261104.md#case-go_cellular_component_0032) | C | B, C | B, C | No |
| [GO_cellular_component_0038](../reports/liveproteinbench_transfer_reassessment_20261102/multiple_defensible_by_both_86_20261104.md#case-go_cellular_component_0038) | B | A, B | A, B | No |
| [GO_cellular_component_0045](../reports/liveproteinbench_transfer_reassessment_20261102/multiple_defensible_by_both_86_20261104.md#case-go_cellular_component_0045) | C | A, C | A, C | No |
| [GO_cellular_component_0133](../reports/liveproteinbench_transfer_reassessment_20261102/multiple_defensible_by_both_86_20261104.md#case-go_cellular_component_0133) | A | A, B | A, B | No |
| [GO_molecular_function_0044](../reports/liveproteinbench_transfer_reassessment_20261102/multiple_defensible_by_both_86_20261104.md#case-go_molecular_function_0044) | B | B, D | B, D | No |
| [GO_molecular_function_0091](../reports/liveproteinbench_transfer_reassessment_20261102/multiple_defensible_by_both_86_20261104.md#case-go_molecular_function_0091) | D | C, D | C, D | Yes |
| [active_site_0003](../reports/liveproteinbench_transfer_reassessment_20261102/multiple_defensible_by_both_86_20261104.md#case-active_site_0003) | C | C, D | C, D | No |
| [active_site_0026](../reports/liveproteinbench_transfer_reassessment_20261102/multiple_defensible_by_both_86_20261104.md#case-active_site_0026) | C | B, C | B, C | No |
| [cofactor_0016](../reports/liveproteinbench_transfer_reassessment_20261102/multiple_defensible_by_both_86_20261104.md#case-cofactor_0016) | C | A, C | A, C | No |
| [cofactor_0025](../reports/liveproteinbench_transfer_reassessment_20261102/multiple_defensible_by_both_86_20261104.md#case-cofactor_0025) | C | C, D | C, D | No |
| [cofactor_0026](../reports/liveproteinbench_transfer_reassessment_20261102/multiple_defensible_by_both_86_20261104.md#case-cofactor_0026) | A | A, C | A, C | No |
| [cofactor_0027](../reports/liveproteinbench_transfer_reassessment_20261102/multiple_defensible_by_both_86_20261104.md#case-cofactor_0027) | D | B, D | B, D | No |
| [cofactor_0042](../reports/liveproteinbench_transfer_reassessment_20261102/multiple_defensible_by_both_86_20261104.md#case-cofactor_0042) | A | A, D | A, D | No |
| [cofactor_0054](../reports/liveproteinbench_transfer_reassessment_20261102/multiple_defensible_by_both_86_20261104.md#case-cofactor_0054) | C | B, C | B, C | No |
| [cofactor_0063](../reports/liveproteinbench_transfer_reassessment_20261102/multiple_defensible_by_both_86_20261104.md#case-cofactor_0063) | B | B, D | B, D | No |
| [cofactor_0068](../reports/liveproteinbench_transfer_reassessment_20261102/multiple_defensible_by_both_86_20261104.md#case-cofactor_0068) | B | B, D | B, D | No |
| [cofactor_0096](../reports/liveproteinbench_transfer_reassessment_20261102/multiple_defensible_by_both_86_20261104.md#case-cofactor_0096) | B | A, B | A, B, C | No |
| [cofactor_0098](../reports/liveproteinbench_transfer_reassessment_20261102/multiple_defensible_by_both_86_20261104.md#case-cofactor_0098) | A | A, C | A, C | No |
| [cofactor_0127](../reports/liveproteinbench_transfer_reassessment_20261102/multiple_defensible_by_both_86_20261104.md#case-cofactor_0127) | D | C, D | C, D | No |
| [cofactor_0128](../reports/liveproteinbench_transfer_reassessment_20261102/multiple_defensible_by_both_86_20261104.md#case-cofactor_0128) | A | A, C | A, C | No |
| [cofactor_0130](../reports/liveproteinbench_transfer_reassessment_20261102/multiple_defensible_by_both_86_20261104.md#case-cofactor_0130) | C | C, D | C, D | No |
| [cofactor_0135](../reports/liveproteinbench_transfer_reassessment_20261102/multiple_defensible_by_both_86_20261104.md#case-cofactor_0135) | D | C, D | C, D | No |
| [cofactor_0139](../reports/liveproteinbench_transfer_reassessment_20261102/multiple_defensible_by_both_86_20261104.md#case-cofactor_0139) | D | B, D | B, D | No |
| [cofactor_0164](../reports/liveproteinbench_transfer_reassessment_20261102/multiple_defensible_by_both_86_20261104.md#case-cofactor_0164) | B | A, B | A, B | No |
| [cofactor_0179](../reports/liveproteinbench_transfer_reassessment_20261102/multiple_defensible_by_both_86_20261104.md#case-cofactor_0179) | A | A, B | A, B | No |
| [motif_position_0015](../reports/liveproteinbench_transfer_reassessment_20261102/multiple_defensible_by_both_86_20261104.md#case-motif_position_0015) | D | C, D | C, D | No |
| [motif_position_0016](../reports/liveproteinbench_transfer_reassessment_20261102/multiple_defensible_by_both_86_20261104.md#case-motif_position_0016) | D | C, D | B, D | No |
| [pathway_0001](../reports/liveproteinbench_transfer_reassessment_20261102/multiple_defensible_by_both_86_20261104.md#case-pathway_0001) | C | B, C | B, C | No |
| [pathway_0006](../reports/liveproteinbench_transfer_reassessment_20261102/multiple_defensible_by_both_86_20261104.md#case-pathway_0006) | C | B, C | B, C | No |
| [pathway_0021](../reports/liveproteinbench_transfer_reassessment_20261102/multiple_defensible_by_both_86_20261104.md#case-pathway_0021) | A | A, B | A, B | No |
| [pathway_0029](../reports/liveproteinbench_transfer_reassessment_20261102/multiple_defensible_by_both_86_20261104.md#case-pathway_0029) | D | C, D | C, D | No |
| [pathway_0032](../reports/liveproteinbench_transfer_reassessment_20261102/multiple_defensible_by_both_86_20261104.md#case-pathway_0032) | C | C, D | C, D | No |
| [pathway_0062](../reports/liveproteinbench_transfer_reassessment_20261102/multiple_defensible_by_both_86_20261104.md#case-pathway_0062) | D | C, D | C, D | No |
| [pathway_0085](../reports/liveproteinbench_transfer_reassessment_20261102/multiple_defensible_by_both_86_20261104.md#case-pathway_0085) | C | B, C | B, C | No |
| [pathway_0108](../reports/liveproteinbench_transfer_reassessment_20261102/multiple_defensible_by_both_86_20261104.md#case-pathway_0108) | A | A, D | A, D | No |
| [pathway_0115](../reports/liveproteinbench_transfer_reassessment_20261102/multiple_defensible_by_both_86_20261104.md#case-pathway_0115) | C | A, C | A, C | No |
| [pathway_0130](../reports/liveproteinbench_transfer_reassessment_20261102/multiple_defensible_by_both_86_20261104.md#case-pathway_0130) | C | C, D | C, D | No |
| [pathway_0147](../reports/liveproteinbench_transfer_reassessment_20261102/multiple_defensible_by_both_86_20261104.md#case-pathway_0147) | A | A, B | A, B | No |
| [pathway_0159](../reports/liveproteinbench_transfer_reassessment_20261102/multiple_defensible_by_both_86_20261104.md#case-pathway_0159) | A | A, B | A, B | No |
| [pathway_0174](../reports/liveproteinbench_transfer_reassessment_20261102/multiple_defensible_by_both_86_20261104.md#case-pathway_0174) | A | A, C | A, C | No |
| [pathway_0185](../reports/liveproteinbench_transfer_reassessment_20261102/multiple_defensible_by_both_86_20261104.md#case-pathway_0185) | D | A, D | A, D | No |
| [pathway_0189](../reports/liveproteinbench_transfer_reassessment_20261102/multiple_defensible_by_both_86_20261104.md#case-pathway_0189) | A | A, B, C | A, C, B | No |
| [pathway_0197](../reports/liveproteinbench_transfer_reassessment_20261102/multiple_defensible_by_both_86_20261104.md#case-pathway_0197) | C | C, D | C, D | No |
| [ph_0000](../reports/liveproteinbench_transfer_reassessment_20261102/multiple_defensible_by_both_86_20261104.md#case-ph_0000) | A | A, B | A, B | No |
| [ph_0008](../reports/liveproteinbench_transfer_reassessment_20261102/multiple_defensible_by_both_86_20261104.md#case-ph_0008) | B | B, C | B, D | No |
| [ph_0023](../reports/liveproteinbench_transfer_reassessment_20261102/multiple_defensible_by_both_86_20261104.md#case-ph_0023) | A | A, C | A, C | No |
| [ph_0036](../reports/liveproteinbench_transfer_reassessment_20261102/multiple_defensible_by_both_86_20261104.md#case-ph_0036) | B | A, B | A, B | No |
| [ph_0039](../reports/liveproteinbench_transfer_reassessment_20261102/multiple_defensible_by_both_86_20261104.md#case-ph_0039) | C | B, C | B, C | No |
| [ph_0040](../reports/liveproteinbench_transfer_reassessment_20261102/multiple_defensible_by_both_86_20261104.md#case-ph_0040) | D | A, C, D | C, D | No |
| [ph_0042](../reports/liveproteinbench_transfer_reassessment_20261102/multiple_defensible_by_both_86_20261104.md#case-ph_0042) | B | B, D | B, D | No |
| [ph_0048](../reports/liveproteinbench_transfer_reassessment_20261102/multiple_defensible_by_both_86_20261104.md#case-ph_0048) | A | A, D | A, D | No |
| [ph_0049](../reports/liveproteinbench_transfer_reassessment_20261102/multiple_defensible_by_both_86_20261104.md#case-ph_0049) | D | A, D | A, D | No |
| [ph_0053](../reports/liveproteinbench_transfer_reassessment_20261102/multiple_defensible_by_both_86_20261104.md#case-ph_0053) | A | A, D | A, D | No |
| [temperature_0002](../reports/liveproteinbench_transfer_reassessment_20261102/multiple_defensible_by_both_86_20261104.md#case-temperature_0002) | B | B, C | A, B, C | No |
| [temperature_0009](../reports/liveproteinbench_transfer_reassessment_20261102/multiple_defensible_by_both_86_20261104.md#case-temperature_0009) | C | B, C, D | B, C | No |
| [temperature_0021](../reports/liveproteinbench_transfer_reassessment_20261102/multiple_defensible_by_both_86_20261104.md#case-temperature_0021) | A | A, C | A, C | No |
| [temperature_0024](../reports/liveproteinbench_transfer_reassessment_20261102/multiple_defensible_by_both_86_20261104.md#case-temperature_0024) | C | A, C, D | A, C, D | No |
| [temperature_0031](../reports/liveproteinbench_transfer_reassessment_20261102/multiple_defensible_by_both_86_20261104.md#case-temperature_0031) | A | A, C | A, C | No |
| [temperature_0034](../reports/liveproteinbench_transfer_reassessment_20261102/multiple_defensible_by_both_86_20261104.md#case-temperature_0034) | C | B, C | B, C | No |
| [transmembrane_0005](../reports/liveproteinbench_transfer_reassessment_20261102/multiple_defensible_by_both_86_20261104.md#case-transmembrane_0005) | C | A, C | A, C | No |
| [transmembrane_0008](../reports/liveproteinbench_transfer_reassessment_20261102/multiple_defensible_by_both_86_20261104.md#case-transmembrane_0008) | A | A, B | A, B | No |
| [transmembrane_0009](../reports/liveproteinbench_transfer_reassessment_20261102/multiple_defensible_by_both_86_20261104.md#case-transmembrane_0009) | D | C, D | C, D | No |
| [transmembrane_0021](../reports/liveproteinbench_transfer_reassessment_20261102/multiple_defensible_by_both_86_20261104.md#case-transmembrane_0021) | B | B, C | B, C | No |
| [transmembrane_0026](../reports/liveproteinbench_transfer_reassessment_20261102/multiple_defensible_by_both_86_20261104.md#case-transmembrane_0026) | B | B, C | B, C | No |
| [transmembrane_0034](../reports/liveproteinbench_transfer_reassessment_20261102/multiple_defensible_by_both_86_20261104.md#case-transmembrane_0034) | D | B, D | B, D | No |
| [transmembrane_0035](../reports/liveproteinbench_transfer_reassessment_20261102/multiple_defensible_by_both_86_20261104.md#case-transmembrane_0035) | A | A, B | A, B | No |
| [transmembrane_0039](../reports/liveproteinbench_transfer_reassessment_20261102/multiple_defensible_by_both_86_20261104.md#case-transmembrane_0039) | D | C, D | A, D | No |
| [transmembrane_0040](../reports/liveproteinbench_transfer_reassessment_20261102/multiple_defensible_by_both_86_20261104.md#case-transmembrane_0040) | B | B, C | B, C | No |
| [transmembrane_0048](../reports/liveproteinbench_transfer_reassessment_20261102/multiple_defensible_by_both_86_20261104.md#case-transmembrane_0048) | D | B, D | B, D | No |
| [transmembrane_0063](../reports/liveproteinbench_transfer_reassessment_20261102/multiple_defensible_by_both_86_20261104.md#case-transmembrane_0063) | D | B, D | B, D | No |
| [transmembrane_0073](../reports/liveproteinbench_transfer_reassessment_20261102/multiple_defensible_by_both_86_20261104.md#case-transmembrane_0073) | A | A, B | A, B | No |
| [transmembrane_0076](../reports/liveproteinbench_transfer_reassessment_20261102/multiple_defensible_by_both_86_20261104.md#case-transmembrane_0076) | C | A, C | A, C | No |
| [transmembrane_0082](../reports/liveproteinbench_transfer_reassessment_20261102/multiple_defensible_by_both_86_20261104.md#case-transmembrane_0082) | A | A, C | A, C | No |
| [transmembrane_0086](../reports/liveproteinbench_transfer_reassessment_20261102/multiple_defensible_by_both_86_20261104.md#case-transmembrane_0086) | D | C, D | C, D | No |
| [transmembrane_0100](../reports/liveproteinbench_transfer_reassessment_20261102/multiple_defensible_by_both_86_20261104.md#case-transmembrane_0100) | C | B, C | C, D | No |
| [transmembrane_0105](../reports/liveproteinbench_transfer_reassessment_20261102/multiple_defensible_by_both_86_20261104.md#case-transmembrane_0105) | B | B, C | B, C | No |
| [transmembrane_0111](../reports/liveproteinbench_transfer_reassessment_20261102/multiple_defensible_by_both_86_20261104.md#case-transmembrane_0111) | D | B, D | B, D | No |
| [transmembrane_0115](../reports/liveproteinbench_transfer_reassessment_20261102/multiple_defensible_by_both_86_20261104.md#case-transmembrane_0115) | A | A, C | A, C | No |
| [transmembrane_0123](../reports/liveproteinbench_transfer_reassessment_20261102/multiple_defensible_by_both_86_20261104.md#case-transmembrane_0123) | B | A, B | A, B | No |
| [transmembrane_0124](../reports/liveproteinbench_transfer_reassessment_20261102/multiple_defensible_by_both_86_20261104.md#case-transmembrane_0124) | B | A, B | A, B | No |
| [transmembrane_0132](../reports/liveproteinbench_transfer_reassessment_20261102/multiple_defensible_by_both_86_20261104.md#case-transmembrane_0132) | B | B, D | B, D | No |
