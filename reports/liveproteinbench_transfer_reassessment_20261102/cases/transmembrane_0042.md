# transmembrane_0042: before and after transfer clarification

[All 1,328 cases](../README.md) · [Method](../METHOD.md) · [Summary](../SUMMARY.md) · [Exact reviewer user message](../inputs/transmembrane_0042.txt)

**Task:** `transmembrane`  
**Author key, unchanged:** **B** — 4..24

| Round | Reviewer | Key support | Transfer / lookup | Output usability (canonical status) |
|---|---|---|---|---|
| before | GPT-6 Luna | supported | lookup-dependent | usable output (valid_review) |
| before | Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | usable output (valid_review) |
| after | GPT-6 Luna | supported | lookup-dependent | usable output (valid_review) |
| after | Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | usable output (valid_review) |

**Usable output means format-valid review, not reasoning-supported or biologically correct.** A usable output can classify the question as reasoning-supported, lookup-dependent or uncertain. An output error is a problem with the saved model response; it does not count a defective benchmark question or wrong key. Each saved review is retained in full below. Labels from output errors are displayed as saved and excluded from label statistics. The author key and reviewer evidence were visible to reviewers; this is a review of answerability and key support, not a benchmark-solving score.

## Complete original question

```text
[Protein Sequence]
MEYLPYIATSIACIVILRWALNMMQWLWFEPRRLEKLLRKQGLQGNSYKFLFGDMKESSMLRNEALAKPMPMPFDNDYFPRINPFVDQLLNKYGMNCFLWMGPVPAIQIGEPELVREAFNRMHEFQKPKTNPLSALLATGLVSYEGDKWAKHRRLINPSFHVEKLKLMIPAFRESIVEVVNQWEKKVPENGSAEIDVWPSLTSLTGDVISRAAFGSVYGDGRRIFELLAVQKELVLSLLKFSYIPGYTYLPTEGNKKMKAVNNEIQRLLENVIQNRKKAMEAGEAAKDDLLGLLMDSNYKESMLEGGGKNKKLIMSFQDLIDECKLFFLAGHETTAVLLVWTLILLCKHQDWQTKAREEVLATFGMSEPTDYDALNRLKIVTMILNEVLRLYPPVVSTNRKLFKGETKLGNLVIPPGVGISLLTIQANRDPKVWGEDASEFRPDRFAEGLVKATKGNVAFFPFGWGPRICIGQNFALTESKMAVAMILQRFTFDLSPSYTHAPSGLITLNPQYGAPLMFRRR

[Multiple Choices]
A. 4..24; 440..463
B. 4..24
C. 27..47; 67..87; 100..120; 144..164; 202..222; 241..261; 274..294
D. 6..26
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

> The exact supplied sequence matches the UniProt entry, which annotates residues 4–24 as a helical transmembrane signal-anchor. The annotation carries computational evidence code ECO:0000255, so it supports the key as a database annotation, not as direct experimental confirmation.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The N-terminus contains a conspicuous hydrophobic stretch consistent with a membrane-spanning helix, distinguishing it from the many unrelated options in C and the extra proposed segment in A. But sequence inspection alone does not establish the precise boundary between the overlapping B and D ranges.


**Missing item-specific fact**

> The specific annotation or other protein-specific evidence assigning the helix boundaries to 4–24 rather than 6–26.


**Reason**

> General sequence reasoning supports an N-terminal membrane anchor, but the choices require distinguishing closely overlapping boundary assignments. That precision depends on an item-specific annotation or measurement absent from the input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "D"
]
```

> Both ranges lie within the same hydrophobic N-terminal stretch and could plausibly describe a membrane-spanning segment. The question provides no boundary convention or evidence that resolves the two-residue shift.


### Important caveats

- The database annotation is computationally evidenced, not identified here as experimentally measured.
- The reviewer-only sequence match and annotation support the expected answer but were not supplied to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminus contains a conspicuous hydrophobic stretch consistent with a membrane-spanning helix, distinguishing it from the many unrelated options in C and the extra proposed segment in A. But sequence inspection alone does not establish the precise boundary between the overlapping B and D ranges.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific annotation or other protein-specific evidence assigning the helix boundaries to 4–24 rather than 6–26.",
    "reason": "General sequence reasoning supports an N-terminal membrane anchor, but the choices require distinguishing closely overlapping boundary assignments. That precision depends on an item-specific annotation or measurement absent from the input."
  },
  "case_id": "transmembrane_0042",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The exact supplied sequence matches the UniProt entry, which annotates residues 4–24 as a helical transmembrane signal-anchor. The annotation carries computational evidence code ECO:0000255, so it supports the key as a database annotation, not as direct experimental confirmation."
  },
  "important_caveats": [
    "The database annotation is computationally evidenced, not identified here as experimentally measured.",
    "The reviewer-only sequence match and annotation support the expected answer but were not supplied to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "D"
    ],
    "reason": "Both ranges lie within the same hydrophobic N-terminal stretch and could plausibly describe a membrane-spanning segment. The question provides no boundary convention or evidence that resolves the two-residue shift."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0042",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact supplied sequence matches the UniProt entry, which annotates residues 4–24 as a helical transmembrane signal-anchor. The annotation carries computational evidence code ECO:0000255, so it supports the key as a database annotation, not as direct experimental confirmation.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The N-terminus contains a conspicuous hydrophobic stretch consistent with a membrane-spanning helix, distinguishing it from the many unrelated options in C and the extra proposed segment in A. But sequence inspection alone does not establish the precise boundary between the overlapping B and D ranges.",
    "missing_item_specific_fact": "The specific annotation or other protein-specific evidence assigning the helix boundaries to 4–24 rather than 6–26.",
    "reason": "General sequence reasoning supports an N-terminal membrane anchor, but the choices require distinguishing closely overlapping boundary assignments. That precision depends on an item-specific annotation or measurement absent from the input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "D"],
    "reason": "Both ranges lie within the same hydrophobic N-terminal stretch and could plausibly describe a membrane-spanning segment. The question provides no boundary convention or evidence that resolves the two-residue shift."
  },
  "important_caveats": [
    "The database annotation is computationally evidenced, not identified here as experimentally measured.",
    "The reviewer-only sequence match and annotation support the expected answer but were not supplied to the evaluated model."
  ]
}
```

</details>

## Before: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry A0AAW1J8D7 annotates a single transmembrane region at positions 4-24, described as 'Helical; Signal-anchor for type II membrane protein' (evidence code ECO:0000255, inferred by similarity). This is consistent with the protein being a Cytochrome P450 (Echinocystic acid 23-monooxygenase / CYP72A984), which is a well-characterized type II single-pass membrane protein. The N-terminal hydrophobic stretch LPYIATSIACIVILRWALNMM (residues 4-24) is the expected signal-anchor. The annotation is computational/curated (ECO:0000255) rather than experimentally measured, but it aligns with the established CYP450 membrane topology paradigm. Option A's additional TM at 440-463 would fall within the P450 catalytic domain (near the FGWGPRICIGQ heme-binding motif), which is cytoplasmic and not membrane-spanning. Option C's seven TM regions are incompatible with CYP450 topology.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3), [C4](#evidence-c4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains the canonical CYP450 heme-binding motif FxxGxRxCxG (visible as 'FGWGPRICIGQ' near position ~440), identifying the protein as a Cytochrome P450. CYP450s are well-established type II single-pass membrane proteins anchored by a single N-terminal signal-anchor helix, which immediately eliminates option C (seven TM regions, a multi-pass topology) and option A (a second TM within the soluble catalytic domain). The N-terminal hydrophobic stretch LPYIATSIACIVILRWALNMM (positions 4-24) is the expected signal-anchor. Distinguishing B (4-24) from D (6-26): the TM helix should initiate at a hydrophobic residue (L4) rather than an aromatic (Y6); aromatic residues like Y are typically at membrane-water interfaces at helix termini, not at the start of the hydrophobic core. Starting at L4 with a P5 (helix-breaking, common at TM boundaries) is more standard than starting at Y6.


**Missing item-specific fact**

> None strictly required. The exact 2-residue boundary between B and D is somewhat fine-grained, but the biological preference for hydrophobic (L) over aromatic (Y) initiation of a TM helix provides a defensible argument. The primary discrimination (eliminating A and C) relies on general CYP450 topology knowledge.


**Reason**

> A model with general biological knowledge can: (1) recognize the CYP450 heme motif to identify the protein family, (2) apply the well-known type II single-pass topology of CYP450s to eliminate multi-pass (C) and dual-TM (A) options, and (3) analyze the N-terminal hydrophobic stretch to prefer position 4 (L, hydrophobic core start) over position 6 (Y, aromatic interface residue) as the TM helix boundary. The B-vs-D distinction is the weakest link but is supported by helix-boundary biochemistry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options A and C are clearly eliminated by CYP450 topology (single N-terminal TM anchor, no TM in catalytic domain). Option D (6-26) is a close positional variant of B but is less defensible because it begins the TM helix at an aromatic tyrosine (Y6) rather than the hydrophobic leucine (L4), which contradicts the typical pattern where aromatics cap helix ends at membrane interfaces. The question asks for 'a segment' (singular), consistent with the single-TM CYP450 topology.


### Important caveats

- The UniProt TM annotation uses evidence code ECO:0000255 (inferred by similarity), meaning it is a computational/curated prediction rather than direct experimental measurement of the membrane-spanning region.
- The B-vs-D distinction (4-24 vs 6-26) is a 2-residue shift; while biological reasoning favors B, the boundary between signal-anchor helix start and the N-terminal flanking residues can vary by 1-2 residues in different prediction tools.
- The protein is from Saponaria officinalis (common soapwort), a plant CYP450; its membrane topology follows the conserved eukaryotic CYP450 paradigm.
- The reviewer-only UniProt accession was inferred from dataset metadata and was not provided to the evaluated model; the model must rely solely on sequence analysis.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains the canonical CYP450 heme-binding motif FxxGxRxCxG (visible as 'FGWGPRICIGQ' near position ~440), identifying the protein as a Cytochrome P450. CYP450s are well-established type II single-pass membrane proteins anchored by a single N-terminal signal-anchor helix, which immediately eliminates option C (seven TM regions, a multi-pass topology) and option A (a second TM within the soluble catalytic domain). The N-terminal hydrophobic stretch LPYIATSIACIVILRWALNMM (positions 4-24) is the expected signal-anchor. Distinguishing B (4-24) from D (6-26): the TM helix should initiate at a hydrophobic residue (L4) rather than an aromatic (Y6); aromatic residues like Y are typically at membrane-water interfaces at helix termini, not at the start of the hydrophobic core. Starting at L4 with a P5 (helix-breaking, common at TM boundaries) is more standard than starting at Y6.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None strictly required. The exact 2-residue boundary between B and D is somewhat fine-grained, but the biological preference for hydrophobic (L) over aromatic (Y) initiation of a TM helix provides a defensible argument. The primary discrimination (eliminating A and C) relies on general CYP450 topology knowledge.",
    "reason": "A model with general biological knowledge can: (1) recognize the CYP450 heme motif to identify the protein family, (2) apply the well-known type II single-pass topology of CYP450s to eliminate multi-pass (C) and dual-TM (A) options, and (3) analyze the N-terminal hydrophobic stretch to prefer position 4 (L, hydrophobic core start) over position 6 (Y, aromatic interface residue) as the TM helix boundary. The B-vs-D distinction is the weakest link but is supported by helix-boundary biochemistry."
  },
  "case_id": "transmembrane_0042",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3",
      "C4"
    ],
    "judgment": "supported",
    "reason": "UniProt entry A0AAW1J8D7 annotates a single transmembrane region at positions 4-24, described as 'Helical; Signal-anchor for type II membrane protein' (evidence code ECO:0000255, inferred by similarity). This is consistent with the protein being a Cytochrome P450 (Echinocystic acid 23-monooxygenase / CYP72A984), which is a well-characterized type II single-pass membrane protein. The N-terminal hydrophobic stretch LPYIATSIACIVILRWALNMM (residues 4-24) is the expected signal-anchor. The annotation is computational/curated (ECO:0000255) rather than experimentally measured, but it aligns with the established CYP450 membrane topology paradigm. Option A's additional TM at 440-463 would fall within the P450 catalytic domain (near the FGWGPRICIGQ heme-binding motif), which is cytoplasmic and not membrane-spanning. Option C's seven TM regions are incompatible with CYP450 topology."
  },
  "important_caveats": [
    "The UniProt TM annotation uses evidence code ECO:0000255 (inferred by similarity), meaning it is a computational/curated prediction rather than direct experimental measurement of the membrane-spanning region.",
    "The B-vs-D distinction (4-24 vs 6-26) is a 2-residue shift; while biological reasoning favors B, the boundary between signal-anchor helix start and the N-terminal flanking residues can vary by 1-2 residues in different prediction tools.",
    "The protein is from Saponaria officinalis (common soapwort), a plant CYP450; its membrane topology follows the conserved eukaryotic CYP450 paradigm.",
    "The reviewer-only UniProt accession was inferred from dataset metadata and was not provided to the evaluated model; the model must rely solely on sequence analysis."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A and C are clearly eliminated by CYP450 topology (single N-terminal TM anchor, no TM in catalytic domain). Option D (6-26) is a close positional variant of B but is less defensible because it begins the TM helix at an aromatic tyrosine (Y6) rather than the hydrophobic leucine (L4), which contradicts the typical pattern where aromatics cap helix ends at membrane interfaces. The question asks for 'a segment' (singular), consistent with the single-TM CYP450 topology."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0042",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry A0AAW1J8D7 annotates a single transmembrane region at positions 4-24, described as 'Helical; Signal-anchor for type II membrane protein' (evidence code ECO:0000255, inferred by similarity). This is consistent with the protein being a Cytochrome P450 (Echinocystic acid 23-monooxygenase / CYP72A984), which is a well-characterized type II single-pass membrane protein. The N-terminal hydrophobic stretch LPYIATSIACIVILRWALNMM (residues 4-24) is the expected signal-anchor. The annotation is computational/curated (ECO:0000255) rather than experimentally measured, but it aligns with the established CYP450 membrane topology paradigm. Option A's additional TM at 440-463 would fall within the P450 catalytic domain (near the FGWGPRICIGQ heme-binding motif), which is cytoplasmic and not membrane-spanning. Option C's seven TM regions are incompatible with CYP450 topology.",
    "evidence_ids": ["C5", "H3", "C4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains the canonical CYP450 heme-binding motif FxxGxRxCxG (visible as 'FGWGPRICIGQ' near position ~440), identifying the protein as a Cytochrome P450. CYP450s are well-established type II single-pass membrane proteins anchored by a single N-terminal signal-anchor helix, which immediately eliminates option C (seven TM regions, a multi-pass topology) and option A (a second TM within the soluble catalytic domain). The N-terminal hydrophobic stretch LPYIATSIACIVILRWALNMM (positions 4-24) is the expected signal-anchor. Distinguishing B (4-24) from D (6-26): the TM helix should initiate at a hydrophobic residue (L4) rather than an aromatic (Y6); aromatic residues like Y are typically at membrane-water interfaces at helix termini, not at the start of the hydrophobic core. Starting at L4 with a P5 (helix-breaking, common at TM boundaries) is more standard than starting at Y6.",
    "missing_item_specific_fact": "None strictly required. The exact 2-residue boundary between B and D is somewhat fine-grained, but the biological preference for hydrophobic (L) over aromatic (Y) initiation of a TM helix provides a defensible argument. The primary discrimination (eliminating A and C) relies on general CYP450 topology knowledge.",
    "reason": "A model with general biological knowledge can: (1) recognize the CYP450 heme motif to identify the protein family, (2) apply the well-known type II single-pass topology of CYP450s to eliminate multi-pass (C) and dual-TM (A) options, and (3) analyze the N-terminal hydrophobic stretch to prefer position 4 (L, hydrophobic core start) over position 6 (Y, aromatic interface residue) as the TM helix boundary. The B-vs-D distinction is the weakest link but is supported by helix-boundary biochemistry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A and C are clearly eliminated by CYP450 topology (single N-terminal TM anchor, no TM in catalytic domain). Option D (6-26) is a close positional variant of B but is less defensible because it begins the TM helix at an aromatic tyrosine (Y6) rather than the hydrophobic leucine (L4), which contradicts the typical pattern where aromatics cap helix ends at membrane interfaces. The question asks for 'a segment' (singular), consistent with the single-TM CYP450 topology."
  },
  "important_caveats": [
    "The UniProt TM annotation uses evidence code ECO:0000255 (inferred by similarity), meaning it is a computational/curated prediction rather than direct experimental measurement of the membrane-spanning region.",
    "The B-vs-D distinction (4-24 vs 6-26) is a 2-residue shift; while biological reasoning favors B, the boundary between signal-anchor helix start and the N-terminal flanking residues can vary by 1-2 residues in different prediction tools.",
    "The protein is from Saponaria officinalis (common soapwort), a plant CYP450; its membrane topology follows the conserved eukaryotic CYP450 paradigm.",
    "The reviewer-only UniProt accession was inferred from dataset metadata and was not provided to the evaluated model; the model must rely solely on sequence analysis."
  ]
}
```

</details>

## After: GPT-6 Luna

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence-matched UniProt record annotates residues 4–24 as a helical transmembrane signal-anchor. This is computational annotation rather than direct experimental evidence, but it supports the keyed answer.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The strongly hydrophobic N-terminal stretch supports a membrane-spanning anchor, and the sequence is consistent with a cytochrome P450, for which an N-terminal anchor is a plausible transferable family-level inference. That can distinguish this region from the many proposed spans in C and the additional span in A, but it does not meaningfully distinguish B from D: both cover the same hydrophobic stretch.


**Missing item-specific fact**

> The exact boundary assignment for this sequence—4..24 rather than the overlapping 6..26—would be needed to select B over D.


**Reason**

> Transferable sequence and family knowledge supports an N-terminal membrane anchor, but the offered choices B and D differ only by a small boundary shift across that same region. The input does not establish which precise endpoints to use.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "D"
]
```

> Both intervals span the same strongly hydrophobic N-terminal segment; the sequence alone does not clearly resolve their slightly different endpoints.


### Important caveats

- The supporting annotation is computational, not direct experimental confirmation.
- The reviewer-only source evidence was not part of the original input and is used only to assess the key.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The strongly hydrophobic N-terminal stretch supports a membrane-spanning anchor, and the sequence is consistent with a cytochrome P450, for which an N-terminal anchor is a plausible transferable family-level inference. That can distinguish this region from the many proposed spans in C and the additional span in A, but it does not meaningfully distinguish B from D: both cover the same hydrophobic stretch.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The exact boundary assignment for this sequence—4..24 rather than the overlapping 6..26—would be needed to select B over D.",
    "reason": "Transferable sequence and family knowledge supports an N-terminal membrane anchor, but the offered choices B and D differ only by a small boundary shift across that same region. The input does not establish which precise endpoints to use."
  },
  "case_id": "transmembrane_0042",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates residues 4–24 as a helical transmembrane signal-anchor. This is computational annotation rather than direct experimental evidence, but it supports the keyed answer."
  },
  "important_caveats": [
    "The supporting annotation is computational, not direct experimental confirmation.",
    "The reviewer-only source evidence was not part of the original input and is used only to assess the key."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "D"
    ],
    "reason": "Both intervals span the same strongly hydrophobic N-terminal segment; the sequence alone does not clearly resolve their slightly different endpoints."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0042",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates residues 4–24 as a helical transmembrane signal-anchor. This is computational annotation rather than direct experimental evidence, but it supports the keyed answer.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The strongly hydrophobic N-terminal stretch supports a membrane-spanning anchor, and the sequence is consistent with a cytochrome P450, for which an N-terminal anchor is a plausible transferable family-level inference. That can distinguish this region from the many proposed spans in C and the additional span in A, but it does not meaningfully distinguish B from D: both cover the same hydrophobic stretch.",
    "missing_item_specific_fact": "The exact boundary assignment for this sequence—4..24 rather than the overlapping 6..26—would be needed to select B over D.",
    "reason": "Transferable sequence and family knowledge supports an N-terminal membrane anchor, but the offered choices B and D differ only by a small boundary shift across that same region. The input does not establish which precise endpoints to use."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "D"],
    "reason": "Both intervals span the same strongly hydrophobic N-terminal segment; the sequence alone does not clearly resolve their slightly different endpoints."
  },
  "important_caveats": [
    "The supporting annotation is computational, not direct experimental confirmation.",
    "The reviewer-only source evidence was not part of the original input and is used only to assess the key."
  ]
}
```

</details>

## After: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A0AAW1J8D7 annotates a single transmembrane helix at positions 4..24, described as 'Helical; Signal-anchor for type II membrane protein' (evidence code ECO:0000255, inferred by similarity). The expected answer B (4..24) matches this annotation exactly. The sequence at positions 4-24 (LPYIATSIACIVILRWALNMM) is a predominantly hydrophobic stretch consistent with a single-pass TM anchor, and the protein is a plant cytochrome P450 (heme-binding motif FGWGPRICIG visible near position 460), a family well-known for type II membrane topology. The annotation is computational/similarity-based, which is standard for TM predictions.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains the canonical P450 heme-binding motif FGWGPRICIG (~positions 460-470), identifying this as a cytochrome P450. Plant CYP450s are well-established single-pass type II membrane proteins anchored by a single N-terminal transmembrane helix, with a large soluble catalytic domain—this family-level knowledge eliminates option C (7 TM helices) and option A (a second TM at 440-463 within the catalytic domain). The N-terminal region shows a clear hydrophobic core: positions 1-3 are M-E-Y (E is charged, breaking hydrophobicity), then L(4) through M(24) form a hydrophobic stretch (L, I, A, I, V, I, L, W, A, L, M, M dominate), and Q(25) is a clearly polar residue that terminates the hydrophobic core. This hydrophobicity profile supports boundaries of 4..24 (option B) over 6..26 (option D): starting at 6 would arbitrarily exclude the clearly hydrophobic L(4), and ending at 26 would include the polar Q(25) within the TM segment. The aromatic W at position 26 is more consistent with a membrane-interface residue outside the TM helix.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The combination of P450 family topology knowledge (single-pass type II membrane protein) and straightforward hydrophobicity analysis of the N-terminal sequence provides a credible, transferable basis for selecting B over the other options. The B-vs-D distinction, while subtle, is addressed by the charged E at position 2 and polar Q at position 25 flanking the hydrophobic core, which a model examining the sequence can observe.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Although B and D differ by only two positions, the hydrophobicity profile (charged E at position 2, hydrophobic L at position 4, polar Q at position 25) provides a reasonable basis to prefer 4..24 over 6..26. Options A and C are clearly inconsistent with P450 single-pass membrane topology.


### Important caveats

- The UniProt annotation uses evidence code ECO:0000255 (inferred by similarity), meaning the TM assignment is computational rather than experimentally validated.
- The B-vs-D boundary distinction (4..24 vs 6..26) is subtle and relies on hydrophobicity interpretation; different TM-prediction algorithms might yield slightly different boundaries.
- The reviewer-only evidence confirms the sequence matches the UniProt entry exactly (SHA-256 match, 522 residues), but the accession and organism identity were not provided to the evaluated model.
- The protein is annotated as Echinocystic acid 23-monooxygenase (CYP72A984) from Saponaria officinalis, but this identity was not part of the original question input.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains the canonical P450 heme-binding motif FGWGPRICIG (~positions 460-470), identifying this as a cytochrome P450. Plant CYP450s are well-established single-pass type II membrane proteins anchored by a single N-terminal transmembrane helix, with a large soluble catalytic domain—this family-level knowledge eliminates option C (7 TM helices) and option A (a second TM at 440-463 within the catalytic domain). The N-terminal region shows a clear hydrophobic core: positions 1-3 are M-E-Y (E is charged, breaking hydrophobicity), then L(4) through M(24) form a hydrophobic stretch (L, I, A, I, V, I, L, W, A, L, M, M dominate), and Q(25) is a clearly polar residue that terminates the hydrophobic core. This hydrophobicity profile supports boundaries of 4..24 (option B) over 6..26 (option D): starting at 6 would arbitrarily exclude the clearly hydrophobic L(4), and ending at 26 would include the polar Q(25) within the TM segment. The aromatic W at position 26 is more consistent with a membrane-interface residue outside the TM helix.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The combination of P450 family topology knowledge (single-pass type II membrane protein) and straightforward hydrophobicity analysis of the N-terminal sequence provides a credible, transferable basis for selecting B over the other options. The B-vs-D distinction, while subtle, is addressed by the charged E at position 2 and polar Q at position 25 flanking the hydrophobic core, which a model examining the sequence can observe."
  },
  "case_id": "transmembrane_0042",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry A0AAW1J8D7 annotates a single transmembrane helix at positions 4..24, described as 'Helical; Signal-anchor for type II membrane protein' (evidence code ECO:0000255, inferred by similarity). The expected answer B (4..24) matches this annotation exactly. The sequence at positions 4-24 (LPYIATSIACIVILRWALNMM) is a predominantly hydrophobic stretch consistent with a single-pass TM anchor, and the protein is a plant cytochrome P450 (heme-binding motif FGWGPRICIG visible near position 460), a family well-known for type II membrane topology. The annotation is computational/similarity-based, which is standard for TM predictions."
  },
  "important_caveats": [
    "The UniProt annotation uses evidence code ECO:0000255 (inferred by similarity), meaning the TM assignment is computational rather than experimentally validated.",
    "The B-vs-D boundary distinction (4..24 vs 6..26) is subtle and relies on hydrophobicity interpretation; different TM-prediction algorithms might yield slightly different boundaries.",
    "The reviewer-only evidence confirms the sequence matches the UniProt entry exactly (SHA-256 match, 522 residues), but the accession and organism identity were not provided to the evaluated model.",
    "The protein is annotated as Echinocystic acid 23-monooxygenase (CYP72A984) from Saponaria officinalis, but this identity was not part of the original question input."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although B and D differ by only two positions, the hydrophobicity profile (charged E at position 2, hydrophobic L at position 4, polar Q at position 25) provides a reasonable basis to prefer 4..24 over 6..26. Options A and C are clearly inconsistent with P450 single-pass membrane topology."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0042",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A0AAW1J8D7 annotates a single transmembrane helix at positions 4..24, described as 'Helical; Signal-anchor for type II membrane protein' (evidence code ECO:0000255, inferred by similarity). The expected answer B (4..24) matches this annotation exactly. The sequence at positions 4-24 (LPYIATSIACIVILRWALNMM) is a predominantly hydrophobic stretch consistent with a single-pass TM anchor, and the protein is a plant cytochrome P450 (heme-binding motif FGWGPRICIG visible near position 460), a family well-known for type II membrane topology. The annotation is computational/similarity-based, which is standard for TM predictions.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains the canonical P450 heme-binding motif FGWGPRICIG (~positions 460-470), identifying this as a cytochrome P450. Plant CYP450s are well-established single-pass type II membrane proteins anchored by a single N-terminal transmembrane helix, with a large soluble catalytic domain—this family-level knowledge eliminates option C (7 TM helices) and option A (a second TM at 440-463 within the catalytic domain). The N-terminal region shows a clear hydrophobic core: positions 1-3 are M-E-Y (E is charged, breaking hydrophobicity), then L(4) through M(24) form a hydrophobic stretch (L, I, A, I, V, I, L, W, A, L, M, M dominate), and Q(25) is a clearly polar residue that terminates the hydrophobic core. This hydrophobicity profile supports boundaries of 4..24 (option B) over 6..26 (option D): starting at 6 would arbitrarily exclude the clearly hydrophobic L(4), and ending at 26 would include the polar Q(25) within the TM segment. The aromatic W at position 26 is more consistent with a membrane-interface residue outside the TM helix.",
    "missing_item_specific_fact": "",
    "reason": "The combination of P450 family topology knowledge (single-pass type II membrane protein) and straightforward hydrophobicity analysis of the N-terminal sequence provides a credible, transferable basis for selecting B over the other options. The B-vs-D distinction, while subtle, is addressed by the charged E at position 2 and polar Q at position 25 flanking the hydrophobic core, which a model examining the sequence can observe."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although B and D differ by only two positions, the hydrophobicity profile (charged E at position 2, hydrophobic L at position 4, polar Q at position 25) provides a reasonable basis to prefer 4..24 over 6..26. Options A and C are clearly inconsistent with P450 single-pass membrane topology."
  },
  "important_caveats": [
    "The UniProt annotation uses evidence code ECO:0000255 (inferred by similarity), meaning the TM assignment is computational rather than experimentally validated.",
    "The B-vs-D boundary distinction (4..24 vs 6..26) is subtle and relies on hydrophobicity interpretation; different TM-prediction algorithms might yield slightly different boundaries.",
    "The reviewer-only evidence confirms the sequence matches the UniProt entry exactly (SHA-256 match, 522 residues), but the accession and organism identity were not provided to the evaluated model.",
    "The protein is annotated as Echinocystic acid 23-monooxygenase (CYP72A984) from Saponaria officinalis, but this identity was not part of the original question input."
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
  "requested_accession": "A0AAW1J8D7",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "benchmark_sequence_sha256": "f866185e1e103357a9c3b20604b1a1695cd77c611aad66a57021597b19150016",
  "benchmark_sequence_length": 522,
  "current_status": "retrieved",
  "current_sequence_comparison": "matched",
  "current_entry_audit": {
    "entryVersion": 6,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-06-10",
    "lastSequenceUpdateDate": "2024-11-27",
    "sequenceVersion": 1
  },
  "current_uniprot_release": "2026_03",
  "current_record_sha256": "622ab455e7c549299e06dff7e6ac0d6d5fd4950316e1f887c806b70e5464ab02",
  "current_source_sequence_sha256": "f866185e1e103357a9c3b20604b1a1695cd77c611aad66a57021597b19150016",
  "current_source_sequence_length": 522,
  "historical_status": "retrieved",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "selected_historical_entry_version": 5,
  "selected_historical_version": {
    "accession": "A0AAW1J8D7",
    "database": "Swiss-Prot",
    "entryVersion": 5,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "C7284_SAPOF",
    "sequenceVersion": 1
  },
  "selected_historical_record_sha256": "813ea7e8b060f5cf01f9f7baef81348aef78766a60262229bbc2dd6f2ea2a48e",
  "selected_historical_source_sequence_sha256": "f866185e1e103357a9c3b20604b1a1695cd77c611aad66a57021597b19150016",
  "selected_historical_source_sequence_length": 522,
  "latest_at_cutoff_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 5,
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1J8D7.json)

```json
{
  "evidence_id": "C1",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAW1J8D7.json",
  "source_sha256": "622ab455e7c549299e06dff7e6ac0d6d5fd4950316e1f887c806b70e5464ab02",
  "retrieved_utc": "2026-11-02T04:26:33.543251+00:00",
  "json_pointer": "/primaryAccession",
  "excerpt": "\"A0AAW1J8D7\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1J8D7.json)

```json
{
  "evidence_id": "C2",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAW1J8D7.json",
  "source_sha256": "622ab455e7c549299e06dff7e6ac0d6d5fd4950316e1f887c806b70e5464ab02",
  "retrieved_utc": "2026-11-02T04:26:33.543251+00:00",
  "json_pointer": "/entryAudit",
  "excerpt": "{\"entryVersion\":6,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-06-10\",\"lastSequenceUpdateDate\":\"2024-11-27\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1J8D7.json)

```json
{
  "evidence_id": "C3",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAW1J8D7.json",
  "source_sha256": "622ab455e7c549299e06dff7e6ac0d6d5fd4950316e1f887c806b70e5464ab02",
  "retrieved_utc": "2026-11-02T04:26:33.543251+00:00",
  "json_pointer": "/organism",
  "excerpt": "{\"commonName\":\"Common soapwort\",\"lineage\":[\"Eukaryota\",\"Viridiplantae\",\"Streptophyta\",\"Embryophyta\",\"Tracheophyta\",\"Spermatophyta\",\"Magnoliopsida\",\"eudicotyledons\",\"Gunneridae\",\"Pentapetalae\",\"Caryophyllales\",\"Caryophyllaceae\",\"Caryophylleae\",\"Saponaria\"],\"scientificName\":\"Saponaria officinalis\",\"synonyms\":[\"Lychnis saponaria\"],\"taxonId\":3572}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1J8D7.json)

```json
{
  "evidence_id": "C4",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAW1J8D7.json",
  "source_sha256": "622ab455e7c549299e06dff7e6ac0d6d5fd4950316e1f887c806b70e5464ab02",
  "retrieved_utc": "2026-11-02T04:26:33.543251+00:00",
  "json_pointer": "/proteinDescription",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39043959\",\"source\":\"PubMed\"}],\"value\":\"Cytochrome P450 72A984\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39043959\",\"source\":\"PubMed\"}],\"value\":\"SoCYP72A984\"}]}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39043959\",\"source\":\"PubMed\"}],\"value\":\"1.14.14.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Echinocystic acid 23-monooxygenase\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1J8D7.json)

```json
{
  "evidence_id": "C5",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAW1J8D7.json",
  "source_sha256": "622ab455e7c549299e06dff7e6ac0d6d5fd4950316e1f887c806b70e5464ab02",
  "retrieved_utc": "2026-11-02T04:26:33.543251+00:00",
  "json_pointer": "/features/1",
  "excerpt": "{\"description\":\"Helical; Signal-anchor for type II membrane protein\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":24},\"start\":{\"modifier\":\"EXACT\",\"value\":4}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1J8D7.json)

```json
{
  "evidence_id": "C6",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAW1J8D7.json",
  "source_sha256": "622ab455e7c549299e06dff7e6ac0d6d5fd4950316e1f887c806b70e5464ab02",
  "retrieved_utc": "2026-11-02T04:26:33.543251+00:00",
  "json_pointer": "/references/0",
  "excerpt": "{\"citation\":{\"authors\":[\"Jo S.\",\"El-Demerdash A.\",\"Owen C.\",\"Srivastava V.\",\"Wu D.\",\"Kikuchi S.\",\"Reed J.\",\"Hodgson H.\",\"Harkess A.\",\"Shu S.\",\"Plott C.\",\"Jenkins J.\",\"Williams M.\",\"Boston L.-B.\",\"Lacchini E.\",\"Qu T.\",\"Goossens A.\",\"Grimwood J.\",\"Schmutz J.\",\"Leebens-Mack J.\",\"Osbourn A.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"39043959\"},{\"database\":\"DOI\",\"id\":\"10.1038/s41589-024-01681-7\"}],\"citationType\":\"journal article\",\"firstPage\":\"215\",\"id\":\"39043959\",\"journal\":\"Nat. Chem. Biol.\",\"lastPage\":\"226\",\"publicationDate\":\"2025\",\"title\":\"Unlocking saponin biosynthesis in soapwort.\",\"volume\":\"21\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"WWM48154.1\",\"source\":\"EMBL\"}],\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [MRNA]\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"TISSUE SPECIFICITY\",\"PATHWAY\",\"BIOTECHNOLOGY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAW1J8D7?format=txt&versions=5)

```json
{
  "evidence_id": "H1",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0AAW1J8D7?format=txt&versions=5",
  "source_sha256": "813ea7e8b060f5cf01f9f7baef81348aef78766a60262229bbc2dd6f2ea2a48e",
  "retrieved_utc": "2026-11-02T04:26:35.528947+00:00",
  "source_locator": "lines 1-17",
  "excerpt": "ID   C7284_SAPOF             Reviewed;         522 AA.\nAC   A0AAW1J8D7;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   27-NOV-2024, sequence version 1.\nDT   28-JAN-2026, entry version 5.\nDE   RecName: Full=Echinocystic acid 23-monooxygenase {ECO:0000305};\nDE            EC=1.14.14.- {ECO:0000269|PubMed:39043959};\nDE   AltName: Full=Cytochrome P450 72A984 {ECO:0000303|PubMed:39043959};\nDE            Short=SoCYP72A984 {ECO:0000303|PubMed:39043959};\nGN   Name=CYP72A984 {ECO:0000303|PubMed:39043959};\nGN   Synonyms=Saoffv11042705m {ECO:0000303|PubMed:39043959};\nGN   ORFNames=RND81_08G155300 {ECO:0000312|EMBL:KAK9699133.1};\nOS   Saponaria officinalis (Common soapwort) (Lychnis saponaria).\nOC   Eukaryota; Viridiplantae; Streptophyta; Embryophyta; Tracheophyta;\nOC   Spermatophyta; Magnoliopsida; eudicotyledons; Gunneridae; Pentapetalae;\nOC   Caryophyllales; Caryophyllaceae; Caryophylleae; Saponaria.\nOX   NCBI_TaxID=3572;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 5,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAW1J8D7?format=txt&versions=5)

```json
{
  "evidence_id": "H2",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0AAW1J8D7?format=txt&versions=5",
  "source_sha256": "813ea7e8b060f5cf01f9f7baef81348aef78766a60262229bbc2dd6f2ea2a48e",
  "retrieved_utc": "2026-11-02T04:26:35.528947+00:00",
  "source_locator": "lines 18-27",
  "excerpt": "RN   [1] {ECO:0000312|EMBL:WWM48154.1}\nRP   NUCLEOTIDE SEQUENCE [MRNA], FUNCTION, CATALYTIC ACTIVITY, TISSUE\nRP   SPECIFICITY, PATHWAY, AND BIOTECHNOLOGY.\nRX   PubMed=39043959; DOI=10.1038/s41589-024-01681-7;\nRA   Jo S., El-Demerdash A., Owen C., Srivastava V., Wu D., Kikuchi S., Reed J.,\nRA   Hodgson H., Harkess A., Shu S., Plott C., Jenkins J., Williams M.,\nRA   Boston L.-B., Lacchini E., Qu T., Goossens A., Grimwood J., Schmutz J.,\nRA   Leebens-Mack J., Osbourn A.;\nRT   \"Unlocking saponin biosynthesis in soapwort.\";\nRL   Nat. Chem. Biol. 21:215-226(2025).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 5,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAW1J8D7?format=txt&versions=5)

```json
{
  "evidence_id": "H3",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0AAW1J8D7?format=txt&versions=5",
  "source_sha256": "813ea7e8b060f5cf01f9f7baef81348aef78766a60262229bbc2dd6f2ea2a48e",
  "retrieved_utc": "2026-11-02T04:26:35.528947+00:00",
  "source_locator": "lines 104-106",
  "excerpt": "FT   TRANSMEM        4..24\nFT                   /note=\"Helical; Signal-anchor for type II membrane protein\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 5,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json), zero-based source row 42. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
