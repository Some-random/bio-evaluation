# catalytic_activity_0085: before and after transfer clarification

[All 1,328 cases](../README.md) · [Method](../METHOD.md) · [Summary](../SUMMARY.md) · [Exact reviewer user message](../inputs/catalytic_activity_0085.txt)

**Task:** `catalytic_activity`  
**Author key, unchanged:** **D** — (19E)-geissoschizine + NADP(+) = 4,21-dehydrogeissoschizine + NADPH

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
MAGETTQLDLSVKAVGWGAADASGTLQPIKFYRRTPGERDVKIRVLYCGVCNFDMEMVRNKWGFTRYPYVFGHETAGEVIEVGSKVQKFKVGDKVGVGCMVGSCGKCFNCQNGMENYCPEPNMADGSVYREQQGEPSFGGCSNVMVVDEKFVLRWPENLPQDTGVPLLCAGIVVYSPMKYMGLDKPGKHIGVIGLGGLGSIAVKFIKAFGGKATVISTSKRKEKEAIEEHGADAFVVNTDTEKLQALAGTMDGVVDTTPGGRTPMSLMLNLLKFDGVVLLVGAPETLFELPVQPLILGRRKIIGSSTGGLKEYQETLDFAAQHNIVCDTEVIGIDYLSTAMERIKNLDVKYRFAIDIGNTLKYED

[Multiple Choices]
A. a cytidine in tRNA + acetyl-CoA + ATP + H2O = an N(4)-acetylcytidine in tRNA + ADP + phosphate + CoA + H(+)
B. acetaldehyde + NAD(+) + H2O = acetate + NADH + 2 H(+)
C. NAD(+) + H2O = ADP-D-ribose + nicotinamide + H(+)
D. (19E)-geissoschizine + NADP(+) = 4,21-dehydrogeissoschizine + NADPH
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

> The supplied sequence exactly matches the UniProt entry annotated as geissoschizine synthase, and that entry lists choice D as its catalytic reaction. However, the reaction annotation is transferred by similarity from UniProtKB:W8JWW7 (ECO:0000250), so it supports the key as a database annotation rather than establishing direct experimental verification for this exact protein.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence alone may suggest an enzyme with oxidoreductase-related features, but it does not provide a defensible way to identify geissoschizine or the specific 4,21-dehydrogenation among the choices.


**Missing item-specific fact**

> The protein-specific functional annotation or experimental substrate/reaction information identifying this sequence as geissoschizine synthase.


**Reason**

> Selecting D requires an item-specific functional association absent from the input. General sequence reasoning does not distinguish this specialized alkaloid reaction from other possible enzyme activities.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The options describe distinct reactions, and the matched database annotation supports D; the limitation concerns whether that reaction can be inferred from the input, not ambiguity between the listed reactions.


### Important caveats

- The reviewer-only evidence identifies a sequence-matched database record, but that identity and annotation were not supplied to the evaluated model.
- The catalytic reaction evidence is transferred by similarity from another UniProt entry; it is not presented here as a direct experimental measurement for this exact sequence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence alone may suggest an enzyme with oxidoreductase-related features, but it does not provide a defensible way to identify geissoschizine or the specific 4,21-dehydrogenation among the choices.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific functional annotation or experimental substrate/reaction information identifying this sequence as geissoschizine synthase.",
    "reason": "Selecting D requires an item-specific functional association absent from the input. General sequence reasoning does not distinguish this specialized alkaloid reaction from other possible enzyme activities."
  },
  "case_id": "catalytic_activity_0085",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the UniProt entry annotated as geissoschizine synthase, and that entry lists choice D as its catalytic reaction. However, the reaction annotation is transferred by similarity from UniProtKB:W8JWW7 (ECO:0000250), so it supports the key as a database annotation rather than establishing direct experimental verification for this exact protein."
  },
  "important_caveats": [
    "The reviewer-only evidence identifies a sequence-matched database record, but that identity and annotation were not supplied to the evaluated model.",
    "The catalytic reaction evidence is transferred by similarity from another UniProt entry; it is not presented here as a direct experimental measurement for this exact sequence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The options describe distinct reactions, and the matched database annotation supports D; the limitation concerns whether that reaction can be inferred from the input, not ambiguity between the listed reactions."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0085",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the UniProt entry annotated as geissoschizine synthase, and that entry lists choice D as its catalytic reaction. However, the reaction annotation is transferred by similarity from UniProtKB:W8JWW7 (ECO:0000250), so it supports the key as a database annotation rather than establishing direct experimental verification for this exact protein.",
    "evidence_ids": ["C1", "C4", "C5", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence alone may suggest an enzyme with oxidoreductase-related features, but it does not provide a defensible way to identify geissoschizine or the specific 4,21-dehydrogenation among the choices.",
    "missing_item_specific_fact": "The protein-specific functional annotation or experimental substrate/reaction information identifying this sequence as geissoschizine synthase.",
    "reason": "Selecting D requires an item-specific functional association absent from the input. General sequence reasoning does not distinguish this specialized alkaloid reaction from other possible enzyme activities."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The options describe distinct reactions, and the matched database annotation supports D; the limitation concerns whether that reaction can be inferred from the input, not ambiguity between the listed reactions."
  },
  "important_caveats": [
    "The reviewer-only evidence identifies a sequence-matched database record, but that identity and annotation were not supplied to the evaluated model.",
    "The catalytic reaction evidence is transferred by similarity from another UniProt entry; it is not presented here as a direct experimental measurement for this exact sequence."
  ]
}
```

</details>

## Before: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The supplied sequence (365 aa, SHA-256 matched) corresponds exactly to UniProt P0DXJ1 (GS_RAUSE, Geissoschizine synthase, EC 1.3.1.36) from Rauvolfia serpentina. The annotated catalytic activity (C5, H4) is verbatim: '(19E)-geissoschizine + NADP(+) = 4,21-dehydrogeissoschizine + NADPH', matching choice D. The EC number carries evidence code ECO:0000250 (inferred by similarity to W8JWW7), while the protein name and functional context are supported by PubMed 38212296 (Nat. Commun. 2024, Guo et al.) with evidence code ECO:0000312 (experimental). The physiological direction is noted as right-to-left (RHEA:11378), but the canonical reaction equation as written in choice D matches RHEA:11376 as annotated. The answer is supported by the database annotation and the underlying experimental publication.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence contains Rossmann-fold-like motifs (e.g., 'GGLGS' near residue ~170, 'GAPETL' near ~230) consistent with NAD(P)-dependent oxidoreductase activity, which could plausibly help eliminate choice A (tRNA acetyltransferase using acetyl-CoA/ATP, no Rossmann fold) and choice C (NADase, entirely different mechanism and fold). However, distinguishing choice B (acetaldehyde dehydrogenase, NAD+-dependent) from choice D (geissoschizine synthase, NADP+-dependent alkaloid dehydrogenase) requires knowing the specific substrate identity (geissoschizine, a monoterpenoid indole alkaloid) and the specific dehydrogenation positions (4,21). No general sequence motif uniquely encodes 'this is a Rauvolfia alkaloid dehydrogenase acting on geissoschizine.'


**Missing item-specific fact**

> The identity of the specific natural-product substrate (geissoschizine) and the regiochemistry of dehydrogenation (4,21-dehydro) are item-specific facts that cannot be deduced from the amino acid sequence by general biological reasoning. The protein's association with Rauvolfia serpentina alkaloid biosynthesis (from PubMed 38212296) and the precise EC 1.3.1.36 assignment are database/experimental annotations absent from the model input.


**Reason**

> While Rossmann-fold motifs narrow the class to NAD(P)-dependent oxidoreductases (eliminating A and C with moderate confidence), the choice between a generic aldehyde dehydrogenase (B) and a highly specific plant alkaloid dehydrogenase (D) cannot be resolved by sequence reasoning alone. Identifying geissoschizine synthase requires recognizing this particular protein or its database annotation, making the question lookup-dependent.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Given the annotation evidence, only D matches the catalytic activity of P0DXJ1. Choices A, B, and C describe mechanistically distinct reactions (acetyltransferase, aldehyde dehydrogenase, NADase) inconsistent with the observed Rossmann-fold oxidoreductase architecture and the specific EC 1.3.1.36 annotation. No ambiguity in the correct answer exists from the evidence standpoint, though from the model's reasoning standpoint B is a closer distractor than A or C.


### Important caveats

- The EC number assignment carries ECO:0000250 (inferred by similarity to W8JWW7), meaning the reaction annotation is transferred rather than directly measured on P0DXJ1 itself. The PubMed 38212296 reference (Guo et al., Nat. Commun. 2024) provides experimental context for the ajmaline biosynthesis pathway including this step.
- The physiological direction is annotated as right-to-left (RHEA:11378), meaning in vivo the enzyme likely catalyzes 4,21-dehydrogeissoschizine + NADPH → (19E)-geissoschizine + NADP+. The multiple-choice option D presents the reaction in the canonical (left-to-right) direction per RHEA:11376, which is standard practice in EC annotations.
- The UniProt entry was first public on 2025-06-18; the historical record (entry version 2) was released 2026-01-28. The sequence match is confirmed across both current and historical snapshots.
- The reviewer-only evidence was not available to the evaluated model; the model must rely solely on the 365-aa sequence and the four reaction choices.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains Rossmann-fold-like motifs (e.g., 'GGLGS' near residue ~170, 'GAPETL' near ~230) consistent with NAD(P)-dependent oxidoreductase activity, which could plausibly help eliminate choice A (tRNA acetyltransferase using acetyl-CoA/ATP, no Rossmann fold) and choice C (NADase, entirely different mechanism and fold). However, distinguishing choice B (acetaldehyde dehydrogenase, NAD+-dependent) from choice D (geissoschizine synthase, NADP+-dependent alkaloid dehydrogenase) requires knowing the specific substrate identity (geissoschizine, a monoterpenoid indole alkaloid) and the specific dehydrogenation positions (4,21). No general sequence motif uniquely encodes 'this is a Rauvolfia alkaloid dehydrogenase acting on geissoschizine.'",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The identity of the specific natural-product substrate (geissoschizine) and the regiochemistry of dehydrogenation (4,21-dehydro) are item-specific facts that cannot be deduced from the amino acid sequence by general biological reasoning. The protein's association with Rauvolfia serpentina alkaloid biosynthesis (from PubMed 38212296) and the precise EC 1.3.1.36 assignment are database/experimental annotations absent from the model input.",
    "reason": "While Rossmann-fold motifs narrow the class to NAD(P)-dependent oxidoreductases (eliminating A and C with moderate confidence), the choice between a generic aldehyde dehydrogenase (B) and a highly specific plant alkaloid dehydrogenase (D) cannot be resolved by sequence reasoning alone. Identifying geissoschizine synthase requires recognizing this particular protein or its database annotation, making the question lookup-dependent."
  },
  "case_id": "catalytic_activity_0085",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H2",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence (365 aa, SHA-256 matched) corresponds exactly to UniProt P0DXJ1 (GS_RAUSE, Geissoschizine synthase, EC 1.3.1.36) from Rauvolfia serpentina. The annotated catalytic activity (C5, H4) is verbatim: '(19E)-geissoschizine + NADP(+) = 4,21-dehydrogeissoschizine + NADPH', matching choice D. The EC number carries evidence code ECO:0000250 (inferred by similarity to W8JWW7), while the protein name and functional context are supported by PubMed 38212296 (Nat. Commun. 2024, Guo et al.) with evidence code ECO:0000312 (experimental). The physiological direction is noted as right-to-left (RHEA:11378), but the canonical reaction equation as written in choice D matches RHEA:11376 as annotated. The answer is supported by the database annotation and the underlying experimental publication."
  },
  "important_caveats": [
    "The EC number assignment carries ECO:0000250 (inferred by similarity to W8JWW7), meaning the reaction annotation is transferred rather than directly measured on P0DXJ1 itself. The PubMed 38212296 reference (Guo et al., Nat. Commun. 2024) provides experimental context for the ajmaline biosynthesis pathway including this step.",
    "The physiological direction is annotated as right-to-left (RHEA:11378), meaning in vivo the enzyme likely catalyzes 4,21-dehydrogeissoschizine + NADPH → (19E)-geissoschizine + NADP+. The multiple-choice option D presents the reaction in the canonical (left-to-right) direction per RHEA:11376, which is standard practice in EC annotations.",
    "The UniProt entry was first public on 2025-06-18; the historical record (entry version 2) was released 2026-01-28. The sequence match is confirmed across both current and historical snapshots.",
    "The reviewer-only evidence was not available to the evaluated model; the model must rely solely on the 365-aa sequence and the four reaction choices."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Given the annotation evidence, only D matches the catalytic activity of P0DXJ1. Choices A, B, and C describe mechanistically distinct reactions (acetyltransferase, aldehyde dehydrogenase, NADase) inconsistent with the observed Rossmann-fold oxidoreductase architecture and the specific EC 1.3.1.36 annotation. No ambiguity in the correct answer exists from the evidence standpoint, though from the model's reasoning standpoint B is a closer distractor than A or C."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0085",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence (365 aa, SHA-256 matched) corresponds exactly to UniProt P0DXJ1 (GS_RAUSE, Geissoschizine synthase, EC 1.3.1.36) from Rauvolfia serpentina. The annotated catalytic activity (C5, H4) is verbatim: '(19E)-geissoschizine + NADP(+) = 4,21-dehydrogeissoschizine + NADPH', matching choice D. The EC number carries evidence code ECO:0000250 (inferred by similarity to W8JWW7), while the protein name and functional context are supported by PubMed 38212296 (Nat. Commun. 2024, Guo et al.) with evidence code ECO:0000312 (experimental). The physiological direction is noted as right-to-left (RHEA:11378), but the canonical reaction equation as written in choice D matches RHEA:11376 as annotated. The answer is supported by the database annotation and the underlying experimental publication.",
    "evidence_ids": ["C1", "C4", "C5", "H2", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence contains Rossmann-fold-like motifs (e.g., 'GGLGS' near residue ~170, 'GAPETL' near ~230) consistent with NAD(P)-dependent oxidoreductase activity, which could plausibly help eliminate choice A (tRNA acetyltransferase using acetyl-CoA/ATP, no Rossmann fold) and choice C (NADase, entirely different mechanism and fold). However, distinguishing choice B (acetaldehyde dehydrogenase, NAD+-dependent) from choice D (geissoschizine synthase, NADP+-dependent alkaloid dehydrogenase) requires knowing the specific substrate identity (geissoschizine, a monoterpenoid indole alkaloid) and the specific dehydrogenation positions (4,21). No general sequence motif uniquely encodes 'this is a Rauvolfia alkaloid dehydrogenase acting on geissoschizine.'",
    "missing_item_specific_fact": "The identity of the specific natural-product substrate (geissoschizine) and the regiochemistry of dehydrogenation (4,21-dehydro) are item-specific facts that cannot be deduced from the amino acid sequence by general biological reasoning. The protein's association with Rauvolfia serpentina alkaloid biosynthesis (from PubMed 38212296) and the precise EC 1.3.1.36 assignment are database/experimental annotations absent from the model input.",
    "reason": "While Rossmann-fold motifs narrow the class to NAD(P)-dependent oxidoreductases (eliminating A and C with moderate confidence), the choice between a generic aldehyde dehydrogenase (B) and a highly specific plant alkaloid dehydrogenase (D) cannot be resolved by sequence reasoning alone. Identifying geissoschizine synthase requires recognizing this particular protein or its database annotation, making the question lookup-dependent."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Given the annotation evidence, only D matches the catalytic activity of P0DXJ1. Choices A, B, and C describe mechanistically distinct reactions (acetyltransferase, aldehyde dehydrogenase, NADase) inconsistent with the observed Rossmann-fold oxidoreductase architecture and the specific EC 1.3.1.36 annotation. No ambiguity in the correct answer exists from the evidence standpoint, though from the model's reasoning standpoint B is a closer distractor than A or C."
  },
  "important_caveats": [
    "The EC number assignment carries ECO:0000250 (inferred by similarity to W8JWW7), meaning the reaction annotation is transferred rather than directly measured on P0DXJ1 itself. The PubMed 38212296 reference (Guo et al., Nat. Commun. 2024) provides experimental context for the ajmaline biosynthesis pathway including this step.",
    "The physiological direction is annotated as right-to-left (RHEA:11378), meaning in vivo the enzyme likely catalyzes 4,21-dehydrogeissoschizine + NADPH → (19E)-geissoschizine + NADP+. The multiple-choice option D presents the reaction in the canonical (left-to-right) direction per RHEA:11376, which is standard practice in EC annotations.",
    "The UniProt entry was first public on 2025-06-18; the historical record (entry version 2) was released 2026-01-28. The sequence match is confirmed across both current and historical snapshots.",
    "The reviewer-only evidence was not available to the evaluated model; the model must rely solely on the 365-aa sequence and the four reaction choices."
  ]
}
```

</details>

## After: GPT-6 Luna

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The matched sequence is annotated with the reaction in choice D in both the current and archived UniProt records. The annotation is transferred by similarity (ECO:0000250, to W8JWW7), so it supports the key but is not direct experimental evidence for this exact sequence.

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

Empty string, as saved.


**Missing item-specific fact**

> That this sequence has geissoschizine-synthase activity, including specificity for the geissoschizine-to-dehydrogeissoschizine transformation.


**Reason**

> The sequence may suggest a cofactor-dependent enzyme, but that broad inference does not establish its substrate or distinguish choice D from the NAD-dependent oxidation in B. Choices A and C describe different reaction types, yet identifying the specific alkaloid transformation requires the enzyme's substrate specificity or a sufficiently recognizable homolog assignment, neither of which is established by the original input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The supplied sequence-matched annotation supports D; no second option is supported by the reviewer evidence.


### Important caveats

- The database reaction annotation is similarity-transferred rather than direct experimental evidence for this exact protein.
- The reviewer-only identity and annotation evidence were not available as original inputs and do not count as transferable evidence for answerability.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "That this sequence has geissoschizine-synthase activity, including specificity for the geissoschizine-to-dehydrogeissoschizine transformation.",
    "reason": "The sequence may suggest a cofactor-dependent enzyme, but that broad inference does not establish its substrate or distinguish choice D from the NAD-dependent oxidation in B. Choices A and C describe different reaction types, yet identifying the specific alkaloid transformation requires the enzyme's substrate specificity or a sufficiently recognizable homolog assignment, neither of which is established by the original input."
  },
  "case_id": "catalytic_activity_0085",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The matched sequence is annotated with the reaction in choice D in both the current and archived UniProt records. The annotation is transferred by similarity (ECO:0000250, to W8JWW7), so it supports the key but is not direct experimental evidence for this exact sequence."
  },
  "important_caveats": [
    "The database reaction annotation is similarity-transferred rather than direct experimental evidence for this exact protein.",
    "The reviewer-only identity and annotation evidence were not available as original inputs and do not count as transferable evidence for answerability."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied sequence-matched annotation supports D; no second option is supported by the reviewer evidence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0085",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The matched sequence is annotated with the reaction in choice D in both the current and archived UniProt records. The annotation is transferred by similarity (ECO:0000250, to W8JWW7), so it supports the key but is not direct experimental evidence for this exact sequence.",
    "evidence_ids": ["C1", "C5", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "",
    "missing_item_specific_fact": "That this sequence has geissoschizine-synthase activity, including specificity for the geissoschizine-to-dehydrogeissoschizine transformation.",
    "reason": "The sequence may suggest a cofactor-dependent enzyme, but that broad inference does not establish its substrate or distinguish choice D from the NAD-dependent oxidation in B. Choices A and C describe different reaction types, yet identifying the specific alkaloid transformation requires the enzyme's substrate specificity or a sufficiently recognizable homolog assignment, neither of which is established by the original input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied sequence-matched annotation supports D; no second option is supported by the reviewer evidence."
  },
  "important_caveats": [
    "The database reaction annotation is similarity-transferred rather than direct experimental evidence for this exact protein.",
    "The reviewer-only identity and annotation evidence were not available as original inputs and do not count as transferable evidence for answerability."
  ]
}
```

</details>

## After: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry P0DXJ1 (Geissoschizine synthase, EC 1.3.1.36) explicitly annotates the catalytic reaction as '(19E)-geissoschizine + NADP(+) = 4,21-dehydrogeissoschizine + NADPH' (evidence codes ECO:0000250 by similarity to W8JWW7 for the EC number; ECO:0000303 from PubMed:38212296 for protein name and function). The sequence in the question matches the UniProt entry (SHA-256 confirmed). The 2024 Nature Communications paper (Guo et al.) experimentally characterized this enzyme in the ajmaline biosynthetic pathway. The expected answer D exactly matches the annotated reaction.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H4](#evidence-h4), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a canonical Rossmann-fold NAD(P)-binding motif 'GGLGSIAVK' (GxGxxG pattern), identifying the protein as an NAD(P)-dependent oxidoreductase. This eliminates option A (a transferase using acetyl-CoA/ATP, which would show CoA-binding motifs and transferase architecture) and option C (a hydrolase cleaving NAD+, which lacks oxidoreductase architecture). Between B (acetaldehyde dehydrogenase, EC 1.2.1.10) and D (NADP+-dependent oxidoreductase, EC 1.3.1.36): the protein is ~365 aa, far shorter than the ~500–550 aa ALDH superfamily to which acetaldehyde dehydrogenase belongs; it also lacks the hallmark ALDH catalytic cysteine in its conserved context and the characteristic ALDH 'GQGLG' motif. The NADP+ preference is suggested by the 'GLGGLGS' arrangement around the Rossmann motif (an extra glycine/acidic context favoring the 2'-phosphate of NADP+). The overall plant-type secondary-metabolism oxidoreductase architecture (monoterpene indole alkaloid pathway enzymes are typically 300–400 aa NADP+-dependent dehydrogenases) is consistent with D. Among the four offered choices, D is the only NADP+-dependent oxidoreductase of the correct size and family, making it the uniquely consistent answer.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can eliminate A (wrong enzyme class—transferase), C (wrong enzyme class—hydrolase), and B (wrong family/size—ALDH superfamily is ~500+ aa with distinct motifs) using the Rossmann fold motif, protein length, and family-level knowledge of oxidoreductases. The remaining option D is the only NADP+-dependent oxidoreductase of appropriate architecture among the choices. The model need not independently predict the substrate name 'geissoschizine'; elimination of the other three options suffices.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options span distinct enzyme classes and families (transferase, ALDH, NAD+-hydrolase, NADP+-dependent oxidoreductase). The sequence features (Rossmann fold, ~365 aa length, plant secondary-metabolism architecture, NADP+ preference signals) uniquely point to D among these four choices.


### Important caveats

- The EC 1.3.1.36 assignment in UniProt carries evidence code ECO:0000250 (similarity to W8JWW7), meaning the EC number itself is inferred by homology rather than directly measured for this exact entry; however, the protein's function was experimentally validated in the 2024 Nat. Commun. paper (PubMed:38212296).
- The specific substrate name 'geissoschizine' is highly specialized (MIA pathway); a model arriving at D does so by elimination and family-level inference rather than by independently naming the substrate.
- The physiological direction annotation notes right-to-left (RHEA:11378), meaning the enzyme may operate in the reverse direction in vivo; the written reaction as given in option D matches the UniProt forward-direction annotation.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a canonical Rossmann-fold NAD(P)-binding motif 'GGLGSIAVK' (GxGxxG pattern), identifying the protein as an NAD(P)-dependent oxidoreductase. This eliminates option A (a transferase using acetyl-CoA/ATP, which would show CoA-binding motifs and transferase architecture) and option C (a hydrolase cleaving NAD+, which lacks oxidoreductase architecture). Between B (acetaldehyde dehydrogenase, EC 1.2.1.10) and D (NADP+-dependent oxidoreductase, EC 1.3.1.36): the protein is ~365 aa, far shorter than the ~500–550 aa ALDH superfamily to which acetaldehyde dehydrogenase belongs; it also lacks the hallmark ALDH catalytic cysteine in its conserved context and the characteristic ALDH 'GQGLG' motif. The NADP+ preference is suggested by the 'GLGGLGS' arrangement around the Rossmann motif (an extra glycine/acidic context favoring the 2'-phosphate of NADP+). The overall plant-type secondary-metabolism oxidoreductase architecture (monoterpene indole alkaloid pathway enzymes are typically 300–400 aa NADP+-dependent dehydrogenases) is consistent with D. Among the four offered choices, D is the only NADP+-dependent oxidoreductase of the correct size and family, making it the uniquely consistent answer.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can eliminate A (wrong enzyme class—transferase), C (wrong enzyme class—hydrolase), and B (wrong family/size—ALDH superfamily is ~500+ aa with distinct motifs) using the Rossmann fold motif, protein length, and family-level knowledge of oxidoreductases. The remaining option D is the only NADP+-dependent oxidoreductase of appropriate architecture among the choices. The model need not independently predict the substrate name 'geissoschizine'; elimination of the other three options suffices."
  },
  "case_id": "catalytic_activity_0085",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H4",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry P0DXJ1 (Geissoschizine synthase, EC 1.3.1.36) explicitly annotates the catalytic reaction as '(19E)-geissoschizine + NADP(+) = 4,21-dehydrogeissoschizine + NADPH' (evidence codes ECO:0000250 by similarity to W8JWW7 for the EC number; ECO:0000303 from PubMed:38212296 for protein name and function). The sequence in the question matches the UniProt entry (SHA-256 confirmed). The 2024 Nature Communications paper (Guo et al.) experimentally characterized this enzyme in the ajmaline biosynthetic pathway. The expected answer D exactly matches the annotated reaction."
  },
  "important_caveats": [
    "The EC 1.3.1.36 assignment in UniProt carries evidence code ECO:0000250 (similarity to W8JWW7), meaning the EC number itself is inferred by homology rather than directly measured for this exact entry; however, the protein's function was experimentally validated in the 2024 Nat. Commun. paper (PubMed:38212296).",
    "The specific substrate name 'geissoschizine' is highly specialized (MIA pathway); a model arriving at D does so by elimination and family-level inference rather than by independently naming the substrate.",
    "The physiological direction annotation notes right-to-left (RHEA:11378), meaning the enzyme may operate in the reverse direction in vivo; the written reaction as given in option D matches the UniProt forward-direction annotation."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span distinct enzyme classes and families (transferase, ALDH, NAD+-hydrolase, NADP+-dependent oxidoreductase). The sequence features (Rossmann fold, ~365 aa length, plant secondary-metabolism architecture, NADP+ preference signals) uniquely point to D among these four choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0085",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry P0DXJ1 (Geissoschizine synthase, EC 1.3.1.36) explicitly annotates the catalytic reaction as '(19E)-geissoschizine + NADP(+) = 4,21-dehydrogeissoschizine + NADPH' (evidence codes ECO:0000250 by similarity to W8JWW7 for the EC number; ECO:0000303 from PubMed:38212296 for protein name and function). The sequence in the question matches the UniProt entry (SHA-256 confirmed). The 2024 Nature Communications paper (Guo et al.) experimentally characterized this enzyme in the ajmaline biosynthetic pathway. The expected answer D exactly matches the annotated reaction.",
    "evidence_ids": ["C4", "C5", "H4", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a canonical Rossmann-fold NAD(P)-binding motif 'GGLGSIAVK' (GxGxxG pattern), identifying the protein as an NAD(P)-dependent oxidoreductase. This eliminates option A (a transferase using acetyl-CoA/ATP, which would show CoA-binding motifs and transferase architecture) and option C (a hydrolase cleaving NAD+, which lacks oxidoreductase architecture). Between B (acetaldehyde dehydrogenase, EC 1.2.1.10) and D (NADP+-dependent oxidoreductase, EC 1.3.1.36): the protein is ~365 aa, far shorter than the ~500–550 aa ALDH superfamily to which acetaldehyde dehydrogenase belongs; it also lacks the hallmark ALDH catalytic cysteine in its conserved context and the characteristic ALDH 'GQGLG' motif. The NADP+ preference is suggested by the 'GLGGLGS' arrangement around the Rossmann motif (an extra glycine/acidic context favoring the 2'-phosphate of NADP+). The overall plant-type secondary-metabolism oxidoreductase architecture (monoterpene indole alkaloid pathway enzymes are typically 300–400 aa NADP+-dependent dehydrogenases) is consistent with D. Among the four offered choices, D is the only NADP+-dependent oxidoreductase of the correct size and family, making it the uniquely consistent answer.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can eliminate A (wrong enzyme class—transferase), C (wrong enzyme class—hydrolase), and B (wrong family/size—ALDH superfamily is ~500+ aa with distinct motifs) using the Rossmann fold motif, protein length, and family-level knowledge of oxidoreductases. The remaining option D is the only NADP+-dependent oxidoreductase of appropriate architecture among the choices. The model need not independently predict the substrate name 'geissoschizine'; elimination of the other three options suffices."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span distinct enzyme classes and families (transferase, ALDH, NAD+-hydrolase, NADP+-dependent oxidoreductase). The sequence features (Rossmann fold, ~365 aa length, plant secondary-metabolism architecture, NADP+ preference signals) uniquely point to D among these four choices."
  },
  "important_caveats": [
    "The EC 1.3.1.36 assignment in UniProt carries evidence code ECO:0000250 (similarity to W8JWW7), meaning the EC number itself is inferred by homology rather than directly measured for this exact entry; however, the protein's function was experimentally validated in the 2024 Nat. Commun. paper (PubMed:38212296).",
    "The specific substrate name 'geissoschizine' is highly specialized (MIA pathway); a model arriving at D does so by elimination and family-level inference rather than by independently naming the substrate.",
    "The physiological direction annotation notes right-to-left (RHEA:11378), meaning the enzyme may operate in the reverse direction in vivo; the written reaction as given in option D matches the UniProt forward-direction annotation."
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
  "requested_accession": "P0DXJ1",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "benchmark_sequence_sha256": "be11b71809d30f0c5458041f2312ead6b14de7b52ebdd4b914b15674410bd94d",
  "benchmark_sequence_length": 365,
  "current_status": "retrieved",
  "current_sequence_comparison": "matched",
  "current_entry_audit": {
    "entryVersion": 4,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2025-06-18",
    "sequenceVersion": 1
  },
  "current_uniprot_release": "2026_03",
  "current_record_sha256": "6eda11173d33f799125da302047e13f2dbcebc81de87a50235cb3bf62d181ed5",
  "current_source_sequence_sha256": "be11b71809d30f0c5458041f2312ead6b14de7b52ebdd4b914b15674410bd94d",
  "current_source_sequence_length": 365,
  "historical_status": "retrieved",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "selected_historical_entry_version": 2,
  "selected_historical_version": {
    "accession": "P0DXJ1",
    "database": "Swiss-Prot",
    "entryVersion": 2,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "GS_RAUSE",
    "sequenceVersion": 1
  },
  "selected_historical_record_sha256": "7ba973e38966d3d8089bcd88dfc1f173357dd4d1bed310495b9a3912403794b7",
  "selected_historical_source_sequence_sha256": "be11b71809d30f0c5458041f2312ead6b14de7b52ebdd4b914b15674410bd94d",
  "selected_historical_source_sequence_length": 365,
  "latest_at_cutoff_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 2,
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXJ1.json)

```json
{
  "evidence_id": "C1",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXJ1.json",
  "source_sha256": "6eda11173d33f799125da302047e13f2dbcebc81de87a50235cb3bf62d181ed5",
  "retrieved_utc": "2026-11-02T04:29:29.884516+00:00",
  "json_pointer": "/primaryAccession",
  "excerpt": "\"P0DXJ1\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXJ1.json)

```json
{
  "evidence_id": "C2",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXJ1.json",
  "source_sha256": "6eda11173d33f799125da302047e13f2dbcebc81de87a50235cb3bf62d181ed5",
  "retrieved_utc": "2026-11-02T04:29:29.884516+00:00",
  "json_pointer": "/entryAudit",
  "excerpt": "{\"entryVersion\":4,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2025-06-18\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXJ1.json)

```json
{
  "evidence_id": "C3",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXJ1.json",
  "source_sha256": "6eda11173d33f799125da302047e13f2dbcebc81de87a50235cb3bf62d181ed5",
  "retrieved_utc": "2026-11-02T04:29:29.884516+00:00",
  "json_pointer": "/organism",
  "excerpt": "{\"commonName\":\"Serpentine wood\",\"lineage\":[\"Eukaryota\",\"Viridiplantae\",\"Streptophyta\",\"Embryophyta\",\"Tracheophyta\",\"Spermatophyta\",\"Magnoliopsida\",\"eudicotyledons\",\"Gunneridae\",\"Pentapetalae\",\"asterids\",\"lamiids\",\"Gentianales\",\"Apocynaceae\",\"Rauvolfioideae\",\"Vinceae\",\"Rauvolfiinae\",\"Rauvolfia\"],\"scientificName\":\"Rauvolfia serpentina\",\"synonyms\":[\"Ophioxylon serpentinum\"],\"taxonId\":4060}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXJ1.json)

```json
{
  "evidence_id": "C4",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXJ1.json",
  "source_sha256": "6eda11173d33f799125da302047e13f2dbcebc81de87a50235cb3bf62d181ed5",
  "retrieved_utc": "2026-11-02T04:29:29.884516+00:00",
  "json_pointer": "/proteinDescription",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"W8JWW7\",\"source\":\"UniProtKB\"}],\"value\":\"1.3.1.36\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"38212296\",\"source\":\"PubMed\"}],\"value\":\"Geissoschizine synthase\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"38212296\",\"source\":\"PubMed\"}],\"value\":\"RsGS\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXJ1.json)

```json
{
  "evidence_id": "C5",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXJ1.json",
  "source_sha256": "6eda11173d33f799125da302047e13f2dbcebc81de87a50235cb3bf62d181ed5",
  "retrieved_utc": "2026-11-02T04:29:29.884516+00:00",
  "json_pointer": "/comments/1",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"right-to-left\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"W8JWW7\",\"source\":\"UniProtKB\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:11378\"}}],\"reaction\":{\"ecNumber\":\"1.3.1.36\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"W8JWW7\",\"source\":\"UniProtKB\"}],\"name\":\"(19E)-geissoschizine + NADP(+) = 4,21-dehydrogeissoschizine + NADPH\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:11376\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:17037\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:17294\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57783\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:58349\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXJ1.json)

```json
{
  "evidence_id": "C6",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXJ1.json",
  "source_sha256": "6eda11173d33f799125da302047e13f2dbcebc81de87a50235cb3bf62d181ed5",
  "retrieved_utc": "2026-11-02T04:29:29.884516+00:00",
  "json_pointer": "/references/0",
  "excerpt": "{\"citation\":{\"authors\":[\"Guo J.\",\"Gao D.\",\"Lian J.\",\"Qu Y.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"38212296\"},{\"database\":\"DOI\",\"id\":\"10.1038/s41467-024-44797-z\"}],\"citationType\":\"journal article\",\"firstPage\":\"457\",\"id\":\"38212296\",\"journal\":\"Nat. Commun.\",\"lastPage\":\"457\",\"publicationDate\":\"2024\",\"title\":\"De novo biosynthesis of antiarrhythmic alkaloid ajmaline.\",\"volume\":\"15\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"WKU61919.1\",\"source\":\"EMBL\"}],\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [MRNA]\",\"FUNCTION\",\"BIOTECHNOLOGY\",\"TISSUE SPECIFICITY\",\"PATHWAY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXJ1?format=txt&versions=2)

```json
{
  "evidence_id": "H1",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/P0DXJ1?format=txt&versions=2",
  "source_sha256": "7ba973e38966d3d8089bcd88dfc1f173357dd4d1bed310495b9a3912403794b7",
  "retrieved_utc": "2026-11-02T04:29:32.265438+00:00",
  "source_locator": "lines 1-15",
  "excerpt": "ID   GS_RAUSE                Reviewed;         365 AA.\nAC   P0DXJ1;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   18-JUN-2025, sequence version 1.\nDT   28-JAN-2026, entry version 2.\nDE   RecName: Full=Geissoschizine synthase {ECO:0000303|PubMed:38212296};\nDE            Short=RsGS {ECO:0000303|PubMed:38212296};\nDE            EC=1.3.1.36 {ECO:0000250|UniProtKB:W8JWW7};\nGN   Name=GS {ECO:0000303|PubMed:38212296};\nOS   Rauvolfia serpentina (Serpentine wood) (Ophioxylon serpentinum).\nOC   Eukaryota; Viridiplantae; Streptophyta; Embryophyta; Tracheophyta;\nOC   Spermatophyta; Magnoliopsida; eudicotyledons; Gunneridae; Pentapetalae;\nOC   asterids; lamiids; Gentianales; Apocynaceae; Rauvolfioideae; Vinceae;\nOC   Rauvolfiinae; Rauvolfia.\nOX   NCBI_TaxID=4060;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 2,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXJ1?format=txt&versions=2)

```json
{
  "evidence_id": "H2",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/P0DXJ1?format=txt&versions=2",
  "source_sha256": "7ba973e38966d3d8089bcd88dfc1f173357dd4d1bed310495b9a3912403794b7",
  "retrieved_utc": "2026-11-02T04:29:32.265438+00:00",
  "source_locator": "lines 6-8",
  "excerpt": "DE   RecName: Full=Geissoschizine synthase {ECO:0000303|PubMed:38212296};\nDE            Short=RsGS {ECO:0000303|PubMed:38212296};\nDE            EC=1.3.1.36 {ECO:0000250|UniProtKB:W8JWW7};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 2,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXJ1?format=txt&versions=2)

```json
{
  "evidence_id": "H3",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/P0DXJ1?format=txt&versions=2",
  "source_sha256": "7ba973e38966d3d8089bcd88dfc1f173357dd4d1bed310495b9a3912403794b7",
  "retrieved_utc": "2026-11-02T04:29:32.265438+00:00",
  "source_locator": "lines 16-22",
  "excerpt": "RN   [1] {ECO:0000312|EMBL:WKU61919.1}\nRP   NUCLEOTIDE SEQUENCE [MRNA], FUNCTION, BIOTECHNOLOGY, TISSUE SPECIFICITY,\nRP   AND PATHWAY.\nRX   PubMed=38212296; DOI=10.1038/s41467-024-44797-z;\nRA   Guo J., Gao D., Lian J., Qu Y.;\nRT   \"De novo biosynthesis of antiarrhythmic alkaloid ajmaline.\";\nRL   Nat. Commun. 15:457-457(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 2,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXJ1?format=txt&versions=2)

```json
{
  "evidence_id": "H4",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/P0DXJ1?format=txt&versions=2",
  "source_sha256": "7ba973e38966d3d8089bcd88dfc1f173357dd4d1bed310495b9a3912403794b7",
  "retrieved_utc": "2026-11-02T04:29:32.265438+00:00",
  "source_locator": "lines 31-37",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=(19E)-geissoschizine + NADP(+) = 4,21-dehydrogeissoschizine +\nCC         NADPH; Xref=Rhea:RHEA:11376, ChEBI:CHEBI:17037, ChEBI:CHEBI:17294,\nCC         ChEBI:CHEBI:57783, ChEBI:CHEBI:58349; EC=1.3.1.36;\nCC         Evidence={ECO:0000250|UniProtKB:W8JWW7};\nCC       PhysiologicalDirection=right-to-left; Xref=Rhea:RHEA:11378;\nCC         Evidence={ECO:0000250|UniProtKB:W8JWW7};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 2,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 85. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
