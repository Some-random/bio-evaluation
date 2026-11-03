# EC_number_0148: before and after transfer clarification

[All 1,328 cases](../README.md) · [Method](../METHOD.md) · [Summary](../SUMMARY.md) · [Exact reviewer user message](../inputs/EC_number_0148.txt)

**Task:** `EC_number`  
**Author key, unchanged:** **A** — 2.7.7.80

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
MSLSLNEYLRYGRQLIVPEFGLQGQISLKNSRVLVVGAGGLGCPALQYLVGAGFGTVGIVDHDTVDISNLHRQILHTSETVEMLKCESAKLQLAKLNPLVQINTHPVALSPDNSFGIFEQYDIILDCTDTPATRYLINDTAVLLGLTVISGSGLKTEGQLSILNFNNTGPCYRCFYPTPPPPSSVTACSDGGVLGPVIGIMGVMMALEAIKVVSGYYLREDVEFQPFLSLYSGYGPLQSLRTFKMRRRSPKCRVCNAGTREITRHVIETELDYAVWCGKMDYNVLEKDERVSVEQLSAQRAPYLVDVRAKEQYSIVHLPNSINIPLNALKHMDTLDVPKETMIYVICRFGNDSQLAVKHLKSIGYENCVDVIGGLTQWSRQIDPNFPIY

[Multiple Choices]
A. 2.7.7.80
B. 2.7.7.1
C. 5.6.1.1
D. 2.7.8.7
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

> The exact sequence matches the UBA4 entry, which annotates EC 2.7.7.80 for its molybdopterin-synthase adenylyltransferase activity. That assignment is transferred by similarity from UniProtKB:O95396, rather than direct experimental evidence for this sequence. The protein is also annotated with a second activity, EC 2.8.1.11, which is not among the choices.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence may suggest a multidomain enzyme with adenylation and sulfur-transfer functions, which can help distinguish it from broad alternatives such as an isomerase. But that inference does not establish the specific molybdopterin-synthase substrate or the exact EC 2.7.7.80 reaction.


**Missing item-specific fact**

> The protein-specific functional assignment that UBA4 adenylates the C-terminal Gly-Gly of the molybdopterin-synthase sulfur-carrier protein; the supplied sequence and choices do not state this substrate or activity.


**Reason**

> Choosing the precise EC requires a protein-specific substrate/function assignment. The supporting database annotation is itself transferred by similarity, and was reviewer-only rather than supplied to the evaluated model.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> A is supported among the listed options for one annotated catalytic activity. However, the wording's singular request for a complete EC number does not convey that this protein has a second annotated activity, EC 2.8.1.11, which is not offered.


### Important caveats

- The sequence match establishes applicability of the cited database record, but not direct experimental validation of either activity for this exact protein.
- The author's source snapshot is unknown; the retrieved historical entry and current entry both support EC 2.7.7.80 by similarity.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence may suggest a multidomain enzyme with adenylation and sulfur-transfer functions, which can help distinguish it from broad alternatives such as an isomerase. But that inference does not establish the specific molybdopterin-synthase substrate or the exact EC 2.7.7.80 reaction.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific functional assignment that UBA4 adenylates the C-terminal Gly-Gly of the molybdopterin-synthase sulfur-carrier protein; the supplied sequence and choices do not state this substrate or activity.",
    "reason": "Choosing the precise EC requires a protein-specific substrate/function assignment. The supporting database annotation is itself transferred by similarity, and was reviewer-only rather than supplied to the evaluated model."
  },
  "case_id": "EC_number_0148",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the UBA4 entry, which annotates EC 2.7.7.80 for its molybdopterin-synthase adenylyltransferase activity. That assignment is transferred by similarity from UniProtKB:O95396, rather than direct experimental evidence for this sequence. The protein is also annotated with a second activity, EC 2.8.1.11, which is not among the choices."
  },
  "important_caveats": [
    "The sequence match establishes applicability of the cited database record, but not direct experimental validation of either activity for this exact protein.",
    "The author's source snapshot is unknown; the retrieved historical entry and current entry both support EC 2.7.7.80 by similarity."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "A is supported among the listed options for one annotated catalytic activity. However, the wording's singular request for a complete EC number does not convey that this protein has a second annotated activity, EC 2.8.1.11, which is not offered."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0148",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the UBA4 entry, which annotates EC 2.7.7.80 for its molybdopterin-synthase adenylyltransferase activity. That assignment is transferred by similarity from UniProtKB:O95396, rather than direct experimental evidence for this sequence. The protein is also annotated with a second activity, EC 2.8.1.11, which is not among the choices.",
    "evidence_ids": ["C1", "C4", "C5", "C6"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence may suggest a multidomain enzyme with adenylation and sulfur-transfer functions, which can help distinguish it from broad alternatives such as an isomerase. But that inference does not establish the specific molybdopterin-synthase substrate or the exact EC 2.7.7.80 reaction.",
    "missing_item_specific_fact": "The protein-specific functional assignment that UBA4 adenylates the C-terminal Gly-Gly of the molybdopterin-synthase sulfur-carrier protein; the supplied sequence and choices do not state this substrate or activity.",
    "reason": "Choosing the precise EC requires a protein-specific substrate/function assignment. The supporting database annotation is itself transferred by similarity, and was reviewer-only rather than supplied to the evaluated model."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "A is supported among the listed options for one annotated catalytic activity. However, the wording's singular request for a complete EC number does not convey that this protein has a second annotated activity, EC 2.8.1.11, which is not offered."
  },
  "important_caveats": [
    "The sequence match establishes applicability of the cited database record, but not direct experimental validation of either activity for this exact protein.",
    "The author's source snapshot is unknown; the retrieved historical entry and current entry both support EC 2.7.7.80 by similarity."
  ]
}
```

</details>

## Before: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry W1QET1 (UBA4_OGAPD) lists EC 2.7.7.80 (Molybdopterin-synthase adenylyltransferase) as one of two EC numbers for this protein, with catalytic activity RHEA:43616 confirmed. The annotation is transferred by similarity (ECO:0000250 to O95396, human UBA4), not direct experiment on this sequence, but it is the established database annotation. The sequence matches (389 aa, SHA-256 confirmed). Among the four choices, only 2.7.7.80 corresponds to an actual EC number for this protein. The second EC number (2.8.1.11) is not among the options, so A is the uniquely correct choice from the given set.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence contains a nucleotidyltransferase-like motif (GAGGLGCPALQYLVGAGFGTVGIVDHDT), which could help a knowledgeable model eliminate C (5.6.1.1, a chromatin-remodeling ATPase) and possibly D (2.7.8.7, CDP-diacylglycerol synthase with a different domain architecture). However, both A (2.7.7.80) and B (2.7.7.1) are nucleotidyltransferases sharing the same fold class. Distinguishing molybdopterin-synthase adenylyltransferase from DNA-directed RNA polymerase requires knowing the specific substrate (molybdopterin-synthase sulfur-carrier protein vs. RNA template), which is an item-specific fact about this protein's function in molybdenum cofactor biosynthesis.


**Missing item-specific fact**

> The identification of this sequence as UBA4, a bifunctional enzyme in the molybdenum cofactor (Moco) biosynthesis pathway that adenylylates the C-terminal Gly-Gly of MOCS2A, is required to select 2.7.7.80 over 2.7.7.1. No general sequence feature in the provided input reveals this substrate specificity.


**Reason**

> While the nucleotidyltransferase domain narrows the class to EC 2.7.x.x, the final distinction between 2.7.7.80 and 2.7.7.1 depends on knowing the protein's specific biological role (molybdenum cofactor biosynthesis) and substrate (MOCS2A sulfur-carrier protein), which is an item-specific annotation fact not derivable from the sequence alone through general reasoning.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Although the protein carries two EC numbers (2.7.7.80 and 2.8.1.11), only 2.7.7.80 appears among the four choices. The other three options (2.7.7.1, 5.6.1.1, 2.7.8.7) do not correspond to this protein's annotation. Thus the singular phrasing 'the EC number' does not create genuine ambiguity among the provided options.


### Important caveats

- The EC 2.7.7.80 annotation carries evidence code ECO:0000250 (similarity to UniProtKB:O95396, human UBA4), meaning it is transferred by homology rather than directly demonstrated on the Ogataea parapolymorpha protein.
- The protein is bifunctional (adenylyltransferase + sulfurtransferase); the question's singular 'EC number' phrasing slightly misrepresents the protein's enzymatic profile, though this does not affect answer selection given the provided choices.
- The UniProt entry was first publicly released 2025-06-18; the historical record at entry version 67 (2026-01-28) already contains the same EC annotations, so the answer is stable across the relevant snapshot window.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a nucleotidyltransferase-like motif (GAGGLGCPALQYLVGAGFGTVGIVDHDT), which could help a knowledgeable model eliminate C (5.6.1.1, a chromatin-remodeling ATPase) and possibly D (2.7.8.7, CDP-diacylglycerol synthase with a different domain architecture). However, both A (2.7.7.80) and B (2.7.7.1) are nucleotidyltransferases sharing the same fold class. Distinguishing molybdopterin-synthase adenylyltransferase from DNA-directed RNA polymerase requires knowing the specific substrate (molybdopterin-synthase sulfur-carrier protein vs. RNA template), which is an item-specific fact about this protein's function in molybdenum cofactor biosynthesis.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The identification of this sequence as UBA4, a bifunctional enzyme in the molybdenum cofactor (Moco) biosynthesis pathway that adenylylates the C-terminal Gly-Gly of MOCS2A, is required to select 2.7.7.80 over 2.7.7.1. No general sequence feature in the provided input reveals this substrate specificity.",
    "reason": "While the nucleotidyltransferase domain narrows the class to EC 2.7.x.x, the final distinction between 2.7.7.80 and 2.7.7.1 depends on knowing the protein's specific biological role (molybdenum cofactor biosynthesis) and substrate (MOCS2A sulfur-carrier protein), which is an item-specific annotation fact not derivable from the sequence alone through general reasoning."
  },
  "case_id": "EC_number_0148",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "UniProt entry W1QET1 (UBA4_OGAPD) lists EC 2.7.7.80 (Molybdopterin-synthase adenylyltransferase) as one of two EC numbers for this protein, with catalytic activity RHEA:43616 confirmed. The annotation is transferred by similarity (ECO:0000250 to O95396, human UBA4), not direct experiment on this sequence, but it is the established database annotation. The sequence matches (389 aa, SHA-256 confirmed). Among the four choices, only 2.7.7.80 corresponds to an actual EC number for this protein. The second EC number (2.8.1.11) is not among the options, so A is the uniquely correct choice from the given set."
  },
  "important_caveats": [
    "The EC 2.7.7.80 annotation carries evidence code ECO:0000250 (similarity to UniProtKB:O95396, human UBA4), meaning it is transferred by homology rather than directly demonstrated on the Ogataea parapolymorpha protein.",
    "The protein is bifunctional (adenylyltransferase + sulfurtransferase); the question's singular 'EC number' phrasing slightly misrepresents the protein's enzymatic profile, though this does not affect answer selection given the provided choices.",
    "The UniProt entry was first publicly released 2025-06-18; the historical record at entry version 67 (2026-01-28) already contains the same EC annotations, so the answer is stable across the relevant snapshot window."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although the protein carries two EC numbers (2.7.7.80 and 2.8.1.11), only 2.7.7.80 appears among the four choices. The other three options (2.7.7.1, 5.6.1.1, 2.7.8.7) do not correspond to this protein's annotation. Thus the singular phrasing 'the EC number' does not create genuine ambiguity among the provided options."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0148",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry W1QET1 (UBA4_OGAPD) lists EC 2.7.7.80 (Molybdopterin-synthase adenylyltransferase) as one of two EC numbers for this protein, with catalytic activity RHEA:43616 confirmed. The annotation is transferred by similarity (ECO:0000250 to O95396, human UBA4), not direct experiment on this sequence, but it is the established database annotation. The sequence matches (389 aa, SHA-256 confirmed). Among the four choices, only 2.7.7.80 corresponds to an actual EC number for this protein. The second EC number (2.8.1.11) is not among the options, so A is the uniquely correct choice from the given set.",
    "evidence_ids": ["C4", "C5", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence contains a nucleotidyltransferase-like motif (GAGGLGCPALQYLVGAGFGTVGIVDHDT), which could help a knowledgeable model eliminate C (5.6.1.1, a chromatin-remodeling ATPase) and possibly D (2.7.8.7, CDP-diacylglycerol synthase with a different domain architecture). However, both A (2.7.7.80) and B (2.7.7.1) are nucleotidyltransferases sharing the same fold class. Distinguishing molybdopterin-synthase adenylyltransferase from DNA-directed RNA polymerase requires knowing the specific substrate (molybdopterin-synthase sulfur-carrier protein vs. RNA template), which is an item-specific fact about this protein's function in molybdenum cofactor biosynthesis.",
    "missing_item_specific_fact": "The identification of this sequence as UBA4, a bifunctional enzyme in the molybdenum cofactor (Moco) biosynthesis pathway that adenylylates the C-terminal Gly-Gly of MOCS2A, is required to select 2.7.7.80 over 2.7.7.1. No general sequence feature in the provided input reveals this substrate specificity.",
    "reason": "While the nucleotidyltransferase domain narrows the class to EC 2.7.x.x, the final distinction between 2.7.7.80 and 2.7.7.1 depends on knowing the protein's specific biological role (molybdenum cofactor biosynthesis) and substrate (MOCS2A sulfur-carrier protein), which is an item-specific annotation fact not derivable from the sequence alone through general reasoning."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although the protein carries two EC numbers (2.7.7.80 and 2.8.1.11), only 2.7.7.80 appears among the four choices. The other three options (2.7.7.1, 5.6.1.1, 2.7.8.7) do not correspond to this protein's annotation. Thus the singular phrasing 'the EC number' does not create genuine ambiguity among the provided options."
  },
  "important_caveats": [
    "The EC 2.7.7.80 annotation carries evidence code ECO:0000250 (similarity to UniProtKB:O95396, human UBA4), meaning it is transferred by homology rather than directly demonstrated on the Ogataea parapolymorpha protein.",
    "The protein is bifunctional (adenylyltransferase + sulfurtransferase); the question's singular 'EC number' phrasing slightly misrepresents the protein's enzymatic profile, though this does not affect answer selection given the provided choices.",
    "The UniProt entry was first publicly released 2025-06-18; the historical record at entry version 67 (2026-01-28) already contains the same EC annotations, so the answer is stable across the relevant snapshot window."
  ]
}
```

</details>

## After: GPT-6 Luna

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence-matched UniProt record assigns EC 2.7.7.80 to the molybdopterin-synthase adenylyltransferase activity. This supports choice A, although the cited evidence is transferred from a homolog rather than a direct assay of this protein.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is consistent with the UBA4/MoeB-like architecture: an N-terminal ATP-dependent adenylation domain and a C-terminal sulfurtransferase-like domain. Transferable knowledge of this family links its adenylation activity to activation of the molybdopterin-synthase sulfur carrier, matching A. That meaningfully distinguishes A from the offered polymerization/transferase alternatives and the isomerase option.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A family- and domain-level inference from the sequence provides a credible basis for selecting A without access to this exact protein's annotation. It is probabilistic rather than a direct demonstration of the target's catalytic activity.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Only A among the listed choices matches the expected adenylyltransferase activity. The protein is also annotated with a sulfurtransferase activity, but that EC number is not offered.


### Important caveats

- The cited EC assignment is based on transfer from a homolog; the supplied evidence does not establish direct experimental validation for this exact protein.
- The protein has an additional catalytic activity, so a single-answer format does not represent all its annotated enzyme functions.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with the UBA4/MoeB-like architecture: an N-terminal ATP-dependent adenylation domain and a C-terminal sulfurtransferase-like domain. Transferable knowledge of this family links its adenylation activity to activation of the molybdopterin-synthase sulfur carrier, matching A. That meaningfully distinguishes A from the offered polymerization/transferase alternatives and the isomerase option.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A family- and domain-level inference from the sequence provides a credible basis for selecting A without access to this exact protein's annotation. It is probabilistic rather than a direct demonstration of the target's catalytic activity."
  },
  "case_id": "EC_number_0148",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record assigns EC 2.7.7.80 to the molybdopterin-synthase adenylyltransferase activity. This supports choice A, although the cited evidence is transferred from a homolog rather than a direct assay of this protein."
  },
  "important_caveats": [
    "The cited EC assignment is based on transfer from a homolog; the supplied evidence does not establish direct experimental validation for this exact protein.",
    "The protein has an additional catalytic activity, so a single-answer format does not represent all its annotated enzyme functions."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only A among the listed choices matches the expected adenylyltransferase activity. The protein is also annotated with a sulfurtransferase activity, but that EC number is not offered."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0148",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record assigns EC 2.7.7.80 to the molybdopterin-synthase adenylyltransferase activity. This supports choice A, although the cited evidence is transferred from a homolog rather than a direct assay of this protein.",
    "evidence_ids": ["C4", "C5", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is consistent with the UBA4/MoeB-like architecture: an N-terminal ATP-dependent adenylation domain and a C-terminal sulfurtransferase-like domain. Transferable knowledge of this family links its adenylation activity to activation of the molybdopterin-synthase sulfur carrier, matching A. That meaningfully distinguishes A from the offered polymerization/transferase alternatives and the isomerase option.",
    "missing_item_specific_fact": "",
    "reason": "A family- and domain-level inference from the sequence provides a credible basis for selecting A without access to this exact protein's annotation. It is probabilistic rather than a direct demonstration of the target's catalytic activity."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only A among the listed choices matches the expected adenylyltransferase activity. The protein is also annotated with a sulfurtransferase activity, but that EC number is not offered."
  },
  "important_caveats": [
    "The cited EC assignment is based on transfer from a homolog; the supplied evidence does not establish direct experimental validation for this exact protein.",
    "The protein has an additional catalytic activity, so a single-answer format does not represent all its annotated enzyme functions."
  ]
}
```

</details>

## After: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry W1QET1 (UBA4_OGAPD, Ogataea parapolymorpha) is annotated with EC 2.7.7.80 (Molybdopterin-synthase adenylyltransferase) for its adenylyltransferase activity. The sequence in the question matches the UniProt entry (SHA-256 confirmed). The annotation is based on similarity to human UBA4 (O95396, ECO:0000250), which is a well-characterized homolog. The catalytic reaction (Gly-Gly + ATP → Gly-Gly-AMP + PPi) is consistent with EC 2.7.7.80. While the evidence is computational/similarity-based rather than direct experimental for this exact protein, the annotation is reasonable and supported.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence (~389 aa) contains a clear Rossmann-fold nucleotide-binding motif in its N-terminal region ('VLVVGAGGLGCPALQYLVGAGFGTVGIVDHDT'), with the canonical GxGxxG pattern visible in 'GAGGLG' and 'GAGFG'. This identifies the protein as a nucleotidyltransferase. Option B (EC 2.7.7.1, DNA-directed RNA polymerase) is eliminated because RNA polymerase catalytic subunits are 1000+ amino acids, far exceeding the 389 aa length. Option C (EC 5.6.1.1, DNA helicase) is eliminated because the sequence lacks characteristic helicase motifs (Walker A/B, DEAH/DEAD boxes) and instead shows a Rossmann-fold transferase architecture. Option D (EC 2.7.8.7, CDP-diacylglycerol synthase) is eliminated because this is a membrane-associated enzyme requiring transmembrane helices, which are absent from this soluble protein. The remaining option A (EC 2.7.7.80, molybdopterin-synthase adenylyltransferase) is a nucleotidyltransferase with a Rossmann fold, fully consistent with the observed sequence features. Additionally, the UBA4 family (ubiquitin-like protein activator 4) is well-conserved across eukaryotes, and the domain architecture here matches the known UBA4 fold, which carries EC 2.7.7.80 activity.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The Rossmann-fold motif, protein size, absence of transmembrane domains, and absence of helicase motifs allow elimination of options B, C, and D through general structural biology and enzyme-family knowledge. The remaining nucleotidyltransferase option (A) is consistent with the observed sequence architecture. Recognition of the UBA4 family from the Rossmann-fold pattern and overall domain organization is transferable knowledge from well-studied homologs (human O95396, S. cerevisiae UBA4).


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options B, C, and D are eliminated by clear structural/size criteria (RNA polymerase size, helicase motifs, transmembrane domains). Only A (a nucleotidyltransferase with Rossmann fold) is consistent with the sequence features. No other option is defensible.


### Important caveats

- The UniProt annotation for EC 2.7.7.80 on this protein is based on similarity to human UBA4 (ECO:0000250), not direct experimental characterization of the Ogataea parapolymorpha protein itself.
- UBA4 proteins carry dual activities (adenylyltransferase EC 2.7.7.80 and sulfurtransferase EC 2.8.1.11); only the adenylyltransferase EC is offered as an option, so the sulfurtransferase activity does not create ambiguity among the choices.
- The UBA4 protein was first integrated into Swiss-Prot on 2025-06-18, relatively recent; however, the family-level knowledge (human, yeast UBA4) predates this and supports the reasoning.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence (~389 aa) contains a clear Rossmann-fold nucleotide-binding motif in its N-terminal region ('VLVVGAGGLGCPALQYLVGAGFGTVGIVDHDT'), with the canonical GxGxxG pattern visible in 'GAGGLG' and 'GAGFG'. This identifies the protein as a nucleotidyltransferase. Option B (EC 2.7.7.1, DNA-directed RNA polymerase) is eliminated because RNA polymerase catalytic subunits are 1000+ amino acids, far exceeding the 389 aa length. Option C (EC 5.6.1.1, DNA helicase) is eliminated because the sequence lacks characteristic helicase motifs (Walker A/B, DEAH/DEAD boxes) and instead shows a Rossmann-fold transferase architecture. Option D (EC 2.7.8.7, CDP-diacylglycerol synthase) is eliminated because this is a membrane-associated enzyme requiring transmembrane helices, which are absent from this soluble protein. The remaining option A (EC 2.7.7.80, molybdopterin-synthase adenylyltransferase) is a nucleotidyltransferase with a Rossmann fold, fully consistent with the observed sequence features. Additionally, the UBA4 family (ubiquitin-like protein activator 4) is well-conserved across eukaryotes, and the domain architecture here matches the known UBA4 fold, which carries EC 2.7.7.80 activity.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The Rossmann-fold motif, protein size, absence of transmembrane domains, and absence of helicase motifs allow elimination of options B, C, and D through general structural biology and enzyme-family knowledge. The remaining nucleotidyltransferase option (A) is consistent with the observed sequence architecture. Recognition of the UBA4 family from the Rossmann-fold pattern and overall domain organization is transferable knowledge from well-studied homologs (human O95396, S. cerevisiae UBA4)."
  },
  "case_id": "EC_number_0148",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "UniProt entry W1QET1 (UBA4_OGAPD, Ogataea parapolymorpha) is annotated with EC 2.7.7.80 (Molybdopterin-synthase adenylyltransferase) for its adenylyltransferase activity. The sequence in the question matches the UniProt entry (SHA-256 confirmed). The annotation is based on similarity to human UBA4 (O95396, ECO:0000250), which is a well-characterized homolog. The catalytic reaction (Gly-Gly + ATP → Gly-Gly-AMP + PPi) is consistent with EC 2.7.7.80. While the evidence is computational/similarity-based rather than direct experimental for this exact protein, the annotation is reasonable and supported."
  },
  "important_caveats": [
    "The UniProt annotation for EC 2.7.7.80 on this protein is based on similarity to human UBA4 (ECO:0000250), not direct experimental characterization of the Ogataea parapolymorpha protein itself.",
    "UBA4 proteins carry dual activities (adenylyltransferase EC 2.7.7.80 and sulfurtransferase EC 2.8.1.11); only the adenylyltransferase EC is offered as an option, so the sulfurtransferase activity does not create ambiguity among the choices.",
    "The UBA4 protein was first integrated into Swiss-Prot on 2025-06-18, relatively recent; however, the family-level knowledge (human, yeast UBA4) predates this and supports the reasoning."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options B, C, and D are eliminated by clear structural/size criteria (RNA polymerase size, helicase motifs, transmembrane domains). Only A (a nucleotidyltransferase with Rossmann fold) is consistent with the sequence features. No other option is defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0148",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry W1QET1 (UBA4_OGAPD, Ogataea parapolymorpha) is annotated with EC 2.7.7.80 (Molybdopterin-synthase adenylyltransferase) for its adenylyltransferase activity. The sequence in the question matches the UniProt entry (SHA-256 confirmed). The annotation is based on similarity to human UBA4 (O95396, ECO:0000250), which is a well-characterized homolog. The catalytic reaction (Gly-Gly + ATP → Gly-Gly-AMP + PPi) is consistent with EC 2.7.7.80. While the evidence is computational/similarity-based rather than direct experimental for this exact protein, the annotation is reasonable and supported.",
    "evidence_ids": ["C4", "C5", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence (~389 aa) contains a clear Rossmann-fold nucleotide-binding motif in its N-terminal region ('VLVVGAGGLGCPALQYLVGAGFGTVGIVDHDT'), with the canonical GxGxxG pattern visible in 'GAGGLG' and 'GAGFG'. This identifies the protein as a nucleotidyltransferase. Option B (EC 2.7.7.1, DNA-directed RNA polymerase) is eliminated because RNA polymerase catalytic subunits are 1000+ amino acids, far exceeding the 389 aa length. Option C (EC 5.6.1.1, DNA helicase) is eliminated because the sequence lacks characteristic helicase motifs (Walker A/B, DEAH/DEAD boxes) and instead shows a Rossmann-fold transferase architecture. Option D (EC 2.7.8.7, CDP-diacylglycerol synthase) is eliminated because this is a membrane-associated enzyme requiring transmembrane helices, which are absent from this soluble protein. The remaining option A (EC 2.7.7.80, molybdopterin-synthase adenylyltransferase) is a nucleotidyltransferase with a Rossmann fold, fully consistent with the observed sequence features. Additionally, the UBA4 family (ubiquitin-like protein activator 4) is well-conserved across eukaryotes, and the domain architecture here matches the known UBA4 fold, which carries EC 2.7.7.80 activity.",
    "missing_item_specific_fact": "",
    "reason": "The Rossmann-fold motif, protein size, absence of transmembrane domains, and absence of helicase motifs allow elimination of options B, C, and D through general structural biology and enzyme-family knowledge. The remaining nucleotidyltransferase option (A) is consistent with the observed sequence architecture. Recognition of the UBA4 family from the Rossmann-fold pattern and overall domain organization is transferable knowledge from well-studied homologs (human O95396, S. cerevisiae UBA4)."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options B, C, and D are eliminated by clear structural/size criteria (RNA polymerase size, helicase motifs, transmembrane domains). Only A (a nucleotidyltransferase with Rossmann fold) is consistent with the sequence features. No other option is defensible."
  },
  "important_caveats": [
    "The UniProt annotation for EC 2.7.7.80 on this protein is based on similarity to human UBA4 (ECO:0000250), not direct experimental characterization of the Ogataea parapolymorpha protein itself.",
    "UBA4 proteins carry dual activities (adenylyltransferase EC 2.7.7.80 and sulfurtransferase EC 2.8.1.11); only the adenylyltransferase EC is offered as an option, so the sulfurtransferase activity does not create ambiguity among the choices.",
    "The UBA4 protein was first integrated into Swiss-Prot on 2025-06-18, relatively recent; however, the family-level knowledge (human, yeast UBA4) predates this and supports the reasoning."
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
  "requested_accession": "W1QET1",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "benchmark_sequence_sha256": "a901665ea3dc44218892e98264561a93d82231546cdf75b9015b7ec0eb86f63a",
  "benchmark_sequence_length": 389,
  "current_status": "retrieved",
  "current_sequence_comparison": "matched",
  "current_entry_audit": {
    "entryVersion": 69,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2014-03-19",
    "sequenceVersion": 1
  },
  "current_uniprot_release": "2026_03",
  "current_record_sha256": "958c25c940d458086b51fa46493ccb8538925f70cafe7242c4eeff6965bc6e08",
  "current_source_sequence_sha256": "a901665ea3dc44218892e98264561a93d82231546cdf75b9015b7ec0eb86f63a",
  "current_source_sequence_length": 389,
  "historical_status": "retrieved",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "selected_historical_entry_version": 67,
  "selected_historical_version": {
    "accession": "W1QET1",
    "database": "Swiss-Prot",
    "entryVersion": 67,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "UBA4_OGAPD",
    "sequenceVersion": 1
  },
  "selected_historical_record_sha256": "1439891a4b0a62345927d6f7a896540071a99c07ab5153e3c7dc6126a8edc193",
  "selected_historical_source_sequence_sha256": "a901665ea3dc44218892e98264561a93d82231546cdf75b9015b7ec0eb86f63a",
  "selected_historical_source_sequence_length": 389,
  "latest_at_cutoff_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 67,
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/W1QET1.json)

```json
{
  "evidence_id": "C1",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/W1QET1.json",
  "source_sha256": "958c25c940d458086b51fa46493ccb8538925f70cafe7242c4eeff6965bc6e08",
  "retrieved_utc": "2026-11-02T04:34:06.106793+00:00",
  "json_pointer": "/primaryAccession",
  "excerpt": "\"W1QET1\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/W1QET1.json)

```json
{
  "evidence_id": "C2",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/W1QET1.json",
  "source_sha256": "958c25c940d458086b51fa46493ccb8538925f70cafe7242c4eeff6965bc6e08",
  "retrieved_utc": "2026-11-02T04:34:06.106793+00:00",
  "json_pointer": "/entryAudit",
  "excerpt": "{\"entryVersion\":69,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2014-03-19\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/W1QET1.json)

```json
{
  "evidence_id": "C3",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/W1QET1.json",
  "source_sha256": "958c25c940d458086b51fa46493ccb8538925f70cafe7242c4eeff6965bc6e08",
  "retrieved_utc": "2026-11-02T04:34:06.106793+00:00",
  "json_pointer": "/organism",
  "excerpt": "{\"commonName\":\"Yeast\",\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP000008673\",\"source\":\"Proteomes\"}],\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Saccharomycotina\",\"Pichiomycetes\",\"Pichiales\",\"Pichiaceae\",\"Ogataea\"],\"scientificName\":\"Ogataea parapolymorpha (strain ATCC 26012 / BCRC 20466 / JCM 22074 / NRRL Y-7560 / DL-1)\",\"synonyms\":[\"Hansenula polymorpha\"],\"taxonId\":871575}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/W1QET1.json)

```json
{
  "evidence_id": "C4",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/W1QET1.json",
  "source_sha256": "958c25c940d458086b51fa46493ccb8538925f70cafe7242c4eeff6965bc6e08",
  "retrieved_utc": "2026-11-02T04:34:06.106793+00:00",
  "json_pointer": "/proteinDescription",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Ubiquitin-like protein activator 4\"}}],\"includes\":[{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Adenylyltransferase UBA4\"}},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Sulfur carrier protein MOCS2A adenylyltransferase\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"O95396\",\"source\":\"UniProtKB\"}],\"value\":\"2.7.7.80\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Molybdopterin-synthase adenylyltransferase\"}}},{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Sulfur carrier protein MOCS2A sulfurtransferase\"}},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Sulfurtransferase UBA4\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"O95396\",\"source\":\"UniProtKB\"}],\"value\":\"2.8.1.11\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Molybdopterin-synthase sulfurtransferase\"}}}],\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Adenylyltransferase and sulfurtransferase uba4\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/W1QET1.json)

```json
{
  "evidence_id": "C5",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/W1QET1.json",
  "source_sha256": "958c25c940d458086b51fa46493ccb8538925f70cafe7242c4eeff6965bc6e08",
  "retrieved_utc": "2026-11-02T04:34:06.106793+00:00",
  "json_pointer": "/comments/1",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"ecNumber\":\"2.7.7.80\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"O95396\",\"source\":\"UniProtKB\"}],\"name\":\"[molybdopterin-synthase sulfur-carrier protein]-C-terminal Gly-Gly + ATP + H(+) = [molybdopterin-synthase sulfur-carrier protein]-C-terminal Gly-Gly-AMP + diphosphate\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:43616\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:12159\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:12202\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:30616\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:33019\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:90618\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:90778\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/W1QET1.json)

```json
{
  "evidence_id": "C6",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/W1QET1.json",
  "source_sha256": "958c25c940d458086b51fa46493ccb8538925f70cafe7242c4eeff6965bc6e08",
  "retrieved_utc": "2026-11-02T04:34:06.106793+00:00",
  "json_pointer": "/comments/2",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"ecNumber\":\"2.8.1.11\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"O95396\",\"source\":\"UniProtKB\"}],\"name\":\"[molybdopterin-synthase sulfur-carrier protein]-C-terminal Gly-Gly-AMP + S-sulfanyl-L-cysteinyl-[cysteine desulfurase] + AH2 = [molybdopterin-synthase sulfur-carrier protein]-C-terminal-Gly-aminoethanethioate + L-cysteinyl-[cysteine desulfurase] + A + AMP + 2 H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:48612\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:12157\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:12158\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:12159\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:19907\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:13193\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:17499\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:29950\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:61963\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:90618\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:232372\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:456215\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/W1QET1?format=txt&versions=67)

```json
{
  "evidence_id": "H1",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/W1QET1?format=txt&versions=67",
  "source_sha256": "1439891a4b0a62345927d6f7a896540071a99c07ab5153e3c7dc6126a8edc193",
  "retrieved_utc": "2026-11-02T04:34:08.361822+00:00",
  "source_locator": "lines 1-24",
  "excerpt": "ID   UBA4_OGAPD              Reviewed;         389 AA.\nAC   W1QET1;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   19-MAR-2014, sequence version 1.\nDT   28-JAN-2026, entry version 67.\nDE   RecName: Full=Adenylyltransferase and sulfurtransferase uba4 {ECO:0000305};\nDE   AltName: Full=Ubiquitin-like protein activator 4 {ECO:0000305};\nDE   Includes:\nDE     RecName: Full=Molybdopterin-synthase adenylyltransferase {ECO:0000305};\nDE              EC=2.7.7.80 {ECO:0000250|UniProtKB:O95396};\nDE     AltName: Full=Adenylyltransferase UBA4 {ECO:0000305};\nDE     AltName: Full=Sulfur carrier protein MOCS2A adenylyltransferase {ECO:0000305};\nDE   Includes:\nDE     RecName: Full=Molybdopterin-synthase sulfurtransferase {ECO:0000305};\nDE              EC=2.8.1.11 {ECO:0000250|UniProtKB:O95396};\nDE     AltName: Full=Sulfur carrier protein MOCS2A sulfurtransferase {ECO:0000305};\nDE     AltName: Full=Sulfurtransferase UBA4 {ECO:0000305};\nGN   Name=UBA4 {ECO:0000305}; Synonyms=CNX4 {ECO:0000303|PubMed:33617956};\nGN   ORFNames=HPODL_00948 {ECO:0000312|EMBL:ESX00063.1};\nOS   Ogataea parapolymorpha (strain ATCC 26012 / BCRC 20466 / JCM 22074 / NRRL\nOS   Y-7560 / DL-1) (Yeast) (Hansenula polymorpha).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Saccharomycotina; Pichiomycetes;\nOC   Pichiales; Pichiaceae; Ogataea.\nOX   NCBI_TaxID=871575 {ECO:0000312|Proteomes:UP000008673};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 67,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/W1QET1?format=txt&versions=67)

```json
{
  "evidence_id": "H2",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/W1QET1?format=txt&versions=67",
  "source_sha256": "1439891a4b0a62345927d6f7a896540071a99c07ab5153e3c7dc6126a8edc193",
  "retrieved_utc": "2026-11-02T04:34:08.361822+00:00",
  "source_locator": "lines 6-17",
  "excerpt": "DE   RecName: Full=Adenylyltransferase and sulfurtransferase uba4 {ECO:0000305};\nDE   AltName: Full=Ubiquitin-like protein activator 4 {ECO:0000305};\nDE   Includes:\nDE     RecName: Full=Molybdopterin-synthase adenylyltransferase {ECO:0000305};\nDE              EC=2.7.7.80 {ECO:0000250|UniProtKB:O95396};\nDE     AltName: Full=Adenylyltransferase UBA4 {ECO:0000305};\nDE     AltName: Full=Sulfur carrier protein MOCS2A adenylyltransferase {ECO:0000305};\nDE   Includes:\nDE     RecName: Full=Molybdopterin-synthase sulfurtransferase {ECO:0000305};\nDE              EC=2.8.1.11 {ECO:0000250|UniProtKB:O95396};\nDE     AltName: Full=Sulfur carrier protein MOCS2A sulfurtransferase {ECO:0000305};\nDE     AltName: Full=Sulfurtransferase UBA4 {ECO:0000305};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 67,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/W1QET1?format=txt&versions=67)

```json
{
  "evidence_id": "H3",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/W1QET1?format=txt&versions=67",
  "source_sha256": "1439891a4b0a62345927d6f7a896540071a99c07ab5153e3c7dc6126a8edc193",
  "retrieved_utc": "2026-11-02T04:34:08.361822+00:00",
  "source_locator": "lines 36-44",
  "excerpt": "RN   [2] {ECO:0000305}\nRP   FUNCTION, AND PATHWAY.\nRX   PubMed=33617956; DOI=10.1016/j.ymben.2021.02.004;\nRA   Perli T., van der Vorm D.N.A., Wassink M., van den Broek M., Pronk J.T.,\nRA   Daran J.M.;\nRT   \"Engineering heterologous molybdenum-cofactor-biosynthesis and nitrate-\nRT   assimilation pathways enables nitrate utilization by Saccharomyces\nRT   cerevisiae.\";\nRL   Metab. Eng. 65:11-29(2021).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 67,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/W1QET1?format=txt&versions=67)

```json
{
  "evidence_id": "H4",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/W1QET1?format=txt&versions=67",
  "source_sha256": "1439891a4b0a62345927d6f7a896540071a99c07ab5153e3c7dc6126a8edc193",
  "retrieved_utc": "2026-11-02T04:34:08.361822+00:00",
  "source_locator": "lines 61-68",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=[molybdopterin-synthase sulfur-carrier protein]-C-terminal\nCC         Gly-Gly + ATP + H(+) = [molybdopterin-synthase sulfur-carrier\nCC         protein]-C-terminal Gly-Gly-AMP + diphosphate; Xref=Rhea:RHEA:43616,\nCC         Rhea:RHEA-COMP:12159, Rhea:RHEA-COMP:12202, ChEBI:CHEBI:15378,\nCC         ChEBI:CHEBI:30616, ChEBI:CHEBI:33019, ChEBI:CHEBI:90618,\nCC         ChEBI:CHEBI:90778; EC=2.7.7.80;\nCC         Evidence={ECO:0000250|UniProtKB:O95396};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 67,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/W1QET1?format=txt&versions=67)

```json
{
  "evidence_id": "H5",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/W1QET1?format=txt&versions=67",
  "source_sha256": "1439891a4b0a62345927d6f7a896540071a99c07ab5153e3c7dc6126a8edc193",
  "retrieved_utc": "2026-11-02T04:34:08.361822+00:00",
  "source_locator": "lines 69-79",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=[molybdopterin-synthase sulfur-carrier protein]-C-terminal\nCC         Gly-Gly-AMP + S-sulfanyl-L-cysteinyl-[cysteine desulfurase] + AH2 =\nCC         [molybdopterin-synthase sulfur-carrier protein]-C-terminal-Gly-\nCC         aminoethanethioate + L-cysteinyl-[cysteine desulfurase] + A + AMP + 2\nCC         H(+); Xref=Rhea:RHEA:48612, Rhea:RHEA-COMP:12157, Rhea:RHEA-\nCC         COMP:12158, Rhea:RHEA-COMP:12159, Rhea:RHEA-COMP:19907,\nCC         ChEBI:CHEBI:13193, ChEBI:CHEBI:15378, ChEBI:CHEBI:17499,\nCC         ChEBI:CHEBI:29950, ChEBI:CHEBI:61963, ChEBI:CHEBI:90618,\nCC         ChEBI:CHEBI:232372, ChEBI:CHEBI:456215; EC=2.8.1.11;\nCC         Evidence={ECO:0000250|UniProtKB:O95396};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 67,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 148. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
