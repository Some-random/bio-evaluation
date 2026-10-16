#!/usr/bin/env bash
set -euo pipefail
task_runtime_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
unset PYTHONHOME PYTHONPATH VIRTUAL_ENV
export PYTHONNOUSERSITE=1 PYTHONDONTWRITEBYTECODE=1
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 NUMEXPR_NUM_THREADS=1
exec "$task_runtime_dir/python/bin/python3.10" "$@"
