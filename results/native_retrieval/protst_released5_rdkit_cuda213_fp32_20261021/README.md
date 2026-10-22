# ProtST protein retrieval (2023)

The released ProtST-ESM1b/PubMedBERT model returned 20 ranked proteins for each of the five released queries over 34,464 retained corpus inputs. These are native ProtST results; Qwen was not used.

The release has no query relevance labels or aggregate accuracy metric, so biological correctness is unscored. The corpus uses a declared RDKit projection: 2,171 of 36,635 source candidates were rejected before inference. Full historical graph/cohort or numerical ranking equivalence is not claimed.

| Released query | Retrieved proteins in rank order |
|---|---|
| FUNCTION: Binding to ATP, adenosine 5'-triphosphate, a universally important coenzyme and enzyme regulator. | 3B9J-A, 2ROP-A, 3JSK-A, 6DZ3-A, 1NB0-A, 4Y4N-A, 4Y72-C, 1S6U-A, 2EW9-A, 5KNP-A, 1Y3K-A, 1BUH-B, 2RML-A, 6CZM-A, 6QD5-A, 4H65-A, 1Q8L-A, 3G4C-A, 1N08-A, 1JWB-B |
| FUNCTION: Binding to a heme, a compound composed of iron complexed in a porphyrin (tetrapyrrole) ring. | 3EQ1-A, 4RHE-A, 3FNV-A, 5CCX-A, 5W56-A, 4N8U-A, 5LZL-A, 4H65-A, 3PDI-A, 5TRE-a, 1ZR9-A, 4AC8-A, 1ZPU-A, 4AP8-A, 6FCO-A, 5CCB-B, 5L8X-A, 1VH8-A, 3AEU-A, 3G4C-A |
| FUNCTION: Binding to GTP, guanosine triphosphate. | 3LMK-A, 5FBH-B, 6N4X-A, 1ISS-A, 6BT5-A, 5CNM-A, 6N4Y-A, 6BAP-A, 5KZQ-A, 5X2N-B, 4OUR-B, 4R70-A, 5C5K-A, 5CNI-A, 3NOT-C, 2VEA-A, 5C5C-A, 6GFL-A, 6G1Y-A, 1DCF-A |
| FUNCTION: Binding to pyridoxal 5' phosphate, the biologically active form of vitamin B6. | 4H65-A, 1UMY-A, 4AP8-A, 2ROP-A, 5DML-A, 6CZM-A, 6FCO-A, 6FCX-A, 1S6U-A, 4AF3-D, 6J79-A, 5LZL-A, 2VFA-A, 2M5O-A, 1Q8L-A, 3KSV-A, 3EQ1-A, 2N7Y-A, 2RML-A, 1VEH-A |
| FUNCTION: Binding to the oxidized form, NAD, of nicotinamide adenine dinucleotide, a coenzyme involved in many redox and biosynthetic reactions. | 3ES9-A, 2BN4-A, 3QFR-A, 6J79-A, 3JSK-A, 3B9J-A, 3FJO-A, 3IWD-A, 5CAX-A, 4Y4N-A, 6FCO-A, 1S6U-A, 2N7Y-A, 4YRY-B, 2ROP-A, 1RZ1-A, 2K3J-A, 2CFY-A, 1TLL-A, 5KZ5-A |

[Original paper](https://arxiv.org/abs/2301.12040). Exact query texts, ranked IDs, score tensors and hash-verified output records accompany this report. The archive contains no checkpoint, credential or reference label.
