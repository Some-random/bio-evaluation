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
python3 /dfs/scratch0/dongweij/bio-evaluation/.local/continuation_2026-10-16/bootstrap_coordinator.py --config /dfs/scratch0/dongweij/bio-evaluation/.local/continuation_2026-10-16/coordinator_config.json --config-sha256 fdd067d1c4f3a5cdad46d6a2ba9fada1e73966b3a4c172556217eae7ce8ddc39 --runtime-dir "$runtime_dir"
