# transmembrane_0023

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `transmembrane`  
**Author expected answer:** **C** — 41..64; 76..96; 108..126; 132..156; 176..195; 201..220; 241..260; 280..300; 312..330; 346..366; 416..437

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MIEKSNNIYLSIDPIVERIKKNGEELPLINSEKKGIDYTQIVVYLVGLSDGLIHLASLAIYYLFKDHYRLTPYQVSLILMYPYLPFILKPIIALITDSISIFGMRRKPYLFLFSLFQSLNFLSLALVDLSLIQATLVLFFISLCASFCTTVAEALVVESSIGKTYSQGTNKVTEFIASKAVGSLSVAYFSGYFLEKVSREYIFMATSIFPLIISISCLFLKEKEYVTRKNIFKQMTDLIKFINTPVFIGPFLYIFVYMSGPDYDDAFFFFCTNKLGFRPSFMGTLRLTYGIASLIGIIVYRVFLKNSSLRNTLIFTTLVSFPIYISPIILTEKINKYFGISNELFVLSGGFLIEAITEIQLLPLFILTANICQEGLEASVFATILSVKNLGSLTKKGTSSLLTYLMKIDTYNFDNLSMYILTCGLFLLLSLSLVPLLPSEDQIESLKNKKIQK

[Multiple Choices]
A. 41..64; 108..126; 132..156; 176..195; 201..220; 241..260; 280..300; 312..330; 346..366; 416..437
B. 41..64; 76..96; 108..126; 132..156; 176..195; 201..220; 241..260; 284..304; 312..330; 346..366; 416..437
C. 41..64; 76..96; 108..126; 132..156; 176..195; 201..220; 241..260; 280..300; 312..330; 346..366; 416..437
D. 1..21; 31..51; 56..76; 77..97; 101..121; 128..148; 149..169; 182..202; 206..226; 321..341
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

> The exact sequence matches the referenced UniProt record, whose current and historical entries annotate the transmembrane regions listed in C, including 280..300. These are computational annotations (ECO:0000255), not evidence of experimental determination of the exact boundaries.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [C9](#evidence-c9), [C10](#evidence-c10), [C11](#evidence-c11), [C12](#evidence-c12), [C13](#evidence-c13), [C14](#evidence-c14), [C15](#evidence-c15), [H10](#evidence-h10).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence has many strongly hydrophobic stretches, supporting a multipass membrane-protein interpretation, but general sequence reasoning does not reliably distinguish the nearly identical 280..300 and 284..304 boundaries.


**Missing item-specific fact**

> The exact annotated or otherwise established boundaries for this particular protein, especially whether the region is recorded as 280..300 or 284..304.


**Reason**

> The sequence supports broad transmembrane-helix prediction, but choosing C over B depends on protein-specific boundary information absent from the input; the database evidence is reviewer-only.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "C"
]
```

> B and C differ only in the placement of one candidate helix by four residues. Both windows overlap the same hydrophobic region, and the input gives no boundary convention or experimental result that resolves the offset.


### Important caveats

- The supporting UniProt transmembrane annotations are computational, not independently verified experimental measurements.
- The historical entry also matches the sequence, but the author's exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has many strongly hydrophobic stretches, supporting a multipass membrane-protein interpretation, but general sequence reasoning does not reliably distinguish the nearly identical 280..300 and 284..304 boundaries.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The exact annotated or otherwise established boundaries for this particular protein, especially whether the region is recorded as 280..300 or 284..304.",
    "reason": "The sequence supports broad transmembrane-helix prediction, but choosing C over B depends on protein-specific boundary information absent from the input; the database evidence is reviewer-only."
  },
  "case_id": "transmembrane_0023",
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
      "C15",
      "H10"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the referenced UniProt record, whose current and historical entries annotate the transmembrane regions listed in C, including 280..300. These are computational annotations (ECO:0000255), not evidence of experimental determination of the exact boundaries."
  },
  "important_caveats": [
    "The supporting UniProt transmembrane annotations are computational, not independently verified experimental measurements.",
    "The historical entry also matches the sequence, but the author's exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "C"
    ],
    "reason": "B and C differ only in the placement of one candidate helix by four residues. Both windows overlap the same hydrophobic region, and the input gives no boundary convention or experimental result that resolves the offset."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0023",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the referenced UniProt record, whose current and historical entries annotate the transmembrane regions listed in C, including 280..300. These are computational annotations (ECO:0000255), not evidence of experimental determination of the exact boundaries.",
    "evidence_ids": ["C5", "C6", "C7", "C8", "C9", "C10", "C11", "C12", "C13", "C14", "C15", "H10"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence has many strongly hydrophobic stretches, supporting a multipass membrane-protein interpretation, but general sequence reasoning does not reliably distinguish the nearly identical 280..300 and 284..304 boundaries.",
    "missing_item_specific_fact": "The exact annotated or otherwise established boundaries for this particular protein, especially whether the region is recorded as 280..300 or 284..304.",
    "reason": "The sequence supports broad transmembrane-helix prediction, but choosing C over B depends on protein-specific boundary information absent from the input; the database evidence is reviewer-only."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "C"],
    "reason": "B and C differ only in the placement of one candidate helix by four residues. Both windows overlap the same hydrophobic region, and the input gives no boundary convention or experimental result that resolves the offset."
  },
  "important_caveats": [
    "The supporting UniProt transmembrane annotations are computational, not independently verified experimental measurements.",
    "The historical entry also matches the sequence, but the author's exact source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt annotation for A0A509AM18 (FT2_PLABA, Plasmodium berghei folate transporter 2) lists exactly 11 transmembrane helical regions at 41..64, 76..96, 108..126, 132..156, 176..195, 201..220, 241..260, 280..300, 312..330, 346..366, and 416..437, which matches Choice C precisely. The sequence in the question matches the UniProt entry (453 AA, SHA256 confirmed). However, all TM annotations carry evidence code ECO:0000255 (similarity-based computational prediction), not experimental determination.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [C9](#evidence-c9), [C10](#evidence-c10), [C11](#evidence-c11), [C12](#evidence-c12), [C13](#evidence-c13), [C14](#evidence-c14), [C15](#evidence-c15), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6), [H7](#evidence-h7), [H8](#evidence-h8), [H9](#evidence-h9), [H10](#evidence-h10), [H11](#evidence-h11), [H12](#evidence-h12), [H13](#evidence-h13).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> Choice D can be eliminated by general reasoning: TM helices do not typically begin at residue 1 of a protein, and the perfectly regular 20-residue sliding-window spacing is biologically unrealistic. Choice A omits the 76..96 region (SLILMYPYLPFILKPIIALIT), which has moderate hydrophobic character and could be argued as TM. However, the critical B-vs-C distinction (284..304 vs 280..300 for the eighth TM region) is a 4-residue boundary shift that cannot be resolved by general hydrophobicity reasoning—both windows contain similar borderline residues (S/T at start, Y/L at end, R at position 286 in both).


**Missing item-specific fact**

> The exact boundary assignment for the eighth TM region (280..300 vs 284..304) depends on the specific computational prediction algorithm and its scoring thresholds used by the annotator. No general biological principle distinguishes a 21-residue helix starting at S(280) ending at Y(300) from a 21-residue helix starting at T(284) ending at L(304) for this particular sequence.


**Reason**

> While D is eliminable by reasoning and A is debatable, the decisive B-vs-C choice requires knowledge of the exact annotation boundaries produced by a specific prediction tool. The 4-residue shift in the eighth TM region is within the noise of hydrophobicity-based predictions and cannot be resolved by general biological knowledge alone.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "C"
]
```

> The only difference between B and C is the eighth TM region (284..304 vs 280..300). Both windows span 21 residues and contain similar residue compositions (polar/borderline at boundaries, hydrophobic core, one arginine at position 286). Without the exact prediction tool output, a knowledgeable biologist could reasonably assign either boundary. The sequence region 280-304 is: S(280)F(281)M(282)G(283)T(284)L(285)R(286)L(287)T(288)Y(289)G(290)I(291)A(292)S(293)L(294)I(295)G(296)I(297)I(298)V(299)Y(300)R(301)V(302)F(303)L(304) — the hydrophobicity profile does not clearly favor one boundary over the other.


### Important caveats

- All TM annotations carry ECO:0000255 (similarity-based prediction), meaning these are computational inferences, not experimentally validated membrane-spanning regions.
- The protein is annotated as a 'Putative' folate transporter with 'Apicoplast-resident' localization from a 2021 study, but the TM topology itself is predicted, not experimentally determined.
- The question presents multiple complete TM topologies as options, making it a whole-set matching task rather than a single-region identification, which increases sensitivity to boundary precision.
- The identity of this protein (A0A509AM18) was not provided to the evaluated model; it was inferred by the reviewer from dataset metadata.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Choice D can be eliminated by general reasoning: TM helices do not typically begin at residue 1 of a protein, and the perfectly regular 20-residue sliding-window spacing is biologically unrealistic. Choice A omits the 76..96 region (SLILMYPYLPFILKPIIALIT), which has moderate hydrophobic character and could be argued as TM. However, the critical B-vs-C distinction (284..304 vs 280..300 for the eighth TM region) is a 4-residue boundary shift that cannot be resolved by general hydrophobicity reasoning—both windows contain similar borderline residues (S/T at start, Y/L at end, R at position 286 in both).",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The exact boundary assignment for the eighth TM region (280..300 vs 284..304) depends on the specific computational prediction algorithm and its scoring thresholds used by the annotator. No general biological principle distinguishes a 21-residue helix starting at S(280) ending at Y(300) from a 21-residue helix starting at T(284) ending at L(304) for this particular sequence.",
    "reason": "While D is eliminable by reasoning and A is debatable, the decisive B-vs-C choice requires knowledge of the exact annotation boundaries produced by a specific prediction tool. The 4-residue shift in the eighth TM region is within the noise of hydrophobicity-based predictions and cannot be resolved by general biological knowledge alone."
  },
  "case_id": "transmembrane_0023",
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
      "C15",
      "H3",
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
    "reason": "The UniProt annotation for A0A509AM18 (FT2_PLABA, Plasmodium berghei folate transporter 2) lists exactly 11 transmembrane helical regions at 41..64, 76..96, 108..126, 132..156, 176..195, 201..220, 241..260, 280..300, 312..330, 346..366, and 416..437, which matches Choice C precisely. The sequence in the question matches the UniProt entry (453 AA, SHA256 confirmed). However, all TM annotations carry evidence code ECO:0000255 (similarity-based computational prediction), not experimental determination."
  },
  "important_caveats": [
    "All TM annotations carry ECO:0000255 (similarity-based prediction), meaning these are computational inferences, not experimentally validated membrane-spanning regions.",
    "The protein is annotated as a 'Putative' folate transporter with 'Apicoplast-resident' localization from a 2021 study, but the TM topology itself is predicted, not experimentally determined.",
    "The question presents multiple complete TM topologies as options, making it a whole-set matching task rather than a single-region identification, which increases sensitivity to boundary precision.",
    "The identity of this protein (A0A509AM18) was not provided to the evaluated model; it was inferred by the reviewer from dataset metadata."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "C"
    ],
    "reason": "The only difference between B and C is the eighth TM region (284..304 vs 280..300). Both windows span 21 residues and contain similar residue compositions (polar/borderline at boundaries, hydrophobic core, one arginine at position 286). Without the exact prediction tool output, a knowledgeable biologist could reasonably assign either boundary. The sequence region 280-304 is: S(280)F(281)M(282)G(283)T(284)L(285)R(286)L(287)T(288)Y(289)G(290)I(291)A(292)S(293)L(294)I(295)G(296)I(297)I(298)V(299)Y(300)R(301)V(302)F(303)L(304) — the hydrophobicity profile does not clearly favor one boundary over the other."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0023",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt annotation for A0A509AM18 (FT2_PLABA, Plasmodium berghei folate transporter 2) lists exactly 11 transmembrane helical regions at 41..64, 76..96, 108..126, 132..156, 176..195, 201..220, 241..260, 280..300, 312..330, 346..366, and 416..437, which matches Choice C precisely. The sequence in the question matches the UniProt entry (453 AA, SHA256 confirmed). However, all TM annotations carry evidence code ECO:0000255 (similarity-based computational prediction), not experimental determination.",
    "evidence_ids": ["C5","C6","C7","C8","C9","C10","C11","C12","C13","C14","C15","H3","H4","H5","H6","H7","H8","H9","H10","H11","H12","H13"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "Choice D can be eliminated by general reasoning: TM helices do not typically begin at residue 1 of a protein, and the perfectly regular 20-residue sliding-window spacing is biologically unrealistic. Choice A omits the 76..96 region (SLILMYPYLPFILKPIIALIT), which has moderate hydrophobic character and could be argued as TM. However, the critical B-vs-C distinction (284..304 vs 280..300 for the eighth TM region) is a 4-residue boundary shift that cannot be resolved by general hydrophobicity reasoning—both windows contain similar borderline residues (S/T at start, Y/L at end, R at position 286 in both).",
    "missing_item_specific_fact": "The exact boundary assignment for the eighth TM region (280..300 vs 284..304) depends on the specific computational prediction algorithm and its scoring thresholds used by the annotator. No general biological principle distinguishes a 21-residue helix starting at S(280) ending at Y(300) from a 21-residue helix starting at T(284) ending at L(304) for this particular sequence.",
    "reason": "While D is eliminable by reasoning and A is debatable, the decisive B-vs-C choice requires knowledge of the exact annotation boundaries produced by a specific prediction tool. The 4-residue shift in the eighth TM region is within the noise of hydrophobicity-based predictions and cannot be resolved by general biological knowledge alone."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "C"],
    "reason": "The only difference between B and C is the eighth TM region (284..304 vs 280..300). Both windows span 21 residues and contain similar residue compositions (polar/borderline at boundaries, hydrophobic core, one arginine at position 286). Without the exact prediction tool output, a knowledgeable biologist could reasonably assign either boundary. The sequence region 280-304 is: S(280)F(281)M(282)G(283)T(284)L(285)R(286)L(287)T(288)Y(289)G(290)I(291)A(292)S(293)L(294)I(295)G(296)I(297)I(298)V(299)Y(300)R(301)V(302)F(303)L(304) — the hydrophobicity profile does not clearly favor one boundary over the other."
  },
  "important_caveats": [
    "All TM annotations carry ECO:0000255 (similarity-based prediction), meaning these are computational inferences, not experimentally validated membrane-spanning regions.",
    "The protein is annotated as a 'Putative' folate transporter with 'Apicoplast-resident' localization from a 2021 study, but the TM topology itself is predicted, not experimentally determined.",
    "The question presents multiple complete TM topologies as options, making it a whole-set matching task rather than a single-region identification, which increases sensitivity to boundary precision.",
    "The identity of this protein (A0A509AM18) was not provided to the evaluated model; it was inferred by the reviewer from dataset metadata."
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

**Accession:** `A0A509AM18` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 20. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A509AM18.json)  
**Locator:** `/features/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:24.632626+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":64},"start":{"modifier":"EXACT","value":41}},"type":"Transmembrane"}
```

Source SHA-256: `f983917de53c311063e3ec0dde4869d4a7e4fd767ac8b680a2f2cb01fe9b92e9`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A509AM18.json)  
**Locator:** `/features/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:24.632626+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":96},"start":{"modifier":"EXACT","value":76}},"type":"Transmembrane"}
```

Source SHA-256: `f983917de53c311063e3ec0dde4869d4a7e4fd767ac8b680a2f2cb01fe9b92e9`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A509AM18.json)  
**Locator:** `/features/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:24.632626+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":126},"start":{"modifier":"EXACT","value":108}},"type":"Transmembrane"}
```

Source SHA-256: `f983917de53c311063e3ec0dde4869d4a7e4fd767ac8b680a2f2cb01fe9b92e9`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A509AM18.json)  
**Locator:** `/features/4`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:24.632626+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":156},"start":{"modifier":"EXACT","value":132}},"type":"Transmembrane"}
```

Source SHA-256: `f983917de53c311063e3ec0dde4869d4a7e4fd767ac8b680a2f2cb01fe9b92e9`.

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A509AM18.json)  
**Locator:** `/features/5`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:24.632626+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":195},"start":{"modifier":"EXACT","value":176}},"type":"Transmembrane"}
```

Source SHA-256: `f983917de53c311063e3ec0dde4869d4a7e4fd767ac8b680a2f2cb01fe9b92e9`.

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A509AM18.json)  
**Locator:** `/features/6`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:24.632626+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":220},"start":{"modifier":"EXACT","value":201}},"type":"Transmembrane"}
```

Source SHA-256: `f983917de53c311063e3ec0dde4869d4a7e4fd767ac8b680a2f2cb01fe9b92e9`.

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A509AM18.json)  
**Locator:** `/features/7`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:24.632626+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":260},"start":{"modifier":"EXACT","value":241}},"type":"Transmembrane"}
```

Source SHA-256: `f983917de53c311063e3ec0dde4869d4a7e4fd767ac8b680a2f2cb01fe9b92e9`.

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A509AM18.json)  
**Locator:** `/features/8`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:24.632626+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":300},"start":{"modifier":"EXACT","value":280}},"type":"Transmembrane"}
```

Source SHA-256: `f983917de53c311063e3ec0dde4869d4a7e4fd767ac8b680a2f2cb01fe9b92e9`.

### Evidence C13

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A509AM18.json)  
**Locator:** `/features/9`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:24.632626+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":330},"start":{"modifier":"EXACT","value":312}},"type":"Transmembrane"}
```

Source SHA-256: `f983917de53c311063e3ec0dde4869d4a7e4fd767ac8b680a2f2cb01fe9b92e9`.

### Evidence C14

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A509AM18.json)  
**Locator:** `/features/10`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:24.632626+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":366},"start":{"modifier":"EXACT","value":346}},"type":"Transmembrane"}
```

Source SHA-256: `f983917de53c311063e3ec0dde4869d4a7e4fd767ac8b680a2f2cb01fe9b92e9`.

### Evidence C15

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A509AM18.json)  
**Locator:** `/features/11`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:24.632626+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":437},"start":{"modifier":"EXACT","value":416}},"type":"Transmembrane"}
```

Source SHA-256: `f983917de53c311063e3ec0dde4869d4a7e4fd767ac8b680a2f2cb01fe9b92e9`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A509AM18?format=txt&versions=20)  
**Locator:** `lines 89-91`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 20 / 1.  
**Retrieved:** 2026-11-02T04:25:29.319637+00:00.  

```text
FT   TRANSMEM        41..64
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `52278aa5726b2473aad0488c2c3da3b14115e3dd0f2c2903d4b27b3d1cb87749`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A509AM18?format=txt&versions=20)  
**Locator:** `lines 92-94`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 20 / 1.  
**Retrieved:** 2026-11-02T04:25:29.319637+00:00.  

```text
FT   TRANSMEM        76..96
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `52278aa5726b2473aad0488c2c3da3b14115e3dd0f2c2903d4b27b3d1cb87749`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A509AM18?format=txt&versions=20)  
**Locator:** `lines 95-97`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 20 / 1.  
**Retrieved:** 2026-11-02T04:25:29.319637+00:00.  

```text
FT   TRANSMEM        108..126
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `52278aa5726b2473aad0488c2c3da3b14115e3dd0f2c2903d4b27b3d1cb87749`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A509AM18?format=txt&versions=20)  
**Locator:** `lines 98-100`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 20 / 1.  
**Retrieved:** 2026-11-02T04:25:29.319637+00:00.  

```text
FT   TRANSMEM        132..156
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `52278aa5726b2473aad0488c2c3da3b14115e3dd0f2c2903d4b27b3d1cb87749`.

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A509AM18?format=txt&versions=20)  
**Locator:** `lines 101-103`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 20 / 1.  
**Retrieved:** 2026-11-02T04:25:29.319637+00:00.  

```text
FT   TRANSMEM        176..195
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `52278aa5726b2473aad0488c2c3da3b14115e3dd0f2c2903d4b27b3d1cb87749`.

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A509AM18?format=txt&versions=20)  
**Locator:** `lines 104-106`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 20 / 1.  
**Retrieved:** 2026-11-02T04:25:29.319637+00:00.  

```text
FT   TRANSMEM        201..220
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `52278aa5726b2473aad0488c2c3da3b14115e3dd0f2c2903d4b27b3d1cb87749`.

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A509AM18?format=txt&versions=20)  
**Locator:** `lines 107-109`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 20 / 1.  
**Retrieved:** 2026-11-02T04:25:29.319637+00:00.  

```text
FT   TRANSMEM        241..260
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `52278aa5726b2473aad0488c2c3da3b14115e3dd0f2c2903d4b27b3d1cb87749`.

### Evidence H10

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A509AM18?format=txt&versions=20)  
**Locator:** `lines 110-112`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 20 / 1.  
**Retrieved:** 2026-11-02T04:25:29.319637+00:00.  

```text
FT   TRANSMEM        280..300
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `52278aa5726b2473aad0488c2c3da3b14115e3dd0f2c2903d4b27b3d1cb87749`.

### Evidence H11

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A509AM18?format=txt&versions=20)  
**Locator:** `lines 113-115`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 20 / 1.  
**Retrieved:** 2026-11-02T04:25:29.319637+00:00.  

```text
FT   TRANSMEM        312..330
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `52278aa5726b2473aad0488c2c3da3b14115e3dd0f2c2903d4b27b3d1cb87749`.

### Evidence H12

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A509AM18?format=txt&versions=20)  
**Locator:** `lines 116-118`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 20 / 1.  
**Retrieved:** 2026-11-02T04:25:29.319637+00:00.  

```text
FT   TRANSMEM        346..366
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `52278aa5726b2473aad0488c2c3da3b14115e3dd0f2c2903d4b27b3d1cb87749`.

### Evidence H13

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A509AM18?format=txt&versions=20)  
**Locator:** `lines 119-121`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 20 / 1.  
**Retrieved:** 2026-11-02T04:25:29.319637+00:00.  

```text
FT   TRANSMEM        416..437
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `52278aa5726b2473aad0488c2c3da3b14115e3dd0f2c2903d4b27b3d1cb87749`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json), zero-based source row 23. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
