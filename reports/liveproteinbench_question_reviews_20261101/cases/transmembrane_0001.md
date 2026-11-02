# transmembrane_0001

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `transmembrane`  
**Author expected answer:** **C** — 5..25; 40..60; 78..98; 119..139; 187..207; 223..243; 261..281; 302..322; 330..350; 385..405

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MLKKLYFTVLSFIAIVGVISLYIRLSEGMKMSALTSYSSWGLWIVFYIYFIGLSAGSFLLSTMVYVFNMKQFERIGKLALFTAFFSLMAGLLFVLIDLGHPERFWHTLVYRQPNSILSWEIQFYLIYMLLIVAEIWFLMREEFAQRAQSTKGLTKLFNRTLTLGYKVPNSQQKLEFHREQSHKWMKILGIAGIPTAVGVHGGTGSLFGVVMAKEYWFSGLTPIIFLVSALVSGAALMLFLYSFFGGAKKNGDSLLKELGTLLTLFIGIDLLLMIAEFLIGLYNPIHHERMTFNEILFGDRWFIFWIGQIGMVIILPILLITISKGKRLLMGLAGLSVVLGIVCVRWILVIPAYVAPHFDGLDSAYNSSRLLYEYSPNLLEWSSSVGLIGIVILLFSITVQLVPVFNKQKEVHQTHGKPTPEIHIKA

[Multiple Choices]
A. 5..25; 40..60; 78..98; 119..139; 187..207; 223..243; 302..322; 330..350; 385..405
B. 5..25; 40..60; 78..98; 119..139; 187..207; 223..243; 261..281; 302..322; 326..352; 385..405
C. 5..25; 40..60; 78..98; 119..139; 187..207; 223..243; 261..281; 302..322; 330..350; 385..405
D. 27..47; 59..79; 109..129; 142..162; 168..188; 225..245
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

> The sequence matches the UniProt record, whose archived and current annotations list the ten intervals in choice C as transmembrane helices. These are computationally evidenced annotations (ECO:0000255), not proof of experimental determination.

Citations as saved: [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6), [H7](#evidence-h7), [H8](#evidence-h8), [H9](#evidence-h9), [H10](#evidence-h10), [H11](#evidence-h11), [H12](#evidence-h12), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [C9](#evidence-c9), [C10](#evidence-c10), [C11](#evidence-c11), [C12](#evidence-c12), [C13](#evidence-c13), [C14](#evidence-c14).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains multiple strongly hydrophobic stretches consistent with membrane-spanning helices, including a hydrophobic core around 330..350. Choice B extends that interval into flanking residues, while choice C better matches the hydrophobic span; choice A also omits a strongly hydrophobic region around 261..281.


**Missing item-specific fact**

> Exact boundary conventions remain protein-specific, but an external annotation is not necessary to distinguish the choices from their conspicuous hydrophobic spans and the charged/polar flanks.


**Reason**

> The sequence itself gives meaningful grounds for selecting the candidate set. Boundary-level predictions are not certain from hydropathy alone, but the alternatives differ in ways that the sequence can help resolve.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The options are not equally supported by the sequence: the listed hydrophobic segments favor C, while B's broader interval includes likely non-membrane flanks and A omits a hydrophobic segment.


### Important caveats

- The supporting UniProt transmembrane features are computationally evidenced rather than independently verified experimental measurements.
- Membrane-spanning boundaries are predictions and may vary with annotation conventions.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains multiple strongly hydrophobic stretches consistent with membrane-spanning helices, including a hydrophobic core around 330..350. Choice B extends that interval into flanking residues, while choice C better matches the hydrophobic span; choice A also omits a strongly hydrophobic region around 261..281.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "Exact boundary conventions remain protein-specific, but an external annotation is not necessary to distinguish the choices from their conspicuous hydrophobic spans and the charged/polar flanks.",
    "reason": "The sequence itself gives meaningful grounds for selecting the candidate set. Boundary-level predictions are not certain from hydropathy alone, but the alternatives differ in ways that the sequence can help resolve."
  },
  "case_id": "transmembrane_0001",
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
      "C5",
      "C6",
      "C7",
      "C8",
      "C9",
      "C10",
      "C11",
      "C12",
      "C13",
      "C14"
    ],
    "judgment": "supported",
    "reason": "The sequence matches the UniProt record, whose archived and current annotations list the ten intervals in choice C as transmembrane helices. These are computationally evidenced annotations (ECO:0000255), not proof of experimental determination."
  },
  "important_caveats": [
    "The supporting UniProt transmembrane features are computationally evidenced rather than independently verified experimental measurements.",
    "Membrane-spanning boundaries are predictions and may vary with annotation conventions."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The options are not equally supported by the sequence: the listed hydrophobic segments favor C, while B's broader interval includes likely non-membrane flanks and A omits a hydrophobic segment."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0001",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches the UniProt record, whose archived and current annotations list the ten intervals in choice C as transmembrane helices. These are computationally evidenced annotations (ECO:0000255), not proof of experimental determination.",
    "evidence_ids": ["H3", "H4", "H5", "H6", "H7", "H8", "H9", "H10", "H11", "H12", "C5", "C6", "C7", "C8", "C9", "C10", "C11", "C12", "C13", "C14"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains multiple strongly hydrophobic stretches consistent with membrane-spanning helices, including a hydrophobic core around 330..350. Choice B extends that interval into flanking residues, while choice C better matches the hydrophobic span; choice A also omits a strongly hydrophobic region around 261..281.",
    "missing_item_specific_fact": "Exact boundary conventions remain protein-specific, but an external annotation is not necessary to distinguish the choices from their conspicuous hydrophobic spans and the charged/polar flanks.",
    "reason": "The sequence itself gives meaningful grounds for selecting the candidate set. Boundary-level predictions are not certain from hydropathy alone, but the alternatives differ in ways that the sequence can help resolve."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The options are not equally supported by the sequence: the listed hydrophobic segments favor C, while B's broader interval includes likely non-membrane flanks and A omits a hydrophobic segment."
  },
  "important_caveats": [
    "The supporting UniProt transmembrane features are computationally evidenced rather than independently verified experimental measurements.",
    "Membrane-spanning boundaries are predictions and may vary with annotation conventions."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> Choice C (5..25; 40..60; 78..98; 119..139; 187..207; 223..243; 261..281; 302..322; 330..350; 385..405) matches the UniProt annotation for A0A0A8X338 (Selenate reductase subunit C, Mesobacillus selenatarsenatis) exactly across all 10 transmembrane helical segments. The sequence SHA256 matches. However, all annotations carry evidence code ECO:0000255 (inferred by similarity), meaning these are computational predictions transferred by homology, not experimentally determined boundaries.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [C9](#evidence-c9), [C10](#evidence-c10), [C11](#evidence-c11), [C12](#evidence-c12), [C13](#evidence-c13), [C14](#evidence-c14), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6), [H7](#evidence-h7), [H8](#evidence-h8), [H9](#evidence-h9), [H10](#evidence-h10), [H11](#evidence-h11), [H12](#evidence-h12).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> General reasoning can eliminate D (only 6 TM helices at entirely wrong positions for a multi-pass membrane anchor) and likely eliminate A (omits the 261..281 hydrophobic stretch, which a careful hydrophobicity scan of the sequence could reveal). However, distinguishing C from B requires resolving the boundary 330..350 vs 326..352 — a 4-residue N-terminal shift and 2-residue C-terminal shift at a single helix. This precision is algorithm-dependent and cannot be reliably determined by hydrophobicity reasoning alone.


**Missing item-specific fact**

> The exact output of the specific computational TM-prediction algorithm (e.g., TMHMM, Phobius) used to generate the UniProt annotation (ECO:0000255, inferred by similarity) that defines the precise residue boundaries, particularly whether the last helix starts at 326 or 330 and ends at 350 or 352.


**Reason**

> The UniProt annotation is purely computational (ECO:0000255 = inferred by similarity). The exact 1–4 residue boundary differences between B and C depend on the specific prediction tool's hydrophobicity window and scoring function, which is an item-specific annotation fact not derivable from general biological principles. While a trained TM predictor might reproduce these boundaries, that constitutes lookup of a specific algorithmic output rather than reasoning from first principles.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "C"
]
```

> B and C differ only at the 9th TM helix boundary (326..352 vs 330..350). Both represent plausible 20–26 residue hydrophobic helices. Without knowing the exact prediction algorithm's scoring, a reasoned hydrophobicity analysis could support either boundary. The distinction rests on a specific computational annotation rather than a clear biological principle.


### Important caveats

- All 10 TM annotations carry ECO:0000255 (inferred by similarity), meaning they are computational predictions transferred from a homologous protein, not experimentally validated boundaries.
- The UniProt entry was first public 2025-02-05; the author's exact source snapshot is unknown, though the sequence has not changed (sequenceVersion 1 since 2015).
- The benchmark sequence matches the UniProt reference exactly (SHA256 confirmed), so numbering is canonical.
- The protein is annotated as a membrane anchor subunit of a selenate reductase complex, consistent with a multi-pass TM topology, but the exact helix count and boundaries are prediction-dependent.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "General reasoning can eliminate D (only 6 TM helices at entirely wrong positions for a multi-pass membrane anchor) and likely eliminate A (omits the 261..281 hydrophobic stretch, which a careful hydrophobicity scan of the sequence could reveal). However, distinguishing C from B requires resolving the boundary 330..350 vs 326..352 — a 4-residue N-terminal shift and 2-residue C-terminal shift at a single helix. This precision is algorithm-dependent and cannot be reliably determined by hydrophobicity reasoning alone.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The exact output of the specific computational TM-prediction algorithm (e.g., TMHMM, Phobius) used to generate the UniProt annotation (ECO:0000255, inferred by similarity) that defines the precise residue boundaries, particularly whether the last helix starts at 326 or 330 and ends at 350 or 352.",
    "reason": "The UniProt annotation is purely computational (ECO:0000255 = inferred by similarity). The exact 1–4 residue boundary differences between B and C depend on the specific prediction tool's hydrophobicity window and scoring function, which is an item-specific annotation fact not derivable from general biological principles. While a trained TM predictor might reproduce these boundaries, that constitutes lookup of a specific algorithmic output rather than reasoning from first principles."
  },
  "case_id": "transmembrane_0001",
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
      "H3",
      "H4",
      "H5",
      "H6",
      "H7",
      "H8",
      "H9",
      "H10",
      "H11",
      "H12"
    ],
    "judgment": "supported",
    "reason": "Choice C (5..25; 40..60; 78..98; 119..139; 187..207; 223..243; 261..281; 302..322; 330..350; 385..405) matches the UniProt annotation for A0A0A8X338 (Selenate reductase subunit C, Mesobacillus selenatarsenatis) exactly across all 10 transmembrane helical segments. The sequence SHA256 matches. However, all annotations carry evidence code ECO:0000255 (inferred by similarity), meaning these are computational predictions transferred by homology, not experimentally determined boundaries."
  },
  "important_caveats": [
    "All 10 TM annotations carry ECO:0000255 (inferred by similarity), meaning they are computational predictions transferred from a homologous protein, not experimentally validated boundaries.",
    "The UniProt entry was first public 2025-02-05; the author's exact source snapshot is unknown, though the sequence has not changed (sequenceVersion 1 since 2015).",
    "The benchmark sequence matches the UniProt reference exactly (SHA256 confirmed), so numbering is canonical.",
    "The protein is annotated as a membrane anchor subunit of a selenate reductase complex, consistent with a multi-pass TM topology, but the exact helix count and boundaries are prediction-dependent."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "C"
    ],
    "reason": "B and C differ only at the 9th TM helix boundary (326..352 vs 330..350). Both represent plausible 20–26 residue hydrophobic helices. Without knowing the exact prediction algorithm's scoring, a reasoned hydrophobicity analysis could support either boundary. The distinction rests on a specific computational annotation rather than a clear biological principle."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0001",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "Choice C (5..25; 40..60; 78..98; 119..139; 187..207; 223..243; 261..281; 302..322; 330..350; 385..405) matches the UniProt annotation for A0A0A8X338 (Selenate reductase subunit C, Mesobacillus selenatarsenatis) exactly across all 10 transmembrane helical segments. The sequence SHA256 matches. However, all annotations carry evidence code ECO:0000255 (inferred by similarity), meaning these are computational predictions transferred by homology, not experimentally determined boundaries.",
    "evidence_ids": ["C5","C6","C7","C8","C9","C10","C11","C12","C13","C14","H3","H4","H5","H6","H7","H8","H9","H10","H11","H12"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "General reasoning can eliminate D (only 6 TM helices at entirely wrong positions for a multi-pass membrane anchor) and likely eliminate A (omits the 261..281 hydrophobic stretch, which a careful hydrophobicity scan of the sequence could reveal). However, distinguishing C from B requires resolving the boundary 330..350 vs 326..352 — a 4-residue N-terminal shift and 2-residue C-terminal shift at a single helix. This precision is algorithm-dependent and cannot be reliably determined by hydrophobicity reasoning alone.",
    "missing_item_specific_fact": "The exact output of the specific computational TM-prediction algorithm (e.g., TMHMM, Phobius) used to generate the UniProt annotation (ECO:0000255, inferred by similarity) that defines the precise residue boundaries, particularly whether the last helix starts at 326 or 330 and ends at 350 or 352.",
    "reason": "The UniProt annotation is purely computational (ECO:0000255 = inferred by similarity). The exact 1–4 residue boundary differences between B and C depend on the specific prediction tool's hydrophobicity window and scoring function, which is an item-specific annotation fact not derivable from general biological principles. While a trained TM predictor might reproduce these boundaries, that constitutes lookup of a specific algorithmic output rather than reasoning from first principles."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "C"],
    "reason": "B and C differ only at the 9th TM helix boundary (326..352 vs 330..350). Both represent plausible 20–26 residue hydrophobic helices. Without knowing the exact prediction algorithm's scoring, a reasoned hydrophobicity analysis could support either boundary. The distinction rests on a specific computational annotation rather than a clear biological principle."
  },
  "important_caveats": [
    "All 10 TM annotations carry ECO:0000255 (inferred by similarity), meaning they are computational predictions transferred from a homologous protein, not experimentally validated boundaries.",
    "The UniProt entry was first public 2025-02-05; the author's exact source snapshot is unknown, though the sequence has not changed (sequenceVersion 1 since 2015).",
    "The benchmark sequence matches the UniProt reference exactly (SHA256 confirmed), so numbering is canonical.",
    "The protein is annotated as a membrane anchor subunit of a selenate reductase complex, consistent with a multi-pass TM topology, but the exact helix count and boundaries are prediction-dependent."
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

**Accession:** `A0A0A8X338` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 26. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0A8X338.json)  
**Locator:** `/features/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:23:56.888485+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":25},"start":{"modifier":"EXACT","value":5}},"type":"Transmembrane"}
```

Source SHA-256: `f24d48c67ebe30dab27bb776e276107f0f50c197edcf4849b2ea2624ac4d4bbe`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0A8X338.json)  
**Locator:** `/features/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:23:56.888485+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":60},"start":{"modifier":"EXACT","value":40}},"type":"Transmembrane"}
```

Source SHA-256: `f24d48c67ebe30dab27bb776e276107f0f50c197edcf4849b2ea2624ac4d4bbe`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0A8X338.json)  
**Locator:** `/features/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:23:56.888485+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":98},"start":{"modifier":"EXACT","value":78}},"type":"Transmembrane"}
```

Source SHA-256: `f24d48c67ebe30dab27bb776e276107f0f50c197edcf4849b2ea2624ac4d4bbe`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0A8X338.json)  
**Locator:** `/features/4`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:23:56.888485+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":139},"start":{"modifier":"EXACT","value":119}},"type":"Transmembrane"}
```

Source SHA-256: `f24d48c67ebe30dab27bb776e276107f0f50c197edcf4849b2ea2624ac4d4bbe`.

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0A8X338.json)  
**Locator:** `/features/5`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:23:56.888485+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":207},"start":{"modifier":"EXACT","value":187}},"type":"Transmembrane"}
```

Source SHA-256: `f24d48c67ebe30dab27bb776e276107f0f50c197edcf4849b2ea2624ac4d4bbe`.

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0A8X338.json)  
**Locator:** `/features/6`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:23:56.888485+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":243},"start":{"modifier":"EXACT","value":223}},"type":"Transmembrane"}
```

Source SHA-256: `f24d48c67ebe30dab27bb776e276107f0f50c197edcf4849b2ea2624ac4d4bbe`.

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0A8X338.json)  
**Locator:** `/features/7`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:23:56.888485+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":281},"start":{"modifier":"EXACT","value":261}},"type":"Transmembrane"}
```

Source SHA-256: `f24d48c67ebe30dab27bb776e276107f0f50c197edcf4849b2ea2624ac4d4bbe`.

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0A8X338.json)  
**Locator:** `/features/8`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:23:56.888485+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":322},"start":{"modifier":"EXACT","value":302}},"type":"Transmembrane"}
```

Source SHA-256: `f24d48c67ebe30dab27bb776e276107f0f50c197edcf4849b2ea2624ac4d4bbe`.

### Evidence C13

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0A8X338.json)  
**Locator:** `/features/9`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:23:56.888485+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":350},"start":{"modifier":"EXACT","value":330}},"type":"Transmembrane"}
```

Source SHA-256: `f24d48c67ebe30dab27bb776e276107f0f50c197edcf4849b2ea2624ac4d4bbe`.

### Evidence C14

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0A8X338.json)  
**Locator:** `/features/10`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:23:56.888485+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":405},"start":{"modifier":"EXACT","value":385}},"type":"Transmembrane"}
```

Source SHA-256: `f24d48c67ebe30dab27bb776e276107f0f50c197edcf4849b2ea2624ac4d4bbe`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0A8X338?format=txt&versions=26)  
**Locator:** `lines 83-85`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 26 / 1.  
**Retrieved:** 2026-11-02T04:24:00.225132+00:00.  

```text
FT   TRANSMEM        5..25
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `eb155874ab7c90cb9f9b357a382d734672b54b5376824079e6a394ed2c9dea57`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0A8X338?format=txt&versions=26)  
**Locator:** `lines 86-88`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 26 / 1.  
**Retrieved:** 2026-11-02T04:24:00.225132+00:00.  

```text
FT   TRANSMEM        40..60
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `eb155874ab7c90cb9f9b357a382d734672b54b5376824079e6a394ed2c9dea57`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0A8X338?format=txt&versions=26)  
**Locator:** `lines 89-91`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 26 / 1.  
**Retrieved:** 2026-11-02T04:24:00.225132+00:00.  

```text
FT   TRANSMEM        78..98
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `eb155874ab7c90cb9f9b357a382d734672b54b5376824079e6a394ed2c9dea57`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0A8X338?format=txt&versions=26)  
**Locator:** `lines 92-94`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 26 / 1.  
**Retrieved:** 2026-11-02T04:24:00.225132+00:00.  

```text
FT   TRANSMEM        119..139
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `eb155874ab7c90cb9f9b357a382d734672b54b5376824079e6a394ed2c9dea57`.

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0A8X338?format=txt&versions=26)  
**Locator:** `lines 95-97`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 26 / 1.  
**Retrieved:** 2026-11-02T04:24:00.225132+00:00.  

```text
FT   TRANSMEM        187..207
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `eb155874ab7c90cb9f9b357a382d734672b54b5376824079e6a394ed2c9dea57`.

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0A8X338?format=txt&versions=26)  
**Locator:** `lines 98-100`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 26 / 1.  
**Retrieved:** 2026-11-02T04:24:00.225132+00:00.  

```text
FT   TRANSMEM        223..243
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `eb155874ab7c90cb9f9b357a382d734672b54b5376824079e6a394ed2c9dea57`.

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0A8X338?format=txt&versions=26)  
**Locator:** `lines 101-103`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 26 / 1.  
**Retrieved:** 2026-11-02T04:24:00.225132+00:00.  

```text
FT   TRANSMEM        261..281
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `eb155874ab7c90cb9f9b357a382d734672b54b5376824079e6a394ed2c9dea57`.

### Evidence H10

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0A8X338?format=txt&versions=26)  
**Locator:** `lines 104-106`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 26 / 1.  
**Retrieved:** 2026-11-02T04:24:00.225132+00:00.  

```text
FT   TRANSMEM        302..322
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `eb155874ab7c90cb9f9b357a382d734672b54b5376824079e6a394ed2c9dea57`.

### Evidence H11

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0A8X338?format=txt&versions=26)  
**Locator:** `lines 107-109`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 26 / 1.  
**Retrieved:** 2026-11-02T04:24:00.225132+00:00.  

```text
FT   TRANSMEM        330..350
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `eb155874ab7c90cb9f9b357a382d734672b54b5376824079e6a394ed2c9dea57`.

### Evidence H12

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0A8X338?format=txt&versions=26)  
**Locator:** `lines 110-112`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 26 / 1.  
**Retrieved:** 2026-11-02T04:24:00.225132+00:00.  

```text
FT   TRANSMEM        385..405
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `eb155874ab7c90cb9f9b357a382d734672b54b5376824079e6a394ed2c9dea57`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json), zero-based source row 1. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
