# GO_cellular_component_0166

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_cellular_component`  
**Author expected answer:** **D** — ATP-binding cassette (ABC) transporter complex

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
A. nuclear periphery
B. cell surface
C. IRE1-TRAF2-ASK1 complex
D. ATP-binding cassette (ABC) transporter complex
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Gene Ontology (GO) Cellular Component Prediction, which is to predict the primary Cellular Component where a protein is located, according to the Gene Ontology (GO) framework. A protein's location within a cell (e.g., Nucleus, Mitochondria, Cytoplasm) is critical for its function and is often determined by specific targeting signals in its amino acid sequence. Based on the provided sequence, you must identify the most likely compartment where the protein resides.. The inputs provided by the user for this task include:

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

> The exact sequence matches a UniProt entry annotated to GO:0043190, ATP-binding cassette (ABC) transporter complex, by IEA:InterPro. This supports D as a database annotation, though not as direct experimental evidence.

Citations as saved: [H1](#evidence-h1), [H4](#evidence-h4), [C1](#evidence-c1), [C6](#evidence-c6).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The strongly hydrophobic sequence supports a multipass membrane protein, but that alone does not establish membership in an ABC transporter complex or distinguish that complex annotation from a membrane-associated location.


**Missing item-specific fact**

> The protein-specific identification as the DrrB2 ABC-transporter permease and its GO:0043190 annotation are not supplied in the question.


**Reason**

> Choosing D depends on identifying the protein or obtaining a family/complex annotation; the sequence’s general membrane topology does not by itself establish the specific GO complex.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The sequence supports membrane association, but the cell-surface option is not equivalent to a membrane or transporter-complex annotation, and the supplied evidence does not establish external cell-surface localization.


### Important caveats

- The ABC-complex annotation is computational (IEA:InterPro), not reported here as direct experimental evidence.
- UniProt also records cell-membrane localization, with evidence transferred by similarity; that is not the same GO term as the cell-surface option.
- The reviewer evidence confirms an exact sequence match and a historical annotation, but that protein-specific information was absent from the evaluated input.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The strongly hydrophobic sequence supports a multipass membrane protein, but that alone does not establish membership in an ABC transporter complex or distinguish that complex annotation from a membrane-associated location.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific identification as the DrrB2 ABC-transporter permease and its GO:0043190 annotation are not supplied in the question.",
    "reason": "Choosing D depends on identifying the protein or obtaining a family/complex annotation; the sequence’s general membrane topology does not by itself establish the specific GO complex."
  },
  "case_id": "GO_cellular_component_0166",
  "expected_answer_check": {
    "evidence_ids": [
      "H1",
      "H4",
      "C1",
      "C6"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry annotated to GO:0043190, ATP-binding cassette (ABC) transporter complex, by IEA:InterPro. This supports D as a database annotation, though not as direct experimental evidence."
  },
  "important_caveats": [
    "The ABC-complex annotation is computational (IEA:InterPro), not reported here as direct experimental evidence.",
    "UniProt also records cell-membrane localization, with evidence transferred by similarity; that is not the same GO term as the cell-surface option.",
    "The reviewer evidence confirms an exact sequence match and a historical annotation, but that protein-specific information was absent from the evaluated input."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence supports membrane association, but the cell-surface option is not equivalent to a membrane or transporter-complex annotation, and the supplied evidence does not establish external cell-surface localization."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0166",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry annotated to GO:0043190, ATP-binding cassette (ABC) transporter complex, by IEA:InterPro. This supports D as a database annotation, though not as direct experimental evidence.",
    "evidence_ids": ["H1", "H4", "C1", "C6"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The strongly hydrophobic sequence supports a multipass membrane protein, but that alone does not establish membership in an ABC transporter complex or distinguish that complex annotation from a membrane-associated location.",
    "missing_item_specific_fact": "The protein-specific identification as the DrrB2 ABC-transporter permease and its GO:0043190 annotation are not supplied in the question.",
    "reason": "Choosing D depends on identifying the protein or obtaining a family/complex annotation; the sequence’s general membrane topology does not by itself establish the specific GO complex."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence supports membrane association, but the cell-surface option is not equivalent to a membrane or transporter-complex annotation, and the supplied evidence does not establish external cell-surface localization."
  },
  "important_caveats": [
    "The ABC-complex annotation is computational (IEA:InterPro), not reported here as direct experimental evidence.",
    "UniProt also records cell-membrane localization, with evidence transferred by similarity; that is not the same GO term as the cell-surface option.",
    "The reviewer evidence confirms an exact sequence match and a historical annotation, but that protein-specific information was absent from the evaluated input."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry P0DXU6 (sequence matched) annotates GO:0043190 (ATP-binding cassette (ABC) transporter complex) with evidence code IEA:InterPro (C6, H4). The protein is named 'Daunorubicin resistance ABC transporter permease protein DrrB2' (C4, H1). The GO term definition (GO3) describes a complex with 'two membrane-associated domains and two ATP-binding domains,' and this protein provides the membrane-associated permease component. The annotation is computational (IEA:InterPro) rather than directly experimental, but it is consistent with the protein's identity as an ABC transporter permease and the multi-pass membrane topology noted in the subcellular location comment (C5, H3).

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H3](#evidence-h3), [H4](#evidence-h4), [GO3](#evidence-go3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains approximately 6-8 hydrophobic stretches consistent with multi-pass transmembrane helices, clearly indicating an integral membrane protein. Option A (nuclear periphery) is eliminated because the protein lacks nuclear localization signals and has obvious TM architecture. Option C (IRE1-TRAF2-ASK1 complex, GO:0009986) is eliminated because it is defined as an endoplasmic reticulum membrane complex in eukaryotes (GO4), incompatible with a bacterial multi-pass membrane protein lacking ER signal sequences. Option B (cell surface, GO:0009986) is defined as 'the external part of the cell wall and/or plasma membrane' for proteins 'attached (integrated or loosely bound)' to the surface (GO1); a protein with ~6-8 TM helices spanning the membrane is an integral membrane transporter, not a surface-attached protein. Option D (ABC transporter complex, GO:0043190) is defined as 'typically comprised of four domains; two membrane-associated domains and two ATP-binding domains' (GO3); the protein's multi-pass TM architecture without any Walker A/B nucleotide-binding motifs is consistent with the permease (membrane-associated) component of such a complex. These GO term definitions and membrane topology arguments provide concrete grounds to select D.


**Missing item-specific fact**

> Precise recognition of ABC transporter transmembrane domain signature motifs (e.g., Pfam ABC_transmem_1/2) to distinguish this from other multi-pass membrane transporter families (MFS, SMR) would require domain-database lookup, though the given options do not include competing transporter families.


**Reason**

> While the specific identification as ABC transporter (rather than another transporter family) benefits from domain-level knowledge, the provided options are sufficiently distinct that general reasoning about membrane topology, GO term semantics, and the absence of nucleotide-binding domains meaningfully narrows the answer to D. The distractors (nuclear periphery, eukaryotic ER complex, cell-surface attachment) are eliminable through standard cell biology knowledge without protein-specific lookup.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options A, B, and C are clearly incompatible with a bacterial multi-pass integral membrane transporter based on GO term definitions and basic cell biology. The UniProt entry also annotates plasma membrane (GO:0005886, ISS), but this is not among the choices. Among the four provided options, D is the only one consistent with an integral membrane transporter permease component.


### Important caveats

- The GO:0043190 annotation carries evidence code IEA:InterPro (automated/computational), not direct experimental evidence. The subcellular location 'Cell membrane' is annotated via ISS (similarity to P32011).
- The UniProt entry was first released 2025-02-05; the benchmark construction date is unknown, so the author may have relied on a different or earlier annotation source.
- The reviewer-only accession P0DXU6 was inferred from dataset metadata absent from the evaluated model input; the model must work from sequence alone.
- The protein name explicitly states 'ABC transporter permease,' but this name is not provided in the question input; reasoning must rely on sequence features and general knowledge.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains approximately 6-8 hydrophobic stretches consistent with multi-pass transmembrane helices, clearly indicating an integral membrane protein. Option A (nuclear periphery) is eliminated because the protein lacks nuclear localization signals and has obvious TM architecture. Option C (IRE1-TRAF2-ASK1 complex, GO:0009986) is eliminated because it is defined as an endoplasmic reticulum membrane complex in eukaryotes (GO4), incompatible with a bacterial multi-pass membrane protein lacking ER signal sequences. Option B (cell surface, GO:0009986) is defined as 'the external part of the cell wall and/or plasma membrane' for proteins 'attached (integrated or loosely bound)' to the surface (GO1); a protein with ~6-8 TM helices spanning the membrane is an integral membrane transporter, not a surface-attached protein. Option D (ABC transporter complex, GO:0043190) is defined as 'typically comprised of four domains; two membrane-associated domains and two ATP-binding domains' (GO3); the protein's multi-pass TM architecture without any Walker A/B nucleotide-binding motifs is consistent with the permease (membrane-associated) component of such a complex. These GO term definitions and membrane topology arguments provide concrete grounds to select D.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "Precise recognition of ABC transporter transmembrane domain signature motifs (e.g., Pfam ABC_transmem_1/2) to distinguish this from other multi-pass membrane transporter families (MFS, SMR) would require domain-database lookup, though the given options do not include competing transporter families.",
    "reason": "While the specific identification as ABC transporter (rather than another transporter family) benefits from domain-level knowledge, the provided options are sufficiently distinct that general reasoning about membrane topology, GO term semantics, and the absence of nucleotide-binding domains meaningfully narrows the answer to D. The distractors (nuclear periphery, eukaryotic ER complex, cell-surface attachment) are eliminable through standard cell biology knowledge without protein-specific lookup."
  },
  "case_id": "GO_cellular_component_0166",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H1",
      "H3",
      "H4",
      "GO3"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry P0DXU6 (sequence matched) annotates GO:0043190 (ATP-binding cassette (ABC) transporter complex) with evidence code IEA:InterPro (C6, H4). The protein is named 'Daunorubicin resistance ABC transporter permease protein DrrB2' (C4, H1). The GO term definition (GO3) describes a complex with 'two membrane-associated domains and two ATP-binding domains,' and this protein provides the membrane-associated permease component. The annotation is computational (IEA:InterPro) rather than directly experimental, but it is consistent with the protein's identity as an ABC transporter permease and the multi-pass membrane topology noted in the subcellular location comment (C5, H3)."
  },
  "important_caveats": [
    "The GO:0043190 annotation carries evidence code IEA:InterPro (automated/computational), not direct experimental evidence. The subcellular location 'Cell membrane' is annotated via ISS (similarity to P32011).",
    "The UniProt entry was first released 2025-02-05; the benchmark construction date is unknown, so the author may have relied on a different or earlier annotation source.",
    "The reviewer-only accession P0DXU6 was inferred from dataset metadata absent from the evaluated model input; the model must work from sequence alone.",
    "The protein name explicitly states 'ABC transporter permease,' but this name is not provided in the question input; reasoning must rely on sequence features and general knowledge."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A, B, and C are clearly incompatible with a bacterial multi-pass integral membrane transporter based on GO term definitions and basic cell biology. The UniProt entry also annotates plasma membrane (GO:0005886, ISS), but this is not among the choices. Among the four provided options, D is the only one consistent with an integral membrane transporter permease component."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0166",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry P0DXU6 (sequence matched) annotates GO:0043190 (ATP-binding cassette (ABC) transporter complex) with evidence code IEA:InterPro (C6, H4). The protein is named 'Daunorubicin resistance ABC transporter permease protein DrrB2' (C4, H1). The GO term definition (GO3) describes a complex with 'two membrane-associated domains and two ATP-binding domains,' and this protein provides the membrane-associated permease component. The annotation is computational (IEA:InterPro) rather than directly experimental, but it is consistent with the protein's identity as an ABC transporter permease and the multi-pass membrane topology noted in the subcellular location comment (C5, H3).",
    "evidence_ids": ["C4", "C5", "C6", "H1", "H3", "H4", "GO3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains approximately 6-8 hydrophobic stretches consistent with multi-pass transmembrane helices, clearly indicating an integral membrane protein. Option A (nuclear periphery) is eliminated because the protein lacks nuclear localization signals and has obvious TM architecture. Option C (IRE1-TRAF2-ASK1 complex, GO:0009986) is eliminated because it is defined as an endoplasmic reticulum membrane complex in eukaryotes (GO4), incompatible with a bacterial multi-pass membrane protein lacking ER signal sequences. Option B (cell surface, GO:0009986) is defined as 'the external part of the cell wall and/or plasma membrane' for proteins 'attached (integrated or loosely bound)' to the surface (GO1); a protein with ~6-8 TM helices spanning the membrane is an integral membrane transporter, not a surface-attached protein. Option D (ABC transporter complex, GO:0043190) is defined as 'typically comprised of four domains; two membrane-associated domains and two ATP-binding domains' (GO3); the protein's multi-pass TM architecture without any Walker A/B nucleotide-binding motifs is consistent with the permease (membrane-associated) component of such a complex. These GO term definitions and membrane topology arguments provide concrete grounds to select D.",
    "missing_item_specific_fact": "Precise recognition of ABC transporter transmembrane domain signature motifs (e.g., Pfam ABC_transmem_1/2) to distinguish this from other multi-pass membrane transporter families (MFS, SMR) would require domain-database lookup, though the given options do not include competing transporter families.",
    "reason": "While the specific identification as ABC transporter (rather than another transporter family) benefits from domain-level knowledge, the provided options are sufficiently distinct that general reasoning about membrane topology, GO term semantics, and the absence of nucleotide-binding domains meaningfully narrows the answer to D. The distractors (nuclear periphery, eukaryotic ER complex, cell-surface attachment) are eliminable through standard cell biology knowledge without protein-specific lookup."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A, B, and C are clearly incompatible with a bacterial multi-pass integral membrane transporter based on GO term definitions and basic cell biology. The UniProt entry also annotates plasma membrane (GO:0005886, ISS), but this is not among the choices. Among the four provided options, D is the only one consistent with an integral membrane transporter permease component."
  },
  "important_caveats": [
    "The GO:0043190 annotation carries evidence code IEA:InterPro (automated/computational), not direct experimental evidence. The subcellular location 'Cell membrane' is annotated via ISS (similarity to P32011).",
    "The UniProt entry was first released 2025-02-05; the benchmark construction date is unknown, so the author may have relied on a different or earlier annotation source.",
    "The reviewer-only accession P0DXU6 was inferred from dataset metadata absent from the evaluated model input; the model must work from sequence alone.",
    "The protein name explicitly states 'ABC transporter permease,' but this name is not provided in the question input; reasoning must rely on sequence features and general knowledge."
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
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:39.151534+00:00.  

```json
{"commentType":"SUBCELLULAR LOCATION","subcellularLocations":[{"location":{"evidences":[{"evidenceCode":"ECO:0000250","id":"P32011","source":"UniProtKB"}],"id":"SL-0039","value":"Cell membrane"},"topology":{"evidences":[{"evidenceCode":"ECO:0000255"}],"id":"SL-9909","value":"Multi-pass membrane protein"}}]}
```

Source SHA-256: `4e7d0b296d64a4ffb645956bc9763e367bd0533eedf73ba35b4dc16bd7421217`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXU6.json)  
**Locator:** `/uniProtKBCrossReferences/5`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:39.151534+00:00.  

```json
{"database":"GO","id":"GO:0043190","properties":[{"key":"GoTerm","value":"C:ATP-binding cassette (ABC) transporter complex"},{"key":"GoEvidenceType","value":"IEA:InterPro"}]}
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
**Locator:** `lines 33-34`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 4 / 1.  
**Retrieved:** 2026-11-02T04:29:40.921406+00:00.  

```text
CC   -!- SUBCELLULAR LOCATION: Cell membrane {ECO:0000250|UniProtKB:P32011};
CC       Multi-pass membrane protein {ECO:0000255}.
```

Source SHA-256: `372a99e71818628749a5230f6a3ea50eb4a3ab3f801909ad5a5e951310594fb7`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXU6?format=txt&versions=4)  
**Locator:** `lines 54-54`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 4 / 1.  
**Retrieved:** 2026-11-02T04:29:40.921406+00:00.  

```text
DR   GO; GO:0043190; C:ATP-binding cassette (ABC) transporter complex; IEA:InterPro.
```

Source SHA-256: `372a99e71818628749a5230f6a3ea50eb4a3ab3f801909ad5a5e951310594fb7`.

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 101772-101784`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0009986
name: cell surface
namespace: cellular_component
alt_id: GO:0009928
alt_id: GO:0009929
def: "The external part of the cell wall and/or plasma membrane." [GOC:jl, GOC:mtg_sensu, GOC:sm]
comment: Note that this term is intended to annotate gene products that are attached (integrated or loosely bound) to the plasma membrane or cell wall.
subset: goslim_pir
synonym: "cell associated" EXACT []
synonym: "cell bound" EXACT []
is_a: GO:0110165 ! cellular anatomical structure

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

### Evidence GO3

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 244782-244797`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0043190
name: ATP-binding cassette (ABC) transporter complex
namespace: cellular_component
alt_id: GO:0043191
alt_id: GO:0043192
def: "A complex for the transport of metabolites into and out of the cell, typically comprised of four domains; two membrane-associated domains and two ATP-binding domains at the intracellular face of the membrane, that form a central pore through the plasma membrane. Each of the four core domains may be encoded as a separate polypeptide or the domains can be fused in any one of a number of ways into multidomain polypeptides. In Bacteria and Archaebacteria, ABC transporters also include substrate binding proteins to bind substrate external to the cytoplasm and deliver it to the transporter." [GOC:jl, GOC:mtg_sensu, PMID:11421269, PMID:15111107]
subset: goslim_metagenomics
subset: goslim_pir
synonym: "ABC-type efflux permease complex" NARROW []
synonym: "ABC-type efflux porter complex" NARROW []
synonym: "ABC-type uptake permease complex" NARROW []
synonym: "mating pheromone exporter" NARROW []
is_a: GO:0098533 ! ATPase dependent transmembrane transport complex
is_a: GO:0098797 ! plasma membrane protein complex

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

### Evidence GO4

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 553487-553496`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:1990604
name: IRE1-TRAF2-ASK1 complex
namespace: cellular_component
def: "A protein complex of the endoplasmic reticulum membrane that consists of IRE1 (Inositol-requiring enzyme-1), TRAF2 (TNF receptor-associated factor 2) and ASK1 (Apoptosis signal-regulating kinase 1, a MAP3K)." [GOC:bf, GOC:PARL, PMID:12050113, PMID:23000344]
synonym: "ERN1-TRAF2-ASK1 complex" RELATED [HGNC:3449]
is_a: GO:0098796 ! membrane protein complex
is_a: GO:0140534 ! endoplasmic reticulum protein-containing complex
relationship: part_of GO:0005789 ! endoplasmic reticulum membrane

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 166. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
