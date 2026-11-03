# transmembrane_0019: before and after transfer clarification

[All 1,328 cases](../README.md) · [Method](../METHOD.md) · [Summary](../SUMMARY.md) · [Exact reviewer user message](../inputs/transmembrane_0019.txt)

**Task:** `transmembrane`  
**Author key, unchanged:** **C** — 1..21; 38..58; 72..92; 125..145; 154..174; 255..275; 284..304; 318..338; 348..368; 398..418; 427..447

| Round | Reviewer | Key support | Transfer / lookup | Output usability (canonical status) |
|---|---|---|---|---|
| before | GPT-6 Luna | supported | lookup-dependent | usable output (valid_review) |
| before | Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | usable output (valid_review) |
| after | GPT-6 Luna | supported | reasoning-supported | usable output (valid_review) |
| after | Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | usable output (valid_review) |

**Usable output means format-valid review, not reasoning-supported or biologically correct.** A usable output can classify the question as reasoning-supported, lookup-dependent or uncertain. An output error is a problem with the saved model response; it does not count a defective benchmark question or wrong key. Each saved review is retained in full below. Labels from output errors are displayed as saved and excluded from label statistics. The author key and reviewer evidence were visible to reviewers; this is a review of answerability and key support, not a benchmark-solving score.

## Complete original question

```text
[Protein Sequence]
MGLFTDLVLYGIVLPALPFIMRNRFHIPNAELQHYTSGFLATYAGASVFFSVPAGWAASKLGSRQLFLGGLVFLFVATAIFAFSTSLALLVVSRLLQGMSTAVVWTAGLDMVQDTVDPSQIGVTIGTIFATISVGELAAPVLGGVLYERGGIAAVFAVSAVMLAIDLGLRGLVIDKKAAVKFESPCLIRSSAERSDHVASAPTVVEAQERTHEGTPLLPQDDDDDSDRYKIDRELGSIVQAIPLLYCFREPRLHLAMLLSFVQALFIGTFDATVPTEAESLFHFSSLQVGLVFIALMLPYFALGRLAGQAVDRFGTKAAATSGYAFLVPCLLLLGLPEKKLVSKEANVALFCTILALNGIGLAVVTSPGYVEAIDVTTKYQVANPGHFGENGPYAQLFGFSSLYFFTGLAVGPLLGGVLRAKFGYAVMGAVYAAISGVTAIVSFLFVGTRRGVCWG

[Multiple Choices]
A. 1..21; 72..92; 125..145; 154..174; 255..275; 284..304; 318..338; 348..368; 398..418; 427..447
B. 27..47; 82..102; 109..129; 136..156; 173..193; 209..229; 333..353; 361..381; 395..415; 427..447; 460..480
C. 1..21; 38..58; 72..92; 125..145; 154..174; 255..275; 284..304; 318..338; 348..368; 398..418; 427..447
D. 1..21; 38..58; 72..92; 125..145; 154..174; 255..275; 284..304; 318..338; 346..372; 398..418; 427..447
```

<details>
<summary>Complete original system instructions</summary>

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

## Four saved visible reviews

## Before: GPT-6 Luna

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The supplied sequence matches the UniProt sequence, whose annotated transmembrane intervals match choice C exactly. The feature evidence is computational (ECO:0000255), not evidence of experimental confirmation.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [C9](#evidence-c9), [C10](#evidence-c10), [C11](#evidence-c11), [C12](#evidence-c12), [C13](#evidence-c13), [C14](#evidence-c14), [C15](#evidence-c15).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence contains multiple hydrophobic stretches, which supports predicting a multi-pass membrane protein and its broad transmembrane regions.


**Missing item-specific fact**

> The exact annotated interval boundaries, including whether the helix at 348..368 or 346..372 is intended, are not supplied and require a protein-specific prediction or annotation.


**Reason**

> Hydropathy can support broad region predictions but does not establish these precise boundaries or the complete keyed set from the input alone.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "C",
  "D"
]
```

> Choices C and D differ only in the boundaries of one strongly hydrophobic segment; the sequence alone does not clearly settle those few-residue boundary differences.


### Important caveats

- The matching database feature annotations are computationally evidenced, not shown here to be experimentally determined.
- The reviewer-only database identity and annotations were not part of the original model input.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains multiple hydrophobic stretches, which supports predicting a multi-pass membrane protein and its broad transmembrane regions.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The exact annotated interval boundaries, including whether the helix at 348..368 or 346..372 is intended, are not supplied and require a protein-specific prediction or annotation.",
    "reason": "Hydropathy can support broad region predictions but does not establish these precise boundaries or the complete keyed set from the input alone."
  },
  "case_id": "transmembrane_0019",
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
      "C13",
      "C14",
      "C15"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence matches the UniProt sequence, whose annotated transmembrane intervals match choice C exactly. The feature evidence is computational (ECO:0000255), not evidence of experimental confirmation."
  },
  "important_caveats": [
    "The matching database feature annotations are computationally evidenced, not shown here to be experimentally determined.",
    "The reviewer-only database identity and annotations were not part of the original model input."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "C",
      "D"
    ],
    "reason": "Choices C and D differ only in the boundaries of one strongly hydrophobic segment; the sequence alone does not clearly settle those few-residue boundary differences."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0019",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence matches the UniProt sequence, whose annotated transmembrane intervals match choice C exactly. The feature evidence is computational (ECO:0000255), not evidence of experimental confirmation.",
    "evidence_ids": ["C5", "C6", "C7", "C8", "C9", "C10", "C11", "C12", "C13", "C14", "C15"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence contains multiple hydrophobic stretches, which supports predicting a multi-pass membrane protein and its broad transmembrane regions.",
    "missing_item_specific_fact": "The exact annotated interval boundaries, including whether the helix at 348..368 or 346..372 is intended, are not supplied and require a protein-specific prediction or annotation.",
    "reason": "Hydropathy can support broad region predictions but does not establish these precise boundaries or the complete keyed set from the input alone."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["C", "D"],
    "reason": "Choices C and D differ only in the boundaries of one strongly hydrophobic segment; the sequence alone does not clearly settle those few-residue boundary differences."
  },
  "important_caveats": [
    "The matching database feature annotations are computationally evidenced, not shown here to be experimentally determined.",
    "The reviewer-only database identity and annotations were not part of the original model input."
  ]
}
```

</details>

## Before: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> Choice C (1..21; 38..58; 72..92; 125..145; 154..174; 255..275; 284..304; 318..338; 348..368; 398..418; 427..447) matches the UniProtKB annotation for A0A455ZIM5 exactly across all 11 transmembrane features. The sequence SHA256 matches. However, all annotations carry evidence code ECO:0000255 (inferred by similarity), meaning they are computational predictions rather than experimental measurements.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [C9](#evidence-c9), [C10](#evidence-c10), [C11](#evidence-c11), [C12](#evidence-c12), [C13](#evidence-c13), [C14](#evidence-c14), [C15](#evidence-c15), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6), [H7](#evidence-h7), [H8](#evidence-h8), [H9](#evidence-h9), [H10](#evidence-h10), [H11](#evidence-h11), [H12](#evidence-h12), [H13](#evidence-h13).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> Choice B can be eliminated by general reasoning: its TM coordinates (27..47, 82..102, etc.) do not correspond to obvious hydrophobic stretches in the sequence. The MFS transporter family topology (6+6 TM arrangement) is general knowledge and could guide rough placement. However, the critical distinctions among the remaining choices—whether 38..58 qualifies as a TM (A vs C) and whether the ninth TM is 348..368 vs 346..372 (C vs D)—depend on the specific output of a prediction algorithm (e.g., TMHMM/Phobius) applied to this sequence, not on general biological principles.


**Missing item-specific fact**

> The exact TM boundary predictions generated by the specific algorithm(s) used for the UniProt annotation (ECO:0000255, by similarity). Distinguishing 348..368 from 346..372, or deciding whether the moderately hydrophobic stretch at 38..58 (GFLATYAGASVFFSVPAGWAA) crosses the membrane, requires the specific computational prediction rather than general hydrophobicity reasoning.


**Reason**

> While general knowledge of MFS topology and hydrophobic stretch identification can narrow choices (eliminating B), the fine-grained boundary differences between A/C/D (±2-4 residues, inclusion/exclusion of a borderline TM) are artifacts of a specific prediction algorithm. A model without access to the UniProt entry or the exact prediction tool output cannot reliably distinguish C from D or A from C using first-principles biology alone.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "C",
  "D"
]
```

> The only difference between C and D is the ninth TM: 348..368 vs 346..372. The sequence around this region (positions 346-372: NVALFCTILALNGIGLAVVTSPGYVEAIDV) contains mixed hydrophobic and polar residues, making both boundaries plausible for a TM helix. Similarly, A vs C differs only by the inclusion of 38..58 (GFLATYAGASVFFSVPAGWAA), a borderline hydrophobic stretch. Without the specific prediction algorithm, both C and D are defensible.


### Important caveats

- All 11 TM annotations carry ECO:0000255 (inferred by similarity), indicating computational prediction rather than experimental validation (e.g., crystal structure or cross-linking).
- The UniProt entry was first released 2025-02-05; the author's source snapshot is unknown but sequence matches across versions.
- MFS transporters canonically have 12 TMs; this annotation lists 11, which is within the known variation of the family.
- The protein is from Metarhizium majus (a fungus), an MFS-type transporter involved in pyrrolopyrazine biosynthesis—no experimental structure exists for this specific protein.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Choice B can be eliminated by general reasoning: its TM coordinates (27..47, 82..102, etc.) do not correspond to obvious hydrophobic stretches in the sequence. The MFS transporter family topology (6+6 TM arrangement) is general knowledge and could guide rough placement. However, the critical distinctions among the remaining choices—whether 38..58 qualifies as a TM (A vs C) and whether the ninth TM is 348..368 vs 346..372 (C vs D)—depend on the specific output of a prediction algorithm (e.g., TMHMM/Phobius) applied to this sequence, not on general biological principles.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The exact TM boundary predictions generated by the specific algorithm(s) used for the UniProt annotation (ECO:0000255, by similarity). Distinguishing 348..368 from 346..372, or deciding whether the moderately hydrophobic stretch at 38..58 (GFLATYAGASVFFSVPAGWAA) crosses the membrane, requires the specific computational prediction rather than general hydrophobicity reasoning.",
    "reason": "While general knowledge of MFS topology and hydrophobic stretch identification can narrow choices (eliminating B), the fine-grained boundary differences between A/C/D (±2-4 residues, inclusion/exclusion of a borderline TM) are artifacts of a specific prediction algorithm. A model without access to the UniProt entry or the exact prediction tool output cannot reliably distinguish C from D or A from C using first-principles biology alone."
  },
  "case_id": "transmembrane_0019",
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
      "C13",
      "C14",
      "C15",
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
      "H13"
    ],
    "judgment": "supported",
    "reason": "Choice C (1..21; 38..58; 72..92; 125..145; 154..174; 255..275; 284..304; 318..338; 348..368; 398..418; 427..447) matches the UniProtKB annotation for A0A455ZIM5 exactly across all 11 transmembrane features. The sequence SHA256 matches. However, all annotations carry evidence code ECO:0000255 (inferred by similarity), meaning they are computational predictions rather than experimental measurements."
  },
  "important_caveats": [
    "All 11 TM annotations carry ECO:0000255 (inferred by similarity), indicating computational prediction rather than experimental validation (e.g., crystal structure or cross-linking).",
    "The UniProt entry was first released 2025-02-05; the author's source snapshot is unknown but sequence matches across versions.",
    "MFS transporters canonically have 12 TMs; this annotation lists 11, which is within the known variation of the family.",
    "The protein is from Metarhizium majus (a fungus), an MFS-type transporter involved in pyrrolopyrazine biosynthesis—no experimental structure exists for this specific protein."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "C",
      "D"
    ],
    "reason": "The only difference between C and D is the ninth TM: 348..368 vs 346..372. The sequence around this region (positions 346-372: NVALFCTILALNGIGLAVVTSPGYVEAIDV) contains mixed hydrophobic and polar residues, making both boundaries plausible for a TM helix. Similarly, A vs C differs only by the inclusion of 38..58 (GFLATYAGASVFFSVPAGWAA), a borderline hydrophobic stretch. Without the specific prediction algorithm, both C and D are defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0019",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "Choice C (1..21; 38..58; 72..92; 125..145; 154..174; 255..275; 284..304; 318..338; 348..368; 398..418; 427..447) matches the UniProtKB annotation for A0A455ZIM5 exactly across all 11 transmembrane features. The sequence SHA256 matches. However, all annotations carry evidence code ECO:0000255 (inferred by similarity), meaning they are computational predictions rather than experimental measurements.",
    "evidence_ids": ["C5","C6","C7","C8","C9","C10","C11","C12","C13","C14","C15","H3","H4","H5","H6","H7","H8","H9","H10","H11","H12","H13"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "Choice B can be eliminated by general reasoning: its TM coordinates (27..47, 82..102, etc.) do not correspond to obvious hydrophobic stretches in the sequence. The MFS transporter family topology (6+6 TM arrangement) is general knowledge and could guide rough placement. However, the critical distinctions among the remaining choices—whether 38..58 qualifies as a TM (A vs C) and whether the ninth TM is 348..368 vs 346..372 (C vs D)—depend on the specific output of a prediction algorithm (e.g., TMHMM/Phobius) applied to this sequence, not on general biological principles.",
    "missing_item_specific_fact": "The exact TM boundary predictions generated by the specific algorithm(s) used for the UniProt annotation (ECO:0000255, by similarity). Distinguishing 348..368 from 346..372, or deciding whether the moderately hydrophobic stretch at 38..58 (GFLATYAGASVFFSVPAGWAA) crosses the membrane, requires the specific computational prediction rather than general hydrophobicity reasoning.",
    "reason": "While general knowledge of MFS topology and hydrophobic stretch identification can narrow choices (eliminating B), the fine-grained boundary differences between A/C/D (±2-4 residues, inclusion/exclusion of a borderline TM) are artifacts of a specific prediction algorithm. A model without access to the UniProt entry or the exact prediction tool output cannot reliably distinguish C from D or A from C using first-principles biology alone."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["C", "D"],
    "reason": "The only difference between C and D is the ninth TM: 348..368 vs 346..372. The sequence around this region (positions 346-372: NVALFCTILALNGIGLAVVTSPGYVEAIDV) contains mixed hydrophobic and polar residues, making both boundaries plausible for a TM helix. Similarly, A vs C differs only by the inclusion of 38..58 (GFLATYAGASVFFSVPAGWAA), a borderline hydrophobic stretch. Without the specific prediction algorithm, both C and D are defensible."
  },
  "important_caveats": [
    "All 11 TM annotations carry ECO:0000255 (inferred by similarity), indicating computational prediction rather than experimental validation (e.g., crystal structure or cross-linking).",
    "The UniProt entry was first released 2025-02-05; the author's source snapshot is unknown but sequence matches across versions.",
    "MFS transporters canonically have 12 TMs; this annotation lists 11, which is within the known variation of the family.",
    "The protein is from Metarhizium majus (a fungus), an MFS-type transporter involved in pyrrolopyrazine biosynthesis—no experimental structure exists for this specific protein."
  ]
}
```

</details>

## After: GPT-6 Luna

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence-matched UniProt entry annotates the eleven transmembrane intervals listed in choice C. These are computational annotations (ECO:0000255), not evidence of experimental measurement, but they support the key for this sequence.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [C9](#evidence-c9), [C10](#evidence-c10), [C11](#evidence-c11), [C12](#evidence-c12), [C13](#evidence-c13), [C14](#evidence-c14), [C15](#evidence-c15).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains repeated long hydrophobic stretches characteristic of transmembrane helices in a multi-pass transporter. Those features support the intervals in C and distinguish them from the many nonmatching intervals and out-of-range coordinate in B; in particular, the hydrophobic stretch around 38..58 supports including that interval, unlike A. The hydrophobic core also favors C's 348..368 interval over D's broader 346..372 range, which includes less hydrophobic flanks.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Family-level knowledge of multi-pass transporters and transferable hydropathy patterns provide a concrete basis for selecting C from these alternatives. Sequence-based boundary estimates are not exact, but the offered alternatives differ in ways the sequence can meaningfully discriminate.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> C and D are close, but the hydrophobic core supports C's narrower interval; D extends beyond it into less hydrophobic flanks.


### Important caveats

- The supporting database annotations are computational rather than experimental.
- Exact transmembrane boundaries can be uncertain when inferred from sequence alone.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains repeated long hydrophobic stretches characteristic of transmembrane helices in a multi-pass transporter. Those features support the intervals in C and distinguish them from the many nonmatching intervals and out-of-range coordinate in B; in particular, the hydrophobic stretch around 38..58 supports including that interval, unlike A. The hydrophobic core also favors C's 348..368 interval over D's broader 346..372 range, which includes less hydrophobic flanks.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Family-level knowledge of multi-pass transporters and transferable hydropathy patterns provide a concrete basis for selecting C from these alternatives. Sequence-based boundary estimates are not exact, but the offered alternatives differ in ways the sequence can meaningfully discriminate."
  },
  "case_id": "transmembrane_0019",
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
      "C13",
      "C14",
      "C15"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt entry annotates the eleven transmembrane intervals listed in choice C. These are computational annotations (ECO:0000255), not evidence of experimental measurement, but they support the key for this sequence."
  },
  "important_caveats": [
    "The supporting database annotations are computational rather than experimental.",
    "Exact transmembrane boundaries can be uncertain when inferred from sequence alone."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "C and D are close, but the hydrophobic core supports C's narrower interval; D extends beyond it into less hydrophobic flanks."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0019",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt entry annotates the eleven transmembrane intervals listed in choice C. These are computational annotations (ECO:0000255), not evidence of experimental measurement, but they support the key for this sequence.",
    "evidence_ids": ["C5", "C6", "C7", "C8", "C9", "C10", "C11", "C12", "C13", "C14", "C15"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains repeated long hydrophobic stretches characteristic of transmembrane helices in a multi-pass transporter. Those features support the intervals in C and distinguish them from the many nonmatching intervals and out-of-range coordinate in B; in particular, the hydrophobic stretch around 38..58 supports including that interval, unlike A. The hydrophobic core also favors C's 348..368 interval over D's broader 346..372 range, which includes less hydrophobic flanks.",
    "missing_item_specific_fact": "",
    "reason": "Family-level knowledge of multi-pass transporters and transferable hydropathy patterns provide a concrete basis for selecting C from these alternatives. Sequence-based boundary estimates are not exact, but the offered alternatives differ in ways the sequence can meaningfully discriminate."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "C and D are close, but the hydrophobic core supports C's narrower interval; D extends beyond it into less hydrophobic flanks."
  },
  "important_caveats": [
    "The supporting database annotations are computational rather than experimental.",
    "Exact transmembrane boundaries can be uncertain when inferred from sequence alone."
  ]
}
```

</details>

## After: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A0A455ZIM5 (PPZB_METMF) annotates exactly 11 transmembrane helical regions at positions 1..21, 38..58, 72..92, 125..145, 154..174, 255..275, 284..304, 318..338, 348..368, 398..418, and 427..447, matching option C precisely. All annotations carry evidence code ECO:0000255 (similarity-based/computational inference), not experimental data, but the sequence match is confirmed (SHA-256 identical). The protein is identified as an MFS-type transporter (ppzB), a family with a canonical 12-TM-helix architecture (11 annotated here).

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [C9](#evidence-c9), [C10](#evidence-c10), [C11](#evidence-c11), [C12](#evidence-c12), [C13](#evidence-c13), [C14](#evidence-c14), [C15](#evidence-c15), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6), [H7](#evidence-h7), [H8](#evidence-h8), [H9](#evidence-h9), [H10](#evidence-h10), [H11](#evidence-h11), [H12](#evidence-h12), [H13](#evidence-h13).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Several transferable lines of reasoning distinguish C from the alternatives. (1) Eliminating B: Option B's proposed TM regions (e.g., 27..47 = IPNAELQHYTSGFLATYAGAS) contain multiple charged/polar residues (N, E, Q, H, R, S, T), which are strongly incompatible with a membrane-spanning alpha-helix. A basic hydrophobicity scan of the sequence shows the true hydrophobic stretches begin at residue 1 (MGLFTDLVLYGIVLPALPFIM), not at 27. B's numbering appears shifted by ~26 positions and does not correspond to actual hydrophobic segments. (2) Eliminating A: Option A omits the region 38..58 (GFLATYAGASVFFSVPAGWAA), which is moderately hydrophobic (F, L, A, V, F, F, V, A, G, W, A, A). More importantly, this protein exhibits the hallmark large hydrophilic cytoplasmic loop around residues 180–250 (KKAAVKFESPCLIRSSAERSDHVASAPTVVEAQERTHEGTPLLPQDDDDDSDRYKIDRELGSIVQAIPLLYCFREPRLH), characteristic of Major Facilitator Superfamily (MFS) transporters, which canonically possess 12 TM helices (6+6 topology). Option A provides only 10 TM regions, too few for the MFS fold. (3) Distinguishing C from D: The sole difference is one helix boundary—C gives 348..368 (21 residues) while D gives 346..372 (27 residues). Position 346 is Glutamate (E), a charged residue highly unfavorable in the hydrophobic membrane interior, and position 369 is Proline (P), a well-known helix-breaking residue. Standard TM-helix definitions (e.g., TMHMM, Phobius) typically exclude such residues from the TM segment. The 21-residue length in C is also more consistent with the canonical MFS TM-helix length (~20–22 residues) than the 27-residue span in D. These are general biophysical principles applicable to any membrane protein, not facts specific to this protein.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can use: (a) hydrophobicity analysis to reject B's polar 'TM' regions; (b) MFS-family topology knowledge (large cytoplasmic loop, ~12 TM helices) to reject A's 10-helix count; (c) general membrane biophysics (charged Glu and helix-breaking Pro are incompatible with TM helix interiors) to reject D's extended boundary. These are transferable principles learned from the broader membrane-protein literature, not annotations specific to this exact protein.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> While the C-vs-D distinction is fine (only 2 residues on each side of one helix), the presence of a charged Glu (E346) and a helix-breaking Pro (P369) in D's extension provides a clear biophysical argument favoring C. No other pair of options is similarly ambiguous: A is missing an entire helix, and B's regions are grossly misaligned with hydrophobic stretches.


### Important caveats

- All UniProt TM annotations use evidence code ECO:0000255 (similarity-based/computational), not experimental structure or cross-linking data. The 'correct' answer reflects a computational prediction transferred by homology.
- The C-vs-D distinction (348..368 vs 346..372) is at the precision boundary where different TM prediction tools (TMHMM, Phobius, DeepTMHMM) may disagree. The biophysical argument against E and P in the TM core is strong but not absolute—some validated TM helices do contain buried charged residues or prolines.
- The MFS 12-TM-helix canonical count is a family-level expectation; this protein is annotated with 11, which is within the observed range for MFS members. The argument against A (10 helices) relies on the family expectation but is not an absolute rule.
- The reviewer-only UniProt accession and organism identity (Metarhizium majus, MFS-type transporter ppzB) were not available to the evaluated model; the reasoning above relies only on sequence-level features and family-level knowledge.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Several transferable lines of reasoning distinguish C from the alternatives. (1) Eliminating B: Option B's proposed TM regions (e.g., 27..47 = IPNAELQHYTSGFLATYAGAS) contain multiple charged/polar residues (N, E, Q, H, R, S, T), which are strongly incompatible with a membrane-spanning alpha-helix. A basic hydrophobicity scan of the sequence shows the true hydrophobic stretches begin at residue 1 (MGLFTDLVLYGIVLPALPFIM), not at 27. B's numbering appears shifted by ~26 positions and does not correspond to actual hydrophobic segments. (2) Eliminating A: Option A omits the region 38..58 (GFLATYAGASVFFSVPAGWAA), which is moderately hydrophobic (F, L, A, V, F, F, V, A, G, W, A, A). More importantly, this protein exhibits the hallmark large hydrophilic cytoplasmic loop around residues 180–250 (KKAAVKFESPCLIRSSAERSDHVASAPTVVEAQERTHEGTPLLPQDDDDDSDRYKIDRELGSIVQAIPLLYCFREPRLH), characteristic of Major Facilitator Superfamily (MFS) transporters, which canonically possess 12 TM helices (6+6 topology). Option A provides only 10 TM regions, too few for the MFS fold. (3) Distinguishing C from D: The sole difference is one helix boundary—C gives 348..368 (21 residues) while D gives 346..372 (27 residues). Position 346 is Glutamate (E), a charged residue highly unfavorable in the hydrophobic membrane interior, and position 369 is Proline (P), a well-known helix-breaking residue. Standard TM-helix definitions (e.g., TMHMM, Phobius) typically exclude such residues from the TM segment. The 21-residue length in C is also more consistent with the canonical MFS TM-helix length (~20–22 residues) than the 27-residue span in D. These are general biophysical principles applicable to any membrane protein, not facts specific to this protein.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can use: (a) hydrophobicity analysis to reject B's polar 'TM' regions; (b) MFS-family topology knowledge (large cytoplasmic loop, ~12 TM helices) to reject A's 10-helix count; (c) general membrane biophysics (charged Glu and helix-breaking Pro are incompatible with TM helix interiors) to reject D's extended boundary. These are transferable principles learned from the broader membrane-protein literature, not annotations specific to this exact protein."
  },
  "case_id": "transmembrane_0019",
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
      "C13",
      "C14",
      "C15",
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
      "H13"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry A0A455ZIM5 (PPZB_METMF) annotates exactly 11 transmembrane helical regions at positions 1..21, 38..58, 72..92, 125..145, 154..174, 255..275, 284..304, 318..338, 348..368, 398..418, and 427..447, matching option C precisely. All annotations carry evidence code ECO:0000255 (similarity-based/computational inference), not experimental data, but the sequence match is confirmed (SHA-256 identical). The protein is identified as an MFS-type transporter (ppzB), a family with a canonical 12-TM-helix architecture (11 annotated here)."
  },
  "important_caveats": [
    "All UniProt TM annotations use evidence code ECO:0000255 (similarity-based/computational), not experimental structure or cross-linking data. The 'correct' answer reflects a computational prediction transferred by homology.",
    "The C-vs-D distinction (348..368 vs 346..372) is at the precision boundary where different TM prediction tools (TMHMM, Phobius, DeepTMHMM) may disagree. The biophysical argument against E and P in the TM core is strong but not absolute—some validated TM helices do contain buried charged residues or prolines.",
    "The MFS 12-TM-helix canonical count is a family-level expectation; this protein is annotated with 11, which is within the observed range for MFS members. The argument against A (10 helices) relies on the family expectation but is not an absolute rule.",
    "The reviewer-only UniProt accession and organism identity (Metarhizium majus, MFS-type transporter ppzB) were not available to the evaluated model; the reasoning above relies only on sequence-level features and family-level knowledge."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While the C-vs-D distinction is fine (only 2 residues on each side of one helix), the presence of a charged Glu (E346) and a helix-breaking Pro (P369) in D's extension provides a clear biophysical argument favoring C. No other pair of options is similarly ambiguous: A is missing an entire helix, and B's regions are grossly misaligned with hydrophobic stretches."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0019",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A0A455ZIM5 (PPZB_METMF) annotates exactly 11 transmembrane helical regions at positions 1..21, 38..58, 72..92, 125..145, 154..174, 255..275, 284..304, 318..338, 348..368, 398..418, and 427..447, matching option C precisely. All annotations carry evidence code ECO:0000255 (similarity-based/computational inference), not experimental data, but the sequence match is confirmed (SHA-256 identical). The protein is identified as an MFS-type transporter (ppzB), a family with a canonical 12-TM-helix architecture (11 annotated here).",
    "evidence_ids": ["C5", "C6", "C7", "C8", "C9", "C10", "C11", "C12", "C13", "C14", "C15", "H3", "H4", "H5", "H6", "H7", "H8", "H9", "H10", "H11", "H12", "H13"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Several transferable lines of reasoning distinguish C from the alternatives. (1) Eliminating B: Option B's proposed TM regions (e.g., 27..47 = IPNAELQHYTSGFLATYAGAS) contain multiple charged/polar residues (N, E, Q, H, R, S, T), which are strongly incompatible with a membrane-spanning alpha-helix. A basic hydrophobicity scan of the sequence shows the true hydrophobic stretches begin at residue 1 (MGLFTDLVLYGIVLPALPFIM), not at 27. B's numbering appears shifted by ~26 positions and does not correspond to actual hydrophobic segments. (2) Eliminating A: Option A omits the region 38..58 (GFLATYAGASVFFSVPAGWAA), which is moderately hydrophobic (F, L, A, V, F, F, V, A, G, W, A, A). More importantly, this protein exhibits the hallmark large hydrophilic cytoplasmic loop around residues 180–250 (KKAAVKFESPCLIRSSAERSDHVASAPTVVEAQERTHEGTPLLPQDDDDDSDRYKIDRELGSIVQAIPLLYCFREPRLH), characteristic of Major Facilitator Superfamily (MFS) transporters, which canonically possess 12 TM helices (6+6 topology). Option A provides only 10 TM regions, too few for the MFS fold. (3) Distinguishing C from D: The sole difference is one helix boundary—C gives 348..368 (21 residues) while D gives 346..372 (27 residues). Position 346 is Glutamate (E), a charged residue highly unfavorable in the hydrophobic membrane interior, and position 369 is Proline (P), a well-known helix-breaking residue. Standard TM-helix definitions (e.g., TMHMM, Phobius) typically exclude such residues from the TM segment. The 21-residue length in C is also more consistent with the canonical MFS TM-helix length (~20–22 residues) than the 27-residue span in D. These are general biophysical principles applicable to any membrane protein, not facts specific to this protein.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can use: (a) hydrophobicity analysis to reject B's polar 'TM' regions; (b) MFS-family topology knowledge (large cytoplasmic loop, ~12 TM helices) to reject A's 10-helix count; (c) general membrane biophysics (charged Glu and helix-breaking Pro are incompatible with TM helix interiors) to reject D's extended boundary. These are transferable principles learned from the broader membrane-protein literature, not annotations specific to this exact protein."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While the C-vs-D distinction is fine (only 2 residues on each side of one helix), the presence of a charged Glu (E346) and a helix-breaking Pro (P369) in D's extension provides a clear biophysical argument favoring C. No other pair of options is similarly ambiguous: A is missing an entire helix, and B's regions are grossly misaligned with hydrophobic stretches."
  },
  "important_caveats": [
    "All UniProt TM annotations use evidence code ECO:0000255 (similarity-based/computational), not experimental structure or cross-linking data. The 'correct' answer reflects a computational prediction transferred by homology.",
    "The C-vs-D distinction (348..368 vs 346..372) is at the precision boundary where different TM prediction tools (TMHMM, Phobius, DeepTMHMM) may disagree. The biophysical argument against E and P in the TM core is strong but not absolute—some validated TM helices do contain buried charged residues or prolines.",
    "The MFS 12-TM-helix canonical count is a family-level expectation; this protein is annotated with 11, which is within the observed range for MFS members. The argument against A (10 helices) relies on the family expectation but is not an absolute rule.",
    "The reviewer-only UniProt accession and organism identity (Metarhizium majus, MFS-type transporter ppzB) were not available to the evaluated model; the reasoning above relies only on sequence-level features and family-level knowledge."
  ]
}
```

</details>

## Existing project source checks of the old Luna review only

These unchanged notes concern the earlier Luna claims. They do not validate either new review or the old Qwen review. No new scientific adjudication was performed.

## Project source-check notes

These project-authored, AI-assisted checks assess specific source claims. They are not expert adjudication and do not replace Luna’s saved review or the author key.

No additional case-specific project note was recorded. Citation membership checks do not establish that every scientific argument is correct.

## Complete reviewer-only evidence and qualifications

All excerpts supplied in the original and revised reviewer user message follow. This material was not available to the original evaluated model. Accession identity came from dataset image-path metadata. Source support and transferable discrimination are separate judgments.

**Applicability metadata, unchanged:**

```json
{
  "requested_accession": "A0A455ZIM5",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "benchmark_sequence_sha256": "04f8c5e9e85da67b086773ba9238fcda3b1271a5894d0e923953e09ca0f0172f",
  "benchmark_sequence_length": 456,
  "current_status": "retrieved",
  "current_sequence_comparison": "matched",
  "current_entry_audit": {
    "entryVersion": 18,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-01-28",
    "lastSequenceUpdateDate": "2019-06-05",
    "sequenceVersion": 1
  },
  "current_uniprot_release": "2026_03",
  "current_record_sha256": "6ca07c0a168a625bda1ae7ac7bf6169436a142dafb1eeff3ee0b50ba41ca0dfa",
  "current_source_sequence_sha256": "04f8c5e9e85da67b086773ba9238fcda3b1271a5894d0e923953e09ca0f0172f",
  "current_source_sequence_length": 456,
  "historical_status": "retrieved",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "selected_historical_entry_version": 18,
  "selected_historical_version": {
    "accession": "A0A455ZIM5",
    "database": "Swiss-Prot",
    "entryVersion": 18,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "PPZB_METMF",
    "sequenceVersion": 1
  },
  "selected_historical_record_sha256": "23d1c6a0dd94bf4fb1bfb14ea0ccf66dde7fd98de0a1a6c3dc11a9bda856717c",
  "selected_historical_source_sequence_sha256": "04f8c5e9e85da67b086773ba9238fcda3b1271a5894d0e923953e09ca0f0172f",
  "selected_historical_source_sequence_length": 456,
  "latest_at_cutoff_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 18,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "actual_author_source_snapshot": "unknown",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed."
}
```

**Qualifications, unchanged:**

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A455ZIM5.json)

```json
{
  "evidence_id": "C1",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A455ZIM5.json",
  "source_sha256": "6ca07c0a168a625bda1ae7ac7bf6169436a142dafb1eeff3ee0b50ba41ca0dfa",
  "retrieved_utc": "2026-11-02T04:25:12.764881+00:00",
  "json_pointer": "/primaryAccession",
  "excerpt": "\"A0A455ZIM5\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A455ZIM5.json)

```json
{
  "evidence_id": "C2",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A455ZIM5.json",
  "source_sha256": "6ca07c0a168a625bda1ae7ac7bf6169436a142dafb1eeff3ee0b50ba41ca0dfa",
  "retrieved_utc": "2026-11-02T04:25:12.764881+00:00",
  "json_pointer": "/entryAudit",
  "excerpt": "{\"entryVersion\":18,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-01-28\",\"lastSequenceUpdateDate\":\"2019-06-05\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A455ZIM5.json)

```json
{
  "evidence_id": "C3",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A455ZIM5.json",
  "source_sha256": "6ca07c0a168a625bda1ae7ac7bf6169436a142dafb1eeff3ee0b50ba41ca0dfa",
  "retrieved_utc": "2026-11-02T04:25:12.764881+00:00",
  "json_pointer": "/organism",
  "excerpt": "{\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Sordariomycetes\",\"Hypocreomycetidae\",\"Hypocreales\",\"Clavicipitaceae\",\"Metarhizium\",\"Metarhizium majus\"],\"scientificName\":\"Metarhizium majus (strain ARSEF 297)\",\"taxonId\":1276143}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A455ZIM5.json)

```json
{
  "evidence_id": "C4",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A455ZIM5.json",
  "source_sha256": "6ca07c0a168a625bda1ae7ac7bf6169436a142dafb1eeff3ee0b50ba41ca0dfa",
  "retrieved_utc": "2026-11-02T04:25:12.764881+00:00",
  "json_pointer": "/proteinDescription",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"30452111\",\"source\":\"PubMed\"}],\"value\":\"Pyrrolopyrazine biosynthesis cluster protein B\"}}],\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"30452111\",\"source\":\"PubMed\"}],\"value\":\"MFS-type transporter ppzB\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A455ZIM5.json)

```json
{
  "evidence_id": "C5",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A455ZIM5.json",
  "source_sha256": "6ca07c0a168a625bda1ae7ac7bf6169436a142dafb1eeff3ee0b50ba41ca0dfa",
  "retrieved_utc": "2026-11-02T04:25:12.764881+00:00",
  "json_pointer": "/features/1",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":21},\"start\":{\"modifier\":\"EXACT\",\"value\":1}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A455ZIM5.json)

```json
{
  "evidence_id": "C6",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A455ZIM5.json",
  "source_sha256": "6ca07c0a168a625bda1ae7ac7bf6169436a142dafb1eeff3ee0b50ba41ca0dfa",
  "retrieved_utc": "2026-11-02T04:25:12.764881+00:00",
  "json_pointer": "/features/2",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":58},\"start\":{\"modifier\":\"EXACT\",\"value\":38}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A455ZIM5.json)

```json
{
  "evidence_id": "C7",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A455ZIM5.json",
  "source_sha256": "6ca07c0a168a625bda1ae7ac7bf6169436a142dafb1eeff3ee0b50ba41ca0dfa",
  "retrieved_utc": "2026-11-02T04:25:12.764881+00:00",
  "json_pointer": "/features/3",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":92},\"start\":{\"modifier\":\"EXACT\",\"value\":72}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A455ZIM5.json)

```json
{
  "evidence_id": "C8",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A455ZIM5.json",
  "source_sha256": "6ca07c0a168a625bda1ae7ac7bf6169436a142dafb1eeff3ee0b50ba41ca0dfa",
  "retrieved_utc": "2026-11-02T04:25:12.764881+00:00",
  "json_pointer": "/features/4",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":145},\"start\":{\"modifier\":\"EXACT\",\"value\":125}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A455ZIM5.json)

```json
{
  "evidence_id": "C9",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A455ZIM5.json",
  "source_sha256": "6ca07c0a168a625bda1ae7ac7bf6169436a142dafb1eeff3ee0b50ba41ca0dfa",
  "retrieved_utc": "2026-11-02T04:25:12.764881+00:00",
  "json_pointer": "/features/5",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":174},\"start\":{\"modifier\":\"EXACT\",\"value\":154}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A455ZIM5.json)

```json
{
  "evidence_id": "C10",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A455ZIM5.json",
  "source_sha256": "6ca07c0a168a625bda1ae7ac7bf6169436a142dafb1eeff3ee0b50ba41ca0dfa",
  "retrieved_utc": "2026-11-02T04:25:12.764881+00:00",
  "json_pointer": "/features/6",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":275},\"start\":{\"modifier\":\"EXACT\",\"value\":255}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A455ZIM5.json)

```json
{
  "evidence_id": "C11",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A455ZIM5.json",
  "source_sha256": "6ca07c0a168a625bda1ae7ac7bf6169436a142dafb1eeff3ee0b50ba41ca0dfa",
  "retrieved_utc": "2026-11-02T04:25:12.764881+00:00",
  "json_pointer": "/features/7",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":304},\"start\":{\"modifier\":\"EXACT\",\"value\":284}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A455ZIM5.json)

```json
{
  "evidence_id": "C12",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A455ZIM5.json",
  "source_sha256": "6ca07c0a168a625bda1ae7ac7bf6169436a142dafb1eeff3ee0b50ba41ca0dfa",
  "retrieved_utc": "2026-11-02T04:25:12.764881+00:00",
  "json_pointer": "/features/8",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":338},\"start\":{\"modifier\":\"EXACT\",\"value\":318}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C13

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A455ZIM5.json)

```json
{
  "evidence_id": "C13",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A455ZIM5.json",
  "source_sha256": "6ca07c0a168a625bda1ae7ac7bf6169436a142dafb1eeff3ee0b50ba41ca0dfa",
  "retrieved_utc": "2026-11-02T04:25:12.764881+00:00",
  "json_pointer": "/features/9",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":368},\"start\":{\"modifier\":\"EXACT\",\"value\":348}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C14

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A455ZIM5.json)

```json
{
  "evidence_id": "C14",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A455ZIM5.json",
  "source_sha256": "6ca07c0a168a625bda1ae7ac7bf6169436a142dafb1eeff3ee0b50ba41ca0dfa",
  "retrieved_utc": "2026-11-02T04:25:12.764881+00:00",
  "json_pointer": "/features/10",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":418},\"start\":{\"modifier\":\"EXACT\",\"value\":398}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C15

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A455ZIM5.json)

```json
{
  "evidence_id": "C15",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A455ZIM5.json",
  "source_sha256": "6ca07c0a168a625bda1ae7ac7bf6169436a142dafb1eeff3ee0b50ba41ca0dfa",
  "retrieved_utc": "2026-11-02T04:25:12.764881+00:00",
  "json_pointer": "/features/11",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":447},\"start\":{\"modifier\":\"EXACT\",\"value\":427}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C16

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A455ZIM5.json)

```json
{
  "evidence_id": "C16",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A455ZIM5.json",
  "source_sha256": "6ca07c0a168a625bda1ae7ac7bf6169436a142dafb1eeff3ee0b50ba41ca0dfa",
  "retrieved_utc": "2026-11-02T04:25:12.764881+00:00",
  "json_pointer": "/references/0",
  "excerpt": "{\"citation\":{\"authors\":[\"Berry D.\",\"Mace W.\",\"Rehner S.A.\",\"Grage K.\",\"Dijkwel P.P.\",\"Young C.A.\",\"Scott B.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"30452111\"},{\"database\":\"DOI\",\"id\":\"10.1111/1462-2920.14483\"}],\"citationType\":\"journal article\",\"firstPage\":\"928\",\"id\":\"30452111\",\"journal\":\"Environ. Microbiol.\",\"lastPage\":\"939\",\"publicationDate\":\"2019\",\"title\":\"Orthologous peramine and pyrrolopyrazine-producing biosynthetic gene clusters in Metarhizium rileyi, Metarhizium majus and Cladonia grayi.\",\"volume\":\"21\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"ARSEF 297\"}],\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [GENOMIC DNA]\",\"FUNCTION\",\"PATHWAY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A455ZIM5?format=txt&versions=18)

```json
{
  "evidence_id": "H1",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A455ZIM5?format=txt&versions=18",
  "source_sha256": "23d1c6a0dd94bf4fb1bfb14ea0ccf66dde7fd98de0a1a6c3dc11a9bda856717c",
  "retrieved_utc": "2026-11-02T04:25:16.028134+00:00",
  "source_locator": "lines 1-13",
  "excerpt": "ID   PPZB_METMF              Reviewed;         456 AA.\nAC   A0A455ZIM5;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   05-JUN-2019, sequence version 1.\nDT   28-JAN-2026, entry version 18.\nDE   RecName: Full=MFS-type transporter ppzB {ECO:0000303|PubMed:30452111};\nDE   AltName: Full=Pyrrolopyrazine biosynthesis cluster protein B {ECO:0000303|PubMed:30452111};\nGN   Name=ppzB;\nOS   Metarhizium majus (strain ARSEF 297).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Sordariomycetes;\nOC   Hypocreomycetidae; Hypocreales; Clavicipitaceae; Metarhizium;\nOC   Metarhizium majus.\nOX   NCBI_TaxID=1276143;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 18,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A455ZIM5?format=txt&versions=18)

```json
{
  "evidence_id": "H2",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A455ZIM5?format=txt&versions=18",
  "source_sha256": "23d1c6a0dd94bf4fb1bfb14ea0ccf66dde7fd98de0a1a6c3dc11a9bda856717c",
  "retrieved_utc": "2026-11-02T04:25:16.028134+00:00",
  "source_locator": "lines 14-22",
  "excerpt": "RN   [1]\nRP   NUCLEOTIDE SEQUENCE [GENOMIC DNA], FUNCTION, AND PATHWAY.\nRC   STRAIN=ARSEF 297;\nRX   PubMed=30452111; DOI=10.1111/1462-2920.14483;\nRA   Berry D., Mace W., Rehner S.A., Grage K., Dijkwel P.P., Young C.A.,\nRA   Scott B.;\nRT   \"Orthologous peramine and pyrrolopyrazine-producing biosynthetic gene\nRT   clusters in Metarhizium rileyi, Metarhizium majus and Cladonia grayi.\";\nRL   Environ. Microbiol. 21:928-939(2019).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 18,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A455ZIM5?format=txt&versions=18)

```json
{
  "evidence_id": "H3",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A455ZIM5?format=txt&versions=18",
  "source_sha256": "23d1c6a0dd94bf4fb1bfb14ea0ccf66dde7fd98de0a1a6c3dc11a9bda856717c",
  "retrieved_utc": "2026-11-02T04:25:16.028134+00:00",
  "source_locator": "lines 65-67",
  "excerpt": "FT   TRANSMEM        1..21\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 18,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A455ZIM5?format=txt&versions=18)

```json
{
  "evidence_id": "H4",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A455ZIM5?format=txt&versions=18",
  "source_sha256": "23d1c6a0dd94bf4fb1bfb14ea0ccf66dde7fd98de0a1a6c3dc11a9bda856717c",
  "retrieved_utc": "2026-11-02T04:25:16.028134+00:00",
  "source_locator": "lines 68-70",
  "excerpt": "FT   TRANSMEM        38..58\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 18,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A455ZIM5?format=txt&versions=18)

```json
{
  "evidence_id": "H5",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A455ZIM5?format=txt&versions=18",
  "source_sha256": "23d1c6a0dd94bf4fb1bfb14ea0ccf66dde7fd98de0a1a6c3dc11a9bda856717c",
  "retrieved_utc": "2026-11-02T04:25:16.028134+00:00",
  "source_locator": "lines 71-73",
  "excerpt": "FT   TRANSMEM        72..92\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 18,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A455ZIM5?format=txt&versions=18)

```json
{
  "evidence_id": "H6",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A455ZIM5?format=txt&versions=18",
  "source_sha256": "23d1c6a0dd94bf4fb1bfb14ea0ccf66dde7fd98de0a1a6c3dc11a9bda856717c",
  "retrieved_utc": "2026-11-02T04:25:16.028134+00:00",
  "source_locator": "lines 74-76",
  "excerpt": "FT   TRANSMEM        125..145\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 18,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A455ZIM5?format=txt&versions=18)

```json
{
  "evidence_id": "H7",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A455ZIM5?format=txt&versions=18",
  "source_sha256": "23d1c6a0dd94bf4fb1bfb14ea0ccf66dde7fd98de0a1a6c3dc11a9bda856717c",
  "retrieved_utc": "2026-11-02T04:25:16.028134+00:00",
  "source_locator": "lines 77-79",
  "excerpt": "FT   TRANSMEM        154..174\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 18,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A455ZIM5?format=txt&versions=18)

```json
{
  "evidence_id": "H8",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A455ZIM5?format=txt&versions=18",
  "source_sha256": "23d1c6a0dd94bf4fb1bfb14ea0ccf66dde7fd98de0a1a6c3dc11a9bda856717c",
  "retrieved_utc": "2026-11-02T04:25:16.028134+00:00",
  "source_locator": "lines 80-82",
  "excerpt": "FT   TRANSMEM        255..275\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 18,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A455ZIM5?format=txt&versions=18)

```json
{
  "evidence_id": "H9",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A455ZIM5?format=txt&versions=18",
  "source_sha256": "23d1c6a0dd94bf4fb1bfb14ea0ccf66dde7fd98de0a1a6c3dc11a9bda856717c",
  "retrieved_utc": "2026-11-02T04:25:16.028134+00:00",
  "source_locator": "lines 83-85",
  "excerpt": "FT   TRANSMEM        284..304\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 18,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H10

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A455ZIM5?format=txt&versions=18)

```json
{
  "evidence_id": "H10",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A455ZIM5?format=txt&versions=18",
  "source_sha256": "23d1c6a0dd94bf4fb1bfb14ea0ccf66dde7fd98de0a1a6c3dc11a9bda856717c",
  "retrieved_utc": "2026-11-02T04:25:16.028134+00:00",
  "source_locator": "lines 86-88",
  "excerpt": "FT   TRANSMEM        318..338\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 18,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H11

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A455ZIM5?format=txt&versions=18)

```json
{
  "evidence_id": "H11",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A455ZIM5?format=txt&versions=18",
  "source_sha256": "23d1c6a0dd94bf4fb1bfb14ea0ccf66dde7fd98de0a1a6c3dc11a9bda856717c",
  "retrieved_utc": "2026-11-02T04:25:16.028134+00:00",
  "source_locator": "lines 89-91",
  "excerpt": "FT   TRANSMEM        348..368\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 18,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H12

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A455ZIM5?format=txt&versions=18)

```json
{
  "evidence_id": "H12",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A455ZIM5?format=txt&versions=18",
  "source_sha256": "23d1c6a0dd94bf4fb1bfb14ea0ccf66dde7fd98de0a1a6c3dc11a9bda856717c",
  "retrieved_utc": "2026-11-02T04:25:16.028134+00:00",
  "source_locator": "lines 92-94",
  "excerpt": "FT   TRANSMEM        398..418\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 18,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H13

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A455ZIM5?format=txt&versions=18)

```json
{
  "evidence_id": "H13",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A455ZIM5?format=txt&versions=18",
  "source_sha256": "23d1c6a0dd94bf4fb1bfb14ea0ccf66dde7fd98de0a1a6c3dc11a9bda856717c",
  "retrieved_utc": "2026-11-02T04:25:16.028134+00:00",
  "source_locator": "lines 95-97",
  "excerpt": "FT   TRANSMEM        427..447\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 18,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json), zero-based source row 19. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
