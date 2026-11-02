# transmembrane_0070

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `transmembrane`  
**Author expected answer:** **D** — 58..78; 85..105; 150..170; 171..191; 198..218; 252..272

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MTTSPGTVESTTPVSGQLRTVLSAGERPARATAVSATLTHLWRAMMAFKHFPVQLIDIVLMPLIFLLMFTYLFGGAFADSTEEYLQFYLPGVTVQAVVMMTVYTGTSLNTDIHKGVFDRFRTLPFWQPATLAGSLLGDVLRYVVALATTVFLGLLLGFRADGGFLGVVGAMLVLIVFGFSVSWIFAALGVVASEPERVSGTSMIVLYPLLFMSNIFVMPETMPGWMQAIVDANPMSHAATASRELMHGTAGFWDVGLVLCVSAGLVAVFAPLTMRLYRNKNAH

[Multiple Choices]
A. 58..78; 150..170; 171..191; 198..218; 252..272
B. 30..50; 62..82; 108..128; 144..164; 186..206; 327..347; 357..377
C. 58..78; 85..105; 147..171; 171..191; 198..218; 252..272
D. 58..78; 85..105; 150..170; 171..191; 198..218; 252..272
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

> The exact sequence matches the UniProt sequence, whose current and archived annotations list all six transmembrane segments in choice D. These annotations carry ECO:0000255, indicating computational evidence rather than direct experimental validation.

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [C9](#evidence-c9), [C10](#evidence-c10), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6), [H7](#evidence-h7), [H8](#evidence-h8).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence has several strongly hydrophobic stretches, which supports the general inference that it is a multi-pass membrane protein and helps reject grossly incompatible coordinates. However, hydrophobicity alone does not reliably establish the precise boundaries or distinguish the close alternatives.


**Missing item-specific fact**

> The protein-specific transmembrane-region boundaries, especially 150..170 versus the nearby 147..171 alternative, are needed to select the keyed coordinates.


**Reason**

> The exact keyed segments are supported by a sequence-matched database annotation, but the choices require protein-specific boundary calls that are not uniquely determined by general biological reasoning from the supplied sequence.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "C",
  "D"
]
```

> Choices C and D differ only in the boundary call for the segment near residues 150..170. Given that transmembrane boundaries are predictions and can vary by a few residues, the sequence alone does not clearly rule out the nearby 147..171 call; the cited annotation specifically favors D.


### Important caveats

- The database annotation is computationally supported, not evidence of experimental mapping of the helix boundaries.
- Reviewer-only accession and annotation information was not supplied to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has several strongly hydrophobic stretches, which supports the general inference that it is a multi-pass membrane protein and helps reject grossly incompatible coordinates. However, hydrophobicity alone does not reliably establish the precise boundaries or distinguish the close alternatives.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific transmembrane-region boundaries, especially 150..170 versus the nearby 147..171 alternative, are needed to select the keyed coordinates.",
    "reason": "The exact keyed segments are supported by a sequence-matched database annotation, but the choices require protein-specific boundary calls that are not uniquely determined by general biological reasoning from the supplied sequence."
  },
  "case_id": "transmembrane_0070",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
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
    "reason": "The exact sequence matches the UniProt sequence, whose current and archived annotations list all six transmembrane segments in choice D. These annotations carry ECO:0000255, indicating computational evidence rather than direct experimental validation."
  },
  "important_caveats": [
    "The database annotation is computationally supported, not evidence of experimental mapping of the helix boundaries.",
    "Reviewer-only accession and annotation information was not supplied to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "C",
      "D"
    ],
    "reason": "Choices C and D differ only in the boundary call for the segment near residues 150..170. Given that transmembrane boundaries are predictions and can vary by a few residues, the sequence alone does not clearly rule out the nearby 147..171 call; the cited annotation specifically favors D."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0070",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt sequence, whose current and archived annotations list all six transmembrane segments in choice D. These annotations carry ECO:0000255, indicating computational evidence rather than direct experimental validation.",
    "evidence_ids": ["C1", "C5", "C6", "C7", "C8", "C9", "C10", "H3", "H4", "H5", "H6", "H7", "H8"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence has several strongly hydrophobic stretches, which supports the general inference that it is a multi-pass membrane protein and helps reject grossly incompatible coordinates. However, hydrophobicity alone does not reliably establish the precise boundaries or distinguish the close alternatives.",
    "missing_item_specific_fact": "The protein-specific transmembrane-region boundaries, especially 150..170 versus the nearby 147..171 alternative, are needed to select the keyed coordinates.",
    "reason": "The exact keyed segments are supported by a sequence-matched database annotation, but the choices require protein-specific boundary calls that are not uniquely determined by general biological reasoning from the supplied sequence."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["C", "D"],
    "reason": "Choices C and D differ only in the boundary call for the segment near residues 150..170. Given that transmembrane boundaries are predictions and can vary by a few residues, the sequence alone does not clearly rule out the nearby 147..171 call; the cited annotation specifically favors D."
  },
  "important_caveats": [
    "The database annotation is computationally supported, not evidence of experimental mapping of the helix boundaries.",
    "Reviewer-only accession and annotation information was not supplied to the evaluated model."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry P0DXU4 (Daunorubicin resistance ABC transporter permease DrrB1, Streptomyces coeruleorubidus) annotates exactly six transmembrane helical regions at 58..78, 85..105, 150..170, 171..191, 198..218, and 252..272, matching Choice D precisely. The sequence SHA256 matches the benchmark input. All annotations carry evidence code ECO:0000255 (inferred by similarity), so these are computational predictions rather than experimental measurements, but they do support the key.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [C9](#evidence-c9), [C10](#evidence-c10), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6), [H7](#evidence-h7), [H8](#evidence-h8).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> Option B can be eliminated because positions 327..347 and 357..377 exceed the 283-residue protein length. Option A is missing the hydrophobic segment around 85..105. Between C and D, the only difference is the third TM region: C gives 147..171 while D gives 150..170. Residues at positions 147-149 are Ala-Thr-Thr (two polar Thr residues), while position 150 is Val (strongly hydrophobic), providing a weak hydrophobicity argument favoring a helix start at 150. However, this 3-residue boundary difference falls well within the typical ±5-residue uncertainty of TM helix prediction tools, and the annotation itself is similarity-based (ECO:0000255), not experimentally determined.


**Missing item-specific fact**

> The precise boundary assignment of the third transmembrane helix (150..170 vs 147..171) as recorded in the UniProt annotation for this specific protein. No general biological principle definitively resolves a 3-residue boundary shift when both candidate helices are within the normal 18-25 residue TM length range.


**Reason**

> While coarse elimination (B exceeds protein length; A omits a hydrophobic segment) is achievable by reasoning, the critical C-vs-D distinction hinges on a 3-residue boundary shift that is within the noise of standard TM prediction. The 'correct' answer is the specific database annotation for this protein, not a conclusion derivable with confidence from sequence hydrophobicity alone.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "C",
  "D"
]
```

> Both C (147..171) and D (150..170) describe hydrophobic stretches of plausible TM helix length (25 vs 21 residues). The 3-residue N-terminal difference (Ala-Thr-Thr vs Val) provides a mild hydrophobicity preference for D but does not exclude C, as TM helices commonly incorporate polar residues near their boundaries. Without the exact database annotation, a careful analyst could reasonably select either.


### Important caveats

- All six TM annotations carry evidence code ECO:0000255 (inferred by similarity), meaning they are computational predictions, not experimental measurements.
- The UniProt entry was first public on 2025-02-05; the author's exact source snapshot is unknown, though the sequence matches.
- Option B contains positions (327..347, 357..377) that exceed the 283-residue protein length, making it trivially eliminable and serving as an easy distractor.
- The protein is annotated as an ABC transporter permease (DrrB1), consistent with a multi-pass TM topology, but the exact helix count and boundaries are annotation-dependent.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Option B can be eliminated because positions 327..347 and 357..377 exceed the 283-residue protein length. Option A is missing the hydrophobic segment around 85..105. Between C and D, the only difference is the third TM region: C gives 147..171 while D gives 150..170. Residues at positions 147-149 are Ala-Thr-Thr (two polar Thr residues), while position 150 is Val (strongly hydrophobic), providing a weak hydrophobicity argument favoring a helix start at 150. However, this 3-residue boundary difference falls well within the typical ±5-residue uncertainty of TM helix prediction tools, and the annotation itself is similarity-based (ECO:0000255), not experimentally determined.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The precise boundary assignment of the third transmembrane helix (150..170 vs 147..171) as recorded in the UniProt annotation for this specific protein. No general biological principle definitively resolves a 3-residue boundary shift when both candidate helices are within the normal 18-25 residue TM length range.",
    "reason": "While coarse elimination (B exceeds protein length; A omits a hydrophobic segment) is achievable by reasoning, the critical C-vs-D distinction hinges on a 3-residue boundary shift that is within the noise of standard TM prediction. The 'correct' answer is the specific database annotation for this protein, not a conclusion derivable with confidence from sequence hydrophobicity alone."
  },
  "case_id": "transmembrane_0070",
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
    "reason": "The UniProt entry P0DXU4 (Daunorubicin resistance ABC transporter permease DrrB1, Streptomyces coeruleorubidus) annotates exactly six transmembrane helical regions at 58..78, 85..105, 150..170, 171..191, 198..218, and 252..272, matching Choice D precisely. The sequence SHA256 matches the benchmark input. All annotations carry evidence code ECO:0000255 (inferred by similarity), so these are computational predictions rather than experimental measurements, but they do support the key."
  },
  "important_caveats": [
    "All six TM annotations carry evidence code ECO:0000255 (inferred by similarity), meaning they are computational predictions, not experimental measurements.",
    "The UniProt entry was first public on 2025-02-05; the author's exact source snapshot is unknown, though the sequence matches.",
    "Option B contains positions (327..347, 357..377) that exceed the 283-residue protein length, making it trivially eliminable and serving as an easy distractor.",
    "The protein is annotated as an ABC transporter permease (DrrB1), consistent with a multi-pass TM topology, but the exact helix count and boundaries are annotation-dependent."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "C",
      "D"
    ],
    "reason": "Both C (147..171) and D (150..170) describe hydrophobic stretches of plausible TM helix length (25 vs 21 residues). The 3-residue N-terminal difference (Ala-Thr-Thr vs Val) provides a mild hydrophobicity preference for D but does not exclude C, as TM helices commonly incorporate polar residues near their boundaries. Without the exact database annotation, a careful analyst could reasonably select either."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0070",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry P0DXU4 (Daunorubicin resistance ABC transporter permease DrrB1, Streptomyces coeruleorubidus) annotates exactly six transmembrane helical regions at 58..78, 85..105, 150..170, 171..191, 198..218, and 252..272, matching Choice D precisely. The sequence SHA256 matches the benchmark input. All annotations carry evidence code ECO:0000255 (inferred by similarity), so these are computational predictions rather than experimental measurements, but they do support the key.",
    "evidence_ids": ["C5", "C6", "C7", "C8", "C9", "C10", "H3", "H4", "H5", "H6", "H7", "H8"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "Option B can be eliminated because positions 327..347 and 357..377 exceed the 283-residue protein length. Option A is missing the hydrophobic segment around 85..105. Between C and D, the only difference is the third TM region: C gives 147..171 while D gives 150..170. Residues at positions 147-149 are Ala-Thr-Thr (two polar Thr residues), while position 150 is Val (strongly hydrophobic), providing a weak hydrophobicity argument favoring a helix start at 150. However, this 3-residue boundary difference falls well within the typical ±5-residue uncertainty of TM helix prediction tools, and the annotation itself is similarity-based (ECO:0000255), not experimentally determined.",
    "missing_item_specific_fact": "The precise boundary assignment of the third transmembrane helix (150..170 vs 147..171) as recorded in the UniProt annotation for this specific protein. No general biological principle definitively resolves a 3-residue boundary shift when both candidate helices are within the normal 18-25 residue TM length range.",
    "reason": "While coarse elimination (B exceeds protein length; A omits a hydrophobic segment) is achievable by reasoning, the critical C-vs-D distinction hinges on a 3-residue boundary shift that is within the noise of standard TM prediction. The 'correct' answer is the specific database annotation for this protein, not a conclusion derivable with confidence from sequence hydrophobicity alone."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["C", "D"],
    "reason": "Both C (147..171) and D (150..170) describe hydrophobic stretches of plausible TM helix length (25 vs 21 residues). The 3-residue N-terminal difference (Ala-Thr-Thr vs Val) provides a mild hydrophobicity preference for D but does not exclude C, as TM helices commonly incorporate polar residues near their boundaries. Without the exact database annotation, a careful analyst could reasonably select either."
  },
  "important_caveats": [
    "All six TM annotations carry evidence code ECO:0000255 (inferred by similarity), meaning they are computational predictions, not experimental measurements.",
    "The UniProt entry was first public on 2025-02-05; the author's exact source snapshot is unknown, though the sequence matches.",
    "Option B contains positions (327..347, 357..377) that exceed the 283-residue protein length, making it trivially eliminable and serving as an easy distractor.",
    "The protein is annotated as an ABC transporter permease (DrrB1), consistent with a multi-pass TM topology, but the exact helix count and boundaries are annotation-dependent."
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

**Accession:** `P0DXU4` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 4. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXU4.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:38.291851+00:00.  

```json
"P0DXU4"
```

Source SHA-256: `0485d691ed0d1c230bd6d0cc546400f66c74af103adcbfae303adf9cef833386`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXU4.json)  
**Locator:** `/features/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:38.291851+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":78},"start":{"modifier":"EXACT","value":58}},"type":"Transmembrane"}
```

Source SHA-256: `0485d691ed0d1c230bd6d0cc546400f66c74af103adcbfae303adf9cef833386`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXU4.json)  
**Locator:** `/features/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:38.291851+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":105},"start":{"modifier":"EXACT","value":85}},"type":"Transmembrane"}
```

Source SHA-256: `0485d691ed0d1c230bd6d0cc546400f66c74af103adcbfae303adf9cef833386`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXU4.json)  
**Locator:** `/features/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:38.291851+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":170},"start":{"modifier":"EXACT","value":150}},"type":"Transmembrane"}
```

Source SHA-256: `0485d691ed0d1c230bd6d0cc546400f66c74af103adcbfae303adf9cef833386`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXU4.json)  
**Locator:** `/features/4`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:38.291851+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":191},"start":{"modifier":"EXACT","value":171}},"type":"Transmembrane"}
```

Source SHA-256: `0485d691ed0d1c230bd6d0cc546400f66c74af103adcbfae303adf9cef833386`.

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXU4.json)  
**Locator:** `/features/5`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:38.291851+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":218},"start":{"modifier":"EXACT","value":198}},"type":"Transmembrane"}
```

Source SHA-256: `0485d691ed0d1c230bd6d0cc546400f66c74af103adcbfae303adf9cef833386`.

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXU4.json)  
**Locator:** `/features/6`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:38.291851+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":272},"start":{"modifier":"EXACT","value":252}},"type":"Transmembrane"}
```

Source SHA-256: `0485d691ed0d1c230bd6d0cc546400f66c74af103adcbfae303adf9cef833386`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXU4?format=txt&versions=4)  
**Locator:** `lines 74-76`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 4 / 1.  
**Retrieved:** 2026-11-02T04:29:40.349229+00:00.  

```text
FT   TRANSMEM        58..78
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `d750c27539bcb0df22e75395c132bc01e7f57cee37b61c3a5ea940e8c526a55f`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXU4?format=txt&versions=4)  
**Locator:** `lines 77-79`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 4 / 1.  
**Retrieved:** 2026-11-02T04:29:40.349229+00:00.  

```text
FT   TRANSMEM        85..105
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `d750c27539bcb0df22e75395c132bc01e7f57cee37b61c3a5ea940e8c526a55f`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXU4?format=txt&versions=4)  
**Locator:** `lines 80-82`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 4 / 1.  
**Retrieved:** 2026-11-02T04:29:40.349229+00:00.  

```text
FT   TRANSMEM        150..170
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `d750c27539bcb0df22e75395c132bc01e7f57cee37b61c3a5ea940e8c526a55f`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXU4?format=txt&versions=4)  
**Locator:** `lines 83-85`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 4 / 1.  
**Retrieved:** 2026-11-02T04:29:40.349229+00:00.  

```text
FT   TRANSMEM        171..191
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `d750c27539bcb0df22e75395c132bc01e7f57cee37b61c3a5ea940e8c526a55f`.

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXU4?format=txt&versions=4)  
**Locator:** `lines 86-88`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 4 / 1.  
**Retrieved:** 2026-11-02T04:29:40.349229+00:00.  

```text
FT   TRANSMEM        198..218
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `d750c27539bcb0df22e75395c132bc01e7f57cee37b61c3a5ea940e8c526a55f`.

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXU4?format=txt&versions=4)  
**Locator:** `lines 89-91`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 4 / 1.  
**Retrieved:** 2026-11-02T04:29:40.349229+00:00.  

```text
FT   TRANSMEM        252..272
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `d750c27539bcb0df22e75395c132bc01e7f57cee37b61c3a5ea940e8c526a55f`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json), zero-based source row 70. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
