# transmembrane_0086

[All 1,736 questions](../README.md) · [Method and limits](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `transmembrane`  
**Author expected answer:** **D** — 306..326; 333..353; 355..375; 466..486

| Expected-answer support | Reasoning versus lookup | Review status |
|---|---|---|
| supported | lookup-dependent | format-valid AI review |

These labels are Luna’s original judgments. Source support and reasoning from the original input are separate questions. The benchmark key and original score are unchanged.

## Complete original question

The sequence and choices below are the complete original user message, in their original order.

```text
[Protein Sequence]
MATTLTPTQRYAAGALLALALRQAQIHQSVLLGAHHHHDDDDEEQGRTSTSSGGGGGSSSSSSNSGAGADADLWTHDSHGLLRPVFRFLEIDPKAWSGLEETAASSEAKHHIGAFLRIIFEEDGESSSDRSVQELALAKGVDVMVMSLGNDSEVGNTIKGGDQDALPSSSGTDKSPGESSHDDQLGINKLTLDDIPANNHRKMALLFALLSACVADKPVSQEEEDRKSTRFRKGYDARHRVALRLLSTWLDVKWIKMEAIEVMVACSAMAAAKEQEQSQESASPKSKWEKWKRGGIIGAAALTGGALLAITGGLAAPAIAAGFGALAPTLGTLVPVIGASGFAAMATAAGSVAGSVAVAASFGAAGAGLTGSKMARRIGSVKEFEFKPIGENHNQGRLAVGILISGFAFDEDDFCRPWEGWQDNLERYILQWESKHIIAVSTAIQDWLTSRLAMELMKQGAMRTVLSGLLAAFAWPATLLAATDFIDSKWSVAIDRSDKAGKMLAEVLLKGLQGNRPVTLIGFSLGARVIFKCLQELALSSDNEGLVERVVLLGAPVSVKGERWEAARKMVAGRFVNVYSTDDWILGVTFRASLLTQGLAGIQAIDVPGVENVDVTELVDGHSSYLSAAQQILEHLELNTYYPVFVPLSAANEETDGTVAQ

[Multiple Choices]
A. 30..50; 62..82; 108..128; 144..164; 186..206; 327..347; 357..377
B. 306..326; 333..353; 466..486
C. 306..326; 333..353; 356..372; 466..486
D. 306..326; 333..353; 355..375; 466..486
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

> The sequence-matched UniProt annotation lists transmembrane regions 306..326, 333..353, 355..375, and 466..486, matching choice D. These are computationally supported annotations (ECO:0000255), not evidence here of experimental boundary measurements.

Cited evidence: [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6), [H7](#evidence-h7), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> Hydrophobic sequence stretches support the general inference that membrane-spanning helices occur in these regions, but they do not uniquely establish the precise annotated boundaries, especially for the highly hydrophobic region represented as 355..375 in D versus 356..372 in C.

**Missing item-specific fact**

> The protein-specific transmembrane feature annotations, including their exact start and end coordinates, are not supplied in the question.

**Reason**

> Choosing the exact listed coordinates depends on protein-specific boundary assignments absent from the input; sequence hydropathy can support a prediction but does not distinguish these near-nested boundaries reliably.

### Question ambiguity

**Multiple defensible options named by Luna:** C, D.

> Both choices include the same other listed regions, and the 356..372 segment in C is a hydrophobic subset of D's 355..375 region. The question does not specify that coordinates must match a particular annotation source or boundary convention.

### Important caveats

- The supporting UniProt evidence is computationally annotated and applies to the exact supplied sequence; it does not establish experimental validation of each boundary.
- The reviewer-only accession and database annotations were not supplied to the evaluated model.

<details>
<summary>Saved visible review as JSON</summary>

```json
{
  "case_id": "transmembrane_0086",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation lists transmembrane regions 306..326, 333..353, 355..375, and 466..486, matching choice D. These are computationally supported annotations (ECO:0000255), not evidence here of experimental boundary measurements.",
    "evidence_ids": [
      "H4",
      "H5",
      "H6",
      "H7",
      "C5",
      "C6",
      "C7",
      "C8"
    ]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "Hydrophobic sequence stretches support the general inference that membrane-spanning helices occur in these regions, but they do not uniquely establish the precise annotated boundaries, especially for the highly hydrophobic region represented as 355..375 in D versus 356..372 in C.",
    "missing_item_specific_fact": "The protein-specific transmembrane feature annotations, including their exact start and end coordinates, are not supplied in the question.",
    "reason": "Choosing the exact listed coordinates depends on protein-specific boundary assignments absent from the input; sequence hydropathy can support a prediction but does not distinguish these near-nested boundaries reliably."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [
      "C",
      "D"
    ],
    "reason": "Both choices include the same other listed regions, and the 356..372 segment in C is a hydrophobic subset of D's 355..375 region. The question does not specify that coordinates must match a particular annotation source or boundary convention."
  },
  "important_caveats": [
    "The supporting UniProt evidence is computationally annotated and applies to the exact supplied sequence; it does not establish experimental validation of each boundary.",
    "The reviewer-only accession and database annotations were not supplied to the evaluated model."
  ]
}
```

</details>

## Project source-check notes

These project-authored, AI-assisted checks assess specific source claims. They are not expert adjudication and do not replace Luna’s saved review or the author key.

No additional case-specific project note was recorded. Citation membership checks do not establish that every scientific argument is correct.

## Reviewer-only source evidence

**This source material was supplied only to the reviewer. It was absent from the original evaluated question.** An exact-sequence database match can support a key without establishing that the question can be answered by reasoning from its original input.

**Accession:** `Q10SS2`; identity was recovered from dataset image-path metadata and was absent from the evaluated model input.  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; selected entry version 121. The exact author source snapshot remains unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q10SS2.json)  
**Locator:** `/features/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:29.234158+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":326},"start":{"modifier":"EXACT","value":306}},"type":"Transmembrane"}
```

Source SHA-256: `0a6a8d6a3c909a1dbd7c765a1a1d325767f551df7a3b5795f41c6d5c449c4e27`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q10SS2.json)  
**Locator:** `/features/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:29.234158+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":353},"start":{"modifier":"EXACT","value":333}},"type":"Transmembrane"}
```

Source SHA-256: `0a6a8d6a3c909a1dbd7c765a1a1d325767f551df7a3b5795f41c6d5c449c4e27`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q10SS2.json)  
**Locator:** `/features/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:29.234158+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":375},"start":{"modifier":"EXACT","value":355}},"type":"Transmembrane"}
```

Source SHA-256: `0a6a8d6a3c909a1dbd7c765a1a1d325767f551df7a3b5795f41c6d5c449c4e27`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q10SS2.json)  
**Locator:** `/features/4`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:29.234158+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":486},"start":{"modifier":"EXACT","value":466}},"type":"Transmembrane"}
```

Source SHA-256: `0a6a8d6a3c909a1dbd7c765a1a1d325767f551df7a3b5795f41c6d5c449c4e27`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q10SS2?format=txt&versions=121)  
**Locator:** `lines 178-180`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 121 / 1.  
**Retrieved:** 2026-11-02T04:30:34.944114+00:00.  

```text
FT   TRANSMEM        306..326
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `acc4e547beb155cdd1e60fb276d5cc6296693b0794b6f3a69d9c2d66a4f46eda`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q10SS2?format=txt&versions=121)  
**Locator:** `lines 181-183`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 121 / 1.  
**Retrieved:** 2026-11-02T04:30:34.944114+00:00.  

```text
FT   TRANSMEM        333..353
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `acc4e547beb155cdd1e60fb276d5cc6296693b0794b6f3a69d9c2d66a4f46eda`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q10SS2?format=txt&versions=121)  
**Locator:** `lines 184-186`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 121 / 1.  
**Retrieved:** 2026-11-02T04:30:34.944114+00:00.  

```text
FT   TRANSMEM        355..375
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `acc4e547beb155cdd1e60fb276d5cc6296693b0794b6f3a69d9c2d66a4f46eda`.

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q10SS2?format=txt&versions=121)  
**Locator:** `lines 187-189`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 121 / 1.  
**Retrieved:** 2026-11-02T04:30:34.944114+00:00.  

```text
FT   TRANSMEM        466..486
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `acc4e547beb155cdd1e60fb276d5cc6296693b0794b6f3a69d9c2d66a4f46eda`.

---

Question and key: [LiveProteinBench source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json) (zero-based source row 86). Benchmark content © 2026 LiveProteinBench contributors, [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). Cited UniProt / Gene Ontology excerpts retain their own attribution; see [source credits](../THIRD_PARTY_NOTICES.md).
