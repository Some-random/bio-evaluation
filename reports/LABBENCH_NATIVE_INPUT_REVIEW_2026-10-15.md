# Native LAB-Bench input review (15 October 2026 UTC)

The pinned task implementations confirm that B01 LitQA2, B02 DbQA, B07 SeqQA and B08 CloningScenarios use the base question/choice interface. LitQA2 source passages and source lists are not native zero-shot solver inputs. Current Qwen LitQA2 prompt bytes remain identical to the previous preparation.

Two older preparation omissions were found before any local execution of those categories: all 82 SuppQA cases need the paper title and DOI; all 108 ProtocolQA cases need the full protocol concatenated with the question. The old preparation omitted those required fields and cannot support a native comparison for those two categories. No successful model predictions for B03 or B06 are being presented as native results.

`prepare_labbench.py` now restores those exact task transformations, confirmed against the pinned official method code using synthetic fixtures. It writes a new `data/labbench_native_complete/` directory and refuses the old directory/report paths. It does not alter any frozen current run inputs or manifests. The original preparation is retained as provenance.

Both previously missing image parquet files were downloaded from the pinned public release and verified against publisher LFS SHA-256 digests. The complete preparation has 181 FigQA questions with 181 images and 244 TableQA questions with 262 images, preserving multiple table images per case. No captions, paper text or answer keys are added to the solver payloads.

The resulting release contains 1,967 public cases across all eight categories. These are prepared cases, not executed results or a local inference allowlist. Detailed counts and hashes are in `labbench_native_complete_preparation.json`; input checks are in `labbench_native_complete_validation.json`; source fetch hashes are in `../sources/lab_task_contract_fetch_2026-10-15.json`.

The first local run remains the 197 reviewed LitQA2 cases. The two held cases and all flagged P18 requests remain held, and OpenAI inference remains suspended. Other local categories require input review before dispatch.
