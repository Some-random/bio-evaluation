# N01–N03 public human-genomic input audit

Preparation is complete for 2,396 released evaluation rows. No inference,
training, model-response inspection, authorization change or inference-config
change occurred. Model messages contain complete released DNA windows and the
original question. Answers, disease annotations and KEGG teacher rationales are
kept in separate scorer-only files.

| Task | Exact prepared source | Rows | Native required information | Target and paper metrics |
| --- | --- | ---: | --- | --- |
| N01 | `wanglab/kegg`, revision `9f0ef941a362f0e308e11861ed82c36338e23586`; test then val | 146 + 144 = 290 | Paired reference/variant DNA; chromosome, complete pathway/network and gene context in the question | Disease; accuracy, macro-F1, macro-precision, macro-recall |
| N02 | `wanglab/variant_effect_coding`, revision `7684ab820d728fb5362328757079a1390a3f43bb`; test | 1,233 | Paired reference/variant DNA and original gene/chromosome question; all test questions identify chromosome 8 | Benign/pathogenic; accuracy and pathogenic-class F1 |
| N03 | `wanglab/variant_effect_non_snv`, revision `aeba75d031b8cb507b3962ab486aa22700afa31c`; test | 873 | Paired reference/altered DNA and original gene/chromosome/position question; retain non-SNV representation | Benign/pathogenic; accuracy and pathogenic-class F1 |

These input and prediction contracts come from the [BioReason paper, Sections
4–5](https://arxiv.org/html/2505.23579v2) and its [official dataset
collection](https://huggingface.co/collections/wanglab/bioreason). The declared
source domain is human clinical-variant interpretation, without an engineering
or pathogen-fitness objective. Source question scaffolds and context were
inspected independently of scorer labels. No rows were selected using labels or
model outcomes.

The prior N01 count blocker is resolved for the released evaluator:
[the pinned official evaluator, lines 40–43](https://github.com/bowang-lab/BioReason/blob/684ff7c09eb1d65e70925c114a7a05a1fcc0403f/eval_kegg_dna_vllm.py#L40)
concatenates test and val in that order. Both files are downloaded and match
publisher SHA-256 digests. This establishes the released 290-row evaluation
construction; archived author predictions and exact paper-run identity remain
unavailable. The val portion is treated as held-out evaluation material here,
not as development data for prompt selection.

The [official KEGG formatter](https://github.com/bowang-lab/BioReason/blob/684ff7c09eb1d65e70925c114a7a05a1fcc0403f/bioreason/dataset/kegg.py)
and [VEP formatter](https://github.com/bowang-lab/BioReason/blob/684ff7c09eb1d65e70925c114a7a05a1fcc0403f/bioreason/dataset/variant_effect.py)
define an LLM-only interface with DNA as text. Therefore a faithful LLM-input
baseline can receive raw sequences; learned DNA embeddings are required for the
separate DNA–LLM specialist architecture. Source baseline models were task
fine-tuned. A prompted local model has a different training regime.

N02 preserves all original `ID` strings. N01 and N03 have stable generated IDs
from task, source split and row index; their provenance retains any original
source index. N03's source `mutated_sequence` maps to the variant-sequence input
slot without reconstructing or changing indels. All released N02/N03 sequence
windows are 4,096 bases. N01's complete released windows range from 4,000 to
4,260 bases across the pair types. Source row order is preserved.

Full released windows are retained in the new preparation. The released
DNA/hybrid evaluator defaults to cropping 1,024 bases from each end of long
windows, and preprocessing order differs across LLM and DNA code paths. The
prepared variant `NATIVE_LLM_INTERFACE_FULL_RELEASE_WINDOWS_PREPARED` names the
source LLM interface and full-window preparation; it does not assert identical
paper preprocessing or completion of a specialist system.

Scoring still needs a frozen, explicit protocol before dispatch:

- N01's released multiclass evaluator reports substring accuracy after its
  final-answer marker. It does not implement the paper's multiclass macro
  metrics. The complete released disease vocabulary has 37 classes; 33 occur
  in the prepared 290-row references. Empty-class handling and final-label
  mapping must be fixed before outcomes.
- VEP's released test hook treats a ground-truth class appearing anywhere in
  generated text as correct. This can credit ambiguous outputs or rationale
  mentions. A strict final-label parser is a separately labeled scoring
  adaptation. The source normalization yields the fixed benign/pathogenic
  vocabulary, with pathogenic as the positive F1 class.
- The paper describes temperature-zero evaluation; released VEP generation
  code uses temperature 0.6. A future local run must preserve its own frozen
  decoder settings and disclose the difference.

The [pinned training/evaluation code](https://github.com/bowang-lab/BioReason/blob/684ff7c09eb1d65e70925c114a7a05a1fcc0403f/train_dna_qwen.py)
supports these implementation caveats. No scorer was silently substituted.
Correct class or disease predictions do not validate generated mechanisms;
KEGG teacher rationales are generated references rather than independently
established mechanistic truth. Explanation support remains unassessed, and
pretraining exposure is unknown.

Artifacts are under `data/catalog_genomic_tasks/{N01,N02,N03}/`:
`model_inputs.jsonl` contains one user message per case;
`input_provenance.jsonl` retains exact source fields and hashes;
`scorer_references.jsonl` holds hidden targets; `class_vocabulary.json` and
`preparation.json` freeze metadata. `sources/genomic_contract_audit_2026-10-15/`
retains pinned public sources and publisher-digest checks. The KEGG train file
was used solely to recover the global class namespace; no training examples
were supplied to a solver.

N04's adapted network holdout and N05's expression-conditioned measurements
remain separate unresolved contracts. N01–N03 do not replace either setting.
