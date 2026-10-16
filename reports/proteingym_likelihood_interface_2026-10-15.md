# Teacher-forced likelihood interface: synthetic proof

The existing GPU5 Qwen/vLLM0.31.0 server supports one completion request per full variant: explicit token-ID prompt, `prompt_logprobs=0`, `echo=true`, `max_tokens=0`, `add_special_tokens=false`, `return_token_ids=true`, no legacy `logprobs` field. Both tiny nonbiological probes passed; no benchmark inputs or biological inference were used.

Use `encode(fixed_prefix)` followed by separately encoded **full** variant tokens. Sum every suffix token’s prompt log probability, excluding prefix terms. Returned IDs must exactly match supplied IDs. Prompt scores use float32 full-vocabulary log-softmax before gathering the actual token; zero top-N does not shrink the normalizer.

The first prompt token has no probability. An empty prefix therefore cannot score the first variant token; a nonempty fixed prefix scores all suffix tokens. EOS is absent unless explicitly appended. The synthetic EOS248046 proof succeeded, while the proposed P17 condition excludes EOS. The server internally generates one token for the zero-output echo path; ignore that token, all generated-token scores and completion-token usage when calculating likelihood. Reject missing/nonfinite terms and the source clipping sentinel−9999.0.

Raw no-prefix ASCII:11prompt tokens, first term correctly unavailable. Fixed-prefix Unicode:3prefix+7suffix+1explicitEOS; all7suffix terms finite, sum−45.397388339042664, EOS separately−11.619762420654297. Raw responses were1,292 and1,323bytes. These are interface fixtures, not benchmark results.

Preserve exact token IDs, suffix indices, original UTF8 and CPU tokenizer offsets. Unicode byte tokens can overlap character offsets; contextual decoding can flush multiple byte pieces or normalize decomposed Unicode. A trailing-space prefix demonstrably merges differently when jointly tokenized. Hard concatenation of separately encoded prefix/suffix IDs is an explicit adaptation; do not assume it equals encoding their concatenated text.

For about1,000 short sequence tokens, selected-only output is roughly0.11MB raw JSON. A conservative planning allowance is0.25MiB wire and1MiB per fully duplicated audit archive, including request IDs and raw/parsed response copies. This is an estimate, not a universal token-vocabulary bound. No long GPU probe was run.

| Evaluation interpretation | Likely demands | Information supplied | Reference | What a score establishes |
|---|---|---|---|---|
| Prospective Qwen causal likelihood adaptation | Sequence compatibility and representation quality; demand classification provisional | Fixed prefix plus full sequence only | Native assay outcomes retained solely for offline scoring | Full-coverage correlation for that declared adaptation; not equality to amino-acid PLM/ProtST masked-head likelihood, a mechanism, or proof against memorization |

All requests, responses, tokenizer offsets, server identity and installed source copies are under `sources/proteingym_likelihood_interface_2026-10-15/`; the JSON records hashes. No protocol approval or benchmark dispatch follows from this interface proof.
