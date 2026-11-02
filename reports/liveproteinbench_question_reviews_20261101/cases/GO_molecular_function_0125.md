# GO_molecular_function_0125

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_molecular_function`  
**Author expected answer:** **C** — RNA binding

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MWPNLFWGFDAYDGSNFNAFPIYFPTEFMQTEPRDQSSCQQLSMEQATEPSMNPDQEDIVEGGENYGELSNQQETVPSFENADQNLSRLEMSTLARELKEKVKQSRALRQSVNNAAEQQPSTKPQPVQQEVQDLINDILKSQDQDDNLKNPSKLTGPQDDTETEKPASTLPTTPRTIKESPLSTYSIPVYCPASPEGRTHIPDEILDNAPKGPRHTHRGQVQMFCNGECGRRETDKAMPAIEPSDKTEETEGATAVRIPPVATDGDLEQDVIMWLRHTGFYDKAKRTDALARWKQLAKMEQGLARPQQDHQEAGVALASASQGSKEAGMGTRPGPDADCPPVCRPEQGGPGSSQAALSCKSKQSTDIQRATLAETRGGSLRDRAANQQPSKKSDRGRCARRHRSSSPRGRSGSHKSRRATTDSPVSRSTTKSTPSRARQPGHRDYREYRDDRNRDTKPRSPLVSCRAAVAFNPGVKGAPLVRQRFRPRQTNTDLQHKARIVGAPPRDMESNIKERQNHDPERQSGQFGIRWLCTSPLALQNTKSLRNSFDDLKPVLLGRDGQEMDDYCGRDLLRLMDASERGLHRP

[Multiple Choices]
A. magnesium ion binding
B. olfactory receptor activity
C. RNA binding
D. nicotinate-nucleotide adenylyltransferase activity
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

> The exact sequence matches a fungal YTH2 protein annotated to bind RNA; its annotation specifically describes recognition of m6A-containing mRNAs. The RNA-binding GO annotation is computationally assigned by InterPro, while the specific m6A-binding statement is supported by similarity, so this is not direct experimental proof for this protein.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence lacks the hydrophobic transmembrane pattern expected of an olfactory receptor and does not obviously resemble the specified metabolic enzyme; its basic, low-complexity regions could be compatible with nucleic-acid interaction. But these clues do not establish RNA binding or distinguish it reliably from other binding functions.


**Missing item-specific fact**

> Identifying the protein as a YTH-domain-containing RNA reader, or otherwise recognizing the YTH domain and its RNA-binding function, requires protein-specific domain or annotation knowledge not supplied in the question.


**Reason**

> The sequence and choices provide some weak grounds against two distractors, but not enough to infer the specific RNA-binding function. The decisive YTH identity and function are item-specific facts absent from the input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> RNA binding is the only choice supported by the matched sequence’s available functional annotation; the other choices are not comparably supported.


### Important caveats

- The sequence match is exact, but the author’s source snapshot is unknown.
- The RNA-binding GO annotation is IEA:InterPro, and the specific m6A-recognition claim is annotated by similarity; the supplied evidence does not establish a direct binding experiment on this exact protein.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence lacks the hydrophobic transmembrane pattern expected of an olfactory receptor and does not obviously resemble the specified metabolic enzyme; its basic, low-complexity regions could be compatible with nucleic-acid interaction. But these clues do not establish RNA binding or distinguish it reliably from other binding functions.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "Identifying the protein as a YTH-domain-containing RNA reader, or otherwise recognizing the YTH domain and its RNA-binding function, requires protein-specific domain or annotation knowledge not supplied in the question.",
    "reason": "The sequence and choices provide some weak grounds against two distractors, but not enough to infer the specific RNA-binding function. The decisive YTH identity and function are item-specific facts absent from the input."
  },
  "case_id": "GO_molecular_function_0125",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches a fungal YTH2 protein annotated to bind RNA; its annotation specifically describes recognition of m6A-containing mRNAs. The RNA-binding GO annotation is computationally assigned by InterPro, while the specific m6A-binding statement is supported by similarity, so this is not direct experimental proof for this protein."
  },
  "important_caveats": [
    "The sequence match is exact, but the author’s source snapshot is unknown.",
    "The RNA-binding GO annotation is IEA:InterPro, and the specific m6A-recognition claim is annotated by similarity; the supplied evidence does not establish a direct binding experiment on this exact protein."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "RNA binding is the only choice supported by the matched sequence’s available functional annotation; the other choices are not comparably supported."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0125",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches a fungal YTH2 protein annotated to bind RNA; its annotation specifically describes recognition of m6A-containing mRNAs. The RNA-binding GO annotation is computationally assigned by InterPro, while the specific m6A-binding statement is supported by similarity, so this is not direct experimental proof for this protein.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence lacks the hydrophobic transmembrane pattern expected of an olfactory receptor and does not obviously resemble the specified metabolic enzyme; its basic, low-complexity regions could be compatible with nucleic-acid interaction. But these clues do not establish RNA binding or distinguish it reliably from other binding functions.",
    "missing_item_specific_fact": "Identifying the protein as a YTH-domain-containing RNA reader, or otherwise recognizing the YTH domain and its RNA-binding function, requires protein-specific domain or annotation knowledge not supplied in the question.",
    "reason": "The sequence and choices provide some weak grounds against two distractors, but not enough to infer the specific RNA-binding function. The decisive YTH identity and function are item-specific facts absent from the input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "RNA binding is the only choice supported by the matched sequence’s available functional annotation; the other choices are not comparably supported."
  },
  "important_caveats": [
    "The sequence match is exact, but the author’s source snapshot is unknown.",
    "The RNA-binding GO annotation is IEA:InterPro, and the specific m6A-recognition claim is annotated by similarity; the supplied evidence does not establish a direct binding experiment on this exact protein."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry G4NB33 (YTH2_PYRO7, YTH domain-containing family protein 2 from Pyricularia oryzae) annotates GO:0003723 (RNA binding) with evidence code IEA:InterPro (C6/H4). The FUNCTION comment (C5/H3) states the protein 'Specifically recognizes and binds N6-methyladenosine (m6A)-containing mRNAs,' supported by both by-similarity evidence (ECO:0000250) and experimental evidence from PubMed:30535195 (ECO:0000269). The YTH domain is a well-characterized m6A RNA-reader module. The sequence matches the canonical entry exactly (586 AA, SHA-256 match). The GO annotation is computational (IEA via InterPro), but the functional description has experimental backing. RNA binding is the correct primary molecular function.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H3](#evidence-h3), [H4](#evidence-h4), [GO2](#evidence-go2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence (~586 AA) lacks the seven hydrophobic transmembrane helices (~20-25 residues each) characteristic of GPCR-family olfactory receptors (GO:0004984), eliminating B. It lacks the well-defined catalytic motifs of nicotinate-nucleotide adenylyltransferase (EC 2.7.7.18, a transferase with specific Rossmann-like fold motifs), eliminating D. It lacks a dedicated, geometrically specific Mg²⁺ coordination site (e.g., EF-hand, DxDxDG-type motif) that would make magnesium ion binding its primary molecular function, eliminating A. The remaining sequence shows a domain-like region with conserved aromatic residues (Trp, Tyr, Phe) arranged in a manner consistent with nucleobase-stacking interactions typical of RNA-binding proteins, supporting C as the best answer by elimination and by positive aromatic-cage features.


**Missing item-specific fact**

> Positive identification of the YTH domain consensus sequence and its specific m6A-recognition aromatic cage would require prior domain knowledge, but the elimination of the three incompatible options relies on general protein-architecture knowledge (7-TM topology, transferase motifs, metal-coordination geometry).


**Reason**

> The three distractors can be eliminated using general structural biology knowledge: olfactory receptors are 7-TM GPCRs (absent here), adenylyltransferase is a specific enzyme class with recognizable catalytic motifs (absent here), and dedicated Mg²⁺ binding requires specific coordination geometry (absent as a primary function). This leaves RNA binding as the only viable option, and the aromatic residue pattern provides weak positive support. The reasoning does not require memorizing this specific protein's database entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options B and D are clearly incompatible with the sequence architecture (no 7-TM pattern, no transferase motifs). Option A is unlikely as a primary molecular function without a dedicated coordination site. Option C is the only remaining defensible choice.


### Important caveats

- The GO:0003723 annotation in UniProt is IEA (Inferred from Electronic Annotation) via InterPro, not a direct experimental GO annotation. However, the functional characterization in the entry has experimental support (PubMed:30535195).
- The reviewer-only evidence was not available to the evaluated model; the reasoning assessment is based solely on what could be inferred from the sequence and general biological knowledge.
- The YTH domain is not as immediately recognizable from primary sequence as, e.g., a kinase or zinc-finger domain; positive identification relies on recognizing aromatic residue patterns consistent with nucleic-acid binding, which is weaker than the elimination arguments for the distractors.
- The UniProt entry was first released 2025-04-09; the benchmark construction date is unknown, so the annotation may not have been available at question-creation time, though the sequence itself is unchanged since 2011.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence (~586 AA) lacks the seven hydrophobic transmembrane helices (~20-25 residues each) characteristic of GPCR-family olfactory receptors (GO:0004984), eliminating B. It lacks the well-defined catalytic motifs of nicotinate-nucleotide adenylyltransferase (EC 2.7.7.18, a transferase with specific Rossmann-like fold motifs), eliminating D. It lacks a dedicated, geometrically specific Mg²⁺ coordination site (e.g., EF-hand, DxDxDG-type motif) that would make magnesium ion binding its primary molecular function, eliminating A. The remaining sequence shows a domain-like region with conserved aromatic residues (Trp, Tyr, Phe) arranged in a manner consistent with nucleobase-stacking interactions typical of RNA-binding proteins, supporting C as the best answer by elimination and by positive aromatic-cage features.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "Positive identification of the YTH domain consensus sequence and its specific m6A-recognition aromatic cage would require prior domain knowledge, but the elimination of the three incompatible options relies on general protein-architecture knowledge (7-TM topology, transferase motifs, metal-coordination geometry).",
    "reason": "The three distractors can be eliminated using general structural biology knowledge: olfactory receptors are 7-TM GPCRs (absent here), adenylyltransferase is a specific enzyme class with recognizable catalytic motifs (absent here), and dedicated Mg²⁺ binding requires specific coordination geometry (absent as a primary function). This leaves RNA binding as the only viable option, and the aromatic residue pattern provides weak positive support. The reasoning does not require memorizing this specific protein's database entry."
  },
  "case_id": "GO_molecular_function_0125",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H1",
      "H3",
      "H4",
      "GO2"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry G4NB33 (YTH2_PYRO7, YTH domain-containing family protein 2 from Pyricularia oryzae) annotates GO:0003723 (RNA binding) with evidence code IEA:InterPro (C6/H4). The FUNCTION comment (C5/H3) states the protein 'Specifically recognizes and binds N6-methyladenosine (m6A)-containing mRNAs,' supported by both by-similarity evidence (ECO:0000250) and experimental evidence from PubMed:30535195 (ECO:0000269). The YTH domain is a well-characterized m6A RNA-reader module. The sequence matches the canonical entry exactly (586 AA, SHA-256 match). The GO annotation is computational (IEA via InterPro), but the functional description has experimental backing. RNA binding is the correct primary molecular function."
  },
  "important_caveats": [
    "The GO:0003723 annotation in UniProt is IEA (Inferred from Electronic Annotation) via InterPro, not a direct experimental GO annotation. However, the functional characterization in the entry has experimental support (PubMed:30535195).",
    "The reviewer-only evidence was not available to the evaluated model; the reasoning assessment is based solely on what could be inferred from the sequence and general biological knowledge.",
    "The YTH domain is not as immediately recognizable from primary sequence as, e.g., a kinase or zinc-finger domain; positive identification relies on recognizing aromatic residue patterns consistent with nucleic-acid binding, which is weaker than the elimination arguments for the distractors.",
    "The UniProt entry was first released 2025-04-09; the benchmark construction date is unknown, so the annotation may not have been available at question-creation time, though the sequence itself is unchanged since 2011."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options B and D are clearly incompatible with the sequence architecture (no 7-TM pattern, no transferase motifs). Option A is unlikely as a primary molecular function without a dedicated coordination site. Option C is the only remaining defensible choice."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0125",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry G4NB33 (YTH2_PYRO7, YTH domain-containing family protein 2 from Pyricularia oryzae) annotates GO:0003723 (RNA binding) with evidence code IEA:InterPro (C6/H4). The FUNCTION comment (C5/H3) states the protein 'Specifically recognizes and binds N6-methyladenosine (m6A)-containing mRNAs,' supported by both by-similarity evidence (ECO:0000250) and experimental evidence from PubMed:30535195 (ECO:0000269). The YTH domain is a well-characterized m6A RNA-reader module. The sequence matches the canonical entry exactly (586 AA, SHA-256 match). The GO annotation is computational (IEA via InterPro), but the functional description has experimental backing. RNA binding is the correct primary molecular function.",
    "evidence_ids": ["C4", "C5", "C6", "H1", "H3", "H4", "GO2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence (~586 AA) lacks the seven hydrophobic transmembrane helices (~20-25 residues each) characteristic of GPCR-family olfactory receptors (GO:0004984), eliminating B. It lacks the well-defined catalytic motifs of nicotinate-nucleotide adenylyltransferase (EC 2.7.7.18, a transferase with specific Rossmann-like fold motifs), eliminating D. It lacks a dedicated, geometrically specific Mg²⁺ coordination site (e.g., EF-hand, DxDxDG-type motif) that would make magnesium ion binding its primary molecular function, eliminating A. The remaining sequence shows a domain-like region with conserved aromatic residues (Trp, Tyr, Phe) arranged in a manner consistent with nucleobase-stacking interactions typical of RNA-binding proteins, supporting C as the best answer by elimination and by positive aromatic-cage features.",
    "missing_item_specific_fact": "Positive identification of the YTH domain consensus sequence and its specific m6A-recognition aromatic cage would require prior domain knowledge, but the elimination of the three incompatible options relies on general protein-architecture knowledge (7-TM topology, transferase motifs, metal-coordination geometry).",
    "reason": "The three distractors can be eliminated using general structural biology knowledge: olfactory receptors are 7-TM GPCRs (absent here), adenylyltransferase is a specific enzyme class with recognizable catalytic motifs (absent here), and dedicated Mg²⁺ binding requires specific coordination geometry (absent as a primary function). This leaves RNA binding as the only viable option, and the aromatic residue pattern provides weak positive support. The reasoning does not require memorizing this specific protein's database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options B and D are clearly incompatible with the sequence architecture (no 7-TM pattern, no transferase motifs). Option A is unlikely as a primary molecular function without a dedicated coordination site. Option C is the only remaining defensible choice."
  },
  "important_caveats": [
    "The GO:0003723 annotation in UniProt is IEA (Inferred from Electronic Annotation) via InterPro, not a direct experimental GO annotation. However, the functional characterization in the entry has experimental support (PubMed:30535195).",
    "The reviewer-only evidence was not available to the evaluated model; the reasoning assessment is based solely on what could be inferred from the sequence and general biological knowledge.",
    "The YTH domain is not as immediately recognizable from primary sequence as, e.g., a kinase or zinc-finger domain; positive identification relies on recognizing aromatic residue patterns consistent with nucleic-acid binding, which is weaker than the elimination arguments for the distractors.",
    "The UniProt entry was first released 2025-04-09; the benchmark construction date is unknown, so the annotation may not have been available at question-creation time, though the sequence itself is unchanged since 2011."
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

**Accession:** `G4NB33` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 42. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G4NB33.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:07.149739+00:00.  

```json
"G4NB33"
```

Source SHA-256: `12d384b1b63c01ae54789687c2477c5a4dedf554ec7ee6db71b77e36b31c2d45`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G4NB33.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:07.149739+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"M6A reader YTH2"}}],"recommendedName":{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"30535195","source":"PubMed"}],"value":"YTH domain-containing family protein 2"}}}
```

Source SHA-256: `12d384b1b63c01ae54789687c2477c5a4dedf554ec7ee6db71b77e36b31c2d45`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G4NB33.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:07.149739+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"A0A9P4XWM4","source":"UniProtKB"},{"evidenceCode":"ECO:0000269","id":"30535195","source":"PubMed"}],"value":"Specifically recognizes and binds N6-methyladenosine (m6A)-containing mRNAs, and regulates their stability (By similarity). M6A is a modification present at internal sites of mRNAs and some non-coding RNAs and plays a role in mRNA stability and processing (By similarity). Plays a role in pathogenicity towards plant host (PubMed:30535195)"}]}
```

Source SHA-256: `12d384b1b63c01ae54789687c2477c5a4dedf554ec7ee6db71b77e36b31c2d45`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G4NB33.json)  
**Locator:** `/uniProtKBCrossReferences/12`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:07.149739+00:00.  

```json
{"database":"GO","id":"GO:0003723","properties":[{"key":"GoTerm","value":"F:RNA binding"},{"key":"GoEvidenceType","value":"IEA:InterPro"}]}
```

Source SHA-256: `12d384b1b63c01ae54789687c2477c5a4dedf554ec7ee6db71b77e36b31c2d45`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G4NB33?format=txt&versions=42)  
**Locator:** `lines 1-13`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 42 / 1.  
**Retrieved:** 2026-11-01T06:28:05.832385+00:00.  

```text
ID   YTH2_PYRO7              Reviewed;         586 AA.
AC   G4NB33;
DT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.
DT   14-DEC-2011, sequence version 1.
DT   28-JAN-2026, entry version 42.
DE   RecName: Full=YTH domain-containing family protein 2 {ECO:0000303|PubMed:30535195};
DE   AltName: Full=M6A reader YTH2 {ECO:0000305};
GN   Name=YTH2 {ECO:0000303|PubMed:30535195}; ORFNames=MGG_00637;
OS   Pyricularia oryzae (strain 70-15 / ATCC MYA-4617 / FGSC 8958) (Rice blast
OS   fungus) (Magnaporthe oryzae).
OC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Sordariomycetes;
OC   Sordariomycetidae; Magnaporthales; Pyriculariaceae; Pyricularia.
OX   NCBI_TaxID=242507;
```

Source SHA-256: `230bc6ccb816d8ed7059ee0b42ed0d37caff3a2e8ab4e2e4c89efbb6f5954ec2`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G4NB33?format=txt&versions=42)  
**Locator:** `lines 33-38`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 42 / 1.  
**Retrieved:** 2026-11-01T06:28:05.832385+00:00.  

```text
CC   -!- FUNCTION: Specifically recognizes and binds N6-methyladenosine (m6A)-
CC       containing mRNAs, and regulates their stability (By similarity). M6A is
CC       a modification present at internal sites of mRNAs and some non-coding
CC       RNAs and plays a role in mRNA stability and processing (By similarity).
CC       Plays a role in pathogenicity towards plant host (PubMed:30535195).
CC       {ECO:0000250|UniProtKB:A0A9P4XWM4, ECO:0000269|PubMed:30535195}.
```

Source SHA-256: `230bc6ccb816d8ed7059ee0b42ed0d37caff3a2e8ab4e2e4c89efbb6f5954ec2`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G4NB33?format=txt&versions=42)  
**Locator:** `lines 61-61`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 42 / 1.  
**Retrieved:** 2026-11-01T06:28:05.832385+00:00.  

```text
DR   GO; GO:0003723; F:RNA binding; IEA:InterPro.
```

Source SHA-256: `230bc6ccb816d8ed7059ee0b42ed0d37caff3a2e8ab4e2e4c89efbb6f5954ec2`.

### Evidence GO2

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 28242-28268`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0003723
name: RNA binding
namespace: molecular_function
alt_id: GO:0000498
alt_id: GO:0044822
def: "Binding to an RNA molecule or a portion thereof." [GOC:jl, GOC:mah]
subset: goslim_agr
subset: goslim_candida
subset: goslim_chembl
subset: goslim_drosophila
subset: goslim_euk_cellular_processes_ribbon
subset: goslim_flybase_ribbon
subset: goslim_generic
subset: goslim_mouse
subset: goslim_plant
subset: goslim_plant_ribbon
subset: goslim_prokaryote
subset: goslim_prokaryote_ribbon
subset: goslim_yeast
synonym: "base pairing with RNA" NARROW []
synonym: "poly(A) RNA binding" RELATED []
synonym: "poly(A)-RNA binding" RELATED []
synonym: "poly-A RNA binding" RELATED []
xref: Reactome:R-HSA-203922 "Exportin-5 recognizes 3' overhang of pre-miRNA"
is_a: GO:0003676 ! nucleic acid binding

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 125. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
