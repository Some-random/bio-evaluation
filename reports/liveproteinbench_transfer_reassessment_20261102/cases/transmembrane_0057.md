# transmembrane_0057: before and after transfer clarification

[All 1,328 cases](../README.md) · [Method](../METHOD.md) · [Summary](../SUMMARY.md) · [Exact reviewer user message](../inputs/transmembrane_0057.txt)

**Task:** `transmembrane`  
**Author key, unchanged:** **B** — 30..50; 62..82; 108..128; 144..164; 186..206; 327..347; 357..377

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
MTQLPYLLDRRGGALAAPATAWGDMMLNRALFSVALLSSVGSAWVVLSYACIKELRSYRHQLILGLAISDLLMSLNFMFSAGWNVAGGDLALEESRTACSVNGFLTQVFVVQTDWWILVIAIATYIILGNFKTQSQFIQTHVWIPWVGPWVLSIIIAAICHGVLGYGYIGGWCWLTSDLMRLLINFIPRWLIVIAIALIYIRLYMIVRKARKWDIEGVSPDPGDDMADTSVILMSVGKKDRERQGSGVLVSRDVSVSFGRKGSTAPTFVTMVTTSGAGDSREAISSCSAREEGSRARTVNVNSSRSLSLGMRQPLNAAQLKRIAKKMMVYPVAYAIIWACPTAIRIYQGTTGSRAPLWITIVDKSCIVIQGLVDAVVYGLNERAWQGWRDHIRRIIYKNEGGRIIG

[Multiple Choices]
A. 139..159; 176..196; 247..267; 272..292; 297..317
B. 30..50; 62..82; 108..128; 144..164; 186..206; 327..347; 357..377
C. 30..50; 62..82; 108..128; 144..164; 186..206; 327..347
D. 30..50; 62..82; 108..128; 144..164; 186..206; 328..343; 357..377
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

> The sequence matches the referenced UniProt entry, whose annotation lists all seven regions in choice B as transmembrane helices. These are computational annotations (ECO:0000255), not evidence of direct experimental determination of the boundaries.

Citations as saved: [C6](#evidence-c6), [C8](#evidence-c8), [C10](#evidence-c10), [C12](#evidence-c12), [C14](#evidence-c14), [C16](#evidence-c16), [C18](#evidence-c18), [H4](#evidence-h4), [H6](#evidence-h6), [H8](#evidence-h8), [H10](#evidence-h10), [H12](#evidence-h12), [H14](#evidence-h14), [H16](#evidence-h16).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence contains hydrophobic stretches consistent with membrane-spanning helices, including near the C-terminus. That supports the general prediction of membrane regions but does not establish their exact residue boundaries.


**Missing item-specific fact**

> The protein-specific transmembrane-region assignments and precise boundaries, particularly the choice between the full 327..347 interval and the shortened 328..343 interval.


**Reason**

> Selecting the exact listed coordinates depends on protein-specific annotation or a prediction beyond what general membrane-protein knowledge establishes. The reviewer-only UniProt evidence supports the key but was not supplied to the evaluated model.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The sequence supports hydrophobic membrane-spanning regions, but it does not independently validate exact endpoints. Among the choices, B is supported by the matched annotation; the other options omit or truncate candidate regions.


### Important caveats

- The supplied evidence identifies the regions as computationally annotated helical transmembrane segments, not experimentally established boundaries.
- The author’s source snapshot is unknown, though the matching sequence occurs in both the historical and current UniProt records.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains hydrophobic stretches consistent with membrane-spanning helices, including near the C-terminus. That supports the general prediction of membrane regions but does not establish their exact residue boundaries.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific transmembrane-region assignments and precise boundaries, particularly the choice between the full 327..347 interval and the shortened 328..343 interval.",
    "reason": "Selecting the exact listed coordinates depends on protein-specific annotation or a prediction beyond what general membrane-protein knowledge establishes. The reviewer-only UniProt evidence supports the key but was not supplied to the evaluated model."
  },
  "case_id": "transmembrane_0057",
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
    "reason": "The sequence matches the referenced UniProt entry, whose annotation lists all seven regions in choice B as transmembrane helices. These are computational annotations (ECO:0000255), not evidence of direct experimental determination of the boundaries."
  },
  "important_caveats": [
    "The supplied evidence identifies the regions as computationally annotated helical transmembrane segments, not experimentally established boundaries.",
    "The author’s source snapshot is unknown, though the matching sequence occurs in both the historical and current UniProt records."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence supports hydrophobic membrane-spanning regions, but it does not independently validate exact endpoints. Among the choices, B is supported by the matched annotation; the other options omit or truncate candidate regions."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0057",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches the referenced UniProt entry, whose annotation lists all seven regions in choice B as transmembrane helices. These are computational annotations (ECO:0000255), not evidence of direct experimental determination of the boundaries.",
    "evidence_ids": ["C6", "C8", "C10", "C12", "C14", "C16", "C18", "H4", "H6", "H8", "H10", "H12", "H14", "H16"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence contains hydrophobic stretches consistent with membrane-spanning helices, including near the C-terminus. That supports the general prediction of membrane regions but does not establish their exact residue boundaries.",
    "missing_item_specific_fact": "The protein-specific transmembrane-region assignments and precise boundaries, particularly the choice between the full 327..347 interval and the shortened 328..343 interval.",
    "reason": "Selecting the exact listed coordinates depends on protein-specific annotation or a prediction beyond what general membrane-protein knowledge establishes. The reviewer-only UniProt evidence supports the key but was not supplied to the evaluated model."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence supports hydrophobic membrane-spanning regions, but it does not independently validate exact endpoints. Among the choices, B is supported by the matched annotation; the other options omit or truncate candidate regions."
  },
  "important_caveats": [
    "The supplied evidence identifies the regions as computationally annotated helical transmembrane segments, not experimentally established boundaries.",
    "The author’s source snapshot is unknown, though the matching sequence occurs in both the historical and current UniProt records."
  ]
}
```

</details>

## Before: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt annotation for G1X9E2 (Ascaroside receptor GPR2, a GPCR from Arthrobotrys oligospora) lists exactly 7 transmembrane helices at positions 30..50, 62..82, 108..128, 144..164, 186..206, 327..347, and 357..377, matching option B precisely. However, all TM annotations carry evidence code ECO:0000255 ('By similarity'), indicating computational prediction rather than experimental determination. The 7-TM topology is consistent with the protein's classification as a GPCR (supported by PubMed:38649409 functional study). The sequence match is confirmed (SHA256 identical, 406 AA).

Citations as saved: [C6](#evidence-c6), [C8](#evidence-c8), [C10](#evidence-c10), [C12](#evidence-c12), [C14](#evidence-c14), [C16](#evidence-c16), [C18](#evidence-c18), [C4](#evidence-c4), [H4](#evidence-h4), [H6](#evidence-h6), [H8](#evidence-h8), [H10](#evidence-h10), [H12](#evidence-h12), [H14](#evidence-h14), [H16](#evidence-h16), [H2](#evidence-h2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The protein is a GPCR (7-TM receptor). Option C lists only 6 TM regions, violating GPCR topology. Option A's positions (139..159, 176..196, 247..267, 272..292, 297..317) do not correspond to hydrophobic stretches in the sequence and are inconsistent with GPCR architecture. The critical B-vs-D distinction concerns TM6: option D gives 328..343 (16 residues ≈ 24 Å helix length), which is too short to span the ~30 Å hydrophobic core of a lipid bilayer in an α-helical conformation (requires ≥20 residues). Option B's 327..347 (21 residues ≈ 31.5 Å) is consistent with canonical TM helix length. Additionally, the hydrophobicity profile around positions 344–347 remains sufficiently hydrophobic to include those residues in the TM segment.


**Missing item-specific fact**

> The exact boundary residue (327 vs 328, 347 vs 343) is determined by a specific computational predictor (ECO:0000255). A model without access to the exact prediction tool output must rely on hydrophobicity judgment and helix-length reasoning, which strongly but not absolutely favors 21 over 16 residues.


**Reason**

> General GPCR knowledge (7 TM helices) eliminates C. Hydrophobicity pattern analysis eliminates A. The B-vs-D distinction is addressable via helix-length biophysics (16 residues is marginal/too short for membrane spanning), though the exact boundary is somewhat predictor-dependent. Overall, reasoning provides meaningful grounds to select B.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> While the exact TM boundary (327 vs 328, 347 vs 343) is somewhat arbitrary from a prediction standpoint, the 16-residue option (D) is biophysically implausible for a membrane-spanning helix, making B the clearly more defensible choice. No other option is equally defensible.


### Important caveats

- All UniProt TM annotations use evidence code ECO:0000255 (By similarity/computational prediction), not experimental structural data. Exact boundaries reflect a specific prediction algorithm's output.
- The protein was identified as GPR2 (Ascaroside receptor) via a 2024 Nature Microbiology paper (PubMed:38649409) demonstrating GPCR function, supporting the 7-TM topology assignment.
- The distinction between B and D (TM6: 327..347 vs 328..343) is a 5-residue boundary difference; while the 16-residue helix in D is biophysically marginal, a very aggressive TM predictor might output shorter boundaries. The reasoning argument (helix length) is strong but not mathematically airtight.
- Option A's positions appear to be a distractor with no correspondence to actual hydrophobic TM stretches in the sequence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The protein is a GPCR (7-TM receptor). Option C lists only 6 TM regions, violating GPCR topology. Option A's positions (139..159, 176..196, 247..267, 272..292, 297..317) do not correspond to hydrophobic stretches in the sequence and are inconsistent with GPCR architecture. The critical B-vs-D distinction concerns TM6: option D gives 328..343 (16 residues ≈ 24 Å helix length), which is too short to span the ~30 Å hydrophobic core of a lipid bilayer in an α-helical conformation (requires ≥20 residues). Option B's 327..347 (21 residues ≈ 31.5 Å) is consistent with canonical TM helix length. Additionally, the hydrophobicity profile around positions 344–347 remains sufficiently hydrophobic to include those residues in the TM segment.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The exact boundary residue (327 vs 328, 347 vs 343) is determined by a specific computational predictor (ECO:0000255). A model without access to the exact prediction tool output must rely on hydrophobicity judgment and helix-length reasoning, which strongly but not absolutely favors 21 over 16 residues.",
    "reason": "General GPCR knowledge (7 TM helices) eliminates C. Hydrophobicity pattern analysis eliminates A. The B-vs-D distinction is addressable via helix-length biophysics (16 residues is marginal/too short for membrane spanning), though the exact boundary is somewhat predictor-dependent. Overall, reasoning provides meaningful grounds to select B."
  },
  "case_id": "transmembrane_0057",
  "expected_answer_check": {
    "evidence_ids": [
      "C6",
      "C8",
      "C10",
      "C12",
      "C14",
      "C16",
      "C18",
      "C4",
      "H4",
      "H6",
      "H8",
      "H10",
      "H12",
      "H14",
      "H16",
      "H2"
    ],
    "judgment": "supported",
    "reason": "The UniProt annotation for G1X9E2 (Ascaroside receptor GPR2, a GPCR from Arthrobotrys oligospora) lists exactly 7 transmembrane helices at positions 30..50, 62..82, 108..128, 144..164, 186..206, 327..347, and 357..377, matching option B precisely. However, all TM annotations carry evidence code ECO:0000255 ('By similarity'), indicating computational prediction rather than experimental determination. The 7-TM topology is consistent with the protein's classification as a GPCR (supported by PubMed:38649409 functional study). The sequence match is confirmed (SHA256 identical, 406 AA)."
  },
  "important_caveats": [
    "All UniProt TM annotations use evidence code ECO:0000255 (By similarity/computational prediction), not experimental structural data. Exact boundaries reflect a specific prediction algorithm's output.",
    "The protein was identified as GPR2 (Ascaroside receptor) via a 2024 Nature Microbiology paper (PubMed:38649409) demonstrating GPCR function, supporting the 7-TM topology assignment.",
    "The distinction between B and D (TM6: 327..347 vs 328..343) is a 5-residue boundary difference; while the 16-residue helix in D is biophysically marginal, a very aggressive TM predictor might output shorter boundaries. The reasoning argument (helix length) is strong but not mathematically airtight.",
    "Option A's positions appear to be a distractor with no correspondence to actual hydrophobic TM stretches in the sequence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While the exact TM boundary (327 vs 328, 347 vs 343) is somewhat arbitrary from a prediction standpoint, the 16-residue option (D) is biophysically implausible for a membrane-spanning helix, making B the clearly more defensible choice. No other option is equally defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0057",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt annotation for G1X9E2 (Ascaroside receptor GPR2, a GPCR from Arthrobotrys oligospora) lists exactly 7 transmembrane helices at positions 30..50, 62..82, 108..128, 144..164, 186..206, 327..347, and 357..377, matching option B precisely. However, all TM annotations carry evidence code ECO:0000255 ('By similarity'), indicating computational prediction rather than experimental determination. The 7-TM topology is consistent with the protein's classification as a GPCR (supported by PubMed:38649409 functional study). The sequence match is confirmed (SHA256 identical, 406 AA).",
    "evidence_ids": ["C6", "C8", "C10", "C12", "C14", "C16", "C18", "C4", "H4", "H6", "H8", "H10", "H12", "H14", "H16", "H2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The protein is a GPCR (7-TM receptor). Option C lists only 6 TM regions, violating GPCR topology. Option A's positions (139..159, 176..196, 247..267, 272..292, 297..317) do not correspond to hydrophobic stretches in the sequence and are inconsistent with GPCR architecture. The critical B-vs-D distinction concerns TM6: option D gives 328..343 (16 residues ≈ 24 Å helix length), which is too short to span the ~30 Å hydrophobic core of a lipid bilayer in an α-helical conformation (requires ≥20 residues). Option B's 327..347 (21 residues ≈ 31.5 Å) is consistent with canonical TM helix length. Additionally, the hydrophobicity profile around positions 344–347 remains sufficiently hydrophobic to include those residues in the TM segment.",
    "missing_item_specific_fact": "The exact boundary residue (327 vs 328, 347 vs 343) is determined by a specific computational predictor (ECO:0000255). A model without access to the exact prediction tool output must rely on hydrophobicity judgment and helix-length reasoning, which strongly but not absolutely favors 21 over 16 residues.",
    "reason": "General GPCR knowledge (7 TM helices) eliminates C. Hydrophobicity pattern analysis eliminates A. The B-vs-D distinction is addressable via helix-length biophysics (16 residues is marginal/too short for membrane spanning), though the exact boundary is somewhat predictor-dependent. Overall, reasoning provides meaningful grounds to select B."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While the exact TM boundary (327 vs 328, 347 vs 343) is somewhat arbitrary from a prediction standpoint, the 16-residue option (D) is biophysically implausible for a membrane-spanning helix, making B the clearly more defensible choice. No other option is equally defensible."
  },
  "important_caveats": [
    "All UniProt TM annotations use evidence code ECO:0000255 (By similarity/computational prediction), not experimental structural data. Exact boundaries reflect a specific prediction algorithm's output.",
    "The protein was identified as GPR2 (Ascaroside receptor) via a 2024 Nature Microbiology paper (PubMed:38649409) demonstrating GPCR function, supporting the 7-TM topology assignment.",
    "The distinction between B and D (TM6: 327..347 vs 328..343) is a 5-residue boundary difference; while the 16-residue helix in D is biophysically marginal, a very aggressive TM predictor might output shorter boundaries. The reasoning argument (helix length) is strong but not mathematically airtight.",
    "Option A's positions appear to be a distractor with no correspondence to actual hydrophobic TM stretches in the sequence."
  ]
}
```

</details>

## After: GPT-6 Luna

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The exact sequence matches UniProt records annotating all seven regions listed in B as transmembrane helices. The annotations are computationally supported (ECO:0000255), not direct experimental evidence of membrane crossing.

Citations as saved: [H4](#evidence-h4), [H6](#evidence-h6), [H8](#evidence-h8), [H10](#evidence-h10), [H12](#evidence-h12), [H14](#evidence-h14), [H16](#evidence-h16).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has several strong hydrophobic stretches, including two near the C-terminus around the candidate regions 327..347 and 357..377. These are consistent with membrane-spanning helices; the long intervening region is comparatively nonhydrophobic. Thus B includes both plausible C-terminal spans, whereas C omits one and D gives a notably shortened interval for the first. Hydrophobic-segment recognition and the common multi-pass architecture of receptors provide transferable grounds for choosing B.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The sequence itself supplies a meaningful hydrophobicity-based distinction among the choices; exact target-specific database recall is not necessary. Boundaries are predictions rather than experimentally established here.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The alternatives differ in whether they include the second C-terminal hydrophobic span and in the coverage of the preceding span; the sequence supports the two full intervals in B.


### Important caveats

- The cited UniProt transmembrane features are computationally supported annotations, not experimental measurements.
- The current and historical records match the supplied sequence, but the author's exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has several strong hydrophobic stretches, including two near the C-terminus around the candidate regions 327..347 and 357..377. These are consistent with membrane-spanning helices; the long intervening region is comparatively nonhydrophobic. Thus B includes both plausible C-terminal spans, whereas C omits one and D gives a notably shortened interval for the first. Hydrophobic-segment recognition and the common multi-pass architecture of receptors provide transferable grounds for choosing B.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The sequence itself supplies a meaningful hydrophobicity-based distinction among the choices; exact target-specific database recall is not necessary. Boundaries are predictions rather than experimentally established here."
  },
  "case_id": "transmembrane_0057",
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
    "reason": "The exact sequence matches UniProt records annotating all seven regions listed in B as transmembrane helices. The annotations are computationally supported (ECO:0000255), not direct experimental evidence of membrane crossing."
  },
  "important_caveats": [
    "The cited UniProt transmembrane features are computationally supported annotations, not experimental measurements.",
    "The current and historical records match the supplied sequence, but the author's exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The alternatives differ in whether they include the second C-terminal hydrophobic span and in the coverage of the preceding span; the sequence supports the two full intervals in B."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0057",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches UniProt records annotating all seven regions listed in B as transmembrane helices. The annotations are computationally supported (ECO:0000255), not direct experimental evidence of membrane crossing.",
    "evidence_ids": ["H4", "H6", "H8", "H10", "H12", "H14", "H16"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has several strong hydrophobic stretches, including two near the C-terminus around the candidate regions 327..347 and 357..377. These are consistent with membrane-spanning helices; the long intervening region is comparatively nonhydrophobic. Thus B includes both plausible C-terminal spans, whereas C omits one and D gives a notably shortened interval for the first. Hydrophobic-segment recognition and the common multi-pass architecture of receptors provide transferable grounds for choosing B.",
    "missing_item_specific_fact": "",
    "reason": "The sequence itself supplies a meaningful hydrophobicity-based distinction among the choices; exact target-specific database recall is not necessary. Boundaries are predictions rather than experimentally established here."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The alternatives differ in whether they include the second C-terminal hydrophobic span and in the coverage of the preceding span; the sequence supports the two full intervals in B."
  },
  "important_caveats": [
    "The cited UniProt transmembrane features are computationally supported annotations, not experimental measurements.",
    "The current and historical records match the supplied sequence, but the author's exact source snapshot is unknown."
  ]
}
```

</details>

## After: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt annotation for G1X9E2 (Ascaroside receptor GPR2) lists exactly 7 transmembrane helices at positions 30..50, 62..82, 108..128, 144..164, 186..206, 327..347, and 357..377, matching option B exactly. The evidence codes are ECO:0000255 (by similarity), indicating computational/predicted annotations based on homology rather than experimental determination. However, the annotation is internally consistent with the sequence topology (alternating extracellular/cytoplasmic loops) and the 7TM GPCR architecture. The sequence match is confirmed (SHA256 identical, 406 AA).

Citations as saved: [C6](#evidence-c6), [C8](#evidence-c8), [C10](#evidence-c10), [C12](#evidence-c12), [C14](#evidence-c14), [C16](#evidence-c16), [C18](#evidence-c18), [H4](#evidence-h4), [H6](#evidence-h6), [H8](#evidence-h8), [H10](#evidence-h10), [H12](#evidence-h12), [H14](#evidence-h14), [H16](#evidence-h16).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> This protein exhibits the hallmark architecture of a 7-transmembrane GPCR: multiple hydrophobic stretches of ~20 residues separated by hydrophilic loops, including a characteristically long third intracellular loop (~120 residues). The 7TM GPCR topology is among the most well-established facts in structural biology, learned from hundreds of characterized GPCRs. This eliminates option A (only 5 TM segments) and option C (only 6 TM segments). Distinguishing B from D requires knowledge that an alpha-helix must be at least ~19-21 residues to span the ~30 Å hydrophobic core of a lipid bilayer (at 1.5 Å/residue rise). Option D's sixth TM segment (328..343) is only 16 residues—physically too short to traverse the membrane—while option B's 327..347 (21 residues) is the standard length. The hydrophobic stretch around positions 327-347 in the sequence (containing residues like Y, P, V, A, Y, A, I, I, W, A, C, P, T, A, I, R, I, Y, Q, G, T) is clearly identifiable as a ~20+ residue hydrophobic segment, supporting the 21-residue assignment over the 16-residue one.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can apply the universally recognized 7TM GPCR architecture to eliminate options A and C, and apply the biophysical minimum helix length (~20 residues) for membrane spanning to eliminate option D's implausibly short 16-residue segment. These are well-established, transferable principles from hundreds of characterized GPCRs and basic membrane biophysics, not facts specific to this exact protein.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The options are well-separated: A has 5 TMs (wrong count for GPCR), C has 6 TMs (wrong count), D has a 16-residue helix (physically too short), leaving B as the only option with 7 TMs of appropriate length. The biophysical constraint on minimum helix length clearly distinguishes B from D.


### Important caveats

- The UniProt transmembrane annotations carry evidence code ECO:0000255 (by similarity), meaning they are computational predictions based on homology to known GPCRs, not experimental measurements.
- The protein identity (Ascaroside receptor GPR2, a GPCR) was determined by reviewer-only UniProt lookup and was not provided to the evaluated model; however, the 7TM architecture is inferable from the sequence pattern itself.
- The long intracellular loop (positions 207-326, ~120 residues) is characteristic of GPCRs and helps confirm the 7TM topology from sequence alone.
- Option A's positions (139..159, etc.) appear to be deliberate ~5-residue shifts of the true TM positions, serving as a positional-shift distractor.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "This protein exhibits the hallmark architecture of a 7-transmembrane GPCR: multiple hydrophobic stretches of ~20 residues separated by hydrophilic loops, including a characteristically long third intracellular loop (~120 residues). The 7TM GPCR topology is among the most well-established facts in structural biology, learned from hundreds of characterized GPCRs. This eliminates option A (only 5 TM segments) and option C (only 6 TM segments). Distinguishing B from D requires knowledge that an alpha-helix must be at least ~19-21 residues to span the ~30 Å hydrophobic core of a lipid bilayer (at 1.5 Å/residue rise). Option D's sixth TM segment (328..343) is only 16 residues—physically too short to traverse the membrane—while option B's 327..347 (21 residues) is the standard length. The hydrophobic stretch around positions 327-347 in the sequence (containing residues like Y, P, V, A, Y, A, I, I, W, A, C, P, T, A, I, R, I, Y, Q, G, T) is clearly identifiable as a ~20+ residue hydrophobic segment, supporting the 21-residue assignment over the 16-residue one.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can apply the universally recognized 7TM GPCR architecture to eliminate options A and C, and apply the biophysical minimum helix length (~20 residues) for membrane spanning to eliminate option D's implausibly short 16-residue segment. These are well-established, transferable principles from hundreds of characterized GPCRs and basic membrane biophysics, not facts specific to this exact protein."
  },
  "case_id": "transmembrane_0057",
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
    "reason": "The UniProt annotation for G1X9E2 (Ascaroside receptor GPR2) lists exactly 7 transmembrane helices at positions 30..50, 62..82, 108..128, 144..164, 186..206, 327..347, and 357..377, matching option B exactly. The evidence codes are ECO:0000255 (by similarity), indicating computational/predicted annotations based on homology rather than experimental determination. However, the annotation is internally consistent with the sequence topology (alternating extracellular/cytoplasmic loops) and the 7TM GPCR architecture. The sequence match is confirmed (SHA256 identical, 406 AA)."
  },
  "important_caveats": [
    "The UniProt transmembrane annotations carry evidence code ECO:0000255 (by similarity), meaning they are computational predictions based on homology to known GPCRs, not experimental measurements.",
    "The protein identity (Ascaroside receptor GPR2, a GPCR) was determined by reviewer-only UniProt lookup and was not provided to the evaluated model; however, the 7TM architecture is inferable from the sequence pattern itself.",
    "The long intracellular loop (positions 207-326, ~120 residues) is characteristic of GPCRs and helps confirm the 7TM topology from sequence alone.",
    "Option A's positions (139..159, etc.) appear to be deliberate ~5-residue shifts of the true TM positions, serving as a positional-shift distractor."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The options are well-separated: A has 5 TMs (wrong count for GPCR), C has 6 TMs (wrong count), D has a 16-residue helix (physically too short), leaving B as the only option with 7 TMs of appropriate length. The biophysical constraint on minimum helix length clearly distinguishes B from D."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0057",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt annotation for G1X9E2 (Ascaroside receptor GPR2) lists exactly 7 transmembrane helices at positions 30..50, 62..82, 108..128, 144..164, 186..206, 327..347, and 357..377, matching option B exactly. The evidence codes are ECO:0000255 (by similarity), indicating computational/predicted annotations based on homology rather than experimental determination. However, the annotation is internally consistent with the sequence topology (alternating extracellular/cytoplasmic loops) and the 7TM GPCR architecture. The sequence match is confirmed (SHA256 identical, 406 AA).",
    "evidence_ids": ["C6", "C8", "C10", "C12", "C14", "C16", "C18", "H4", "H6", "H8", "H10", "H12", "H14", "H16"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "This protein exhibits the hallmark architecture of a 7-transmembrane GPCR: multiple hydrophobic stretches of ~20 residues separated by hydrophilic loops, including a characteristically long third intracellular loop (~120 residues). The 7TM GPCR topology is among the most well-established facts in structural biology, learned from hundreds of characterized GPCRs. This eliminates option A (only 5 TM segments) and option C (only 6 TM segments). Distinguishing B from D requires knowledge that an alpha-helix must be at least ~19-21 residues to span the ~30 Å hydrophobic core of a lipid bilayer (at 1.5 Å/residue rise). Option D's sixth TM segment (328..343) is only 16 residues—physically too short to traverse the membrane—while option B's 327..347 (21 residues) is the standard length. The hydrophobic stretch around positions 327-347 in the sequence (containing residues like Y, P, V, A, Y, A, I, I, W, A, C, P, T, A, I, R, I, Y, Q, G, T) is clearly identifiable as a ~20+ residue hydrophobic segment, supporting the 21-residue assignment over the 16-residue one.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can apply the universally recognized 7TM GPCR architecture to eliminate options A and C, and apply the biophysical minimum helix length (~20 residues) for membrane spanning to eliminate option D's implausibly short 16-residue segment. These are well-established, transferable principles from hundreds of characterized GPCRs and basic membrane biophysics, not facts specific to this exact protein."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The options are well-separated: A has 5 TMs (wrong count for GPCR), C has 6 TMs (wrong count), D has a 16-residue helix (physically too short), leaving B as the only option with 7 TMs of appropriate length. The biophysical constraint on minimum helix length clearly distinguishes B from D."
  },
  "important_caveats": [
    "The UniProt transmembrane annotations carry evidence code ECO:0000255 (by similarity), meaning they are computational predictions based on homology to known GPCRs, not experimental measurements.",
    "The protein identity (Ascaroside receptor GPR2, a GPCR) was determined by reviewer-only UniProt lookup and was not provided to the evaluated model; however, the 7TM architecture is inferable from the sequence pattern itself.",
    "The long intracellular loop (positions 207-326, ~120 residues) is characteristic of GPCRs and helps confirm the 7TM topology from sequence alone.",
    "Option A's positions (139..159, etc.) appear to be deliberate ~5-residue shifts of the true TM positions, serving as a positional-shift distractor."
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
  "requested_accession": "G1X9E2",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "benchmark_sequence_sha256": "4e764ad5fe8865d73836f34a410857326f248f960936c909cff720a56696f0f3",
  "benchmark_sequence_length": 406,
  "current_status": "retrieved",
  "current_sequence_comparison": "matched",
  "current_entry_audit": {
    "entryVersion": 47,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2011-11-16",
    "sequenceVersion": 1
  },
  "current_uniprot_release": "2026_03",
  "current_record_sha256": "d672d0bdd6e6d87681068eb4f338f9f4a6f7cf51e1400211480752ecd223995f",
  "current_source_sequence_sha256": "4e764ad5fe8865d73836f34a410857326f248f960936c909cff720a56696f0f3",
  "current_source_sequence_length": 406,
  "historical_status": "retrieved",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "selected_historical_entry_version": 45,
  "selected_historical_version": {
    "accession": "G1X9E2",
    "database": "Swiss-Prot",
    "entryVersion": 45,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "GPR2_ARTOA",
    "sequenceVersion": 1
  },
  "selected_historical_record_sha256": "e35d509b45ea64e3eac1fedae5691280c0fa8c7205a8651df542bc73ee054a3f",
  "selected_historical_source_sequence_sha256": "4e764ad5fe8865d73836f34a410857326f248f960936c909cff720a56696f0f3",
  "selected_historical_source_sequence_length": 406,
  "latest_at_cutoff_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 45,
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G1X9E2.json)

```json
{
  "evidence_id": "C1",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/G1X9E2.json",
  "source_sha256": "d672d0bdd6e6d87681068eb4f338f9f4a6f7cf51e1400211480752ecd223995f",
  "retrieved_utc": "2026-11-02T04:28:30.739464+00:00",
  "json_pointer": "/primaryAccession",
  "excerpt": "\"G1X9E2\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G1X9E2.json)

```json
{
  "evidence_id": "C2",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/G1X9E2.json",
  "source_sha256": "d672d0bdd6e6d87681068eb4f338f9f4a6f7cf51e1400211480752ecd223995f",
  "retrieved_utc": "2026-11-02T04:28:30.739464+00:00",
  "json_pointer": "/entryAudit",
  "excerpt": "{\"entryVersion\":47,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2011-11-16\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G1X9E2.json)

```json
{
  "evidence_id": "C3",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/G1X9E2.json",
  "source_sha256": "d672d0bdd6e6d87681068eb4f338f9f4a6f7cf51e1400211480752ecd223995f",
  "retrieved_utc": "2026-11-02T04:28:30.739464+00:00",
  "json_pointer": "/organism",
  "excerpt": "{\"commonName\":\"Nematode-trapping fungus\",\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP000008784\",\"source\":\"Proteomes\"}],\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Orbiliomycetes\",\"Orbiliales\",\"Orbiliaceae\",\"Orbilia\",\"Orbilia oligospora\"],\"scientificName\":\"Arthrobotrys oligospora (strain ATCC 24927 / CBS 115.81 / DSM 1491)\",\"synonyms\":[\"Didymozoophaga oligospora\"],\"taxonId\":756982}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G1X9E2.json)

```json
{
  "evidence_id": "C4",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/G1X9E2.json",
  "source_sha256": "d672d0bdd6e6d87681068eb4f338f9f4a6f7cf51e1400211480752ecd223995f",
  "retrieved_utc": "2026-11-02T04:28:30.739464+00:00",
  "json_pointer": "/proteinDescription",
  "excerpt": "{\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Ascaroside receptor GPR2\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G1X9E2.json)

```json
{
  "evidence_id": "C5",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/G1X9E2.json",
  "source_sha256": "d672d0bdd6e6d87681068eb4f338f9f4a6f7cf51e1400211480752ecd223995f",
  "retrieved_utc": "2026-11-02T04:28:30.739464+00:00",
  "json_pointer": "/features/1",
  "excerpt": "{\"description\":\"Extracellular\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":29},\"start\":{\"modifier\":\"EXACT\",\"value\":1}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G1X9E2.json)

```json
{
  "evidence_id": "C6",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/G1X9E2.json",
  "source_sha256": "d672d0bdd6e6d87681068eb4f338f9f4a6f7cf51e1400211480752ecd223995f",
  "retrieved_utc": "2026-11-02T04:28:30.739464+00:00",
  "json_pointer": "/features/2",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":50},\"start\":{\"modifier\":\"EXACT\",\"value\":30}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G1X9E2.json)

```json
{
  "evidence_id": "C7",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/G1X9E2.json",
  "source_sha256": "d672d0bdd6e6d87681068eb4f338f9f4a6f7cf51e1400211480752ecd223995f",
  "retrieved_utc": "2026-11-02T04:28:30.739464+00:00",
  "json_pointer": "/features/3",
  "excerpt": "{\"description\":\"Cytoplasmic\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":61},\"start\":{\"modifier\":\"EXACT\",\"value\":51}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G1X9E2.json)

```json
{
  "evidence_id": "C8",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/G1X9E2.json",
  "source_sha256": "d672d0bdd6e6d87681068eb4f338f9f4a6f7cf51e1400211480752ecd223995f",
  "retrieved_utc": "2026-11-02T04:28:30.739464+00:00",
  "json_pointer": "/features/4",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":82},\"start\":{\"modifier\":\"EXACT\",\"value\":62}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G1X9E2.json)

```json
{
  "evidence_id": "C9",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/G1X9E2.json",
  "source_sha256": "d672d0bdd6e6d87681068eb4f338f9f4a6f7cf51e1400211480752ecd223995f",
  "retrieved_utc": "2026-11-02T04:28:30.739464+00:00",
  "json_pointer": "/features/5",
  "excerpt": "{\"description\":\"Extracellular\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":107},\"start\":{\"modifier\":\"EXACT\",\"value\":83}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G1X9E2.json)

```json
{
  "evidence_id": "C10",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/G1X9E2.json",
  "source_sha256": "d672d0bdd6e6d87681068eb4f338f9f4a6f7cf51e1400211480752ecd223995f",
  "retrieved_utc": "2026-11-02T04:28:30.739464+00:00",
  "json_pointer": "/features/6",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":128},\"start\":{\"modifier\":\"EXACT\",\"value\":108}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G1X9E2.json)

```json
{
  "evidence_id": "C11",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/G1X9E2.json",
  "source_sha256": "d672d0bdd6e6d87681068eb4f338f9f4a6f7cf51e1400211480752ecd223995f",
  "retrieved_utc": "2026-11-02T04:28:30.739464+00:00",
  "json_pointer": "/features/7",
  "excerpt": "{\"description\":\"Cytoplasmic\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":143},\"start\":{\"modifier\":\"EXACT\",\"value\":129}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G1X9E2.json)

```json
{
  "evidence_id": "C12",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/G1X9E2.json",
  "source_sha256": "d672d0bdd6e6d87681068eb4f338f9f4a6f7cf51e1400211480752ecd223995f",
  "retrieved_utc": "2026-11-02T04:28:30.739464+00:00",
  "json_pointer": "/features/8",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":164},\"start\":{\"modifier\":\"EXACT\",\"value\":144}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C13

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G1X9E2.json)

```json
{
  "evidence_id": "C13",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/G1X9E2.json",
  "source_sha256": "d672d0bdd6e6d87681068eb4f338f9f4a6f7cf51e1400211480752ecd223995f",
  "retrieved_utc": "2026-11-02T04:28:30.739464+00:00",
  "json_pointer": "/features/9",
  "excerpt": "{\"description\":\"Extracellular\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":185},\"start\":{\"modifier\":\"EXACT\",\"value\":165}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C14

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G1X9E2.json)

```json
{
  "evidence_id": "C14",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/G1X9E2.json",
  "source_sha256": "d672d0bdd6e6d87681068eb4f338f9f4a6f7cf51e1400211480752ecd223995f",
  "retrieved_utc": "2026-11-02T04:28:30.739464+00:00",
  "json_pointer": "/features/10",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":206},\"start\":{\"modifier\":\"EXACT\",\"value\":186}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C15

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G1X9E2.json)

```json
{
  "evidence_id": "C15",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/G1X9E2.json",
  "source_sha256": "d672d0bdd6e6d87681068eb4f338f9f4a6f7cf51e1400211480752ecd223995f",
  "retrieved_utc": "2026-11-02T04:28:30.739464+00:00",
  "json_pointer": "/features/11",
  "excerpt": "{\"description\":\"Cytoplasmic\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":326},\"start\":{\"modifier\":\"EXACT\",\"value\":207}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C16

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G1X9E2.json)

```json
{
  "evidence_id": "C16",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/G1X9E2.json",
  "source_sha256": "d672d0bdd6e6d87681068eb4f338f9f4a6f7cf51e1400211480752ecd223995f",
  "retrieved_utc": "2026-11-02T04:28:30.739464+00:00",
  "json_pointer": "/features/12",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":347},\"start\":{\"modifier\":\"EXACT\",\"value\":327}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C17

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G1X9E2.json)

```json
{
  "evidence_id": "C17",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/G1X9E2.json",
  "source_sha256": "d672d0bdd6e6d87681068eb4f338f9f4a6f7cf51e1400211480752ecd223995f",
  "retrieved_utc": "2026-11-02T04:28:30.739464+00:00",
  "json_pointer": "/features/13",
  "excerpt": "{\"description\":\"Extracellular\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":356},\"start\":{\"modifier\":\"EXACT\",\"value\":348}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C18

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G1X9E2.json)

```json
{
  "evidence_id": "C18",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/G1X9E2.json",
  "source_sha256": "d672d0bdd6e6d87681068eb4f338f9f4a6f7cf51e1400211480752ecd223995f",
  "retrieved_utc": "2026-11-02T04:28:30.739464+00:00",
  "json_pointer": "/features/14",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":377},\"start\":{\"modifier\":\"EXACT\",\"value\":357}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C19

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G1X9E2.json)

```json
{
  "evidence_id": "C19",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/G1X9E2.json",
  "source_sha256": "d672d0bdd6e6d87681068eb4f338f9f4a6f7cf51e1400211480752ecd223995f",
  "retrieved_utc": "2026-11-02T04:28:30.739464+00:00",
  "json_pointer": "/features/15",
  "excerpt": "{\"description\":\"Cytoplasmic\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":406},\"start\":{\"modifier\":\"EXACT\",\"value\":378}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G1X9E2?format=txt&versions=45)

```json
{
  "evidence_id": "H1",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/G1X9E2?format=txt&versions=45",
  "source_sha256": "e35d509b45ea64e3eac1fedae5691280c0fa8c7205a8651df542bc73ee054a3f",
  "retrieved_utc": "2026-11-02T04:28:32.723564+00:00",
  "source_locator": "lines 1-13",
  "excerpt": "ID   GPR2_ARTOA              Reviewed;         406 AA.\nAC   G1X9E2;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   16-NOV-2011, sequence version 1.\nDT   28-JAN-2026, entry version 45.\nDE   RecName: Full=Ascaroside receptor GPR2 {ECO:0000305};\nGN   Name=GPR2 {ECO:0000303|PubMed:38649409};\nGN   ORFNames=AOL_s00076g249 {ECO:0000312|EMBL:EGX50174.1};\nOS   Arthrobotrys oligospora (strain ATCC 24927 / CBS 115.81 / DSM 1491)\nOS   (Nematode-trapping fungus) (Didymozoophaga oligospora).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Orbiliomycetes;\nOC   Orbiliales; Orbiliaceae; Orbilia; Orbilia oligospora.\nOX   NCBI_TaxID=756982 {ECO:0000312|Proteomes:UP000008784};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 45,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G1X9E2?format=txt&versions=45)

```json
{
  "evidence_id": "H2",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/G1X9E2?format=txt&versions=45",
  "source_sha256": "e35d509b45ea64e3eac1fedae5691280c0fa8c7205a8651df542bc73ee054a3f",
  "retrieved_utc": "2026-11-02T04:28:32.723564+00:00",
  "source_locator": "lines 25-34",
  "excerpt": "RN   [2] {ECO:0000305}\nRP   FUNCTION, INTERACTION WITH GPA2 AND GPR3, SUBCELLULAR LOCATION, INDUCTION,\nRP   AND DISRUPTION PHENOTYPE.\nRC   STRAIN=TWF154 {ECO:0000303|PubMed:38649409};\nRX   PubMed=38649409; DOI=10.1038/s41564-024-01679-w;\nRA   Kuo C.Y., Tay R.J., Lin H.C., Juan S.C., Vidal-Diez de Ulzurrun G.,\nRA   Chang Y.C., Hoki J., Schroeder F.C., Hsueh Y.P.;\nRT   \"The nematode-trapping fungus Arthrobotrys oligospora detects prey\nRT   pheromones via G protein-coupled receptors.\";\nRL   Nat. Microbiol. 9:1738-1751(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 45,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G1X9E2?format=txt&versions=45)

```json
{
  "evidence_id": "H3",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/G1X9E2?format=txt&versions=45",
  "source_sha256": "e35d509b45ea64e3eac1fedae5691280c0fa8c7205a8651df542bc73ee054a3f",
  "retrieved_utc": "2026-11-02T04:28:32.723564+00:00",
  "source_locator": "lines 94-96",
  "excerpt": "FT   TOPO_DOM        1..29\nFT                   /note=\"Extracellular\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 45,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G1X9E2?format=txt&versions=45)

```json
{
  "evidence_id": "H4",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/G1X9E2?format=txt&versions=45",
  "source_sha256": "e35d509b45ea64e3eac1fedae5691280c0fa8c7205a8651df542bc73ee054a3f",
  "retrieved_utc": "2026-11-02T04:28:32.723564+00:00",
  "source_locator": "lines 97-99",
  "excerpt": "FT   TRANSMEM        30..50\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 45,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G1X9E2?format=txt&versions=45)

```json
{
  "evidence_id": "H5",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/G1X9E2?format=txt&versions=45",
  "source_sha256": "e35d509b45ea64e3eac1fedae5691280c0fa8c7205a8651df542bc73ee054a3f",
  "retrieved_utc": "2026-11-02T04:28:32.723564+00:00",
  "source_locator": "lines 100-102",
  "excerpt": "FT   TOPO_DOM        51..61\nFT                   /note=\"Cytoplasmic\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 45,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G1X9E2?format=txt&versions=45)

```json
{
  "evidence_id": "H6",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/G1X9E2?format=txt&versions=45",
  "source_sha256": "e35d509b45ea64e3eac1fedae5691280c0fa8c7205a8651df542bc73ee054a3f",
  "retrieved_utc": "2026-11-02T04:28:32.723564+00:00",
  "source_locator": "lines 103-105",
  "excerpt": "FT   TRANSMEM        62..82\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 45,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G1X9E2?format=txt&versions=45)

```json
{
  "evidence_id": "H7",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/G1X9E2?format=txt&versions=45",
  "source_sha256": "e35d509b45ea64e3eac1fedae5691280c0fa8c7205a8651df542bc73ee054a3f",
  "retrieved_utc": "2026-11-02T04:28:32.723564+00:00",
  "source_locator": "lines 106-108",
  "excerpt": "FT   TOPO_DOM        83..107\nFT                   /note=\"Extracellular\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 45,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G1X9E2?format=txt&versions=45)

```json
{
  "evidence_id": "H8",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/G1X9E2?format=txt&versions=45",
  "source_sha256": "e35d509b45ea64e3eac1fedae5691280c0fa8c7205a8651df542bc73ee054a3f",
  "retrieved_utc": "2026-11-02T04:28:32.723564+00:00",
  "source_locator": "lines 109-111",
  "excerpt": "FT   TRANSMEM        108..128\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 45,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G1X9E2?format=txt&versions=45)

```json
{
  "evidence_id": "H9",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/G1X9E2?format=txt&versions=45",
  "source_sha256": "e35d509b45ea64e3eac1fedae5691280c0fa8c7205a8651df542bc73ee054a3f",
  "retrieved_utc": "2026-11-02T04:28:32.723564+00:00",
  "source_locator": "lines 112-114",
  "excerpt": "FT   TOPO_DOM        129..143\nFT                   /note=\"Cytoplasmic\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 45,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H10

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G1X9E2?format=txt&versions=45)

```json
{
  "evidence_id": "H10",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/G1X9E2?format=txt&versions=45",
  "source_sha256": "e35d509b45ea64e3eac1fedae5691280c0fa8c7205a8651df542bc73ee054a3f",
  "retrieved_utc": "2026-11-02T04:28:32.723564+00:00",
  "source_locator": "lines 115-117",
  "excerpt": "FT   TRANSMEM        144..164\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 45,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H11

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G1X9E2?format=txt&versions=45)

```json
{
  "evidence_id": "H11",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/G1X9E2?format=txt&versions=45",
  "source_sha256": "e35d509b45ea64e3eac1fedae5691280c0fa8c7205a8651df542bc73ee054a3f",
  "retrieved_utc": "2026-11-02T04:28:32.723564+00:00",
  "source_locator": "lines 118-120",
  "excerpt": "FT   TOPO_DOM        165..185\nFT                   /note=\"Extracellular\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 45,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H12

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G1X9E2?format=txt&versions=45)

```json
{
  "evidence_id": "H12",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/G1X9E2?format=txt&versions=45",
  "source_sha256": "e35d509b45ea64e3eac1fedae5691280c0fa8c7205a8651df542bc73ee054a3f",
  "retrieved_utc": "2026-11-02T04:28:32.723564+00:00",
  "source_locator": "lines 121-123",
  "excerpt": "FT   TRANSMEM        186..206\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 45,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H13

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G1X9E2?format=txt&versions=45)

```json
{
  "evidence_id": "H13",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/G1X9E2?format=txt&versions=45",
  "source_sha256": "e35d509b45ea64e3eac1fedae5691280c0fa8c7205a8651df542bc73ee054a3f",
  "retrieved_utc": "2026-11-02T04:28:32.723564+00:00",
  "source_locator": "lines 124-126",
  "excerpt": "FT   TOPO_DOM        207..326\nFT                   /note=\"Cytoplasmic\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 45,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H14

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G1X9E2?format=txt&versions=45)

```json
{
  "evidence_id": "H14",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/G1X9E2?format=txt&versions=45",
  "source_sha256": "e35d509b45ea64e3eac1fedae5691280c0fa8c7205a8651df542bc73ee054a3f",
  "retrieved_utc": "2026-11-02T04:28:32.723564+00:00",
  "source_locator": "lines 127-129",
  "excerpt": "FT   TRANSMEM        327..347\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 45,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H15

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G1X9E2?format=txt&versions=45)

```json
{
  "evidence_id": "H15",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/G1X9E2?format=txt&versions=45",
  "source_sha256": "e35d509b45ea64e3eac1fedae5691280c0fa8c7205a8651df542bc73ee054a3f",
  "retrieved_utc": "2026-11-02T04:28:32.723564+00:00",
  "source_locator": "lines 130-132",
  "excerpt": "FT   TOPO_DOM        348..356\nFT                   /note=\"Extracellular\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 45,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H16

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G1X9E2?format=txt&versions=45)

```json
{
  "evidence_id": "H16",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/G1X9E2?format=txt&versions=45",
  "source_sha256": "e35d509b45ea64e3eac1fedae5691280c0fa8c7205a8651df542bc73ee054a3f",
  "retrieved_utc": "2026-11-02T04:28:32.723564+00:00",
  "source_locator": "lines 133-135",
  "excerpt": "FT   TRANSMEM        357..377\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 45,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H17

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G1X9E2?format=txt&versions=45)

```json
{
  "evidence_id": "H17",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/G1X9E2?format=txt&versions=45",
  "source_sha256": "e35d509b45ea64e3eac1fedae5691280c0fa8c7205a8651df542bc73ee054a3f",
  "retrieved_utc": "2026-11-02T04:28:32.723564+00:00",
  "source_locator": "lines 136-138",
  "excerpt": "FT   TOPO_DOM        378..406\nFT                   /note=\"Cytoplasmic\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 45,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json), zero-based source row 57. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
