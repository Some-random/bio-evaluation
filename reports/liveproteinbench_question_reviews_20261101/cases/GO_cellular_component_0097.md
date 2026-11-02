# GO_cellular_component_0097

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_cellular_component`  
**Author expected answer:** **A** — plasma membrane

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | contradicted | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | contradicted | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MHQDNSMRRAINQSRNGGSDSCDINNDREHDNINRNSYINNFHIENINSDKNEQSYIYCSDRAQVTDSILGNRKYTHEENINSTEMFSRTNYEYSNKNNVDIEMYNISNNNFYNGNNNGHSNDIIDYINNNNVNKDLSNTSNNADINTYIKKLTSNQSTAYCDGKGYNESANGSNFDINFRDVIKNNNNKNYKNNNHVPDDMLELGDRSFDSSFYIHNNVEEIDTERSNRLSFMSKLKMYFNYFGPGWIVAIAYLDPGNICGNLNVGLIRSDDFINVNSSVKDYTGYRLLWVLVYGHILGFIFHTLSMKLGHITGLDLAALCRKEFSSKFSYFLYICVQIAIWGAHLQAIIGVFVAINLILGIPVKIAILYTLIEAFAYSFLENKSLDLLEKVLSLLIGILVCCFMFNVFMTPINFQEVASSILYPRIPKGKLLDTMGLLGSVISAHIFYLHSNLTSKKKPVIYNDRMVKRYNKLGTIESGGSLLVSCITNCIIVLTFAEVNISGDDRKADYNLFNAYDVMKKYFGKTSMYIWSFGLLSSGNNASFMCEYASKSVFEGFLNKNVNPFFRVIFSRIILFIMLYAYVSYDKYTIDQLSNFINVVQILLLPLAIIPLYRFSIHKNVLGKFAIKGAFKYLVFVLVISIIVANFLLTLFDFLQYAPSNLYVIFIFISSIFYLLFIIYFFNMPITKTYYKDS

[Multiple Choices]
A. plasma membrane
B. early endosome membrane
C. striated muscle dense body
D. midbody
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

### Expected-answer support: contradicted

> The sequence-matched UniProt record reports experimentally supported localization to the vacuole membrane, which conflicts with plasma membrane as the primary location asked for. Plasma membrane is present only as an IEA:TreeGrafter GO annotation, not as experimental localization evidence.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence has multiple hydrophobic transmembrane regions, supporting that it is a membrane protein, but this does not distinguish plasma membrane from an endosomal or vacuolar membrane.


**Missing item-specific fact**

> PyDMT1's specific subcellular localization, which requires protein-specific annotation or experimental evidence.


**Reason**

> The sequence supports membrane association but supplies no reliable targeting or trafficking clue that resolves these membrane compartments. The experimental localization is item-specific and was not provided to the evaluated model.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The evidence points to vacuole membrane, which is not offered. Plasma membrane has a computational GO annotation, but no supplied evidence supports early endosome membrane, striated muscle dense body, or midbody; the available choices therefore do not capture the reported experimental localization.


### Important caveats

- The sequence match is exact, but the cited experimental localization is a UniProt annotation attributed to a publication, not an independent review of that study.
- The plasma membrane annotation is computational and does not establish that plasma membrane is the primary location.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has multiple hydrophobic transmembrane regions, supporting that it is a membrane protein, but this does not distinguish plasma membrane from an endosomal or vacuolar membrane.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "PyDMT1's specific subcellular localization, which requires protein-specific annotation or experimental evidence.",
    "reason": "The sequence supports membrane association but supplies no reliable targeting or trafficking clue that resolves these membrane compartments. The experimental localization is item-specific and was not provided to the evaluated model."
  },
  "case_id": "GO_cellular_component_0097",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H3",
      "H4"
    ],
    "judgment": "contradicted",
    "reason": "The sequence-matched UniProt record reports experimentally supported localization to the vacuole membrane, which conflicts with plasma membrane as the primary location asked for. Plasma membrane is present only as an IEA:TreeGrafter GO annotation, not as experimental localization evidence."
  },
  "important_caveats": [
    "The sequence match is exact, but the cited experimental localization is a UniProt annotation attributed to a publication, not an independent review of that study.",
    "The plasma membrane annotation is computational and does not establish that plasma membrane is the primary location."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The evidence points to vacuole membrane, which is not offered. Plasma membrane has a computational GO annotation, but no supplied evidence supports early endosome membrane, striated muscle dense body, or midbody; the available choices therefore do not capture the reported experimental localization."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0097",
  "expected_answer_check": {
    "judgment": "contradicted",
    "reason": "The sequence-matched UniProt record reports experimentally supported localization to the vacuole membrane, which conflicts with plasma membrane as the primary location asked for. Plasma membrane is present only as an IEA:TreeGrafter GO annotation, not as experimental localization evidence.",
    "evidence_ids": ["C5", "C6", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence has multiple hydrophobic transmembrane regions, supporting that it is a membrane protein, but this does not distinguish plasma membrane from an endosomal or vacuolar membrane.",
    "missing_item_specific_fact": "PyDMT1's specific subcellular localization, which requires protein-specific annotation or experimental evidence.",
    "reason": "The sequence supports membrane association but supplies no reliable targeting or trafficking clue that resolves these membrane compartments. The experimental localization is item-specific and was not provided to the evaluated model."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The evidence points to vacuole membrane, which is not offered. Plasma membrane has a computational GO annotation, but no supplied evidence supports early endosome membrane, striated muscle dense body, or midbody; the available choices therefore do not capture the reported experimental localization."
  },
  "important_caveats": [
    "The sequence match is exact, but the cited experimental localization is a UniProt annotation attributed to a publication, not an independent review of that study.",
    "The plasma membrane annotation is computational and does not establish that plasma membrane is the primary location."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: contradicted

> The experimental subcellular location (ECO:0000269, PubMed:38049852) places this protein at the 'Vacuole membrane' (food vacuole), as a multi-pass membrane protein. The protein is named 'Food vacuole resident transporter 1' / 'Divalent metal transporter 1 (PyDMT1).' The only annotation supporting 'plasma membrane' (GO:0005886) carries evidence code IEA:TreeGrafter, a purely computational homology transfer, not experimental evidence. The experimental data contradicts the plasma membrane assignment; the true location is the food vacuole membrane, which is neither plasma membrane nor early endosome membrane.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5), [C4](#evidence-c4), [C8](#evidence-c8).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence clearly encodes a multi-pass membrane transporter (multiple long hydrophobic stretches in the C-terminal ~450 residues, preceded by a very long hydrophilic N-terminal domain). This eliminates options C (striated muscle dense body — impossible in Plasmodium, which lacks striated muscle) and D (midbody — a cytokinesis bridge structure, not a transporter location). However, distinguishing between plasma membrane (A) and early endosome membrane (B) for a multi-pass transporter requires knowledge of the specific protein identity, its targeting signals, or its experimentally determined localization — none of which are derivable from the sequence alone.


**Missing item-specific fact**

> The experimental localization of this protein to the food vacuole membrane (per PubMed:38049852) is the critical fact. Without knowing this is PyDMT1/FVRT1 localized to the food vacuole (a compartment more analogous to endosome/lysosome than plasma membrane), a model cannot distinguish A from B by sequence reasoning alone.


**Reason**

> While the sequence supports 'membrane protein' and eliminates C and D, the A-vs-B distinction for a multi-pass transporter cannot be resolved by general biological reasoning from the sequence. It requires the specific experimental annotation that this transporter resides on the food vacuole membrane.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "B"
]
```

> The true experimental location is the food vacuole membrane, which is not among the options. Between the two membrane options (A: plasma membrane, B: early endosome membrane), the food vacuole is functionally and topologically closer to an endosomal/lysosomal compartment than to the plasma membrane, making B arguably more defensible than A. The expected answer A is supported only by a weak IEA:TreeGrafter computational annotation that is contradicted by experimental data.


### Important caveats

- The expected answer 'plasma membrane' is supported only by an IEA:TreeGrafter (automated computational transfer) annotation, not by experimental evidence.
- The experimentally determined location (ECO:0000269, PubMed:38049852) is 'Vacuole membrane' (food vacuole), which is not offered as an option.
- The food vacuole in Plasmodium is a digestive organelle more analogous to a lysosome/endosome than to the plasma membrane, making option B potentially closer to the true location than option A.
- The GO:0005886 (plasma membrane) annotation is a homology-based computational transfer (IEA:TreeGrafter) and should not be treated as equivalent to experimental evidence.
- The sequence matches the UniProt entry A0A077Y877 exactly (696 aa), confirmed in both current and historical (v38) records.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence clearly encodes a multi-pass membrane transporter (multiple long hydrophobic stretches in the C-terminal ~450 residues, preceded by a very long hydrophilic N-terminal domain). This eliminates options C (striated muscle dense body — impossible in Plasmodium, which lacks striated muscle) and D (midbody — a cytokinesis bridge structure, not a transporter location). However, distinguishing between plasma membrane (A) and early endosome membrane (B) for a multi-pass transporter requires knowledge of the specific protein identity, its targeting signals, or its experimentally determined localization — none of which are derivable from the sequence alone.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The experimental localization of this protein to the food vacuole membrane (per PubMed:38049852) is the critical fact. Without knowing this is PyDMT1/FVRT1 localized to the food vacuole (a compartment more analogous to endosome/lysosome than plasma membrane), a model cannot distinguish A from B by sequence reasoning alone.",
    "reason": "While the sequence supports 'membrane protein' and eliminates C and D, the A-vs-B distinction for a multi-pass transporter cannot be resolved by general biological reasoning from the sequence. It requires the specific experimental annotation that this transporter resides on the food vacuole membrane."
  },
  "case_id": "GO_cellular_component_0097",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "C7",
      "H3",
      "H4",
      "H5",
      "C4",
      "C8"
    ],
    "judgment": "contradicted",
    "reason": "The experimental subcellular location (ECO:0000269, PubMed:38049852) places this protein at the 'Vacuole membrane' (food vacuole), as a multi-pass membrane protein. The protein is named 'Food vacuole resident transporter 1' / 'Divalent metal transporter 1 (PyDMT1).' The only annotation supporting 'plasma membrane' (GO:0005886) carries evidence code IEA:TreeGrafter, a purely computational homology transfer, not experimental evidence. The experimental data contradicts the plasma membrane assignment; the true location is the food vacuole membrane, which is neither plasma membrane nor early endosome membrane."
  },
  "important_caveats": [
    "The expected answer 'plasma membrane' is supported only by an IEA:TreeGrafter (automated computational transfer) annotation, not by experimental evidence.",
    "The experimentally determined location (ECO:0000269, PubMed:38049852) is 'Vacuole membrane' (food vacuole), which is not offered as an option.",
    "The food vacuole in Plasmodium is a digestive organelle more analogous to a lysosome/endosome than to the plasma membrane, making option B potentially closer to the true location than option A.",
    "The GO:0005886 (plasma membrane) annotation is a homology-based computational transfer (IEA:TreeGrafter) and should not be treated as equivalent to experimental evidence.",
    "The sequence matches the UniProt entry A0A077Y877 exactly (696 aa), confirmed in both current and historical (v38) records."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "B"
    ],
    "reason": "The true experimental location is the food vacuole membrane, which is not among the options. Between the two membrane options (A: plasma membrane, B: early endosome membrane), the food vacuole is functionally and topologically closer to an endosomal/lysosomal compartment than to the plasma membrane, making B arguably more defensible than A. The expected answer A is supported only by a weak IEA:TreeGrafter computational annotation that is contradicted by experimental data."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0097",
  "expected_answer_check": {
    "judgment": "contradicted",
    "reason": "The experimental subcellular location (ECO:0000269, PubMed:38049852) places this protein at the 'Vacuole membrane' (food vacuole), as a multi-pass membrane protein. The protein is named 'Food vacuole resident transporter 1' / 'Divalent metal transporter 1 (PyDMT1).' The only annotation supporting 'plasma membrane' (GO:0005886) carries evidence code IEA:TreeGrafter, a purely computational homology transfer, not experimental evidence. The experimental data contradicts the plasma membrane assignment; the true location is the food vacuole membrane, which is neither plasma membrane nor early endosome membrane.",
    "evidence_ids": ["C5", "C6", "C7", "H3", "H4", "H5", "C4", "C8"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence clearly encodes a multi-pass membrane transporter (multiple long hydrophobic stretches in the C-terminal ~450 residues, preceded by a very long hydrophilic N-terminal domain). This eliminates options C (striated muscle dense body — impossible in Plasmodium, which lacks striated muscle) and D (midbody — a cytokinesis bridge structure, not a transporter location). However, distinguishing between plasma membrane (A) and early endosome membrane (B) for a multi-pass transporter requires knowledge of the specific protein identity, its targeting signals, or its experimentally determined localization — none of which are derivable from the sequence alone.",
    "missing_item_specific_fact": "The experimental localization of this protein to the food vacuole membrane (per PubMed:38049852) is the critical fact. Without knowing this is PyDMT1/FVRT1 localized to the food vacuole (a compartment more analogous to endosome/lysosome than plasma membrane), a model cannot distinguish A from B by sequence reasoning alone.",
    "reason": "While the sequence supports 'membrane protein' and eliminates C and D, the A-vs-B distinction for a multi-pass transporter cannot be resolved by general biological reasoning from the sequence. It requires the specific experimental annotation that this transporter resides on the food vacuole membrane."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "B"],
    "reason": "The true experimental location is the food vacuole membrane, which is not among the options. Between the two membrane options (A: plasma membrane, B: early endosome membrane), the food vacuole is functionally and topologically closer to an endosomal/lysosomal compartment than to the plasma membrane, making B arguably more defensible than A. The expected answer A is supported only by a weak IEA:TreeGrafter computational annotation that is contradicted by experimental data."
  },
  "important_caveats": [
    "The expected answer 'plasma membrane' is supported only by an IEA:TreeGrafter (automated computational transfer) annotation, not by experimental evidence.",
    "The experimentally determined location (ECO:0000269, PubMed:38049852) is 'Vacuole membrane' (food vacuole), which is not offered as an option.",
    "The food vacuole in Plasmodium is a digestive organelle more analogous to a lysosome/endosome than to the plasma membrane, making option B potentially closer to the true location than option A.",
    "The GO:0005886 (plasma membrane) annotation is a homology-based computational transfer (IEA:TreeGrafter) and should not be treated as equivalent to experimental evidence.",
    "The sequence matches the UniProt entry A0A077Y877 exactly (696 aa), confirmed in both current and historical (v38) records."
  ]
}
```

</details>

## Existing project source checks of Luna’s review

The notes below were prepared for specific claims in the Luna review. They are not independent validation of Qwen’s claims, expert adjudication, or replacement verdicts.

## Project source-check notes

These project-authored, AI-assisted checks assess specific source claims. They are not expert adjudication and do not replace Luna’s saved review or the author key.

### Source check 1

**Check:** `mixed_location_annotations_require_qualification`.

> C5/H3 annotate vacuole membrane with ECO:0000269; C6/H4 separately carry plasma membrane as IEA:TreeGrafter.

**Remaining uncertainty:** The excerpts favor a different experimentally annotated location but do not independently establish that plasma-membrane localization never occurs.

Evidence checked: [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H4](#evidence-h4).

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
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:23:53.473191+00:00.  

```json
{"commentType":"SUBCELLULAR LOCATION","subcellularLocations":[{"location":{"evidences":[{"evidenceCode":"ECO:0000269","id":"38049852","source":"PubMed"}],"id":"SL-0271","value":"Vacuole membrane"},"topology":{"evidences":[{"evidenceCode":"ECO:0000255"}],"id":"SL-9909","value":"Multi-pass membrane protein"}}]}
```

Source SHA-256: `40ae967522d3c49e686d4ca88a1b70ecbe6d0cae59d2d1589a2e894a199b51f8`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A077Y877.json)  
**Locator:** `/uniProtKBCrossReferences/12`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:23:53.473191+00:00.  

```json
{"database":"GO","id":"GO:0005886","properties":[{"key":"GoTerm","value":"C:plasma membrane"},{"key":"GoEvidenceType","value":"IEA:TreeGrafter"}]}
```

Source SHA-256: `40ae967522d3c49e686d4ca88a1b70ecbe6d0cae59d2d1589a2e894a199b51f8`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A077Y877.json)  
**Locator:** `/uniProtKBCrossReferences/13`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:23:53.473191+00:00.  

```json
{"database":"GO","id":"GO:0005774","properties":[{"key":"GoTerm","value":"C:vacuolar membrane"},{"key":"GoEvidenceType","value":"IEA:UniProtKB-SubCell"}]}
```

Source SHA-256: `40ae967522d3c49e686d4ca88a1b70ecbe6d0cae59d2d1589a2e894a199b51f8`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A077Y877.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:23:53.473191+00:00.  

```json
{"citation":{"authors":["Zhong M.","Zhou B."],"citationCrossReferences":[{"database":"PubMed","id":"38049852"},{"database":"DOI","id":"10.1186/s12915-023-01776-y"}],"citationType":"journal article","firstPage":"279","id":"38049852","journal":"BMC Biol.","lastPage":"279","publicationDate":"2023","title":"Plasmodium yoelii iron transporter PyDMT1 interacts with host ferritin and is required in full activity for malarial pathogenesis.","volume":"21"},"evidences":[{"evidenceCode":"ECO:0000305"}],"referenceNumber":2,"referencePositions":["FUNCTION","TRANSPORTER ACTIVITY","SUBCELLULAR LOCATION","DISRUPTION PHENOTYPE"]}
```

Source SHA-256: `40ae967522d3c49e686d4ca88a1b70ecbe6d0cae59d2d1589a2e894a199b51f8`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A077Y877?format=txt&versions=38)  
**Locator:** `lines 43-44`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 38 / 1.  
**Retrieved:** 2026-11-02T04:23:55.877262+00:00.  

```text
CC   -!- SUBCELLULAR LOCATION: Vacuole membrane {ECO:0000269|PubMed:38049852};
CC       Multi-pass membrane protein {ECO:0000255}.
```

Source SHA-256: `37d8308df1bef1cc329abc6c16923e33dab13fd5f51df70f00187771ddf50b47`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A077Y877?format=txt&versions=38)  
**Locator:** `lines 73-73`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 38 / 1.  
**Retrieved:** 2026-11-02T04:23:55.877262+00:00.  

```text
DR   GO; GO:0005886; C:plasma membrane; IEA:TreeGrafter.
```

Source SHA-256: `37d8308df1bef1cc329abc6c16923e33dab13fd5f51df70f00187771ddf50b47`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A077Y877?format=txt&versions=38)  
**Locator:** `lines 74-74`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 38 / 1.  
**Retrieved:** 2026-11-02T04:23:55.877262+00:00.  

```text
DR   GO; GO:0005774; C:vacuolar membrane; IEA:UniProtKB-SubCell.
```

Source SHA-256: `37d8308df1bef1cc329abc6c16923e33dab13fd5f51df70f00187771ddf50b47`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 97. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
