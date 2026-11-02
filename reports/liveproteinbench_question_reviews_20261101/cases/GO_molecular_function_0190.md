# GO_molecular_function_0190

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_molecular_function`  
**Author expected answer:** **D** — methylated histone binding

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

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
<summary>Original system instructions, verbatim</summary>

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

## GPT-6 Luna

**Saved status:** `valid_review`.

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

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

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

## Existing project source checks of Luna’s review

The notes below were prepared for specific claims in the Luna review. They are not independent validation of Qwen’s claims, expert adjudication, or replacement verdicts.

## Project source-check notes

These project-authored, AI-assisted checks assess specific source claims. They are not expert adjudication and do not replace Luna’s saved review or the author key.

No additional case-specific project note was recorded. Citation membership checks do not establish that every scientific argument is correct.

## Reviewer-only source evidence

**Both reviewers received this source evidence separately from the original question. It was not available to the original evaluated model.** Source support and reasoning from the original sequence/choices are distinct assessments.

**Accession:** `Q9W2I4` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 172. Exact author snapshot unknown.

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
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:46.947791+00:00.  

```json
"Q9W2I4"
```

Source SHA-256: `99e79ffdf07452f0c2ae6b5b82b60c28b7ea2d0331542973f4e028462aab9481`.

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9W2I4.json)  
**Locator:** `/entryAudit`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:46.947791+00:00.  

```json
{"entryVersion":174,"firstPublicDate":"2025-06-18","lastAnnotationUpdateDate":"2026-09-02","lastSequenceUpdateDate":"2002-10-01","sequenceVersion":2}
```

Source SHA-256: `99e79ffdf07452f0c2ae6b5b82b60c28b7ea2d0331542973f4e028462aab9481`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9W2I4.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:46.947791+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"SAGA complex subunit Sgf29"}}],"recommendedName":{"fullName":{"evidences":[{"evidenceCode":"ECO:0000312","id":"FBgn0050390","source":"FlyBase"}],"value":"SAGA-associated factor 29kDa"}}}
```

Source SHA-256: `99e79ffdf07452f0c2ae6b5b82b60c28b7ea2d0331542973f4e028462aab9481`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9W2I4.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:46.947791+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"16980620","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"20008933","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"21764853","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"24493646","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"30559249","source":"PubMed"}],"value":"Component of both the SAGA and CHAT histone acetyltransferase complexes, which both predominantly acetylate histone H3"}]}
```

Source SHA-256: `99e79ffdf07452f0c2ae6b5b82b60c28b7ea2d0331542973f4e028462aab9481`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9W2I4.json)  
**Locator:** `/uniProtKBCrossReferences/41`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:46.947791+00:00.  

```json
{"database":"GO","id":"GO:0140003","properties":[{"key":"GoTerm","value":"F:histone H3K36me3 reader activity"},{"key":"GoEvidenceType","value":"ISS:FlyBase"}]}
```

Source SHA-256: `99e79ffdf07452f0c2ae6b5b82b60c28b7ea2d0331542973f4e028462aab9481`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9W2I4.json)  
**Locator:** `/uniProtKBCrossReferences/42`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:46.947791+00:00.  

```json
{"database":"GO","id":"GO:0140002","properties":[{"key":"GoTerm","value":"F:histone H3K4me3 reader activity"},{"key":"GoEvidenceType","value":"ISS:FlyBase"}]}
```

Source SHA-256: `99e79ffdf07452f0c2ae6b5b82b60c28b7ea2d0331542973f4e028462aab9481`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9W2I4?format=txt&versions=172)  
**Locator:** `lines 82-90`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 172 / 2.  
**Retrieved:** 2026-11-02T04:33:50.066048+00:00.  

```text
RN   [5] {ECO:0000305}
RP   FUNCTION, IDENTIFICATION IN SAGA COMPLEX, SUBCELLULAR LOCATION, AND
RP   IDENTIFICATION BY MASS SPECTROMETRY.
RX   PubMed=20008933; DOI=10.1101/gad.1846409;
RA   Weake V.M., Swanson S.K., Mushegian A., Florens L., Washburn M.P.,
RA   Abmayr S.M., Workman J.L.;
RT   "A novel histone fold domain-containing protein that replaces TAF6 in
RT   Drosophila SAGA is required for SAGA-dependent gene expression.";
RL   Genes Dev. 23:2818-2823(2009).
```

Source SHA-256: `9cdab37ca5165bf0ed7c572bc5323ec3cdbf7ef551b85431bdf2251f55d4d874`.

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9W2I4?format=txt&versions=172)  
**Locator:** `lines 118-122`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 172 / 2.  
**Retrieved:** 2026-11-02T04:33:50.066048+00:00.  

```text
CC   -!- FUNCTION: Component of both the SAGA and CHAT histone acetyltransferase
CC       complexes, which both predominantly acetylate histone H3.
CC       {ECO:0000269|PubMed:16980620, ECO:0000269|PubMed:20008933,
CC       ECO:0000269|PubMed:21764853, ECO:0000269|PubMed:24493646,
CC       ECO:0000269|PubMed:30559249}.
```

Source SHA-256: `9cdab37ca5165bf0ed7c572bc5323ec3cdbf7ef551b85431bdf2251f55d4d874`.

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9W2I4?format=txt&versions=172)  
**Locator:** `lines 184-184`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 172 / 2.  
**Retrieved:** 2026-11-02T04:33:50.066048+00:00.  

```text
DR   GO; GO:0140003; F:histone H3K36me3 reader activity; ISS:FlyBase.
```

Source SHA-256: `9cdab37ca5165bf0ed7c572bc5323ec3cdbf7ef551b85431bdf2251f55d4d874`.

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9W2I4?format=txt&versions=172)  
**Locator:** `lines 185-185`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 172 / 2.  
**Retrieved:** 2026-11-02T04:33:50.066048+00:00.  

```text
DR   GO; GO:0140002; F:histone H3K4me3 reader activity; ISS:FlyBase.
```

Source SHA-256: `9cdab37ca5165bf0ed7c572bc5323ec3cdbf7ef551b85431bdf2251f55d4d874`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 190. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
