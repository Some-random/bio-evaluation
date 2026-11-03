# transmembrane_0117: before and after transfer clarification

[All 1,328 cases](../README.md) · [Method](../METHOD.md) · [Summary](../SUMMARY.md) · [Exact reviewer user message](../inputs/transmembrane_0117.txt)

**Task:** `transmembrane`  
**Author key, unchanged:** **B** — 31..51; 82..102; 112..132; 138..158; 179..199; 211..231; 353..373; 381..401; 409..429; 437..457; 478..498

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
MTTSSDSAMVNHTPSPWYKFGFKSFAEFNTYVTFVFLGMSIMMVASAVTSAPDFLTRYYVYATGDPDAVAETPLFWNNANTFYNAGTYVLQVLTELFSLTPFMRRIPLSVRLFVGLGIPFAELLLIIIVPAATIKSQHGAIAVIMVVACVGGFSKALCDSCTNALVGPFPTKFMNGAQWGLTVIALLMSIIQIILKVSMGTSFHDILTMSRIYFGICIGIQLFAIFELAILRFNPFAQKYIAEYRAGAQRNAQNNESTLEETAPSMNEPAAGDIADLPATVDDKERALNEEEGDEVRAVTSEEFHVKRGAVLTATGDADKMVDLDQTGNITSTEQLLRASAASVFKRVYPMLVCVFLIYFTSLLTFPGVFFLVSTTSGWYMTVIVTLFNAGDFISRMVLMFRPLRPSPKVVVAGTLGRLIIIPFLVLCVRGIIRGEALPYVLITLLGLTNGYFGCMACIHCPRTTTLRYAGERSLAAMLSGISIMLGLCFGSNLSLAITLTH

[Multiple Choices]
A. 61..81; 91..111; 169..189; 192..212; 276..296; 317..337; 789..809; 830..850; 908..928; 929..949; 1033..1053; 1058..1078
B. 31..51; 82..102; 112..132; 138..158; 179..199; 211..231; 353..373; 381..401; 409..429; 437..457; 478..498
C. 31..51; 82..102; 112..132; 138..158; 179..199; 211..231; 353..373; 381..401; 409..429; 437..457
D. 31..51; 82..102; 112..132; 138..158; 179..199; 211..231; 353..373; 384..405; 409..429; 437..457; 478..498
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

> The sequence matches the UniProt entry, whose annotated transmembrane regions match all 11 intervals in B. These span annotations are primarily computational (ECO:0000255), so they support the key as an annotation-based answer but are not, by themselves, experimental validation of every boundary.

Citations as saved: [C6](#evidence-c6), [C8](#evidence-c8), [C10](#evidence-c10), [C12](#evidence-c12), [C14](#evidence-c14), [C16](#evidence-c16), [C18](#evidence-c18), [C20](#evidence-c20), [C22](#evidence-c22), [C24](#evidence-c24), [C26](#evidence-c26).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence has multiple strongly hydrophobic stretches consistent with a multi-pass membrane protein, including the C-terminal region omitted by C. This supports the broad pattern of transmembrane helices, but does not reliably establish the exact listed boundaries.


**Missing item-specific fact**

> The precise annotated boundaries for this particular protein, especially the distinction between 381..401 and the closely overlapping 384..405 interval, are not supplied in the question.


**Reason**

> General sequence reasoning can identify likely membrane-spanning stretches, but the options require exact residue intervals. Choosing the keyed set depends on protein-specific boundary annotations or a sufficiently calibrated predictor, not merely on broad hydrophobicity reasoning.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "D"
]
```

> B matches the cited annotation. However, B's 381..401 and D's 384..405 intervals substantially overlap the same hydrophobic segment, and the question gives no boundary convention that would make such a small shift biologically unambiguous.


### Important caveats

- The reviewer-only database identity and annotations were not supplied to the evaluated model.
- Database transmembrane features here are computational annotations; the cited topology evidence does not independently establish every helix boundary experimentally.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has multiple strongly hydrophobic stretches consistent with a multi-pass membrane protein, including the C-terminal region omitted by C. This supports the broad pattern of transmembrane helices, but does not reliably establish the exact listed boundaries.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The precise annotated boundaries for this particular protein, especially the distinction between 381..401 and the closely overlapping 384..405 interval, are not supplied in the question.",
    "reason": "General sequence reasoning can identify likely membrane-spanning stretches, but the options require exact residue intervals. Choosing the keyed set depends on protein-specific boundary annotations or a sufficiently calibrated predictor, not merely on broad hydrophobicity reasoning."
  },
  "case_id": "transmembrane_0117",
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
      "C26"
    ],
    "judgment": "supported",
    "reason": "The sequence matches the UniProt entry, whose annotated transmembrane regions match all 11 intervals in B. These span annotations are primarily computational (ECO:0000255), so they support the key as an annotation-based answer but are not, by themselves, experimental validation of every boundary."
  },
  "important_caveats": [
    "The reviewer-only database identity and annotations were not supplied to the evaluated model.",
    "Database transmembrane features here are computational annotations; the cited topology evidence does not independently establish every helix boundary experimentally."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "D"
    ],
    "reason": "B matches the cited annotation. However, B's 381..401 and D's 384..405 intervals substantially overlap the same hydrophobic segment, and the question gives no boundary convention that would make such a small shift biologically unambiguous."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0117",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches the UniProt entry, whose annotated transmembrane regions match all 11 intervals in B. These span annotations are primarily computational (ECO:0000255), so they support the key as an annotation-based answer but are not, by themselves, experimental validation of every boundary.",
    "evidence_ids": ["C6", "C8", "C10", "C12", "C14", "C16", "C18", "C20", "C22", "C24", "C26"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence has multiple strongly hydrophobic stretches consistent with a multi-pass membrane protein, including the C-terminal region omitted by C. This supports the broad pattern of transmembrane helices, but does not reliably establish the exact listed boundaries.",
    "missing_item_specific_fact": "The precise annotated boundaries for this particular protein, especially the distinction between 381..401 and the closely overlapping 384..405 interval, are not supplied in the question.",
    "reason": "General sequence reasoning can identify likely membrane-spanning stretches, but the options require exact residue intervals. Choosing the keyed set depends on protein-specific boundary annotations or a sufficiently calibrated predictor, not merely on broad hydrophobicity reasoning."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "D"],
    "reason": "B matches the cited annotation. However, B's 381..401 and D's 384..405 intervals substantially overlap the same hydrophobic segment, and the question gives no boundary convention that would make such a small shift biologically unambiguous."
  },
  "important_caveats": [
    "The reviewer-only database identity and annotations were not supplied to the evaluated model.",
    "Database transmembrane features here are computational annotations; the cited topology evidence does not independently establish every helix boundary experimentally."
  ]
}
```

</details>

## Before: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry Q9GTP4 (Crithidia fasciculata Nucleoside transporter 2, CfNT2) annotates exactly 11 transmembrane helices at positions 31-51, 82-102, 112-132, 138-158, 179-199, 211-231, 353-373, 381-401, 409-429, 437-457, and 478-498, matching Choice B exactly. The sequence in the question (502 aa) matches the UniProt sequence (sha256 confirmed). TM boundaries carry evidence code ECO:0000255 (computational/PROSITE pattern-based prediction), while intervening topological domains are supported by experimental mutagenesis data (PubMed:20037157). The key is consistent with the database annotation.

Citations as saved: [C6](#evidence-c6), [C8](#evidence-c8), [C10](#evidence-c10), [C12](#evidence-c12), [C14](#evidence-c14), [C16](#evidence-c16), [C18](#evidence-c18), [C20](#evidence-c20), [C22](#evidence-c22), [C24](#evidence-c24), [C26](#evidence-c26), [H5](#evidence-h5), [H7](#evidence-h7), [H9](#evidence-h9), [H11](#evidence-h11), [H13](#evidence-h13), [H15](#evidence-h15), [H17](#evidence-h17), [H19](#evidence-h19), [H21](#evidence-h21), [H23](#evidence-h23), [H25](#evidence-h25).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> Choice A can be eliminated by noting positions 789, 830, 908, 929, 1033, 1058 exceed the 502-residue protein length. General ENT-family knowledge (equilibrative nucleoside transporters typically have 11 TM helices) could help eliminate Choice C (only 10 TMs). However, the critical B-vs-D distinction—whether TM8 spans 381-401 or 384-405 (a 3-residue shift)—cannot be resolved by general hydrophobicity reasoning; the region contains a mix of hydrophobic and polar residues whose exact helix boundaries depend on the specific prediction algorithm (PROSITE PS50250 pattern matching, ECO:0000255).


**Missing item-specific fact**

> The precise start/end coordinates of TM8 (381-401 vs 384-405) as determined by the specific computational prediction method used in the UniProt annotation. No general biological principle or simple hydrophobicity analysis distinguishes a 21-residue helix starting at 381 from one starting at 384 in this particular sequence context.


**Reason**

> While A is trivially eliminable and C is weakly eliminable via ENT-family topology knowledge, the decisive B-vs-D distinction requires knowledge of the exact algorithmic boundaries assigned to this protein's TM helices. This is an item-specific annotation fact, not derivable from general transmembrane biology.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "D"
]
```

> Both B and D contain 11 TM segments with nearly identical boundaries. The only difference is TM8 (381-401 in B vs 384-405 in D), a 3-residue shift that falls within the typical uncertainty of hydrophobicity-based TM prediction. Without access to the specific prediction algorithm's output, both boundaries are plausible for a helix in this region. The sequence in the 381-405 window contains sufficient hydrophobic character to support either boundary assignment.


### Important caveats

- All TM boundary annotations carry ECO:0000255 (computational prediction via PROSITE pattern), not experimental determination of helix boundaries. The experimental evidence (PubMed:20037157) supports the overall topology (number of TMs, inside/outside orientation) but not the exact residue-level start/end of each helix.
- Choice A is clearly invalid (positions exceed protein length), serving as an easy distractor.
- The UniProt entry was first released in 2025-02-05; the author's source snapshot is unknown, though the sequence has been unchanged since 2001-03-01.
- The ENT family generally has 11 TM helices, which provides weak reasoning support for choosing an 11-TM answer (B or D) over C (10 TMs).

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Choice A can be eliminated by noting positions 789, 830, 908, 929, 1033, 1058 exceed the 502-residue protein length. General ENT-family knowledge (equilibrative nucleoside transporters typically have 11 TM helices) could help eliminate Choice C (only 10 TMs). However, the critical B-vs-D distinction—whether TM8 spans 381-401 or 384-405 (a 3-residue shift)—cannot be resolved by general hydrophobicity reasoning; the region contains a mix of hydrophobic and polar residues whose exact helix boundaries depend on the specific prediction algorithm (PROSITE PS50250 pattern matching, ECO:0000255).",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The precise start/end coordinates of TM8 (381-401 vs 384-405) as determined by the specific computational prediction method used in the UniProt annotation. No general biological principle or simple hydrophobicity analysis distinguishes a 21-residue helix starting at 381 from one starting at 384 in this particular sequence context.",
    "reason": "While A is trivially eliminable and C is weakly eliminable via ENT-family topology knowledge, the decisive B-vs-D distinction requires knowledge of the exact algorithmic boundaries assigned to this protein's TM helices. This is an item-specific annotation fact, not derivable from general transmembrane biology."
  },
  "case_id": "transmembrane_0117",
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
      "H25"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry Q9GTP4 (Crithidia fasciculata Nucleoside transporter 2, CfNT2) annotates exactly 11 transmembrane helices at positions 31-51, 82-102, 112-132, 138-158, 179-199, 211-231, 353-373, 381-401, 409-429, 437-457, and 478-498, matching Choice B exactly. The sequence in the question (502 aa) matches the UniProt sequence (sha256 confirmed). TM boundaries carry evidence code ECO:0000255 (computational/PROSITE pattern-based prediction), while intervening topological domains are supported by experimental mutagenesis data (PubMed:20037157). The key is consistent with the database annotation."
  },
  "important_caveats": [
    "All TM boundary annotations carry ECO:0000255 (computational prediction via PROSITE pattern), not experimental determination of helix boundaries. The experimental evidence (PubMed:20037157) supports the overall topology (number of TMs, inside/outside orientation) but not the exact residue-level start/end of each helix.",
    "Choice A is clearly invalid (positions exceed protein length), serving as an easy distractor.",
    "The UniProt entry was first released in 2025-02-05; the author's source snapshot is unknown, though the sequence has been unchanged since 2001-03-01.",
    "The ENT family generally has 11 TM helices, which provides weak reasoning support for choosing an 11-TM answer (B or D) over C (10 TMs)."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "D"
    ],
    "reason": "Both B and D contain 11 TM segments with nearly identical boundaries. The only difference is TM8 (381-401 in B vs 384-405 in D), a 3-residue shift that falls within the typical uncertainty of hydrophobicity-based TM prediction. Without access to the specific prediction algorithm's output, both boundaries are plausible for a helix in this region. The sequence in the 381-405 window contains sufficient hydrophobic character to support either boundary assignment."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0117",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry Q9GTP4 (Crithidia fasciculata Nucleoside transporter 2, CfNT2) annotates exactly 11 transmembrane helices at positions 31-51, 82-102, 112-132, 138-158, 179-199, 211-231, 353-373, 381-401, 409-429, 437-457, and 478-498, matching Choice B exactly. The sequence in the question (502 aa) matches the UniProt sequence (sha256 confirmed). TM boundaries carry evidence code ECO:0000255 (computational/PROSITE pattern-based prediction), while intervening topological domains are supported by experimental mutagenesis data (PubMed:20037157). The key is consistent with the database annotation.",
    "evidence_ids": ["C6","C8","C10","C12","C14","C16","C18","C20","C22","C24","C26","H5","H7","H9","H11","H13","H15","H17","H19","H21","H23","H25"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "Choice A can be eliminated by noting positions 789, 830, 908, 929, 1033, 1058 exceed the 502-residue protein length. General ENT-family knowledge (equilibrative nucleoside transporters typically have 11 TM helices) could help eliminate Choice C (only 10 TMs). However, the critical B-vs-D distinction—whether TM8 spans 381-401 or 384-405 (a 3-residue shift)—cannot be resolved by general hydrophobicity reasoning; the region contains a mix of hydrophobic and polar residues whose exact helix boundaries depend on the specific prediction algorithm (PROSITE PS50250 pattern matching, ECO:0000255).",
    "missing_item_specific_fact": "The precise start/end coordinates of TM8 (381-401 vs 384-405) as determined by the specific computational prediction method used in the UniProt annotation. No general biological principle or simple hydrophobicity analysis distinguishes a 21-residue helix starting at 381 from one starting at 384 in this particular sequence context.",
    "reason": "While A is trivially eliminable and C is weakly eliminable via ENT-family topology knowledge, the decisive B-vs-D distinction requires knowledge of the exact algorithmic boundaries assigned to this protein's TM helices. This is an item-specific annotation fact, not derivable from general transmembrane biology."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "D"],
    "reason": "Both B and D contain 11 TM segments with nearly identical boundaries. The only difference is TM8 (381-401 in B vs 384-405 in D), a 3-residue shift that falls within the typical uncertainty of hydrophobicity-based TM prediction. Without access to the specific prediction algorithm's output, both boundaries are plausible for a helix in this region. The sequence in the 381-405 window contains sufficient hydrophobic character to support either boundary assignment."
  },
  "important_caveats": [
    "All TM boundary annotations carry ECO:0000255 (computational prediction via PROSITE pattern), not experimental determination of helix boundaries. The experimental evidence (PubMed:20037157) supports the overall topology (number of TMs, inside/outside orientation) but not the exact residue-level start/end of each helix.",
    "Choice A is clearly invalid (positions exceed protein length), serving as an easy distractor.",
    "The UniProt entry was first released in 2025-02-05; the author's source snapshot is unknown, though the sequence has been unchanged since 2001-03-01.",
    "The ENT family generally has 11 TM helices, which provides weak reasoning support for choosing an 11-TM answer (B or D) over C (10 TMs)."
  ]
}
```

</details>

## After: GPT-6 Luna

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence-matched UniProt record annotates all 11 segments in B as transmembrane helices. These are computational annotations (ECO:0000255), not direct experimental measurements of each boundary.

Citations as saved: [H5](#evidence-h5), [H7](#evidence-h7), [H9](#evidence-h9), [H11](#evidence-h11), [H13](#evidence-h13), [H15](#evidence-h15), [H17](#evidence-h17), [H19](#evidence-h19), [H21](#evidence-h21), [H23](#evidence-h23), [H25](#evidence-h25).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence has repeated hydrophobic stretches consistent with a multi-pass helical membrane protein, so transferable sequence and family-level knowledge supports the overall pattern in B and D and distinguishes them from less fitting choices. But B and D differ at one boundary within the same strongly hydrophobic stretch; that qualitative evidence does not reliably select the exact coordinates in B.


**Missing item-specific fact**

> The target-specific predicted boundary for the disputed helix, 381..401 rather than 384..405.


**Reason**

> Biological reasoning supports the membrane-spanning pattern, but the offered choices require distinguishing a small boundary shift that is not reliably resolved by the sequence's general hydrophobic pattern. Selecting B over D depends on the exact target-specific annotation or prediction.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "D"
]
```

> B and D agree on the other listed spans and place their differing ranges within the same hydrophobic stretch. The sequence supports a membrane helix there, but does not make the precise boundaries unambiguous.


### Important caveats

- The supplied sequence matches the reviewer-only source sequence; the exact author source snapshot is unknown.
- The source supports B as an annotation, but its transmembrane boundary evidence is computational rather than direct experimental evidence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has repeated hydrophobic stretches consistent with a multi-pass helical membrane protein, so transferable sequence and family-level knowledge supports the overall pattern in B and D and distinguishes them from less fitting choices. But B and D differ at one boundary within the same strongly hydrophobic stretch; that qualitative evidence does not reliably select the exact coordinates in B.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The target-specific predicted boundary for the disputed helix, 381..401 rather than 384..405.",
    "reason": "Biological reasoning supports the membrane-spanning pattern, but the offered choices require distinguishing a small boundary shift that is not reliably resolved by the sequence's general hydrophobic pattern. Selecting B over D depends on the exact target-specific annotation or prediction."
  },
  "case_id": "transmembrane_0117",
  "expected_answer_check": {
    "evidence_ids": [
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
      "H25"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates all 11 segments in B as transmembrane helices. These are computational annotations (ECO:0000255), not direct experimental measurements of each boundary."
  },
  "important_caveats": [
    "The supplied sequence matches the reviewer-only source sequence; the exact author source snapshot is unknown.",
    "The source supports B as an annotation, but its transmembrane boundary evidence is computational rather than direct experimental evidence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "D"
    ],
    "reason": "B and D agree on the other listed spans and place their differing ranges within the same hydrophobic stretch. The sequence supports a membrane helix there, but does not make the precise boundaries unambiguous."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0117",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates all 11 segments in B as transmembrane helices. These are computational annotations (ECO:0000255), not direct experimental measurements of each boundary.",
    "evidence_ids": ["H5", "H7", "H9", "H11", "H13", "H15", "H17", "H19", "H21", "H23", "H25"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence has repeated hydrophobic stretches consistent with a multi-pass helical membrane protein, so transferable sequence and family-level knowledge supports the overall pattern in B and D and distinguishes them from less fitting choices. But B and D differ at one boundary within the same strongly hydrophobic stretch; that qualitative evidence does not reliably select the exact coordinates in B.",
    "missing_item_specific_fact": "The target-specific predicted boundary for the disputed helix, 381..401 rather than 384..405.",
    "reason": "Biological reasoning supports the membrane-spanning pattern, but the offered choices require distinguishing a small boundary shift that is not reliably resolved by the sequence's general hydrophobic pattern. Selecting B over D depends on the exact target-specific annotation or prediction."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "D"],
    "reason": "B and D agree on the other listed spans and place their differing ranges within the same hydrophobic stretch. The sequence supports a membrane helix there, but does not make the precise boundaries unambiguous."
  },
  "important_caveats": [
    "The supplied sequence matches the reviewer-only source sequence; the exact author source snapshot is unknown.",
    "The source supports B as an annotation, but its transmembrane boundary evidence is computational rather than direct experimental evidence."
  ]
}
```

</details>

## After: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry Q9GTP4 (NT2_CRIFA, Crithidia fasciculata Nucleoside Transporter 2) annotates exactly 11 transmembrane helical regions at positions 31-51, 82-102, 112-132, 138-158, 179-199, 211-231, 353-373, 381-401, 409-429, 437-457, and 478-498, which matches option B precisely. The TM annotations carry evidence code ECO:0000255 (inferred by similarity), while the flanking topological domains are supported by experimental mutagenesis data (PubMed:20037157). The sequence is 502 AA, consistent with the benchmark input.

Citations as saved: [C6](#evidence-c6), [C8](#evidence-c8), [C10](#evidence-c10), [C12](#evidence-c12), [C14](#evidence-c14), [C16](#evidence-c16), [C18](#evidence-c18), [C20](#evidence-c20), [C22](#evidence-c22), [C24](#evidence-c24), [C26](#evidence-c26), [H5](#evidence-h5), [H7](#evidence-h7), [H9](#evidence-h9), [H11](#evidence-h11), [H13](#evidence-h13), [H15](#evidence-h15), [H17](#evidence-h17), [H19](#evidence-h19), [H21](#evidence-h21), [H23](#evidence-h23), [H25](#evidence-h25).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Option A is trivially eliminated because it references positions up to 1078, far exceeding the 502-residue protein. Option D differs from B by extending TM8 from 381-401 to 384-405; positions 402 (R) and 405 (R) are charged arginines embedded in what would be a membrane-spanning helix, which is energetically highly unfavorable—standard hydrophobicity principles (e.g., Kyte-Doolittle, Wimley-White) strongly disfavor placing Arg in the hydrophobic core of a lipid bilayer, favoring the shorter 381-401 boundary. Option C omits the 478-498 segment; scanning this region reveals a 21-residue predominantly hydrophobic stretch (MLS-GISIMLGLCFGSNLSLAI) with a hydrophobic moment consistent with a TM helix, and the flanking context (charged/polar residues at 458-477 on one side and only 4 short residues at 499-502 on the other) supports it as a membrane-spanning segment. Additionally, equilibrative nucleoside transporters (ENT family) canonically possess 11 TM helices, so recognizing the family-level topology would favor 11 TM regions (B) over 10 (C). Thus, hydrophobicity analysis and family-level topology knowledge meaningfully distinguish B from the alternatives.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A model can eliminate A by sequence length, distinguish D from B by identifying charged Arg residues in the proposed extension (402, 405), and identify the 478-498 hydrophobic segment as a TM region using standard hydrophobicity analysis. The ENT family's canonical 11-TM topology provides additional family-level support for B over C. These are transferable principles from membrane protein biology and do not require recalling this specific protein's database annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The charged-residue argument cleanly eliminates D relative to B. The hydrophobicity of 478-498, while containing some polar residues, is sufficiently hydrophobic (majority Leu, Ile, Met, Phe, Ala) to be identified as a TM candidate, and the ENT-family 11-TM topology supports its inclusion. No other option is defensible given these analyses.


### Important caveats

- The UniProt TM annotations carry evidence code ECO:0000255 (inferred by similarity), meaning exact boundaries are computational predictions rather than experimentally determined. The topological domain assignments, however, are supported by the 2010 mutagenesis study (PubMed:20037157).
- The exact residue-level boundaries (e.g., 381 vs 384) are prediction-dependent; a model's hydrophobicity window might shift by 1-2 residues. However, the offered choices differ by 3+ residues, making the charged-residue argument decisive.
- The model would not necessarily recognize the protein as an ENT family member from sequence alone, but hydrophobicity scanning of the full 502-residue sequence would independently identify the 478-498 segment as a TM candidate.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Option A is trivially eliminated because it references positions up to 1078, far exceeding the 502-residue protein. Option D differs from B by extending TM8 from 381-401 to 384-405; positions 402 (R) and 405 (R) are charged arginines embedded in what would be a membrane-spanning helix, which is energetically highly unfavorable—standard hydrophobicity principles (e.g., Kyte-Doolittle, Wimley-White) strongly disfavor placing Arg in the hydrophobic core of a lipid bilayer, favoring the shorter 381-401 boundary. Option C omits the 478-498 segment; scanning this region reveals a 21-residue predominantly hydrophobic stretch (MLS-GISIMLGLCFGSNLSLAI) with a hydrophobic moment consistent with a TM helix, and the flanking context (charged/polar residues at 458-477 on one side and only 4 short residues at 499-502 on the other) supports it as a membrane-spanning segment. Additionally, equilibrative nucleoside transporters (ENT family) canonically possess 11 TM helices, so recognizing the family-level topology would favor 11 TM regions (B) over 10 (C). Thus, hydrophobicity analysis and family-level topology knowledge meaningfully distinguish B from the alternatives.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A model can eliminate A by sequence length, distinguish D from B by identifying charged Arg residues in the proposed extension (402, 405), and identify the 478-498 hydrophobic segment as a TM region using standard hydrophobicity analysis. The ENT family's canonical 11-TM topology provides additional family-level support for B over C. These are transferable principles from membrane protein biology and do not require recalling this specific protein's database annotation."
  },
  "case_id": "transmembrane_0117",
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
      "H25"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry Q9GTP4 (NT2_CRIFA, Crithidia fasciculata Nucleoside Transporter 2) annotates exactly 11 transmembrane helical regions at positions 31-51, 82-102, 112-132, 138-158, 179-199, 211-231, 353-373, 381-401, 409-429, 437-457, and 478-498, which matches option B precisely. The TM annotations carry evidence code ECO:0000255 (inferred by similarity), while the flanking topological domains are supported by experimental mutagenesis data (PubMed:20037157). The sequence is 502 AA, consistent with the benchmark input."
  },
  "important_caveats": [
    "The UniProt TM annotations carry evidence code ECO:0000255 (inferred by similarity), meaning exact boundaries are computational predictions rather than experimentally determined. The topological domain assignments, however, are supported by the 2010 mutagenesis study (PubMed:20037157).",
    "The exact residue-level boundaries (e.g., 381 vs 384) are prediction-dependent; a model's hydrophobicity window might shift by 1-2 residues. However, the offered choices differ by 3+ residues, making the charged-residue argument decisive.",
    "The model would not necessarily recognize the protein as an ENT family member from sequence alone, but hydrophobicity scanning of the full 502-residue sequence would independently identify the 478-498 segment as a TM candidate."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The charged-residue argument cleanly eliminates D relative to B. The hydrophobicity of 478-498, while containing some polar residues, is sufficiently hydrophobic (majority Leu, Ile, Met, Phe, Ala) to be identified as a TM candidate, and the ENT-family 11-TM topology supports its inclusion. No other option is defensible given these analyses."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0117",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry Q9GTP4 (NT2_CRIFA, Crithidia fasciculata Nucleoside Transporter 2) annotates exactly 11 transmembrane helical regions at positions 31-51, 82-102, 112-132, 138-158, 179-199, 211-231, 353-373, 381-401, 409-429, 437-457, and 478-498, which matches option B precisely. The TM annotations carry evidence code ECO:0000255 (inferred by similarity), while the flanking topological domains are supported by experimental mutagenesis data (PubMed:20037157). The sequence is 502 AA, consistent with the benchmark input.",
    "evidence_ids": ["C6", "C8", "C10", "C12", "C14", "C16", "C18", "C20", "C22", "C24", "C26", "H5", "H7", "H9", "H11", "H13", "H15", "H17", "H19", "H21", "H23", "H25"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Option A is trivially eliminated because it references positions up to 1078, far exceeding the 502-residue protein. Option D differs from B by extending TM8 from 381-401 to 384-405; positions 402 (R) and 405 (R) are charged arginines embedded in what would be a membrane-spanning helix, which is energetically highly unfavorable—standard hydrophobicity principles (e.g., Kyte-Doolittle, Wimley-White) strongly disfavor placing Arg in the hydrophobic core of a lipid bilayer, favoring the shorter 381-401 boundary. Option C omits the 478-498 segment; scanning this region reveals a 21-residue predominantly hydrophobic stretch (MLS-GISIMLGLCFGSNLSLAI) with a hydrophobic moment consistent with a TM helix, and the flanking context (charged/polar residues at 458-477 on one side and only 4 short residues at 499-502 on the other) supports it as a membrane-spanning segment. Additionally, equilibrative nucleoside transporters (ENT family) canonically possess 11 TM helices, so recognizing the family-level topology would favor 11 TM regions (B) over 10 (C). Thus, hydrophobicity analysis and family-level topology knowledge meaningfully distinguish B from the alternatives.",
    "missing_item_specific_fact": "",
    "reason": "A model can eliminate A by sequence length, distinguish D from B by identifying charged Arg residues in the proposed extension (402, 405), and identify the 478-498 hydrophobic segment as a TM region using standard hydrophobicity analysis. The ENT family's canonical 11-TM topology provides additional family-level support for B over C. These are transferable principles from membrane protein biology and do not require recalling this specific protein's database annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The charged-residue argument cleanly eliminates D relative to B. The hydrophobicity of 478-498, while containing some polar residues, is sufficiently hydrophobic (majority Leu, Ile, Met, Phe, Ala) to be identified as a TM candidate, and the ENT-family 11-TM topology supports its inclusion. No other option is defensible given these analyses."
  },
  "important_caveats": [
    "The UniProt TM annotations carry evidence code ECO:0000255 (inferred by similarity), meaning exact boundaries are computational predictions rather than experimentally determined. The topological domain assignments, however, are supported by the 2010 mutagenesis study (PubMed:20037157).",
    "The exact residue-level boundaries (e.g., 381 vs 384) are prediction-dependent; a model's hydrophobicity window might shift by 1-2 residues. However, the offered choices differ by 3+ residues, making the charged-residue argument decisive.",
    "The model would not necessarily recognize the protein as an ENT family member from sequence alone, but hydrophobicity scanning of the full 502-residue sequence would independently identify the 478-498 segment as a TM candidate."
  ]
}
```

</details>

## Existing project source checks of the old Luna review only

These unchanged notes concern the earlier Luna claims. They do not validate either new review or the old Qwen review. No new scientific adjudication was performed.

## Project source-check notes

These project-authored, AI-assisted checks assess specific source claims. They are not expert adjudication and do not replace Luna’s saved review or the author key.

### Source check 1

**Check:** `boundary_alternative_not_independently_validated`.

> Cited computational Transmembrane features match keyB381..401; original optionD substitutes384..405, as the model states.

**Remaining uncertainty:** These annotations establish the database interval but do not demonstrate that the alternative interval is equally valid under the wording.

Evidence checked: [C6](#evidence-c6), [C8](#evidence-c8), [C10](#evidence-c10), [C12](#evidence-c12), [C14](#evidence-c14), [C16](#evidence-c16), [C18](#evidence-c18), [C20](#evidence-c20), [C22](#evidence-c22), [C24](#evidence-c24), [C26](#evidence-c26).

## Complete reviewer-only evidence and qualifications

All excerpts supplied in the original and revised reviewer user message follow. This material was not available to the original evaluated model. Accession identity came from dataset image-path metadata. Source support and transferable discrimination are separate judgments.

**Applicability metadata, unchanged:**

```json
{
  "requested_accession": "Q9GTP4",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "benchmark_sequence_sha256": "6e53d808d65dc861f251d0ee2f1b1ba4738fbf7c8abbca765447ebb335e58560",
  "benchmark_sequence_length": 502,
  "current_status": "retrieved",
  "current_sequence_comparison": "matched",
  "current_entry_audit": {
    "entryVersion": 55,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-01-28",
    "lastSequenceUpdateDate": "2001-03-01",
    "sequenceVersion": 1
  },
  "current_uniprot_release": "2026_03",
  "current_record_sha256": "3c9982e101acb399e2361c4884d826caa6e853175a76e749eee018234bb47b73",
  "current_source_sequence_sha256": "6e53d808d65dc861f251d0ee2f1b1ba4738fbf7c8abbca765447ebb335e58560",
  "current_source_sequence_length": 502,
  "historical_status": "retrieved",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "selected_historical_entry_version": 55,
  "selected_historical_version": {
    "accession": "Q9GTP4",
    "database": "Swiss-Prot",
    "entryVersion": 55,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "NT2_CRIFA",
    "sequenceVersion": 1
  },
  "selected_historical_record_sha256": "130ca0749d2c91bc4f41009fc3423401ec6f66d72dd1c0a97de44d68f33480c8",
  "selected_historical_source_sequence_sha256": "6e53d808d65dc861f251d0ee2f1b1ba4738fbf7c8abbca765447ebb335e58560",
  "selected_historical_source_sequence_length": 502,
  "latest_at_cutoff_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 55,
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9GTP4.json)

```json
{
  "evidence_id": "C1",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q9GTP4.json",
  "source_sha256": "3c9982e101acb399e2361c4884d826caa6e853175a76e749eee018234bb47b73",
  "retrieved_utc": "2026-11-02T04:32:48.296419+00:00",
  "json_pointer": "/primaryAccession",
  "excerpt": "\"Q9GTP4\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9GTP4.json)

```json
{
  "evidence_id": "C2",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q9GTP4.json",
  "source_sha256": "3c9982e101acb399e2361c4884d826caa6e853175a76e749eee018234bb47b73",
  "retrieved_utc": "2026-11-02T04:32:48.296419+00:00",
  "json_pointer": "/entryAudit",
  "excerpt": "{\"entryVersion\":55,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-01-28\",\"lastSequenceUpdateDate\":\"2001-03-01\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9GTP4.json)

```json
{
  "evidence_id": "C3",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q9GTP4.json",
  "source_sha256": "3c9982e101acb399e2361c4884d826caa6e853175a76e749eee018234bb47b73",
  "retrieved_utc": "2026-11-02T04:32:48.296419+00:00",
  "json_pointer": "/organism",
  "excerpt": "{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"AAG22611.1\",\"source\":\"EMBL\"}],\"lineage\":[\"Eukaryota\",\"Discoba\",\"Euglenozoa\",\"Kinetoplastea\",\"Metakinetoplastina\",\"Trypanosomatida\",\"Trypanosomatidae\",\"Leishmaniinae\",\"Crithidia\"],\"scientificName\":\"Crithidia fasciculata\",\"taxonId\":5656}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9GTP4.json)

```json
{
  "evidence_id": "C4",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q9GTP4.json",
  "source_sha256": "3c9982e101acb399e2361c4884d826caa6e853175a76e749eee018234bb47b73",
  "retrieved_utc": "2026-11-02T04:32:48.296419+00:00",
  "json_pointer": "/proteinDescription",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"20037157\",\"source\":\"PubMed\"}],\"value\":\"Equilibrative nucleoside transporter 2\"}}],\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"15694482\",\"source\":\"PubMed\"}],\"value\":\"Nucleoside transporter 2\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"15694482\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000303\",\"id\":\"20037157\",\"source\":\"PubMed\"}],\"value\":\"CfNT2\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9GTP4.json)

```json
{
  "evidence_id": "C5",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q9GTP4.json",
  "source_sha256": "3c9982e101acb399e2361c4884d826caa6e853175a76e749eee018234bb47b73",
  "retrieved_utc": "2026-11-02T04:32:48.296419+00:00",
  "json_pointer": "/features/1",
  "excerpt": "{\"description\":\"Cytoplasmic\",\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"20037157\",\"source\":\"PubMed\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":30},\"start\":{\"modifier\":\"EXACT\",\"value\":1}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9GTP4.json)

```json
{
  "evidence_id": "C6",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q9GTP4.json",
  "source_sha256": "3c9982e101acb399e2361c4884d826caa6e853175a76e749eee018234bb47b73",
  "retrieved_utc": "2026-11-02T04:32:48.296419+00:00",
  "json_pointer": "/features/2",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":51},\"start\":{\"modifier\":\"EXACT\",\"value\":31}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9GTP4.json)

```json
{
  "evidence_id": "C7",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q9GTP4.json",
  "source_sha256": "3c9982e101acb399e2361c4884d826caa6e853175a76e749eee018234bb47b73",
  "retrieved_utc": "2026-11-02T04:32:48.296419+00:00",
  "json_pointer": "/features/3",
  "excerpt": "{\"description\":\"Extracellular\",\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"20037157\",\"source\":\"PubMed\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":81},\"start\":{\"modifier\":\"EXACT\",\"value\":52}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9GTP4.json)

```json
{
  "evidence_id": "C8",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q9GTP4.json",
  "source_sha256": "3c9982e101acb399e2361c4884d826caa6e853175a76e749eee018234bb47b73",
  "retrieved_utc": "2026-11-02T04:32:48.296419+00:00",
  "json_pointer": "/features/4",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":102},\"start\":{\"modifier\":\"EXACT\",\"value\":82}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9GTP4.json)

```json
{
  "evidence_id": "C9",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q9GTP4.json",
  "source_sha256": "3c9982e101acb399e2361c4884d826caa6e853175a76e749eee018234bb47b73",
  "retrieved_utc": "2026-11-02T04:32:48.296419+00:00",
  "json_pointer": "/features/5",
  "excerpt": "{\"description\":\"Cytoplasmic\",\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"20037157\",\"source\":\"PubMed\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":111},\"start\":{\"modifier\":\"EXACT\",\"value\":103}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9GTP4.json)

```json
{
  "evidence_id": "C10",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q9GTP4.json",
  "source_sha256": "3c9982e101acb399e2361c4884d826caa6e853175a76e749eee018234bb47b73",
  "retrieved_utc": "2026-11-02T04:32:48.296419+00:00",
  "json_pointer": "/features/6",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":132},\"start\":{\"modifier\":\"EXACT\",\"value\":112}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9GTP4.json)

```json
{
  "evidence_id": "C11",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q9GTP4.json",
  "source_sha256": "3c9982e101acb399e2361c4884d826caa6e853175a76e749eee018234bb47b73",
  "retrieved_utc": "2026-11-02T04:32:48.296419+00:00",
  "json_pointer": "/features/7",
  "excerpt": "{\"description\":\"Extracellular\",\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"20037157\",\"source\":\"PubMed\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":137},\"start\":{\"modifier\":\"EXACT\",\"value\":133}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9GTP4.json)

```json
{
  "evidence_id": "C12",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q9GTP4.json",
  "source_sha256": "3c9982e101acb399e2361c4884d826caa6e853175a76e749eee018234bb47b73",
  "retrieved_utc": "2026-11-02T04:32:48.296419+00:00",
  "json_pointer": "/features/8",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":158},\"start\":{\"modifier\":\"EXACT\",\"value\":138}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C13

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9GTP4.json)

```json
{
  "evidence_id": "C13",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q9GTP4.json",
  "source_sha256": "3c9982e101acb399e2361c4884d826caa6e853175a76e749eee018234bb47b73",
  "retrieved_utc": "2026-11-02T04:32:48.296419+00:00",
  "json_pointer": "/features/9",
  "excerpt": "{\"description\":\"Cytoplasmic\",\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"20037157\",\"source\":\"PubMed\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":178},\"start\":{\"modifier\":\"EXACT\",\"value\":159}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C14

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9GTP4.json)

```json
{
  "evidence_id": "C14",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q9GTP4.json",
  "source_sha256": "3c9982e101acb399e2361c4884d826caa6e853175a76e749eee018234bb47b73",
  "retrieved_utc": "2026-11-02T04:32:48.296419+00:00",
  "json_pointer": "/features/10",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":199},\"start\":{\"modifier\":\"EXACT\",\"value\":179}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C15

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9GTP4.json)

```json
{
  "evidence_id": "C15",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q9GTP4.json",
  "source_sha256": "3c9982e101acb399e2361c4884d826caa6e853175a76e749eee018234bb47b73",
  "retrieved_utc": "2026-11-02T04:32:48.296419+00:00",
  "json_pointer": "/features/11",
  "excerpt": "{\"description\":\"Extracellular\",\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"20037157\",\"source\":\"PubMed\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":210},\"start\":{\"modifier\":\"EXACT\",\"value\":200}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C16

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9GTP4.json)

```json
{
  "evidence_id": "C16",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q9GTP4.json",
  "source_sha256": "3c9982e101acb399e2361c4884d826caa6e853175a76e749eee018234bb47b73",
  "retrieved_utc": "2026-11-02T04:32:48.296419+00:00",
  "json_pointer": "/features/12",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":231},\"start\":{\"modifier\":\"EXACT\",\"value\":211}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C17

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9GTP4.json)

```json
{
  "evidence_id": "C17",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q9GTP4.json",
  "source_sha256": "3c9982e101acb399e2361c4884d826caa6e853175a76e749eee018234bb47b73",
  "retrieved_utc": "2026-11-02T04:32:48.296419+00:00",
  "json_pointer": "/features/13",
  "excerpt": "{\"description\":\"Cytoplasmic\",\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"20037157\",\"source\":\"PubMed\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":352},\"start\":{\"modifier\":\"EXACT\",\"value\":232}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C18

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9GTP4.json)

```json
{
  "evidence_id": "C18",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q9GTP4.json",
  "source_sha256": "3c9982e101acb399e2361c4884d826caa6e853175a76e749eee018234bb47b73",
  "retrieved_utc": "2026-11-02T04:32:48.296419+00:00",
  "json_pointer": "/features/14",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":373},\"start\":{\"modifier\":\"EXACT\",\"value\":353}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C19

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9GTP4.json)

```json
{
  "evidence_id": "C19",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q9GTP4.json",
  "source_sha256": "3c9982e101acb399e2361c4884d826caa6e853175a76e749eee018234bb47b73",
  "retrieved_utc": "2026-11-02T04:32:48.296419+00:00",
  "json_pointer": "/features/15",
  "excerpt": "{\"description\":\"Extracellular\",\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"20037157\",\"source\":\"PubMed\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":380},\"start\":{\"modifier\":\"EXACT\",\"value\":374}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C20

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9GTP4.json)

```json
{
  "evidence_id": "C20",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q9GTP4.json",
  "source_sha256": "3c9982e101acb399e2361c4884d826caa6e853175a76e749eee018234bb47b73",
  "retrieved_utc": "2026-11-02T04:32:48.296419+00:00",
  "json_pointer": "/features/16",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":401},\"start\":{\"modifier\":\"EXACT\",\"value\":381}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C21

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9GTP4.json)

```json
{
  "evidence_id": "C21",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q9GTP4.json",
  "source_sha256": "3c9982e101acb399e2361c4884d826caa6e853175a76e749eee018234bb47b73",
  "retrieved_utc": "2026-11-02T04:32:48.296419+00:00",
  "json_pointer": "/features/17",
  "excerpt": "{\"description\":\"Cytoplasmic\",\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"20037157\",\"source\":\"PubMed\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":408},\"start\":{\"modifier\":\"EXACT\",\"value\":402}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C22

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9GTP4.json)

```json
{
  "evidence_id": "C22",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q9GTP4.json",
  "source_sha256": "3c9982e101acb399e2361c4884d826caa6e853175a76e749eee018234bb47b73",
  "retrieved_utc": "2026-11-02T04:32:48.296419+00:00",
  "json_pointer": "/features/18",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":429},\"start\":{\"modifier\":\"EXACT\",\"value\":409}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C23

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9GTP4.json)

```json
{
  "evidence_id": "C23",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q9GTP4.json",
  "source_sha256": "3c9982e101acb399e2361c4884d826caa6e853175a76e749eee018234bb47b73",
  "retrieved_utc": "2026-11-02T04:32:48.296419+00:00",
  "json_pointer": "/features/19",
  "excerpt": "{\"description\":\"Extracellular\",\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"20037157\",\"source\":\"PubMed\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":436},\"start\":{\"modifier\":\"EXACT\",\"value\":430}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C24

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9GTP4.json)

```json
{
  "evidence_id": "C24",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q9GTP4.json",
  "source_sha256": "3c9982e101acb399e2361c4884d826caa6e853175a76e749eee018234bb47b73",
  "retrieved_utc": "2026-11-02T04:32:48.296419+00:00",
  "json_pointer": "/features/20",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":457},\"start\":{\"modifier\":\"EXACT\",\"value\":437}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C25

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9GTP4.json)

```json
{
  "evidence_id": "C25",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q9GTP4.json",
  "source_sha256": "3c9982e101acb399e2361c4884d826caa6e853175a76e749eee018234bb47b73",
  "retrieved_utc": "2026-11-02T04:32:48.296419+00:00",
  "json_pointer": "/features/21",
  "excerpt": "{\"description\":\"Cytoplasmic\",\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"20037157\",\"source\":\"PubMed\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":477},\"start\":{\"modifier\":\"EXACT\",\"value\":458}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C26

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9GTP4.json)

```json
{
  "evidence_id": "C26",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q9GTP4.json",
  "source_sha256": "3c9982e101acb399e2361c4884d826caa6e853175a76e749eee018234bb47b73",
  "retrieved_utc": "2026-11-02T04:32:48.296419+00:00",
  "json_pointer": "/features/22",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":498},\"start\":{\"modifier\":\"EXACT\",\"value\":478}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C27

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9GTP4.json)

```json
{
  "evidence_id": "C27",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q9GTP4.json",
  "source_sha256": "3c9982e101acb399e2361c4884d826caa6e853175a76e749eee018234bb47b73",
  "retrieved_utc": "2026-11-02T04:32:48.296419+00:00",
  "json_pointer": "/features/23",
  "excerpt": "{\"description\":\"Extracellular\",\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"20037157\",\"source\":\"PubMed\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":502},\"start\":{\"modifier\":\"EXACT\",\"value\":499}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C28

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9GTP4.json)

```json
{
  "evidence_id": "C28",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q9GTP4.json",
  "source_sha256": "3c9982e101acb399e2361c4884d826caa6e853175a76e749eee018234bb47b73",
  "retrieved_utc": "2026-11-02T04:32:48.296419+00:00",
  "json_pointer": "/references/1",
  "excerpt": "{\"citation\":{\"authors\":[\"Liu W.\",\"Arendt C.S.\",\"Gessford S.K.\",\"Ntaba D.\",\"Carter N.S.\",\"Ullman B.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"15694482\"},{\"database\":\"DOI\",\"id\":\"10.1016/j.molbiopara.2004.11.018\"}],\"citationType\":\"journal article\",\"firstPage\":\"1\",\"id\":\"15694482\",\"journal\":\"Mol. Biochem. Parasitol.\",\"lastPage\":\"12\",\"publicationDate\":\"2005\",\"title\":\"Identification and characterization of purine nucleoside transporters from Crithidia fasciculata.\",\"volume\":\"140\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"TRANSPORTER ACTIVITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"INDUCTION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C29

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9GTP4.json)

```json
{
  "evidence_id": "C29",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q9GTP4.json",
  "source_sha256": "3c9982e101acb399e2361c4884d826caa6e853175a76e749eee018234bb47b73",
  "retrieved_utc": "2026-11-02T04:32:48.296419+00:00",
  "json_pointer": "/references/2",
  "excerpt": "{\"citation\":{\"authors\":[\"Arendt C.S.\",\"Ullman B.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"20037157\"},{\"database\":\"DOI\",\"id\":\"10.1074/jbc.m109.074351\"}],\"citationType\":\"journal article\",\"firstPage\":\"6024\",\"id\":\"20037157\",\"journal\":\"J. Biol. Chem.\",\"lastPage\":\"6035\",\"publicationDate\":\"2010\",\"title\":\"Role of transmembrane domain 4 in ligand permeation by Crithidia fasciculata equilibrative nucleoside transporter 2 (CfNT2).\",\"volume\":\"285\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":3,\"referencePositions\":[\"FUNCTION\",\"TRANSPORTER ACTIVITY\",\"SUBCELLULAR LOCATION\",\"MUTAGENESIS OF VAL-89; HIS-138; GLY-139; ALA-140; ILE-141; ALA-142; VAL-143; ILE-144; MET-145; VAL-146; VAL-147; ALA-148; VAL-150; GLY-151; GLY-152; PHE-153; SER-154; LYS-155; ALA-156; LEU-157; ASP-159; SER-160; THR-162; ASN-163; ALA-164; LEU-165; VAL-166; GLY-167; PRO-168; PHE-169; PRO-170; THR-171 AND LYS-172\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9GTP4?format=txt&versions=55)

```json
{
  "evidence_id": "H1",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q9GTP4?format=txt&versions=55",
  "source_sha256": "130ca0749d2c91bc4f41009fc3423401ec6f66d72dd1c0a97de44d68f33480c8",
  "retrieved_utc": "2026-11-02T04:32:52.675125+00:00",
  "source_locator": "lines 1-12",
  "excerpt": "ID   NT2_CRIFA               Reviewed;         502 AA.\nAC   Q9GTP4;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   01-MAR-2001, sequence version 1.\nDT   28-JAN-2026, entry version 55.\nDE   RecName: Full=Nucleoside transporter 2 {ECO:0000303|PubMed:15694482};\nDE            Short=CfNT2 {ECO:0000303|PubMed:15694482, ECO:0000303|PubMed:20037157};\nDE   AltName: Full=Equilibrative nucleoside transporter 2 {ECO:0000303|PubMed:20037157};\nOS   Crithidia fasciculata.\nOC   Eukaryota; Discoba; Euglenozoa; Kinetoplastea; Metakinetoplastina;\nOC   Trypanosomatida; Trypanosomatidae; Leishmaniinae; Crithidia.\nOX   NCBI_TaxID=5656 {ECO:0000312|EMBL:AAG22611.1};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 55,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9GTP4?format=txt&versions=55)

```json
{
  "evidence_id": "H2",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q9GTP4?format=txt&versions=55",
  "source_sha256": "130ca0749d2c91bc4f41009fc3423401ec6f66d72dd1c0a97de44d68f33480c8",
  "retrieved_utc": "2026-11-02T04:32:52.675125+00:00",
  "source_locator": "lines 19-26",
  "excerpt": "RN   [2] {ECO:0000305}\nRP   FUNCTION, TRANSPORTER ACTIVITY, BIOPHYSICOCHEMICAL PROPERTIES, AND\nRP   INDUCTION.\nRX   PubMed=15694482; DOI=10.1016/j.molbiopara.2004.11.018;\nRA   Liu W., Arendt C.S., Gessford S.K., Ntaba D., Carter N.S., Ullman B.;\nRT   \"Identification and characterization of purine nucleoside transporters from\nRT   Crithidia fasciculata.\";\nRL   Mol. Biochem. Parasitol. 140:1-12(2005).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 55,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9GTP4?format=txt&versions=55)

```json
{
  "evidence_id": "H3",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q9GTP4?format=txt&versions=55",
  "source_sha256": "130ca0749d2c91bc4f41009fc3423401ec6f66d72dd1c0a97de44d68f33480c8",
  "retrieved_utc": "2026-11-02T04:32:52.675125+00:00",
  "source_locator": "lines 27-38",
  "excerpt": "RN   [3] {ECO:0000305}\nRP   FUNCTION, TRANSPORTER ACTIVITY, SUBCELLULAR LOCATION, AND MUTAGENESIS OF\nRP   VAL-89; HIS-138; GLY-139; ALA-140; ILE-141; ALA-142; VAL-143; ILE-144;\nRP   MET-145; VAL-146; VAL-147; ALA-148; VAL-150; GLY-151; GLY-152; PHE-153;\nRP   SER-154; LYS-155; ALA-156; LEU-157; ASP-159; SER-160; THR-162; ASN-163;\nRP   ALA-164; LEU-165; VAL-166; GLY-167; PRO-168; PHE-169; PRO-170; THR-171 AND\nRP   LYS-172.\nRX   PubMed=20037157; DOI=10.1074/jbc.m109.074351;\nRA   Arendt C.S., Ullman B.;\nRT   \"Role of transmembrane domain 4 in ligand permeation by Crithidia\nRT   fasciculata equilibrative nucleoside transporter 2 (CfNT2).\";\nRL   J. Biol. Chem. 285:6024-6035(2010).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 55,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9GTP4?format=txt&versions=55)

```json
{
  "evidence_id": "H4",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q9GTP4?format=txt&versions=55",
  "source_sha256": "130ca0749d2c91bc4f41009fc3423401ec6f66d72dd1c0a97de44d68f33480c8",
  "retrieved_utc": "2026-11-02T04:32:52.675125+00:00",
  "source_locator": "lines 83-85",
  "excerpt": "FT   TOPO_DOM        1..30\nFT                   /note=\"Cytoplasmic\"\nFT                   /evidence=\"ECO:0000303|PubMed:20037157\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 55,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9GTP4?format=txt&versions=55)

```json
{
  "evidence_id": "H5",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q9GTP4?format=txt&versions=55",
  "source_sha256": "130ca0749d2c91bc4f41009fc3423401ec6f66d72dd1c0a97de44d68f33480c8",
  "retrieved_utc": "2026-11-02T04:32:52.675125+00:00",
  "source_locator": "lines 86-88",
  "excerpt": "FT   TRANSMEM        31..51\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 55,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9GTP4?format=txt&versions=55)

```json
{
  "evidence_id": "H6",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q9GTP4?format=txt&versions=55",
  "source_sha256": "130ca0749d2c91bc4f41009fc3423401ec6f66d72dd1c0a97de44d68f33480c8",
  "retrieved_utc": "2026-11-02T04:32:52.675125+00:00",
  "source_locator": "lines 89-91",
  "excerpt": "FT   TOPO_DOM        52..81\nFT                   /note=\"Extracellular\"\nFT                   /evidence=\"ECO:0000303|PubMed:20037157\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 55,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9GTP4?format=txt&versions=55)

```json
{
  "evidence_id": "H7",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q9GTP4?format=txt&versions=55",
  "source_sha256": "130ca0749d2c91bc4f41009fc3423401ec6f66d72dd1c0a97de44d68f33480c8",
  "retrieved_utc": "2026-11-02T04:32:52.675125+00:00",
  "source_locator": "lines 92-94",
  "excerpt": "FT   TRANSMEM        82..102\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 55,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9GTP4?format=txt&versions=55)

```json
{
  "evidence_id": "H8",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q9GTP4?format=txt&versions=55",
  "source_sha256": "130ca0749d2c91bc4f41009fc3423401ec6f66d72dd1c0a97de44d68f33480c8",
  "retrieved_utc": "2026-11-02T04:32:52.675125+00:00",
  "source_locator": "lines 95-97",
  "excerpt": "FT   TOPO_DOM        103..111\nFT                   /note=\"Cytoplasmic\"\nFT                   /evidence=\"ECO:0000303|PubMed:20037157\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 55,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9GTP4?format=txt&versions=55)

```json
{
  "evidence_id": "H9",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q9GTP4?format=txt&versions=55",
  "source_sha256": "130ca0749d2c91bc4f41009fc3423401ec6f66d72dd1c0a97de44d68f33480c8",
  "retrieved_utc": "2026-11-02T04:32:52.675125+00:00",
  "source_locator": "lines 98-100",
  "excerpt": "FT   TRANSMEM        112..132\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 55,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H10

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9GTP4?format=txt&versions=55)

```json
{
  "evidence_id": "H10",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q9GTP4?format=txt&versions=55",
  "source_sha256": "130ca0749d2c91bc4f41009fc3423401ec6f66d72dd1c0a97de44d68f33480c8",
  "retrieved_utc": "2026-11-02T04:32:52.675125+00:00",
  "source_locator": "lines 101-103",
  "excerpt": "FT   TOPO_DOM        133..137\nFT                   /note=\"Extracellular\"\nFT                   /evidence=\"ECO:0000303|PubMed:20037157\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 55,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H11

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9GTP4?format=txt&versions=55)

```json
{
  "evidence_id": "H11",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q9GTP4?format=txt&versions=55",
  "source_sha256": "130ca0749d2c91bc4f41009fc3423401ec6f66d72dd1c0a97de44d68f33480c8",
  "retrieved_utc": "2026-11-02T04:32:52.675125+00:00",
  "source_locator": "lines 104-106",
  "excerpt": "FT   TRANSMEM        138..158\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 55,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H12

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9GTP4?format=txt&versions=55)

```json
{
  "evidence_id": "H12",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q9GTP4?format=txt&versions=55",
  "source_sha256": "130ca0749d2c91bc4f41009fc3423401ec6f66d72dd1c0a97de44d68f33480c8",
  "retrieved_utc": "2026-11-02T04:32:52.675125+00:00",
  "source_locator": "lines 107-109",
  "excerpt": "FT   TOPO_DOM        159..178\nFT                   /note=\"Cytoplasmic\"\nFT                   /evidence=\"ECO:0000303|PubMed:20037157\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 55,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H13

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9GTP4?format=txt&versions=55)

```json
{
  "evidence_id": "H13",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q9GTP4?format=txt&versions=55",
  "source_sha256": "130ca0749d2c91bc4f41009fc3423401ec6f66d72dd1c0a97de44d68f33480c8",
  "retrieved_utc": "2026-11-02T04:32:52.675125+00:00",
  "source_locator": "lines 110-112",
  "excerpt": "FT   TRANSMEM        179..199\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 55,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H14

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9GTP4?format=txt&versions=55)

```json
{
  "evidence_id": "H14",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q9GTP4?format=txt&versions=55",
  "source_sha256": "130ca0749d2c91bc4f41009fc3423401ec6f66d72dd1c0a97de44d68f33480c8",
  "retrieved_utc": "2026-11-02T04:32:52.675125+00:00",
  "source_locator": "lines 113-115",
  "excerpt": "FT   TOPO_DOM        200..210\nFT                   /note=\"Extracellular\"\nFT                   /evidence=\"ECO:0000303|PubMed:20037157\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 55,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H15

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9GTP4?format=txt&versions=55)

```json
{
  "evidence_id": "H15",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q9GTP4?format=txt&versions=55",
  "source_sha256": "130ca0749d2c91bc4f41009fc3423401ec6f66d72dd1c0a97de44d68f33480c8",
  "retrieved_utc": "2026-11-02T04:32:52.675125+00:00",
  "source_locator": "lines 116-118",
  "excerpt": "FT   TRANSMEM        211..231\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 55,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H16

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9GTP4?format=txt&versions=55)

```json
{
  "evidence_id": "H16",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q9GTP4?format=txt&versions=55",
  "source_sha256": "130ca0749d2c91bc4f41009fc3423401ec6f66d72dd1c0a97de44d68f33480c8",
  "retrieved_utc": "2026-11-02T04:32:52.675125+00:00",
  "source_locator": "lines 119-121",
  "excerpt": "FT   TOPO_DOM        232..352\nFT                   /note=\"Cytoplasmic\"\nFT                   /evidence=\"ECO:0000303|PubMed:20037157\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 55,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H17

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9GTP4?format=txt&versions=55)

```json
{
  "evidence_id": "H17",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q9GTP4?format=txt&versions=55",
  "source_sha256": "130ca0749d2c91bc4f41009fc3423401ec6f66d72dd1c0a97de44d68f33480c8",
  "retrieved_utc": "2026-11-02T04:32:52.675125+00:00",
  "source_locator": "lines 122-124",
  "excerpt": "FT   TRANSMEM        353..373\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 55,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H18

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9GTP4?format=txt&versions=55)

```json
{
  "evidence_id": "H18",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q9GTP4?format=txt&versions=55",
  "source_sha256": "130ca0749d2c91bc4f41009fc3423401ec6f66d72dd1c0a97de44d68f33480c8",
  "retrieved_utc": "2026-11-02T04:32:52.675125+00:00",
  "source_locator": "lines 125-127",
  "excerpt": "FT   TOPO_DOM        374..380\nFT                   /note=\"Extracellular\"\nFT                   /evidence=\"ECO:0000303|PubMed:20037157\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 55,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H19

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9GTP4?format=txt&versions=55)

```json
{
  "evidence_id": "H19",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q9GTP4?format=txt&versions=55",
  "source_sha256": "130ca0749d2c91bc4f41009fc3423401ec6f66d72dd1c0a97de44d68f33480c8",
  "retrieved_utc": "2026-11-02T04:32:52.675125+00:00",
  "source_locator": "lines 128-130",
  "excerpt": "FT   TRANSMEM        381..401\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 55,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H20

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9GTP4?format=txt&versions=55)

```json
{
  "evidence_id": "H20",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q9GTP4?format=txt&versions=55",
  "source_sha256": "130ca0749d2c91bc4f41009fc3423401ec6f66d72dd1c0a97de44d68f33480c8",
  "retrieved_utc": "2026-11-02T04:32:52.675125+00:00",
  "source_locator": "lines 131-133",
  "excerpt": "FT   TOPO_DOM        402..408\nFT                   /note=\"Cytoplasmic\"\nFT                   /evidence=\"ECO:0000303|PubMed:20037157\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 55,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H21

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9GTP4?format=txt&versions=55)

```json
{
  "evidence_id": "H21",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q9GTP4?format=txt&versions=55",
  "source_sha256": "130ca0749d2c91bc4f41009fc3423401ec6f66d72dd1c0a97de44d68f33480c8",
  "retrieved_utc": "2026-11-02T04:32:52.675125+00:00",
  "source_locator": "lines 134-136",
  "excerpt": "FT   TRANSMEM        409..429\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 55,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H22

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9GTP4?format=txt&versions=55)

```json
{
  "evidence_id": "H22",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q9GTP4?format=txt&versions=55",
  "source_sha256": "130ca0749d2c91bc4f41009fc3423401ec6f66d72dd1c0a97de44d68f33480c8",
  "retrieved_utc": "2026-11-02T04:32:52.675125+00:00",
  "source_locator": "lines 137-139",
  "excerpt": "FT   TOPO_DOM        430..436\nFT                   /note=\"Extracellular\"\nFT                   /evidence=\"ECO:0000303|PubMed:20037157\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 55,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H23

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9GTP4?format=txt&versions=55)

```json
{
  "evidence_id": "H23",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q9GTP4?format=txt&versions=55",
  "source_sha256": "130ca0749d2c91bc4f41009fc3423401ec6f66d72dd1c0a97de44d68f33480c8",
  "retrieved_utc": "2026-11-02T04:32:52.675125+00:00",
  "source_locator": "lines 140-142",
  "excerpt": "FT   TRANSMEM        437..457\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 55,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H24

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9GTP4?format=txt&versions=55)

```json
{
  "evidence_id": "H24",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q9GTP4?format=txt&versions=55",
  "source_sha256": "130ca0749d2c91bc4f41009fc3423401ec6f66d72dd1c0a97de44d68f33480c8",
  "retrieved_utc": "2026-11-02T04:32:52.675125+00:00",
  "source_locator": "lines 143-145",
  "excerpt": "FT   TOPO_DOM        458..477\nFT                   /note=\"Cytoplasmic\"\nFT                   /evidence=\"ECO:0000303|PubMed:20037157\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 55,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H25

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9GTP4?format=txt&versions=55)

```json
{
  "evidence_id": "H25",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q9GTP4?format=txt&versions=55",
  "source_sha256": "130ca0749d2c91bc4f41009fc3423401ec6f66d72dd1c0a97de44d68f33480c8",
  "retrieved_utc": "2026-11-02T04:32:52.675125+00:00",
  "source_locator": "lines 146-148",
  "excerpt": "FT   TRANSMEM        478..498\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 55,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H26

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9GTP4?format=txt&versions=55)

```json
{
  "evidence_id": "H26",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q9GTP4?format=txt&versions=55",
  "source_sha256": "130ca0749d2c91bc4f41009fc3423401ec6f66d72dd1c0a97de44d68f33480c8",
  "retrieved_utc": "2026-11-02T04:32:52.675125+00:00",
  "source_locator": "lines 149-151",
  "excerpt": "FT   TOPO_DOM        499..502\nFT                   /note=\"Extracellular\"\nFT                   /evidence=\"ECO:0000303|PubMed:20037157\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 55,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json), zero-based source row 117. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
