# Description-guided protein generation: reviewed subset

This handoff defines a **59-case partial Qwen3.8-27B baseline** from the first 64 source-order cases of BioT5+'s public 5,876-case protein-design export. Five reviewed prefix cases and all 5,812 cases outside that prefix remain held. Every approved ID has an input-only review reason in `input_review.json`.

The exact source prompt template and per-instance instruction/description are retained. A frozen system instruction requests the native protein-token serialization. Original BF16 Qwen uses the fixed 4,096-token, medium-thinking, seed42, n=1 condition, with one concurrent request and no generation retries. A request with ambiguous prior dispatch is held rather than regenerated.

The primary metric is the qualified released-code paired-reference ROUGE-L condition. It preserves the source's target/input alternate-reference wiring. It uses full source prompts and targets, rather than reproducing BioT5+ tokenization or its 512/256 token truncation. This lexical score can reward common serialization or an input echo; it does not establish functional protein design. Paper normalized Smith–Waterman remains unavailable. Details are in [the preparation report](../../reports/P36_PREPARATION_2026-10-16.md).

`proposed_config.json` is the frozen condition; `proposed_authorization.json` is deliberately disabled. Actual dispatch requires a separate approval of that exact configuration hash, a loopback vLLM endpoint, and an absolute run directory. Publication does not authorize a new run.

Raw benchmark inputs, reference sequences, full source data, and model weights are excluded from this Git handoff. To reconstruct the exact local input/reference files from pinned public artifacts, run:

```bash
python3 restore_inputs.py
```

The restore script verifies publisher/source hashes and reconstructs the frozen 59-case files without changing their reviewed scope or configuration. It prints no sequences and performs no inference. The resulting local files are ignored by Git. The supplied source snapshots and hashes establish provenance; unknown publisher instance-license metadata remains recorded.

The runner needs Python's standard library. The offline scorer uses the exact versions in `requirements.lock.txt`; a separate CPU-only portable Python3.10 archive preserves those same versions. Given a node-local extracted runtime and an already authorized run:

```bash
/path/to/local-scorer-runtime/score_python.sh score_p36.py --run-dir /absolute/path/to/run
```

Scoring locks raw outputs/missing slots before opening references. Missing/failed slots are empty predictions in the full 59-slot denominator; malformed and length-stopped content is retained without repair. `scores.json` and `per_case_scores.json` contain no target sequences. The native wrapper's `native_metric_output.tsv` contains targets and belongs in the private data archive, outside Git.

Six synthetic tests cover source reference pairing, serialization artifacts, target exclusion, the dispatch authorization gate, failed-slot/raw-content handling, and output-lock mutation detection:

```bash
/path/to/local-scorer-runtime/score_python.sh -m unittest -v test_p36.py
```
