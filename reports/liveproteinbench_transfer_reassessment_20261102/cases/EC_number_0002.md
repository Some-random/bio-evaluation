# EC_number_0002: before and after transfer clarification

[All 1,328 cases](../README.md) · [Method](../METHOD.md) · [Summary](../SUMMARY.md) · [Exact reviewer user message](../inputs/EC_number_0002.txt)

**Task:** `EC_number`  
**Author key, unchanged:** **C** — 1.97.1.14

| Round | Reviewer | Key support | Transfer / lookup | Output usability (canonical status) |
|---|---|---|---|---|
| before | GPT-6 Luna | supported | lookup-dependent | usable output (valid_review) |
| before | Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | output error (invalid_review) |
| after | GPT-6 Luna | supported | lookup-dependent | usable output (valid_review) |
| after | Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | usable output (valid_review) |

**Usable output means format-valid review, not reasoning-supported or biologically correct.** A usable output can classify the question as reasoning-supported, lookup-dependent or uncertain. An output error is a problem with the saved model response; it does not count a defective benchmark question or wrong key. Each saved review is retained in full below. Labels from output errors are displayed as saved and excluded from label statistics. The author key and reviewer evidence were visible to reviewers; this is a review of answerability and key support, not a benchmark-solving score.

## Complete original question

```text
[Protein Sequence]
MLKKLYFTVLSFIAIVGVISLYIRLSEGMKMSALTSYSSWGLWIVFYIYFIGLSAGSFLLSTMVYVFNMKQFERIGKLALFTAFFSLMAGLLFVLIDLGHPERFWHTLVYRQPNSILSWEIQFYLIYMLLIVAEIWFLMREEFAQRAQSTKGLTKLFNRTLTLGYKVPNSQQKLEFHREQSHKWMKILGIAGIPTAVGVHGGTGSLFGVVMAKEYWFSGLTPIIFLVSALVSGAALMLFLYSFFGGAKKNGDSLLKELGTLLTLFIGIDLLLMIAEFLIGLYNPIHHERMTFNEILFGDRWFIFWIGQIGMVIILPILLITISKGKRLLMGLAGLSVVLGIVCVRWILVIPAYVAPHFDGLDSAYNSSRLLYEYSPNLLEWSSSVGLIGIVILLFSITVQLVPVFNKQKEVHQTHGKPTPEIHIKA

[Multiple Choices]
A. 1.97.1.13
B. 1.5.1.38
C. 1.97.1.14
D. 1.14.19.80
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

> The supplied sequence exactly matches the UniProt entry for selenate reductase subunit C, annotated with EC 1.97.1.14 and a selenate-reductase reaction. The annotation cites a study describing the respiratory selenate reductase complex. This supports choice C as the assigned EC number, though it does not establish that this membrane-anchor subunit alone catalyzes the reaction.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The strongly hydrophobic sequence is consistent with a multi-pass membrane protein, but that broad feature does not identify the specific selenate-reductase complex or distinguish its exact EC number from the alternatives.


**Missing item-specific fact**

> The protein-specific annotation identifying this sequence as subunit C of the selenate reductase complex and assigning that complex EC 1.97.1.14.


**Reason**

> The exact four-part EC assignment depends on a protein-specific functional annotation or experimental identification absent from the sequence and choices. General sequence reasoning does not meaningfully resolve the close EC alternatives.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The matched sequence's database annotation supports C; no supplied evidence supports another listed EC number.


### Important caveats

- The UniProt annotation is a curated database claim citing a paper, not independent verification here of the primary experimental results.
- The EC number is assigned to the selenate-reductase activity of the complex; the sequence is annotated as its membrane-anchor subunit.
- The sequence match is exact in the reviewer evidence, but the author's original source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The strongly hydrophobic sequence is consistent with a multi-pass membrane protein, but that broad feature does not identify the specific selenate-reductase complex or distinguish its exact EC number from the alternatives.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific annotation identifying this sequence as subunit C of the selenate reductase complex and assigning that complex EC 1.97.1.14.",
    "reason": "The exact four-part EC assignment depends on a protein-specific functional annotation or experimental identification absent from the sequence and choices. General sequence reasoning does not meaningfully resolve the close EC alternatives."
  },
  "case_id": "EC_number_0002",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "H1",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the UniProt entry for selenate reductase subunit C, annotated with EC 1.97.1.14 and a selenate-reductase reaction. The annotation cites a study describing the respiratory selenate reductase complex. This supports choice C as the assigned EC number, though it does not establish that this membrane-anchor subunit alone catalyzes the reaction."
  },
  "important_caveats": [
    "The UniProt annotation is a curated database claim citing a paper, not independent verification here of the primary experimental results.",
    "The EC number is assigned to the selenate-reductase activity of the complex; the sequence is annotated as its membrane-anchor subunit.",
    "The sequence match is exact in the reviewer evidence, but the author's original source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched sequence's database annotation supports C; no supplied evidence supports another listed EC number."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0002",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the UniProt entry for selenate reductase subunit C, annotated with EC 1.97.1.14 and a selenate-reductase reaction. The annotation cites a study describing the respiratory selenate reductase complex. This supports choice C as the assigned EC number, though it does not establish that this membrane-anchor subunit alone catalyzes the reaction.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H1", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The strongly hydrophobic sequence is consistent with a multi-pass membrane protein, but that broad feature does not identify the specific selenate-reductase complex or distinguish its exact EC number from the alternatives.",
    "missing_item_specific_fact": "The protein-specific annotation identifying this sequence as subunit C of the selenate reductase complex and assigning that complex EC 1.97.1.14.",
    "reason": "The exact four-part EC assignment depends on a protein-specific functional annotation or experimental identification absent from the sequence and choices. General sequence reasoning does not meaningfully resolve the close EC alternatives."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched sequence's database annotation supports C; no supplied evidence supports another listed EC number."
  },
  "important_caveats": [
    "The UniProt annotation is a curated database claim citing a paper, not independent verification here of the primary experimental results.",
    "The EC number is assigned to the selenate-reductase activity of the complex; the sequence is annotated as its membrane-anchor subunit.",
    "The sequence match is exact in the reviewer evidence, but the author's original source snapshot is unknown."
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

> The sequence matches UniProt entry A0A0A8X338 (SRDC_MESS1), annotated as Selenate reductase subunit C with EC 1.97.1.14. The annotation carries evidence code ECO:0000305 (inferred by similarity) referencing PubMed:21357486 (Kuroda et al. 2011, characterization of the srdBCA operon). The catalytic reaction is selenite + a quinone + H2O = selenate + a quinol. The protein is the membrane anchor subunit of the respiratory selenate reductase complex. The key is supported by reviewed Swiss-Prot annotation, though the evidence code indicates similarity-based inference rather than direct experimental characterization of this specific subunit's catalytic activity.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The extreme hydrophobicity and predicted multi-pass transmembrane topology of the 426-aa sequence could weakly argue for a quinone-dependent (membrane-associated, EC 1.97.1.14) over a ferredoxin-dependent (soluble, EC 1.97.1.13) selenate reductase, and against soluble enzymes like dihydrofolate reductase (1.5.1.38). However, this argument only applies AFTER one has already identified the protein as a selenate/selenite reductase, which cannot be determined from the sequence alone without recognizing the specific protein or its homologs.


**Missing item-specific fact**

> The identification of this protein as a subunit of the selenate reductase (srd) complex requires recognition of the specific sequence or its close homologs. No catalytic motif, cofactor-binding signature, or unique sequence feature in the provided sequence reveals selenate reductase activity de novo. The assignment to EC 1.97.1.14 specifically (rather than 1.97.1.13 or any other oxidoreductase) depends on knowing this is the membrane anchor subunit of the quinone-dependent selenate reductase complex.


**Reason**

> While the membrane-anchoring topology provides a post-hoc rationalization for choosing quinone-dependent (1.97.1.14) over ferredoxin-dependent (1.97.1.13), the fundamental task of recognizing the protein as a selenate reductase at all requires sequence-level recognition or database lookup. The sequence lacks a distinctive catalytic motif that would allow a model to infer selenate reduction from general biological principles. Selection among the four options depends on item-specific knowledge of this protein's identity.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A (1.97.1.13) and C (1.97.1.14) are both selenate/selenite reductases; without knowing the specific protein, a model cannot definitively exclude 1.97.1.13 based solely on hydrophobicity, since some ferredoxin-dependent enzymes also associate with membranes."
]
```

> The distinction between 1.97.1.13 and 1.97.1.14 rests on whether the enzyme uses quinone (membrane-bound) or ferredoxin (soluble) as electron donor. The membrane topology weakly favors 1.97.1.14, but this is not definitive without knowing the protein's identity. Options B and D are more clearly eliminable as non-membrane or unrelated enzyme classes.


### Important caveats

- The UniProt annotation uses evidence code ECO:0000305 (inferred by similarity), meaning the EC assignment for this specific subunit C is based on similarity to the characterized srd complex rather than direct in vitro activity measurement of subunit C alone.
- The protein is described as a 'membrane anchor subunit,' suggesting its role is structural/anchoring rather than catalytic; the EC number refers to the complex activity rather than necessarily the subunit's own catalytic function.
- The sequence match to A0A0A8X338 is exact (426 aa, SHA256 matched), confirming the reviewer evidence applies to the benchmark sequence.
- The reviewer evidence is not available to the evaluated model; the model must work from the raw sequence alone.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The extreme hydrophobicity and predicted multi-pass transmembrane topology of the 426-aa sequence could weakly argue for a quinone-dependent (membrane-associated, EC 1.97.1.14) over a ferredoxin-dependent (soluble, EC 1.97.1.13) selenate reductase, and against soluble enzymes like dihydrofolate reductase (1.5.1.38). However, this argument only applies AFTER one has already identified the protein as a selenate/selenite reductase, which cannot be determined from the sequence alone without recognizing the specific protein or its homologs.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The identification of this protein as a subunit of the selenate reductase (srd) complex requires recognition of the specific sequence or its close homologs. No catalytic motif, cofactor-binding signature, or unique sequence feature in the provided sequence reveals selenate reductase activity de novo. The assignment to EC 1.97.1.14 specifically (rather than 1.97.1.13 or any other oxidoreductase) depends on knowing this is the membrane anchor subunit of the quinone-dependent selenate reductase complex.",
    "reason": "While the membrane-anchoring topology provides a post-hoc rationalization for choosing quinone-dependent (1.97.1.14) over ferredoxin-dependent (1.97.1.13), the fundamental task of recognizing the protein as a selenate reductase at all requires sequence-level recognition or database lookup. The sequence lacks a distinctive catalytic motif that would allow a model to infer selenate reduction from general biological principles. Selection among the four options depends on item-specific knowledge of this protein's identity."
  },
  "case_id": "EC_number_0002",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence matches UniProt entry A0A0A8X338 (SRDC_MESS1), annotated as Selenate reductase subunit C with EC 1.97.1.14. The annotation carries evidence code ECO:0000305 (inferred by similarity) referencing PubMed:21357486 (Kuroda et al. 2011, characterization of the srdBCA operon). The catalytic reaction is selenite + a quinone + H2O = selenate + a quinol. The protein is the membrane anchor subunit of the respiratory selenate reductase complex. The key is supported by reviewed Swiss-Prot annotation, though the evidence code indicates similarity-based inference rather than direct experimental characterization of this specific subunit's catalytic activity."
  },
  "important_caveats": [
    "The UniProt annotation uses evidence code ECO:0000305 (inferred by similarity), meaning the EC assignment for this specific subunit C is based on similarity to the characterized srd complex rather than direct in vitro activity measurement of subunit C alone.",
    "The protein is described as a 'membrane anchor subunit,' suggesting its role is structural/anchoring rather than catalytic; the EC number refers to the complex activity rather than necessarily the subunit's own catalytic function.",
    "The sequence match to A0A0A8X338 is exact (426 aa, SHA256 matched), confirming the reviewer evidence applies to the benchmark sequence.",
    "The reviewer evidence is not available to the evaluated model; the model must work from the raw sequence alone."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A (1.97.1.13) and C (1.97.1.14) are both selenate/selenite reductases; without knowing the specific protein, a model cannot definitively exclude 1.97.1.13 based solely on hydrophobicity, since some ferredoxin-dependent enzymes also associate with membranes."
    ],
    "reason": "The distinction between 1.97.1.13 and 1.97.1.14 rests on whether the enzyme uses quinone (membrane-bound) or ferredoxin (soluble) as electron donor. The membrane topology weakly favors 1.97.1.14, but this is not definitive without knowing the protein's identity. Options B and D are more clearly eliminable as non-membrane or unrelated enzyme classes."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0002",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches UniProt entry A0A0A8X338 (SRDC_MESS1), annotated as Selenate reductase subunit C with EC 1.97.1.14. The annotation carries evidence code ECO:0000305 (inferred by similarity) referencing PubMed:21357486 (Kuroda et al. 2011, characterization of the srdBCA operon). The catalytic reaction is selenite + a quinone + H2O = selenate + a quinol. The protein is the membrane anchor subunit of the respiratory selenate reductase complex. The key is supported by reviewed Swiss-Prot annotation, though the evidence code indicates similarity-based inference rather than direct experimental characterization of this specific subunit's catalytic activity.",
    "evidence_ids": ["C4", "C5", "C6", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The extreme hydrophobicity and predicted multi-pass transmembrane topology of the 426-aa sequence could weakly argue for a quinone-dependent (membrane-associated, EC 1.97.1.14) over a ferredoxin-dependent (soluble, EC 1.97.1.13) selenate reductase, and against soluble enzymes like dihydrofolate reductase (1.5.1.38). However, this argument only applies AFTER one has already identified the protein as a selenate/selenite reductase, which cannot be determined from the sequence alone without recognizing the specific protein or its homologs.",
    "missing_item_specific_fact": "The identification of this protein as a subunit of the selenate reductase (srd) complex requires recognition of the specific sequence or its close homologs. No catalytic motif, cofactor-binding signature, or unique sequence feature in the provided sequence reveals selenate reductase activity de novo. The assignment to EC 1.97.1.14 specifically (rather than 1.97.1.13 or any other oxidoreductase) depends on knowing this is the membrane anchor subunit of the quinone-dependent selenate reductase complex.",
    "reason": "While the membrane-anchoring topology provides a post-hoc rationalization for choosing quinone-dependent (1.97.1.14) over ferredoxin-dependent (1.97.1.13), the fundamental task of recognizing the protein as a selenate reductase at all requires sequence-level recognition or database lookup. The sequence lacks a distinctive catalytic motif that would allow a model to infer selenate reduction from general biological principles. Selection among the four options depends on item-specific knowledge of this protein's identity."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A (1.97.1.13) and C (1.97.1.14) are both selenate/selenite reductases; without knowing the specific protein, a model cannot definitively exclude 1.97.1.13 based solely on hydrophobicity, since some ferredoxin-dependent enzymes also associate with membranes."],
    "reason": "The distinction between 1.97.1.13 and 1.97.1.14 rests on whether the enzyme uses quinone (membrane-bound) or ferredoxin (soluble) as electron donor. The membrane topology weakly favors 1.97.1.14, but this is not definitive without knowing the protein's identity. Options B and D are more clearly eliminable as non-membrane or unrelated enzyme classes."
  },
  "important_caveats": [
    "The UniProt annotation uses evidence code ECO:0000305 (inferred by similarity), meaning the EC assignment for this specific subunit C is based on similarity to the characterized srd complex rather than direct in vitro activity measurement of subunit C alone.",
    "The protein is described as a 'membrane anchor subunit,' suggesting its role is structural/anchoring rather than catalytic; the EC number refers to the complex activity rather than necessarily the subunit's own catalytic function.",
    "The sequence match to A0A0A8X338 is exact (426 aa, SHA256 matched), confirming the reviewer evidence applies to the benchmark sequence.",
    "The reviewer evidence is not available to the evaluated model; the model must work from the raw sequence alone."
  ]
}
```

</details>

## After: GPT-6 Luna

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The exact sequence matches a UniProt entry annotated as selenate reductase subunit C with EC 1.97.1.14; the entry also assigns the selenate-reduction reaction to that EC and cites a paper on the respiratory selenate reductase complex.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence is strongly hydrophobic and consistent with a multi-pass membrane anchor, which suggests association with a membrane enzyme complex. But that broad feature does not identify the complex's substrate or distinguish EC 1.97.1.14 from the nearby alternative 1.97.1.13; the sequence lacks an evident catalytic domain that would resolve that distinction.


**Missing item-specific fact**

> The protein's specific assignment as the membrane-anchor subunit of a selenate reductase complex, whose reaction is assigned EC 1.97.1.14.


**Reason**

> A transferable inference supports a membrane-associated role, but not the specific reaction needed to choose between the closely related EC alternatives. The decisive link to selenate reductase is an annotation or experimentally established fact about this protein or its complex.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The supplied evidence supports the keyed EC number; it does not establish another offered option as equally defensible.


### Important caveats

- The EC number describes the selenate reductase complex's reaction, although the queried protein is annotated as its membrane-anchor subunit.
- The UniProt functional annotation is manually attributed to a cited publication; the excerpts do not independently demonstrate a purified-subunit catalytic assay.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is strongly hydrophobic and consistent with a multi-pass membrane anchor, which suggests association with a membrane enzyme complex. But that broad feature does not identify the complex's substrate or distinguish EC 1.97.1.14 from the nearby alternative 1.97.1.13; the sequence lacks an evident catalytic domain that would resolve that distinction.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein's specific assignment as the membrane-anchor subunit of a selenate reductase complex, whose reaction is assigned EC 1.97.1.14.",
    "reason": "A transferable inference supports a membrane-associated role, but not the specific reaction needed to choose between the closely related EC alternatives. The decisive link to selenate reductase is an annotation or experimentally established fact about this protein or its complex."
  },
  "case_id": "EC_number_0002",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry annotated as selenate reductase subunit C with EC 1.97.1.14; the entry also assigns the selenate-reduction reaction to that EC and cites a paper on the respiratory selenate reductase complex."
  },
  "important_caveats": [
    "The EC number describes the selenate reductase complex's reaction, although the queried protein is annotated as its membrane-anchor subunit.",
    "The UniProt functional annotation is manually attributed to a cited publication; the excerpts do not independently demonstrate a purified-subunit catalytic assay."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied evidence supports the keyed EC number; it does not establish another offered option as equally defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0002",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry annotated as selenate reductase subunit C with EC 1.97.1.14; the entry also assigns the selenate-reduction reaction to that EC and cites a paper on the respiratory selenate reductase complex.",
    "evidence_ids": ["C1", "C4", "C5", "C6"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence is strongly hydrophobic and consistent with a multi-pass membrane anchor, which suggests association with a membrane enzyme complex. But that broad feature does not identify the complex's substrate or distinguish EC 1.97.1.14 from the nearby alternative 1.97.1.13; the sequence lacks an evident catalytic domain that would resolve that distinction.",
    "missing_item_specific_fact": "The protein's specific assignment as the membrane-anchor subunit of a selenate reductase complex, whose reaction is assigned EC 1.97.1.14.",
    "reason": "A transferable inference supports a membrane-associated role, but not the specific reaction needed to choose between the closely related EC alternatives. The decisive link to selenate reductase is an annotation or experimentally established fact about this protein or its complex."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied evidence supports the keyed EC number; it does not establish another offered option as equally defensible."
  },
  "important_caveats": [
    "The EC number describes the selenate reductase complex's reaction, although the queried protein is annotated as its membrane-anchor subunit.",
    "The UniProt functional annotation is manually attributed to a cited publication; the excerpts do not independently demonstrate a purified-subunit catalytic assay."
  ]
}
```

</details>

## After: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry A0A0A8X338 annotates this protein as 'Selenate reductase subunit C' with EC 1.97.1.14. The catalytic activity (selenite + quinone + H2O = selenate + quinol) is listed with EC 1.97.1.14. The evidence code is ECO:0000305 (inferred by curator), based on the Kuroda et al. 2011 characterization of the srdBCA operon as encoding the respiratory selenate reductase complex. The subunit C is identified as the membrane anchor of that complex. The annotation is a curatorial assignment of the complex-level EC number to this subunit rather than direct experimental demonstration of catalysis by subunit C alone, but it is the recorded and supported annotation.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> Options B (1.5.1.38, CH-NH group oxidoreductase) and D (1.14.19.80, cytochrome P450 monooxygenase) can likely be eliminated by general knowledge: the sequence lacks P450 heme-binding motifs (FxxGxxxCxG) and shows no features of amino oxidoreductases. The sequence is clearly a polytopic membrane protein with multiple TM helices, a signal peptide, and conserved histidines suggestive of a cytochrome b-type membrane anchor of a respiratory complex. This narrows the choice to the 1.97.1.x family (options A and C). However, distinguishing 1.97.1.13 from 1.97.1.14 requires knowing the specific substrate (e.g., selenate vs. arsenite or another substrate) of the respiratory complex to which this membrane anchor belongs. The membrane anchor subunits of different respiratory complexes (srdC, aioC, napC, etc.) share overall cytochrome b-type architecture and TM topology, and no widely established, transferable sequence signature reliably distinguishes the selenate reductase membrane anchor from the arsenite oxidase membrane anchor or other 1.97.1.x members based on sequence alone.


**Missing item-specific fact**

> The specific identity of the enzyme complex (selenate reductase srdBCA) and the substrate specificity of the overall complex, which determines whether the EC number is 1.97.1.13 or 1.97.1.14. This is a fact about this particular protein's biological role and the organism's physiology (selenate-reducing bacterium), not derivable from general membrane-anchor sequence features.


**Reason**

> While the sequence allows elimination of B and D via general knowledge, and suggests a cytochrome b-type membrane anchor of a respiratory complex (narrowing to the 1.97.1.x family), the distinction between 1.97.1.13 and 1.97.1.14 requires knowing the specific substrate of the enzyme complex. The membrane anchor subunit itself does not catalyze the reaction; its EC assignment is curatorial (ECO:0000305). No well-known transferable sequence feature reliably distinguishes selenate reductase membrane anchors from other 1.97.1.x family membrane anchors without targeted knowledge of this specific complex.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "C"
]
```

> Both 1.97.1.13 and 1.97.1.14 are in the same EC subclass (1.97.1.x, 'Other oxidoreductases') and both could plausibly be membrane anchors of respiratory complexes with cytochrome b-type subunits. Without knowing the specific substrate of the complex, a model cannot reliably distinguish these two options from sequence alone.


### Important caveats

- The EC 1.97.1.14 annotation uses evidence code ECO:0000305 (inferred by curator), meaning the EC number was assigned to this subunit based on its membership in the selenate reductase complex rather than direct experimental demonstration of catalysis by subunit C alone.
- The protein is the membrane anchor subunit, not the catalytic subunit; the actual redox chemistry occurs at the SrdA catalytic subunit.
- The identity of EC 1.97.1.13 was not independently verified from the provided evidence; it is assumed to be a valid EC number in the same family.
- The organism (Mesobacillus selenatarsenatis) is known for selenate reduction, which provides contextual support for the annotation but was not given to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Options B (1.5.1.38, CH-NH group oxidoreductase) and D (1.14.19.80, cytochrome P450 monooxygenase) can likely be eliminated by general knowledge: the sequence lacks P450 heme-binding motifs (FxxGxxxCxG) and shows no features of amino oxidoreductases. The sequence is clearly a polytopic membrane protein with multiple TM helices, a signal peptide, and conserved histidines suggestive of a cytochrome b-type membrane anchor of a respiratory complex. This narrows the choice to the 1.97.1.x family (options A and C). However, distinguishing 1.97.1.13 from 1.97.1.14 requires knowing the specific substrate (e.g., selenate vs. arsenite or another substrate) of the respiratory complex to which this membrane anchor belongs. The membrane anchor subunits of different respiratory complexes (srdC, aioC, napC, etc.) share overall cytochrome b-type architecture and TM topology, and no widely established, transferable sequence signature reliably distinguishes the selenate reductase membrane anchor from the arsenite oxidase membrane anchor or other 1.97.1.x members based on sequence alone.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific identity of the enzyme complex (selenate reductase srdBCA) and the substrate specificity of the overall complex, which determines whether the EC number is 1.97.1.13 or 1.97.1.14. This is a fact about this particular protein's biological role and the organism's physiology (selenate-reducing bacterium), not derivable from general membrane-anchor sequence features.",
    "reason": "While the sequence allows elimination of B and D via general knowledge, and suggests a cytochrome b-type membrane anchor of a respiratory complex (narrowing to the 1.97.1.x family), the distinction between 1.97.1.13 and 1.97.1.14 requires knowing the specific substrate of the enzyme complex. The membrane anchor subunit itself does not catalyze the reaction; its EC assignment is curatorial (ECO:0000305). No well-known transferable sequence feature reliably distinguishes selenate reductase membrane anchors from other 1.97.1.x family membrane anchors without targeted knowledge of this specific complex."
  },
  "case_id": "EC_number_0002",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "UniProt entry A0A0A8X338 annotates this protein as 'Selenate reductase subunit C' with EC 1.97.1.14. The catalytic activity (selenite + quinone + H2O = selenate + quinol) is listed with EC 1.97.1.14. The evidence code is ECO:0000305 (inferred by curator), based on the Kuroda et al. 2011 characterization of the srdBCA operon as encoding the respiratory selenate reductase complex. The subunit C is identified as the membrane anchor of that complex. The annotation is a curatorial assignment of the complex-level EC number to this subunit rather than direct experimental demonstration of catalysis by subunit C alone, but it is the recorded and supported annotation."
  },
  "important_caveats": [
    "The EC 1.97.1.14 annotation uses evidence code ECO:0000305 (inferred by curator), meaning the EC number was assigned to this subunit based on its membership in the selenate reductase complex rather than direct experimental demonstration of catalysis by subunit C alone.",
    "The protein is the membrane anchor subunit, not the catalytic subunit; the actual redox chemistry occurs at the SrdA catalytic subunit.",
    "The identity of EC 1.97.1.13 was not independently verified from the provided evidence; it is assumed to be a valid EC number in the same family.",
    "The organism (Mesobacillus selenatarsenatis) is known for selenate reduction, which provides contextual support for the annotation but was not given to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "C"
    ],
    "reason": "Both 1.97.1.13 and 1.97.1.14 are in the same EC subclass (1.97.1.x, 'Other oxidoreductases') and both could plausibly be membrane anchors of respiratory complexes with cytochrome b-type subunits. Without knowing the specific substrate of the complex, a model cannot reliably distinguish these two options from sequence alone."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0002",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry A0A0A8X338 annotates this protein as 'Selenate reductase subunit C' with EC 1.97.1.14. The catalytic activity (selenite + quinone + H2O = selenate + quinol) is listed with EC 1.97.1.14. The evidence code is ECO:0000305 (inferred by curator), based on the Kuroda et al. 2011 characterization of the srdBCA operon as encoding the respiratory selenate reductase complex. The subunit C is identified as the membrane anchor of that complex. The annotation is a curatorial assignment of the complex-level EC number to this subunit rather than direct experimental demonstration of catalysis by subunit C alone, but it is the recorded and supported annotation.",
    "evidence_ids": ["C4", "C5", "C6", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "Options B (1.5.1.38, CH-NH group oxidoreductase) and D (1.14.19.80, cytochrome P450 monooxygenase) can likely be eliminated by general knowledge: the sequence lacks P450 heme-binding motifs (FxxGxxxCxG) and shows no features of amino oxidoreductases. The sequence is clearly a polytopic membrane protein with multiple TM helices, a signal peptide, and conserved histidines suggestive of a cytochrome b-type membrane anchor of a respiratory complex. This narrows the choice to the 1.97.1.x family (options A and C). However, distinguishing 1.97.1.13 from 1.97.1.14 requires knowing the specific substrate (e.g., selenate vs. arsenite or another substrate) of the respiratory complex to which this membrane anchor belongs. The membrane anchor subunits of different respiratory complexes (srdC, aioC, napC, etc.) share overall cytochrome b-type architecture and TM topology, and no widely established, transferable sequence signature reliably distinguishes the selenate reductase membrane anchor from the arsenite oxidase membrane anchor or other 1.97.1.x members based on sequence alone.",
    "missing_item_specific_fact": "The specific identity of the enzyme complex (selenate reductase srdBCA) and the substrate specificity of the overall complex, which determines whether the EC number is 1.97.1.13 or 1.97.1.14. This is a fact about this particular protein's biological role and the organism's physiology (selenate-reducing bacterium), not derivable from general membrane-anchor sequence features.",
    "reason": "While the sequence allows elimination of B and D via general knowledge, and suggests a cytochrome b-type membrane anchor of a respiratory complex (narrowing to the 1.97.1.x family), the distinction between 1.97.1.13 and 1.97.1.14 requires knowing the specific substrate of the enzyme complex. The membrane anchor subunit itself does not catalyze the reaction; its EC assignment is curatorial (ECO:0000305). No well-known transferable sequence feature reliably distinguishes selenate reductase membrane anchors from other 1.97.1.x family membrane anchors without targeted knowledge of this specific complex."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "C"],
    "reason": "Both 1.97.1.13 and 1.97.1.14 are in the same EC subclass (1.97.1.x, 'Other oxidoreductases') and both could plausibly be membrane anchors of respiratory complexes with cytochrome b-type subunits. Without knowing the specific substrate of the complex, a model cannot reliably distinguish these two options from sequence alone."
  },
  "important_caveats": [
    "The EC 1.97.1.14 annotation uses evidence code ECO:0000305 (inferred by curator), meaning the EC number was assigned to this subunit based on its membership in the selenate reductase complex rather than direct experimental demonstration of catalysis by subunit C alone.",
    "The protein is the membrane anchor subunit, not the catalytic subunit; the actual redox chemistry occurs at the SrdA catalytic subunit.",
    "The identity of EC 1.97.1.13 was not independently verified from the provided evidence; it is assumed to be a valid EC number in the same family.",
    "The organism (Mesobacillus selenatarsenatis) is known for selenate reduction, which provides contextual support for the annotation but was not given to the evaluated model."
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
  "requested_accession": "A0A0A8X338",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "benchmark_sequence_sha256": "218a8fc8c9a5550707cff8e4e71529fa4d0cadfec3371e5a9738f79c411a7e67",
  "benchmark_sequence_length": 426,
  "current_status": "retrieved",
  "current_sequence_comparison": "matched",
  "current_entry_audit": {
    "entryVersion": 28,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2015-03-04",
    "sequenceVersion": 1
  },
  "current_uniprot_release": "2026_03",
  "current_record_sha256": "f24d48c67ebe30dab27bb776e276107f0f50c197edcf4849b2ea2624ac4d4bbe",
  "current_source_sequence_sha256": "218a8fc8c9a5550707cff8e4e71529fa4d0cadfec3371e5a9738f79c411a7e67",
  "current_source_sequence_length": 426,
  "historical_status": "retrieved",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "selected_historical_entry_version": 26,
  "selected_historical_version": {
    "accession": "A0A0A8X338",
    "database": "Swiss-Prot",
    "entryVersion": 26,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "SRDC_MESS1",
    "sequenceVersion": 1
  },
  "selected_historical_record_sha256": "eb155874ab7c90cb9f9b357a382d734672b54b5376824079e6a394ed2c9dea57",
  "selected_historical_source_sequence_sha256": "218a8fc8c9a5550707cff8e4e71529fa4d0cadfec3371e5a9738f79c411a7e67",
  "selected_historical_source_sequence_length": 426,
  "latest_at_cutoff_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 26,
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0A8X338.json)

```json
{
  "evidence_id": "C1",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0A8X338.json",
  "source_sha256": "f24d48c67ebe30dab27bb776e276107f0f50c197edcf4849b2ea2624ac4d4bbe",
  "retrieved_utc": "2026-11-02T04:23:56.888485+00:00",
  "json_pointer": "/primaryAccession",
  "excerpt": "\"A0A0A8X338\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0A8X338.json)

```json
{
  "evidence_id": "C2",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0A8X338.json",
  "source_sha256": "f24d48c67ebe30dab27bb776e276107f0f50c197edcf4849b2ea2624ac4d4bbe",
  "retrieved_utc": "2026-11-02T04:23:56.888485+00:00",
  "json_pointer": "/entryAudit",
  "excerpt": "{\"entryVersion\":28,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2015-03-04\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0A8X338.json)

```json
{
  "evidence_id": "C3",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0A8X338.json",
  "source_sha256": "f24d48c67ebe30dab27bb776e276107f0f50c197edcf4849b2ea2624ac4d4bbe",
  "retrieved_utc": "2026-11-02T04:23:56.888485+00:00",
  "json_pointer": "/organism",
  "excerpt": "{\"lineage\":[\"Bacteria\",\"Bacillati\",\"Bacillota\",\"Bacilli\",\"Caryophanales\",\"Bacillaceae\",\"Mesobacillus\"],\"scientificName\":\"Mesobacillus selenatarsenatis (strain DSM 18680 / JCM 14380 / FERM P-15431 / SF-1)\",\"taxonId\":1321606}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0A8X338.json)

```json
{
  "evidence_id": "C4",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0A8X338.json",
  "source_sha256": "f24d48c67ebe30dab27bb776e276107f0f50c197edcf4849b2ea2624ac4d4bbe",
  "retrieved_utc": "2026-11-02T04:23:56.888485+00:00",
  "json_pointer": "/proteinDescription",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Selenate reductase membrane anchor subunit\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"21357486\",\"source\":\"PubMed\"}],\"value\":\"1.97.1.14\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Selenate reductase subunit C\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0A8X338.json)

```json
{
  "evidence_id": "C5",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0A8X338.json",
  "source_sha256": "f24d48c67ebe30dab27bb776e276107f0f50c197edcf4849b2ea2624ac4d4bbe",
  "retrieved_utc": "2026-11-02T04:23:56.888485+00:00",
  "json_pointer": "/comments/1",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"ecNumber\":\"1.97.1.14\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"21357486\",\"source\":\"PubMed\"}],\"name\":\"selenite + a quinone + H2O = selenate + a quinol\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:51636\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15075\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:18212\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:24646\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:132124\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0A8X338.json)

```json
{
  "evidence_id": "C6",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0A8X338.json",
  "source_sha256": "f24d48c67ebe30dab27bb776e276107f0f50c197edcf4849b2ea2624ac4d4bbe",
  "retrieved_utc": "2026-11-02T04:23:56.888485+00:00",
  "json_pointer": "/references/0",
  "excerpt": "{\"citation\":{\"authors\":[\"Kuroda M.\",\"Yamashita M.\",\"Miwa E.\",\"Imao K.\",\"Fujimoto N.\",\"Ono H.\",\"Nagano K.\",\"Sei K.\",\"Ike M.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"21357486\"},{\"database\":\"DOI\",\"id\":\"10.1128/jb.01197-10\"}],\"citationType\":\"journal article\",\"firstPage\":\"2141\",\"id\":\"21357486\",\"journal\":\"J. Bacteriol.\",\"lastPage\":\"2148\",\"publicationDate\":\"2011\",\"title\":\"Molecular cloning and characterization of the srdBCA operon, encoding the respiratory selenate reductase complex, from the selenate-reducing bacterium Bacillus selenatarsenatis SF-1.\",\"volume\":\"193\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"BAJ83593.1\",\"source\":\"EMBL\"}],\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"DSM 18680 / JCM 14380 / FERM P-15431 / SF-1\"}],\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [GENOMIC DNA]\",\"FUNCTION AS A SELENATE REDUCTASE\",\"SUBUNIT\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0A8X338?format=txt&versions=26)

```json
{
  "evidence_id": "H1",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A0A8X338?format=txt&versions=26",
  "source_sha256": "eb155874ab7c90cb9f9b357a382d734672b54b5376824079e6a394ed2c9dea57",
  "retrieved_utc": "2026-11-02T04:24:00.225132+00:00",
  "source_locator": "lines 1-15",
  "excerpt": "ID   SRDC_MESS1              Reviewed;         426 AA.\nAC   A0A0A8X338; E9RFD0;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   04-MAR-2015, sequence version 1.\nDT   28-JAN-2026, entry version 26.\nDE   RecName: Full=Selenate reductase subunit C {ECO:0000305};\nDE            EC=1.97.1.14 {ECO:0000305|PubMed:21357486};\nDE   AltName: Full=Selenate reductase membrane anchor subunit {ECO:0000305};\nGN   Name=srdC {ECO:0000303|PubMed:21357486};\nGN   ORFNames=SAMD00020551_1551 {ECO:0000312|EMBL:GAM13407.1};\nOS   Mesobacillus selenatarsenatis (strain DSM 18680 / JCM 14380 / FERM P-15431\nOS   / SF-1).\nOC   Bacteria; Bacillati; Bacillota; Bacilli; Bacillales; Bacillaceae;\nOC   Mesobacillus.\nOX   NCBI_TaxID=1321606;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 26,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0A8X338?format=txt&versions=26)

```json
{
  "evidence_id": "H2",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A0A8X338?format=txt&versions=26",
  "source_sha256": "eb155874ab7c90cb9f9b357a382d734672b54b5376824079e6a394ed2c9dea57",
  "retrieved_utc": "2026-11-02T04:24:00.225132+00:00",
  "source_locator": "lines 6-8",
  "excerpt": "DE   RecName: Full=Selenate reductase subunit C {ECO:0000305};\nDE            EC=1.97.1.14 {ECO:0000305|PubMed:21357486};\nDE   AltName: Full=Selenate reductase membrane anchor subunit {ECO:0000305};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 26,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0A8X338?format=txt&versions=26)

```json
{
  "evidence_id": "H3",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A0A8X338?format=txt&versions=26",
  "source_sha256": "eb155874ab7c90cb9f9b357a382d734672b54b5376824079e6a394ed2c9dea57",
  "retrieved_utc": "2026-11-02T04:24:00.225132+00:00",
  "source_locator": "lines 16-26",
  "excerpt": "RN   [1] {ECO:0000312|EMBL:BAJ83593.1}\nRP   NUCLEOTIDE SEQUENCE [GENOMIC DNA], FUNCTION AS A SELENATE REDUCTASE, AND\nRP   SUBUNIT.\nRC   STRAIN=DSM 18680 / JCM 14380 / FERM P-15431 / SF-1;\nRX   PubMed=21357486; DOI=10.1128/jb.01197-10;\nRA   Kuroda M., Yamashita M., Miwa E., Imao K., Fujimoto N., Ono H., Nagano K.,\nRA   Sei K., Ike M.;\nRT   \"Molecular cloning and characterization of the srdBCA operon, encoding the\nRT   respiratory selenate reductase complex, from the selenate-reducing\nRT   bacterium Bacillus selenatarsenatis SF-1.\";\nRL   J. Bacteriol. 193:2141-2148(2011).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 26,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0A8X338?format=txt&versions=26)

```json
{
  "evidence_id": "H4",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A0A8X338?format=txt&versions=26",
  "source_sha256": "eb155874ab7c90cb9f9b357a382d734672b54b5376824079e6a394ed2c9dea57",
  "retrieved_utc": "2026-11-02T04:24:00.225132+00:00",
  "source_locator": "lines 43-47",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=selenite + a quinone + H2O = selenate + a quinol;\nCC         Xref=Rhea:RHEA:51636, ChEBI:CHEBI:15075, ChEBI:CHEBI:15377,\nCC         ChEBI:CHEBI:18212, ChEBI:CHEBI:24646, ChEBI:CHEBI:132124;\nCC         EC=1.97.1.14; Evidence={ECO:0000305|PubMed:21357486};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 26,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 2. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
