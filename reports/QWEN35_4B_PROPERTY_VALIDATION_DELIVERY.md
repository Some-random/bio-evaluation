# Qwen3.5 protein-property delivery validation

All 184 development outcomes were preserved.
These checks assess numeric output delivery on the existing validation panels. Biological correctness was not scored.

| Model | Validation task | Saved | Finite scalar | Truncated | Output range |
|---|---|---:|---:|---:|---|
| Qwen3.5-4B-Base | FLIP Meltome thermostability | 16/16 | 16 | 0 | 73 to 73 |
| Qwen3.5-4B-Base | TAPE stability | 12/12 | 12 | 0 | -3.2 to -3.2 |
| Qwen3.5-4B-Base | TAPE GFP fluorescence | 64/64 | 64 | 0 | 7.25 to 7.25 |
| Qwen3.5-4B | FLIP Meltome thermostability | 16/16 | 16 | 0 | 73 to 73 |
| Qwen3.5-4B | TAPE stability | 12/12 | 12 | 0 | -1.27 to -1.24 |
| Qwen3.5-4B | TAPE GFP fluorescence | 64/64 | 64 | 0 | -3.57 to -3.57 |

Both models use the same complete source prompts, nonthinking output mode, a fixed finite-number grammar and 256 output tokens. Numeric ranges describe model outputs only. Unclosed generation attempts remain unknown in a terminal partial record.

The earlier thinking16K Base condition stopped after 24 thermostability outputs: 13 numeric finals, 7 truncations and 4 nonnumeric finals. Its raw outputs are preserved separately; it produced no benchmark score.

[Raw trajectories, approved inputs and code](https://github.com/Some-random/bio-evaluation/blob/main/results/runs/qwen35_4b_pair_property_validation_delivery_nonthinking_regex256_20261022_v3/archive_index.json).
