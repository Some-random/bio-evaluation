# transmembrane_0123

[All 1,736 questions](../README.md) · [Method and limits](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `transmembrane`  
**Author expected answer:** **B** — 31..51; 112..132; 133..153; 179..199; 212..232; 350..370; 378..398; 406..426; 428..448; 475..495

| Expected-answer support | Reasoning versus lookup | Review status |
|---|---|---|
| supported | lookup-dependent | format-valid AI review |

These labels are Luna’s original judgments. Source support and reasoning from the original input are separate questions. The benchmark key and original score are unchanged.

## Complete original question

The sequence and choices below are the complete original user message, in their original order.

```text
[Protein Sequence]
MTGQSAAVEGSNSALPWYRMGFHTLAEFNTYVTFVLLGMSIMMVTSAVTSAPDFVTKYFIYATGDPDAVAETPLFWNNANTFYNAGTYAMQVVTEIASLTPFMRSIPLGIRLFLGLGIPFVELVVIIAVPAATIPTQNGAIAVIMVVAMMGGLSKALCDSCTNALVGPFPTKFMNGAQWGLTVIALFMSIIQIILQVSMGSTFQDVLTISRIYFGIGIGIQVMAIAALVLLRYNPFAQKYIAEFRAAALRRRGHVEPEESQDSKEPATGDVAEAPKAGEKEVTLDAMEEADEVRAVPSDAFVAKSGAVLQATGDADRMVDLDQTKNITSTEQMLRASVWSVFKRIYPMLLCAFTIFFTTLLVFPGVFFLVPARSGWYMTIIVTLFNAGDFVARVLLMIRVLRPSPKLVIVGTFGRLAVIPLIVLCVRGFIPGVALPYVLIFLFGLTNGYFGTMSCIHCPRTPTLHYAGERSVAAMLAGISLMLGLCFGSNMSLAITLTY

[Multiple Choices]
A. 31..51; 112..132; 133..153; 181..199; 212..232; 350..370; 378..398; 406..426; 428..448; 475..495
B. 31..51; 112..132; 133..153; 179..199; 212..232; 350..370; 378..398; 406..426; 428..448; 475..495
C. 31..51; 133..153; 179..199; 212..232; 350..370; 378..398; 406..426; 428..448; 475..495
D. 4..24; 81..101; 116..136; 158..178; 181..201; 228..248; 271..291; 309..329
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

> The sequence exactly matches the historical UniProt record, whose annotated transmembrane intervals correspond to choice B. These intervals are annotated as helical with evidence code ECO:0000255, indicating computational annotation rather than direct experimental determination of each boundary.

Cited evidence: [H6](#evidence-h6), [H7](#evidence-h7), [H8](#evidence-h8), [H9](#evidence-h9), [H10](#evidence-h10), [H11](#evidence-h11), [H12](#evidence-h12), [H13](#evidence-h13), [H14](#evidence-h14), [H15](#evidence-h15).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence contains multiple hydrophobic stretches consistent with membrane-spanning helices, supporting the general prediction of a multipass membrane protein. But this does not resolve the exact annotated boundaries.

**Missing item-specific fact**

> The specific transmembrane-region coordinates for this protein, particularly whether the fourth listed region begins at 179 or 181.

**Reason**

> Choices A and B differ only by a two-residue boundary shift. Sequence hydrophobicity supports a membrane helix there but does not meaningfully distinguish those precise starts; the keyed coordinate depends on protein-specific annotation or equivalent external evidence.

### Question ambiguity

**Multiple defensible options named by Luna:** A, B.

> The 179..199 versus 181..199 alternatives both describe a plausible hydrophobic membrane-spanning segment; the input provides no criterion for choosing the exact boundary.

### Important caveats

- Reviewer-only database evidence supports the key but was not supplied to the evaluated model.
- The cited transmembrane boundary annotations are computational, not direct experimental measurements.

<details>
<summary>Saved visible review as JSON</summary>

```json
{
  "case_id": "transmembrane_0123",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence exactly matches the historical UniProt record, whose annotated transmembrane intervals correspond to choice B. These intervals are annotated as helical with evidence code ECO:0000255, indicating computational annotation rather than direct experimental determination of each boundary.",
    "evidence_ids": [
      "H6",
      "H7",
      "H8",
      "H9",
      "H10",
      "H11",
      "H12",
      "H13",
      "H14",
      "H15"
    ]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence contains multiple hydrophobic stretches consistent with membrane-spanning helices, supporting the general prediction of a multipass membrane protein. But this does not resolve the exact annotated boundaries.",
    "missing_item_specific_fact": "The specific transmembrane-region coordinates for this protein, particularly whether the fourth listed region begins at 179 or 181.",
    "reason": "Choices A and B differ only by a two-residue boundary shift. Sequence hydrophobicity supports a membrane helix there but does not meaningfully distinguish those precise starts; the keyed coordinate depends on protein-specific annotation or equivalent external evidence."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "B"
    ],
    "reason": "The 179..199 versus 181..199 alternatives both describe a plausible hydrophobic membrane-spanning segment; the input provides no criterion for choosing the exact boundary."
  },
  "important_caveats": [
    "Reviewer-only database evidence supports the key but was not supplied to the evaluated model.",
    "The cited transmembrane boundary annotations are computational, not direct experimental measurements."
  ]
}
```

</details>

## Project source-check notes

These project-authored, AI-assisted checks assess specific source claims. They are not expert adjudication and do not replace Luna’s saved review or the author key.

No additional case-specific project note was recorded. Citation membership checks do not establish that every scientific argument is correct.

## Reviewer-only source evidence

**This source material was supplied only to the reviewer. It was absent from the original evaluated question.** An exact-sequence database match can support a key without establishing that the question can be answered by reasoning from its original input.

**Accession:** `Q9NBV4`; identity was recovered from dataset image-path metadata and was absent from the evaluated model input.  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; selected entry version 62. The exact author source snapshot remains unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9NBV4?format=txt&versions=62)  
**Locator:** `lines 145-147`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 62 / 1.  
**Retrieved:** 2026-11-02T04:33:13.069958+00:00.  

```text
FT   TRANSMEM        31..51
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `c6f3ea767f28b291172d1bff1e34f97db01c5d476a90a59f7196e827ba0e0fa9`.

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9NBV4?format=txt&versions=62)  
**Locator:** `lines 148-150`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 62 / 1.  
**Retrieved:** 2026-11-02T04:33:13.069958+00:00.  

```text
FT   TRANSMEM        112..132
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `c6f3ea767f28b291172d1bff1e34f97db01c5d476a90a59f7196e827ba0e0fa9`.

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9NBV4?format=txt&versions=62)  
**Locator:** `lines 151-153`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 62 / 1.  
**Retrieved:** 2026-11-02T04:33:13.069958+00:00.  

```text
FT   TRANSMEM        133..153
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `c6f3ea767f28b291172d1bff1e34f97db01c5d476a90a59f7196e827ba0e0fa9`.

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9NBV4?format=txt&versions=62)  
**Locator:** `lines 154-156`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 62 / 1.  
**Retrieved:** 2026-11-02T04:33:13.069958+00:00.  

```text
FT   TRANSMEM        179..199
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `c6f3ea767f28b291172d1bff1e34f97db01c5d476a90a59f7196e827ba0e0fa9`.

### Evidence H10

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9NBV4?format=txt&versions=62)  
**Locator:** `lines 157-159`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 62 / 1.  
**Retrieved:** 2026-11-02T04:33:13.069958+00:00.  

```text
FT   TRANSMEM        212..232
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `c6f3ea767f28b291172d1bff1e34f97db01c5d476a90a59f7196e827ba0e0fa9`.

### Evidence H11

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9NBV4?format=txt&versions=62)  
**Locator:** `lines 160-162`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 62 / 1.  
**Retrieved:** 2026-11-02T04:33:13.069958+00:00.  

```text
FT   TRANSMEM        350..370
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `c6f3ea767f28b291172d1bff1e34f97db01c5d476a90a59f7196e827ba0e0fa9`.

### Evidence H12

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9NBV4?format=txt&versions=62)  
**Locator:** `lines 163-165`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 62 / 1.  
**Retrieved:** 2026-11-02T04:33:13.069958+00:00.  

```text
FT   TRANSMEM        378..398
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `c6f3ea767f28b291172d1bff1e34f97db01c5d476a90a59f7196e827ba0e0fa9`.

### Evidence H13

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9NBV4?format=txt&versions=62)  
**Locator:** `lines 166-168`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 62 / 1.  
**Retrieved:** 2026-11-02T04:33:13.069958+00:00.  

```text
FT   TRANSMEM        406..426
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `c6f3ea767f28b291172d1bff1e34f97db01c5d476a90a59f7196e827ba0e0fa9`.

### Evidence H14

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9NBV4?format=txt&versions=62)  
**Locator:** `lines 169-171`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 62 / 1.  
**Retrieved:** 2026-11-02T04:33:13.069958+00:00.  

```text
FT   TRANSMEM        428..448
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `c6f3ea767f28b291172d1bff1e34f97db01c5d476a90a59f7196e827ba0e0fa9`.

### Evidence H15

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9NBV4?format=txt&versions=62)  
**Locator:** `lines 172-174`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 62 / 1.  
**Retrieved:** 2026-11-02T04:33:13.069958+00:00.  

```text
FT   TRANSMEM        475..495
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `c6f3ea767f28b291172d1bff1e34f97db01c5d476a90a59f7196e827ba0e0fa9`.

---

Question and key: [LiveProteinBench source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json) (zero-based source row 123). Benchmark content © 2026 LiveProteinBench contributors, [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). Cited UniProt / Gene Ontology excerpts retain their own attribution; see [source credits](../THIRD_PARTY_NOTICES.md).
