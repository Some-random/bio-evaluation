# transmembrane_0100

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `transmembrane`  
**Author expected answer:** **C** — 1..21; 31..51; 56..76; 77..97; 101..121; 128..148; 149..169; 182..202; 206..226; 321..341

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MFGFDNLILGVYLFNFLLILTATYTDIKERIIPHFVIILMLIVNLPIGYYFFGFDAITSFFATLILCLILGVGMGGGDVKMFTALSPLFAAETIYFVPKDISILIGLSALFAAIFPMTKILKNYWKDIIPSSAYLAMLIGIIVSITEIYSIGNTKTILWSYIILSIFISRKIPKYRIISNKLGYITPIYLIGFYLLNPAYFVSENVLISFFVYIGQLSLISLVIYALTGAEISSKKQISDLKEGDIIRDIVTIKENGEVTVENANILKRFKHMIYGEMGKLEGKSLMTDGEGLSDENLELLNKLQNEGKIGGELNVLTTYPFVPFVLVAYCVITLLNMGVINYLVG

[Multiple Choices]
A. 357..377; 397..419; 481..501; 506..526; 591..611; 619..639
B. 1..21; 33..56; 56..76; 77..97; 101..121; 128..148; 149..169; 182..202; 206..226; 321..341
C. 1..21; 31..51; 56..76; 77..97; 101..121; 128..148; 149..169; 182..202; 206..226; 321..341
D. 1..21; 31..51; 56..76; 101..121; 128..148; 149..169; 182..202; 206..226; 321..341
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

> Choice C matches the transmembrane intervals annotated for the exact matching sequence in both the current UniProt record and a historical snapshot. These annotations carry ECO:0000255, indicating computational evidence; they support the key as an annotation-based answer, not as direct experimental confirmation.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [C9](#evidence-c9), [C10](#evidence-c10), [C11](#evidence-c11), [C12](#evidence-c12), [C13](#evidence-c13), [C14](#evidence-c14), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6), [H7](#evidence-h7), [H8](#evidence-h8), [H9](#evidence-h9), [H10](#evidence-h10), [H11](#evidence-h11), [H12](#evidence-h12), [H13](#evidence-h13).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence has many hydrophobic stretches, which makes a multi-pass membrane protein plausible and supports several candidate regions. But that general signal does not robustly establish the complete set of spans or their exact boundaries, especially for the less clearly hydrophobic 77..97 interval.


**Missing item-specific fact**

> The sequence-specific transmembrane-region annotation, including its predicted intervals and boundary conventions, is absent from the prompt.


**Reason**

> Choosing C over the alternatives depends on the precise region map: sequence hydrophobicity is informative, but does not uniquely determine the marginal span or small boundary differences among the choices.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The supplied reference annotation supports C as the matching option. Transmembrane boundaries can vary between prediction methods, but no other listed choice matches the cited annotation.


### Important caveats

- The supporting UniProt transmembrane annotations are computational, not established here by direct experimental topology measurements.
- The reviewer-only accession and annotations were not available to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has many hydrophobic stretches, which makes a multi-pass membrane protein plausible and supports several candidate regions. But that general signal does not robustly establish the complete set of spans or their exact boundaries, especially for the less clearly hydrophobic 77..97 interval.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The sequence-specific transmembrane-region annotation, including its predicted intervals and boundary conventions, is absent from the prompt.",
    "reason": "Choosing C over the alternatives depends on the precise region map: sequence hydrophobicity is informative, but does not uniquely determine the marginal span or small boundary differences among the choices."
  },
  "case_id": "transmembrane_0100",
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
      "C13",
      "C14",
      "H4",
      "H5",
      "H6",
      "H7",
      "H8",
      "H9",
      "H10",
      "H11",
      "H12",
      "H13"
    ],
    "judgment": "supported",
    "reason": "Choice C matches the transmembrane intervals annotated for the exact matching sequence in both the current UniProt record and a historical snapshot. These annotations carry ECO:0000255, indicating computational evidence; they support the key as an annotation-based answer, not as direct experimental confirmation."
  },
  "important_caveats": [
    "The supporting UniProt transmembrane annotations are computational, not established here by direct experimental topology measurements.",
    "The reviewer-only accession and annotations were not available to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied reference annotation supports C as the matching option. Transmembrane boundaries can vary between prediction methods, but no other listed choice matches the cited annotation."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0100",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "Choice C matches the transmembrane intervals annotated for the exact matching sequence in both the current UniProt record and a historical snapshot. These annotations carry ECO:0000255, indicating computational evidence; they support the key as an annotation-based answer, not as direct experimental confirmation.",
    "evidence_ids": ["C5", "C6", "C7", "C8", "C9", "C10", "C11", "C12", "C13", "C14", "H4", "H5", "H6", "H7", "H8", "H9", "H10", "H11", "H12", "H13"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence has many hydrophobic stretches, which makes a multi-pass membrane protein plausible and supports several candidate regions. But that general signal does not robustly establish the complete set of spans or their exact boundaries, especially for the less clearly hydrophobic 77..97 interval.",
    "missing_item_specific_fact": "The sequence-specific transmembrane-region annotation, including its predicted intervals and boundary conventions, is absent from the prompt.",
    "reason": "Choosing C over the alternatives depends on the precise region map: sequence hydrophobicity is informative, but does not uniquely determine the marginal span or small boundary differences among the choices."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied reference annotation supports C as the matching option. Transmembrane boundaries can vary between prediction methods, but no other listed choice matches the cited annotation."
  },
  "important_caveats": [
    "The supporting UniProt transmembrane annotations are computational, not established here by direct experimental topology measurements.",
    "The reviewer-only accession and annotations were not available to the evaluated model."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry Q6M0N8 (Prepilin peptidase EppA, 346 AA) annotates exactly ten transmembrane helical regions at positions 1..21, 31..51, 56..76, 77..97, 101..121, 128..148, 149..169, 182..202, 206..226, and 321..341, matching Choice C precisely. The sequence SHA256 matches the benchmark input. All annotations carry evidence code ECO:0000255 (by similarity), i.e., computational inference from homologous proteins rather than direct experimental determination.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [C9](#evidence-c9), [C10](#evidence-c10), [C11](#evidence-c11), [C12](#evidence-c12), [C13](#evidence-c13), [C14](#evidence-c14), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6), [H7](#evidence-h7), [H8](#evidence-h8), [H9](#evidence-h9), [H10](#evidence-h10), [H11](#evidence-h11), [H12](#evidence-h12), [H13](#evidence-h13).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> Choice A is trivially eliminated (positions 357–639 exceed the 346-residue protein). Most TM regions (1..21, 31..51, 101..121, 182..202, 321..341) are clearly hydrophobic and identifiable by general hydropathy reasoning. However, the two critical distinctions—(i) whether 77..97 (GDVKMFTALSPLFAAETIYFV) qualifies as a TM helix, and (ii) whether the second helix starts at 31 or 33—cannot be reliably resolved by hydrophobicity analysis. Region 77..97 contains three charged residues (D78, K80, E91), a proline (P86), and only ~67% hydrophobic residues, making it a borderline/non-canonical TM segment that a careful hydropathy scan would likely exclude.


**Missing item-specific fact**

> The specific UniProt 'by similarity' annotation that designates 77..97 as a transmembrane helix and fixes the second helix boundary at 31..51 rather than 33..56. No general biological principle or sequence heuristic uniquely determines these exact boundaries for this particular protein.


**Reason**

> A model performing standard hydrophobicity/window analysis would plausibly omit the charged/proline-containing 77..97 segment (favoring D) or shift the second helix boundary (favoring B). The correct answer depends on the item-specific UniProt annotation, not on a reasoning chain derivable from the sequence alone.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "C",
  "D"
]
```

> Choice D (omitting 77..97) is arguably more defensible from pure hydropathy analysis because that region contains charged residues (D, K, E) and a proline, deviating from the typical >80% hydrophobic composition of a TM α-helix. Choice B (33..56 instead of 31..51) is also a plausible boundary variant. Only Choice A is unambiguously wrong. The question wording does not specify a particular prediction algorithm or threshold that would uniquely select C over D.


### Important caveats

- All ten TM annotations carry ECO:0000255 (by similarity), a computational inference, not experimental data. The 'ground truth' is thus a database prediction, not a measured structure.
- The reviewer-only UniProt accession (Q6M0N8) was inferred from dataset metadata and was absent from the evaluated model input; the model sees only the raw 346-aa sequence.
- The 77..97 region's charged/proline content means that a well-reasoned hydrophobicity-based answer (Choice D) could be scientifically defensible even though it disagrees with the similarity-based annotation.
- Entry version 82 (historical) and version 83 (current) both carry identical TM annotations; no annotation drift affects the key.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Choice A is trivially eliminated (positions 357–639 exceed the 346-residue protein). Most TM regions (1..21, 31..51, 101..121, 182..202, 321..341) are clearly hydrophobic and identifiable by general hydropathy reasoning. However, the two critical distinctions—(i) whether 77..97 (GDVKMFTALSPLFAAETIYFV) qualifies as a TM helix, and (ii) whether the second helix starts at 31 or 33—cannot be reliably resolved by hydrophobicity analysis. Region 77..97 contains three charged residues (D78, K80, E91), a proline (P86), and only ~67% hydrophobic residues, making it a borderline/non-canonical TM segment that a careful hydropathy scan would likely exclude.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific UniProt 'by similarity' annotation that designates 77..97 as a transmembrane helix and fixes the second helix boundary at 31..51 rather than 33..56. No general biological principle or sequence heuristic uniquely determines these exact boundaries for this particular protein.",
    "reason": "A model performing standard hydrophobicity/window analysis would plausibly omit the charged/proline-containing 77..97 segment (favoring D) or shift the second helix boundary (favoring B). The correct answer depends on the item-specific UniProt annotation, not on a reasoning chain derivable from the sequence alone."
  },
  "case_id": "transmembrane_0100",
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
      "C13",
      "C14",
      "H4",
      "H5",
      "H6",
      "H7",
      "H8",
      "H9",
      "H10",
      "H11",
      "H12",
      "H13"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry Q6M0N8 (Prepilin peptidase EppA, 346 AA) annotates exactly ten transmembrane helical regions at positions 1..21, 31..51, 56..76, 77..97, 101..121, 128..148, 149..169, 182..202, 206..226, and 321..341, matching Choice C precisely. The sequence SHA256 matches the benchmark input. All annotations carry evidence code ECO:0000255 (by similarity), i.e., computational inference from homologous proteins rather than direct experimental determination."
  },
  "important_caveats": [
    "All ten TM annotations carry ECO:0000255 (by similarity), a computational inference, not experimental data. The 'ground truth' is thus a database prediction, not a measured structure.",
    "The reviewer-only UniProt accession (Q6M0N8) was inferred from dataset metadata and was absent from the evaluated model input; the model sees only the raw 346-aa sequence.",
    "The 77..97 region's charged/proline content means that a well-reasoned hydrophobicity-based answer (Choice D) could be scientifically defensible even though it disagrees with the similarity-based annotation.",
    "Entry version 82 (historical) and version 83 (current) both carry identical TM annotations; no annotation drift affects the key."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "C",
      "D"
    ],
    "reason": "Choice D (omitting 77..97) is arguably more defensible from pure hydropathy analysis because that region contains charged residues (D, K, E) and a proline, deviating from the typical >80% hydrophobic composition of a TM α-helix. Choice B (33..56 instead of 31..51) is also a plausible boundary variant. Only Choice A is unambiguously wrong. The question wording does not specify a particular prediction algorithm or threshold that would uniquely select C over D."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0100",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry Q6M0N8 (Prepilin peptidase EppA, 346 AA) annotates exactly ten transmembrane helical regions at positions 1..21, 31..51, 56..76, 77..97, 101..121, 128..148, 149..169, 182..202, 206..226, and 321..341, matching Choice C precisely. The sequence SHA256 matches the benchmark input. All annotations carry evidence code ECO:0000255 (by similarity), i.e., computational inference from homologous proteins rather than direct experimental determination.",
    "evidence_ids": ["C5","C6","C7","C8","C9","C10","C11","C12","C13","C14","H4","H5","H6","H7","H8","H9","H10","H11","H12","H13"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "Choice A is trivially eliminated (positions 357–639 exceed the 346-residue protein). Most TM regions (1..21, 31..51, 101..121, 182..202, 321..341) are clearly hydrophobic and identifiable by general hydropathy reasoning. However, the two critical distinctions—(i) whether 77..97 (GDVKMFTALSPLFAAETIYFV) qualifies as a TM helix, and (ii) whether the second helix starts at 31 or 33—cannot be reliably resolved by hydrophobicity analysis. Region 77..97 contains three charged residues (D78, K80, E91), a proline (P86), and only ~67% hydrophobic residues, making it a borderline/non-canonical TM segment that a careful hydropathy scan would likely exclude.",
    "missing_item_specific_fact": "The specific UniProt 'by similarity' annotation that designates 77..97 as a transmembrane helix and fixes the second helix boundary at 31..51 rather than 33..56. No general biological principle or sequence heuristic uniquely determines these exact boundaries for this particular protein.",
    "reason": "A model performing standard hydrophobicity/window analysis would plausibly omit the charged/proline-containing 77..97 segment (favoring D) or shift the second helix boundary (favoring B). The correct answer depends on the item-specific UniProt annotation, not on a reasoning chain derivable from the sequence alone."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["C", "D"],
    "reason": "Choice D (omitting 77..97) is arguably more defensible from pure hydropathy analysis because that region contains charged residues (D, K, E) and a proline, deviating from the typical >80% hydrophobic composition of a TM α-helix. Choice B (33..56 instead of 31..51) is also a plausible boundary variant. Only Choice A is unambiguously wrong. The question wording does not specify a particular prediction algorithm or threshold that would uniquely select C over D."
  },
  "important_caveats": [
    "All ten TM annotations carry ECO:0000255 (by similarity), a computational inference, not experimental data. The 'ground truth' is thus a database prediction, not a measured structure.",
    "The reviewer-only UniProt accession (Q6M0N8) was inferred from dataset metadata and was absent from the evaluated model input; the model sees only the raw 346-aa sequence.",
    "The 77..97 region's charged/proline content means that a well-reasoned hydrophobicity-based answer (Choice D) could be scientifically defensible even though it disagrees with the similarity-based annotation.",
    "Entry version 82 (historical) and version 83 (current) both carry identical TM annotations; no annotation drift affects the key."
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

**Accession:** `Q6M0N8` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 82. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6M0N8.json)  
**Locator:** `/features/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:42.105570+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":21},"start":{"modifier":"EXACT","value":1}},"type":"Transmembrane"}
```

Source SHA-256: `7a4af27303c7c5267346a50d5911ef3e3a55003fa5cc3be434c4311406e03db3`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6M0N8.json)  
**Locator:** `/features/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:42.105570+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":51},"start":{"modifier":"EXACT","value":31}},"type":"Transmembrane"}
```

Source SHA-256: `7a4af27303c7c5267346a50d5911ef3e3a55003fa5cc3be434c4311406e03db3`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6M0N8.json)  
**Locator:** `/features/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:42.105570+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":76},"start":{"modifier":"EXACT","value":56}},"type":"Transmembrane"}
```

Source SHA-256: `7a4af27303c7c5267346a50d5911ef3e3a55003fa5cc3be434c4311406e03db3`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6M0N8.json)  
**Locator:** `/features/4`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:42.105570+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":97},"start":{"modifier":"EXACT","value":77}},"type":"Transmembrane"}
```

Source SHA-256: `7a4af27303c7c5267346a50d5911ef3e3a55003fa5cc3be434c4311406e03db3`.

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6M0N8.json)  
**Locator:** `/features/5`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:42.105570+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":121},"start":{"modifier":"EXACT","value":101}},"type":"Transmembrane"}
```

Source SHA-256: `7a4af27303c7c5267346a50d5911ef3e3a55003fa5cc3be434c4311406e03db3`.

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6M0N8.json)  
**Locator:** `/features/6`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:42.105570+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":148},"start":{"modifier":"EXACT","value":128}},"type":"Transmembrane"}
```

Source SHA-256: `7a4af27303c7c5267346a50d5911ef3e3a55003fa5cc3be434c4311406e03db3`.

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6M0N8.json)  
**Locator:** `/features/7`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:42.105570+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":169},"start":{"modifier":"EXACT","value":149}},"type":"Transmembrane"}
```

Source SHA-256: `7a4af27303c7c5267346a50d5911ef3e3a55003fa5cc3be434c4311406e03db3`.

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6M0N8.json)  
**Locator:** `/features/8`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:42.105570+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":202},"start":{"modifier":"EXACT","value":182}},"type":"Transmembrane"}
```

Source SHA-256: `7a4af27303c7c5267346a50d5911ef3e3a55003fa5cc3be434c4311406e03db3`.

### Evidence C13

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6M0N8.json)  
**Locator:** `/features/9`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:42.105570+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":226},"start":{"modifier":"EXACT","value":206}},"type":"Transmembrane"}
```

Source SHA-256: `7a4af27303c7c5267346a50d5911ef3e3a55003fa5cc3be434c4311406e03db3`.

### Evidence C14

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6M0N8.json)  
**Locator:** `/features/10`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:42.105570+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":341},"start":{"modifier":"EXACT","value":321}},"type":"Transmembrane"}
```

Source SHA-256: `7a4af27303c7c5267346a50d5911ef3e3a55003fa5cc3be434c4311406e03db3`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q6M0N8?format=txt&versions=82)  
**Locator:** `lines 87-89`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 82 / 1.  
**Retrieved:** 2026-11-02T04:31:46.039212+00:00.  

```text
FT   TRANSMEM        1..21
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `db360aef5d1ea6667df242a1cc2d0cea06cc60f4f37e16fbd6c154d182306232`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q6M0N8?format=txt&versions=82)  
**Locator:** `lines 90-92`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 82 / 1.  
**Retrieved:** 2026-11-02T04:31:46.039212+00:00.  

```text
FT   TRANSMEM        31..51
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `db360aef5d1ea6667df242a1cc2d0cea06cc60f4f37e16fbd6c154d182306232`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q6M0N8?format=txt&versions=82)  
**Locator:** `lines 93-95`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 82 / 1.  
**Retrieved:** 2026-11-02T04:31:46.039212+00:00.  

```text
FT   TRANSMEM        56..76
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `db360aef5d1ea6667df242a1cc2d0cea06cc60f4f37e16fbd6c154d182306232`.

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q6M0N8?format=txt&versions=82)  
**Locator:** `lines 96-98`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 82 / 1.  
**Retrieved:** 2026-11-02T04:31:46.039212+00:00.  

```text
FT   TRANSMEM        77..97
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `db360aef5d1ea6667df242a1cc2d0cea06cc60f4f37e16fbd6c154d182306232`.

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q6M0N8?format=txt&versions=82)  
**Locator:** `lines 99-101`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 82 / 1.  
**Retrieved:** 2026-11-02T04:31:46.039212+00:00.  

```text
FT   TRANSMEM        101..121
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `db360aef5d1ea6667df242a1cc2d0cea06cc60f4f37e16fbd6c154d182306232`.

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q6M0N8?format=txt&versions=82)  
**Locator:** `lines 102-104`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 82 / 1.  
**Retrieved:** 2026-11-02T04:31:46.039212+00:00.  

```text
FT   TRANSMEM        128..148
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `db360aef5d1ea6667df242a1cc2d0cea06cc60f4f37e16fbd6c154d182306232`.

### Evidence H10

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q6M0N8?format=txt&versions=82)  
**Locator:** `lines 105-107`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 82 / 1.  
**Retrieved:** 2026-11-02T04:31:46.039212+00:00.  

```text
FT   TRANSMEM        149..169
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `db360aef5d1ea6667df242a1cc2d0cea06cc60f4f37e16fbd6c154d182306232`.

### Evidence H11

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q6M0N8?format=txt&versions=82)  
**Locator:** `lines 108-110`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 82 / 1.  
**Retrieved:** 2026-11-02T04:31:46.039212+00:00.  

```text
FT   TRANSMEM        182..202
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `db360aef5d1ea6667df242a1cc2d0cea06cc60f4f37e16fbd6c154d182306232`.

### Evidence H12

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q6M0N8?format=txt&versions=82)  
**Locator:** `lines 111-113`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 82 / 1.  
**Retrieved:** 2026-11-02T04:31:46.039212+00:00.  

```text
FT   TRANSMEM        206..226
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `db360aef5d1ea6667df242a1cc2d0cea06cc60f4f37e16fbd6c154d182306232`.

### Evidence H13

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q6M0N8?format=txt&versions=82)  
**Locator:** `lines 114-116`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 82 / 1.  
**Retrieved:** 2026-11-02T04:31:46.039212+00:00.  

```text
FT   TRANSMEM        321..341
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `db360aef5d1ea6667df242a1cc2d0cea06cc60f4f37e16fbd6c154d182306232`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json), zero-based source row 100. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
