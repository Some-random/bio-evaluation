# GO_biological_process_0086

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_biological_process`  
**Author expected answer:** **D** — negative stranded viral RNA replication

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MDQFIKQDETGDLIETGMNVANHFLSAPIQGTNLLSKATIIPGVAPVLIGNPEQKNIQYPTASHQGSKSKGRSSGAKPIIVSSSEVGTGGTQIPEPLFAQTGQGGTVTTVYQDPTIQPTGSYRSVELAKIGKERMINRFVEKPRTSTPVTEFKRGGPGAAAQGQTIQEEGIDGNGASAGSKERSGSLSGATPYAHLSLPQQDSTPANVGIAQQSAISANEIMDLLRGMDARLQHLEQKVDKVLAQGSMVTQIKNELSTVKTTLATIEGMMATVKIMDPGNPTGVPVDELRRSFSDHVTIVSGPGDVSFSSSEEPTLYLDELARPIPKPRPAKQPKPQPVKDLAGRKVMITKMITDCVANPQMKQAFEQRLAKASTEDALNDIKRDIIRSAI

[Multiple Choices]
A. negative regulation of heterochromatin formation
B. regulation of leaf senescence
C. transcription by RNA polymerase II
D. negative stranded viral RNA replication
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

> The sequence exactly matches the 391-aa mumps orthorubulavirus phosphoprotein. Its UniProt record describes a role in viral RNA replication, and assigns negative stranded viral RNA replication with IDA evidence linked to PMID 24501400. This supports choice D; it is not merely a computational prediction.

Citations as saved: [C1](#evidence-c1), [C3](#evidence-c3), [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The choices concern very different contexts, so recognizing that the sequence belongs to a viral protein could favor D over plant- or chromatin-related processes. But the sequence alone does not provide a sufficiently specific basis to identify this protein's role in negative-strand viral RNA replication.


**Missing item-specific fact**

> The sequence-specific identity as the mumps virus phosphoprotein and its established participation in replication of the negative-strand viral RNA genome.


**Reason**

> The decisive identity and functional annotation are item-specific facts absent from the prompt. Inferring them from an exact sequence match or a database record would be lookup or memorization, not reasoning from the supplied information.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The matched protein is annotated for viral RNA replication and transcription, but the RNA polymerase II option specifies a distinct host DNA-templated process and does not describe the viral RNA synthesis role. The listed choices therefore leave D as the supported answer.


### Important caveats

- Reviewer-only database evidence supports the answer key but was not supplied to the evaluated model.
- The functional description in the protein record is partly stated as being by similarity; the GO replication annotation is separately marked IDA and linked to a publication.
- The author's exact database snapshot is unknown, although the sequence matches both the current record and the checked historical record.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The choices concern very different contexts, so recognizing that the sequence belongs to a viral protein could favor D over plant- or chromatin-related processes. But the sequence alone does not provide a sufficiently specific basis to identify this protein's role in negative-strand viral RNA replication.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The sequence-specific identity as the mumps virus phosphoprotein and its established participation in replication of the negative-strand viral RNA genome.",
    "reason": "The decisive identity and functional annotation are item-specific facts absent from the prompt. Inferring them from an exact sequence match or a database record would be lookup or memorization, not reasoning from the supplied information."
  },
  "case_id": "GO_biological_process_0086",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C3",
      "C5",
      "C6",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The sequence exactly matches the 391-aa mumps orthorubulavirus phosphoprotein. Its UniProt record describes a role in viral RNA replication, and assigns negative stranded viral RNA replication with IDA evidence linked to PMID 24501400. This supports choice D; it is not merely a computational prediction."
  },
  "important_caveats": [
    "Reviewer-only database evidence supports the answer key but was not supplied to the evaluated model.",
    "The functional description in the protein record is partly stated as being by similarity; the GO replication annotation is separately marked IDA and linked to a publication.",
    "The author's exact database snapshot is unknown, although the sequence matches both the current record and the checked historical record."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched protein is annotated for viral RNA replication and transcription, but the RNA polymerase II option specifies a distinct host DNA-templated process and does not describe the viral RNA synthesis role. The listed choices therefore leave D as the supported answer."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_biological_process_0086",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence exactly matches the 391-aa mumps orthorubulavirus phosphoprotein. Its UniProt record describes a role in viral RNA replication, and assigns negative stranded viral RNA replication with IDA evidence linked to PMID 24501400. This supports choice D; it is not merely a computational prediction.",
    "evidence_ids": ["C1", "C3", "C5", "C6", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The choices concern very different contexts, so recognizing that the sequence belongs to a viral protein could favor D over plant- or chromatin-related processes. But the sequence alone does not provide a sufficiently specific basis to identify this protein's role in negative-strand viral RNA replication.",
    "missing_item_specific_fact": "The sequence-specific identity as the mumps virus phosphoprotein and its established participation in replication of the negative-strand viral RNA genome.",
    "reason": "The decisive identity and functional annotation are item-specific facts absent from the prompt. Inferring them from an exact sequence match or a database record would be lookup or memorization, not reasoning from the supplied information."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched protein is annotated for viral RNA replication and transcription, but the RNA polymerase II option specifies a distinct host DNA-templated process and does not describe the viral RNA synthesis role. The listed choices therefore leave D as the supported answer."
  },
  "important_caveats": [
    "Reviewer-only database evidence supports the answer key but was not supplied to the evaluated model.",
    "The functional description in the protein record is partly stated as being by similarity; the GO replication annotation is separately marked IDA and linked to a publication.",
    "The author's exact database snapshot is unknown, although the sequence matches both the current record and the checked historical record."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence matches UniProt F8V2V0 (Phosphoprotein of Mumps orthorubulavirus, a (-)ssRNA virus in family Paramyxoviridae). The entry carries GO:0039689 'negative stranded viral RNA replication' annotated with IDA:UniProtKB evidence (Inferred from Direct Assay), citing PubMed:24501400. The FUNCTION comment describes the protein as an 'Essential cofactor of the RNA polymerase L that plays a central role in the transcription and replication by forming the polymerase complex with RNA polymerase L and recruiting L to the genomic N-RNA template for RNA synthesis.' The virus lineage (Negarnaviricota, Mononegavirales) confirms negative-stranded RNA virus biology. The expected answer D is directly and strongly supported.

Citations as saved: [C1](#evidence-c1), [C3](#evidence-c3), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C8](#evidence-c8), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3), [GO3](#evidence-go3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> One could weakly argue from sequence features: the protein is small (391 AA), has a highly disordered N-terminal region rich in S/T/P/G (phosphorylation sites), lacks DNA-binding domains, enzymatic chromatin-modifier domains, RNA Pol II subunit motifs, and plant-specific features. By elimination of A (no chromatin-modifying domains), C (not an RNA Pol II component or general transcription factor), and B (no plant-specific signatures), one might narrow toward a viral replication cofactor. However, this elimination is weak and does not positively identify the protein as a (-)ssRNA virus phosphoprotein without recognizing the specific sequence or knowing paramyxovirus P protein architecture.


**Missing item-specific fact**

> Identification of this exact 391-aa sequence as the Phosphoprotein (P/V) of Mumps orthorubulavirus (UniProt F8V2V0), a member of Paramyxoviridae (Mononegavirales, Negarnaviricota), which is a negative-stranded RNA virus. Without this protein-specific annotation or recognition of the paramyxovirus P protein fold/composition, the sequence alone does not positively and reliably distinguish option D from the alternatives.


**Reason**

> While the distractors are from clearly different biological contexts (epigenetic regulation, plant biology, cellular DNA-templated transcription), positively identifying the protein as a viral replication cofactor from a raw 391-aa sequence requires either recognizing the exact protein or possessing specialized knowledge of paramyxovirus phosphoprotein sequence features. General biological reasoning provides only weak eliminative arguments, not a positive identification pathway.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options span entirely different biological contexts (epigenetic regulation, plant senescence, cellular Pol II transcription, viral (-)ssRNA replication). Once the protein is identified as viral, D is unambiguously correct and A, B, C are clearly inapplicable. The UniProt entry also annotates GO:0039697 (negative stranded viral RNA transcription), but that term is not among the options, so it does not create ambiguity with the given choices.


### Important caveats

- The GO:0039689 annotation carries IDA:UniProtKB evidence (Inferred from Direct Assay) citing PubMed:24501400, a mutagenesis/phosphorylation study of mumps P protein roles in transcription and replication — this is experimental evidence, not purely computational transfer.
- The FUNCTION comment itself is annotated 'By similarity' (ECO:0000250) to P06162 (Sendai virus P) and P16072 (Measles virus P), but the GO:0039689 annotation is IDA (direct assay), which is a stronger evidence class.
- The sequence was first publicly released in UniProt on 2025-04-09 (entry version 47); the historical snapshot at entry version 45 (2026-01-28) also matches. The author's construction date is unknown.
- The identity of the protein (accession F8V2V0) was inferred by the reviewer from dataset metadata; it was not provided to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "One could weakly argue from sequence features: the protein is small (391 AA), has a highly disordered N-terminal region rich in S/T/P/G (phosphorylation sites), lacks DNA-binding domains, enzymatic chromatin-modifier domains, RNA Pol II subunit motifs, and plant-specific features. By elimination of A (no chromatin-modifying domains), C (not an RNA Pol II component or general transcription factor), and B (no plant-specific signatures), one might narrow toward a viral replication cofactor. However, this elimination is weak and does not positively identify the protein as a (-)ssRNA virus phosphoprotein without recognizing the specific sequence or knowing paramyxovirus P protein architecture.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "Identification of this exact 391-aa sequence as the Phosphoprotein (P/V) of Mumps orthorubulavirus (UniProt F8V2V0), a member of Paramyxoviridae (Mononegavirales, Negarnaviricota), which is a negative-stranded RNA virus. Without this protein-specific annotation or recognition of the paramyxovirus P protein fold/composition, the sequence alone does not positively and reliably distinguish option D from the alternatives.",
    "reason": "While the distractors are from clearly different biological contexts (epigenetic regulation, plant biology, cellular DNA-templated transcription), positively identifying the protein as a viral replication cofactor from a raw 391-aa sequence requires either recognizing the exact protein or possessing specialized knowledge of paramyxovirus phosphoprotein sequence features. General biological reasoning provides only weak eliminative arguments, not a positive identification pathway."
  },
  "case_id": "GO_biological_process_0086",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C3",
      "C4",
      "C5",
      "C6",
      "C8",
      "H1",
      "H2",
      "H3",
      "GO3"
    ],
    "judgment": "supported",
    "reason": "The sequence matches UniProt F8V2V0 (Phosphoprotein of Mumps orthorubulavirus, a (-)ssRNA virus in family Paramyxoviridae). The entry carries GO:0039689 'negative stranded viral RNA replication' annotated with IDA:UniProtKB evidence (Inferred from Direct Assay), citing PubMed:24501400. The FUNCTION comment describes the protein as an 'Essential cofactor of the RNA polymerase L that plays a central role in the transcription and replication by forming the polymerase complex with RNA polymerase L and recruiting L to the genomic N-RNA template for RNA synthesis.' The virus lineage (Negarnaviricota, Mononegavirales) confirms negative-stranded RNA virus biology. The expected answer D is directly and strongly supported."
  },
  "important_caveats": [
    "The GO:0039689 annotation carries IDA:UniProtKB evidence (Inferred from Direct Assay) citing PubMed:24501400, a mutagenesis/phosphorylation study of mumps P protein roles in transcription and replication — this is experimental evidence, not purely computational transfer.",
    "The FUNCTION comment itself is annotated 'By similarity' (ECO:0000250) to P06162 (Sendai virus P) and P16072 (Measles virus P), but the GO:0039689 annotation is IDA (direct assay), which is a stronger evidence class.",
    "The sequence was first publicly released in UniProt on 2025-04-09 (entry version 47); the historical snapshot at entry version 45 (2026-01-28) also matches. The author's construction date is unknown.",
    "The identity of the protein (accession F8V2V0) was inferred by the reviewer from dataset metadata; it was not provided to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span entirely different biological contexts (epigenetic regulation, plant senescence, cellular Pol II transcription, viral (-)ssRNA replication). Once the protein is identified as viral, D is unambiguously correct and A, B, C are clearly inapplicable. The UniProt entry also annotates GO:0039697 (negative stranded viral RNA transcription), but that term is not among the options, so it does not create ambiguity with the given choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_biological_process_0086",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches UniProt F8V2V0 (Phosphoprotein of Mumps orthorubulavirus, a (-)ssRNA virus in family Paramyxoviridae). The entry carries GO:0039689 'negative stranded viral RNA replication' annotated with IDA:UniProtKB evidence (Inferred from Direct Assay), citing PubMed:24501400. The FUNCTION comment describes the protein as an 'Essential cofactor of the RNA polymerase L that plays a central role in the transcription and replication by forming the polymerase complex with RNA polymerase L and recruiting L to the genomic N-RNA template for RNA synthesis.' The virus lineage (Negarnaviricota, Mononegavirales) confirms negative-stranded RNA virus biology. The expected answer D is directly and strongly supported.",
    "evidence_ids": ["C1", "C3", "C4", "C5", "C6", "C8", "H1", "H2", "H3", "GO3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "One could weakly argue from sequence features: the protein is small (391 AA), has a highly disordered N-terminal region rich in S/T/P/G (phosphorylation sites), lacks DNA-binding domains, enzymatic chromatin-modifier domains, RNA Pol II subunit motifs, and plant-specific features. By elimination of A (no chromatin-modifying domains), C (not an RNA Pol II component or general transcription factor), and B (no plant-specific signatures), one might narrow toward a viral replication cofactor. However, this elimination is weak and does not positively identify the protein as a (-)ssRNA virus phosphoprotein without recognizing the specific sequence or knowing paramyxovirus P protein architecture.",
    "missing_item_specific_fact": "Identification of this exact 391-aa sequence as the Phosphoprotein (P/V) of Mumps orthorubulavirus (UniProt F8V2V0), a member of Paramyxoviridae (Mononegavirales, Negarnaviricota), which is a negative-stranded RNA virus. Without this protein-specific annotation or recognition of the paramyxovirus P protein fold/composition, the sequence alone does not positively and reliably distinguish option D from the alternatives.",
    "reason": "While the distractors are from clearly different biological contexts (epigenetic regulation, plant biology, cellular DNA-templated transcription), positively identifying the protein as a viral replication cofactor from a raw 391-aa sequence requires either recognizing the exact protein or possessing specialized knowledge of paramyxovirus phosphoprotein sequence features. General biological reasoning provides only weak eliminative arguments, not a positive identification pathway."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span entirely different biological contexts (epigenetic regulation, plant senescence, cellular Pol II transcription, viral (-)ssRNA replication). Once the protein is identified as viral, D is unambiguously correct and A, B, C are clearly inapplicable. The UniProt entry also annotates GO:0039697 (negative stranded viral RNA transcription), but that term is not among the options, so it does not create ambiguity with the given choices."
  },
  "important_caveats": [
    "The GO:0039689 annotation carries IDA:UniProtKB evidence (Inferred from Direct Assay) citing PubMed:24501400, a mutagenesis/phosphorylation study of mumps P protein roles in transcription and replication — this is experimental evidence, not purely computational transfer.",
    "The FUNCTION comment itself is annotated 'By similarity' (ECO:0000250) to P06162 (Sendai virus P) and P16072 (Measles virus P), but the GO:0039689 annotation is IDA (direct assay), which is a stronger evidence class.",
    "The sequence was first publicly released in UniProt on 2025-04-09 (entry version 47); the historical snapshot at entry version 45 (2026-01-28) also matches. The author's construction date is unknown.",
    "The identity of the protein (accession F8V2V0) was inferred by the reviewer from dataset metadata; it was not provided to the evaluated model."
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

**Accession:** `F8V2V0` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 45. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/F8V2V0.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:19.040321+00:00.  

```json
"F8V2V0"
```

Source SHA-256: `56857522ea5f5b710f455232a0b818fb905cf20618243ede6b9fd62313bc5ed7`.

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/F8V2V0.json)  
**Locator:** `/organism`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:19.040321+00:00.  

```json
{"commonName":"MuV","lineage":["Viruses","Riboviria","Orthornavirae","Negarnaviricota","Haploviricotina","Monjiviricetes","Mononegavirales","Paramyxoviridae","Rubulavirinae","Orthorubulavirus","Orthorubulavirus parotitidis"],"scientificName":"Mumps orthorubulavirus","taxonId":2560602}
```

Source SHA-256: `56857522ea5f5b710f455232a0b818fb905cf20618243ede6b9fd62313bc5ed7`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/F8V2V0.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:19.040321+00:00.  

```json
{"recommendedName":{"fullName":{"value":"Phosphoprotein"}}}
```

Source SHA-256: `56857522ea5f5b710f455232a0b818fb905cf20618243ede6b9fd62313bc5ed7`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/F8V2V0.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:19.040321+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"P06162","source":"UniProtKB"},{"evidenceCode":"ECO:0000250","id":"P16072","source":"UniProtKB"}],"value":"Essential cofactor of the RNA polymerase L that plays a central role in the transcription and replication by forming the polymerase complex with RNA polymerase L and recruiting L to the genomic N-RNA template for RNA synthesis (By similarity). Also plays a central role in the encapsidation of nascent RNA chains by forming the encapsidation complex with the nucleocapsid protein N (N-P complex). Acts as a chaperone for newly synthesized free N protein, so-called N0, allowing encapsidation of nascent RNA chains during replication (By similarity). The nucleoprotein protein N prevents excessive phosphorylation of P, which leads to down-regulation of viral transcription/ replication. Participates, together with N, in the formation of viral factories (viroplasms), which are large inclusions in the host cytoplasm where replication takes place (By similarity)"}]}
```

Source SHA-256: `56857522ea5f5b710f455232a0b818fb905cf20618243ede6b9fd62313bc5ed7`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/F8V2V0.json)  
**Locator:** `/uniProtKBCrossReferences/17`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:19.040321+00:00.  

```json
{"database":"GO","evidences":[{"evidenceCode":"ECO:0000314","id":"24501400","source":"PubMed"}],"id":"GO:0039689","properties":[{"key":"GoTerm","value":"P:negative stranded viral RNA replication"},{"key":"GoEvidenceType","value":"IDA:UniProtKB"}]}
```

Source SHA-256: `56857522ea5f5b710f455232a0b818fb905cf20618243ede6b9fd62313bc5ed7`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/F8V2V0.json)  
**Locator:** `/references/7`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:19.040321+00:00.  

```json
{"citation":{"authors":["Pickar A.","Xu P.","Elson A.","Li Z.","Zengel J.","He B."],"citationCrossReferences":[{"database":"PubMed","id":"24501400"},{"database":"DOI","id":"10.1128/jvi.03673-13"}],"citationType":"journal article","firstPage":"4414","id":"24501400","journal":"J. Virol.","lastPage":"4422","publicationDate":"2014","title":"Roles of serine and threonine residues of mumps virus P protein in viral transcription and replication.","volume":"88"},"referenceNumber":8,"referencePositions":["IDENTIFICATION BY MASS SPECTROMETRY","MUTAGENESIS OF THR-101","PHOSPHORYLATION AT THR-10; THR-16; THR-39; SER-69; THR-91; THR-150; THR-165; SER-188; THR-250; SER-257; THR-258; THR-282; SER-374 AND THR-375"]}
```

Source SHA-256: `56857522ea5f5b710f455232a0b818fb905cf20618243ede6b9fd62313bc5ed7`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/F8V2V0?format=txt&versions=45)  
**Locator:** `lines 1-12`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 45 / 1.  
**Retrieved:** 2026-11-02T04:28:21.959103+00:00.  

```text
ID   PHOSP_MUMPV             Reviewed;         391 AA.
AC   F8V2V0;
DT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.
DT   21-SEP-2011, sequence version 1.
DT   28-JAN-2026, entry version 45.
DE   RecName: Full=Phosphoprotein;
GN   Name=V/P; Synonyms=P, V;
OS   Mumps orthorubulavirus (MuV).
OC   Viruses; Riboviria; Orthornavirae; Negarnaviricota; Haploviricotina;
OC   Monjiviricetes; Mononegavirales; Paramyxoviridae; Rubulavirinae;
OC   Orthorubulavirus; Orthorubulavirus parotitidis.
OX   NCBI_TaxID=2560602;
```

Source SHA-256: `dd84ed0caab5d00246d29d76a498798af374cc0b04d5c2f26441769c2956c54e`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/F8V2V0?format=txt&versions=45)  
**Locator:** `lines 84-97`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 45 / 1.  
**Retrieved:** 2026-11-02T04:28:21.959103+00:00.  

```text
CC   -!- FUNCTION: Essential cofactor of the RNA polymerase L that plays a
CC       central role in the transcription and replication by forming the
CC       polymerase complex with RNA polymerase L and recruiting L to the
CC       genomic N-RNA template for RNA synthesis (By similarity). Also plays a
CC       central role in the encapsidation of nascent RNA chains by forming the
CC       encapsidation complex with the nucleocapsid protein N (N-P complex).
CC       Acts as a chaperone for newly synthesized free N protein, so-called N0,
CC       allowing encapsidation of nascent RNA chains during replication (By
CC       similarity). The nucleoprotein protein N prevents excessive
CC       phosphorylation of P, which leads to down-regulation of viral
CC       transcription/ replication. Participates, together with N, in the
CC       formation of viral factories (viroplasms), which are large inclusions
CC       in the host cytoplasm where replication takes place (By similarity).
CC       {ECO:0000250|UniProtKB:P06162, ECO:0000250|UniProtKB:P16072}.
```

Source SHA-256: `dd84ed0caab5d00246d29d76a498798af374cc0b04d5c2f26441769c2956c54e`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/F8V2V0?format=txt&versions=45)  
**Locator:** `lines 154-154`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 45 / 1.  
**Retrieved:** 2026-11-02T04:28:21.959103+00:00.  

```text
DR   GO; GO:0039689; P:negative stranded viral RNA replication; IDA:UniProtKB.
```

Source SHA-256: `dd84ed0caab5d00246d29d76a498798af374cc0b04d5c2f26441769c2956c54e`.

### Evidence GO3

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 232753-232761`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0039689
name: negative stranded viral RNA replication
namespace: biological_process
def: "A viral genome replication process where the template genome is negative stranded, single stranded RNA ((-)ssRNA)." [GOC:bf, GOC:jl, VZ:1096]
synonym: "(-)ss viral RNA replication" EXACT [VZ:1096]
xref: VZ:1096 "Negative stranded RNA virus replication"
is_a: GO:0039694 ! viral RNA genome replication

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_biological_process.json), zero-based source row 86. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
