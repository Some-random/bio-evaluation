# temperature_0017: before and after transfer clarification

[All 1,328 cases](../README.md) · [Method](../METHOD.md) · [Summary](../SUMMARY.md) · [Exact reviewer user message](../inputs/temperature_0017.txt)

**Task:** `temperature`  
**Author key, unchanged:** **C** — 90

| Round | Reviewer | Key support | Transfer / lookup | Output usability (canonical status) |
|---|---|---|---|---|
| before | GPT-6 Luna | supported | lookup-dependent | usable output (valid_review) |
| before | Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | output error (invalid_review) |
| after | GPT-6 Luna | supported | lookup-dependent | usable output (valid_review) |
| after | Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | usable output (valid_review) |

**Usable output means format-valid review, not reasoning-supported or biologically correct.** A usable output can classify the question as reasoning-supported, lookup-dependent or uncertain. An output error is a problem with the saved model response; it does not count a defective benchmark question or wrong key. Each saved review is retained in full below. Labels from output errors are displayed as saved and excluded from label statistics. The author key and reviewer evidence were visible to reviewers; this is a review of answerability and key support, not a benchmark-solving score.

## Complete original question

```text
[Protein Sequence]
MLNDYLQWEKFILRGVEFPTRYRVDGDEVEITPSSRLYVSGMGGSGVVGDLIRDFSIVWNWDVEVTVVKDYFLRARDGLLIAVSYSGNTVETLYSVEYAKKRRIPTVAITTGGKLAQMGVPTIIIPKASAPRAALPQMLTAALHVVRKVYGIPIEIPEALEPPNDPLIHKLMEDFQKRPTIVAPETMRGVAYRVKNEFNENAKIEPSVEILPEAHHNWIEGSERPIVALTSPHIPREHQERVKATLEILGGTLYVVEMSTRGVLTFLREVGVASIKLAESRGVNPLATPRIEALKRRLQ

[Multiple Choices]
A. 25
B. 41
C. 90
D. 59
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Protein Thermal Adaptation Prediction, which is to predict the thermal adaptation category of a protein. This relates to the optimal temperature range in which the protein is stable and functional (e.g., cold-adapted, moderate temperature-adapted, or heat-adapted). This property is encoded by subtle patterns in the amino acid sequence that affect the protein's structural stability, such as amino acid composition and the potential for internal bonds. Based on the provided sequence, you must classify the protein into its most likely thermal category.. The inputs provided by the user for this task include:

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

> The exact 299-aa sequence matches the UniProt entry, which reports an optimum temperature of 90°C for phosphoglucose isomerase activity, with experimental evidence attributed to PubMed 39208883. This supports choice C, though the primary paper was not independently reviewed here.

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence alone does not provide a defensible way to distinguish an exact optimum of 90°C from the other listed temperatures. General sequence-based thermal tendencies would not establish this particular measured value.


**Missing item-specific fact**

> The protein-specific experimental temperature optimum (reported as 90°C), or an external identification of the protein and its associated measurement.


**Reason**

> The protein identity, organism, and temperature measurement are absent from the evaluated input. Recognizing or looking up this sequence could supply the answer, but that is item-specific lookup rather than reasoning from the provided information.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The system wording describes thermal categories, but the choices are numeric temperatures. Interpreting them as candidate optimum temperatures, the cited evidence distinguishes 90°C.


### Important caveats

- The reported optimum is specifically for phosphoglucose isomerase activity, not an unrestricted measure of stability or thermal category.
- The source sequence match is exact, including in the checked historical entry; the author's exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence alone does not provide a defensible way to distinguish an exact optimum of 90°C from the other listed temperatures. General sequence-based thermal tendencies would not establish this particular measured value.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific experimental temperature optimum (reported as 90°C), or an external identification of the protein and its associated measurement.",
    "reason": "The protein identity, organism, and temperature measurement are absent from the evaluated input. Recognizing or looking up this sequence could supply the answer, but that is item-specific lookup rather than reasoning from the provided information."
  },
  "case_id": "temperature_0017",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The exact 299-aa sequence matches the UniProt entry, which reports an optimum temperature of 90°C for phosphoglucose isomerase activity, with experimental evidence attributed to PubMed 39208883. This supports choice C, though the primary paper was not independently reviewed here."
  },
  "important_caveats": [
    "The reported optimum is specifically for phosphoglucose isomerase activity, not an unrestricted measure of stability or thermal category.",
    "The source sequence match is exact, including in the checked historical entry; the author's exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The system wording describes thermal categories, but the choices are numeric temperatures. Interpreting them as candidate optimum temperatures, the cited evidence distinguishes 90°C."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "temperature_0017",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact 299-aa sequence matches the UniProt entry, which reports an optimum temperature of 90°C for phosphoglucose isomerase activity, with experimental evidence attributed to PubMed 39208883. This supports choice C, though the primary paper was not independently reviewed here.",
    "evidence_ids": ["C1", "C5", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence alone does not provide a defensible way to distinguish an exact optimum of 90°C from the other listed temperatures. General sequence-based thermal tendencies would not establish this particular measured value.",
    "missing_item_specific_fact": "The protein-specific experimental temperature optimum (reported as 90°C), or an external identification of the protein and its associated measurement.",
    "reason": "The protein identity, organism, and temperature measurement are absent from the evaluated input. Recognizing or looking up this sequence could supply the answer, but that is item-specific lookup rather than reasoning from the provided information."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The system wording describes thermal categories, but the choices are numeric temperatures. Interpreting them as candidate optimum temperatures, the cited evidence distinguishes 90°C."
  },
  "important_caveats": [
    "The reported optimum is specifically for phosphoglucose isomerase activity, not an unrestricted measure of stability or thermal category.",
    "The source sequence match is exact, including in the checked historical entry; the author's exact source snapshot is unknown."
  ]
}
```

</details>

## Before: Qwen3.8-Flash-Next-NVFP4

**Output usability:** output error.
**Canonical saved status:** `invalid_review`.

**This saved response has an output error and is not a usable structured review.** Any labels below remain the original saved values; they are excluded from label distributions and agreement. This output status does not judge the benchmark question, author key or biological correctness. No field or option ID has been repaired.

**Validation errors:** `question_ambiguity:invalid_option_ids`.

### Expected-answer support: supported

> UniProt entry A3MTR6 (PGMI_PYRCJ) from Pyrobaculum calidifontis explicitly annotates: 'Optimum temperature is 90 degrees Celsius (for phosphoglucose isomerase activity)' with experimental evidence code ECO:0000269 from PubMed:39208883 (Maqsood et al., 2024). The sequence matches perfectly (SHA256 identical, 299 AA). The 90°C value is an experimentally determined optimum, not a computational prediction.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3), [C1](#evidence-c1), [C3](#evidence-c3), [C4](#evidence-c4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence shows elevated charged-residue content (K, E, R, D) and patterns consistent with thermophilic salt-bridge networks, which could narrow the answer away from 25°C (mesophilic) and 41°C (moderate thermophilic). However, distinguishing 90°C (hyperthermophilic) from 59°C (thermophilic) requires knowing the organism is Pyrobaculum calidifontis, a hyperthermophilic archaeon growing at ~90°C, or having access to the specific experimental measurement. General sequence-composition heuristics (charged residue ratio, proline content, loop length) can indicate 'thermophilic' broadly but cannot reliably separate 59 from 90 without organism context.


**Missing item-specific fact**

> The organism identity (Pyrobaculum calidifontis, a hyperthermophilic archaeon) or the experimentally determined optimum temperature of 90°C from PubMed:39208883. Without knowing the source organism is a hyperthermophile, the sequence alone does not provide a general-biology argument that cleanly separates 90°C from 59°C.


**Reason**

> While the sequence exhibits thermophilic signatures (high charged-residue density, salt-bridge-forming patterns), the precise distinction between 59°C and 90°C depends on organism-specific knowledge (Pyrobaculum is a known hyperthermophile) or the experimental measurement itself. This is not derivable from general biological reasoning about amino acid composition alone.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "C (90)",
  "D (59)"
]
```

> Both 90°C and 59°C represent thermophilic optima. From sequence composition alone, without organism identification, a knowledgeable model could reasonably argue for either a thermophilic (59°C) or hyperthermophilic (90°C) assignment based on the degree of charged-residue enrichment. The question does not provide organism context, making the 59 vs 90 distinction dependent on external knowledge.


### Important caveats

- The UniProt annotation of 90°C is experimentally determined (ECO:0000269, PubMed:39208883, 2024 paper), not a computational prediction.
- The organism identity (Pyrobaculum calidifontis, hyperthermophilic archaeon) is not provided in the question input, making organism-based reasoning unavailable to the evaluated model.
- The sequence was deposited in 2007 but the experimental characterization (including the 90°C optimum) was published in 2024, so the annotation is relatively recent.
- The question's framing ('subtle patterns in the amino acid sequence') implies sequence-based reasoning should suffice, but in practice the precise temperature value requires organism or experimental knowledge.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence shows elevated charged-residue content (K, E, R, D) and patterns consistent with thermophilic salt-bridge networks, which could narrow the answer away from 25°C (mesophilic) and 41°C (moderate thermophilic). However, distinguishing 90°C (hyperthermophilic) from 59°C (thermophilic) requires knowing the organism is Pyrobaculum calidifontis, a hyperthermophilic archaeon growing at ~90°C, or having access to the specific experimental measurement. General sequence-composition heuristics (charged residue ratio, proline content, loop length) can indicate 'thermophilic' broadly but cannot reliably separate 59 from 90 without organism context.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The organism identity (Pyrobaculum calidifontis, a hyperthermophilic archaeon) or the experimentally determined optimum temperature of 90°C from PubMed:39208883. Without knowing the source organism is a hyperthermophile, the sequence alone does not provide a general-biology argument that cleanly separates 90°C from 59°C.",
    "reason": "While the sequence exhibits thermophilic signatures (high charged-residue density, salt-bridge-forming patterns), the precise distinction between 59°C and 90°C depends on organism-specific knowledge (Pyrobaculum is a known hyperthermophile) or the experimental measurement itself. This is not derivable from general biological reasoning about amino acid composition alone."
  },
  "case_id": "temperature_0017",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3",
      "C1",
      "C3",
      "C4"
    ],
    "judgment": "supported",
    "reason": "UniProt entry A3MTR6 (PGMI_PYRCJ) from Pyrobaculum calidifontis explicitly annotates: 'Optimum temperature is 90 degrees Celsius (for phosphoglucose isomerase activity)' with experimental evidence code ECO:0000269 from PubMed:39208883 (Maqsood et al., 2024). The sequence matches perfectly (SHA256 identical, 299 AA). The 90°C value is an experimentally determined optimum, not a computational prediction."
  },
  "important_caveats": [
    "The UniProt annotation of 90°C is experimentally determined (ECO:0000269, PubMed:39208883, 2024 paper), not a computational prediction.",
    "The organism identity (Pyrobaculum calidifontis, hyperthermophilic archaeon) is not provided in the question input, making organism-based reasoning unavailable to the evaluated model.",
    "The sequence was deposited in 2007 but the experimental characterization (including the 90°C optimum) was published in 2024, so the annotation is relatively recent.",
    "The question's framing ('subtle patterns in the amino acid sequence') implies sequence-based reasoning should suffice, but in practice the precise temperature value requires organism or experimental knowledge."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "C (90)",
      "D (59)"
    ],
    "reason": "Both 90°C and 59°C represent thermophilic optima. From sequence composition alone, without organism identification, a knowledgeable model could reasonably argue for either a thermophilic (59°C) or hyperthermophilic (90°C) assignment based on the degree of charged-residue enrichment. The question does not provide organism context, making the 59 vs 90 distinction dependent on external knowledge."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "temperature_0017",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry A3MTR6 (PGMI_PYRCJ) from Pyrobaculum calidifontis explicitly annotates: 'Optimum temperature is 90 degrees Celsius (for phosphoglucose isomerase activity)' with experimental evidence code ECO:0000269 from PubMed:39208883 (Maqsood et al., 2024). The sequence matches perfectly (SHA256 identical, 299 AA). The 90°C value is an experimentally determined optimum, not a computational prediction.",
    "evidence_ids": ["C5", "H3", "C1", "C3", "C4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence shows elevated charged-residue content (K, E, R, D) and patterns consistent with thermophilic salt-bridge networks, which could narrow the answer away from 25°C (mesophilic) and 41°C (moderate thermophilic). However, distinguishing 90°C (hyperthermophilic) from 59°C (thermophilic) requires knowing the organism is Pyrobaculum calidifontis, a hyperthermophilic archaeon growing at ~90°C, or having access to the specific experimental measurement. General sequence-composition heuristics (charged residue ratio, proline content, loop length) can indicate 'thermophilic' broadly but cannot reliably separate 59 from 90 without organism context.",
    "missing_item_specific_fact": "The organism identity (Pyrobaculum calidifontis, a hyperthermophilic archaeon) or the experimentally determined optimum temperature of 90°C from PubMed:39208883. Without knowing the source organism is a hyperthermophile, the sequence alone does not provide a general-biology argument that cleanly separates 90°C from 59°C.",
    "reason": "While the sequence exhibits thermophilic signatures (high charged-residue density, salt-bridge-forming patterns), the precise distinction between 59°C and 90°C depends on organism-specific knowledge (Pyrobaculum is a known hyperthermophile) or the experimental measurement itself. This is not derivable from general biological reasoning about amino acid composition alone."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["C (90)", "D (59)"],
    "reason": "Both 90°C and 59°C represent thermophilic optima. From sequence composition alone, without organism identification, a knowledgeable model could reasonably argue for either a thermophilic (59°C) or hyperthermophilic (90°C) assignment based on the degree of charged-residue enrichment. The question does not provide organism context, making the 59 vs 90 distinction dependent on external knowledge."
  },
  "important_caveats": [
    "The UniProt annotation of 90°C is experimentally determined (ECO:0000269, PubMed:39208883, 2024 paper), not a computational prediction.",
    "The organism identity (Pyrobaculum calidifontis, hyperthermophilic archaeon) is not provided in the question input, making organism-based reasoning unavailable to the evaluated model.",
    "The sequence was deposited in 2007 but the experimental characterization (including the 90°C optimum) was published in 2024, so the annotation is relatively recent.",
    "The question's framing ('subtle patterns in the amino acid sequence') implies sequence-based reasoning should suffice, but in practice the precise temperature value requires organism or experimental knowledge."
  ]
}
```

</details>

## After: GPT-6 Luna

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence-matched UniProt annotation reports an optimum temperature of 90°C for phosphoglucose isomerase activity, citing experimental evidence. This supports choice C; the supplied excerpts do not independently validate the cited paper.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> Sequence composition can provide probabilistic clues about thermal adaptation, but no clear transferable feature in the supplied sequence distinguishes an optimum of 90°C from 59°C. Those choices require a more specific temperature inference than a general thermophile-versus-mesophile tendency supplies.


**Missing item-specific fact**

> The experimentally reported optimum temperature for this exact protein, or other target-specific evidence sufficient to distinguish 90°C from the other offered values.


**Reason**

> The input gives only a sequence and numeric alternatives, with no organism or assay context. A broad sequence-based estimate may be possible, but selecting the precise optimum depends on target-specific information absent from the input; recalling this protein's record would not count as transfer from related proteins.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The choices are distinct numeric temperatures, and the supplied evidence identifies one measured optimum. The input alone leaves the precise value uncertain, but no particular pair of choices is established as equally defensible.


### Important caveats

- The temperature annotation is curated and cites experimental evidence; the cited primary study was not independently reviewed here.
- The reviewer evidence reports a sequence match, but its accession and annotations were not part of the original model input.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Sequence composition can provide probabilistic clues about thermal adaptation, but no clear transferable feature in the supplied sequence distinguishes an optimum of 90°C from 59°C. Those choices require a more specific temperature inference than a general thermophile-versus-mesophile tendency supplies.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The experimentally reported optimum temperature for this exact protein, or other target-specific evidence sufficient to distinguish 90°C from the other offered values.",
    "reason": "The input gives only a sequence and numeric alternatives, with no organism or assay context. A broad sequence-based estimate may be possible, but selecting the precise optimum depends on target-specific information absent from the input; recalling this protein's record would not count as transfer from related proteins."
  },
  "case_id": "temperature_0017",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation reports an optimum temperature of 90°C for phosphoglucose isomerase activity, citing experimental evidence. This supports choice C; the supplied excerpts do not independently validate the cited paper."
  },
  "important_caveats": [
    "The temperature annotation is curated and cites experimental evidence; the cited primary study was not independently reviewed here.",
    "The reviewer evidence reports a sequence match, but its accession and annotations were not part of the original model input."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The choices are distinct numeric temperatures, and the supplied evidence identifies one measured optimum. The input alone leaves the precise value uncertain, but no particular pair of choices is established as equally defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "temperature_0017",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation reports an optimum temperature of 90°C for phosphoglucose isomerase activity, citing experimental evidence. This supports choice C; the supplied excerpts do not independently validate the cited paper.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "Sequence composition can provide probabilistic clues about thermal adaptation, but no clear transferable feature in the supplied sequence distinguishes an optimum of 90°C from 59°C. Those choices require a more specific temperature inference than a general thermophile-versus-mesophile tendency supplies.",
    "missing_item_specific_fact": "The experimentally reported optimum temperature for this exact protein, or other target-specific evidence sufficient to distinguish 90°C from the other offered values.",
    "reason": "The input gives only a sequence and numeric alternatives, with no organism or assay context. A broad sequence-based estimate may be possible, but selecting the precise optimum depends on target-specific information absent from the input; recalling this protein's record would not count as transfer from related proteins."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The choices are distinct numeric temperatures, and the supplied evidence identifies one measured optimum. The input alone leaves the precise value uncertain, but no particular pair of choices is established as equally defensible."
  },
  "important_caveats": [
    "The temperature annotation is curated and cites experimental evidence; the cited primary study was not independently reviewed here.",
    "The reviewer evidence reports a sequence match, but its accession and annotations were not part of the original model input."
  ]
}
```

</details>

## After: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A3MTR6 (sequence matched, 299 AA) records an experimentally determined optimum temperature of 90°C for phosphoglucose isomerase activity (ECO:0000269, PubMed:39208883), with thermostability half-life of ~50 min at 100°C. The sequence from Pyrobaculum calidifontis (a hyperthermophilic archaeon in Thermoproteota) is confirmed as the source. The answer of 90°C is directly supported by experimental measurement.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence exhibits extreme amino acid composition features learned from other hyperthermophilic proteins: (1) Very high Arg content (~8-10%) with a markedly elevated Arg/Lys ratio, consistent with bidentate salt-bridge networks characteristic of hyperthermophiles rather than moderate thermophiles; (2) High Glu content providing counter-charges for salt bridges; (3) Near-complete absence of thermolabile residues (no Cys, very few Gln, Asn, Ser, Thr); (4) High hydrophobic content (I, V, L) indicating a tightly packed core. The TIM-barrel 'GG' motif and overall architecture identify this as a phosphoglucose isomerase family member. The EXTREMITY of the composition bias—particularly the very high Arg/Lys ratio and near-zero thermolabile residues—distinguishes hyperthermophilic adaptation (90°C) from moderate thermophilic adaptation (59°C), where enrichment is present but less extreme. Mesophilic options (25, 41) are easily excluded by the high charged and hydrophobic content.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can recognize the PGI/TIM-barrel family from the GG motif and sequence architecture, then apply learned composition patterns from other hyperthermophilic proteins (extreme Arg enrichment, high R/K ratio, absence of Cys/Q/N, high hydrophobicity) to distinguish 90°C from 59°C. While the 90-vs-59 distinction is probabilistic rather than certain, the extremity of the composition bias provides a meaningful and defensible inference consistent with known hyperthermophile signatures.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "C",
  "D"
]
```

> Distinguishing 90°C from 59°C purely from sequence composition is inherently probabilistic. A model recognizing thermophilic composition might select 59°C (moderate thermophile) if it judges the composition as 'thermophilic but not extreme.' However, the very high Arg/Lys ratio and near-absence of all thermolabile residues tip the balance toward hyperthermophilic (90°C). The distinction is defensible but not absolute from sequence alone.


### Important caveats

- The 90°C value is an experimental measurement (PubMed:39208883), not a computational prediction; the benchmark task frames this as prediction from sequence.
- The distinction between 90°C and 59°C from sequence composition alone is probabilistic; the argument relies on the extremity of composition bias matching known hyperthermophile patterns.
- The organism (Pyrobaculum calidifontis, a hyperthermophilic archaeon) is not provided in the model input; the inference must come from sequence features alone.
- The UniProt annotation was added in 2025 (first public date 2025-02-05), so the experimental characterization is relatively recent.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence exhibits extreme amino acid composition features learned from other hyperthermophilic proteins: (1) Very high Arg content (~8-10%) with a markedly elevated Arg/Lys ratio, consistent with bidentate salt-bridge networks characteristic of hyperthermophiles rather than moderate thermophiles; (2) High Glu content providing counter-charges for salt bridges; (3) Near-complete absence of thermolabile residues (no Cys, very few Gln, Asn, Ser, Thr); (4) High hydrophobic content (I, V, L) indicating a tightly packed core. The TIM-barrel 'GG' motif and overall architecture identify this as a phosphoglucose isomerase family member. The EXTREMITY of the composition bias—particularly the very high Arg/Lys ratio and near-zero thermolabile residues—distinguishes hyperthermophilic adaptation (90°C) from moderate thermophilic adaptation (59°C), where enrichment is present but less extreme. Mesophilic options (25, 41) are easily excluded by the high charged and hydrophobic content.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can recognize the PGI/TIM-barrel family from the GG motif and sequence architecture, then apply learned composition patterns from other hyperthermophilic proteins (extreme Arg enrichment, high R/K ratio, absence of Cys/Q/N, high hydrophobicity) to distinguish 90°C from 59°C. While the 90-vs-59 distinction is probabilistic rather than certain, the extremity of the composition bias provides a meaningful and defensible inference consistent with known hyperthermophile signatures."
  },
  "case_id": "temperature_0017",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry A3MTR6 (sequence matched, 299 AA) records an experimentally determined optimum temperature of 90°C for phosphoglucose isomerase activity (ECO:0000269, PubMed:39208883), with thermostability half-life of ~50 min at 100°C. The sequence from Pyrobaculum calidifontis (a hyperthermophilic archaeon in Thermoproteota) is confirmed as the source. The answer of 90°C is directly supported by experimental measurement."
  },
  "important_caveats": [
    "The 90°C value is an experimental measurement (PubMed:39208883), not a computational prediction; the benchmark task frames this as prediction from sequence.",
    "The distinction between 90°C and 59°C from sequence composition alone is probabilistic; the argument relies on the extremity of composition bias matching known hyperthermophile patterns.",
    "The organism (Pyrobaculum calidifontis, a hyperthermophilic archaeon) is not provided in the model input; the inference must come from sequence features alone.",
    "The UniProt annotation was added in 2025 (first public date 2025-02-05), so the experimental characterization is relatively recent."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "C",
      "D"
    ],
    "reason": "Distinguishing 90°C from 59°C purely from sequence composition is inherently probabilistic. A model recognizing thermophilic composition might select 59°C (moderate thermophile) if it judges the composition as 'thermophilic but not extreme.' However, the very high Arg/Lys ratio and near-absence of all thermolabile residues tip the balance toward hyperthermophilic (90°C). The distinction is defensible but not absolute from sequence alone."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "temperature_0017",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A3MTR6 (sequence matched, 299 AA) records an experimentally determined optimum temperature of 90°C for phosphoglucose isomerase activity (ECO:0000269, PubMed:39208883), with thermostability half-life of ~50 min at 100°C. The sequence from Pyrobaculum calidifontis (a hyperthermophilic archaeon in Thermoproteota) is confirmed as the source. The answer of 90°C is directly supported by experimental measurement.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence exhibits extreme amino acid composition features learned from other hyperthermophilic proteins: (1) Very high Arg content (~8-10%) with a markedly elevated Arg/Lys ratio, consistent with bidentate salt-bridge networks characteristic of hyperthermophiles rather than moderate thermophiles; (2) High Glu content providing counter-charges for salt bridges; (3) Near-complete absence of thermolabile residues (no Cys, very few Gln, Asn, Ser, Thr); (4) High hydrophobic content (I, V, L) indicating a tightly packed core. The TIM-barrel 'GG' motif and overall architecture identify this as a phosphoglucose isomerase family member. The EXTREMITY of the composition bias—particularly the very high Arg/Lys ratio and near-zero thermolabile residues—distinguishes hyperthermophilic adaptation (90°C) from moderate thermophilic adaptation (59°C), where enrichment is present but less extreme. Mesophilic options (25, 41) are easily excluded by the high charged and hydrophobic content.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can recognize the PGI/TIM-barrel family from the GG motif and sequence architecture, then apply learned composition patterns from other hyperthermophilic proteins (extreme Arg enrichment, high R/K ratio, absence of Cys/Q/N, high hydrophobicity) to distinguish 90°C from 59°C. While the 90-vs-59 distinction is probabilistic rather than certain, the extremity of the composition bias provides a meaningful and defensible inference consistent with known hyperthermophile signatures."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["C", "D"],
    "reason": "Distinguishing 90°C from 59°C purely from sequence composition is inherently probabilistic. A model recognizing thermophilic composition might select 59°C (moderate thermophile) if it judges the composition as 'thermophilic but not extreme.' However, the very high Arg/Lys ratio and near-absence of all thermolabile residues tip the balance toward hyperthermophilic (90°C). The distinction is defensible but not absolute from sequence alone."
  },
  "important_caveats": [
    "The 90°C value is an experimental measurement (PubMed:39208883), not a computational prediction; the benchmark task frames this as prediction from sequence.",
    "The distinction between 90°C and 59°C from sequence composition alone is probabilistic; the argument relies on the extremity of composition bias matching known hyperthermophile patterns.",
    "The organism (Pyrobaculum calidifontis, a hyperthermophilic archaeon) is not provided in the model input; the inference must come from sequence features alone.",
    "The UniProt annotation was added in 2025 (first public date 2025-02-05), so the experimental characterization is relatively recent."
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
  "requested_accession": "A3MTR6",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "benchmark_sequence_sha256": "c1fe40d32c9a8ace25b121d1ae83f544553f7aee96a73eb13f919f4b78b80f91",
  "benchmark_sequence_length": 299,
  "current_status": "retrieved",
  "current_sequence_comparison": "matched",
  "current_entry_audit": {
    "entryVersion": 75,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2007-04-03",
    "sequenceVersion": 1
  },
  "current_uniprot_release": "2026_03",
  "current_record_sha256": "ab4d5d4975cecc6a04c1957b13bd9283e2ef63f3360c1922d6682cfab0917db3",
  "current_source_sequence_sha256": "c1fe40d32c9a8ace25b121d1ae83f544553f7aee96a73eb13f919f4b78b80f91",
  "current_source_sequence_length": 299,
  "historical_status": "retrieved",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "selected_historical_entry_version": 74,
  "selected_historical_version": {
    "accession": "A3MTR6",
    "database": "Swiss-Prot",
    "entryVersion": 74,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_02/2026_02",
    "lastReleaseDate": "10-Jun-2026",
    "name": "PGMI_PYRCJ",
    "sequenceVersion": 1
  },
  "selected_historical_record_sha256": "9c472af706932a5c4dae44d3e7eaa83f12d4956caae5979ddee1e4be573d0761",
  "selected_historical_source_sequence_sha256": "c1fe40d32c9a8ace25b121d1ae83f544553f7aee96a73eb13f919f4b78b80f91",
  "selected_historical_source_sequence_length": 299,
  "latest_at_cutoff_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 74,
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A3MTR6.json)

```json
{
  "evidence_id": "C1",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A3MTR6.json",
  "source_sha256": "ab4d5d4975cecc6a04c1957b13bd9283e2ef63f3360c1922d6682cfab0917db3",
  "retrieved_utc": "2026-11-02T04:26:58.786987+00:00",
  "json_pointer": "/primaryAccession",
  "excerpt": "\"A3MTR6\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A3MTR6.json)

```json
{
  "evidence_id": "C2",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A3MTR6.json",
  "source_sha256": "ab4d5d4975cecc6a04c1957b13bd9283e2ef63f3360c1922d6682cfab0917db3",
  "retrieved_utc": "2026-11-02T04:26:58.786987+00:00",
  "json_pointer": "/entryAudit",
  "excerpt": "{\"entryVersion\":75,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2007-04-03\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A3MTR6.json)

```json
{
  "evidence_id": "C3",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A3MTR6.json",
  "source_sha256": "ab4d5d4975cecc6a04c1957b13bd9283e2ef63f3360c1922d6682cfab0917db3",
  "retrieved_utc": "2026-11-02T04:26:58.786987+00:00",
  "json_pointer": "/organism",
  "excerpt": "{\"lineage\":[\"Archaea\",\"Thermoproteota\",\"Thermoprotei\",\"Thermoproteales\",\"Thermoproteaceae\",\"Pyrobaculum\"],\"scientificName\":\"Pyrobaculum calidifontis (strain DSM 21063 / JCM 11548 / VA1)\",\"taxonId\":410359}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A3MTR6.json)

```json
{
  "evidence_id": "C4",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A3MTR6.json",
  "source_sha256": "ab4d5d4975cecc6a04c1957b13bd9283e2ef63f3360c1922d6682cfab0917db3",
  "retrieved_utc": "2026-11-02T04:26:58.786987+00:00",
  "json_pointer": "/proteinDescription",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39208883\",\"source\":\"PubMed\"}],\"value\":\"Glucose-6-phosphate isomerase\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"GPI\"}]},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Mannose-6-phosphate isomerase\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39208883\",\"source\":\"PubMed\"}],\"value\":\"5.3.1.8\"},{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39208883\",\"source\":\"PubMed\"}],\"value\":\"5.3.1.9\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39208883\",\"source\":\"PubMed\"}],\"value\":\"Bifunctional phosphoglucose/phosphomannose isomerase\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Bifunctional PGI/PMI\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A3MTR6.json)

```json
{
  "evidence_id": "C5",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A3MTR6.json",
  "source_sha256": "ab4d5d4975cecc6a04c1957b13bd9283e2ef63f3360c1922d6682cfab0917db3",
  "retrieved_utc": "2026-11-02T04:26:58.786987+00:00",
  "json_pointer": "/comments/4",
  "excerpt": "{\"commentType\":\"BIOPHYSICOCHEMICAL PROPERTIES\",\"kineticParameters\":{\"maximumVelocities\":[{\"enzyme\":\"enzyme with glucose 6-phosphate as substrate\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39208883\",\"source\":\"PubMed\"}],\"unit\":\"umol/min/mg\",\"velocity\":290.0},{\"enzyme\":\"enzyme with mannose 6-phosphate as substrate\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39208883\",\"source\":\"PubMed\"}],\"unit\":\"umol/min/mg\",\"velocity\":235.0},{\"enzyme\":\"enzyme with fructose 6-phosphate as substrate\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39208883\",\"source\":\"PubMed\"}],\"unit\":\"umol/min/mg\",\"velocity\":240.0}],\"michaelisConstants\":[{\"constant\":0.33,\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39208883\",\"source\":\"PubMed\"}],\"substrate\":\"glucose 6-phosphate\",\"unit\":\"mM\"},{\"constant\":0.34,\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39208883\",\"source\":\"PubMed\"}],\"substrate\":\"mannose 6-phosphate\",\"unit\":\"mM\"},{\"constant\":0.29,\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39208883\",\"source\":\"PubMed\"}],\"substrate\":\"fructose 6-phosphate\",\"unit\":\"mM\"}],\"note\":{\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39208883\",\"source\":\"PubMed\"}],\"value\":\"kcat is 315 sec(-1) with glucose 6-phosphate as substrate. kcat is 240 sec(-1) with mannose 6-phosphate as substrate. kcat is 265 sec(-1) with fructose 6-phosphate as substrate.\"}]}},\"phDependence\":{\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39208883\",\"source\":\"PubMed\"}],\"value\":\"Optimum pH is 8.5 (for phosphoglucose isomerase activity) (PubMed:39208883). Activity is reduced significantly below pH 8.0 and above 9.0 (PubMed:39208883).\"}]},\"temperatureDependence\":{\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39208883\",\"source\":\"PubMed\"}],\"value\":\"Optimum temperature is 90 degrees Celsius (for phosphoglucose isomerase activity) (PubMed:39208883). Displays high thermostability with a half-life of about 50 minutes at 100 degrees Celsius (PubMed:39208883).\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A3MTR6.json)

```json
{
  "evidence_id": "C6",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A3MTR6.json",
  "source_sha256": "ab4d5d4975cecc6a04c1957b13bd9283e2ef63f3360c1922d6682cfab0917db3",
  "retrieved_utc": "2026-11-02T04:26:58.786987+00:00",
  "json_pointer": "/references/1",
  "excerpt": "{\"citation\":{\"authors\":[\"Maqsood A.\",\"Shakir N.A.\",\"Aslam M.\",\"Rahman M.\",\"Rashid N.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"39208883\"},{\"database\":\"DOI\",\"id\":\"10.1016/j.ijbiomac.2024.135127\"}],\"citationType\":\"journal article\",\"firstPage\":\"135127\",\"id\":\"39208883\",\"journal\":\"Int. J. Biol. Macromol.\",\"lastPage\":\"135127\",\"publicationDate\":\"2024\",\"title\":\"Structural and functional investigations of Pcal_0606, a bifunctional phosphoglucose/phosphomannose isomerase from Pyrobaculum calidifontis.\",\"volume\":\"279\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"DSM 21063 / JCM 11548 / VA1\"}],\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"ACTIVITY REGULATION\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"SUBUNIT\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A3MTR6?format=txt&versions=74)

```json
{
  "evidence_id": "H1",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A3MTR6?format=txt&versions=74",
  "source_sha256": "9c472af706932a5c4dae44d3e7eaa83f12d4956caae5979ddee1e4be573d0761",
  "retrieved_utc": "2026-11-02T04:27:04.156488+00:00",
  "source_locator": "lines 1-17",
  "excerpt": "ID   PGMI_PYRCJ              Reviewed;         299 AA.\nAC   A3MTR6;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   03-APR-2007, sequence version 1.\nDT   28-JAN-2026, entry version 74.\nDE   RecName: Full=Bifunctional phosphoglucose/phosphomannose isomerase {ECO:0000303|PubMed:39208883};\nDE            Short=Bifunctional PGI/PMI {ECO:0000305};\nDE            EC=5.3.1.8 {ECO:0000269|PubMed:39208883};\nDE            EC=5.3.1.9 {ECO:0000269|PubMed:39208883};\nDE   AltName: Full=Glucose-6-phosphate isomerase {ECO:0000303|PubMed:39208883};\nDE            Short=GPI {ECO:0000305};\nDE   AltName: Full=Mannose-6-phosphate isomerase {ECO:0000305};\nGN   OrderedLocusNames=Pcal_0606 {ECO:0000312|EMBL:ABO08033.1};\nOS   Pyrobaculum calidifontis (strain DSM 21063 / JCM 11548 / VA1).\nOC   Archaea; Thermoproteota; Thermoprotei; Thermoproteales; Thermoproteaceae;\nOC   Pyrobaculum.\nOX   NCBI_TaxID=410359;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 74,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A3MTR6?format=txt&versions=74)

```json
{
  "evidence_id": "H2",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A3MTR6?format=txt&versions=74",
  "source_sha256": "9c472af706932a5c4dae44d3e7eaa83f12d4956caae5979ddee1e4be573d0761",
  "retrieved_utc": "2026-11-02T04:27:04.156488+00:00",
  "source_locator": "lines 28-36",
  "excerpt": "RN   [2]\nRP   FUNCTION, CATALYTIC ACTIVITY, ACTIVITY REGULATION, BIOPHYSICOCHEMICAL\nRP   PROPERTIES, AND SUBUNIT.\nRC   STRAIN=DSM 21063 / JCM 11548 / VA1;\nRX   PubMed=39208883; DOI=10.1016/j.ijbiomac.2024.135127;\nRA   Maqsood A., Shakir N.A., Aslam M., Rahman M., Rashid N.;\nRT   \"Structural and functional investigations of Pcal_0606, a bifunctional\nRT   phosphoglucose/phosphomannose isomerase from Pyrobaculum calidifontis.\";\nRL   Int. J. Biol. Macromol. 279:135127-135127(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 74,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A3MTR6?format=txt&versions=74)

```json
{
  "evidence_id": "H3",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A3MTR6?format=txt&versions=74",
  "source_sha256": "9c472af706932a5c4dae44d3e7eaa83f12d4956caae5979ddee1e4be573d0761",
  "retrieved_utc": "2026-11-02T04:27:04.156488+00:00",
  "source_locator": "lines 55-78",
  "excerpt": "CC   -!- BIOPHYSICOCHEMICAL PROPERTIES:\nCC       Kinetic parameters:\nCC         KM=0.33 mM for glucose 6-phosphate {ECO:0000269|PubMed:39208883};\nCC         KM=0.34 mM for mannose 6-phosphate {ECO:0000269|PubMed:39208883};\nCC         KM=0.29 mM for fructose 6-phosphate {ECO:0000269|PubMed:39208883};\nCC         Vmax=290 umol/min/mg enzyme with glucose 6-phosphate as substrate\nCC         {ECO:0000269|PubMed:39208883};\nCC         Vmax=235 umol/min/mg enzyme with mannose 6-phosphate as substrate\nCC         {ECO:0000269|PubMed:39208883};\nCC         Vmax=240 umol/min/mg enzyme with fructose 6-phosphate as substrate\nCC         {ECO:0000269|PubMed:39208883};\nCC         Note=kcat is 315 sec(-1) with glucose 6-phosphate as substrate. kcat\nCC         is 240 sec(-1) with mannose 6-phosphate as substrate. kcat is 265\nCC         sec(-1) with fructose 6-phosphate as substrate.\nCC         {ECO:0000269|PubMed:39208883};\nCC       pH dependence:\nCC         Optimum pH is 8.5 (for phosphoglucose isomerase activity)\nCC         (PubMed:39208883). Activity is reduced significantly below pH 8.0 and\nCC         above 9.0 (PubMed:39208883). {ECO:0000269|PubMed:39208883};\nCC       Temperature dependence:\nCC         Optimum temperature is 90 degrees Celsius (for phosphoglucose\nCC         isomerase activity) (PubMed:39208883). Displays high thermostability\nCC         with a half-life of about 50 minutes at 100 degrees Celsius\nCC         (PubMed:39208883). {ECO:0000269|PubMed:39208883};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 74,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/temperature.json), zero-based source row 17. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
