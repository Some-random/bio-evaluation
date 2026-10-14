# Private repository and daily backup

The user requested a private repository and daily uploads for this evaluation
workspace on 14 October 2026 UTC. Repository creation and pushes are authorized;
paid biological inference remains separately unapproved.

The proposed name is `bio-evaluation`, under the GitHub account authenticated
on this server. Set `owner` in `configs/backup.json` for an explicit account.
The backup verifies GitHub's private flag before every push and never changes
an existing remote or forces a push. A repository-name collision stops creation.

Code, protocols, the original handoff, configuration, reports and interpretation
metadata are committed directly. All permitted files in `data/`, `sources/`,
`results/` and `logs/` are included in a deterministic compressed archive under `artifacts/`.
The archive is split into parts of at most 90 MiB to fit GitHub's file limits.
Its manifest records every included data file's size and SHA-256 hash.

Credentials, local backup runtime state, environments and caches stay
local. Credential filename rules and common credential-content checks run before
commit or upload; archive members are checked too. These checks are useful
guards, not a guarantee that every possible secret format can be detected.
Snapshots contain held-out evaluation material: do not use the backup repository
as model training material, a solver retrieval index, or a solver workspace.

The daily cron entry is `/etc/cron.d/dongwei-bio-evaluation-backup`, scheduled
at **10:00 UTC / 02:00 PST (fixed UTC−8)**. It runs on the server independently
of this chat while the server and cron service are running. It commits first,
then uploads; a failed upload preserves the local commit for the next run.
Runtime status is `.local/backup_status.json`; job logs are `.local/backup.log`.

Authenticate on the server without pasting a credential into chat:

```bash
gh auth login --hostname github.com --git-protocol https --web
python3 /data/rustfs1/dongweij/bio-evaluation/scripts/daily_backup.py
```

The GitHub CLI must retain authentication on this server for unattended pushes.
A connected chat plugin alone does not establish server authentication.
Creating a private repo needs account permission; an OpenAI API key cannot
provide GitHub access. No unrelated workspace or Affibody files are included.
Manually created Git commits require a history review before the automatic job
will upload them; ordinary uncommitted workspace changes are handled automatically.

Restore archived files into a separate trusted directory after joining the
parts in manifest order. For the current archive, this command lists contents:

```bash
cat artifacts/evaluation-assets.tar.gz.part* | tar -tzf -
```

Before extraction, verify the concatenated SHA-256 against `artifacts/manifest.json`.
The archived paths retain their original top folders, including any evaluation logs.
Future large files should be placed in those directories. No model responses
or numerical biological scores existed when the backup was first prepared.
