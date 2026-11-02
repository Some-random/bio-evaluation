# transmembrane_0080

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `transmembrane`  
**Author expected answer:** **D** — 4..24; 81..101; 116..136; 158..178; 181..201; 228..248; 271..291; 309..329

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MLHLTPLIFLSLAMAAAVGVWGVFTWNGGFDEMDGIVASHQSTGILGLQHCPDLDRGLMSMVAFNLPVVGRNPIFPAGRRFMVQFLANVAVIPVILNTEGARAEPGSLVRYSTTWGLFSQMATSAVMCPLYGFWFVRQSGAKQTEGGTLRPLPPNKWVVPSSVLIGYGIPALLSFDPFQWGLDLQIRGILAFTLYPLCISLTARLMRKVSKKRGRSLSPEWNSTISYVAVGVVGMVSHLWYLGTGLTGYPLSGDAVSSVAGPTEVGRAAQLVLLFLQIDYVITFAAMLLLAWHELTRHQLVRSWRAAGTLAVGWLFLGPGATLAAAWALREQWLSRPRGVRGEIKQKPK

[Multiple Choices]
A. 14..34; 78..98; 114..134; 137..157; 162..182; 193..213; 235..255; 328..348; 380..400; 471..491
B. 4..24; 80..105; 116..136; 158..178; 181..201; 228..248; 271..291; 309..329
C. 81..101; 116..136; 158..178; 181..201; 228..248; 271..291; 309..329
D. 4..24; 81..101; 116..136; 158..178; 181..201; 228..248; 271..291; 309..329
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

> The sequence matches the historical UniProt record, whose transmembrane annotations match choice D exactly. These annotations are computational (ECO:0000255), not evidence of experimental boundary measurements.

Citations as saved: [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6), [H7](#evidence-h7), [H8](#evidence-h8), [H9](#evidence-h9), [H10](#evidence-h10).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The strongly hydrophobic stretches support several membrane-spanning helices, including the N-terminal segment, but sequence hydropathy alone does not reliably settle exact boundaries such as 80..105 versus 81..101.


**Missing item-specific fact**

> The protein-specific transmembrane-region annotations and their precise coordinate boundaries.


**Reason**

> Selecting the exact listed intervals, rather than approximate hydrophobic helices, depends on protein-specific annotation or equivalent external evidence absent from the input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "D"
]
```

> As approximate sequence-based predictions, B and D both mark the same hydrophobic regions, with a differing boundary for the 81..101 helix. The supplied sequence does not establish a unique boundary convention; D is uniquely supported as the matching annotated answer.


### Important caveats

- The cited database annotations are computational and should not be described as experimental validation.
- The historical and current records match the supplied sequence, but the author's exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The strongly hydrophobic stretches support several membrane-spanning helices, including the N-terminal segment, but sequence hydropathy alone does not reliably settle exact boundaries such as 80..105 versus 81..101.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific transmembrane-region annotations and their precise coordinate boundaries.",
    "reason": "Selecting the exact listed intervals, rather than approximate hydrophobic helices, depends on protein-specific annotation or equivalent external evidence absent from the input."
  },
  "case_id": "transmembrane_0080",
  "expected_answer_check": {
    "evidence_ids": [
      "H3",
      "H4",
      "H5",
      "H6",
      "H7",
      "H8",
      "H9",
      "H10"
    ],
    "judgment": "supported",
    "reason": "The sequence matches the historical UniProt record, whose transmembrane annotations match choice D exactly. These annotations are computational (ECO:0000255), not evidence of experimental boundary measurements."
  },
  "important_caveats": [
    "The cited database annotations are computational and should not be described as experimental validation.",
    "The historical and current records match the supplied sequence, but the author's exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "D"
    ],
    "reason": "As approximate sequence-based predictions, B and D both mark the same hydrophobic regions, with a differing boundary for the 81..101 helix. The supplied sequence does not establish a unique boundary convention; D is uniquely supported as the matching annotated answer."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0080",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches the historical UniProt record, whose transmembrane annotations match choice D exactly. These annotations are computational (ECO:0000255), not evidence of experimental boundary measurements.",
    "evidence_ids": ["H3", "H4", "H5", "H6", "H7", "H8", "H9", "H10"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The strongly hydrophobic stretches support several membrane-spanning helices, including the N-terminal segment, but sequence hydropathy alone does not reliably settle exact boundaries such as 80..105 versus 81..101.",
    "missing_item_specific_fact": "The protein-specific transmembrane-region annotations and their precise coordinate boundaries.",
    "reason": "Selecting the exact listed intervals, rather than approximate hydrophobic helices, depends on protein-specific annotation or equivalent external evidence absent from the input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "D"],
    "reason": "As approximate sequence-based predictions, B and D both mark the same hydrophobic regions, with a differing boundary for the 81..101 helix. The supplied sequence does not establish a unique boundary convention; D is uniquely supported as the matching annotated answer."
  },
  "important_caveats": [
    "The cited database annotations are computational and should not be described as experimental validation.",
    "The historical and current records match the supplied sequence, but the author's exact source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt annotation (P9WEG7, evidence code ECO:0000255 'By similarity') lists exactly 8 transmembrane helical regions: 4..24, 81..101, 116..136, 158..178, 181..201, 228..248, 271..291, 309..329, matching Choice D precisely. The sequence is confirmed as 349 residues (matched SHA-256). The annotation is computational (by similarity) rather than experimental, but it is internally consistent and the hydrophobic character of the annotated regions is verifiable from the sequence itself.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [C9](#evidence-c9), [C10](#evidence-c10), [C11](#evidence-c11), [C12](#evidence-c12), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6), [H7](#evidence-h7), [H8](#evidence-h8), [H9](#evidence-h9), [H10](#evidence-h10).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Three reasoning steps distinguish D from the distractors: (1) Choice A includes positions 380..400 and 471..491, which exceed the 349-residue protein length — eliminable by arithmetic. (2) Choice C omits the N-terminal segment 4..24 (L-T-P-L-I-F-L-S-L-A-M-A-A-A-V-G-V-W-G-V-F), a classic signal-peptide hydrophobic core that is unmistakable by hydropathy. (3) Between B and D, the second segment differs: B proposes 80..105, D proposes 81..101. Position 80 is Arg (charged, incompatible with a TM helix interior), while position 81 is Phe (strongly hydrophobic, a natural helix start). Position 101 is Ala (hydrophobic, acceptable helix end), while position 102 is Arg (charged, a natural boundary). Position 105 is Pro (helix breaker, incompatible with a TM helix terminus). A model applying the principle that charged residues and prolines are excluded from TM helix cores can select 81..101 over 80..105.


**Missing item-specific fact**

> None critical. The boundary discrimination between B and D rests on general principles (charged residues exclude TM helix membership; proline breaks helices), which are identifiable from the sequence itself.


**Reason**

> The question provides sufficient sequence information for a model to apply standard TM-helix biophysical constraints (hydrophobicity, charge exclusion, proline incompatibility) to arrive at D without needing to memorize a specific database entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Choice A is eliminated by arithmetic (positions exceed protein length). Choice C is eliminated by the obvious N-terminal hydrophobic signal peptide. Choice B is eliminated because it includes Arg(80) and Pro(105) in the second TM helix, violating fundamental TM-helix biophysics. Only D is fully consistent with both the sequence and TM-helix constraints.


### Important caveats

- The UniProt annotation uses evidence code ECO:0000255 (By similarity), meaning the TM boundaries are computational predictions, not experimental measurements. Exact boundaries of TM helices are inherently approximate.
- The B-vs-D distinction (80..105 vs 81..101) is a 1-residue shift at the start and 4-residue shift at the end. While the Arg(80)/Pro(105) argument strongly favors D, a very different prediction tool could in principle produce slightly different boundaries.
- The reviewer-only UniProt accession and annotation were not available to the evaluated model; however, the reasoning above relies only on the sequence and general biology.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Three reasoning steps distinguish D from the distractors: (1) Choice A includes positions 380..400 and 471..491, which exceed the 349-residue protein length — eliminable by arithmetic. (2) Choice C omits the N-terminal segment 4..24 (L-T-P-L-I-F-L-S-L-A-M-A-A-A-V-G-V-W-G-V-F), a classic signal-peptide hydrophobic core that is unmistakable by hydropathy. (3) Between B and D, the second segment differs: B proposes 80..105, D proposes 81..101. Position 80 is Arg (charged, incompatible with a TM helix interior), while position 81 is Phe (strongly hydrophobic, a natural helix start). Position 101 is Ala (hydrophobic, acceptable helix end), while position 102 is Arg (charged, a natural boundary). Position 105 is Pro (helix breaker, incompatible with a TM helix terminus). A model applying the principle that charged residues and prolines are excluded from TM helix cores can select 81..101 over 80..105.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None critical. The boundary discrimination between B and D rests on general principles (charged residues exclude TM helix membership; proline breaks helices), which are identifiable from the sequence itself.",
    "reason": "The question provides sufficient sequence information for a model to apply standard TM-helix biophysical constraints (hydrophobicity, charge exclusion, proline incompatibility) to arrive at D without needing to memorize a specific database entry."
  },
  "case_id": "transmembrane_0080",
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
      "H3",
      "H4",
      "H5",
      "H6",
      "H7",
      "H8",
      "H9",
      "H10"
    ],
    "judgment": "supported",
    "reason": "The UniProt annotation (P9WEG7, evidence code ECO:0000255 'By similarity') lists exactly 8 transmembrane helical regions: 4..24, 81..101, 116..136, 158..178, 181..201, 228..248, 271..291, 309..329, matching Choice D precisely. The sequence is confirmed as 349 residues (matched SHA-256). The annotation is computational (by similarity) rather than experimental, but it is internally consistent and the hydrophobic character of the annotated regions is verifiable from the sequence itself."
  },
  "important_caveats": [
    "The UniProt annotation uses evidence code ECO:0000255 (By similarity), meaning the TM boundaries are computational predictions, not experimental measurements. Exact boundaries of TM helices are inherently approximate.",
    "The B-vs-D distinction (80..105 vs 81..101) is a 1-residue shift at the start and 4-residue shift at the end. While the Arg(80)/Pro(105) argument strongly favors D, a very different prediction tool could in principle produce slightly different boundaries.",
    "The reviewer-only UniProt accession and annotation were not available to the evaluated model; however, the reasoning above relies only on the sequence and general biology."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Choice A is eliminated by arithmetic (positions exceed protein length). Choice C is eliminated by the obvious N-terminal hydrophobic signal peptide. Choice B is eliminated because it includes Arg(80) and Pro(105) in the second TM helix, violating fundamental TM-helix biophysics. Only D is fully consistent with both the sequence and TM-helix constraints."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0080",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt annotation (P9WEG7, evidence code ECO:0000255 'By similarity') lists exactly 8 transmembrane helical regions: 4..24, 81..101, 116..136, 158..178, 181..201, 228..248, 271..291, 309..329, matching Choice D precisely. The sequence is confirmed as 349 residues (matched SHA-256). The annotation is computational (by similarity) rather than experimental, but it is internally consistent and the hydrophobic character of the annotated regions is verifiable from the sequence itself.",
    "evidence_ids": ["C5", "C6", "C7", "C8", "C9", "C10", "C11", "C12", "H3", "H4", "H5", "H6", "H7", "H8", "H9", "H10"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Three reasoning steps distinguish D from the distractors: (1) Choice A includes positions 380..400 and 471..491, which exceed the 349-residue protein length — eliminable by arithmetic. (2) Choice C omits the N-terminal segment 4..24 (L-T-P-L-I-F-L-S-L-A-M-A-A-A-V-G-V-W-G-V-F), a classic signal-peptide hydrophobic core that is unmistakable by hydropathy. (3) Between B and D, the second segment differs: B proposes 80..105, D proposes 81..101. Position 80 is Arg (charged, incompatible with a TM helix interior), while position 81 is Phe (strongly hydrophobic, a natural helix start). Position 101 is Ala (hydrophobic, acceptable helix end), while position 102 is Arg (charged, a natural boundary). Position 105 is Pro (helix breaker, incompatible with a TM helix terminus). A model applying the principle that charged residues and prolines are excluded from TM helix cores can select 81..101 over 80..105.",
    "missing_item_specific_fact": "None critical. The boundary discrimination between B and D rests on general principles (charged residues exclude TM helix membership; proline breaks helices), which are identifiable from the sequence itself.",
    "reason": "The question provides sufficient sequence information for a model to apply standard TM-helix biophysical constraints (hydrophobicity, charge exclusion, proline incompatibility) to arrive at D without needing to memorize a specific database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Choice A is eliminated by arithmetic (positions exceed protein length). Choice C is eliminated by the obvious N-terminal hydrophobic signal peptide. Choice B is eliminated because it includes Arg(80) and Pro(105) in the second TM helix, violating fundamental TM-helix biophysics. Only D is fully consistent with both the sequence and TM-helix constraints."
  },
  "important_caveats": [
    "The UniProt annotation uses evidence code ECO:0000255 (By similarity), meaning the TM boundaries are computational predictions, not experimental measurements. Exact boundaries of TM helices are inherently approximate.",
    "The B-vs-D distinction (80..105 vs 81..101) is a 1-residue shift at the start and 4-residue shift at the end. While the Arg(80)/Pro(105) argument strongly favors D, a very different prediction tool could in principle produce slightly different boundaries.",
    "The reviewer-only UniProt accession and annotation were not available to the evaluated model; however, the reasoning above relies only on the sequence and general biology."
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

**Accession:** `P9WEG7` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 2. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P9WEG7.json)  
**Locator:** `/features/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:17.512806+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":24},"start":{"modifier":"EXACT","value":4}},"type":"Transmembrane"}
```

Source SHA-256: `cc0cb3cc56cbc60432581eb408108dc2d2be5bfdc4ea3d2699b2708dcea8ab8b`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P9WEG7.json)  
**Locator:** `/features/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:17.512806+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":101},"start":{"modifier":"EXACT","value":81}},"type":"Transmembrane"}
```

Source SHA-256: `cc0cb3cc56cbc60432581eb408108dc2d2be5bfdc4ea3d2699b2708dcea8ab8b`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P9WEG7.json)  
**Locator:** `/features/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:17.512806+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":136},"start":{"modifier":"EXACT","value":116}},"type":"Transmembrane"}
```

Source SHA-256: `cc0cb3cc56cbc60432581eb408108dc2d2be5bfdc4ea3d2699b2708dcea8ab8b`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P9WEG7.json)  
**Locator:** `/features/4`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:17.512806+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":178},"start":{"modifier":"EXACT","value":158}},"type":"Transmembrane"}
```

Source SHA-256: `cc0cb3cc56cbc60432581eb408108dc2d2be5bfdc4ea3d2699b2708dcea8ab8b`.

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P9WEG7.json)  
**Locator:** `/features/5`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:17.512806+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":201},"start":{"modifier":"EXACT","value":181}},"type":"Transmembrane"}
```

Source SHA-256: `cc0cb3cc56cbc60432581eb408108dc2d2be5bfdc4ea3d2699b2708dcea8ab8b`.

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P9WEG7.json)  
**Locator:** `/features/6`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:17.512806+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":248},"start":{"modifier":"EXACT","value":228}},"type":"Transmembrane"}
```

Source SHA-256: `cc0cb3cc56cbc60432581eb408108dc2d2be5bfdc4ea3d2699b2708dcea8ab8b`.

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P9WEG7.json)  
**Locator:** `/features/7`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:17.512806+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":291},"start":{"modifier":"EXACT","value":271}},"type":"Transmembrane"}
```

Source SHA-256: `cc0cb3cc56cbc60432581eb408108dc2d2be5bfdc4ea3d2699b2708dcea8ab8b`.

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P9WEG7.json)  
**Locator:** `/features/8`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:17.512806+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":329},"start":{"modifier":"EXACT","value":309}},"type":"Transmembrane"}
```

Source SHA-256: `cc0cb3cc56cbc60432581eb408108dc2d2be5bfdc4ea3d2699b2708dcea8ab8b`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P9WEG7?format=txt&versions=2)  
**Locator:** `lines 66-68`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 2 / 1.  
**Retrieved:** 2026-11-02T04:30:21.947384+00:00.  

```text
FT   TRANSMEM        4..24
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `20bc0e67398f5d9ca5428fba937ca2d4cf4546b725019108174063d3acb20d32`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P9WEG7?format=txt&versions=2)  
**Locator:** `lines 69-71`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 2 / 1.  
**Retrieved:** 2026-11-02T04:30:21.947384+00:00.  

```text
FT   TRANSMEM        81..101
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `20bc0e67398f5d9ca5428fba937ca2d4cf4546b725019108174063d3acb20d32`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P9WEG7?format=txt&versions=2)  
**Locator:** `lines 72-74`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 2 / 1.  
**Retrieved:** 2026-11-02T04:30:21.947384+00:00.  

```text
FT   TRANSMEM        116..136
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `20bc0e67398f5d9ca5428fba937ca2d4cf4546b725019108174063d3acb20d32`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P9WEG7?format=txt&versions=2)  
**Locator:** `lines 75-77`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 2 / 1.  
**Retrieved:** 2026-11-02T04:30:21.947384+00:00.  

```text
FT   TRANSMEM        158..178
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `20bc0e67398f5d9ca5428fba937ca2d4cf4546b725019108174063d3acb20d32`.

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P9WEG7?format=txt&versions=2)  
**Locator:** `lines 78-80`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 2 / 1.  
**Retrieved:** 2026-11-02T04:30:21.947384+00:00.  

```text
FT   TRANSMEM        181..201
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `20bc0e67398f5d9ca5428fba937ca2d4cf4546b725019108174063d3acb20d32`.

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P9WEG7?format=txt&versions=2)  
**Locator:** `lines 81-83`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 2 / 1.  
**Retrieved:** 2026-11-02T04:30:21.947384+00:00.  

```text
FT   TRANSMEM        228..248
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `20bc0e67398f5d9ca5428fba937ca2d4cf4546b725019108174063d3acb20d32`.

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P9WEG7?format=txt&versions=2)  
**Locator:** `lines 84-86`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 2 / 1.  
**Retrieved:** 2026-11-02T04:30:21.947384+00:00.  

```text
FT   TRANSMEM        271..291
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `20bc0e67398f5d9ca5428fba937ca2d4cf4546b725019108174063d3acb20d32`.

### Evidence H10

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P9WEG7?format=txt&versions=2)  
**Locator:** `lines 87-89`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 2 / 1.  
**Retrieved:** 2026-11-02T04:30:21.947384+00:00.  

```text
FT   TRANSMEM        309..329
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `20bc0e67398f5d9ca5428fba937ca2d4cf4546b725019108174063d3acb20d32`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json), zero-based source row 80. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
