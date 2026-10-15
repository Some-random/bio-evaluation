# Private repository snapshot

On 15 October 2026 UTC the user requested creating a private repository and uploading this evaluation workspace. Repository: [Some-random/bio-evaluation](https://github.com/Some-random/bio-evaluation). GitHub privacy and push permission were verified before data transfer. This is a one-time upload; the previously canceled daily schedule remains disabled.

The snapshot includes:

- Code, tests, configurations, reports, original handoff and interpretation metadata in Git.
- All evaluation inputs, cached public sources, raw requests/responses, scored results and logs in `artifacts/evaluation-assets.tar.gz.part*`, with per-file SHA-256 hashes in `artifacts/manifest.json`.
- Pinned model references and verification records: Qwen/Qwen3.8-27B revision `1d4bf0f2ff6012fd82039f2fa52739d0dd7c60c0`, all 32 publisher file sizes/digests, precision, serving configuration and download/setup scripts.

The user explicitly chose to keep the public checkpoint local and back up references only. `configs/backup.json` therefore sets `include_checkpoint_in_private_release` to `false`. No model weight release assets are uploaded. The original verified checkpoint remains in `models/Qwen3.8-27B/` on the local data disk.

Credentials, model weights, `.local/` process state, virtual environments and caches stay local. No unrelated Affibody files are included. The backup does not change model execution scope or submit any benchmark inference.

`scripts/publish_private_snapshot.py` performs the one-time snapshot and upload. It uses the existing GitHub CLI login, with per-process proxy scheme handling; it opens no SSH connection and changes no global proxy or Git credential setting. Credential filename/content checks include archive members and existing Git history. Runtime progress is `.local/github_upload/progress.json` and the worker log is `.local/github_upload/worker.log`. A process lock prevents duplicate jobs.

To restore evaluation data after cloning, verify the concatenated SHA-256 in `artifacts/manifest.json` and the listed per-file hashes, then extract the archive into a trusted copy of this workspace:

```bash
cat artifacts/evaluation-assets.tar.gz.part* | tar -xzf -
```

On another machine, obtain the public checkpoint from its publisher at the exact revision in `configs/local_model.json`; the weights are not restored from GitHub. Check every file's size and publisher digest against `reports/local_model_complete_verification.json` before serving it. The original download/setup scripts and pinned source metadata are included. Read the resource and execution restrictions in `AGENTS.md` before starting setup or inference.

Archives contain held-out reference labels and prior incident logs. Do not give the repository or backups to benchmark solver tools, use them as a training or retrieval corpus, or resume held biological requests through another provider.
