# catalytic_activity_0190: before and after transfer clarification

[All 1,328 cases](../README.md) · [Method](../METHOD.md) · [Summary](../SUMMARY.md) · [Exact reviewer user message](../inputs/catalytic_activity_0190.txt)

**Task:** `catalytic_activity`  
**Author key, unchanged:** **D** — L-fucose + NAD(+) = L-fucono-1,5-lactone + NADH + H(+)

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
MAAVTRYSGKVVVVTGGSRGIGAAIVRAFVDSGAQVVFCDKDEAGGRALEQELSGTVFIPGDVTQERDLQTLVSETLSRFGHLDCVVNNAGYHPPAQLPEETSAQGFRQLLEVNLLGTYTLIKLALPHLRKSRGNIINISSLVGAIGQSQALTYVATKGAVTAMTKALALDESRHGVRVNCISPGNIWTPLWEELAASTSDPRATILEGTLAQPLGRMGQPAEVAAAAVFLASEATFCTGLELLVTGGAELGYGRKASKSSLGEVPTLPPNVH

[Multiple Choices]
A. a 3-O-beta-D-glucosyl-beta-D-glucuronoside + phosphate = a beta-D-glucuronoside + alpha-D-glucose 1-phosphate
B. (2R,3R,5S)-2-(S-pantetheinyl)-carbapenam-3-carboxylate + AH2 + 2 S-adenosyl-L-methionine = (2R,3R,5S,6R)-6-(methyl)-2-(S-pantetheinyl)-carbapenam-3-carboxylate + 5'-deoxyadenosine + L-methionine + A + S-adenosyl-L-homocysteine + 2 H(+)
C. demethylluteothin + S-adenosyl-L-methionine = luteothin + S-adenosyl-L-homocysteine
D. L-fucose + NAD(+) = L-fucono-1,5-lactone + NADH + H(+)
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

> The sequence exactly matches the mouse UniProt entry annotated with reaction D. However, the catalytic-activity annotation is transferred by similarity from Q9BPX1 (ECO:0000250), not evidence here of a direct experiment on this protein.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The N-terminal glycine-rich motif is consistent with an NAD-binding dehydrogenase, which favors D over the glycosidase and methyltransferase choices. It does not establish L-fucose as the substrate.


**Missing item-specific fact**

> The protein's substrate specificity—particularly its annotated or experimentally established activity on L-fucose—is not supplied.


**Reason**

> Sequence features can suggest a dehydrogenase family, but assigning the precise L-fucose-to-lactone reaction depends on protein-specific functional information.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The options describe distinct reaction types, and D is the one consistent with the likely NAD-dependent dehydrogenase class; the uncertainty is the exact substrate specificity, not an equally supported alternative.


### Important caveats

- The evidence supports D as a database annotation for the sequence, but the cited evidence is transferred by similarity and does not independently establish direct experimental validation for this mouse protein.
- The author's exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal glycine-rich motif is consistent with an NAD-binding dehydrogenase, which favors D over the glycosidase and methyltransferase choices. It does not establish L-fucose as the substrate.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein's substrate specificity—particularly its annotated or experimentally established activity on L-fucose—is not supplied.",
    "reason": "Sequence features can suggest a dehydrogenase family, but assigning the precise L-fucose-to-lactone reaction depends on protein-specific functional information."
  },
  "case_id": "catalytic_activity_0190",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H2",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The sequence exactly matches the mouse UniProt entry annotated with reaction D. However, the catalytic-activity annotation is transferred by similarity from Q9BPX1 (ECO:0000250), not evidence here of a direct experiment on this protein."
  },
  "important_caveats": [
    "The evidence supports D as a database annotation for the sequence, but the cited evidence is transferred by similarity and does not independently establish direct experimental validation for this mouse protein.",
    "The author's exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The options describe distinct reaction types, and D is the one consistent with the likely NAD-dependent dehydrogenase class; the uncertainty is the exact substrate specificity, not an equally supported alternative."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0190",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence exactly matches the mouse UniProt entry annotated with reaction D. However, the catalytic-activity annotation is transferred by similarity from Q9BPX1 (ECO:0000250), not evidence here of a direct experiment on this protein.",
    "evidence_ids": ["C1", "C4", "C5", "H2", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The N-terminal glycine-rich motif is consistent with an NAD-binding dehydrogenase, which favors D over the glycosidase and methyltransferase choices. It does not establish L-fucose as the substrate.",
    "missing_item_specific_fact": "The protein's substrate specificity—particularly its annotated or experimentally established activity on L-fucose—is not supplied.",
    "reason": "Sequence features can suggest a dehydrogenase family, but assigning the precise L-fucose-to-lactone reaction depends on protein-specific functional information."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The options describe distinct reaction types, and D is the one consistent with the likely NAD-dependent dehydrogenase class; the uncertainty is the exact substrate specificity, not an equally supported alternative."
  },
  "important_caveats": [
    "The evidence supports D as a database annotation for the sequence, but the cited evidence is transferred by similarity and does not independently establish direct experimental validation for this mouse protein.",
    "The author's exact source snapshot is unknown."
  ]
}
```

</details>

## Before: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt E9Q3D4 (sequence SHA256 match confirmed) is annotated as L-fucose dehydrogenase (EC 1.1.1.122) with the exact catalytic reaction 'L-fucose + NAD(+) = L-fucono-1,5-lactone + NADH + H(+)' listed as the primary reaction (C5, H3). The evidence code is ECO:0000250 (inferred by similarity from human ortholog Q9BPX1), making this a transferred annotation rather than direct experimental evidence for the mouse protein, but it is the authoritative database annotation for this exact sequence. The entry also lists D-arabinose and L-galactose as alternative substrates (C6, C7), but L-fucose is the recommended/primary reaction. The expected answer matches the annotation exactly.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence displays hallmark short-chain dehydrogenase/reductase (SDR) family architecture: an N-terminal Rossmann-fold NAD-binding motif (VVVVTGGSRGIGAAIVRAF, containing the GxGxxG pattern GSRGIGAA) and a C-terminal catalytic tetrad region (YGRK near the C-terminus, consistent with the Tyr-x-x-x-Lys pair). SDRs catalyze simple NAD(P)+-dependent oxidation of alcohols/aldehydes/ketones. Among the four choices, only option D (L-fucose + NAD+ → L-fucono-1,5-lactone + NADH + H+) represents a simple NAD-dependent dehydrogenase reaction consistent with SDR mechanism. Option A is a phosphorylase reaction (no NAD, different fold), option B is a radical SAM carbapenam synthase reaction (requires radical chemistry and SAM, incompatible with SDR fold), and option C is an O-methyltransferase reaction (SAM-dependent, no NAD). The SDR family identification from sequence features eliminates three of four options without needing to memorize the specific UniProt entry.


**Missing item-specific fact**

> None critical. The specific substrate identity (L-fucose vs. D-arabinose or L-galactose, which are also listed in the UniProt entry) would require item-specific knowledge, but those alternatives are not among the answer choices, so the SDR-family reasoning suffices to select D uniquely.


**Reason**

> A knowledgeable reader can identify the SDR family from the Rossmann-fold and catalytic-tetrad motifs, then eliminate the phosphorylase, radical SAM, and methyltransferase options as mechanistically incompatible with SDR architecture. This leaves D as the only viable answer through general enzymology reasoning.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Although the UniProt entry lists three substrates (L-fucose, D-arabinose, L-galactose) for this enzyme, only L-fucose appears among the answer choices. The other three options represent entirely different enzyme classes (phosphorylase, radical SAM synthase, methyltransferase) that are mechanistically incompatible with the SDR fold evident in the sequence. No ambiguity exists among the provided choices.


### Important caveats

- The UniProt annotation carries evidence code ECO:0000250 (inferred by similarity from human Q9BPX1), meaning the L-fucose dehydrogenase assignment for the mouse protein is a computational transfer, not a direct experimental measurement on this exact protein.
- The entry is relatively new (first public date 2025-04-09); the author's source snapshot is unknown, so the annotation available at benchmark construction time may have differed.
- The protein also has the alternative name 'Hydroxysteroid 17-beta dehydrogenase 14,' reflecting its SDR-family membership and potential broader substrate range, but this does not conflict with the L-fucose dehydrogenase annotation.
- The sequence is 273 aa, consistent with a monomeric SDR; no cofactor-binding anomalies or truncations are apparent.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence displays hallmark short-chain dehydrogenase/reductase (SDR) family architecture: an N-terminal Rossmann-fold NAD-binding motif (VVVVTGGSRGIGAAIVRAF, containing the GxGxxG pattern GSRGIGAA) and a C-terminal catalytic tetrad region (YGRK near the C-terminus, consistent with the Tyr-x-x-x-Lys pair). SDRs catalyze simple NAD(P)+-dependent oxidation of alcohols/aldehydes/ketones. Among the four choices, only option D (L-fucose + NAD+ → L-fucono-1,5-lactone + NADH + H+) represents a simple NAD-dependent dehydrogenase reaction consistent with SDR mechanism. Option A is a phosphorylase reaction (no NAD, different fold), option B is a radical SAM carbapenam synthase reaction (requires radical chemistry and SAM, incompatible with SDR fold), and option C is an O-methyltransferase reaction (SAM-dependent, no NAD). The SDR family identification from sequence features eliminates three of four options without needing to memorize the specific UniProt entry.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None critical. The specific substrate identity (L-fucose vs. D-arabinose or L-galactose, which are also listed in the UniProt entry) would require item-specific knowledge, but those alternatives are not among the answer choices, so the SDR-family reasoning suffices to select D uniquely.",
    "reason": "A knowledgeable reader can identify the SDR family from the Rossmann-fold and catalytic-tetrad motifs, then eliminate the phosphorylase, radical SAM, and methyltransferase options as mechanistically incompatible with SDR architecture. This leaves D as the only viable answer through general enzymology reasoning."
  },
  "case_id": "catalytic_activity_0190",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2",
      "H3"
    ],
    "judgment": "supported",
    "reason": "UniProt E9Q3D4 (sequence SHA256 match confirmed) is annotated as L-fucose dehydrogenase (EC 1.1.1.122) with the exact catalytic reaction 'L-fucose + NAD(+) = L-fucono-1,5-lactone + NADH + H(+)' listed as the primary reaction (C5, H3). The evidence code is ECO:0000250 (inferred by similarity from human ortholog Q9BPX1), making this a transferred annotation rather than direct experimental evidence for the mouse protein, but it is the authoritative database annotation for this exact sequence. The entry also lists D-arabinose and L-galactose as alternative substrates (C6, C7), but L-fucose is the recommended/primary reaction. The expected answer matches the annotation exactly."
  },
  "important_caveats": [
    "The UniProt annotation carries evidence code ECO:0000250 (inferred by similarity from human Q9BPX1), meaning the L-fucose dehydrogenase assignment for the mouse protein is a computational transfer, not a direct experimental measurement on this exact protein.",
    "The entry is relatively new (first public date 2025-04-09); the author's source snapshot is unknown, so the annotation available at benchmark construction time may have differed.",
    "The protein also has the alternative name 'Hydroxysteroid 17-beta dehydrogenase 14,' reflecting its SDR-family membership and potential broader substrate range, but this does not conflict with the L-fucose dehydrogenase annotation.",
    "The sequence is 273 aa, consistent with a monomeric SDR; no cofactor-binding anomalies or truncations are apparent."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although the UniProt entry lists three substrates (L-fucose, D-arabinose, L-galactose) for this enzyme, only L-fucose appears among the answer choices. The other three options represent entirely different enzyme classes (phosphorylase, radical SAM synthase, methyltransferase) that are mechanistically incompatible with the SDR fold evident in the sequence. No ambiguity exists among the provided choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0190",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt E9Q3D4 (sequence SHA256 match confirmed) is annotated as L-fucose dehydrogenase (EC 1.1.1.122) with the exact catalytic reaction 'L-fucose + NAD(+) = L-fucono-1,5-lactone + NADH + H(+)' listed as the primary reaction (C5, H3). The evidence code is ECO:0000250 (inferred by similarity from human ortholog Q9BPX1), making this a transferred annotation rather than direct experimental evidence for the mouse protein, but it is the authoritative database annotation for this exact sequence. The entry also lists D-arabinose and L-galactose as alternative substrates (C6, C7), but L-fucose is the recommended/primary reaction. The expected answer matches the annotation exactly.",
    "evidence_ids": ["C4", "C5", "H2", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence displays hallmark short-chain dehydrogenase/reductase (SDR) family architecture: an N-terminal Rossmann-fold NAD-binding motif (VVVVTGGSRGIGAAIVRAF, containing the GxGxxG pattern GSRGIGAA) and a C-terminal catalytic tetrad region (YGRK near the C-terminus, consistent with the Tyr-x-x-x-Lys pair). SDRs catalyze simple NAD(P)+-dependent oxidation of alcohols/aldehydes/ketones. Among the four choices, only option D (L-fucose + NAD+ → L-fucono-1,5-lactone + NADH + H+) represents a simple NAD-dependent dehydrogenase reaction consistent with SDR mechanism. Option A is a phosphorylase reaction (no NAD, different fold), option B is a radical SAM carbapenam synthase reaction (requires radical chemistry and SAM, incompatible with SDR fold), and option C is an O-methyltransferase reaction (SAM-dependent, no NAD). The SDR family identification from sequence features eliminates three of four options without needing to memorize the specific UniProt entry.",
    "missing_item_specific_fact": "None critical. The specific substrate identity (L-fucose vs. D-arabinose or L-galactose, which are also listed in the UniProt entry) would require item-specific knowledge, but those alternatives are not among the answer choices, so the SDR-family reasoning suffices to select D uniquely.",
    "reason": "A knowledgeable reader can identify the SDR family from the Rossmann-fold and catalytic-tetrad motifs, then eliminate the phosphorylase, radical SAM, and methyltransferase options as mechanistically incompatible with SDR architecture. This leaves D as the only viable answer through general enzymology reasoning."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although the UniProt entry lists three substrates (L-fucose, D-arabinose, L-galactose) for this enzyme, only L-fucose appears among the answer choices. The other three options represent entirely different enzyme classes (phosphorylase, radical SAM synthase, methyltransferase) that are mechanistically incompatible with the SDR fold evident in the sequence. No ambiguity exists among the provided choices."
  },
  "important_caveats": [
    "The UniProt annotation carries evidence code ECO:0000250 (inferred by similarity from human Q9BPX1), meaning the L-fucose dehydrogenase assignment for the mouse protein is a computational transfer, not a direct experimental measurement on this exact protein.",
    "The entry is relatively new (first public date 2025-04-09); the author's source snapshot is unknown, so the annotation available at benchmark construction time may have differed.",
    "The protein also has the alternative name 'Hydroxysteroid 17-beta dehydrogenase 14,' reflecting its SDR-family membership and potential broader substrate range, but this does not conflict with the L-fucose dehydrogenase annotation.",
    "The sequence is 273 aa, consistent with a monomeric SDR; no cofactor-binding anomalies or truncations are apparent."
  ]
}
```

</details>

## After: GPT-6 Luna

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence-matched UniProt record assigns this protein L-fucose dehydrogenase activity and the reaction in option D. The assignment is supported by similarity evidence from Q9BPX1 (ECO:0000250), so it is an annotation by transfer rather than evidence of direct experimental characterization of this protein.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has an N-terminal glycine-rich Rossmann-like motif (around VVTGGSRGIG), consistent with an NAD-dependent oxidoreductase, and its length and motif pattern are compatible with the short-chain dehydrogenase/reductase family. That makes option D, an NAD-dependent sugar oxidation, meaningfully more plausible than the glycoside phosphorylase in A or the SAM-dependent reactions in B and C. This is a family-level inference, not proof of the exact substrate.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Transferable sequence and enzyme-family knowledge distinguishes the NAD-dependent dehydrogenase choice from the other reaction types. The exact substrate assignment is less certain from sequence alone, but the alternatives make the family-level distinction useful.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Only D matches the oxidoreductase class suggested by the sequence among the offered choices.


### Important caveats

- The cited catalytic-activity annotation is transferred from a homolog and should not be described as direct experimental confirmation for this exact protein.
- The record also lists related sugar oxidation reactions, so the sequence-based choice among these options does not establish that L-fucose is the only substrate.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has an N-terminal glycine-rich Rossmann-like motif (around VVTGGSRGIG), consistent with an NAD-dependent oxidoreductase, and its length and motif pattern are compatible with the short-chain dehydrogenase/reductase family. That makes option D, an NAD-dependent sugar oxidation, meaningfully more plausible than the glycoside phosphorylase in A or the SAM-dependent reactions in B and C. This is a family-level inference, not proof of the exact substrate.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Transferable sequence and enzyme-family knowledge distinguishes the NAD-dependent dehydrogenase choice from the other reaction types. The exact substrate assignment is less certain from sequence alone, but the alternatives make the family-level distinction useful."
  },
  "case_id": "catalytic_activity_0190",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record assigns this protein L-fucose dehydrogenase activity and the reaction in option D. The assignment is supported by similarity evidence from Q9BPX1 (ECO:0000250), so it is an annotation by transfer rather than evidence of direct experimental characterization of this protein."
  },
  "important_caveats": [
    "The cited catalytic-activity annotation is transferred from a homolog and should not be described as direct experimental confirmation for this exact protein.",
    "The record also lists related sugar oxidation reactions, so the sequence-based choice among these options does not establish that L-fucose is the only substrate."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only D matches the oxidoreductase class suggested by the sequence among the offered choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0190",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record assigns this protein L-fucose dehydrogenase activity and the reaction in option D. The assignment is supported by similarity evidence from Q9BPX1 (ECO:0000250), so it is an annotation by transfer rather than evidence of direct experimental characterization of this protein.",
    "evidence_ids": ["C4", "C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has an N-terminal glycine-rich Rossmann-like motif (around VVTGGSRGIG), consistent with an NAD-dependent oxidoreductase, and its length and motif pattern are compatible with the short-chain dehydrogenase/reductase family. That makes option D, an NAD-dependent sugar oxidation, meaningfully more plausible than the glycoside phosphorylase in A or the SAM-dependent reactions in B and C. This is a family-level inference, not proof of the exact substrate.",
    "missing_item_specific_fact": "",
    "reason": "Transferable sequence and enzyme-family knowledge distinguishes the NAD-dependent dehydrogenase choice from the other reaction types. The exact substrate assignment is less certain from sequence alone, but the alternatives make the family-level distinction useful."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only D matches the oxidoreductase class suggested by the sequence among the offered choices."
  },
  "important_caveats": [
    "The cited catalytic-activity annotation is transferred from a homolog and should not be described as direct experimental confirmation for this exact protein.",
    "The record also lists related sugar oxidation reactions, so the sequence-based choice among these options does not establish that L-fucose is the only substrate."
  ]
}
```

</details>

## After: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry E9Q3D4 annotates this sequence as L-fucose dehydrogenase (EC 1.1.1.122) with the catalytic activity L-fucose + NAD(+) = L-fucono-1,5-lactone + NADH + H(+). The annotation evidence code is ECO:0000250 (transferred by similarity from human ortholog Q9BPX1), meaning this is a computational/similarity-based annotation rather than direct experimental characterization of this exact mouse protein. The annotation nonetheless supports the expected answer as the recorded function.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains an unambiguous Rossmann-fold NAD(P)-binding motif at the N-terminus: 'VVVVTGGSRGIGAAIVRAF' (the GGxGxG glycine-rich loop). This immediately identifies the protein as an NAD(P)-dependent oxidoreductase. Among the four choices, only D (L-fucose + NAD(+) → L-fucono-1,5-lactone + NADH + H+) is an NAD-dependent dehydrogenase reaction. Choice A is a phosphorylase (no cofactor), B is a radical-SAM enzyme (uses SAM and a reductant AH2, not NAD), and C is a SAM-dependent methyltransferase (no NAD). Furthermore, the overall length (273 aa) and conserved SDR-family motifs ('NISSLVGA' catalytic region, 'TGGAELGYGRK' C-terminal motif) confirm membership in the short-chain dehydrogenase/reductase superfamily, which is exclusively composed of NAD(P)-dependent enzymes. This family-level identification plus the NAD-binding motif cleanly eliminates A, B, and C and selects D.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The Rossmann-fold NAD-binding motif and SDR-family sequence architecture are directly readable from the input sequence and represent transferable knowledge about protein families. Since D is the only NAD-dependent dehydrogenase among the four options, family-level recognition of an SDR/NAD-binding enzyme is sufficient to select D without needing to recall the exact substrate specificity of this particular mouse protein. The other three choices are mechanistically incompatible with the visible cofactor-binding architecture.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Only one option (D) is an NAD-dependent dehydrogenase reaction. The Rossmann-fold motif unambiguously identifies the enzyme as an NAD(P)-dependent oxidoreductase, making A (phosphorylase), B (radical SAM), and C (methyltransferase) clearly incompatible. No other option is defensible given the sequence features.


### Important caveats

- The UniProt annotation for E9Q3D4 is based on similarity transfer (ECO:0000250) from the human ortholog Q9BPX1, not direct experimental characterization of the mouse protein itself.
- The SDR family is very large and functionally diverse; identifying the specific substrate (L-fucose) among many possible SDR substrates would require more detailed knowledge. However, this is unnecessary here because D is the sole dehydrogenase option among the four choices.
- The protein is also annotated with alternative names including 'Hydroxysteroid 17-beta dehydrogenase 14,' reflecting its historical classification. The reannotation as L-fucose dehydrogenase is relatively recent (entry first public 2025-04-09).

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains an unambiguous Rossmann-fold NAD(P)-binding motif at the N-terminus: 'VVVVTGGSRGIGAAIVRAF' (the GGxGxG glycine-rich loop). This immediately identifies the protein as an NAD(P)-dependent oxidoreductase. Among the four choices, only D (L-fucose + NAD(+) → L-fucono-1,5-lactone + NADH + H+) is an NAD-dependent dehydrogenase reaction. Choice A is a phosphorylase (no cofactor), B is a radical-SAM enzyme (uses SAM and a reductant AH2, not NAD), and C is a SAM-dependent methyltransferase (no NAD). Furthermore, the overall length (273 aa) and conserved SDR-family motifs ('NISSLVGA' catalytic region, 'TGGAELGYGRK' C-terminal motif) confirm membership in the short-chain dehydrogenase/reductase superfamily, which is exclusively composed of NAD(P)-dependent enzymes. This family-level identification plus the NAD-binding motif cleanly eliminates A, B, and C and selects D.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The Rossmann-fold NAD-binding motif and SDR-family sequence architecture are directly readable from the input sequence and represent transferable knowledge about protein families. Since D is the only NAD-dependent dehydrogenase among the four options, family-level recognition of an SDR/NAD-binding enzyme is sufficient to select D without needing to recall the exact substrate specificity of this particular mouse protein. The other three choices are mechanistically incompatible with the visible cofactor-binding architecture."
  },
  "case_id": "catalytic_activity_0190",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry E9Q3D4 annotates this sequence as L-fucose dehydrogenase (EC 1.1.1.122) with the catalytic activity L-fucose + NAD(+) = L-fucono-1,5-lactone + NADH + H(+). The annotation evidence code is ECO:0000250 (transferred by similarity from human ortholog Q9BPX1), meaning this is a computational/similarity-based annotation rather than direct experimental characterization of this exact mouse protein. The annotation nonetheless supports the expected answer as the recorded function."
  },
  "important_caveats": [
    "The UniProt annotation for E9Q3D4 is based on similarity transfer (ECO:0000250) from the human ortholog Q9BPX1, not direct experimental characterization of the mouse protein itself.",
    "The SDR family is very large and functionally diverse; identifying the specific substrate (L-fucose) among many possible SDR substrates would require more detailed knowledge. However, this is unnecessary here because D is the sole dehydrogenase option among the four choices.",
    "The protein is also annotated with alternative names including 'Hydroxysteroid 17-beta dehydrogenase 14,' reflecting its historical classification. The reannotation as L-fucose dehydrogenase is relatively recent (entry first public 2025-04-09)."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only one option (D) is an NAD-dependent dehydrogenase reaction. The Rossmann-fold motif unambiguously identifies the enzyme as an NAD(P)-dependent oxidoreductase, making A (phosphorylase), B (radical SAM), and C (methyltransferase) clearly incompatible. No other option is defensible given the sequence features."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0190",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry E9Q3D4 annotates this sequence as L-fucose dehydrogenase (EC 1.1.1.122) with the catalytic activity L-fucose + NAD(+) = L-fucono-1,5-lactone + NADH + H(+). The annotation evidence code is ECO:0000250 (transferred by similarity from human ortholog Q9BPX1), meaning this is a computational/similarity-based annotation rather than direct experimental characterization of this exact mouse protein. The annotation nonetheless supports the expected answer as the recorded function.",
    "evidence_ids": ["C4", "C5", "H2", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains an unambiguous Rossmann-fold NAD(P)-binding motif at the N-terminus: 'VVVVTGGSRGIGAAIVRAF' (the GGxGxG glycine-rich loop). This immediately identifies the protein as an NAD(P)-dependent oxidoreductase. Among the four choices, only D (L-fucose + NAD(+) → L-fucono-1,5-lactone + NADH + H+) is an NAD-dependent dehydrogenase reaction. Choice A is a phosphorylase (no cofactor), B is a radical-SAM enzyme (uses SAM and a reductant AH2, not NAD), and C is a SAM-dependent methyltransferase (no NAD). Furthermore, the overall length (273 aa) and conserved SDR-family motifs ('NISSLVGA' catalytic region, 'TGGAELGYGRK' C-terminal motif) confirm membership in the short-chain dehydrogenase/reductase superfamily, which is exclusively composed of NAD(P)-dependent enzymes. This family-level identification plus the NAD-binding motif cleanly eliminates A, B, and C and selects D.",
    "missing_item_specific_fact": "",
    "reason": "The Rossmann-fold NAD-binding motif and SDR-family sequence architecture are directly readable from the input sequence and represent transferable knowledge about protein families. Since D is the only NAD-dependent dehydrogenase among the four options, family-level recognition of an SDR/NAD-binding enzyme is sufficient to select D without needing to recall the exact substrate specificity of this particular mouse protein. The other three choices are mechanistically incompatible with the visible cofactor-binding architecture."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only one option (D) is an NAD-dependent dehydrogenase reaction. The Rossmann-fold motif unambiguously identifies the enzyme as an NAD(P)-dependent oxidoreductase, making A (phosphorylase), B (radical SAM), and C (methyltransferase) clearly incompatible. No other option is defensible given the sequence features."
  },
  "important_caveats": [
    "The UniProt annotation for E9Q3D4 is based on similarity transfer (ECO:0000250) from the human ortholog Q9BPX1, not direct experimental characterization of the mouse protein itself.",
    "The SDR family is very large and functionally diverse; identifying the specific substrate (L-fucose) among many possible SDR substrates would require more detailed knowledge. However, this is unnecessary here because D is the sole dehydrogenase option among the four choices.",
    "The protein is also annotated with alternative names including 'Hydroxysteroid 17-beta dehydrogenase 14,' reflecting its historical classification. The reannotation as L-fucose dehydrogenase is relatively recent (entry first public 2025-04-09)."
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
  "requested_accession": "E9Q3D4",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "benchmark_sequence_sha256": "656e530c86ac38dd860b870f49c25d1c6de9ec15bf60eef81798043517661097",
  "benchmark_sequence_length": 273,
  "current_status": "retrieved",
  "current_sequence_comparison": "matched",
  "current_entry_audit": {
    "entryVersion": 97,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2011-04-05",
    "sequenceVersion": 1
  },
  "current_uniprot_release": "2026_03",
  "current_record_sha256": "bd47482a576a5aceb231929788ca2f5078c56926357a52cc62412f8c497bcd3f",
  "current_source_sequence_sha256": "656e530c86ac38dd860b870f49c25d1c6de9ec15bf60eef81798043517661097",
  "current_source_sequence_length": 273,
  "historical_status": "retrieved",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "selected_historical_entry_version": 95,
  "selected_historical_version": {
    "accession": "E9Q3D4",
    "database": "Swiss-Prot",
    "entryVersion": 95,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "DHB14_MOUSE",
    "sequenceVersion": 1
  },
  "selected_historical_record_sha256": "e2e2499fa9a4008684b0b5a4af04f9fe0ed35d0a8b57fcdbdd5131ae007b3673",
  "selected_historical_source_sequence_sha256": "656e530c86ac38dd860b870f49c25d1c6de9ec15bf60eef81798043517661097",
  "selected_historical_source_sequence_length": 273,
  "latest_at_cutoff_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 95,
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E9Q3D4.json)

```json
{
  "evidence_id": "C1",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/E9Q3D4.json",
  "source_sha256": "bd47482a576a5aceb231929788ca2f5078c56926357a52cc62412f8c497bcd3f",
  "retrieved_utc": "2026-11-02T04:28:08.225634+00:00",
  "json_pointer": "/primaryAccession",
  "excerpt": "\"E9Q3D4\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E9Q3D4.json)

```json
{
  "evidence_id": "C2",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/E9Q3D4.json",
  "source_sha256": "bd47482a576a5aceb231929788ca2f5078c56926357a52cc62412f8c497bcd3f",
  "retrieved_utc": "2026-11-02T04:28:08.225634+00:00",
  "json_pointer": "/entryAudit",
  "excerpt": "{\"entryVersion\":97,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2011-04-05\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E9Q3D4.json)

```json
{
  "evidence_id": "C3",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/E9Q3D4.json",
  "source_sha256": "bd47482a576a5aceb231929788ca2f5078c56926357a52cc62412f8c497bcd3f",
  "retrieved_utc": "2026-11-02T04:28:08.225634+00:00",
  "json_pointer": "/organism",
  "excerpt": "{\"commonName\":\"Mouse\",\"lineage\":[\"Eukaryota\",\"Metazoa\",\"Chordata\",\"Craniata\",\"Vertebrata\",\"Euteleostomi\",\"Mammalia\",\"Eutheria\",\"Euarchontoglires\",\"Glires\",\"Rodentia\",\"Myomorpha\",\"Muroidea\",\"Muridae\",\"Murinae\",\"Mus\",\"Mus\"],\"scientificName\":\"Mus musculus\",\"taxonId\":10090}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E9Q3D4.json)

```json
{
  "evidence_id": "C4",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/E9Q3D4.json",
  "source_sha256": "bd47482a576a5aceb231929788ca2f5078c56926357a52cc62412f8c497bcd3f",
  "retrieved_utc": "2026-11-02T04:28:08.225634+00:00",
  "json_pointer": "/proteinDescription",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"value\":\"Hydroxysteroid 17-beta dehydrogenase 14\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9BPX1\",\"source\":\"UniProtKB\"}],\"value\":\"1.1.1.122\"}],\"fullName\":{\"value\":\"L-fucose dehydrogenase\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E9Q3D4.json)

```json
{
  "evidence_id": "C5",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/E9Q3D4.json",
  "source_sha256": "bd47482a576a5aceb231929788ca2f5078c56926357a52cc62412f8c497bcd3f",
  "retrieved_utc": "2026-11-02T04:28:08.225634+00:00",
  "json_pointer": "/comments/1",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9BPX1\",\"source\":\"UniProtKB\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:81516\"}}],\"reaction\":{\"ecNumber\":\"1.1.1.122\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9BPX1\",\"source\":\"UniProtKB\"}],\"name\":\"L-fucose + NAD(+) = L-fucono-1,5-lactone + NADH + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:81515\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:2181\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57540\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57945\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:81457\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E9Q3D4.json)

```json
{
  "evidence_id": "C6",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/E9Q3D4.json",
  "source_sha256": "bd47482a576a5aceb231929788ca2f5078c56926357a52cc62412f8c497bcd3f",
  "retrieved_utc": "2026-11-02T04:28:08.225634+00:00",
  "json_pointer": "/comments/2",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"ecNumber\":\"1.1.1.122\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9BPX1\",\"source\":\"UniProtKB\"}],\"name\":\"D-arabinose + NAD(+) = D-arabinono-1,5-lactone + NADH + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:81519\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:46994\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57540\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57945\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:194242\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E9Q3D4.json)

```json
{
  "evidence_id": "C7",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/E9Q3D4.json",
  "source_sha256": "bd47482a576a5aceb231929788ca2f5078c56926357a52cc62412f8c497bcd3f",
  "retrieved_utc": "2026-11-02T04:28:08.225634+00:00",
  "json_pointer": "/comments/3",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"ecNumber\":\"1.1.1.122\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9BPX1\",\"source\":\"UniProtKB\"}],\"name\":\"L-galactose + NAD(+) = L-galactono-1,5-lactone + NADH + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:81523\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:37619\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57540\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57945\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:182410\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E9Q3D4?format=txt&versions=95)

```json
{
  "evidence_id": "H1",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/E9Q3D4?format=txt&versions=95",
  "source_sha256": "e2e2499fa9a4008684b0b5a4af04f9fe0ed35d0a8b57fcdbdd5131ae007b3673",
  "retrieved_utc": "2026-11-02T04:28:17.926007+00:00",
  "source_locator": "lines 1-14",
  "excerpt": "ID   DHB14_MOUSE             Reviewed;         273 AA.\nAC   E9Q3D4;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   05-APR-2011, sequence version 1.\nDT   28-JAN-2026, entry version 95.\nDE   RecName: Full=L-fucose dehydrogenase;\nDE            EC=1.1.1.122 {ECO:0000250|UniProtKB:Q9BPX1};\nDE   AltName: Full=Hydroxysteroid 17-beta dehydrogenase 14;\nGN   Name=Hsd17b14 {ECO:0000312|MGI:MGI:1913315}; Synonyms=Dhrs10, retSDR3;\nOS   Mus musculus (Mouse).\nOC   Eukaryota; Metazoa; Chordata; Craniata; Vertebrata; Euteleostomi; Mammalia;\nOC   Eutheria; Euarchontoglires; Glires; Rodentia; Myomorpha; Muroidea; Muridae;\nOC   Murinae; Mus; Mus.\nOX   NCBI_TaxID=10090;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 95,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E9Q3D4?format=txt&versions=95)

```json
{
  "evidence_id": "H2",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/E9Q3D4?format=txt&versions=95",
  "source_sha256": "e2e2499fa9a4008684b0b5a4af04f9fe0ed35d0a8b57fcdbdd5131ae007b3673",
  "retrieved_utc": "2026-11-02T04:28:17.926007+00:00",
  "source_locator": "lines 6-8",
  "excerpt": "DE   RecName: Full=L-fucose dehydrogenase;\nDE            EC=1.1.1.122 {ECO:0000250|UniProtKB:Q9BPX1};\nDE   AltName: Full=Hydroxysteroid 17-beta dehydrogenase 14;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 95,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E9Q3D4?format=txt&versions=95)

```json
{
  "evidence_id": "H3",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/E9Q3D4?format=txt&versions=95",
  "source_sha256": "e2e2499fa9a4008684b0b5a4af04f9fe0ed35d0a8b57fcdbdd5131ae007b3673",
  "retrieved_utc": "2026-11-02T04:28:17.926007+00:00",
  "source_locator": "lines 34-40",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=L-fucose + NAD(+) = L-fucono-1,5-lactone + NADH + H(+);\nCC         Xref=Rhea:RHEA:81515, ChEBI:CHEBI:2181, ChEBI:CHEBI:15378,\nCC         ChEBI:CHEBI:57540, ChEBI:CHEBI:57945, ChEBI:CHEBI:81457;\nCC         EC=1.1.1.122; Evidence={ECO:0000250|UniProtKB:Q9BPX1};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:81516;\nCC         Evidence={ECO:0000250|UniProtKB:Q9BPX1};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 95,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E9Q3D4?format=txt&versions=95)

```json
{
  "evidence_id": "H4",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/E9Q3D4?format=txt&versions=95",
  "source_sha256": "e2e2499fa9a4008684b0b5a4af04f9fe0ed35d0a8b57fcdbdd5131ae007b3673",
  "retrieved_utc": "2026-11-02T04:28:17.926007+00:00",
  "source_locator": "lines 41-45",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=D-arabinose + NAD(+) = D-arabinono-1,5-lactone + NADH + H(+);\nCC         Xref=Rhea:RHEA:81519, ChEBI:CHEBI:15378, ChEBI:CHEBI:46994,\nCC         ChEBI:CHEBI:57540, ChEBI:CHEBI:57945, ChEBI:CHEBI:194242;\nCC         EC=1.1.1.122; Evidence={ECO:0000250|UniProtKB:Q9BPX1};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 95,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E9Q3D4?format=txt&versions=95)

```json
{
  "evidence_id": "H5",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/E9Q3D4?format=txt&versions=95",
  "source_sha256": "e2e2499fa9a4008684b0b5a4af04f9fe0ed35d0a8b57fcdbdd5131ae007b3673",
  "retrieved_utc": "2026-11-02T04:28:17.926007+00:00",
  "source_locator": "lines 46-50",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=L-galactose + NAD(+) = L-galactono-1,5-lactone + NADH + H(+);\nCC         Xref=Rhea:RHEA:81523, ChEBI:CHEBI:15378, ChEBI:CHEBI:37619,\nCC         ChEBI:CHEBI:57540, ChEBI:CHEBI:57945, ChEBI:CHEBI:182410;\nCC         EC=1.1.1.122; Evidence={ECO:0000250|UniProtKB:Q9BPX1};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 95,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 190. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
