# transmembrane_0124

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `transmembrane`  
**Author expected answer:** **B** — 152..172; 193..223; 229..254; 266..284; 326..348; 360..378; 390..410; 431..452

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MAPPAARARYIANKADNQILSKKPPKRPGLNGNNKTKEATPAGKKKDKDAKKRNQPTSGGQEKGLPNPIMPSVQTAFKTFVSARLCSAIWAYIADCDETFNYWEPLHYIINGHGLQTWEYSPQFGLRSYTYLLLQGVPGYFYQKLFNPSPILIFYMVRCMLGFGCAVMERYMYKSICQEFGIHIGRLWLIFQLFSVGMFVSSTALLPSSFSMYFGCAALAAWWQQNYCFAIFLTAISALLGWPFAALIGIPLVLEMLLRQRDWKTFVQWTLISGATVAIPMIAIDTSYFGKLTFAPLNIVWYNVFTSHGPNIFGTEPLSYYIINGFLNFNIIWLLALQLPIMLVIDYLIVPAKSKSTLNFPHYISLAPLYLWLLVFFAQPHKEERFLFPIYPLISLCGAITVDVYQRIFFRMKSVVFKIKAGVHYLDHSMFIAILVMVTSTLLGLSRVFALYRNYHAPMDLMLELNQFKATPQYDPDVIYNVCIGKDWHRYPGSFFFPAKNFRLRFLKSEFRGMLPAYYDEGQNATKVVQPYFNDLNQENEHMYFDYDRCDFLVDFDEGKYTALEPNYSKRSKDWSVMKSLPFLIPEKSHKVLRAFYVPFLTDNHIQYGDFNLLKRKTKRNGR

[Multiple Choices]
A. 152..172; 189..222; 229..254; 266..284; 326..348; 360..378; 390..410; 431..452
B. 152..172; 193..223; 229..254; 266..284; 326..348; 360..378; 390..410; 431..452
C. 193..223; 229..254; 266..284; 326..348; 360..378; 390..410; 431..452
D. 61..81; 91..111; 169..189; 192..212; 276..296; 317..337; 789..809; 830..850; 908..928; 929..949; 1033..1053; 1058..1078
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Transmembrane Region Prediction, which is to predict a region of the protein that spans across a cell membrane. These transmembrane domains are typically hydrophobic alpha-helices that anchor the protein within the lipid bilayer or form channels. Based on the provided amino acid sequence, you must select the option that correctly identifies the start and end positions of a segment that crosses the membrane.. The inputs provided by the user for this task include:

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

> The supplied sequence matches the 623-aa UniProt entry, whose current and historical annotations list all eight transmembrane intervals in B, including 193..223. These are RuleBase computational annotations, not evidence of experimental validation.

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [C9](#evidence-c9), [C10](#evidence-c10), [C11](#evidence-c11), [C12](#evidence-c12), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6), [H7](#evidence-h7), [H8](#evidence-h8), [H9](#evidence-h9).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence contains multiple strongly hydrophobic stretches consistent with a multi-pass membrane protein, which supports predicting transmembrane helices in broad regions.


**Missing item-specific fact**

> The precise annotated boundaries, especially 193..223 rather than the nearby 189..222, are protein-specific and are not established by a general biological rule in the input.


**Reason**

> Sequence hydrophobicity can guide prediction, but it does not reliably settle the close endpoint differences among the choices. Selecting B's exact annotated intervals depends on a protein-specific annotation or prediction absent from the input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "B"
]
```

> A and B differ only in the boundaries of one helix, by a few residues. Membrane-helix boundaries are prediction-dependent and not physically sharp; without a specified annotation convention, the sequence alone does not clearly rule out A as an approximate predicted span. B matches the cited UniProt annotation.


### Important caveats

- The sequence match supports applying the cited UniProt record to this sequence, but the accession and annotations were reviewer-only information.
- The transmembrane features are computational RuleBase annotations; the supplied evidence does not independently establish experimental membrane-spanning boundaries.
- The author’s exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains multiple strongly hydrophobic stretches consistent with a multi-pass membrane protein, which supports predicting transmembrane helices in broad regions.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The precise annotated boundaries, especially 193..223 rather than the nearby 189..222, are protein-specific and are not established by a general biological rule in the input.",
    "reason": "Sequence hydrophobicity can guide prediction, but it does not reliably settle the close endpoint differences among the choices. Selecting B's exact annotated intervals depends on a protein-specific annotation or prediction absent from the input."
  },
  "case_id": "transmembrane_0124",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "C6",
      "C7",
      "C8",
      "C9",
      "C10",
      "C11",
      "C12",
      "H2",
      "H3",
      "H4",
      "H5",
      "H6",
      "H7",
      "H8",
      "H9"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence matches the 623-aa UniProt entry, whose current and historical annotations list all eight transmembrane intervals in B, including 193..223. These are RuleBase computational annotations, not evidence of experimental validation."
  },
  "important_caveats": [
    "The sequence match supports applying the cited UniProt record to this sequence, but the accession and annotations were reviewer-only information.",
    "The transmembrane features are computational RuleBase annotations; the supplied evidence does not independently establish experimental membrane-spanning boundaries.",
    "The author’s exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "B"
    ],
    "reason": "A and B differ only in the boundaries of one helix, by a few residues. Membrane-helix boundaries are prediction-dependent and not physically sharp; without a specified annotation convention, the sequence alone does not clearly rule out A as an approximate predicted span. B matches the cited UniProt annotation."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0124",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence matches the 623-aa UniProt entry, whose current and historical annotations list all eight transmembrane intervals in B, including 193..223. These are RuleBase computational annotations, not evidence of experimental validation.",
    "evidence_ids": ["C1", "C5", "C6", "C7", "C8", "C9", "C10", "C11", "C12", "H2", "H3", "H4", "H5", "H6", "H7", "H8", "H9"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence contains multiple strongly hydrophobic stretches consistent with a multi-pass membrane protein, which supports predicting transmembrane helices in broad regions.",
    "missing_item_specific_fact": "The precise annotated boundaries, especially 193..223 rather than the nearby 189..222, are protein-specific and are not established by a general biological rule in the input.",
    "reason": "Sequence hydrophobicity can guide prediction, but it does not reliably settle the close endpoint differences among the choices. Selecting B's exact annotated intervals depends on a protein-specific annotation or prediction absent from the input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "B"],
    "reason": "A and B differ only in the boundaries of one helix, by a few residues. Membrane-helix boundaries are prediction-dependent and not physically sharp; without a specified annotation convention, the sequence alone does not clearly rule out A as an approximate predicted span. B matches the cited UniProt annotation."
  },
  "important_caveats": [
    "The sequence match supports applying the cited UniProt record to this sequence, but the accession and annotations were reviewer-only information.",
    "The transmembrane features are computational RuleBase annotations; the supplied evidence does not independently establish experimental membrane-spanning boundaries.",
    "The author’s exact source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry Q9VBV8 (ALG9_DROME, 623 AA) annotates exactly eight transmembrane helical regions: 152..172, 193..223, 229..254, 266..284, 326..348, 360..378, 390..410, 431..452. These match choice B precisely. The evidence codes are ECO:0000255|RuleBase:RU363075, indicating computational (rule-based) predictions rather than experimental measurements, but the annotation is present and consistent across both the current entry (v176) and the historical archived entry (v174). The sequence SHA-256 of the benchmark input matches the UniProt sequence.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [C9](#evidence-c9), [C10](#evidence-c10), [C11](#evidence-c11), [C12](#evidence-c12), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6), [H7](#evidence-h7), [H8](#evidence-h8), [H9](#evidence-h9).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> General hydrophobicity analysis can identify that a TM helix exists in the ~150-220 region and can eliminate C (missing first TM) and D (positions exceeding the 623-residue sequence length). However, the critical discrimination between A (189..222) and B (193..223) hinges on a 4-residue shift at the N-terminus and 1-residue shift at the C-terminus of the second TM segment. These boundaries fall within the typical uncertainty window of any hydrophobicity-based TM predictor, and no general biological principle reliably selects 193 over 189 as the helix start.


**Missing item-specific fact**

> The exact output of the RuleBase:RU363075 prediction algorithm for this specific sequence, which defines the precise residue boundaries (193 vs 189; 223 vs 222). This is a protein-specific computational annotation not derivable from general biological reasoning alone.


**Reason**

> Eliminating C and D is straightforward (missing region; out-of-range positions). But choosing B over A requires knowing the exact boundaries assigned by a particular prediction tool. A 4-residue boundary difference is well within the resolution limit of hydrophobicity-window methods, so no general biological argument reliably distinguishes 189..222 from 193..223 without access to the specific annotation or algorithm output.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "B"
]
```

> Both A and B list eight TM regions that are biologically plausible for this sequence. The only difference is the second TM boundary (189..222 vs 193..223), a shift of 4 residues at the start and 1 at the end. Without the specific RuleBase prediction output, a careful hydrophobicity analysis could reasonably place the helix boundary at either 189 or 193, making both options defensible from sequence alone. C and D are clearly eliminable.


### Important caveats

- All TM annotations are computational predictions (ECO:0000255, RuleBase), not experimentally validated boundaries.
- The UniProt accession Q9VBV8 was inferred by the reviewer from dataset metadata; it was not provided to the evaluated model.
- The sequence in the question (623 AA) matches the UniProt sequence exactly (SHA-256 confirmed), so numbering is consistent.
- Choice D contains positions (789..809, 830..850, 908..928, 929..949, 1033..1053, 1058..1078) that exceed the 623-residue sequence length, making it trivially eliminable.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "General hydrophobicity analysis can identify that a TM helix exists in the ~150-220 region and can eliminate C (missing first TM) and D (positions exceeding the 623-residue sequence length). However, the critical discrimination between A (189..222) and B (193..223) hinges on a 4-residue shift at the N-terminus and 1-residue shift at the C-terminus of the second TM segment. These boundaries fall within the typical uncertainty window of any hydrophobicity-based TM predictor, and no general biological principle reliably selects 193 over 189 as the helix start.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The exact output of the RuleBase:RU363075 prediction algorithm for this specific sequence, which defines the precise residue boundaries (193 vs 189; 223 vs 222). This is a protein-specific computational annotation not derivable from general biological reasoning alone.",
    "reason": "Eliminating C and D is straightforward (missing region; out-of-range positions). But choosing B over A requires knowing the exact boundaries assigned by a particular prediction tool. A 4-residue boundary difference is well within the resolution limit of hydrophobicity-window methods, so no general biological argument reliably distinguishes 189..222 from 193..223 without access to the specific annotation or algorithm output."
  },
  "case_id": "transmembrane_0124",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "C7",
      "C8",
      "C9",
      "C10",
      "C11",
      "C12",
      "H2",
      "H3",
      "H4",
      "H5",
      "H6",
      "H7",
      "H8",
      "H9"
    ],
    "judgment": "supported",
    "reason": "UniProt entry Q9VBV8 (ALG9_DROME, 623 AA) annotates exactly eight transmembrane helical regions: 152..172, 193..223, 229..254, 266..284, 326..348, 360..378, 390..410, 431..452. These match choice B precisely. The evidence codes are ECO:0000255|RuleBase:RU363075, indicating computational (rule-based) predictions rather than experimental measurements, but the annotation is present and consistent across both the current entry (v176) and the historical archived entry (v174). The sequence SHA-256 of the benchmark input matches the UniProt sequence."
  },
  "important_caveats": [
    "All TM annotations are computational predictions (ECO:0000255, RuleBase), not experimentally validated boundaries.",
    "The UniProt accession Q9VBV8 was inferred by the reviewer from dataset metadata; it was not provided to the evaluated model.",
    "The sequence in the question (623 AA) matches the UniProt sequence exactly (SHA-256 confirmed), so numbering is consistent.",
    "Choice D contains positions (789..809, 830..850, 908..928, 929..949, 1033..1053, 1058..1078) that exceed the 623-residue sequence length, making it trivially eliminable."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "B"
    ],
    "reason": "Both A and B list eight TM regions that are biologically plausible for this sequence. The only difference is the second TM boundary (189..222 vs 193..223), a shift of 4 residues at the start and 1 at the end. Without the specific RuleBase prediction output, a careful hydrophobicity analysis could reasonably place the helix boundary at either 189 or 193, making both options defensible from sequence alone. C and D are clearly eliminable."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{"case_id":"transmembrane_0124","expected_answer_check":{"judgment":"supported","reason":"UniProt entry Q9VBV8 (ALG9_DROME, 623 AA) annotates exactly eight transmembrane helical regions: 152..172, 193..223, 229..254, 266..284, 326..348, 360..378, 390..410, 431..452. These match choice B precisely. The evidence codes are ECO:0000255|RuleBase:RU363075, indicating computational (rule-based) predictions rather than experimental measurements, but the annotation is present and consistent across both the current entry (v176) and the historical archived entry (v174). The sequence SHA-256 of the benchmark input matches the UniProt sequence.","evidence_ids":["C5","C6","C7","C8","C9","C10","C11","C12","H2","H3","H4","H5","H6","H7","H8","H9"]},"answerability_check":{"judgment":"lookup_or_memorization_dependent","discriminating_biological_argument":"General hydrophobicity analysis can identify that a TM helix exists in the ~150-220 region and can eliminate C (missing first TM) and D (positions exceeding the 623-residue sequence length). However, the critical discrimination between A (189..222) and B (193..223) hinges on a 4-residue shift at the N-terminus and 1-residue shift at the C-terminus of the second TM segment. These boundaries fall within the typical uncertainty window of any hydrophobicity-based TM predictor, and no general biological principle reliably selects 193 over 189 as the helix start.","missing_item_specific_fact":"The exact output of the RuleBase:RU363075 prediction algorithm for this specific sequence, which defines the precise residue boundaries (193 vs 189; 223 vs 222). This is a protein-specific computational annotation not derivable from general biological reasoning alone.","reason":"Eliminating C and D is straightforward (missing region; out-of-range positions). But choosing B over A requires knowing the exact boundaries assigned by a particular prediction tool. A 4-residue boundary difference is well within the resolution limit of hydrophobicity-window methods, so no general biological argument reliably distinguishes 189..222 from 193..223 without access to the specific annotation or algorithm output."},"question_ambiguity":{"multiple_defensible_options":["A","B"],"reason":"Both A and B list eight TM regions that are biologically plausible for this sequence. The only difference is the second TM boundary (189..222 vs 193..223), a shift of 4 residues at the start and 1 at the end. Without the specific RuleBase prediction output, a careful hydrophobicity analysis could reasonably place the helix boundary at either 189 or 193, making both options defensible from sequence alone. C and D are clearly eliminable."},"important_caveats":["All TM annotations are computational predictions (ECO:0000255, RuleBase), not experimentally validated boundaries.","The UniProt accession Q9VBV8 was inferred by the reviewer from dataset metadata; it was not provided to the evaluated model.","The sequence in the question (623 AA) matches the UniProt sequence exactly (SHA-256 confirmed), so numbering is consistent.","Choice D contains positions (789..809, 830..850, 908..928, 929..949, 1033..1053, 1058..1078) that exceed the 623-residue sequence length, making it trivially eliminable."]}
```

</details>

## Existing project source checks of Luna’s review

The notes below were prepared for specific claims in the Luna review. They are not independent validation of Qwen’s claims, expert adjudication, or replacement verdicts.

## Project source-check notes

These project-authored, AI-assisted checks assess specific source claims. They are not expert adjudication and do not replace Luna’s saved review or the author key.

No additional case-specific project note was recorded. Citation membership checks do not establish that every scientific argument is correct.

## Reviewer-only source evidence

**Both reviewers received this source evidence separately from the original question. It was not available to the original evaluated model.** Source support and reasoning from the original sequence/choices are distinct assessments.

**Accession:** `Q9VBV8` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 174. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VBV8.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:29.193985+00:00.  

```json
"Q9VBV8"
```

Source SHA-256: `24b898b648022de52a5691dcf6976ea8900e27682aaaa66849096b4d46e10d5f`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VBV8.json)  
**Locator:** `/features/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:29.193985+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255","id":"RU363075","source":"RuleBase"}],"location":{"end":{"modifier":"EXACT","value":172},"start":{"modifier":"EXACT","value":152}},"type":"Transmembrane"}
```

Source SHA-256: `24b898b648022de52a5691dcf6976ea8900e27682aaaa66849096b4d46e10d5f`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VBV8.json)  
**Locator:** `/features/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:29.193985+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255","id":"RU363075","source":"RuleBase"}],"location":{"end":{"modifier":"EXACT","value":223},"start":{"modifier":"EXACT","value":193}},"type":"Transmembrane"}
```

Source SHA-256: `24b898b648022de52a5691dcf6976ea8900e27682aaaa66849096b4d46e10d5f`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VBV8.json)  
**Locator:** `/features/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:29.193985+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255","id":"RU363075","source":"RuleBase"}],"location":{"end":{"modifier":"EXACT","value":254},"start":{"modifier":"EXACT","value":229}},"type":"Transmembrane"}
```

Source SHA-256: `24b898b648022de52a5691dcf6976ea8900e27682aaaa66849096b4d46e10d5f`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VBV8.json)  
**Locator:** `/features/4`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:29.193985+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255","id":"RU363075","source":"RuleBase"}],"location":{"end":{"modifier":"EXACT","value":284},"start":{"modifier":"EXACT","value":266}},"type":"Transmembrane"}
```

Source SHA-256: `24b898b648022de52a5691dcf6976ea8900e27682aaaa66849096b4d46e10d5f`.

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VBV8.json)  
**Locator:** `/features/5`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:29.193985+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255","id":"RU363075","source":"RuleBase"}],"location":{"end":{"modifier":"EXACT","value":348},"start":{"modifier":"EXACT","value":326}},"type":"Transmembrane"}
```

Source SHA-256: `24b898b648022de52a5691dcf6976ea8900e27682aaaa66849096b4d46e10d5f`.

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VBV8.json)  
**Locator:** `/features/6`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:29.193985+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255","id":"RU363075","source":"RuleBase"}],"location":{"end":{"modifier":"EXACT","value":378},"start":{"modifier":"EXACT","value":360}},"type":"Transmembrane"}
```

Source SHA-256: `24b898b648022de52a5691dcf6976ea8900e27682aaaa66849096b4d46e10d5f`.

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VBV8.json)  
**Locator:** `/features/7`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:29.193985+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255","id":"RU363075","source":"RuleBase"}],"location":{"end":{"modifier":"EXACT","value":410},"start":{"modifier":"EXACT","value":390}},"type":"Transmembrane"}
```

Source SHA-256: `24b898b648022de52a5691dcf6976ea8900e27682aaaa66849096b4d46e10d5f`.

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VBV8.json)  
**Locator:** `/features/8`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:29.193985+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255","id":"RU363075","source":"RuleBase"}],"location":{"end":{"modifier":"EXACT","value":452},"start":{"modifier":"EXACT","value":431}},"type":"Transmembrane"}
```

Source SHA-256: `24b898b648022de52a5691dcf6976ea8900e27682aaaa66849096b4d46e10d5f`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VBV8?format=txt&versions=174)  
**Locator:** `lines 193-195`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 174 / 1.  
**Retrieved:** 2026-11-01T06:28:51.427257+00:00.  

```text
FT   TRANSMEM        152..172
FT                   /note="Helical"
FT                   /evidence="ECO:0000255|RuleBase:RU363075"
```

Source SHA-256: `32d28578b9cd594cb2408d344ac0c5be7d01172b1298053b690508892af4f5f8`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VBV8?format=txt&versions=174)  
**Locator:** `lines 196-198`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 174 / 1.  
**Retrieved:** 2026-11-01T06:28:51.427257+00:00.  

```text
FT   TRANSMEM        193..223
FT                   /note="Helical"
FT                   /evidence="ECO:0000255|RuleBase:RU363075"
```

Source SHA-256: `32d28578b9cd594cb2408d344ac0c5be7d01172b1298053b690508892af4f5f8`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VBV8?format=txt&versions=174)  
**Locator:** `lines 199-201`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 174 / 1.  
**Retrieved:** 2026-11-01T06:28:51.427257+00:00.  

```text
FT   TRANSMEM        229..254
FT                   /note="Helical"
FT                   /evidence="ECO:0000255|RuleBase:RU363075"
```

Source SHA-256: `32d28578b9cd594cb2408d344ac0c5be7d01172b1298053b690508892af4f5f8`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VBV8?format=txt&versions=174)  
**Locator:** `lines 202-204`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 174 / 1.  
**Retrieved:** 2026-11-01T06:28:51.427257+00:00.  

```text
FT   TRANSMEM        266..284
FT                   /note="Helical"
FT                   /evidence="ECO:0000255|RuleBase:RU363075"
```

Source SHA-256: `32d28578b9cd594cb2408d344ac0c5be7d01172b1298053b690508892af4f5f8`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VBV8?format=txt&versions=174)  
**Locator:** `lines 205-207`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 174 / 1.  
**Retrieved:** 2026-11-01T06:28:51.427257+00:00.  

```text
FT   TRANSMEM        326..348
FT                   /note="Helical"
FT                   /evidence="ECO:0000255|RuleBase:RU363075"
```

Source SHA-256: `32d28578b9cd594cb2408d344ac0c5be7d01172b1298053b690508892af4f5f8`.

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VBV8?format=txt&versions=174)  
**Locator:** `lines 208-210`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 174 / 1.  
**Retrieved:** 2026-11-01T06:28:51.427257+00:00.  

```text
FT   TRANSMEM        360..378
FT                   /note="Helical"
FT                   /evidence="ECO:0000255|RuleBase:RU363075"
```

Source SHA-256: `32d28578b9cd594cb2408d344ac0c5be7d01172b1298053b690508892af4f5f8`.

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VBV8?format=txt&versions=174)  
**Locator:** `lines 211-213`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 174 / 1.  
**Retrieved:** 2026-11-01T06:28:51.427257+00:00.  

```text
FT   TRANSMEM        390..410
FT                   /note="Helical"
FT                   /evidence="ECO:0000255|RuleBase:RU363075"
```

Source SHA-256: `32d28578b9cd594cb2408d344ac0c5be7d01172b1298053b690508892af4f5f8`.

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VBV8?format=txt&versions=174)  
**Locator:** `lines 214-216`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 174 / 1.  
**Retrieved:** 2026-11-01T06:28:51.427257+00:00.  

```text
FT   TRANSMEM        431..452
FT                   /note="Helical"
FT                   /evidence="ECO:0000255|RuleBase:RU363075"
```

Source SHA-256: `32d28578b9cd594cb2408d344ac0c5be7d01172b1298053b690508892af4f5f8`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json), zero-based source row 124. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
