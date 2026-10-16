#!/bin/bash
#SBATCH --partition=il-cpu
#SBATCH --qos=il-cpu
#SBATCH --cpus-per-task=2
#SBATCH --mem=4G
#SBATCH --time=14-00:00:00
#SBATCH --job-name=bio-eval-reporting
#SBATCH --output=/dfs/scratch0/dongweij/bio-evaluation/.local/continuation_2026-10-16/logs/coordinator-%j.log
set -euo pipefail
umask 077
local_base="${SLURM_TMPDIR:-/tmp}"
runtime_dir="$(mktemp -d "$local_base/bio-eval-continuation-${SLURM_JOB_ID}-XXXXXX")"
trap 'rm -rf -- "$runtime_dir"' EXIT
python3 /dfs/scratch0/dongweij/bio-evaluation/.local/continuation_2026-10-16/bootstrap_coordinator.py --config /dfs/scratch0/dongweij/bio-evaluation/.local/continuation_2026-10-16/coordinator_config.json --config-sha256 14a54fe3dfd49a0aac66323e1f35acd22285e83ec48fae9704e06d57e7df82d2 --runtime-dir "$runtime_dir"
