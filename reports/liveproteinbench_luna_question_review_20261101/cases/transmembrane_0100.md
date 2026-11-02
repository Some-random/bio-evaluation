# transmembrane_0100

[All 1,736 questions](../README.md) · [Method and limits](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `transmembrane`  
**Author expected answer:** **C** — 1..21; 31..51; 56..76; 77..97; 101..121; 128..148; 149..169; 182..202; 206..226; 321..341

| Expected-answer support | Reasoning versus lookup | Review status |
|---|---|---|
| supported | lookup-dependent | format-valid AI review |

These labels are Luna’s original judgments. Source support and reasoning from the original input are separate questions. The benchmark key and original score are unchanged.

## Complete original question

The sequence and choices below are the complete original user message, in their original order.

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

## Luna’s full visible review

### Expected-answer support: supported

> Choice C matches the transmembrane intervals annotated for the exact matching sequence in both the current UniProt record and a historical snapshot. These annotations carry ECO:0000255, indicating computational evidence; they support the key as an annotation-based answer, not as direct experimental confirmation.

Cited evidence: [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [C9](#evidence-c9), [C10](#evidence-c10), [C11](#evidence-c11), [C12](#evidence-c12), [C13](#evidence-c13), [C14](#evidence-c14), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6), [H7](#evidence-h7), [H8](#evidence-h8), [H9](#evidence-h9), [H10](#evidence-h10), [H11](#evidence-h11), [H12](#evidence-h12), [H13](#evidence-h13).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence has many hydrophobic stretches, which makes a multi-pass membrane protein plausible and supports several candidate regions. But that general signal does not robustly establish the complete set of spans or their exact boundaries, especially for the less clearly hydrophobic 77..97 interval.

**Missing item-specific fact**

> The sequence-specific transmembrane-region annotation, including its predicted intervals and boundary conventions, is absent from the prompt.

**Reason**

> Choosing C over the alternatives depends on the precise region map: sequence hydrophobicity is informative, but does not uniquely determine the marginal span or small boundary differences among the choices.

### Question ambiguity

**Multiple defensible options named by Luna:** none.

> The supplied reference annotation supports C as the matching option. Transmembrane boundaries can vary between prediction methods, but no other listed choice matches the cited annotation.

### Important caveats

- The supporting UniProt transmembrane annotations are computational, not established here by direct experimental topology measurements.
- The reviewer-only accession and annotations were not available to the evaluated model.

<details>
<summary>Saved visible review as JSON</summary>

```json
{
  "case_id": "transmembrane_0100",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "Choice C matches the transmembrane intervals annotated for the exact matching sequence in both the current UniProt record and a historical snapshot. These annotations carry ECO:0000255, indicating computational evidence; they support the key as an annotation-based answer, not as direct experimental confirmation.",
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
    ]
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

## Project source-check notes

These project-authored, AI-assisted checks assess specific source claims. They are not expert adjudication and do not replace Luna’s saved review or the author key.

No additional case-specific project note was recorded. Citation membership checks do not establish that every scientific argument is correct.

## Reviewer-only source evidence

**This source material was supplied only to the reviewer. It was absent from the original evaluated question.** An exact-sequence database match can support a key without establishing that the question can be answered by reasoning from its original input.

**Accession:** `Q6M0N8`; identity was recovered from dataset image-path metadata and was absent from the evaluated model input.  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; selected entry version 82. The exact author source snapshot remains unknown.

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

Question and key: [LiveProteinBench source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json) (zero-based source row 100). Benchmark content © 2026 LiveProteinBench contributors, [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). Cited UniProt / Gene Ontology excerpts retain their own attribution; see [source credits](../THIRD_PARTY_NOTICES.md).
