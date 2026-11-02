# transmembrane_0050

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `transmembrane`  
**Author expected answer:** **A** — 39..59; 94..114; 117..137; 148..168; 177..197; 217..237; 365..385; 405..425; 433..453; 461..481; 488..508; 528..548

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MKDSRGKRRCLAFLKGLRLKTDPNLPGAKQKTPFNISRFWLLVIIVIYTATSACIYFDWSAIRNLLLTVGKYKHLNVGDYPDITLSPQYKRINSLYPITLAIHFTMSVFCGFLYDHIGPKFTAIIGQMCNIMSWVFLSIDSTTVDTTFLSFVFLGLGADTAFIPILTISNLYPDASTFILTVVGAAASLSYAVPATLNFICRRYPSTPFPYICYGYIFLILVPCLLVATFLLPLMPFKGLDYYIERDQSRRSGAEGDAHRGRRGDPKMVTSQTNDEVDVEMQPFENAQSEASKGRSGNGSNTPSTRGNTPNGGKQTRGKTTSESNRSSKGEGSAIQGVEEEDQATNSSKGVNEEDSDFHRKSISLFFKVLLSYPSICIIVYFILFNISTVFYGMVTDTYFSYDRSIINIINILMPISCIPCIIFGRFINRYGSAIIIILMNAFSALMHLTALIKHRAAGLVSAFLYMCVTSIYTSQIYCFIQNSFPSVVFGKLLGFASLCGGLFSLLCEKLYDQIVSKDGASIDPTNVVLLLVIAFILMFLPLTVLYFRKYERSIEDLHQEVAMSQSSGRA

[Multiple Choices]
A. 39..59; 94..114; 117..137; 148..168; 177..197; 217..237; 365..385; 405..425; 433..453; 461..481; 488..508; 528..548
B. 9..29; 41..61; 84..104; 118..138; 153..173; 175..195; 202..222; 231..251
C. 41..61; 94..114; 117..137; 148..168; 177..197; 217..237; 365..385; 405..425; 433..453; 461..481; 488..508; 528..548
D. 39..59; 94..114; 117..137; 148..168; 177..197; 217..237; 365..385; 405..425; 433..453; 461..481; 488..508
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

> The sequence exactly matches the historical UniProt record, whose annotations list all 12 transmembrane regions in choice A. These are computationally evidenced annotations (ECO:0000255), not demonstrated here as experimental measurements.

Citations as saved: [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6), [H7](#evidence-h7), [H8](#evidence-h8), [H9](#evidence-h9), [H10](#evidence-h10), [H11](#evidence-h11), [H12](#evidence-h12), [H13](#evidence-h13), [H14](#evidence-h14).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence contains multiple hydrophobic stretches consistent with membrane-spanning helices, and a long non-hydrophobic intervening region supports two membrane-associated clusters. This helps identify likely transmembrane regions generally, but does not determine the precise annotated boundaries.


**Missing item-specific fact**

> The exact protein-specific transmembrane boundaries, especially whether the first segment starts at residue 39 or 41, are not supplied and require an annotation or protein-specific prediction.


**Reason**

> The choices mainly differ by exact region coordinates and inclusion of a final region. Sequence hydrophobicity supports the general pattern but cannot establish the exact boundaries given in the key.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "C"
]
```

> A and C list the same regions except for a two-residue shift in the first segment's start. Both include the same strongly hydrophobic stretch, so the sequence alone does not clearly distinguish those boundary choices.


### Important caveats

- The reviewer-only UniProt evidence supports the key but was not provided to the evaluated model.
- The cited transmembrane features are computationally evidenced annotations, not necessarily experimental determinations.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains multiple hydrophobic stretches consistent with membrane-spanning helices, and a long non-hydrophobic intervening region supports two membrane-associated clusters. This helps identify likely transmembrane regions generally, but does not determine the precise annotated boundaries.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The exact protein-specific transmembrane boundaries, especially whether the first segment starts at residue 39 or 41, are not supplied and require an annotation or protein-specific prediction.",
    "reason": "The choices mainly differ by exact region coordinates and inclusion of a final region. Sequence hydrophobicity supports the general pattern but cannot establish the exact boundaries given in the key."
  },
  "case_id": "transmembrane_0050",
  "expected_answer_check": {
    "evidence_ids": [
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
      "H13",
      "H14"
    ],
    "judgment": "supported",
    "reason": "The sequence exactly matches the historical UniProt record, whose annotations list all 12 transmembrane regions in choice A. These are computationally evidenced annotations (ECO:0000255), not demonstrated here as experimental measurements."
  },
  "important_caveats": [
    "The reviewer-only UniProt evidence supports the key but was not provided to the evaluated model.",
    "The cited transmembrane features are computationally evidenced annotations, not necessarily experimental determinations."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "C"
    ],
    "reason": "A and C list the same regions except for a two-residue shift in the first segment's start. Both include the same strongly hydrophobic stretch, so the sequence alone does not clearly distinguish those boundary choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0050",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence exactly matches the historical UniProt record, whose annotations list all 12 transmembrane regions in choice A. These are computationally evidenced annotations (ECO:0000255), not demonstrated here as experimental measurements.",
    "evidence_ids": ["H3", "H4", "H5", "H6", "H7", "H8", "H9", "H10", "H11", "H12", "H13", "H14"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence contains multiple hydrophobic stretches consistent with membrane-spanning helices, and a long non-hydrophobic intervening region supports two membrane-associated clusters. This helps identify likely transmembrane regions generally, but does not determine the precise annotated boundaries.",
    "missing_item_specific_fact": "The exact protein-specific transmembrane boundaries, especially whether the first segment starts at residue 39 or 41, are not supplied and require an annotation or protein-specific prediction.",
    "reason": "The choices mainly differ by exact region coordinates and inclusion of a final region. Sequence hydrophobicity supports the general pattern but cannot establish the exact boundaries given in the key."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "C"],
    "reason": "A and C list the same regions except for a two-residue shift in the first segment's start. Both include the same strongly hydrophobic stretch, so the sequence alone does not clearly distinguish those boundary choices."
  },
  "important_caveats": [
    "The reviewer-only UniProt evidence supports the key but was not provided to the evaluated model.",
    "The cited transmembrane features are computationally evidenced annotations, not necessarily experimental determinations."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> Choice A lists exactly the 12 transmembrane helical regions annotated in UniProt entry A5K9W3 (Cationic amino acid transporter 8, Plasmodium vivax): 39..59, 94..114, 117..137, 148..168, 177..197, 217..237, 365..385, 405..425, 433..453, 461..481, 488..508, 528..548. All match the database annotations (C5–C16, H3–H14). The sequence SHA256 matches the benchmark input. Note: all annotations carry evidence code ECO:0000255 (inferred by similarity), i.e., computational predictions rather than experimental measurements.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [C9](#evidence-c9), [C10](#evidence-c10), [C11](#evidence-c11), [C12](#evidence-c12), [C13](#evidence-c13), [C14](#evidence-c14), [C15](#evidence-c15), [C16](#evidence-c16), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6), [H7](#evidence-h7), [H8](#evidence-h8), [H9](#evidence-h9), [H10](#evidence-h10), [H11](#evidence-h11), [H12](#evidence-h12), [H13](#evidence-h13), [H14](#evidence-h14).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> A model could identify major hydrophobic stretches and roughly locate 12 TM helices in a 571-residue amino acid transporter. However, the critical distinctions between the choices are: (1) A vs C differ by only 2 residues in the first TM region (39..59 vs 41..61) — both fall within a continuous hydrophobic stretch and no biological principle mandates one boundary over the other; (2) A vs D differ by the presence/absence of the last TM region (528..548) — this hydrophobic segment near the C-terminus could be argued either way; (3) B is clearly wrong (shifted positions). The exact 21-residue boundaries at single-residue precision are algorithm-dependent predictions (ECO:0000255), not experimentally determined.


**Missing item-specific fact**

> The specific boundary assignments made by UniProt's similarity-based prediction pipeline for this protein, particularly whether the first TM helix starts at residue 39 or 41, and whether the C-terminal hydrophobic stretch at 528..548 is classified as a TM helix rather than a peripheral hydrophobic segment.


**Reason**

> The answer requires reproducing exact computational-prediction boundaries to single-residue precision. The A-vs-C distinction (2 residues) is biologically indistinguishable; the A-vs-D distinction depends on how a particular algorithm classifies a marginal hydrophobic segment. General hydrophobicity reasoning can narrow the field but cannot resolve these precise boundary choices without knowing the specific annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "C",
  "D"
]
```

> Choice C differs from A only by 2 residues in the first TM helix (41..61 vs 39..59); both boundaries lie within a continuous hydrophobic stretch and neither is more biologically correct. Choice D omits the last TM region (528..548), which is a hydrophobic segment whose classification as a true TM helix vs. a cytoplasmic hydrophobic patch is debatable. Only B is clearly wrong. The question effectively tests recall of one specific algorithm's boundary calls among several biologically plausible alternatives.


### Important caveats

- All 12 TM annotations carry evidence code ECO:0000255 (inferred by similarity), meaning they are computational predictions, not experimentally validated boundaries.
- The 2-residue boundary differences between choices A and C are within the typical uncertainty of helix-boundary prediction and cannot be resolved by biology.
- The UniProt entry was first public in June 2025; the author's source snapshot is unknown but the sequence has not changed since 2007.
- A model with strong TM-prediction training (e.g., deep learning hydrophobicity models) might approximate the correct regions but would not reliably reproduce exact boundaries to ±1 residue without memorizing the specific annotation.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "A model could identify major hydrophobic stretches and roughly locate 12 TM helices in a 571-residue amino acid transporter. However, the critical distinctions between the choices are: (1) A vs C differ by only 2 residues in the first TM region (39..59 vs 41..61) — both fall within a continuous hydrophobic stretch and no biological principle mandates one boundary over the other; (2) A vs D differ by the presence/absence of the last TM region (528..548) — this hydrophobic segment near the C-terminus could be argued either way; (3) B is clearly wrong (shifted positions). The exact 21-residue boundaries at single-residue precision are algorithm-dependent predictions (ECO:0000255), not experimentally determined.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific boundary assignments made by UniProt's similarity-based prediction pipeline for this protein, particularly whether the first TM helix starts at residue 39 or 41, and whether the C-terminal hydrophobic stretch at 528..548 is classified as a TM helix rather than a peripheral hydrophobic segment.",
    "reason": "The answer requires reproducing exact computational-prediction boundaries to single-residue precision. The A-vs-C distinction (2 residues) is biologically indistinguishable; the A-vs-D distinction depends on how a particular algorithm classifies a marginal hydrophobic segment. General hydrophobicity reasoning can narrow the field but cannot resolve these precise boundary choices without knowing the specific annotation."
  },
  "case_id": "transmembrane_0050",
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
      "C16",
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
      "H13",
      "H14"
    ],
    "judgment": "supported",
    "reason": "Choice A lists exactly the 12 transmembrane helical regions annotated in UniProt entry A5K9W3 (Cationic amino acid transporter 8, Plasmodium vivax): 39..59, 94..114, 117..137, 148..168, 177..197, 217..237, 365..385, 405..425, 433..453, 461..481, 488..508, 528..548. All match the database annotations (C5–C16, H3–H14). The sequence SHA256 matches the benchmark input. Note: all annotations carry evidence code ECO:0000255 (inferred by similarity), i.e., computational predictions rather than experimental measurements."
  },
  "important_caveats": [
    "All 12 TM annotations carry evidence code ECO:0000255 (inferred by similarity), meaning they are computational predictions, not experimentally validated boundaries.",
    "The 2-residue boundary differences between choices A and C are within the typical uncertainty of helix-boundary prediction and cannot be resolved by biology.",
    "The UniProt entry was first public in June 2025; the author's source snapshot is unknown but the sequence has not changed since 2007.",
    "A model with strong TM-prediction training (e.g., deep learning hydrophobicity models) might approximate the correct regions but would not reliably reproduce exact boundaries to ±1 residue without memorizing the specific annotation."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "C",
      "D"
    ],
    "reason": "Choice C differs from A only by 2 residues in the first TM helix (41..61 vs 39..59); both boundaries lie within a continuous hydrophobic stretch and neither is more biologically correct. Choice D omits the last TM region (528..548), which is a hydrophobic segment whose classification as a true TM helix vs. a cytoplasmic hydrophobic patch is debatable. Only B is clearly wrong. The question effectively tests recall of one specific algorithm's boundary calls among several biologically plausible alternatives."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{"case_id":"transmembrane_0050","expected_answer_check":{"judgment":"supported","reason":"Choice A lists exactly the 12 transmembrane helical regions annotated in UniProt entry A5K9W3 (Cationic amino acid transporter 8, Plasmodium vivax): 39..59, 94..114, 117..137, 148..168, 177..197, 217..237, 365..385, 405..425, 433..453, 461..481, 488..508, 528..548. All match the database annotations (C5–C16, H3–H14). The sequence SHA256 matches the benchmark input. Note: all annotations carry evidence code ECO:0000255 (inferred by similarity), i.e., computational predictions rather than experimental measurements.","evidence_ids":["C5","C6","C7","C8","C9","C10","C11","C12","C13","C14","C15","C16","H3","H4","H5","H6","H7","H8","H9","H10","H11","H12","H13","H14"]},"answerability_check":{"judgment":"lookup_or_memorization_dependent","discriminating_biological_argument":"A model could identify major hydrophobic stretches and roughly locate 12 TM helices in a 571-residue amino acid transporter. However, the critical distinctions between the choices are: (1) A vs C differ by only 2 residues in the first TM region (39..59 vs 41..61) — both fall within a continuous hydrophobic stretch and no biological principle mandates one boundary over the other; (2) A vs D differ by the presence/absence of the last TM region (528..548) — this hydrophobic segment near the C-terminus could be argued either way; (3) B is clearly wrong (shifted positions). The exact 21-residue boundaries at single-residue precision are algorithm-dependent predictions (ECO:0000255), not experimentally determined.","missing_item_specific_fact":"The specific boundary assignments made by UniProt's similarity-based prediction pipeline for this protein, particularly whether the first TM helix starts at residue 39 or 41, and whether the C-terminal hydrophobic stretch at 528..548 is classified as a TM helix rather than a peripheral hydrophobic segment.","reason":"The answer requires reproducing exact computational-prediction boundaries to single-residue precision. The A-vs-C distinction (2 residues) is biologically indistinguishable; the A-vs-D distinction depends on how a particular algorithm classifies a marginal hydrophobic segment. General hydrophobicity reasoning can narrow the field but cannot resolve these precise boundary choices without knowing the specific annotation."},"question_ambiguity":{"multiple_defensible_options":["A","C","D"],"reason":"Choice C differs from A only by 2 residues in the first TM helix (41..61 vs 39..59); both boundaries lie within a continuous hydrophobic stretch and neither is more biologically correct. Choice D omits the last TM region (528..548), which is a hydrophobic segment whose classification as a true TM helix vs. a cytoplasmic hydrophobic patch is debatable. Only B is clearly wrong. The question effectively tests recall of one specific algorithm's boundary calls among several biologically plausible alternatives."},"important_caveats":["All 12 TM annotations carry evidence code ECO:0000255 (inferred by similarity), meaning they are computational predictions, not experimentally validated boundaries.","The 2-residue boundary differences between choices A and C are within the typical uncertainty of helix-boundary prediction and cannot be resolved by biology.","The UniProt entry was first public in June 2025; the author's source snapshot is unknown but the sequence has not changed since 2007.","A model with strong TM-prediction training (e.g., deep learning hydrophobicity models) might approximate the correct regions but would not reliably reproduce exact boundaries to ±1 residue without memorizing the specific annotation."]}
```

</details>

## Existing project source checks of Luna’s review

The notes below were prepared for specific claims in the Luna review. They are not independent validation of Qwen’s claims, expert adjudication, or replacement verdicts.

## Project source-check notes

These project-authored, AI-assisted checks assess specific source claims. They are not expert adjudication and do not replace Luna’s saved review or the author key.

No additional case-specific project note was recorded. Citation membership checks do not establish that every scientific argument is correct.

## Reviewer-only source evidence

**Both reviewers received this source evidence separately from the original question. It was not available to the original evaluated model.** Source support and reasoning from the original sequence/choices are distinct assessments.

**Accession:** `A5K9W3` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 70. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A5K9W3.json)  
**Locator:** `/features/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:03.679737+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":59},"start":{"modifier":"EXACT","value":39}},"type":"Transmembrane"}
```

Source SHA-256: `4f0bdab5e9e7326eb9b6a761a41895f5bb4b5b9bae7c92cfc419fe755650b7a7`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A5K9W3.json)  
**Locator:** `/features/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:03.679737+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":114},"start":{"modifier":"EXACT","value":94}},"type":"Transmembrane"}
```

Source SHA-256: `4f0bdab5e9e7326eb9b6a761a41895f5bb4b5b9bae7c92cfc419fe755650b7a7`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A5K9W3.json)  
**Locator:** `/features/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:03.679737+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":137},"start":{"modifier":"EXACT","value":117}},"type":"Transmembrane"}
```

Source SHA-256: `4f0bdab5e9e7326eb9b6a761a41895f5bb4b5b9bae7c92cfc419fe755650b7a7`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A5K9W3.json)  
**Locator:** `/features/4`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:03.679737+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":168},"start":{"modifier":"EXACT","value":148}},"type":"Transmembrane"}
```

Source SHA-256: `4f0bdab5e9e7326eb9b6a761a41895f5bb4b5b9bae7c92cfc419fe755650b7a7`.

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A5K9W3.json)  
**Locator:** `/features/5`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:03.679737+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":197},"start":{"modifier":"EXACT","value":177}},"type":"Transmembrane"}
```

Source SHA-256: `4f0bdab5e9e7326eb9b6a761a41895f5bb4b5b9bae7c92cfc419fe755650b7a7`.

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A5K9W3.json)  
**Locator:** `/features/6`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:03.679737+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":237},"start":{"modifier":"EXACT","value":217}},"type":"Transmembrane"}
```

Source SHA-256: `4f0bdab5e9e7326eb9b6a761a41895f5bb4b5b9bae7c92cfc419fe755650b7a7`.

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A5K9W3.json)  
**Locator:** `/features/7`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:03.679737+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":385},"start":{"modifier":"EXACT","value":365}},"type":"Transmembrane"}
```

Source SHA-256: `4f0bdab5e9e7326eb9b6a761a41895f5bb4b5b9bae7c92cfc419fe755650b7a7`.

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A5K9W3.json)  
**Locator:** `/features/8`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:03.679737+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":425},"start":{"modifier":"EXACT","value":405}},"type":"Transmembrane"}
```

Source SHA-256: `4f0bdab5e9e7326eb9b6a761a41895f5bb4b5b9bae7c92cfc419fe755650b7a7`.

### Evidence C13

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A5K9W3.json)  
**Locator:** `/features/9`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:03.679737+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":453},"start":{"modifier":"EXACT","value":433}},"type":"Transmembrane"}
```

Source SHA-256: `4f0bdab5e9e7326eb9b6a761a41895f5bb4b5b9bae7c92cfc419fe755650b7a7`.

### Evidence C14

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A5K9W3.json)  
**Locator:** `/features/10`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:03.679737+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":481},"start":{"modifier":"EXACT","value":461}},"type":"Transmembrane"}
```

Source SHA-256: `4f0bdab5e9e7326eb9b6a761a41895f5bb4b5b9bae7c92cfc419fe755650b7a7`.

### Evidence C15

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A5K9W3.json)  
**Locator:** `/features/11`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:03.679737+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":508},"start":{"modifier":"EXACT","value":488}},"type":"Transmembrane"}
```

Source SHA-256: `4f0bdab5e9e7326eb9b6a761a41895f5bb4b5b9bae7c92cfc419fe755650b7a7`.

### Evidence C16

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A5K9W3.json)  
**Locator:** `/features/12`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:03.679737+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":548},"start":{"modifier":"EXACT","value":528}},"type":"Transmembrane"}
```

Source SHA-256: `4f0bdab5e9e7326eb9b6a761a41895f5bb4b5b9bae7c92cfc419fe755650b7a7`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A5K9W3?format=txt&versions=70)  
**Locator:** `lines 83-85`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 70 / 1.  
**Retrieved:** 2026-11-02T04:27:11.338974+00:00.  

```text
FT   TRANSMEM        39..59
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `5fa55f18851f98378363667b0094890e54d37ee80e9a4c1b8d3f1f7eec1b9221`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A5K9W3?format=txt&versions=70)  
**Locator:** `lines 86-88`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 70 / 1.  
**Retrieved:** 2026-11-02T04:27:11.338974+00:00.  

```text
FT   TRANSMEM        94..114
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `5fa55f18851f98378363667b0094890e54d37ee80e9a4c1b8d3f1f7eec1b9221`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A5K9W3?format=txt&versions=70)  
**Locator:** `lines 89-91`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 70 / 1.  
**Retrieved:** 2026-11-02T04:27:11.338974+00:00.  

```text
FT   TRANSMEM        117..137
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `5fa55f18851f98378363667b0094890e54d37ee80e9a4c1b8d3f1f7eec1b9221`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A5K9W3?format=txt&versions=70)  
**Locator:** `lines 92-94`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 70 / 1.  
**Retrieved:** 2026-11-02T04:27:11.338974+00:00.  

```text
FT   TRANSMEM        148..168
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `5fa55f18851f98378363667b0094890e54d37ee80e9a4c1b8d3f1f7eec1b9221`.

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A5K9W3?format=txt&versions=70)  
**Locator:** `lines 95-97`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 70 / 1.  
**Retrieved:** 2026-11-02T04:27:11.338974+00:00.  

```text
FT   TRANSMEM        177..197
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `5fa55f18851f98378363667b0094890e54d37ee80e9a4c1b8d3f1f7eec1b9221`.

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A5K9W3?format=txt&versions=70)  
**Locator:** `lines 98-100`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 70 / 1.  
**Retrieved:** 2026-11-02T04:27:11.338974+00:00.  

```text
FT   TRANSMEM        217..237
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `5fa55f18851f98378363667b0094890e54d37ee80e9a4c1b8d3f1f7eec1b9221`.

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A5K9W3?format=txt&versions=70)  
**Locator:** `lines 101-103`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 70 / 1.  
**Retrieved:** 2026-11-02T04:27:11.338974+00:00.  

```text
FT   TRANSMEM        365..385
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `5fa55f18851f98378363667b0094890e54d37ee80e9a4c1b8d3f1f7eec1b9221`.

### Evidence H10

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A5K9W3?format=txt&versions=70)  
**Locator:** `lines 104-106`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 70 / 1.  
**Retrieved:** 2026-11-02T04:27:11.338974+00:00.  

```text
FT   TRANSMEM        405..425
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `5fa55f18851f98378363667b0094890e54d37ee80e9a4c1b8d3f1f7eec1b9221`.

### Evidence H11

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A5K9W3?format=txt&versions=70)  
**Locator:** `lines 107-109`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 70 / 1.  
**Retrieved:** 2026-11-02T04:27:11.338974+00:00.  

```text
FT   TRANSMEM        433..453
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `5fa55f18851f98378363667b0094890e54d37ee80e9a4c1b8d3f1f7eec1b9221`.

### Evidence H12

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A5K9W3?format=txt&versions=70)  
**Locator:** `lines 110-112`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 70 / 1.  
**Retrieved:** 2026-11-02T04:27:11.338974+00:00.  

```text
FT   TRANSMEM        461..481
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `5fa55f18851f98378363667b0094890e54d37ee80e9a4c1b8d3f1f7eec1b9221`.

### Evidence H13

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A5K9W3?format=txt&versions=70)  
**Locator:** `lines 113-115`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 70 / 1.  
**Retrieved:** 2026-11-02T04:27:11.338974+00:00.  

```text
FT   TRANSMEM        488..508
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `5fa55f18851f98378363667b0094890e54d37ee80e9a4c1b8d3f1f7eec1b9221`.

### Evidence H14

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A5K9W3?format=txt&versions=70)  
**Locator:** `lines 116-118`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 70 / 1.  
**Retrieved:** 2026-11-02T04:27:11.338974+00:00.  

```text
FT   TRANSMEM        528..548
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `5fa55f18851f98378363667b0094890e54d37ee80e9a4c1b8d3f1f7eec1b9221`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json), zero-based source row 50. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
