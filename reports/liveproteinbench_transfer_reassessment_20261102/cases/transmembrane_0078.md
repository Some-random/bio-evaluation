# transmembrane_0078: before and after transfer clarification

[All 1,328 cases](../README.md) · [Method](../METHOD.md) · [Summary](../SUMMARY.md) · [Exact reviewer user message](../inputs/transmembrane_0078.txt)

**Task:** `transmembrane`  
**Author key, unchanged:** **D** — 3..23

| Round | Reviewer | Key support | Transfer / lookup | Output usability (canonical status) |
|---|---|---|---|---|
| before | GPT-6 Luna | supported | lookup-dependent | usable output (valid_review) |
| before | Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | usable output (valid_review) |
| after | GPT-6 Luna | supported | reasoning-supported | usable output (valid_review) |
| after | Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | usable output (valid_review) |

**Usable output means format-valid review, not reasoning-supported or biologically correct.** A usable output can classify the question as reasoning-supported, lookup-dependent or uncertain. An output error is a problem with the saved model response; it does not count a defective benchmark question or wrong key. Each saved review is retained in full below. Labels from output errors are displayed as saved and excluded from label statistics. The author key and reviewer evidence were visible to reviewers; this is a review of answerability and key support, not a benchmark-solving score.

## Complete original question

```text
[Protein Sequence]
MDKISIIPIVGVALSLAIILQLGRTYWRLRHIPGPFPACITNFQRVGWVKTKRAHLILQDMHKKYGEVVRIGPNMVSFSNPEVIPTVYPARSGFPKGDFYVTLRPYTRGGGALHAVFNTTEEDLHKQIKSPIAPMFTPANTPSFEGLVDEVLTCIHEKLDENFIANSEIFNLGQWLQYFAFDVMGTMTFSKRYGFLDTGKDVGRMLGTIVDFMRDAAPMTQIPWLDWALRKNRIGDSIQRLFGKTASLGILGFVGKAIKERQELLSKGDFKVSDEKSGRKDFLTRFIELQQNDPKIPPWAPTAWTFSNVIAGSDSVGSLMRTTMFNLLVYPHTLEKLHDELRSAGVSRPYPKWSEIRNLLYLDACVQEGARMHPPFALPFERVVPAGGITILGYYLPGGTVVGGSPYVVNRHRETFGRDAEFWRPERWLESDEGHKRKLEQGVLTFGAGRRVCLGKHVGILEIKKLISFLVLNYDIRVVNPEKFELENSWFFFQRGLYATIRKRPDAVAVKNQQV

[Multiple Choices]
A. 3..23; 635..655
B. 5..27
C. 3..18
D. 3..23
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

> The sequence matches the cited UniProt entry, which annotates residues 3–23 as a helical transmembrane region. The annotation is computational (ECO:0000255), not presented here as experimental evidence.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The strong N-terminal hydrophobic stretch around residues 4–23 supports a membrane-spanning helix; the much later interval in A is outside this 515-residue protein, and C truncates the hydrophobic stretch.


**Missing item-specific fact**

> Choosing the exact annotated boundaries 3–23 rather than the overlapping 5–27 requires a boundary convention or protein-specific annotation not supplied in the question.


**Reason**

> Sequence hydropathy identifies the likely N-terminal transmembrane region, but its fuzzy boundaries do not robustly settle the close choice between D and B.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "D"
]
```

> Both intervals overlap the N-terminal hydrophobic helix; residues near the C-terminal boundary, including aromatic residues, can plausibly be included as membrane-interface or helix-boundary residues.


### Important caveats

- Reviewer-only evidence supports the key but was absent from the evaluated input.
- The supplied evidence supports a computational database annotation, not an independently verified experimental boundary.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The strong N-terminal hydrophobic stretch around residues 4–23 supports a membrane-spanning helix; the much later interval in A is outside this 515-residue protein, and C truncates the hydrophobic stretch.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "Choosing the exact annotated boundaries 3–23 rather than the overlapping 5–27 requires a boundary convention or protein-specific annotation not supplied in the question.",
    "reason": "Sequence hydropathy identifies the likely N-terminal transmembrane region, but its fuzzy boundaries do not robustly settle the close choice between D and B."
  },
  "case_id": "transmembrane_0078",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The sequence matches the cited UniProt entry, which annotates residues 3–23 as a helical transmembrane region. The annotation is computational (ECO:0000255), not presented here as experimental evidence."
  },
  "important_caveats": [
    "Reviewer-only evidence supports the key but was absent from the evaluated input.",
    "The supplied evidence supports a computational database annotation, not an independently verified experimental boundary."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "D"
    ],
    "reason": "Both intervals overlap the N-terminal hydrophobic helix; residues near the C-terminal boundary, including aromatic residues, can plausibly be included as membrane-interface or helix-boundary residues."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0078",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches the cited UniProt entry, which annotates residues 3–23 as a helical transmembrane region. The annotation is computational (ECO:0000255), not presented here as experimental evidence.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The strong N-terminal hydrophobic stretch around residues 4–23 supports a membrane-spanning helix; the much later interval in A is outside this 515-residue protein, and C truncates the hydrophobic stretch.",
    "missing_item_specific_fact": "Choosing the exact annotated boundaries 3–23 rather than the overlapping 5–27 requires a boundary convention or protein-specific annotation not supplied in the question.",
    "reason": "Sequence hydropathy identifies the likely N-terminal transmembrane region, but its fuzzy boundaries do not robustly settle the close choice between D and B."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "D"],
    "reason": "Both intervals overlap the N-terminal hydrophobic helix; residues near the C-terminal boundary, including aromatic residues, can plausibly be included as membrane-interface or helix-boundary residues."
  },
  "important_caveats": [
    "Reviewer-only evidence supports the key but was absent from the evaluated input.",
    "The supplied evidence supports a computational database annotation, not an independently verified experimental boundary."
  ]
}
```

</details>

## Before: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt annotation (evidence C5, H3) explicitly annotates a transmembrane helix at positions 3..23 with note 'Helical'. The sequence at positions 3-23 (KISIIPIVGVALSLAIILQLG) is predominantly hydrophobic, consistent with a TM helix. However, the evidence code is ECO:0000255 (inferred by similarity), meaning this is a computational annotation rather than experimental determination. The sequence match is confirmed (SHA256 identical).

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3), [C1](#evidence-c1).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Option A is eliminated because position 635..655 exceeds the 515-residue protein length. Option B (5..27) includes polar/aromatic residues R(24), T(25), Y(26), W(27) that disrupt the hydrophobic stretch, making it an implausible TM boundary. Between C (3..18, 16 residues) and D (3..23, 21 residues): a transmembrane alpha-helix requires approximately 20 residues (at ~1.5 Å/residue rise) to span the ~30 Å hydrophobic core of the lipid bilayer. The hydrophobic stretch KISIIPIVGVALSLAIILQLG extends through position 23, with the core hydrophobicity (I, V, A, L, S) persisting past position 18. Sixteen residues (option C) is too short for a complete TM helix, while 21 residues (option D) is within the typical 18-25 range.


**Missing item-specific fact**

> None critical. The exact endpoint (23 vs 20 or 22) involves some algorithmic boundary-determination judgment, but the broad biological reasoning (helix length requirement, hydrophobic stretch extent) meaningfully distinguishes D from C.


**Reason**

> A model can eliminate A (out of range) and B (polar residues at boundary) by simple sequence inspection, then use the well-established requirement that TM helices need ~20 residues to span the membrane to prefer D (21 residues) over C (16 residues). The hydrophobic character of positions 19-23 (I, L, Q, L, G) supports extension beyond 18.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "C"
]
```

> Option C (3..18) represents a defensible but short TM prediction. The Q at position 21 is a polar residue that could argue for ending the helix earlier. However, the 16-residue length of C falls below the minimum needed to span the bilayer, and L(22)/G(23) are compatible with TM helix interiors, making D the stronger choice by biological reasoning.


### Important caveats

- The UniProt annotation uses ECO:0000255 (inferred by similarity), meaning the 3..23 boundary is a computational prediction, not an experimental measurement.
- The exact TM helix boundary (e.g., 20 vs 22 vs 23) is inherently algorithm-dependent; the question tests the correct annotation rather than an experimentally validated value.
- Option A's second range (635..655) is trivially impossible for a 515-residue protein, serving as a distractor.
- The annotation was first public in April 2025; the author's source snapshot is unknown but the sequence matches across all checked versions.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Option A is eliminated because position 635..655 exceeds the 515-residue protein length. Option B (5..27) includes polar/aromatic residues R(24), T(25), Y(26), W(27) that disrupt the hydrophobic stretch, making it an implausible TM boundary. Between C (3..18, 16 residues) and D (3..23, 21 residues): a transmembrane alpha-helix requires approximately 20 residues (at ~1.5 Å/residue rise) to span the ~30 Å hydrophobic core of the lipid bilayer. The hydrophobic stretch KISIIPIVGVALSLAIILQLG extends through position 23, with the core hydrophobicity (I, V, A, L, S) persisting past position 18. Sixteen residues (option C) is too short for a complete TM helix, while 21 residues (option D) is within the typical 18-25 range.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None critical. The exact endpoint (23 vs 20 or 22) involves some algorithmic boundary-determination judgment, but the broad biological reasoning (helix length requirement, hydrophobic stretch extent) meaningfully distinguishes D from C.",
    "reason": "A model can eliminate A (out of range) and B (polar residues at boundary) by simple sequence inspection, then use the well-established requirement that TM helices need ~20 residues to span the membrane to prefer D (21 residues) over C (16 residues). The hydrophobic character of positions 19-23 (I, L, Q, L, G) supports extension beyond 18."
  },
  "case_id": "transmembrane_0078",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3",
      "C1"
    ],
    "judgment": "supported",
    "reason": "UniProt annotation (evidence C5, H3) explicitly annotates a transmembrane helix at positions 3..23 with note 'Helical'. The sequence at positions 3-23 (KISIIPIVGVALSLAIILQLG) is predominantly hydrophobic, consistent with a TM helix. However, the evidence code is ECO:0000255 (inferred by similarity), meaning this is a computational annotation rather than experimental determination. The sequence match is confirmed (SHA256 identical)."
  },
  "important_caveats": [
    "The UniProt annotation uses ECO:0000255 (inferred by similarity), meaning the 3..23 boundary is a computational prediction, not an experimental measurement.",
    "The exact TM helix boundary (e.g., 20 vs 22 vs 23) is inherently algorithm-dependent; the question tests the correct annotation rather than an experimentally validated value.",
    "Option A's second range (635..655) is trivially impossible for a 515-residue protein, serving as a distractor.",
    "The annotation was first public in April 2025; the author's source snapshot is unknown but the sequence matches across all checked versions."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "C"
    ],
    "reason": "Option C (3..18) represents a defensible but short TM prediction. The Q at position 21 is a polar residue that could argue for ending the helix earlier. However, the 16-residue length of C falls below the minimum needed to span the bilayer, and L(22)/G(23) are compatible with TM helix interiors, making D the stronger choice by biological reasoning."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0078",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt annotation (evidence C5, H3) explicitly annotates a transmembrane helix at positions 3..23 with note 'Helical'. The sequence at positions 3-23 (KISIIPIVGVALSLAIILQLG) is predominantly hydrophobic, consistent with a TM helix. However, the evidence code is ECO:0000255 (inferred by similarity), meaning this is a computational annotation rather than experimental determination. The sequence match is confirmed (SHA256 identical).",
    "evidence_ids": ["C5", "H3", "C1"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Option A is eliminated because position 635..655 exceeds the 515-residue protein length. Option B (5..27) includes polar/aromatic residues R(24), T(25), Y(26), W(27) that disrupt the hydrophobic stretch, making it an implausible TM boundary. Between C (3..18, 16 residues) and D (3..23, 21 residues): a transmembrane alpha-helix requires approximately 20 residues (at ~1.5 Å/residue rise) to span the ~30 Å hydrophobic core of the lipid bilayer. The hydrophobic stretch KISIIPIVGVALSLAIILQLG extends through position 23, with the core hydrophobicity (I, V, A, L, S) persisting past position 18. Sixteen residues (option C) is too short for a complete TM helix, while 21 residues (option D) is within the typical 18-25 range.",
    "missing_item_specific_fact": "None critical. The exact endpoint (23 vs 20 or 22) involves some algorithmic boundary-determination judgment, but the broad biological reasoning (helix length requirement, hydrophobic stretch extent) meaningfully distinguishes D from C.",
    "reason": "A model can eliminate A (out of range) and B (polar residues at boundary) by simple sequence inspection, then use the well-established requirement that TM helices need ~20 residues to span the membrane to prefer D (21 residues) over C (16 residues). The hydrophobic character of positions 19-23 (I, L, Q, L, G) supports extension beyond 18."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["C"],
    "reason": "Option C (3..18) represents a defensible but short TM prediction. The Q at position 21 is a polar residue that could argue for ending the helix earlier. However, the 16-residue length of C falls below the minimum needed to span the bilayer, and L(22)/G(23) are compatible with TM helix interiors, making D the stronger choice by biological reasoning."
  },
  "important_caveats": [
    "The UniProt annotation uses ECO:0000255 (inferred by similarity), meaning the 3..23 boundary is a computational prediction, not an experimental measurement.",
    "The exact TM helix boundary (e.g., 20 vs 22 vs 23) is inherently algorithm-dependent; the question tests the correct annotation rather than an experimentally validated value.",
    "Option A's second range (635..655) is trivially impossible for a 515-residue protein, serving as a distractor.",
    "The annotation was first public in April 2025; the author's source snapshot is unknown but the sequence matches across all checked versions."
  ]
}
```

</details>

## After: GPT-6 Luna

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence-matched UniProt record annotates a helical transmembrane region at 3..23. This is computational annotation (ECO:0000255), not direct experimental evidence.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Residues 3..23 form a long, strongly hydrophobic stretch, consistent with a membrane-spanning alpha helix. This favors D over C, which truncates the stretch, and B, which extends into the more polar and charged sequence after it. A also includes coordinates beyond this 515-residue sequence.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The sequence itself contains a recognizable hydrophobic transmembrane segment, so transferable knowledge of membrane-spanning helices meaningfully distinguishes the offered choices.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the offered choices, 3..23 best captures the hydrophobic segment; the alternatives either truncate it, extend it into non-hydrophobic residues, or include out-of-range coordinates.


### Important caveats

- The supporting database feature is computationally annotated; the supplied evidence does not establish experimental confirmation of membrane insertion or exact boundaries.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Residues 3..23 form a long, strongly hydrophobic stretch, consistent with a membrane-spanning alpha helix. This favors D over C, which truncates the stretch, and B, which extends into the more polar and charged sequence after it. A also includes coordinates beyond this 515-residue sequence.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The sequence itself contains a recognizable hydrophobic transmembrane segment, so transferable knowledge of membrane-spanning helices meaningfully distinguishes the offered choices."
  },
  "case_id": "transmembrane_0078",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates a helical transmembrane region at 3..23. This is computational annotation (ECO:0000255), not direct experimental evidence."
  },
  "important_caveats": [
    "The supporting database feature is computationally annotated; the supplied evidence does not establish experimental confirmation of membrane insertion or exact boundaries."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the offered choices, 3..23 best captures the hydrophobic segment; the alternatives either truncate it, extend it into non-hydrophobic residues, or include out-of-range coordinates."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0078",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates a helical transmembrane region at 3..23. This is computational annotation (ECO:0000255), not direct experimental evidence.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Residues 3..23 form a long, strongly hydrophobic stretch, consistent with a membrane-spanning alpha helix. This favors D over C, which truncates the stretch, and B, which extends into the more polar and charged sequence after it. A also includes coordinates beyond this 515-residue sequence.",
    "missing_item_specific_fact": "",
    "reason": "The sequence itself contains a recognizable hydrophobic transmembrane segment, so transferable knowledge of membrane-spanning helices meaningfully distinguishes the offered choices."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the offered choices, 3..23 best captures the hydrophobic segment; the alternatives either truncate it, extend it into non-hydrophobic residues, or include out-of-range coordinates."
  },
  "important_caveats": [
    "The supporting database feature is computationally annotated; the supplied evidence does not establish experimental confirmation of membrane insertion or exact boundaries."
  ]
}
```

</details>

## After: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt annotation (evidence code ECO:0000255, inferred by similarity) records a transmembrane helix at positions 3..23. The segment KISIIPIVGVALSLAIILQLG (21 residues) is predominantly hydrophobic with boundary residues (K at 3, G at 23), consistent with a TM alpha-helix of appropriate length. The annotation is computational/inferred rather than experimentally verified, but it directly supports the expected answer.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Several transferable principles distinguish D from the other choices. (1) Option A is trivially eliminated because positions 635-655 exceed the 515-residue protein length. (2) A TM alpha-helix requires approximately 19-21 residues to span the ~30 Å hydrophobic core of the lipid bilayer; option C (3..18) provides only 16 residues, which is below the minimum helix length for membrane crossing. (3) Option B (5..27) extends into positions 24-27 (R, T, Y, W), which include a charged Arg and aromatic Trp/Tyr residues that are characteristic of the membrane-water interface, not the hydrophobic core. (4) Option D (3..23) yields a 21-residue segment that is predominantly hydrophobic (I, I, I, P, I, V, V, A, L, L, A, I, I, L, L) with boundary residues (K, S, Q, G) at the edges, matching the expected length and composition of a TM helix. This reasoning relies on general TM helix biophysics learned from many membrane proteins, not on memorizing this specific entry.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The discrimination among options relies on well-established general principles: TM helix length (~19-21 residues), hydrophobic composition, boundary residue patterns (charged/aromatic at interfaces), and simple arithmetic (option A exceeds protein length). No fact specific to this exact protein beyond reading the sequence is needed.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Option A is eliminated by length; option C is too short for a TM helix; option B includes clearly non-TM residues (Arg, Tyr, Trp). Only D satisfies both the length requirement and the hydrophobic composition criterion for a TM alpha-helix.


### Important caveats

- The UniProt annotation uses evidence code ECO:0000255 (inferred by similarity), meaning the TM assignment is computational rather than experimentally determined.
- The segment 3-23 is not a 'textbook' pure-hydrophobic TM helix; it contains several polar residues (K, S, S, Q, G), which is common in real TM helices but makes purely hydrophobicity-based prediction less crisp.
- The protein is a fungal cytochrome P450 monooxygenase (mfmA from Annulohypoxylon moriforme), a family in which N-terminal TM anchoring to the ER membrane is a well-known feature, further supporting the annotation.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Several transferable principles distinguish D from the other choices. (1) Option A is trivially eliminated because positions 635-655 exceed the 515-residue protein length. (2) A TM alpha-helix requires approximately 19-21 residues to span the ~30 Å hydrophobic core of the lipid bilayer; option C (3..18) provides only 16 residues, which is below the minimum helix length for membrane crossing. (3) Option B (5..27) extends into positions 24-27 (R, T, Y, W), which include a charged Arg and aromatic Trp/Tyr residues that are characteristic of the membrane-water interface, not the hydrophobic core. (4) Option D (3..23) yields a 21-residue segment that is predominantly hydrophobic (I, I, I, P, I, V, V, A, L, L, A, I, I, L, L) with boundary residues (K, S, Q, G) at the edges, matching the expected length and composition of a TM helix. This reasoning relies on general TM helix biophysics learned from many membrane proteins, not on memorizing this specific entry.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The discrimination among options relies on well-established general principles: TM helix length (~19-21 residues), hydrophobic composition, boundary residue patterns (charged/aromatic at interfaces), and simple arithmetic (option A exceeds protein length). No fact specific to this exact protein beyond reading the sequence is needed."
  },
  "case_id": "transmembrane_0078",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The UniProt annotation (evidence code ECO:0000255, inferred by similarity) records a transmembrane helix at positions 3..23. The segment KISIIPIVGVALSLAIILQLG (21 residues) is predominantly hydrophobic with boundary residues (K at 3, G at 23), consistent with a TM alpha-helix of appropriate length. The annotation is computational/inferred rather than experimentally verified, but it directly supports the expected answer."
  },
  "important_caveats": [
    "The UniProt annotation uses evidence code ECO:0000255 (inferred by similarity), meaning the TM assignment is computational rather than experimentally determined.",
    "The segment 3-23 is not a 'textbook' pure-hydrophobic TM helix; it contains several polar residues (K, S, S, Q, G), which is common in real TM helices but makes purely hydrophobicity-based prediction less crisp.",
    "The protein is a fungal cytochrome P450 monooxygenase (mfmA from Annulohypoxylon moriforme), a family in which N-terminal TM anchoring to the ER membrane is a well-known feature, further supporting the annotation."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Option A is eliminated by length; option C is too short for a TM helix; option B includes clearly non-TM residues (Arg, Tyr, Trp). Only D satisfies both the length requirement and the hydrophobic composition criterion for a TM alpha-helix."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0078",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt annotation (evidence code ECO:0000255, inferred by similarity) records a transmembrane helix at positions 3..23. The segment KISIIPIVGVALSLAIILQLG (21 residues) is predominantly hydrophobic with boundary residues (K at 3, G at 23), consistent with a TM alpha-helix of appropriate length. The annotation is computational/inferred rather than experimentally verified, but it directly supports the expected answer.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Several transferable principles distinguish D from the other choices. (1) Option A is trivially eliminated because positions 635-655 exceed the 515-residue protein length. (2) A TM alpha-helix requires approximately 19-21 residues to span the ~30 Å hydrophobic core of the lipid bilayer; option C (3..18) provides only 16 residues, which is below the minimum helix length for membrane crossing. (3) Option B (5..27) extends into positions 24-27 (R, T, Y, W), which include a charged Arg and aromatic Trp/Tyr residues that are characteristic of the membrane-water interface, not the hydrophobic core. (4) Option D (3..23) yields a 21-residue segment that is predominantly hydrophobic (I, I, I, P, I, V, V, A, L, L, A, I, I, L, L) with boundary residues (K, S, Q, G) at the edges, matching the expected length and composition of a TM helix. This reasoning relies on general TM helix biophysics learned from many membrane proteins, not on memorizing this specific entry.",
    "missing_item_specific_fact": "",
    "reason": "The discrimination among options relies on well-established general principles: TM helix length (~19-21 residues), hydrophobic composition, boundary residue patterns (charged/aromatic at interfaces), and simple arithmetic (option A exceeds protein length). No fact specific to this exact protein beyond reading the sequence is needed."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Option A is eliminated by length; option C is too short for a TM helix; option B includes clearly non-TM residues (Arg, Tyr, Trp). Only D satisfies both the length requirement and the hydrophobic composition criterion for a TM alpha-helix."
  },
  "important_caveats": [
    "The UniProt annotation uses evidence code ECO:0000255 (inferred by similarity), meaning the TM assignment is computational rather than experimentally determined.",
    "The segment 3-23 is not a 'textbook' pure-hydrophobic TM helix; it contains several polar residues (K, S, S, Q, G), which is common in real TM helices but makes purely hydrophobicity-based prediction less crisp.",
    "The protein is a fungal cytochrome P450 monooxygenase (mfmA from Annulohypoxylon moriforme), a family in which N-terminal TM anchoring to the ER membrane is a well-known feature, further supporting the annotation."
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
  "requested_accession": "P9WEG0",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "benchmark_sequence_sha256": "b148dd6535a2478e2a065541559f956e45ac653fa2dceff0ebdbeae21e9d5591",
  "benchmark_sequence_length": 515,
  "current_status": "retrieved",
  "current_sequence_comparison": "matched",
  "current_entry_audit": {
    "entryVersion": 5,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2025-04-09",
    "sequenceVersion": 1
  },
  "current_uniprot_release": "2026_03",
  "current_record_sha256": "a6e6527f5d1306f7f6b07d9ae1a2faeb4bf00fa63555cc612e053eae8f17e600",
  "current_source_sequence_sha256": "b148dd6535a2478e2a065541559f956e45ac653fa2dceff0ebdbeae21e9d5591",
  "current_source_sequence_length": 515,
  "historical_status": "retrieved",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "selected_historical_entry_version": 3,
  "selected_historical_version": {
    "accession": "P9WEG0",
    "database": "Swiss-Prot",
    "entryVersion": 3,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "MFMA_ANNMO",
    "sequenceVersion": 1
  },
  "selected_historical_record_sha256": "3b311182ec72cd21034e97a0da2e7b1c6f9097ddf71e067e2d78b84e2753fac2",
  "selected_historical_source_sequence_sha256": "b148dd6535a2478e2a065541559f956e45ac653fa2dceff0ebdbeae21e9d5591",
  "selected_historical_source_sequence_length": 515,
  "latest_at_cutoff_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 3,
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P9WEG0.json)

```json
{
  "evidence_id": "C1",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/P9WEG0.json",
  "source_sha256": "a6e6527f5d1306f7f6b07d9ae1a2faeb4bf00fa63555cc612e053eae8f17e600",
  "retrieved_utc": "2026-11-02T04:30:13.096452+00:00",
  "json_pointer": "/primaryAccession",
  "excerpt": "\"P9WEG0\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P9WEG0.json)

```json
{
  "evidence_id": "C2",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/P9WEG0.json",
  "source_sha256": "a6e6527f5d1306f7f6b07d9ae1a2faeb4bf00fa63555cc612e053eae8f17e600",
  "retrieved_utc": "2026-11-02T04:30:13.096452+00:00",
  "json_pointer": "/entryAudit",
  "excerpt": "{\"entryVersion\":5,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2025-04-09\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P9WEG0.json)

```json
{
  "evidence_id": "C3",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/P9WEG0.json",
  "source_sha256": "a6e6527f5d1306f7f6b07d9ae1a2faeb4bf00fa63555cc612e053eae8f17e600",
  "retrieved_utc": "2026-11-02T04:30:13.096452+00:00",
  "json_pointer": "/organism",
  "excerpt": "{\"commonName\":\"Filamentous fungus\",\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Sordariomycetes\",\"Xylariomycetidae\",\"Xylariales\",\"Hypoxylaceae\",\"Annulohypoxylon\"],\"scientificName\":\"Annulohypoxylon moriforme\",\"synonyms\":[\"Hypoxylon moriforme\"],\"taxonId\":326622}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P9WEG0.json)

```json
{
  "evidence_id": "C4",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/P9WEG0.json",
  "source_sha256": "a6e6527f5d1306f7f6b07d9ae1a2faeb4bf00fa63555cc612e053eae8f17e600",
  "retrieved_utc": "2026-11-02T04:30:13.096452+00:00",
  "json_pointer": "/proteinDescription",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"38404388\",\"source\":\"PubMed\"}],\"value\":\"11'-O-desmethylfendlerol biosynthesis cluster protein A\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38404388\",\"source\":\"PubMed\"}],\"value\":\"1.-.-.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"38404388\",\"source\":\"PubMed\"}],\"value\":\"Cytochrome P450 monooxygenase mfmA\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P9WEG0.json)

```json
{
  "evidence_id": "C5",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/P9WEG0.json",
  "source_sha256": "a6e6527f5d1306f7f6b07d9ae1a2faeb4bf00fa63555cc612e053eae8f17e600",
  "retrieved_utc": "2026-11-02T04:30:13.096452+00:00",
  "json_pointer": "/features/1",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":23},\"start\":{\"modifier\":\"EXACT\",\"value\":3}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P9WEG0.json)

```json
{
  "evidence_id": "C6",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/P9WEG0.json",
  "source_sha256": "a6e6527f5d1306f7f6b07d9ae1a2faeb4bf00fa63555cc612e053eae8f17e600",
  "retrieved_utc": "2026-11-02T04:30:13.096452+00:00",
  "json_pointer": "/references/1",
  "excerpt": "{\"citation\":{\"authors\":[\"Yan D.\",\"Matsuda Y.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"38404388\"},{\"database\":\"DOI\",\"id\":\"10.1039/d3sc06001b\"}],\"citationType\":\"journal article\",\"firstPage\":\"3011\",\"id\":\"38404388\",\"journal\":\"Chem. Sci.\",\"lastPage\":\"3017\",\"publicationDate\":\"2024\",\"title\":\"Global genome mining-driven discovery of an unusual biosynthetic logic for fungal polyketide-terpenoid hybrids.\",\"volume\":\"15\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"CBS 123579\"}],\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"PATHWAY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P9WEG0?format=txt&versions=3)

```json
{
  "evidence_id": "H1",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/P9WEG0?format=txt&versions=3",
  "source_sha256": "3b311182ec72cd21034e97a0da2e7b1c6f9097ddf71e067e2d78b84e2753fac2",
  "retrieved_utc": "2026-11-02T04:30:18.350529+00:00",
  "source_locator": "lines 1-13",
  "excerpt": "ID   MFMA_ANNMO              Reviewed;         515 AA.\nAC   P9WEG0;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   09-APR-2025, sequence version 1.\nDT   28-JAN-2026, entry version 3.\nDE   RecName: Full=Cytochrome P450 monooxygenase mfmA {ECO:0000303|PubMed:38404388};\nDE            EC=1.-.-.- {ECO:0000269|PubMed:38404388};\nDE   AltName: Full=11'-O-desmethylfendlerol biosynthesis cluster protein A {ECO:0000303|PubMed:38404388};\nGN   Name=mfmA {ECO:0000303|PubMed:38404388}; ORFNames=F4805DRAFT_29954;\nOS   Annulohypoxylon moriforme (Filamentous fungus) (Hypoxylon moriforme).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Sordariomycetes;\nOC   Xylariomycetidae; Xylariales; Hypoxylaceae; Annulohypoxylon.\nOX   NCBI_TaxID=326622;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 3,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P9WEG0?format=txt&versions=3)

```json
{
  "evidence_id": "H2",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/P9WEG0?format=txt&versions=3",
  "source_sha256": "3b311182ec72cd21034e97a0da2e7b1c6f9097ddf71e067e2d78b84e2753fac2",
  "retrieved_utc": "2026-11-02T04:30:18.350529+00:00",
  "source_locator": "lines 28-35",
  "excerpt": "RN   [2]\nRP   FUNCTION, CATALYTIC ACTIVITY, AND PATHWAY.\nRC   STRAIN=CBS 123579;\nRX   PubMed=38404388; DOI=10.1039/d3sc06001b;\nRA   Yan D., Matsuda Y.;\nRT   \"Global genome mining-driven discovery of an unusual biosynthetic logic for\nRT   fungal polyketide-terpenoid hybrids.\";\nRL   Chem. Sci. 15:3011-3017(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 3,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P9WEG0?format=txt&versions=3)

```json
{
  "evidence_id": "H3",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/P9WEG0?format=txt&versions=3",
  "source_sha256": "3b311182ec72cd21034e97a0da2e7b1c6f9097ddf71e067e2d78b84e2753fac2",
  "retrieved_utc": "2026-11-02T04:30:18.350529+00:00",
  "source_locator": "lines 96-98",
  "excerpt": "FT   TRANSMEM        3..23\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 3,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json), zero-based source row 78. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
