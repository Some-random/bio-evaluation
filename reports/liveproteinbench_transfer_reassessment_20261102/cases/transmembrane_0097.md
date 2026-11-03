# transmembrane_0097: before and after transfer clarification

[All 1,328 cases](../README.md) · [Method](../METHOD.md) · [Summary](../SUMMARY.md) · [Exact reviewer user message](../inputs/transmembrane_0097.txt)

**Task:** `transmembrane`  
**Author key, unchanged:** **B** — 371..391; 409..429; 444..464; 472..492; 531..551; 564..586; 596..618

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
MKQNPAKTARMWIIICLLFVLGQATDNDRDFKMCGKWLHGIAPQNLEYDLKTGCERIEISANESTLSIQGRITAKCTQSSSIQLDSNPHQNQSHFCVFWEPLLDLLIVEVNGKNHTLCKPNGLQGTCCTDLSQGVQDNAHMYGIVNGSVKGDIITGDLKGNYIFDGAHINCKEKFCDEARLKPRGANMIEEVVMRFNAKGRVDLPCAQGTVIEMDEEFTGHNFTVPAPRFVDANTIPSVYIPSSLRSVSRRKSKVVCTYYKNKTLFERGPSKSALLDDIVGLSVENETIRNLIEPVKIRFHHRPFAPDSSGRCVSWDTKQDNEVNWKDDGCDTVKINEEQTECHCNHLTYFAILVQVEQKSTVRHLKALTFITAVGCAVSLVSCLVLFYWLCKRRRGKKNQISLVHRGLVVAIFLLCLFFILTGILANVANETVCQLTGSLLHYGLLSTLCWMAMEVFHTFLLVRKVFNSPLPIWIFYLMGFGFPFLLVSILLSVGDIYGERKIKPSDDVNNPYRMCWMTEGDKSQLAHYIINIGLLAVVVSSGLVMLFLVVREIRNRPDWKKIHVAFLSIWGLTCLYGTTWALGFLDFGPFSEVTLFLFCIINSLQGFFLMLRYYALERMKKKDVSSSDGSSSGSSKQHMLQTNEKS

[Multiple Choices]
A. 32..52; 730..750; 795..815; 845..865; 1111..1131
B. 371..391; 409..429; 444..464; 472..492; 531..551; 564..586; 596..618
C. 371..391; 409..429; 472..492; 531..551; 564..586; 596..618
D. 371..391; 409..431; 444..464; 472..492; 531..551; 564..586; 596..618
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

> The sequence matches the historical UniProt record, whose annotations list all seven transmembrane segments in choice B. These are computational annotations (ECO:0000255), not evidence of direct experimental measurement of the boundaries.

Citations as saved: [H5](#evidence-h5), [H7](#evidence-h7), [H9](#evidence-h9), [H11](#evidence-h11), [H13](#evidence-h13), [H15](#evidence-h15), [H17](#evidence-h17).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence's hydrophobic stretches support identifying a multi-pass membrane region and can distinguish it from the clearly mismatched option A, but do not establish the exact boundaries needed to choose between the near-identical options.


**Missing item-specific fact**

> The particular transmembrane boundary annotations for this protein, especially whether the helix is labeled 409..429 or 409..431.


**Reason**

> The input gives a sequence but no boundary convention or protein-specific topology annotation. General hydrophobicity reasoning can locate likely helices, but cannot robustly resolve the precise coordinates that distinguish the remaining choices.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "D"
]
```

> B and D list the same regions except that D extends one predicted helix by two residues, 409..431 rather than 409..429. Without a stated boundary convention, both ranges can reasonably describe the same membrane-spanning helix.


### Important caveats

- The supporting annotation applies to the exact supplied sequence, but its evidence code indicates computational annotation rather than direct experimental determination.
- The reviewer-only database evidence supports the key; it was not provided to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence's hydrophobic stretches support identifying a multi-pass membrane region and can distinguish it from the clearly mismatched option A, but do not establish the exact boundaries needed to choose between the near-identical options.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The particular transmembrane boundary annotations for this protein, especially whether the helix is labeled 409..429 or 409..431.",
    "reason": "The input gives a sequence but no boundary convention or protein-specific topology annotation. General hydrophobicity reasoning can locate likely helices, but cannot robustly resolve the precise coordinates that distinguish the remaining choices."
  },
  "case_id": "transmembrane_0097",
  "expected_answer_check": {
    "evidence_ids": [
      "H5",
      "H7",
      "H9",
      "H11",
      "H13",
      "H15",
      "H17"
    ],
    "judgment": "supported",
    "reason": "The sequence matches the historical UniProt record, whose annotations list all seven transmembrane segments in choice B. These are computational annotations (ECO:0000255), not evidence of direct experimental measurement of the boundaries."
  },
  "important_caveats": [
    "The supporting annotation applies to the exact supplied sequence, but its evidence code indicates computational annotation rather than direct experimental determination.",
    "The reviewer-only database evidence supports the key; it was not provided to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "D"
    ],
    "reason": "B and D list the same regions except that D extends one predicted helix by two residues, 409..431 rather than 409..429. Without a stated boundary convention, both ranges can reasonably describe the same membrane-spanning helix."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0097",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches the historical UniProt record, whose annotations list all seven transmembrane segments in choice B. These are computational annotations (ECO:0000255), not evidence of direct experimental measurement of the boundaries.",
    "evidence_ids": ["H5", "H7", "H9", "H11", "H13", "H15", "H17"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence's hydrophobic stretches support identifying a multi-pass membrane region and can distinguish it from the clearly mismatched option A, but do not establish the exact boundaries needed to choose between the near-identical options.",
    "missing_item_specific_fact": "The particular transmembrane boundary annotations for this protein, especially whether the helix is labeled 409..429 or 409..431.",
    "reason": "The input gives a sequence but no boundary convention or protein-specific topology annotation. General hydrophobicity reasoning can locate likely helices, but cannot robustly resolve the precise coordinates that distinguish the remaining choices."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "D"],
    "reason": "B and D list the same regions except that D extends one predicted helix by two residues, 409..431 rather than 409..429. Without a stated boundary convention, both ranges can reasonably describe the same membrane-spanning helix."
  },
  "important_caveats": [
    "The supporting annotation applies to the exact supplied sequence, but its evidence code indicates computational annotation rather than direct experimental determination.",
    "The reviewer-only database evidence supports the key; it was not provided to the evaluated model."
  ]
}
```

</details>

## Before: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt annotation for Q59I63 (Zebrafish ADGRG1/GPR56, sequence matched, 648 AA) lists exactly seven transmembrane helices at 371-391, 409-429, 444-464, 472-492, 531-551, 564-586, and 596-618, matching option B precisely. However, all TM annotations carry evidence code ECO:0000255 (By similarity), indicating computational prediction by similarity to other GPCRs rather than direct experimental determination. The annotation is consistent with the expected answer but is of predicted, not experimentally validated, status.

Citations as saved: [C6](#evidence-c6), [C8](#evidence-c8), [C10](#evidence-c10), [C12](#evidence-c12), [C14](#evidence-c14), [C16](#evidence-c16), [C18](#evidence-c18), [H5](#evidence-h5), [H7](#evidence-h7), [H9](#evidence-h9), [H11](#evidence-h11), [H13](#evidence-h13), [H15](#evidence-h15), [H17](#evidence-h17).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> General GPCR biology (seven TM helices in the 7-TM bundle) eliminates option C (only six TMs) and option A (positions 730-1131 exceed the 648-residue protein length). This framework reasoning is sound. However, the critical distinction between B and D is a 2-residue difference in TM2's C-terminal boundary (ends at 429 vs 431). Both 21- and 23-residue helices fall within the normal GPCR TM length range (~19-26 residues). Distinguishing the exact boundary requires either the specific UniProt annotation or a residue-level hydropathy analysis precise enough to classify positions 430-431 as hydrophilic (extracellular loop) versus hydrophobic (TM extension), which is at the limit of reliable sequence-based inference.


**Missing item-specific fact**

> The exact residue identities at positions 430-431 and their hydrophobicity classification, or equivalently the specific database annotation boundary (TM2 = 409-429 vs 409-431), which determines whether the answer is B or D.


**Reason**

> While the 7-TM GPCR architecture and the general location of the TM bundle in the C-terminal ~250 residues are reasoning-accessible, the final B-vs-D discrimination hinges on a 2-residue boundary that is annotation-dependent. A careful hydropathy scan of the provided sequence might in principle resolve it, but the margin is too narrow for confident general-knowledge reasoning, and the correct boundary matches the specific UniProt entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "D"
]
```

> Options B and D differ only in whether TM2 ends at residue 429 or 431 (a 2-residue shift). Both lengths (21 vs 23 residues) are within the normal range for a GPCR transmembrane helix. Without the specific annotation or a definitive structural/experimental boundary, both boundaries are biologically plausible. The question wording ('correctly identifies the start and end positions') implies a single exact answer, but the 2-residue TM boundary is inherently fuzzy in prediction practice.


### Important caveats

- All seven TM annotations carry ECO:0000255 (By similarity), meaning they are computational predictions transferred from homologous GPCRs, not experimentally determined boundaries.
- The UniProt entry was first publicly released 2025-06-18 (sequence version 2); the author's source snapshot is unknown, but the sequence matches the current and historical (v119) records.
- Option A is trivially eliminable (positions exceed the 648-residue protein length), serving as a very easy distractor.
- Option C is eliminable by the well-known 7-TM GPCR architecture, making the effective discrimination a B-vs-D choice.
- The 2-residue boundary difference between B and D is within the typical uncertainty of TM prediction tools and does not reflect a functionally significant distinction.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "General GPCR biology (seven TM helices in the 7-TM bundle) eliminates option C (only six TMs) and option A (positions 730-1131 exceed the 648-residue protein length). This framework reasoning is sound. However, the critical distinction between B and D is a 2-residue difference in TM2's C-terminal boundary (ends at 429 vs 431). Both 21- and 23-residue helices fall within the normal GPCR TM length range (~19-26 residues). Distinguishing the exact boundary requires either the specific UniProt annotation or a residue-level hydropathy analysis precise enough to classify positions 430-431 as hydrophilic (extracellular loop) versus hydrophobic (TM extension), which is at the limit of reliable sequence-based inference.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The exact residue identities at positions 430-431 and their hydrophobicity classification, or equivalently the specific database annotation boundary (TM2 = 409-429 vs 409-431), which determines whether the answer is B or D.",
    "reason": "While the 7-TM GPCR architecture and the general location of the TM bundle in the C-terminal ~250 residues are reasoning-accessible, the final B-vs-D discrimination hinges on a 2-residue boundary that is annotation-dependent. A careful hydropathy scan of the provided sequence might in principle resolve it, but the margin is too narrow for confident general-knowledge reasoning, and the correct boundary matches the specific UniProt entry."
  },
  "case_id": "transmembrane_0097",
  "expected_answer_check": {
    "evidence_ids": [
      "C6",
      "C8",
      "C10",
      "C12",
      "C14",
      "C16",
      "C18",
      "H5",
      "H7",
      "H9",
      "H11",
      "H13",
      "H15",
      "H17"
    ],
    "judgment": "supported",
    "reason": "The UniProt annotation for Q59I63 (Zebrafish ADGRG1/GPR56, sequence matched, 648 AA) lists exactly seven transmembrane helices at 371-391, 409-429, 444-464, 472-492, 531-551, 564-586, and 596-618, matching option B precisely. However, all TM annotations carry evidence code ECO:0000255 (By similarity), indicating computational prediction by similarity to other GPCRs rather than direct experimental determination. The annotation is consistent with the expected answer but is of predicted, not experimentally validated, status."
  },
  "important_caveats": [
    "All seven TM annotations carry ECO:0000255 (By similarity), meaning they are computational predictions transferred from homologous GPCRs, not experimentally determined boundaries.",
    "The UniProt entry was first publicly released 2025-06-18 (sequence version 2); the author's source snapshot is unknown, but the sequence matches the current and historical (v119) records.",
    "Option A is trivially eliminable (positions exceed the 648-residue protein length), serving as a very easy distractor.",
    "Option C is eliminable by the well-known 7-TM GPCR architecture, making the effective discrimination a B-vs-D choice.",
    "The 2-residue boundary difference between B and D is within the typical uncertainty of TM prediction tools and does not reflect a functionally significant distinction."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "D"
    ],
    "reason": "Options B and D differ only in whether TM2 ends at residue 429 or 431 (a 2-residue shift). Both lengths (21 vs 23 residues) are within the normal range for a GPCR transmembrane helix. Without the specific annotation or a definitive structural/experimental boundary, both boundaries are biologically plausible. The question wording ('correctly identifies the start and end positions') implies a single exact answer, but the 2-residue TM boundary is inherently fuzzy in prediction practice."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0097",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt annotation for Q59I63 (Zebrafish ADGRG1/GPR56, sequence matched, 648 AA) lists exactly seven transmembrane helices at 371-391, 409-429, 444-464, 472-492, 531-551, 564-586, and 596-618, matching option B precisely. However, all TM annotations carry evidence code ECO:0000255 (By similarity), indicating computational prediction by similarity to other GPCRs rather than direct experimental determination. The annotation is consistent with the expected answer but is of predicted, not experimentally validated, status.",
    "evidence_ids": ["C6", "C8", "C10", "C12", "C14", "C16", "C18", "H5", "H7", "H9", "H11", "H13", "H15", "H17"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "General GPCR biology (seven TM helices in the 7-TM bundle) eliminates option C (only six TMs) and option A (positions 730-1131 exceed the 648-residue protein length). This framework reasoning is sound. However, the critical distinction between B and D is a 2-residue difference in TM2's C-terminal boundary (ends at 429 vs 431). Both 21- and 23-residue helices fall within the normal GPCR TM length range (~19-26 residues). Distinguishing the exact boundary requires either the specific UniProt annotation or a residue-level hydropathy analysis precise enough to classify positions 430-431 as hydrophilic (extracellular loop) versus hydrophobic (TM extension), which is at the limit of reliable sequence-based inference.",
    "missing_item_specific_fact": "The exact residue identities at positions 430-431 and their hydrophobicity classification, or equivalently the specific database annotation boundary (TM2 = 409-429 vs 409-431), which determines whether the answer is B or D.",
    "reason": "While the 7-TM GPCR architecture and the general location of the TM bundle in the C-terminal ~250 residues are reasoning-accessible, the final B-vs-D discrimination hinges on a 2-residue boundary that is annotation-dependent. A careful hydropathy scan of the provided sequence might in principle resolve it, but the margin is too narrow for confident general-knowledge reasoning, and the correct boundary matches the specific UniProt entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "D"],
    "reason": "Options B and D differ only in whether TM2 ends at residue 429 or 431 (a 2-residue shift). Both lengths (21 vs 23 residues) are within the normal range for a GPCR transmembrane helix. Without the specific annotation or a definitive structural/experimental boundary, both boundaries are biologically plausible. The question wording ('correctly identifies the start and end positions') implies a single exact answer, but the 2-residue TM boundary is inherently fuzzy in prediction practice."
  },
  "important_caveats": [
    "All seven TM annotations carry ECO:0000255 (By similarity), meaning they are computational predictions transferred from homologous GPCRs, not experimentally determined boundaries.",
    "The UniProt entry was first publicly released 2025-06-18 (sequence version 2); the author's source snapshot is unknown, but the sequence matches the current and historical (v119) records.",
    "Option A is trivially eliminable (positions exceed the 648-residue protein length), serving as a very easy distractor.",
    "Option C is eliminable by the well-known 7-TM GPCR architecture, making the effective discrimination a B-vs-D choice.",
    "The 2-residue boundary difference between B and D is within the typical uncertainty of TM prediction tools and does not reflect a functionally significant distinction."
  ]
}
```

</details>

## After: GPT-6 Luna

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence exactly matches the cited source sequence, whose annotations list seven transmembrane helices at the positions in B. These annotations support the key, though their evidence code is computational (ECO:0000255), not direct experimental evidence.

Citations as saved: [H5](#evidence-h5), [H7](#evidence-h7), [H9](#evidence-h9), [H11](#evidence-h11), [H13](#evidence-h13), [H15](#evidence-h15), [H17](#evidence-h17).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has a long extracellular region followed by a cluster of seven membrane-length hydrophobic segments, characteristic of a seven-transmembrane GPCR. Those segments distinguish B from C, which omits one, and from A, whose listed positions do not match the seven-helix cluster. The strong hydrophobic spans support B's boundaries over D's extension of one helix into the following basic, non-hydrophobic loop.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Family-level knowledge of GPCR architecture and recognizable hydrophobic spans in the supplied sequence meaningfully distinguish the offered choices without needing the exact protein's database record. Predicted helix boundaries can be approximate, so sequence-based reasoning does not independently establish experimental topology at every residue.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> B best matches the seven hydrophobic spans; the alternatives either omit a span, extend a span into a charged loop, or list unrelated positions.


### Important caveats

- The cited transmembrane annotations are computational predictions, not direct experimental measurements.
- Exact transmembrane boundaries may vary among prediction methods.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has a long extracellular region followed by a cluster of seven membrane-length hydrophobic segments, characteristic of a seven-transmembrane GPCR. Those segments distinguish B from C, which omits one, and from A, whose listed positions do not match the seven-helix cluster. The strong hydrophobic spans support B's boundaries over D's extension of one helix into the following basic, non-hydrophobic loop.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Family-level knowledge of GPCR architecture and recognizable hydrophobic spans in the supplied sequence meaningfully distinguish the offered choices without needing the exact protein's database record. Predicted helix boundaries can be approximate, so sequence-based reasoning does not independently establish experimental topology at every residue."
  },
  "case_id": "transmembrane_0097",
  "expected_answer_check": {
    "evidence_ids": [
      "H5",
      "H7",
      "H9",
      "H11",
      "H13",
      "H15",
      "H17"
    ],
    "judgment": "supported",
    "reason": "The sequence exactly matches the cited source sequence, whose annotations list seven transmembrane helices at the positions in B. These annotations support the key, though their evidence code is computational (ECO:0000255), not direct experimental evidence."
  },
  "important_caveats": [
    "The cited transmembrane annotations are computational predictions, not direct experimental measurements.",
    "Exact transmembrane boundaries may vary among prediction methods."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "B best matches the seven hydrophobic spans; the alternatives either omit a span, extend a span into a charged loop, or list unrelated positions."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0097",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence exactly matches the cited source sequence, whose annotations list seven transmembrane helices at the positions in B. These annotations support the key, though their evidence code is computational (ECO:0000255), not direct experimental evidence.",
    "evidence_ids": ["H5", "H7", "H9", "H11", "H13", "H15", "H17"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has a long extracellular region followed by a cluster of seven membrane-length hydrophobic segments, characteristic of a seven-transmembrane GPCR. Those segments distinguish B from C, which omits one, and from A, whose listed positions do not match the seven-helix cluster. The strong hydrophobic spans support B's boundaries over D's extension of one helix into the following basic, non-hydrophobic loop.",
    "missing_item_specific_fact": "",
    "reason": "Family-level knowledge of GPCR architecture and recognizable hydrophobic spans in the supplied sequence meaningfully distinguish the offered choices without needing the exact protein's database record. Predicted helix boundaries can be approximate, so sequence-based reasoning does not independently establish experimental topology at every residue."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "B best matches the seven hydrophobic spans; the alternatives either omit a span, extend a span into a charged loop, or list unrelated positions."
  },
  "important_caveats": [
    "The cited transmembrane annotations are computational predictions, not direct experimental measurements.",
    "Exact transmembrane boundaries may vary among prediction methods."
  ]
}
```

</details>

## After: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt annotation for Q59I63 (ADGRG1/GPR56, Zebrafish) lists exactly seven transmembrane helical segments at 371-391, 409-429, 444-464, 472-492, 531-551, 564-586, and 596-618, matching Choice B precisely. The topological domains (extracellular 25-370, cytoplasmic 392-408, extracellular 430-443, etc.) are consistent with a canonical 7-TM GPCR topology. All TM annotations carry evidence code ECO:0000255 (similarity-based/procurable), indicating computational transfer rather than experimental structure, but they are the current database annotations.

Citations as saved: [C6](#evidence-c6), [C8](#evidence-c8), [C10](#evidence-c10), [C12](#evidence-c12), [C14](#evidence-c14), [C16](#evidence-c16), [C18](#evidence-c18), [C5](#evidence-c5), [C7](#evidence-c7), [C9](#evidence-c9), [C11](#evidence-c11), [C13](#evidence-c13), [C15](#evidence-c15), [C17](#evidence-c17), [H5](#evidence-h5), [H7](#evidence-h7), [H9](#evidence-h9), [H11](#evidence-h11), [H13](#evidence-h13), [H15](#evidence-h15), [H17](#evidence-h17).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Choice A is trivially eliminated because its positions (730, 795, 845, 1111) exceed the 648-residue protein length. Choices B, C, and D all place TM helices in the C-terminal ~250 residues, consistent with the large N-terminal extracellular domain of an adhesion GPCR. The decisive transferable-knowledge step is recognizing the canonical seven-transmembrane-helix architecture of all GPCRs (rhodopsin, beta-adrenergic receptor, and hundreds of solved GPCR structures). This eliminates Choice C, which lists only six TM segments. The remaining B-vs-D distinction is a two-residue difference in TM2 (ending at 429 vs 431). In GPCRs, the extracellular loop 2 (ECL2) between TM2 and TM3 is a short hydrophilic segment that typically contains a conserved cysteine forming a disulfide bond with TM3. A model examining the input sequence at positions 430-431 can assess whether those residues are hydrophobic (extending the helix, favoring D) or hydrophilic/polar (beginning the extracellular loop, favoring B). The alternating TM/loop topology of GPCRs provides a structural framework for identifying the helix-to-loop transition, making this a legitimate sequence-analysis reasoning task rather than a memorization task.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The 7-TM GPCR architecture is a well-established, broadly transferable fact from hundreds of GPCR structures and family-level knowledge. It decisively eliminates A (out-of-range positions) and C (only 6 TMs). The B-vs-D distinction, while fine-grained (2 residues), is answerable by examining hydrophobicity at positions 430-431 in the provided sequence and applying the GPCR topology principle that extracellular loops begin with hydrophilic residues. No fact unique to this exact protein's annotation is strictly necessary.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> A is eliminated by exceeding protein length; C is eliminated by having only 6 TM helices (GPCRs have 7). The B-vs-D difference is only two residues (429 vs 431) in TM2. If residues 430-431 were borderline hydrophobic, both could be argued, but the GPCR extracellular-loop topology (hydrophilic residues, conserved ECL2 cysteine) provides a clear structural rationale for B. No other pair of options is genuinely defensible.


### Important caveats

- All UniProt TM annotations carry evidence code ECO:0000255 (similarity-based/procurable), meaning they are computational predictions transferred from homology, not experimentally determined boundaries. The exact helix termini could shift by 1-2 residues with different prediction algorithms.
- The B-vs-D distinction (2 residues in one of seven helices) is extremely fine-grained. A model relying on approximate hydropathy windows might not reliably resolve this boundary without careful residue-level analysis.
- The protein is an adhesion GPCR (ADGRG1/GPR56) with a large N-terminal extracellular domain (residues 25-370) followed by the 7-TM domain (371-618) and a short cytoplasmic tail (619-648). This architecture is consistent with the adhesion GPCR subfamily but the question does not require identifying the subfamily explicitly.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Choice A is trivially eliminated because its positions (730, 795, 845, 1111) exceed the 648-residue protein length. Choices B, C, and D all place TM helices in the C-terminal ~250 residues, consistent with the large N-terminal extracellular domain of an adhesion GPCR. The decisive transferable-knowledge step is recognizing the canonical seven-transmembrane-helix architecture of all GPCRs (rhodopsin, beta-adrenergic receptor, and hundreds of solved GPCR structures). This eliminates Choice C, which lists only six TM segments. The remaining B-vs-D distinction is a two-residue difference in TM2 (ending at 429 vs 431). In GPCRs, the extracellular loop 2 (ECL2) between TM2 and TM3 is a short hydrophilic segment that typically contains a conserved cysteine forming a disulfide bond with TM3. A model examining the input sequence at positions 430-431 can assess whether those residues are hydrophobic (extending the helix, favoring D) or hydrophilic/polar (beginning the extracellular loop, favoring B). The alternating TM/loop topology of GPCRs provides a structural framework for identifying the helix-to-loop transition, making this a legitimate sequence-analysis reasoning task rather than a memorization task.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The 7-TM GPCR architecture is a well-established, broadly transferable fact from hundreds of GPCR structures and family-level knowledge. It decisively eliminates A (out-of-range positions) and C (only 6 TMs). The B-vs-D distinction, while fine-grained (2 residues), is answerable by examining hydrophobicity at positions 430-431 in the provided sequence and applying the GPCR topology principle that extracellular loops begin with hydrophilic residues. No fact unique to this exact protein's annotation is strictly necessary."
  },
  "case_id": "transmembrane_0097",
  "expected_answer_check": {
    "evidence_ids": [
      "C6",
      "C8",
      "C10",
      "C12",
      "C14",
      "C16",
      "C18",
      "C5",
      "C7",
      "C9",
      "C11",
      "C13",
      "C15",
      "C17",
      "H5",
      "H7",
      "H9",
      "H11",
      "H13",
      "H15",
      "H17"
    ],
    "judgment": "supported",
    "reason": "The UniProt annotation for Q59I63 (ADGRG1/GPR56, Zebrafish) lists exactly seven transmembrane helical segments at 371-391, 409-429, 444-464, 472-492, 531-551, 564-586, and 596-618, matching Choice B precisely. The topological domains (extracellular 25-370, cytoplasmic 392-408, extracellular 430-443, etc.) are consistent with a canonical 7-TM GPCR topology. All TM annotations carry evidence code ECO:0000255 (similarity-based/procurable), indicating computational transfer rather than experimental structure, but they are the current database annotations."
  },
  "important_caveats": [
    "All UniProt TM annotations carry evidence code ECO:0000255 (similarity-based/procurable), meaning they are computational predictions transferred from homology, not experimentally determined boundaries. The exact helix termini could shift by 1-2 residues with different prediction algorithms.",
    "The B-vs-D distinction (2 residues in one of seven helices) is extremely fine-grained. A model relying on approximate hydropathy windows might not reliably resolve this boundary without careful residue-level analysis.",
    "The protein is an adhesion GPCR (ADGRG1/GPR56) with a large N-terminal extracellular domain (residues 25-370) followed by the 7-TM domain (371-618) and a short cytoplasmic tail (619-648). This architecture is consistent with the adhesion GPCR subfamily but the question does not require identifying the subfamily explicitly."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "A is eliminated by exceeding protein length; C is eliminated by having only 6 TM helices (GPCRs have 7). The B-vs-D difference is only two residues (429 vs 431) in TM2. If residues 430-431 were borderline hydrophobic, both could be argued, but the GPCR extracellular-loop topology (hydrophilic residues, conserved ECL2 cysteine) provides a clear structural rationale for B. No other pair of options is genuinely defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0097",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt annotation for Q59I63 (ADGRG1/GPR56, Zebrafish) lists exactly seven transmembrane helical segments at 371-391, 409-429, 444-464, 472-492, 531-551, 564-586, and 596-618, matching Choice B precisely. The topological domains (extracellular 25-370, cytoplasmic 392-408, extracellular 430-443, etc.) are consistent with a canonical 7-TM GPCR topology. All TM annotations carry evidence code ECO:0000255 (similarity-based/procurable), indicating computational transfer rather than experimental structure, but they are the current database annotations.",
    "evidence_ids": ["C6", "C8", "C10", "C12", "C14", "C16", "C18", "C5", "C7", "C9", "C11", "C13", "C15", "C17", "H5", "H7", "H9", "H11", "H13", "H15", "H17"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Choice A is trivially eliminated because its positions (730, 795, 845, 1111) exceed the 648-residue protein length. Choices B, C, and D all place TM helices in the C-terminal ~250 residues, consistent with the large N-terminal extracellular domain of an adhesion GPCR. The decisive transferable-knowledge step is recognizing the canonical seven-transmembrane-helix architecture of all GPCRs (rhodopsin, beta-adrenergic receptor, and hundreds of solved GPCR structures). This eliminates Choice C, which lists only six TM segments. The remaining B-vs-D distinction is a two-residue difference in TM2 (ending at 429 vs 431). In GPCRs, the extracellular loop 2 (ECL2) between TM2 and TM3 is a short hydrophilic segment that typically contains a conserved cysteine forming a disulfide bond with TM3. A model examining the input sequence at positions 430-431 can assess whether those residues are hydrophobic (extending the helix, favoring D) or hydrophilic/polar (beginning the extracellular loop, favoring B). The alternating TM/loop topology of GPCRs provides a structural framework for identifying the helix-to-loop transition, making this a legitimate sequence-analysis reasoning task rather than a memorization task.",
    "missing_item_specific_fact": "",
    "reason": "The 7-TM GPCR architecture is a well-established, broadly transferable fact from hundreds of GPCR structures and family-level knowledge. It decisively eliminates A (out-of-range positions) and C (only 6 TMs). The B-vs-D distinction, while fine-grained (2 residues), is answerable by examining hydrophobicity at positions 430-431 in the provided sequence and applying the GPCR topology principle that extracellular loops begin with hydrophilic residues. No fact unique to this exact protein's annotation is strictly necessary."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "A is eliminated by exceeding protein length; C is eliminated by having only 6 TM helices (GPCRs have 7). The B-vs-D difference is only two residues (429 vs 431) in TM2. If residues 430-431 were borderline hydrophobic, both could be argued, but the GPCR extracellular-loop topology (hydrophilic residues, conserved ECL2 cysteine) provides a clear structural rationale for B. No other pair of options is genuinely defensible."
  },
  "important_caveats": [
    "All UniProt TM annotations carry evidence code ECO:0000255 (similarity-based/procurable), meaning they are computational predictions transferred from homology, not experimentally determined boundaries. The exact helix termini could shift by 1-2 residues with different prediction algorithms.",
    "The B-vs-D distinction (2 residues in one of seven helices) is extremely fine-grained. A model relying on approximate hydropathy windows might not reliably resolve this boundary without careful residue-level analysis.",
    "The protein is an adhesion GPCR (ADGRG1/GPR56) with a large N-terminal extracellular domain (residues 25-370) followed by the 7-TM domain (371-618) and a short cytoplasmic tail (619-648). This architecture is consistent with the adhesion GPCR subfamily but the question does not require identifying the subfamily explicitly."
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
  "requested_accession": "Q59I63",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "benchmark_sequence_sha256": "0aeb6f4623306585d8f08066b919f9b296ac122794d0737052b31610ace39de4",
  "benchmark_sequence_length": 648,
  "current_status": "retrieved",
  "current_sequence_comparison": "matched",
  "current_entry_audit": {
    "entryVersion": 121,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2025-06-18",
    "sequenceVersion": 2
  },
  "current_uniprot_release": "2026_03",
  "current_record_sha256": "a16a326ac63664dbc4e3b324e2c1c9ff44948e77fb05c1001e3446f3a60d30fe",
  "current_source_sequence_sha256": "0aeb6f4623306585d8f08066b919f9b296ac122794d0737052b31610ace39de4",
  "current_source_sequence_length": 648,
  "historical_status": "retrieved",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "selected_historical_entry_version": 119,
  "selected_historical_version": {
    "accession": "Q59I63",
    "database": "Swiss-Prot",
    "entryVersion": 119,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "AGRG1_DANRE",
    "sequenceVersion": 2
  },
  "selected_historical_record_sha256": "b3b3944ca7d7dd4847591f08fda1ac31f6e70235cc8a188b119e1d57001755c0",
  "selected_historical_source_sequence_sha256": "0aeb6f4623306585d8f08066b919f9b296ac122794d0737052b31610ace39de4",
  "selected_historical_source_sequence_length": 648,
  "latest_at_cutoff_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 119,
      "exact_sequence_comparison": "matched",
      "sequence_version": 2
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q59I63.json)

```json
{
  "evidence_id": "C1",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q59I63.json",
  "source_sha256": "a16a326ac63664dbc4e3b324e2c1c9ff44948e77fb05c1001e3446f3a60d30fe",
  "retrieved_utc": "2026-11-02T04:31:01.992326+00:00",
  "json_pointer": "/primaryAccession",
  "excerpt": "\"Q59I63\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q59I63.json)

```json
{
  "evidence_id": "C2",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q59I63.json",
  "source_sha256": "a16a326ac63664dbc4e3b324e2c1c9ff44948e77fb05c1001e3446f3a60d30fe",
  "retrieved_utc": "2026-11-02T04:31:01.992326+00:00",
  "json_pointer": "/entryAudit",
  "excerpt": "{\"entryVersion\":121,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2025-06-18\",\"sequenceVersion\":2}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q59I63.json)

```json
{
  "evidence_id": "C3",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q59I63.json",
  "source_sha256": "a16a326ac63664dbc4e3b324e2c1c9ff44948e77fb05c1001e3446f3a60d30fe",
  "retrieved_utc": "2026-11-02T04:31:01.992326+00:00",
  "json_pointer": "/organism",
  "excerpt": "{\"commonName\":\"Zebrafish\",\"lineage\":[\"Eukaryota\",\"Metazoa\",\"Chordata\",\"Craniata\",\"Vertebrata\",\"Euteleostomi\",\"Actinopterygii\",\"Neopterygii\",\"Teleostei\",\"Ostariophysi\",\"Cypriniformes\",\"Danionidae\",\"Danioninae\",\"Danio\"],\"scientificName\":\"Danio rerio\",\"synonyms\":[\"Brachydanio rerio\"],\"taxonId\":7955}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q59I63.json)

```json
{
  "evidence_id": "C4",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q59I63.json",
  "source_sha256": "a16a326ac63664dbc4e3b324e2c1c9ff44948e77fb05c1001e3446f3a60d30fe",
  "retrieved_utc": "2026-11-02T04:31:01.992326+00:00",
  "json_pointer": "/proteinDescription",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"25607772\",\"source\":\"PubMed\"}],\"value\":\"G protein-coupled receptor 56\"}}],\"contains\":[{\"alternativeNames\":[{\"fullName\":{\"value\":\"ADGRG1 N-terminal fragment\"},\"shortNames\":[{\"value\":\"ADGRG1 NT\"}]}],\"recommendedName\":{\"fullName\":{\"value\":\"Adhesion G protein-coupled receptor G1, N-terminal fragment\"}}},{\"alternativeNames\":[{\"fullName\":{\"value\":\"ADGRG1 C-terminal fragment\"},\"shortNames\":[{\"value\":\"ADGRG1 CT\"}]}],\"recommendedName\":{\"fullName\":{\"value\":\"Adhesion G protein-coupled receptor G1, C-terminal fragment\"}}}],\"flag\":\"Precursor\",\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Adhesion G protein-coupled receptor G1\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q59I63.json)

```json
{
  "evidence_id": "C5",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q59I63.json",
  "source_sha256": "a16a326ac63664dbc4e3b324e2c1c9ff44948e77fb05c1001e3446f3a60d30fe",
  "retrieved_utc": "2026-11-02T04:31:01.992326+00:00",
  "json_pointer": "/features/4",
  "excerpt": "{\"description\":\"Extracellular\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":370},\"start\":{\"modifier\":\"EXACT\",\"value\":25}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q59I63.json)

```json
{
  "evidence_id": "C6",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q59I63.json",
  "source_sha256": "a16a326ac63664dbc4e3b324e2c1c9ff44948e77fb05c1001e3446f3a60d30fe",
  "retrieved_utc": "2026-11-02T04:31:01.992326+00:00",
  "json_pointer": "/features/5",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":391},\"start\":{\"modifier\":\"EXACT\",\"value\":371}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q59I63.json)

```json
{
  "evidence_id": "C7",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q59I63.json",
  "source_sha256": "a16a326ac63664dbc4e3b324e2c1c9ff44948e77fb05c1001e3446f3a60d30fe",
  "retrieved_utc": "2026-11-02T04:31:01.992326+00:00",
  "json_pointer": "/features/6",
  "excerpt": "{\"description\":\"Cytoplasmic\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":408},\"start\":{\"modifier\":\"EXACT\",\"value\":392}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q59I63.json)

```json
{
  "evidence_id": "C8",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q59I63.json",
  "source_sha256": "a16a326ac63664dbc4e3b324e2c1c9ff44948e77fb05c1001e3446f3a60d30fe",
  "retrieved_utc": "2026-11-02T04:31:01.992326+00:00",
  "json_pointer": "/features/7",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":429},\"start\":{\"modifier\":\"EXACT\",\"value\":409}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q59I63.json)

```json
{
  "evidence_id": "C9",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q59I63.json",
  "source_sha256": "a16a326ac63664dbc4e3b324e2c1c9ff44948e77fb05c1001e3446f3a60d30fe",
  "retrieved_utc": "2026-11-02T04:31:01.992326+00:00",
  "json_pointer": "/features/8",
  "excerpt": "{\"description\":\"Extracellular\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":443},\"start\":{\"modifier\":\"EXACT\",\"value\":430}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q59I63.json)

```json
{
  "evidence_id": "C10",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q59I63.json",
  "source_sha256": "a16a326ac63664dbc4e3b324e2c1c9ff44948e77fb05c1001e3446f3a60d30fe",
  "retrieved_utc": "2026-11-02T04:31:01.992326+00:00",
  "json_pointer": "/features/9",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":464},\"start\":{\"modifier\":\"EXACT\",\"value\":444}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q59I63.json)

```json
{
  "evidence_id": "C11",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q59I63.json",
  "source_sha256": "a16a326ac63664dbc4e3b324e2c1c9ff44948e77fb05c1001e3446f3a60d30fe",
  "retrieved_utc": "2026-11-02T04:31:01.992326+00:00",
  "json_pointer": "/features/10",
  "excerpt": "{\"description\":\"Cytoplasmic\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":471},\"start\":{\"modifier\":\"EXACT\",\"value\":465}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q59I63.json)

```json
{
  "evidence_id": "C12",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q59I63.json",
  "source_sha256": "a16a326ac63664dbc4e3b324e2c1c9ff44948e77fb05c1001e3446f3a60d30fe",
  "retrieved_utc": "2026-11-02T04:31:01.992326+00:00",
  "json_pointer": "/features/11",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":492},\"start\":{\"modifier\":\"EXACT\",\"value\":472}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C13

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q59I63.json)

```json
{
  "evidence_id": "C13",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q59I63.json",
  "source_sha256": "a16a326ac63664dbc4e3b324e2c1c9ff44948e77fb05c1001e3446f3a60d30fe",
  "retrieved_utc": "2026-11-02T04:31:01.992326+00:00",
  "json_pointer": "/features/12",
  "excerpt": "{\"description\":\"Extracellular\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":530},\"start\":{\"modifier\":\"EXACT\",\"value\":493}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C14

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q59I63.json)

```json
{
  "evidence_id": "C14",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q59I63.json",
  "source_sha256": "a16a326ac63664dbc4e3b324e2c1c9ff44948e77fb05c1001e3446f3a60d30fe",
  "retrieved_utc": "2026-11-02T04:31:01.992326+00:00",
  "json_pointer": "/features/13",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":551},\"start\":{\"modifier\":\"EXACT\",\"value\":531}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C15

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q59I63.json)

```json
{
  "evidence_id": "C15",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q59I63.json",
  "source_sha256": "a16a326ac63664dbc4e3b324e2c1c9ff44948e77fb05c1001e3446f3a60d30fe",
  "retrieved_utc": "2026-11-02T04:31:01.992326+00:00",
  "json_pointer": "/features/14",
  "excerpt": "{\"description\":\"Cytoplasmic\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":563},\"start\":{\"modifier\":\"EXACT\",\"value\":552}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C16

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q59I63.json)

```json
{
  "evidence_id": "C16",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q59I63.json",
  "source_sha256": "a16a326ac63664dbc4e3b324e2c1c9ff44948e77fb05c1001e3446f3a60d30fe",
  "retrieved_utc": "2026-11-02T04:31:01.992326+00:00",
  "json_pointer": "/features/15",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":586},\"start\":{\"modifier\":\"EXACT\",\"value\":564}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C17

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q59I63.json)

```json
{
  "evidence_id": "C17",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q59I63.json",
  "source_sha256": "a16a326ac63664dbc4e3b324e2c1c9ff44948e77fb05c1001e3446f3a60d30fe",
  "retrieved_utc": "2026-11-02T04:31:01.992326+00:00",
  "json_pointer": "/features/16",
  "excerpt": "{\"description\":\"Extracellular\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":595},\"start\":{\"modifier\":\"EXACT\",\"value\":587}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C18

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q59I63.json)

```json
{
  "evidence_id": "C18",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q59I63.json",
  "source_sha256": "a16a326ac63664dbc4e3b324e2c1c9ff44948e77fb05c1001e3446f3a60d30fe",
  "retrieved_utc": "2026-11-02T04:31:01.992326+00:00",
  "json_pointer": "/features/17",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":618},\"start\":{\"modifier\":\"EXACT\",\"value\":596}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C19

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q59I63.json)

```json
{
  "evidence_id": "C19",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q59I63.json",
  "source_sha256": "a16a326ac63664dbc4e3b324e2c1c9ff44948e77fb05c1001e3446f3a60d30fe",
  "retrieved_utc": "2026-11-02T04:31:01.992326+00:00",
  "json_pointer": "/features/18",
  "excerpt": "{\"description\":\"Cytoplasmic\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":648},\"start\":{\"modifier\":\"EXACT\",\"value\":619}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C20

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q59I63.json)

```json
{
  "evidence_id": "C20",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q59I63.json",
  "source_sha256": "a16a326ac63664dbc4e3b324e2c1c9ff44948e77fb05c1001e3446f3a60d30fe",
  "retrieved_utc": "2026-11-02T04:31:01.992326+00:00",
  "json_pointer": "/references/2",
  "excerpt": "{\"citation\":{\"authors\":[\"Ackerman S.D.\",\"Garcia C.\",\"Piao X.\",\"Gutmann D.H.\",\"Monk K.R.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"25607772\"},{\"database\":\"DOI\",\"id\":\"10.1038/ncomms7122\"}],\"citationType\":\"journal article\",\"firstPage\":\"6122\",\"id\":\"25607772\",\"journal\":\"Nat. Commun.\",\"lastPage\":\"6122\",\"publicationDate\":\"2015\",\"title\":\"The adhesion GPCR Gpr56 regulates oligodendrocyte development via interactions with Galpha12/13 and RhoA.\",\"volume\":\"6\"},\"referenceNumber\":3,\"referencePositions\":[\"FUNCTION\",\"DEVELOPMENTAL STAGE\",\"DISRUPTION PHENOTYPE\",\"MUTAGENESIS OF 325-ASN-TRP-326\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q59I63?format=txt&versions=119)

```json
{
  "evidence_id": "H1",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q59I63?format=txt&versions=119",
  "source_sha256": "b3b3944ca7d7dd4847591f08fda1ac31f6e70235cc8a188b119e1d57001755c0",
  "retrieved_utc": "2026-11-02T04:31:04.584714+00:00",
  "source_locator": "lines 1-24",
  "excerpt": "ID   AGRG1_DANRE             Reviewed;         648 AA.\nAC   Q59I63; A0A0R4IXA8; A0A8M2BDY6; F1QZM9;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   18-JUN-2025, sequence version 2.\nDT   28-JAN-2026, entry version 119.\nDE   RecName: Full=Adhesion G-protein coupled receptor G1 {ECO:0000305};\nDE   AltName: Full=G-protein coupled receptor 56 {ECO:0000303|PubMed:25607772};\nDE   Contains:\nDE     RecName: Full=Adhesion G-protein coupled receptor G1, N-terminal fragment;\nDE     AltName: Full=ADGRG1 N-terminal fragment;\nDE              Short=ADGRG1 NT;\nDE   Contains:\nDE     RecName: Full=Adhesion G-protein coupled receptor G1, C-terminal fragment;\nDE     AltName: Full=ADGRG1 C-terminal fragment;\nDE              Short=ADGRG1 CT;\nDE   Flags: Precursor;\nGN   Name=adgrg1 {ECO:0000303|PubMed:29367382,\nGN   ECO:0000312|ZFIN:ZDB-GENE-030131-3671};\nGN   Synonyms=gpr56 {ECO:0000303|PubMed:25607772};\nOS   Danio rerio (Zebrafish) (Brachydanio rerio).\nOC   Eukaryota; Metazoa; Chordata; Craniata; Vertebrata; Euteleostomi;\nOC   Actinopterygii; Neopterygii; Teleostei; Ostariophysi; Cypriniformes;\nOC   Danionidae; Danioninae; Danio.\nOX   NCBI_TaxID=7955;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 119,
  "sequence_version": 2,
  "sequence_comparison": "matched"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q59I63?format=txt&versions=119)

```json
{
  "evidence_id": "H2",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q59I63?format=txt&versions=119",
  "source_sha256": "b3b3944ca7d7dd4847591f08fda1ac31f6e70235cc8a188b119e1d57001755c0",
  "retrieved_utc": "2026-11-02T04:31:04.584714+00:00",
  "source_locator": "lines 70-77",
  "excerpt": "RN   [3]\nRP   FUNCTION, DEVELOPMENTAL STAGE, DISRUPTION PHENOTYPE, AND MUTAGENESIS OF\nRP   325-ASN-TRP-326.\nRX   PubMed=25607772; DOI=10.1038/ncomms7122;\nRA   Ackerman S.D., Garcia C., Piao X., Gutmann D.H., Monk K.R.;\nRT   \"The adhesion GPCR Gpr56 regulates oligodendrocyte development via\nRT   interactions with Galpha12/13 and RhoA.\";\nRL   Nat. Commun. 6:6122-6122(2015).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 119,
  "sequence_version": 2,
  "sequence_comparison": "matched"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q59I63?format=txt&versions=119)

```json
{
  "evidence_id": "H3",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q59I63?format=txt&versions=119",
  "source_sha256": "b3b3944ca7d7dd4847591f08fda1ac31f6e70235cc8a188b119e1d57001755c0",
  "retrieved_utc": "2026-11-02T04:31:04.584714+00:00",
  "source_locator": "lines 78-85",
  "excerpt": "RN   [4]\nRP   FUNCTION.\nRX   PubMed=29367382; DOI=10.1084/jem.20161714;\nRA   Ackerman S.D., Luo R., Poitelon Y., Mogha A., Harty B.L., D'Rozario M.,\nRA   Sanchez N.E., Lakkaraju A.K.K., Gamble P., Li J., Qu J., MacEwan M.R.,\nRA   Ray W.Z., Aguzzi A., Feltri M.L., Piao X., Monk K.R.;\nRT   \"GPR56/ADGRG1 regulates development and maintenance of peripheral myelin.\";\nRL   J. Exp. Med. 215:941-961(2018).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 119,
  "sequence_version": 2,
  "sequence_comparison": "matched"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q59I63?format=txt&versions=119)

```json
{
  "evidence_id": "H4",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q59I63?format=txt&versions=119",
  "source_sha256": "b3b3944ca7d7dd4847591f08fda1ac31f6e70235cc8a188b119e1d57001755c0",
  "retrieved_utc": "2026-11-02T04:31:04.584714+00:00",
  "source_locator": "lines 211-213",
  "excerpt": "FT   TOPO_DOM        25..370\nFT                   /note=\"Extracellular\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 119,
  "sequence_version": 2,
  "sequence_comparison": "matched"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q59I63?format=txt&versions=119)

```json
{
  "evidence_id": "H5",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q59I63?format=txt&versions=119",
  "source_sha256": "b3b3944ca7d7dd4847591f08fda1ac31f6e70235cc8a188b119e1d57001755c0",
  "retrieved_utc": "2026-11-02T04:31:04.584714+00:00",
  "source_locator": "lines 214-216",
  "excerpt": "FT   TRANSMEM        371..391\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 119,
  "sequence_version": 2,
  "sequence_comparison": "matched"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q59I63?format=txt&versions=119)

```json
{
  "evidence_id": "H6",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q59I63?format=txt&versions=119",
  "source_sha256": "b3b3944ca7d7dd4847591f08fda1ac31f6e70235cc8a188b119e1d57001755c0",
  "retrieved_utc": "2026-11-02T04:31:04.584714+00:00",
  "source_locator": "lines 217-219",
  "excerpt": "FT   TOPO_DOM        392..408\nFT                   /note=\"Cytoplasmic\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 119,
  "sequence_version": 2,
  "sequence_comparison": "matched"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q59I63?format=txt&versions=119)

```json
{
  "evidence_id": "H7",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q59I63?format=txt&versions=119",
  "source_sha256": "b3b3944ca7d7dd4847591f08fda1ac31f6e70235cc8a188b119e1d57001755c0",
  "retrieved_utc": "2026-11-02T04:31:04.584714+00:00",
  "source_locator": "lines 220-222",
  "excerpt": "FT   TRANSMEM        409..429\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 119,
  "sequence_version": 2,
  "sequence_comparison": "matched"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q59I63?format=txt&versions=119)

```json
{
  "evidence_id": "H8",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q59I63?format=txt&versions=119",
  "source_sha256": "b3b3944ca7d7dd4847591f08fda1ac31f6e70235cc8a188b119e1d57001755c0",
  "retrieved_utc": "2026-11-02T04:31:04.584714+00:00",
  "source_locator": "lines 223-225",
  "excerpt": "FT   TOPO_DOM        430..443\nFT                   /note=\"Extracellular\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 119,
  "sequence_version": 2,
  "sequence_comparison": "matched"
}
```

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q59I63?format=txt&versions=119)

```json
{
  "evidence_id": "H9",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q59I63?format=txt&versions=119",
  "source_sha256": "b3b3944ca7d7dd4847591f08fda1ac31f6e70235cc8a188b119e1d57001755c0",
  "retrieved_utc": "2026-11-02T04:31:04.584714+00:00",
  "source_locator": "lines 226-228",
  "excerpt": "FT   TRANSMEM        444..464\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 119,
  "sequence_version": 2,
  "sequence_comparison": "matched"
}
```

### Evidence H10

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q59I63?format=txt&versions=119)

```json
{
  "evidence_id": "H10",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q59I63?format=txt&versions=119",
  "source_sha256": "b3b3944ca7d7dd4847591f08fda1ac31f6e70235cc8a188b119e1d57001755c0",
  "retrieved_utc": "2026-11-02T04:31:04.584714+00:00",
  "source_locator": "lines 229-231",
  "excerpt": "FT   TOPO_DOM        465..471\nFT                   /note=\"Cytoplasmic\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 119,
  "sequence_version": 2,
  "sequence_comparison": "matched"
}
```

### Evidence H11

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q59I63?format=txt&versions=119)

```json
{
  "evidence_id": "H11",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q59I63?format=txt&versions=119",
  "source_sha256": "b3b3944ca7d7dd4847591f08fda1ac31f6e70235cc8a188b119e1d57001755c0",
  "retrieved_utc": "2026-11-02T04:31:04.584714+00:00",
  "source_locator": "lines 232-234",
  "excerpt": "FT   TRANSMEM        472..492\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 119,
  "sequence_version": 2,
  "sequence_comparison": "matched"
}
```

### Evidence H12

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q59I63?format=txt&versions=119)

```json
{
  "evidence_id": "H12",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q59I63?format=txt&versions=119",
  "source_sha256": "b3b3944ca7d7dd4847591f08fda1ac31f6e70235cc8a188b119e1d57001755c0",
  "retrieved_utc": "2026-11-02T04:31:04.584714+00:00",
  "source_locator": "lines 235-237",
  "excerpt": "FT   TOPO_DOM        493..530\nFT                   /note=\"Extracellular\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 119,
  "sequence_version": 2,
  "sequence_comparison": "matched"
}
```

### Evidence H13

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q59I63?format=txt&versions=119)

```json
{
  "evidence_id": "H13",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q59I63?format=txt&versions=119",
  "source_sha256": "b3b3944ca7d7dd4847591f08fda1ac31f6e70235cc8a188b119e1d57001755c0",
  "retrieved_utc": "2026-11-02T04:31:04.584714+00:00",
  "source_locator": "lines 238-240",
  "excerpt": "FT   TRANSMEM        531..551\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 119,
  "sequence_version": 2,
  "sequence_comparison": "matched"
}
```

### Evidence H14

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q59I63?format=txt&versions=119)

```json
{
  "evidence_id": "H14",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q59I63?format=txt&versions=119",
  "source_sha256": "b3b3944ca7d7dd4847591f08fda1ac31f6e70235cc8a188b119e1d57001755c0",
  "retrieved_utc": "2026-11-02T04:31:04.584714+00:00",
  "source_locator": "lines 241-243",
  "excerpt": "FT   TOPO_DOM        552..563\nFT                   /note=\"Cytoplasmic\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 119,
  "sequence_version": 2,
  "sequence_comparison": "matched"
}
```

### Evidence H15

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q59I63?format=txt&versions=119)

```json
{
  "evidence_id": "H15",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q59I63?format=txt&versions=119",
  "source_sha256": "b3b3944ca7d7dd4847591f08fda1ac31f6e70235cc8a188b119e1d57001755c0",
  "retrieved_utc": "2026-11-02T04:31:04.584714+00:00",
  "source_locator": "lines 244-246",
  "excerpt": "FT   TRANSMEM        564..586\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 119,
  "sequence_version": 2,
  "sequence_comparison": "matched"
}
```

### Evidence H16

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q59I63?format=txt&versions=119)

```json
{
  "evidence_id": "H16",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q59I63?format=txt&versions=119",
  "source_sha256": "b3b3944ca7d7dd4847591f08fda1ac31f6e70235cc8a188b119e1d57001755c0",
  "retrieved_utc": "2026-11-02T04:31:04.584714+00:00",
  "source_locator": "lines 247-249",
  "excerpt": "FT   TOPO_DOM        587..595\nFT                   /note=\"Extracellular\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 119,
  "sequence_version": 2,
  "sequence_comparison": "matched"
}
```

### Evidence H17

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q59I63?format=txt&versions=119)

```json
{
  "evidence_id": "H17",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q59I63?format=txt&versions=119",
  "source_sha256": "b3b3944ca7d7dd4847591f08fda1ac31f6e70235cc8a188b119e1d57001755c0",
  "retrieved_utc": "2026-11-02T04:31:04.584714+00:00",
  "source_locator": "lines 250-252",
  "excerpt": "FT   TRANSMEM        596..618\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 119,
  "sequence_version": 2,
  "sequence_comparison": "matched"
}
```

### Evidence H18

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q59I63?format=txt&versions=119)

```json
{
  "evidence_id": "H18",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q59I63?format=txt&versions=119",
  "source_sha256": "b3b3944ca7d7dd4847591f08fda1ac31f6e70235cc8a188b119e1d57001755c0",
  "retrieved_utc": "2026-11-02T04:31:04.584714+00:00",
  "source_locator": "lines 253-255",
  "excerpt": "FT   TOPO_DOM        619..648\nFT                   /note=\"Cytoplasmic\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 119,
  "sequence_version": 2,
  "sequence_comparison": "matched"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json), zero-based source row 97. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
