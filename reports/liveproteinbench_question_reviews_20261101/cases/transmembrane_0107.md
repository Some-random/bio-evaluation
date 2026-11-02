# transmembrane_0107

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `transmembrane`  
**Author expected answer:** **D** — 229..247; 276..299; 320..345; 351..370; 382..404; 424..445; 466..487; 516..534; 555..573; 585..603; 623..645; 651..673

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

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
<summary>Original system instructions, verbatim</summary>

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

## GPT-6 Luna

**Saved status:** `valid_review`.

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

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

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

## Existing project source checks of Luna’s review

The notes below were prepared for specific claims in the Luna review. They are not independent validation of Qwen’s claims, expert adjudication, or replacement verdicts.

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

## Reviewer-only source evidence

**Both reviewers received this source evidence separately from the original question. It was not available to the original evaluated model.** Source support and reasoning from the original sequence/choices are distinct assessments.

**Accession:** `Q8I3M7` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 117. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I3M7.json)  
**Locator:** `/features/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:04.373002+00:00.  

```json
{"description":"Cytoplasmic","evidences":[{"evidenceCode":"ECO:0000305"}],"location":{"end":{"modifier":"EXACT","value":228},"start":{"modifier":"EXACT","value":1}},"type":"Topological domain"}
```

Source SHA-256: `574775c6d804e30e776f29661e18531280dbca6553bdbb138d45bcd3288c2f30`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I3M7.json)  
**Locator:** `/features/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:04.373002+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":247},"start":{"modifier":"EXACT","value":229}},"type":"Transmembrane"}
```

Source SHA-256: `574775c6d804e30e776f29661e18531280dbca6553bdbb138d45bcd3288c2f30`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I3M7.json)  
**Locator:** `/features/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:04.373002+00:00.  

```json
{"description":"Vacuolar","evidences":[{"evidenceCode":"ECO:0000305"}],"location":{"end":{"modifier":"EXACT","value":275},"start":{"modifier":"EXACT","value":248}},"type":"Topological domain"}
```

Source SHA-256: `574775c6d804e30e776f29661e18531280dbca6553bdbb138d45bcd3288c2f30`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I3M7.json)  
**Locator:** `/features/4`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:04.373002+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":299},"start":{"modifier":"EXACT","value":276}},"type":"Transmembrane"}
```

Source SHA-256: `574775c6d804e30e776f29661e18531280dbca6553bdbb138d45bcd3288c2f30`.

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I3M7.json)  
**Locator:** `/features/5`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:04.373002+00:00.  

```json
{"description":"Cytoplasmic","evidences":[{"evidenceCode":"ECO:0000305"}],"location":{"end":{"modifier":"EXACT","value":319},"start":{"modifier":"EXACT","value":300}},"type":"Topological domain"}
```

Source SHA-256: `574775c6d804e30e776f29661e18531280dbca6553bdbb138d45bcd3288c2f30`.

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I3M7.json)  
**Locator:** `/features/6`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:04.373002+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":345},"start":{"modifier":"EXACT","value":320}},"type":"Transmembrane"}
```

Source SHA-256: `574775c6d804e30e776f29661e18531280dbca6553bdbb138d45bcd3288c2f30`.

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I3M7.json)  
**Locator:** `/features/7`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:04.373002+00:00.  

```json
{"description":"Vacuolar","evidences":[{"evidenceCode":"ECO:0000305"}],"location":{"end":{"modifier":"EXACT","value":350},"start":{"modifier":"EXACT","value":346}},"type":"Topological domain"}
```

Source SHA-256: `574775c6d804e30e776f29661e18531280dbca6553bdbb138d45bcd3288c2f30`.

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I3M7.json)  
**Locator:** `/features/8`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:04.373002+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":370},"start":{"modifier":"EXACT","value":351}},"type":"Transmembrane"}
```

Source SHA-256: `574775c6d804e30e776f29661e18531280dbca6553bdbb138d45bcd3288c2f30`.

### Evidence C13

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I3M7.json)  
**Locator:** `/features/9`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:04.373002+00:00.  

```json
{"description":"Cytoplasmic","evidences":[{"evidenceCode":"ECO:0000305"}],"location":{"end":{"modifier":"EXACT","value":381},"start":{"modifier":"EXACT","value":371}},"type":"Topological domain"}
```

Source SHA-256: `574775c6d804e30e776f29661e18531280dbca6553bdbb138d45bcd3288c2f30`.

### Evidence C14

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I3M7.json)  
**Locator:** `/features/10`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:04.373002+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":404},"start":{"modifier":"EXACT","value":382}},"type":"Transmembrane"}
```

Source SHA-256: `574775c6d804e30e776f29661e18531280dbca6553bdbb138d45bcd3288c2f30`.

### Evidence C15

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I3M7.json)  
**Locator:** `/features/11`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:04.373002+00:00.  

```json
{"description":"Vacuolar","evidences":[{"evidenceCode":"ECO:0000305"}],"location":{"end":{"modifier":"EXACT","value":423},"start":{"modifier":"EXACT","value":405}},"type":"Topological domain"}
```

Source SHA-256: `574775c6d804e30e776f29661e18531280dbca6553bdbb138d45bcd3288c2f30`.

### Evidence C16

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I3M7.json)  
**Locator:** `/features/12`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:04.373002+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":445},"start":{"modifier":"EXACT","value":424}},"type":"Transmembrane"}
```

Source SHA-256: `574775c6d804e30e776f29661e18531280dbca6553bdbb138d45bcd3288c2f30`.

### Evidence C17

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I3M7.json)  
**Locator:** `/features/13`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:04.373002+00:00.  

```json
{"description":"Cytoplasmic","evidences":[{"evidenceCode":"ECO:0000305"}],"location":{"end":{"modifier":"EXACT","value":465},"start":{"modifier":"EXACT","value":446}},"type":"Topological domain"}
```

Source SHA-256: `574775c6d804e30e776f29661e18531280dbca6553bdbb138d45bcd3288c2f30`.

### Evidence C18

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I3M7.json)  
**Locator:** `/features/14`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:04.373002+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":487},"start":{"modifier":"EXACT","value":466}},"type":"Transmembrane"}
```

Source SHA-256: `574775c6d804e30e776f29661e18531280dbca6553bdbb138d45bcd3288c2f30`.

### Evidence C19

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I3M7.json)  
**Locator:** `/features/15`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:04.373002+00:00.  

```json
{"description":"Vacuolar","evidences":[{"evidenceCode":"ECO:0000305"}],"location":{"end":{"modifier":"EXACT","value":515},"start":{"modifier":"EXACT","value":488}},"type":"Topological domain"}
```

Source SHA-256: `574775c6d804e30e776f29661e18531280dbca6553bdbb138d45bcd3288c2f30`.

### Evidence C20

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I3M7.json)  
**Locator:** `/features/16`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:04.373002+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":534},"start":{"modifier":"EXACT","value":516}},"type":"Transmembrane"}
```

Source SHA-256: `574775c6d804e30e776f29661e18531280dbca6553bdbb138d45bcd3288c2f30`.

### Evidence C21

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I3M7.json)  
**Locator:** `/features/17`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:04.373002+00:00.  

```json
{"description":"Cytoplasmic","evidences":[{"evidenceCode":"ECO:0000305"}],"location":{"end":{"modifier":"EXACT","value":554},"start":{"modifier":"EXACT","value":535}},"type":"Topological domain"}
```

Source SHA-256: `574775c6d804e30e776f29661e18531280dbca6553bdbb138d45bcd3288c2f30`.

### Evidence C22

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I3M7.json)  
**Locator:** `/features/18`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:04.373002+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":573},"start":{"modifier":"EXACT","value":555}},"type":"Transmembrane"}
```

Source SHA-256: `574775c6d804e30e776f29661e18531280dbca6553bdbb138d45bcd3288c2f30`.

### Evidence C23

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I3M7.json)  
**Locator:** `/features/19`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:04.373002+00:00.  

```json
{"description":"Vacuolar","evidences":[{"evidenceCode":"ECO:0000305"}],"location":{"end":{"modifier":"EXACT","value":584},"start":{"modifier":"EXACT","value":574}},"type":"Topological domain"}
```

Source SHA-256: `574775c6d804e30e776f29661e18531280dbca6553bdbb138d45bcd3288c2f30`.

### Evidence C24

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I3M7.json)  
**Locator:** `/features/20`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:04.373002+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":603},"start":{"modifier":"EXACT","value":585}},"type":"Transmembrane"}
```

Source SHA-256: `574775c6d804e30e776f29661e18531280dbca6553bdbb138d45bcd3288c2f30`.

### Evidence C25

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I3M7.json)  
**Locator:** `/features/21`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:04.373002+00:00.  

```json
{"description":"Cytoplasmic","evidences":[{"evidenceCode":"ECO:0000305"}],"location":{"end":{"modifier":"EXACT","value":622},"start":{"modifier":"EXACT","value":604}},"type":"Topological domain"}
```

Source SHA-256: `574775c6d804e30e776f29661e18531280dbca6553bdbb138d45bcd3288c2f30`.

### Evidence C26

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I3M7.json)  
**Locator:** `/features/22`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:04.373002+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":645},"start":{"modifier":"EXACT","value":623}},"type":"Transmembrane"}
```

Source SHA-256: `574775c6d804e30e776f29661e18531280dbca6553bdbb138d45bcd3288c2f30`.

### Evidence C27

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I3M7.json)  
**Locator:** `/features/23`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:04.373002+00:00.  

```json
{"description":"Vacuolar","evidences":[{"evidenceCode":"ECO:0000305"}],"location":{"end":{"modifier":"EXACT","value":650},"start":{"modifier":"EXACT","value":646}},"type":"Topological domain"}
```

Source SHA-256: `574775c6d804e30e776f29661e18531280dbca6553bdbb138d45bcd3288c2f30`.

### Evidence C28

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I3M7.json)  
**Locator:** `/features/24`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:04.373002+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":673},"start":{"modifier":"EXACT","value":651}},"type":"Transmembrane"}
```

Source SHA-256: `574775c6d804e30e776f29661e18531280dbca6553bdbb138d45bcd3288c2f30`.

### Evidence C29

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I3M7.json)  
**Locator:** `/features/25`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:04.373002+00:00.  

```json
{"description":"Cytoplasmic","evidences":[{"evidenceCode":"ECO:0000269","id":"39467134","source":"PubMed"}],"location":{"end":{"modifier":"EXACT","value":684},"start":{"modifier":"EXACT","value":674}},"type":"Topological domain"}
```

Source SHA-256: `574775c6d804e30e776f29661e18531280dbca6553bdbb138d45bcd3288c2f30`.

### Evidence C32

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I3M7.json)  
**Locator:** `/references/4`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:04.373002+00:00.  

```json
{"citation":{"authors":["Loveridge K.M.","Sigala P.A."],"citationCrossReferences":[{"database":"PubMed","id":"39467134"},{"database":"DOI","id":"10.1073/pnas.2411631121"}],"citationType":"journal article","firstPage":"e2411631121","id":"39467134","journal":"Proc. Natl. Acad. Sci. U.S.A.","lastPage":"e2411631121","publicationDate":"2024","title":"Identification of a divalent metal transporter required for cellular iron metabolism in malaria parasites.","volume":"121"},"evidences":[{"evidenceCode":"ECO:0000305"}],"referenceNumber":5,"referencePositions":["FUNCTION","SUBCELLULAR LOCATION","DISRUPTION PHENOTYPE","TOPOLOGY"]}
```

Source SHA-256: `574775c6d804e30e776f29661e18531280dbca6553bdbb138d45bcd3288c2f30`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I3M7?format=txt&versions=117)  
**Locator:** `lines 68-74`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 117 / 1.  
**Retrieved:** 2026-11-02T04:32:12.059738+00:00.  

```text
RN   [5] {ECO:0000305}
RP   FUNCTION, SUBCELLULAR LOCATION, DISRUPTION PHENOTYPE, AND TOPOLOGY.
RX   PubMed=39467134; DOI=10.1073/pnas.2411631121;
RA   Loveridge K.M., Sigala P.A.;
RT   "Identification of a divalent metal transporter required for cellular iron
RT   metabolism in malaria parasites.";
RL   Proc. Natl. Acad. Sci. U.S.A. 121:e2411631121-e2411631121(2024).
```

Source SHA-256: `75db2a237303bdcca1e3dff1a43527aaee7cf8b65d99a684cef3447701a84319`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I3M7?format=txt&versions=117)  
**Locator:** `lines 150-152`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 117 / 1.  
**Retrieved:** 2026-11-02T04:32:12.059738+00:00.  

```text
FT   TOPO_DOM        1..228
FT                   /note="Cytoplasmic"
FT                   /evidence="ECO:0000305"
```

Source SHA-256: `75db2a237303bdcca1e3dff1a43527aaee7cf8b65d99a684cef3447701a84319`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I3M7?format=txt&versions=117)  
**Locator:** `lines 153-155`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 117 / 1.  
**Retrieved:** 2026-11-02T04:32:12.059738+00:00.  

```text
FT   TRANSMEM        229..247
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `75db2a237303bdcca1e3dff1a43527aaee7cf8b65d99a684cef3447701a84319`.

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I3M7?format=txt&versions=117)  
**Locator:** `lines 156-158`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 117 / 1.  
**Retrieved:** 2026-11-02T04:32:12.059738+00:00.  

```text
FT   TOPO_DOM        248..275
FT                   /note="Vacuolar"
FT                   /evidence="ECO:0000305"
```

Source SHA-256: `75db2a237303bdcca1e3dff1a43527aaee7cf8b65d99a684cef3447701a84319`.

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I3M7?format=txt&versions=117)  
**Locator:** `lines 159-161`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 117 / 1.  
**Retrieved:** 2026-11-02T04:32:12.059738+00:00.  

```text
FT   TRANSMEM        276..299
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `75db2a237303bdcca1e3dff1a43527aaee7cf8b65d99a684cef3447701a84319`.

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I3M7?format=txt&versions=117)  
**Locator:** `lines 162-164`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 117 / 1.  
**Retrieved:** 2026-11-02T04:32:12.059738+00:00.  

```text
FT   TOPO_DOM        300..319
FT                   /note="Cytoplasmic"
FT                   /evidence="ECO:0000305"
```

Source SHA-256: `75db2a237303bdcca1e3dff1a43527aaee7cf8b65d99a684cef3447701a84319`.

### Evidence H10

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I3M7?format=txt&versions=117)  
**Locator:** `lines 165-167`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 117 / 1.  
**Retrieved:** 2026-11-02T04:32:12.059738+00:00.  

```text
FT   TRANSMEM        320..345
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `75db2a237303bdcca1e3dff1a43527aaee7cf8b65d99a684cef3447701a84319`.

### Evidence H11

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I3M7?format=txt&versions=117)  
**Locator:** `lines 168-170`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 117 / 1.  
**Retrieved:** 2026-11-02T04:32:12.059738+00:00.  

```text
FT   TOPO_DOM        346..350
FT                   /note="Vacuolar"
FT                   /evidence="ECO:0000305"
```

Source SHA-256: `75db2a237303bdcca1e3dff1a43527aaee7cf8b65d99a684cef3447701a84319`.

### Evidence H12

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I3M7?format=txt&versions=117)  
**Locator:** `lines 171-173`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 117 / 1.  
**Retrieved:** 2026-11-02T04:32:12.059738+00:00.  

```text
FT   TRANSMEM        351..370
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `75db2a237303bdcca1e3dff1a43527aaee7cf8b65d99a684cef3447701a84319`.

### Evidence H13

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I3M7?format=txt&versions=117)  
**Locator:** `lines 174-176`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 117 / 1.  
**Retrieved:** 2026-11-02T04:32:12.059738+00:00.  

```text
FT   TOPO_DOM        371..381
FT                   /note="Cytoplasmic"
FT                   /evidence="ECO:0000305"
```

Source SHA-256: `75db2a237303bdcca1e3dff1a43527aaee7cf8b65d99a684cef3447701a84319`.

### Evidence H14

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I3M7?format=txt&versions=117)  
**Locator:** `lines 177-179`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 117 / 1.  
**Retrieved:** 2026-11-02T04:32:12.059738+00:00.  

```text
FT   TRANSMEM        382..404
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `75db2a237303bdcca1e3dff1a43527aaee7cf8b65d99a684cef3447701a84319`.

### Evidence H15

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I3M7?format=txt&versions=117)  
**Locator:** `lines 180-182`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 117 / 1.  
**Retrieved:** 2026-11-02T04:32:12.059738+00:00.  

```text
FT   TOPO_DOM        405..423
FT                   /note="Vacuolar"
FT                   /evidence="ECO:0000305"
```

Source SHA-256: `75db2a237303bdcca1e3dff1a43527aaee7cf8b65d99a684cef3447701a84319`.

### Evidence H16

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I3M7?format=txt&versions=117)  
**Locator:** `lines 183-185`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 117 / 1.  
**Retrieved:** 2026-11-02T04:32:12.059738+00:00.  

```text
FT   TRANSMEM        424..445
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `75db2a237303bdcca1e3dff1a43527aaee7cf8b65d99a684cef3447701a84319`.

### Evidence H17

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I3M7?format=txt&versions=117)  
**Locator:** `lines 186-188`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 117 / 1.  
**Retrieved:** 2026-11-02T04:32:12.059738+00:00.  

```text
FT   TOPO_DOM        446..465
FT                   /note="Cytoplasmic"
FT                   /evidence="ECO:0000305"
```

Source SHA-256: `75db2a237303bdcca1e3dff1a43527aaee7cf8b65d99a684cef3447701a84319`.

### Evidence H18

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I3M7?format=txt&versions=117)  
**Locator:** `lines 189-191`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 117 / 1.  
**Retrieved:** 2026-11-02T04:32:12.059738+00:00.  

```text
FT   TRANSMEM        466..487
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `75db2a237303bdcca1e3dff1a43527aaee7cf8b65d99a684cef3447701a84319`.

### Evidence H19

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I3M7?format=txt&versions=117)  
**Locator:** `lines 192-194`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 117 / 1.  
**Retrieved:** 2026-11-02T04:32:12.059738+00:00.  

```text
FT   TOPO_DOM        488..515
FT                   /note="Vacuolar"
FT                   /evidence="ECO:0000305"
```

Source SHA-256: `75db2a237303bdcca1e3dff1a43527aaee7cf8b65d99a684cef3447701a84319`.

### Evidence H20

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I3M7?format=txt&versions=117)  
**Locator:** `lines 195-197`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 117 / 1.  
**Retrieved:** 2026-11-02T04:32:12.059738+00:00.  

```text
FT   TRANSMEM        516..534
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `75db2a237303bdcca1e3dff1a43527aaee7cf8b65d99a684cef3447701a84319`.

### Evidence H21

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I3M7?format=txt&versions=117)  
**Locator:** `lines 198-200`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 117 / 1.  
**Retrieved:** 2026-11-02T04:32:12.059738+00:00.  

```text
FT   TOPO_DOM        535..554
FT                   /note="Cytoplasmic"
FT                   /evidence="ECO:0000305"
```

Source SHA-256: `75db2a237303bdcca1e3dff1a43527aaee7cf8b65d99a684cef3447701a84319`.

### Evidence H22

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I3M7?format=txt&versions=117)  
**Locator:** `lines 201-203`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 117 / 1.  
**Retrieved:** 2026-11-02T04:32:12.059738+00:00.  

```text
FT   TRANSMEM        555..573
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `75db2a237303bdcca1e3dff1a43527aaee7cf8b65d99a684cef3447701a84319`.

### Evidence H23

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I3M7?format=txt&versions=117)  
**Locator:** `lines 204-206`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 117 / 1.  
**Retrieved:** 2026-11-02T04:32:12.059738+00:00.  

```text
FT   TOPO_DOM        574..584
FT                   /note="Vacuolar"
FT                   /evidence="ECO:0000305"
```

Source SHA-256: `75db2a237303bdcca1e3dff1a43527aaee7cf8b65d99a684cef3447701a84319`.

### Evidence H24

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I3M7?format=txt&versions=117)  
**Locator:** `lines 207-209`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 117 / 1.  
**Retrieved:** 2026-11-02T04:32:12.059738+00:00.  

```text
FT   TRANSMEM        585..603
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `75db2a237303bdcca1e3dff1a43527aaee7cf8b65d99a684cef3447701a84319`.

### Evidence H25

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I3M7?format=txt&versions=117)  
**Locator:** `lines 210-212`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 117 / 1.  
**Retrieved:** 2026-11-02T04:32:12.059738+00:00.  

```text
FT   TOPO_DOM        604..622
FT                   /note="Cytoplasmic"
FT                   /evidence="ECO:0000305"
```

Source SHA-256: `75db2a237303bdcca1e3dff1a43527aaee7cf8b65d99a684cef3447701a84319`.

### Evidence H26

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I3M7?format=txt&versions=117)  
**Locator:** `lines 213-215`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 117 / 1.  
**Retrieved:** 2026-11-02T04:32:12.059738+00:00.  

```text
FT   TRANSMEM        623..645
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `75db2a237303bdcca1e3dff1a43527aaee7cf8b65d99a684cef3447701a84319`.

### Evidence H27

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I3M7?format=txt&versions=117)  
**Locator:** `lines 216-218`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 117 / 1.  
**Retrieved:** 2026-11-02T04:32:12.059738+00:00.  

```text
FT   TOPO_DOM        646..650
FT                   /note="Vacuolar"
FT                   /evidence="ECO:0000305"
```

Source SHA-256: `75db2a237303bdcca1e3dff1a43527aaee7cf8b65d99a684cef3447701a84319`.

### Evidence H28

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I3M7?format=txt&versions=117)  
**Locator:** `lines 219-221`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 117 / 1.  
**Retrieved:** 2026-11-02T04:32:12.059738+00:00.  

```text
FT   TRANSMEM        651..673
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `75db2a237303bdcca1e3dff1a43527aaee7cf8b65d99a684cef3447701a84319`.

### Evidence H29

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I3M7?format=txt&versions=117)  
**Locator:** `lines 222-224`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 117 / 1.  
**Retrieved:** 2026-11-02T04:32:12.059738+00:00.  

```text
FT   TOPO_DOM        674..684
FT                   /note="Cytoplasmic"
FT                   /evidence="ECO:0000269|PubMed:39467134"
```

Source SHA-256: `75db2a237303bdcca1e3dff1a43527aaee7cf8b65d99a684cef3447701a84319`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json), zero-based source row 107. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
