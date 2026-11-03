# EC_number_0119: before and after transfer clarification

[All 1,328 cases](../README.md) · [Method](../METHOD.md) · [Summary](../SUMMARY.md) · [Exact reviewer user message](../inputs/EC_number_0119.txt)

**Task:** `EC_number`  
**Author key, unchanged:** **C** — 1.1.1.122

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
MAAVGRYSGKVVVVTGGSRGIGAAIVRAFVDSGAQVVFCDKDEAGGRAVEQELLGTVFIPGDVTQEGDLQTLISETVSRFGHLDCVVNNAGYHPPAQLPEETSAQGFRQLLEENLLGAYTLIKLALPHLRKSKGNIINISSLVGAIGQSQALTYVATKGAVTAMTKALALDESRYGVRVNCISPGNIWTPLWQELAAATSDPRATILEGTLAQPLGRMGQPAEVGAAAVFLASEATFCTGLELFMTGGAELGYGRKASSSTLVEVPILPP

[Multiple Choices]
A. 1.1.1.336
B. 5.4.99.39
C. 1.1.1.122
D. 3.1.1.29
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

> The supplied sequence exactly matches the rat UniProt entry, whose EC 1.1.1.122 annotation is linked to experimental evidence (ECO:0000269) for oxidation of L-fucose and other sugars. This supports choice C, while preserving that the evidence is reported through a curated database entry citing a paper.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence's cofactor-binding motif and enzyme-family features may suggest an NAD-dependent oxidoreductase, helping distinguish it from an isomerase or hydrolase, but they do not establish the precise substrate specificity needed to distinguish the dehydrogenase options.


**Missing item-specific fact**

> The protein's experimentally characterized substrate specificity and corresponding EC annotation are not supplied in the question.


**Reason**

> Choosing the exact four-part EC number depends on protein-specific functional knowledge absent from the input; recognizing the sequence or consulting its annotation would resolve it, but is not reasoning from the supplied information.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The options designate distinct enzyme classifications, and the sequence-matched annotation with cited experimental evidence supports C. The sequence-only input does not itself resolve exact substrate specificity, but that is a lookup-dependence limitation rather than evidence that multiple options are correct.


### Important caveats

- The evidence is from a sequence-matched UniProt annotation citing a 2024 paper; the primary study was not independently reviewed here.
- The author’s exact data-construction snapshot is unknown, although the sequence-matched archived entry already records EC 1.1.1.122.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence's cofactor-binding motif and enzyme-family features may suggest an NAD-dependent oxidoreductase, helping distinguish it from an isomerase or hydrolase, but they do not establish the precise substrate specificity needed to distinguish the dehydrogenase options.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein's experimentally characterized substrate specificity and corresponding EC annotation are not supplied in the question.",
    "reason": "Choosing the exact four-part EC number depends on protein-specific functional knowledge absent from the input; recognizing the sequence or consulting its annotation would resolve it, but is not reasoning from the supplied information."
  },
  "case_id": "EC_number_0119",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "C7",
      "C8",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the rat UniProt entry, whose EC 1.1.1.122 annotation is linked to experimental evidence (ECO:0000269) for oxidation of L-fucose and other sugars. This supports choice C, while preserving that the evidence is reported through a curated database entry citing a paper."
  },
  "important_caveats": [
    "The evidence is from a sequence-matched UniProt annotation citing a 2024 paper; the primary study was not independently reviewed here.",
    "The author’s exact data-construction snapshot is unknown, although the sequence-matched archived entry already records EC 1.1.1.122."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The options designate distinct enzyme classifications, and the sequence-matched annotation with cited experimental evidence supports C. The sequence-only input does not itself resolve exact substrate specificity, but that is a lookup-dependence limitation rather than evidence that multiple options are correct."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0119",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the rat UniProt entry, whose EC 1.1.1.122 annotation is linked to experimental evidence (ECO:0000269) for oxidation of L-fucose and other sugars. This supports choice C, while preserving that the evidence is reported through a curated database entry citing a paper.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "C7", "C8", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence's cofactor-binding motif and enzyme-family features may suggest an NAD-dependent oxidoreductase, helping distinguish it from an isomerase or hydrolase, but they do not establish the precise substrate specificity needed to distinguish the dehydrogenase options.",
    "missing_item_specific_fact": "The protein's experimentally characterized substrate specificity and corresponding EC annotation are not supplied in the question.",
    "reason": "Choosing the exact four-part EC number depends on protein-specific functional knowledge absent from the input; recognizing the sequence or consulting its annotation would resolve it, but is not reasoning from the supplied information."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The options designate distinct enzyme classifications, and the sequence-matched annotation with cited experimental evidence supports C. The sequence-only input does not itself resolve exact substrate specificity, but that is a lookup-dependence limitation rather than evidence that multiple options are correct."
  },
  "important_caveats": [
    "The evidence is from a sequence-matched UniProt annotation citing a 2024 paper; the primary study was not independently reviewed here.",
    "The author’s exact data-construction snapshot is unknown, although the sequence-matched archived entry already records EC 1.1.1.122."
  ]
}
```

</details>

## Before: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry A0A8I6GJ95 (rat HSD17B14, 270 aa, sequence SHA256 matched) is annotated as L-fucose dehydrogenase with EC 1.1.1.122, supported by experimental evidence (ECO:0000269, PubMed:38944119, 2024 JBC paper by Witecka et al.). The catalytic activity L-fucose + NAD(+) = L-fucono-1,5-lactone + NADH + H(+) is confirmed experimentally. The expected answer C (1.1.1.122) is directly supported.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C8](#evidence-c8), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The N-terminal mitochondrial targeting signal and the Rossmann-fold NAD-binding motif (VVVTGGSRGIGAA) allow a model to infer this is an NAD-dependent dehydrogenase (EC 1.1.1.x), thereby eliminating the isomerase (B, EC 5.4.99.39) and hydrolase (D, EC 3.1.1.29). However, no general sequence feature distinguishes EC 1.1.1.122 (L-fucose dehydrogenase) from EC 1.1.1.336 (another EC 1.1.1.x dehydrogenase). The substrate-specificity residues that determine whether this enzyme acts on L-fucose versus the substrate of 1.1.1.336 are not identifiable from the raw sequence without prior knowledge of this particular protein's active-site architecture or its database annotation.


**Missing item-specific fact**

> The specific substrate-binding and catalytic-site residues that confer L-fucose specificity in HSD17B14, or alternatively the protein's identity as HSD17B14/L-fucose dehydrogenase (a function only experimentally established in 2024, PubMed:38944119), are required to distinguish EC 1.1.1.122 from EC 1.1.1.336.


**Reason**

> While the Rossmann fold provides a valid general argument for EC class 1.1.1.x (oxidoreductase, CH-OH, NAD+), selecting the fourth digit (122 vs 336) requires protein-specific knowledge. The function was only confirmed experimentally in 2024; before that, HSD17B14 had no well-established EC assignment. No general biological reasoning from the 270-aa sequence alone can distinguish these two EC 1.1.1.x options.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "C"
]
```

> Both A (1.1.1.336) and C (1.1.1.122) are EC 1.1.1.x oxidoreductases consistent with the Rossmann-fold NAD-binding motif visible in the sequence. Without protein-specific knowledge, a model cannot definitively choose between them. Options B (isomerase) and D (hydrolase) are clearly incompatible with the dehydrogenase fold and can be eliminated by reasoning.


### Important caveats

- The EC 1.1.1.122 assignment for HSD17B14 is very recent (2024, PubMed:38944119). Before this publication, HSD17B14 was primarily associated with mitochondrial RNA processing and lacked a confirmed EC number. A model trained on older data would not associate this sequence with EC 1.1.1.122.
- The protein's alternative name 'Hydroxysteroid 17-beta dehydrogenase 14' could mislead a model toward steroid-dehydrogenase EC numbers, which are not among the choices, adding to the lookup dependency.
- All UniProt evidence is reviewer-only and was not available to the evaluated model. The sequence-match is confirmed (SHA256 identical, 270 aa).
- The identity of EC 1.1.1.336 as a specific enzyme was not independently verified in this audit; it is treated as a plausible distractor within the same EC subclass.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal mitochondrial targeting signal and the Rossmann-fold NAD-binding motif (VVVTGGSRGIGAA) allow a model to infer this is an NAD-dependent dehydrogenase (EC 1.1.1.x), thereby eliminating the isomerase (B, EC 5.4.99.39) and hydrolase (D, EC 3.1.1.29). However, no general sequence feature distinguishes EC 1.1.1.122 (L-fucose dehydrogenase) from EC 1.1.1.336 (another EC 1.1.1.x dehydrogenase). The substrate-specificity residues that determine whether this enzyme acts on L-fucose versus the substrate of 1.1.1.336 are not identifiable from the raw sequence without prior knowledge of this particular protein's active-site architecture or its database annotation.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific substrate-binding and catalytic-site residues that confer L-fucose specificity in HSD17B14, or alternatively the protein's identity as HSD17B14/L-fucose dehydrogenase (a function only experimentally established in 2024, PubMed:38944119), are required to distinguish EC 1.1.1.122 from EC 1.1.1.336.",
    "reason": "While the Rossmann fold provides a valid general argument for EC class 1.1.1.x (oxidoreductase, CH-OH, NAD+), selecting the fourth digit (122 vs 336) requires protein-specific knowledge. The function was only confirmed experimentally in 2024; before that, HSD17B14 had no well-established EC assignment. No general biological reasoning from the 270-aa sequence alone can distinguish these two EC 1.1.1.x options."
  },
  "case_id": "EC_number_0119",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C8",
      "H2",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "UniProt entry A0A8I6GJ95 (rat HSD17B14, 270 aa, sequence SHA256 matched) is annotated as L-fucose dehydrogenase with EC 1.1.1.122, supported by experimental evidence (ECO:0000269, PubMed:38944119, 2024 JBC paper by Witecka et al.). The catalytic activity L-fucose + NAD(+) = L-fucono-1,5-lactone + NADH + H(+) is confirmed experimentally. The expected answer C (1.1.1.122) is directly supported."
  },
  "important_caveats": [
    "The EC 1.1.1.122 assignment for HSD17B14 is very recent (2024, PubMed:38944119). Before this publication, HSD17B14 was primarily associated with mitochondrial RNA processing and lacked a confirmed EC number. A model trained on older data would not associate this sequence with EC 1.1.1.122.",
    "The protein's alternative name 'Hydroxysteroid 17-beta dehydrogenase 14' could mislead a model toward steroid-dehydrogenase EC numbers, which are not among the choices, adding to the lookup dependency.",
    "All UniProt evidence is reviewer-only and was not available to the evaluated model. The sequence-match is confirmed (SHA256 identical, 270 aa).",
    "The identity of EC 1.1.1.336 as a specific enzyme was not independently verified in this audit; it is treated as a plausible distractor within the same EC subclass."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "C"
    ],
    "reason": "Both A (1.1.1.336) and C (1.1.1.122) are EC 1.1.1.x oxidoreductases consistent with the Rossmann-fold NAD-binding motif visible in the sequence. Without protein-specific knowledge, a model cannot definitively choose between them. Options B (isomerase) and D (hydrolase) are clearly incompatible with the dehydrogenase fold and can be eliminated by reasoning."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0119",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry A0A8I6GJ95 (rat HSD17B14, 270 aa, sequence SHA256 matched) is annotated as L-fucose dehydrogenase with EC 1.1.1.122, supported by experimental evidence (ECO:0000269, PubMed:38944119, 2024 JBC paper by Witecka et al.). The catalytic activity L-fucose + NAD(+) = L-fucono-1,5-lactone + NADH + H(+) is confirmed experimentally. The expected answer C (1.1.1.122) is directly supported.",
    "evidence_ids": ["C4", "C5", "C8", "H2", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The N-terminal mitochondrial targeting signal and the Rossmann-fold NAD-binding motif (VVVTGGSRGIGAA) allow a model to infer this is an NAD-dependent dehydrogenase (EC 1.1.1.x), thereby eliminating the isomerase (B, EC 5.4.99.39) and hydrolase (D, EC 3.1.1.29). However, no general sequence feature distinguishes EC 1.1.1.122 (L-fucose dehydrogenase) from EC 1.1.1.336 (another EC 1.1.1.x dehydrogenase). The substrate-specificity residues that determine whether this enzyme acts on L-fucose versus the substrate of 1.1.1.336 are not identifiable from the raw sequence without prior knowledge of this particular protein's active-site architecture or its database annotation.",
    "missing_item_specific_fact": "The specific substrate-binding and catalytic-site residues that confer L-fucose specificity in HSD17B14, or alternatively the protein's identity as HSD17B14/L-fucose dehydrogenase (a function only experimentally established in 2024, PubMed:38944119), are required to distinguish EC 1.1.1.122 from EC 1.1.1.336.",
    "reason": "While the Rossmann fold provides a valid general argument for EC class 1.1.1.x (oxidoreductase, CH-OH, NAD+), selecting the fourth digit (122 vs 336) requires protein-specific knowledge. The function was only confirmed experimentally in 2024; before that, HSD17B14 had no well-established EC assignment. No general biological reasoning from the 270-aa sequence alone can distinguish these two EC 1.1.1.x options."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "C"],
    "reason": "Both A (1.1.1.336) and C (1.1.1.122) are EC 1.1.1.x oxidoreductases consistent with the Rossmann-fold NAD-binding motif visible in the sequence. Without protein-specific knowledge, a model cannot definitively choose between them. Options B (isomerase) and D (hydrolase) are clearly incompatible with the dehydrogenase fold and can be eliminated by reasoning."
  },
  "important_caveats": [
    "The EC 1.1.1.122 assignment for HSD17B14 is very recent (2024, PubMed:38944119). Before this publication, HSD17B14 was primarily associated with mitochondrial RNA processing and lacked a confirmed EC number. A model trained on older data would not associate this sequence with EC 1.1.1.122.",
    "The protein's alternative name 'Hydroxysteroid 17-beta dehydrogenase 14' could mislead a model toward steroid-dehydrogenase EC numbers, which are not among the choices, adding to the lookup dependency.",
    "All UniProt evidence is reviewer-only and was not available to the evaluated model. The sequence-match is confirmed (SHA256 identical, 270 aa).",
    "The identity of EC 1.1.1.336 as a specific enzyme was not independently verified in this audit; it is treated as a plausible distractor within the same EC subclass."
  ]
}
```

</details>

## After: GPT-6 Luna

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The reviewer evidence identifies the matched sequence as EC 1.1.1.122 and links that assignment to an experimentally supported L-fucose dehydrogenase reaction. The assigned option is C.

Citations as saved: [C5](#evidence-c5), [C8](#evidence-c8), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The N-terminal glycine-rich Rossmann-like motif and the rest of the sequence are consistent with an NAD-dependent short-chain dehydrogenase/reductase. That supports an oxidoreductase-level inference, but does not meaningfully distinguish the substrate-specific EC choices A and C.


**Missing item-specific fact**

> The sequence input does not establish this protein's substrate specificity—particularly its experimentally reported oxidation of L-fucose—or otherwise distinguish EC 1.1.1.122 from the other dehydrogenase choice.


**Reason**

> The transferable sequence features support a dehydrogenase family/class inference, not the complete EC number. Selecting C depends on substrate-specific functional information for this protein that is not supplied in the question.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The EC alternatives specify distinct activities; the question has a definite target property, although the supplied sequence alone does not resolve its substrate specificity.


### Important caveats

- The reviewer-only UniProt evidence matches the supplied sequence and cites an experimental publication, but that evidence was not available as original model input.
- A Rossmann-like motif indicates likely cofactor-binding chemistry, not a particular substrate or complete EC number.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal glycine-rich Rossmann-like motif and the rest of the sequence are consistent with an NAD-dependent short-chain dehydrogenase/reductase. That supports an oxidoreductase-level inference, but does not meaningfully distinguish the substrate-specific EC choices A and C.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The sequence input does not establish this protein's substrate specificity—particularly its experimentally reported oxidation of L-fucose—or otherwise distinguish EC 1.1.1.122 from the other dehydrogenase choice.",
    "reason": "The transferable sequence features support a dehydrogenase family/class inference, not the complete EC number. Selecting C depends on substrate-specific functional information for this protein that is not supplied in the question."
  },
  "case_id": "EC_number_0119",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C8",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The reviewer evidence identifies the matched sequence as EC 1.1.1.122 and links that assignment to an experimentally supported L-fucose dehydrogenase reaction. The assigned option is C."
  },
  "important_caveats": [
    "The reviewer-only UniProt evidence matches the supplied sequence and cites an experimental publication, but that evidence was not available as original model input.",
    "A Rossmann-like motif indicates likely cofactor-binding chemistry, not a particular substrate or complete EC number."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The EC alternatives specify distinct activities; the question has a definite target property, although the supplied sequence alone does not resolve its substrate specificity."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0119",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The reviewer evidence identifies the matched sequence as EC 1.1.1.122 and links that assignment to an experimentally supported L-fucose dehydrogenase reaction. The assigned option is C.",
    "evidence_ids": ["C5", "C8", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The N-terminal glycine-rich Rossmann-like motif and the rest of the sequence are consistent with an NAD-dependent short-chain dehydrogenase/reductase. That supports an oxidoreductase-level inference, but does not meaningfully distinguish the substrate-specific EC choices A and C.",
    "missing_item_specific_fact": "The sequence input does not establish this protein's substrate specificity—particularly its experimentally reported oxidation of L-fucose—or otherwise distinguish EC 1.1.1.122 from the other dehydrogenase choice.",
    "reason": "The transferable sequence features support a dehydrogenase family/class inference, not the complete EC number. Selecting C depends on substrate-specific functional information for this protein that is not supplied in the question."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The EC alternatives specify distinct activities; the question has a definite target property, although the supplied sequence alone does not resolve its substrate specificity."
  },
  "important_caveats": [
    "The reviewer-only UniProt evidence matches the supplied sequence and cites an experimental publication, but that evidence was not available as original model input.",
    "A Rossmann-like motif indicates likely cofactor-binding chemistry, not a particular substrate or complete EC number."
  ]
}
```

</details>

## After: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A0A8I6GJ95 (sequence matched) annotates this protein as L-fucose dehydrogenase with EC 1.1.1.122, supported by experimental evidence (ECO:0000269, PubMed:38944119, 2024 JBC paper by Witecka et al. demonstrating HSD17B14 is an L-fucose dehydrogenase). The catalytic activity comments confirm the reaction L-fucose + NAD+ = L-fucono-1,5-lactone + NADH + H+ under EC 1.1.1.122.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence contains a clear Rossmann-fold NAD-binding motif (GSRGIGAAIVRA at the N-terminus), a short-chain dehydrogenase/reductase (SDR) catalytic architecture (~270 aa, VVG motif, and a YxxxK catalytic motif near the C-terminus in 'GYGRK'), and the 'VVFCDKDE' region. These features confidently identify the protein as an NAD-dependent dehydrogenase/reductase, eliminating option B (5.4.99.39, an isomerase) and option D (3.1.1.29, a carboxylester hydrolase). However, both remaining options A (1.1.1.336) and C (1.1.1.122) fall within the same EC class 1.1.1 (oxidoreductases acting on the CH-OH group with NAD+ as acceptor). General SDR superfamily knowledge establishes the 1.1.1.x assignment but does not resolve the fourth digit. The specific substrate (L-fucose vs. whatever 1.1.1.336 acts on) is determined by active-site geometry and experimental characterization, not by a broadly transferable sequence motif that distinguishes these two particular EC numbers.


**Missing item-specific fact**

> The specific substrate specificity of this enzyme (L-fucose dehydrogenase activity, EC 1.1.1.122) was established experimentally only in 2024 (PubMed:38944119). Distinguishing EC 1.1.1.122 from EC 1.1.1.336 requires knowing which specific CH-OH substrate this particular SDR enzyme oxidizes, a fact about this exact protein that is not encoded in a recognizable sequence motif distinguishable from other 1.1.1.x enzymes using general SDR family knowledge.


**Reason**

> The sequence unambiguously identifies an SDR/NAD-dependent dehydrogenase, ruling out the isomerase (B) and hydrolase (D) options through well-established family-level knowledge. However, the critical A-vs-C distinction (both 1.1.1.x) requires knowing the specific substrate of this protein, which was determined experimentally in 2024 and is not inferable from general SDR or Rossmann-fold knowledge. No conserved subfamily motif in the sequence reliably separates 1.1.1.336 from 1.1.1.122.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options B and D are clearly incompatible with the Rossmann-fold SDR architecture. Between A and C, the evidence supports C, and while the A-vs-C distinction is hard to make from sequence alone, only one is the experimentally validated annotation. No genuine ambiguity in the sense of two equally defensible choices exists given the evidence.


### Important caveats

- EC 1.1.1.336 is a less commonly referenced EC number; if it is obscure or not well-characterized, a model might default to the more familiar 1.1.1.122, but this would reflect familiarity bias rather than biological reasoning.
- The L-fucose dehydrogenase activity of HSD17B14 was only established in 2024; the protein was previously annotated under its HSD17B family name, so the EC 1.1.1.122 assignment is very recent.
- The sequence features (Rossmann fold, SDR catalytic tetrad, ~270 aa length) are consistent with the broad SDR superfamily but do not pinpoint the specific substrate class needed to resolve the fourth EC digit.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a clear Rossmann-fold NAD-binding motif (GSRGIGAAIVRA at the N-terminus), a short-chain dehydrogenase/reductase (SDR) catalytic architecture (~270 aa, VVG motif, and a YxxxK catalytic motif near the C-terminus in 'GYGRK'), and the 'VVFCDKDE' region. These features confidently identify the protein as an NAD-dependent dehydrogenase/reductase, eliminating option B (5.4.99.39, an isomerase) and option D (3.1.1.29, a carboxylester hydrolase). However, both remaining options A (1.1.1.336) and C (1.1.1.122) fall within the same EC class 1.1.1 (oxidoreductases acting on the CH-OH group with NAD+ as acceptor). General SDR superfamily knowledge establishes the 1.1.1.x assignment but does not resolve the fourth digit. The specific substrate (L-fucose vs. whatever 1.1.1.336 acts on) is determined by active-site geometry and experimental characterization, not by a broadly transferable sequence motif that distinguishes these two particular EC numbers.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific substrate specificity of this enzyme (L-fucose dehydrogenase activity, EC 1.1.1.122) was established experimentally only in 2024 (PubMed:38944119). Distinguishing EC 1.1.1.122 from EC 1.1.1.336 requires knowing which specific CH-OH substrate this particular SDR enzyme oxidizes, a fact about this exact protein that is not encoded in a recognizable sequence motif distinguishable from other 1.1.1.x enzymes using general SDR family knowledge.",
    "reason": "The sequence unambiguously identifies an SDR/NAD-dependent dehydrogenase, ruling out the isomerase (B) and hydrolase (D) options through well-established family-level knowledge. However, the critical A-vs-C distinction (both 1.1.1.x) requires knowing the specific substrate of this protein, which was determined experimentally in 2024 and is not inferable from general SDR or Rossmann-fold knowledge. No conserved subfamily motif in the sequence reliably separates 1.1.1.336 from 1.1.1.122."
  },
  "case_id": "EC_number_0119",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry A0A8I6GJ95 (sequence matched) annotates this protein as L-fucose dehydrogenase with EC 1.1.1.122, supported by experimental evidence (ECO:0000269, PubMed:38944119, 2024 JBC paper by Witecka et al. demonstrating HSD17B14 is an L-fucose dehydrogenase). The catalytic activity comments confirm the reaction L-fucose + NAD+ = L-fucono-1,5-lactone + NADH + H+ under EC 1.1.1.122."
  },
  "important_caveats": [
    "EC 1.1.1.336 is a less commonly referenced EC number; if it is obscure or not well-characterized, a model might default to the more familiar 1.1.1.122, but this would reflect familiarity bias rather than biological reasoning.",
    "The L-fucose dehydrogenase activity of HSD17B14 was only established in 2024; the protein was previously annotated under its HSD17B family name, so the EC 1.1.1.122 assignment is very recent.",
    "The sequence features (Rossmann fold, SDR catalytic tetrad, ~270 aa length) are consistent with the broad SDR superfamily but do not pinpoint the specific substrate class needed to resolve the fourth EC digit."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options B and D are clearly incompatible with the Rossmann-fold SDR architecture. Between A and C, the evidence supports C, and while the A-vs-C distinction is hard to make from sequence alone, only one is the experimentally validated annotation. No genuine ambiguity in the sense of two equally defensible choices exists given the evidence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0119",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A0A8I6GJ95 (sequence matched) annotates this protein as L-fucose dehydrogenase with EC 1.1.1.122, supported by experimental evidence (ECO:0000269, PubMed:38944119, 2024 JBC paper by Witecka et al. demonstrating HSD17B14 is an L-fucose dehydrogenase). The catalytic activity comments confirm the reaction L-fucose + NAD+ = L-fucono-1,5-lactone + NADH + H+ under EC 1.1.1.122.",
    "evidence_ids": ["C4", "C5", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence contains a clear Rossmann-fold NAD-binding motif (GSRGIGAAIVRA at the N-terminus), a short-chain dehydrogenase/reductase (SDR) catalytic architecture (~270 aa, VVG motif, and a YxxxK catalytic motif near the C-terminus in 'GYGRK'), and the 'VVFCDKDE' region. These features confidently identify the protein as an NAD-dependent dehydrogenase/reductase, eliminating option B (5.4.99.39, an isomerase) and option D (3.1.1.29, a carboxylester hydrolase). However, both remaining options A (1.1.1.336) and C (1.1.1.122) fall within the same EC class 1.1.1 (oxidoreductases acting on the CH-OH group with NAD+ as acceptor). General SDR superfamily knowledge establishes the 1.1.1.x assignment but does not resolve the fourth digit. The specific substrate (L-fucose vs. whatever 1.1.1.336 acts on) is determined by active-site geometry and experimental characterization, not by a broadly transferable sequence motif that distinguishes these two particular EC numbers.",
    "missing_item_specific_fact": "The specific substrate specificity of this enzyme (L-fucose dehydrogenase activity, EC 1.1.1.122) was established experimentally only in 2024 (PubMed:38944119). Distinguishing EC 1.1.1.122 from EC 1.1.1.336 requires knowing which specific CH-OH substrate this particular SDR enzyme oxidizes, a fact about this exact protein that is not encoded in a recognizable sequence motif distinguishable from other 1.1.1.x enzymes using general SDR family knowledge.",
    "reason": "The sequence unambiguously identifies an SDR/NAD-dependent dehydrogenase, ruling out the isomerase (B) and hydrolase (D) options through well-established family-level knowledge. However, the critical A-vs-C distinction (both 1.1.1.x) requires knowing the specific substrate of this protein, which was determined experimentally in 2024 and is not inferable from general SDR or Rossmann-fold knowledge. No conserved subfamily motif in the sequence reliably separates 1.1.1.336 from 1.1.1.122."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options B and D are clearly incompatible with the Rossmann-fold SDR architecture. Between A and C, the evidence supports C, and while the A-vs-C distinction is hard to make from sequence alone, only one is the experimentally validated annotation. No genuine ambiguity in the sense of two equally defensible choices exists given the evidence."
  },
  "important_caveats": [
    "EC 1.1.1.336 is a less commonly referenced EC number; if it is obscure or not well-characterized, a model might default to the more familiar 1.1.1.122, but this would reflect familiarity bias rather than biological reasoning.",
    "The L-fucose dehydrogenase activity of HSD17B14 was only established in 2024; the protein was previously annotated under its HSD17B family name, so the EC 1.1.1.122 assignment is very recent.",
    "The sequence features (Rossmann fold, SDR catalytic tetrad, ~270 aa length) are consistent with the broad SDR superfamily but do not pinpoint the specific substrate class needed to resolve the fourth EC digit."
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
  "requested_accession": "A0A8I6GJ95",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "benchmark_sequence_sha256": "bd37d1d516e73777e155d3437157c555ba99078fd50abfd1f3899c2c20580fad",
  "benchmark_sequence_length": 270,
  "current_status": "retrieved",
  "current_sequence_comparison": "matched",
  "current_entry_audit": {
    "entryVersion": 21,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2022-05-25",
    "sequenceVersion": 1
  },
  "current_uniprot_release": "2026_03",
  "current_record_sha256": "b771d75ec68fe3fe40ec9ce4a7c5be09aba6ba685a4b44078776bc6814ffb3ca",
  "current_source_sequence_sha256": "bd37d1d516e73777e155d3437157c555ba99078fd50abfd1f3899c2c20580fad",
  "current_source_sequence_length": 270,
  "historical_status": "retrieved",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "selected_historical_entry_version": 19,
  "selected_historical_version": {
    "accession": "A0A8I6GJ95",
    "database": "Swiss-Prot",
    "entryVersion": 19,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "DHB14_RAT",
    "sequenceVersion": 1
  },
  "selected_historical_record_sha256": "254b3aaa13d8772a07a9fba560b88aee21dbd339669de4833af8d223c7eed898",
  "selected_historical_source_sequence_sha256": "bd37d1d516e73777e155d3437157c555ba99078fd50abfd1f3899c2c20580fad",
  "selected_historical_source_sequence_length": 270,
  "latest_at_cutoff_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 19,
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8I6GJ95.json)

```json
{
  "evidence_id": "C1",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8I6GJ95.json",
  "source_sha256": "b771d75ec68fe3fe40ec9ce4a7c5be09aba6ba685a4b44078776bc6814ffb3ca",
  "retrieved_utc": "2026-11-01T06:25:12.152365+00:00",
  "json_pointer": "/primaryAccession",
  "excerpt": "\"A0A8I6GJ95\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8I6GJ95.json)

```json
{
  "evidence_id": "C2",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8I6GJ95.json",
  "source_sha256": "b771d75ec68fe3fe40ec9ce4a7c5be09aba6ba685a4b44078776bc6814ffb3ca",
  "retrieved_utc": "2026-11-01T06:25:12.152365+00:00",
  "json_pointer": "/entryAudit",
  "excerpt": "{\"entryVersion\":21,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2022-05-25\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8I6GJ95.json)

```json
{
  "evidence_id": "C3",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8I6GJ95.json",
  "source_sha256": "b771d75ec68fe3fe40ec9ce4a7c5be09aba6ba685a4b44078776bc6814ffb3ca",
  "retrieved_utc": "2026-11-01T06:25:12.152365+00:00",
  "json_pointer": "/organism",
  "excerpt": "{\"commonName\":\"Rat\",\"lineage\":[\"Eukaryota\",\"Metazoa\",\"Chordata\",\"Craniata\",\"Vertebrata\",\"Euteleostomi\",\"Mammalia\",\"Eutheria\",\"Euarchontoglires\",\"Glires\",\"Rodentia\",\"Myomorpha\",\"Muroidea\",\"Muridae\",\"Murinae\",\"Rattus\"],\"scientificName\":\"Rattus norvegicus\",\"taxonId\":10116}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8I6GJ95.json)

```json
{
  "evidence_id": "C4",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8I6GJ95.json",
  "source_sha256": "b771d75ec68fe3fe40ec9ce4a7c5be09aba6ba685a4b44078776bc6814ffb3ca",
  "retrieved_utc": "2026-11-01T06:25:12.152365+00:00",
  "json_pointer": "/proteinDescription",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"value\":\"Hydroxysteroid 17-beta dehydrogenase 14\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38944119\",\"source\":\"PubMed\"}],\"value\":\"1.1.1.122\"}],\"fullName\":{\"value\":\"L-fucose dehydrogenase\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8I6GJ95.json)

```json
{
  "evidence_id": "C5",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8I6GJ95.json",
  "source_sha256": "b771d75ec68fe3fe40ec9ce4a7c5be09aba6ba685a4b44078776bc6814ffb3ca",
  "retrieved_utc": "2026-11-01T06:25:12.152365+00:00",
  "json_pointer": "/comments/1",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"38944119\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:81516\"}}],\"reaction\":{\"ecNumber\":\"1.1.1.122\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38944119\",\"source\":\"PubMed\"}],\"name\":\"L-fucose + NAD(+) = L-fucono-1,5-lactone + NADH + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:81515\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:2181\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57540\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57945\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:81457\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8I6GJ95.json)

```json
{
  "evidence_id": "C6",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8I6GJ95.json",
  "source_sha256": "b771d75ec68fe3fe40ec9ce4a7c5be09aba6ba685a4b44078776bc6814ffb3ca",
  "retrieved_utc": "2026-11-01T06:25:12.152365+00:00",
  "json_pointer": "/comments/2",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"38944119\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:81520\"}}],\"reaction\":{\"ecNumber\":\"1.1.1.122\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38944119\",\"source\":\"PubMed\"}],\"name\":\"D-arabinose + NAD(+) = D-arabinono-1,5-lactone + NADH + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:81519\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:46994\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57540\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57945\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:194242\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8I6GJ95.json)

```json
{
  "evidence_id": "C7",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8I6GJ95.json",
  "source_sha256": "b771d75ec68fe3fe40ec9ce4a7c5be09aba6ba685a4b44078776bc6814ffb3ca",
  "retrieved_utc": "2026-11-01T06:25:12.152365+00:00",
  "json_pointer": "/comments/3",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"38944119\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:81524\"}}],\"reaction\":{\"ecNumber\":\"1.1.1.122\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38944119\",\"source\":\"PubMed\"}],\"name\":\"L-galactose + NAD(+) = L-galactono-1,5-lactone + NADH + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:81523\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:37619\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57540\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57945\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:182410\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8I6GJ95.json)

```json
{
  "evidence_id": "C8",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8I6GJ95.json",
  "source_sha256": "b771d75ec68fe3fe40ec9ce4a7c5be09aba6ba685a4b44078776bc6814ffb3ca",
  "retrieved_utc": "2026-11-01T06:25:12.152365+00:00",
  "json_pointer": "/references/1",
  "excerpt": "{\"citation\":{\"authors\":[\"Witecka A.\",\"Kazak V.\",\"Kwiatkowski S.\",\"Kiersztan A.\",\"Jagielski A.K.\",\"Kozminski W.\",\"Augustyniak R.\",\"Drozak J.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"38944119\"},{\"database\":\"DOI\",\"id\":\"10.1016/j.jbc.2024.107501\"}],\"citationType\":\"journal article\",\"firstPage\":\"107501\",\"id\":\"38944119\",\"journal\":\"J. Biol. Chem.\",\"lastPage\":\"107501\",\"publicationDate\":\"2024\",\"title\":\"Hydroxysteroid 17-beta dehydrogenase 14 (HSD17B14) is an L-fucose dehydrogenase, the initial enzyme of the L-fucose degradation pathway.\",\"volume\":\"300\"},\"referenceNumber\":2,\"referencePositions\":[\"CATALYTIC ACTIVITY\",\"FUNCTION\",\"BIOPHYSICOCHEMICAL PROPERTIES\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8I6GJ95?format=txt&versions=19)

```json
{
  "evidence_id": "H1",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A8I6GJ95?format=txt&versions=19",
  "source_sha256": "254b3aaa13d8772a07a9fba560b88aee21dbd339669de4833af8d223c7eed898",
  "retrieved_utc": "2026-11-01T06:42:06.511227+00:00",
  "source_locator": "lines 1-14",
  "excerpt": "ID   DHB14_RAT               Reviewed;         270 AA.\nAC   A0A8I6GJ95;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   25-MAY-2022, sequence version 1.\nDT   28-JAN-2026, entry version 19.\nDE   RecName: Full=L-fucose dehydrogenase;\nDE            EC=1.1.1.122 {ECO:0000269|PubMed:38944119};\nDE   AltName: Full=Hydroxysteroid 17-beta dehydrogenase 14;\nGN   Name=Hsd17b14;\nOS   Rattus norvegicus (Rat).\nOC   Eukaryota; Metazoa; Chordata; Craniata; Vertebrata; Euteleostomi; Mammalia;\nOC   Eutheria; Euarchontoglires; Glires; Rodentia; Myomorpha; Muroidea; Muridae;\nOC   Murinae; Rattus.\nOX   NCBI_TaxID=10116;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 19,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8I6GJ95?format=txt&versions=19)

```json
{
  "evidence_id": "H2",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A8I6GJ95?format=txt&versions=19",
  "source_sha256": "254b3aaa13d8772a07a9fba560b88aee21dbd339669de4833af8d223c7eed898",
  "retrieved_utc": "2026-11-01T06:42:06.511227+00:00",
  "source_locator": "lines 6-8",
  "excerpt": "DE   RecName: Full=L-fucose dehydrogenase;\nDE            EC=1.1.1.122 {ECO:0000269|PubMed:38944119};\nDE   AltName: Full=Hydroxysteroid 17-beta dehydrogenase 14;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 19,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8I6GJ95?format=txt&versions=19)

```json
{
  "evidence_id": "H3",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A8I6GJ95?format=txt&versions=19",
  "source_sha256": "254b3aaa13d8772a07a9fba560b88aee21dbd339669de4833af8d223c7eed898",
  "retrieved_utc": "2026-11-01T06:42:06.511227+00:00",
  "source_locator": "lines 62-69",
  "excerpt": "RN   [2]\nRP   CATALYTIC ACTIVITY, FUNCTION, AND BIOPHYSICOCHEMICAL PROPERTIES.\nRX   PubMed=38944119; DOI=10.1016/j.jbc.2024.107501;\nRA   Witecka A., Kazak V., Kwiatkowski S., Kiersztan A., Jagielski A.K.,\nRA   Kozminski W., Augustyniak R., Drozak J.;\nRT   \"Hydroxysteroid 17-beta dehydrogenase 14 (HSD17B14) is an L-fucose\nRT   dehydrogenase, the initial enzyme of the L-fucose degradation pathway.\";\nRL   J. Biol. Chem. 300:107501-107501(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 19,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8I6GJ95?format=txt&versions=19)

```json
{
  "evidence_id": "H4",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A8I6GJ95?format=txt&versions=19",
  "source_sha256": "254b3aaa13d8772a07a9fba560b88aee21dbd339669de4833af8d223c7eed898",
  "retrieved_utc": "2026-11-01T06:42:06.511227+00:00",
  "source_locator": "lines 77-83",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=L-fucose + NAD(+) = L-fucono-1,5-lactone + NADH + H(+);\nCC         Xref=Rhea:RHEA:81515, ChEBI:CHEBI:2181, ChEBI:CHEBI:15378,\nCC         ChEBI:CHEBI:57540, ChEBI:CHEBI:57945, ChEBI:CHEBI:81457;\nCC         EC=1.1.1.122; Evidence={ECO:0000269|PubMed:38944119};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:81516;\nCC         Evidence={ECO:0000305|PubMed:38944119};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 19,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8I6GJ95?format=txt&versions=19)

```json
{
  "evidence_id": "H5",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A8I6GJ95?format=txt&versions=19",
  "source_sha256": "254b3aaa13d8772a07a9fba560b88aee21dbd339669de4833af8d223c7eed898",
  "retrieved_utc": "2026-11-01T06:42:06.511227+00:00",
  "source_locator": "lines 84-90",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=D-arabinose + NAD(+) = D-arabinono-1,5-lactone + NADH + H(+);\nCC         Xref=Rhea:RHEA:81519, ChEBI:CHEBI:15378, ChEBI:CHEBI:46994,\nCC         ChEBI:CHEBI:57540, ChEBI:CHEBI:57945, ChEBI:CHEBI:194242;\nCC         EC=1.1.1.122; Evidence={ECO:0000269|PubMed:38944119};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:81520;\nCC         Evidence={ECO:0000305|PubMed:38944119};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 19,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8I6GJ95?format=txt&versions=19)

```json
{
  "evidence_id": "H6",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A8I6GJ95?format=txt&versions=19",
  "source_sha256": "254b3aaa13d8772a07a9fba560b88aee21dbd339669de4833af8d223c7eed898",
  "retrieved_utc": "2026-11-01T06:42:06.511227+00:00",
  "source_locator": "lines 91-97",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=L-galactose + NAD(+) = L-galactono-1,5-lactone + NADH + H(+);\nCC         Xref=Rhea:RHEA:81523, ChEBI:CHEBI:15378, ChEBI:CHEBI:37619,\nCC         ChEBI:CHEBI:57540, ChEBI:CHEBI:57945, ChEBI:CHEBI:182410;\nCC         EC=1.1.1.122; Evidence={ECO:0000269|PubMed:38944119};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:81524;\nCC         Evidence={ECO:0000305|PubMed:38944119};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 19,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 119. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
