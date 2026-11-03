# transmembrane_0034: before and after transfer clarification

[All 1,328 cases](../README.md) · [Method](../METHOD.md) · [Summary](../SUMMARY.md) · [Exact reviewer user message](../inputs/transmembrane_0034.txt)

**Task:** `transmembrane`  
**Author key, unchanged:** **D** — 47..71; 139..171; 196..220; 421..450; 466..495; 500..536; 560..592; 613..631; 635..659; 667..695; 701..721

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
MLPYVIATLGSAGSTCKASTCSNSTKDYCYSARIRSTVLQGLPFGGVPTVLALDFMCFLALLFVFSILRKVAWDYGRLALVTDADSIASALHSDNHDRYERLTSVSSSVDFDQRDNGFCSWLTAIFRIKDDEIRDKCGGDAVHYLSFQRHIIGLLVAVGVLSVGIVLPVNFSGDLLENNAYSFGRTTIANLNSGNNLLWLHTSFAFLYLLLTVYSMRRHTSKMRYKEDDLVKRTLFINGISKYAEPEKIKKHFEEAYANCTVLEARPCYDVARLMFLDAERRKAERGRIYFTNLQSKENTPSMINPKPCGHLCCCVIRGCEEVEAIEYYTKLEEKLKDDYKREKEKVNEKPLGMAFVTFHNETITAIILKDFNACKCQGCACRGEPRASSCSESLHVSNWTVSYAPDPQNIYWEHLSIRGFIWWIRCLVINVVLFILLFFLTTPAIIITTMDKFNVTKPVEYLNNPIITQFFPTLLLWCFSALLPTIVYYSAFFEAHWTRSGENRTTMHKCYTFLIFMVLLLPSLGLSSLDVFFRWLFDKKFLAEAAVRFECVFLPDNGAFFVNYVIASAFIGNAMDLLRIPGLLMYMIRLCLARSAAERRNVKRHQAYEFQFGAAYAWMMCVFTVVMTYSITCPIIVPFGLMYMLLKHLVDRYNLYYAYLPAKLDKKIHSGAVNQVVAAPILCLFWLLFFSTMRTGFLAPTSMFTFVVLVITIVICLCHVCFGHFKYLSAHNYKIEHTEVDTTESRQNGRPATNLPAPKSAKYIAQVLQDSSPEGEATESEEQGSQDEELITTDGMNDTDFQSCEDSLIENEIRQ

[Multiple Choices]
A. 47..71; 139..171; 196..220; 421..450; 466..495; 500..536; 613..631; 635..659; 667..695; 701..721
B. 47..71; 139..171; 196..220; 421..450; 466..495; 500..536; 560..592; 613..631; 635..659; 669..693; 701..721
C. 27..47; 78..98; 108..128; 136..156; 173..193; 209..229; 337..357; 366..386; 400..420; 432..452; 465..485
D. 47..71; 139..171; 196..220; 421..450; 466..495; 500..536; 560..592; 613..631; 635..659; 667..695; 701..721
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

> The sequence-matched UniProt record annotates the transmembrane regions as 47–71, 139–171, 196–220, 421–450, 466–495, 500–536, 560–592, 613–631, 635–659, 667–695, and 701–721, matching D. These annotations are supported by similarity evidence to Q3TWI9, not shown here to be direct experimental measurements for this chicken protein.

Citations as saved: [H4](#evidence-h4), [H6](#evidence-h6), [H8](#evidence-h8), [H10](#evidence-h10), [H12](#evidence-h12), [H14](#evidence-h14), [H16](#evidence-h16), [H18](#evidence-h18), [H20](#evidence-h20), [H22](#evidence-h22), [H24](#evidence-h24).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence contains multiple hydrophobic stretches consistent with membrane-spanning helices, which supports the general prediction of many transmembrane regions.


**Missing item-specific fact**

> The exact annotated helix boundaries—especially whether the final listed helix is 667–695 or 669–693—are protein-specific coordinate information not supplied in the question.


**Reason**

> General hydropathy can identify plausible membrane-spanning regions but does not uniquely establish the precise listed boundaries. Distinguishing D from B requires the protein-specific annotation or an equivalent detailed analysis; recognizing or recalling the exact database entry would be lookup, not reasoning from the supplied input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "D"
]
```

> B and D differ only in the boundaries assigned to the same final hydrophobic helix. The broad description of a segment that crosses a membrane does not itself explain why the narrower 669–693 interval should be rejected as a crossing segment, although the matched annotation specifies 667–695.


### Important caveats

- The reviewer-only source sequence matches the supplied sequence; the author’s precise source snapshot is unknown.
- The cited transmembrane annotations carry similarity-based evidence, so they support the key as annotation but do not establish direct experimental verification for this exact protein.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains multiple hydrophobic stretches consistent with membrane-spanning helices, which supports the general prediction of many transmembrane regions.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The exact annotated helix boundaries—especially whether the final listed helix is 667–695 or 669–693—are protein-specific coordinate information not supplied in the question.",
    "reason": "General hydropathy can identify plausible membrane-spanning regions but does not uniquely establish the precise listed boundaries. Distinguishing D from B requires the protein-specific annotation or an equivalent detailed analysis; recognizing or recalling the exact database entry would be lookup, not reasoning from the supplied input."
  },
  "case_id": "transmembrane_0034",
  "expected_answer_check": {
    "evidence_ids": [
      "H4",
      "H6",
      "H8",
      "H10",
      "H12",
      "H14",
      "H16",
      "H18",
      "H20",
      "H22",
      "H24"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates the transmembrane regions as 47–71, 139–171, 196–220, 421–450, 466–495, 500–536, 560–592, 613–631, 635–659, 667–695, and 701–721, matching D. These annotations are supported by similarity evidence to Q3TWI9, not shown here to be direct experimental measurements for this chicken protein."
  },
  "important_caveats": [
    "The reviewer-only source sequence matches the supplied sequence; the author’s precise source snapshot is unknown.",
    "The cited transmembrane annotations carry similarity-based evidence, so they support the key as annotation but do not establish direct experimental verification for this exact protein."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "D"
    ],
    "reason": "B and D differ only in the boundaries assigned to the same final hydrophobic helix. The broad description of a segment that crosses a membrane does not itself explain why the narrower 669–693 interval should be rejected as a crossing segment, although the matched annotation specifies 667–695."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0034",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates the transmembrane regions as 47–71, 139–171, 196–220, 421–450, 466–495, 500–536, 560–592, 613–631, 635–659, 667–695, and 701–721, matching D. These annotations are supported by similarity evidence to Q3TWI9, not shown here to be direct experimental measurements for this chicken protein.",
    "evidence_ids": ["H4", "H6", "H8", "H10", "H12", "H14", "H16", "H18", "H20", "H22", "H24"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence contains multiple hydrophobic stretches consistent with membrane-spanning helices, which supports the general prediction of many transmembrane regions.",
    "missing_item_specific_fact": "The exact annotated helix boundaries—especially whether the final listed helix is 667–695 or 669–693—are protein-specific coordinate information not supplied in the question.",
    "reason": "General hydropathy can identify plausible membrane-spanning regions but does not uniquely establish the precise listed boundaries. Distinguishing D from B requires the protein-specific annotation or an equivalent detailed analysis; recognizing or recalling the exact database entry would be lookup, not reasoning from the supplied input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "D"],
    "reason": "B and D differ only in the boundaries assigned to the same final hydrophobic helix. The broad description of a segment that crosses a membrane does not itself explain why the narrower 669–693 interval should be rejected as a crossing segment, although the matched annotation specifies 667–695."
  },
  "important_caveats": [
    "The reviewer-only source sequence matches the supplied sequence; the author’s precise source snapshot is unknown.",
    "The cited transmembrane annotations carry similarity-based evidence, so they support the key as annotation but do not establish direct experimental verification for this exact protein."
  ]
}
```

</details>

## Before: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> Choice D lists exactly 11 transmembrane helices (TM0–TM10) at positions 47..71, 139..171, 196..220, 421..450, 466..495, 500..536, 560..592, 613..631, 635..659, 667..695, 701..721, which match the UniProtKB annotation for A0A8V0ZB02 (TMEM63B_CHICK) residue-for-residue. The sequence in the question matches the UniProt entry exactly (SHA-256 confirmed). The annotation evidence codes are ECO:0000250 (similarity to human Q3TWI9), indicating computational transfer rather than direct experimental determination, but the annotation is the authoritative database record for this protein.

Citations as saved: [C6](#evidence-c6), [C8](#evidence-c8), [C10](#evidence-c10), [C12](#evidence-c12), [C14](#evidence-c14), [C16](#evidence-c16), [C18](#evidence-c18), [C20](#evidence-c20), [C22](#evidence-c22), [C24](#evidence-c24), [C26](#evidence-c26), [H4](#evidence-h4), [H6](#evidence-h6), [H8](#evidence-h8), [H10](#evidence-h10), [H12](#evidence-h12), [H14](#evidence-h14), [H16](#evidence-h16), [H18](#evidence-h18), [H20](#evidence-h20), [H22](#evidence-h22), [H24](#evidence-h24).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> Choice C can be eliminated by general reasoning: it presents uniform 20-residue segments with a naive sliding-window topology that does not match the known 11-TM architecture of the TMEM63/OSCA family. Choice A is missing TM6 (560..592), which could in principle be identified as a hydrophobic stretch by sequence analysis. However, the critical distinction between B and D is a 2-residue boundary shift at TM9 (669..693 vs 667..695). This falls well within the ±2–3 residue uncertainty of any hydrophobicity-based TM predictor (TMHMM, Phobius, DeepTMHMM) and cannot be resolved by general biological reasoning about helix length, hydrophobicity, or topology. Selecting D over B requires knowledge of the specific annotation boundary from UniProt or the output of a particular prediction tool.


**Missing item-specific fact**

> The exact TM9 boundary assignment (667..695 vs 669..693) as recorded in the UniProt annotation for A0A8V0ZB02, which was derived by similarity transfer from human TMEM63B (Q3TWI9) and is not derivable from the sequence alone through general biological principles.


**Reason**

> While eliminating C and identifying the missing TM6 in A involves some reasoning about TM domain length and hydrophobicity, the final B-vs-D discrimination hinges on a 2-residue boundary difference at TM9 that is within the resolution limit of hydrophobicity prediction. This is an item-specific annotation fact, not a consequence of general biological knowledge.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "D"
]
```

> B and D differ only at TM9 boundaries (669..693 vs 667..695). A 2-residue shift at a TM helix boundary is within the typical uncertainty of hydrophobicity-based prediction and does not alter the topology or the number of membrane crossings. From a pure sequence-analysis standpoint, both assignments are biologically plausible. D is correct per the UniProt annotation, but the question wording ('correctly identifies the start and end positions') does not provide grounds to prefer 667 over 669 or 695 over 693 without referencing the specific annotation.


### Important caveats

- All 11 TM annotations carry evidence code ECO:0000250 (similarity to Q3TWI9), meaning they are computational transfers from the human ortholog, not experimentally validated boundaries for the chicken protein.
- The UniProt entry was first public on 2025-06-18; the author's source snapshot date is unknown, so the annotation available at question-construction time may differ.
- Choice A (10 segments, missing TM6) and Choice C (naive 20-residue scan) are clearly distinguishable from D by reasoning; the ambiguity is confined to the B-vs-D boundary.
- The sequence matches the UniProt entry exactly (SHA-256 verified), so coordinate numbering is consistent.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Choice C can be eliminated by general reasoning: it presents uniform 20-residue segments with a naive sliding-window topology that does not match the known 11-TM architecture of the TMEM63/OSCA family. Choice A is missing TM6 (560..592), which could in principle be identified as a hydrophobic stretch by sequence analysis. However, the critical distinction between B and D is a 2-residue boundary shift at TM9 (669..693 vs 667..695). This falls well within the ±2–3 residue uncertainty of any hydrophobicity-based TM predictor (TMHMM, Phobius, DeepTMHMM) and cannot be resolved by general biological reasoning about helix length, hydrophobicity, or topology. Selecting D over B requires knowledge of the specific annotation boundary from UniProt or the output of a particular prediction tool.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The exact TM9 boundary assignment (667..695 vs 669..693) as recorded in the UniProt annotation for A0A8V0ZB02, which was derived by similarity transfer from human TMEM63B (Q3TWI9) and is not derivable from the sequence alone through general biological principles.",
    "reason": "While eliminating C and identifying the missing TM6 in A involves some reasoning about TM domain length and hydrophobicity, the final B-vs-D discrimination hinges on a 2-residue boundary difference at TM9 that is within the resolution limit of hydrophobicity prediction. This is an item-specific annotation fact, not a consequence of general biological knowledge."
  },
  "case_id": "transmembrane_0034",
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
      "H4",
      "H6",
      "H8",
      "H10",
      "H12",
      "H14",
      "H16",
      "H18",
      "H20",
      "H22",
      "H24"
    ],
    "judgment": "supported",
    "reason": "Choice D lists exactly 11 transmembrane helices (TM0–TM10) at positions 47..71, 139..171, 196..220, 421..450, 466..495, 500..536, 560..592, 613..631, 635..659, 667..695, 701..721, which match the UniProtKB annotation for A0A8V0ZB02 (TMEM63B_CHICK) residue-for-residue. The sequence in the question matches the UniProt entry exactly (SHA-256 confirmed). The annotation evidence codes are ECO:0000250 (similarity to human Q3TWI9), indicating computational transfer rather than direct experimental determination, but the annotation is the authoritative database record for this protein."
  },
  "important_caveats": [
    "All 11 TM annotations carry evidence code ECO:0000250 (similarity to Q3TWI9), meaning they are computational transfers from the human ortholog, not experimentally validated boundaries for the chicken protein.",
    "The UniProt entry was first public on 2025-06-18; the author's source snapshot date is unknown, so the annotation available at question-construction time may differ.",
    "Choice A (10 segments, missing TM6) and Choice C (naive 20-residue scan) are clearly distinguishable from D by reasoning; the ambiguity is confined to the B-vs-D boundary.",
    "The sequence matches the UniProt entry exactly (SHA-256 verified), so coordinate numbering is consistent."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "D"
    ],
    "reason": "B and D differ only at TM9 boundaries (669..693 vs 667..695). A 2-residue shift at a TM helix boundary is within the typical uncertainty of hydrophobicity-based prediction and does not alter the topology or the number of membrane crossings. From a pure sequence-analysis standpoint, both assignments are biologically plausible. D is correct per the UniProt annotation, but the question wording ('correctly identifies the start and end positions') does not provide grounds to prefer 667 over 669 or 695 over 693 without referencing the specific annotation."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0034",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "Choice D lists exactly 11 transmembrane helices (TM0–TM10) at positions 47..71, 139..171, 196..220, 421..450, 466..495, 500..536, 560..592, 613..631, 635..659, 667..695, 701..721, which match the UniProtKB annotation for A0A8V0ZB02 (TMEM63B_CHICK) residue-for-residue. The sequence in the question matches the UniProt entry exactly (SHA-256 confirmed). The annotation evidence codes are ECO:0000250 (similarity to human Q3TWI9), indicating computational transfer rather than direct experimental determination, but the annotation is the authoritative database record for this protein.",
    "evidence_ids": ["C6", "C8", "C10", "C12", "C14", "C16", "C18", "C20", "C22", "C24", "C26", "H4", "H6", "H8", "H10", "H12", "H14", "H16", "H18", "H20", "H22", "H24"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "Choice C can be eliminated by general reasoning: it presents uniform 20-residue segments with a naive sliding-window topology that does not match the known 11-TM architecture of the TMEM63/OSCA family. Choice A is missing TM6 (560..592), which could in principle be identified as a hydrophobic stretch by sequence analysis. However, the critical distinction between B and D is a 2-residue boundary shift at TM9 (669..693 vs 667..695). This falls well within the ±2–3 residue uncertainty of any hydrophobicity-based TM predictor (TMHMM, Phobius, DeepTMHMM) and cannot be resolved by general biological reasoning about helix length, hydrophobicity, or topology. Selecting D over B requires knowledge of the specific annotation boundary from UniProt or the output of a particular prediction tool.",
    "missing_item_specific_fact": "The exact TM9 boundary assignment (667..695 vs 669..693) as recorded in the UniProt annotation for A0A8V0ZB02, which was derived by similarity transfer from human TMEM63B (Q3TWI9) and is not derivable from the sequence alone through general biological principles.",
    "reason": "While eliminating C and identifying the missing TM6 in A involves some reasoning about TM domain length and hydrophobicity, the final B-vs-D discrimination hinges on a 2-residue boundary difference at TM9 that is within the resolution limit of hydrophobicity prediction. This is an item-specific annotation fact, not a consequence of general biological knowledge."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "D"],
    "reason": "B and D differ only at TM9 boundaries (669..693 vs 667..695). A 2-residue shift at a TM helix boundary is within the typical uncertainty of hydrophobicity-based prediction and does not alter the topology or the number of membrane crossings. From a pure sequence-analysis standpoint, both assignments are biologically plausible. D is correct per the UniProt annotation, but the question wording ('correctly identifies the start and end positions') does not provide grounds to prefer 667 over 669 or 695 over 693 without referencing the specific annotation."
  },
  "important_caveats": [
    "All 11 TM annotations carry evidence code ECO:0000250 (similarity to Q3TWI9), meaning they are computational transfers from the human ortholog, not experimentally validated boundaries for the chicken protein.",
    "The UniProt entry was first public on 2025-06-18; the author's source snapshot date is unknown, so the annotation available at question-construction time may differ.",
    "Choice A (10 segments, missing TM6) and Choice C (naive 20-residue scan) are clearly distinguishable from D by reasoning; the ambiguity is confined to the B-vs-D boundary.",
    "The sequence matches the UniProt entry exactly (SHA-256 verified), so coordinate numbering is consistent."
  ]
}
```

</details>

## After: GPT-6 Luna

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The matched UniProt sequence annotation lists the transmembrane segments in choice D. These annotations are supported by similarity evidence to another UniProt entry, so they support the key as database annotation but are not direct experimental validation for this sequence.

Citations as saved: [C6](#evidence-c6), [C8](#evidence-c8), [C10](#evidence-c10), [C12](#evidence-c12), [C14](#evidence-c14), [C16](#evidence-c16), [C18](#evidence-c18), [C20](#evidence-c20), [C22](#evidence-c22), [C24](#evidence-c24), [C26](#evidence-c26).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence has repeated hydrophobic stretches consistent with a multi-pass membrane protein, which helps distinguish the membrane-spanning choices from C and favors choices that include the segment around 560–592. But this does not reliably resolve the two-residue boundary differences between B and D at the later helix.


**Missing item-specific fact**

> The reference-specific or convention-specific boundary for the helix around 667–695 is needed to select D over B as the exact keyed coordinate range.


**Reason**

> Transferable knowledge supports identifying the overall membrane topology, but B and D both mark the same strongly hydrophobic helix and differ only slightly in its endpoints. The sequence and general membrane-protein principles do not provide a dependable basis for the exact boundary distinction.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "D"
]
```

> Both options identify the same hydrophobic membrane-spanning helix; the small endpoint difference is not clearly resolvable from the wording or sequence alone.


### Important caveats

- The supporting transmembrane annotations use similarity evidence; they should not be described as experimentally established for this exact protein.
- The reviewer-only source identity and annotations were not original inputs and are not used as transferable knowledge.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has repeated hydrophobic stretches consistent with a multi-pass membrane protein, which helps distinguish the membrane-spanning choices from C and favors choices that include the segment around 560–592. But this does not reliably resolve the two-residue boundary differences between B and D at the later helix.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The reference-specific or convention-specific boundary for the helix around 667–695 is needed to select D over B as the exact keyed coordinate range.",
    "reason": "Transferable knowledge supports identifying the overall membrane topology, but B and D both mark the same strongly hydrophobic helix and differ only slightly in its endpoints. The sequence and general membrane-protein principles do not provide a dependable basis for the exact boundary distinction."
  },
  "case_id": "transmembrane_0034",
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
    "reason": "The matched UniProt sequence annotation lists the transmembrane segments in choice D. These annotations are supported by similarity evidence to another UniProt entry, so they support the key as database annotation but are not direct experimental validation for this sequence."
  },
  "important_caveats": [
    "The supporting transmembrane annotations use similarity evidence; they should not be described as experimentally established for this exact protein.",
    "The reviewer-only source identity and annotations were not original inputs and are not used as transferable knowledge."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "D"
    ],
    "reason": "Both options identify the same hydrophobic membrane-spanning helix; the small endpoint difference is not clearly resolvable from the wording or sequence alone."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0034",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The matched UniProt sequence annotation lists the transmembrane segments in choice D. These annotations are supported by similarity evidence to another UniProt entry, so they support the key as database annotation but are not direct experimental validation for this sequence.",
    "evidence_ids": ["C6", "C8", "C10", "C12", "C14", "C16", "C18", "C20", "C22", "C24", "C26"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence has repeated hydrophobic stretches consistent with a multi-pass membrane protein, which helps distinguish the membrane-spanning choices from C and favors choices that include the segment around 560–592. But this does not reliably resolve the two-residue boundary differences between B and D at the later helix.",
    "missing_item_specific_fact": "The reference-specific or convention-specific boundary for the helix around 667–695 is needed to select D over B as the exact keyed coordinate range.",
    "reason": "Transferable knowledge supports identifying the overall membrane topology, but B and D both mark the same strongly hydrophobic helix and differ only slightly in its endpoints. The sequence and general membrane-protein principles do not provide a dependable basis for the exact boundary distinction."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "D"],
    "reason": "Both options identify the same hydrophobic membrane-spanning helix; the small endpoint difference is not clearly resolvable from the wording or sequence alone."
  },
  "important_caveats": [
    "The supporting transmembrane annotations use similarity evidence; they should not be described as experimentally established for this exact protein.",
    "The reviewer-only source identity and annotations were not original inputs and are not used as transferable knowledge."
  ]
}
```

</details>

## After: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A0A8V0ZB02 (TMEM63B, Gallus gallus) annotates exactly 11 transmembrane helices at the positions listed in option D: TM0 47-71, TM1 139-171, TM2 196-220, TM3 421-450, TM4 466-495, TM5 500-536, TM6 560-592, TM7 613-631, TM8 635-659, TM9 667-695, TM10 701-721. The evidence codes are ECO:0000250 (similarity-based annotation from human ortholog Q3TWI9), so this is computational inference by homology rather than direct experimental determination, but the annotation is internally consistent and matches the sequence. Option D matches the annotation exactly.

Citations as saved: [C6](#evidence-c6), [C8](#evidence-c8), [C10](#evidence-c10), [C12](#evidence-c12), [C14](#evidence-c14), [C16](#evidence-c16), [C18](#evidence-c18), [C20](#evidence-c20), [C22](#evidence-c22), [C24](#evidence-c24), [C26](#evidence-c26).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Option C uses uniformly 20-residue windows at roughly regular intervals, which contradicts the well-known variability in TM helix lengths (typically 18-30+ residues) and the irregular spacing dictated by actual hydrophobic stretches; a sliding-window hydrophobicity analysis immediately eliminates C. Option A omits the TM6 region at 560-592; examining the sequence between the end of TM5 (~536) and the cytoplasmic loop at 593-612 reveals a clearly hydrophobic stretch of ~33 residues consistent with a membrane-spanning helix, so a model performing hydrophobicity profiling can identify this region and eliminate A. The remaining distinction between B and D is a 2-residue boundary shift in TM9 (669-693 vs 667-695). A model examining the hydrophobicity profile at those exact boundaries could note whether residues at positions 667-668 and 694-695 are hydrophobic (supporting D's wider helix) or hydrophilic (supporting B's narrower helix). While this 2-residue difference is within the typical uncertainty of TM boundary prediction, the overall reasoning path—identifying 11 hydrophobic segments of varying lengths at approximately the right positions—meaningfully distinguishes D from A and C, and provides a defensible (if not certain) basis for preferring D over B.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The primary reasoning path (hydrophobicity analysis to identify ~11 TM segments of varying length, eliminating C's uniform windows and A's missing TM6) is well-supported by transferable knowledge of membrane protein topology. The B-vs-D distinction involves only a 2-residue boundary shift in TM9, which is subtle but can be approached by examining local hydrophobicity at those positions. The question is answerable through sequence-based reasoning without needing to recall this protein's specific database record.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "D"
]
```

> Options B and D differ only in the TM9 boundaries: B gives 669-693 (25 residues) while D gives 667-695 (29 residues). A 2-residue shift at each boundary is within the typical uncertainty of TM helix boundary prediction from sequence alone. Without precise knowledge of where the hydrophobic stretch begins and ends at those exact positions, a model could reasonably select either option. The UniProt annotation supports D, but the sequence-based reasoning margin between B and D is very narrow.


### Important caveats

- All UniProt TM annotations for this entry carry evidence code ECO:0000250 (similarity to Q3TWI9, human TMEM63B), meaning they are computational inferences by homology rather than experimentally determined boundaries.
- The 2-residue boundary difference between options B and D (TM9: 669-693 vs 667-695) is within the typical error range of TM prediction algorithms, making this the weakest point of the question's discriminability.
- The reviewer-only evidence was not available to the evaluated model; the reasoning assessment is based solely on the original sequence and answer choices.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Option C uses uniformly 20-residue windows at roughly regular intervals, which contradicts the well-known variability in TM helix lengths (typically 18-30+ residues) and the irregular spacing dictated by actual hydrophobic stretches; a sliding-window hydrophobicity analysis immediately eliminates C. Option A omits the TM6 region at 560-592; examining the sequence between the end of TM5 (~536) and the cytoplasmic loop at 593-612 reveals a clearly hydrophobic stretch of ~33 residues consistent with a membrane-spanning helix, so a model performing hydrophobicity profiling can identify this region and eliminate A. The remaining distinction between B and D is a 2-residue boundary shift in TM9 (669-693 vs 667-695). A model examining the hydrophobicity profile at those exact boundaries could note whether residues at positions 667-668 and 694-695 are hydrophobic (supporting D's wider helix) or hydrophilic (supporting B's narrower helix). While this 2-residue difference is within the typical uncertainty of TM boundary prediction, the overall reasoning path—identifying 11 hydrophobic segments of varying lengths at approximately the right positions—meaningfully distinguishes D from A and C, and provides a defensible (if not certain) basis for preferring D over B.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The primary reasoning path (hydrophobicity analysis to identify ~11 TM segments of varying length, eliminating C's uniform windows and A's missing TM6) is well-supported by transferable knowledge of membrane protein topology. The B-vs-D distinction involves only a 2-residue boundary shift in TM9, which is subtle but can be approached by examining local hydrophobicity at those positions. The question is answerable through sequence-based reasoning without needing to recall this protein's specific database record."
  },
  "case_id": "transmembrane_0034",
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
    "reason": "The UniProt entry A0A8V0ZB02 (TMEM63B, Gallus gallus) annotates exactly 11 transmembrane helices at the positions listed in option D: TM0 47-71, TM1 139-171, TM2 196-220, TM3 421-450, TM4 466-495, TM5 500-536, TM6 560-592, TM7 613-631, TM8 635-659, TM9 667-695, TM10 701-721. The evidence codes are ECO:0000250 (similarity-based annotation from human ortholog Q3TWI9), so this is computational inference by homology rather than direct experimental determination, but the annotation is internally consistent and matches the sequence. Option D matches the annotation exactly."
  },
  "important_caveats": [
    "All UniProt TM annotations for this entry carry evidence code ECO:0000250 (similarity to Q3TWI9, human TMEM63B), meaning they are computational inferences by homology rather than experimentally determined boundaries.",
    "The 2-residue boundary difference between options B and D (TM9: 669-693 vs 667-695) is within the typical error range of TM prediction algorithms, making this the weakest point of the question's discriminability.",
    "The reviewer-only evidence was not available to the evaluated model; the reasoning assessment is based solely on the original sequence and answer choices."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "D"
    ],
    "reason": "Options B and D differ only in the TM9 boundaries: B gives 669-693 (25 residues) while D gives 667-695 (29 residues). A 2-residue shift at each boundary is within the typical uncertainty of TM helix boundary prediction from sequence alone. Without precise knowledge of where the hydrophobic stretch begins and ends at those exact positions, a model could reasonably select either option. The UniProt annotation supports D, but the sequence-based reasoning margin between B and D is very narrow."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0034",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A0A8V0ZB02 (TMEM63B, Gallus gallus) annotates exactly 11 transmembrane helices at the positions listed in option D: TM0 47-71, TM1 139-171, TM2 196-220, TM3 421-450, TM4 466-495, TM5 500-536, TM6 560-592, TM7 613-631, TM8 635-659, TM9 667-695, TM10 701-721. The evidence codes are ECO:0000250 (similarity-based annotation from human ortholog Q3TWI9), so this is computational inference by homology rather than direct experimental determination, but the annotation is internally consistent and matches the sequence. Option D matches the annotation exactly.",
    "evidence_ids": ["C6", "C8", "C10", "C12", "C14", "C16", "C18", "C20", "C22", "C24", "C26"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Option C uses uniformly 20-residue windows at roughly regular intervals, which contradicts the well-known variability in TM helix lengths (typically 18-30+ residues) and the irregular spacing dictated by actual hydrophobic stretches; a sliding-window hydrophobicity analysis immediately eliminates C. Option A omits the TM6 region at 560-592; examining the sequence between the end of TM5 (~536) and the cytoplasmic loop at 593-612 reveals a clearly hydrophobic stretch of ~33 residues consistent with a membrane-spanning helix, so a model performing hydrophobicity profiling can identify this region and eliminate A. The remaining distinction between B and D is a 2-residue boundary shift in TM9 (669-693 vs 667-695). A model examining the hydrophobicity profile at those exact boundaries could note whether residues at positions 667-668 and 694-695 are hydrophobic (supporting D's wider helix) or hydrophilic (supporting B's narrower helix). While this 2-residue difference is within the typical uncertainty of TM boundary prediction, the overall reasoning path—identifying 11 hydrophobic segments of varying lengths at approximately the right positions—meaningfully distinguishes D from A and C, and provides a defensible (if not certain) basis for preferring D over B.",
    "missing_item_specific_fact": "",
    "reason": "The primary reasoning path (hydrophobicity analysis to identify ~11 TM segments of varying length, eliminating C's uniform windows and A's missing TM6) is well-supported by transferable knowledge of membrane protein topology. The B-vs-D distinction involves only a 2-residue boundary shift in TM9, which is subtle but can be approached by examining local hydrophobicity at those positions. The question is answerable through sequence-based reasoning without needing to recall this protein's specific database record."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "D"],
    "reason": "Options B and D differ only in the TM9 boundaries: B gives 669-693 (25 residues) while D gives 667-695 (29 residues). A 2-residue shift at each boundary is within the typical uncertainty of TM helix boundary prediction from sequence alone. Without precise knowledge of where the hydrophobic stretch begins and ends at those exact positions, a model could reasonably select either option. The UniProt annotation supports D, but the sequence-based reasoning margin between B and D is very narrow."
  },
  "important_caveats": [
    "All UniProt TM annotations for this entry carry evidence code ECO:0000250 (similarity to Q3TWI9, human TMEM63B), meaning they are computational inferences by homology rather than experimentally determined boundaries.",
    "The 2-residue boundary difference between options B and D (TM9: 669-693 vs 667-695) is within the typical error range of TM prediction algorithms, making this the weakest point of the question's discriminability.",
    "The reviewer-only evidence was not available to the evaluated model; the reasoning assessment is based solely on the original sequence and answer choices."
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

> Exact-match historical features annotate keyD, including667..695 with similarity evidence. OptionB narrows it to669..693;701..721 remains the final interval in both.

**Remaining uncertainty:** The source establishes the keyed coordinates but does not independently validate the narrowed alternative. The model calls the differing interval the final helix, although it is penultimate in the listed coordinate set.

Evidence checked: [H4](#evidence-h4), [H6](#evidence-h6), [H8](#evidence-h8), [H10](#evidence-h10), [H12](#evidence-h12), [H14](#evidence-h14), [H16](#evidence-h16), [H18](#evidence-h18), [H20](#evidence-h20), [H22](#evidence-h22), [H24](#evidence-h24).

## Complete reviewer-only evidence and qualifications

All excerpts supplied in the original and revised reviewer user message follow. This material was not available to the original evaluated model. Accession identity came from dataset image-path metadata. Source support and transferable discrimination are separate judgments.

**Applicability metadata, unchanged:**

```json
{
  "requested_accession": "A0A8V0ZB02",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "benchmark_sequence_sha256": "78ed17aad829cd9ff2c762ae9fcbd73ccfa275b6ddb7d47e552a86dc2ac5e435",
  "benchmark_sequence_length": 816,
  "current_status": "retrieved",
  "current_sequence_comparison": "matched",
  "current_entry_audit": {
    "entryVersion": 18,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2022-12-14",
    "sequenceVersion": 1
  },
  "current_uniprot_release": "2026_03",
  "current_record_sha256": "2a70bd6be844793f85a89646f4b0890123b0430bff08bb408f761d9ee7d44c74",
  "current_source_sequence_sha256": "78ed17aad829cd9ff2c762ae9fcbd73ccfa275b6ddb7d47e552a86dc2ac5e435",
  "current_source_sequence_length": 816,
  "historical_status": "retrieved",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "selected_historical_entry_version": 16,
  "selected_historical_version": {
    "accession": "A0A8V0ZB02",
    "database": "Swiss-Prot",
    "entryVersion": 16,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "TM63B_CHICK",
    "sequenceVersion": 1
  },
  "selected_historical_record_sha256": "098fa8177aa78ced176ae350c71e2c32a9c01620a23e7c5f32ac21455a5f8704",
  "selected_historical_source_sequence_sha256": "78ed17aad829cd9ff2c762ae9fcbd73ccfa275b6ddb7d47e552a86dc2ac5e435",
  "selected_historical_source_sequence_length": 816,
  "latest_at_cutoff_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 16,
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8V0ZB02.json)

```json
{
  "evidence_id": "C1",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8V0ZB02.json",
  "source_sha256": "2a70bd6be844793f85a89646f4b0890123b0430bff08bb408f761d9ee7d44c74",
  "retrieved_utc": "2026-11-01T06:24:51.590118+00:00",
  "json_pointer": "/primaryAccession",
  "excerpt": "\"A0A8V0ZB02\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8V0ZB02.json)

```json
{
  "evidence_id": "C2",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8V0ZB02.json",
  "source_sha256": "2a70bd6be844793f85a89646f4b0890123b0430bff08bb408f761d9ee7d44c74",
  "retrieved_utc": "2026-11-01T06:24:51.590118+00:00",
  "json_pointer": "/entryAudit",
  "excerpt": "{\"entryVersion\":18,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2022-12-14\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8V0ZB02.json)

```json
{
  "evidence_id": "C3",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8V0ZB02.json",
  "source_sha256": "2a70bd6be844793f85a89646f4b0890123b0430bff08bb408f761d9ee7d44c74",
  "retrieved_utc": "2026-11-01T06:24:51.590118+00:00",
  "json_pointer": "/organism",
  "excerpt": "{\"commonName\":\"Chicken\",\"lineage\":[\"Eukaryota\",\"Metazoa\",\"Chordata\",\"Craniata\",\"Vertebrata\",\"Euteleostomi\",\"Archelosauria\",\"Archosauria\",\"Dinosauria\",\"Saurischia\",\"Theropoda\",\"Coelurosauria\",\"Aves\",\"Neognathae\",\"Galloanserae\",\"Galliformes\",\"Phasianidae\",\"Phasianinae\",\"Gallus\"],\"scientificName\":\"Gallus gallus\",\"taxonId\":9031}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8V0ZB02.json)

```json
{
  "evidence_id": "C4",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8V0ZB02.json",
  "source_sha256": "2a70bd6be844793f85a89646f4b0890123b0430bff08bb408f761d9ee7d44c74",
  "retrieved_utc": "2026-11-01T06:24:51.590118+00:00",
  "json_pointer": "/proteinDescription",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39716028\",\"source\":\"PubMed\"}],\"value\":\"Transmembrane protein 63B\"}}],\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Mechanosensitive cation channel TMEM63B\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8V0ZB02.json)

```json
{
  "evidence_id": "C5",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8V0ZB02.json",
  "source_sha256": "2a70bd6be844793f85a89646f4b0890123b0430bff08bb408f761d9ee7d44c74",
  "retrieved_utc": "2026-11-01T06:24:51.590118+00:00",
  "json_pointer": "/features/1",
  "excerpt": "{\"description\":\"Extracellular\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q3TWI9\",\"source\":\"UniProtKB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":46},\"start\":{\"modifier\":\"EXACT\",\"value\":1}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8V0ZB02.json)

```json
{
  "evidence_id": "C6",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8V0ZB02.json",
  "source_sha256": "2a70bd6be844793f85a89646f4b0890123b0430bff08bb408f761d9ee7d44c74",
  "retrieved_utc": "2026-11-01T06:24:51.590118+00:00",
  "json_pointer": "/features/2",
  "excerpt": "{\"description\":\"Helical; Name=TM0\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q3TWI9\",\"source\":\"UniProtKB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":71},\"start\":{\"modifier\":\"EXACT\",\"value\":47}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8V0ZB02.json)

```json
{
  "evidence_id": "C7",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8V0ZB02.json",
  "source_sha256": "2a70bd6be844793f85a89646f4b0890123b0430bff08bb408f761d9ee7d44c74",
  "retrieved_utc": "2026-11-01T06:24:51.590118+00:00",
  "json_pointer": "/features/3",
  "excerpt": "{\"description\":\"Cytoplasmic\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q3TWI9\",\"source\":\"UniProtKB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":138},\"start\":{\"modifier\":\"EXACT\",\"value\":72}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8V0ZB02.json)

```json
{
  "evidence_id": "C8",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8V0ZB02.json",
  "source_sha256": "2a70bd6be844793f85a89646f4b0890123b0430bff08bb408f761d9ee7d44c74",
  "retrieved_utc": "2026-11-01T06:24:51.590118+00:00",
  "json_pointer": "/features/4",
  "excerpt": "{\"description\":\"Helical; Name=TM1\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q3TWI9\",\"source\":\"UniProtKB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":171},\"start\":{\"modifier\":\"EXACT\",\"value\":139}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8V0ZB02.json)

```json
{
  "evidence_id": "C9",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8V0ZB02.json",
  "source_sha256": "2a70bd6be844793f85a89646f4b0890123b0430bff08bb408f761d9ee7d44c74",
  "retrieved_utc": "2026-11-01T06:24:51.590118+00:00",
  "json_pointer": "/features/5",
  "excerpt": "{\"description\":\"Extracellular\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q3TWI9\",\"source\":\"UniProtKB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":195},\"start\":{\"modifier\":\"EXACT\",\"value\":172}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8V0ZB02.json)

```json
{
  "evidence_id": "C10",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8V0ZB02.json",
  "source_sha256": "2a70bd6be844793f85a89646f4b0890123b0430bff08bb408f761d9ee7d44c74",
  "retrieved_utc": "2026-11-01T06:24:51.590118+00:00",
  "json_pointer": "/features/6",
  "excerpt": "{\"description\":\"Helical; Name=TM2\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q3TWI9\",\"source\":\"UniProtKB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":220},\"start\":{\"modifier\":\"EXACT\",\"value\":196}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8V0ZB02.json)

```json
{
  "evidence_id": "C11",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8V0ZB02.json",
  "source_sha256": "2a70bd6be844793f85a89646f4b0890123b0430bff08bb408f761d9ee7d44c74",
  "retrieved_utc": "2026-11-01T06:24:51.590118+00:00",
  "json_pointer": "/features/7",
  "excerpt": "{\"description\":\"Cytoplasmic\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q3TWI9\",\"source\":\"UniProtKB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":420},\"start\":{\"modifier\":\"EXACT\",\"value\":221}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8V0ZB02.json)

```json
{
  "evidence_id": "C12",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8V0ZB02.json",
  "source_sha256": "2a70bd6be844793f85a89646f4b0890123b0430bff08bb408f761d9ee7d44c74",
  "retrieved_utc": "2026-11-01T06:24:51.590118+00:00",
  "json_pointer": "/features/8",
  "excerpt": "{\"description\":\"Helical; Name=TM3\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q3TWI9\",\"source\":\"UniProtKB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":450},\"start\":{\"modifier\":\"EXACT\",\"value\":421}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C13

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8V0ZB02.json)

```json
{
  "evidence_id": "C13",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8V0ZB02.json",
  "source_sha256": "2a70bd6be844793f85a89646f4b0890123b0430bff08bb408f761d9ee7d44c74",
  "retrieved_utc": "2026-11-01T06:24:51.590118+00:00",
  "json_pointer": "/features/9",
  "excerpt": "{\"description\":\"Extracellular\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q3TWI9\",\"source\":\"UniProtKB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":465},\"start\":{\"modifier\":\"EXACT\",\"value\":451}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C14

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8V0ZB02.json)

```json
{
  "evidence_id": "C14",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8V0ZB02.json",
  "source_sha256": "2a70bd6be844793f85a89646f4b0890123b0430bff08bb408f761d9ee7d44c74",
  "retrieved_utc": "2026-11-01T06:24:51.590118+00:00",
  "json_pointer": "/features/10",
  "excerpt": "{\"description\":\"Helical; Name=TM4\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q3TWI9\",\"source\":\"UniProtKB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":495},\"start\":{\"modifier\":\"EXACT\",\"value\":466}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C15

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8V0ZB02.json)

```json
{
  "evidence_id": "C15",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8V0ZB02.json",
  "source_sha256": "2a70bd6be844793f85a89646f4b0890123b0430bff08bb408f761d9ee7d44c74",
  "retrieved_utc": "2026-11-01T06:24:51.590118+00:00",
  "json_pointer": "/features/11",
  "excerpt": "{\"description\":\"Cytoplasmic\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q3TWI9\",\"source\":\"UniProtKB\"},{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":499},\"start\":{\"modifier\":\"EXACT\",\"value\":496}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C16

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8V0ZB02.json)

```json
{
  "evidence_id": "C16",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8V0ZB02.json",
  "source_sha256": "2a70bd6be844793f85a89646f4b0890123b0430bff08bb408f761d9ee7d44c74",
  "retrieved_utc": "2026-11-01T06:24:51.590118+00:00",
  "json_pointer": "/features/12",
  "excerpt": "{\"description\":\"Helical; Name=TM5\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q3TWI9\",\"source\":\"UniProtKB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":536},\"start\":{\"modifier\":\"EXACT\",\"value\":500}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C17

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8V0ZB02.json)

```json
{
  "evidence_id": "C17",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8V0ZB02.json",
  "source_sha256": "2a70bd6be844793f85a89646f4b0890123b0430bff08bb408f761d9ee7d44c74",
  "retrieved_utc": "2026-11-01T06:24:51.590118+00:00",
  "json_pointer": "/features/13",
  "excerpt": "{\"description\":\"Extracellular\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q3TWI9\",\"source\":\"UniProtKB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":559},\"start\":{\"modifier\":\"EXACT\",\"value\":537}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C18

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8V0ZB02.json)

```json
{
  "evidence_id": "C18",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8V0ZB02.json",
  "source_sha256": "2a70bd6be844793f85a89646f4b0890123b0430bff08bb408f761d9ee7d44c74",
  "retrieved_utc": "2026-11-01T06:24:51.590118+00:00",
  "json_pointer": "/features/14",
  "excerpt": "{\"description\":\"Helical; Name=TM6\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q3TWI9\",\"source\":\"UniProtKB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":592},\"start\":{\"modifier\":\"EXACT\",\"value\":560}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C19

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8V0ZB02.json)

```json
{
  "evidence_id": "C19",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8V0ZB02.json",
  "source_sha256": "2a70bd6be844793f85a89646f4b0890123b0430bff08bb408f761d9ee7d44c74",
  "retrieved_utc": "2026-11-01T06:24:51.590118+00:00",
  "json_pointer": "/features/15",
  "excerpt": "{\"description\":\"Cytoplasmic\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q3TWI9\",\"source\":\"UniProtKB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":612},\"start\":{\"modifier\":\"EXACT\",\"value\":593}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C20

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8V0ZB02.json)

```json
{
  "evidence_id": "C20",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8V0ZB02.json",
  "source_sha256": "2a70bd6be844793f85a89646f4b0890123b0430bff08bb408f761d9ee7d44c74",
  "retrieved_utc": "2026-11-01T06:24:51.590118+00:00",
  "json_pointer": "/features/16",
  "excerpt": "{\"description\":\"Helical; Name=TM7\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q3TWI9\",\"source\":\"UniProtKB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":631},\"start\":{\"modifier\":\"EXACT\",\"value\":613}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C21

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8V0ZB02.json)

```json
{
  "evidence_id": "C21",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8V0ZB02.json",
  "source_sha256": "2a70bd6be844793f85a89646f4b0890123b0430bff08bb408f761d9ee7d44c74",
  "retrieved_utc": "2026-11-01T06:24:51.590118+00:00",
  "json_pointer": "/features/17",
  "excerpt": "{\"description\":\"Extracellular\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q3TWI9\",\"source\":\"UniProtKB\"},{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":634},\"start\":{\"modifier\":\"EXACT\",\"value\":632}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C22

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8V0ZB02.json)

```json
{
  "evidence_id": "C22",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8V0ZB02.json",
  "source_sha256": "2a70bd6be844793f85a89646f4b0890123b0430bff08bb408f761d9ee7d44c74",
  "retrieved_utc": "2026-11-01T06:24:51.590118+00:00",
  "json_pointer": "/features/18",
  "excerpt": "{\"description\":\"Helical; Name=TM8\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q3TWI9\",\"source\":\"UniProtKB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":659},\"start\":{\"modifier\":\"EXACT\",\"value\":635}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C23

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8V0ZB02.json)

```json
{
  "evidence_id": "C23",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8V0ZB02.json",
  "source_sha256": "2a70bd6be844793f85a89646f4b0890123b0430bff08bb408f761d9ee7d44c74",
  "retrieved_utc": "2026-11-01T06:24:51.590118+00:00",
  "json_pointer": "/features/19",
  "excerpt": "{\"description\":\"Cytoplasmic\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q3TWI9\",\"source\":\"UniProtKB\"},{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":666},\"start\":{\"modifier\":\"EXACT\",\"value\":660}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C24

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8V0ZB02.json)

```json
{
  "evidence_id": "C24",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8V0ZB02.json",
  "source_sha256": "2a70bd6be844793f85a89646f4b0890123b0430bff08bb408f761d9ee7d44c74",
  "retrieved_utc": "2026-11-01T06:24:51.590118+00:00",
  "json_pointer": "/features/20",
  "excerpt": "{\"description\":\"Helical; Name=TM9\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q3TWI9\",\"source\":\"UniProtKB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":695},\"start\":{\"modifier\":\"EXACT\",\"value\":667}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C25

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8V0ZB02.json)

```json
{
  "evidence_id": "C25",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8V0ZB02.json",
  "source_sha256": "2a70bd6be844793f85a89646f4b0890123b0430bff08bb408f761d9ee7d44c74",
  "retrieved_utc": "2026-11-01T06:24:51.590118+00:00",
  "json_pointer": "/features/21",
  "excerpt": "{\"description\":\"Extracellular\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q3TWI9\",\"source\":\"UniProtKB\"},{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":700},\"start\":{\"modifier\":\"EXACT\",\"value\":696}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C26

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8V0ZB02.json)

```json
{
  "evidence_id": "C26",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8V0ZB02.json",
  "source_sha256": "2a70bd6be844793f85a89646f4b0890123b0430bff08bb408f761d9ee7d44c74",
  "retrieved_utc": "2026-11-01T06:24:51.590118+00:00",
  "json_pointer": "/features/22",
  "excerpt": "{\"description\":\"Helical; Name=TM10\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q3TWI9\",\"source\":\"UniProtKB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":721},\"start\":{\"modifier\":\"EXACT\",\"value\":701}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C27

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8V0ZB02.json)

```json
{
  "evidence_id": "C27",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8V0ZB02.json",
  "source_sha256": "2a70bd6be844793f85a89646f4b0890123b0430bff08bb408f761d9ee7d44c74",
  "retrieved_utc": "2026-11-01T06:24:51.590118+00:00",
  "json_pointer": "/features/23",
  "excerpt": "{\"description\":\"Cytoplasmic\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q3TWI9\",\"source\":\"UniProtKB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":816},\"start\":{\"modifier\":\"EXACT\",\"value\":722}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C28

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8V0ZB02.json)

```json
{
  "evidence_id": "C28",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8V0ZB02.json",
  "source_sha256": "2a70bd6be844793f85a89646f4b0890123b0430bff08bb408f761d9ee7d44c74",
  "retrieved_utc": "2026-11-01T06:24:51.590118+00:00",
  "json_pointer": "/references/1",
  "excerpt": "{\"citation\":{\"authors\":[\"Miyata Y.\",\"Nishimura M.\",\"Nagata A.\",\"Jing X.\",\"Sultan C.S.\",\"Kuribayashi R.\",\"Takahashi K.\",\"Lee Y.\",\"Nishizawa T.\",\"Segawa K.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"39716028\"},{\"database\":\"DOI\",\"id\":\"10.1002/1873-3468.15084\"}],\"citationType\":\"journal article\",\"firstPage\":\"0\",\"id\":\"39716028\",\"journal\":\"FEBS Lett.\",\"lastPage\":\"0\",\"publicationDate\":\"2024\",\"title\":\"Membrane structure-responsive lipid scramblase activity of the TMEM63/OSCA family.\",\"volume\":\"0\"},\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8V0ZB02?format=txt&versions=16)

```json
{
  "evidence_id": "H1",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A8V0ZB02?format=txt&versions=16",
  "source_sha256": "098fa8177aa78ced176ae350c71e2c32a9c01620a23e7c5f32ac21455a5f8704",
  "retrieved_utc": "2026-11-01T06:27:36.055628+00:00",
  "source_locator": "lines 1-14",
  "excerpt": "ID   TM63B_CHICK             Reviewed;         816 AA.\nAC   A0A8V0ZB02;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   14-DEC-2022, sequence version 1.\nDT   28-JAN-2026, entry version 16.\nDE   RecName: Full=Mechanosensitive cation channel TMEM63B {ECO:0000305};\nDE   AltName: Full=Transmembrane protein 63B {ECO:0000303|PubMed:39716028};\nGN   Name=TMEM63B {ECO:0000303|PubMed:39716028};\nOS   Gallus gallus (Chicken).\nOC   Eukaryota; Metazoa; Chordata; Craniata; Vertebrata; Euteleostomi;\nOC   Archelosauria; Archosauria; Dinosauria; Saurischia; Theropoda;\nOC   Coelurosauria; Aves; Neognathae; Galloanserae; Galliformes; Phasianidae;\nOC   Phasianinae; Gallus.\nOX   NCBI_TaxID=9031;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 16,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8V0ZB02?format=txt&versions=16)

```json
{
  "evidence_id": "H2",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A8V0ZB02?format=txt&versions=16",
  "source_sha256": "098fa8177aa78ced176ae350c71e2c32a9c01620a23e7c5f32ac21455a5f8704",
  "retrieved_utc": "2026-11-01T06:27:36.055628+00:00",
  "source_locator": "lines 55-62",
  "excerpt": "RN   [2]\nRP   FUNCTION.\nRX   PubMed=39716028; DOI=10.1002/1873-3468.15084;\nRA   Miyata Y., Nishimura M., Nagata A., Jing X., Sultan C.S., Kuribayashi R.,\nRA   Takahashi K., Lee Y., Nishizawa T., Segawa K.;\nRT   \"Membrane structure-responsive lipid scramblase activity of the TMEM63/OSCA\nRT   family.\";\nRL   FEBS Lett. 0:0-0(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 16,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8V0ZB02?format=txt&versions=16)

```json
{
  "evidence_id": "H3",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A8V0ZB02?format=txt&versions=16",
  "source_sha256": "098fa8177aa78ced176ae350c71e2c32a9c01620a23e7c5f32ac21455a5f8704",
  "retrieved_utc": "2026-11-01T06:27:36.055628+00:00",
  "source_locator": "lines 134-136",
  "excerpt": "FT   TOPO_DOM        1..46\nFT                   /note=\"Extracellular\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q3TWI9\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 16,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8V0ZB02?format=txt&versions=16)

```json
{
  "evidence_id": "H4",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A8V0ZB02?format=txt&versions=16",
  "source_sha256": "098fa8177aa78ced176ae350c71e2c32a9c01620a23e7c5f32ac21455a5f8704",
  "retrieved_utc": "2026-11-01T06:27:36.055628+00:00",
  "source_locator": "lines 137-139",
  "excerpt": "FT   TRANSMEM        47..71\nFT                   /note=\"Helical; Name=TM0\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q3TWI9\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 16,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8V0ZB02?format=txt&versions=16)

```json
{
  "evidence_id": "H5",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A8V0ZB02?format=txt&versions=16",
  "source_sha256": "098fa8177aa78ced176ae350c71e2c32a9c01620a23e7c5f32ac21455a5f8704",
  "retrieved_utc": "2026-11-01T06:27:36.055628+00:00",
  "source_locator": "lines 140-142",
  "excerpt": "FT   TOPO_DOM        72..138\nFT                   /note=\"Cytoplasmic\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q3TWI9\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 16,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8V0ZB02?format=txt&versions=16)

```json
{
  "evidence_id": "H6",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A8V0ZB02?format=txt&versions=16",
  "source_sha256": "098fa8177aa78ced176ae350c71e2c32a9c01620a23e7c5f32ac21455a5f8704",
  "retrieved_utc": "2026-11-01T06:27:36.055628+00:00",
  "source_locator": "lines 143-145",
  "excerpt": "FT   TRANSMEM        139..171\nFT                   /note=\"Helical; Name=TM1\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q3TWI9\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 16,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8V0ZB02?format=txt&versions=16)

```json
{
  "evidence_id": "H7",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A8V0ZB02?format=txt&versions=16",
  "source_sha256": "098fa8177aa78ced176ae350c71e2c32a9c01620a23e7c5f32ac21455a5f8704",
  "retrieved_utc": "2026-11-01T06:27:36.055628+00:00",
  "source_locator": "lines 146-148",
  "excerpt": "FT   TOPO_DOM        172..195\nFT                   /note=\"Extracellular\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q3TWI9\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 16,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8V0ZB02?format=txt&versions=16)

```json
{
  "evidence_id": "H8",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A8V0ZB02?format=txt&versions=16",
  "source_sha256": "098fa8177aa78ced176ae350c71e2c32a9c01620a23e7c5f32ac21455a5f8704",
  "retrieved_utc": "2026-11-01T06:27:36.055628+00:00",
  "source_locator": "lines 149-151",
  "excerpt": "FT   TRANSMEM        196..220\nFT                   /note=\"Helical; Name=TM2\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q3TWI9\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 16,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8V0ZB02?format=txt&versions=16)

```json
{
  "evidence_id": "H9",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A8V0ZB02?format=txt&versions=16",
  "source_sha256": "098fa8177aa78ced176ae350c71e2c32a9c01620a23e7c5f32ac21455a5f8704",
  "retrieved_utc": "2026-11-01T06:27:36.055628+00:00",
  "source_locator": "lines 152-154",
  "excerpt": "FT   TOPO_DOM        221..420\nFT                   /note=\"Cytoplasmic\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q3TWI9\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 16,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H10

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8V0ZB02?format=txt&versions=16)

```json
{
  "evidence_id": "H10",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A8V0ZB02?format=txt&versions=16",
  "source_sha256": "098fa8177aa78ced176ae350c71e2c32a9c01620a23e7c5f32ac21455a5f8704",
  "retrieved_utc": "2026-11-01T06:27:36.055628+00:00",
  "source_locator": "lines 155-157",
  "excerpt": "FT   TRANSMEM        421..450\nFT                   /note=\"Helical; Name=TM3\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q3TWI9\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 16,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H11

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8V0ZB02?format=txt&versions=16)

```json
{
  "evidence_id": "H11",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A8V0ZB02?format=txt&versions=16",
  "source_sha256": "098fa8177aa78ced176ae350c71e2c32a9c01620a23e7c5f32ac21455a5f8704",
  "retrieved_utc": "2026-11-01T06:27:36.055628+00:00",
  "source_locator": "lines 158-160",
  "excerpt": "FT   TOPO_DOM        451..465\nFT                   /note=\"Extracellular\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q3TWI9\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 16,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H12

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8V0ZB02?format=txt&versions=16)

```json
{
  "evidence_id": "H12",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A8V0ZB02?format=txt&versions=16",
  "source_sha256": "098fa8177aa78ced176ae350c71e2c32a9c01620a23e7c5f32ac21455a5f8704",
  "retrieved_utc": "2026-11-01T06:27:36.055628+00:00",
  "source_locator": "lines 161-163",
  "excerpt": "FT   TRANSMEM        466..495\nFT                   /note=\"Helical; Name=TM4\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q3TWI9\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 16,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H13

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8V0ZB02?format=txt&versions=16)

```json
{
  "evidence_id": "H13",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A8V0ZB02?format=txt&versions=16",
  "source_sha256": "098fa8177aa78ced176ae350c71e2c32a9c01620a23e7c5f32ac21455a5f8704",
  "retrieved_utc": "2026-11-01T06:27:36.055628+00:00",
  "source_locator": "lines 164-166",
  "excerpt": "FT   TOPO_DOM        496..499\nFT                   /note=\"Cytoplasmic\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q3TWI9, ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 16,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H14

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8V0ZB02?format=txt&versions=16)

```json
{
  "evidence_id": "H14",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A8V0ZB02?format=txt&versions=16",
  "source_sha256": "098fa8177aa78ced176ae350c71e2c32a9c01620a23e7c5f32ac21455a5f8704",
  "retrieved_utc": "2026-11-01T06:27:36.055628+00:00",
  "source_locator": "lines 167-169",
  "excerpt": "FT   TRANSMEM        500..536\nFT                   /note=\"Helical; Name=TM5\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q3TWI9\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 16,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H15

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8V0ZB02?format=txt&versions=16)

```json
{
  "evidence_id": "H15",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A8V0ZB02?format=txt&versions=16",
  "source_sha256": "098fa8177aa78ced176ae350c71e2c32a9c01620a23e7c5f32ac21455a5f8704",
  "retrieved_utc": "2026-11-01T06:27:36.055628+00:00",
  "source_locator": "lines 170-172",
  "excerpt": "FT   TOPO_DOM        537..559\nFT                   /note=\"Extracellular\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q3TWI9\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 16,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H16

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8V0ZB02?format=txt&versions=16)

```json
{
  "evidence_id": "H16",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A8V0ZB02?format=txt&versions=16",
  "source_sha256": "098fa8177aa78ced176ae350c71e2c32a9c01620a23e7c5f32ac21455a5f8704",
  "retrieved_utc": "2026-11-01T06:27:36.055628+00:00",
  "source_locator": "lines 173-175",
  "excerpt": "FT   TRANSMEM        560..592\nFT                   /note=\"Helical; Name=TM6\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q3TWI9\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 16,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H17

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8V0ZB02?format=txt&versions=16)

```json
{
  "evidence_id": "H17",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A8V0ZB02?format=txt&versions=16",
  "source_sha256": "098fa8177aa78ced176ae350c71e2c32a9c01620a23e7c5f32ac21455a5f8704",
  "retrieved_utc": "2026-11-01T06:27:36.055628+00:00",
  "source_locator": "lines 176-178",
  "excerpt": "FT   TOPO_DOM        593..612\nFT                   /note=\"Cytoplasmic\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q3TWI9\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 16,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H18

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8V0ZB02?format=txt&versions=16)

```json
{
  "evidence_id": "H18",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A8V0ZB02?format=txt&versions=16",
  "source_sha256": "098fa8177aa78ced176ae350c71e2c32a9c01620a23e7c5f32ac21455a5f8704",
  "retrieved_utc": "2026-11-01T06:27:36.055628+00:00",
  "source_locator": "lines 179-181",
  "excerpt": "FT   TRANSMEM        613..631\nFT                   /note=\"Helical; Name=TM7\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q3TWI9\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 16,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H19

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8V0ZB02?format=txt&versions=16)

```json
{
  "evidence_id": "H19",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A8V0ZB02?format=txt&versions=16",
  "source_sha256": "098fa8177aa78ced176ae350c71e2c32a9c01620a23e7c5f32ac21455a5f8704",
  "retrieved_utc": "2026-11-01T06:27:36.055628+00:00",
  "source_locator": "lines 182-184",
  "excerpt": "FT   TOPO_DOM        632..634\nFT                   /note=\"Extracellular\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q3TWI9, ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 16,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H20

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8V0ZB02?format=txt&versions=16)

```json
{
  "evidence_id": "H20",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A8V0ZB02?format=txt&versions=16",
  "source_sha256": "098fa8177aa78ced176ae350c71e2c32a9c01620a23e7c5f32ac21455a5f8704",
  "retrieved_utc": "2026-11-01T06:27:36.055628+00:00",
  "source_locator": "lines 185-187",
  "excerpt": "FT   TRANSMEM        635..659\nFT                   /note=\"Helical; Name=TM8\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q3TWI9\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 16,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H21

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8V0ZB02?format=txt&versions=16)

```json
{
  "evidence_id": "H21",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A8V0ZB02?format=txt&versions=16",
  "source_sha256": "098fa8177aa78ced176ae350c71e2c32a9c01620a23e7c5f32ac21455a5f8704",
  "retrieved_utc": "2026-11-01T06:27:36.055628+00:00",
  "source_locator": "lines 188-190",
  "excerpt": "FT   TOPO_DOM        660..666\nFT                   /note=\"Cytoplasmic\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q3TWI9, ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 16,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H22

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8V0ZB02?format=txt&versions=16)

```json
{
  "evidence_id": "H22",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A8V0ZB02?format=txt&versions=16",
  "source_sha256": "098fa8177aa78ced176ae350c71e2c32a9c01620a23e7c5f32ac21455a5f8704",
  "retrieved_utc": "2026-11-01T06:27:36.055628+00:00",
  "source_locator": "lines 191-193",
  "excerpt": "FT   TRANSMEM        667..695\nFT                   /note=\"Helical; Name=TM9\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q3TWI9\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 16,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H23

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8V0ZB02?format=txt&versions=16)

```json
{
  "evidence_id": "H23",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A8V0ZB02?format=txt&versions=16",
  "source_sha256": "098fa8177aa78ced176ae350c71e2c32a9c01620a23e7c5f32ac21455a5f8704",
  "retrieved_utc": "2026-11-01T06:27:36.055628+00:00",
  "source_locator": "lines 194-196",
  "excerpt": "FT   TOPO_DOM        696..700\nFT                   /note=\"Extracellular\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q3TWI9, ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 16,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H24

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8V0ZB02?format=txt&versions=16)

```json
{
  "evidence_id": "H24",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A8V0ZB02?format=txt&versions=16",
  "source_sha256": "098fa8177aa78ced176ae350c71e2c32a9c01620a23e7c5f32ac21455a5f8704",
  "retrieved_utc": "2026-11-01T06:27:36.055628+00:00",
  "source_locator": "lines 197-199",
  "excerpt": "FT   TRANSMEM        701..721\nFT                   /note=\"Helical; Name=TM10\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q3TWI9\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 16,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H25

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8V0ZB02?format=txt&versions=16)

```json
{
  "evidence_id": "H25",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A8V0ZB02?format=txt&versions=16",
  "source_sha256": "098fa8177aa78ced176ae350c71e2c32a9c01620a23e7c5f32ac21455a5f8704",
  "retrieved_utc": "2026-11-01T06:27:36.055628+00:00",
  "source_locator": "lines 200-202",
  "excerpt": "FT   TOPO_DOM        722..816\nFT                   /note=\"Cytoplasmic\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q3TWI9\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 16,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json), zero-based source row 34. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
