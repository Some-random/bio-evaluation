# EC_number_0078: before and after transfer clarification

[All 1,328 cases](../README.md) · [Method](../METHOD.md) · [Summary](../SUMMARY.md) · [Exact reviewer user message](../inputs/EC_number_0078.txt)

**Task:** `EC_number`  
**Author key, unchanged:** **B** — 2.1.1.27

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
MGSYHDEKNVMGGSDQGELCSLAMTIASGSVPAMVLKALIELDVLELIKRAGPGAQLSPAQIVAQLPTKNPDAGTMLDRMLRLLASYEILSCSTQTLPDGRVERLYGLAPVCQFFTNNEDGATLGAIVQLSQEKLVVESWYHLKDAVLDGGIPFKKAQGMTIYEYPKTDPRFNQVFNSGMSNYSTIIMRDLLERYKGFEGISTLVDIAGGTGASINMVVSKYPTIKGINFDLPHVIKDAPSYDGVEHVGGDMFESVTKADAMLIKWTLCDWSDEHCLKLLKNCYNALPDNGKVIVCDYVLPMAPETSNAAKTVFLLDAIMLANFVGGKGRTKQEFEALARKVGFEGFEVPCSSYDFSVMELFKKKNN

[Multiple Choices]
A. 2.1.1.353
B. 2.1.1.27
C. 5.4.99.14
D. 2.5.1.76
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

> The exact sequence matches the cited UniProt entry, which assigns EC 2.1.1.27 and records the tyramine + SAM methylation reaction with PubMed experimental evidence. The historical entry also contains this assignment.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence may support a broad methyltransferase inference, but that does not establish the exact substrate specificity or distinguish EC 2.1.1.27 from another methyltransferase option.


**Missing item-specific fact**

> The protein's demonstrated reaction—methyl transfer from SAM to tyramine and related amines—is not supplied in the question.


**Reason**

> Choosing the precise four-part EC number depends on protein-specific substrate and reaction evidence absent from the sequence prompt; recognizing the sequence or recalling its annotation would be lookup or memorization.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Reviewer-only evidence supports B for this exact sequence, though the input alone does not establish that specific EC assignment.


### Important caveats

- The cited UniProt entry and sequence match are reviewer-only information, not information available to the evaluated model.
- The EC assignment is supported by a recorded experimental-evidence citation; the primary papers were not independently reviewed here.
- The author's exact source snapshot is unknown, but a historical entry within the stated cutoff also matches the sequence and gives the same EC assignment.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence may support a broad methyltransferase inference, but that does not establish the exact substrate specificity or distinguish EC 2.1.1.27 from another methyltransferase option.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein's demonstrated reaction—methyl transfer from SAM to tyramine and related amines—is not supplied in the question.",
    "reason": "Choosing the precise four-part EC number depends on protein-specific substrate and reaction evidence absent from the sequence prompt; recognizing the sequence or recalling its annotation would be lookup or memorization."
  },
  "case_id": "EC_number_0078",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H2",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the cited UniProt entry, which assigns EC 2.1.1.27 and records the tyramine + SAM methylation reaction with PubMed experimental evidence. The historical entry also contains this assignment."
  },
  "important_caveats": [
    "The cited UniProt entry and sequence match are reviewer-only information, not information available to the evaluated model.",
    "The EC assignment is supported by a recorded experimental-evidence citation; the primary papers were not independently reviewed here.",
    "The author's exact source snapshot is unknown, but a historical entry within the stated cutoff also matches the sequence and gives the same EC assignment."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Reviewer-only evidence supports B for this exact sequence, though the input alone does not establish that specific EC assignment."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0078",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the cited UniProt entry, which assigns EC 2.1.1.27 and records the tyramine + SAM methylation reaction with PubMed experimental evidence. The historical entry also contains this assignment.",
    "evidence_ids": ["C1", "C4", "C5", "H2", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence may support a broad methyltransferase inference, but that does not establish the exact substrate specificity or distinguish EC 2.1.1.27 from another methyltransferase option.",
    "missing_item_specific_fact": "The protein's demonstrated reaction—methyl transfer from SAM to tyramine and related amines—is not supplied in the question.",
    "reason": "Choosing the precise four-part EC number depends on protein-specific substrate and reaction evidence absent from the sequence prompt; recognizing the sequence or recalling its annotation would be lookup or memorization."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Reviewer-only evidence supports B for this exact sequence, though the input alone does not establish that specific EC assignment."
  },
  "important_caveats": [
    "The cited UniProt entry and sequence match are reviewer-only information, not information available to the evaluated model.",
    "The EC assignment is supported by a recorded experimental-evidence citation; the primary papers were not independently reviewed here.",
    "The author's exact source snapshot is unknown, but a historical entry within the stated cutoff also matches the sequence and gives the same EC assignment."
  ]
}
```

</details>

## Before: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A0AA51VIL7 (sequence SHA256 matched) explicitly annotates EC=2.1.1.27 (Tyramine N-methyltransferase 1) with evidence codes ECO:0000269 (PubMed:38835170, experimental) and ECO:0000255 (PROSITE-ProRule PRU01020). The catalytic reaction 'tyramine + SAM = N-methyltyramine + SAH + H+' is confirmed by experimental evidence. The sequence matches the benchmark input exactly.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H5](#evidence-h5), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence contains a VQEGFEG motif (~residues 290-296) characteristic of plant class-I SAM-dependent methyltransferases, which could help eliminate C (isomerase, EC 5.4.99.14) and D (alkyl/aryl transferase, EC 2.5.1.76). However, this motif is shared by both O-methyltransferases and N-methyltransferases in plants. The enzyme was initially misnamed 'O-methyltransferase 4' (LwOMT4) and only reclassified as an N-methyltransferase (EC 2.1.1.27) through experimental substrate assays (PubMed:38835170, 2024). Distinguishing 2.1.1.27 from 2.1.1.353 (another specific methyltransferase) from sequence alone is not feasible.


**Missing item-specific fact**

> The specific experimental determination that this enzyme catalyzes N-methylation of tyramine (rather than O-methylation or methylation of another substrate) required in vitro enzyme assays and product identification (PubMed:38835170, PubMed:37675639). No sequence motif in the provided 367-aa sequence uniquely identifies tyramine as the substrate or nitrogen as the methylation acceptor.


**Reason**

> While general methyltransferase motifs allow elimination of C and D, the final choice between A (2.1.1.353) and B (2.1.1.27) depends entirely on the experimentally determined substrate specificity of this particular peyote enzyme. The PROSITE-ProRule PRU01020 only confirms the general SAM-dependent methyltransferase fold, not the specific reaction. This is a recently characterized enzyme (first published 2023-2024) whose EC assignment was resolved only through targeted biochemical experiments.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "B"
]
```

> Both A (2.1.1.353) and B (2.1.1.27) are methyltransferases. Without experimental knowledge of this enzyme's specific substrate (tyramine) and methylation position (nitrogen), a model relying solely on sequence features would see a typical plant SAM-dependent methyltransferase with the VQEGFEG motif and could plausibly assign either EC number. The initial annotation of this enzyme as 'O-methyltransferase 4' further confounds sequence-based inference.


### Important caveats

- The UniProt annotation carries ECO:0000269 (PubMed) evidence, indicating experimental validation, not mere computational prediction.
- The enzyme was initially misclassified as an O-methyltransferase (LwOMT4) in the 2023 paper and only reclassified as an N-methyltransferase (LwNMT1, EC 2.1.1.27) in the 2024 paper, making sequence-based inference particularly unreliable for this entry.
- The PROSITE-ProRule PRU01020 evidence (ECO:0000255) only supports the general methyltransferase classification, not the specific EC 2.1.1.27 assignment.
- The sequence is from a recently characterized enzyme (first public release 2025-06-18), limiting the training data available to models for this specific entry.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a VQEGFEG motif (~residues 290-296) characteristic of plant class-I SAM-dependent methyltransferases, which could help eliminate C (isomerase, EC 5.4.99.14) and D (alkyl/aryl transferase, EC 2.5.1.76). However, this motif is shared by both O-methyltransferases and N-methyltransferases in plants. The enzyme was initially misnamed 'O-methyltransferase 4' (LwOMT4) and only reclassified as an N-methyltransferase (EC 2.1.1.27) through experimental substrate assays (PubMed:38835170, 2024). Distinguishing 2.1.1.27 from 2.1.1.353 (another specific methyltransferase) from sequence alone is not feasible.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific experimental determination that this enzyme catalyzes N-methylation of tyramine (rather than O-methylation or methylation of another substrate) required in vitro enzyme assays and product identification (PubMed:38835170, PubMed:37675639). No sequence motif in the provided 367-aa sequence uniquely identifies tyramine as the substrate or nitrogen as the methylation acceptor.",
    "reason": "While general methyltransferase motifs allow elimination of C and D, the final choice between A (2.1.1.353) and B (2.1.1.27) depends entirely on the experimentally determined substrate specificity of this particular peyote enzyme. The PROSITE-ProRule PRU01020 only confirms the general SAM-dependent methyltransferase fold, not the specific reaction. This is a recently characterized enzyme (first published 2023-2024) whose EC assignment was resolved only through targeted biochemical experiments."
  },
  "case_id": "EC_number_0078",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2",
      "H5",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry A0AA51VIL7 (sequence SHA256 matched) explicitly annotates EC=2.1.1.27 (Tyramine N-methyltransferase 1) with evidence codes ECO:0000269 (PubMed:38835170, experimental) and ECO:0000255 (PROSITE-ProRule PRU01020). The catalytic reaction 'tyramine + SAM = N-methyltyramine + SAH + H+' is confirmed by experimental evidence. The sequence matches the benchmark input exactly."
  },
  "important_caveats": [
    "The UniProt annotation carries ECO:0000269 (PubMed) evidence, indicating experimental validation, not mere computational prediction.",
    "The enzyme was initially misclassified as an O-methyltransferase (LwOMT4) in the 2023 paper and only reclassified as an N-methyltransferase (LwNMT1, EC 2.1.1.27) in the 2024 paper, making sequence-based inference particularly unreliable for this entry.",
    "The PROSITE-ProRule PRU01020 evidence (ECO:0000255) only supports the general methyltransferase classification, not the specific EC 2.1.1.27 assignment.",
    "The sequence is from a recently characterized enzyme (first public release 2025-06-18), limiting the training data available to models for this specific entry."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "B"
    ],
    "reason": "Both A (2.1.1.353) and B (2.1.1.27) are methyltransferases. Without experimental knowledge of this enzyme's specific substrate (tyramine) and methylation position (nitrogen), a model relying solely on sequence features would see a typical plant SAM-dependent methyltransferase with the VQEGFEG motif and could plausibly assign either EC number. The initial annotation of this enzyme as 'O-methyltransferase 4' further confounds sequence-based inference."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0078",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A0AA51VIL7 (sequence SHA256 matched) explicitly annotates EC=2.1.1.27 (Tyramine N-methyltransferase 1) with evidence codes ECO:0000269 (PubMed:38835170, experimental) and ECO:0000255 (PROSITE-ProRule PRU01020). The catalytic reaction 'tyramine + SAM = N-methyltyramine + SAH + H+' is confirmed by experimental evidence. The sequence matches the benchmark input exactly.",
    "evidence_ids": ["C4", "C5", "H2", "H5", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence contains a VQEGFEG motif (~residues 290-296) characteristic of plant class-I SAM-dependent methyltransferases, which could help eliminate C (isomerase, EC 5.4.99.14) and D (alkyl/aryl transferase, EC 2.5.1.76). However, this motif is shared by both O-methyltransferases and N-methyltransferases in plants. The enzyme was initially misnamed 'O-methyltransferase 4' (LwOMT4) and only reclassified as an N-methyltransferase (EC 2.1.1.27) through experimental substrate assays (PubMed:38835170, 2024). Distinguishing 2.1.1.27 from 2.1.1.353 (another specific methyltransferase) from sequence alone is not feasible.",
    "missing_item_specific_fact": "The specific experimental determination that this enzyme catalyzes N-methylation of tyramine (rather than O-methylation or methylation of another substrate) required in vitro enzyme assays and product identification (PubMed:38835170, PubMed:37675639). No sequence motif in the provided 367-aa sequence uniquely identifies tyramine as the substrate or nitrogen as the methylation acceptor.",
    "reason": "While general methyltransferase motifs allow elimination of C and D, the final choice between A (2.1.1.353) and B (2.1.1.27) depends entirely on the experimentally determined substrate specificity of this particular peyote enzyme. The PROSITE-ProRule PRU01020 only confirms the general SAM-dependent methyltransferase fold, not the specific reaction. This is a recently characterized enzyme (first published 2023-2024) whose EC assignment was resolved only through targeted biochemical experiments."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "B"],
    "reason": "Both A (2.1.1.353) and B (2.1.1.27) are methyltransferases. Without experimental knowledge of this enzyme's specific substrate (tyramine) and methylation position (nitrogen), a model relying solely on sequence features would see a typical plant SAM-dependent methyltransferase with the VQEGFEG motif and could plausibly assign either EC number. The initial annotation of this enzyme as 'O-methyltransferase 4' further confounds sequence-based inference."
  },
  "important_caveats": [
    "The UniProt annotation carries ECO:0000269 (PubMed) evidence, indicating experimental validation, not mere computational prediction.",
    "The enzyme was initially misclassified as an O-methyltransferase (LwOMT4) in the 2023 paper and only reclassified as an N-methyltransferase (LwNMT1, EC 2.1.1.27) in the 2024 paper, making sequence-based inference particularly unreliable for this entry.",
    "The PROSITE-ProRule PRU01020 evidence (ECO:0000255) only supports the general methyltransferase classification, not the specific EC 2.1.1.27 assignment.",
    "The sequence is from a recently characterized enzyme (first public release 2025-06-18), limiting the training data available to models for this specific entry."
  ]
}
```

</details>

## After: GPT-6 Luna

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The matched sequence is annotated EC 2.1.1.27, and the catalytic-activity annotation reports tyramine methylation with experimental evidence cited to PubMed. This supports the keyed EC, while the source excerpts do not independently reproduce the experiments.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence is consistent with a SAM-dependent methyltransferase, which plausibly separates choices A and B from the mutase and prenyltransferase choices C and D. But A and B are both EC 2.1.1 methyltransferases; the broad methyltransferase-family signal does not establish the specific substrate activity needed to choose between them.


**Missing item-specific fact**

> The target's substrate specificity or a reliable homolog/function annotation sufficient to establish its precise EC assignment.


**Reason**

> The sequence supports a general methyltransferase inference, but the offered alternatives include two methyltransferase EC numbers. Distinguishing those exact activities requires more specific functional evidence than the broad family-level signal provides.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The evidence supports B as the target's EC number; no second option is established as a valid EC assignment for this protein. The limitation is sequence-only discrimination, not evidence that multiple answers are correct.


### Important caveats

- The reviewer-only records match the supplied sequence, but the author's exact source snapshot is unknown.
- The cited source annotation reports experimental evidence; the primary studies were not independently reviewed here.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with a SAM-dependent methyltransferase, which plausibly separates choices A and B from the mutase and prenyltransferase choices C and D. But A and B are both EC 2.1.1 methyltransferases; the broad methyltransferase-family signal does not establish the specific substrate activity needed to choose between them.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The target's substrate specificity or a reliable homolog/function annotation sufficient to establish its precise EC assignment.",
    "reason": "The sequence supports a general methyltransferase inference, but the offered alternatives include two methyltransferase EC numbers. Distinguishing those exact activities requires more specific functional evidence than the broad family-level signal provides."
  },
  "case_id": "EC_number_0078",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The matched sequence is annotated EC 2.1.1.27, and the catalytic-activity annotation reports tyramine methylation with experimental evidence cited to PubMed. This supports the keyed EC, while the source excerpts do not independently reproduce the experiments."
  },
  "important_caveats": [
    "The reviewer-only records match the supplied sequence, but the author's exact source snapshot is unknown.",
    "The cited source annotation reports experimental evidence; the primary studies were not independently reviewed here."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The evidence supports B as the target's EC number; no second option is established as a valid EC assignment for this protein. The limitation is sequence-only discrimination, not evidence that multiple answers are correct."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0078",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The matched sequence is annotated EC 2.1.1.27, and the catalytic-activity annotation reports tyramine methylation with experimental evidence cited to PubMed. This supports the keyed EC, while the source excerpts do not independently reproduce the experiments.",
    "evidence_ids": ["C4", "C5", "H2", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence is consistent with a SAM-dependent methyltransferase, which plausibly separates choices A and B from the mutase and prenyltransferase choices C and D. But A and B are both EC 2.1.1 methyltransferases; the broad methyltransferase-family signal does not establish the specific substrate activity needed to choose between them.",
    "missing_item_specific_fact": "The target's substrate specificity or a reliable homolog/function annotation sufficient to establish its precise EC assignment.",
    "reason": "The sequence supports a general methyltransferase inference, but the offered alternatives include two methyltransferase EC numbers. Distinguishing those exact activities requires more specific functional evidence than the broad family-level signal provides."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The evidence supports B as the target's EC number; no second option is established as a valid EC assignment for this protein. The limitation is sequence-only discrimination, not evidence that multiple answers are correct."
  },
  "important_caveats": [
    "The reviewer-only records match the supplied sequence, but the author's exact source snapshot is unknown.",
    "The cited source annotation reports experimental evidence; the primary studies were not independently reviewed here."
  ]
}
```

</details>

## After: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The reviewer-only evidence confirms the sequence matches UniProt A0AA51VIL7 (NMT1_LOPWI), annotated as Tyramine N-methyltransferase 1 with EC 2.1.1.27. The EC assignment is supported by both PROSITE-ProRule PRU01020 (computational, ECO:0000255) and experimental evidence (ECO:0000269, PubMed:38835170). Multiple catalytic activities are documented showing N-methyltransferase activity on tyramine, dopamine, mescaline, and various phenethylamine substrates using SAM as methyl donor. The reaction 'tyramine + SAM = N-methyltyramine + SAH + H+' is the canonical EC 2.1.1.27 reaction.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C17](#evidence-c17), [H1](#evidence-h1), [H2](#evidence-h2), [H5](#evidence-h5), [H6](#evidence-h6), [H7](#evidence-h7), [H17](#evidence-h17).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains hallmark SAM-dependent methyltransferase motifs: the 'VDIAGGTGASIN' region (~residues 188-200) includes the diagnostic GAS (Gly-Ala-Ser) motif of the Rossmann-like fold found in class I SAM-dependent methyltransferases. This immediately places the enzyme in EC 2.1.1 (methyltransferases transferring one-carbon groups), eliminating C (5.4.99.14, an isomerase) and D (2.5.1.76, an alkyl/aryl transferase with a different catalytic mechanism and fold). Among EC 2.1.1 options, the PROSITE-ProRule PRU01020 is a well-known pattern signature specifically for tyramine N-methyltransferases (PNMTs) in plants. Plant phenethylamine N-methyltransferases are a well-characterized family (~350-400 aa, specific active-site residues) involved in alkaloid biosynthesis pathways including mescaline production in Cactaceae. EC 2.1.1.27 is the long-established, IUBMB-recognized EC number for tyramine N-methyltransferase, whereas EC 2.1.1.353 is either a very recently assigned or non-standard number with no widely recognized association to this enzyme class. A model recognizing the GAS motif, the plant methyltransferase fold, and the PROSITE PRU01020 pattern would confidently select 2.1.1.27 over the obscure or fabricated 2.1.1.353.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The sequence provides sufficient diagnostic features (GAS motif, overall length ~367 aa consistent with plant SAM-MTs, PROSITE PRU01020 pattern) to identify the enzyme as a tyramine N-methyltransferase. Transferable knowledge of plant methyltransferase families, the PROSITE-ProRule database, and the well-studied phenethylamine N-methyltransferase family in alkaloid biosynthesis allows distinguishing EC 2.1.1.27 from the other options. Option C (isomerase) and D (alkyltransferase) are eliminated by the methyltransferase fold. Option A (2.1.1.353) lacks the established association with tyramine N-methyltransferase that 2.1.1.27 carries in the literature and pattern databases.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> EC 5.4.99.14 (isomerase) and EC 2.5.1.76 (alkyltransferase) are clearly incompatible with the SAM-binding methyltransferase motifs in the sequence. EC 2.1.1.353 is either non-standard or refers to a different, unrelated methyltransferase, making it a weak distractor. EC 2.1.1.27 is the uniquely well-established EC number for tyramine N-methyltransferase, supported by the PROSITE PRU01020 signature.


### Important caveats

- The PROSITE-ProRule PRU01020 evidence code (ECO:0000255) is computational/pattern-based; the definitive experimental validation comes from PubMed:38835170 (ECO:0000269).
- EC 2.1.1.353 could not be definitively identified as a standard IUBMB EC number; if it is a very recently assigned number for a related enzyme, the distinction from 2.1.1.27 relies on the PROSITE pattern match and family-level knowledge rather than a single sequence feature.
- The sequence is from Lophophora williamsii (peyote), a Cactaceae species known for mescaline biosynthesis; this biological context supports the tyramine N-methyltransferase assignment but was not provided to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains hallmark SAM-dependent methyltransferase motifs: the 'VDIAGGTGASIN' region (~residues 188-200) includes the diagnostic GAS (Gly-Ala-Ser) motif of the Rossmann-like fold found in class I SAM-dependent methyltransferases. This immediately places the enzyme in EC 2.1.1 (methyltransferases transferring one-carbon groups), eliminating C (5.4.99.14, an isomerase) and D (2.5.1.76, an alkyl/aryl transferase with a different catalytic mechanism and fold). Among EC 2.1.1 options, the PROSITE-ProRule PRU01020 is a well-known pattern signature specifically for tyramine N-methyltransferases (PNMTs) in plants. Plant phenethylamine N-methyltransferases are a well-characterized family (~350-400 aa, specific active-site residues) involved in alkaloid biosynthesis pathways including mescaline production in Cactaceae. EC 2.1.1.27 is the long-established, IUBMB-recognized EC number for tyramine N-methyltransferase, whereas EC 2.1.1.353 is either a very recently assigned or non-standard number with no widely recognized association to this enzyme class. A model recognizing the GAS motif, the plant methyltransferase fold, and the PROSITE PRU01020 pattern would confidently select 2.1.1.27 over the obscure or fabricated 2.1.1.353.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The sequence provides sufficient diagnostic features (GAS motif, overall length ~367 aa consistent with plant SAM-MTs, PROSITE PRU01020 pattern) to identify the enzyme as a tyramine N-methyltransferase. Transferable knowledge of plant methyltransferase families, the PROSITE-ProRule database, and the well-studied phenethylamine N-methyltransferase family in alkaloid biosynthesis allows distinguishing EC 2.1.1.27 from the other options. Option C (isomerase) and D (alkyltransferase) are eliminated by the methyltransferase fold. Option A (2.1.1.353) lacks the established association with tyramine N-methyltransferase that 2.1.1.27 carries in the literature and pattern databases."
  },
  "case_id": "EC_number_0078",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C7",
      "C17",
      "H1",
      "H2",
      "H5",
      "H6",
      "H7",
      "H17"
    ],
    "judgment": "supported",
    "reason": "The reviewer-only evidence confirms the sequence matches UniProt A0AA51VIL7 (NMT1_LOPWI), annotated as Tyramine N-methyltransferase 1 with EC 2.1.1.27. The EC assignment is supported by both PROSITE-ProRule PRU01020 (computational, ECO:0000255) and experimental evidence (ECO:0000269, PubMed:38835170). Multiple catalytic activities are documented showing N-methyltransferase activity on tyramine, dopamine, mescaline, and various phenethylamine substrates using SAM as methyl donor. The reaction 'tyramine + SAM = N-methyltyramine + SAH + H+' is the canonical EC 2.1.1.27 reaction."
  },
  "important_caveats": [
    "The PROSITE-ProRule PRU01020 evidence code (ECO:0000255) is computational/pattern-based; the definitive experimental validation comes from PubMed:38835170 (ECO:0000269).",
    "EC 2.1.1.353 could not be definitively identified as a standard IUBMB EC number; if it is a very recently assigned number for a related enzyme, the distinction from 2.1.1.27 relies on the PROSITE pattern match and family-level knowledge rather than a single sequence feature.",
    "The sequence is from Lophophora williamsii (peyote), a Cactaceae species known for mescaline biosynthesis; this biological context supports the tyramine N-methyltransferase assignment but was not provided to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "EC 5.4.99.14 (isomerase) and EC 2.5.1.76 (alkyltransferase) are clearly incompatible with the SAM-binding methyltransferase motifs in the sequence. EC 2.1.1.353 is either non-standard or refers to a different, unrelated methyltransferase, making it a weak distractor. EC 2.1.1.27 is the uniquely well-established EC number for tyramine N-methyltransferase, supported by the PROSITE PRU01020 signature."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0078",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The reviewer-only evidence confirms the sequence matches UniProt A0AA51VIL7 (NMT1_LOPWI), annotated as Tyramine N-methyltransferase 1 with EC 2.1.1.27. The EC assignment is supported by both PROSITE-ProRule PRU01020 (computational, ECO:0000255) and experimental evidence (ECO:0000269, PubMed:38835170). Multiple catalytic activities are documented showing N-methyltransferase activity on tyramine, dopamine, mescaline, and various phenethylamine substrates using SAM as methyl donor. The reaction 'tyramine + SAM = N-methyltyramine + SAH + H+' is the canonical EC 2.1.1.27 reaction.",
    "evidence_ids": ["C4", "C5", "C6", "C7", "C17", "H1", "H2", "H5", "H6", "H7", "H17"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains hallmark SAM-dependent methyltransferase motifs: the 'VDIAGGTGASIN' region (~residues 188-200) includes the diagnostic GAS (Gly-Ala-Ser) motif of the Rossmann-like fold found in class I SAM-dependent methyltransferases. This immediately places the enzyme in EC 2.1.1 (methyltransferases transferring one-carbon groups), eliminating C (5.4.99.14, an isomerase) and D (2.5.1.76, an alkyl/aryl transferase with a different catalytic mechanism and fold). Among EC 2.1.1 options, the PROSITE-ProRule PRU01020 is a well-known pattern signature specifically for tyramine N-methyltransferases (PNMTs) in plants. Plant phenethylamine N-methyltransferases are a well-characterized family (~350-400 aa, specific active-site residues) involved in alkaloid biosynthesis pathways including mescaline production in Cactaceae. EC 2.1.1.27 is the long-established, IUBMB-recognized EC number for tyramine N-methyltransferase, whereas EC 2.1.1.353 is either a very recently assigned or non-standard number with no widely recognized association to this enzyme class. A model recognizing the GAS motif, the plant methyltransferase fold, and the PROSITE PRU01020 pattern would confidently select 2.1.1.27 over the obscure or fabricated 2.1.1.353.",
    "missing_item_specific_fact": "",
    "reason": "The sequence provides sufficient diagnostic features (GAS motif, overall length ~367 aa consistent with plant SAM-MTs, PROSITE PRU01020 pattern) to identify the enzyme as a tyramine N-methyltransferase. Transferable knowledge of plant methyltransferase families, the PROSITE-ProRule database, and the well-studied phenethylamine N-methyltransferase family in alkaloid biosynthesis allows distinguishing EC 2.1.1.27 from the other options. Option C (isomerase) and D (alkyltransferase) are eliminated by the methyltransferase fold. Option A (2.1.1.353) lacks the established association with tyramine N-methyltransferase that 2.1.1.27 carries in the literature and pattern databases."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "EC 5.4.99.14 (isomerase) and EC 2.5.1.76 (alkyltransferase) are clearly incompatible with the SAM-binding methyltransferase motifs in the sequence. EC 2.1.1.353 is either non-standard or refers to a different, unrelated methyltransferase, making it a weak distractor. EC 2.1.1.27 is the uniquely well-established EC number for tyramine N-methyltransferase, supported by the PROSITE PRU01020 signature."
  },
  "important_caveats": [
    "The PROSITE-ProRule PRU01020 evidence code (ECO:0000255) is computational/pattern-based; the definitive experimental validation comes from PubMed:38835170 (ECO:0000269).",
    "EC 2.1.1.353 could not be definitively identified as a standard IUBMB EC number; if it is a very recently assigned number for a related enzyme, the distinction from 2.1.1.27 relies on the PROSITE pattern match and family-level knowledge rather than a single sequence feature.",
    "The sequence is from Lophophora williamsii (peyote), a Cactaceae species known for mescaline biosynthesis; this biological context supports the tyramine N-methyltransferase assignment but was not provided to the evaluated model."
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
  "requested_accession": "A0AA51VIL7",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "benchmark_sequence_sha256": "906a0fa54cdd2ce71a5c37c6ca189cd70e43ff9b39cc2d3e1acaa55aa615c8d4",
  "benchmark_sequence_length": 367,
  "current_status": "retrieved",
  "current_sequence_comparison": "matched",
  "current_entry_audit": {
    "entryVersion": 12,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2024-01-24",
    "sequenceVersion": 1
  },
  "current_uniprot_release": "2026_03",
  "current_record_sha256": "a5716b3c7e89f33127adc2f7a1674ece442bb48daa4358bf4bc4253e71206ee6",
  "current_source_sequence_sha256": "906a0fa54cdd2ce71a5c37c6ca189cd70e43ff9b39cc2d3e1acaa55aa615c8d4",
  "current_source_sequence_length": 367,
  "historical_status": "retrieved",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "selected_historical_entry_version": 10,
  "selected_historical_version": {
    "accession": "A0AA51VIL7",
    "database": "Swiss-Prot",
    "entryVersion": 10,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "NMT1_LOPWI",
    "sequenceVersion": 1
  },
  "selected_historical_record_sha256": "e4eaff71313f44d4f70b4dabe345699f1e93502209fec974e1426ccfcd7207c8",
  "selected_historical_source_sequence_sha256": "906a0fa54cdd2ce71a5c37c6ca189cd70e43ff9b39cc2d3e1acaa55aa615c8d4",
  "selected_historical_source_sequence_length": 367,
  "latest_at_cutoff_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 10,
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AA51VIL7.json)

```json
{
  "evidence_id": "C1",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0AA51VIL7.json",
  "source_sha256": "a5716b3c7e89f33127adc2f7a1674ece442bb48daa4358bf4bc4253e71206ee6",
  "retrieved_utc": "2026-11-01T06:24:55.487954+00:00",
  "json_pointer": "/primaryAccession",
  "excerpt": "\"A0AA51VIL7\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AA51VIL7.json)

```json
{
  "evidence_id": "C2",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0AA51VIL7.json",
  "source_sha256": "a5716b3c7e89f33127adc2f7a1674ece442bb48daa4358bf4bc4253e71206ee6",
  "retrieved_utc": "2026-11-01T06:24:55.487954+00:00",
  "json_pointer": "/entryAudit",
  "excerpt": "{\"entryVersion\":12,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2024-01-24\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AA51VIL7.json)

```json
{
  "evidence_id": "C3",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0AA51VIL7.json",
  "source_sha256": "a5716b3c7e89f33127adc2f7a1674ece442bb48daa4358bf4bc4253e71206ee6",
  "retrieved_utc": "2026-11-01T06:24:55.487954+00:00",
  "json_pointer": "/organism",
  "excerpt": "{\"commonName\":\"Peyote\",\"lineage\":[\"Eukaryota\",\"Viridiplantae\",\"Streptophyta\",\"Embryophyta\",\"Tracheophyta\",\"Spermatophyta\",\"Magnoliopsida\",\"eudicotyledons\",\"Gunneridae\",\"Pentapetalae\",\"Caryophyllales\",\"Cactineae\",\"Cactaceae\",\"Cactoideae\",\"Cacteae\",\"Lophophora\"],\"scientificName\":\"Lophophora williamsii\",\"synonyms\":[\"Echinocactus williamsii\"],\"taxonId\":130138}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AA51VIL7.json)

```json
{
  "evidence_id": "C4",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0AA51VIL7.json",
  "source_sha256": "a5716b3c7e89f33127adc2f7a1674ece442bb48daa4358bf4bc4253e71206ee6",
  "retrieved_utc": "2026-11-01T06:24:55.487954+00:00",
  "json_pointer": "/proteinDescription",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"37675639\",\"source\":\"PubMed\"}],\"value\":\"O-methyltransferase 4\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"37675639\",\"source\":\"PubMed\"}],\"value\":\"LwOMT4\"}]}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU01020\",\"source\":\"PROSITE-ProRule\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38835170\",\"source\":\"PubMed\"}],\"value\":\"2.1.1.27\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"38835170\",\"source\":\"PubMed\"}],\"value\":\"Tyramine N-methyltransferase 1\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"38835170\",\"source\":\"PubMed\"}],\"value\":\"LwNMT1\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AA51VIL7.json)

```json
{
  "evidence_id": "C5",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0AA51VIL7.json",
  "source_sha256": "a5716b3c7e89f33127adc2f7a1674ece442bb48daa4358bf4bc4253e71206ee6",
  "retrieved_utc": "2026-11-01T06:24:55.487954+00:00",
  "json_pointer": "/comments/1",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38835170\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:14866\"}}],\"reaction\":{\"ecNumber\":\"2.1.1.27\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38835170\",\"source\":\"PubMed\"}],\"name\":\"tyramine + S-adenosyl-L-methionine = N-methyltyramine + S-adenosyl-L-homocysteine + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:14865\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57856\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:58155\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:59789\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:327995\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AA51VIL7.json)

```json
{
  "evidence_id": "C6",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0AA51VIL7.json",
  "source_sha256": "a5716b3c7e89f33127adc2f7a1674ece442bb48daa4358bf4bc4253e71206ee6",
  "retrieved_utc": "2026-11-01T06:24:55.487954+00:00",
  "json_pointer": "/comments/2",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38835170\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:80992\"}}],\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38835170\",\"source\":\"PubMed\"}],\"name\":\"N-methyltyramine + S-adenosyl-L-methionine = hordenine + S-adenosyl-L-homocysteine + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:80991\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57856\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:58155\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:59789\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:231770\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AA51VIL7.json)

```json
{
  "evidence_id": "C7",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0AA51VIL7.json",
  "source_sha256": "a5716b3c7e89f33127adc2f7a1674ece442bb48daa4358bf4bc4253e71206ee6",
  "retrieved_utc": "2026-11-01T06:24:55.487954+00:00",
  "json_pointer": "/comments/3",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38835170\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:80996\"}}],\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38835170\",\"source\":\"PubMed\"}],\"name\":\"dopamine + S-adenosyl-L-methionine = N-methyl-dopamine + S-adenosyl-L-homocysteine + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:80995\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57856\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:59789\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:59905\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:231771\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AA51VIL7.json)

```json
{
  "evidence_id": "C8",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0AA51VIL7.json",
  "source_sha256": "a5716b3c7e89f33127adc2f7a1674ece442bb48daa4358bf4bc4253e71206ee6",
  "retrieved_utc": "2026-11-01T06:24:55.487954+00:00",
  "json_pointer": "/comments/4",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38835170\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:81000\"}}],\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38835170\",\"source\":\"PubMed\"}],\"name\":\"N-methyl-dopamine + S-adenosyl-L-methionine = N,N-dimethyldopamine + S-adenosyl-L-homocysteine + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:80999\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57856\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:59789\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:231771\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:231772\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AA51VIL7.json)

```json
{
  "evidence_id": "C9",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0AA51VIL7.json",
  "source_sha256": "a5716b3c7e89f33127adc2f7a1674ece442bb48daa4358bf4bc4253e71206ee6",
  "retrieved_utc": "2026-11-01T06:24:55.487954+00:00",
  "json_pointer": "/comments/5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"37675639\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38835170\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:81004\"}}],\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"37675639\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38835170\",\"source\":\"PubMed\"}],\"name\":\"3-methoxytyramine + S-adenosyl-L-methionine = N-methyl-3-methoxytyramine + S-adenosyl-L-homocysteine + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:81003\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57856\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:59789\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:192089\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:231773\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AA51VIL7.json)

```json
{
  "evidence_id": "C10",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0AA51VIL7.json",
  "source_sha256": "a5716b3c7e89f33127adc2f7a1674ece442bb48daa4358bf4bc4253e71206ee6",
  "retrieved_utc": "2026-11-01T06:24:55.487954+00:00",
  "json_pointer": "/comments/6",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38835170\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:81008\"}}],\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38835170\",\"source\":\"PubMed\"}],\"name\":\"N-methyl-3-methoxytyramine + S-adenosyl-L-methionine = N,N-dimethyl-3-methoxytyramine + S-adenosyl-L-homocysteine + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:81007\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57856\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:59789\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:231773\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:231774\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AA51VIL7.json)

```json
{
  "evidence_id": "C11",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0AA51VIL7.json",
  "source_sha256": "a5716b3c7e89f33127adc2f7a1674ece442bb48daa4358bf4bc4253e71206ee6",
  "retrieved_utc": "2026-11-01T06:24:55.487954+00:00",
  "json_pointer": "/comments/7",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38835170\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:81012\"}}],\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38835170\",\"source\":\"PubMed\"}],\"name\":\"3,4-dihydroxy-5-methoxyphenethylamine + S-adenosyl-L-methionine = N-methyl-3,4-dihydroxy-5-methoxyphenethylamine + S-adenosyl-L-homocysteine + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:81011\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57856\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:59789\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:231763\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:231775\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AA51VIL7.json)

```json
{
  "evidence_id": "C12",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0AA51VIL7.json",
  "source_sha256": "a5716b3c7e89f33127adc2f7a1674ece442bb48daa4358bf4bc4253e71206ee6",
  "retrieved_utc": "2026-11-01T06:24:55.487954+00:00",
  "json_pointer": "/comments/8",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38835170\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:81016\"}}],\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38835170\",\"source\":\"PubMed\"}],\"name\":\"N-methyl-3,4-dihydroxy-5-methoxyphenethylamine + S-adenosyl-L-methionine = N,N-dimethyl-3,4-dihydroxy-5-methoxyphenethylamine + S-adenosyl-L-homocysteine + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:81015\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57856\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:59789\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:231775\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:231776\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C13

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AA51VIL7.json)

```json
{
  "evidence_id": "C13",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0AA51VIL7.json",
  "source_sha256": "a5716b3c7e89f33127adc2f7a1674ece442bb48daa4358bf4bc4253e71206ee6",
  "retrieved_utc": "2026-11-01T06:24:55.487954+00:00",
  "json_pointer": "/comments/9",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38835170\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:81020\"}}],\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38835170\",\"source\":\"PubMed\"}],\"name\":\"3-hydroxy-4,5-dimethoxyphenethylamine + S-adenosyl-L-methionine = N-methyl-3-hydroxy-4,5-dimethoxyphenethylamine + S-adenosyl-L-homocysteine + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:81019\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57856\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:59789\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:231769\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:231779\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C14

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AA51VIL7.json)

```json
{
  "evidence_id": "C14",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0AA51VIL7.json",
  "source_sha256": "a5716b3c7e89f33127adc2f7a1674ece442bb48daa4358bf4bc4253e71206ee6",
  "retrieved_utc": "2026-11-01T06:24:55.487954+00:00",
  "json_pointer": "/comments/10",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38835170\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:81024\"}}],\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38835170\",\"source\":\"PubMed\"}],\"name\":\"N-methyl-3-hydroxy-4,5-dimethoxyphenethylamine + S-adenosyl-L-methionine = N,N-dimethyl-3-hydroxy-4,5-dimethoxyphenethylamine + S-adenosyl-L-homocysteine + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:81023\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57856\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:59789\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:231779\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:231780\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C15

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AA51VIL7.json)

```json
{
  "evidence_id": "C15",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0AA51VIL7.json",
  "source_sha256": "a5716b3c7e89f33127adc2f7a1674ece442bb48daa4358bf4bc4253e71206ee6",
  "retrieved_utc": "2026-11-01T06:24:55.487954+00:00",
  "json_pointer": "/comments/11",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"37675639\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38835170\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:81028\"}}],\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"37675639\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38835170\",\"source\":\"PubMed\"}],\"name\":\"4-hydroxy-3,5-dimethoxyphenethylamine + S-adenosyl-L-methionine = N-methyl-4-hydroxy-3,5-dimethoxyphenethylamine + S-adenosyl-L-homocysteine + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:81027\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57856\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:59789\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:231768\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:231777\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C16

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AA51VIL7.json)

```json
{
  "evidence_id": "C16",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0AA51VIL7.json",
  "source_sha256": "a5716b3c7e89f33127adc2f7a1674ece442bb48daa4358bf4bc4253e71206ee6",
  "retrieved_utc": "2026-11-01T06:24:55.487954+00:00",
  "json_pointer": "/comments/12",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38835170\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:81032\"}}],\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38835170\",\"source\":\"PubMed\"}],\"name\":\"N-methyl-4-hydroxy-3,5-dimethoxyphenethylamine + S-adenosyl-L-methionine = N,N-dimethyl-4-hydroxy-3,5-dimethoxyphenethylamine + S-adenosyl-L-homocysteine + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:81031\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57856\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:59789\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:231777\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:231778\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C17

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AA51VIL7.json)

```json
{
  "evidence_id": "C17",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0AA51VIL7.json",
  "source_sha256": "a5716b3c7e89f33127adc2f7a1674ece442bb48daa4358bf4bc4253e71206ee6",
  "retrieved_utc": "2026-11-01T06:24:55.487954+00:00",
  "json_pointer": "/comments/13",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38835170\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:81036\"}}],\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38835170\",\"source\":\"PubMed\"}],\"name\":\"mescaline + S-adenosyl-L-methionine = N-methylmescaline + S-adenosyl-L-homocysteine + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:81035\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57856\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:59789\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:231762\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:231781\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C18

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AA51VIL7.json)

```json
{
  "evidence_id": "C18",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0AA51VIL7.json",
  "source_sha256": "a5716b3c7e89f33127adc2f7a1674ece442bb48daa4358bf4bc4253e71206ee6",
  "retrieved_utc": "2026-11-01T06:24:55.487954+00:00",
  "json_pointer": "/comments/14",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38835170\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:81040\"}}],\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38835170\",\"source\":\"PubMed\"}],\"name\":\"N-methylmescaline + S-adenosyl-L-methionine = N,N-dimethylmescaline + S-adenosyl-L-homocysteine + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:81039\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57856\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:59789\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:231781\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:231782\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C19

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AA51VIL7.json)

```json
{
  "evidence_id": "C19",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0AA51VIL7.json",
  "source_sha256": "a5716b3c7e89f33127adc2f7a1674ece442bb48daa4358bf4bc4253e71206ee6",
  "retrieved_utc": "2026-11-01T06:24:55.487954+00:00",
  "json_pointer": "/references/0",
  "excerpt": "{\"citation\":{\"authors\":[\"Watkins J.L.\",\"Li Q.\",\"Yeaman S.\",\"Facchini P.J.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"37675639\"},{\"database\":\"DOI\",\"id\":\"10.1111/tpj.16447\"}],\"citationType\":\"journal article\",\"firstPage\":\"635\",\"id\":\"37675639\",\"journal\":\"Plant J.\",\"lastPage\":\"649\",\"publicationDate\":\"2023\",\"title\":\"Elucidation of the mescaline biosynthetic pathway in peyote (Lophophora williamsii).\",\"volume\":\"116\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"WMX25282.1\",\"source\":\"EMBL\"}],\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"cv. Jourdaniana\"}],\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [MRNA]\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"PATHWAY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C20

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AA51VIL7.json)

```json
{
  "evidence_id": "C20",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0AA51VIL7.json",
  "source_sha256": "a5716b3c7e89f33127adc2f7a1674ece442bb48daa4358bf4bc4253e71206ee6",
  "retrieved_utc": "2026-11-01T06:24:55.487954+00:00",
  "json_pointer": "/references/1",
  "excerpt": "{\"citation\":{\"authors\":[\"Berman P.\",\"de Haro L.A.\",\"Cavaco A.-R.\",\"Panda S.\",\"Dong Y.\",\"Kuzmich N.\",\"Lichtenstein G.\",\"Peleg Y.\",\"Harat H.\",\"Jozwiak A.\",\"Cai J.\",\"Heinig U.\",\"Meir S.\",\"Rogachev I.\",\"Aharoni A.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"38835170\"},{\"database\":\"DOI\",\"id\":\"10.1016/j.molp.2024.05.012\"}],\"citationType\":\"journal article\",\"firstPage\":\"1129\",\"id\":\"38835170\",\"journal\":\"Mol. Plant\",\"lastPage\":\"1150\",\"publicationDate\":\"2024\",\"title\":\"The biosynthetic pathway of the hallucinogen mescaline and its heterologous reconstruction.\",\"volume\":\"17\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"cv. Rehovot 7\"}],\"referenceNumber\":2,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [MRNA]\",\"FUNCTION\",\"MUTAGENESIS OF TRP-266; ASP-270 AND PHE-324\",\"CATALYTIC ACTIVITY\",\"PATHWAY\",\"BIOTECHNOLOGY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AA51VIL7?format=txt&versions=10)

```json
{
  "evidence_id": "H1",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0AA51VIL7?format=txt&versions=10",
  "source_sha256": "e4eaff71313f44d4f70b4dabe345699f1e93502209fec974e1426ccfcd7207c8",
  "retrieved_utc": "2026-11-01T06:27:38.117320+00:00",
  "source_locator": "lines 1-17",
  "excerpt": "ID   NMT1_LOPWI              Reviewed;         367 AA.\nAC   A0AA51VIL7;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   24-JAN-2024, sequence version 1.\nDT   28-JAN-2026, entry version 10.\nDE   RecName: Full=Tyramine N-methyltransferase 1 {ECO:0000305|PubMed:38835170};\nDE            Short=LwNMT1 {ECO:0000303|PubMed:38835170};\nDE            EC=2.1.1.27 {ECO:0000255|PROSITE-ProRule:PRU01020, ECO:0000269|PubMed:38835170};\nDE   AltName: Full=O-methyltransferase 4 {ECO:0000303|PubMed:37675639};\nDE            Short=LwOMT4 {ECO:0000303|PubMed:37675639};\nGN   Name=NMT1 {ECO:0000303|PubMed:38835170};\nGN   Synonyms=OMT4 {ECO:0000303|PubMed:37675639};\nOS   Lophophora williamsii (Peyote) (Echinocactus williamsii).\nOC   Eukaryota; Viridiplantae; Streptophyta; Embryophyta; Tracheophyta;\nOC   Spermatophyta; Magnoliopsida; eudicotyledons; Gunneridae; Pentapetalae;\nOC   Caryophyllales; Cactineae; Cactaceae; Cactoideae; Cacteae; Lophophora.\nOX   NCBI_TaxID=130138;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 10,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AA51VIL7?format=txt&versions=10)

```json
{
  "evidence_id": "H2",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0AA51VIL7?format=txt&versions=10",
  "source_sha256": "e4eaff71313f44d4f70b4dabe345699f1e93502209fec974e1426ccfcd7207c8",
  "retrieved_utc": "2026-11-01T06:27:38.117320+00:00",
  "source_locator": "lines 6-10",
  "excerpt": "DE   RecName: Full=Tyramine N-methyltransferase 1 {ECO:0000305|PubMed:38835170};\nDE            Short=LwNMT1 {ECO:0000303|PubMed:38835170};\nDE            EC=2.1.1.27 {ECO:0000255|PROSITE-ProRule:PRU01020, ECO:0000269|PubMed:38835170};\nDE   AltName: Full=O-methyltransferase 4 {ECO:0000303|PubMed:37675639};\nDE            Short=LwOMT4 {ECO:0000303|PubMed:37675639};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 10,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AA51VIL7?format=txt&versions=10)

```json
{
  "evidence_id": "H3",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0AA51VIL7?format=txt&versions=10",
  "source_sha256": "e4eaff71313f44d4f70b4dabe345699f1e93502209fec974e1426ccfcd7207c8",
  "retrieved_utc": "2026-11-01T06:27:38.117320+00:00",
  "source_locator": "lines 18-25",
  "excerpt": "RN   [1] {ECO:0000312|EMBL:WMX25282.1}\nRP   NUCLEOTIDE SEQUENCE [MRNA], FUNCTION, CATALYTIC ACTIVITY, AND PATHWAY.\nRC   STRAIN=cv. Jourdaniana;\nRX   PubMed=37675639; DOI=10.1111/tpj.16447;\nRA   Watkins J.L., Li Q., Yeaman S., Facchini P.J.;\nRT   \"Elucidation of the mescaline biosynthetic pathway in peyote (Lophophora\nRT   williamsii).\";\nRL   Plant J. 116:635-649(2023).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 10,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AA51VIL7?format=txt&versions=10)

```json
{
  "evidence_id": "H4",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0AA51VIL7?format=txt&versions=10",
  "source_sha256": "e4eaff71313f44d4f70b4dabe345699f1e93502209fec974e1426ccfcd7207c8",
  "retrieved_utc": "2026-11-01T06:27:38.117320+00:00",
  "source_locator": "lines 26-36",
  "excerpt": "RN   [2]\nRP   NUCLEOTIDE SEQUENCE [MRNA], FUNCTION, MUTAGENESIS OF TRP-266; ASP-270 AND\nRP   PHE-324, CATALYTIC ACTIVITY, PATHWAY, AND BIOTECHNOLOGY.\nRC   STRAIN=cv. Rehovot 7;\nRX   PubMed=38835170; DOI=10.1016/j.molp.2024.05.012;\nRA   Berman P., de Haro L.A., Cavaco A.-R., Panda S., Dong Y., Kuzmich N.,\nRA   Lichtenstein G., Peleg Y., Harat H., Jozwiak A., Cai J., Heinig U.,\nRA   Meir S., Rogachev I., Aharoni A.;\nRT   \"The biosynthetic pathway of the hallucinogen mescaline and its\nRT   heterologous reconstruction.\";\nRL   Mol. Plant 17:1129-1150(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 10,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AA51VIL7?format=txt&versions=10)

```json
{
  "evidence_id": "H5",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0AA51VIL7?format=txt&versions=10",
  "source_sha256": "e4eaff71313f44d4f70b4dabe345699f1e93502209fec974e1426ccfcd7207c8",
  "retrieved_utc": "2026-11-01T06:27:38.117320+00:00",
  "source_locator": "lines 50-57",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=tyramine + S-adenosyl-L-methionine = N-methyltyramine + S-\nCC         adenosyl-L-homocysteine + H(+); Xref=Rhea:RHEA:14865,\nCC         ChEBI:CHEBI:15378, ChEBI:CHEBI:57856, ChEBI:CHEBI:58155,\nCC         ChEBI:CHEBI:59789, ChEBI:CHEBI:327995; EC=2.1.1.27;\nCC         Evidence={ECO:0000269|PubMed:38835170};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:14866;\nCC         Evidence={ECO:0000269|PubMed:38835170};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 10,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AA51VIL7?format=txt&versions=10)

```json
{
  "evidence_id": "H6",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0AA51VIL7?format=txt&versions=10",
  "source_sha256": "e4eaff71313f44d4f70b4dabe345699f1e93502209fec974e1426ccfcd7207c8",
  "retrieved_utc": "2026-11-01T06:27:38.117320+00:00",
  "source_locator": "lines 58-65",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=N-methyltyramine + S-adenosyl-L-methionine = hordenine + S-\nCC         adenosyl-L-homocysteine + H(+); Xref=Rhea:RHEA:80991,\nCC         ChEBI:CHEBI:15378, ChEBI:CHEBI:57856, ChEBI:CHEBI:58155,\nCC         ChEBI:CHEBI:59789, ChEBI:CHEBI:231770;\nCC         Evidence={ECO:0000269|PubMed:38835170};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:80992;\nCC         Evidence={ECO:0000269|PubMed:38835170};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 10,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AA51VIL7?format=txt&versions=10)

```json
{
  "evidence_id": "H7",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0AA51VIL7?format=txt&versions=10",
  "source_sha256": "e4eaff71313f44d4f70b4dabe345699f1e93502209fec974e1426ccfcd7207c8",
  "retrieved_utc": "2026-11-01T06:27:38.117320+00:00",
  "source_locator": "lines 66-73",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=dopamine + S-adenosyl-L-methionine = N-methyl-dopamine + S-\nCC         adenosyl-L-homocysteine + H(+); Xref=Rhea:RHEA:80995,\nCC         ChEBI:CHEBI:15378, ChEBI:CHEBI:57856, ChEBI:CHEBI:59789,\nCC         ChEBI:CHEBI:59905, ChEBI:CHEBI:231771;\nCC         Evidence={ECO:0000269|PubMed:38835170};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:80996;\nCC         Evidence={ECO:0000269|PubMed:38835170};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 10,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AA51VIL7?format=txt&versions=10)

```json
{
  "evidence_id": "H8",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0AA51VIL7?format=txt&versions=10",
  "source_sha256": "e4eaff71313f44d4f70b4dabe345699f1e93502209fec974e1426ccfcd7207c8",
  "retrieved_utc": "2026-11-01T06:27:38.117320+00:00",
  "source_locator": "lines 74-81",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=N-methyl-dopamine + S-adenosyl-L-methionine = N,N-\nCC         dimethyldopamine + S-adenosyl-L-homocysteine + H(+);\nCC         Xref=Rhea:RHEA:80999, ChEBI:CHEBI:15378, ChEBI:CHEBI:57856,\nCC         ChEBI:CHEBI:59789, ChEBI:CHEBI:231771, ChEBI:CHEBI:231772;\nCC         Evidence={ECO:0000269|PubMed:38835170};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:81000;\nCC         Evidence={ECO:0000269|PubMed:38835170};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 10,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AA51VIL7?format=txt&versions=10)

```json
{
  "evidence_id": "H9",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0AA51VIL7?format=txt&versions=10",
  "source_sha256": "e4eaff71313f44d4f70b4dabe345699f1e93502209fec974e1426ccfcd7207c8",
  "retrieved_utc": "2026-11-01T06:27:38.117320+00:00",
  "source_locator": "lines 82-89",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=3-methoxytyramine + S-adenosyl-L-methionine = N-methyl-3-\nCC         methoxytyramine + S-adenosyl-L-homocysteine + H(+);\nCC         Xref=Rhea:RHEA:81003, ChEBI:CHEBI:15378, ChEBI:CHEBI:57856,\nCC         ChEBI:CHEBI:59789, ChEBI:CHEBI:192089, ChEBI:CHEBI:231773;\nCC         Evidence={ECO:0000269|PubMed:37675639, ECO:0000269|PubMed:38835170};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:81004;\nCC         Evidence={ECO:0000269|PubMed:37675639, ECO:0000269|PubMed:38835170};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 10,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H10

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AA51VIL7?format=txt&versions=10)

```json
{
  "evidence_id": "H10",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0AA51VIL7?format=txt&versions=10",
  "source_sha256": "e4eaff71313f44d4f70b4dabe345699f1e93502209fec974e1426ccfcd7207c8",
  "retrieved_utc": "2026-11-01T06:27:38.117320+00:00",
  "source_locator": "lines 90-97",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=N-methyl-3-methoxytyramine + S-adenosyl-L-methionine = N,N-\nCC         dimethyl-3-methoxytyramine + S-adenosyl-L-homocysteine + H(+);\nCC         Xref=Rhea:RHEA:81007, ChEBI:CHEBI:15378, ChEBI:CHEBI:57856,\nCC         ChEBI:CHEBI:59789, ChEBI:CHEBI:231773, ChEBI:CHEBI:231774;\nCC         Evidence={ECO:0000269|PubMed:38835170};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:81008;\nCC         Evidence={ECO:0000269|PubMed:38835170};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 10,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H11

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AA51VIL7?format=txt&versions=10)

```json
{
  "evidence_id": "H11",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0AA51VIL7?format=txt&versions=10",
  "source_sha256": "e4eaff71313f44d4f70b4dabe345699f1e93502209fec974e1426ccfcd7207c8",
  "retrieved_utc": "2026-11-01T06:27:38.117320+00:00",
  "source_locator": "lines 98-106",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=3,4-dihydroxy-5-methoxyphenethylamine + S-adenosyl-L-\nCC         methionine = N-methyl-3,4-dihydroxy-5-methoxyphenethylamine + S-\nCC         adenosyl-L-homocysteine + H(+); Xref=Rhea:RHEA:81011,\nCC         ChEBI:CHEBI:15378, ChEBI:CHEBI:57856, ChEBI:CHEBI:59789,\nCC         ChEBI:CHEBI:231763, ChEBI:CHEBI:231775;\nCC         Evidence={ECO:0000269|PubMed:38835170};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:81012;\nCC         Evidence={ECO:0000269|PubMed:38835170};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 10,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H12

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AA51VIL7?format=txt&versions=10)

```json
{
  "evidence_id": "H12",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0AA51VIL7?format=txt&versions=10",
  "source_sha256": "e4eaff71313f44d4f70b4dabe345699f1e93502209fec974e1426ccfcd7207c8",
  "retrieved_utc": "2026-11-01T06:27:38.117320+00:00",
  "source_locator": "lines 107-115",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=N-methyl-3,4-dihydroxy-5-methoxyphenethylamine + S-adenosyl-L-\nCC         methionine = N,N-dimethyl-3,4-dihydroxy-5-methoxyphenethylamine + S-\nCC         adenosyl-L-homocysteine + H(+); Xref=Rhea:RHEA:81015,\nCC         ChEBI:CHEBI:15378, ChEBI:CHEBI:57856, ChEBI:CHEBI:59789,\nCC         ChEBI:CHEBI:231775, ChEBI:CHEBI:231776;\nCC         Evidence={ECO:0000269|PubMed:38835170};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:81016;\nCC         Evidence={ECO:0000269|PubMed:38835170};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 10,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H13

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AA51VIL7?format=txt&versions=10)

```json
{
  "evidence_id": "H13",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0AA51VIL7?format=txt&versions=10",
  "source_sha256": "e4eaff71313f44d4f70b4dabe345699f1e93502209fec974e1426ccfcd7207c8",
  "retrieved_utc": "2026-11-01T06:27:38.117320+00:00",
  "source_locator": "lines 116-124",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=3-hydroxy-4,5-dimethoxyphenethylamine + S-adenosyl-L-\nCC         methionine = N-methyl-3-hydroxy-4,5-dimethoxyphenethylamine + S-\nCC         adenosyl-L-homocysteine + H(+); Xref=Rhea:RHEA:81019,\nCC         ChEBI:CHEBI:15378, ChEBI:CHEBI:57856, ChEBI:CHEBI:59789,\nCC         ChEBI:CHEBI:231769, ChEBI:CHEBI:231779;\nCC         Evidence={ECO:0000269|PubMed:38835170};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:81020;\nCC         Evidence={ECO:0000269|PubMed:38835170};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 10,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H14

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AA51VIL7?format=txt&versions=10)

```json
{
  "evidence_id": "H14",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0AA51VIL7?format=txt&versions=10",
  "source_sha256": "e4eaff71313f44d4f70b4dabe345699f1e93502209fec974e1426ccfcd7207c8",
  "retrieved_utc": "2026-11-01T06:27:38.117320+00:00",
  "source_locator": "lines 125-133",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=N-methyl-3-hydroxy-4,5-dimethoxyphenethylamine + S-adenosyl-L-\nCC         methionine = N,N-dimethyl-3-hydroxy-4,5-dimethoxyphenethylamine + S-\nCC         adenosyl-L-homocysteine + H(+); Xref=Rhea:RHEA:81023,\nCC         ChEBI:CHEBI:15378, ChEBI:CHEBI:57856, ChEBI:CHEBI:59789,\nCC         ChEBI:CHEBI:231779, ChEBI:CHEBI:231780;\nCC         Evidence={ECO:0000269|PubMed:38835170};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:81024;\nCC         Evidence={ECO:0000269|PubMed:38835170};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 10,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H15

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AA51VIL7?format=txt&versions=10)

```json
{
  "evidence_id": "H15",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0AA51VIL7?format=txt&versions=10",
  "source_sha256": "e4eaff71313f44d4f70b4dabe345699f1e93502209fec974e1426ccfcd7207c8",
  "retrieved_utc": "2026-11-01T06:27:38.117320+00:00",
  "source_locator": "lines 134-142",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=4-hydroxy-3,5-dimethoxyphenethylamine + S-adenosyl-L-\nCC         methionine = N-methyl-4-hydroxy-3,5-dimethoxyphenethylamine + S-\nCC         adenosyl-L-homocysteine + H(+); Xref=Rhea:RHEA:81027,\nCC         ChEBI:CHEBI:15378, ChEBI:CHEBI:57856, ChEBI:CHEBI:59789,\nCC         ChEBI:CHEBI:231768, ChEBI:CHEBI:231777;\nCC         Evidence={ECO:0000269|PubMed:37675639, ECO:0000269|PubMed:38835170};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:81028;\nCC         Evidence={ECO:0000269|PubMed:37675639, ECO:0000269|PubMed:38835170};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 10,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H16

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AA51VIL7?format=txt&versions=10)

```json
{
  "evidence_id": "H16",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0AA51VIL7?format=txt&versions=10",
  "source_sha256": "e4eaff71313f44d4f70b4dabe345699f1e93502209fec974e1426ccfcd7207c8",
  "retrieved_utc": "2026-11-01T06:27:38.117320+00:00",
  "source_locator": "lines 143-151",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=N-methyl-4-hydroxy-3,5-dimethoxyphenethylamine + S-adenosyl-L-\nCC         methionine = N,N-dimethyl-4-hydroxy-3,5-dimethoxyphenethylamine + S-\nCC         adenosyl-L-homocysteine + H(+); Xref=Rhea:RHEA:81031,\nCC         ChEBI:CHEBI:15378, ChEBI:CHEBI:57856, ChEBI:CHEBI:59789,\nCC         ChEBI:CHEBI:231777, ChEBI:CHEBI:231778;\nCC         Evidence={ECO:0000269|PubMed:38835170};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:81032;\nCC         Evidence={ECO:0000269|PubMed:38835170};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 10,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H17

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AA51VIL7?format=txt&versions=10)

```json
{
  "evidence_id": "H17",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0AA51VIL7?format=txt&versions=10",
  "source_sha256": "e4eaff71313f44d4f70b4dabe345699f1e93502209fec974e1426ccfcd7207c8",
  "retrieved_utc": "2026-11-01T06:27:38.117320+00:00",
  "source_locator": "lines 152-159",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=mescaline + S-adenosyl-L-methionine = N-methylmescaline + S-\nCC         adenosyl-L-homocysteine + H(+); Xref=Rhea:RHEA:81035,\nCC         ChEBI:CHEBI:15378, ChEBI:CHEBI:57856, ChEBI:CHEBI:59789,\nCC         ChEBI:CHEBI:231762, ChEBI:CHEBI:231781;\nCC         Evidence={ECO:0000269|PubMed:38835170};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:81036;\nCC         Evidence={ECO:0000269|PubMed:38835170};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 10,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H18

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AA51VIL7?format=txt&versions=10)

```json
{
  "evidence_id": "H18",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0AA51VIL7?format=txt&versions=10",
  "source_sha256": "e4eaff71313f44d4f70b4dabe345699f1e93502209fec974e1426ccfcd7207c8",
  "retrieved_utc": "2026-11-01T06:27:38.117320+00:00",
  "source_locator": "lines 160-167",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=N-methylmescaline + S-adenosyl-L-methionine = N,N-\nCC         dimethylmescaline + S-adenosyl-L-homocysteine + H(+);\nCC         Xref=Rhea:RHEA:81039, ChEBI:CHEBI:15378, ChEBI:CHEBI:57856,\nCC         ChEBI:CHEBI:59789, ChEBI:CHEBI:231781, ChEBI:CHEBI:231782;\nCC         Evidence={ECO:0000269|PubMed:38835170};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:81040;\nCC         Evidence={ECO:0000269|PubMed:38835170};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 10,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 78. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
