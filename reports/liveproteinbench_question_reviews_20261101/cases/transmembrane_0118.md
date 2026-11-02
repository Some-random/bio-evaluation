# transmembrane_0118

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `transmembrane`  
**Author expected answer:** **A** — 27..47; 78..98; 108..128; 136..156; 173..193; 209..229; 338..358; 362..382; 401..421; 433..453; 466..486

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MSLKGGTAAPAPMAPPRKWYDMTSAEFYVYVVAFMCGISIMMPINAVFSAPSYMLEYYLYATKDPFLVPKMTNFWTNVMTYYNLISMVTSLVVEPLTLLKSFRKIPMLVRLLGGLSVLIIEIIVLMVVPARGTTEAGAVATMCIAGFIGGLGTSIFESTVYGMFGAFPPSFTSIMMGGVGISGVLTSLIQIIVKAALPDTYEGVKKQSYIYYSLDVGIQAATFIALIMMRFNSFAQLHFGDLGGVKSKVDAGSLAGAGENVREPGAEATELEQYTEPAIGQIQEKNAEAHKDDPLAERELSEEESGDSRAVEAAGEAPTSNEILRATSVFSVLRSVKWMFVACGFNFLITLFLFPGIATGMFPESKWFATVAVFIFNCCDVLGRFSSAFRITWPRRYNQRWIIVAASFARVIFVPLLLLHSYHYIPSEAYGYVMQVVFGLSSGYIASMALVLGPQSKGIDNDGKRFVAGTLMGISILVGGTIGTVLSIMTQTIRETY

[Multiple Choices]
A. 27..47; 78..98; 108..128; 136..156; 173..193; 209..229; 338..358; 362..382; 401..421; 433..453; 466..486
B. 27..47; 78..98; 108..128; 136..156; 173..193; 209..229; 338..358; 362..382; 399..417; 433..453; 466..486
C. 222..242
D. 27..47; 78..98; 108..128; 136..156; 173..193; 209..229; 338..358; 401..421; 433..453; 466..486
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

> The sequence exactly matches the cited UniProt record, whose annotated transmembrane ranges correspond to choice A. These features are marked ECO:0000255, indicating computational annotation rather than direct experimental determination of the boundaries.

Citations as saved: [C1](#evidence-c1), [H6](#evidence-h6), [H8](#evidence-h8), [H10](#evidence-h10), [H12](#evidence-h12), [H14](#evidence-h14), [H16](#evidence-h16), [H18](#evidence-h18), [H20](#evidence-h20), [H22](#evidence-h22), [H24](#evidence-h24), [H26](#evidence-h26).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has repeated strongly hydrophobic stretches of roughly membrane-spanning length, with intervening more polar regions, supporting the listed multi-pass topology. In particular, the hydrophobic stretch around 362–382 is a plausible membrane-spanning helix omitted by D, and the sequence pattern around 401–421 favors A over the shorter, shifted B interval.


**Missing item-specific fact**

> No specific database annotation is required to distinguish the choices at the level of sequence-based transmembrane prediction; the exact residue boundaries remain estimates.


**Reason**

> The supplied sequence and choices provide meaningful hydropathy-based grounds for identifying the spans and favoring A. The external annotation supports the key but is not needed as the model's input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> A is the choice whose intervals match the sequence's predicted membrane-spanning stretches; the other options omit a clear span or give a less plausible shifted/shortened interval.


### Important caveats

- The cited UniProt transmembrane features are computational annotations, not evidence that every boundary was experimentally mapped.
- The historical and current source records match the supplied sequence, but the author's exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has repeated strongly hydrophobic stretches of roughly membrane-spanning length, with intervening more polar regions, supporting the listed multi-pass topology. In particular, the hydrophobic stretch around 362–382 is a plausible membrane-spanning helix omitted by D, and the sequence pattern around 401–421 favors A over the shorter, shifted B interval.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "No specific database annotation is required to distinguish the choices at the level of sequence-based transmembrane prediction; the exact residue boundaries remain estimates.",
    "reason": "The supplied sequence and choices provide meaningful hydropathy-based grounds for identifying the spans and favoring A. The external annotation supports the key but is not needed as the model's input."
  },
  "case_id": "transmembrane_0118",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "H6",
      "H8",
      "H10",
      "H12",
      "H14",
      "H16",
      "H18",
      "H20",
      "H22",
      "H24",
      "H26"
    ],
    "judgment": "supported",
    "reason": "The sequence exactly matches the cited UniProt record, whose annotated transmembrane ranges correspond to choice A. These features are marked ECO:0000255, indicating computational annotation rather than direct experimental determination of the boundaries."
  },
  "important_caveats": [
    "The cited UniProt transmembrane features are computational annotations, not evidence that every boundary was experimentally mapped.",
    "The historical and current source records match the supplied sequence, but the author's exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "A is the choice whose intervals match the sequence's predicted membrane-spanning stretches; the other options omit a clear span or give a less plausible shifted/shortened interval."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0118",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence exactly matches the cited UniProt record, whose annotated transmembrane ranges correspond to choice A. These features are marked ECO:0000255, indicating computational annotation rather than direct experimental determination of the boundaries.",
    "evidence_ids": ["C1", "H6", "H8", "H10", "H12", "H14", "H16", "H18", "H20", "H22", "H24", "H26"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has repeated strongly hydrophobic stretches of roughly membrane-spanning length, with intervening more polar regions, supporting the listed multi-pass topology. In particular, the hydrophobic stretch around 362–382 is a plausible membrane-spanning helix omitted by D, and the sequence pattern around 401–421 favors A over the shorter, shifted B interval.",
    "missing_item_specific_fact": "No specific database annotation is required to distinguish the choices at the level of sequence-based transmembrane prediction; the exact residue boundaries remain estimates.",
    "reason": "The supplied sequence and choices provide meaningful hydropathy-based grounds for identifying the spans and favoring A. The external annotation supports the key but is not needed as the model's input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "A is the choice whose intervals match the sequence's predicted membrane-spanning stretches; the other options omit a clear span or give a less plausible shifted/shortened interval."
  },
  "important_caveats": [
    "The cited UniProt transmembrane features are computational annotations, not evidence that every boundary was experimentally mapped.",
    "The historical and current source records match the supplied sequence, but the author's exact source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry Q9GTP5 (Nucleoside transporter 1, CfNT1, from Crithidia fasciculata) annotates exactly 11 transmembrane helical segments at positions 27..47, 78..98, 108..128, 136..156, 173..193, 209..229, 338..358, 362..382, 401..421, 433..453, and 466..486, matching Choice A precisely. The sequence SHA256 matches the benchmark input (497 AA). However, all TM annotations carry evidence code ECO:0000255 ('Predicted by sequence analysis'), meaning these are computational predictions rather than experimentally determined boundaries.

Citations as saved: [C6](#evidence-c6), [C8](#evidence-c8), [C10](#evidence-c10), [C12](#evidence-c12), [C14](#evidence-c14), [C16](#evidence-c16), [C18](#evidence-c18), [C20](#evidence-c20), [C22](#evidence-c22), [C24](#evidence-c24), [C26](#evidence-c26), [H6](#evidence-h6), [H8](#evidence-h8), [H10](#evidence-h10), [H12](#evidence-h12), [H14](#evidence-h14), [H16](#evidence-h16), [H18](#evidence-h18), [H20](#evidence-h20), [H22](#evidence-h22), [H24](#evidence-h24), [H26](#evidence-h26).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The protein is an equilibrative nucleoside transporter (ENT family), which is well-established in the literature to possess 11 transmembrane domains. This family-level knowledge, combined with hydrophobicity analysis of the sequence (identifying ~20-residue hydrophobic stretches) and the alternating cytoplasmic/extracellular topology constraint, allows a model to distinguish the correct 11-TM answer (A) from Choice C (single TM, obviously wrong for an ENT) and Choice D (missing one TM segment, violating the 11-TM ENT topology). The presence of the 362..382 segment can be supported by examining the hydrophobic character of that region and the topological alternation pattern.


**Missing item-specific fact**

> The exact 2-residue boundary shift between Choice A (401..421) and Choice B (399..417) for the 9th TM segment is within the inherent uncertainty of computational TM prediction tools (ECO:0000255). Distinguishing these two options with certainty would require the specific UniProt annotation or the output of the particular prediction algorithm used, as both boundaries fall within the hydrophobic core of the same helix.


**Reason**

> The primary biological reasoning (ENT transporters have 11 TM domains; hydrophobicity analysis; topological alternation) meaningfully distinguishes the correct answer from the major distractors C and D. The A-vs-B distinction is a minor boundary precision issue (2 residues) that sits at the noise floor of TM prediction algorithms, but the overall question tests general transmembrane topology reasoning rather than memorization of one specific database entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "B"
]
```

> Choices A and B differ only in the boundaries of the 9th TM segment (401..421 vs 399..417). Both fall within the same hydrophobic helical region and are within the ±2-3 residue uncertainty typical of TM boundary predictions. Without the exact annotation, a well-reasoned hydrophobicity analysis could plausibly support either boundary. However, since the question forces an exact match and the UniProt annotation specifies 401..421, A is the 'correct' answer by convention.


### Important caveats

- All 11 TM annotations carry evidence code ECO:0000255 (predicted by sequence analysis), not experimental evidence (e.g., crystallography or cryo-EM). The exact boundaries are algorithm-dependent.
- The UniProt entry was first released in 2025 (Swiss-Prot) and the author's source snapshot date is unknown; the annotation may have evolved.
- The A-vs-B boundary difference (401..421 vs 399..417) represents prediction-tool precision rather than a biologically meaningful distinction.
- The reviewer-only UniProt accession (Q9GTP5) was inferred from dataset metadata and was not provided to the evaluated model; the model must work from sequence alone.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The protein is an equilibrative nucleoside transporter (ENT family), which is well-established in the literature to possess 11 transmembrane domains. This family-level knowledge, combined with hydrophobicity analysis of the sequence (identifying ~20-residue hydrophobic stretches) and the alternating cytoplasmic/extracellular topology constraint, allows a model to distinguish the correct 11-TM answer (A) from Choice C (single TM, obviously wrong for an ENT) and Choice D (missing one TM segment, violating the 11-TM ENT topology). The presence of the 362..382 segment can be supported by examining the hydrophobic character of that region and the topological alternation pattern.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The exact 2-residue boundary shift between Choice A (401..421) and Choice B (399..417) for the 9th TM segment is within the inherent uncertainty of computational TM prediction tools (ECO:0000255). Distinguishing these two options with certainty would require the specific UniProt annotation or the output of the particular prediction algorithm used, as both boundaries fall within the hydrophobic core of the same helix.",
    "reason": "The primary biological reasoning (ENT transporters have 11 TM domains; hydrophobicity analysis; topological alternation) meaningfully distinguishes the correct answer from the major distractors C and D. The A-vs-B distinction is a minor boundary precision issue (2 residues) that sits at the noise floor of TM prediction algorithms, but the overall question tests general transmembrane topology reasoning rather than memorization of one specific database entry."
  },
  "case_id": "transmembrane_0118",
  "expected_answer_check": {
    "evidence_ids": [
      "C6",
      "C8",
      "C10",
      "C12",
      "C14",
      "C16",
      "C18",
      "C20",
      "C22",
      "C24",
      "C26",
      "H6",
      "H8",
      "H10",
      "H12",
      "H14",
      "H16",
      "H18",
      "H20",
      "H22",
      "H24",
      "H26"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry Q9GTP5 (Nucleoside transporter 1, CfNT1, from Crithidia fasciculata) annotates exactly 11 transmembrane helical segments at positions 27..47, 78..98, 108..128, 136..156, 173..193, 209..229, 338..358, 362..382, 401..421, 433..453, and 466..486, matching Choice A precisely. The sequence SHA256 matches the benchmark input (497 AA). However, all TM annotations carry evidence code ECO:0000255 ('Predicted by sequence analysis'), meaning these are computational predictions rather than experimentally determined boundaries."
  },
  "important_caveats": [
    "All 11 TM annotations carry evidence code ECO:0000255 (predicted by sequence analysis), not experimental evidence (e.g., crystallography or cryo-EM). The exact boundaries are algorithm-dependent.",
    "The UniProt entry was first released in 2025 (Swiss-Prot) and the author's source snapshot date is unknown; the annotation may have evolved.",
    "The A-vs-B boundary difference (401..421 vs 399..417) represents prediction-tool precision rather than a biologically meaningful distinction.",
    "The reviewer-only UniProt accession (Q9GTP5) was inferred from dataset metadata and was not provided to the evaluated model; the model must work from sequence alone."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "B"
    ],
    "reason": "Choices A and B differ only in the boundaries of the 9th TM segment (401..421 vs 399..417). Both fall within the same hydrophobic helical region and are within the ±2-3 residue uncertainty typical of TM boundary predictions. Without the exact annotation, a well-reasoned hydrophobicity analysis could plausibly support either boundary. However, since the question forces an exact match and the UniProt annotation specifies 401..421, A is the 'correct' answer by convention."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0118",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry Q9GTP5 (Nucleoside transporter 1, CfNT1, from Crithidia fasciculata) annotates exactly 11 transmembrane helical segments at positions 27..47, 78..98, 108..128, 136..156, 173..193, 209..229, 338..358, 362..382, 401..421, 433..453, and 466..486, matching Choice A precisely. The sequence SHA256 matches the benchmark input (497 AA). However, all TM annotations carry evidence code ECO:0000255 ('Predicted by sequence analysis'), meaning these are computational predictions rather than experimentally determined boundaries.",
    "evidence_ids": ["C6","C8","C10","C12","C14","C16","C18","C20","C22","C24","C26","H6","H8","H10","H12","H14","H16","H18","H20","H22","H24","H26"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The protein is an equilibrative nucleoside transporter (ENT family), which is well-established in the literature to possess 11 transmembrane domains. This family-level knowledge, combined with hydrophobicity analysis of the sequence (identifying ~20-residue hydrophobic stretches) and the alternating cytoplasmic/extracellular topology constraint, allows a model to distinguish the correct 11-TM answer (A) from Choice C (single TM, obviously wrong for an ENT) and Choice D (missing one TM segment, violating the 11-TM ENT topology). The presence of the 362..382 segment can be supported by examining the hydrophobic character of that region and the topological alternation pattern.",
    "missing_item_specific_fact": "The exact 2-residue boundary shift between Choice A (401..421) and Choice B (399..417) for the 9th TM segment is within the inherent uncertainty of computational TM prediction tools (ECO:0000255). Distinguishing these two options with certainty would require the specific UniProt annotation or the output of the particular prediction algorithm used, as both boundaries fall within the hydrophobic core of the same helix.",
    "reason": "The primary biological reasoning (ENT transporters have 11 TM domains; hydrophobicity analysis; topological alternation) meaningfully distinguishes the correct answer from the major distractors C and D. The A-vs-B distinction is a minor boundary precision issue (2 residues) that sits at the noise floor of TM prediction algorithms, but the overall question tests general transmembrane topology reasoning rather than memorization of one specific database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "B"],
    "reason": "Choices A and B differ only in the boundaries of the 9th TM segment (401..421 vs 399..417). Both fall within the same hydrophobic helical region and are within the ±2-3 residue uncertainty typical of TM boundary predictions. Without the exact annotation, a well-reasoned hydrophobicity analysis could plausibly support either boundary. However, since the question forces an exact match and the UniProt annotation specifies 401..421, A is the 'correct' answer by convention."
  },
  "important_caveats": [
    "All 11 TM annotations carry evidence code ECO:0000255 (predicted by sequence analysis), not experimental evidence (e.g., crystallography or cryo-EM). The exact boundaries are algorithm-dependent.",
    "The UniProt entry was first released in 2025 (Swiss-Prot) and the author's source snapshot date is unknown; the annotation may have evolved.",
    "The A-vs-B boundary difference (401..421 vs 399..417) represents prediction-tool precision rather than a biologically meaningful distinction.",
    "The reviewer-only UniProt accession (Q9GTP5) was inferred from dataset metadata and was not provided to the evaluated model; the model must work from sequence alone."
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

**Accession:** `Q9GTP5` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 57. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9GTP5.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:26.527509+00:00.  

```json
"Q9GTP5"
```

Source SHA-256: `1543207ed03c551de730c893aa46260773725d011a3be50c53bd77787e5c817f`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9GTP5.json)  
**Locator:** `/features/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:26.527509+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":47},"start":{"modifier":"EXACT","value":27}},"type":"Transmembrane"}
```

Source SHA-256: `1543207ed03c551de730c893aa46260773725d011a3be50c53bd77787e5c817f`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9GTP5.json)  
**Locator:** `/features/4`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:26.527509+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":98},"start":{"modifier":"EXACT","value":78}},"type":"Transmembrane"}
```

Source SHA-256: `1543207ed03c551de730c893aa46260773725d011a3be50c53bd77787e5c817f`.

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9GTP5.json)  
**Locator:** `/features/6`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:26.527509+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":128},"start":{"modifier":"EXACT","value":108}},"type":"Transmembrane"}
```

Source SHA-256: `1543207ed03c551de730c893aa46260773725d011a3be50c53bd77787e5c817f`.

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9GTP5.json)  
**Locator:** `/features/8`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:26.527509+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":156},"start":{"modifier":"EXACT","value":136}},"type":"Transmembrane"}
```

Source SHA-256: `1543207ed03c551de730c893aa46260773725d011a3be50c53bd77787e5c817f`.

### Evidence C14

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9GTP5.json)  
**Locator:** `/features/10`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:26.527509+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":193},"start":{"modifier":"EXACT","value":173}},"type":"Transmembrane"}
```

Source SHA-256: `1543207ed03c551de730c893aa46260773725d011a3be50c53bd77787e5c817f`.

### Evidence C16

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9GTP5.json)  
**Locator:** `/features/12`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:26.527509+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":229},"start":{"modifier":"EXACT","value":209}},"type":"Transmembrane"}
```

Source SHA-256: `1543207ed03c551de730c893aa46260773725d011a3be50c53bd77787e5c817f`.

### Evidence C18

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9GTP5.json)  
**Locator:** `/features/14`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:26.527509+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":358},"start":{"modifier":"EXACT","value":338}},"type":"Transmembrane"}
```

Source SHA-256: `1543207ed03c551de730c893aa46260773725d011a3be50c53bd77787e5c817f`.

### Evidence C20

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9GTP5.json)  
**Locator:** `/features/16`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:26.527509+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":382},"start":{"modifier":"EXACT","value":362}},"type":"Transmembrane"}
```

Source SHA-256: `1543207ed03c551de730c893aa46260773725d011a3be50c53bd77787e5c817f`.

### Evidence C22

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9GTP5.json)  
**Locator:** `/features/18`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:26.527509+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":421},"start":{"modifier":"EXACT","value":401}},"type":"Transmembrane"}
```

Source SHA-256: `1543207ed03c551de730c893aa46260773725d011a3be50c53bd77787e5c817f`.

### Evidence C24

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9GTP5.json)  
**Locator:** `/features/20`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:26.527509+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":453},"start":{"modifier":"EXACT","value":433}},"type":"Transmembrane"}
```

Source SHA-256: `1543207ed03c551de730c893aa46260773725d011a3be50c53bd77787e5c817f`.

### Evidence C26

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9GTP5.json)  
**Locator:** `/features/22`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:26.527509+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":486},"start":{"modifier":"EXACT","value":466}},"type":"Transmembrane"}
```

Source SHA-256: `1543207ed03c551de730c893aa46260773725d011a3be50c53bd77787e5c817f`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9GTP5?format=txt&versions=57)  
**Locator:** `lines 104-106`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 57 / 1.  
**Retrieved:** 2026-11-01T06:28:47.063579+00:00.  

```text
FT   TRANSMEM        27..47
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `7426320c762a09c28cce26459dfd7f6960cc0a07dde3142fc087281aecaff990`.

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9GTP5?format=txt&versions=57)  
**Locator:** `lines 110-112`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 57 / 1.  
**Retrieved:** 2026-11-01T06:28:47.063579+00:00.  

```text
FT   TRANSMEM        78..98
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `7426320c762a09c28cce26459dfd7f6960cc0a07dde3142fc087281aecaff990`.

### Evidence H10

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9GTP5?format=txt&versions=57)  
**Locator:** `lines 116-118`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 57 / 1.  
**Retrieved:** 2026-11-01T06:28:47.063579+00:00.  

```text
FT   TRANSMEM        108..128
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `7426320c762a09c28cce26459dfd7f6960cc0a07dde3142fc087281aecaff990`.

### Evidence H12

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9GTP5?format=txt&versions=57)  
**Locator:** `lines 122-124`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 57 / 1.  
**Retrieved:** 2026-11-01T06:28:47.063579+00:00.  

```text
FT   TRANSMEM        136..156
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `7426320c762a09c28cce26459dfd7f6960cc0a07dde3142fc087281aecaff990`.

### Evidence H14

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9GTP5?format=txt&versions=57)  
**Locator:** `lines 128-130`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 57 / 1.  
**Retrieved:** 2026-11-01T06:28:47.063579+00:00.  

```text
FT   TRANSMEM        173..193
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `7426320c762a09c28cce26459dfd7f6960cc0a07dde3142fc087281aecaff990`.

### Evidence H16

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9GTP5?format=txt&versions=57)  
**Locator:** `lines 134-136`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 57 / 1.  
**Retrieved:** 2026-11-01T06:28:47.063579+00:00.  

```text
FT   TRANSMEM        209..229
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `7426320c762a09c28cce26459dfd7f6960cc0a07dde3142fc087281aecaff990`.

### Evidence H18

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9GTP5?format=txt&versions=57)  
**Locator:** `lines 140-142`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 57 / 1.  
**Retrieved:** 2026-11-01T06:28:47.063579+00:00.  

```text
FT   TRANSMEM        338..358
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `7426320c762a09c28cce26459dfd7f6960cc0a07dde3142fc087281aecaff990`.

### Evidence H20

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9GTP5?format=txt&versions=57)  
**Locator:** `lines 146-148`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 57 / 1.  
**Retrieved:** 2026-11-01T06:28:47.063579+00:00.  

```text
FT   TRANSMEM        362..382
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `7426320c762a09c28cce26459dfd7f6960cc0a07dde3142fc087281aecaff990`.

### Evidence H22

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9GTP5?format=txt&versions=57)  
**Locator:** `lines 152-154`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 57 / 1.  
**Retrieved:** 2026-11-01T06:28:47.063579+00:00.  

```text
FT   TRANSMEM        401..421
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `7426320c762a09c28cce26459dfd7f6960cc0a07dde3142fc087281aecaff990`.

### Evidence H24

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9GTP5?format=txt&versions=57)  
**Locator:** `lines 158-160`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 57 / 1.  
**Retrieved:** 2026-11-01T06:28:47.063579+00:00.  

```text
FT   TRANSMEM        433..453
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `7426320c762a09c28cce26459dfd7f6960cc0a07dde3142fc087281aecaff990`.

### Evidence H26

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9GTP5?format=txt&versions=57)  
**Locator:** `lines 164-166`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 57 / 1.  
**Retrieved:** 2026-11-01T06:28:47.063579+00:00.  

```text
FT   TRANSMEM        466..486
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `7426320c762a09c28cce26459dfd7f6960cc0a07dde3142fc087281aecaff990`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json), zero-based source row 118. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
