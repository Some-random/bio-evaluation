# transmembrane_0119: before and after transfer clarification

[All 1,328 cases](../README.md) · [Method](../METHOD.md) · [Summary](../SUMMARY.md) · [Exact reviewer user message](../inputs/transmembrane_0119.txt)

**Task:** `transmembrane`  
**Author key, unchanged:** **B** — 483..503

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
MKAFPVICLGFAIFSSSICVNINILQQIGYIKQQVWQLSYYSQSSSSYVVVKLLPNIQPTDNSCEFKSVTQYNKTLSNLLLPIAENINNIASPSPGSRRHKRFAGIAIGIAALGVATAAQVTAAVSLVQAQTNARAIAAMKNSIQATNRAVFEVKEGTQQLAIAVQAIQDHINTIMNTQLNNMSCQILDNQLATSLGLYLTELTTVFQPQLINPALSPISIQALRSLLGSMTPAVVQATLSTSISAAEILSAGLMEGQIVSVLLDEMQMIVKINIPTIVTQSNALVIDFHSISSFINNQESIIQLPDRILEIGNEQWRYPAKNCKLTRHHIFCQYNEAERLSLETKLCLAGNISACVFSPIAGSYMRRFVALDGTIVANCRSLTCLCKSPSYPIYQPDHHAVTTIDLTSCQTLSLDGLDFSIVSLSNITYAENLTISLSQTINTQPIDISTELSKVNASLQNAVKYIKESNHQLQSVSVSSKIGAIIVAALVLSILSIIISLLFCCWAYIATKEIRRINFKTNHINTISSSVDDLIRY

[Multiple Choices]
A. 39..59; 94..114; 117..137; 148..168; 177..197; 217..237; 365..385; 405..425; 433..453; 461..481; 488..508; 528..548
B. 483..503
C. 483..507
D. 483..503; 558..583
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

> The sequence exactly matches the UniProt record, whose transmembrane annotation is 483..503. The annotation carries evidence code ECO:0000255, indicating computational support rather than a reported experimental measurement.

Citations as saved: [C5](#evidence-c5), [H2](#evidence-h2).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence contains a strong hydrophobic C-terminal stretch, which supports a membrane-spanning helix in this region and disfavors choices listing many unrelated segments. It does not establish the precise endpoint.


**Missing item-specific fact**

> The specific 483..503 boundary used by the protein's database annotation is absent from the input; distinguishing that boundary from 483..507 requires an item-specific annotation or other evidence.


**Reason**

> Sequence reasoning can locate the likely membrane anchor, but both B and C overlap the hydrophobic stretch. General membrane biology alone does not resolve their four-residue endpoint difference.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "C"
]
```

> Both intervals cover the strongly hydrophobic segment beginning at 483. The additional residues in C remain hydrophobic/aromatic, so the sequence alone does not make the precise boundary between B and C unambiguous.


### Important caveats

- The supporting annotation is computational, not direct experimental evidence.
- The reviewer-only source record matches the supplied sequence, including in the historical record checked; the author's exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a strong hydrophobic C-terminal stretch, which supports a membrane-spanning helix in this region and disfavors choices listing many unrelated segments. It does not establish the precise endpoint.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific 483..503 boundary used by the protein's database annotation is absent from the input; distinguishing that boundary from 483..507 requires an item-specific annotation or other evidence.",
    "reason": "Sequence reasoning can locate the likely membrane anchor, but both B and C overlap the hydrophobic stretch. General membrane biology alone does not resolve their four-residue endpoint difference."
  },
  "case_id": "transmembrane_0119",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H2"
    ],
    "judgment": "supported",
    "reason": "The sequence exactly matches the UniProt record, whose transmembrane annotation is 483..503. The annotation carries evidence code ECO:0000255, indicating computational support rather than a reported experimental measurement."
  },
  "important_caveats": [
    "The supporting annotation is computational, not direct experimental evidence.",
    "The reviewer-only source record matches the supplied sequence, including in the historical record checked; the author's exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "C"
    ],
    "reason": "Both intervals cover the strongly hydrophobic segment beginning at 483. The additional residues in C remain hydrophobic/aromatic, so the sequence alone does not make the precise boundary between B and C unambiguous."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0119",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence exactly matches the UniProt record, whose transmembrane annotation is 483..503. The annotation carries evidence code ECO:0000255, indicating computational support rather than a reported experimental measurement.",
    "evidence_ids": ["C5", "H2"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence contains a strong hydrophobic C-terminal stretch, which supports a membrane-spanning helix in this region and disfavors choices listing many unrelated segments. It does not establish the precise endpoint.",
    "missing_item_specific_fact": "The specific 483..503 boundary used by the protein's database annotation is absent from the input; distinguishing that boundary from 483..507 requires an item-specific annotation or other evidence.",
    "reason": "Sequence reasoning can locate the likely membrane anchor, but both B and C overlap the hydrophobic stretch. General membrane biology alone does not resolve their four-residue endpoint difference."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "C"],
    "reason": "Both intervals cover the strongly hydrophobic segment beginning at 483. The additional residues in C remain hydrophobic/aromatic, so the sequence alone does not make the precise boundary between B and C unambiguous."
  },
  "important_caveats": [
    "The supporting annotation is computational, not direct experimental evidence.",
    "The reviewer-only source record matches the supplied sequence, including in the historical record checked; the author's exact source snapshot is unknown."
  ]
}
```

</details>

## Before: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt Q9JAE0 (Mumps virus Fusion glycoprotein F0) annotates a single transmembrane helical region at 483..503 (evidence code ECO:0000255, inferred by similarity). Both the current entry (C5) and the historical v90 record (H2) confirm this annotation. The sequence is 538 residues, consistent with a single-pass type I membrane protein typical of paramyxovirus F proteins. Option D is impossible (positions 558-583 exceed the 538-residue sequence), and option A lists 12 TM segments inconsistent with the known single-pass topology of paramyxovirus F proteins.

Citations as saved: [C1](#evidence-c1), [C3](#evidence-c3), [C4](#evidence-c4), [C5](#evidence-c5), [H1](#evidence-h1), [H2](#evidence-h2).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> General knowledge that paramyxovirus F proteins are single-pass type I membrane proteins with one TM helix near the C-terminus eliminates options A (12 TM segments) and D (positions exceeding protein length). Identifying the hydrophobic stretch near the C-terminus (~IVAALVLSILSIIISLLFCCWAYI) as the TM region is reasonable. However, the precise end boundary (503 vs 507) hinges on whether the last ~4 residues (e.g., including W/Y interface residues or a few borderline hydrophobic residues) are counted within the helix. Both 21-residue and 25-residue TM helices fall within the normal range, and the hydrophobicity transition in that region is gradual rather than sharp.


**Missing item-specific fact**

> The exact annotation boundary (483..503 vs 483..507) from the UniProt entry or equivalent structural/hydrophobicity-profile determination. Without the specific annotation or a precise hydropathy plot with a defined threshold, the 4-residue difference between options B and C cannot be reliably resolved by general biological reasoning alone.


**Reason**

> While the general location (single TM near C-terminus, ~position 483) and the elimination of options A and D are reasoning-accessible, the fine discrimination between B (483..503) and C (483..507) depends on the specific annotation boundary. The hydrophobic stretch is ~24 residues long; whether the final 3-4 residues (borderline, near the W/Y interface) are included or excluded requires the item-specific annotation or a precise computational threshold, not general biological principles.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "C"
]
```

> Both 483..503 (21 residues) and 483..507 (25 residues) represent plausible TM helix lengths for a paramyxovirus F protein. The hydrophobic stretch in the C-terminal region is approximately 24 residues, and the boundary between TM core and membrane-interface residues (W, Y) is not sharply defined by sequence alone. Without the annotation, both B and C could be defended on hydrophobicity grounds.


### Important caveats

- The UniProt annotation uses evidence code ECO:0000255 (inferred by similarity), meaning the TM boundary is a computational/transfer annotation rather than direct experimental measurement (e.g., cryo-EM of the full-length F protein).
- Option D is trivially eliminated because positions 558-583 exceed the 538-residue protein length.
- Option A is eliminated by the well-established single-pass topology of paramyxovirus fusion glycoproteins.
- The signal peptide at the N-terminus (MKAFPVICLGFAIFSSSIC) is cleaved and is not a TM domain, which is relevant to eliminating spurious hydrophobic segments in option A.
- The exact author source snapshot is unknown; the annotation has been stable across entry versions 90 and 91.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "General knowledge that paramyxovirus F proteins are single-pass type I membrane proteins with one TM helix near the C-terminus eliminates options A (12 TM segments) and D (positions exceeding protein length). Identifying the hydrophobic stretch near the C-terminus (~IVAALVLSILSIIISLLFCCWAYI) as the TM region is reasonable. However, the precise end boundary (503 vs 507) hinges on whether the last ~4 residues (e.g., including W/Y interface residues or a few borderline hydrophobic residues) are counted within the helix. Both 21-residue and 25-residue TM helices fall within the normal range, and the hydrophobicity transition in that region is gradual rather than sharp.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The exact annotation boundary (483..503 vs 483..507) from the UniProt entry or equivalent structural/hydrophobicity-profile determination. Without the specific annotation or a precise hydropathy plot with a defined threshold, the 4-residue difference between options B and C cannot be reliably resolved by general biological reasoning alone.",
    "reason": "While the general location (single TM near C-terminus, ~position 483) and the elimination of options A and D are reasoning-accessible, the fine discrimination between B (483..503) and C (483..507) depends on the specific annotation boundary. The hydrophobic stretch is ~24 residues long; whether the final 3-4 residues (borderline, near the W/Y interface) are included or excluded requires the item-specific annotation or a precise computational threshold, not general biological principles."
  },
  "case_id": "transmembrane_0119",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C3",
      "C4",
      "C5",
      "H1",
      "H2"
    ],
    "judgment": "supported",
    "reason": "UniProt Q9JAE0 (Mumps virus Fusion glycoprotein F0) annotates a single transmembrane helical region at 483..503 (evidence code ECO:0000255, inferred by similarity). Both the current entry (C5) and the historical v90 record (H2) confirm this annotation. The sequence is 538 residues, consistent with a single-pass type I membrane protein typical of paramyxovirus F proteins. Option D is impossible (positions 558-583 exceed the 538-residue sequence), and option A lists 12 TM segments inconsistent with the known single-pass topology of paramyxovirus F proteins."
  },
  "important_caveats": [
    "The UniProt annotation uses evidence code ECO:0000255 (inferred by similarity), meaning the TM boundary is a computational/transfer annotation rather than direct experimental measurement (e.g., cryo-EM of the full-length F protein).",
    "Option D is trivially eliminated because positions 558-583 exceed the 538-residue protein length.",
    "Option A is eliminated by the well-established single-pass topology of paramyxovirus fusion glycoproteins.",
    "The signal peptide at the N-terminus (MKAFPVICLGFAIFSSSIC) is cleaved and is not a TM domain, which is relevant to eliminating spurious hydrophobic segments in option A.",
    "The exact author source snapshot is unknown; the annotation has been stable across entry versions 90 and 91."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "C"
    ],
    "reason": "Both 483..503 (21 residues) and 483..507 (25 residues) represent plausible TM helix lengths for a paramyxovirus F protein. The hydrophobic stretch in the C-terminal region is approximately 24 residues, and the boundary between TM core and membrane-interface residues (W, Y) is not sharply defined by sequence alone. Without the annotation, both B and C could be defended on hydrophobicity grounds."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0119",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt Q9JAE0 (Mumps virus Fusion glycoprotein F0) annotates a single transmembrane helical region at 483..503 (evidence code ECO:0000255, inferred by similarity). Both the current entry (C5) and the historical v90 record (H2) confirm this annotation. The sequence is 538 residues, consistent with a single-pass type I membrane protein typical of paramyxovirus F proteins. Option D is impossible (positions 558-583 exceed the 538-residue sequence), and option A lists 12 TM segments inconsistent with the known single-pass topology of paramyxovirus F proteins.",
    "evidence_ids": ["C1", "C3", "C4", "C5", "H1", "H2"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "General knowledge that paramyxovirus F proteins are single-pass type I membrane proteins with one TM helix near the C-terminus eliminates options A (12 TM segments) and D (positions exceeding protein length). Identifying the hydrophobic stretch near the C-terminus (~IVAALVLSILSIIISLLFCCWAYI) as the TM region is reasonable. However, the precise end boundary (503 vs 507) hinges on whether the last ~4 residues (e.g., including W/Y interface residues or a few borderline hydrophobic residues) are counted within the helix. Both 21-residue and 25-residue TM helices fall within the normal range, and the hydrophobicity transition in that region is gradual rather than sharp.",
    "missing_item_specific_fact": "The exact annotation boundary (483..503 vs 483..507) from the UniProt entry or equivalent structural/hydrophobicity-profile determination. Without the specific annotation or a precise hydropathy plot with a defined threshold, the 4-residue difference between options B and C cannot be reliably resolved by general biological reasoning alone.",
    "reason": "While the general location (single TM near C-terminus, ~position 483) and the elimination of options A and D are reasoning-accessible, the fine discrimination between B (483..503) and C (483..507) depends on the specific annotation boundary. The hydrophobic stretch is ~24 residues long; whether the final 3-4 residues (borderline, near the W/Y interface) are included or excluded requires the item-specific annotation or a precise computational threshold, not general biological principles."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "C"],
    "reason": "Both 483..503 (21 residues) and 483..507 (25 residues) represent plausible TM helix lengths for a paramyxovirus F protein. The hydrophobic stretch in the C-terminal region is approximately 24 residues, and the boundary between TM core and membrane-interface residues (W, Y) is not sharply defined by sequence alone. Without the annotation, both B and C could be defended on hydrophobicity grounds."
  },
  "important_caveats": [
    "The UniProt annotation uses evidence code ECO:0000255 (inferred by similarity), meaning the TM boundary is a computational/transfer annotation rather than direct experimental measurement (e.g., cryo-EM of the full-length F protein).",
    "Option D is trivially eliminated because positions 558-583 exceed the 538-residue protein length.",
    "Option A is eliminated by the well-established single-pass topology of paramyxovirus fusion glycoproteins.",
    "The signal peptide at the N-terminus (MKAFPVICLGFAIFSSSIC) is cleaved and is not a TM domain, which is relevant to eliminating spurious hydrophobic segments in option A.",
    "The exact author source snapshot is unknown; the annotation has been stable across entry versions 90 and 91."
  ]
}
```

</details>

## After: GPT-6 Luna

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence-matched UniProt record annotates a helical transmembrane region at 483..503, matching choice B. The cited evidence code indicates computational annotation, not experimental validation.

Citations as saved: [C5](#evidence-c5), [H2](#evidence-h2).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence has a strongly hydrophobic C-terminal segment, so transferable knowledge of membrane-spanning helices supports a transmembrane region in this neighborhood and rules out the many-region proposal in A. But that feature does not reliably distinguish B from C: both include the hydrophobic core, and their four-residue endpoint difference lies near the uncertain membrane boundary.


**Missing item-specific fact**

> The exact boundary used for this protein's transmembrane annotation—503 rather than 507—is not specified by the sequence or a boundary convention in the original input.


**Reason**

> Family- or sequence-level reasoning meaningfully identifies the C-terminal membrane-spanning segment, but does not uniquely determine which of the nearly identical B and C ranges is intended. Selecting the keyed endpoint requires the protein-specific annotation or an equivalent boundary determination.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "C"
]
```

> Both ranges cover the same strongly hydrophobic C-terminal helix and differ only in whether the interval extends four residues farther into its boundary region. The prompt supplies no convention that makes that endpoint distinction decisive.


### Important caveats

- The supporting database feature is computationally annotated; it should not be described as experimental confirmation.
- The source sequence matches the supplied sequence, but the exact source snapshot used by the author is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has a strongly hydrophobic C-terminal segment, so transferable knowledge of membrane-spanning helices supports a transmembrane region in this neighborhood and rules out the many-region proposal in A. But that feature does not reliably distinguish B from C: both include the hydrophobic core, and their four-residue endpoint difference lies near the uncertain membrane boundary.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The exact boundary used for this protein's transmembrane annotation—503 rather than 507—is not specified by the sequence or a boundary convention in the original input.",
    "reason": "Family- or sequence-level reasoning meaningfully identifies the C-terminal membrane-spanning segment, but does not uniquely determine which of the nearly identical B and C ranges is intended. Selecting the keyed endpoint requires the protein-specific annotation or an equivalent boundary determination."
  },
  "case_id": "transmembrane_0119",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H2"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates a helical transmembrane region at 483..503, matching choice B. The cited evidence code indicates computational annotation, not experimental validation."
  },
  "important_caveats": [
    "The supporting database feature is computationally annotated; it should not be described as experimental confirmation.",
    "The source sequence matches the supplied sequence, but the exact source snapshot used by the author is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "C"
    ],
    "reason": "Both ranges cover the same strongly hydrophobic C-terminal helix and differ only in whether the interval extends four residues farther into its boundary region. The prompt supplies no convention that makes that endpoint distinction decisive."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0119",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates a helical transmembrane region at 483..503, matching choice B. The cited evidence code indicates computational annotation, not experimental validation.",
    "evidence_ids": ["C5", "H2"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence has a strongly hydrophobic C-terminal segment, so transferable knowledge of membrane-spanning helices supports a transmembrane region in this neighborhood and rules out the many-region proposal in A. But that feature does not reliably distinguish B from C: both include the hydrophobic core, and their four-residue endpoint difference lies near the uncertain membrane boundary.",
    "missing_item_specific_fact": "The exact boundary used for this protein's transmembrane annotation—503 rather than 507—is not specified by the sequence or a boundary convention in the original input.",
    "reason": "Family- or sequence-level reasoning meaningfully identifies the C-terminal membrane-spanning segment, but does not uniquely determine which of the nearly identical B and C ranges is intended. Selecting the keyed endpoint requires the protein-specific annotation or an equivalent boundary determination."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "C"],
    "reason": "Both ranges cover the same strongly hydrophobic C-terminal helix and differ only in whether the interval extends four residues farther into its boundary region. The prompt supplies no convention that makes that endpoint distinction decisive."
  },
  "important_caveats": [
    "The supporting database feature is computationally annotated; it should not be described as experimental confirmation.",
    "The source sequence matches the supplied sequence, but the exact source snapshot used by the author is unknown."
  ]
}
```

</details>

## After: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt annotation (C5, H2) for Q9JAE0 lists exactly one transmembrane region at 483..503, helical, with evidence code ECO:0000255 (inferred by similarity). This matches choice B exactly. Choice C extends to 507 (4 extra residues), choice D includes a region at 558..583 which exceeds the 538-residue protein length, and choice A lists 12 TM regions inconsistent with the single-pass topology of paramyxovirus fusion glycoproteins.

Citations as saved: [C5](#evidence-c5), [H2](#evidence-h2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Family-level knowledge of paramyxovirus F proteins (measles F, NDV F, RSV F, other rubulaviruses) establishes that these are single-pass Type I membrane proteins with one C-terminal transmembrane anchor of approximately 20-23 hydrophobic residues. This eliminates choice A (12 TM regions, incompatible with single-pass topology). Choice D is eliminated by simple arithmetic: position 558 exceeds the 538-residue protein length. The sequence itself shows a clear hydrophobic stretch near the C-terminus ('IGAIIVAALVLSILSIIISLLFCCWAYI') consistent with a single TM helix. Distinguishing B (483..503, 21 residues) from C (483..507, 25 residues) relies on hydrophobicity boundary analysis: after the core hydrophobic stretch, the appearance of polar/charged residues (T, K, E) argues against extending to 507, and the typical TM length for paramyxovirus F proteins (~20-22 residues from measles/NDV homologs) favors 21 over 25.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can eliminate A via single-pass topology of paramyxovirus F proteins, eliminate D via simple length check (558>538), and narrow B vs C through hydrophobicity boundary analysis and family-typical TM length (~20-22 residues). The sequence's C-terminal hydrophobic stretch is visually identifiable, and the drop to polar residues after ~503 supports the shorter boundary. This uses transferable knowledge from other paramyxovirus F proteins and general TM helix principles.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> While B vs C is a fine distinction (21 vs 25 residues), the combination of family-typical TM length (~20-22 residues for paramyxovirus F proteins) and the hydrophobicity profile of the sequence (polar residues appearing after ~503) provides a reasonable basis to prefer B. D is impossible (exceeds protein length) and A contradicts single-pass topology. No two options are equally defensible.


### Important caveats

- The UniProt annotation uses evidence code ECO:0000255 (inferred by similarity), meaning the TM boundary is computationally derived by analogy to related proteins rather than experimentally determined.
- The B vs C distinction (21 vs 25 residues) is subtle; some TM prediction tools include aromatic interfacial residues (W, Y) in the TM boundary, which could argue for the longer 25-residue span.
- The model was not given the protein name or family identity in the input; family recognition must come from sequence features or general knowledge of paramyxovirus F protein architecture.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Family-level knowledge of paramyxovirus F proteins (measles F, NDV F, RSV F, other rubulaviruses) establishes that these are single-pass Type I membrane proteins with one C-terminal transmembrane anchor of approximately 20-23 hydrophobic residues. This eliminates choice A (12 TM regions, incompatible with single-pass topology). Choice D is eliminated by simple arithmetic: position 558 exceeds the 538-residue protein length. The sequence itself shows a clear hydrophobic stretch near the C-terminus ('IGAIIVAALVLSILSIIISLLFCCWAYI') consistent with a single TM helix. Distinguishing B (483..503, 21 residues) from C (483..507, 25 residues) relies on hydrophobicity boundary analysis: after the core hydrophobic stretch, the appearance of polar/charged residues (T, K, E) argues against extending to 507, and the typical TM length for paramyxovirus F proteins (~20-22 residues from measles/NDV homologs) favors 21 over 25.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can eliminate A via single-pass topology of paramyxovirus F proteins, eliminate D via simple length check (558>538), and narrow B vs C through hydrophobicity boundary analysis and family-typical TM length (~20-22 residues). The sequence's C-terminal hydrophobic stretch is visually identifiable, and the drop to polar residues after ~503 supports the shorter boundary. This uses transferable knowledge from other paramyxovirus F proteins and general TM helix principles."
  },
  "case_id": "transmembrane_0119",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H2"
    ],
    "judgment": "supported",
    "reason": "UniProt annotation (C5, H2) for Q9JAE0 lists exactly one transmembrane region at 483..503, helical, with evidence code ECO:0000255 (inferred by similarity). This matches choice B exactly. Choice C extends to 507 (4 extra residues), choice D includes a region at 558..583 which exceeds the 538-residue protein length, and choice A lists 12 TM regions inconsistent with the single-pass topology of paramyxovirus fusion glycoproteins."
  },
  "important_caveats": [
    "The UniProt annotation uses evidence code ECO:0000255 (inferred by similarity), meaning the TM boundary is computationally derived by analogy to related proteins rather than experimentally determined.",
    "The B vs C distinction (21 vs 25 residues) is subtle; some TM prediction tools include aromatic interfacial residues (W, Y) in the TM boundary, which could argue for the longer 25-residue span.",
    "The model was not given the protein name or family identity in the input; family recognition must come from sequence features or general knowledge of paramyxovirus F protein architecture."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While B vs C is a fine distinction (21 vs 25 residues), the combination of family-typical TM length (~20-22 residues for paramyxovirus F proteins) and the hydrophobicity profile of the sequence (polar residues appearing after ~503) provides a reasonable basis to prefer B. D is impossible (exceeds protein length) and A contradicts single-pass topology. No two options are equally defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0119",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt annotation (C5, H2) for Q9JAE0 lists exactly one transmembrane region at 483..503, helical, with evidence code ECO:0000255 (inferred by similarity). This matches choice B exactly. Choice C extends to 507 (4 extra residues), choice D includes a region at 558..583 which exceeds the 538-residue protein length, and choice A lists 12 TM regions inconsistent with the single-pass topology of paramyxovirus fusion glycoproteins.",
    "evidence_ids": ["C5", "H2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Family-level knowledge of paramyxovirus F proteins (measles F, NDV F, RSV F, other rubulaviruses) establishes that these are single-pass Type I membrane proteins with one C-terminal transmembrane anchor of approximately 20-23 hydrophobic residues. This eliminates choice A (12 TM regions, incompatible with single-pass topology). Choice D is eliminated by simple arithmetic: position 558 exceeds the 538-residue protein length. The sequence itself shows a clear hydrophobic stretch near the C-terminus ('IGAIIVAALVLSILSIIISLLFCCWAYI') consistent with a single TM helix. Distinguishing B (483..503, 21 residues) from C (483..507, 25 residues) relies on hydrophobicity boundary analysis: after the core hydrophobic stretch, the appearance of polar/charged residues (T, K, E) argues against extending to 507, and the typical TM length for paramyxovirus F proteins (~20-22 residues from measles/NDV homologs) favors 21 over 25.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can eliminate A via single-pass topology of paramyxovirus F proteins, eliminate D via simple length check (558>538), and narrow B vs C through hydrophobicity boundary analysis and family-typical TM length (~20-22 residues). The sequence's C-terminal hydrophobic stretch is visually identifiable, and the drop to polar residues after ~503 supports the shorter boundary. This uses transferable knowledge from other paramyxovirus F proteins and general TM helix principles."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While B vs C is a fine distinction (21 vs 25 residues), the combination of family-typical TM length (~20-22 residues for paramyxovirus F proteins) and the hydrophobicity profile of the sequence (polar residues appearing after ~503) provides a reasonable basis to prefer B. D is impossible (exceeds protein length) and A contradicts single-pass topology. No two options are equally defensible."
  },
  "important_caveats": [
    "The UniProt annotation uses evidence code ECO:0000255 (inferred by similarity), meaning the TM boundary is computationally derived by analogy to related proteins rather than experimentally determined.",
    "The B vs C distinction (21 vs 25 residues) is subtle; some TM prediction tools include aromatic interfacial residues (W, Y) in the TM boundary, which could argue for the longer 25-residue span.",
    "The model was not given the protein name or family identity in the input; family recognition must come from sequence features or general knowledge of paramyxovirus F protein architecture."
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
  "requested_accession": "Q9JAE0",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "benchmark_sequence_sha256": "84b8b6d5569e7af3104931216ad9f8c5987039b8f633aa753dde20994a79f904",
  "benchmark_sequence_length": 538,
  "current_status": "retrieved",
  "current_sequence_comparison": "matched",
  "current_entry_audit": {
    "entryVersion": 91,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2000-10-01",
    "sequenceVersion": 1
  },
  "current_uniprot_release": "2026_03",
  "current_record_sha256": "a780478bc274d83b2ecd8193dfbe338e0c35241fcd823c0246f785340a757c97",
  "current_source_sequence_sha256": "84b8b6d5569e7af3104931216ad9f8c5987039b8f633aa753dde20994a79f904",
  "current_source_sequence_length": 538,
  "historical_status": "retrieved",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "selected_historical_entry_version": 90,
  "selected_historical_version": {
    "accession": "Q9JAE0",
    "database": "Swiss-Prot",
    "entryVersion": 90,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_02/2026_02",
    "lastReleaseDate": "10-Jun-2026",
    "name": "FUS_MUMPK",
    "sequenceVersion": 1
  },
  "selected_historical_record_sha256": "08d7f73eabc93f41a14ddf3a765bb47e6225789823b6283397bfc28281fbc95b",
  "selected_historical_source_sequence_sha256": "84b8b6d5569e7af3104931216ad9f8c5987039b8f633aa753dde20994a79f904",
  "selected_historical_source_sequence_length": 538,
  "latest_at_cutoff_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 90,
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9JAE0.json)

```json
{
  "evidence_id": "C1",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q9JAE0.json",
  "source_sha256": "a780478bc274d83b2ecd8193dfbe338e0c35241fcd823c0246f785340a757c97",
  "retrieved_utc": "2026-11-02T04:32:53.076550+00:00",
  "json_pointer": "/primaryAccession",
  "excerpt": "\"Q9JAE0\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9JAE0.json)

```json
{
  "evidence_id": "C2",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q9JAE0.json",
  "source_sha256": "a780478bc274d83b2ecd8193dfbe338e0c35241fcd823c0246f785340a757c97",
  "retrieved_utc": "2026-11-02T04:32:53.076550+00:00",
  "json_pointer": "/entryAudit",
  "excerpt": "{\"entryVersion\":91,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2000-10-01\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9JAE0.json)

```json
{
  "evidence_id": "C3",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q9JAE0.json",
  "source_sha256": "a780478bc274d83b2ecd8193dfbe338e0c35241fcd823c0246f785340a757c97",
  "retrieved_utc": "2026-11-02T04:32:53.076550+00:00",
  "json_pointer": "/organism",
  "excerpt": "{\"commonName\":\"MuV\",\"lineage\":[\"Viruses\",\"Riboviria\",\"Orthornavirae\",\"Negarnaviricota\",\"Haploviricotina\",\"Monjiviricetes\",\"Mononegavirales\",\"Paramyxoviridae\",\"Rubulavirinae\",\"Orthorubulavirus\",\"Orthorubulavirus parotitidis\",\"Mumps orthorubulavirus\"],\"scientificName\":\"Mumps virus (strain Kilham)\",\"taxonId\":11169}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9JAE0.json)

```json
{
  "evidence_id": "C4",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q9JAE0.json",
  "source_sha256": "a780478bc274d83b2ecd8193dfbe338e0c35241fcd823c0246f785340a757c97",
  "retrieved_utc": "2026-11-02T04:32:53.076550+00:00",
  "json_pointer": "/proteinDescription",
  "excerpt": "{\"contains\":[{\"recommendedName\":{\"fullName\":{\"value\":\"Fusion glycoprotein F2\"}}},{\"recommendedName\":{\"fullName\":{\"value\":\"Fusion glycoprotein F1\"}}}],\"flag\":\"Precursor\",\"recommendedName\":{\"fullName\":{\"value\":\"Fusion glycoprotein F0\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9JAE0.json)

```json
{
  "evidence_id": "C5",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q9JAE0.json",
  "source_sha256": "a780478bc274d83b2ecd8193dfbe338e0c35241fcd823c0246f785340a757c97",
  "retrieved_utc": "2026-11-02T04:32:53.076550+00:00",
  "json_pointer": "/features/4",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":503},\"start\":{\"modifier\":\"EXACT\",\"value\":483}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9JAE0?format=txt&versions=90)

```json
{
  "evidence_id": "H1",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q9JAE0?format=txt&versions=90",
  "source_sha256": "08d7f73eabc93f41a14ddf3a765bb47e6225789823b6283397bfc28281fbc95b",
  "retrieved_utc": "2026-11-02T04:32:57.440303+00:00",
  "source_locator": "lines 1-18",
  "excerpt": "ID   FUS_MUMPK               Reviewed;         538 AA.\nAC   Q9JAE0;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   01-OCT-2000, sequence version 1.\nDT   28-JAN-2026, entry version 90.\nDE   RecName: Full=Fusion glycoprotein F0;\nDE   Contains:\nDE     RecName: Full=Fusion glycoprotein F2;\nDE   Contains:\nDE     RecName: Full=Fusion glycoprotein F1;\nDE   Flags: Precursor;\nGN   Name=F;\nOS   Mumps virus (strain Kilham) (MuV).\nOC   Viruses; Riboviria; Orthornavirae; Negarnaviricota; Haploviricotina;\nOC   Monjiviricetes; Mononegavirales; Paramyxoviridae; Rubulavirinae;\nOC   Orthorubulavirus; Orthorubulavirus parotitidis; Mumps orthorubulavirus.\nOX   NCBI_TaxID=11169;\nOH   NCBI_TaxID=9606; Homo sapiens (Human).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 90,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9JAE0?format=txt&versions=90)

```json
{
  "evidence_id": "H2",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q9JAE0?format=txt&versions=90",
  "source_sha256": "08d7f73eabc93f41a14ddf3a765bb47e6225789823b6283397bfc28281fbc95b",
  "retrieved_utc": "2026-11-02T04:32:57.440303+00:00",
  "source_locator": "lines 108-110",
  "excerpt": "FT   TRANSMEM        483..503\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 90,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json), zero-based source row 119. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
