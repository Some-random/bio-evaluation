# transmembrane_0128

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `transmembrane`  
**Author expected answer:** **B** — 278..286; 308..323

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MQAYESGDERGLIYGYVLNGRGGGRRVGRNQIAVLDLLPEESLWLHWDRGVPEAQAWLRDSAGLSEFACDLLLEEATRPRLLDLGAESLLVFLRGVNLNPGAEPEDMVSLRVFADARRVISLRLRPLKAVADLLEDLEAGKGPKTASEVVYYLAHYLTDRVDTLISGIADQLDAVEELVEADERASPDQHQLRTLRRRSAGLRRYLAPQRDIYSQLARYKLSWFVEDDADYWNELNNRLTRNLEELELIRERISVLQEAESRRITERMNRTMYLLGIITGFFLPMSFVTGLLGINVGGIPGADAPHGFWLACLLIGGVATFQWWVFRRLRWL

[Multiple Choices]
A. 278..286; 311..325
B. 278..286; 308..323
C. 24..44; 63..83; 84..104; 151..171; 173..193
D. 278..286
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

> The sequence-matched UniProt record annotates transmembrane regions at 278..286 and 308..323, exactly matching B. Both annotations cite the structural study and PDB 7NH9; this is evidence-linked annotation, not an independent reanalysis of the experiment.

Citations as saved: [C6](#evidence-c6), [C8](#evidence-c8), [H5](#evidence-h5), [H7](#evidence-h7).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The C-terminal sequence contains conspicuously hydrophobic stretches, supporting membrane association and making the many proposed spans in C implausible. But sequence hydrophobicity alone does not establish the precise 278..286 boundary or resolve the small boundary shifts between A and B.


**Missing item-specific fact**

> The protein-specific curated or structurally informed transmembrane boundaries, particularly the short 278..286 segment and the exact endpoints of the C-terminal span.


**Reason**

> The supplied sequence offers a broad hydrophobicity clue but not a reliable basis for reproducing these exact region coordinates; the matching annotation and its structural evidence are reviewer-only.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "B"
]
```

> A and B share the first interval and give closely overlapping coordinates for the same hydrophobic C-terminal region. If the question means approximate residues in a membrane-crossing helix, both ranges are plausible; B is the supported choice for the exact annotated coordinates.


### Important caveats

- The current and archived sequence-matched records support B, but the author's precise source snapshot is unknown.
- The evidence is a curated annotation citing a paper and PDB structure; it should not be described as independently verified here.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The C-terminal sequence contains conspicuously hydrophobic stretches, supporting membrane association and making the many proposed spans in C implausible. But sequence hydrophobicity alone does not establish the precise 278..286 boundary or resolve the small boundary shifts between A and B.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific curated or structurally informed transmembrane boundaries, particularly the short 278..286 segment and the exact endpoints of the C-terminal span.",
    "reason": "The supplied sequence offers a broad hydrophobicity clue but not a reliable basis for reproducing these exact region coordinates; the matching annotation and its structural evidence are reviewer-only."
  },
  "case_id": "transmembrane_0128",
  "expected_answer_check": {
    "evidence_ids": [
      "C6",
      "C8",
      "H5",
      "H7"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates transmembrane regions at 278..286 and 308..323, exactly matching B. Both annotations cite the structural study and PDB 7NH9; this is evidence-linked annotation, not an independent reanalysis of the experiment."
  },
  "important_caveats": [
    "The current and archived sequence-matched records support B, but the author's precise source snapshot is unknown.",
    "The evidence is a curated annotation citing a paper and PDB structure; it should not be described as independently verified here."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "B"
    ],
    "reason": "A and B share the first interval and give closely overlapping coordinates for the same hydrophobic C-terminal region. If the question means approximate residues in a membrane-crossing helix, both ranges are plausible; B is the supported choice for the exact annotated coordinates."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0128",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates transmembrane regions at 278..286 and 308..323, exactly matching B. Both annotations cite the structural study and PDB 7NH9; this is evidence-linked annotation, not an independent reanalysis of the experiment.",
    "evidence_ids": ["C6", "C8", "H5", "H7"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The C-terminal sequence contains conspicuously hydrophobic stretches, supporting membrane association and making the many proposed spans in C implausible. But sequence hydrophobicity alone does not establish the precise 278..286 boundary or resolve the small boundary shifts between A and B.",
    "missing_item_specific_fact": "The protein-specific curated or structurally informed transmembrane boundaries, particularly the short 278..286 segment and the exact endpoints of the C-terminal span.",
    "reason": "The supplied sequence offers a broad hydrophobicity clue but not a reliable basis for reproducing these exact region coordinates; the matching annotation and its structural evidence are reviewer-only."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "B"],
    "reason": "A and B share the first interval and give closely overlapping coordinates for the same hydrophobic C-terminal region. If the question means approximate residues in a membrane-crossing helix, both ranges are plausible; B is the supported choice for the exact annotated coordinates."
  },
  "important_caveats": [
    "The current and archived sequence-matched records support B, but the author's precise source snapshot is unknown.",
    "The evidence is a curated annotation citing a paper and PDB structure; it should not be described as independently verified here."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt annotation for Q9ZIH2 (CmaX, P. aeruginosa PAO1) lists exactly two transmembrane helices: 278-286 and 308-323, both supported by experimental evidence (PubMed:34175341 and cryo-EM structure PDB 7NH9 at 3.03 Å). The flanking topological domains (cytoplasmic 1-277, periplasmic 287-307, cytoplasmic 324-332) are consistent with a two-TM transporter topology. The benchmark sequence matches the canonical entry exactly (SHA-256 match, 332 residues). Choice B (278..286; 308..323) matches the annotation precisely.

Citations as saved: [C6](#evidence-c6), [C8](#evidence-c8), [C5](#evidence-c5), [C7](#evidence-c7), [C9](#evidence-c9), [H5](#evidence-h5), [H7](#evidence-h7), [H4](#evidence-h4), [H6](#evidence-h6), [H8](#evidence-h8).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> Options C and D can be eliminated by general reasoning: C places five TM segments in the N-terminal hydrophilic region (positions 24-193), which is clearly cytoplasmic; D lists only one TM, inconsistent with a membrane-spanning transporter. However, the critical distinction between A (311..325) and B (308..323) is a 3-residue shift in both the start and end of TM2. The sequence around these boundaries (H308-G309-F310 at one end; F323-Q324-W325 at the other) contains mixed hydrophobic/polar residues at both candidate boundaries, making it impossible to reliably assign exact endpoints by hydrophobicity alone. Similarly, TM1 at 278-286 is only 9 residues (far shorter than the canonical ~20-residue TM helix), a structural peculiarity only explainable by the cryo-EM data.


**Missing item-specific fact**

> The exact transmembrane helix boundaries (278-286 and 308-323) as determined by the 3.03 Å cryo-EM structure (PDB 7NH9, Stetsenko et al. 2021). Without this structural data, hydrophobicity-based sequence analysis cannot reliably distinguish a 3-residue boundary shift such as 308-323 vs 311-325, nor explain the unusually short 9-residue TM1.


**Reason**

> While C and D are eliminable by general biological reasoning, the decisive choice between A and B depends on the precise structural boundaries measured by cryo-EM, an item-specific experimental fact not derivable from the sequence alone. Standard hydrophobicity scales and TM-prediction heuristics would not confidently resolve a 3-residue boundary difference in a region containing mixed polar/apolar residues.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "B"
]
```

> From pure sequence hydrophobicity, the boundaries 308-323 (B) and 311-325 (A) are both plausible TM2 assignments. Position 311 is a tryptophan (a classic membrane-interface residue), which could arguably favor A's start. Position 325 is also a tryptophan, while 323 is phenylalanine. Without the cryo-EM structure, a hydrophobicity-based predictor could reasonably select either boundary. The 3-residue shift is within the typical error margin of sequence-based TM prediction tools.


### Important caveats

- The TM1 annotation (278-286, only 9 residues) is unusually short for a transmembrane helix and is defined by the cryo-EM structure rather than by canonical hydrophobic-length criteria.
- The UniProt annotation carries evidence codes ECO:0000269 (PubMed experimental) and ECO:0007744 (PDB structure), indicating the boundaries are experimentally determined, not purely computational.
- The accession Q9ZIH2 was inferred from reviewer-only metadata; the evaluated model received only the raw sequence without any database identifier.
- The entry was first publicly released in Feb 2025; depending on the author's data-construction date, this annotation may or may not have been available in the author's source snapshot, though the sequence itself dates to 1999.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Options C and D can be eliminated by general reasoning: C places five TM segments in the N-terminal hydrophilic region (positions 24-193), which is clearly cytoplasmic; D lists only one TM, inconsistent with a membrane-spanning transporter. However, the critical distinction between A (311..325) and B (308..323) is a 3-residue shift in both the start and end of TM2. The sequence around these boundaries (H308-G309-F310 at one end; F323-Q324-W325 at the other) contains mixed hydrophobic/polar residues at both candidate boundaries, making it impossible to reliably assign exact endpoints by hydrophobicity alone. Similarly, TM1 at 278-286 is only 9 residues (far shorter than the canonical ~20-residue TM helix), a structural peculiarity only explainable by the cryo-EM data.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The exact transmembrane helix boundaries (278-286 and 308-323) as determined by the 3.03 Å cryo-EM structure (PDB 7NH9, Stetsenko et al. 2021). Without this structural data, hydrophobicity-based sequence analysis cannot reliably distinguish a 3-residue boundary shift such as 308-323 vs 311-325, nor explain the unusually short 9-residue TM1.",
    "reason": "While C and D are eliminable by general biological reasoning, the decisive choice between A and B depends on the precise structural boundaries measured by cryo-EM, an item-specific experimental fact not derivable from the sequence alone. Standard hydrophobicity scales and TM-prediction heuristics would not confidently resolve a 3-residue boundary difference in a region containing mixed polar/apolar residues."
  },
  "case_id": "transmembrane_0128",
  "expected_answer_check": {
    "evidence_ids": [
      "C6",
      "C8",
      "C5",
      "C7",
      "C9",
      "H5",
      "H7",
      "H4",
      "H6",
      "H8"
    ],
    "judgment": "supported",
    "reason": "UniProt annotation for Q9ZIH2 (CmaX, P. aeruginosa PAO1) lists exactly two transmembrane helices: 278-286 and 308-323, both supported by experimental evidence (PubMed:34175341 and cryo-EM structure PDB 7NH9 at 3.03 Å). The flanking topological domains (cytoplasmic 1-277, periplasmic 287-307, cytoplasmic 324-332) are consistent with a two-TM transporter topology. The benchmark sequence matches the canonical entry exactly (SHA-256 match, 332 residues). Choice B (278..286; 308..323) matches the annotation precisely."
  },
  "important_caveats": [
    "The TM1 annotation (278-286, only 9 residues) is unusually short for a transmembrane helix and is defined by the cryo-EM structure rather than by canonical hydrophobic-length criteria.",
    "The UniProt annotation carries evidence codes ECO:0000269 (PubMed experimental) and ECO:0007744 (PDB structure), indicating the boundaries are experimentally determined, not purely computational.",
    "The accession Q9ZIH2 was inferred from reviewer-only metadata; the evaluated model received only the raw sequence without any database identifier.",
    "The entry was first publicly released in Feb 2025; depending on the author's data-construction date, this annotation may or may not have been available in the author's source snapshot, though the sequence itself dates to 1999."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "B"
    ],
    "reason": "From pure sequence hydrophobicity, the boundaries 308-323 (B) and 311-325 (A) are both plausible TM2 assignments. Position 311 is a tryptophan (a classic membrane-interface residue), which could arguably favor A's start. Position 325 is also a tryptophan, while 323 is phenylalanine. Without the cryo-EM structure, a hydrophobicity-based predictor could reasonably select either boundary. The 3-residue shift is within the typical error margin of sequence-based TM prediction tools."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0128",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt annotation for Q9ZIH2 (CmaX, P. aeruginosa PAO1) lists exactly two transmembrane helices: 278-286 and 308-323, both supported by experimental evidence (PubMed:34175341 and cryo-EM structure PDB 7NH9 at 3.03 Å). The flanking topological domains (cytoplasmic 1-277, periplasmic 287-307, cytoplasmic 324-332) are consistent with a two-TM transporter topology. The benchmark sequence matches the canonical entry exactly (SHA-256 match, 332 residues). Choice B (278..286; 308..323) matches the annotation precisely.",
    "evidence_ids": ["C6", "C8", "C5", "C7", "C9", "H5", "H7", "H4", "H6", "H8"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "Options C and D can be eliminated by general reasoning: C places five TM segments in the N-terminal hydrophilic region (positions 24-193), which is clearly cytoplasmic; D lists only one TM, inconsistent with a membrane-spanning transporter. However, the critical distinction between A (311..325) and B (308..323) is a 3-residue shift in both the start and end of TM2. The sequence around these boundaries (H308-G309-F310 at one end; F323-Q324-W325 at the other) contains mixed hydrophobic/polar residues at both candidate boundaries, making it impossible to reliably assign exact endpoints by hydrophobicity alone. Similarly, TM1 at 278-286 is only 9 residues (far shorter than the canonical ~20-residue TM helix), a structural peculiarity only explainable by the cryo-EM data.",
    "missing_item_specific_fact": "The exact transmembrane helix boundaries (278-286 and 308-323) as determined by the 3.03 Å cryo-EM structure (PDB 7NH9, Stetsenko et al. 2021). Without this structural data, hydrophobicity-based sequence analysis cannot reliably distinguish a 3-residue boundary shift such as 308-323 vs 311-325, nor explain the unusually short 9-residue TM1.",
    "reason": "While C and D are eliminable by general biological reasoning, the decisive choice between A and B depends on the precise structural boundaries measured by cryo-EM, an item-specific experimental fact not derivable from the sequence alone. Standard hydrophobicity scales and TM-prediction heuristics would not confidently resolve a 3-residue boundary difference in a region containing mixed polar/apolar residues."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "B"],
    "reason": "From pure sequence hydrophobicity, the boundaries 308-323 (B) and 311-325 (A) are both plausible TM2 assignments. Position 311 is a tryptophan (a classic membrane-interface residue), which could arguably favor A's start. Position 325 is also a tryptophan, while 323 is phenylalanine. Without the cryo-EM structure, a hydrophobicity-based predictor could reasonably select either boundary. The 3-residue shift is within the typical error margin of sequence-based TM prediction tools."
  },
  "important_caveats": [
    "The TM1 annotation (278-286, only 9 residues) is unusually short for a transmembrane helix and is defined by the cryo-EM structure rather than by canonical hydrophobic-length criteria.",
    "The UniProt annotation carries evidence codes ECO:0000269 (PubMed experimental) and ECO:0007744 (PDB structure), indicating the boundaries are experimentally determined, not purely computational.",
    "The accession Q9ZIH2 was inferred from reviewer-only metadata; the evaluated model received only the raw sequence without any database identifier.",
    "The entry was first publicly released in Feb 2025; depending on the author's data-construction date, this annotation may or may not have been available in the author's source snapshot, though the sequence itself dates to 1999."
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

**Accession:** `Q9ZIH2` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 153. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9ZIH2.json)  
**Locator:** `/features/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:54.880542+00:00.  

```json
{"description":"Cytoplasmic","evidences":[{"evidenceCode":"ECO:0000269","id":"34175341","source":"PubMed"}],"location":{"end":{"modifier":"EXACT","value":277},"start":{"modifier":"EXACT","value":1}},"type":"Topological domain"}
```

Source SHA-256: `a00f4c0271bbd4fae7afeb16e71be27aaff79dadde11086a04686cc2d5355d0e`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9ZIH2.json)  
**Locator:** `/features/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:54.880542+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000269","id":"34175341","source":"PubMed"},{"evidenceCode":"ECO:0007744","id":"7NH9","source":"PDB"}],"location":{"end":{"modifier":"EXACT","value":286},"start":{"modifier":"EXACT","value":278}},"type":"Transmembrane"}
```

Source SHA-256: `a00f4c0271bbd4fae7afeb16e71be27aaff79dadde11086a04686cc2d5355d0e`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9ZIH2.json)  
**Locator:** `/features/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:54.880542+00:00.  

```json
{"description":"Periplasmic","evidences":[{"evidenceCode":"ECO:0000269","id":"34175341","source":"PubMed"}],"location":{"end":{"modifier":"EXACT","value":307},"start":{"modifier":"EXACT","value":287}},"type":"Topological domain"}
```

Source SHA-256: `a00f4c0271bbd4fae7afeb16e71be27aaff79dadde11086a04686cc2d5355d0e`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9ZIH2.json)  
**Locator:** `/features/4`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:54.880542+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000269","id":"34175341","source":"PubMed"},{"evidenceCode":"ECO:0007744","id":"7NH9","source":"PDB"}],"location":{"end":{"modifier":"EXACT","value":323},"start":{"modifier":"EXACT","value":308}},"type":"Transmembrane"}
```

Source SHA-256: `a00f4c0271bbd4fae7afeb16e71be27aaff79dadde11086a04686cc2d5355d0e`.

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9ZIH2.json)  
**Locator:** `/features/5`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:54.880542+00:00.  

```json
{"description":"Cytoplasmic","evidences":[{"evidenceCode":"ECO:0000269","id":"34175341","source":"PubMed"}],"location":{"end":{"modifier":"EXACT","value":332},"start":{"modifier":"EXACT","value":324}},"type":"Topological domain"}
```

Source SHA-256: `a00f4c0271bbd4fae7afeb16e71be27aaff79dadde11086a04686cc2d5355d0e`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9ZIH2?format=txt&versions=153)  
**Locator:** `lines 122-124`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 153 / 1.  
**Retrieved:** 2026-11-02T04:33:58.139616+00:00.  

```text
FT   TOPO_DOM        1..277
FT                   /note="Cytoplasmic"
FT                   /evidence="ECO:0000269|PubMed:34175341"
```

Source SHA-256: `ef1f3b913665475f320bd32d9a7e46b733d69ecc2d4104881ec5fd04fc3481b9`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9ZIH2?format=txt&versions=153)  
**Locator:** `lines 125-128`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 153 / 1.  
**Retrieved:** 2026-11-02T04:33:58.139616+00:00.  

```text
FT   TRANSMEM        278..286
FT                   /note="Helical"
FT                   /evidence="ECO:0000269|PubMed:34175341,
FT                   ECO:0007744|PDB:7NH9"
```

Source SHA-256: `ef1f3b913665475f320bd32d9a7e46b733d69ecc2d4104881ec5fd04fc3481b9`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9ZIH2?format=txt&versions=153)  
**Locator:** `lines 129-131`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 153 / 1.  
**Retrieved:** 2026-11-02T04:33:58.139616+00:00.  

```text
FT   TOPO_DOM        287..307
FT                   /note="Periplasmic"
FT                   /evidence="ECO:0000269|PubMed:34175341"
```

Source SHA-256: `ef1f3b913665475f320bd32d9a7e46b733d69ecc2d4104881ec5fd04fc3481b9`.

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9ZIH2?format=txt&versions=153)  
**Locator:** `lines 132-135`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 153 / 1.  
**Retrieved:** 2026-11-02T04:33:58.139616+00:00.  

```text
FT   TRANSMEM        308..323
FT                   /note="Helical"
FT                   /evidence="ECO:0000269|PubMed:34175341,
FT                   ECO:0007744|PDB:7NH9"
```

Source SHA-256: `ef1f3b913665475f320bd32d9a7e46b733d69ecc2d4104881ec5fd04fc3481b9`.

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9ZIH2?format=txt&versions=153)  
**Locator:** `lines 136-138`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 153 / 1.  
**Retrieved:** 2026-11-02T04:33:58.139616+00:00.  

```text
FT   TOPO_DOM        324..332
FT                   /note="Cytoplasmic"
FT                   /evidence="ECO:0000269|PubMed:34175341"
```

Source SHA-256: `ef1f3b913665475f320bd32d9a7e46b733d69ecc2d4104881ec5fd04fc3481b9`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json), zero-based source row 128. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
