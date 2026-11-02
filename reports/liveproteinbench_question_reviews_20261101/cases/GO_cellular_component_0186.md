# GO_cellular_component_0186

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_cellular_component`  
**Author expected answer:** **C** — extracellular space

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MPPLGVLLLLVALGHSTQGHRPLPIRKAHKFDWWERGNFYQIYPRSFKDSDGDGIGDLKGITQTIDYLKTIGIDGVWLSPIFKSPMNDFGYDISDFYAIQEEYGTMEDFEELAAKCASIGLKLILDFVPNHSSDEHEHFRLSEEGIEPYKDYYIWHSGVLDANGTRHPPSNWISVFRGSAWQWSDKRQQYYLHQFQKKQPDLNYRNPALVEEMKNVMRFWLNKGIAGFRIDALPYLFESEEVDGHYRDEPLSGQATDDPDNPAYLTHTETKDQPETYDMVHQWRQVVDEYTARDNFTRIILTEAYTAVQNMTRFYGTPAAPGAQIPFNFQLITLLTVNSTGRDFVNAVQSWTRAMPSGAIANWVLGNHDNSRIASRLGVARADLYNIALQTLPGIAVTYYGEEIAMVDQWISWNDTIDPAACNADPATYELYSRDPVRTPFQWSNGTNAGFSNASRTWLPVADGYRELNVAAQLAAPRSHLKTFMQLTAYRKRRLLAEGNFVLRTVGRDLVMYKRSVPGVGYVVVALNFGPEPATLPVASQFPGTGEHWLKVIASSLQAQPQAGTWINTRLYKLAPDSGIVLERLTGRNDLMT

[Multiple Choices]
A. cytoplasmic vesicle
B. side of membrane
C. extracellular space
D. nuclear membrane
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

> The sequence-matched UniProt entry annotates the protein as secreted and assigns it to the extracellular space with IDA evidence. This supports choice C; the underlying publication was not independently reviewed here.

Citations as saved: [H3](#evidence-h3), [H4](#evidence-h4), [C5](#evidence-c5), [C6](#evidence-c6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The N-terminus contains a strong hydrophobic stretch consistent with a secretory signal peptide, while the sequence does not show an obvious later transmembrane anchor. That favors a soluble secreted/extracellular protein over the membrane-associated or intracellular choices.


**Missing item-specific fact**

> No protein-specific annotation or experimental measurement is required to make the sequence-based distinction, though it would be needed to establish the actual localization experimentally.


**Reason**

> The supplied sequence itself offers a meaningful secretion signal, making extracellular space the biologically defensible choice among these options.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The sequence's N-terminal signal peptide supports extracellular secretion, and the alternatives are not comparably supported by the sequence.


### Important caveats

- The reviewer-only UniProt record matches the supplied sequence; its annotations are evidence about this sequence, not information supplied to the evaluated model.
- The cited UniProt localization annotation is attributed to a publication, which was not independently validated here.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminus contains a strong hydrophobic stretch consistent with a secretory signal peptide, while the sequence does not show an obvious later transmembrane anchor. That favors a soluble secreted/extracellular protein over the membrane-associated or intracellular choices.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "No protein-specific annotation or experimental measurement is required to make the sequence-based distinction, though it would be needed to establish the actual localization experimentally.",
    "reason": "The supplied sequence itself offers a meaningful secretion signal, making extracellular space the biologically defensible choice among these options."
  },
  "case_id": "GO_cellular_component_0186",
  "expected_answer_check": {
    "evidence_ids": [
      "H3",
      "H4",
      "C5",
      "C6"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt entry annotates the protein as secreted and assigns it to the extracellular space with IDA evidence. This supports choice C; the underlying publication was not independently reviewed here."
  },
  "important_caveats": [
    "The reviewer-only UniProt record matches the supplied sequence; its annotations are evidence about this sequence, not information supplied to the evaluated model.",
    "The cited UniProt localization annotation is attributed to a publication, which was not independently validated here."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence's N-terminal signal peptide supports extracellular secretion, and the alternatives are not comparably supported by the sequence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0186",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt entry annotates the protein as secreted and assigns it to the extracellular space with IDA evidence. This supports choice C; the underlying publication was not independently reviewed here.",
    "evidence_ids": ["H3", "H4", "C5", "C6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The N-terminus contains a strong hydrophobic stretch consistent with a secretory signal peptide, while the sequence does not show an obvious later transmembrane anchor. That favors a soluble secreted/extracellular protein over the membrane-associated or intracellular choices.",
    "missing_item_specific_fact": "No protein-specific annotation or experimental measurement is required to make the sequence-based distinction, though it would be needed to establish the actual localization experimentally.",
    "reason": "The supplied sequence itself offers a meaningful secretion signal, making extracellular space the biologically defensible choice among these options."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence's N-terminal signal peptide supports extracellular secretion, and the alternatives are not comparably supported by the sequence."
  },
  "important_caveats": [
    "The reviewer-only UniProt record matches the supplied sequence; its annotations are evidence about this sequence, not information supplied to the evaluated model.",
    "The cited UniProt localization annotation is attributed to a publication, which was not independently validated here."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt Q7PYT9 (Salivary alpha-glucosidase, Anopheles gambiae) carries GO:0005615 (extracellular space) with IDA evidence (H4, C6), and the subcellular location is annotated as 'Secreted' with experimental evidence from PubMed:38428508 (C5, H3). The protein is flagged as a Precursor with a signal peptide, consistent with secretion. The expected answer 'extracellular space' matches the direct GO annotation.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H3](#evidence-h3), [H4](#evidence-h4), [H1](#evidence-h1).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The N-terminal sequence 'MPPLGVLLLLVALGHSTQ' exhibits the tripartite architecture of a classical signal peptide (basic N-region 'MPP', hydrophobic H-region 'LGVLLLLVALGH', polar C-region 'STQ'), indicating entry into the secretory pathway. The remainder of the 593-residue sequence lacks long hydrophobic stretches that would indicate transmembrane anchors (eliminating 'side of membrane'), lacks a canonical nuclear localization signal (eliminating 'nuclear membrane'), and lacks a mitochondrial targeting sequence. A protein with a signal peptide but no transmembrane domain is processed through the secretory pathway and released extracellularly, making 'extracellular space' the primary location. 'Cytoplasmic vesicle' is at best a transient transit compartment, not the primary steady-state location of a fully secreted protein.


**Missing item-specific fact**

> None critical. The signal peptide is identifiable from sequence features, and the absence of alternative targeting signals is assessable from the sequence. Knowing the protein is specifically a 'salivary alpha-glucosidase' would confirm the answer but is not strictly required for the reasoning chain.


**Reason**

> A model can identify the N-terminal signal peptide from hydrophobicity patterns, note the absence of transmembrane domains, NLS, or mitochondrial targeting sequences, and conclude the protein follows the default secretory pathway to the extracellular space. This is general cell-biology reasoning applied to sequence features.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options represent distinct cellular compartments (intracellular vesicle, membrane leaflet, extracellular, nuclear envelope). A secreted protein with a signal peptide and no transmembrane anchor maps cleanly to extracellular space. Cytoplasmic vesicle is only a transient transit compartment, not a primary location for a fully secreted protein. The other two options are clearly inconsistent with the sequence features.


### Important caveats

- The GO annotation GO:0005615 (extracellular space) with IDA evidence is the direct source for the key; the GO term 'extracellular region' (GO:0005576) is also annotated. The option text 'extracellular space' matches GO:0005615 exactly.
- The 'Secreted' subcellular location annotation is supported by experimental evidence (PubMed:38428508, 2024), but the GO IDA annotation references an earlier PubMed (17913537). Both support the extracellular localization.
- The identity of this protein as a salivary enzyme is not stated in the model input; the reasoning must rely on sequence-derived signal peptide detection and absence of other targeting signals.
- The signal peptide (residues ~1-18) is a computationally predictable feature; experimental confirmation of secretion comes from the 2024 study, which post-dates some benchmark construction timelines.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal sequence 'MPPLGVLLLLVALGHSTQ' exhibits the tripartite architecture of a classical signal peptide (basic N-region 'MPP', hydrophobic H-region 'LGVLLLLVALGH', polar C-region 'STQ'), indicating entry into the secretory pathway. The remainder of the 593-residue sequence lacks long hydrophobic stretches that would indicate transmembrane anchors (eliminating 'side of membrane'), lacks a canonical nuclear localization signal (eliminating 'nuclear membrane'), and lacks a mitochondrial targeting sequence. A protein with a signal peptide but no transmembrane domain is processed through the secretory pathway and released extracellularly, making 'extracellular space' the primary location. 'Cytoplasmic vesicle' is at best a transient transit compartment, not the primary steady-state location of a fully secreted protein.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None critical. The signal peptide is identifiable from sequence features, and the absence of alternative targeting signals is assessable from the sequence. Knowing the protein is specifically a 'salivary alpha-glucosidase' would confirm the answer but is not strictly required for the reasoning chain.",
    "reason": "A model can identify the N-terminal signal peptide from hydrophobicity patterns, note the absence of transmembrane domains, NLS, or mitochondrial targeting sequences, and conclude the protein follows the default secretory pathway to the extracellular space. This is general cell-biology reasoning applied to sequence features."
  },
  "case_id": "GO_cellular_component_0186",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "C7",
      "H3",
      "H4",
      "H1"
    ],
    "judgment": "supported",
    "reason": "UniProt Q7PYT9 (Salivary alpha-glucosidase, Anopheles gambiae) carries GO:0005615 (extracellular space) with IDA evidence (H4, C6), and the subcellular location is annotated as 'Secreted' with experimental evidence from PubMed:38428508 (C5, H3). The protein is flagged as a Precursor with a signal peptide, consistent with secretion. The expected answer 'extracellular space' matches the direct GO annotation."
  },
  "important_caveats": [
    "The GO annotation GO:0005615 (extracellular space) with IDA evidence is the direct source for the key; the GO term 'extracellular region' (GO:0005576) is also annotated. The option text 'extracellular space' matches GO:0005615 exactly.",
    "The 'Secreted' subcellular location annotation is supported by experimental evidence (PubMed:38428508, 2024), but the GO IDA annotation references an earlier PubMed (17913537). Both support the extracellular localization.",
    "The identity of this protein as a salivary enzyme is not stated in the model input; the reasoning must rely on sequence-derived signal peptide detection and absence of other targeting signals.",
    "The signal peptide (residues ~1-18) is a computationally predictable feature; experimental confirmation of secretion comes from the 2024 study, which post-dates some benchmark construction timelines."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent distinct cellular compartments (intracellular vesicle, membrane leaflet, extracellular, nuclear envelope). A secreted protein with a signal peptide and no transmembrane anchor maps cleanly to extracellular space. Cytoplasmic vesicle is only a transient transit compartment, not a primary location for a fully secreted protein. The other two options are clearly inconsistent with the sequence features."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0186",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt Q7PYT9 (Salivary alpha-glucosidase, Anopheles gambiae) carries GO:0005615 (extracellular space) with IDA evidence (H4, C6), and the subcellular location is annotated as 'Secreted' with experimental evidence from PubMed:38428508 (C5, H3). The protein is flagged as a Precursor with a signal peptide, consistent with secretion. The expected answer 'extracellular space' matches the direct GO annotation.",
    "evidence_ids": ["C5", "C6", "C7", "H3", "H4", "H1"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The N-terminal sequence 'MPPLGVLLLLVALGHSTQ' exhibits the tripartite architecture of a classical signal peptide (basic N-region 'MPP', hydrophobic H-region 'LGVLLLLVALGH', polar C-region 'STQ'), indicating entry into the secretory pathway. The remainder of the 593-residue sequence lacks long hydrophobic stretches that would indicate transmembrane anchors (eliminating 'side of membrane'), lacks a canonical nuclear localization signal (eliminating 'nuclear membrane'), and lacks a mitochondrial targeting sequence. A protein with a signal peptide but no transmembrane domain is processed through the secretory pathway and released extracellularly, making 'extracellular space' the primary location. 'Cytoplasmic vesicle' is at best a transient transit compartment, not the primary steady-state location of a fully secreted protein.",
    "missing_item_specific_fact": "None critical. The signal peptide is identifiable from sequence features, and the absence of alternative targeting signals is assessable from the sequence. Knowing the protein is specifically a 'salivary alpha-glucosidase' would confirm the answer but is not strictly required for the reasoning chain.",
    "reason": "A model can identify the N-terminal signal peptide from hydrophobicity patterns, note the absence of transmembrane domains, NLS, or mitochondrial targeting sequences, and conclude the protein follows the default secretory pathway to the extracellular space. This is general cell-biology reasoning applied to sequence features."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent distinct cellular compartments (intracellular vesicle, membrane leaflet, extracellular, nuclear envelope). A secreted protein with a signal peptide and no transmembrane anchor maps cleanly to extracellular space. Cytoplasmic vesicle is only a transient transit compartment, not a primary location for a fully secreted protein. The other two options are clearly inconsistent with the sequence features."
  },
  "important_caveats": [
    "The GO annotation GO:0005615 (extracellular space) with IDA evidence is the direct source for the key; the GO term 'extracellular region' (GO:0005576) is also annotated. The option text 'extracellular space' matches GO:0005615 exactly.",
    "The 'Secreted' subcellular location annotation is supported by experimental evidence (PubMed:38428508, 2024), but the GO IDA annotation references an earlier PubMed (17913537). Both support the extracellular localization.",
    "The identity of this protein as a salivary enzyme is not stated in the model input; the reasoning must rely on sequence-derived signal peptide detection and absence of other targeting signals.",
    "The signal peptide (residues ~1-18) is a computationally predictable feature; experimental confirmation of secretion comes from the 2024 study, which post-dates some benchmark construction timelines."
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

**Accession:** `Q7PYT9` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 132. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q7PYT9.json)  
**Locator:** `/comments/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:10.588074+00:00.  

```json
{"commentType":"SUBCELLULAR LOCATION","subcellularLocations":[{"location":{"evidences":[{"evidenceCode":"ECO:0000269","id":"38428508","source":"PubMed"}],"id":"SL-0243","value":"Secreted"}}]}
```

Source SHA-256: `b95ba5f84a3c800481a01173df1ae62cd4cae90bbd222bbb34ea446d40d2dc8d`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q7PYT9.json)  
**Locator:** `/uniProtKBCrossReferences/16`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:10.588074+00:00.  

```json
{"database":"GO","evidences":[{"evidenceCode":"ECO:0000314","id":"17913537","source":"PubMed"}],"id":"GO:0005576","properties":[{"key":"GoTerm","value":"C:extracellular region"},{"key":"GoEvidenceType","value":"IDA:UniProtKB"}]}
```

Source SHA-256: `b95ba5f84a3c800481a01173df1ae62cd4cae90bbd222bbb34ea446d40d2dc8d`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q7PYT9.json)  
**Locator:** `/references/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:10.588074+00:00.  

```json
{"citation":{"authors":["Williams A.E.","Gittis A.G.","Botello K.","Cruz P.","Martin-Martin I.","Valenzuela Leon P.C.","Sumner B.","Bonilla B.","Calvo E."],"citationCrossReferences":[{"database":"PubMed","id":"38428508"},{"database":"DOI","id":"10.1016/j.ibmb.2024.104097"}],"citationType":"journal article","firstPage":"104097","id":"38428508","journal":"Insect Biochem. Mol. Biol.","lastPage":"104097","publicationDate":"2024","title":"Structural and functional comparisons of salivary alpha-glucosidases from the mosquito vectors Aedes aegypti, Anopheles gambiae, and Culex quinquefasciatus.","volume":"167"},"evidences":[{"evidenceCode":"ECO:0000305"}],"referenceNumber":4,"referencePositions":["FUNCTION","CATALYTIC ACTIVITY","BIOPHYSICOCHEMICAL PROPERTIES","SUBCELLULAR LOCATION","TISSUE SPECIFICITY"]}
```

Source SHA-256: `b95ba5f84a3c800481a01173df1ae62cd4cae90bbd222bbb34ea446d40d2dc8d`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q7PYT9?format=txt&versions=132)  
**Locator:** `lines 1-16`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 132 / 3.  
**Retrieved:** 2026-11-01T06:42:03.279027+00:00.  

```text
ID   MALT_ANOGA              Reviewed;         593 AA.
AC   Q7PYT9;
DT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.
DT   09-JAN-2007, sequence version 3.
DT   28-JAN-2026, entry version 132.
DE   RecName: Full=Salivary alpha-glucosidase {ECO:0000303|PubMed:38428508};
DE            Short=AnGluc {ECO:0000303|PubMed:38428508};
DE            EC=3.2.1.20 {ECO:0000269|PubMed:38428508};
DE   Flags: Precursor;
GN   Name=MAL1 {ECO:0000250|UniProtKB:P13080};
GN   ORFNames=AgaP_AGAP002102 {ECO:0000312|EMBL:EAA00998.3};
OS   Anopheles gambiae (African malaria mosquito).
OC   Eukaryota; Metazoa; Ecdysozoa; Arthropoda; Hexapoda; Insecta; Pterygota;
OC   Neoptera; Endopterygota; Diptera; Nematocera; Culicoidea; Culicidae;
OC   Anophelinae; Anopheles.
OX   NCBI_TaxID=7165 {ECO:0000312|EMBL:EAA00998.3};
```

Source SHA-256: `de59e19c2630176f429b35ceca36f772399cba06a5d924df213abc4f4cd0c052`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q7PYT9?format=txt&versions=132)  
**Locator:** `lines 83-83`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 132 / 3.  
**Retrieved:** 2026-11-01T06:42:03.279027+00:00.  

```text
CC   -!- SUBCELLULAR LOCATION: Secreted {ECO:0000269|PubMed:38428508}.
```

Source SHA-256: `de59e19c2630176f429b35ceca36f772399cba06a5d924df213abc4f4cd0c052`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q7PYT9?format=txt&versions=132)  
**Locator:** `lines 107-107`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 132 / 3.  
**Retrieved:** 2026-11-01T06:42:03.279027+00:00.  

```text
DR   GO; GO:0005615; C:extracellular space; IDA:UniProtKB.
```

Source SHA-256: `de59e19c2630176f429b35ceca36f772399cba06a5d924df213abc4f4cd0c052`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 186. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
