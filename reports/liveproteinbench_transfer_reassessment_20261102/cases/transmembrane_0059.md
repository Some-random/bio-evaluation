# transmembrane_0059: before and after transfer clarification

[All 1,328 cases](../README.md) · [Method](../METHOD.md) · [Summary](../SUMMARY.md) · [Exact reviewer user message](../inputs/transmembrane_0059.txt)

**Task:** `transmembrane`  
**Author key, unchanged:** **B** — 17..37; 48..68; 94..114; 129..149; 176..196; 295..315; 322..342

| Round | Reviewer | Key support | Transfer / lookup | Output usability (canonical status) |
|---|---|---|---|---|
| before | GPT-6 Luna | supported | reasoning-supported | usable output (valid_review) |
| before | Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | usable output (valid_review) |
| after | GPT-6 Luna | supported | lookup-dependent | usable output (valid_review) |
| after | Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | usable output (valid_review) |

**Usable output means format-valid review, not reasoning-supported or biologically correct.** A usable output can classify the question as reasoning-supported, lookup-dependent or uncertain. An output error is a problem with the saved model response; it does not count a defective benchmark question or wrong key. Each saved review is retained in full below. Labels from output errors are displayed as saved and excluded from label statistics. The author key and reviewer evidence were visible to reviewers; this is a review of answerability and key support, not a benchmark-solving score.

## Complete original question

```text
[Protein Sequence]
MQPFGDAWSQRHLAGVVLAGSVLSIVGSLYMILGFFFLRECRSFRHKLILGLAVSDLLLALNFFIPSLSMVTGREISSPWNEGFCSANGFLMQLFFAQIDVWQISIALITLLMLSGPSMVLKWIRENVWAVWLFPWLVSLIAAFFAFGFWDYANVGGFCWLGSRNIRLYFNYIPRWIIILVCLVIYIAVYRLILHARRRANIQKTYRGRASDRAPPQPVTTTAPATNPESEKVNPDEISSGNGSSSLDTSRSGSSTGFTQTVHDPAVAGQIQTAAERAQEEAEQQKQVRKIAIQMISYPLAYAVLWAIPTIVMIIQVARGGEGVSIHVEGLAKMLLVFNGFVDAHVYGFNERTAMGWRQRIRPAAQEDDEEAAGTSGGVHEVVSRPEPTLKNPNVWQQNMV

[Multiple Choices]
A. 17..37; 48..68; 94..114; 134..154; 176..196; 295..315; 322..342
B. 17..37; 48..68; 94..114; 129..149; 176..196; 295..315; 322..342
C. 28..48; 59..79; 106..126
D. 48..68; 94..114; 129..149; 176..196; 295..315; 322..342
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

> The sequence exactly matches the UniProt record, whose historical and current annotations include all seven transmembrane spans listed in B, including 129..149. These are computational annotations (ECO:0000255), not evidence of direct experimental measurement.

Citations as saved: [H4](#evidence-h4), [H6](#evidence-h6), [H8](#evidence-h8), [H10](#evidence-h10), [H12](#evidence-h12), [H14](#evidence-h14), [H16](#evidence-h16).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains successive strongly hydrophobic stretches separated by more polar or charged regions, consistent with a multi-pass membrane protein. The candidate set’s seven-span pattern fits this sequence; around the disputed span, 129..149 better captures the hydrophobic segment than the shifted 134..154 option, which extends into more polar residues.


**Missing item-specific fact**

> The exact curated transmembrane coordinates are not given, but sequence hydropathy and the pattern of separated hydrophobic segments provide meaningful grounds to distinguish the choices. The database annotation is useful confirmation, not information supplied to the model.


**Reason**

> This is a sequence-based prediction task with a recognizable multi-pass hydrophobic pattern. The evidence supports an inference from the input rather than requiring recognition of the exact protein or recall of its database entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The alternatives omit or shift spans in ways that fit the sequence less well; no competing option is comparably supported by the supplied sequence.


### Important caveats

- The supporting database transmembrane features are computationally annotated, not established here as experimental measurements.
- The historical record sequence matches the supplied sequence, but the author’s exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains successive strongly hydrophobic stretches separated by more polar or charged regions, consistent with a multi-pass membrane protein. The candidate set’s seven-span pattern fits this sequence; around the disputed span, 129..149 better captures the hydrophobic segment than the shifted 134..154 option, which extends into more polar residues.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The exact curated transmembrane coordinates are not given, but sequence hydropathy and the pattern of separated hydrophobic segments provide meaningful grounds to distinguish the choices. The database annotation is useful confirmation, not information supplied to the model.",
    "reason": "This is a sequence-based prediction task with a recognizable multi-pass hydrophobic pattern. The evidence supports an inference from the input rather than requiring recognition of the exact protein or recall of its database entry."
  },
  "case_id": "transmembrane_0059",
  "expected_answer_check": {
    "evidence_ids": [
      "H4",
      "H6",
      "H8",
      "H10",
      "H12",
      "H14",
      "H16"
    ],
    "judgment": "supported",
    "reason": "The sequence exactly matches the UniProt record, whose historical and current annotations include all seven transmembrane spans listed in B, including 129..149. These are computational annotations (ECO:0000255), not evidence of direct experimental measurement."
  },
  "important_caveats": [
    "The supporting database transmembrane features are computationally annotated, not established here as experimental measurements.",
    "The historical record sequence matches the supplied sequence, but the author’s exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The alternatives omit or shift spans in ways that fit the sequence less well; no competing option is comparably supported by the supplied sequence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0059",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence exactly matches the UniProt record, whose historical and current annotations include all seven transmembrane spans listed in B, including 129..149. These are computational annotations (ECO:0000255), not evidence of direct experimental measurement.",
    "evidence_ids": ["H4", "H6", "H8", "H10", "H12", "H14", "H16"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains successive strongly hydrophobic stretches separated by more polar or charged regions, consistent with a multi-pass membrane protein. The candidate set’s seven-span pattern fits this sequence; around the disputed span, 129..149 better captures the hydrophobic segment than the shifted 134..154 option, which extends into more polar residues.",
    "missing_item_specific_fact": "The exact curated transmembrane coordinates are not given, but sequence hydropathy and the pattern of separated hydrophobic segments provide meaningful grounds to distinguish the choices. The database annotation is useful confirmation, not information supplied to the model.",
    "reason": "This is a sequence-based prediction task with a recognizable multi-pass hydrophobic pattern. The evidence supports an inference from the input rather than requiring recognition of the exact protein or recall of its database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The alternatives omit or shift spans in ways that fit the sequence less well; no competing option is comparably supported by the supplied sequence."
  },
  "important_caveats": [
    "The supporting database transmembrane features are computationally annotated, not established here as experimental measurements.",
    "The historical record sequence matches the supplied sequence, but the author’s exact source snapshot is unknown."
  ]
}
```

</details>

## Before: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry G1XJN1 (Ascaroside receptor GPR3, Arthrobotrys oligospora) annotates exactly seven transmembrane helices at 17-37, 48-68, 94-114, 129-149, 176-196, 295-315, and 322-342, matching option B precisely. Both the current entry (v48) and the historical entry (v46) confirm these coordinates. The sequence in the question matches the UniProt sequence (SHA-256 identical, 401 AA). However, all TM annotations carry evidence code ECO:0000255 (inferred by similarity), meaning these are computational predictions from homology to known GPCR architectures, not experimentally determined boundaries.

Citations as saved: [C6](#evidence-c6), [C8](#evidence-c8), [C10](#evidence-c10), [C12](#evidence-c12), [C14](#evidence-c14), [C16](#evidence-c16), [C18](#evidence-c18), [H4](#evidence-h4), [H6](#evidence-h6), [H8](#evidence-h8), [H10](#evidence-h10), [H12](#evidence-h12), [H14](#evidence-h14), [H16](#evidence-h16).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> General GPCR knowledge eliminates C (only 3 TM segments) and D (6 segments, missing TM1) since a canonical GPCR requires 7 TM helices. For the A-vs-B distinction (TM4 at 129-149 vs 134-154), a partial hydrophobicity argument exists: residues 129-133 (W-A-V-W-L) are hydrophobic and favor B's earlier start, while residues 150-154 include D and N (hydrophilic) that favor B's earlier end. However, this is a 5-residue shift within a 21-residue helix, well within the boundary uncertainty of any hydrophobicity-based predictor.


**Missing item-specific fact**

> The exact TM4 boundary (129-149 vs 134-154) is a specific output of the UniProt similarity-based prediction (ECO:0000255), not an experimentally determined value. Distinguishing A from B with confidence requires knowing the particular annotation or prediction-tool output rather than applying general biological principles, since both boundaries fall within the plausible hydrophobic stretch.


**Reason**

> While GPCR topology reasoning (7 TM segments) eliminates C and D, the critical A-vs-B discrimination hinges on a 5-residue boundary shift in TM4. The residues at the contested positions (WAVWL at 129-133; WDYAN at 150-154) provide weak hydrophobicity hints favoring B, but TM helix boundaries in GPCRs are inherently fuzzy and commonly include aromatic and even polar residues at their edges. The 'correct' boundaries are themselves computational predictions (ECO:0000255), so the question effectively asks the model to reproduce a specific annotation output rather than derive a biologically certain answer.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "B"
]
```

> Options A and B differ only in TM4 (134-154 vs 129-149). Both are plausible 21-residue hydrophobic segments. The 5-residue shift falls within the typical boundary uncertainty of TM prediction tools. Without the specific database annotation, a competent hydrophobicity analysis could reasonably assign TM4 to either range, making A a defensible alternative.


### Important caveats

- All seven TM annotations carry evidence code ECO:0000255 (similarity inference), meaning even the 'correct' boundaries are computational predictions, not experimental measurements.
- The UniProt entry was first public in April 2025; the author's source snapshot is unknown, though the sequence and annotations are stable (sequence version 1 unchanged since 2011).
- The reviewer-only evidence confirms the annotation but was not available to the evaluated model; the model must reason from sequence alone.
- Option C (3 segments) and D (6 segments) are clearly wrong for a GPCR, making the effective discrimination a binary A-vs-B choice on a single boundary.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "General GPCR knowledge eliminates C (only 3 TM segments) and D (6 segments, missing TM1) since a canonical GPCR requires 7 TM helices. For the A-vs-B distinction (TM4 at 129-149 vs 134-154), a partial hydrophobicity argument exists: residues 129-133 (W-A-V-W-L) are hydrophobic and favor B's earlier start, while residues 150-154 include D and N (hydrophilic) that favor B's earlier end. However, this is a 5-residue shift within a 21-residue helix, well within the boundary uncertainty of any hydrophobicity-based predictor.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The exact TM4 boundary (129-149 vs 134-154) is a specific output of the UniProt similarity-based prediction (ECO:0000255), not an experimentally determined value. Distinguishing A from B with confidence requires knowing the particular annotation or prediction-tool output rather than applying general biological principles, since both boundaries fall within the plausible hydrophobic stretch.",
    "reason": "While GPCR topology reasoning (7 TM segments) eliminates C and D, the critical A-vs-B discrimination hinges on a 5-residue boundary shift in TM4. The residues at the contested positions (WAVWL at 129-133; WDYAN at 150-154) provide weak hydrophobicity hints favoring B, but TM helix boundaries in GPCRs are inherently fuzzy and commonly include aromatic and even polar residues at their edges. The 'correct' boundaries are themselves computational predictions (ECO:0000255), so the question effectively asks the model to reproduce a specific annotation output rather than derive a biologically certain answer."
  },
  "case_id": "transmembrane_0059",
  "expected_answer_check": {
    "evidence_ids": [
      "C6",
      "C8",
      "C10",
      "C12",
      "C14",
      "C16",
      "C18",
      "H4",
      "H6",
      "H8",
      "H10",
      "H12",
      "H14",
      "H16"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry G1XJN1 (Ascaroside receptor GPR3, Arthrobotrys oligospora) annotates exactly seven transmembrane helices at 17-37, 48-68, 94-114, 129-149, 176-196, 295-315, and 322-342, matching option B precisely. Both the current entry (v48) and the historical entry (v46) confirm these coordinates. The sequence in the question matches the UniProt sequence (SHA-256 identical, 401 AA). However, all TM annotations carry evidence code ECO:0000255 (inferred by similarity), meaning these are computational predictions from homology to known GPCR architectures, not experimentally determined boundaries."
  },
  "important_caveats": [
    "All seven TM annotations carry evidence code ECO:0000255 (similarity inference), meaning even the 'correct' boundaries are computational predictions, not experimental measurements.",
    "The UniProt entry was first public in April 2025; the author's source snapshot is unknown, though the sequence and annotations are stable (sequence version 1 unchanged since 2011).",
    "The reviewer-only evidence confirms the annotation but was not available to the evaluated model; the model must reason from sequence alone.",
    "Option C (3 segments) and D (6 segments) are clearly wrong for a GPCR, making the effective discrimination a binary A-vs-B choice on a single boundary."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "B"
    ],
    "reason": "Options A and B differ only in TM4 (134-154 vs 129-149). Both are plausible 21-residue hydrophobic segments. The 5-residue shift falls within the typical boundary uncertainty of TM prediction tools. Without the specific database annotation, a competent hydrophobicity analysis could reasonably assign TM4 to either range, making A a defensible alternative."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0059",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry G1XJN1 (Ascaroside receptor GPR3, Arthrobotrys oligospora) annotates exactly seven transmembrane helices at 17-37, 48-68, 94-114, 129-149, 176-196, 295-315, and 322-342, matching option B precisely. Both the current entry (v48) and the historical entry (v46) confirm these coordinates. The sequence in the question matches the UniProt sequence (SHA-256 identical, 401 AA). However, all TM annotations carry evidence code ECO:0000255 (inferred by similarity), meaning these are computational predictions from homology to known GPCR architectures, not experimentally determined boundaries.",
    "evidence_ids": ["C6", "C8", "C10", "C12", "C14", "C16", "C18", "H4", "H6", "H8", "H10", "H12", "H14", "H16"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "General GPCR knowledge eliminates C (only 3 TM segments) and D (6 segments, missing TM1) since a canonical GPCR requires 7 TM helices. For the A-vs-B distinction (TM4 at 129-149 vs 134-154), a partial hydrophobicity argument exists: residues 129-133 (W-A-V-W-L) are hydrophobic and favor B's earlier start, while residues 150-154 include D and N (hydrophilic) that favor B's earlier end. However, this is a 5-residue shift within a 21-residue helix, well within the boundary uncertainty of any hydrophobicity-based predictor.",
    "missing_item_specific_fact": "The exact TM4 boundary (129-149 vs 134-154) is a specific output of the UniProt similarity-based prediction (ECO:0000255), not an experimentally determined value. Distinguishing A from B with confidence requires knowing the particular annotation or prediction-tool output rather than applying general biological principles, since both boundaries fall within the plausible hydrophobic stretch.",
    "reason": "While GPCR topology reasoning (7 TM segments) eliminates C and D, the critical A-vs-B discrimination hinges on a 5-residue boundary shift in TM4. The residues at the contested positions (WAVWL at 129-133; WDYAN at 150-154) provide weak hydrophobicity hints favoring B, but TM helix boundaries in GPCRs are inherently fuzzy and commonly include aromatic and even polar residues at their edges. The 'correct' boundaries are themselves computational predictions (ECO:0000255), so the question effectively asks the model to reproduce a specific annotation output rather than derive a biologically certain answer."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "B"],
    "reason": "Options A and B differ only in TM4 (134-154 vs 129-149). Both are plausible 21-residue hydrophobic segments. The 5-residue shift falls within the typical boundary uncertainty of TM prediction tools. Without the specific database annotation, a competent hydrophobicity analysis could reasonably assign TM4 to either range, making A a defensible alternative."
  },
  "important_caveats": [
    "All seven TM annotations carry evidence code ECO:0000255 (similarity inference), meaning even the 'correct' boundaries are computational predictions, not experimental measurements.",
    "The UniProt entry was first public in April 2025; the author's source snapshot is unknown, though the sequence and annotations are stable (sequence version 1 unchanged since 2011).",
    "The reviewer-only evidence confirms the annotation but was not available to the evaluated model; the model must reason from sequence alone.",
    "Option C (3 segments) and D (6 segments) are clearly wrong for a GPCR, making the effective discrimination a binary A-vs-B choice on a single boundary."
  ]
}
```

</details>

## After: GPT-6 Luna

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence-matched historical UniProt record annotates seven helical transmembrane regions at the coordinates listed in B. These annotations carry computational evidence code ECO:0000255, so they support the key as database annotations but are not, by themselves, experimental confirmation.

Citations as saved: [H4](#evidence-h4), [H6](#evidence-h6), [H8](#evidence-h8), [H10](#evidence-h10), [H12](#evidence-h12), [H14](#evidence-h14), [H16](#evidence-h16).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence has repeated hydrophobic stretches consistent with a seven-transmembrane receptor, which meaningfully favors the seven-span choices over C and helps reject D, which omits an apparent span. But this transferable pattern does not reliably distinguish B from A: they differ only in the proposed boundaries of one helix, and both intervals cover a plausible membrane-spanning stretch.


**Missing item-specific fact**

> The exact boundary annotation for the relevant helix—129..149 rather than 134..154—is not established by the sequence pattern alone.


**Reason**

> Family-level and hydropathy reasoning support the overall seven-helix topology, but the offered choices also test a fine boundary difference for which no clear sequence-based discriminator is available.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "B"
]
```

> Both choices describe seven spans, and their only difference is a five-residue shift in one predicted helix interval. Without a stated boundary convention or tolerance, both intervals could reasonably describe the same membrane-spanning helix.


### Important caveats

- The reviewer-only source evidence is sequence-matched, but the author's exact source snapshot is unknown.
- The source annotation is computational; the evidence supplied does not establish experimental validation of the precise boundaries.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has repeated hydrophobic stretches consistent with a seven-transmembrane receptor, which meaningfully favors the seven-span choices over C and helps reject D, which omits an apparent span. But this transferable pattern does not reliably distinguish B from A: they differ only in the proposed boundaries of one helix, and both intervals cover a plausible membrane-spanning stretch.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The exact boundary annotation for the relevant helix—129..149 rather than 134..154—is not established by the sequence pattern alone.",
    "reason": "Family-level and hydropathy reasoning support the overall seven-helix topology, but the offered choices also test a fine boundary difference for which no clear sequence-based discriminator is available."
  },
  "case_id": "transmembrane_0059",
  "expected_answer_check": {
    "evidence_ids": [
      "H4",
      "H6",
      "H8",
      "H10",
      "H12",
      "H14",
      "H16"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched historical UniProt record annotates seven helical transmembrane regions at the coordinates listed in B. These annotations carry computational evidence code ECO:0000255, so they support the key as database annotations but are not, by themselves, experimental confirmation."
  },
  "important_caveats": [
    "The reviewer-only source evidence is sequence-matched, but the author's exact source snapshot is unknown.",
    "The source annotation is computational; the evidence supplied does not establish experimental validation of the precise boundaries."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "B"
    ],
    "reason": "Both choices describe seven spans, and their only difference is a five-residue shift in one predicted helix interval. Without a stated boundary convention or tolerance, both intervals could reasonably describe the same membrane-spanning helix."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0059",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched historical UniProt record annotates seven helical transmembrane regions at the coordinates listed in B. These annotations carry computational evidence code ECO:0000255, so they support the key as database annotations but are not, by themselves, experimental confirmation.",
    "evidence_ids": ["H4", "H6", "H8", "H10", "H12", "H14", "H16"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence has repeated hydrophobic stretches consistent with a seven-transmembrane receptor, which meaningfully favors the seven-span choices over C and helps reject D, which omits an apparent span. But this transferable pattern does not reliably distinguish B from A: they differ only in the proposed boundaries of one helix, and both intervals cover a plausible membrane-spanning stretch.",
    "missing_item_specific_fact": "The exact boundary annotation for the relevant helix—129..149 rather than 134..154—is not established by the sequence pattern alone.",
    "reason": "Family-level and hydropathy reasoning support the overall seven-helix topology, but the offered choices also test a fine boundary difference for which no clear sequence-based discriminator is available."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "B"],
    "reason": "Both choices describe seven spans, and their only difference is a five-residue shift in one predicted helix interval. Without a stated boundary convention or tolerance, both intervals could reasonably describe the same membrane-spanning helix."
  },
  "important_caveats": [
    "The reviewer-only source evidence is sequence-matched, but the author's exact source snapshot is unknown.",
    "The source annotation is computational; the evidence supplied does not establish experimental validation of the precise boundaries."
  ]
}
```

</details>

## After: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt annotation for G1XJN1 (Ascaroside receptor GPR3) lists exactly seven transmembrane helices at 17..37, 48..68, 94..114, 129..149, 176..196, 295..315, and 322..342, matching option B precisely. The evidence code ECO:0000255 indicates these are computational/similarity-based predictions (ProRule), consistent with the GPCR 7-TM architecture. The topological domains (extracellular 1..16, cytoplasmic 38..47, etc.) are consistent with the TM boundaries in option B.

Citations as saved: [C6](#evidence-c6), [C8](#evidence-c8), [C10](#evidence-c10), [C12](#evidence-c12), [C14](#evidence-c14), [C16](#evidence-c16), [C18](#evidence-c18).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> 1) GPCR family recognition: The sequence length (~401 aa), multiple hydrophobic stretches, and topology pattern (short N-terminal extracellular segment, alternating TM/cytoplasmic/extracellular segments, long intracellular loop ~197-294) are hallmarks of a 7-TM GPCR. This eliminates option C (only 3 TM) and option D (only 6 TM, missing the first TM near the N-terminus). 2) Distinguishing A from B (TM4 boundary): Option A places TM4 at 134..154, which includes D(151), Y(152), and N(154) — charged/polar residues at the C-terminal end that are inconsistent with a hydrophobic TM helix. Option B's TM4 at 129..149 (W-A-V-W-L-F-P-W-L-V-S-L-I-A-A-F-F-A-F-G-F) is a predominantly hydrophobic 21-residue stretch typical of GPCR TM helices. The preceding cytoplasmic loop (115-128, containing S-G-P-S-M-V-L-K-W-I-R-E-N-V) and following extracellular loop (150-175, containing W-D-Y-A-N-V-G-G-F-C-W-L-G-S-R-N-I-R-L-Y-F-N-Y-I-P-R-W) are consistent with B's boundaries. Hydrophobicity analysis of the raw sequence, combined with GPCR TM-length expectations (~20-25 hydrophobic residues), distinguishes B from A.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model recognizing GPCR architecture (7 TM, ~400 aa, long ICL3) can eliminate C and D. Hydrophobicity inspection of the 4th TM region reveals that option A's range (134-154) terminates with polar/charged residues (D, Y, N) incompatible with a lipid-embedded helix, while option B's range (129-149) is a continuous hydrophobic stretch. This is a standard transferable criterion for TM boundary assignment.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The options are well-differentiated: C has wrong TM count (3), D is missing a TM (6 instead of 7), and the A-vs-B distinction is resolvable by hydrophobicity of the 4th TM region. No two options are equally defensible.


### Important caveats

- The UniProt TM annotations use ECO:0000255 (computational prediction by similarity/ProRule), not experimental determination. However, the GPCR 7-TM architecture is one of the most robust structural predictions in biology.
- The exact residue-level boundaries (e.g., 129 vs 134 for TM4 start) are somewhat arbitrary in any prediction method, but the hydrophobicity argument clearly favors 129-149 over 134-154.
- The sequence is from a fungal GPCR (Arthrobotrys oligospora), which is less commonly studied than mammalian GPCRs, but the 7-TM architecture and hydrophobic TM helix principles are universal across the GPCR superfamily.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "1) GPCR family recognition: The sequence length (~401 aa), multiple hydrophobic stretches, and topology pattern (short N-terminal extracellular segment, alternating TM/cytoplasmic/extracellular segments, long intracellular loop ~197-294) are hallmarks of a 7-TM GPCR. This eliminates option C (only 3 TM) and option D (only 6 TM, missing the first TM near the N-terminus). 2) Distinguishing A from B (TM4 boundary): Option A places TM4 at 134..154, which includes D(151), Y(152), and N(154) — charged/polar residues at the C-terminal end that are inconsistent with a hydrophobic TM helix. Option B's TM4 at 129..149 (W-A-V-W-L-F-P-W-L-V-S-L-I-A-A-F-F-A-F-G-F) is a predominantly hydrophobic 21-residue stretch typical of GPCR TM helices. The preceding cytoplasmic loop (115-128, containing S-G-P-S-M-V-L-K-W-I-R-E-N-V) and following extracellular loop (150-175, containing W-D-Y-A-N-V-G-G-F-C-W-L-G-S-R-N-I-R-L-Y-F-N-Y-I-P-R-W) are consistent with B's boundaries. Hydrophobicity analysis of the raw sequence, combined with GPCR TM-length expectations (~20-25 hydrophobic residues), distinguishes B from A.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model recognizing GPCR architecture (7 TM, ~400 aa, long ICL3) can eliminate C and D. Hydrophobicity inspection of the 4th TM region reveals that option A's range (134-154) terminates with polar/charged residues (D, Y, N) incompatible with a lipid-embedded helix, while option B's range (129-149) is a continuous hydrophobic stretch. This is a standard transferable criterion for TM boundary assignment."
  },
  "case_id": "transmembrane_0059",
  "expected_answer_check": {
    "evidence_ids": [
      "C6",
      "C8",
      "C10",
      "C12",
      "C14",
      "C16",
      "C18"
    ],
    "judgment": "supported",
    "reason": "The UniProt annotation for G1XJN1 (Ascaroside receptor GPR3) lists exactly seven transmembrane helices at 17..37, 48..68, 94..114, 129..149, 176..196, 295..315, and 322..342, matching option B precisely. The evidence code ECO:0000255 indicates these are computational/similarity-based predictions (ProRule), consistent with the GPCR 7-TM architecture. The topological domains (extracellular 1..16, cytoplasmic 38..47, etc.) are consistent with the TM boundaries in option B."
  },
  "important_caveats": [
    "The UniProt TM annotations use ECO:0000255 (computational prediction by similarity/ProRule), not experimental determination. However, the GPCR 7-TM architecture is one of the most robust structural predictions in biology.",
    "The exact residue-level boundaries (e.g., 129 vs 134 for TM4 start) are somewhat arbitrary in any prediction method, but the hydrophobicity argument clearly favors 129-149 over 134-154.",
    "The sequence is from a fungal GPCR (Arthrobotrys oligospora), which is less commonly studied than mammalian GPCRs, but the 7-TM architecture and hydrophobic TM helix principles are universal across the GPCR superfamily."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The options are well-differentiated: C has wrong TM count (3), D is missing a TM (6 instead of 7), and the A-vs-B distinction is resolvable by hydrophobicity of the 4th TM region. No two options are equally defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{"case_id":"transmembrane_0059","expected_answer_check":{"judgment":"supported","reason":"The UniProt annotation for G1XJN1 (Ascaroside receptor GPR3) lists exactly seven transmembrane helices at 17..37, 48..68, 94..114, 129..149, 176..196, 295..315, and 322..342, matching option B precisely. The evidence code ECO:0000255 indicates these are computational/similarity-based predictions (ProRule), consistent with the GPCR 7-TM architecture. The topological domains (extracellular 1..16, cytoplasmic 38..47, etc.) are consistent with the TM boundaries in option B.","evidence_ids":["C6","C8","C10","C12","C14","C16","C18"]},"answerability_check":{"judgment":"reasoning_supported","discriminating_biological_argument":"1) GPCR family recognition: The sequence length (~401 aa), multiple hydrophobic stretches, and topology pattern (short N-terminal extracellular segment, alternating TM/cytoplasmic/extracellular segments, long intracellular loop ~197-294) are hallmarks of a 7-TM GPCR. This eliminates option C (only 3 TM) and option D (only 6 TM, missing the first TM near the N-terminus). 2) Distinguishing A from B (TM4 boundary): Option A places TM4 at 134..154, which includes D(151), Y(152), and N(154) — charged/polar residues at the C-terminal end that are inconsistent with a hydrophobic TM helix. Option B's TM4 at 129..149 (W-A-V-W-L-F-P-W-L-V-S-L-I-A-A-F-F-A-F-G-F) is a predominantly hydrophobic 21-residue stretch typical of GPCR TM helices. The preceding cytoplasmic loop (115-128, containing S-G-P-S-M-V-L-K-W-I-R-E-N-V) and following extracellular loop (150-175, containing W-D-Y-A-N-V-G-G-F-C-W-L-G-S-R-N-I-R-L-Y-F-N-Y-I-P-R-W) are consistent with B's boundaries. Hydrophobicity analysis of the raw sequence, combined with GPCR TM-length expectations (~20-25 hydrophobic residues), distinguishes B from A.","missing_item_specific_fact":"","reason":"A knowledgeable model recognizing GPCR architecture (7 TM, ~400 aa, long ICL3) can eliminate C and D. Hydrophobicity inspection of the 4th TM region reveals that option A's range (134-154) terminates with polar/charged residues (D, Y, N) incompatible with a lipid-embedded helix, while option B's range (129-149) is a continuous hydrophobic stretch. This is a standard transferable criterion for TM boundary assignment."},"question_ambiguity":{"multiple_defensible_options":[],"reason":"The options are well-differentiated: C has wrong TM count (3), D is missing a TM (6 instead of 7), and the A-vs-B distinction is resolvable by hydrophobicity of the 4th TM region. No two options are equally defensible."},"important_caveats":["The UniProt TM annotations use ECO:0000255 (computational prediction by similarity/ProRule), not experimental determination. However, the GPCR 7-TM architecture is one of the most robust structural predictions in biology.","The exact residue-level boundaries (e.g., 129 vs 134 for TM4 start) are somewhat arbitrary in any prediction method, but the hydrophobicity argument clearly favors 129-149 over 134-154.","The sequence is from a fungal GPCR (Arthrobotrys oligospora), which is less commonly studied than mammalian GPCRs, but the 7-TM architecture and hydrophobic TM helix principles are universal across the GPCR superfamily."]}
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
  "requested_accession": "G1XJN1",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "benchmark_sequence_sha256": "4dd73ee248fe4746f47939e543bfae15df5e67cdf643f70fa23f5cfc53ae8be0",
  "benchmark_sequence_length": 401,
  "current_status": "retrieved",
  "current_sequence_comparison": "matched",
  "current_entry_audit": {
    "entryVersion": 48,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2011-11-16",
    "sequenceVersion": 1
  },
  "current_uniprot_release": "2026_03",
  "current_record_sha256": "d1cb02451e5c1d2640cfcdf6c12c2a6a6f5853805bd439c3031dde0eea563a37",
  "current_source_sequence_sha256": "4dd73ee248fe4746f47939e543bfae15df5e67cdf643f70fa23f5cfc53ae8be0",
  "current_source_sequence_length": 401,
  "historical_status": "retrieved",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "selected_historical_entry_version": 46,
  "selected_historical_version": {
    "accession": "G1XJN1",
    "database": "Swiss-Prot",
    "entryVersion": 46,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "GPR3_ARTOA",
    "sequenceVersion": 1
  },
  "selected_historical_record_sha256": "3c78ac63e30f9e6fea6d4c3a7ddd8ee59ee45f0a9c5a7225b00c7055bec78804",
  "selected_historical_source_sequence_sha256": "4dd73ee248fe4746f47939e543bfae15df5e67cdf643f70fa23f5cfc53ae8be0",
  "selected_historical_source_sequence_length": 401,
  "latest_at_cutoff_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 46,
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G1XJN1.json)

```json
{
  "evidence_id": "C1",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/G1XJN1.json",
  "source_sha256": "d1cb02451e5c1d2640cfcdf6c12c2a6a6f5853805bd439c3031dde0eea563a37",
  "retrieved_utc": "2026-11-01T06:25:05.818783+00:00",
  "json_pointer": "/primaryAccession",
  "excerpt": "\"G1XJN1\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G1XJN1.json)

```json
{
  "evidence_id": "C2",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/G1XJN1.json",
  "source_sha256": "d1cb02451e5c1d2640cfcdf6c12c2a6a6f5853805bd439c3031dde0eea563a37",
  "retrieved_utc": "2026-11-01T06:25:05.818783+00:00",
  "json_pointer": "/entryAudit",
  "excerpt": "{\"entryVersion\":48,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2011-11-16\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G1XJN1.json)

```json
{
  "evidence_id": "C3",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/G1XJN1.json",
  "source_sha256": "d1cb02451e5c1d2640cfcdf6c12c2a6a6f5853805bd439c3031dde0eea563a37",
  "retrieved_utc": "2026-11-01T06:25:05.818783+00:00",
  "json_pointer": "/organism",
  "excerpt": "{\"commonName\":\"Nematode-trapping fungus\",\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP000008784\",\"source\":\"Proteomes\"}],\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Orbiliomycetes\",\"Orbiliales\",\"Orbiliaceae\",\"Orbilia\",\"Orbilia oligospora\"],\"scientificName\":\"Arthrobotrys oligospora (strain ATCC 24927 / CBS 115.81 / DSM 1491)\",\"synonyms\":[\"Didymozoophaga oligospora\"],\"taxonId\":756982}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G1XJN1.json)

```json
{
  "evidence_id": "C4",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/G1XJN1.json",
  "source_sha256": "d1cb02451e5c1d2640cfcdf6c12c2a6a6f5853805bd439c3031dde0eea563a37",
  "retrieved_utc": "2026-11-01T06:25:05.818783+00:00",
  "json_pointer": "/proteinDescription",
  "excerpt": "{\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Ascaroside receptor GPR3\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G1XJN1.json)

```json
{
  "evidence_id": "C5",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/G1XJN1.json",
  "source_sha256": "d1cb02451e5c1d2640cfcdf6c12c2a6a6f5853805bd439c3031dde0eea563a37",
  "retrieved_utc": "2026-11-01T06:25:05.818783+00:00",
  "json_pointer": "/features/1",
  "excerpt": "{\"description\":\"Extracellular\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":16},\"start\":{\"modifier\":\"EXACT\",\"value\":1}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G1XJN1.json)

```json
{
  "evidence_id": "C6",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/G1XJN1.json",
  "source_sha256": "d1cb02451e5c1d2640cfcdf6c12c2a6a6f5853805bd439c3031dde0eea563a37",
  "retrieved_utc": "2026-11-01T06:25:05.818783+00:00",
  "json_pointer": "/features/2",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":37},\"start\":{\"modifier\":\"EXACT\",\"value\":17}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G1XJN1.json)

```json
{
  "evidence_id": "C7",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/G1XJN1.json",
  "source_sha256": "d1cb02451e5c1d2640cfcdf6c12c2a6a6f5853805bd439c3031dde0eea563a37",
  "retrieved_utc": "2026-11-01T06:25:05.818783+00:00",
  "json_pointer": "/features/3",
  "excerpt": "{\"description\":\"Cytoplasmic\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":47},\"start\":{\"modifier\":\"EXACT\",\"value\":38}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G1XJN1.json)

```json
{
  "evidence_id": "C8",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/G1XJN1.json",
  "source_sha256": "d1cb02451e5c1d2640cfcdf6c12c2a6a6f5853805bd439c3031dde0eea563a37",
  "retrieved_utc": "2026-11-01T06:25:05.818783+00:00",
  "json_pointer": "/features/4",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":68},\"start\":{\"modifier\":\"EXACT\",\"value\":48}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G1XJN1.json)

```json
{
  "evidence_id": "C9",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/G1XJN1.json",
  "source_sha256": "d1cb02451e5c1d2640cfcdf6c12c2a6a6f5853805bd439c3031dde0eea563a37",
  "retrieved_utc": "2026-11-01T06:25:05.818783+00:00",
  "json_pointer": "/features/5",
  "excerpt": "{\"description\":\"Extracellular\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":93},\"start\":{\"modifier\":\"EXACT\",\"value\":69}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G1XJN1.json)

```json
{
  "evidence_id": "C10",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/G1XJN1.json",
  "source_sha256": "d1cb02451e5c1d2640cfcdf6c12c2a6a6f5853805bd439c3031dde0eea563a37",
  "retrieved_utc": "2026-11-01T06:25:05.818783+00:00",
  "json_pointer": "/features/6",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":114},\"start\":{\"modifier\":\"EXACT\",\"value\":94}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G1XJN1.json)

```json
{
  "evidence_id": "C11",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/G1XJN1.json",
  "source_sha256": "d1cb02451e5c1d2640cfcdf6c12c2a6a6f5853805bd439c3031dde0eea563a37",
  "retrieved_utc": "2026-11-01T06:25:05.818783+00:00",
  "json_pointer": "/features/7",
  "excerpt": "{\"description\":\"Cytoplasmic\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":128},\"start\":{\"modifier\":\"EXACT\",\"value\":115}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G1XJN1.json)

```json
{
  "evidence_id": "C12",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/G1XJN1.json",
  "source_sha256": "d1cb02451e5c1d2640cfcdf6c12c2a6a6f5853805bd439c3031dde0eea563a37",
  "retrieved_utc": "2026-11-01T06:25:05.818783+00:00",
  "json_pointer": "/features/8",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":149},\"start\":{\"modifier\":\"EXACT\",\"value\":129}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C13

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G1XJN1.json)

```json
{
  "evidence_id": "C13",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/G1XJN1.json",
  "source_sha256": "d1cb02451e5c1d2640cfcdf6c12c2a6a6f5853805bd439c3031dde0eea563a37",
  "retrieved_utc": "2026-11-01T06:25:05.818783+00:00",
  "json_pointer": "/features/9",
  "excerpt": "{\"description\":\"Extracellular\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":175},\"start\":{\"modifier\":\"EXACT\",\"value\":150}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C14

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G1XJN1.json)

```json
{
  "evidence_id": "C14",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/G1XJN1.json",
  "source_sha256": "d1cb02451e5c1d2640cfcdf6c12c2a6a6f5853805bd439c3031dde0eea563a37",
  "retrieved_utc": "2026-11-01T06:25:05.818783+00:00",
  "json_pointer": "/features/10",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":196},\"start\":{\"modifier\":\"EXACT\",\"value\":176}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C15

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G1XJN1.json)

```json
{
  "evidence_id": "C15",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/G1XJN1.json",
  "source_sha256": "d1cb02451e5c1d2640cfcdf6c12c2a6a6f5853805bd439c3031dde0eea563a37",
  "retrieved_utc": "2026-11-01T06:25:05.818783+00:00",
  "json_pointer": "/features/11",
  "excerpt": "{\"description\":\"Cytoplasmic\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":294},\"start\":{\"modifier\":\"EXACT\",\"value\":197}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C16

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G1XJN1.json)

```json
{
  "evidence_id": "C16",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/G1XJN1.json",
  "source_sha256": "d1cb02451e5c1d2640cfcdf6c12c2a6a6f5853805bd439c3031dde0eea563a37",
  "retrieved_utc": "2026-11-01T06:25:05.818783+00:00",
  "json_pointer": "/features/12",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":315},\"start\":{\"modifier\":\"EXACT\",\"value\":295}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C17

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G1XJN1.json)

```json
{
  "evidence_id": "C17",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/G1XJN1.json",
  "source_sha256": "d1cb02451e5c1d2640cfcdf6c12c2a6a6f5853805bd439c3031dde0eea563a37",
  "retrieved_utc": "2026-11-01T06:25:05.818783+00:00",
  "json_pointer": "/features/13",
  "excerpt": "{\"description\":\"Extracellular\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":321},\"start\":{\"modifier\":\"EXACT\",\"value\":316}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C18

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G1XJN1.json)

```json
{
  "evidence_id": "C18",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/G1XJN1.json",
  "source_sha256": "d1cb02451e5c1d2640cfcdf6c12c2a6a6f5853805bd439c3031dde0eea563a37",
  "retrieved_utc": "2026-11-01T06:25:05.818783+00:00",
  "json_pointer": "/features/14",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":342},\"start\":{\"modifier\":\"EXACT\",\"value\":322}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C19

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G1XJN1.json)

```json
{
  "evidence_id": "C19",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/G1XJN1.json",
  "source_sha256": "d1cb02451e5c1d2640cfcdf6c12c2a6a6f5853805bd439c3031dde0eea563a37",
  "retrieved_utc": "2026-11-01T06:25:05.818783+00:00",
  "json_pointer": "/features/15",
  "excerpt": "{\"description\":\"Cytoplasmic\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":401},\"start\":{\"modifier\":\"EXACT\",\"value\":343}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G1XJN1?format=txt&versions=46)

```json
{
  "evidence_id": "H1",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/G1XJN1?format=txt&versions=46",
  "source_sha256": "3c78ac63e30f9e6fea6d4c3a7ddd8ee59ee45f0a9c5a7225b00c7055bec78804",
  "retrieved_utc": "2026-11-01T06:28:00.513965+00:00",
  "source_locator": "lines 1-13",
  "excerpt": "ID   GPR3_ARTOA              Reviewed;         401 AA.\nAC   G1XJN1;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   16-NOV-2011, sequence version 1.\nDT   28-JAN-2026, entry version 46.\nDE   RecName: Full=Ascaroside receptor GPR3 {ECO:0000305};\nGN   Name=GPR3 {ECO:0000303|PubMed:38649409};\nGN   ORFNames=AOL_s00097g558 {ECO:0000312|EMBL:EGX46654.1};\nOS   Arthrobotrys oligospora (strain ATCC 24927 / CBS 115.81 / DSM 1491)\nOS   (Nematode-trapping fungus) (Didymozoophaga oligospora).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Orbiliomycetes;\nOC   Orbiliales; Orbiliaceae; Orbilia; Orbilia oligospora.\nOX   NCBI_TaxID=756982 {ECO:0000312|Proteomes:UP000008784};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 46,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G1XJN1?format=txt&versions=46)

```json
{
  "evidence_id": "H2",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/G1XJN1?format=txt&versions=46",
  "source_sha256": "3c78ac63e30f9e6fea6d4c3a7ddd8ee59ee45f0a9c5a7225b00c7055bec78804",
  "retrieved_utc": "2026-11-01T06:28:00.513965+00:00",
  "source_locator": "lines 25-34",
  "excerpt": "RN   [2] {ECO:0000305}\nRP   FUNCTION, INTERACTION WITH GPA2 AND GPR2, SUBCELLULAR LOCATION, INDUCTION,\nRP   AND DISRUPTION PHENOTYPE.\nRC   STRAIN=TWF154 {ECO:0000303|PubMed:38649409};\nRX   PubMed=38649409; DOI=10.1038/s41564-024-01679-w;\nRA   Kuo C.Y., Tay R.J., Lin H.C., Juan S.C., Vidal-Diez de Ulzurrun G.,\nRA   Chang Y.C., Hoki J., Schroeder F.C., Hsueh Y.P.;\nRT   \"The nematode-trapping fungus Arthrobotrys oligospora detects prey\nRT   pheromones via G protein-coupled receptors.\";\nRL   Nat. Microbiol. 9:1738-1751(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 46,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G1XJN1?format=txt&versions=46)

```json
{
  "evidence_id": "H3",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/G1XJN1?format=txt&versions=46",
  "source_sha256": "3c78ac63e30f9e6fea6d4c3a7ddd8ee59ee45f0a9c5a7225b00c7055bec78804",
  "retrieved_utc": "2026-11-01T06:28:00.513965+00:00",
  "source_locator": "lines 96-98",
  "excerpt": "FT   TOPO_DOM        1..16\nFT                   /note=\"Extracellular\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 46,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G1XJN1?format=txt&versions=46)

```json
{
  "evidence_id": "H4",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/G1XJN1?format=txt&versions=46",
  "source_sha256": "3c78ac63e30f9e6fea6d4c3a7ddd8ee59ee45f0a9c5a7225b00c7055bec78804",
  "retrieved_utc": "2026-11-01T06:28:00.513965+00:00",
  "source_locator": "lines 99-101",
  "excerpt": "FT   TRANSMEM        17..37\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 46,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G1XJN1?format=txt&versions=46)

```json
{
  "evidence_id": "H5",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/G1XJN1?format=txt&versions=46",
  "source_sha256": "3c78ac63e30f9e6fea6d4c3a7ddd8ee59ee45f0a9c5a7225b00c7055bec78804",
  "retrieved_utc": "2026-11-01T06:28:00.513965+00:00",
  "source_locator": "lines 102-104",
  "excerpt": "FT   TOPO_DOM        38..47\nFT                   /note=\"Cytoplasmic\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 46,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G1XJN1?format=txt&versions=46)

```json
{
  "evidence_id": "H6",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/G1XJN1?format=txt&versions=46",
  "source_sha256": "3c78ac63e30f9e6fea6d4c3a7ddd8ee59ee45f0a9c5a7225b00c7055bec78804",
  "retrieved_utc": "2026-11-01T06:28:00.513965+00:00",
  "source_locator": "lines 105-107",
  "excerpt": "FT   TRANSMEM        48..68\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 46,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G1XJN1?format=txt&versions=46)

```json
{
  "evidence_id": "H7",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/G1XJN1?format=txt&versions=46",
  "source_sha256": "3c78ac63e30f9e6fea6d4c3a7ddd8ee59ee45f0a9c5a7225b00c7055bec78804",
  "retrieved_utc": "2026-11-01T06:28:00.513965+00:00",
  "source_locator": "lines 108-110",
  "excerpt": "FT   TOPO_DOM        69..93\nFT                   /note=\"Extracellular\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 46,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G1XJN1?format=txt&versions=46)

```json
{
  "evidence_id": "H8",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/G1XJN1?format=txt&versions=46",
  "source_sha256": "3c78ac63e30f9e6fea6d4c3a7ddd8ee59ee45f0a9c5a7225b00c7055bec78804",
  "retrieved_utc": "2026-11-01T06:28:00.513965+00:00",
  "source_locator": "lines 111-113",
  "excerpt": "FT   TRANSMEM        94..114\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 46,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G1XJN1?format=txt&versions=46)

```json
{
  "evidence_id": "H9",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/G1XJN1?format=txt&versions=46",
  "source_sha256": "3c78ac63e30f9e6fea6d4c3a7ddd8ee59ee45f0a9c5a7225b00c7055bec78804",
  "retrieved_utc": "2026-11-01T06:28:00.513965+00:00",
  "source_locator": "lines 114-116",
  "excerpt": "FT   TOPO_DOM        115..128\nFT                   /note=\"Cytoplasmic\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 46,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H10

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G1XJN1?format=txt&versions=46)

```json
{
  "evidence_id": "H10",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/G1XJN1?format=txt&versions=46",
  "source_sha256": "3c78ac63e30f9e6fea6d4c3a7ddd8ee59ee45f0a9c5a7225b00c7055bec78804",
  "retrieved_utc": "2026-11-01T06:28:00.513965+00:00",
  "source_locator": "lines 117-119",
  "excerpt": "FT   TRANSMEM        129..149\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 46,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H11

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G1XJN1?format=txt&versions=46)

```json
{
  "evidence_id": "H11",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/G1XJN1?format=txt&versions=46",
  "source_sha256": "3c78ac63e30f9e6fea6d4c3a7ddd8ee59ee45f0a9c5a7225b00c7055bec78804",
  "retrieved_utc": "2026-11-01T06:28:00.513965+00:00",
  "source_locator": "lines 120-122",
  "excerpt": "FT   TOPO_DOM        150..175\nFT                   /note=\"Extracellular\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 46,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H12

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G1XJN1?format=txt&versions=46)

```json
{
  "evidence_id": "H12",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/G1XJN1?format=txt&versions=46",
  "source_sha256": "3c78ac63e30f9e6fea6d4c3a7ddd8ee59ee45f0a9c5a7225b00c7055bec78804",
  "retrieved_utc": "2026-11-01T06:28:00.513965+00:00",
  "source_locator": "lines 123-125",
  "excerpt": "FT   TRANSMEM        176..196\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 46,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H13

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G1XJN1?format=txt&versions=46)

```json
{
  "evidence_id": "H13",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/G1XJN1?format=txt&versions=46",
  "source_sha256": "3c78ac63e30f9e6fea6d4c3a7ddd8ee59ee45f0a9c5a7225b00c7055bec78804",
  "retrieved_utc": "2026-11-01T06:28:00.513965+00:00",
  "source_locator": "lines 126-128",
  "excerpt": "FT   TOPO_DOM        197..294\nFT                   /note=\"Cytoplasmic\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 46,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H14

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G1XJN1?format=txt&versions=46)

```json
{
  "evidence_id": "H14",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/G1XJN1?format=txt&versions=46",
  "source_sha256": "3c78ac63e30f9e6fea6d4c3a7ddd8ee59ee45f0a9c5a7225b00c7055bec78804",
  "retrieved_utc": "2026-11-01T06:28:00.513965+00:00",
  "source_locator": "lines 129-131",
  "excerpt": "FT   TRANSMEM        295..315\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 46,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H15

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G1XJN1?format=txt&versions=46)

```json
{
  "evidence_id": "H15",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/G1XJN1?format=txt&versions=46",
  "source_sha256": "3c78ac63e30f9e6fea6d4c3a7ddd8ee59ee45f0a9c5a7225b00c7055bec78804",
  "retrieved_utc": "2026-11-01T06:28:00.513965+00:00",
  "source_locator": "lines 132-134",
  "excerpt": "FT   TOPO_DOM        316..321\nFT                   /note=\"Extracellular\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 46,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H16

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G1XJN1?format=txt&versions=46)

```json
{
  "evidence_id": "H16",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/G1XJN1?format=txt&versions=46",
  "source_sha256": "3c78ac63e30f9e6fea6d4c3a7ddd8ee59ee45f0a9c5a7225b00c7055bec78804",
  "retrieved_utc": "2026-11-01T06:28:00.513965+00:00",
  "source_locator": "lines 135-137",
  "excerpt": "FT   TRANSMEM        322..342\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 46,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H17

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G1XJN1?format=txt&versions=46)

```json
{
  "evidence_id": "H17",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/G1XJN1?format=txt&versions=46",
  "source_sha256": "3c78ac63e30f9e6fea6d4c3a7ddd8ee59ee45f0a9c5a7225b00c7055bec78804",
  "retrieved_utc": "2026-11-01T06:28:00.513965+00:00",
  "source_locator": "lines 138-140",
  "excerpt": "FT   TOPO_DOM        343..401\nFT                   /note=\"Cytoplasmic\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 46,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json), zero-based source row 59. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
