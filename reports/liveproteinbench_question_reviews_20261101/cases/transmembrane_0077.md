# transmembrane_0077

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `transmembrane`  
**Author expected answer:** **D** — 25..45; 55..75; 80..100; 116..136; 175..195; 211..231

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MFSNLHLPLNPIDKVNQPPVYYLQVQDGLIICSGLCWTTAYILYIRQAYRDKSYGMPLVCLCANIAWEFLFGAAIPESAAQVVSFFPWFVIDIGIVYTTWKFGREQWKHAPLVAQNLGWILLGGIAGMLVMFWAFLKTYDNRYEAGFYLAWTDQIIVSTTSVAQLMSRNNTSGHSWGIWFTRWIGSVFAELIFVWRYWNYPESYPVAATHVTIFLFIVTEVADLTYPFVYASLDKKEKKKLK

[Multiple Choices]
A. 4..24; 81..101; 116..136; 158..178; 181..201; 228..248; 271..291; 309..329
B. 25..45; 55..75; 80..100; 116..136; 175..195; 216..232
C. 25..45; 55..75; 116..136; 175..195; 211..231
D. 25..45; 55..75; 80..100; 116..136; 175..195; 211..231
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

> The sequence-matched UniProt entry annotates all six regions in D as transmembrane helices, so the key is supported as a computational prediction. The evidence does not establish experimental membrane spanning.

Citations as saved: [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6), [H7](#evidence-h7), [H8](#evidence-h8).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> Several listed regions coincide with hydrophobic stretches, which supports candidate membrane helices in general; however, that does not uniquely determine the precise predicted boundaries.


**Missing item-specific fact**

> A protein-specific transmembrane prediction or annotation is needed to distinguish the closely overlapping C-terminal alternatives, especially D's 211..231 from B's 216..232.


**Reason**

> Sequence hydrophobicity offers useful clues but does not uniquely establish all six intervals or their exact endpoints. The specific predicted topology is not supplied in the question.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "D"
]
```

> Both include the same first five regions and a plausible overlapping C-terminal hydrophobic segment; the sequence alone does not clearly resolve their differing endpoints. The supplied annotation favors D.


### Important caveats

- The transmembrane annotations carry ECO:0000255 computational evidence codes, not experimental topology evidence.
- The archived annotation matches the supplied sequence, but the author's exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Several listed regions coincide with hydrophobic stretches, which supports candidate membrane helices in general; however, that does not uniquely determine the precise predicted boundaries.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "A protein-specific transmembrane prediction or annotation is needed to distinguish the closely overlapping C-terminal alternatives, especially D's 211..231 from B's 216..232.",
    "reason": "Sequence hydrophobicity offers useful clues but does not uniquely establish all six intervals or their exact endpoints. The specific predicted topology is not supplied in the question."
  },
  "case_id": "transmembrane_0077",
  "expected_answer_check": {
    "evidence_ids": [
      "H3",
      "H4",
      "H5",
      "H6",
      "H7",
      "H8"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt entry annotates all six regions in D as transmembrane helices, so the key is supported as a computational prediction. The evidence does not establish experimental membrane spanning."
  },
  "important_caveats": [
    "The transmembrane annotations carry ECO:0000255 computational evidence codes, not experimental topology evidence.",
    "The archived annotation matches the supplied sequence, but the author's exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "D"
    ],
    "reason": "Both include the same first five regions and a plausible overlapping C-terminal hydrophobic segment; the sequence alone does not clearly resolve their differing endpoints. The supplied annotation favors D."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0077",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt entry annotates all six regions in D as transmembrane helices, so the key is supported as a computational prediction. The evidence does not establish experimental membrane spanning.",
    "evidence_ids": ["H3", "H4", "H5", "H6", "H7", "H8"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "Several listed regions coincide with hydrophobic stretches, which supports candidate membrane helices in general; however, that does not uniquely determine the precise predicted boundaries.",
    "missing_item_specific_fact": "A protein-specific transmembrane prediction or annotation is needed to distinguish the closely overlapping C-terminal alternatives, especially D's 211..231 from B's 216..232.",
    "reason": "Sequence hydrophobicity offers useful clues but does not uniquely establish all six intervals or their exact endpoints. The specific predicted topology is not supplied in the question."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "D"],
    "reason": "Both include the same first five regions and a plausible overlapping C-terminal hydrophobic segment; the sequence alone does not clearly resolve their differing endpoints. The supplied annotation favors D."
  },
  "important_caveats": [
    "The transmembrane annotations carry ECO:0000255 computational evidence codes, not experimental topology evidence.",
    "The archived annotation matches the supplied sequence, but the author's exact source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> Option D (25..45; 55..75; 80..100; 116..136; 175..195; 211..231) exactly matches all six transmembrane helix annotations in UniProt entry P0DY23 (evidence IDs C5–C10, H3–H8). The sequence SHA-256 of the supplied 242-aa protein matches the UniProt entry. However, the evidence code for every TM annotation is ECO:0000255 (automatic assertion from rule-based annotation by a curator), meaning these are computational predictions, not experimentally validated membrane-spanning segments. The annotation is nonetheless the authoritative database record for this entry.

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [C9](#evidence-c9), [C10](#evidence-c10), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6), [H7](#evidence-h7), [H8](#evidence-h8).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> General hydrophobicity analysis can identify approximate TM stretches (e.g., the strongly hydrophobic segments around 116–136 and 175–195 are recognizable). Option A is easily eliminated because positions 271–291 and 309–329 exceed the 242-aa protein length. However, the critical distinctions among B, C, and D cannot be resolved by general reasoning: (1) whether residues 80–100 (AQVVSFFPWFVIDIGIVYTTW), which contain several polar residues (Q, S, P, D, Y, T), constitute a TM helix is borderline and algorithm-dependent; (2) the exact boundary of the last TM region (211..231 in D vs. 216..232 in B) involves mixed hydrophobic/polar sequence where no clear biological criterion separates the two.


**Missing item-specific fact**

> The specific transmembrane prediction algorithm (e.g., TMHMM, Phobius) and its parameterization used to generate the ECO:0000255 rule-based annotation, which determines whether the borderline region at 80–100 is called a TM helix and where the exact start/end of the final TM segment falls.


**Reason**

> The UniProt TM annotations are rule-based computational predictions (ECO:0000255). The precise boundaries that distinguish D from B (211..231 vs 216..232) and the inclusion/exclusion of the borderline region 80..100 (distinguishing D from C) depend on the output of a particular prediction algorithm, not on a general biological principle that a model could apply to the raw sequence. Selecting D requires reproducing the exact database annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "D"
]
```

> Options B and D differ only in the last TM region: B lists 216..232 while D lists 211..231. The sequence in this region (VTIFLFIVTEVADLTYPFVYAS) is mixed hydrophobic/polar, and neither boundary is strongly favored by general hydrophobicity criteria. Without the specific prediction algorithm's output, both boundaries are plausible. Option C is less defensible because it omits the 80..100 region entirely while retaining five of the six annotated TM segments, making it a clear subset error.


### Important caveats

- All six TM annotations carry evidence code ECO:0000255 (rule-based computational annotation), not experimental evidence. They should not be treated as experimentally confirmed membrane-spanning regions.
- The protein is annotated as a Pyr4-family terpene cyclase (EC 4.2.3.-), a soluble enzyme class; the TM annotations are computational predictions that may reflect membrane-associated helices rather than true bilayer-spanning segments.
- The UniProt accession P0DY23 and its annotation were not provided to the evaluated model; the model only received the raw sequence and four answer choices.
- The sequence match between the benchmark input and the UniProt entry is confirmed (SHA-256 match), but the historical annotation snapshot used by the question author is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "General hydrophobicity analysis can identify approximate TM stretches (e.g., the strongly hydrophobic segments around 116–136 and 175–195 are recognizable). Option A is easily eliminated because positions 271–291 and 309–329 exceed the 242-aa protein length. However, the critical distinctions among B, C, and D cannot be resolved by general reasoning: (1) whether residues 80–100 (AQVVSFFPWFVIDIGIVYTTW), which contain several polar residues (Q, S, P, D, Y, T), constitute a TM helix is borderline and algorithm-dependent; (2) the exact boundary of the last TM region (211..231 in D vs. 216..232 in B) involves mixed hydrophobic/polar sequence where no clear biological criterion separates the two.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific transmembrane prediction algorithm (e.g., TMHMM, Phobius) and its parameterization used to generate the ECO:0000255 rule-based annotation, which determines whether the borderline region at 80–100 is called a TM helix and where the exact start/end of the final TM segment falls.",
    "reason": "The UniProt TM annotations are rule-based computational predictions (ECO:0000255). The precise boundaries that distinguish D from B (211..231 vs 216..232) and the inclusion/exclusion of the borderline region 80..100 (distinguishing D from C) depend on the output of a particular prediction algorithm, not on a general biological principle that a model could apply to the raw sequence. Selecting D requires reproducing the exact database annotation."
  },
  "case_id": "transmembrane_0077",
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
    "reason": "Option D (25..45; 55..75; 80..100; 116..136; 175..195; 211..231) exactly matches all six transmembrane helix annotations in UniProt entry P0DY23 (evidence IDs C5–C10, H3–H8). The sequence SHA-256 of the supplied 242-aa protein matches the UniProt entry. However, the evidence code for every TM annotation is ECO:0000255 (automatic assertion from rule-based annotation by a curator), meaning these are computational predictions, not experimentally validated membrane-spanning segments. The annotation is nonetheless the authoritative database record for this entry."
  },
  "important_caveats": [
    "All six TM annotations carry evidence code ECO:0000255 (rule-based computational annotation), not experimental evidence. They should not be treated as experimentally confirmed membrane-spanning regions.",
    "The protein is annotated as a Pyr4-family terpene cyclase (EC 4.2.3.-), a soluble enzyme class; the TM annotations are computational predictions that may reflect membrane-associated helices rather than true bilayer-spanning segments.",
    "The UniProt accession P0DY23 and its annotation were not provided to the evaluated model; the model only received the raw sequence and four answer choices.",
    "The sequence match between the benchmark input and the UniProt entry is confirmed (SHA-256 match), but the historical annotation snapshot used by the question author is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "D"
    ],
    "reason": "Options B and D differ only in the last TM region: B lists 216..232 while D lists 211..231. The sequence in this region (VTIFLFIVTEVADLTYPFVYAS) is mixed hydrophobic/polar, and neither boundary is strongly favored by general hydrophobicity criteria. Without the specific prediction algorithm's output, both boundaries are plausible. Option C is less defensible because it omits the 80..100 region entirely while retaining five of the six annotated TM segments, making it a clear subset error."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0077",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "Option D (25..45; 55..75; 80..100; 116..136; 175..195; 211..231) exactly matches all six transmembrane helix annotations in UniProt entry P0DY23 (evidence IDs C5–C10, H3–H8). The sequence SHA-256 of the supplied 242-aa protein matches the UniProt entry. However, the evidence code for every TM annotation is ECO:0000255 (automatic assertion from rule-based annotation by a curator), meaning these are computational predictions, not experimentally validated membrane-spanning segments. The annotation is nonetheless the authoritative database record for this entry.",
    "evidence_ids": ["C1", "C5", "C6", "C7", "C8", "C9", "C10", "H3", "H4", "H5", "H6", "H7", "H8"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "General hydrophobicity analysis can identify approximate TM stretches (e.g., the strongly hydrophobic segments around 116–136 and 175–195 are recognizable). Option A is easily eliminated because positions 271–291 and 309–329 exceed the 242-aa protein length. However, the critical distinctions among B, C, and D cannot be resolved by general reasoning: (1) whether residues 80–100 (AQVVSFFPWFVIDIGIVYTTW), which contain several polar residues (Q, S, P, D, Y, T), constitute a TM helix is borderline and algorithm-dependent; (2) the exact boundary of the last TM region (211..231 in D vs. 216..232 in B) involves mixed hydrophobic/polar sequence where no clear biological criterion separates the two.",
    "missing_item_specific_fact": "The specific transmembrane prediction algorithm (e.g., TMHMM, Phobius) and its parameterization used to generate the ECO:0000255 rule-based annotation, which determines whether the borderline region at 80–100 is called a TM helix and where the exact start/end of the final TM segment falls.",
    "reason": "The UniProt TM annotations are rule-based computational predictions (ECO:0000255). The precise boundaries that distinguish D from B (211..231 vs 216..232) and the inclusion/exclusion of the borderline region 80..100 (distinguishing D from C) depend on the output of a particular prediction algorithm, not on a general biological principle that a model could apply to the raw sequence. Selecting D requires reproducing the exact database annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "D"],
    "reason": "Options B and D differ only in the last TM region: B lists 216..232 while D lists 211..231. The sequence in this region (VTIFLFIVTEVADLTYPFVYAS) is mixed hydrophobic/polar, and neither boundary is strongly favored by general hydrophobicity criteria. Without the specific prediction algorithm's output, both boundaries are plausible. Option C is less defensible because it omits the 80..100 region entirely while retaining five of the six annotated TM segments, making it a clear subset error."
  },
  "important_caveats": [
    "All six TM annotations carry evidence code ECO:0000255 (rule-based computational annotation), not experimental evidence. They should not be treated as experimentally confirmed membrane-spanning regions.",
    "The protein is annotated as a Pyr4-family terpene cyclase (EC 4.2.3.-), a soluble enzyme class; the TM annotations are computational predictions that may reflect membrane-associated helices rather than true bilayer-spanning segments.",
    "The UniProt accession P0DY23 and its annotation were not provided to the evaluated model; the model only received the raw sequence and four answer choices.",
    "The sequence match between the benchmark input and the UniProt entry is confirmed (SHA-256 match), but the historical annotation snapshot used by the question author is unknown."
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

**Accession:** `P0DY23` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 3. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DY23.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:06.355655+00:00.  

```json
"P0DY23"
```

Source SHA-256: `6af7a985bb93d19c99b5af4867a56ec8d88ffbb618fc982eb2bddb21ed56136c`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DY23.json)  
**Locator:** `/features/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:06.355655+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":45},"start":{"modifier":"EXACT","value":25}},"type":"Transmembrane"}
```

Source SHA-256: `6af7a985bb93d19c99b5af4867a56ec8d88ffbb618fc982eb2bddb21ed56136c`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DY23.json)  
**Locator:** `/features/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:06.355655+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":75},"start":{"modifier":"EXACT","value":55}},"type":"Transmembrane"}
```

Source SHA-256: `6af7a985bb93d19c99b5af4867a56ec8d88ffbb618fc982eb2bddb21ed56136c`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DY23.json)  
**Locator:** `/features/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:06.355655+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":100},"start":{"modifier":"EXACT","value":80}},"type":"Transmembrane"}
```

Source SHA-256: `6af7a985bb93d19c99b5af4867a56ec8d88ffbb618fc982eb2bddb21ed56136c`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DY23.json)  
**Locator:** `/features/4`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:06.355655+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":136},"start":{"modifier":"EXACT","value":116}},"type":"Transmembrane"}
```

Source SHA-256: `6af7a985bb93d19c99b5af4867a56ec8d88ffbb618fc982eb2bddb21ed56136c`.

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DY23.json)  
**Locator:** `/features/5`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:06.355655+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":195},"start":{"modifier":"EXACT","value":175}},"type":"Transmembrane"}
```

Source SHA-256: `6af7a985bb93d19c99b5af4867a56ec8d88ffbb618fc982eb2bddb21ed56136c`.

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DY23.json)  
**Locator:** `/features/6`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:06.355655+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":231},"start":{"modifier":"EXACT","value":211}},"type":"Transmembrane"}
```

Source SHA-256: `6af7a985bb93d19c99b5af4867a56ec8d88ffbb618fc982eb2bddb21ed56136c`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DY23?format=txt&versions=3)  
**Locator:** `lines 77-79`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 3 / 1.  
**Retrieved:** 2026-11-02T04:30:08.630908+00:00.  

```text
FT   TRANSMEM        25..45
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `3fa07f60335a414512ee3950d17eeba0727ca5a77e80ddc7a1d8da8b59a78b2d`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DY23?format=txt&versions=3)  
**Locator:** `lines 80-82`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 3 / 1.  
**Retrieved:** 2026-11-02T04:30:08.630908+00:00.  

```text
FT   TRANSMEM        55..75
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `3fa07f60335a414512ee3950d17eeba0727ca5a77e80ddc7a1d8da8b59a78b2d`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DY23?format=txt&versions=3)  
**Locator:** `lines 83-85`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 3 / 1.  
**Retrieved:** 2026-11-02T04:30:08.630908+00:00.  

```text
FT   TRANSMEM        80..100
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `3fa07f60335a414512ee3950d17eeba0727ca5a77e80ddc7a1d8da8b59a78b2d`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DY23?format=txt&versions=3)  
**Locator:** `lines 86-88`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 3 / 1.  
**Retrieved:** 2026-11-02T04:30:08.630908+00:00.  

```text
FT   TRANSMEM        116..136
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `3fa07f60335a414512ee3950d17eeba0727ca5a77e80ddc7a1d8da8b59a78b2d`.

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DY23?format=txt&versions=3)  
**Locator:** `lines 89-91`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 3 / 1.  
**Retrieved:** 2026-11-02T04:30:08.630908+00:00.  

```text
FT   TRANSMEM        175..195
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `3fa07f60335a414512ee3950d17eeba0727ca5a77e80ddc7a1d8da8b59a78b2d`.

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DY23?format=txt&versions=3)  
**Locator:** `lines 92-94`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 3 / 1.  
**Retrieved:** 2026-11-02T04:30:08.630908+00:00.  

```text
FT   TRANSMEM        211..231
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `3fa07f60335a414512ee3950d17eeba0727ca5a77e80ddc7a1d8da8b59a78b2d`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json), zero-based source row 77. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
