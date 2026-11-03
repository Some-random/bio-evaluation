# transmembrane_0054: before and after transfer clarification

[All 1,328 cases](../README.md) · [Method](../METHOD.md) · [Summary](../SUMMARY.md) · [Exact reviewer user message](../inputs/transmembrane_0054.txt)

**Task:** `transmembrane`  
**Author key, unchanged:** **D** — 17..53; 58..88; 94..129; 138..164; 181..218; 223..258; 269..297

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
MASLRGSETMCNITTSCNVDSNIDQFFQPTLYIIVIVLGFPTNCMALWAAYMQVKQKNELGIYLMNLSIADLLYITTLPLWIDYFVHHDNWIHGQVSCKLFGFIFYTNIYVSIAFLCCISVDRYLAVAHPLKFAKVRRVKTALLVSAIVWLTEIVANSAPLFHDELFQDRFNHTFCFEKYPMEPWVAGMNLYRTFLGFLAPWGIMLAAYRGILRAVRGNVSTERQEKAKIKRLALSLILIVLLCFAPYHVLLLWRSVLFLINPCDCGGEENLFGAYHVTLALTSLNCVADPILYCFVNEGARHDVGRALATLLGLFQRGKSPETLMGASITVETPLAVKKPDFYSEVKTNAYKNDIEVLKDECLQMTILSVKK

[Multiple Choices]
A. 17..53; 94..129; 138..164; 181..218; 223..258; 269..297
B. 3..23
C. 17..53; 58..88; 94..129; 135..160; 181..218; 223..258; 269..297
D. 17..53; 58..88; 94..129; 138..164; 181..218; 223..258; 269..297
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

> The supplied sequence matches the historical UniProt sequence, whose annotation lists the seven transmembrane regions exactly as in D. Those annotations cite a publication and cryo-EM structures, providing stronger support than sequence prediction alone.

Citations as saved: [H4](#evidence-h4), [H6](#evidence-h6), [H8](#evidence-h8), [H10](#evidence-h10), [H12](#evidence-h12), [H14](#evidence-h14), [H16](#evidence-h16).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has several hydrophobic stretches consistent with membrane-spanning helices, including 58–88, which rules against A and B. Around the fourth span, the basic-rich sequence preceding the hydrophobic stretch supports D over C, which extends into that basic region and truncates the span.


**Missing item-specific fact**

> No item-specific fact is necessary for a meaningful sequence-based choice, though an experimental structure or annotation would better establish exact helix boundaries.


**Reason**

> The sequence and choices provide a biological basis for distinguishing D. Exact transmembrane boundaries can be uncertain from sequence alone, but the competing ranges differ in ways that hydrophobicity and the charged loop help resolve.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The endpoints are predictions rather than inherently sharp boundaries, but the sequence features and listed ranges support D as the best choice.


### Important caveats

- The reviewer-only UniProt evidence supports the key but was not supplied to the evaluated model.
- The cited annotation is tied to a matched sequence and cites publication and structural evidence; the exact author-side source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has several hydrophobic stretches consistent with membrane-spanning helices, including 58–88, which rules against A and B. Around the fourth span, the basic-rich sequence preceding the hydrophobic stretch supports D over C, which extends into that basic region and truncates the span.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "No item-specific fact is necessary for a meaningful sequence-based choice, though an experimental structure or annotation would better establish exact helix boundaries.",
    "reason": "The sequence and choices provide a biological basis for distinguishing D. Exact transmembrane boundaries can be uncertain from sequence alone, but the competing ranges differ in ways that hydrophobicity and the charged loop help resolve."
  },
  "case_id": "transmembrane_0054",
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
    "reason": "The supplied sequence matches the historical UniProt sequence, whose annotation lists the seven transmembrane regions exactly as in D. Those annotations cite a publication and cryo-EM structures, providing stronger support than sequence prediction alone."
  },
  "important_caveats": [
    "The reviewer-only UniProt evidence supports the key but was not supplied to the evaluated model.",
    "The cited annotation is tied to a matched sequence and cites publication and structural evidence; the exact author-side source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The endpoints are predictions rather than inherently sharp boundaries, but the sequence features and listed ranges support D as the best choice."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0054",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence matches the historical UniProt sequence, whose annotation lists the seven transmembrane regions exactly as in D. Those annotations cite a publication and cryo-EM structures, providing stronger support than sequence prediction alone.",
    "evidence_ids": ["H4", "H6", "H8", "H10", "H12", "H14", "H16"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has several hydrophobic stretches consistent with membrane-spanning helices, including 58–88, which rules against A and B. Around the fourth span, the basic-rich sequence preceding the hydrophobic stretch supports D over C, which extends into that basic region and truncates the span.",
    "missing_item_specific_fact": "No item-specific fact is necessary for a meaningful sequence-based choice, though an experimental structure or annotation would better establish exact helix boundaries.",
    "reason": "The sequence and choices provide a biological basis for distinguishing D. Exact transmembrane boundaries can be uncertain from sequence alone, but the competing ranges differ in ways that hydrophobicity and the charged loop help resolve."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The endpoints are predictions rather than inherently sharp boundaries, but the sequence features and listed ranges support D as the best choice."
  },
  "important_caveats": [
    "The reviewer-only UniProt evidence supports the key but was not supplied to the evaluated model.",
    "The cited annotation is tied to a matched sequence and cites publication and structural evidence; the exact author-side source snapshot is unknown."
  ]
}
```

</details>

## Before: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry E7FEL0 (Zebrafish GPR4) annotates exactly seven transmembrane helices at positions 17-53, 58-88, 94-129, 138-164, 181-218, 223-258, and 269-297, matching option D precisely. These annotations carry experimental evidence codes (ECO:0000269 from PubMed:39799123 and ECO:0007744 from PDB structures 8ZFZ and 9J31, a 3.05 Å cryo-EM structure of the activated GPR4-Gs complex), constituting structural experimental determination rather than mere computational prediction.

Citations as saved: [C6](#evidence-c6), [C8](#evidence-c8), [C10](#evidence-c10), [C12](#evidence-c12), [C14](#evidence-c14), [C16](#evidence-c16), [C18](#evidence-c18), [C20](#evidence-c20), [H4](#evidence-h4), [H6](#evidence-h6), [H8](#evidence-h8), [H10](#evidence-h10), [H12](#evidence-h12), [H14](#evidence-h14), [H16](#evidence-h16).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> General GPCR knowledge (7-TM topology) and the positive-inside rule (favoring K135 and R137 in the cytoplasmic loop rather than within TM4) can eliminate options A (only 6 TM regions) and B (single 21-residue segment), and weakly favor D over C. However, the C-vs-D distinction hinges on a 3-residue boundary (TM4 start at 135 vs 138), where hydrophobicity scores for K(-3.9), V(4.2), R(-4.5) are mixed and a sliding-window predictor could reasonably place the boundary at either position. The positive-inside rule is a statistical tendency (~60-70%), not a hard rule, and R138 itself (the first residue in D's TM4) is also charged, weakening the argument.


**Missing item-specific fact**

> The exact cryo-EM-determined boundary of TM4 (residue 138 vs 135) as resolved in PDB structures 8ZFZ/9J31. No sequence-based hydrophobicity heuristic or general topological rule can definitively resolve a 3-residue boundary difference in a region with mixed hydrophobicity.


**Reason**

> While recognizing 7 TM domains and applying the positive-inside rule narrows choices from four to two, the final C-vs-D discrimination depends on the precise structural annotation from cryo-EM data not derivable from sequence alone. The 3-residue shift in TM4 start is within the uncertainty of any hydrophobicity-based prediction method.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Although C and D differ by only 3 residues in TM4 start, the positive-inside rule provides a mild but not definitive preference for D. No other option pair is equally defensible: A omits an obvious 31-residue hydrophobic helix (TM2), and B is a trivially short single segment. The question wording ('correctly identifies the start and end positions') implies a single exact answer, which aligns with the structural annotation.


### Important caveats

- The TM boundaries are from a 2025 cryo-EM structure (Nat. Commun. 16:605), which postdates the benchmark sequence's original 2011 submission. The author's source snapshot is unknown; if constructed before mid-2025, the annotation basis may have been computational (e.g., a TM prediction tool) rather than experimental.
- The reviewer-only UniProt accession (E7FEL0) was inferred from dataset metadata and was not provided to the evaluated model; the model must work from sequence alone.
- The positive-inside rule argument for D over C is suggestive but not conclusive; a model applying rigorous hydrophobicity windowing could plausibly select C.
- The sequence matches the canonical UniProt entry exactly (SHA-256 confirmed), so numbering is unambiguous.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "General GPCR knowledge (7-TM topology) and the positive-inside rule (favoring K135 and R137 in the cytoplasmic loop rather than within TM4) can eliminate options A (only 6 TM regions) and B (single 21-residue segment), and weakly favor D over C. However, the C-vs-D distinction hinges on a 3-residue boundary (TM4 start at 135 vs 138), where hydrophobicity scores for K(-3.9), V(4.2), R(-4.5) are mixed and a sliding-window predictor could reasonably place the boundary at either position. The positive-inside rule is a statistical tendency (~60-70%), not a hard rule, and R138 itself (the first residue in D's TM4) is also charged, weakening the argument.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The exact cryo-EM-determined boundary of TM4 (residue 138 vs 135) as resolved in PDB structures 8ZFZ/9J31. No sequence-based hydrophobicity heuristic or general topological rule can definitively resolve a 3-residue boundary difference in a region with mixed hydrophobicity.",
    "reason": "While recognizing 7 TM domains and applying the positive-inside rule narrows choices from four to two, the final C-vs-D discrimination depends on the precise structural annotation from cryo-EM data not derivable from sequence alone. The 3-residue shift in TM4 start is within the uncertainty of any hydrophobicity-based prediction method."
  },
  "case_id": "transmembrane_0054",
  "expected_answer_check": {
    "evidence_ids": [
      "C6",
      "C8",
      "C10",
      "C12",
      "C14",
      "C16",
      "C18",
      "C20",
      "H4",
      "H6",
      "H8",
      "H10",
      "H12",
      "H14",
      "H16"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry E7FEL0 (Zebrafish GPR4) annotates exactly seven transmembrane helices at positions 17-53, 58-88, 94-129, 138-164, 181-218, 223-258, and 269-297, matching option D precisely. These annotations carry experimental evidence codes (ECO:0000269 from PubMed:39799123 and ECO:0007744 from PDB structures 8ZFZ and 9J31, a 3.05 Å cryo-EM structure of the activated GPR4-Gs complex), constituting structural experimental determination rather than mere computational prediction."
  },
  "important_caveats": [
    "The TM boundaries are from a 2025 cryo-EM structure (Nat. Commun. 16:605), which postdates the benchmark sequence's original 2011 submission. The author's source snapshot is unknown; if constructed before mid-2025, the annotation basis may have been computational (e.g., a TM prediction tool) rather than experimental.",
    "The reviewer-only UniProt accession (E7FEL0) was inferred from dataset metadata and was not provided to the evaluated model; the model must work from sequence alone.",
    "The positive-inside rule argument for D over C is suggestive but not conclusive; a model applying rigorous hydrophobicity windowing could plausibly select C.",
    "The sequence matches the canonical UniProt entry exactly (SHA-256 confirmed), so numbering is unambiguous."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although C and D differ by only 3 residues in TM4 start, the positive-inside rule provides a mild but not definitive preference for D. No other option pair is equally defensible: A omits an obvious 31-residue hydrophobic helix (TM2), and B is a trivially short single segment. The question wording ('correctly identifies the start and end positions') implies a single exact answer, which aligns with the structural annotation."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0054",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry E7FEL0 (Zebrafish GPR4) annotates exactly seven transmembrane helices at positions 17-53, 58-88, 94-129, 138-164, 181-218, 223-258, and 269-297, matching option D precisely. These annotations carry experimental evidence codes (ECO:0000269 from PubMed:39799123 and ECO:0007744 from PDB structures 8ZFZ and 9J31, a 3.05 Å cryo-EM structure of the activated GPR4-Gs complex), constituting structural experimental determination rather than mere computational prediction.",
    "evidence_ids": ["C6", "C8", "C10", "C12", "C14", "C16", "C18", "C20", "H4", "H6", "H8", "H10", "H12", "H14", "H16"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "General GPCR knowledge (7-TM topology) and the positive-inside rule (favoring K135 and R137 in the cytoplasmic loop rather than within TM4) can eliminate options A (only 6 TM regions) and B (single 21-residue segment), and weakly favor D over C. However, the C-vs-D distinction hinges on a 3-residue boundary (TM4 start at 135 vs 138), where hydrophobicity scores for K(-3.9), V(4.2), R(-4.5) are mixed and a sliding-window predictor could reasonably place the boundary at either position. The positive-inside rule is a statistical tendency (~60-70%), not a hard rule, and R138 itself (the first residue in D's TM4) is also charged, weakening the argument.",
    "missing_item_specific_fact": "The exact cryo-EM-determined boundary of TM4 (residue 138 vs 135) as resolved in PDB structures 8ZFZ/9J31. No sequence-based hydrophobicity heuristic or general topological rule can definitively resolve a 3-residue boundary difference in a region with mixed hydrophobicity.",
    "reason": "While recognizing 7 TM domains and applying the positive-inside rule narrows choices from four to two, the final C-vs-D discrimination depends on the precise structural annotation from cryo-EM data not derivable from sequence alone. The 3-residue shift in TM4 start is within the uncertainty of any hydrophobicity-based prediction method."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although C and D differ by only 3 residues in TM4 start, the positive-inside rule provides a mild but not definitive preference for D. No other option pair is equally defensible: A omits an obvious 31-residue hydrophobic helix (TM2), and B is a trivially short single segment. The question wording ('correctly identifies the start and end positions') implies a single exact answer, which aligns with the structural annotation."
  },
  "important_caveats": [
    "The TM boundaries are from a 2025 cryo-EM structure (Nat. Commun. 16:605), which postdates the benchmark sequence's original 2011 submission. The author's source snapshot is unknown; if constructed before mid-2025, the annotation basis may have been computational (e.g., a TM prediction tool) rather than experimental.",
    "The reviewer-only UniProt accession (E7FEL0) was inferred from dataset metadata and was not provided to the evaluated model; the model must work from sequence alone.",
    "The positive-inside rule argument for D over C is suggestive but not conclusive; a model applying rigorous hydrophobicity windowing could plausibly select C.",
    "The sequence matches the canonical UniProt entry exactly (SHA-256 confirmed), so numbering is unambiguous."
  ]
}
```

</details>

## After: GPT-6 Luna

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence-matched UniProt annotation assigns all seven listed transmembrane helices the coordinates in D. The helix annotations cite a publication and PDB structures; this supports the key as a database annotation with experimental-structure evidence, though the excerpts do not independently validate the underlying experiments.

Citations as saved: [C6](#evidence-c6), [C8](#evidence-c8), [C10](#evidence-c10), [C12](#evidence-c12), [C14](#evidence-c14), [C16](#evidence-c16), [C18](#evidence-c18).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence has several hydrophobic stretches consistent with a seven-transmembrane GPCR, so transferable GPCR knowledge supports rejecting B and recognizing that A omits a likely helix. But C and D share the same seven-helix pattern and differ only in the boundaries assigned to one helix.


**Missing item-specific fact**

> The exact boundary annotation for the helix represented as 135..160 in C versus 138..164 in D.


**Reason**

> Family-level recognition and hydropathy identify the membrane-spanning core, but do not meaningfully settle these alternative boundary conventions for the same helix. Selecting the keyed range requires the specific boundary assignment, rather than merely recognizing a GPCR.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "C",
  "D"
]
```

> Both ranges include the same likely transmembrane core; the sequence alone does not establish whether the helix should be delimited as 135..160 or 138..164.


### Important caveats

- The reviewer-only evidence matches the supplied sequence, but the author's exact source snapshot is unknown.
- Transmembrane boundaries, particularly at helix ends, can depend on annotation conventions and structural interpretation.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has several hydrophobic stretches consistent with a seven-transmembrane GPCR, so transferable GPCR knowledge supports rejecting B and recognizing that A omits a likely helix. But C and D share the same seven-helix pattern and differ only in the boundaries assigned to one helix.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The exact boundary annotation for the helix represented as 135..160 in C versus 138..164 in D.",
    "reason": "Family-level recognition and hydropathy identify the membrane-spanning core, but do not meaningfully settle these alternative boundary conventions for the same helix. Selecting the keyed range requires the specific boundary assignment, rather than merely recognizing a GPCR."
  },
  "case_id": "transmembrane_0054",
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
    "reason": "The sequence-matched UniProt annotation assigns all seven listed transmembrane helices the coordinates in D. The helix annotations cite a publication and PDB structures; this supports the key as a database annotation with experimental-structure evidence, though the excerpts do not independently validate the underlying experiments."
  },
  "important_caveats": [
    "The reviewer-only evidence matches the supplied sequence, but the author's exact source snapshot is unknown.",
    "Transmembrane boundaries, particularly at helix ends, can depend on annotation conventions and structural interpretation."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "C",
      "D"
    ],
    "reason": "Both ranges include the same likely transmembrane core; the sequence alone does not establish whether the helix should be delimited as 135..160 or 138..164."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0054",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation assigns all seven listed transmembrane helices the coordinates in D. The helix annotations cite a publication and PDB structures; this supports the key as a database annotation with experimental-structure evidence, though the excerpts do not independently validate the underlying experiments.",
    "evidence_ids": ["C6", "C8", "C10", "C12", "C14", "C16", "C18"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence has several hydrophobic stretches consistent with a seven-transmembrane GPCR, so transferable GPCR knowledge supports rejecting B and recognizing that A omits a likely helix. But C and D share the same seven-helix pattern and differ only in the boundaries assigned to one helix.",
    "missing_item_specific_fact": "The exact boundary annotation for the helix represented as 135..160 in C versus 138..164 in D.",
    "reason": "Family-level recognition and hydropathy identify the membrane-spanning core, but do not meaningfully settle these alternative boundary conventions for the same helix. Selecting the keyed range requires the specific boundary assignment, rather than merely recognizing a GPCR."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["C", "D"],
    "reason": "Both ranges include the same likely transmembrane core; the sequence alone does not establish whether the helix should be delimited as 135..160 or 138..164."
  },
  "important_caveats": [
    "The reviewer-only evidence matches the supplied sequence, but the author's exact source snapshot is unknown.",
    "Transmembrane boundaries, particularly at helix ends, can depend on annotation conventions and structural interpretation."
  ]
}
```

</details>

## After: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt annotation for this protein (GPR4, zebrafish) lists exactly seven transmembrane helices at 17..53, 58..88, 94..129, 138..164, 181..218, 223..258, and 269..297, each supported by experimental evidence (cryo-EM structures PDB 8ZFZ and 9J31, and mutagenesis data from PubMed 39799123). This matches Choice D exactly.

Citations as saved: [C6](#evidence-c6), [C8](#evidence-c8), [C10](#evidence-c10), [C12](#evidence-c12), [C14](#evidence-c14), [C16](#evidence-c16), [C18](#evidence-c18).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains the GPCR DRY motif (D122-R123-Y124) at the end of TM3, confirming the 7-TM-helix GPCR architecture, which eliminates A (only 6 segments) and B (single short segment). Between C and D, the difference is TM4 boundaries: C gives 135..160, D gives 138..164. Transferable GPCR knowledge provides a meaningful probabilistic argument favoring D: (1) At the intracellular end, positions 135-137 contain K-V-R (3 of 4 residues charged), which is atypical even for a TM helix boundary; starting at R138-V139-K140-T141 is more consistent with the snorkeling pattern seen at GPCR TM helix intracellular termini. (2) At the extracellular end, positions 161-162 are L-F (strongly hydrophobic), which would be unusual in an extracellular loop but consistent with a TM helix hydrophobic core; ending at D164 is consistent with the common extracellular snorkeling pattern (Asp/Glu at the outer boundary). (3) ICL2 length: 130-137 (8 residues, Choice D) is within the typical 4-10 residue range for GPCR ICL2, while 130-134 (5 residues, Choice C) is also plausible but the charged cluster K135-R137 argues against including them in the helix. These family-level structural principles (snorkeling, hydrophobic core continuity, loop length constraints) provide a credible basis to favor D over C, though the distinction is subtle.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The GPCR family identification (DRY motif, 7-TM topology) eliminates A and B. The C vs D distinction relies on hydrophobicity profiling and GPCR structural conventions (snorkeling at helix termini, hydrophobic core continuity, ICL2/ECL2 length constraints) learned from the broader GPCR family. While the 3-residue difference at each TM4 boundary is subtle, the charged-residue cluster at 135-137 and the hydrophobic L-F at 161-162 provide a transferable probabilistic argument favoring D.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> A and B are clearly eliminated by the 7-TM GPCR architecture. C and D differ only in TM4 boundaries (135..160 vs 138..164). While the distinction is subtle, the hydrophobicity profile and GPCR structural conventions provide a reasonable basis to favor D. No other options are equally defensible.


### Important caveats

- The C vs D distinction (TM4: 135..160 vs 138..164) is subtle and within the typical uncertainty range of computational TM prediction tools. The correct boundaries were determined by cryo-EM structure (PDB 8ZFZ/9J31), which provides atomic-level resolution not available from sequence alone.
- The reviewer-only evidence confirms the sequence matches UniProt E7FEL0 (GPR4_DANRE, zebrafish), but this identification was not available to the evaluated model.
- A model relying solely on hydrophobicity scales might produce TM4 boundaries closer to C; the argument favoring D depends on GPCR-specific structural conventions (snorkeling, loop constraints) rather than a simple hydropathy threshold.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains the GPCR DRY motif (D122-R123-Y124) at the end of TM3, confirming the 7-TM-helix GPCR architecture, which eliminates A (only 6 segments) and B (single short segment). Between C and D, the difference is TM4 boundaries: C gives 135..160, D gives 138..164. Transferable GPCR knowledge provides a meaningful probabilistic argument favoring D: (1) At the intracellular end, positions 135-137 contain K-V-R (3 of 4 residues charged), which is atypical even for a TM helix boundary; starting at R138-V139-K140-T141 is more consistent with the snorkeling pattern seen at GPCR TM helix intracellular termini. (2) At the extracellular end, positions 161-162 are L-F (strongly hydrophobic), which would be unusual in an extracellular loop but consistent with a TM helix hydrophobic core; ending at D164 is consistent with the common extracellular snorkeling pattern (Asp/Glu at the outer boundary). (3) ICL2 length: 130-137 (8 residues, Choice D) is within the typical 4-10 residue range for GPCR ICL2, while 130-134 (5 residues, Choice C) is also plausible but the charged cluster K135-R137 argues against including them in the helix. These family-level structural principles (snorkeling, hydrophobic core continuity, loop length constraints) provide a credible basis to favor D over C, though the distinction is subtle.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The GPCR family identification (DRY motif, 7-TM topology) eliminates A and B. The C vs D distinction relies on hydrophobicity profiling and GPCR structural conventions (snorkeling at helix termini, hydrophobic core continuity, ICL2/ECL2 length constraints) learned from the broader GPCR family. While the 3-residue difference at each TM4 boundary is subtle, the charged-residue cluster at 135-137 and the hydrophobic L-F at 161-162 provide a transferable probabilistic argument favoring D."
  },
  "case_id": "transmembrane_0054",
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
    "reason": "The UniProt annotation for this protein (GPR4, zebrafish) lists exactly seven transmembrane helices at 17..53, 58..88, 94..129, 138..164, 181..218, 223..258, and 269..297, each supported by experimental evidence (cryo-EM structures PDB 8ZFZ and 9J31, and mutagenesis data from PubMed 39799123). This matches Choice D exactly."
  },
  "important_caveats": [
    "The C vs D distinction (TM4: 135..160 vs 138..164) is subtle and within the typical uncertainty range of computational TM prediction tools. The correct boundaries were determined by cryo-EM structure (PDB 8ZFZ/9J31), which provides atomic-level resolution not available from sequence alone.",
    "The reviewer-only evidence confirms the sequence matches UniProt E7FEL0 (GPR4_DANRE, zebrafish), but this identification was not available to the evaluated model.",
    "A model relying solely on hydrophobicity scales might produce TM4 boundaries closer to C; the argument favoring D depends on GPCR-specific structural conventions (snorkeling, loop constraints) rather than a simple hydropathy threshold."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "A and B are clearly eliminated by the 7-TM GPCR architecture. C and D differ only in TM4 boundaries (135..160 vs 138..164). While the distinction is subtle, the hydrophobicity profile and GPCR structural conventions provide a reasonable basis to favor D. No other options are equally defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0054",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt annotation for this protein (GPR4, zebrafish) lists exactly seven transmembrane helices at 17..53, 58..88, 94..129, 138..164, 181..218, 223..258, and 269..297, each supported by experimental evidence (cryo-EM structures PDB 8ZFZ and 9J31, and mutagenesis data from PubMed 39799123). This matches Choice D exactly.",
    "evidence_ids": ["C6", "C8", "C10", "C12", "C14", "C16", "C18"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains the GPCR DRY motif (D122-R123-Y124) at the end of TM3, confirming the 7-TM-helix GPCR architecture, which eliminates A (only 6 segments) and B (single short segment). Between C and D, the difference is TM4 boundaries: C gives 135..160, D gives 138..164. Transferable GPCR knowledge provides a meaningful probabilistic argument favoring D: (1) At the intracellular end, positions 135-137 contain K-V-R (3 of 4 residues charged), which is atypical even for a TM helix boundary; starting at R138-V139-K140-T141 is more consistent with the snorkeling pattern seen at GPCR TM helix intracellular termini. (2) At the extracellular end, positions 161-162 are L-F (strongly hydrophobic), which would be unusual in an extracellular loop but consistent with a TM helix hydrophobic core; ending at D164 is consistent with the common extracellular snorkeling pattern (Asp/Glu at the outer boundary). (3) ICL2 length: 130-137 (8 residues, Choice D) is within the typical 4-10 residue range for GPCR ICL2, while 130-134 (5 residues, Choice C) is also plausible but the charged cluster K135-R137 argues against including them in the helix. These family-level structural principles (snorkeling, hydrophobic core continuity, loop length constraints) provide a credible basis to favor D over C, though the distinction is subtle.",
    "missing_item_specific_fact": "",
    "reason": "The GPCR family identification (DRY motif, 7-TM topology) eliminates A and B. The C vs D distinction relies on hydrophobicity profiling and GPCR structural conventions (snorkeling at helix termini, hydrophobic core continuity, ICL2/ECL2 length constraints) learned from the broader GPCR family. While the 3-residue difference at each TM4 boundary is subtle, the charged-residue cluster at 135-137 and the hydrophobic L-F at 161-162 provide a transferable probabilistic argument favoring D."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "A and B are clearly eliminated by the 7-TM GPCR architecture. C and D differ only in TM4 boundaries (135..160 vs 138..164). While the distinction is subtle, the hydrophobicity profile and GPCR structural conventions provide a reasonable basis to favor D. No other options are equally defensible."
  },
  "important_caveats": [
    "The C vs D distinction (TM4: 135..160 vs 138..164) is subtle and within the typical uncertainty range of computational TM prediction tools. The correct boundaries were determined by cryo-EM structure (PDB 8ZFZ/9J31), which provides atomic-level resolution not available from sequence alone.",
    "The reviewer-only evidence confirms the sequence matches UniProt E7FEL0 (GPR4_DANRE, zebrafish), but this identification was not available to the evaluated model.",
    "A model relying solely on hydrophobicity scales might produce TM4 boundaries closer to C; the argument favoring D depends on GPCR-specific structural conventions (snorkeling, loop constraints) rather than a simple hydropathy threshold."
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
  "requested_accession": "E7FEL0",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "benchmark_sequence_sha256": "08d2e4cbf983015ea5196294c41c8bc68ce217495899f0359fa842fabc71f413",
  "benchmark_sequence_length": 373,
  "current_status": "retrieved",
  "current_sequence_comparison": "matched",
  "current_entry_audit": {
    "entryVersion": 101,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2011-03-08",
    "sequenceVersion": 1
  },
  "current_uniprot_release": "2026_03",
  "current_record_sha256": "36f6ec0f1f41e3c4a3ba2109b2d762f3c0f2e896b891b1172156f642628c0dd4",
  "current_source_sequence_sha256": "08d2e4cbf983015ea5196294c41c8bc68ce217495899f0359fa842fabc71f413",
  "current_source_sequence_length": 373,
  "historical_status": "retrieved",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "selected_historical_entry_version": 99,
  "selected_historical_version": {
    "accession": "E7FEL0",
    "database": "Swiss-Prot",
    "entryVersion": 99,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "GPR4_DANRE",
    "sequenceVersion": 1
  },
  "selected_historical_record_sha256": "77459f384ab3083be302beb8cb4cd600b88183275fff5fbc110a53c59c8454b1",
  "selected_historical_source_sequence_sha256": "08d2e4cbf983015ea5196294c41c8bc68ce217495899f0359fa842fabc71f413",
  "selected_historical_source_sequence_length": 373,
  "latest_at_cutoff_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 99,
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E7FEL0.json)

```json
{
  "evidence_id": "C1",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/E7FEL0.json",
  "source_sha256": "36f6ec0f1f41e3c4a3ba2109b2d762f3c0f2e896b891b1172156f642628c0dd4",
  "retrieved_utc": "2026-11-02T04:28:01.793515+00:00",
  "json_pointer": "/primaryAccession",
  "excerpt": "\"E7FEL0\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E7FEL0.json)

```json
{
  "evidence_id": "C2",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/E7FEL0.json",
  "source_sha256": "36f6ec0f1f41e3c4a3ba2109b2d762f3c0f2e896b891b1172156f642628c0dd4",
  "retrieved_utc": "2026-11-02T04:28:01.793515+00:00",
  "json_pointer": "/entryAudit",
  "excerpt": "{\"entryVersion\":101,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2011-03-08\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E7FEL0.json)

```json
{
  "evidence_id": "C3",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/E7FEL0.json",
  "source_sha256": "36f6ec0f1f41e3c4a3ba2109b2d762f3c0f2e896b891b1172156f642628c0dd4",
  "retrieved_utc": "2026-11-02T04:28:01.793515+00:00",
  "json_pointer": "/organism",
  "excerpt": "{\"commonName\":\"Zebrafish\",\"lineage\":[\"Eukaryota\",\"Metazoa\",\"Chordata\",\"Craniata\",\"Vertebrata\",\"Euteleostomi\",\"Actinopterygii\",\"Neopterygii\",\"Teleostei\",\"Ostariophysi\",\"Cypriniformes\",\"Danionidae\",\"Danioninae\",\"Danio\"],\"scientificName\":\"Danio rerio\",\"synonyms\":[\"Brachydanio rerio\"],\"taxonId\":7955}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E7FEL0.json)

```json
{
  "evidence_id": "C4",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/E7FEL0.json",
  "source_sha256": "36f6ec0f1f41e3c4a3ba2109b2d762f3c0f2e896b891b1172156f642628c0dd4",
  "retrieved_utc": "2026-11-02T04:28:01.793515+00:00",
  "json_pointer": "/proteinDescription",
  "excerpt": "{\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39799123\",\"source\":\"PubMed\"}],\"value\":\"G protein-coupled receptor 4\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39799123\",\"source\":\"PubMed\"}],\"value\":\"zGPR4\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E7FEL0.json)

```json
{
  "evidence_id": "C5",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/E7FEL0.json",
  "source_sha256": "36f6ec0f1f41e3c4a3ba2109b2d762f3c0f2e896b891b1172156f642628c0dd4",
  "retrieved_utc": "2026-11-02T04:28:01.793515+00:00",
  "json_pointer": "/features/1",
  "excerpt": "{\"description\":\"Extracellular\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39799123\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8ZFZ\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"9J31\",\"source\":\"PDB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":16},\"start\":{\"modifier\":\"EXACT\",\"value\":1}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E7FEL0.json)

```json
{
  "evidence_id": "C6",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/E7FEL0.json",
  "source_sha256": "36f6ec0f1f41e3c4a3ba2109b2d762f3c0f2e896b891b1172156f642628c0dd4",
  "retrieved_utc": "2026-11-02T04:28:01.793515+00:00",
  "json_pointer": "/features/2",
  "excerpt": "{\"description\":\"Helical; Name=1\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39799123\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8ZFZ\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"9J31\",\"source\":\"PDB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":53},\"start\":{\"modifier\":\"EXACT\",\"value\":17}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E7FEL0.json)

```json
{
  "evidence_id": "C7",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/E7FEL0.json",
  "source_sha256": "36f6ec0f1f41e3c4a3ba2109b2d762f3c0f2e896b891b1172156f642628c0dd4",
  "retrieved_utc": "2026-11-02T04:28:01.793515+00:00",
  "json_pointer": "/features/3",
  "excerpt": "{\"description\":\"Cytoplasmic\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39799123\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8ZFZ\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"9J31\",\"source\":\"PDB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":57},\"start\":{\"modifier\":\"EXACT\",\"value\":54}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E7FEL0.json)

```json
{
  "evidence_id": "C8",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/E7FEL0.json",
  "source_sha256": "36f6ec0f1f41e3c4a3ba2109b2d762f3c0f2e896b891b1172156f642628c0dd4",
  "retrieved_utc": "2026-11-02T04:28:01.793515+00:00",
  "json_pointer": "/features/4",
  "excerpt": "{\"description\":\"Helical; Name=2\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39799123\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8ZFZ\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"9J31\",\"source\":\"PDB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":88},\"start\":{\"modifier\":\"EXACT\",\"value\":58}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E7FEL0.json)

```json
{
  "evidence_id": "C9",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/E7FEL0.json",
  "source_sha256": "36f6ec0f1f41e3c4a3ba2109b2d762f3c0f2e896b891b1172156f642628c0dd4",
  "retrieved_utc": "2026-11-02T04:28:01.793515+00:00",
  "json_pointer": "/features/5",
  "excerpt": "{\"description\":\"Extracellular\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39799123\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8ZFZ\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"9J31\",\"source\":\"PDB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":93},\"start\":{\"modifier\":\"EXACT\",\"value\":89}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E7FEL0.json)

```json
{
  "evidence_id": "C10",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/E7FEL0.json",
  "source_sha256": "36f6ec0f1f41e3c4a3ba2109b2d762f3c0f2e896b891b1172156f642628c0dd4",
  "retrieved_utc": "2026-11-02T04:28:01.793515+00:00",
  "json_pointer": "/features/6",
  "excerpt": "{\"description\":\"Helical; Name=3\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39799123\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8ZFZ\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"9J31\",\"source\":\"PDB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":129},\"start\":{\"modifier\":\"EXACT\",\"value\":94}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E7FEL0.json)

```json
{
  "evidence_id": "C11",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/E7FEL0.json",
  "source_sha256": "36f6ec0f1f41e3c4a3ba2109b2d762f3c0f2e896b891b1172156f642628c0dd4",
  "retrieved_utc": "2026-11-02T04:28:01.793515+00:00",
  "json_pointer": "/features/7",
  "excerpt": "{\"description\":\"Cytoplasmic\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39799123\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8ZFZ\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"9J31\",\"source\":\"PDB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":137},\"start\":{\"modifier\":\"EXACT\",\"value\":130}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E7FEL0.json)

```json
{
  "evidence_id": "C12",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/E7FEL0.json",
  "source_sha256": "36f6ec0f1f41e3c4a3ba2109b2d762f3c0f2e896b891b1172156f642628c0dd4",
  "retrieved_utc": "2026-11-02T04:28:01.793515+00:00",
  "json_pointer": "/features/8",
  "excerpt": "{\"description\":\"Helical; Name=4\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39799123\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8ZFZ\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"9J31\",\"source\":\"PDB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":164},\"start\":{\"modifier\":\"EXACT\",\"value\":138}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C13

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E7FEL0.json)

```json
{
  "evidence_id": "C13",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/E7FEL0.json",
  "source_sha256": "36f6ec0f1f41e3c4a3ba2109b2d762f3c0f2e896b891b1172156f642628c0dd4",
  "retrieved_utc": "2026-11-02T04:28:01.793515+00:00",
  "json_pointer": "/features/9",
  "excerpt": "{\"description\":\"Extracellular\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39799123\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8ZFZ\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"9J31\",\"source\":\"PDB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":180},\"start\":{\"modifier\":\"EXACT\",\"value\":165}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C14

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E7FEL0.json)

```json
{
  "evidence_id": "C14",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/E7FEL0.json",
  "source_sha256": "36f6ec0f1f41e3c4a3ba2109b2d762f3c0f2e896b891b1172156f642628c0dd4",
  "retrieved_utc": "2026-11-02T04:28:01.793515+00:00",
  "json_pointer": "/features/10",
  "excerpt": "{\"description\":\"Helical; Name=5\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39799123\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8ZFZ\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"9J31\",\"source\":\"PDB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":218},\"start\":{\"modifier\":\"EXACT\",\"value\":181}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C15

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E7FEL0.json)

```json
{
  "evidence_id": "C15",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/E7FEL0.json",
  "source_sha256": "36f6ec0f1f41e3c4a3ba2109b2d762f3c0f2e896b891b1172156f642628c0dd4",
  "retrieved_utc": "2026-11-02T04:28:01.793515+00:00",
  "json_pointer": "/features/11",
  "excerpt": "{\"description\":\"Cytoplasmic\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39799123\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8ZFZ\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"9J31\",\"source\":\"PDB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":222},\"start\":{\"modifier\":\"EXACT\",\"value\":219}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C16

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E7FEL0.json)

```json
{
  "evidence_id": "C16",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/E7FEL0.json",
  "source_sha256": "36f6ec0f1f41e3c4a3ba2109b2d762f3c0f2e896b891b1172156f642628c0dd4",
  "retrieved_utc": "2026-11-02T04:28:01.793515+00:00",
  "json_pointer": "/features/12",
  "excerpt": "{\"description\":\"Helical; Name=6\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39799123\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8ZFZ\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"9J31\",\"source\":\"PDB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":258},\"start\":{\"modifier\":\"EXACT\",\"value\":223}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C17

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E7FEL0.json)

```json
{
  "evidence_id": "C17",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/E7FEL0.json",
  "source_sha256": "36f6ec0f1f41e3c4a3ba2109b2d762f3c0f2e896b891b1172156f642628c0dd4",
  "retrieved_utc": "2026-11-02T04:28:01.793515+00:00",
  "json_pointer": "/features/13",
  "excerpt": "{\"description\":\"Extracellular\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39799123\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8ZFZ\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"9J31\",\"source\":\"PDB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":268},\"start\":{\"modifier\":\"EXACT\",\"value\":259}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C18

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E7FEL0.json)

```json
{
  "evidence_id": "C18",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/E7FEL0.json",
  "source_sha256": "36f6ec0f1f41e3c4a3ba2109b2d762f3c0f2e896b891b1172156f642628c0dd4",
  "retrieved_utc": "2026-11-02T04:28:01.793515+00:00",
  "json_pointer": "/features/14",
  "excerpt": "{\"description\":\"Helical; Name=7\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39799123\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8ZFZ\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"9J31\",\"source\":\"PDB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":297},\"start\":{\"modifier\":\"EXACT\",\"value\":269}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C19

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E7FEL0.json)

```json
{
  "evidence_id": "C19",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/E7FEL0.json",
  "source_sha256": "36f6ec0f1f41e3c4a3ba2109b2d762f3c0f2e896b891b1172156f642628c0dd4",
  "retrieved_utc": "2026-11-02T04:28:01.793515+00:00",
  "json_pointer": "/features/15",
  "excerpt": "{\"description\":\"Cytoplasmic\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":373},\"start\":{\"modifier\":\"EXACT\",\"value\":298}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C20

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E7FEL0.json)

```json
{
  "evidence_id": "C20",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/E7FEL0.json",
  "source_sha256": "36f6ec0f1f41e3c4a3ba2109b2d762f3c0f2e896b891b1172156f642628c0dd4",
  "retrieved_utc": "2026-11-02T04:28:01.793515+00:00",
  "json_pointer": "/references/1",
  "excerpt": "{\"citation\":{\"authors\":[\"Ma Y.\",\"Wang Y.\",\"Tang M.\",\"Weng Y.\",\"Chen Y.\",\"Xu Y.\",\"An S.\",\"Wu Y.\",\"Zhao S.\",\"Xu H.\",\"Li D.\",\"Liu M.\",\"Lu W.\",\"Ru H.\",\"Song G.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"39799123\"},{\"database\":\"DOI\",\"id\":\"10.1038/s41467-025-55901-2\"}],\"citationType\":\"journal article\",\"firstPage\":\"605\",\"id\":\"39799123\",\"journal\":\"Nat. Commun.\",\"lastPage\":\"605\",\"publicationDate\":\"2025\",\"title\":\"Cryo-EM structure of an activated GPR4-Gs signaling complex.\",\"volume\":\"16\"},\"evidences\":[{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8ZFZ\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"9J31\",\"source\":\"PDB\"}],\"referenceNumber\":2,\"referencePositions\":[\"STRUCTURE BY ELECTRON MICROSCOPY (3.05 ANGSTROMS) OF 2-360 IN COMPLEX WITH GNAS\",\"FUNCTION\",\"MUTAGENESIS OF GLN-53; ASN-58; GLU-59; ASP-71; HIS-87; ASP-89; TYR-106; TYR-110; ARG-123; ARG-137; 164-ASP-GLU-165; HIS-173; GLU-178; ASN-219; GLU-226; TYR-248; TYR-276; HIS-277; ASP-290 AND GLU-299\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E7FEL0?format=txt&versions=99)

```json
{
  "evidence_id": "H1",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/E7FEL0?format=txt&versions=99",
  "source_sha256": "77459f384ab3083be302beb8cb4cd600b88183275fff5fbc110a53c59c8454b1",
  "retrieved_utc": "2026-11-02T04:28:05.185174+00:00",
  "source_locator": "lines 1-14",
  "excerpt": "ID   GPR4_DANRE              Reviewed;         373 AA.\nAC   E7FEL0; A0A8M2B4J4;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   08-MAR-2011, sequence version 1.\nDT   28-JAN-2026, entry version 99.\nDE   RecName: Full=G-protein coupled receptor 4 {ECO:0000303|PubMed:39799123};\nDE            Short=zGPR4 {ECO:0000303|PubMed:39799123};\nGN   Name=gpr4 {ECO:0000303|PubMed:39799123,\nGN   ECO:0000312|ZFIN:ZDB-GENE-101202-1};\nOS   Danio rerio (Zebrafish) (Brachydanio rerio).\nOC   Eukaryota; Metazoa; Chordata; Craniata; Vertebrata; Euteleostomi;\nOC   Actinopterygii; Neopterygii; Teleostei; Ostariophysi; Cypriniformes;\nOC   Danionidae; Danioninae; Danio.\nOX   NCBI_TaxID=7955;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 99,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E7FEL0?format=txt&versions=99)

```json
{
  "evidence_id": "H2",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/E7FEL0?format=txt&versions=99",
  "source_sha256": "77459f384ab3083be302beb8cb4cd600b88183275fff5fbc110a53c59c8454b1",
  "retrieved_utc": "2026-11-02T04:28:05.185174+00:00",
  "source_locator": "lines 52-61",
  "excerpt": "RN   [2] {ECO:0007744|PDB:8ZFZ, ECO:0007744|PDB:9J31}\nRP   STRUCTURE BY ELECTRON MICROSCOPY (3.05 ANGSTROMS) OF 2-360 IN COMPLEX WITH\nRP   GNAS, FUNCTION, AND MUTAGENESIS OF GLN-53; ASN-58; GLU-59; ASP-71; HIS-87;\nRP   ASP-89; TYR-106; TYR-110; ARG-123; ARG-137; 164-ASP-GLU-165; HIS-173;\nRP   GLU-178; ASN-219; GLU-226; TYR-248; TYR-276; HIS-277; ASP-290 AND GLU-299.\nRX   PubMed=39799123; DOI=10.1038/s41467-025-55901-2;\nRA   Ma Y., Wang Y., Tang M., Weng Y., Chen Y., Xu Y., An S., Wu Y., Zhao S.,\nRA   Xu H., Li D., Liu M., Lu W., Ru H., Song G.;\nRT   \"Cryo-EM structure of an activated GPR4-Gs signaling complex.\";\nRL   Nat. Commun. 16:605-605(2025).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 99,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E7FEL0?format=txt&versions=99)

```json
{
  "evidence_id": "H3",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/E7FEL0?format=txt&versions=99",
  "source_sha256": "77459f384ab3083be302beb8cb4cd600b88183275fff5fbc110a53c59c8454b1",
  "retrieved_utc": "2026-11-02T04:28:05.185174+00:00",
  "source_locator": "lines 144-147",
  "excerpt": "FT   TOPO_DOM        1..16\nFT                   /note=\"Extracellular\"\nFT                   /evidence=\"ECO:0000269|PubMed:39799123,\nFT                   ECO:0007744|PDB:8ZFZ, ECO:0007744|PDB:9J31\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 99,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E7FEL0?format=txt&versions=99)

```json
{
  "evidence_id": "H4",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/E7FEL0?format=txt&versions=99",
  "source_sha256": "77459f384ab3083be302beb8cb4cd600b88183275fff5fbc110a53c59c8454b1",
  "retrieved_utc": "2026-11-02T04:28:05.185174+00:00",
  "source_locator": "lines 148-151",
  "excerpt": "FT   TRANSMEM        17..53\nFT                   /note=\"Helical; Name=1\"\nFT                   /evidence=\"ECO:0000269|PubMed:39799123,\nFT                   ECO:0007744|PDB:8ZFZ, ECO:0007744|PDB:9J31\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 99,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E7FEL0?format=txt&versions=99)

```json
{
  "evidence_id": "H5",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/E7FEL0?format=txt&versions=99",
  "source_sha256": "77459f384ab3083be302beb8cb4cd600b88183275fff5fbc110a53c59c8454b1",
  "retrieved_utc": "2026-11-02T04:28:05.185174+00:00",
  "source_locator": "lines 152-155",
  "excerpt": "FT   TOPO_DOM        54..57\nFT                   /note=\"Cytoplasmic\"\nFT                   /evidence=\"ECO:0000269|PubMed:39799123,\nFT                   ECO:0007744|PDB:8ZFZ, ECO:0007744|PDB:9J31\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 99,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E7FEL0?format=txt&versions=99)

```json
{
  "evidence_id": "H6",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/E7FEL0?format=txt&versions=99",
  "source_sha256": "77459f384ab3083be302beb8cb4cd600b88183275fff5fbc110a53c59c8454b1",
  "retrieved_utc": "2026-11-02T04:28:05.185174+00:00",
  "source_locator": "lines 156-159",
  "excerpt": "FT   TRANSMEM        58..88\nFT                   /note=\"Helical; Name=2\"\nFT                   /evidence=\"ECO:0000269|PubMed:39799123,\nFT                   ECO:0007744|PDB:8ZFZ, ECO:0007744|PDB:9J31\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 99,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E7FEL0?format=txt&versions=99)

```json
{
  "evidence_id": "H7",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/E7FEL0?format=txt&versions=99",
  "source_sha256": "77459f384ab3083be302beb8cb4cd600b88183275fff5fbc110a53c59c8454b1",
  "retrieved_utc": "2026-11-02T04:28:05.185174+00:00",
  "source_locator": "lines 160-163",
  "excerpt": "FT   TOPO_DOM        89..93\nFT                   /note=\"Extracellular\"\nFT                   /evidence=\"ECO:0000269|PubMed:39799123,\nFT                   ECO:0007744|PDB:8ZFZ, ECO:0007744|PDB:9J31\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 99,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E7FEL0?format=txt&versions=99)

```json
{
  "evidence_id": "H8",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/E7FEL0?format=txt&versions=99",
  "source_sha256": "77459f384ab3083be302beb8cb4cd600b88183275fff5fbc110a53c59c8454b1",
  "retrieved_utc": "2026-11-02T04:28:05.185174+00:00",
  "source_locator": "lines 164-167",
  "excerpt": "FT   TRANSMEM        94..129\nFT                   /note=\"Helical; Name=3\"\nFT                   /evidence=\"ECO:0000269|PubMed:39799123,\nFT                   ECO:0007744|PDB:8ZFZ, ECO:0007744|PDB:9J31\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 99,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E7FEL0?format=txt&versions=99)

```json
{
  "evidence_id": "H9",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/E7FEL0?format=txt&versions=99",
  "source_sha256": "77459f384ab3083be302beb8cb4cd600b88183275fff5fbc110a53c59c8454b1",
  "retrieved_utc": "2026-11-02T04:28:05.185174+00:00",
  "source_locator": "lines 168-171",
  "excerpt": "FT   TOPO_DOM        130..137\nFT                   /note=\"Cytoplasmic\"\nFT                   /evidence=\"ECO:0000269|PubMed:39799123,\nFT                   ECO:0007744|PDB:8ZFZ, ECO:0007744|PDB:9J31\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 99,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H10

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E7FEL0?format=txt&versions=99)

```json
{
  "evidence_id": "H10",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/E7FEL0?format=txt&versions=99",
  "source_sha256": "77459f384ab3083be302beb8cb4cd600b88183275fff5fbc110a53c59c8454b1",
  "retrieved_utc": "2026-11-02T04:28:05.185174+00:00",
  "source_locator": "lines 172-175",
  "excerpt": "FT   TRANSMEM        138..164\nFT                   /note=\"Helical; Name=4\"\nFT                   /evidence=\"ECO:0000269|PubMed:39799123,\nFT                   ECO:0007744|PDB:8ZFZ, ECO:0007744|PDB:9J31\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 99,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H11

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E7FEL0?format=txt&versions=99)

```json
{
  "evidence_id": "H11",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/E7FEL0?format=txt&versions=99",
  "source_sha256": "77459f384ab3083be302beb8cb4cd600b88183275fff5fbc110a53c59c8454b1",
  "retrieved_utc": "2026-11-02T04:28:05.185174+00:00",
  "source_locator": "lines 176-179",
  "excerpt": "FT   TOPO_DOM        165..180\nFT                   /note=\"Extracellular\"\nFT                   /evidence=\"ECO:0000269|PubMed:39799123,\nFT                   ECO:0007744|PDB:8ZFZ, ECO:0007744|PDB:9J31\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 99,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H12

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E7FEL0?format=txt&versions=99)

```json
{
  "evidence_id": "H12",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/E7FEL0?format=txt&versions=99",
  "source_sha256": "77459f384ab3083be302beb8cb4cd600b88183275fff5fbc110a53c59c8454b1",
  "retrieved_utc": "2026-11-02T04:28:05.185174+00:00",
  "source_locator": "lines 180-183",
  "excerpt": "FT   TRANSMEM        181..218\nFT                   /note=\"Helical; Name=5\"\nFT                   /evidence=\"ECO:0000269|PubMed:39799123,\nFT                   ECO:0007744|PDB:8ZFZ, ECO:0007744|PDB:9J31\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 99,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H13

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E7FEL0?format=txt&versions=99)

```json
{
  "evidence_id": "H13",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/E7FEL0?format=txt&versions=99",
  "source_sha256": "77459f384ab3083be302beb8cb4cd600b88183275fff5fbc110a53c59c8454b1",
  "retrieved_utc": "2026-11-02T04:28:05.185174+00:00",
  "source_locator": "lines 184-187",
  "excerpt": "FT   TOPO_DOM        219..222\nFT                   /note=\"Cytoplasmic\"\nFT                   /evidence=\"ECO:0000269|PubMed:39799123,\nFT                   ECO:0007744|PDB:8ZFZ, ECO:0007744|PDB:9J31\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 99,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H14

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E7FEL0?format=txt&versions=99)

```json
{
  "evidence_id": "H14",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/E7FEL0?format=txt&versions=99",
  "source_sha256": "77459f384ab3083be302beb8cb4cd600b88183275fff5fbc110a53c59c8454b1",
  "retrieved_utc": "2026-11-02T04:28:05.185174+00:00",
  "source_locator": "lines 188-191",
  "excerpt": "FT   TRANSMEM        223..258\nFT                   /note=\"Helical; Name=6\"\nFT                   /evidence=\"ECO:0000269|PubMed:39799123,\nFT                   ECO:0007744|PDB:8ZFZ, ECO:0007744|PDB:9J31\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 99,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H15

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E7FEL0?format=txt&versions=99)

```json
{
  "evidence_id": "H15",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/E7FEL0?format=txt&versions=99",
  "source_sha256": "77459f384ab3083be302beb8cb4cd600b88183275fff5fbc110a53c59c8454b1",
  "retrieved_utc": "2026-11-02T04:28:05.185174+00:00",
  "source_locator": "lines 192-195",
  "excerpt": "FT   TOPO_DOM        259..268\nFT                   /note=\"Extracellular\"\nFT                   /evidence=\"ECO:0000269|PubMed:39799123,\nFT                   ECO:0007744|PDB:8ZFZ, ECO:0007744|PDB:9J31\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 99,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H16

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E7FEL0?format=txt&versions=99)

```json
{
  "evidence_id": "H16",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/E7FEL0?format=txt&versions=99",
  "source_sha256": "77459f384ab3083be302beb8cb4cd600b88183275fff5fbc110a53c59c8454b1",
  "retrieved_utc": "2026-11-02T04:28:05.185174+00:00",
  "source_locator": "lines 196-199",
  "excerpt": "FT   TRANSMEM        269..297\nFT                   /note=\"Helical; Name=7\"\nFT                   /evidence=\"ECO:0000269|PubMed:39799123,\nFT                   ECO:0007744|PDB:8ZFZ, ECO:0007744|PDB:9J31\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 99,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H17

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E7FEL0?format=txt&versions=99)

```json
{
  "evidence_id": "H17",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/E7FEL0?format=txt&versions=99",
  "source_sha256": "77459f384ab3083be302beb8cb4cd600b88183275fff5fbc110a53c59c8454b1",
  "retrieved_utc": "2026-11-02T04:28:05.185174+00:00",
  "source_locator": "lines 200-202",
  "excerpt": "FT   TOPO_DOM        298..373\nFT                   /note=\"Cytoplasmic\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 99,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json), zero-based source row 54. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
