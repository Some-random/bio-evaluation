# EC_number_0038: before and after transfer clarification

[All 1,328 cases](../README.md) · [Method](../METHOD.md) · [Summary](../SUMMARY.md) · [Exact reviewer user message](../inputs/EC_number_0038.txt)

**Task:** `EC_number`  
**Author key, unchanged:** **C** — 2.4.1.259

| Round | Reviewer | Key support | Transfer / lookup | Output usability (canonical status) |
|---|---|---|---|---|
| before | GPT-6 Luna | supported | lookup-dependent | usable output (valid_review) |
| before | Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | usable output (valid_review) |
| after | GPT-6 Luna | supported | reasoning-supported | usable output (valid_review) |
| after | Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | usable output (valid_review) |

**Usable output means format-valid review, not reasoning-supported or biologically correct.** A usable output can classify the question as reasoning-supported, lookup-dependent or uncertain. An output error is a problem with the saved model response; it does not count a defective benchmark question or wrong key. Each saved review is retained in full below. Labels from output errors are displayed as saved and excluded from label statistics. The author key and reviewer evidence were visible to reviewers; this is a review of answerability and key support, not a benchmark-solving score.

## Complete original question

```text
[Protein Sequence]
MAPPAARARYIANKADNQILSKKPPKRPGLNGNNKTKEATPAGKKKDKDAKKRNQPTSGGQEKGLPNPIMPSVQTAFKTFVSARLCSAIWAYIADCDETFNYWEPLHYIINGHGLQTWEYSPQFGLRSYTYLLLQGVPGYFYQKLFNPSPILIFYMVRCMLGFGCAVMERYMYKSICQEFGIHIGRLWLIFQLFSVGMFVSSTALLPSSFSMYFGCAALAAWWQQNYCFAIFLTAISALLGWPFAALIGIPLVLEMLLRQRDWKTFVQWTLISGATVAIPMIAIDTSYFGKLTFAPLNIVWYNVFTSHGPNIFGTEPLSYYIINGFLNFNIIWLLALQLPIMLVIDYLIVPAKSKSTLNFPHYISLAPLYLWLLVFFAQPHKEERFLFPIYPLISLCGAITVDVYQRIFFRMKSVVFKIKAGVHYLDHSMFIAILVMVTSTLLGLSRVFALYRNYHAPMDLMLELNQFKATPQYDPDVIYNVCIGKDWHRYPGSFFFPAKNFRLRFLKSEFRGMLPAYYDEGQNATKVVQPYFNDLNQENEHMYFDYDRCDFLVDFDEGKYTALEPNYSKRSKDWSVMKSLPFLIPEKSHKVLRAFYVPFLTDNHIQYGDFNLLKRKTKRNGR

[Multiple Choices]
A. 2.4.1.392
B. 4.2.1.70
C. 2.4.1.259
D. 2.3.1.319
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

> The exact sequence matches the Drosophila Alg9 record, which annotates EC 2.4.1.259 and describes the corresponding mannosyltransferase reaction. This support is transferred by similarity from Q9H6U8 (ECO:0000250), not evidence of direct experimental characterization of this exact protein.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H1](#evidence-h1), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence is consistent with a multipass membrane glycosyltransferase, but that broad inference does not determine its precise glycan substrate, reaction, or complete EC number.


**Missing item-specific fact**

> Identifying this protein as Alg9 and knowing its specific annotated mannosyltransferase activities requires protein-specific functional annotation or experimental knowledge absent from the input.


**Reason**

> The exact EC distinction among the choices depends on the specific reaction catalyzed, which cannot be established from the sequence and choices by general biological reasoning alone.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the listed choices, the evidence supports C. The matched record also annotates EC 2.4.1.261 for a second reaction, but that number is not offered as an option.


### Important caveats

- The supporting EC annotations are similarity-based transfers, not direct experimental evidence for the supplied Drosophila protein.
- The exact author data snapshot is unknown, though the matched historical record available by the stated cutoff includes EC 2.4.1.259.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with a multipass membrane glycosyltransferase, but that broad inference does not determine its precise glycan substrate, reaction, or complete EC number.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "Identifying this protein as Alg9 and knowing its specific annotated mannosyltransferase activities requires protein-specific functional annotation or experimental knowledge absent from the input.",
    "reason": "The exact EC distinction among the choices depends on the specific reaction catalyzed, which cannot be established from the sequence and choices by general biological reasoning alone."
  },
  "case_id": "EC_number_0038",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H1",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the Drosophila Alg9 record, which annotates EC 2.4.1.259 and describes the corresponding mannosyltransferase reaction. This support is transferred by similarity from Q9H6U8 (ECO:0000250), not evidence of direct experimental characterization of this exact protein."
  },
  "important_caveats": [
    "The supporting EC annotations are similarity-based transfers, not direct experimental evidence for the supplied Drosophila protein.",
    "The exact author data snapshot is unknown, though the matched historical record available by the stated cutoff includes EC 2.4.1.259."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed choices, the evidence supports C. The matched record also annotates EC 2.4.1.261 for a second reaction, but that number is not offered as an option."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0038",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the Drosophila Alg9 record, which annotates EC 2.4.1.259 and describes the corresponding mannosyltransferase reaction. This support is transferred by similarity from Q9H6U8 (ECO:0000250), not evidence of direct experimental characterization of this exact protein.",
    "evidence_ids": ["C1", "C4", "C5", "H1", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence is consistent with a multipass membrane glycosyltransferase, but that broad inference does not determine its precise glycan substrate, reaction, or complete EC number.",
    "missing_item_specific_fact": "Identifying this protein as Alg9 and knowing its specific annotated mannosyltransferase activities requires protein-specific functional annotation or experimental knowledge absent from the input.",
    "reason": "The exact EC distinction among the choices depends on the specific reaction catalyzed, which cannot be established from the sequence and choices by general biological reasoning alone."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed choices, the evidence supports C. The matched record also annotates EC 2.4.1.261 for a second reaction, but that number is not offered as an option."
  },
  "important_caveats": [
    "The supporting EC annotations are similarity-based transfers, not direct experimental evidence for the supplied Drosophila protein.",
    "The exact author data snapshot is unknown, though the matched historical record available by the stated cutoff includes EC 2.4.1.259."
  ]
}
```

</details>

## Before: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence matches UniProt Q9VBV8 (ALG9_DROME, Drosophila melanogaster Alpha-1,2-mannosyltransferase Alg9) exactly (623 AA, SHA256 confirmed). The UniProt entry assigns EC 2.4.1.259 (and also EC 2.4.1.261) with evidence code ECO:0000250 (inferred by similarity from human Q9H6U8). Among the four choices, only 2.4.1.259 (option C) appears in the annotation. The other options (2.4.1.392, 4.2.1.70, 2.3.1.319) are unrelated EC numbers. The annotation is computational (transferred by similarity), not direct experimental evidence for the Drosophila protein, but it is the official database assignment.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> One could note the protein is a polytopic membrane protein with multiple hydrophobic segments consistent with an ER-resident enzyme, and might infer it belongs to the transferase class (EC 2) rather than lyase (EC 4), eliminating option B. However, distinguishing EC 2.4.1.259 (alpha-1,2-mannosyltransferase Alg9, GT47 family) from EC 2.4.1.392 (another glycosyltransferase) and EC 2.3.1.319 (acyltransferase) requires knowing the specific protein family, its role in the dolichol-linked N-glycan biosynthesis pathway (adding the 6th mannose to Man5GlcNAc2-PP-dolichol), and the exact EC assignment. No general sequence motif or biochemical reasoning from the raw 623-aa sequence alone reliably distinguishes these four specific EC numbers.


**Missing item-specific fact**

> The specific identity of this sequence as Alg9 (Drosophila ortholog of human DPAGT1-pathway mannosyltransferase) and the knowledge that Alg9 catalyzes the alpha-1,2-mannosyl transfer step designated EC 2.4.1.259 (as opposed to other glycosyltransferase EC numbers in the choices). This is a protein-specific database annotation.


**Reason**

> While the transferase vs. lyase distinction (eliminating B) is somewhat accessible, the precise 4-digit EC assignment among three transferase options (A, C, D) requires recognizing this as Alg9 and recalling its specific EC number. This is fundamentally a sequence-to-annotation lookup task, not a reasoning task from general biochemistry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Although the UniProt entry annotates both EC 2.4.1.259 and EC 2.4.1.261, only 2.4.1.259 appears among the four choices. None of the distractors match any annotation for this protein. Thus, among the given options, only C is defensible.


### Important caveats

- The EC assignment carries evidence code ECO:0000250 (inferred by similarity from human Q9H6U8), not direct experimental characterization of the Drosophila protein.
- The protein is annotated with a second EC number (2.4.1.261) for a later step in the same pathway; the question asks for 'the' EC number (singular), which is slightly imprecise, but this does not affect answer selection since 2.4.1.261 is not a choice.
- The UniProt entry was first public in 2025-06-18 (Swiss-Prot reviewed status); the benchmark's author source snapshot is unknown but the sequence has been unchanged since 2000.
- The accession identity was inferred by the reviewer from dataset metadata, not provided to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "One could note the protein is a polytopic membrane protein with multiple hydrophobic segments consistent with an ER-resident enzyme, and might infer it belongs to the transferase class (EC 2) rather than lyase (EC 4), eliminating option B. However, distinguishing EC 2.4.1.259 (alpha-1,2-mannosyltransferase Alg9, GT47 family) from EC 2.4.1.392 (another glycosyltransferase) and EC 2.3.1.319 (acyltransferase) requires knowing the specific protein family, its role in the dolichol-linked N-glycan biosynthesis pathway (adding the 6th mannose to Man5GlcNAc2-PP-dolichol), and the exact EC assignment. No general sequence motif or biochemical reasoning from the raw 623-aa sequence alone reliably distinguishes these four specific EC numbers.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific identity of this sequence as Alg9 (Drosophila ortholog of human DPAGT1-pathway mannosyltransferase) and the knowledge that Alg9 catalyzes the alpha-1,2-mannosyl transfer step designated EC 2.4.1.259 (as opposed to other glycosyltransferase EC numbers in the choices). This is a protein-specific database annotation.",
    "reason": "While the transferase vs. lyase distinction (eliminating B) is somewhat accessible, the precise 4-digit EC assignment among three transferase options (A, C, D) requires recognizing this as Alg9 and recalling its specific EC number. This is fundamentally a sequence-to-annotation lookup task, not a reasoning task from general biochemistry."
  },
  "case_id": "EC_number_0038",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H1",
      "H2",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The sequence matches UniProt Q9VBV8 (ALG9_DROME, Drosophila melanogaster Alpha-1,2-mannosyltransferase Alg9) exactly (623 AA, SHA256 confirmed). The UniProt entry assigns EC 2.4.1.259 (and also EC 2.4.1.261) with evidence code ECO:0000250 (inferred by similarity from human Q9H6U8). Among the four choices, only 2.4.1.259 (option C) appears in the annotation. The other options (2.4.1.392, 4.2.1.70, 2.3.1.319) are unrelated EC numbers. The annotation is computational (transferred by similarity), not direct experimental evidence for the Drosophila protein, but it is the official database assignment."
  },
  "important_caveats": [
    "The EC assignment carries evidence code ECO:0000250 (inferred by similarity from human Q9H6U8), not direct experimental characterization of the Drosophila protein.",
    "The protein is annotated with a second EC number (2.4.1.261) for a later step in the same pathway; the question asks for 'the' EC number (singular), which is slightly imprecise, but this does not affect answer selection since 2.4.1.261 is not a choice.",
    "The UniProt entry was first public in 2025-06-18 (Swiss-Prot reviewed status); the benchmark's author source snapshot is unknown but the sequence has been unchanged since 2000.",
    "The accession identity was inferred by the reviewer from dataset metadata, not provided to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although the UniProt entry annotates both EC 2.4.1.259 and EC 2.4.1.261, only 2.4.1.259 appears among the four choices. None of the distractors match any annotation for this protein. Thus, among the given options, only C is defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0038",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches UniProt Q9VBV8 (ALG9_DROME, Drosophila melanogaster Alpha-1,2-mannosyltransferase Alg9) exactly (623 AA, SHA256 confirmed). The UniProt entry assigns EC 2.4.1.259 (and also EC 2.4.1.261) with evidence code ECO:0000250 (inferred by similarity from human Q9H6U8). Among the four choices, only 2.4.1.259 (option C) appears in the annotation. The other options (2.4.1.392, 4.2.1.70, 2.3.1.319) are unrelated EC numbers. The annotation is computational (transferred by similarity), not direct experimental evidence for the Drosophila protein, but it is the official database assignment.",
    "evidence_ids": ["C4", "C5", "H1", "H2", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "One could note the protein is a polytopic membrane protein with multiple hydrophobic segments consistent with an ER-resident enzyme, and might infer it belongs to the transferase class (EC 2) rather than lyase (EC 4), eliminating option B. However, distinguishing EC 2.4.1.259 (alpha-1,2-mannosyltransferase Alg9, GT47 family) from EC 2.4.1.392 (another glycosyltransferase) and EC 2.3.1.319 (acyltransferase) requires knowing the specific protein family, its role in the dolichol-linked N-glycan biosynthesis pathway (adding the 6th mannose to Man5GlcNAc2-PP-dolichol), and the exact EC assignment. No general sequence motif or biochemical reasoning from the raw 623-aa sequence alone reliably distinguishes these four specific EC numbers.",
    "missing_item_specific_fact": "The specific identity of this sequence as Alg9 (Drosophila ortholog of human DPAGT1-pathway mannosyltransferase) and the knowledge that Alg9 catalyzes the alpha-1,2-mannosyl transfer step designated EC 2.4.1.259 (as opposed to other glycosyltransferase EC numbers in the choices). This is a protein-specific database annotation.",
    "reason": "While the transferase vs. lyase distinction (eliminating B) is somewhat accessible, the precise 4-digit EC assignment among three transferase options (A, C, D) requires recognizing this as Alg9 and recalling its specific EC number. This is fundamentally a sequence-to-annotation lookup task, not a reasoning task from general biochemistry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although the UniProt entry annotates both EC 2.4.1.259 and EC 2.4.1.261, only 2.4.1.259 appears among the four choices. None of the distractors match any annotation for this protein. Thus, among the given options, only C is defensible."
  },
  "important_caveats": [
    "The EC assignment carries evidence code ECO:0000250 (inferred by similarity from human Q9H6U8), not direct experimental characterization of the Drosophila protein.",
    "The protein is annotated with a second EC number (2.4.1.261) for a later step in the same pathway; the question asks for 'the' EC number (singular), which is slightly imprecise, but this does not affect answer selection since 2.4.1.261 is not a choice.",
    "The UniProt entry was first public in 2025-06-18 (Swiss-Prot reviewed status); the benchmark's author source snapshot is unknown but the sequence has been unchanged since 2000.",
    "The accession identity was inferred by the reviewer from dataset metadata, not provided to the evaluated model."
  ]
}
```

</details>

## After: GPT-6 Luna

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence-matched historical UniProt record assigns EC 2.4.1.259, supporting choice C. This is a transferred annotation based on similarity, not direct experimental evidence in the supplied excerpts. The record also assigns EC 2.4.1.261, which is not among the choices.

Citations as saved: [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The long, highly hydrophobic sequence is consistent with a multipass membrane enzyme involved in lipid-linked oligosaccharide processing. Recognition of the conserved Alg9-like mannosyltransferase family from sequence similarity provides a transferable basis for favoring an alpha-1,2-mannosyltransferase option such as C over the lyase and acyltransferase choices, and distinguishes it from an unrelated transferase option.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A family-level inference from the sequence can meaningfully distinguish choice C among the offered alternatives without relying on the exact protein's database record. The sequence's membrane topology alone would not establish the detailed reaction, so the inference depends on recognizing conserved family similarity.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Only C among the listed choices is supported by the sequence-matched annotation. The protein is additionally assigned EC 2.4.1.261, but that number is not offered.


### Important caveats

- The cited EC assignments are transferred by similarity rather than shown here as direct experimental findings for this protein.
- The question asks for a complete EC number in the singular, while the record assigns two EC numbers; only one is included in the choices.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The long, highly hydrophobic sequence is consistent with a multipass membrane enzyme involved in lipid-linked oligosaccharide processing. Recognition of the conserved Alg9-like mannosyltransferase family from sequence similarity provides a transferable basis for favoring an alpha-1,2-mannosyltransferase option such as C over the lyase and acyltransferase choices, and distinguishes it from an unrelated transferase option.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A family-level inference from the sequence can meaningfully distinguish choice C among the offered alternatives without relying on the exact protein's database record. The sequence's membrane topology alone would not establish the detailed reaction, so the inference depends on recognizing conserved family similarity."
  },
  "case_id": "EC_number_0038",
  "expected_answer_check": {
    "evidence_ids": [
      "H2",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched historical UniProt record assigns EC 2.4.1.259, supporting choice C. This is a transferred annotation based on similarity, not direct experimental evidence in the supplied excerpts. The record also assigns EC 2.4.1.261, which is not among the choices."
  },
  "important_caveats": [
    "The cited EC assignments are transferred by similarity rather than shown here as direct experimental findings for this protein.",
    "The question asks for a complete EC number in the singular, while the record assigns two EC numbers; only one is included in the choices."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only C among the listed choices is supported by the sequence-matched annotation. The protein is additionally assigned EC 2.4.1.261, but that number is not offered."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0038",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched historical UniProt record assigns EC 2.4.1.259, supporting choice C. This is a transferred annotation based on similarity, not direct experimental evidence in the supplied excerpts. The record also assigns EC 2.4.1.261, which is not among the choices.",
    "evidence_ids": ["H2", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The long, highly hydrophobic sequence is consistent with a multipass membrane enzyme involved in lipid-linked oligosaccharide processing. Recognition of the conserved Alg9-like mannosyltransferase family from sequence similarity provides a transferable basis for favoring an alpha-1,2-mannosyltransferase option such as C over the lyase and acyltransferase choices, and distinguishes it from an unrelated transferase option.",
    "missing_item_specific_fact": "",
    "reason": "A family-level inference from the sequence can meaningfully distinguish choice C among the offered alternatives without relying on the exact protein's database record. The sequence's membrane topology alone would not establish the detailed reaction, so the inference depends on recognizing conserved family similarity."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only C among the listed choices is supported by the sequence-matched annotation. The protein is additionally assigned EC 2.4.1.261, but that number is not offered."
  },
  "important_caveats": [
    "The cited EC assignments are transferred by similarity rather than shown here as direct experimental findings for this protein.",
    "The question asks for a complete EC number in the singular, while the record assigns two EC numbers; only one is included in the choices."
  ]
}
```

</details>

## After: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry Q9VBV8 (ALG9_DROME) lists EC=2.4.1.259 as the primary EC number for Alpha-1,2-mannosyltransferase Alg9, with the catalytic activity describing the transfer of an alpha-1,2-linked mannose from dolichyl-P-Man to the Man6GlcNAc2-PP-dolichol acceptor (Rhea:RHEA:29531). The evidence code is ECO:0000250 (inferred by similarity to human Alg9 Q9H6U8), which is computational transfer rather than direct experimental measurement, but the annotation is consistent and the EC number is the standard assignment for Alg9. The entry also carries EC=2.4.1.261 as a secondary activity, but that EC is not among the offered choices, so it does not contradict choice C.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 623-aa sequence contains approximately 10+ hydrophobic segments consistent with a multi-pass transmembrane ER-resident glycosyltransferase, the hallmark architecture of Alg9 (alpha-1,2-mannosyltransferase) in the N-glycan biosynthesis pathway. Alg9 is one of the most well-characterized enzymes in the dolichol-linked oligosaccharide assembly pathway across yeast, human, Drosophila, and other model organisms. A knowledgeable model can recognize the multi-TM topology, overall length (~600 aa), and conserved sequence motifs as characteristic of the Alg9 family. Knowing that Alg9 catalyzes the alpha-1,2-mannosyltransferase step (EC 2.4.1.259) is standard N-glycan biosynthesis pathway knowledge, analogous to knowing hexokinase is EC 2.7.1.1. Distractors B (EC 4.2.1.70, a lyase/hydratase) and D (EC 2.3.1.319, an acyltransferase) belong to entirely different EC classes and are incompatible with a multi-pass membrane glycosyltransferase architecture. Between A (EC 2.4.1.392, a different glycosyltransferase) and C (EC 2.4.1.259, Alg9), family-level recognition of the Alg9 signature narrows the answer to C.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The multi-pass TM architecture and overall sequence features are consistent with the well-known Alg9 family in N-glycan biosynthesis. Recognizing this family from sequence topology and knowing its canonical EC number (2.4.1.259) is transferable knowledge from studying N-glycan assembly in multiple organisms. The EC-class-level distractors (B, D) are eliminable by basic structural reasoning, and the within-class distinction (A vs C) follows from family identification.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The UniProt entry also lists EC 2.4.1.261 as a secondary activity, but this EC number is not among the offered choices, so it does not create ambiguity. Among the four options, B and D are in wrong EC classes for a multi-pass membrane glycosyltransferase. A (2.4.1.392) is a different glycosyltransferase that does not match the Alg9 family signature. C (2.4.1.259) is the primary and most specific EC assignment for Alg9.


### Important caveats

- The UniProt EC annotation for this Drosophila Alg9 is based on similarity (ECO:0000250) to human Alg9 (Q9H6U8), not on direct experimental characterization of the fly protein.
- The entry also carries EC 2.4.1.261 as a secondary activity; if that EC had been offered as an alternative, the question would be genuinely ambiguous.
- Distinguishing EC 2.4.1.259 from EC 2.4.1.392 at the sequence level requires family-level recognition of Alg9; a model without strong N-glycan biosynthesis knowledge might struggle with this specific pair of glycosyltransferase EC numbers.
- The sequence itself does not contain an explicit signal peptide annotation visible in the raw sequence, though the N-terminal region is consistent with ER targeting.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 623-aa sequence contains approximately 10+ hydrophobic segments consistent with a multi-pass transmembrane ER-resident glycosyltransferase, the hallmark architecture of Alg9 (alpha-1,2-mannosyltransferase) in the N-glycan biosynthesis pathway. Alg9 is one of the most well-characterized enzymes in the dolichol-linked oligosaccharide assembly pathway across yeast, human, Drosophila, and other model organisms. A knowledgeable model can recognize the multi-TM topology, overall length (~600 aa), and conserved sequence motifs as characteristic of the Alg9 family. Knowing that Alg9 catalyzes the alpha-1,2-mannosyltransferase step (EC 2.4.1.259) is standard N-glycan biosynthesis pathway knowledge, analogous to knowing hexokinase is EC 2.7.1.1. Distractors B (EC 4.2.1.70, a lyase/hydratase) and D (EC 2.3.1.319, an acyltransferase) belong to entirely different EC classes and are incompatible with a multi-pass membrane glycosyltransferase architecture. Between A (EC 2.4.1.392, a different glycosyltransferase) and C (EC 2.4.1.259, Alg9), family-level recognition of the Alg9 signature narrows the answer to C.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The multi-pass TM architecture and overall sequence features are consistent with the well-known Alg9 family in N-glycan biosynthesis. Recognizing this family from sequence topology and knowing its canonical EC number (2.4.1.259) is transferable knowledge from studying N-glycan assembly in multiple organisms. The EC-class-level distractors (B, D) are eliminable by basic structural reasoning, and the within-class distinction (A vs C) follows from family identification."
  },
  "case_id": "EC_number_0038",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry Q9VBV8 (ALG9_DROME) lists EC=2.4.1.259 as the primary EC number for Alpha-1,2-mannosyltransferase Alg9, with the catalytic activity describing the transfer of an alpha-1,2-linked mannose from dolichyl-P-Man to the Man6GlcNAc2-PP-dolichol acceptor (Rhea:RHEA:29531). The evidence code is ECO:0000250 (inferred by similarity to human Alg9 Q9H6U8), which is computational transfer rather than direct experimental measurement, but the annotation is consistent and the EC number is the standard assignment for Alg9. The entry also carries EC=2.4.1.261 as a secondary activity, but that EC is not among the offered choices, so it does not contradict choice C."
  },
  "important_caveats": [
    "The UniProt EC annotation for this Drosophila Alg9 is based on similarity (ECO:0000250) to human Alg9 (Q9H6U8), not on direct experimental characterization of the fly protein.",
    "The entry also carries EC 2.4.1.261 as a secondary activity; if that EC had been offered as an alternative, the question would be genuinely ambiguous.",
    "Distinguishing EC 2.4.1.259 from EC 2.4.1.392 at the sequence level requires family-level recognition of Alg9; a model without strong N-glycan biosynthesis knowledge might struggle with this specific pair of glycosyltransferase EC numbers.",
    "The sequence itself does not contain an explicit signal peptide annotation visible in the raw sequence, though the N-terminal region is consistent with ER targeting."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The UniProt entry also lists EC 2.4.1.261 as a secondary activity, but this EC number is not among the offered choices, so it does not create ambiguity. Among the four options, B and D are in wrong EC classes for a multi-pass membrane glycosyltransferase. A (2.4.1.392) is a different glycosyltransferase that does not match the Alg9 family signature. C (2.4.1.259) is the primary and most specific EC assignment for Alg9."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0038",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry Q9VBV8 (ALG9_DROME) lists EC=2.4.1.259 as the primary EC number for Alpha-1,2-mannosyltransferase Alg9, with the catalytic activity describing the transfer of an alpha-1,2-linked mannose from dolichyl-P-Man to the Man6GlcNAc2-PP-dolichol acceptor (Rhea:RHEA:29531). The evidence code is ECO:0000250 (inferred by similarity to human Alg9 Q9H6U8), which is computational transfer rather than direct experimental measurement, but the annotation is consistent and the EC number is the standard assignment for Alg9. The entry also carries EC=2.4.1.261 as a secondary activity, but that EC is not among the offered choices, so it does not contradict choice C.",
    "evidence_ids": ["C4", "C5", "H2", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 623-aa sequence contains approximately 10+ hydrophobic segments consistent with a multi-pass transmembrane ER-resident glycosyltransferase, the hallmark architecture of Alg9 (alpha-1,2-mannosyltransferase) in the N-glycan biosynthesis pathway. Alg9 is one of the most well-characterized enzymes in the dolichol-linked oligosaccharide assembly pathway across yeast, human, Drosophila, and other model organisms. A knowledgeable model can recognize the multi-TM topology, overall length (~600 aa), and conserved sequence motifs as characteristic of the Alg9 family. Knowing that Alg9 catalyzes the alpha-1,2-mannosyltransferase step (EC 2.4.1.259) is standard N-glycan biosynthesis pathway knowledge, analogous to knowing hexokinase is EC 2.7.1.1. Distractors B (EC 4.2.1.70, a lyase/hydratase) and D (EC 2.3.1.319, an acyltransferase) belong to entirely different EC classes and are incompatible with a multi-pass membrane glycosyltransferase architecture. Between A (EC 2.4.1.392, a different glycosyltransferase) and C (EC 2.4.1.259, Alg9), family-level recognition of the Alg9 signature narrows the answer to C.",
    "missing_item_specific_fact": "",
    "reason": "The multi-pass TM architecture and overall sequence features are consistent with the well-known Alg9 family in N-glycan biosynthesis. Recognizing this family from sequence topology and knowing its canonical EC number (2.4.1.259) is transferable knowledge from studying N-glycan assembly in multiple organisms. The EC-class-level distractors (B, D) are eliminable by basic structural reasoning, and the within-class distinction (A vs C) follows from family identification."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The UniProt entry also lists EC 2.4.1.261 as a secondary activity, but this EC number is not among the offered choices, so it does not create ambiguity. Among the four options, B and D are in wrong EC classes for a multi-pass membrane glycosyltransferase. A (2.4.1.392) is a different glycosyltransferase that does not match the Alg9 family signature. C (2.4.1.259) is the primary and most specific EC assignment for Alg9."
  },
  "important_caveats": [
    "The UniProt EC annotation for this Drosophila Alg9 is based on similarity (ECO:0000250) to human Alg9 (Q9H6U8), not on direct experimental characterization of the fly protein.",
    "The entry also carries EC 2.4.1.261 as a secondary activity; if that EC had been offered as an alternative, the question would be genuinely ambiguous.",
    "Distinguishing EC 2.4.1.259 from EC 2.4.1.392 at the sequence level requires family-level recognition of Alg9; a model without strong N-glycan biosynthesis knowledge might struggle with this specific pair of glycosyltransferase EC numbers.",
    "The sequence itself does not contain an explicit signal peptide annotation visible in the raw sequence, though the N-terminal region is consistent with ER targeting."
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
  "requested_accession": "Q9VBV8",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "benchmark_sequence_sha256": "f408e9420c1052e4e0d32438a8e2c7e6058387a35e5959dc8c2bf30c8f4f8cb5",
  "benchmark_sequence_length": 623,
  "current_status": "retrieved",
  "current_sequence_comparison": "matched",
  "current_entry_audit": {
    "entryVersion": 176,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2000-05-01",
    "sequenceVersion": 1
  },
  "current_uniprot_release": "2026_03",
  "current_record_sha256": "24b898b648022de52a5691dcf6976ea8900e27682aaaa66849096b4d46e10d5f",
  "current_source_sequence_sha256": "f408e9420c1052e4e0d32438a8e2c7e6058387a35e5959dc8c2bf30c8f4f8cb5",
  "current_source_sequence_length": 623,
  "historical_status": "retrieved",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "selected_historical_entry_version": 174,
  "selected_historical_version": {
    "accession": "Q9VBV8",
    "database": "Swiss-Prot",
    "entryVersion": 174,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "ALG9_DROME",
    "sequenceVersion": 1
  },
  "selected_historical_record_sha256": "32d28578b9cd594cb2408d344ac0c5be7d01172b1298053b690508892af4f5f8",
  "selected_historical_source_sequence_sha256": "f408e9420c1052e4e0d32438a8e2c7e6058387a35e5959dc8c2bf30c8f4f8cb5",
  "selected_historical_source_sequence_length": 623,
  "latest_at_cutoff_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 174,
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VBV8.json)

```json
{
  "evidence_id": "C1",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VBV8.json",
  "source_sha256": "24b898b648022de52a5691dcf6976ea8900e27682aaaa66849096b4d46e10d5f",
  "retrieved_utc": "2026-11-01T06:25:29.193985+00:00",
  "json_pointer": "/primaryAccession",
  "excerpt": "\"Q9VBV8\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VBV8.json)

```json
{
  "evidence_id": "C2",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VBV8.json",
  "source_sha256": "24b898b648022de52a5691dcf6976ea8900e27682aaaa66849096b4d46e10d5f",
  "retrieved_utc": "2026-11-01T06:25:29.193985+00:00",
  "json_pointer": "/entryAudit",
  "excerpt": "{\"entryVersion\":176,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2000-05-01\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VBV8.json)

```json
{
  "evidence_id": "C3",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VBV8.json",
  "source_sha256": "24b898b648022de52a5691dcf6976ea8900e27682aaaa66849096b4d46e10d5f",
  "retrieved_utc": "2026-11-01T06:25:29.193985+00:00",
  "json_pointer": "/organism",
  "excerpt": "{\"commonName\":\"Fruit fly\",\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP000000803\",\"source\":\"Proteomes\"}],\"lineage\":[\"Eukaryota\",\"Metazoa\",\"Ecdysozoa\",\"Arthropoda\",\"Altocrustacea\",\"Allotriocarida\",\"Hexapoda\",\"Insecta\",\"Pterygota\",\"Neoptera\",\"Eumetabola\",\"Endopterygota\",\"Aparaglossata\",\"Panorpida\",\"Diptera\",\"Brachycera\",\"Muscomorpha\",\"Ephydroidea\",\"Drosophilidae\",\"Drosophila\",\"Sophophora\"],\"scientificName\":\"Drosophila melanogaster\",\"taxonId\":7227}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VBV8.json)

```json
{
  "evidence_id": "C4",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VBV8.json",
  "source_sha256": "24b898b648022de52a5691dcf6976ea8900e27682aaaa66849096b4d46e10d5f",
  "retrieved_utc": "2026-11-01T06:25:29.193985+00:00",
  "json_pointer": "/proteinDescription",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Dolichyl-P-Man:Man6GlcNAc2-PP-dolichol alpha-1,2-mannosyltransferase\"}},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Dolichyl-P-Man:Man8GlcNAc2-PP-dolichol alpha-1,2-mannosyltransferase\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9H6U8\",\"source\":\"UniProtKB\"}],\"value\":\"2.4.1.259\"},{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9H6U8\",\"source\":\"UniProtKB\"}],\"value\":\"2.4.1.261\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"FBgn0039293\",\"source\":\"FlyBase\"}],\"value\":\"Alpha-1,2-mannosyltransferase Alg9\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VBV8.json)

```json
{
  "evidence_id": "C5",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VBV8.json",
  "source_sha256": "24b898b648022de52a5691dcf6976ea8900e27682aaaa66849096b4d46e10d5f",
  "retrieved_utc": "2026-11-01T06:25:29.193985+00:00",
  "json_pointer": "/comments/1",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"ecNumber\":\"2.4.1.259\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9H6U8\",\"source\":\"UniProtKB\"}],\"name\":\"an alpha-D-Man-(1->2)-alpha-D-Man-(1->2)-alpha-D-Man-(1->3)-[alpha-D-Man-(1->3)-alpha-D-Man-(1->6)]-beta-D-Man-(1->4)-beta-D-GlcNAc-(1->4)-alpha-D-GlcNAc-diphospho-di-trans,poly-cis-dolichol + a di-trans,poly-cis-dolichyl beta-D-mannosyl phosphate = an alpha-D-Man-(1->2)-alpha-D-Man-(1->2)-alpha-D-Man-(1->3)-[alpha-D-Man-(1->2)-alpha-D-Man-(1->3)-alpha-D-Man-(1->6)]-beta-D-Man-(1->4)-beta-D-GlcNAc-(1->4)-alpha-D-GlcNAc-diphospho-di-trans,poly-cis-dolichol + a di-trans,poly-cis-dolichyl phosphate + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:29531\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:19498\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:19501\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:19517\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:19518\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57683\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:58211\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:132516\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:132517\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VBV8.json)

```json
{
  "evidence_id": "C6",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VBV8.json",
  "source_sha256": "24b898b648022de52a5691dcf6976ea8900e27682aaaa66849096b4d46e10d5f",
  "retrieved_utc": "2026-11-01T06:25:29.193985+00:00",
  "json_pointer": "/comments/2",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"ecNumber\":\"2.4.1.261\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9H6U8\",\"source\":\"UniProtKB\"}],\"name\":\"an alpha-D-Man-(1->2)-alpha-D-Man-(1->2)-alpha-D-Man-(1->3)-[alpha-D-Man-(1->2)-alpha-D-Man-(1->3)-[alpha-D-Man-(1->6)]-alpha-D-Man-(1->6)]-beta-D-Man-(1->4)-beta-D-GlcNAc-(1->4)-alpha-D-GlcNAc-diphospho-di-trans,poly-cis-dolichol + a di-trans,poly-cis-dolichyl beta-D-mannosyl phosphate = an alpha-D-Man-(1->2)-alpha-D-Man-(1->2)-alpha-D-Man-(1->3)-[alpha-D-Man-(1->2)-alpha-D-Man-(1->3)-[alpha-D-Man-(1->2)-alpha-D-Man-(1->6)]-alpha-D-Man-(1->6)]-beta-D-Man-(1->4)-beta-D-GlcNAc-(1->4)-alpha-D-GlcNAc-diphospho-di-trans,poly-cis-dolichol + a di-trans,poly-cis-dolichyl phosphate + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:29539\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:19498\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:19501\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:19519\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:19520\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57683\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:58211\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:132519\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:132520\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VBV8?format=txt&versions=174)

```json
{
  "evidence_id": "H1",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q9VBV8?format=txt&versions=174",
  "source_sha256": "32d28578b9cd594cb2408d344ac0c5be7d01172b1298053b690508892af4f5f8",
  "retrieved_utc": "2026-11-01T06:28:51.427257+00:00",
  "source_locator": "lines 1-17",
  "excerpt": "ID   ALG9_DROME              Reviewed;         623 AA.\nAC   Q9VBV8;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   01-MAY-2000, sequence version 1.\nDT   28-JAN-2026, entry version 174.\nDE   RecName: Full=Alpha-1,2-mannosyltransferase Alg9 {ECO:0000312|FlyBase:FBgn0039293};\nDE            EC=2.4.1.259 {ECO:0000250|UniProtKB:Q9H6U8};\nDE            EC=2.4.1.261 {ECO:0000250|UniProtKB:Q9H6U8};\nDE   AltName: Full=Dolichyl-P-Man:Man6GlcNAc2-PP-dolichol alpha-1,2-mannosyltransferase {ECO:0000305};\nDE   AltName: Full=Dolichyl-P-Man:Man8GlcNAc2-PP-dolichol alpha-1,2-mannosyltransferase {ECO:0000305};\nGN   Name=Alg9 {ECO:0000312|FlyBase:FBgn0039293};\nGN   ORFNames=CG11851 {ECO:0000312|FlyBase:FBgn0039293};\nOS   Drosophila melanogaster (Fruit fly).\nOC   Eukaryota; Metazoa; Ecdysozoa; Arthropoda; Hexapoda; Insecta; Pterygota;\nOC   Neoptera; Endopterygota; Diptera; Brachycera; Muscomorpha; Ephydroidea;\nOC   Drosophilidae; Drosophila; Sophophora.\nOX   NCBI_TaxID=7227 {ECO:0000312|Proteomes:UP000000803};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 174,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VBV8?format=txt&versions=174)

```json
{
  "evidence_id": "H2",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q9VBV8?format=txt&versions=174",
  "source_sha256": "32d28578b9cd594cb2408d344ac0c5be7d01172b1298053b690508892af4f5f8",
  "retrieved_utc": "2026-11-01T06:28:51.427257+00:00",
  "source_locator": "lines 6-10",
  "excerpt": "DE   RecName: Full=Alpha-1,2-mannosyltransferase Alg9 {ECO:0000312|FlyBase:FBgn0039293};\nDE            EC=2.4.1.259 {ECO:0000250|UniProtKB:Q9H6U8};\nDE            EC=2.4.1.261 {ECO:0000250|UniProtKB:Q9H6U8};\nDE   AltName: Full=Dolichyl-P-Man:Man6GlcNAc2-PP-dolichol alpha-1,2-mannosyltransferase {ECO:0000305};\nDE   AltName: Full=Dolichyl-P-Man:Man8GlcNAc2-PP-dolichol alpha-1,2-mannosyltransferase {ECO:0000305};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 174,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VBV8?format=txt&versions=174)

```json
{
  "evidence_id": "H3",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q9VBV8?format=txt&versions=174",
  "source_sha256": "32d28578b9cd594cb2408d344ac0c5be7d01172b1298053b690508892af4f5f8",
  "retrieved_utc": "2026-11-01T06:28:51.427257+00:00",
  "source_locator": "lines 104-116",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=an alpha-D-Man-(1->2)-alpha-D-Man-(1->2)-alpha-D-Man-(1->3)-\nCC         [alpha-D-Man-(1->3)-alpha-D-Man-(1->6)]-beta-D-Man-(1->4)-beta-D-\nCC         GlcNAc-(1->4)-alpha-D-GlcNAc-diphospho-di-trans,poly-cis-dolichol + a\nCC         di-trans,poly-cis-dolichyl beta-D-mannosyl phosphate = an alpha-D-\nCC         Man-(1->2)-alpha-D-Man-(1->2)-alpha-D-Man-(1->3)-[alpha-D-Man-(1->2)-\nCC         alpha-D-Man-(1->3)-alpha-D-Man-(1->6)]-beta-D-Man-(1->4)-beta-D-\nCC         GlcNAc-(1->4)-alpha-D-GlcNAc-diphospho-di-trans,poly-cis-dolichol + a\nCC         di-trans,poly-cis-dolichyl phosphate + H(+); Xref=Rhea:RHEA:29531,\nCC         Rhea:RHEA-COMP:19498, Rhea:RHEA-COMP:19501, Rhea:RHEA-COMP:19517,\nCC         Rhea:RHEA-COMP:19518, ChEBI:CHEBI:15378, ChEBI:CHEBI:57683,\nCC         ChEBI:CHEBI:58211, ChEBI:CHEBI:132516, ChEBI:CHEBI:132517;\nCC         EC=2.4.1.259; Evidence={ECO:0000250|UniProtKB:Q9H6U8};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 174,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VBV8?format=txt&versions=174)

```json
{
  "evidence_id": "H4",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q9VBV8?format=txt&versions=174",
  "source_sha256": "32d28578b9cd594cb2408d344ac0c5be7d01172b1298053b690508892af4f5f8",
  "retrieved_utc": "2026-11-01T06:28:51.427257+00:00",
  "source_locator": "lines 117-131",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=an alpha-D-Man-(1->2)-alpha-D-Man-(1->2)-alpha-D-Man-(1->3)-\nCC         [alpha-D-Man-(1->2)-alpha-D-Man-(1->3)-[alpha-D-Man-(1->6)]-alpha-D-\nCC         Man-(1->6)]-beta-D-Man-(1->4)-beta-D-GlcNAc-(1->4)-alpha-D-GlcNAc-\nCC         diphospho-di-trans,poly-cis-dolichol + a di-trans,poly-cis-dolichyl\nCC         beta-D-mannosyl phosphate = an alpha-D-Man-(1->2)-alpha-D-Man-(1->2)-\nCC         alpha-D-Man-(1->3)-[alpha-D-Man-(1->2)-alpha-D-Man-(1->3)-[alpha-D-\nCC         Man-(1->2)-alpha-D-Man-(1->6)]-alpha-D-Man-(1->6)]-beta-D-Man-(1->4)-\nCC         beta-D-GlcNAc-(1->4)-alpha-D-GlcNAc-diphospho-di-trans,poly-cis-\nCC         dolichol + a di-trans,poly-cis-dolichyl phosphate + H(+);\nCC         Xref=Rhea:RHEA:29539, Rhea:RHEA-COMP:19498, Rhea:RHEA-COMP:19501,\nCC         Rhea:RHEA-COMP:19519, Rhea:RHEA-COMP:19520, ChEBI:CHEBI:15378,\nCC         ChEBI:CHEBI:57683, ChEBI:CHEBI:58211, ChEBI:CHEBI:132519,\nCC         ChEBI:CHEBI:132520; EC=2.4.1.261;\nCC         Evidence={ECO:0000250|UniProtKB:Q9H6U8};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 174,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 38. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
