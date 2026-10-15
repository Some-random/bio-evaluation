# Biological evaluation collection
Reviewed 2026-10-12

## What is included
- **64 biological/biomedical evaluation settings** and **14 general-model control groups**.
- A scored task is not always an independent dataset: several settings reuse a source with different outputs, splits or allowed information.
- **25 metric explanations**, **26 official entry points**, and a paper-to-task crosswalk.
- Excel, CSV and JSON representations of the catalog. No trained model or new prediction result.

## What is NOT included
Raw benchmark datasets, papers' full copyrighted text, model weights and a universal runnable evaluation harness are not bundled.
Public documentation and resource pages were accessible. Direct network requests from the working container failed DNS resolution, so no raw-data downloads are claimed.

## Reading order
1. **Biological tasks**: What is the question? What input does the student receive? What is its output? What supplies the reference?
2. **Protocols**: Match the ID to metric, split/version, implementation and caveat.
3. **Paper map**: See which evaluations a paper actually reports.
4. **Metrics**: Interpret the score; do not conflate it with the underlying biological property.
5. **Resources / Limits**: Resolve acquisition and protocol details before running.
6. **General controls**: OLMo/DCLM checks belong here, separate from biological outcomes.

## The main scientific questions
- **Protein annotation/property**: given a sequence, predict function, location, solubility, interaction, or a measured property.
- **Mutation prediction**: given a reference and changes, predict the change's observed outcome.
- **Mutation proposals**: given an objective, find good changes; retrieving one annotated answer is a different metric from experimental hit rate.
- **Protein–text reasoning**: explain function or mutation effects; wording overlap is not proof of mechanism.
- **Structure reconstruction/design**: compare coordinates or sequence with an existing complex; not a fresh binding experiment.
- **Research evidence QA**: answer from literature, figures, tables, databases or sequences; resource allowance changes the task.
- **Generation diagnostics**: diversity, novelty and predictor scores describe candidate samples, not necessarily successful function.

## Agent handoff: acquisition and evaluation boundaries
This file is a reference, not authorization to train models or download every large dataset.
When implementing a selected evaluation:
1. Use its official entry point and pin the release / commit and exact split.
2. Keep benchmark evaluation records out of training, midtraining, SFT, distillation and retrieval corpora. PG-LLM explicitly prohibits benchmark-specific tuning on its splits.
3. Preserve the task's allowed input. Do not leak reference labels or teacher-only evidence into the student prompt.
4. Use the original metric implementation, including thresholds, tie handling, ontology propagation, normalization and aggregation.
5. Keep numerical assays separate. Aggregate per assay or other specified unit rather than merging incompatible outcomes.
6. Distinguish zero-shot inference, few-shot prompting and supervised head fitting; they are different protocols.
7. Keep experimental outcomes, curated annotations, structure-derived facts and learned-scoring-model outputs distinguishable.
8. Save exact predictions and per-example provenance. State missing dependencies rather than replacing the evaluation silently.

## Scope boundaries
The current core reading is BioT5+, MutaPLM and ProtST, plus LLaVA-Med/PMC-VQA for image evidence.
Earlier NatureLM, Proteo-R1, BioReason, BioReason-Pro, Ryze, STRIDE and biological-posttraining evaluations are retained for continuity.
NatureLM and BioT5+ are protein-focused here; their unrelated molecule/material/genomics task suites are not expanded. Drug–target interaction is included as an explicitly labeled cross-domain setting.
Main benchmark protocols and relevant auxiliary evaluations are catalogued; not every experimental ablation or individual subtask in OLMo/DCLM.
The prior uploaded/generated evaluation workbook was used to recover the earlier list; this collection adds primary-source checks and does not treat prior assistant text as independent evidence.

## Useful non-equivalences
- PEER/TAPE **stability regression** is not automatically NatureLM's **stability classification**.
- **Membrane-versus-soluble localization** is not the same test as **expression solubility**.
- **ProteinGym** is a suite of assays; **PG-LLM** packages an evaluation-only ranking interface; **PFArena** changes the task and supplied evidence.
- A **TCR–peptide** or generic **protein–protein interaction** label is not an Affibody–pMHC label.
- **Fmax** is a threshold-maximized retrospective score, not a frozen operating threshold.
- **AP** is not necessarily trapezoidal AUPRC.
- **High pLDDT**, **low docking energy**, **native sequence recovery** and **experimental binding** are distinct claims.
- A held-out figure question judged against a generated caption-derived answer is not the same evidential standard as an independently measured protein outcome.
- No catalogued public dataset establishes the exact Stage-3 full-peptide × Affibody outcomes in Xinyu's experiment.

## Unresolved access items
The exact official PFArena release link, some NatureLM processed tests, Proteo-R1's full processed holdout, and the biological-posttraining study's complete adapted species/test manifests were not established.
MutaDescribe's HF viewer currently shows mixed-schema errors; use dataset files and the official loader.
Some older conversation uploads expired; an upload-specific verification requires the exact file to be available again.
