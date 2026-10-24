# NatureLM-style unconditional generation

All 1,000 saved Qwen3.8-27B generations are retained. Mean length: 12383.76 residues; released-code diversity: 0.7960. OmegaFold2 completed 440/440 eligible folds; mean predictor confidence: 75.47/100.

The released evaluator folds outputs shorter than 100 residues: 440 are eligible and 560 are outside that gate. The generation denominator remains 1,000. A canonical tagged-output decoder imposed formatting without a residue-count cutoff; format validity is imposed rather than a model capability score. The original generation job failed after sealing and before folding; a separately admitted recovery used those same immutable outputs.

This is an available-code adaptation. NatureLM reports 50% identity clustering, whereas this released-code diversity uses 99% equal-length positional clustering. Predictor confidence is not experimental function or measured structure. No generation was repeated.
