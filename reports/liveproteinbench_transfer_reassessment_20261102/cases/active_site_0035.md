# active_site_0035: before and after transfer clarification

[All 1,328 cases](../README.md) · [Method](../METHOD.md) · [Summary](../SUMMARY.md) · [Exact reviewer user message](../inputs/active_site_0035.txt)

**Task:** `active_site`  
**Author key, unchanged:** **A** — Position 2 (Nucleophile)

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
MCGVLALILANQSSSAANDLHEALYVLQHRGQDAAGIATSTSSGHIHIRKKNGMAADVFQSGARLANLFGSMGIAHLRYPTAGGSANTEAQPFYVNSPYGICFAHNGNLINTVELRRYLDFEIHRHINSDSDSELMLNIFADELSETKKARVNTEDIFNGLSKMYQRCEGAWACTAMLAGFGVIGFRDAYGIRPLVMGSRPSSDGDGLDYMIASESIALDRLGFTNVRDIQPGEAVIVAKGAEPVFCQVAPRKSYTPDLFEYVYFARPDSVIDGISVYQSRQRMGRYLAARLLEVLGPEGIKEIDVVIPVPETSSPAAASVAHALNKPYCAGYIRNPYVFRTFIMPGQATRQKGVRRKLSAVKEEFKNRTILLVDDSIARGTTSREAISMAREAGVKKIIAACCSPEITYPHIYGIDLPSPHEMVAYERDNNDIAQNLGADRIVYQTLEDLQASCAEIARENDFQEPHTFENGVFSGQYVTPVPEGYFALLEKIRGTGRKEALDKSSKRL

[Multiple Choices]
A. Position 2 (Nucleophile)
B. Position 1137 (Proton donor; for dehydratase activity)
C. Position 367 (Proton donor)
D. Position 317 (For beta-ketoacyl synthase activity)
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Enzyme Active Site Prediction, which is to identify the key amino acid residues that form the active site of an enzyme. The active site is the specific region on the enzyme where a substrate binds and the chemical reaction is catalyzed. Based on the full protein sequence provided, you must select the option that correctly lists the amino acid residues (by their type and position) that constitute the enzyme's catalytic center.. The inputs provided by the user for this task include:

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

> The exact-sequence-matched UniProt record annotates residue 2 as the active-site nucleophile, consistent with choice A. This is a PROSITE-ProRule computational annotation, not direct experimental evidence for this residue.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence has a cysteine at position 2, making it a plausible nucleophile; however, the presence of that residue alone does not establish that it is catalytic.


**Missing item-specific fact**

> The input does not identify the protein's enzyme family or provide an active-site annotation linking Cys2 to nucleophilic catalysis.


**Reason**

> Selecting A as the active-site residue requires a protein-family or site-specific fact not established by the sequence and choices alone. The residue's identity is a useful clue, but not sufficient evidence of its catalytic role.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Only choice A is supported by the matched annotation; choice B also gives a position beyond the supplied sequence length of 510 residues.


### Important caveats

- The site assignment is supported by a computational ProRule annotation; the supplied evidence does not establish direct experimental validation.
- The reviewer-only source information was not part of the evaluated model input and does not make the question reasoning-supported.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has a cysteine at position 2, making it a plausible nucleophile; however, the presence of that residue alone does not establish that it is catalytic.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The input does not identify the protein's enzyme family or provide an active-site annotation linking Cys2 to nucleophilic catalysis.",
    "reason": "Selecting A as the active-site residue requires a protein-family or site-specific fact not established by the sequence and choices alone. The residue's identity is a useful clue, but not sufficient evidence of its catalytic role."
  },
  "case_id": "active_site_0035",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The exact-sequence-matched UniProt record annotates residue 2 as the active-site nucleophile, consistent with choice A. This is a PROSITE-ProRule computational annotation, not direct experimental evidence for this residue."
  },
  "important_caveats": [
    "The site assignment is supported by a computational ProRule annotation; the supplied evidence does not establish direct experimental validation.",
    "The reviewer-only source information was not part of the evaluated model input and does not make the question reasoning-supported."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only choice A is supported by the matched annotation; choice B also gives a position beyond the supplied sequence length of 510 residues."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "active_site_0035",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact-sequence-matched UniProt record annotates residue 2 as the active-site nucleophile, consistent with choice A. This is a PROSITE-ProRule computational annotation, not direct experimental evidence for this residue.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence has a cysteine at position 2, making it a plausible nucleophile; however, the presence of that residue alone does not establish that it is catalytic.",
    "missing_item_specific_fact": "The input does not identify the protein's enzyme family or provide an active-site annotation linking Cys2 to nucleophilic catalysis.",
    "reason": "Selecting A as the active-site residue requires a protein-family or site-specific fact not established by the sequence and choices alone. The residue's identity is a useful clue, but not sufficient evidence of its catalytic role."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only choice A is supported by the matched annotation; choice B also gives a position beyond the supplied sequence length of 510 residues."
  },
  "important_caveats": [
    "The site assignment is supported by a computational ProRule annotation; the supplied evidence does not establish direct experimental validation.",
    "The reviewer-only source information was not part of the evaluated model input and does not make the question reasoning-supported."
  ]
}
```

</details>

## Before: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt annotation (evidence C5/H3) explicitly annotates ACT_SITE at position 2 with note 'Nucleophile', evidenced by PROSITE-ProRule PRU00609 (ECO:0000255, computational/protein-family annotation). The sequence begins 'MC' placing Cys at position 2, consistent with the well-established N-terminal catalytic cysteine nucleophile of type I glutamine amidotransferases. The protein is annotated as EC 2.4.2.14 (phosphoribosylpyrophosphate amidotransferase FrzK). The evidence is computational (pattern-based) rather than direct experimental, but the underlying mechanistic principle (Cys nucleophile in type I amidotransferases) is well-supported by studies of homologous enzymes. Options B (position 1137 exceeds the 510-aa sequence), D (beta-ketoacyl synthase is an unrelated enzyme class), and C (no annotated active site at 367) are all inconsistent with the annotation.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3), [C4](#evidence-c4), [C1](#evidence-c1).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 510-aa sequence eliminates option B (position 1137) outright. Option D references 'beta-ketoacyl synthase activity,' a fatty-acid-synthesis enzyme class mechanistically unrelated to amidotransferases, eliminating it by functional mismatch. Between A and C: the sequence contains recognizable type I glutamine amidotransferase motifs (e.g., 'CFAHNG' near residues 36-41), and the N-terminal 'MC' places a cysteine at position 2. In type I glutamine amidotransferases, the N-terminal Cys is the well-characterized nucleophile that attacks the glutamine amide nitrogen. This general mechanistic principle allows selection of A (nucleophile at Cys-2) over C (proton donor at 367), as the primary catalytic residue in this enzyme class is the nucleophilic Cys, not a mid-sequence proton donor.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The question provides a 510-aa sequence from which options B (out-of-range position) and D (wrong enzyme class) are eliminable by basic reasoning. The remaining choice between A and C is resolved by recognizing the type I glutamine amidotransferase fold (supported by sequence motifs like CFAHNG) and applying the general biochemical principle that the N-terminal Cys serves as the catalytic nucleophile in this enzyme family. This is generalizable mechanistic knowledge, not an item-specific lookup.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Option B is physically impossible (position 1137 > 510 aa). Option D names an unrelated enzyme class. Option C (proton donor at 367) is not supported by any annotation and is inconsistent with the primary catalytic mechanism of type I amidotransferases. Only option A aligns with both the annotation and the established mechanism.


### Important caveats

- The active-site annotation carries evidence code ECO:0000255 (PROSITE-ProRule), meaning it is a computational/pattern-based assignment rather than direct experimental mutagenesis or structural evidence for this specific protein.
- The Mg2+ binding sites at positions 313, 375, 376 are annotated by similarity to P00497 (E. coli PurF), indicating transferred annotation for the cofactor-binding domain.
- The reviewer-only evidence was not available to the evaluated model; the reasoning path relies on general biochemical knowledge of type I amidotransferase catalytic mechanisms.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 510-aa sequence eliminates option B (position 1137) outright. Option D references 'beta-ketoacyl synthase activity,' a fatty-acid-synthesis enzyme class mechanistically unrelated to amidotransferases, eliminating it by functional mismatch. Between A and C: the sequence contains recognizable type I glutamine amidotransferase motifs (e.g., 'CFAHNG' near residues 36-41), and the N-terminal 'MC' places a cysteine at position 2. In type I glutamine amidotransferases, the N-terminal Cys is the well-characterized nucleophile that attacks the glutamine amide nitrogen. This general mechanistic principle allows selection of A (nucleophile at Cys-2) over C (proton donor at 367), as the primary catalytic residue in this enzyme class is the nucleophilic Cys, not a mid-sequence proton donor.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The question provides a 510-aa sequence from which options B (out-of-range position) and D (wrong enzyme class) are eliminable by basic reasoning. The remaining choice between A and C is resolved by recognizing the type I glutamine amidotransferase fold (supported by sequence motifs like CFAHNG) and applying the general biochemical principle that the N-terminal Cys serves as the catalytic nucleophile in this enzyme family. This is generalizable mechanistic knowledge, not an item-specific lookup."
  },
  "case_id": "active_site_0035",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3",
      "C4",
      "C1"
    ],
    "judgment": "supported",
    "reason": "UniProt annotation (evidence C5/H3) explicitly annotates ACT_SITE at position 2 with note 'Nucleophile', evidenced by PROSITE-ProRule PRU00609 (ECO:0000255, computational/protein-family annotation). The sequence begins 'MC' placing Cys at position 2, consistent with the well-established N-terminal catalytic cysteine nucleophile of type I glutamine amidotransferases. The protein is annotated as EC 2.4.2.14 (phosphoribosylpyrophosphate amidotransferase FrzK). The evidence is computational (pattern-based) rather than direct experimental, but the underlying mechanistic principle (Cys nucleophile in type I amidotransferases) is well-supported by studies of homologous enzymes. Options B (position 1137 exceeds the 510-aa sequence), D (beta-ketoacyl synthase is an unrelated enzyme class), and C (no annotated active site at 367) are all inconsistent with the annotation."
  },
  "important_caveats": [
    "The active-site annotation carries evidence code ECO:0000255 (PROSITE-ProRule), meaning it is a computational/pattern-based assignment rather than direct experimental mutagenesis or structural evidence for this specific protein.",
    "The Mg2+ binding sites at positions 313, 375, 376 are annotated by similarity to P00497 (E. coli PurF), indicating transferred annotation for the cofactor-binding domain.",
    "The reviewer-only evidence was not available to the evaluated model; the reasoning path relies on general biochemical knowledge of type I amidotransferase catalytic mechanisms."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Option B is physically impossible (position 1137 > 510 aa). Option D names an unrelated enzyme class. Option C (proton donor at 367) is not supported by any annotation and is inconsistent with the primary catalytic mechanism of type I amidotransferases. Only option A aligns with both the annotation and the established mechanism."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "active_site_0035",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt annotation (evidence C5/H3) explicitly annotates ACT_SITE at position 2 with note 'Nucleophile', evidenced by PROSITE-ProRule PRU00609 (ECO:0000255, computational/protein-family annotation). The sequence begins 'MC' placing Cys at position 2, consistent with the well-established N-terminal catalytic cysteine nucleophile of type I glutamine amidotransferases. The protein is annotated as EC 2.4.2.14 (phosphoribosylpyrophosphate amidotransferase FrzK). The evidence is computational (pattern-based) rather than direct experimental, but the underlying mechanistic principle (Cys nucleophile in type I amidotransferases) is well-supported by studies of homologous enzymes. Options B (position 1137 exceeds the 510-aa sequence), D (beta-ketoacyl synthase is an unrelated enzyme class), and C (no annotated active site at 367) are all inconsistent with the annotation.",
    "evidence_ids": ["C5", "H3", "C4", "C1"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 510-aa sequence eliminates option B (position 1137) outright. Option D references 'beta-ketoacyl synthase activity,' a fatty-acid-synthesis enzyme class mechanistically unrelated to amidotransferases, eliminating it by functional mismatch. Between A and C: the sequence contains recognizable type I glutamine amidotransferase motifs (e.g., 'CFAHNG' near residues 36-41), and the N-terminal 'MC' places a cysteine at position 2. In type I glutamine amidotransferases, the N-terminal Cys is the well-characterized nucleophile that attacks the glutamine amide nitrogen. This general mechanistic principle allows selection of A (nucleophile at Cys-2) over C (proton donor at 367), as the primary catalytic residue in this enzyme class is the nucleophilic Cys, not a mid-sequence proton donor.",
    "missing_item_specific_fact": "",
    "reason": "The question provides a 510-aa sequence from which options B (out-of-range position) and D (wrong enzyme class) are eliminable by basic reasoning. The remaining choice between A and C is resolved by recognizing the type I glutamine amidotransferase fold (supported by sequence motifs like CFAHNG) and applying the general biochemical principle that the N-terminal Cys serves as the catalytic nucleophile in this enzyme family. This is generalizable mechanistic knowledge, not an item-specific lookup."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Option B is physically impossible (position 1137 > 510 aa). Option D names an unrelated enzyme class. Option C (proton donor at 367) is not supported by any annotation and is inconsistent with the primary catalytic mechanism of type I amidotransferases. Only option A aligns with both the annotation and the established mechanism."
  },
  "important_caveats": [
    "The active-site annotation carries evidence code ECO:0000255 (PROSITE-ProRule), meaning it is a computational/pattern-based assignment rather than direct experimental mutagenesis or structural evidence for this specific protein.",
    "The Mg2+ binding sites at positions 313, 375, 376 are annotated by similarity to P00497 (E. coli PurF), indicating transferred annotation for the cofactor-binding domain.",
    "The reviewer-only evidence was not available to the evaluated model; the reasoning path relies on general biochemical knowledge of type I amidotransferase catalytic mechanisms."
  ]
}
```

</details>

## After: GPT-6 Luna

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> Position 2 is cysteine in the supplied, sequence-matched protein. The source annotates it as the active-site nucleophile; that annotation is based on a PROSITE rule, so it supports the key as a computational annotation rather than direct experimental evidence.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence begins M-C, placing a cysteine at position 2. In glutamine-dependent phosphoribosyl amidotransferase family proteins, a conserved N-terminal cysteine acts as the catalytic nucleophile. This transferable family-level pattern makes A a meaningful choice; B is also excluded because position 1137 lies beyond the 510-residue sequence.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The N-terminal cysteine and its characteristic catalytic role provide a credible inference from the sequence and knowledge of related enzymes. The exact target's database annotation is not necessary to distinguish the offered choices.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The conserved N-terminal nucleophile supports A, while B gives an out-of-range position and the other options describe different roles.


### Important caveats

- The reviewer evidence is a PROSITE-ProRule annotation, not direct experimental confirmation.
- The family-level inference is strong but does not itself establish experimental activity for this particular protein.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence begins M-C, placing a cysteine at position 2. In glutamine-dependent phosphoribosyl amidotransferase family proteins, a conserved N-terminal cysteine acts as the catalytic nucleophile. This transferable family-level pattern makes A a meaningful choice; B is also excluded because position 1137 lies beyond the 510-residue sequence.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The N-terminal cysteine and its characteristic catalytic role provide a credible inference from the sequence and knowledge of related enzymes. The exact target's database annotation is not necessary to distinguish the offered choices."
  },
  "case_id": "active_site_0035",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "Position 2 is cysteine in the supplied, sequence-matched protein. The source annotates it as the active-site nucleophile; that annotation is based on a PROSITE rule, so it supports the key as a computational annotation rather than direct experimental evidence."
  },
  "important_caveats": [
    "The reviewer evidence is a PROSITE-ProRule annotation, not direct experimental confirmation.",
    "The family-level inference is strong but does not itself establish experimental activity for this particular protein."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The conserved N-terminal nucleophile supports A, while B gives an out-of-range position and the other options describe different roles."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "active_site_0035",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "Position 2 is cysteine in the supplied, sequence-matched protein. The source annotates it as the active-site nucleophile; that annotation is based on a PROSITE rule, so it supports the key as a computational annotation rather than direct experimental evidence.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence begins M-C, placing a cysteine at position 2. In glutamine-dependent phosphoribosyl amidotransferase family proteins, a conserved N-terminal cysteine acts as the catalytic nucleophile. This transferable family-level pattern makes A a meaningful choice; B is also excluded because position 1137 lies beyond the 510-residue sequence.",
    "missing_item_specific_fact": "",
    "reason": "The N-terminal cysteine and its characteristic catalytic role provide a credible inference from the sequence and knowledge of related enzymes. The exact target's database annotation is not necessary to distinguish the offered choices."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The conserved N-terminal nucleophile supports A, while B gives an out-of-range position and the other options describe different roles."
  },
  "important_caveats": [
    "The reviewer evidence is a PROSITE-ProRule annotation, not direct experimental confirmation.",
    "The family-level inference is strong but does not itself establish experimental activity for this particular protein."
  ]
}
```

</details>

## After: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry (A0A7T8J1U7) annotates position 2 as 'Active site: Nucleophile' (evidence ECO:0000255|PROSITE-ProRule:PRU00609, i.e., class-I glutamine amidotransferase family rule). The sequence begins 'MC...' and position 2 is Cys. In all well-characterized class-I glutamine amidotransferases (PurF/P00497, TrpG, HisH, etc.), the N-terminal Cys is the catalytic nucleophile that attacks the γ-amide of glutamine. The annotation is computational (PROSITE-ProRule) but is grounded in an extremely well-established family mechanism. The expected answer A matches the sole 'Active site' feature in the record.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The N-terminal 'MC' motif is the hallmark of the class-I glutamine amidotransferase (GAT) domain. In every characterized member of this superfamily (E. coli PurF, TrpG, HisH, and many others), the Cys at position 2 is the catalytic nucleophile that forms a thioester intermediate with the amide nitrogen of glutamine. This is textbook enzymology and highly conserved across the family. A knowledgeable model recognizing the 'MC' start and the PRPP amidotransferase context (EC 2.4.2.14, 'Glutamine PRPP amidotransferase' as an alternative name is not given to the model, but the sequence length ~510 AA and the GAT signature are visible) can infer that Cys2 is the nucleophile. The distractors are eliminable: B references position 1137 in a 510-residue protein (physically impossible); D references 'beta-ketoacyl synthase activity,' a completely unrelated enzyme family (FabH/FAS); C references a 'proton donor' at 367, which is not the primary catalytic residue in GAT mechanism (the nucleophile is). Thus family-level knowledge of class-I GATs meaningfully distinguishes A from all other options.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Recognition of the N-terminal Cys as the class-I GAT nucleophile is transferable knowledge from dozens of well-studied homologs (PurF, TrpG, HisH). The distractors are eliminated by basic checks (position 1137 > 510 AA; wrong enzyme family for D; proton donor is not the defining catalytic residue for GAT). No target-specific memorization is required.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Option B is physically impossible (position 1137 in a 510 AA protein). Option D references an unrelated enzyme activity. Option C (proton donor at 367) is not annotated and does not match the primary catalytic mechanism of GATs. Only option A aligns with the well-established N-terminal Cys nucleophile of class-I GATs and the sole 'Active site' annotation.


### Important caveats

- The active-site annotation at position 2 carries evidence code ECO:0000255 (PROSITE-ProRule), i.e., it is a family/pattern-based computational inference rather than direct experimental mutagenesis on this exact protein. However, the underlying mechanism is experimentally validated in canonical homologs (e.g., E. coli PurF Cys2).
- The protein is bifunctional (GAT + PRPP transferase domains); the question's 'catalytic center' is interpreted as the GAT nucleophile per the annotation. The PRPP transferase domain's catalytic residues (Mg2+ binding at 313, 375, 376) are annotated as 'Binding site,' not 'Active site.'
- Distractor B (position 1137) exceeds the protein length (510 AA), making it trivially eliminable and reducing the effective difficulty of the question.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal 'MC' motif is the hallmark of the class-I glutamine amidotransferase (GAT) domain. In every characterized member of this superfamily (E. coli PurF, TrpG, HisH, and many others), the Cys at position 2 is the catalytic nucleophile that forms a thioester intermediate with the amide nitrogen of glutamine. This is textbook enzymology and highly conserved across the family. A knowledgeable model recognizing the 'MC' start and the PRPP amidotransferase context (EC 2.4.2.14, 'Glutamine PRPP amidotransferase' as an alternative name is not given to the model, but the sequence length ~510 AA and the GAT signature are visible) can infer that Cys2 is the nucleophile. The distractors are eliminable: B references position 1137 in a 510-residue protein (physically impossible); D references 'beta-ketoacyl synthase activity,' a completely unrelated enzyme family (FabH/FAS); C references a 'proton donor' at 367, which is not the primary catalytic residue in GAT mechanism (the nucleophile is). Thus family-level knowledge of class-I GATs meaningfully distinguishes A from all other options.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Recognition of the N-terminal Cys as the class-I GAT nucleophile is transferable knowledge from dozens of well-studied homologs (PurF, TrpG, HisH). The distractors are eliminated by basic checks (position 1137 > 510 AA; wrong enzyme family for D; proton donor is not the defining catalytic residue for GAT). No target-specific memorization is required."
  },
  "case_id": "active_site_0035",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry (A0A7T8J1U7) annotates position 2 as 'Active site: Nucleophile' (evidence ECO:0000255|PROSITE-ProRule:PRU00609, i.e., class-I glutamine amidotransferase family rule). The sequence begins 'MC...' and position 2 is Cys. In all well-characterized class-I glutamine amidotransferases (PurF/P00497, TrpG, HisH, etc.), the N-terminal Cys is the catalytic nucleophile that attacks the γ-amide of glutamine. The annotation is computational (PROSITE-ProRule) but is grounded in an extremely well-established family mechanism. The expected answer A matches the sole 'Active site' feature in the record."
  },
  "important_caveats": [
    "The active-site annotation at position 2 carries evidence code ECO:0000255 (PROSITE-ProRule), i.e., it is a family/pattern-based computational inference rather than direct experimental mutagenesis on this exact protein. However, the underlying mechanism is experimentally validated in canonical homologs (e.g., E. coli PurF Cys2).",
    "The protein is bifunctional (GAT + PRPP transferase domains); the question's 'catalytic center' is interpreted as the GAT nucleophile per the annotation. The PRPP transferase domain's catalytic residues (Mg2+ binding at 313, 375, 376) are annotated as 'Binding site,' not 'Active site.'",
    "Distractor B (position 1137) exceeds the protein length (510 AA), making it trivially eliminable and reducing the effective difficulty of the question."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Option B is physically impossible (position 1137 in a 510 AA protein). Option D references an unrelated enzyme activity. Option C (proton donor at 367) is not annotated and does not match the primary catalytic mechanism of GATs. Only option A aligns with the well-established N-terminal Cys nucleophile of class-I GATs and the sole 'Active site' annotation."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "active_site_0035",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry (A0A7T8J1U7) annotates position 2 as 'Active site: Nucleophile' (evidence ECO:0000255|PROSITE-ProRule:PRU00609, i.e., class-I glutamine amidotransferase family rule). The sequence begins 'MC...' and position 2 is Cys. In all well-characterized class-I glutamine amidotransferases (PurF/P00497, TrpG, HisH, etc.), the N-terminal Cys is the catalytic nucleophile that attacks the γ-amide of glutamine. The annotation is computational (PROSITE-ProRule) but is grounded in an extremely well-established family mechanism. The expected answer A matches the sole 'Active site' feature in the record.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The N-terminal 'MC' motif is the hallmark of the class-I glutamine amidotransferase (GAT) domain. In every characterized member of this superfamily (E. coli PurF, TrpG, HisH, and many others), the Cys at position 2 is the catalytic nucleophile that forms a thioester intermediate with the amide nitrogen of glutamine. This is textbook enzymology and highly conserved across the family. A knowledgeable model recognizing the 'MC' start and the PRPP amidotransferase context (EC 2.4.2.14, 'Glutamine PRPP amidotransferase' as an alternative name is not given to the model, but the sequence length ~510 AA and the GAT signature are visible) can infer that Cys2 is the nucleophile. The distractors are eliminable: B references position 1137 in a 510-residue protein (physically impossible); D references 'beta-ketoacyl synthase activity,' a completely unrelated enzyme family (FabH/FAS); C references a 'proton donor' at 367, which is not the primary catalytic residue in GAT mechanism (the nucleophile is). Thus family-level knowledge of class-I GATs meaningfully distinguishes A from all other options.",
    "missing_item_specific_fact": "",
    "reason": "Recognition of the N-terminal Cys as the class-I GAT nucleophile is transferable knowledge from dozens of well-studied homologs (PurF, TrpG, HisH). The distractors are eliminated by basic checks (position 1137 > 510 AA; wrong enzyme family for D; proton donor is not the defining catalytic residue for GAT). No target-specific memorization is required."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Option B is physically impossible (position 1137 in a 510 AA protein). Option D references an unrelated enzyme activity. Option C (proton donor at 367) is not annotated and does not match the primary catalytic mechanism of GATs. Only option A aligns with the well-established N-terminal Cys nucleophile of class-I GATs and the sole 'Active site' annotation."
  },
  "important_caveats": [
    "The active-site annotation at position 2 carries evidence code ECO:0000255 (PROSITE-ProRule), i.e., it is a family/pattern-based computational inference rather than direct experimental mutagenesis on this exact protein. However, the underlying mechanism is experimentally validated in canonical homologs (e.g., E. coli PurF Cys2).",
    "The protein is bifunctional (GAT + PRPP transferase domains); the question's 'catalytic center' is interpreted as the GAT nucleophile per the annotation. The PRPP transferase domain's catalytic residues (Mg2+ binding at 313, 375, 376) are annotated as 'Binding site,' not 'Active site.'",
    "Distractor B (position 1137) exceeds the protein length (510 AA), making it trivially eliminable and reducing the effective difficulty of the question."
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
  "requested_accession": "A0A7T8J1U7",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "benchmark_sequence_sha256": "44dc44e51fdf196ccecccc1dbeec4ed51df88981f809d29be8495d6c59ba2224",
  "benchmark_sequence_length": 510,
  "current_status": "retrieved",
  "current_sequence_comparison": "matched",
  "current_entry_audit": {
    "entryVersion": 18,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2021-06-02",
    "sequenceVersion": 1
  },
  "current_uniprot_release": "2026_03",
  "current_record_sha256": "56665e1cd9e3380e3faeac05a356479129623641a0ef275c9308eeccf948063d",
  "current_source_sequence_sha256": "44dc44e51fdf196ccecccc1dbeec4ed51df88981f809d29be8495d6c59ba2224",
  "current_source_sequence_length": 510,
  "historical_status": "retrieved",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "selected_historical_entry_version": 16,
  "selected_historical_version": {
    "accession": "A0A7T8J1U7",
    "database": "Swiss-Prot",
    "entryVersion": 16,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "FRZK_CLASX",
    "sequenceVersion": 1
  },
  "selected_historical_record_sha256": "578ee5dbb88bc40f60a644a1dc0fae09acdb5d05f79fe55109621fabea2329a5",
  "selected_historical_source_sequence_sha256": "44dc44e51fdf196ccecccc1dbeec4ed51df88981f809d29be8495d6c59ba2224",
  "selected_historical_source_sequence_length": 510,
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8J1U7.json)

```json
{
  "evidence_id": "C1",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7T8J1U7.json",
  "source_sha256": "56665e1cd9e3380e3faeac05a356479129623641a0ef275c9308eeccf948063d",
  "retrieved_utc": "2026-11-02T04:25:51.826168+00:00",
  "json_pointer": "/primaryAccession",
  "excerpt": "\"A0A7T8J1U7\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8J1U7.json)

```json
{
  "evidence_id": "C2",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7T8J1U7.json",
  "source_sha256": "56665e1cd9e3380e3faeac05a356479129623641a0ef275c9308eeccf948063d",
  "retrieved_utc": "2026-11-02T04:25:51.826168+00:00",
  "json_pointer": "/entryAudit",
  "excerpt": "{\"entryVersion\":18,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2021-06-02\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8J1U7.json)

```json
{
  "evidence_id": "C3",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7T8J1U7.json",
  "source_sha256": "56665e1cd9e3380e3faeac05a356479129623641a0ef275c9308eeccf948063d",
  "retrieved_utc": "2026-11-02T04:25:51.826168+00:00",
  "json_pointer": "/organism",
  "excerpt": "{\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Sordariomycetes\",\"Hypocreomycetidae\",\"Hypocreales\",\"Hypocreaceae\",\"Cladobotryum\"],\"scientificName\":\"Cladobotryum sp\",\"taxonId\":2040732}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8J1U7.json)

```json
{
  "evidence_id": "C4",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7T8J1U7.json",
  "source_sha256": "56665e1cd9e3380e3faeac05a356479129623641a0ef275c9308eeccf948063d",
  "retrieved_utc": "2026-11-02T04:25:51.826168+00:00",
  "json_pointer": "/proteinDescription",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"33372776\",\"source\":\"PubMed\"}],\"value\":\"FR901483 biosynthesis clusters protein K\"}},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"33372776\",\"source\":\"PubMed\"}],\"value\":\"Glutamine phosphoribosylpyrophosphate amidotransferase\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"33372776\",\"source\":\"PubMed\"}],\"value\":\"2.4.2.14\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"33372776\",\"source\":\"PubMed\"}],\"value\":\"Phosphoribosylpyrophosphate amidotransferase FrzK\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"33372776\",\"source\":\"PubMed\"}],\"value\":\"ATase FrzK\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8J1U7.json)

```json
{
  "evidence_id": "C5",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7T8J1U7.json",
  "source_sha256": "56665e1cd9e3380e3faeac05a356479129623641a0ef275c9308eeccf948063d",
  "retrieved_utc": "2026-11-02T04:25:51.826168+00:00",
  "json_pointer": "/features/2",
  "excerpt": "{\"description\":\"Nucleophile\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU00609\",\"source\":\"PROSITE-ProRule\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":2},\"start\":{\"modifier\":\"EXACT\",\"value\":2}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8J1U7.json)

```json
{
  "evidence_id": "C6",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7T8J1U7.json",
  "source_sha256": "56665e1cd9e3380e3faeac05a356479129623641a0ef275c9308eeccf948063d",
  "retrieved_utc": "2026-11-02T04:25:51.826168+00:00",
  "json_pointer": "/features/3",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P00497\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:18420\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:18420\",\"name\":\"Mg(2+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":313},\"start\":{\"modifier\":\"EXACT\",\"value\":313}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8J1U7.json)

```json
{
  "evidence_id": "C7",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7T8J1U7.json",
  "source_sha256": "56665e1cd9e3380e3faeac05a356479129623641a0ef275c9308eeccf948063d",
  "retrieved_utc": "2026-11-02T04:25:51.826168+00:00",
  "json_pointer": "/features/4",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P00497\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:18420\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:18420\",\"name\":\"Mg(2+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":375},\"start\":{\"modifier\":\"EXACT\",\"value\":375}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8J1U7.json)

```json
{
  "evidence_id": "C8",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7T8J1U7.json",
  "source_sha256": "56665e1cd9e3380e3faeac05a356479129623641a0ef275c9308eeccf948063d",
  "retrieved_utc": "2026-11-02T04:25:51.826168+00:00",
  "json_pointer": "/features/5",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P00497\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:18420\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:18420\",\"name\":\"Mg(2+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":376},\"start\":{\"modifier\":\"EXACT\",\"value\":376}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8J1U7.json)

```json
{
  "evidence_id": "C9",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7T8J1U7.json",
  "source_sha256": "56665e1cd9e3380e3faeac05a356479129623641a0ef275c9308eeccf948063d",
  "retrieved_utc": "2026-11-02T04:25:51.826168+00:00",
  "json_pointer": "/references/0",
  "excerpt": "{\"citation\":{\"authors\":[\"Zhang Z.\",\"Tamura Y.\",\"Tang M.\",\"Qiao T.\",\"Sato M.\",\"Otsu Y.\",\"Sasamura S.\",\"Taniguchi M.\",\"Watanabe K.\",\"Tang Y.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"33372776\"},{\"database\":\"DOI\",\"id\":\"10.1021/jacs.0c12352\"}],\"citationType\":\"journal article\",\"firstPage\":\"132\",\"id\":\"33372776\",\"journal\":\"J. Am. Chem. Soc.\",\"lastPage\":\"136\",\"publicationDate\":\"2021\",\"title\":\"Biosynthesis of the Immunosuppressant (-)-FR901483.\",\"volume\":\"143\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"11231\"}],\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [GENOMIC DNA]\",\"FUNCTION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7T8J1U7?format=txt&versions=16)

```json
{
  "evidence_id": "H1",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A7T8J1U7?format=txt&versions=16",
  "source_sha256": "578ee5dbb88bc40f60a644a1dc0fae09acdb5d05f79fe55109621fabea2329a5",
  "retrieved_utc": "2026-11-02T04:25:55.036238+00:00",
  "source_locator": "lines 1-15",
  "excerpt": "ID   FRZK_CLASX              Reviewed;         510 AA.\nAC   A0A7T8J1U7;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   02-JUN-2021, sequence version 1.\nDT   28-JAN-2026, entry version 16.\nDE   RecName: Full=Phosphoribosylpyrophosphate amidotransferase FrzK {ECO:0000303|PubMed:33372776};\nDE            Short=ATase FrzK {ECO:0000303|PubMed:33372776};\nDE            EC=2.4.2.14 {ECO:0000269|PubMed:33372776};\nDE   AltName: Full=FR901483 biosynthesis clusters protein K {ECO:0000303|PubMed:33372776};\nDE   AltName: Full=Glutamine phosphoribosylpyrophosphate amidotransferase {ECO:0000303|PubMed:33372776};\nGN   Name=FrzK {ECO:0000303|PubMed:33372776};\nOS   Cladobotryum sp.\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Sordariomycetes;\nOC   Hypocreomycetidae; Hypocreales; Hypocreaceae; Cladobotryum.\nOX   NCBI_TaxID=2040732;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 16,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7T8J1U7?format=txt&versions=16)

```json
{
  "evidence_id": "H2",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A7T8J1U7?format=txt&versions=16",
  "source_sha256": "578ee5dbb88bc40f60a644a1dc0fae09acdb5d05f79fe55109621fabea2329a5",
  "retrieved_utc": "2026-11-02T04:25:55.036238+00:00",
  "source_locator": "lines 16-23",
  "excerpt": "RN   [1]\nRP   NUCLEOTIDE SEQUENCE [GENOMIC DNA], AND FUNCTION.\nRC   STRAIN=11231;\nRX   PubMed=33372776; DOI=10.1021/jacs.0c12352;\nRA   Zhang Z., Tamura Y., Tang M., Qiao T., Sato M., Otsu Y., Sasamura S.,\nRA   Taniguchi M., Watanabe K., Tang Y.;\nRT   \"Biosynthesis of the Immunosuppressant (-)-FR901483.\";\nRL   J. Am. Chem. Soc. 143:132-136(2021).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 16,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7T8J1U7?format=txt&versions=16)

```json
{
  "evidence_id": "H3",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A7T8J1U7?format=txt&versions=16",
  "source_sha256": "578ee5dbb88bc40f60a644a1dc0fae09acdb5d05f79fe55109621fabea2329a5",
  "retrieved_utc": "2026-11-02T04:25:55.036238+00:00",
  "source_locator": "lines 99-101",
  "excerpt": "FT   ACT_SITE        2\nFT                   /note=\"Nucleophile\"\nFT                   /evidence=\"ECO:0000255|PROSITE-ProRule:PRU00609\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 16,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7T8J1U7?format=txt&versions=16)

```json
{
  "evidence_id": "H4",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A7T8J1U7?format=txt&versions=16",
  "source_sha256": "578ee5dbb88bc40f60a644a1dc0fae09acdb5d05f79fe55109621fabea2329a5",
  "retrieved_utc": "2026-11-02T04:25:55.036238+00:00",
  "source_locator": "lines 102-105",
  "excerpt": "FT   BINDING         313\nFT                   /ligand=\"Mg(2+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:18420\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:P00497\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 16,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7T8J1U7?format=txt&versions=16)

```json
{
  "evidence_id": "H5",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A7T8J1U7?format=txt&versions=16",
  "source_sha256": "578ee5dbb88bc40f60a644a1dc0fae09acdb5d05f79fe55109621fabea2329a5",
  "retrieved_utc": "2026-11-02T04:25:55.036238+00:00",
  "source_locator": "lines 106-109",
  "excerpt": "FT   BINDING         375\nFT                   /ligand=\"Mg(2+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:18420\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:P00497\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 16,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7T8J1U7?format=txt&versions=16)

```json
{
  "evidence_id": "H6",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A7T8J1U7?format=txt&versions=16",
  "source_sha256": "578ee5dbb88bc40f60a644a1dc0fae09acdb5d05f79fe55109621fabea2329a5",
  "retrieved_utc": "2026-11-02T04:25:55.036238+00:00",
  "source_locator": "lines 110-113",
  "excerpt": "FT   BINDING         376\nFT                   /ligand=\"Mg(2+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:18420\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:P00497\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 16,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/active_site.json), zero-based source row 35. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
