# active_site_0073: before and after transfer clarification

[All 1,328 cases](../README.md) · [Method](../METHOD.md) · [Summary](../SUMMARY.md) · [Exact reviewer user message](../inputs/active_site_0073.txt)

**Task:** `active_site`  
**Author key, unchanged:** **C** — Position 93 (Proton donor)

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
MAGSEPVRAEGETMAVDAAPRKPRILLAASGSVAAVKFANLCHCFSEWADVRAVSTSASLHFIDRAAMPKDVILYTDDNEWSSWKKLGDSVLHIELRKWADIMVIAPLSANTLGKIAGGLCDNLLTCIVRAWDYSKPFFVAPAMNTFMWNNPFTERHLISIDELGISLIPPVTKRLACGDYGNGAMAEPSTIYSTVRLFYESKAQQGNGDI

[Multiple Choices]
A. Position 959 (Proton acceptor; for dehydratase activity)
B. Position 170 (Proton donor)
C. Position 93 (Proton donor)
D. Position 4848 (Proton donor; for dehydratase activity 2)
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

> The sequence matches the UniProt entry for soybean HAL3a/PPCDC, which annotates residue 93 as a proton donor. This annotation is transferred by similarity from UniProtKB:Q9SWE5, rather than shown here to be direct experimental evidence for this soybean protein.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence may permit protein-family inference, but no supplied context or general biochemical principle identifies residue 93 as the proton donor rather than another candidate position.


**Missing item-specific fact**

> The protein-specific active-site annotation assigning proton-donor function to residue 93.


**Reason**

> Choosing C depends on an exact residue-function annotation for this protein or a sufficiently close homolog; that fact is not provided by the sequence and choices alone.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the listed options, the supplied reviewer evidence supports C; it does not support the other listed positions. The annotations also identify residue 178 as a proton donor, but that position is not an option.


### Important caveats

- The UniProt annotation is evidence by similarity (ECO:0000250), not independently verified direct experimental evidence in the supplied material.
- The question describes active-site residues in the plural but offers individual-position choices.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence may permit protein-family inference, but no supplied context or general biochemical principle identifies residue 93 as the proton donor rather than another candidate position.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific active-site annotation assigning proton-donor function to residue 93.",
    "reason": "Choosing C depends on an exact residue-function annotation for this protein or a sufficiently close homolog; that fact is not provided by the sequence and choices alone."
  },
  "case_id": "active_site_0073",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H2"
    ],
    "judgment": "supported",
    "reason": "The sequence matches the UniProt entry for soybean HAL3a/PPCDC, which annotates residue 93 as a proton donor. This annotation is transferred by similarity from UniProtKB:Q9SWE5, rather than shown here to be direct experimental evidence for this soybean protein."
  },
  "important_caveats": [
    "The UniProt annotation is evidence by similarity (ECO:0000250), not independently verified direct experimental evidence in the supplied material.",
    "The question describes active-site residues in the plural but offers individual-position choices."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed options, the supplied reviewer evidence supports C; it does not support the other listed positions. The annotations also identify residue 178 as a proton donor, but that position is not an option."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "active_site_0073",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches the UniProt entry for soybean HAL3a/PPCDC, which annotates residue 93 as a proton donor. This annotation is transferred by similarity from UniProtKB:Q9SWE5, rather than shown here to be direct experimental evidence for this soybean protein.",
    "evidence_ids": ["C1", "C4", "C5", "H2"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence may permit protein-family inference, but no supplied context or general biochemical principle identifies residue 93 as the proton donor rather than another candidate position.",
    "missing_item_specific_fact": "The protein-specific active-site annotation assigning proton-donor function to residue 93.",
    "reason": "Choosing C depends on an exact residue-function annotation for this protein or a sufficiently close homolog; that fact is not provided by the sequence and choices alone."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed options, the supplied reviewer evidence supports C; it does not support the other listed positions. The annotations also identify residue 178 as a proton donor, but that position is not an option."
  },
  "important_caveats": [
    "The UniProt annotation is evidence by similarity (ECO:0000250), not independently verified direct experimental evidence in the supplied material.",
    "The question describes active-site residues in the plural but offers individual-position choices."
  ]
}
```

</details>

## Before: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry C6SZ50 (HAL3A_SOYBN, Phosphopantothenoylcysteine decarboxylase HAL3a, EC 4.1.1.36) annotates position 93 as an Active site with description 'Proton donor' (evidence code ECO:0000250, inferred by similarity from Q9SWE5). The sequence at position 93 is indeed Histidine (H), consistent with a proton-donor role. The annotation is computational (similarity transfer), not direct experimental evidence for this specific protein, but it is the authoritative database annotation supporting the expected answer.

Citations as saved: [C5](#evidence-c5), [H2](#evidence-h2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The provided sequence is only 211 amino acids long, so options A (position 959) and D (position 4848) are trivially eliminated as positions exceeding the protein length. Between the remaining options, position 93 is Histidine (H), a canonical catalytic residue capable of acting as a proton donor/acceptor, while position 170 is Proline (P), a structurally constrained residue that is not involved in proton transfer catalysis. Additionally, the enzyme is a decarboxylase (EC 4.1.1.36), making descriptions referencing 'dehydratase activity' (options A and D) functionally inconsistent. General knowledge of amino acid catalytic roles suffices to select C.


**Missing item-specific fact**

> None critical. The reasoning relies on counting sequence length (trivial) and recognizing His vs Pro catalytic potential (general biochemistry).


**Reason**

> A model can eliminate A and D by noting positions 959 and 4848 exceed the 211-residue sequence, then distinguish B from C by recognizing that Histidine is a well-known proton-transfer catalytic residue whereas Proline is not. This is general biological reasoning, not a lookup of a specific database entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options A and D are invalid by sequence length. Option B places a catalytic role on Proline, which is biochemically implausible. Only option C (His93, proton donor) is consistent with both the sequence and general catalytic chemistry. No genuine ambiguity remains.


### Important caveats

- The UniProt annotation for position 93 carries evidence code ECO:0000250 (inferred by similarity from Q9SWE5), meaning it is a computational transfer, not a direct experimental determination for this soybean protein.
- The enzyme also has a second annotated active site at position 178 (also 'Proton donor'), but this position is not offered as a choice, so it does not create ambiguity.
- Options A and D reference 'dehydratase activity' while the enzyme is classified as a decarboxylase (EC 4.1.1.36), adding another layer of inconsistency beyond the out-of-range positions.
- The reviewer-only evidence confirms the sequence match (SHA-256 identical) between the benchmark input and UniProt C6SZ50 at both current and historical (entry version 84) snapshots.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The provided sequence is only 211 amino acids long, so options A (position 959) and D (position 4848) are trivially eliminated as positions exceeding the protein length. Between the remaining options, position 93 is Histidine (H), a canonical catalytic residue capable of acting as a proton donor/acceptor, while position 170 is Proline (P), a structurally constrained residue that is not involved in proton transfer catalysis. Additionally, the enzyme is a decarboxylase (EC 4.1.1.36), making descriptions referencing 'dehydratase activity' (options A and D) functionally inconsistent. General knowledge of amino acid catalytic roles suffices to select C.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None critical. The reasoning relies on counting sequence length (trivial) and recognizing His vs Pro catalytic potential (general biochemistry).",
    "reason": "A model can eliminate A and D by noting positions 959 and 4848 exceed the 211-residue sequence, then distinguish B from C by recognizing that Histidine is a well-known proton-transfer catalytic residue whereas Proline is not. This is general biological reasoning, not a lookup of a specific database entry."
  },
  "case_id": "active_site_0073",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H2"
    ],
    "judgment": "supported",
    "reason": "UniProt entry C6SZ50 (HAL3A_SOYBN, Phosphopantothenoylcysteine decarboxylase HAL3a, EC 4.1.1.36) annotates position 93 as an Active site with description 'Proton donor' (evidence code ECO:0000250, inferred by similarity from Q9SWE5). The sequence at position 93 is indeed Histidine (H), consistent with a proton-donor role. The annotation is computational (similarity transfer), not direct experimental evidence for this specific protein, but it is the authoritative database annotation supporting the expected answer."
  },
  "important_caveats": [
    "The UniProt annotation for position 93 carries evidence code ECO:0000250 (inferred by similarity from Q9SWE5), meaning it is a computational transfer, not a direct experimental determination for this soybean protein.",
    "The enzyme also has a second annotated active site at position 178 (also 'Proton donor'), but this position is not offered as a choice, so it does not create ambiguity.",
    "Options A and D reference 'dehydratase activity' while the enzyme is classified as a decarboxylase (EC 4.1.1.36), adding another layer of inconsistency beyond the out-of-range positions.",
    "The reviewer-only evidence confirms the sequence match (SHA-256 identical) between the benchmark input and UniProt C6SZ50 at both current and historical (entry version 84) snapshots."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A and D are invalid by sequence length. Option B places a catalytic role on Proline, which is biochemically implausible. Only option C (His93, proton donor) is consistent with both the sequence and general catalytic chemistry. No genuine ambiguity remains."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "active_site_0073",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry C6SZ50 (HAL3A_SOYBN, Phosphopantothenoylcysteine decarboxylase HAL3a, EC 4.1.1.36) annotates position 93 as an Active site with description 'Proton donor' (evidence code ECO:0000250, inferred by similarity from Q9SWE5). The sequence at position 93 is indeed Histidine (H), consistent with a proton-donor role. The annotation is computational (similarity transfer), not direct experimental evidence for this specific protein, but it is the authoritative database annotation supporting the expected answer.",
    "evidence_ids": ["C5", "H2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The provided sequence is only 211 amino acids long, so options A (position 959) and D (position 4848) are trivially eliminated as positions exceeding the protein length. Between the remaining options, position 93 is Histidine (H), a canonical catalytic residue capable of acting as a proton donor/acceptor, while position 170 is Proline (P), a structurally constrained residue that is not involved in proton transfer catalysis. Additionally, the enzyme is a decarboxylase (EC 4.1.1.36), making descriptions referencing 'dehydratase activity' (options A and D) functionally inconsistent. General knowledge of amino acid catalytic roles suffices to select C.",
    "missing_item_specific_fact": "None critical. The reasoning relies on counting sequence length (trivial) and recognizing His vs Pro catalytic potential (general biochemistry).",
    "reason": "A model can eliminate A and D by noting positions 959 and 4848 exceed the 211-residue sequence, then distinguish B from C by recognizing that Histidine is a well-known proton-transfer catalytic residue whereas Proline is not. This is general biological reasoning, not a lookup of a specific database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A and D are invalid by sequence length. Option B places a catalytic role on Proline, which is biochemically implausible. Only option C (His93, proton donor) is consistent with both the sequence and general catalytic chemistry. No genuine ambiguity remains."
  },
  "important_caveats": [
    "The UniProt annotation for position 93 carries evidence code ECO:0000250 (inferred by similarity from Q9SWE5), meaning it is a computational transfer, not a direct experimental determination for this soybean protein.",
    "The enzyme also has a second annotated active site at position 178 (also 'Proton donor'), but this position is not offered as a choice, so it does not create ambiguity.",
    "Options A and D reference 'dehydratase activity' while the enzyme is classified as a decarboxylase (EC 4.1.1.36), adding another layer of inconsistency beyond the out-of-range positions.",
    "The reviewer-only evidence confirms the sequence match (SHA-256 identical) between the benchmark input and UniProt C6SZ50 at both current and historical (entry version 84) snapshots."
  ]
}
```

</details>

## After: GPT-6 Luna

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence-matched UniProt record annotates position 93 as a proton donor. That annotation is transferred by similarity from Q9SWE5 (ECO:0000250), so it supports the key but is not direct experimental evidence for this exact protein.

Citations as saved: [C5](#evidence-c5), [H2](#evidence-h2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is consistent with the phosphopantothenoylcysteine decarboxylase family, for which conserved catalytic residues can be inferred by homology. Among the plausible-length choices, residue 93 is His, a credible proton donor and a conserved catalytic feature in this family; residue 170 is Pro, which lacks a side-chain proton-donating group and has no backbone amide proton. Choices at 959 and 4848 are outside the 211-residue sequence.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Family-level catalytic knowledge, together with the residues actually present at the offered positions, meaningfully favors C without needing the target's database record. This is a credible inference, though not an independent experimental demonstration.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Only C among the offered options identifies a plausible proton-donating residue at a valid position. The record also annotates another proton donor at position 178, but that position is not an offered option.


### Important caveats

- The supporting annotation is similarity-based rather than direct experimental evidence for this sequence.
- The options ask for a single residue even though the source record annotates more than one proton donor.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with the phosphopantothenoylcysteine decarboxylase family, for which conserved catalytic residues can be inferred by homology. Among the plausible-length choices, residue 93 is His, a credible proton donor and a conserved catalytic feature in this family; residue 170 is Pro, which lacks a side-chain proton-donating group and has no backbone amide proton. Choices at 959 and 4848 are outside the 211-residue sequence.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Family-level catalytic knowledge, together with the residues actually present at the offered positions, meaningfully favors C without needing the target's database record. This is a credible inference, though not an independent experimental demonstration."
  },
  "case_id": "active_site_0073",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H2"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates position 93 as a proton donor. That annotation is transferred by similarity from Q9SWE5 (ECO:0000250), so it supports the key but is not direct experimental evidence for this exact protein."
  },
  "important_caveats": [
    "The supporting annotation is similarity-based rather than direct experimental evidence for this sequence.",
    "The options ask for a single residue even though the source record annotates more than one proton donor."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only C among the offered options identifies a plausible proton-donating residue at a valid position. The record also annotates another proton donor at position 178, but that position is not an offered option."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "active_site_0073",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates position 93 as a proton donor. That annotation is transferred by similarity from Q9SWE5 (ECO:0000250), so it supports the key but is not direct experimental evidence for this exact protein.",
    "evidence_ids": ["C5", "H2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is consistent with the phosphopantothenoylcysteine decarboxylase family, for which conserved catalytic residues can be inferred by homology. Among the plausible-length choices, residue 93 is His, a credible proton donor and a conserved catalytic feature in this family; residue 170 is Pro, which lacks a side-chain proton-donating group and has no backbone amide proton. Choices at 959 and 4848 are outside the 211-residue sequence.",
    "missing_item_specific_fact": "",
    "reason": "Family-level catalytic knowledge, together with the residues actually present at the offered positions, meaningfully favors C without needing the target's database record. This is a credible inference, though not an independent experimental demonstration."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only C among the offered options identifies a plausible proton-donating residue at a valid position. The record also annotates another proton donor at position 178, but that position is not an offered option."
  },
  "important_caveats": [
    "The supporting annotation is similarity-based rather than direct experimental evidence for this sequence.",
    "The options ask for a single residue even though the source record annotates more than one proton donor."
  ]
}
```

</details>

## After: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry C6SZ50 annotates position 93 as an Active Site with description 'Proton donor' (evidence code ECO:0000250, transferred from Q9SWE5). Position 93 in the 211-residue sequence corresponds to Histidine (H), consistent with a proton donor role in an FMN-dependent decarboxylase. The annotation is a similarity-transfer annotation rather than direct experimental evidence, but it is a valid database annotation supporting the expected answer.

Citations as saved: [C5](#evidence-c5), [H2](#evidence-h2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The protein sequence is 211 amino acids long. Options A (position 959) and D (position 4848) refer to positions that do not exist in this sequence and can be eliminated immediately by counting residues. This leaves B (position 170) and C (position 93). Position 170 is Proline (P), which lacks any ionizable side chain and is structurally rigid—proline is essentially never a catalytic proton donor. Position 93 is Histidine (H), whose imidazole side chain (pKa ~6-7) is the canonical proton donor/acceptor in enzyme catalysis. Furthermore, the sequence contains FMN-binding Rossmann-fold motifs (e.g., GxGxxG patterns around residues 31-33, 56-58), identifying this as an FMN-dependent decarboxylase. In the PPCDC (phosphopantothenoylcysteine decarboxylase) family, a conserved histidine serves as the proton donor in the decarboxylation mechanism. Thus, family-level knowledge of FMN-dependent decarboxylases combined with basic amino-acid chemistry (His vs. Pro as catalytic residues) meaningfully distinguishes C from B without needing the specific UniProt annotation for this exact protein.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The question is answerable through: (1) sequence-length elimination of A and D, (2) chemical reasoning that proline cannot be a proton donor while histidine commonly is, and (3) family-level knowledge of FMN-dependent decarboxylase mechanisms where a conserved His acts as proton donor. No fact specific to this exact protein beyond what is inferable from the sequence and general biochemistry is required.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options A and D are eliminated by sequence length (211 residues). Option B (position 170 = Proline) is chemically implausible as a proton donor. Option C (position 93 = Histidine) is the only chemically sensible proton donor among the viable choices. No ambiguity remains.


### Important caveats

- The UniProt annotation for position 93 is based on similarity transfer (ECO:0000250 from Q9SWE5), not direct experimental mutagenesis or structural determination for this specific soybean protein.
- The UniProt entry also annotates position 178 (Cysteine) as a second proton donor active site, but this position is not offered as a choice, so it does not create ambiguity among the provided options.
- The question format lists only a single residue per option, whereas active sites typically involve multiple residues; however, the task asks for the key catalytic residue and the options are structured accordingly.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The protein sequence is 211 amino acids long. Options A (position 959) and D (position 4848) refer to positions that do not exist in this sequence and can be eliminated immediately by counting residues. This leaves B (position 170) and C (position 93). Position 170 is Proline (P), which lacks any ionizable side chain and is structurally rigid—proline is essentially never a catalytic proton donor. Position 93 is Histidine (H), whose imidazole side chain (pKa ~6-7) is the canonical proton donor/acceptor in enzyme catalysis. Furthermore, the sequence contains FMN-binding Rossmann-fold motifs (e.g., GxGxxG patterns around residues 31-33, 56-58), identifying this as an FMN-dependent decarboxylase. In the PPCDC (phosphopantothenoylcysteine decarboxylase) family, a conserved histidine serves as the proton donor in the decarboxylation mechanism. Thus, family-level knowledge of FMN-dependent decarboxylases combined with basic amino-acid chemistry (His vs. Pro as catalytic residues) meaningfully distinguishes C from B without needing the specific UniProt annotation for this exact protein.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The question is answerable through: (1) sequence-length elimination of A and D, (2) chemical reasoning that proline cannot be a proton donor while histidine commonly is, and (3) family-level knowledge of FMN-dependent decarboxylase mechanisms where a conserved His acts as proton donor. No fact specific to this exact protein beyond what is inferable from the sequence and general biochemistry is required."
  },
  "case_id": "active_site_0073",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H2"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry C6SZ50 annotates position 93 as an Active Site with description 'Proton donor' (evidence code ECO:0000250, transferred from Q9SWE5). Position 93 in the 211-residue sequence corresponds to Histidine (H), consistent with a proton donor role in an FMN-dependent decarboxylase. The annotation is a similarity-transfer annotation rather than direct experimental evidence, but it is a valid database annotation supporting the expected answer."
  },
  "important_caveats": [
    "The UniProt annotation for position 93 is based on similarity transfer (ECO:0000250 from Q9SWE5), not direct experimental mutagenesis or structural determination for this specific soybean protein.",
    "The UniProt entry also annotates position 178 (Cysteine) as a second proton donor active site, but this position is not offered as a choice, so it does not create ambiguity among the provided options.",
    "The question format lists only a single residue per option, whereas active sites typically involve multiple residues; however, the task asks for the key catalytic residue and the options are structured accordingly."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A and D are eliminated by sequence length (211 residues). Option B (position 170 = Proline) is chemically implausible as a proton donor. Option C (position 93 = Histidine) is the only chemically sensible proton donor among the viable choices. No ambiguity remains."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "active_site_0073",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry C6SZ50 annotates position 93 as an Active Site with description 'Proton donor' (evidence code ECO:0000250, transferred from Q9SWE5). Position 93 in the 211-residue sequence corresponds to Histidine (H), consistent with a proton donor role in an FMN-dependent decarboxylase. The annotation is a similarity-transfer annotation rather than direct experimental evidence, but it is a valid database annotation supporting the expected answer.",
    "evidence_ids": ["C5", "H2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The protein sequence is 211 amino acids long. Options A (position 959) and D (position 4848) refer to positions that do not exist in this sequence and can be eliminated immediately by counting residues. This leaves B (position 170) and C (position 93). Position 170 is Proline (P), which lacks any ionizable side chain and is structurally rigid—proline is essentially never a catalytic proton donor. Position 93 is Histidine (H), whose imidazole side chain (pKa ~6-7) is the canonical proton donor/acceptor in enzyme catalysis. Furthermore, the sequence contains FMN-binding Rossmann-fold motifs (e.g., GxGxxG patterns around residues 31-33, 56-58), identifying this as an FMN-dependent decarboxylase. In the PPCDC (phosphopantothenoylcysteine decarboxylase) family, a conserved histidine serves as the proton donor in the decarboxylation mechanism. Thus, family-level knowledge of FMN-dependent decarboxylases combined with basic amino-acid chemistry (His vs. Pro as catalytic residues) meaningfully distinguishes C from B without needing the specific UniProt annotation for this exact protein.",
    "missing_item_specific_fact": "",
    "reason": "The question is answerable through: (1) sequence-length elimination of A and D, (2) chemical reasoning that proline cannot be a proton donor while histidine commonly is, and (3) family-level knowledge of FMN-dependent decarboxylase mechanisms where a conserved His acts as proton donor. No fact specific to this exact protein beyond what is inferable from the sequence and general biochemistry is required."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A and D are eliminated by sequence length (211 residues). Option B (position 170 = Proline) is chemically implausible as a proton donor. Option C (position 93 = Histidine) is the only chemically sensible proton donor among the viable choices. No ambiguity remains."
  },
  "important_caveats": [
    "The UniProt annotation for position 93 is based on similarity transfer (ECO:0000250 from Q9SWE5), not direct experimental mutagenesis or structural determination for this specific soybean protein.",
    "The UniProt entry also annotates position 178 (Cysteine) as a second proton donor active site, but this position is not offered as a choice, so it does not create ambiguity among the provided options.",
    "The question format lists only a single residue per option, whereas active sites typically involve multiple residues; however, the task asks for the key catalytic residue and the options are structured accordingly."
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
  "requested_accession": "C6SZ50",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "benchmark_sequence_sha256": "42d591b72a59644dce840573d469e04fad803877d6364e70afe70b2cffcfd7ad",
  "benchmark_sequence_length": 211,
  "current_status": "retrieved",
  "current_sequence_comparison": "matched",
  "current_entry_audit": {
    "entryVersion": 86,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2009-09-22",
    "sequenceVersion": 1
  },
  "current_uniprot_release": "2026_03",
  "current_record_sha256": "d2226dda9179b81f36d4679262e16bb210a289390044f58410d1a107b4408396",
  "current_source_sequence_sha256": "42d591b72a59644dce840573d469e04fad803877d6364e70afe70b2cffcfd7ad",
  "current_source_sequence_length": 211,
  "historical_status": "retrieved",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "selected_historical_entry_version": 84,
  "selected_historical_version": {
    "accession": "C6SZ50",
    "database": "Swiss-Prot",
    "entryVersion": 84,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "HAL3A_SOYBN",
    "sequenceVersion": 1
  },
  "selected_historical_record_sha256": "1ce346fa691149ee6e809ca984b0d5dbda18272b4eb904ae9e28b38ca8688212",
  "selected_historical_source_sequence_sha256": "42d591b72a59644dce840573d469e04fad803877d6364e70afe70b2cffcfd7ad",
  "selected_historical_source_sequence_length": 211,
  "latest_at_cutoff_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 84,
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C6SZ50.json)

```json
{
  "evidence_id": "C1",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/C6SZ50.json",
  "source_sha256": "d2226dda9179b81f36d4679262e16bb210a289390044f58410d1a107b4408396",
  "retrieved_utc": "2026-11-02T04:27:34.573952+00:00",
  "json_pointer": "/primaryAccession",
  "excerpt": "\"C6SZ50\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C6SZ50.json)

```json
{
  "evidence_id": "C2",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/C6SZ50.json",
  "source_sha256": "d2226dda9179b81f36d4679262e16bb210a289390044f58410d1a107b4408396",
  "retrieved_utc": "2026-11-02T04:27:34.573952+00:00",
  "json_pointer": "/entryAudit",
  "excerpt": "{\"entryVersion\":86,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2009-09-22\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C6SZ50.json)

```json
{
  "evidence_id": "C3",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/C6SZ50.json",
  "source_sha256": "d2226dda9179b81f36d4679262e16bb210a289390044f58410d1a107b4408396",
  "retrieved_utc": "2026-11-02T04:27:34.573952+00:00",
  "json_pointer": "/organism",
  "excerpt": "{\"commonName\":\"Soybean\",\"lineage\":[\"Eukaryota\",\"Viridiplantae\",\"Streptophyta\",\"Embryophyta\",\"Tracheophyta\",\"Spermatophyta\",\"Magnoliopsida\",\"eudicotyledons\",\"Gunneridae\",\"Pentapetalae\",\"rosids\",\"fabids\",\"Fabales\",\"Fabaceae\",\"Papilionoideae\",\"50 kb inversion clade\",\"NPAAA clade\",\"indigoferoid/millettioid clade\",\"Phaseoleae\",\"Glycine\",\"Glycine subgen. Soja\"],\"scientificName\":\"Glycine max\",\"synonyms\":[\"Glycine hispida\"],\"taxonId\":3847}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C6SZ50.json)

```json
{
  "evidence_id": "C4",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/C6SZ50.json",
  "source_sha256": "d2226dda9179b81f36d4679262e16bb210a289390044f58410d1a107b4408396",
  "retrieved_utc": "2026-11-02T04:27:34.573952+00:00",
  "json_pointer": "/proteinDescription",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"Ref.3\",\"source\":\"Reference\"},{\"evidenceCode\":\"ECO:0000303\",\"id\":\"Ref.4\",\"source\":\"Reference\"}],\"value\":\"Halotolerance protein 3a\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"Ref.3\",\"source\":\"Reference\"},{\"evidenceCode\":\"ECO:0000303\",\"id\":\"Ref.4\",\"source\":\"Reference\"}],\"value\":\"GmHAL3a\"}]}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9SWE5\",\"source\":\"UniProtKB\"}],\"value\":\"4.1.1.36\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Phosphopantothenoylcysteine decarboxylase HAL3a\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"PPCDC\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C6SZ50.json)

```json
{
  "evidence_id": "C5",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/C6SZ50.json",
  "source_sha256": "d2226dda9179b81f36d4679262e16bb210a289390044f58410d1a107b4408396",
  "retrieved_utc": "2026-11-02T04:27:34.573952+00:00",
  "json_pointer": "/features/1",
  "excerpt": "{\"description\":\"Proton donor\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9SWE5\",\"source\":\"UniProtKB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":93},\"start\":{\"modifier\":\"EXACT\",\"value\":93}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C6SZ50.json)

```json
{
  "evidence_id": "C6",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/C6SZ50.json",
  "source_sha256": "d2226dda9179b81f36d4679262e16bb210a289390044f58410d1a107b4408396",
  "retrieved_utc": "2026-11-02T04:27:34.573952+00:00",
  "json_pointer": "/features/2",
  "excerpt": "{\"description\":\"Proton donor\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9SWE5\",\"source\":\"UniProtKB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":178},\"start\":{\"modifier\":\"EXACT\",\"value\":178}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C6SZ50.json)

```json
{
  "evidence_id": "C7",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/C6SZ50.json",
  "source_sha256": "d2226dda9179b81f36d4679262e16bb210a289390044f58410d1a107b4408396",
  "retrieved_utc": "2026-11-02T04:27:34.573952+00:00",
  "json_pointer": "/features/3",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9SWE5\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:58210\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:58210\",\"name\":\"FMN\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":33},\"start\":{\"modifier\":\"EXACT\",\"value\":31}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C6SZ50.json)

```json
{
  "evidence_id": "C8",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/C6SZ50.json",
  "source_sha256": "d2226dda9179b81f36d4679262e16bb210a289390044f58410d1a107b4408396",
  "retrieved_utc": "2026-11-02T04:27:34.573952+00:00",
  "json_pointer": "/features/4",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9SWE5\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:58210\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:58210\",\"name\":\"FMN\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":58},\"start\":{\"modifier\":\"EXACT\",\"value\":56}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C6SZ50.json)

```json
{
  "evidence_id": "C9",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/C6SZ50.json",
  "source_sha256": "d2226dda9179b81f36d4679262e16bb210a289390044f58410d1a107b4408396",
  "retrieved_utc": "2026-11-02T04:27:34.573952+00:00",
  "json_pointer": "/features/5",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9SWE5\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:58210\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:58210\",\"name\":\"FMN\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":112},\"start\":{\"modifier\":\"EXACT\",\"value\":109}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C6SZ50.json)

```json
{
  "evidence_id": "C10",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/C6SZ50.json",
  "source_sha256": "d2226dda9179b81f36d4679262e16bb210a289390044f58410d1a107b4408396",
  "retrieved_utc": "2026-11-02T04:27:34.573952+00:00",
  "json_pointer": "/features/6",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9SWE5\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:58210\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:58210\",\"name\":\"FMN\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":143},\"start\":{\"modifier\":\"EXACT\",\"value\":143}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C6SZ50.json)

```json
{
  "evidence_id": "C11",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/C6SZ50.json",
  "source_sha256": "d2226dda9179b81f36d4679262e16bb210a289390044f58410d1a107b4408396",
  "retrieved_utc": "2026-11-02T04:27:34.573952+00:00",
  "json_pointer": "/features/7",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9SWE5\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:59458\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:59458\",\"name\":\"N-[(R)-4-phosphopantothenoyl]-L-cysteine\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":145},\"start\":{\"modifier\":\"EXACT\",\"value\":145}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C6SZ50.json)

```json
{
  "evidence_id": "C12",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/C6SZ50.json",
  "source_sha256": "d2226dda9179b81f36d4679262e16bb210a289390044f58410d1a107b4408396",
  "retrieved_utc": "2026-11-02T04:27:34.573952+00:00",
  "json_pointer": "/features/8",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9SWE5\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:59458\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:59458\",\"name\":\"N-[(R)-4-phosphopantothenoyl]-L-cysteine\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":175},\"start\":{\"modifier\":\"EXACT\",\"value\":175}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C13

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C6SZ50.json)

```json
{
  "evidence_id": "C13",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/C6SZ50.json",
  "source_sha256": "d2226dda9179b81f36d4679262e16bb210a289390044f58410d1a107b4408396",
  "retrieved_utc": "2026-11-02T04:27:34.573952+00:00",
  "json_pointer": "/features/9",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9SWE5\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:59458\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:59458\",\"name\":\"N-[(R)-4-phosphopantothenoyl]-L-cysteine\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":177},\"start\":{\"modifier\":\"EXACT\",\"value\":177}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C14

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C6SZ50.json)

```json
{
  "evidence_id": "C14",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/C6SZ50.json",
  "source_sha256": "d2226dda9179b81f36d4679262e16bb210a289390044f58410d1a107b4408396",
  "retrieved_utc": "2026-11-02T04:27:34.573952+00:00",
  "json_pointer": "/features/10",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9SWE5\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:59458\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:59458\",\"name\":\"N-[(R)-4-phosphopantothenoyl]-L-cysteine\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":186},\"start\":{\"modifier\":\"EXACT\",\"value\":186}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C15

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C6SZ50.json)

```json
{
  "evidence_id": "C15",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/C6SZ50.json",
  "source_sha256": "d2226dda9179b81f36d4679262e16bb210a289390044f58410d1a107b4408396",
  "retrieved_utc": "2026-11-02T04:27:34.573952+00:00",
  "json_pointer": "/features/11",
  "excerpt": "{\"description\":\"Important for catalytic activity\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9SWE5\",\"source\":\"UniProtKB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":178},\"start\":{\"modifier\":\"EXACT\",\"value\":178}},\"type\":\"Site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/C6SZ50?format=txt&versions=84)

```json
{
  "evidence_id": "H1",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/C6SZ50?format=txt&versions=84",
  "source_sha256": "1ce346fa691149ee6e809ca984b0d5dbda18272b4eb904ae9e28b38ca8688212",
  "retrieved_utc": "2026-11-02T04:27:36.741333+00:00",
  "source_locator": "lines 1-19",
  "excerpt": "ID   HAL3A_SOYBN             Reviewed;         211 AA.\nAC   C6SZ50;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   22-SEP-2009, sequence version 1.\nDT   28-JAN-2026, entry version 84.\nDE   RecName: Full=Phosphopantothenoylcysteine decarboxylase HAL3a {ECO:0000305};\nDE            Short=PPCDC {ECO:0000305};\nDE            EC=4.1.1.36 {ECO:0000250|UniProtKB:Q9SWE5};\nDE   AltName: Full=Halotolerance protein 3a {ECO:0000303|Ref.3, ECO:0000303|Ref.4};\nDE            Short=GmHAL3a {ECO:0000303|Ref.3, ECO:0000303|Ref.4};\nGN   Name=HAL3A {ECO:0000303|Ref.3, ECO:0000303|Ref.4};\nGN   OrderedLocusNames=Glyma03g020900 {ECO:0000312|EMBL:KRH65212.1};\nOS   Glycine max (Soybean) (Glycine hispida).\nOC   Eukaryota; Viridiplantae; Streptophyta; Embryophyta; Tracheophyta;\nOC   Spermatophyta; Magnoliopsida; eudicotyledons; Gunneridae; Pentapetalae;\nOC   rosids; fabids; Fabales; Fabaceae; Papilionoideae; 50 kb inversion clade;\nOC   NPAAA clade; indigoferoid/millettioid clade; Phaseoleae; Glycine;\nOC   Glycine subgen. Soja.\nOX   NCBI_TaxID=3847;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 84,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/C6SZ50?format=txt&versions=84)

```json
{
  "evidence_id": "H2",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/C6SZ50?format=txt&versions=84",
  "source_sha256": "1ce346fa691149ee6e809ca984b0d5dbda18272b4eb904ae9e28b38ca8688212",
  "retrieved_utc": "2026-11-02T04:27:36.741333+00:00",
  "source_locator": "lines 150-152",
  "excerpt": "FT   ACT_SITE        93\nFT                   /note=\"Proton donor\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q9SWE5\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 84,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/C6SZ50?format=txt&versions=84)

```json
{
  "evidence_id": "H3",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/C6SZ50?format=txt&versions=84",
  "source_sha256": "1ce346fa691149ee6e809ca984b0d5dbda18272b4eb904ae9e28b38ca8688212",
  "retrieved_utc": "2026-11-02T04:27:36.741333+00:00",
  "source_locator": "lines 153-155",
  "excerpt": "FT   ACT_SITE        178\nFT                   /note=\"Proton donor\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q9SWE5\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 84,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/C6SZ50?format=txt&versions=84)

```json
{
  "evidence_id": "H4",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/C6SZ50?format=txt&versions=84",
  "source_sha256": "1ce346fa691149ee6e809ca984b0d5dbda18272b4eb904ae9e28b38ca8688212",
  "retrieved_utc": "2026-11-02T04:27:36.741333+00:00",
  "source_locator": "lines 156-159",
  "excerpt": "FT   BINDING         31..33\nFT                   /ligand=\"FMN\"\nFT                   /ligand_id=\"ChEBI:CHEBI:58210\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q9SWE5\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 84,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/C6SZ50?format=txt&versions=84)

```json
{
  "evidence_id": "H5",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/C6SZ50?format=txt&versions=84",
  "source_sha256": "1ce346fa691149ee6e809ca984b0d5dbda18272b4eb904ae9e28b38ca8688212",
  "retrieved_utc": "2026-11-02T04:27:36.741333+00:00",
  "source_locator": "lines 160-163",
  "excerpt": "FT   BINDING         56..58\nFT                   /ligand=\"FMN\"\nFT                   /ligand_id=\"ChEBI:CHEBI:58210\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q9SWE5\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 84,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/C6SZ50?format=txt&versions=84)

```json
{
  "evidence_id": "H6",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/C6SZ50?format=txt&versions=84",
  "source_sha256": "1ce346fa691149ee6e809ca984b0d5dbda18272b4eb904ae9e28b38ca8688212",
  "retrieved_utc": "2026-11-02T04:27:36.741333+00:00",
  "source_locator": "lines 164-167",
  "excerpt": "FT   BINDING         109..112\nFT                   /ligand=\"FMN\"\nFT                   /ligand_id=\"ChEBI:CHEBI:58210\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q9SWE5\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 84,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/C6SZ50?format=txt&versions=84)

```json
{
  "evidence_id": "H7",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/C6SZ50?format=txt&versions=84",
  "source_sha256": "1ce346fa691149ee6e809ca984b0d5dbda18272b4eb904ae9e28b38ca8688212",
  "retrieved_utc": "2026-11-02T04:27:36.741333+00:00",
  "source_locator": "lines 168-171",
  "excerpt": "FT   BINDING         143\nFT                   /ligand=\"FMN\"\nFT                   /ligand_id=\"ChEBI:CHEBI:58210\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q9SWE5\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 84,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/C6SZ50?format=txt&versions=84)

```json
{
  "evidence_id": "H8",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/C6SZ50?format=txt&versions=84",
  "source_sha256": "1ce346fa691149ee6e809ca984b0d5dbda18272b4eb904ae9e28b38ca8688212",
  "retrieved_utc": "2026-11-02T04:27:36.741333+00:00",
  "source_locator": "lines 172-175",
  "excerpt": "FT   BINDING         145\nFT                   /ligand=\"N-[(R)-4-phosphopantothenoyl]-L-cysteine\"\nFT                   /ligand_id=\"ChEBI:CHEBI:59458\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q9SWE5\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 84,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/C6SZ50?format=txt&versions=84)

```json
{
  "evidence_id": "H9",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/C6SZ50?format=txt&versions=84",
  "source_sha256": "1ce346fa691149ee6e809ca984b0d5dbda18272b4eb904ae9e28b38ca8688212",
  "retrieved_utc": "2026-11-02T04:27:36.741333+00:00",
  "source_locator": "lines 176-179",
  "excerpt": "FT   BINDING         175\nFT                   /ligand=\"N-[(R)-4-phosphopantothenoyl]-L-cysteine\"\nFT                   /ligand_id=\"ChEBI:CHEBI:59458\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q9SWE5\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 84,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H10

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/C6SZ50?format=txt&versions=84)

```json
{
  "evidence_id": "H10",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/C6SZ50?format=txt&versions=84",
  "source_sha256": "1ce346fa691149ee6e809ca984b0d5dbda18272b4eb904ae9e28b38ca8688212",
  "retrieved_utc": "2026-11-02T04:27:36.741333+00:00",
  "source_locator": "lines 180-183",
  "excerpt": "FT   BINDING         177\nFT                   /ligand=\"N-[(R)-4-phosphopantothenoyl]-L-cysteine\"\nFT                   /ligand_id=\"ChEBI:CHEBI:59458\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q9SWE5\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 84,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H11

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/C6SZ50?format=txt&versions=84)

```json
{
  "evidence_id": "H11",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/C6SZ50?format=txt&versions=84",
  "source_sha256": "1ce346fa691149ee6e809ca984b0d5dbda18272b4eb904ae9e28b38ca8688212",
  "retrieved_utc": "2026-11-02T04:27:36.741333+00:00",
  "source_locator": "lines 184-187",
  "excerpt": "FT   BINDING         186\nFT                   /ligand=\"N-[(R)-4-phosphopantothenoyl]-L-cysteine\"\nFT                   /ligand_id=\"ChEBI:CHEBI:59458\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q9SWE5\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 84,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H12

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/C6SZ50?format=txt&versions=84)

```json
{
  "evidence_id": "H12",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/C6SZ50?format=txt&versions=84",
  "source_sha256": "1ce346fa691149ee6e809ca984b0d5dbda18272b4eb904ae9e28b38ca8688212",
  "retrieved_utc": "2026-11-02T04:27:36.741333+00:00",
  "source_locator": "lines 188-190",
  "excerpt": "FT   SITE            178\nFT                   /note=\"Important for catalytic activity\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q9SWE5\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 84,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/active_site.json), zero-based source row 73. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
