# DeepFRI-derived P12–P15 source and confidence audit

All four source contracts and disabled Qwen sparse-confidence proposals are prepared. No inference, provider call, training, central authorization or queue change was performed.

| Task | Branch | Released test IDs | Classes | Current RDKit PDBs | Printed native count |
| --- | --- | ---: | ---: | ---: | ---: |
| P12 | EC | 1919 | 538 | 1853 | 1840 |
| P13 | BP | 3416 | 1943 | 3129 | 2991 |
| P14 | MF | 3416 | 489 | 3129 | 2991 |
| P15 | CC | 3416 | 320 | 3129 | 2991 |

Native Zenodo test-only ZIPs total 271,260,486 bytes. Member CRC/size and local SHA-256 are verified; complete parent-archive MD5s are unverified because training/validation structures were skipped. Exact publisher URLs, revisions and hashes are in the source manifest and JSON audit.

Full released FASTA and PDB-modeled residues remain separate. Only 105 EC and 142 GO parsed sequences equal full FASTA; 1,748 EC and 2,987 GO differ. The qualified current parser projection cannot establish the authors’ unpublished parsed cache. Native ProtST consumes residue identities and crops to first 550 modeled residues. Every prepared source sequence remains complete.

Retired-ID replacements, one outside-test EC FASTA record, and one missing GO test PDB are recorded explicitly. Qwen proposals use exact Zenodo released test lists with complete FASTA, not claimed native paper case identity. Global vocabulary order is complete source-header order, never selected by test-positive labels. GO names are exact native headers; EC supplemental names use ExPASy 02-Sep-2026, including 12 transferred/deleted entries without remapping the original 538 IDs.

[Pinned TorchDrug metric code](https://github.com/DeepGraphLearning/torchdrug/blob/6066fbd82360abb5f270cba1eca560af01b8cc90/torchdrug/metrics/metric.py) defines flattened rank-average `auprc@micro` and rank-position `f1_max`. Ties can be evaluated within a score block, unlike sklearn’s threshold-grouped micro AP. Native and supplemental metrics retain separate names; the better result is never selected.

GO reference annotations already include source OBO reachability closure, excluding the three roots. Native ProtST scoring applies no output-score propagation. Exact author OBO bytes/version are absent from audited assets; the source collection script uses an unversioned URL. This blocks exact closure regeneration, not scoring the provided target matrix. Current GO was not substituted.

Final disabled proposals are `configs/local_deepfri_p12_sparse_confidence_proposed.json` through `p15`; earlier disabled snapshots are preserved. An explicit final numeric JSON scores map declares omitted classes zero; an explicit empty scores object is valid. Constant, binary and tied numeric vectors remain valid. Missing/malformed/truncated answers are invalid, with no repair or hard-label conversion. Any invalid planned vector makes full AP/Fmax null; parsed-only metrics remain separate.

The scorer locks all raw outputs/missing slots and validates manifest/config/model/input/reference hashes before labels. CPU float32 native scoring freezes Torch 2.13.0+cu132 and one intraop/interop thread. Separate sklearn 1.5.2 AP uses the existing isolated environment; serving packages were unchanged. `OFFLINE_ALL_ZERO_REFERENCE` is a predeclared diagnostic, never model predictions or invalid-output replacement. Historical author GPU tie equivalence is unknown.

Actual tokenizer input IDs verify all 12,167 prompts fit 262,144 tokens. Maximum prompt lengths: EC 11,353 / BP 33,203 / MF 9,627 / CC 5,677, plus unchanged 4,096 output tokens. Total volume is 183,005,770 prompt tokens without cache savings and at most 49,836,032 output tokens. Fixed vocabulary follows the varying sequence, so ordinary shared-prefix savings are not assumed. Output validity and quality remain unmeasured.

The [official ProtST release](https://github.com/DeepGraphLearning/ProtST) advertises three pretraining checkpoints. Safe ZIP metadata inspection found no downstream task MLP; tensor weights were not downloaded or unpickled. Source downstream evaluation first trains a fresh head. No frozen EC/GO task head was found in audited official assets. Author task checkpoints plus class/case/dependency identity are needed for native specialist reproduction without training.

Separate DeepFRI trained-model archives are reachable, about 904/872 MB, but their contents were not acquired or validated. They would be a different specialist baseline, not an automatic replacement for Qwen or ProtST.

Ten reporter, four preparation, three sparse-contract, two range-ZIP and six scorer synthetic tests pass. Original first LitQA2 artifacts, interpretation registry, held content and frozen genomic files remain unchanged. Prediction agreement does not validate explanations, calibration, mechanisms or biological absence. Public pretraining exposure is unknown.
