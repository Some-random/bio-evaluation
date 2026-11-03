# transmembrane_0025: before and after transfer clarification

[All 1,328 cases](../README.md) · [Method](../METHOD.md) · [Summary](../SUMMARY.md) · [Exact reviewer user message](../inputs/transmembrane_0025.txt)

**Task:** `transmembrane`  
**Author key, unchanged:** **B** — 9..45; 50..80; 86..121; 130..156; 173..211; 216..251; 268..296

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
MSNFTPDACNVDSGLDSVLPPSLYALVFTLGLPANLLALWAAWLQVRKGRELGVYLLNLSLSDLLLICALPPWTDYYLRRDVWGYGPGACRLFGFVFYTNLYVGAAFLSCVSADRYLAVAHPLRFPGARPIRSAAAVSALIWMLELAANAPPLLGEAIHRDRYNHTFCYESYPLSGRGAALANVGRVLAGFLLPWGVMMLCYAGLLRALRGSASCEQRERRRVRRLALGLPCVALLCYGPYHALLLLRSLVFLVGGGSVDAGGGCALEERLFPAYHASLALATLNCLADPALYCLACPGARGEVAKVVGGVVAWAMGKERRAWGERGGNGRGCGEGEEVGMVELRGNGREFVV

[Multiple Choices]
A. 5..25
B. 9..45; 50..80; 86..121; 130..156; 173..211; 216..251; 268..296
C. 9..45; 50..80; 89..125; 130..156; 173..211; 216..251; 268..296
D. 9..45; 50..80; 86..121; 130..156; 173..211; 216..251
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

> The supplied sequence exactly matches the historical and current UniProt sequence. The matched entry annotates seven transmembrane helices at the coordinates listed in B, with ECO:0000269 evidence linked to the cited study. This supports B, though the primary study was not independently reviewed here.

Citations as saved: [H4](#evidence-h4), [H6](#evidence-h6), [H8](#evidence-h8), [H10](#evidence-h10), [H12](#evidence-h12), [H14](#evidence-h14), [H16](#evidence-h16), [C6](#evidence-c6), [C8](#evidence-c8), [C10](#evidence-c10), [C12](#evidence-c12), [C14](#evidence-c14), [C16](#evidence-c16), [C18](#evidence-c18).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The strongly hydrophobic stretches and seven-helix pattern support a multi-pass, likely seven-transmembrane protein. They do not reliably establish the exact boundaries needed to distinguish B from C, which differ at the third segment.


**Missing item-specific fact**

> The protein-specific transmembrane boundary annotation or structural/topological evidence identifying the third helix as 86..121 rather than 89..125.


**Reason**

> Selecting the exact keyed intervals, especially between the near-identical B and C options, depends on item-specific boundary information not supplied in the question. Recognizing the sequence or recalling its annotation would be lookup, not sequence-based reasoning.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "C"
]
```

> From the sequence alone, both options give seven largely hydrophobic segments, and the small shift in the third segment's boundaries is not decisively resolved by generic hydrophobicity reasoning. The reviewer-only annotation supports B.


### Important caveats

- The annotation evidence is linked to a publication using ECO:0000269, but the primary paper was not independently validated here.
- The exact author source snapshot is unknown; the sequence matches the available historical and current records.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The strongly hydrophobic stretches and seven-helix pattern support a multi-pass, likely seven-transmembrane protein. They do not reliably establish the exact boundaries needed to distinguish B from C, which differ at the third segment.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific transmembrane boundary annotation or structural/topological evidence identifying the third helix as 86..121 rather than 89..125.",
    "reason": "Selecting the exact keyed intervals, especially between the near-identical B and C options, depends on item-specific boundary information not supplied in the question. Recognizing the sequence or recalling its annotation would be lookup, not sequence-based reasoning."
  },
  "case_id": "transmembrane_0025",
  "expected_answer_check": {
    "evidence_ids": [
      "H4",
      "H6",
      "H8",
      "H10",
      "H12",
      "H14",
      "H16",
      "C6",
      "C8",
      "C10",
      "C12",
      "C14",
      "C16",
      "C18"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the historical and current UniProt sequence. The matched entry annotates seven transmembrane helices at the coordinates listed in B, with ECO:0000269 evidence linked to the cited study. This supports B, though the primary study was not independently reviewed here."
  },
  "important_caveats": [
    "The annotation evidence is linked to a publication using ECO:0000269, but the primary paper was not independently validated here.",
    "The exact author source snapshot is unknown; the sequence matches the available historical and current records."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "C"
    ],
    "reason": "From the sequence alone, both options give seven largely hydrophobic segments, and the small shift in the third segment's boundaries is not decisively resolved by generic hydrophobicity reasoning. The reviewer-only annotation supports B."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0025",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the historical and current UniProt sequence. The matched entry annotates seven transmembrane helices at the coordinates listed in B, with ECO:0000269 evidence linked to the cited study. This supports B, though the primary study was not independently reviewed here.",
    "evidence_ids": ["H4", "H6", "H8", "H10", "H12", "H14", "H16", "C6", "C8", "C10", "C12", "C14", "C16", "C18"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The strongly hydrophobic stretches and seven-helix pattern support a multi-pass, likely seven-transmembrane protein. They do not reliably establish the exact boundaries needed to distinguish B from C, which differ at the third segment.",
    "missing_item_specific_fact": "The protein-specific transmembrane boundary annotation or structural/topological evidence identifying the third helix as 86..121 rather than 89..125.",
    "reason": "Selecting the exact keyed intervals, especially between the near-identical B and C options, depends on item-specific boundary information not supplied in the question. Recognizing the sequence or recalling its annotation would be lookup, not sequence-based reasoning."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "C"],
    "reason": "From the sequence alone, both options give seven largely hydrophobic segments, and the small shift in the third segment's boundaries is not decisively resolved by generic hydrophobicity reasoning. The reviewer-only annotation supports B."
  },
  "important_caveats": [
    "The annotation evidence is linked to a publication using ECO:0000269, but the primary paper was not independently validated here.",
    "The exact author source snapshot is unknown; the sequence matches the available historical and current records."
  ]
}
```

</details>

## Before: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The expected answer B (9..45; 50..80; 86..121; 130..156; 173..211; 216..251; 268..296) matches exactly the seven transmembrane helix boundaries annotated in UniProt entry A0A6I8PUB9 (Xenopus tropicalis GPR4). Each TM segment is annotated with evidence code ECO:0000269 (experimental evidence) from PubMed:39753131, a cryo-EM structure paper (Wen et al., Cell 2025). The sequence in the question matches the UniProt sequence (353 AA, SHA-256 confirmed). Option C differs in TM3 boundaries (89..125 vs 86..121), option D omits TM7 (268..296), and option A is a single short segment incompatible with a 7TM receptor.

Citations as saved: [C6](#evidence-c6), [C8](#evidence-c8), [C10](#evidence-c10), [C12](#evidence-c12), [C14](#evidence-c14), [C16](#evidence-c16), [C18](#evidence-c18), [H4](#evidence-h4), [H6](#evidence-h6), [H8](#evidence-h8), [H10](#evidence-h10), [H12](#evidence-h12), [H14](#evidence-h14), [H16](#evidence-h16).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> General GPCR biology (7 transmembrane helices) allows elimination of option A (single 21-residue segment) and option D (only 6 TMs). The approximate positions of the seven hydrophobic stretches can be estimated from the sequence, broadly matching both B and C. However, the critical distinction between B and C is the exact boundary of TM3: B gives 86..121 while C gives 89..125. This 3-residue N-terminal shift and 4-residue C-terminal shift cannot be resolved by hydrophobicity analysis or helix-propensity reasoning. The region 86–88 (GPG) and 122–125 (PLRF) are neither clearly hydrophobic nor clearly helix-breaking in a way that definitively favors one boundary. The correct boundaries (86..121) were determined by cryo-EM structural analysis (PubMed:39753131), an item-specific experimental measurement not derivable from the sequence alone.


**Missing item-specific fact**

> The exact cryo-EM–determined boundaries of TM3 (residues 86–121) for this specific Xenopus tropicalis GPR4 structure, which distinguish option B (86..121) from option C (89..125). No general biological principle or sequence heuristic reliably resolves a 3–4 residue boundary shift in a GPCR TM helix containing multiple polar/charged residues.


**Reason**

> While recognizing the protein as a 7TM GPCR and estimating approximate TM positions is reasoning-supported, the final choice between B and C hinges on the precise experimentally determined TM3 boundaries from a specific cryo-EM study. A sequence-only analysis cannot distinguish GPG at position 86–88 (included in B's TM3) from their exclusion (C's TM3 starting at 89), nor can it determine whether the TM3 helix terminates at H121 or F125.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "C"
]
```

> Options B and C differ only in TM3 boundaries (86..121 vs 89..125). From the sequence alone, the residues GPG(86–88) and PLRF(122–125) are ambiguous as TM-inclusive or loop residues. A hydrophobicity or helix-propensity analysis could plausibly favor either boundary. Without the cryo-EM structural determination, both B and C are defensible. Options A and D are clearly eliminable (wrong number of TMs).


### Important caveats

- The UniProt TM annotations carry experimental evidence (ECO:0000269, cryo-EM structure from PubMed:39753131), making the boundaries experimentally determined rather than purely computational predictions.
- The question wording says 'a segment that crosses the membrane' (singular) but the answer choices list all seven TM segments. The intent is clearly to identify the complete set of TM regions.
- The reviewer-only evidence confirms the sequence match (SHA-256 identical) and that the annotation was present in the historical snapshot (entry version 25, released 2026-01-28), which is within the benchmark construction window.
- The GPG motif at positions 86–88 within TM3 is unusual for a transmembrane helix (proline is a helix breaker), yet the cryo-EM structure includes it within the TM helix, illustrating that simple helix-propensity heuristics would not reproduce the experimental boundaries.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "General GPCR biology (7 transmembrane helices) allows elimination of option A (single 21-residue segment) and option D (only 6 TMs). The approximate positions of the seven hydrophobic stretches can be estimated from the sequence, broadly matching both B and C. However, the critical distinction between B and C is the exact boundary of TM3: B gives 86..121 while C gives 89..125. This 3-residue N-terminal shift and 4-residue C-terminal shift cannot be resolved by hydrophobicity analysis or helix-propensity reasoning. The region 86–88 (GPG) and 122–125 (PLRF) are neither clearly hydrophobic nor clearly helix-breaking in a way that definitively favors one boundary. The correct boundaries (86..121) were determined by cryo-EM structural analysis (PubMed:39753131), an item-specific experimental measurement not derivable from the sequence alone.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The exact cryo-EM–determined boundaries of TM3 (residues 86–121) for this specific Xenopus tropicalis GPR4 structure, which distinguish option B (86..121) from option C (89..125). No general biological principle or sequence heuristic reliably resolves a 3–4 residue boundary shift in a GPCR TM helix containing multiple polar/charged residues.",
    "reason": "While recognizing the protein as a 7TM GPCR and estimating approximate TM positions is reasoning-supported, the final choice between B and C hinges on the precise experimentally determined TM3 boundaries from a specific cryo-EM study. A sequence-only analysis cannot distinguish GPG at position 86–88 (included in B's TM3) from their exclusion (C's TM3 starting at 89), nor can it determine whether the TM3 helix terminates at H121 or F125."
  },
  "case_id": "transmembrane_0025",
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
    "reason": "The expected answer B (9..45; 50..80; 86..121; 130..156; 173..211; 216..251; 268..296) matches exactly the seven transmembrane helix boundaries annotated in UniProt entry A0A6I8PUB9 (Xenopus tropicalis GPR4). Each TM segment is annotated with evidence code ECO:0000269 (experimental evidence) from PubMed:39753131, a cryo-EM structure paper (Wen et al., Cell 2025). The sequence in the question matches the UniProt sequence (353 AA, SHA-256 confirmed). Option C differs in TM3 boundaries (89..125 vs 86..121), option D omits TM7 (268..296), and option A is a single short segment incompatible with a 7TM receptor."
  },
  "important_caveats": [
    "The UniProt TM annotations carry experimental evidence (ECO:0000269, cryo-EM structure from PubMed:39753131), making the boundaries experimentally determined rather than purely computational predictions.",
    "The question wording says 'a segment that crosses the membrane' (singular) but the answer choices list all seven TM segments. The intent is clearly to identify the complete set of TM regions.",
    "The reviewer-only evidence confirms the sequence match (SHA-256 identical) and that the annotation was present in the historical snapshot (entry version 25, released 2026-01-28), which is within the benchmark construction window.",
    "The GPG motif at positions 86–88 within TM3 is unusual for a transmembrane helix (proline is a helix breaker), yet the cryo-EM structure includes it within the TM helix, illustrating that simple helix-propensity heuristics would not reproduce the experimental boundaries."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "C"
    ],
    "reason": "Options B and C differ only in TM3 boundaries (86..121 vs 89..125). From the sequence alone, the residues GPG(86–88) and PLRF(122–125) are ambiguous as TM-inclusive or loop residues. A hydrophobicity or helix-propensity analysis could plausibly favor either boundary. Without the cryo-EM structural determination, both B and C are defensible. Options A and D are clearly eliminable (wrong number of TMs)."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0025",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The expected answer B (9..45; 50..80; 86..121; 130..156; 173..211; 216..251; 268..296) matches exactly the seven transmembrane helix boundaries annotated in UniProt entry A0A6I8PUB9 (Xenopus tropicalis GPR4). Each TM segment is annotated with evidence code ECO:0000269 (experimental evidence) from PubMed:39753131, a cryo-EM structure paper (Wen et al., Cell 2025). The sequence in the question matches the UniProt sequence (353 AA, SHA-256 confirmed). Option C differs in TM3 boundaries (89..125 vs 86..121), option D omits TM7 (268..296), and option A is a single short segment incompatible with a 7TM receptor.",
    "evidence_ids": ["C6", "C8", "C10", "C12", "C14", "C16", "C18", "H4", "H6", "H8", "H10", "H12", "H14", "H16"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "General GPCR biology (7 transmembrane helices) allows elimination of option A (single 21-residue segment) and option D (only 6 TMs). The approximate positions of the seven hydrophobic stretches can be estimated from the sequence, broadly matching both B and C. However, the critical distinction between B and C is the exact boundary of TM3: B gives 86..121 while C gives 89..125. This 3-residue N-terminal shift and 4-residue C-terminal shift cannot be resolved by hydrophobicity analysis or helix-propensity reasoning. The region 86–88 (GPG) and 122–125 (PLRF) are neither clearly hydrophobic nor clearly helix-breaking in a way that definitively favors one boundary. The correct boundaries (86..121) were determined by cryo-EM structural analysis (PubMed:39753131), an item-specific experimental measurement not derivable from the sequence alone.",
    "missing_item_specific_fact": "The exact cryo-EM–determined boundaries of TM3 (residues 86–121) for this specific Xenopus tropicalis GPR4 structure, which distinguish option B (86..121) from option C (89..125). No general biological principle or sequence heuristic reliably resolves a 3–4 residue boundary shift in a GPCR TM helix containing multiple polar/charged residues.",
    "reason": "While recognizing the protein as a 7TM GPCR and estimating approximate TM positions is reasoning-supported, the final choice between B and C hinges on the precise experimentally determined TM3 boundaries from a specific cryo-EM study. A sequence-only analysis cannot distinguish GPG at position 86–88 (included in B's TM3) from their exclusion (C's TM3 starting at 89), nor can it determine whether the TM3 helix terminates at H121 or F125."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "C"],
    "reason": "Options B and C differ only in TM3 boundaries (86..121 vs 89..125). From the sequence alone, the residues GPG(86–88) and PLRF(122–125) are ambiguous as TM-inclusive or loop residues. A hydrophobicity or helix-propensity analysis could plausibly favor either boundary. Without the cryo-EM structural determination, both B and C are defensible. Options A and D are clearly eliminable (wrong number of TMs)."
  },
  "important_caveats": [
    "The UniProt TM annotations carry experimental evidence (ECO:0000269, cryo-EM structure from PubMed:39753131), making the boundaries experimentally determined rather than purely computational predictions.",
    "The question wording says 'a segment that crosses the membrane' (singular) but the answer choices list all seven TM segments. The intent is clearly to identify the complete set of TM regions.",
    "The reviewer-only evidence confirms the sequence match (SHA-256 identical) and that the annotation was present in the historical snapshot (entry version 25, released 2026-01-28), which is within the benchmark construction window.",
    "The GPG motif at positions 86–88 within TM3 is unusual for a transmembrane helix (proline is a helix breaker), yet the cryo-EM structure includes it within the TM helix, illustrating that simple helix-propensity heuristics would not reproduce the experimental boundaries."
  ]
}
```

</details>

## After: GPT-6 Luna

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence-matched UniProt record annotates the seven transmembrane helices at the coordinates in choice B. The annotations cite experimental evidence (ECO:0000269) and the associated structural study, though the supplied excerpts do not independently validate that study's results.

Citations as saved: [C6](#evidence-c6), [C8](#evidence-c8), [C10](#evidence-c10), [C12](#evidence-c12), [C14](#evidence-c14), [C16](#evidence-c16), [C18](#evidence-c18).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence is strongly characteristic of a seven-transmembrane GPCR: its hydrophobic stretches and alternating loops make the seven-helix choices much more credible than A or D. That family-level inference does not robustly distinguish B from C, which differ only in the boundaries assigned to the third helix.


**Missing item-specific fact**

> The exact boundary annotation for the third transmembrane helix in this protein is needed to choose between B and C.


**Reason**

> Transferable GPCR knowledge supports the overall topology, but the third-helix boundary shift is too small and ambiguous to select one interval confidently from sequence pattern alone. The exact annotated coordinates are a fact about this protein.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "C"
]
```

> B and C both describe the same apparent seven-helix topology and differ only by a few residues at the third helix's boundaries. Such close boundary choices are not clearly distinguished by the question's wording or by an unambiguous sequence feature.


### Important caveats

- The reviewer-only source record matches the supplied sequence; its identity and annotations were not part of the original model input.
- Transmembrane helix boundaries can be convention-dependent, so support for the recorded coordinates does not make the nearby alternative biologically impossible.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is strongly characteristic of a seven-transmembrane GPCR: its hydrophobic stretches and alternating loops make the seven-helix choices much more credible than A or D. That family-level inference does not robustly distinguish B from C, which differ only in the boundaries assigned to the third helix.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The exact boundary annotation for the third transmembrane helix in this protein is needed to choose between B and C.",
    "reason": "Transferable GPCR knowledge supports the overall topology, but the third-helix boundary shift is too small and ambiguous to select one interval confidently from sequence pattern alone. The exact annotated coordinates are a fact about this protein."
  },
  "case_id": "transmembrane_0025",
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
    "reason": "The sequence-matched UniProt record annotates the seven transmembrane helices at the coordinates in choice B. The annotations cite experimental evidence (ECO:0000269) and the associated structural study, though the supplied excerpts do not independently validate that study's results."
  },
  "important_caveats": [
    "The reviewer-only source record matches the supplied sequence; its identity and annotations were not part of the original model input.",
    "Transmembrane helix boundaries can be convention-dependent, so support for the recorded coordinates does not make the nearby alternative biologically impossible."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "C"
    ],
    "reason": "B and C both describe the same apparent seven-helix topology and differ only by a few residues at the third helix's boundaries. Such close boundary choices are not clearly distinguished by the question's wording or by an unambiguous sequence feature."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0025",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates the seven transmembrane helices at the coordinates in choice B. The annotations cite experimental evidence (ECO:0000269) and the associated structural study, though the supplied excerpts do not independently validate that study's results.",
    "evidence_ids": ["C6", "C8", "C10", "C12", "C14", "C16", "C18"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence is strongly characteristic of a seven-transmembrane GPCR: its hydrophobic stretches and alternating loops make the seven-helix choices much more credible than A or D. That family-level inference does not robustly distinguish B from C, which differ only in the boundaries assigned to the third helix.",
    "missing_item_specific_fact": "The exact boundary annotation for the third transmembrane helix in this protein is needed to choose between B and C.",
    "reason": "Transferable GPCR knowledge supports the overall topology, but the third-helix boundary shift is too small and ambiguous to select one interval confidently from sequence pattern alone. The exact annotated coordinates are a fact about this protein."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "C"],
    "reason": "B and C both describe the same apparent seven-helix topology and differ only by a few residues at the third helix's boundaries. Such close boundary choices are not clearly distinguished by the question's wording or by an unambiguous sequence feature."
  },
  "important_caveats": [
    "The reviewer-only source record matches the supplied sequence; its identity and annotations were not part of the original model input.",
    "Transmembrane helix boundaries can be convention-dependent, so support for the recorded coordinates does not make the nearby alternative biologically impossible."
  ]
}
```

</details>

## After: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A0A6I8PUB9 annotates exactly seven transmembrane helices at 9..45, 50..80, 86..121, 130..156, 173..211, 216..251, and 268..296, all with experimental evidence (ECO:0000269, cryo-EM structure from PubMed:39753131). This matches option B precisely.

Citations as saved: [C6](#evidence-c6), [C8](#evidence-c8), [C10](#evidence-c10), [C12](#evidence-c12), [C14](#evidence-c14), [C16](#evidence-c16), [C18](#evidence-c18).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is 353 residues with a pattern of seven long hydrophobic stretches separated by short polar/charged loops, consistent with a 7-TM GPCR. This eliminates A (single 21-residue segment) and D (only six TMs). The remaining distinction between B and C concerns TM3 boundaries (86..121 vs 89..125). In option C, TM3 would extend to residue 125, incorporating positions 122-125 (PLRF). Position 124 is arginine (R), a strongly charged residue that is thermodynamically unfavorable in the hydrophobic core of a transmembrane helix. In GPCRs, the cytoplasmic loop between TM3 and TM4 typically contains such charged residues (e.g., the conserved DRY motif region). Placing R within the TM helix contradicts the well-established principle that charged residues reside in aqueous loops. Additionally, the 5-residue extracellular loop (81-85: DVWGY) before TM3 is consistent with the short loops seen in GPCR crystal/cryo-EM structures, supporting a TM3 start near 86 rather than 89. The combination of 7-TM topology knowledge and the charged-residue-in-loop principle provides a credible transferable basis to select B over C.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can apply GPCR 7-TM topology to eliminate A and D, then use the principle that charged residues (R at position 124) belong in cytoplasmic loops rather than TM helix interiors to reject C's extended TM3 boundary. The GPG segment at 86-88 is a short polar dip tolerable at a TM boundary in GPCR structures. These are transferable biophysical and structural principles learned from many GPCRs.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Option A is clearly wrong (single short segment), D lacks the 7th TM, and C includes a charged arginine within TM3 which contradicts TM helix biophysics. B is the only option consistent with both 7-TM GPCR topology and hydrophobicity constraints.


### Important caveats

- The exact TM boundaries in the UniProt entry were determined by cryo-EM structure (experimental), so the precise residue-level boundaries (e.g., 86 vs 89 for TM3 start) may not be perfectly reproducible by hydropathy analysis alone.
- The GPG segment at positions 86-88 is a borderline case for TM inclusion; a model relying solely on hydrophobicity might exclude it, but the charged-residue argument for the C-terminal boundary (position 124) is more decisive.
- The reviewer-only evidence confirms the sequence matches the benchmark input exactly (SHA256 match), validating that the annotation applies to the supplied sequence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is 353 residues with a pattern of seven long hydrophobic stretches separated by short polar/charged loops, consistent with a 7-TM GPCR. This eliminates A (single 21-residue segment) and D (only six TMs). The remaining distinction between B and C concerns TM3 boundaries (86..121 vs 89..125). In option C, TM3 would extend to residue 125, incorporating positions 122-125 (PLRF). Position 124 is arginine (R), a strongly charged residue that is thermodynamically unfavorable in the hydrophobic core of a transmembrane helix. In GPCRs, the cytoplasmic loop between TM3 and TM4 typically contains such charged residues (e.g., the conserved DRY motif region). Placing R within the TM helix contradicts the well-established principle that charged residues reside in aqueous loops. Additionally, the 5-residue extracellular loop (81-85: DVWGY) before TM3 is consistent with the short loops seen in GPCR crystal/cryo-EM structures, supporting a TM3 start near 86 rather than 89. The combination of 7-TM topology knowledge and the charged-residue-in-loop principle provides a credible transferable basis to select B over C.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can apply GPCR 7-TM topology to eliminate A and D, then use the principle that charged residues (R at position 124) belong in cytoplasmic loops rather than TM helix interiors to reject C's extended TM3 boundary. The GPG segment at 86-88 is a short polar dip tolerable at a TM boundary in GPCR structures. These are transferable biophysical and structural principles learned from many GPCRs."
  },
  "case_id": "transmembrane_0025",
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
    "reason": "The UniProt entry A0A6I8PUB9 annotates exactly seven transmembrane helices at 9..45, 50..80, 86..121, 130..156, 173..211, 216..251, and 268..296, all with experimental evidence (ECO:0000269, cryo-EM structure from PubMed:39753131). This matches option B precisely."
  },
  "important_caveats": [
    "The exact TM boundaries in the UniProt entry were determined by cryo-EM structure (experimental), so the precise residue-level boundaries (e.g., 86 vs 89 for TM3 start) may not be perfectly reproducible by hydropathy analysis alone.",
    "The GPG segment at positions 86-88 is a borderline case for TM inclusion; a model relying solely on hydrophobicity might exclude it, but the charged-residue argument for the C-terminal boundary (position 124) is more decisive.",
    "The reviewer-only evidence confirms the sequence matches the benchmark input exactly (SHA256 match), validating that the annotation applies to the supplied sequence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Option A is clearly wrong (single short segment), D lacks the 7th TM, and C includes a charged arginine within TM3 which contradicts TM helix biophysics. B is the only option consistent with both 7-TM GPCR topology and hydrophobicity constraints."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0025",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A0A6I8PUB9 annotates exactly seven transmembrane helices at 9..45, 50..80, 86..121, 130..156, 173..211, 216..251, and 268..296, all with experimental evidence (ECO:0000269, cryo-EM structure from PubMed:39753131). This matches option B precisely.",
    "evidence_ids": ["C6", "C8", "C10", "C12", "C14", "C16", "C18"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is 353 residues with a pattern of seven long hydrophobic stretches separated by short polar/charged loops, consistent with a 7-TM GPCR. This eliminates A (single 21-residue segment) and D (only six TMs). The remaining distinction between B and C concerns TM3 boundaries (86..121 vs 89..125). In option C, TM3 would extend to residue 125, incorporating positions 122-125 (PLRF). Position 124 is arginine (R), a strongly charged residue that is thermodynamically unfavorable in the hydrophobic core of a transmembrane helix. In GPCRs, the cytoplasmic loop between TM3 and TM4 typically contains such charged residues (e.g., the conserved DRY motif region). Placing R within the TM helix contradicts the well-established principle that charged residues reside in aqueous loops. Additionally, the 5-residue extracellular loop (81-85: DVWGY) before TM3 is consistent with the short loops seen in GPCR crystal/cryo-EM structures, supporting a TM3 start near 86 rather than 89. The combination of 7-TM topology knowledge and the charged-residue-in-loop principle provides a credible transferable basis to select B over C.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can apply GPCR 7-TM topology to eliminate A and D, then use the principle that charged residues (R at position 124) belong in cytoplasmic loops rather than TM helix interiors to reject C's extended TM3 boundary. The GPG segment at 86-88 is a short polar dip tolerable at a TM boundary in GPCR structures. These are transferable biophysical and structural principles learned from many GPCRs."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Option A is clearly wrong (single short segment), D lacks the 7th TM, and C includes a charged arginine within TM3 which contradicts TM helix biophysics. B is the only option consistent with both 7-TM GPCR topology and hydrophobicity constraints."
  },
  "important_caveats": [
    "The exact TM boundaries in the UniProt entry were determined by cryo-EM structure (experimental), so the precise residue-level boundaries (e.g., 86 vs 89 for TM3 start) may not be perfectly reproducible by hydropathy analysis alone.",
    "The GPG segment at positions 86-88 is a borderline case for TM inclusion; a model relying solely on hydrophobicity might exclude it, but the charged-residue argument for the C-terminal boundary (position 124) is more decisive.",
    "The reviewer-only evidence confirms the sequence matches the benchmark input exactly (SHA256 match), validating that the annotation applies to the supplied sequence."
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
  "requested_accession": "A0A6I8PUB9",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "benchmark_sequence_sha256": "7093384a068f217cd38de58555a2ce625b886a7c15c3e1a032328261341f4f66",
  "benchmark_sequence_length": 353,
  "current_status": "retrieved",
  "current_sequence_comparison": "matched",
  "current_entry_audit": {
    "entryVersion": 27,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2020-08-12",
    "sequenceVersion": 1
  },
  "current_uniprot_release": "2026_03",
  "current_record_sha256": "a744101e779b456c34c37646ab2aee926ca32698d73eef5421228a17149aa4e1",
  "current_source_sequence_sha256": "7093384a068f217cd38de58555a2ce625b886a7c15c3e1a032328261341f4f66",
  "current_source_sequence_length": 353,
  "historical_status": "retrieved",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "selected_historical_entry_version": 25,
  "selected_historical_version": {
    "accession": "A0A6I8PUB9",
    "database": "Swiss-Prot",
    "entryVersion": 25,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "GPR4_XENTR",
    "sequenceVersion": 1
  },
  "selected_historical_record_sha256": "57795ac8541e9349c417ffab8858e9955615bd1d0fd8bb5a206b1104334eba37",
  "selected_historical_source_sequence_sha256": "7093384a068f217cd38de58555a2ce625b886a7c15c3e1a032328261341f4f66",
  "selected_historical_source_sequence_length": 353,
  "latest_at_cutoff_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 25,
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A6I8PUB9.json)

```json
{
  "evidence_id": "C1",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A6I8PUB9.json",
  "source_sha256": "a744101e779b456c34c37646ab2aee926ca32698d73eef5421228a17149aa4e1",
  "retrieved_utc": "2026-11-02T04:25:33.494326+00:00",
  "json_pointer": "/primaryAccession",
  "excerpt": "\"A0A6I8PUB9\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A6I8PUB9.json)

```json
{
  "evidence_id": "C2",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A6I8PUB9.json",
  "source_sha256": "a744101e779b456c34c37646ab2aee926ca32698d73eef5421228a17149aa4e1",
  "retrieved_utc": "2026-11-02T04:25:33.494326+00:00",
  "json_pointer": "/entryAudit",
  "excerpt": "{\"entryVersion\":27,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2020-08-12\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A6I8PUB9.json)

```json
{
  "evidence_id": "C3",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A6I8PUB9.json",
  "source_sha256": "a744101e779b456c34c37646ab2aee926ca32698d73eef5421228a17149aa4e1",
  "retrieved_utc": "2026-11-02T04:25:33.494326+00:00",
  "json_pointer": "/organism",
  "excerpt": "{\"commonName\":\"Western clawed frog\",\"lineage\":[\"Eukaryota\",\"Metazoa\",\"Chordata\",\"Craniata\",\"Vertebrata\",\"Euteleostomi\",\"Amphibia\",\"Batrachia\",\"Anura\",\"Pipoidea\",\"Pipidae\",\"Xenopodinae\",\"Xenopus\",\"Silurana\"],\"scientificName\":\"Xenopus tropicalis\",\"synonyms\":[\"Silurana tropicalis\"],\"taxonId\":8364}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A6I8PUB9.json)

```json
{
  "evidence_id": "C4",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A6I8PUB9.json",
  "source_sha256": "a744101e779b456c34c37646ab2aee926ca32698d73eef5421228a17149aa4e1",
  "retrieved_utc": "2026-11-02T04:25:33.494326+00:00",
  "json_pointer": "/proteinDescription",
  "excerpt": "{\"recommendedName\":{\"fullName\":{\"value\":\"G protein-coupled receptor 4\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39753131\",\"source\":\"PubMed\"}],\"value\":\"XtGPR4\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A6I8PUB9.json)

```json
{
  "evidence_id": "C5",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A6I8PUB9.json",
  "source_sha256": "a744101e779b456c34c37646ab2aee926ca32698d73eef5421228a17149aa4e1",
  "retrieved_utc": "2026-11-02T04:25:33.494326+00:00",
  "json_pointer": "/features/1",
  "excerpt": "{\"description\":\"Extracellular\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39753131\",\"source\":\"PubMed\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":8},\"start\":{\"modifier\":\"EXACT\",\"value\":1}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A6I8PUB9.json)

```json
{
  "evidence_id": "C6",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A6I8PUB9.json",
  "source_sha256": "a744101e779b456c34c37646ab2aee926ca32698d73eef5421228a17149aa4e1",
  "retrieved_utc": "2026-11-02T04:25:33.494326+00:00",
  "json_pointer": "/features/2",
  "excerpt": "{\"description\":\"Helical; Name=1\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39753131\",\"source\":\"PubMed\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":45},\"start\":{\"modifier\":\"EXACT\",\"value\":9}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A6I8PUB9.json)

```json
{
  "evidence_id": "C7",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A6I8PUB9.json",
  "source_sha256": "a744101e779b456c34c37646ab2aee926ca32698d73eef5421228a17149aa4e1",
  "retrieved_utc": "2026-11-02T04:25:33.494326+00:00",
  "json_pointer": "/features/3",
  "excerpt": "{\"description\":\"Cytoplasmic\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39753131\",\"source\":\"PubMed\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":49},\"start\":{\"modifier\":\"EXACT\",\"value\":46}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A6I8PUB9.json)

```json
{
  "evidence_id": "C8",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A6I8PUB9.json",
  "source_sha256": "a744101e779b456c34c37646ab2aee926ca32698d73eef5421228a17149aa4e1",
  "retrieved_utc": "2026-11-02T04:25:33.494326+00:00",
  "json_pointer": "/features/4",
  "excerpt": "{\"description\":\"Helical; Name=2\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39753131\",\"source\":\"PubMed\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":80},\"start\":{\"modifier\":\"EXACT\",\"value\":50}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A6I8PUB9.json)

```json
{
  "evidence_id": "C9",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A6I8PUB9.json",
  "source_sha256": "a744101e779b456c34c37646ab2aee926ca32698d73eef5421228a17149aa4e1",
  "retrieved_utc": "2026-11-02T04:25:33.494326+00:00",
  "json_pointer": "/features/5",
  "excerpt": "{\"description\":\"Extracellular\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39753131\",\"source\":\"PubMed\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":85},\"start\":{\"modifier\":\"EXACT\",\"value\":81}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A6I8PUB9.json)

```json
{
  "evidence_id": "C10",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A6I8PUB9.json",
  "source_sha256": "a744101e779b456c34c37646ab2aee926ca32698d73eef5421228a17149aa4e1",
  "retrieved_utc": "2026-11-02T04:25:33.494326+00:00",
  "json_pointer": "/features/6",
  "excerpt": "{\"description\":\"Helical; Name=3\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39753131\",\"source\":\"PubMed\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":121},\"start\":{\"modifier\":\"EXACT\",\"value\":86}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A6I8PUB9.json)

```json
{
  "evidence_id": "C11",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A6I8PUB9.json",
  "source_sha256": "a744101e779b456c34c37646ab2aee926ca32698d73eef5421228a17149aa4e1",
  "retrieved_utc": "2026-11-02T04:25:33.494326+00:00",
  "json_pointer": "/features/7",
  "excerpt": "{\"description\":\"Cytoplasmic\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39753131\",\"source\":\"PubMed\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":129},\"start\":{\"modifier\":\"EXACT\",\"value\":122}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A6I8PUB9.json)

```json
{
  "evidence_id": "C12",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A6I8PUB9.json",
  "source_sha256": "a744101e779b456c34c37646ab2aee926ca32698d73eef5421228a17149aa4e1",
  "retrieved_utc": "2026-11-02T04:25:33.494326+00:00",
  "json_pointer": "/features/8",
  "excerpt": "{\"description\":\"Helical; Name=4\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39753131\",\"source\":\"PubMed\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":156},\"start\":{\"modifier\":\"EXACT\",\"value\":130}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C13

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A6I8PUB9.json)

```json
{
  "evidence_id": "C13",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A6I8PUB9.json",
  "source_sha256": "a744101e779b456c34c37646ab2aee926ca32698d73eef5421228a17149aa4e1",
  "retrieved_utc": "2026-11-02T04:25:33.494326+00:00",
  "json_pointer": "/features/9",
  "excerpt": "{\"description\":\"Extracellular\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39753131\",\"source\":\"PubMed\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":172},\"start\":{\"modifier\":\"EXACT\",\"value\":157}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C14

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A6I8PUB9.json)

```json
{
  "evidence_id": "C14",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A6I8PUB9.json",
  "source_sha256": "a744101e779b456c34c37646ab2aee926ca32698d73eef5421228a17149aa4e1",
  "retrieved_utc": "2026-11-02T04:25:33.494326+00:00",
  "json_pointer": "/features/10",
  "excerpt": "{\"description\":\"Helical; Name=5\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39753131\",\"source\":\"PubMed\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":211},\"start\":{\"modifier\":\"EXACT\",\"value\":173}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C15

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A6I8PUB9.json)

```json
{
  "evidence_id": "C15",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A6I8PUB9.json",
  "source_sha256": "a744101e779b456c34c37646ab2aee926ca32698d73eef5421228a17149aa4e1",
  "retrieved_utc": "2026-11-02T04:25:33.494326+00:00",
  "json_pointer": "/features/11",
  "excerpt": "{\"description\":\"Cytoplasmic\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39753131\",\"source\":\"PubMed\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":215},\"start\":{\"modifier\":\"EXACT\",\"value\":212}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C16

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A6I8PUB9.json)

```json
{
  "evidence_id": "C16",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A6I8PUB9.json",
  "source_sha256": "a744101e779b456c34c37646ab2aee926ca32698d73eef5421228a17149aa4e1",
  "retrieved_utc": "2026-11-02T04:25:33.494326+00:00",
  "json_pointer": "/features/12",
  "excerpt": "{\"description\":\"Helical; Name=6\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39753131\",\"source\":\"PubMed\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":251},\"start\":{\"modifier\":\"EXACT\",\"value\":216}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C17

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A6I8PUB9.json)

```json
{
  "evidence_id": "C17",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A6I8PUB9.json",
  "source_sha256": "a744101e779b456c34c37646ab2aee926ca32698d73eef5421228a17149aa4e1",
  "retrieved_utc": "2026-11-02T04:25:33.494326+00:00",
  "json_pointer": "/features/13",
  "excerpt": "{\"description\":\"Extracellular\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39753131\",\"source\":\"PubMed\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":267},\"start\":{\"modifier\":\"EXACT\",\"value\":252}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C18

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A6I8PUB9.json)

```json
{
  "evidence_id": "C18",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A6I8PUB9.json",
  "source_sha256": "a744101e779b456c34c37646ab2aee926ca32698d73eef5421228a17149aa4e1",
  "retrieved_utc": "2026-11-02T04:25:33.494326+00:00",
  "json_pointer": "/features/14",
  "excerpt": "{\"description\":\"Helical; Name=7\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39753131\",\"source\":\"PubMed\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":296},\"start\":{\"modifier\":\"EXACT\",\"value\":268}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C19

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A6I8PUB9.json)

```json
{
  "evidence_id": "C19",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A6I8PUB9.json",
  "source_sha256": "a744101e779b456c34c37646ab2aee926ca32698d73eef5421228a17149aa4e1",
  "retrieved_utc": "2026-11-02T04:25:33.494326+00:00",
  "json_pointer": "/features/15",
  "excerpt": "{\"description\":\"Cytoplasmic\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39753131\",\"source\":\"PubMed\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":353},\"start\":{\"modifier\":\"EXACT\",\"value\":297}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C20

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A6I8PUB9.json)

```json
{
  "evidence_id": "C20",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A6I8PUB9.json",
  "source_sha256": "a744101e779b456c34c37646ab2aee926ca32698d73eef5421228a17149aa4e1",
  "retrieved_utc": "2026-11-02T04:25:33.494326+00:00",
  "json_pointer": "/references/1",
  "excerpt": "{\"citation\":{\"authors\":[\"Wen X.\",\"Shang P.\",\"Chen H.\",\"Guo L.\",\"Rong N.\",\"Jiang X.\",\"Li X.\",\"Liu J.\",\"Yang G.\",\"Zhang J.\",\"Zhu K.\",\"Meng Q.\",\"He X.\",\"Wang Z.\",\"Liu Z.\",\"Cheng H.\",\"Zheng Y.\",\"Zhang B.\",\"Pang J.\",\"Liu Z.\",\"Xiao P.\",\"Chen Y.\",\"Liu L.\",\"Luo F.\",\"Yu X.\",\"Yi F.\",\"Zhang P.\",\"Yang F.\",\"Deng C.\",\"Sun J.P.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"39753131\"},{\"database\":\"DOI\",\"id\":\"10.1016/j.cell.2024.12.001\"}],\"citationType\":\"journal article\",\"firstPage\":\"653\",\"id\":\"39753131\",\"journal\":\"Cell\",\"lastPage\":\"670\",\"publicationDate\":\"2025\",\"title\":\"Evolutionary study and structural basis of proton sensing by Mus GPR4 and Xenopus GPR4.\",\"volume\":\"188\"},\"referenceNumber\":2,\"referencePositions\":[\"STRUCTURE BY ELECTRON MICROSCOPY\",\"DISULFIDE BONDS\",\"FUNCTION\",\"ACTIVITY REGULATION\",\"DOMAIN\",\"MUTAGENESIS OF GLU-51; VAL-119; PRO-122; LEU-123; HIS-159; HIS-165; SER-171; TYR-172; SER-214 AND HIS-276\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A6I8PUB9?format=txt&versions=25)

```json
{
  "evidence_id": "H1",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A6I8PUB9?format=txt&versions=25",
  "source_sha256": "57795ac8541e9349c417ffab8858e9955615bd1d0fd8bb5a206b1104334eba37",
  "retrieved_utc": "2026-11-02T04:25:39.964772+00:00",
  "source_locator": "lines 1-12",
  "excerpt": "ID   GPR4_XENTR              Reviewed;         353 AA.\nAC   A0A6I8PUB9;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   12-AUG-2020, sequence version 1.\nDT   28-JAN-2026, entry version 25.\nDE   RecName: Full=G-protein coupled receptor 4;\nDE            Short=XtGPR4 {ECO:0000303|PubMed:39753131};\nGN   Name=gpr4;\nOS   Xenopus tropicalis (Western clawed frog) (Silurana tropicalis).\nOC   Eukaryota; Metazoa; Chordata; Craniata; Vertebrata; Euteleostomi; Amphibia;\nOC   Batrachia; Anura; Pipoidea; Pipidae; Xenopodinae; Xenopus; Silurana.\nOX   NCBI_TaxID=8364;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 25,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A6I8PUB9?format=txt&versions=25)

```json
{
  "evidence_id": "H2",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A6I8PUB9?format=txt&versions=25",
  "source_sha256": "57795ac8541e9349c417ffab8858e9955615bd1d0fd8bb5a206b1104334eba37",
  "retrieved_utc": "2026-11-02T04:25:39.964772+00:00",
  "source_locator": "lines 27-38",
  "excerpt": "RN   [2]\nRP   STRUCTURE BY ELECTRON MICROSCOPY, DISULFIDE BONDS, FUNCTION, ACTIVITY\nRP   REGULATION, DOMAIN, AND MUTAGENESIS OF GLU-51; VAL-119; PRO-122; LEU-123;\nRP   HIS-159; HIS-165; SER-171; TYR-172; SER-214 AND HIS-276.\nRX   PubMed=39753131; DOI=10.1016/j.cell.2024.12.001;\nRA   Wen X., Shang P., Chen H., Guo L., Rong N., Jiang X., Li X., Liu J.,\nRA   Yang G., Zhang J., Zhu K., Meng Q., He X., Wang Z., Liu Z., Cheng H.,\nRA   Zheng Y., Zhang B., Pang J., Liu Z., Xiao P., Chen Y., Liu L., Luo F.,\nRA   Yu X., Yi F., Zhang P., Yang F., Deng C., Sun J.P.;\nRT   \"Evolutionary study and structural basis of proton sensing by Mus GPR4 and\nRT   Xenopus GPR4.\";\nRL   Cell 188:653-670(2025).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 25,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A6I8PUB9?format=txt&versions=25)

```json
{
  "evidence_id": "H3",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A6I8PUB9?format=txt&versions=25",
  "source_sha256": "57795ac8541e9349c417ffab8858e9955615bd1d0fd8bb5a206b1104334eba37",
  "retrieved_utc": "2026-11-02T04:25:39.964772+00:00",
  "source_locator": "lines 139-141",
  "excerpt": "FT   TOPO_DOM        1..8\nFT                   /note=\"Extracellular\"\nFT                   /evidence=\"ECO:0000269|PubMed:39753131\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 25,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A6I8PUB9?format=txt&versions=25)

```json
{
  "evidence_id": "H4",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A6I8PUB9?format=txt&versions=25",
  "source_sha256": "57795ac8541e9349c417ffab8858e9955615bd1d0fd8bb5a206b1104334eba37",
  "retrieved_utc": "2026-11-02T04:25:39.964772+00:00",
  "source_locator": "lines 142-144",
  "excerpt": "FT   TRANSMEM        9..45\nFT                   /note=\"Helical; Name=1\"\nFT                   /evidence=\"ECO:0000269|PubMed:39753131\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 25,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A6I8PUB9?format=txt&versions=25)

```json
{
  "evidence_id": "H5",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A6I8PUB9?format=txt&versions=25",
  "source_sha256": "57795ac8541e9349c417ffab8858e9955615bd1d0fd8bb5a206b1104334eba37",
  "retrieved_utc": "2026-11-02T04:25:39.964772+00:00",
  "source_locator": "lines 145-147",
  "excerpt": "FT   TOPO_DOM        46..49\nFT                   /note=\"Cytoplasmic\"\nFT                   /evidence=\"ECO:0000269|PubMed:39753131\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 25,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A6I8PUB9?format=txt&versions=25)

```json
{
  "evidence_id": "H6",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A6I8PUB9?format=txt&versions=25",
  "source_sha256": "57795ac8541e9349c417ffab8858e9955615bd1d0fd8bb5a206b1104334eba37",
  "retrieved_utc": "2026-11-02T04:25:39.964772+00:00",
  "source_locator": "lines 148-150",
  "excerpt": "FT   TRANSMEM        50..80\nFT                   /note=\"Helical; Name=2\"\nFT                   /evidence=\"ECO:0000269|PubMed:39753131\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 25,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A6I8PUB9?format=txt&versions=25)

```json
{
  "evidence_id": "H7",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A6I8PUB9?format=txt&versions=25",
  "source_sha256": "57795ac8541e9349c417ffab8858e9955615bd1d0fd8bb5a206b1104334eba37",
  "retrieved_utc": "2026-11-02T04:25:39.964772+00:00",
  "source_locator": "lines 151-153",
  "excerpt": "FT   TOPO_DOM        81..85\nFT                   /note=\"Extracellular\"\nFT                   /evidence=\"ECO:0000269|PubMed:39753131\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 25,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A6I8PUB9?format=txt&versions=25)

```json
{
  "evidence_id": "H8",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A6I8PUB9?format=txt&versions=25",
  "source_sha256": "57795ac8541e9349c417ffab8858e9955615bd1d0fd8bb5a206b1104334eba37",
  "retrieved_utc": "2026-11-02T04:25:39.964772+00:00",
  "source_locator": "lines 154-156",
  "excerpt": "FT   TRANSMEM        86..121\nFT                   /note=\"Helical; Name=3\"\nFT                   /evidence=\"ECO:0000269|PubMed:39753131\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 25,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A6I8PUB9?format=txt&versions=25)

```json
{
  "evidence_id": "H9",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A6I8PUB9?format=txt&versions=25",
  "source_sha256": "57795ac8541e9349c417ffab8858e9955615bd1d0fd8bb5a206b1104334eba37",
  "retrieved_utc": "2026-11-02T04:25:39.964772+00:00",
  "source_locator": "lines 157-159",
  "excerpt": "FT   TOPO_DOM        122..129\nFT                   /note=\"Cytoplasmic\"\nFT                   /evidence=\"ECO:0000269|PubMed:39753131\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 25,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H10

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A6I8PUB9?format=txt&versions=25)

```json
{
  "evidence_id": "H10",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A6I8PUB9?format=txt&versions=25",
  "source_sha256": "57795ac8541e9349c417ffab8858e9955615bd1d0fd8bb5a206b1104334eba37",
  "retrieved_utc": "2026-11-02T04:25:39.964772+00:00",
  "source_locator": "lines 160-162",
  "excerpt": "FT   TRANSMEM        130..156\nFT                   /note=\"Helical; Name=4\"\nFT                   /evidence=\"ECO:0000269|PubMed:39753131\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 25,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H11

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A6I8PUB9?format=txt&versions=25)

```json
{
  "evidence_id": "H11",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A6I8PUB9?format=txt&versions=25",
  "source_sha256": "57795ac8541e9349c417ffab8858e9955615bd1d0fd8bb5a206b1104334eba37",
  "retrieved_utc": "2026-11-02T04:25:39.964772+00:00",
  "source_locator": "lines 163-165",
  "excerpt": "FT   TOPO_DOM        157..172\nFT                   /note=\"Extracellular\"\nFT                   /evidence=\"ECO:0000269|PubMed:39753131\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 25,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H12

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A6I8PUB9?format=txt&versions=25)

```json
{
  "evidence_id": "H12",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A6I8PUB9?format=txt&versions=25",
  "source_sha256": "57795ac8541e9349c417ffab8858e9955615bd1d0fd8bb5a206b1104334eba37",
  "retrieved_utc": "2026-11-02T04:25:39.964772+00:00",
  "source_locator": "lines 166-168",
  "excerpt": "FT   TRANSMEM        173..211\nFT                   /note=\"Helical; Name=5\"\nFT                   /evidence=\"ECO:0000269|PubMed:39753131\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 25,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H13

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A6I8PUB9?format=txt&versions=25)

```json
{
  "evidence_id": "H13",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A6I8PUB9?format=txt&versions=25",
  "source_sha256": "57795ac8541e9349c417ffab8858e9955615bd1d0fd8bb5a206b1104334eba37",
  "retrieved_utc": "2026-11-02T04:25:39.964772+00:00",
  "source_locator": "lines 169-171",
  "excerpt": "FT   TOPO_DOM        212..215\nFT                   /note=\"Cytoplasmic\"\nFT                   /evidence=\"ECO:0000269|PubMed:39753131\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 25,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H14

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A6I8PUB9?format=txt&versions=25)

```json
{
  "evidence_id": "H14",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A6I8PUB9?format=txt&versions=25",
  "source_sha256": "57795ac8541e9349c417ffab8858e9955615bd1d0fd8bb5a206b1104334eba37",
  "retrieved_utc": "2026-11-02T04:25:39.964772+00:00",
  "source_locator": "lines 172-174",
  "excerpt": "FT   TRANSMEM        216..251\nFT                   /note=\"Helical; Name=6\"\nFT                   /evidence=\"ECO:0000269|PubMed:39753131\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 25,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H15

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A6I8PUB9?format=txt&versions=25)

```json
{
  "evidence_id": "H15",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A6I8PUB9?format=txt&versions=25",
  "source_sha256": "57795ac8541e9349c417ffab8858e9955615bd1d0fd8bb5a206b1104334eba37",
  "retrieved_utc": "2026-11-02T04:25:39.964772+00:00",
  "source_locator": "lines 175-177",
  "excerpt": "FT   TOPO_DOM        252..267\nFT                   /note=\"Extracellular\"\nFT                   /evidence=\"ECO:0000269|PubMed:39753131\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 25,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H16

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A6I8PUB9?format=txt&versions=25)

```json
{
  "evidence_id": "H16",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A6I8PUB9?format=txt&versions=25",
  "source_sha256": "57795ac8541e9349c417ffab8858e9955615bd1d0fd8bb5a206b1104334eba37",
  "retrieved_utc": "2026-11-02T04:25:39.964772+00:00",
  "source_locator": "lines 178-180",
  "excerpt": "FT   TRANSMEM        268..296\nFT                   /note=\"Helical; Name=7\"\nFT                   /evidence=\"ECO:0000269|PubMed:39753131\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 25,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H17

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A6I8PUB9?format=txt&versions=25)

```json
{
  "evidence_id": "H17",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A6I8PUB9?format=txt&versions=25",
  "source_sha256": "57795ac8541e9349c417ffab8858e9955615bd1d0fd8bb5a206b1104334eba37",
  "retrieved_utc": "2026-11-02T04:25:39.964772+00:00",
  "source_locator": "lines 181-183",
  "excerpt": "FT   TOPO_DOM        297..353\nFT                   /note=\"Cytoplasmic\"\nFT                   /evidence=\"ECO:0000269|PubMed:39753131\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 25,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json), zero-based source row 25. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
