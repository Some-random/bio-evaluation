# transmembrane_0075

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `transmembrane`  
**Author expected answer:** **D** — 5..25; 81..101; 115..135; 151..171; 182..202; 229..249; 269..289; 305..325

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MPRPVSVVFVSLIIAAAVGVWGVFAWNGGFEELDAIVNRHPSTGIPGLNHFPSLDQGLMSMAAFNLPVVGREPLFAEGRHFMAQLLANVFAIPIVLLTEDFRAAPGSVARYSTSWGVFSQLATSAVMCPLYGVCFSRRSNPRRVAVLPGRSTWIVLISVLIGYGAPAMLIFDPFSWGLKPQIWGVLAFTVYPLYVCLTASLLLKTVSSKRGRASRSVQKDSDSNSSLHYVVAGIVGVAGHLSYIGFHLGEHTGTAATRPDRVAQLVLRFLQIDYVITFAAMLTLAWHELTHSGRISLKPWRVAGYLLLGWLFIGPGATLAAAWALRERWIRQDTQEEKKRKL

[Multiple Choices]
A. 27..47; 82..102; 109..129; 136..156; 173..193; 209..229; 333..353; 361..381; 395..415; 427..447; 460..480
B. 5..25; 81..101; 119..136; 151..171; 182..202; 229..249; 269..289; 305..325
C. 5..25; 81..101; 115..135; 151..171; 229..249; 269..289; 305..325
D. 5..25; 81..101; 115..135; 151..171; 182..202; 229..249; 269..289; 305..325
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

> The sequence-matched UniProt annotation lists all eight transmembrane regions in choice D. These are computationally evidenced annotations (ECO:0000255), not established here as experimental measurements.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [C9](#evidence-c9), [C10](#evidence-c10), [C11](#evidence-c11), [C12](#evidence-c12), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6), [H7](#evidence-h7), [H8](#evidence-h8), [H9](#evidence-h9), [H10](#evidence-h10).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has multiple long, strongly hydrophobic stretches consistent with membrane-spanning alpha-helices; choice D places eight candidate regions over those stretches. In particular, it includes the hydrophobic segment around 182–202, which choice C omits, and avoids the unsupported extra regions in A.


**Missing item-specific fact**

> No protein-specific external fact is necessary to distinguish the broad pattern in these choices, though exact segment boundaries can depend on prediction conventions.


**Reason**

> Sequence hydrophobicity provides meaningful grounds for selecting the set of candidate spans. The matching database annotation supports the key but is reviewer-only and is not the basis for classifying the question as answerable by reasoning.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> D is the choice whose full set of regions corresponds to the hydrophobic membrane-spanning pattern; the alternatives omit, shift, or add regions.


### Important caveats

- The cited UniProt feature evidence is computational rather than experimental.
- The source sequence matches exactly, but the author’s precise source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has multiple long, strongly hydrophobic stretches consistent with membrane-spanning alpha-helices; choice D places eight candidate regions over those stretches. In particular, it includes the hydrophobic segment around 182–202, which choice C omits, and avoids the unsupported extra regions in A.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "No protein-specific external fact is necessary to distinguish the broad pattern in these choices, though exact segment boundaries can depend on prediction conventions.",
    "reason": "Sequence hydrophobicity provides meaningful grounds for selecting the set of candidate spans. The matching database annotation supports the key but is reviewer-only and is not the basis for classifying the question as answerable by reasoning."
  },
  "case_id": "transmembrane_0075",
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
      "H3",
      "H4",
      "H5",
      "H6",
      "H7",
      "H8",
      "H9",
      "H10"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation lists all eight transmembrane regions in choice D. These are computationally evidenced annotations (ECO:0000255), not established here as experimental measurements."
  },
  "important_caveats": [
    "The cited UniProt feature evidence is computational rather than experimental.",
    "The source sequence matches exactly, but the author’s precise source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "D is the choice whose full set of regions corresponds to the hydrophobic membrane-spanning pattern; the alternatives omit, shift, or add regions."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0075",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation lists all eight transmembrane regions in choice D. These are computationally evidenced annotations (ECO:0000255), not established here as experimental measurements.",
    "evidence_ids": ["C5", "C6", "C7", "C8", "C9", "C10", "C11", "C12", "H3", "H4", "H5", "H6", "H7", "H8", "H9", "H10"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has multiple long, strongly hydrophobic stretches consistent with membrane-spanning alpha-helices; choice D places eight candidate regions over those stretches. In particular, it includes the hydrophobic segment around 182–202, which choice C omits, and avoids the unsupported extra regions in A.",
    "missing_item_specific_fact": "No protein-specific external fact is necessary to distinguish the broad pattern in these choices, though exact segment boundaries can depend on prediction conventions.",
    "reason": "Sequence hydrophobicity provides meaningful grounds for selecting the set of candidate spans. The matching database annotation supports the key but is reviewer-only and is not the basis for classifying the question as answerable by reasoning."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "D is the choice whose full set of regions corresponds to the hydrophobic membrane-spanning pattern; the alternatives omit, shift, or add regions."
  },
  "important_caveats": [
    "The cited UniProt feature evidence is computational rather than experimental.",
    "The source sequence matches exactly, but the author’s precise source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry P0DXW0 (Terpene cyclase resF, Aspergillus sclerotiorum, 342 AA) annotates exactly 8 transmembrane helices at positions 5..25, 81..101, 115..135, 151..171, 182..202, 229..249, 269..289, and 305..325, which matches choice D verbatim. The sequence SHA256 matches the benchmark input. All annotations carry evidence code ECO:0000255 (predicted by similarity/prorule), so these are computational predictions rather than experimentally verified TM regions, but they constitute the authoritative database annotation for this entry.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [C9](#evidence-c9), [C10](#evidence-c10), [C11](#evidence-c11), [C12](#evidence-c12), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6), [H7](#evidence-h7), [H8](#evidence-h8), [H9](#evidence-h9), [H10](#evidence-h10).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> Choice A can be eliminated by reasoning (positions 333–480 exceed the 342-residue protein length). A general hydrophobicity scan can identify the major TM stretches (e.g., 5..25, 81..101, 229..249, 269..289, 305..325) as clearly hydrophobic. However, the critical distinctions between B, C, and D hinge on (1) whether the 182..202 region (QIWGVLAFTVYPLYVCLTASL), which contains multiple polar residues (Q, T, Y, P, C, T, S) alongside hydrophobic ones, qualifies as a TM helix, and (2) whether the third TM starts at 115 or 119 and ends at 135 or 136. These borderline calls depend on the specific prediction algorithm (prorule) rather than on unambiguous hydrophobicity thresholds.


**Missing item-specific fact**

> The exact output of the specific computational TM prediction tool (prorule/ECO:0000255) used to generate the UniProt annotation, particularly the decision to include the borderline 182..202 segment and the precise boundaries of the 115..135 vs 119..136 region.


**Reason**

> While a model can eliminate A and identify the major TM helices by hydrophobicity analysis, the precise answer (D over C or B) requires knowing the exact prediction-tool output. The 182..202 segment is genuinely borderline (mixed hydrophobic/polar composition), and the 4-residue boundary shift in the third TM (115 vs 119) is not resolvable by general biological reasoning alone. The answer depends on the specific computational annotation rather than a clear-cut biological argument.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "C"
]
```

> Choice C (7 TM regions, omitting 182..202) is defensible because the 182..202 segment (QIWGVLAFTVYPLYVCLTASL) has a mixed hydrophobic/polar composition that many hydrophobicity-based analyses would not confidently classify as a TM helix. The annotation is purely computational (ECO:0000255), not experimental, so the inclusion of this borderline region is a tool-specific judgment call. A model performing independent hydrophobicity analysis could reasonably exclude it, yielding C.


### Important caveats

- All 8 TM annotations are ECO:0000255 (predicted by similarity/prorule), not experimentally verified. The 'correct' answer reflects a computational prediction, not experimental topology data.
- The UniProt entry was first released in February 2025; the author's source snapshot date is unknown.
- Choice A is trivially eliminable (positions exceed protein length), reducing the effective discrimination to B vs C vs D.
- The boundary differences between B and D (119..136 vs 115..135) are within the typical uncertainty range of TM prediction tools (±5 residues).

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Choice A can be eliminated by reasoning (positions 333–480 exceed the 342-residue protein length). A general hydrophobicity scan can identify the major TM stretches (e.g., 5..25, 81..101, 229..249, 269..289, 305..325) as clearly hydrophobic. However, the critical distinctions between B, C, and D hinge on (1) whether the 182..202 region (QIWGVLAFTVYPLYVCLTASL), which contains multiple polar residues (Q, T, Y, P, C, T, S) alongside hydrophobic ones, qualifies as a TM helix, and (2) whether the third TM starts at 115 or 119 and ends at 135 or 136. These borderline calls depend on the specific prediction algorithm (prorule) rather than on unambiguous hydrophobicity thresholds.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The exact output of the specific computational TM prediction tool (prorule/ECO:0000255) used to generate the UniProt annotation, particularly the decision to include the borderline 182..202 segment and the precise boundaries of the 115..135 vs 119..136 region.",
    "reason": "While a model can eliminate A and identify the major TM helices by hydrophobicity analysis, the precise answer (D over C or B) requires knowing the exact prediction-tool output. The 182..202 segment is genuinely borderline (mixed hydrophobic/polar composition), and the 4-residue boundary shift in the third TM (115 vs 119) is not resolvable by general biological reasoning alone. The answer depends on the specific computational annotation rather than a clear-cut biological argument."
  },
  "case_id": "transmembrane_0075",
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
      "H3",
      "H4",
      "H5",
      "H6",
      "H7",
      "H8",
      "H9",
      "H10"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry P0DXW0 (Terpene cyclase resF, Aspergillus sclerotiorum, 342 AA) annotates exactly 8 transmembrane helices at positions 5..25, 81..101, 115..135, 151..171, 182..202, 229..249, 269..289, and 305..325, which matches choice D verbatim. The sequence SHA256 matches the benchmark input. All annotations carry evidence code ECO:0000255 (predicted by similarity/prorule), so these are computational predictions rather than experimentally verified TM regions, but they constitute the authoritative database annotation for this entry."
  },
  "important_caveats": [
    "All 8 TM annotations are ECO:0000255 (predicted by similarity/prorule), not experimentally verified. The 'correct' answer reflects a computational prediction, not experimental topology data.",
    "The UniProt entry was first released in February 2025; the author's source snapshot date is unknown.",
    "Choice A is trivially eliminable (positions exceed protein length), reducing the effective discrimination to B vs C vs D.",
    "The boundary differences between B and D (119..136 vs 115..135) are within the typical uncertainty range of TM prediction tools (±5 residues)."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "C"
    ],
    "reason": "Choice C (7 TM regions, omitting 182..202) is defensible because the 182..202 segment (QIWGVLAFTVYPLYVCLTASL) has a mixed hydrophobic/polar composition that many hydrophobicity-based analyses would not confidently classify as a TM helix. The annotation is purely computational (ECO:0000255), not experimental, so the inclusion of this borderline region is a tool-specific judgment call. A model performing independent hydrophobicity analysis could reasonably exclude it, yielding C."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0075",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry P0DXW0 (Terpene cyclase resF, Aspergillus sclerotiorum, 342 AA) annotates exactly 8 transmembrane helices at positions 5..25, 81..101, 115..135, 151..171, 182..202, 229..249, 269..289, and 305..325, which matches choice D verbatim. The sequence SHA256 matches the benchmark input. All annotations carry evidence code ECO:0000255 (predicted by similarity/prorule), so these are computational predictions rather than experimentally verified TM regions, but they constitute the authoritative database annotation for this entry.",
    "evidence_ids": ["C5", "C6", "C7", "C8", "C9", "C10", "C11", "C12", "H3", "H4", "H5", "H6", "H7", "H8", "H9", "H10"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "Choice A can be eliminated by reasoning (positions 333–480 exceed the 342-residue protein length). A general hydrophobicity scan can identify the major TM stretches (e.g., 5..25, 81..101, 229..249, 269..289, 305..325) as clearly hydrophobic. However, the critical distinctions between B, C, and D hinge on (1) whether the 182..202 region (QIWGVLAFTVYPLYVCLTASL), which contains multiple polar residues (Q, T, Y, P, C, T, S) alongside hydrophobic ones, qualifies as a TM helix, and (2) whether the third TM starts at 115 or 119 and ends at 135 or 136. These borderline calls depend on the specific prediction algorithm (prorule) rather than on unambiguous hydrophobicity thresholds.",
    "missing_item_specific_fact": "The exact output of the specific computational TM prediction tool (prorule/ECO:0000255) used to generate the UniProt annotation, particularly the decision to include the borderline 182..202 segment and the precise boundaries of the 115..135 vs 119..136 region.",
    "reason": "While a model can eliminate A and identify the major TM helices by hydrophobicity analysis, the precise answer (D over C or B) requires knowing the exact prediction-tool output. The 182..202 segment is genuinely borderline (mixed hydrophobic/polar composition), and the 4-residue boundary shift in the third TM (115 vs 119) is not resolvable by general biological reasoning alone. The answer depends on the specific computational annotation rather than a clear-cut biological argument."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["C"],
    "reason": "Choice C (7 TM regions, omitting 182..202) is defensible because the 182..202 segment (QIWGVLAFTVYPLYVCLTASL) has a mixed hydrophobic/polar composition that many hydrophobicity-based analyses would not confidently classify as a TM helix. The annotation is purely computational (ECO:0000255), not experimental, so the inclusion of this borderline region is a tool-specific judgment call. A model performing independent hydrophobicity analysis could reasonably exclude it, yielding C."
  },
  "important_caveats": [
    "All 8 TM annotations are ECO:0000255 (predicted by similarity/prorule), not experimentally verified. The 'correct' answer reflects a computational prediction, not experimental topology data.",
    "The UniProt entry was first released in February 2025; the author's source snapshot date is unknown.",
    "Choice A is trivially eliminable (positions exceed protein length), reducing the effective discrimination to B vs C vs D.",
    "The boundary differences between B and D (119..136 vs 115..135) are within the typical uncertainty range of TM prediction tools (±5 residues)."
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

**Accession:** `P0DXW0` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 2. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXW0.json)  
**Locator:** `/features/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:50.537709+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":25},"start":{"modifier":"EXACT","value":5}},"type":"Transmembrane"}
```

Source SHA-256: `20826975e15383c7e7ed9a18e9833743bdc1e763a65798dcc5e4dbb145fcc991`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXW0.json)  
**Locator:** `/features/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:50.537709+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":101},"start":{"modifier":"EXACT","value":81}},"type":"Transmembrane"}
```

Source SHA-256: `20826975e15383c7e7ed9a18e9833743bdc1e763a65798dcc5e4dbb145fcc991`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXW0.json)  
**Locator:** `/features/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:50.537709+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":135},"start":{"modifier":"EXACT","value":115}},"type":"Transmembrane"}
```

Source SHA-256: `20826975e15383c7e7ed9a18e9833743bdc1e763a65798dcc5e4dbb145fcc991`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXW0.json)  
**Locator:** `/features/4`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:50.537709+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":171},"start":{"modifier":"EXACT","value":151}},"type":"Transmembrane"}
```

Source SHA-256: `20826975e15383c7e7ed9a18e9833743bdc1e763a65798dcc5e4dbb145fcc991`.

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXW0.json)  
**Locator:** `/features/5`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:50.537709+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":202},"start":{"modifier":"EXACT","value":182}},"type":"Transmembrane"}
```

Source SHA-256: `20826975e15383c7e7ed9a18e9833743bdc1e763a65798dcc5e4dbb145fcc991`.

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXW0.json)  
**Locator:** `/features/6`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:50.537709+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":249},"start":{"modifier":"EXACT","value":229}},"type":"Transmembrane"}
```

Source SHA-256: `20826975e15383c7e7ed9a18e9833743bdc1e763a65798dcc5e4dbb145fcc991`.

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXW0.json)  
**Locator:** `/features/7`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:50.537709+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":289},"start":{"modifier":"EXACT","value":269}},"type":"Transmembrane"}
```

Source SHA-256: `20826975e15383c7e7ed9a18e9833743bdc1e763a65798dcc5e4dbb145fcc991`.

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXW0.json)  
**Locator:** `/features/8`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:50.537709+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":325},"start":{"modifier":"EXACT","value":305}},"type":"Transmembrane"}
```

Source SHA-256: `20826975e15383c7e7ed9a18e9833743bdc1e763a65798dcc5e4dbb145fcc991`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXW0?format=txt&versions=2)  
**Locator:** `lines 53-55`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 2 / 1.  
**Retrieved:** 2026-11-02T04:29:54.246056+00:00.  

```text
FT   TRANSMEM        5..25
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `4ee0148ff929a45fee99461aa9272fe9ea0eed8e9ecc9ee53739e76044ec61c4`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXW0?format=txt&versions=2)  
**Locator:** `lines 56-58`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 2 / 1.  
**Retrieved:** 2026-11-02T04:29:54.246056+00:00.  

```text
FT   TRANSMEM        81..101
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `4ee0148ff929a45fee99461aa9272fe9ea0eed8e9ecc9ee53739e76044ec61c4`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXW0?format=txt&versions=2)  
**Locator:** `lines 59-61`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 2 / 1.  
**Retrieved:** 2026-11-02T04:29:54.246056+00:00.  

```text
FT   TRANSMEM        115..135
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `4ee0148ff929a45fee99461aa9272fe9ea0eed8e9ecc9ee53739e76044ec61c4`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXW0?format=txt&versions=2)  
**Locator:** `lines 62-64`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 2 / 1.  
**Retrieved:** 2026-11-02T04:29:54.246056+00:00.  

```text
FT   TRANSMEM        151..171
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `4ee0148ff929a45fee99461aa9272fe9ea0eed8e9ecc9ee53739e76044ec61c4`.

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXW0?format=txt&versions=2)  
**Locator:** `lines 65-67`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 2 / 1.  
**Retrieved:** 2026-11-02T04:29:54.246056+00:00.  

```text
FT   TRANSMEM        182..202
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `4ee0148ff929a45fee99461aa9272fe9ea0eed8e9ecc9ee53739e76044ec61c4`.

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXW0?format=txt&versions=2)  
**Locator:** `lines 68-70`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 2 / 1.  
**Retrieved:** 2026-11-02T04:29:54.246056+00:00.  

```text
FT   TRANSMEM        229..249
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `4ee0148ff929a45fee99461aa9272fe9ea0eed8e9ecc9ee53739e76044ec61c4`.

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXW0?format=txt&versions=2)  
**Locator:** `lines 71-73`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 2 / 1.  
**Retrieved:** 2026-11-02T04:29:54.246056+00:00.  

```text
FT   TRANSMEM        269..289
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `4ee0148ff929a45fee99461aa9272fe9ea0eed8e9ecc9ee53739e76044ec61c4`.

### Evidence H10

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXW0?format=txt&versions=2)  
**Locator:** `lines 74-76`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 2 / 1.  
**Retrieved:** 2026-11-02T04:29:54.246056+00:00.  

```text
FT   TRANSMEM        305..325
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `4ee0148ff929a45fee99461aa9272fe9ea0eed8e9ecc9ee53739e76044ec61c4`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json), zero-based source row 75. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
