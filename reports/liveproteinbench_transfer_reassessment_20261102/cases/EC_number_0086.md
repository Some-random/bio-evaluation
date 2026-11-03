# EC_number_0086: before and after transfer clarification

[All 1,328 cases](../README.md) · [Method](../METHOD.md) · [Summary](../SUMMARY.md) · [Exact reviewer user message](../inputs/EC_number_0086.txt)

**Task:** `EC_number`  
**Author key, unchanged:** **B** — 3.2.1.18

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
MEPSKLFIMSDNATFAPGPVVNAAGKKTFRTCFRILVLSVQAVTLILVIVTLGELIRMINDQGLSNQLSSITDKIRESAAMIASAVGVMNQVIHGVTVSLPLQIEGNQNQLLSTLATICTNRNQVSNCSTNIPLVNDLRFINGINKFIIEDYATHDFSIGHPLNMPSFIPTATSPNGCTRIPSFSLGKTHWCYTHNVINANCKDHTSSNQYVSMGILVQTASGYPMFKTLKIQYLSDGLNRKSCSIATVPDGCAMYCYVSTQLETDDYAGSSPPTQKLTLLFYNDTIKERTISPSGLEGNWATLVPGVGSGIYFENKLIFPAYGGVLPNSTLGVKSAREFFRPVNPYNPCSGPPQELDQRALRSYFPSYFSSRRVQSAFLVCAWNQILVTNCELVVPSNNQTLMGAEGRVLLINNRLLYYQRSTSWWPYELLYEISFTFTNSGQSSVNMSWIPIYSFTRPGLGKCSGENICPTVCVSGVYLDPWPLTPYSHQSGINRNFYFTGALLNSSTTRVNPTLYVSALNNLKVLAPYGTQGLFASYTTTTCFQDTGDASVYCVYIMELASNIVGEFQILPVLARLTIT

[Multiple Choices]
A. 3.2.1.20
B. 3.2.1.18
C. 1.14.19.80
D. 4.2.1.183
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

> The exact sequence matches UniProtKB Q8QV65, annotated as mumps virus hemagglutinin-neuraminidase with EC 3.2.1.18. The catalytic-activity annotation specifies hydrolysis of terminal sialic-acid linkages. Its evidence is transferred from another UniProtKB entry (ECO:0000250), so this supports the annotation but is not direct experimental evidence for this sequence.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence is consistent with a viral membrane glycoprotein, which makes some options less plausible, but that broad context does not establish the specific catalytic activity or substrate needed to distinguish EC 3.2.1.18 from other glycosidases.


**Missing item-specific fact**

> The protein-specific identification as mumps virus hemagglutinin-neuraminidase, or evidence that it hydrolyzes terminal sialic-acid linkages, is absent from the question.


**Reason**

> Choosing the precise EC number depends on protein-specific functional annotation or equivalent evidence, not a general biological inference available from the sequence and choices alone.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The matched UniProt annotation supports choice B; the other listed EC numbers describe different activities.


### Important caveats

- The reviewer-only accession and annotations were not supplied to the evaluated model.
- The annotation evidence is transferred from a related entry rather than direct experimental evidence for this sequence.
- The author's exact source snapshot is unknown, although a historical entry with an exact sequence match was retrieved.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with a viral membrane glycoprotein, which makes some options less plausible, but that broad context does not establish the specific catalytic activity or substrate needed to distinguish EC 3.2.1.18 from other glycosidases.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific identification as mumps virus hemagglutinin-neuraminidase, or evidence that it hydrolyzes terminal sialic-acid linkages, is absent from the question.",
    "reason": "Choosing the precise EC number depends on protein-specific functional annotation or equivalent evidence, not a general biological inference available from the sequence and choices alone."
  },
  "case_id": "EC_number_0086",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H2",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches UniProtKB Q8QV65, annotated as mumps virus hemagglutinin-neuraminidase with EC 3.2.1.18. The catalytic-activity annotation specifies hydrolysis of terminal sialic-acid linkages. Its evidence is transferred from another UniProtKB entry (ECO:0000250), so this supports the annotation but is not direct experimental evidence for this sequence."
  },
  "important_caveats": [
    "The reviewer-only accession and annotations were not supplied to the evaluated model.",
    "The annotation evidence is transferred from a related entry rather than direct experimental evidence for this sequence.",
    "The author's exact source snapshot is unknown, although a historical entry with an exact sequence match was retrieved."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched UniProt annotation supports choice B; the other listed EC numbers describe different activities."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0086",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches UniProtKB Q8QV65, annotated as mumps virus hemagglutinin-neuraminidase with EC 3.2.1.18. The catalytic-activity annotation specifies hydrolysis of terminal sialic-acid linkages. Its evidence is transferred from another UniProtKB entry (ECO:0000250), so this supports the annotation but is not direct experimental evidence for this sequence.",
    "evidence_ids": ["C1", "C4", "C5", "H2", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence is consistent with a viral membrane glycoprotein, which makes some options less plausible, but that broad context does not establish the specific catalytic activity or substrate needed to distinguish EC 3.2.1.18 from other glycosidases.",
    "missing_item_specific_fact": "The protein-specific identification as mumps virus hemagglutinin-neuraminidase, or evidence that it hydrolyzes terminal sialic-acid linkages, is absent from the question.",
    "reason": "Choosing the precise EC number depends on protein-specific functional annotation or equivalent evidence, not a general biological inference available from the sequence and choices alone."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched UniProt annotation supports choice B; the other listed EC numbers describe different activities."
  },
  "important_caveats": [
    "The reviewer-only accession and annotations were not supplied to the evaluated model.",
    "The annotation evidence is transferred from a related entry rather than direct experimental evidence for this sequence.",
    "The author's exact source snapshot is unknown, although a historical entry with an exact sequence match was retrieved."
  ]
}
```

</details>

## Before: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence matches UniProt Q8QV65 (Mumps virus Jeryl-Lynn HN protein, 582 aa, sequence SHA-256 confirmed). The current and historical (v114) UniProt entries annotate this protein as Hemagglutinin-neuraminidase with EC 3.2.1.18 (exo-alpha-sialidase), catalyzing hydrolysis of alpha-(2→3)-, alpha-(2→6)-, alpha-(2→8)-glycosidic linkages of terminal sialic acid residues. The evidence code is ECO:0000250 (similarity transfer from Q9WAF5), so the annotation is computational/inferred rather than directly experimental for this exact sequence, but paramyxovirus HN neuraminidase activity is well-established in the literature. The expected answer B (3.2.1.18) is consistent with the annotation.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> A general virology argument exists: recognizing the sequence as a paramyxovirus surface glycoprotein (signal peptide at N-terminus, transmembrane anchor, multiple N-linked glycosylation sites) and recalling that paramyxovirus HN proteins possess neuraminidase (sialidase) activity would point to EC 3.2.1.18. However, this requires identifying the specific protein family and recalling its functional annotation rather than deriving the EC number from catalytic motifs visible in the sequence. The neuraminidase catalytic residues (conserved Arg, Tyr, Asp in a beta-propeller) are not readily identifiable in the raw 582-aa sequence without prior structural/family knowledge.


**Missing item-specific fact**

> Recognition that this specific 582-aa sequence is the Mumps virus HN glycoprotein (or a paramyxovirus HN protein) and the associated knowledge that HN proteins carry exo-alpha-sialidase (neuraminidase) activity. Without this protein-specific identification, the raw sequence does not present obvious catalytic motifs that would allow reasoning to distinguish EC 3.2.1.18 from EC 3.2.1.20 (alpha-N-acetylglucosaminidase) or the unrelated options C and D.


**Reason**

> The question requires identifying a specific viral protein and recalling its enzymatic function. While the distractors span different EC classes (glycosidase vs monooxygenase vs lyase), narrowing to the correct glycosidase subtype (3.2.1.18 vs 3.2.1.20) demands knowledge of the protein's identity and substrate specificity that is not derivable from sequence features alone. This is essentially a lookup of the UniProt annotation for Q8QV65.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options span three EC classes (3.2.1.x glycosidases, 1.14.x.x oxidoreductases, 4.2.x.x lyases), so options C and D are clearly wrong for a glycosidase. Between A (3.2.1.20, alpha-N-acetylglucosaminidase) and B (3.2.1.18, exo-alpha-sialidase), the annotation unambiguously supports B. No genuine ambiguity among the options given the protein identity.


### Important caveats

- The EC annotation carries evidence code ECO:0000250 (similarity transfer from Q9WAF5), meaning it is not a direct experimental measurement on this exact Jeryl-Lynn sequence, though neuraminidase activity of paramyxovirus HN proteins is broadly well-characterized.
- The UniProt entry was first public in April 2025; the benchmark's construction date is unknown, so the author may have used an earlier or different source.
- The reviewer-only accession (Q8QV65) was inferred from dataset image-path metadata and was not available to the evaluated model.
- The sequence is 582 aa and matches the canonical entry exactly; no isoform or construct numbering issues apply.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "A general virology argument exists: recognizing the sequence as a paramyxovirus surface glycoprotein (signal peptide at N-terminus, transmembrane anchor, multiple N-linked glycosylation sites) and recalling that paramyxovirus HN proteins possess neuraminidase (sialidase) activity would point to EC 3.2.1.18. However, this requires identifying the specific protein family and recalling its functional annotation rather than deriving the EC number from catalytic motifs visible in the sequence. The neuraminidase catalytic residues (conserved Arg, Tyr, Asp in a beta-propeller) are not readily identifiable in the raw 582-aa sequence without prior structural/family knowledge.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "Recognition that this specific 582-aa sequence is the Mumps virus HN glycoprotein (or a paramyxovirus HN protein) and the associated knowledge that HN proteins carry exo-alpha-sialidase (neuraminidase) activity. Without this protein-specific identification, the raw sequence does not present obvious catalytic motifs that would allow reasoning to distinguish EC 3.2.1.18 from EC 3.2.1.20 (alpha-N-acetylglucosaminidase) or the unrelated options C and D.",
    "reason": "The question requires identifying a specific viral protein and recalling its enzymatic function. While the distractors span different EC classes (glycosidase vs monooxygenase vs lyase), narrowing to the correct glycosidase subtype (3.2.1.18 vs 3.2.1.20) demands knowledge of the protein's identity and substrate specificity that is not derivable from sequence features alone. This is essentially a lookup of the UniProt annotation for Q8QV65."
  },
  "case_id": "EC_number_0086",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H1",
      "H2",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The sequence matches UniProt Q8QV65 (Mumps virus Jeryl-Lynn HN protein, 582 aa, sequence SHA-256 confirmed). The current and historical (v114) UniProt entries annotate this protein as Hemagglutinin-neuraminidase with EC 3.2.1.18 (exo-alpha-sialidase), catalyzing hydrolysis of alpha-(2→3)-, alpha-(2→6)-, alpha-(2→8)-glycosidic linkages of terminal sialic acid residues. The evidence code is ECO:0000250 (similarity transfer from Q9WAF5), so the annotation is computational/inferred rather than directly experimental for this exact sequence, but paramyxovirus HN neuraminidase activity is well-established in the literature. The expected answer B (3.2.1.18) is consistent with the annotation."
  },
  "important_caveats": [
    "The EC annotation carries evidence code ECO:0000250 (similarity transfer from Q9WAF5), meaning it is not a direct experimental measurement on this exact Jeryl-Lynn sequence, though neuraminidase activity of paramyxovirus HN proteins is broadly well-characterized.",
    "The UniProt entry was first public in April 2025; the benchmark's construction date is unknown, so the author may have used an earlier or different source.",
    "The reviewer-only accession (Q8QV65) was inferred from dataset image-path metadata and was not available to the evaluated model.",
    "The sequence is 582 aa and matches the canonical entry exactly; no isoform or construct numbering issues apply."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span three EC classes (3.2.1.x glycosidases, 1.14.x.x oxidoreductases, 4.2.x.x lyases), so options C and D are clearly wrong for a glycosidase. Between A (3.2.1.20, alpha-N-acetylglucosaminidase) and B (3.2.1.18, exo-alpha-sialidase), the annotation unambiguously supports B. No genuine ambiguity among the options given the protein identity."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0086",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches UniProt Q8QV65 (Mumps virus Jeryl-Lynn HN protein, 582 aa, sequence SHA-256 confirmed). The current and historical (v114) UniProt entries annotate this protein as Hemagglutinin-neuraminidase with EC 3.2.1.18 (exo-alpha-sialidase), catalyzing hydrolysis of alpha-(2→3)-, alpha-(2→6)-, alpha-(2→8)-glycosidic linkages of terminal sialic acid residues. The evidence code is ECO:0000250 (similarity transfer from Q9WAF5), so the annotation is computational/inferred rather than directly experimental for this exact sequence, but paramyxovirus HN neuraminidase activity is well-established in the literature. The expected answer B (3.2.1.18) is consistent with the annotation.",
    "evidence_ids": ["C1", "C4", "C5", "H1", "H2", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "A general virology argument exists: recognizing the sequence as a paramyxovirus surface glycoprotein (signal peptide at N-terminus, transmembrane anchor, multiple N-linked glycosylation sites) and recalling that paramyxovirus HN proteins possess neuraminidase (sialidase) activity would point to EC 3.2.1.18. However, this requires identifying the specific protein family and recalling its functional annotation rather than deriving the EC number from catalytic motifs visible in the sequence. The neuraminidase catalytic residues (conserved Arg, Tyr, Asp in a beta-propeller) are not readily identifiable in the raw 582-aa sequence without prior structural/family knowledge.",
    "missing_item_specific_fact": "Recognition that this specific 582-aa sequence is the Mumps virus HN glycoprotein (or a paramyxovirus HN protein) and the associated knowledge that HN proteins carry exo-alpha-sialidase (neuraminidase) activity. Without this protein-specific identification, the raw sequence does not present obvious catalytic motifs that would allow reasoning to distinguish EC 3.2.1.18 from EC 3.2.1.20 (alpha-N-acetylglucosaminidase) or the unrelated options C and D.",
    "reason": "The question requires identifying a specific viral protein and recalling its enzymatic function. While the distractors span different EC classes (glycosidase vs monooxygenase vs lyase), narrowing to the correct glycosidase subtype (3.2.1.18 vs 3.2.1.20) demands knowledge of the protein's identity and substrate specificity that is not derivable from sequence features alone. This is essentially a lookup of the UniProt annotation for Q8QV65."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span three EC classes (3.2.1.x glycosidases, 1.14.x.x oxidoreductases, 4.2.x.x lyases), so options C and D are clearly wrong for a glycosidase. Between A (3.2.1.20, alpha-N-acetylglucosaminidase) and B (3.2.1.18, exo-alpha-sialidase), the annotation unambiguously supports B. No genuine ambiguity among the options given the protein identity."
  },
  "important_caveats": [
    "The EC annotation carries evidence code ECO:0000250 (similarity transfer from Q9WAF5), meaning it is not a direct experimental measurement on this exact Jeryl-Lynn sequence, though neuraminidase activity of paramyxovirus HN proteins is broadly well-characterized.",
    "The UniProt entry was first public in April 2025; the benchmark's construction date is unknown, so the author may have used an earlier or different source.",
    "The reviewer-only accession (Q8QV65) was inferred from dataset image-path metadata and was not available to the evaluated model.",
    "The sequence is 582 aa and matches the canonical entry exactly; no isoform or construct numbering issues apply."
  ]
}
```

</details>

## After: GPT-6 Luna

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence-matched UniProt records assign EC 3.2.1.18 and describe hydrolysis of terminal sialic-acid linkages, supporting choice B. The annotation is transferred from a related protein (ECO:0000250), not direct experimental evidence for this exact protein in the supplied excerpts.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence’s N-terminal membrane anchor followed by a large extracellular domain is characteristic of paramyxovirus hemagglutinin-neuraminidase proteins; family-level recognition and the conserved sialidase function of such proteins support neuraminidase EC 3.2.1.18 (B). The alternatives describe unrelated enzyme activities, including alpha-glucosidase (A), a desaturase (C), and a lyase (D).


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A transferable viral glycoprotein-family inference meaningfully distinguishes B from the offered alternatives, although the sequence pattern alone need not prove the exact substrate range or experimentally establish the activity.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the offered choices, the neuraminidase classification is distinct; no other option is comparably supported by the sequence and family-level inference.


### Important caveats

- The database assignment is homology-transferred rather than direct experimental evidence for this sequence in the supplied excerpts.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence’s N-terminal membrane anchor followed by a large extracellular domain is characteristic of paramyxovirus hemagglutinin-neuraminidase proteins; family-level recognition and the conserved sialidase function of such proteins support neuraminidase EC 3.2.1.18 (B). The alternatives describe unrelated enzyme activities, including alpha-glucosidase (A), a desaturase (C), and a lyase (D).",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A transferable viral glycoprotein-family inference meaningfully distinguishes B from the offered alternatives, although the sequence pattern alone need not prove the exact substrate range or experimentally establish the activity."
  },
  "case_id": "EC_number_0086",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt records assign EC 3.2.1.18 and describe hydrolysis of terminal sialic-acid linkages, supporting choice B. The annotation is transferred from a related protein (ECO:0000250), not direct experimental evidence for this exact protein in the supplied excerpts."
  },
  "important_caveats": [
    "The database assignment is homology-transferred rather than direct experimental evidence for this sequence in the supplied excerpts."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the offered choices, the neuraminidase classification is distinct; no other option is comparably supported by the sequence and family-level inference."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0086",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt records assign EC 3.2.1.18 and describe hydrolysis of terminal sialic-acid linkages, supporting choice B. The annotation is transferred from a related protein (ECO:0000250), not direct experimental evidence for this exact protein in the supplied excerpts.",
    "evidence_ids": ["C4", "C5", "H2", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence’s N-terminal membrane anchor followed by a large extracellular domain is characteristic of paramyxovirus hemagglutinin-neuraminidase proteins; family-level recognition and the conserved sialidase function of such proteins support neuraminidase EC 3.2.1.18 (B). The alternatives describe unrelated enzyme activities, including alpha-glucosidase (A), a desaturase (C), and a lyase (D).",
    "missing_item_specific_fact": "",
    "reason": "A transferable viral glycoprotein-family inference meaningfully distinguishes B from the offered alternatives, although the sequence pattern alone need not prove the exact substrate range or experimentally establish the activity."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the offered choices, the neuraminidase classification is distinct; no other option is comparably supported by the sequence and family-level inference."
  },
  "important_caveats": [
    "The database assignment is homology-transferred rather than direct experimental evidence for this sequence in the supplied excerpts."
  ]
}
```

</details>

## After: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry Q8QV65 (HN_MUMPJ, Mumps virus Hemagglutinin-neuraminidase) lists EC 3.2.1.18 with catalytic activity described as hydrolysis of alpha-(2->3)-, alpha-(2->6)-, alpha-(2->8)- glycosidic linkages of terminal sialic acid residues. The annotation uses evidence code ECO:0000250 (inferred by similarity from Q9WAF5, another paramyxovirus HN protein), indicating a family-level transfer rather than direct experimental measurement, but the assignment is consistent with the well-characterized neuraminidase activity of paramyxovirus HN proteins.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 582-aa sequence displays the hallmark architecture of a paramyxovirus surface glycoprotein: an N-terminal signal peptide (MEPSKLFIMSDNATFAPGPVVNAAGKK), followed by a hydrophobic transmembrane domain (~residues 28-52), a stalk region, and a large globular head domain with multiple conserved cysteines (disulfide bonds) and N-glycosylation sequons (N-X-S/T). This architecture, combined with the ~580-aa length, is highly characteristic of the paramyxovirus Hemagglutinin-Neuraminidase (HN) protein family. The HN protein's catalytic function is neuraminidase (exo-alpha-sialidase, EC 3.2.1.18), belonging to glycoside hydrolase family 33 (GH33), which is a defining, well-known property of this entire protein family across paramyxoviruses. Among the four choices: (A) 3.2.1.20 is alpha-galactosidase (GH27 family, a small soluble enzyme with completely different architecture); (C) 1.14.19.80 is an oxidoreductase (wrong enzyme class entirely); (D) 4.2.1.183 is a lyase (wrong mechanism). Only 3.2.1.18 matches the neuraminidase catalytic activity inherent to the paramyxovirus HN protein family. Recognizing the viral surface glycoprotein architecture and knowing that HN proteins are sialidases/neuraminidases is transferable family-level knowledge, not memorization of this specific protein's database entry.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A model can recognize the paramyxovirus HN protein family from the sequence architecture (signal peptide + TM domain + globular head with Cys/N-glyc pattern, ~580 aa) and apply the well-established fact that HN proteins catalyze neuraminidase (sialidase) reactions assigned EC 3.2.1.18. The other three choices belong to entirely different enzyme classes (different glycosidase specificity, oxidoreductase, lyase) incompatible with the observed viral surface glycoprotein architecture. This is a legitimate family-level inference from conserved structural and sequence features shared across paramyxovirus HN proteins.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four choices span three different enzyme classes (glycosidases of different specificity, oxidoreductase, lyase). The viral surface glycoprotein architecture and paramyxovirus HN family features clearly point to neuraminidase (3.2.1.18) and exclude the other options. No ambiguity exists among the offered alternatives.


### Important caveats

- The UniProt annotation uses evidence code ECO:0000250 (similarity-based transfer from Q9WAF5), meaning the EC assignment is inferred by homology rather than direct experimental assay on this specific mumps virus HN protein.
- The hemagglutinin (receptor-binding) activity of HN proteins is not separately assigned an EC number; only the neuraminidase catalytic activity receives the EC 3.2.1.18 designation.
- The reviewer-only evidence confirms sequence match (582 aa, SHA256 match) but the evaluated model had no access to the accession, organism name, or annotation.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 582-aa sequence displays the hallmark architecture of a paramyxovirus surface glycoprotein: an N-terminal signal peptide (MEPSKLFIMSDNATFAPGPVVNAAGKK), followed by a hydrophobic transmembrane domain (~residues 28-52), a stalk region, and a large globular head domain with multiple conserved cysteines (disulfide bonds) and N-glycosylation sequons (N-X-S/T). This architecture, combined with the ~580-aa length, is highly characteristic of the paramyxovirus Hemagglutinin-Neuraminidase (HN) protein family. The HN protein's catalytic function is neuraminidase (exo-alpha-sialidase, EC 3.2.1.18), belonging to glycoside hydrolase family 33 (GH33), which is a defining, well-known property of this entire protein family across paramyxoviruses. Among the four choices: (A) 3.2.1.20 is alpha-galactosidase (GH27 family, a small soluble enzyme with completely different architecture); (C) 1.14.19.80 is an oxidoreductase (wrong enzyme class entirely); (D) 4.2.1.183 is a lyase (wrong mechanism). Only 3.2.1.18 matches the neuraminidase catalytic activity inherent to the paramyxovirus HN protein family. Recognizing the viral surface glycoprotein architecture and knowing that HN proteins are sialidases/neuraminidases is transferable family-level knowledge, not memorization of this specific protein's database entry.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A model can recognize the paramyxovirus HN protein family from the sequence architecture (signal peptide + TM domain + globular head with Cys/N-glyc pattern, ~580 aa) and apply the well-established fact that HN proteins catalyze neuraminidase (sialidase) reactions assigned EC 3.2.1.18. The other three choices belong to entirely different enzyme classes (different glycosidase specificity, oxidoreductase, lyase) incompatible with the observed viral surface glycoprotein architecture. This is a legitimate family-level inference from conserved structural and sequence features shared across paramyxovirus HN proteins."
  },
  "case_id": "EC_number_0086",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry Q8QV65 (HN_MUMPJ, Mumps virus Hemagglutinin-neuraminidase) lists EC 3.2.1.18 with catalytic activity described as hydrolysis of alpha-(2->3)-, alpha-(2->6)-, alpha-(2->8)- glycosidic linkages of terminal sialic acid residues. The annotation uses evidence code ECO:0000250 (inferred by similarity from Q9WAF5, another paramyxovirus HN protein), indicating a family-level transfer rather than direct experimental measurement, but the assignment is consistent with the well-characterized neuraminidase activity of paramyxovirus HN proteins."
  },
  "important_caveats": [
    "The UniProt annotation uses evidence code ECO:0000250 (similarity-based transfer from Q9WAF5), meaning the EC assignment is inferred by homology rather than direct experimental assay on this specific mumps virus HN protein.",
    "The hemagglutinin (receptor-binding) activity of HN proteins is not separately assigned an EC number; only the neuraminidase catalytic activity receives the EC 3.2.1.18 designation.",
    "The reviewer-only evidence confirms sequence match (582 aa, SHA256 match) but the evaluated model had no access to the accession, organism name, or annotation."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices span three different enzyme classes (glycosidases of different specificity, oxidoreductase, lyase). The viral surface glycoprotein architecture and paramyxovirus HN family features clearly point to neuraminidase (3.2.1.18) and exclude the other options. No ambiguity exists among the offered alternatives."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0086",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry Q8QV65 (HN_MUMPJ, Mumps virus Hemagglutinin-neuraminidase) lists EC 3.2.1.18 with catalytic activity described as hydrolysis of alpha-(2->3)-, alpha-(2->6)-, alpha-(2->8)- glycosidic linkages of terminal sialic acid residues. The annotation uses evidence code ECO:0000250 (inferred by similarity from Q9WAF5, another paramyxovirus HN protein), indicating a family-level transfer rather than direct experimental measurement, but the assignment is consistent with the well-characterized neuraminidase activity of paramyxovirus HN proteins.",
    "evidence_ids": ["C4", "C5", "H2", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 582-aa sequence displays the hallmark architecture of a paramyxovirus surface glycoprotein: an N-terminal signal peptide (MEPSKLFIMSDNATFAPGPVVNAAGKK), followed by a hydrophobic transmembrane domain (~residues 28-52), a stalk region, and a large globular head domain with multiple conserved cysteines (disulfide bonds) and N-glycosylation sequons (N-X-S/T). This architecture, combined with the ~580-aa length, is highly characteristic of the paramyxovirus Hemagglutinin-Neuraminidase (HN) protein family. The HN protein's catalytic function is neuraminidase (exo-alpha-sialidase, EC 3.2.1.18), belonging to glycoside hydrolase family 33 (GH33), which is a defining, well-known property of this entire protein family across paramyxoviruses. Among the four choices: (A) 3.2.1.20 is alpha-galactosidase (GH27 family, a small soluble enzyme with completely different architecture); (C) 1.14.19.80 is an oxidoreductase (wrong enzyme class entirely); (D) 4.2.1.183 is a lyase (wrong mechanism). Only 3.2.1.18 matches the neuraminidase catalytic activity inherent to the paramyxovirus HN protein family. Recognizing the viral surface glycoprotein architecture and knowing that HN proteins are sialidases/neuraminidases is transferable family-level knowledge, not memorization of this specific protein's database entry.",
    "missing_item_specific_fact": "",
    "reason": "A model can recognize the paramyxovirus HN protein family from the sequence architecture (signal peptide + TM domain + globular head with Cys/N-glyc pattern, ~580 aa) and apply the well-established fact that HN proteins catalyze neuraminidase (sialidase) reactions assigned EC 3.2.1.18. The other three choices belong to entirely different enzyme classes (different glycosidase specificity, oxidoreductase, lyase) incompatible with the observed viral surface glycoprotein architecture. This is a legitimate family-level inference from conserved structural and sequence features shared across paramyxovirus HN proteins."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices span three different enzyme classes (glycosidases of different specificity, oxidoreductase, lyase). The viral surface glycoprotein architecture and paramyxovirus HN family features clearly point to neuraminidase (3.2.1.18) and exclude the other options. No ambiguity exists among the offered alternatives."
  },
  "important_caveats": [
    "The UniProt annotation uses evidence code ECO:0000250 (similarity-based transfer from Q9WAF5), meaning the EC assignment is inferred by homology rather than direct experimental assay on this specific mumps virus HN protein.",
    "The hemagglutinin (receptor-binding) activity of HN proteins is not separately assigned an EC number; only the neuraminidase catalytic activity receives the EC 3.2.1.18 designation.",
    "The reviewer-only evidence confirms sequence match (582 aa, SHA256 match) but the evaluated model had no access to the accession, organism name, or annotation."
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
  "requested_accession": "Q8QV65",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "benchmark_sequence_sha256": "6c411ff86d03391238be03a02eacdb3e2948b7a46bfa5706f0f99e829e1e420f",
  "benchmark_sequence_length": 582,
  "current_status": "retrieved",
  "current_sequence_comparison": "matched",
  "current_entry_audit": {
    "entryVersion": 116,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2002-06-01",
    "sequenceVersion": 1
  },
  "current_uniprot_release": "2026_03",
  "current_record_sha256": "bc4438119d1c029de1baa6feae7ea6afaed8e7e0d19410c4fed725f8fcb3753b",
  "current_source_sequence_sha256": "6c411ff86d03391238be03a02eacdb3e2948b7a46bfa5706f0f99e829e1e420f",
  "current_source_sequence_length": 582,
  "historical_status": "retrieved",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "selected_historical_entry_version": 114,
  "selected_historical_version": {
    "accession": "Q8QV65",
    "database": "Swiss-Prot",
    "entryVersion": 114,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "HN_MUMPJ",
    "sequenceVersion": 1
  },
  "selected_historical_record_sha256": "32a38cacb11cc75414f260107fe816d041e5d43d9075624a51461e99158215ec",
  "selected_historical_source_sequence_sha256": "6c411ff86d03391238be03a02eacdb3e2948b7a46bfa5706f0f99e829e1e420f",
  "selected_historical_source_sequence_length": 582,
  "latest_at_cutoff_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 114,
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8QV65.json)

```json
{
  "evidence_id": "C1",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q8QV65.json",
  "source_sha256": "bc4438119d1c029de1baa6feae7ea6afaed8e7e0d19410c4fed725f8fcb3753b",
  "retrieved_utc": "2026-11-02T04:32:24.225587+00:00",
  "json_pointer": "/primaryAccession",
  "excerpt": "\"Q8QV65\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8QV65.json)

```json
{
  "evidence_id": "C2",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q8QV65.json",
  "source_sha256": "bc4438119d1c029de1baa6feae7ea6afaed8e7e0d19410c4fed725f8fcb3753b",
  "retrieved_utc": "2026-11-02T04:32:24.225587+00:00",
  "json_pointer": "/entryAudit",
  "excerpt": "{\"entryVersion\":116,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2002-06-01\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8QV65.json)

```json
{
  "evidence_id": "C3",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q8QV65.json",
  "source_sha256": "bc4438119d1c029de1baa6feae7ea6afaed8e7e0d19410c4fed725f8fcb3753b",
  "retrieved_utc": "2026-11-02T04:32:24.225587+00:00",
  "json_pointer": "/organism",
  "excerpt": "{\"commonName\":\"MuV\",\"lineage\":[\"Viruses\",\"Riboviria\",\"Orthornavirae\",\"Negarnaviricota\",\"Haploviricotina\",\"Monjiviricetes\",\"Mononegavirales\",\"Paramyxoviridae\",\"Rubulavirinae\",\"Orthorubulavirus\",\"Orthorubulavirus parotitidis\",\"Mumps orthorubulavirus\"],\"scientificName\":\"Mumps virus genotype A (strain Jeryl-Lynn)\",\"taxonId\":11168}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8QV65.json)

```json
{
  "evidence_id": "C4",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q8QV65.json",
  "source_sha256": "bc4438119d1c029de1baa6feae7ea6afaed8e7e0d19410c4fed725f8fcb3753b",
  "retrieved_utc": "2026-11-02T04:32:24.225587+00:00",
  "json_pointer": "/proteinDescription",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9WAF5\",\"source\":\"UniProtKB\"}],\"value\":\"3.2.1.18\"}],\"fullName\":{\"value\":\"Hemagglutinin-neuraminidase\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8QV65.json)

```json
{
  "evidence_id": "C5",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q8QV65.json",
  "source_sha256": "bc4438119d1c029de1baa6feae7ea6afaed8e7e0d19410c4fed725f8fcb3753b",
  "retrieved_utc": "2026-11-02T04:32:24.225587+00:00",
  "json_pointer": "/comments/2",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"ecNumber\":\"3.2.1.18\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9WAF5\",\"source\":\"UniProtKB\"}],\"name\":\"Hydrolysis of alpha-(2->3)-, alpha-(2->6)-, alpha-(2->8)- glycosidic linkages of terminal sialic acid residues in oligosaccharides, glycoproteins, glycolipids, colominic acid and synthetic substrates.\"}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8QV65?format=txt&versions=114)

```json
{
  "evidence_id": "H1",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q8QV65?format=txt&versions=114",
  "source_sha256": "32a38cacb11cc75414f260107fe816d041e5d43d9075624a51461e99158215ec",
  "retrieved_utc": "2026-11-02T04:32:27.640645+00:00",
  "source_locator": "lines 1-14",
  "excerpt": "ID   HN_MUMPJ                Reviewed;         582 AA.\nAC   Q8QV65; C7C5S5;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   01-JUN-2002, sequence version 1.\nDT   28-JAN-2026, entry version 114.\nDE   RecName: Full=Hemagglutinin-neuraminidase;\nDE            EC=3.2.1.18 {ECO:0000250|UniProtKB:Q9WAF5};\nGN   Name=HN;\nOS   Mumps virus genotype A (strain Jeryl-Lynn) (MuV).\nOC   Viruses; Riboviria; Orthornavirae; Negarnaviricota; Haploviricotina;\nOC   Monjiviricetes; Mononegavirales; Paramyxoviridae; Rubulavirinae;\nOC   Orthorubulavirus; Orthorubulavirus parotitidis; Mumps orthorubulavirus.\nOX   NCBI_TaxID=11168;\nOH   NCBI_TaxID=9606; Homo sapiens (Human).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 114,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8QV65?format=txt&versions=114)

```json
{
  "evidence_id": "H2",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q8QV65?format=txt&versions=114",
  "source_sha256": "32a38cacb11cc75414f260107fe816d041e5d43d9075624a51461e99158215ec",
  "retrieved_utc": "2026-11-02T04:32:27.640645+00:00",
  "source_locator": "lines 6-7",
  "excerpt": "DE   RecName: Full=Hemagglutinin-neuraminidase;\nDE            EC=3.2.1.18 {ECO:0000250|UniProtKB:Q9WAF5};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 114,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8QV65?format=txt&versions=114)

```json
{
  "evidence_id": "H3",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q8QV65?format=txt&versions=114",
  "source_sha256": "32a38cacb11cc75414f260107fe816d041e5d43d9075624a51461e99158215ec",
  "retrieved_utc": "2026-11-02T04:32:27.640645+00:00",
  "source_locator": "lines 50-55",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=Hydrolysis of alpha-(2->3)-, alpha-(2->6)-, alpha-\nCC         (2->8)- glycosidic linkages of terminal sialic acid residues in\nCC         oligosaccharides, glycoproteins, glycolipids, colominic acid and\nCC         synthetic substrates.; EC=3.2.1.18;\nCC         Evidence={ECO:0000250|UniProtKB:Q9WAF5};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 114,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 86. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
