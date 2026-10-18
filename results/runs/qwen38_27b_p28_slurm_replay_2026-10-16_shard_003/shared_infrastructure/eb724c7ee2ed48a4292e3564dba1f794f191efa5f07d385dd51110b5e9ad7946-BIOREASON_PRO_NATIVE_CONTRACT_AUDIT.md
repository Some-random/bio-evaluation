P28 can support a declared contextual zero-shot Qwen adaptation. The native
BioReason-Pro model itself uses trained ESM3/protein projection and GO-graph
encoder/projection components; these may be important to prediction and are not
replicated by the existing Qwen checkpoint. This does not make the task invalid
or establish anything about either system's internal reasoning.

The exact released test parquet is pinned to HuggingFace revision
`a18315a77d27dd4fe5a28b9b757695cff4ba4e3f`, publisher LFS SHA256
`f8acd81f3b08400783a34f4189428e4f41fa0c648bc8e4fa58b10ee58bb66828`.
It contains8,630 unique proteins. The pinned native `data/common_proteins.txt`
lists471 IDs, all present in the release, leaving **8,159 eligible cases**.
All released rows are prepared, while only the original eligible source-order
IDs are provided for execution. The excluded471 are never scheduled. Every
prepared input and reference was reconciled against the publisher parquet.

The input contract comes from author commit
`a93ac2a96387103c100c4d6a6674d6fe1dfaf9e8`, verified against Git blob hashes.
The original formatter permits organism, InterPro domain context,
STRING interaction context and GO-GPT predictions. These are preserved exactly,
including the predictor-derived GO context; it is not mistaken for a forbidden
gold annotation. No protein name, gold function/subcellular description, target
GO annotation, teacher reasoning or teacher answer reaches prompt construction.
The source input-only columns are explicitly selected before reference columns
are opened. All complete raw sequences are retained:8–10,986 amino acids.

The source `format.py` combines its system and user text inside one user turn,
preceded by protein and GO-graph embedding placeholders. This adaptation replaces
the protein representation with the full raw sequence and keeps the original
combined instruction/context text; it does not supply the trained GO-graph
embedding. The current `eval.py` path passes no structure coordinates to the
processor/model even though structures were used during model training. No
measured coordinate input is silently dropped from that audited evaluation path.
See the pinned [formatter](https://github.com/bowang-lab/BioReason-Pro/blob/a93ac2a96387103c100c4d6a6674d6fe1dfaf9e8/bioreason2/dataset/cafa5/format.py),
[prompt builder](https://github.com/bowang-lab/BioReason-Pro/blob/a93ac2a96387103c100c4d6a6674d6fe1dfaf9e8/bioreason2/dataset/cafa5/load.py#L198)
and [actual evaluation path](https://github.com/bowang-lab/BioReason-Pro/blob/a93ac2a96387103c100c4d6a6674d6fe1dfaf9e8/eval.py#L245).

All8,630 source rows contain an organism and `go_pred`;7,198 have InterPro text
and1,228 have STRING text. Every row follows the native context-template branch.
The fixed source flags ask for all three GO aspects and always request a
UniProt-style summary. The authors explicitly added these flags to avoid
conditioning the prompt on gold-aspect or gold-summary presence. Their comments
say published prompts used those presence hints. The adaptation therefore keeps
the current label-independent native option and declares this paper-protocol
difference; it does not recreate the gold-dependent selectors. This is not an
extra context ablation or a test-outcome-selected variant.

The [v1 paper, Methods4.1.3](https://www.biorxiv.org/content/10.64898/2026.03.19.712954v1.full)
describes training annotations before November2022 and target annotations newly
acquired March2023–February2024, with no prior experimental target-aspect
annotation. Its released aspect counts match the parquet exactly:
BP5,819/169,459 annotations, MF2,080/19,773, CC3,440/41,592. After the native471
exclusions, the corresponding eligible counts are BP5,623, MF1,878 and CC3,293.
Final parquet rows have no annotation timestamps, so the temporal boundary is
verified as the published contract plus the immutable released IDs, rather than
an independent regeneration. Newer notebooks for a214→226/2025 extended holdout
are separate source artifacts and are not substituted. P29's species holdout
remains distinct. The requested v2 paper was not directly accessible here.

Native outcome scoring uses the repository's exact GO ontology release
**2023-01-01**, with43,248 active terms and3,491 alternate IDs. Ontology SHA256 is
`0c0062efbb1b199a6a54e62c0c48ff0038d39173aecc7edfab66a20090d5ec2d`.
The original IA file has43,248 entries,30,267 finite positive weights, SHA256
`9612326576384847c02ab08a5e9ea0558766a6ce3ec076a1664f975344cf498f`.
No weights are recomputed from held-out annotations. Every source reference GO
term is recognized by the pinned ontology or its alternate-ID mapping.

The native dependency was declared simply `cafaeval`, without a historical
version lock. This proposal prospectively pins the original PyPI
**cafaeval1.3.0** source distribution, SHA256
`abaaa1b225acfba8a188ac29c2b450f2b4b798631d20eeda018a1cd1eda9332b`.
Its code is vendored unchanged and byte-verified against that archive; no package
download occurs at scoring time. CPU scoring uses numpy1.21.5/pandas1.5.3.
Pandas/dateutil/six were added locally without changing the existing NumPy or any
model environment. Exact historical-package equality is not claimed.

The scorer calls the original CAFA ontology parser, gold/prediction propagation
and matrix metric functions: `is_a` and `part_of`, max-score ancestor propagation,
roots included, native CAFA protein-centric normalization and positive finite IA
weights. It assigns hard confidence1 to each extracted GO ID, matching the
released wrapper. Threshold0.99 is sufficient for the native Fmax sweep because
every nonzero prediction has the same score. Primary results are separate
BP/MF/CC Fmax and IA-weighted Fmax fractions; no unlike metrics are averaged.
The source parser's ontology/aspect eligibility rules remain intact.

All8,159 eligible prediction slots are locked before gold references are read.
Missing, transport-failed, empty and no-GO responses remain empty prediction
sets. The top-level package drops namespaces with no predictions; this adapter
instead calls its unchanged underlying metric with a zero matrix for that
namespace, preserving every gold row and yielding the native zero precision/
recall outcome. It never fabricates a GO term or confidence to force coverage.
Synthetic tests establish equality with the pinned original evaluator when
predictions exist and verify the empty-aspect/missing-case behavior.

Prediction extraction receives **generated continuation only**. The existing
local API archives separate generated reasoning and final-content channels;
the scorer reconstructs those channels in order, rejects conflicting duplicate
reasoning fields, and applies the native GO-ID regex to the continuation. It
never concatenates the request, initial `go_pred`, teacher trace or source
annotation into the generated output. Final-content-only GO sets are unscored
diagnostics. The released shell wrapper uses `final_answer_only=False`; the
paper describes final-block extraction, so that discrepancy is explicit.
See the pinned [native scorer](https://github.com/bowang-lab/BioReason-Pro/blob/a93ac2a96387103c100c4d6a6674d6fe1dfaf9e8/evals/cafa_evals.py)
and [scoring invocation](https://github.com/bowang-lab/BioReason-Pro/blob/a93ac2a96387103c100c4d6a6674d6fe1dfaf9e8/evals/run_cafa_eval.sh).

One generation per case is fixed; the source's optional oracle best-of-k
selection is not used. Every eligible failure stays in native ground truth,
with completeness and truncation counts reported. Complete raw sequences replace
the native2,000-residue crop. The frozen Qwen4,096-token output budget differs
from original model/paper inference settings. The largest eligible prompt has
18,487 UTF8 bytes; even the conservative byte-level BPE bound plus1,024 control
tokens and4,096 output tokens is23,607, below the pinned262,144-token context.
No input truncation is necessary.

Correct GO predictions establish agreement with recorded annotations under this
specific system, not explanation correctness or mechanistic truth. Missing
annotations do not establish biological negatives; poor scores do not isolate
general reasoning. Learned protein representations may materially affect
performance. Public pretraining exposure and the histories of supplied predictor
context remain unknown. No new training, judge, provider call, biological model
request, task authorization or queue change was performed in this preparation.
