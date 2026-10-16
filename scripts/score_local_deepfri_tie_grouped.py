#!/usr/bin/env python3
"""Isolated sklearn-only supplemental AP helper; accepts hashed non-pickle NPZ."""
import argparse
import hashlib
import io
import json
from pathlib import Path
import platform
import sys

import numpy
import sklearn
from sklearn.metrics import average_precision_score


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--describe-runtime", action="store_true")
    args = parser.parse_args()
    if args.describe_runtime:
        print(json.dumps({"python": platform.python_version(), "sklearn": sklearn.__version__, "numpy": numpy.__version__}))
    else:
        request = json.load(sys.stdin)
        raw = Path(request["matrix_path"]).read_bytes()
        if hashlib.sha256(raw).hexdigest() != request["sha256"]:
            raise ValueError("Supplemental matrix changed")
        with numpy.load(io.BytesIO(raw), allow_pickle=False) as arrays:
            scores, targets = arrays["scores"], arrays["targets"]
        if scores.shape != targets.shape or scores.ndim != 2 or not numpy.isfinite(scores).all() or not numpy.isin(targets, [0, 1]).all():
            raise ValueError("Supplemental score/target matrix invalid")
        print(json.dumps({"sklearn_micro_average_precision": float(average_precision_score(targets, scores, average="micro"))}))
