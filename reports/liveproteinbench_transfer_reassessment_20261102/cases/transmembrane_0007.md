# transmembrane_0007: before and after transfer clarification

[All 1,328 cases](../README.md) · [Method](../METHOD.md) · [Summary](../SUMMARY.md) · [Exact reviewer user message](../inputs/transmembrane_0007.txt)

**Task:** `transmembrane`  
**Author key, unchanged:** **B** — 65..85; 137..157; 158..178; 187..207; 216..236; 250..270; 334..354; 367..387; 392..412; 423..443; 455..475; 489..509

| Round | Reviewer | Key support | Transfer / lookup | Output usability (canonical status) |
|---|---|---|---|---|
| before | GPT-6 Luna | supported | lookup-dependent | usable output (valid_review) |
| before | Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | usable output (valid_review) |
| after | GPT-6 Luna | supported | uncertain | usable output (valid_review) |
| after | Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | usable output (valid_review) |

**Usable output means format-valid review, not reasoning-supported or biologically correct.** A usable output can classify the question as reasoning-supported, lookup-dependent or uncertain. An output error is a problem with the saved model response; it does not count a defective benchmark question or wrong key. Each saved review is retained in full below. Labels from output errors are displayed as saved and excluded from label statistics. The author key and reviewer evidence were visible to reviewers; this is a review of answerability and key support, not a benchmark-solving score.

## Complete original question

```text
[Protein Sequence]
MASSDSNAKLASQRLHSCAGGEESSGQCLEKQGAGARLRGWLAQLLPRADLPGARQKTPFNLNRYVLLLLYSIVVFTTGAVFYGWTALSAMIFKNDGFAYLCPKDASGVYVPDLRATQGKLYICDEQDAAVQKLYTMTFAVACLMSAGAGTLLDWLGPLWTELLGQLLNLVGWLFLAFSTVDRPLYYPALVFIGLGADASMLPTLCIRHLFPGSTGLIITILGSAASASFGIPLVLNTIVENHGVSVRDVSIGYCFFGPVLGVLVALLFMPRRGFALDDAGTIFREPDSGEGEGEAGPYALENGAQGGESQNAQETRRRKLLDPIVSSSFWTQFFSIRYFLIVLYFVVVSWATSYYQQAARRMFSEDVVSVIEVLLPLSFIPCILLGKVADVVGIIRVLFVMNTSGLLTYVFSFFKTDATGYLSACCFMVYMSLLTSQVYVYVEGTFSPNHFGKLIGISNLTGGLLSLVSNPLYENITVNRDNGDPLCIQIAMTALLCVQYVWIFILGFLKSGNSPLLNMDVKAKDDADAEKRADNAPGAEERTSAPSGSSSELAAVTVTPPQDSA

[Multiple Choices]
A. 65..85; 137..157; 187..207; 216..236; 250..270; 334..354; 367..387; 392..412; 423..443; 455..475; 489..509
B. 65..85; 137..157; 158..178; 187..207; 216..236; 250..270; 334..354; 367..387; 392..412; 423..443; 455..475; 489..509
C. 179..199; 357..377
D. 65..85; 137..157; 158..178; 185..206; 216..236; 250..270; 334..354; 367..387; 392..412; 423..443; 455..475; 489..509
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

> The sequence-matched historical UniProt entry annotates the listed transmembrane intervals, including 158..178 and 187..207, so it supports choice B. These annotations use ECO:0000255, indicating computational evidence rather than direct experimental confirmation.

Citations as saved: [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6), [H7](#evidence-h7), [H8](#evidence-h8), [H9](#evidence-h9), [H10](#evidence-h10), [H11](#evidence-h11), [H12](#evidence-h12), [H13](#evidence-h13), [H14](#evidence-h14), [H15](#evidence-h15).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence has multiple hydrophobic stretches consistent with membrane-spanning helices, including a likely segment around 158..178, which helps distinguish choices that omit it. But sequence hydrophobicity alone does not reliably resolve the exact endpoints of closely overlapping candidate intervals.


**Missing item-specific fact**

> A protein-specific transmembrane annotation or other evidence establishing the precise helix boundaries, especially whether the interval is 187..207 or 185..206.


**Reason**

> Broad sequence features support a multi-pass membrane protein, but the choice between B and D depends on precise, item-specific boundaries that are not established by general biological reasoning from the supplied sequence.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "D"
]
```

> Choices B and D include nearly the same candidate helix, with boundaries shifted by only a few residues. Both intervals could plausibly represent the same membrane-spanning region based on sequence-level evidence, even though the cited annotation matches B.


### Important caveats

- Reviewer-only database evidence supports the expected answer but was not supplied to the evaluated model.
- The cited transmembrane annotations are computational, not direct experimental measurements.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has multiple hydrophobic stretches consistent with membrane-spanning helices, including a likely segment around 158..178, which helps distinguish choices that omit it. But sequence hydrophobicity alone does not reliably resolve the exact endpoints of closely overlapping candidate intervals.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "A protein-specific transmembrane annotation or other evidence establishing the precise helix boundaries, especially whether the interval is 187..207 or 185..206.",
    "reason": "Broad sequence features support a multi-pass membrane protein, but the choice between B and D depends on precise, item-specific boundaries that are not established by general biological reasoning from the supplied sequence."
  },
  "case_id": "transmembrane_0007",
  "expected_answer_check": {
    "evidence_ids": [
      "H4",
      "H5",
      "H6",
      "H7",
      "H8",
      "H9",
      "H10",
      "H11",
      "H12",
      "H13",
      "H14",
      "H15"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched historical UniProt entry annotates the listed transmembrane intervals, including 158..178 and 187..207, so it supports choice B. These annotations use ECO:0000255, indicating computational evidence rather than direct experimental confirmation."
  },
  "important_caveats": [
    "Reviewer-only database evidence supports the expected answer but was not supplied to the evaluated model.",
    "The cited transmembrane annotations are computational, not direct experimental measurements."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "D"
    ],
    "reason": "Choices B and D include nearly the same candidate helix, with boundaries shifted by only a few residues. Both intervals could plausibly represent the same membrane-spanning region based on sequence-level evidence, even though the cited annotation matches B."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0007",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched historical UniProt entry annotates the listed transmembrane intervals, including 158..178 and 187..207, so it supports choice B. These annotations use ECO:0000255, indicating computational evidence rather than direct experimental confirmation.",
    "evidence_ids": ["H4", "H5", "H6", "H7", "H8", "H9", "H10", "H11", "H12", "H13", "H14", "H15"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence has multiple hydrophobic stretches consistent with membrane-spanning helices, including a likely segment around 158..178, which helps distinguish choices that omit it. But sequence hydrophobicity alone does not reliably resolve the exact endpoints of closely overlapping candidate intervals.",
    "missing_item_specific_fact": "A protein-specific transmembrane annotation or other evidence establishing the precise helix boundaries, especially whether the interval is 187..207 or 185..206.",
    "reason": "Broad sequence features support a multi-pass membrane protein, but the choice between B and D depends on precise, item-specific boundaries that are not established by general biological reasoning from the supplied sequence."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "D"],
    "reason": "Choices B and D include nearly the same candidate helix, with boundaries shifted by only a few residues. Both intervals could plausibly represent the same membrane-spanning region based on sequence-level evidence, even though the cited annotation matches B."
  },
  "important_caveats": [
    "Reviewer-only database evidence supports the expected answer but was not supplied to the evaluated model.",
    "The cited transmembrane annotations are computational, not direct experimental measurements."
  ]
}
```

</details>

## Before: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProtKB/Swiss-Prot entry A0A125YQS6 (TgApiAT6-1, amino acid transporter 6-1 from Toxoplasma gondii) annotates exactly 12 transmembrane helical regions at 65..85, 137..157, 158..178, 187..207, 216..236, 250..270, 334..354, 367..387, 392..412, 423..443, 455..475, and 489..509, matching option B exactly. The sequence SHA256 matches the benchmark input. However, all TM annotations carry evidence code ECO:0000255 (inferred by similarity), indicating computational annotation rather than experimental determination.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [C9](#evidence-c9), [C10](#evidence-c10), [C11](#evidence-c11), [C12](#evidence-c12), [C13](#evidence-c13), [C14](#evidence-c14), [C15](#evidence-c15), [C16](#evidence-c16), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6), [H7](#evidence-h7), [H8](#evidence-h8), [H9](#evidence-h9), [H10](#evidence-h10), [H11](#evidence-h11), [H12](#evidence-h12), [H13](#evidence-h13), [H14](#evidence-h14), [H15](#evidence-h15).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> Option C (only 2 TM regions) can be eliminated by reasoning: a 566-residue amino acid transporter of the ApiAT family is expected to have approximately 12 TM helices, not 2. Option A (missing 158..178) might be partially addressable by noting a hydrophobic stretch in that region, but distinguishing it as a separate helix from the adjacent 137..157 helix is ambiguous. The critical distinction between B (187..207) and D (185..206) involves a 2-residue boundary shift that cannot be resolved by general hydrophobicity reasoning—it depends on the specific computational annotation boundary.


**Missing item-specific fact**

> The exact 1-2 residue boundary precision of the TM helix at positions 185-207 vs 187-209, and the definitive assignment of 158..178 as a separate helix from 137..157, are determined by the UniProt computational annotation (ECO:0000255) rather than by a general biological principle. Distinguishing B from D requires knowing the precise annotation boundary.


**Reason**

> While general biological knowledge (transporter topology, hydrophobic helix length ~20 residues, ApiAT family ~12 TM) can eliminate C and provide approximate regions, the precise boundaries distinguishing B from D (2-residue shift at one helix) and B from A (inclusion/exclusion of one helix) are annotation-specific facts. The ECO:0000255 evidence code confirms these are computational predictions, not experimentally determined boundaries, making the exact values database-specific.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "D"
]
```

> The distinction between B (187..207) and D (185..206) involves a 2-residue boundary shift. Without the specific annotation, both boundaries could be argued as reasonable hydrophobic helix termini by sequence inspection. Similarly, A vs B hinges on whether 158..178 constitutes a separate helix or is contiguous with 137..157, which is not unambiguously resolvable by general reasoning.


### Important caveats

- All TM annotations carry ECO:0000255 (inferred by similarity), meaning they are computational predictions, not experimental measurements. The 'correct' boundaries reflect a specific prediction algorithm's output.
- The sequence match is confirmed (SHA256 identical), and the entry is reviewed Swiss-Prot, but the TM boundaries themselves are not experimentally validated.
- Option C is an obvious distractor (2 TM regions for a 12-TM transporter) and does not meaningfully test knowledge.
- The reviewer-only evidence confirms the key but was not available to the evaluated model; the model must rely on sequence analysis or memorization of this specific annotation.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Option C (only 2 TM regions) can be eliminated by reasoning: a 566-residue amino acid transporter of the ApiAT family is expected to have approximately 12 TM helices, not 2. Option A (missing 158..178) might be partially addressable by noting a hydrophobic stretch in that region, but distinguishing it as a separate helix from the adjacent 137..157 helix is ambiguous. The critical distinction between B (187..207) and D (185..206) involves a 2-residue boundary shift that cannot be resolved by general hydrophobicity reasoning—it depends on the specific computational annotation boundary.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The exact 1-2 residue boundary precision of the TM helix at positions 185-207 vs 187-209, and the definitive assignment of 158..178 as a separate helix from 137..157, are determined by the UniProt computational annotation (ECO:0000255) rather than by a general biological principle. Distinguishing B from D requires knowing the precise annotation boundary.",
    "reason": "While general biological knowledge (transporter topology, hydrophobic helix length ~20 residues, ApiAT family ~12 TM) can eliminate C and provide approximate regions, the precise boundaries distinguishing B from D (2-residue shift at one helix) and B from A (inclusion/exclusion of one helix) are annotation-specific facts. The ECO:0000255 evidence code confirms these are computational predictions, not experimentally determined boundaries, making the exact values database-specific."
  },
  "case_id": "transmembrane_0007",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "C7",
      "C8",
      "C9",
      "C10",
      "C11",
      "C12",
      "C13",
      "C14",
      "C15",
      "C16",
      "H4",
      "H5",
      "H6",
      "H7",
      "H8",
      "H9",
      "H10",
      "H11",
      "H12",
      "H13",
      "H14",
      "H15"
    ],
    "judgment": "supported",
    "reason": "The UniProtKB/Swiss-Prot entry A0A125YQS6 (TgApiAT6-1, amino acid transporter 6-1 from Toxoplasma gondii) annotates exactly 12 transmembrane helical regions at 65..85, 137..157, 158..178, 187..207, 216..236, 250..270, 334..354, 367..387, 392..412, 423..443, 455..475, and 489..509, matching option B exactly. The sequence SHA256 matches the benchmark input. However, all TM annotations carry evidence code ECO:0000255 (inferred by similarity), indicating computational annotation rather than experimental determination."
  },
  "important_caveats": [
    "All TM annotations carry ECO:0000255 (inferred by similarity), meaning they are computational predictions, not experimental measurements. The 'correct' boundaries reflect a specific prediction algorithm's output.",
    "The sequence match is confirmed (SHA256 identical), and the entry is reviewed Swiss-Prot, but the TM boundaries themselves are not experimentally validated.",
    "Option C is an obvious distractor (2 TM regions for a 12-TM transporter) and does not meaningfully test knowledge.",
    "The reviewer-only evidence confirms the key but was not available to the evaluated model; the model must rely on sequence analysis or memorization of this specific annotation."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "D"
    ],
    "reason": "The distinction between B (187..207) and D (185..206) involves a 2-residue boundary shift. Without the specific annotation, both boundaries could be argued as reasonable hydrophobic helix termini by sequence inspection. Similarly, A vs B hinges on whether 158..178 constitutes a separate helix or is contiguous with 137..157, which is not unambiguously resolvable by general reasoning."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0007",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProtKB/Swiss-Prot entry A0A125YQS6 (TgApiAT6-1, amino acid transporter 6-1 from Toxoplasma gondii) annotates exactly 12 transmembrane helical regions at 65..85, 137..157, 158..178, 187..207, 216..236, 250..270, 334..354, 367..387, 392..412, 423..443, 455..475, and 489..509, matching option B exactly. The sequence SHA256 matches the benchmark input. However, all TM annotations carry evidence code ECO:0000255 (inferred by similarity), indicating computational annotation rather than experimental determination.",
    "evidence_ids": ["C5","C6","C7","C8","C9","C10","C11","C12","C13","C14","C15","C16","H4","H5","H6","H7","H8","H9","H10","H11","H12","H13","H14","H15"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "Option C (only 2 TM regions) can be eliminated by reasoning: a 566-residue amino acid transporter of the ApiAT family is expected to have approximately 12 TM helices, not 2. Option A (missing 158..178) might be partially addressable by noting a hydrophobic stretch in that region, but distinguishing it as a separate helix from the adjacent 137..157 helix is ambiguous. The critical distinction between B (187..207) and D (185..206) involves a 2-residue boundary shift that cannot be resolved by general hydrophobicity reasoning—it depends on the specific computational annotation boundary.",
    "missing_item_specific_fact": "The exact 1-2 residue boundary precision of the TM helix at positions 185-207 vs 187-209, and the definitive assignment of 158..178 as a separate helix from 137..157, are determined by the UniProt computational annotation (ECO:0000255) rather than by a general biological principle. Distinguishing B from D requires knowing the precise annotation boundary.",
    "reason": "While general biological knowledge (transporter topology, hydrophobic helix length ~20 residues, ApiAT family ~12 TM) can eliminate C and provide approximate regions, the precise boundaries distinguishing B from D (2-residue shift at one helix) and B from A (inclusion/exclusion of one helix) are annotation-specific facts. The ECO:0000255 evidence code confirms these are computational predictions, not experimentally determined boundaries, making the exact values database-specific."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "D"],
    "reason": "The distinction between B (187..207) and D (185..206) involves a 2-residue boundary shift. Without the specific annotation, both boundaries could be argued as reasonable hydrophobic helix termini by sequence inspection. Similarly, A vs B hinges on whether 158..178 constitutes a separate helix or is contiguous with 137..157, which is not unambiguously resolvable by general reasoning."
  },
  "important_caveats": [
    "All TM annotations carry ECO:0000255 (inferred by similarity), meaning they are computational predictions, not experimental measurements. The 'correct' boundaries reflect a specific prediction algorithm's output.",
    "The sequence match is confirmed (SHA256 identical), and the entry is reviewed Swiss-Prot, but the TM boundaries themselves are not experimentally validated.",
    "Option C is an obvious distractor (2 TM regions for a 12-TM transporter) and does not meaningfully test knowledge.",
    "The reviewer-only evidence confirms the key but was not available to the evaluated model; the model must rely on sequence analysis or memorization of this specific annotation."
  ]
}
```

</details>

## After: GPT-6 Luna

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence-matched UniProt annotation lists all the transmembrane segments in B, including 158..178. These are computationally evidenced helical annotations (ECO:0000255), not necessarily experimental measurements, but they support the key.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [C9](#evidence-c9), [C10](#evidence-c10), [C11](#evidence-c11), [C12](#evidence-c12), [C13](#evidence-c13), [C14](#evidence-c14), [C15](#evidence-c15), [C16](#evidence-c16).

### Reasoning versus lookup: uncertain

**Discriminating biological argument**

> The sequence contains numerous strongly hydrophobic stretches consistent with a multipass membrane protein; in particular, the region around 158..178 is hydrophobic, favoring B or D over A, which omits it. But B and D differ only by a small boundary shift in another hydrophobic span, which sequence hydropathy does not clearly resolve.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Transferable sequence-based reasoning supports the overall set of membrane-spanning regions, but does not clearly select B over D. Since both alternatives include a plausible span in essentially the same region, the available input does not establish a unique answer or a necessary exact-protein fact that would make one biologically correct.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "D"
]
```

> B and D contain the same set of predicted spans except that one interval is shifted by roughly two residues; both intervals plausibly cover the same membrane-spanning helix, and the question gives no boundary convention that distinguishes them.


### Important caveats

- The supporting source annotation is computational and reviewer-only; it was not part of the original model input.
- The database annotation supports B's exact coordinates, but that does not make the nearby alternative interval biologically implausible.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains numerous strongly hydrophobic stretches consistent with a multipass membrane protein; in particular, the region around 158..178 is hydrophobic, favoring B or D over A, which omits it. But B and D differ only by a small boundary shift in another hydrophobic span, which sequence hydropathy does not clearly resolve.",
    "judgment": "cannot_determine",
    "missing_item_specific_fact": "",
    "reason": "Transferable sequence-based reasoning supports the overall set of membrane-spanning regions, but does not clearly select B over D. Since both alternatives include a plausible span in essentially the same region, the available input does not establish a unique answer or a necessary exact-protein fact that would make one biologically correct."
  },
  "case_id": "transmembrane_0007",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "C7",
      "C8",
      "C9",
      "C10",
      "C11",
      "C12",
      "C13",
      "C14",
      "C15",
      "C16"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation lists all the transmembrane segments in B, including 158..178. These are computationally evidenced helical annotations (ECO:0000255), not necessarily experimental measurements, but they support the key."
  },
  "important_caveats": [
    "The supporting source annotation is computational and reviewer-only; it was not part of the original model input.",
    "The database annotation supports B's exact coordinates, but that does not make the nearby alternative interval biologically implausible."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "D"
    ],
    "reason": "B and D contain the same set of predicted spans except that one interval is shifted by roughly two residues; both intervals plausibly cover the same membrane-spanning helix, and the question gives no boundary convention that distinguishes them."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0007",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation lists all the transmembrane segments in B, including 158..178. These are computationally evidenced helical annotations (ECO:0000255), not necessarily experimental measurements, but they support the key.",
    "evidence_ids": ["C5", "C6", "C7", "C8", "C9", "C10", "C11", "C12", "C13", "C14", "C15", "C16"]
  },
  "answerability_check": {
    "judgment": "cannot_determine",
    "discriminating_biological_argument": "The sequence contains numerous strongly hydrophobic stretches consistent with a multipass membrane protein; in particular, the region around 158..178 is hydrophobic, favoring B or D over A, which omits it. But B and D differ only by a small boundary shift in another hydrophobic span, which sequence hydropathy does not clearly resolve.",
    "missing_item_specific_fact": "",
    "reason": "Transferable sequence-based reasoning supports the overall set of membrane-spanning regions, but does not clearly select B over D. Since both alternatives include a plausible span in essentially the same region, the available input does not establish a unique answer or a necessary exact-protein fact that would make one biologically correct."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "D"],
    "reason": "B and D contain the same set of predicted spans except that one interval is shifted by roughly two residues; both intervals plausibly cover the same membrane-spanning helix, and the question gives no boundary convention that distinguishes them."
  },
  "important_caveats": [
    "The supporting source annotation is computational and reviewer-only; it was not part of the original model input.",
    "The database annotation supports B's exact coordinates, but that does not make the nearby alternative interval biologically implausible."
  ]
}
```

</details>

## After: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt annotation for this protein (A0A125YQS6, Amino acid transporter 6-1 from Toxoplasma gondii) lists exactly 12 transmembrane helices at positions 65-85, 137-157, 158-178, 187-207, 216-236, 250-270, 334-354, 367-387, 392-412, 423-443, 455-475, 489-509, which matches choice B exactly. All annotations carry evidence code ECO:0000255 (inferred by similarity), indicating computational prediction rather than experimental determination, but the annotation is consistent with the expected answer.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [C9](#evidence-c9), [C10](#evidence-c10), [C11](#evidence-c11), [C12](#evidence-c12), [C13](#evidence-c13), [C14](#evidence-c14), [C15](#evidence-c15), [C16](#evidence-c16), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6), [H7](#evidence-h7), [H8](#evidence-h8), [H9](#evidence-h9), [H10](#evidence-h10), [H11](#evidence-h11), [H12](#evidence-h12), [H13](#evidence-h13), [H14](#evidence-h14), [H15](#evidence-h15).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The protein is an amino acid transporter (identified by the hydrophobic multi-pass topology and the ApiAT-family context). Members of the LeuT/AAAT superfamily, including apicomplexan amino acid transporters, possess a canonical 12-TM architecture organized as two inverted 5-TM bundles plus two additional helices, confirmed by crystal structures of LeuT, Mhp1, BetP, and vSGLT. This 12-TM architecture is strong family-level transferable knowledge. Option C (only 2 TMs) is immediately eliminated for any multi-pass membrane transporter. Option A lists only 11 TM segments, inconsistent with the expected 12-TM LeuT-fold topology; the missing 158-178 segment corresponds to a hydrophobic stretch in the sequence that should be recognized as a TM helix. This leaves B and D, which differ only in the 4th TM boundary (187..207 vs 185..206). While this 2-residue shift is within the typical uncertainty of TM boundary prediction, the hydrophobicity profile at those boundary positions (residues 185-186 vs 205-206) can be assessed from the sequence: if the residues at 185-186 are more polar or charged than those at 205-206, the helix core more naturally begins at 187. The 12-TM architecture argument is the primary discriminator eliminating A and C, and the boundary-residue hydrophobicity provides a secondary (if finer) basis for preferring B over D.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The 12-TM LeuT-fold architecture of amino acid transporters is well-established from multiple crystal structures and is transferable family knowledge. This eliminates options A (11 TMs) and C (2 TMs). Between B and D, the 2-residue boundary shift in the 4th TM is fine but can be approached by examining hydrophobicity of boundary residues in the provided sequence. The primary discrimination (12 vs 11 vs 2 TMs) is firmly supported by transferable structural biology knowledge.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Option C is clearly wrong (2 TMs for a multi-pass transporter). Option A is inconsistent with the 12-TM architecture. Between B and D, the 2-residue shift is fine but the 12-TM count and boundary hydrophobicity favor B. No other option is equally defensible.


### Important caveats

- All UniProt TM annotations carry ECO:0000255 (inferred by similarity), meaning they are computational predictions, not experimentally validated boundaries.
- The B vs D distinction (187..207 vs 185..206) is at the edge of typical TM predictor accuracy (±1-3 residues); a model relying solely on general hydrophobicity heuristics might find both plausible.
- The ApiAT family is relatively recently characterized (2019-2021 publications); a model's training data may or may not include detailed topology information for this specific family.
- The evidence codes confirm the annotations are by-similarity predictions from the LeuT/AAAT superfamily, not from direct experimental determination of this protein's structure.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The protein is an amino acid transporter (identified by the hydrophobic multi-pass topology and the ApiAT-family context). Members of the LeuT/AAAT superfamily, including apicomplexan amino acid transporters, possess a canonical 12-TM architecture organized as two inverted 5-TM bundles plus two additional helices, confirmed by crystal structures of LeuT, Mhp1, BetP, and vSGLT. This 12-TM architecture is strong family-level transferable knowledge. Option C (only 2 TMs) is immediately eliminated for any multi-pass membrane transporter. Option A lists only 11 TM segments, inconsistent with the expected 12-TM LeuT-fold topology; the missing 158-178 segment corresponds to a hydrophobic stretch in the sequence that should be recognized as a TM helix. This leaves B and D, which differ only in the 4th TM boundary (187..207 vs 185..206). While this 2-residue shift is within the typical uncertainty of TM boundary prediction, the hydrophobicity profile at those boundary positions (residues 185-186 vs 205-206) can be assessed from the sequence: if the residues at 185-186 are more polar or charged than those at 205-206, the helix core more naturally begins at 187. The 12-TM architecture argument is the primary discriminator eliminating A and C, and the boundary-residue hydrophobicity provides a secondary (if finer) basis for preferring B over D.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The 12-TM LeuT-fold architecture of amino acid transporters is well-established from multiple crystal structures and is transferable family knowledge. This eliminates options A (11 TMs) and C (2 TMs). Between B and D, the 2-residue boundary shift in the 4th TM is fine but can be approached by examining hydrophobicity of boundary residues in the provided sequence. The primary discrimination (12 vs 11 vs 2 TMs) is firmly supported by transferable structural biology knowledge."
  },
  "case_id": "transmembrane_0007",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "C7",
      "C8",
      "C9",
      "C10",
      "C11",
      "C12",
      "C13",
      "C14",
      "C15",
      "C16",
      "H4",
      "H5",
      "H6",
      "H7",
      "H8",
      "H9",
      "H10",
      "H11",
      "H12",
      "H13",
      "H14",
      "H15"
    ],
    "judgment": "supported",
    "reason": "The UniProt annotation for this protein (A0A125YQS6, Amino acid transporter 6-1 from Toxoplasma gondii) lists exactly 12 transmembrane helices at positions 65-85, 137-157, 158-178, 187-207, 216-236, 250-270, 334-354, 367-387, 392-412, 423-443, 455-475, 489-509, which matches choice B exactly. All annotations carry evidence code ECO:0000255 (inferred by similarity), indicating computational prediction rather than experimental determination, but the annotation is consistent with the expected answer."
  },
  "important_caveats": [
    "All UniProt TM annotations carry ECO:0000255 (inferred by similarity), meaning they are computational predictions, not experimentally validated boundaries.",
    "The B vs D distinction (187..207 vs 185..206) is at the edge of typical TM predictor accuracy (±1-3 residues); a model relying solely on general hydrophobicity heuristics might find both plausible.",
    "The ApiAT family is relatively recently characterized (2019-2021 publications); a model's training data may or may not include detailed topology information for this specific family.",
    "The evidence codes confirm the annotations are by-similarity predictions from the LeuT/AAAT superfamily, not from direct experimental determination of this protein's structure."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Option C is clearly wrong (2 TMs for a multi-pass transporter). Option A is inconsistent with the 12-TM architecture. Between B and D, the 2-residue shift is fine but the 12-TM count and boundary hydrophobicity favor B. No other option is equally defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0007",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt annotation for this protein (A0A125YQS6, Amino acid transporter 6-1 from Toxoplasma gondii) lists exactly 12 transmembrane helices at positions 65-85, 137-157, 158-178, 187-207, 216-236, 250-270, 334-354, 367-387, 392-412, 423-443, 455-475, 489-509, which matches choice B exactly. All annotations carry evidence code ECO:0000255 (inferred by similarity), indicating computational prediction rather than experimental determination, but the annotation is consistent with the expected answer.",
    "evidence_ids": ["C5", "C6", "C7", "C8", "C9", "C10", "C11", "C12", "C13", "C14", "C15", "C16", "H4", "H5", "H6", "H7", "H8", "H9", "H10", "H11", "H12", "H13", "H14", "H15"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The protein is an amino acid transporter (identified by the hydrophobic multi-pass topology and the ApiAT-family context). Members of the LeuT/AAAT superfamily, including apicomplexan amino acid transporters, possess a canonical 12-TM architecture organized as two inverted 5-TM bundles plus two additional helices, confirmed by crystal structures of LeuT, Mhp1, BetP, and vSGLT. This 12-TM architecture is strong family-level transferable knowledge. Option C (only 2 TMs) is immediately eliminated for any multi-pass membrane transporter. Option A lists only 11 TM segments, inconsistent with the expected 12-TM LeuT-fold topology; the missing 158-178 segment corresponds to a hydrophobic stretch in the sequence that should be recognized as a TM helix. This leaves B and D, which differ only in the 4th TM boundary (187..207 vs 185..206). While this 2-residue shift is within the typical uncertainty of TM boundary prediction, the hydrophobicity profile at those boundary positions (residues 185-186 vs 205-206) can be assessed from the sequence: if the residues at 185-186 are more polar or charged than those at 205-206, the helix core more naturally begins at 187. The 12-TM architecture argument is the primary discriminator eliminating A and C, and the boundary-residue hydrophobicity provides a secondary (if finer) basis for preferring B over D.",
    "missing_item_specific_fact": "",
    "reason": "The 12-TM LeuT-fold architecture of amino acid transporters is well-established from multiple crystal structures and is transferable family knowledge. This eliminates options A (11 TMs) and C (2 TMs). Between B and D, the 2-residue boundary shift in the 4th TM is fine but can be approached by examining hydrophobicity of boundary residues in the provided sequence. The primary discrimination (12 vs 11 vs 2 TMs) is firmly supported by transferable structural biology knowledge."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Option C is clearly wrong (2 TMs for a multi-pass transporter). Option A is inconsistent with the 12-TM architecture. Between B and D, the 2-residue shift is fine but the 12-TM count and boundary hydrophobicity favor B. No other option is equally defensible."
  },
  "important_caveats": [
    "All UniProt TM annotations carry ECO:0000255 (inferred by similarity), meaning they are computational predictions, not experimentally validated boundaries.",
    "The B vs D distinction (187..207 vs 185..206) is at the edge of typical TM predictor accuracy (±1-3 residues); a model relying solely on general hydrophobicity heuristics might find both plausible.",
    "The ApiAT family is relatively recently characterized (2019-2021 publications); a model's training data may or may not include detailed topology information for this specific family.",
    "The evidence codes confirm the annotations are by-similarity predictions from the LeuT/AAAT superfamily, not from direct experimental determination of this protein's structure."
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
  "requested_accession": "A0A125YQS6",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "benchmark_sequence_sha256": "191d7f468b8038b8c857041307d438fb970f63e9521e4a58ae0faafd7ad33072",
  "benchmark_sequence_length": 566,
  "current_status": "retrieved",
  "current_sequence_comparison": "matched",
  "current_entry_audit": {
    "entryVersion": 33,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2016-04-13",
    "sequenceVersion": 1
  },
  "current_uniprot_release": "2026_03",
  "current_record_sha256": "fe45df740c1133045fa704bf8db7ed1e22b8af4077b4407e44e9e271dc51f39f",
  "current_source_sequence_sha256": "191d7f468b8038b8c857041307d438fb970f63e9521e4a58ae0faafd7ad33072",
  "current_source_sequence_length": 566,
  "historical_status": "retrieved",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "selected_historical_entry_version": 32,
  "selected_historical_version": {
    "accession": "A0A125YQS6",
    "database": "Swiss-Prot",
    "entryVersion": 32,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_02/2026_02",
    "lastReleaseDate": "10-Jun-2026",
    "name": "AT6_TOXGM",
    "sequenceVersion": 1
  },
  "selected_historical_record_sha256": "d1f59d0960a176349ecfb71f807306e5811e320840d2d34cbe7fbcebeb965659",
  "selected_historical_source_sequence_sha256": "191d7f468b8038b8c857041307d438fb970f63e9521e4a58ae0faafd7ad33072",
  "selected_historical_source_sequence_length": 566,
  "latest_at_cutoff_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 32,
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A125YQS6.json)

```json
{
  "evidence_id": "C1",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A125YQS6.json",
  "source_sha256": "fe45df740c1133045fa704bf8db7ed1e22b8af4077b4407e44e9e271dc51f39f",
  "retrieved_utc": "2026-11-02T04:24:25.310365+00:00",
  "json_pointer": "/primaryAccession",
  "excerpt": "\"A0A125YQS6\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A125YQS6.json)

```json
{
  "evidence_id": "C2",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A125YQS6.json",
  "source_sha256": "fe45df740c1133045fa704bf8db7ed1e22b8af4077b4407e44e9e271dc51f39f",
  "retrieved_utc": "2026-11-02T04:24:25.310365+00:00",
  "json_pointer": "/entryAudit",
  "excerpt": "{\"entryVersion\":33,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2016-04-13\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A125YQS6.json)

```json
{
  "evidence_id": "C3",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A125YQS6.json",
  "source_sha256": "fe45df740c1133045fa704bf8db7ed1e22b8af4077b4407e44e9e271dc51f39f",
  "retrieved_utc": "2026-11-02T04:24:25.310365+00:00",
  "json_pointer": "/organism",
  "excerpt": "{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP000001529\",\"source\":\"Proteomes\"}],\"lineage\":[\"Eukaryota\",\"Sar\",\"Alveolata\",\"Apicomplexa\",\"Conoidasida\",\"Coccidia\",\"Eucoccidiorida\",\"Eimeriorina\",\"Sarcocystidae\",\"Toxoplasma\"],\"scientificName\":\"Toxoplasma gondii (strain ATCC 50611 / Me49)\",\"taxonId\":508771}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A125YQS6.json)

```json
{
  "evidence_id": "C4",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A125YQS6.json",
  "source_sha256": "fe45df740c1133045fa704bf8db7ed1e22b8af4077b4407e44e9e271dc51f39f",
  "retrieved_utc": "2026-11-02T04:24:25.310365+00:00",
  "json_pointer": "/proteinDescription",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Apicomplexan amino acid transporter 6-1\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"30742695\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000303\",\"id\":\"34432856\",\"source\":\"PubMed\"}],\"value\":\"TgApiAT6-1\"}]}],\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Amino acid transporter 6-1\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A125YQS6.json)

```json
{
  "evidence_id": "C5",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A125YQS6.json",
  "source_sha256": "fe45df740c1133045fa704bf8db7ed1e22b8af4077b4407e44e9e271dc51f39f",
  "retrieved_utc": "2026-11-02T04:24:25.310365+00:00",
  "json_pointer": "/features/1",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":85},\"start\":{\"modifier\":\"EXACT\",\"value\":65}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A125YQS6.json)

```json
{
  "evidence_id": "C6",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A125YQS6.json",
  "source_sha256": "fe45df740c1133045fa704bf8db7ed1e22b8af4077b4407e44e9e271dc51f39f",
  "retrieved_utc": "2026-11-02T04:24:25.310365+00:00",
  "json_pointer": "/features/2",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":157},\"start\":{\"modifier\":\"EXACT\",\"value\":137}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A125YQS6.json)

```json
{
  "evidence_id": "C7",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A125YQS6.json",
  "source_sha256": "fe45df740c1133045fa704bf8db7ed1e22b8af4077b4407e44e9e271dc51f39f",
  "retrieved_utc": "2026-11-02T04:24:25.310365+00:00",
  "json_pointer": "/features/3",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":178},\"start\":{\"modifier\":\"EXACT\",\"value\":158}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A125YQS6.json)

```json
{
  "evidence_id": "C8",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A125YQS6.json",
  "source_sha256": "fe45df740c1133045fa704bf8db7ed1e22b8af4077b4407e44e9e271dc51f39f",
  "retrieved_utc": "2026-11-02T04:24:25.310365+00:00",
  "json_pointer": "/features/4",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":207},\"start\":{\"modifier\":\"EXACT\",\"value\":187}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A125YQS6.json)

```json
{
  "evidence_id": "C9",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A125YQS6.json",
  "source_sha256": "fe45df740c1133045fa704bf8db7ed1e22b8af4077b4407e44e9e271dc51f39f",
  "retrieved_utc": "2026-11-02T04:24:25.310365+00:00",
  "json_pointer": "/features/5",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":236},\"start\":{\"modifier\":\"EXACT\",\"value\":216}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A125YQS6.json)

```json
{
  "evidence_id": "C10",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A125YQS6.json",
  "source_sha256": "fe45df740c1133045fa704bf8db7ed1e22b8af4077b4407e44e9e271dc51f39f",
  "retrieved_utc": "2026-11-02T04:24:25.310365+00:00",
  "json_pointer": "/features/6",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":270},\"start\":{\"modifier\":\"EXACT\",\"value\":250}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A125YQS6.json)

```json
{
  "evidence_id": "C11",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A125YQS6.json",
  "source_sha256": "fe45df740c1133045fa704bf8db7ed1e22b8af4077b4407e44e9e271dc51f39f",
  "retrieved_utc": "2026-11-02T04:24:25.310365+00:00",
  "json_pointer": "/features/7",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":354},\"start\":{\"modifier\":\"EXACT\",\"value\":334}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A125YQS6.json)

```json
{
  "evidence_id": "C12",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A125YQS6.json",
  "source_sha256": "fe45df740c1133045fa704bf8db7ed1e22b8af4077b4407e44e9e271dc51f39f",
  "retrieved_utc": "2026-11-02T04:24:25.310365+00:00",
  "json_pointer": "/features/8",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":387},\"start\":{\"modifier\":\"EXACT\",\"value\":367}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C13

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A125YQS6.json)

```json
{
  "evidence_id": "C13",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A125YQS6.json",
  "source_sha256": "fe45df740c1133045fa704bf8db7ed1e22b8af4077b4407e44e9e271dc51f39f",
  "retrieved_utc": "2026-11-02T04:24:25.310365+00:00",
  "json_pointer": "/features/9",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":412},\"start\":{\"modifier\":\"EXACT\",\"value\":392}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C14

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A125YQS6.json)

```json
{
  "evidence_id": "C14",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A125YQS6.json",
  "source_sha256": "fe45df740c1133045fa704bf8db7ed1e22b8af4077b4407e44e9e271dc51f39f",
  "retrieved_utc": "2026-11-02T04:24:25.310365+00:00",
  "json_pointer": "/features/10",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":443},\"start\":{\"modifier\":\"EXACT\",\"value\":423}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C15

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A125YQS6.json)

```json
{
  "evidence_id": "C15",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A125YQS6.json",
  "source_sha256": "fe45df740c1133045fa704bf8db7ed1e22b8af4077b4407e44e9e271dc51f39f",
  "retrieved_utc": "2026-11-02T04:24:25.310365+00:00",
  "json_pointer": "/features/11",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":475},\"start\":{\"modifier\":\"EXACT\",\"value\":455}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C16

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A125YQS6.json)

```json
{
  "evidence_id": "C16",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A125YQS6.json",
  "source_sha256": "fe45df740c1133045fa704bf8db7ed1e22b8af4077b4407e44e9e271dc51f39f",
  "retrieved_utc": "2026-11-02T04:24:25.310365+00:00",
  "json_pointer": "/features/12",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":509},\"start\":{\"modifier\":\"EXACT\",\"value\":489}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C17

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A125YQS6.json)

```json
{
  "evidence_id": "C17",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A125YQS6.json",
  "source_sha256": "fe45df740c1133045fa704bf8db7ed1e22b8af4077b4407e44e9e271dc51f39f",
  "retrieved_utc": "2026-11-02T04:24:25.310365+00:00",
  "json_pointer": "/references/1",
  "excerpt": "{\"citation\":{\"authors\":[\"Parker K.E.R.\",\"Fairweather S.J.\",\"Rajendran E.\",\"Blume M.\",\"McConville M.J.\",\"Broeer S.\",\"Kirk K.\",\"van Dooren G.G.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"30742695\"},{\"database\":\"DOI\",\"id\":\"10.1371/journal.ppat.1007577\"}],\"citationType\":\"journal article\",\"firstPage\":\"e1007577\",\"id\":\"30742695\",\"journal\":\"PLoS Pathog.\",\"lastPage\":\"e1007577\",\"publicationDate\":\"2019\",\"title\":\"The tyrosine transporter of Toxoplasma gondii is a member of the newly defined apicomplexan amino acid transporter (ApiAT) family.\",\"volume\":\"15\"},\"referenceNumber\":2,\"referencePositions\":[\"SUBCELLULAR LOCATION\",\"DEVELOPMENTAL STAGE\",\"DISRUPTION PHENOTYPE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C18

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A125YQS6.json)

```json
{
  "evidence_id": "C18",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A125YQS6.json",
  "source_sha256": "fe45df740c1133045fa704bf8db7ed1e22b8af4077b4407e44e9e271dc51f39f",
  "retrieved_utc": "2026-11-02T04:24:25.310365+00:00",
  "json_pointer": "/references/3",
  "excerpt": "{\"citation\":{\"authors\":[\"Fairweather S.J.\",\"Rajendran E.\",\"Blume M.\",\"Javed K.\",\"Steinhoefel B.\",\"McConville M.J.\",\"Kirk K.\",\"Broeer S.\",\"van Dooren G.G.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"34432856\"},{\"database\":\"DOI\",\"id\":\"10.1371/journal.ppat.1009835\"}],\"citationType\":\"journal article\",\"firstPage\":\"e1009835\",\"id\":\"34432856\",\"journal\":\"PLoS Pathog.\",\"lastPage\":\"e1009835\",\"publicationDate\":\"2021\",\"title\":\"Coordinated action of multiple transporters in the acquisition of essential cationic amino acids by the intracellular parasite Toxoplasma gondii.\",\"volume\":\"17\"},\"referenceNumber\":4,\"referencePositions\":[\"FUNCTION\",\"TRANSPORTER ACTIVITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"SUBCELLULAR LOCATION\",\"DISRUPTION PHENOTYPE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A125YQS6?format=txt&versions=32)

```json
{
  "evidence_id": "H1",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A125YQS6?format=txt&versions=32",
  "source_sha256": "d1f59d0960a176349ecfb71f807306e5811e320840d2d34cbe7fbcebeb965659",
  "retrieved_utc": "2026-11-02T04:24:28.654244+00:00",
  "source_locator": "lines 1-14",
  "excerpt": "ID   AT6_TOXGM               Reviewed;         566 AA.\nAC   A0A125YQS6;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   13-APR-2016, sequence version 1.\nDT   28-JAN-2026, entry version 32.\nDE   RecName: Full=Amino acid transporter 6-1 {ECO:0000305};\nDE   AltName: Full=Apicomplexan amino acid transporter 6-1 {ECO:0000305};\nDE            Short=TgApiAT6-1 {ECO:0000303|PubMed:30742695, ECO:0000303|PubMed:34432856};\nGN   Name=ApiAT6-1 {ECO:0000305};\nGN   ORFNames=TGME49_240810 {ECO:0000312|EMBL:EPT30670.1};\nOS   Toxoplasma gondii (strain ATCC 50611 / Me49).\nOC   Eukaryota; Sar; Alveolata; Apicomplexa; Conoidasida; Coccidia;\nOC   Eucoccidiorida; Eimeriorina; Sarcocystidae; Toxoplasma.\nOX   NCBI_TaxID=508771 {ECO:0000312|Proteomes:UP000001529};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 32,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A125YQS6?format=txt&versions=32)

```json
{
  "evidence_id": "H2",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A125YQS6?format=txt&versions=32",
  "source_sha256": "d1f59d0960a176349ecfb71f807306e5811e320840d2d34cbe7fbcebeb965659",
  "retrieved_utc": "2026-11-02T04:24:28.654244+00:00",
  "source_locator": "lines 21-28",
  "excerpt": "RN   [2]\nRP   SUBCELLULAR LOCATION, DEVELOPMENTAL STAGE, AND DISRUPTION PHENOTYPE.\nRX   PubMed=30742695; DOI=10.1371/journal.ppat.1007577;\nRA   Parker K.E.R., Fairweather S.J., Rajendran E., Blume M., McConville M.J.,\nRA   Broeer S., Kirk K., van Dooren G.G.;\nRT   \"The tyrosine transporter of Toxoplasma gondii is a member of the newly\nRT   defined apicomplexan amino acid transporter (ApiAT) family.\";\nRL   PLoS Pathog. 15:e1007577-e1007577(2019).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 32,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A125YQS6?format=txt&versions=32)

```json
{
  "evidence_id": "H3",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A125YQS6?format=txt&versions=32",
  "source_sha256": "d1f59d0960a176349ecfb71f807306e5811e320840d2d34cbe7fbcebeb965659",
  "retrieved_utc": "2026-11-02T04:24:28.654244+00:00",
  "source_locator": "lines 37-46",
  "excerpt": "RN   [4]\nRP   FUNCTION, TRANSPORTER ACTIVITY, BIOPHYSICOCHEMICAL PROPERTIES, SUBCELLULAR\nRP   LOCATION, AND DISRUPTION PHENOTYPE.\nRX   PubMed=34432856; DOI=10.1371/journal.ppat.1009835;\nRA   Fairweather S.J., Rajendran E., Blume M., Javed K., Steinhoefel B.,\nRA   McConville M.J., Kirk K., Broeer S., van Dooren G.G.;\nRT   \"Coordinated action of multiple transporters in the acquisition of\nRT   essential cationic amino acids by the intracellular parasite Toxoplasma\nRT   gondii.\";\nRL   PLoS Pathog. 17:e1009835-e1009835(2021).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 32,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A125YQS6?format=txt&versions=32)

```json
{
  "evidence_id": "H4",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A125YQS6?format=txt&versions=32",
  "source_sha256": "d1f59d0960a176349ecfb71f807306e5811e320840d2d34cbe7fbcebeb965659",
  "retrieved_utc": "2026-11-02T04:24:28.654244+00:00",
  "source_locator": "lines 114-116",
  "excerpt": "FT   TRANSMEM        65..85\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 32,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A125YQS6?format=txt&versions=32)

```json
{
  "evidence_id": "H5",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A125YQS6?format=txt&versions=32",
  "source_sha256": "d1f59d0960a176349ecfb71f807306e5811e320840d2d34cbe7fbcebeb965659",
  "retrieved_utc": "2026-11-02T04:24:28.654244+00:00",
  "source_locator": "lines 117-119",
  "excerpt": "FT   TRANSMEM        137..157\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 32,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A125YQS6?format=txt&versions=32)

```json
{
  "evidence_id": "H6",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A125YQS6?format=txt&versions=32",
  "source_sha256": "d1f59d0960a176349ecfb71f807306e5811e320840d2d34cbe7fbcebeb965659",
  "retrieved_utc": "2026-11-02T04:24:28.654244+00:00",
  "source_locator": "lines 120-122",
  "excerpt": "FT   TRANSMEM        158..178\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 32,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A125YQS6?format=txt&versions=32)

```json
{
  "evidence_id": "H7",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A125YQS6?format=txt&versions=32",
  "source_sha256": "d1f59d0960a176349ecfb71f807306e5811e320840d2d34cbe7fbcebeb965659",
  "retrieved_utc": "2026-11-02T04:24:28.654244+00:00",
  "source_locator": "lines 123-125",
  "excerpt": "FT   TRANSMEM        187..207\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 32,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A125YQS6?format=txt&versions=32)

```json
{
  "evidence_id": "H8",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A125YQS6?format=txt&versions=32",
  "source_sha256": "d1f59d0960a176349ecfb71f807306e5811e320840d2d34cbe7fbcebeb965659",
  "retrieved_utc": "2026-11-02T04:24:28.654244+00:00",
  "source_locator": "lines 126-128",
  "excerpt": "FT   TRANSMEM        216..236\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 32,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A125YQS6?format=txt&versions=32)

```json
{
  "evidence_id": "H9",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A125YQS6?format=txt&versions=32",
  "source_sha256": "d1f59d0960a176349ecfb71f807306e5811e320840d2d34cbe7fbcebeb965659",
  "retrieved_utc": "2026-11-02T04:24:28.654244+00:00",
  "source_locator": "lines 129-131",
  "excerpt": "FT   TRANSMEM        250..270\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 32,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H10

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A125YQS6?format=txt&versions=32)

```json
{
  "evidence_id": "H10",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A125YQS6?format=txt&versions=32",
  "source_sha256": "d1f59d0960a176349ecfb71f807306e5811e320840d2d34cbe7fbcebeb965659",
  "retrieved_utc": "2026-11-02T04:24:28.654244+00:00",
  "source_locator": "lines 132-134",
  "excerpt": "FT   TRANSMEM        334..354\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 32,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H11

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A125YQS6?format=txt&versions=32)

```json
{
  "evidence_id": "H11",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A125YQS6?format=txt&versions=32",
  "source_sha256": "d1f59d0960a176349ecfb71f807306e5811e320840d2d34cbe7fbcebeb965659",
  "retrieved_utc": "2026-11-02T04:24:28.654244+00:00",
  "source_locator": "lines 135-137",
  "excerpt": "FT   TRANSMEM        367..387\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 32,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H12

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A125YQS6?format=txt&versions=32)

```json
{
  "evidence_id": "H12",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A125YQS6?format=txt&versions=32",
  "source_sha256": "d1f59d0960a176349ecfb71f807306e5811e320840d2d34cbe7fbcebeb965659",
  "retrieved_utc": "2026-11-02T04:24:28.654244+00:00",
  "source_locator": "lines 138-140",
  "excerpt": "FT   TRANSMEM        392..412\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 32,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H13

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A125YQS6?format=txt&versions=32)

```json
{
  "evidence_id": "H13",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A125YQS6?format=txt&versions=32",
  "source_sha256": "d1f59d0960a176349ecfb71f807306e5811e320840d2d34cbe7fbcebeb965659",
  "retrieved_utc": "2026-11-02T04:24:28.654244+00:00",
  "source_locator": "lines 141-143",
  "excerpt": "FT   TRANSMEM        423..443\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 32,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H14

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A125YQS6?format=txt&versions=32)

```json
{
  "evidence_id": "H14",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A125YQS6?format=txt&versions=32",
  "source_sha256": "d1f59d0960a176349ecfb71f807306e5811e320840d2d34cbe7fbcebeb965659",
  "retrieved_utc": "2026-11-02T04:24:28.654244+00:00",
  "source_locator": "lines 144-146",
  "excerpt": "FT   TRANSMEM        455..475\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 32,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H15

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A125YQS6?format=txt&versions=32)

```json
{
  "evidence_id": "H15",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A125YQS6?format=txt&versions=32",
  "source_sha256": "d1f59d0960a176349ecfb71f807306e5811e320840d2d34cbe7fbcebeb965659",
  "retrieved_utc": "2026-11-02T04:24:28.654244+00:00",
  "source_locator": "lines 147-149",
  "excerpt": "FT   TRANSMEM        489..509\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 32,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json), zero-based source row 7. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
