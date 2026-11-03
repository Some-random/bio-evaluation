# GO_cellular_component_0140: before and after transfer clarification

[All 1,328 cases](../README.md) · [Method](../METHOD.md) · [Summary](../SUMMARY.md) · [Exact reviewer user message](../inputs/GO_cellular_component_0140.txt)

**Task:** `GO_cellular_component`  
**Author key, unchanged:** **D** — cytoplasm

| Round | Reviewer | Key support | Transfer / lookup | Output usability (canonical status) |
|---|---|---|---|---|
| before | GPT-6 Luna | supported | lookup-dependent | usable output (valid_review) |
| before | Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | usable output (valid_review) |
| after | GPT-6 Luna | supported | reasoning-supported | usable output (valid_review) |
| after | Qwen3.8-Flash-Next-NVFP4 | no saved label | no saved label | output error (invalid_review) |

**Usable output means format-valid review, not reasoning-supported or biologically correct.** A usable output can classify the question as reasoning-supported, lookup-dependent or uncertain. An output error is a problem with the saved model response; it does not count a defective benchmark question or wrong key. Each saved review is retained in full below. Labels from output errors are displayed as saved and excluded from label statistics. The author key and reviewer evidence were visible to reviewers; this is a review of answerability and key support, not a benchmark-solving score.

## Complete original question

```text
[Protein Sequence]
MDFESKYCTSQVNGTITITTRKVLDENLKSLLDEGKGELFLSCIPRNHSCSPRWIVEVASELGEVYIMRYKIDFSGNSRGYAYLQYINVDLKESAMQYLPMRFRQLCMCLRVEPSTNNRELVLKNVESSLRPWQVYQEMLKIHPFTIVRVYEYQLDQFFYIFEYRNNDSAASAHQRVRNSIRKFGEHAHISWLTAENILSRASGSFCFQREVSQNRTRRVPPRQKGCFKF

[Multiple Choices]
A. vitelline envelope
B. ciliary basal body
C. cell surface
D. cytoplasm
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Gene Ontology (GO) Cellular Component Prediction, which is to predict the primary Cellular Component where a protein is located, according to the Gene Ontology (GO) framework. A protein's location within a cell (e.g., Nucleus, Mitochondria, Cytoplasm) is critical for its function and is often determined by specific targeting signals in its amino acid sequence. Based on the provided sequence, you must identify the most likely compartment where the protein resides.. The inputs provided by the user for this task include:

* Protein Sequence: The amino acid sequence of the protein.
* Multiple Choices: Candidate answers for the protein-related question.

Please think step-by-step about this problem:
1. Analyze the protein sequence carefully.
2. Consider the biological context and function.
3. Evaluate each multiple-choice option.
4. Provide your reasoning process.
5. Finally, give your answer.

Provide your response in the following format:
1. reasoning: [Your detailed reasoning here]
2. answer: Your final answer, which should be "A", "B", "C" or "D".
```

</details>

## Four saved visible reviews

## Before: GPT-6 Luna

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The exact sequence matches the Drosophila tumorous testis protein. Its UniProt subcellular-location annotation reports cytoplasm with experimental evidence (ECO:0000269), and its GO cytoplasm annotation is IDA:FlyBase. This supports choice D, while not establishing that cytoplasm is its only location.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence is a soluble-looking protein without an obvious signal peptide or transmembrane segment, which argues against cell-surface or vitelline-envelope localization. That does not reliably distinguish cytoplasm from a ciliary basal body, and the localization is not determined by those features alone.


**Missing item-specific fact**

> The protein-specific localization evidence identifying this Drosophila protein as cytoplasmic is absent from the sequence and choices.


**Reason**

> General sequence features make some options less plausible, but the key distinction among intracellular destinations depends on protein-specific annotation or experimental localization.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The supplied reviewer evidence supports cytoplasm; it also notes a nucleus annotation, but nucleus is not an offered choice. No evidence supplied supports another listed option.


### Important caveats

- The localization evidence is reviewer-only and was not available to the evaluated model.
- The GO and UniProt records match the sequence, but the author's exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is a soluble-looking protein without an obvious signal peptide or transmembrane segment, which argues against cell-surface or vitelline-envelope localization. That does not reliably distinguish cytoplasm from a ciliary basal body, and the localization is not determined by those features alone.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific localization evidence identifying this Drosophila protein as cytoplasmic is absent from the sequence and choices.",
    "reason": "General sequence features make some options less plausible, but the key distinction among intracellular destinations depends on protein-specific annotation or experimental localization."
  },
  "case_id": "GO_cellular_component_0140",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the Drosophila tumorous testis protein. Its UniProt subcellular-location annotation reports cytoplasm with experimental evidence (ECO:0000269), and its GO cytoplasm annotation is IDA:FlyBase. This supports choice D, while not establishing that cytoplasm is its only location."
  },
  "important_caveats": [
    "The localization evidence is reviewer-only and was not available to the evaluated model.",
    "The GO and UniProt records match the sequence, but the author's exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied reviewer evidence supports cytoplasm; it also notes a nucleus annotation, but nucleus is not an offered choice. No evidence supplied supports another listed option."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0140",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the Drosophila tumorous testis protein. Its UniProt subcellular-location annotation reports cytoplasm with experimental evidence (ECO:0000269), and its GO cytoplasm annotation is IDA:FlyBase. This supports choice D, while not establishing that cytoplasm is its only location.",
    "evidence_ids": ["C5", "C6", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence is a soluble-looking protein without an obvious signal peptide or transmembrane segment, which argues against cell-surface or vitelline-envelope localization. That does not reliably distinguish cytoplasm from a ciliary basal body, and the localization is not determined by those features alone.",
    "missing_item_specific_fact": "The protein-specific localization evidence identifying this Drosophila protein as cytoplasmic is absent from the sequence and choices.",
    "reason": "General sequence features make some options less plausible, but the key distinction among intracellular destinations depends on protein-specific annotation or experimental localization."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied reviewer evidence supports cytoplasm; it also notes a nucleus annotation, but nucleus is not an offered choice. No evidence supplied supports another listed option."
  },
  "important_caveats": [
    "The localization evidence is reviewer-only and was not available to the evaluated model.",
    "The GO and UniProt records match the sequence, but the author's exact source snapshot is unknown."
  ]
}
```

</details>

## Before: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry Q8IQA2 (TUT_DROME) carries a SUBCELLULAR LOCATION comment of 'Cytoplasm' with evidence code ECO:0000269 (direct assay, PubMed:25412508), and a GO:0005737 (cytoplasm) annotation with evidence type IDA (Inferred from Direct Assay, FlyBase). This is experimental immunolocalization evidence from Chen et al. 2014 (PLoS Genet), not merely computational inference. The protein is an RRM-containing RNA-binding protein (tumorous testis) that forms a complex with BAM and BGCN in germline stem cell differentiation, a role consistent with cytoplasmic mRNA regulation. Sequence match is confirmed (SHA256 identical across benchmark, current, and historical entry v156).

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H4](#evidence-h4), [C9](#evidence-c9), [H2](#evidence-h2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 230-residue sequence lacks an N-terminal signal peptide (no hydrophobic 15-30 residue stretch at the N-terminus), ruling out secretion and thus the extracellular vitelline envelope (A) and cell surface (C). It lacks a transmembrane domain or GPI-anchor signal, further excluding C. It shows no tubulin-like repeats, no centriole/basal-body structural motifs, and no microtubule-organizing-center signatures, making ciliary basal body (B) implausible. The sequence contains a region consistent with an RRM (RNA Recognition Motif) fold, characteristic of cytoplasmic RNA-binding proteins. A small protein with no targeting signals and an RRM domain defaults to the cytoplasm by elimination and by functional class.


**Missing item-specific fact**

> None strictly required. Positive confirmation of the RRM domain and the specific TUT/BAM/BGCN complex role would benefit from database lookup, but the elimination of A, B, and C via absence of required targeting signals is achievable from the sequence and general biology.


**Reason**

> The three distractors each require specific structural features (signal peptide for A and C; centriole/basal-body architecture for B) that are demonstrably absent from the sequence. The remaining option, cytoplasm, is the default compartment for a small soluble protein lacking organelle-targeting signals, and the RRM-like fold is consistent with cytoplasmic RNA regulation. This constitutes a concrete, sequence-grounded biological argument.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The question asks for the primary cellular component. Among the four options, only cytoplasm is compatible with a small intracellular protein lacking signal peptides, transmembrane domains, or centriole structural motifs. The GO nucleus and ribonucleoprotein-complex annotations (both IBA, inferred by similarity) are not among the choices and do not conflict with the primary cytoplasmic assignment supported by direct assay.


### Important caveats

- The UniProt entry also carries GO:0005634 (nucleus, IBA:GO_Central) and GO:1990904 (ribonucleoprotein complex, IBA:GO_Central), but these are similarity-based inferences, not direct experimental assignments, and are not among the answer options.
- The RRM domain identification from the raw sequence is inferential; a model without domain-prediction tools may struggle to positively identify it, though the elimination approach does not depend on this.
- The identity of the protein (Q8IQA2, TUT_DROME) was inferred by the reviewer from dataset metadata absent from the model input; the model sees only the sequence and options.
- The GO ontology snapshot used by the benchmark authors is unknown; the current ontology was used for reviewer verification.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 230-residue sequence lacks an N-terminal signal peptide (no hydrophobic 15-30 residue stretch at the N-terminus), ruling out secretion and thus the extracellular vitelline envelope (A) and cell surface (C). It lacks a transmembrane domain or GPI-anchor signal, further excluding C. It shows no tubulin-like repeats, no centriole/basal-body structural motifs, and no microtubule-organizing-center signatures, making ciliary basal body (B) implausible. The sequence contains a region consistent with an RRM (RNA Recognition Motif) fold, characteristic of cytoplasmic RNA-binding proteins. A small protein with no targeting signals and an RRM domain defaults to the cytoplasm by elimination and by functional class.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None strictly required. Positive confirmation of the RRM domain and the specific TUT/BAM/BGCN complex role would benefit from database lookup, but the elimination of A, B, and C via absence of required targeting signals is achievable from the sequence and general biology.",
    "reason": "The three distractors each require specific structural features (signal peptide for A and C; centriole/basal-body architecture for B) that are demonstrably absent from the sequence. The remaining option, cytoplasm, is the default compartment for a small soluble protein lacking organelle-targeting signals, and the RRM-like fold is consistent with cytoplasmic RNA regulation. This constitutes a concrete, sequence-grounded biological argument."
  },
  "case_id": "GO_cellular_component_0140",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H3",
      "H4",
      "C9",
      "H2"
    ],
    "judgment": "supported",
    "reason": "UniProt entry Q8IQA2 (TUT_DROME) carries a SUBCELLULAR LOCATION comment of 'Cytoplasm' with evidence code ECO:0000269 (direct assay, PubMed:25412508), and a GO:0005737 (cytoplasm) annotation with evidence type IDA (Inferred from Direct Assay, FlyBase). This is experimental immunolocalization evidence from Chen et al. 2014 (PLoS Genet), not merely computational inference. The protein is an RRM-containing RNA-binding protein (tumorous testis) that forms a complex with BAM and BGCN in germline stem cell differentiation, a role consistent with cytoplasmic mRNA regulation. Sequence match is confirmed (SHA256 identical across benchmark, current, and historical entry v156)."
  },
  "important_caveats": [
    "The UniProt entry also carries GO:0005634 (nucleus, IBA:GO_Central) and GO:1990904 (ribonucleoprotein complex, IBA:GO_Central), but these are similarity-based inferences, not direct experimental assignments, and are not among the answer options.",
    "The RRM domain identification from the raw sequence is inferential; a model without domain-prediction tools may struggle to positively identify it, though the elimination approach does not depend on this.",
    "The identity of the protein (Q8IQA2, TUT_DROME) was inferred by the reviewer from dataset metadata absent from the model input; the model sees only the sequence and options.",
    "The GO ontology snapshot used by the benchmark authors is unknown; the current ontology was used for reviewer verification."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The question asks for the primary cellular component. Among the four options, only cytoplasm is compatible with a small intracellular protein lacking signal peptides, transmembrane domains, or centriole structural motifs. The GO nucleus and ribonucleoprotein-complex annotations (both IBA, inferred by similarity) are not among the choices and do not conflict with the primary cytoplasmic assignment supported by direct assay."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0140",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry Q8IQA2 (TUT_DROME) carries a SUBCELLULAR LOCATION comment of 'Cytoplasm' with evidence code ECO:0000269 (direct assay, PubMed:25412508), and a GO:0005737 (cytoplasm) annotation with evidence type IDA (Inferred from Direct Assay, FlyBase). This is experimental immunolocalization evidence from Chen et al. 2014 (PLoS Genet), not merely computational inference. The protein is an RRM-containing RNA-binding protein (tumorous testis) that forms a complex with BAM and BGCN in germline stem cell differentiation, a role consistent with cytoplasmic mRNA regulation. Sequence match is confirmed (SHA256 identical across benchmark, current, and historical entry v156).",
    "evidence_ids": ["C5", "C6", "H3", "H4", "C9", "H2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 230-residue sequence lacks an N-terminal signal peptide (no hydrophobic 15-30 residue stretch at the N-terminus), ruling out secretion and thus the extracellular vitelline envelope (A) and cell surface (C). It lacks a transmembrane domain or GPI-anchor signal, further excluding C. It shows no tubulin-like repeats, no centriole/basal-body structural motifs, and no microtubule-organizing-center signatures, making ciliary basal body (B) implausible. The sequence contains a region consistent with an RRM (RNA Recognition Motif) fold, characteristic of cytoplasmic RNA-binding proteins. A small protein with no targeting signals and an RRM domain defaults to the cytoplasm by elimination and by functional class.",
    "missing_item_specific_fact": "None strictly required. Positive confirmation of the RRM domain and the specific TUT/BAM/BGCN complex role would benefit from database lookup, but the elimination of A, B, and C via absence of required targeting signals is achievable from the sequence and general biology.",
    "reason": "The three distractors each require specific structural features (signal peptide for A and C; centriole/basal-body architecture for B) that are demonstrably absent from the sequence. The remaining option, cytoplasm, is the default compartment for a small soluble protein lacking organelle-targeting signals, and the RRM-like fold is consistent with cytoplasmic RNA regulation. This constitutes a concrete, sequence-grounded biological argument."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The question asks for the primary cellular component. Among the four options, only cytoplasm is compatible with a small intracellular protein lacking signal peptides, transmembrane domains, or centriole structural motifs. The GO nucleus and ribonucleoprotein-complex annotations (both IBA, inferred by similarity) are not among the choices and do not conflict with the primary cytoplasmic assignment supported by direct assay."
  },
  "important_caveats": [
    "The UniProt entry also carries GO:0005634 (nucleus, IBA:GO_Central) and GO:1990904 (ribonucleoprotein complex, IBA:GO_Central), but these are similarity-based inferences, not direct experimental assignments, and are not among the answer options.",
    "The RRM domain identification from the raw sequence is inferential; a model without domain-prediction tools may struggle to positively identify it, though the elimination approach does not depend on this.",
    "The identity of the protein (Q8IQA2, TUT_DROME) was inferred by the reviewer from dataset metadata absent from the model input; the model sees only the sequence and options.",
    "The GO ontology snapshot used by the benchmark authors is unknown; the current ontology was used for reviewer verification."
  ]
}
```

</details>

## After: GPT-6 Luna

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence matches the annotated protein, and both the current and archived records report cytoplasm; the GO annotation is experimentally supported (IDA), and the subcellular-location annotation cites experimental evidence. The record also has a nucleus annotation by IBA, but that does not contradict cytoplasmic localization.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H4](#evidence-h4), [C7](#evidence-c7), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is a soluble-looking globular protein with no apparent signal peptide or transmembrane segment, making an extracellular vitelline-envelope or cell-surface location unlikely. Its RNA-binding-protein-like features are consistent with an intracellular protein; among the offered choices, cytoplasm is the credible option, whereas a ciliary basal body would require more specific localization evidence.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Transferable sequence and protein-class knowledge meaningfully favors the intracellular cytoplasm choice over the offered extracellular, surface, and basal-body alternatives. This is a probabilistic inference, not proof of cytoplasmic rather than nuclear localization; nucleus is not an offered choice.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The evidence supports cytoplasm, and the offered alternatives do not provide a comparably plausible location. Possible nuclear localization does not create a second defensible offered option.


### Important caveats

- The sequence alone does not establish the experimentally observed localization or whether cytoplasm is the protein's primary location.
- The source record also includes a nucleus annotation, transferred by IBA; localization need not be exclusive.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is a soluble-looking globular protein with no apparent signal peptide or transmembrane segment, making an extracellular vitelline-envelope or cell-surface location unlikely. Its RNA-binding-protein-like features are consistent with an intracellular protein; among the offered choices, cytoplasm is the credible option, whereas a ciliary basal body would require more specific localization evidence.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Transferable sequence and protein-class knowledge meaningfully favors the intracellular cytoplasm choice over the offered extracellular, surface, and basal-body alternatives. This is a probabilistic inference, not proof of cytoplasmic rather than nuclear localization; nucleus is not an offered choice."
  },
  "case_id": "GO_cellular_component_0140",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H3",
      "H4",
      "C7",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The sequence matches the annotated protein, and both the current and archived records report cytoplasm; the GO annotation is experimentally supported (IDA), and the subcellular-location annotation cites experimental evidence. The record also has a nucleus annotation by IBA, but that does not contradict cytoplasmic localization."
  },
  "important_caveats": [
    "The sequence alone does not establish the experimentally observed localization or whether cytoplasm is the protein's primary location.",
    "The source record also includes a nucleus annotation, transferred by IBA; localization need not be exclusive."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The evidence supports cytoplasm, and the offered alternatives do not provide a comparably plausible location. Possible nuclear localization does not create a second defensible offered option."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0140",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches the annotated protein, and both the current and archived records report cytoplasm; the GO annotation is experimentally supported (IDA), and the subcellular-location annotation cites experimental evidence. The record also has a nucleus annotation by IBA, but that does not contradict cytoplasmic localization.",
    "evidence_ids": ["C5", "C6", "H3", "H4", "C7", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is a soluble-looking globular protein with no apparent signal peptide or transmembrane segment, making an extracellular vitelline-envelope or cell-surface location unlikely. Its RNA-binding-protein-like features are consistent with an intracellular protein; among the offered choices, cytoplasm is the credible option, whereas a ciliary basal body would require more specific localization evidence.",
    "missing_item_specific_fact": "",
    "reason": "Transferable sequence and protein-class knowledge meaningfully favors the intracellular cytoplasm choice over the offered extracellular, surface, and basal-body alternatives. This is a probabilistic inference, not proof of cytoplasmic rather than nuclear localization; nucleus is not an offered choice."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The evidence supports cytoplasm, and the offered alternatives do not provide a comparably plausible location. Possible nuclear localization does not create a second defensible offered option."
  },
  "important_caveats": [
    "The sequence alone does not establish the experimentally observed localization or whether cytoplasm is the protein's primary location.",
    "The source record also includes a nucleus annotation, transferred by IBA; localization need not be exclusive."
  ]
}
```

</details>

## After: Qwen3.8-Flash-Next-NVFP4

**Output usability:** output error.
**Canonical saved status:** `invalid_review`.

**This saved response has an output error and is not a usable structured review.** Any labels below remain the original saved values; they are excluded from label distributions and agreement. This output status does not judge the benchmark question, author key or biological correctness. No field or option ID has been repaired.

No visible final review text was saved. Internal model reasoning is not a substitute for a visible review and is not published. The final-content extraction failed because the saved final content was not text.

**Saved parsed visible review:** `null`.

**Exact saved visible final text:** empty string (`""`). No visible final is synthesized from private reasoning.

## Existing project source checks of the old Luna review only

These unchanged notes concern the earlier Luna claims. They do not validate either new review or the old Qwen review. No new scientific adjudication was performed.

## Project source-check notes

These project-authored, AI-assisted checks assess specific source claims. They are not expert adjudication and do not replace Luna’s saved review or the author key.

No additional case-specific project note was recorded. Citation membership checks do not establish that every scientific argument is correct.

## Complete reviewer-only evidence and qualifications

All excerpts supplied in the original and revised reviewer user message follow. This material was not available to the original evaluated model. Accession identity came from dataset image-path metadata. Source support and transferable discrimination are separate judgments.

**Applicability metadata, unchanged:**

```json
{
  "requested_accession": "Q8IQA2",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "benchmark_sequence_sha256": "037561273abf1ce94daf38d05ffaf93e8d9d4649e8d111cc07a5e50b33c8c022",
  "benchmark_sequence_length": 230,
  "current_status": "retrieved",
  "current_sequence_comparison": "matched",
  "current_entry_audit": {
    "entryVersion": 158,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2003-03-01",
    "sequenceVersion": 1
  },
  "current_uniprot_release": "2026_03",
  "current_record_sha256": "0602f9a5538349898a0569f81e032214b6d397ab9c4082ab5b5a31acc3ff8299",
  "current_source_sequence_sha256": "037561273abf1ce94daf38d05ffaf93e8d9d4649e8d111cc07a5e50b33c8c022",
  "current_source_sequence_length": 230,
  "historical_status": "retrieved",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "selected_historical_entry_version": 156,
  "selected_historical_version": {
    "accession": "Q8IQA2",
    "database": "Swiss-Prot",
    "entryVersion": 156,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "TUT_DROME",
    "sequenceVersion": 1
  },
  "selected_historical_record_sha256": "ee4b024dec0b13e4b3cd47072ce6c30cc94a8ba78c2a035c58f840273f55dfa6",
  "selected_historical_source_sequence_sha256": "037561273abf1ce94daf38d05ffaf93e8d9d4649e8d111cc07a5e50b33c8c022",
  "selected_historical_source_sequence_length": 230,
  "latest_at_cutoff_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 156,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "actual_author_source_snapshot": "unknown",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed."
}
```

**Qualifications, unchanged:**

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IQA2.json)

```json
{
  "evidence_id": "C1",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q8IQA2.json",
  "source_sha256": "0602f9a5538349898a0569f81e032214b6d397ab9c4082ab5b5a31acc3ff8299",
  "retrieved_utc": "2026-11-02T04:32:19.021600+00:00",
  "json_pointer": "/primaryAccession",
  "excerpt": "\"Q8IQA2\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IQA2.json)

```json
{
  "evidence_id": "C2",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q8IQA2.json",
  "source_sha256": "0602f9a5538349898a0569f81e032214b6d397ab9c4082ab5b5a31acc3ff8299",
  "retrieved_utc": "2026-11-02T04:32:19.021600+00:00",
  "json_pointer": "/entryAudit",
  "excerpt": "{\"entryVersion\":158,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2003-03-01\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IQA2.json)

```json
{
  "evidence_id": "C3",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q8IQA2.json",
  "source_sha256": "0602f9a5538349898a0569f81e032214b6d397ab9c4082ab5b5a31acc3ff8299",
  "retrieved_utc": "2026-11-02T04:32:19.021600+00:00",
  "json_pointer": "/organism",
  "excerpt": "{\"commonName\":\"Fruit fly\",\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP000000803\",\"source\":\"Proteomes\"}],\"lineage\":[\"Eukaryota\",\"Metazoa\",\"Ecdysozoa\",\"Arthropoda\",\"Altocrustacea\",\"Allotriocarida\",\"Hexapoda\",\"Insecta\",\"Pterygota\",\"Neoptera\",\"Eumetabola\",\"Endopterygota\",\"Aparaglossata\",\"Panorpida\",\"Diptera\",\"Brachycera\",\"Muscomorpha\",\"Ephydroidea\",\"Drosophilidae\",\"Drosophila\",\"Sophophora\"],\"scientificName\":\"Drosophila melanogaster\",\"taxonId\":7227}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IQA2.json)

```json
{
  "evidence_id": "C4",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q8IQA2.json",
  "source_sha256": "0602f9a5538349898a0569f81e032214b6d397ab9c4082ab5b5a31acc3ff8299",
  "retrieved_utc": "2026-11-02T04:32:19.021600+00:00",
  "json_pointer": "/proteinDescription",
  "excerpt": "{\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"25412508\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000312\",\"id\":\"FBgn0052364\",\"source\":\"FlyBase\"}],\"value\":\"Protein tumorous testis\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IQA2.json)

```json
{
  "evidence_id": "C5",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q8IQA2.json",
  "source_sha256": "0602f9a5538349898a0569f81e032214b6d397ab9c4082ab5b5a31acc3ff8299",
  "retrieved_utc": "2026-11-02T04:32:19.021600+00:00",
  "json_pointer": "/comments/2",
  "excerpt": "{\"commentType\":\"SUBCELLULAR LOCATION\",\"subcellularLocations\":[{\"location\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"25412508\",\"source\":\"PubMed\"}],\"id\":\"SL-0086\",\"value\":\"Cytoplasm\"}}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IQA2.json)

```json
{
  "evidence_id": "C6",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q8IQA2.json",
  "source_sha256": "0602f9a5538349898a0569f81e032214b6d397ab9c4082ab5b5a31acc3ff8299",
  "retrieved_utc": "2026-11-02T04:32:19.021600+00:00",
  "json_pointer": "/uniProtKBCrossReferences/26",
  "excerpt": "{\"database\":\"GO\",\"evidences\":[{\"evidenceCode\":\"ECO:0000314\",\"id\":\"25412508\",\"source\":\"PubMed\"}],\"id\":\"GO:0005737\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"C:cytoplasm\"},{\"key\":\"GoEvidenceType\",\"value\":\"IDA:FlyBase\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IQA2.json)

```json
{
  "evidence_id": "C7",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q8IQA2.json",
  "source_sha256": "0602f9a5538349898a0569f81e032214b6d397ab9c4082ab5b5a31acc3ff8299",
  "retrieved_utc": "2026-11-02T04:32:19.021600+00:00",
  "json_pointer": "/uniProtKBCrossReferences/27",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0005634\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"C:nucleus\"},{\"key\":\"GoEvidenceType\",\"value\":\"IBA:GO_Central\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IQA2.json)

```json
{
  "evidence_id": "C8",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q8IQA2.json",
  "source_sha256": "0602f9a5538349898a0569f81e032214b6d397ab9c4082ab5b5a31acc3ff8299",
  "retrieved_utc": "2026-11-02T04:32:19.021600+00:00",
  "json_pointer": "/uniProtKBCrossReferences/28",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:1990904\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"C:ribonucleoprotein complex\"},{\"key\":\"GoEvidenceType\",\"value\":\"IBA:GO_Central\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IQA2.json)

```json
{
  "evidence_id": "C9",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q8IQA2.json",
  "source_sha256": "0602f9a5538349898a0569f81e032214b6d397ab9c4082ab5b5a31acc3ff8299",
  "retrieved_utc": "2026-11-02T04:32:19.021600+00:00",
  "json_pointer": "/references/2",
  "excerpt": "{\"citation\":{\"authors\":[\"Chen D.\",\"Wu C.\",\"Zhao S.\",\"Geng Q.\",\"Gao Y.\",\"Li X.\",\"Zhang Y.\",\"Wang Z.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"25412508\"},{\"database\":\"DOI\",\"id\":\"10.1371/journal.pgen.1004797\"}],\"citationType\":\"journal article\",\"firstPage\":\"e1004797\",\"id\":\"25412508\",\"journal\":\"PLoS Genet.\",\"lastPage\":\"e1004797\",\"publicationDate\":\"2014\",\"title\":\"Three RNA binding proteins form a complex to promote differentiation of germline stem cell lineage in Drosophila.\",\"volume\":\"10\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":3,\"referencePositions\":[\"FUNCTION\",\"INTERACTION WITH BAM AND BGCN\",\"SUBCELLULAR LOCATION\",\"RRM DOMAIN\",\"DISRUPTION PHENOTYPE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IQA2?format=txt&versions=156)

```json
{
  "evidence_id": "H1",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q8IQA2?format=txt&versions=156",
  "source_sha256": "ee4b024dec0b13e4b3cd47072ce6c30cc94a8ba78c2a035c58f840273f55dfa6",
  "retrieved_utc": "2026-11-02T04:32:22.135035+00:00",
  "source_locator": "lines 1-14",
  "excerpt": "ID   TUT_DROME               Reviewed;         230 AA.\nAC   Q8IQA2;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   01-MAR-2003, sequence version 1.\nDT   28-JAN-2026, entry version 156.\nDE   RecName: Full=Protein tumorous testis {ECO:0000303|PubMed:25412508, ECO:0000312|FlyBase:FBgn0052364};\nGN   Name=tut {ECO:0000303|PubMed:25412508, ECO:0000312|FlyBase:FBgn0052364};\nGN   Synonyms=anon-WO0118547.705 {ECO:0000312|EMBL:AAN12017.1};\nGN   ORFNames=CG32364 {ECO:0000312|FlyBase:FBgn0052364};\nOS   Drosophila melanogaster (Fruit fly).\nOC   Eukaryota; Metazoa; Ecdysozoa; Arthropoda; Hexapoda; Insecta; Pterygota;\nOC   Neoptera; Endopterygota; Diptera; Brachycera; Muscomorpha; Ephydroidea;\nOC   Drosophilidae; Drosophila; Sophophora.\nOX   NCBI_TaxID=7227 {ECO:0000312|Proteomes:UP000000803};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 156,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IQA2?format=txt&versions=156)

```json
{
  "evidence_id": "H2",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q8IQA2?format=txt&versions=156",
  "source_sha256": "ee4b024dec0b13e4b3cd47072ce6c30cc94a8ba78c2a035c58f840273f55dfa6",
  "retrieved_utc": "2026-11-02T04:32:22.135035+00:00",
  "source_locator": "lines 68-75",
  "excerpt": "RN   [3] {ECO:0000305}\nRP   FUNCTION, INTERACTION WITH BAM AND BGCN, SUBCELLULAR LOCATION, RRM DOMAIN,\nRP   AND DISRUPTION PHENOTYPE.\nRX   PubMed=25412508; DOI=10.1371/journal.pgen.1004797;\nRA   Chen D., Wu C., Zhao S., Geng Q., Gao Y., Li X., Zhang Y., Wang Z.;\nRT   \"Three RNA binding proteins form a complex to promote differentiation of\nRT   germline stem cell lineage in Drosophila.\";\nRL   PLoS Genet. 10:e1004797-e1004797(2014).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 156,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IQA2?format=txt&versions=156)

```json
{
  "evidence_id": "H3",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q8IQA2?format=txt&versions=156",
  "source_sha256": "ee4b024dec0b13e4b3cd47072ce6c30cc94a8ba78c2a035c58f840273f55dfa6",
  "retrieved_utc": "2026-11-02T04:32:22.135035+00:00",
  "source_locator": "lines 111-111",
  "excerpt": "CC   -!- SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:25412508}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 156,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IQA2?format=txt&versions=156)

```json
{
  "evidence_id": "H4",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q8IQA2?format=txt&versions=156",
  "source_sha256": "ee4b024dec0b13e4b3cd47072ce6c30cc94a8ba78c2a035c58f840273f55dfa6",
  "retrieved_utc": "2026-11-02T04:32:22.135035+00:00",
  "source_locator": "lines 148-148",
  "excerpt": "DR   GO; GO:0005737; C:cytoplasm; IDA:FlyBase.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 156,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IQA2?format=txt&versions=156)

```json
{
  "evidence_id": "H5",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q8IQA2?format=txt&versions=156",
  "source_sha256": "ee4b024dec0b13e4b3cd47072ce6c30cc94a8ba78c2a035c58f840273f55dfa6",
  "retrieved_utc": "2026-11-02T04:32:22.135035+00:00",
  "source_locator": "lines 149-149",
  "excerpt": "DR   GO; GO:0005634; C:nucleus; IBA:GO_Central.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 156,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IQA2?format=txt&versions=156)

```json
{
  "evidence_id": "H6",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q8IQA2?format=txt&versions=156",
  "source_sha256": "ee4b024dec0b13e4b3cd47072ce6c30cc94a8ba78c2a035c58f840273f55dfa6",
  "retrieved_utc": "2026-11-02T04:32:22.135035+00:00",
  "source_locator": "lines 150-150",
  "excerpt": "DR   GO; GO:1990904; C:ribonucleoprotein complex; IBA:GO_Central.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 156,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
  "source": "Gene Ontology current ontology",
  "url": "https://current.geneontology.org/ontology/go-basic.obo",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source_locator": "lines 58957-58974",
  "excerpt": "[Term]\nid: GO:0005737\nname: cytoplasm\nnamespace: cellular_component\ndef: \"The contents of a cell excluding the plasma membrane and nucleus, but including other subcellular structures.\" [ISBN:0198547684]\nsubset: goslim_candida\nsubset: goslim_chembl\nsubset: goslim_metagenomics\nsubset: goslim_pir\nsubset: goslim_plant\nsubset: goslim_plant_ribbon\nsubset: goslim_prokaryote\nsubset: goslim_prokaryote_ribbon\nsubset: goslim_yeast\nxref: Wikipedia:Cytoplasm\nis_a: GO:0110165 ! cellular anatomical structure\nrelationship: part_of GO:0005622 ! intracellular anatomical structure\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "go_id": "GO:0005737"
}
```

### Evidence GO2

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO2",
  "source": "Gene Ontology current ontology",
  "url": "https://current.geneontology.org/ontology/go-basic.obo",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source_locator": "lines 101772-101784",
  "excerpt": "[Term]\nid: GO:0009986\nname: cell surface\nnamespace: cellular_component\nalt_id: GO:0009928\nalt_id: GO:0009929\ndef: \"The external part of the cell wall and/or plasma membrane.\" [GOC:jl, GOC:mtg_sensu, GOC:sm]\ncomment: Note that this term is intended to annotate gene products that are attached (integrated or loosely bound) to the plasma membrane or cell wall.\nsubset: goslim_pir\nsynonym: \"cell associated\" EXACT []\nsynonym: \"cell bound\" EXACT []\nis_a: GO:0110165 ! cellular anatomical structure\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "go_id": "GO:0009986"
}
```

### Evidence GO3

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO3",
  "source": "Gene Ontology current ontology",
  "url": "https://current.geneontology.org/ontology/go-basic.obo",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source_locator": "lines 224054-224069",
  "excerpt": "[Term]\nid: GO:0036064\nname: ciliary basal body\nnamespace: cellular_component\nalt_id: GO:0005932\ndef: \"A membrane-tethered, short cylindrical array of microtubules and associated proteins found at the base of a eukaryotic cilium (also called flagellum) that is similar in structure to a centriole and derives from it. The cilium basal body is the site of assembly and remodeling of the cilium and serves as a nucleation site for axoneme growth. As well as anchoring the cilium, it is thought to provide a selective gateway regulating the entry of ciliary proteins and vesicles by intraflagellar transport.\" [GOC:cilia, GOC:clt, PMID:21750193]\ncomment: In most eukaryotic cells, 'ciliary basal body' (GO:0036064) and 'centriole' (GO:0005814) represent a common entity that cycles through its function in cell division, then ciliogenesis, then cell division again. However, these structures are modified extensively as they transition into each other, and may contain different proteins, specific to each component.\nsynonym: \"basal body\" BROAD []\nsynonym: \"cilial basal body\" EXACT []\nsynonym: \"cilium basal body\" EXACT [GOC:bf]\nsynonym: \"kinetosome\" EXACT [PMID:11125699]\nsynonym: \"microtubule basal body\" EXACT []\nxref: NIF_Subcellular:sao11978067\nis_a: GO:0005815 ! microtubule organizing center\nrelationship: part_of GO:0005929 ! cilium\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "go_id": "GO:0036064"
}
```

### Evidence GO4

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO4",
  "source": "Gene Ontology current ontology",
  "url": "https://current.geneontology.org/ontology/go-basic.obo",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source_locator": "lines 347268-347275",
  "excerpt": "[Term]\nid: GO:0060388\nname: vitelline envelope\nnamespace: cellular_component\ndef: \"A glycoprotein-based structure that lies outside the plasma membrane and surrounds the egg before fertilization.\" [GOC:dph, ISBN:0878932437]\nsynonym: \"fertilization membrane\" RELATED []\nis_a: GO:0035805 ! egg coat\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "go_id": "GO:0060388"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 140. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
