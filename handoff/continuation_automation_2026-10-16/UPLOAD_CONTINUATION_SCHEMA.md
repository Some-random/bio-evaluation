# Continuation uploader contract

`upload_continuation.py` only backs up the frozen 59-case P36 condition and the exact verified source-preparation bundle. It never starts inference, scores outputs, changes frozen files, or marks the original full P36 benchmark complete. Importing it makes no network request and reads no credentials. The process uses its own checkout, leaving the remaining-evaluations uploader unchanged.

The local renderer pointer is `results/runs/p36-qwen3.8-27b-biot5-reviewed59-20261016/upload_status.json`; the same schema is pushed from the isolated checkout. The stable Git pointer also includes README, case index, archive manifests, frozen configuration, input review and the most recent metadata archive. Raw pairs and scorer files are private release assets with individual-file and whole-archive SHA-256 manifests.

| Field | Meaning |
|---|---|
| `task_id` | Always `P36`. |
| `planned` | Always 59 input-reviewed cases. |
| `full_source_cases` | Always 5,876; this is not the evaluated denominator. |
| `full_benchmark_complete` | Always false. |
| `uploaded_trajectories` | Saved request/response pairs archived and published; includes error responses, excludes request-only dispatches. |
| `uploaded_completed_pairs` | Archived HTTP-200 pairs with completed status, one final string, and exact preserved API-body/content/provenance alignment. |
| `uploaded_error_response_pairs` | Archived saved error responses, including null-final-content errors. These are preserved immediately. |
| `uploaded_ambiguous_request_records` | Archived requests with no saved response, admitted only after generation is terminal. |
| `generation_terminal` | Dispatch summary or terminal completion receipt exists. |
| `scoring_terminal` | Completion receipt exists or all four expected scoring artifacts exist. This field does not assert scorer success. |
| `scoring_success` | Scope, output lock, saved file hashes, ordered 59-case scorer slots and finite ROUGE-L validate; a known nonzero scoring exit code makes this false. |
| `metrics`, `metric_label`, `comparison_qualification` | Copied unchanged from saved scores only when `scoring_success` is true. No calculations or metric substitutions. |
| `status` | Local upload-cycle/publication state. |
| `updated_at_utc` | Pointer update time. |

Successful scoring validation requires the exact task/variant/model revision, planned59/full5876 metadata, `full_benchmark_complete:false`, finite ROUGE-L in [0,1], a matching contract hash over the manifest plus both request/response slots for all59 cases, each saved/absent slot matching its lock, and an ordered59-slot per-case artifact. Terminal score artifacts are preserved even when they do not establish full-source completion. The metric remains qualified released-code paired-reference ROUGE, not normalized Smith-Waterman or a biological-function assay.

The allowlist excludes the full5,876-case source JSON, `input_review_index.jsonl`, outside-prefix raw text, model weights, environments, credentials and unrelated projects. Metadata consists of configuration, input-review IDs/hashes/reasons, source provenance/licensing/code, dispatch/completion summaries and terminal scorer evidence. Request payloads must match the exact59-case input contract. No request-only pending dispatch is uploaded while generation runs. Previously archived records and manifests cannot be overwritten with different bytes.

Private-repository and push permission are checked before publication, uploads and pushes. A failed push is retried on later cycles; concurrent main updates are rebased without a force push. Redirected asset verification strips credentials. All candidate files and archives pass the existing repository scanner. `--once` runs one upload cycle; the default loop retries every60 seconds. No process is started by the handoff itself.
