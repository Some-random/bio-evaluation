# transmembrane_0019

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `transmembrane`  
**Author expected answer:** **C** — 1..21; 38..58; 72..92; 125..145; 154..174; 255..275; 284..304; 318..338; 348..368; 398..418; 427..447

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

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

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

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

## Existing project source checks of Luna’s review

The notes below were prepared for specific claims in the Luna review. They are not independent validation of Qwen’s claims, expert adjudication, or replacement verdicts.

## Project source-check notes

These project-authored, AI-assisted checks assess specific source claims. They are not expert adjudication and do not replace Luna’s saved review or the author key.

No additional case-specific project note was recorded. Citation membership checks do not establish that every scientific argument is correct.

## Reviewer-only source evidence

**Both reviewers received this source evidence separately from the original question. It was not available to the original evaluated model.** Source support and reasoning from the original sequence/choices are distinct assessments.

**Accession:** `A0A455ZIM5` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 18. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A455ZIM5.json)  
**Locator:** `/features/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:12.764881+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":21},"start":{"modifier":"EXACT","value":1}},"type":"Transmembrane"}
```

Source SHA-256: `6ca07c0a168a625bda1ae7ac7bf6169436a142dafb1eeff3ee0b50ba41ca0dfa`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A455ZIM5.json)  
**Locator:** `/features/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:12.764881+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":58},"start":{"modifier":"EXACT","value":38}},"type":"Transmembrane"}
```

Source SHA-256: `6ca07c0a168a625bda1ae7ac7bf6169436a142dafb1eeff3ee0b50ba41ca0dfa`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A455ZIM5.json)  
**Locator:** `/features/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:12.764881+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":92},"start":{"modifier":"EXACT","value":72}},"type":"Transmembrane"}
```

Source SHA-256: `6ca07c0a168a625bda1ae7ac7bf6169436a142dafb1eeff3ee0b50ba41ca0dfa`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A455ZIM5.json)  
**Locator:** `/features/4`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:12.764881+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":145},"start":{"modifier":"EXACT","value":125}},"type":"Transmembrane"}
```

Source SHA-256: `6ca07c0a168a625bda1ae7ac7bf6169436a142dafb1eeff3ee0b50ba41ca0dfa`.

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A455ZIM5.json)  
**Locator:** `/features/5`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:12.764881+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":174},"start":{"modifier":"EXACT","value":154}},"type":"Transmembrane"}
```

Source SHA-256: `6ca07c0a168a625bda1ae7ac7bf6169436a142dafb1eeff3ee0b50ba41ca0dfa`.

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A455ZIM5.json)  
**Locator:** `/features/6`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:12.764881+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":275},"start":{"modifier":"EXACT","value":255}},"type":"Transmembrane"}
```

Source SHA-256: `6ca07c0a168a625bda1ae7ac7bf6169436a142dafb1eeff3ee0b50ba41ca0dfa`.

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A455ZIM5.json)  
**Locator:** `/features/7`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:12.764881+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":304},"start":{"modifier":"EXACT","value":284}},"type":"Transmembrane"}
```

Source SHA-256: `6ca07c0a168a625bda1ae7ac7bf6169436a142dafb1eeff3ee0b50ba41ca0dfa`.

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A455ZIM5.json)  
**Locator:** `/features/8`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:12.764881+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":338},"start":{"modifier":"EXACT","value":318}},"type":"Transmembrane"}
```

Source SHA-256: `6ca07c0a168a625bda1ae7ac7bf6169436a142dafb1eeff3ee0b50ba41ca0dfa`.

### Evidence C13

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A455ZIM5.json)  
**Locator:** `/features/9`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:12.764881+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":368},"start":{"modifier":"EXACT","value":348}},"type":"Transmembrane"}
```

Source SHA-256: `6ca07c0a168a625bda1ae7ac7bf6169436a142dafb1eeff3ee0b50ba41ca0dfa`.

### Evidence C14

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A455ZIM5.json)  
**Locator:** `/features/10`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:12.764881+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":418},"start":{"modifier":"EXACT","value":398}},"type":"Transmembrane"}
```

Source SHA-256: `6ca07c0a168a625bda1ae7ac7bf6169436a142dafb1eeff3ee0b50ba41ca0dfa`.

### Evidence C15

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A455ZIM5.json)  
**Locator:** `/features/11`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:12.764881+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":447},"start":{"modifier":"EXACT","value":427}},"type":"Transmembrane"}
```

Source SHA-256: `6ca07c0a168a625bda1ae7ac7bf6169436a142dafb1eeff3ee0b50ba41ca0dfa`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A455ZIM5?format=txt&versions=18)  
**Locator:** `lines 65-67`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 18 / 1.  
**Retrieved:** 2026-11-02T04:25:16.028134+00:00.  

```text
FT   TRANSMEM        1..21
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `23d1c6a0dd94bf4fb1bfb14ea0ccf66dde7fd98de0a1a6c3dc11a9bda856717c`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A455ZIM5?format=txt&versions=18)  
**Locator:** `lines 68-70`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 18 / 1.  
**Retrieved:** 2026-11-02T04:25:16.028134+00:00.  

```text
FT   TRANSMEM        38..58
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `23d1c6a0dd94bf4fb1bfb14ea0ccf66dde7fd98de0a1a6c3dc11a9bda856717c`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A455ZIM5?format=txt&versions=18)  
**Locator:** `lines 71-73`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 18 / 1.  
**Retrieved:** 2026-11-02T04:25:16.028134+00:00.  

```text
FT   TRANSMEM        72..92
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `23d1c6a0dd94bf4fb1bfb14ea0ccf66dde7fd98de0a1a6c3dc11a9bda856717c`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A455ZIM5?format=txt&versions=18)  
**Locator:** `lines 74-76`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 18 / 1.  
**Retrieved:** 2026-11-02T04:25:16.028134+00:00.  

```text
FT   TRANSMEM        125..145
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `23d1c6a0dd94bf4fb1bfb14ea0ccf66dde7fd98de0a1a6c3dc11a9bda856717c`.

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A455ZIM5?format=txt&versions=18)  
**Locator:** `lines 77-79`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 18 / 1.  
**Retrieved:** 2026-11-02T04:25:16.028134+00:00.  

```text
FT   TRANSMEM        154..174
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `23d1c6a0dd94bf4fb1bfb14ea0ccf66dde7fd98de0a1a6c3dc11a9bda856717c`.

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A455ZIM5?format=txt&versions=18)  
**Locator:** `lines 80-82`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 18 / 1.  
**Retrieved:** 2026-11-02T04:25:16.028134+00:00.  

```text
FT   TRANSMEM        255..275
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `23d1c6a0dd94bf4fb1bfb14ea0ccf66dde7fd98de0a1a6c3dc11a9bda856717c`.

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A455ZIM5?format=txt&versions=18)  
**Locator:** `lines 83-85`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 18 / 1.  
**Retrieved:** 2026-11-02T04:25:16.028134+00:00.  

```text
FT   TRANSMEM        284..304
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `23d1c6a0dd94bf4fb1bfb14ea0ccf66dde7fd98de0a1a6c3dc11a9bda856717c`.

### Evidence H10

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A455ZIM5?format=txt&versions=18)  
**Locator:** `lines 86-88`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 18 / 1.  
**Retrieved:** 2026-11-02T04:25:16.028134+00:00.  

```text
FT   TRANSMEM        318..338
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `23d1c6a0dd94bf4fb1bfb14ea0ccf66dde7fd98de0a1a6c3dc11a9bda856717c`.

### Evidence H11

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A455ZIM5?format=txt&versions=18)  
**Locator:** `lines 89-91`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 18 / 1.  
**Retrieved:** 2026-11-02T04:25:16.028134+00:00.  

```text
FT   TRANSMEM        348..368
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `23d1c6a0dd94bf4fb1bfb14ea0ccf66dde7fd98de0a1a6c3dc11a9bda856717c`.

### Evidence H12

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A455ZIM5?format=txt&versions=18)  
**Locator:** `lines 92-94`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 18 / 1.  
**Retrieved:** 2026-11-02T04:25:16.028134+00:00.  

```text
FT   TRANSMEM        398..418
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `23d1c6a0dd94bf4fb1bfb14ea0ccf66dde7fd98de0a1a6c3dc11a9bda856717c`.

### Evidence H13

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A455ZIM5?format=txt&versions=18)  
**Locator:** `lines 95-97`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 18 / 1.  
**Retrieved:** 2026-11-02T04:25:16.028134+00:00.  

```text
FT   TRANSMEM        427..447
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `23d1c6a0dd94bf4fb1bfb14ea0ccf66dde7fd98de0a1a6c3dc11a9bda856717c`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json), zero-based source row 19. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
