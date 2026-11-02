# transmembrane_0001

[All 1,736 questions](../README.md) · [Method and limits](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `transmembrane`  
**Author expected answer:** **C** — 5..25; 40..60; 78..98; 119..139; 187..207; 223..243; 261..281; 302..322; 330..350; 385..405

| Expected-answer support | Reasoning versus lookup | Review status |
|---|---|---|
| supported | reasoning-supported | format-valid AI review |

These labels are Luna’s original judgments. Source support and reasoning from the original input are separate questions. The benchmark key and original score are unchanged.

## Complete original question

The sequence and choices below are the complete original user message, in their original order.

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

## Luna’s full visible review

### Expected-answer support: supported

> The sequence matches the UniProt record, whose archived and current annotations list the ten intervals in choice C as transmembrane helices. These are computationally evidenced annotations (ECO:0000255), not proof of experimental determination.

Cited evidence: [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6), [H7](#evidence-h7), [H8](#evidence-h8), [H9](#evidence-h9), [H10](#evidence-h10), [H11](#evidence-h11), [H12](#evidence-h12), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [C9](#evidence-c9), [C10](#evidence-c10), [C11](#evidence-c11), [C12](#evidence-c12), [C13](#evidence-c13), [C14](#evidence-c14).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains multiple strongly hydrophobic stretches consistent with membrane-spanning helices, including a hydrophobic core around 330..350. Choice B extends that interval into flanking residues, while choice C better matches the hydrophobic span; choice A also omits a strongly hydrophobic region around 261..281.

**Missing item-specific fact**

> Exact boundary conventions remain protein-specific, but an external annotation is not necessary to distinguish the choices from their conspicuous hydrophobic spans and the charged/polar flanks.

**Reason**

> The sequence itself gives meaningful grounds for selecting the candidate set. Boundary-level predictions are not certain from hydropathy alone, but the alternatives differ in ways that the sequence can help resolve.

### Question ambiguity

**Multiple defensible options named by Luna:** none.

> The options are not equally supported by the sequence: the listed hydrophobic segments favor C, while B's broader interval includes likely non-membrane flanks and A omits a hydrophobic segment.

### Important caveats

- The supporting UniProt transmembrane features are computationally evidenced rather than independently verified experimental measurements.
- Membrane-spanning boundaries are predictions and may vary with annotation conventions.

<details>
<summary>Saved visible review as JSON</summary>

```json
{
  "case_id": "transmembrane_0001",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches the UniProt record, whose archived and current annotations list the ten intervals in choice C as transmembrane helices. These are computationally evidenced annotations (ECO:0000255), not proof of experimental determination.",
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
    ]
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

## Project source-check notes

These project-authored, AI-assisted checks assess specific source claims. They are not expert adjudication and do not replace Luna’s saved review or the author key.

No additional case-specific project note was recorded. Citation membership checks do not establish that every scientific argument is correct.

## Reviewer-only source evidence

**This source material was supplied only to the reviewer. It was absent from the original evaluated question.** An exact-sequence database match can support a key without establishing that the question can be answered by reasoning from its original input.

**Accession:** `A0A0A8X338`; identity was recovered from dataset image-path metadata and was absent from the evaluated model input.  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; selected entry version 26. The exact author source snapshot remains unknown.

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

Question and key: [LiveProteinBench source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json) (zero-based source row 1). Benchmark content © 2026 LiveProteinBench contributors, [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). Cited UniProt / Gene Ontology excerpts retain their own attribution; see [source credits](../THIRD_PARTY_NOTICES.md).
