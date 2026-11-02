# transmembrane_0045

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `transmembrane`  
**Author expected answer:** **C** — 113..133; 143..163; 166..186; 234..254; 275..295; 384..404; 413..433; 437..457; 473..493

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MTALDTDTPTAGRSAPLISPGPVIPPPDFGPLDRAQGWAMTAIITALAAITRFLNLGSPTDAGTPIFDEKHYAPQAWQVLHNDGVEDNPGYGLVVHPPVGKQLIAIGEWLFGYNGLGWRFSGAVCGVIIVMLVTRIARRISRSTLVGAIAGLLIIADGVSFVSSRTALLDVFLVMFAVAAFACLMVDRDQVRERMYHAFLDGRIAETRWGTRLGVRWWRFGAGVLLGLACATKWSGLYFVLFFGVMTLVFDAIARKQYHVPHPWRGMLRRDLGPAAYVFGLIPFAVYLASYAPWFASETAVNRYEVGRSIGPDSILPIPDALRSLWHYTHAAYRFHSNLTNADGNHHPWESKPWTWPMSLRPVLYAIDNQDVPGCGAQSCVKAVMLVGTPAMWFIAVPVLGWALWRTVVRRDWRYGAVLVGYMAGFLPWFADIDRQMYFFYATVMAPFLVLAIALILGDILYKPNQNPERRTLGLLTVCFYVALVITNFAWMYPILTGLPISQTTWNLQIWLPSWR

[Multiple Choices]
A. 113..133; 143..163; 166..186; 234..254; 275..295; 382..407; 413..433; 437..457; 473..493
B. 6..26
C. 113..133; 143..163; 166..186; 234..254; 275..295; 384..404; 413..433; 437..457; 473..493
D. 113..133; 143..163; 166..186; 234..254; 275..295; 384..404; 413..433; 437..457
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

> The matched historical UniProt entry annotates all nine regions listed in C, including 384..404 and 473..493. These annotations are computationally evidenced (ECO:0000255), not direct experimental measurements.

Citations as saved: [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6), [H7](#evidence-h7), [H8](#evidence-h8), [H9](#evidence-h9), [H10](#evidence-h10), [H11](#evidence-h11).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence contains multiple strongly hydrophobic stretches consistent with membrane-spanning helices, while 6..26 is not a convincing membrane-spanning segment. This supports the general pattern but does not establish precise helix boundaries.


**Missing item-specific fact**

> The protein-specific annotation or other evidence establishing the chosen boundaries, especially 384..404 rather than the overlapping 382..407, is absent from the input.


**Reason**

> General sequence reasoning can identify likely transmembrane regions, but cannot reliably select exact endpoints for this protein. The reviewer-only database evidence supports the key but was not supplied to the evaluated model.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "C"
]
```

> A and C differ only in the boundaries of an overlapping hydrophobic segment (382..407 versus 384..404); the question gives no boundary convention that distinguishes them biologically.


### Important caveats

- The supporting annotations are computationally evidenced, not experimental confirmation of exact membrane boundaries.
- The historical entry matches the supplied sequence, but the author's exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains multiple strongly hydrophobic stretches consistent with membrane-spanning helices, while 6..26 is not a convincing membrane-spanning segment. This supports the general pattern but does not establish precise helix boundaries.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific annotation or other evidence establishing the chosen boundaries, especially 384..404 rather than the overlapping 382..407, is absent from the input.",
    "reason": "General sequence reasoning can identify likely transmembrane regions, but cannot reliably select exact endpoints for this protein. The reviewer-only database evidence supports the key but was not supplied to the evaluated model."
  },
  "case_id": "transmembrane_0045",
  "expected_answer_check": {
    "evidence_ids": [
      "H3",
      "H4",
      "H5",
      "H6",
      "H7",
      "H8",
      "H9",
      "H10",
      "H11"
    ],
    "judgment": "supported",
    "reason": "The matched historical UniProt entry annotates all nine regions listed in C, including 384..404 and 473..493. These annotations are computationally evidenced (ECO:0000255), not direct experimental measurements."
  },
  "important_caveats": [
    "The supporting annotations are computationally evidenced, not experimental confirmation of exact membrane boundaries.",
    "The historical entry matches the supplied sequence, but the author's exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "C"
    ],
    "reason": "A and C differ only in the boundaries of an overlapping hydrophobic segment (382..407 versus 384..404); the question gives no boundary convention that distinguishes them biologically."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0045",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The matched historical UniProt entry annotates all nine regions listed in C, including 384..404 and 473..493. These annotations are computationally evidenced (ECO:0000255), not direct experimental measurements.",
    "evidence_ids": ["H3", "H4", "H5", "H6", "H7", "H8", "H9", "H10", "H11"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence contains multiple strongly hydrophobic stretches consistent with membrane-spanning helices, while 6..26 is not a convincing membrane-spanning segment. This supports the general pattern but does not establish precise helix boundaries.",
    "missing_item_specific_fact": "The protein-specific annotation or other evidence establishing the chosen boundaries, especially 384..404 rather than the overlapping 382..407, is absent from the input.",
    "reason": "General sequence reasoning can identify likely transmembrane regions, but cannot reliably select exact endpoints for this protein. The reviewer-only database evidence supports the key but was not supplied to the evaluated model."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "C"],
    "reason": "A and C differ only in the boundaries of an overlapping hydrophobic segment (382..407 versus 384..404); the question gives no boundary convention that distinguishes them biologically."
  },
  "important_caveats": [
    "The supporting annotations are computationally evidenced, not experimental confirmation of exact membrane boundaries.",
    "The historical entry matches the supplied sequence, but the author's exact source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A0R3E8 (PMT_MYCS2, Mycolicibacterium smegmatis) annotates exactly 9 transmembrane helical regions at positions 113..133, 143..163, 166..186, 234..254, 275..295, 384..404, 413..433, 437..457, and 473..493, matching Choice C verbatim. The sequence in the question matches the UniProt sequence (SHA-256 confirmed). All annotations carry evidence code ECO:0000255 (by similarity), meaning they are computational predictions transferred from related proteins rather than experimental measurements.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [C9](#evidence-c9), [C10](#evidence-c10), [C11](#evidence-c11), [C12](#evidence-c12), [C13](#evidence-c13), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6), [H7](#evidence-h7), [H8](#evidence-h8), [H9](#evidence-h9), [H10](#evidence-h10), [H11](#evidence-h11).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> A model can identify the general presence of multiple hydrophobic stretches (~20-25 residues) consistent with TM helices, and can note a hydrophobic C-terminal segment near position 473-493 that supports the existence of a 9th TM (distinguishing C from D). However, the critical A-vs-C distinction (382..407 vs 384..404 for the 6th TM) is a 2-residue boundary shift at both ends, which falls entirely within the ±2-3 residue uncertainty inherent to any hydrophobicity-based TM prediction algorithm. No general biological principle (hydrophobicity threshold, helix length, flanking charge) can definitively resolve whether the TM starts at 382 or 384 or ends at 404 or 407.


**Missing item-specific fact**

> The exact boundary positions as output by the specific prediction algorithm used by UniProt curators (ECO:0000255, by similarity). Distinguishing 382..407 from 384..404 requires reproducing the exact algorithmic cutoff rather than applying a general biological rule.


**Reason**

> The question presents four choices that differ by only 2 residues in one TM boundary (A vs C) or by the presence/absence of the last TM (C vs D). While the C-vs-D distinction has some sequence-level support (a hydrophobic stretch exists near 473-493), the A-vs-C distinction is unresolvable by general reasoning because 2-residue boundary differences are within the noise of all standard TM predictors. Selecting the exact UniProt-annotated boundaries requires memorizing or looking up the specific database entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "C"
]
```

> Choices A and C differ only in the 6th TM region (382..407 vs 384..404). Both represent plausible hydrophobic stretches of 25-26 or 21-22 residues, respectively. Standard TM prediction tools (TMHMM, Phobius, DeepTMHMM) routinely disagree by 2-3 residues on boundary placement. Without access to the specific algorithm output, both A and C are defensible from sequence analysis alone.


### Important caveats

- All TM annotations carry ECO:0000255 (by similarity), indicating computational prediction transferred from homologs, not experimental validation. The exact boundaries are algorithm-dependent.
- The UniProt entry was first public in June 2025; the author's source snapshot date is unknown, though the sequence has been unchanged since 2007.
- Choice B (6..26) is a trivially wrong distractor corresponding to a short N-terminal hydrophobic stretch insufficient for a TM helix.
- The reviewer-only evidence confirms the sequence match and annotation but was not available to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "A model can identify the general presence of multiple hydrophobic stretches (~20-25 residues) consistent with TM helices, and can note a hydrophobic C-terminal segment near position 473-493 that supports the existence of a 9th TM (distinguishing C from D). However, the critical A-vs-C distinction (382..407 vs 384..404 for the 6th TM) is a 2-residue boundary shift at both ends, which falls entirely within the ±2-3 residue uncertainty inherent to any hydrophobicity-based TM prediction algorithm. No general biological principle (hydrophobicity threshold, helix length, flanking charge) can definitively resolve whether the TM starts at 382 or 384 or ends at 404 or 407.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The exact boundary positions as output by the specific prediction algorithm used by UniProt curators (ECO:0000255, by similarity). Distinguishing 382..407 from 384..404 requires reproducing the exact algorithmic cutoff rather than applying a general biological rule.",
    "reason": "The question presents four choices that differ by only 2 residues in one TM boundary (A vs C) or by the presence/absence of the last TM (C vs D). While the C-vs-D distinction has some sequence-level support (a hydrophobic stretch exists near 473-493), the A-vs-C distinction is unresolvable by general reasoning because 2-residue boundary differences are within the noise of all standard TM predictors. Selecting the exact UniProt-annotated boundaries requires memorizing or looking up the specific database entry."
  },
  "case_id": "transmembrane_0045",
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
      "H3",
      "H4",
      "H5",
      "H6",
      "H7",
      "H8",
      "H9",
      "H10",
      "H11"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry A0R3E8 (PMT_MYCS2, Mycolicibacterium smegmatis) annotates exactly 9 transmembrane helical regions at positions 113..133, 143..163, 166..186, 234..254, 275..295, 384..404, 413..433, 437..457, and 473..493, matching Choice C verbatim. The sequence in the question matches the UniProt sequence (SHA-256 confirmed). All annotations carry evidence code ECO:0000255 (by similarity), meaning they are computational predictions transferred from related proteins rather than experimental measurements."
  },
  "important_caveats": [
    "All TM annotations carry ECO:0000255 (by similarity), indicating computational prediction transferred from homologs, not experimental validation. The exact boundaries are algorithm-dependent.",
    "The UniProt entry was first public in June 2025; the author's source snapshot date is unknown, though the sequence has been unchanged since 2007.",
    "Choice B (6..26) is a trivially wrong distractor corresponding to a short N-terminal hydrophobic stretch insufficient for a TM helix.",
    "The reviewer-only evidence confirms the sequence match and annotation but was not available to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "C"
    ],
    "reason": "Choices A and C differ only in the 6th TM region (382..407 vs 384..404). Both represent plausible hydrophobic stretches of 25-26 or 21-22 residues, respectively. Standard TM prediction tools (TMHMM, Phobius, DeepTMHMM) routinely disagree by 2-3 residues on boundary placement. Without access to the specific algorithm output, both A and C are defensible from sequence analysis alone."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0045",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A0R3E8 (PMT_MYCS2, Mycolicibacterium smegmatis) annotates exactly 9 transmembrane helical regions at positions 113..133, 143..163, 166..186, 234..254, 275..295, 384..404, 413..433, 437..457, and 473..493, matching Choice C verbatim. The sequence in the question matches the UniProt sequence (SHA-256 confirmed). All annotations carry evidence code ECO:0000255 (by similarity), meaning they are computational predictions transferred from related proteins rather than experimental measurements.",
    "evidence_ids": ["C5", "C6", "C7", "C8", "C9", "C10", "C11", "C12", "C13", "H3", "H4", "H5", "H6", "H7", "H8", "H9", "H10", "H11"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "A model can identify the general presence of multiple hydrophobic stretches (~20-25 residues) consistent with TM helices, and can note a hydrophobic C-terminal segment near position 473-493 that supports the existence of a 9th TM (distinguishing C from D). However, the critical A-vs-C distinction (382..407 vs 384..404 for the 6th TM) is a 2-residue boundary shift at both ends, which falls entirely within the ±2-3 residue uncertainty inherent to any hydrophobicity-based TM prediction algorithm. No general biological principle (hydrophobicity threshold, helix length, flanking charge) can definitively resolve whether the TM starts at 382 or 384 or ends at 404 or 407.",
    "missing_item_specific_fact": "The exact boundary positions as output by the specific prediction algorithm used by UniProt curators (ECO:0000255, by similarity). Distinguishing 382..407 from 384..404 requires reproducing the exact algorithmic cutoff rather than applying a general biological rule.",
    "reason": "The question presents four choices that differ by only 2 residues in one TM boundary (A vs C) or by the presence/absence of the last TM (C vs D). While the C-vs-D distinction has some sequence-level support (a hydrophobic stretch exists near 473-493), the A-vs-C distinction is unresolvable by general reasoning because 2-residue boundary differences are within the noise of all standard TM predictors. Selecting the exact UniProt-annotated boundaries requires memorizing or looking up the specific database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "C"],
    "reason": "Choices A and C differ only in the 6th TM region (382..407 vs 384..404). Both represent plausible hydrophobic stretches of 25-26 or 21-22 residues, respectively. Standard TM prediction tools (TMHMM, Phobius, DeepTMHMM) routinely disagree by 2-3 residues on boundary placement. Without access to the specific algorithm output, both A and C are defensible from sequence analysis alone."
  },
  "important_caveats": [
    "All TM annotations carry ECO:0000255 (by similarity), indicating computational prediction transferred from homologs, not experimental validation. The exact boundaries are algorithm-dependent.",
    "The UniProt entry was first public in June 2025; the author's source snapshot date is unknown, though the sequence has been unchanged since 2007.",
    "Choice B (6..26) is a trivially wrong distractor corresponding to a short N-terminal hydrophobic stretch insufficient for a TM helix.",
    "The reviewer-only evidence confirms the sequence match and annotation but was not available to the evaluated model."
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

**Accession:** `A0R3E8` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 114. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0R3E8.json)  
**Locator:** `/features/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:45.822179+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":133},"start":{"modifier":"EXACT","value":113}},"type":"Transmembrane"}
```

Source SHA-256: `7460bfadb65f50b4073bc118af38399e6b1513a5f5a97e209de8bb6435c7ac44`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0R3E8.json)  
**Locator:** `/features/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:45.822179+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":163},"start":{"modifier":"EXACT","value":143}},"type":"Transmembrane"}
```

Source SHA-256: `7460bfadb65f50b4073bc118af38399e6b1513a5f5a97e209de8bb6435c7ac44`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0R3E8.json)  
**Locator:** `/features/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:45.822179+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":186},"start":{"modifier":"EXACT","value":166}},"type":"Transmembrane"}
```

Source SHA-256: `7460bfadb65f50b4073bc118af38399e6b1513a5f5a97e209de8bb6435c7ac44`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0R3E8.json)  
**Locator:** `/features/4`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:45.822179+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":254},"start":{"modifier":"EXACT","value":234}},"type":"Transmembrane"}
```

Source SHA-256: `7460bfadb65f50b4073bc118af38399e6b1513a5f5a97e209de8bb6435c7ac44`.

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0R3E8.json)  
**Locator:** `/features/5`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:45.822179+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":295},"start":{"modifier":"EXACT","value":275}},"type":"Transmembrane"}
```

Source SHA-256: `7460bfadb65f50b4073bc118af38399e6b1513a5f5a97e209de8bb6435c7ac44`.

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0R3E8.json)  
**Locator:** `/features/6`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:45.822179+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":404},"start":{"modifier":"EXACT","value":384}},"type":"Transmembrane"}
```

Source SHA-256: `7460bfadb65f50b4073bc118af38399e6b1513a5f5a97e209de8bb6435c7ac44`.

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0R3E8.json)  
**Locator:** `/features/7`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:45.822179+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":433},"start":{"modifier":"EXACT","value":413}},"type":"Transmembrane"}
```

Source SHA-256: `7460bfadb65f50b4073bc118af38399e6b1513a5f5a97e209de8bb6435c7ac44`.

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0R3E8.json)  
**Locator:** `/features/8`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:45.822179+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":457},"start":{"modifier":"EXACT","value":437}},"type":"Transmembrane"}
```

Source SHA-256: `7460bfadb65f50b4073bc118af38399e6b1513a5f5a97e209de8bb6435c7ac44`.

### Evidence C13

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0R3E8.json)  
**Locator:** `/features/9`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:45.822179+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":493},"start":{"modifier":"EXACT","value":473}},"type":"Transmembrane"}
```

Source SHA-256: `7460bfadb65f50b4073bc118af38399e6b1513a5f5a97e209de8bb6435c7ac44`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0R3E8?format=txt&versions=114)  
**Locator:** `lines 108-110`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 114 / 1.  
**Retrieved:** 2026-11-02T04:26:48.840229+00:00.  

```text
FT   TRANSMEM        113..133
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `4c32d7463b098ec708cba16ef0ffc8465a4a08c5c9abc6fb7d70933bd38435a7`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0R3E8?format=txt&versions=114)  
**Locator:** `lines 111-113`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 114 / 1.  
**Retrieved:** 2026-11-02T04:26:48.840229+00:00.  

```text
FT   TRANSMEM        143..163
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `4c32d7463b098ec708cba16ef0ffc8465a4a08c5c9abc6fb7d70933bd38435a7`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0R3E8?format=txt&versions=114)  
**Locator:** `lines 114-116`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 114 / 1.  
**Retrieved:** 2026-11-02T04:26:48.840229+00:00.  

```text
FT   TRANSMEM        166..186
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `4c32d7463b098ec708cba16ef0ffc8465a4a08c5c9abc6fb7d70933bd38435a7`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0R3E8?format=txt&versions=114)  
**Locator:** `lines 117-119`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 114 / 1.  
**Retrieved:** 2026-11-02T04:26:48.840229+00:00.  

```text
FT   TRANSMEM        234..254
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `4c32d7463b098ec708cba16ef0ffc8465a4a08c5c9abc6fb7d70933bd38435a7`.

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0R3E8?format=txt&versions=114)  
**Locator:** `lines 120-122`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 114 / 1.  
**Retrieved:** 2026-11-02T04:26:48.840229+00:00.  

```text
FT   TRANSMEM        275..295
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `4c32d7463b098ec708cba16ef0ffc8465a4a08c5c9abc6fb7d70933bd38435a7`.

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0R3E8?format=txt&versions=114)  
**Locator:** `lines 123-125`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 114 / 1.  
**Retrieved:** 2026-11-02T04:26:48.840229+00:00.  

```text
FT   TRANSMEM        384..404
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `4c32d7463b098ec708cba16ef0ffc8465a4a08c5c9abc6fb7d70933bd38435a7`.

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0R3E8?format=txt&versions=114)  
**Locator:** `lines 126-128`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 114 / 1.  
**Retrieved:** 2026-11-02T04:26:48.840229+00:00.  

```text
FT   TRANSMEM        413..433
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `4c32d7463b098ec708cba16ef0ffc8465a4a08c5c9abc6fb7d70933bd38435a7`.

### Evidence H10

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0R3E8?format=txt&versions=114)  
**Locator:** `lines 129-131`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 114 / 1.  
**Retrieved:** 2026-11-02T04:26:48.840229+00:00.  

```text
FT   TRANSMEM        437..457
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `4c32d7463b098ec708cba16ef0ffc8465a4a08c5c9abc6fb7d70933bd38435a7`.

### Evidence H11

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0R3E8?format=txt&versions=114)  
**Locator:** `lines 132-134`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 114 / 1.  
**Retrieved:** 2026-11-02T04:26:48.840229+00:00.  

```text
FT   TRANSMEM        473..493
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `4c32d7463b098ec708cba16ef0ffc8465a4a08c5c9abc6fb7d70933bd38435a7`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json), zero-based source row 45. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
