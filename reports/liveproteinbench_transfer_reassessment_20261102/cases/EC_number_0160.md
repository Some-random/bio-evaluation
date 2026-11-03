# EC_number_0160: before and after transfer clarification

[All 1,328 cases](../README.md) · [Method](../METHOD.md) · [Summary](../SUMMARY.md) · [Exact reviewer user message](../inputs/EC_number_0160.txt)

**Task:** `EC_number`  
**Author key, unchanged:** **B** — 1.1.1.136

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
MEKEKGEEKMNDSRKITVIGLGYVGLPLAIHFAERGYNVVGLDKDKRKIERIEKGDSYIPDVSSNVLKDLVQNKQLVVYTPHTGIEEFQNSEYVIVTVPTPINKQKEPDLSALIAASHYIKQNLQAGQTFIFESSTYPGTLEEVIIPIIAQSGKEVGKDYYIGYSPERIDPANQQYTVQTIPKVISGQTERCKQQVQKLYSTIFDTVVPVSSPKVAEMCKLFENIQRLVNISLVNELNILCEKLGIDFREALEAAATKPFGFTPYWPGPGIGGHCIPVDPLYFQWKARQLGQSSQLIEVAHMINEKMPQQIVTQVKELSAPPGTVFLIGIAYKKDVNDLRESPALPIIELLVNEGYKVQYHDPYISSAKIGDKIYDSIPLKKKTLEKADCILIVTDHSNIDWNICKGMKHVIDTRGVLKKVSA

[Multiple Choices]
A. 1.1.1.122
B. 1.1.1.136
C. 1.2.1.101
D. 2.1.1.395
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

> The supplied sequence exactly matches the 423-aa UniProt entry for this protein. That entry assigns EC 1.1.1.136 and records the catalytic activity with experimental evidence (ECO:0000269) linked to PubMed 20529859, supporting choice B.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> Sequence features may suggest a dehydrogenase, which is consistent with the 1.1.1 choices, but they do not establish which substrate-specific EC number applies.


**Missing item-specific fact**

> The protein's experimentally determined substrate and catalytic reaction—UDP-N-acetyl-D-glucosamine 6-dehydrogenation—are not supplied in the question.


**Reason**

> Distinguishing among the candidate dehydrogenase EC numbers requires protein-specific functional annotation or experimental knowledge absent from the sequence-and-choices input; recognizing the sequence or recalling its database entry would be lookup or memorization.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The choices specify distinct EC classifications, and the matched protein's supported classification is 1.1.1.136. The lack of enough input to infer it is an answerability limitation, not evidence that multiple options are correct.


### Important caveats

- The functional evidence is reported in UniProt with an experimental evidence code and a literature reference; the primary paper was not independently retrieved here.
- The exact sequence match and database identity are reviewer-only evidence, not information supplied to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Sequence features may suggest a dehydrogenase, which is consistent with the 1.1.1 choices, but they do not establish which substrate-specific EC number applies.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein's experimentally determined substrate and catalytic reaction—UDP-N-acetyl-D-glucosamine 6-dehydrogenation—are not supplied in the question.",
    "reason": "Distinguishing among the candidate dehydrogenase EC numbers requires protein-specific functional annotation or experimental knowledge absent from the sequence-and-choices input; recognizing the sequence or recalling its database entry would be lookup or memorization."
  },
  "case_id": "EC_number_0160",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the 423-aa UniProt entry for this protein. That entry assigns EC 1.1.1.136 and records the catalytic activity with experimental evidence (ECO:0000269) linked to PubMed 20529859, supporting choice B."
  },
  "important_caveats": [
    "The functional evidence is reported in UniProt with an experimental evidence code and a literature reference; the primary paper was not independently retrieved here.",
    "The exact sequence match and database identity are reviewer-only evidence, not information supplied to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The choices specify distinct EC classifications, and the matched protein's supported classification is 1.1.1.136. The lack of enough input to infer it is an answerability limitation, not evidence that multiple options are correct."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0160",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the 423-aa UniProt entry for this protein. That entry assigns EC 1.1.1.136 and records the catalytic activity with experimental evidence (ECO:0000269) linked to PubMed 20529859, supporting choice B.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "Sequence features may suggest a dehydrogenase, which is consistent with the 1.1.1 choices, but they do not establish which substrate-specific EC number applies.",
    "missing_item_specific_fact": "The protein's experimentally determined substrate and catalytic reaction—UDP-N-acetyl-D-glucosamine 6-dehydrogenation—are not supplied in the question.",
    "reason": "Distinguishing among the candidate dehydrogenase EC numbers requires protein-specific functional annotation or experimental knowledge absent from the sequence-and-choices input; recognizing the sequence or recalling its database entry would be lookup or memorization."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The choices specify distinct EC classifications, and the matched protein's supported classification is 1.1.1.136. The lack of enough input to infer it is an answerability limitation, not evidence that multiple options are correct."
  },
  "important_caveats": [
    "The functional evidence is reported in UniProt with an experimental evidence code and a literature reference; the primary paper was not independently retrieved here.",
    "The exact sequence match and database identity are reviewer-only evidence, not information supplied to the evaluated model."
  ]
}
```

</details>

## Before: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry A7GKX6 (sequence exactly matches the benchmark, 423 aa) annotates this protein as UDP-N-acetyl-D-glucosamine 6-dehydrogenase with EC 1.1.1.136, supported by experimental evidence (ECO:0000269, PubMed:20529859, J. Biol. Chem. 285:24825-24833, 2010). The catalytic reaction (UDP-GlcNAc + 2 NAD+ + H2O → UDP-2-acetamido-2-deoxy-α-D-glucuronate + 2 NADH + 3 H+) is confirmed. The sequence match is exact (SHA256 identical).

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The Rossmann-fold motif 'IGLGYVGLPLAIH' (GxGxxG-like) at the N-terminus is consistent with an NAD+-dependent dehydrogenase acting on a CH-OH group (EC 1.1.1.x), which provides partial reasoning support for eliminating option C (1.2.1.101, aldehyde dehydrogenase, different mechanism) and option D (2.1.1.395, methyltransferase, entirely different EC class). However, the critical distinction between option A (1.1.1.122, UDP-glucose 6-dehydrogenase) and option B (1.1.1.136, UDP-N-acetyl-D-glucosamine 6-dehydrogenase) hinges on whether the active site specifically accommodates the N-acetyl group at C2 of the sugar. Both are closely related SDR-type NAD-dependent dehydrogenases oxidizing the C6-OH of a UDP-sugar; the substrate-specificity residues that discriminate UDP-Glc from UDP-GlcNAc are protein-specific and cannot be reliably inferred from the linear sequence alone without structural or experimental knowledge.


**Missing item-specific fact**

> The precise active-site residues and substrate-binding geometry that distinguish UDP-Glc 6-dehydrogenase (1.1.1.122) from UDP-GlcNAc 6-dehydrogenase (1.1.1.136) for this particular protein. This requires knowledge of the specific enzyme's substrate specificity determined experimentally (PubMed:20529859) or by memorizing the database annotation for this sequence.


**Reason**

> While general fold recognition (Rossmann motif) can narrow the answer to 1.1.1.x, the final discrimination between the two 1.1.1.x options requires a protein-specific experimental fact about substrate specificity that is not derivable from the sequence through general biological reasoning.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "B"
]
```

> Options A (1.1.1.122) and B (1.1.1.136) are both NAD+-dependent dehydrogenases acting on the C6-OH of a UDP-sugar via a Rossmann-fold mechanism. From sequence alone, without specific active-site structural knowledge, a knowledgeable model could reasonably assign either UDP-Glc 6-DH or UDP-GlcNAc 6-DH. Options C and D are more clearly eliminable based on EC class (aldehyde dehydrogenase vs. methyltransferase).


### Important caveats

- The UniProt annotation carries experimental evidence (ECO:0000269) from a 2010 J. Biol. Chem. study, lending strong support to EC 1.1.1.136 for this specific sequence.
- The sequence-to-accession identity (A7GKX6) was inferred by the reviewer from dataset metadata; the evaluated model had no access to this identifier.
- The entry was first publicly released in Swiss-Prot on 2025-02-05, so it was not in older training corpora, reducing the likelihood of memorization from pre-2025 data.
- The Rossmann-fold reasoning for eliminating C and D is sound but does not resolve the A-vs-B distinction.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The Rossmann-fold motif 'IGLGYVGLPLAIH' (GxGxxG-like) at the N-terminus is consistent with an NAD+-dependent dehydrogenase acting on a CH-OH group (EC 1.1.1.x), which provides partial reasoning support for eliminating option C (1.2.1.101, aldehyde dehydrogenase, different mechanism) and option D (2.1.1.395, methyltransferase, entirely different EC class). However, the critical distinction between option A (1.1.1.122, UDP-glucose 6-dehydrogenase) and option B (1.1.1.136, UDP-N-acetyl-D-glucosamine 6-dehydrogenase) hinges on whether the active site specifically accommodates the N-acetyl group at C2 of the sugar. Both are closely related SDR-type NAD-dependent dehydrogenases oxidizing the C6-OH of a UDP-sugar; the substrate-specificity residues that discriminate UDP-Glc from UDP-GlcNAc are protein-specific and cannot be reliably inferred from the linear sequence alone without structural or experimental knowledge.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The precise active-site residues and substrate-binding geometry that distinguish UDP-Glc 6-dehydrogenase (1.1.1.122) from UDP-GlcNAc 6-dehydrogenase (1.1.1.136) for this particular protein. This requires knowledge of the specific enzyme's substrate specificity determined experimentally (PubMed:20529859) or by memorizing the database annotation for this sequence.",
    "reason": "While general fold recognition (Rossmann motif) can narrow the answer to 1.1.1.x, the final discrimination between the two 1.1.1.x options requires a protein-specific experimental fact about substrate specificity that is not derivable from the sequence through general biological reasoning."
  },
  "case_id": "EC_number_0160",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "UniProt entry A7GKX6 (sequence exactly matches the benchmark, 423 aa) annotates this protein as UDP-N-acetyl-D-glucosamine 6-dehydrogenase with EC 1.1.1.136, supported by experimental evidence (ECO:0000269, PubMed:20529859, J. Biol. Chem. 285:24825-24833, 2010). The catalytic reaction (UDP-GlcNAc + 2 NAD+ + H2O → UDP-2-acetamido-2-deoxy-α-D-glucuronate + 2 NADH + 3 H+) is confirmed. The sequence match is exact (SHA256 identical)."
  },
  "important_caveats": [
    "The UniProt annotation carries experimental evidence (ECO:0000269) from a 2010 J. Biol. Chem. study, lending strong support to EC 1.1.1.136 for this specific sequence.",
    "The sequence-to-accession identity (A7GKX6) was inferred by the reviewer from dataset metadata; the evaluated model had no access to this identifier.",
    "The entry was first publicly released in Swiss-Prot on 2025-02-05, so it was not in older training corpora, reducing the likelihood of memorization from pre-2025 data.",
    "The Rossmann-fold reasoning for eliminating C and D is sound but does not resolve the A-vs-B distinction."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "B"
    ],
    "reason": "Options A (1.1.1.122) and B (1.1.1.136) are both NAD+-dependent dehydrogenases acting on the C6-OH of a UDP-sugar via a Rossmann-fold mechanism. From sequence alone, without specific active-site structural knowledge, a knowledgeable model could reasonably assign either UDP-Glc 6-DH or UDP-GlcNAc 6-DH. Options C and D are more clearly eliminable based on EC class (aldehyde dehydrogenase vs. methyltransferase)."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0160",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry A7GKX6 (sequence exactly matches the benchmark, 423 aa) annotates this protein as UDP-N-acetyl-D-glucosamine 6-dehydrogenase with EC 1.1.1.136, supported by experimental evidence (ECO:0000269, PubMed:20529859, J. Biol. Chem. 285:24825-24833, 2010). The catalytic reaction (UDP-GlcNAc + 2 NAD+ + H2O → UDP-2-acetamido-2-deoxy-α-D-glucuronate + 2 NADH + 3 H+) is confirmed. The sequence match is exact (SHA256 identical).",
    "evidence_ids": ["C4", "C5", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The Rossmann-fold motif 'IGLGYVGLPLAIH' (GxGxxG-like) at the N-terminus is consistent with an NAD+-dependent dehydrogenase acting on a CH-OH group (EC 1.1.1.x), which provides partial reasoning support for eliminating option C (1.2.1.101, aldehyde dehydrogenase, different mechanism) and option D (2.1.1.395, methyltransferase, entirely different EC class). However, the critical distinction between option A (1.1.1.122, UDP-glucose 6-dehydrogenase) and option B (1.1.1.136, UDP-N-acetyl-D-glucosamine 6-dehydrogenase) hinges on whether the active site specifically accommodates the N-acetyl group at C2 of the sugar. Both are closely related SDR-type NAD-dependent dehydrogenases oxidizing the C6-OH of a UDP-sugar; the substrate-specificity residues that discriminate UDP-Glc from UDP-GlcNAc are protein-specific and cannot be reliably inferred from the linear sequence alone without structural or experimental knowledge.",
    "missing_item_specific_fact": "The precise active-site residues and substrate-binding geometry that distinguish UDP-Glc 6-dehydrogenase (1.1.1.122) from UDP-GlcNAc 6-dehydrogenase (1.1.1.136) for this particular protein. This requires knowledge of the specific enzyme's substrate specificity determined experimentally (PubMed:20529859) or by memorizing the database annotation for this sequence.",
    "reason": "While general fold recognition (Rossmann motif) can narrow the answer to 1.1.1.x, the final discrimination between the two 1.1.1.x options requires a protein-specific experimental fact about substrate specificity that is not derivable from the sequence through general biological reasoning."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "B"],
    "reason": "Options A (1.1.1.122) and B (1.1.1.136) are both NAD+-dependent dehydrogenases acting on the C6-OH of a UDP-sugar via a Rossmann-fold mechanism. From sequence alone, without specific active-site structural knowledge, a knowledgeable model could reasonably assign either UDP-Glc 6-DH or UDP-GlcNAc 6-DH. Options C and D are more clearly eliminable based on EC class (aldehyde dehydrogenase vs. methyltransferase)."
  },
  "important_caveats": [
    "The UniProt annotation carries experimental evidence (ECO:0000269) from a 2010 J. Biol. Chem. study, lending strong support to EC 1.1.1.136 for this specific sequence.",
    "The sequence-to-accession identity (A7GKX6) was inferred by the reviewer from dataset metadata; the evaluated model had no access to this identifier.",
    "The entry was first publicly released in Swiss-Prot on 2025-02-05, so it was not in older training corpora, reducing the likelihood of memorization from pre-2025 data.",
    "The Rossmann-fold reasoning for eliminating C and D is sound but does not resolve the A-vs-B distinction."
  ]
}
```

</details>

## After: GPT-6 Luna

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence matches the cited UniProt entry, which assigns EC 1.1.1.136 and identifies the enzyme as UDP-N-acetyl-D-glucosamine 6-dehydrogenase. The annotation links both the EC number and catalytic reaction to ECO:0000269 evidence from a cited publication, supporting the key for this sequence.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 423-aa sequence has the pattern of an NAD-dependent nucleotide-sugar dehydrogenase, including an N-terminal glycine-rich dinucleotide-binding region and a conserved catalytic region. Transferable knowledge of this enzyme family can distinguish it from the unrelated aldehyde dehydrogenase and methyltransferase choices (C and D); subfamily-level sequence similarity can further favor UDP-N-acetylglucosamine 6-dehydrogenase (B) over the closely related UDP-glucose 6-dehydrogenase (A).


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The complete sequence provides substantial evidence for family and subfamily recognition, so choosing among these alternatives has a meaningful basis in transferable sequence patterns. The close relationship between A and B makes the substrate-specific distinction less obvious from a short motif alone, but the full sequence permits a defensible homology-based inference.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> A is a close alternative in the same broad enzyme class, but the full sequence supports the more specific UDP-N-acetylglucosamine dehydrogenase assignment; no second option is comparably defensible.


### Important caveats

- The source annotation cites experimental evidence, but the underlying publication was not independently reviewed here.
- Reviewer-only source identity and annotation support the answer check; they are not inputs to the transferability judgment.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 423-aa sequence has the pattern of an NAD-dependent nucleotide-sugar dehydrogenase, including an N-terminal glycine-rich dinucleotide-binding region and a conserved catalytic region. Transferable knowledge of this enzyme family can distinguish it from the unrelated aldehyde dehydrogenase and methyltransferase choices (C and D); subfamily-level sequence similarity can further favor UDP-N-acetylglucosamine 6-dehydrogenase (B) over the closely related UDP-glucose 6-dehydrogenase (A).",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The complete sequence provides substantial evidence for family and subfamily recognition, so choosing among these alternatives has a meaningful basis in transferable sequence patterns. The close relationship between A and B makes the substrate-specific distinction less obvious from a short motif alone, but the full sequence permits a defensible homology-based inference."
  },
  "case_id": "EC_number_0160",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5"
    ],
    "judgment": "supported",
    "reason": "The sequence matches the cited UniProt entry, which assigns EC 1.1.1.136 and identifies the enzyme as UDP-N-acetyl-D-glucosamine 6-dehydrogenase. The annotation links both the EC number and catalytic reaction to ECO:0000269 evidence from a cited publication, supporting the key for this sequence."
  },
  "important_caveats": [
    "The source annotation cites experimental evidence, but the underlying publication was not independently reviewed here.",
    "Reviewer-only source identity and annotation support the answer check; they are not inputs to the transferability judgment."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "A is a close alternative in the same broad enzyme class, but the full sequence supports the more specific UDP-N-acetylglucosamine dehydrogenase assignment; no second option is comparably defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0160",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches the cited UniProt entry, which assigns EC 1.1.1.136 and identifies the enzyme as UDP-N-acetyl-D-glucosamine 6-dehydrogenase. The annotation links both the EC number and catalytic reaction to ECO:0000269 evidence from a cited publication, supporting the key for this sequence.",
    "evidence_ids": ["C4", "C5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 423-aa sequence has the pattern of an NAD-dependent nucleotide-sugar dehydrogenase, including an N-terminal glycine-rich dinucleotide-binding region and a conserved catalytic region. Transferable knowledge of this enzyme family can distinguish it from the unrelated aldehyde dehydrogenase and methyltransferase choices (C and D); subfamily-level sequence similarity can further favor UDP-N-acetylglucosamine 6-dehydrogenase (B) over the closely related UDP-glucose 6-dehydrogenase (A).",
    "missing_item_specific_fact": "",
    "reason": "The complete sequence provides substantial evidence for family and subfamily recognition, so choosing among these alternatives has a meaningful basis in transferable sequence patterns. The close relationship between A and B makes the substrate-specific distinction less obvious from a short motif alone, but the full sequence permits a defensible homology-based inference."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "A is a close alternative in the same broad enzyme class, but the full sequence supports the more specific UDP-N-acetylglucosamine dehydrogenase assignment; no second option is comparably defensible."
  },
  "important_caveats": [
    "The source annotation cites experimental evidence, but the underlying publication was not independently reviewed here.",
    "Reviewer-only source identity and annotation support the answer check; they are not inputs to the transferability judgment."
  ]
}
```

</details>

## After: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A7GKX6 (sequence matched, 423 aa) is annotated as UDP-N-acetyl-D-glucosamine 6-dehydrogenase with EC 1.1.1.136, supported by experimental evidence (ECO:0000269, PubMed 20529859, J. Biol. Chem. 285:24825-24833, 2010). The catalytic reaction is confirmed as UDP-N-acetyl-alpha-D-glucosamine + 2 NAD(+) + H2O → UDP-2-acetamido-2-deoxy-alpha-D-glucuronate + 2 NADH + 3 H(+). Choice B matches.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence displays canonical SDR (Short-chain Dehydrogenase/Reductase) features: a Rossmann-type NAD(P)-binding motif (GLGYVGLPL at the N-terminus) and the GDS catalytic motif (GDSYIPDVSSNVLKDLVQNK), placing this enzyme in EC class 1.1.1.x (oxidoreductase, CH-OH group, NAD+ acceptor). This eliminates C (1.2.1.101, aldehyde dehydrogenase, different fold) and D (2.1.1.395, methyltransferase, different fold). The critical distinction is between A (1.1.1.122, UDP-glucose 6-dehydrogenase) and B (1.1.1.136, UDP-GlcNAc 6-dehydrogenase). Both are SDR-type UDP-sugar dehydrogenases. However, the protein is 423 aa with an SDR catalytic core followed by a substantial C-terminal extension (~170+ residues beyond the ~250-aa SDR domain). Known UDP-glucose 6-dehydrogenases (EC 1.1.1.122) from plants, E. coli, and other bacteria are compact SDRs of ~250–270 aa. The extended architecture with additional C-terminal structural elements is a recognized feature of the bacterial UDP-GlcNAc 6-dehydrogenase subfamily (EC 1.1.1.136), where the extra domain contributes residues that form a deeper active-site pocket to accommodate the N-acetyl group of GlcNAc. This length-and-architecture argument, drawn from family-level knowledge of SDR superfamily members, meaningfully favors B over A.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The SDR fold identification eliminates C and D definitively. The distinction between A and B rests on the atypical 423-aa length with an extended C-terminal domain beyond the SDR core, which is a transferable family-level feature distinguishing bacterial UDP-GlcNAc 6-dehydrogenases from the shorter UDP-glucose 6-dehydrogenases. This is a probabilistic but concrete architectural inference, not a lookup of this specific protein's record.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A"
]
```

> Both A (1.1.1.122) and B (1.1.1.136) are SDR-type NAD-dependent UDP-sugar 6-dehydrogenases sharing the same EC class and fold. Without the length/architecture argument, a knowledgeable model could reasonably consider A as well. The length-based discrimination is probabilistic rather than definitive, as it is conceivable (though not observed in characterized examples) that a longer UDP-glucose 6-dehydrogenase could exist. Still, the offered alternatives make B the stronger inference.


### Important caveats

- The length-based argument (423 aa vs ~250 aa for typical UDP-Glc 6-DH) is the primary discriminator between A and B; it is a family-architecture regularity, not a sequence-motif proof.
- The specific residues that recognize the N-acetyl group of GlcNAc in the extended active-site pocket cannot be pinpointed from the raw sequence alone without structural knowledge of this subfamily.
- The experimental annotation (ECO:0000269) in the source confirms the answer, but this was reviewer-only evidence not available to the evaluated model.
- The protein is from Bacillus cytotoxicus (B. cereus group), but organism identity was not provided in the original input and should not be used as a discriminator.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence displays canonical SDR (Short-chain Dehydrogenase/Reductase) features: a Rossmann-type NAD(P)-binding motif (GLGYVGLPL at the N-terminus) and the GDS catalytic motif (GDSYIPDVSSNVLKDLVQNK), placing this enzyme in EC class 1.1.1.x (oxidoreductase, CH-OH group, NAD+ acceptor). This eliminates C (1.2.1.101, aldehyde dehydrogenase, different fold) and D (2.1.1.395, methyltransferase, different fold). The critical distinction is between A (1.1.1.122, UDP-glucose 6-dehydrogenase) and B (1.1.1.136, UDP-GlcNAc 6-dehydrogenase). Both are SDR-type UDP-sugar dehydrogenases. However, the protein is 423 aa with an SDR catalytic core followed by a substantial C-terminal extension (~170+ residues beyond the ~250-aa SDR domain). Known UDP-glucose 6-dehydrogenases (EC 1.1.1.122) from plants, E. coli, and other bacteria are compact SDRs of ~250–270 aa. The extended architecture with additional C-terminal structural elements is a recognized feature of the bacterial UDP-GlcNAc 6-dehydrogenase subfamily (EC 1.1.1.136), where the extra domain contributes residues that form a deeper active-site pocket to accommodate the N-acetyl group of GlcNAc. This length-and-architecture argument, drawn from family-level knowledge of SDR superfamily members, meaningfully favors B over A.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The SDR fold identification eliminates C and D definitively. The distinction between A and B rests on the atypical 423-aa length with an extended C-terminal domain beyond the SDR core, which is a transferable family-level feature distinguishing bacterial UDP-GlcNAc 6-dehydrogenases from the shorter UDP-glucose 6-dehydrogenases. This is a probabilistic but concrete architectural inference, not a lookup of this specific protein's record."
  },
  "case_id": "EC_number_0160",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry A7GKX6 (sequence matched, 423 aa) is annotated as UDP-N-acetyl-D-glucosamine 6-dehydrogenase with EC 1.1.1.136, supported by experimental evidence (ECO:0000269, PubMed 20529859, J. Biol. Chem. 285:24825-24833, 2010). The catalytic reaction is confirmed as UDP-N-acetyl-alpha-D-glucosamine + 2 NAD(+) + H2O → UDP-2-acetamido-2-deoxy-alpha-D-glucuronate + 2 NADH + 3 H(+). Choice B matches."
  },
  "important_caveats": [
    "The length-based argument (423 aa vs ~250 aa for typical UDP-Glc 6-DH) is the primary discriminator between A and B; it is a family-architecture regularity, not a sequence-motif proof.",
    "The specific residues that recognize the N-acetyl group of GlcNAc in the extended active-site pocket cannot be pinpointed from the raw sequence alone without structural knowledge of this subfamily.",
    "The experimental annotation (ECO:0000269) in the source confirms the answer, but this was reviewer-only evidence not available to the evaluated model.",
    "The protein is from Bacillus cytotoxicus (B. cereus group), but organism identity was not provided in the original input and should not be used as a discriminator."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A"
    ],
    "reason": "Both A (1.1.1.122) and B (1.1.1.136) are SDR-type NAD-dependent UDP-sugar 6-dehydrogenases sharing the same EC class and fold. Without the length/architecture argument, a knowledgeable model could reasonably consider A as well. The length-based discrimination is probabilistic rather than definitive, as it is conceivable (though not observed in characterized examples) that a longer UDP-glucose 6-dehydrogenase could exist. Still, the offered alternatives make B the stronger inference."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0160",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A7GKX6 (sequence matched, 423 aa) is annotated as UDP-N-acetyl-D-glucosamine 6-dehydrogenase with EC 1.1.1.136, supported by experimental evidence (ECO:0000269, PubMed 20529859, J. Biol. Chem. 285:24825-24833, 2010). The catalytic reaction is confirmed as UDP-N-acetyl-alpha-D-glucosamine + 2 NAD(+) + H2O → UDP-2-acetamido-2-deoxy-alpha-D-glucuronate + 2 NADH + 3 H(+). Choice B matches.",
    "evidence_ids": ["C4", "C5", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence displays canonical SDR (Short-chain Dehydrogenase/Reductase) features: a Rossmann-type NAD(P)-binding motif (GLGYVGLPL at the N-terminus) and the GDS catalytic motif (GDSYIPDVSSNVLKDLVQNK), placing this enzyme in EC class 1.1.1.x (oxidoreductase, CH-OH group, NAD+ acceptor). This eliminates C (1.2.1.101, aldehyde dehydrogenase, different fold) and D (2.1.1.395, methyltransferase, different fold). The critical distinction is between A (1.1.1.122, UDP-glucose 6-dehydrogenase) and B (1.1.1.136, UDP-GlcNAc 6-dehydrogenase). Both are SDR-type UDP-sugar dehydrogenases. However, the protein is 423 aa with an SDR catalytic core followed by a substantial C-terminal extension (~170+ residues beyond the ~250-aa SDR domain). Known UDP-glucose 6-dehydrogenases (EC 1.1.1.122) from plants, E. coli, and other bacteria are compact SDRs of ~250–270 aa. The extended architecture with additional C-terminal structural elements is a recognized feature of the bacterial UDP-GlcNAc 6-dehydrogenase subfamily (EC 1.1.1.136), where the extra domain contributes residues that form a deeper active-site pocket to accommodate the N-acetyl group of GlcNAc. This length-and-architecture argument, drawn from family-level knowledge of SDR superfamily members, meaningfully favors B over A.",
    "missing_item_specific_fact": "",
    "reason": "The SDR fold identification eliminates C and D definitively. The distinction between A and B rests on the atypical 423-aa length with an extended C-terminal domain beyond the SDR core, which is a transferable family-level feature distinguishing bacterial UDP-GlcNAc 6-dehydrogenases from the shorter UDP-glucose 6-dehydrogenases. This is a probabilistic but concrete architectural inference, not a lookup of this specific protein's record."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A"],
    "reason": "Both A (1.1.1.122) and B (1.1.1.136) are SDR-type NAD-dependent UDP-sugar 6-dehydrogenases sharing the same EC class and fold. Without the length/architecture argument, a knowledgeable model could reasonably consider A as well. The length-based discrimination is probabilistic rather than definitive, as it is conceivable (though not observed in characterized examples) that a longer UDP-glucose 6-dehydrogenase could exist. Still, the offered alternatives make B the stronger inference."
  },
  "important_caveats": [
    "The length-based argument (423 aa vs ~250 aa for typical UDP-Glc 6-DH) is the primary discriminator between A and B; it is a family-architecture regularity, not a sequence-motif proof.",
    "The specific residues that recognize the N-acetyl group of GlcNAc in the extended active-site pocket cannot be pinpointed from the raw sequence alone without structural knowledge of this subfamily.",
    "The experimental annotation (ECO:0000269) in the source confirms the answer, but this was reviewer-only evidence not available to the evaluated model.",
    "The protein is from Bacillus cytotoxicus (B. cereus group), but organism identity was not provided in the original input and should not be used as a discriminator."
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
  "requested_accession": "A7GKX6",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "benchmark_sequence_sha256": "5bad7e65801ec8cb99f507e9a58146ea70fefa83160d8597748c30f9b3364a8a",
  "benchmark_sequence_length": 423,
  "current_status": "retrieved",
  "current_sequence_comparison": "matched",
  "current_entry_audit": {
    "entryVersion": 98,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2007-09-11",
    "sequenceVersion": 1
  },
  "current_uniprot_release": "2026_03",
  "current_record_sha256": "68eff0a78e5c0dadd87ed867729ca5fa907f1022d5a7d7c02ac69e250707cc4f",
  "current_source_sequence_sha256": "5bad7e65801ec8cb99f507e9a58146ea70fefa83160d8597748c30f9b3364a8a",
  "current_source_sequence_length": 423,
  "historical_status": "retrieved",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "selected_historical_entry_version": 96,
  "selected_historical_version": {
    "accession": "A7GKX6",
    "database": "Swiss-Prot",
    "entryVersion": 96,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "UGNAD_BACCN",
    "sequenceVersion": 1
  },
  "selected_historical_record_sha256": "d8a31aa88fd823d2c4ea18977d36968e48e5c0bbc7cb1fe4c9e6ca7171435666",
  "selected_historical_source_sequence_sha256": "5bad7e65801ec8cb99f507e9a58146ea70fefa83160d8597748c30f9b3364a8a",
  "selected_historical_source_sequence_length": 423,
  "latest_at_cutoff_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 96,
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A7GKX6.json)

```json
{
  "evidence_id": "C1",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A7GKX6.json",
  "source_sha256": "68eff0a78e5c0dadd87ed867729ca5fa907f1022d5a7d7c02ac69e250707cc4f",
  "retrieved_utc": "2026-11-02T04:27:09.484643+00:00",
  "json_pointer": "/primaryAccession",
  "excerpt": "\"A7GKX6\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A7GKX6.json)

```json
{
  "evidence_id": "C2",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A7GKX6.json",
  "source_sha256": "68eff0a78e5c0dadd87ed867729ca5fa907f1022d5a7d7c02ac69e250707cc4f",
  "retrieved_utc": "2026-11-02T04:27:09.484643+00:00",
  "json_pointer": "/entryAudit",
  "excerpt": "{\"entryVersion\":98,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2007-09-11\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A7GKX6.json)

```json
{
  "evidence_id": "C3",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A7GKX6.json",
  "source_sha256": "68eff0a78e5c0dadd87ed867729ca5fa907f1022d5a7d7c02ac69e250707cc4f",
  "retrieved_utc": "2026-11-02T04:27:09.484643+00:00",
  "json_pointer": "/organism",
  "excerpt": "{\"lineage\":[\"Bacteria\",\"Bacillati\",\"Bacillota\",\"Bacilli\",\"Caryophanales\",\"Bacillaceae\",\"Bacillus\",\"Bacillus cereus group\"],\"scientificName\":\"Bacillus cytotoxicus (strain DSM 22905 / CIP 110041 / 391-98 / NVH 391-98)\",\"taxonId\":315749}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A7GKX6.json)

```json
{
  "evidence_id": "C4",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A7GKX6.json",
  "source_sha256": "68eff0a78e5c0dadd87ed867729ca5fa907f1022d5a7d7c02ac69e250707cc4f",
  "retrieved_utc": "2026-11-02T04:27:09.484643+00:00",
  "json_pointer": "/proteinDescription",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"20529859\",\"source\":\"PubMed\"}],\"value\":\"1.1.1.136\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"20529859\",\"source\":\"PubMed\"}],\"value\":\"UDP-N-acetyl-D-glucosamine 6-dehydrogenase\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"20529859\",\"source\":\"PubMed\"}],\"value\":\"UDP-GlcNAc 6-dehydrogenase\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A7GKX6.json)

```json
{
  "evidence_id": "C5",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A7GKX6.json",
  "source_sha256": "68eff0a78e5c0dadd87ed867729ca5fa907f1022d5a7d7c02ac69e250707cc4f",
  "retrieved_utc": "2026-11-02T04:27:09.484643+00:00",
  "json_pointer": "/comments/1",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"20529859\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:13326\"}}],\"reaction\":{\"ecNumber\":\"1.1.1.136\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"20529859\",\"source\":\"PubMed\"}],\"name\":\"UDP-N-acetyl-alpha-D-glucosamine + 2 NAD(+) + H2O = UDP-2-acetamido-2-deoxy-alpha-D-glucuronate + 2 NADH + 3 H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:13325\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57540\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57705\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57945\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:65040\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A7GKX6.json)

```json
{
  "evidence_id": "C6",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A7GKX6.json",
  "source_sha256": "68eff0a78e5c0dadd87ed867729ca5fa907f1022d5a7d7c02ac69e250707cc4f",
  "retrieved_utc": "2026-11-02T04:27:09.484643+00:00",
  "json_pointer": "/references/1",
  "excerpt": "{\"citation\":{\"authors\":[\"Gu X.\",\"Glushka J.\",\"Lee S.G.\",\"Bar-Peled M.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"20529859\"},{\"database\":\"DOI\",\"id\":\"10.1074/jbc.m110.125872\"}],\"citationType\":\"journal article\",\"firstPage\":\"24825\",\"id\":\"20529859\",\"journal\":\"J. Biol. Chem.\",\"lastPage\":\"24833\",\"publicationDate\":\"2010\",\"title\":\"Biosynthesis of a new UDP-sugar, UDP-2-acetamido-2-deoxyxylose, in the human pathogen Bacillus cereus subspecies cytotoxis NVH 391-98.\",\"volume\":\"285\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"ADE43879.1\",\"source\":\"EMBL\"}],\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"DSM 22905 / CIP 110041 / 391-98 / NVH 391-98\"}],\"referenceNumber\":2,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [GENOMIC DNA]\",\"FUNCTION\",\"CATALYTIC ACTIVITY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A7GKX6?format=txt&versions=96)

```json
{
  "evidence_id": "H1",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A7GKX6?format=txt&versions=96",
  "source_sha256": "d8a31aa88fd823d2c4ea18977d36968e48e5c0bbc7cb1fe4c9e6ca7171435666",
  "retrieved_utc": "2026-11-02T04:27:11.633421+00:00",
  "source_locator": "lines 1-14",
  "excerpt": "ID   UGNAD_BACCN             Reviewed;         423 AA.\nAC   A7GKX6;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   11-SEP-2007, sequence version 1.\nDT   28-JAN-2026, entry version 96.\nDE   RecName: Full=UDP-N-acetyl-D-glucosamine 6-dehydrogenase {ECO:0000303|PubMed:20529859};\nDE            Short=UDP-GlcNAc 6-dehydrogenase {ECO:0000303|PubMed:20529859};\nDE            EC=1.1.1.136 {ECO:0000269|PubMed:20529859};\nGN   Name=UGlcNAcDH {ECO:0000303|PubMed:20529859};\nGN   OrderedLocusNames=Bcer98_0429 {ECO:0000312|EMBL:ABS20784.1};\nOS   Bacillus cytotoxicus (strain DSM 22905 / CIP 110041 / 391-98 / NVH 391-98).\nOC   Bacteria; Bacillati; Bacillota; Bacilli; Bacillales; Bacillaceae; Bacillus;\nOC   Bacillus cereus group.\nOX   NCBI_TaxID=315749;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 96,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A7GKX6?format=txt&versions=96)

```json
{
  "evidence_id": "H2",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A7GKX6?format=txt&versions=96",
  "source_sha256": "d8a31aa88fd823d2c4ea18977d36968e48e5c0bbc7cb1fe4c9e6ca7171435666",
  "retrieved_utc": "2026-11-02T04:27:11.633421+00:00",
  "source_locator": "lines 6-8",
  "excerpt": "DE   RecName: Full=UDP-N-acetyl-D-glucosamine 6-dehydrogenase {ECO:0000303|PubMed:20529859};\nDE            Short=UDP-GlcNAc 6-dehydrogenase {ECO:0000303|PubMed:20529859};\nDE            EC=1.1.1.136 {ECO:0000269|PubMed:20529859};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 96,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A7GKX6?format=txt&versions=96)

```json
{
  "evidence_id": "H3",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A7GKX6?format=txt&versions=96",
  "source_sha256": "d8a31aa88fd823d2c4ea18977d36968e48e5c0bbc7cb1fe4c9e6ca7171435666",
  "retrieved_utc": "2026-11-02T04:27:11.633421+00:00",
  "source_locator": "lines 26-33",
  "excerpt": "RN   [2] {ECO:0000312|EMBL:ADE43879.1}\nRP   NUCLEOTIDE SEQUENCE [GENOMIC DNA], FUNCTION, AND CATALYTIC ACTIVITY.\nRC   STRAIN=DSM 22905 / CIP 110041 / 391-98 / NVH 391-98;\nRX   PubMed=20529859; DOI=10.1074/jbc.m110.125872;\nRA   Gu X., Glushka J., Lee S.G., Bar-Peled M.;\nRT   \"Biosynthesis of a new UDP-sugar, UDP-2-acetamido-2-deoxyxylose, in the\nRT   human pathogen Bacillus cereus subspecies cytotoxis NVH 391-98.\";\nRL   J. Biol. Chem. 285:24825-24833(2010).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 96,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A7GKX6?format=txt&versions=96)

```json
{
  "evidence_id": "H4",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A7GKX6?format=txt&versions=96",
  "source_sha256": "d8a31aa88fd823d2c4ea18977d36968e48e5c0bbc7cb1fe4c9e6ca7171435666",
  "retrieved_utc": "2026-11-02T04:27:11.633421+00:00",
  "source_locator": "lines 40-48",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=UDP-N-acetyl-alpha-D-glucosamine + 2 NAD(+) + H2O = UDP-2-\nCC         acetamido-2-deoxy-alpha-D-glucuronate + 2 NADH + 3 H(+);\nCC         Xref=Rhea:RHEA:13325, ChEBI:CHEBI:15377, ChEBI:CHEBI:15378,\nCC         ChEBI:CHEBI:57540, ChEBI:CHEBI:57705, ChEBI:CHEBI:57945,\nCC         ChEBI:CHEBI:65040; EC=1.1.1.136;\nCC         Evidence={ECO:0000269|PubMed:20529859};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:13326;\nCC         Evidence={ECO:0000269|PubMed:20529859};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 96,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 160. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
