# EC_number_0197

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `EC_number`  
**Author expected answer:** **A** — 3.2.1.18

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MEPSKLFTISDNATFAPGPVINVADKKTFRTCFRILVLSVQAVTLILVIVNLGELVRMINDQGLSNQLSSITDKIRESANMIASAVGVMNQVIHGVTVSLPLQIEGNQNQLLSTLATICTSKKQVSNCSTNIPLVNDLRFINGINKFIIEDYATHDFSIGHPLNMPSFIPTATSPNGCTRIPSFSLGKTHWCYTHNVINANCKDHTSSNQYVSMGILVQTASGYPMFKTLKIQYLSDGLNRKSCSIATVPDGCAMYCYISTQLETDDYAGSSPPTQKLTLLFYNDTVTERTISPSGLEGNWATLVPGVGSGIYFENKLIFPAYGGVLPNSTLGVKSAREFFRPVNPYNPCSGPQQDLDQRALRSYFPSYFSNRRVQSAFLVCAWNQILVTNCELVVPSNNQTLMGAEGRVLLINNRLLYYQRSTSWWPYELLYEISFTFTNSGQSSVNMSWIPIYSFTRPGSGNCSGENVCPTACVSGVYLDPWPLTPYSHQSGINRNFYFTGALLNSSTTRVNPTLYVSALNNLKVLAPYGTQGLFASYTTTTCFQDTGDASVYCVYIMELASNIVGEFQILPVLTRLTIT

[Multiple Choices]
A. 3.2.1.18
B. 3.2.1.20
C. 1.8.1.9
D. 2.3.1.312
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

> The exact sequence matches the UniProt entry for mumps virus hemagglutinin-neuraminidase, annotated with EC 3.2.1.18 and sialic-acid hydrolysis activity. The annotation is transferred by similarity from Q9WAF5 (ECO:0000250), so it supports the key but is not direct experimental evidence for this exact protein.

Citations as saved: [C1](#evidence-c1), [C3](#evidence-c3), [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The N-terminal hydrophobic segment is consistent with a membrane-associated viral glycoprotein, but that feature does not establish its catalytic activity or the specific EC number.


**Missing item-specific fact**

> The protein's identity as hemagglutinin-neuraminidase and its sialidase activity are not supplied; distinguishing EC 3.2.1.18 requires that protein-specific annotation or equivalent functional evidence.


**Reason**

> The sequence may support computational recognition, but the input gives no clear general biological argument that establishes this exact enzymatic function rather than the alternatives.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The supplied reviewer evidence supports A; it does not support the alternative EC numbers.


### Important caveats

- The UniProt functional assignment is similarity-transferred, not direct experimental evidence for this exact strain's protein.
- Reviewer-only identity and annotation evidence establish support for the key but were not available in the original question.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal hydrophobic segment is consistent with a membrane-associated viral glycoprotein, but that feature does not establish its catalytic activity or the specific EC number.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein's identity as hemagglutinin-neuraminidase and its sialidase activity are not supplied; distinguishing EC 3.2.1.18 requires that protein-specific annotation or equivalent functional evidence.",
    "reason": "The sequence may support computational recognition, but the input gives no clear general biological argument that establishes this exact enzymatic function rather than the alternatives."
  },
  "case_id": "EC_number_0197",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C3",
      "C4",
      "C5",
      "H2",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry for mumps virus hemagglutinin-neuraminidase, annotated with EC 3.2.1.18 and sialic-acid hydrolysis activity. The annotation is transferred by similarity from Q9WAF5 (ECO:0000250), so it supports the key but is not direct experimental evidence for this exact protein."
  },
  "important_caveats": [
    "The UniProt functional assignment is similarity-transferred, not direct experimental evidence for this exact strain's protein.",
    "Reviewer-only identity and annotation evidence establish support for the key but were not available in the original question."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied reviewer evidence supports A; it does not support the alternative EC numbers."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0197",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry for mumps virus hemagglutinin-neuraminidase, annotated with EC 3.2.1.18 and sialic-acid hydrolysis activity. The annotation is transferred by similarity from Q9WAF5 (ECO:0000250), so it supports the key but is not direct experimental evidence for this exact protein.",
    "evidence_ids": ["C1", "C3", "C4", "C5", "H2", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The N-terminal hydrophobic segment is consistent with a membrane-associated viral glycoprotein, but that feature does not establish its catalytic activity or the specific EC number.",
    "missing_item_specific_fact": "The protein's identity as hemagglutinin-neuraminidase and its sialidase activity are not supplied; distinguishing EC 3.2.1.18 requires that protein-specific annotation or equivalent functional evidence.",
    "reason": "The sequence may support computational recognition, but the input gives no clear general biological argument that establishes this exact enzymatic function rather than the alternatives."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied reviewer evidence supports A; it does not support the alternative EC numbers."
  },
  "important_caveats": [
    "The UniProt functional assignment is similarity-transferred, not direct experimental evidence for this exact strain's protein.",
    "Reviewer-only identity and annotation evidence establish support for the key but were not available in the original question."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The protein sequence exactly matches UniProt Q5SC51 (Mumps virus HN_MUMPZ, 582 AA, sequence SHA256 matched in both current and historical entries). The UniProt annotation assigns EC 3.2.1.18 (Hemagglutinin-neuraminidase) with catalytic activity: hydrolysis of alpha-(2->3)-, alpha-(2->6)-, alpha-(2->8)- glycosidic linkages of terminal sialic acid residues. The evidence code is ECO:0000250 (inferred by similarity from Q9WAF5), but mumps HN neuraminidase activity is well-established in virology literature. The annotation is consistent with the protein's identity as a paramyxovirus surface glycoprotein.

Citations as saved: [C1](#evidence-c1), [C3](#evidence-c3), [C4](#evidence-c4), [C5](#evidence-c5), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains sialidase-family motifs including variants of the R-Y-S-S-Y signature (e.g., 'RNFYFT' and 'IYSFTRPGSGNCS' regions) and arginine-rich sialic-acid-binding residues characteristic of neuraminidases (EC 3.2.1.18). These motifs are absent from alpha-galactosidases (EC 3.2.1.20), which use a different catalytic framework. Options C (1.8.1.9, thioredoxin reductase) and D (2.3.1.312, acyltransferase) are readily eliminated by the absence of FAD/NADPH-binding Rossmann motifs or acyl-CoA-binding domains. The presence of a signal peptide and type-II membrane topology further supports a viral surface glycoprotein with receptor-binding/enzymatic activity rather than a soluble oxidoreductase or transferase.


**Missing item-specific fact**

> None strictly required; however, precise motif identification in paramyxovirus HN (where canonical motifs are somewhat degenerate compared to bacterial sialidases) benefits from familiarity with the specific sequence context of Rubulavirinae HN proteins.


**Reason**

> A knowledgeable student can identify sialidase-specific sequence motifs (R-Y-S-S-Y variants, conserved Arg residues) that distinguish EC 3.2.1.18 from EC 3.2.1.20, and eliminate EC 1.8.1.9 and EC 2.3.1.312 based on absent cofactor/substrate-binding motifs. This constitutes a concrete biological argument from the supplied sequence. The path is somewhat aided by recognizing the protein family, but the motif-level reasoning is independently valid.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options C and D are clearly eliminated by sequence architecture. The A vs B distinction is resolvable via sialidase-specific motifs. No other option is defensible.


### Important caveats

- The UniProt EC annotation uses evidence code ECO:0000250 (similarity-based, transferred from Q9WAF5), not direct experimental measurement on this specific strain. However, mumps HN neuraminidase activity is extensively documented in virology literature.
- The paramyxovirus HN R-Y-S-S-Y motif is somewhat degenerate compared to bacterial sialidases, making motif-based reasoning slightly less straightforward than for canonical sialidases.
- The sequence match to Q5SC51 is exact (SHA256 verified), confirming the protein identity underlying the annotation.
- The historical entry (version 105) and current entry (version 107) both carry the same EC annotation, indicating stability of the assignment.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains sialidase-family motifs including variants of the R-Y-S-S-Y signature (e.g., 'RNFYFT' and 'IYSFTRPGSGNCS' regions) and arginine-rich sialic-acid-binding residues characteristic of neuraminidases (EC 3.2.1.18). These motifs are absent from alpha-galactosidases (EC 3.2.1.20), which use a different catalytic framework. Options C (1.8.1.9, thioredoxin reductase) and D (2.3.1.312, acyltransferase) are readily eliminated by the absence of FAD/NADPH-binding Rossmann motifs or acyl-CoA-binding domains. The presence of a signal peptide and type-II membrane topology further supports a viral surface glycoprotein with receptor-binding/enzymatic activity rather than a soluble oxidoreductase or transferase.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None strictly required; however, precise motif identification in paramyxovirus HN (where canonical motifs are somewhat degenerate compared to bacterial sialidases) benefits from familiarity with the specific sequence context of Rubulavirinae HN proteins.",
    "reason": "A knowledgeable student can identify sialidase-specific sequence motifs (R-Y-S-S-Y variants, conserved Arg residues) that distinguish EC 3.2.1.18 from EC 3.2.1.20, and eliminate EC 1.8.1.9 and EC 2.3.1.312 based on absent cofactor/substrate-binding motifs. This constitutes a concrete biological argument from the supplied sequence. The path is somewhat aided by recognizing the protein family, but the motif-level reasoning is independently valid."
  },
  "case_id": "EC_number_0197",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C3",
      "C4",
      "C5",
      "H1",
      "H2",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The protein sequence exactly matches UniProt Q5SC51 (Mumps virus HN_MUMPZ, 582 AA, sequence SHA256 matched in both current and historical entries). The UniProt annotation assigns EC 3.2.1.18 (Hemagglutinin-neuraminidase) with catalytic activity: hydrolysis of alpha-(2->3)-, alpha-(2->6)-, alpha-(2->8)- glycosidic linkages of terminal sialic acid residues. The evidence code is ECO:0000250 (inferred by similarity from Q9WAF5), but mumps HN neuraminidase activity is well-established in virology literature. The annotation is consistent with the protein's identity as a paramyxovirus surface glycoprotein."
  },
  "important_caveats": [
    "The UniProt EC annotation uses evidence code ECO:0000250 (similarity-based, transferred from Q9WAF5), not direct experimental measurement on this specific strain. However, mumps HN neuraminidase activity is extensively documented in virology literature.",
    "The paramyxovirus HN R-Y-S-S-Y motif is somewhat degenerate compared to bacterial sialidases, making motif-based reasoning slightly less straightforward than for canonical sialidases.",
    "The sequence match to Q5SC51 is exact (SHA256 verified), confirming the protein identity underlying the annotation.",
    "The historical entry (version 105) and current entry (version 107) both carry the same EC annotation, indicating stability of the assignment."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options C and D are clearly eliminated by sequence architecture. The A vs B distinction is resolvable via sialidase-specific motifs. No other option is defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0197",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The protein sequence exactly matches UniProt Q5SC51 (Mumps virus HN_MUMPZ, 582 AA, sequence SHA256 matched in both current and historical entries). The UniProt annotation assigns EC 3.2.1.18 (Hemagglutinin-neuraminidase) with catalytic activity: hydrolysis of alpha-(2->3)-, alpha-(2->6)-, alpha-(2->8)- glycosidic linkages of terminal sialic acid residues. The evidence code is ECO:0000250 (inferred by similarity from Q9WAF5), but mumps HN neuraminidase activity is well-established in virology literature. The annotation is consistent with the protein's identity as a paramyxovirus surface glycoprotein.",
    "evidence_ids": ["C1", "C3", "C4", "C5", "H1", "H2", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains sialidase-family motifs including variants of the R-Y-S-S-Y signature (e.g., 'RNFYFT' and 'IYSFTRPGSGNCS' regions) and arginine-rich sialic-acid-binding residues characteristic of neuraminidases (EC 3.2.1.18). These motifs are absent from alpha-galactosidases (EC 3.2.1.20), which use a different catalytic framework. Options C (1.8.1.9, thioredoxin reductase) and D (2.3.1.312, acyltransferase) are readily eliminated by the absence of FAD/NADPH-binding Rossmann motifs or acyl-CoA-binding domains. The presence of a signal peptide and type-II membrane topology further supports a viral surface glycoprotein with receptor-binding/enzymatic activity rather than a soluble oxidoreductase or transferase.",
    "missing_item_specific_fact": "None strictly required; however, precise motif identification in paramyxovirus HN (where canonical motifs are somewhat degenerate compared to bacterial sialidases) benefits from familiarity with the specific sequence context of Rubulavirinae HN proteins.",
    "reason": "A knowledgeable student can identify sialidase-specific sequence motifs (R-Y-S-S-Y variants, conserved Arg residues) that distinguish EC 3.2.1.18 from EC 3.2.1.20, and eliminate EC 1.8.1.9 and EC 2.3.1.312 based on absent cofactor/substrate-binding motifs. This constitutes a concrete biological argument from the supplied sequence. The path is somewhat aided by recognizing the protein family, but the motif-level reasoning is independently valid."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options C and D are clearly eliminated by sequence architecture. The A vs B distinction is resolvable via sialidase-specific motifs. No other option is defensible."
  },
  "important_caveats": [
    "The UniProt EC annotation uses evidence code ECO:0000250 (similarity-based, transferred from Q9WAF5), not direct experimental measurement on this specific strain. However, mumps HN neuraminidase activity is extensively documented in virology literature.",
    "The paramyxovirus HN R-Y-S-S-Y motif is somewhat degenerate compared to bacterial sialidases, making motif-based reasoning slightly less straightforward than for canonical sialidases.",
    "The sequence match to Q5SC51 is exact (SHA256 verified), confirming the protein identity underlying the annotation.",
    "The historical entry (version 105) and current entry (version 107) both carry the same EC annotation, indicating stability of the assignment."
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

**Accession:** `Q5SC51` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 105. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5SC51.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:29.846842+00:00.  

```json
"Q5SC51"
```

Source SHA-256: `84cb4071f2488c26b98cb3a00a95cf7fafbb3f15b4205e39b2029f487b04b1c3`.

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5SC51.json)  
**Locator:** `/organism`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:29.846842+00:00.  

```json
{"commonName":"MuV","lineage":["Viruses","Riboviria","Orthornavirae","Negarnaviricota","Haploviricotina","Monjiviricetes","Mononegavirales","Paramyxoviridae","Rubulavirinae","Orthorubulavirus","Orthorubulavirus parotitidis","Mumps orthorubulavirus"],"scientificName":"Mumps virus genotype N (strain L-Zagreb vaccine)","taxonId":301186}
```

Source SHA-256: `84cb4071f2488c26b98cb3a00a95cf7fafbb3f15b4205e39b2029f487b04b1c3`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5SC51.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:29.846842+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q9WAF5","source":"UniProtKB"}],"value":"3.2.1.18"}],"fullName":{"value":"Hemagglutinin-neuraminidase"}}}
```

Source SHA-256: `84cb4071f2488c26b98cb3a00a95cf7fafbb3f15b4205e39b2029f487b04b1c3`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5SC51.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:29.846842+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"3.2.1.18","evidences":[{"evidenceCode":"ECO:0000250","id":"Q9WAF5","source":"UniProtKB"}],"name":"Hydrolysis of alpha-(2->3)-, alpha-(2->6)-, alpha-(2->8)- glycosidic linkages of terminal sialic acid residues in oligosaccharides, glycoproteins, glycolipids, colominic acid and synthetic substrates."}}
```

Source SHA-256: `84cb4071f2488c26b98cb3a00a95cf7fafbb3f15b4205e39b2029f487b04b1c3`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5SC51?format=txt&versions=105)  
**Locator:** `lines 1-14`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 105 / 1.  
**Retrieved:** 2026-11-02T04:31:32.054381+00:00.  

```text
ID   HN_MUMPZ                Reviewed;         582 AA.
AC   Q5SC51;
DT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.
DT   21-DEC-2004, sequence version 1.
DT   28-JAN-2026, entry version 105.
DE   RecName: Full=Hemagglutinin-neuraminidase;
DE            EC=3.2.1.18 {ECO:0000250|UniProtKB:Q9WAF5};
GN   Name=HN;
OS   Mumps virus genotype N (strain L-Zagreb vaccine) (MuV).
OC   Viruses; Riboviria; Orthornavirae; Negarnaviricota; Haploviricotina;
OC   Monjiviricetes; Mononegavirales; Paramyxoviridae; Rubulavirinae;
OC   Orthorubulavirus; Orthorubulavirus parotitidis; Mumps orthorubulavirus.
OX   NCBI_TaxID=301186;
OH   NCBI_TaxID=9606; Homo sapiens (Human).
```

Source SHA-256: `8bf1ba1afc5634387cc3311f78ac6fc61cefd51f3d1e338d340ea041cd46beeb`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5SC51?format=txt&versions=105)  
**Locator:** `lines 6-7`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 105 / 1.  
**Retrieved:** 2026-11-02T04:31:32.054381+00:00.  

```text
DE   RecName: Full=Hemagglutinin-neuraminidase;
DE            EC=3.2.1.18 {ECO:0000250|UniProtKB:Q9WAF5};
```

Source SHA-256: `8bf1ba1afc5634387cc3311f78ac6fc61cefd51f3d1e338d340ea041cd46beeb`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5SC51?format=txt&versions=105)  
**Locator:** `lines 51-56`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 105 / 1.  
**Retrieved:** 2026-11-02T04:31:32.054381+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=Hydrolysis of alpha-(2->3)-, alpha-(2->6)-, alpha-
CC         (2->8)- glycosidic linkages of terminal sialic acid residues in
CC         oligosaccharides, glycoproteins, glycolipids, colominic acid and
CC         synthetic substrates.; EC=3.2.1.18;
CC         Evidence={ECO:0000250|UniProtKB:Q9WAF5};
```

Source SHA-256: `8bf1ba1afc5634387cc3311f78ac6fc61cefd51f3d1e338d340ea041cd46beeb`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 197. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
