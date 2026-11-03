# EC_number_0033: before and after transfer clarification

[All 1,328 cases](../README.md) · [Method](../METHOD.md) · [Summary](../SUMMARY.md) · [Exact reviewer user message](../inputs/EC_number_0033.txt)

**Task:** `EC_number`  
**Author key, unchanged:** **C** — 2.3.1.318

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
MTQPCIISVAITGSLPRKRDNPAVPITVSEQVESTQAAFEAGATLVHLHVRNDDETPSSEPDRFARVLEGIRKHAPGIITQVSTGGRSGAGRERGGMLSLRPDMASLATGSVNFPTRVYDNPPDLVDWLAAEMKAYAIKPEIEAFDLSMIFQAVAMQQAGKIDGALHIQFVMGIKNAMPVDREVLAFYVHTLRRLAPDATWTGAGIGRDQLTMARWSLELGGHCRTGLEDNVRLDKQTLAPSNAALVSQVAALCEEYGRPVATVAQARALLGLPSMEIDGRSPW

[Multiple Choices]
A. 2.3.1.193
B. 6.3.5.1
C. 2.3.1.318
D. 4.3.1.24
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

> The exact sequence matches the UniProt entry annotated as 3-oxoadipate:acetyl-CoA acetyltransferase, EC 2.3.1.318. Its catalytic-activity annotation assigns the reaction 3-oxoadipate + acetyl-CoA = acetoacetate + succinyl-CoA and cites experimental evidence (ECO:0000269, PubMed:24240508).

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence is compatible with an enzyme, but the supplied sequence and choices do not establish its precise substrate specificity or reaction. Distinguishing the listed EC numbers requires identifying the protein's specific catalytic function.


**Missing item-specific fact**

> The sequence-specific functional annotation or experimental evidence identifying this protein's catalyzed reaction as 3-oxoadipate:acetyl-CoA acetyltransferase.


**Reason**

> The supporting reaction annotation is reviewer-only and was not provided in the question. General sequence reasoning alone does not meaningfully select this exact EC number over the alternatives.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The choices specify different EC numbers, and the sequence-matched annotation supports C; no evidence here supports another listed option.


### Important caveats

- The UniProt annotation cites experimental evidence, but the cited primary paper was not independently reviewed here.
- The actual author source snapshot is unknown; the reviewer-only historical record and current record both match the supplied sequence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is compatible with an enzyme, but the supplied sequence and choices do not establish its precise substrate specificity or reaction. Distinguishing the listed EC numbers requires identifying the protein's specific catalytic function.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The sequence-specific functional annotation or experimental evidence identifying this protein's catalyzed reaction as 3-oxoadipate:acetyl-CoA acetyltransferase.",
    "reason": "The supporting reaction annotation is reviewer-only and was not provided in the question. General sequence reasoning alone does not meaningfully select this exact EC number over the alternatives."
  },
  "case_id": "EC_number_0033",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry annotated as 3-oxoadipate:acetyl-CoA acetyltransferase, EC 2.3.1.318. Its catalytic-activity annotation assigns the reaction 3-oxoadipate + acetyl-CoA = acetoacetate + succinyl-CoA and cites experimental evidence (ECO:0000269, PubMed:24240508)."
  },
  "important_caveats": [
    "The UniProt annotation cites experimental evidence, but the cited primary paper was not independently reviewed here.",
    "The actual author source snapshot is unknown; the reviewer-only historical record and current record both match the supplied sequence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The choices specify different EC numbers, and the sequence-matched annotation supports C; no evidence here supports another listed option."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0033",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry annotated as 3-oxoadipate:acetyl-CoA acetyltransferase, EC 2.3.1.318. Its catalytic-activity annotation assigns the reaction 3-oxoadipate + acetyl-CoA = acetoacetate + succinyl-CoA and cites experimental evidence (ECO:0000269, PubMed:24240508).",
    "evidence_ids": ["C1", "C4", "C5", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence is compatible with an enzyme, but the supplied sequence and choices do not establish its precise substrate specificity or reaction. Distinguishing the listed EC numbers requires identifying the protein's specific catalytic function.",
    "missing_item_specific_fact": "The sequence-specific functional annotation or experimental evidence identifying this protein's catalyzed reaction as 3-oxoadipate:acetyl-CoA acetyltransferase.",
    "reason": "The supporting reaction annotation is reviewer-only and was not provided in the question. General sequence reasoning alone does not meaningfully select this exact EC number over the alternatives."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The choices specify different EC numbers, and the sequence-matched annotation supports C; no evidence here supports another listed option."
  },
  "important_caveats": [
    "The UniProt annotation cites experimental evidence, but the cited primary paper was not independently reviewed here.",
    "The actual author source snapshot is unknown; the reviewer-only historical record and current record both match the supplied sequence."
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

> The supplied 284-aa sequence exactly matches UniProt Q0KAA1 (3OXCE_CUPNH) from Cupriavidus necator H16. The EC 2.3.1.318 annotation (3-oxoadipate:acetyl-CoA acetyltransferase) is backed by experimental evidence (ECO:0000269, in vitro assay) from PubMed 24240508 (Bastard et al., Nat. Chem. Biol. 2014). The catalytic reaction (3-oxoadipate + acetyl-CoA → acetoacetate + succinyl-CoA) is confirmed with Rhea and ChEBI cross-references. Sequence match is confirmed in both current (v89) and historical (v87) snapshots.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> Two distractors (6.3.5.1, a ligase/glutamine synthetase; 4.3.1.24, a C-N lyase) can be eliminated by recognizing the wrong enzyme class and inconsistent protein size (glutamine synthetase is ~460+ aa in bacteria vs. 284 aa here). However, the remaining contest is between EC 2.3.1.193 and EC 2.3.1.318, both acyltransferases. Distinguishing between two specific acyltransferase EC numbers from a 284-aa sequence requires knowledge of the precise substrate specificity (3-oxoadipate + acetyl-CoA → acetoacetate + succinyl-CoA) determined experimentally in 2014. No general sequence motif or family-level reasoning separates these two EC numbers.


**Missing item-specific fact**

> The specific substrate specificity of this enzyme (3-oxoadipate:acetyl-CoA acetyltransferase) was established only by in vitro experimentation (PubMed 24240508, 2014). Without knowing which acyltransferase subfamily this protein belongs to and its exact reaction, one cannot distinguish EC 2.3.1.193 from EC 2.3.1.318 by sequence reasoning alone.


**Reason**

> While class-level elimination (ligase, lyase) is feasible, the critical discrimination between two acyltransferase EC numbers depends on an item-specific experimental fact (the exact substrates/products of this recently characterized enzyme) that is not inferable from general sequence features or motifs.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A (2.3.1.193)",
  "C (2.3.1.318)"
]
```

> Both are acyltransferases. Without prior knowledge of the specific reaction catalyzed by this 284-aa protein, a model cannot distinguish between these two EC numbers from sequence alone. The other two options (6.3.5.1, 4.3.1.24) are eliminable by class and size, but the A-vs-C contest is not resolvable by general reasoning.


### Important caveats

- EC 2.3.1.318 was assigned relatively recently (2014 experimental characterization; UniProt entry first public 2025-02-05), making it unlikely to be widely represented in training data.
- The identity of EC 2.3.1.193 could not be independently verified from the supplied evidence; its exact name and substrate are not provided, limiting the ability to assess whether any subtle sequence distinction exists.
- The reviewer-only evidence confirms the key but was not available to the evaluated model.
- The sequence-to-function mapping for this enzyme was established by heterologous expression and in vitro assay, not by sequence homology alone.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Two distractors (6.3.5.1, a ligase/glutamine synthetase; 4.3.1.24, a C-N lyase) can be eliminated by recognizing the wrong enzyme class and inconsistent protein size (glutamine synthetase is ~460+ aa in bacteria vs. 284 aa here). However, the remaining contest is between EC 2.3.1.193 and EC 2.3.1.318, both acyltransferases. Distinguishing between two specific acyltransferase EC numbers from a 284-aa sequence requires knowledge of the precise substrate specificity (3-oxoadipate + acetyl-CoA → acetoacetate + succinyl-CoA) determined experimentally in 2014. No general sequence motif or family-level reasoning separates these two EC numbers.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific substrate specificity of this enzyme (3-oxoadipate:acetyl-CoA acetyltransferase) was established only by in vitro experimentation (PubMed 24240508, 2014). Without knowing which acyltransferase subfamily this protein belongs to and its exact reaction, one cannot distinguish EC 2.3.1.193 from EC 2.3.1.318 by sequence reasoning alone.",
    "reason": "While class-level elimination (ligase, lyase) is feasible, the critical discrimination between two acyltransferase EC numbers depends on an item-specific experimental fact (the exact substrates/products of this recently characterized enzyme) that is not inferable from general sequence features or motifs."
  },
  "case_id": "EC_number_0033",
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
    "reason": "The supplied 284-aa sequence exactly matches UniProt Q0KAA1 (3OXCE_CUPNH) from Cupriavidus necator H16. The EC 2.3.1.318 annotation (3-oxoadipate:acetyl-CoA acetyltransferase) is backed by experimental evidence (ECO:0000269, in vitro assay) from PubMed 24240508 (Bastard et al., Nat. Chem. Biol. 2014). The catalytic reaction (3-oxoadipate + acetyl-CoA → acetoacetate + succinyl-CoA) is confirmed with Rhea and ChEBI cross-references. Sequence match is confirmed in both current (v89) and historical (v87) snapshots."
  },
  "important_caveats": [
    "EC 2.3.1.318 was assigned relatively recently (2014 experimental characterization; UniProt entry first public 2025-02-05), making it unlikely to be widely represented in training data.",
    "The identity of EC 2.3.1.193 could not be independently verified from the supplied evidence; its exact name and substrate are not provided, limiting the ability to assess whether any subtle sequence distinction exists.",
    "The reviewer-only evidence confirms the key but was not available to the evaluated model.",
    "The sequence-to-function mapping for this enzyme was established by heterologous expression and in vitro assay, not by sequence homology alone."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A (2.3.1.193)",
      "C (2.3.1.318)"
    ],
    "reason": "Both are acyltransferases. Without prior knowledge of the specific reaction catalyzed by this 284-aa protein, a model cannot distinguish between these two EC numbers from sequence alone. The other two options (6.3.5.1, 4.3.1.24) are eliminable by class and size, but the A-vs-C contest is not resolvable by general reasoning."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0033",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied 284-aa sequence exactly matches UniProt Q0KAA1 (3OXCE_CUPNH) from Cupriavidus necator H16. The EC 2.3.1.318 annotation (3-oxoadipate:acetyl-CoA acetyltransferase) is backed by experimental evidence (ECO:0000269, in vitro assay) from PubMed 24240508 (Bastard et al., Nat. Chem. Biol. 2014). The catalytic reaction (3-oxoadipate + acetyl-CoA → acetoacetate + succinyl-CoA) is confirmed with Rhea and ChEBI cross-references. Sequence match is confirmed in both current (v89) and historical (v87) snapshots.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H1", "H2", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "Two distractors (6.3.5.1, a ligase/glutamine synthetase; 4.3.1.24, a C-N lyase) can be eliminated by recognizing the wrong enzyme class and inconsistent protein size (glutamine synthetase is ~460+ aa in bacteria vs. 284 aa here). However, the remaining contest is between EC 2.3.1.193 and EC 2.3.1.318, both acyltransferases. Distinguishing between two specific acyltransferase EC numbers from a 284-aa sequence requires knowledge of the precise substrate specificity (3-oxoadipate + acetyl-CoA → acetoacetate + succinyl-CoA) determined experimentally in 2014. No general sequence motif or family-level reasoning separates these two EC numbers.",
    "missing_item_specific_fact": "The specific substrate specificity of this enzyme (3-oxoadipate:acetyl-CoA acetyltransferase) was established only by in vitro experimentation (PubMed 24240508, 2014). Without knowing which acyltransferase subfamily this protein belongs to and its exact reaction, one cannot distinguish EC 2.3.1.193 from EC 2.3.1.318 by sequence reasoning alone.",
    "reason": "While class-level elimination (ligase, lyase) is feasible, the critical discrimination between two acyltransferase EC numbers depends on an item-specific experimental fact (the exact substrates/products of this recently characterized enzyme) that is not inferable from general sequence features or motifs."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A (2.3.1.193)", "C (2.3.1.318)"],
    "reason": "Both are acyltransferases. Without prior knowledge of the specific reaction catalyzed by this 284-aa protein, a model cannot distinguish between these two EC numbers from sequence alone. The other two options (6.3.5.1, 4.3.1.24) are eliminable by class and size, but the A-vs-C contest is not resolvable by general reasoning."
  },
  "important_caveats": [
    "EC 2.3.1.318 was assigned relatively recently (2014 experimental characterization; UniProt entry first public 2025-02-05), making it unlikely to be widely represented in training data.",
    "The identity of EC 2.3.1.193 could not be independently verified from the supplied evidence; its exact name and substrate are not provided, limiting the ability to assess whether any subtle sequence distinction exists.",
    "The reviewer-only evidence confirms the key but was not available to the evaluated model.",
    "The sequence-to-function mapping for this enzyme was established by heterologous expression and in vitro assay, not by sequence homology alone."
  ]
}
```

</details>

## After: GPT-6 Luna

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence-matched UniProt record assigns EC 2.3.1.318 and gives the corresponding 3-oxoadipate + acetyl-CoA reaction, citing experimental evidence (ECO:0000269). This supports the key, though the cited study was not independently reviewed here.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence has features consistent with a CoA-dependent acyltransferase/thiolase-like enzyme, which makes the acyltransferase choices more plausible than the carbamoyl-phosphate synthetase or lyase choices. Those general family features do not, by themselves, establish the substrate-specific reaction needed to distinguish EC 2.3.1.318 from the other acyltransferase option.


**Missing item-specific fact**

> The enzyme's experimentally established substrate and reaction specificity, particularly whether it catalyzes the 3-oxoadipate reaction assigned to EC 2.3.1.318.


**Reason**

> Transferable family-level knowledge can narrow the chemistry, but the offered choices include another acyltransferase and the sequence features stated here do not credibly resolve that finer specificity. Choosing C requires target-specific functional annotation or equivalent substrate-specific evidence.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The reviewer-only evidence supports C; the limitation is that the original sequence does not provide a sufficiently specific transferable discriminator, not that another option is established as equally correct.


### Important caveats

- The source evidence is reviewer-only and was not part of the original model input.
- The cited experimental evidence is reported in the sequence-matched UniProt record; the primary study was not independently validated here.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has features consistent with a CoA-dependent acyltransferase/thiolase-like enzyme, which makes the acyltransferase choices more plausible than the carbamoyl-phosphate synthetase or lyase choices. Those general family features do not, by themselves, establish the substrate-specific reaction needed to distinguish EC 2.3.1.318 from the other acyltransferase option.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The enzyme's experimentally established substrate and reaction specificity, particularly whether it catalyzes the 3-oxoadipate reaction assigned to EC 2.3.1.318.",
    "reason": "Transferable family-level knowledge can narrow the chemistry, but the offered choices include another acyltransferase and the sequence features stated here do not credibly resolve that finer specificity. Choosing C requires target-specific functional annotation or equivalent substrate-specific evidence."
  },
  "case_id": "EC_number_0033",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record assigns EC 2.3.1.318 and gives the corresponding 3-oxoadipate + acetyl-CoA reaction, citing experimental evidence (ECO:0000269). This supports the key, though the cited study was not independently reviewed here."
  },
  "important_caveats": [
    "The source evidence is reviewer-only and was not part of the original model input.",
    "The cited experimental evidence is reported in the sequence-matched UniProt record; the primary study was not independently validated here."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The reviewer-only evidence supports C; the limitation is that the original sequence does not provide a sufficiently specific transferable discriminator, not that another option is established as equally correct."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0033",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record assigns EC 2.3.1.318 and gives the corresponding 3-oxoadipate + acetyl-CoA reaction, citing experimental evidence (ECO:0000269). This supports the key, though the cited study was not independently reviewed here.",
    "evidence_ids": ["C4", "C5", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence has features consistent with a CoA-dependent acyltransferase/thiolase-like enzyme, which makes the acyltransferase choices more plausible than the carbamoyl-phosphate synthetase or lyase choices. Those general family features do not, by themselves, establish the substrate-specific reaction needed to distinguish EC 2.3.1.318 from the other acyltransferase option.",
    "missing_item_specific_fact": "The enzyme's experimentally established substrate and reaction specificity, particularly whether it catalyzes the 3-oxoadipate reaction assigned to EC 2.3.1.318.",
    "reason": "Transferable family-level knowledge can narrow the chemistry, but the offered choices include another acyltransferase and the sequence features stated here do not credibly resolve that finer specificity. Choosing C requires target-specific functional annotation or equivalent substrate-specific evidence."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The reviewer-only evidence supports C; the limitation is that the original sequence does not provide a sufficiently specific transferable discriminator, not that another option is established as equally correct."
  },
  "important_caveats": [
    "The source evidence is reviewer-only and was not part of the original model input.",
    "The cited experimental evidence is reported in the sequence-matched UniProt record; the primary study was not independently validated here."
  ]
}
```

</details>

## After: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry Q0KAA1 (sequence matched, 284 aa) annotates EC 2.3.1.318 (3-oxoadipate:acetyl-CoA acetyltransferase) with evidence code ECO:0000269 (inferred from direct assay), citing PubMed:24240508 (Bastard et al., Nat. Chem. Biol. 2014). The catalytic reaction '3-oxoadipate + acetyl-CoA = acetoacetate + succinyl-CoA' is experimentally characterized. Both the current entry and the historical archived entry (version 87) confirm this annotation with the same evidence code and primary reference. The sequence in the question matches the source sequence exactly.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 284-aa sequence contains hallmark thiolase-superfamily features: the 'GKIDGALHIQFVMGIKNAMPVDREVLAFYVHTLRRLAPDATWTGAGIGRDQLTMARWSLELGG' region displays the conserved thiolase active-site architecture (GAGIG motif, the catalytic Cys/His/Asn triad region, and the CoA-binding loop 'GGRSGAGRERGG'). This thiolase-like fold is incompatible with EC 6.3.5.1 (a ligase requiring ATP-binding Walker-A/B motifs and a distinct fold) and EC 4.3.1.24 (a carbon–nitrogen lyase with an unrelated fold), effectively eliminating choices B and D. Both remaining choices A (2.3.1.193) and C (2.3.1.318) fall in EC 2.3.1.x (acyltransferases), so family-level recognition narrows the field to these two. The 284-aa length is notably shorter than canonical thiolases (~390–400 aa), and the overall motif arrangement is more consistent with divergent thiolase-superfamily members that catalyze CoA-transfer reactions on non-thioester substrates (e.g., 3-oxoadipate cleavage) rather than the classic C–C cleavage of acyl-CoA thioesters. The 2014 paper by Bastard et al. that characterized this enzyme was titled 'Revealing the hidden functional diversity of an enzyme family,' underscoring that this protein belongs to the thiolase superfamily but has an unexpected substrate specificity. A model recognizing the thiolase fold, the atypical shortness, and the CoA-transferase-type active-site geometry can probabilistically favor EC 2.3.1.318 (a recently defined thiolase-superfamily CoA-transferase) over EC 2.3.1.193, though the A-vs-C distinction is the hardest part of the question.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The thiolase-fold recognition is a legitimate, transferable inference from other thiolase-superfamily proteins that eliminates the ligase (B) and lyase (D) choices. The A-vs-C distinction relies on subfamily-level features (shorter-than-canonical length, CoA-transferase geometry, divergent active-site context) that are shared patterns across the broader thiolase superfamily and do not require memorizing this exact protein's database entry. The inference is probabilistic rather than certain, but it meaningfully distinguishes the offered choices.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "C"
]
```

> Both A (EC 2.3.1.193) and C (EC 2.3.1.318) are acyltransferases within EC 2.3.1.x, and both could be associated with thiolase-superfamily folds. Without certainty about the exact identity and reaction of EC 2.3.1.193, a model might hesitate between the two. The 2014 paper's emphasis on 'hidden functional diversity' implies that sequence-based prediction alone does not straightforwardly yield EC 2.3.1.318, making the A-vs-C boundary genuinely difficult.


### Important caveats

- The exact identity and reaction of EC 2.3.1.193 could not be independently confirmed from the supplied evidence; if it is itself a thiolase, the A-vs-C distinction becomes substantially harder and may lean toward lookup dependence.
- The 2014 primary reference (PubMed:24240508) demonstrated the EC 2.3.1.318 activity experimentally (ECO:0000269); the 'hidden functional diversity' framing suggests that pure sequence homology to classic thiolases would not predict this EC number, making the A-vs-C discrimination inherently challenging.
- The reviewer-only evidence (UniProt Q0KAA1, Cupriavidus necator) was not available to the evaluated model; the answerability assessment relies solely on the sequence and choices as presented.
- The 284-aa length and motif arrangement support a thiolase-superfamily assignment but do not uniquely determine the exact EC number within 2.3.1.x; the reasoning for C over A is probabilistic and subfamily-level rather than definitive.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 284-aa sequence contains hallmark thiolase-superfamily features: the 'GKIDGALHIQFVMGIKNAMPVDREVLAFYVHTLRRLAPDATWTGAGIGRDQLTMARWSLELGG' region displays the conserved thiolase active-site architecture (GAGIG motif, the catalytic Cys/His/Asn triad region, and the CoA-binding loop 'GGRSGAGRERGG'). This thiolase-like fold is incompatible with EC 6.3.5.1 (a ligase requiring ATP-binding Walker-A/B motifs and a distinct fold) and EC 4.3.1.24 (a carbon–nitrogen lyase with an unrelated fold), effectively eliminating choices B and D. Both remaining choices A (2.3.1.193) and C (2.3.1.318) fall in EC 2.3.1.x (acyltransferases), so family-level recognition narrows the field to these two. The 284-aa length is notably shorter than canonical thiolases (~390–400 aa), and the overall motif arrangement is more consistent with divergent thiolase-superfamily members that catalyze CoA-transfer reactions on non-thioester substrates (e.g., 3-oxoadipate cleavage) rather than the classic C–C cleavage of acyl-CoA thioesters. The 2014 paper by Bastard et al. that characterized this enzyme was titled 'Revealing the hidden functional diversity of an enzyme family,' underscoring that this protein belongs to the thiolase superfamily but has an unexpected substrate specificity. A model recognizing the thiolase fold, the atypical shortness, and the CoA-transferase-type active-site geometry can probabilistically favor EC 2.3.1.318 (a recently defined thiolase-superfamily CoA-transferase) over EC 2.3.1.193, though the A-vs-C distinction is the hardest part of the question.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The thiolase-fold recognition is a legitimate, transferable inference from other thiolase-superfamily proteins that eliminates the ligase (B) and lyase (D) choices. The A-vs-C distinction relies on subfamily-level features (shorter-than-canonical length, CoA-transferase geometry, divergent active-site context) that are shared patterns across the broader thiolase superfamily and do not require memorizing this exact protein's database entry. The inference is probabilistic rather than certain, but it meaningfully distinguishes the offered choices."
  },
  "case_id": "EC_number_0033",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "UniProt entry Q0KAA1 (sequence matched, 284 aa) annotates EC 2.3.1.318 (3-oxoadipate:acetyl-CoA acetyltransferase) with evidence code ECO:0000269 (inferred from direct assay), citing PubMed:24240508 (Bastard et al., Nat. Chem. Biol. 2014). The catalytic reaction '3-oxoadipate + acetyl-CoA = acetoacetate + succinyl-CoA' is experimentally characterized. Both the current entry and the historical archived entry (version 87) confirm this annotation with the same evidence code and primary reference. The sequence in the question matches the source sequence exactly."
  },
  "important_caveats": [
    "The exact identity and reaction of EC 2.3.1.193 could not be independently confirmed from the supplied evidence; if it is itself a thiolase, the A-vs-C distinction becomes substantially harder and may lean toward lookup dependence.",
    "The 2014 primary reference (PubMed:24240508) demonstrated the EC 2.3.1.318 activity experimentally (ECO:0000269); the 'hidden functional diversity' framing suggests that pure sequence homology to classic thiolases would not predict this EC number, making the A-vs-C discrimination inherently challenging.",
    "The reviewer-only evidence (UniProt Q0KAA1, Cupriavidus necator) was not available to the evaluated model; the answerability assessment relies solely on the sequence and choices as presented.",
    "The 284-aa length and motif arrangement support a thiolase-superfamily assignment but do not uniquely determine the exact EC number within 2.3.1.x; the reasoning for C over A is probabilistic and subfamily-level rather than definitive."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "C"
    ],
    "reason": "Both A (EC 2.3.1.193) and C (EC 2.3.1.318) are acyltransferases within EC 2.3.1.x, and both could be associated with thiolase-superfamily folds. Without certainty about the exact identity and reaction of EC 2.3.1.193, a model might hesitate between the two. The 2014 paper's emphasis on 'hidden functional diversity' implies that sequence-based prediction alone does not straightforwardly yield EC 2.3.1.318, making the A-vs-C boundary genuinely difficult."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0033",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry Q0KAA1 (sequence matched, 284 aa) annotates EC 2.3.1.318 (3-oxoadipate:acetyl-CoA acetyltransferase) with evidence code ECO:0000269 (inferred from direct assay), citing PubMed:24240508 (Bastard et al., Nat. Chem. Biol. 2014). The catalytic reaction '3-oxoadipate + acetyl-CoA = acetoacetate + succinyl-CoA' is experimentally characterized. Both the current entry and the historical archived entry (version 87) confirm this annotation with the same evidence code and primary reference. The sequence in the question matches the source sequence exactly.",
    "evidence_ids": ["C4", "C5", "C6", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 284-aa sequence contains hallmark thiolase-superfamily features: the 'GKIDGALHIQFVMGIKNAMPVDREVLAFYVHTLRRLAPDATWTGAGIGRDQLTMARWSLELGG' region displays the conserved thiolase active-site architecture (GAGIG motif, the catalytic Cys/His/Asn triad region, and the CoA-binding loop 'GGRSGAGRERGG'). This thiolase-like fold is incompatible with EC 6.3.5.1 (a ligase requiring ATP-binding Walker-A/B motifs and a distinct fold) and EC 4.3.1.24 (a carbon–nitrogen lyase with an unrelated fold), effectively eliminating choices B and D. Both remaining choices A (2.3.1.193) and C (2.3.1.318) fall in EC 2.3.1.x (acyltransferases), so family-level recognition narrows the field to these two. The 284-aa length is notably shorter than canonical thiolases (~390–400 aa), and the overall motif arrangement is more consistent with divergent thiolase-superfamily members that catalyze CoA-transfer reactions on non-thioester substrates (e.g., 3-oxoadipate cleavage) rather than the classic C–C cleavage of acyl-CoA thioesters. The 2014 paper by Bastard et al. that characterized this enzyme was titled 'Revealing the hidden functional diversity of an enzyme family,' underscoring that this protein belongs to the thiolase superfamily but has an unexpected substrate specificity. A model recognizing the thiolase fold, the atypical shortness, and the CoA-transferase-type active-site geometry can probabilistically favor EC 2.3.1.318 (a recently defined thiolase-superfamily CoA-transferase) over EC 2.3.1.193, though the A-vs-C distinction is the hardest part of the question.",
    "missing_item_specific_fact": "",
    "reason": "The thiolase-fold recognition is a legitimate, transferable inference from other thiolase-superfamily proteins that eliminates the ligase (B) and lyase (D) choices. The A-vs-C distinction relies on subfamily-level features (shorter-than-canonical length, CoA-transferase geometry, divergent active-site context) that are shared patterns across the broader thiolase superfamily and do not require memorizing this exact protein's database entry. The inference is probabilistic rather than certain, but it meaningfully distinguishes the offered choices."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "C"],
    "reason": "Both A (EC 2.3.1.193) and C (EC 2.3.1.318) are acyltransferases within EC 2.3.1.x, and both could be associated with thiolase-superfamily folds. Without certainty about the exact identity and reaction of EC 2.3.1.193, a model might hesitate between the two. The 2014 paper's emphasis on 'hidden functional diversity' implies that sequence-based prediction alone does not straightforwardly yield EC 2.3.1.318, making the A-vs-C boundary genuinely difficult."
  },
  "important_caveats": [
    "The exact identity and reaction of EC 2.3.1.193 could not be independently confirmed from the supplied evidence; if it is itself a thiolase, the A-vs-C distinction becomes substantially harder and may lean toward lookup dependence.",
    "The 2014 primary reference (PubMed:24240508) demonstrated the EC 2.3.1.318 activity experimentally (ECO:0000269); the 'hidden functional diversity' framing suggests that pure sequence homology to classic thiolases would not predict this EC number, making the A-vs-C discrimination inherently challenging.",
    "The reviewer-only evidence (UniProt Q0KAA1, Cupriavidus necator) was not available to the evaluated model; the answerability assessment relies solely on the sequence and choices as presented.",
    "The 284-aa length and motif arrangement support a thiolase-superfamily assignment but do not uniquely determine the exact EC number within 2.3.1.x; the reasoning for C over A is probabilistic and subfamily-level rather than definitive."
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
  "requested_accession": "Q0KAA1",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "benchmark_sequence_sha256": "578ee40d19a4187b96bbd813dd5b2ad6c5cd4952c2e58954fc66e0445da2dd06",
  "benchmark_sequence_length": 284,
  "current_status": "retrieved",
  "current_sequence_comparison": "matched",
  "current_entry_audit": {
    "entryVersion": 89,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2006-10-03",
    "sequenceVersion": 1
  },
  "current_uniprot_release": "2026_03",
  "current_record_sha256": "c8f71ccfa4b417ca33bf6e9e7b333cdb179beaa73d1bbbba6e6d86bbeaaac140",
  "current_source_sequence_sha256": "578ee40d19a4187b96bbd813dd5b2ad6c5cd4952c2e58954fc66e0445da2dd06",
  "current_source_sequence_length": 284,
  "historical_status": "retrieved",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "selected_historical_entry_version": 87,
  "selected_historical_version": {
    "accession": "Q0KAA1",
    "database": "Swiss-Prot",
    "entryVersion": 87,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "3OXCE_CUPNH",
    "sequenceVersion": 1
  },
  "selected_historical_record_sha256": "6f05fdb130e65dbd4fe594e672961fa4042d9e020ec6cf0253a116bc497dc13e",
  "selected_historical_source_sequence_sha256": "578ee40d19a4187b96bbd813dd5b2ad6c5cd4952c2e58954fc66e0445da2dd06",
  "selected_historical_source_sequence_length": 284,
  "latest_at_cutoff_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 87,
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q0KAA1.json)

```json
{
  "evidence_id": "C1",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q0KAA1.json",
  "source_sha256": "c8f71ccfa4b417ca33bf6e9e7b333cdb179beaa73d1bbbba6e6d86bbeaaac140",
  "retrieved_utc": "2026-11-02T04:30:26.682394+00:00",
  "json_pointer": "/primaryAccession",
  "excerpt": "\"Q0KAA1\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q0KAA1.json)

```json
{
  "evidence_id": "C2",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q0KAA1.json",
  "source_sha256": "c8f71ccfa4b417ca33bf6e9e7b333cdb179beaa73d1bbbba6e6d86bbeaaac140",
  "retrieved_utc": "2026-11-02T04:30:26.682394+00:00",
  "json_pointer": "/entryAudit",
  "excerpt": "{\"entryVersion\":89,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2006-10-03\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q0KAA1.json)

```json
{
  "evidence_id": "C3",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q0KAA1.json",
  "source_sha256": "c8f71ccfa4b417ca33bf6e9e7b333cdb179beaa73d1bbbba6e6d86bbeaaac140",
  "retrieved_utc": "2026-11-02T04:30:26.682394+00:00",
  "json_pointer": "/organism",
  "excerpt": "{\"commonName\":\"Ralstonia eutropha\",\"lineage\":[\"Bacteria\",\"Pseudomonadati\",\"Pseudomonadota\",\"Betaproteobacteria\",\"Burkholderiales\",\"Burkholderiaceae\",\"Cupriavidus\"],\"scientificName\":\"Cupriavidus necator (strain ATCC 17699 / DSM 428 / KCTC 22496 / NCIMB 10442 / H16 / Stanier 337)\",\"taxonId\":381666}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q0KAA1.json)

```json
{
  "evidence_id": "C4",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q0KAA1.json",
  "source_sha256": "c8f71ccfa4b417ca33bf6e9e7b333cdb179beaa73d1bbbba6e6d86bbeaaac140",
  "retrieved_utc": "2026-11-02T04:30:26.682394+00:00",
  "json_pointer": "/proteinDescription",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"3-oxoadipate cleavage enzyme\"}},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"24240508\",\"source\":\"PubMed\"}],\"value\":\"BKACE_378\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"24240508\",\"source\":\"PubMed\"}],\"value\":\"2.3.1.318\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"3-oxoadipate:acetyl-CoA acetyltransferase\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q0KAA1.json)

```json
{
  "evidence_id": "C5",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q0KAA1.json",
  "source_sha256": "c8f71ccfa4b417ca33bf6e9e7b333cdb179beaa73d1bbbba6e6d86bbeaaac140",
  "retrieved_utc": "2026-11-02T04:30:26.682394+00:00",
  "json_pointer": "/comments/1",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"ecNumber\":\"2.3.1.318\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"24240508\",\"source\":\"PubMed\"}],\"name\":\"3-oxoadipate + acetyl-CoA = acetoacetate + succinyl-CoA\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:79651\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:13705\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15775\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57288\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57292\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q0KAA1.json)

```json
{
  "evidence_id": "C6",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q0KAA1.json",
  "source_sha256": "c8f71ccfa4b417ca33bf6e9e7b333cdb179beaa73d1bbbba6e6d86bbeaaac140",
  "retrieved_utc": "2026-11-02T04:30:26.682394+00:00",
  "json_pointer": "/references/2",
  "excerpt": "{\"citation\":{\"authors\":[\"Bastard K.\",\"Smith A.A.\",\"Vergne-Vaxelaire C.\",\"Perret A.\",\"Zaparucha A.\",\"De Melo-Minardi R.\",\"Mariage A.\",\"Boutard M.\",\"Debard A.\",\"Lechaplais C.\",\"Pelle C.\",\"Pellouin V.\",\"Perchat N.\",\"Petit J.L.\",\"Kreimeyer A.\",\"Medigue C.\",\"Weissenbach J.\",\"Artiguenave F.\",\"De Berardinis V.\",\"Vallenet D.\",\"Salanoubat M.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"24240508\"},{\"database\":\"DOI\",\"id\":\"10.1038/nchembio.1387\"}],\"citationType\":\"journal article\",\"firstPage\":\"42\",\"id\":\"24240508\",\"journal\":\"Nat. Chem. Biol.\",\"lastPage\":\"49\",\"publicationDate\":\"2014\",\"title\":\"Revealing the hidden functional diversity of an enzyme family.\",\"volume\":\"10\"},\"referenceNumber\":3,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q0KAA1?format=txt&versions=87)

```json
{
  "evidence_id": "H1",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q0KAA1?format=txt&versions=87",
  "source_sha256": "6f05fdb130e65dbd4fe594e672961fa4042d9e020ec6cf0253a116bc497dc13e",
  "retrieved_utc": "2026-11-02T04:30:29.925890+00:00",
  "source_locator": "lines 1-16",
  "excerpt": "ID   3OXCE_CUPNH             Reviewed;         284 AA.\nAC   Q0KAA1;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   03-OCT-2006, sequence version 1.\nDT   28-JAN-2026, entry version 87.\nDE   RecName: Full=3-oxoadipate:acetyl-CoA acetyltransferase {ECO:0000305};\nDE            EC=2.3.1.318 {ECO:0000269|PubMed:24240508};\nDE   AltName: Full=3-oxoadipate cleavage enzyme {ECO:0000305};\nDE   AltName: Full=BKACE_378 {ECO:0000303|PubMed:24240508};\nGN   OrderedLocusNames=H16_A1969 {ECO:0000312|EMBL:CAJ93070.1};\nGN   ORFNames=E6A55_10065 {ECO:0000312|EMBL:QCC00902.1};\nOS   Cupriavidus necator (strain ATCC 17699 / DSM 428 / KCTC 22496 / NCIMB 10442\nOS   / H16 / Stanier 337) (Ralstonia eutropha).\nOC   Bacteria; Pseudomonadati; Pseudomonadota; Betaproteobacteria;\nOC   Burkholderiales; Burkholderiaceae; Cupriavidus.\nOX   NCBI_TaxID=381666;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 87,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q0KAA1?format=txt&versions=87)

```json
{
  "evidence_id": "H2",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q0KAA1?format=txt&versions=87",
  "source_sha256": "6f05fdb130e65dbd4fe594e672961fa4042d9e020ec6cf0253a116bc497dc13e",
  "retrieved_utc": "2026-11-02T04:30:29.925890+00:00",
  "source_locator": "lines 6-9",
  "excerpt": "DE   RecName: Full=3-oxoadipate:acetyl-CoA acetyltransferase {ECO:0000305};\nDE            EC=2.3.1.318 {ECO:0000269|PubMed:24240508};\nDE   AltName: Full=3-oxoadipate cleavage enzyme {ECO:0000305};\nDE   AltName: Full=BKACE_378 {ECO:0000303|PubMed:24240508};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 87,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q0KAA1?format=txt&versions=87)

```json
{
  "evidence_id": "H3",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q0KAA1?format=txt&versions=87",
  "source_sha256": "6f05fdb130e65dbd4fe594e672961fa4042d9e020ec6cf0253a116bc497dc13e",
  "retrieved_utc": "2026-11-02T04:30:29.925890+00:00",
  "source_locator": "lines 34-43",
  "excerpt": "RN   [3]\nRP   FUNCTION, CATALYTIC ACTIVITY, AND BIOPHYSICOCHEMICAL PROPERTIES.\nRX   PubMed=24240508; DOI=10.1038/nchembio.1387;\nRA   Bastard K., Smith A.A., Vergne-Vaxelaire C., Perret A., Zaparucha A.,\nRA   De Melo-Minardi R., Mariage A., Boutard M., Debard A., Lechaplais C.,\nRA   Pelle C., Pellouin V., Perchat N., Petit J.L., Kreimeyer A., Medigue C.,\nRA   Weissenbach J., Artiguenave F., De Berardinis V., Vallenet D.,\nRA   Salanoubat M.;\nRT   \"Revealing the hidden functional diversity of an enzyme family.\";\nRL   Nat. Chem. Biol. 10:42-49(2014).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 87,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q0KAA1?format=txt&versions=87)

```json
{
  "evidence_id": "H4",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q0KAA1?format=txt&versions=87",
  "source_sha256": "6f05fdb130e65dbd4fe594e672961fa4042d9e020ec6cf0253a116bc497dc13e",
  "retrieved_utc": "2026-11-02T04:30:29.925890+00:00",
  "source_locator": "lines 49-53",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=3-oxoadipate + acetyl-CoA = acetoacetate + succinyl-CoA;\nCC         Xref=Rhea:RHEA:79651, ChEBI:CHEBI:13705, ChEBI:CHEBI:15775,\nCC         ChEBI:CHEBI:57288, ChEBI:CHEBI:57292; EC=2.3.1.318;\nCC         Evidence={ECO:0000269|PubMed:24240508};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 87,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 33. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
