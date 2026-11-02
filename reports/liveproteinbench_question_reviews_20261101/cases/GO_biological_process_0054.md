# GO_biological_process_0054

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_biological_process`  
**Author expected answer:** **C** — virion attachment to host cell

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MEPSKLFIMSDNATFAPGPVVNAAGKKTFRTCFRILVLSVQAVTLILVIVTLGELIRMINDQGLSNQLSSITDKIRESAAMIASAVGVMNQVIHGVTVSLPLQIEGNQNQLLSTLATICTNRNQVSNCSTNIPLVNDLRFINGINKFIIEDYATHDFSIGHPLNMPSFIPTATSPNGCTRIPSFSLGKTHWCYTHNVINANCKDHTSSNQYVSMGILVQTASGYPMFKTLKIQYLSDGLNRKSCSIATVPDGCAMYCYVSTQLETDDYAGSSPPTQKLTLLFYNDTIKERTISPSGLEGNWATLVPGVGSGIYFENKLIFPAYGGVLPNSTLGVKSAREFFRPVNPYNPCSGPPQELDQRALRSYFPSYFSSRRVQSAFLVCAWNQILVTNCELVVPSNNQTLMGAEGRVLLINNRLLYYQRSTSWWPYELLYEISFTFTNSGQSSVNMSWIPIYSFTRPGLGKCSGENICPTVCVSGVYLDPWPLTPYSHQSGINRNFYFTGALLNSSTTRVNPTLYVSALNNLKVLAPYGTQGLFASYTTTTCFQDTGDASVYCVYIMELASNIVGEFQILPVLARLTIT

[Multiple Choices]
A. response to parathyroid hormone
B. response to acidic pH
C. virion attachment to host cell
D. myelination
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Gene Ontology (GO) Biological Process Prediction, which is to predict the primary biological process a given protein participates in, as defined by the Gene Ontology (GO) 'Biological Process' branch. A biological process is a series of molecular events that accomplishes a larger biological program, such as cell division or signal transduction. Based on the provided protein sequence, you must select the option that best describes the overall biological objective to which the protein contributes.. The inputs provided by the user for this task include:

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

> The supplied sequence exactly matches the mumps virus hemagglutinin-neuraminidase entry. Its function annotation says it attaches the virus to sialic-acid-containing cell receptors, and the matching historical entry assigns GO:0019062, virion attachment to host cell. The functional evidence is by similarity, and the GO annotation is IEA, not direct experimental evidence for this exact sequence.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C8](#evidence-c8), [H1](#evidence-h1), [H2](#evidence-h2), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence is compatible with a membrane-associated protein with a large extracellular region, but that alone does not identify its specific role in virion attachment or meaningfully distinguish that process from the other choices.


**Missing item-specific fact**

> The protein-specific identity and functional annotation as mumps virus hemagglutinin-neuraminidase, including its receptor-binding role, are absent from the input.


**Reason**

> Choosing C requires identifying this particular viral protein or knowing its specific receptor-binding function; generic sequence properties do not establish the biological process.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The matching protein annotation specifically supports virion attachment to host cell; the other options do not have comparable support.


### Important caveats

- The annotation applies to an exact sequence match, but the protein-specific identity was established using reviewer-only information not provided to the evaluated model.
- The functional annotation is transferred by similarity, and the GO process annotation is electronic; neither establishes direct experimental evidence for this exact sequence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is compatible with a membrane-associated protein with a large extracellular region, but that alone does not identify its specific role in virion attachment or meaningfully distinguish that process from the other choices.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific identity and functional annotation as mumps virus hemagglutinin-neuraminidase, including its receptor-binding role, are absent from the input.",
    "reason": "Choosing C requires identifying this particular viral protein or knowing its specific receptor-binding function; generic sequence properties do not establish the biological process."
  },
  "case_id": "GO_biological_process_0054",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C8",
      "H1",
      "H2",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the mumps virus hemagglutinin-neuraminidase entry. Its function annotation says it attaches the virus to sialic-acid-containing cell receptors, and the matching historical entry assigns GO:0019062, virion attachment to host cell. The functional evidence is by similarity, and the GO annotation is IEA, not direct experimental evidence for this exact sequence."
  },
  "important_caveats": [
    "The annotation applies to an exact sequence match, but the protein-specific identity was established using reviewer-only information not provided to the evaluated model.",
    "The functional annotation is transferred by similarity, and the GO process annotation is electronic; neither establishes direct experimental evidence for this exact sequence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matching protein annotation specifically supports virion attachment to host cell; the other options do not have comparable support."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_biological_process_0054",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the mumps virus hemagglutinin-neuraminidase entry. Its function annotation says it attaches the virus to sialic-acid-containing cell receptors, and the matching historical entry assigns GO:0019062, virion attachment to host cell. The functional evidence is by similarity, and the GO annotation is IEA, not direct experimental evidence for this exact sequence.",
    "evidence_ids": ["C1", "C4", "C5", "C8", "H1", "H2", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence is compatible with a membrane-associated protein with a large extracellular region, but that alone does not identify its specific role in virion attachment or meaningfully distinguish that process from the other choices.",
    "missing_item_specific_fact": "The protein-specific identity and functional annotation as mumps virus hemagglutinin-neuraminidase, including its receptor-binding role, are absent from the input.",
    "reason": "Choosing C requires identifying this particular viral protein or knowing its specific receptor-binding function; generic sequence properties do not establish the biological process."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matching protein annotation specifically supports virion attachment to host cell; the other options do not have comparable support."
  },
  "important_caveats": [
    "The annotation applies to an exact sequence match, but the protein-specific identity was established using reviewer-only information not provided to the evaluated model.",
    "The functional annotation is transferred by similarity, and the GO process annotation is electronic; neither establishes direct experimental evidence for this exact sequence."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence matches UniProt Q8QV65, the Hemagglutinin-neuraminidase (HN) of Mumps virus (strain Jeryl-Lynn). The UniProt entry directly annotates GO:0019062 'virion attachment to host cell' (evidence IEA:UniProtKB-KW, evidence_id C8/H5). The FUNCTION comment (C5/H2) states: 'Attaches the virus to alpha-2,3-linked sialic acid-containing cell receptors and thereby initiating infection.' The GO term definition (GO2) is 'The process by which a virion protein binds to molecules on the host cellular surface.' The annotation evidence code is IEA (inferred from electronic annotation via keyword), not direct experimental, but the functional description is consistent with well-established paramyxovirus HN biology. The expected answer C is supported.

Citations as saved: [C1](#evidence-c1), [C3](#evidence-c3), [C4](#evidence-c4), [C5](#evidence-c5), [C8](#evidence-c8), [H1](#evidence-h1), [H2](#evidence-h2), [H5](#evidence-h5), [GO2](#evidence-go2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 582-aa sequence displays hallmarks of a viral envelope surface glycoprotein: a hydrophobic transmembrane segment near the N-terminus (residues ~30-50, ILVLSVQAVTLILVIVTLGELIR), multiple N-glycosylation sequons (N-X-S/T motifs distributed throughout the extracellular domain), and several cysteine residues consistent with structural disulfide bonds. This architecture (extracellular domain + TM anchor + short cytoplasmic tail) is characteristic of paramyxovirus surface glycoproteins. Among the four options, only C ('virion attachment to host cell') describes a viral biological process; A (parathyroid hormone response), B (acidic pH response), and D (myelination) are mammalian cellular processes incompatible with a viral membrane glycoprotein. Recognizing the protein as viral and selecting the sole viral option constitutes a valid reasoning chain from sequence features to answer.


**Missing item-specific fact**

> Precise identification of this sequence as the Mumps HN protein (rather than, e.g., a different viral glycoprotein) would require database lookup. However, this is not needed to answer the question, since C is the only viral-process option and the other three are clearly non-viral mammalian processes.


**Reason**

> A model with general virology and protein-structure knowledge can identify the sequence as a viral surface glycoprotein from its TM domain, glycosylation pattern, and cysteine architecture, then eliminate the three mammalian-process distractors to arrive at C. The reasoning does not require memorizing the specific UniProt accession or GO annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options A, B, and D describe mammalian cellular processes (hormone signaling, pH stress response, oligodendrocyte/Schwann cell myelination) that are incompatible with a viral membrane glycoprotein. Option C is the only viral biological process and the only one consistent with the protein's architecture. No ambiguity among the choices.


### Important caveats

- The GO annotation for GO:0019062 carries evidence code IEA:UniProtKB-KW (inferred from electronic annotation via keyword KW-1161), not direct experimental evidence. The functional description itself is annotated 'By similarity' (ECO:0000250) from related paramyxovirus HN proteins (Q786F2, Q9WAF5).
- The reviewer evidence confirms sequence identity (SHA-256 match) between the benchmark sequence and UniProt Q8QV65, but the accession was inferred from dataset metadata absent from the model input.
- The reasoning path relies on recognizing viral glycoprotein features (TM domain, N-glycosylation, disulfide bonds) and eliminating non-viral options; it does not require identifying the exact virus or protein name.
- The GO annotation is present in both the current entry (v116) and the historical entry (v114), so the annotation was available at the approximate benchmark construction date.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 582-aa sequence displays hallmarks of a viral envelope surface glycoprotein: a hydrophobic transmembrane segment near the N-terminus (residues ~30-50, ILVLSVQAVTLILVIVTLGELIR), multiple N-glycosylation sequons (N-X-S/T motifs distributed throughout the extracellular domain), and several cysteine residues consistent with structural disulfide bonds. This architecture (extracellular domain + TM anchor + short cytoplasmic tail) is characteristic of paramyxovirus surface glycoproteins. Among the four options, only C ('virion attachment to host cell') describes a viral biological process; A (parathyroid hormone response), B (acidic pH response), and D (myelination) are mammalian cellular processes incompatible with a viral membrane glycoprotein. Recognizing the protein as viral and selecting the sole viral option constitutes a valid reasoning chain from sequence features to answer.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "Precise identification of this sequence as the Mumps HN protein (rather than, e.g., a different viral glycoprotein) would require database lookup. However, this is not needed to answer the question, since C is the only viral-process option and the other three are clearly non-viral mammalian processes.",
    "reason": "A model with general virology and protein-structure knowledge can identify the sequence as a viral surface glycoprotein from its TM domain, glycosylation pattern, and cysteine architecture, then eliminate the three mammalian-process distractors to arrive at C. The reasoning does not require memorizing the specific UniProt accession or GO annotation."
  },
  "case_id": "GO_biological_process_0054",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C3",
      "C4",
      "C5",
      "C8",
      "H1",
      "H2",
      "H5",
      "GO2"
    ],
    "judgment": "supported",
    "reason": "The sequence matches UniProt Q8QV65, the Hemagglutinin-neuraminidase (HN) of Mumps virus (strain Jeryl-Lynn). The UniProt entry directly annotates GO:0019062 'virion attachment to host cell' (evidence IEA:UniProtKB-KW, evidence_id C8/H5). The FUNCTION comment (C5/H2) states: 'Attaches the virus to alpha-2,3-linked sialic acid-containing cell receptors and thereby initiating infection.' The GO term definition (GO2) is 'The process by which a virion protein binds to molecules on the host cellular surface.' The annotation evidence code is IEA (inferred from electronic annotation via keyword), not direct experimental, but the functional description is consistent with well-established paramyxovirus HN biology. The expected answer C is supported."
  },
  "important_caveats": [
    "The GO annotation for GO:0019062 carries evidence code IEA:UniProtKB-KW (inferred from electronic annotation via keyword KW-1161), not direct experimental evidence. The functional description itself is annotated 'By similarity' (ECO:0000250) from related paramyxovirus HN proteins (Q786F2, Q9WAF5).",
    "The reviewer evidence confirms sequence identity (SHA-256 match) between the benchmark sequence and UniProt Q8QV65, but the accession was inferred from dataset metadata absent from the model input.",
    "The reasoning path relies on recognizing viral glycoprotein features (TM domain, N-glycosylation, disulfide bonds) and eliminating non-viral options; it does not require identifying the exact virus or protein name.",
    "The GO annotation is present in both the current entry (v116) and the historical entry (v114), so the annotation was available at the approximate benchmark construction date."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A, B, and D describe mammalian cellular processes (hormone signaling, pH stress response, oligodendrocyte/Schwann cell myelination) that are incompatible with a viral membrane glycoprotein. Option C is the only viral biological process and the only one consistent with the protein's architecture. No ambiguity among the choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_biological_process_0054",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches UniProt Q8QV65, the Hemagglutinin-neuraminidase (HN) of Mumps virus (strain Jeryl-Lynn). The UniProt entry directly annotates GO:0019062 'virion attachment to host cell' (evidence IEA:UniProtKB-KW, evidence_id C8/H5). The FUNCTION comment (C5/H2) states: 'Attaches the virus to alpha-2,3-linked sialic acid-containing cell receptors and thereby initiating infection.' The GO term definition (GO2) is 'The process by which a virion protein binds to molecules on the host cellular surface.' The annotation evidence code is IEA (inferred from electronic annotation via keyword), not direct experimental, but the functional description is consistent with well-established paramyxovirus HN biology. The expected answer C is supported.",
    "evidence_ids": ["C1", "C3", "C4", "C5", "C8", "H1", "H2", "H5", "GO2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 582-aa sequence displays hallmarks of a viral envelope surface glycoprotein: a hydrophobic transmembrane segment near the N-terminus (residues ~30-50, ILVLSVQAVTLILVIVTLGELIR), multiple N-glycosylation sequons (N-X-S/T motifs distributed throughout the extracellular domain), and several cysteine residues consistent with structural disulfide bonds. This architecture (extracellular domain + TM anchor + short cytoplasmic tail) is characteristic of paramyxovirus surface glycoproteins. Among the four options, only C ('virion attachment to host cell') describes a viral biological process; A (parathyroid hormone response), B (acidic pH response), and D (myelination) are mammalian cellular processes incompatible with a viral membrane glycoprotein. Recognizing the protein as viral and selecting the sole viral option constitutes a valid reasoning chain from sequence features to answer.",
    "missing_item_specific_fact": "Precise identification of this sequence as the Mumps HN protein (rather than, e.g., a different viral glycoprotein) would require database lookup. However, this is not needed to answer the question, since C is the only viral-process option and the other three are clearly non-viral mammalian processes.",
    "reason": "A model with general virology and protein-structure knowledge can identify the sequence as a viral surface glycoprotein from its TM domain, glycosylation pattern, and cysteine architecture, then eliminate the three mammalian-process distractors to arrive at C. The reasoning does not require memorizing the specific UniProt accession or GO annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A, B, and D describe mammalian cellular processes (hormone signaling, pH stress response, oligodendrocyte/Schwann cell myelination) that are incompatible with a viral membrane glycoprotein. Option C is the only viral biological process and the only one consistent with the protein's architecture. No ambiguity among the choices."
  },
  "important_caveats": [
    "The GO annotation for GO:0019062 carries evidence code IEA:UniProtKB-KW (inferred from electronic annotation via keyword KW-1161), not direct experimental evidence. The functional description itself is annotated 'By similarity' (ECO:0000250) from related paramyxovirus HN proteins (Q786F2, Q9WAF5).",
    "The reviewer evidence confirms sequence identity (SHA-256 match) between the benchmark sequence and UniProt Q8QV65, but the accession was inferred from dataset metadata absent from the model input.",
    "The reasoning path relies on recognizing viral glycoprotein features (TM domain, N-glycosylation, disulfide bonds) and eliminating non-viral options; it does not require identifying the exact virus or protein name.",
    "The GO annotation is present in both the current entry (v116) and the historical entry (v114), so the annotation was available at the approximate benchmark construction date."
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

**Accession:** `Q8QV65` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 114. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8QV65.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:24.225587+00:00.  

```json
"Q8QV65"
```

Source SHA-256: `bc4438119d1c029de1baa6feae7ea6afaed8e7e0d19410c4fed725f8fcb3753b`.

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8QV65.json)  
**Locator:** `/organism`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:24.225587+00:00.  

```json
{"commonName":"MuV","lineage":["Viruses","Riboviria","Orthornavirae","Negarnaviricota","Haploviricotina","Monjiviricetes","Mononegavirales","Paramyxoviridae","Rubulavirinae","Orthorubulavirus","Orthorubulavirus parotitidis","Mumps orthorubulavirus"],"scientificName":"Mumps virus genotype A (strain Jeryl-Lynn)","taxonId":11168}
```

Source SHA-256: `bc4438119d1c029de1baa6feae7ea6afaed8e7e0d19410c4fed725f8fcb3753b`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8QV65.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:24.225587+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q9WAF5","source":"UniProtKB"}],"value":"3.2.1.18"}],"fullName":{"value":"Hemagglutinin-neuraminidase"}}}
```

Source SHA-256: `bc4438119d1c029de1baa6feae7ea6afaed8e7e0d19410c4fed725f8fcb3753b`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8QV65.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:24.225587+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q786F2","source":"UniProtKB"},{"evidenceCode":"ECO:0000250","id":"Q9WAF5","source":"UniProtKB"}],"value":"Attaches the virus to alpha-2,3-linked sialic acid-containing cell receptors and thereby initiating infection (By similarity). Binding of HN protein to the receptor induces a conformational change that allows the F protein to trigger virion/cell membranes fusion (By similarity). Binds to the glycan motifs sialyl Lewis (SLe) and GM2 ganglioside (GM2-glycan) (By similarity)"}]}
```

Source SHA-256: `bc4438119d1c029de1baa6feae7ea6afaed8e7e0d19410c4fed725f8fcb3753b`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8QV65.json)  
**Locator:** `/uniProtKBCrossReferences/13`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:24.225587+00:00.  

```json
{"database":"GO","id":"GO:0019062","properties":[{"key":"GoTerm","value":"P:virion attachment to host cell"},{"key":"GoEvidenceType","value":"IEA:UniProtKB-KW"}]}
```

Source SHA-256: `bc4438119d1c029de1baa6feae7ea6afaed8e7e0d19410c4fed725f8fcb3753b`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8QV65?format=txt&versions=114)  
**Locator:** `lines 1-14`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 114 / 1.  
**Retrieved:** 2026-11-02T04:32:27.640645+00:00.  

```text
ID   HN_MUMPJ                Reviewed;         582 AA.
AC   Q8QV65; C7C5S5;
DT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.
DT   01-JUN-2002, sequence version 1.
DT   28-JAN-2026, entry version 114.
DE   RecName: Full=Hemagglutinin-neuraminidase;
DE            EC=3.2.1.18 {ECO:0000250|UniProtKB:Q9WAF5};
GN   Name=HN;
OS   Mumps virus genotype A (strain Jeryl-Lynn) (MuV).
OC   Viruses; Riboviria; Orthornavirae; Negarnaviricota; Haploviricotina;
OC   Monjiviricetes; Mononegavirales; Paramyxoviridae; Rubulavirinae;
OC   Orthorubulavirus; Orthorubulavirus parotitidis; Mumps orthorubulavirus.
OX   NCBI_TaxID=11168;
OH   NCBI_TaxID=9606; Homo sapiens (Human).
```

Source SHA-256: `32a38cacb11cc75414f260107fe816d041e5d43d9075624a51461e99158215ec`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8QV65?format=txt&versions=114)  
**Locator:** `lines 40-46`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 114 / 1.  
**Retrieved:** 2026-11-02T04:32:27.640645+00:00.  

```text
CC   -!- FUNCTION: Attaches the virus to alpha-2,3-linked sialic acid-containing
CC       cell receptors and thereby initiating infection (By similarity).
CC       Binding of HN protein to the receptor induces a conformational change
CC       that allows the F protein to trigger virion/cell membranes fusion (By
CC       similarity). Binds to the glycan motifs sialyl Lewis (SLe) and GM2
CC       ganglioside (GM2-glycan) (By similarity).
CC       {ECO:0000250|UniProtKB:Q786F2, ECO:0000250|UniProtKB:Q9WAF5}.
```

Source SHA-256: `32a38cacb11cc75414f260107fe816d041e5d43d9075624a51461e99158215ec`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8QV65?format=txt&versions=114)  
**Locator:** `lines 86-86`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 114 / 1.  
**Retrieved:** 2026-11-02T04:32:27.640645+00:00.  

```text
DR   GO; GO:0019062; P:virion attachment to host cell; IEA:UniProtKB-KW.
```

Source SHA-256: `32a38cacb11cc75414f260107fe816d041e5d43d9075624a51461e99158215ec`.

### Evidence GO2

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 145019-145031`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0019062
name: virion attachment to host cell
namespace: biological_process
def: "The process by which a virion protein binds to molecules on the host cellular surface or host cell surface projection." [GOC:bf, GOC:jl, UniProtKB-KW:KW-1161, VZ:956]
subset: goslim_virus
synonym: "viral absorption" EXACT []
synonym: "viral attachment to host cell" RELATED [GOC:bf, GOC:jl]
synonym: "virion attachment to host cell surface receptor" NARROW []
xref: VZ:956 "Viral attachment to host cell"
is_a: GO:0044650 ! adhesion of symbiont to host cell
relationship: part_of GO:0019058 ! viral life cycle

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_biological_process.json), zero-based source row 54. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
