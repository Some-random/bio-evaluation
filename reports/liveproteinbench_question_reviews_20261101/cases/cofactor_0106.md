# cofactor_0106

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `cofactor`  
**Author expected answer:** **A** — FMN

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MSSTAPEDVARPLLALPAIEAFDAIVRGRRSVRSYADVQVPRRTVRDVLELAARAPSNSNVQPWHTYVLTGRHKRALTDSVLRYYDTIGRTVREFDYQPGPDGWEEPYKERRESFGEGLYGRALGLSLADVDDREFYHRRNYDFFAAPVGLIVTVARNPRLSALIDAGAYIQTILLSARSRGLSTCAQASFLDFHPAVRECLAIPTHRTIVCGISLGYEDAQHPIASNATTREPVDRHVTFLWDDDD

[Multiple Choices]
A. FMN
B. a divalent metal cation
C. [2Fe-2S] cluster
D. pyridoxal 5'-phosphate
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

> The exact supplied sequence matches the UniProt entry annotated as binding one FMN per subunit, supporting choice A. However, the cofactor annotation is transferred by similarity from another UniProt protein (ECO:0000250), not direct experimental evidence for this sequence.

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence alone does not provide a sufficiently definitive cofactor-binding signature to distinguish FMN from the listed alternatives; identifying the protein as a 4-nitrobenzoate reductase would help, but that identity is not supplied.


**Missing item-specific fact**

> The protein-specific annotation or experimental determination that this enzyme binds FMN is absent from the input.


**Reason**

> The key is supported by reviewer-only annotation, but that annotation was not supplied to the model. Exact-sequence recognition or recall of the protein's entry would be lookup or memorization, not reasoning from the provided evidence.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The supplied evidence does not establish another listed choice, though the input itself lacks enough information to distinguish the choices reliably.


### Important caveats

- The reviewer-only annotation matches the exact sequence but attributes the FMN annotation to similarity-based evidence rather than direct experimental evidence for this protein.
- The author’s source snapshot is unknown; a historical matching UniProt record also carried the FMN annotation.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence alone does not provide a sufficiently definitive cofactor-binding signature to distinguish FMN from the listed alternatives; identifying the protein as a 4-nitrobenzoate reductase would help, but that identity is not supplied.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific annotation or experimental determination that this enzyme binds FMN is absent from the input.",
    "reason": "The key is supported by reviewer-only annotation, but that annotation was not supplied to the model. Exact-sequence recognition or recall of the protein's entry would be lookup or memorization, not reasoning from the provided evidence."
  },
  "case_id": "cofactor_0106",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact supplied sequence matches the UniProt entry annotated as binding one FMN per subunit, supporting choice A. However, the cofactor annotation is transferred by similarity from another UniProt protein (ECO:0000250), not direct experimental evidence for this sequence."
  },
  "important_caveats": [
    "The reviewer-only annotation matches the exact sequence but attributes the FMN annotation to similarity-based evidence rather than direct experimental evidence for this protein.",
    "The author’s source snapshot is unknown; a historical matching UniProt record also carried the FMN annotation."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied evidence does not establish another listed choice, though the input itself lacks enough information to distinguish the choices reliably."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "cofactor_0106",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact supplied sequence matches the UniProt entry annotated as binding one FMN per subunit, supporting choice A. However, the cofactor annotation is transferred by similarity from another UniProt protein (ECO:0000250), not direct experimental evidence for this sequence.",
    "evidence_ids": ["C1", "C5", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence alone does not provide a sufficiently definitive cofactor-binding signature to distinguish FMN from the listed alternatives; identifying the protein as a 4-nitrobenzoate reductase would help, but that identity is not supplied.",
    "missing_item_specific_fact": "The protein-specific annotation or experimental determination that this enzyme binds FMN is absent from the input.",
    "reason": "The key is supported by reviewer-only annotation, but that annotation was not supplied to the model. Exact-sequence recognition or recall of the protein's entry would be lookup or memorization, not reasoning from the provided evidence."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied evidence does not establish another listed choice, though the input itself lacks enough information to distinguish the choices reliably."
  },
  "important_caveats": [
    "The reviewer-only annotation matches the exact sequence but attributes the FMN annotation to similarity-based evidence rather than direct experimental evidence for this protein.",
    "The author’s source snapshot is unknown; a historical matching UniProt record also carried the FMN annotation."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry P0DXG6 annotates FMN as the cofactor (CHEBI:58210, 'Binds 1 FMN per subunit'), matching the expected answer. The evidence code is ECO:0000250 (inferred by similarity to A0R6D0), so the FMN assignment for this specific protein is a computational transfer rather than direct experimental measurement. However, the protein is classified as a nitroreductase (EC 1.7.1.-), and FMN is the well-established canonical cofactor for the nitroreductase superfamily. The primary reference (PubMed 34554625) provides FUNCTION, CATALYTIC ACTIVITY, and BIOPHYSICOCHEMICAL PROPERTIES data, lending indirect experimental support. The annotation is consistent with established biochemistry of this enzyme class.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4), [C4](#evidence-c4), [H2](#evidence-h2), [C6](#evidence-c6), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 247-aa sequence contains recognizable features of the nitroreductase/flavoprotein superfamily: a Rossmann-fold-like FMN-binding motif (the 'GLYGRALGLSLADV' segment displays the G-x-G-x-x-G flavin-binding pattern), an overall α/β fold architecture, and a size consistent with monomeric nitroreductases (~200–250 aa). Nitroreductases are a large, well-characterized enzyme class whose defining cofactor is FMN. Among the four choices, FMN is the only cofactor biochemically consistent with a flavoprotein oxidoreductase. A divalent metal cation (B) would require metal-coordinating His/Asp/Glu triads not prominently featured here; a &#91;2Fe-2S&#93; cluster (C) would require a Cys-rich motif (C-x-x-C-x-x-C-x-x-C) absent from this sequence; PLP (D) is the cofactor of aminotransferases and decarboxylases, not oxidoreductases of this fold. Thus, recognizing the protein as a flavoprotein-type oxidoreductase from sequence architecture and eliminating the three biochemically incompatible distractors constitutes a defensible reasoning path.


**Missing item-specific fact**

> None strictly required. The model does not need to know this is specifically a 4-nitrobenzoate reductase; identifying it as a member of the nitroreductase superfamily (or more broadly a flavoprotein oxidoreductase) from sequence motifs and applying the general rule that this class uses FMN suffices. Exact sequence-to-accession lookup would shortcut the reasoning but is not logically necessary.


**Reason**

> The sequence provides concrete structural-biochemical clues (Rossmann-like flavin-binding motif, absence of metal/Fe-S/PLP signatures) that allow a knowledgeable model to select FMN over the three distractors through general enzymology. The question does not hinge on a single obscure annotation fact.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four choices are biochemically distinct and mutually exclusive for a nitroreductase-fold protein. FMN is the canonical and only plausible cofactor; metal cations, Fe-S clusters, and PLP are associated with entirely different enzyme folds and mechanisms. No ambiguity exists among the options once the protein family is recognized.


### Important caveats

- The FMN cofactor annotation carries evidence code ECO:0000250 (inferred by similarity to UniProtKB:A0R6D0), not direct experimental proof for P0DXG6 itself. The parent publication (PubMed 34554625) reports catalytic and biophysical data that support but do not independently confirm the FMN assignment for this exact protein.
- The UniProt entry was first released 2025-02-05; the author's source snapshot date is unknown. The sequence matches exactly in both current and historical (entry version 3) records.
- The reviewer-only accession P0DXG6 was inferred from dataset metadata and was not available to the evaluated model; the model must work from the raw sequence alone.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 247-aa sequence contains recognizable features of the nitroreductase/flavoprotein superfamily: a Rossmann-fold-like FMN-binding motif (the 'GLYGRALGLSLADV' segment displays the G-x-G-x-x-G flavin-binding pattern), an overall α/β fold architecture, and a size consistent with monomeric nitroreductases (~200–250 aa). Nitroreductases are a large, well-characterized enzyme class whose defining cofactor is FMN. Among the four choices, FMN is the only cofactor biochemically consistent with a flavoprotein oxidoreductase. A divalent metal cation (B) would require metal-coordinating His/Asp/Glu triads not prominently featured here; a [2Fe-2S] cluster (C) would require a Cys-rich motif (C-x-x-C-x-x-C-x-x-C) absent from this sequence; PLP (D) is the cofactor of aminotransferases and decarboxylases, not oxidoreductases of this fold. Thus, recognizing the protein as a flavoprotein-type oxidoreductase from sequence architecture and eliminating the three biochemically incompatible distractors constitutes a defensible reasoning path.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None strictly required. The model does not need to know this is specifically a 4-nitrobenzoate reductase; identifying it as a member of the nitroreductase superfamily (or more broadly a flavoprotein oxidoreductase) from sequence motifs and applying the general rule that this class uses FMN suffices. Exact sequence-to-accession lookup would shortcut the reasoning but is not logically necessary.",
    "reason": "The sequence provides concrete structural-biochemical clues (Rossmann-like flavin-binding motif, absence of metal/Fe-S/PLP signatures) that allow a knowledgeable model to select FMN over the three distractors through general enzymology. The question does not hinge on a single obscure annotation fact."
  },
  "case_id": "cofactor_0106",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4",
      "C4",
      "H2",
      "C6",
      "H3"
    ],
    "judgment": "supported",
    "reason": "UniProt entry P0DXG6 annotates FMN as the cofactor (CHEBI:58210, 'Binds 1 FMN per subunit'), matching the expected answer. The evidence code is ECO:0000250 (inferred by similarity to A0R6D0), so the FMN assignment for this specific protein is a computational transfer rather than direct experimental measurement. However, the protein is classified as a nitroreductase (EC 1.7.1.-), and FMN is the well-established canonical cofactor for the nitroreductase superfamily. The primary reference (PubMed 34554625) provides FUNCTION, CATALYTIC ACTIVITY, and BIOPHYSICOCHEMICAL PROPERTIES data, lending indirect experimental support. The annotation is consistent with established biochemistry of this enzyme class."
  },
  "important_caveats": [
    "The FMN cofactor annotation carries evidence code ECO:0000250 (inferred by similarity to UniProtKB:A0R6D0), not direct experimental proof for P0DXG6 itself. The parent publication (PubMed 34554625) reports catalytic and biophysical data that support but do not independently confirm the FMN assignment for this exact protein.",
    "The UniProt entry was first released 2025-02-05; the author's source snapshot date is unknown. The sequence matches exactly in both current and historical (entry version 3) records.",
    "The reviewer-only accession P0DXG6 was inferred from dataset metadata and was not available to the evaluated model; the model must work from the raw sequence alone."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices are biochemically distinct and mutually exclusive for a nitroreductase-fold protein. FMN is the canonical and only plausible cofactor; metal cations, Fe-S clusters, and PLP are associated with entirely different enzyme folds and mechanisms. No ambiguity exists among the options once the protein family is recognized."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "cofactor_0106",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry P0DXG6 annotates FMN as the cofactor (CHEBI:58210, 'Binds 1 FMN per subunit'), matching the expected answer. The evidence code is ECO:0000250 (inferred by similarity to A0R6D0), so the FMN assignment for this specific protein is a computational transfer rather than direct experimental measurement. However, the protein is classified as a nitroreductase (EC 1.7.1.-), and FMN is the well-established canonical cofactor for the nitroreductase superfamily. The primary reference (PubMed 34554625) provides FUNCTION, CATALYTIC ACTIVITY, and BIOPHYSICOCHEMICAL PROPERTIES data, lending indirect experimental support. The annotation is consistent with established biochemistry of this enzyme class.",
    "evidence_ids": ["C5", "H4", "C4", "H2", "C6", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 247-aa sequence contains recognizable features of the nitroreductase/flavoprotein superfamily: a Rossmann-fold-like FMN-binding motif (the 'GLYGRALGLSLADV' segment displays the G-x-G-x-x-G flavin-binding pattern), an overall α/β fold architecture, and a size consistent with monomeric nitroreductases (~200–250 aa). Nitroreductases are a large, well-characterized enzyme class whose defining cofactor is FMN. Among the four choices, FMN is the only cofactor biochemically consistent with a flavoprotein oxidoreductase. A divalent metal cation (B) would require metal-coordinating His/Asp/Glu triads not prominently featured here; a [2Fe-2S] cluster (C) would require a Cys-rich motif (C-x-x-C-x-x-C-x-x-C) absent from this sequence; PLP (D) is the cofactor of aminotransferases and decarboxylases, not oxidoreductases of this fold. Thus, recognizing the protein as a flavoprotein-type oxidoreductase from sequence architecture and eliminating the three biochemically incompatible distractors constitutes a defensible reasoning path.",
    "missing_item_specific_fact": "None strictly required. The model does not need to know this is specifically a 4-nitrobenzoate reductase; identifying it as a member of the nitroreductase superfamily (or more broadly a flavoprotein oxidoreductase) from sequence motifs and applying the general rule that this class uses FMN suffices. Exact sequence-to-accession lookup would shortcut the reasoning but is not logically necessary.",
    "reason": "The sequence provides concrete structural-biochemical clues (Rossmann-like flavin-binding motif, absence of metal/Fe-S/PLP signatures) that allow a knowledgeable model to select FMN over the three distractors through general enzymology. The question does not hinge on a single obscure annotation fact."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices are biochemically distinct and mutually exclusive for a nitroreductase-fold protein. FMN is the canonical and only plausible cofactor; metal cations, Fe-S clusters, and PLP are associated with entirely different enzyme folds and mechanisms. No ambiguity exists among the options once the protein family is recognized."
  },
  "important_caveats": [
    "The FMN cofactor annotation carries evidence code ECO:0000250 (inferred by similarity to UniProtKB:A0R6D0), not direct experimental proof for P0DXG6 itself. The parent publication (PubMed 34554625) reports catalytic and biophysical data that support but do not independently confirm the FMN assignment for this exact protein.",
    "The UniProt entry was first released 2025-02-05; the author's source snapshot date is unknown. The sequence matches exactly in both current and historical (entry version 3) records.",
    "The reviewer-only accession P0DXG6 was inferred from dataset metadata and was not available to the evaluated model; the model must work from the raw sequence alone."
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

**Accession:** `P0DXG6` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 3. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXG6.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:26.531539+00:00.  

```json
"P0DXG6"
```

Source SHA-256: `adb8135fbe43dc6d05fa848fc357b229a5a07072499f7104d6191c232bd5c429`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXG6.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:26.531539+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"34554625","source":"PubMed"}],"value":"4-nitrobenzoate nitroreductase"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"34554625","source":"PubMed"}],"value":"4-NBA nitroreductase"}]}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"34554625","source":"PubMed"}],"value":"1.7.1.-"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"34554625","source":"PubMed"}],"value":"4-nitrobenzoate reductase"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"34554625","source":"PubMed"}],"value":"4-NBA reductase"}]}}
```

Source SHA-256: `adb8135fbe43dc6d05fa848fc357b229a5a07072499f7104d6191c232bd5c429`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXG6.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:26.531539+00:00.  

```json
{"cofactors":[{"cofactorCrossReference":{"database":"ChEBI","id":"CHEBI:58210"},"evidences":[{"evidenceCode":"ECO:0000250","id":"A0R6D0","source":"UniProtKB"}],"name":"FMN"}],"commentType":"COFACTOR","note":{"texts":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"A0R6D0","source":"UniProtKB"}],"value":"Binds 1 FMN per subunit."}]}}
```

Source SHA-256: `adb8135fbe43dc6d05fa848fc357b229a5a07072499f7104d6191c232bd5c429`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXG6.json)  
**Locator:** `/references/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:26.531539+00:00.  

```json
{"citation":{"authors":["Cheng M.","Qian Y.","Xing Z.","Zylstra G.J.","Huang X."],"citationCrossReferences":[{"database":"PubMed","id":"34554625"},{"database":"DOI","id":"10.1111/1462-2920.15787"}],"citationType":"journal article","firstPage":"7028","id":"34554625","journal":"Environ. Microbiol.","lastPage":"7041","publicationDate":"2021","title":"The low-nanomolar 4-nitrobenzoate-responsive repressor PnbX negatively regulates the actinomycete-derived 4-nitrobenzoate-degrading pnb locus.","volume":"23"},"referenceComments":[{"type":"STRAIN","value":"LMS-CY"}],"referenceNumber":1,"referencePositions":["NUCLEOTIDE SEQUENCE [LARGE SCALE GENOMIC DNA]","FUNCTION","CATALYTIC ACTIVITY","BIOPHYSICOCHEMICAL PROPERTIES","INDUCTION"]}
```

Source SHA-256: `adb8135fbe43dc6d05fa848fc357b229a5a07072499f7104d6191c232bd5c429`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXG6?format=txt&versions=3)  
**Locator:** `lines 6-10`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 3 / 1.  
**Retrieved:** 2026-11-02T04:29:31.939265+00:00.  

```text
DE   RecName: Full=4-nitrobenzoate reductase {ECO:0000303|PubMed:34554625};
DE            Short=4-NBA reductase {ECO:0000303|PubMed:34554625};
DE            EC=1.7.1.- {ECO:0000269|PubMed:34554625};
DE   AltName: Full=4-nitrobenzoate nitroreductase {ECO:0000303|PubMed:34554625};
DE            Short=4-NBA nitroreductase {ECO:0000303|PubMed:34554625};
```

Source SHA-256: `6bf7ac47ab7367bc964f268ea8c8b2cfa06e184e9dfb134015fe0af0dcebef36`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXG6?format=txt&versions=3)  
**Locator:** `lines 17-25`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 3 / 1.  
**Retrieved:** 2026-11-02T04:29:31.939265+00:00.  

```text
RN   [1]
RP   NUCLEOTIDE SEQUENCE [LARGE SCALE GENOMIC DNA], FUNCTION, CATALYTIC
RP   ACTIVITY, BIOPHYSICOCHEMICAL PROPERTIES, AND INDUCTION.
RC   STRAIN=LMS-CY;
RX   PubMed=34554625; DOI=10.1111/1462-2920.15787;
RA   Cheng M., Qian Y., Xing Z., Zylstra G.J., Huang X.;
RT   "The low-nanomolar 4-nitrobenzoate-responsive repressor PnbX negatively
RT   regulates the actinomycete-derived 4-nitrobenzoate-degrading pnb locus.";
RL   Environ. Microbiol. 23:7028-7041(2021).
```

Source SHA-256: `6bf7ac47ab7367bc964f268ea8c8b2cfa06e184e9dfb134015fe0af0dcebef36`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXG6?format=txt&versions=3)  
**Locator:** `lines 38-41`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 3 / 1.  
**Retrieved:** 2026-11-02T04:29:31.939265+00:00.  

```text
CC   -!- COFACTOR:
CC       Name=FMN; Xref=ChEBI:CHEBI:58210;
CC         Evidence={ECO:0000250|UniProtKB:A0R6D0};
CC       Note=Binds 1 FMN per subunit. {ECO:0000250|UniProtKB:A0R6D0};
```

Source SHA-256: `6bf7ac47ab7367bc964f268ea8c8b2cfa06e184e9dfb134015fe0af0dcebef36`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/cofactor.json), zero-based source row 106. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
