# pathway_0030

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `pathway`  
**Author expected answer:** **C** — Cofactor biosynthesis

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MAGSEPVRAEGETMAVDAAPRKPRILLAASGSVAAVKFANLCHCFSEWADVRAVSTSASLHFIDRAAMPKDVILYTDDNEWSSWKKLGDSVLHIELRKWADIMVIAPLSANTLGKIAGGLCDNLLTCIVRAWDYSKPFFVAPAMNTFMWNNPFTERHLISIDELGISLIPPVTKRLACGDYGNGAMAEPSTIYSTVRLFYESKAQQGNGDI

[Multiple Choices]
A. L-threonine from L-aspartate: step 5/5. .
B. fatty acid beta-oxidation. .
C. Cofactor biosynthesis
D. N(1)-(5-phospho-D-ribosyl)glycinamide from 5-phospho-alpha-D-ribose 1-diphosphate: step 1/2. .
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

> The exact sequence matches a UniProt entry annotated as phosphopantothenoylcysteine decarboxylase (PPCDC), with a pathway annotation placing it in cofactor and coenzyme A biosynthesis. The annotation is transferred by similarity, so it supports the key as a database annotation but is not direct experimental confirmation for this protein.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence is a protein sequence, but the supplied input gives no organism, protein name, functional context, or pathway reaction that distinguishes cofactor biosynthesis from the other listed pathways.


**Missing item-specific fact**

> Identifying this sequence as PPCDC, and knowing that PPCDC participates in coenzyme A biosynthesis, is needed to select C.


**Reason**

> The pathway assignment depends on a protein-specific functional annotation absent from the question. Recognizing the sequence or retrieving its annotation would be lookup, not reasoning from supplied biological context.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The annotation maps the protein to cofactor biosynthesis, specifically coenzyme A biosynthesis; none of the other choices describes that pathway.


### Important caveats

- The pathway annotation is supported by similarity to another UniProt entry (ECO:0000250), rather than evidence of direct experimental characterization of this soybean protein in the supplied excerpts.
- Reviewer-only accession and database information establishes support for the key but was not available to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is a protein sequence, but the supplied input gives no organism, protein name, functional context, or pathway reaction that distinguishes cofactor biosynthesis from the other listed pathways.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "Identifying this sequence as PPCDC, and knowing that PPCDC participates in coenzyme A biosynthesis, is needed to select C.",
    "reason": "The pathway assignment depends on a protein-specific functional annotation absent from the question. Recognizing the sequence or retrieving its annotation would be lookup, not reasoning from supplied biological context."
  },
  "case_id": "pathway_0030",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H2"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry annotated as phosphopantothenoylcysteine decarboxylase (PPCDC), with a pathway annotation placing it in cofactor and coenzyme A biosynthesis. The annotation is transferred by similarity, so it supports the key as a database annotation but is not direct experimental confirmation for this protein."
  },
  "important_caveats": [
    "The pathway annotation is supported by similarity to another UniProt entry (ECO:0000250), rather than evidence of direct experimental characterization of this soybean protein in the supplied excerpts.",
    "Reviewer-only accession and database information establishes support for the key but was not available to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The annotation maps the protein to cofactor biosynthesis, specifically coenzyme A biosynthesis; none of the other choices describes that pathway."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0030",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry annotated as phosphopantothenoylcysteine decarboxylase (PPCDC), with a pathway annotation placing it in cofactor and coenzyme A biosynthesis. The annotation is transferred by similarity, so it supports the key as a database annotation but is not direct experimental confirmation for this protein.",
    "evidence_ids": ["C1", "C4", "C5", "H2"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence is a protein sequence, but the supplied input gives no organism, protein name, functional context, or pathway reaction that distinguishes cofactor biosynthesis from the other listed pathways.",
    "missing_item_specific_fact": "Identifying this sequence as PPCDC, and knowing that PPCDC participates in coenzyme A biosynthesis, is needed to select C.",
    "reason": "The pathway assignment depends on a protein-specific functional annotation absent from the question. Recognizing the sequence or retrieving its annotation would be lookup, not reasoning from supplied biological context."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The annotation maps the protein to cofactor biosynthesis, specifically coenzyme A biosynthesis; none of the other choices describes that pathway."
  },
  "important_caveats": [
    "The pathway annotation is supported by similarity to another UniProt entry (ECO:0000250), rather than evidence of direct experimental characterization of this soybean protein in the supplied excerpts.",
    "Reviewer-only accession and database information establishes support for the key but was not available to the evaluated model."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry C6SZ50 (HAL3A_SOYBN, Phosphopantothenoylcysteine decarboxylase, EC 4.1.1.36) annotates the pathway as 'Cofactor biosynthesis; coenzyme A biosynthesis; CoA from (R)-pantothenate: step 3/5' (evidence_id C5, H2). The expected answer 'Cofactor biosynthesis' is the correct top-level pathway category. The evidence code is ECO:0000250 (inferred by similarity to Arabidopsis Q9SWE5), so the assignment is computational/transferred rather than directly experimental for this soybean protein, but PPCDC is a highly conserved enzyme family and the CoA-biosynthesis role is well established across species.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H1](#evidence-h1), [H2](#evidence-h2).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> Weak structural inferences are possible: the protein is only 211 aa (small for beta-oxidation enzymes), lacks obvious PLP-binding motifs (arguing against threonine synthase, option A), and lacks a glutamine amidotransferase domain (arguing against GAR synthase, option D). The CHCF motif and conserved Cys/His residues suggest a small metalloenzyme, consistent with PPCDC. However, these observations do not uniquely or reliably point to 'Cofactor biosynthesis' rather than other small-enzyme pathways. The decisive step requires recognizing the vanillin-halogenase/HAL3/PPCDC protein family and knowing that PPCDC catalyzes a step in CoA (a cofactor) biosynthesis.


**Missing item-specific fact**

> The identification of this 211-aa sequence as phosphopantothenoylcysteine decarboxylase (PPCDC/HAL3a, EC 4.1.1.36) and its membership in the vanillin-halogenase superfamily, which is not derivable from generic sequence heuristics alone. The specific pathway assignment (CoA biosynthesis → Cofactor biosynthesis) depends on knowing the function of this particular enzyme family.


**Reason**

> While the small size and absence of PLP or glutamine-amidotransferase motifs can weakly disfavour options A, B, and D, positively identifying 'Cofactor biosynthesis' requires recognizing the PPCDC/HAL3 protein family from its sequence, which is essentially a database-lookup or memorization task rather than a chain of general biological reasoning.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options belong to entirely distinct metabolic pathways (threonine biosynthesis, fatty acid beta-oxidation, CoA/cofactor biosynthesis, purine biosynthesis). Once the protein is identified as PPCDC, only option C is correct. The wording of option C ('Cofactor biosynthesis') is the valid top-level UniProt pathway heading. No other option is defensible for this enzyme.


### Important caveats

- The pathway annotation carries evidence code ECO:0000250 (similarity to Q9SWE5, Arabidopsis PPCDC), meaning it is a computational transfer, not direct experimental validation on the soybean protein.
- The UniProt entry was first publicly released 2025-04-09; the author's source snapshot is unknown, but the historical version (entry 84, released 2026-01-28) already contained the same pathway annotation.
- The reviewer-only evidence confirms exact sequence match (SHA-256 identical) between the benchmark input and the UniProt entry, so the annotation applies to the supplied sequence.
- The alternative name 'Halotolerance protein 3a' (GmHAL3a) reflects the protein's discovery context (halotolerance) but does not alter its enzymatic pathway assignment.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Weak structural inferences are possible: the protein is only 211 aa (small for beta-oxidation enzymes), lacks obvious PLP-binding motifs (arguing against threonine synthase, option A), and lacks a glutamine amidotransferase domain (arguing against GAR synthase, option D). The CHCF motif and conserved Cys/His residues suggest a small metalloenzyme, consistent with PPCDC. However, these observations do not uniquely or reliably point to 'Cofactor biosynthesis' rather than other small-enzyme pathways. The decisive step requires recognizing the vanillin-halogenase/HAL3/PPCDC protein family and knowing that PPCDC catalyzes a step in CoA (a cofactor) biosynthesis.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The identification of this 211-aa sequence as phosphopantothenoylcysteine decarboxylase (PPCDC/HAL3a, EC 4.1.1.36) and its membership in the vanillin-halogenase superfamily, which is not derivable from generic sequence heuristics alone. The specific pathway assignment (CoA biosynthesis → Cofactor biosynthesis) depends on knowing the function of this particular enzyme family.",
    "reason": "While the small size and absence of PLP or glutamine-amidotransferase motifs can weakly disfavour options A, B, and D, positively identifying 'Cofactor biosynthesis' requires recognizing the PPCDC/HAL3 protein family from its sequence, which is essentially a database-lookup or memorization task rather than a chain of general biological reasoning."
  },
  "case_id": "pathway_0030",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H1",
      "H2"
    ],
    "judgment": "supported",
    "reason": "UniProt entry C6SZ50 (HAL3A_SOYBN, Phosphopantothenoylcysteine decarboxylase, EC 4.1.1.36) annotates the pathway as 'Cofactor biosynthesis; coenzyme A biosynthesis; CoA from (R)-pantothenate: step 3/5' (evidence_id C5, H2). The expected answer 'Cofactor biosynthesis' is the correct top-level pathway category. The evidence code is ECO:0000250 (inferred by similarity to Arabidopsis Q9SWE5), so the assignment is computational/transferred rather than directly experimental for this soybean protein, but PPCDC is a highly conserved enzyme family and the CoA-biosynthesis role is well established across species."
  },
  "important_caveats": [
    "The pathway annotation carries evidence code ECO:0000250 (similarity to Q9SWE5, Arabidopsis PPCDC), meaning it is a computational transfer, not direct experimental validation on the soybean protein.",
    "The UniProt entry was first publicly released 2025-04-09; the author's source snapshot is unknown, but the historical version (entry 84, released 2026-01-28) already contained the same pathway annotation.",
    "The reviewer-only evidence confirms exact sequence match (SHA-256 identical) between the benchmark input and the UniProt entry, so the annotation applies to the supplied sequence.",
    "The alternative name 'Halotolerance protein 3a' (GmHAL3a) reflects the protein's discovery context (halotolerance) but does not alter its enzymatic pathway assignment."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options belong to entirely distinct metabolic pathways (threonine biosynthesis, fatty acid beta-oxidation, CoA/cofactor biosynthesis, purine biosynthesis). Once the protein is identified as PPCDC, only option C is correct. The wording of option C ('Cofactor biosynthesis') is the valid top-level UniProt pathway heading. No other option is defensible for this enzyme."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0030",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry C6SZ50 (HAL3A_SOYBN, Phosphopantothenoylcysteine decarboxylase, EC 4.1.1.36) annotates the pathway as 'Cofactor biosynthesis; coenzyme A biosynthesis; CoA from (R)-pantothenate: step 3/5' (evidence_id C5, H2). The expected answer 'Cofactor biosynthesis' is the correct top-level pathway category. The evidence code is ECO:0000250 (inferred by similarity to Arabidopsis Q9SWE5), so the assignment is computational/transferred rather than directly experimental for this soybean protein, but PPCDC is a highly conserved enzyme family and the CoA-biosynthesis role is well established across species.",
    "evidence_ids": ["C4", "C5", "H1", "H2"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "Weak structural inferences are possible: the protein is only 211 aa (small for beta-oxidation enzymes), lacks obvious PLP-binding motifs (arguing against threonine synthase, option A), and lacks a glutamine amidotransferase domain (arguing against GAR synthase, option D). The CHCF motif and conserved Cys/His residues suggest a small metalloenzyme, consistent with PPCDC. However, these observations do not uniquely or reliably point to 'Cofactor biosynthesis' rather than other small-enzyme pathways. The decisive step requires recognizing the vanillin-halogenase/HAL3/PPCDC protein family and knowing that PPCDC catalyzes a step in CoA (a cofactor) biosynthesis.",
    "missing_item_specific_fact": "The identification of this 211-aa sequence as phosphopantothenoylcysteine decarboxylase (PPCDC/HAL3a, EC 4.1.1.36) and its membership in the vanillin-halogenase superfamily, which is not derivable from generic sequence heuristics alone. The specific pathway assignment (CoA biosynthesis → Cofactor biosynthesis) depends on knowing the function of this particular enzyme family.",
    "reason": "While the small size and absence of PLP or glutamine-amidotransferase motifs can weakly disfavour options A, B, and D, positively identifying 'Cofactor biosynthesis' requires recognizing the PPCDC/HAL3 protein family from its sequence, which is essentially a database-lookup or memorization task rather than a chain of general biological reasoning."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options belong to entirely distinct metabolic pathways (threonine biosynthesis, fatty acid beta-oxidation, CoA/cofactor biosynthesis, purine biosynthesis). Once the protein is identified as PPCDC, only option C is correct. The wording of option C ('Cofactor biosynthesis') is the valid top-level UniProt pathway heading. No other option is defensible for this enzyme."
  },
  "important_caveats": [
    "The pathway annotation carries evidence code ECO:0000250 (similarity to Q9SWE5, Arabidopsis PPCDC), meaning it is a computational transfer, not direct experimental validation on the soybean protein.",
    "The UniProt entry was first publicly released 2025-04-09; the author's source snapshot is unknown, but the historical version (entry 84, released 2026-01-28) already contained the same pathway annotation.",
    "The reviewer-only evidence confirms exact sequence match (SHA-256 identical) between the benchmark input and the UniProt entry, so the annotation applies to the supplied sequence.",
    "The alternative name 'Halotolerance protein 3a' (GmHAL3a) reflects the protein's discovery context (halotolerance) but does not alter its enzymatic pathway assignment."
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

**Accession:** `C6SZ50` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 84. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C6SZ50.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:34.573952+00:00.  

```json
"C6SZ50"
```

Source SHA-256: `d2226dda9179b81f36d4679262e16bb210a289390044f58410d1a107b4408396`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C6SZ50.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:34.573952+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"Ref.3","source":"Reference"},{"evidenceCode":"ECO:0000303","id":"Ref.4","source":"Reference"}],"value":"Halotolerance protein 3a"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"Ref.3","source":"Reference"},{"evidenceCode":"ECO:0000303","id":"Ref.4","source":"Reference"}],"value":"GmHAL3a"}]}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q9SWE5","source":"UniProtKB"}],"value":"4.1.1.36"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Phosphopantothenoylcysteine decarboxylase HAL3a"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"PPCDC"}]}}
```

Source SHA-256: `d2226dda9179b81f36d4679262e16bb210a289390044f58410d1a107b4408396`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C6SZ50.json)  
**Locator:** `/comments/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:34.573952+00:00.  

```json
{"commentType":"PATHWAY","texts":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q9SWE5","source":"UniProtKB"}],"value":"Cofactor biosynthesis; coenzyme A biosynthesis; CoA from (R)-pantothenate: step 3/5"}]}
```

Source SHA-256: `d2226dda9179b81f36d4679262e16bb210a289390044f58410d1a107b4408396`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/C6SZ50?format=txt&versions=84)  
**Locator:** `lines 1-19`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 84 / 1.  
**Retrieved:** 2026-11-02T04:27:36.741333+00:00.  

```text
ID   HAL3A_SOYBN             Reviewed;         211 AA.
AC   C6SZ50;
DT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.
DT   22-SEP-2009, sequence version 1.
DT   28-JAN-2026, entry version 84.
DE   RecName: Full=Phosphopantothenoylcysteine decarboxylase HAL3a {ECO:0000305};
DE            Short=PPCDC {ECO:0000305};
DE            EC=4.1.1.36 {ECO:0000250|UniProtKB:Q9SWE5};
DE   AltName: Full=Halotolerance protein 3a {ECO:0000303|Ref.3, ECO:0000303|Ref.4};
DE            Short=GmHAL3a {ECO:0000303|Ref.3, ECO:0000303|Ref.4};
GN   Name=HAL3A {ECO:0000303|Ref.3, ECO:0000303|Ref.4};
GN   OrderedLocusNames=Glyma03g020900 {ECO:0000312|EMBL:KRH65212.1};
OS   Glycine max (Soybean) (Glycine hispida).
OC   Eukaryota; Viridiplantae; Streptophyta; Embryophyta; Tracheophyta;
OC   Spermatophyta; Magnoliopsida; eudicotyledons; Gunneridae; Pentapetalae;
OC   rosids; fabids; Fabales; Fabaceae; Papilionoideae; 50 kb inversion clade;
OC   NPAAA clade; indigoferoid/millettioid clade; Phaseoleae; Glycine;
OC   Glycine subgen. Soja.
OX   NCBI_TaxID=3847;
```

Source SHA-256: `1ce346fa691149ee6e809ca984b0d5dbda18272b4eb904ae9e28b38ca8688212`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/C6SZ50?format=txt&versions=84)  
**Locator:** `lines 73-74`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 84 / 1.  
**Retrieved:** 2026-11-02T04:27:36.741333+00:00.  

```text
CC   -!- PATHWAY: Cofactor biosynthesis; coenzyme A biosynthesis; CoA from (R)-
CC       pantothenate: step 3/5. {ECO:0000250|UniProtKB:Q9SWE5}.
```

Source SHA-256: `1ce346fa691149ee6e809ca984b0d5dbda18272b4eb904ae9e28b38ca8688212`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 30. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
