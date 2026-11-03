# EC_number_0175: before and after transfer clarification

[All 1,328 cases](../README.md) · [Method](../METHOD.md) · [Summary](../SUMMARY.md) · [Exact reviewer user message](../inputs/EC_number_0175.txt)

**Task:** `EC_number`  
**Author key, unchanged:** **C** — 1.14.14.154

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
MGLSHSGEIVYIHPSSPVDLFTTCASLPTKPPPSFSDMPSPLFLVSGFLGVCVAYAVANIIRQLLFPNAKEPPVVFHWFPWLGSALTYGKDPYKFLFAARAKYGDVFTFVLLGRNVTVHLGVAGNDFVFNGKETHMNAEEIYGPLCNPVFGEGVVYDCPNSKLMEQKKFVKFGLTTDALKAHVRLIEHEVVNYIKSSRDFKGPSGVINVPPVMAQITIFTAAIALQGPEVRSKLTNEFASLYHDLDGGFSPINFVLPHAPFPHNIKRDRAQLKMRKIYEAIIAERRAGKIPPTTDMISHLMQCSYKNGRPIPDSEISNMMITILMAGQHNSSNIASWIMLHLANEPQLCEELYQEQLDQLADEHGNLPELELHTVEKLKLHSSVVKETLRMHNAIHSIMRLVKQPLPVPNTSWTVPPGHAVLASPGVSANSNEYFLNPTKWDPHRWDDRVIEEDDESEMVDYGYGRTSRGTKSAYLPFGGGRHRCIGEKFAYLNLEVITAVMVRNFRFKNVDGRVDVPGTDYSTMFSRPLEPAEICWERR

[Multiple Choices]
A. 1.14.14.104
B. 3.2.1.183
C. 1.14.14.154
D. 5.2.1.8
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Enzyme Commission (EC) Number Prediction, which is to predict the complete 4-digit Enzyme Commission (EC) number for a given protein. The EC number is a numerical classification that categorizes enzymes based on the chemical reactions they catalyze. You should select the most accurate EC number from the provided options based on the protein's sequence.. The inputs provided by the user for this task include:

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

> The exact 540-residue sequence matches the UniProt entry annotated as sterol 14-alpha demethylase with EC 1.14.14.154, supporting choice C. The EC assignment cites a publication; the listed catalytic-reaction annotations include evidence transferred from homologs, so they should not be treated as direct experimental measurements of this exact protein.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H1](#evidence-h1), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> Sequence features may support identifying this as a cytochrome P450, which makes the P450 choices more plausible than the hydrolase or isomerase choices. But that broad family-level inference does not establish which specific P450 reaction, and thus which complete EC number, applies.


**Missing item-specific fact**

> The protein-specific identification as sterol 14-alpha demethylase (CYP51) and its associated reaction specificity are needed to distinguish EC 1.14.14.154 from another P450 option such as 1.14.14.104.


**Reason**

> The supplied sequence and choices do not provide the functional or substrate-specific annotation needed for a complete four-part EC number. Recognizing the broad enzyme family is not enough to infer the precise EC subclass.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The matched database annotation supports a unique EC assignment for this protein. The limitation is that the input does not establish that assignment, rather than that multiple EC numbers are equally correct for the protein.


### Important caveats

- The accession and database records are reviewer-only evidence, not information supplied to the evaluated model.
- The sequence match supports applying the annotation to the sequence in the question, but database annotation and homology-transferred reaction evidence are not equivalent to independent experimental validation of every listed reaction.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Sequence features may support identifying this as a cytochrome P450, which makes the P450 choices more plausible than the hydrolase or isomerase choices. But that broad family-level inference does not establish which specific P450 reaction, and thus which complete EC number, applies.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific identification as sterol 14-alpha demethylase (CYP51) and its associated reaction specificity are needed to distinguish EC 1.14.14.154 from another P450 option such as 1.14.14.104.",
    "reason": "The supplied sequence and choices do not provide the functional or substrate-specific annotation needed for a complete four-part EC number. Recognizing the broad enzyme family is not enough to infer the precise EC subclass."
  },
  "case_id": "EC_number_0175",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H1",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact 540-residue sequence matches the UniProt entry annotated as sterol 14-alpha demethylase with EC 1.14.14.154, supporting choice C. The EC assignment cites a publication; the listed catalytic-reaction annotations include evidence transferred from homologs, so they should not be treated as direct experimental measurements of this exact protein."
  },
  "important_caveats": [
    "The accession and database records are reviewer-only evidence, not information supplied to the evaluated model.",
    "The sequence match supports applying the annotation to the sequence in the question, but database annotation and homology-transferred reaction evidence are not equivalent to independent experimental validation of every listed reaction."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched database annotation supports a unique EC assignment for this protein. The limitation is that the input does not establish that assignment, rather than that multiple EC numbers are equally correct for the protein."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0175",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact 540-residue sequence matches the UniProt entry annotated as sterol 14-alpha demethylase with EC 1.14.14.154, supporting choice C. The EC assignment cites a publication; the listed catalytic-reaction annotations include evidence transferred from homologs, so they should not be treated as direct experimental measurements of this exact protein.",
    "evidence_ids": ["C1", "C4", "C5", "H1", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "Sequence features may support identifying this as a cytochrome P450, which makes the P450 choices more plausible than the hydrolase or isomerase choices. But that broad family-level inference does not establish which specific P450 reaction, and thus which complete EC number, applies.",
    "missing_item_specific_fact": "The protein-specific identification as sterol 14-alpha demethylase (CYP51) and its associated reaction specificity are needed to distinguish EC 1.14.14.154 from another P450 option such as 1.14.14.104.",
    "reason": "The supplied sequence and choices do not provide the functional or substrate-specific annotation needed for a complete four-part EC number. Recognizing the broad enzyme family is not enough to infer the precise EC subclass."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched database annotation supports a unique EC assignment for this protein. The limitation is that the input does not establish that assignment, rather than that multiple EC numbers are equally correct for the protein."
  },
  "important_caveats": [
    "The accession and database records are reviewer-only evidence, not information supplied to the evaluated model.",
    "The sequence match supports applying the annotation to the sequence in the question, but database annotation and homology-transferred reaction evidence are not equivalent to independent experimental validation of every listed reaction."
  ]
}
```

</details>

## Before: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry P0DXV0 (LAN1_PYRDE) is annotated with EC 1.14.14.154 (Sterol 14-alpha demethylase), with evidence code ECO:0000305 (inferred from direct assay) linked to PubMed:33857369 (Liu et al., 2021). The benchmark sequence matches the source sequence exactly (540 AA, SHA256 confirmed). Multiple catalytic activity reactions confirm 14α-demethylation of sterols (lanosterol, eburicol, generic 14α-methyl steroids) with NADPH-hemoprotein reductase and O2, consistent with EC 1.14.14.154.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C9](#evidence-c9), [C13](#evidence-c13), [H1](#evidence-h1), [H2](#evidence-h2), [H4](#evidence-h4), [H8](#evidence-h8), [H12](#evidence-h12).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence contains a canonical P450 heme-binding motif (FGGGRHRCIGEKF with the conserved axial Cys), confirming membership in EC class 1.14.14 (P450 monooxygenases). This eliminates B (3.2.1.183, glycosidase) and D (5.2.1.8, isomerase) as they belong to entirely different EC classes. However, both A (1.14.14.104) and C (1.14.14.154) are P450 monooxygenases in the same EC subclass. Distinguishing the 4th digit (specific substrate/reaction: sterol 14α-demethylase vs. another P450 reaction) from sequence alone requires knowing which specific substrate this enzyme acts upon.


**Missing item-specific fact**

> The specific substrate identity (14α-methyl sterol demethylation vs. whatever reaction EC 1.14.14.104 catalyzes) is an item-specific annotation fact. While one might weakly argue that fungal P450s are commonly CYP51, this is a statistical prior, not a deterministic sequence-based argument. The 4th EC digit for P450s encodes the specific substrate, which cannot be reliably deduced from general sequence features without database lookup.


**Reason**

> The question reduces to identifying the correct 4th-digit EC number among two P450 monooxygenase options. Sequence features (heme-binding motif, ~540 AA length, overall P450 fold) establish the 1.14.14 class but cannot distinguish between two specific P450 reactions. Selecting 154 over 104 requires either recognizing the exact sequence as CYP51 from memorization or accessing the UniProt annotation—both are lookup-dependent operations rather than general biological reasoning.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "C"
]
```

> Both A (1.14.14.104) and C (1.14.14.154) are P450 monooxygenase EC numbers. Without the specific substrate information or CYP51-specific active-site motif knowledge, a model cannot definitively distinguish between them from sequence alone. B and D are clearly eliminable (wrong EC class), but A vs C requires item-specific knowledge.


### Important caveats

- The EC 1.14.14.154 annotation carries evidence code ECO:0000305 (inferred from direct assay), indicating experimental support from PubMed:33857369, not merely computational prediction.
- The entry was first published 2025-02-05, making it a relatively recent annotation; the benchmark author's source snapshot is unknown.
- EC 1.14.14.104's specific identity was not independently verified in the supplied evidence; its plausibility as a P450 distractor is assumed from the EC numbering scheme.
- The sequence is from a fungal organism (Pyrenophora dematioidea), which weakly supports CYP51 (essential for ergosterol biosynthesis) as the most common fungal P450, but this statistical argument does not definitively exclude EC 1.14.14.104.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a canonical P450 heme-binding motif (FGGGRHRCIGEKF with the conserved axial Cys), confirming membership in EC class 1.14.14 (P450 monooxygenases). This eliminates B (3.2.1.183, glycosidase) and D (5.2.1.8, isomerase) as they belong to entirely different EC classes. However, both A (1.14.14.104) and C (1.14.14.154) are P450 monooxygenases in the same EC subclass. Distinguishing the 4th digit (specific substrate/reaction: sterol 14α-demethylase vs. another P450 reaction) from sequence alone requires knowing which specific substrate this enzyme acts upon.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific substrate identity (14α-methyl sterol demethylation vs. whatever reaction EC 1.14.14.104 catalyzes) is an item-specific annotation fact. While one might weakly argue that fungal P450s are commonly CYP51, this is a statistical prior, not a deterministic sequence-based argument. The 4th EC digit for P450s encodes the specific substrate, which cannot be reliably deduced from general sequence features without database lookup.",
    "reason": "The question reduces to identifying the correct 4th-digit EC number among two P450 monooxygenase options. Sequence features (heme-binding motif, ~540 AA length, overall P450 fold) establish the 1.14.14 class but cannot distinguish between two specific P450 reactions. Selecting 154 over 104 requires either recognizing the exact sequence as CYP51 from memorization or accessing the UniProt annotation—both are lookup-dependent operations rather than general biological reasoning."
  },
  "case_id": "EC_number_0175",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C9",
      "C13",
      "H1",
      "H2",
      "H4",
      "H8",
      "H12"
    ],
    "judgment": "supported",
    "reason": "UniProt entry P0DXV0 (LAN1_PYRDE) is annotated with EC 1.14.14.154 (Sterol 14-alpha demethylase), with evidence code ECO:0000305 (inferred from direct assay) linked to PubMed:33857369 (Liu et al., 2021). The benchmark sequence matches the source sequence exactly (540 AA, SHA256 confirmed). Multiple catalytic activity reactions confirm 14α-demethylation of sterols (lanosterol, eburicol, generic 14α-methyl steroids) with NADPH-hemoprotein reductase and O2, consistent with EC 1.14.14.154."
  },
  "important_caveats": [
    "The EC 1.14.14.154 annotation carries evidence code ECO:0000305 (inferred from direct assay), indicating experimental support from PubMed:33857369, not merely computational prediction.",
    "The entry was first published 2025-02-05, making it a relatively recent annotation; the benchmark author's source snapshot is unknown.",
    "EC 1.14.14.104's specific identity was not independently verified in the supplied evidence; its plausibility as a P450 distractor is assumed from the EC numbering scheme.",
    "The sequence is from a fungal organism (Pyrenophora dematioidea), which weakly supports CYP51 (essential for ergosterol biosynthesis) as the most common fungal P450, but this statistical argument does not definitively exclude EC 1.14.14.104."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "C"
    ],
    "reason": "Both A (1.14.14.104) and C (1.14.14.154) are P450 monooxygenase EC numbers. Without the specific substrate information or CYP51-specific active-site motif knowledge, a model cannot definitively distinguish between them from sequence alone. B and D are clearly eliminable (wrong EC class), but A vs C requires item-specific knowledge."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0175",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry P0DXV0 (LAN1_PYRDE) is annotated with EC 1.14.14.154 (Sterol 14-alpha demethylase), with evidence code ECO:0000305 (inferred from direct assay) linked to PubMed:33857369 (Liu et al., 2021). The benchmark sequence matches the source sequence exactly (540 AA, SHA256 confirmed). Multiple catalytic activity reactions confirm 14α-demethylation of sterols (lanosterol, eburicol, generic 14α-methyl steroids) with NADPH-hemoprotein reductase and O2, consistent with EC 1.14.14.154.",
    "evidence_ids": ["C1", "C4", "C5", "C9", "C13", "H1", "H2", "H4", "H8", "H12"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence contains a canonical P450 heme-binding motif (FGGGRHRCIGEKF with the conserved axial Cys), confirming membership in EC class 1.14.14 (P450 monooxygenases). This eliminates B (3.2.1.183, glycosidase) and D (5.2.1.8, isomerase) as they belong to entirely different EC classes. However, both A (1.14.14.104) and C (1.14.14.154) are P450 monooxygenases in the same EC subclass. Distinguishing the 4th digit (specific substrate/reaction: sterol 14α-demethylase vs. another P450 reaction) from sequence alone requires knowing which specific substrate this enzyme acts upon.",
    "missing_item_specific_fact": "The specific substrate identity (14α-methyl sterol demethylation vs. whatever reaction EC 1.14.14.104 catalyzes) is an item-specific annotation fact. While one might weakly argue that fungal P450s are commonly CYP51, this is a statistical prior, not a deterministic sequence-based argument. The 4th EC digit for P450s encodes the specific substrate, which cannot be reliably deduced from general sequence features without database lookup.",
    "reason": "The question reduces to identifying the correct 4th-digit EC number among two P450 monooxygenase options. Sequence features (heme-binding motif, ~540 AA length, overall P450 fold) establish the 1.14.14 class but cannot distinguish between two specific P450 reactions. Selecting 154 over 104 requires either recognizing the exact sequence as CYP51 from memorization or accessing the UniProt annotation—both are lookup-dependent operations rather than general biological reasoning."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "C"],
    "reason": "Both A (1.14.14.104) and C (1.14.14.154) are P450 monooxygenase EC numbers. Without the specific substrate information or CYP51-specific active-site motif knowledge, a model cannot definitively distinguish between them from sequence alone. B and D are clearly eliminable (wrong EC class), but A vs C requires item-specific knowledge."
  },
  "important_caveats": [
    "The EC 1.14.14.154 annotation carries evidence code ECO:0000305 (inferred from direct assay), indicating experimental support from PubMed:33857369, not merely computational prediction.",
    "The entry was first published 2025-02-05, making it a relatively recent annotation; the benchmark author's source snapshot is unknown.",
    "EC 1.14.14.104's specific identity was not independently verified in the supplied evidence; its plausibility as a P450 distractor is assumed from the EC numbering scheme.",
    "The sequence is from a fungal organism (Pyrenophora dematioidea), which weakly supports CYP51 (essential for ergosterol biosynthesis) as the most common fungal P450, but this statistical argument does not definitively exclude EC 1.14.14.104."
  ]
}
```

</details>

## After: GPT-6 Luna

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The supplied sequence exactly matches the reviewed UniProt sequence. That record assigns EC 1.14.14.154 to the protein as sterol 14-alpha demethylase (C4); its catalytic-activity annotation also gives this EC for sterol demethylation reactions, with evidence transferred from related proteins (C5, C9). This supports the key, while not constituting direct experimental evidence for this exact protein's activity.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C9](#evidence-c9).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is consistent with a fungal microsomal cytochrome P450: it has an N-terminal hydrophobic segment and the conserved C-terminal heme-thiolate region. More specifically, family-level recognition of CYP51 sterol 14-alpha-demethylases among P450 homologs provides a credible way to distinguish EC 1.14.14.154 (C) from the other P450 option, 1.14.14.104 (A); the glycosidase and isomerase options are still less consistent with the sequence.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A complete EC number is difficult to establish from generic P450 features alone, but the full sequence permits transferable family/homology inference toward CYP51, which meaningfully distinguishes the offered P450 alternatives without needing the exact protein's recorded annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The options name distinct enzyme classifications, and the sequence's likely CYP51 family assignment favors C rather than leaving an equally defensible alternative.


### Important caveats

- The reviewer-only database annotation is sequence-matched but partly based on transferred evidence from related proteins; it should not be described as direct experimental validation of this exact protein.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with a fungal microsomal cytochrome P450: it has an N-terminal hydrophobic segment and the conserved C-terminal heme-thiolate region. More specifically, family-level recognition of CYP51 sterol 14-alpha-demethylases among P450 homologs provides a credible way to distinguish EC 1.14.14.154 (C) from the other P450 option, 1.14.14.104 (A); the glycosidase and isomerase options are still less consistent with the sequence.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A complete EC number is difficult to establish from generic P450 features alone, but the full sequence permits transferable family/homology inference toward CYP51, which meaningfully distinguishes the offered P450 alternatives without needing the exact protein's recorded annotation."
  },
  "case_id": "EC_number_0175",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C9"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the reviewed UniProt sequence. That record assigns EC 1.14.14.154 to the protein as sterol 14-alpha demethylase (C4); its catalytic-activity annotation also gives this EC for sterol demethylation reactions, with evidence transferred from related proteins (C5, C9). This supports the key, while not constituting direct experimental evidence for this exact protein's activity."
  },
  "important_caveats": [
    "The reviewer-only database annotation is sequence-matched but partly based on transferred evidence from related proteins; it should not be described as direct experimental validation of this exact protein."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The options name distinct enzyme classifications, and the sequence's likely CYP51 family assignment favors C rather than leaving an equally defensible alternative."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0175",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the reviewed UniProt sequence. That record assigns EC 1.14.14.154 to the protein as sterol 14-alpha demethylase (C4); its catalytic-activity annotation also gives this EC for sterol demethylation reactions, with evidence transferred from related proteins (C5, C9). This supports the key, while not constituting direct experimental evidence for this exact protein's activity.",
    "evidence_ids": ["C4", "C5", "C9"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is consistent with a fungal microsomal cytochrome P450: it has an N-terminal hydrophobic segment and the conserved C-terminal heme-thiolate region. More specifically, family-level recognition of CYP51 sterol 14-alpha-demethylases among P450 homologs provides a credible way to distinguish EC 1.14.14.154 (C) from the other P450 option, 1.14.14.104 (A); the glycosidase and isomerase options are still less consistent with the sequence.",
    "missing_item_specific_fact": "",
    "reason": "A complete EC number is difficult to establish from generic P450 features alone, but the full sequence permits transferable family/homology inference toward CYP51, which meaningfully distinguishes the offered P450 alternatives without needing the exact protein's recorded annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The options name distinct enzyme classifications, and the sequence's likely CYP51 family assignment favors C rather than leaving an equally defensible alternative."
  },
  "important_caveats": [
    "The reviewer-only database annotation is sequence-matched but partly based on transferred evidence from related proteins; it should not be described as direct experimental validation of this exact protein."
  ]
}
```

</details>

## After: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry P0DXV0 (LAN1_PYRDE) from Pyrenophora dematioidea is annotated as Sterol 14-alpha demethylase with EC 1.14.14.154, confirmed by both the current entry (C4) and the archived flat-file record (H2). The catalytic activity reactions (C5-C16, H4-H15) describe the 14α-demethylation of lanosterol and eburicol, consistent with CYP51 function. The sequence match is confirmed (540 aa, SHA256 match). The evidence code ECO:0000305 (PubMed:33857369) indicates the EC assignment is supported by experimental literature.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C9](#evidence-c9), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains the canonical P450 heme-binding motif 'FGGGRHRCIG' (residues ~460-470), which unambiguously identifies this as a cytochrome P450 monooxygenase (EC class 1.14.14.x). This eliminates option B (3.2.1.183, a glycosidase/hydrolase) and option D (5.2.1.8, an isomerase) because these belong to entirely different EC classes (3 and 5) incompatible with a heme-containing monooxygenase. Between the two remaining P450 options (A: 1.14.14.104 and C: 1.14.14.154), the sequence exhibits CYP51/sterol 14α-demethylase family signatures: (1) the specific 'FGGGRHRCIG' pattern with the conserved I-helix threonine region upstream, (2) the hydrophobic N-terminal membrane-anchoring segment (~30 residues) typical of membrane-bound fungal CYP51, (3) the overall ~540 aa length consistent with fungal CYP51, and (4) the conserved substrate-binding pocket architecture. CYP51 is one of the most conserved P450 families across eukaryotes, and its sequence signature is well-characterized in the literature. EC 1.14.14.154 specifically denotes sterol 14α-demethylase (CYP51), while EC 1.14.14.104 does not correspond to a well-recognized P450 reaction in standard EC databases, making it a likely fabricated distractor. A knowledgeable model recognizing the CYP51 family pattern can reasonably assign 1.14.14.154.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The P450 heme-binding motif (FGGGRHRC) is directly readable from the sequence and eliminates non-P450 options. The CYP51 family-level features (specific heme-binding pattern, membrane anchor, length, conserved architecture) provide a transferable inference from knowledge of the highly conserved CYP51/sterol 14α-demethylase family to distinguish EC 1.14.14.154 from the other P450 option. The 4th-digit distinction is supported by family recognition and the likely invalidity of EC 1.14.14.104 as a recognized entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options B and D are clearly eliminated by the P450 heme-binding motif. Between A and C, the CYP51 family signatures in the sequence and the questionable validity of EC 1.14.14.104 as a recognized EC number provide sufficient basis to favor C without genuine ambiguity.


### Important caveats

- The specific assignment of the 4th EC digit (154 vs 104) relies on CYP51 family recognition; a model without detailed P450 family knowledge might struggle to distinguish the two 1.14.14.x options purely from sequence without database lookup.
- The UniProt annotation evidence code ECO:0000305 links the EC number to PubMed:33857369, indicating experimental literature support rather than purely computational inference.
- EC 1.14.14.104 could potentially be a valid but obscure EC number; its non-recognition as a standard entry strengthens the case for C but does not constitute absolute proof of invalidity.
- The protein is from a lanomycin biosynthetic gene cluster (a CYP51 inhibitor natural product), which is a specific biological context not derivable from sequence alone but does not affect the EC assignment.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains the canonical P450 heme-binding motif 'FGGGRHRCIG' (residues ~460-470), which unambiguously identifies this as a cytochrome P450 monooxygenase (EC class 1.14.14.x). This eliminates option B (3.2.1.183, a glycosidase/hydrolase) and option D (5.2.1.8, an isomerase) because these belong to entirely different EC classes (3 and 5) incompatible with a heme-containing monooxygenase. Between the two remaining P450 options (A: 1.14.14.104 and C: 1.14.14.154), the sequence exhibits CYP51/sterol 14α-demethylase family signatures: (1) the specific 'FGGGRHRCIG' pattern with the conserved I-helix threonine region upstream, (2) the hydrophobic N-terminal membrane-anchoring segment (~30 residues) typical of membrane-bound fungal CYP51, (3) the overall ~540 aa length consistent with fungal CYP51, and (4) the conserved substrate-binding pocket architecture. CYP51 is one of the most conserved P450 families across eukaryotes, and its sequence signature is well-characterized in the literature. EC 1.14.14.154 specifically denotes sterol 14α-demethylase (CYP51), while EC 1.14.14.104 does not correspond to a well-recognized P450 reaction in standard EC databases, making it a likely fabricated distractor. A knowledgeable model recognizing the CYP51 family pattern can reasonably assign 1.14.14.154.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The P450 heme-binding motif (FGGGRHRC) is directly readable from the sequence and eliminates non-P450 options. The CYP51 family-level features (specific heme-binding pattern, membrane anchor, length, conserved architecture) provide a transferable inference from knowledge of the highly conserved CYP51/sterol 14α-demethylase family to distinguish EC 1.14.14.154 from the other P450 option. The 4th-digit distinction is supported by family recognition and the likely invalidity of EC 1.14.14.104 as a recognized entry."
  },
  "case_id": "EC_number_0175",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C9",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry P0DXV0 (LAN1_PYRDE) from Pyrenophora dematioidea is annotated as Sterol 14-alpha demethylase with EC 1.14.14.154, confirmed by both the current entry (C4) and the archived flat-file record (H2). The catalytic activity reactions (C5-C16, H4-H15) describe the 14α-demethylation of lanosterol and eburicol, consistent with CYP51 function. The sequence match is confirmed (540 aa, SHA256 match). The evidence code ECO:0000305 (PubMed:33857369) indicates the EC assignment is supported by experimental literature."
  },
  "important_caveats": [
    "The specific assignment of the 4th EC digit (154 vs 104) relies on CYP51 family recognition; a model without detailed P450 family knowledge might struggle to distinguish the two 1.14.14.x options purely from sequence without database lookup.",
    "The UniProt annotation evidence code ECO:0000305 links the EC number to PubMed:33857369, indicating experimental literature support rather than purely computational inference.",
    "EC 1.14.14.104 could potentially be a valid but obscure EC number; its non-recognition as a standard entry strengthens the case for C but does not constitute absolute proof of invalidity.",
    "The protein is from a lanomycin biosynthetic gene cluster (a CYP51 inhibitor natural product), which is a specific biological context not derivable from sequence alone but does not affect the EC assignment."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options B and D are clearly eliminated by the P450 heme-binding motif. Between A and C, the CYP51 family signatures in the sequence and the questionable validity of EC 1.14.14.104 as a recognized EC number provide sufficient basis to favor C without genuine ambiguity."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0175",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry P0DXV0 (LAN1_PYRDE) from Pyrenophora dematioidea is annotated as Sterol 14-alpha demethylase with EC 1.14.14.154, confirmed by both the current entry (C4) and the archived flat-file record (H2). The catalytic activity reactions (C5-C16, H4-H15) describe the 14α-demethylation of lanosterol and eburicol, consistent with CYP51 function. The sequence match is confirmed (540 aa, SHA256 match). The evidence code ECO:0000305 (PubMed:33857369) indicates the EC assignment is supported by experimental literature.",
    "evidence_ids": ["C4", "C5", "C9", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains the canonical P450 heme-binding motif 'FGGGRHRCIG' (residues ~460-470), which unambiguously identifies this as a cytochrome P450 monooxygenase (EC class 1.14.14.x). This eliminates option B (3.2.1.183, a glycosidase/hydrolase) and option D (5.2.1.8, an isomerase) because these belong to entirely different EC classes (3 and 5) incompatible with a heme-containing monooxygenase. Between the two remaining P450 options (A: 1.14.14.104 and C: 1.14.14.154), the sequence exhibits CYP51/sterol 14α-demethylase family signatures: (1) the specific 'FGGGRHRCIG' pattern with the conserved I-helix threonine region upstream, (2) the hydrophobic N-terminal membrane-anchoring segment (~30 residues) typical of membrane-bound fungal CYP51, (3) the overall ~540 aa length consistent with fungal CYP51, and (4) the conserved substrate-binding pocket architecture. CYP51 is one of the most conserved P450 families across eukaryotes, and its sequence signature is well-characterized in the literature. EC 1.14.14.154 specifically denotes sterol 14α-demethylase (CYP51), while EC 1.14.14.104 does not correspond to a well-recognized P450 reaction in standard EC databases, making it a likely fabricated distractor. A knowledgeable model recognizing the CYP51 family pattern can reasonably assign 1.14.14.154.",
    "missing_item_specific_fact": "",
    "reason": "The P450 heme-binding motif (FGGGRHRC) is directly readable from the sequence and eliminates non-P450 options. The CYP51 family-level features (specific heme-binding pattern, membrane anchor, length, conserved architecture) provide a transferable inference from knowledge of the highly conserved CYP51/sterol 14α-demethylase family to distinguish EC 1.14.14.154 from the other P450 option. The 4th-digit distinction is supported by family recognition and the likely invalidity of EC 1.14.14.104 as a recognized entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options B and D are clearly eliminated by the P450 heme-binding motif. Between A and C, the CYP51 family signatures in the sequence and the questionable validity of EC 1.14.14.104 as a recognized EC number provide sufficient basis to favor C without genuine ambiguity."
  },
  "important_caveats": [
    "The specific assignment of the 4th EC digit (154 vs 104) relies on CYP51 family recognition; a model without detailed P450 family knowledge might struggle to distinguish the two 1.14.14.x options purely from sequence without database lookup.",
    "The UniProt annotation evidence code ECO:0000305 links the EC number to PubMed:33857369, indicating experimental literature support rather than purely computational inference.",
    "EC 1.14.14.104 could potentially be a valid but obscure EC number; its non-recognition as a standard entry strengthens the case for C but does not constitute absolute proof of invalidity.",
    "The protein is from a lanomycin biosynthetic gene cluster (a CYP51 inhibitor natural product), which is a specific biological context not derivable from sequence alone but does not affect the EC assignment."
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
  "requested_accession": "P0DXV0",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "benchmark_sequence_sha256": "7892b58432fcc729eff0e7866dfac47e6055a778388a0efd41daa5ff7eb4bdd5",
  "benchmark_sequence_length": 540,
  "current_status": "retrieved",
  "current_sequence_comparison": "matched",
  "current_entry_audit": {
    "entryVersion": 6,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2025-02-05",
    "sequenceVersion": 1
  },
  "current_uniprot_release": "2026_03",
  "current_record_sha256": "2b160263904b8131f1c8a75b02b0f4aff9b666aad2d76208024c4b4be635743d",
  "current_source_sequence_sha256": "7892b58432fcc729eff0e7866dfac47e6055a778388a0efd41daa5ff7eb4bdd5",
  "current_source_sequence_length": 540,
  "historical_status": "retrieved",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "selected_historical_entry_version": 4,
  "selected_historical_version": {
    "accession": "P0DXV0",
    "database": "Swiss-Prot",
    "entryVersion": 4,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "LAN1_PYRDE",
    "sequenceVersion": 1
  },
  "selected_historical_record_sha256": "e154cd9089aa6b8a42d60528a7ce84bec0c5a19fc8f6e92dd2125bb46b055be2",
  "selected_historical_source_sequence_sha256": "7892b58432fcc729eff0e7866dfac47e6055a778388a0efd41daa5ff7eb4bdd5",
  "selected_historical_source_sequence_length": 540,
  "latest_at_cutoff_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 4,
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXV0.json)

```json
{
  "evidence_id": "C1",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXV0.json",
  "source_sha256": "2b160263904b8131f1c8a75b02b0f4aff9b666aad2d76208024c4b4be635743d",
  "retrieved_utc": "2026-11-02T04:29:42.875207+00:00",
  "json_pointer": "/primaryAccession",
  "excerpt": "\"P0DXV0\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXV0.json)

```json
{
  "evidence_id": "C2",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXV0.json",
  "source_sha256": "2b160263904b8131f1c8a75b02b0f4aff9b666aad2d76208024c4b4be635743d",
  "retrieved_utc": "2026-11-02T04:29:42.875207+00:00",
  "json_pointer": "/entryAudit",
  "excerpt": "{\"entryVersion\":6,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2025-02-05\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXV0.json)

```json
{
  "evidence_id": "C3",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXV0.json",
  "source_sha256": "2b160263904b8131f1c8a75b02b0f4aff9b666aad2d76208024c4b4be635743d",
  "retrieved_utc": "2026-11-02T04:29:42.875207+00:00",
  "json_pointer": "/organism",
  "excerpt": "{\"commonName\":\"Helminthosporium dematioideum\",\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Dothideomycetes\",\"Pleosporomycetidae\",\"Pleosporales\",\"Pleosporineae\",\"Pleosporaceae\",\"Pyrenophora\"],\"scientificName\":\"Pyrenophora dematioidea\",\"taxonId\":139229}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXV0.json)

```json
{
  "evidence_id": "C4",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXV0.json",
  "source_sha256": "2b160263904b8131f1c8a75b02b0f4aff9b666aad2d76208024c4b4be635743d",
  "retrieved_utc": "2026-11-02T04:29:42.875207+00:00",
  "json_pointer": "/proteinDescription",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"33857369\",\"source\":\"PubMed\"}],\"value\":\"Cytochrome P450 monooxygenase\"}},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"33857369\",\"source\":\"PubMed\"}],\"value\":\"Ergosterol biosynthesis protein\"}},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"33857369\",\"source\":\"PubMed\"}],\"value\":\"Lanomycin biosynthesis cluster protein 1\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"33857369\",\"source\":\"PubMed\"}],\"value\":\"1.14.14.154\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"33857369\",\"source\":\"PubMed\"}],\"value\":\"Sterol 14-alpha demethylase\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXV0.json)

```json
{
  "evidence_id": "C5",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXV0.json",
  "source_sha256": "2b160263904b8131f1c8a75b02b0f4aff9b666aad2d76208024c4b4be635743d",
  "retrieved_utc": "2026-11-02T04:29:42.875207+00:00",
  "json_pointer": "/comments/1",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q4WNT5\",\"source\":\"UniProtKB\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:54029\"}}],\"reaction\":{\"ecNumber\":\"1.14.14.154\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q4WNT5\",\"source\":\"UniProtKB\"}],\"name\":\"a 14alpha-methyl steroid + 3 reduced [NADPH--hemoprotein reductase] + 3 O2 = a Delta(14) steroid + formate + 3 oxidized [NADPH--hemoprotein reductase] + 4 H2O + 4 H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:54028\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:11964\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:11965\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15379\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15740\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57618\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:58210\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:138029\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:138031\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXV0.json)

```json
{
  "evidence_id": "C6",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXV0.json",
  "source_sha256": "2b160263904b8131f1c8a75b02b0f4aff9b666aad2d76208024c4b4be635743d",
  "retrieved_utc": "2026-11-02T04:29:42.875207+00:00",
  "json_pointer": "/comments/2",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P10614\",\"source\":\"UniProtKB\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:68061\"}}],\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P10614\",\"source\":\"UniProtKB\"}],\"name\":\"a 14alpha-methyl steroid + reduced [NADPH--hemoprotein reductase] + O2 = a 14alpha-hydroxymethyl steroid + oxidized [NADPH--hemoprotein reductase] + H2O + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:68060\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:11964\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:11965\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15379\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57618\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:58210\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:138029\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:176901\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXV0.json)

```json
{
  "evidence_id": "C7",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXV0.json",
  "source_sha256": "2b160263904b8131f1c8a75b02b0f4aff9b666aad2d76208024c4b4be635743d",
  "retrieved_utc": "2026-11-02T04:29:42.875207+00:00",
  "json_pointer": "/comments/3",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P10614\",\"source\":\"UniProtKB\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:68065\"}}],\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P10614\",\"source\":\"UniProtKB\"}],\"name\":\"a 14alpha-hydroxymethyl steroid + reduced [NADPH--hemoprotein reductase] + O2 = a 14alpha-formyl steroid + oxidized [NADPH--hemoprotein reductase] + 2 H2O + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:68064\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:11964\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:11965\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15379\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57618\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:58210\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:176901\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:176902\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXV0.json)

```json
{
  "evidence_id": "C8",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXV0.json",
  "source_sha256": "2b160263904b8131f1c8a75b02b0f4aff9b666aad2d76208024c4b4be635743d",
  "retrieved_utc": "2026-11-02T04:29:42.875207+00:00",
  "json_pointer": "/comments/4",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P10614\",\"source\":\"UniProtKB\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:68069\"}}],\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P10614\",\"source\":\"UniProtKB\"}],\"name\":\"a 14alpha-formyl steroid + reduced [NADPH--hemoprotein reductase] + O2 = a Delta(14) steroid + formate + oxidized [NADPH--hemoprotein reductase] + H2O + 2 H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:68068\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:11964\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:11965\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15379\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15740\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57618\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:58210\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:138031\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:176902\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXV0.json)

```json
{
  "evidence_id": "C9",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXV0.json",
  "source_sha256": "2b160263904b8131f1c8a75b02b0f4aff9b666aad2d76208024c4b4be635743d",
  "retrieved_utc": "2026-11-02T04:29:42.875207+00:00",
  "json_pointer": "/comments/5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q4WNT5\",\"source\":\"UniProtKB\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:25287\"}}],\"reaction\":{\"ecNumber\":\"1.14.14.154\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q4WNT5\",\"source\":\"UniProtKB\"}],\"name\":\"lanosterol + 3 reduced [NADPH--hemoprotein reductase] + 3 O2 = 4,4-dimethyl-5alpha-cholesta-8,14,24-trien-3beta-ol + formate + 3 oxidized [NADPH--hemoprotein reductase] + 4 H2O + 4 H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:25286\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:11964\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:11965\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15379\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15740\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:16521\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:17813\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57618\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:58210\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXV0.json)

```json
{
  "evidence_id": "C10",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXV0.json",
  "source_sha256": "2b160263904b8131f1c8a75b02b0f4aff9b666aad2d76208024c4b4be635743d",
  "retrieved_utc": "2026-11-02T04:29:42.875207+00:00",
  "json_pointer": "/comments/6",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P10614\",\"source\":\"UniProtKB\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:75104\"}}],\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P10614\",\"source\":\"UniProtKB\"}],\"name\":\"lanosterol + reduced [NADPH--hemoprotein reductase] + O2 = 32-hydroxylanosterol + oxidized [NADPH--hemoprotein reductase] + H2O + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:75103\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:11964\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:11965\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15379\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:16521\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57618\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:58210\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:166806\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXV0.json)

```json
{
  "evidence_id": "C11",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXV0.json",
  "source_sha256": "2b160263904b8131f1c8a75b02b0f4aff9b666aad2d76208024c4b4be635743d",
  "retrieved_utc": "2026-11-02T04:29:42.875207+00:00",
  "json_pointer": "/comments/7",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P10614\",\"source\":\"UniProtKB\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:75108\"}}],\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P10614\",\"source\":\"UniProtKB\"}],\"name\":\"32-hydroxylanosterol + reduced [NADPH--hemoprotein reductase] + O2 = 32-oxolanosterol + oxidized [NADPH--hemoprotein reductase] + 2 H2O + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:75107\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:11964\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:11965\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15379\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57618\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:58210\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:166681\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:166806\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXV0.json)

```json
{
  "evidence_id": "C12",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXV0.json",
  "source_sha256": "2b160263904b8131f1c8a75b02b0f4aff9b666aad2d76208024c4b4be635743d",
  "retrieved_utc": "2026-11-02T04:29:42.875207+00:00",
  "json_pointer": "/comments/8",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P10614\",\"source\":\"UniProtKB\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:75112\"}}],\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P10614\",\"source\":\"UniProtKB\"}],\"name\":\"32-oxolanosterol + reduced [NADPH--hemoprotein reductase] + O2 = 4,4-dimethyl-5alpha-cholesta-8,14,24-trien-3beta-ol + formate + oxidized [NADPH--hemoprotein reductase] + H2O + 2 H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:75111\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:11964\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:11965\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15379\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15740\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:17813\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57618\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:58210\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:166681\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C13

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXV0.json)

```json
{
  "evidence_id": "C13",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXV0.json",
  "source_sha256": "2b160263904b8131f1c8a75b02b0f4aff9b666aad2d76208024c4b4be635743d",
  "retrieved_utc": "2026-11-02T04:29:42.875207+00:00",
  "json_pointer": "/comments/9",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q4WNT5\",\"source\":\"UniProtKB\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:75440\"}}],\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q4WNT5\",\"source\":\"UniProtKB\"}],\"name\":\"eburicol + 3 reduced [NADPH--hemoprotein reductase] + 3 O2 = 14-demethyleburicol + formate + 3 oxidized [NADPH--hemoprotein reductase] + 4 H2O + 4 H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:75439\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:11964\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:11965\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15379\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15740\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57618\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:58210\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:70315\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:194330\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C14

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXV0.json)

```json
{
  "evidence_id": "C14",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXV0.json",
  "source_sha256": "2b160263904b8131f1c8a75b02b0f4aff9b666aad2d76208024c4b4be635743d",
  "retrieved_utc": "2026-11-02T04:29:42.875207+00:00",
  "json_pointer": "/comments/10",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P10614\",\"source\":\"UniProtKB\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:75428\"}}],\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P10614\",\"source\":\"UniProtKB\"}],\"name\":\"eburicol + reduced [NADPH--hemoprotein reductase] + O2 = 32-hydroxyeburicol + oxidized [NADPH--hemoprotein reductase] + H2O + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:75427\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:11964\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:11965\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15379\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57618\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:58210\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:70315\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:194328\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C15

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXV0.json)

```json
{
  "evidence_id": "C15",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXV0.json",
  "source_sha256": "2b160263904b8131f1c8a75b02b0f4aff9b666aad2d76208024c4b4be635743d",
  "retrieved_utc": "2026-11-02T04:29:42.875207+00:00",
  "json_pointer": "/comments/11",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P10614\",\"source\":\"UniProtKB\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:75432\"}}],\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P10614\",\"source\":\"UniProtKB\"}],\"name\":\"32-hydroxyeburicol + reduced [NADPH--hemoprotein reductase] + O2 = 32-oxoeburicol + oxidized [NADPH--hemoprotein reductase] + 2 H2O + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:75431\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:11964\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:11965\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15379\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57618\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:58210\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:194328\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:194329\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C16

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXV0.json)

```json
{
  "evidence_id": "C16",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXV0.json",
  "source_sha256": "2b160263904b8131f1c8a75b02b0f4aff9b666aad2d76208024c4b4be635743d",
  "retrieved_utc": "2026-11-02T04:29:42.875207+00:00",
  "json_pointer": "/comments/12",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P10614\",\"source\":\"UniProtKB\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:75436\"}}],\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P10614\",\"source\":\"UniProtKB\"}],\"name\":\"32-oxoeburicol + reduced [NADPH--hemoprotein reductase] + O2 = 14-demethyleburicol + formate + oxidized [NADPH--hemoprotein reductase] + H2O + 2 H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:75435\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:11964\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:11965\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15379\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15740\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57618\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:58210\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:194329\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:194330\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C17

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXV0.json)

```json
{
  "evidence_id": "C17",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXV0.json",
  "source_sha256": "2b160263904b8131f1c8a75b02b0f4aff9b666aad2d76208024c4b4be635743d",
  "retrieved_utc": "2026-11-02T04:29:42.875207+00:00",
  "json_pointer": "/references/0",
  "excerpt": "{\"citation\":{\"authors\":[\"Liu N.\",\"Abramyan E.D.\",\"Cheng W.\",\"Perlatti B.\",\"Harvey C.J.B.\",\"Bills G.F.\",\"Tang Y.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"33857369\"},{\"database\":\"DOI\",\"id\":\"10.1021/jacs.1c01516\"}],\"citationType\":\"journal article\",\"firstPage\":\"6043\",\"id\":\"33857369\",\"journal\":\"J. Am. Chem. Soc.\",\"lastPage\":\"6047\",\"publicationDate\":\"2021\",\"title\":\"Targeted genome mining reveals the biosynthetic gene clusters of natural product CYP51 inhibitors.\",\"volume\":\"143\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"TTI-1096\"}],\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [GENOMIC DNA]\",\"FUNCTION\",\"PATHWAY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXV0?format=txt&versions=4)

```json
{
  "evidence_id": "H1",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/P0DXV0?format=txt&versions=4",
  "source_sha256": "e154cd9089aa6b8a42d60528a7ce84bec0c5a19fc8f6e92dd2125bb46b055be2",
  "retrieved_utc": "2026-11-02T04:29:45.056058+00:00",
  "source_locator": "lines 1-16",
  "excerpt": "ID   LAN1_PYRDE              Reviewed;         540 AA.\nAC   P0DXV0;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   05-FEB-2025, sequence version 1.\nDT   28-JAN-2026, entry version 4.\nDE   RecName: Full=Sterol 14-alpha demethylase {ECO:0000303|PubMed:33857369};\nDE            EC=1.14.14.154 {ECO:0000305|PubMed:33857369};\nDE   AltName: Full=Cytochrome P450 monooxygenase {ECO:0000303|PubMed:33857369};\nDE   AltName: Full=Ergosterol biosynthesis protein {ECO:0000303|PubMed:33857369};\nDE   AltName: Full=Lanomycin biosynthesis cluster protein 1 {ECO:0000303|PubMed:33857369};\nGN   Name=ORF1 {ECO:0000303|PubMed:33857369};\nOS   Pyrenophora dematioidea (Helminthosporium dematioideum).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Dothideomycetes;\nOC   Pleosporomycetidae; Pleosporales; Pleosporineae; Pleosporaceae;\nOC   Pyrenophora.\nOX   NCBI_TaxID=139229;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 4,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXV0?format=txt&versions=4)

```json
{
  "evidence_id": "H2",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/P0DXV0?format=txt&versions=4",
  "source_sha256": "e154cd9089aa6b8a42d60528a7ce84bec0c5a19fc8f6e92dd2125bb46b055be2",
  "retrieved_utc": "2026-11-02T04:29:45.056058+00:00",
  "source_locator": "lines 6-10",
  "excerpt": "DE   RecName: Full=Sterol 14-alpha demethylase {ECO:0000303|PubMed:33857369};\nDE            EC=1.14.14.154 {ECO:0000305|PubMed:33857369};\nDE   AltName: Full=Cytochrome P450 monooxygenase {ECO:0000303|PubMed:33857369};\nDE   AltName: Full=Ergosterol biosynthesis protein {ECO:0000303|PubMed:33857369};\nDE   AltName: Full=Lanomycin biosynthesis cluster protein 1 {ECO:0000303|PubMed:33857369};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 4,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXV0?format=txt&versions=4)

```json
{
  "evidence_id": "H3",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/P0DXV0?format=txt&versions=4",
  "source_sha256": "e154cd9089aa6b8a42d60528a7ce84bec0c5a19fc8f6e92dd2125bb46b055be2",
  "retrieved_utc": "2026-11-02T04:29:45.056058+00:00",
  "source_locator": "lines 17-25",
  "excerpt": "RN   [1]\nRP   NUCLEOTIDE SEQUENCE [GENOMIC DNA], FUNCTION, AND PATHWAY.\nRC   STRAIN=TTI-1096;\nRX   PubMed=33857369; DOI=10.1021/jacs.1c01516;\nRA   Liu N., Abramyan E.D., Cheng W., Perlatti B., Harvey C.J.B., Bills G.F.,\nRA   Tang Y.;\nRT   \"Targeted genome mining reveals the biosynthetic gene clusters of natural\nRT   product CYP51 inhibitors.\";\nRL   J. Am. Chem. Soc. 143:6043-6047(2021).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 4,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXV0?format=txt&versions=4)

```json
{
  "evidence_id": "H4",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/P0DXV0?format=txt&versions=4",
  "source_sha256": "e154cd9089aa6b8a42d60528a7ce84bec0c5a19fc8f6e92dd2125bb46b055be2",
  "retrieved_utc": "2026-11-02T04:29:45.056058+00:00",
  "source_locator": "lines 36-46",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=a 14alpha-methyl steroid + 3 reduced [NADPH--hemoprotein\nCC         reductase] + 3 O2 = a Delta(14) steroid + formate + 3 oxidized\nCC         [NADPH--hemoprotein reductase] + 4 H2O + 4 H(+);\nCC         Xref=Rhea:RHEA:54028, Rhea:RHEA-COMP:11964, Rhea:RHEA-COMP:11965,\nCC         ChEBI:CHEBI:15377, ChEBI:CHEBI:15378, ChEBI:CHEBI:15379,\nCC         ChEBI:CHEBI:15740, ChEBI:CHEBI:57618, ChEBI:CHEBI:58210,\nCC         ChEBI:CHEBI:138029, ChEBI:CHEBI:138031; EC=1.14.14.154;\nCC         Evidence={ECO:0000250|UniProtKB:Q4WNT5};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:54029;\nCC         Evidence={ECO:0000250|UniProtKB:Q4WNT5};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 4,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXV0?format=txt&versions=4)

```json
{
  "evidence_id": "H5",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/P0DXV0?format=txt&versions=4",
  "source_sha256": "e154cd9089aa6b8a42d60528a7ce84bec0c5a19fc8f6e92dd2125bb46b055be2",
  "retrieved_utc": "2026-11-02T04:29:45.056058+00:00",
  "source_locator": "lines 47-56",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=a 14alpha-methyl steroid + reduced [NADPH--hemoprotein\nCC         reductase] + O2 = a 14alpha-hydroxymethyl steroid + oxidized [NADPH--\nCC         hemoprotein reductase] + H2O + H(+); Xref=Rhea:RHEA:68060, Rhea:RHEA-\nCC         COMP:11964, Rhea:RHEA-COMP:11965, ChEBI:CHEBI:15377,\nCC         ChEBI:CHEBI:15378, ChEBI:CHEBI:15379, ChEBI:CHEBI:57618,\nCC         ChEBI:CHEBI:58210, ChEBI:CHEBI:138029, ChEBI:CHEBI:176901;\nCC         Evidence={ECO:0000250|UniProtKB:P10614};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:68061;\nCC         Evidence={ECO:0000250|UniProtKB:P10614};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 4,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXV0?format=txt&versions=4)

```json
{
  "evidence_id": "H6",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/P0DXV0?format=txt&versions=4",
  "source_sha256": "e154cd9089aa6b8a42d60528a7ce84bec0c5a19fc8f6e92dd2125bb46b055be2",
  "retrieved_utc": "2026-11-02T04:29:45.056058+00:00",
  "source_locator": "lines 57-66",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=a 14alpha-hydroxymethyl steroid + reduced [NADPH--hemoprotein\nCC         reductase] + O2 = a 14alpha-formyl steroid + oxidized [NADPH--\nCC         hemoprotein reductase] + 2 H2O + H(+); Xref=Rhea:RHEA:68064,\nCC         Rhea:RHEA-COMP:11964, Rhea:RHEA-COMP:11965, ChEBI:CHEBI:15377,\nCC         ChEBI:CHEBI:15378, ChEBI:CHEBI:15379, ChEBI:CHEBI:57618,\nCC         ChEBI:CHEBI:58210, ChEBI:CHEBI:176901, ChEBI:CHEBI:176902;\nCC         Evidence={ECO:0000250|UniProtKB:P10614};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:68065;\nCC         Evidence={ECO:0000250|UniProtKB:P10614};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 4,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXV0?format=txt&versions=4)

```json
{
  "evidence_id": "H7",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/P0DXV0?format=txt&versions=4",
  "source_sha256": "e154cd9089aa6b8a42d60528a7ce84bec0c5a19fc8f6e92dd2125bb46b055be2",
  "retrieved_utc": "2026-11-02T04:29:45.056058+00:00",
  "source_locator": "lines 67-76",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=a 14alpha-formyl steroid + reduced [NADPH--hemoprotein\nCC         reductase] + O2 = a Delta(14) steroid + formate + oxidized [NADPH--\nCC         hemoprotein reductase] + H2O + 2 H(+); Xref=Rhea:RHEA:68068,\nCC         Rhea:RHEA-COMP:11964, Rhea:RHEA-COMP:11965, ChEBI:CHEBI:15377,\nCC         ChEBI:CHEBI:15378, ChEBI:CHEBI:15379, ChEBI:CHEBI:15740,\nCC         ChEBI:CHEBI:57618, ChEBI:CHEBI:58210, ChEBI:CHEBI:138031,\nCC         ChEBI:CHEBI:176902; Evidence={ECO:0000250|UniProtKB:P10614};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:68069;\nCC         Evidence={ECO:0000250|UniProtKB:P10614};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 4,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXV0?format=txt&versions=4)

```json
{
  "evidence_id": "H8",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/P0DXV0?format=txt&versions=4",
  "source_sha256": "e154cd9089aa6b8a42d60528a7ce84bec0c5a19fc8f6e92dd2125bb46b055be2",
  "retrieved_utc": "2026-11-02T04:29:45.056058+00:00",
  "source_locator": "lines 77-87",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=lanosterol + 3 reduced [NADPH--hemoprotein reductase] + 3 O2 =\nCC         4,4-dimethyl-5alpha-cholesta-8,14,24-trien-3beta-ol + formate + 3\nCC         oxidized [NADPH--hemoprotein reductase] + 4 H2O + 4 H(+);\nCC         Xref=Rhea:RHEA:25286, Rhea:RHEA-COMP:11964, Rhea:RHEA-COMP:11965,\nCC         ChEBI:CHEBI:15377, ChEBI:CHEBI:15378, ChEBI:CHEBI:15379,\nCC         ChEBI:CHEBI:15740, ChEBI:CHEBI:16521, ChEBI:CHEBI:17813,\nCC         ChEBI:CHEBI:57618, ChEBI:CHEBI:58210; EC=1.14.14.154;\nCC         Evidence={ECO:0000250|UniProtKB:Q4WNT5};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:25287;\nCC         Evidence={ECO:0000250|UniProtKB:Q4WNT5};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 4,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXV0?format=txt&versions=4)

```json
{
  "evidence_id": "H9",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/P0DXV0?format=txt&versions=4",
  "source_sha256": "e154cd9089aa6b8a42d60528a7ce84bec0c5a19fc8f6e92dd2125bb46b055be2",
  "retrieved_utc": "2026-11-02T04:29:45.056058+00:00",
  "source_locator": "lines 88-96",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=lanosterol + reduced [NADPH--hemoprotein reductase] + O2 = 32-\nCC         hydroxylanosterol + oxidized [NADPH--hemoprotein reductase] + H2O +\nCC         H(+); Xref=Rhea:RHEA:75103, Rhea:RHEA-COMP:11964, Rhea:RHEA-\nCC         COMP:11965, ChEBI:CHEBI:15377, ChEBI:CHEBI:15378, ChEBI:CHEBI:15379,\nCC         ChEBI:CHEBI:16521, ChEBI:CHEBI:57618, ChEBI:CHEBI:58210,\nCC         ChEBI:CHEBI:166806; Evidence={ECO:0000250|UniProtKB:P10614};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:75104;\nCC         Evidence={ECO:0000250|UniProtKB:P10614};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 4,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H10

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXV0?format=txt&versions=4)

```json
{
  "evidence_id": "H10",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/P0DXV0?format=txt&versions=4",
  "source_sha256": "e154cd9089aa6b8a42d60528a7ce84bec0c5a19fc8f6e92dd2125bb46b055be2",
  "retrieved_utc": "2026-11-02T04:29:45.056058+00:00",
  "source_locator": "lines 97-105",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=32-hydroxylanosterol + reduced [NADPH--hemoprotein reductase]\nCC         + O2 = 32-oxolanosterol + oxidized [NADPH--hemoprotein reductase] + 2\nCC         H2O + H(+); Xref=Rhea:RHEA:75107, Rhea:RHEA-COMP:11964, Rhea:RHEA-\nCC         COMP:11965, ChEBI:CHEBI:15377, ChEBI:CHEBI:15378, ChEBI:CHEBI:15379,\nCC         ChEBI:CHEBI:57618, ChEBI:CHEBI:58210, ChEBI:CHEBI:166681,\nCC         ChEBI:CHEBI:166806; Evidence={ECO:0000250|UniProtKB:P10614};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:75108;\nCC         Evidence={ECO:0000250|UniProtKB:P10614};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 4,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H11

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXV0?format=txt&versions=4)

```json
{
  "evidence_id": "H11",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/P0DXV0?format=txt&versions=4",
  "source_sha256": "e154cd9089aa6b8a42d60528a7ce84bec0c5a19fc8f6e92dd2125bb46b055be2",
  "retrieved_utc": "2026-11-02T04:29:45.056058+00:00",
  "source_locator": "lines 106-116",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=32-oxolanosterol + reduced [NADPH--hemoprotein reductase] + O2\nCC         = 4,4-dimethyl-5alpha-cholesta-8,14,24-trien-3beta-ol + formate +\nCC         oxidized [NADPH--hemoprotein reductase] + H2O + 2 H(+);\nCC         Xref=Rhea:RHEA:75111, Rhea:RHEA-COMP:11964, Rhea:RHEA-COMP:11965,\nCC         ChEBI:CHEBI:15377, ChEBI:CHEBI:15378, ChEBI:CHEBI:15379,\nCC         ChEBI:CHEBI:15740, ChEBI:CHEBI:17813, ChEBI:CHEBI:57618,\nCC         ChEBI:CHEBI:58210, ChEBI:CHEBI:166681;\nCC         Evidence={ECO:0000250|UniProtKB:P10614};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:75112;\nCC         Evidence={ECO:0000250|UniProtKB:P10614};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 4,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H12

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXV0?format=txt&versions=4)

```json
{
  "evidence_id": "H12",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/P0DXV0?format=txt&versions=4",
  "source_sha256": "e154cd9089aa6b8a42d60528a7ce84bec0c5a19fc8f6e92dd2125bb46b055be2",
  "retrieved_utc": "2026-11-02T04:29:45.056058+00:00",
  "source_locator": "lines 117-126",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=eburicol + 3 reduced [NADPH--hemoprotein reductase] + 3 O2 =\nCC         14-demethyleburicol + formate + 3 oxidized [NADPH--hemoprotein\nCC         reductase] + 4 H2O + 4 H(+); Xref=Rhea:RHEA:75439, Rhea:RHEA-\nCC         COMP:11964, Rhea:RHEA-COMP:11965, ChEBI:CHEBI:15377,\nCC         ChEBI:CHEBI:15378, ChEBI:CHEBI:15379, ChEBI:CHEBI:15740,\nCC         ChEBI:CHEBI:57618, ChEBI:CHEBI:58210, ChEBI:CHEBI:70315,\nCC         ChEBI:CHEBI:194330; Evidence={ECO:0000250|UniProtKB:Q4WNT5};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:75440;\nCC         Evidence={ECO:0000250|UniProtKB:Q4WNT5};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 4,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H13

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXV0?format=txt&versions=4)

```json
{
  "evidence_id": "H13",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/P0DXV0?format=txt&versions=4",
  "source_sha256": "e154cd9089aa6b8a42d60528a7ce84bec0c5a19fc8f6e92dd2125bb46b055be2",
  "retrieved_utc": "2026-11-02T04:29:45.056058+00:00",
  "source_locator": "lines 127-135",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=eburicol + reduced [NADPH--hemoprotein reductase] + O2 = 32-\nCC         hydroxyeburicol + oxidized [NADPH--hemoprotein reductase] + H2O +\nCC         H(+); Xref=Rhea:RHEA:75427, Rhea:RHEA-COMP:11964, Rhea:RHEA-\nCC         COMP:11965, ChEBI:CHEBI:15377, ChEBI:CHEBI:15378, ChEBI:CHEBI:15379,\nCC         ChEBI:CHEBI:57618, ChEBI:CHEBI:58210, ChEBI:CHEBI:70315,\nCC         ChEBI:CHEBI:194328; Evidence={ECO:0000250|UniProtKB:P10614};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:75428;\nCC         Evidence={ECO:0000250|UniProtKB:P10614};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 4,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H14

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXV0?format=txt&versions=4)

```json
{
  "evidence_id": "H14",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/P0DXV0?format=txt&versions=4",
  "source_sha256": "e154cd9089aa6b8a42d60528a7ce84bec0c5a19fc8f6e92dd2125bb46b055be2",
  "retrieved_utc": "2026-11-02T04:29:45.056058+00:00",
  "source_locator": "lines 136-144",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=32-hydroxyeburicol + reduced [NADPH--hemoprotein reductase] +\nCC         O2 = 32-oxoeburicol + oxidized [NADPH--hemoprotein reductase] + 2 H2O\nCC         + H(+); Xref=Rhea:RHEA:75431, Rhea:RHEA-COMP:11964, Rhea:RHEA-\nCC         COMP:11965, ChEBI:CHEBI:15377, ChEBI:CHEBI:15378, ChEBI:CHEBI:15379,\nCC         ChEBI:CHEBI:57618, ChEBI:CHEBI:58210, ChEBI:CHEBI:194328,\nCC         ChEBI:CHEBI:194329; Evidence={ECO:0000250|UniProtKB:P10614};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:75432;\nCC         Evidence={ECO:0000250|UniProtKB:P10614};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 4,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H15

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXV0?format=txt&versions=4)

```json
{
  "evidence_id": "H15",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/P0DXV0?format=txt&versions=4",
  "source_sha256": "e154cd9089aa6b8a42d60528a7ce84bec0c5a19fc8f6e92dd2125bb46b055be2",
  "retrieved_utc": "2026-11-02T04:29:45.056058+00:00",
  "source_locator": "lines 145-154",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=32-oxoeburicol + reduced [NADPH--hemoprotein reductase] + O2 =\nCC         14-demethyleburicol + formate + oxidized [NADPH--hemoprotein\nCC         reductase] + H2O + 2 H(+); Xref=Rhea:RHEA:75435, Rhea:RHEA-\nCC         COMP:11964, Rhea:RHEA-COMP:11965, ChEBI:CHEBI:15377,\nCC         ChEBI:CHEBI:15378, ChEBI:CHEBI:15379, ChEBI:CHEBI:15740,\nCC         ChEBI:CHEBI:57618, ChEBI:CHEBI:58210, ChEBI:CHEBI:194329,\nCC         ChEBI:CHEBI:194330; Evidence={ECO:0000250|UniProtKB:P10614};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:75436;\nCC         Evidence={ECO:0000250|UniProtKB:P10614};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 4,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 175. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
