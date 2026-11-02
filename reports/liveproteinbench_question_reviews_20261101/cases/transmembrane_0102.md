# transmembrane_0102

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `transmembrane`  
**Author expected answer:** **D** — 27..47; 59..81; 96..116; 138..158; 204..224; 246..266; 270..290

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MVNFTHVSEFVLLGFQGGPGMQAMLFLIFLILYGIAVVGNLGMIVIIWVDAHLHTPMYAFLQSLSLLDICYSSTIAPRALANSMQEDHTISFGGCAAQFFFLSLFGITEAFLLAAMAYDRFIAICNPLLYSVSMSHQVCVLLISGSYLWGVVNAIAQTTMTFRLPFCGSNEINDFFCDVPPLLSLSCSDTFINQLVLLGLCGSIIVSTFLIVLVSYIYIISTILRIPTMQGCQKAFSTCASHLTGVCLFFGTVFFMYAQPSAIFFMEQSKIVSIFYTMVIPMLNPLIYSLRNKEVKQALRRSMQKLSL

[Multiple Choices]
A. 27..47; 96..116; 138..158; 204..224; 246..266; 270..290
B. 27..47; 59..81; 96..116; 138..158; 204..224; 246..266; 275..292
C. 35..55
D. 27..47; 59..81; 96..116; 138..158; 204..224; 246..266; 270..290
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

> The supplied sequence exactly matches the historical and current UniProt sequence. Both annotations assign seven transmembrane helices at the coordinates in D. The entries label these features with ECO:0000255, indicating computational evidence, not direct experimental validation.

Citations as saved: [H3](#evidence-h3), [H5](#evidence-h5), [H7](#evidence-h7), [H9](#evidence-h9), [H11](#evidence-h11), [H13](#evidence-h13), [H15](#evidence-h15), [C6](#evidence-c6), [C8](#evidence-c8), [C10](#evidence-c10), [C12](#evidence-c12), [C14](#evidence-c14), [C16](#evidence-c16), [C18](#evidence-c18).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence has multiple long hydrophobic stretches, consistent with a multi-pass membrane protein and plausibly seven membrane-spanning helices. That general pattern does not establish the exact start and end coordinates needed to distinguish the options.


**Missing item-specific fact**

> The protein-specific assignment of helix boundaries, especially the final span's 270..290 coordinates rather than the alternative 275..292, is absent from the input and requires a specific annotation or prediction.


**Reason**

> Hydropathy and general knowledge support identifying likely membrane-spanning regions, but the precise boundaries in the choices depend on protein-specific segmentation. The reviewer-only UniProt evidence supports D but was not supplied to the evaluated model.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "D"
]
```

> At the level of approximate membrane-spanning regions, B and D both include the seven hydrophobic spans; their final-region boundaries differ. The available sequence alone does not definitively settle those exact boundaries, although the cited computational annotation specifies D.


### Important caveats

- The matching UniProt annotations are computationally supported; they should not be described as experimental measurements.
- The actual author source snapshot is unknown, although a matching historical annotation is available.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has multiple long hydrophobic stretches, consistent with a multi-pass membrane protein and plausibly seven membrane-spanning helices. That general pattern does not establish the exact start and end coordinates needed to distinguish the options.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific assignment of helix boundaries, especially the final span's 270..290 coordinates rather than the alternative 275..292, is absent from the input and requires a specific annotation or prediction.",
    "reason": "Hydropathy and general knowledge support identifying likely membrane-spanning regions, but the precise boundaries in the choices depend on protein-specific segmentation. The reviewer-only UniProt evidence supports D but was not supplied to the evaluated model."
  },
  "case_id": "transmembrane_0102",
  "expected_answer_check": {
    "evidence_ids": [
      "H3",
      "H5",
      "H7",
      "H9",
      "H11",
      "H13",
      "H15",
      "C6",
      "C8",
      "C10",
      "C12",
      "C14",
      "C16",
      "C18"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the historical and current UniProt sequence. Both annotations assign seven transmembrane helices at the coordinates in D. The entries label these features with ECO:0000255, indicating computational evidence, not direct experimental validation."
  },
  "important_caveats": [
    "The matching UniProt annotations are computationally supported; they should not be described as experimental measurements.",
    "The actual author source snapshot is unknown, although a matching historical annotation is available."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "D"
    ],
    "reason": "At the level of approximate membrane-spanning regions, B and D both include the seven hydrophobic spans; their final-region boundaries differ. The available sequence alone does not definitively settle those exact boundaries, although the cited computational annotation specifies D."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0102",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the historical and current UniProt sequence. Both annotations assign seven transmembrane helices at the coordinates in D. The entries label these features with ECO:0000255, indicating computational evidence, not direct experimental validation.",
    "evidence_ids": ["H3", "H5", "H7", "H9", "H11", "H13", "H15", "C6", "C8", "C10", "C12", "C14", "C16", "C18"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence has multiple long hydrophobic stretches, consistent with a multi-pass membrane protein and plausibly seven membrane-spanning helices. That general pattern does not establish the exact start and end coordinates needed to distinguish the options.",
    "missing_item_specific_fact": "The protein-specific assignment of helix boundaries, especially the final span's 270..290 coordinates rather than the alternative 275..292, is absent from the input and requires a specific annotation or prediction.",
    "reason": "Hydropathy and general knowledge support identifying likely membrane-spanning regions, but the precise boundaries in the choices depend on protein-specific segmentation. The reviewer-only UniProt evidence supports D but was not supplied to the evaluated model."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "D"],
    "reason": "At the level of approximate membrane-spanning regions, B and D both include the seven hydrophobic spans; their final-region boundaries differ. The available sequence alone does not definitively settle those exact boundaries, although the cited computational annotation specifies D."
  },
  "important_caveats": [
    "The matching UniProt annotations are computationally supported; they should not be described as experimental measurements.",
    "The actual author source snapshot is unknown, although a matching historical annotation is available."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry Q6UXT6 (OR9H1_HUMAN) annotates exactly seven transmembrane helices at 27..47, 59..81, 96..116, 138..158, 204..224, 246..266, and 270..290, matching choice D precisely. All annotations carry evidence code ECO:0000255 (inferred by similarity, i.e., computational/prorule-based prediction rather than direct experimental determination), but they are the canonical Swiss-Prot annotation and are consistent across the historical (v106) and current (v108) snapshots with identical sequence match.

Citations as saved: [C6](#evidence-c6), [C8](#evidence-c8), [C10](#evidence-c10), [C12](#evidence-c12), [C14](#evidence-c14), [C16](#evidence-c16), [C18](#evidence-c18), [H3](#evidence-h3), [H5](#evidence-h5), [H7](#evidence-h7), [H9](#evidence-h9), [H11](#evidence-h11), [H13](#evidence-h13), [H15](#evidence-h15).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Olfactory receptors are well-established 7-transmembrane GPCRs, which immediately disfavors option A (only 6 TMs, missing the TM2 region at 59..81) and option C (single TM). The region 59-81 (AFLQSLSLLDICYSSTIAPRALA) contains a hydrophobic core flanked by short polar segments, consistent with a TM helix in a GPCR bundle. For TM7, the sequence at 270-274 (IFFME) is substantially more hydrophobic than 275-279 (QSKIV), making a helix start at 270 rather than 275 the hydrophobically preferred choice; similarly, positions 291-292 (NP) are not strongly hydrophobic, favoring an end at 290 over 292. Thus, general GPCR topology knowledge combined with hydrophobicity-window reasoning can distinguish D from A and B.


**Missing item-specific fact**

> None strictly required. The exact 5-residue boundary shift of TM7 (270 vs 275 start) is a fine-grained call that a hydrophobicity predictor would resolve more confidently, but the IFFM vs QSK contrast is visible by inspection.


**Reason**

> The 7-TM GPCR topology is textbook knowledge for olfactory receptors, and the hydrophobic character of the candidate TM segments (especially the presence of TM2 and the hydrophobicity contrast at the TM7 N-terminus) provides concrete sequence-based grounds to select D over A and B without needing to memorize the specific UniProt entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Option C (single TM) is trivially wrong for a 7-TM GPCR. Option A omits TM2, which is identifiable as a hydrophobic helix in the 7-TM context. Option B shifts TM7 boundaries into a polar/charged region (QSK at 275-277) and past the hydrophobic core, making it less defensible. D is the only option consistent with both 7-TM topology and hydrophobicity.


### Important caveats

- All TM annotations are ECO:0000255 (inferred by similarity / ProRule), not experimentally determined. The exact boundaries are computational predictions and could differ by a few residues under alternative predictors.
- The sequence provided (307 characters by manual count) may differ by one residue from the 308-AA UniProt entry; the reviewer confirms sequence match (SHA-256 identical), so this is likely a counting artifact in the prompt.
- The distinction between B and D (TM7: 275..292 vs 270..290) is a ~5-residue boundary call that, while hydrophobically rationalizable, is at the precision limit of manual sequence inspection.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Olfactory receptors are well-established 7-transmembrane GPCRs, which immediately disfavors option A (only 6 TMs, missing the TM2 region at 59..81) and option C (single TM). The region 59-81 (AFLQSLSLLDICYSSTIAPRALA) contains a hydrophobic core flanked by short polar segments, consistent with a TM helix in a GPCR bundle. For TM7, the sequence at 270-274 (IFFME) is substantially more hydrophobic than 275-279 (QSKIV), making a helix start at 270 rather than 275 the hydrophobically preferred choice; similarly, positions 291-292 (NP) are not strongly hydrophobic, favoring an end at 290 over 292. Thus, general GPCR topology knowledge combined with hydrophobicity-window reasoning can distinguish D from A and B.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None strictly required. The exact 5-residue boundary shift of TM7 (270 vs 275 start) is a fine-grained call that a hydrophobicity predictor would resolve more confidently, but the IFFM vs QSK contrast is visible by inspection.",
    "reason": "The 7-TM GPCR topology is textbook knowledge for olfactory receptors, and the hydrophobic character of the candidate TM segments (especially the presence of TM2 and the hydrophobicity contrast at the TM7 N-terminus) provides concrete sequence-based grounds to select D over A and B without needing to memorize the specific UniProt entry."
  },
  "case_id": "transmembrane_0102",
  "expected_answer_check": {
    "evidence_ids": [
      "C6",
      "C8",
      "C10",
      "C12",
      "C14",
      "C16",
      "C18",
      "H3",
      "H5",
      "H7",
      "H9",
      "H11",
      "H13",
      "H15"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry Q6UXT6 (OR9H1_HUMAN) annotates exactly seven transmembrane helices at 27..47, 59..81, 96..116, 138..158, 204..224, 246..266, and 270..290, matching choice D precisely. All annotations carry evidence code ECO:0000255 (inferred by similarity, i.e., computational/prorule-based prediction rather than direct experimental determination), but they are the canonical Swiss-Prot annotation and are consistent across the historical (v106) and current (v108) snapshots with identical sequence match."
  },
  "important_caveats": [
    "All TM annotations are ECO:0000255 (inferred by similarity / ProRule), not experimentally determined. The exact boundaries are computational predictions and could differ by a few residues under alternative predictors.",
    "The sequence provided (307 characters by manual count) may differ by one residue from the 308-AA UniProt entry; the reviewer confirms sequence match (SHA-256 identical), so this is likely a counting artifact in the prompt.",
    "The distinction between B and D (TM7: 275..292 vs 270..290) is a ~5-residue boundary call that, while hydrophobically rationalizable, is at the precision limit of manual sequence inspection."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Option C (single TM) is trivially wrong for a 7-TM GPCR. Option A omits TM2, which is identifiable as a hydrophobic helix in the 7-TM context. Option B shifts TM7 boundaries into a polar/charged region (QSK at 275-277) and past the hydrophobic core, making it less defensible. D is the only option consistent with both 7-TM topology and hydrophobicity."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0102",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry Q6UXT6 (OR9H1_HUMAN) annotates exactly seven transmembrane helices at 27..47, 59..81, 96..116, 138..158, 204..224, 246..266, and 270..290, matching choice D precisely. All annotations carry evidence code ECO:0000255 (inferred by similarity, i.e., computational/prorule-based prediction rather than direct experimental determination), but they are the canonical Swiss-Prot annotation and are consistent across the historical (v106) and current (v108) snapshots with identical sequence match.",
    "evidence_ids": ["C6","C8","C10","C12","C14","C16","C18","H3","H5","H7","H9","H11","H13","H15"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Olfactory receptors are well-established 7-transmembrane GPCRs, which immediately disfavors option A (only 6 TMs, missing the TM2 region at 59..81) and option C (single TM). The region 59-81 (AFLQSLSLLDICYSSTIAPRALA) contains a hydrophobic core flanked by short polar segments, consistent with a TM helix in a GPCR bundle. For TM7, the sequence at 270-274 (IFFME) is substantially more hydrophobic than 275-279 (QSKIV), making a helix start at 270 rather than 275 the hydrophobically preferred choice; similarly, positions 291-292 (NP) are not strongly hydrophobic, favoring an end at 290 over 292. Thus, general GPCR topology knowledge combined with hydrophobicity-window reasoning can distinguish D from A and B.",
    "missing_item_specific_fact": "None strictly required. The exact 5-residue boundary shift of TM7 (270 vs 275 start) is a fine-grained call that a hydrophobicity predictor would resolve more confidently, but the IFFM vs QSK contrast is visible by inspection.",
    "reason": "The 7-TM GPCR topology is textbook knowledge for olfactory receptors, and the hydrophobic character of the candidate TM segments (especially the presence of TM2 and the hydrophobicity contrast at the TM7 N-terminus) provides concrete sequence-based grounds to select D over A and B without needing to memorize the specific UniProt entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Option C (single TM) is trivially wrong for a 7-TM GPCR. Option A omits TM2, which is identifiable as a hydrophobic helix in the 7-TM context. Option B shifts TM7 boundaries into a polar/charged region (QSK at 275-277) and past the hydrophobic core, making it less defensible. D is the only option consistent with both 7-TM topology and hydrophobicity."
  },
  "important_caveats": [
    "All TM annotations are ECO:0000255 (inferred by similarity / ProRule), not experimentally determined. The exact boundaries are computational predictions and could differ by a few residues under alternative predictors.",
    "The sequence provided (307 characters by manual count) may differ by one residue from the 308-AA UniProt entry; the reviewer confirms sequence match (SHA-256 identical), so this is likely a counting artifact in the prompt.",
    "The distinction between B and D (TM7: 275..292 vs 270..290) is a ~5-residue boundary call that, while hydrophobically rationalizable, is at the precision limit of manual sequence inspection."
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

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6UXT6.json)  
**Locator:** `/features/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:45.136978+00:00.  

```json
{"description":"Helical; Name=1","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":47},"start":{"modifier":"EXACT","value":27}},"type":"Transmembrane"}
```

Source SHA-256: `d761824ae03c221d019ed712f82a29f42f3f5f479f6233c26b23ed7827f111d1`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6UXT6.json)  
**Locator:** `/features/4`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:45.136978+00:00.  

```json
{"description":"Helical; Name=2","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":81},"start":{"modifier":"EXACT","value":59}},"type":"Transmembrane"}
```

Source SHA-256: `d761824ae03c221d019ed712f82a29f42f3f5f479f6233c26b23ed7827f111d1`.

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6UXT6.json)  
**Locator:** `/features/6`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:45.136978+00:00.  

```json
{"description":"Helical; Name=3","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":116},"start":{"modifier":"EXACT","value":96}},"type":"Transmembrane"}
```

Source SHA-256: `d761824ae03c221d019ed712f82a29f42f3f5f479f6233c26b23ed7827f111d1`.

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6UXT6.json)  
**Locator:** `/features/8`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:45.136978+00:00.  

```json
{"description":"Helical; Name=4","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":158},"start":{"modifier":"EXACT","value":138}},"type":"Transmembrane"}
```

Source SHA-256: `d761824ae03c221d019ed712f82a29f42f3f5f479f6233c26b23ed7827f111d1`.

### Evidence C14

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6UXT6.json)  
**Locator:** `/features/10`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:45.136978+00:00.  

```json
{"description":"Helical; Name=5","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":224},"start":{"modifier":"EXACT","value":204}},"type":"Transmembrane"}
```

Source SHA-256: `d761824ae03c221d019ed712f82a29f42f3f5f479f6233c26b23ed7827f111d1`.

### Evidence C16

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6UXT6.json)  
**Locator:** `/features/12`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:45.136978+00:00.  

```json
{"description":"Helical; Name=6","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":266},"start":{"modifier":"EXACT","value":246}},"type":"Transmembrane"}
```

Source SHA-256: `d761824ae03c221d019ed712f82a29f42f3f5f479f6233c26b23ed7827f111d1`.

### Evidence C18

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6UXT6.json)  
**Locator:** `/features/14`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:45.136978+00:00.  

```json
{"description":"Helical; Name=7","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":290},"start":{"modifier":"EXACT","value":270}},"type":"Transmembrane"}
```

Source SHA-256: `d761824ae03c221d019ed712f82a29f42f3f5f479f6233c26b23ed7827f111d1`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q6UXT6?format=txt&versions=106)  
**Locator:** `lines 121-123`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 106 / 1.  
**Retrieved:** 2026-11-02T04:31:47.614110+00:00.  

```text
FT   TRANSMEM        27..47
FT                   /note="Helical; Name=1"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `072cef681e411cc08becb56d888ebce42ad8a93eca1ca016afab23f858b5896a`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q6UXT6?format=txt&versions=106)  
**Locator:** `lines 127-129`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 106 / 1.  
**Retrieved:** 2026-11-02T04:31:47.614110+00:00.  

```text
FT   TRANSMEM        59..81
FT                   /note="Helical; Name=2"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `072cef681e411cc08becb56d888ebce42ad8a93eca1ca016afab23f858b5896a`.

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q6UXT6?format=txt&versions=106)  
**Locator:** `lines 133-135`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 106 / 1.  
**Retrieved:** 2026-11-02T04:31:47.614110+00:00.  

```text
FT   TRANSMEM        96..116
FT                   /note="Helical; Name=3"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `072cef681e411cc08becb56d888ebce42ad8a93eca1ca016afab23f858b5896a`.

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q6UXT6?format=txt&versions=106)  
**Locator:** `lines 139-141`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 106 / 1.  
**Retrieved:** 2026-11-02T04:31:47.614110+00:00.  

```text
FT   TRANSMEM        138..158
FT                   /note="Helical; Name=4"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `072cef681e411cc08becb56d888ebce42ad8a93eca1ca016afab23f858b5896a`.

### Evidence H11

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q6UXT6?format=txt&versions=106)  
**Locator:** `lines 145-147`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 106 / 1.  
**Retrieved:** 2026-11-02T04:31:47.614110+00:00.  

```text
FT   TRANSMEM        204..224
FT                   /note="Helical; Name=5"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `072cef681e411cc08becb56d888ebce42ad8a93eca1ca016afab23f858b5896a`.

### Evidence H13

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q6UXT6?format=txt&versions=106)  
**Locator:** `lines 151-153`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 106 / 1.  
**Retrieved:** 2026-11-02T04:31:47.614110+00:00.  

```text
FT   TRANSMEM        246..266
FT                   /note="Helical; Name=6"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `072cef681e411cc08becb56d888ebce42ad8a93eca1ca016afab23f858b5896a`.

### Evidence H15

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q6UXT6?format=txt&versions=106)  
**Locator:** `lines 157-159`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 106 / 1.  
**Retrieved:** 2026-11-02T04:31:47.614110+00:00.  

```text
FT   TRANSMEM        270..290
FT                   /note="Helical; Name=7"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `072cef681e411cc08becb56d888ebce42ad8a93eca1ca016afab23f858b5896a`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json), zero-based source row 102. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
