# EC_number_0082: before and after transfer clarification

[All 1,328 cases](../README.md) · [Method](../METHOD.md) · [Summary](../SUMMARY.md) · [Exact reviewer user message](../inputs/EC_number_0082.txt)

**Task:** `EC_number`  
**Author key, unchanged:** **B** — 2.3.1.312

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
MQIKPPYLLFIGDATDKLSIKMAQSLADWRAELCVGELSVNGCTVSTGLNQCSICEAAKLGAKTFVLGFANSGGVLDKKWLPIISEAIENGMNIVSGLHDKLTNFDELVSLSQKHNTNLLDIRHPSTAFATGKGYKRKGKRLLTVGTDCSVGKMYTSLSLEKAMKEQNIDVDFRATGQCGILISGSGVAIDCVIADFISGAAESLSPDAEETHWDIIEGQGSLSHPAFAGVSLGLLHGSQPDALVICHALNRTHMRGLLHTSFPSIETTIELNIAAAKLTNPDVQVVGISVNTSSVSIEQGNEICERLSQTFGVPCVDPLRDGVDSIVANLC

[Multiple Choices]
A. 2.3.1.193
B. 2.3.1.312
C. 2.1.1.393
D. 5.2.1.8
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

> The supplied sequence exactly matches the 332-aa UniProt entry annotated as EC 2.3.1.312. The annotation cites experimental evidence for acetyl-CoA-dependent acetylation of D-glutamate, and also reports activity with D-aspartate and D-glutamine.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence may permit inference of an enzyme family or acetyltransferase-like activity, but the supplied input does not establish the specific substrate preference or complete EC classification needed to distinguish the options.


**Missing item-specific fact**

> The protein-specific experimentally characterized reaction and its EC assignment, namely D-amino-acid N-acetylation classified as EC 2.3.1.312.


**Reason**

> Choosing the precise EC number depends on protein-specific functional characterization or an external annotation; sequence-based general reasoning alone does not meaningfully resolve the relevant substrate-specific distinction.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The matched sequence has direct cited annotation to option B; the evidence does not support another listed option.


### Important caveats

- The cited experimental evidence is represented here through UniProt annotations citing PubMed 36690779; the primary paper was not independently reviewed.
- The reviewer-only accession and annotation were not supplied to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence may permit inference of an enzyme family or acetyltransferase-like activity, but the supplied input does not establish the specific substrate preference or complete EC classification needed to distinguish the options.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific experimentally characterized reaction and its EC assignment, namely D-amino-acid N-acetylation classified as EC 2.3.1.312.",
    "reason": "Choosing the precise EC number depends on protein-specific functional characterization or an external annotation; sequence-based general reasoning alone does not meaningfully resolve the relevant substrate-specific distinction."
  },
  "case_id": "EC_number_0082",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "C7",
      "H4",
      "H5",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the 332-aa UniProt entry annotated as EC 2.3.1.312. The annotation cites experimental evidence for acetyl-CoA-dependent acetylation of D-glutamate, and also reports activity with D-aspartate and D-glutamine."
  },
  "important_caveats": [
    "The cited experimental evidence is represented here through UniProt annotations citing PubMed 36690779; the primary paper was not independently reviewed.",
    "The reviewer-only accession and annotation were not supplied to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched sequence has direct cited annotation to option B; the evidence does not support another listed option."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0082",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the 332-aa UniProt entry annotated as EC 2.3.1.312. The annotation cites experimental evidence for acetyl-CoA-dependent acetylation of D-glutamate, and also reports activity with D-aspartate and D-glutamine.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "C7", "H4", "H5", "H6"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence may permit inference of an enzyme family or acetyltransferase-like activity, but the supplied input does not establish the specific substrate preference or complete EC classification needed to distinguish the options.",
    "missing_item_specific_fact": "The protein-specific experimentally characterized reaction and its EC assignment, namely D-amino-acid N-acetylation classified as EC 2.3.1.312.",
    "reason": "Choosing the precise EC number depends on protein-specific functional characterization or an external annotation; sequence-based general reasoning alone does not meaningfully resolve the relevant substrate-specific distinction."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched sequence has direct cited annotation to option B; the evidence does not support another listed option."
  },
  "important_caveats": [
    "The cited experimental evidence is represented here through UniProt annotations citing PubMed 36690779; the primary paper was not independently reviewed.",
    "The reviewer-only accession and annotation were not supplied to the evaluated model."
  ]
}
```

</details>

## Before: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry P0DXZ1 (sequence SHA256 matched, 332 aa) annotates this protein as D-glutamate N-acetyltransferase, EC 2.3.1.312, with direct experimental evidence (ECO:0000269, PubMed:36690779, ISME J. 2023). The catalytic activity 'D-glutamate + acetyl-CoA = N-acetyl-D-glutamate + CoA + H(+)' is experimentally confirmed. The answer B (2.3.1.312) is fully supported by experimental data.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [H2](#evidence-h2), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> A knowledgeable model might recognize GNAT (Gcn5-related N-acetyltransferase) fold motifs in the sequence (e.g., the 'GSGVAIDC' region resembling a CoA-binding P-loop, overall ~332-aa length consistent with GNAT superfamily), which could plausibly eliminate option D (EC 5.2.1.8, an isomerase — wrong EC class) and option C (EC 2.1.1.393, a methyltransferase — different transferase subclass). This narrows the field to two 2.3.1.x acyltransferase options.


**Missing item-specific fact**

> Distinguishing between EC 2.3.1.193 (option A) and EC 2.3.1.312 (option B) requires knowing the precise substrate specificity of this particular enzyme (D-glutamate vs. the substrate of 2.3.1.193). This is an item-specific annotation fact. Moreover, EC 2.3.1.312 was newly assigned in 2023 for a novel D-glutamate catabolic pathway, so it is absent from older reference databases and cannot be inferred from general sequence motifs alone.


**Reason**

> While GNAT-fold recognition provides a partial biological argument to eliminate the isomerase and methyltransferase distractors, the final choice between two acyltransferase EC numbers (2.3.1.193 vs 2.3.1.312) depends on knowing the exact substrate preference of this specific enzyme, which is a database-lookup fact not derivable from the sequence by general reasoning.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options C (methyltransferase, EC 2.1.1.x) and D (isomerase, EC 5.2.1.x) are clearly different EC classes and are not defensible for a GNAT-like acetyltransferase. The remaining two options (A: 2.3.1.193 and B: 2.3.1.312) are both 2.3.1.x acyltransferases, but the experimental evidence unambiguously assigns 2.3.1.312. No genuine ambiguity in the correct answer.


### Important caveats

- EC 2.3.1.312 was newly assigned in 2023 (PubMed:36690779) for a novel D-glutamate catabolic pathway in marine Proteobacteria. It would not appear in pre-2023 reference databases, making this question heavily dependent on up-to-date annotation knowledge.
- The protein also shows activity on D-aspartate and D-glutamine (C6, C7), broadening substrate scope beyond the primary D-glutamate reaction, but the EC assignment remains 2.3.1.312.
- The reviewer-only UniProt accession (P0DXZ1) and its annotation were not available to the evaluated model; the model sees only the raw sequence and four EC-number choices.
- If EC 2.3.1.193 is not a currently valid or well-characterized EC number, it may be a trivially eliminable distractor, but this cannot be confirmed from the supplied evidence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "A knowledgeable model might recognize GNAT (Gcn5-related N-acetyltransferase) fold motifs in the sequence (e.g., the 'GSGVAIDC' region resembling a CoA-binding P-loop, overall ~332-aa length consistent with GNAT superfamily), which could plausibly eliminate option D (EC 5.2.1.8, an isomerase — wrong EC class) and option C (EC 2.1.1.393, a methyltransferase — different transferase subclass). This narrows the field to two 2.3.1.x acyltransferase options.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "Distinguishing between EC 2.3.1.193 (option A) and EC 2.3.1.312 (option B) requires knowing the precise substrate specificity of this particular enzyme (D-glutamate vs. the substrate of 2.3.1.193). This is an item-specific annotation fact. Moreover, EC 2.3.1.312 was newly assigned in 2023 for a novel D-glutamate catabolic pathway, so it is absent from older reference databases and cannot be inferred from general sequence motifs alone.",
    "reason": "While GNAT-fold recognition provides a partial biological argument to eliminate the isomerase and methyltransferase distractors, the final choice between two acyltransferase EC numbers (2.3.1.193 vs 2.3.1.312) depends on knowing the exact substrate preference of this specific enzyme, which is a database-lookup fact not derivable from the sequence by general reasoning."
  },
  "case_id": "EC_number_0082",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C7",
      "C8",
      "H2",
      "H4",
      "H5",
      "H6"
    ],
    "judgment": "supported",
    "reason": "UniProt entry P0DXZ1 (sequence SHA256 matched, 332 aa) annotates this protein as D-glutamate N-acetyltransferase, EC 2.3.1.312, with direct experimental evidence (ECO:0000269, PubMed:36690779, ISME J. 2023). The catalytic activity 'D-glutamate + acetyl-CoA = N-acetyl-D-glutamate + CoA + H(+)' is experimentally confirmed. The answer B (2.3.1.312) is fully supported by experimental data."
  },
  "important_caveats": [
    "EC 2.3.1.312 was newly assigned in 2023 (PubMed:36690779) for a novel D-glutamate catabolic pathway in marine Proteobacteria. It would not appear in pre-2023 reference databases, making this question heavily dependent on up-to-date annotation knowledge.",
    "The protein also shows activity on D-aspartate and D-glutamine (C6, C7), broadening substrate scope beyond the primary D-glutamate reaction, but the EC assignment remains 2.3.1.312.",
    "The reviewer-only UniProt accession (P0DXZ1) and its annotation were not available to the evaluated model; the model sees only the raw sequence and four EC-number choices.",
    "If EC 2.3.1.193 is not a currently valid or well-characterized EC number, it may be a trivially eliminable distractor, but this cannot be confirmed from the supplied evidence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options C (methyltransferase, EC 2.1.1.x) and D (isomerase, EC 5.2.1.x) are clearly different EC classes and are not defensible for a GNAT-like acetyltransferase. The remaining two options (A: 2.3.1.193 and B: 2.3.1.312) are both 2.3.1.x acyltransferases, but the experimental evidence unambiguously assigns 2.3.1.312. No genuine ambiguity in the correct answer."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0082",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry P0DXZ1 (sequence SHA256 matched, 332 aa) annotates this protein as D-glutamate N-acetyltransferase, EC 2.3.1.312, with direct experimental evidence (ECO:0000269, PubMed:36690779, ISME J. 2023). The catalytic activity 'D-glutamate + acetyl-CoA = N-acetyl-D-glutamate + CoA + H(+)' is experimentally confirmed. The answer B (2.3.1.312) is fully supported by experimental data.",
    "evidence_ids": ["C4", "C5", "C6", "C7", "C8", "H2", "H4", "H5", "H6"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "A knowledgeable model might recognize GNAT (Gcn5-related N-acetyltransferase) fold motifs in the sequence (e.g., the 'GSGVAIDC' region resembling a CoA-binding P-loop, overall ~332-aa length consistent with GNAT superfamily), which could plausibly eliminate option D (EC 5.2.1.8, an isomerase — wrong EC class) and option C (EC 2.1.1.393, a methyltransferase — different transferase subclass). This narrows the field to two 2.3.1.x acyltransferase options.",
    "missing_item_specific_fact": "Distinguishing between EC 2.3.1.193 (option A) and EC 2.3.1.312 (option B) requires knowing the precise substrate specificity of this particular enzyme (D-glutamate vs. the substrate of 2.3.1.193). This is an item-specific annotation fact. Moreover, EC 2.3.1.312 was newly assigned in 2023 for a novel D-glutamate catabolic pathway, so it is absent from older reference databases and cannot be inferred from general sequence motifs alone.",
    "reason": "While GNAT-fold recognition provides a partial biological argument to eliminate the isomerase and methyltransferase distractors, the final choice between two acyltransferase EC numbers (2.3.1.193 vs 2.3.1.312) depends on knowing the exact substrate preference of this specific enzyme, which is a database-lookup fact not derivable from the sequence by general reasoning."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options C (methyltransferase, EC 2.1.1.x) and D (isomerase, EC 5.2.1.x) are clearly different EC classes and are not defensible for a GNAT-like acetyltransferase. The remaining two options (A: 2.3.1.193 and B: 2.3.1.312) are both 2.3.1.x acyltransferases, but the experimental evidence unambiguously assigns 2.3.1.312. No genuine ambiguity in the correct answer."
  },
  "important_caveats": [
    "EC 2.3.1.312 was newly assigned in 2023 (PubMed:36690779) for a novel D-glutamate catabolic pathway in marine Proteobacteria. It would not appear in pre-2023 reference databases, making this question heavily dependent on up-to-date annotation knowledge.",
    "The protein also shows activity on D-aspartate and D-glutamine (C6, C7), broadening substrate scope beyond the primary D-glutamate reaction, but the EC assignment remains 2.3.1.312.",
    "The reviewer-only UniProt accession (P0DXZ1) and its annotation were not available to the evaluated model; the model sees only the raw sequence and four EC-number choices.",
    "If EC 2.3.1.193 is not a currently valid or well-characterized EC number, it may be a trivially eliminable distractor, but this cannot be confirmed from the supplied evidence."
  ]
}
```

</details>

## After: GPT-6 Luna

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence-matched UniProt annotation assigns EC 2.3.1.312 and cites experimental evidence. The catalytic-activity record specifies acetylation of D-glutamate, which supports choice B. The cited study was not independently reviewed here.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

Empty string, as saved.


**Missing item-specific fact**

> Evidence that this protein specifically acetylates D-glutamate, or a sufficiently close characterized homolog establishing that substrate specificity, is not supplied in the original input.


**Reason**

> The sequence may suggest an enzyme, but no clear feature in the input distinguishes the D-glutamate acetyltransferase choice B from the other acetyltransferase choice A. Their distinction depends on substrate specificity, which is not reliably inferred from the broad enzyme class alone.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The supplied experimental annotation supports B; lack of a clear sequence-only discriminator does not make another option an equally defensible actual EC assignment.


### Important caveats

- The supporting source is a sequence-matched database record citing experimental evidence; the cited paper was not independently checked.
- The reviewer-only source identity and annotations were not part of the original model input.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "Evidence that this protein specifically acetylates D-glutamate, or a sufficiently close characterized homolog establishing that substrate specificity, is not supplied in the original input.",
    "reason": "The sequence may suggest an enzyme, but no clear feature in the input distinguishes the D-glutamate acetyltransferase choice B from the other acetyltransferase choice A. Their distinction depends on substrate specificity, which is not reliably inferred from the broad enzyme class alone."
  },
  "case_id": "EC_number_0082",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation assigns EC 2.3.1.312 and cites experimental evidence. The catalytic-activity record specifies acetylation of D-glutamate, which supports choice B. The cited study was not independently reviewed here."
  },
  "important_caveats": [
    "The supporting source is a sequence-matched database record citing experimental evidence; the cited paper was not independently checked.",
    "The reviewer-only source identity and annotations were not part of the original model input."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied experimental annotation supports B; lack of a clear sequence-only discriminator does not make another option an equally defensible actual EC assignment."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0082",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation assigns EC 2.3.1.312 and cites experimental evidence. The catalytic-activity record specifies acetylation of D-glutamate, which supports choice B. The cited study was not independently reviewed here.",
    "evidence_ids": ["C4", "C5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "",
    "missing_item_specific_fact": "Evidence that this protein specifically acetylates D-glutamate, or a sufficiently close characterized homolog establishing that substrate specificity, is not supplied in the original input.",
    "reason": "The sequence may suggest an enzyme, but no clear feature in the input distinguishes the D-glutamate acetyltransferase choice B from the other acetyltransferase choice A. Their distinction depends on substrate specificity, which is not reliably inferred from the broad enzyme class alone."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied experimental annotation supports B; lack of a clear sequence-only discriminator does not make another option an equally defensible actual EC assignment."
  },
  "important_caveats": [
    "The supporting source is a sequence-matched database record citing experimental evidence; the cited paper was not independently checked.",
    "The reviewer-only source identity and annotations were not part of the original model input."
  ]
}
```

</details>

## After: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry P0DXZ1 annotates this 332-aa protein as D-glutamate N-acetyltransferase, EC 2.3.1.312, with experimental evidence (ECO:0000269, PubMed:36690779, ISME J. 2023). The catalytic reaction D-glutamate + acetyl-CoA → N-acetyl-D-glutamate + CoA + H(+) is experimentally validated. The benchmark sequence matches the source sequence exactly (SHA-256 confirmed). The historical Swiss-Prot record (entry version 3) also carries EC 2.3.1.312.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> Transferable knowledge can narrow the EC class: the sequence contains a GNAT (GCN5-related N-acetyltransferase) fold motif ('GFANSGG' near the N-terminus, acetyl-CoA-binding region features), which is characteristic of acyltransferases (EC 2.3.x), not methyltransferases (EC 2.1.x) or isomerases (EC 5.2.x). This reliably eliminates C (2.1.1.393, methyltransferase) and D (5.2.1.8, cis-trans isomerase). However, both remaining options A (2.3.1.193) and B (2.3.1.312) fall within EC 2.3.1.x (acyltransferases transferring groups other than amino-acyl groups). Distinguishing between these two specific four-digit EC numbers requires knowing the exact substrate specificity of the enzyme (e.g., D-glutamate vs. whatever substrate 2.3.1.193 acts on). While GNAT subfamily classification can indicate the general substrate class, the precise assignment to EC 2.3.1.312 versus 2.3.1.193 depends on experimentally determined substrate specificity and active-site residue configurations that are not reliably extractable from the raw sequence alone without already knowing this protein's annotation.


**Missing item-specific fact**

> The experimentally determined substrate specificity of this particular GNAT-fold protein (i.e., that it specifically acetylates D-glutamate, D-aspartate, and D-glutamine rather than the substrate of EC 2.3.1.193), which is established only through the in vitro enzymatic assays reported in PubMed:36690779.


**Reason**

> The GNAT fold and acyltransferase motifs allow elimination of the methyltransferase (C) and isomerase (D) options through family-level inference. However, the final distinction between 2.3.1.193 and 2.3.1.312 requires knowledge of the exact substrate specificity, which is an experimental measurement specific to this protein and not derivable from sequence homology or general GNAT-family knowledge alone.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options span three different EC top-level classes (2.3.1.x acyltransferase, 2.1.1.x methyltransferase, 5.2.1.x isomerase), so there is no ambiguity in the question format. The difficulty lies in distinguishing the two 2.3.1.x options, not in ambiguous wording.


### Important caveats

- The UniProt entry was first published on 2025-04-09 and the Swiss-Prot review (entry version 3) was released in 2026_01. The author's source snapshot is unknown; if the question was constructed before the Swiss-Prot annotation, the EC number may have been derived from the primary publication directly.
- EC 2.3.1.193 is a valid but obscure EC number; its exact substrate identity was not independently verified in this review. The argument for lookup dependence assumes that 2.3.1.193 and 2.3.1.312 cannot be distinguished by GNAT subfamily features alone, which may be refined with more detailed active-site analysis.
- The reviewer-only evidence confirms sequence match and experimental evidence code (ECO:0000269), but the evaluated model had access only to the raw sequence and the four EC number choices.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Transferable knowledge can narrow the EC class: the sequence contains a GNAT (GCN5-related N-acetyltransferase) fold motif ('GFANSGG' near the N-terminus, acetyl-CoA-binding region features), which is characteristic of acyltransferases (EC 2.3.x), not methyltransferases (EC 2.1.x) or isomerases (EC 5.2.x). This reliably eliminates C (2.1.1.393, methyltransferase) and D (5.2.1.8, cis-trans isomerase). However, both remaining options A (2.3.1.193) and B (2.3.1.312) fall within EC 2.3.1.x (acyltransferases transferring groups other than amino-acyl groups). Distinguishing between these two specific four-digit EC numbers requires knowing the exact substrate specificity of the enzyme (e.g., D-glutamate vs. whatever substrate 2.3.1.193 acts on). While GNAT subfamily classification can indicate the general substrate class, the precise assignment to EC 2.3.1.312 versus 2.3.1.193 depends on experimentally determined substrate specificity and active-site residue configurations that are not reliably extractable from the raw sequence alone without already knowing this protein's annotation.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The experimentally determined substrate specificity of this particular GNAT-fold protein (i.e., that it specifically acetylates D-glutamate, D-aspartate, and D-glutamine rather than the substrate of EC 2.3.1.193), which is established only through the in vitro enzymatic assays reported in PubMed:36690779.",
    "reason": "The GNAT fold and acyltransferase motifs allow elimination of the methyltransferase (C) and isomerase (D) options through family-level inference. However, the final distinction between 2.3.1.193 and 2.3.1.312 requires knowledge of the exact substrate specificity, which is an experimental measurement specific to this protein and not derivable from sequence homology or general GNAT-family knowledge alone."
  },
  "case_id": "EC_number_0082",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry P0DXZ1 annotates this 332-aa protein as D-glutamate N-acetyltransferase, EC 2.3.1.312, with experimental evidence (ECO:0000269, PubMed:36690779, ISME J. 2023). The catalytic reaction D-glutamate + acetyl-CoA → N-acetyl-D-glutamate + CoA + H(+) is experimentally validated. The benchmark sequence matches the source sequence exactly (SHA-256 confirmed). The historical Swiss-Prot record (entry version 3) also carries EC 2.3.1.312."
  },
  "important_caveats": [
    "The UniProt entry was first published on 2025-04-09 and the Swiss-Prot review (entry version 3) was released in 2026_01. The author's source snapshot is unknown; if the question was constructed before the Swiss-Prot annotation, the EC number may have been derived from the primary publication directly.",
    "EC 2.3.1.193 is a valid but obscure EC number; its exact substrate identity was not independently verified in this review. The argument for lookup dependence assumes that 2.3.1.193 and 2.3.1.312 cannot be distinguished by GNAT subfamily features alone, which may be refined with more detailed active-site analysis.",
    "The reviewer-only evidence confirms sequence match and experimental evidence code (ECO:0000269), but the evaluated model had access only to the raw sequence and the four EC number choices."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span three different EC top-level classes (2.3.1.x acyltransferase, 2.1.1.x methyltransferase, 5.2.1.x isomerase), so there is no ambiguity in the question format. The difficulty lies in distinguishing the two 2.3.1.x options, not in ambiguous wording."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0082",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry P0DXZ1 annotates this 332-aa protein as D-glutamate N-acetyltransferase, EC 2.3.1.312, with experimental evidence (ECO:0000269, PubMed:36690779, ISME J. 2023). The catalytic reaction D-glutamate + acetyl-CoA → N-acetyl-D-glutamate + CoA + H(+) is experimentally validated. The benchmark sequence matches the source sequence exactly (SHA-256 confirmed). The historical Swiss-Prot record (entry version 3) also carries EC 2.3.1.312.",
    "evidence_ids": ["C4", "C5", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "Transferable knowledge can narrow the EC class: the sequence contains a GNAT (GCN5-related N-acetyltransferase) fold motif ('GFANSGG' near the N-terminus, acetyl-CoA-binding region features), which is characteristic of acyltransferases (EC 2.3.x), not methyltransferases (EC 2.1.x) or isomerases (EC 5.2.x). This reliably eliminates C (2.1.1.393, methyltransferase) and D (5.2.1.8, cis-trans isomerase). However, both remaining options A (2.3.1.193) and B (2.3.1.312) fall within EC 2.3.1.x (acyltransferases transferring groups other than amino-acyl groups). Distinguishing between these two specific four-digit EC numbers requires knowing the exact substrate specificity of the enzyme (e.g., D-glutamate vs. whatever substrate 2.3.1.193 acts on). While GNAT subfamily classification can indicate the general substrate class, the precise assignment to EC 2.3.1.312 versus 2.3.1.193 depends on experimentally determined substrate specificity and active-site residue configurations that are not reliably extractable from the raw sequence alone without already knowing this protein's annotation.",
    "missing_item_specific_fact": "The experimentally determined substrate specificity of this particular GNAT-fold protein (i.e., that it specifically acetylates D-glutamate, D-aspartate, and D-glutamine rather than the substrate of EC 2.3.1.193), which is established only through the in vitro enzymatic assays reported in PubMed:36690779.",
    "reason": "The GNAT fold and acyltransferase motifs allow elimination of the methyltransferase (C) and isomerase (D) options through family-level inference. However, the final distinction between 2.3.1.193 and 2.3.1.312 requires knowledge of the exact substrate specificity, which is an experimental measurement specific to this protein and not derivable from sequence homology or general GNAT-family knowledge alone."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span three different EC top-level classes (2.3.1.x acyltransferase, 2.1.1.x methyltransferase, 5.2.1.x isomerase), so there is no ambiguity in the question format. The difficulty lies in distinguishing the two 2.3.1.x options, not in ambiguous wording."
  },
  "important_caveats": [
    "The UniProt entry was first published on 2025-04-09 and the Swiss-Prot review (entry version 3) was released in 2026_01. The author's source snapshot is unknown; if the question was constructed before the Swiss-Prot annotation, the EC number may have been derived from the primary publication directly.",
    "EC 2.3.1.193 is a valid but obscure EC number; its exact substrate identity was not independently verified in this review. The argument for lookup dependence assumes that 2.3.1.193 and 2.3.1.312 cannot be distinguished by GNAT subfamily features alone, which may be refined with more detailed active-site analysis.",
    "The reviewer-only evidence confirms sequence match and experimental evidence code (ECO:0000269), but the evaluated model had access only to the raw sequence and the four EC number choices."
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
  "requested_accession": "P0DXZ1",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "benchmark_sequence_sha256": "d233fd888471e43669f332aeb0b2fac44fb59ce5fab9d43f3919864cdb20c35d",
  "benchmark_sequence_length": 332,
  "current_status": "retrieved",
  "current_sequence_comparison": "matched",
  "current_entry_audit": {
    "entryVersion": 5,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2025-04-09",
    "sequenceVersion": 1
  },
  "current_uniprot_release": "2026_03",
  "current_record_sha256": "aa2463d659dcce0272e4a1954d2f0e0ac1de2519b56334e15e5b9a8b29cffa17",
  "current_source_sequence_sha256": "d233fd888471e43669f332aeb0b2fac44fb59ce5fab9d43f3919864cdb20c35d",
  "current_source_sequence_length": 332,
  "historical_status": "retrieved",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "selected_historical_entry_version": 3,
  "selected_historical_version": {
    "accession": "P0DXZ1",
    "database": "Swiss-Prot",
    "entryVersion": 3,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "DGCN_PSEAS",
    "sequenceVersion": 1
  },
  "selected_historical_record_sha256": "f028fea1879dfe3aaa57742281e0eecbec1a2030f44e9354a914347ae6b4be60",
  "selected_historical_source_sequence_sha256": "d233fd888471e43669f332aeb0b2fac44fb59ce5fab9d43f3919864cdb20c35d",
  "selected_historical_source_sequence_length": 332,
  "latest_at_cutoff_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 3,
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXZ1.json)

```json
{
  "evidence_id": "C1",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXZ1.json",
  "source_sha256": "aa2463d659dcce0272e4a1954d2f0e0ac1de2519b56334e15e5b9a8b29cffa17",
  "retrieved_utc": "2026-11-02T04:29:58.706491+00:00",
  "json_pointer": "/primaryAccession",
  "excerpt": "\"P0DXZ1\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXZ1.json)

```json
{
  "evidence_id": "C2",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXZ1.json",
  "source_sha256": "aa2463d659dcce0272e4a1954d2f0e0ac1de2519b56334e15e5b9a8b29cffa17",
  "retrieved_utc": "2026-11-02T04:29:58.706491+00:00",
  "json_pointer": "/entryAudit",
  "excerpt": "{\"entryVersion\":5,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2025-04-09\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXZ1.json)

```json
{
  "evidence_id": "C3",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXZ1.json",
  "source_sha256": "aa2463d659dcce0272e4a1954d2f0e0ac1de2519b56334e15e5b9a8b29cffa17",
  "retrieved_utc": "2026-11-02T04:29:58.706491+00:00",
  "json_pointer": "/organism",
  "excerpt": "{\"lineage\":[\"Bacteria\",\"Pseudomonadati\",\"Pseudomonadota\",\"Gammaproteobacteria\",\"Alteromonadales\",\"Pseudoalteromonadaceae\",\"Pseudoalteromonas\"],\"scientificName\":\"Pseudoalteromonas sp\",\"taxonId\":53249}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXZ1.json)

```json
{
  "evidence_id": "C4",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXZ1.json",
  "source_sha256": "aa2463d659dcce0272e4a1954d2f0e0ac1de2519b56334e15e5b9a8b29cffa17",
  "retrieved_utc": "2026-11-02T04:29:58.706491+00:00",
  "json_pointer": "/proteinDescription",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"36690779\",\"source\":\"PubMed\"}],\"value\":\"2.3.1.312\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"D-glutamate N-acetyltransferase\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXZ1.json)

```json
{
  "evidence_id": "C5",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXZ1.json",
  "source_sha256": "aa2463d659dcce0272e4a1954d2f0e0ac1de2519b56334e15e5b9a8b29cffa17",
  "retrieved_utc": "2026-11-02T04:29:58.706491+00:00",
  "json_pointer": "/comments/1",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"36690779\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:76496\"}}],\"reaction\":{\"ecNumber\":\"2.3.1.312\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"36690779\",\"source\":\"PubMed\"}],\"name\":\"D-glutamate + acetyl-CoA = N-acetyl-D-glutamate + CoA + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:76495\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:29986\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57287\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57288\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:195260\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXZ1.json)

```json
{
  "evidence_id": "C6",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXZ1.json",
  "source_sha256": "aa2463d659dcce0272e4a1954d2f0e0ac1de2519b56334e15e5b9a8b29cffa17",
  "retrieved_utc": "2026-11-02T04:29:58.706491+00:00",
  "json_pointer": "/comments/2",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"ecNumber\":\"2.3.1.312\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"36690779\",\"source\":\"PubMed\"}],\"name\":\"D-aspartate + acetyl-CoA = N-acetyl-D-aspartate + CoA + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:76551\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:29990\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57287\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57288\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:195274\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXZ1.json)

```json
{
  "evidence_id": "C7",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXZ1.json",
  "source_sha256": "aa2463d659dcce0272e4a1954d2f0e0ac1de2519b56334e15e5b9a8b29cffa17",
  "retrieved_utc": "2026-11-02T04:29:58.706491+00:00",
  "json_pointer": "/comments/3",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"ecNumber\":\"2.3.1.312\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"36690779\",\"source\":\"PubMed\"}],\"name\":\"D-glutamine + acetyl-CoA = N-acetyl-D-glutamine + CoA + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:76547\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57287\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57288\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:58000\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:143880\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXZ1.json)

```json
{
  "evidence_id": "C8",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXZ1.json",
  "source_sha256": "aa2463d659dcce0272e4a1954d2f0e0ac1de2519b56334e15e5b9a8b29cffa17",
  "retrieved_utc": "2026-11-02T04:29:58.706491+00:00",
  "json_pointer": "/references/0",
  "excerpt": "{\"citation\":{\"authors\":[\"Yu Y.\",\"Wang P.\",\"Cao H.Y.\",\"Teng Z.J.\",\"Zhu Y.\",\"Wang M.\",\"McMinn A.\",\"Chen Y.\",\"Xiang H.\",\"Zhang Y.Z.\",\"Chen X.L.\",\"Zhang Y.Q.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"36690779\"},{\"database\":\"DOI\",\"id\":\"10.1038/s41396-023-01364-6\"}],\"citationType\":\"journal article\",\"firstPage\":\"537\",\"id\":\"36690779\",\"journal\":\"ISME J.\",\"lastPage\":\"548\",\"publicationDate\":\"2023\",\"title\":\"Novel D-glutamate catabolic pathway in marine Proteobacteria and halophilic archaea.\",\"volume\":\"17\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"CF6-2\"}],\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [GENOMIC DNA]\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"INDUCTION\",\"DISRUPTION PHENOTYPE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXZ1?format=txt&versions=3)

```json
{
  "evidence_id": "H1",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/P0DXZ1?format=txt&versions=3",
  "source_sha256": "f028fea1879dfe3aaa57742281e0eecbec1a2030f44e9354a914347ae6b4be60",
  "retrieved_utc": "2026-11-02T04:30:00.858326+00:00",
  "source_locator": "lines 1-12",
  "excerpt": "ID   DGCN_PSEAS              Reviewed;         332 AA.\nAC   P0DXZ1;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   09-APR-2025, sequence version 1.\nDT   28-JAN-2026, entry version 3.\nDE   RecName: Full=D-glutamate N-acetyltransferase {ECO:0000305};\nDE            EC=2.3.1.312 {ECO:0000269|PubMed:36690779};\nGN   Name=dgcN {ECO:0000303|PubMed:36690779};\nOS   Pseudoalteromonas sp.\nOC   Bacteria; Pseudomonadati; Pseudomonadota; Gammaproteobacteria;\nOC   Alteromonadales; Pseudoalteromonadaceae; Pseudoalteromonas.\nOX   NCBI_TaxID=53249;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 3,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXZ1?format=txt&versions=3)

```json
{
  "evidence_id": "H2",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/P0DXZ1?format=txt&versions=3",
  "source_sha256": "f028fea1879dfe3aaa57742281e0eecbec1a2030f44e9354a914347ae6b4be60",
  "retrieved_utc": "2026-11-02T04:30:00.858326+00:00",
  "source_locator": "lines 6-7",
  "excerpt": "DE   RecName: Full=D-glutamate N-acetyltransferase {ECO:0000305};\nDE            EC=2.3.1.312 {ECO:0000269|PubMed:36690779};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 3,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXZ1?format=txt&versions=3)

```json
{
  "evidence_id": "H3",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/P0DXZ1?format=txt&versions=3",
  "source_sha256": "f028fea1879dfe3aaa57742281e0eecbec1a2030f44e9354a914347ae6b4be60",
  "retrieved_utc": "2026-11-02T04:30:00.858326+00:00",
  "source_locator": "lines 13-22",
  "excerpt": "RN   [1]\nRP   NUCLEOTIDE SEQUENCE [GENOMIC DNA], FUNCTION, CATALYTIC ACTIVITY, INDUCTION,\nRP   AND DISRUPTION PHENOTYPE.\nRC   STRAIN=CF6-2;\nRX   PubMed=36690779; DOI=10.1038/s41396-023-01364-6;\nRA   Yu Y., Wang P., Cao H.Y., Teng Z.J., Zhu Y., Wang M., McMinn A., Chen Y.,\nRA   Xiang H., Zhang Y.Z., Chen X.L., Zhang Y.Q.;\nRT   \"Novel D-glutamate catabolic pathway in marine Proteobacteria and\nRT   halophilic archaea.\";\nRL   ISME J. 17:537-548(2023).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 3,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXZ1?format=txt&versions=3)

```json
{
  "evidence_id": "H4",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/P0DXZ1?format=txt&versions=3",
  "source_sha256": "f028fea1879dfe3aaa57742281e0eecbec1a2030f44e9354a914347ae6b4be60",
  "retrieved_utc": "2026-11-02T04:30:00.858326+00:00",
  "source_locator": "lines 31-37",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=D-glutamate + acetyl-CoA = N-acetyl-D-glutamate + CoA + H(+);\nCC         Xref=Rhea:RHEA:76495, ChEBI:CHEBI:15378, ChEBI:CHEBI:29986,\nCC         ChEBI:CHEBI:57287, ChEBI:CHEBI:57288, ChEBI:CHEBI:195260;\nCC         EC=2.3.1.312; Evidence={ECO:0000269|PubMed:36690779};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:76496;\nCC         Evidence={ECO:0000269|PubMed:36690779};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 3,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXZ1?format=txt&versions=3)

```json
{
  "evidence_id": "H5",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/P0DXZ1?format=txt&versions=3",
  "source_sha256": "f028fea1879dfe3aaa57742281e0eecbec1a2030f44e9354a914347ae6b4be60",
  "retrieved_utc": "2026-11-02T04:30:00.858326+00:00",
  "source_locator": "lines 38-42",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=D-aspartate + acetyl-CoA = N-acetyl-D-aspartate + CoA + H(+);\nCC         Xref=Rhea:RHEA:76551, ChEBI:CHEBI:15378, ChEBI:CHEBI:29990,\nCC         ChEBI:CHEBI:57287, ChEBI:CHEBI:57288, ChEBI:CHEBI:195274;\nCC         EC=2.3.1.312; Evidence={ECO:0000269|PubMed:36690779};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 3,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXZ1?format=txt&versions=3)

```json
{
  "evidence_id": "H6",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/P0DXZ1?format=txt&versions=3",
  "source_sha256": "f028fea1879dfe3aaa57742281e0eecbec1a2030f44e9354a914347ae6b4be60",
  "retrieved_utc": "2026-11-02T04:30:00.858326+00:00",
  "source_locator": "lines 43-47",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=D-glutamine + acetyl-CoA = N-acetyl-D-glutamine + CoA + H(+);\nCC         Xref=Rhea:RHEA:76547, ChEBI:CHEBI:15378, ChEBI:CHEBI:57287,\nCC         ChEBI:CHEBI:57288, ChEBI:CHEBI:58000, ChEBI:CHEBI:143880;\nCC         EC=2.3.1.312; Evidence={ECO:0000269|PubMed:36690779};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 3,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 82. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
