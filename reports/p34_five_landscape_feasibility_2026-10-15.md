# P34: five-landscape source-only feasibility review

A Qwen replacement-head baseline is scientifically possible; absence of a trained joint head is not grounds to drop this prediction task. It is not activation-ready or established as an exact paper replication. No forward pass, generation, sampler, training, base download, or existing frozen-file edit occurred.

Allowed scope: **AMIE, avGFP, E4B, LGK, UBE2I**. The sixth landscape stays held. Five-landscape results cannot stand in for the complete paper setting.

The [released head](https://github.com/PharMolix/MutaPLM/blob/495815b2069419d19d9449a59070d0fb24b596d1/model/modeling_esm.py#L1358-L1373) returns a per-position binary mutation probability at temperature0.5 times a33-class AA softmax at0.5. It masks BOS/EOS/padding positions before returning. It has neither a global position normalization nor a WT/AA20 filter.

The [released optimizer](https://github.com/PharMolix/MutaPLM/blob/495815b2069419d19d9449a59070d0fb24b596d1/evaluator.py#L190-L323) adds the previous selected weight to every next-grid cell, then samples20 flattened cells without replacement. This revives previously masked positions from round2. Native Python string editing uses token positions as character offsets; special strings and position0 can change length. These are source properties, not failures observed in this audit. Repairing them changes the condition.

The [paper Algorithm1](https://arxiv.org/html/2410.22949v1#A3.SS4) instead describes summed head scores and a global softmax. LGK goal wording also differs. The paper's SD wording does not match released population-variance outputs. Select and disclose one protocol target prospectively; neither a silent repair nor a claim that both are identical is valid.

A concrete source-shaped adapter would ask a fixed binary likelihood question at each native token position and obtain all33 conditional class likelihoods, apply the two temperature0.5 normalizations, then return the exact-shaped product grid. Preserve the original prior, flattening, RNG, sampling, string edits, batch size4 and trained oracle. A categorical position×residue factorization is another valid declared baseline, but changes native position-mass calibration. Keep all33 classes and no outcome-based retries or repairs. No prompt or protocol was frozen here.

For a complete run, each landscape uses20seeds×10rounds×20selected cells,3,620 proposal states,920 source proposal batches,1,020 oracle batches and4,020 oracle scalar values. Across five:18,100 states,4,600 proposal batches,5,100 oracle batches and20,100 scalar values. The oracle does not feed selection. These complete-run counts do not guarantee source code will finish after malformed edits.

| Landscape | Start residues | Full start/function/goal tokens¹ | Oracle tokens initially | 33-class complete-label prefix evaluations² | Prefix-free label-event evaluations² |
|---|---:|---:|---:|---:|---:|
| AMIE | 341 | 233 | 343 | 55,548,900 | 14,813,040 |
| avGFP | 237 | 216 | 239 | 38,607,300 | 10,295,280 |
| E4B | 102 | 193 | 104 | 16,615,800 | 4,430,880 |
| LGK | 439 | 354 | 441 | 71,513,100 | 19,070,160 |
| UBE2I | 159 | 278 | 161 | 25,901,100 | 6,906,960 |

¹ Pinned local Qwen tokenizer only; illustrative named fields, before chat/task/prefix overhead. Full current sequences cannot silently be cropped. Later native edits may greatly increase length.

² Conditional on every state retaining its starting length. Binary+33 complete-newline labels requires45 evaluations per actual unmasked position; the separately defined prefix-free class event requires12. Totals are208,186,200 or55,516,320 respectively. These equal HTTP calls only with one prefix per request; batching changes transport count. Actual counts depend on native candidate lengths. Neither interface has a full runtime proof. Decimal positions are multi-token; all33 support and prefix behavior were checked with tokenizer metadata only.

Use the exact original ESM1b encoder and five existing trained decoder heads, including the source1024-token cutoff, special tokens and batching. The five starts initially fit; future native edits may not. The2,609,617,413-byte encoder remains metadata-only. Learned weights must be restored and audited before any later forward. Unused raw valid.json rows are not scientifically required by the optimizer and must not be exposed to Qwen through generic loader logging.

| Evaluation | Likely demands (provisional) | Information supplied | Reference source | What scores establish |
|---|---|---|---|---|
| Five permitted P34 landscapes | Sequence/function conditioning, residue-effect priors, calibration and multistep search; learned representations may matter | Current full sequence, fixed function and objective; no assay data or oracle feedback | Fixed author-trained ESM1b proxy | High: stronger proxy-scored candidates under the frozen search budget. Low: weaker performance for this adapter/search. Neither validates a rationale, experimental improvement, memorization absence or an internal computation. |

Before activation: resolve paper/source target; freeze the full likelihood-head contract and failure handling; prove the extended fixed-ID/assistant-prefill interface with synthetic strings; verify source-tensor equivalence using nonbiological fixtures; audit the original oracle restoration and approve resource cost. Do not add candidate filters, deduplicate, substitute an encoder/head, or use post-outcome calibration.

The JSON records complete math, indexing, hashes, source-qualified starting-asset provenance, all per-landscape counts and explicit blockers. Existing results remain untouched.
