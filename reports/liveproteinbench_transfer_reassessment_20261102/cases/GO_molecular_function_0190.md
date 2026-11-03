# GO_molecular_function_0190: before and after transfer clarification

[All 1,328 cases](../README.md) · [Method](../METHOD.md) · [Summary](../SUMMARY.md) · [Exact reviewer user message](../inputs/GO_molecular_function_0190.txt)

**Task:** `GO_molecular_function`  
**Author key, unchanged:** **D** — methylated histone binding

| Round | Reviewer | Key support | Transfer / lookup | Output usability (canonical status) |
|---|---|---|---|---|
| before | GPT-6 Luna | supported | lookup-dependent | usable output (valid_review) |
| before | Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | usable output (valid_review) |
| after | GPT-6 Luna | supported | reasoning-supported | usable output (valid_review) |
| after | Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | usable output (valid_review) |

**Usable output means format-valid review, not reasoning-supported or biologically correct.** A usable output can classify the question as reasoning-supported, lookup-dependent or uncertain. An output error is a problem with the saved model response; it does not count a defective benchmark question or wrong key. Each saved review is retained in full below. Labels from output errors are displayed as saved and excluded from label statistics. The author key and reviewer evidence were visible to reviewers; this is a review of answerability and key support, not a benchmark-solving score.

## Complete original question

```text
[Protein Sequence]
MPLTAESAAQQIQDRLKDIQQNIHNVDEERRRAENSIASLVRSLHATNQKVKPLLKASLTEAAQEEATIRAALAKIHEIRSIRNERRIQARNAGNKEAIRRGALMKMVQLSAQTLPLFVGKLGERAPALCGAIPAEGNYVAKVGDNVAALAKGIDEEENWILAEVVQFLHRQNKYDVIDIDEEQKDRHVLSKRKVIPLPLMRANPETDGHALFPKDTVVMALYPQTTCFYKAIVHRLPQTATEDYEVLFEDSSYTNGYAEPLPVAQRYVIAYRPTKKGAGSGSGNLSSA

[Multiple Choices]
A. calcium-dependent phospholipid binding
B. MAP kinase activity
C. threonine synthase activity
D. methylated histone binding
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Gene Ontology (GO) Molecular Function Prediction, which is to predict the fundamental activity of a protein at the molecular level, as defined by the Gene Ontology (GO) 'Molecular Function' branch. This describes the elemental tasks a protein performs, such as catalysis, transport, or binding to specific molecules. Based on the protein's amino acid sequence, you are to select the option that best describes its primary molecular function.. The inputs provided by the user for this task include:

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

> The sequence matches Drosophila Sgf29, and its GO annotations include histone H3K36me3 and H3K4me3 reader activity, which support the broader choice of methylated histone binding. These specific GO annotations are inferred by sequence similarity (ISS), not shown here as direct experimental measurements.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C6](#evidence-c6), [C7](#evidence-c7).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence provides no clear basis for identifying methylated histone recognition specifically over other binding functions. Eliminating the enzyme choices from sequence features would not distinguish choice D from choice A.


**Missing item-specific fact**

> The protein-specific fact that Sgf29 recognizes methylated histone H3 marks, such as H3K4me3 and H3K36me3.


**Reason**

> Distinguishing D depends on knowledge of this protein's histone-reader function, which is not established by the sequence and choices alone. The reviewer-only annotation supports the key but was not provided to the evaluated model.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the listed choices, methylated histone binding is supported for this protein; the other options describe distinct activities not supported by the supplied evidence.


### Important caveats

- The sequence-to-entry match is exact, but the accession and annotation were reviewer-only.
- The specific histone-reader GO annotations carry ISS evidence; the cited functional annotation about SAGA/CHAT complex membership does not itself establish direct histone binding.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence provides no clear basis for identifying methylated histone recognition specifically over other binding functions. Eliminating the enzyme choices from sequence features would not distinguish choice D from choice A.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific fact that Sgf29 recognizes methylated histone H3 marks, such as H3K4me3 and H3K36me3.",
    "reason": "Distinguishing D depends on knowledge of this protein's histone-reader function, which is not established by the sequence and choices alone. The reviewer-only annotation supports the key but was not provided to the evaluated model."
  },
  "case_id": "GO_molecular_function_0190",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C6",
      "C7"
    ],
    "judgment": "supported",
    "reason": "The sequence matches Drosophila Sgf29, and its GO annotations include histone H3K36me3 and H3K4me3 reader activity, which support the broader choice of methylated histone binding. These specific GO annotations are inferred by sequence similarity (ISS), not shown here as direct experimental measurements."
  },
  "important_caveats": [
    "The sequence-to-entry match is exact, but the accession and annotation were reviewer-only.",
    "The specific histone-reader GO annotations carry ISS evidence; the cited functional annotation about SAGA/CHAT complex membership does not itself establish direct histone binding."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed choices, methylated histone binding is supported for this protein; the other options describe distinct activities not supported by the supplied evidence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0190",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches Drosophila Sgf29, and its GO annotations include histone H3K36me3 and H3K4me3 reader activity, which support the broader choice of methylated histone binding. These specific GO annotations are inferred by sequence similarity (ISS), not shown here as direct experimental measurements.",
    "evidence_ids": ["C1", "C4", "C6", "C7"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence provides no clear basis for identifying methylated histone recognition specifically over other binding functions. Eliminating the enzyme choices from sequence features would not distinguish choice D from choice A.",
    "missing_item_specific_fact": "The protein-specific fact that Sgf29 recognizes methylated histone H3 marks, such as H3K4me3 and H3K36me3.",
    "reason": "Distinguishing D depends on knowledge of this protein's histone-reader function, which is not established by the sequence and choices alone. The reviewer-only annotation supports the key but was not provided to the evaluated model."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed choices, methylated histone binding is supported for this protein; the other options describe distinct activities not supported by the supplied evidence."
  },
  "important_caveats": [
    "The sequence-to-entry match is exact, but the accession and annotation were reviewer-only.",
    "The specific histone-reader GO annotations carry ISS evidence; the cited functional annotation about SAGA/CHAT complex membership does not itself establish direct histone binding."
  ]
}
```

</details>

## Before: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The protein is Drosophila Sgf29 (Q9W2I4), annotated with GO:0140002 'histone H3K4me3 reader activity' and GO:0140003 'histone H3K36me3 reader activity' (both ISS:FlyBase). These reader activities involve binding to methylated histone residues, making 'methylated histone binding' a valid generalization. The protein is also confirmed as a component of SAGA/CHAT histone acetyltransferase complexes. However, the evidence codes are ISS (inferred by sequence/similarity), not direct experimental binding assays for this specific protein, so the support is computational/annotation-based rather than experimentally demonstrated for this exact protein.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H7](#evidence-h7), [H8](#evidence-h8), [H9](#evidence-h9).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence lacks kinase catalytic motifs (HRD, DFG, VAIK) required for MAP kinase activity (B), lacks PLP-dependent enzyme catalytic residues for threonine synthase (C), and lacks C2 domain calcium-binding loops for calcium-dependent phospholipid binding (A). By elimination, the remaining option (D) is consistent with the protein's chromatin-associated context. Additionally, the sequence contains a cluster of aromatic residues (multiple Y, F in the C-terminal region) patterned consistently with a Tudor-domain aromatic cage used for methyl-lysine recognition, providing weak positive support for methylated histone binding.


**Missing item-specific fact**

> Positive identification of the Tudor domain from sequence alone is non-trivial without structural knowledge or database annotation. The specific assignment to 'methylated histone binding' over other non-catalytic binding functions relies partly on recognizing the protein's identity or the Tudor fold.


**Reason**

> Elimination of three options through absence of characteristic catalytic/binding motifs is achievable through general biological knowledge. The remaining option is the only non-catalytic binding function and is consistent with the aromatic residue pattern. However, the positive identification is somewhat indirect and relies on elimination rather than a strong direct sequence signature.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options A, B, and C each require specific catalytic or structural features (kinase motifs, PLP enzyme machinery, C2 domain) that are clearly absent from the sequence. Option D is the only remaining viable choice and is supported by the annotated reader activities. No other option is defensible.


### Important caveats

- The GO annotations for methylated histone reader activity carry ISS (Inferred from Sequence/Similarity) evidence codes, not direct experimental evidence for this specific protein.
- 'Methylated histone binding' is a paraphrase, not an exact GO term (ontology_option_term_candidates show empty term_ids for option D). The closest annotated terms are 'histone H3K4me3 reader activity' and 'histone H3K36me3 reader activity.'
- The protein's primary annotated function is as a component of SAGA/CHAT histone acetyltransferase complexes; the methyl-lysine reader activity is a sub-function within that complex context.
- The Tudor domain identification from raw sequence is speculative without structural confirmation; the elimination-based reasoning is more robust than positive sequence recognition for this case.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence lacks kinase catalytic motifs (HRD, DFG, VAIK) required for MAP kinase activity (B), lacks PLP-dependent enzyme catalytic residues for threonine synthase (C), and lacks C2 domain calcium-binding loops for calcium-dependent phospholipid binding (A). By elimination, the remaining option (D) is consistent with the protein's chromatin-associated context. Additionally, the sequence contains a cluster of aromatic residues (multiple Y, F in the C-terminal region) patterned consistently with a Tudor-domain aromatic cage used for methyl-lysine recognition, providing weak positive support for methylated histone binding.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "Positive identification of the Tudor domain from sequence alone is non-trivial without structural knowledge or database annotation. The specific assignment to 'methylated histone binding' over other non-catalytic binding functions relies partly on recognizing the protein's identity or the Tudor fold.",
    "reason": "Elimination of three options through absence of characteristic catalytic/binding motifs is achievable through general biological knowledge. The remaining option is the only non-catalytic binding function and is consistent with the aromatic residue pattern. However, the positive identification is somewhat indirect and relies on elimination rather than a strong direct sequence signature."
  },
  "case_id": "GO_molecular_function_0190",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "C7",
      "H7",
      "H8",
      "H9"
    ],
    "judgment": "supported",
    "reason": "The protein is Drosophila Sgf29 (Q9W2I4), annotated with GO:0140002 'histone H3K4me3 reader activity' and GO:0140003 'histone H3K36me3 reader activity' (both ISS:FlyBase). These reader activities involve binding to methylated histone residues, making 'methylated histone binding' a valid generalization. The protein is also confirmed as a component of SAGA/CHAT histone acetyltransferase complexes. However, the evidence codes are ISS (inferred by sequence/similarity), not direct experimental binding assays for this specific protein, so the support is computational/annotation-based rather than experimentally demonstrated for this exact protein."
  },
  "important_caveats": [
    "The GO annotations for methylated histone reader activity carry ISS (Inferred from Sequence/Similarity) evidence codes, not direct experimental evidence for this specific protein.",
    "'Methylated histone binding' is a paraphrase, not an exact GO term (ontology_option_term_candidates show empty term_ids for option D). The closest annotated terms are 'histone H3K4me3 reader activity' and 'histone H3K36me3 reader activity.'",
    "The protein's primary annotated function is as a component of SAGA/CHAT histone acetyltransferase complexes; the methyl-lysine reader activity is a sub-function within that complex context.",
    "The Tudor domain identification from raw sequence is speculative without structural confirmation; the elimination-based reasoning is more robust than positive sequence recognition for this case."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A, B, and C each require specific catalytic or structural features (kinase motifs, PLP enzyme machinery, C2 domain) that are clearly absent from the sequence. Option D is the only remaining viable choice and is supported by the annotated reader activities. No other option is defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0190",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The protein is Drosophila Sgf29 (Q9W2I4), annotated with GO:0140002 'histone H3K4me3 reader activity' and GO:0140003 'histone H3K36me3 reader activity' (both ISS:FlyBase). These reader activities involve binding to methylated histone residues, making 'methylated histone binding' a valid generalization. The protein is also confirmed as a component of SAGA/CHAT histone acetyltransferase complexes. However, the evidence codes are ISS (inferred by sequence/similarity), not direct experimental binding assays for this specific protein, so the support is computational/annotation-based rather than experimentally demonstrated for this exact protein.",
    "evidence_ids": ["C5", "C6", "C7", "H7", "H8", "H9"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence lacks kinase catalytic motifs (HRD, DFG, VAIK) required for MAP kinase activity (B), lacks PLP-dependent enzyme catalytic residues for threonine synthase (C), and lacks C2 domain calcium-binding loops for calcium-dependent phospholipid binding (A). By elimination, the remaining option (D) is consistent with the protein's chromatin-associated context. Additionally, the sequence contains a cluster of aromatic residues (multiple Y, F in the C-terminal region) patterned consistently with a Tudor-domain aromatic cage used for methyl-lysine recognition, providing weak positive support for methylated histone binding.",
    "missing_item_specific_fact": "Positive identification of the Tudor domain from sequence alone is non-trivial without structural knowledge or database annotation. The specific assignment to 'methylated histone binding' over other non-catalytic binding functions relies partly on recognizing the protein's identity or the Tudor fold.",
    "reason": "Elimination of three options through absence of characteristic catalytic/binding motifs is achievable through general biological knowledge. The remaining option is the only non-catalytic binding function and is consistent with the aromatic residue pattern. However, the positive identification is somewhat indirect and relies on elimination rather than a strong direct sequence signature."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A, B, and C each require specific catalytic or structural features (kinase motifs, PLP enzyme machinery, C2 domain) that are clearly absent from the sequence. Option D is the only remaining viable choice and is supported by the annotated reader activities. No other option is defensible."
  },
  "important_caveats": [
    "The GO annotations for methylated histone reader activity carry ISS (Inferred from Sequence/Similarity) evidence codes, not direct experimental evidence for this specific protein.",
    "'Methylated histone binding' is a paraphrase, not an exact GO term (ontology_option_term_candidates show empty term_ids for option D). The closest annotated terms are 'histone H3K4me3 reader activity' and 'histone H3K36me3 reader activity.'",
    "The protein's primary annotated function is as a component of SAGA/CHAT histone acetyltransferase complexes; the methyl-lysine reader activity is a sub-function within that complex context.",
    "The Tudor domain identification from raw sequence is speculative without structural confirmation; the elimination-based reasoning is more robust than positive sequence recognition for this case."
  ]
}
```

</details>

## After: GPT-6 Luna

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence-matched UniProt record assigns histone H3K36me3 and H3K4me3 reader activities, both consistent with methylated histone binding. These GO annotations are supported as annotations, though their evidence code is ISS rather than direct experimental evidence in the supplied excerpts.

Citations as saved: [C6](#evidence-c6), [C7](#evidence-c7).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> A knowledgeable model can recognize a plausible Tudor-domain histone-reader profile in the sequence using patterns learned from related proteins. Tudor reader domains use an aromatic cage to bind methylated lysines on histones, making methylated histone binding a meaningful fit. The sequence does not show the characteristic catalytic architecture expected for a MAP kinase or threonine synthase, nor an evident calcium-dependent phospholipid-binding domain.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The family/domain-level inference distinguishes D from these alternatives without needing the exact protein's database annotation. It is a credible sequence-based inference, although not a direct demonstration of binding.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the offered choices, methylated histone binding is the only one supported by the likely reader-domain profile.


### Important caveats

- The supplied GO evidence for the specific reader activities is ISS (inferred from sequence or structural similarity), not direct experimental evidence in these excerpts.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "A knowledgeable model can recognize a plausible Tudor-domain histone-reader profile in the sequence using patterns learned from related proteins. Tudor reader domains use an aromatic cage to bind methylated lysines on histones, making methylated histone binding a meaningful fit. The sequence does not show the characteristic catalytic architecture expected for a MAP kinase or threonine synthase, nor an evident calcium-dependent phospholipid-binding domain.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The family/domain-level inference distinguishes D from these alternatives without needing the exact protein's database annotation. It is a credible sequence-based inference, although not a direct demonstration of binding."
  },
  "case_id": "GO_molecular_function_0190",
  "expected_answer_check": {
    "evidence_ids": [
      "C6",
      "C7"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record assigns histone H3K36me3 and H3K4me3 reader activities, both consistent with methylated histone binding. These GO annotations are supported as annotations, though their evidence code is ISS rather than direct experimental evidence in the supplied excerpts."
  },
  "important_caveats": [
    "The supplied GO evidence for the specific reader activities is ISS (inferred from sequence or structural similarity), not direct experimental evidence in these excerpts."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the offered choices, methylated histone binding is the only one supported by the likely reader-domain profile."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0190",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record assigns histone H3K36me3 and H3K4me3 reader activities, both consistent with methylated histone binding. These GO annotations are supported as annotations, though their evidence code is ISS rather than direct experimental evidence in the supplied excerpts.",
    "evidence_ids": ["C6", "C7"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "A knowledgeable model can recognize a plausible Tudor-domain histone-reader profile in the sequence using patterns learned from related proteins. Tudor reader domains use an aromatic cage to bind methylated lysines on histones, making methylated histone binding a meaningful fit. The sequence does not show the characteristic catalytic architecture expected for a MAP kinase or threonine synthase, nor an evident calcium-dependent phospholipid-binding domain.",
    "missing_item_specific_fact": "",
    "reason": "The family/domain-level inference distinguishes D from these alternatives without needing the exact protein's database annotation. It is a credible sequence-based inference, although not a direct demonstration of binding."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the offered choices, methylated histone binding is the only one supported by the likely reader-domain profile."
  },
  "important_caveats": [
    "The supplied GO evidence for the specific reader activities is ISS (inferred from sequence or structural similarity), not direct experimental evidence in these excerpts."
  ]
}
```

</details>

## After: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry (Q9W2I4, Sgf29_DROME) carries GO:0140003 (histone H3K36me3 reader activity) and GO:0140002 (histone H3K4me3 reader activity), both annotated via ISS:FlyBase. These describe reading methylated histone marks, which is a specific form of methylated histone binding. The option text 'methylated histone binding' is a reasonable generalization of these reader activities. The evidence is ISS (inferred from sequence similarity) rather than direct experimental proof for this exact protein, but the annotations are consistent with and support the expected answer. The protein is also documented as a component of SAGA/CHAT histone acetyltransferase complexes, consistent with histone-interaction function.

Citations as saved: [C6](#evidence-c6), [C7](#evidence-c7), [C5](#evidence-c5), [H8](#evidence-h8), [H9](#evidence-h9), [H7](#evidence-h7).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 289-residue sequence contains recognizable WD40 repeats in the C-terminal half (alternating hydrophobic residues, 'GKLGER', 'NYVAKVGDN', 'WILAE', 'VIDIDEE', 'VLSKRKV', 'VPLPLMR', 'VVMALYP', 'VIAYRP' patterns) and a coiled-coil/histone-fold-like region in the N-terminal half (heptad repeat patterns in 'IQDRLKDIQQNIHNVDEERRRAENSIASLVRSLHATNQKVKPLLKASLTEAAQEEATIRAALAKIHEIRSIRNERRIQARNAGNKEAIRRGALMKMVQLSAQ'). WD40 repeats are a well-known protein-interaction module found in chromatin readers (e.g., TAF3 TFIID subunit, ING family H3K4me3 readers, other SAGA subunits). The combination of a histone-fold/coiled-coil region with WD40 repeats in a small ~29 kDa protein is characteristic of chromatin-associated histone readers. Option B (MAP kinase activity) requires a kinase catalytic domain with DFG motif, glycine-rich loop, and activation segment—none present. Option C (threonine synthase) requires PLP-binding motifs and lyase catalytic residues—absent. Option A (calcium-dependent phospholipid binding) requires C2 domains or EF-hand calcium-binding motifs—absent. Among the four options, only D (methylated histone binding) is consistent with a WD40-containing chromatin protein. Transferable knowledge from homologous SAGA subunits (yeast Sgf29, human SGF29) and other WD40 histone readers supports this inference.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can recognize WD40 repeats and histone-fold/coiled-coil features from the sequence, rule out kinase (B), PLP-lyase (C), and calcium/phospholipid-binding (A) based on the absence of their defining motifs, and select D based on the well-established association of WD40 domains with histone reading in chromatin complexes. This is a family-level and structural-feature inference, not a lookup of this protein's specific annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options A, B, and C require specific catalytic or binding motifs (kinase domain, PLP-binding site, C2/EF-hand) that are clearly absent from the sequence. Only D is consistent with the observed WD40 + histone-fold architecture. No alternative option is defensible.


### Important caveats

- The GO annotations for this protein are ISS (Inferred from Sequence Similarity), meaning the methylated-histone-reader function is transferred from homologs (e.g., yeast Sgf29) rather than demonstrated experimentally for this Drosophila protein specifically.
- The option text 'methylated histone binding' does not exactly match a single GO term (term_ids for option D are empty in the ontology mapping), but it is a reasonable functional generalization of GO:0140002 and GO:0140003.
- The reviewer-only evidence confirms the protein identity (Q9W2I4, Sgf29_DROME) and its SAGA/CHAT complex membership, but this identity was not provided to the evaluated model; the model must infer function from sequence features alone.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 289-residue sequence contains recognizable WD40 repeats in the C-terminal half (alternating hydrophobic residues, 'GKLGER', 'NYVAKVGDN', 'WILAE', 'VIDIDEE', 'VLSKRKV', 'VPLPLMR', 'VVMALYP', 'VIAYRP' patterns) and a coiled-coil/histone-fold-like region in the N-terminal half (heptad repeat patterns in 'IQDRLKDIQQNIHNVDEERRRAENSIASLVRSLHATNQKVKPLLKASLTEAAQEEATIRAALAKIHEIRSIRNERRIQARNAGNKEAIRRGALMKMVQLSAQ'). WD40 repeats are a well-known protein-interaction module found in chromatin readers (e.g., TAF3 TFIID subunit, ING family H3K4me3 readers, other SAGA subunits). The combination of a histone-fold/coiled-coil region with WD40 repeats in a small ~29 kDa protein is characteristic of chromatin-associated histone readers. Option B (MAP kinase activity) requires a kinase catalytic domain with DFG motif, glycine-rich loop, and activation segment—none present. Option C (threonine synthase) requires PLP-binding motifs and lyase catalytic residues—absent. Option A (calcium-dependent phospholipid binding) requires C2 domains or EF-hand calcium-binding motifs—absent. Among the four options, only D (methylated histone binding) is consistent with a WD40-containing chromatin protein. Transferable knowledge from homologous SAGA subunits (yeast Sgf29, human SGF29) and other WD40 histone readers supports this inference.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can recognize WD40 repeats and histone-fold/coiled-coil features from the sequence, rule out kinase (B), PLP-lyase (C), and calcium/phospholipid-binding (A) based on the absence of their defining motifs, and select D based on the well-established association of WD40 domains with histone reading in chromatin complexes. This is a family-level and structural-feature inference, not a lookup of this protein's specific annotation."
  },
  "case_id": "GO_molecular_function_0190",
  "expected_answer_check": {
    "evidence_ids": [
      "C6",
      "C7",
      "C5",
      "H8",
      "H9",
      "H7"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry (Q9W2I4, Sgf29_DROME) carries GO:0140003 (histone H3K36me3 reader activity) and GO:0140002 (histone H3K4me3 reader activity), both annotated via ISS:FlyBase. These describe reading methylated histone marks, which is a specific form of methylated histone binding. The option text 'methylated histone binding' is a reasonable generalization of these reader activities. The evidence is ISS (inferred from sequence similarity) rather than direct experimental proof for this exact protein, but the annotations are consistent with and support the expected answer. The protein is also documented as a component of SAGA/CHAT histone acetyltransferase complexes, consistent with histone-interaction function."
  },
  "important_caveats": [
    "The GO annotations for this protein are ISS (Inferred from Sequence Similarity), meaning the methylated-histone-reader function is transferred from homologs (e.g., yeast Sgf29) rather than demonstrated experimentally for this Drosophila protein specifically.",
    "The option text 'methylated histone binding' does not exactly match a single GO term (term_ids for option D are empty in the ontology mapping), but it is a reasonable functional generalization of GO:0140002 and GO:0140003.",
    "The reviewer-only evidence confirms the protein identity (Q9W2I4, Sgf29_DROME) and its SAGA/CHAT complex membership, but this identity was not provided to the evaluated model; the model must infer function from sequence features alone."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A, B, and C require specific catalytic or binding motifs (kinase domain, PLP-binding site, C2/EF-hand) that are clearly absent from the sequence. Only D is consistent with the observed WD40 + histone-fold architecture. No alternative option is defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0190",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry (Q9W2I4, Sgf29_DROME) carries GO:0140003 (histone H3K36me3 reader activity) and GO:0140002 (histone H3K4me3 reader activity), both annotated via ISS:FlyBase. These describe reading methylated histone marks, which is a specific form of methylated histone binding. The option text 'methylated histone binding' is a reasonable generalization of these reader activities. The evidence is ISS (inferred from sequence similarity) rather than direct experimental proof for this exact protein, but the annotations are consistent with and support the expected answer. The protein is also documented as a component of SAGA/CHAT histone acetyltransferase complexes, consistent with histone-interaction function.",
    "evidence_ids": ["C6", "C7", "C5", "H8", "H9", "H7"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 289-residue sequence contains recognizable WD40 repeats in the C-terminal half (alternating hydrophobic residues, 'GKLGER', 'NYVAKVGDN', 'WILAE', 'VIDIDEE', 'VLSKRKV', 'VPLPLMR', 'VVMALYP', 'VIAYRP' patterns) and a coiled-coil/histone-fold-like region in the N-terminal half (heptad repeat patterns in 'IQDRLKDIQQNIHNVDEERRRAENSIASLVRSLHATNQKVKPLLKASLTEAAQEEATIRAALAKIHEIRSIRNERRIQARNAGNKEAIRRGALMKMVQLSAQ'). WD40 repeats are a well-known protein-interaction module found in chromatin readers (e.g., TAF3 TFIID subunit, ING family H3K4me3 readers, other SAGA subunits). The combination of a histone-fold/coiled-coil region with WD40 repeats in a small ~29 kDa protein is characteristic of chromatin-associated histone readers. Option B (MAP kinase activity) requires a kinase catalytic domain with DFG motif, glycine-rich loop, and activation segment—none present. Option C (threonine synthase) requires PLP-binding motifs and lyase catalytic residues—absent. Option A (calcium-dependent phospholipid binding) requires C2 domains or EF-hand calcium-binding motifs—absent. Among the four options, only D (methylated histone binding) is consistent with a WD40-containing chromatin protein. Transferable knowledge from homologous SAGA subunits (yeast Sgf29, human SGF29) and other WD40 histone readers supports this inference.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can recognize WD40 repeats and histone-fold/coiled-coil features from the sequence, rule out kinase (B), PLP-lyase (C), and calcium/phospholipid-binding (A) based on the absence of their defining motifs, and select D based on the well-established association of WD40 domains with histone reading in chromatin complexes. This is a family-level and structural-feature inference, not a lookup of this protein's specific annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A, B, and C require specific catalytic or binding motifs (kinase domain, PLP-binding site, C2/EF-hand) that are clearly absent from the sequence. Only D is consistent with the observed WD40 + histone-fold architecture. No alternative option is defensible."
  },
  "important_caveats": [
    "The GO annotations for this protein are ISS (Inferred from Sequence Similarity), meaning the methylated-histone-reader function is transferred from homologs (e.g., yeast Sgf29) rather than demonstrated experimentally for this Drosophila protein specifically.",
    "The option text 'methylated histone binding' does not exactly match a single GO term (term_ids for option D are empty in the ontology mapping), but it is a reasonable functional generalization of GO:0140002 and GO:0140003.",
    "The reviewer-only evidence confirms the protein identity (Q9W2I4, Sgf29_DROME) and its SAGA/CHAT complex membership, but this identity was not provided to the evaluated model; the model must infer function from sequence features alone."
  ]
}
```

</details>

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
  "requested_accession": "Q9W2I4",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "benchmark_sequence_sha256": "56bfcc6869c1cec19263500d511a7aa9d950b825750317b030d3a5072e39bde4",
  "benchmark_sequence_length": 289,
  "current_status": "retrieved",
  "current_sequence_comparison": "matched",
  "current_entry_audit": {
    "entryVersion": 174,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2002-10-01",
    "sequenceVersion": 2
  },
  "current_uniprot_release": "2026_03",
  "current_record_sha256": "99e79ffdf07452f0c2ae6b5b82b60c28b7ea2d0331542973f4e028462aab9481",
  "current_source_sequence_sha256": "56bfcc6869c1cec19263500d511a7aa9d950b825750317b030d3a5072e39bde4",
  "current_source_sequence_length": 289,
  "historical_status": "retrieved",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "selected_historical_entry_version": 172,
  "selected_historical_version": {
    "accession": "Q9W2I4",
    "database": "Swiss-Prot",
    "entryVersion": 172,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "SGF29_DROME",
    "sequenceVersion": 2
  },
  "selected_historical_record_sha256": "9cdab37ca5165bf0ed7c572bc5323ec3cdbf7ef551b85431bdf2251f55d4d874",
  "selected_historical_source_sequence_sha256": "56bfcc6869c1cec19263500d511a7aa9d950b825750317b030d3a5072e39bde4",
  "selected_historical_source_sequence_length": 289,
  "latest_at_cutoff_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 172,
      "exact_sequence_comparison": "matched",
      "sequence_version": 2
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9W2I4.json)

```json
{
  "evidence_id": "C1",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q9W2I4.json",
  "source_sha256": "99e79ffdf07452f0c2ae6b5b82b60c28b7ea2d0331542973f4e028462aab9481",
  "retrieved_utc": "2026-11-02T04:33:46.947791+00:00",
  "json_pointer": "/primaryAccession",
  "excerpt": "\"Q9W2I4\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9W2I4.json)

```json
{
  "evidence_id": "C2",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q9W2I4.json",
  "source_sha256": "99e79ffdf07452f0c2ae6b5b82b60c28b7ea2d0331542973f4e028462aab9481",
  "retrieved_utc": "2026-11-02T04:33:46.947791+00:00",
  "json_pointer": "/entryAudit",
  "excerpt": "{\"entryVersion\":174,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2002-10-01\",\"sequenceVersion\":2}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9W2I4.json)

```json
{
  "evidence_id": "C3",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q9W2I4.json",
  "source_sha256": "99e79ffdf07452f0c2ae6b5b82b60c28b7ea2d0331542973f4e028462aab9481",
  "retrieved_utc": "2026-11-02T04:33:46.947791+00:00",
  "json_pointer": "/organism",
  "excerpt": "{\"commonName\":\"Fruit fly\",\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP000000803\",\"source\":\"Proteomes\"}],\"lineage\":[\"Eukaryota\",\"Metazoa\",\"Ecdysozoa\",\"Arthropoda\",\"Altocrustacea\",\"Allotriocarida\",\"Hexapoda\",\"Insecta\",\"Pterygota\",\"Neoptera\",\"Eumetabola\",\"Endopterygota\",\"Aparaglossata\",\"Panorpida\",\"Diptera\",\"Brachycera\",\"Muscomorpha\",\"Ephydroidea\",\"Drosophilidae\",\"Drosophila\",\"Sophophora\"],\"scientificName\":\"Drosophila melanogaster\",\"taxonId\":7227}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9W2I4.json)

```json
{
  "evidence_id": "C4",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q9W2I4.json",
  "source_sha256": "99e79ffdf07452f0c2ae6b5b82b60c28b7ea2d0331542973f4e028462aab9481",
  "retrieved_utc": "2026-11-02T04:33:46.947791+00:00",
  "json_pointer": "/proteinDescription",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"SAGA complex subunit Sgf29\"}}],\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"FBgn0050390\",\"source\":\"FlyBase\"}],\"value\":\"SAGA-associated factor 29kDa\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9W2I4.json)

```json
{
  "evidence_id": "C5",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q9W2I4.json",
  "source_sha256": "99e79ffdf07452f0c2ae6b5b82b60c28b7ea2d0331542973f4e028462aab9481",
  "retrieved_utc": "2026-11-02T04:33:46.947791+00:00",
  "json_pointer": "/comments/0",
  "excerpt": "{\"commentType\":\"FUNCTION\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"16980620\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"20008933\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"21764853\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"24493646\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"30559249\",\"source\":\"PubMed\"}],\"value\":\"Component of both the SAGA and CHAT histone acetyltransferase complexes, which both predominantly acetylate histone H3\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9W2I4.json)

```json
{
  "evidence_id": "C6",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q9W2I4.json",
  "source_sha256": "99e79ffdf07452f0c2ae6b5b82b60c28b7ea2d0331542973f4e028462aab9481",
  "retrieved_utc": "2026-11-02T04:33:46.947791+00:00",
  "json_pointer": "/uniProtKBCrossReferences/41",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0140003\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"F:histone H3K36me3 reader activity\"},{\"key\":\"GoEvidenceType\",\"value\":\"ISS:FlyBase\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9W2I4.json)

```json
{
  "evidence_id": "C7",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q9W2I4.json",
  "source_sha256": "99e79ffdf07452f0c2ae6b5b82b60c28b7ea2d0331542973f4e028462aab9481",
  "retrieved_utc": "2026-11-02T04:33:46.947791+00:00",
  "json_pointer": "/uniProtKBCrossReferences/42",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0140002\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"F:histone H3K4me3 reader activity\"},{\"key\":\"GoEvidenceType\",\"value\":\"ISS:FlyBase\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9W2I4.json)

```json
{
  "evidence_id": "C8",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q9W2I4.json",
  "source_sha256": "99e79ffdf07452f0c2ae6b5b82b60c28b7ea2d0331542973f4e028462aab9481",
  "retrieved_utc": "2026-11-02T04:33:46.947791+00:00",
  "json_pointer": "/references/3",
  "excerpt": "{\"citation\":{\"authors\":[\"Guelman S.\",\"Suganuma T.\",\"Florens L.\",\"Weake V.\",\"Swanson S.K.\",\"Washburn M.P.\",\"Abmayr S.M.\",\"Workman J.L.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"16980620\"},{\"database\":\"DOI\",\"id\":\"10.1128/mcb.00130-06\"}],\"citationType\":\"journal article\",\"firstPage\":\"7178\",\"id\":\"16980620\",\"journal\":\"Mol. Cell. Biol.\",\"lastPage\":\"7189\",\"publicationDate\":\"2006\",\"title\":\"The essential gene wda encodes a WD40 repeat subunit of Drosophila SAGA required for histone H3 acetylation.\",\"volume\":\"26\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":4,\"referencePositions\":[\"FUNCTION\",\"IDENTIFICATION IN SAGA COMPLEX\",\"IDENTIFICATION BY MASS SPECTROMETRY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9W2I4.json)

```json
{
  "evidence_id": "C9",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q9W2I4.json",
  "source_sha256": "99e79ffdf07452f0c2ae6b5b82b60c28b7ea2d0331542973f4e028462aab9481",
  "retrieved_utc": "2026-11-02T04:33:46.947791+00:00",
  "json_pointer": "/references/4",
  "excerpt": "{\"citation\":{\"authors\":[\"Weake V.M.\",\"Swanson S.K.\",\"Mushegian A.\",\"Florens L.\",\"Washburn M.P.\",\"Abmayr S.M.\",\"Workman J.L.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"20008933\"},{\"database\":\"DOI\",\"id\":\"10.1101/gad.1846409\"}],\"citationType\":\"journal article\",\"firstPage\":\"2818\",\"id\":\"20008933\",\"journal\":\"Genes Dev.\",\"lastPage\":\"2823\",\"publicationDate\":\"2009\",\"title\":\"A novel histone fold domain-containing protein that replaces TAF6 in Drosophila SAGA is required for SAGA-dependent gene expression.\",\"volume\":\"23\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":5,\"referencePositions\":[\"FUNCTION\",\"IDENTIFICATION IN SAGA COMPLEX\",\"SUBCELLULAR LOCATION\",\"IDENTIFICATION BY MASS SPECTROMETRY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9W2I4.json)

```json
{
  "evidence_id": "C10",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q9W2I4.json",
  "source_sha256": "99e79ffdf07452f0c2ae6b5b82b60c28b7ea2d0331542973f4e028462aab9481",
  "retrieved_utc": "2026-11-02T04:33:46.947791+00:00",
  "json_pointer": "/references/5",
  "excerpt": "{\"citation\":{\"authors\":[\"Weake V.M.\",\"Dyer J.O.\",\"Seidel C.\",\"Box A.\",\"Swanson S.K.\",\"Peak A.\",\"Florens L.\",\"Washburn M.P.\",\"Abmayr S.M.\",\"Workman J.L.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"21764853\"},{\"database\":\"DOI\",\"id\":\"10.1101/gad.2046211\"}],\"citationType\":\"journal article\",\"firstPage\":\"1499\",\"id\":\"21764853\",\"journal\":\"Genes Dev.\",\"lastPage\":\"1509\",\"publicationDate\":\"2011\",\"title\":\"Post-transcription initiation function of the ubiquitous SAGA complex in tissue-specific gene activation.\",\"volume\":\"25\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":6,\"referencePositions\":[\"FUNCTION\",\"IDENTIFICATION IN SAGA COMPLEX\",\"DEVELOPMENTAL STAGE\",\"IDENTIFICATION BY MASS SPECTROMETRY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9W2I4.json)

```json
{
  "evidence_id": "C11",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q9W2I4.json",
  "source_sha256": "99e79ffdf07452f0c2ae6b5b82b60c28b7ea2d0331542973f4e028462aab9481",
  "retrieved_utc": "2026-11-02T04:33:46.947791+00:00",
  "json_pointer": "/references/6",
  "excerpt": "{\"citation\":{\"authors\":[\"Mohan R.D.\",\"Dialynas G.\",\"Weake V.M.\",\"Liu J.\",\"Martin-Brown S.\",\"Florens L.\",\"Washburn M.P.\",\"Workman J.L.\",\"Abmayr S.M.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"24493646\"},{\"database\":\"DOI\",\"id\":\"10.1101/gad.225151.113\"}],\"citationType\":\"journal article\",\"firstPage\":\"259\",\"id\":\"24493646\",\"journal\":\"Genes Dev.\",\"lastPage\":\"272\",\"publicationDate\":\"2014\",\"title\":\"Loss of Drosophila Ataxin-7, a SAGA subunit, reduces H2B ubiquitination and leads to neural and retinal degeneration.\",\"volume\":\"28\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":7,\"referencePositions\":[\"FUNCTION\",\"IDENTIFICATION IN THE SAGA COMPLEX\",\"SUBCELLULAR LOCATION\",\"IDENTIFICATION BY MASS SPECTROMETRY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9W2I4.json)

```json
{
  "evidence_id": "C12",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q9W2I4.json",
  "source_sha256": "99e79ffdf07452f0c2ae6b5b82b60c28b7ea2d0331542973f4e028462aab9481",
  "retrieved_utc": "2026-11-02T04:33:46.947791+00:00",
  "json_pointer": "/references/7",
  "excerpt": "{\"citation\":{\"authors\":[\"Torres-Zelada E.F.\",\"Stephenson R.E.\",\"Alpsoy A.\",\"Anderson B.D.\",\"Swanson S.K.\",\"Florens L.\",\"Dykhuizen E.C.\",\"Washburn M.P.\",\"Weake V.M.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"30559249\"},{\"database\":\"DOI\",\"id\":\"10.1242/jcs.214072\"}],\"citationType\":\"journal article\",\"firstPage\":\"0\",\"id\":\"30559249\",\"journal\":\"J. Cell Sci.\",\"lastPage\":\"0\",\"publicationDate\":\"2019\",\"title\":\"The Drosophila Dbf4 ortholog Chiffon forms a complex with Gcn5 that is necessary for histone acetylation and viability.\",\"volume\":\"132\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":8,\"referencePositions\":[\"FUNCTION\",\"IDENTIFICATION IN THE SAGA AND CHAT COMPLEXES\",\"IDENTIFICATION BY MASS SPECTROMETRY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9W2I4?format=txt&versions=172)

```json
{
  "evidence_id": "H1",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q9W2I4?format=txt&versions=172",
  "source_sha256": "9cdab37ca5165bf0ed7c572bc5323ec3cdbf7ef551b85431bdf2251f55d4d874",
  "retrieved_utc": "2026-11-02T04:33:50.066048+00:00",
  "source_locator": "lines 1-14",
  "excerpt": "ID   SGF29_DROME             Reviewed;         289 AA.\nAC   Q9W2I4;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   01-OCT-2002, sequence version 2.\nDT   28-JAN-2026, entry version 172.\nDE   RecName: Full=SAGA-associated factor 29kDa {ECO:0000312|FlyBase:FBgn0050390};\nDE   AltName: Full=SAGA complex subunit Sgf29 {ECO:0000305};\nGN   Name=Sgf29 {ECO:0000303|PubMed:16980620, ECO:0000312|FlyBase:FBgn0050390};\nGN   ORFNames=CG30390 {ECO:0000312|FlyBase:FBgn0050390};\nOS   Drosophila melanogaster (Fruit fly).\nOC   Eukaryota; Metazoa; Ecdysozoa; Arthropoda; Hexapoda; Insecta; Pterygota;\nOC   Neoptera; Endopterygota; Diptera; Brachycera; Muscomorpha; Ephydroidea;\nOC   Drosophilidae; Drosophila; Sophophora.\nOX   NCBI_TaxID=7227 {ECO:0000312|Proteomes:UP000000803};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 172,
  "sequence_version": 2,
  "sequence_comparison": "matched"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9W2I4?format=txt&versions=172)

```json
{
  "evidence_id": "H2",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q9W2I4?format=txt&versions=172",
  "source_sha256": "9cdab37ca5165bf0ed7c572bc5323ec3cdbf7ef551b85431bdf2251f55d4d874",
  "retrieved_utc": "2026-11-02T04:33:50.066048+00:00",
  "source_locator": "lines 73-81",
  "excerpt": "RN   [4] {ECO:0000305}\nRP   FUNCTION, IDENTIFICATION IN SAGA COMPLEX, AND IDENTIFICATION BY MASS\nRP   SPECTROMETRY.\nRX   PubMed=16980620; DOI=10.1128/mcb.00130-06;\nRA   Guelman S., Suganuma T., Florens L., Weake V., Swanson S.K., Washburn M.P.,\nRA   Abmayr S.M., Workman J.L.;\nRT   \"The essential gene wda encodes a WD40 repeat subunit of Drosophila SAGA\nRT   required for histone H3 acetylation.\";\nRL   Mol. Cell. Biol. 26:7178-7189(2006).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 172,
  "sequence_version": 2,
  "sequence_comparison": "matched"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9W2I4?format=txt&versions=172)

```json
{
  "evidence_id": "H3",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q9W2I4?format=txt&versions=172",
  "source_sha256": "9cdab37ca5165bf0ed7c572bc5323ec3cdbf7ef551b85431bdf2251f55d4d874",
  "retrieved_utc": "2026-11-02T04:33:50.066048+00:00",
  "source_locator": "lines 82-90",
  "excerpt": "RN   [5] {ECO:0000305}\nRP   FUNCTION, IDENTIFICATION IN SAGA COMPLEX, SUBCELLULAR LOCATION, AND\nRP   IDENTIFICATION BY MASS SPECTROMETRY.\nRX   PubMed=20008933; DOI=10.1101/gad.1846409;\nRA   Weake V.M., Swanson S.K., Mushegian A., Florens L., Washburn M.P.,\nRA   Abmayr S.M., Workman J.L.;\nRT   \"A novel histone fold domain-containing protein that replaces TAF6 in\nRT   Drosophila SAGA is required for SAGA-dependent gene expression.\";\nRL   Genes Dev. 23:2818-2823(2009).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 172,
  "sequence_version": 2,
  "sequence_comparison": "matched"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9W2I4?format=txt&versions=172)

```json
{
  "evidence_id": "H4",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q9W2I4?format=txt&versions=172",
  "source_sha256": "9cdab37ca5165bf0ed7c572bc5323ec3cdbf7ef551b85431bdf2251f55d4d874",
  "retrieved_utc": "2026-11-02T04:33:50.066048+00:00",
  "source_locator": "lines 91-99",
  "excerpt": "RN   [6] {ECO:0000305}\nRP   FUNCTION, IDENTIFICATION IN SAGA COMPLEX, DEVELOPMENTAL STAGE, AND\nRP   IDENTIFICATION BY MASS SPECTROMETRY.\nRX   PubMed=21764853; DOI=10.1101/gad.2046211;\nRA   Weake V.M., Dyer J.O., Seidel C., Box A., Swanson S.K., Peak A.,\nRA   Florens L., Washburn M.P., Abmayr S.M., Workman J.L.;\nRT   \"Post-transcription initiation function of the ubiquitous SAGA complex in\nRT   tissue-specific gene activation.\";\nRL   Genes Dev. 25:1499-1509(2011).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 172,
  "sequence_version": 2,
  "sequence_comparison": "matched"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9W2I4?format=txt&versions=172)

```json
{
  "evidence_id": "H5",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q9W2I4?format=txt&versions=172",
  "source_sha256": "9cdab37ca5165bf0ed7c572bc5323ec3cdbf7ef551b85431bdf2251f55d4d874",
  "retrieved_utc": "2026-11-02T04:33:50.066048+00:00",
  "source_locator": "lines 100-108",
  "excerpt": "RN   [7] {ECO:0000305}\nRP   FUNCTION, IDENTIFICATION IN THE SAGA COMPLEX, SUBCELLULAR LOCATION, AND\nRP   IDENTIFICATION BY MASS SPECTROMETRY.\nRX   PubMed=24493646; DOI=10.1101/gad.225151.113;\nRA   Mohan R.D., Dialynas G., Weake V.M., Liu J., Martin-Brown S., Florens L.,\nRA   Washburn M.P., Workman J.L., Abmayr S.M.;\nRT   \"Loss of Drosophila Ataxin-7, a SAGA subunit, reduces H2B ubiquitination\nRT   and leads to neural and retinal degeneration.\";\nRL   Genes Dev. 28:259-272(2014).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 172,
  "sequence_version": 2,
  "sequence_comparison": "matched"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9W2I4?format=txt&versions=172)

```json
{
  "evidence_id": "H6",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q9W2I4?format=txt&versions=172",
  "source_sha256": "9cdab37ca5165bf0ed7c572bc5323ec3cdbf7ef551b85431bdf2251f55d4d874",
  "retrieved_utc": "2026-11-02T04:33:50.066048+00:00",
  "source_locator": "lines 109-117",
  "excerpt": "RN   [8] {ECO:0000305}\nRP   FUNCTION, IDENTIFICATION IN THE SAGA AND CHAT COMPLEXES, AND IDENTIFICATION\nRP   BY MASS SPECTROMETRY.\nRX   PubMed=30559249; DOI=10.1242/jcs.214072;\nRA   Torres-Zelada E.F., Stephenson R.E., Alpsoy A., Anderson B.D.,\nRA   Swanson S.K., Florens L., Dykhuizen E.C., Washburn M.P., Weake V.M.;\nRT   \"The Drosophila Dbf4 ortholog Chiffon forms a complex with Gcn5 that is\nRT   necessary for histone acetylation and viability.\";\nRL   J. Cell Sci. 132:0-0(2019).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 172,
  "sequence_version": 2,
  "sequence_comparison": "matched"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9W2I4?format=txt&versions=172)

```json
{
  "evidence_id": "H7",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q9W2I4?format=txt&versions=172",
  "source_sha256": "9cdab37ca5165bf0ed7c572bc5323ec3cdbf7ef551b85431bdf2251f55d4d874",
  "retrieved_utc": "2026-11-02T04:33:50.066048+00:00",
  "source_locator": "lines 118-122",
  "excerpt": "CC   -!- FUNCTION: Component of both the SAGA and CHAT histone acetyltransferase\nCC       complexes, which both predominantly acetylate histone H3.\nCC       {ECO:0000269|PubMed:16980620, ECO:0000269|PubMed:20008933,\nCC       ECO:0000269|PubMed:21764853, ECO:0000269|PubMed:24493646,\nCC       ECO:0000269|PubMed:30559249}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 172,
  "sequence_version": 2,
  "sequence_comparison": "matched"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9W2I4?format=txt&versions=172)

```json
{
  "evidence_id": "H8",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q9W2I4?format=txt&versions=172",
  "source_sha256": "9cdab37ca5165bf0ed7c572bc5323ec3cdbf7ef551b85431bdf2251f55d4d874",
  "retrieved_utc": "2026-11-02T04:33:50.066048+00:00",
  "source_locator": "lines 184-184",
  "excerpt": "DR   GO; GO:0140003; F:histone H3K36me3 reader activity; ISS:FlyBase.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 172,
  "sequence_version": 2,
  "sequence_comparison": "matched"
}
```

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9W2I4?format=txt&versions=172)

```json
{
  "evidence_id": "H9",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q9W2I4?format=txt&versions=172",
  "source_sha256": "9cdab37ca5165bf0ed7c572bc5323ec3cdbf7ef551b85431bdf2251f55d4d874",
  "retrieved_utc": "2026-11-02T04:33:50.066048+00:00",
  "source_locator": "lines 185-185",
  "excerpt": "DR   GO; GO:0140002; F:histone H3K4me3 reader activity; ISS:FlyBase.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 172,
  "sequence_version": 2,
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
  "source_locator": "lines 47806-47847",
  "excerpt": "[Term]\nid: GO:0004707\nname: MAP kinase activity\nnamespace: molecular_function\nalt_id: GO:0008338\nalt_id: GO:0008339\nalt_id: GO:0016908\nalt_id: GO:0016909\ndef: \"Catalysis of the reaction: protein + ATP = protein phosphate + ADP. This reaction is the phosphorylation of proteins. Mitogen-activated protein kinase; a family of protein kinases that perform a crucial step in relaying signals from the plasma membrane to the nucleus. They are activated by a wide range of proliferation- or differentiation-inducing signals; activation is strong with agonists such as polypeptide growth factors and tumor-promoting phorbol esters, but weak (in most cell backgrounds) by stress stimuli.\" [GOC:ma, ISBN:0198547684]\nsynonym: \"ATP:protein phosphotransferase (MAPKK-activated) activity\" RELATED [EC:2.7.11.24]\nsynonym: \"ERK\" RELATED [EC:2.7.11.24]\nsynonym: \"ERK1\" EXACT []\nsynonym: \"ERK2\" RELATED []\nsynonym: \"extracellular signal-regulated kinase activity\" NARROW [EC:2.7.11.24]\nsynonym: \"MAP kinase 1 activity\" NARROW []\nsynonym: \"MAP kinase 2 activity\" NARROW []\nsynonym: \"MAPK\" RELATED [EC:2.7.11.24, PMID:20811974]\nsynonym: \"MBP kinase I activity\" NARROW [EC:2.7.11.24]\nsynonym: \"MBP kinase II activity\" NARROW [EC:2.7.11.24]\nsynonym: \"mitogen activated kinase activity\" EXACT []\nsynonym: \"mitogen-activated protein kinase activity\" RELATED [EC:2.7.11.24]\nsynonym: \"myelin basic protein kinase activity\" NARROW [EC:2.7.11.24]\nsynonym: \"SAP kinase activity\" NARROW []\nsynonym: \"SAPK\" NARROW []\nsynonym: \"stress-activated kinase activity\" NARROW []\nsynonym: \"stress-activated protein kinase activity\" NARROW []\nxref: EC:2.7.11.24\nxref: KEGG_REACTION:R00162\nxref: MetaCyc:2.7.11.24-RXN\nxref: Reactome:R-HSA-111898 \"Phosphorylation of cPLA2 by ERK-2\"\nxref: Reactome:R-HSA-198733 \"ERK5 is activated\"\nxref: Reactome:R-HSA-445079 \"Phosphorylation of L1 by ERK\"\nxref: Reactome:R-HSA-5654560 \"Activated ERK1/2 threonine-phosphorylates FGFR1-associated FRS2\"\nxref: Reactome:R-HSA-5654562 \"Activated ERK1/2 threonine-phosphorylates FGFR2-associated FRS2\"\nxref: Reactome:R-HSA-5654565 \"Activated ERK1/2 threonine-phosphorylates FGFR3-associated FRS2\"\nxref: Reactome:R-HSA-5654566 \"Activated ERK1/2 threonine-phosphorylates FGFR4-associated FRS2\"\nxref: Reactome:R-HSA-73722 \"Phosphorylation of UBF-1:rDNA Promoter\"\nxref: Reactome:R-HSA-9626832 \"MAPK1 or MAPK3 phosphorylates NCF1 at Ser345\"\nxref: Reactome:R-HSA-9825759 \"MAPK-dependent phosphorylation of KARS\"\nis_a: GO:0004674 ! protein serine/threonine kinase activity\nproperty_value: skos:exactMatch EC:2.7.11.24\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "go_id": "GO:0004707"
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
  "source_locator": "lines 49992-50006",
  "excerpt": "[Term]\nid: GO:0004795\nname: threonine synthase activity\nnamespace: molecular_function\ndef: \"Catalysis of the reaction: O-phospho-L-homoserine + H2O = L-threonine + phosphate.\" [EC:4.2.3.1]\nsynonym: \"O-phospho-L-homoserine phospho-lyase (adding water)\" RELATED [EC:4.2.3.1]\nsynonym: \"O-phospho-L-homoserine phospho-lyase (adding water; L-threonine-forming)\" RELATED [EC:4.2.3.1]\nsynonym: \"threonine synthetase activity\" RELATED [EC:4.2.3.1]\nxref: EC:4.2.3.1\nxref: MetaCyc:THRESYN-RXN\nxref: RHEA:10840\nis_a: GO:0016838 ! carbon-oxygen lyase activity, acting on phosphates\nproperty_value: skos:exactMatch EC:4.2.3.1\nproperty_value: skos:exactMatch RHEA:10840\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "go_id": "GO:0004795"
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
  "source_locator": "lines 57197-57203",
  "excerpt": "[Term]\nid: GO:0005544\nname: calcium-dependent phospholipid binding\nnamespace: molecular_function\ndef: \"Binding to a phospholipid, a class of lipids containing phosphoric acid as a mono- or diester, in the presence of calcium.\" [GOC:jl]\nis_a: GO:0005543 ! phospholipid binding\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "go_id": "GO:0005544"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 190. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
