# GO_biological_process_0167

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_biological_process`  
**Author expected answer:** **C** — cell adhesion

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MAQWWLILLGLWTVLPSLAGGKLLNVCMNSKHHKQEPGPEDKLYFECMPWKDNACCTRDTSWEAHLDEPLLFNFSMTHCGLLTPLCHKHFIQAICFYECSPNLGPWIQPVVPNRQEEQRLWDVPLCLEDCEEWWKDCRTSHTCKADWLHGWVWDQGKNGCPAHAPCLPFSDYFPTPADLCEKIWNNTFKASPERRNSGRCLQKWFEPTHGNPNVEVALHFAGSASAPQLSYSITAFSLCLLLHA

[Multiple Choices]
A. lipid catabolic process
B. stress-activated MAPK cascade
C. cell adhesion
D. regulation of establishment of protein localization
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

> The supplied sequence exactly matches rat JUNO. Its UniProt functional annotation describes JUNO as an oocyte-surface receptor whose interaction with IZUMO1 is a necessary sperm–egg adhesion event; the matched entry also annotates cell adhesion (GO:0007155). The functional statement is transferred by similarity, and the GO annotation is ISO:RGD, so this supports the key but is not direct experimental evidence for this rat sequence.

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> A signal peptide and likely extracellular receptor domain are consistent with a cell-surface interaction, but those sequence features do not identify the particular adhesion role or reliably distinguish it from the listed processes.


**Missing item-specific fact**

> The protein-specific fact that this sequence is JUNO, the oocyte receptor for IZUMO1 involved in sperm–egg adhesion.


**Reason**

> Choosing C depends on knowing the identity or function of this particular protein, information not established by the sequence and choices through general biological reasoning alone.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The protein-specific functional evidence supports cell adhesion; none of the other listed processes is comparably supported by the supplied evidence.


### Important caveats

- The functional annotation is based on similarity to mouse JUNO (ECO:0000250), and the cell-adhesion GO annotation carries evidence code ISO:RGD; these are not direct experimental demonstrations for the rat protein.
- The exact author source snapshot is unknown, although the sequence matches both the cited historical and current UniProt records.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "A signal peptide and likely extracellular receptor domain are consistent with a cell-surface interaction, but those sequence features do not identify the particular adhesion role or reliably distinguish it from the listed processes.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific fact that this sequence is JUNO, the oocyte receptor for IZUMO1 involved in sperm–egg adhesion.",
    "reason": "Choosing C depends on knowing the identity or function of this particular protein, information not established by the sequence and choices through general biological reasoning alone."
  },
  "case_id": "GO_biological_process_0167",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "C6",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches rat JUNO. Its UniProt functional annotation describes JUNO as an oocyte-surface receptor whose interaction with IZUMO1 is a necessary sperm–egg adhesion event; the matched entry also annotates cell adhesion (GO:0007155). The functional statement is transferred by similarity, and the GO annotation is ISO:RGD, so this supports the key but is not direct experimental evidence for this rat sequence."
  },
  "important_caveats": [
    "The functional annotation is based on similarity to mouse JUNO (ECO:0000250), and the cell-adhesion GO annotation carries evidence code ISO:RGD; these are not direct experimental demonstrations for the rat protein.",
    "The exact author source snapshot is unknown, although the sequence matches both the cited historical and current UniProt records."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The protein-specific functional evidence supports cell adhesion; none of the other listed processes is comparably supported by the supplied evidence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_biological_process_0167",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches rat JUNO. Its UniProt functional annotation describes JUNO as an oocyte-surface receptor whose interaction with IZUMO1 is a necessary sperm–egg adhesion event; the matched entry also annotates cell adhesion (GO:0007155). The functional statement is transferred by similarity, and the GO annotation is ISO:RGD, so this supports the key but is not direct experimental evidence for this rat sequence.",
    "evidence_ids": ["C1", "C5", "C6", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "A signal peptide and likely extracellular receptor domain are consistent with a cell-surface interaction, but those sequence features do not identify the particular adhesion role or reliably distinguish it from the listed processes.",
    "missing_item_specific_fact": "The protein-specific fact that this sequence is JUNO, the oocyte receptor for IZUMO1 involved in sperm–egg adhesion.",
    "reason": "Choosing C depends on knowing the identity or function of this particular protein, information not established by the sequence and choices through general biological reasoning alone."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The protein-specific functional evidence supports cell adhesion; none of the other listed processes is comparably supported by the supplied evidence."
  },
  "important_caveats": [
    "The functional annotation is based on similarity to mouse JUNO (ECO:0000250), and the cell-adhesion GO annotation carries evidence code ISO:RGD; these are not direct experimental demonstrations for the rat protein.",
    "The exact author source snapshot is unknown, although the sequence matches both the cited historical and current UniProt records."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry F1M928 (JUNO/Folate receptor 4 from Rattus norvegicus) is directly annotated with GO:0007155 (cell adhesion) with evidence code ISO:RGD (C6/H4). The function comment (C5/H3) explicitly states: 'The IZUMO1:IZUMO1R/JUNO interaction is a necessary adhesion event between sperm and egg that is required for fertilization.' The protein is a GPI-anchored oocyte-surface receptor whose primary described role is mediating sperm-egg adhesion. While more specific GO terms exist (sperm-egg recognition, single fertilization), 'cell adhesion' is a valid and directly annotated parent-level biological process for this protein.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H3](#evidence-h3), [H4](#evidence-h4), [GO1](#evidence-go1).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> General sequence features (N-terminal signal peptide, C-terminal GPI-anchor signal, cysteine-rich folate-receptor-fold) identify this as a GPI-anchored cell-surface receptor. This weakly disfavors options A (lipid catabolism) and B (MAPK cascade), as a GPI-anchored surface receptor is unlikely to catalyze lipid breakdown or act as a kinase-cascade component. However, the folate receptor family (FR1-3) is canonically associated with folate binding/transport, NOT cell adhesion. Distinguishing this particular family member (FR4/JUNO) as an adhesion receptor rather than a folate transporter requires the protein-specific fact that JUNO does not bind folate and instead mediates sperm-egg adhesion via IZUMO1 binding.


**Missing item-specific fact**

> The knowledge that this specific folate receptor family member (FR4/JUNO) has lost folate-binding capability and instead functions as a sperm-egg adhesion receptor for IZUMO1. Without this protein-specific annotation, a model seeing a folate-receptor-fold GPI-anchored protein would more plausibly predict folate transport/metabolism than cell adhesion.


**Reason**

> While GPI anchoring and receptor architecture weakly support a cell-surface adhesion role over the clearly unrelated distractors (lipid catabolism, MAPK cascade), the critical inference—that this folate receptor family member is an adhesion receptor rather than a folate transporter—depends on protein-specific functional annotation. The sequence alone does not distinguish JUNO's adhesion role from the canonical folate-binding role of its family members.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options A, B, and D are clearly inconsistent with a GPI-anchored cell-surface receptor. The only remaining question is whether a model would predict 'cell adhesion' or something related to folate transport for a folate-receptor-fold protein, but no folate-transport option is offered, making C the only viable choice among the four.


### Important caveats

- The GO:0007155 annotation carries evidence code ISO:RGD (inferred from sequence/structural similarity via RGD database), not direct experimental evidence for the rat protein. The functional description is transferred by similarity from mouse Q9EQF4 (ISS).
- More specific GO terms for this protein include 'sperm-egg recognition' (GO:0035036) and 'fusion of sperm to egg plasma membrane' (GO:0007342), but these are not offered as options.
- The UniProt entry was first public in 2025-02-05; the benchmark construction date is unknown. The sequence has matched since sequence version 2 (2013-04-03).
- The protein is named 'Folate receptor 4' but the function comment explicitly states 'Does not bind folate,' making the folate-receptor naming potentially misleading for a model relying on family-level inference.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "General sequence features (N-terminal signal peptide, C-terminal GPI-anchor signal, cysteine-rich folate-receptor-fold) identify this as a GPI-anchored cell-surface receptor. This weakly disfavors options A (lipid catabolism) and B (MAPK cascade), as a GPI-anchored surface receptor is unlikely to catalyze lipid breakdown or act as a kinase-cascade component. However, the folate receptor family (FR1-3) is canonically associated with folate binding/transport, NOT cell adhesion. Distinguishing this particular family member (FR4/JUNO) as an adhesion receptor rather than a folate transporter requires the protein-specific fact that JUNO does not bind folate and instead mediates sperm-egg adhesion via IZUMO1 binding.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The knowledge that this specific folate receptor family member (FR4/JUNO) has lost folate-binding capability and instead functions as a sperm-egg adhesion receptor for IZUMO1. Without this protein-specific annotation, a model seeing a folate-receptor-fold GPI-anchored protein would more plausibly predict folate transport/metabolism than cell adhesion.",
    "reason": "While GPI anchoring and receptor architecture weakly support a cell-surface adhesion role over the clearly unrelated distractors (lipid catabolism, MAPK cascade), the critical inference—that this folate receptor family member is an adhesion receptor rather than a folate transporter—depends on protein-specific functional annotation. The sequence alone does not distinguish JUNO's adhesion role from the canonical folate-binding role of its family members."
  },
  "case_id": "GO_biological_process_0167",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "H1",
      "H3",
      "H4",
      "GO1"
    ],
    "judgment": "supported",
    "reason": "UniProt entry F1M928 (JUNO/Folate receptor 4 from Rattus norvegicus) is directly annotated with GO:0007155 (cell adhesion) with evidence code ISO:RGD (C6/H4). The function comment (C5/H3) explicitly states: 'The IZUMO1:IZUMO1R/JUNO interaction is a necessary adhesion event between sperm and egg that is required for fertilization.' The protein is a GPI-anchored oocyte-surface receptor whose primary described role is mediating sperm-egg adhesion. While more specific GO terms exist (sperm-egg recognition, single fertilization), 'cell adhesion' is a valid and directly annotated parent-level biological process for this protein."
  },
  "important_caveats": [
    "The GO:0007155 annotation carries evidence code ISO:RGD (inferred from sequence/structural similarity via RGD database), not direct experimental evidence for the rat protein. The functional description is transferred by similarity from mouse Q9EQF4 (ISS).",
    "More specific GO terms for this protein include 'sperm-egg recognition' (GO:0035036) and 'fusion of sperm to egg plasma membrane' (GO:0007342), but these are not offered as options.",
    "The UniProt entry was first public in 2025-02-05; the benchmark construction date is unknown. The sequence has matched since sequence version 2 (2013-04-03).",
    "The protein is named 'Folate receptor 4' but the function comment explicitly states 'Does not bind folate,' making the folate-receptor naming potentially misleading for a model relying on family-level inference."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A, B, and D are clearly inconsistent with a GPI-anchored cell-surface receptor. The only remaining question is whether a model would predict 'cell adhesion' or something related to folate transport for a folate-receptor-fold protein, but no folate-transport option is offered, making C the only viable choice among the four."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_biological_process_0167",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry F1M928 (JUNO/Folate receptor 4 from Rattus norvegicus) is directly annotated with GO:0007155 (cell adhesion) with evidence code ISO:RGD (C6/H4). The function comment (C5/H3) explicitly states: 'The IZUMO1:IZUMO1R/JUNO interaction is a necessary adhesion event between sperm and egg that is required for fertilization.' The protein is a GPI-anchored oocyte-surface receptor whose primary described role is mediating sperm-egg adhesion. While more specific GO terms exist (sperm-egg recognition, single fertilization), 'cell adhesion' is a valid and directly annotated parent-level biological process for this protein.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H1", "H3", "H4", "GO1"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "General sequence features (N-terminal signal peptide, C-terminal GPI-anchor signal, cysteine-rich folate-receptor-fold) identify this as a GPI-anchored cell-surface receptor. This weakly disfavors options A (lipid catabolism) and B (MAPK cascade), as a GPI-anchored surface receptor is unlikely to catalyze lipid breakdown or act as a kinase-cascade component. However, the folate receptor family (FR1-3) is canonically associated with folate binding/transport, NOT cell adhesion. Distinguishing this particular family member (FR4/JUNO) as an adhesion receptor rather than a folate transporter requires the protein-specific fact that JUNO does not bind folate and instead mediates sperm-egg adhesion via IZUMO1 binding.",
    "missing_item_specific_fact": "The knowledge that this specific folate receptor family member (FR4/JUNO) has lost folate-binding capability and instead functions as a sperm-egg adhesion receptor for IZUMO1. Without this protein-specific annotation, a model seeing a folate-receptor-fold GPI-anchored protein would more plausibly predict folate transport/metabolism than cell adhesion.",
    "reason": "While GPI anchoring and receptor architecture weakly support a cell-surface adhesion role over the clearly unrelated distractors (lipid catabolism, MAPK cascade), the critical inference—that this folate receptor family member is an adhesion receptor rather than a folate transporter—depends on protein-specific functional annotation. The sequence alone does not distinguish JUNO's adhesion role from the canonical folate-binding role of its family members."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A, B, and D are clearly inconsistent with a GPI-anchored cell-surface receptor. The only remaining question is whether a model would predict 'cell adhesion' or something related to folate transport for a folate-receptor-fold protein, but no folate-transport option is offered, making C the only viable choice among the four."
  },
  "important_caveats": [
    "The GO:0007155 annotation carries evidence code ISO:RGD (inferred from sequence/structural similarity via RGD database), not direct experimental evidence for the rat protein. The functional description is transferred by similarity from mouse Q9EQF4 (ISS).",
    "More specific GO terms for this protein include 'sperm-egg recognition' (GO:0035036) and 'fusion of sperm to egg plasma membrane' (GO:0007342), but these are not offered as options.",
    "The UniProt entry was first public in 2025-02-05; the benchmark construction date is unknown. The sequence has matched since sequence version 2 (2013-04-03).",
    "The protein is named 'Folate receptor 4' but the function comment explicitly states 'Does not bind folate,' making the folate-receptor naming potentially misleading for a model relying on family-level inference."
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

**Accession:** `F1M928` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 92. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/F1M928.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:11.745036+00:00.  

```json
"F1M928"
```

Source SHA-256: `b56a36704099444e686e704fe8993d737b0fe848fed00c7247b8f75bf147a97d`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/F1M928.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:11.745036+00:00.  

```json
{"alternativeNames":[{"fullName":{"value":"Folate receptor 4"}},{"fullName":{"value":"Folate receptor delta"},"shortNames":[{"value":"FR-delta"}]},{"fullName":{"value":"IZUMO1 receptor protein JUNO"}}],"flag":"Precursor","recommendedName":{"fullName":{"value":"Sperm-egg fusion protein Juno"}}}
```

Source SHA-256: `b56a36704099444e686e704fe8993d737b0fe848fed00c7247b8f75bf147a97d`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/F1M928.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:11.745036+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q9EQF4","source":"UniProtKB"}],"value":"Receptor for IZUMO1 present at the cell surface of oocytes (oolemma), which is essential for species-specific gamete recognition and fertilization. The IZUMO1:IZUMO1R/JUNO interaction is a necessary adhesion event between sperm and egg that is required for fertilization but is not sufficient for cell fusion. The ligand-receptor interaction probably does not act as a membrane 'fusogen'. Does not bind folate"}]}
```

Source SHA-256: `b56a36704099444e686e704fe8993d737b0fe848fed00c7247b8f75bf147a97d`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/F1M928.json)  
**Locator:** `/uniProtKBCrossReferences/34`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:11.745036+00:00.  

```json
{"database":"GO","id":"GO:0007155","properties":[{"key":"GoTerm","value":"P:cell adhesion"},{"key":"GoEvidenceType","value":"ISO:RGD"}]}
```

Source SHA-256: `b56a36704099444e686e704fe8993d737b0fe848fed00c7247b8f75bf147a97d`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/F1M928?format=txt&versions=92)  
**Locator:** `lines 1-17`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 92 / 2.  
**Retrieved:** 2026-11-02T04:28:13.956568+00:00.  

```text
ID   JUNO_RAT                Reviewed;         244 AA.
AC   F1M928; A0A1B1W5N3; A6JNA9;
DT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.
DT   03-APR-2013, sequence version 2.
DT   28-JAN-2026, entry version 92.
DE   RecName: Full=Sperm-egg fusion protein Juno;
DE   AltName: Full=Folate receptor 4;
DE   AltName: Full=Folate receptor delta;
DE            Short=FR-delta;
DE   AltName: Full=IZUMO1 receptor protein JUNO;
DE   Flags: Precursor;
GN   Name=Izumo1r; Synonyms=Folr4, JUNO {ECO:0000303|PubMed:37951137};
OS   Rattus norvegicus (Rat).
OC   Eukaryota; Metazoa; Chordata; Craniata; Vertebrata; Euteleostomi; Mammalia;
OC   Eutheria; Euarchontoglires; Glires; Rodentia; Myomorpha; Muroidea; Muridae;
OC   Murinae; Rattus.
OX   NCBI_TaxID=10116;
```

Source SHA-256: `57bdb51b29963fdcfb395f44171ffb2ca0c93e66ec625c64278875faf6b4aa52`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/F1M928?format=txt&versions=92)  
**Locator:** `lines 87-93`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 92 / 2.  
**Retrieved:** 2026-11-02T04:28:13.956568+00:00.  

```text
CC   -!- FUNCTION: Receptor for IZUMO1 present at the cell surface of oocytes
CC       (oolemma), which is essential for species-specific gamete recognition
CC       and fertilization. The IZUMO1:IZUMO1R/JUNO interaction is a necessary
CC       adhesion event between sperm and egg that is required for fertilization
CC       but is not sufficient for cell fusion. The ligand-receptor interaction
CC       probably does not act as a membrane 'fusogen'. Does not bind folate.
CC       {ECO:0000250|UniProtKB:Q9EQF4}.
```

Source SHA-256: `57bdb51b29963fdcfb395f44171ffb2ca0c93e66ec625c64278875faf6b4aa52`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/F1M928?format=txt&versions=92)  
**Locator:** `lines 152-152`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 92 / 2.  
**Retrieved:** 2026-11-02T04:28:13.956568+00:00.  

```text
DR   GO; GO:0007155; P:cell adhesion; ISO:RGD.
```

Source SHA-256: `57bdb51b29963fdcfb395f44171ffb2ca0c93e66ec625c64278875faf6b4aa52`.

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 73784-73803`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0007155
name: cell adhesion
namespace: biological_process
alt_id: GO:0098602
def: "The attachment of a cell, either to another cell or to an underlying substrate such as the extracellular matrix, via cell adhesion molecules." [GOC:hb, GOC:pf]
subset: goslim_candida
subset: goslim_chembl
subset: goslim_drosophila
subset: goslim_euk_cellular_processes_ribbon
subset: goslim_generic
subset: goslim_metagenomics
subset: goslim_pir
subset: goslim_pombe
subset: goslim_prokaryote
synonym: "cell adhesion molecule activity" RELATED []
synonym: "single organism cell adhesion" RELATED []
xref: Wikipedia:Cell_adhesion
is_a: GO:0009987 ! cellular process

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_biological_process.json), zero-based source row 167. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
