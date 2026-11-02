# transmembrane_0092

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `transmembrane`  
**Author expected answer:** **D** — 6..26; 300..320; 337..357; 373..393; 416..436; 439..459

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MGLTDIFLNLLLFVYPAVFIIYQIILYEISARKQINQEALKYSNLPVLSIIVPIKNEEISVIQGLLDNLSNLIWDKKKLEIIIVSDDNEDYFTKIINTVKVPKDLTVYFYRREKKLGYKSGALQYGFEKATGDLILTIDVDSRLPPNALINAYEKMQSNTCDAIVFQWNGYSSNQYSTLAKGMVVSTLFASKALFEGKEKLKLKIYPVGSGTMFSREALRVVNGWDYRLVQDDLEIGTRLIYNGKNVCASGIPIYVEVPDNFYSFYVQQTRWAMGSAEVLRNRLKYIIKSKISFTQRMDLIIYLLQYTPVIVTFFISTLLSLMLPFRIGHDPLNSPALLFWLVSLGLYASLLLSLALKLGLNLKDSLMGIGRLTAFTVSISPFIVFNFFKGLLKSGNTYVITPKGTVKKTNKLLRIIAIIGVFGLLYLLSSILYIYEGYYVTGIWLLYYSSAYLYTMLLYYKEL

[Multiple Choices]
A. 6..26; 300..320; 337..357; 372..388; 416..436; 439..459
B. 6..26; 337..357; 373..393; 416..436; 439..459
C. 1..21
D. 6..26; 300..320; 337..357; 373..393; 416..436; 439..459
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

> The sequence matches the archived UniProt record, whose transmembrane annotations give all six intervals in choice D. These annotations carry ECO:0000255, indicating computational support rather than experimental confirmation.

Citations as saved: [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6), [H7](#evidence-h7).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence contains several strongly hydrophobic stretches consistent with membrane-spanning helices, which supports identifying approximate regions and disfavors options that omit obvious candidates.


**Missing item-specific fact**

> The exact annotated boundaries, especially the choice between 373..393 and the overlapping 372..388 interval, are not established by the input.


**Reason**

> Sequence hydrophobicity provides useful evidence for likely transmembrane regions, but it does not uniquely resolve the closely overlapping boundary choices. Selecting the annotation-exact answer depends on protein-specific coordinates absent from the question.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "D"
]
```

> Both choices include the same set of approximate hydrophobic regions; A's 372..388 interval overlaps the likely membrane-spanning helix in D. The supplied sequence does not clearly establish the exact endpoint difference.


### Important caveats

- The supporting UniProt annotation is computational, not evidence of experimental determination.
- The archived record matches the sequence, but the author's exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains several strongly hydrophobic stretches consistent with membrane-spanning helices, which supports identifying approximate regions and disfavors options that omit obvious candidates.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The exact annotated boundaries, especially the choice between 373..393 and the overlapping 372..388 interval, are not established by the input.",
    "reason": "Sequence hydrophobicity provides useful evidence for likely transmembrane regions, but it does not uniquely resolve the closely overlapping boundary choices. Selecting the annotation-exact answer depends on protein-specific coordinates absent from the question."
  },
  "case_id": "transmembrane_0092",
  "expected_answer_check": {
    "evidence_ids": [
      "H2",
      "H3",
      "H4",
      "H5",
      "H6",
      "H7"
    ],
    "judgment": "supported",
    "reason": "The sequence matches the archived UniProt record, whose transmembrane annotations give all six intervals in choice D. These annotations carry ECO:0000255, indicating computational support rather than experimental confirmation."
  },
  "important_caveats": [
    "The supporting UniProt annotation is computational, not evidence of experimental determination.",
    "The archived record matches the sequence, but the author's exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "D"
    ],
    "reason": "Both choices include the same set of approximate hydrophobic regions; A's 372..388 interval overlaps the likely membrane-spanning helix in D. The supplied sequence does not clearly establish the exact endpoint difference."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0092",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches the archived UniProt record, whose transmembrane annotations give all six intervals in choice D. These annotations carry ECO:0000255, indicating computational support rather than experimental confirmation.",
    "evidence_ids": ["H2", "H3", "H4", "H5", "H6", "H7"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence contains several strongly hydrophobic stretches consistent with membrane-spanning helices, which supports identifying approximate regions and disfavors options that omit obvious candidates.",
    "missing_item_specific_fact": "The exact annotated boundaries, especially the choice between 373..393 and the overlapping 372..388 interval, are not established by the input.",
    "reason": "Sequence hydrophobicity provides useful evidence for likely transmembrane regions, but it does not uniquely resolve the closely overlapping boundary choices. Selecting the annotation-exact answer depends on protein-specific coordinates absent from the question."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "D"],
    "reason": "Both choices include the same set of approximate hydrophobic regions; A's 372..388 interval overlaps the likely membrane-spanning helix in D. The supplied sequence does not clearly establish the exact endpoint difference."
  },
  "important_caveats": [
    "The supporting UniProt annotation is computational, not evidence of experimental determination.",
    "The archived record matches the sequence, but the author's exact source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt annotation for Q4J8Q7 (sequence matched, 464 AA) lists exactly six transmembrane helical regions: 6..26, 300..320, 337..357, 373..393, 416..436, 439..459, all annotated with ECO:0000255 (inferred by similarity). Choice D matches these six regions exactly. The historical entry (v83) confirms the same boundaries. The sequence SHA256 matches the benchmark input.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [C9](#evidence-c9), [C10](#evidence-c10), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6), [H7](#evidence-h7).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> A model could potentially identify the approximate number of hydrophobic stretches (e.g., 6 vs 5 vs 1) and roughly locate them by hydrophobicity scanning, which would eliminate C (single TM, wrong start) and possibly B (missing the 300..320 region). However, the critical distinction between A (372..388) and D (373..393) involves a 1-residue shift at the N-terminus and a 5-residue extension at the C-terminus of one helix. These boundaries fall well within the uncertainty envelope of any computational TM predictor and cannot be resolved by general hydrophobicity reasoning, helix-propensity analysis, or knowledge of membrane biology. The annotations themselves carry ECO:0000255 (similarity-based inference), confirming they are algorithmic outputs with inherent positional noise.


**Missing item-specific fact**

> The exact boundary coordinates assigned by the specific prediction pipeline used in the UniProt annotation (e.g., whether the helix at ~373 starts at 372 or 373, and whether it ends at 388 or 393). No general biological principle distinguishes 372..388 from 373..393 for this particular sequence.


**Reason**

> While the gross TM topology (number and approximate location of helices) is inferable from hydrophobicity, the exact residue-level boundaries that distinguish A from D (and to some extent B from D regarding the 300..320 region) depend on the output of a particular computational predictor recorded in the database. No biological argument from the sequence alone can justify choosing 393 over 388 as the C-terminal boundary of the fourth TM helix.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "D"
]
```

> Options A and D differ only in the boundary of one TM helix (372..388 vs 373..393). Both describe a hydrophobic helical segment in the same region. Without the specific annotation, both are defensible predictions. The 1-5 residue difference is within the typical ±3-5 residue uncertainty of TM helix boundary predictions.


### Important caveats

- All six TM annotations carry evidence code ECO:0000255 (inferred by similarity), meaning they are computational predictions, not experimentally validated measurements.
- The distinction between choices A and D (372..388 vs 373..393) is within the noise of any standard TM prediction tool and does not reflect a biologically meaningful difference.
- The UniProt entry was first public in 2025-06-18; the historical version 83 (entry version at retrieval) already contained these annotations, but the author's exact source snapshot is unknown.
- Choice C (1..21) is a clear distractor with a wrong start position and only one TM region; choice B omits the 300..320 region, which is a more substantive error but still requires recognizing that region as TM.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "A model could potentially identify the approximate number of hydrophobic stretches (e.g., 6 vs 5 vs 1) and roughly locate them by hydrophobicity scanning, which would eliminate C (single TM, wrong start) and possibly B (missing the 300..320 region). However, the critical distinction between A (372..388) and D (373..393) involves a 1-residue shift at the N-terminus and a 5-residue extension at the C-terminus of one helix. These boundaries fall well within the uncertainty envelope of any computational TM predictor and cannot be resolved by general hydrophobicity reasoning, helix-propensity analysis, or knowledge of membrane biology. The annotations themselves carry ECO:0000255 (similarity-based inference), confirming they are algorithmic outputs with inherent positional noise.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The exact boundary coordinates assigned by the specific prediction pipeline used in the UniProt annotation (e.g., whether the helix at ~373 starts at 372 or 373, and whether it ends at 388 or 393). No general biological principle distinguishes 372..388 from 373..393 for this particular sequence.",
    "reason": "While the gross TM topology (number and approximate location of helices) is inferable from hydrophobicity, the exact residue-level boundaries that distinguish A from D (and to some extent B from D regarding the 300..320 region) depend on the output of a particular computational predictor recorded in the database. No biological argument from the sequence alone can justify choosing 393 over 388 as the C-terminal boundary of the fourth TM helix."
  },
  "case_id": "transmembrane_0092",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "C7",
      "C8",
      "C9",
      "C10",
      "H2",
      "H3",
      "H4",
      "H5",
      "H6",
      "H7"
    ],
    "judgment": "supported",
    "reason": "The UniProt annotation for Q4J8Q7 (sequence matched, 464 AA) lists exactly six transmembrane helical regions: 6..26, 300..320, 337..357, 373..393, 416..436, 439..459, all annotated with ECO:0000255 (inferred by similarity). Choice D matches these six regions exactly. The historical entry (v83) confirms the same boundaries. The sequence SHA256 matches the benchmark input."
  },
  "important_caveats": [
    "All six TM annotations carry evidence code ECO:0000255 (inferred by similarity), meaning they are computational predictions, not experimentally validated measurements.",
    "The distinction between choices A and D (372..388 vs 373..393) is within the noise of any standard TM prediction tool and does not reflect a biologically meaningful difference.",
    "The UniProt entry was first public in 2025-06-18; the historical version 83 (entry version at retrieval) already contained these annotations, but the author's exact source snapshot is unknown.",
    "Choice C (1..21) is a clear distractor with a wrong start position and only one TM region; choice B omits the 300..320 region, which is a more substantive error but still requires recognizing that region as TM."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "D"
    ],
    "reason": "Options A and D differ only in the boundary of one TM helix (372..388 vs 373..393). Both describe a hydrophobic helical segment in the same region. Without the specific annotation, both are defensible predictions. The 1-5 residue difference is within the typical ±3-5 residue uncertainty of TM helix boundary predictions."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0092",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt annotation for Q4J8Q7 (sequence matched, 464 AA) lists exactly six transmembrane helical regions: 6..26, 300..320, 337..357, 373..393, 416..436, 439..459, all annotated with ECO:0000255 (inferred by similarity). Choice D matches these six regions exactly. The historical entry (v83) confirms the same boundaries. The sequence SHA256 matches the benchmark input.",
    "evidence_ids": ["C5", "C6", "C7", "C8", "C9", "C10", "H2", "H3", "H4", "H5", "H6", "H7"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "A model could potentially identify the approximate number of hydrophobic stretches (e.g., 6 vs 5 vs 1) and roughly locate them by hydrophobicity scanning, which would eliminate C (single TM, wrong start) and possibly B (missing the 300..320 region). However, the critical distinction between A (372..388) and D (373..393) involves a 1-residue shift at the N-terminus and a 5-residue extension at the C-terminus of one helix. These boundaries fall well within the uncertainty envelope of any computational TM predictor and cannot be resolved by general hydrophobicity reasoning, helix-propensity analysis, or knowledge of membrane biology. The annotations themselves carry ECO:0000255 (similarity-based inference), confirming they are algorithmic outputs with inherent positional noise.",
    "missing_item_specific_fact": "The exact boundary coordinates assigned by the specific prediction pipeline used in the UniProt annotation (e.g., whether the helix at ~373 starts at 372 or 373, and whether it ends at 388 or 393). No general biological principle distinguishes 372..388 from 373..393 for this particular sequence.",
    "reason": "While the gross TM topology (number and approximate location of helices) is inferable from hydrophobicity, the exact residue-level boundaries that distinguish A from D (and to some extent B from D regarding the 300..320 region) depend on the output of a particular computational predictor recorded in the database. No biological argument from the sequence alone can justify choosing 393 over 388 as the C-terminal boundary of the fourth TM helix."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "D"],
    "reason": "Options A and D differ only in the boundary of one TM helix (372..388 vs 373..393). Both describe a hydrophobic helical segment in the same region. Without the specific annotation, both are defensible predictions. The 1-5 residue difference is within the typical ±3-5 residue uncertainty of TM helix boundary predictions."
  },
  "important_caveats": [
    "All six TM annotations carry evidence code ECO:0000255 (inferred by similarity), meaning they are computational predictions, not experimentally validated measurements.",
    "The distinction between choices A and D (372..388 vs 373..393) is within the noise of any standard TM prediction tool and does not reflect a biologically meaningful difference.",
    "The UniProt entry was first public in 2025-06-18; the historical version 83 (entry version at retrieval) already contained these annotations, but the author's exact source snapshot is unknown.",
    "Choice C (1..21) is a clear distractor with a wrong start position and only one TM region; choice B omits the 300..320 region, which is a more substantive error but still requires recognizing that region as TM."
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

**Accession:** `Q4J8Q7` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 83. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4J8Q7.json)  
**Locator:** `/features/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:48.833149+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":26},"start":{"modifier":"EXACT","value":6}},"type":"Transmembrane"}
```

Source SHA-256: `3e85eec2dfbc367c39396a2802767d7bd8d7eecdc2ad5665df5f0b909ffd12ee`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4J8Q7.json)  
**Locator:** `/features/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:48.833149+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":320},"start":{"modifier":"EXACT","value":300}},"type":"Transmembrane"}
```

Source SHA-256: `3e85eec2dfbc367c39396a2802767d7bd8d7eecdc2ad5665df5f0b909ffd12ee`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4J8Q7.json)  
**Locator:** `/features/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:48.833149+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":357},"start":{"modifier":"EXACT","value":337}},"type":"Transmembrane"}
```

Source SHA-256: `3e85eec2dfbc367c39396a2802767d7bd8d7eecdc2ad5665df5f0b909ffd12ee`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4J8Q7.json)  
**Locator:** `/features/4`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:48.833149+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":393},"start":{"modifier":"EXACT","value":373}},"type":"Transmembrane"}
```

Source SHA-256: `3e85eec2dfbc367c39396a2802767d7bd8d7eecdc2ad5665df5f0b909ffd12ee`.

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4J8Q7.json)  
**Locator:** `/features/5`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:48.833149+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":436},"start":{"modifier":"EXACT","value":416}},"type":"Transmembrane"}
```

Source SHA-256: `3e85eec2dfbc367c39396a2802767d7bd8d7eecdc2ad5665df5f0b909ffd12ee`.

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4J8Q7.json)  
**Locator:** `/features/6`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:48.833149+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":459},"start":{"modifier":"EXACT","value":439}},"type":"Transmembrane"}
```

Source SHA-256: `3e85eec2dfbc367c39396a2802767d7bd8d7eecdc2ad5665df5f0b909ffd12ee`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q4J8Q7?format=txt&versions=83)  
**Locator:** `lines 73-75`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 83 / 1.  
**Retrieved:** 2026-11-02T04:30:51.056852+00:00.  

```text
FT   TRANSMEM        6..26
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `77a0391d87d26f83f55657f76a4009b13d967514999d8b969ae7fda3d19b4120`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q4J8Q7?format=txt&versions=83)  
**Locator:** `lines 76-78`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 83 / 1.  
**Retrieved:** 2026-11-02T04:30:51.056852+00:00.  

```text
FT   TRANSMEM        300..320
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `77a0391d87d26f83f55657f76a4009b13d967514999d8b969ae7fda3d19b4120`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q4J8Q7?format=txt&versions=83)  
**Locator:** `lines 79-81`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 83 / 1.  
**Retrieved:** 2026-11-02T04:30:51.056852+00:00.  

```text
FT   TRANSMEM        337..357
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `77a0391d87d26f83f55657f76a4009b13d967514999d8b969ae7fda3d19b4120`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q4J8Q7?format=txt&versions=83)  
**Locator:** `lines 82-84`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 83 / 1.  
**Retrieved:** 2026-11-02T04:30:51.056852+00:00.  

```text
FT   TRANSMEM        373..393
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `77a0391d87d26f83f55657f76a4009b13d967514999d8b969ae7fda3d19b4120`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q4J8Q7?format=txt&versions=83)  
**Locator:** `lines 85-87`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 83 / 1.  
**Retrieved:** 2026-11-02T04:30:51.056852+00:00.  

```text
FT   TRANSMEM        416..436
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `77a0391d87d26f83f55657f76a4009b13d967514999d8b969ae7fda3d19b4120`.

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q4J8Q7?format=txt&versions=83)  
**Locator:** `lines 88-90`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 83 / 1.  
**Retrieved:** 2026-11-02T04:30:51.056852+00:00.  

```text
FT   TRANSMEM        439..459
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `77a0391d87d26f83f55657f76a4009b13d967514999d8b969ae7fda3d19b4120`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json), zero-based source row 92. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
