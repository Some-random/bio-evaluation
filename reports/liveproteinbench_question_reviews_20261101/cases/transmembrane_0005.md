# transmembrane_0005

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `transmembrane`  
**Author expected answer:** **C** — 9..29; 41..61; 84..104; 118..138; 153..173; 175..195; 202..222; 231..251

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MKNNKISGFQWAMTIFVFFVITMALSIMLRDFQSIIGVKHFIFEVTDLAPLIAAIICILVFKYKKVQLAGLKFSISLKVIERLLLALILPLIILIIGMYSFNTFADSFILLQSTGLSVPITHILIGHILMAFVVEFGFRSYLQNIVETKMNTFFASIVVGLMYSVFSANTTYGTEFAAYNFLYTFSFSMILGELIRATKGRTIYIATTFHASMTFGLIFLFSEEIGDLFSIKVIAISTAIVAVGYIGLSLIIRGIAYLTTRRNLEELEPNNYLDHVNDDEETNHTEAEKSSSNIKDAEKTGVATASTVGVAKNDTENTVADEPSIHEGTEKTEPQHHIGNQTESNHDEDHDITSESVESAESVKQAPQSDDLTNDSNEDEIEQSLKEPVTYKEDRRSSVVIDAEKHIEKTEEQSSDKNK

[Multiple Choices]
A. 9..29; 42..61; 84..104; 118..138; 153..173; 175..195; 202..222; 231..251
B. 9..29; 41..61; 84..104; 118..138; 153..173; 175..195; 202..222
C. 9..29; 41..61; 84..104; 118..138; 153..173; 175..195; 202..222; 231..251
D. 3..23
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

> The sequence matches the cited UniProt record, whose transmembrane annotations give the eight intervals in choice C. These are computational annotations (ECO:0000255), not evidence of experimental measurement.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [C9](#evidence-c9), [C10](#evidence-c10), [C11](#evidence-c11), [C12](#evidence-c12), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6), [H7](#evidence-h7), [H8](#evidence-h8), [H9](#evidence-h9), [H10](#evidence-h10), [H11](#evidence-h11).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence contains multiple long hydrophobic stretches consistent with membrane-spanning helices, including a hydrophobic region corresponding broadly to the final candidate span; this supports a multi-pass topology and weighs against D or omitting that span as in B.


**Missing item-specific fact**

> The exact annotated helix boundaries, particularly whether the second interval begins at residue 41 or 42, are protein-specific details not reliably determined from the supplied sequence alone.


**Reason**

> Sequence composition supports the broad topology, but choosing the exact listed coordinates requires an item-specific boundary annotation or equivalent evidence.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "C"
]
```

> A and C differ by only one residue at the start of the second span, while both include the evident final hydrophobic span. The sequence alone does not sharply distinguish those boundary choices.


### Important caveats

- The supporting UniProt transmembrane features are computationally annotated; they should not be described as experimentally established.
- The reviewer-only sequence-matched database evidence was not supplied to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains multiple long hydrophobic stretches consistent with membrane-spanning helices, including a hydrophobic region corresponding broadly to the final candidate span; this supports a multi-pass topology and weighs against D or omitting that span as in B.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The exact annotated helix boundaries, particularly whether the second interval begins at residue 41 or 42, are protein-specific details not reliably determined from the supplied sequence alone.",
    "reason": "Sequence composition supports the broad topology, but choosing the exact listed coordinates requires an item-specific boundary annotation or equivalent evidence."
  },
  "case_id": "transmembrane_0005",
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
      "H4",
      "H5",
      "H6",
      "H7",
      "H8",
      "H9",
      "H10",
      "H11"
    ],
    "judgment": "supported",
    "reason": "The sequence matches the cited UniProt record, whose transmembrane annotations give the eight intervals in choice C. These are computational annotations (ECO:0000255), not evidence of experimental measurement."
  },
  "important_caveats": [
    "The supporting UniProt transmembrane features are computationally annotated; they should not be described as experimentally established.",
    "The reviewer-only sequence-matched database evidence was not supplied to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "C"
    ],
    "reason": "A and C differ by only one residue at the start of the second span, while both include the evident final hydrophobic span. The sequence alone does not sharply distinguish those boundary choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0005",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches the cited UniProt record, whose transmembrane annotations give the eight intervals in choice C. These are computational annotations (ECO:0000255), not evidence of experimental measurement.",
    "evidence_ids": ["C5", "C6", "C7", "C8", "C9", "C10", "C11", "C12", "H4", "H5", "H6", "H7", "H8", "H9", "H10", "H11"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence contains multiple long hydrophobic stretches consistent with membrane-spanning helices, including a hydrophobic region corresponding broadly to the final candidate span; this supports a multi-pass topology and weighs against D or omitting that span as in B.",
    "missing_item_specific_fact": "The exact annotated helix boundaries, particularly whether the second interval begins at residue 41 or 42, are protein-specific details not reliably determined from the supplied sequence alone.",
    "reason": "Sequence composition supports the broad topology, but choosing the exact listed coordinates requires an item-specific boundary annotation or equivalent evidence."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "C"],
    "reason": "A and C differ by only one residue at the start of the second span, while both include the evident final hydrophobic span. The sequence alone does not sharply distinguish those boundary choices."
  },
  "important_caveats": [
    "The supporting UniProt transmembrane features are computationally annotated; they should not be described as experimentally established.",
    "The reviewer-only sequence-matched database evidence was not supplied to the evaluated model."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A0A0H3KA40 (LyrA/SpdC from S. aureus Newman) annotates exactly eight transmembrane helical regions: 9-29, 41-61, 84-104, 118-138, 153-173, 175-195, 202-222, and 231-251. Choice C matches all eight regions with identical boundaries. The sequence in the question matches the canonical entry (419 AA, SHA-256 confirmed). Note that all eight annotations carry evidence code ECO:0000255 (inferred by similarity), meaning these are computational predictions transferred from a homolog, not experimental measurements.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [C9](#evidence-c9), [C10](#evidence-c10), [C11](#evidence-c11), [C12](#evidence-c12), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6), [H7](#evidence-h7), [H8](#evidence-h8), [H9](#evidence-h9), [H10](#evidence-h10), [H11](#evidence-h11).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> Choice D (3..23) can be eliminated by recognizing the protein as a multi-pass membrane protein with multiple hydrophobic stretches. A weak biological argument favors C over A: position 41 is Phe (strongly hydrophobic) immediately following charged residues K39 and H40, so the hydrophobic TM core naturally begins at F41 rather than I42. However, this single-residue boundary shift is within the noise of any hydrophobicity-window predictor. The B vs C distinction (7 vs 8 TMs) requires assessing whether residues 231-251 (IKVIAISTAIVAVGYIGLSLIIR) constitute a TM; this region is mixed (contains K, S, T, R) and borderline, making the call dependent on the specific prediction tool's thresholds.


**Missing item-specific fact**

> The exact boundary of TM2 (residue 41 vs 42) and the inclusion/exclusion of TM8 (231-251) depend on the specific computational prediction algorithm and its window size, scoring matrix, and thresholds used to generate the ECO:0000255 annotations. No general biological principle definitively resolves the single-residue shift or the borderline hydrophobicity of the 231-251 segment.


**Reason**

> While D is clearly eliminable and the multi-pass topology is evident from the sequence, the definitive distinctions between A and C (one-residue TM2 boundary shift) and between B and C (inclusion of the borderline 8th TM) cannot be resolved by general biological reasoning. These boundaries are artifacts of the specific prediction tool used for the UniProt annotation (ECO:0000255, inferred by similarity). Selecting C over A and B requires knowing the exact output of that particular predictor, i.e., memorizing the database entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "C"
]
```

> The only difference between A and C is whether TM2 starts at residue 41 (Phe) or 42 (Ile). Both residues are hydrophobic, and the preceding residues are K39 (charged) and H40 (charged/polar). A hydrophobicity-window analysis could reasonably place the boundary at either position depending on window size and threshold. Without the specific prediction algorithm's parameters, both A and C are defensible from a sequence-analysis standpoint.


### Important caveats

- All eight TM annotations carry evidence code ECO:0000255 (inferred by similarity), indicating computational predictions transferred from a homologous protein, not experimental measurements (e.g., cryo-EM, crystallography, or cross-linking).
- The UniProt entry was first publicly released on 2025-06-18; the historical snapshot checked (entry version 36, released 2026-01-28) already contains these annotations. The author's exact source snapshot is unknown.
- The reviewer-only evidence confirms sequence match (SHA-256 identical between benchmark input and UniProt canonical sequence), so the annotation is applicable to the supplied sequence.
- The question asks to identify 'a segment that crosses the membrane' (singular) but the choices present complete multi-TM topologies. This wording is slightly misleading but does not change the intended task.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Choice D (3..23) can be eliminated by recognizing the protein as a multi-pass membrane protein with multiple hydrophobic stretches. A weak biological argument favors C over A: position 41 is Phe (strongly hydrophobic) immediately following charged residues K39 and H40, so the hydrophobic TM core naturally begins at F41 rather than I42. However, this single-residue boundary shift is within the noise of any hydrophobicity-window predictor. The B vs C distinction (7 vs 8 TMs) requires assessing whether residues 231-251 (IKVIAISTAIVAVGYIGLSLIIR) constitute a TM; this region is mixed (contains K, S, T, R) and borderline, making the call dependent on the specific prediction tool's thresholds.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The exact boundary of TM2 (residue 41 vs 42) and the inclusion/exclusion of TM8 (231-251) depend on the specific computational prediction algorithm and its window size, scoring matrix, and thresholds used to generate the ECO:0000255 annotations. No general biological principle definitively resolves the single-residue shift or the borderline hydrophobicity of the 231-251 segment.",
    "reason": "While D is clearly eliminable and the multi-pass topology is evident from the sequence, the definitive distinctions between A and C (one-residue TM2 boundary shift) and between B and C (inclusion of the borderline 8th TM) cannot be resolved by general biological reasoning. These boundaries are artifacts of the specific prediction tool used for the UniProt annotation (ECO:0000255, inferred by similarity). Selecting C over A and B requires knowing the exact output of that particular predictor, i.e., memorizing the database entry."
  },
  "case_id": "transmembrane_0005",
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
      "H4",
      "H5",
      "H6",
      "H7",
      "H8",
      "H9",
      "H10",
      "H11"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry A0A0H3KA40 (LyrA/SpdC from S. aureus Newman) annotates exactly eight transmembrane helical regions: 9-29, 41-61, 84-104, 118-138, 153-173, 175-195, 202-222, and 231-251. Choice C matches all eight regions with identical boundaries. The sequence in the question matches the canonical entry (419 AA, SHA-256 confirmed). Note that all eight annotations carry evidence code ECO:0000255 (inferred by similarity), meaning these are computational predictions transferred from a homolog, not experimental measurements."
  },
  "important_caveats": [
    "All eight TM annotations carry evidence code ECO:0000255 (inferred by similarity), indicating computational predictions transferred from a homologous protein, not experimental measurements (e.g., cryo-EM, crystallography, or cross-linking).",
    "The UniProt entry was first publicly released on 2025-06-18; the historical snapshot checked (entry version 36, released 2026-01-28) already contains these annotations. The author's exact source snapshot is unknown.",
    "The reviewer-only evidence confirms sequence match (SHA-256 identical between benchmark input and UniProt canonical sequence), so the annotation is applicable to the supplied sequence.",
    "The question asks to identify 'a segment that crosses the membrane' (singular) but the choices present complete multi-TM topologies. This wording is slightly misleading but does not change the intended task."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "C"
    ],
    "reason": "The only difference between A and C is whether TM2 starts at residue 41 (Phe) or 42 (Ile). Both residues are hydrophobic, and the preceding residues are K39 (charged) and H40 (charged/polar). A hydrophobicity-window analysis could reasonably place the boundary at either position depending on window size and threshold. Without the specific prediction algorithm's parameters, both A and C are defensible from a sequence-analysis standpoint."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0005",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A0A0H3KA40 (LyrA/SpdC from S. aureus Newman) annotates exactly eight transmembrane helical regions: 9-29, 41-61, 84-104, 118-138, 153-173, 175-195, 202-222, and 231-251. Choice C matches all eight regions with identical boundaries. The sequence in the question matches the canonical entry (419 AA, SHA-256 confirmed). Note that all eight annotations carry evidence code ECO:0000255 (inferred by similarity), meaning these are computational predictions transferred from a homolog, not experimental measurements.",
    "evidence_ids": ["C5", "C6", "C7", "C8", "C9", "C10", "C11", "C12", "H4", "H5", "H6", "H7", "H8", "H9", "H10", "H11"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "Choice D (3..23) can be eliminated by recognizing the protein as a multi-pass membrane protein with multiple hydrophobic stretches. A weak biological argument favors C over A: position 41 is Phe (strongly hydrophobic) immediately following charged residues K39 and H40, so the hydrophobic TM core naturally begins at F41 rather than I42. However, this single-residue boundary shift is within the noise of any hydrophobicity-window predictor. The B vs C distinction (7 vs 8 TMs) requires assessing whether residues 231-251 (IKVIAISTAIVAVGYIGLSLIIR) constitute a TM; this region is mixed (contains K, S, T, R) and borderline, making the call dependent on the specific prediction tool's thresholds.",
    "missing_item_specific_fact": "The exact boundary of TM2 (residue 41 vs 42) and the inclusion/exclusion of TM8 (231-251) depend on the specific computational prediction algorithm and its window size, scoring matrix, and thresholds used to generate the ECO:0000255 annotations. No general biological principle definitively resolves the single-residue shift or the borderline hydrophobicity of the 231-251 segment.",
    "reason": "While D is clearly eliminable and the multi-pass topology is evident from the sequence, the definitive distinctions between A and C (one-residue TM2 boundary shift) and between B and C (inclusion of the borderline 8th TM) cannot be resolved by general biological reasoning. These boundaries are artifacts of the specific prediction tool used for the UniProt annotation (ECO:0000255, inferred by similarity). Selecting C over A and B requires knowing the exact output of that particular predictor, i.e., memorizing the database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "C"],
    "reason": "The only difference between A and C is whether TM2 starts at residue 41 (Phe) or 42 (Ile). Both residues are hydrophobic, and the preceding residues are K39 (charged) and H40 (charged/polar). A hydrophobicity-window analysis could reasonably place the boundary at either position depending on window size and threshold. Without the specific prediction algorithm's parameters, both A and C are defensible from a sequence-analysis standpoint."
  },
  "important_caveats": [
    "All eight TM annotations carry evidence code ECO:0000255 (inferred by similarity), indicating computational predictions transferred from a homologous protein, not experimental measurements (e.g., cryo-EM, crystallography, or cross-linking).",
    "The UniProt entry was first publicly released on 2025-06-18; the historical snapshot checked (entry version 36, released 2026-01-28) already contains these annotations. The author's exact source snapshot is unknown.",
    "The reviewer-only evidence confirms sequence match (SHA-256 identical between benchmark input and UniProt canonical sequence), so the annotation is applicable to the supplied sequence.",
    "The question asks to identify 'a segment that crosses the membrane' (singular) but the choices present complete multi-TM topologies. This wording is slightly misleading but does not change the intended task."
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

**Accession:** `A0A0H3KA40` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 36. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0H3KA40.json)  
**Locator:** `/features/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:09.578744+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":29},"start":{"modifier":"EXACT","value":9}},"type":"Transmembrane"}
```

Source SHA-256: `01b319fc1f34daeda156e8cfc7e6f4bb541e8c4bcb4a73e8f3c4f78c8d2c62d2`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0H3KA40.json)  
**Locator:** `/features/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:09.578744+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":61},"start":{"modifier":"EXACT","value":41}},"type":"Transmembrane"}
```

Source SHA-256: `01b319fc1f34daeda156e8cfc7e6f4bb541e8c4bcb4a73e8f3c4f78c8d2c62d2`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0H3KA40.json)  
**Locator:** `/features/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:09.578744+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":104},"start":{"modifier":"EXACT","value":84}},"type":"Transmembrane"}
```

Source SHA-256: `01b319fc1f34daeda156e8cfc7e6f4bb541e8c4bcb4a73e8f3c4f78c8d2c62d2`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0H3KA40.json)  
**Locator:** `/features/4`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:09.578744+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":138},"start":{"modifier":"EXACT","value":118}},"type":"Transmembrane"}
```

Source SHA-256: `01b319fc1f34daeda156e8cfc7e6f4bb541e8c4bcb4a73e8f3c4f78c8d2c62d2`.

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0H3KA40.json)  
**Locator:** `/features/5`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:09.578744+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":173},"start":{"modifier":"EXACT","value":153}},"type":"Transmembrane"}
```

Source SHA-256: `01b319fc1f34daeda156e8cfc7e6f4bb541e8c4bcb4a73e8f3c4f78c8d2c62d2`.

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0H3KA40.json)  
**Locator:** `/features/6`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:09.578744+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":195},"start":{"modifier":"EXACT","value":175}},"type":"Transmembrane"}
```

Source SHA-256: `01b319fc1f34daeda156e8cfc7e6f4bb541e8c4bcb4a73e8f3c4f78c8d2c62d2`.

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0H3KA40.json)  
**Locator:** `/features/7`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:09.578744+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":222},"start":{"modifier":"EXACT","value":202}},"type":"Transmembrane"}
```

Source SHA-256: `01b319fc1f34daeda156e8cfc7e6f4bb541e8c4bcb4a73e8f3c4f78c8d2c62d2`.

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0H3KA40.json)  
**Locator:** `/features/8`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:09.578744+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":251},"start":{"modifier":"EXACT","value":231}},"type":"Transmembrane"}
```

Source SHA-256: `01b319fc1f34daeda156e8cfc7e6f4bb541e8c4bcb4a73e8f3c4f78c8d2c62d2`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0H3KA40?format=txt&versions=36)  
**Locator:** `lines 96-98`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 36 / 1.  
**Retrieved:** 2026-11-02T04:24:11.851883+00:00.  

```text
FT   TRANSMEM        9..29
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `d02c88a1544f67f6b8c7af47b40f478812539c62fe01fc0b43e7958088f0d2ff`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0H3KA40?format=txt&versions=36)  
**Locator:** `lines 99-101`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 36 / 1.  
**Retrieved:** 2026-11-02T04:24:11.851883+00:00.  

```text
FT   TRANSMEM        41..61
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `d02c88a1544f67f6b8c7af47b40f478812539c62fe01fc0b43e7958088f0d2ff`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0H3KA40?format=txt&versions=36)  
**Locator:** `lines 102-104`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 36 / 1.  
**Retrieved:** 2026-11-02T04:24:11.851883+00:00.  

```text
FT   TRANSMEM        84..104
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `d02c88a1544f67f6b8c7af47b40f478812539c62fe01fc0b43e7958088f0d2ff`.

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0H3KA40?format=txt&versions=36)  
**Locator:** `lines 105-107`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 36 / 1.  
**Retrieved:** 2026-11-02T04:24:11.851883+00:00.  

```text
FT   TRANSMEM        118..138
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `d02c88a1544f67f6b8c7af47b40f478812539c62fe01fc0b43e7958088f0d2ff`.

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0H3KA40?format=txt&versions=36)  
**Locator:** `lines 108-110`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 36 / 1.  
**Retrieved:** 2026-11-02T04:24:11.851883+00:00.  

```text
FT   TRANSMEM        153..173
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `d02c88a1544f67f6b8c7af47b40f478812539c62fe01fc0b43e7958088f0d2ff`.

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0H3KA40?format=txt&versions=36)  
**Locator:** `lines 111-113`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 36 / 1.  
**Retrieved:** 2026-11-02T04:24:11.851883+00:00.  

```text
FT   TRANSMEM        175..195
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `d02c88a1544f67f6b8c7af47b40f478812539c62fe01fc0b43e7958088f0d2ff`.

### Evidence H10

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0H3KA40?format=txt&versions=36)  
**Locator:** `lines 114-116`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 36 / 1.  
**Retrieved:** 2026-11-02T04:24:11.851883+00:00.  

```text
FT   TRANSMEM        202..222
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `d02c88a1544f67f6b8c7af47b40f478812539c62fe01fc0b43e7958088f0d2ff`.

### Evidence H11

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0H3KA40?format=txt&versions=36)  
**Locator:** `lines 117-119`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 36 / 1.  
**Retrieved:** 2026-11-02T04:24:11.851883+00:00.  

```text
FT   TRANSMEM        231..251
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `d02c88a1544f67f6b8c7af47b40f478812539c62fe01fc0b43e7958088f0d2ff`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json), zero-based source row 5. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
