# GO_molecular_function_0154: before and after transfer clarification

[All 1,328 cases](../README.md) · [Method](../METHOD.md) · [Summary](../SUMMARY.md) · [Exact reviewer user message](../inputs/GO_molecular_function_0154.txt)

**Task:** `GO_molecular_function`  
**Author key, unchanged:** **D** — cystathionine gamma-lyase activity

| Round | Reviewer | Key support | Transfer / lookup | Output usability (canonical status) |
|---|---|---|---|---|
| before | GPT-6 Luna | contradicted | lookup-dependent | usable output (valid_review) |
| before | Qwen3.8-Flash-Next-NVFP4 | contradicted | reasoning-supported | usable output (valid_review) |
| after | GPT-6 Luna | contradicted | lookup-dependent | usable output (valid_review) |
| after | Qwen3.8-Flash-Next-NVFP4 | contradicted | reasoning-supported | usable output (valid_review) |

**Usable output means format-valid review, not reasoning-supported or biologically correct.** A usable output can classify the question as reasoning-supported, lookup-dependent or uncertain. An output error is a problem with the saved model response; it does not count a defective benchmark question or wrong key. Each saved review is retained in full below. Labels from output errors are displayed as saved and excluded from label statistics. The author key and reviewer evidence were visible to reviewers; this is a review of answerability and key support, not a benchmark-solving score.

## Complete original question

```text
[Protein Sequence]
MIAVNSRNSLNADMTSLHPETLMVHGGMKGLTEAGVHVPAIDLSTTNPVNDVATGGDSYEWLATGHTLKDGDSAVYQRLWQPGVARFETALAGLEHAEEAVAFATGMAAMTAALLAAVSAGTPHIVAVRPLYGGSDHLLETGLLGTTVTWAKEADIASAIQDDTGLVIVETPANPSLDLVDLDSVVSAAGNVPVLVDNTFCTPVLQQPISHGAALVLHSATKYLGGHGDAMGGIIATNADWAMRLRQVRAITGALLHPMGAYLLHRGLRTLAVRMRAAQTTAGELAERLDAHPAISVVHYPGLKGQDPRGLLGRQMSGGGAMIAMELAGGFDAARSFVEHCNLVVHAVSLGGADTLIQHPASLTHRPVAATAKPGDGLIRLSVGLEHVDDLADDLIAALDASRAAA

[Multiple Choices]
A. S-adenosyl-L-methionine binding
B. ubiquitin protein ligase activity
C. amidophosphoribosyltransferase activity
D. cystathionine gamma-lyase activity
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Gene Ontology (GO) Molecular Function Prediction, which is to predict the fundamental activity of a protein at the molecular level, as defined by the Gene Ontology (GO) 'Molecular Function' branch. This describes the elemental tasks a protein performs, such as catalysis, transport, or binding to specific molecules. Based on the protein's amino acid sequence, you are to select the option that best describes its primary molecular function.. The inputs provided by the user for this task include:

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

### Expected-answer support: contradicted

> The sequence-matched protein is experimentally annotated as an L-methionine gamma-lyase, and the cited functional evidence says it has no activity toward L-cystathionine. The D-term assignment is only computational (IEA:TreeGrafter), so it does not outweigh that evidence. The experimentally supported primary activity is not among the choices.

Citations as saved: [C5](#evidence-c5), [C8](#evidence-c8), [C10](#evidence-c10).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence is consistent with a PLP-dependent enzyme, but that broad family-level clue does not distinguish cystathionine gamma-lyase activity from related gamma-lyase activities with different substrate specificity.


**Missing item-specific fact**

> Whether this particular protein catalyzes a reaction on L-cystathionine; the cited experiments report that it does not and identify methionine gamma-lyase activity instead.


**Reason**

> The sequence and choices do not provide a reliable basis for resolving this specific substrate preference. The needed distinction depends on protein-specific functional characterization or an external annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The experimental evidence supports methionine gamma-lyase activity, which is not listed. None of the offered options is supported as the protein's primary activity by the supplied sequence alone; D is contradicted by the cited substrate-specificity evidence.


### Important caveats

- The reviewer-only database record matches the supplied sequence; that record and its annotations were not provided to the evaluated model.
- The cystathionine gamma-lyase annotation is computational, whereas the methionine gamma-lyase and lack-of-cystathionine-activity evidence is linked to experimental literature.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with a PLP-dependent enzyme, but that broad family-level clue does not distinguish cystathionine gamma-lyase activity from related gamma-lyase activities with different substrate specificity.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "Whether this particular protein catalyzes a reaction on L-cystathionine; the cited experiments report that it does not and identify methionine gamma-lyase activity instead.",
    "reason": "The sequence and choices do not provide a reliable basis for resolving this specific substrate preference. The needed distinction depends on protein-specific functional characterization or an external annotation."
  },
  "case_id": "GO_molecular_function_0154",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C8",
      "C10"
    ],
    "judgment": "contradicted",
    "reason": "The sequence-matched protein is experimentally annotated as an L-methionine gamma-lyase, and the cited functional evidence says it has no activity toward L-cystathionine. The D-term assignment is only computational (IEA:TreeGrafter), so it does not outweigh that evidence. The experimentally supported primary activity is not among the choices."
  },
  "important_caveats": [
    "The reviewer-only database record matches the supplied sequence; that record and its annotations were not provided to the evaluated model.",
    "The cystathionine gamma-lyase annotation is computational, whereas the methionine gamma-lyase and lack-of-cystathionine-activity evidence is linked to experimental literature."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The experimental evidence supports methionine gamma-lyase activity, which is not listed. None of the offered options is supported as the protein's primary activity by the supplied sequence alone; D is contradicted by the cited substrate-specificity evidence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0154",
  "expected_answer_check": {
    "judgment": "contradicted",
    "reason": "The sequence-matched protein is experimentally annotated as an L-methionine gamma-lyase, and the cited functional evidence says it has no activity toward L-cystathionine. The D-term assignment is only computational (IEA:TreeGrafter), so it does not outweigh that evidence. The experimentally supported primary activity is not among the choices.",
    "evidence_ids": ["C5", "C8", "C10"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence is consistent with a PLP-dependent enzyme, but that broad family-level clue does not distinguish cystathionine gamma-lyase activity from related gamma-lyase activities with different substrate specificity.",
    "missing_item_specific_fact": "Whether this particular protein catalyzes a reaction on L-cystathionine; the cited experiments report that it does not and identify methionine gamma-lyase activity instead.",
    "reason": "The sequence and choices do not provide a reliable basis for resolving this specific substrate preference. The needed distinction depends on protein-specific functional characterization or an external annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The experimental evidence supports methionine gamma-lyase activity, which is not listed. None of the offered options is supported as the protein's primary activity by the supplied sequence alone; D is contradicted by the cited substrate-specificity evidence."
  },
  "important_caveats": [
    "The reviewer-only database record matches the supplied sequence; that record and its annotations were not provided to the evaluated model.",
    "The cystathionine gamma-lyase annotation is computational, whereas the methionine gamma-lyase and lack-of-cystathionine-activity evidence is linked to experimental literature."
  ]
}
```

</details>

## Before: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: contradicted

> The protein (UniProt A0A2H1K3G9, L-methionine gamma-lyase from Brevibacterium aurantiacum) is experimentally confirmed (ECO:0000269, PubMed:9726878 and PubMed:30940696) to catalyze alpha,gamma-elimination of L-methionine (EC 4.4.1.11) and L-homocysteine (EC 4.4.1.2), but the FUNCTION comment explicitly states it 'has no activity toward L-cysteine, L-cystathionine, S-adenosyl-L-homocysteine and D-methionine.' The GO:0004123 (cystathionine gamma-lyase activity) annotation is solely IEA:TreeGrafter (computational homology inference) and is directly contradicted by experimental substrate-specificity data. The correct primary molecular function is methionine gamma-lyase activity (GO:0018826, EXP) or homocysteine desulfhydrase activity (GO:0047982, EXP), neither of which is offered as a choice.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [C9](#evidence-c9), [C10](#evidence-c10), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6), [H7](#evidence-h7), [H8](#evidence-h8), [H9](#evidence-h9).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains motifs characteristic of the Cys/Met metabolism PLP-dependent enzyme family (e.g., the conserved PLP-binding lysine region, the 'GGMKGL' and 'ETALAGLE' segments typical of this superfamily). A knowledgeable biologist can identify this as a pyridoxal-phosphate-dependent gamma-lyase acting on sulfur amino acids. Among the four choices: A (SAM binding) is a binding function, B (ubiquitin ligase) is a transferase/ligase, C (amidophosphoribosyltransferase) is a transferase — none are lyases. Only D (cystathionine gamma-lyase) is a PLP-dependent carbon-sulfur lyase on a sulfur amino acid, matching the mechanistic class identifiable from sequence.


**Missing item-specific fact**

> The precise substrate specificity (methionine vs. cystathionine vs. homocysteine) cannot be unambiguously determined from sequence alone. The correct substrate is L-methionine, not L-cystathionine, but the option 'methionine gamma-lyase activity' is not offered.


**Reason**

> A model can reason from sequence motifs to identify the mechanistic class (PLP-dependent gamma-lyase on sulfur amino acids) and select D by elimination of the three mechanistically unrelated options. However, the precise substrate assignment (cystathionine vs. methionine) would require specific knowledge, and the 'correct' answer is actually experimentally contradicted.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the four provided choices, only D falls within the correct mechanistic class (PLP-dependent carbon-sulfur lyase). A, B, and C are mechanistically unrelated (binding, ubiquitin ligase, amidotransferase). However, the question is fundamentally flawed because the experimentally correct answer (methionine gamma-lyase activity / homocysteine desulfhydrase activity) is not among the options, and the offered 'correct' answer (cystathionine gamma-lyase) is explicitly contradicted by experimental data.


### Important caveats

- The expected answer D is contradicted by experimental evidence: the protein has NO activity toward L-cystathionine (PubMed:9726878, PubMed:30940696). The GO:0004123 annotation is IEA:TreeGrafter only.
- The protein's true primary molecular function is L-methionine gamma-lyase activity (GO:0018826, EXP) and homocysteine desulfhydrase activity (GO:0047982, EXP). Neither is offered as a choice.
- The benchmark appears to have selected the GO:0004123 annotation from the database without recognizing it as a low-confidence computational inference contradicted by experimental data.
- The question is answerable by elimination (D is the only lyase option), but the 'correct' answer is scientifically inaccurate for this specific protein.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains motifs characteristic of the Cys/Met metabolism PLP-dependent enzyme family (e.g., the conserved PLP-binding lysine region, the 'GGMKGL' and 'ETALAGLE' segments typical of this superfamily). A knowledgeable biologist can identify this as a pyridoxal-phosphate-dependent gamma-lyase acting on sulfur amino acids. Among the four choices: A (SAM binding) is a binding function, B (ubiquitin ligase) is a transferase/ligase, C (amidophosphoribosyltransferase) is a transferase — none are lyases. Only D (cystathionine gamma-lyase) is a PLP-dependent carbon-sulfur lyase on a sulfur amino acid, matching the mechanistic class identifiable from sequence.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The precise substrate specificity (methionine vs. cystathionine vs. homocysteine) cannot be unambiguously determined from sequence alone. The correct substrate is L-methionine, not L-cystathionine, but the option 'methionine gamma-lyase activity' is not offered.",
    "reason": "A model can reason from sequence motifs to identify the mechanistic class (PLP-dependent gamma-lyase on sulfur amino acids) and select D by elimination of the three mechanistically unrelated options. However, the precise substrate assignment (cystathionine vs. methionine) would require specific knowledge, and the 'correct' answer is actually experimentally contradicted."
  },
  "case_id": "GO_molecular_function_0154",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "C7",
      "C8",
      "C9",
      "C10",
      "H4",
      "H5",
      "H6",
      "H7",
      "H8",
      "H9"
    ],
    "judgment": "contradicted",
    "reason": "The protein (UniProt A0A2H1K3G9, L-methionine gamma-lyase from Brevibacterium aurantiacum) is experimentally confirmed (ECO:0000269, PubMed:9726878 and PubMed:30940696) to catalyze alpha,gamma-elimination of L-methionine (EC 4.4.1.11) and L-homocysteine (EC 4.4.1.2), but the FUNCTION comment explicitly states it 'has no activity toward L-cysteine, L-cystathionine, S-adenosyl-L-homocysteine and D-methionine.' The GO:0004123 (cystathionine gamma-lyase activity) annotation is solely IEA:TreeGrafter (computational homology inference) and is directly contradicted by experimental substrate-specificity data. The correct primary molecular function is methionine gamma-lyase activity (GO:0018826, EXP) or homocysteine desulfhydrase activity (GO:0047982, EXP), neither of which is offered as a choice."
  },
  "important_caveats": [
    "The expected answer D is contradicted by experimental evidence: the protein has NO activity toward L-cystathionine (PubMed:9726878, PubMed:30940696). The GO:0004123 annotation is IEA:TreeGrafter only.",
    "The protein's true primary molecular function is L-methionine gamma-lyase activity (GO:0018826, EXP) and homocysteine desulfhydrase activity (GO:0047982, EXP). Neither is offered as a choice.",
    "The benchmark appears to have selected the GO:0004123 annotation from the database without recognizing it as a low-confidence computational inference contradicted by experimental data.",
    "The question is answerable by elimination (D is the only lyase option), but the 'correct' answer is scientifically inaccurate for this specific protein."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the four provided choices, only D falls within the correct mechanistic class (PLP-dependent carbon-sulfur lyase). A, B, and C are mechanistically unrelated (binding, ubiquitin ligase, amidotransferase). However, the question is fundamentally flawed because the experimentally correct answer (methionine gamma-lyase activity / homocysteine desulfhydrase activity) is not among the options, and the offered 'correct' answer (cystathionine gamma-lyase) is explicitly contradicted by experimental data."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0154",
  "expected_answer_check": {
    "judgment": "contradicted",
    "reason": "The protein (UniProt A0A2H1K3G9, L-methionine gamma-lyase from Brevibacterium aurantiacum) is experimentally confirmed (ECO:0000269, PubMed:9726878 and PubMed:30940696) to catalyze alpha,gamma-elimination of L-methionine (EC 4.4.1.11) and L-homocysteine (EC 4.4.1.2), but the FUNCTION comment explicitly states it 'has no activity toward L-cysteine, L-cystathionine, S-adenosyl-L-homocysteine and D-methionine.' The GO:0004123 (cystathionine gamma-lyase activity) annotation is solely IEA:TreeGrafter (computational homology inference) and is directly contradicted by experimental substrate-specificity data. The correct primary molecular function is methionine gamma-lyase activity (GO:0018826, EXP) or homocysteine desulfhydrase activity (GO:0047982, EXP), neither of which is offered as a choice.",
    "evidence_ids": ["C5", "C6", "C7", "C8", "C9", "C10", "H4", "H5", "H6", "H7", "H8", "H9"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains motifs characteristic of the Cys/Met metabolism PLP-dependent enzyme family (e.g., the conserved PLP-binding lysine region, the 'GGMKGL' and 'ETALAGLE' segments typical of this superfamily). A knowledgeable biologist can identify this as a pyridoxal-phosphate-dependent gamma-lyase acting on sulfur amino acids. Among the four choices: A (SAM binding) is a binding function, B (ubiquitin ligase) is a transferase/ligase, C (amidophosphoribosyltransferase) is a transferase — none are lyases. Only D (cystathionine gamma-lyase) is a PLP-dependent carbon-sulfur lyase on a sulfur amino acid, matching the mechanistic class identifiable from sequence.",
    "missing_item_specific_fact": "The precise substrate specificity (methionine vs. cystathionine vs. homocysteine) cannot be unambiguously determined from sequence alone. The correct substrate is L-methionine, not L-cystathionine, but the option 'methionine gamma-lyase activity' is not offered.",
    "reason": "A model can reason from sequence motifs to identify the mechanistic class (PLP-dependent gamma-lyase on sulfur amino acids) and select D by elimination of the three mechanistically unrelated options. However, the precise substrate assignment (cystathionine vs. methionine) would require specific knowledge, and the 'correct' answer is actually experimentally contradicted."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the four provided choices, only D falls within the correct mechanistic class (PLP-dependent carbon-sulfur lyase). A, B, and C are mechanistically unrelated (binding, ubiquitin ligase, amidotransferase). However, the question is fundamentally flawed because the experimentally correct answer (methionine gamma-lyase activity / homocysteine desulfhydrase activity) is not among the options, and the offered 'correct' answer (cystathionine gamma-lyase) is explicitly contradicted by experimental data."
  },
  "important_caveats": [
    "The expected answer D is contradicted by experimental evidence: the protein has NO activity toward L-cystathionine (PubMed:9726878, PubMed:30940696). The GO:0004123 annotation is IEA:TreeGrafter only.",
    "The protein's true primary molecular function is L-methionine gamma-lyase activity (GO:0018826, EXP) and homocysteine desulfhydrase activity (GO:0047982, EXP). Neither is offered as a choice.",
    "The benchmark appears to have selected the GO:0004123 annotation from the database without recognizing it as a low-confidence computational inference contradicted by experimental data.",
    "The question is answerable by elimination (D is the only lyase option), but the 'correct' answer is scientifically inaccurate for this specific protein."
  ]
}
```

</details>

## After: GPT-6 Luna

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: contradicted

> The sequence-matched record reports experimentally supported L-methionine gamma-lyase activity and says the protein has no activity toward L-cystathionine, the substrate required for cystathionine gamma-lyase activity. The key's GO annotation is computationally transferred and does not outweigh this substrate-specific evidence.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C8](#evidence-c8).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence is consistent with a PLP-dependent gamma-lyase family enzyme, making D more plausible than the unrelated SAM-binding, ubiquitin-ligase, and amidophosphoribosyltransferase choices. But family membership alone does not establish that this enzyme acts on cystathionine rather than another substrate.


**Missing item-specific fact**

> Whether this particular enzyme catalyzes cystathionine cleavage or instead has a different substrate specificity.


**Reason**

> Transferable family knowledge points toward D as the closest offered option, but the question asks for a specific molecular activity, and the sequence alone does not resolve the substrate-specific distinction that determines whether D is correct.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> No other listed option is a plausible description of the enzyme family, although the closest option, D, does not match the reported substrate specificity.


### Important caveats

- The evidence supports a different activity, methionine gamma-lyase, which is not offered as an option.
- The exact author annotation snapshot is unknown; the sequence match supports applicability of the cited record to the supplied sequence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with a PLP-dependent gamma-lyase family enzyme, making D more plausible than the unrelated SAM-binding, ubiquitin-ligase, and amidophosphoribosyltransferase choices. But family membership alone does not establish that this enzyme acts on cystathionine rather than another substrate.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "Whether this particular enzyme catalyzes cystathionine cleavage or instead has a different substrate specificity.",
    "reason": "Transferable family knowledge points toward D as the closest offered option, but the question asks for a specific molecular activity, and the sequence alone does not resolve the substrate-specific distinction that determines whether D is correct."
  },
  "case_id": "GO_molecular_function_0154",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "C8"
    ],
    "judgment": "contradicted",
    "reason": "The sequence-matched record reports experimentally supported L-methionine gamma-lyase activity and says the protein has no activity toward L-cystathionine, the substrate required for cystathionine gamma-lyase activity. The key's GO annotation is computationally transferred and does not outweigh this substrate-specific evidence."
  },
  "important_caveats": [
    "The evidence supports a different activity, methionine gamma-lyase, which is not offered as an option.",
    "The exact author annotation snapshot is unknown; the sequence match supports applicability of the cited record to the supplied sequence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No other listed option is a plausible description of the enzyme family, although the closest option, D, does not match the reported substrate specificity."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0154",
  "expected_answer_check": {
    "judgment": "contradicted",
    "reason": "The sequence-matched record reports experimentally supported L-methionine gamma-lyase activity and says the protein has no activity toward L-cystathionine, the substrate required for cystathionine gamma-lyase activity. The key's GO annotation is computationally transferred and does not outweigh this substrate-specific evidence.",
    "evidence_ids": ["C5", "C6", "C8"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence is consistent with a PLP-dependent gamma-lyase family enzyme, making D more plausible than the unrelated SAM-binding, ubiquitin-ligase, and amidophosphoribosyltransferase choices. But family membership alone does not establish that this enzyme acts on cystathionine rather than another substrate.",
    "missing_item_specific_fact": "Whether this particular enzyme catalyzes cystathionine cleavage or instead has a different substrate specificity.",
    "reason": "Transferable family knowledge points toward D as the closest offered option, but the question asks for a specific molecular activity, and the sequence alone does not resolve the substrate-specific distinction that determines whether D is correct."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No other listed option is a plausible description of the enzyme family, although the closest option, D, does not match the reported substrate specificity."
  },
  "important_caveats": [
    "The evidence supports a different activity, methionine gamma-lyase, which is not offered as an option.",
    "The exact author annotation snapshot is unknown; the sequence match supports applicability of the cited record to the supplied sequence."
  ]
}
```

</details>

## After: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: contradicted

> The expected answer D (cystathionine gamma-lyase activity, GO:0004123) is contradicted by experimental evidence. The UniProt entry (A0A2H1K3G9) annotates this protein as L-methionine gamma-lyase (EC 4.4.1.11) with experimental evidence (PubMed:30940696, PubMed:9726878), and the FUNCTION comment explicitly states it 'has no activity toward L-cysteine, L-cystathionine, S-adenosyl-L-homocysteine and D-methionine.' The GO:0004123 annotation is only IEA:TreeGrafter (computational similarity transfer), while the experimentally supported GO terms are GO:0018826 (methionine gamma-lyase activity, EXP) and GO:0047982 (homocysteine desulfhydrase activity, EXP). GO:0004123 is defined as 'Catalysis of the reaction: L-cystathionine + H2O = 2-oxobutanoate + L-cysteine + NH4+', which this protein explicitly cannot perform.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [C9](#evidence-c9), [C10](#evidence-c10), [GO2](#evidence-go2), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6), [H7](#evidence-h7), [H8](#evidence-h8), [H9](#evidence-h9).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> A knowledgeable model can recognize PLP-binding sequence features in this ~406-aa protein (e.g., the 'GGMKGL' region near the N-terminus consistent with the PLP-binding lysine motif in fold-type I PLP enzymes, and overall architecture resembling the Cys/Met metabolism PLP-dependent enzyme family). This eliminates option B (ubiquitin protein ligase activity — E3 ligases have RING/U-box/HECT folds, not PLP-dependent fold-type I) and option C (amidophosphoribosyltransferase activity — a glutamine amidotransferase with a completely different fold and no PLP requirement). Option A (SAM binding) is a binding activity associated with radical SAM enzymes (CX3CX2C motif) or methyltransferases, not a PLP-dependent catalytic enzyme. Among the four options, D (cystathionine gamma-lyase activity) is the only PLP-dependent catalytic lyase activity, making it the sole option consistent with the recognized enzyme family. The model can reach D through family-level inference without knowing this protein's specific substrate specificity.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Family recognition of the PLP-dependent Cys/Met metabolism enzyme fold meaningfully distinguishes D from the other three options. The model does not need to know this exact protein's experimental substrate profile; recognizing the PLP-binding architecture and fold-type I characteristics is sufficient to eliminate A (binding, different fold), B (E3 ligase fold), and C (amidotransferase fold), leaving D as the only PLP-dependent catalytic option. However, this reasoning path, while valid for distinguishing among the offered choices, leads to a factually incorrect answer because the protein is a methionine gamma-lyase, not a cystathionine gamma-lyase.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the four offered options, only D is consistent with a PLP-dependent lyase fold. A, B, and C describe fundamentally different enzyme classes and folds. No ambiguity exists among the offered choices for a model performing family-level reasoning. The issue is not ambiguity among options but that the correct answer (methionine gamma-lyase activity) is not offered.


### Important caveats

- The expected answer D is contradicted by experimental evidence: the protein explicitly has NO activity toward L-cystathionine. The GO:0004123 annotation is computational (IEA:TreeGrafter), not experimental.
- The experimentally verified molecular function is L-methionine gamma-lyase activity (GO:0018826, EXP) and homocysteine desulfhydrase activity (GO:0047982, EXP), neither of which is offered as a choice.
- The reasoning path to D is valid for eliminating the other three options based on fold/family recognition, but it leads to a factually incorrect assignment of substrate specificity within the PLP-dependent Cys/Met metabolism enzyme family.
- Cystathionine gamma-lyase (EC 4.4.1.1) and methionine gamma-lyase (EC 4.4.1.11) are closely related PLP enzymes in the same family, making the computational annotation error understandable but factually wrong for this specific protein.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "A knowledgeable model can recognize PLP-binding sequence features in this ~406-aa protein (e.g., the 'GGMKGL' region near the N-terminus consistent with the PLP-binding lysine motif in fold-type I PLP enzymes, and overall architecture resembling the Cys/Met metabolism PLP-dependent enzyme family). This eliminates option B (ubiquitin protein ligase activity — E3 ligases have RING/U-box/HECT folds, not PLP-dependent fold-type I) and option C (amidophosphoribosyltransferase activity — a glutamine amidotransferase with a completely different fold and no PLP requirement). Option A (SAM binding) is a binding activity associated with radical SAM enzymes (CX3CX2C motif) or methyltransferases, not a PLP-dependent catalytic enzyme. Among the four options, D (cystathionine gamma-lyase activity) is the only PLP-dependent catalytic lyase activity, making it the sole option consistent with the recognized enzyme family. The model can reach D through family-level inference without knowing this protein's specific substrate specificity.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Family recognition of the PLP-dependent Cys/Met metabolism enzyme fold meaningfully distinguishes D from the other three options. The model does not need to know this exact protein's experimental substrate profile; recognizing the PLP-binding architecture and fold-type I characteristics is sufficient to eliminate A (binding, different fold), B (E3 ligase fold), and C (amidotransferase fold), leaving D as the only PLP-dependent catalytic option. However, this reasoning path, while valid for distinguishing among the offered choices, leads to a factually incorrect answer because the protein is a methionine gamma-lyase, not a cystathionine gamma-lyase."
  },
  "case_id": "GO_molecular_function_0154",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C7",
      "C8",
      "C9",
      "C10",
      "GO2",
      "H4",
      "H5",
      "H6",
      "H7",
      "H8",
      "H9"
    ],
    "judgment": "contradicted",
    "reason": "The expected answer D (cystathionine gamma-lyase activity, GO:0004123) is contradicted by experimental evidence. The UniProt entry (A0A2H1K3G9) annotates this protein as L-methionine gamma-lyase (EC 4.4.1.11) with experimental evidence (PubMed:30940696, PubMed:9726878), and the FUNCTION comment explicitly states it 'has no activity toward L-cysteine, L-cystathionine, S-adenosyl-L-homocysteine and D-methionine.' The GO:0004123 annotation is only IEA:TreeGrafter (computational similarity transfer), while the experimentally supported GO terms are GO:0018826 (methionine gamma-lyase activity, EXP) and GO:0047982 (homocysteine desulfhydrase activity, EXP). GO:0004123 is defined as 'Catalysis of the reaction: L-cystathionine + H2O = 2-oxobutanoate + L-cysteine + NH4+', which this protein explicitly cannot perform."
  },
  "important_caveats": [
    "The expected answer D is contradicted by experimental evidence: the protein explicitly has NO activity toward L-cystathionine. The GO:0004123 annotation is computational (IEA:TreeGrafter), not experimental.",
    "The experimentally verified molecular function is L-methionine gamma-lyase activity (GO:0018826, EXP) and homocysteine desulfhydrase activity (GO:0047982, EXP), neither of which is offered as a choice.",
    "The reasoning path to D is valid for eliminating the other three options based on fold/family recognition, but it leads to a factually incorrect assignment of substrate specificity within the PLP-dependent Cys/Met metabolism enzyme family.",
    "Cystathionine gamma-lyase (EC 4.4.1.1) and methionine gamma-lyase (EC 4.4.1.11) are closely related PLP enzymes in the same family, making the computational annotation error understandable but factually wrong for this specific protein."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the four offered options, only D is consistent with a PLP-dependent lyase fold. A, B, and C describe fundamentally different enzyme classes and folds. No ambiguity exists among the offered choices for a model performing family-level reasoning. The issue is not ambiguity among options but that the correct answer (methionine gamma-lyase activity) is not offered."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0154",
  "expected_answer_check": {
    "judgment": "contradicted",
    "reason": "The expected answer D (cystathionine gamma-lyase activity, GO:0004123) is contradicted by experimental evidence. The UniProt entry (A0A2H1K3G9) annotates this protein as L-methionine gamma-lyase (EC 4.4.1.11) with experimental evidence (PubMed:30940696, PubMed:9726878), and the FUNCTION comment explicitly states it 'has no activity toward L-cysteine, L-cystathionine, S-adenosyl-L-homocysteine and D-methionine.' The GO:0004123 annotation is only IEA:TreeGrafter (computational similarity transfer), while the experimentally supported GO terms are GO:0018826 (methionine gamma-lyase activity, EXP) and GO:0047982 (homocysteine desulfhydrase activity, EXP). GO:0004123 is defined as 'Catalysis of the reaction: L-cystathionine + H2O = 2-oxobutanoate + L-cysteine + NH4+', which this protein explicitly cannot perform.",
    "evidence_ids": ["C4", "C5", "C6", "C7", "C8", "C9", "C10", "GO2", "H4", "H5", "H6", "H7", "H8", "H9"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "A knowledgeable model can recognize PLP-binding sequence features in this ~406-aa protein (e.g., the 'GGMKGL' region near the N-terminus consistent with the PLP-binding lysine motif in fold-type I PLP enzymes, and overall architecture resembling the Cys/Met metabolism PLP-dependent enzyme family). This eliminates option B (ubiquitin protein ligase activity — E3 ligases have RING/U-box/HECT folds, not PLP-dependent fold-type I) and option C (amidophosphoribosyltransferase activity — a glutamine amidotransferase with a completely different fold and no PLP requirement). Option A (SAM binding) is a binding activity associated with radical SAM enzymes (CX3CX2C motif) or methyltransferases, not a PLP-dependent catalytic enzyme. Among the four options, D (cystathionine gamma-lyase activity) is the only PLP-dependent catalytic lyase activity, making it the sole option consistent with the recognized enzyme family. The model can reach D through family-level inference without knowing this protein's specific substrate specificity.",
    "missing_item_specific_fact": "",
    "reason": "Family recognition of the PLP-dependent Cys/Met metabolism enzyme fold meaningfully distinguishes D from the other three options. The model does not need to know this exact protein's experimental substrate profile; recognizing the PLP-binding architecture and fold-type I characteristics is sufficient to eliminate A (binding, different fold), B (E3 ligase fold), and C (amidotransferase fold), leaving D as the only PLP-dependent catalytic option. However, this reasoning path, while valid for distinguishing among the offered choices, leads to a factually incorrect answer because the protein is a methionine gamma-lyase, not a cystathionine gamma-lyase."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the four offered options, only D is consistent with a PLP-dependent lyase fold. A, B, and C describe fundamentally different enzyme classes and folds. No ambiguity exists among the offered choices for a model performing family-level reasoning. The issue is not ambiguity among options but that the correct answer (methionine gamma-lyase activity) is not offered."
  },
  "important_caveats": [
    "The expected answer D is contradicted by experimental evidence: the protein explicitly has NO activity toward L-cystathionine. The GO:0004123 annotation is computational (IEA:TreeGrafter), not experimental.",
    "The experimentally verified molecular function is L-methionine gamma-lyase activity (GO:0018826, EXP) and homocysteine desulfhydrase activity (GO:0047982, EXP), neither of which is offered as a choice.",
    "The reasoning path to D is valid for eliminating the other three options based on fold/family recognition, but it leads to a factually incorrect assignment of substrate specificity within the PLP-dependent Cys/Met metabolism enzyme family.",
    "Cystathionine gamma-lyase (EC 4.4.1.1) and methionine gamma-lyase (EC 4.4.1.11) are closely related PLP enzymes in the same family, making the computational annotation error understandable but factually wrong for this specific protein."
  ]
}
```

</details>

## Existing project source checks of the old Luna review only

These unchanged notes concern the earlier Luna claims. They do not validate either new review or the old Qwen review. No new scientific adjudication was performed.

## Project source-check notes

These project-authored, AI-assisted checks assess specific source claims. They are not expert adjudication and do not replace Luna’s saved review or the author key.

### Source check 1

**Check:** `explicit_negative_substrate_evidence_traced`.

> C5 explicitly reports no activity toward L-cystathionine, while describing L-methionine gamma-lyase activity. C8 still assigns the keyed cystathionine gamma-lyase term via IEA:TreeGrafter; C10 assigns methionine gamma-lyase with EXP evidence. The negative-substrate statement is genuinely present and applies to the exact matched sequence.

**Remaining uncertainty:** The cited primary papers and assay conditions were not independently reviewed. This source trace preserves, rather than replaces, the model contradiction judgment.

Evidence checked: [C5](#evidence-c5), [C8](#evidence-c8), [C10](#evidence-c10).

## Complete reviewer-only evidence and qualifications

All excerpts supplied in the original and revised reviewer user message follow. This material was not available to the original evaluated model. Accession identity came from dataset image-path metadata. Source support and transferable discrimination are separate judgments.

**Applicability metadata, unchanged:**

```json
{
  "requested_accession": "A0A2H1K3G9",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "benchmark_sequence_sha256": "435ffd3b8e0f97253809f6299a192824acbc91b3f9ba8e80c96d087a48e0a9a8",
  "benchmark_sequence_length": 406,
  "current_status": "retrieved",
  "current_sequence_comparison": "matched",
  "current_entry_audit": {
    "entryVersion": 34,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2018-01-31",
    "sequenceVersion": 1
  },
  "current_uniprot_release": "2026_03",
  "current_record_sha256": "a920c3d8a2606b869b1968d0c8b2153e5ed89fbf0c4578d7222ed95845d1c3a6",
  "current_source_sequence_sha256": "435ffd3b8e0f97253809f6299a192824acbc91b3f9ba8e80c96d087a48e0a9a8",
  "current_source_sequence_length": 406,
  "historical_status": "retrieved",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "selected_historical_entry_version": 32,
  "selected_historical_version": {
    "accession": "A0A2H1K3G9",
    "database": "Swiss-Prot",
    "entryVersion": 32,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "MEGL_BREAU",
    "sequenceVersion": 1
  },
  "selected_historical_record_sha256": "9f8f2097c25cd1b2756007ac83a5f1a172b3bde4aa3f977e22144a88c5ee6f0b",
  "selected_historical_source_sequence_sha256": "435ffd3b8e0f97253809f6299a192824acbc91b3f9ba8e80c96d087a48e0a9a8",
  "selected_historical_source_sequence_length": 406,
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
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2H1K3G9.json)

```json
{
  "evidence_id": "C1",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2H1K3G9.json",
  "source_sha256": "a920c3d8a2606b869b1968d0c8b2153e5ed89fbf0c4578d7222ed95845d1c3a6",
  "retrieved_utc": "2026-11-01T06:24:44.554855+00:00",
  "json_pointer": "/primaryAccession",
  "excerpt": "\"A0A2H1K3G9\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2H1K3G9.json)

```json
{
  "evidence_id": "C2",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2H1K3G9.json",
  "source_sha256": "a920c3d8a2606b869b1968d0c8b2153e5ed89fbf0c4578d7222ed95845d1c3a6",
  "retrieved_utc": "2026-11-01T06:24:44.554855+00:00",
  "json_pointer": "/entryAudit",
  "excerpt": "{\"entryVersion\":34,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2018-01-31\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2H1K3G9.json)

```json
{
  "evidence_id": "C3",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2H1K3G9.json",
  "source_sha256": "a920c3d8a2606b869b1968d0c8b2153e5ed89fbf0c4578d7222ed95845d1c3a6",
  "retrieved_utc": "2026-11-01T06:24:44.554855+00:00",
  "json_pointer": "/organism",
  "excerpt": "{\"lineage\":[\"Bacteria\",\"Bacillati\",\"Actinomycetota\",\"Actinomycetes\",\"Micrococcales\",\"Brevibacteriaceae\",\"Brevibacterium\"],\"scientificName\":\"Brevibacterium aurantiacum\",\"taxonId\":273384}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2H1K3G9.json)

```json
{
  "evidence_id": "C4",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2H1K3G9.json",
  "source_sha256": "a920c3d8a2606b869b1968d0c8b2153e5ed89fbf0c4578d7222ed95845d1c3a6",
  "retrieved_utc": "2026-11-01T06:24:44.554855+00:00",
  "json_pointer": "/proteinDescription",
  "excerpt": "{\"alternativeNames\":[{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"30940696\",\"source\":\"PubMed\"}],\"value\":\"4.4.1.2\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"30940696\",\"source\":\"PubMed\"}],\"value\":\"Homocysteine desulfhydrase\"}},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"30940696\",\"source\":\"PubMed\"}],\"value\":\"MGL-BL929\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"30940696\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"9726878\",\"source\":\"PubMed\"}],\"value\":\"4.4.1.11\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"30940696\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000303\",\"id\":\"9726878\",\"source\":\"PubMed\"}],\"value\":\"L-methionine gamma-lyase\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"30940696\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000303\",\"id\":\"9726878\",\"source\":\"PubMed\"}],\"value\":\"MGL\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2H1K3G9.json)

```json
{
  "evidence_id": "C5",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2H1K3G9.json",
  "source_sha256": "a920c3d8a2606b869b1968d0c8b2153e5ed89fbf0c4578d7222ed95845d1c3a6",
  "retrieved_utc": "2026-11-01T06:24:44.554855+00:00",
  "json_pointer": "/comments/0",
  "excerpt": "{\"commentType\":\"FUNCTION\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"30940696\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"9726878\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000305\",\"id\":\"9726878\",\"source\":\"PubMed\"}],\"value\":\"Catalyzes the alpha,gamma-elimination of L-methionine to produce methanethiol, 2-oxobutanoate and ammonia (PubMed:30940696, PubMed:9726878). May be responsible for the production of methanethiol associated with desirable Cheddar-type sulfur notes during cheese ripening (Probable). Is also able to catalyze the alpha,gamma-elimination of L-homocysteine and DL-selenomethionine, but has no activity toward L-cysteine, L-cystathionine, S-adenosyl-L-homocysteine and D-methionine (PubMed:30940696, PubMed:9726878)\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2H1K3G9.json)

```json
{
  "evidence_id": "C6",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2H1K3G9.json",
  "source_sha256": "a920c3d8a2606b869b1968d0c8b2153e5ed89fbf0c4578d7222ed95845d1c3a6",
  "retrieved_utc": "2026-11-01T06:24:44.554855+00:00",
  "json_pointer": "/comments/1",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"30940696\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:23801\"}}],\"reaction\":{\"ecNumber\":\"4.4.1.11\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"30940696\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"9726878\",\"source\":\"PubMed\"}],\"name\":\"L-methionine + H2O = methanethiol + 2-oxobutanoate + NH4(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:23800\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:16007\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:16763\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:28938\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57844\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2H1K3G9.json)

```json
{
  "evidence_id": "C7",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2H1K3G9.json",
  "source_sha256": "a920c3d8a2606b869b1968d0c8b2153e5ed89fbf0c4578d7222ed95845d1c3a6",
  "retrieved_utc": "2026-11-01T06:24:44.554855+00:00",
  "json_pointer": "/comments/2",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"30940696\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:14502\"}}],\"reaction\":{\"ecNumber\":\"4.4.1.2\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"30940696\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"9726878\",\"source\":\"PubMed\"}],\"name\":\"L-homocysteine + H2O = 2-oxobutanoate + hydrogen sulfide + NH4(+) + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:14501\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:16763\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:28938\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:29919\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:58199\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2H1K3G9.json)

```json
{
  "evidence_id": "C8",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2H1K3G9.json",
  "source_sha256": "a920c3d8a2606b869b1968d0c8b2153e5ed89fbf0c4578d7222ed95845d1c3a6",
  "retrieved_utc": "2026-11-01T06:24:44.554855+00:00",
  "json_pointer": "/uniProtKBCrossReferences/12",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0004123\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"F:cystathionine gamma-lyase activity\"},{\"key\":\"GoEvidenceType\",\"value\":\"IEA:TreeGrafter\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2H1K3G9.json)

```json
{
  "evidence_id": "C9",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2H1K3G9.json",
  "source_sha256": "a920c3d8a2606b869b1968d0c8b2153e5ed89fbf0c4578d7222ed95845d1c3a6",
  "retrieved_utc": "2026-11-01T06:24:44.554855+00:00",
  "json_pointer": "/uniProtKBCrossReferences/13",
  "excerpt": "{\"database\":\"GO\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"30940696\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"9726878\",\"source\":\"PubMed\"}],\"id\":\"GO:0047982\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"F:homocysteine desulfhydrase activity\"},{\"key\":\"GoEvidenceType\",\"value\":\"EXP:UniProtKB\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2H1K3G9.json)

```json
{
  "evidence_id": "C10",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2H1K3G9.json",
  "source_sha256": "a920c3d8a2606b869b1968d0c8b2153e5ed89fbf0c4578d7222ed95845d1c3a6",
  "retrieved_utc": "2026-11-01T06:24:44.554855+00:00",
  "json_pointer": "/uniProtKBCrossReferences/14",
  "excerpt": "{\"database\":\"GO\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"30940696\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"9726878\",\"source\":\"PubMed\"}],\"id\":\"GO:0018826\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"F:methionine gamma-lyase activity\"},{\"key\":\"GoEvidenceType\",\"value\":\"EXP:UniProtKB\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2H1K3G9.json)

```json
{
  "evidence_id": "C11",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2H1K3G9.json",
  "source_sha256": "a920c3d8a2606b869b1968d0c8b2153e5ed89fbf0c4578d7222ed95845d1c3a6",
  "retrieved_utc": "2026-11-01T06:24:44.554855+00:00",
  "json_pointer": "/uniProtKBCrossReferences/15",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0030170\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"F:pyridoxal phosphate binding\"},{\"key\":\"GoEvidenceType\",\"value\":\"IEA:InterPro\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2H1K3G9.json)

```json
{
  "evidence_id": "C12",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2H1K3G9.json",
  "source_sha256": "a920c3d8a2606b869b1968d0c8b2153e5ed89fbf0c4578d7222ed95845d1c3a6",
  "retrieved_utc": "2026-11-01T06:24:44.554855+00:00",
  "json_pointer": "/references/1",
  "excerpt": "{\"citation\":{\"authors\":[\"Dias B.\",\"Weimer B.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"9726878\"},{\"database\":\"DOI\",\"id\":\"10.1128/aem.64.9.3327-3331.1998\"}],\"citationType\":\"journal article\",\"firstPage\":\"3327\",\"id\":\"9726878\",\"journal\":\"Appl. Environ. Microbiol.\",\"lastPage\":\"3331\",\"publicationDate\":\"1998\",\"title\":\"Purification and characterization of L-methionine gamma-lyase from brevibacterium linens BL2.\",\"volume\":\"64\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"BL2\"}],\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"COFACTOR\",\"SUBSTRATE SPECIFICITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"ACTIVITY REGULATION\",\"SUBUNIT\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C13

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2H1K3G9.json)

```json
{
  "evidence_id": "C13",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2H1K3G9.json",
  "source_sha256": "a920c3d8a2606b869b1968d0c8b2153e5ed89fbf0c4578d7222ed95845d1c3a6",
  "retrieved_utc": "2026-11-01T06:24:44.554855+00:00",
  "json_pointer": "/references/2",
  "excerpt": "{\"citation\":{\"authors\":[\"Machover D.\",\"Rossi L.\",\"Hamelin J.\",\"Desterke C.\",\"Goldschmidt E.\",\"Chadefaux-Vekemans B.\",\"Bonnarme P.\",\"Briozzo P.\",\"Kopecny D.\",\"Pierige F.\",\"Magnani M.\",\"Mollicone R.\",\"Haghighi-Rad F.\",\"Gaston-Mathe Y.\",\"Dairou J.\",\"Boucheix C.\",\"Saffroy R.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"30940696\"},{\"database\":\"DOI\",\"id\":\"10.1124/jpet.119.256537\"}],\"citationType\":\"journal article\",\"firstPage\":\"489\",\"id\":\"30940696\",\"journal\":\"J. Pharmacol. Exp. Ther.\",\"lastPage\":\"502\",\"publicationDate\":\"2019\",\"title\":\"Effects in Cancer Cells of the Recombinant L-Methionine Gamma-Lyase from Brevibacterium aurantiacum. Encapsulation in Human Erythrocytes for Sustained L-Methionine Elimination.\",\"volume\":\"369\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"ATCC 9175 / DSM 20426 / JCM 2590 / NBRC 12171 / NCDO 739 / NCIMB 8546 / KC\"}],\"referenceNumber\":3,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"COFACTOR\",\"SUBSTRATE SPECIFICITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"SUBUNIT\",\"BIOTECHNOLOGY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2H1K3G9?format=txt&versions=32)

```json
{
  "evidence_id": "H1",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A2H1K3G9?format=txt&versions=32",
  "source_sha256": "9f8f2097c25cd1b2756007ac83a5f1a172b3bde4aa3f977e22144a88c5ee6f0b",
  "retrieved_utc": "2026-11-01T06:27:25.782043+00:00",
  "source_locator": "lines 1-19",
  "excerpt": "ID   MEGL_BREAU              Reviewed;         406 AA.\nAC   A0A2H1K3G9;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   31-JAN-2018, sequence version 1.\nDT   28-JAN-2026, entry version 32.\nDE   RecName: Full=L-methionine gamma-lyase {ECO:0000303|PubMed:30940696, ECO:0000303|PubMed:9726878};\nDE            Short=MGL {ECO:0000303|PubMed:30940696, ECO:0000303|PubMed:9726878};\nDE            EC=4.4.1.11 {ECO:0000269|PubMed:30940696, ECO:0000269|PubMed:9726878};\nDE   AltName: Full=Homocysteine desulfhydrase {ECO:0000303|PubMed:30940696};\nDE            EC=4.4.1.2 {ECO:0000269|PubMed:30940696};\nDE   AltName: Full=MGL-BL929 {ECO:0000303|PubMed:30940696};\nGN   ORFNames=BAUR9175_03070 {ECO:0000312|EMBL:SMX94104.1},\nGN   BAUR920_03040 {ECO:0000312|EMBL:SMX97377.1},\nGN   BAURA63_02933 {ECO:0000312|EMBL:SMX94451.1},\nGN   BAURA86_00394 {ECO:0000312|EMBL:SMX72154.1};\nOS   Brevibacterium aurantiacum.\nOC   Bacteria; Bacillati; Actinomycetota; Actinomycetes; Micrococcales;\nOC   Brevibacteriaceae; Brevibacterium.\nOX   NCBI_TaxID=273384;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 32,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2H1K3G9?format=txt&versions=32)

```json
{
  "evidence_id": "H2",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A2H1K3G9?format=txt&versions=32",
  "source_sha256": "9f8f2097c25cd1b2756007ac83a5f1a172b3bde4aa3f977e22144a88c5ee6f0b",
  "retrieved_utc": "2026-11-01T06:27:25.782043+00:00",
  "source_locator": "lines 27-35",
  "excerpt": "RN   [2]\nRP   FUNCTION, CATALYTIC ACTIVITY, COFACTOR, SUBSTRATE SPECIFICITY,\nRP   BIOPHYSICOCHEMICAL PROPERTIES, ACTIVITY REGULATION, AND SUBUNIT.\nRC   STRAIN=BL2;\nRX   PubMed=9726878; DOI=10.1128/aem.64.9.3327-3331.1998;\nRA   Dias B., Weimer B.;\nRT   \"Purification and characterization of L-methionine gamma-lyase from\nRT   brevibacterium linens BL2.\";\nRL   Appl. Environ. Microbiol. 64:3327-3331(1998).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 32,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2H1K3G9?format=txt&versions=32)

```json
{
  "evidence_id": "H3",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A2H1K3G9?format=txt&versions=32",
  "source_sha256": "9f8f2097c25cd1b2756007ac83a5f1a172b3bde4aa3f977e22144a88c5ee6f0b",
  "retrieved_utc": "2026-11-01T06:27:25.782043+00:00",
  "source_locator": "lines 36-49",
  "excerpt": "RN   [3]\nRP   FUNCTION, CATALYTIC ACTIVITY, COFACTOR, SUBSTRATE SPECIFICITY,\nRP   BIOPHYSICOCHEMICAL PROPERTIES, SUBUNIT, AND BIOTECHNOLOGY.\nRC   STRAIN=ATCC 9175 / DSM 20426 / JCM 2590 / NBRC 12171 / NCDO 739 / NCIMB\nRC   8546 / KC;\nRX   PubMed=30940696; DOI=10.1124/jpet.119.256537;\nRA   Machover D., Rossi L., Hamelin J., Desterke C., Goldschmidt E.,\nRA   Chadefaux-Vekemans B., Bonnarme P., Briozzo P., Kopecny D., Pierige F.,\nRA   Magnani M., Mollicone R., Haghighi-Rad F., Gaston-Mathe Y., Dairou J.,\nRA   Boucheix C., Saffroy R.;\nRT   \"Effects in Cancer Cells of the Recombinant L-Methionine Gamma-Lyase from\nRT   Brevibacterium aurantiacum. Encapsulation in Human Erythrocytes for\nRT   Sustained L-Methionine Elimination.\";\nRL   J. Pharmacol. Exp. Ther. 369:489-502(2019).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 32,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2H1K3G9?format=txt&versions=32)

```json
{
  "evidence_id": "H4",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A2H1K3G9?format=txt&versions=32",
  "source_sha256": "9f8f2097c25cd1b2756007ac83a5f1a172b3bde4aa3f977e22144a88c5ee6f0b",
  "retrieved_utc": "2026-11-01T06:27:25.782043+00:00",
  "source_locator": "lines 50-59",
  "excerpt": "CC   -!- FUNCTION: Catalyzes the alpha,gamma-elimination of L-methionine to\nCC       produce methanethiol, 2-oxobutanoate and ammonia (PubMed:30940696,\nCC       PubMed:9726878). May be responsible for the production of methanethiol\nCC       associated with desirable Cheddar-type sulfur notes during cheese\nCC       ripening (Probable). Is also able to catalyze the alpha,gamma-\nCC       elimination of L-homocysteine and DL-selenomethionine, but has no\nCC       activity toward L-cysteine, L-cystathionine, S-adenosyl-L-homocysteine\nCC       and D-methionine (PubMed:30940696, PubMed:9726878).\nCC       {ECO:0000269|PubMed:30940696, ECO:0000269|PubMed:9726878,\nCC       ECO:0000305|PubMed:9726878}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 32,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2H1K3G9?format=txt&versions=32)

```json
{
  "evidence_id": "H5",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A2H1K3G9?format=txt&versions=32",
  "source_sha256": "9f8f2097c25cd1b2756007ac83a5f1a172b3bde4aa3f977e22144a88c5ee6f0b",
  "retrieved_utc": "2026-11-01T06:27:25.782043+00:00",
  "source_locator": "lines 60-66",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=L-methionine + H2O = methanethiol + 2-oxobutanoate + NH4(+);\nCC         Xref=Rhea:RHEA:23800, ChEBI:CHEBI:15377, ChEBI:CHEBI:16007,\nCC         ChEBI:CHEBI:16763, ChEBI:CHEBI:28938, ChEBI:CHEBI:57844; EC=4.4.1.11;\nCC         Evidence={ECO:0000269|PubMed:30940696, ECO:0000269|PubMed:9726878};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:23801;\nCC         Evidence={ECO:0000269|PubMed:30940696};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 32,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2H1K3G9?format=txt&versions=32)

```json
{
  "evidence_id": "H6",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A2H1K3G9?format=txt&versions=32",
  "source_sha256": "9f8f2097c25cd1b2756007ac83a5f1a172b3bde4aa3f977e22144a88c5ee6f0b",
  "retrieved_utc": "2026-11-01T06:27:25.782043+00:00",
  "source_locator": "lines 67-74",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=L-homocysteine + H2O = 2-oxobutanoate + hydrogen sulfide +\nCC         NH4(+) + H(+); Xref=Rhea:RHEA:14501, ChEBI:CHEBI:15377,\nCC         ChEBI:CHEBI:15378, ChEBI:CHEBI:16763, ChEBI:CHEBI:28938,\nCC         ChEBI:CHEBI:29919, ChEBI:CHEBI:58199; EC=4.4.1.2;\nCC         Evidence={ECO:0000269|PubMed:30940696, ECO:0000269|PubMed:9726878};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:14502;\nCC         Evidence={ECO:0000305|PubMed:30940696};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 32,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2H1K3G9?format=txt&versions=32)

```json
{
  "evidence_id": "H7",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A2H1K3G9?format=txt&versions=32",
  "source_sha256": "9f8f2097c25cd1b2756007ac83a5f1a172b3bde4aa3f977e22144a88c5ee6f0b",
  "retrieved_utc": "2026-11-01T06:27:25.782043+00:00",
  "source_locator": "lines 124-124",
  "excerpt": "DR   GO; GO:0004123; F:cystathionine gamma-lyase activity; IEA:TreeGrafter.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 32,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2H1K3G9?format=txt&versions=32)

```json
{
  "evidence_id": "H8",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A2H1K3G9?format=txt&versions=32",
  "source_sha256": "9f8f2097c25cd1b2756007ac83a5f1a172b3bde4aa3f977e22144a88c5ee6f0b",
  "retrieved_utc": "2026-11-01T06:27:25.782043+00:00",
  "source_locator": "lines 125-125",
  "excerpt": "DR   GO; GO:0047982; F:homocysteine desulfhydrase activity; IEA:UniProtKB-EC.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 32,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2H1K3G9?format=txt&versions=32)

```json
{
  "evidence_id": "H9",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A2H1K3G9?format=txt&versions=32",
  "source_sha256": "9f8f2097c25cd1b2756007ac83a5f1a172b3bde4aa3f977e22144a88c5ee6f0b",
  "retrieved_utc": "2026-11-01T06:27:25.782043+00:00",
  "source_locator": "lines 126-126",
  "excerpt": "DR   GO; GO:0018826; F:methionine gamma-lyase activity; IEA:UniProtKB-EC.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 32,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H10

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2H1K3G9?format=txt&versions=32)

```json
{
  "evidence_id": "H10",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A2H1K3G9?format=txt&versions=32",
  "source_sha256": "9f8f2097c25cd1b2756007ac83a5f1a172b3bde4aa3f977e22144a88c5ee6f0b",
  "retrieved_utc": "2026-11-01T06:27:25.782043+00:00",
  "source_locator": "lines 127-127",
  "excerpt": "DR   GO; GO:0030170; F:pyridoxal phosphate binding; IEA:InterPro.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 32,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
  "source": "Gene Ontology current ontology",
  "url": "https://current.geneontology.org/ontology/go-basic.obo",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source_locator": "lines 34028-34054",
  "excerpt": "[Term]\nid: GO:0004044\nname: amidophosphoribosyltransferase activity\nnamespace: molecular_function\ndef: \"Catalysis of the reaction: 5-phospho-beta-D-ribosylamine + L-glutamate + diphosphate = 5-phospho-alpha-D-ribose 1-diphosphate + L-glutamine + H2O.\" [EC:2.4.2.14, RHEA:14905]\nsynonym: \"5'-phosphoribosylpyrophosphate amidotransferase activity\" RELATED [EC:2.4.2.14]\nsynonym: \"5-phosphoribosyl-1-pyrophosphate amidotransferase activity\" RELATED [EC:2.4.2.14]\nsynonym: \"5-phosphoribosylamine:diphosphate phospho-alpha-D-ribosyltransferase (glutamate-amidating)\" RELATED [EC:2.4.2.14]\nsynonym: \"5-phosphororibosyl-1-pyrophosphate amidotransferase activity\" RELATED [EC:2.4.2.14]\nsynonym: \"alpha-5-phosphoribosyl-1-pyrophosphate amidotransferase activity\" RELATED [EC:2.4.2.14]\nsynonym: \"glutamine 5-phosphoribosylpyrophosphate amidotransferase activity\" RELATED [EC:2.4.2.14]\nsynonym: \"glutamine phosphoribosyldiphosphate amidotransferase activity\" RELATED [EC:2.4.2.14]\nsynonym: \"glutamine phosphoribosylpyrophosphate amidotransferase activity\" RELATED [EC:2.4.2.14]\nsynonym: \"glutamine ribosylpyrophosphate 5-phosphate amidotransferase activity\" RELATED [EC:2.4.2.14]\nsynonym: \"phosphoribose pyrophosphate amidotransferase activity\" RELATED [EC:2.4.2.14]\nsynonym: \"phosphoribosyl pyrophosphate amidotransferase activity\" RELATED [EC:2.4.2.14]\nsynonym: \"phosphoribosyldiphosphate 5-amidotransferase activity\" RELATED [EC:2.4.2.14]\nsynonym: \"phosphoribosylpyrophosphate glutamyl amidotransferase activity\" RELATED [EC:2.4.2.14]\nxref: EC:2.4.2.14\nxref: KEGG_REACTION:R01072\nxref: MetaCyc:PRPPAMIDOTRANS-RXN\nxref: Reactome:R-HSA-73815 \"5-phospho-alpha-D-ribose 1-diphosphate (PRPP) + H2O + L-glutamine <=> 5-phosphoribosylamine + L-glutamate +pyrophosphate\"\nxref: RHEA:14905\nis_a: GO:0016763 ! pentosyltransferase activity\nproperty_value: skos:exactMatch EC:2.4.2.14\nproperty_value: skos:exactMatch RHEA:14905\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "go_id": "GO:0004044"
}
```

### Evidence GO2

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO2",
  "source": "Gene Ontology current ontology",
  "url": "https://current.geneontology.org/ontology/go-basic.obo",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source_locator": "lines 35823-35842",
  "excerpt": "[Term]\nid: GO:0004123\nname: cystathionine gamma-lyase activity\nnamespace: molecular_function\nalt_id: GO:0016225\ndef: \"Catalysis of the reaction: L-cystathionine + H2O = 2-oxobutanoate + L-cysteine + NH4+.\" [RHEA:14005]\nsynonym: \"gamma-cystathionase activity\" BROAD [EC:4.4.1.1]\nsynonym: \"homoserine deaminase activity\" RELATED [EC:4.4.1.1]\nsynonym: \"homoserine deaminase-cystathionase activity\" RELATED [EC:4.4.1.1]\nsynonym: \"homoserine dehydratase activity\" RELATED [EC:4.4.1.1]\nsynonym: \"L-cystathionine cysteine-lyase (deaminating)\" BROAD [EC:4.4.1.1]\nsynonym: \"L-cystathionine cysteine-lyase (deaminating; 2-oxobutanoate-forming)\" RELATED [EC:4.4.1.1]\nxref: KEGG_REACTION:R01001\nxref: MetaCyc:RXN-15130\nxref: Reactome:R-HSA-1614583 \"PXLP-K212-CTH cleaves L-Cystathionine\"\nxref: RHEA:14005\nis_a: GO:0016846 ! carbon-sulfur lyase activity\nproperty_value: skos:broadMatch EC:4.4.1.1\nproperty_value: skos:exactMatch RHEA:14005\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "go_id": "GO:0004123"
}
```

### Evidence GO3

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO3",
  "source": "Gene Ontology current ontology",
  "url": "https://current.geneontology.org/ontology/go-basic.obo",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source_locator": "lines 358126-358254",
  "excerpt": "[Term]\nid: GO:0061630\nname: ubiquitin protein ligase activity\nnamespace: molecular_function\nalt_id: GO:0090302\nalt_id: GO:0090622\nalt_id: GO:1904264\nalt_id: GO:1904822\ndef: \"Catalysis of the transfer of ubiquitin to a substrate protein via the reaction X-ubiquitin + S = X + S-ubiquitin, where X is either an E2 or E3 enzyme, the X-ubiquitin linkage is a thioester bond, and the S-ubiquitin linkage is an amide bond: an isopeptide bond between the C-terminal glycine of ubiquitin and the epsilon-amino group of lysine residues in the substrate or, in the linear extension of ubiquitin chains, a peptide bond the between the C-terminal glycine and N-terminal methionine of ubiquitin residues.\" [GOC:BioGRID, GOC:dph, GOC:mah, GOC:tb, PMID:22863777]\ncomment: This enzyme catalyzes a transferase reaction.\nsynonym: \"E3\" BROAD [GOC:dph]\nsynonym: \"ER-associated E3 ligase\" RELATED [PMID:24019521]\nsynonym: \"protein ubiquitination activity\" EXACT [GOC:dph]\nsynonym: \"ubiquitin ligase activity\" EXACT [GOC:dph]\nxref: EC:2.3.2.26\nxref: EC:2.3.2.27\nxref: EC:2.3.2.31\nxref: EC:2.3.2.33\nxref: EC:2.3.2.36\nxref: Reactome:R-HSA-1225956 \"Inefficient ubiquitination of ligand-responsive p-6Y-EGFR mutants by p-Y371-CBL\"\nxref: Reactome:R-HSA-1504190 \"DVL is ubiquitinated by CUL3:KLHL12:RBX1\"\nxref: Reactome:R-HSA-183036 \"Ubiquitination of stimulated EGFR (CBL:GRB2)\"\nxref: Reactome:R-HSA-201445 \"Ubiquitin-dependent degradation controls basal levels of R-Smad1/5/8\"\nxref: Reactome:R-HSA-3322429 \"XIAP monoubiquinates TLE\"\nxref: Reactome:R-HSA-3640861 \"RNF146 ubiquitinates ADP-ribosylated AXIN\"\nxref: Reactome:R-HSA-4608852 \"SMURF1/2 ubiquitinates PRICKLE1\"\nxref: Reactome:R-HSA-4641129 \"AXIN is ubiquitinated by SMURF2\"\nxref: Reactome:R-HSA-4641159 \"DVL1 is ubiquitinated by HECW1\"\nxref: Reactome:R-HSA-4641246 \"ZNRF3 autoubiquitinates to promote its internalization\"\nxref: Reactome:R-HSA-4641253 \"ZNRF3 ubiquitinates FZD to promote its downregulation\"\nxref: Reactome:R-HSA-5246693 \"APC is K63-polyubiquitinated\"\nxref: Reactome:R-HSA-5610737 \"NUMB:ITCH bind and ubiquitnate GLI1\"\nxref: Reactome:R-HSA-5632648 \"SMURF1/2 ubiquitinates PTCH1\"\nxref: Reactome:R-HSA-5635856 \"SPOP:CUL3:RBX1 ubiquitinates GLI2,3\"\nxref: Reactome:R-HSA-5635864 \"NUMB:ITCH ubiquitinates GLI1\"\nxref: Reactome:R-HSA-5654672 \"CBL ubiquitinates FRS2 and FGFR1\"\nxref: Reactome:R-HSA-5654677 \"CBL ubiquitinates FRS2 and FGFR2\"\nxref: Reactome:R-HSA-5654679 \"CBL ubiquitinates FRS2 and FGFR3\"\nxref: Reactome:R-HSA-5654684 \"CBL ubiquitinates FRS2 and FGFR4\"\nxref: Reactome:R-HSA-5658424 \"KBTBD7:CUL3:RBX1 ubiquitinates NF1\"\nxref: Reactome:R-HSA-5674022 \"BRAP autoubiquitinates\"\nxref: Reactome:R-HSA-5682858 \"RNF8 and RNF168 ubiquitinate H2AFX\"\nxref: Reactome:R-HSA-5684071 \"RNF4 ubiquitinates MDC1\"\nxref: Reactome:R-HSA-5687081 \"MAPK6 is ubiquitinated at the N-terminal\"\nxref: Reactome:R-HSA-5689111 \"PARK2 autoubiquitinates\"\nxref: Reactome:R-HSA-5690827 \"TNFAIP3 (A20) ubiquitinates RIPK1\"\nxref: Reactome:R-HSA-6781867 \"ERCC8:DDB1:CUL4:RBX1 ubiquitinates ERCC6 and RNA Pol II\"\nxref: Reactome:R-HSA-6782943 \"UV-DDB ubiquitinates XPC\"\nxref: Reactome:R-HSA-6785361 \"Monoubiquitination of FANCD2:FANCI\"\nxref: Reactome:R-HSA-6790487 \"RNF111 ubiquitinates SUMOylated XPC\"\nxref: Reactome:R-HSA-6798373 \"MDM2 ubiquitinates DYRK2\"\nxref: Reactome:R-HSA-6804253 \"MDM2 ubiquitinates JMY\"\nxref: Reactome:R-HSA-6804441 \"RNF34 or RFFL ubiquitinates phosphorylated TP53\"\nxref: Reactome:R-HSA-6804724 \"MDM2 ubiquitinates phosphorylated MDM4\"\nxref: Reactome:R-HSA-6804879 \"MDM2 ubiquitinates TP53\"\nxref: Reactome:R-HSA-6804942 \"MDM2 homodimers auto-ubiquitinate\"\nxref: Reactome:R-HSA-6807106 \"PTEN undergoes monoubiquitination\"\nxref: Reactome:R-HSA-6807134 \"NEDD4, WWP2, CHIP and XIAP polyubiquitinate PTEN\"\nxref: Reactome:R-HSA-68946 \"Phosphorylated Orc1 is ubiquitinated while still associated with chromatin\"\nxref: Reactome:R-HSA-69015 \"Cytoplasmic phosphorylated Cdc6 is ubiquitinated by the anaphase-promoting complex\"\nxref: Reactome:R-HSA-8848829 \"CBL autoubiquitinates\"\nxref: Reactome:R-HSA-8851011 \"TRIM27 polyubiquitinates PTEN\"\nxref: Reactome:R-HSA-8854041 \"SCF-FBXL7 ubiquitinates AURKA\"\nxref: Reactome:R-HSA-8854051 \"SCF-FBXL18 ubiquitinates FBXL7\"\nxref: Reactome:R-HSA-8854628 \"MYLIP dimer ubiquitinates VLDLR on Lys-839\"\nxref: Reactome:R-HSA-8866546 \"RNF5 and RNF185 ubiquitinate misfolded CFTR\"\nxref: Reactome:R-HSA-8866856 \"RNF5 and RNF185 ubiquitinate CFTR F508del\"\nxref: Reactome:R-HSA-8867288 \"OS9:SEL1:ERAD E3 ligase:DERL2 ubiquitinates unfolded protein:(GlcNAc)2 (Man)9-5\"\nxref: Reactome:R-HSA-8875183 \"CBL monoubiquitinates activated MET\"\nxref: Reactome:R-HSA-8875431 \"LRIG1 undergoes ubiquitination\"\nxref: Reactome:R-HSA-8876258 \"CBL monoubiquitinates InlB-bound MET\"\nxref: Reactome:R-HSA-8877003 \"CBLL1 ubiqutinates the InlA-bound CDH1 complex\"\nxref: Reactome:R-HSA-8938773 \"RNF144A polyubiquitinates PRKDC\"\nxref: Reactome:R-HSA-8938815 \"RNF152 polyubiquitinates RRAGA\"\nxref: Reactome:R-HSA-8939335 \"RNF181 polyubiquinates BCL10\"\nxref: Reactome:R-HSA-8939706 \"SCF(SKP2) polyubiquitinates RUNX2\"\nxref: Reactome:R-HSA-8942101 \"RNF20:RNF40 monoubiquitinates Histone H2B\"\nxref: Reactome:R-HSA-8943003 \"SHPRH polyubiquitinates monoubiquitinated PCNA\"\nxref: Reactome:R-HSA-8943040 \"HLTF polyubiquitinates monoubiquitinated PCNA\"\nxref: Reactome:R-HSA-8943080 \"TMEM129 polyubiquitinates HLA (MHC class I heavy chain) bound to cytomegalovirus US11\"\nxref: Reactome:R-HSA-8948775 \"MKRN1 polyubiquitinates PTEN\"\nxref: Reactome:R-HSA-8948832 \"RNF146 polyubiquitinates PARylated PTEN\"\nxref: Reactome:R-HSA-8952382 \"MDM2 polyubiquitinates RUNX3\"\nxref: Reactome:R-HSA-8952419 \"SMURFs ubiquitinate RUNX3\"\nxref: Reactome:R-HSA-8953946 \"PEX2:PEX10:PEX12 monoubiquitinates PEX5S,L at cysteine-11\"\nxref: Reactome:R-HSA-8956026 \"CUL9:RBX1 ubiquitinates BIRC5\"\nxref: Reactome:R-HSA-8956684 \"ITCH polyubiquitinates TP73\"\nxref: Reactome:R-HSA-9008076 \"WWP1 polyubiquitinates RUNX2\"\nxref: Reactome:R-HSA-9009308 \"STUB1 polyubiquitinates RUNX2\"\nxref: Reactome:R-HSA-9009403 \"SMURF1 polyubiquitinates RUNX2\"\nxref: Reactome:R-HSA-9011300 \"ZSWIM8 ubiquitinates ROBO3.1\"\nxref: Reactome:R-HSA-9021523 \"WWP2 ubiquitinates NOTCH3\"\nxref: Reactome:R-HSA-9033485 \"PEX2:PEX10:PEX12 monoubiquitinates PEX5L at cysteine-11\"\nxref: Reactome:R-HSA-934604 \"Phosphorylated SPRY2 is ubiquitinated by CBL\"\nxref: Reactome:R-HSA-936462 \"PIN1 mediated IRF3 degradation\"\nxref: Reactome:R-HSA-936475 \"Negative regulation of DDX58/IFIH1 signaling by RNF216\"\nxref: Reactome:R-HSA-9604629 \"FBXW7 promotes ubiquitination of p-NICD4\"\nxref: Reactome:R-HSA-9685195 \"SARS-CoV-1 9b recruits ITCH to MAVS\"\nxref: Reactome:R-HSA-9686920 \"PELI1 ubiquitinates RIPK3 at K363\"\nxref: Reactome:R-HSA-9686969 \"APC/C:Cdh1 polyubiquitinates SKP2\"\nxref: Reactome:R-HSA-9705738 \"SOCS1,3 ubiquitinates CSF3R in SOCS1,3:p-4Y-CSF3R:CSF3 dimer:LYN:p-Y-JAK1:p-JAK2:p-SYK:p-HCK:p-TYK2:CUL5:ELOB:ELOC:RNF7\"\nxref: Reactome:R-HSA-9706354 \"Ubiquitination of FLT3\"\nxref: Reactome:R-HSA-9706356 \"CBL mutants don't ubiquitinate FLT3\"\nxref: Reactome:R-HSA-9708517 \"FBXL17 ubiquitinates BACH1 (in BACH1:FBXL17:SCF (SKP2))\"\nxref: Reactome:R-HSA-9733316 \"p-Y-CBL autoubiquitinates and multiubiquitinates p-Y561-CSF1R in CSF1 dimer:p-Y561-CSF1R dimer:p-Y-CBL\"\nxref: Reactome:R-HSA-9755304 \"MUL1 ubiquitinates UBXN7\"\nxref: Reactome:R-HSA-9755505 \"KEAP1:NEDD8-CUL3:RBX1 complex ubiquitinates NFE2L2\"\nxref: Reactome:R-HSA-9759154 \"TRIM21 ubiquitinates SQSTM1\"\nxref: Reactome:R-HSA-9759172 \"KEAP1:CUL3:RBX1 ubiquitinates p-S349 SQSTM1 oligomer\"\nxref: Reactome:R-HSA-9762091 \"NFE2L2 is ubiquitinated by BTRC:SKP1:CUL1:RBX1\"\nxref: Reactome:R-HSA-9766645 \"CUL3:RBX1 ubiquitinates KEAP1\"\nxref: Reactome:R-HSA-990526 \"Recruitment of ITCH and K48 ubiquitination of MAVS\"\nxref: Reactome:R-HSA-9929490 \"CD274 ubiquitination by SPOP:CUL3:RBX1 complex\"\nxref: Reactome:R-HSA-9931298 \"Ubiquitination of CD274 by ERAD complex\"\nxref: Reactome:R-HSA-9931430 \"MIB2-mediated K63-ubiquitination of CD274\"\nxref: Reactome:R-HSA-9932510 \"BTRC:CUL1:SKP1:RBX1 (SCF-beta-TrCP1) ubiquitinylates phosphorylated PER1,2,3\"\nxref: Reactome:R-HSA-9932512 \"FBXL3:CUL1:SKP1:RBX1 ubiquitinylates phosphorylated CRY1,2\"\nxref: Reactome:R-HSA-9945766 \"NS3 is ubiquitinated\"\nxref: Reactome:R-HSA-9946390 \"NS1 dimer is ubiquitinated\"\nxref: Reactome:R-HSA-9948362 \"LTN1 K48 polyubiquitinates the nascent peptide in NEMF:60S ribosomal subunit:peptidyl-tRNA with nascent peptide\"\nxref: Reactome:R-HSA-9954737 \"RCHY1 K48 polyubiquitinates alanine-tailed nascent peptide\"\nis_a: GO:0004842 ! ubiquitin-protein transferase activity\nis_a: GO:0061659 ! ubiquitin-like protein ligase activity\nproperty_value: skos:narrowMatch EC:2.3.2.26\nproperty_value: skos:narrowMatch EC:2.3.2.27\nproperty_value: skos:narrowMatch EC:2.3.2.31\nproperty_value: skos:narrowMatch EC:2.3.2.33\nproperty_value: skos:narrowMatch EC:2.3.2.36\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "go_id": "GO:0061630"
}
```

### Evidence GO4

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO4",
  "source": "Gene Ontology current ontology",
  "url": "https://current.geneontology.org/ontology/go-basic.obo",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source_locator": "lines 516127-516137",
  "excerpt": "[Term]\nid: GO:1904047\nname: S-adenosyl-L-methionine binding\nnamespace: molecular_function\nalt_id: GO:0070283\ndef: \"Binding to S-adenosyl-L-methionine.\" [GO_REF:0000067, GOC:BHF, GOC:hal, GOC:TermGenie, PMID:22985361]\nsynonym: \"radical SAM enzyme activity\" NARROW []\nxref: Reactome:R-HSA-947535 \"Cyclisation of GTP to precursor Z\"\nis_a: GO:0043169 ! cation binding\nis_a: GO:1901681 ! sulfur compound binding\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "go_id": "GO:1904047"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 154. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
