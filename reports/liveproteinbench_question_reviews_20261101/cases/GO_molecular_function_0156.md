# GO_molecular_function_0156

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_molecular_function`  
**Author expected answer:** **D** — ABC-type transporter activity

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MTTLDLTARSDRGRVYWLLADCWNIVRRGLTHYQRQPVNIAWQLGFPILSVLLYGYVFGSAMKVPGGGDYKDFLMPGMFVMTMAFGFINTATLVVYDSTKGVIDRFRSMPMASSAVVAGRGVTDLITACAELAIMMLTAFAMGWRPDGGLGFLGAFGLLLWLRFALIWIGVWLGLLVPNPEAAGGLFAVAFPLTMISSIMVAPQLMPDWLGWVAMWNPISSTAAATRELFGTPVGGDTWVEQHALLMAGVWPVILTLVFLPLAVRRFKKLSR

[Multiple Choices]
A. transcription coregulator activity
B. damaged DNA binding
C. structural constituent of cell wall
D. ABC-type transporter activity
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

> The supplied sequence matches UniProt entry P0DXU6. Its annotation identifies it as the DrrB2 permease of an ABC transporter, and the cited study reports its involvement in daunorubicin efflux; the entry says it is responsible for substrate translocation across the membrane (qualified as probable). The specific GO annotation is computational (IEA:InterPro), distinct from the cited functional evidence.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The many hydrophobic stretches support an integral membrane protein and make the transcription, damaged-DNA-binding, and cell-wall options poor fits. They do not establish that this membrane protein belongs to an ABC transporter.


**Missing item-specific fact**

> The protein-specific identification as DrrB2, a permease component of the DrrA2B2 ABC transporter involved in daunorubicin efflux, is absent from the input.


**Reason**

> The sequence gives a general membrane-protein clue, but lacks an evident ATP-binding cassette domain or other supplied context that identifies ABC-type transport specifically. Choosing D over other possible membrane-transport functions requires protein-specific family or annotation information.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The evidence supports D; the other options do not fit the matched protein's identified function. The lack of ABC-specific evidence in the sequence makes the task lookup-dependent, but does not make another listed option defensible.


### Important caveats

- The cited GO term is annotated with computational evidence (IEA:InterPro), whereas the functional comment cites a publication for involvement in efflux and qualifies direct translocation as probable.
- The protein is described as a permease component of an ABC transporter complex; this does not imply that this sequence alone contains the complex's ATP-hydrolyzing nucleotide-binding domains.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The many hydrophobic stretches support an integral membrane protein and make the transcription, damaged-DNA-binding, and cell-wall options poor fits. They do not establish that this membrane protein belongs to an ABC transporter.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific identification as DrrB2, a permease component of the DrrA2B2 ABC transporter involved in daunorubicin efflux, is absent from the input.",
    "reason": "The sequence gives a general membrane-protein clue, but lacks an evident ATP-binding cassette domain or other supplied context that identifies ABC-type transport specifically. Choosing D over other possible membrane-transport functions requires protein-specific family or annotation information."
  },
  "case_id": "GO_molecular_function_0156",
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
    "reason": "The supplied sequence matches UniProt entry P0DXU6. Its annotation identifies it as the DrrB2 permease of an ABC transporter, and the cited study reports its involvement in daunorubicin efflux; the entry says it is responsible for substrate translocation across the membrane (qualified as probable). The specific GO annotation is computational (IEA:InterPro), distinct from the cited functional evidence."
  },
  "important_caveats": [
    "The cited GO term is annotated with computational evidence (IEA:InterPro), whereas the functional comment cites a publication for involvement in efflux and qualifies direct translocation as probable.",
    "The protein is described as a permease component of an ABC transporter complex; this does not imply that this sequence alone contains the complex's ATP-hydrolyzing nucleotide-binding domains."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The evidence supports D; the other options do not fit the matched protein's identified function. The lack of ABC-specific evidence in the sequence makes the task lookup-dependent, but does not make another listed option defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0156",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence matches UniProt entry P0DXU6. Its annotation identifies it as the DrrB2 permease of an ABC transporter, and the cited study reports its involvement in daunorubicin efflux; the entry says it is responsible for substrate translocation across the membrane (qualified as probable). The specific GO annotation is computational (IEA:InterPro), distinct from the cited functional evidence.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The many hydrophobic stretches support an integral membrane protein and make the transcription, damaged-DNA-binding, and cell-wall options poor fits. They do not establish that this membrane protein belongs to an ABC transporter.",
    "missing_item_specific_fact": "The protein-specific identification as DrrB2, a permease component of the DrrA2B2 ABC transporter involved in daunorubicin efflux, is absent from the input.",
    "reason": "The sequence gives a general membrane-protein clue, but lacks an evident ATP-binding cassette domain or other supplied context that identifies ABC-type transport specifically. Choosing D over other possible membrane-transport functions requires protein-specific family or annotation information."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The evidence supports D; the other options do not fit the matched protein's identified function. The lack of ABC-specific evidence in the sequence makes the task lookup-dependent, but does not make another listed option defensible."
  },
  "important_caveats": [
    "The cited GO term is annotated with computational evidence (IEA:InterPro), whereas the functional comment cites a publication for involvement in efflux and qualifies direct translocation as probable.",
    "The protein is described as a permease component of an ABC transporter complex; this does not imply that this sequence alone contains the complex's ATP-hydrolyzing nucleotide-binding domains."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry P0DXU6 (sequence SHA256 match confirmed) annotates this protein as 'Daunorubicin resistance ABC transporter permease protein DrrB2' with GO:0140359 'ABC-type transporter activity' (IEA:InterPro). The functional comment is supported by experimental evidence (ECO:0000269, PubMed:39375957): 'Part of the ABC transporter complex DrrA2B2 involved in daunorubicin efflux.' The GO term GO:0140359 definition matches option D exactly. The sequence is 272 AA, matching the benchmark input.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H3](#evidence-h3), [H4](#evidence-h4), [GO4](#evidence-go4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 272-residue sequence is overwhelmingly hydrophobic (dominated by L, V, I, F, A, W, M, G) with multiple extended hydrophobic stretches consistent with 10+ transmembrane helices, characteristic of a multi-pass membrane permease. This biophysical profile is fundamentally incompatible with: (A) transcription coregulator activity (requires protein-protein/DNA interaction domains, not TM helices); (B) damaged DNA binding (requires DNA-recognizing motifs, not membrane-spanning segments); and (C) structural constituent of cell wall (GO:0005199 refers to proteins contributing to cell-wall structural integrity, typically extracellular or periplasmic with specific domains like LysM, not a polytopic integral membrane protein). The only option consistent with a multi-pass hydrophobic membrane protein is D, ABC-type transporter activity. While distinguishing ABC-type specifically from other membrane transporter families (MFS, P-type) from raw sequence alone is difficult, the question only requires selecting among these four options, and the hydrophobicity profile decisively eliminates A, B, and C.


**Missing item-specific fact**

> None critically missing. The specific identification as 'ABC-type' (vs. other transporter families) benefits from recognizing ABC permease fold motifs or database lookup, but among the four given choices, the membrane-transporter character alone suffices to select D.


**Reason**

> A knowledgeable model can reason from the extreme hydrophobicity and multi-TM topology of the sequence to conclude it is a membrane transporter/permease, then eliminate the three non-membrane options (transcription, DNA binding, cell wall structural) to arrive at D. This does not require memorizing the specific P0DXU6 entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options span fundamentally different molecular functions (transcription regulation, DNA binding, structural, transport). The sequence's extreme hydrophobicity and multi-pass TM character are incompatible with options A, B, and C. No other option is defensible for a polytopic integral membrane protein.


### Important caveats

- The GO annotation GO:0140359 carries evidence code IEA:InterPro (computational inference), though the functional comment is experimentally supported (PubMed:39375957, ECO:0000269).
- The UniProt entry was first published 2025-02-05; the exact author data-construction date is unknown, though the historical version (v4, released 2026-01-28) matches the benchmark sequence.
- Distinguishing ABC-type specifically from other membrane transporter families (MFS, P-type, etc.) from raw sequence alone is non-trivial; however, the multiple-choice format makes this unnecessary since only D is a membrane transport option.
- All reviewer evidence is absent from the evaluated model input; the model must rely on sequence biophysics and general biological knowledge.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 272-residue sequence is overwhelmingly hydrophobic (dominated by L, V, I, F, A, W, M, G) with multiple extended hydrophobic stretches consistent with 10+ transmembrane helices, characteristic of a multi-pass membrane permease. This biophysical profile is fundamentally incompatible with: (A) transcription coregulator activity (requires protein-protein/DNA interaction domains, not TM helices); (B) damaged DNA binding (requires DNA-recognizing motifs, not membrane-spanning segments); and (C) structural constituent of cell wall (GO:0005199 refers to proteins contributing to cell-wall structural integrity, typically extracellular or periplasmic with specific domains like LysM, not a polytopic integral membrane protein). The only option consistent with a multi-pass hydrophobic membrane protein is D, ABC-type transporter activity. While distinguishing ABC-type specifically from other membrane transporter families (MFS, P-type) from raw sequence alone is difficult, the question only requires selecting among these four options, and the hydrophobicity profile decisively eliminates A, B, and C.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None critically missing. The specific identification as 'ABC-type' (vs. other transporter families) benefits from recognizing ABC permease fold motifs or database lookup, but among the four given choices, the membrane-transporter character alone suffices to select D.",
    "reason": "A knowledgeable model can reason from the extreme hydrophobicity and multi-TM topology of the sequence to conclude it is a membrane transporter/permease, then eliminate the three non-membrane options (transcription, DNA binding, cell wall structural) to arrive at D. This does not require memorizing the specific P0DXU6 entry."
  },
  "case_id": "GO_molecular_function_0156",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H1",
      "H3",
      "H4",
      "GO4"
    ],
    "judgment": "supported",
    "reason": "UniProt entry P0DXU6 (sequence SHA256 match confirmed) annotates this protein as 'Daunorubicin resistance ABC transporter permease protein DrrB2' with GO:0140359 'ABC-type transporter activity' (IEA:InterPro). The functional comment is supported by experimental evidence (ECO:0000269, PubMed:39375957): 'Part of the ABC transporter complex DrrA2B2 involved in daunorubicin efflux.' The GO term GO:0140359 definition matches option D exactly. The sequence is 272 AA, matching the benchmark input."
  },
  "important_caveats": [
    "The GO annotation GO:0140359 carries evidence code IEA:InterPro (computational inference), though the functional comment is experimentally supported (PubMed:39375957, ECO:0000269).",
    "The UniProt entry was first published 2025-02-05; the exact author data-construction date is unknown, though the historical version (v4, released 2026-01-28) matches the benchmark sequence.",
    "Distinguishing ABC-type specifically from other membrane transporter families (MFS, P-type, etc.) from raw sequence alone is non-trivial; however, the multiple-choice format makes this unnecessary since only D is a membrane transport option.",
    "All reviewer evidence is absent from the evaluated model input; the model must rely on sequence biophysics and general biological knowledge."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span fundamentally different molecular functions (transcription regulation, DNA binding, structural, transport). The sequence's extreme hydrophobicity and multi-pass TM character are incompatible with options A, B, and C. No other option is defensible for a polytopic integral membrane protein."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0156",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry P0DXU6 (sequence SHA256 match confirmed) annotates this protein as 'Daunorubicin resistance ABC transporter permease protein DrrB2' with GO:0140359 'ABC-type transporter activity' (IEA:InterPro). The functional comment is supported by experimental evidence (ECO:0000269, PubMed:39375957): 'Part of the ABC transporter complex DrrA2B2 involved in daunorubicin efflux.' The GO term GO:0140359 definition matches option D exactly. The sequence is 272 AA, matching the benchmark input.",
    "evidence_ids": ["C4", "C5", "C6", "H1", "H3", "H4", "GO4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 272-residue sequence is overwhelmingly hydrophobic (dominated by L, V, I, F, A, W, M, G) with multiple extended hydrophobic stretches consistent with 10+ transmembrane helices, characteristic of a multi-pass membrane permease. This biophysical profile is fundamentally incompatible with: (A) transcription coregulator activity (requires protein-protein/DNA interaction domains, not TM helices); (B) damaged DNA binding (requires DNA-recognizing motifs, not membrane-spanning segments); and (C) structural constituent of cell wall (GO:0005199 refers to proteins contributing to cell-wall structural integrity, typically extracellular or periplasmic with specific domains like LysM, not a polytopic integral membrane protein). The only option consistent with a multi-pass hydrophobic membrane protein is D, ABC-type transporter activity. While distinguishing ABC-type specifically from other membrane transporter families (MFS, P-type) from raw sequence alone is difficult, the question only requires selecting among these four options, and the hydrophobicity profile decisively eliminates A, B, and C.",
    "missing_item_specific_fact": "None critically missing. The specific identification as 'ABC-type' (vs. other transporter families) benefits from recognizing ABC permease fold motifs or database lookup, but among the four given choices, the membrane-transporter character alone suffices to select D.",
    "reason": "A knowledgeable model can reason from the extreme hydrophobicity and multi-TM topology of the sequence to conclude it is a membrane transporter/permease, then eliminate the three non-membrane options (transcription, DNA binding, cell wall structural) to arrive at D. This does not require memorizing the specific P0DXU6 entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span fundamentally different molecular functions (transcription regulation, DNA binding, structural, transport). The sequence's extreme hydrophobicity and multi-pass TM character are incompatible with options A, B, and C. No other option is defensible for a polytopic integral membrane protein."
  },
  "important_caveats": [
    "The GO annotation GO:0140359 carries evidence code IEA:InterPro (computational inference), though the functional comment is experimentally supported (PubMed:39375957, ECO:0000269).",
    "The UniProt entry was first published 2025-02-05; the exact author data-construction date is unknown, though the historical version (v4, released 2026-01-28) matches the benchmark sequence.",
    "Distinguishing ABC-type specifically from other membrane transporter families (MFS, P-type, etc.) from raw sequence alone is non-trivial; however, the multiple-choice format makes this unnecessary since only D is a membrane transport option.",
    "All reviewer evidence is absent from the evaluated model input; the model must rely on sequence biophysics and general biological knowledge."
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

**Accession:** `P0DXU6` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 4. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXU6.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:39.151534+00:00.  

```json
"P0DXU6"
```

Source SHA-256: `4e7d0b296d64a4ffb645956bc9763e367bd0533eedf73ba35b4dc16bd7421217`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXU6.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:39.151534+00:00.  

```json
{"recommendedName":{"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Daunorubicin resistance ABC transporter permease protein DrrB2"}}}
```

Source SHA-256: `4e7d0b296d64a4ffb645956bc9763e367bd0533eedf73ba35b4dc16bd7421217`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXU6.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:39.151534+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"39375957","source":"PubMed"},{"evidenceCode":"ECO:0000305"}],"value":"Part of the ABC transporter complex DrrA2B2 involved in daunorubicin efflux (PubMed:39375957). Responsible for the translocation of the substrate across the membrane (Probable). Confers self-resistance to daunorubicin, an antibiotic produced by S.coeruleorubidus (PubMed:39375957)"}]}
```

Source SHA-256: `4e7d0b296d64a4ffb645956bc9763e367bd0533eedf73ba35b4dc16bd7421217`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXU6.json)  
**Locator:** `/uniProtKBCrossReferences/7`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:39.151534+00:00.  

```json
{"database":"GO","id":"GO:0140359","properties":[{"key":"GoTerm","value":"F:ABC-type transporter activity"},{"key":"GoEvidenceType","value":"IEA:InterPro"}]}
```

Source SHA-256: `4e7d0b296d64a4ffb645956bc9763e367bd0533eedf73ba35b4dc16bd7421217`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXU6?format=txt&versions=4)  
**Locator:** `lines 1-12`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 4 / 1.  
**Retrieved:** 2026-11-02T04:29:40.921406+00:00.  

```text
ID   DRRB2_STRC4             Reviewed;         272 AA.
AC   P0DXU6;
DT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.
DT   05-FEB-2025, sequence version 1.
DT   28-JAN-2026, entry version 4.
DE   RecName: Full=Daunorubicin resistance ABC transporter permease protein DrrB2 {ECO:0000305};
GN   Name=drrB2 {ECO:0000303|PubMed:39375957};
GN   ORFNames=R5U08_15990 {ECO:0000312|EMBL:WOT35540.1};
OS   Streptomyces coeruleorubidus.
OC   Bacteria; Bacillati; Actinomycetota; Actinomycetes; Kitasatosporales;
OC   Streptomycetaceae; Streptomyces.
OX   NCBI_TaxID=116188;
```

Source SHA-256: `372a99e71818628749a5230f6a3ea50eb4a3ab3f801909ad5a5e951310594fb7`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXU6?format=txt&versions=4)  
**Locator:** `lines 25-30`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 4 / 1.  
**Retrieved:** 2026-11-02T04:29:40.921406+00:00.  

```text
CC   -!- FUNCTION: Part of the ABC transporter complex DrrA2B2 involved in
CC       daunorubicin efflux (PubMed:39375957). Responsible for the
CC       translocation of the substrate across the membrane (Probable). Confers
CC       self-resistance to daunorubicin, an antibiotic produced by
CC       S.coeruleorubidus (PubMed:39375957). {ECO:0000269|PubMed:39375957,
CC       ECO:0000305}.
```

Source SHA-256: `372a99e71818628749a5230f6a3ea50eb4a3ab3f801909ad5a5e951310594fb7`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXU6?format=txt&versions=4)  
**Locator:** `lines 55-55`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 4 / 1.  
**Retrieved:** 2026-11-02T04:29:40.921406+00:00.  

```text
DR   GO; GO:0140359; F:ABC-type transporter activity; IEA:InterPro.
```

Source SHA-256: `372a99e71818628749a5230f6a3ea50eb4a3ab3f801909ad5a5e951310594fb7`.

### Evidence GO4

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 439730-439752`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0140359
name: ABC-type transporter activity
namespace: molecular_function
def: "Primary active transporter characterized by two nucleotide-binding domains and two transmembrane domains. Uses the energy generated from ATP hydrolysis to drive the transport of a substance across a membrane." [PMID:26517899]
synonym: "ABC transporter" EXACT []
synonym: "ABC-type efflux permease activity" EXACT []
synonym: "ABC-type efflux porter activity" EXACT []
synonym: "ABC-type transmembrane transporter activity" EXACT []
synonym: "ABC-type uptake permease activity" EXACT []
synonym: "ATP binding cassette transporter" EXACT []
synonym: "ATP-binding cassette (ABC) transporter activity" EXACT []
synonym: "ATP-binding cassette transporter" EXACT []
xref: Reactome:R-HSA-266070 "LTC4 is exported from the cytosol by ABCC1"
xref: Reactome:R-HSA-429157 "ABCC4 accumulation of dense granule contents"
xref: Reactome:R-HSA-5362459 "VCP-catalyzed ATP hydrolysis promotes the translocation of Hh-C into the cytosol"
xref: Reactome:R-HSA-5387389 "Hh processing variants are translocated to the cytosol in a VCP-dependent manner"
xref: Reactome:R-HSA-9661405 "ABCC1 transports BIL from cytosol to extracellular region (blood)"
xref: Reactome:R-HSA-9750656 "ABCC2, ABCC3 transport salicylate metabolites from cytosol to extracellular region of hepatic cells"
xref: TC:3.A.1
xref: Wikipedia:ATP-binding_cassette_transporter
is_a: GO:0042626 ! ATPase-coupled transmembrane transporter activity

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 156. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
