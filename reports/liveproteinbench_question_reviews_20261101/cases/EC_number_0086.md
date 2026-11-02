# EC_number_0086

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `EC_number`  
**Author expected answer:** **B** — 3.2.1.18

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

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
<summary>Original system instructions, verbatim</summary>

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

## GPT-6 Luna

**Saved status:** `valid_review`.

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

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

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

## Existing project source checks of Luna’s review

The notes below were prepared for specific claims in the Luna review. They are not independent validation of Qwen’s claims, expert adjudication, or replacement verdicts.

## Project source-check notes

These project-authored, AI-assisted checks assess specific source claims. They are not expert adjudication and do not replace Luna’s saved review or the author key.

No additional case-specific project note was recorded. Citation membership checks do not establish that every scientific argument is correct.

## Reviewer-only source evidence

**Both reviewers received this source evidence separately from the original question. It was not available to the original evaluated model.** Source support and reasoning from the original sequence/choices are distinct assessments.

**Accession:** `Q8QV65` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 114. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8QV65.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:24.225587+00:00.  

```json
"Q8QV65"
```

Source SHA-256: `bc4438119d1c029de1baa6feae7ea6afaed8e7e0d19410c4fed725f8fcb3753b`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8QV65.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:24.225587+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q9WAF5","source":"UniProtKB"}],"value":"3.2.1.18"}],"fullName":{"value":"Hemagglutinin-neuraminidase"}}}
```

Source SHA-256: `bc4438119d1c029de1baa6feae7ea6afaed8e7e0d19410c4fed725f8fcb3753b`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8QV65.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:24.225587+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"3.2.1.18","evidences":[{"evidenceCode":"ECO:0000250","id":"Q9WAF5","source":"UniProtKB"}],"name":"Hydrolysis of alpha-(2->3)-, alpha-(2->6)-, alpha-(2->8)- glycosidic linkages of terminal sialic acid residues in oligosaccharides, glycoproteins, glycolipids, colominic acid and synthetic substrates."}}
```

Source SHA-256: `bc4438119d1c029de1baa6feae7ea6afaed8e7e0d19410c4fed725f8fcb3753b`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8QV65?format=txt&versions=114)  
**Locator:** `lines 1-14`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 114 / 1.  
**Retrieved:** 2026-11-02T04:32:27.640645+00:00.  

```text
ID   HN_MUMPJ                Reviewed;         582 AA.
AC   Q8QV65; C7C5S5;
DT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.
DT   01-JUN-2002, sequence version 1.
DT   28-JAN-2026, entry version 114.
DE   RecName: Full=Hemagglutinin-neuraminidase;
DE            EC=3.2.1.18 {ECO:0000250|UniProtKB:Q9WAF5};
GN   Name=HN;
OS   Mumps virus genotype A (strain Jeryl-Lynn) (MuV).
OC   Viruses; Riboviria; Orthornavirae; Negarnaviricota; Haploviricotina;
OC   Monjiviricetes; Mononegavirales; Paramyxoviridae; Rubulavirinae;
OC   Orthorubulavirus; Orthorubulavirus parotitidis; Mumps orthorubulavirus.
OX   NCBI_TaxID=11168;
OH   NCBI_TaxID=9606; Homo sapiens (Human).
```

Source SHA-256: `32a38cacb11cc75414f260107fe816d041e5d43d9075624a51461e99158215ec`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8QV65?format=txt&versions=114)  
**Locator:** `lines 6-7`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 114 / 1.  
**Retrieved:** 2026-11-02T04:32:27.640645+00:00.  

```text
DE   RecName: Full=Hemagglutinin-neuraminidase;
DE            EC=3.2.1.18 {ECO:0000250|UniProtKB:Q9WAF5};
```

Source SHA-256: `32a38cacb11cc75414f260107fe816d041e5d43d9075624a51461e99158215ec`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8QV65?format=txt&versions=114)  
**Locator:** `lines 50-55`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 114 / 1.  
**Retrieved:** 2026-11-02T04:32:27.640645+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=Hydrolysis of alpha-(2->3)-, alpha-(2->6)-, alpha-
CC         (2->8)- glycosidic linkages of terminal sialic acid residues in
CC         oligosaccharides, glycoproteins, glycolipids, colominic acid and
CC         synthetic substrates.; EC=3.2.1.18;
CC         Evidence={ECO:0000250|UniProtKB:Q9WAF5};
```

Source SHA-256: `32a38cacb11cc75414f260107fe816d041e5d43d9075624a51461e99158215ec`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 86. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
