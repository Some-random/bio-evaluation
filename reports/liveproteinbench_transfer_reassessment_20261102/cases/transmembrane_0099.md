# transmembrane_0099: before and after transfer clarification

[All 1,328 cases](../README.md) · [Method](../METHOD.md) · [Summary](../SUMMARY.md) · [Exact reviewer user message](../inputs/transmembrane_0099.txt)

**Task:** `transmembrane`  
**Author key, unchanged:** **D** — 483..503

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
MKAFSVTCLGFAVFSSSICVNINILQQIGYIKQQVRQLSYYSQSSSSYIVVKLLPNIQPTDNSCEFKSVTQYNKTLSNLLLPIAENINNIASPSPGSRRHKRFAGIAIGIAALGVATAAQVTAAVSLVQAQTNARAIAAMKNSIQATNRAIFEVKEGTQQLAIAVQAIQDHINTIMNTQLNNMTCQILDNQLATFLGLYLTELTTVFQPQLINPALSPISIQALRSLLGSMTPAVVQATLSTSISAAEILSAGLMEGQIVSVLLDEMQMIVKVNIPTIVTQSNALVIDFYSISSFINNQESIIQLPDRILEIGNEQWSYPAKNCKLTRHHIFCQYNEAERLSLESKLCLAGNISACVFSPIAGSYMRRFVALDGTIVANCRSLTCLCKSPSYPIYQPDHHAVTTIDLTACQTLSLDGLDFSIVSLSNITYAENLTISLSQTINTQPIDISTELSKVNASLQNAVKYIKESNHQLLSVSVNSKIGAIIVTALVLSILSIIISLLFCCWAYIATKEIRRINFKTNHINTISSSVDDLIRY

[Multiple Choices]
A. 278..286; 308..323
B. 483..507
C. 483..503; 567..591
D. 483..503
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

> The sequence-matched UniProt annotation places a helical transmembrane region at 483..503, matching choice D. This annotation is computationally supported (ECO:0000255), not presented as direct experimental evidence.

Citations as saved: [C6](#evidence-c6), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence contains a conspicuous hydrophobic C-terminal stretch consistent with a membrane-spanning helix, distinguishing it from the other distant candidate regions.


**Missing item-specific fact**

> The exact annotated boundary, especially whether the region ends at 503 or extends to 507, is not uniquely established by general hydropathy reasoning.


**Reason**

> Sequence reasoning supports the location of a membrane-spanning helix, but selecting the precise annotated endpoint requires a protein-specific boundary annotation or comparable item-specific evidence.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "D"
]
```

> Both choices include the strongly hydrophobic segment at 483 onward. The additional residues in B could be treated as part of an extended membrane-associated region, while the supplied evidence annotates the core helix as ending at 503.


### Important caveats

- The reviewer-only annotation matches the supplied sequence; the actual source snapshot used by the author is unknown.
- The cited transmembrane annotation is computationally evidenced, not independently validated here by primary experimental data.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a conspicuous hydrophobic C-terminal stretch consistent with a membrane-spanning helix, distinguishing it from the other distant candidate regions.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The exact annotated boundary, especially whether the region ends at 503 or extends to 507, is not uniquely established by general hydropathy reasoning.",
    "reason": "Sequence reasoning supports the location of a membrane-spanning helix, but selecting the precise annotated endpoint requires a protein-specific boundary annotation or comparable item-specific evidence."
  },
  "case_id": "transmembrane_0099",
  "expected_answer_check": {
    "evidence_ids": [
      "C6",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation places a helical transmembrane region at 483..503, matching choice D. This annotation is computationally supported (ECO:0000255), not presented as direct experimental evidence."
  },
  "important_caveats": [
    "The reviewer-only annotation matches the supplied sequence; the actual source snapshot used by the author is unknown.",
    "The cited transmembrane annotation is computationally evidenced, not independently validated here by primary experimental data."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "D"
    ],
    "reason": "Both choices include the strongly hydrophobic segment at 483 onward. The additional residues in B could be treated as part of an extended membrane-associated region, while the supplied evidence annotates the core helix as ending at 503."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0099",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation places a helical transmembrane region at 483..503, matching choice D. This annotation is computationally supported (ECO:0000255), not presented as direct experimental evidence.",
    "evidence_ids": ["C6", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence contains a conspicuous hydrophobic C-terminal stretch consistent with a membrane-spanning helix, distinguishing it from the other distant candidate regions.",
    "missing_item_specific_fact": "The exact annotated boundary, especially whether the region ends at 503 or extends to 507, is not uniquely established by general hydropathy reasoning.",
    "reason": "Sequence reasoning supports the location of a membrane-spanning helix, but selecting the precise annotated endpoint requires a protein-specific boundary annotation or comparable item-specific evidence."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "D"],
    "reason": "Both choices include the strongly hydrophobic segment at 483 onward. The additional residues in B could be treated as part of an extended membrane-associated region, while the supplied evidence annotates the core helix as ending at 503."
  },
  "important_caveats": [
    "The reviewer-only annotation matches the supplied sequence; the actual source snapshot used by the author is unknown.",
    "The cited transmembrane annotation is computationally evidenced, not independently validated here by primary experimental data."
  ]
}
```

</details>

## Before: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry Q5SC53 (Mumps virus Fusion glycoprotein F0, 538 AA) annotates a single transmembrane helix at positions 483..503 (evidence code ECO:0000255, homology/proximity inference), flanked by an extracellular topological domain (20..482) and a cytoplasmic domain (504..538). This is consistent with the well-established single-pass type I membrane topology of paramyxovirus class I fusion glycoproteins. The sequence match is confirmed (SHA-256 identical). The annotation is computational/homology-based rather than directly experimental, but it is a standard, well-supported annotation for this protein family.

Citations as saved: [C6](#evidence-c6), [H3](#evidence-h3), [C5](#evidence-c5), [C7](#evidence-c7), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> A model can reason from the sequence that (1) option A references positions (278-286, 308-323) in the large extracellular domain where the sequence is not hydrophobic, and (2) option C references positions 567-591 which exceed the protein length of 538 residues, so both are clearly eliminable. The remaining critical choice is between B (483..507) and D (483..503). The hydrophobic stretch in the C-terminal region is identifiable, but the exact C-terminal boundary of the TM helix at residue 503 versus 507 cannot be definitively resolved from sequence alone: residues 504-507 (C, C, W, A) are also hydrophobic, and the aromatic Trp at ~506 could plausibly be part of the membrane-water interface. Distinguishing 21-residue vs 25-residue TM helix boundaries depends on the specific annotation convention for this protein.


**Missing item-specific fact**

> The precise C-terminal boundary of the transmembrane helix (residue 503 vs 507) as annotated in UniProt for this specific Mumps virus F protein entry, which is a protein-specific annotation boundary not derivable from general hydrophobicity analysis alone.


**Reason**

> While general sequence reasoning eliminates options A and C, the decisive distinction between B (483..507) and D (483..503) requires knowledge of the exact annotation boundary. Both 21- and 25-residue TM helices are within the normal range for class I fusion proteins, and the sequence around 503-507 (FLCCWA) does not provide a clear-cut hydrophobicity cutoff. The answer depends on the specific UniProt annotation rather than a generalizable biological principle.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "D"
]
```

> From sequence analysis alone, both 483..503 (21 residues) and 483..507 (25 residues) are plausible TM helix boundaries. The residues at 504-507 (C, C, W, A) are hydrophobic, and Trp is a classic membrane-interface residue. Without the specific annotation, a knowledgeable model could reasonably select B. However, option C is definitively eliminable (positions beyond protein length) and A is eliminable (non-hydrophobic extracellular region).


### Important caveats

- The UniProt TM annotation uses evidence code ECO:0000255 (similarity/proximity), meaning it is inferred by homology to related paramyxovirus F proteins rather than from direct experimental measurement of this specific strain's TM boundaries.
- The sequence is from a vaccine strain (L-Zagreb) of Mumps virus genotype N; TM boundaries in paramyxovirus F proteins are generally well-conserved across strains.
- Option C's second segment (567..591) references positions beyond the 538-residue protein, making it trivially eliminable regardless of biological reasoning.
- The author key (D) matches the current UniProt annotation exactly, but the annotation is computational/homology-based, not experimentally determined for this specific protein.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "A model can reason from the sequence that (1) option A references positions (278-286, 308-323) in the large extracellular domain where the sequence is not hydrophobic, and (2) option C references positions 567-591 which exceed the protein length of 538 residues, so both are clearly eliminable. The remaining critical choice is between B (483..507) and D (483..503). The hydrophobic stretch in the C-terminal region is identifiable, but the exact C-terminal boundary of the TM helix at residue 503 versus 507 cannot be definitively resolved from sequence alone: residues 504-507 (C, C, W, A) are also hydrophobic, and the aromatic Trp at ~506 could plausibly be part of the membrane-water interface. Distinguishing 21-residue vs 25-residue TM helix boundaries depends on the specific annotation convention for this protein.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The precise C-terminal boundary of the transmembrane helix (residue 503 vs 507) as annotated in UniProt for this specific Mumps virus F protein entry, which is a protein-specific annotation boundary not derivable from general hydrophobicity analysis alone.",
    "reason": "While general sequence reasoning eliminates options A and C, the decisive distinction between B (483..507) and D (483..503) requires knowledge of the exact annotation boundary. Both 21- and 25-residue TM helices are within the normal range for class I fusion proteins, and the sequence around 503-507 (FLCCWA) does not provide a clear-cut hydrophobicity cutoff. The answer depends on the specific UniProt annotation rather than a generalizable biological principle."
  },
  "case_id": "transmembrane_0099",
  "expected_answer_check": {
    "evidence_ids": [
      "C6",
      "H3",
      "C5",
      "C7",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "UniProt entry Q5SC53 (Mumps virus Fusion glycoprotein F0, 538 AA) annotates a single transmembrane helix at positions 483..503 (evidence code ECO:0000255, homology/proximity inference), flanked by an extracellular topological domain (20..482) and a cytoplasmic domain (504..538). This is consistent with the well-established single-pass type I membrane topology of paramyxovirus class I fusion glycoproteins. The sequence match is confirmed (SHA-256 identical). The annotation is computational/homology-based rather than directly experimental, but it is a standard, well-supported annotation for this protein family."
  },
  "important_caveats": [
    "The UniProt TM annotation uses evidence code ECO:0000255 (similarity/proximity), meaning it is inferred by homology to related paramyxovirus F proteins rather than from direct experimental measurement of this specific strain's TM boundaries.",
    "The sequence is from a vaccine strain (L-Zagreb) of Mumps virus genotype N; TM boundaries in paramyxovirus F proteins are generally well-conserved across strains.",
    "Option C's second segment (567..591) references positions beyond the 538-residue protein, making it trivially eliminable regardless of biological reasoning.",
    "The author key (D) matches the current UniProt annotation exactly, but the annotation is computational/homology-based, not experimentally determined for this specific protein."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "D"
    ],
    "reason": "From sequence analysis alone, both 483..503 (21 residues) and 483..507 (25 residues) are plausible TM helix boundaries. The residues at 504-507 (C, C, W, A) are hydrophobic, and Trp is a classic membrane-interface residue. Without the specific annotation, a knowledgeable model could reasonably select B. However, option C is definitively eliminable (positions beyond protein length) and A is eliminable (non-hydrophobic extracellular region)."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0099",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry Q5SC53 (Mumps virus Fusion glycoprotein F0, 538 AA) annotates a single transmembrane helix at positions 483..503 (evidence code ECO:0000255, homology/proximity inference), flanked by an extracellular topological domain (20..482) and a cytoplasmic domain (504..538). This is consistent with the well-established single-pass type I membrane topology of paramyxovirus class I fusion glycoproteins. The sequence match is confirmed (SHA-256 identical). The annotation is computational/homology-based rather than directly experimental, but it is a standard, well-supported annotation for this protein family.",
    "evidence_ids": ["C6", "H3", "C5", "C7", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "A model can reason from the sequence that (1) option A references positions (278-286, 308-323) in the large extracellular domain where the sequence is not hydrophobic, and (2) option C references positions 567-591 which exceed the protein length of 538 residues, so both are clearly eliminable. The remaining critical choice is between B (483..507) and D (483..503). The hydrophobic stretch in the C-terminal region is identifiable, but the exact C-terminal boundary of the TM helix at residue 503 versus 507 cannot be definitively resolved from sequence alone: residues 504-507 (C, C, W, A) are also hydrophobic, and the aromatic Trp at ~506 could plausibly be part of the membrane-water interface. Distinguishing 21-residue vs 25-residue TM helix boundaries depends on the specific annotation convention for this protein.",
    "missing_item_specific_fact": "The precise C-terminal boundary of the transmembrane helix (residue 503 vs 507) as annotated in UniProt for this specific Mumps virus F protein entry, which is a protein-specific annotation boundary not derivable from general hydrophobicity analysis alone.",
    "reason": "While general sequence reasoning eliminates options A and C, the decisive distinction between B (483..507) and D (483..503) requires knowledge of the exact annotation boundary. Both 21- and 25-residue TM helices are within the normal range for class I fusion proteins, and the sequence around 503-507 (FLCCWA) does not provide a clear-cut hydrophobicity cutoff. The answer depends on the specific UniProt annotation rather than a generalizable biological principle."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "D"],
    "reason": "From sequence analysis alone, both 483..503 (21 residues) and 483..507 (25 residues) are plausible TM helix boundaries. The residues at 504-507 (C, C, W, A) are hydrophobic, and Trp is a classic membrane-interface residue. Without the specific annotation, a knowledgeable model could reasonably select B. However, option C is definitively eliminable (positions beyond protein length) and A is eliminable (non-hydrophobic extracellular region)."
  },
  "important_caveats": [
    "The UniProt TM annotation uses evidence code ECO:0000255 (similarity/proximity), meaning it is inferred by homology to related paramyxovirus F proteins rather than from direct experimental measurement of this specific strain's TM boundaries.",
    "The sequence is from a vaccine strain (L-Zagreb) of Mumps virus genotype N; TM boundaries in paramyxovirus F proteins are generally well-conserved across strains.",
    "Option C's second segment (567..591) references positions beyond the 538-residue protein, making it trivially eliminable regardless of biological reasoning.",
    "The author key (D) matches the current UniProt annotation exactly, but the annotation is computational/homology-based, not experimentally determined for this specific protein."
  ]
}
```

</details>

## After: GPT-6 Luna

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence-matched historical UniProt entry annotates residues 483–503 as a helical transmembrane region, supporting the key. The annotation is computationally evidenced (ECO:0000255), so this supports the answer as a database annotation, not as independently established experimental evidence.

Citations as saved: [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has a conspicuous hydrophobic stretch near its C terminus, followed by a more polar/charged tail, a transferable pattern for a membrane anchor in a membrane glycoprotein. Its roughly membrane-length hydrophobic core favors D over the internal region in A; C also proposes positions beyond the 538-residue sequence. B overlaps the same anchor but extends farther into its flanking region.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The sequence itself provides a credible basis for identifying the C-terminal membrane-spanning segment and favoring its hydrophobic core. Exact boundaries are less certain from sequence alone, but the main distinction does not require knowing this protein’s recorded annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "D"
]
```

> B and D share the same start and encompass the same strongly hydrophobic core; B extends the endpoint by four residues. Because membrane boundaries can be fuzzy and flanking hydrophobic or aromatic residues may lie at the membrane interface, sequence evidence alone does not make that endpoint distinction absolute. D remains the better match to the annotated core.


### Important caveats

- The historical annotation matches the supplied sequence, but its evidence code indicates computational annotation rather than experimental proof.
- The source evidence is reviewer-only and was not part of the original input.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has a conspicuous hydrophobic stretch near its C terminus, followed by a more polar/charged tail, a transferable pattern for a membrane anchor in a membrane glycoprotein. Its roughly membrane-length hydrophobic core favors D over the internal region in A; C also proposes positions beyond the 538-residue sequence. B overlaps the same anchor but extends farther into its flanking region.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The sequence itself provides a credible basis for identifying the C-terminal membrane-spanning segment and favoring its hydrophobic core. Exact boundaries are less certain from sequence alone, but the main distinction does not require knowing this protein’s recorded annotation."
  },
  "case_id": "transmembrane_0099",
  "expected_answer_check": {
    "evidence_ids": [
      "H3"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched historical UniProt entry annotates residues 483–503 as a helical transmembrane region, supporting the key. The annotation is computationally evidenced (ECO:0000255), so this supports the answer as a database annotation, not as independently established experimental evidence."
  },
  "important_caveats": [
    "The historical annotation matches the supplied sequence, but its evidence code indicates computational annotation rather than experimental proof.",
    "The source evidence is reviewer-only and was not part of the original input."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "D"
    ],
    "reason": "B and D share the same start and encompass the same strongly hydrophobic core; B extends the endpoint by four residues. Because membrane boundaries can be fuzzy and flanking hydrophobic or aromatic residues may lie at the membrane interface, sequence evidence alone does not make that endpoint distinction absolute. D remains the better match to the annotated core."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0099",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched historical UniProt entry annotates residues 483–503 as a helical transmembrane region, supporting the key. The annotation is computationally evidenced (ECO:0000255), so this supports the answer as a database annotation, not as independently established experimental evidence.",
    "evidence_ids": ["H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has a conspicuous hydrophobic stretch near its C terminus, followed by a more polar/charged tail, a transferable pattern for a membrane anchor in a membrane glycoprotein. Its roughly membrane-length hydrophobic core favors D over the internal region in A; C also proposes positions beyond the 538-residue sequence. B overlaps the same anchor but extends farther into its flanking region.",
    "missing_item_specific_fact": "",
    "reason": "The sequence itself provides a credible basis for identifying the C-terminal membrane-spanning segment and favoring its hydrophobic core. Exact boundaries are less certain from sequence alone, but the main distinction does not require knowing this protein’s recorded annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "D"],
    "reason": "B and D share the same start and encompass the same strongly hydrophobic core; B extends the endpoint by four residues. Because membrane boundaries can be fuzzy and flanking hydrophobic or aromatic residues may lie at the membrane interface, sequence evidence alone does not make that endpoint distinction absolute. D remains the better match to the annotated core."
  },
  "important_caveats": [
    "The historical annotation matches the supplied sequence, but its evidence code indicates computational annotation rather than experimental proof.",
    "The source evidence is reviewer-only and was not part of the original input."
  ]
}
```

</details>

## After: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt annotation (evidence code ECO:0000255, similarity-based) explicitly annotates a single transmembrane helix at 483..503, with the extracellular domain ending at 482 and the cytoplasmic domain beginning at 504. The sequence at 483-503 (IGAIIVTALVLSILSIIISLL) is a hydrophobic alpha-helical stretch consistent with a single-pass TM anchor. This matches choice D exactly.

Citations as saved: [C6](#evidence-c6), [H3](#evidence-h3), [C5](#evidence-c5), [H2](#evidence-h2), [C7](#evidence-c7), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Multiple transferable inferences distinguish D from the alternatives: (1) Option C references positions 567-591 in a 538-residue protein, immediately eliminating it. (2) Option A (278-286; 308-323) contains charged/polar residues (K, N, P, Q, D, R, E, G, N, Q) incompatible with a TM helix's hydrophobic core. (3) The sequence at 483-503 is a classic ~21-residue aliphatic hydrophobic stretch (I,G,A,I,I,V,T,A,L,V,L,S,I,L,S,I,I,I,S,L,L), the hallmark of a single-pass TM anchor. (4) Distinguishing D (483-503) from B (483-507): the additional residues at 504-507 (F,C,C,W) are aromatic residues characteristic of the membrane-water interface 'aromatic belt' that marks the TM/cytoplasmic boundary, not the hydrophobic core. This is a well-established principle in membrane protein biology (Trp/Tyr anchoring at lipid-water interfaces). (5) The protein architecture—a large extracellular domain (~480 residues) followed by a single C-terminal TM helix and a short cytoplasmic tail (~35 residues)—matches the known topology of paramyxovirus class I fusion glycoproteins (NDV F, measles F, RSV F homologs), all of which have a single TM anchor near the C-terminus. The annotation evidence code ECO:0000255 confirms this topology was transferred from related paramyxovirus F proteins.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can eliminate C by sequence length, eliminate A by hydrophobicity analysis, and distinguish D from B using the aromatic-belt boundary principle and the well-known single-TM topology of paramyxovirus fusion glycoproteins learned from homologs like NDV F and measles F. The hydrophobic core clearly ends at position 503, with aromatic residues at 504-507 serving as interface markers.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Option C is invalid (exceeds protein length). Option A lacks hydrophobic character. Option B extends the TM by 4 aromatic residues that are more consistent with the interface/boundary rather than the hydrophobic core. Option D matches the canonical hydrophobic stretch and the known paramyxovirus F topology. While B vs D is the closest call, the aromatic-belt principle and family-level topology knowledge favor D.


### Important caveats

- The UniProt annotation uses evidence code ECO:0000255 (similarity-based transfer), meaning the TM boundaries were inferred from related proteins rather than determined experimentally for this exact sequence.
- The distinction between D (483-503) and B (483-507) is the most subtle aspect; some TM predictors might include the aromatic residues as part of the TM helix. However, the aliphatic-only core convention and the paramyxovirus F family topology favor the shorter definition.
- The protein identity (Mumps virus F glycoprotein) was not provided to the model; recognition relies on sequence features and family-level pattern matching.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Multiple transferable inferences distinguish D from the alternatives: (1) Option C references positions 567-591 in a 538-residue protein, immediately eliminating it. (2) Option A (278-286; 308-323) contains charged/polar residues (K, N, P, Q, D, R, E, G, N, Q) incompatible with a TM helix's hydrophobic core. (3) The sequence at 483-503 is a classic ~21-residue aliphatic hydrophobic stretch (I,G,A,I,I,V,T,A,L,V,L,S,I,L,S,I,I,I,S,L,L), the hallmark of a single-pass TM anchor. (4) Distinguishing D (483-503) from B (483-507): the additional residues at 504-507 (F,C,C,W) are aromatic residues characteristic of the membrane-water interface 'aromatic belt' that marks the TM/cytoplasmic boundary, not the hydrophobic core. This is a well-established principle in membrane protein biology (Trp/Tyr anchoring at lipid-water interfaces). (5) The protein architecture—a large extracellular domain (~480 residues) followed by a single C-terminal TM helix and a short cytoplasmic tail (~35 residues)—matches the known topology of paramyxovirus class I fusion glycoproteins (NDV F, measles F, RSV F homologs), all of which have a single TM anchor near the C-terminus. The annotation evidence code ECO:0000255 confirms this topology was transferred from related paramyxovirus F proteins.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can eliminate C by sequence length, eliminate A by hydrophobicity analysis, and distinguish D from B using the aromatic-belt boundary principle and the well-known single-TM topology of paramyxovirus fusion glycoproteins learned from homologs like NDV F and measles F. The hydrophobic core clearly ends at position 503, with aromatic residues at 504-507 serving as interface markers."
  },
  "case_id": "transmembrane_0099",
  "expected_answer_check": {
    "evidence_ids": [
      "C6",
      "H3",
      "C5",
      "H2",
      "C7",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt annotation (evidence code ECO:0000255, similarity-based) explicitly annotates a single transmembrane helix at 483..503, with the extracellular domain ending at 482 and the cytoplasmic domain beginning at 504. The sequence at 483-503 (IGAIIVTALVLSILSIIISLL) is a hydrophobic alpha-helical stretch consistent with a single-pass TM anchor. This matches choice D exactly."
  },
  "important_caveats": [
    "The UniProt annotation uses evidence code ECO:0000255 (similarity-based transfer), meaning the TM boundaries were inferred from related proteins rather than determined experimentally for this exact sequence.",
    "The distinction between D (483-503) and B (483-507) is the most subtle aspect; some TM predictors might include the aromatic residues as part of the TM helix. However, the aliphatic-only core convention and the paramyxovirus F family topology favor the shorter definition.",
    "The protein identity (Mumps virus F glycoprotein) was not provided to the model; recognition relies on sequence features and family-level pattern matching."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Option C is invalid (exceeds protein length). Option A lacks hydrophobic character. Option B extends the TM by 4 aromatic residues that are more consistent with the interface/boundary rather than the hydrophobic core. Option D matches the canonical hydrophobic stretch and the known paramyxovirus F topology. While B vs D is the closest call, the aromatic-belt principle and family-level topology knowledge favor D."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0099",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt annotation (evidence code ECO:0000255, similarity-based) explicitly annotates a single transmembrane helix at 483..503, with the extracellular domain ending at 482 and the cytoplasmic domain beginning at 504. The sequence at 483-503 (IGAIIVTALVLSILSIIISLL) is a hydrophobic alpha-helical stretch consistent with a single-pass TM anchor. This matches choice D exactly.",
    "evidence_ids": ["C6", "H3", "C5", "H2", "C7", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Multiple transferable inferences distinguish D from the alternatives: (1) Option C references positions 567-591 in a 538-residue protein, immediately eliminating it. (2) Option A (278-286; 308-323) contains charged/polar residues (K, N, P, Q, D, R, E, G, N, Q) incompatible with a TM helix's hydrophobic core. (3) The sequence at 483-503 is a classic ~21-residue aliphatic hydrophobic stretch (I,G,A,I,I,V,T,A,L,V,L,S,I,L,S,I,I,I,S,L,L), the hallmark of a single-pass TM anchor. (4) Distinguishing D (483-503) from B (483-507): the additional residues at 504-507 (F,C,C,W) are aromatic residues characteristic of the membrane-water interface 'aromatic belt' that marks the TM/cytoplasmic boundary, not the hydrophobic core. This is a well-established principle in membrane protein biology (Trp/Tyr anchoring at lipid-water interfaces). (5) The protein architecture—a large extracellular domain (~480 residues) followed by a single C-terminal TM helix and a short cytoplasmic tail (~35 residues)—matches the known topology of paramyxovirus class I fusion glycoproteins (NDV F, measles F, RSV F homologs), all of which have a single TM anchor near the C-terminus. The annotation evidence code ECO:0000255 confirms this topology was transferred from related paramyxovirus F proteins.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can eliminate C by sequence length, eliminate A by hydrophobicity analysis, and distinguish D from B using the aromatic-belt boundary principle and the well-known single-TM topology of paramyxovirus fusion glycoproteins learned from homologs like NDV F and measles F. The hydrophobic core clearly ends at position 503, with aromatic residues at 504-507 serving as interface markers."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Option C is invalid (exceeds protein length). Option A lacks hydrophobic character. Option B extends the TM by 4 aromatic residues that are more consistent with the interface/boundary rather than the hydrophobic core. Option D matches the canonical hydrophobic stretch and the known paramyxovirus F topology. While B vs D is the closest call, the aromatic-belt principle and family-level topology knowledge favor D."
  },
  "important_caveats": [
    "The UniProt annotation uses evidence code ECO:0000255 (similarity-based transfer), meaning the TM boundaries were inferred from related proteins rather than determined experimentally for this exact sequence.",
    "The distinction between D (483-503) and B (483-507) is the most subtle aspect; some TM predictors might include the aromatic residues as part of the TM helix. However, the aliphatic-only core convention and the paramyxovirus F family topology favor the shorter definition.",
    "The protein identity (Mumps virus F glycoprotein) was not provided to the model; recognition relies on sequence features and family-level pattern matching."
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
  "requested_accession": "Q5SC53",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "benchmark_sequence_sha256": "ca344ce86c8ca532870fd703c59b36aa651563981a4288efac2646db70979fec",
  "benchmark_sequence_length": 538,
  "current_status": "retrieved",
  "current_sequence_comparison": "matched",
  "current_entry_audit": {
    "entryVersion": 81,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-06-10",
    "lastSequenceUpdateDate": "2004-12-21",
    "sequenceVersion": 1
  },
  "current_uniprot_release": "2026_03",
  "current_record_sha256": "72eeca0dc4f0e1b54320c79e260ae9238e7fcefb733b978db81bae5e0d233fa9",
  "current_source_sequence_sha256": "ca344ce86c8ca532870fd703c59b36aa651563981a4288efac2646db70979fec",
  "current_source_sequence_length": 538,
  "historical_status": "retrieved",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "selected_historical_entry_version": 80,
  "selected_historical_version": {
    "accession": "Q5SC53",
    "database": "Swiss-Prot",
    "entryVersion": 80,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "FUS_MUMPZ",
    "sequenceVersion": 1
  },
  "selected_historical_record_sha256": "afb9ab9d6093f040c16474e49b884836fed8582e6d2cecfa0264668dfd09db66",
  "selected_historical_source_sequence_sha256": "ca344ce86c8ca532870fd703c59b36aa651563981a4288efac2646db70979fec",
  "selected_historical_source_sequence_length": 538,
  "latest_at_cutoff_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 80,
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5SC53.json)

```json
{
  "evidence_id": "C1",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q5SC53.json",
  "source_sha256": "72eeca0dc4f0e1b54320c79e260ae9238e7fcefb733b978db81bae5e0d233fa9",
  "retrieved_utc": "2026-11-01T06:25:22.414761+00:00",
  "json_pointer": "/primaryAccession",
  "excerpt": "\"Q5SC53\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5SC53.json)

```json
{
  "evidence_id": "C2",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q5SC53.json",
  "source_sha256": "72eeca0dc4f0e1b54320c79e260ae9238e7fcefb733b978db81bae5e0d233fa9",
  "retrieved_utc": "2026-11-01T06:25:22.414761+00:00",
  "json_pointer": "/entryAudit",
  "excerpt": "{\"entryVersion\":81,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-06-10\",\"lastSequenceUpdateDate\":\"2004-12-21\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5SC53.json)

```json
{
  "evidence_id": "C3",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q5SC53.json",
  "source_sha256": "72eeca0dc4f0e1b54320c79e260ae9238e7fcefb733b978db81bae5e0d233fa9",
  "retrieved_utc": "2026-11-01T06:25:22.414761+00:00",
  "json_pointer": "/organism",
  "excerpt": "{\"commonName\":\"MuV\",\"lineage\":[\"Viruses\",\"Riboviria\",\"Orthornavirae\",\"Negarnaviricota\",\"Haploviricotina\",\"Monjiviricetes\",\"Mononegavirales\",\"Paramyxoviridae\",\"Rubulavirinae\",\"Orthorubulavirus\",\"Orthorubulavirus parotitidis\",\"Mumps orthorubulavirus\"],\"scientificName\":\"Mumps virus genotype N (strain L-Zagreb vaccine)\",\"taxonId\":301186}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5SC53.json)

```json
{
  "evidence_id": "C4",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q5SC53.json",
  "source_sha256": "72eeca0dc4f0e1b54320c79e260ae9238e7fcefb733b978db81bae5e0d233fa9",
  "retrieved_utc": "2026-11-01T06:25:22.414761+00:00",
  "json_pointer": "/proteinDescription",
  "excerpt": "{\"contains\":[{\"recommendedName\":{\"fullName\":{\"value\":\"Fusion glycoprotein F2\"}}},{\"recommendedName\":{\"fullName\":{\"value\":\"Fusion glycoprotein F1\"}}}],\"flag\":\"Precursor\",\"recommendedName\":{\"fullName\":{\"value\":\"Fusion glycoprotein F0\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5SC53.json)

```json
{
  "evidence_id": "C5",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q5SC53.json",
  "source_sha256": "72eeca0dc4f0e1b54320c79e260ae9238e7fcefb733b978db81bae5e0d233fa9",
  "retrieved_utc": "2026-11-01T06:25:22.414761+00:00",
  "json_pointer": "/features/4",
  "excerpt": "{\"description\":\"Extracellular\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":482},\"start\":{\"modifier\":\"EXACT\",\"value\":20}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5SC53.json)

```json
{
  "evidence_id": "C6",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q5SC53.json",
  "source_sha256": "72eeca0dc4f0e1b54320c79e260ae9238e7fcefb733b978db81bae5e0d233fa9",
  "retrieved_utc": "2026-11-01T06:25:22.414761+00:00",
  "json_pointer": "/features/5",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":503},\"start\":{\"modifier\":\"EXACT\",\"value\":483}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5SC53.json)

```json
{
  "evidence_id": "C7",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q5SC53.json",
  "source_sha256": "72eeca0dc4f0e1b54320c79e260ae9238e7fcefb733b978db81bae5e0d233fa9",
  "retrieved_utc": "2026-11-01T06:25:22.414761+00:00",
  "json_pointer": "/features/6",
  "excerpt": "{\"description\":\"Cytoplasmic\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":538},\"start\":{\"modifier\":\"EXACT\",\"value\":504}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5SC53?format=txt&versions=80)

```json
{
  "evidence_id": "H1",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q5SC53?format=txt&versions=80",
  "source_sha256": "afb9ab9d6093f040c16474e49b884836fed8582e6d2cecfa0264668dfd09db66",
  "retrieved_utc": "2026-11-01T06:28:38.619336+00:00",
  "source_locator": "lines 1-18",
  "excerpt": "ID   FUS_MUMPZ               Reviewed;         538 AA.\nAC   Q5SC53;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   21-DEC-2004, sequence version 1.\nDT   28-JAN-2026, entry version 80.\nDE   RecName: Full=Fusion glycoprotein F0;\nDE   Contains:\nDE     RecName: Full=Fusion glycoprotein F2;\nDE   Contains:\nDE     RecName: Full=Fusion glycoprotein F1;\nDE   Flags: Precursor;\nGN   Name=F;\nOS   Mumps virus genotype N (strain L-Zagreb vaccine) (MuV).\nOC   Viruses; Riboviria; Orthornavirae; Negarnaviricota; Haploviricotina;\nOC   Monjiviricetes; Mononegavirales; Paramyxoviridae; Rubulavirinae;\nOC   Orthorubulavirus; Orthorubulavirus parotitidis; Mumps orthorubulavirus.\nOX   NCBI_TaxID=301186;\nOH   NCBI_TaxID=9606; Homo sapiens (Human).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 80,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5SC53?format=txt&versions=80)

```json
{
  "evidence_id": "H2",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q5SC53?format=txt&versions=80",
  "source_sha256": "afb9ab9d6093f040c16474e49b884836fed8582e6d2cecfa0264668dfd09db66",
  "retrieved_utc": "2026-11-01T06:28:38.619336+00:00",
  "source_locator": "lines 124-126",
  "excerpt": "FT   TOPO_DOM        20..482\nFT                   /note=\"Extracellular\"\nFT                   /evidence=\"ECO:0000250\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 80,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5SC53?format=txt&versions=80)

```json
{
  "evidence_id": "H3",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q5SC53?format=txt&versions=80",
  "source_sha256": "afb9ab9d6093f040c16474e49b884836fed8582e6d2cecfa0264668dfd09db66",
  "retrieved_utc": "2026-11-01T06:28:38.619336+00:00",
  "source_locator": "lines 127-129",
  "excerpt": "FT   TRANSMEM        483..503\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 80,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5SC53?format=txt&versions=80)

```json
{
  "evidence_id": "H4",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q5SC53?format=txt&versions=80",
  "source_sha256": "afb9ab9d6093f040c16474e49b884836fed8582e6d2cecfa0264668dfd09db66",
  "retrieved_utc": "2026-11-01T06:28:38.619336+00:00",
  "source_locator": "lines 130-132",
  "excerpt": "FT   TOPO_DOM        504..538\nFT                   /note=\"Cytoplasmic\"\nFT                   /evidence=\"ECO:0000250\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 80,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json), zero-based source row 99. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
