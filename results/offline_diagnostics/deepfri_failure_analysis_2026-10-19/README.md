# P12–P15 offline failure analysis evidence

This bundle preserves a separately named diagnosis of existing Qwen outputs. It contains no new model generations, repaired predictions, or replacement historical scores.

For each task:

- `*_output_diagnoses.jsonl.gz` contains all original case IDs, final-answer text, finish reason, output budget, original sparse vector or invalid status, and the frozen diagnostic partition/crosscuts. No reasoning field is used.
- `*_source_inventory.jsonl.gz` records the exact original request/response file hashes and the payload hash for every case.
- `*_matched_subset.jsonl.gz` contains the exact ordered parsed subset, unchanged sparse scores, and scorer-only positive class indices used by both the model and all-zero baseline. Class index order is in `analysis.json`.

`classification_rules.json` and `classification_frozen.json` record the rules, code/test hashes, source identities and classifications frozen before this analysis opened reference labels. `vector_provenance_receipt.json` separately confirms that every valid saved sparse vector equals its exact final-answer JSON.

`analysis.json` is byte-identical to the structured report under `reports/`. `native_metric.py` preserves the pinned TorchDrug source (revision `6066fbd82360abb5f270cba1eca560af01b8cc90`, SHA-256 `760f376d4125ab2cc9332c9e83b944d4464da51aea577d75266d9247aca81776`). Only the `area_under_prc` and `f1_max` functions are extracted for evaluation; the module's unrelated dependencies are not imported.

Reproduce the portable subset calculation from the repository root:

```bash
python scripts/verify_deepfri_matched_subset.py
```

The recorded runtime is Python 3.12.15, Torch 2.13.0+cu130 and NumPy 2.3.5, using CPU float32 scores and one thread. The verifier checks these Torch/NumPy versions, evidence hashes, exact selected IDs, equality to final-answer JSON, both source metrics and the tie-grouped AP before reporting success. No GPU or API is used.

The all-zero reference uses the same cases and classes as the model subset. It does not impute missing model answers. Full-test primary metrics remain undefined under the separately declared local completeness policy. The full-set historical all-zero reference is retained in `analysis.json`, but is not the matched comparison.

This bundle contains held-out evaluation targets. Do not supply it to a benchmark solver or use it to tune prompts, sampling, extraction, or model selection.
