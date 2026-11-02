# cofactor_0034

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `cofactor`  
**Author expected answer:** **B** — FMN

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | invalid_review |

**Paired comparison:** not comparable: one or both reviews invalid or missing. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MTSSEPASPEIEQQANSAPRRPRILLAASGSVAAIKFGNLCHSFSEWAEVKAVATRASLHFIDRASLPKDVILYTEEDEWSTWNKVGDSVLHIELRSWADILVIAPLSANTLGKIAGGLCDNLLTCIVRAWDYSKPFFVAPAMNTLMWKNPFTEQHIMSIDELGVSLIPPVTKRLACGDYGNGAMAEPSVIYSTVRLFFESRVQQSGNIVQQPV

[Multiple Choices]
A. FAD
B. FMN
C. Mg(2+)
D. [2Fe-2S] cluster
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Predicting Protein Cofactor, which is to identify the specific cofactor required for a given protein's catalytic activity. A cofactor is a non-protein chemical compound or metallic ion that is essential for an enzyme's function. Based on the provided protein sequence, you will need to determine which of the multiple-choice options is the correct cofactor.. The inputs provided by the user for this task include:

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

> The supplied sequence exactly matches the UniProt entry annotated as a phosphopantothenoylcysteine decarboxylase, and that entry annotates one FMN per subunit. The cofactor annotation is transferred by similarity (ECO:0000250), so it supports FMN but is not direct experimental evidence for this exact protein in the excerpts.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence is the only supplied biological input; it does not state the protein's function or cofactor. Identifying the specific FMN-dependent enzyme family would require protein-specific sequence annotation or prior knowledge.


**Missing item-specific fact**

> The connection between this sequence and HAL3/PPCDC, together with the family cofactor annotation that it binds FMN.


**Reason**

> The reviewer-only annotation supports the key, but that annotation was not available to the evaluated model. Inferring a specific cofactor from the raw sequence alone would depend on recognizing or looking up this protein or its family.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The matched sequence's entry specifies FMN; the evidence does not support another listed option.


### Important caveats

- The FMN evidence is transferred by similarity from UniProtKB:Q9SWE5, not shown here as a direct experimental measurement of this apple protein.
- The exact sequence match establishes applicability of the annotation to the supplied sequence, but the author's source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is the only supplied biological input; it does not state the protein's function or cofactor. Identifying the specific FMN-dependent enzyme family would require protein-specific sequence annotation or prior knowledge.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The connection between this sequence and HAL3/PPCDC, together with the family cofactor annotation that it binds FMN.",
    "reason": "The reviewer-only annotation supports the key, but that annotation was not available to the evaluated model. Inferring a specific cofactor from the raw sequence alone would depend on recognizing or looking up this protein or its family."
  },
  "case_id": "cofactor_0034",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the UniProt entry annotated as a phosphopantothenoylcysteine decarboxylase, and that entry annotates one FMN per subunit. The cofactor annotation is transferred by similarity (ECO:0000250), so it supports FMN but is not direct experimental evidence for this exact protein in the excerpts."
  },
  "important_caveats": [
    "The FMN evidence is transferred by similarity from UniProtKB:Q9SWE5, not shown here as a direct experimental measurement of this apple protein.",
    "The exact sequence match establishes applicability of the annotation to the supplied sequence, but the author's source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched sequence's entry specifies FMN; the evidence does not support another listed option."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "cofactor_0034",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the UniProt entry annotated as a phosphopantothenoylcysteine decarboxylase, and that entry annotates one FMN per subunit. The cofactor annotation is transferred by similarity (ECO:0000250), so it supports FMN but is not direct experimental evidence for this exact protein in the excerpts.",
    "evidence_ids": ["C1", "C4", "C5", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence is the only supplied biological input; it does not state the protein's function or cofactor. Identifying the specific FMN-dependent enzyme family would require protein-specific sequence annotation or prior knowledge.",
    "missing_item_specific_fact": "The connection between this sequence and HAL3/PPCDC, together with the family cofactor annotation that it binds FMN.",
    "reason": "The reviewer-only annotation supports the key, but that annotation was not available to the evaluated model. Inferring a specific cofactor from the raw sequence alone would depend on recognizing or looking up this protein or its family."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched sequence's entry specifies FMN; the evidence does not support another listed option."
  },
  "important_caveats": [
    "The FMN evidence is transferred by similarity from UniProtKB:Q9SWE5, not shown here as a direct experimental measurement of this apple protein.",
    "The exact sequence match establishes applicability of the annotation to the supplied sequence, but the author's source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `invalid_review`.

**This result is not a valid structured review.** Any saved labels below remain the model’s original values; they are excluded from label distributions and paired agreement. No field or option ID has been repaired.

**Validation errors:** `question_ambiguity:invalid_option_ids`.

### Expected-answer support: supported

> The UniProt entry A0A498JQK2 (HAL3_MALDO, phosphopantothenoylcysteine decarboxylase, EC 4.1.1.36) explicitly annotates FMN as the cofactor (C5, H4). The cofactor annotation carries evidence code ECO:0000250 (inferred from similarity to Q9SWE5), but the enzymatic identity (EC 4.1.1.36) is experimentally supported (ECO:0000269, PubMed:32761275). Phosphopantothenoylcysteine decarboxylase is a well-characterized FMN-dependent enzyme in the coenzyme A biosynthesis pathway, making FMN the established cofactor for this enzyme class. The answer is scientifically sound.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4), [C4](#evidence-c4), [H2](#evidence-h2), [C6](#evidence-c6).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The N-terminal Rossmann-like motif (ASGSVAAI) suggests a flavin-binding protein, which could eliminate Mg2+ (C) and &#91;2Fe-2S&#93; (D) as implausible for a flavoprotein. However, distinguishing FMN (B) from FAD (A) based on sequence alone is extremely difficult: both are flavins recognized by Rossmann folds, and the motif 'GSVAAI' is too generic to specify which flavin is bound. The critical step—identifying this 214-aa sequence as a phosphopantothenoylcysteine decarboxylase (CDC/PPCDC) whose FMN dependence is textbook biochemistry—requires recognizing the specific protein family from the sequence, which is effectively a database lookup or memorization of the CDC domain architecture. Without that identification, the FMN-vs-FAD choice cannot be resolved from general sequence features.


**Missing item-specific fact**

> The identification of this specific 214-aa sequence as a member of the phosphopantothenoylcysteine decarboxylase (CDC/PPCDC) family, and the knowledge that CDC specifically binds FMN (not FAD) as its flavin cofactor. This enzyme-class-specific cofactor assignment is not derivable from generic flavoprotein sequence motifs.


**Reason**

> While the CDC-FMN relationship is well-established biochemistry, the question requires first recognizing the raw sequence as CDC. The Rossmann fold motif is shared by FAD- and FMN-binding proteins alike, and the 214-aa length alone does not uniquely specify CDC. The FMN-vs-FAD distinction for this enzyme is an item-specific fact about the CDC enzyme class, not a generalizable sequence heuristic. A model must either identify the protein via sequence matching (lookup) or have memorized the CDC family's cofactor preference.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A (FAD)",
  "B (FMN)"
]
```

> Both FAD and FMN are flavin cofactors recognized by Rossmann-type folds. The sequence contains a generic dinucleotide/flavin-binding motif (GSVAAI) that does not distinguish FMN from FAD. Without prior identification of the protein as CDC, a knowledgeable model could reasonably consider FAD as a plausible flavin cofactor. Mg2+ and &#91;2Fe-2S&#93; are clearly weaker distractors for a flavoprotein-like sequence, but the FMN/FAD pair is genuinely ambiguous from sequence alone.


### Important caveats

- The FMN cofactor annotation for A0A498JQK2 is transferred by similarity (ECO:0000250) from Q9SWE5, not directly experimentally measured for this specific apple HAL3 protein. However, the EC assignment (4.1.1.36) is experimentally supported, and the FMN dependence of CDC enzymes is well-established in the literature.
- The protein identity (HAL3/PPCDC) and its FMN dependence are reviewer-only annotations absent from the model input. The model receives only the raw 214-aa sequence and four cofactor choices.
- The sequence match is confirmed (SHA-256 match to both current and historical UniProt entries), so the annotation applies to the exact sequence provided.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal Rossmann-like motif (ASGSVAAI) suggests a flavin-binding protein, which could eliminate Mg2+ (C) and [2Fe-2S] (D) as implausible for a flavoprotein. However, distinguishing FMN (B) from FAD (A) based on sequence alone is extremely difficult: both are flavins recognized by Rossmann folds, and the motif 'GSVAAI' is too generic to specify which flavin is bound. The critical step—identifying this 214-aa sequence as a phosphopantothenoylcysteine decarboxylase (CDC/PPCDC) whose FMN dependence is textbook biochemistry—requires recognizing the specific protein family from the sequence, which is effectively a database lookup or memorization of the CDC domain architecture. Without that identification, the FMN-vs-FAD choice cannot be resolved from general sequence features.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The identification of this specific 214-aa sequence as a member of the phosphopantothenoylcysteine decarboxylase (CDC/PPCDC) family, and the knowledge that CDC specifically binds FMN (not FAD) as its flavin cofactor. This enzyme-class-specific cofactor assignment is not derivable from generic flavoprotein sequence motifs.",
    "reason": "While the CDC-FMN relationship is well-established biochemistry, the question requires first recognizing the raw sequence as CDC. The Rossmann fold motif is shared by FAD- and FMN-binding proteins alike, and the 214-aa length alone does not uniquely specify CDC. The FMN-vs-FAD distinction for this enzyme is an item-specific fact about the CDC enzyme class, not a generalizable sequence heuristic. A model must either identify the protein via sequence matching (lookup) or have memorized the CDC family's cofactor preference."
  },
  "case_id": "cofactor_0034",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4",
      "C4",
      "H2",
      "C6"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry A0A498JQK2 (HAL3_MALDO, phosphopantothenoylcysteine decarboxylase, EC 4.1.1.36) explicitly annotates FMN as the cofactor (C5, H4). The cofactor annotation carries evidence code ECO:0000250 (inferred from similarity to Q9SWE5), but the enzymatic identity (EC 4.1.1.36) is experimentally supported (ECO:0000269, PubMed:32761275). Phosphopantothenoylcysteine decarboxylase is a well-characterized FMN-dependent enzyme in the coenzyme A biosynthesis pathway, making FMN the established cofactor for this enzyme class. The answer is scientifically sound."
  },
  "important_caveats": [
    "The FMN cofactor annotation for A0A498JQK2 is transferred by similarity (ECO:0000250) from Q9SWE5, not directly experimentally measured for this specific apple HAL3 protein. However, the EC assignment (4.1.1.36) is experimentally supported, and the FMN dependence of CDC enzymes is well-established in the literature.",
    "The protein identity (HAL3/PPCDC) and its FMN dependence are reviewer-only annotations absent from the model input. The model receives only the raw 214-aa sequence and four cofactor choices.",
    "The sequence match is confirmed (SHA-256 match to both current and historical UniProt entries), so the annotation applies to the exact sequence provided."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A (FAD)",
      "B (FMN)"
    ],
    "reason": "Both FAD and FMN are flavin cofactors recognized by Rossmann-type folds. The sequence contains a generic dinucleotide/flavin-binding motif (GSVAAI) that does not distinguish FMN from FAD. Without prior identification of the protein as CDC, a knowledgeable model could reasonably consider FAD as a plausible flavin cofactor. Mg2+ and [2Fe-2S] are clearly weaker distractors for a flavoprotein-like sequence, but the FMN/FAD pair is genuinely ambiguous from sequence alone."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "cofactor_0034",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A0A498JQK2 (HAL3_MALDO, phosphopantothenoylcysteine decarboxylase, EC 4.1.1.36) explicitly annotates FMN as the cofactor (C5, H4). The cofactor annotation carries evidence code ECO:0000250 (inferred from similarity to Q9SWE5), but the enzymatic identity (EC 4.1.1.36) is experimentally supported (ECO:0000269, PubMed:32761275). Phosphopantothenoylcysteine decarboxylase is a well-characterized FMN-dependent enzyme in the coenzyme A biosynthesis pathway, making FMN the established cofactor for this enzyme class. The answer is scientifically sound.",
    "evidence_ids": ["C5", "H4", "C4", "H2", "C6"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The N-terminal Rossmann-like motif (ASGSVAAI) suggests a flavin-binding protein, which could eliminate Mg2+ (C) and [2Fe-2S] (D) as implausible for a flavoprotein. However, distinguishing FMN (B) from FAD (A) based on sequence alone is extremely difficult: both are flavins recognized by Rossmann folds, and the motif 'GSVAAI' is too generic to specify which flavin is bound. The critical step—identifying this 214-aa sequence as a phosphopantothenoylcysteine decarboxylase (CDC/PPCDC) whose FMN dependence is textbook biochemistry—requires recognizing the specific protein family from the sequence, which is effectively a database lookup or memorization of the CDC domain architecture. Without that identification, the FMN-vs-FAD choice cannot be resolved from general sequence features.",
    "missing_item_specific_fact": "The identification of this specific 214-aa sequence as a member of the phosphopantothenoylcysteine decarboxylase (CDC/PPCDC) family, and the knowledge that CDC specifically binds FMN (not FAD) as its flavin cofactor. This enzyme-class-specific cofactor assignment is not derivable from generic flavoprotein sequence motifs.",
    "reason": "While the CDC-FMN relationship is well-established biochemistry, the question requires first recognizing the raw sequence as CDC. The Rossmann fold motif is shared by FAD- and FMN-binding proteins alike, and the 214-aa length alone does not uniquely specify CDC. The FMN-vs-FAD distinction for this enzyme is an item-specific fact about the CDC enzyme class, not a generalizable sequence heuristic. A model must either identify the protein via sequence matching (lookup) or have memorized the CDC family's cofactor preference."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A (FAD)", "B (FMN)"],
    "reason": "Both FAD and FMN are flavin cofactors recognized by Rossmann-type folds. The sequence contains a generic dinucleotide/flavin-binding motif (GSVAAI) that does not distinguish FMN from FAD. Without prior identification of the protein as CDC, a knowledgeable model could reasonably consider FAD as a plausible flavin cofactor. Mg2+ and [2Fe-2S] are clearly weaker distractors for a flavoprotein-like sequence, but the FMN/FAD pair is genuinely ambiguous from sequence alone."
  },
  "important_caveats": [
    "The FMN cofactor annotation for A0A498JQK2 is transferred by similarity (ECO:0000250) from Q9SWE5, not directly experimentally measured for this specific apple HAL3 protein. However, the EC assignment (4.1.1.36) is experimentally supported, and the FMN dependence of CDC enzymes is well-established in the literature.",
    "The protein identity (HAL3/PPCDC) and its FMN dependence are reviewer-only annotations absent from the model input. The model receives only the raw 214-aa sequence and four cofactor choices.",
    "The sequence match is confirmed (SHA-256 match to both current and historical UniProt entries), so the annotation applies to the exact sequence provided."
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

**Accession:** `A0A498JQK2` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 19. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A498JQK2.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:46.295142+00:00.  

```json
"A0A498JQK2"
```

Source SHA-256: `2c9613d7efc5e321099105e7df8e04bdd2092654fa07c37207bdc79f66b8d3b2`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A498JQK2.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:46.295142+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"32761275","source":"PubMed"}],"value":"Halotolerance protein 3"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"32761275","source":"PubMed"}],"value":"MdHAL3"}]}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"32761275","source":"PubMed"}],"value":"4.1.1.36"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Phosphopantothenoylcysteine decarboxylase HAL3"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"32761275","source":"PubMed"}],"value":"PPCDC"}]}}
```

Source SHA-256: `2c9613d7efc5e321099105e7df8e04bdd2092654fa07c37207bdc79f66b8d3b2`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A498JQK2.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:46.295142+00:00.  

```json
{"cofactors":[{"cofactorCrossReference":{"database":"ChEBI","id":"CHEBI:58210"},"evidences":[{"evidenceCode":"ECO:0000250","id":"Q9SWE5","source":"UniProtKB"}],"name":"FMN"}],"commentType":"COFACTOR","note":{"texts":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q9SWE5","source":"UniProtKB"}],"value":"Binds 1 FMN per subunit."}]}}
```

Source SHA-256: `2c9613d7efc5e321099105e7df8e04bdd2092654fa07c37207bdc79f66b8d3b2`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A498JQK2.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:46.295142+00:00.  

```json
{"citation":{"authors":["Yang S.","Zhang F.","Wang Y.","Xue H.","Jiang Q.","Shi J.","Dai H.","Zhang Z.","Li L.","He P.","Li Y.","Ma Y."],"citationCrossReferences":[{"database":"PubMed","id":"32761275"},{"database":"DOI","id":"10.1007/s00299-020-02576-2"}],"citationType":"journal article","firstPage":"1479","id":"32761275","journal":"Plant Cell Rep.","lastPage":"1491","publicationDate":"2020","title":"MdHAL3, a 4'-phosphopantothenoylcysteine decarboxylase, is involved in the salt tolerance of autotetraploid apple.","volume":"39"},"referenceComments":[{"type":"STRAIN","value":"cv. GL-3"},{"type":"STRAIN","value":"cv. Hanfu"}],"referenceNumber":2,"referencePositions":["FUNCTION","DISRUPTION PHENOTYPE","CATALYTIC ACTIVITY","TISSUE SPECIFICITY","INDUCTION BY SALT STRESS","SUBCELLULAR LOCATION"]}
```

Source SHA-256: `2c9613d7efc5e321099105e7df8e04bdd2092654fa07c37207bdc79f66b8d3b2`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A498JQK2?format=txt&versions=19)  
**Locator:** `lines 6-10`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 19 / 1.  
**Retrieved:** 2026-11-01T06:27:31.570388+00:00.  

```text
DE   RecName: Full=Phosphopantothenoylcysteine decarboxylase HAL3 {ECO:0000305};
DE            Short=PPCDC {ECO:0000303|PubMed:32761275};
DE            EC=4.1.1.36 {ECO:0000269|PubMed:32761275};
DE   AltName: Full=Halotolerance protein 3 {ECO:0000303|PubMed:32761275};
DE            Short=MdHAL3 {ECO:0000303|PubMed:32761275};
```

Source SHA-256: `0d82d450cb21391ae574aa004d536baec6b477d61421e803b284844ec1434bbd`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A498JQK2?format=txt&versions=19)  
**Locator:** `lines 51-54`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 19 / 1.  
**Retrieved:** 2026-11-01T06:27:31.570388+00:00.  

```text
CC   -!- COFACTOR:
CC       Name=FMN; Xref=ChEBI:CHEBI:58210;
CC         Evidence={ECO:0000250|UniProtKB:Q9SWE5};
CC       Note=Binds 1 FMN per subunit. {ECO:0000250|UniProtKB:Q9SWE5};
```

Source SHA-256: `0d82d450cb21391ae574aa004d536baec6b477d61421e803b284844ec1434bbd`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/cofactor.json), zero-based source row 34. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
