# transmembrane_0076

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `transmembrane`  
**Author expected answer:** **C** — 5..25; 72..92; 111..131; 149..169; 177..197; 222..242; 267..287; 298..318

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MLHSASVIFLSLSVLAAVGVWGPFVRDGGFDAMDAVVARHPSTGIPGLQHYPEFDRGLMSIVAFNLSAVNSIAYCFMMQFLANVAVIPVILCTEDSSAAPGSWVRYSTIWGLLSQLGTSAVIYPLYAMSFIRQSSREPSQTRQPMSDMALILNMAMGYALPAAITLNVLHSSLNMQIWGILAFTVYPICMKLMARIIKVFTGFRKFPTRSRHQSIPTLRYAVAGGVALQGHLWYLGTELGIFKGHTPSLSAEKMDSEGGARLVLRFLQVDYAITFLAMLLLAWHELIYHRILPAWRALGGLIIGWILVGPGATLAAAWYLRSRFIMAPGKRKKRYGD

[Multiple Choices]
A. 5..25; 72..92; 111..131; 151..170; 177..197; 222..242; 267..287; 298..318
B. 227..249
C. 5..25; 72..92; 111..131; 149..169; 177..197; 222..242; 267..287; 298..318
D. 72..92; 111..131; 149..169; 177..197; 222..242; 267..287; 298..318
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

> The sequence-matched UniProt record annotates eight transmembrane helices at the coordinates in choice C. The evidence code ECO:0000255 indicates computational annotation, not experimental confirmation; the same coordinates are present in the historical record checked.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [C9](#evidence-c9), [C10](#evidence-c10), [C11](#evidence-c11), [C12](#evidence-c12), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6), [H7](#evidence-h7), [H8](#evidence-h8), [H9](#evidence-h9), [H10](#evidence-h10).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence has multiple long hydrophobic stretches consistent with membrane-spanning helices, supporting the general prediction of several transmembrane regions.


**Missing item-specific fact**

> Selecting C over A requires the exact predicted boundaries for the region annotated as 149..169 rather than 151..170; that item-specific coordinate annotation is not supplied.


**Reason**

> Sequence composition supports broad transmembrane predictions, but does not reliably distinguish the nearly identical boundary choices. The exact database-style coordinates depend on an item-specific annotation or prediction.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "C"
]
```

> Choices A and C differ only in the boundaries of one hydrophobic span by about two residues. Both are plausible sequence-based boundary estimates, although the cited annotation specifically supports C.


### Important caveats

- The reviewer-only evidence was not supplied to the evaluated model and does not make the question reasoning-supported.
- The UniProt coordinates are computational annotations, not evidence that the membrane boundaries were experimentally measured.
- The sequence matches the cited UniProt sequence; the historical record checked also carries these coordinates, but the author's exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has multiple long hydrophobic stretches consistent with membrane-spanning helices, supporting the general prediction of several transmembrane regions.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "Selecting C over A requires the exact predicted boundaries for the region annotated as 149..169 rather than 151..170; that item-specific coordinate annotation is not supplied.",
    "reason": "Sequence composition supports broad transmembrane predictions, but does not reliably distinguish the nearly identical boundary choices. The exact database-style coordinates depend on an item-specific annotation or prediction."
  },
  "case_id": "transmembrane_0076",
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
    "reason": "The sequence-matched UniProt record annotates eight transmembrane helices at the coordinates in choice C. The evidence code ECO:0000255 indicates computational annotation, not experimental confirmation; the same coordinates are present in the historical record checked."
  },
  "important_caveats": [
    "The reviewer-only evidence was not supplied to the evaluated model and does not make the question reasoning-supported.",
    "The UniProt coordinates are computational annotations, not evidence that the membrane boundaries were experimentally measured.",
    "The sequence matches the cited UniProt sequence; the historical record checked also carries these coordinates, but the author's exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "C"
    ],
    "reason": "Choices A and C differ only in the boundaries of one hydrophobic span by about two residues. Both are plausible sequence-based boundary estimates, although the cited annotation specifically supports C."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0076",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates eight transmembrane helices at the coordinates in choice C. The evidence code ECO:0000255 indicates computational annotation, not experimental confirmation; the same coordinates are present in the historical record checked.",
    "evidence_ids": ["C5", "C6", "C7", "C8", "C9", "C10", "C11", "C12", "H3", "H4", "H5", "H6", "H7", "H8", "H9", "H10"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence has multiple long hydrophobic stretches consistent with membrane-spanning helices, supporting the general prediction of several transmembrane regions.",
    "missing_item_specific_fact": "Selecting C over A requires the exact predicted boundaries for the region annotated as 149..169 rather than 151..170; that item-specific coordinate annotation is not supplied.",
    "reason": "Sequence composition supports broad transmembrane predictions, but does not reliably distinguish the nearly identical boundary choices. The exact database-style coordinates depend on an item-specific annotation or prediction."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "C"],
    "reason": "Choices A and C differ only in the boundaries of one hydrophobic span by about two residues. Both are plausible sequence-based boundary estimates, although the cited annotation specifically supports C."
  },
  "important_caveats": [
    "The reviewer-only evidence was not supplied to the evaluated model and does not make the question reasoning-supported.",
    "The UniProt coordinates are computational annotations, not evidence that the membrane boundaries were experimentally measured.",
    "The sequence matches the cited UniProt sequence; the historical record checked also carries these coordinates, but the author's exact source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry P0DXW1 (terpene cyclase from Pyrenophora dematioidea, sequence matched by SHA256) annotates exactly eight transmembrane helical regions: 5..25, 72..92, 111..131, 149..169, 177..197, 222..242, 267..287, 298..318. This matches Choice C verbatim. However, all eight annotations carry evidence code ECO:0000255 (inferred by similarity), meaning they are computational predictions transferred from homologous entries, not experimentally determined boundaries. The annotation is a database claim, not experimental proof of membrane topology.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [C9](#evidence-c9), [C10](#evidence-c10), [C11](#evidence-c11), [C12](#evidence-c12), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6), [H7](#evidence-h7), [H8](#evidence-h8), [H9](#evidence-h9), [H10](#evidence-h10).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> Choice B (single region 227..249) is trivially eliminable because the 337-residue protein contains multiple long hydrophobic stretches, making a single-TM assignment implausible. The C-vs-D distinction (inclusion of the N-terminal 5..25 segment) could in principle be argued: the N-terminal region is hydrophobic but lacks the classic signal-peptide architecture (no N-terminal basic residues, no clear AXA cleavage motif), so one might reason it is a genuine TM helix rather than a cleaved signal peptide. However, this argument is weak and ambiguous.


**Missing item-specific fact**

> The critical A-vs-C distinction is a 2-residue boundary shift for the fourth TM helix (151..170 vs 149..169). The local sequence (149-MALILNMAMGYALPAAITLNV-169 vs 151-LILNMAMGYALPAAITLNVL-170) has nearly identical hydrophobicity profiles; M(149) and A(150) are hydrophobic, and L(170) is hydrophobic, so no general biological principle cleanly favors one boundary over the other. Resolving this requires the specific UniProt annotation (or the output of the particular prediction tool that generated it), which is absent from the model input.


**Reason**

> The question's decisive discrimination between the two most plausible choices (A and C) hinges on a 2-residue boundary assignment that is within the normal uncertainty of any TM prediction method and cannot be resolved by hydrophobicity analysis, helix-propensity reasoning, or general membrane biology. The annotation evidence is computational (ECO:0000255), so even the 'ground truth' is a prediction, not an experimental measurement. A model would need to recall or look up the exact UniProt feature coordinates for P0DXW1 to select C over A.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "C"
]
```

> Choices A and C differ only in the 4th TM boundary (151..170 vs 149..169). The hydrophobicity profile of residues 149–170 does not sharply delineate one boundary over the other: positions 149 (M) and 150 (A) are hydrophobic, and position 170 (L) is also hydrophobic. Any reasonable TM-prediction heuristic could place the boundary at either 149 or 151. Without the specific database annotation, both A and C are defensible. Choice D (omitting 5..25) is somewhat less defensible but not unreasonable if one interprets the N-terminal hydrophobic stretch as a signal peptide.


### Important caveats

- All eight TM annotations carry ECO:0000255 (similarity-based inference), not experimental evidence. The 'correct' boundaries are computational predictions, not measured membrane-spanning regions.
- The UniProt entry was first public on 2025-02-05; the author's source snapshot date is unknown, though the sequence and annotation were stable through at least entry version 2.
- Choice B (single region 227..249) is an obvious distractor that does not affect the substantive ambiguity between A, C, and D.
- The reviewer-only evidence confirms sequence identity (SHA256 match) between the benchmark input and the UniProt entry, so the annotation does apply to the supplied sequence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Choice B (single region 227..249) is trivially eliminable because the 337-residue protein contains multiple long hydrophobic stretches, making a single-TM assignment implausible. The C-vs-D distinction (inclusion of the N-terminal 5..25 segment) could in principle be argued: the N-terminal region is hydrophobic but lacks the classic signal-peptide architecture (no N-terminal basic residues, no clear AXA cleavage motif), so one might reason it is a genuine TM helix rather than a cleaved signal peptide. However, this argument is weak and ambiguous.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The critical A-vs-C distinction is a 2-residue boundary shift for the fourth TM helix (151..170 vs 149..169). The local sequence (149-MALILNMAMGYALPAAITLNV-169 vs 151-LILNMAMGYALPAAITLNVL-170) has nearly identical hydrophobicity profiles; M(149) and A(150) are hydrophobic, and L(170) is hydrophobic, so no general biological principle cleanly favors one boundary over the other. Resolving this requires the specific UniProt annotation (or the output of the particular prediction tool that generated it), which is absent from the model input.",
    "reason": "The question's decisive discrimination between the two most plausible choices (A and C) hinges on a 2-residue boundary assignment that is within the normal uncertainty of any TM prediction method and cannot be resolved by hydrophobicity analysis, helix-propensity reasoning, or general membrane biology. The annotation evidence is computational (ECO:0000255), so even the 'ground truth' is a prediction, not an experimental measurement. A model would need to recall or look up the exact UniProt feature coordinates for P0DXW1 to select C over A."
  },
  "case_id": "transmembrane_0076",
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
    "reason": "The UniProt entry P0DXW1 (terpene cyclase from Pyrenophora dematioidea, sequence matched by SHA256) annotates exactly eight transmembrane helical regions: 5..25, 72..92, 111..131, 149..169, 177..197, 222..242, 267..287, 298..318. This matches Choice C verbatim. However, all eight annotations carry evidence code ECO:0000255 (inferred by similarity), meaning they are computational predictions transferred from homologous entries, not experimentally determined boundaries. The annotation is a database claim, not experimental proof of membrane topology."
  },
  "important_caveats": [
    "All eight TM annotations carry ECO:0000255 (similarity-based inference), not experimental evidence. The 'correct' boundaries are computational predictions, not measured membrane-spanning regions.",
    "The UniProt entry was first public on 2025-02-05; the author's source snapshot date is unknown, though the sequence and annotation were stable through at least entry version 2.",
    "Choice B (single region 227..249) is an obvious distractor that does not affect the substantive ambiguity between A, C, and D.",
    "The reviewer-only evidence confirms sequence identity (SHA256 match) between the benchmark input and the UniProt entry, so the annotation does apply to the supplied sequence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "C"
    ],
    "reason": "Choices A and C differ only in the 4th TM boundary (151..170 vs 149..169). The hydrophobicity profile of residues 149–170 does not sharply delineate one boundary over the other: positions 149 (M) and 150 (A) are hydrophobic, and position 170 (L) is also hydrophobic. Any reasonable TM-prediction heuristic could place the boundary at either 149 or 151. Without the specific database annotation, both A and C are defensible. Choice D (omitting 5..25) is somewhat less defensible but not unreasonable if one interprets the N-terminal hydrophobic stretch as a signal peptide."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0076",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry P0DXW1 (terpene cyclase from Pyrenophora dematioidea, sequence matched by SHA256) annotates exactly eight transmembrane helical regions: 5..25, 72..92, 111..131, 149..169, 177..197, 222..242, 267..287, 298..318. This matches Choice C verbatim. However, all eight annotations carry evidence code ECO:0000255 (inferred by similarity), meaning they are computational predictions transferred from homologous entries, not experimentally determined boundaries. The annotation is a database claim, not experimental proof of membrane topology.",
    "evidence_ids": ["C5", "C6", "C7", "C8", "C9", "C10", "C11", "C12", "H3", "H4", "H5", "H6", "H7", "H8", "H9", "H10"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "Choice B (single region 227..249) is trivially eliminable because the 337-residue protein contains multiple long hydrophobic stretches, making a single-TM assignment implausible. The C-vs-D distinction (inclusion of the N-terminal 5..25 segment) could in principle be argued: the N-terminal region is hydrophobic but lacks the classic signal-peptide architecture (no N-terminal basic residues, no clear AXA cleavage motif), so one might reason it is a genuine TM helix rather than a cleaved signal peptide. However, this argument is weak and ambiguous.",
    "missing_item_specific_fact": "The critical A-vs-C distinction is a 2-residue boundary shift for the fourth TM helix (151..170 vs 149..169). The local sequence (149-MALILNMAMGYALPAAITLNV-169 vs 151-LILNMAMGYALPAAITLNVL-170) has nearly identical hydrophobicity profiles; M(149) and A(150) are hydrophobic, and L(170) is hydrophobic, so no general biological principle cleanly favors one boundary over the other. Resolving this requires the specific UniProt annotation (or the output of the particular prediction tool that generated it), which is absent from the model input.",
    "reason": "The question's decisive discrimination between the two most plausible choices (A and C) hinges on a 2-residue boundary assignment that is within the normal uncertainty of any TM prediction method and cannot be resolved by hydrophobicity analysis, helix-propensity reasoning, or general membrane biology. The annotation evidence is computational (ECO:0000255), so even the 'ground truth' is a prediction, not an experimental measurement. A model would need to recall or look up the exact UniProt feature coordinates for P0DXW1 to select C over A."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "C"],
    "reason": "Choices A and C differ only in the 4th TM boundary (151..170 vs 149..169). The hydrophobicity profile of residues 149–170 does not sharply delineate one boundary over the other: positions 149 (M) and 150 (A) are hydrophobic, and position 170 (L) is also hydrophobic. Any reasonable TM-prediction heuristic could place the boundary at either 149 or 151. Without the specific database annotation, both A and C are defensible. Choice D (omitting 5..25) is somewhat less defensible but not unreasonable if one interprets the N-terminal hydrophobic stretch as a signal peptide."
  },
  "important_caveats": [
    "All eight TM annotations carry ECO:0000255 (similarity-based inference), not experimental evidence. The 'correct' boundaries are computational predictions, not measured membrane-spanning regions.",
    "The UniProt entry was first public on 2025-02-05; the author's source snapshot date is unknown, though the sequence and annotation were stable through at least entry version 2.",
    "Choice B (single region 227..249) is an obvious distractor that does not affect the substantive ambiguity between A, C, and D.",
    "The reviewer-only evidence confirms sequence identity (SHA256 match) between the benchmark input and the UniProt entry, so the annotation does apply to the supplied sequence."
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

**Accession:** `P0DXW1` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 2. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXW1.json)  
**Locator:** `/features/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:16.733133+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":25},"start":{"modifier":"EXACT","value":5}},"type":"Transmembrane"}
```

Source SHA-256: `3f2ff3dca517c7cada001b0d9e2f2388aebcbab4f14d2d2a9a551d33f51517e8`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXW1.json)  
**Locator:** `/features/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:16.733133+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":92},"start":{"modifier":"EXACT","value":72}},"type":"Transmembrane"}
```

Source SHA-256: `3f2ff3dca517c7cada001b0d9e2f2388aebcbab4f14d2d2a9a551d33f51517e8`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXW1.json)  
**Locator:** `/features/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:16.733133+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":131},"start":{"modifier":"EXACT","value":111}},"type":"Transmembrane"}
```

Source SHA-256: `3f2ff3dca517c7cada001b0d9e2f2388aebcbab4f14d2d2a9a551d33f51517e8`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXW1.json)  
**Locator:** `/features/4`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:16.733133+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":169},"start":{"modifier":"EXACT","value":149}},"type":"Transmembrane"}
```

Source SHA-256: `3f2ff3dca517c7cada001b0d9e2f2388aebcbab4f14d2d2a9a551d33f51517e8`.

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXW1.json)  
**Locator:** `/features/5`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:16.733133+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":197},"start":{"modifier":"EXACT","value":177}},"type":"Transmembrane"}
```

Source SHA-256: `3f2ff3dca517c7cada001b0d9e2f2388aebcbab4f14d2d2a9a551d33f51517e8`.

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXW1.json)  
**Locator:** `/features/6`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:16.733133+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":242},"start":{"modifier":"EXACT","value":222}},"type":"Transmembrane"}
```

Source SHA-256: `3f2ff3dca517c7cada001b0d9e2f2388aebcbab4f14d2d2a9a551d33f51517e8`.

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXW1.json)  
**Locator:** `/features/7`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:16.733133+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":287},"start":{"modifier":"EXACT","value":267}},"type":"Transmembrane"}
```

Source SHA-256: `3f2ff3dca517c7cada001b0d9e2f2388aebcbab4f14d2d2a9a551d33f51517e8`.

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXW1.json)  
**Locator:** `/features/8`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:16.733133+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":318},"start":{"modifier":"EXACT","value":298}},"type":"Transmembrane"}
```

Source SHA-256: `3f2ff3dca517c7cada001b0d9e2f2388aebcbab4f14d2d2a9a551d33f51517e8`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXW1?format=txt&versions=2)  
**Locator:** `lines 51-53`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 2 / 1.  
**Retrieved:** 2026-11-01T06:28:24.266216+00:00.  

```text
FT   TRANSMEM        5..25
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `db1acbf2ac66c5648de96f9c489a7a4f13b2cb19c91ff902f8cef92abf8b0704`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXW1?format=txt&versions=2)  
**Locator:** `lines 54-56`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 2 / 1.  
**Retrieved:** 2026-11-01T06:28:24.266216+00:00.  

```text
FT   TRANSMEM        72..92
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `db1acbf2ac66c5648de96f9c489a7a4f13b2cb19c91ff902f8cef92abf8b0704`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXW1?format=txt&versions=2)  
**Locator:** `lines 57-59`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 2 / 1.  
**Retrieved:** 2026-11-01T06:28:24.266216+00:00.  

```text
FT   TRANSMEM        111..131
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `db1acbf2ac66c5648de96f9c489a7a4f13b2cb19c91ff902f8cef92abf8b0704`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXW1?format=txt&versions=2)  
**Locator:** `lines 60-62`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 2 / 1.  
**Retrieved:** 2026-11-01T06:28:24.266216+00:00.  

```text
FT   TRANSMEM        149..169
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `db1acbf2ac66c5648de96f9c489a7a4f13b2cb19c91ff902f8cef92abf8b0704`.

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXW1?format=txt&versions=2)  
**Locator:** `lines 63-65`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 2 / 1.  
**Retrieved:** 2026-11-01T06:28:24.266216+00:00.  

```text
FT   TRANSMEM        177..197
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `db1acbf2ac66c5648de96f9c489a7a4f13b2cb19c91ff902f8cef92abf8b0704`.

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXW1?format=txt&versions=2)  
**Locator:** `lines 66-68`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 2 / 1.  
**Retrieved:** 2026-11-01T06:28:24.266216+00:00.  

```text
FT   TRANSMEM        222..242
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `db1acbf2ac66c5648de96f9c489a7a4f13b2cb19c91ff902f8cef92abf8b0704`.

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXW1?format=txt&versions=2)  
**Locator:** `lines 69-71`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 2 / 1.  
**Retrieved:** 2026-11-01T06:28:24.266216+00:00.  

```text
FT   TRANSMEM        267..287
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `db1acbf2ac66c5648de96f9c489a7a4f13b2cb19c91ff902f8cef92abf8b0704`.

### Evidence H10

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXW1?format=txt&versions=2)  
**Locator:** `lines 72-74`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 2 / 1.  
**Retrieved:** 2026-11-01T06:28:24.266216+00:00.  

```text
FT   TRANSMEM        298..318
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `db1acbf2ac66c5648de96f9c489a7a4f13b2cb19c91ff902f8cef92abf8b0704`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json), zero-based source row 76. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
