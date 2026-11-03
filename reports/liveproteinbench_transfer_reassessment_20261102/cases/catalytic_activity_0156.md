# catalytic_activity_0156: before and after transfer clarification

[All 1,328 cases](../README.md) · [Method](../METHOD.md) · [Summary](../SUMMARY.md) · [Exact reviewer user message](../inputs/catalytic_activity_0156.txt)

**Task:** `catalytic_activity`  
**Author key, unchanged:** **C** — D-mannitol 1-phosphate + NAD(+) = beta-D-fructose 6-phosphate + NADH + H(+)

| Round | Reviewer | Key support | Transfer / lookup | Output usability (canonical status) |
|---|---|---|---|---|
| before | GPT-6 Luna | supported | reasoning-supported | usable output (valid_review) |
| before | Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | usable output (valid_review) |
| after | GPT-6 Luna | supported | reasoning-supported | usable output (valid_review) |
| after | Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | usable output (valid_review) |

**Usable output means format-valid review, not reasoning-supported or biologically correct.** A usable output can classify the question as reasoning-supported, lookup-dependent or uncertain. An output error is a problem with the saved model response; it does not count a defective benchmark question or wrong key. Each saved review is retained in full below. Labels from output errors are displayed as saved and excluded from label statistics. The author key and reviewer evidence were visible to reviewers; this is a review of answerability and key support, not a benchmark-solving score.

## Complete original question

```text
[Protein Sequence]
MSDMKAIHFGGGNIGRGFVAEFLHKSGYEVVFVDVMDAIINALQQNKSYTVTEVGTSETKSKTIDNYRAINSKTDEDKVVEEIATADIVTCAVGPNILKFIAPVIAKGIENRKKDSPIAVIACENAIGATDTLRKFIEEKLSDSTKSNIQDKARFANSAIDRIVPMQDENAGLNVKIEKFYEWCVESKPFLPSQPPKIEGVHFVEDLTPFIERKLFTVNTGHATAAYYGYNRGKECIHDVLQDKELNEIVRNTLKETAHLIVNKHEISEEDQNQYVEKIIKRISNPVLKDNVERVGRAPLRKLSRNERFIGPAAHLAEMGAKYDALLGGIEMCLRFQNVEGDDESFELAKILKENSSSDATEKITGLERNHTLFPAVEEVVKKVQA

[Multiple Choices]
A. L-tyrosine + reduced [NADPH--hemoprotein reductase] + O2 = L-dopa + oxidized [NADPH--hemoprotein reductase] + H2O + H(+)
B. (2R,3R,5S,6R)-6-(methyl)-2-(S-pantetheinyl)-carbapenam-3-carboxylate + AH2 + 2 S-adenosyl-L-methionine = (2R,3R,5S,6R)-6-(ethyl)-2-(S-pantetheinyl)-carbapenam-3-carboxylate + 5'-deoxyadenosine + L-methionine + A + S-adenosyl-L-homocysteine + 2 H(+)
C. D-mannitol 1-phosphate + NAD(+) = beta-D-fructose 6-phosphate + NADH + H(+)
D. vinorine + reduced [NADPH--hemoprotein reductase] + O2 = vomilenine + oxidized [NADPH--hemoprotein reductase] + H2O + H(+)
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

> The exact sequence matches a UniProt entry annotated as mannitol-1-phosphate 5-dehydrogenase with the reaction in choice C. The annotation supports the key, but its EC assignment is transferred by similarity, not shown here as direct experimental verification for this sequence.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H1](#evidence-h1), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The N-terminal glycine-rich region is consistent with a dinucleotide-binding oxidoreductase, and choice C is the only NAD(+)/NADH-dependent reaction. The alternatives instead invoke oxygen-dependent hemoprotein-reductase chemistry or SAM-dependent chemistry, for which the sequence provides no comparable signature.


**Missing item-specific fact**

> The motif does not by itself establish mannitol-1-phosphate as the substrate or prove the exact product; that specificity is supported by the reviewer-only annotation.


**Reason**

> Sequence-based cofactor and enzyme-class clues meaningfully distinguish the listed reaction classes, although they do not independently establish the precise substrate conversion.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the choices, only C matches an NAD(+)-dependent dehydrogenase reaction.


### Important caveats

- The sequence match is exact, but the supplied database annotation assigns EC 1.1.1.17 by similarity; the excerpts do not establish direct experimental measurement of this sequence's activity.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal glycine-rich region is consistent with a dinucleotide-binding oxidoreductase, and choice C is the only NAD(+)/NADH-dependent reaction. The alternatives instead invoke oxygen-dependent hemoprotein-reductase chemistry or SAM-dependent chemistry, for which the sequence provides no comparable signature.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The motif does not by itself establish mannitol-1-phosphate as the substrate or prove the exact product; that specificity is supported by the reviewer-only annotation.",
    "reason": "Sequence-based cofactor and enzyme-class clues meaningfully distinguish the listed reaction classes, although they do not independently establish the precise substrate conversion."
  },
  "case_id": "catalytic_activity_0156",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H1",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry annotated as mannitol-1-phosphate 5-dehydrogenase with the reaction in choice C. The annotation supports the key, but its EC assignment is transferred by similarity, not shown here as direct experimental verification for this sequence."
  },
  "important_caveats": [
    "The sequence match is exact, but the supplied database annotation assigns EC 1.1.1.17 by similarity; the excerpts do not establish direct experimental measurement of this sequence's activity."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the choices, only C matches an NAD(+)-dependent dehydrogenase reaction."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0156",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry annotated as mannitol-1-phosphate 5-dehydrogenase with the reaction in choice C. The annotation supports the key, but its EC assignment is transferred by similarity, not shown here as direct experimental verification for this sequence.",
    "evidence_ids": ["C1", "C4", "C5", "H1", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The N-terminal glycine-rich region is consistent with a dinucleotide-binding oxidoreductase, and choice C is the only NAD(+)/NADH-dependent reaction. The alternatives instead invoke oxygen-dependent hemoprotein-reductase chemistry or SAM-dependent chemistry, for which the sequence provides no comparable signature.",
    "missing_item_specific_fact": "The motif does not by itself establish mannitol-1-phosphate as the substrate or prove the exact product; that specificity is supported by the reviewer-only annotation.",
    "reason": "Sequence-based cofactor and enzyme-class clues meaningfully distinguish the listed reaction classes, although they do not independently establish the precise substrate conversion."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the choices, only C matches an NAD(+)-dependent dehydrogenase reaction."
  },
  "important_caveats": [
    "The sequence match is exact, but the supplied database annotation assigns EC 1.1.1.17 by similarity; the excerpts do not establish direct experimental measurement of this sequence's activity."
  ]
}
```

</details>

## Before: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The supplied sequence (386 AA) matches UniProt entry A0A223HDH4 (MPDH_AURME), which is annotated as Mannitol-1-phosphate 5-dehydrogenase (EC 1.1.1.17). The catalytic activity annotation explicitly states: D-mannitol 1-phosphate + NAD(+) = beta-D-fructose 6-phosphate + NADH + H(+), matching Choice C verbatim. The EC assignment carries evidence code ECO:0000250 (similarity to Q4X1A4), but the entry also cites PubMed 32003433 for FUNCTION and DISRUPTION PHENOTYPE, providing experimental support for the enzymatic role in Aureobasidium melanogenum. The sequence match is exact (sha256 confirmed) across both current and historical (v15) snapshots.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> Partial elimination is possible: the sequence lacks the canonical P450 heme-binding motif (FxxGxxxCxG), arguing against Choices A and D (both cytochrome P450 monooxygenases), and lacks the radical SAM CxxxCxxC motif, arguing against Choice B. A Rossmann-like GxGxxG pattern (GGGNIGRGF) near the N-terminus is consistent with NAD-binding dehydrogenases. However, this only narrows the class to 'NAD-dependent dehydrogenase'—it does not identify the specific substrate as mannitol-1-phosphate rather than glucose-6-phosphate, lactate, sorbitol, or hundreds of other possible substrates.


**Missing item-specific fact**

> The specific substrate identity (mannitol-1-phosphate vs. other sugar-phosphate or alcohol substrates) cannot be determined from the 386-residue sequence by general biological reasoning alone. Identification requires either database lookup of this exact protein or memorization of the A0A223HDH4 / MPDH_AURME annotation.


**Reason**

> While negative evidence (absence of P450 and radical SAM motifs) provides some reasoning-based elimination of three choices, the positive identification of the specific catalytic reaction (mannitol-1-phosphate oxidation) from a bare amino-acid sequence demands item-specific external knowledge. No general sequence heuristic distinguishes mannitol-1-phosphate 5-dehydrogenase from other NAD-dependent sugar-phosphate dehydrogenases.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Choices A and D are P450 reactions, B is a radical SAM reaction; all three are reasonably excluded by absence of their diagnostic motifs. Among the four options, C is the only NAD-dependent dehydrogenase reaction, making it the sole remaining candidate after elimination. No genuine ambiguity among the four choices exists given the sequence.


### Important caveats

- The EC assignment for A0A223HDH4 is by similarity (ECO:0000250 to Q4X1A4), not direct in-vitro characterization of this specific protein; however, a separate PubMed reference (32003433) provides genetic/experimental evidence for the function in the organism.
- The reviewer-only accession was inferred from dataset metadata and was absent from the evaluated model's input.
- The elimination of P450 and radical SAM options by motif absence is a valid but coarse-grained reasoning step; it does not constitute positive identification of the specific substrate.
- The historical entry (v15) was first released in January 2026; the author's construction date is unknown, so the annotation may or may not have been available when the benchmark was assembled.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Partial elimination is possible: the sequence lacks the canonical P450 heme-binding motif (FxxGxxxCxG), arguing against Choices A and D (both cytochrome P450 monooxygenases), and lacks the radical SAM CxxxCxxC motif, arguing against Choice B. A Rossmann-like GxGxxG pattern (GGGNIGRGF) near the N-terminus is consistent with NAD-binding dehydrogenases. However, this only narrows the class to 'NAD-dependent dehydrogenase'—it does not identify the specific substrate as mannitol-1-phosphate rather than glucose-6-phosphate, lactate, sorbitol, or hundreds of other possible substrates.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific substrate identity (mannitol-1-phosphate vs. other sugar-phosphate or alcohol substrates) cannot be determined from the 386-residue sequence by general biological reasoning alone. Identification requires either database lookup of this exact protein or memorization of the A0A223HDH4 / MPDH_AURME annotation.",
    "reason": "While negative evidence (absence of P450 and radical SAM motifs) provides some reasoning-based elimination of three choices, the positive identification of the specific catalytic reaction (mannitol-1-phosphate oxidation) from a bare amino-acid sequence demands item-specific external knowledge. No general sequence heuristic distinguishes mannitol-1-phosphate 5-dehydrogenase from other NAD-dependent sugar-phosphate dehydrogenases."
  },
  "case_id": "catalytic_activity_0156",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "H1",
      "H2",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence (386 AA) matches UniProt entry A0A223HDH4 (MPDH_AURME), which is annotated as Mannitol-1-phosphate 5-dehydrogenase (EC 1.1.1.17). The catalytic activity annotation explicitly states: D-mannitol 1-phosphate + NAD(+) = beta-D-fructose 6-phosphate + NADH + H(+), matching Choice C verbatim. The EC assignment carries evidence code ECO:0000250 (similarity to Q4X1A4), but the entry also cites PubMed 32003433 for FUNCTION and DISRUPTION PHENOTYPE, providing experimental support for the enzymatic role in Aureobasidium melanogenum. The sequence match is exact (sha256 confirmed) across both current and historical (v15) snapshots."
  },
  "important_caveats": [
    "The EC assignment for A0A223HDH4 is by similarity (ECO:0000250 to Q4X1A4), not direct in-vitro characterization of this specific protein; however, a separate PubMed reference (32003433) provides genetic/experimental evidence for the function in the organism.",
    "The reviewer-only accession was inferred from dataset metadata and was absent from the evaluated model's input.",
    "The elimination of P450 and radical SAM options by motif absence is a valid but coarse-grained reasoning step; it does not constitute positive identification of the specific substrate.",
    "The historical entry (v15) was first released in January 2026; the author's construction date is unknown, so the annotation may or may not have been available when the benchmark was assembled."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Choices A and D are P450 reactions, B is a radical SAM reaction; all three are reasonably excluded by absence of their diagnostic motifs. Among the four options, C is the only NAD-dependent dehydrogenase reaction, making it the sole remaining candidate after elimination. No genuine ambiguity among the four choices exists given the sequence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0156",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence (386 AA) matches UniProt entry A0A223HDH4 (MPDH_AURME), which is annotated as Mannitol-1-phosphate 5-dehydrogenase (EC 1.1.1.17). The catalytic activity annotation explicitly states: D-mannitol 1-phosphate + NAD(+) = beta-D-fructose 6-phosphate + NADH + H(+), matching Choice C verbatim. The EC assignment carries evidence code ECO:0000250 (similarity to Q4X1A4), but the entry also cites PubMed 32003433 for FUNCTION and DISRUPTION PHENOTYPE, providing experimental support for the enzymatic role in Aureobasidium melanogenum. The sequence match is exact (sha256 confirmed) across both current and historical (v15) snapshots.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H1", "H2", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "Partial elimination is possible: the sequence lacks the canonical P450 heme-binding motif (FxxGxxxCxG), arguing against Choices A and D (both cytochrome P450 monooxygenases), and lacks the radical SAM CxxxCxxC motif, arguing against Choice B. A Rossmann-like GxGxxG pattern (GGGNIGRGF) near the N-terminus is consistent with NAD-binding dehydrogenases. However, this only narrows the class to 'NAD-dependent dehydrogenase'—it does not identify the specific substrate as mannitol-1-phosphate rather than glucose-6-phosphate, lactate, sorbitol, or hundreds of other possible substrates.",
    "missing_item_specific_fact": "The specific substrate identity (mannitol-1-phosphate vs. other sugar-phosphate or alcohol substrates) cannot be determined from the 386-residue sequence by general biological reasoning alone. Identification requires either database lookup of this exact protein or memorization of the A0A223HDH4 / MPDH_AURME annotation.",
    "reason": "While negative evidence (absence of P450 and radical SAM motifs) provides some reasoning-based elimination of three choices, the positive identification of the specific catalytic reaction (mannitol-1-phosphate oxidation) from a bare amino-acid sequence demands item-specific external knowledge. No general sequence heuristic distinguishes mannitol-1-phosphate 5-dehydrogenase from other NAD-dependent sugar-phosphate dehydrogenases."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Choices A and D are P450 reactions, B is a radical SAM reaction; all three are reasonably excluded by absence of their diagnostic motifs. Among the four options, C is the only NAD-dependent dehydrogenase reaction, making it the sole remaining candidate after elimination. No genuine ambiguity among the four choices exists given the sequence."
  },
  "important_caveats": [
    "The EC assignment for A0A223HDH4 is by similarity (ECO:0000250 to Q4X1A4), not direct in-vitro characterization of this specific protein; however, a separate PubMed reference (32003433) provides genetic/experimental evidence for the function in the organism.",
    "The reviewer-only accession was inferred from dataset metadata and was absent from the evaluated model's input.",
    "The elimination of P450 and radical SAM options by motif absence is a valid but coarse-grained reasoning step; it does not constitute positive identification of the specific substrate.",
    "The historical entry (v15) was first released in January 2026; the author's construction date is unknown, so the annotation may or may not have been available when the benchmark was assembled."
  ]
}
```

</details>

## After: GPT-6 Luna

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The source annotation for the exact matched sequence gives the reaction in choice C. Its EC-number evidence is transferred by similarity (ECO:0000250), so this supports the key as an annotation but does not establish direct experimental validation for this protein.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4), [C4](#evidence-c4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence begins with a glycine-rich motif characteristic of Rossmann-like dinucleotide-binding enzymes, and its overall length and sequence are consistent with a soluble dehydrogenase. That makes the NAD(+)/NADH reaction in C a credible family-level inference. By contrast, A and D are oxygen-dependent monooxygenase reactions using a hemoprotein reductase, and B is a complex methylation reaction involving S-adenosylmethionine and a carbapenam substrate.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The sequence and choices permit a meaningful inference toward a dinucleotide-dependent dehydrogenase rather than the oxygen-dependent or SAM-dependent alternatives. The sequence alone does not prove the precise substrate specificity, but the alternatives make the family-level distinction relevant and sufficiently discriminating.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The alternatives describe distinct reaction classes; the sequence supports the dehydrogenase choice over the listed alternatives.


### Important caveats

- The source annotation matches the supplied sequence, but its cited EC evidence is transferred by similarity rather than identified here as direct experimental evidence for this exact protein.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence begins with a glycine-rich motif characteristic of Rossmann-like dinucleotide-binding enzymes, and its overall length and sequence are consistent with a soluble dehydrogenase. That makes the NAD(+)/NADH reaction in C a credible family-level inference. By contrast, A and D are oxygen-dependent monooxygenase reactions using a hemoprotein reductase, and B is a complex methylation reaction involving S-adenosylmethionine and a carbapenam substrate.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The sequence and choices permit a meaningful inference toward a dinucleotide-dependent dehydrogenase rather than the oxygen-dependent or SAM-dependent alternatives. The sequence alone does not prove the precise substrate specificity, but the alternatives make the family-level distinction relevant and sufficiently discriminating."
  },
  "case_id": "catalytic_activity_0156",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4",
      "C4"
    ],
    "judgment": "supported",
    "reason": "The source annotation for the exact matched sequence gives the reaction in choice C. Its EC-number evidence is transferred by similarity (ECO:0000250), so this supports the key as an annotation but does not establish direct experimental validation for this protein."
  },
  "important_caveats": [
    "The source annotation matches the supplied sequence, but its cited EC evidence is transferred by similarity rather than identified here as direct experimental evidence for this exact protein."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The alternatives describe distinct reaction classes; the sequence supports the dehydrogenase choice over the listed alternatives."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0156",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The source annotation for the exact matched sequence gives the reaction in choice C. Its EC-number evidence is transferred by similarity (ECO:0000250), so this supports the key as an annotation but does not establish direct experimental validation for this protein.",
    "evidence_ids": ["C5", "H4", "C4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence begins with a glycine-rich motif characteristic of Rossmann-like dinucleotide-binding enzymes, and its overall length and sequence are consistent with a soluble dehydrogenase. That makes the NAD(+)/NADH reaction in C a credible family-level inference. By contrast, A and D are oxygen-dependent monooxygenase reactions using a hemoprotein reductase, and B is a complex methylation reaction involving S-adenosylmethionine and a carbapenam substrate.",
    "missing_item_specific_fact": "",
    "reason": "The sequence and choices permit a meaningful inference toward a dinucleotide-dependent dehydrogenase rather than the oxygen-dependent or SAM-dependent alternatives. The sequence alone does not prove the precise substrate specificity, but the alternatives make the family-level distinction relevant and sufficiently discriminating."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The alternatives describe distinct reaction classes; the sequence supports the dehydrogenase choice over the listed alternatives."
  },
  "important_caveats": [
    "The source annotation matches the supplied sequence, but its cited EC evidence is transferred by similarity rather than identified here as direct experimental evidence for this exact protein."
  ]
}
```

</details>

## After: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry A0A223HDH4 (MPDH_AURME, 386 AA, exact sequence match) annotates this protein as Mannitol-1-phosphate 5-dehydrogenase (EC 1.1.1.17) with catalytic activity 'D-mannitol 1-phosphate + NAD(+) = beta-D-fructose 6-phosphate + NADH + H(+)', matching choice C exactly. The EC number is assigned via similarity (ECO:0000250 to Q4X1A4), while the protein name is supported by PubMed:32003433 (experimental genetic evidence in Aureobasidium). The annotation is computational/similarity-based for the EC assignment but backed by experimental literature for the protein identity.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H4](#evidence-h4), [H2](#evidence-h2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a canonical Rossmann-fold NAD-binding motif: GGGNIGRG (positions ~12-19, GxGxxG pattern) followed by VVFVDVMDA, which is the hallmark of NAD-dependent dehydrogenases/reductases. Choice C (mannitol-1-phosphate 5-dehydrogenase) is the only option involving NAD(+) as a direct hydride acceptor in a dehydrogenase reaction. Choices A and D describe cytochrome P450 monooxygenases, which require distinctive heme-binding motifs (FGXGXXCXXXG, FSAG in the I-helix) and use NADPH-hemoprotein reductase + O2 — none of these P450 signatures are present in the sequence. Choice B describes a radical SAM enzyme requiring a CX3CX2C Fe-S cluster-binding motif, also absent. The Rossmann fold architecture positively identifies an NAD-dependent dehydrogenase and simultaneously excludes P450 and radical SAM mechanisms, uniquely selecting C among the four offered alternatives.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The Rossmann fold NAD-binding motif is a well-known, transferable sequence signature recognized across hundreds of dehydrogenase families. Its presence, combined with the absence of P450 heme-binding motifs and radical SAM motifs, provides a concrete structural-mechanistic argument that distinguishes choice C from A, B, and D without requiring knowledge of this specific protein's database annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four choices represent mechanistically distinct enzyme classes (P450 monooxygenase ×2, radical SAM enzyme, NAD-dependent dehydrogenase). The Rossmann fold motif and absence of P450/radical SAM signatures cleanly separate C from the others.


### Important caveats

- The EC annotation is assigned by similarity (ECO:0000250) to Q4X1A4 rather than by direct experimental kinetics on this exact protein, though PubMed:32003433 provides experimental genetic evidence for the protein's role in liamocin biosynthesis in Aureobasidium.
- The Rossmann fold argument identifies the enzyme as an NAD-dependent dehydrogenase but does not by itself prove mannitol-1-phosphate as the specific substrate; however, among the four offered choices, C is the only NAD-dependent dehydrogenase, making the family-level inference sufficient for the multiple-choice format.
- The reviewer-only accession and organism identity were not available to the evaluated model; the argument relies solely on sequence motifs visible in the input.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a canonical Rossmann-fold NAD-binding motif: GGGNIGRG (positions ~12-19, GxGxxG pattern) followed by VVFVDVMDA, which is the hallmark of NAD-dependent dehydrogenases/reductases. Choice C (mannitol-1-phosphate 5-dehydrogenase) is the only option involving NAD(+) as a direct hydride acceptor in a dehydrogenase reaction. Choices A and D describe cytochrome P450 monooxygenases, which require distinctive heme-binding motifs (FGXGXXCXXXG, FSAG in the I-helix) and use NADPH-hemoprotein reductase + O2 — none of these P450 signatures are present in the sequence. Choice B describes a radical SAM enzyme requiring a CX3CX2C Fe-S cluster-binding motif, also absent. The Rossmann fold architecture positively identifies an NAD-dependent dehydrogenase and simultaneously excludes P450 and radical SAM mechanisms, uniquely selecting C among the four offered alternatives.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The Rossmann fold NAD-binding motif is a well-known, transferable sequence signature recognized across hundreds of dehydrogenase families. Its presence, combined with the absence of P450 heme-binding motifs and radical SAM motifs, provides a concrete structural-mechanistic argument that distinguishes choice C from A, B, and D without requiring knowledge of this specific protein's database annotation."
  },
  "case_id": "catalytic_activity_0156",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H4",
      "H2"
    ],
    "judgment": "supported",
    "reason": "UniProt entry A0A223HDH4 (MPDH_AURME, 386 AA, exact sequence match) annotates this protein as Mannitol-1-phosphate 5-dehydrogenase (EC 1.1.1.17) with catalytic activity 'D-mannitol 1-phosphate + NAD(+) = beta-D-fructose 6-phosphate + NADH + H(+)', matching choice C exactly. The EC number is assigned via similarity (ECO:0000250 to Q4X1A4), while the protein name is supported by PubMed:32003433 (experimental genetic evidence in Aureobasidium). The annotation is computational/similarity-based for the EC assignment but backed by experimental literature for the protein identity."
  },
  "important_caveats": [
    "The EC annotation is assigned by similarity (ECO:0000250) to Q4X1A4 rather than by direct experimental kinetics on this exact protein, though PubMed:32003433 provides experimental genetic evidence for the protein's role in liamocin biosynthesis in Aureobasidium.",
    "The Rossmann fold argument identifies the enzyme as an NAD-dependent dehydrogenase but does not by itself prove mannitol-1-phosphate as the specific substrate; however, among the four offered choices, C is the only NAD-dependent dehydrogenase, making the family-level inference sufficient for the multiple-choice format.",
    "The reviewer-only accession and organism identity were not available to the evaluated model; the argument relies solely on sequence motifs visible in the input."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices represent mechanistically distinct enzyme classes (P450 monooxygenase ×2, radical SAM enzyme, NAD-dependent dehydrogenase). The Rossmann fold motif and absence of P450/radical SAM signatures cleanly separate C from the others."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0156",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry A0A223HDH4 (MPDH_AURME, 386 AA, exact sequence match) annotates this protein as Mannitol-1-phosphate 5-dehydrogenase (EC 1.1.1.17) with catalytic activity 'D-mannitol 1-phosphate + NAD(+) = beta-D-fructose 6-phosphate + NADH + H(+)', matching choice C exactly. The EC number is assigned via similarity (ECO:0000250 to Q4X1A4), while the protein name is supported by PubMed:32003433 (experimental genetic evidence in Aureobasidium). The annotation is computational/similarity-based for the EC assignment but backed by experimental literature for the protein identity.",
    "evidence_ids": ["C4", "C5", "H4", "H2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a canonical Rossmann-fold NAD-binding motif: GGGNIGRG (positions ~12-19, GxGxxG pattern) followed by VVFVDVMDA, which is the hallmark of NAD-dependent dehydrogenases/reductases. Choice C (mannitol-1-phosphate 5-dehydrogenase) is the only option involving NAD(+) as a direct hydride acceptor in a dehydrogenase reaction. Choices A and D describe cytochrome P450 monooxygenases, which require distinctive heme-binding motifs (FGXGXXCXXXG, FSAG in the I-helix) and use NADPH-hemoprotein reductase + O2 — none of these P450 signatures are present in the sequence. Choice B describes a radical SAM enzyme requiring a CX3CX2C Fe-S cluster-binding motif, also absent. The Rossmann fold architecture positively identifies an NAD-dependent dehydrogenase and simultaneously excludes P450 and radical SAM mechanisms, uniquely selecting C among the four offered alternatives.",
    "missing_item_specific_fact": "",
    "reason": "The Rossmann fold NAD-binding motif is a well-known, transferable sequence signature recognized across hundreds of dehydrogenase families. Its presence, combined with the absence of P450 heme-binding motifs and radical SAM motifs, provides a concrete structural-mechanistic argument that distinguishes choice C from A, B, and D without requiring knowledge of this specific protein's database annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices represent mechanistically distinct enzyme classes (P450 monooxygenase ×2, radical SAM enzyme, NAD-dependent dehydrogenase). The Rossmann fold motif and absence of P450/radical SAM signatures cleanly separate C from the others."
  },
  "important_caveats": [
    "The EC annotation is assigned by similarity (ECO:0000250) to Q4X1A4 rather than by direct experimental kinetics on this exact protein, though PubMed:32003433 provides experimental genetic evidence for the protein's role in liamocin biosynthesis in Aureobasidium.",
    "The Rossmann fold argument identifies the enzyme as an NAD-dependent dehydrogenase but does not by itself prove mannitol-1-phosphate as the specific substrate; however, among the four offered choices, C is the only NAD-dependent dehydrogenase, making the family-level inference sufficient for the multiple-choice format.",
    "The reviewer-only accession and organism identity were not available to the evaluated model; the argument relies solely on sequence motifs visible in the input."
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
  "requested_accession": "A0A223HDH4",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "benchmark_sequence_sha256": "0560835617463254f8bb4727e9aa3fdfd4d7e2ebec6b8a2c79e57b4d0f7ae518",
  "benchmark_sequence_length": 386,
  "current_status": "retrieved",
  "current_sequence_comparison": "matched",
  "current_entry_audit": {
    "entryVersion": 16,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2017-10-25",
    "sequenceVersion": 1
  },
  "current_uniprot_release": "2026_03",
  "current_record_sha256": "7c8df05c75e909c885087b874bfd4270859d408d933f4695e68a2b558bd8ea6e",
  "current_source_sequence_sha256": "0560835617463254f8bb4727e9aa3fdfd4d7e2ebec6b8a2c79e57b4d0f7ae518",
  "current_source_sequence_length": 386,
  "historical_status": "retrieved",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "selected_historical_entry_version": 15,
  "selected_historical_version": {
    "accession": "A0A223HDH4",
    "database": "Swiss-Prot",
    "entryVersion": 15,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_02/2026_02",
    "lastReleaseDate": "10-Jun-2026",
    "name": "MPDH_AURME",
    "sequenceVersion": 1
  },
  "selected_historical_record_sha256": "cdb64e60ab7ff06bc6c58dba44ce5f9a0a74986e515a667043ef14c65f549ac0",
  "selected_historical_source_sequence_sha256": "0560835617463254f8bb4727e9aa3fdfd4d7e2ebec6b8a2c79e57b4d0f7ae518",
  "selected_historical_source_sequence_length": 386,
  "latest_at_cutoff_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 15,
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A223HDH4.json)

```json
{
  "evidence_id": "C1",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A223HDH4.json",
  "source_sha256": "7c8df05c75e909c885087b874bfd4270859d408d933f4695e68a2b558bd8ea6e",
  "retrieved_utc": "2026-11-02T04:24:43.559987+00:00",
  "json_pointer": "/primaryAccession",
  "excerpt": "\"A0A223HDH4\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A223HDH4.json)

```json
{
  "evidence_id": "C2",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A223HDH4.json",
  "source_sha256": "7c8df05c75e909c885087b874bfd4270859d408d933f4695e68a2b558bd8ea6e",
  "retrieved_utc": "2026-11-02T04:24:43.559987+00:00",
  "json_pointer": "/entryAudit",
  "excerpt": "{\"entryVersion\":16,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2017-10-25\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A223HDH4.json)

```json
{
  "evidence_id": "C3",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A223HDH4.json",
  "source_sha256": "7c8df05c75e909c885087b874bfd4270859d408d933f4695e68a2b558bd8ea6e",
  "retrieved_utc": "2026-11-02T04:24:43.559987+00:00",
  "json_pointer": "/organism",
  "excerpt": "{\"commonName\":\"Aureobasidium pullulans var. melanogenum\",\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Dothideomycetes\",\"Dothideomycetidae\",\"Dothideales\",\"Saccotheciaceae\",\"Aureobasidium\"],\"scientificName\":\"Aureobasidium melanogenum\",\"taxonId\":46634}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A223HDH4.json)

```json
{
  "evidence_id": "C4",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A223HDH4.json",
  "source_sha256": "7c8df05c75e909c885087b874bfd4270859d408d933f4695e68a2b558bd8ea6e",
  "retrieved_utc": "2026-11-02T04:24:43.559987+00:00",
  "json_pointer": "/proteinDescription",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q4X1A4\",\"source\":\"UniProtKB\"}],\"value\":\"1.1.1.17\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"32003433\",\"source\":\"PubMed\"}],\"value\":\"Mannitol-1-phosphate 5-dehydrogenase\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"32003433\",\"source\":\"PubMed\"}],\"value\":\"MPDH\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A223HDH4.json)

```json
{
  "evidence_id": "C5",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A223HDH4.json",
  "source_sha256": "7c8df05c75e909c885087b874bfd4270859d408d933f4695e68a2b558bd8ea6e",
  "retrieved_utc": "2026-11-02T04:24:43.559987+00:00",
  "json_pointer": "/comments/1",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"ecNumber\":\"1.1.1.17\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q4X1A4\",\"source\":\"UniProtKB\"}],\"name\":\"D-mannitol 1-phosphate + NAD(+) = beta-D-fructose 6-phosphate + NADH + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:19661\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57540\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57634\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57945\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:61381\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A223HDH4.json)

```json
{
  "evidence_id": "C6",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A223HDH4.json",
  "source_sha256": "7c8df05c75e909c885087b874bfd4270859d408d933f4695e68a2b558bd8ea6e",
  "retrieved_utc": "2026-11-02T04:24:43.559987+00:00",
  "json_pointer": "/references/3",
  "excerpt": "{\"citation\":{\"authors\":[\"Xue S.J.\",\"Liu G.L.\",\"Chi Z.\",\"Gao Z.C.\",\"Hu Z.\",\"Chi Z.M.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"32003433\"},{\"database\":\"DOI\",\"id\":\"10.1042/bcj20190922\"}],\"citationType\":\"journal article\",\"firstPage\":\"887\",\"id\":\"32003433\",\"journal\":\"Biochem. J.\",\"lastPage\":\"903\",\"publicationDate\":\"2020\",\"title\":\"Genetic evidences for the core biosynthesis pathway, regulation, transport and secretion of liamocins in yeast-like fungal cells.\",\"volume\":\"477\"},\"referenceNumber\":4,\"referencePositions\":[\"FUNCTION\",\"DISRUPTION PHENOTYPE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A223HDH4?format=txt&versions=15)

```json
{
  "evidence_id": "H1",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A223HDH4?format=txt&versions=15",
  "source_sha256": "cdb64e60ab7ff06bc6c58dba44ce5f9a0a74986e515a667043ef14c65f549ac0",
  "retrieved_utc": "2026-11-02T04:24:46.025296+00:00",
  "source_locator": "lines 1-12",
  "excerpt": "ID   MPDH_AURME              Reviewed;         386 AA.\nAC   A0A223HDH4;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   25-OCT-2017, sequence version 1.\nDT   28-JAN-2026, entry version 15.\nDE   RecName: Full=Mannitol-1-phosphate 5-dehydrogenase {ECO:0000303|PubMed:32003433};\nDE            Short=MPDH {ECO:0000303|PubMed:32003433};\nDE            EC=1.1.1.17 {ECO:0000250|UniProtKB:Q4X1A4};\nOS   Aureobasidium melanogenum (Aureobasidium pullulans var. melanogenum).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Dothideomycetes;\nOC   Dothideomycetidae; Dothideales; Saccotheciaceae; Aureobasidium.\nOX   NCBI_TaxID=46634;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 15,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A223HDH4?format=txt&versions=15)

```json
{
  "evidence_id": "H2",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A223HDH4?format=txt&versions=15",
  "source_sha256": "cdb64e60ab7ff06bc6c58dba44ce5f9a0a74986e515a667043ef14c65f549ac0",
  "retrieved_utc": "2026-11-02T04:24:46.025296+00:00",
  "source_locator": "lines 6-8",
  "excerpt": "DE   RecName: Full=Mannitol-1-phosphate 5-dehydrogenase {ECO:0000303|PubMed:32003433};\nDE            Short=MPDH {ECO:0000303|PubMed:32003433};\nDE            EC=1.1.1.17 {ECO:0000250|UniProtKB:Q4X1A4};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 15,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A223HDH4?format=txt&versions=15)

```json
{
  "evidence_id": "H3",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A223HDH4?format=txt&versions=15",
  "source_sha256": "cdb64e60ab7ff06bc6c58dba44ce5f9a0a74986e515a667043ef14c65f549ac0",
  "retrieved_utc": "2026-11-02T04:24:46.025296+00:00",
  "source_locator": "lines 31-37",
  "excerpt": "RN   [4]\nRP   FUNCTION, AND DISRUPTION PHENOTYPE.\nRX   PubMed=32003433; DOI=10.1042/bcj20190922;\nRA   Xue S.J., Liu G.L., Chi Z., Gao Z.C., Hu Z., Chi Z.M.;\nRT   \"Genetic evidences for the core biosynthesis pathway, regulation, transport\nRT   and secretion of liamocins in yeast-like fungal cells.\";\nRL   Biochem. J. 477:887-903(2020).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 15,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A223HDH4?format=txt&versions=15)

```json
{
  "evidence_id": "H4",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A223HDH4?format=txt&versions=15",
  "source_sha256": "cdb64e60ab7ff06bc6c58dba44ce5f9a0a74986e515a667043ef14c65f549ac0",
  "retrieved_utc": "2026-11-02T04:24:46.025296+00:00",
  "source_locator": "lines 53-58",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=D-mannitol 1-phosphate + NAD(+) = beta-D-fructose 6-phosphate\nCC         + NADH + H(+); Xref=Rhea:RHEA:19661, ChEBI:CHEBI:15378,\nCC         ChEBI:CHEBI:57540, ChEBI:CHEBI:57634, ChEBI:CHEBI:57945,\nCC         ChEBI:CHEBI:61381; EC=1.1.1.17;\nCC         Evidence={ECO:0000250|UniProtKB:Q4X1A4};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 15,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 156. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
