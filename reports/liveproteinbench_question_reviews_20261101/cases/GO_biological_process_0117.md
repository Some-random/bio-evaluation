# GO_biological_process_0117

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_biological_process`  
**Author expected answer:** **B** — iron ion transmembrane transport

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MHQDNSMRRAINQSRNGGSDSCDINNDREHDNINRNSYINNFHIENINSDKNEQSYIYCSDRAQVTDSILGNRKYTHEENINSTEMFSRTNYEYSNKNNVDIEMYNISNNNFYNGNNNGHSNDIIDYINNNNVNKDLSNTSNNADINTYIKKLTSNQSTAYCDGKGYNESANGSNFDINFRDVIKNNNNKNYKNNNHVPDDMLELGDRSFDSSFYIHNNVEEIDTERSNRLSFMSKLKMYFNYFGPGWIVAIAYLDPGNICGNLNVGLIRSDDFINVNSSVKDYTGYRLLWVLVYGHILGFIFHTLSMKLGHITGLDLAALCRKEFSSKFSYFLYICVQIAIWGAHLQAIIGVFVAINLILGIPVKIAILYTLIEAFAYSFLENKSLDLLEKVLSLLIGILVCCFMFNVFMTPINFQEVASSILYPRIPKGKLLDTMGLLGSVISAHIFYLHSNLTSKKKPVIYNDRMVKRYNKLGTIESGGSLLVSCITNCIIVLTFAEVNISGDDRKADYNLFNAYDVMKKYFGKTSMYIWSFGLLSSGNNASFMCEYASKSVFEGFLNKNVNPFFRVIFSRIILFIMLYAYVSYDKYTIDQLSNFINVVQILLLPLAIIPLYRFSIHKNVLGKFAIKGAFKYLVFVLVISIIVANFLLTLFDFLQYAPSNLYVIFIFISSIFYLLFIIYFFNMPITKTYYKDS

[Multiple Choices]
A. defense response to bacterium
B. iron ion transmembrane transport
C. nuclear pore complex assembly
D. ribosomal large subunit assembly
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

> The exact sequence matches the Plasmodium yoelii DMT1 entry, whose function is annotated as an iron transporter with experimental evidence cited; the matching GO term is iron ion transmembrane transport. The GO annotation itself is computationally inferred, so it should not be mistaken for the experimental evidence.

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The many hydrophobic segments in the sequence support a multipass membrane protein, making a transport process more plausible than ribosomal or nuclear-pore assembly. But that does not identify iron as the transported ion.


**Missing item-specific fact**

> The protein-specific substrate/function assignment that this transporter transports iron; the supplied sequence and choices do not establish that specificity.


**Reason**

> The key is supported by reviewer-only protein annotation and cited experimental evidence, but the sequence-based argument supports transporter architecture, not the iron-specific GO process. The exact substrate assignment is an item-specific fact absent from the input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the listed choices, iron transport is the only one consistent with a multipass membrane transporter, though the sequence alone does not demonstrate iron specificity.


### Important caveats

- The matched UniProt function annotation cites experimental evidence, but the primary study was not independently reviewed here.
- The GO annotation is marked IEA:TreeGrafter, a computational annotation.
- The historical record matches the sequence, but the author's exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The many hydrophobic segments in the sequence support a multipass membrane protein, making a transport process more plausible than ribosomal or nuclear-pore assembly. But that does not identify iron as the transported ion.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific substrate/function assignment that this transporter transports iron; the supplied sequence and choices do not establish that specificity.",
    "reason": "The key is supported by reviewer-only protein annotation and cited experimental evidence, but the sequence-based argument supports transporter architecture, not the iron-specific GO process. The exact substrate assignment is an item-specific fact absent from the input."
  },
  "case_id": "GO_biological_process_0117",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "C6",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the Plasmodium yoelii DMT1 entry, whose function is annotated as an iron transporter with experimental evidence cited; the matching GO term is iron ion transmembrane transport. The GO annotation itself is computationally inferred, so it should not be mistaken for the experimental evidence."
  },
  "important_caveats": [
    "The matched UniProt function annotation cites experimental evidence, but the primary study was not independently reviewed here.",
    "The GO annotation is marked IEA:TreeGrafter, a computational annotation.",
    "The historical record matches the sequence, but the author's exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed choices, iron transport is the only one consistent with a multipass membrane transporter, though the sequence alone does not demonstrate iron specificity."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_biological_process_0117",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the Plasmodium yoelii DMT1 entry, whose function is annotated as an iron transporter with experimental evidence cited; the matching GO term is iron ion transmembrane transport. The GO annotation itself is computationally inferred, so it should not be mistaken for the experimental evidence.",
    "evidence_ids": ["C1", "C5", "C6", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The many hydrophobic segments in the sequence support a multipass membrane protein, making a transport process more plausible than ribosomal or nuclear-pore assembly. But that does not identify iron as the transported ion.",
    "missing_item_specific_fact": "The protein-specific substrate/function assignment that this transporter transports iron; the supplied sequence and choices do not establish that specificity.",
    "reason": "The key is supported by reviewer-only protein annotation and cited experimental evidence, but the sequence-based argument supports transporter architecture, not the iron-specific GO process. The exact substrate assignment is an item-specific fact absent from the input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed choices, iron transport is the only one consistent with a multipass membrane transporter, though the sequence alone does not demonstrate iron specificity."
  },
  "important_caveats": [
    "The matched UniProt function annotation cites experimental evidence, but the primary study was not independently reviewed here.",
    "The GO annotation is marked IEA:TreeGrafter, a computational annotation.",
    "The historical record matches the sequence, but the author's exact source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry (A0A077Y877, DMT1_PLAYE, Plasmodium yoelii) names the protein 'Divalent metal transporter 1' (PyDMT1) with experimental evidence (ECO:0000269, PubMed:38049852) stating 'Iron transporter.' The GO annotation GO:0034755 (iron ion transmembrane transport) is present (IEA:TreeGrafter), but the experimental FUNCTION annotation independently confirms iron transport activity. The sequence matches the benchmark input exactly (SHA256 confirmed). The expected answer B is well-supported by both experimental and database evidence.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The C-terminal ~500 residues of the sequence contain numerous long hydrophobic stretches (~20+ residues each, e.g., 'GPGWIVAIAYLDPG...', 'YRLLWVLVYGHILGFIFHTLSMKLGHITGLDL...', 'IAIWGAHLQAIIGVFVAINLILGIPVKIAILYTLIEAFAYSF...', 'LLIGILVCCFMFNVFMTPINFQ...', 'SLLVSCITNCIIVLTFAEVNIS...', 'SMYIWSFGLLSSG...', 'IFSRIILFIMLYAYVSYD...', 'QILLLPLAIIPLYRFSIHKNVLGKFAIKGAFKYLVFVLVISIIVANFLLTLFDFLQY...', 'VIFIFISSIFYLLFIIYFFNMPITK...'), indicating a multi-pass transmembrane protein consistent with a membrane transporter. Among the four options, only B ('iron ion transmembrane transport') describes a transmembrane transport process. Options A (defense response to bacterium), C (nuclear pore complex assembly), and D (ribosomal large subunit assembly) describe processes carried out by soluble or scaffold proteins, not multi-pass membrane transporters. The transmembrane topology visible in the sequence eliminates A, C, and D.


**Missing item-specific fact**

> The specific substrate identity (iron vs. other divalent metals) cannot be determined from sequence alone without recognizing the DMT1/NRAMP family signature. However, since B is the only transmembrane transport option among the four choices, the substrate specificity is not needed to select the correct answer.


**Reason**

> A model can observe the multi-pass transmembrane architecture from the hydrophobic stretches in the sequence and recognize that only option B describes a transmembrane transport process. Options A, C, and D are processes associated with soluble proteins (immune signaling components, nucleoporins, ribosomal assembly factors) and are incompatible with a 12-TM transporter topology. This is a concrete biological argument from the sequence itself.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options span fundamentally different biological process categories: immune defense (A), membrane transport (B), nuclear structure assembly (C), and ribosome biogenesis (D). The multi-pass transmembrane topology of the sequence is incompatible with A, C, and D as the primary biological process. B is the sole transport option, making the choice unambiguous once transmembrane architecture is recognized.


### Important caveats

- The GO:0034755 annotation carries evidence code IEA:TreeGrafter (computational inference by similarity), but the experimental FUNCTION annotation (ECO:0000269, PubMed:38049852) independently confirms iron transport, strengthening the key.
- The N-terminal asparagine-rich region (characteristic of Plasmodium proteins) is not provided as organism context in the model input; a model must rely on transmembrane topology reasoning rather than organism-specific knowledge.
- The specific 'iron' designation (vs. other divalent metals like Mn2+, Zn2+) is not derivable from sequence topology alone, but is irrelevant here because B is the only transport option.
- The UniProt entry was first publicly released in April 2025; the benchmark's author source snapshot is unknown, though the sequence has been unchanged since October 2014.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The C-terminal ~500 residues of the sequence contain numerous long hydrophobic stretches (~20+ residues each, e.g., 'GPGWIVAIAYLDPG...', 'YRLLWVLVYGHILGFIFHTLSMKLGHITGLDL...', 'IAIWGAHLQAIIGVFVAINLILGIPVKIAILYTLIEAFAYSF...', 'LLIGILVCCFMFNVFMTPINFQ...', 'SLLVSCITNCIIVLTFAEVNIS...', 'SMYIWSFGLLSSG...', 'IFSRIILFIMLYAYVSYD...', 'QILLLPLAIIPLYRFSIHKNVLGKFAIKGAFKYLVFVLVISIIVANFLLTLFDFLQY...', 'VIFIFISSIFYLLFIIYFFNMPITK...'), indicating a multi-pass transmembrane protein consistent with a membrane transporter. Among the four options, only B ('iron ion transmembrane transport') describes a transmembrane transport process. Options A (defense response to bacterium), C (nuclear pore complex assembly), and D (ribosomal large subunit assembly) describe processes carried out by soluble or scaffold proteins, not multi-pass membrane transporters. The transmembrane topology visible in the sequence eliminates A, C, and D.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The specific substrate identity (iron vs. other divalent metals) cannot be determined from sequence alone without recognizing the DMT1/NRAMP family signature. However, since B is the only transmembrane transport option among the four choices, the substrate specificity is not needed to select the correct answer.",
    "reason": "A model can observe the multi-pass transmembrane architecture from the hydrophobic stretches in the sequence and recognize that only option B describes a transmembrane transport process. Options A, C, and D are processes associated with soluble proteins (immune signaling components, nucleoporins, ribosomal assembly factors) and are incompatible with a 12-TM transporter topology. This is a concrete biological argument from the sequence itself."
  },
  "case_id": "GO_biological_process_0117",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H1",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry (A0A077Y877, DMT1_PLAYE, Plasmodium yoelii) names the protein 'Divalent metal transporter 1' (PyDMT1) with experimental evidence (ECO:0000269, PubMed:38049852) stating 'Iron transporter.' The GO annotation GO:0034755 (iron ion transmembrane transport) is present (IEA:TreeGrafter), but the experimental FUNCTION annotation independently confirms iron transport activity. The sequence matches the benchmark input exactly (SHA256 confirmed). The expected answer B is well-supported by both experimental and database evidence."
  },
  "important_caveats": [
    "The GO:0034755 annotation carries evidence code IEA:TreeGrafter (computational inference by similarity), but the experimental FUNCTION annotation (ECO:0000269, PubMed:38049852) independently confirms iron transport, strengthening the key.",
    "The N-terminal asparagine-rich region (characteristic of Plasmodium proteins) is not provided as organism context in the model input; a model must rely on transmembrane topology reasoning rather than organism-specific knowledge.",
    "The specific 'iron' designation (vs. other divalent metals like Mn2+, Zn2+) is not derivable from sequence topology alone, but is irrelevant here because B is the only transport option.",
    "The UniProt entry was first publicly released in April 2025; the benchmark's author source snapshot is unknown, though the sequence has been unchanged since October 2014."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span fundamentally different biological process categories: immune defense (A), membrane transport (B), nuclear structure assembly (C), and ribosome biogenesis (D). The multi-pass transmembrane topology of the sequence is incompatible with A, C, and D as the primary biological process. B is the sole transport option, making the choice unambiguous once transmembrane architecture is recognized."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_biological_process_0117",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry (A0A077Y877, DMT1_PLAYE, Plasmodium yoelii) names the protein 'Divalent metal transporter 1' (PyDMT1) with experimental evidence (ECO:0000269, PubMed:38049852) stating 'Iron transporter.' The GO annotation GO:0034755 (iron ion transmembrane transport) is present (IEA:TreeGrafter), but the experimental FUNCTION annotation independently confirms iron transport activity. The sequence matches the benchmark input exactly (SHA256 confirmed). The expected answer B is well-supported by both experimental and database evidence.",
    "evidence_ids": ["C4", "C5", "C6", "H1", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The C-terminal ~500 residues of the sequence contain numerous long hydrophobic stretches (~20+ residues each, e.g., 'GPGWIVAIAYLDPG...', 'YRLLWVLVYGHILGFIFHTLSMKLGHITGLDL...', 'IAIWGAHLQAIIGVFVAINLILGIPVKIAILYTLIEAFAYSF...', 'LLIGILVCCFMFNVFMTPINFQ...', 'SLLVSCITNCIIVLTFAEVNIS...', 'SMYIWSFGLLSSG...', 'IFSRIILFIMLYAYVSYD...', 'QILLLPLAIIPLYRFSIHKNVLGKFAIKGAFKYLVFVLVISIIVANFLLTLFDFLQY...', 'VIFIFISSIFYLLFIIYFFNMPITK...'), indicating a multi-pass transmembrane protein consistent with a membrane transporter. Among the four options, only B ('iron ion transmembrane transport') describes a transmembrane transport process. Options A (defense response to bacterium), C (nuclear pore complex assembly), and D (ribosomal large subunit assembly) describe processes carried out by soluble or scaffold proteins, not multi-pass membrane transporters. The transmembrane topology visible in the sequence eliminates A, C, and D.",
    "missing_item_specific_fact": "The specific substrate identity (iron vs. other divalent metals) cannot be determined from sequence alone without recognizing the DMT1/NRAMP family signature. However, since B is the only transmembrane transport option among the four choices, the substrate specificity is not needed to select the correct answer.",
    "reason": "A model can observe the multi-pass transmembrane architecture from the hydrophobic stretches in the sequence and recognize that only option B describes a transmembrane transport process. Options A, C, and D are processes associated with soluble proteins (immune signaling components, nucleoporins, ribosomal assembly factors) and are incompatible with a 12-TM transporter topology. This is a concrete biological argument from the sequence itself."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span fundamentally different biological process categories: immune defense (A), membrane transport (B), nuclear structure assembly (C), and ribosome biogenesis (D). The multi-pass transmembrane topology of the sequence is incompatible with A, C, and D as the primary biological process. B is the sole transport option, making the choice unambiguous once transmembrane architecture is recognized."
  },
  "important_caveats": [
    "The GO:0034755 annotation carries evidence code IEA:TreeGrafter (computational inference by similarity), but the experimental FUNCTION annotation (ECO:0000269, PubMed:38049852) independently confirms iron transport, strengthening the key.",
    "The N-terminal asparagine-rich region (characteristic of Plasmodium proteins) is not provided as organism context in the model input; a model must rely on transmembrane topology reasoning rather than organism-specific knowledge.",
    "The specific 'iron' designation (vs. other divalent metals like Mn2+, Zn2+) is not derivable from sequence topology alone, but is irrelevant here because B is the only transport option.",
    "The UniProt entry was first publicly released in April 2025; the benchmark's author source snapshot is unknown, though the sequence has been unchanged since October 2014."
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

**Accession:** `A0A077Y877` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 38. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A077Y877.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:23:53.473191+00:00.  

```json
"A0A077Y877"
```

Source SHA-256: `40ae967522d3c49e686d4ca88a1b70ecbe6d0cae59d2d1589a2e894a199b51f8`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A077Y877.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:23:53.473191+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q8I3M7","source":"UniProtKB"}],"value":"Food vacuole resident transporter 1"}}],"recommendedName":{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"38049852","source":"PubMed"}],"value":"Divalent metal transporter 1"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"38049852","source":"PubMed"}],"value":"PyDMT1"}]}}
```

Source SHA-256: `40ae967522d3c49e686d4ca88a1b70ecbe6d0cae59d2d1589a2e894a199b51f8`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A077Y877.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:23:53.473191+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"38049852","source":"PubMed"}],"value":"Iron transporter (PubMed:38049852). Required for parasite development during the blood stages (PubMed:38049852). Required for full pathogenicity (PubMed:38049852)"}]}
```

Source SHA-256: `40ae967522d3c49e686d4ca88a1b70ecbe6d0cae59d2d1589a2e894a199b51f8`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A077Y877.json)  
**Locator:** `/uniProtKBCrossReferences/16`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:23:53.473191+00:00.  

```json
{"database":"GO","id":"GO:0034755","properties":[{"key":"GoTerm","value":"P:iron ion transmembrane transport"},{"key":"GoEvidenceType","value":"IEA:TreeGrafter"}]}
```

Source SHA-256: `40ae967522d3c49e686d4ca88a1b70ecbe6d0cae59d2d1589a2e894a199b51f8`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A077Y877?format=txt&versions=38)  
**Locator:** `lines 1-15`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 38 / 1.  
**Retrieved:** 2026-11-02T04:23:55.877262+00:00.  

```text
ID   DMT1_PLAYE              Reviewed;         696 AA.
AC   A0A077Y877;
DT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.
DT   29-OCT-2014, sequence version 1.
DT   28-JAN-2026, entry version 38.
DE   RecName: Full=Divalent metal transporter 1 {ECO:0000303|PubMed:38049852};
DE            Short=PyDMT1 {ECO:0000303|PubMed:38049852};
DE   AltName: Full=Food vacuole resident transporter 1 {ECO:0000250|UniProtKB:Q8I3M7};
GN   Name=FVRT1 {ECO:0000250|UniProtKB:Q8I3M7};
GN   ORFNames=PY17X_1241800 {ECO:0000312|EMBL:VTZ80216.1},
GN   PYYM_1241000 {ECO:0000312|EMBL:CDU19580.1};
OS   Plasmodium yoelii.
OC   Eukaryota; Sar; Alveolata; Apicomplexa; Aconoidasida; Haemosporida;
OC   Plasmodiidae; Plasmodium; Plasmodium (Vinckeia).
OX   NCBI_TaxID=5861 {ECO:0000312|Proteomes:UP000072904};
```

Source SHA-256: `37d8308df1bef1cc329abc6c16923e33dab13fd5f51df70f00187771ddf50b47`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A077Y877?format=txt&versions=38)  
**Locator:** `lines 37-39`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 38 / 1.  
**Retrieved:** 2026-11-02T04:23:55.877262+00:00.  

```text
CC   -!- FUNCTION: Iron transporter (PubMed:38049852). Required for parasite
CC       development during the blood stages (PubMed:38049852). Required for
CC       full pathogenicity (PubMed:38049852). {ECO:0000269|PubMed:38049852}.
```

Source SHA-256: `37d8308df1bef1cc329abc6c16923e33dab13fd5f51df70f00187771ddf50b47`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A077Y877?format=txt&versions=38)  
**Locator:** `lines 77-77`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 38 / 1.  
**Retrieved:** 2026-11-02T04:23:55.877262+00:00.  

```text
DR   GO; GO:0034755; P:iron ion transmembrane transport; IEA:TreeGrafter.
```

Source SHA-256: `37d8308df1bef1cc329abc6c16923e33dab13fd5f51df70f00187771ddf50b47`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_biological_process.json), zero-based source row 117. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
