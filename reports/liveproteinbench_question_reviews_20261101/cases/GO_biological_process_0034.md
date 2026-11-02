# GO_biological_process_0034

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_biological_process`  
**Author expected answer:** **A** — virion assembly

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MAGSQIKIPLPKPPDSDSQRLNAFPIIMAQEGKGRLLRQIRLRKILSGDPSDQQITFVNTYGFIRATPETSEFISESSPQKVTPVVTACMLSFGAGPVLEDPQHMLKALDQTDIRVRKTASDKEQILFEINRIPNLFRHHQISADHLIQASSDKYVKSPAKLIAGVNYIYCVTFLSVTVCSASLKFRVARPLLAARSRLVRAVQMEVLLRVTCKKDSQMAKSMLNDPEGEGCIASVWFHLCNLCKGRNKLRSYDENYFASKCRKMNLTVSIGDMWGPTILVHAGGHIPTTAKPFFNSRGWVCHPIHQSSPSLAKTLWSSGCEIKAASAILQGSDYASLAKTDDIIYSKIKVDKDAANYKGVSWSPFRKSASMSNL

[Multiple Choices]
A. virion assembly
B. protein urmylation
C. regulation of monoatomic ion transmembrane transport
D. [2Fe-2S] cluster assembly
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

> The exact sequence matches a UniProt entry identifying it as the mumps virus matrix protein, whose annotated function includes a crucial role in virus assembly. The virion-assembly GO annotation is computationally assigned by InterPro, and the function statement is transferred by similarity, so this supports the key but is not direct experimental evidence for this exact protein.

Citations as saved: [C3](#evidence-c3), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The choices describe distinct biological processes, but the supplied sequence alone does not provide a clear, generally recognizable feature that identifies this protein as a viral matrix protein or establishes its role in virion assembly.


**Missing item-specific fact**

> The protein-specific identification as a mumps virus matrix protein and its annotated role in virus assembly are needed to distinguish A.


**Reason**

> Choosing A depends on knowing or looking up the sequence's protein identity and functional annotation; those facts are not supplied in the question.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The sequence-matched annotation supports virion assembly, and the other options do not have comparable support in the supplied reviewer evidence.


### Important caveats

- Reviewer-only database identity and annotation evidence was not available to the evaluated model.
- The function annotation is transferred by similarity, while the GO annotation is computationally assigned; neither excerpt establishes direct experimental validation for this exact protein.
- The author’s exact source snapshot is unknown, although the sequence matches both the historical and current records examined.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The choices describe distinct biological processes, but the supplied sequence alone does not provide a clear, generally recognizable feature that identifies this protein as a viral matrix protein or establishes its role in virion assembly.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific identification as a mumps virus matrix protein and its annotated role in virus assembly are needed to distinguish A.",
    "reason": "Choosing A depends on knowing or looking up the sequence's protein identity and functional annotation; those facts are not supplied in the question."
  },
  "case_id": "GO_biological_process_0034",
  "expected_answer_check": {
    "evidence_ids": [
      "C3",
      "C4",
      "C5",
      "C6",
      "H1",
      "H2",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry identifying it as the mumps virus matrix protein, whose annotated function includes a crucial role in virus assembly. The virion-assembly GO annotation is computationally assigned by InterPro, and the function statement is transferred by similarity, so this supports the key but is not direct experimental evidence for this exact protein."
  },
  "important_caveats": [
    "Reviewer-only database identity and annotation evidence was not available to the evaluated model.",
    "The function annotation is transferred by similarity, while the GO annotation is computationally assigned; neither excerpt establishes direct experimental validation for this exact protein.",
    "The author’s exact source snapshot is unknown, although the sequence matches both the historical and current records examined."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence-matched annotation supports virion assembly, and the other options do not have comparable support in the supplied reviewer evidence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_biological_process_0034",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry identifying it as the mumps virus matrix protein, whose annotated function includes a crucial role in virus assembly. The virion-assembly GO annotation is computationally assigned by InterPro, and the function statement is transferred by similarity, so this supports the key but is not direct experimental evidence for this exact protein.",
    "evidence_ids": ["C3", "C4", "C5", "C6", "H1", "H2", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The choices describe distinct biological processes, but the supplied sequence alone does not provide a clear, generally recognizable feature that identifies this protein as a viral matrix protein or establishes its role in virion assembly.",
    "missing_item_specific_fact": "The protein-specific identification as a mumps virus matrix protein and its annotated role in virus assembly are needed to distinguish A.",
    "reason": "Choosing A depends on knowing or looking up the sequence's protein identity and functional annotation; those facts are not supplied in the question."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence-matched annotation supports virion assembly, and the other options do not have comparable support in the supplied reviewer evidence."
  },
  "important_caveats": [
    "Reviewer-only database identity and annotation evidence was not available to the evaluated model.",
    "The function annotation is transferred by similarity, while the GO annotation is computationally assigned; neither excerpt establishes direct experimental validation for this exact protein.",
    "The author’s exact source snapshot is unknown, although the sequence matches both the historical and current records examined."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry Q5SC54 identifies this 375-aa protein as the Matrix (M) protein of Mumps virus. The FUNCTION comment (C5/H2) states 'The M protein has a crucial role in virus assembly and interacts with the RNP complex as well as with the viral membrane.' The GO annotation GO:0019068 (virion assembly) is present (C6/H3) with evidence type IEA:InterPro. The GO term definition (GO1) matches the described role. Note: the evidence code is ECO:0000250 (inferred from similar protein Q9W850) and IEA:InterPro, indicating computational/transferred annotation rather than direct experimental evidence for this specific strain, but the annotation is consistent and well-supported by the known role of paramyxovirus M proteins.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H2](#evidence-h2), [H3](#evidence-h3), [GO1](#evidence-go1).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The protein sequence exhibits characteristics of a viral structural/adaptor protein: amphipathic helical regions (e.g., hydrophobic stretch 'VTFLSVTVCSASLKFRVARPLLAARSRLVRAVQMEVLLRVTCKK' suggesting membrane association), charged segments (RNP-interaction), no transmembrane domains, and no enzymatic catalytic motifs. Among the four options, three describe highly specific cellular molecular mechanisms: protein urmylation requires E1/E2/E3-like enzymatic domains; ion transport regulation requires channel or transporter regulatory domains; &#91;2Fe-2S&#93; cluster assembly requires ISC/SUF machinery components (e.g., scaffold proteins with conserved Cys-rich motifs). None of these domain architectures are present. The only option consistent with a non-enzymatic, membrane-associating structural protein is 'virion assembly,' which describes a structural/adaptor role in viral particle formation. Additionally, the 'GSDY' motif near the C-terminus is a recognized paramyxovirus M-protein signature.


**Missing item-specific fact**

> Exact recognition of the sequence as Mumps virus Matrix protein (UniProt Q5SC54) would require database lookup, but the general biological reasoning about viral structural protein architecture versus specific cellular enzymatic/regulatory pathways provides a defensible path to the answer.


**Reason**

> While precise protein identification requires lookup, the question provides meaningful grounds for elimination: the three distractors describe specific enzymatic or regulatory mechanisms whose domain requirements are absent from the sequence, while the remaining option (virion assembly) matches the structural/adaptor character of the protein. A knowledgeable model can reason from protein architecture to the correct category without memorizing the exact UniProt entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The three distractors (urmylation, ion transport regulation, Fe-S cluster assembly) are highly specific cellular processes with well-defined domain requirements that are clearly absent from this sequence. 'Virion assembly' is the only option describing a structural/adaptor role, making it uniquely defensible for a non-enzymatic, membrane-associating protein. No ambiguity among options.


### Important caveats

- The GO annotation evidence is IEA:InterPro (computational inference) and the function comment is ECO:0000250 (inferred from similar protein Q9W850, the Sendai virus M protein), not direct experimental evidence for this specific Mumps strain.
- The UniProt entry was first publicly released on 2025-04-09 (entry version 34); the historical archived version (32) was released 2026-01-28. The exact author source snapshot is unknown.
- The accession was inferred from dataset image-path metadata and was not provided to the evaluated model.
- The 'GSDY' motif recognition and paramyxovirus M-protein knowledge, while general virology, represents specialized domain knowledge that may not be universally available to all models.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The protein sequence exhibits characteristics of a viral structural/adaptor protein: amphipathic helical regions (e.g., hydrophobic stretch 'VTFLSVTVCSASLKFRVARPLLAARSRLVRAVQMEVLLRVTCKK' suggesting membrane association), charged segments (RNP-interaction), no transmembrane domains, and no enzymatic catalytic motifs. Among the four options, three describe highly specific cellular molecular mechanisms: protein urmylation requires E1/E2/E3-like enzymatic domains; ion transport regulation requires channel or transporter regulatory domains; [2Fe-2S] cluster assembly requires ISC/SUF machinery components (e.g., scaffold proteins with conserved Cys-rich motifs). None of these domain architectures are present. The only option consistent with a non-enzymatic, membrane-associating structural protein is 'virion assembly,' which describes a structural/adaptor role in viral particle formation. Additionally, the 'GSDY' motif near the C-terminus is a recognized paramyxovirus M-protein signature.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "Exact recognition of the sequence as Mumps virus Matrix protein (UniProt Q5SC54) would require database lookup, but the general biological reasoning about viral structural protein architecture versus specific cellular enzymatic/regulatory pathways provides a defensible path to the answer.",
    "reason": "While precise protein identification requires lookup, the question provides meaningful grounds for elimination: the three distractors describe specific enzymatic or regulatory mechanisms whose domain requirements are absent from the sequence, while the remaining option (virion assembly) matches the structural/adaptor character of the protein. A knowledgeable model can reason from protein architecture to the correct category without memorizing the exact UniProt entry."
  },
  "case_id": "GO_biological_process_0034",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H2",
      "H3",
      "GO1"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry Q5SC54 identifies this 375-aa protein as the Matrix (M) protein of Mumps virus. The FUNCTION comment (C5/H2) states 'The M protein has a crucial role in virus assembly and interacts with the RNP complex as well as with the viral membrane.' The GO annotation GO:0019068 (virion assembly) is present (C6/H3) with evidence type IEA:InterPro. The GO term definition (GO1) matches the described role. Note: the evidence code is ECO:0000250 (inferred from similar protein Q9W850) and IEA:InterPro, indicating computational/transferred annotation rather than direct experimental evidence for this specific strain, but the annotation is consistent and well-supported by the known role of paramyxovirus M proteins."
  },
  "important_caveats": [
    "The GO annotation evidence is IEA:InterPro (computational inference) and the function comment is ECO:0000250 (inferred from similar protein Q9W850, the Sendai virus M protein), not direct experimental evidence for this specific Mumps strain.",
    "The UniProt entry was first publicly released on 2025-04-09 (entry version 34); the historical archived version (32) was released 2026-01-28. The exact author source snapshot is unknown.",
    "The accession was inferred from dataset image-path metadata and was not provided to the evaluated model.",
    "The 'GSDY' motif recognition and paramyxovirus M-protein knowledge, while general virology, represents specialized domain knowledge that may not be universally available to all models."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The three distractors (urmylation, ion transport regulation, Fe-S cluster assembly) are highly specific cellular processes with well-defined domain requirements that are clearly absent from this sequence. 'Virion assembly' is the only option describing a structural/adaptor role, making it uniquely defensible for a non-enzymatic, membrane-associating protein. No ambiguity among options."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_biological_process_0034",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry Q5SC54 identifies this 375-aa protein as the Matrix (M) protein of Mumps virus. The FUNCTION comment (C5/H2) states 'The M protein has a crucial role in virus assembly and interacts with the RNP complex as well as with the viral membrane.' The GO annotation GO:0019068 (virion assembly) is present (C6/H3) with evidence type IEA:InterPro. The GO term definition (GO1) matches the described role. Note: the evidence code is ECO:0000250 (inferred from similar protein Q9W850) and IEA:InterPro, indicating computational/transferred annotation rather than direct experimental evidence for this specific strain, but the annotation is consistent and well-supported by the known role of paramyxovirus M proteins.",
    "evidence_ids": ["C4", "C5", "C6", "H2", "H3", "GO1"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The protein sequence exhibits characteristics of a viral structural/adaptor protein: amphipathic helical regions (e.g., hydrophobic stretch 'VTFLSVTVCSASLKFRVARPLLAARSRLVRAVQMEVLLRVTCKK' suggesting membrane association), charged segments (RNP-interaction), no transmembrane domains, and no enzymatic catalytic motifs. Among the four options, three describe highly specific cellular molecular mechanisms: protein urmylation requires E1/E2/E3-like enzymatic domains; ion transport regulation requires channel or transporter regulatory domains; [2Fe-2S] cluster assembly requires ISC/SUF machinery components (e.g., scaffold proteins with conserved Cys-rich motifs). None of these domain architectures are present. The only option consistent with a non-enzymatic, membrane-associating structural protein is 'virion assembly,' which describes a structural/adaptor role in viral particle formation. Additionally, the 'GSDY' motif near the C-terminus is a recognized paramyxovirus M-protein signature.",
    "missing_item_specific_fact": "Exact recognition of the sequence as Mumps virus Matrix protein (UniProt Q5SC54) would require database lookup, but the general biological reasoning about viral structural protein architecture versus specific cellular enzymatic/regulatory pathways provides a defensible path to the answer.",
    "reason": "While precise protein identification requires lookup, the question provides meaningful grounds for elimination: the three distractors describe specific enzymatic or regulatory mechanisms whose domain requirements are absent from the sequence, while the remaining option (virion assembly) matches the structural/adaptor character of the protein. A knowledgeable model can reason from protein architecture to the correct category without memorizing the exact UniProt entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The three distractors (urmylation, ion transport regulation, Fe-S cluster assembly) are highly specific cellular processes with well-defined domain requirements that are clearly absent from this sequence. 'Virion assembly' is the only option describing a structural/adaptor role, making it uniquely defensible for a non-enzymatic, membrane-associating protein. No ambiguity among options."
  },
  "important_caveats": [
    "The GO annotation evidence is IEA:InterPro (computational inference) and the function comment is ECO:0000250 (inferred from similar protein Q9W850, the Sendai virus M protein), not direct experimental evidence for this specific Mumps strain.",
    "The UniProt entry was first publicly released on 2025-04-09 (entry version 34); the historical archived version (32) was released 2026-01-28. The exact author source snapshot is unknown.",
    "The accession was inferred from dataset image-path metadata and was not provided to the evaluated model.",
    "The 'GSDY' motif recognition and paramyxovirus M-protein knowledge, while general virology, represents specialized domain knowledge that may not be universally available to all models."
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

**Accession:** `Q5SC54` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 32. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5SC54.json)  
**Locator:** `/organism`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:31.669710+00:00.  

```json
{"commonName":"MuV","lineage":["Viruses","Riboviria","Orthornavirae","Negarnaviricota","Haploviricotina","Monjiviricetes","Mononegavirales","Paramyxoviridae","Rubulavirinae","Orthorubulavirus","Orthorubulavirus parotitidis","Mumps orthorubulavirus"],"scientificName":"Mumps virus genotype N (strain L-Zagreb vaccine)","taxonId":301186}
```

Source SHA-256: `166dfef0065f5b43e0c10d95199121285d4e73edccaa487cd0bfe2f64dac34fa`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5SC54.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:31.669710+00:00.  

```json
{"recommendedName":{"fullName":{"value":"Matrix protein"}}}
```

Source SHA-256: `166dfef0065f5b43e0c10d95199121285d4e73edccaa487cd0bfe2f64dac34fa`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5SC54.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:31.669710+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q9W850","source":"UniProtKB"}],"value":"The M protein has a crucial role in virus assembly and interacts with the RNP complex as well as with the viral membrane"}]}
```

Source SHA-256: `166dfef0065f5b43e0c10d95199121285d4e73edccaa487cd0bfe2f64dac34fa`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5SC54.json)  
**Locator:** `/uniProtKBCrossReferences/5`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:31.669710+00:00.  

```json
{"database":"GO","id":"GO:0019068","properties":[{"key":"GoTerm","value":"P:virion assembly"},{"key":"GoEvidenceType","value":"IEA:InterPro"}]}
```

Source SHA-256: `166dfef0065f5b43e0c10d95199121285d4e73edccaa487cd0bfe2f64dac34fa`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5SC54?format=txt&versions=32)  
**Locator:** `lines 1-13`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 32 / 1.  
**Retrieved:** 2026-11-02T04:31:33.730421+00:00.  

```text
ID   MATRX_MUMPZ             Reviewed;         375 AA.
AC   Q5SC54;
DT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.
DT   21-DEC-2004, sequence version 1.
DT   28-JAN-2026, entry version 32.
DE   RecName: Full=Matrix protein;
GN   Name=M;
OS   Mumps virus genotype N (strain L-Zagreb vaccine) (MuV).
OC   Viruses; Riboviria; Orthornavirae; Negarnaviricota; Haploviricotina;
OC   Monjiviricetes; Mononegavirales; Paramyxoviridae; Rubulavirinae;
OC   Orthorubulavirus; Orthorubulavirus parotitidis; Mumps orthorubulavirus.
OX   NCBI_TaxID=301186;
OH   NCBI_TaxID=9606; Homo sapiens (Human).
```

Source SHA-256: `d586fa1cdf94fd272203045de450655195b9c5ea2cadbc746fdf7bb17530f1b4`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5SC54?format=txt&versions=32)  
**Locator:** `lines 40-42`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 32 / 1.  
**Retrieved:** 2026-11-02T04:31:33.730421+00:00.  

```text
CC   -!- FUNCTION: The M protein has a crucial role in virus assembly and
CC       interacts with the RNP complex as well as with the viral membrane.
CC       {ECO:0000250|UniProtKB:Q9W850}.
```

Source SHA-256: `d586fa1cdf94fd272203045de450655195b9c5ea2cadbc746fdf7bb17530f1b4`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5SC54?format=txt&versions=32)  
**Locator:** `lines 58-58`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 32 / 1.  
**Retrieved:** 2026-11-02T04:31:33.730421+00:00.  

```text
DR   GO; GO:0019068; P:virion assembly; IEA:InterPro.
```

Source SHA-256: `d586fa1cdf94fd272203045de450655195b9c5ea2cadbc746fdf7bb17530f1b4`.

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 145078-145098`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0019068
name: virion assembly
namespace: biological_process
alt_id: GO:0042963
def: "A late phase of the viral life cycle during which all the components necessary for the formation of a mature virion collect at a particular site in the cell and the basic structure of the virus particle is formed." [ISBN:0121585336]
subset: goslim_virus
synonym: "bacteriophage assembly" NARROW [GOC:bm]
synonym: "phage assembly" NARROW [GOC:bm]
synonym: "viral assembly" EXACT []
synonym: "viral particle assembly" EXACT []
synonym: "virion assembly and maintenance" EXACT [GOC:bf, GOC:jl]
synonym: "virion organization" EXACT [GOC:bf, GOC:jl]
synonym: "virus assembly" EXACT [GOC:dph, GOC:tb]
synonym: "virus particle assembly" EXACT []
xref: Reactome:R-HSA-168302 "Budding"
xref: Reactome:R-HSA-168316 "Assembly of Viral Components at the Budding Site"
xref: Reactome:R-HSA-175474 "Assembly Of The HIV Virion"
is_a: GO:0016032 ! viral process
relationship: part_of GO:0019058 ! viral life cycle

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_biological_process.json), zero-based source row 34. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
