# Biological evaluation workspace

Private research workspace covering 64 biological evaluation settings. The first local Qwen3.8-27B run completed on 15 October 2026 UTC: **197 reviewed public LAB-Bench LitQA2 questions, 77 correct (39.1% accuracy), 41.0% precision and 95.4% coverage**. No requests failed and all outputs parsed. This is one seeded public subset run; explanation support is unassessed and pretraining exposure is unknown.

- [First local results and paper context](reports/FIRST_LOCAL_EVALUATION.md)
- [Current evaluation overview](reports/PROJECT_OVERVIEW.md)
- [Task demands and score interpretation](reports/INTERPRETATION_TABLE.md)
- [Readiness of all 64 settings](reports/per_task_readiness.csv)
- [Leakage and memorization controls](reports/MEMORIZATION_PROTOCOL.md)
- [Verified checkpoint and server setup](reports/LOCAL_MODEL_SETUP.md)
- [Native LAB-Bench input corrections](reports/LABBENCH_NATIVE_INPUT_REVIEW_2026-10-15.md)
- [Private snapshot and restore instructions](reports/BACKUP_SETUP.md)

All eight public LAB-Bench categories have complete native preparation (1,967 cases), including required figure/table images, paper titles/DOIs and full protocols. Other local evaluation case reviews and frozen execution configs are pending. The OpenAI inference hold and held pathogen-fitness requests remain in place. This repository is an archive and working record, not permission to run unreviewed tasks or change native benchmark restrictions.

Code, configurations, reports, handoff materials and interpretation metadata are stored directly in Git. `artifacts/manifest.json` inventories the compressed snapshot of all data, sources, raw requests/responses, results and logs. Parts in `artifacts/` remain below GitHub's individual-file limit. The complete original BF16 Qwen checkpoint, including all 18 weight files and supporting files, is packaged in the private `snapshot-2026-10-15` release; it is published only after GitHub's asset sizes and SHA-256 digests match the local manifest. See `reports/qwen_checkpoint_release_manifest.json` for checkpoint part/file hashes.

Credentials, virtual environments, package/build/download caches and transient process state remain local. Source-pinned model files, evaluation data and work are preserved. No unrelated Affibody workspace is included. This upload is one-time; automatic daily uploads remain disabled.

This repository and its archives contain scorer-only reference answers. Keep them outside solver tools, training and retrieval corpora. Task-demand labels remain provisional; outcome agreement does not establish explanation correctness. Read [the execution addendum](handoff/EXECUTION_EXAMPLES.md) and `AGENTS.md` before continuing. The addendum's illustrative examples are not benchmark data.
