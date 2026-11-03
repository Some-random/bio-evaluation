# transmembrane_0062: before and after transfer clarification

[All 1,328 cases](../README.md) · [Method](../METHOD.md) · [Summary](../SUMMARY.md) · [Exact reviewer user message](../inputs/transmembrane_0062.txt)

**Task:** `transmembrane`  
**Author key, unchanged:** **A** — 27..47; 78..98; 108..128; 136..156; 173..193; 209..229; 337..357; 366..386; 400..420; 432..452; 465..485

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
MSSHTSTPNHASAAPPRKWYDMTSAEFYVYVVAFMCGISMLMPINAVFSAPSYMLQYYLYATKDPNHVPQMTNFWSNVMTYYNLIGLVTGLVMEPLTLLKSFRKIPMLVRLLGGLCILIVEIIVLMAVPARGTTEGGAVATMCIAGFIGGLGKSIFESTVYGMFGAFPPSFTSIMMGGVGISGVLTSLIQIIVKAALPDTYEGVKKQSYIYYSLDVGIQAATFIALIMMRFNSFAQLHFGDLGGVKSKVDAGSLAGAGENVREPGAEATELEQYTEPAIGQIQEKNAEAHKDDPLVDREHSDDVDEHGDALRAVEGPTSNEILRATSIISVLRSIKWMFVSCAFVFVVTLFLFPGIATGMFPESKWFATVAVFIFNCCDVLGRVAPALRFMWPRSYNQRWIIVAASFARVIFVPLLLLYSYHYIPSEAYGYVIMVIFGFSSGYVASMSLTLGPQSKGIDNDGKRFVAGTLMGISILVGGTIGTVLSIMTQTIREKY

[Multiple Choices]
A. 27..47; 78..98; 108..128; 136..156; 173..193; 209..229; 337..357; 366..386; 400..420; 432..452; 465..485
B. 93..113; 163..183; 382..402; 425..445; 764..784
C. 27..47; 78..98; 108..128; 136..156; 173..193; 209..229; 337..357; 400..420; 432..452; 465..485
D. 27..47; 78..98; 108..128; 136..156; 173..193; 209..229; 337..357; 366..386; 400..420; 436..447; 465..485
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

> The sequence matches the cited UniProt record, whose annotated transmembrane intervals correspond exactly to Choice A. The helix features carry computational evidence code ECO:0000255, so this supports the key as an annotation-based prediction, not as direct experimental mapping of membrane boundaries.

Citations as saved: [C6](#evidence-c6), [C8](#evidence-c8), [C10](#evidence-c10), [C12](#evidence-c12), [C14](#evidence-c14), [C16](#evidence-c16), [C18](#evidence-c18), [C20](#evidence-c20), [C22](#evidence-c22), [C24](#evidence-c24), [C26](#evidence-c26).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence has many strongly hydrophobic stretches, consistent with a multipass membrane protein, so general sequence reasoning can identify likely transmembrane helices in broad terms.


**Missing item-specific fact**

> Selecting the exact listed intervals requires protein-specific transmembrane boundary annotations or equivalent detailed topology predictions; generic hydropathy reasoning does not reliably distinguish the precise endpoints in these choices.


**Reason**

> The input provides sequence but no protein identity, topology annotation, or experimental boundary data. The near-identical choices differ in specific helix inclusion or endpoint placement, which is an item-specific fact rather than a conclusion established by general biological reasoning alone.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Under the supplied annotation coordinates, only Choice A lists all the annotated transmembrane intervals. Actual membrane boundaries can be less exact than annotation coordinates, but the choices do not establish another full set of equivalent intervals.


### Important caveats

- The supporting UniProt annotations are reviewer-only and were not available in the question input.
- The transmembrane annotations are computationally supported rather than shown here to be experimentally measured; the author’s original source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has many strongly hydrophobic stretches, consistent with a multipass membrane protein, so general sequence reasoning can identify likely transmembrane helices in broad terms.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "Selecting the exact listed intervals requires protein-specific transmembrane boundary annotations or equivalent detailed topology predictions; generic hydropathy reasoning does not reliably distinguish the precise endpoints in these choices.",
    "reason": "The input provides sequence but no protein identity, topology annotation, or experimental boundary data. The near-identical choices differ in specific helix inclusion or endpoint placement, which is an item-specific fact rather than a conclusion established by general biological reasoning alone."
  },
  "case_id": "transmembrane_0062",
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
    "reason": "The sequence matches the cited UniProt record, whose annotated transmembrane intervals correspond exactly to Choice A. The helix features carry computational evidence code ECO:0000255, so this supports the key as an annotation-based prediction, not as direct experimental mapping of membrane boundaries."
  },
  "important_caveats": [
    "The supporting UniProt annotations are reviewer-only and were not available in the question input.",
    "The transmembrane annotations are computationally supported rather than shown here to be experimentally measured; the author’s original source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Under the supplied annotation coordinates, only Choice A lists all the annotated transmembrane intervals. Actual membrane boundaries can be less exact than annotation coordinates, but the choices do not establish another full set of equivalent intervals."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0062",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches the cited UniProt record, whose annotated transmembrane intervals correspond exactly to Choice A. The helix features carry computational evidence code ECO:0000255, so this supports the key as an annotation-based prediction, not as direct experimental mapping of membrane boundaries.",
    "evidence_ids": ["C6", "C8", "C10", "C12", "C14", "C16", "C18", "C20", "C22", "C24", "C26"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence has many strongly hydrophobic stretches, consistent with a multipass membrane protein, so general sequence reasoning can identify likely transmembrane helices in broad terms.",
    "missing_item_specific_fact": "Selecting the exact listed intervals requires protein-specific transmembrane boundary annotations or equivalent detailed topology predictions; generic hydropathy reasoning does not reliably distinguish the precise endpoints in these choices.",
    "reason": "The input provides sequence but no protein identity, topology annotation, or experimental boundary data. The near-identical choices differ in specific helix inclusion or endpoint placement, which is an item-specific fact rather than a conclusion established by general biological reasoning alone."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Under the supplied annotation coordinates, only Choice A lists all the annotated transmembrane intervals. Actual membrane boundaries can be less exact than annotation coordinates, but the choices do not establish another full set of equivalent intervals."
  },
  "important_caveats": [
    "The supporting UniProt annotations are reviewer-only and were not available in the question input.",
    "The transmembrane annotations are computationally supported rather than shown here to be experimentally measured; the author’s original source snapshot is unknown."
  ]
}
```

</details>

## Before: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry J9UD11 (Adenosine transporter 1, CfAT1, from Crithidia fasciculata) annotates exactly 11 transmembrane helical regions at 27..47, 78..98, 108..128, 136..156, 173..193, 209..229, 337..357, 366..386, 400..420, 432..452, and 465..485, matching Choice A precisely. The evidence code ECO:0000255 indicates these are computational predictions by similarity, not experimentally determined boundaries, but the annotation is consistent and the sequence match is confirmed (SHA256 identical).

Citations as saved: [C6](#evidence-c6), [C8](#evidence-c8), [C10](#evidence-c10), [C12](#evidence-c12), [C14](#evidence-c14), [C16](#evidence-c16), [C18](#evidence-c18), [C20](#evidence-c20), [C22](#evidence-c22), [C24](#evidence-c24), [C26](#evidence-c26), [H4](#evidence-h4), [H6](#evidence-h6), [H8](#evidence-h8), [H10](#evidence-h10), [H12](#evidence-h12), [H14](#evidence-h14), [H16](#evidence-h16), [H18](#evidence-h18), [H20](#evidence-h20), [H22](#evidence-h22), [H24](#evidence-h24).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Three independent biological arguments distinguish A from the distractors: (1) Equilibrative nucleoside transporters (ENT family) are well-established to possess 11 transmembrane domains; this eliminates B (only 5 TM regions) and C (only 10 TM regions). (2) Choice B includes region 764..784, which exceeds the 496-residue protein length, making it physically impossible. (3) Choice D replaces the 432..452 segment (21 residues) with 436..447 (12 residues); a 12-residue hydrophobic stretch is too short to span a ~30 Å lipid bilayer as an alpha-helix (which requires approximately 19–25 hydrophobic residues), eliminating D on basic membrane-biophysics grounds.


**Missing item-specific fact**

> None that is strictly required. The ENT 11-TM topology is general family-level knowledge, and the minimum TM-helix length is basic membrane biology. Exact boundary assignment at the residue level is algorithm-dependent, but the multiple-choice format allows elimination by the length argument.


**Reason**

> The question can be answered by combining general knowledge of ENT family topology (11 TMs), a sanity check against protein length, and the biophysical requirement that a TM helix needs ~20 hydrophobic residues. These are general biological arguments, not item-specific database lookups.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> B is eliminated by exceeding protein length and by having only 5 TMs. C is eliminated by having only 10 TMs (inconsistent with ENT topology). D is eliminated by containing a 12-residue segment too short for a TM helix. Only A satisfies all biological constraints simultaneously.


### Important caveats

- All 11 TM annotations carry evidence code ECO:0000255 (by similarity), meaning they are computational predictions transferred from a homolog, not experimentally validated boundaries. Exact residue-level boundaries are inherently approximate.
- The distinction between A and D (432..452 vs 436..447) relies on a minimum-length argument; a model performing a simple hydrophobicity scan might not cleanly resolve a 4-residue boundary shift without careful analysis.
- The protein is from Crithidia fasciculata, a trypanosomatid; its membrane composition and hydrophobicity thresholds may differ slightly from mammalian references, though this does not affect the qualitative 11-TM topology argument.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Three independent biological arguments distinguish A from the distractors: (1) Equilibrative nucleoside transporters (ENT family) are well-established to possess 11 transmembrane domains; this eliminates B (only 5 TM regions) and C (only 10 TM regions). (2) Choice B includes region 764..784, which exceeds the 496-residue protein length, making it physically impossible. (3) Choice D replaces the 432..452 segment (21 residues) with 436..447 (12 residues); a 12-residue hydrophobic stretch is too short to span a ~30 Å lipid bilayer as an alpha-helix (which requires approximately 19–25 hydrophobic residues), eliminating D on basic membrane-biophysics grounds.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None that is strictly required. The ENT 11-TM topology is general family-level knowledge, and the minimum TM-helix length is basic membrane biology. Exact boundary assignment at the residue level is algorithm-dependent, but the multiple-choice format allows elimination by the length argument.",
    "reason": "The question can be answered by combining general knowledge of ENT family topology (11 TMs), a sanity check against protein length, and the biophysical requirement that a TM helix needs ~20 hydrophobic residues. These are general biological arguments, not item-specific database lookups."
  },
  "case_id": "transmembrane_0062",
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
    "reason": "The UniProt entry J9UD11 (Adenosine transporter 1, CfAT1, from Crithidia fasciculata) annotates exactly 11 transmembrane helical regions at 27..47, 78..98, 108..128, 136..156, 173..193, 209..229, 337..357, 366..386, 400..420, 432..452, and 465..485, matching Choice A precisely. The evidence code ECO:0000255 indicates these are computational predictions by similarity, not experimentally determined boundaries, but the annotation is consistent and the sequence match is confirmed (SHA256 identical)."
  },
  "important_caveats": [
    "All 11 TM annotations carry evidence code ECO:0000255 (by similarity), meaning they are computational predictions transferred from a homolog, not experimentally validated boundaries. Exact residue-level boundaries are inherently approximate.",
    "The distinction between A and D (432..452 vs 436..447) relies on a minimum-length argument; a model performing a simple hydrophobicity scan might not cleanly resolve a 4-residue boundary shift without careful analysis.",
    "The protein is from Crithidia fasciculata, a trypanosomatid; its membrane composition and hydrophobicity thresholds may differ slightly from mammalian references, though this does not affect the qualitative 11-TM topology argument."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "B is eliminated by exceeding protein length and by having only 5 TMs. C is eliminated by having only 10 TMs (inconsistent with ENT topology). D is eliminated by containing a 12-residue segment too short for a TM helix. Only A satisfies all biological constraints simultaneously."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0062",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry J9UD11 (Adenosine transporter 1, CfAT1, from Crithidia fasciculata) annotates exactly 11 transmembrane helical regions at 27..47, 78..98, 108..128, 136..156, 173..193, 209..229, 337..357, 366..386, 400..420, 432..452, and 465..485, matching Choice A precisely. The evidence code ECO:0000255 indicates these are computational predictions by similarity, not experimentally determined boundaries, but the annotation is consistent and the sequence match is confirmed (SHA256 identical).",
    "evidence_ids": ["C6","C8","C10","C12","C14","C16","C18","C20","C22","C24","C26","H4","H6","H8","H10","H12","H14","H16","H18","H20","H22","H24"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Three independent biological arguments distinguish A from the distractors: (1) Equilibrative nucleoside transporters (ENT family) are well-established to possess 11 transmembrane domains; this eliminates B (only 5 TM regions) and C (only 10 TM regions). (2) Choice B includes region 764..784, which exceeds the 496-residue protein length, making it physically impossible. (3) Choice D replaces the 432..452 segment (21 residues) with 436..447 (12 residues); a 12-residue hydrophobic stretch is too short to span a ~30 Å lipid bilayer as an alpha-helix (which requires approximately 19–25 hydrophobic residues), eliminating D on basic membrane-biophysics grounds.",
    "missing_item_specific_fact": "None that is strictly required. The ENT 11-TM topology is general family-level knowledge, and the minimum TM-helix length is basic membrane biology. Exact boundary assignment at the residue level is algorithm-dependent, but the multiple-choice format allows elimination by the length argument.",
    "reason": "The question can be answered by combining general knowledge of ENT family topology (11 TMs), a sanity check against protein length, and the biophysical requirement that a TM helix needs ~20 hydrophobic residues. These are general biological arguments, not item-specific database lookups."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "B is eliminated by exceeding protein length and by having only 5 TMs. C is eliminated by having only 10 TMs (inconsistent with ENT topology). D is eliminated by containing a 12-residue segment too short for a TM helix. Only A satisfies all biological constraints simultaneously."
  },
  "important_caveats": [
    "All 11 TM annotations carry evidence code ECO:0000255 (by similarity), meaning they are computational predictions transferred from a homolog, not experimentally validated boundaries. Exact residue-level boundaries are inherently approximate.",
    "The distinction between A and D (432..452 vs 436..447) relies on a minimum-length argument; a model performing a simple hydrophobicity scan might not cleanly resolve a 4-residue boundary shift without careful analysis.",
    "The protein is from Crithidia fasciculata, a trypanosomatid; its membrane composition and hydrophobicity thresholds may differ slightly from mammalian references, though this does not affect the qualitative 11-TM topology argument."
  ]
}
```

</details>

## After: GPT-6 Luna

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence-matched UniProt record annotates the regions listed in A as transmembrane helices, including 366..386 and 432..452. These annotations support the key, though the cited ECO:0000255 evidence is computational rather than direct experimental verification.

Citations as saved: [H4](#evidence-h4), [H6](#evidence-h6), [H8](#evidence-h8), [H10](#evidence-h10), [H12](#evidence-h12), [H14](#evidence-h14), [H16](#evidence-h16), [H18](#evidence-h18), [H20](#evidence-h20), [H22](#evidence-h22), [H24](#evidence-h24).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has repeated long hydrophobic stretches characteristic of a multi-pass membrane protein, separated by loops, including a substantial non-hydrophobic region around 230..336. Transferable knowledge of membrane-protein and transporter architecture supports the listed helix pattern. In particular, the hydrophobic stretch around 366..386 supports the segment included in A but omitted in C; the hydrophobic region around 432..452 also favors A over D's shortened alternative.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The sequence itself supplies the relevant hydrophobic pattern, and general knowledge of multi-pass membrane proteins makes the offered alternatives meaningfully distinguishable without relying on the exact protein's recorded annotation. Exact helix boundaries may be uncertain from sequence alone, but that does not prevent a credible choice among these options.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The alternatives differ at regions where the sequence's hydrophobic stretches support the boundaries in A; no competing option is comparably supported.


### Important caveats

- The reviewer evidence is a database annotation and does not establish that each boundary was experimentally measured.
- The source sequence matches the supplied sequence, but the author's exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has repeated long hydrophobic stretches characteristic of a multi-pass membrane protein, separated by loops, including a substantial non-hydrophobic region around 230..336. Transferable knowledge of membrane-protein and transporter architecture supports the listed helix pattern. In particular, the hydrophobic stretch around 366..386 supports the segment included in A but omitted in C; the hydrophobic region around 432..452 also favors A over D's shortened alternative.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The sequence itself supplies the relevant hydrophobic pattern, and general knowledge of multi-pass membrane proteins makes the offered alternatives meaningfully distinguishable without relying on the exact protein's recorded annotation. Exact helix boundaries may be uncertain from sequence alone, but that does not prevent a credible choice among these options."
  },
  "case_id": "transmembrane_0062",
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
    "reason": "The sequence-matched UniProt record annotates the regions listed in A as transmembrane helices, including 366..386 and 432..452. These annotations support the key, though the cited ECO:0000255 evidence is computational rather than direct experimental verification."
  },
  "important_caveats": [
    "The reviewer evidence is a database annotation and does not establish that each boundary was experimentally measured.",
    "The source sequence matches the supplied sequence, but the author's exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The alternatives differ at regions where the sequence's hydrophobic stretches support the boundaries in A; no competing option is comparably supported."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0062",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates the regions listed in A as transmembrane helices, including 366..386 and 432..452. These annotations support the key, though the cited ECO:0000255 evidence is computational rather than direct experimental verification.",
    "evidence_ids": ["H4", "H6", "H8", "H10", "H12", "H14", "H16", "H18", "H20", "H22", "H24"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has repeated long hydrophobic stretches characteristic of a multi-pass membrane protein, separated by loops, including a substantial non-hydrophobic region around 230..336. Transferable knowledge of membrane-protein and transporter architecture supports the listed helix pattern. In particular, the hydrophobic stretch around 366..386 supports the segment included in A but omitted in C; the hydrophobic region around 432..452 also favors A over D's shortened alternative.",
    "missing_item_specific_fact": "",
    "reason": "The sequence itself supplies the relevant hydrophobic pattern, and general knowledge of multi-pass membrane proteins makes the offered alternatives meaningfully distinguishable without relying on the exact protein's recorded annotation. Exact helix boundaries may be uncertain from sequence alone, but that does not prevent a credible choice among these options."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The alternatives differ at regions where the sequence's hydrophobic stretches support the boundaries in A; no competing option is comparably supported."
  },
  "important_caveats": [
    "The reviewer evidence is a database annotation and does not establish that each boundary was experimentally measured.",
    "The source sequence matches the supplied sequence, but the author's exact source snapshot is unknown."
  ]
}
```

</details>

## After: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry J9UD11 (Adenosine transporter 1, CfAT1, Crithidia fasciculata) annotates exactly 11 transmembrane helical regions at positions 27..47, 78..98, 108..128, 136..156, 173..193, 209..229, 337..357, 366..386, 400..420, 432..452, and 465..485 (evidence code ECO:0000255, inferred by similarity). Choice A matches these 11 regions exactly. The sequence in the question (496 aa) matches the UniProt sequence (sha256 confirmed).

Citations as saved: [C6](#evidence-c6), [C8](#evidence-c8), [C10](#evidence-c10), [C12](#evidence-c12), [C14](#evidence-c14), [C16](#evidence-c16), [C18](#evidence-c18), [C20](#evidence-c20), [C22](#evidence-c22), [C24](#evidence-c24), [C26](#evidence-c26).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Three transferable arguments distinguish Choice A from the alternatives. (1) The sequence contains hallmarks of the equilibrative nucleoside transporter (ENT) family (e.g., conserved hydrophobic motifs in the N-terminal and C-terminal halves, a long cytoplasmic loop ~230-336 between the two 6+5 TM domains). Crystal structures of human ENT1 (PDB 4C34) and ENT2, plus extensive literature, establish that functional ENTs have exactly 11 TM helices. This eliminates B (only 5 TM regions) and C (only 10 TM regions, missing 366..386). (2) TM alpha-helices must span a ~30 Å lipid bilayer, requiring approximately 20+ hydrophobic residues. Option D lists a 12-residue segment (436..447) as a TM helix, which is biophysically insufficient to cross the membrane; the correct region 432..452 is 21 residues. This general biophysical constraint eliminates D. (3) Option B includes position 764..784, which exceeds the 496-residue protein length—a trivial elimination. Together, ENT-family topology (11 TM) and TM-helix length requirements (≥~20 residues) provide a concrete, transferable basis to select A.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The ENT family's 11-TM topology is well-established from multiple homologous crystal structures and is transferable to any member of the family. The minimum TM helix length (~20 residues) is a general biophysical principle. These two pieces of knowledge, applied to the offered alternatives, meaningfully eliminate B, C, and D without requiring recall of J9UD11's specific annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options B, C, and D each have clear defects: B exceeds protein length and has too few TM regions; C omits one TM helix (inconsistent with 11-TM ENT topology); D includes a 12-residue segment too short for a TM helix. Only A is fully consistent with both family topology and biophysical constraints.


### Important caveats

- The UniProt TM annotations carry evidence code ECO:0000255 (inferred by similarity/prorule), not direct experimental determination. They are computational predictions based on homology to structurally characterized ENTs.
- The reviewer-only evidence confirms sequence match (sha256) between the benchmark input and UniProt J9UD11, but the model was not given the accession or organism name.
- Identifying the sequence as an ENT from the raw amino acid sequence requires recognizing family-level motifs; a model unfamiliar with ENT topology might rely more heavily on hydrophobicity profiling, which could introduce boundary uncertainty but would still favor A over B/C/D on the length and count criteria.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Three transferable arguments distinguish Choice A from the alternatives. (1) The sequence contains hallmarks of the equilibrative nucleoside transporter (ENT) family (e.g., conserved hydrophobic motifs in the N-terminal and C-terminal halves, a long cytoplasmic loop ~230-336 between the two 6+5 TM domains). Crystal structures of human ENT1 (PDB 4C34) and ENT2, plus extensive literature, establish that functional ENTs have exactly 11 TM helices. This eliminates B (only 5 TM regions) and C (only 10 TM regions, missing 366..386). (2) TM alpha-helices must span a ~30 Å lipid bilayer, requiring approximately 20+ hydrophobic residues. Option D lists a 12-residue segment (436..447) as a TM helix, which is biophysically insufficient to cross the membrane; the correct region 432..452 is 21 residues. This general biophysical constraint eliminates D. (3) Option B includes position 764..784, which exceeds the 496-residue protein length—a trivial elimination. Together, ENT-family topology (11 TM) and TM-helix length requirements (≥~20 residues) provide a concrete, transferable basis to select A.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The ENT family's 11-TM topology is well-established from multiple homologous crystal structures and is transferable to any member of the family. The minimum TM helix length (~20 residues) is a general biophysical principle. These two pieces of knowledge, applied to the offered alternatives, meaningfully eliminate B, C, and D without requiring recall of J9UD11's specific annotation."
  },
  "case_id": "transmembrane_0062",
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
    "reason": "The UniProt entry J9UD11 (Adenosine transporter 1, CfAT1, Crithidia fasciculata) annotates exactly 11 transmembrane helical regions at positions 27..47, 78..98, 108..128, 136..156, 173..193, 209..229, 337..357, 366..386, 400..420, 432..452, and 465..485 (evidence code ECO:0000255, inferred by similarity). Choice A matches these 11 regions exactly. The sequence in the question (496 aa) matches the UniProt sequence (sha256 confirmed)."
  },
  "important_caveats": [
    "The UniProt TM annotations carry evidence code ECO:0000255 (inferred by similarity/prorule), not direct experimental determination. They are computational predictions based on homology to structurally characterized ENTs.",
    "The reviewer-only evidence confirms sequence match (sha256) between the benchmark input and UniProt J9UD11, but the model was not given the accession or organism name.",
    "Identifying the sequence as an ENT from the raw amino acid sequence requires recognizing family-level motifs; a model unfamiliar with ENT topology might rely more heavily on hydrophobicity profiling, which could introduce boundary uncertainty but would still favor A over B/C/D on the length and count criteria."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options B, C, and D each have clear defects: B exceeds protein length and has too few TM regions; C omits one TM helix (inconsistent with 11-TM ENT topology); D includes a 12-residue segment too short for a TM helix. Only A is fully consistent with both family topology and biophysical constraints."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0062",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry J9UD11 (Adenosine transporter 1, CfAT1, Crithidia fasciculata) annotates exactly 11 transmembrane helical regions at positions 27..47, 78..98, 108..128, 136..156, 173..193, 209..229, 337..357, 366..386, 400..420, 432..452, and 465..485 (evidence code ECO:0000255, inferred by similarity). Choice A matches these 11 regions exactly. The sequence in the question (496 aa) matches the UniProt sequence (sha256 confirmed).",
    "evidence_ids": ["C6", "C8", "C10", "C12", "C14", "C16", "C18", "C20", "C22", "C24", "C26"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Three transferable arguments distinguish Choice A from the alternatives. (1) The sequence contains hallmarks of the equilibrative nucleoside transporter (ENT) family (e.g., conserved hydrophobic motifs in the N-terminal and C-terminal halves, a long cytoplasmic loop ~230-336 between the two 6+5 TM domains). Crystal structures of human ENT1 (PDB 4C34) and ENT2, plus extensive literature, establish that functional ENTs have exactly 11 TM helices. This eliminates B (only 5 TM regions) and C (only 10 TM regions, missing 366..386). (2) TM alpha-helices must span a ~30 Å lipid bilayer, requiring approximately 20+ hydrophobic residues. Option D lists a 12-residue segment (436..447) as a TM helix, which is biophysically insufficient to cross the membrane; the correct region 432..452 is 21 residues. This general biophysical constraint eliminates D. (3) Option B includes position 764..784, which exceeds the 496-residue protein length—a trivial elimination. Together, ENT-family topology (11 TM) and TM-helix length requirements (≥~20 residues) provide a concrete, transferable basis to select A.",
    "missing_item_specific_fact": "",
    "reason": "The ENT family's 11-TM topology is well-established from multiple homologous crystal structures and is transferable to any member of the family. The minimum TM helix length (~20 residues) is a general biophysical principle. These two pieces of knowledge, applied to the offered alternatives, meaningfully eliminate B, C, and D without requiring recall of J9UD11's specific annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options B, C, and D each have clear defects: B exceeds protein length and has too few TM regions; C omits one TM helix (inconsistent with 11-TM ENT topology); D includes a 12-residue segment too short for a TM helix. Only A is fully consistent with both family topology and biophysical constraints."
  },
  "important_caveats": [
    "The UniProt TM annotations carry evidence code ECO:0000255 (inferred by similarity/prorule), not direct experimental determination. They are computational predictions based on homology to structurally characterized ENTs.",
    "The reviewer-only evidence confirms sequence match (sha256) between the benchmark input and UniProt J9UD11, but the model was not given the accession or organism name.",
    "Identifying the sequence as an ENT from the raw amino acid sequence requires recognizing family-level motifs; a model unfamiliar with ENT topology might rely more heavily on hydrophobicity profiling, which could introduce boundary uncertainty but would still favor A over B/C/D on the length and count criteria."
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
  "requested_accession": "J9UD11",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "benchmark_sequence_sha256": "7c36d5c7fae62fcbb8bf70a0ab3d89954fbfbbc6fd19a54c7c3dda630ce5c242",
  "benchmark_sequence_length": 496,
  "current_status": "retrieved",
  "current_sequence_comparison": "matched",
  "current_entry_audit": {
    "entryVersion": 26,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-01-28",
    "lastSequenceUpdateDate": "2012-11-28",
    "sequenceVersion": 1
  },
  "current_uniprot_release": "2026_03",
  "current_record_sha256": "b8a834408fc72a31b2ce6a3190a6f2a1e7030d828c3ec7442331408414d4777c",
  "current_source_sequence_sha256": "7c36d5c7fae62fcbb8bf70a0ab3d89954fbfbbc6fd19a54c7c3dda630ce5c242",
  "current_source_sequence_length": 496,
  "historical_status": "retrieved",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "selected_historical_entry_version": 26,
  "selected_historical_version": {
    "accession": "J9UD11",
    "database": "Swiss-Prot",
    "entryVersion": 26,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "AT1_CRIFA",
    "sequenceVersion": 1
  },
  "selected_historical_record_sha256": "52f5c9978ed3814d8396e7feee320cd18c812e512a57459050eeb591ed24b7a6",
  "selected_historical_source_sequence_sha256": "7c36d5c7fae62fcbb8bf70a0ab3d89954fbfbbc6fd19a54c7c3dda630ce5c242",
  "selected_historical_source_sequence_length": 496,
  "latest_at_cutoff_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 26,
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9UD11.json)

```json
{
  "evidence_id": "C1",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/J9UD11.json",
  "source_sha256": "b8a834408fc72a31b2ce6a3190a6f2a1e7030d828c3ec7442331408414d4777c",
  "retrieved_utc": "2026-11-02T04:28:53.178363+00:00",
  "json_pointer": "/primaryAccession",
  "excerpt": "\"J9UD11\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9UD11.json)

```json
{
  "evidence_id": "C2",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/J9UD11.json",
  "source_sha256": "b8a834408fc72a31b2ce6a3190a6f2a1e7030d828c3ec7442331408414d4777c",
  "retrieved_utc": "2026-11-02T04:28:53.178363+00:00",
  "json_pointer": "/entryAudit",
  "excerpt": "{\"entryVersion\":26,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-01-28\",\"lastSequenceUpdateDate\":\"2012-11-28\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9UD11.json)

```json
{
  "evidence_id": "C3",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/J9UD11.json",
  "source_sha256": "b8a834408fc72a31b2ce6a3190a6f2a1e7030d828c3ec7442331408414d4777c",
  "retrieved_utc": "2026-11-02T04:28:53.178363+00:00",
  "json_pointer": "/organism",
  "excerpt": "{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"AFR68832.1\",\"source\":\"EMBL\"}],\"lineage\":[\"Eukaryota\",\"Discoba\",\"Euglenozoa\",\"Kinetoplastea\",\"Metakinetoplastina\",\"Trypanosomatida\",\"Trypanosomatidae\",\"Leishmaniinae\",\"Crithidia\"],\"scientificName\":\"Crithidia fasciculata\",\"taxonId\":5656}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9UD11.json)

```json
{
  "evidence_id": "C4",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/J9UD11.json",
  "source_sha256": "b8a834408fc72a31b2ce6a3190a6f2a1e7030d828c3ec7442331408414d4777c",
  "retrieved_utc": "2026-11-02T04:28:53.178363+00:00",
  "json_pointer": "/proteinDescription",
  "excerpt": "{\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"24120444\",\"source\":\"PubMed\"}],\"value\":\"Adenosine transporter 1\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"24120444\",\"source\":\"PubMed\"}],\"value\":\"CfAT1\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9UD11.json)

```json
{
  "evidence_id": "C5",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/J9UD11.json",
  "source_sha256": "b8a834408fc72a31b2ce6a3190a6f2a1e7030d828c3ec7442331408414d4777c",
  "retrieved_utc": "2026-11-02T04:28:53.178363+00:00",
  "json_pointer": "/features/1",
  "excerpt": "{\"description\":\"Cytoplasmic\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":26},\"start\":{\"modifier\":\"EXACT\",\"value\":1}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9UD11.json)

```json
{
  "evidence_id": "C6",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/J9UD11.json",
  "source_sha256": "b8a834408fc72a31b2ce6a3190a6f2a1e7030d828c3ec7442331408414d4777c",
  "retrieved_utc": "2026-11-02T04:28:53.178363+00:00",
  "json_pointer": "/features/2",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":47},\"start\":{\"modifier\":\"EXACT\",\"value\":27}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9UD11.json)

```json
{
  "evidence_id": "C7",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/J9UD11.json",
  "source_sha256": "b8a834408fc72a31b2ce6a3190a6f2a1e7030d828c3ec7442331408414d4777c",
  "retrieved_utc": "2026-11-02T04:28:53.178363+00:00",
  "json_pointer": "/features/3",
  "excerpt": "{\"description\":\"Extracellular\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":77},\"start\":{\"modifier\":\"EXACT\",\"value\":48}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9UD11.json)

```json
{
  "evidence_id": "C8",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/J9UD11.json",
  "source_sha256": "b8a834408fc72a31b2ce6a3190a6f2a1e7030d828c3ec7442331408414d4777c",
  "retrieved_utc": "2026-11-02T04:28:53.178363+00:00",
  "json_pointer": "/features/4",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":98},\"start\":{\"modifier\":\"EXACT\",\"value\":78}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9UD11.json)

```json
{
  "evidence_id": "C9",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/J9UD11.json",
  "source_sha256": "b8a834408fc72a31b2ce6a3190a6f2a1e7030d828c3ec7442331408414d4777c",
  "retrieved_utc": "2026-11-02T04:28:53.178363+00:00",
  "json_pointer": "/features/5",
  "excerpt": "{\"description\":\"Cytoplasmic\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":107},\"start\":{\"modifier\":\"EXACT\",\"value\":99}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9UD11.json)

```json
{
  "evidence_id": "C10",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/J9UD11.json",
  "source_sha256": "b8a834408fc72a31b2ce6a3190a6f2a1e7030d828c3ec7442331408414d4777c",
  "retrieved_utc": "2026-11-02T04:28:53.178363+00:00",
  "json_pointer": "/features/6",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":128},\"start\":{\"modifier\":\"EXACT\",\"value\":108}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9UD11.json)

```json
{
  "evidence_id": "C11",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/J9UD11.json",
  "source_sha256": "b8a834408fc72a31b2ce6a3190a6f2a1e7030d828c3ec7442331408414d4777c",
  "retrieved_utc": "2026-11-02T04:28:53.178363+00:00",
  "json_pointer": "/features/7",
  "excerpt": "{\"description\":\"Extracellular\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":135},\"start\":{\"modifier\":\"EXACT\",\"value\":129}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9UD11.json)

```json
{
  "evidence_id": "C12",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/J9UD11.json",
  "source_sha256": "b8a834408fc72a31b2ce6a3190a6f2a1e7030d828c3ec7442331408414d4777c",
  "retrieved_utc": "2026-11-02T04:28:53.178363+00:00",
  "json_pointer": "/features/8",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":156},\"start\":{\"modifier\":\"EXACT\",\"value\":136}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C13

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9UD11.json)

```json
{
  "evidence_id": "C13",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/J9UD11.json",
  "source_sha256": "b8a834408fc72a31b2ce6a3190a6f2a1e7030d828c3ec7442331408414d4777c",
  "retrieved_utc": "2026-11-02T04:28:53.178363+00:00",
  "json_pointer": "/features/9",
  "excerpt": "{\"description\":\"Cytoplasmic\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":172},\"start\":{\"modifier\":\"EXACT\",\"value\":157}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C14

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9UD11.json)

```json
{
  "evidence_id": "C14",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/J9UD11.json",
  "source_sha256": "b8a834408fc72a31b2ce6a3190a6f2a1e7030d828c3ec7442331408414d4777c",
  "retrieved_utc": "2026-11-02T04:28:53.178363+00:00",
  "json_pointer": "/features/10",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":193},\"start\":{\"modifier\":\"EXACT\",\"value\":173}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C15

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9UD11.json)

```json
{
  "evidence_id": "C15",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/J9UD11.json",
  "source_sha256": "b8a834408fc72a31b2ce6a3190a6f2a1e7030d828c3ec7442331408414d4777c",
  "retrieved_utc": "2026-11-02T04:28:53.178363+00:00",
  "json_pointer": "/features/11",
  "excerpt": "{\"description\":\"Extracellular\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":208},\"start\":{\"modifier\":\"EXACT\",\"value\":194}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C16

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9UD11.json)

```json
{
  "evidence_id": "C16",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/J9UD11.json",
  "source_sha256": "b8a834408fc72a31b2ce6a3190a6f2a1e7030d828c3ec7442331408414d4777c",
  "retrieved_utc": "2026-11-02T04:28:53.178363+00:00",
  "json_pointer": "/features/12",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":229},\"start\":{\"modifier\":\"EXACT\",\"value\":209}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C17

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9UD11.json)

```json
{
  "evidence_id": "C17",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/J9UD11.json",
  "source_sha256": "b8a834408fc72a31b2ce6a3190a6f2a1e7030d828c3ec7442331408414d4777c",
  "retrieved_utc": "2026-11-02T04:28:53.178363+00:00",
  "json_pointer": "/features/13",
  "excerpt": "{\"description\":\"Cytoplasmic\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":336},\"start\":{\"modifier\":\"EXACT\",\"value\":230}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C18

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9UD11.json)

```json
{
  "evidence_id": "C18",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/J9UD11.json",
  "source_sha256": "b8a834408fc72a31b2ce6a3190a6f2a1e7030d828c3ec7442331408414d4777c",
  "retrieved_utc": "2026-11-02T04:28:53.178363+00:00",
  "json_pointer": "/features/14",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":357},\"start\":{\"modifier\":\"EXACT\",\"value\":337}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C19

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9UD11.json)

```json
{
  "evidence_id": "C19",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/J9UD11.json",
  "source_sha256": "b8a834408fc72a31b2ce6a3190a6f2a1e7030d828c3ec7442331408414d4777c",
  "retrieved_utc": "2026-11-02T04:28:53.178363+00:00",
  "json_pointer": "/features/15",
  "excerpt": "{\"description\":\"Extracellular\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":365},\"start\":{\"modifier\":\"EXACT\",\"value\":358}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C20

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9UD11.json)

```json
{
  "evidence_id": "C20",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/J9UD11.json",
  "source_sha256": "b8a834408fc72a31b2ce6a3190a6f2a1e7030d828c3ec7442331408414d4777c",
  "retrieved_utc": "2026-11-02T04:28:53.178363+00:00",
  "json_pointer": "/features/16",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":386},\"start\":{\"modifier\":\"EXACT\",\"value\":366}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C21

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9UD11.json)

```json
{
  "evidence_id": "C21",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/J9UD11.json",
  "source_sha256": "b8a834408fc72a31b2ce6a3190a6f2a1e7030d828c3ec7442331408414d4777c",
  "retrieved_utc": "2026-11-02T04:28:53.178363+00:00",
  "json_pointer": "/features/17",
  "excerpt": "{\"description\":\"Cytoplasmic\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":399},\"start\":{\"modifier\":\"EXACT\",\"value\":387}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C22

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9UD11.json)

```json
{
  "evidence_id": "C22",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/J9UD11.json",
  "source_sha256": "b8a834408fc72a31b2ce6a3190a6f2a1e7030d828c3ec7442331408414d4777c",
  "retrieved_utc": "2026-11-02T04:28:53.178363+00:00",
  "json_pointer": "/features/18",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":420},\"start\":{\"modifier\":\"EXACT\",\"value\":400}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C23

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9UD11.json)

```json
{
  "evidence_id": "C23",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/J9UD11.json",
  "source_sha256": "b8a834408fc72a31b2ce6a3190a6f2a1e7030d828c3ec7442331408414d4777c",
  "retrieved_utc": "2026-11-02T04:28:53.178363+00:00",
  "json_pointer": "/features/19",
  "excerpt": "{\"description\":\"Extracellular\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":431},\"start\":{\"modifier\":\"EXACT\",\"value\":421}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C24

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9UD11.json)

```json
{
  "evidence_id": "C24",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/J9UD11.json",
  "source_sha256": "b8a834408fc72a31b2ce6a3190a6f2a1e7030d828c3ec7442331408414d4777c",
  "retrieved_utc": "2026-11-02T04:28:53.178363+00:00",
  "json_pointer": "/features/20",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":452},\"start\":{\"modifier\":\"EXACT\",\"value\":432}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C25

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9UD11.json)

```json
{
  "evidence_id": "C25",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/J9UD11.json",
  "source_sha256": "b8a834408fc72a31b2ce6a3190a6f2a1e7030d828c3ec7442331408414d4777c",
  "retrieved_utc": "2026-11-02T04:28:53.178363+00:00",
  "json_pointer": "/features/21",
  "excerpt": "{\"description\":\"Cytoplasmic\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":464},\"start\":{\"modifier\":\"EXACT\",\"value\":453}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C26

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9UD11.json)

```json
{
  "evidence_id": "C26",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/J9UD11.json",
  "source_sha256": "b8a834408fc72a31b2ce6a3190a6f2a1e7030d828c3ec7442331408414d4777c",
  "retrieved_utc": "2026-11-02T04:28:53.178363+00:00",
  "json_pointer": "/features/22",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":485},\"start\":{\"modifier\":\"EXACT\",\"value\":465}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C27

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9UD11.json)

```json
{
  "evidence_id": "C27",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/J9UD11.json",
  "source_sha256": "b8a834408fc72a31b2ce6a3190a6f2a1e7030d828c3ec7442331408414d4777c",
  "retrieved_utc": "2026-11-02T04:28:53.178363+00:00",
  "json_pointer": "/features/23",
  "excerpt": "{\"description\":\"Extracellular\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":496},\"start\":{\"modifier\":\"EXACT\",\"value\":486}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C28

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9UD11.json)

```json
{
  "evidence_id": "C28",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/J9UD11.json",
  "source_sha256": "b8a834408fc72a31b2ce6a3190a6f2a1e7030d828c3ec7442331408414d4777c",
  "retrieved_utc": "2026-11-02T04:28:53.178363+00:00",
  "json_pointer": "/references/0",
  "excerpt": "{\"citation\":{\"authors\":[\"Arendt C.S.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"24120444\"},{\"database\":\"DOI\",\"id\":\"10.1016/j.molbiopara.2013.09.007\"}],\"citationType\":\"journal article\",\"firstPage\":\"75\",\"id\":\"24120444\",\"journal\":\"Mol. Biochem. Parasitol.\",\"lastPage\":\"79\",\"publicationDate\":\"2013\",\"title\":\"Crithidia fasciculata adenosine transporter 1 (CfAT1), a novel high-affinity equilibrative nucleoside transporter specific for adenosine.\",\"volume\":\"191\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"AFR68832.1\",\"source\":\"EMBL\"},{\"evidenceCode\":\"ECO:0000312\",\"id\":\"AFR68833.1\",\"source\":\"EMBL\"}],\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [GENOMIC DNA]\",\"FUNCTION\",\"TRANSPORTER ACTIVITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"MUTAGENESIS OF LYS-153\",\"VARIANTS MET-433 AND VAL-481\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/J9UD11?format=txt&versions=26)

```json
{
  "evidence_id": "H1",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/J9UD11?format=txt&versions=26",
  "source_sha256": "52f5c9978ed3814d8396e7feee320cd18c812e512a57459050eeb591ed24b7a6",
  "retrieved_utc": "2026-11-02T04:28:56.181587+00:00",
  "source_locator": "lines 1-13",
  "excerpt": "ID   AT1_CRIFA               Reviewed;         496 AA.\nAC   J9UD11; J9U6P1;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   28-NOV-2012, sequence version 1.\nDT   28-JAN-2026, entry version 26.\nDE   RecName: Full=Adenosine transporter 1 {ECO:0000303|PubMed:24120444};\nDE            Short=CfAT1 {ECO:0000303|PubMed:24120444};\nGN   Name=AT1 {ECO:0000312|EMBL:AFR68832.1};\nGN   Synonyms=AT1.2 {ECO:0000312|EMBL:AFR68833.1};\nOS   Crithidia fasciculata.\nOC   Eukaryota; Discoba; Euglenozoa; Kinetoplastea; Metakinetoplastina;\nOC   Trypanosomatida; Trypanosomatidae; Leishmaniinae; Crithidia.\nOX   NCBI_TaxID=5656 {ECO:0000312|EMBL:AFR68832.1};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 26,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/J9UD11?format=txt&versions=26)

```json
{
  "evidence_id": "H2",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/J9UD11?format=txt&versions=26",
  "source_sha256": "52f5c9978ed3814d8396e7feee320cd18c812e512a57459050eeb591ed24b7a6",
  "retrieved_utc": "2026-11-02T04:28:56.181587+00:00",
  "source_locator": "lines 14-22",
  "excerpt": "RN   [1] {ECO:0000312|EMBL:AFR68832.1, ECO:0000312|EMBL:AFR68833.1}\nRP   NUCLEOTIDE SEQUENCE [GENOMIC DNA], FUNCTION, TRANSPORTER ACTIVITY,\nRP   BIOPHYSICOCHEMICAL PROPERTIES, MUTAGENESIS OF LYS-153, AND VARIANTS MET-433\nRP   AND VAL-481.\nRX   PubMed=24120444; DOI=10.1016/j.molbiopara.2013.09.007;\nRA   Arendt C.S.;\nRT   \"Crithidia fasciculata adenosine transporter 1 (CfAT1), a novel high-\nRT   affinity equilibrative nucleoside transporter specific for adenosine.\";\nRL   Mol. Biochem. Parasitol. 191:75-79(2013).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 26,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/J9UD11?format=txt&versions=26)

```json
{
  "evidence_id": "H3",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/J9UD11?format=txt&versions=26",
  "source_sha256": "52f5c9978ed3814d8396e7feee320cd18c812e512a57459050eeb591ed24b7a6",
  "retrieved_utc": "2026-11-02T04:28:56.181587+00:00",
  "source_locator": "lines 60-62",
  "excerpt": "FT   TOPO_DOM        1..26\nFT                   /note=\"Cytoplasmic\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 26,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/J9UD11?format=txt&versions=26)

```json
{
  "evidence_id": "H4",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/J9UD11?format=txt&versions=26",
  "source_sha256": "52f5c9978ed3814d8396e7feee320cd18c812e512a57459050eeb591ed24b7a6",
  "retrieved_utc": "2026-11-02T04:28:56.181587+00:00",
  "source_locator": "lines 63-65",
  "excerpt": "FT   TRANSMEM        27..47\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 26,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/J9UD11?format=txt&versions=26)

```json
{
  "evidence_id": "H5",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/J9UD11?format=txt&versions=26",
  "source_sha256": "52f5c9978ed3814d8396e7feee320cd18c812e512a57459050eeb591ed24b7a6",
  "retrieved_utc": "2026-11-02T04:28:56.181587+00:00",
  "source_locator": "lines 66-68",
  "excerpt": "FT   TOPO_DOM        48..77\nFT                   /note=\"Extracellular\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 26,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/J9UD11?format=txt&versions=26)

```json
{
  "evidence_id": "H6",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/J9UD11?format=txt&versions=26",
  "source_sha256": "52f5c9978ed3814d8396e7feee320cd18c812e512a57459050eeb591ed24b7a6",
  "retrieved_utc": "2026-11-02T04:28:56.181587+00:00",
  "source_locator": "lines 69-71",
  "excerpt": "FT   TRANSMEM        78..98\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 26,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/J9UD11?format=txt&versions=26)

```json
{
  "evidence_id": "H7",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/J9UD11?format=txt&versions=26",
  "source_sha256": "52f5c9978ed3814d8396e7feee320cd18c812e512a57459050eeb591ed24b7a6",
  "retrieved_utc": "2026-11-02T04:28:56.181587+00:00",
  "source_locator": "lines 72-74",
  "excerpt": "FT   TOPO_DOM        99..107\nFT                   /note=\"Cytoplasmic\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 26,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/J9UD11?format=txt&versions=26)

```json
{
  "evidence_id": "H8",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/J9UD11?format=txt&versions=26",
  "source_sha256": "52f5c9978ed3814d8396e7feee320cd18c812e512a57459050eeb591ed24b7a6",
  "retrieved_utc": "2026-11-02T04:28:56.181587+00:00",
  "source_locator": "lines 75-77",
  "excerpt": "FT   TRANSMEM        108..128\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 26,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/J9UD11?format=txt&versions=26)

```json
{
  "evidence_id": "H9",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/J9UD11?format=txt&versions=26",
  "source_sha256": "52f5c9978ed3814d8396e7feee320cd18c812e512a57459050eeb591ed24b7a6",
  "retrieved_utc": "2026-11-02T04:28:56.181587+00:00",
  "source_locator": "lines 78-80",
  "excerpt": "FT   TOPO_DOM        129..135\nFT                   /note=\"Extracellular\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 26,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H10

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/J9UD11?format=txt&versions=26)

```json
{
  "evidence_id": "H10",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/J9UD11?format=txt&versions=26",
  "source_sha256": "52f5c9978ed3814d8396e7feee320cd18c812e512a57459050eeb591ed24b7a6",
  "retrieved_utc": "2026-11-02T04:28:56.181587+00:00",
  "source_locator": "lines 81-83",
  "excerpt": "FT   TRANSMEM        136..156\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 26,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H11

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/J9UD11?format=txt&versions=26)

```json
{
  "evidence_id": "H11",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/J9UD11?format=txt&versions=26",
  "source_sha256": "52f5c9978ed3814d8396e7feee320cd18c812e512a57459050eeb591ed24b7a6",
  "retrieved_utc": "2026-11-02T04:28:56.181587+00:00",
  "source_locator": "lines 84-86",
  "excerpt": "FT   TOPO_DOM        157..172\nFT                   /note=\"Cytoplasmic\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 26,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H12

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/J9UD11?format=txt&versions=26)

```json
{
  "evidence_id": "H12",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/J9UD11?format=txt&versions=26",
  "source_sha256": "52f5c9978ed3814d8396e7feee320cd18c812e512a57459050eeb591ed24b7a6",
  "retrieved_utc": "2026-11-02T04:28:56.181587+00:00",
  "source_locator": "lines 87-89",
  "excerpt": "FT   TRANSMEM        173..193\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 26,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H13

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/J9UD11?format=txt&versions=26)

```json
{
  "evidence_id": "H13",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/J9UD11?format=txt&versions=26",
  "source_sha256": "52f5c9978ed3814d8396e7feee320cd18c812e512a57459050eeb591ed24b7a6",
  "retrieved_utc": "2026-11-02T04:28:56.181587+00:00",
  "source_locator": "lines 90-92",
  "excerpt": "FT   TOPO_DOM        194..208\nFT                   /note=\"Extracellular\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 26,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H14

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/J9UD11?format=txt&versions=26)

```json
{
  "evidence_id": "H14",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/J9UD11?format=txt&versions=26",
  "source_sha256": "52f5c9978ed3814d8396e7feee320cd18c812e512a57459050eeb591ed24b7a6",
  "retrieved_utc": "2026-11-02T04:28:56.181587+00:00",
  "source_locator": "lines 93-95",
  "excerpt": "FT   TRANSMEM        209..229\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 26,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H15

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/J9UD11?format=txt&versions=26)

```json
{
  "evidence_id": "H15",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/J9UD11?format=txt&versions=26",
  "source_sha256": "52f5c9978ed3814d8396e7feee320cd18c812e512a57459050eeb591ed24b7a6",
  "retrieved_utc": "2026-11-02T04:28:56.181587+00:00",
  "source_locator": "lines 96-98",
  "excerpt": "FT   TOPO_DOM        230..336\nFT                   /note=\"Cytoplasmic\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 26,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H16

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/J9UD11?format=txt&versions=26)

```json
{
  "evidence_id": "H16",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/J9UD11?format=txt&versions=26",
  "source_sha256": "52f5c9978ed3814d8396e7feee320cd18c812e512a57459050eeb591ed24b7a6",
  "retrieved_utc": "2026-11-02T04:28:56.181587+00:00",
  "source_locator": "lines 99-101",
  "excerpt": "FT   TRANSMEM        337..357\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 26,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H17

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/J9UD11?format=txt&versions=26)

```json
{
  "evidence_id": "H17",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/J9UD11?format=txt&versions=26",
  "source_sha256": "52f5c9978ed3814d8396e7feee320cd18c812e512a57459050eeb591ed24b7a6",
  "retrieved_utc": "2026-11-02T04:28:56.181587+00:00",
  "source_locator": "lines 102-104",
  "excerpt": "FT   TOPO_DOM        358..365\nFT                   /note=\"Extracellular\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 26,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H18

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/J9UD11?format=txt&versions=26)

```json
{
  "evidence_id": "H18",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/J9UD11?format=txt&versions=26",
  "source_sha256": "52f5c9978ed3814d8396e7feee320cd18c812e512a57459050eeb591ed24b7a6",
  "retrieved_utc": "2026-11-02T04:28:56.181587+00:00",
  "source_locator": "lines 105-107",
  "excerpt": "FT   TRANSMEM        366..386\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 26,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H19

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/J9UD11?format=txt&versions=26)

```json
{
  "evidence_id": "H19",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/J9UD11?format=txt&versions=26",
  "source_sha256": "52f5c9978ed3814d8396e7feee320cd18c812e512a57459050eeb591ed24b7a6",
  "retrieved_utc": "2026-11-02T04:28:56.181587+00:00",
  "source_locator": "lines 108-110",
  "excerpt": "FT   TOPO_DOM        387..399\nFT                   /note=\"Cytoplasmic\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 26,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H20

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/J9UD11?format=txt&versions=26)

```json
{
  "evidence_id": "H20",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/J9UD11?format=txt&versions=26",
  "source_sha256": "52f5c9978ed3814d8396e7feee320cd18c812e512a57459050eeb591ed24b7a6",
  "retrieved_utc": "2026-11-02T04:28:56.181587+00:00",
  "source_locator": "lines 111-113",
  "excerpt": "FT   TRANSMEM        400..420\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 26,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H21

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/J9UD11?format=txt&versions=26)

```json
{
  "evidence_id": "H21",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/J9UD11?format=txt&versions=26",
  "source_sha256": "52f5c9978ed3814d8396e7feee320cd18c812e512a57459050eeb591ed24b7a6",
  "retrieved_utc": "2026-11-02T04:28:56.181587+00:00",
  "source_locator": "lines 114-116",
  "excerpt": "FT   TOPO_DOM        421..431\nFT                   /note=\"Extracellular\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 26,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H22

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/J9UD11?format=txt&versions=26)

```json
{
  "evidence_id": "H22",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/J9UD11?format=txt&versions=26",
  "source_sha256": "52f5c9978ed3814d8396e7feee320cd18c812e512a57459050eeb591ed24b7a6",
  "retrieved_utc": "2026-11-02T04:28:56.181587+00:00",
  "source_locator": "lines 117-119",
  "excerpt": "FT   TRANSMEM        432..452\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 26,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H23

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/J9UD11?format=txt&versions=26)

```json
{
  "evidence_id": "H23",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/J9UD11?format=txt&versions=26",
  "source_sha256": "52f5c9978ed3814d8396e7feee320cd18c812e512a57459050eeb591ed24b7a6",
  "retrieved_utc": "2026-11-02T04:28:56.181587+00:00",
  "source_locator": "lines 120-122",
  "excerpt": "FT   TOPO_DOM        453..464\nFT                   /note=\"Cytoplasmic\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 26,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H24

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/J9UD11?format=txt&versions=26)

```json
{
  "evidence_id": "H24",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/J9UD11?format=txt&versions=26",
  "source_sha256": "52f5c9978ed3814d8396e7feee320cd18c812e512a57459050eeb591ed24b7a6",
  "retrieved_utc": "2026-11-02T04:28:56.181587+00:00",
  "source_locator": "lines 123-125",
  "excerpt": "FT   TRANSMEM        465..485\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 26,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H25

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/J9UD11?format=txt&versions=26)

```json
{
  "evidence_id": "H25",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/J9UD11?format=txt&versions=26",
  "source_sha256": "52f5c9978ed3814d8396e7feee320cd18c812e512a57459050eeb591ed24b7a6",
  "retrieved_utc": "2026-11-02T04:28:56.181587+00:00",
  "source_locator": "lines 126-128",
  "excerpt": "FT   TOPO_DOM        486..496\nFT                   /note=\"Extracellular\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 26,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json), zero-based source row 62. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
