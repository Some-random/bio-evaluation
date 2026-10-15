# Private repository snapshot

On 15 October 2026 UTC the user requested creating a private repository and uploading this evaluation workspace. Repository: [Some-random/bio-evaluation](https://github.com/Some-random/bio-evaluation). GitHub privacy and push permission were verified before data transfer. This is a one-time upload; the previously canceled daily schedule remains disabled.

The snapshot includes:

- Code, tests, configurations, reports, original handoff and interpretation metadata in Git.
- All evaluation inputs, cached public sources, raw requests/responses, scored results and logs in `artifacts/evaluation-assets.tar.gz.part*`, with per-file SHA-256 hashes in `artifacts/manifest.json`.
- The entire pinned Qwen3.8-27B BF16 checkpoint in the private `snapshot-2026-10-15` release: 18 weight files, 14 publisher supporting files and our completion receipt. Every publisher file is checked against its pinned digest while packaging; every uploaded part is checked against GitHub's size and SHA-256 digest. The original license is retained.

The checkpoint release contains 512 MiB uncompressed tar parts and a manifest. GitHub's release assets remain private with this repository. The release stays draft until all expected assets are verified; an interrupted upload resumes by matching existing asset digests. No completed asset is blindly overwritten.

Credentials, `.local/` process state, virtual environments and caches stay local. The source checkpoint files are preserved, so caches and installed packages do not need to be duplicated. No unrelated Affibody files are included. The backup does not change model execution scope or submit any benchmark inference.

`scripts/publish_private_snapshot.py` performs the one-time snapshot and upload. It uses the existing GitHub CLI login, with per-process proxy scheme handling; it opens no SSH connection and changes no global proxy or Git credential setting. Credential filename/content checks include archive members and existing Git history. Runtime progress is `.local/github_upload/progress.json` and the worker log is `.local/github_upload/worker.log`. A process lock prevents duplicate jobs.

To restore evaluation data after cloning, verify the concatenated SHA-256 in `artifacts/manifest.json` and the listed per-file hashes, then extract the archive into a trusted copy of this workspace:

```bash
cat artifacts/evaluation-assets.tar.gz.part* | tar -xzf -
```

To restore the complete checkpoint, authenticate to GitHub for this private repo, download its release parts, verify their sizes/SHA-256 against `reports/qwen_checkpoint_release_manifest.json`, and join them in manifest order:

```bash
gh release download snapshot-2026-10-15 --repo Some-random/bio-evaluation --pattern 'qwen-checkpoint.tar.part*' --dir .local/checkpoint-release
cat .local/checkpoint-release/qwen-checkpoint.tar.part* | tar -xf -
```

This recreates `models/Qwen3.8-27B/`. The archive manifest records the checksum of the joined tar and every original file. Keep downloaded restore parts on a disk with sufficient space. The standard model download recipe also remains available if preferred.

Archives contain held-out reference labels and prior incident logs. Do not give the repository or backups to benchmark solver tools, use them as a training or retrieval corpus, or resume held biological requests through another provider.
