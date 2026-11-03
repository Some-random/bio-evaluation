# transmembrane_0107: before and after transfer clarification

[All 1,328 cases](../README.md) · [Method](../METHOD.md) · [Summary](../SUMMARY.md) · [Exact reviewer user message](../inputs/transmembrane_0107.txt)

**Task:** `transmembrane`  
**Author key, unchanged:** **D** — 229..247; 276..299; 320..345; 351..370; 382..404; 424..445; 466..487; 516..534; 555..573; 585..603; 623..645; 651..673

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
MEKDFTERSTKGQRKLANGVVENIESKLKNHLDNNNVINKSVNYEDVMCSNVKLSVHDDEYDIKNIKKDVCNLSKLSEERLSNNISLKDNNKVVKNPEIDTKTARQQYKKRLNSTQSTMNIEGNINNEKDDIIEDYDDGLIRNMDYEMSIVKNKRNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNSNNVDNRKRNKNEECYDESYCISDNLDEITSYRNKLSLYNKLRMCFNYFGPGWIVAIAYLDPGNLCSNLNVGLIRSPDPTLEKDYSGYYLLWIMVYGHMLGFIFQVLSMRLGHVTGLDLASLCSKEFDRTTSTIIYVLVQIAIWGAHIQAIIGTFIALNLIFGISVKVAIFYTLFEAIIYSFLENKSLGLLENVLSFLVGILAVSFFVNVFMTPINFKELAISILYPRIPKGKEIDALALLGSIISAHIFYLHTNLTAKKKSVICNDLSLRRYNTLGTIESGGSLFLSCLTNCIIVLTFAEVNLKSFERRDQYNLFTAYEVMRKSFGKISMYIWSFGLLSSGNNSSFMCEYASKSVVEGFLNKKINTFVRVFTFRLMLFSLLYMFLTLNKYTLDQLTNFINVIQVLLLPMATIPLYRFSIHENVLGEFRLKKFPKFAVFLIIIAIIISNVLLTFLDFVHKETSLITIFFLVIFSFLYFGFIIYFFNIPIKKNYIQRN

[Multiple Choices]
A. 13..35
B. 229..247; 276..299; 320..345; 351..370; 382..404; 466..487; 516..534; 555..573; 585..603; 623..645; 651..673
C. 229..247; 272..299; 320..345; 351..370; 382..404; 424..445; 466..487; 516..534; 555..573; 585..603; 623..645; 651..673
D. 229..247; 276..299; 320..345; 351..370; 382..404; 424..445; 466..487; 516..534; 555..573; 585..603; 623..645; 651..673
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

> The sequence matches the historical UniProt record, whose annotated transmembrane regions match Choice D exactly. These regions are marked helical with evidence code ECO:0000255, indicating computational annotation rather than direct experimental determination of each boundary.

Citations as saved: [H6](#evidence-h6), [H8](#evidence-h8), [H10](#evidence-h10), [H12](#evidence-h12), [H14](#evidence-h14), [H16](#evidence-h16), [H18](#evidence-h18), [H20](#evidence-h20), [H22](#evidence-h22), [H24](#evidence-h24), [H26](#evidence-h26), [H28](#evidence-h28).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence has a series of strongly hydrophobic stretches consistent with a multi-pass membrane protein, distinguishing the transmembrane-region choices from Choice A and supporting inclusion of the 424..445 segment absent from Choice B. But the sequence alone does not reliably establish all exact boundaries.


**Missing item-specific fact**

> The exact transmembrane-region coordinates, especially the 272 versus 276 start in Choices C and D, require a particular boundary annotation or prediction that is not supplied in the question.


**Reason**

> Hydropathy supports the general membrane topology, but predicted helix boundaries can vary. The GYYL residues immediately before the annotated 276 start make sequence-only exclusion of the earlier boundary uncertain.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "C",
  "D"
]
```

> The choices differ at the start of one predicted helix: Choice C includes four additional residues, GYYL, which are hydrophobic or aromatic and could plausibly lie at a membrane interface. The exact coordinate convention is not specified; the supplied sequence alone does not conclusively distinguish that boundary.


### Important caveats

- The reviewer-only UniProt evidence supports D for the matched sequence, but the actual source snapshot used by the author is unknown.
- The cited transmembrane annotations are computational, not experimental confirmation of exact boundaries.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has a series of strongly hydrophobic stretches consistent with a multi-pass membrane protein, distinguishing the transmembrane-region choices from Choice A and supporting inclusion of the 424..445 segment absent from Choice B. But the sequence alone does not reliably establish all exact boundaries.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The exact transmembrane-region coordinates, especially the 272 versus 276 start in Choices C and D, require a particular boundary annotation or prediction that is not supplied in the question.",
    "reason": "Hydropathy supports the general membrane topology, but predicted helix boundaries can vary. The GYYL residues immediately before the annotated 276 start make sequence-only exclusion of the earlier boundary uncertain."
  },
  "case_id": "transmembrane_0107",
  "expected_answer_check": {
    "evidence_ids": [
      "H6",
      "H8",
      "H10",
      "H12",
      "H14",
      "H16",
      "H18",
      "H20",
      "H22",
      "H24",
      "H26",
      "H28"
    ],
    "judgment": "supported",
    "reason": "The sequence matches the historical UniProt record, whose annotated transmembrane regions match Choice D exactly. These regions are marked helical with evidence code ECO:0000255, indicating computational annotation rather than direct experimental determination of each boundary."
  },
  "important_caveats": [
    "The reviewer-only UniProt evidence supports D for the matched sequence, but the actual source snapshot used by the author is unknown.",
    "The cited transmembrane annotations are computational, not experimental confirmation of exact boundaries."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "C",
      "D"
    ],
    "reason": "The choices differ at the start of one predicted helix: Choice C includes four additional residues, GYYL, which are hydrophobic or aromatic and could plausibly lie at a membrane interface. The exact coordinate convention is not specified; the supplied sequence alone does not conclusively distinguish that boundary."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0107",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches the historical UniProt record, whose annotated transmembrane regions match Choice D exactly. These regions are marked helical with evidence code ECO:0000255, indicating computational annotation rather than direct experimental determination of each boundary.",
    "evidence_ids": ["H6", "H8", "H10", "H12", "H14", "H16", "H18", "H20", "H22", "H24", "H26", "H28"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence has a series of strongly hydrophobic stretches consistent with a multi-pass membrane protein, distinguishing the transmembrane-region choices from Choice A and supporting inclusion of the 424..445 segment absent from Choice B. But the sequence alone does not reliably establish all exact boundaries.",
    "missing_item_specific_fact": "The exact transmembrane-region coordinates, especially the 272 versus 276 start in Choices C and D, require a particular boundary annotation or prediction that is not supplied in the question.",
    "reason": "Hydropathy supports the general membrane topology, but predicted helix boundaries can vary. The GYYL residues immediately before the annotated 276 start make sequence-only exclusion of the earlier boundary uncertain."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["C", "D"],
    "reason": "The choices differ at the start of one predicted helix: Choice C includes four additional residues, GYYL, which are hydrophobic or aromatic and could plausibly lie at a membrane interface. The exact coordinate convention is not specified; the supplied sequence alone does not conclusively distinguish that boundary."
  },
  "important_caveats": [
    "The reviewer-only UniProt evidence supports D for the matched sequence, but the actual source snapshot used by the author is unknown.",
    "The cited transmembrane annotations are computational, not experimental confirmation of exact boundaries."
  ]
}
```

</details>

## Before: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> Choice D lists exactly 12 transmembrane helices (229..247; 276..299; 320..345; 351..370; 382..404; 424..445; 466..487; 516..534; 555..573; 585..603; 623..645; 651..673), which match the UniProt annotation for Q8I3M7 (DMT1_PLAF7) precisely. The TM boundaries are annotated with evidence code ECO:0000255 (inferred by similarity), while the overall alternating topology (cytoplasmic/vacuolar) is supported by experimental evidence from PubMed:39467134 (ECO:0000269). The sequence match is confirmed (sha256 identical).

Citations as saved: [C6](#evidence-c6), [C8](#evidence-c8), [C10](#evidence-c10), [C12](#evidence-c12), [C14](#evidence-c14), [C16](#evidence-c16), [C18](#evidence-c18), [C20](#evidence-c20), [C22](#evidence-c22), [C24](#evidence-c24), [C26](#evidence-c26), [C28](#evidence-c28), [C5](#evidence-c5), [C7](#evidence-c7), [C9](#evidence-c9), [C11](#evidence-c11), [C13](#evidence-c13), [C15](#evidence-c15), [C17](#evidence-c17), [C19](#evidence-c19), [C21](#evidence-c21), [C23](#evidence-c23), [C25](#evidence-c25), [C27](#evidence-c27), [C29](#evidence-c29), [C32](#evidence-c32), [H6](#evidence-h6), [H8](#evidence-h8), [H10](#evidence-h10), [H12](#evidence-h12), [H14](#evidence-h14), [H16](#evidence-h16), [H18](#evidence-h18), [H20](#evidence-h20), [H22](#evidence-h22), [H24](#evidence-h24), [H26](#evidence-h26), [H28](#evidence-h28), [H29](#evidence-h29), [H4](#evidence-h4), [H5](#evidence-h5), [H7](#evidence-h7), [H9](#evidence-h9), [H11](#evidence-h11), [H13](#evidence-h13), [H15](#evidence-h15), [H17](#evidence-h17), [H19](#evidence-h19), [H21](#evidence-h21), [H23](#evidence-h23), [H25](#evidence-h25), [H27](#evidence-h27).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> A model could use hydrophobicity analysis to identify that the N-terminal region (13..35, Choice A) is in a charged/polar cytoplasmic domain and is not a TM helix. The presence of a hydrophobic stretch at 424..445 (present in D, absent in B) could potentially be identified by scanning for a ~22-residue hydrophobic segment between two loops. However, the critical distinction between D and C (second TM starting at 276 vs 272) involves only a 4-residue boundary shift that depends on the precise hydrophobicity cutoff of a specific prediction algorithm.


**Missing item-specific fact**

> The exact hydrophobicity boundary at position 272 vs 276 (whether residues 272-275 are sufficiently hydrophobic to be included in the TM helix or belong to the preceding vacuolar loop) is determined by the specific computational method (ECO:0000255, inferred by similarity) used to generate the annotation. This fine-grained boundary cannot be reliably resolved by general hydrophobicity reasoning alone, as the 4-residue difference falls within the range where different prediction tools disagree.


**Reason**

> The choices differ by (1) omission of the 424..445 TM helix (B vs D) and (2) a 4-residue shift in the start of the second TM helix (272 vs 276, C vs D). While the presence of a hydrophobic region at 424..445 might be identifiable by general reasoning, the precise boundary at 276 vs 272 is a method-specific prediction detail (ECO:0000255). Distinguishing D from C requires knowledge of the exact annotation rather than a generalizable biological argument.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Choice A (13..35) is clearly wrong as it falls in the highly charged N-terminal cytoplasmic region. Choice B omits a TM helix (424..445) that corresponds to a hydrophobic stretch. Choice C shifts the second TM boundary by 4 residues. Only D matches the full annotation. While C is close to D, the 4-residue shift makes it a distinct and less accurate answer per the annotation.


### Important caveats

- All TM annotations carry evidence code ECO:0000255 (inferred by similarity), meaning they are computational predictions rather than experimentally determined boundaries.
- The overall topology (alternating cytoplasmic/vacuolar orientation) is supported by experimental work (PubMed:39467134, 2024 PNAS), but individual helix boundaries remain computational.
- The reviewer-only UniProt evidence confirms the sequence match and annotation but was not available to the evaluated model.
- The author source snapshot is unknown; the annotation may have been updated since the benchmark was constructed.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "A model could use hydrophobicity analysis to identify that the N-terminal region (13..35, Choice A) is in a charged/polar cytoplasmic domain and is not a TM helix. The presence of a hydrophobic stretch at 424..445 (present in D, absent in B) could potentially be identified by scanning for a ~22-residue hydrophobic segment between two loops. However, the critical distinction between D and C (second TM starting at 276 vs 272) involves only a 4-residue boundary shift that depends on the precise hydrophobicity cutoff of a specific prediction algorithm.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The exact hydrophobicity boundary at position 272 vs 276 (whether residues 272-275 are sufficiently hydrophobic to be included in the TM helix or belong to the preceding vacuolar loop) is determined by the specific computational method (ECO:0000255, inferred by similarity) used to generate the annotation. This fine-grained boundary cannot be reliably resolved by general hydrophobicity reasoning alone, as the 4-residue difference falls within the range where different prediction tools disagree.",
    "reason": "The choices differ by (1) omission of the 424..445 TM helix (B vs D) and (2) a 4-residue shift in the start of the second TM helix (272 vs 276, C vs D). While the presence of a hydrophobic region at 424..445 might be identifiable by general reasoning, the precise boundary at 276 vs 272 is a method-specific prediction detail (ECO:0000255). Distinguishing D from C requires knowledge of the exact annotation rather than a generalizable biological argument."
  },
  "case_id": "transmembrane_0107",
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
      "C22",
      "C24",
      "C26",
      "C28",
      "C5",
      "C7",
      "C9",
      "C11",
      "C13",
      "C15",
      "C17",
      "C19",
      "C21",
      "C23",
      "C25",
      "C27",
      "C29",
      "C32",
      "H6",
      "H8",
      "H10",
      "H12",
      "H14",
      "H16",
      "H18",
      "H20",
      "H22",
      "H24",
      "H26",
      "H28",
      "H29",
      "H4",
      "H5",
      "H7",
      "H9",
      "H11",
      "H13",
      "H15",
      "H17",
      "H19",
      "H21",
      "H23",
      "H25",
      "H27"
    ],
    "judgment": "supported",
    "reason": "Choice D lists exactly 12 transmembrane helices (229..247; 276..299; 320..345; 351..370; 382..404; 424..445; 466..487; 516..534; 555..573; 585..603; 623..645; 651..673), which match the UniProt annotation for Q8I3M7 (DMT1_PLAF7) precisely. The TM boundaries are annotated with evidence code ECO:0000255 (inferred by similarity), while the overall alternating topology (cytoplasmic/vacuolar) is supported by experimental evidence from PubMed:39467134 (ECO:0000269). The sequence match is confirmed (sha256 identical)."
  },
  "important_caveats": [
    "All TM annotations carry evidence code ECO:0000255 (inferred by similarity), meaning they are computational predictions rather than experimentally determined boundaries.",
    "The overall topology (alternating cytoplasmic/vacuolar orientation) is supported by experimental work (PubMed:39467134, 2024 PNAS), but individual helix boundaries remain computational.",
    "The reviewer-only UniProt evidence confirms the sequence match and annotation but was not available to the evaluated model.",
    "The author source snapshot is unknown; the annotation may have been updated since the benchmark was constructed."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Choice A (13..35) is clearly wrong as it falls in the highly charged N-terminal cytoplasmic region. Choice B omits a TM helix (424..445) that corresponds to a hydrophobic stretch. Choice C shifts the second TM boundary by 4 residues. Only D matches the full annotation. While C is close to D, the 4-residue shift makes it a distinct and less accurate answer per the annotation."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{"case_id":"transmembrane_0107","expected_answer_check":{"judgment":"supported","reason":"Choice D lists exactly 12 transmembrane helices (229..247; 276..299; 320..345; 351..370; 382..404; 424..445; 466..487; 516..534; 555..573; 585..603; 623..645; 651..673), which match the UniProt annotation for Q8I3M7 (DMT1_PLAF7) precisely. The TM boundaries are annotated with evidence code ECO:0000255 (inferred by similarity), while the overall alternating topology (cytoplasmic/vacuolar) is supported by experimental evidence from PubMed:39467134 (ECO:0000269). The sequence match is confirmed (sha256 identical).","evidence_ids":["C6","C8","C10","C12","C14","C16","C18","C20","C22","C24","C26","C28","C5","C7","C9","C11","C13","C15","C17","C19","C21","C23","C25","C27","C29","C32","H6","H8","H10","H12","H14","H16","H18","H20","H22","H24","H26","H28","H29","H4","H5","H7","H9","H11","H13","H15","H17","H19","H21","H23","H25","H27"]},"answerability_check":{"judgment":"lookup_or_memorization_dependent","discriminating_biological_argument":"A model could use hydrophobicity analysis to identify that the N-terminal region (13..35, Choice A) is in a charged/polar cytoplasmic domain and is not a TM helix. The presence of a hydrophobic stretch at 424..445 (present in D, absent in B) could potentially be identified by scanning for a ~22-residue hydrophobic segment between two loops. However, the critical distinction between D and C (second TM starting at 276 vs 272) involves only a 4-residue boundary shift that depends on the precise hydrophobicity cutoff of a specific prediction algorithm.","missing_item_specific_fact":"The exact hydrophobicity boundary at position 272 vs 276 (whether residues 272-275 are sufficiently hydrophobic to be included in the TM helix or belong to the preceding vacuolar loop) is determined by the specific computational method (ECO:0000255, inferred by similarity) used to generate the annotation. This fine-grained boundary cannot be reliably resolved by general hydrophobicity reasoning alone, as the 4-residue difference falls within the range where different prediction tools disagree.","reason":"The choices differ by (1) omission of the 424..445 TM helix (B vs D) and (2) a 4-residue shift in the start of the second TM helix (272 vs 276, C vs D). While the presence of a hydrophobic region at 424..445 might be identifiable by general reasoning, the precise boundary at 276 vs 272 is a method-specific prediction detail (ECO:0000255). Distinguishing D from C requires knowledge of the exact annotation rather than a generalizable biological argument."},"question_ambiguity":{"multiple_defensible_options":[],"reason":"Choice A (13..35) is clearly wrong as it falls in the highly charged N-terminal cytoplasmic region. Choice B omits a TM helix (424..445) that corresponds to a hydrophobic stretch. Choice C shifts the second TM boundary by 4 residues. Only D matches the full annotation. While C is close to D, the 4-residue shift makes it a distinct and less accurate answer per the annotation."},"important_caveats":["All TM annotations carry evidence code ECO:0000255 (inferred by similarity), meaning they are computational predictions rather than experimentally determined boundaries.","The overall topology (alternating cytoplasmic/vacuolar orientation) is supported by experimental work (PubMed:39467134, 2024 PNAS), but individual helix boundaries remain computational.","The reviewer-only UniProt evidence confirms the sequence match and annotation but was not available to the evaluated model.","The author source snapshot is unknown; the annotation may have been updated since the benchmark was constructed."]}
```

</details>

## After: GPT-6 Luna

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence-matched historical UniProt entry annotates the transmembrane spans listed in D, including 424..445; those annotations match D rather than B or C. The helix annotations carry computational evidence code ECO:0000255, so this supports D as a predicted topology, not as experimental confirmation of every boundary.

Citations as saved: [H6](#evidence-h6), [H8](#evidence-h8), [H10](#evidence-h10), [H12](#evidence-h12), [H14](#evidence-h14), [H16](#evidence-h16), [H18](#evidence-h18), [H20](#evidence-h20), [H22](#evidence-h22), [H24](#evidence-h24), [H26](#evidence-h26), [H28](#evidence-h28).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has repeated hydrophobic stretches of roughly membrane-helix length, separated by more polar regions, supporting a multipass membrane protein. The hydrophobic stretch around 424..445 favors D over B, which omits it; the polar residues preceding the next hydrophobic run make C's earlier start at 272 less plausible than D's start at 276. These sequence patterns and general principles of multipass transporter topology are transferable and do not require knowing this protein's database entry.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The sequence itself provides a meaningful basis for distinguishing the listed alternatives. Exact helix boundaries can be uncertain from sequence alone, but the competing options differ at positions where hydrophobicity and the surrounding sequence support D.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> D is the best-supported option among those offered: B omits a hydrophobic span, while C extends the second span into a less hydrophobic preceding region.


### Important caveats

- The reviewer-only annotation matches the supplied sequence, but its helix calls are computational rather than direct experimental measurements.
- The author's exact data-source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has repeated hydrophobic stretches of roughly membrane-helix length, separated by more polar regions, supporting a multipass membrane protein. The hydrophobic stretch around 424..445 favors D over B, which omits it; the polar residues preceding the next hydrophobic run make C's earlier start at 272 less plausible than D's start at 276. These sequence patterns and general principles of multipass transporter topology are transferable and do not require knowing this protein's database entry.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The sequence itself provides a meaningful basis for distinguishing the listed alternatives. Exact helix boundaries can be uncertain from sequence alone, but the competing options differ at positions where hydrophobicity and the surrounding sequence support D."
  },
  "case_id": "transmembrane_0107",
  "expected_answer_check": {
    "evidence_ids": [
      "H6",
      "H8",
      "H10",
      "H12",
      "H14",
      "H16",
      "H18",
      "H20",
      "H22",
      "H24",
      "H26",
      "H28"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched historical UniProt entry annotates the transmembrane spans listed in D, including 424..445; those annotations match D rather than B or C. The helix annotations carry computational evidence code ECO:0000255, so this supports D as a predicted topology, not as experimental confirmation of every boundary."
  },
  "important_caveats": [
    "The reviewer-only annotation matches the supplied sequence, but its helix calls are computational rather than direct experimental measurements.",
    "The author's exact data-source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "D is the best-supported option among those offered: B omits a hydrophobic span, while C extends the second span into a less hydrophobic preceding region."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0107",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched historical UniProt entry annotates the transmembrane spans listed in D, including 424..445; those annotations match D rather than B or C. The helix annotations carry computational evidence code ECO:0000255, so this supports D as a predicted topology, not as experimental confirmation of every boundary.",
    "evidence_ids": ["H6", "H8", "H10", "H12", "H14", "H16", "H18", "H20", "H22", "H24", "H26", "H28"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has repeated hydrophobic stretches of roughly membrane-helix length, separated by more polar regions, supporting a multipass membrane protein. The hydrophobic stretch around 424..445 favors D over B, which omits it; the polar residues preceding the next hydrophobic run make C's earlier start at 272 less plausible than D's start at 276. These sequence patterns and general principles of multipass transporter topology are transferable and do not require knowing this protein's database entry.",
    "missing_item_specific_fact": "",
    "reason": "The sequence itself provides a meaningful basis for distinguishing the listed alternatives. Exact helix boundaries can be uncertain from sequence alone, but the competing options differ at positions where hydrophobicity and the surrounding sequence support D."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "D is the best-supported option among those offered: B omits a hydrophobic span, while C extends the second span into a less hydrophobic preceding region."
  },
  "important_caveats": [
    "The reviewer-only annotation matches the supplied sequence, but its helix calls are computational rather than direct experimental measurements.",
    "The author's exact data-source snapshot is unknown."
  ]
}
```

</details>

## After: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry Q8I3M7 (DMT1_PLAF7) annotates exactly 12 transmembrane helices at positions 229..247, 276..299, 320..345, 351..370, 382..404, 424..445, 466..487, 516..534, 555..573, 585..603, 623..645, 651..673, matching option D exactly. The TM helix annotations carry evidence code ECO:0000255 (inferred by similarity), i.e. computational/annotation transfer rather than direct experimental determination of each helix boundary. The topological domain assignments carry ECO:0000305 (curator inference) and the C-terminal cytoplasmic domain (674..684) carries experimental evidence ECO:0000269 from PubMed:39467134. The overall topology is consistent with the NRAMP/DMT family architecture.

Citations as saved: [C6](#evidence-c6), [C8](#evidence-c8), [C10](#evidence-c10), [C12](#evidence-c12), [C14](#evidence-c14), [C16](#evidence-c16), [C18](#evidence-c18), [C20](#evidence-c20), [C22](#evidence-c22), [C24](#evidence-c24), [C26](#evidence-c26), [C28](#evidence-c28), [C5](#evidence-c5), [C7](#evidence-c7), [C9](#evidence-c9), [C11](#evidence-c11), [C13](#evidence-c13), [C15](#evidence-c15), [C17](#evidence-c17), [C19](#evidence-c19), [C21](#evidence-c21), [C23](#evidence-c23), [C25](#evidence-c25), [C27](#evidence-c27), [C29](#evidence-c29).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The C-terminal ~450 residues of this protein display a series of hydrophobic stretches separated by short hydrophilic loops, characteristic of a multi-pass membrane transporter. Recognizing this as an NRAMP (Natural Resistance-Associated Macrophage Protein) / DMT-family transporter is feasible from the domain architecture: a long hydrophilic N-terminal region (~1-228) followed by a compact cluster of alternating hydrophobic and hydrophilic segments. NRAMP-family members (e.g., human NRAMP1/SLC11A1, plant IRT1/2, yeast SMF proteins) consistently possess 12 transmembrane helices. This family-level regularity directly distinguishes option D (12 TM regions) from option B (11 TM regions, which omits the 424..445 helix). For the C-vs-D distinction (second TM starting at 272 vs 276), a model can inspect the residue composition at positions 272-275: if those residues are polar or charged (e.g., containing Ser, Thr, Asn, Gln, Lys, Arg), they are inconsistent with a lipid-facing helix and would be assigned to the preceding loop, favoring the 276 start. The NRAMP family argument eliminates B, and the local hydrophobicity at the 272-275 boundary provides a sequence-based argument for D over C.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The NRAMP/DMT family is well-characterized as a 12-TM-helix transporter family across eukaryotes (human, plant, fungal homologs). This is transferable family-level knowledge, not a fact specific to this exact protein. The boundary question (272 vs 276) is addressable by examining the hydrophobicity of the specific residues in the supplied sequence. A model does not need to recall the UniProt entry for Q8I3M7 to arrive at D; it can use family-level TM count and local sequence analysis.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options B and D are clearly distinguished by the NRAMP-family 12-TM expectation. Options C and D differ only in the start position of the second TM (272 vs 276), a 4-residue boundary question. While different prediction tools might disagree on such fine boundaries, the local hydrophobicity profile of the supplied sequence provides a reasonable basis for preferring 276. The distinction is fine but not genuinely ambiguous given the family context and sequence analysis.


### Important caveats

- The UniProt TM annotations carry evidence code ECO:0000255 (inferred by similarity), meaning the exact helix boundaries are computational/annotation transfers rather than experimentally determined at single-residue resolution.
- The 272-vs-276 boundary (C vs D) is a fine-grained prediction-boundary question; different TM-prediction tools (TMHMM, Phobius, DeepTMHMM) could disagree by a few residues at helix termini. The NRAMP-family 12-TM argument robustly eliminates B but the C-vs-D distinction relies more heavily on local hydrophobicity judgment.
- The reviewer-only evidence confirms the sequence matches Q8I3M7 (Plasmodium falciparum DMT1), but the evaluated model receives only the raw sequence with no name, organism, or accession.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The C-terminal ~450 residues of this protein display a series of hydrophobic stretches separated by short hydrophilic loops, characteristic of a multi-pass membrane transporter. Recognizing this as an NRAMP (Natural Resistance-Associated Macrophage Protein) / DMT-family transporter is feasible from the domain architecture: a long hydrophilic N-terminal region (~1-228) followed by a compact cluster of alternating hydrophobic and hydrophilic segments. NRAMP-family members (e.g., human NRAMP1/SLC11A1, plant IRT1/2, yeast SMF proteins) consistently possess 12 transmembrane helices. This family-level regularity directly distinguishes option D (12 TM regions) from option B (11 TM regions, which omits the 424..445 helix). For the C-vs-D distinction (second TM starting at 272 vs 276), a model can inspect the residue composition at positions 272-275: if those residues are polar or charged (e.g., containing Ser, Thr, Asn, Gln, Lys, Arg), they are inconsistent with a lipid-facing helix and would be assigned to the preceding loop, favoring the 276 start. The NRAMP family argument eliminates B, and the local hydrophobicity at the 272-275 boundary provides a sequence-based argument for D over C.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The NRAMP/DMT family is well-characterized as a 12-TM-helix transporter family across eukaryotes (human, plant, fungal homologs). This is transferable family-level knowledge, not a fact specific to this exact protein. The boundary question (272 vs 276) is addressable by examining the hydrophobicity of the specific residues in the supplied sequence. A model does not need to recall the UniProt entry for Q8I3M7 to arrive at D; it can use family-level TM count and local sequence analysis."
  },
  "case_id": "transmembrane_0107",
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
      "C22",
      "C24",
      "C26",
      "C28",
      "C5",
      "C7",
      "C9",
      "C11",
      "C13",
      "C15",
      "C17",
      "C19",
      "C21",
      "C23",
      "C25",
      "C27",
      "C29"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry Q8I3M7 (DMT1_PLAF7) annotates exactly 12 transmembrane helices at positions 229..247, 276..299, 320..345, 351..370, 382..404, 424..445, 466..487, 516..534, 555..573, 585..603, 623..645, 651..673, matching option D exactly. The TM helix annotations carry evidence code ECO:0000255 (inferred by similarity), i.e. computational/annotation transfer rather than direct experimental determination of each helix boundary. The topological domain assignments carry ECO:0000305 (curator inference) and the C-terminal cytoplasmic domain (674..684) carries experimental evidence ECO:0000269 from PubMed:39467134. The overall topology is consistent with the NRAMP/DMT family architecture."
  },
  "important_caveats": [
    "The UniProt TM annotations carry evidence code ECO:0000255 (inferred by similarity), meaning the exact helix boundaries are computational/annotation transfers rather than experimentally determined at single-residue resolution.",
    "The 272-vs-276 boundary (C vs D) is a fine-grained prediction-boundary question; different TM-prediction tools (TMHMM, Phobius, DeepTMHMM) could disagree by a few residues at helix termini. The NRAMP-family 12-TM argument robustly eliminates B but the C-vs-D distinction relies more heavily on local hydrophobicity judgment.",
    "The reviewer-only evidence confirms the sequence matches Q8I3M7 (Plasmodium falciparum DMT1), but the evaluated model receives only the raw sequence with no name, organism, or accession."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options B and D are clearly distinguished by the NRAMP-family 12-TM expectation. Options C and D differ only in the start position of the second TM (272 vs 276), a 4-residue boundary question. While different prediction tools might disagree on such fine boundaries, the local hydrophobicity profile of the supplied sequence provides a reasonable basis for preferring 276. The distinction is fine but not genuinely ambiguous given the family context and sequence analysis."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0107",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry Q8I3M7 (DMT1_PLAF7) annotates exactly 12 transmembrane helices at positions 229..247, 276..299, 320..345, 351..370, 382..404, 424..445, 466..487, 516..534, 555..573, 585..603, 623..645, 651..673, matching option D exactly. The TM helix annotations carry evidence code ECO:0000255 (inferred by similarity), i.e. computational/annotation transfer rather than direct experimental determination of each helix boundary. The topological domain assignments carry ECO:0000305 (curator inference) and the C-terminal cytoplasmic domain (674..684) carries experimental evidence ECO:0000269 from PubMed:39467134. The overall topology is consistent with the NRAMP/DMT family architecture.",
    "evidence_ids": ["C6", "C8", "C10", "C12", "C14", "C16", "C18", "C20", "C22", "C24", "C26", "C28", "C5", "C7", "C9", "C11", "C13", "C15", "C17", "C19", "C21", "C23", "C25", "C27", "C29"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The C-terminal ~450 residues of this protein display a series of hydrophobic stretches separated by short hydrophilic loops, characteristic of a multi-pass membrane transporter. Recognizing this as an NRAMP (Natural Resistance-Associated Macrophage Protein) / DMT-family transporter is feasible from the domain architecture: a long hydrophilic N-terminal region (~1-228) followed by a compact cluster of alternating hydrophobic and hydrophilic segments. NRAMP-family members (e.g., human NRAMP1/SLC11A1, plant IRT1/2, yeast SMF proteins) consistently possess 12 transmembrane helices. This family-level regularity directly distinguishes option D (12 TM regions) from option B (11 TM regions, which omits the 424..445 helix). For the C-vs-D distinction (second TM starting at 272 vs 276), a model can inspect the residue composition at positions 272-275: if those residues are polar or charged (e.g., containing Ser, Thr, Asn, Gln, Lys, Arg), they are inconsistent with a lipid-facing helix and would be assigned to the preceding loop, favoring the 276 start. The NRAMP family argument eliminates B, and the local hydrophobicity at the 272-275 boundary provides a sequence-based argument for D over C.",
    "missing_item_specific_fact": "",
    "reason": "The NRAMP/DMT family is well-characterized as a 12-TM-helix transporter family across eukaryotes (human, plant, fungal homologs). This is transferable family-level knowledge, not a fact specific to this exact protein. The boundary question (272 vs 276) is addressable by examining the hydrophobicity of the specific residues in the supplied sequence. A model does not need to recall the UniProt entry for Q8I3M7 to arrive at D; it can use family-level TM count and local sequence analysis."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options B and D are clearly distinguished by the NRAMP-family 12-TM expectation. Options C and D differ only in the start position of the second TM (272 vs 276), a 4-residue boundary question. While different prediction tools might disagree on such fine boundaries, the local hydrophobicity profile of the supplied sequence provides a reasonable basis for preferring 276. The distinction is fine but not genuinely ambiguous given the family context and sequence analysis."
  },
  "important_caveats": [
    "The UniProt TM annotations carry evidence code ECO:0000255 (inferred by similarity), meaning the exact helix boundaries are computational/annotation transfers rather than experimentally determined at single-residue resolution.",
    "The 272-vs-276 boundary (C vs D) is a fine-grained prediction-boundary question; different TM-prediction tools (TMHMM, Phobius, DeepTMHMM) could disagree by a few residues at helix termini. The NRAMP-family 12-TM argument robustly eliminates B but the C-vs-D distinction relies more heavily on local hydrophobicity judgment.",
    "The reviewer-only evidence confirms the sequence matches Q8I3M7 (Plasmodium falciparum DMT1), but the evaluated model receives only the raw sequence with no name, organism, or accession."
  ]
}
```

</details>

## Existing project source checks of the old Luna review only

These unchanged notes concern the earlier Luna claims. They do not validate either new review or the old Qwen review. No new scientific adjudication was performed.

## Project source-check notes

These project-authored, AI-assisted checks assess specific source claims. They are not expert adjudication and do not replace Luna’s saved review or the author key.

### Source check 1

**Check:** `model_residue_identity_error_in_ambiguity_reason`.

> OptionC extends the second interval from keyD276..299 to272..299. Original1-based residues272..275 are YSGY, not the model claimed GYYL. The historical annotations match D and use ECO:0000255.

**Remaining uncertainty:** The incorrect four-residue string invalidates that literal premise only. Whether the shifted span remains biologically plausible is unresolved here; no ambiguity or key verdict is changed.

**Direct check of the original sequence:**

```json
{
  "inclusive_range": [
    272,
    275
  ],
  "indexing": "1-based",
  "residues": "YSGY",
  "sequence_sha256": "ad3e4f51961e13a279b7a2c9a8d92d3b0cb723ff3f0b8baf5ac09b89a6e02c7c"
}
```

Evidence checked: [H6](#evidence-h6), [H8](#evidence-h8), [H10](#evidence-h10), [H12](#evidence-h12), [H14](#evidence-h14), [H16](#evidence-h16), [H18](#evidence-h18), [H20](#evidence-h20), [H22](#evidence-h22), [H24](#evidence-h24), [H26](#evidence-h26), [H28](#evidence-h28).

## Complete reviewer-only evidence and qualifications

All excerpts supplied in the original and revised reviewer user message follow. This material was not available to the original evaluated model. Accession identity came from dataset image-path metadata. Source support and transferable discrimination are separate judgments.

**Applicability metadata, unchanged:**

```json
{
  "requested_accession": "Q8I3M7",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "benchmark_sequence_sha256": "ad3e4f51961e13a279b7a2c9a8d92d3b0cb723ff3f0b8baf5ac09b89a6e02c7c",
  "benchmark_sequence_length": 684,
  "current_status": "retrieved",
  "current_sequence_comparison": "matched",
  "current_entry_audit": {
    "entryVersion": 119,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2003-03-01",
    "sequenceVersion": 1
  },
  "current_uniprot_release": "2026_03",
  "current_record_sha256": "574775c6d804e30e776f29661e18531280dbca6553bdbb138d45bcd3288c2f30",
  "current_source_sequence_sha256": "ad3e4f51961e13a279b7a2c9a8d92d3b0cb723ff3f0b8baf5ac09b89a6e02c7c",
  "current_source_sequence_length": 684,
  "historical_status": "retrieved",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "selected_historical_entry_version": 117,
  "selected_historical_version": {
    "accession": "Q8I3M7",
    "database": "Swiss-Prot",
    "entryVersion": 117,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "DMT1_PLAF7",
    "sequenceVersion": 1
  },
  "selected_historical_record_sha256": "75db2a237303bdcca1e3dff1a43527aaee7cf8b65d99a684cef3447701a84319",
  "selected_historical_source_sequence_sha256": "ad3e4f51961e13a279b7a2c9a8d92d3b0cb723ff3f0b8baf5ac09b89a6e02c7c",
  "selected_historical_source_sequence_length": 684,
  "latest_at_cutoff_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 117,
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I3M7.json)

```json
{
  "evidence_id": "C1",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q8I3M7.json",
  "source_sha256": "574775c6d804e30e776f29661e18531280dbca6553bdbb138d45bcd3288c2f30",
  "retrieved_utc": "2026-11-02T04:32:04.373002+00:00",
  "json_pointer": "/primaryAccession",
  "excerpt": "\"Q8I3M7\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I3M7.json)

```json
{
  "evidence_id": "C2",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q8I3M7.json",
  "source_sha256": "574775c6d804e30e776f29661e18531280dbca6553bdbb138d45bcd3288c2f30",
  "retrieved_utc": "2026-11-02T04:32:04.373002+00:00",
  "json_pointer": "/entryAudit",
  "excerpt": "{\"entryVersion\":119,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2003-03-01\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I3M7.json)

```json
{
  "evidence_id": "C3",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q8I3M7.json",
  "source_sha256": "574775c6d804e30e776f29661e18531280dbca6553bdbb138d45bcd3288c2f30",
  "retrieved_utc": "2026-11-02T04:32:04.373002+00:00",
  "json_pointer": "/organism",
  "excerpt": "{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP000001450\",\"source\":\"Proteomes\"}],\"lineage\":[\"Eukaryota\",\"Sar\",\"Alveolata\",\"Apicomplexa\",\"Aconoidasida\",\"Haemosporida\",\"Plasmodiidae\",\"Plasmodium\",\"Laverania\"],\"scientificName\":\"Plasmodium falciparum (isolate 3D7)\",\"taxonId\":36329}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I3M7.json)

```json
{
  "evidence_id": "C4",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q8I3M7.json",
  "source_sha256": "574775c6d804e30e776f29661e18531280dbca6553bdbb138d45bcd3288c2f30",
  "retrieved_utc": "2026-11-02T04:32:04.373002+00:00",
  "json_pointer": "/proteinDescription",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"35404116\",\"source\":\"PubMed\"}],\"value\":\"Food vacuole resident transporter 1\"}},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39575308\",\"source\":\"PubMed\"}],\"value\":\"PfNRAMP\"}}],\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39467134\",\"source\":\"PubMed\"}],\"value\":\"Divalent metal transporter 1\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39467134\",\"source\":\"PubMed\"}],\"value\":\"DMT1\"},{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39467134\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39575308\",\"source\":\"PubMed\"}],\"value\":\"PfDMT1\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I3M7.json)

```json
{
  "evidence_id": "C5",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q8I3M7.json",
  "source_sha256": "574775c6d804e30e776f29661e18531280dbca6553bdbb138d45bcd3288c2f30",
  "retrieved_utc": "2026-11-02T04:32:04.373002+00:00",
  "json_pointer": "/features/1",
  "excerpt": "{\"description\":\"Cytoplasmic\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":228},\"start\":{\"modifier\":\"EXACT\",\"value\":1}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I3M7.json)

```json
{
  "evidence_id": "C6",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q8I3M7.json",
  "source_sha256": "574775c6d804e30e776f29661e18531280dbca6553bdbb138d45bcd3288c2f30",
  "retrieved_utc": "2026-11-02T04:32:04.373002+00:00",
  "json_pointer": "/features/2",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":247},\"start\":{\"modifier\":\"EXACT\",\"value\":229}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I3M7.json)

```json
{
  "evidence_id": "C7",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q8I3M7.json",
  "source_sha256": "574775c6d804e30e776f29661e18531280dbca6553bdbb138d45bcd3288c2f30",
  "retrieved_utc": "2026-11-02T04:32:04.373002+00:00",
  "json_pointer": "/features/3",
  "excerpt": "{\"description\":\"Vacuolar\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":275},\"start\":{\"modifier\":\"EXACT\",\"value\":248}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I3M7.json)

```json
{
  "evidence_id": "C8",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q8I3M7.json",
  "source_sha256": "574775c6d804e30e776f29661e18531280dbca6553bdbb138d45bcd3288c2f30",
  "retrieved_utc": "2026-11-02T04:32:04.373002+00:00",
  "json_pointer": "/features/4",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":299},\"start\":{\"modifier\":\"EXACT\",\"value\":276}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I3M7.json)

```json
{
  "evidence_id": "C9",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q8I3M7.json",
  "source_sha256": "574775c6d804e30e776f29661e18531280dbca6553bdbb138d45bcd3288c2f30",
  "retrieved_utc": "2026-11-02T04:32:04.373002+00:00",
  "json_pointer": "/features/5",
  "excerpt": "{\"description\":\"Cytoplasmic\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":319},\"start\":{\"modifier\":\"EXACT\",\"value\":300}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I3M7.json)

```json
{
  "evidence_id": "C10",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q8I3M7.json",
  "source_sha256": "574775c6d804e30e776f29661e18531280dbca6553bdbb138d45bcd3288c2f30",
  "retrieved_utc": "2026-11-02T04:32:04.373002+00:00",
  "json_pointer": "/features/6",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":345},\"start\":{\"modifier\":\"EXACT\",\"value\":320}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I3M7.json)

```json
{
  "evidence_id": "C11",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q8I3M7.json",
  "source_sha256": "574775c6d804e30e776f29661e18531280dbca6553bdbb138d45bcd3288c2f30",
  "retrieved_utc": "2026-11-02T04:32:04.373002+00:00",
  "json_pointer": "/features/7",
  "excerpt": "{\"description\":\"Vacuolar\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":350},\"start\":{\"modifier\":\"EXACT\",\"value\":346}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I3M7.json)

```json
{
  "evidence_id": "C12",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q8I3M7.json",
  "source_sha256": "574775c6d804e30e776f29661e18531280dbca6553bdbb138d45bcd3288c2f30",
  "retrieved_utc": "2026-11-02T04:32:04.373002+00:00",
  "json_pointer": "/features/8",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":370},\"start\":{\"modifier\":\"EXACT\",\"value\":351}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C13

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I3M7.json)

```json
{
  "evidence_id": "C13",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q8I3M7.json",
  "source_sha256": "574775c6d804e30e776f29661e18531280dbca6553bdbb138d45bcd3288c2f30",
  "retrieved_utc": "2026-11-02T04:32:04.373002+00:00",
  "json_pointer": "/features/9",
  "excerpt": "{\"description\":\"Cytoplasmic\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":381},\"start\":{\"modifier\":\"EXACT\",\"value\":371}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C14

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I3M7.json)

```json
{
  "evidence_id": "C14",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q8I3M7.json",
  "source_sha256": "574775c6d804e30e776f29661e18531280dbca6553bdbb138d45bcd3288c2f30",
  "retrieved_utc": "2026-11-02T04:32:04.373002+00:00",
  "json_pointer": "/features/10",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":404},\"start\":{\"modifier\":\"EXACT\",\"value\":382}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C15

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I3M7.json)

```json
{
  "evidence_id": "C15",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q8I3M7.json",
  "source_sha256": "574775c6d804e30e776f29661e18531280dbca6553bdbb138d45bcd3288c2f30",
  "retrieved_utc": "2026-11-02T04:32:04.373002+00:00",
  "json_pointer": "/features/11",
  "excerpt": "{\"description\":\"Vacuolar\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":423},\"start\":{\"modifier\":\"EXACT\",\"value\":405}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C16

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I3M7.json)

```json
{
  "evidence_id": "C16",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q8I3M7.json",
  "source_sha256": "574775c6d804e30e776f29661e18531280dbca6553bdbb138d45bcd3288c2f30",
  "retrieved_utc": "2026-11-02T04:32:04.373002+00:00",
  "json_pointer": "/features/12",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":445},\"start\":{\"modifier\":\"EXACT\",\"value\":424}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C17

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I3M7.json)

```json
{
  "evidence_id": "C17",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q8I3M7.json",
  "source_sha256": "574775c6d804e30e776f29661e18531280dbca6553bdbb138d45bcd3288c2f30",
  "retrieved_utc": "2026-11-02T04:32:04.373002+00:00",
  "json_pointer": "/features/13",
  "excerpt": "{\"description\":\"Cytoplasmic\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":465},\"start\":{\"modifier\":\"EXACT\",\"value\":446}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C18

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I3M7.json)

```json
{
  "evidence_id": "C18",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q8I3M7.json",
  "source_sha256": "574775c6d804e30e776f29661e18531280dbca6553bdbb138d45bcd3288c2f30",
  "retrieved_utc": "2026-11-02T04:32:04.373002+00:00",
  "json_pointer": "/features/14",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":487},\"start\":{\"modifier\":\"EXACT\",\"value\":466}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C19

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I3M7.json)

```json
{
  "evidence_id": "C19",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q8I3M7.json",
  "source_sha256": "574775c6d804e30e776f29661e18531280dbca6553bdbb138d45bcd3288c2f30",
  "retrieved_utc": "2026-11-02T04:32:04.373002+00:00",
  "json_pointer": "/features/15",
  "excerpt": "{\"description\":\"Vacuolar\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":515},\"start\":{\"modifier\":\"EXACT\",\"value\":488}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C20

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I3M7.json)

```json
{
  "evidence_id": "C20",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q8I3M7.json",
  "source_sha256": "574775c6d804e30e776f29661e18531280dbca6553bdbb138d45bcd3288c2f30",
  "retrieved_utc": "2026-11-02T04:32:04.373002+00:00",
  "json_pointer": "/features/16",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":534},\"start\":{\"modifier\":\"EXACT\",\"value\":516}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C21

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I3M7.json)

```json
{
  "evidence_id": "C21",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q8I3M7.json",
  "source_sha256": "574775c6d804e30e776f29661e18531280dbca6553bdbb138d45bcd3288c2f30",
  "retrieved_utc": "2026-11-02T04:32:04.373002+00:00",
  "json_pointer": "/features/17",
  "excerpt": "{\"description\":\"Cytoplasmic\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":554},\"start\":{\"modifier\":\"EXACT\",\"value\":535}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C22

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I3M7.json)

```json
{
  "evidence_id": "C22",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q8I3M7.json",
  "source_sha256": "574775c6d804e30e776f29661e18531280dbca6553bdbb138d45bcd3288c2f30",
  "retrieved_utc": "2026-11-02T04:32:04.373002+00:00",
  "json_pointer": "/features/18",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":573},\"start\":{\"modifier\":\"EXACT\",\"value\":555}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C23

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I3M7.json)

```json
{
  "evidence_id": "C23",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q8I3M7.json",
  "source_sha256": "574775c6d804e30e776f29661e18531280dbca6553bdbb138d45bcd3288c2f30",
  "retrieved_utc": "2026-11-02T04:32:04.373002+00:00",
  "json_pointer": "/features/19",
  "excerpt": "{\"description\":\"Vacuolar\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":584},\"start\":{\"modifier\":\"EXACT\",\"value\":574}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C24

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I3M7.json)

```json
{
  "evidence_id": "C24",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q8I3M7.json",
  "source_sha256": "574775c6d804e30e776f29661e18531280dbca6553bdbb138d45bcd3288c2f30",
  "retrieved_utc": "2026-11-02T04:32:04.373002+00:00",
  "json_pointer": "/features/20",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":603},\"start\":{\"modifier\":\"EXACT\",\"value\":585}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C25

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I3M7.json)

```json
{
  "evidence_id": "C25",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q8I3M7.json",
  "source_sha256": "574775c6d804e30e776f29661e18531280dbca6553bdbb138d45bcd3288c2f30",
  "retrieved_utc": "2026-11-02T04:32:04.373002+00:00",
  "json_pointer": "/features/21",
  "excerpt": "{\"description\":\"Cytoplasmic\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":622},\"start\":{\"modifier\":\"EXACT\",\"value\":604}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C26

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I3M7.json)

```json
{
  "evidence_id": "C26",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q8I3M7.json",
  "source_sha256": "574775c6d804e30e776f29661e18531280dbca6553bdbb138d45bcd3288c2f30",
  "retrieved_utc": "2026-11-02T04:32:04.373002+00:00",
  "json_pointer": "/features/22",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":645},\"start\":{\"modifier\":\"EXACT\",\"value\":623}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C27

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I3M7.json)

```json
{
  "evidence_id": "C27",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q8I3M7.json",
  "source_sha256": "574775c6d804e30e776f29661e18531280dbca6553bdbb138d45bcd3288c2f30",
  "retrieved_utc": "2026-11-02T04:32:04.373002+00:00",
  "json_pointer": "/features/23",
  "excerpt": "{\"description\":\"Vacuolar\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":650},\"start\":{\"modifier\":\"EXACT\",\"value\":646}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C28

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I3M7.json)

```json
{
  "evidence_id": "C28",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q8I3M7.json",
  "source_sha256": "574775c6d804e30e776f29661e18531280dbca6553bdbb138d45bcd3288c2f30",
  "retrieved_utc": "2026-11-02T04:32:04.373002+00:00",
  "json_pointer": "/features/24",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":673},\"start\":{\"modifier\":\"EXACT\",\"value\":651}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C29

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I3M7.json)

```json
{
  "evidence_id": "C29",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q8I3M7.json",
  "source_sha256": "574775c6d804e30e776f29661e18531280dbca6553bdbb138d45bcd3288c2f30",
  "retrieved_utc": "2026-11-02T04:32:04.373002+00:00",
  "json_pointer": "/features/25",
  "excerpt": "{\"description\":\"Cytoplasmic\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39467134\",\"source\":\"PubMed\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":684},\"start\":{\"modifier\":\"EXACT\",\"value\":674}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C30

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I3M7.json)

```json
{
  "evidence_id": "C30",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q8I3M7.json",
  "source_sha256": "574775c6d804e30e776f29661e18531280dbca6553bdbb138d45bcd3288c2f30",
  "retrieved_utc": "2026-11-02T04:32:04.373002+00:00",
  "json_pointer": "/references/2",
  "excerpt": "{\"citation\":{\"authors\":[\"Wichers J.S.\",\"Mesen-Ramirez P.\",\"Fuchs G.\",\"Yu-Strzelczyk J.\",\"Staecker J.\",\"von Thien H.\",\"Alder A.\",\"Henshall I.\",\"Liffner B.\",\"Nagel G.\",\"Loew C.\",\"Wilson D.\",\"Spielmann T.\",\"Gao S.\",\"Gilberger T.W.\",\"Bachmann A.\",\"Strauss J.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"35404116\"},{\"database\":\"DOI\",\"id\":\"10.1128/mbio.00623-22\"}],\"citationType\":\"journal article\",\"firstPage\":\"e0062322\",\"id\":\"35404116\",\"journal\":\"MBio\",\"lastPage\":\"e0062322\",\"publicationDate\":\"2022\",\"title\":\"PMRT1, a Plasmodium-Specific Parasite Plasma Membrane Transporter, Is Essential for Asexual and Sexual Blood Stage Development.\",\"volume\":\"13\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":3,\"referencePositions\":[\"SUBCELLULAR LOCATION\",\"DEVELOPMENTAL STAGE\",\"DISRUPTION PHENOTYPE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C31

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I3M7.json)

```json
{
  "evidence_id": "C31",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q8I3M7.json",
  "source_sha256": "574775c6d804e30e776f29661e18531280dbca6553bdbb138d45bcd3288c2f30",
  "retrieved_utc": "2026-11-02T04:32:04.373002+00:00",
  "json_pointer": "/references/3",
  "excerpt": "{\"citation\":{\"authors\":[\"Wunderlich J.\",\"Kotov V.\",\"Votborg-Novel L.\",\"Ntalla C.\",\"Geffken M.\",\"Peine S.\",\"Portugal S.\",\"Strauss J.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"39575308\"},{\"database\":\"DOI\",\"id\":\"10.3389/fcimb.2024.1480076\"}],\"citationType\":\"journal article\",\"firstPage\":\"1480076\",\"id\":\"39575308\",\"journal\":\"Front. Cell. Infect. Microbiol.\",\"lastPage\":\"1480076\",\"publicationDate\":\"2024\",\"title\":\"Iron transport pathways in the human malaria parasite Plasmodium falciparum revealed by RNA-sequencing.\",\"volume\":\"14\"},\"referenceNumber\":4,\"referencePositions\":[\"INDUCTION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C32

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I3M7.json)

```json
{
  "evidence_id": "C32",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q8I3M7.json",
  "source_sha256": "574775c6d804e30e776f29661e18531280dbca6553bdbb138d45bcd3288c2f30",
  "retrieved_utc": "2026-11-02T04:32:04.373002+00:00",
  "json_pointer": "/references/4",
  "excerpt": "{\"citation\":{\"authors\":[\"Loveridge K.M.\",\"Sigala P.A.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"39467134\"},{\"database\":\"DOI\",\"id\":\"10.1073/pnas.2411631121\"}],\"citationType\":\"journal article\",\"firstPage\":\"e2411631121\",\"id\":\"39467134\",\"journal\":\"Proc. Natl. Acad. Sci. U.S.A.\",\"lastPage\":\"e2411631121\",\"publicationDate\":\"2024\",\"title\":\"Identification of a divalent metal transporter required for cellular iron metabolism in malaria parasites.\",\"volume\":\"121\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":5,\"referencePositions\":[\"FUNCTION\",\"SUBCELLULAR LOCATION\",\"DISRUPTION PHENOTYPE\",\"TOPOLOGY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I3M7?format=txt&versions=117)

```json
{
  "evidence_id": "H1",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q8I3M7?format=txt&versions=117",
  "source_sha256": "75db2a237303bdcca1e3dff1a43527aaee7cf8b65d99a684cef3447701a84319",
  "retrieved_utc": "2026-11-02T04:32:12.059738+00:00",
  "source_locator": "lines 1-16",
  "excerpt": "ID   DMT1_PLAF7              Reviewed;         684 AA.\nAC   Q8I3M7;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   01-MAR-2003, sequence version 1.\nDT   28-JAN-2026, entry version 117.\nDE   RecName: Full=Divalent metal transporter 1 {ECO:0000303|PubMed:39467134};\nDE            Short=DMT1 {ECO:0000303|PubMed:39467134};\nDE            Short=PfDMT1 {ECO:0000303|PubMed:39467134, ECO:0000303|PubMed:39575308};\nDE   AltName: Full=Food vacuole resident transporter 1 {ECO:0000303|PubMed:35404116};\nDE   AltName: Full=PfNRAMP {ECO:0000303|PubMed:39575308};\nGN   Name=FVRT1 {ECO:0000303|PubMed:35404116};\nGN   ORFNames=PF3D7_0523800 {ECO:0000312|EMBL:CAD51601.1};\nOS   Plasmodium falciparum (isolate 3D7).\nOC   Eukaryota; Sar; Alveolata; Apicomplexa; Aconoidasida; Haemosporida;\nOC   Plasmodiidae; Plasmodium; Plasmodium (Laverania).\nOX   NCBI_TaxID=36329 {ECO:0000312|Proteomes:UP000001450};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 117,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I3M7?format=txt&versions=117)

```json
{
  "evidence_id": "H2",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q8I3M7?format=txt&versions=117",
  "source_sha256": "75db2a237303bdcca1e3dff1a43527aaee7cf8b65d99a684cef3447701a84319",
  "retrieved_utc": "2026-11-02T04:32:12.059738+00:00",
  "source_locator": "lines 51-59",
  "excerpt": "RN   [3] {ECO:0000305}\nRP   SUBCELLULAR LOCATION, DEVELOPMENTAL STAGE, AND DISRUPTION PHENOTYPE.\nRX   PubMed=35404116; DOI=10.1128/mbio.00623-22;\nRA   Wichers J.S., Mesen-Ramirez P., Fuchs G., Yu-Strzelczyk J., Staecker J.,\nRA   von Thien H., Alder A., Henshall I., Liffner B., Nagel G., Loew C.,\nRA   Wilson D., Spielmann T., Gao S., Gilberger T.W., Bachmann A., Strauss J.;\nRT   \"PMRT1, a Plasmodium-Specific Parasite Plasma Membrane Transporter, Is\nRT   Essential for Asexual and Sexual Blood Stage Development.\";\nRL   MBio 13:e0062322-e0062322(2022).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 117,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I3M7?format=txt&versions=117)

```json
{
  "evidence_id": "H3",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q8I3M7?format=txt&versions=117",
  "source_sha256": "75db2a237303bdcca1e3dff1a43527aaee7cf8b65d99a684cef3447701a84319",
  "retrieved_utc": "2026-11-02T04:32:12.059738+00:00",
  "source_locator": "lines 60-67",
  "excerpt": "RN   [4]\nRP   INDUCTION.\nRX   PubMed=39575308; DOI=10.3389/fcimb.2024.1480076;\nRA   Wunderlich J., Kotov V., Votborg-Novel L., Ntalla C., Geffken M., Peine S.,\nRA   Portugal S., Strauss J.;\nRT   \"Iron transport pathways in the human malaria parasite Plasmodium\nRT   falciparum revealed by RNA-sequencing.\";\nRL   Front. Cell. Infect. Microbiol. 14:1480076-1480076(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 117,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I3M7?format=txt&versions=117)

```json
{
  "evidence_id": "H4",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q8I3M7?format=txt&versions=117",
  "source_sha256": "75db2a237303bdcca1e3dff1a43527aaee7cf8b65d99a684cef3447701a84319",
  "retrieved_utc": "2026-11-02T04:32:12.059738+00:00",
  "source_locator": "lines 68-74",
  "excerpt": "RN   [5] {ECO:0000305}\nRP   FUNCTION, SUBCELLULAR LOCATION, DISRUPTION PHENOTYPE, AND TOPOLOGY.\nRX   PubMed=39467134; DOI=10.1073/pnas.2411631121;\nRA   Loveridge K.M., Sigala P.A.;\nRT   \"Identification of a divalent metal transporter required for cellular iron\nRT   metabolism in malaria parasites.\";\nRL   Proc. Natl. Acad. Sci. U.S.A. 121:e2411631121-e2411631121(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 117,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I3M7?format=txt&versions=117)

```json
{
  "evidence_id": "H5",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q8I3M7?format=txt&versions=117",
  "source_sha256": "75db2a237303bdcca1e3dff1a43527aaee7cf8b65d99a684cef3447701a84319",
  "retrieved_utc": "2026-11-02T04:32:12.059738+00:00",
  "source_locator": "lines 150-152",
  "excerpt": "FT   TOPO_DOM        1..228\nFT                   /note=\"Cytoplasmic\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 117,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I3M7?format=txt&versions=117)

```json
{
  "evidence_id": "H6",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q8I3M7?format=txt&versions=117",
  "source_sha256": "75db2a237303bdcca1e3dff1a43527aaee7cf8b65d99a684cef3447701a84319",
  "retrieved_utc": "2026-11-02T04:32:12.059738+00:00",
  "source_locator": "lines 153-155",
  "excerpt": "FT   TRANSMEM        229..247\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 117,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I3M7?format=txt&versions=117)

```json
{
  "evidence_id": "H7",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q8I3M7?format=txt&versions=117",
  "source_sha256": "75db2a237303bdcca1e3dff1a43527aaee7cf8b65d99a684cef3447701a84319",
  "retrieved_utc": "2026-11-02T04:32:12.059738+00:00",
  "source_locator": "lines 156-158",
  "excerpt": "FT   TOPO_DOM        248..275\nFT                   /note=\"Vacuolar\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 117,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I3M7?format=txt&versions=117)

```json
{
  "evidence_id": "H8",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q8I3M7?format=txt&versions=117",
  "source_sha256": "75db2a237303bdcca1e3dff1a43527aaee7cf8b65d99a684cef3447701a84319",
  "retrieved_utc": "2026-11-02T04:32:12.059738+00:00",
  "source_locator": "lines 159-161",
  "excerpt": "FT   TRANSMEM        276..299\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 117,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I3M7?format=txt&versions=117)

```json
{
  "evidence_id": "H9",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q8I3M7?format=txt&versions=117",
  "source_sha256": "75db2a237303bdcca1e3dff1a43527aaee7cf8b65d99a684cef3447701a84319",
  "retrieved_utc": "2026-11-02T04:32:12.059738+00:00",
  "source_locator": "lines 162-164",
  "excerpt": "FT   TOPO_DOM        300..319\nFT                   /note=\"Cytoplasmic\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 117,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H10

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I3M7?format=txt&versions=117)

```json
{
  "evidence_id": "H10",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q8I3M7?format=txt&versions=117",
  "source_sha256": "75db2a237303bdcca1e3dff1a43527aaee7cf8b65d99a684cef3447701a84319",
  "retrieved_utc": "2026-11-02T04:32:12.059738+00:00",
  "source_locator": "lines 165-167",
  "excerpt": "FT   TRANSMEM        320..345\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 117,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H11

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I3M7?format=txt&versions=117)

```json
{
  "evidence_id": "H11",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q8I3M7?format=txt&versions=117",
  "source_sha256": "75db2a237303bdcca1e3dff1a43527aaee7cf8b65d99a684cef3447701a84319",
  "retrieved_utc": "2026-11-02T04:32:12.059738+00:00",
  "source_locator": "lines 168-170",
  "excerpt": "FT   TOPO_DOM        346..350\nFT                   /note=\"Vacuolar\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 117,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H12

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I3M7?format=txt&versions=117)

```json
{
  "evidence_id": "H12",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q8I3M7?format=txt&versions=117",
  "source_sha256": "75db2a237303bdcca1e3dff1a43527aaee7cf8b65d99a684cef3447701a84319",
  "retrieved_utc": "2026-11-02T04:32:12.059738+00:00",
  "source_locator": "lines 171-173",
  "excerpt": "FT   TRANSMEM        351..370\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 117,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H13

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I3M7?format=txt&versions=117)

```json
{
  "evidence_id": "H13",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q8I3M7?format=txt&versions=117",
  "source_sha256": "75db2a237303bdcca1e3dff1a43527aaee7cf8b65d99a684cef3447701a84319",
  "retrieved_utc": "2026-11-02T04:32:12.059738+00:00",
  "source_locator": "lines 174-176",
  "excerpt": "FT   TOPO_DOM        371..381\nFT                   /note=\"Cytoplasmic\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 117,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H14

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I3M7?format=txt&versions=117)

```json
{
  "evidence_id": "H14",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q8I3M7?format=txt&versions=117",
  "source_sha256": "75db2a237303bdcca1e3dff1a43527aaee7cf8b65d99a684cef3447701a84319",
  "retrieved_utc": "2026-11-02T04:32:12.059738+00:00",
  "source_locator": "lines 177-179",
  "excerpt": "FT   TRANSMEM        382..404\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 117,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H15

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I3M7?format=txt&versions=117)

```json
{
  "evidence_id": "H15",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q8I3M7?format=txt&versions=117",
  "source_sha256": "75db2a237303bdcca1e3dff1a43527aaee7cf8b65d99a684cef3447701a84319",
  "retrieved_utc": "2026-11-02T04:32:12.059738+00:00",
  "source_locator": "lines 180-182",
  "excerpt": "FT   TOPO_DOM        405..423\nFT                   /note=\"Vacuolar\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 117,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H16

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I3M7?format=txt&versions=117)

```json
{
  "evidence_id": "H16",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q8I3M7?format=txt&versions=117",
  "source_sha256": "75db2a237303bdcca1e3dff1a43527aaee7cf8b65d99a684cef3447701a84319",
  "retrieved_utc": "2026-11-02T04:32:12.059738+00:00",
  "source_locator": "lines 183-185",
  "excerpt": "FT   TRANSMEM        424..445\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 117,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H17

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I3M7?format=txt&versions=117)

```json
{
  "evidence_id": "H17",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q8I3M7?format=txt&versions=117",
  "source_sha256": "75db2a237303bdcca1e3dff1a43527aaee7cf8b65d99a684cef3447701a84319",
  "retrieved_utc": "2026-11-02T04:32:12.059738+00:00",
  "source_locator": "lines 186-188",
  "excerpt": "FT   TOPO_DOM        446..465\nFT                   /note=\"Cytoplasmic\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 117,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H18

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I3M7?format=txt&versions=117)

```json
{
  "evidence_id": "H18",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q8I3M7?format=txt&versions=117",
  "source_sha256": "75db2a237303bdcca1e3dff1a43527aaee7cf8b65d99a684cef3447701a84319",
  "retrieved_utc": "2026-11-02T04:32:12.059738+00:00",
  "source_locator": "lines 189-191",
  "excerpt": "FT   TRANSMEM        466..487\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 117,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H19

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I3M7?format=txt&versions=117)

```json
{
  "evidence_id": "H19",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q8I3M7?format=txt&versions=117",
  "source_sha256": "75db2a237303bdcca1e3dff1a43527aaee7cf8b65d99a684cef3447701a84319",
  "retrieved_utc": "2026-11-02T04:32:12.059738+00:00",
  "source_locator": "lines 192-194",
  "excerpt": "FT   TOPO_DOM        488..515\nFT                   /note=\"Vacuolar\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 117,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H20

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I3M7?format=txt&versions=117)

```json
{
  "evidence_id": "H20",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q8I3M7?format=txt&versions=117",
  "source_sha256": "75db2a237303bdcca1e3dff1a43527aaee7cf8b65d99a684cef3447701a84319",
  "retrieved_utc": "2026-11-02T04:32:12.059738+00:00",
  "source_locator": "lines 195-197",
  "excerpt": "FT   TRANSMEM        516..534\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 117,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H21

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I3M7?format=txt&versions=117)

```json
{
  "evidence_id": "H21",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q8I3M7?format=txt&versions=117",
  "source_sha256": "75db2a237303bdcca1e3dff1a43527aaee7cf8b65d99a684cef3447701a84319",
  "retrieved_utc": "2026-11-02T04:32:12.059738+00:00",
  "source_locator": "lines 198-200",
  "excerpt": "FT   TOPO_DOM        535..554\nFT                   /note=\"Cytoplasmic\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 117,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H22

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I3M7?format=txt&versions=117)

```json
{
  "evidence_id": "H22",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q8I3M7?format=txt&versions=117",
  "source_sha256": "75db2a237303bdcca1e3dff1a43527aaee7cf8b65d99a684cef3447701a84319",
  "retrieved_utc": "2026-11-02T04:32:12.059738+00:00",
  "source_locator": "lines 201-203",
  "excerpt": "FT   TRANSMEM        555..573\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 117,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H23

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I3M7?format=txt&versions=117)

```json
{
  "evidence_id": "H23",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q8I3M7?format=txt&versions=117",
  "source_sha256": "75db2a237303bdcca1e3dff1a43527aaee7cf8b65d99a684cef3447701a84319",
  "retrieved_utc": "2026-11-02T04:32:12.059738+00:00",
  "source_locator": "lines 204-206",
  "excerpt": "FT   TOPO_DOM        574..584\nFT                   /note=\"Vacuolar\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 117,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H24

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I3M7?format=txt&versions=117)

```json
{
  "evidence_id": "H24",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q8I3M7?format=txt&versions=117",
  "source_sha256": "75db2a237303bdcca1e3dff1a43527aaee7cf8b65d99a684cef3447701a84319",
  "retrieved_utc": "2026-11-02T04:32:12.059738+00:00",
  "source_locator": "lines 207-209",
  "excerpt": "FT   TRANSMEM        585..603\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 117,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H25

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I3M7?format=txt&versions=117)

```json
{
  "evidence_id": "H25",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q8I3M7?format=txt&versions=117",
  "source_sha256": "75db2a237303bdcca1e3dff1a43527aaee7cf8b65d99a684cef3447701a84319",
  "retrieved_utc": "2026-11-02T04:32:12.059738+00:00",
  "source_locator": "lines 210-212",
  "excerpt": "FT   TOPO_DOM        604..622\nFT                   /note=\"Cytoplasmic\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 117,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H26

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I3M7?format=txt&versions=117)

```json
{
  "evidence_id": "H26",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q8I3M7?format=txt&versions=117",
  "source_sha256": "75db2a237303bdcca1e3dff1a43527aaee7cf8b65d99a684cef3447701a84319",
  "retrieved_utc": "2026-11-02T04:32:12.059738+00:00",
  "source_locator": "lines 213-215",
  "excerpt": "FT   TRANSMEM        623..645\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 117,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H27

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I3M7?format=txt&versions=117)

```json
{
  "evidence_id": "H27",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q8I3M7?format=txt&versions=117",
  "source_sha256": "75db2a237303bdcca1e3dff1a43527aaee7cf8b65d99a684cef3447701a84319",
  "retrieved_utc": "2026-11-02T04:32:12.059738+00:00",
  "source_locator": "lines 216-218",
  "excerpt": "FT   TOPO_DOM        646..650\nFT                   /note=\"Vacuolar\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 117,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H28

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I3M7?format=txt&versions=117)

```json
{
  "evidence_id": "H28",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q8I3M7?format=txt&versions=117",
  "source_sha256": "75db2a237303bdcca1e3dff1a43527aaee7cf8b65d99a684cef3447701a84319",
  "retrieved_utc": "2026-11-02T04:32:12.059738+00:00",
  "source_locator": "lines 219-221",
  "excerpt": "FT   TRANSMEM        651..673\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 117,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H29

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I3M7?format=txt&versions=117)

```json
{
  "evidence_id": "H29",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q8I3M7?format=txt&versions=117",
  "source_sha256": "75db2a237303bdcca1e3dff1a43527aaee7cf8b65d99a684cef3447701a84319",
  "retrieved_utc": "2026-11-02T04:32:12.059738+00:00",
  "source_locator": "lines 222-224",
  "excerpt": "FT   TOPO_DOM        674..684\nFT                   /note=\"Cytoplasmic\"\nFT                   /evidence=\"ECO:0000269|PubMed:39467134\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 117,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json), zero-based source row 107. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
