# GO_biological_process_0054: before and after transfer clarification

[All 1,328 cases](../README.md) · [Method](../METHOD.md) · [Summary](../SUMMARY.md) · [Exact reviewer user message](../inputs/GO_biological_process_0054.txt)

**Task:** `GO_biological_process`  
**Author key, unchanged:** **C** — virion attachment to host cell

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
MEPSKLFIMSDNATFAPGPVVNAAGKKTFRTCFRILVLSVQAVTLILVIVTLGELIRMINDQGLSNQLSSITDKIRESAAMIASAVGVMNQVIHGVTVSLPLQIEGNQNQLLSTLATICTNRNQVSNCSTNIPLVNDLRFINGINKFIIEDYATHDFSIGHPLNMPSFIPTATSPNGCTRIPSFSLGKTHWCYTHNVINANCKDHTSSNQYVSMGILVQTASGYPMFKTLKIQYLSDGLNRKSCSIATVPDGCAMYCYVSTQLETDDYAGSSPPTQKLTLLFYNDTIKERTISPSGLEGNWATLVPGVGSGIYFENKLIFPAYGGVLPNSTLGVKSAREFFRPVNPYNPCSGPPQELDQRALRSYFPSYFSSRRVQSAFLVCAWNQILVTNCELVVPSNNQTLMGAEGRVLLINNRLLYYQRSTSWWPYELLYEISFTFTNSGQSSVNMSWIPIYSFTRPGLGKCSGENICPTVCVSGVYLDPWPLTPYSHQSGINRNFYFTGALLNSSTTRVNPTLYVSALNNLKVLAPYGTQGLFASYTTTTCFQDTGDASVYCVYIMELASNIVGEFQILPVLARLTIT

[Multiple Choices]
A. response to parathyroid hormone
B. response to acidic pH
C. virion attachment to host cell
D. myelination
```

<details>
<summary>Complete original system instructions</summary>

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

## Four saved visible reviews

## Before: GPT-6 Luna

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

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

## Before: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

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

## After: GPT-6 Luna

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence-matched annotation identifies virion attachment to host cell (C8). The associated function annotation says the protein attaches virus to sialic-acid-containing cell receptors and initiates infection, but this is supported by similarity rather than direct experimental evidence for this protein (C5).

Citations as saved: [C5](#evidence-c5), [C8](#evidence-c8).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The N-terminal membrane anchor followed by a large extracellular domain, together with the sequence's viral hemagglutinin-neuraminidase family features, supports recognizing a paramyxovirus HN-like surface protein. HN-family proteins bind host-cell sialic-acid receptors to attach virions, distinguishing C from the hormone response, acidic-pH response, and myelination choices.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Family-level recognition and the conserved attachment role of viral HN proteins provide a meaningful inference from the sequence and transferable knowledge; the exact protein's database annotation is not necessary to distinguish the offered choices.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the offered choices, virion attachment best matches the inferred viral receptor-binding role.


### Important caveats

- The supporting UniProt function annotation is by similarity, and the GO annotation is electronic; the supplied evidence does not establish direct experimental validation for this exact protein.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal membrane anchor followed by a large extracellular domain, together with the sequence's viral hemagglutinin-neuraminidase family features, supports recognizing a paramyxovirus HN-like surface protein. HN-family proteins bind host-cell sialic-acid receptors to attach virions, distinguishing C from the hormone response, acidic-pH response, and myelination choices.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Family-level recognition and the conserved attachment role of viral HN proteins provide a meaningful inference from the sequence and transferable knowledge; the exact protein's database annotation is not necessary to distinguish the offered choices."
  },
  "case_id": "GO_biological_process_0054",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C8"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched annotation identifies virion attachment to host cell (C8). The associated function annotation says the protein attaches virus to sialic-acid-containing cell receptors and initiates infection, but this is supported by similarity rather than direct experimental evidence for this protein (C5)."
  },
  "important_caveats": [
    "The supporting UniProt function annotation is by similarity, and the GO annotation is electronic; the supplied evidence does not establish direct experimental validation for this exact protein."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the offered choices, virion attachment best matches the inferred viral receptor-binding role."
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
    "reason": "The sequence-matched annotation identifies virion attachment to host cell (C8). The associated function annotation says the protein attaches virus to sialic-acid-containing cell receptors and initiates infection, but this is supported by similarity rather than direct experimental evidence for this protein (C5).",
    "evidence_ids": ["C5", "C8"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The N-terminal membrane anchor followed by a large extracellular domain, together with the sequence's viral hemagglutinin-neuraminidase family features, supports recognizing a paramyxovirus HN-like surface protein. HN-family proteins bind host-cell sialic-acid receptors to attach virions, distinguishing C from the hormone response, acidic-pH response, and myelination choices.",
    "missing_item_specific_fact": "",
    "reason": "Family-level recognition and the conserved attachment role of viral HN proteins provide a meaningful inference from the sequence and transferable knowledge; the exact protein's database annotation is not necessary to distinguish the offered choices."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the offered choices, virion attachment best matches the inferred viral receptor-binding role."
  },
  "important_caveats": [
    "The supporting UniProt function annotation is by similarity, and the GO annotation is electronic; the supplied evidence does not establish direct experimental validation for this exact protein."
  ]
}
```

</details>

## After: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The reviewer-only evidence confirms this is the Hemagglutinin-neuraminidase (HN) protein of Mumps virus (Q8QV65). UniProt function annotation states it 'Attaches the virus to alpha-2,3-linked sialic acid-containing cell receptors and thereby initiating infection.' GO annotation GO:0019062 (virion attachment to host cell) is present (IEA:UniProtKB-KW). The functional description and GO term directly match option C.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C8](#evidence-c8), [H2](#evidence-h2), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 582-aa sequence exhibits hallmarks of paramyxovirus HN (hemagglutinin-neuraminidase) attachment glycoproteins, a well-characterized protein family shared across NDV, measles, parainfluenza, and mumps viruses. Key transferable features include: (1) the conserved neuraminidase active-site motifs (e.g., 'CYTH' in 'THWCYTHNV' corresponding to the R-Y-E catalytic region conserved across all paramyxovirus HN proteins); (2) the characteristic type-II membrane protein architecture (N-terminal signal-anchor followed by a large ectodomain); (3) the conserved cysteine spacing patterns ('CW' motifs in 'LVTNCE' and 'CPTVCV') typical of paramyxovirus attachment proteins; (4) the overall length (~560-630 aa) matching the paramyxovirus HN family. Neuraminidase activity cleaves sialic acid from host receptors, which is mechanistically inseparable from viral attachment/detachment. Against the distractors: myelination (D) involves oligodendrocyte/Schwann-cell structural proteins (MBP, PLP, MAG) with entirely different architectures; response to parathyroid hormone (A) involves mammalian GPCR signaling components; response to acidic pH (B) describes endosomal conformational changes (as in influenza HA fusion peptide), not the primary enzymatic attachment function of HN. Recognizing the neuraminidase motif and paramyxovirus HN family architecture from other viruses (NDV HN, measles H) provides a concrete, transferable basis for selecting C.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A model with knowledge of paramyxovirus HN proteins from other members (NDV, parainfluenza, measles) can recognize the conserved neuraminidase motifs, the type-II membrane topology, and the ~582-aa length as hallmarks of the viral attachment glycoprotein family. This family-level pattern meaningfully distinguishes option C from the three clearly unrelated distractors without requiring the exact UniProt record for this specific mumps strain.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The three distractors (parathyroid hormone response, acidic pH response, myelination) describe mammalian cellular processes with no plausible connection to a viral neuraminidase/attachment glycoprotein. No reasonable biological argument supports any option other than C for a protein with conserved paramyxovirus HN architecture.


### Important caveats

- The GO annotation for this entry is IEA:UniProtKB-KW (inferred from keyword), not experimentally verified for this specific mumps strain. However, the functional mechanism (sialic-acid binding/attachment) is well-established across the paramyxovirus HN family.
- The reviewer-only evidence reveals the exact organism (Mumps virus Jeryl-Lynn) and protein name (HN), which were not provided to the evaluated model. The model must rely on sequence features and family-level knowledge.
- The neuraminidase catalytic motifs are recognizable but require familiarity with paramyxovirus HN sequences from other members of the family.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 582-aa sequence exhibits hallmarks of paramyxovirus HN (hemagglutinin-neuraminidase) attachment glycoproteins, a well-characterized protein family shared across NDV, measles, parainfluenza, and mumps viruses. Key transferable features include: (1) the conserved neuraminidase active-site motifs (e.g., 'CYTH' in 'THWCYTHNV' corresponding to the R-Y-E catalytic region conserved across all paramyxovirus HN proteins); (2) the characteristic type-II membrane protein architecture (N-terminal signal-anchor followed by a large ectodomain); (3) the conserved cysteine spacing patterns ('CW' motifs in 'LVTNCE' and 'CPTVCV') typical of paramyxovirus attachment proteins; (4) the overall length (~560-630 aa) matching the paramyxovirus HN family. Neuraminidase activity cleaves sialic acid from host receptors, which is mechanistically inseparable from viral attachment/detachment. Against the distractors: myelination (D) involves oligodendrocyte/Schwann-cell structural proteins (MBP, PLP, MAG) with entirely different architectures; response to parathyroid hormone (A) involves mammalian GPCR signaling components; response to acidic pH (B) describes endosomal conformational changes (as in influenza HA fusion peptide), not the primary enzymatic attachment function of HN. Recognizing the neuraminidase motif and paramyxovirus HN family architecture from other viruses (NDV HN, measles H) provides a concrete, transferable basis for selecting C.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A model with knowledge of paramyxovirus HN proteins from other members (NDV, parainfluenza, measles) can recognize the conserved neuraminidase motifs, the type-II membrane topology, and the ~582-aa length as hallmarks of the viral attachment glycoprotein family. This family-level pattern meaningfully distinguishes option C from the three clearly unrelated distractors without requiring the exact UniProt record for this specific mumps strain."
  },
  "case_id": "GO_biological_process_0054",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C8",
      "H2",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The reviewer-only evidence confirms this is the Hemagglutinin-neuraminidase (HN) protein of Mumps virus (Q8QV65). UniProt function annotation states it 'Attaches the virus to alpha-2,3-linked sialic acid-containing cell receptors and thereby initiating infection.' GO annotation GO:0019062 (virion attachment to host cell) is present (IEA:UniProtKB-KW). The functional description and GO term directly match option C."
  },
  "important_caveats": [
    "The GO annotation for this entry is IEA:UniProtKB-KW (inferred from keyword), not experimentally verified for this specific mumps strain. However, the functional mechanism (sialic-acid binding/attachment) is well-established across the paramyxovirus HN family.",
    "The reviewer-only evidence reveals the exact organism (Mumps virus Jeryl-Lynn) and protein name (HN), which were not provided to the evaluated model. The model must rely on sequence features and family-level knowledge.",
    "The neuraminidase catalytic motifs are recognizable but require familiarity with paramyxovirus HN sequences from other members of the family."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The three distractors (parathyroid hormone response, acidic pH response, myelination) describe mammalian cellular processes with no plausible connection to a viral neuraminidase/attachment glycoprotein. No reasonable biological argument supports any option other than C for a protein with conserved paramyxovirus HN architecture."
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
    "reason": "The reviewer-only evidence confirms this is the Hemagglutinin-neuraminidase (HN) protein of Mumps virus (Q8QV65). UniProt function annotation states it 'Attaches the virus to alpha-2,3-linked sialic acid-containing cell receptors and thereby initiating infection.' GO annotation GO:0019062 (virion attachment to host cell) is present (IEA:UniProtKB-KW). The functional description and GO term directly match option C.",
    "evidence_ids": ["C4", "C5", "C8", "H2", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 582-aa sequence exhibits hallmarks of paramyxovirus HN (hemagglutinin-neuraminidase) attachment glycoproteins, a well-characterized protein family shared across NDV, measles, parainfluenza, and mumps viruses. Key transferable features include: (1) the conserved neuraminidase active-site motifs (e.g., 'CYTH' in 'THWCYTHNV' corresponding to the R-Y-E catalytic region conserved across all paramyxovirus HN proteins); (2) the characteristic type-II membrane protein architecture (N-terminal signal-anchor followed by a large ectodomain); (3) the conserved cysteine spacing patterns ('CW' motifs in 'LVTNCE' and 'CPTVCV') typical of paramyxovirus attachment proteins; (4) the overall length (~560-630 aa) matching the paramyxovirus HN family. Neuraminidase activity cleaves sialic acid from host receptors, which is mechanistically inseparable from viral attachment/detachment. Against the distractors: myelination (D) involves oligodendrocyte/Schwann-cell structural proteins (MBP, PLP, MAG) with entirely different architectures; response to parathyroid hormone (A) involves mammalian GPCR signaling components; response to acidic pH (B) describes endosomal conformational changes (as in influenza HA fusion peptide), not the primary enzymatic attachment function of HN. Recognizing the neuraminidase motif and paramyxovirus HN family architecture from other viruses (NDV HN, measles H) provides a concrete, transferable basis for selecting C.",
    "missing_item_specific_fact": "",
    "reason": "A model with knowledge of paramyxovirus HN proteins from other members (NDV, parainfluenza, measles) can recognize the conserved neuraminidase motifs, the type-II membrane topology, and the ~582-aa length as hallmarks of the viral attachment glycoprotein family. This family-level pattern meaningfully distinguishes option C from the three clearly unrelated distractors without requiring the exact UniProt record for this specific mumps strain."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The three distractors (parathyroid hormone response, acidic pH response, myelination) describe mammalian cellular processes with no plausible connection to a viral neuraminidase/attachment glycoprotein. No reasonable biological argument supports any option other than C for a protein with conserved paramyxovirus HN architecture."
  },
  "important_caveats": [
    "The GO annotation for this entry is IEA:UniProtKB-KW (inferred from keyword), not experimentally verified for this specific mumps strain. However, the functional mechanism (sialic-acid binding/attachment) is well-established across the paramyxovirus HN family.",
    "The reviewer-only evidence reveals the exact organism (Mumps virus Jeryl-Lynn) and protein name (HN), which were not provided to the evaluated model. The model must rely on sequence features and family-level knowledge.",
    "The neuraminidase catalytic motifs are recognizable but require familiarity with paramyxovirus HN sequences from other members of the family."
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
  "requested_accession": "Q8QV65",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "benchmark_sequence_sha256": "6c411ff86d03391238be03a02eacdb3e2948b7a46bfa5706f0f99e829e1e420f",
  "benchmark_sequence_length": 582,
  "current_status": "retrieved",
  "current_sequence_comparison": "matched",
  "current_entry_audit": {
    "entryVersion": 116,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2002-06-01",
    "sequenceVersion": 1
  },
  "current_uniprot_release": "2026_03",
  "current_record_sha256": "bc4438119d1c029de1baa6feae7ea6afaed8e7e0d19410c4fed725f8fcb3753b",
  "current_source_sequence_sha256": "6c411ff86d03391238be03a02eacdb3e2948b7a46bfa5706f0f99e829e1e420f",
  "current_source_sequence_length": 582,
  "historical_status": "retrieved",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "selected_historical_entry_version": 114,
  "selected_historical_version": {
    "accession": "Q8QV65",
    "database": "Swiss-Prot",
    "entryVersion": 114,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "HN_MUMPJ",
    "sequenceVersion": 1
  },
  "selected_historical_record_sha256": "32a38cacb11cc75414f260107fe816d041e5d43d9075624a51461e99158215ec",
  "selected_historical_source_sequence_sha256": "6c411ff86d03391238be03a02eacdb3e2948b7a46bfa5706f0f99e829e1e420f",
  "selected_historical_source_sequence_length": 582,
  "latest_at_cutoff_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 114,
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8QV65.json)

```json
{
  "evidence_id": "C1",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q8QV65.json",
  "source_sha256": "bc4438119d1c029de1baa6feae7ea6afaed8e7e0d19410c4fed725f8fcb3753b",
  "retrieved_utc": "2026-11-02T04:32:24.225587+00:00",
  "json_pointer": "/primaryAccession",
  "excerpt": "\"Q8QV65\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8QV65.json)

```json
{
  "evidence_id": "C2",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q8QV65.json",
  "source_sha256": "bc4438119d1c029de1baa6feae7ea6afaed8e7e0d19410c4fed725f8fcb3753b",
  "retrieved_utc": "2026-11-02T04:32:24.225587+00:00",
  "json_pointer": "/entryAudit",
  "excerpt": "{\"entryVersion\":116,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2002-06-01\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8QV65.json)

```json
{
  "evidence_id": "C3",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q8QV65.json",
  "source_sha256": "bc4438119d1c029de1baa6feae7ea6afaed8e7e0d19410c4fed725f8fcb3753b",
  "retrieved_utc": "2026-11-02T04:32:24.225587+00:00",
  "json_pointer": "/organism",
  "excerpt": "{\"commonName\":\"MuV\",\"lineage\":[\"Viruses\",\"Riboviria\",\"Orthornavirae\",\"Negarnaviricota\",\"Haploviricotina\",\"Monjiviricetes\",\"Mononegavirales\",\"Paramyxoviridae\",\"Rubulavirinae\",\"Orthorubulavirus\",\"Orthorubulavirus parotitidis\",\"Mumps orthorubulavirus\"],\"scientificName\":\"Mumps virus genotype A (strain Jeryl-Lynn)\",\"taxonId\":11168}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8QV65.json)

```json
{
  "evidence_id": "C4",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q8QV65.json",
  "source_sha256": "bc4438119d1c029de1baa6feae7ea6afaed8e7e0d19410c4fed725f8fcb3753b",
  "retrieved_utc": "2026-11-02T04:32:24.225587+00:00",
  "json_pointer": "/proteinDescription",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9WAF5\",\"source\":\"UniProtKB\"}],\"value\":\"3.2.1.18\"}],\"fullName\":{\"value\":\"Hemagglutinin-neuraminidase\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8QV65.json)

```json
{
  "evidence_id": "C5",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q8QV65.json",
  "source_sha256": "bc4438119d1c029de1baa6feae7ea6afaed8e7e0d19410c4fed725f8fcb3753b",
  "retrieved_utc": "2026-11-02T04:32:24.225587+00:00",
  "json_pointer": "/comments/0",
  "excerpt": "{\"commentType\":\"FUNCTION\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q786F2\",\"source\":\"UniProtKB\"},{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9WAF5\",\"source\":\"UniProtKB\"}],\"value\":\"Attaches the virus to alpha-2,3-linked sialic acid-containing cell receptors and thereby initiating infection (By similarity). Binding of HN protein to the receptor induces a conformational change that allows the F protein to trigger virion/cell membranes fusion (By similarity). Binds to the glycan motifs sialyl Lewis (SLe) and GM2 ganglioside (GM2-glycan) (By similarity)\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8QV65.json)

```json
{
  "evidence_id": "C6",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q8QV65.json",
  "source_sha256": "bc4438119d1c029de1baa6feae7ea6afaed8e7e0d19410c4fed725f8fcb3753b",
  "retrieved_utc": "2026-11-02T04:32:24.225587+00:00",
  "json_pointer": "/comments/1",
  "excerpt": "{\"commentType\":\"FUNCTION\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q91UL0\",\"source\":\"UniProtKB\"}],\"value\":\"Neuraminidase activity ensures the efficient spread of the virus by dissociating the mature virions from the neuraminic acid containing glycoproteins\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8QV65.json)

```json
{
  "evidence_id": "C7",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q8QV65.json",
  "source_sha256": "bc4438119d1c029de1baa6feae7ea6afaed8e7e0d19410c4fed725f8fcb3753b",
  "retrieved_utc": "2026-11-02T04:32:24.225587+00:00",
  "json_pointer": "/uniProtKBCrossReferences/12",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0046718\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"P:symbiont entry into host cell\"},{\"key\":\"GoEvidenceType\",\"value\":\"IEA:UniProtKB-KW\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8QV65.json)

```json
{
  "evidence_id": "C8",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q8QV65.json",
  "source_sha256": "bc4438119d1c029de1baa6feae7ea6afaed8e7e0d19410c4fed725f8fcb3753b",
  "retrieved_utc": "2026-11-02T04:32:24.225587+00:00",
  "json_pointer": "/uniProtKBCrossReferences/13",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0019062\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"P:virion attachment to host cell\"},{\"key\":\"GoEvidenceType\",\"value\":\"IEA:UniProtKB-KW\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8QV65?format=txt&versions=114)

```json
{
  "evidence_id": "H1",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q8QV65?format=txt&versions=114",
  "source_sha256": "32a38cacb11cc75414f260107fe816d041e5d43d9075624a51461e99158215ec",
  "retrieved_utc": "2026-11-02T04:32:27.640645+00:00",
  "source_locator": "lines 1-14",
  "excerpt": "ID   HN_MUMPJ                Reviewed;         582 AA.\nAC   Q8QV65; C7C5S5;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   01-JUN-2002, sequence version 1.\nDT   28-JAN-2026, entry version 114.\nDE   RecName: Full=Hemagglutinin-neuraminidase;\nDE            EC=3.2.1.18 {ECO:0000250|UniProtKB:Q9WAF5};\nGN   Name=HN;\nOS   Mumps virus genotype A (strain Jeryl-Lynn) (MuV).\nOC   Viruses; Riboviria; Orthornavirae; Negarnaviricota; Haploviricotina;\nOC   Monjiviricetes; Mononegavirales; Paramyxoviridae; Rubulavirinae;\nOC   Orthorubulavirus; Orthorubulavirus parotitidis; Mumps orthorubulavirus.\nOX   NCBI_TaxID=11168;\nOH   NCBI_TaxID=9606; Homo sapiens (Human).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 114,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8QV65?format=txt&versions=114)

```json
{
  "evidence_id": "H2",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q8QV65?format=txt&versions=114",
  "source_sha256": "32a38cacb11cc75414f260107fe816d041e5d43d9075624a51461e99158215ec",
  "retrieved_utc": "2026-11-02T04:32:27.640645+00:00",
  "source_locator": "lines 40-46",
  "excerpt": "CC   -!- FUNCTION: Attaches the virus to alpha-2,3-linked sialic acid-containing\nCC       cell receptors and thereby initiating infection (By similarity).\nCC       Binding of HN protein to the receptor induces a conformational change\nCC       that allows the F protein to trigger virion/cell membranes fusion (By\nCC       similarity). Binds to the glycan motifs sialyl Lewis (SLe) and GM2\nCC       ganglioside (GM2-glycan) (By similarity).\nCC       {ECO:0000250|UniProtKB:Q786F2, ECO:0000250|UniProtKB:Q9WAF5}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 114,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8QV65?format=txt&versions=114)

```json
{
  "evidence_id": "H3",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q8QV65?format=txt&versions=114",
  "source_sha256": "32a38cacb11cc75414f260107fe816d041e5d43d9075624a51461e99158215ec",
  "retrieved_utc": "2026-11-02T04:32:27.640645+00:00",
  "source_locator": "lines 47-49",
  "excerpt": "CC   -!- FUNCTION: Neuraminidase activity ensures the efficient spread of the\nCC       virus by dissociating the mature virions from the neuraminic acid\nCC       containing glycoproteins. {ECO:0000250|UniProtKB:Q91UL0}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 114,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8QV65?format=txt&versions=114)

```json
{
  "evidence_id": "H4",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q8QV65?format=txt&versions=114",
  "source_sha256": "32a38cacb11cc75414f260107fe816d041e5d43d9075624a51461e99158215ec",
  "retrieved_utc": "2026-11-02T04:32:27.640645+00:00",
  "source_locator": "lines 85-85",
  "excerpt": "DR   GO; GO:0046718; P:symbiont entry into host cell; IEA:UniProtKB-KW.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 114,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8QV65?format=txt&versions=114)

```json
{
  "evidence_id": "H5",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q8QV65?format=txt&versions=114",
  "source_sha256": "32a38cacb11cc75414f260107fe816d041e5d43d9075624a51461e99158215ec",
  "retrieved_utc": "2026-11-02T04:32:27.640645+00:00",
  "source_locator": "lines 86-86",
  "excerpt": "DR   GO; GO:0019062; P:virion attachment to host cell; IEA:UniProtKB-KW.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 114,
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
  "source_locator": "lines 106089-106097",
  "excerpt": "[Term]\nid: GO:0010447\nname: response to acidic pH\nnamespace: biological_process\ndef: \"Any process that results in a change in state or activity of a cell or an organism (in terms of movement, secretion, enzyme production, gene expression, etc.) as a result of a pH stimulus with pH < 7. pH is a measure of the acidity or basicity of an aqueous solution.\" [GOC:curators, GOC:tb, Wikipedia:PH]\ncomment: This term should be used to annotate instances where a cell or organism is responding to a chemical that is playing the role of an acid (e.g. proton donor) and therefore lowering the pH. If instead you wish to describe a response to a specific acid as a chemical, such as the anion portion of glutamate, please annotate to the appropriate child of GO:0001101 'response to acid chemical'.\nsynonym: \"response to acidity\" BROAD []\nis_a: GO:0009268 ! response to pH\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "go_id": "GO:0010447"
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
  "source_locator": "lines 145019-145031",
  "excerpt": "[Term]\nid: GO:0019062\nname: virion attachment to host cell\nnamespace: biological_process\ndef: \"The process by which a virion protein binds to molecules on the host cellular surface or host cell surface projection.\" [GOC:bf, GOC:jl, UniProtKB-KW:KW-1161, VZ:956]\nsubset: goslim_virus\nsynonym: \"viral absorption\" EXACT []\nsynonym: \"viral attachment to host cell\" RELATED [GOC:bf, GOC:jl]\nsynonym: \"virion attachment to host cell surface receptor\" NARROW []\nxref: VZ:956 \"Viral attachment to host cell\"\nis_a: GO:0044650 ! adhesion of symbiont to host cell\nrelationship: part_of GO:0019058 ! viral life cycle\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "go_id": "GO:0019062"
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
  "source_locator": "lines 238590-238598",
  "excerpt": "[Term]\nid: GO:0042552\nname: myelination\nnamespace: biological_process\ndef: \"The process in which myelin sheaths are formed and maintained around neurons. Oligodendrocytes in the brain and spinal cord and Schwann cells in the peripheral nervous system wrap axons with compact layers of their plasma membrane. Adjacent myelin segments are separated by a non-myelinated stretch of axon called a node of Ranvier.\" [GOC:dgh, GOC:mah]\nsynonym: \"myelinogenesis\" RELATED [GOC:cjm, HP:0003429]\nxref: Wikipedia:Myelin\nis_a: GO:0008366 ! axon ensheathment\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "go_id": "GO:0042552"
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
  "source_locator": "lines 374090-374097",
  "excerpt": "[Term]\nid: GO:0071107\nname: response to parathyroid hormone\nnamespace: biological_process\ndef: \"Any process that results in a change in state or activity of a cell or an organism (in terms of movement, secretion, enzyme production, gene expression, etc.) as a result of a parathyroid hormone stimulus.\" [GOC:mah, GOC:yaf]\nsynonym: \"response to parathyroid hormone stimulus\" EXACT [GOC:dos]\nis_a: GO:0009725 ! response to hormone\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "go_id": "GO:0071107"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_biological_process.json), zero-based source row 54. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
