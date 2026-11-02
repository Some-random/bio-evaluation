# pathway_0015

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `pathway`  
**Author expected answer:** **B** — Cofactor biosynthesis

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MAGSEPVSAEGESMAVDAAPRKPRILLAASGSVAAVKFANLCHCFSEWADVRAVSSSGSLHFIDRASMPKDVILYTDEDEWSSWKKLGDSVLHIELRKWADIMVIAPLSANTLGKIAGGLCDNLLTCIVRAWDYSKPFFVAPAMNTLMWNNPFTERHFISIDELGISLIPPVTKRLACGDYGNGAMAEPSTIYSTVRLFYESKAQQGRAVVTLR

[Multiple Choices]
A. L-threonine from L-aspartate: step 1/5. .
B. Cofactor biosynthesis
C. Glycolipid biosynthesis
D. L-cystathionine from O-succinyl-L-homoserine: step 1/1. .
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Protein Pathway Prediction, which is to predict the primary metabolic or signaling pathway in which a given protein functions. Biological pathways are series of chemical reactions occurring within a cell that are essential for life. Based on the protein's amino acid sequence, you should identify the most relevant pathway from the given options.. The inputs provided by the user for this task include:

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

> The exact sequence matches the soybean HAL3b/PPCDC entry, whose pathway annotation places it in cofactor and coenzyme A biosynthesis. The enzyme annotation is supported by transfer from a related UniProt entry, so this supports the keyed broad pathway without establishing that it was experimentally validated for this soybean protein.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence alone offers no clear general biological cue that distinguishes cofactor biosynthesis from the listed amino-acid or glycolipid pathways; identifying the relevant enzyme family requires protein-specific functional knowledge.


**Missing item-specific fact**

> The protein's identity as phosphopantothenoylcysteine decarboxylase (PPCDC), and its role in coenzyme A biosynthesis, is not supplied in the question.


**Reason**

> The answer is supported by an annotation for this exact sequence, but that reviewer-only annotation was absent from the model input. Recognizing the sequence or recalling its database record would be lookup or memorization, not reasoning from the provided context.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The matching annotation places the protein in cofactor biosynthesis, corresponding to B; the other choices describe different pathways.


### Important caveats

- The matched UniProt pathway annotation cites evidence transferred by similarity from another UniProt entry (ECO:0000250), rather than direct experimental evidence shown here.
- The exact author source snapshot is unknown, although the sequence matches the historical entry available by the stated cutoff.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence alone offers no clear general biological cue that distinguishes cofactor biosynthesis from the listed amino-acid or glycolipid pathways; identifying the relevant enzyme family requires protein-specific functional knowledge.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein's identity as phosphopantothenoylcysteine decarboxylase (PPCDC), and its role in coenzyme A biosynthesis, is not supplied in the question.",
    "reason": "The answer is supported by an annotation for this exact sequence, but that reviewer-only annotation was absent from the model input. Recognizing the sequence or recalling its database record would be lookup or memorization, not reasoning from the provided context."
  },
  "case_id": "pathway_0015",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H2"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the soybean HAL3b/PPCDC entry, whose pathway annotation places it in cofactor and coenzyme A biosynthesis. The enzyme annotation is supported by transfer from a related UniProt entry, so this supports the keyed broad pathway without establishing that it was experimentally validated for this soybean protein."
  },
  "important_caveats": [
    "The matched UniProt pathway annotation cites evidence transferred by similarity from another UniProt entry (ECO:0000250), rather than direct experimental evidence shown here.",
    "The exact author source snapshot is unknown, although the sequence matches the historical entry available by the stated cutoff."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matching annotation places the protein in cofactor biosynthesis, corresponding to B; the other choices describe different pathways."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0015",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the soybean HAL3b/PPCDC entry, whose pathway annotation places it in cofactor and coenzyme A biosynthesis. The enzyme annotation is supported by transfer from a related UniProt entry, so this supports the keyed broad pathway without establishing that it was experimentally validated for this soybean protein.",
    "evidence_ids": ["C1", "C4", "C5", "H2"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence alone offers no clear general biological cue that distinguishes cofactor biosynthesis from the listed amino-acid or glycolipid pathways; identifying the relevant enzyme family requires protein-specific functional knowledge.",
    "missing_item_specific_fact": "The protein's identity as phosphopantothenoylcysteine decarboxylase (PPCDC), and its role in coenzyme A biosynthesis, is not supplied in the question.",
    "reason": "The answer is supported by an annotation for this exact sequence, but that reviewer-only annotation was absent from the model input. Recognizing the sequence or recalling its database record would be lookup or memorization, not reasoning from the provided context."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matching annotation places the protein in cofactor biosynthesis, corresponding to B; the other choices describe different pathways."
  },
  "important_caveats": [
    "The matched UniProt pathway annotation cites evidence transferred by similarity from another UniProt entry (ECO:0000250), rather than direct experimental evidence shown here.",
    "The exact author source snapshot is unknown, although the sequence matches the historical entry available by the stated cutoff."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry C6TA59 (HAL3B_SOYBN) explicitly annotates the pathway as 'Cofactor biosynthesis; coenzyme A biosynthesis; CoA from (R)-pantothenate: step 3/5' (evidence C5, H2). The protein is Phosphopantothenoylcysteine decarboxylase (PPCDC, EC 4.1.1.36), which catalyzes a committed step in coenzyme A biosynthesis. CoA biosynthesis is classified under the top-level UniProt pathway category 'Cofactor biosynthesis,' directly matching answer B. The evidence code is ECO:0000250 (similarity to Q9SWE5), so the annotation is computationally transferred rather than experimentally verified for this specific soybean protein, but it is a valid and consistent annotation.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H1](#evidence-h1), [H2](#evidence-h2).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> One could note the conserved cysteine-rich motif 'CHCF' in the sequence, which is characteristic of the PPCDC enzyme family, and reason that PPCDC participates in CoA biosynthesis. However, reliably identifying this short motif as diagnostic of PPCDC among all small cysteine-containing proteins, and then correctly mapping PPCDC to the specific UniProt pathway category 'Cofactor biosynthesis' (rather than, say, amino acid biosynthesis or general metabolism), requires specialized knowledge of this particular enzyme family and database pathway taxonomy.


**Missing item-specific fact**

> The specific identification of this 214-aa sequence as phosphopantothenoylcysteine decarboxylase (PPCDC, EC 4.1.1.36) and the knowledge that CoA biosynthesis is categorized under 'Cofactor biosynthesis' in the UniProt pathway hierarchy. Without recognizing the PPCDC family, the sequence offers no obvious pathway-specific feature that clearly distinguishes cofactor biosynthesis from the three other unrelated pathway options.


**Reason**

> The four choices span completely unrelated pathways (amino acid biosynthesis, cofactor biosynthesis, glycolipid biosynthesis, methionine biosynthesis). Distinguishing them requires identifying the specific enzyme, which depends on recognizing PPCDC family features or recalling the protein's identity. General biological reasoning from a 214-aa sequence without a clear pathway-specific catalytic signature (e.g., no obvious glycosyltransferase, kinase, or aspartokinase motif) does not meaningfully narrow the choices without item-specific knowledge.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The UniProt annotation unambiguously places this protein in 'Cofactor biosynthesis; coenzyme A biosynthesis.' None of the other three options (threonine biosynthesis, glycolipid biosynthesis, cystathionine synthesis) bear any relation to PPCDC or CoA biosynthesis. Answer B is the sole defensible choice.


### Important caveats

- The pathway annotation carries evidence code ECO:0000250 (inferred by similarity from Q9SWE5), meaning it is computationally transferred rather than experimentally validated for this specific soybean protein.
- The protein is also named 'Halotolerance protein 3b' (GmHAL3b), which could mislead a model toward a stress-response pathway rather than cofactor biosynthesis.
- The accession C6TA59 was inferred by the reviewer from dataset metadata; the evaluated model received only the raw sequence and had no access to this identifier.
- The UniProt entry was first publicly released on 2025-04-09; the author's source snapshot date is unknown, so the annotation available at question-construction time may differ.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "One could note the conserved cysteine-rich motif 'CHCF' in the sequence, which is characteristic of the PPCDC enzyme family, and reason that PPCDC participates in CoA biosynthesis. However, reliably identifying this short motif as diagnostic of PPCDC among all small cysteine-containing proteins, and then correctly mapping PPCDC to the specific UniProt pathway category 'Cofactor biosynthesis' (rather than, say, amino acid biosynthesis or general metabolism), requires specialized knowledge of this particular enzyme family and database pathway taxonomy.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific identification of this 214-aa sequence as phosphopantothenoylcysteine decarboxylase (PPCDC, EC 4.1.1.36) and the knowledge that CoA biosynthesis is categorized under 'Cofactor biosynthesis' in the UniProt pathway hierarchy. Without recognizing the PPCDC family, the sequence offers no obvious pathway-specific feature that clearly distinguishes cofactor biosynthesis from the three other unrelated pathway options.",
    "reason": "The four choices span completely unrelated pathways (amino acid biosynthesis, cofactor biosynthesis, glycolipid biosynthesis, methionine biosynthesis). Distinguishing them requires identifying the specific enzyme, which depends on recognizing PPCDC family features or recalling the protein's identity. General biological reasoning from a 214-aa sequence without a clear pathway-specific catalytic signature (e.g., no obvious glycosyltransferase, kinase, or aspartokinase motif) does not meaningfully narrow the choices without item-specific knowledge."
  },
  "case_id": "pathway_0015",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H1",
      "H2"
    ],
    "judgment": "supported",
    "reason": "UniProt entry C6TA59 (HAL3B_SOYBN) explicitly annotates the pathway as 'Cofactor biosynthesis; coenzyme A biosynthesis; CoA from (R)-pantothenate: step 3/5' (evidence C5, H2). The protein is Phosphopantothenoylcysteine decarboxylase (PPCDC, EC 4.1.1.36), which catalyzes a committed step in coenzyme A biosynthesis. CoA biosynthesis is classified under the top-level UniProt pathway category 'Cofactor biosynthesis,' directly matching answer B. The evidence code is ECO:0000250 (similarity to Q9SWE5), so the annotation is computationally transferred rather than experimentally verified for this specific soybean protein, but it is a valid and consistent annotation."
  },
  "important_caveats": [
    "The pathway annotation carries evidence code ECO:0000250 (inferred by similarity from Q9SWE5), meaning it is computationally transferred rather than experimentally validated for this specific soybean protein.",
    "The protein is also named 'Halotolerance protein 3b' (GmHAL3b), which could mislead a model toward a stress-response pathway rather than cofactor biosynthesis.",
    "The accession C6TA59 was inferred by the reviewer from dataset metadata; the evaluated model received only the raw sequence and had no access to this identifier.",
    "The UniProt entry was first publicly released on 2025-04-09; the author's source snapshot date is unknown, so the annotation available at question-construction time may differ."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The UniProt annotation unambiguously places this protein in 'Cofactor biosynthesis; coenzyme A biosynthesis.' None of the other three options (threonine biosynthesis, glycolipid biosynthesis, cystathionine synthesis) bear any relation to PPCDC or CoA biosynthesis. Answer B is the sole defensible choice."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0015",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry C6TA59 (HAL3B_SOYBN) explicitly annotates the pathway as 'Cofactor biosynthesis; coenzyme A biosynthesis; CoA from (R)-pantothenate: step 3/5' (evidence C5, H2). The protein is Phosphopantothenoylcysteine decarboxylase (PPCDC, EC 4.1.1.36), which catalyzes a committed step in coenzyme A biosynthesis. CoA biosynthesis is classified under the top-level UniProt pathway category 'Cofactor biosynthesis,' directly matching answer B. The evidence code is ECO:0000250 (similarity to Q9SWE5), so the annotation is computationally transferred rather than experimentally verified for this specific soybean protein, but it is a valid and consistent annotation.",
    "evidence_ids": ["C4", "C5", "H1", "H2"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "One could note the conserved cysteine-rich motif 'CHCF' in the sequence, which is characteristic of the PPCDC enzyme family, and reason that PPCDC participates in CoA biosynthesis. However, reliably identifying this short motif as diagnostic of PPCDC among all small cysteine-containing proteins, and then correctly mapping PPCDC to the specific UniProt pathway category 'Cofactor biosynthesis' (rather than, say, amino acid biosynthesis or general metabolism), requires specialized knowledge of this particular enzyme family and database pathway taxonomy.",
    "missing_item_specific_fact": "The specific identification of this 214-aa sequence as phosphopantothenoylcysteine decarboxylase (PPCDC, EC 4.1.1.36) and the knowledge that CoA biosynthesis is categorized under 'Cofactor biosynthesis' in the UniProt pathway hierarchy. Without recognizing the PPCDC family, the sequence offers no obvious pathway-specific feature that clearly distinguishes cofactor biosynthesis from the three other unrelated pathway options.",
    "reason": "The four choices span completely unrelated pathways (amino acid biosynthesis, cofactor biosynthesis, glycolipid biosynthesis, methionine biosynthesis). Distinguishing them requires identifying the specific enzyme, which depends on recognizing PPCDC family features or recalling the protein's identity. General biological reasoning from a 214-aa sequence without a clear pathway-specific catalytic signature (e.g., no obvious glycosyltransferase, kinase, or aspartokinase motif) does not meaningfully narrow the choices without item-specific knowledge."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The UniProt annotation unambiguously places this protein in 'Cofactor biosynthesis; coenzyme A biosynthesis.' None of the other three options (threonine biosynthesis, glycolipid biosynthesis, cystathionine synthesis) bear any relation to PPCDC or CoA biosynthesis. Answer B is the sole defensible choice."
  },
  "important_caveats": [
    "The pathway annotation carries evidence code ECO:0000250 (inferred by similarity from Q9SWE5), meaning it is computationally transferred rather than experimentally validated for this specific soybean protein.",
    "The protein is also named 'Halotolerance protein 3b' (GmHAL3b), which could mislead a model toward a stress-response pathway rather than cofactor biosynthesis.",
    "The accession C6TA59 was inferred by the reviewer from dataset metadata; the evaluated model received only the raw sequence and had no access to this identifier.",
    "The UniProt entry was first publicly released on 2025-04-09; the author's source snapshot date is unknown, so the annotation available at question-construction time may differ."
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

**Accession:** `C6TA59` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 84. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C6TA59.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:35.244012+00:00.  

```json
"C6TA59"
```

Source SHA-256: `4f24a50395840d689b2bca6503bac71363002becd9e9b0e170ac85361993f2a0`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C6TA59.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:35.244012+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"Ref.3","source":"Reference"},{"evidenceCode":"ECO:0000303","id":"Ref.4","source":"Reference"}],"value":"Halotolerance protein 3b"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"Ref.3","source":"Reference"},{"evidenceCode":"ECO:0000303","id":"Ref.4","source":"Reference"}],"value":"GmHAL3b"}]}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q9SWE5","source":"UniProtKB"}],"value":"4.1.1.36"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Phosphopantothenoylcysteine decarboxylase HAL3b"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"PPCDC"}]}}
```

Source SHA-256: `4f24a50395840d689b2bca6503bac71363002becd9e9b0e170ac85361993f2a0`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C6TA59.json)  
**Locator:** `/comments/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:35.244012+00:00.  

```json
{"commentType":"PATHWAY","texts":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q9SWE5","source":"UniProtKB"}],"value":"Cofactor biosynthesis; coenzyme A biosynthesis; CoA from (R)-pantothenate: step 3/5"}]}
```

Source SHA-256: `4f24a50395840d689b2bca6503bac71363002becd9e9b0e170ac85361993f2a0`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/C6TA59?format=txt&versions=84)  
**Locator:** `lines 1-19`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 84 / 1.  
**Retrieved:** 2026-11-02T04:27:37.263279+00:00.  

```text
ID   HAL3B_SOYBN             Reviewed;         214 AA.
AC   C6TA59;
DT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.
DT   22-SEP-2009, sequence version 1.
DT   28-JAN-2026, entry version 84.
DE   RecName: Full=Phosphopantothenoylcysteine decarboxylase HAL3b {ECO:0000305};
DE            Short=PPCDC {ECO:0000305};
DE            EC=4.1.1.36 {ECO:0000250|UniProtKB:Q9SWE5};
DE   AltName: Full=Halotolerance protein 3b {ECO:0000303|Ref.3, ECO:0000303|Ref.4};
DE            Short=GmHAL3b {ECO:0000303|Ref.3, ECO:0000303|Ref.4};
GN   Name=HAL3B {ECO:0000303|Ref.3, ECO:0000303|Ref.4};
GN   OrderedLocusNames=Glyma07g082800 {ECO:0000312|EMBL:KRH48322.1};
OS   Glycine max (Soybean) (Glycine hispida).
OC   Eukaryota; Viridiplantae; Streptophyta; Embryophyta; Tracheophyta;
OC   Spermatophyta; Magnoliopsida; eudicotyledons; Gunneridae; Pentapetalae;
OC   rosids; fabids; Fabales; Fabaceae; Papilionoideae; 50 kb inversion clade;
OC   NPAAA clade; indigoferoid/millettioid clade; Phaseoleae; Glycine;
OC   Glycine subgen. Soja.
OX   NCBI_TaxID=3847;
```

Source SHA-256: `9ba69ef0f337ff2a30393964c793af5f757c0c52e62614aa37894bfe6ab8f68d`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/C6TA59?format=txt&versions=84)  
**Locator:** `lines 73-74`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 84 / 1.  
**Retrieved:** 2026-11-02T04:27:37.263279+00:00.  

```text
CC   -!- PATHWAY: Cofactor biosynthesis; coenzyme A biosynthesis; CoA from (R)-
CC       pantothenate: step 3/5. {ECO:0000250|UniProtKB:Q9SWE5}.
```

Source SHA-256: `9ba69ef0f337ff2a30393964c793af5f757c0c52e62614aa37894bfe6ab8f68d`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 15. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
