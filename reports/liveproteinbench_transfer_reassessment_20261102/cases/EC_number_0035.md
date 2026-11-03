# EC_number_0035: before and after transfer clarification

[All 1,328 cases](../README.md) · [Method](../METHOD.md) · [Summary](../SUMMARY.md) · [Exact reviewer user message](../inputs/EC_number_0035.txt)

**Task:** `EC_number`  
**Author key, unchanged:** **C** — 2.1.1.392

| Round | Reviewer | Key support | Transfer / lookup | Output usability (canonical status) |
|---|---|---|---|---|
| before | GPT-6 Luna | supported | lookup-dependent | usable output (valid_review) |
| before | Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | usable output (valid_review) |
| after | GPT-6 Luna | supported | lookup-dependent | usable output (valid_review) |
| after | Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | usable output (valid_review) |

**Usable output means format-valid review, not reasoning-supported or biologically correct.** A usable output can classify the question as reasoning-supported, lookup-dependent or uncertain. An output error is a problem with the saved model response; it does not count a defective benchmark question or wrong key. Each saved review is retained in full below. Labels from output errors are displayed as saved and excluded from label statistics. The author key and reviewer evidence were visible to reviewers; this is a review of answerability and key support, not a benchmark-solving score.

## Complete original question

```text
[Protein Sequence]
MAEKQQAVTEFYNNTSPRGAWEFLLGDHLHEGFYDPGTTATISGSQAAAARMIDEALRFANIYDDPSKKPKNMLDIGCGVGGTCVHVAKQYGIQCKGITLSPEEVKCAQGIAKAQGLEEKVSFDVGDALNLPYKDGTFDLVLTIECIEHVQDKEKFIREMIRVAAPGAPIVILSYAHRNLSPSAESLKPDEKKVLKKICDNLALSCLCSSADFVRWLTQLPAEDIKTADWTQNTSPFFPLLMKETFTWKGFTSLLMKGGWTAIKELLALRMMSKAADDGLLKFVAITCRKSK

[Multiple Choices]
A. 2.1.1.395
B. 2.1.1.27
C. 2.1.1.392
D. 1.3.1.36
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

> The supplied sequence exactly matches the reviewed UniProt sequence for this protein. Its EC 2.1.1.392 annotation is linked to evidence-coded catalytic activity for methylating norajmaline and 4-methylnorajmaline; the cited evidence code is experimental, though the underlying papers were not independently reviewed here.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence may support a broad inference of methyltransferase activity, and EC 1.3.1.36 is a different enzyme class. But that does not distinguish the closely related methyltransferase options by their specific substrate and reaction.


**Missing item-specific fact**

> The protein-specific catalytic activity—especially its methylation of norajmaline to ajmaline, which identifies EC 2.1.1.392—is not supplied in the question and requires a specific annotation or experimental result.


**Reason**

> Choosing the exact EC number depends on protein-specific substrate specificity, not a general sequence-level argument available from the provided input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The reviewer-only evidence supports C for the matched sequence. The sequence-only input does not reveal the exact substrate specificity, but that limitation concerns answerability rather than evidence that another option is correct.


### Important caveats

- The database annotation cites experimental evidence, but the primary papers were not independently retrieved or validated.
- The exact author data-source snapshot is unknown, although the sequence matches both the current and retrieved historical UniProt records.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence may support a broad inference of methyltransferase activity, and EC 1.3.1.36 is a different enzyme class. But that does not distinguish the closely related methyltransferase options by their specific substrate and reaction.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific catalytic activity—especially its methylation of norajmaline to ajmaline, which identifies EC 2.1.1.392—is not supplied in the question and requires a specific annotation or experimental result.",
    "reason": "Choosing the exact EC number depends on protein-specific substrate specificity, not a general sequence-level argument available from the provided input."
  },
  "case_id": "EC_number_0035",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the reviewed UniProt sequence for this protein. Its EC 2.1.1.392 annotation is linked to evidence-coded catalytic activity for methylating norajmaline and 4-methylnorajmaline; the cited evidence code is experimental, though the underlying papers were not independently reviewed here."
  },
  "important_caveats": [
    "The database annotation cites experimental evidence, but the primary papers were not independently retrieved or validated.",
    "The exact author data-source snapshot is unknown, although the sequence matches both the current and retrieved historical UniProt records."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The reviewer-only evidence supports C for the matched sequence. The sequence-only input does not reveal the exact substrate specificity, but that limitation concerns answerability rather than evidence that another option is correct."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0035",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the reviewed UniProt sequence for this protein. Its EC 2.1.1.392 annotation is linked to evidence-coded catalytic activity for methylating norajmaline and 4-methylnorajmaline; the cited evidence code is experimental, though the underlying papers were not independently reviewed here.",
    "evidence_ids": ["C1", "C4", "C5", "C6"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence may support a broad inference of methyltransferase activity, and EC 1.3.1.36 is a different enzyme class. But that does not distinguish the closely related methyltransferase options by their specific substrate and reaction.",
    "missing_item_specific_fact": "The protein-specific catalytic activity—especially its methylation of norajmaline to ajmaline, which identifies EC 2.1.1.392—is not supplied in the question and requires a specific annotation or experimental result.",
    "reason": "Choosing the exact EC number depends on protein-specific substrate specificity, not a general sequence-level argument available from the provided input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The reviewer-only evidence supports C for the matched sequence. The sequence-only input does not reveal the exact substrate specificity, but that limitation concerns answerability rather than evidence that another option is correct."
  },
  "important_caveats": [
    "The database annotation cites experimental evidence, but the primary papers were not independently retrieved or validated.",
    "The exact author data-source snapshot is unknown, although the sequence matches both the current and retrieved historical UniProt records."
  ]
}
```

</details>

## Before: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry A0A075D6M1 (NNMT_RAUSE) confirms this 292-aa sequence from Rauvolfia serpentina is Norajmaline N-methyltransferase with EC 2.1.1.392. The EC assignment is backed by experimental evidence (ECO:0000269) from PubMed 27122470 (Cazares-Flores et al., Plant J. 2016) and PubMed 38212296 (Guo et al., Nat. Commun. 2024), documenting the catalytic reaction: norajmaline + SAM → ajmaline + SAH + H+. Sequence match is exact (SHA-256 identical). The expected answer C (2.1.1.392) is correct.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C7](#evidence-c7), [C8](#evidence-c8), [H1](#evidence-h1), [H2](#evidence-h2), [H5](#evidence-h5), [H6](#evidence-h6).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> From the sequence, one can reasonably identify a SAM-dependent methyltransferase fold (Rossmann-like motifs including 'GCGVGGTC', 'VLT', and the conserved catalytic region), which supports EC class 2.1.1.- (N-methyltransferases) and eliminates D (1.3.1.36, an oxidoreductase). However, distinguishing the 4th digit — 392 vs 395 vs 27 — requires knowing the exact substrate specificity (norajmaline vs other alkaloid substrates). The EC 4th digit is an arbitrary catalog identifier for a specific enzyme–substrate pair, not derivable from general sequence motifs.


**Missing item-specific fact**

> The specific substrate identity (norajmaline → ajmaline N-methylation) and the precise active-site residues that confer selectivity for norajmaline over other potential N-methyltransferase substrates. This is an experimentally determined fact (PubMed 27122470, 38212296) not inferable from the raw sequence without database lookup or memorization of this specific entry.


**Reason**

> While the methyltransferase fold narrows the answer to EC 2.1.1.-, the three methyltransferase options (2.1.1.392, 2.1.1.395, 2.1.1.27) differ only in their arbitrary 4th-digit catalog number, which encodes the exact substrate. No general biological rule or sequence heuristic distinguishes 'norajmaline N-methyltransferase' from 'another N-methyltransferase' at the 4th-digit level. Selection requires item-specific knowledge of this protein's experimentally characterized substrate specificity.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> D (1.3.1.36, oxidoreductase) is clearly eliminable by recognizing the methyltransferase fold. Among A, B, and C (all 2.1.1.-), only C is correct per experimental evidence, but the question does not provide enough sequence-level information to reason between them. The ambiguity is not in the correctness of the key but in the absence of reasoning grounds to distinguish the three methyltransferase options.


### Important caveats

- The UniProt annotation was first released in Swiss-Prot on 2025-06-18; the EC assignment relies on 2016 and 2024 experimental papers. The benchmark author's source snapshot is unknown.
- EC 4th-digit numbers (392, 395, 27) are essentially catalog identifiers for specific enzyme-substrate pairs; no general biological rule maps sequence motifs to a specific 4th digit.
- The sequence alone does not reveal the organism (Rauvolfia serpentina) or the gene name (NNMT), both of which would be needed for contextual inference about ajmaline biosynthesis.
- Distractor D (1.3.1.36, oxidoreductase) is a trivially eliminable option given the clear methyltransferase fold, reducing effective discrimination to a three-way choice among N-methyltransferases that require substrate-specific knowledge.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "From the sequence, one can reasonably identify a SAM-dependent methyltransferase fold (Rossmann-like motifs including 'GCGVGGTC', 'VLT', and the conserved catalytic region), which supports EC class 2.1.1.- (N-methyltransferases) and eliminates D (1.3.1.36, an oxidoreductase). However, distinguishing the 4th digit — 392 vs 395 vs 27 — requires knowing the exact substrate specificity (norajmaline vs other alkaloid substrates). The EC 4th digit is an arbitrary catalog identifier for a specific enzyme–substrate pair, not derivable from general sequence motifs.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific substrate identity (norajmaline → ajmaline N-methylation) and the precise active-site residues that confer selectivity for norajmaline over other potential N-methyltransferase substrates. This is an experimentally determined fact (PubMed 27122470, 38212296) not inferable from the raw sequence without database lookup or memorization of this specific entry.",
    "reason": "While the methyltransferase fold narrows the answer to EC 2.1.1.-, the three methyltransferase options (2.1.1.392, 2.1.1.395, 2.1.1.27) differ only in their arbitrary 4th-digit catalog number, which encodes the exact substrate. No general biological rule or sequence heuristic distinguishes 'norajmaline N-methyltransferase' from 'another N-methyltransferase' at the 4th-digit level. Selection requires item-specific knowledge of this protein's experimentally characterized substrate specificity."
  },
  "case_id": "EC_number_0035",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C7",
      "C8",
      "H1",
      "H2",
      "H5",
      "H6"
    ],
    "judgment": "supported",
    "reason": "UniProt entry A0A075D6M1 (NNMT_RAUSE) confirms this 292-aa sequence from Rauvolfia serpentina is Norajmaline N-methyltransferase with EC 2.1.1.392. The EC assignment is backed by experimental evidence (ECO:0000269) from PubMed 27122470 (Cazares-Flores et al., Plant J. 2016) and PubMed 38212296 (Guo et al., Nat. Commun. 2024), documenting the catalytic reaction: norajmaline + SAM → ajmaline + SAH + H+. Sequence match is exact (SHA-256 identical). The expected answer C (2.1.1.392) is correct."
  },
  "important_caveats": [
    "The UniProt annotation was first released in Swiss-Prot on 2025-06-18; the EC assignment relies on 2016 and 2024 experimental papers. The benchmark author's source snapshot is unknown.",
    "EC 4th-digit numbers (392, 395, 27) are essentially catalog identifiers for specific enzyme-substrate pairs; no general biological rule maps sequence motifs to a specific 4th digit.",
    "The sequence alone does not reveal the organism (Rauvolfia serpentina) or the gene name (NNMT), both of which would be needed for contextual inference about ajmaline biosynthesis.",
    "Distractor D (1.3.1.36, oxidoreductase) is a trivially eliminable option given the clear methyltransferase fold, reducing effective discrimination to a three-way choice among N-methyltransferases that require substrate-specific knowledge."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "D (1.3.1.36, oxidoreductase) is clearly eliminable by recognizing the methyltransferase fold. Among A, B, and C (all 2.1.1.-), only C is correct per experimental evidence, but the question does not provide enough sequence-level information to reason between them. The ambiguity is not in the correctness of the key but in the absence of reasoning grounds to distinguish the three methyltransferase options."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0035",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry A0A075D6M1 (NNMT_RAUSE) confirms this 292-aa sequence from Rauvolfia serpentina is Norajmaline N-methyltransferase with EC 2.1.1.392. The EC assignment is backed by experimental evidence (ECO:0000269) from PubMed 27122470 (Cazares-Flores et al., Plant J. 2016) and PubMed 38212296 (Guo et al., Nat. Commun. 2024), documenting the catalytic reaction: norajmaline + SAM → ajmaline + SAH + H+. Sequence match is exact (SHA-256 identical). The expected answer C (2.1.1.392) is correct.",
    "evidence_ids": ["C4", "C5", "C7", "C8", "H1", "H2", "H5", "H6"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "From the sequence, one can reasonably identify a SAM-dependent methyltransferase fold (Rossmann-like motifs including 'GCGVGGTC', 'VLT', and the conserved catalytic region), which supports EC class 2.1.1.- (N-methyltransferases) and eliminates D (1.3.1.36, an oxidoreductase). However, distinguishing the 4th digit — 392 vs 395 vs 27 — requires knowing the exact substrate specificity (norajmaline vs other alkaloid substrates). The EC 4th digit is an arbitrary catalog identifier for a specific enzyme–substrate pair, not derivable from general sequence motifs.",
    "missing_item_specific_fact": "The specific substrate identity (norajmaline → ajmaline N-methylation) and the precise active-site residues that confer selectivity for norajmaline over other potential N-methyltransferase substrates. This is an experimentally determined fact (PubMed 27122470, 38212296) not inferable from the raw sequence without database lookup or memorization of this specific entry.",
    "reason": "While the methyltransferase fold narrows the answer to EC 2.1.1.-, the three methyltransferase options (2.1.1.392, 2.1.1.395, 2.1.1.27) differ only in their arbitrary 4th-digit catalog number, which encodes the exact substrate. No general biological rule or sequence heuristic distinguishes 'norajmaline N-methyltransferase' from 'another N-methyltransferase' at the 4th-digit level. Selection requires item-specific knowledge of this protein's experimentally characterized substrate specificity."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "D (1.3.1.36, oxidoreductase) is clearly eliminable by recognizing the methyltransferase fold. Among A, B, and C (all 2.1.1.-), only C is correct per experimental evidence, but the question does not provide enough sequence-level information to reason between them. The ambiguity is not in the correctness of the key but in the absence of reasoning grounds to distinguish the three methyltransferase options."
  },
  "important_caveats": [
    "The UniProt annotation was first released in Swiss-Prot on 2025-06-18; the EC assignment relies on 2016 and 2024 experimental papers. The benchmark author's source snapshot is unknown.",
    "EC 4th-digit numbers (392, 395, 27) are essentially catalog identifiers for specific enzyme-substrate pairs; no general biological rule maps sequence motifs to a specific 4th digit.",
    "The sequence alone does not reveal the organism (Rauvolfia serpentina) or the gene name (NNMT), both of which would be needed for contextual inference about ajmaline biosynthesis.",
    "Distractor D (1.3.1.36, oxidoreductase) is a trivially eliminable option given the clear methyltransferase fold, reducing effective discrimination to a three-way choice among N-methyltransferases that require substrate-specific knowledge."
  ]
}
```

</details>

## After: GPT-6 Luna

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The matched sequence is annotated as EC 2.1.1.392, with cited experimental evidence for methylation reactions involving norajmaline and 4-methylnorajmaline. This supports choice C.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence is consistent with a SAM-dependent methyltransferase, which makes the methyltransferase options more plausible than the oxidoreductase option D. But that broad feature does not distinguish EC 2.1.1.392 from the other methyltransferase choices: the exact substrate and reaction specificity is the deciding information.


**Missing item-specific fact**

> The enzyme's experimentally established substrate and product specificity, or a characterized homolog that establishes the same specificity.


**Reason**

> The sequence offers a transferable clue to methyltransferase activity, but not a credible basis for selecting this particular EC subclass over the other methyltransferase alternatives. The precise reaction assignment depends on information about this protein or a sufficiently characterized homolog that is absent from the input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The evidence supports one EC assignment for the protein; insufficient sequence information to infer that assignment is not itself evidence that multiple choices are correct.


### Important caveats

- The reviewer-only evidence matches the supplied sequence and cites experimental evidence for the annotated reactions; those annotations were not part of the original input.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with a SAM-dependent methyltransferase, which makes the methyltransferase options more plausible than the oxidoreductase option D. But that broad feature does not distinguish EC 2.1.1.392 from the other methyltransferase choices: the exact substrate and reaction specificity is the deciding information.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The enzyme's experimentally established substrate and product specificity, or a characterized homolog that establishes the same specificity.",
    "reason": "The sequence offers a transferable clue to methyltransferase activity, but not a credible basis for selecting this particular EC subclass over the other methyltransferase alternatives. The precise reaction assignment depends on information about this protein or a sufficiently characterized homolog that is absent from the input."
  },
  "case_id": "EC_number_0035",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6"
    ],
    "judgment": "supported",
    "reason": "The matched sequence is annotated as EC 2.1.1.392, with cited experimental evidence for methylation reactions involving norajmaline and 4-methylnorajmaline. This supports choice C."
  },
  "important_caveats": [
    "The reviewer-only evidence matches the supplied sequence and cites experimental evidence for the annotated reactions; those annotations were not part of the original input."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The evidence supports one EC assignment for the protein; insufficient sequence information to infer that assignment is not itself evidence that multiple choices are correct."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0035",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The matched sequence is annotated as EC 2.1.1.392, with cited experimental evidence for methylation reactions involving norajmaline and 4-methylnorajmaline. This supports choice C.",
    "evidence_ids": ["C5", "C6"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence is consistent with a SAM-dependent methyltransferase, which makes the methyltransferase options more plausible than the oxidoreductase option D. But that broad feature does not distinguish EC 2.1.1.392 from the other methyltransferase choices: the exact substrate and reaction specificity is the deciding information.",
    "missing_item_specific_fact": "The enzyme's experimentally established substrate and product specificity, or a characterized homolog that establishes the same specificity.",
    "reason": "The sequence offers a transferable clue to methyltransferase activity, but not a credible basis for selecting this particular EC subclass over the other methyltransferase alternatives. The precise reaction assignment depends on information about this protein or a sufficiently characterized homolog that is absent from the input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The evidence supports one EC assignment for the protein; insufficient sequence information to infer that assignment is not itself evidence that multiple choices are correct."
  },
  "important_caveats": [
    "The reviewer-only evidence matches the supplied sequence and cites experimental evidence for the annotated reactions; those annotations were not part of the original input."
  ]
}
```

</details>

## After: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A0A075D6M1 (NNMT_RAUSE) is annotated with EC 2.1.1.392 (Norajmaline N-methyltransferase) with experimental evidence (ECO:0000269, PubMed:38212296). The catalytic activity is norajmaline + SAM → ajmaline + SAH + H+. The sequence SHA256 matches the benchmark input exactly.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H2](#evidence-h2), [H5](#evidence-h5), [H6](#evidence-h6).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

Empty string, as saved.


**Missing item-specific fact**

> The specific substrate specificity of this enzyme (norajmaline N-methylation to produce ajmaline, EC 2.1.1.392) versus the substrate acted upon by EC 2.1.1.395. Both EC numbers fall in the 2.1.1.39x range and belong to the same gene family of plant methyltransferases derived from gamma-tocopherol C-methyltransferase. Distinguishing which specific nitrogen/substrate this particular enzyme methylates requires knowing the experimentally determined substrate specificity of this exact protein, which is not encoded in readily interpretable sequence motifs.


**Reason**

> The model can eliminate D (1.3.1.36, oxidoreductase — wrong EC class, no FAD/NAD or CH-CH oxidoreductase motifs) and likely B (2.1.1.27, histamine N-methyltransferase — a well-characterized animal enzyme with a distinctly different sequence). However, distinguishing A (2.1.1.395) from C (2.1.1.392) requires knowing the specific substrate of this enzyme. Both are very recently assigned EC numbers for plant N-methyltransferases in the same gene family (derived from gamma-tocopherol C-methyltransferase). The sequence contains generic SAM-binding motifs (e.g., GCGVGG) common to all methyltransferases in this family, but the active-site residues that determine whether the enzyme methylates norajmaline (→2.1.1.392) versus the substrate of 2.1.1.395 are not identifiable from sequence alone without prior knowledge of this specific enzyme's experimental characterization.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "C"
]
```

> Both A (2.1.1.395) and C (2.1.1.392) are methyltransferases in the same recently assigned EC range belonging to the same plant gene family. Without knowing the exact substrate specificity determined experimentally, a model cannot reliably choose between them based on sequence features alone.


### Important caveats

- The alternative name 'Gamma-tocopherol-like methyltransferase' appears only in the reviewer-only UniProt annotation, not in the model's input.
- EC 2.1.1.392 and 2.1.1.395 are both very recent EC assignments (2024–2025 era), making them less likely to be well-represented in training data.
- The sequence does contain methyltransferase-characteristic motifs (GCGVGG, Rossmann-like fold indicators), supporting the 2.1.1.x class but not the specific last digit.
- The experimental evidence for EC 2.1.1.392 comes from in vitro enzyme assays (PubMed:27122470, PubMed:38212296), confirming the substrate specificity that cannot be inferred from sequence alone.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific substrate specificity of this enzyme (norajmaline N-methylation to produce ajmaline, EC 2.1.1.392) versus the substrate acted upon by EC 2.1.1.395. Both EC numbers fall in the 2.1.1.39x range and belong to the same gene family of plant methyltransferases derived from gamma-tocopherol C-methyltransferase. Distinguishing which specific nitrogen/substrate this particular enzyme methylates requires knowing the experimentally determined substrate specificity of this exact protein, which is not encoded in readily interpretable sequence motifs.",
    "reason": "The model can eliminate D (1.3.1.36, oxidoreductase — wrong EC class, no FAD/NAD or CH-CH oxidoreductase motifs) and likely B (2.1.1.27, histamine N-methyltransferase — a well-characterized animal enzyme with a distinctly different sequence). However, distinguishing A (2.1.1.395) from C (2.1.1.392) requires knowing the specific substrate of this enzyme. Both are very recently assigned EC numbers for plant N-methyltransferases in the same gene family (derived from gamma-tocopherol C-methyltransferase). The sequence contains generic SAM-binding motifs (e.g., GCGVGG) common to all methyltransferases in this family, but the active-site residues that determine whether the enzyme methylates norajmaline (→2.1.1.392) versus the substrate of 2.1.1.395 are not identifiable from sequence alone without prior knowledge of this specific enzyme's experimental characterization."
  },
  "case_id": "EC_number_0035",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H2",
      "H5",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry A0A075D6M1 (NNMT_RAUSE) is annotated with EC 2.1.1.392 (Norajmaline N-methyltransferase) with experimental evidence (ECO:0000269, PubMed:38212296). The catalytic activity is norajmaline + SAM → ajmaline + SAH + H+. The sequence SHA256 matches the benchmark input exactly."
  },
  "important_caveats": [
    "The alternative name 'Gamma-tocopherol-like methyltransferase' appears only in the reviewer-only UniProt annotation, not in the model's input.",
    "EC 2.1.1.392 and 2.1.1.395 are both very recent EC assignments (2024–2025 era), making them less likely to be well-represented in training data.",
    "The sequence does contain methyltransferase-characteristic motifs (GCGVGG, Rossmann-like fold indicators), supporting the 2.1.1.x class but not the specific last digit.",
    "The experimental evidence for EC 2.1.1.392 comes from in vitro enzyme assays (PubMed:27122470, PubMed:38212296), confirming the substrate specificity that cannot be inferred from sequence alone."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "C"
    ],
    "reason": "Both A (2.1.1.395) and C (2.1.1.392) are methyltransferases in the same recently assigned EC range belonging to the same plant gene family. Without knowing the exact substrate specificity determined experimentally, a model cannot reliably choose between them based on sequence features alone."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0035",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A0A075D6M1 (NNMT_RAUSE) is annotated with EC 2.1.1.392 (Norajmaline N-methyltransferase) with experimental evidence (ECO:0000269, PubMed:38212296). The catalytic activity is norajmaline + SAM → ajmaline + SAH + H+. The sequence SHA256 matches the benchmark input exactly.",
    "evidence_ids": ["C4", "C5", "C6", "H2", "H5", "H6"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "",
    "missing_item_specific_fact": "The specific substrate specificity of this enzyme (norajmaline N-methylation to produce ajmaline, EC 2.1.1.392) versus the substrate acted upon by EC 2.1.1.395. Both EC numbers fall in the 2.1.1.39x range and belong to the same gene family of plant methyltransferases derived from gamma-tocopherol C-methyltransferase. Distinguishing which specific nitrogen/substrate this particular enzyme methylates requires knowing the experimentally determined substrate specificity of this exact protein, which is not encoded in readily interpretable sequence motifs.",
    "reason": "The model can eliminate D (1.3.1.36, oxidoreductase — wrong EC class, no FAD/NAD or CH-CH oxidoreductase motifs) and likely B (2.1.1.27, histamine N-methyltransferase — a well-characterized animal enzyme with a distinctly different sequence). However, distinguishing A (2.1.1.395) from C (2.1.1.392) requires knowing the specific substrate of this enzyme. Both are very recently assigned EC numbers for plant N-methyltransferases in the same gene family (derived from gamma-tocopherol C-methyltransferase). The sequence contains generic SAM-binding motifs (e.g., GCGVGG) common to all methyltransferases in this family, but the active-site residues that determine whether the enzyme methylates norajmaline (→2.1.1.392) versus the substrate of 2.1.1.395 are not identifiable from sequence alone without prior knowledge of this specific enzyme's experimental characterization."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "C"],
    "reason": "Both A (2.1.1.395) and C (2.1.1.392) are methyltransferases in the same recently assigned EC range belonging to the same plant gene family. Without knowing the exact substrate specificity determined experimentally, a model cannot reliably choose between them based on sequence features alone."
  },
  "important_caveats": [
    "The alternative name 'Gamma-tocopherol-like methyltransferase' appears only in the reviewer-only UniProt annotation, not in the model's input.",
    "EC 2.1.1.392 and 2.1.1.395 are both very recent EC assignments (2024–2025 era), making them less likely to be well-represented in training data.",
    "The sequence does contain methyltransferase-characteristic motifs (GCGVGG, Rossmann-like fold indicators), supporting the 2.1.1.x class but not the specific last digit.",
    "The experimental evidence for EC 2.1.1.392 comes from in vitro enzyme assays (PubMed:27122470, PubMed:38212296), confirming the substrate specificity that cannot be inferred from sequence alone."
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
  "requested_accession": "A0A075D6M1",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "benchmark_sequence_sha256": "1d64f8836757be86aab995d1a14b3feb88531eb4212b35fbfd7dbdc62567e997",
  "benchmark_sequence_length": 292,
  "current_status": "retrieved",
  "current_sequence_comparison": "matched",
  "current_entry_audit": {
    "entryVersion": 38,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2014-10-29",
    "sequenceVersion": 1
  },
  "current_uniprot_release": "2026_03",
  "current_record_sha256": "3bb9ffb2ae03473556ed523492c0744d518e1d741d7bd4b3a3fc9dc695f623a9",
  "current_source_sequence_sha256": "1d64f8836757be86aab995d1a14b3feb88531eb4212b35fbfd7dbdc62567e997",
  "current_source_sequence_length": 292,
  "historical_status": "retrieved",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "selected_historical_entry_version": 36,
  "selected_historical_version": {
    "accession": "A0A075D6M1",
    "database": "Swiss-Prot",
    "entryVersion": 36,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "NNMT_RAUSE",
    "sequenceVersion": 1
  },
  "selected_historical_record_sha256": "ea487ae2513c784ecb9c3536d3436f3ff3869372e436c3eb33f2b9b462f39efa",
  "selected_historical_source_sequence_sha256": "1d64f8836757be86aab995d1a14b3feb88531eb4212b35fbfd7dbdc62567e997",
  "selected_historical_source_sequence_length": 292,
  "latest_at_cutoff_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 36,
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A075D6M1.json)

```json
{
  "evidence_id": "C1",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A075D6M1.json",
  "source_sha256": "3bb9ffb2ae03473556ed523492c0744d518e1d741d7bd4b3a3fc9dc695f623a9",
  "retrieved_utc": "2026-11-01T06:24:36.783284+00:00",
  "json_pointer": "/primaryAccession",
  "excerpt": "\"A0A075D6M1\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A075D6M1.json)

```json
{
  "evidence_id": "C2",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A075D6M1.json",
  "source_sha256": "3bb9ffb2ae03473556ed523492c0744d518e1d741d7bd4b3a3fc9dc695f623a9",
  "retrieved_utc": "2026-11-01T06:24:36.783284+00:00",
  "json_pointer": "/entryAudit",
  "excerpt": "{\"entryVersion\":38,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2014-10-29\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A075D6M1.json)

```json
{
  "evidence_id": "C3",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A075D6M1.json",
  "source_sha256": "3bb9ffb2ae03473556ed523492c0744d518e1d741d7bd4b3a3fc9dc695f623a9",
  "retrieved_utc": "2026-11-01T06:24:36.783284+00:00",
  "json_pointer": "/organism",
  "excerpt": "{\"commonName\":\"Serpentine wood\",\"lineage\":[\"Eukaryota\",\"Viridiplantae\",\"Streptophyta\",\"Embryophyta\",\"Tracheophyta\",\"Spermatophyta\",\"Magnoliopsida\",\"eudicotyledons\",\"Gunneridae\",\"Pentapetalae\",\"asterids\",\"lamiids\",\"Gentianales\",\"Apocynaceae\",\"Rauvolfioideae\",\"Vinceae\",\"Rauvolfiinae\",\"Rauvolfia\"],\"scientificName\":\"Rauvolfia serpentina\",\"synonyms\":[\"Ophioxylon serpentinum\"],\"taxonId\":4060}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A075D6M1.json)

```json
{
  "evidence_id": "C4",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A075D6M1.json",
  "source_sha256": "3bb9ffb2ae03473556ed523492c0744d518e1d741d7bd4b3a3fc9dc695f623a9",
  "retrieved_utc": "2026-11-01T06:24:36.783284+00:00",
  "json_pointer": "/proteinDescription",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"AHH02781.1\",\"source\":\"EMBL\"}],\"value\":\"Gamma-tocopherol-like methyltransferase NNMT\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38212296\",\"source\":\"PubMed\"}],\"value\":\"2.1.1.392\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"27122470\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000303\",\"id\":\"38212296\",\"source\":\"PubMed\"}],\"value\":\"Norajmaline N-methyltransferase\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"27122470\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000303\",\"id\":\"38212296\",\"source\":\"PubMed\"}],\"value\":\"RsNNMT\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A075D6M1.json)

```json
{
  "evidence_id": "C5",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A075D6M1.json",
  "source_sha256": "3bb9ffb2ae03473556ed523492c0744d518e1d741d7bd4b3a3fc9dc695f623a9",
  "retrieved_utc": "2026-11-01T06:24:36.783284+00:00",
  "json_pointer": "/comments/1",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"27122470\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38212296\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:79600\"}}],\"reaction\":{\"ecNumber\":\"2.1.1.392\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"27122470\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38212296\",\"source\":\"PubMed\"}],\"name\":\"norajmaline + S-adenosyl-L-methionine = ajmaline + S-adenosyl-L-homocysteine + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:79599\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57856\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:58567\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:59789\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:77618\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A075D6M1.json)

```json
{
  "evidence_id": "C6",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A075D6M1.json",
  "source_sha256": "3bb9ffb2ae03473556ed523492c0744d518e1d741d7bd4b3a3fc9dc695f623a9",
  "retrieved_utc": "2026-11-01T06:24:36.783284+00:00",
  "json_pointer": "/comments/2",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"27122470\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:79604\"}}],\"reaction\":{\"ecNumber\":\"2.1.1.392\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"27122470\",\"source\":\"PubMed\"}],\"name\":\"4-methylnorajmaline + S-adenosyl-L-methionine = 4-methylajmaline + S-adenosyl-L-homocysteine + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:79603\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57856\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:59789\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:230509\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:230510\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A075D6M1.json)

```json
{
  "evidence_id": "C7",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A075D6M1.json",
  "source_sha256": "3bb9ffb2ae03473556ed523492c0744d518e1d741d7bd4b3a3fc9dc695f623a9",
  "retrieved_utc": "2026-11-01T06:24:36.783284+00:00",
  "json_pointer": "/references/1",
  "excerpt": "{\"citation\":{\"authors\":[\"Cazares-Flores P.\",\"Levac D.\",\"De Luca V.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"27122470\"},{\"database\":\"DOI\",\"id\":\"10.1111/tpj.13186\"}],\"citationType\":\"journal article\",\"firstPage\":\"335\",\"id\":\"27122470\",\"journal\":\"Plant J.\",\"lastPage\":\"342\",\"publicationDate\":\"2016\",\"title\":\"Rauvolfia serpentina N-methyltransferases involved in ajmaline and Nbeta -methylajmaline biosynthesis belong to a gene family derived from gamma-tocopherol C-methyltransferase.\",\"volume\":\"87\"},\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"PATHWAY\",\"TISSUE SPECIFICITY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A075D6M1.json)

```json
{
  "evidence_id": "C8",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A075D6M1.json",
  "source_sha256": "3bb9ffb2ae03473556ed523492c0744d518e1d741d7bd4b3a3fc9dc695f623a9",
  "retrieved_utc": "2026-11-01T06:24:36.783284+00:00",
  "json_pointer": "/references/2",
  "excerpt": "{\"citation\":{\"authors\":[\"Guo J.\",\"Gao D.\",\"Lian J.\",\"Qu Y.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"38212296\"},{\"database\":\"DOI\",\"id\":\"10.1038/s41467-024-44797-z\"}],\"citationType\":\"journal article\",\"firstPage\":\"457\",\"id\":\"38212296\",\"journal\":\"Nat. Commun.\",\"lastPage\":\"457\",\"publicationDate\":\"2024\",\"title\":\"De novo biosynthesis of antiarrhythmic alkaloid ajmaline.\",\"volume\":\"15\"},\"referenceNumber\":3,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"PATHWAY\",\"TISSUE SPECIFICITY\",\"BIOTECHNOLOGY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A075D6M1?format=txt&versions=36)

```json
{
  "evidence_id": "H1",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A075D6M1?format=txt&versions=36",
  "source_sha256": "ea487ae2513c784ecb9c3536d3436f3ff3869372e436c3eb33f2b9b462f39efa",
  "retrieved_utc": "2026-11-01T06:27:15.852655+00:00",
  "source_locator": "lines 1-17",
  "excerpt": "ID   NNMT_RAUSE              Reviewed;         292 AA.\nAC   A0A075D6M1;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   29-OCT-2014, sequence version 1.\nDT   28-JAN-2026, entry version 36.\nDE   RecName: Full=Norajmaline N-methyltransferase {ECO:0000303|PubMed:27122470, ECO:0000303|PubMed:38212296};\nDE            Short=RsNNMT {ECO:0000303|PubMed:27122470, ECO:0000303|PubMed:38212296};\nDE            EC=2.1.1.392 {ECO:0000269|PubMed:38212296};\nDE   AltName: Full=Gamma-tocopherol-like methyltransferase NNMT {ECO:0000312|EMBL:AHH02781.1};\nGN   Name=NNMT {ECO:0000303|PubMed:38212296};\nGN   Synonyms=Rs9447 {ECO:0000312|EMBL:AHH02781.1};\nOS   Rauvolfia serpentina (Serpentine wood) (Ophioxylon serpentinum).\nOC   Eukaryota; Viridiplantae; Streptophyta; Embryophyta; Tracheophyta;\nOC   Spermatophyta; Magnoliopsida; eudicotyledons; Gunneridae; Pentapetalae;\nOC   asterids; lamiids; Gentianales; Apocynaceae; Rauvolfioideae; Vinceae;\nOC   Rauvolfiinae; Rauvolfia.\nOX   NCBI_TaxID=4060;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 36,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A075D6M1?format=txt&versions=36)

```json
{
  "evidence_id": "H2",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A075D6M1?format=txt&versions=36",
  "source_sha256": "ea487ae2513c784ecb9c3536d3436f3ff3869372e436c3eb33f2b9b462f39efa",
  "retrieved_utc": "2026-11-01T06:27:15.852655+00:00",
  "source_locator": "lines 6-9",
  "excerpt": "DE   RecName: Full=Norajmaline N-methyltransferase {ECO:0000303|PubMed:27122470, ECO:0000303|PubMed:38212296};\nDE            Short=RsNNMT {ECO:0000303|PubMed:27122470, ECO:0000303|PubMed:38212296};\nDE            EC=2.1.1.392 {ECO:0000269|PubMed:38212296};\nDE   AltName: Full=Gamma-tocopherol-like methyltransferase NNMT {ECO:0000312|EMBL:AHH02781.1};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 36,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A075D6M1?format=txt&versions=36)

```json
{
  "evidence_id": "H3",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A075D6M1?format=txt&versions=36",
  "source_sha256": "ea487ae2513c784ecb9c3536d3436f3ff3869372e436c3eb33f2b9b462f39efa",
  "retrieved_utc": "2026-11-01T06:27:15.852655+00:00",
  "source_locator": "lines 27-35",
  "excerpt": "RN   [2]\nRP   FUNCTION, CATALYTIC ACTIVITY, BIOPHYSICOCHEMICAL PROPERTIES, PATHWAY, AND\nRP   TISSUE SPECIFICITY.\nRX   PubMed=27122470; DOI=10.1111/tpj.13186;\nRA   Cazares-Flores P., Levac D., De Luca V.;\nRT   \"Rauvolfia serpentina N-methyltransferases involved in ajmaline and Nbeta\nRT   -methylajmaline biosynthesis belong to a gene family derived from gamma-\nRT   tocopherol C-methyltransferase.\";\nRL   Plant J. 87:335-342(2016).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 36,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A075D6M1?format=txt&versions=36)

```json
{
  "evidence_id": "H4",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A075D6M1?format=txt&versions=36",
  "source_sha256": "ea487ae2513c784ecb9c3536d3436f3ff3869372e436c3eb33f2b9b462f39efa",
  "retrieved_utc": "2026-11-01T06:27:15.852655+00:00",
  "source_locator": "lines 36-42",
  "excerpt": "RN   [3]\nRP   FUNCTION, CATALYTIC ACTIVITY, PATHWAY, TISSUE SPECIFICITY, AND\nRP   BIOTECHNOLOGY.\nRX   PubMed=38212296; DOI=10.1038/s41467-024-44797-z;\nRA   Guo J., Gao D., Lian J., Qu Y.;\nRT   \"De novo biosynthesis of antiarrhythmic alkaloid ajmaline.\";\nRL   Nat. Commun. 15:457-457(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 36,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A075D6M1?format=txt&versions=36)

```json
{
  "evidence_id": "H5",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A075D6M1?format=txt&versions=36",
  "source_sha256": "ea487ae2513c784ecb9c3536d3436f3ff3869372e436c3eb33f2b9b462f39efa",
  "retrieved_utc": "2026-11-01T06:27:15.852655+00:00",
  "source_locator": "lines 51-58",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=norajmaline + S-adenosyl-L-methionine = ajmaline + S-adenosyl-\nCC         L-homocysteine + H(+); Xref=Rhea:RHEA:79599, ChEBI:CHEBI:15378,\nCC         ChEBI:CHEBI:57856, ChEBI:CHEBI:58567, ChEBI:CHEBI:59789,\nCC         ChEBI:CHEBI:77618; EC=2.1.1.392;\nCC         Evidence={ECO:0000269|PubMed:27122470, ECO:0000269|PubMed:38212296};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:79600;\nCC         Evidence={ECO:0000269|PubMed:27122470, ECO:0000269|PubMed:38212296};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 36,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A075D6M1?format=txt&versions=36)

```json
{
  "evidence_id": "H6",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A075D6M1?format=txt&versions=36",
  "source_sha256": "ea487ae2513c784ecb9c3536d3436f3ff3869372e436c3eb33f2b9b462f39efa",
  "retrieved_utc": "2026-11-01T06:27:15.852655+00:00",
  "source_locator": "lines 59-66",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=4-methylnorajmaline + S-adenosyl-L-methionine = 4-\nCC         methylajmaline + S-adenosyl-L-homocysteine + H(+);\nCC         Xref=Rhea:RHEA:79603, ChEBI:CHEBI:15378, ChEBI:CHEBI:57856,\nCC         ChEBI:CHEBI:59789, ChEBI:CHEBI:230509, ChEBI:CHEBI:230510;\nCC         EC=2.1.1.392; Evidence={ECO:0000269|PubMed:27122470};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:79604;\nCC         Evidence={ECO:0000269|PubMed:27122470};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 36,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 35. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
