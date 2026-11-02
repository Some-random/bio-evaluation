# transmembrane_0022

[All 1,736 questions](../README.md) · [Method and limits](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `transmembrane`  
**Author expected answer:** **B** — 12..32; 181..201; 220..240; 244..264; 285..305; 312..332; 346..366; 398..418

| Expected-answer support | Reasoning versus lookup | Review status |
|---|---|---|
| supported | lookup-dependent | format-valid AI review |

These labels are Luna’s original judgments. Source support and reasoning from the original input are separate questions. The benchmark key and original score are unchanged.

## Complete original question

The sequence and choices below are the complete original user message, in their original order.

```text
[Protein Sequence]
MIIDLFQSKKLIISIIILILRISLFSCAEHLFFNNNFNFFNFSENNHAKVNELNIDTKYLYQGLRNINIYLALSALNGITKEKINDISQWNGYKTRNNDETNISNVVVTEWKQLNKKSFFLKNNNISNNDNLIKGMPNPYFINSLTEDINNINLYFNIRNDIKYGEIIYKGTYIPHIYNNIFLIFLISYMYWFCIKILFNGYIKGKYVAKEYILKISTLFIFFVILKISLIFLPAILSCIVCLILTFYFYSISMSPCKDIFYLFESTRIKKEPIGWIIIVYAESILIGNVIYNFLCPPKIIIIFIRYIQNDFLVKIICLTIILFISFLIFFLMISNIFPAKKAQNFVFSFTSSYLIVSCFAYFWNIFLLRFLNNTNIFQIEPIMFFSYTPKFVFNRQNMFALFMIFAMSILSIIFPRIKKLKQNIFDMKENIYDSDIDIGKASKNRYNIILNYFT

[Multiple Choices]
A. 12..32; 181..201; 220..240; 249..261; 285..305; 312..332; 346..366; 398..418
B. 12..32; 181..201; 220..240; 244..264; 285..305; 312..332; 346..366; 398..418
C. 6..26
D. 12..32; 181..201; 220..240; 285..305; 312..332; 346..366; 398..418
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

> The sequence-matched historical UniProt entry annotates the eight spans listed in B, including 244..264. These are computationally supported annotations (ECO:0000255), not evidence of experimental boundary measurement.

Cited evidence: [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6), [H7](#evidence-h7), [H8](#evidence-h8), [H9](#evidence-h9), [H10](#evidence-h10).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence contains multiple hydrophobic stretches consistent with transmembrane helices, but that general pattern does not establish the precise annotated boundaries or uniquely resolve the 244..264 interval versus the shorter 249..261 alternative.

**Missing item-specific fact**

> The protein-specific transmembrane annotation giving the span 244..264 and the remaining listed coordinates.

**Reason**

> Selecting B's exact coordinate set depends on protein-specific boundary annotations absent from the input. The sequence supports a multipass membrane-protein prediction, but does not independently establish those precise boundaries.

### Question ambiguity

**Multiple defensible options named by Luna:** none.

> B matches the sequence-matched annotated coordinate set. The shorter interval in A lies within the hydrophobic region but is not an equally supported complete membrane-spanning segment.

### Important caveats

- The cited historical UniProt record matches the supplied sequence, but the author's exact source snapshot is unknown.
- The transmembrane features carry computational evidence; this supports the key as an annotation, not as experimentally verified boundaries.

<details>
<summary>Saved visible review as JSON</summary>

```json
{
  "case_id": "transmembrane_0022",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched historical UniProt entry annotates the eight spans listed in B, including 244..264. These are computationally supported annotations (ECO:0000255), not evidence of experimental boundary measurement.",
    "evidence_ids": [
      "H3",
      "H4",
      "H5",
      "H6",
      "H7",
      "H8",
      "H9",
      "H10"
    ]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence contains multiple hydrophobic stretches consistent with transmembrane helices, but that general pattern does not establish the precise annotated boundaries or uniquely resolve the 244..264 interval versus the shorter 249..261 alternative.",
    "missing_item_specific_fact": "The protein-specific transmembrane annotation giving the span 244..264 and the remaining listed coordinates.",
    "reason": "Selecting B's exact coordinate set depends on protein-specific boundary annotations absent from the input. The sequence supports a multipass membrane-protein prediction, but does not independently establish those precise boundaries."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "B matches the sequence-matched annotated coordinate set. The shorter interval in A lies within the hydrophobic region but is not an equally supported complete membrane-spanning segment."
  },
  "important_caveats": [
    "The cited historical UniProt record matches the supplied sequence, but the author's exact source snapshot is unknown.",
    "The transmembrane features carry computational evidence; this supports the key as an annotation, not as experimentally verified boundaries."
  ]
}
```

</details>

## Project source-check notes

These project-authored, AI-assisted checks assess specific source claims. They are not expert adjudication and do not replace Luna’s saved review or the author key.

No additional case-specific project note was recorded. Citation membership checks do not establish that every scientific argument is correct.

## Reviewer-only source evidence

**This source material was supplied only to the reviewer. It was absent from the original evaluated question.** An exact-sequence database match can support a key without establishing that the question can be answered by reasoning from its original input.

**Accession:** `A0A509AKT6`; identity was recovered from dataset image-path metadata and was absent from the evaluated model input.  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; selected entry version 19. The exact author source snapshot remains unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A509AKT6?format=txt&versions=19)  
**Locator:** `lines 82-84`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 19 / 1.  
**Retrieved:** 2026-11-02T04:25:27.030552+00:00.  

```text
FT   TRANSMEM        12..32
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `6d40908ee73c41ed5a2c9670ef889cabc4ff6bd15769a8b8824958da5cb4a8f5`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A509AKT6?format=txt&versions=19)  
**Locator:** `lines 85-87`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 19 / 1.  
**Retrieved:** 2026-11-02T04:25:27.030552+00:00.  

```text
FT   TRANSMEM        181..201
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `6d40908ee73c41ed5a2c9670ef889cabc4ff6bd15769a8b8824958da5cb4a8f5`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A509AKT6?format=txt&versions=19)  
**Locator:** `lines 88-90`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 19 / 1.  
**Retrieved:** 2026-11-02T04:25:27.030552+00:00.  

```text
FT   TRANSMEM        220..240
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `6d40908ee73c41ed5a2c9670ef889cabc4ff6bd15769a8b8824958da5cb4a8f5`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A509AKT6?format=txt&versions=19)  
**Locator:** `lines 91-93`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 19 / 1.  
**Retrieved:** 2026-11-02T04:25:27.030552+00:00.  

```text
FT   TRANSMEM        244..264
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `6d40908ee73c41ed5a2c9670ef889cabc4ff6bd15769a8b8824958da5cb4a8f5`.

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A509AKT6?format=txt&versions=19)  
**Locator:** `lines 94-96`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 19 / 1.  
**Retrieved:** 2026-11-02T04:25:27.030552+00:00.  

```text
FT   TRANSMEM        285..305
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `6d40908ee73c41ed5a2c9670ef889cabc4ff6bd15769a8b8824958da5cb4a8f5`.

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A509AKT6?format=txt&versions=19)  
**Locator:** `lines 97-99`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 19 / 1.  
**Retrieved:** 2026-11-02T04:25:27.030552+00:00.  

```text
FT   TRANSMEM        312..332
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `6d40908ee73c41ed5a2c9670ef889cabc4ff6bd15769a8b8824958da5cb4a8f5`.

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A509AKT6?format=txt&versions=19)  
**Locator:** `lines 100-102`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 19 / 1.  
**Retrieved:** 2026-11-02T04:25:27.030552+00:00.  

```text
FT   TRANSMEM        346..366
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `6d40908ee73c41ed5a2c9670ef889cabc4ff6bd15769a8b8824958da5cb4a8f5`.

### Evidence H10

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A509AKT6?format=txt&versions=19)  
**Locator:** `lines 103-105`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 19 / 1.  
**Retrieved:** 2026-11-02T04:25:27.030552+00:00.  

```text
FT   TRANSMEM        398..418
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `6d40908ee73c41ed5a2c9670ef889cabc4ff6bd15769a8b8824958da5cb4a8f5`.

---

Question and key: [LiveProteinBench source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json) (zero-based source row 22). Benchmark content © 2026 LiveProteinBench contributors, [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). Cited UniProt / Gene Ontology excerpts retain their own attribution; see [source credits](../THIRD_PARTY_NOTICES.md).
