# transmembrane_0032: before and after transfer clarification

[All 1,328 cases](../README.md) · [Method](../METHOD.md) · [Summary](../SUMMARY.md) · [Exact reviewer user message](../inputs/transmembrane_0032.txt)

**Task:** `transmembrane`  
**Author key, unchanged:** **C** — 12..28

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
MGLLRIMMPPKLQLLAVVAFAVAMLFLENQIQKLEESRAKLERAIARHEVREIEQRHTMDGPRQDAAVDEEEDIVIIYNRVPKTASTSFTNIAYDLCAKNRYHVLHINTTKNNPVMSLQDQVRFVKNITTWNEMKPGFYHGHISYLDFAKFGVKKKPIYINVIRDPIERLVSYYYFLRFGDDYRPGLRRRKQGDKKTFDECVAEGGSDCAPEKLWLQIPFFCGHSSECWNVGSRWAMDQAKYNLINEYFLVGVTEELEDFIMLLEAALPRFFRGATDLYRTGKKSHLRKTTEKKLPTKQTIAKLQQSDIWKMENEFYEFALEQFQFIRAHAVREKDGDLYILAQNFFYEKIYPKSN

[Multiple Choices]
A. 2709..2729
B. 12..28; 531..556
C. 12..28
D. 15..29
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

> The sequence-matched UniProt record annotates residues 12–28 as a helical transmembrane signal-anchor. The annotation is computational (ECO:0000255), not direct experimental evidence, but it supports the keyed answer.

Citations as saved: [C6](#evidence-c6), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The N-terminus contains a conspicuously hydrophobic stretch consistent with a membrane-spanning signal-anchor, distinguishing it from the out-of-range choices. That supports the region broadly, but does not establish its precise endpoints.


**Missing item-specific fact**

> The protein-specific transmembrane boundary annotation, or equivalent evidence establishing the exact endpoints 12 and 28, is absent from the input.


**Reason**

> Sequence-based reasoning can identify the likely N-terminal membrane helix, but cannot reliably distinguish the annotated 12–28 span from the overlapping 15–29 candidate at residue-level precision.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "C",
  "D"
]
```

> Both choices overlap the same hydrophobic N-terminal segment; D could describe a plausible membrane-spanning core, even though the sequence-matched annotation specifies C.


### Important caveats

- The supporting annotation is computational rather than direct experimental evidence.
- The supplied sequence matches the cited canonical sequence; no construct or isoform numbering is assumed.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminus contains a conspicuously hydrophobic stretch consistent with a membrane-spanning signal-anchor, distinguishing it from the out-of-range choices. That supports the region broadly, but does not establish its precise endpoints.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific transmembrane boundary annotation, or equivalent evidence establishing the exact endpoints 12 and 28, is absent from the input.",
    "reason": "Sequence-based reasoning can identify the likely N-terminal membrane helix, but cannot reliably distinguish the annotated 12–28 span from the overlapping 15–29 candidate at residue-level precision."
  },
  "case_id": "transmembrane_0032",
  "expected_answer_check": {
    "evidence_ids": [
      "C6",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates residues 12–28 as a helical transmembrane signal-anchor. The annotation is computational (ECO:0000255), not direct experimental evidence, but it supports the keyed answer."
  },
  "important_caveats": [
    "The supporting annotation is computational rather than direct experimental evidence.",
    "The supplied sequence matches the cited canonical sequence; no construct or isoform numbering is assumed."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "C",
      "D"
    ],
    "reason": "Both choices overlap the same hydrophobic N-terminal segment; D could describe a plausible membrane-spanning core, even though the sequence-matched annotation specifies C."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0032",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates residues 12–28 as a helical transmembrane signal-anchor. The annotation is computational (ECO:0000255), not direct experimental evidence, but it supports the keyed answer.",
    "evidence_ids": ["C6", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The N-terminus contains a conspicuously hydrophobic stretch consistent with a membrane-spanning signal-anchor, distinguishing it from the out-of-range choices. That supports the region broadly, but does not establish its precise endpoints.",
    "missing_item_specific_fact": "The protein-specific transmembrane boundary annotation, or equivalent evidence establishing the exact endpoints 12 and 28, is absent from the input.",
    "reason": "Sequence-based reasoning can identify the likely N-terminal membrane helix, but cannot reliably distinguish the annotated 12–28 span from the overlapping 15–29 candidate at residue-level precision."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["C", "D"],
    "reason": "Both choices overlap the same hydrophobic N-terminal segment; D could describe a plausible membrane-spanning core, even though the sequence-matched annotation specifies C."
  },
  "important_caveats": [
    "The supporting annotation is computational rather than direct experimental evidence.",
    "The supplied sequence matches the cited canonical sequence; no construct or isoform numbering is assumed."
  ]
}
```

</details>

## Before: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A0A8C2LVE3 (HS2ST_CRIGR, Chinese hamster Heparan sulfate 2-O-sulfotransferase 1) annotates a single transmembrane helix at positions 12..28, described as a 'Helical; Signal-anchor for type II membrane protein' (evidence C6/H3). The sequence at 12-28 (LQLLAVVAFAVAMLFLE) is predominantly hydrophobic, consistent with a TM alpha-helix. The flanking topology (cytoplasmic 1-11, lumenal 29-356) is also annotated (C5, C7). The evidence code is ECO:0000255 (similarity-based, transferred from a homolog), so the boundaries are computationally inferred rather than experimentally measured, but the annotation is consistent with the sequence's hydrophobic profile.

Citations as saved: [C6](#evidence-c6), [H3](#evidence-h3), [C5](#evidence-c5), [C7](#evidence-c7), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Options A (2709..2729) and B (531..556 component) are trivially eliminated as they exceed the 356-residue sequence length. The real distinction is C (12..28) vs D (15..29). The positive-inside rule provides a concrete argument: residue K(11) is the last positively charged residue before the hydrophobic stretch, consistent with the cytoplasmic boundary at position 11 and TM onset at position 12. Additionally, the hydrophobic core L(12)-L(27) is contiguous and strongly hydrophobic (LQ-L-L-A-V-V-A-F-A-V-A-M-L-F-L), while option D's inclusion of N(29) extends into the clearly polar/charged lumenal domain (NQIQKLEESR…). Option C's endpoint at E(28) sits at the membrane-water interface, a common boundary residue for TM helices.


**Missing item-specific fact**

> The exact TM helix boundary is inherently uncertain to ±2-3 residues without experimental data (the annotation uses ECO:0000255 similarity evidence). However, the positive-inside rule and hydrophobicity profile provide defensible general reasoning to prefer C over D.


**Reason**

> While the C-vs-D margin is narrow (3-residue shift), general biological principles (positive-inside rule, hydrophobicity continuity, membrane-interface residue placement) provide meaningful grounds to distinguish them. The elimination of A and B is trivial. The question is not purely lookup-dependent, though the exact boundary precision does carry some annotation-specific uncertainty.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> A and B are eliminated by sequence-length impossibility. Between C and D, the positive-inside rule (K at position 11) and the hydrophobicity profile favor C. While the margin is small, D's inclusion of N(29) in the TM region is less consistent with the clearly polar lumenal domain starting at position 29. No other option is defensible.


### Important caveats

- The UniProt TM boundary annotation carries evidence code ECO:0000255 (similarity-based inference from a homolog), not direct experimental determination. The exact 12..28 boundaries are therefore computationally transferred and carry inherent uncertainty.
- The distinction between C (12..28) and D (15..29) is within the typical ±2-3 residue uncertainty of TM helix boundary prediction. A model relying solely on hydrophobicity windows might not confidently separate these.
- The protein is a type II membrane protein with a single signal-anchor TM; this topology is correctly reflected in the sequence (short N-terminal cytoplasmic tail, long C-terminal lumenal catalytic domain).
- The reviewer-only evidence confirms sequence match (SHA-256 identical) between the benchmark sequence and the UniProt entry, so the annotation applies directly to the supplied sequence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Options A (2709..2729) and B (531..556 component) are trivially eliminated as they exceed the 356-residue sequence length. The real distinction is C (12..28) vs D (15..29). The positive-inside rule provides a concrete argument: residue K(11) is the last positively charged residue before the hydrophobic stretch, consistent with the cytoplasmic boundary at position 11 and TM onset at position 12. Additionally, the hydrophobic core L(12)-L(27) is contiguous and strongly hydrophobic (LQ-L-L-A-V-V-A-F-A-V-A-M-L-F-L), while option D's inclusion of N(29) extends into the clearly polar/charged lumenal domain (NQIQKLEESR…). Option C's endpoint at E(28) sits at the membrane-water interface, a common boundary residue for TM helices.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The exact TM helix boundary is inherently uncertain to ±2-3 residues without experimental data (the annotation uses ECO:0000255 similarity evidence). However, the positive-inside rule and hydrophobicity profile provide defensible general reasoning to prefer C over D.",
    "reason": "While the C-vs-D margin is narrow (3-residue shift), general biological principles (positive-inside rule, hydrophobicity continuity, membrane-interface residue placement) provide meaningful grounds to distinguish them. The elimination of A and B is trivial. The question is not purely lookup-dependent, though the exact boundary precision does carry some annotation-specific uncertainty."
  },
  "case_id": "transmembrane_0032",
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
    "reason": "The UniProt entry A0A8C2LVE3 (HS2ST_CRIGR, Chinese hamster Heparan sulfate 2-O-sulfotransferase 1) annotates a single transmembrane helix at positions 12..28, described as a 'Helical; Signal-anchor for type II membrane protein' (evidence C6/H3). The sequence at 12-28 (LQLLAVVAFAVAMLFLE) is predominantly hydrophobic, consistent with a TM alpha-helix. The flanking topology (cytoplasmic 1-11, lumenal 29-356) is also annotated (C5, C7). The evidence code is ECO:0000255 (similarity-based, transferred from a homolog), so the boundaries are computationally inferred rather than experimentally measured, but the annotation is consistent with the sequence's hydrophobic profile."
  },
  "important_caveats": [
    "The UniProt TM boundary annotation carries evidence code ECO:0000255 (similarity-based inference from a homolog), not direct experimental determination. The exact 12..28 boundaries are therefore computationally transferred and carry inherent uncertainty.",
    "The distinction between C (12..28) and D (15..29) is within the typical ±2-3 residue uncertainty of TM helix boundary prediction. A model relying solely on hydrophobicity windows might not confidently separate these.",
    "The protein is a type II membrane protein with a single signal-anchor TM; this topology is correctly reflected in the sequence (short N-terminal cytoplasmic tail, long C-terminal lumenal catalytic domain).",
    "The reviewer-only evidence confirms sequence match (SHA-256 identical) between the benchmark sequence and the UniProt entry, so the annotation applies directly to the supplied sequence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "A and B are eliminated by sequence-length impossibility. Between C and D, the positive-inside rule (K at position 11) and the hydrophobicity profile favor C. While the margin is small, D's inclusion of N(29) in the TM region is less consistent with the clearly polar lumenal domain starting at position 29. No other option is defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0032",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A0A8C2LVE3 (HS2ST_CRIGR, Chinese hamster Heparan sulfate 2-O-sulfotransferase 1) annotates a single transmembrane helix at positions 12..28, described as a 'Helical; Signal-anchor for type II membrane protein' (evidence C6/H3). The sequence at 12-28 (LQLLAVVAFAVAMLFLE) is predominantly hydrophobic, consistent with a TM alpha-helix. The flanking topology (cytoplasmic 1-11, lumenal 29-356) is also annotated (C5, C7). The evidence code is ECO:0000255 (similarity-based, transferred from a homolog), so the boundaries are computationally inferred rather than experimentally measured, but the annotation is consistent with the sequence's hydrophobic profile.",
    "evidence_ids": ["C6", "H3", "C5", "C7", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Options A (2709..2729) and B (531..556 component) are trivially eliminated as they exceed the 356-residue sequence length. The real distinction is C (12..28) vs D (15..29). The positive-inside rule provides a concrete argument: residue K(11) is the last positively charged residue before the hydrophobic stretch, consistent with the cytoplasmic boundary at position 11 and TM onset at position 12. Additionally, the hydrophobic core L(12)-L(27) is contiguous and strongly hydrophobic (LQ-L-L-A-V-V-A-F-A-V-A-M-L-F-L), while option D's inclusion of N(29) extends into the clearly polar/charged lumenal domain (NQIQKLEESR…). Option C's endpoint at E(28) sits at the membrane-water interface, a common boundary residue for TM helices.",
    "missing_item_specific_fact": "The exact TM helix boundary is inherently uncertain to ±2-3 residues without experimental data (the annotation uses ECO:0000255 similarity evidence). However, the positive-inside rule and hydrophobicity profile provide defensible general reasoning to prefer C over D.",
    "reason": "While the C-vs-D margin is narrow (3-residue shift), general biological principles (positive-inside rule, hydrophobicity continuity, membrane-interface residue placement) provide meaningful grounds to distinguish them. The elimination of A and B is trivial. The question is not purely lookup-dependent, though the exact boundary precision does carry some annotation-specific uncertainty."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "A and B are eliminated by sequence-length impossibility. Between C and D, the positive-inside rule (K at position 11) and the hydrophobicity profile favor C. While the margin is small, D's inclusion of N(29) in the TM region is less consistent with the clearly polar lumenal domain starting at position 29. No other option is defensible."
  },
  "important_caveats": [
    "The UniProt TM boundary annotation carries evidence code ECO:0000255 (similarity-based inference from a homolog), not direct experimental determination. The exact 12..28 boundaries are therefore computationally transferred and carry inherent uncertainty.",
    "The distinction between C (12..28) and D (15..29) is within the typical ±2-3 residue uncertainty of TM helix boundary prediction. A model relying solely on hydrophobicity windows might not confidently separate these.",
    "The protein is a type II membrane protein with a single signal-anchor TM; this topology is correctly reflected in the sequence (short N-terminal cytoplasmic tail, long C-terminal lumenal catalytic domain).",
    "The reviewer-only evidence confirms sequence match (SHA-256 identical) between the benchmark sequence and the UniProt entry, so the annotation applies directly to the supplied sequence."
  ]
}
```

</details>

## After: GPT-6 Luna

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence-matched UniProt annotation identifies residues 12–28 as a helical transmembrane signal-anchor. Its evidence code (ECO:0000255) indicates computational annotation, not experimental evidence.

Citations as saved: [H3](#evidence-h3), [C6](#evidence-c6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The N-terminus contains a strong hydrophobic stretch, approximately residues 12–27, consistent with a membrane-spanning signal-anchor helix. Choice C covers that stretch and its boundary; A is outside the sequence length, and B includes an impossible second segment. Compared with D, C includes more of the hydrophobic run and does not extend as far into the polar residues that follow.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Transferable knowledge about hydrophobic signal-anchor helices meaningfully favors C among the choices, though sequence-based boundary placement is approximate.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "C",
  "D"
]
```

> The hydrophobic core is shared by C and D, and the precise boundaries of a transmembrane helix are not sharply determined from sequence alone. C is better supported as the interval covering the full hydrophobic stretch, but D could plausibly describe its spanning core.


### Important caveats

- The reviewer-only annotation matches the supplied sequence, but the cited support is computational rather than experimental.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminus contains a strong hydrophobic stretch, approximately residues 12–27, consistent with a membrane-spanning signal-anchor helix. Choice C covers that stretch and its boundary; A is outside the sequence length, and B includes an impossible second segment. Compared with D, C includes more of the hydrophobic run and does not extend as far into the polar residues that follow.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Transferable knowledge about hydrophobic signal-anchor helices meaningfully favors C among the choices, though sequence-based boundary placement is approximate."
  },
  "case_id": "transmembrane_0032",
  "expected_answer_check": {
    "evidence_ids": [
      "H3",
      "C6"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation identifies residues 12–28 as a helical transmembrane signal-anchor. Its evidence code (ECO:0000255) indicates computational annotation, not experimental evidence."
  },
  "important_caveats": [
    "The reviewer-only annotation matches the supplied sequence, but the cited support is computational rather than experimental."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "C",
      "D"
    ],
    "reason": "The hydrophobic core is shared by C and D, and the precise boundaries of a transmembrane helix are not sharply determined from sequence alone. C is better supported as the interval covering the full hydrophobic stretch, but D could plausibly describe its spanning core."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0032",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation identifies residues 12–28 as a helical transmembrane signal-anchor. Its evidence code (ECO:0000255) indicates computational annotation, not experimental evidence.",
    "evidence_ids": ["H3", "C6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The N-terminus contains a strong hydrophobic stretch, approximately residues 12–27, consistent with a membrane-spanning signal-anchor helix. Choice C covers that stretch and its boundary; A is outside the sequence length, and B includes an impossible second segment. Compared with D, C includes more of the hydrophobic run and does not extend as far into the polar residues that follow.",
    "missing_item_specific_fact": "",
    "reason": "Transferable knowledge about hydrophobic signal-anchor helices meaningfully favors C among the choices, though sequence-based boundary placement is approximate."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["C", "D"],
    "reason": "The hydrophobic core is shared by C and D, and the precise boundaries of a transmembrane helix are not sharply determined from sequence alone. C is better supported as the interval covering the full hydrophobic stretch, but D could plausibly describe its spanning core."
  },
  "important_caveats": [
    "The reviewer-only annotation matches the supplied sequence, but the cited support is computational rather than experimental."
  ]
}
```

</details>

## After: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt annotation (evidence C6, H3) records TRANSMEM 12..28 as a helical signal-anchor for a type II membrane protein, with cytoplasmic topological domain 1..11 and lumenal domain 29..356. The evidence code ECO:0000255 indicates this is a similarity-based (computational/transfer) annotation rather than direct experimental measurement, but it is consistent with the hydrophobicity profile of the sequence (LQLLAVVAFAVAMLFLE at positions 12–28 is a 17-residue hydrophobic stretch bounded by charged K11 and E28). The sequence is confirmed to match the benchmark (SHA-256 match, 356 aa).

Citations as saved: [C6](#evidence-c6), [H3](#evidence-h3), [C5](#evidence-c5), [C7](#evidence-c7).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Options A (2709..2729) and B (531..556 component) are immediately eliminated because the protein is only 356 residues long. The real distinction is C (12..28) vs D (15..29). Examining the N-terminal sequence: positions 1–11 are MGLLRIMMPPK, ending with the charged residue K11. Position 12 is L (hydrophobic), beginning a contiguous hydrophobic stretch LQLLAVVAFAVAMLFLE (12–27) that ends at E28 (charged). This charged-to-hydrophobic transition (K11→L12) and the hydrophobic-to-charged transition (L27→E28) are standard markers for TM helix boundaries in type II membrane proteins (short cytoplasmic N-term, single TM signal-anchor, lumenal body). Starting the TM at 15 would place hydrophobic leucines at positions 12 and 14 in a 'cytoplasmic' domain, which is inconsistent with the hydrophobicity profile. The 17-residue helix (12–28) is also more typical for a signal-anchor TM domain than the 15-residue alternative (15–29). Golgi-resident sulfotransferases (the HS2ST family) are well-known type II membrane proteins with this exact topology, providing transferable family-level knowledge.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A model can eliminate A and B by noting positions exceed the 356-aa protein length. Between C and D, the hydrophobicity transition from charged K11 to hydrophobic L12, the presence of two leucines (L12, L14) that would be anomalously placed in a cytoplasmic domain under option D, and the charged E28 boundary all favor C. Type II membrane protein topology (short N-terminal cytoplasmic tail, single TM, lumenal catalytic domain) is standard transferable knowledge applicable to Golgi sulfotransferases.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options A and B are eliminated by protein length. Between C and D, the hydrophobicity transition at K11→L12 and the placement of hydrophobic leucines at 12 and 14 strongly favor C. While D is not absurd, the sequence evidence and type II membrane protein topology conventions make C clearly the better answer.


### Important caveats

- The UniProt TM annotation carries evidence code ECO:0000255 (similarity to other proteins), meaning it is a computational/transfer annotation, not an experimental determination. The exact boundaries (12 vs 15 start, 28 vs 29 end) are within the typical uncertainty range of TM prediction tools.
- The benchmark sequence is confirmed to match the UniProt entry A0A8C2LVE3 (HS2ST1 from Cricetulus griseus) by SHA-256, but the organism identity was not provided to the evaluated model.
- The protein name and family (heparan sulfate 2-O-sulfotransferase) were not given in the original prompt; the model must infer type II membrane protein topology from sequence features alone or from recognizing the hydrophobic N-terminal anchor pattern.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Options A (2709..2729) and B (531..556 component) are immediately eliminated because the protein is only 356 residues long. The real distinction is C (12..28) vs D (15..29). Examining the N-terminal sequence: positions 1–11 are MGLLRIMMPPK, ending with the charged residue K11. Position 12 is L (hydrophobic), beginning a contiguous hydrophobic stretch LQLLAVVAFAVAMLFLE (12–27) that ends at E28 (charged). This charged-to-hydrophobic transition (K11→L12) and the hydrophobic-to-charged transition (L27→E28) are standard markers for TM helix boundaries in type II membrane proteins (short cytoplasmic N-term, single TM signal-anchor, lumenal body). Starting the TM at 15 would place hydrophobic leucines at positions 12 and 14 in a 'cytoplasmic' domain, which is inconsistent with the hydrophobicity profile. The 17-residue helix (12–28) is also more typical for a signal-anchor TM domain than the 15-residue alternative (15–29). Golgi-resident sulfotransferases (the HS2ST family) are well-known type II membrane proteins with this exact topology, providing transferable family-level knowledge.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A model can eliminate A and B by noting positions exceed the 356-aa protein length. Between C and D, the hydrophobicity transition from charged K11 to hydrophobic L12, the presence of two leucines (L12, L14) that would be anomalously placed in a cytoplasmic domain under option D, and the charged E28 boundary all favor C. Type II membrane protein topology (short N-terminal cytoplasmic tail, single TM, lumenal catalytic domain) is standard transferable knowledge applicable to Golgi sulfotransferases."
  },
  "case_id": "transmembrane_0032",
  "expected_answer_check": {
    "evidence_ids": [
      "C6",
      "H3",
      "C5",
      "C7"
    ],
    "judgment": "supported",
    "reason": "The UniProt annotation (evidence C6, H3) records TRANSMEM 12..28 as a helical signal-anchor for a type II membrane protein, with cytoplasmic topological domain 1..11 and lumenal domain 29..356. The evidence code ECO:0000255 indicates this is a similarity-based (computational/transfer) annotation rather than direct experimental measurement, but it is consistent with the hydrophobicity profile of the sequence (LQLLAVVAFAVAMLFLE at positions 12–28 is a 17-residue hydrophobic stretch bounded by charged K11 and E28). The sequence is confirmed to match the benchmark (SHA-256 match, 356 aa)."
  },
  "important_caveats": [
    "The UniProt TM annotation carries evidence code ECO:0000255 (similarity to other proteins), meaning it is a computational/transfer annotation, not an experimental determination. The exact boundaries (12 vs 15 start, 28 vs 29 end) are within the typical uncertainty range of TM prediction tools.",
    "The benchmark sequence is confirmed to match the UniProt entry A0A8C2LVE3 (HS2ST1 from Cricetulus griseus) by SHA-256, but the organism identity was not provided to the evaluated model.",
    "The protein name and family (heparan sulfate 2-O-sulfotransferase) were not given in the original prompt; the model must infer type II membrane protein topology from sequence features alone or from recognizing the hydrophobic N-terminal anchor pattern."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A and B are eliminated by protein length. Between C and D, the hydrophobicity transition at K11→L12 and the placement of hydrophobic leucines at 12 and 14 strongly favor C. While D is not absurd, the sequence evidence and type II membrane protein topology conventions make C clearly the better answer."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0032",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt annotation (evidence C6, H3) records TRANSMEM 12..28 as a helical signal-anchor for a type II membrane protein, with cytoplasmic topological domain 1..11 and lumenal domain 29..356. The evidence code ECO:0000255 indicates this is a similarity-based (computational/transfer) annotation rather than direct experimental measurement, but it is consistent with the hydrophobicity profile of the sequence (LQLLAVVAFAVAMLFLE at positions 12–28 is a 17-residue hydrophobic stretch bounded by charged K11 and E28). The sequence is confirmed to match the benchmark (SHA-256 match, 356 aa).",
    "evidence_ids": ["C6", "H3", "C5", "C7"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Options A (2709..2729) and B (531..556 component) are immediately eliminated because the protein is only 356 residues long. The real distinction is C (12..28) vs D (15..29). Examining the N-terminal sequence: positions 1–11 are MGLLRIMMPPK, ending with the charged residue K11. Position 12 is L (hydrophobic), beginning a contiguous hydrophobic stretch LQLLAVVAFAVAMLFLE (12–27) that ends at E28 (charged). This charged-to-hydrophobic transition (K11→L12) and the hydrophobic-to-charged transition (L27→E28) are standard markers for TM helix boundaries in type II membrane proteins (short cytoplasmic N-term, single TM signal-anchor, lumenal body). Starting the TM at 15 would place hydrophobic leucines at positions 12 and 14 in a 'cytoplasmic' domain, which is inconsistent with the hydrophobicity profile. The 17-residue helix (12–28) is also more typical for a signal-anchor TM domain than the 15-residue alternative (15–29). Golgi-resident sulfotransferases (the HS2ST family) are well-known type II membrane proteins with this exact topology, providing transferable family-level knowledge.",
    "missing_item_specific_fact": "",
    "reason": "A model can eliminate A and B by noting positions exceed the 356-aa protein length. Between C and D, the hydrophobicity transition from charged K11 to hydrophobic L12, the presence of two leucines (L12, L14) that would be anomalously placed in a cytoplasmic domain under option D, and the charged E28 boundary all favor C. Type II membrane protein topology (short N-terminal cytoplasmic tail, single TM, lumenal catalytic domain) is standard transferable knowledge applicable to Golgi sulfotransferases."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A and B are eliminated by protein length. Between C and D, the hydrophobicity transition at K11→L12 and the placement of hydrophobic leucines at 12 and 14 strongly favor C. While D is not absurd, the sequence evidence and type II membrane protein topology conventions make C clearly the better answer."
  },
  "important_caveats": [
    "The UniProt TM annotation carries evidence code ECO:0000255 (similarity to other proteins), meaning it is a computational/transfer annotation, not an experimental determination. The exact boundaries (12 vs 15 start, 28 vs 29 end) are within the typical uncertainty range of TM prediction tools.",
    "The benchmark sequence is confirmed to match the UniProt entry A0A8C2LVE3 (HS2ST1 from Cricetulus griseus) by SHA-256, but the organism identity was not provided to the evaluated model.",
    "The protein name and family (heparan sulfate 2-O-sulfotransferase) were not given in the original prompt; the model must infer type II membrane protein topology from sequence features alone or from recognizing the hydrophobic N-terminal anchor pattern."
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
  "requested_accession": "A0A8C2LVE3",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "benchmark_sequence_sha256": "a438080c10ef2ba2b4b0a97657c783c3e1a5599568ecacaea65e61097d20104d",
  "benchmark_sequence_length": 356,
  "current_status": "retrieved",
  "current_sequence_comparison": "matched",
  "current_entry_audit": {
    "entryVersion": 21,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2022-01-19",
    "sequenceVersion": 1
  },
  "current_uniprot_release": "2026_03",
  "current_record_sha256": "0d3ae0ae5ef516524f45ece4202b2e4a49d7ab8d354dec6f6098830001d44574",
  "current_source_sequence_sha256": "a438080c10ef2ba2b4b0a97657c783c3e1a5599568ecacaea65e61097d20104d",
  "current_source_sequence_length": 356,
  "historical_status": "retrieved",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "selected_historical_entry_version": 19,
  "selected_historical_version": {
    "accession": "A0A8C2LVE3",
    "database": "Swiss-Prot",
    "entryVersion": 19,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "HS2ST_CRIGR",
    "sequenceVersion": 1
  },
  "selected_historical_record_sha256": "c78db6d4bdbc3208dbc3401f5215ab34d630f3586e718f4eb0558db0f9ef4abb",
  "selected_historical_source_sequence_sha256": "a438080c10ef2ba2b4b0a97657c783c3e1a5599568ecacaea65e61097d20104d",
  "selected_historical_source_sequence_length": 356,
  "latest_at_cutoff_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 19,
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8C2LVE3.json)

```json
{
  "evidence_id": "C1",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8C2LVE3.json",
  "source_sha256": "0d3ae0ae5ef516524f45ece4202b2e4a49d7ab8d354dec6f6098830001d44574",
  "retrieved_utc": "2026-11-02T04:25:56.866768+00:00",
  "json_pointer": "/primaryAccession",
  "excerpt": "\"A0A8C2LVE3\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8C2LVE3.json)

```json
{
  "evidence_id": "C2",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8C2LVE3.json",
  "source_sha256": "0d3ae0ae5ef516524f45ece4202b2e4a49d7ab8d354dec6f6098830001d44574",
  "retrieved_utc": "2026-11-02T04:25:56.866768+00:00",
  "json_pointer": "/entryAudit",
  "excerpt": "{\"entryVersion\":21,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2022-01-19\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8C2LVE3.json)

```json
{
  "evidence_id": "C3",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8C2LVE3.json",
  "source_sha256": "0d3ae0ae5ef516524f45ece4202b2e4a49d7ab8d354dec6f6098830001d44574",
  "retrieved_utc": "2026-11-02T04:25:56.866768+00:00",
  "json_pointer": "/organism",
  "excerpt": "{\"commonName\":\"Chinese hamster\",\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP001108280\",\"source\":\"Proteomes\"}],\"lineage\":[\"Eukaryota\",\"Metazoa\",\"Chordata\",\"Craniata\",\"Vertebrata\",\"Euteleostomi\",\"Mammalia\",\"Eutheria\",\"Euarchontoglires\",\"Glires\",\"Rodentia\",\"Myomorpha\",\"Muroidea\",\"Cricetidae\",\"Cricetinae\",\"Cricetulus\"],\"scientificName\":\"Cricetulus griseus\",\"synonyms\":[\"Cricetulus barabensis griseus\"],\"taxonId\":10029}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8C2LVE3.json)

```json
{
  "evidence_id": "C4",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8C2LVE3.json",
  "source_sha256": "0d3ae0ae5ef516524f45ece4202b2e4a49d7ab8d354dec6f6098830001d44574",
  "retrieved_utc": "2026-11-02T04:25:56.866768+00:00",
  "json_pointer": "/proteinDescription",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q8R3H7\",\"source\":\"UniProtKB\"}],\"value\":\"2-O-sulfotransferase\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q8R3H7\",\"source\":\"UniProtKB\"}],\"value\":\"2-OST\"},{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q76KB1\",\"source\":\"UniProtKB\"}],\"value\":\"2OST\"}]},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q8R3H7\",\"source\":\"UniProtKB\"}],\"value\":\"HS 2-O-sulfotransferase\"}},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q8R3H7\",\"source\":\"UniProtKB\"}],\"value\":\"Heparan sulfate 2-sulfotransferase\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q8R3H7\",\"source\":\"UniProtKB\"}],\"value\":\"2.8.2.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q7LGA3\",\"source\":\"UniProtKB\"}],\"value\":\"Heparan sulfate 2-O-sulfotransferase 1\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8C2LVE3.json)

```json
{
  "evidence_id": "C5",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8C2LVE3.json",
  "source_sha256": "0d3ae0ae5ef516524f45ece4202b2e4a49d7ab8d354dec6f6098830001d44574",
  "retrieved_utc": "2026-11-02T04:25:56.866768+00:00",
  "json_pointer": "/features/1",
  "excerpt": "{\"description\":\"Cytoplasmic\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":11},\"start\":{\"modifier\":\"EXACT\",\"value\":1}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8C2LVE3.json)

```json
{
  "evidence_id": "C6",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8C2LVE3.json",
  "source_sha256": "0d3ae0ae5ef516524f45ece4202b2e4a49d7ab8d354dec6f6098830001d44574",
  "retrieved_utc": "2026-11-02T04:25:56.866768+00:00",
  "json_pointer": "/features/2",
  "excerpt": "{\"description\":\"Helical; Signal-anchor for type II membrane protein\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":28},\"start\":{\"modifier\":\"EXACT\",\"value\":12}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8C2LVE3.json)

```json
{
  "evidence_id": "C7",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8C2LVE3.json",
  "source_sha256": "0d3ae0ae5ef516524f45ece4202b2e4a49d7ab8d354dec6f6098830001d44574",
  "retrieved_utc": "2026-11-02T04:25:56.866768+00:00",
  "json_pointer": "/features/3",
  "excerpt": "{\"description\":\"Lumenal\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":356},\"start\":{\"modifier\":\"EXACT\",\"value\":29}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8C2LVE3?format=txt&versions=19)

```json
{
  "evidence_id": "H1",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A8C2LVE3?format=txt&versions=19",
  "source_sha256": "c78db6d4bdbc3208dbc3401f5215ab34d630f3586e718f4eb0558db0f9ef4abb",
  "retrieved_utc": "2026-11-02T04:26:00.260576+00:00",
  "source_locator": "lines 1-18",
  "excerpt": "ID   HS2ST_CRIGR             Reviewed;         356 AA.\nAC   A0A8C2LVE3;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   19-JAN-2022, sequence version 1.\nDT   28-JAN-2026, entry version 19.\nDE   RecName: Full=Heparan sulfate 2-O-sulfotransferase 1 {ECO:0000250|UniProtKB:Q7LGA3};\nDE            EC=2.8.2.- {ECO:0000250|UniProtKB:Q8R3H7};\nDE   AltName: Full=2-O-sulfotransferase {ECO:0000250|UniProtKB:Q8R3H7};\nDE            Short=2-OST {ECO:0000250|UniProtKB:Q8R3H7};\nDE            Short=2OST {ECO:0000250|UniProtKB:Q76KB1};\nDE   AltName: Full=HS 2-O-sulfotransferase {ECO:0000250|UniProtKB:Q8R3H7};\nDE   AltName: Full=Heparan sulfate 2-sulfotransferase {ECO:0000250|UniProtKB:Q8R3H7};\nGN   Name=HS2ST1 {ECO:0000250|UniProtKB:Q7LGA3}; Synonyms=LOC100760748;\nOS   Cricetulus griseus (Chinese hamster) (Cricetulus barabensis griseus).\nOC   Eukaryota; Metazoa; Chordata; Craniata; Vertebrata; Euteleostomi; Mammalia;\nOC   Eutheria; Euarchontoglires; Glires; Rodentia; Myomorpha; Muroidea;\nOC   Cricetidae; Cricetinae; Cricetulus.\nOX   NCBI_TaxID=10029 {ECO:0000312|Proteomes:UP001108280};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 19,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8C2LVE3?format=txt&versions=19)

```json
{
  "evidence_id": "H2",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A8C2LVE3?format=txt&versions=19",
  "source_sha256": "c78db6d4bdbc3208dbc3401f5215ab34d630f3586e718f4eb0558db0f9ef4abb",
  "retrieved_utc": "2026-11-02T04:26:00.260576+00:00",
  "source_locator": "lines 96-98",
  "excerpt": "FT   TOPO_DOM        1..11\nFT                   /note=\"Cytoplasmic\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 19,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8C2LVE3?format=txt&versions=19)

```json
{
  "evidence_id": "H3",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A8C2LVE3?format=txt&versions=19",
  "source_sha256": "c78db6d4bdbc3208dbc3401f5215ab34d630f3586e718f4eb0558db0f9ef4abb",
  "retrieved_utc": "2026-11-02T04:26:00.260576+00:00",
  "source_locator": "lines 99-101",
  "excerpt": "FT   TRANSMEM        12..28\nFT                   /note=\"Helical; Signal-anchor for type II membrane protein\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 19,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8C2LVE3?format=txt&versions=19)

```json
{
  "evidence_id": "H4",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A8C2LVE3?format=txt&versions=19",
  "source_sha256": "c78db6d4bdbc3208dbc3401f5215ab34d630f3586e718f4eb0558db0f9ef4abb",
  "retrieved_utc": "2026-11-02T04:26:00.260576+00:00",
  "source_locator": "lines 102-104",
  "excerpt": "FT   TOPO_DOM        29..356\nFT                   /note=\"Lumenal\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 19,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json), zero-based source row 32. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
