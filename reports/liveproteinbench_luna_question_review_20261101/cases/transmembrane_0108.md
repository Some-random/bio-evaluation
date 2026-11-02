# transmembrane_0108

[All 1,736 questions](../README.md) · [Method and limits](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `transmembrane`  
**Author expected answer:** **D** — 58..78; 89..109; 122..142; 146..166; 192..212; 216..236; 266..286; 300..320; 326..346; 352..372; 405..425; 431..451

| Expected-answer support | Reasoning versus lookup | Review status |
|---|---|---|
| supported | lookup-dependent | format-valid AI review |

These labels are Luna’s original judgments. Source support and reasoning from the original input are separate questions. The benchmark key and original score are unchanged.

## Complete original question

The sequence and choices below are the complete original user message, in their original order.

```text
[Protein Sequence]
MEDDDFSIKDKKENYETCSTETISSYISINEKCQLIEKDINDDNHENPYMIFNKISSSLIAMLQGVEVLCNLSIIYLLKDNYHLHPASLSIVMCFIKIPWSIKLVWAVISDNYPIFGYRRKYYLLLGSFLCILSLICLGLITHNNLFITILLLFIYFFGSSLCNVIGEAQVVESNRNCSINSSARNVSLFFAFRKLSFAIMSYLSGYLLLLISKKHIFLIGSFLPICVFTSGFFIIEKRNYTKSSIKDQIKCIYSIIKLSYLKNFIIFIFIMMSTPSCGNTLFFYITNELKFSPNLLGKMAMFQSLASFISIISYMLFFTKIDIRKLLLYSTIIITPFCLLPLVVIKKVNYFLFIPNTLFFITDTVLIEFIAEFQTMPILVLCSRLIPEGFESTIYSLLLSSNNFASIISSFLSSLLTYSLNITSTNFTNLPYMIIICCLTNIIPIFFLYILPNHSQKKNLQHSNSHTQKYYSYPSTDYISSQKSDSSEITKFSADMQIDDITLE

[Multiple Choices]
A. 58..78; 89..109; 122..142; 146..166; 192..212; 216..236; 266..286; 300..320; 326..346; 405..425; 431..451
B. 58..78; 89..109; 122..142; 146..166; 192..212; 216..236; 266..286; 300..320; 326..346; 352..372; 400..427; 431..451
C. 27..47; 78..98; 108..128; 136..156; 173..193; 209..229; 337..357; 366..386; 400..420; 432..452; 465..485
D. 58..78; 89..109; 122..142; 146..166; 192..212; 216..236; 266..286; 300..320; 326..346; 352..372; 405..425; 431..451
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

> The sequence matches the UniProt record, whose historical and current annotations list the twelve transmembrane intervals in D. These are annotated as helical features with evidence code ECO:0000255, indicating computational annotation rather than direct experimental measurement.

Cited evidence: [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [C9](#evidence-c9), [C10](#evidence-c10), [C11](#evidence-c11), [C12](#evidence-c12), [C13](#evidence-c13), [C14](#evidence-c14), [C15](#evidence-c15), [C16](#evidence-c16), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6), [H7](#evidence-h7), [H8](#evidence-h8), [H9](#evidence-h9), [H10](#evidence-h10), [H11](#evidence-h11), [H12](#evidence-h12), [H13](#evidence-h13), [H14](#evidence-h14).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence contains many hydrophobic stretches, which supports a multi-pass membrane-protein interpretation and can help locate likely membrane-spanning helices. It does not independently establish the exact annotated boundaries needed to distinguish the options.

**Missing item-specific fact**

> The protein-specific set of annotated transmembrane intervals, especially the inclusion of 352..372 and the precise 405..425 interval rather than the shifted 400..427 interval.

**Reason**

> Choosing the keyed option requires protein-specific interval annotations or equivalent external evidence. General hydrophobicity reasoning can suggest candidate helices but does not reliably determine these precise boundaries.

### Question ambiguity

**Multiple defensible options named by Luna:** B, D.

> B and D differ at the final long helix: 400..427 versus 405..425. Both describe a plausible membrane-spanning region at sequence-level resolution, although only D matches the cited UniProt annotation.

### Important caveats

- The supporting transmembrane features are computational annotations, not evidence of experimentally measured boundaries.
- The current and archived records match the supplied sequence; the author's exact source snapshot is unknown.

<details>
<summary>Saved visible review as JSON</summary>

```json
{
  "case_id": "transmembrane_0108",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches the UniProt record, whose historical and current annotations list the twelve transmembrane intervals in D. These are annotated as helical features with evidence code ECO:0000255, indicating computational annotation rather than direct experimental measurement.",
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
    ]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence contains many hydrophobic stretches, which supports a multi-pass membrane-protein interpretation and can help locate likely membrane-spanning helices. It does not independently establish the exact annotated boundaries needed to distinguish the options.",
    "missing_item_specific_fact": "The protein-specific set of annotated transmembrane intervals, especially the inclusion of 352..372 and the precise 405..425 interval rather than the shifted 400..427 interval.",
    "reason": "Choosing the keyed option requires protein-specific interval annotations or equivalent external evidence. General hydrophobicity reasoning can suggest candidate helices but does not reliably determine these precise boundaries."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "D"
    ],
    "reason": "B and D differ at the final long helix: 400..427 versus 405..425. Both describe a plausible membrane-spanning region at sequence-level resolution, although only D matches the cited UniProt annotation."
  },
  "important_caveats": [
    "The supporting transmembrane features are computational annotations, not evidence of experimentally measured boundaries.",
    "The current and archived records match the supplied sequence; the author's exact source snapshot is unknown."
  ]
}
```

</details>

## Project source-check notes

These project-authored, AI-assisted checks assess specific source claims. They are not expert adjudication and do not replace Luna’s saved review or the author key.

No additional case-specific project note was recorded. Citation membership checks do not establish that every scientific argument is correct.

## Reviewer-only source evidence

**This source material was supplied only to the reviewer. It was absent from the original evaluated question.** An exact-sequence database match can support a key without establishing that the question can be answered by reasoning from its original input.

**Accession:** `Q8IBB7`; identity was recovered from dataset image-path metadata and was absent from the evaluated model input.  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; selected entry version 98. The exact author source snapshot remains unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IBB7.json)  
**Locator:** `/features/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:06.455529+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":78},"start":{"modifier":"EXACT","value":58}},"type":"Transmembrane"}
```

Source SHA-256: `f181b4dbb2ac2ea55eb60db5ac65720a1ffcd9dd3096b131edc4a79c0f2331cd`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IBB7.json)  
**Locator:** `/features/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:06.455529+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":109},"start":{"modifier":"EXACT","value":89}},"type":"Transmembrane"}
```

Source SHA-256: `f181b4dbb2ac2ea55eb60db5ac65720a1ffcd9dd3096b131edc4a79c0f2331cd`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IBB7.json)  
**Locator:** `/features/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:06.455529+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":142},"start":{"modifier":"EXACT","value":122}},"type":"Transmembrane"}
```

Source SHA-256: `f181b4dbb2ac2ea55eb60db5ac65720a1ffcd9dd3096b131edc4a79c0f2331cd`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IBB7.json)  
**Locator:** `/features/4`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:06.455529+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":166},"start":{"modifier":"EXACT","value":146}},"type":"Transmembrane"}
```

Source SHA-256: `f181b4dbb2ac2ea55eb60db5ac65720a1ffcd9dd3096b131edc4a79c0f2331cd`.

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IBB7.json)  
**Locator:** `/features/5`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:06.455529+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":212},"start":{"modifier":"EXACT","value":192}},"type":"Transmembrane"}
```

Source SHA-256: `f181b4dbb2ac2ea55eb60db5ac65720a1ffcd9dd3096b131edc4a79c0f2331cd`.

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IBB7.json)  
**Locator:** `/features/6`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:06.455529+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":236},"start":{"modifier":"EXACT","value":216}},"type":"Transmembrane"}
```

Source SHA-256: `f181b4dbb2ac2ea55eb60db5ac65720a1ffcd9dd3096b131edc4a79c0f2331cd`.

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IBB7.json)  
**Locator:** `/features/7`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:06.455529+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":286},"start":{"modifier":"EXACT","value":266}},"type":"Transmembrane"}
```

Source SHA-256: `f181b4dbb2ac2ea55eb60db5ac65720a1ffcd9dd3096b131edc4a79c0f2331cd`.

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IBB7.json)  
**Locator:** `/features/8`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:06.455529+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":320},"start":{"modifier":"EXACT","value":300}},"type":"Transmembrane"}
```

Source SHA-256: `f181b4dbb2ac2ea55eb60db5ac65720a1ffcd9dd3096b131edc4a79c0f2331cd`.

### Evidence C13

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IBB7.json)  
**Locator:** `/features/9`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:06.455529+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":346},"start":{"modifier":"EXACT","value":326}},"type":"Transmembrane"}
```

Source SHA-256: `f181b4dbb2ac2ea55eb60db5ac65720a1ffcd9dd3096b131edc4a79c0f2331cd`.

### Evidence C14

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IBB7.json)  
**Locator:** `/features/10`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:06.455529+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":372},"start":{"modifier":"EXACT","value":352}},"type":"Transmembrane"}
```

Source SHA-256: `f181b4dbb2ac2ea55eb60db5ac65720a1ffcd9dd3096b131edc4a79c0f2331cd`.

### Evidence C15

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IBB7.json)  
**Locator:** `/features/11`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:06.455529+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":425},"start":{"modifier":"EXACT","value":405}},"type":"Transmembrane"}
```

Source SHA-256: `f181b4dbb2ac2ea55eb60db5ac65720a1ffcd9dd3096b131edc4a79c0f2331cd`.

### Evidence C16

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IBB7.json)  
**Locator:** `/features/12`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:06.455529+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":451},"start":{"modifier":"EXACT","value":431}},"type":"Transmembrane"}
```

Source SHA-256: `f181b4dbb2ac2ea55eb60db5ac65720a1ffcd9dd3096b131edc4a79c0f2331cd`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IBB7?format=txt&versions=98)  
**Locator:** `lines 110-112`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 98 / 1.  
**Retrieved:** 2026-11-02T04:32:10.640562+00:00.  

```text
FT   TRANSMEM        58..78
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `23128f941b579a9921cbe78a9e91da7734842a0f3c2311d1bf182aed647224f0`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IBB7?format=txt&versions=98)  
**Locator:** `lines 113-115`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 98 / 1.  
**Retrieved:** 2026-11-02T04:32:10.640562+00:00.  

```text
FT   TRANSMEM        89..109
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `23128f941b579a9921cbe78a9e91da7734842a0f3c2311d1bf182aed647224f0`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IBB7?format=txt&versions=98)  
**Locator:** `lines 116-118`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 98 / 1.  
**Retrieved:** 2026-11-02T04:32:10.640562+00:00.  

```text
FT   TRANSMEM        122..142
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `23128f941b579a9921cbe78a9e91da7734842a0f3c2311d1bf182aed647224f0`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IBB7?format=txt&versions=98)  
**Locator:** `lines 119-121`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 98 / 1.  
**Retrieved:** 2026-11-02T04:32:10.640562+00:00.  

```text
FT   TRANSMEM        146..166
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `23128f941b579a9921cbe78a9e91da7734842a0f3c2311d1bf182aed647224f0`.

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IBB7?format=txt&versions=98)  
**Locator:** `lines 122-124`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 98 / 1.  
**Retrieved:** 2026-11-02T04:32:10.640562+00:00.  

```text
FT   TRANSMEM        192..212
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `23128f941b579a9921cbe78a9e91da7734842a0f3c2311d1bf182aed647224f0`.

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IBB7?format=txt&versions=98)  
**Locator:** `lines 125-127`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 98 / 1.  
**Retrieved:** 2026-11-02T04:32:10.640562+00:00.  

```text
FT   TRANSMEM        216..236
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `23128f941b579a9921cbe78a9e91da7734842a0f3c2311d1bf182aed647224f0`.

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IBB7?format=txt&versions=98)  
**Locator:** `lines 128-130`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 98 / 1.  
**Retrieved:** 2026-11-02T04:32:10.640562+00:00.  

```text
FT   TRANSMEM        266..286
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `23128f941b579a9921cbe78a9e91da7734842a0f3c2311d1bf182aed647224f0`.

### Evidence H10

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IBB7?format=txt&versions=98)  
**Locator:** `lines 131-133`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 98 / 1.  
**Retrieved:** 2026-11-02T04:32:10.640562+00:00.  

```text
FT   TRANSMEM        300..320
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `23128f941b579a9921cbe78a9e91da7734842a0f3c2311d1bf182aed647224f0`.

### Evidence H11

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IBB7?format=txt&versions=98)  
**Locator:** `lines 134-136`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 98 / 1.  
**Retrieved:** 2026-11-02T04:32:10.640562+00:00.  

```text
FT   TRANSMEM        326..346
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `23128f941b579a9921cbe78a9e91da7734842a0f3c2311d1bf182aed647224f0`.

### Evidence H12

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IBB7?format=txt&versions=98)  
**Locator:** `lines 137-139`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 98 / 1.  
**Retrieved:** 2026-11-02T04:32:10.640562+00:00.  

```text
FT   TRANSMEM        352..372
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `23128f941b579a9921cbe78a9e91da7734842a0f3c2311d1bf182aed647224f0`.

### Evidence H13

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IBB7?format=txt&versions=98)  
**Locator:** `lines 140-142`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 98 / 1.  
**Retrieved:** 2026-11-02T04:32:10.640562+00:00.  

```text
FT   TRANSMEM        405..425
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `23128f941b579a9921cbe78a9e91da7734842a0f3c2311d1bf182aed647224f0`.

### Evidence H14

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IBB7?format=txt&versions=98)  
**Locator:** `lines 143-145`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 98 / 1.  
**Retrieved:** 2026-11-02T04:32:10.640562+00:00.  

```text
FT   TRANSMEM        431..451
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `23128f941b579a9921cbe78a9e91da7734842a0f3c2311d1bf182aed647224f0`.

---

Question and key: [LiveProteinBench source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json) (zero-based source row 108). Benchmark content © 2026 LiveProteinBench contributors, [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). Cited UniProt / Gene Ontology excerpts retain their own attribution; see [source credits](../THIRD_PARTY_NOTICES.md).
