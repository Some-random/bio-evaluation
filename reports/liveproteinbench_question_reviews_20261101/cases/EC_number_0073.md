# EC_number_0073

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `EC_number`  
**Author expected answer:** **C** — 4.1.1.36

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MAGSEPVSAEGESMAVDAAPRKPRILLAASGSVAAVKFANLCHCFSEWADVRAVSSSGSLHFIDRASMPKDVILYTDEDEWSSWKKLGDSVLHIELRKWADIMVIAPLSANTLGKIAGGLCDNLLTCIVRAWDYSKPFFVAPAMNTLMWNNPFTERHFISIDELGISLIPPVTKRLACGDYGNGAMAEPSTIYSTVRLFYESKAQQGRAVVTLR

[Multiple Choices]
A. 4.1.1.128
B. 1.14.14.187
C. 4.1.1.36
D. 1.1.1.136
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Enzyme Commission (EC) Number Prediction, which is to predict the complete 4-digit Enzyme Commission (EC) number for a given protein. The EC number is a numerical classification that categorizes enzymes based on the chemical reactions they catalyze. You should select the most accurate EC number from the provided options based on the protein's sequence.. The inputs provided by the user for this task include:

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

> The supplied sequence exactly matches the UniProt entry for soybean HAL3b, annotated as phosphopantothenoylcysteine decarboxylase with EC 4.1.1.36. The annotation and catalytic reaction are transferred by similarity from UniProtKB Q9SWE5, so they support the key but are not direct experimental evidence for this sequence.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence is a protein sequence, but the input supplies no organism, function, reaction, or explicit family annotation that distinguishes this particular decarboxylase from the other listed enzyme classes.


**Missing item-specific fact**

> Identifying this sequence as HAL3b/PPCDC, or having an equivalent family-specific homology or annotation result, is needed to select EC 4.1.1.36.


**Reason**

> The key is supported by a sequence-matched database annotation, but that annotation is not provided in the question. Recognizing the specific protein or relying on an external family/database identification is lookup or memorization, not a concrete argument available from the prompt alone.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The sequence-matched annotation assigns EC 4.1.1.36; the evidence provided does not support another listed option.


### Important caveats

- The EC assignment is supported by similarity evidence from Q9SWE5 rather than direct experimental evidence for the supplied soybean sequence.
- The reviewer-only sequence match and database annotation were not available to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is a protein sequence, but the input supplies no organism, function, reaction, or explicit family annotation that distinguishes this particular decarboxylase from the other listed enzyme classes.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "Identifying this sequence as HAL3b/PPCDC, or having an equivalent family-specific homology or annotation result, is needed to select EC 4.1.1.36.",
    "reason": "The key is supported by a sequence-matched database annotation, but that annotation is not provided in the question. Recognizing the specific protein or relying on an external family/database identification is lookup or memorization, not a concrete argument available from the prompt alone."
  },
  "case_id": "EC_number_0073",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H2",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the UniProt entry for soybean HAL3b, annotated as phosphopantothenoylcysteine decarboxylase with EC 4.1.1.36. The annotation and catalytic reaction are transferred by similarity from UniProtKB Q9SWE5, so they support the key but are not direct experimental evidence for this sequence."
  },
  "important_caveats": [
    "The EC assignment is supported by similarity evidence from Q9SWE5 rather than direct experimental evidence for the supplied soybean sequence.",
    "The reviewer-only sequence match and database annotation were not available to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence-matched annotation assigns EC 4.1.1.36; the evidence provided does not support another listed option."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0073",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the UniProt entry for soybean HAL3b, annotated as phosphopantothenoylcysteine decarboxylase with EC 4.1.1.36. The annotation and catalytic reaction are transferred by similarity from UniProtKB Q9SWE5, so they support the key but are not direct experimental evidence for this sequence.",
    "evidence_ids": ["C1", "C4", "C5", "H2", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence is a protein sequence, but the input supplies no organism, function, reaction, or explicit family annotation that distinguishes this particular decarboxylase from the other listed enzyme classes.",
    "missing_item_specific_fact": "Identifying this sequence as HAL3b/PPCDC, or having an equivalent family-specific homology or annotation result, is needed to select EC 4.1.1.36.",
    "reason": "The key is supported by a sequence-matched database annotation, but that annotation is not provided in the question. Recognizing the specific protein or relying on an external family/database identification is lookup or memorization, not a concrete argument available from the prompt alone."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence-matched annotation assigns EC 4.1.1.36; the evidence provided does not support another listed option."
  },
  "important_caveats": [
    "The EC assignment is supported by similarity evidence from Q9SWE5 rather than direct experimental evidence for the supplied soybean sequence.",
    "The reviewer-only sequence match and database annotation were not available to the evaluated model."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry C6TA59 (HAL3B_SOYBN) annotates this 214-aa soybean protein as Phosphopantothenoylcysteine decarboxylase (PPCDC) with EC 4.1.1.36. The catalytic reaction (N-&#91;(R)-4-phosphopantothenoyl&#93;-L-cysteine + H(+) → (R)-4'-phosphopantetheine + CO2) is consistent with a carboxy-lyase. The sequence matches the UniProt entry exactly (SHA256 confirmed). However, the EC assignment carries evidence code ECO:0000250 (inferred by similarity from Q9SWE5, the yeast PPCDC), so it is a computational/similarity transfer rather than direct experimental characterization of the soybean protein itself. The annotation is nonetheless well-supported within the PPCDC enzyme family.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence contains a conserved 'GDYG' motif (in the segment 'ACGDYGNGAMAEPSTIYSTVRLFYESKAQQGRAVVTLR') and is ~214 aa in length, features associated with PPCDC enzymes. One could eliminate choices B (1.14.14.187, a monooxygenase) and D (1.1.1.136, a dehydrogenase) by noting the absence of typical oxidoreductase motifs (Rossmann NAD-binding fold, heme-binding Cys-His residues, etc.). However, the critical distinction between choice A (4.1.1.128, a different carboxy-lyase) and choice C (4.1.1.36, PPCDC) both fall in EC sub-subclass 4.1.1 (carboxy-lyases). No general biological reasoning from the raw sequence alone can determine which specific carboxy-lyase substrate (phosphopantothenoylcysteine vs. the substrate of EC 4.1.1.128) this enzyme acts upon. Recognizing the 'GDYG' motif as specifically diagnostic of PPCDC rather than another decarboxylase constitutes protein-family-specific memorization, not general biochemical reasoning.


**Missing item-specific fact**

> The specific substrate identity and active-site architecture that distinguishes EC 4.1.1.36 (PPCDC, acting on phosphopantothenoylcysteine) from EC 4.1.1.128 (a different carboxy-lyase) cannot be inferred from the sequence without prior knowledge of the PPCDC enzyme family or database lookup.


**Reason**

> While the broad enzyme class (lyase vs. oxidoreductase) might be partially inferable from the absence of oxidoreductase cofactor-binding motifs, the decisive distinction between two carboxy-lyases in the same EC sub-subclass (4.1.1.36 vs 4.1.1.128) requires recognizing a protein-family-specific motif ('GDYG') and knowing its exact enzymatic assignment. This is effectively memorizing the database entry for this protein rather than reasoning from general biochemistry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "C"
]
```

> Both A (4.1.1.128) and C (4.1.1.36) belong to EC sub-subclass 4.1.1 (carboxy-lyases/decarboxylases). From the sequence alone, without specific PPCDC-family knowledge, a solver cannot confidently distinguish which carboxy-lyase this is. Choices B and D (oxidoreductases) are clearly different classes and are unlikely to be confused with the correct answer by a knowledgeable model.


### Important caveats

- The EC annotation for C6TA59 is based on similarity transfer (ECO:0000250) from the yeast PPCDC (Q9SWE5), not direct experimental characterization of the soybean HAL3b protein.
- The UniProt entry was first released in 2025-04-09; the author's source snapshot date is unknown, though the sequence has been stable since 2009.
- The 'GDYG' motif is a recognizable PPCDC signature for trained models, but this constitutes family-specific pattern recognition rather than general biochemical reasoning.
- EC 4.1.1.128 is a relatively obscure carboxy-lyase; its presence as a distractor tests whether the model can pinpoint the exact substrate specificity rather than just the broad enzyme class.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a conserved 'GDYG' motif (in the segment 'ACGDYGNGAMAEPSTIYSTVRLFYESKAQQGRAVVTLR') and is ~214 aa in length, features associated with PPCDC enzymes. One could eliminate choices B (1.14.14.187, a monooxygenase) and D (1.1.1.136, a dehydrogenase) by noting the absence of typical oxidoreductase motifs (Rossmann NAD-binding fold, heme-binding Cys-His residues, etc.). However, the critical distinction between choice A (4.1.1.128, a different carboxy-lyase) and choice C (4.1.1.36, PPCDC) both fall in EC sub-subclass 4.1.1 (carboxy-lyases). No general biological reasoning from the raw sequence alone can determine which specific carboxy-lyase substrate (phosphopantothenoylcysteine vs. the substrate of EC 4.1.1.128) this enzyme acts upon. Recognizing the 'GDYG' motif as specifically diagnostic of PPCDC rather than another decarboxylase constitutes protein-family-specific memorization, not general biochemical reasoning.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific substrate identity and active-site architecture that distinguishes EC 4.1.1.36 (PPCDC, acting on phosphopantothenoylcysteine) from EC 4.1.1.128 (a different carboxy-lyase) cannot be inferred from the sequence without prior knowledge of the PPCDC enzyme family or database lookup.",
    "reason": "While the broad enzyme class (lyase vs. oxidoreductase) might be partially inferable from the absence of oxidoreductase cofactor-binding motifs, the decisive distinction between two carboxy-lyases in the same EC sub-subclass (4.1.1.36 vs 4.1.1.128) requires recognizing a protein-family-specific motif ('GDYG') and knowing its exact enzymatic assignment. This is effectively memorizing the database entry for this protein rather than reasoning from general biochemistry."
  },
  "case_id": "EC_number_0073",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2",
      "H3"
    ],
    "judgment": "supported",
    "reason": "UniProt entry C6TA59 (HAL3B_SOYBN) annotates this 214-aa soybean protein as Phosphopantothenoylcysteine decarboxylase (PPCDC) with EC 4.1.1.36. The catalytic reaction (N-[(R)-4-phosphopantothenoyl]-L-cysteine + H(+) → (R)-4'-phosphopantetheine + CO2) is consistent with a carboxy-lyase. The sequence matches the UniProt entry exactly (SHA256 confirmed). However, the EC assignment carries evidence code ECO:0000250 (inferred by similarity from Q9SWE5, the yeast PPCDC), so it is a computational/similarity transfer rather than direct experimental characterization of the soybean protein itself. The annotation is nonetheless well-supported within the PPCDC enzyme family."
  },
  "important_caveats": [
    "The EC annotation for C6TA59 is based on similarity transfer (ECO:0000250) from the yeast PPCDC (Q9SWE5), not direct experimental characterization of the soybean HAL3b protein.",
    "The UniProt entry was first released in 2025-04-09; the author's source snapshot date is unknown, though the sequence has been stable since 2009.",
    "The 'GDYG' motif is a recognizable PPCDC signature for trained models, but this constitutes family-specific pattern recognition rather than general biochemical reasoning.",
    "EC 4.1.1.128 is a relatively obscure carboxy-lyase; its presence as a distractor tests whether the model can pinpoint the exact substrate specificity rather than just the broad enzyme class."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "C"
    ],
    "reason": "Both A (4.1.1.128) and C (4.1.1.36) belong to EC sub-subclass 4.1.1 (carboxy-lyases/decarboxylases). From the sequence alone, without specific PPCDC-family knowledge, a solver cannot confidently distinguish which carboxy-lyase this is. Choices B and D (oxidoreductases) are clearly different classes and are unlikely to be confused with the correct answer by a knowledgeable model."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0073",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry C6TA59 (HAL3B_SOYBN) annotates this 214-aa soybean protein as Phosphopantothenoylcysteine decarboxylase (PPCDC) with EC 4.1.1.36. The catalytic reaction (N-[(R)-4-phosphopantothenoyl]-L-cysteine + H(+) → (R)-4'-phosphopantetheine + CO2) is consistent with a carboxy-lyase. The sequence matches the UniProt entry exactly (SHA256 confirmed). However, the EC assignment carries evidence code ECO:0000250 (inferred by similarity from Q9SWE5, the yeast PPCDC), so it is a computational/similarity transfer rather than direct experimental characterization of the soybean protein itself. The annotation is nonetheless well-supported within the PPCDC enzyme family.",
    "evidence_ids": ["C4", "C5", "H2", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence contains a conserved 'GDYG' motif (in the segment 'ACGDYGNGAMAEPSTIYSTVRLFYESKAQQGRAVVTLR') and is ~214 aa in length, features associated with PPCDC enzymes. One could eliminate choices B (1.14.14.187, a monooxygenase) and D (1.1.1.136, a dehydrogenase) by noting the absence of typical oxidoreductase motifs (Rossmann NAD-binding fold, heme-binding Cys-His residues, etc.). However, the critical distinction between choice A (4.1.1.128, a different carboxy-lyase) and choice C (4.1.1.36, PPCDC) both fall in EC sub-subclass 4.1.1 (carboxy-lyases). No general biological reasoning from the raw sequence alone can determine which specific carboxy-lyase substrate (phosphopantothenoylcysteine vs. the substrate of EC 4.1.1.128) this enzyme acts upon. Recognizing the 'GDYG' motif as specifically diagnostic of PPCDC rather than another decarboxylase constitutes protein-family-specific memorization, not general biochemical reasoning.",
    "missing_item_specific_fact": "The specific substrate identity and active-site architecture that distinguishes EC 4.1.1.36 (PPCDC, acting on phosphopantothenoylcysteine) from EC 4.1.1.128 (a different carboxy-lyase) cannot be inferred from the sequence without prior knowledge of the PPCDC enzyme family or database lookup.",
    "reason": "While the broad enzyme class (lyase vs. oxidoreductase) might be partially inferable from the absence of oxidoreductase cofactor-binding motifs, the decisive distinction between two carboxy-lyases in the same EC sub-subclass (4.1.1.36 vs 4.1.1.128) requires recognizing a protein-family-specific motif ('GDYG') and knowing its exact enzymatic assignment. This is effectively memorizing the database entry for this protein rather than reasoning from general biochemistry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "C"],
    "reason": "Both A (4.1.1.128) and C (4.1.1.36) belong to EC sub-subclass 4.1.1 (carboxy-lyases/decarboxylases). From the sequence alone, without specific PPCDC-family knowledge, a solver cannot confidently distinguish which carboxy-lyase this is. Choices B and D (oxidoreductases) are clearly different classes and are unlikely to be confused with the correct answer by a knowledgeable model."
  },
  "important_caveats": [
    "The EC annotation for C6TA59 is based on similarity transfer (ECO:0000250) from the yeast PPCDC (Q9SWE5), not direct experimental characterization of the soybean HAL3b protein.",
    "The UniProt entry was first released in 2025-04-09; the author's source snapshot date is unknown, though the sequence has been stable since 2009.",
    "The 'GDYG' motif is a recognizable PPCDC signature for trained models, but this constitutes family-specific pattern recognition rather than general biochemical reasoning.",
    "EC 4.1.1.128 is a relatively obscure carboxy-lyase; its presence as a distractor tests whether the model can pinpoint the exact substrate specificity rather than just the broad enzyme class."
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

**Accession:** `C6TA59` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 84. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C6TA59.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:35.244012+00:00.  

```json
"C6TA59"
```

Source SHA-256: `4f24a50395840d689b2bca6503bac71363002becd9e9b0e170ac85361993f2a0`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C6TA59.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:35.244012+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"Ref.3","source":"Reference"},{"evidenceCode":"ECO:0000303","id":"Ref.4","source":"Reference"}],"value":"Halotolerance protein 3b"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"Ref.3","source":"Reference"},{"evidenceCode":"ECO:0000303","id":"Ref.4","source":"Reference"}],"value":"GmHAL3b"}]}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q9SWE5","source":"UniProtKB"}],"value":"4.1.1.36"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Phosphopantothenoylcysteine decarboxylase HAL3b"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"PPCDC"}]}}
```

Source SHA-256: `4f24a50395840d689b2bca6503bac71363002becd9e9b0e170ac85361993f2a0`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C6TA59.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:35.244012+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000250","id":"Q9SWE5","source":"UniProtKB"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:16794"}}],"reaction":{"ecNumber":"4.1.1.36","evidences":[{"evidenceCode":"ECO:0000250","id":"Q9SWE5","source":"UniProtKB"}],"name":"N-[(R)-4-phosphopantothenoyl]-L-cysteine + H(+) = (R)-4'-phosphopantetheine + CO2","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:16793"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:16526"},{"database":"ChEBI","id":"CHEBI:59458"},{"database":"ChEBI","id":"CHEBI:61723"}]}}
```

Source SHA-256: `4f24a50395840d689b2bca6503bac71363002becd9e9b0e170ac85361993f2a0`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/C6TA59?format=txt&versions=84)  
**Locator:** `lines 6-10`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 84 / 1.  
**Retrieved:** 2026-11-02T04:27:37.263279+00:00.  

```text
DE   RecName: Full=Phosphopantothenoylcysteine decarboxylase HAL3b {ECO:0000305};
DE            Short=PPCDC {ECO:0000305};
DE            EC=4.1.1.36 {ECO:0000250|UniProtKB:Q9SWE5};
DE   AltName: Full=Halotolerance protein 3b {ECO:0000303|Ref.3, ECO:0000303|Ref.4};
DE            Short=GmHAL3b {ECO:0000303|Ref.3, ECO:0000303|Ref.4};
```

Source SHA-256: `9ba69ef0f337ff2a30393964c793af5f757c0c52e62614aa37894bfe6ab8f68d`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/C6TA59?format=txt&versions=84)  
**Locator:** `lines 62-68`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 84 / 1.  
**Retrieved:** 2026-11-02T04:27:37.263279+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=N-[(R)-4-phosphopantothenoyl]-L-cysteine + H(+) = (R)-4'-
CC         phosphopantetheine + CO2; Xref=Rhea:RHEA:16793, ChEBI:CHEBI:15378,
CC         ChEBI:CHEBI:16526, ChEBI:CHEBI:59458, ChEBI:CHEBI:61723; EC=4.1.1.36;
CC         Evidence={ECO:0000250|UniProtKB:Q9SWE5};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:16794;
CC         Evidence={ECO:0000250|UniProtKB:Q9SWE5};
```

Source SHA-256: `9ba69ef0f337ff2a30393964c793af5f757c0c52e62614aa37894bfe6ab8f68d`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 73. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
