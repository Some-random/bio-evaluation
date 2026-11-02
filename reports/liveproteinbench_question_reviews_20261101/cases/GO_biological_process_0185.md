# GO_biological_process_0185

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_biological_process`  
**Author expected answer:** **C** — negative stranded viral RNA transcription

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MSSVLKAFERFTIEQELQDRGEEGSIPPETLKSAVKVFVINTPNPTTRYQMLNFCLRIICSQNARASHRVGALITLFSLPSAGMQNHIRLADRSPEAQIERCEIDGFEPGTYRLIPNARANLTANEIAAYALLADDLPPTINNGTPYVHADVEGQPCDEIEQFLDRCYSVLIQAWVMVCKCMTAYDQPAGSADRRFAKYQQQGRLEARYMLQPEAQRLIQTAIRKSLVVRQYLTFELQLARRQGLLSNRYYAMVGDIGKYIENSGLTAFFLTLKYALGTKWSPLSLAAFTGELTKLRSLMMLYRDLGEQARYLALLEAPQIMDFAPGGYPLIFSYAMGVGTVLDVQMRNYTYARPFLNGYYFQIGVETARRQQGTVDNRVADDLGLTPEQRTEVTQLVDRLARGRGAGIPGGPVNPFVPPVQQQQPAAVYEDIPALEESDDDGDEDGGAGFQNGAQAPAVRQGGQNDFRAQPLQDPIQAQLFMPLYPQVSNIPNHQNHQINRIGGMEHQDLLRYNENGDSQQDARGEHGNTFPNNPNQNAQSQVGDWDE

[Multiple Choices]
A. signal transduction
B. mitochondrial respiratory chain complex assembly
C. negative stranded viral RNA transcription
D. response to cobalamin
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

> The sequence exactly matches the mumps virus nucleoprotein in the current and archived UniProt records. That record annotates negative stranded viral RNA transcription; the current annotation has IDA evidence, and the term also appears in the archived record.

Citations as saved: [C1](#evidence-c1), [C3](#evidence-c3), [C4](#evidence-c4), [C7](#evidence-c7), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> Once identified as a nucleoprotein of a negative-strand RNA virus, its association with the encapsidated genome used for transcription makes C biologically plausible. The supplied sequence alone does not establish that identity or specific role.


**Missing item-specific fact**

> The protein's identity as mumps virus nucleoprotein and its documented participation in negative-strand viral RNA transcription.


**Reason**

> Distinguishing C requires a protein-specific identification or annotation not supplied in the question; sequence inspection alone offers no decisive basis for this process among the choices.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> C is supported for this sequence, while the other choices do not describe the documented viral nucleoprotein role.


### Important caveats

- The GO annotation is reviewer-only evidence and was not available to the evaluated model.
- The archived record establishes that the term was present by the historical cutoff, but the author's exact source snapshot is unknown.
- The annotation supports the protein's contribution to transcription; it does not imply that the nucleoprotein itself catalyzes RNA synthesis.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Once identified as a nucleoprotein of a negative-strand RNA virus, its association with the encapsidated genome used for transcription makes C biologically plausible. The supplied sequence alone does not establish that identity or specific role.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein's identity as mumps virus nucleoprotein and its documented participation in negative-strand viral RNA transcription.",
    "reason": "Distinguishing C requires a protein-specific identification or annotation not supplied in the question; sequence inspection alone offers no decisive basis for this process among the choices."
  },
  "case_id": "GO_biological_process_0185",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C3",
      "C4",
      "C7",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The sequence exactly matches the mumps virus nucleoprotein in the current and archived UniProt records. That record annotates negative stranded viral RNA transcription; the current annotation has IDA evidence, and the term also appears in the archived record."
  },
  "important_caveats": [
    "The GO annotation is reviewer-only evidence and was not available to the evaluated model.",
    "The archived record establishes that the term was present by the historical cutoff, but the author's exact source snapshot is unknown.",
    "The annotation supports the protein's contribution to transcription; it does not imply that the nucleoprotein itself catalyzes RNA synthesis."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "C is supported for this sequence, while the other choices do not describe the documented viral nucleoprotein role."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_biological_process_0185",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence exactly matches the mumps virus nucleoprotein in the current and archived UniProt records. That record annotates negative stranded viral RNA transcription; the current annotation has IDA evidence, and the term also appears in the archived record.",
    "evidence_ids": ["C1", "C3", "C4", "C7", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "Once identified as a nucleoprotein of a negative-strand RNA virus, its association with the encapsidated genome used for transcription makes C biologically plausible. The supplied sequence alone does not establish that identity or specific role.",
    "missing_item_specific_fact": "The protein's identity as mumps virus nucleoprotein and its documented participation in negative-strand viral RNA transcription.",
    "reason": "Distinguishing C requires a protein-specific identification or annotation not supplied in the question; sequence inspection alone offers no decisive basis for this process among the choices."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "C is supported for this sequence, while the other choices do not describe the documented viral nucleoprotein role."
  },
  "important_caveats": [
    "The GO annotation is reviewer-only evidence and was not available to the evaluated model.",
    "The archived record establishes that the term was present by the historical cutoff, but the author's exact source snapshot is unknown.",
    "The annotation supports the protein's contribution to transcription; it does not imply that the nucleoprotein itself catalyzes RNA synthesis."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The protein sequence matches UniProt Q9DQA5 (NCAP_MUMPV), the Mumps virus Nucleoprotein, a paramyxovirus (Mononegavirales, negative-stranded RNA virus). UniProt annotates this protein with GO:0039697 'negative stranded viral RNA transcription' with IDA:UniProtKB evidence (PubMed:25948749, Zengel et al. 2015, demonstrating roles of N phosphorylation in regulating viral RNA transcription and replication). The FUNCTION comment confirms the encapsidated genomic RNA serves as template for transcription and replication. The GO term definition (GO:0039697) is 'A viral transcription process that uses negative stranded (-) single stranded (ss) RNA as a template,' which matches the protein's role. The IDA evidence code indicates direct experimental support.

Citations as saved: [C1](#evidence-c1), [C3](#evidence-c3), [C4](#evidence-c4), [C5](#evidence-c5), [C7](#evidence-c7), [C9](#evidence-c9), [H1](#evidence-h1), [H3](#evidence-h3), [H5](#evidence-h5), [GO4](#evidence-go4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> A knowledgeable biologist could partially eliminate options B (no mitochondrial transit peptide or respiratory chain complex assembly motifs) and D (no cobalamin/vitamin B12 binding motifs). The protein also lacks canonical signal transduction domains (no kinase, GTPase, phosphatase, SH2/SH3, or receptor-like domains), weakening option A. However, arriving at the specific answer 'negative stranded viral RNA transcription' requires recognizing this as a paramyxovirus nucleoprotein involved in RNA encapsidation and transcription, which is a protein-specific identification rather than a general reasoning chain from sequence features.


**Missing item-specific fact**

> The identification of this 549-aa sequence as the Mumps virus (or paramyxovirus) Nucleoprotein, a component of the negative-stranded RNA virus nucleocapsid complex that serves as template for viral transcription. Without this specific protein identity, the sequence's composition (basic patches, helical regions, C-terminal acidic tail) is not uniquely diagnostic of 'negative stranded viral RNA transcription' versus other broad categories.


**Reason**

> While negative elimination of B and D is feasible, and the absence of canonical signaling domains weakens A, the positive assignment to 'negative stranded viral RNA transcription' requires recognizing this specific protein as a paramyxovirus N protein. The sequence does not contain a unique, unambiguous motif that would lead a biologist to this precise GO term through general reasoning alone. This is essentially a protein identification task followed by annotation lookup.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the four choices, C is clearly the best fit. GO:0039689 'negative stranded viral RNA replication' is also annotated to this protein but is not offered as an option. Options A, B, and D are well-motivated distractors that can be eliminated. No ambiguity in the correct answer among the given choices.


### Important caveats

- The UniProt entry was first publicly released on 2025-04-09 (entry version 77 current); the benchmark may have been constructed from an earlier data source or different annotation snapshot.
- The GO annotation evidence code is IDA (Inferred from Direct Assay) referencing PubMed:25948749, indicating experimental support rather than purely computational inference.
- The protein is also annotated to GO:0039689 (negative stranded viral RNA replication), indicating it participates in both transcription and replication; the question asks for the 'primary' process and selects transcription, which is defensible but somewhat arbitrary given the dual annotation.
- The sequence match is confirmed (SHA256 match between benchmark and UniProt entry), so the annotation applies directly to the supplied sequence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "A knowledgeable biologist could partially eliminate options B (no mitochondrial transit peptide or respiratory chain complex assembly motifs) and D (no cobalamin/vitamin B12 binding motifs). The protein also lacks canonical signal transduction domains (no kinase, GTPase, phosphatase, SH2/SH3, or receptor-like domains), weakening option A. However, arriving at the specific answer 'negative stranded viral RNA transcription' requires recognizing this as a paramyxovirus nucleoprotein involved in RNA encapsidation and transcription, which is a protein-specific identification rather than a general reasoning chain from sequence features.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The identification of this 549-aa sequence as the Mumps virus (or paramyxovirus) Nucleoprotein, a component of the negative-stranded RNA virus nucleocapsid complex that serves as template for viral transcription. Without this specific protein identity, the sequence's composition (basic patches, helical regions, C-terminal acidic tail) is not uniquely diagnostic of 'negative stranded viral RNA transcription' versus other broad categories.",
    "reason": "While negative elimination of B and D is feasible, and the absence of canonical signaling domains weakens A, the positive assignment to 'negative stranded viral RNA transcription' requires recognizing this specific protein as a paramyxovirus N protein. The sequence does not contain a unique, unambiguous motif that would lead a biologist to this precise GO term through general reasoning alone. This is essentially a protein identification task followed by annotation lookup."
  },
  "case_id": "GO_biological_process_0185",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C3",
      "C4",
      "C5",
      "C7",
      "C9",
      "H1",
      "H3",
      "H5",
      "GO4"
    ],
    "judgment": "supported",
    "reason": "The protein sequence matches UniProt Q9DQA5 (NCAP_MUMPV), the Mumps virus Nucleoprotein, a paramyxovirus (Mononegavirales, negative-stranded RNA virus). UniProt annotates this protein with GO:0039697 'negative stranded viral RNA transcription' with IDA:UniProtKB evidence (PubMed:25948749, Zengel et al. 2015, demonstrating roles of N phosphorylation in regulating viral RNA transcription and replication). The FUNCTION comment confirms the encapsidated genomic RNA serves as template for transcription and replication. The GO term definition (GO:0039697) is 'A viral transcription process that uses negative stranded (-) single stranded (ss) RNA as a template,' which matches the protein's role. The IDA evidence code indicates direct experimental support."
  },
  "important_caveats": [
    "The UniProt entry was first publicly released on 2025-04-09 (entry version 77 current); the benchmark may have been constructed from an earlier data source or different annotation snapshot.",
    "The GO annotation evidence code is IDA (Inferred from Direct Assay) referencing PubMed:25948749, indicating experimental support rather than purely computational inference.",
    "The protein is also annotated to GO:0039689 (negative stranded viral RNA replication), indicating it participates in both transcription and replication; the question asks for the 'primary' process and selects transcription, which is defensible but somewhat arbitrary given the dual annotation.",
    "The sequence match is confirmed (SHA256 match between benchmark and UniProt entry), so the annotation applies directly to the supplied sequence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the four choices, C is clearly the best fit. GO:0039689 'negative stranded viral RNA replication' is also annotated to this protein but is not offered as an option. Options A, B, and D are well-motivated distractors that can be eliminated. No ambiguity in the correct answer among the given choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_biological_process_0185",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The protein sequence matches UniProt Q9DQA5 (NCAP_MUMPV), the Mumps virus Nucleoprotein, a paramyxovirus (Mononegavirales, negative-stranded RNA virus). UniProt annotates this protein with GO:0039697 'negative stranded viral RNA transcription' with IDA:UniProtKB evidence (PubMed:25948749, Zengel et al. 2015, demonstrating roles of N phosphorylation in regulating viral RNA transcription and replication). The FUNCTION comment confirms the encapsidated genomic RNA serves as template for transcription and replication. The GO term definition (GO:0039697) is 'A viral transcription process that uses negative stranded (-) single stranded (ss) RNA as a template,' which matches the protein's role. The IDA evidence code indicates direct experimental support.",
    "evidence_ids": ["C1", "C3", "C4", "C5", "C7", "C9", "H1", "H3", "H5", "GO4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "A knowledgeable biologist could partially eliminate options B (no mitochondrial transit peptide or respiratory chain complex assembly motifs) and D (no cobalamin/vitamin B12 binding motifs). The protein also lacks canonical signal transduction domains (no kinase, GTPase, phosphatase, SH2/SH3, or receptor-like domains), weakening option A. However, arriving at the specific answer 'negative stranded viral RNA transcription' requires recognizing this as a paramyxovirus nucleoprotein involved in RNA encapsidation and transcription, which is a protein-specific identification rather than a general reasoning chain from sequence features.",
    "missing_item_specific_fact": "The identification of this 549-aa sequence as the Mumps virus (or paramyxovirus) Nucleoprotein, a component of the negative-stranded RNA virus nucleocapsid complex that serves as template for viral transcription. Without this specific protein identity, the sequence's composition (basic patches, helical regions, C-terminal acidic tail) is not uniquely diagnostic of 'negative stranded viral RNA transcription' versus other broad categories.",
    "reason": "While negative elimination of B and D is feasible, and the absence of canonical signaling domains weakens A, the positive assignment to 'negative stranded viral RNA transcription' requires recognizing this specific protein as a paramyxovirus N protein. The sequence does not contain a unique, unambiguous motif that would lead a biologist to this precise GO term through general reasoning alone. This is essentially a protein identification task followed by annotation lookup."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the four choices, C is clearly the best fit. GO:0039689 'negative stranded viral RNA replication' is also annotated to this protein but is not offered as an option. Options A, B, and D are well-motivated distractors that can be eliminated. No ambiguity in the correct answer among the given choices."
  },
  "important_caveats": [
    "The UniProt entry was first publicly released on 2025-04-09 (entry version 77 current); the benchmark may have been constructed from an earlier data source or different annotation snapshot.",
    "The GO annotation evidence code is IDA (Inferred from Direct Assay) referencing PubMed:25948749, indicating experimental support rather than purely computational inference.",
    "The protein is also annotated to GO:0039689 (negative stranded viral RNA replication), indicating it participates in both transcription and replication; the question asks for the 'primary' process and selects transcription, which is defensible but somewhat arbitrary given the dual annotation.",
    "The sequence match is confirmed (SHA256 match between benchmark and UniProt entry), so the annotation applies directly to the supplied sequence."
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

**Accession:** `Q9DQA5` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 75. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9DQA5.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:44.717580+00:00.  

```json
"Q9DQA5"
```

Source SHA-256: `d7d60030e8c6f9e92350899ae5875332c9af57d1cad52452c8575db188eb0616`.

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9DQA5.json)  
**Locator:** `/organism`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:44.717580+00:00.  

```json
{"commonName":"MuV","lineage":["Viruses","Riboviria","Orthornavirae","Negarnaviricota","Haploviricotina","Monjiviricetes","Mononegavirales","Paramyxoviridae","Rubulavirinae","Orthorubulavirus","Orthorubulavirus parotitidis"],"scientificName":"Mumps orthorubulavirus","taxonId":2560602}
```

Source SHA-256: `d7d60030e8c6f9e92350899ae5875332c9af57d1cad52452c8575db188eb0616`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9DQA5.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:44.717580+00:00.  

```json
{"alternativeNames":[{"fullName":{"value":"Nucleocapsid protein"},"shortNames":[{"value":"NP"},{"value":"Protein N"}]}],"recommendedName":{"fullName":{"value":"Nucleoprotein"}}}
```

Source SHA-256: `d7d60030e8c6f9e92350899ae5875332c9af57d1cad52452c8575db188eb0616`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9DQA5.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:44.717580+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"P06159","source":"UniProtKB"},{"evidenceCode":"ECO:0000269","id":"25288750","source":"PubMed"}],"value":"Forms the helical nucleocapsid (NC) with 12.71 N subunits per helical turn and a rise of 5.3 Angstrom per N subunit, protecting the genome from nucleases (PubMed:25288750). The encapsidated genomic RNA serves as template for transcription and replication; encapsidation by N is coupled to RNA synthesis (By similarity). Forms the encapsidation complex with the phosphoprotein protein P (PubMed:25288750). Before encapsidation, the newly synthesized free N protein, so-called N0, is chaperoned by P (By similarity)"}]}
```

Source SHA-256: `d7d60030e8c6f9e92350899ae5875332c9af57d1cad52452c8575db188eb0616`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9DQA5.json)  
**Locator:** `/uniProtKBCrossReferences/15`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:44.717580+00:00.  

```json
{"database":"GO","evidences":[{"evidenceCode":"ECO:0000314","id":"25948749","source":"PubMed"}],"id":"GO:0039697","properties":[{"key":"GoTerm","value":"P:negative stranded viral RNA transcription"},{"key":"GoEvidenceType","value":"IDA:UniProtKB"}]}
```

Source SHA-256: `d7d60030e8c6f9e92350899ae5875332c9af57d1cad52452c8575db188eb0616`.

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9DQA5.json)  
**Locator:** `/references/4`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:44.717580+00:00.  

```json
{"citation":{"authors":["Zengel J.","Pickar A.","Xu P.","Lin A.","He B."],"citationCrossReferences":[{"database":"PubMed","id":"25948749"},{"database":"DOI","id":"10.1128/jvi.00686-15"}],"citationType":"journal article","firstPage":"7338","id":"25948749","journal":"J. Virol.","lastPage":"7347","publicationDate":"2015","title":"Roles of Phosphorylation of the Nucleocapsid Protein of Mumps Virus in Regulating Viral RNA Transcription and Replication.","volume":"89"},"referenceNumber":5,"referencePositions":["PHOSPHORYLATION AT SER-439","MUTAGENESIS OF SER-439"]}
```

Source SHA-256: `d7d60030e8c6f9e92350899ae5875332c9af57d1cad52452c8575db188eb0616`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9DQA5?format=txt&versions=75)  
**Locator:** `lines 1-15`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 75 / 1.  
**Retrieved:** 2026-11-02T04:32:47.340950+00:00.  

```text
ID   NCAP_MUMPV              Reviewed;         549 AA.
AC   Q9DQA5;
DT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.
DT   01-MAR-2001, sequence version 1.
DT   18-JUN-2025, entry version 75.
DE   RecName: Full=Nucleoprotein;
DE   AltName: Full=Nucleocapsid protein;
DE            Short=NP;
DE            Short=Protein N;
GN   Name=N; Synonyms=NP;
OS   Mumps orthorubulavirus (MuV).
OC   Viruses; Riboviria; Orthornavirae; Negarnaviricota; Haploviricotina;
OC   Monjiviricetes; Mononegavirales; Paramyxoviridae; Rubulavirinae;
OC   Orthorubulavirus; Orthorubulavirus parotitidis.
OX   NCBI_TaxID=2560602;
```

Source SHA-256: `763472111d52213635ee889993d7006bb0d23458afc3514f6dcc2c0e7d58510d`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9DQA5?format=txt&versions=75)  
**Locator:** `lines 58-66`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 75 / 1.  
**Retrieved:** 2026-11-02T04:32:47.340950+00:00.  

```text
CC   -!- FUNCTION: Forms the helical nucleocapsid (NC) with 12.71 N subunits per
CC       helical turn and a rise of 5.3 Angstrom per N subunit, protecting the
CC       genome from nucleases (PubMed:25288750). The encapsidated genomic RNA
CC       serves as template for transcription and replication; encapsidation by
CC       N is coupled to RNA synthesis (By similarity). Forms the encapsidation
CC       complex with the phosphoprotein protein P (PubMed:25288750). Before
CC       encapsidation, the newly synthesized free N protein, so-called N0, is
CC       chaperoned by P (By similarity). {ECO:0000250|UniProtKB:P06159,
CC       ECO:0000269|PubMed:25288750}.
```

Source SHA-256: `763472111d52213635ee889993d7006bb0d23458afc3514f6dcc2c0e7d58510d`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9DQA5?format=txt&versions=75)  
**Locator:** `lines 109-109`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 75 / 1.  
**Retrieved:** 2026-11-02T04:32:47.340950+00:00.  

```text
DR   GO; GO:0039697; P:negative stranded viral RNA transcription; IDA:UniProtKB.
```

Source SHA-256: `763472111d52213635ee889993d7006bb0d23458afc3514f6dcc2c0e7d58510d`.

### Evidence GO4

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 232826-232833`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0039697
name: negative stranded viral RNA transcription
namespace: biological_process
def: "A viral transcription process that uses negative stranded (-) single stranded (ss) RNA as a template." [VZ:1096]
xref: VZ:1096 "Negative stranded RNA virus replication"
is_a: GO:0039696 ! RNA-templated viral transcription

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_biological_process.json), zero-based source row 185. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
