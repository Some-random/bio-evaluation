# catalytic_activity_0142: before and after transfer clarification

[All 1,328 cases](../README.md) · [Method](../METHOD.md) · [Summary](../SUMMARY.md) · [Exact reviewer user message](../inputs/catalytic_activity_0142.txt)

**Task:** `catalytic_activity`  
**Author key, unchanged:** **B** — 17-O-acetylnorajmaline + NADP(+) = (2R)-1,2-dihydrovomilenine + NADPH + 2 H(+)

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
MAGKSPEEQHPVKAYGWAARDSSGILSPFKFSRRATGDHDVRVKILYAGVCHSDLQSARNEMGCFTYPLVPGFETVGIATEVGSKVTKMKVGDKVAVGIMVGSCGKCDDCVNDRECYCPEVITSYGRIDHDGTPTYGGFSNETVANEKFVFRFPEKLPMAAGAPLLNAGVSVYSPMRFYGLDKPGMHLGVVGLGGLGHLAVKFAKAFGVKVTVISTSSIKKGEAINDLGADAFLVSTDAKQMQAGSGTLDGILDTVPVVHPIEPLLGLLKNHTKLVLVGATMGSFELPILPLGVGRKSVASTVGGSTTEAQEMLDFAAEHNITANVEIIPMDYINTAMERIEKNDVRYRFVIDVGNTLTPPES

[Multiple Choices]
A. benzoyl-CoA + L-lysyl-[protein] = N(6)-benzoyl-L-lysyl-[protein] + CoA + H(+)
B. 17-O-acetylnorajmaline + NADP(+) = (2R)-1,2-dihydrovomilenine + NADPH + 2 H(+)
C. (2E,6E)-farnesyl diphosphate = (S,S)-drim-8-en-11-yl diphosphate
D. UDP-2-acetamido-2-deoxy-alpha-D-glucuronate + H(+) = UDP-N-acetyl-alpha-D-xylosamine + CO2
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

> The exact sequence matches a UniProt entry annotating choice B as a catalytic reaction, but that assignment is transferred by similarity (ECO:0000250), not direct experimental evidence for this sequence. The same entry reports experimental evidence for a different reaction, which does not contradict B.

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence could plausibly indicate an oxidoreductase, making the NADP-linked choice B more compatible than the transferase, terpene-cyclization, or sugar-decarboxylation choices. That broad class inference does not establish the specific substrates and products in B.


**Missing item-specific fact**

> The protein-specific catalytic annotation linking this sequence to the 17-O-acetylnorajmaline reaction.


**Reason**

> Choosing the exact transformation requires protein-specific functional information absent from the input; recognizing the sequence or recalling its database annotation would be lookup or memorization, not reasoning from the supplied evidence.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Only choice B is supported by the supplied reviewer evidence as an annotation for the matching sequence; the separately reported experimental reaction is not among the options.


### Important caveats

- The choice-B annotation is transferred from a related UniProt entry, rather than directly experimentally established for this sequence in the cited annotation.
- The matching protein has experimental evidence for a distinct catalytic reaction, which does not by itself exclude the transferred choice-B activity.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence could plausibly indicate an oxidoreductase, making the NADP-linked choice B more compatible than the transferase, terpene-cyclization, or sugar-decarboxylation choices. That broad class inference does not establish the specific substrates and products in B.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific catalytic annotation linking this sequence to the 17-O-acetylnorajmaline reaction.",
    "reason": "Choosing the exact transformation requires protein-specific functional information absent from the input; recognizing the sequence or recalling its database annotation would be lookup or memorization, not reasoning from the supplied evidence."
  },
  "case_id": "catalytic_activity_0142",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry annotating choice B as a catalytic reaction, but that assignment is transferred by similarity (ECO:0000250), not direct experimental evidence for this sequence. The same entry reports experimental evidence for a different reaction, which does not contradict B."
  },
  "important_caveats": [
    "The choice-B annotation is transferred from a related UniProt entry, rather than directly experimentally established for this sequence in the cited annotation.",
    "The matching protein has experimental evidence for a distinct catalytic reaction, which does not by itself exclude the transferred choice-B activity."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only choice B is supported by the supplied reviewer evidence as an annotation for the matching sequence; the separately reported experimental reaction is not among the options."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0142",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry annotating choice B as a catalytic reaction, but that assignment is transferred by similarity (ECO:0000250), not direct experimental evidence for this sequence. The same entry reports experimental evidence for a different reaction, which does not contradict B.",
    "evidence_ids": ["C1", "C5", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence could plausibly indicate an oxidoreductase, making the NADP-linked choice B more compatible than the transferase, terpene-cyclization, or sugar-decarboxylation choices. That broad class inference does not establish the specific substrates and products in B.",
    "missing_item_specific_fact": "The protein-specific catalytic annotation linking this sequence to the 17-O-acetylnorajmaline reaction.",
    "reason": "Choosing the exact transformation requires protein-specific functional information absent from the input; recognizing the sequence or recalling its database annotation would be lookup or memorization, not reasoning from the supplied evidence."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only choice B is supported by the supplied reviewer evidence as an annotation for the matching sequence; the separately reported experimental reaction is not among the options."
  },
  "important_caveats": [
    "The choice-B annotation is transferred from a related UniProt entry, rather than directly experimentally established for this sequence in the cited annotation.",
    "The matching protein has experimental evidence for a distinct catalytic reaction, which does not by itself exclude the transferred choice-B activity."
  ]
}
```

</details>

## Before: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A0A0U4BHM2 (sequence matched exactly) lists the reaction '17-O-acetylnorajmaline + NADP(+) = (2R)-1,2-dihydrovomilenine + NADPH + 2 H(+)' (EC 1.3.1.73) as a catalytic activity (C5/H4). The recommended protein name is '1,2-Dihydrovomilenine reductase' with EC 1.3.1.73. However, the evidence code for this specific reaction is ECO:0000250 (inferred by similarity from A0A0U3S9Q3), not direct experimental assay. The experimentally verified activity (ECO:0000269, C6/H5) is a different reaction: (20S)-19,20-dihydrovomilenine + NADP(+) = vomilenine + NADPH + H(+). The expected answer matches the UniProt annotation but rests on similarity-based inference rather than direct experimental confirmation for this particular substrate.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains identifiable Rossmann-fold nucleotide-binding motifs: 'GATMGSFELPILPLGVGRKS' (GxGxxG variant) and 'GGLGHLAVKFAKAFGVKVTVISTSSIKKGEAINDLGA' (GGLGH motif), characteristic of NAD(P)-dependent oxidoreductases. Among the four choices, only B describes an NADP+-dependent oxidation-reduction reaction (EC 1.3.1.73). Choice A is an acyltransferase (no NADP+), C is a cyclase (no cofactor), and D is a decarboxylase (no NADP+). Identifying the protein as an oxidoreductase from these structural motifs eliminates A, C, and D, leaving B.


**Missing item-specific fact**

> The specific substrate identity (17-O-acetylnorajmaline) cannot be determined from sequence alone; however, the elimination of non-oxidoreductase choices via cofactor/enzyme-class reasoning is sufficient to select B from the given options.


**Reason**

> The sequence provides sufficient structural information (Rossmann fold motifs, overall ~363 aa oxidoreductase architecture) to identify the enzyme class as an NAD(P)-dependent reductase. This uniquely matches choice B among the four options, which differ in enzyme class (transferase, oxidoreductase, cyclase, decarboxylase). The reasoning does not require memorizing this specific protein's database entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four choices represent distinct enzyme classes (acyltransferase, oxidoreductase, sesquiterpene cyclase, decarboxylase), making them mutually exclusive. Only B is consistent with an NAD(P)-dependent oxidoreductase, which the sequence motifs support.


### Important caveats

- The EC 1.3.1.73 assignment for the 17-O-acetylnorajmaline reaction is based on similarity inference (ECO:0000250), not direct experimental evidence for this protein.
- The experimentally characterized activity (ECO:0000269, PubMed:26715562) is for the dihydrovomilenine→vomilenine reduction, a different reaction not offered as a choice.
- The protein is annotated as a 'CAD-like reductase' (cinnamyl alcohol dehydrogenase-like), which is a broad family; substrate specificity within this family cannot be predicted from sequence motifs alone.
- The physiological direction of the B reaction is right-to-left (reducing 1,2-dihydrovomilenine), though the equation is written left-to-right in the answer choice, consistent with UniProt's convention.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains identifiable Rossmann-fold nucleotide-binding motifs: 'GATMGSFELPILPLGVGRKS' (GxGxxG variant) and 'GGLGHLAVKFAKAFGVKVTVISTSSIKKGEAINDLGA' (GGLGH motif), characteristic of NAD(P)-dependent oxidoreductases. Among the four choices, only B describes an NADP+-dependent oxidation-reduction reaction (EC 1.3.1.73). Choice A is an acyltransferase (no NADP+), C is a cyclase (no cofactor), and D is a decarboxylase (no NADP+). Identifying the protein as an oxidoreductase from these structural motifs eliminates A, C, and D, leaving B.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The specific substrate identity (17-O-acetylnorajmaline) cannot be determined from sequence alone; however, the elimination of non-oxidoreductase choices via cofactor/enzyme-class reasoning is sufficient to select B from the given options.",
    "reason": "The sequence provides sufficient structural information (Rossmann fold motifs, overall ~363 aa oxidoreductase architecture) to identify the enzyme class as an NAD(P)-dependent reductase. This uniquely matches choice B among the four options, which differ in enzyme class (transferase, oxidoreductase, cyclase, decarboxylase). The reasoning does not require memorizing this specific protein's database entry."
  },
  "case_id": "catalytic_activity_0142",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H1",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry A0A0U4BHM2 (sequence matched exactly) lists the reaction '17-O-acetylnorajmaline + NADP(+) = (2R)-1,2-dihydrovomilenine + NADPH + 2 H(+)' (EC 1.3.1.73) as a catalytic activity (C5/H4). The recommended protein name is '1,2-Dihydrovomilenine reductase' with EC 1.3.1.73. However, the evidence code for this specific reaction is ECO:0000250 (inferred by similarity from A0A0U3S9Q3), not direct experimental assay. The experimentally verified activity (ECO:0000269, C6/H5) is a different reaction: (20S)-19,20-dihydrovomilenine + NADP(+) = vomilenine + NADPH + H(+). The expected answer matches the UniProt annotation but rests on similarity-based inference rather than direct experimental confirmation for this particular substrate."
  },
  "important_caveats": [
    "The EC 1.3.1.73 assignment for the 17-O-acetylnorajmaline reaction is based on similarity inference (ECO:0000250), not direct experimental evidence for this protein.",
    "The experimentally characterized activity (ECO:0000269, PubMed:26715562) is for the dihydrovomilenine→vomilenine reduction, a different reaction not offered as a choice.",
    "The protein is annotated as a 'CAD-like reductase' (cinnamyl alcohol dehydrogenase-like), which is a broad family; substrate specificity within this family cannot be predicted from sequence motifs alone.",
    "The physiological direction of the B reaction is right-to-left (reducing 1,2-dihydrovomilenine), though the equation is written left-to-right in the answer choice, consistent with UniProt's convention."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices represent distinct enzyme classes (acyltransferase, oxidoreductase, sesquiterpene cyclase, decarboxylase), making them mutually exclusive. Only B is consistent with an NAD(P)-dependent oxidoreductase, which the sequence motifs support."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0142",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A0A0U4BHM2 (sequence matched exactly) lists the reaction '17-O-acetylnorajmaline + NADP(+) = (2R)-1,2-dihydrovomilenine + NADPH + 2 H(+)' (EC 1.3.1.73) as a catalytic activity (C5/H4). The recommended protein name is '1,2-Dihydrovomilenine reductase' with EC 1.3.1.73. However, the evidence code for this specific reaction is ECO:0000250 (inferred by similarity from A0A0U3S9Q3), not direct experimental assay. The experimentally verified activity (ECO:0000269, C6/H5) is a different reaction: (20S)-19,20-dihydrovomilenine + NADP(+) = vomilenine + NADPH + H(+). The expected answer matches the UniProt annotation but rests on similarity-based inference rather than direct experimental confirmation for this particular substrate.",
    "evidence_ids": ["C4", "C5", "C6", "H1", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains identifiable Rossmann-fold nucleotide-binding motifs: 'GATMGSFELPILPLGVGRKS' (GxGxxG variant) and 'GGLGHLAVKFAKAFGVKVTVISTSSIKKGEAINDLGA' (GGLGH motif), characteristic of NAD(P)-dependent oxidoreductases. Among the four choices, only B describes an NADP+-dependent oxidation-reduction reaction (EC 1.3.1.73). Choice A is an acyltransferase (no NADP+), C is a cyclase (no cofactor), and D is a decarboxylase (no NADP+). Identifying the protein as an oxidoreductase from these structural motifs eliminates A, C, and D, leaving B.",
    "missing_item_specific_fact": "The specific substrate identity (17-O-acetylnorajmaline) cannot be determined from sequence alone; however, the elimination of non-oxidoreductase choices via cofactor/enzyme-class reasoning is sufficient to select B from the given options.",
    "reason": "The sequence provides sufficient structural information (Rossmann fold motifs, overall ~363 aa oxidoreductase architecture) to identify the enzyme class as an NAD(P)-dependent reductase. This uniquely matches choice B among the four options, which differ in enzyme class (transferase, oxidoreductase, cyclase, decarboxylase). The reasoning does not require memorizing this specific protein's database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices represent distinct enzyme classes (acyltransferase, oxidoreductase, sesquiterpene cyclase, decarboxylase), making them mutually exclusive. Only B is consistent with an NAD(P)-dependent oxidoreductase, which the sequence motifs support."
  },
  "important_caveats": [
    "The EC 1.3.1.73 assignment for the 17-O-acetylnorajmaline reaction is based on similarity inference (ECO:0000250), not direct experimental evidence for this protein.",
    "The experimentally characterized activity (ECO:0000269, PubMed:26715562) is for the dihydrovomilenine→vomilenine reduction, a different reaction not offered as a choice.",
    "The protein is annotated as a 'CAD-like reductase' (cinnamyl alcohol dehydrogenase-like), which is a broad family; substrate specificity within this family cannot be predicted from sequence motifs alone.",
    "The physiological direction of the B reaction is right-to-left (reducing 1,2-dihydrovomilenine), though the equation is written left-to-right in the answer choice, consistent with UniProt's convention."
  ]
}
```

</details>

## After: GPT-6 Luna

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence-matched database entry annotates reaction B, but the evidence is transferred by similarity (ECO:0000250), not direct experimental confirmation for this protein. The record reports experimental evidence for a different NADP-dependent reaction, which does not contradict B but means the support for B is computational rather than direct.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has features consistent with a plant CAD-like, NAD(P)-dependent reductase, including a cysteine-rich region and glycine-rich regions compatible with metal/cofactor binding. Among these choices, B is the NADP-dependent redox reaction; A is an acyl transfer, C a terpene cyclization, and D a nucleotide-sugar decarboxylation. This family-level and reaction-class inference meaningfully favors B, though it does not independently establish its exact substrate specificity.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Transferable knowledge of reductase families and cofactor-dependent reaction classes distinguishes B from the offered alternatives without needing the exact protein's recorded annotation. The inference is probabilistic and does not amount to experimental proof of B.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The listed alternatives describe clearly different reaction classes; no second option is comparably supported by the sequence-level reductase inference.


### Important caveats

- The specific reaction annotation for B is similarity-based for this protein; the supplied evidence does not show direct experimental validation of that reaction.
- The database also reports experimental evidence for a different NADP-dependent reaction, so the sequence-level inference supports the reaction class more strongly than the precise substrate and product.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has features consistent with a plant CAD-like, NAD(P)-dependent reductase, including a cysteine-rich region and glycine-rich regions compatible with metal/cofactor binding. Among these choices, B is the NADP-dependent redox reaction; A is an acyl transfer, C a terpene cyclization, and D a nucleotide-sugar decarboxylation. This family-level and reaction-class inference meaningfully favors B, though it does not independently establish its exact substrate specificity.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Transferable knowledge of reductase families and cofactor-dependent reaction classes distinguishes B from the offered alternatives without needing the exact protein's recorded annotation. The inference is probabilistic and does not amount to experimental proof of B."
  },
  "case_id": "catalytic_activity_0142",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched database entry annotates reaction B, but the evidence is transferred by similarity (ECO:0000250), not direct experimental confirmation for this protein. The record reports experimental evidence for a different NADP-dependent reaction, which does not contradict B but means the support for B is computational rather than direct."
  },
  "important_caveats": [
    "The specific reaction annotation for B is similarity-based for this protein; the supplied evidence does not show direct experimental validation of that reaction.",
    "The database also reports experimental evidence for a different NADP-dependent reaction, so the sequence-level inference supports the reaction class more strongly than the precise substrate and product."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The listed alternatives describe clearly different reaction classes; no second option is comparably supported by the sequence-level reductase inference."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0142",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched database entry annotates reaction B, but the evidence is transferred by similarity (ECO:0000250), not direct experimental confirmation for this protein. The record reports experimental evidence for a different NADP-dependent reaction, which does not contradict B but means the support for B is computational rather than direct.",
    "evidence_ids": ["C5", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has features consistent with a plant CAD-like, NAD(P)-dependent reductase, including a cysteine-rich region and glycine-rich regions compatible with metal/cofactor binding. Among these choices, B is the NADP-dependent redox reaction; A is an acyl transfer, C a terpene cyclization, and D a nucleotide-sugar decarboxylation. This family-level and reaction-class inference meaningfully favors B, though it does not independently establish its exact substrate specificity.",
    "missing_item_specific_fact": "",
    "reason": "Transferable knowledge of reductase families and cofactor-dependent reaction classes distinguishes B from the offered alternatives without needing the exact protein's recorded annotation. The inference is probabilistic and does not amount to experimental proof of B."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The listed alternatives describe clearly different reaction classes; no second option is comparably supported by the sequence-level reductase inference."
  },
  "important_caveats": [
    "The specific reaction annotation for B is similarity-based for this protein; the supplied evidence does not show direct experimental validation of that reaction.",
    "The database also reports experimental evidence for a different NADP-dependent reaction, so the sequence-level inference supports the reaction class more strongly than the precise substrate and product."
  ]
}
```

</details>

## After: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A0A0U4BHM2 (sequence matched exactly) lists the primary catalytic activity as EC 1.3.1.73: '17-O-acetylnorajmaline + NADP(+) = (2R)-1,2-dihydrovomilenine + NADPH + 2 H(+)', which is identical to option B. The annotation carries ECO:0000250 (similarity to A0A0U3S9Q3) for this reaction, while the protein's overall function in the MIA pathway is experimentally confirmed (ECO:0000269, PubMed 26715562). The physiological direction is right-to-left (reduction), but the oxidation-direction reaction as written remains the annotated catalytic activity.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a clear NAD(P)-binding Rossmann fold motif ('GATMGSFELPILPLGVGRKSVASTVGG' with the canonical GxxGxxG pattern) and overall architecture consistent with the SDR/CAD-like (short-chain dehydrogenase/reductase) superfamily. This immediately identifies the enzyme as a dehydrogenase/reductase requiring NAD(P) as a cofactor. Among the four options, only B involves NADP(+) as a cofactor in a redox reaction. Option A is a lysine acyltransferase (no NADP), option C is a terpene cyclase/synthase (no NADP, different fold with DDXXD motifs), and option D is a decarboxylase (no NADP). Recognizing the NAD(P)-binding motif and SDR/CAD-like family membership is standard transferable knowledge that eliminates A, C, and D and uniquely selects B.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can identify the Rossmann-fold NAD(P)-binding motif and SDR/CAD-like family architecture from the sequence alone, then eliminate the three non-redox options (transferase, terpene cyclase, decarboxylase) because they do not involve NADP(+) cofactor chemistry. This family-level inference meaningfully distinguishes B from the offered alternatives without requiring the specific substrate names.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Only option B involves NADP(+) as a cofactor, which is the sole reaction type consistent with the NAD(P)-binding motifs and SDR/CAD-like fold evident in the sequence. The other three options describe fundamentally different enzyme classes (transferase, cyclase, decarboxylase) that are incompatible with the observed cofactor-binding architecture.


### Important caveats

- The primary EC 1.3.1.73 annotation is by similarity (ECO:0000250) to A0A0U3S9Q3, not direct experimental measurement on this exact protein, though the protein's role in the MIA pathway is experimentally supported (ECO:0000269).
- The physiological direction of the B reaction is right-to-left (the enzyme functions primarily as a reductase in vivo), but the oxidation-direction reaction as written is still the standard catalytic activity annotation.
- The protein also has a second annotated catalytic activity (EC 1.5.1.-: (20S)-19,20-dihydrovomilenine + NADP(+) = vomilenine + NADPH + H(+)), but this is not among the answer choices and does not create ambiguity.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a clear NAD(P)-binding Rossmann fold motif ('GATMGSFELPILPLGVGRKSVASTVGG' with the canonical GxxGxxG pattern) and overall architecture consistent with the SDR/CAD-like (short-chain dehydrogenase/reductase) superfamily. This immediately identifies the enzyme as a dehydrogenase/reductase requiring NAD(P) as a cofactor. Among the four options, only B involves NADP(+) as a cofactor in a redox reaction. Option A is a lysine acyltransferase (no NADP), option C is a terpene cyclase/synthase (no NADP, different fold with DDXXD motifs), and option D is a decarboxylase (no NADP). Recognizing the NAD(P)-binding motif and SDR/CAD-like family membership is standard transferable knowledge that eliminates A, C, and D and uniquely selects B.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can identify the Rossmann-fold NAD(P)-binding motif and SDR/CAD-like family architecture from the sequence alone, then eliminate the three non-redox options (transferase, terpene cyclase, decarboxylase) because they do not involve NADP(+) cofactor chemistry. This family-level inference meaningfully distinguishes B from the offered alternatives without requiring the specific substrate names."
  },
  "case_id": "catalytic_activity_0142",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry A0A0U4BHM2 (sequence matched exactly) lists the primary catalytic activity as EC 1.3.1.73: '17-O-acetylnorajmaline + NADP(+) = (2R)-1,2-dihydrovomilenine + NADPH + 2 H(+)', which is identical to option B. The annotation carries ECO:0000250 (similarity to A0A0U3S9Q3) for this reaction, while the protein's overall function in the MIA pathway is experimentally confirmed (ECO:0000269, PubMed 26715562). The physiological direction is right-to-left (reduction), but the oxidation-direction reaction as written remains the annotated catalytic activity."
  },
  "important_caveats": [
    "The primary EC 1.3.1.73 annotation is by similarity (ECO:0000250) to A0A0U3S9Q3, not direct experimental measurement on this exact protein, though the protein's role in the MIA pathway is experimentally supported (ECO:0000269).",
    "The physiological direction of the B reaction is right-to-left (the enzyme functions primarily as a reductase in vivo), but the oxidation-direction reaction as written is still the standard catalytic activity annotation.",
    "The protein also has a second annotated catalytic activity (EC 1.5.1.-: (20S)-19,20-dihydrovomilenine + NADP(+) = vomilenine + NADPH + H(+)), but this is not among the answer choices and does not create ambiguity."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only option B involves NADP(+) as a cofactor, which is the sole reaction type consistent with the NAD(P)-binding motifs and SDR/CAD-like fold evident in the sequence. The other three options describe fundamentally different enzyme classes (transferase, cyclase, decarboxylase) that are incompatible with the observed cofactor-binding architecture."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0142",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A0A0U4BHM2 (sequence matched exactly) lists the primary catalytic activity as EC 1.3.1.73: '17-O-acetylnorajmaline + NADP(+) = (2R)-1,2-dihydrovomilenine + NADPH + 2 H(+)', which is identical to option B. The annotation carries ECO:0000250 (similarity to A0A0U3S9Q3) for this reaction, while the protein's overall function in the MIA pathway is experimentally confirmed (ECO:0000269, PubMed 26715562). The physiological direction is right-to-left (reduction), but the oxidation-direction reaction as written remains the annotated catalytic activity.",
    "evidence_ids": ["C4", "C5", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a clear NAD(P)-binding Rossmann fold motif ('GATMGSFELPILPLGVGRKSVASTVGG' with the canonical GxxGxxG pattern) and overall architecture consistent with the SDR/CAD-like (short-chain dehydrogenase/reductase) superfamily. This immediately identifies the enzyme as a dehydrogenase/reductase requiring NAD(P) as a cofactor. Among the four options, only B involves NADP(+) as a cofactor in a redox reaction. Option A is a lysine acyltransferase (no NADP), option C is a terpene cyclase/synthase (no NADP, different fold with DDXXD motifs), and option D is a decarboxylase (no NADP). Recognizing the NAD(P)-binding motif and SDR/CAD-like family membership is standard transferable knowledge that eliminates A, C, and D and uniquely selects B.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can identify the Rossmann-fold NAD(P)-binding motif and SDR/CAD-like family architecture from the sequence alone, then eliminate the three non-redox options (transferase, terpene cyclase, decarboxylase) because they do not involve NADP(+) cofactor chemistry. This family-level inference meaningfully distinguishes B from the offered alternatives without requiring the specific substrate names."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only option B involves NADP(+) as a cofactor, which is the sole reaction type consistent with the NAD(P)-binding motifs and SDR/CAD-like fold evident in the sequence. The other three options describe fundamentally different enzyme classes (transferase, cyclase, decarboxylase) that are incompatible with the observed cofactor-binding architecture."
  },
  "important_caveats": [
    "The primary EC 1.3.1.73 annotation is by similarity (ECO:0000250) to A0A0U3S9Q3, not direct experimental measurement on this exact protein, though the protein's role in the MIA pathway is experimentally supported (ECO:0000269).",
    "The physiological direction of the B reaction is right-to-left (the enzyme functions primarily as a reductase in vivo), but the oxidation-direction reaction as written is still the standard catalytic activity annotation.",
    "The protein also has a second annotated catalytic activity (EC 1.5.1.-: (20S)-19,20-dihydrovomilenine + NADP(+) = vomilenine + NADPH + H(+)), but this is not among the answer choices and does not create ambiguity."
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
  "requested_accession": "A0A0U4BHM2",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "benchmark_sequence_sha256": "351c34d2095e544533593a3430ee8d4f870ed8068eab99c7a6c309e20ddfb657",
  "benchmark_sequence_length": 363,
  "current_status": "retrieved",
  "current_sequence_comparison": "matched",
  "current_entry_audit": {
    "entryVersion": 32,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2016-03-16",
    "sequenceVersion": 1
  },
  "current_uniprot_release": "2026_03",
  "current_record_sha256": "c26b85d02403fbdfc042529d2261359bc369b05deb9442cd6e55153bd5141c6f",
  "current_source_sequence_sha256": "351c34d2095e544533593a3430ee8d4f870ed8068eab99c7a6c309e20ddfb657",
  "current_source_sequence_length": 363,
  "historical_status": "retrieved",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "selected_historical_entry_version": 30,
  "selected_historical_version": {
    "accession": "A0A0U4BHM2",
    "database": "Swiss-Prot",
    "entryVersion": 30,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "DHVOR_RAUTE",
    "sequenceVersion": 1
  },
  "selected_historical_record_sha256": "f1ca3ed3dfca81ae192adab6c5b2e6c70586c275e9a49b6b2913846785e88634",
  "selected_historical_source_sequence_sha256": "351c34d2095e544533593a3430ee8d4f870ed8068eab99c7a6c309e20ddfb657",
  "selected_historical_source_sequence_length": 363,
  "latest_at_cutoff_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 30,
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0U4BHM2.json)

```json
{
  "evidence_id": "C1",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0U4BHM2.json",
  "source_sha256": "c26b85d02403fbdfc042529d2261359bc369b05deb9442cd6e55153bd5141c6f",
  "retrieved_utc": "2026-11-02T04:24:23.340033+00:00",
  "json_pointer": "/primaryAccession",
  "excerpt": "\"A0A0U4BHM2\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0U4BHM2.json)

```json
{
  "evidence_id": "C2",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0U4BHM2.json",
  "source_sha256": "c26b85d02403fbdfc042529d2261359bc369b05deb9442cd6e55153bd5141c6f",
  "retrieved_utc": "2026-11-02T04:24:23.340033+00:00",
  "json_pointer": "/entryAudit",
  "excerpt": "{\"entryVersion\":32,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2016-03-16\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0U4BHM2.json)

```json
{
  "evidence_id": "C3",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0U4BHM2.json",
  "source_sha256": "c26b85d02403fbdfc042529d2261359bc369b05deb9442cd6e55153bd5141c6f",
  "retrieved_utc": "2026-11-02T04:24:23.340033+00:00",
  "json_pointer": "/organism",
  "excerpt": "{\"commonName\":\"Be still tree\",\"lineage\":[\"Eukaryota\",\"Viridiplantae\",\"Streptophyta\",\"Embryophyta\",\"Tracheophyta\",\"Spermatophyta\",\"Magnoliopsida\",\"eudicotyledons\",\"Gunneridae\",\"Pentapetalae\",\"asterids\",\"lamiids\",\"Gentianales\",\"Apocynaceae\",\"Rauvolfioideae\",\"Vinceae\",\"Rauvolfiinae\",\"Rauvolfia\"],\"scientificName\":\"Rauvolfia tetraphylla\",\"taxonId\":545371}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0U4BHM2.json)

```json
{
  "evidence_id": "C4",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0U4BHM2.json",
  "source_sha256": "c26b85d02403fbdfc042529d2261359bc369b05deb9442cd6e55153bd5141c6f",
  "retrieved_utc": "2026-11-02T04:24:23.340033+00:00",
  "json_pointer": "/proteinDescription",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"26715562\",\"source\":\"PubMed\"}],\"value\":\"Protein RR2\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"26715562\",\"source\":\"PubMed\"}],\"value\":\"RtRR2\"}]},{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"26715562\",\"source\":\"PubMed\"}],\"value\":\"1.5.1.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"26715562\",\"source\":\"PubMed\"}],\"value\":\"Vomilenine reductase 2\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"26715562\",\"source\":\"PubMed\"}],\"value\":\"RtVR2\"}]}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"A0A0U3S9Q3\",\"source\":\"UniProtKB\"}],\"value\":\"1.3.1.73\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"26715562\",\"source\":\"PubMed\"}],\"value\":\"1,2-Dihydrovomilenine reductase\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"26715562\",\"source\":\"PubMed\"}],\"value\":\"RtDHVR\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0U4BHM2.json)

```json
{
  "evidence_id": "C5",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0U4BHM2.json",
  "source_sha256": "c26b85d02403fbdfc042529d2261359bc369b05deb9442cd6e55153bd5141c6f",
  "retrieved_utc": "2026-11-02T04:24:23.340033+00:00",
  "json_pointer": "/comments/1",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"right-to-left\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"A0A0U3S9Q3\",\"source\":\"UniProtKB\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:12322\"}}],\"reaction\":{\"ecNumber\":\"1.3.1.73\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"A0A0U3S9Q3\",\"source\":\"UniProtKB\"}],\"name\":\"17-O-acetylnorajmaline + NADP(+) = (2R)-1,2-dihydrovomilenine + NADPH + 2 H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:12320\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:17372\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57783\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:58349\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:77725\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0U4BHM2.json)

```json
{
  "evidence_id": "C6",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0U4BHM2.json",
  "source_sha256": "c26b85d02403fbdfc042529d2261359bc369b05deb9442cd6e55153bd5141c6f",
  "retrieved_utc": "2026-11-02T04:24:23.340033+00:00",
  "json_pointer": "/comments/2",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"right-to-left\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"26715562\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:79637\"}}],\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"26715562\",\"source\":\"PubMed\"}],\"name\":\"(20S)-19,20-dihydrovomilenine + NADP(+) = vomilenine + NADPH + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:79635\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:16408\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57783\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:58349\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:230482\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0U4BHM2.json)

```json
{
  "evidence_id": "C7",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0U4BHM2.json",
  "source_sha256": "c26b85d02403fbdfc042529d2261359bc369b05deb9442cd6e55153bd5141c6f",
  "retrieved_utc": "2026-11-02T04:24:23.340033+00:00",
  "json_pointer": "/references/0",
  "excerpt": "{\"citation\":{\"authors\":[\"Geissler M.\",\"Burghard M.\",\"Volk J.\",\"Staniek A.\",\"Warzecha H.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"26715562\"},{\"database\":\"DOI\",\"id\":\"10.1007/s00425-015-2446-6\"}],\"citationType\":\"journal article\",\"firstPage\":\"813\",\"id\":\"26715562\",\"journal\":\"Planta\",\"lastPage\":\"824\",\"publicationDate\":\"2016\",\"title\":\"A novel cinnamyl alcohol dehydrogenase (CAD)-like reductase contributes to the structural diversity of monoterpenoid indole alkaloids in Rauvolfia.\",\"volume\":\"243\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"ALW82982.1\",\"source\":\"EMBL\"}],\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [MRNA]\",\"PROTEIN SEQUENCE OF 14-26 AND 149-156\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"PATHWAY\",\"BIOPHYSICOCHEMICAL PROPERTIES\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0U4BHM2?format=txt&versions=30)

```json
{
  "evidence_id": "H1",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A0U4BHM2?format=txt&versions=30",
  "source_sha256": "f1ca3ed3dfca81ae192adab6c5b2e6c70586c275e9a49b6b2913846785e88634",
  "retrieved_utc": "2026-11-02T04:24:25.840272+00:00",
  "source_locator": "lines 1-22",
  "excerpt": "ID   DHVOR_RAUTE             Reviewed;         363 AA.\nAC   A0A0U4BHM2;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   16-MAR-2016, sequence version 1.\nDT   28-JAN-2026, entry version 30.\nDE   RecName: Full=1,2-Dihydrovomilenine reductase {ECO:0000303|PubMed:26715562};\nDE            Short=RtDHVR {ECO:0000303|PubMed:26715562};\nDE            EC=1.3.1.73 {ECO:0000250|UniProtKB:A0A0U3S9Q3};\nDE   AltName: Full=Protein RR2 {ECO:0000303|PubMed:26715562};\nDE            Short=RtRR2 {ECO:0000303|PubMed:26715562};\nDE   AltName: Full=Vomilenine reductase 2 {ECO:0000303|PubMed:26715562};\nDE            Short=RtVR2 {ECO:0000303|PubMed:26715562};\nDE            EC=1.5.1.- {ECO:0000269|PubMed:26715562};\nGN   Name=DHVR {ECO:0000303|PubMed:26715562};\nGN   Synonyms=RR2 {ECO:0000303|PubMed:26715562},\nGN   VR2 {ECO:0000303|PubMed:26715562};\nOS   Rauvolfia tetraphylla (Be still tree).\nOC   Eukaryota; Viridiplantae; Streptophyta; Embryophyta; Tracheophyta;\nOC   Spermatophyta; Magnoliopsida; eudicotyledons; Gunneridae; Pentapetalae;\nOC   asterids; lamiids; Gentianales; Apocynaceae; Rauvolfioideae; Vinceae;\nOC   Rauvolfiinae; Rauvolfia.\nOX   NCBI_TaxID=545371;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 30,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0U4BHM2?format=txt&versions=30)

```json
{
  "evidence_id": "H2",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A0U4BHM2?format=txt&versions=30",
  "source_sha256": "f1ca3ed3dfca81ae192adab6c5b2e6c70586c275e9a49b6b2913846785e88634",
  "retrieved_utc": "2026-11-02T04:24:25.840272+00:00",
  "source_locator": "lines 6-13",
  "excerpt": "DE   RecName: Full=1,2-Dihydrovomilenine reductase {ECO:0000303|PubMed:26715562};\nDE            Short=RtDHVR {ECO:0000303|PubMed:26715562};\nDE            EC=1.3.1.73 {ECO:0000250|UniProtKB:A0A0U3S9Q3};\nDE   AltName: Full=Protein RR2 {ECO:0000303|PubMed:26715562};\nDE            Short=RtRR2 {ECO:0000303|PubMed:26715562};\nDE   AltName: Full=Vomilenine reductase 2 {ECO:0000303|PubMed:26715562};\nDE            Short=RtVR2 {ECO:0000303|PubMed:26715562};\nDE            EC=1.5.1.- {ECO:0000269|PubMed:26715562};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 30,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0U4BHM2?format=txt&versions=30)

```json
{
  "evidence_id": "H3",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A0U4BHM2?format=txt&versions=30",
  "source_sha256": "f1ca3ed3dfca81ae192adab6c5b2e6c70586c275e9a49b6b2913846785e88634",
  "retrieved_utc": "2026-11-02T04:24:25.840272+00:00",
  "source_locator": "lines 23-30",
  "excerpt": "RN   [1] {ECO:0000312|EMBL:ALW82982.1}\nRP   NUCLEOTIDE SEQUENCE [MRNA], PROTEIN SEQUENCE OF 14-26 AND 149-156,\nRP   FUNCTION, CATALYTIC ACTIVITY, PATHWAY, AND BIOPHYSICOCHEMICAL PROPERTIES.\nRX   PubMed=26715562; DOI=10.1007/s00425-015-2446-6;\nRA   Geissler M., Burghard M., Volk J., Staniek A., Warzecha H.;\nRT   \"A novel cinnamyl alcohol dehydrogenase (CAD)-like reductase contributes to\nRT   the structural diversity of monoterpenoid indole alkaloids in Rauvolfia.\";\nRL   Planta 243:813-824(2016).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 30,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0U4BHM2?format=txt&versions=30)

```json
{
  "evidence_id": "H4",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A0U4BHM2?format=txt&versions=30",
  "source_sha256": "f1ca3ed3dfca81ae192adab6c5b2e6c70586c275e9a49b6b2913846785e88634",
  "retrieved_utc": "2026-11-02T04:24:25.840272+00:00",
  "source_locator": "lines 39-46",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=17-O-acetylnorajmaline + NADP(+) = (2R)-1,2-dihydrovomilenine\nCC         + NADPH + 2 H(+); Xref=Rhea:RHEA:12320, ChEBI:CHEBI:15378,\nCC         ChEBI:CHEBI:17372, ChEBI:CHEBI:57783, ChEBI:CHEBI:58349,\nCC         ChEBI:CHEBI:77725; EC=1.3.1.73;\nCC         Evidence={ECO:0000250|UniProtKB:A0A0U3S9Q3};\nCC       PhysiologicalDirection=right-to-left; Xref=Rhea:RHEA:12322;\nCC         Evidence={ECO:0000250|UniProtKB:A0A0U3S9Q3};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 30,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0U4BHM2?format=txt&versions=30)

```json
{
  "evidence_id": "H5",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A0U4BHM2?format=txt&versions=30",
  "source_sha256": "f1ca3ed3dfca81ae192adab6c5b2e6c70586c275e9a49b6b2913846785e88634",
  "retrieved_utc": "2026-11-02T04:24:25.840272+00:00",
  "source_locator": "lines 47-53",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=(20S)-19,20-dihydrovomilenine + NADP(+) = vomilenine + NADPH +\nCC         H(+); Xref=Rhea:RHEA:79635, ChEBI:CHEBI:15378, ChEBI:CHEBI:16408,\nCC         ChEBI:CHEBI:57783, ChEBI:CHEBI:58349, ChEBI:CHEBI:230482;\nCC         Evidence={ECO:0000269|PubMed:26715562};\nCC       PhysiologicalDirection=right-to-left; Xref=Rhea:RHEA:79637;\nCC         Evidence={ECO:0000269|PubMed:26715562};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 30,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 142. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
