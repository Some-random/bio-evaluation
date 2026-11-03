# catalytic_activity_0109: before and after transfer clarification

[All 1,328 cases](../README.md) · [Method](../METHOD.md) · [Summary](../SUMMARY.md) · [Exact reviewer user message](../inputs/catalytic_activity_0109.txt)

**Task:** `catalytic_activity`  
**Author key, unchanged:** **C** — Hydrolysis of terminal, non-reducing (1-&gt;4)-linked alpha-D-glucose residues with release of alpha-D-glucose.

| Round | Reviewer | Key support | Transfer / lookup | Output usability (canonical status) |
|---|---|---|---|---|
| before | GPT-6 Luna | supported | lookup-dependent | usable output (valid_review) |
| before | Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | usable output (valid_review) |
| after | GPT-6 Luna | no saved label | no saved label | output error (invalid_review) |
| after | Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | usable output (valid_review) |

**Usable output means format-valid review, not reasoning-supported or biologically correct.** A usable output can classify the question as reasoning-supported, lookup-dependent or uncertain. An output error is a problem with the saved model response; it does not count a defective benchmark question or wrong key. Each saved review is retained in full below. Labels from output errors are displayed as saved and excluded from label statistics. The author key and reviewer evidence were visible to reviewers; this is a review of answerability and key support, not a benchmark-solving score.

## Complete original question

```text
[Protein Sequence]
MKTFAPLLATLLLAGFGSALQWWEHGNFYQVYPRSFKDSDGNGIGDLDGVTEKLQYLKDVGMDGIWLSPIFASPMADFGYDISDFYNIQGEYGDLAAFERLSAKCKELGLRLILDFVPNHTSNQHEYFKKSVQKEDPYTNYYVWHPGVTNEDGTKSPPSNWISVFRGSAWEWNEDRQEYYLHQFLKEQPDLNYRDPALVEEMKNVLKFWLNKGVSGFRIDAVPYLFESVEVENRYVDEPLSRATDDAENPAYLIHNQTMDQPETYDMIYQWRAVLDEFTAKDNQTRIMMTEGYTSIPNVMKFFGEGEQNGAQIPFNFQMISNLRKTSTAADFARYANLWLDNLPAGRRSNWVLGNHDNNRIGSRLGEAKIDLYNIALQTLPDIAVTYYGEEIGMVDQPIPFNETVDPAGLRAGPDDYTLYSRDPARTPMQWNSDKNAGFSSADKTWLPVATNYKQLNVKAQDAAQKSHLKLFKRLTTYRKRQILTHGDLDLRTTDSNLVLYKRKVDKVGYVVVVLNFSDEPQSLAAIKQQFPGADDRLQVVASSKLVTIKDNKWINVADTELPGESAIVLQKLWGPNPVVVYEA

[Multiple Choices]
A. N-methyl-4-hydroxy-3,5-dimethoxyphenethylamine + S-adenosyl-L-methionine = N,N-dimethyl-4-hydroxy-3,5-dimethoxyphenethylamine + S-adenosyl-L-homocysteine + H(+)
B. AH2 + 2 S-adenosyl-L-methionine = 2 5'-deoxyadenosin-5'-yl radical + 2 L-methionine + A + 2 H(+)
C. Hydrolysis of terminal, non-reducing (1->4)-linked alpha-D-glucose residues with release of alpha-D-glucose.
D. beta-nicotinamide D-ribonucleotide + ATP + H(+) = diphosphate + NAD(+)
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Enzymatic Reaction Prediction, which is to identify the specific chemical reaction catalyzed by a given enzyme. This involves understanding the enzyme's function based on its amino acid sequence and then selecting the correct transformation of substrates into products from a list of possible reactions.. The inputs provided by the user for this task include:

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

> The exact sequence matches UniProt entry B0XAA1, annotated as salivary alpha-glucosidase with the reaction in choice C. The catalytic-activity annotation carries experimental evidence codes linked to two publications, though those studies were not independently reviewed here.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The N-terminal signal peptide is consistent with a secreted protein and makes the cytosolic-enzyme alternatives less plausible, but it does not establish the enzyme's substrate specificity or exact reaction.


**Missing item-specific fact**

> The supplied input does not provide this protein's experimentally established alpha-glucosidase activity or an identification linking it to that catalytic annotation.


**Reason**

> Selecting the precise hydrolysis reaction requires protein-specific functional knowledge or a reliable family/annotation match. General sequence context alone does not establish hydrolysis of terminal alpha-D-glucose residues.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The choices describe distinct enzyme activities, and the sequence-matched annotation supports C.


### Important caveats

- The cited database evidence is reviewer-only and was not available to the evaluated model.
- The UniProt annotation cites experimental evidence, but the underlying papers were not independently assessed.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal signal peptide is consistent with a secreted protein and makes the cytosolic-enzyme alternatives less plausible, but it does not establish the enzyme's substrate specificity or exact reaction.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The supplied input does not provide this protein's experimentally established alpha-glucosidase activity or an identification linking it to that catalytic annotation.",
    "reason": "Selecting the precise hydrolysis reaction requires protein-specific functional knowledge or a reliable family/annotation match. General sequence context alone does not establish hydrolysis of terminal alpha-D-glucose residues."
  },
  "case_id": "catalytic_activity_0109",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches UniProt entry B0XAA1, annotated as salivary alpha-glucosidase with the reaction in choice C. The catalytic-activity annotation carries experimental evidence codes linked to two publications, though those studies were not independently reviewed here."
  },
  "important_caveats": [
    "The cited database evidence is reviewer-only and was not available to the evaluated model.",
    "The UniProt annotation cites experimental evidence, but the underlying papers were not independently assessed."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The choices describe distinct enzyme activities, and the sequence-matched annotation supports C."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0109",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches UniProt entry B0XAA1, annotated as salivary alpha-glucosidase with the reaction in choice C. The catalytic-activity annotation carries experimental evidence codes linked to two publications, though those studies were not independently reviewed here.",
    "evidence_ids": ["C1", "C4", "C5", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The N-terminal signal peptide is consistent with a secreted protein and makes the cytosolic-enzyme alternatives less plausible, but it does not establish the enzyme's substrate specificity or exact reaction.",
    "missing_item_specific_fact": "The supplied input does not provide this protein's experimentally established alpha-glucosidase activity or an identification linking it to that catalytic annotation.",
    "reason": "Selecting the precise hydrolysis reaction requires protein-specific functional knowledge or a reliable family/annotation match. General sequence context alone does not establish hydrolysis of terminal alpha-D-glucose residues."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The choices describe distinct enzyme activities, and the sequence-matched annotation supports C."
  },
  "important_caveats": [
    "The cited database evidence is reviewer-only and was not available to the evaluated model.",
    "The UniProt annotation cites experimental evidence, but the underlying papers were not independently assessed."
  ]
}
```

</details>

## Before: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The protein sequence (584 aa, sha256-matched) corresponds to UniProt B0XAA1 (MALT_CULQU), Salivary alpha-glucosidase from Culex quinquefasciatus. The catalytic activity is annotated as EC 3.2.1.20: 'Hydrolysis of terminal, non-reducing (1->4)-linked alpha-D-glucose residues with release of alpha-D-glucose,' supported by experimental evidence (ECO:0000269) from PubMed:25746591 and PubMed:38428508. Choice C matches this annotation verbatim.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> Weak elimination-based reasoning is possible: the absence of a CX3CX2C motif argues against radical SAM (B); the 584-aa length and lack of NAD-synthetase active-site architecture argue against D; the absence of a canonical SAM-binding Rossmann-fold motif weakly argues against A. However, none of these negative observations positively identifies the enzyme as a GH31 alpha-glucosidase (EC 3.2.1.20) specifically, as opposed to another glycosidase, protease, or other hydrolase.


**Missing item-specific fact**

> Positive identification requires either recognition of the exact sequence (or its UniProt entry) or detailed knowledge of GH31-family catalytic motifs (e.g., the specific Glu nucleophile and Asp general-acid arrangement in the TIM-barrel active site) sufficient to assign EC 3.2.1.20 from primary sequence alone. The sequence does not contain an easily recognizable, unique catalytic signature that unambiguously distinguishes alpha-glucosidase from other glycoside hydrolases or other enzyme classes without database lookup.


**Reason**

> The four choices span radically different enzyme classes, making elimination of some distractors feasible, but the positive assignment to alpha-glucosidase (EC 3.2.1.20) from a 584-aa sequence without structural context or database access depends on item-specific knowledge of GH31 family motifs or direct recognition of this protein. General biological knowledge alone does not provide a concrete, sequence-grounded argument that uniquely selects C over, say, a generic glycosidase or another hydrolase.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four choices represent distinct enzyme classes (methyltransferase, radical SAM, glycosidase, NAD synthetase). Given the correct annotation, only C is correct. The distractors are from sufficiently different enzyme classes that they are unlikely to be confused with the true answer by a knowledgeable reader, though the positive identification of C from sequence alone is difficult.


### Important caveats

- The reviewer-only evidence confirms the annotation via experimental evidence codes (ECO:0000269), establishing the key is scientifically grounded.
- The sequence match between the benchmark input and UniProt B0XAA1 is exact (sha256 confirmed), so the annotation applies directly.
- The UniProt entry was first public in 2025-04-09; if the benchmark was constructed before that date, the annotation may not have been available in the author's source snapshot, though the underlying publications (2015, 2024) predate the entry.
- Elimination-based reasoning (removing B and D) is possible but does not constitute positive identification of alpha-glucosidase activity.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Weak elimination-based reasoning is possible: the absence of a CX3CX2C motif argues against radical SAM (B); the 584-aa length and lack of NAD-synthetase active-site architecture argue against D; the absence of a canonical SAM-binding Rossmann-fold motif weakly argues against A. However, none of these negative observations positively identifies the enzyme as a GH31 alpha-glucosidase (EC 3.2.1.20) specifically, as opposed to another glycosidase, protease, or other hydrolase.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "Positive identification requires either recognition of the exact sequence (or its UniProt entry) or detailed knowledge of GH31-family catalytic motifs (e.g., the specific Glu nucleophile and Asp general-acid arrangement in the TIM-barrel active site) sufficient to assign EC 3.2.1.20 from primary sequence alone. The sequence does not contain an easily recognizable, unique catalytic signature that unambiguously distinguishes alpha-glucosidase from other glycoside hydrolases or other enzyme classes without database lookup.",
    "reason": "The four choices span radically different enzyme classes, making elimination of some distractors feasible, but the positive assignment to alpha-glucosidase (EC 3.2.1.20) from a 584-aa sequence without structural context or database access depends on item-specific knowledge of GH31 family motifs or direct recognition of this protein. General biological knowledge alone does not provide a concrete, sequence-grounded argument that uniquely selects C over, say, a generic glycosidase or another hydrolase."
  },
  "case_id": "catalytic_activity_0109",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C7",
      "H2",
      "H3",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The protein sequence (584 aa, sha256-matched) corresponds to UniProt B0XAA1 (MALT_CULQU), Salivary alpha-glucosidase from Culex quinquefasciatus. The catalytic activity is annotated as EC 3.2.1.20: 'Hydrolysis of terminal, non-reducing (1->4)-linked alpha-D-glucose residues with release of alpha-D-glucose,' supported by experimental evidence (ECO:0000269) from PubMed:25746591 and PubMed:38428508. Choice C matches this annotation verbatim."
  },
  "important_caveats": [
    "The reviewer-only evidence confirms the annotation via experimental evidence codes (ECO:0000269), establishing the key is scientifically grounded.",
    "The sequence match between the benchmark input and UniProt B0XAA1 is exact (sha256 confirmed), so the annotation applies directly.",
    "The UniProt entry was first public in 2025-04-09; if the benchmark was constructed before that date, the annotation may not have been available in the author's source snapshot, though the underlying publications (2015, 2024) predate the entry.",
    "Elimination-based reasoning (removing B and D) is possible but does not constitute positive identification of alpha-glucosidase activity."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices represent distinct enzyme classes (methyltransferase, radical SAM, glycosidase, NAD synthetase). Given the correct annotation, only C is correct. The distractors are from sufficiently different enzyme classes that they are unlikely to be confused with the true answer by a knowledgeable reader, though the positive identification of C from sequence alone is difficult."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0109",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The protein sequence (584 aa, sha256-matched) corresponds to UniProt B0XAA1 (MALT_CULQU), Salivary alpha-glucosidase from Culex quinquefasciatus. The catalytic activity is annotated as EC 3.2.1.20: 'Hydrolysis of terminal, non-reducing (1->4)-linked alpha-D-glucose residues with release of alpha-D-glucose,' supported by experimental evidence (ECO:0000269) from PubMed:25746591 and PubMed:38428508. Choice C matches this annotation verbatim.",
    "evidence_ids": ["C4", "C5", "C6", "C7", "H2", "H3", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "Weak elimination-based reasoning is possible: the absence of a CX3CX2C motif argues against radical SAM (B); the 584-aa length and lack of NAD-synthetase active-site architecture argue against D; the absence of a canonical SAM-binding Rossmann-fold motif weakly argues against A. However, none of these negative observations positively identifies the enzyme as a GH31 alpha-glucosidase (EC 3.2.1.20) specifically, as opposed to another glycosidase, protease, or other hydrolase.",
    "missing_item_specific_fact": "Positive identification requires either recognition of the exact sequence (or its UniProt entry) or detailed knowledge of GH31-family catalytic motifs (e.g., the specific Glu nucleophile and Asp general-acid arrangement in the TIM-barrel active site) sufficient to assign EC 3.2.1.20 from primary sequence alone. The sequence does not contain an easily recognizable, unique catalytic signature that unambiguously distinguishes alpha-glucosidase from other glycoside hydrolases or other enzyme classes without database lookup.",
    "reason": "The four choices span radically different enzyme classes, making elimination of some distractors feasible, but the positive assignment to alpha-glucosidase (EC 3.2.1.20) from a 584-aa sequence without structural context or database access depends on item-specific knowledge of GH31 family motifs or direct recognition of this protein. General biological knowledge alone does not provide a concrete, sequence-grounded argument that uniquely selects C over, say, a generic glycosidase or another hydrolase."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices represent distinct enzyme classes (methyltransferase, radical SAM, glycosidase, NAD synthetase). Given the correct annotation, only C is correct. The distractors are from sufficiently different enzyme classes that they are unlikely to be confused with the true answer by a knowledgeable reader, though the positive identification of C from sequence alone is difficult."
  },
  "important_caveats": [
    "The reviewer-only evidence confirms the annotation via experimental evidence codes (ECO:0000269), establishing the key is scientifically grounded.",
    "The sequence match between the benchmark input and UniProt B0XAA1 is exact (sha256 confirmed), so the annotation applies directly.",
    "The UniProt entry was first public in 2025-04-09; if the benchmark was constructed before that date, the annotation may not have been available in the author's source snapshot, though the underlying publications (2015, 2024) predate the entry.",
    "Elimination-based reasoning (removing B and D) is possible but does not constitute positive identification of alpha-glucosidase activity."
  ]
}
```

</details>

## After: GPT-6 Luna

**Output usability:** output error.
**Canonical saved status:** `invalid_review`.

**This saved response has an output error and is not a usable structured review.** Any labels below remain the original saved values; they are excluded from label distributions and agreement. This output status does not judge the benchmark question, author key or biological correctness. No field or option ID has been repaired.

**Validation errors:** `invalid_json:Expecting property name enclosed in double quotes: line 13 column 3 (char 1300)`.

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0109",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation assigns this protein the reaction in option C and cites experimental evidence codes for that catalytic activity. This supports the key, though the cited primary studies were not independently reviewed here.",
    "evidence_ids": ["C5", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The N-terminus has a hydrophobic signal-peptide-like segment, consistent with a secreted enzyme, and the long sequence is compatible with a eukaryotic glycoside hydrolase. Family-level knowledge of secreted alpha-glucosidases makes cleavage of alpha-glucose linkages (C) a credible inference. The alternatives instead describe a small-molecule methyltransferase, a radical-SAM reaction, or ATP-dependent NAD synthesis, none of which fits that sequence/context nearly as well.",
    "missing_item_specific_fact": "",
    "reason": "Transferable sequence and enzyme-family patterns meaningfully distinguish the glycoside-hydrolysis option from the three chemically and biologically different alternatives, even without establishing the exact substrate specificity from first principles.",
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The offered reactions describe distinct enzyme activities, and the sequence/context supports option C over the others."
  },
  "important_caveats": [
    "The signal-peptide and family interpretation is an inference from the supplied sequence, not direct experimental evidence shown to the model.",
    "The database annotation cites experimental evidence, but the primary papers were not independently validated in this review."
  ]
}
```

</details>

**Saved parsed visible review:** `null`.

## After: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry B0XAA1 (sequence matched) annotates this protein as Salivary alpha-glucosidase with EC 3.2.1.20 and the catalytic activity 'Hydrolysis of terminal, non-reducing (1->4)-linked alpha-D-glucose residues with release of alpha-D-glucose.' This annotation is backed by experimental evidence (ECO:0000269) from two independent PubMed studies (25746591 and 38428508). The expected answer C matches the annotated reaction exactly.

Citations as saved: [C5](#evidence-c5), [C4](#evidence-c4), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence begins with a clear hydrophobic signal peptide (MKTFAPLLATLLLAGFGSALQWWEHG), indicating a secreted protein. This immediately disfavors options B (radical SAM enzymes are intracellular and require a CX3CX2C motif, which is absent) and D (NAD synthase/NMN adenylyltransferase is intracellular). The total length of 584 residues is far too long for option A (COMT is ~271 aa, cytoplasmic, no signal peptide). The remaining option C (alpha-glucosidase, GH31 family) is consistent with: (1) a secreted insect salivary enzyme, (2) the ~500-600 aa length typical of GH31 catalytic domains, (3) the absence of motifs diagnostic of the other three families. Family-level knowledge that insect salivary alpha-glucosidases (GH31) are secreted proteins of this approximate size provides a credible transferable inference to select C among the four offered choices.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The signal peptide (visible in the N-terminal hydrophobic stretch), the 584-aa length, the absence of a radical SAM CX3CX2C motif, and general knowledge that COMT is ~271 aa and cytoplasmic collectively eliminate A, B, and D. GH31 alpha-glucosidases in insects are well-known secreted salivary enzymes of this size, making C the only viable option through family-level reasoning without needing the exact database annotation for this specific protein.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options represent very different enzyme classes (methyltransferase, radical SAM, glycosidase, nucleotidyltransferase). The signal peptide, length, and absence of family-specific motifs for A, B, and D leave C as the uniquely consistent choice. No two options are simultaneously defensible.


### Important caveats

- The signal peptide recognition is based on the hydrophobic N-terminal stretch; while highly suggestive, formal signal peptide prediction tools would confirm this.
- The argument relies on the four offered choices being the only alternatives; in a broader search, other secreted 584-aa enzymes could exist, but the question constrains the answer space to these four.
- The UniProt annotation is experimentally supported (ECO:0000269) from two independent studies, strengthening confidence in the key.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence begins with a clear hydrophobic signal peptide (MKTFAPLLATLLLAGFGSALQWWEHG), indicating a secreted protein. This immediately disfavors options B (radical SAM enzymes are intracellular and require a CX3CX2C motif, which is absent) and D (NAD synthase/NMN adenylyltransferase is intracellular). The total length of 584 residues is far too long for option A (COMT is ~271 aa, cytoplasmic, no signal peptide). The remaining option C (alpha-glucosidase, GH31 family) is consistent with: (1) a secreted insect salivary enzyme, (2) the ~500-600 aa length typical of GH31 catalytic domains, (3) the absence of motifs diagnostic of the other three families. Family-level knowledge that insect salivary alpha-glucosidases (GH31) are secreted proteins of this approximate size provides a credible transferable inference to select C among the four offered choices.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The signal peptide (visible in the N-terminal hydrophobic stretch), the 584-aa length, the absence of a radical SAM CX3CX2C motif, and general knowledge that COMT is ~271 aa and cytoplasmic collectively eliminate A, B, and D. GH31 alpha-glucosidases in insects are well-known secreted salivary enzymes of this size, making C the only viable option through family-level reasoning without needing the exact database annotation for this specific protein."
  },
  "case_id": "catalytic_activity_0109",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry B0XAA1 (sequence matched) annotates this protein as Salivary alpha-glucosidase with EC 3.2.1.20 and the catalytic activity 'Hydrolysis of terminal, non-reducing (1->4)-linked alpha-D-glucose residues with release of alpha-D-glucose.' This annotation is backed by experimental evidence (ECO:0000269) from two independent PubMed studies (25746591 and 38428508). The expected answer C matches the annotated reaction exactly."
  },
  "important_caveats": [
    "The signal peptide recognition is based on the hydrophobic N-terminal stretch; while highly suggestive, formal signal peptide prediction tools would confirm this.",
    "The argument relies on the four offered choices being the only alternatives; in a broader search, other secreted 584-aa enzymes could exist, but the question constrains the answer space to these four.",
    "The UniProt annotation is experimentally supported (ECO:0000269) from two independent studies, strengthening confidence in the key."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent very different enzyme classes (methyltransferase, radical SAM, glycosidase, nucleotidyltransferase). The signal peptide, length, and absence of family-specific motifs for A, B, and D leave C as the uniquely consistent choice. No two options are simultaneously defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0109",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry B0XAA1 (sequence matched) annotates this protein as Salivary alpha-glucosidase with EC 3.2.1.20 and the catalytic activity 'Hydrolysis of terminal, non-reducing (1->4)-linked alpha-D-glucose residues with release of alpha-D-glucose.' This annotation is backed by experimental evidence (ECO:0000269) from two independent PubMed studies (25746591 and 38428508). The expected answer C matches the annotated reaction exactly.",
    "evidence_ids": ["C5", "C4", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence begins with a clear hydrophobic signal peptide (MKTFAPLLATLLLAGFGSALQWWEHG), indicating a secreted protein. This immediately disfavors options B (radical SAM enzymes are intracellular and require a CX3CX2C motif, which is absent) and D (NAD synthase/NMN adenylyltransferase is intracellular). The total length of 584 residues is far too long for option A (COMT is ~271 aa, cytoplasmic, no signal peptide). The remaining option C (alpha-glucosidase, GH31 family) is consistent with: (1) a secreted insect salivary enzyme, (2) the ~500-600 aa length typical of GH31 catalytic domains, (3) the absence of motifs diagnostic of the other three families. Family-level knowledge that insect salivary alpha-glucosidases (GH31) are secreted proteins of this approximate size provides a credible transferable inference to select C among the four offered choices.",
    "missing_item_specific_fact": "",
    "reason": "The signal peptide (visible in the N-terminal hydrophobic stretch), the 584-aa length, the absence of a radical SAM CX3CX2C motif, and general knowledge that COMT is ~271 aa and cytoplasmic collectively eliminate A, B, and D. GH31 alpha-glucosidases in insects are well-known secreted salivary enzymes of this size, making C the only viable option through family-level reasoning without needing the exact database annotation for this specific protein."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent very different enzyme classes (methyltransferase, radical SAM, glycosidase, nucleotidyltransferase). The signal peptide, length, and absence of family-specific motifs for A, B, and D leave C as the uniquely consistent choice. No two options are simultaneously defensible."
  },
  "important_caveats": [
    "The signal peptide recognition is based on the hydrophobic N-terminal stretch; while highly suggestive, formal signal peptide prediction tools would confirm this.",
    "The argument relies on the four offered choices being the only alternatives; in a broader search, other secreted 584-aa enzymes could exist, but the question constrains the answer space to these four.",
    "The UniProt annotation is experimentally supported (ECO:0000269) from two independent studies, strengthening confidence in the key."
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
  "requested_accession": "B0XAA1",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "benchmark_sequence_sha256": "29d6b8000e7795f6bbd083f2568cece3ab8850588bc2d1c4dda913580b5b41a1",
  "benchmark_sequence_length": 584,
  "current_status": "retrieved",
  "current_sequence_comparison": "matched",
  "current_entry_audit": {
    "entryVersion": 94,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2008-04-08",
    "sequenceVersion": 1
  },
  "current_uniprot_release": "2026_03",
  "current_record_sha256": "9afccd0935d9c913183f609d3d8afcc2196f79187f5d0532d2ba6ed0e5048c10",
  "current_source_sequence_sha256": "29d6b8000e7795f6bbd083f2568cece3ab8850588bc2d1c4dda913580b5b41a1",
  "current_source_sequence_length": 584,
  "historical_status": "retrieved",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "selected_historical_entry_version": 92,
  "selected_historical_version": {
    "accession": "B0XAA1",
    "database": "Swiss-Prot",
    "entryVersion": 92,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "MALT_CULQU",
    "sequenceVersion": 1
  },
  "selected_historical_record_sha256": "5fda9ac6361a740657451da46434a8060a2e37043092db9553e846bf116af583",
  "selected_historical_source_sequence_sha256": "29d6b8000e7795f6bbd083f2568cece3ab8850588bc2d1c4dda913580b5b41a1",
  "selected_historical_source_sequence_length": 584,
  "latest_at_cutoff_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 92,
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B0XAA1.json)

```json
{
  "evidence_id": "C1",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/B0XAA1.json",
  "source_sha256": "9afccd0935d9c913183f609d3d8afcc2196f79187f5d0532d2ba6ed0e5048c10",
  "retrieved_utc": "2026-11-02T04:27:15.565561+00:00",
  "json_pointer": "/primaryAccession",
  "excerpt": "\"B0XAA1\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B0XAA1.json)

```json
{
  "evidence_id": "C2",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/B0XAA1.json",
  "source_sha256": "9afccd0935d9c913183f609d3d8afcc2196f79187f5d0532d2ba6ed0e5048c10",
  "retrieved_utc": "2026-11-02T04:27:15.565561+00:00",
  "json_pointer": "/entryAudit",
  "excerpt": "{\"entryVersion\":94,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2008-04-08\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B0XAA1.json)

```json
{
  "evidence_id": "C3",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/B0XAA1.json",
  "source_sha256": "9afccd0935d9c913183f609d3d8afcc2196f79187f5d0532d2ba6ed0e5048c10",
  "retrieved_utc": "2026-11-02T04:27:15.565561+00:00",
  "json_pointer": "/organism",
  "excerpt": "{\"commonName\":\"Southern house mosquito\",\"lineage\":[\"Eukaryota\",\"Metazoa\",\"Ecdysozoa\",\"Arthropoda\",\"Altocrustacea\",\"Allotriocarida\",\"Hexapoda\",\"Insecta\",\"Pterygota\",\"Neoptera\",\"Eumetabola\",\"Endopterygota\",\"Aparaglossata\",\"Panorpida\",\"Diptera\",\"Nematocera\",\"Culicoidea\",\"Culicidae\",\"Culicinae\",\"Culicini\",\"Culex\",\"Culex\"],\"scientificName\":\"Culex quinquefasciatus\",\"synonyms\":[\"Culex pungens\"],\"taxonId\":7176}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B0XAA1.json)

```json
{
  "evidence_id": "C4",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/B0XAA1.json",
  "source_sha256": "9afccd0935d9c913183f609d3d8afcc2196f79187f5d0532d2ba6ed0e5048c10",
  "retrieved_utc": "2026-11-02T04:27:15.565561+00:00",
  "json_pointer": "/proteinDescription",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"25746591\",\"source\":\"PubMed\"}],\"value\":\"CQMalI\"}}],\"flag\":\"Precursor\",\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"25746591\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38428508\",\"source\":\"PubMed\"}],\"value\":\"3.2.1.20\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"38428508\",\"source\":\"PubMed\"}],\"value\":\"Salivary alpha-glucosidase\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"38428508\",\"source\":\"PubMed\"}],\"value\":\"CxGluc\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B0XAA1.json)

```json
{
  "evidence_id": "C5",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/B0XAA1.json",
  "source_sha256": "9afccd0935d9c913183f609d3d8afcc2196f79187f5d0532d2ba6ed0e5048c10",
  "retrieved_utc": "2026-11-02T04:27:15.565561+00:00",
  "json_pointer": "/comments/1",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"ecNumber\":\"3.2.1.20\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"25746591\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38428508\",\"source\":\"PubMed\"}],\"name\":\"Hydrolysis of terminal, non-reducing (1->4)-linked alpha-D-glucose residues with release of alpha-D-glucose.\"}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B0XAA1.json)

```json
{
  "evidence_id": "C6",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/B0XAA1.json",
  "source_sha256": "9afccd0935d9c913183f609d3d8afcc2196f79187f5d0532d2ba6ed0e5048c10",
  "retrieved_utc": "2026-11-02T04:27:15.565561+00:00",
  "json_pointer": "/references/1",
  "excerpt": "{\"citation\":{\"authors\":[\"Suthangkornkul R.\",\"Sirichaiyakul P.\",\"Sungvornyothin S.\",\"Thepouyporn A.\",\"Svasti J.\",\"Arthan D.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"25746591\"},{\"database\":\"DOI\",\"id\":\"10.1016/j.pep.2015.02.018\"}],\"citationType\":\"journal article\",\"firstPage\":\"145\",\"id\":\"25746591\",\"journal\":\"Protein Expr. Purif.\",\"lastPage\":\"150\",\"publicationDate\":\"2015\",\"title\":\"Functional expression and molecular characterization of Culex quinquefasciatus salivary alpha-glucosidase (MalI).\",\"volume\":\"110\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"ACTIVITY REGULATION\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"GLYCOSYLATION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B0XAA1.json)

```json
{
  "evidence_id": "C7",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/B0XAA1.json",
  "source_sha256": "9afccd0935d9c913183f609d3d8afcc2196f79187f5d0532d2ba6ed0e5048c10",
  "retrieved_utc": "2026-11-02T04:27:15.565561+00:00",
  "json_pointer": "/references/2",
  "excerpt": "{\"citation\":{\"authors\":[\"Williams A.E.\",\"Gittis A.G.\",\"Botello K.\",\"Cruz P.\",\"Martin-Martin I.\",\"Valenzuela Leon P.C.\",\"Sumner B.\",\"Bonilla B.\",\"Calvo E.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"38428508\"},{\"database\":\"DOI\",\"id\":\"10.1016/j.ibmb.2024.104097\"}],\"citationType\":\"journal article\",\"firstPage\":\"104097\",\"id\":\"38428508\",\"journal\":\"Insect Biochem. Mol. Biol.\",\"lastPage\":\"104097\",\"publicationDate\":\"2024\",\"title\":\"Structural and functional comparisons of salivary alpha-glucosidases from the mosquito vectors Aedes aegypti, Anopheles gambiae, and Culex quinquefasciatus.\",\"volume\":\"167\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":3,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"SUBCELLULAR LOCATION\",\"TISSUE SPECIFICITY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B0XAA1?format=txt&versions=92)

```json
{
  "evidence_id": "H1",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/B0XAA1?format=txt&versions=92",
  "source_sha256": "5fda9ac6361a740657451da46434a8060a2e37043092db9553e846bf116af583",
  "retrieved_utc": "2026-11-02T04:27:18.547256+00:00",
  "source_locator": "lines 1-17",
  "excerpt": "ID   MALT_CULQU              Reviewed;         584 AA.\nAC   B0XAA1;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   08-APR-2008, sequence version 1.\nDT   28-JAN-2026, entry version 92.\nDE   RecName: Full=Salivary alpha-glucosidase {ECO:0000303|PubMed:38428508};\nDE            Short=CxGluc {ECO:0000303|PubMed:38428508};\nDE            EC=3.2.1.20 {ECO:0000269|PubMed:25746591, ECO:0000269|PubMed:38428508};\nDE   AltName: Full=CQMalI {ECO:0000303|PubMed:25746591};\nDE   Flags: Precursor;\nGN   Name=MAL1 {ECO:0000303|PubMed:25746591};\nGN   ORFNames=CpipJ_CPIJ016362 {ECO:0000312|EMBL:EDS43598.1};\nOS   Culex quinquefasciatus (Southern house mosquito) (Culex pungens).\nOC   Eukaryota; Metazoa; Ecdysozoa; Arthropoda; Hexapoda; Insecta; Pterygota;\nOC   Neoptera; Endopterygota; Diptera; Nematocera; Culicoidea; Culicidae;\nOC   Culicinae; Culicini; Culex; Culex.\nOX   NCBI_TaxID=7176;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 92,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B0XAA1?format=txt&versions=92)

```json
{
  "evidence_id": "H2",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/B0XAA1?format=txt&versions=92",
  "source_sha256": "5fda9ac6361a740657451da46434a8060a2e37043092db9553e846bf116af583",
  "retrieved_utc": "2026-11-02T04:27:18.547256+00:00",
  "source_locator": "lines 6-10",
  "excerpt": "DE   RecName: Full=Salivary alpha-glucosidase {ECO:0000303|PubMed:38428508};\nDE            Short=CxGluc {ECO:0000303|PubMed:38428508};\nDE            EC=3.2.1.20 {ECO:0000269|PubMed:25746591, ECO:0000269|PubMed:38428508};\nDE   AltName: Full=CQMalI {ECO:0000303|PubMed:25746591};\nDE   Flags: Precursor;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 92,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B0XAA1?format=txt&versions=92)

```json
{
  "evidence_id": "H3",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/B0XAA1?format=txt&versions=92",
  "source_sha256": "5fda9ac6361a740657451da46434a8060a2e37043092db9553e846bf116af583",
  "retrieved_utc": "2026-11-02T04:27:18.547256+00:00",
  "source_locator": "lines 32-40",
  "excerpt": "RN   [2] {ECO:0000305}\nRP   FUNCTION, CATALYTIC ACTIVITY, ACTIVITY REGULATION, BIOPHYSICOCHEMICAL\nRP   PROPERTIES, AND GLYCOSYLATION.\nRX   PubMed=25746591; DOI=10.1016/j.pep.2015.02.018;\nRA   Suthangkornkul R., Sirichaiyakul P., Sungvornyothin S., Thepouyporn A.,\nRA   Svasti J., Arthan D.;\nRT   \"Functional expression and molecular characterization of Culex\nRT   quinquefasciatus salivary alpha-glucosidase (MalI).\";\nRL   Protein Expr. Purif. 110:145-150(2015).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 92,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B0XAA1?format=txt&versions=92)

```json
{
  "evidence_id": "H4",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/B0XAA1?format=txt&versions=92",
  "source_sha256": "5fda9ac6361a740657451da46434a8060a2e37043092db9553e846bf116af583",
  "retrieved_utc": "2026-11-02T04:27:18.547256+00:00",
  "source_locator": "lines 41-50",
  "excerpt": "RN   [3] {ECO:0000305}\nRP   FUNCTION, CATALYTIC ACTIVITY, BIOPHYSICOCHEMICAL PROPERTIES, SUBCELLULAR\nRP   LOCATION, AND TISSUE SPECIFICITY.\nRX   PubMed=38428508; DOI=10.1016/j.ibmb.2024.104097;\nRA   Williams A.E., Gittis A.G., Botello K., Cruz P., Martin-Martin I.,\nRA   Valenzuela Leon P.C., Sumner B., Bonilla B., Calvo E.;\nRT   \"Structural and functional comparisons of salivary alpha-glucosidases from\nRT   the mosquito vectors Aedes aegypti, Anopheles gambiae, and Culex\nRT   quinquefasciatus.\";\nRL   Insect Biochem. Mol. Biol. 167:104097-104097(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 92,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B0XAA1?format=txt&versions=92)

```json
{
  "evidence_id": "H5",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/B0XAA1?format=txt&versions=92",
  "source_sha256": "5fda9ac6361a740657451da46434a8060a2e37043092db9553e846bf116af583",
  "retrieved_utc": "2026-11-02T04:27:18.547256+00:00",
  "source_locator": "lines 56-59",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=Hydrolysis of terminal, non-reducing (1->4)-linked alpha-D-\nCC         glucose residues with release of alpha-D-glucose.; EC=3.2.1.20;\nCC         Evidence={ECO:0000269|PubMed:25746591, ECO:0000269|PubMed:38428508};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 92,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 109. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
