# transmembrane_0128: before and after transfer clarification

[All 1,328 cases](../README.md) · [Method](../METHOD.md) · [Summary](../SUMMARY.md) · [Exact reviewer user message](../inputs/transmembrane_0128.txt)

**Task:** `transmembrane`  
**Author key, unchanged:** **B** — 278..286; 308..323

| Round | Reviewer | Key support | Transfer / lookup | Output usability (canonical status) |
|---|---|---|---|---|
| before | GPT-6 Luna | supported | lookup-dependent | usable output (valid_review) |
| before | Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | usable output (valid_review) |
| after | GPT-6 Luna | supported | lookup-dependent | usable output (valid_review) |
| after | Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | usable output (valid_review) |

**Usable output means format-valid review, not reasoning-supported or biologically correct.** A usable output can classify the question as reasoning-supported, lookup-dependent or uncertain. An output error is a problem with the saved model response; it does not count a defective benchmark question or wrong key. Each saved review is retained in full below. Labels from output errors are displayed as saved and excluded from label statistics. The author key and reviewer evidence were visible to reviewers; this is a review of answerability and key support, not a benchmark-solving score.

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

## Before: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

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

## After: GPT-6 Luna

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence-matched UniProt record annotates transmembrane regions at 278..286 and 308..323, matching B. The annotations cite experimental evidence and the 7NH9 structure; this supports the key, though the primary study was not independently reviewed here.

Citations as saved: [C6](#evidence-c6), [C8](#evidence-c8), [H5](#evidence-h5), [H7](#evidence-h7).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence has a C-terminal hydrophobic region consistent with membrane-spanning helices, and transferable transporter knowledge could distinguish those options from the N-terminal, mostly nonhydrophobic regions in C. It does not, however, establish whether the second span should be placed at 308..323 or 311..325: both intervals cover a strongly hydrophobic stretch.


**Missing item-specific fact**

> The exact annotated or structurally assigned boundaries of the second transmembrane segment are needed to distinguish B from A.


**Reason**

> Sequence hydropathy and family-level reasoning support the general location and number of membrane spans, but do not meaningfully resolve the small boundary shift between A and B. The keyed coordinates are supported by reviewer-only evidence, not uniquely recoverable from the original input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "B"
]
```

> A and B share the same first interval and give overlapping, strongly hydrophobic windows for the second span. The sequence alone does not specify those precise endpoints, and either window is a plausible membrane-spanning segment.


### Important caveats

- Reviewer-only annotations match the supplied sequence; the cited evidence includes experimental and structural evidence, but the underlying paper was not independently validated.
- The exact extent assigned to a transmembrane helix can depend on structural or annotation conventions.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has a C-terminal hydrophobic region consistent with membrane-spanning helices, and transferable transporter knowledge could distinguish those options from the N-terminal, mostly nonhydrophobic regions in C. It does not, however, establish whether the second span should be placed at 308..323 or 311..325: both intervals cover a strongly hydrophobic stretch.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The exact annotated or structurally assigned boundaries of the second transmembrane segment are needed to distinguish B from A.",
    "reason": "Sequence hydropathy and family-level reasoning support the general location and number of membrane spans, but do not meaningfully resolve the small boundary shift between A and B. The keyed coordinates are supported by reviewer-only evidence, not uniquely recoverable from the original input."
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
    "reason": "The sequence-matched UniProt record annotates transmembrane regions at 278..286 and 308..323, matching B. The annotations cite experimental evidence and the 7NH9 structure; this supports the key, though the primary study was not independently reviewed here."
  },
  "important_caveats": [
    "Reviewer-only annotations match the supplied sequence; the cited evidence includes experimental and structural evidence, but the underlying paper was not independently validated.",
    "The exact extent assigned to a transmembrane helix can depend on structural or annotation conventions."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "B"
    ],
    "reason": "A and B share the same first interval and give overlapping, strongly hydrophobic windows for the second span. The sequence alone does not specify those precise endpoints, and either window is a plausible membrane-spanning segment."
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
    "reason": "The sequence-matched UniProt record annotates transmembrane regions at 278..286 and 308..323, matching B. The annotations cite experimental evidence and the 7NH9 structure; this supports the key, though the primary study was not independently reviewed here.",
    "evidence_ids": ["C6", "C8", "H5", "H7"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence has a C-terminal hydrophobic region consistent with membrane-spanning helices, and transferable transporter knowledge could distinguish those options from the N-terminal, mostly nonhydrophobic regions in C. It does not, however, establish whether the second span should be placed at 308..323 or 311..325: both intervals cover a strongly hydrophobic stretch.",
    "missing_item_specific_fact": "The exact annotated or structurally assigned boundaries of the second transmembrane segment are needed to distinguish B from A.",
    "reason": "Sequence hydropathy and family-level reasoning support the general location and number of membrane spans, but do not meaningfully resolve the small boundary shift between A and B. The keyed coordinates are supported by reviewer-only evidence, not uniquely recoverable from the original input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "B"],
    "reason": "A and B share the same first interval and give overlapping, strongly hydrophobic windows for the second span. The sequence alone does not specify those precise endpoints, and either window is a plausible membrane-spanning segment."
  },
  "important_caveats": [
    "Reviewer-only annotations match the supplied sequence; the cited evidence includes experimental and structural evidence, but the underlying paper was not independently validated.",
    "The exact extent assigned to a transmembrane helix can depend on structural or annotation conventions."
  ]
}
```

</details>

## After: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt annotation for Q9ZIH2 (CmaX/ZntB from P. aeruginosa) records exactly two transmembrane helices: 278..286 and 308..323, both supported by cryo-EM structure PDB 7NH9 (3.03 Å) and experimental topology data (PubMed 34175341). The topological domains confirm cytoplasmic 1-277, periplasmic loop 287-307, and cytoplasmic 324-332, consistent with exactly two membrane-spanning helices at the annotated positions. Choice B matches these boundaries exactly.

Citations as saved: [C6](#evidence-c6), [C8](#evidence-c8), [C5](#evidence-c5), [C7](#evidence-c7), [C9](#evidence-c9), [H5](#evidence-h5), [H7](#evidence-h7).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Multiple layers of transferable reasoning distinguish B from the alternatives: (1) The N-terminal 277 residues are clearly soluble/cytoplasmic (high charged-residue density, no long hydrophobic stretches), eliminating C which places TMs in that region. (2) The C-terminal ~55 residues contain two distinct hydrophobic stretches separated by a more polar loop (containing P, N, D, H), indicating two TMs rather than one, eliminating D. (3) For the second TM boundary, the well-established aromatic-residue-at-membrane-interface principle (Trp/Tyr enrichment at helix termini, observed across many membrane proteins) favors boundaries at W308 and W322-W323 (choice B: 308..323) over C311 and F325 (choice A: 311..325). Trp is the most prevalent residue at the lipid-water interface in TM helices, making W-L-A...W-W a classic helix signature, while starting at Cys and ending at Phe is less characteristic.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can apply: (a) hydrophobicity/topology reasoning to eliminate C and D, (b) the aromatic-interface rule (Trp at TM boundaries, a pattern learned from hundreds of membrane protein structures) to prefer 308..323 over 311..325, and (c) the presence of two hydrophobic stretches to reject the single-TM option. The distinction between B and A rests on the Trp residues at positions 308 and 322-323, which is a transferable biophysical principle rather than a protein-specific annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> While B and A differ by only 3 residues at the start and 2 at the end of the second TM, the aromatic-residue interface principle provides a clear basis for preferring B (W at both boundaries) over A (C at start, F at end). Choice C is clearly wrong (N-terminal cytoplasmic region), and D is incomplete. No genuine ambiguity remains among the offered choices.


### Important caveats

- The first TM at 278..286 is only 9 residues, unusually short for a standard alpha-helical TM (typically 18-25 residues). This likely reflects a tilted helix or partial helix in the cryo-EM structure of the ZntB/CmaX fold. Since all relevant choices (A, B, D) include this segment, the model need not independently validate its length.
- The boundary distinction between B and A (±3 residues) is at the edge of what sequence-based reasoning can resolve with certainty; the aromatic-interface argument provides a strong but not absolute basis.
- The annotation derives from a 3.03 Å cryo-EM structure (PDB 7NH9), which is experimental but has limited resolution for defining exact helix termini.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Multiple layers of transferable reasoning distinguish B from the alternatives: (1) The N-terminal 277 residues are clearly soluble/cytoplasmic (high charged-residue density, no long hydrophobic stretches), eliminating C which places TMs in that region. (2) The C-terminal ~55 residues contain two distinct hydrophobic stretches separated by a more polar loop (containing P, N, D, H), indicating two TMs rather than one, eliminating D. (3) For the second TM boundary, the well-established aromatic-residue-at-membrane-interface principle (Trp/Tyr enrichment at helix termini, observed across many membrane proteins) favors boundaries at W308 and W322-W323 (choice B: 308..323) over C311 and F325 (choice A: 311..325). Trp is the most prevalent residue at the lipid-water interface in TM helices, making W-L-A...W-W a classic helix signature, while starting at Cys and ending at Phe is less characteristic.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can apply: (a) hydrophobicity/topology reasoning to eliminate C and D, (b) the aromatic-interface rule (Trp at TM boundaries, a pattern learned from hundreds of membrane protein structures) to prefer 308..323 over 311..325, and (c) the presence of two hydrophobic stretches to reject the single-TM option. The distinction between B and A rests on the Trp residues at positions 308 and 322-323, which is a transferable biophysical principle rather than a protein-specific annotation."
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
      "H7"
    ],
    "judgment": "supported",
    "reason": "The UniProt annotation for Q9ZIH2 (CmaX/ZntB from P. aeruginosa) records exactly two transmembrane helices: 278..286 and 308..323, both supported by cryo-EM structure PDB 7NH9 (3.03 Å) and experimental topology data (PubMed 34175341). The topological domains confirm cytoplasmic 1-277, periplasmic loop 287-307, and cytoplasmic 324-332, consistent with exactly two membrane-spanning helices at the annotated positions. Choice B matches these boundaries exactly."
  },
  "important_caveats": [
    "The first TM at 278..286 is only 9 residues, unusually short for a standard alpha-helical TM (typically 18-25 residues). This likely reflects a tilted helix or partial helix in the cryo-EM structure of the ZntB/CmaX fold. Since all relevant choices (A, B, D) include this segment, the model need not independently validate its length.",
    "The boundary distinction between B and A (±3 residues) is at the edge of what sequence-based reasoning can resolve with certainty; the aromatic-interface argument provides a strong but not absolute basis.",
    "The annotation derives from a 3.03 Å cryo-EM structure (PDB 7NH9), which is experimental but has limited resolution for defining exact helix termini."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While B and A differ by only 3 residues at the start and 2 at the end of the second TM, the aromatic-residue interface principle provides a clear basis for preferring B (W at both boundaries) over A (C at start, F at end). Choice C is clearly wrong (N-terminal cytoplasmic region), and D is incomplete. No genuine ambiguity remains among the offered choices."
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
    "reason": "The UniProt annotation for Q9ZIH2 (CmaX/ZntB from P. aeruginosa) records exactly two transmembrane helices: 278..286 and 308..323, both supported by cryo-EM structure PDB 7NH9 (3.03 Å) and experimental topology data (PubMed 34175341). The topological domains confirm cytoplasmic 1-277, periplasmic loop 287-307, and cytoplasmic 324-332, consistent with exactly two membrane-spanning helices at the annotated positions. Choice B matches these boundaries exactly.",
    "evidence_ids": ["C6", "C8", "C5", "C7", "C9", "H5", "H7"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Multiple layers of transferable reasoning distinguish B from the alternatives: (1) The N-terminal 277 residues are clearly soluble/cytoplasmic (high charged-residue density, no long hydrophobic stretches), eliminating C which places TMs in that region. (2) The C-terminal ~55 residues contain two distinct hydrophobic stretches separated by a more polar loop (containing P, N, D, H), indicating two TMs rather than one, eliminating D. (3) For the second TM boundary, the well-established aromatic-residue-at-membrane-interface principle (Trp/Tyr enrichment at helix termini, observed across many membrane proteins) favors boundaries at W308 and W322-W323 (choice B: 308..323) over C311 and F325 (choice A: 311..325). Trp is the most prevalent residue at the lipid-water interface in TM helices, making W-L-A...W-W a classic helix signature, while starting at Cys and ending at Phe is less characteristic.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can apply: (a) hydrophobicity/topology reasoning to eliminate C and D, (b) the aromatic-interface rule (Trp at TM boundaries, a pattern learned from hundreds of membrane protein structures) to prefer 308..323 over 311..325, and (c) the presence of two hydrophobic stretches to reject the single-TM option. The distinction between B and A rests on the Trp residues at positions 308 and 322-323, which is a transferable biophysical principle rather than a protein-specific annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While B and A differ by only 3 residues at the start and 2 at the end of the second TM, the aromatic-residue interface principle provides a clear basis for preferring B (W at both boundaries) over A (C at start, F at end). Choice C is clearly wrong (N-terminal cytoplasmic region), and D is incomplete. No genuine ambiguity remains among the offered choices."
  },
  "important_caveats": [
    "The first TM at 278..286 is only 9 residues, unusually short for a standard alpha-helical TM (typically 18-25 residues). This likely reflects a tilted helix or partial helix in the cryo-EM structure of the ZntB/CmaX fold. Since all relevant choices (A, B, D) include this segment, the model need not independently validate its length.",
    "The boundary distinction between B and A (±3 residues) is at the edge of what sequence-based reasoning can resolve with certainty; the aromatic-interface argument provides a strong but not absolute basis.",
    "The annotation derives from a 3.03 Å cryo-EM structure (PDB 7NH9), which is experimental but has limited resolution for defining exact helix termini."
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
  "requested_accession": "Q9ZIH2",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "benchmark_sequence_sha256": "988a45b94bdf9854fe2938f5dca65ebc73a07414f1d018dcbbc91c52ce85ad8a",
  "benchmark_sequence_length": 332,
  "current_status": "retrieved",
  "current_sequence_comparison": "matched",
  "current_entry_audit": {
    "entryVersion": 155,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "1999-05-01",
    "sequenceVersion": 1
  },
  "current_uniprot_release": "2026_03",
  "current_record_sha256": "a00f4c0271bbd4fae7afeb16e71be27aaff79dadde11086a04686cc2d5355d0e",
  "current_source_sequence_sha256": "988a45b94bdf9854fe2938f5dca65ebc73a07414f1d018dcbbc91c52ce85ad8a",
  "current_source_sequence_length": 332,
  "historical_status": "retrieved",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "selected_historical_entry_version": 153,
  "selected_historical_version": {
    "accession": "Q9ZIH2",
    "database": "Swiss-Prot",
    "entryVersion": 153,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "CMAX_PSEAE",
    "sequenceVersion": 1
  },
  "selected_historical_record_sha256": "ef1f3b913665475f320bd32d9a7e46b733d69ecc2d4104881ec5fd04fc3481b9",
  "selected_historical_source_sequence_sha256": "988a45b94bdf9854fe2938f5dca65ebc73a07414f1d018dcbbc91c52ce85ad8a",
  "selected_historical_source_sequence_length": 332,
  "latest_at_cutoff_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 153,
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9ZIH2.json)

```json
{
  "evidence_id": "C1",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q9ZIH2.json",
  "source_sha256": "a00f4c0271bbd4fae7afeb16e71be27aaff79dadde11086a04686cc2d5355d0e",
  "retrieved_utc": "2026-11-02T04:33:54.880542+00:00",
  "json_pointer": "/primaryAccession",
  "excerpt": "\"Q9ZIH2\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9ZIH2.json)

```json
{
  "evidence_id": "C2",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q9ZIH2.json",
  "source_sha256": "a00f4c0271bbd4fae7afeb16e71be27aaff79dadde11086a04686cc2d5355d0e",
  "retrieved_utc": "2026-11-02T04:33:54.880542+00:00",
  "json_pointer": "/entryAudit",
  "excerpt": "{\"entryVersion\":155,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"1999-05-01\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9ZIH2.json)

```json
{
  "evidence_id": "C3",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q9ZIH2.json",
  "source_sha256": "a00f4c0271bbd4fae7afeb16e71be27aaff79dadde11086a04686cc2d5355d0e",
  "retrieved_utc": "2026-11-02T04:33:54.880542+00:00",
  "json_pointer": "/organism",
  "excerpt": "{\"lineage\":[\"Bacteria\",\"Pseudomonadati\",\"Pseudomonadota\",\"Gammaproteobacteria\",\"Pseudomonadales\",\"Pseudomonadaceae\",\"Pseudomonas\"],\"scientificName\":\"Pseudomonas aeruginosa (strain ATCC 15692 / DSM 22644 / CIP 104116 / JCM 14847 / LMG 12228 / 1C / PRS 101 / PAO1)\",\"taxonId\":208964}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9ZIH2.json)

```json
{
  "evidence_id": "C4",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q9ZIH2.json",
  "source_sha256": "a00f4c0271bbd4fae7afeb16e71be27aaff79dadde11086a04686cc2d5355d0e",
  "retrieved_utc": "2026-11-02T04:33:54.880542+00:00",
  "json_pointer": "/proteinDescription",
  "excerpt": "{\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Divalent cation transporter CmaX\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9ZIH2.json)

```json
{
  "evidence_id": "C5",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q9ZIH2.json",
  "source_sha256": "a00f4c0271bbd4fae7afeb16e71be27aaff79dadde11086a04686cc2d5355d0e",
  "retrieved_utc": "2026-11-02T04:33:54.880542+00:00",
  "json_pointer": "/features/1",
  "excerpt": "{\"description\":\"Cytoplasmic\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"34175341\",\"source\":\"PubMed\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":277},\"start\":{\"modifier\":\"EXACT\",\"value\":1}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9ZIH2.json)

```json
{
  "evidence_id": "C6",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q9ZIH2.json",
  "source_sha256": "a00f4c0271bbd4fae7afeb16e71be27aaff79dadde11086a04686cc2d5355d0e",
  "retrieved_utc": "2026-11-02T04:33:54.880542+00:00",
  "json_pointer": "/features/2",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"34175341\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"7NH9\",\"source\":\"PDB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":286},\"start\":{\"modifier\":\"EXACT\",\"value\":278}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9ZIH2.json)

```json
{
  "evidence_id": "C7",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q9ZIH2.json",
  "source_sha256": "a00f4c0271bbd4fae7afeb16e71be27aaff79dadde11086a04686cc2d5355d0e",
  "retrieved_utc": "2026-11-02T04:33:54.880542+00:00",
  "json_pointer": "/features/3",
  "excerpt": "{\"description\":\"Periplasmic\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"34175341\",\"source\":\"PubMed\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":307},\"start\":{\"modifier\":\"EXACT\",\"value\":287}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9ZIH2.json)

```json
{
  "evidence_id": "C8",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q9ZIH2.json",
  "source_sha256": "a00f4c0271bbd4fae7afeb16e71be27aaff79dadde11086a04686cc2d5355d0e",
  "retrieved_utc": "2026-11-02T04:33:54.880542+00:00",
  "json_pointer": "/features/4",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"34175341\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"7NH9\",\"source\":\"PDB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":323},\"start\":{\"modifier\":\"EXACT\",\"value\":308}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9ZIH2.json)

```json
{
  "evidence_id": "C9",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q9ZIH2.json",
  "source_sha256": "a00f4c0271bbd4fae7afeb16e71be27aaff79dadde11086a04686cc2d5355d0e",
  "retrieved_utc": "2026-11-02T04:33:54.880542+00:00",
  "json_pointer": "/features/5",
  "excerpt": "{\"description\":\"Cytoplasmic\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"34175341\",\"source\":\"PubMed\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":332},\"start\":{\"modifier\":\"EXACT\",\"value\":324}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9ZIH2.json)

```json
{
  "evidence_id": "C10",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q9ZIH2.json",
  "source_sha256": "a00f4c0271bbd4fae7afeb16e71be27aaff79dadde11086a04686cc2d5355d0e",
  "retrieved_utc": "2026-11-02T04:33:54.880542+00:00",
  "json_pointer": "/references/2",
  "excerpt": "{\"citation\":{\"authors\":[\"Stetsenko A.\",\"Stehantsev P.\",\"Dranenko N.O.\",\"Gelfand M.S.\",\"Guskov A.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"34175341\"},{\"database\":\"DOI\",\"id\":\"10.1016/j.ijbiomac.2021.06.130\"}],\"citationType\":\"journal article\",\"firstPage\":\"760\",\"id\":\"34175341\",\"journal\":\"Int. J. Biol. Macromol.\",\"lastPage\":\"767\",\"publicationDate\":\"2021\",\"title\":\"Structural and biochemical characterization of a novel ZntB (CmaX) transporter protein from Pseudomonas aeruginosa.\",\"volume\":\"184\"},\"evidences\":[{\"evidenceCode\":\"ECO:0007744\",\"id\":\"7NH9\",\"source\":\"PDB\"}],\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"ATCC 15692 / DSM 22644 / CIP 104116 / JCM 14847 / LMG 12228 / 1C / PRS 101 / PAO1\"}],\"referenceNumber\":3,\"referencePositions\":[\"STRUCTURE BY ELECTRON MICROSCOPY (3.03 ANGSTROMS)\",\"FUNCTION\",\"TRANSPORTER ACTIVITY\",\"SUBUNIT\",\"SUBCELLULAR LOCATION\",\"TOPOLOGY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9ZIH2?format=txt&versions=153)

```json
{
  "evidence_id": "H1",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q9ZIH2?format=txt&versions=153",
  "source_sha256": "ef1f3b913665475f320bd32d9a7e46b733d69ecc2d4104881ec5fd04fc3481b9",
  "retrieved_utc": "2026-11-02T04:33:58.139616+00:00",
  "source_locator": "lines 1-14",
  "excerpt": "ID   CMAX_PSEAE              Reviewed;         332 AA.\nAC   Q9ZIH2; A0A1S1C048; G3XD00; Q7DCE5;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   01-MAY-1999, sequence version 1.\nDT   28-JAN-2026, entry version 153.\nDE   RecName: Full=Divalent cation transporter CmaX {ECO:0000305};\nGN   Name=cmaX {ECO:0000303|PubMed:10438740, ECO:0000303|PubMed:34175341};\nGN   Synonyms=zntB {ECO:0000303|PubMed:34175341};\nGN   OrderedLocusNames=PA1773 {ECO:0000312|EMBL:AAG05162.1};\nOS   Pseudomonas aeruginosa (strain ATCC 15692 / DSM 22644 / CIP 104116 / JCM\nOS   14847 / LMG 12228 / 1C / PRS 101 / PAO1).\nOC   Bacteria; Pseudomonadati; Pseudomonadota; Gammaproteobacteria;\nOC   Pseudomonadales; Pseudomonadaceae; Pseudomonas.\nOX   NCBI_TaxID=208964;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 153,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9ZIH2?format=txt&versions=153)

```json
{
  "evidence_id": "H2",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q9ZIH2?format=txt&versions=153",
  "source_sha256": "ef1f3b913665475f320bd32d9a7e46b733d69ecc2d4104881ec5fd04fc3481b9",
  "retrieved_utc": "2026-11-02T04:33:58.139616+00:00",
  "source_locator": "lines 15-24",
  "excerpt": "RN   [1] {ECO:0000312|EMBL:AAD11565.1}\nRP   NUCLEOTIDE SEQUENCE [GENOMIC DNA].\nRC   STRAIN=ATCC 15692 / DSM 22644 / CIP 104116 / JCM 14847 / LMG 12228 / 1C /\nRC   PRS 101 / PAO1;\nRX   PubMed=10438740; DOI=10.1128/jb.181.16.4746-4754.1999;\nRA   Brinkman F.S., Schoofs G., Hancock R.E., De Mot R.;\nRT   \"Influence of a putative ECF sigma factor on expression of the major outer\nRT   membrane protein, OprF, in Pseudomonas aeruginosa and Pseudomonas\nRT   fluorescens.\";\nRL   J. Bacteriol. 181:4746-4754(1999).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 153,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9ZIH2?format=txt&versions=153)

```json
{
  "evidence_id": "H3",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q9ZIH2?format=txt&versions=153",
  "source_sha256": "ef1f3b913665475f320bd32d9a7e46b733d69ecc2d4104881ec5fd04fc3481b9",
  "retrieved_utc": "2026-11-02T04:33:58.139616+00:00",
  "source_locator": "lines 39-48",
  "excerpt": "RN   [3] {ECO:0007744|PDB:7NH9}\nRP   STRUCTURE BY ELECTRON MICROSCOPY (3.03 ANGSTROMS), FUNCTION, TRANSPORTER\nRP   ACTIVITY, SUBUNIT, SUBCELLULAR LOCATION, AND TOPOLOGY.\nRC   STRAIN=ATCC 15692 / DSM 22644 / CIP 104116 / JCM 14847 / LMG 12228 / 1C /\nRC   PRS 101 / PAO1;\nRX   PubMed=34175341; DOI=10.1016/j.ijbiomac.2021.06.130;\nRA   Stetsenko A., Stehantsev P., Dranenko N.O., Gelfand M.S., Guskov A.;\nRT   \"Structural and biochemical characterization of a novel ZntB (CmaX)\nRT   transporter protein from Pseudomonas aeruginosa.\";\nRL   Int. J. Biol. Macromol. 184:760-767(2021).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 153,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9ZIH2?format=txt&versions=153)

```json
{
  "evidence_id": "H4",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q9ZIH2?format=txt&versions=153",
  "source_sha256": "ef1f3b913665475f320bd32d9a7e46b733d69ecc2d4104881ec5fd04fc3481b9",
  "retrieved_utc": "2026-11-02T04:33:58.139616+00:00",
  "source_locator": "lines 122-124",
  "excerpt": "FT   TOPO_DOM        1..277\nFT                   /note=\"Cytoplasmic\"\nFT                   /evidence=\"ECO:0000269|PubMed:34175341\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 153,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9ZIH2?format=txt&versions=153)

```json
{
  "evidence_id": "H5",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q9ZIH2?format=txt&versions=153",
  "source_sha256": "ef1f3b913665475f320bd32d9a7e46b733d69ecc2d4104881ec5fd04fc3481b9",
  "retrieved_utc": "2026-11-02T04:33:58.139616+00:00",
  "source_locator": "lines 125-128",
  "excerpt": "FT   TRANSMEM        278..286\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000269|PubMed:34175341,\nFT                   ECO:0007744|PDB:7NH9\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 153,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9ZIH2?format=txt&versions=153)

```json
{
  "evidence_id": "H6",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q9ZIH2?format=txt&versions=153",
  "source_sha256": "ef1f3b913665475f320bd32d9a7e46b733d69ecc2d4104881ec5fd04fc3481b9",
  "retrieved_utc": "2026-11-02T04:33:58.139616+00:00",
  "source_locator": "lines 129-131",
  "excerpt": "FT   TOPO_DOM        287..307\nFT                   /note=\"Periplasmic\"\nFT                   /evidence=\"ECO:0000269|PubMed:34175341\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 153,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9ZIH2?format=txt&versions=153)

```json
{
  "evidence_id": "H7",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q9ZIH2?format=txt&versions=153",
  "source_sha256": "ef1f3b913665475f320bd32d9a7e46b733d69ecc2d4104881ec5fd04fc3481b9",
  "retrieved_utc": "2026-11-02T04:33:58.139616+00:00",
  "source_locator": "lines 132-135",
  "excerpt": "FT   TRANSMEM        308..323\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000269|PubMed:34175341,\nFT                   ECO:0007744|PDB:7NH9\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 153,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9ZIH2?format=txt&versions=153)

```json
{
  "evidence_id": "H8",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q9ZIH2?format=txt&versions=153",
  "source_sha256": "ef1f3b913665475f320bd32d9a7e46b733d69ecc2d4104881ec5fd04fc3481b9",
  "retrieved_utc": "2026-11-02T04:33:58.139616+00:00",
  "source_locator": "lines 136-138",
  "excerpt": "FT   TOPO_DOM        324..332\nFT                   /note=\"Cytoplasmic\"\nFT                   /evidence=\"ECO:0000269|PubMed:34175341\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 153,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json), zero-based source row 128. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
