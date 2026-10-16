# FigQA / TableQA postrun integrity audit

No local target leakage, permutation error, image/case mismatch or saved-score arithmetic discrepancy detected in all425completed cases.

| Setting | Cases / original images | Correct / accuracy | Integrity result |
| --- | --- | --- | --- |
| B04 FigQA | 181 / 181 | 137 / 75.69% | All source prompts, choice/target permutations, image order/bytes, actual requests and saved score flags reconcile |
| B05 TableQA | 244 / 262 | 216 / 88.52% | All source prompts, choice/target permutations, image order/bytes, actual requests and saved score flags reconcile |

The audit independently recomputed publisher parquet SHA-256 digests, reconstructed the seed42 choice permutations and native text rendering, and matched every request to its source case and image bytes. Correct and abstention targets stay outside the solver payload. All saved response hashes match their pre-scoring locks; saved parser answers, correctness flags and aggregate arithmetic agree with the original references. No model output was reparsed and no rationale was graded.

The higher scores than [Ryze Table1](https://arxiv.org/html/2606.00902v1#S3.T1) therefore have no detected local bookkeeping explanation. This audit cannot rule out prior public-data exposure, dataset shortcuts or differences in model/image processing and evaluation regimes. It does not establish a controlled model ranking or stronger biological reasoning.

No inference or existing-artifact changes occurred. The audit read only B04/B05 source data and task-specific run inputs; the reference-letter/count metadata prefix stopped before B06. Full425-case hashes and checks are in the [JSON audit](labbench_vision_postrun_integrity_audit.json).
