# transmembrane_0013: before and after transfer clarification

[All 1,328 cases](../README.md) · [Method](../METHOD.md) · [Summary](../SUMMARY.md) · [Exact reviewer user message](../inputs/transmembrane_0013.txt)

**Task:** `transmembrane`  
**Author key, unchanged:** **C** — 29..49; 66..86; 98..118; 141..163; 196..216; 237..257; 270..290

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
MEVSNMTTVTVFILLGLSNNPQVQALLFVLFLVIYLLTLLGNLLMVLVISTDSHLCTPMYFFLRQLSFLDAFYSSIIVPKLLENLLSKGETISFLECFTQISLVIFSGATEACLLSVMAYDRFQAMCHPLLYVVIINRRVCAGLVGASWAIGMGTGLINTLLLAQQHFCGPNVIHSFACELPPVLLLTCSDPCASIVSILTTMSVLGLGTLVLLLGSYSCIIMTALRINSATGRSKIFSTCSSHFLVVTIFYTSGVLRYMIPASGSALEQVLSVQYSVITPLLNPLIYSLKSQEVKVALRRMLARKSRLPL

[Multiple Choices]
A. 278..286; 308..323
B. 32..52; 66..86; 98..118; 141..163; 196..216; 237..257; 270..290
C. 29..49; 66..86; 98..118; 141..163; 196..216; 237..257; 270..290
D. 29..49; 66..86; 98..118; 196..216; 237..257; 270..290
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

> The exact sequence matches the UniProt record, whose historical and current annotations list the seven transmembrane regions in choice C. The transmembrane annotations carry evidence code ECO:0000255, indicating computational annotation rather than, on this evidence, experimental validation.

Citations as saved: [C6](#evidence-c6), [C8](#evidence-c8), [C10](#evidence-c10), [C12](#evidence-c12), [C14](#evidence-c14), [C16](#evidence-c16), [C18](#evidence-c18), [H3](#evidence-h3), [H5](#evidence-h5), [H7](#evidence-h7), [H9](#evidence-h9), [H11](#evidence-h11), [H13](#evidence-h13), [H15](#evidence-h15).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence has the repeated hydrophobic segments expected of a seven-transmembrane receptor, which supports the shared overall pattern in choices B and C. It does not decisively establish whether the first segment begins at residue 29 or 32.


**Missing item-specific fact**

> The precise annotated boundary for the first transmembrane helix, 29 rather than 32, is needed to select C over B.


**Reason**

> General sequence reasoning supports the broad locations of the helices, but the near-identical B and C options differ only by a three-residue boundary shift within the same hydrophobic region. Choosing between them depends on a protein-specific boundary annotation or prediction.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "C"
]
```

> Both choices identify the same seven broadly hydrophobic segments; their only difference is whether the first begins at residue 32 or 29, a boundary not clearly distinguishable from the supplied sequence alone.


### Important caveats

- The reviewer-only UniProt evidence matches the supplied sequence, but the author’s exact source snapshot is unknown.
- The cited transmembrane annotations are computationally evidenced; this support does not establish experimental measurement of the helix boundaries.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has the repeated hydrophobic segments expected of a seven-transmembrane receptor, which supports the shared overall pattern in choices B and C. It does not decisively establish whether the first segment begins at residue 29 or 32.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The precise annotated boundary for the first transmembrane helix, 29 rather than 32, is needed to select C over B.",
    "reason": "General sequence reasoning supports the broad locations of the helices, but the near-identical B and C options differ only by a three-residue boundary shift within the same hydrophobic region. Choosing between them depends on a protein-specific boundary annotation or prediction."
  },
  "case_id": "transmembrane_0013",
  "expected_answer_check": {
    "evidence_ids": [
      "C6",
      "C8",
      "C10",
      "C12",
      "C14",
      "C16",
      "C18",
      "H3",
      "H5",
      "H7",
      "H9",
      "H11",
      "H13",
      "H15"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt record, whose historical and current annotations list the seven transmembrane regions in choice C. The transmembrane annotations carry evidence code ECO:0000255, indicating computational annotation rather than, on this evidence, experimental validation."
  },
  "important_caveats": [
    "The reviewer-only UniProt evidence matches the supplied sequence, but the author’s exact source snapshot is unknown.",
    "The cited transmembrane annotations are computationally evidenced; this support does not establish experimental measurement of the helix boundaries."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "C"
    ],
    "reason": "Both choices identify the same seven broadly hydrophobic segments; their only difference is whether the first begins at residue 32 or 29, a boundary not clearly distinguishable from the supplied sequence alone."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0013",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt record, whose historical and current annotations list the seven transmembrane regions in choice C. The transmembrane annotations carry evidence code ECO:0000255, indicating computational annotation rather than, on this evidence, experimental validation.",
    "evidence_ids": ["C6", "C8", "C10", "C12", "C14", "C16", "C18", "H3", "H5", "H7", "H9", "H11", "H13", "H15"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence has the repeated hydrophobic segments expected of a seven-transmembrane receptor, which supports the shared overall pattern in choices B and C. It does not decisively establish whether the first segment begins at residue 29 or 32.",
    "missing_item_specific_fact": "The precise annotated boundary for the first transmembrane helix, 29 rather than 32, is needed to select C over B.",
    "reason": "General sequence reasoning supports the broad locations of the helices, but the near-identical B and C options differ only by a three-residue boundary shift within the same hydrophobic region. Choosing between them depends on a protein-specific boundary annotation or prediction."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "C"],
    "reason": "Both choices identify the same seven broadly hydrophobic segments; their only difference is whether the first begins at residue 32 or 29, a boundary not clearly distinguishable from the supplied sequence alone."
  },
  "important_caveats": [
    "The reviewer-only UniProt evidence matches the supplied sequence, but the author’s exact source snapshot is unknown.",
    "The cited transmembrane annotations are computationally evidenced; this support does not establish experimental measurement of the helix boundaries."
  ]
}
```

</details>

## Before: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> Choice C (29..49; 66..86; 98..118; 141..163; 196..216; 237..257; 270..290) matches the UniProt annotation for A0A2R8YED5 (Olfactory receptor 5BS1) exactly across all seven transmembrane helices. The evidence codes are ECO:0000255 (inferred by similarity), meaning these are computational annotations transferred by homology, not experimentally determined boundaries. Nevertheless, they are the canonical database annotation for this sequence, and the sequence SHA-256 matches the benchmark input.

Citations as saved: [C6](#evidence-c6), [C8](#evidence-c8), [C10](#evidence-c10), [C12](#evidence-c12), [C14](#evidence-c14), [C16](#evidence-c16), [C18](#evidence-c18), [H3](#evidence-h3), [H5](#evidence-h5), [H7](#evidence-h7), [H9](#evidence-h9), [H11](#evidence-h11), [H13](#evidence-h13), [H15](#evidence-h15).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The protein is 311 residues with multiple long hydrophobic stretches, consistent with a seven-transmembrane GPCR. Olfactory receptors are canonical 7-TM GPCRs, so a model with general GPCR knowledge can eliminate A (only 2 segments) and D (only 6 segments, missing TM4 at 141..163). Between B and C, the sole difference is whether TM1 begins at residue 29 (V-L-F) or 32 (L). Positions 29–31 (V, L, F) are strongly hydrophobic and form part of the continuous hydrophobic helix core VLFLVIYLLTLLGNLLMVLVI; the preceding residues at 25–27 (A, L, L) are more ambiguous. A standard hydropathy-window analysis (e.g., Kyte-Doolittle with a 19–21 residue window) would naturally extend the TM1 helix to include VLF at position 29, favoring C. The N-terminal extracellular segment (1–28) contains polar/charged residues (S, N, N, P, Q, V, Q) that break the hydrophobic stretch before position 29, supporting a TM1 start at 29 rather than 32.


**Missing item-specific fact**

> None strictly required. The B-vs-C distinction rests on a 3-residue boundary that is resolvable by hydrophobicity analysis, though the margin is thin. The exact annotation (ECO:0000255, inferred by similarity) confirms C but is not the only path to it.


**Reason**

> The major structural reasoning (7-TM GPCR topology) eliminates A and D. The B-vs-C distinction, while narrow, can be addressed by standard hydropathy analysis: the hydrophobic residues VLF at 29–31 belong to the TM1 helix core, and the polar residues in the N-terminal region (positions ~19–28) mark the extracellular boundary. This provides a concrete, if thin, biological argument for C over B without requiring memorization of a specific database entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "C"
]
```

> B and C differ only in the TM1 start position (32 vs 29, a 3-residue shift). Both boundaries are within the hydrophobic N-terminal region, and different hydropathy algorithms or window sizes could yield either boundary. C is slightly better supported because V(29), L(30), F(31) are hydrophobic and the preceding residues (A25, L26, L27, F28) are more ambiguous, but a model choosing B would not be unreasonable. The annotation evidence (ECO:0000255) is computational, not experimental, so neither boundary is experimentally fixed.


### Important caveats

- All seven TM annotations carry evidence code ECO:0000255 (inferred by similarity), meaning they are computational predictions transferred from homologous proteins, not experimentally validated boundaries.
- The B-vs-C distinction (3 residues in TM1) is at the threshold of what hydropathy analysis can reliably resolve; different algorithms and parameter choices could shift this boundary.
- The UniProt entry was first released 2025-02-05 and has undergone annotation updates; the historical snapshot used by the benchmark author is unknown.
- The reviewer-only evidence confirms sequence identity (SHA-256 match) but the evaluated model had no access to the UniProt annotation or accession.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The protein is 311 residues with multiple long hydrophobic stretches, consistent with a seven-transmembrane GPCR. Olfactory receptors are canonical 7-TM GPCRs, so a model with general GPCR knowledge can eliminate A (only 2 segments) and D (only 6 segments, missing TM4 at 141..163). Between B and C, the sole difference is whether TM1 begins at residue 29 (V-L-F) or 32 (L). Positions 29–31 (V, L, F) are strongly hydrophobic and form part of the continuous hydrophobic helix core VLFLVIYLLTLLGNLLMVLVI; the preceding residues at 25–27 (A, L, L) are more ambiguous. A standard hydropathy-window analysis (e.g., Kyte-Doolittle with a 19–21 residue window) would naturally extend the TM1 helix to include VLF at position 29, favoring C. The N-terminal extracellular segment (1–28) contains polar/charged residues (S, N, N, P, Q, V, Q) that break the hydrophobic stretch before position 29, supporting a TM1 start at 29 rather than 32.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None strictly required. The B-vs-C distinction rests on a 3-residue boundary that is resolvable by hydrophobicity analysis, though the margin is thin. The exact annotation (ECO:0000255, inferred by similarity) confirms C but is not the only path to it.",
    "reason": "The major structural reasoning (7-TM GPCR topology) eliminates A and D. The B-vs-C distinction, while narrow, can be addressed by standard hydropathy analysis: the hydrophobic residues VLF at 29–31 belong to the TM1 helix core, and the polar residues in the N-terminal region (positions ~19–28) mark the extracellular boundary. This provides a concrete, if thin, biological argument for C over B without requiring memorization of a specific database entry."
  },
  "case_id": "transmembrane_0013",
  "expected_answer_check": {
    "evidence_ids": [
      "C6",
      "C8",
      "C10",
      "C12",
      "C14",
      "C16",
      "C18",
      "H3",
      "H5",
      "H7",
      "H9",
      "H11",
      "H13",
      "H15"
    ],
    "judgment": "supported",
    "reason": "Choice C (29..49; 66..86; 98..118; 141..163; 196..216; 237..257; 270..290) matches the UniProt annotation for A0A2R8YED5 (Olfactory receptor 5BS1) exactly across all seven transmembrane helices. The evidence codes are ECO:0000255 (inferred by similarity), meaning these are computational annotations transferred by homology, not experimentally determined boundaries. Nevertheless, they are the canonical database annotation for this sequence, and the sequence SHA-256 matches the benchmark input."
  },
  "important_caveats": [
    "All seven TM annotations carry evidence code ECO:0000255 (inferred by similarity), meaning they are computational predictions transferred from homologous proteins, not experimentally validated boundaries.",
    "The B-vs-C distinction (3 residues in TM1) is at the threshold of what hydropathy analysis can reliably resolve; different algorithms and parameter choices could shift this boundary.",
    "The UniProt entry was first released 2025-02-05 and has undergone annotation updates; the historical snapshot used by the benchmark author is unknown.",
    "The reviewer-only evidence confirms sequence identity (SHA-256 match) but the evaluated model had no access to the UniProt annotation or accession."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "C"
    ],
    "reason": "B and C differ only in the TM1 start position (32 vs 29, a 3-residue shift). Both boundaries are within the hydrophobic N-terminal region, and different hydropathy algorithms or window sizes could yield either boundary. C is slightly better supported because V(29), L(30), F(31) are hydrophobic and the preceding residues (A25, L26, L27, F28) are more ambiguous, but a model choosing B would not be unreasonable. The annotation evidence (ECO:0000255) is computational, not experimental, so neither boundary is experimentally fixed."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0013",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "Choice C (29..49; 66..86; 98..118; 141..163; 196..216; 237..257; 270..290) matches the UniProt annotation for A0A2R8YED5 (Olfactory receptor 5BS1) exactly across all seven transmembrane helices. The evidence codes are ECO:0000255 (inferred by similarity), meaning these are computational annotations transferred by homology, not experimentally determined boundaries. Nevertheless, they are the canonical database annotation for this sequence, and the sequence SHA-256 matches the benchmark input.",
    "evidence_ids": ["C6", "C8", "C10", "C12", "C14", "C16", "C18", "H3", "H5", "H7", "H9", "H11", "H13", "H15"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The protein is 311 residues with multiple long hydrophobic stretches, consistent with a seven-transmembrane GPCR. Olfactory receptors are canonical 7-TM GPCRs, so a model with general GPCR knowledge can eliminate A (only 2 segments) and D (only 6 segments, missing TM4 at 141..163). Between B and C, the sole difference is whether TM1 begins at residue 29 (V-L-F) or 32 (L). Positions 29–31 (V, L, F) are strongly hydrophobic and form part of the continuous hydrophobic helix core VLFLVIYLLTLLGNLLMVLVI; the preceding residues at 25–27 (A, L, L) are more ambiguous. A standard hydropathy-window analysis (e.g., Kyte-Doolittle with a 19–21 residue window) would naturally extend the TM1 helix to include VLF at position 29, favoring C. The N-terminal extracellular segment (1–28) contains polar/charged residues (S, N, N, P, Q, V, Q) that break the hydrophobic stretch before position 29, supporting a TM1 start at 29 rather than 32.",
    "missing_item_specific_fact": "None strictly required. The B-vs-C distinction rests on a 3-residue boundary that is resolvable by hydrophobicity analysis, though the margin is thin. The exact annotation (ECO:0000255, inferred by similarity) confirms C but is not the only path to it.",
    "reason": "The major structural reasoning (7-TM GPCR topology) eliminates A and D. The B-vs-C distinction, while narrow, can be addressed by standard hydropathy analysis: the hydrophobic residues VLF at 29–31 belong to the TM1 helix core, and the polar residues in the N-terminal region (positions ~19–28) mark the extracellular boundary. This provides a concrete, if thin, biological argument for C over B without requiring memorization of a specific database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "C"],
    "reason": "B and C differ only in the TM1 start position (32 vs 29, a 3-residue shift). Both boundaries are within the hydrophobic N-terminal region, and different hydropathy algorithms or window sizes could yield either boundary. C is slightly better supported because V(29), L(30), F(31) are hydrophobic and the preceding residues (A25, L26, L27, F28) are more ambiguous, but a model choosing B would not be unreasonable. The annotation evidence (ECO:0000255) is computational, not experimental, so neither boundary is experimentally fixed."
  },
  "important_caveats": [
    "All seven TM annotations carry evidence code ECO:0000255 (inferred by similarity), meaning they are computational predictions transferred from homologous proteins, not experimentally validated boundaries.",
    "The B-vs-C distinction (3 residues in TM1) is at the threshold of what hydropathy analysis can reliably resolve; different algorithms and parameter choices could shift this boundary.",
    "The UniProt entry was first released 2025-02-05 and has undergone annotation updates; the historical snapshot used by the benchmark author is unknown.",
    "The reviewer-only evidence confirms sequence identity (SHA-256 match) but the evaluated model had no access to the UniProt annotation or accession."
  ]
}
```

</details>

## After: GPT-6 Luna

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence-matched UniProt annotations list seven transmembrane helices, including 29..49 and the other regions in choice C. These annotations are computationally evidenced, not experimental confirmation.

Citations as saved: [C6](#evidence-c6), [C8](#evidence-c8), [C10](#evidence-c10), [C12](#evidence-c12), [C14](#evidence-c14), [C16](#evidence-c16), [C18](#evidence-c18).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has the characteristic pattern of a multi-pass, seven-helix membrane protein: long hydrophobic stretches recur at the regions listed in C, including a particularly hydrophobic stretch around 29..49. This distinguishes C from A, which does not give the set of membrane-spanning regions, and D, which omits a likely helix. C is also favored over B because B shifts the first segment toward more polar residues at its end.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Transferable knowledge of membrane-protein hydropathy and seven-helix architectures provides a credible basis for selecting C among these choices, although sequence-based inference does not establish exact helix boundaries with certainty.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "C"
]
```

> B and C describe nearly the same strongly hydrophobic first helix, shifted by only three residues. C is better supported by the hydropathy pattern, but exact membrane-helix boundaries are approximate, so the sequence alone may not uniquely settle those endpoints.


### Important caveats

- The cited source annotations are computationally evidenced; they should not be represented as experimental measurements.
- The reviewer-only source identity and annotations were not part of the original model input.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has the characteristic pattern of a multi-pass, seven-helix membrane protein: long hydrophobic stretches recur at the regions listed in C, including a particularly hydrophobic stretch around 29..49. This distinguishes C from A, which does not give the set of membrane-spanning regions, and D, which omits a likely helix. C is also favored over B because B shifts the first segment toward more polar residues at its end.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Transferable knowledge of membrane-protein hydropathy and seven-helix architectures provides a credible basis for selecting C among these choices, although sequence-based inference does not establish exact helix boundaries with certainty."
  },
  "case_id": "transmembrane_0013",
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
    "reason": "The sequence-matched UniProt annotations list seven transmembrane helices, including 29..49 and the other regions in choice C. These annotations are computationally evidenced, not experimental confirmation."
  },
  "important_caveats": [
    "The cited source annotations are computationally evidenced; they should not be represented as experimental measurements.",
    "The reviewer-only source identity and annotations were not part of the original model input."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "C"
    ],
    "reason": "B and C describe nearly the same strongly hydrophobic first helix, shifted by only three residues. C is better supported by the hydropathy pattern, but exact membrane-helix boundaries are approximate, so the sequence alone may not uniquely settle those endpoints."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0013",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotations list seven transmembrane helices, including 29..49 and the other regions in choice C. These annotations are computationally evidenced, not experimental confirmation.",
    "evidence_ids": ["C6", "C8", "C10", "C12", "C14", "C16", "C18"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has the characteristic pattern of a multi-pass, seven-helix membrane protein: long hydrophobic stretches recur at the regions listed in C, including a particularly hydrophobic stretch around 29..49. This distinguishes C from A, which does not give the set of membrane-spanning regions, and D, which omits a likely helix. C is also favored over B because B shifts the first segment toward more polar residues at its end.",
    "missing_item_specific_fact": "",
    "reason": "Transferable knowledge of membrane-protein hydropathy and seven-helix architectures provides a credible basis for selecting C among these choices, although sequence-based inference does not establish exact helix boundaries with certainty."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "C"],
    "reason": "B and C describe nearly the same strongly hydrophobic first helix, shifted by only three residues. C is better supported by the hydropathy pattern, but exact membrane-helix boundaries are approximate, so the sequence alone may not uniquely settle those endpoints."
  },
  "important_caveats": [
    "The cited source annotations are computationally evidenced; they should not be represented as experimental measurements.",
    "The reviewer-only source identity and annotations were not part of the original model input."
  ]
}
```

</details>

## After: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt annotation for this sequence (A0A2R8YED5, Olfactory receptor 5BS1) lists exactly 7 transmembrane helices at positions 29..49, 66..86, 98..118, 141..163, 196..216, 237..257, and 270..290, matching option C precisely. The evidence code ECO:0000255 indicates inference by similarity (computational annotation), not experimental determination, but the annotation is consistent with the hydrophobicity profile of the sequence. The topological domain assignments (Extracellular 1-28, Cytoplasmic 50-65, Extracellular 87-97, etc.) are internally consistent with the 7TM topology.

Citations as saved: [C6](#evidence-c6), [C8](#evidence-c8), [C10](#evidence-c10), [C12](#evidence-c12), [C14](#evidence-c14), [C16](#evidence-c16), [C18](#evidence-c18), [H3](#evidence-h3), [H5](#evidence-h5), [H7](#evidence-h7), [H9](#evidence-h9), [H11](#evidence-h11), [H13](#evidence-h13), [H15](#evidence-h15).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Three transferable inference steps distinguish C from the alternatives: (1) The protein is 311 residues with multiple long hydrophobic stretches, consistent with a 7TM GPCR (olfactory receptor family). This eliminates A (only 2 segments of 9 and 16 residues—far too short to span a ~30 Å bilayer) and D (only 6 TM regions, missing the clearly hydrophobic 141-163 segment: CAGLVGASWAIGMGTGLINTLLL). (2) Between B and C, the first TM boundary differs: 32..52 vs 29..49. Positions 50-52 are S-T-D (polar), making 32-52 an unnatural TM terminus that includes polar residues in the helix. Positions 29-49 (VLFVLVIYLLTLLGNLLMVLVI) form a clean hydrophobic helix ending at Ile-49. (3) The N-terminal region (1-28) contains many polar residues (MEVSNMTTV, SNNPQVQ) typical of an extracellular domain in GPCRs, placing the TM1 start at ~29 rather than 32. These are standard hydrophobicity-based TM prediction arguments applicable to any membrane protein, not specific to this exact protein.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A model with knowledge of GPCR 7TM topology, standard hydrophobicity windows (~20-25 hydrophobic residues for a TM helix), and the requirement that TM helices terminate at hydrophobic boundaries can eliminate A (too few/too short), D (missing a clearly hydrophobic TM4), and B (TM1 boundary includes polar STD at positions 50-52). The remaining choice C is selected by standard hydropathy analysis without needing to recall this specific protein's database annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> While the exact boundary between 29 and 32 for TM1 start could be debated by a few residues, option B's inclusion of polar S-T-D at positions 50-52 within the TM helix is a clear disqualifier under standard TM prediction criteria. Option D is eliminated by the GPCR 7TM requirement. Option A is eliminated by the absurdly short segments. Only C satisfies all constraints simultaneously.


### Important caveats

- The UniProt annotation uses evidence code ECO:0000255 (inferred by similarity), meaning the TM boundaries are computationally predicted, not experimentally determined.
- The exact TM1 start position (29 vs 32) is a matter of a few residues and could vary slightly among different prediction algorithms; however, the inclusion of polar residues in option B's boundary makes it clearly less appropriate.
- The protein identity (olfactory receptor) was not provided in the original input; the 7TM inference relies on recognizing the sequence as a GPCR-family protein from its hydrophobic pattern and length.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Three transferable inference steps distinguish C from the alternatives: (1) The protein is 311 residues with multiple long hydrophobic stretches, consistent with a 7TM GPCR (olfactory receptor family). This eliminates A (only 2 segments of 9 and 16 residues—far too short to span a ~30 Å bilayer) and D (only 6 TM regions, missing the clearly hydrophobic 141-163 segment: CAGLVGASWAIGMGTGLINTLLL). (2) Between B and C, the first TM boundary differs: 32..52 vs 29..49. Positions 50-52 are S-T-D (polar), making 32-52 an unnatural TM terminus that includes polar residues in the helix. Positions 29-49 (VLFVLVIYLLTLLGNLLMVLVI) form a clean hydrophobic helix ending at Ile-49. (3) The N-terminal region (1-28) contains many polar residues (MEVSNMTTV, SNNPQVQ) typical of an extracellular domain in GPCRs, placing the TM1 start at ~29 rather than 32. These are standard hydrophobicity-based TM prediction arguments applicable to any membrane protein, not specific to this exact protein.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A model with knowledge of GPCR 7TM topology, standard hydrophobicity windows (~20-25 hydrophobic residues for a TM helix), and the requirement that TM helices terminate at hydrophobic boundaries can eliminate A (too few/too short), D (missing a clearly hydrophobic TM4), and B (TM1 boundary includes polar STD at positions 50-52). The remaining choice C is selected by standard hydropathy analysis without needing to recall this specific protein's database annotation."
  },
  "case_id": "transmembrane_0013",
  "expected_answer_check": {
    "evidence_ids": [
      "C6",
      "C8",
      "C10",
      "C12",
      "C14",
      "C16",
      "C18",
      "H3",
      "H5",
      "H7",
      "H9",
      "H11",
      "H13",
      "H15"
    ],
    "judgment": "supported",
    "reason": "The UniProt annotation for this sequence (A0A2R8YED5, Olfactory receptor 5BS1) lists exactly 7 transmembrane helices at positions 29..49, 66..86, 98..118, 141..163, 196..216, 237..257, and 270..290, matching option C precisely. The evidence code ECO:0000255 indicates inference by similarity (computational annotation), not experimental determination, but the annotation is consistent with the hydrophobicity profile of the sequence. The topological domain assignments (Extracellular 1-28, Cytoplasmic 50-65, Extracellular 87-97, etc.) are internally consistent with the 7TM topology."
  },
  "important_caveats": [
    "The UniProt annotation uses evidence code ECO:0000255 (inferred by similarity), meaning the TM boundaries are computationally predicted, not experimentally determined.",
    "The exact TM1 start position (29 vs 32) is a matter of a few residues and could vary slightly among different prediction algorithms; however, the inclusion of polar residues in option B's boundary makes it clearly less appropriate.",
    "The protein identity (olfactory receptor) was not provided in the original input; the 7TM inference relies on recognizing the sequence as a GPCR-family protein from its hydrophobic pattern and length."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While the exact boundary between 29 and 32 for TM1 start could be debated by a few residues, option B's inclusion of polar S-T-D at positions 50-52 within the TM helix is a clear disqualifier under standard TM prediction criteria. Option D is eliminated by the GPCR 7TM requirement. Option A is eliminated by the absurdly short segments. Only C satisfies all constraints simultaneously."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0013",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt annotation for this sequence (A0A2R8YED5, Olfactory receptor 5BS1) lists exactly 7 transmembrane helices at positions 29..49, 66..86, 98..118, 141..163, 196..216, 237..257, and 270..290, matching option C precisely. The evidence code ECO:0000255 indicates inference by similarity (computational annotation), not experimental determination, but the annotation is consistent with the hydrophobicity profile of the sequence. The topological domain assignments (Extracellular 1-28, Cytoplasmic 50-65, Extracellular 87-97, etc.) are internally consistent with the 7TM topology.",
    "evidence_ids": ["C6", "C8", "C10", "C12", "C14", "C16", "C18", "H3", "H5", "H7", "H9", "H11", "H13", "H15"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Three transferable inference steps distinguish C from the alternatives: (1) The protein is 311 residues with multiple long hydrophobic stretches, consistent with a 7TM GPCR (olfactory receptor family). This eliminates A (only 2 segments of 9 and 16 residues—far too short to span a ~30 Å bilayer) and D (only 6 TM regions, missing the clearly hydrophobic 141-163 segment: CAGLVGASWAIGMGTGLINTLLL). (2) Between B and C, the first TM boundary differs: 32..52 vs 29..49. Positions 50-52 are S-T-D (polar), making 32-52 an unnatural TM terminus that includes polar residues in the helix. Positions 29-49 (VLFVLVIYLLTLLGNLLMVLVI) form a clean hydrophobic helix ending at Ile-49. (3) The N-terminal region (1-28) contains many polar residues (MEVSNMTTV, SNNPQVQ) typical of an extracellular domain in GPCRs, placing the TM1 start at ~29 rather than 32. These are standard hydrophobicity-based TM prediction arguments applicable to any membrane protein, not specific to this exact protein.",
    "missing_item_specific_fact": "",
    "reason": "A model with knowledge of GPCR 7TM topology, standard hydrophobicity windows (~20-25 hydrophobic residues for a TM helix), and the requirement that TM helices terminate at hydrophobic boundaries can eliminate A (too few/too short), D (missing a clearly hydrophobic TM4), and B (TM1 boundary includes polar STD at positions 50-52). The remaining choice C is selected by standard hydropathy analysis without needing to recall this specific protein's database annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While the exact boundary between 29 and 32 for TM1 start could be debated by a few residues, option B's inclusion of polar S-T-D at positions 50-52 within the TM helix is a clear disqualifier under standard TM prediction criteria. Option D is eliminated by the GPCR 7TM requirement. Option A is eliminated by the absurdly short segments. Only C satisfies all constraints simultaneously."
  },
  "important_caveats": [
    "The UniProt annotation uses evidence code ECO:0000255 (inferred by similarity), meaning the TM boundaries are computationally predicted, not experimentally determined.",
    "The exact TM1 start position (29 vs 32) is a matter of a few residues and could vary slightly among different prediction algorithms; however, the inclusion of polar residues in option B's boundary makes it clearly less appropriate.",
    "The protein identity (olfactory receptor) was not provided in the original input; the 7TM inference relies on recognizing the sequence as a GPCR-family protein from its hydrophobic pattern and length."
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
  "requested_accession": "A0A2R8YED5",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "benchmark_sequence_sha256": "ff6310a4b4f4740c74bc69549e735efa3d99058c3339ad175a562e376a5b2703",
  "benchmark_sequence_length": 311,
  "current_status": "retrieved",
  "current_sequence_comparison": "matched",
  "current_entry_audit": {
    "entryVersion": 30,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2018-06-20",
    "sequenceVersion": 1
  },
  "current_uniprot_release": "2026_03",
  "current_record_sha256": "d0a68a9d870084d5a8a25b212bcab1f8fc22e1d9dc23ed81cdab2f3f4f4889f2",
  "current_source_sequence_sha256": "ff6310a4b4f4740c74bc69549e735efa3d99058c3339ad175a562e376a5b2703",
  "current_source_sequence_length": 311,
  "historical_status": "retrieved",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "selected_historical_entry_version": 28,
  "selected_historical_version": {
    "accession": "A0A2R8YED5",
    "database": "Swiss-Prot",
    "entryVersion": 28,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "O5BS1_HUMAN",
    "sequenceVersion": 1
  },
  "selected_historical_record_sha256": "cca1844e232709cdf49594e55779c1f7550585001e53d4c1927ed8cbc4f14327",
  "selected_historical_source_sequence_sha256": "ff6310a4b4f4740c74bc69549e735efa3d99058c3339ad175a562e376a5b2703",
  "selected_historical_source_sequence_length": 311,
  "latest_at_cutoff_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 28,
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2R8YED5.json)

```json
{
  "evidence_id": "C1",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2R8YED5.json",
  "source_sha256": "d0a68a9d870084d5a8a25b212bcab1f8fc22e1d9dc23ed81cdab2f3f4f4889f2",
  "retrieved_utc": "2026-11-01T06:24:45.255114+00:00",
  "json_pointer": "/primaryAccession",
  "excerpt": "\"A0A2R8YED5\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2R8YED5.json)

```json
{
  "evidence_id": "C2",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2R8YED5.json",
  "source_sha256": "d0a68a9d870084d5a8a25b212bcab1f8fc22e1d9dc23ed81cdab2f3f4f4889f2",
  "retrieved_utc": "2026-11-01T06:24:45.255114+00:00",
  "json_pointer": "/entryAudit",
  "excerpt": "{\"entryVersion\":30,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2018-06-20\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2R8YED5.json)

```json
{
  "evidence_id": "C3",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2R8YED5.json",
  "source_sha256": "d0a68a9d870084d5a8a25b212bcab1f8fc22e1d9dc23ed81cdab2f3f4f4889f2",
  "retrieved_utc": "2026-11-01T06:24:45.255114+00:00",
  "json_pointer": "/organism",
  "excerpt": "{\"commonName\":\"Human\",\"lineage\":[\"Eukaryota\",\"Metazoa\",\"Chordata\",\"Craniata\",\"Vertebrata\",\"Euteleostomi\",\"Mammalia\",\"Eutheria\",\"Euarchontoglires\",\"Primates\",\"Haplorrhini\",\"Catarrhini\",\"Hominidae\",\"Homo\"],\"scientificName\":\"Homo sapiens\",\"taxonId\":9606}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2R8YED5.json)

```json
{
  "evidence_id": "C4",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2R8YED5.json",
  "source_sha256": "d0a68a9d870084d5a8a25b212bcab1f8fc22e1d9dc23ed81cdab2f3f4f4889f2",
  "retrieved_utc": "2026-11-01T06:24:45.255114+00:00",
  "json_pointer": "/proteinDescription",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"HGNC:19627\",\"source\":\"HGNC\"}],\"value\":\"Olfactory receptor family 5 subfamily BS member 1\"}}],\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Olfactory receptor 5BS1\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2R8YED5.json)

```json
{
  "evidence_id": "C5",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2R8YED5.json",
  "source_sha256": "d0a68a9d870084d5a8a25b212bcab1f8fc22e1d9dc23ed81cdab2f3f4f4889f2",
  "retrieved_utc": "2026-11-01T06:24:45.255114+00:00",
  "json_pointer": "/features/1",
  "excerpt": "{\"description\":\"Extracellular\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":28},\"start\":{\"modifier\":\"EXACT\",\"value\":1}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2R8YED5.json)

```json
{
  "evidence_id": "C6",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2R8YED5.json",
  "source_sha256": "d0a68a9d870084d5a8a25b212bcab1f8fc22e1d9dc23ed81cdab2f3f4f4889f2",
  "retrieved_utc": "2026-11-01T06:24:45.255114+00:00",
  "json_pointer": "/features/2",
  "excerpt": "{\"description\":\"Helical; Name=1\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":49},\"start\":{\"modifier\":\"EXACT\",\"value\":29}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2R8YED5.json)

```json
{
  "evidence_id": "C7",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2R8YED5.json",
  "source_sha256": "d0a68a9d870084d5a8a25b212bcab1f8fc22e1d9dc23ed81cdab2f3f4f4889f2",
  "retrieved_utc": "2026-11-01T06:24:45.255114+00:00",
  "json_pointer": "/features/3",
  "excerpt": "{\"description\":\"Cytoplasmic\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":65},\"start\":{\"modifier\":\"EXACT\",\"value\":50}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2R8YED5.json)

```json
{
  "evidence_id": "C8",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2R8YED5.json",
  "source_sha256": "d0a68a9d870084d5a8a25b212bcab1f8fc22e1d9dc23ed81cdab2f3f4f4889f2",
  "retrieved_utc": "2026-11-01T06:24:45.255114+00:00",
  "json_pointer": "/features/4",
  "excerpt": "{\"description\":\"Helical; Name=2\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":86},\"start\":{\"modifier\":\"EXACT\",\"value\":66}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2R8YED5.json)

```json
{
  "evidence_id": "C9",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2R8YED5.json",
  "source_sha256": "d0a68a9d870084d5a8a25b212bcab1f8fc22e1d9dc23ed81cdab2f3f4f4889f2",
  "retrieved_utc": "2026-11-01T06:24:45.255114+00:00",
  "json_pointer": "/features/5",
  "excerpt": "{\"description\":\"Extracellular\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":97},\"start\":{\"modifier\":\"EXACT\",\"value\":87}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2R8YED5.json)

```json
{
  "evidence_id": "C10",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2R8YED5.json",
  "source_sha256": "d0a68a9d870084d5a8a25b212bcab1f8fc22e1d9dc23ed81cdab2f3f4f4889f2",
  "retrieved_utc": "2026-11-01T06:24:45.255114+00:00",
  "json_pointer": "/features/6",
  "excerpt": "{\"description\":\"Helical; Name=3\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":118},\"start\":{\"modifier\":\"EXACT\",\"value\":98}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2R8YED5.json)

```json
{
  "evidence_id": "C11",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2R8YED5.json",
  "source_sha256": "d0a68a9d870084d5a8a25b212bcab1f8fc22e1d9dc23ed81cdab2f3f4f4889f2",
  "retrieved_utc": "2026-11-01T06:24:45.255114+00:00",
  "json_pointer": "/features/7",
  "excerpt": "{\"description\":\"Cytoplasmic\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":140},\"start\":{\"modifier\":\"EXACT\",\"value\":119}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2R8YED5.json)

```json
{
  "evidence_id": "C12",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2R8YED5.json",
  "source_sha256": "d0a68a9d870084d5a8a25b212bcab1f8fc22e1d9dc23ed81cdab2f3f4f4889f2",
  "retrieved_utc": "2026-11-01T06:24:45.255114+00:00",
  "json_pointer": "/features/8",
  "excerpt": "{\"description\":\"Helical; Name=4\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":163},\"start\":{\"modifier\":\"EXACT\",\"value\":141}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C13

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2R8YED5.json)

```json
{
  "evidence_id": "C13",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2R8YED5.json",
  "source_sha256": "d0a68a9d870084d5a8a25b212bcab1f8fc22e1d9dc23ed81cdab2f3f4f4889f2",
  "retrieved_utc": "2026-11-01T06:24:45.255114+00:00",
  "json_pointer": "/features/9",
  "excerpt": "{\"description\":\"Extracellular\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":195},\"start\":{\"modifier\":\"EXACT\",\"value\":164}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C14

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2R8YED5.json)

```json
{
  "evidence_id": "C14",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2R8YED5.json",
  "source_sha256": "d0a68a9d870084d5a8a25b212bcab1f8fc22e1d9dc23ed81cdab2f3f4f4889f2",
  "retrieved_utc": "2026-11-01T06:24:45.255114+00:00",
  "json_pointer": "/features/10",
  "excerpt": "{\"description\":\"Helical; Name=5\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":216},\"start\":{\"modifier\":\"EXACT\",\"value\":196}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C15

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2R8YED5.json)

```json
{
  "evidence_id": "C15",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2R8YED5.json",
  "source_sha256": "d0a68a9d870084d5a8a25b212bcab1f8fc22e1d9dc23ed81cdab2f3f4f4889f2",
  "retrieved_utc": "2026-11-01T06:24:45.255114+00:00",
  "json_pointer": "/features/11",
  "excerpt": "{\"description\":\"Cytoplasmic\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":236},\"start\":{\"modifier\":\"EXACT\",\"value\":217}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C16

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2R8YED5.json)

```json
{
  "evidence_id": "C16",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2R8YED5.json",
  "source_sha256": "d0a68a9d870084d5a8a25b212bcab1f8fc22e1d9dc23ed81cdab2f3f4f4889f2",
  "retrieved_utc": "2026-11-01T06:24:45.255114+00:00",
  "json_pointer": "/features/12",
  "excerpt": "{\"description\":\"Helical; Name=6\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":257},\"start\":{\"modifier\":\"EXACT\",\"value\":237}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C17

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2R8YED5.json)

```json
{
  "evidence_id": "C17",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2R8YED5.json",
  "source_sha256": "d0a68a9d870084d5a8a25b212bcab1f8fc22e1d9dc23ed81cdab2f3f4f4889f2",
  "retrieved_utc": "2026-11-01T06:24:45.255114+00:00",
  "json_pointer": "/features/13",
  "excerpt": "{\"description\":\"Extracellular\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":269},\"start\":{\"modifier\":\"EXACT\",\"value\":258}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C18

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2R8YED5.json)

```json
{
  "evidence_id": "C18",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2R8YED5.json",
  "source_sha256": "d0a68a9d870084d5a8a25b212bcab1f8fc22e1d9dc23ed81cdab2f3f4f4889f2",
  "retrieved_utc": "2026-11-01T06:24:45.255114+00:00",
  "json_pointer": "/features/14",
  "excerpt": "{\"description\":\"Helical; Name=7\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":290},\"start\":{\"modifier\":\"EXACT\",\"value\":270}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C19

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2R8YED5.json)

```json
{
  "evidence_id": "C19",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2R8YED5.json",
  "source_sha256": "d0a68a9d870084d5a8a25b212bcab1f8fc22e1d9dc23ed81cdab2f3f4f4889f2",
  "retrieved_utc": "2026-11-01T06:24:45.255114+00:00",
  "json_pointer": "/features/15",
  "excerpt": "{\"description\":\"Cytoplasmic\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":311},\"start\":{\"modifier\":\"EXACT\",\"value\":291}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2R8YED5?format=txt&versions=28)

```json
{
  "evidence_id": "H1",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A2R8YED5?format=txt&versions=28",
  "source_sha256": "cca1844e232709cdf49594e55779c1f7550585001e53d4c1927ed8cbc4f14327",
  "retrieved_utc": "2026-11-01T06:27:26.314292+00:00",
  "source_locator": "lines 1-14",
  "excerpt": "ID   O5BS1_HUMAN             Reviewed;         311 AA.\nAC   A0A2R8YED5; Q8NH44;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   20-JUN-2018, sequence version 1.\nDT   28-JAN-2026, entry version 28.\nDE   RecName: Full=Olfactory receptor 5BS1 {ECO:0000305};\nDE   AltName: Full=Olfactory receptor family 5 subfamily BS member 1 {ECO:0000312|HGNC:HGNC:19627};\nGN   Name=OR5BS1 {ECO:0000312|HGNC:HGNC:19627};\nGN   Synonyms=OR5BS1P {ECO:0000312|HGNC:HGNC:19627};\nOS   Homo sapiens (Human).\nOC   Eukaryota; Metazoa; Chordata; Craniata; Vertebrata; Euteleostomi; Mammalia;\nOC   Eutheria; Euarchontoglires; Primates; Haplorrhini; Catarrhini; Hominidae;\nOC   Homo.\nOX   NCBI_TaxID=9606;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 28,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2R8YED5?format=txt&versions=28)

```json
{
  "evidence_id": "H2",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A2R8YED5?format=txt&versions=28",
  "source_sha256": "cca1844e232709cdf49594e55779c1f7550585001e53d4c1927ed8cbc4f14327",
  "retrieved_utc": "2026-11-01T06:27:26.314292+00:00",
  "source_locator": "lines 135-137",
  "excerpt": "FT   TOPO_DOM        1..28\nFT                   /note=\"Extracellular\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 28,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2R8YED5?format=txt&versions=28)

```json
{
  "evidence_id": "H3",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A2R8YED5?format=txt&versions=28",
  "source_sha256": "cca1844e232709cdf49594e55779c1f7550585001e53d4c1927ed8cbc4f14327",
  "retrieved_utc": "2026-11-01T06:27:26.314292+00:00",
  "source_locator": "lines 138-140",
  "excerpt": "FT   TRANSMEM        29..49\nFT                   /note=\"Helical; Name=1\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 28,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2R8YED5?format=txt&versions=28)

```json
{
  "evidence_id": "H4",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A2R8YED5?format=txt&versions=28",
  "source_sha256": "cca1844e232709cdf49594e55779c1f7550585001e53d4c1927ed8cbc4f14327",
  "retrieved_utc": "2026-11-01T06:27:26.314292+00:00",
  "source_locator": "lines 141-143",
  "excerpt": "FT   TOPO_DOM        50..65\nFT                   /note=\"Cytoplasmic\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 28,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2R8YED5?format=txt&versions=28)

```json
{
  "evidence_id": "H5",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A2R8YED5?format=txt&versions=28",
  "source_sha256": "cca1844e232709cdf49594e55779c1f7550585001e53d4c1927ed8cbc4f14327",
  "retrieved_utc": "2026-11-01T06:27:26.314292+00:00",
  "source_locator": "lines 144-146",
  "excerpt": "FT   TRANSMEM        66..86\nFT                   /note=\"Helical; Name=2\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 28,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2R8YED5?format=txt&versions=28)

```json
{
  "evidence_id": "H6",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A2R8YED5?format=txt&versions=28",
  "source_sha256": "cca1844e232709cdf49594e55779c1f7550585001e53d4c1927ed8cbc4f14327",
  "retrieved_utc": "2026-11-01T06:27:26.314292+00:00",
  "source_locator": "lines 147-149",
  "excerpt": "FT   TOPO_DOM        87..97\nFT                   /note=\"Extracellular\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 28,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2R8YED5?format=txt&versions=28)

```json
{
  "evidence_id": "H7",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A2R8YED5?format=txt&versions=28",
  "source_sha256": "cca1844e232709cdf49594e55779c1f7550585001e53d4c1927ed8cbc4f14327",
  "retrieved_utc": "2026-11-01T06:27:26.314292+00:00",
  "source_locator": "lines 150-152",
  "excerpt": "FT   TRANSMEM        98..118\nFT                   /note=\"Helical; Name=3\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 28,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2R8YED5?format=txt&versions=28)

```json
{
  "evidence_id": "H8",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A2R8YED5?format=txt&versions=28",
  "source_sha256": "cca1844e232709cdf49594e55779c1f7550585001e53d4c1927ed8cbc4f14327",
  "retrieved_utc": "2026-11-01T06:27:26.314292+00:00",
  "source_locator": "lines 153-155",
  "excerpt": "FT   TOPO_DOM        119..140\nFT                   /note=\"Cytoplasmic\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 28,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2R8YED5?format=txt&versions=28)

```json
{
  "evidence_id": "H9",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A2R8YED5?format=txt&versions=28",
  "source_sha256": "cca1844e232709cdf49594e55779c1f7550585001e53d4c1927ed8cbc4f14327",
  "retrieved_utc": "2026-11-01T06:27:26.314292+00:00",
  "source_locator": "lines 156-158",
  "excerpt": "FT   TRANSMEM        141..163\nFT                   /note=\"Helical; Name=4\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 28,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H10

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2R8YED5?format=txt&versions=28)

```json
{
  "evidence_id": "H10",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A2R8YED5?format=txt&versions=28",
  "source_sha256": "cca1844e232709cdf49594e55779c1f7550585001e53d4c1927ed8cbc4f14327",
  "retrieved_utc": "2026-11-01T06:27:26.314292+00:00",
  "source_locator": "lines 159-161",
  "excerpt": "FT   TOPO_DOM        164..195\nFT                   /note=\"Extracellular\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 28,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H11

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2R8YED5?format=txt&versions=28)

```json
{
  "evidence_id": "H11",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A2R8YED5?format=txt&versions=28",
  "source_sha256": "cca1844e232709cdf49594e55779c1f7550585001e53d4c1927ed8cbc4f14327",
  "retrieved_utc": "2026-11-01T06:27:26.314292+00:00",
  "source_locator": "lines 162-164",
  "excerpt": "FT   TRANSMEM        196..216\nFT                   /note=\"Helical; Name=5\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 28,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H12

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2R8YED5?format=txt&versions=28)

```json
{
  "evidence_id": "H12",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A2R8YED5?format=txt&versions=28",
  "source_sha256": "cca1844e232709cdf49594e55779c1f7550585001e53d4c1927ed8cbc4f14327",
  "retrieved_utc": "2026-11-01T06:27:26.314292+00:00",
  "source_locator": "lines 165-167",
  "excerpt": "FT   TOPO_DOM        217..236\nFT                   /note=\"Cytoplasmic\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 28,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H13

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2R8YED5?format=txt&versions=28)

```json
{
  "evidence_id": "H13",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A2R8YED5?format=txt&versions=28",
  "source_sha256": "cca1844e232709cdf49594e55779c1f7550585001e53d4c1927ed8cbc4f14327",
  "retrieved_utc": "2026-11-01T06:27:26.314292+00:00",
  "source_locator": "lines 168-170",
  "excerpt": "FT   TRANSMEM        237..257\nFT                   /note=\"Helical; Name=6\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 28,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H14

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2R8YED5?format=txt&versions=28)

```json
{
  "evidence_id": "H14",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A2R8YED5?format=txt&versions=28",
  "source_sha256": "cca1844e232709cdf49594e55779c1f7550585001e53d4c1927ed8cbc4f14327",
  "retrieved_utc": "2026-11-01T06:27:26.314292+00:00",
  "source_locator": "lines 171-173",
  "excerpt": "FT   TOPO_DOM        258..269\nFT                   /note=\"Extracellular\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 28,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H15

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2R8YED5?format=txt&versions=28)

```json
{
  "evidence_id": "H15",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A2R8YED5?format=txt&versions=28",
  "source_sha256": "cca1844e232709cdf49594e55779c1f7550585001e53d4c1927ed8cbc4f14327",
  "retrieved_utc": "2026-11-01T06:27:26.314292+00:00",
  "source_locator": "lines 174-176",
  "excerpt": "FT   TRANSMEM        270..290\nFT                   /note=\"Helical; Name=7\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 28,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H16

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2R8YED5?format=txt&versions=28)

```json
{
  "evidence_id": "H16",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A2R8YED5?format=txt&versions=28",
  "source_sha256": "cca1844e232709cdf49594e55779c1f7550585001e53d4c1927ed8cbc4f14327",
  "retrieved_utc": "2026-11-01T06:27:26.314292+00:00",
  "source_locator": "lines 177-179",
  "excerpt": "FT   TOPO_DOM        291..311\nFT                   /note=\"Cytoplasmic\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 28,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json), zero-based source row 13. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
