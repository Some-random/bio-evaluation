# GO_cellular_component_0160

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_cellular_component`  
**Author expected answer:** **D** — plasma membrane

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MVNFTHVSEFVLLGFQGGPGMQAMLFLIFLILYGIAVVGNLGMIVIIWVDAHLHTPMYAFLQSLSLLDICYSSTIAPRALANSMQEDHTISFGGCAAQFFFLSLFGITEAFLLAAMAYDRFIAICNPLLYSVSMSHQVCVLLISGSYLWGVVNAIAQTTMTFRLPFCGSNEINDFFCDVPPLLSLSCSDTFINQLVLLGLCGSIIVSTFLIVLVSYIYIISTILRIPTMQGCQKAFSTCASHLTGVCLFFGTVFFMYAQPSAIFFMEQSKIVSIFYTMVIPMLNPLIYSLRNKEVKQALRRSMQKLSL

[Multiple Choices]
A. centrosome
B. Ndc80 complex
C. histone deacetylase complex
D. plasma membrane
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

> The exact sequence matches a UniProt entry annotated to the cell membrane and to GO:0005886 (plasma membrane). The GO assignment is IEA computational annotation, so this supports the key as an annotation but does not establish experimental localization.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H2](#evidence-h2), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has multiple long hydrophobic segments consistent with a multi-pass membrane protein. That strongly favors the plasma-membrane option over the listed centrosomal and nuclear protein complexes; a cell-surface receptor is a biologically reasonable prediction.


**Missing item-specific fact**

> The sequence alone does not establish experimentally that this protein is at the plasma membrane rather than another membrane. The specific database localization annotation is not supplied in the question.


**Reason**

> The sequence and choices provide a meaningful basis for predicting D at this coarse level, though they do not prove the precise localization.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among these choices, plasma membrane is the only membrane location and is the best fit for a multi-pass membrane protein.


### Important caveats

- The cited GO plasma-membrane annotation is computational (IEA:UniProtKB-SubCell), not direct experimental evidence.
- The reviewer-only evidence matches the sequence, but the author's exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has multiple long hydrophobic segments consistent with a multi-pass membrane protein. That strongly favors the plasma-membrane option over the listed centrosomal and nuclear protein complexes; a cell-surface receptor is a biologically reasonable prediction.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The sequence alone does not establish experimentally that this protein is at the plasma membrane rather than another membrane. The specific database localization annotation is not supplied in the question.",
    "reason": "The sequence and choices provide a meaningful basis for predicting D at this coarse level, though they do not prove the precise localization."
  },
  "case_id": "GO_cellular_component_0160",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H2",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry annotated to the cell membrane and to GO:0005886 (plasma membrane). The GO assignment is IEA computational annotation, so this supports the key as an annotation but does not establish experimental localization."
  },
  "important_caveats": [
    "The cited GO plasma-membrane annotation is computational (IEA:UniProtKB-SubCell), not direct experimental evidence.",
    "The reviewer-only evidence matches the sequence, but the author's exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among these choices, plasma membrane is the only membrane location and is the best fit for a multi-pass membrane protein."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0160",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry annotated to the cell membrane and to GO:0005886 (plasma membrane). The GO assignment is IEA computational annotation, so this supports the key as an annotation but does not establish experimental localization.",
    "evidence_ids": ["C5", "C6", "H2", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has multiple long hydrophobic segments consistent with a multi-pass membrane protein. That strongly favors the plasma-membrane option over the listed centrosomal and nuclear protein complexes; a cell-surface receptor is a biologically reasonable prediction.",
    "missing_item_specific_fact": "The sequence alone does not establish experimentally that this protein is at the plasma membrane rather than another membrane. The specific database localization annotation is not supplied in the question.",
    "reason": "The sequence and choices provide a meaningful basis for predicting D at this coarse level, though they do not prove the precise localization."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among these choices, plasma membrane is the only membrane location and is the best fit for a multi-pass membrane protein."
  },
  "important_caveats": [
    "The cited GO plasma-membrane annotation is computational (IEA:UniProtKB-SubCell), not direct experimental evidence.",
    "The reviewer-only evidence matches the sequence, but the author's exact source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry Q6UXT6 (OR9H1_HUMAN) annotates the subcellular location as 'Cell membrane' with 'Multi-pass membrane protein' topology (evidence codes ECO:0000305 and ECO:0000255). The GO cross-reference is GO:0005886 (plasma membrane), which has 'cell membrane' as an EXACT synonym (GO3). The protein is an olfactory receptor, a well-characterized 7-transmembrane GPCR family member universally localized to the plasma membrane of olfactory neurons. The sequence (308 aa) shows ~7 hydrophobic stretches consistent with 7-TM topology. The evidence code for the GO annotation is IEA (Inferred from Electronic Annotation), and the topology assignment uses similarity-based inference, but the family-level biology of olfactory receptors as plasma membrane GPCRs is robust.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H2](#evidence-h2), [H3](#evidence-h3), [GO3](#evidence-go3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 308-aa sequence contains approximately seven distinct hydrophobic stretches separated by hydrophilic loops, a hallmark topology of 7-transmembrane G-protein-coupled receptors. General biological knowledge establishes that 7-TM receptors are integral plasma membrane proteins. The three distractors (centrosome, Ndc80 complex, histone deacetylase complex) are all non-membrane-associated structures (centrosome is a microtubule-organizing center; Ndc80 is an outer kinetochore complex; HDAC complex is nuclear). A multi-pass membrane protein with seven TM segments is incompatible with any of these non-membrane compartments. Thus, recognizing the multi-pass membrane topology from the hydrophobic pattern and applying the general principle that 7-TM receptors reside in the plasma membrane is sufficient to select D without knowing the exact protein identity.


**Missing item-specific fact**

> None critical. While knowing the protein is specifically an olfactory receptor (OR9H1) would confirm the answer, the multi-pass membrane topology visible in the sequence combined with the non-membrane nature of the three distractors provides a sufficient reasoning pathway.


**Reason**

> The sequence's hydrophobic stretch pattern is directly observable and indicates transmembrane topology. The biological principle that multi-pass membrane proteins with 7-TM architecture reside in the plasma membrane is general knowledge. The distractors are all clearly non-membrane structures, making elimination straightforward. No protein-specific database lookup is strictly required.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The three distractors (centrosome, Ndc80 complex, histone deacetylase complex) are all non-membrane cellular structures with no plausible association with a multi-pass transmembrane protein. Only plasma membrane is consistent with the observed 7-TM topology. No ambiguity exists among the choices.


### Important caveats

- The GO annotation evidence code is IEA (Inferred from Electronic Annotation) derived from UniProtKB-SubCell, not direct experimental localization. However, the family-level assignment of olfactory receptors to the plasma membrane is well-established.
- The UniProt entry was first publicly released 2025-02-05; the historical snapshot (entry version 106, released 2026-01-28) already contains the plasma membrane annotation. The sequence has been unchanged since 2004.
- The reviewer identified the accession Q6UXT6 from dataset metadata; the evaluated model received only the raw sequence with no accession or protein name.
- The topology assignment uses ECO:0000255 (similarity-based inference), meaning it is based on homology to other GPCRs rather than direct experimental membrane topology determination, though this is standard for GPCR family members.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 308-aa sequence contains approximately seven distinct hydrophobic stretches separated by hydrophilic loops, a hallmark topology of 7-transmembrane G-protein-coupled receptors. General biological knowledge establishes that 7-TM receptors are integral plasma membrane proteins. The three distractors (centrosome, Ndc80 complex, histone deacetylase complex) are all non-membrane-associated structures (centrosome is a microtubule-organizing center; Ndc80 is an outer kinetochore complex; HDAC complex is nuclear). A multi-pass membrane protein with seven TM segments is incompatible with any of these non-membrane compartments. Thus, recognizing the multi-pass membrane topology from the hydrophobic pattern and applying the general principle that 7-TM receptors reside in the plasma membrane is sufficient to select D without knowing the exact protein identity.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None critical. While knowing the protein is specifically an olfactory receptor (OR9H1) would confirm the answer, the multi-pass membrane topology visible in the sequence combined with the non-membrane nature of the three distractors provides a sufficient reasoning pathway.",
    "reason": "The sequence's hydrophobic stretch pattern is directly observable and indicates transmembrane topology. The biological principle that multi-pass membrane proteins with 7-TM architecture reside in the plasma membrane is general knowledge. The distractors are all clearly non-membrane structures, making elimination straightforward. No protein-specific database lookup is strictly required."
  },
  "case_id": "GO_cellular_component_0160",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H2",
      "H3",
      "GO3"
    ],
    "judgment": "supported",
    "reason": "UniProt entry Q6UXT6 (OR9H1_HUMAN) annotates the subcellular location as 'Cell membrane' with 'Multi-pass membrane protein' topology (evidence codes ECO:0000305 and ECO:0000255). The GO cross-reference is GO:0005886 (plasma membrane), which has 'cell membrane' as an EXACT synonym (GO3). The protein is an olfactory receptor, a well-characterized 7-transmembrane GPCR family member universally localized to the plasma membrane of olfactory neurons. The sequence (308 aa) shows ~7 hydrophobic stretches consistent with 7-TM topology. The evidence code for the GO annotation is IEA (Inferred from Electronic Annotation), and the topology assignment uses similarity-based inference, but the family-level biology of olfactory receptors as plasma membrane GPCRs is robust."
  },
  "important_caveats": [
    "The GO annotation evidence code is IEA (Inferred from Electronic Annotation) derived from UniProtKB-SubCell, not direct experimental localization. However, the family-level assignment of olfactory receptors to the plasma membrane is well-established.",
    "The UniProt entry was first publicly released 2025-02-05; the historical snapshot (entry version 106, released 2026-01-28) already contains the plasma membrane annotation. The sequence has been unchanged since 2004.",
    "The reviewer identified the accession Q6UXT6 from dataset metadata; the evaluated model received only the raw sequence with no accession or protein name.",
    "The topology assignment uses ECO:0000255 (similarity-based inference), meaning it is based on homology to other GPCRs rather than direct experimental membrane topology determination, though this is standard for GPCR family members."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The three distractors (centrosome, Ndc80 complex, histone deacetylase complex) are all non-membrane cellular structures with no plausible association with a multi-pass transmembrane protein. Only plasma membrane is consistent with the observed 7-TM topology. No ambiguity exists among the choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0160",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry Q6UXT6 (OR9H1_HUMAN) annotates the subcellular location as 'Cell membrane' with 'Multi-pass membrane protein' topology (evidence codes ECO:0000305 and ECO:0000255). The GO cross-reference is GO:0005886 (plasma membrane), which has 'cell membrane' as an EXACT synonym (GO3). The protein is an olfactory receptor, a well-characterized 7-transmembrane GPCR family member universally localized to the plasma membrane of olfactory neurons. The sequence (308 aa) shows ~7 hydrophobic stretches consistent with 7-TM topology. The evidence code for the GO annotation is IEA (Inferred from Electronic Annotation), and the topology assignment uses similarity-based inference, but the family-level biology of olfactory receptors as plasma membrane GPCRs is robust.",
    "evidence_ids": ["C4", "C5", "C6", "H2", "H3", "GO3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 308-aa sequence contains approximately seven distinct hydrophobic stretches separated by hydrophilic loops, a hallmark topology of 7-transmembrane G-protein-coupled receptors. General biological knowledge establishes that 7-TM receptors are integral plasma membrane proteins. The three distractors (centrosome, Ndc80 complex, histone deacetylase complex) are all non-membrane-associated structures (centrosome is a microtubule-organizing center; Ndc80 is an outer kinetochore complex; HDAC complex is nuclear). A multi-pass membrane protein with seven TM segments is incompatible with any of these non-membrane compartments. Thus, recognizing the multi-pass membrane topology from the hydrophobic pattern and applying the general principle that 7-TM receptors reside in the plasma membrane is sufficient to select D without knowing the exact protein identity.",
    "missing_item_specific_fact": "None critical. While knowing the protein is specifically an olfactory receptor (OR9H1) would confirm the answer, the multi-pass membrane topology visible in the sequence combined with the non-membrane nature of the three distractors provides a sufficient reasoning pathway.",
    "reason": "The sequence's hydrophobic stretch pattern is directly observable and indicates transmembrane topology. The biological principle that multi-pass membrane proteins with 7-TM architecture reside in the plasma membrane is general knowledge. The distractors are all clearly non-membrane structures, making elimination straightforward. No protein-specific database lookup is strictly required."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The three distractors (centrosome, Ndc80 complex, histone deacetylase complex) are all non-membrane cellular structures with no plausible association with a multi-pass transmembrane protein. Only plasma membrane is consistent with the observed 7-TM topology. No ambiguity exists among the choices."
  },
  "important_caveats": [
    "The GO annotation evidence code is IEA (Inferred from Electronic Annotation) derived from UniProtKB-SubCell, not direct experimental localization. However, the family-level assignment of olfactory receptors to the plasma membrane is well-established.",
    "The UniProt entry was first publicly released 2025-02-05; the historical snapshot (entry version 106, released 2026-01-28) already contains the plasma membrane annotation. The sequence has been unchanged since 2004.",
    "The reviewer identified the accession Q6UXT6 from dataset metadata; the evaluated model received only the raw sequence with no accession or protein name.",
    "The topology assignment uses ECO:0000255 (similarity-based inference), meaning it is based on homology to other GPCRs rather than direct experimental membrane topology determination, though this is standard for GPCR family members."
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

**Accession:** `Q6UXT6` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 106. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6UXT6.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:45.136978+00:00.  

```json
{"alternativeNames":[{"fullName":{"value":"Olfactory receptor family 9 subfamily H member 1"}}],"recommendedName":{"fullName":{"value":"Olfactory receptor OR9H1"}}}
```

Source SHA-256: `d761824ae03c221d019ed712f82a29f42f3f5f479f6233c26b23ed7827f111d1`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6UXT6.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:45.136978+00:00.  

```json
{"commentType":"SUBCELLULAR LOCATION","subcellularLocations":[{"location":{"evidences":[{"evidenceCode":"ECO:0000305"}],"id":"SL-0039","value":"Cell membrane"},"topology":{"evidences":[{"evidenceCode":"ECO:0000255"}],"id":"SL-9909","value":"Multi-pass membrane protein"}}]}
```

Source SHA-256: `d761824ae03c221d019ed712f82a29f42f3f5f479f6233c26b23ed7827f111d1`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6UXT6.json)  
**Locator:** `/uniProtKBCrossReferences/9`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:45.136978+00:00.  

```json
{"database":"GO","id":"GO:0005886","properties":[{"key":"GoTerm","value":"C:plasma membrane"},{"key":"GoEvidenceType","value":"IEA:UniProtKB-SubCell"}]}
```

Source SHA-256: `d761824ae03c221d019ed712f82a29f42f3f5f479f6233c26b23ed7827f111d1`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q6UXT6?format=txt&versions=106)  
**Locator:** `lines 66-67`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 106 / 1.  
**Retrieved:** 2026-11-02T04:31:47.614110+00:00.  

```text
CC   -!- SUBCELLULAR LOCATION: Cell membrane {ECO:0000305}; Multi-pass membrane
CC       protein {ECO:0000255}.
```

Source SHA-256: `072cef681e411cc08becb56d888ebce42ad8a93eca1ca016afab23f858b5896a`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q6UXT6?format=txt&versions=106)  
**Locator:** `lines 95-95`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 106 / 1.  
**Retrieved:** 2026-11-02T04:31:47.614110+00:00.  

```text
DR   GO; GO:0005886; C:plasma membrane; IEA:UniProtKB-SubCell.
```

Source SHA-256: `072cef681e411cc08becb56d888ebce42ad8a93eca1ca016afab23f858b5896a`.

### Evidence GO3

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 60420-60454`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0005886
name: plasma membrane
namespace: cellular_component
alt_id: GO:0005887
alt_id: GO:0005904
def: "The membrane surrounding a cell that separates the cell from its external environment. It consists of a phospholipid bilayer and associated proteins." [ISBN:0716731363]
subset: goslim_agr
subset: goslim_candida
subset: goslim_chembl
subset: goslim_drosophila
subset: goslim_euk_cellular_processes_ribbon
subset: goslim_generic
subset: goslim_metagenomics
subset: goslim_mouse
subset: goslim_plant
subset: goslim_plant_ribbon
subset: goslim_prokaryote
subset: goslim_prokaryote_ribbon
subset: goslim_yeast
synonym: "bacterial inner membrane" NARROW []
synonym: "cell membrane" EXACT []
synonym: "cellular membrane" EXACT [NIF_Subcellular:sao6433132645]
synonym: "cytoplasmic membrane" EXACT []
synonym: "inner endospore membrane" NARROW []
synonym: "integral component of plasma membrane" NARROW []
synonym: "integral to plasma membrane" NARROW []
synonym: "juxtamembrane" BROAD []
synonym: "plasma membrane lipid bilayer" NARROW [GOC:mah]
synonym: "plasmalemma" EXACT []
xref: NIF_Subcellular:sao1663586795
xref: Wikipedia:Cell_membrane
is_a: GO:0016020 ! membrane
relationship: part_of GO:0071944 ! cell periphery

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 160. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
