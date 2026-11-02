# transmembrane_0024

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `transmembrane`  
**Author expected answer:** **D** — 10..30; 45..65; 75..95; 105..125; 142..162; 243..263; 269..289

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MSQPEFTRSIVGASFLLPVINGAMHIPPAVSATRVTLEDNQPRDAPILVLLFALSVLIDVMDKAADLPRQTRKTWLMTIVVFASPFVVLAVYGTMHCGLLALLRLLGVPLLAVVHAMPLIPVYSWKTGSISTVKLKYFLGPFKSLFGATCIGLMDVTAVVLYLRGTMLHPENASSAGHFRVLMYTITYDFLWESICDVRDIQEDEQNNITTLATAFGVRPTLIFLGGSTMMGDLSITLLGGGSAVLSVVRSTVFWGAFAALALHKPRSAVYPWGLATLFGLLPVWLASLGART

[Multiple Choices]
A. 10..30; 45..65; 105..125; 142..162; 243..263; 269..289
B. 10..30; 49..60; 75..95; 105..125; 142..162; 243..263; 269..289
C. 1404..1424
D. 10..30; 45..65; 75..95; 105..125; 142..162; 243..263; 269..289
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

> The sequence-matched UniProt record annotates all seven regions in choice D as helical transmembrane segments. These annotations carry evidence code ECO:0000255, indicating computational evidence, not necessarily experimental confirmation.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [C9](#evidence-c9), [C10](#evidence-c10), [C11](#evidence-c11).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains multiple long, strongly hydrophobic stretches consistent with membrane-spanning helices, including stretches corresponding to the seven intervals in D. D includes those intervals, whereas A omits one and B substitutes a shortened interval; C gives an incompatible coordinate.


**Missing item-specific fact**

> No protein-specific database fact is required to distinguish the choices at this level, although exact helix boundaries would ordinarily be prediction-dependent.


**Reason**

> The sequence hydropathy provides meaningful grounds to favor D over the alternatives; the external annotation supports the key but is not the basis for classifying the question as answerable.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Only D lists all the hydrophobic candidate segments with the stated boundaries; the other choices omit, truncate, or misplace regions.


### Important caveats

- The supporting UniProt transmembrane annotations are computational (ECO:0000255), not evidence of direct experimental measurement.
- Hydropathy supports the predicted regions but does not establish exact membrane boundaries with mathematical certainty.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains multiple long, strongly hydrophobic stretches consistent with membrane-spanning helices, including stretches corresponding to the seven intervals in D. D includes those intervals, whereas A omits one and B substitutes a shortened interval; C gives an incompatible coordinate.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "No protein-specific database fact is required to distinguish the choices at this level, although exact helix boundaries would ordinarily be prediction-dependent.",
    "reason": "The sequence hydropathy provides meaningful grounds to favor D over the alternatives; the external annotation supports the key but is not the basis for classifying the question as answerable."
  },
  "case_id": "transmembrane_0024",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "C7",
      "C8",
      "C9",
      "C10",
      "C11"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates all seven regions in choice D as helical transmembrane segments. These annotations carry evidence code ECO:0000255, indicating computational evidence, not necessarily experimental confirmation."
  },
  "important_caveats": [
    "The supporting UniProt transmembrane annotations are computational (ECO:0000255), not evidence of direct experimental measurement.",
    "Hydropathy supports the predicted regions but does not establish exact membrane boundaries with mathematical certainty."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only D lists all the hydrophobic candidate segments with the stated boundaries; the other choices omit, truncate, or misplace regions."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0024",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates all seven regions in choice D as helical transmembrane segments. These annotations carry evidence code ECO:0000255, indicating computational evidence, not necessarily experimental confirmation.",
    "evidence_ids": ["C5", "C6", "C7", "C8", "C9", "C10", "C11"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains multiple long, strongly hydrophobic stretches consistent with membrane-spanning helices, including stretches corresponding to the seven intervals in D. D includes those intervals, whereas A omits one and B substitutes a shortened interval; C gives an incompatible coordinate.",
    "missing_item_specific_fact": "No protein-specific database fact is required to distinguish the choices at this level, although exact helix boundaries would ordinarily be prediction-dependent.",
    "reason": "The sequence hydropathy provides meaningful grounds to favor D over the alternatives; the external annotation supports the key but is not the basis for classifying the question as answerable."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only D lists all the hydrophobic candidate segments with the stated boundaries; the other choices omit, truncate, or misplace regions."
  },
  "important_caveats": [
    "The supporting UniProt transmembrane annotations are computational (ECO:0000255), not evidence of direct experimental measurement.",
    "Hydropathy supports the predicted regions but does not establish exact membrane boundaries with mathematical certainty."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A0A6A6H402 (Prenyltransferase vviA, Viridothelium virens) annotates exactly seven transmembrane helices: 10..30, 45..65, 75..95, 105..125, 142..162, 243..263, 269..289, which matches Choice D precisely. The sequence in the question (293 AA) matches the UniProt sequence (sha256 confirmed). However, all TM annotations carry evidence code ECO:0000255 (inferred by similarity), meaning they are computational predictions by similarity rather than experimental measurements. The annotation is nonetheless the authoritative database record for this protein.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [C9](#evidence-c9), [C10](#evidence-c10), [C11](#evidence-c11), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6), [H7](#evidence-h7), [H8](#evidence-h8), [H9](#evidence-h9).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The choices can be distinguished using general transmembrane helix biology: (1) Choice C (1404..1424) is trivially eliminated because the protein is only 293 residues long. (2) Choice A omits the region 75..95 (WLMTIVVFASPFVVLAVYGTM), which is a highly hydrophobic 21-residue stretch clearly consistent with a TM helix — omitting it is biologically implausible. (3) Choice B replaces 45..65 (21 residues, APILVLLFALSVLIDVMDKAA) with 49..60 (only 12 residues, VLLFALSVLIDV), which is too short to span a ~30 Å lipid bilayer as an α-helix (minimum ~19–20 residues needed). (4) Choice D includes all hydrophobic stretches with appropriate ~21-residue lengths, making it the only biologically coherent option.


**Missing item-specific fact**

> None critical. The precise boundary choices (e.g., why 45..65 rather than 44..64) are algorithm-dependent, but the question's distractors differ in ways (missing a clearly hydrophobic region, helix too short, out-of-range positions) that are addressable by general TM biology without memorizing the UniProt annotation.


**Reason**

> A model applying standard TM helix criteria — hydrophobicity of the segment, minimum helix length of ~20 residues to span the bilayer, and the constraint that positions must fall within the protein length — can eliminate A (missing hydrophobic segment), B (helix too short at 12 residues), and C (out of range), leaving D. This constitutes a concrete biological reasoning chain from the supplied sequence and choices.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four choices differ in biologically meaningful ways (omission of a hydrophobic region, helix length below TM minimum, out-of-range coordinates) that allow a single option to be identified through general reasoning. No two choices are equally defensible under standard TM helix criteria.


### Important caveats

- All seven TM annotations carry ECO:0000255 (inferred by similarity), meaning they are computational predictions, not experimental measurements. Exact boundaries are algorithm-dependent.
- The UniProt entry was first released 2025-04-09; the author's source snapshot is unknown but sequence match is confirmed for both current and historical (v12) records.
- The reasoning pathway relies on the specific distractor design (12-residue vs 21-residue helix, omission of an obvious hydrophobic segment). If distractors had subtler boundary shifts (e.g., 46..66 vs 45..65), pure reasoning would be insufficient and the question would become lookup-dependent.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The choices can be distinguished using general transmembrane helix biology: (1) Choice C (1404..1424) is trivially eliminated because the protein is only 293 residues long. (2) Choice A omits the region 75..95 (WLMTIVVFASPFVVLAVYGTM), which is a highly hydrophobic 21-residue stretch clearly consistent with a TM helix — omitting it is biologically implausible. (3) Choice B replaces 45..65 (21 residues, APILVLLFALSVLIDVMDKAA) with 49..60 (only 12 residues, VLLFALSVLIDV), which is too short to span a ~30 Å lipid bilayer as an α-helix (minimum ~19–20 residues needed). (4) Choice D includes all hydrophobic stretches with appropriate ~21-residue lengths, making it the only biologically coherent option.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None critical. The precise boundary choices (e.g., why 45..65 rather than 44..64) are algorithm-dependent, but the question's distractors differ in ways (missing a clearly hydrophobic region, helix too short, out-of-range positions) that are addressable by general TM biology without memorizing the UniProt annotation.",
    "reason": "A model applying standard TM helix criteria — hydrophobicity of the segment, minimum helix length of ~20 residues to span the bilayer, and the constraint that positions must fall within the protein length — can eliminate A (missing hydrophobic segment), B (helix too short at 12 residues), and C (out of range), leaving D. This constitutes a concrete biological reasoning chain from the supplied sequence and choices."
  },
  "case_id": "transmembrane_0024",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "C7",
      "C8",
      "C9",
      "C10",
      "C11",
      "H3",
      "H4",
      "H5",
      "H6",
      "H7",
      "H8",
      "H9"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry A0A6A6H402 (Prenyltransferase vviA, Viridothelium virens) annotates exactly seven transmembrane helices: 10..30, 45..65, 75..95, 105..125, 142..162, 243..263, 269..289, which matches Choice D precisely. The sequence in the question (293 AA) matches the UniProt sequence (sha256 confirmed). However, all TM annotations carry evidence code ECO:0000255 (inferred by similarity), meaning they are computational predictions by similarity rather than experimental measurements. The annotation is nonetheless the authoritative database record for this protein."
  },
  "important_caveats": [
    "All seven TM annotations carry ECO:0000255 (inferred by similarity), meaning they are computational predictions, not experimental measurements. Exact boundaries are algorithm-dependent.",
    "The UniProt entry was first released 2025-04-09; the author's source snapshot is unknown but sequence match is confirmed for both current and historical (v12) records.",
    "The reasoning pathway relies on the specific distractor design (12-residue vs 21-residue helix, omission of an obvious hydrophobic segment). If distractors had subtler boundary shifts (e.g., 46..66 vs 45..65), pure reasoning would be insufficient and the question would become lookup-dependent."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices differ in biologically meaningful ways (omission of a hydrophobic region, helix length below TM minimum, out-of-range coordinates) that allow a single option to be identified through general reasoning. No two choices are equally defensible under standard TM helix criteria."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0024",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A0A6A6H402 (Prenyltransferase vviA, Viridothelium virens) annotates exactly seven transmembrane helices: 10..30, 45..65, 75..95, 105..125, 142..162, 243..263, 269..289, which matches Choice D precisely. The sequence in the question (293 AA) matches the UniProt sequence (sha256 confirmed). However, all TM annotations carry evidence code ECO:0000255 (inferred by similarity), meaning they are computational predictions by similarity rather than experimental measurements. The annotation is nonetheless the authoritative database record for this protein.",
    "evidence_ids": ["C5", "C6", "C7", "C8", "C9", "C10", "C11", "H3", "H4", "H5", "H6", "H7", "H8", "H9"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The choices can be distinguished using general transmembrane helix biology: (1) Choice C (1404..1424) is trivially eliminated because the protein is only 293 residues long. (2) Choice A omits the region 75..95 (WLMTIVVFASPFVVLAVYGTM), which is a highly hydrophobic 21-residue stretch clearly consistent with a TM helix — omitting it is biologically implausible. (3) Choice B replaces 45..65 (21 residues, APILVLLFALSVLIDVMDKAA) with 49..60 (only 12 residues, VLLFALSVLIDV), which is too short to span a ~30 Å lipid bilayer as an α-helix (minimum ~19–20 residues needed). (4) Choice D includes all hydrophobic stretches with appropriate ~21-residue lengths, making it the only biologically coherent option.",
    "missing_item_specific_fact": "None critical. The precise boundary choices (e.g., why 45..65 rather than 44..64) are algorithm-dependent, but the question's distractors differ in ways (missing a clearly hydrophobic region, helix too short, out-of-range positions) that are addressable by general TM biology without memorizing the UniProt annotation.",
    "reason": "A model applying standard TM helix criteria — hydrophobicity of the segment, minimum helix length of ~20 residues to span the bilayer, and the constraint that positions must fall within the protein length — can eliminate A (missing hydrophobic segment), B (helix too short at 12 residues), and C (out of range), leaving D. This constitutes a concrete biological reasoning chain from the supplied sequence and choices."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices differ in biologically meaningful ways (omission of a hydrophobic region, helix length below TM minimum, out-of-range coordinates) that allow a single option to be identified through general reasoning. No two choices are equally defensible under standard TM helix criteria."
  },
  "important_caveats": [
    "All seven TM annotations carry ECO:0000255 (inferred by similarity), meaning they are computational predictions, not experimental measurements. Exact boundaries are algorithm-dependent.",
    "The UniProt entry was first released 2025-04-09; the author's source snapshot is unknown but sequence match is confirmed for both current and historical (v12) records.",
    "The reasoning pathway relies on the specific distractor design (12-residue vs 21-residue helix, omission of an obvious hydrophobic segment). If distractors had subtler boundary shifts (e.g., 46..66 vs 45..65), pure reasoning would be insufficient and the question would become lookup-dependent."
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

**Accession:** `A0A6A6H402` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 12. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A6A6H402.json)  
**Locator:** `/features/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:32.724960+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":30},"start":{"modifier":"EXACT","value":10}},"type":"Transmembrane"}
```

Source SHA-256: `b8205d729e2e5bd4217fba29840a41164bb96c507173b89acd7a02b8a587f862`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A6A6H402.json)  
**Locator:** `/features/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:32.724960+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":65},"start":{"modifier":"EXACT","value":45}},"type":"Transmembrane"}
```

Source SHA-256: `b8205d729e2e5bd4217fba29840a41164bb96c507173b89acd7a02b8a587f862`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A6A6H402.json)  
**Locator:** `/features/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:32.724960+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":95},"start":{"modifier":"EXACT","value":75}},"type":"Transmembrane"}
```

Source SHA-256: `b8205d729e2e5bd4217fba29840a41164bb96c507173b89acd7a02b8a587f862`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A6A6H402.json)  
**Locator:** `/features/4`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:32.724960+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":125},"start":{"modifier":"EXACT","value":105}},"type":"Transmembrane"}
```

Source SHA-256: `b8205d729e2e5bd4217fba29840a41164bb96c507173b89acd7a02b8a587f862`.

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A6A6H402.json)  
**Locator:** `/features/5`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:32.724960+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":162},"start":{"modifier":"EXACT","value":142}},"type":"Transmembrane"}
```

Source SHA-256: `b8205d729e2e5bd4217fba29840a41164bb96c507173b89acd7a02b8a587f862`.

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A6A6H402.json)  
**Locator:** `/features/6`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:32.724960+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":263},"start":{"modifier":"EXACT","value":243}},"type":"Transmembrane"}
```

Source SHA-256: `b8205d729e2e5bd4217fba29840a41164bb96c507173b89acd7a02b8a587f862`.

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A6A6H402.json)  
**Locator:** `/features/7`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:32.724960+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":289},"start":{"modifier":"EXACT","value":269}},"type":"Transmembrane"}
```

Source SHA-256: `b8205d729e2e5bd4217fba29840a41164bb96c507173b89acd7a02b8a587f862`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A6A6H402?format=txt&versions=12)  
**Locator:** `lines 81-83`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 12 / 1.  
**Retrieved:** 2026-11-02T04:25:34.642719+00:00.  

```text
FT   TRANSMEM        10..30
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `f3fb0188f37dd39fa5b2add2435b66089c72d61d50cfdb8351cca69e37efe727`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A6A6H402?format=txt&versions=12)  
**Locator:** `lines 84-86`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 12 / 1.  
**Retrieved:** 2026-11-02T04:25:34.642719+00:00.  

```text
FT   TRANSMEM        45..65
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `f3fb0188f37dd39fa5b2add2435b66089c72d61d50cfdb8351cca69e37efe727`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A6A6H402?format=txt&versions=12)  
**Locator:** `lines 87-89`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 12 / 1.  
**Retrieved:** 2026-11-02T04:25:34.642719+00:00.  

```text
FT   TRANSMEM        75..95
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `f3fb0188f37dd39fa5b2add2435b66089c72d61d50cfdb8351cca69e37efe727`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A6A6H402?format=txt&versions=12)  
**Locator:** `lines 90-92`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 12 / 1.  
**Retrieved:** 2026-11-02T04:25:34.642719+00:00.  

```text
FT   TRANSMEM        105..125
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `f3fb0188f37dd39fa5b2add2435b66089c72d61d50cfdb8351cca69e37efe727`.

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A6A6H402?format=txt&versions=12)  
**Locator:** `lines 93-95`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 12 / 1.  
**Retrieved:** 2026-11-02T04:25:34.642719+00:00.  

```text
FT   TRANSMEM        142..162
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `f3fb0188f37dd39fa5b2add2435b66089c72d61d50cfdb8351cca69e37efe727`.

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A6A6H402?format=txt&versions=12)  
**Locator:** `lines 96-98`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 12 / 1.  
**Retrieved:** 2026-11-02T04:25:34.642719+00:00.  

```text
FT   TRANSMEM        243..263
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `f3fb0188f37dd39fa5b2add2435b66089c72d61d50cfdb8351cca69e37efe727`.

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A6A6H402?format=txt&versions=12)  
**Locator:** `lines 99-101`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 12 / 1.  
**Retrieved:** 2026-11-02T04:25:34.642719+00:00.  

```text
FT   TRANSMEM        269..289
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `f3fb0188f37dd39fa5b2add2435b66089c72d61d50cfdb8351cca69e37efe727`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json), zero-based source row 24. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
