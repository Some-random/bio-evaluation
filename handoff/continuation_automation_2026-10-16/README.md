# Evaluation reporting and continuation worker

CPU Slurm job **237895** runs the grouped GitHub report updater every five minutes and the new P36 trajectory uploader every minute. Both have completed their first private GitHub publication. The existing trajectory supervisor, eight GPU allocations, six sealed plans and 83,690 planned cases continue independently.

The supplemental P36 condition runs 59 individually reviewed cases through the existing Qwen vLLM server, using no additional GPU. Five other reviewed cases and 5,812 unreviewed cases remain held. This is a partial paired-reference ROUGE adaptation; full P36 completion, paper Smith–Waterman reproduction and biological function validation remain false. Saved malformed/error responses are archived alongside completed responses without retries or repair.

The coordinator starts the frozen offline CPU scorer after generation ends, then the uploader preserves its artifacts and the overview can display the qualified subset score. It never starts or retries model generation. A failed/interrupted scoring attempt remains recorded; existing validated score artifacts can be reused.

## Deployment record

See [deployment.json](deployment.json) for the submitted command, resources, first verified commits and exact source hashes. The files here preserve the deployed implementation and absolute paths. The active copies live under `.local/continuation_2026-10-16/`; the running CPU job owns its isolated temporary runtimes. Model weights, credentials, environments and raw benchmark inputs/targets are excluded from this handoff.

The report publisher owns only its six generated report files and uses `.local/reporting_updater/upload_checkout`. The P36/source uploader owns its two result directories and a separate checkout. Both verify the private repository and use explicit staged paths; the original trajectory uploader's checkout remains independent. The report publisher rejects conflicting upstream edits to its owned generated files. A transient upload error preserves the last verified progress counts and timestamps; missing both source snapshots stops publication before any report is overwritten.

Metadata refresh and Git publishing use the repository's existing private credential helper and archive scanner. Deployment tests cover refresh/completion accounting, concurrent Git pushes, ownership checks, immutable trajectory/member hashes, error-response preservation, source exclusion and one-shot scoring. The exact P36 scientific condition and restoration code are in [the subset handoff](../p36_reviewed_subset_2026-10-16/README.md).
