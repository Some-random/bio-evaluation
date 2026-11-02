# transmembrane_0071

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `transmembrane`  
**Author expected answer:** **A** — 38..58; 73..93; 124..144; 156..176; 182..202; 244..264

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MTTLDLTARSDRGRVYWLLADCWNIVRRGLTHYQRQPVNIAWQLGFPILSVLLYGYVFGSAMKVPGGGDYKDFLMPGMFVMTMAFGFINTATLVVYDSTKGVIDRFRSMPMASSAVVAGRGVTDLITACAELAIMMLTAFAMGWRPDGGLGFLGAFGLLLWLRFALIWIGVWLGLLVPNPEAAGGLFAVAFPLTMISSIMVAPQLMPDWLGWVAMWNPISSTAAATRELFGTPVGGDTWVEQHALLMAGVWPVILTLVFLPLAVRRFKKLSR

[Multiple Choices]
A. 38..58; 73..93; 124..144; 156..176; 182..202; 244..264
B. 38..58; 73..93; 123..147; 156..176; 182..202; 244..264
C. 35..55
D. 38..58; 73..93; 124..144; 156..176; 244..264
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

> The sequence-matched historical UniProt record annotates all six transmembrane intervals listed in A. The annotations carry ECO:0000255, indicating computational evidence; they support the key as an annotation, not as direct experimental confirmation.

Citations as saved: [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6), [H7](#evidence-h7), [H8](#evidence-h8).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence contains several hydrophobic stretches consistent with membrane-spanning helices, so general sequence reasoning can suggest a multi-pass membrane protein. It does not robustly determine the exact boundaries or the annotated count needed to distinguish these choices.


**Missing item-specific fact**

> The protein-specific transmembrane annotation with its interval boundaries, particularly the exact limits of the 123/124..144/147 region and whether 182..202 is included.


**Reason**

> The sequence supports broad hydrophobic-helix predictions, but selecting the exact annotated intervals in A requires protein-specific boundary information absent from the question.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Against the supplied historical annotation, A uniquely lists all six annotated intervals; the alternatives omit an interval or alter a boundary.


### Important caveats

- The reviewer-only source identifies the matching protein as DrrB2 and provides the interval annotations, but that identification and annotation were not supplied to the evaluated model.
- The intervals are computational annotations, not established here by independent experimental mapping; transmembrane boundaries can depend on the prediction or annotation method.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains several hydrophobic stretches consistent with membrane-spanning helices, so general sequence reasoning can suggest a multi-pass membrane protein. It does not robustly determine the exact boundaries or the annotated count needed to distinguish these choices.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific transmembrane annotation with its interval boundaries, particularly the exact limits of the 123/124..144/147 region and whether 182..202 is included.",
    "reason": "The sequence supports broad hydrophobic-helix predictions, but selecting the exact annotated intervals in A requires protein-specific boundary information absent from the question."
  },
  "case_id": "transmembrane_0071",
  "expected_answer_check": {
    "evidence_ids": [
      "H3",
      "H4",
      "H5",
      "H6",
      "H7",
      "H8"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched historical UniProt record annotates all six transmembrane intervals listed in A. The annotations carry ECO:0000255, indicating computational evidence; they support the key as an annotation, not as direct experimental confirmation."
  },
  "important_caveats": [
    "The reviewer-only source identifies the matching protein as DrrB2 and provides the interval annotations, but that identification and annotation were not supplied to the evaluated model.",
    "The intervals are computational annotations, not established here by independent experimental mapping; transmembrane boundaries can depend on the prediction or annotation method."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Against the supplied historical annotation, A uniquely lists all six annotated intervals; the alternatives omit an interval or alter a boundary."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0071",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched historical UniProt record annotates all six transmembrane intervals listed in A. The annotations carry ECO:0000255, indicating computational evidence; they support the key as an annotation, not as direct experimental confirmation.",
    "evidence_ids": ["H3", "H4", "H5", "H6", "H7", "H8"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence contains several hydrophobic stretches consistent with membrane-spanning helices, so general sequence reasoning can suggest a multi-pass membrane protein. It does not robustly determine the exact boundaries or the annotated count needed to distinguish these choices.",
    "missing_item_specific_fact": "The protein-specific transmembrane annotation with its interval boundaries, particularly the exact limits of the 123/124..144/147 region and whether 182..202 is included.",
    "reason": "The sequence supports broad hydrophobic-helix predictions, but selecting the exact annotated intervals in A requires protein-specific boundary information absent from the question."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Against the supplied historical annotation, A uniquely lists all six annotated intervals; the alternatives omit an interval or alter a boundary."
  },
  "important_caveats": [
    "The reviewer-only source identifies the matching protein as DrrB2 and provides the interval annotations, but that identification and annotation were not supplied to the evaluated model.",
    "The intervals are computational annotations, not established here by independent experimental mapping; transmembrane boundaries can depend on the prediction or annotation method."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> Choice A (38..58; 73..93; 124..144; 156..176; 182..202; 244..264) exactly matches all six transmembrane helix annotations in UniProt entry P0DXU6 (evidence codes ECO:0000255, i.e., inferred by similarity). The sequence matches (SHA-256 identical), and the annotation is present in both the current entry (C5–C10) and the archived entry version 4 (H3–H8). The annotation is computational (by similarity), not experimentally determined, but it is the authoritative database assignment.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [C9](#evidence-c9), [C10](#evidence-c10), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6), [H7](#evidence-h7), [H8](#evidence-h8).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> C (single TM region) is trivially eliminable for a 272-residue ABC transporter permease, and D omits the 182..202 helix (AAGGLFAVAFPLTMISSIMVA), which is clearly hydrophobic enough to be a TM segment. However, the critical distinction between A and B lies solely in the third TM boundary: 124..144 vs 123..147. The extra residues in B (T at 123; R, P, D, G at 145–147) are more polar/charged and P is a helix-breaker, giving a very weak hydrophobicity argument for the shorter boundary. This is a 1-residue start and 3-residue end shift—far below the resolution that general hydrophobicity reasoning can reliably discriminate without a specific prediction tool or database lookup.


**Missing item-specific fact**

> The exact boundary assignment produced by the annotation pipeline (ECO:0000255, inferred by similarity) that defines whether the third TM is 124..144 or 123..147. No general biological principle cleanly resolves a 3-residue difference at a TM boundary.


**Reason**

> Eliminating C and D uses general reasoning (multi-TM protein, obvious hydrophobic segment missing). The decisive A-vs-B choice hinges on a 1–3 residue boundary precision that depends on the specific computational annotation rather than on general transmembrane biology.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "B"
]
```

> The third TM boundary differs by only a few residues (124..144 vs 123..147). Both regions contain a hydrophobic core flanked by somewhat polar residues. Without running a specific TM predictor or consulting the exact annotation, a careful analyst could reasonably assign either boundary. The question wording ('a segment that crosses the membrane') is also slightly ambiguous about whether one or all TM regions must be identified, though the multi-region format of A, B, and D makes the intended reading clear.


### Important caveats

- All six TM annotations carry evidence code ECO:0000255 (inferred by similarity), meaning they are computational predictions transferred by homology, not experimentally validated boundaries.
- The A-vs-B distinction (124..144 vs 123..147) is within the typical ±3–5 residue uncertainty of TM prediction tools, making it an unusually fine-grained discrimination for a benchmark question.
- The UniProt accession P0DXU6 was inferred from dataset metadata and was not provided to the evaluated model; the model must work from the raw sequence alone.
- The protein is an ABC transporter permease (DrrB2) involved in daunorubicin efflux; its multi-TM architecture is consistent with the six-helix assignment but does not uniquely determine the exact boundary positions.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "C (single TM region) is trivially eliminable for a 272-residue ABC transporter permease, and D omits the 182..202 helix (AAGGLFAVAFPLTMISSIMVA), which is clearly hydrophobic enough to be a TM segment. However, the critical distinction between A and B lies solely in the third TM boundary: 124..144 vs 123..147. The extra residues in B (T at 123; R, P, D, G at 145–147) are more polar/charged and P is a helix-breaker, giving a very weak hydrophobicity argument for the shorter boundary. This is a 1-residue start and 3-residue end shift—far below the resolution that general hydrophobicity reasoning can reliably discriminate without a specific prediction tool or database lookup.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The exact boundary assignment produced by the annotation pipeline (ECO:0000255, inferred by similarity) that defines whether the third TM is 124..144 or 123..147. No general biological principle cleanly resolves a 3-residue difference at a TM boundary.",
    "reason": "Eliminating C and D uses general reasoning (multi-TM protein, obvious hydrophobic segment missing). The decisive A-vs-B choice hinges on a 1–3 residue boundary precision that depends on the specific computational annotation rather than on general transmembrane biology."
  },
  "case_id": "transmembrane_0071",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "C7",
      "C8",
      "C9",
      "C10",
      "H3",
      "H4",
      "H5",
      "H6",
      "H7",
      "H8"
    ],
    "judgment": "supported",
    "reason": "Choice A (38..58; 73..93; 124..144; 156..176; 182..202; 244..264) exactly matches all six transmembrane helix annotations in UniProt entry P0DXU6 (evidence codes ECO:0000255, i.e., inferred by similarity). The sequence matches (SHA-256 identical), and the annotation is present in both the current entry (C5–C10) and the archived entry version 4 (H3–H8). The annotation is computational (by similarity), not experimentally determined, but it is the authoritative database assignment."
  },
  "important_caveats": [
    "All six TM annotations carry evidence code ECO:0000255 (inferred by similarity), meaning they are computational predictions transferred by homology, not experimentally validated boundaries.",
    "The A-vs-B distinction (124..144 vs 123..147) is within the typical ±3–5 residue uncertainty of TM prediction tools, making it an unusually fine-grained discrimination for a benchmark question.",
    "The UniProt accession P0DXU6 was inferred from dataset metadata and was not provided to the evaluated model; the model must work from the raw sequence alone.",
    "The protein is an ABC transporter permease (DrrB2) involved in daunorubicin efflux; its multi-TM architecture is consistent with the six-helix assignment but does not uniquely determine the exact boundary positions."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "B"
    ],
    "reason": "The third TM boundary differs by only a few residues (124..144 vs 123..147). Both regions contain a hydrophobic core flanked by somewhat polar residues. Without running a specific TM predictor or consulting the exact annotation, a careful analyst could reasonably assign either boundary. The question wording ('a segment that crosses the membrane') is also slightly ambiguous about whether one or all TM regions must be identified, though the multi-region format of A, B, and D makes the intended reading clear."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0071",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "Choice A (38..58; 73..93; 124..144; 156..176; 182..202; 244..264) exactly matches all six transmembrane helix annotations in UniProt entry P0DXU6 (evidence codes ECO:0000255, i.e., inferred by similarity). The sequence matches (SHA-256 identical), and the annotation is present in both the current entry (C5–C10) and the archived entry version 4 (H3–H8). The annotation is computational (by similarity), not experimentally determined, but it is the authoritative database assignment.",
    "evidence_ids": ["C5", "C6", "C7", "C8", "C9", "C10", "H3", "H4", "H5", "H6", "H7", "H8"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "C (single TM region) is trivially eliminable for a 272-residue ABC transporter permease, and D omits the 182..202 helix (AAGGLFAVAFPLTMISSIMVA), which is clearly hydrophobic enough to be a TM segment. However, the critical distinction between A and B lies solely in the third TM boundary: 124..144 vs 123..147. The extra residues in B (T at 123; R, P, D, G at 145–147) are more polar/charged and P is a helix-breaker, giving a very weak hydrophobicity argument for the shorter boundary. This is a 1-residue start and 3-residue end shift—far below the resolution that general hydrophobicity reasoning can reliably discriminate without a specific prediction tool or database lookup.",
    "missing_item_specific_fact": "The exact boundary assignment produced by the annotation pipeline (ECO:0000255, inferred by similarity) that defines whether the third TM is 124..144 or 123..147. No general biological principle cleanly resolves a 3-residue difference at a TM boundary.",
    "reason": "Eliminating C and D uses general reasoning (multi-TM protein, obvious hydrophobic segment missing). The decisive A-vs-B choice hinges on a 1–3 residue boundary precision that depends on the specific computational annotation rather than on general transmembrane biology."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "B"],
    "reason": "The third TM boundary differs by only a few residues (124..144 vs 123..147). Both regions contain a hydrophobic core flanked by somewhat polar residues. Without running a specific TM predictor or consulting the exact annotation, a careful analyst could reasonably assign either boundary. The question wording ('a segment that crosses the membrane') is also slightly ambiguous about whether one or all TM regions must be identified, though the multi-region format of A, B, and D makes the intended reading clear."
  },
  "important_caveats": [
    "All six TM annotations carry evidence code ECO:0000255 (inferred by similarity), meaning they are computational predictions transferred by homology, not experimentally validated boundaries.",
    "The A-vs-B distinction (124..144 vs 123..147) is within the typical ±3–5 residue uncertainty of TM prediction tools, making it an unusually fine-grained discrimination for a benchmark question.",
    "The UniProt accession P0DXU6 was inferred from dataset metadata and was not provided to the evaluated model; the model must work from the raw sequence alone.",
    "The protein is an ABC transporter permease (DrrB2) involved in daunorubicin efflux; its multi-TM architecture is consistent with the six-helix assignment but does not uniquely determine the exact boundary positions."
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

**Accession:** `P0DXU6` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 4. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXU6.json)  
**Locator:** `/features/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:39.151534+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":58},"start":{"modifier":"EXACT","value":38}},"type":"Transmembrane"}
```

Source SHA-256: `4e7d0b296d64a4ffb645956bc9763e367bd0533eedf73ba35b4dc16bd7421217`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXU6.json)  
**Locator:** `/features/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:39.151534+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":93},"start":{"modifier":"EXACT","value":73}},"type":"Transmembrane"}
```

Source SHA-256: `4e7d0b296d64a4ffb645956bc9763e367bd0533eedf73ba35b4dc16bd7421217`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXU6.json)  
**Locator:** `/features/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:39.151534+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":144},"start":{"modifier":"EXACT","value":124}},"type":"Transmembrane"}
```

Source SHA-256: `4e7d0b296d64a4ffb645956bc9763e367bd0533eedf73ba35b4dc16bd7421217`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXU6.json)  
**Locator:** `/features/4`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:39.151534+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":176},"start":{"modifier":"EXACT","value":156}},"type":"Transmembrane"}
```

Source SHA-256: `4e7d0b296d64a4ffb645956bc9763e367bd0533eedf73ba35b4dc16bd7421217`.

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXU6.json)  
**Locator:** `/features/5`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:39.151534+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":202},"start":{"modifier":"EXACT","value":182}},"type":"Transmembrane"}
```

Source SHA-256: `4e7d0b296d64a4ffb645956bc9763e367bd0533eedf73ba35b4dc16bd7421217`.

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXU6.json)  
**Locator:** `/features/6`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:39.151534+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":264},"start":{"modifier":"EXACT","value":244}},"type":"Transmembrane"}
```

Source SHA-256: `4e7d0b296d64a4ffb645956bc9763e367bd0533eedf73ba35b4dc16bd7421217`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXU6?format=txt&versions=4)  
**Locator:** `lines 73-75`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 4 / 1.  
**Retrieved:** 2026-11-02T04:29:40.921406+00:00.  

```text
FT   TRANSMEM        38..58
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `372a99e71818628749a5230f6a3ea50eb4a3ab3f801909ad5a5e951310594fb7`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXU6?format=txt&versions=4)  
**Locator:** `lines 76-78`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 4 / 1.  
**Retrieved:** 2026-11-02T04:29:40.921406+00:00.  

```text
FT   TRANSMEM        73..93
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `372a99e71818628749a5230f6a3ea50eb4a3ab3f801909ad5a5e951310594fb7`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXU6?format=txt&versions=4)  
**Locator:** `lines 79-81`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 4 / 1.  
**Retrieved:** 2026-11-02T04:29:40.921406+00:00.  

```text
FT   TRANSMEM        124..144
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `372a99e71818628749a5230f6a3ea50eb4a3ab3f801909ad5a5e951310594fb7`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXU6?format=txt&versions=4)  
**Locator:** `lines 82-84`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 4 / 1.  
**Retrieved:** 2026-11-02T04:29:40.921406+00:00.  

```text
FT   TRANSMEM        156..176
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `372a99e71818628749a5230f6a3ea50eb4a3ab3f801909ad5a5e951310594fb7`.

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXU6?format=txt&versions=4)  
**Locator:** `lines 85-87`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 4 / 1.  
**Retrieved:** 2026-11-02T04:29:40.921406+00:00.  

```text
FT   TRANSMEM        182..202
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `372a99e71818628749a5230f6a3ea50eb4a3ab3f801909ad5a5e951310594fb7`.

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXU6?format=txt&versions=4)  
**Locator:** `lines 88-90`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 4 / 1.  
**Retrieved:** 2026-11-02T04:29:40.921406+00:00.  

```text
FT   TRANSMEM        244..264
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `372a99e71818628749a5230f6a3ea50eb4a3ab3f801909ad5a5e951310594fb7`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json), zero-based source row 71. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
