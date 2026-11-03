# transmembrane_0049: before and after transfer clarification

[All 1,328 cases](../README.md) · [Method](../METHOD.md) · [Summary](../SUMMARY.md) · [Exact reviewer user message](../inputs/transmembrane_0049.txt)

**Task:** `transmembrane`  
**Author key, unchanged:** **B** — 35..55; 68..88; 99..119; 139..159

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
MADFPGKVSTQTSSQEPQRSFAISSSVDMGFIKSIPGILLIAEIVVGLLVWTLIASTPHYLIPALGWVLFVSITLWLLSIALLVILLLSLHQRLPSVPWPLVLLVFYSVAALLYLTAFLANAATVPGGYYQGHLGASAFFGIVETLLYTASSYFAYLGWRGEGQNAAGSTVPV

[Multiple Choices]
A. 35..55; 99..119; 139..159
B. 35..55; 68..88; 99..119; 139..159
C. 35..55
D. 35..55; 63..83; 99..119; 139..159
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

> The sequence exactly matches the historical UniProt record, which annotates transmembrane helices at 35–55, 68–88, 99–119, and 139–159—the intervals in B. The helix annotations carry computational evidence code ECO:0000255, so this supports the key as a database annotation, not as independently established experimental evidence.

Citations as saved: [H3](#evidence-h3), [H5](#evidence-h5), [H7](#evidence-h7), [H9](#evidence-h9).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence contains long hydrophobic stretches consistent with multiple membrane-spanning helices, including a particularly hydrophobic region around residues 63–88. That supports identifying the general region, but does not reliably establish its exact annotated boundaries.


**Missing item-specific fact**

> The protein-specific annotation locating the second helix at 68–88 rather than the also-hydrophobic 63–83 interval is not supplied in the question.


**Reason**

> The sequence permits broad transmembrane-region inference, but the choices test exact boundaries within a continuous hydrophobic stretch. General sequence reasoning does not clearly distinguish B from D.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "D"
]
```

> Both choices include the same strongly hydrophobic second region but give different boundaries. The sequence alone does not unambiguously determine those precise endpoints.


### Important caveats

- Reviewer-only database evidence was not available to the evaluated model.
- The cited transmembrane annotations are computational; the supplied evidence does not independently verify the boundaries experimentally.
- The source record sequence matches the input, but the author's exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains long hydrophobic stretches consistent with multiple membrane-spanning helices, including a particularly hydrophobic region around residues 63–88. That supports identifying the general region, but does not reliably establish its exact annotated boundaries.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific annotation locating the second helix at 68–88 rather than the also-hydrophobic 63–83 interval is not supplied in the question.",
    "reason": "The sequence permits broad transmembrane-region inference, but the choices test exact boundaries within a continuous hydrophobic stretch. General sequence reasoning does not clearly distinguish B from D."
  },
  "case_id": "transmembrane_0049",
  "expected_answer_check": {
    "evidence_ids": [
      "H3",
      "H5",
      "H7",
      "H9"
    ],
    "judgment": "supported",
    "reason": "The sequence exactly matches the historical UniProt record, which annotates transmembrane helices at 35–55, 68–88, 99–119, and 139–159—the intervals in B. The helix annotations carry computational evidence code ECO:0000255, so this supports the key as a database annotation, not as independently established experimental evidence."
  },
  "important_caveats": [
    "Reviewer-only database evidence was not available to the evaluated model.",
    "The cited transmembrane annotations are computational; the supplied evidence does not independently verify the boundaries experimentally.",
    "The source record sequence matches the input, but the author's exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "D"
    ],
    "reason": "Both choices include the same strongly hydrophobic second region but give different boundaries. The sequence alone does not unambiguously determine those precise endpoints."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0049",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence exactly matches the historical UniProt record, which annotates transmembrane helices at 35–55, 68–88, 99–119, and 139–159—the intervals in B. The helix annotations carry computational evidence code ECO:0000255, so this supports the key as a database annotation, not as independently established experimental evidence.",
    "evidence_ids": ["H3", "H5", "H7", "H9"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence contains long hydrophobic stretches consistent with multiple membrane-spanning helices, including a particularly hydrophobic region around residues 63–88. That supports identifying the general region, but does not reliably establish its exact annotated boundaries.",
    "missing_item_specific_fact": "The protein-specific annotation locating the second helix at 68–88 rather than the also-hydrophobic 63–83 interval is not supplied in the question.",
    "reason": "The sequence permits broad transmembrane-region inference, but the choices test exact boundaries within a continuous hydrophobic stretch. General sequence reasoning does not clearly distinguish B from D."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "D"],
    "reason": "Both choices include the same strongly hydrophobic second region but give different boundaries. The sequence alone does not unambiguously determine those precise endpoints."
  },
  "important_caveats": [
    "Reviewer-only database evidence was not available to the evaluated model.",
    "The cited transmembrane annotations are computational; the supplied evidence does not independently verify the boundaries experimentally.",
    "The source record sequence matches the input, but the author's exact source snapshot is unknown."
  ]
}
```

</details>

## Before: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt annotation for A3KQ86 (Zebrafish Plasmolipin, 173 aa, sequence matched) lists exactly four helical transmembrane segments at 35..55, 68..88, 99..119, and 139..159, matching choice B precisely. The evidence code ECO:0000255 indicates these are inferred by similarity (computational), not experimentally determined, but the annotation is consistent with the sequence. Sequence-level hydrophobicity analysis also supports these boundaries: the 56-67 extracellular loop contains polar residues (S, T, H, Y) and helix-breaking residues (P at 58, P at 63, G at 66), making 68..88 a more plausible hydrophobic helix start than 63..83.

Citations as saved: [C6](#evidence-c6), [C8](#evidence-c8), [C10](#evidence-c10), [C12](#evidence-c12), [H3](#evidence-h3), [H5](#evidence-h5), [H7](#evidence-h7), [H9](#evidence-h9).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The question can be addressed through hydrophobicity analysis of the sequence. (1) Counting long hydrophobic stretches (~20 residues) identifies four candidate TM helices, eliminating C (one TM) and A (three TMs, missing the second). (2) The critical distinction between B (68..88) and D (63..83) rests on the composition of residues 63-67: P(63), A(64), L(65), G(66), W(67). Proline and glycine are well-established alpha-helix breakers; their presence within a proposed 21-residue TM helix (63..83) is structurally implausible. Additionally, residues 56-62 (S, T, P, H, Y, L, I) are predominantly polar/charged, forming a clear extracellular loop. Starting the helix at 68 (V) yields a clean hydrophobic stretch VLFVSITLWLLSIALLVILL. The flanking polar/charged residues at 89-93 (S, L, H, Q, R) confirm the helix end at 88.


**Missing item-specific fact**

> None strictly required. The helix-breaking properties of proline and glycine, the hydrophobicity of the 68-88 stretch, and the polar character of the 56-67 loop are all general biochemical knowledge applicable to any sequence.


**Reason**

> A model with general knowledge of TM helix composition (hydrophobic residues, ~20-aa length, avoidance of helix breakers like Pro and Gly in the transmembrane core) can distinguish B from D by identifying P at 63 and G at 66 as incompatible with a TM helix, and can distinguish B from A and C by recognizing four distinct hydrophobic stretches. The exact residue-level boundaries require precision but are defensible from the sequence alone.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> While one might argue for slight boundary shifts (e.g., 67..88 vs 68..88), the choices are constructed so that only B matches both the correct number of TMs (four) and a helix composition free of internal helix-breaking residues. D is clearly weaker because it includes P and G within the helix. A and C omit TMs that are clearly hydrophobic in the sequence.


### Important caveats

- All four TM annotations carry evidence code ECO:0000255 (inferred by similarity), meaning they are computational predictions from homology, not experimental measurements. The 'correct' answer reflects a database annotation, not experimentally validated topology.
- The UniProt entry was first public on 2025-02-05; the author's source snapshot date is unknown, though the sequence version (1) has been stable since 2007.
- The reviewer-only evidence (accession A3KQ86, UniProt annotations) was not available to the evaluated model; the model must reason from the raw sequence and general biology alone.
- Exact TM boundaries (e.g., whether the helix starts at 67 or 68) are inherently approximate in computational predictions; the question's multiple-choice format constrains the answer to the provided options.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The question can be addressed through hydrophobicity analysis of the sequence. (1) Counting long hydrophobic stretches (~20 residues) identifies four candidate TM helices, eliminating C (one TM) and A (three TMs, missing the second). (2) The critical distinction between B (68..88) and D (63..83) rests on the composition of residues 63-67: P(63), A(64), L(65), G(66), W(67). Proline and glycine are well-established alpha-helix breakers; their presence within a proposed 21-residue TM helix (63..83) is structurally implausible. Additionally, residues 56-62 (S, T, P, H, Y, L, I) are predominantly polar/charged, forming a clear extracellular loop. Starting the helix at 68 (V) yields a clean hydrophobic stretch VLFVSITLWLLSIALLVILL. The flanking polar/charged residues at 89-93 (S, L, H, Q, R) confirm the helix end at 88.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None strictly required. The helix-breaking properties of proline and glycine, the hydrophobicity of the 68-88 stretch, and the polar character of the 56-67 loop are all general biochemical knowledge applicable to any sequence.",
    "reason": "A model with general knowledge of TM helix composition (hydrophobic residues, ~20-aa length, avoidance of helix breakers like Pro and Gly in the transmembrane core) can distinguish B from D by identifying P at 63 and G at 66 as incompatible with a TM helix, and can distinguish B from A and C by recognizing four distinct hydrophobic stretches. The exact residue-level boundaries require precision but are defensible from the sequence alone."
  },
  "case_id": "transmembrane_0049",
  "expected_answer_check": {
    "evidence_ids": [
      "C6",
      "C8",
      "C10",
      "C12",
      "H3",
      "H5",
      "H7",
      "H9"
    ],
    "judgment": "supported",
    "reason": "The UniProt annotation for A3KQ86 (Zebrafish Plasmolipin, 173 aa, sequence matched) lists exactly four helical transmembrane segments at 35..55, 68..88, 99..119, and 139..159, matching choice B precisely. The evidence code ECO:0000255 indicates these are inferred by similarity (computational), not experimentally determined, but the annotation is consistent with the sequence. Sequence-level hydrophobicity analysis also supports these boundaries: the 56-67 extracellular loop contains polar residues (S, T, H, Y) and helix-breaking residues (P at 58, P at 63, G at 66), making 68..88 a more plausible hydrophobic helix start than 63..83."
  },
  "important_caveats": [
    "All four TM annotations carry evidence code ECO:0000255 (inferred by similarity), meaning they are computational predictions from homology, not experimental measurements. The 'correct' answer reflects a database annotation, not experimentally validated topology.",
    "The UniProt entry was first public on 2025-02-05; the author's source snapshot date is unknown, though the sequence version (1) has been stable since 2007.",
    "The reviewer-only evidence (accession A3KQ86, UniProt annotations) was not available to the evaluated model; the model must reason from the raw sequence and general biology alone.",
    "Exact TM boundaries (e.g., whether the helix starts at 67 or 68) are inherently approximate in computational predictions; the question's multiple-choice format constrains the answer to the provided options."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While one might argue for slight boundary shifts (e.g., 67..88 vs 68..88), the choices are constructed so that only B matches both the correct number of TMs (four) and a helix composition free of internal helix-breaking residues. D is clearly weaker because it includes P and G within the helix. A and C omit TMs that are clearly hydrophobic in the sequence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0049",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt annotation for A3KQ86 (Zebrafish Plasmolipin, 173 aa, sequence matched) lists exactly four helical transmembrane segments at 35..55, 68..88, 99..119, and 139..159, matching choice B precisely. The evidence code ECO:0000255 indicates these are inferred by similarity (computational), not experimentally determined, but the annotation is consistent with the sequence. Sequence-level hydrophobicity analysis also supports these boundaries: the 56-67 extracellular loop contains polar residues (S, T, H, Y) and helix-breaking residues (P at 58, P at 63, G at 66), making 68..88 a more plausible hydrophobic helix start than 63..83.",
    "evidence_ids": ["C6", "C8", "C10", "C12", "H3", "H5", "H7", "H9"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The question can be addressed through hydrophobicity analysis of the sequence. (1) Counting long hydrophobic stretches (~20 residues) identifies four candidate TM helices, eliminating C (one TM) and A (three TMs, missing the second). (2) The critical distinction between B (68..88) and D (63..83) rests on the composition of residues 63-67: P(63), A(64), L(65), G(66), W(67). Proline and glycine are well-established alpha-helix breakers; their presence within a proposed 21-residue TM helix (63..83) is structurally implausible. Additionally, residues 56-62 (S, T, P, H, Y, L, I) are predominantly polar/charged, forming a clear extracellular loop. Starting the helix at 68 (V) yields a clean hydrophobic stretch VLFVSITLWLLSIALLVILL. The flanking polar/charged residues at 89-93 (S, L, H, Q, R) confirm the helix end at 88.",
    "missing_item_specific_fact": "None strictly required. The helix-breaking properties of proline and glycine, the hydrophobicity of the 68-88 stretch, and the polar character of the 56-67 loop are all general biochemical knowledge applicable to any sequence.",
    "reason": "A model with general knowledge of TM helix composition (hydrophobic residues, ~20-aa length, avoidance of helix breakers like Pro and Gly in the transmembrane core) can distinguish B from D by identifying P at 63 and G at 66 as incompatible with a TM helix, and can distinguish B from A and C by recognizing four distinct hydrophobic stretches. The exact residue-level boundaries require precision but are defensible from the sequence alone."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While one might argue for slight boundary shifts (e.g., 67..88 vs 68..88), the choices are constructed so that only B matches both the correct number of TMs (four) and a helix composition free of internal helix-breaking residues. D is clearly weaker because it includes P and G within the helix. A and C omit TMs that are clearly hydrophobic in the sequence."
  },
  "important_caveats": [
    "All four TM annotations carry evidence code ECO:0000255 (inferred by similarity), meaning they are computational predictions from homology, not experimental measurements. The 'correct' answer reflects a database annotation, not experimentally validated topology.",
    "The UniProt entry was first public on 2025-02-05; the author's source snapshot date is unknown, though the sequence version (1) has been stable since 2007.",
    "The reviewer-only evidence (accession A3KQ86, UniProt annotations) was not available to the evaluated model; the model must reason from the raw sequence and general biology alone.",
    "Exact TM boundaries (e.g., whether the helix starts at 67 or 68) are inherently approximate in computational predictions; the question's multiple-choice format constrains the answer to the provided options."
  ]
}
```

</details>

## After: GPT-6 Luna

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The matched UniProt record annotates four helical transmembrane regions at 35..55, 68..88, 99..119, and 139..159, matching B. These annotations carry computational evidence code ECO:0000255, so they support the key as database annotation, not as independent experimental confirmation.

Citations as saved: [C6](#evidence-c6), [C8](#evidence-c8), [C10](#evidence-c10), [C12](#evidence-c12).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has four conspicuously hydrophobic stretches, consistent with a small multipass membrane protein. Their lengths and hydrophobic composition support the four-helix choices B and D, while A omits one such stretch and C omits several. The second stretch has a particularly hydrophobic core around 68..88; the proline near the start of D's 63..83 interval makes B a plausible better boundary estimate.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Transferable knowledge about transmembrane helices and hydrophobic sequence patterns meaningfully distinguishes the four-span options from those listing fewer spans. However, the sequence alone does not sharply establish the precise boundaries of the second interval.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "D"
]
```

> Both options include the same four apparent hydrophobic spans, and the proposed second intervals overlap substantially. Since the task asks for a segment that crosses the membrane without defining a boundary convention, 63..83 could plausibly identify the same crossing helix as 68..88, despite B being the better-supported boundary estimate.


### Important caveats

- The supplied source evidence is reviewer-only and was not part of the original model input.
- The cited database transmembrane annotations are computationally evidenced, not established here by direct experimental measurements.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has four conspicuously hydrophobic stretches, consistent with a small multipass membrane protein. Their lengths and hydrophobic composition support the four-helix choices B and D, while A omits one such stretch and C omits several. The second stretch has a particularly hydrophobic core around 68..88; the proline near the start of D's 63..83 interval makes B a plausible better boundary estimate.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Transferable knowledge about transmembrane helices and hydrophobic sequence patterns meaningfully distinguishes the four-span options from those listing fewer spans. However, the sequence alone does not sharply establish the precise boundaries of the second interval."
  },
  "case_id": "transmembrane_0049",
  "expected_answer_check": {
    "evidence_ids": [
      "C6",
      "C8",
      "C10",
      "C12"
    ],
    "judgment": "supported",
    "reason": "The matched UniProt record annotates four helical transmembrane regions at 35..55, 68..88, 99..119, and 139..159, matching B. These annotations carry computational evidence code ECO:0000255, so they support the key as database annotation, not as independent experimental confirmation."
  },
  "important_caveats": [
    "The supplied source evidence is reviewer-only and was not part of the original model input.",
    "The cited database transmembrane annotations are computationally evidenced, not established here by direct experimental measurements."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "D"
    ],
    "reason": "Both options include the same four apparent hydrophobic spans, and the proposed second intervals overlap substantially. Since the task asks for a segment that crosses the membrane without defining a boundary convention, 63..83 could plausibly identify the same crossing helix as 68..88, despite B being the better-supported boundary estimate."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0049",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The matched UniProt record annotates four helical transmembrane regions at 35..55, 68..88, 99..119, and 139..159, matching B. These annotations carry computational evidence code ECO:0000255, so they support the key as database annotation, not as independent experimental confirmation.",
    "evidence_ids": ["C6", "C8", "C10", "C12"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has four conspicuously hydrophobic stretches, consistent with a small multipass membrane protein. Their lengths and hydrophobic composition support the four-helix choices B and D, while A omits one such stretch and C omits several. The second stretch has a particularly hydrophobic core around 68..88; the proline near the start of D's 63..83 interval makes B a plausible better boundary estimate.",
    "missing_item_specific_fact": "",
    "reason": "Transferable knowledge about transmembrane helices and hydrophobic sequence patterns meaningfully distinguishes the four-span options from those listing fewer spans. However, the sequence alone does not sharply establish the precise boundaries of the second interval."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "D"],
    "reason": "Both options include the same four apparent hydrophobic spans, and the proposed second intervals overlap substantially. Since the task asks for a segment that crosses the membrane without defining a boundary convention, 63..83 could plausibly identify the same crossing helix as 68..88, despite B being the better-supported boundary estimate."
  },
  "important_caveats": [
    "The supplied source evidence is reviewer-only and was not part of the original model input.",
    "The cited database transmembrane annotations are computationally evidenced, not established here by direct experimental measurements."
  ]
}
```

</details>

## After: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt annotation for A3KQ86 (Plasmolipin, Zebrafish) explicitly lists four transmembrane helices at 35..55, 68..88, 99..119, and 139..159, matching choice B exactly. The evidence codes are ECO:0000255 (predicted by similarity) and ECO:0000305 (inferred by curator), indicating computational/curator-based annotation rather than direct experimental determination, but the annotation is consistent with the hydrophobicity profile of the sequence. The topological domains (cytoplasmic 1-34, extracellular 56-67, cytoplasmic 89-98, extracellular 120-138, cytoplasmic 160-173) are internally consistent with a 4-TM topology.

Citations as saved: [C6](#evidence-c6), [C8](#evidence-c8), [C10](#evidence-c10), [C12](#evidence-c12), [H3](#evidence-h3), [H5](#evidence-h5), [H7](#evidence-h7), [H9](#evidence-h9).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Two layers of transferable reasoning distinguish B from the alternatives. First, the number of TM segments: the 173-AA sequence contains four distinct hydrophobic stretches (~21 residues each) separated by short polar/charged loops, making a 4-TM topology clear and eliminating C (1 TM) and A (3 TMs, which omits the obvious hydrophobic region at ~68-88: VLFVSITLWLLSIALLVILLL). Second, B vs D differ only in the second TM boundary (68..88 vs 63..83). Position 63 is proline, a well-known alpha-helix breaker; TM helices virtually never initiate with proline. The residues 56-67 (STHYLIPALGW) contain serine, threonine, histidine, and tyrosine—polar residues characteristic of a short aqueous loop—while position 68 begins with valine, a canonical helix-forming hydrophobic residue. Additionally, plasmolipin-family proteins are a recognized 4-TM membrane protein family, providing family-level support for exactly four segments. The loop lengths implied by B (12, 10, 19 AA) are more typical of short extracellular/cytoplasmic loops than those implied by D (7, 15, 19 AA).


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can identify four hydrophobic segments by hydropathy analysis, eliminate A and C, and then use the proline-helix-breaker rule at position 63 plus the polar composition of the 56-67 loop to favor 68..88 (B) over 63..83 (D). Family-level knowledge of 4-TM plasmolipin proteins further corroborates four segments. No fact specific to this exact protein beyond the sequence itself is required.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The proline at position 63 and the polar residues in the 56-67 stretch provide a clear, concrete sequence-based argument against D's 63..83 boundary. The four hydrophobic stretches are sufficiently distinct to rule out A and C. While exact TM boundaries can have ±1-2 residue uncertainty in practice, the offered choices differ by 5 residues, well within the range where the proline and loop-composition arguments discriminate.


### Important caveats

- The UniProt TM annotations use ECO:0000255 (similarity-based prediction), so they are computational predictions rather than experimentally determined boundaries. The exact residue-level boundaries could shift slightly with different prediction algorithms.
- The reviewer-only evidence confirms the sequence matches A3KQ86 (Plasmolipin, Danio rerio), but the evaluated model was not given the protein name or organism; the reasoning above relies only on the raw sequence and general biological knowledge.
- The third TM region (139..159: FFGIVETLLYTASSYFAYLGW) contains several polar residues (E, T, S, S, Y) and is the least hydrophobic of the four; a strict hydropathy threshold might question it, but all four answer choices include this segment, so it does not affect discrimination among options.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Two layers of transferable reasoning distinguish B from the alternatives. First, the number of TM segments: the 173-AA sequence contains four distinct hydrophobic stretches (~21 residues each) separated by short polar/charged loops, making a 4-TM topology clear and eliminating C (1 TM) and A (3 TMs, which omits the obvious hydrophobic region at ~68-88: VLFVSITLWLLSIALLVILLL). Second, B vs D differ only in the second TM boundary (68..88 vs 63..83). Position 63 is proline, a well-known alpha-helix breaker; TM helices virtually never initiate with proline. The residues 56-67 (STHYLIPALGW) contain serine, threonine, histidine, and tyrosine—polar residues characteristic of a short aqueous loop—while position 68 begins with valine, a canonical helix-forming hydrophobic residue. Additionally, plasmolipin-family proteins are a recognized 4-TM membrane protein family, providing family-level support for exactly four segments. The loop lengths implied by B (12, 10, 19 AA) are more typical of short extracellular/cytoplasmic loops than those implied by D (7, 15, 19 AA).",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can identify four hydrophobic segments by hydropathy analysis, eliminate A and C, and then use the proline-helix-breaker rule at position 63 plus the polar composition of the 56-67 loop to favor 68..88 (B) over 63..83 (D). Family-level knowledge of 4-TM plasmolipin proteins further corroborates four segments. No fact specific to this exact protein beyond the sequence itself is required."
  },
  "case_id": "transmembrane_0049",
  "expected_answer_check": {
    "evidence_ids": [
      "C6",
      "C8",
      "C10",
      "C12",
      "H3",
      "H5",
      "H7",
      "H9"
    ],
    "judgment": "supported",
    "reason": "The UniProt annotation for A3KQ86 (Plasmolipin, Zebrafish) explicitly lists four transmembrane helices at 35..55, 68..88, 99..119, and 139..159, matching choice B exactly. The evidence codes are ECO:0000255 (predicted by similarity) and ECO:0000305 (inferred by curator), indicating computational/curator-based annotation rather than direct experimental determination, but the annotation is consistent with the hydrophobicity profile of the sequence. The topological domains (cytoplasmic 1-34, extracellular 56-67, cytoplasmic 89-98, extracellular 120-138, cytoplasmic 160-173) are internally consistent with a 4-TM topology."
  },
  "important_caveats": [
    "The UniProt TM annotations use ECO:0000255 (similarity-based prediction), so they are computational predictions rather than experimentally determined boundaries. The exact residue-level boundaries could shift slightly with different prediction algorithms.",
    "The reviewer-only evidence confirms the sequence matches A3KQ86 (Plasmolipin, Danio rerio), but the evaluated model was not given the protein name or organism; the reasoning above relies only on the raw sequence and general biological knowledge.",
    "The third TM region (139..159: FFGIVETLLYTASSYFAYLGW) contains several polar residues (E, T, S, S, Y) and is the least hydrophobic of the four; a strict hydropathy threshold might question it, but all four answer choices include this segment, so it does not affect discrimination among options."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The proline at position 63 and the polar residues in the 56-67 stretch provide a clear, concrete sequence-based argument against D's 63..83 boundary. The four hydrophobic stretches are sufficiently distinct to rule out A and C. While exact TM boundaries can have ±1-2 residue uncertainty in practice, the offered choices differ by 5 residues, well within the range where the proline and loop-composition arguments discriminate."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0049",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt annotation for A3KQ86 (Plasmolipin, Zebrafish) explicitly lists four transmembrane helices at 35..55, 68..88, 99..119, and 139..159, matching choice B exactly. The evidence codes are ECO:0000255 (predicted by similarity) and ECO:0000305 (inferred by curator), indicating computational/curator-based annotation rather than direct experimental determination, but the annotation is consistent with the hydrophobicity profile of the sequence. The topological domains (cytoplasmic 1-34, extracellular 56-67, cytoplasmic 89-98, extracellular 120-138, cytoplasmic 160-173) are internally consistent with a 4-TM topology.",
    "evidence_ids": ["C6", "C8", "C10", "C12", "H3", "H5", "H7", "H9"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Two layers of transferable reasoning distinguish B from the alternatives. First, the number of TM segments: the 173-AA sequence contains four distinct hydrophobic stretches (~21 residues each) separated by short polar/charged loops, making a 4-TM topology clear and eliminating C (1 TM) and A (3 TMs, which omits the obvious hydrophobic region at ~68-88: VLFVSITLWLLSIALLVILLL). Second, B vs D differ only in the second TM boundary (68..88 vs 63..83). Position 63 is proline, a well-known alpha-helix breaker; TM helices virtually never initiate with proline. The residues 56-67 (STHYLIPALGW) contain serine, threonine, histidine, and tyrosine—polar residues characteristic of a short aqueous loop—while position 68 begins with valine, a canonical helix-forming hydrophobic residue. Additionally, plasmolipin-family proteins are a recognized 4-TM membrane protein family, providing family-level support for exactly four segments. The loop lengths implied by B (12, 10, 19 AA) are more typical of short extracellular/cytoplasmic loops than those implied by D (7, 15, 19 AA).",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can identify four hydrophobic segments by hydropathy analysis, eliminate A and C, and then use the proline-helix-breaker rule at position 63 plus the polar composition of the 56-67 loop to favor 68..88 (B) over 63..83 (D). Family-level knowledge of 4-TM plasmolipin proteins further corroborates four segments. No fact specific to this exact protein beyond the sequence itself is required."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The proline at position 63 and the polar residues in the 56-67 stretch provide a clear, concrete sequence-based argument against D's 63..83 boundary. The four hydrophobic stretches are sufficiently distinct to rule out A and C. While exact TM boundaries can have ±1-2 residue uncertainty in practice, the offered choices differ by 5 residues, well within the range where the proline and loop-composition arguments discriminate."
  },
  "important_caveats": [
    "The UniProt TM annotations use ECO:0000255 (similarity-based prediction), so they are computational predictions rather than experimentally determined boundaries. The exact residue-level boundaries could shift slightly with different prediction algorithms.",
    "The reviewer-only evidence confirms the sequence matches A3KQ86 (Plasmolipin, Danio rerio), but the evaluated model was not given the protein name or organism; the reasoning above relies only on the raw sequence and general biological knowledge.",
    "The third TM region (139..159: FFGIVETLLYTASSYFAYLGW) contains several polar residues (E, T, S, S, Y) and is the least hydrophobic of the four; a strict hydropathy threshold might question it, but all four answer choices include this segment, so it does not affect discrimination among options."
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
  "requested_accession": "A3KQ86",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "benchmark_sequence_sha256": "41896d53c37932e1e171f9fcec9cd1931289884cdd217d271fb4438225cae35a",
  "benchmark_sequence_length": 173,
  "current_status": "retrieved",
  "current_sequence_comparison": "matched",
  "current_entry_audit": {
    "entryVersion": 123,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2007-04-03",
    "sequenceVersion": 1
  },
  "current_uniprot_release": "2026_03",
  "current_record_sha256": "71db059b7d92b9cbb982c45261c2eacda70b05b9667017a735c6b72a71c6846e",
  "current_source_sequence_sha256": "41896d53c37932e1e171f9fcec9cd1931289884cdd217d271fb4438225cae35a",
  "current_source_sequence_length": 173,
  "historical_status": "retrieved",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "selected_historical_entry_version": 121,
  "selected_historical_version": {
    "accession": "A3KQ86",
    "database": "Swiss-Prot",
    "entryVersion": 121,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "PLLP_DANRE",
    "sequenceVersion": 1
  },
  "selected_historical_record_sha256": "a6866759886a22c2e64aae8941e7fe997c98c66a52079a88daaa7c18d3ddd601",
  "selected_historical_source_sequence_sha256": "41896d53c37932e1e171f9fcec9cd1931289884cdd217d271fb4438225cae35a",
  "selected_historical_source_sequence_length": 173,
  "latest_at_cutoff_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 121,
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A3KQ86.json)

```json
{
  "evidence_id": "C1",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A3KQ86.json",
  "source_sha256": "71db059b7d92b9cbb982c45261c2eacda70b05b9667017a735c6b72a71c6846e",
  "retrieved_utc": "2026-11-02T04:26:56.110007+00:00",
  "json_pointer": "/primaryAccession",
  "excerpt": "\"A3KQ86\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A3KQ86.json)

```json
{
  "evidence_id": "C2",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A3KQ86.json",
  "source_sha256": "71db059b7d92b9cbb982c45261c2eacda70b05b9667017a735c6b72a71c6846e",
  "retrieved_utc": "2026-11-02T04:26:56.110007+00:00",
  "json_pointer": "/entryAudit",
  "excerpt": "{\"entryVersion\":123,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2007-04-03\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A3KQ86.json)

```json
{
  "evidence_id": "C3",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A3KQ86.json",
  "source_sha256": "71db059b7d92b9cbb982c45261c2eacda70b05b9667017a735c6b72a71c6846e",
  "retrieved_utc": "2026-11-02T04:26:56.110007+00:00",
  "json_pointer": "/organism",
  "excerpt": "{\"commonName\":\"Zebrafish\",\"lineage\":[\"Eukaryota\",\"Metazoa\",\"Chordata\",\"Craniata\",\"Vertebrata\",\"Euteleostomi\",\"Actinopterygii\",\"Neopterygii\",\"Teleostei\",\"Ostariophysi\",\"Cypriniformes\",\"Danionidae\",\"Danioninae\",\"Danio\"],\"scientificName\":\"Danio rerio\",\"synonyms\":[\"Brachydanio rerio\"],\"taxonId\":7955}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A3KQ86.json)

```json
{
  "evidence_id": "C4",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A3KQ86.json",
  "source_sha256": "71db059b7d92b9cbb982c45261c2eacda70b05b9667017a735c6b72a71c6846e",
  "retrieved_utc": "2026-11-02T04:26:56.110007+00:00",
  "json_pointer": "/proteinDescription",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"value\":\"Plasma membrane proteolipid\"}}],\"recommendedName\":{\"fullName\":{\"value\":\"Plasmolipin\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A3KQ86.json)

```json
{
  "evidence_id": "C5",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A3KQ86.json",
  "source_sha256": "71db059b7d92b9cbb982c45261c2eacda70b05b9667017a735c6b72a71c6846e",
  "retrieved_utc": "2026-11-02T04:26:56.110007+00:00",
  "json_pointer": "/features/1",
  "excerpt": "{\"description\":\"Cytoplasmic\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":34},\"start\":{\"modifier\":\"EXACT\",\"value\":1}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A3KQ86.json)

```json
{
  "evidence_id": "C6",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A3KQ86.json",
  "source_sha256": "71db059b7d92b9cbb982c45261c2eacda70b05b9667017a735c6b72a71c6846e",
  "retrieved_utc": "2026-11-02T04:26:56.110007+00:00",
  "json_pointer": "/features/2",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":55},\"start\":{\"modifier\":\"EXACT\",\"value\":35}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A3KQ86.json)

```json
{
  "evidence_id": "C7",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A3KQ86.json",
  "source_sha256": "71db059b7d92b9cbb982c45261c2eacda70b05b9667017a735c6b72a71c6846e",
  "retrieved_utc": "2026-11-02T04:26:56.110007+00:00",
  "json_pointer": "/features/3",
  "excerpt": "{\"description\":\"Extracellular\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":67},\"start\":{\"modifier\":\"EXACT\",\"value\":56}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A3KQ86.json)

```json
{
  "evidence_id": "C8",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A3KQ86.json",
  "source_sha256": "71db059b7d92b9cbb982c45261c2eacda70b05b9667017a735c6b72a71c6846e",
  "retrieved_utc": "2026-11-02T04:26:56.110007+00:00",
  "json_pointer": "/features/4",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":88},\"start\":{\"modifier\":\"EXACT\",\"value\":68}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A3KQ86.json)

```json
{
  "evidence_id": "C9",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A3KQ86.json",
  "source_sha256": "71db059b7d92b9cbb982c45261c2eacda70b05b9667017a735c6b72a71c6846e",
  "retrieved_utc": "2026-11-02T04:26:56.110007+00:00",
  "json_pointer": "/features/5",
  "excerpt": "{\"description\":\"Cytoplasmic\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":98},\"start\":{\"modifier\":\"EXACT\",\"value\":89}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A3KQ86.json)

```json
{
  "evidence_id": "C10",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A3KQ86.json",
  "source_sha256": "71db059b7d92b9cbb982c45261c2eacda70b05b9667017a735c6b72a71c6846e",
  "retrieved_utc": "2026-11-02T04:26:56.110007+00:00",
  "json_pointer": "/features/6",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":119},\"start\":{\"modifier\":\"EXACT\",\"value\":99}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A3KQ86.json)

```json
{
  "evidence_id": "C11",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A3KQ86.json",
  "source_sha256": "71db059b7d92b9cbb982c45261c2eacda70b05b9667017a735c6b72a71c6846e",
  "retrieved_utc": "2026-11-02T04:26:56.110007+00:00",
  "json_pointer": "/features/7",
  "excerpt": "{\"description\":\"Extracellular\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":138},\"start\":{\"modifier\":\"EXACT\",\"value\":120}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A3KQ86.json)

```json
{
  "evidence_id": "C12",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A3KQ86.json",
  "source_sha256": "71db059b7d92b9cbb982c45261c2eacda70b05b9667017a735c6b72a71c6846e",
  "retrieved_utc": "2026-11-02T04:26:56.110007+00:00",
  "json_pointer": "/features/8",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":159},\"start\":{\"modifier\":\"EXACT\",\"value\":139}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C13

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A3KQ86.json)

```json
{
  "evidence_id": "C13",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A3KQ86.json",
  "source_sha256": "71db059b7d92b9cbb982c45261c2eacda70b05b9667017a735c6b72a71c6846e",
  "retrieved_utc": "2026-11-02T04:26:56.110007+00:00",
  "json_pointer": "/features/9",
  "excerpt": "{\"description\":\"Cytoplasmic\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":173},\"start\":{\"modifier\":\"EXACT\",\"value\":160}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A3KQ86?format=txt&versions=121)

```json
{
  "evidence_id": "H1",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A3KQ86?format=txt&versions=121",
  "source_sha256": "a6866759886a22c2e64aae8941e7fe997c98c66a52079a88daaa7c18d3ddd601",
  "retrieved_utc": "2026-11-02T04:26:58.657829+00:00",
  "source_locator": "lines 1-13",
  "excerpt": "ID   PLLP_DANRE              Reviewed;         173 AA.\nAC   A3KQ86; F6NKZ5;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   03-APR-2007, sequence version 1.\nDT   28-JAN-2026, entry version 121.\nDE   RecName: Full=Plasmolipin;\nDE   AltName: Full=Plasma membrane proteolipid;\nGN   Name=pllp; ORFNames=si:dkey-73n10.4;\nOS   Danio rerio (Zebrafish) (Brachydanio rerio).\nOC   Eukaryota; Metazoa; Chordata; Craniata; Vertebrata; Euteleostomi;\nOC   Actinopterygii; Neopterygii; Teleostei; Ostariophysi; Cypriniformes;\nOC   Danionidae; Danioninae; Danio.\nOX   NCBI_TaxID=7955;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 121,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A3KQ86?format=txt&versions=121)

```json
{
  "evidence_id": "H2",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A3KQ86?format=txt&versions=121",
  "source_sha256": "a6866759886a22c2e64aae8941e7fe997c98c66a52079a88daaa7c18d3ddd601",
  "retrieved_utc": "2026-11-02T04:26:58.657829+00:00",
  "source_locator": "lines 150-152",
  "excerpt": "FT   TOPO_DOM        1..34\nFT                   /note=\"Cytoplasmic\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 121,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A3KQ86?format=txt&versions=121)

```json
{
  "evidence_id": "H3",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A3KQ86?format=txt&versions=121",
  "source_sha256": "a6866759886a22c2e64aae8941e7fe997c98c66a52079a88daaa7c18d3ddd601",
  "retrieved_utc": "2026-11-02T04:26:58.657829+00:00",
  "source_locator": "lines 153-155",
  "excerpt": "FT   TRANSMEM        35..55\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 121,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A3KQ86?format=txt&versions=121)

```json
{
  "evidence_id": "H4",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A3KQ86?format=txt&versions=121",
  "source_sha256": "a6866759886a22c2e64aae8941e7fe997c98c66a52079a88daaa7c18d3ddd601",
  "retrieved_utc": "2026-11-02T04:26:58.657829+00:00",
  "source_locator": "lines 156-158",
  "excerpt": "FT   TOPO_DOM        56..67\nFT                   /note=\"Extracellular\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 121,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A3KQ86?format=txt&versions=121)

```json
{
  "evidence_id": "H5",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A3KQ86?format=txt&versions=121",
  "source_sha256": "a6866759886a22c2e64aae8941e7fe997c98c66a52079a88daaa7c18d3ddd601",
  "retrieved_utc": "2026-11-02T04:26:58.657829+00:00",
  "source_locator": "lines 159-161",
  "excerpt": "FT   TRANSMEM        68..88\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 121,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A3KQ86?format=txt&versions=121)

```json
{
  "evidence_id": "H6",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A3KQ86?format=txt&versions=121",
  "source_sha256": "a6866759886a22c2e64aae8941e7fe997c98c66a52079a88daaa7c18d3ddd601",
  "retrieved_utc": "2026-11-02T04:26:58.657829+00:00",
  "source_locator": "lines 162-164",
  "excerpt": "FT   TOPO_DOM        89..98\nFT                   /note=\"Cytoplasmic\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 121,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A3KQ86?format=txt&versions=121)

```json
{
  "evidence_id": "H7",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A3KQ86?format=txt&versions=121",
  "source_sha256": "a6866759886a22c2e64aae8941e7fe997c98c66a52079a88daaa7c18d3ddd601",
  "retrieved_utc": "2026-11-02T04:26:58.657829+00:00",
  "source_locator": "lines 165-167",
  "excerpt": "FT   TRANSMEM        99..119\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 121,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A3KQ86?format=txt&versions=121)

```json
{
  "evidence_id": "H8",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A3KQ86?format=txt&versions=121",
  "source_sha256": "a6866759886a22c2e64aae8941e7fe997c98c66a52079a88daaa7c18d3ddd601",
  "retrieved_utc": "2026-11-02T04:26:58.657829+00:00",
  "source_locator": "lines 168-170",
  "excerpt": "FT   TOPO_DOM        120..138\nFT                   /note=\"Extracellular\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 121,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A3KQ86?format=txt&versions=121)

```json
{
  "evidence_id": "H9",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A3KQ86?format=txt&versions=121",
  "source_sha256": "a6866759886a22c2e64aae8941e7fe997c98c66a52079a88daaa7c18d3ddd601",
  "retrieved_utc": "2026-11-02T04:26:58.657829+00:00",
  "source_locator": "lines 171-173",
  "excerpt": "FT   TRANSMEM        139..159\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 121,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H10

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A3KQ86?format=txt&versions=121)

```json
{
  "evidence_id": "H10",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A3KQ86?format=txt&versions=121",
  "source_sha256": "a6866759886a22c2e64aae8941e7fe997c98c66a52079a88daaa7c18d3ddd601",
  "retrieved_utc": "2026-11-02T04:26:58.657829+00:00",
  "source_locator": "lines 174-176",
  "excerpt": "FT   TOPO_DOM        160..173\nFT                   /note=\"Cytoplasmic\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 121,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json), zero-based source row 49. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
