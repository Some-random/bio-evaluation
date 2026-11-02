# pathway_0018

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `pathway`  
**Author expected answer:** **C** — Amino-acid biosynthesis

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MSQSPTNVPRSYNSVLDLKLASPTNSASGATGGWIVQKFGGTSVGKFPENIVDNIVKVYSQTNRVAVVCSARSSQTKSEGTTSRLLRSADLAENDKDYQPLLNAIEEDHVTNAERIQSEEIKQELIKDTKQEIEHVRELLHACQIIGEISPRSLDSIMAVGEKLSCLFMTALMKDHGLNAVYINLQDVIPLSYDFQKGFDDSFYQFLSQEIGKRVLQCDKEREGEEDVIPVLTGYFGVVPGGLLNGVGRGYTDLCAALAAVALQADELQIWKEVDGIFTADPRKVPNARLLDSVTPEEAAELTYYGSEVIHPFTMEQVIRAKIPIRIKNVENPTGKGTIIYPDNIGRRGEATPPHPPAAFEQLAMSSLLQRKRSATAITAKQDIVVINIHSNKKTLSHGFLAHVFTTLDKYKLVVDLISTSEVHVSMALSIQSDQESQLKHALVDLRKMGTVDVTKKMTIVSLVGKQMVNFIGIAGNMFKVLADEKINIEMISQGANEINISAVINEKDTIRALKSIHAKLLEGGSAIGDSSAVDTRLEALKLS

[Multiple Choices]
A. glycosylphosphatidylinositol-anchor biosynthesis. .
B. Pigment biosynthesis. .
C. Amino-acid biosynthesis
D. deamido-NAD(+) from nicotinate D-ribonucleotide: step 1/1. .
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

> The exact-matched sequence is annotated as aspartokinase, with amino-acid biosynthesis pathways listed for it. The annotation is transferred by similarity from UniProtKB:P10869 (ECO:0000250), so it supports choice C but does not establish direct experimental validation for this protein.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H2](#evidence-h2), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The choices name distinct pathways, but the supplied sequence alone does not give a sufficiently specific, unambiguous basis to identify its pathway as amino-acid biosynthesis.


**Missing item-specific fact**

> The protein's identity or functional annotation as aspartokinase, or equivalent protein-specific evidence linking its activity to amino-acid biosynthesis.


**Reason**

> Selecting C depends on recognizing or externally identifying this particular sequence's function. General sequence-based reasoning does not independently establish the pathway.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The provided annotation links the sequence to amino-acid biosynthesis, while the other choices describe different pathways.


### Important caveats

- The sequence match is exact, but the pathway and enzyme annotations are based on similarity transfer rather than direct experimental evidence in the supplied evidence.
- The author's precise source snapshot is unknown; a historical matched record also supports the same pathway assignment.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The choices name distinct pathways, but the supplied sequence alone does not give a sufficiently specific, unambiguous basis to identify its pathway as amino-acid biosynthesis.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein's identity or functional annotation as aspartokinase, or equivalent protein-specific evidence linking its activity to amino-acid biosynthesis.",
    "reason": "Selecting C depends on recognizing or externally identifying this particular sequence's function. General sequence-based reasoning does not independently establish the pathway."
  },
  "case_id": "pathway_0018",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "H2",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The exact-matched sequence is annotated as aspartokinase, with amino-acid biosynthesis pathways listed for it. The annotation is transferred by similarity from UniProtKB:P10869 (ECO:0000250), so it supports choice C but does not establish direct experimental validation for this protein."
  },
  "important_caveats": [
    "The sequence match is exact, but the pathway and enzyme annotations are based on similarity transfer rather than direct experimental evidence in the supplied evidence.",
    "The author's precise source snapshot is unknown; a historical matched record also supports the same pathway assignment."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The provided annotation links the sequence to amino-acid biosynthesis, while the other choices describe different pathways."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0018",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact-matched sequence is annotated as aspartokinase, with amino-acid biosynthesis pathways listed for it. The annotation is transferred by similarity from UniProtKB:P10869 (ECO:0000250), so it supports choice C but does not establish direct experimental validation for this protein.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H2", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The choices name distinct pathways, but the supplied sequence alone does not give a sufficiently specific, unambiguous basis to identify its pathway as amino-acid biosynthesis.",
    "missing_item_specific_fact": "The protein's identity or functional annotation as aspartokinase, or equivalent protein-specific evidence linking its activity to amino-acid biosynthesis.",
    "reason": "Selecting C depends on recognizing or externally identifying this particular sequence's function. General sequence-based reasoning does not independently establish the pathway."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The provided annotation links the sequence to amino-acid biosynthesis, while the other choices describe different pathways."
  },
  "important_caveats": [
    "The sequence match is exact, but the pathway and enzyme annotations are based on similarity transfer rather than direct experimental evidence in the supplied evidence.",
    "The author's precise source snapshot is unknown; a historical matched record also supports the same pathway assignment."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A0A1D8PMB8 annotates this protein as Aspartokinase (EC 2.7.2.4, gene HOM3) and assigns it to 'Amino-acid biosynthesis' in two pathway comments (L-methionine biosynthesis step 1/3 and L-threonine biosynthesis step 1/5). The annotation is based on similarity to P10869 (ECO:0000250, computational inference), but aspartokinase's role in amino acid biosynthesis is extremely well-established biochemistry. The expected answer C ('Amino-acid biosynthesis') directly matches the pathway category in the annotation.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a recognizable P-loop/Walker A kinase motif (GGTSVGKF near residues 28-35), indicating this is a kinase. Among the four options, amino-acid biosynthesis is the only pathway whose primary enzymatic steps include amino acid kinases (aspartokinase, glutamate 5-kinase, etc.) that phosphorylate amino acid substrates. GPI-anchor biosynthesis is dominated by glycosyltransferases; pigment biosynthesis involves oxidoreductases and cyclases; NAD+ biosynthesis involves phosphoribosyltransferases and adenylyltransferases. Recognizing the kinase fold and connecting amino acid kinases to amino acid biosynthesis is general biochemical knowledge that meaningfully distinguishes option C from the distractors.


**Missing item-specific fact**

> Precise identification of the enzyme as aspartokinase (EC 2.7.2.4) specifically requires either sequence recognition or database lookup, but the pathway assignment to 'amino-acid biosynthesis' follows from the general reasoning that a small-molecule kinase acting on an amino acid substrate belongs to amino acid biosynthesis, and none of the other three options feature amino acid kinases as primary enzymes.


**Reason**

> The P-loop motif is identifiable from the raw sequence, and the connection between amino acid kinases and amino acid biosynthesis is standard biochemistry. The distractors are clearly unrelated to kinase-dominated pathways, making the correct answer reachable through general biological reasoning without memorizing the specific UniProt entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options represent clearly distinct metabolic pathways. Only 'Amino-acid biosynthesis' is consistent with a kinase acting on an amino acid substrate. The other three options (GPI-anchor, pigment, NAD+) do not feature amino acid kinases as primary pathway enzymes.


### Important caveats

- The UniProt pathway annotation is based on similarity (ECO:0000250) to S. cerevisiae aspartokinase P10869, not on direct experimental characterization of the Candida albicans enzyme. However, aspartokinase function in amino acid biosynthesis is universally established.
- The sequence-to-accession mapping was inferred from reviewer-only metadata; the evaluated model received only the raw sequence.
- Option D ('deamido-NAD(+) from nicotinate D-ribonucleotide: step 1/1') is oddly specific and appears to be a UniProt-style pathway step label, making it an unusual distractor format compared to the broader category labels in A, B, C.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a recognizable P-loop/Walker A kinase motif (GGTSVGKF near residues 28-35), indicating this is a kinase. Among the four options, amino-acid biosynthesis is the only pathway whose primary enzymatic steps include amino acid kinases (aspartokinase, glutamate 5-kinase, etc.) that phosphorylate amino acid substrates. GPI-anchor biosynthesis is dominated by glycosyltransferases; pigment biosynthesis involves oxidoreductases and cyclases; NAD+ biosynthesis involves phosphoribosyltransferases and adenylyltransferases. Recognizing the kinase fold and connecting amino acid kinases to amino acid biosynthesis is general biochemical knowledge that meaningfully distinguishes option C from the distractors.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "Precise identification of the enzyme as aspartokinase (EC 2.7.2.4) specifically requires either sequence recognition or database lookup, but the pathway assignment to 'amino-acid biosynthesis' follows from the general reasoning that a small-molecule kinase acting on an amino acid substrate belongs to amino acid biosynthesis, and none of the other three options feature amino acid kinases as primary enzymes.",
    "reason": "The P-loop motif is identifiable from the raw sequence, and the connection between amino acid kinases and amino acid biosynthesis is standard biochemistry. The distractors are clearly unrelated to kinase-dominated pathways, making the correct answer reachable through general biological reasoning without memorizing the specific UniProt entry."
  },
  "case_id": "pathway_0018",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H1",
      "H2",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry A0A1D8PMB8 annotates this protein as Aspartokinase (EC 2.7.2.4, gene HOM3) and assigns it to 'Amino-acid biosynthesis' in two pathway comments (L-methionine biosynthesis step 1/3 and L-threonine biosynthesis step 1/5). The annotation is based on similarity to P10869 (ECO:0000250, computational inference), but aspartokinase's role in amino acid biosynthesis is extremely well-established biochemistry. The expected answer C ('Amino-acid biosynthesis') directly matches the pathway category in the annotation."
  },
  "important_caveats": [
    "The UniProt pathway annotation is based on similarity (ECO:0000250) to S. cerevisiae aspartokinase P10869, not on direct experimental characterization of the Candida albicans enzyme. However, aspartokinase function in amino acid biosynthesis is universally established.",
    "The sequence-to-accession mapping was inferred from reviewer-only metadata; the evaluated model received only the raw sequence.",
    "Option D ('deamido-NAD(+) from nicotinate D-ribonucleotide: step 1/1') is oddly specific and appears to be a UniProt-style pathway step label, making it an unusual distractor format compared to the broader category labels in A, B, C."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent clearly distinct metabolic pathways. Only 'Amino-acid biosynthesis' is consistent with a kinase acting on an amino acid substrate. The other three options (GPI-anchor, pigment, NAD+) do not feature amino acid kinases as primary pathway enzymes."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0018",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A0A1D8PMB8 annotates this protein as Aspartokinase (EC 2.7.2.4, gene HOM3) and assigns it to 'Amino-acid biosynthesis' in two pathway comments (L-methionine biosynthesis step 1/3 and L-threonine biosynthesis step 1/5). The annotation is based on similarity to P10869 (ECO:0000250, computational inference), but aspartokinase's role in amino acid biosynthesis is extremely well-established biochemistry. The expected answer C ('Amino-acid biosynthesis') directly matches the pathway category in the annotation.",
    "evidence_ids": ["C4", "C5", "C6", "H1", "H2", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a recognizable P-loop/Walker A kinase motif (GGTSVGKF near residues 28-35), indicating this is a kinase. Among the four options, amino-acid biosynthesis is the only pathway whose primary enzymatic steps include amino acid kinases (aspartokinase, glutamate 5-kinase, etc.) that phosphorylate amino acid substrates. GPI-anchor biosynthesis is dominated by glycosyltransferases; pigment biosynthesis involves oxidoreductases and cyclases; NAD+ biosynthesis involves phosphoribosyltransferases and adenylyltransferases. Recognizing the kinase fold and connecting amino acid kinases to amino acid biosynthesis is general biochemical knowledge that meaningfully distinguishes option C from the distractors.",
    "missing_item_specific_fact": "Precise identification of the enzyme as aspartokinase (EC 2.7.2.4) specifically requires either sequence recognition or database lookup, but the pathway assignment to 'amino-acid biosynthesis' follows from the general reasoning that a small-molecule kinase acting on an amino acid substrate belongs to amino acid biosynthesis, and none of the other three options feature amino acid kinases as primary enzymes.",
    "reason": "The P-loop motif is identifiable from the raw sequence, and the connection between amino acid kinases and amino acid biosynthesis is standard biochemistry. The distractors are clearly unrelated to kinase-dominated pathways, making the correct answer reachable through general biological reasoning without memorizing the specific UniProt entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent clearly distinct metabolic pathways. Only 'Amino-acid biosynthesis' is consistent with a kinase acting on an amino acid substrate. The other three options (GPI-anchor, pigment, NAD+) do not feature amino acid kinases as primary pathway enzymes."
  },
  "important_caveats": [
    "The UniProt pathway annotation is based on similarity (ECO:0000250) to S. cerevisiae aspartokinase P10869, not on direct experimental characterization of the Candida albicans enzyme. However, aspartokinase function in amino acid biosynthesis is universally established.",
    "The sequence-to-accession mapping was inferred from reviewer-only metadata; the evaluated model received only the raw sequence.",
    "Option D ('deamido-NAD(+) from nicotinate D-ribonucleotide: step 1/1') is oddly specific and appears to be a UniProt-style pathway step label, making it an unusual distractor format compared to the broader category labels in A, B, C."
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

**Accession:** `A0A1D8PMB8` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 39. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A1D8PMB8.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:32.794689+00:00.  

```json
"A0A1D8PMB8"
```

Source SHA-256: `7c688e4eaabc3e4781e5ade84edef7517de0ae1c9eaf84cba6bd0311b17eacc2`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A1D8PMB8.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:32.794689+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"P10869","source":"UniProtKB"}],"value":"2.7.2.4"}],"fullName":{"value":"Aspartokinase"}}}
```

Source SHA-256: `7c688e4eaabc3e4781e5ade84edef7517de0ae1c9eaf84cba6bd0311b17eacc2`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A1D8PMB8.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:32.794689+00:00.  

```json
{"commentType":"PATHWAY","texts":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"P10869","source":"UniProtKB"}],"value":"Amino-acid biosynthesis; L-methionine biosynthesis via de novo pathway; L-homoserine from L-aspartate: step 1/3"}]}
```

Source SHA-256: `7c688e4eaabc3e4781e5ade84edef7517de0ae1c9eaf84cba6bd0311b17eacc2`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A1D8PMB8.json)  
**Locator:** `/comments/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:32.794689+00:00.  

```json
{"commentType":"PATHWAY","texts":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"P10869","source":"UniProtKB"}],"value":"Amino-acid biosynthesis; L-threonine biosynthesis; L-threonine from L-aspartate: step 1/5"}]}
```

Source SHA-256: `7c688e4eaabc3e4781e5ade84edef7517de0ae1c9eaf84cba6bd0311b17eacc2`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A1D8PMB8?format=txt&versions=39)  
**Locator:** `lines 1-14`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 39 / 1.  
**Retrieved:** 2026-11-02T04:24:35.627360+00:00.  

```text
ID   AK_CANAL                Reviewed;         544 AA.
AC   A0A1D8PMB8;
DT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.
DT   18-JAN-2017, sequence version 1.
DT   18-JUN-2025, entry version 39.
DE   RecName: Full=Aspartokinase;
DE            EC=2.7.2.4 {ECO:0000250|UniProtKB:P10869};
GN   Name=HOM3 {ECO:0000312|CGD:CAL0000181037};
GN   OrderedLocusNames=CAALFM_C405540WA {ECO:0000312|EMBL:AOW29286.1},
GN   orf19.8820 {ECO:0000312|CGD:CAL0000181037};
OS   Candida albicans (strain SC5314 / ATCC MYA-2876) (Yeast).
OC   Eukaryota; Fungi; Dikarya; Ascomycota; Saccharomycotina; Pichiomycetes;
OC   Debaryomycetaceae; Candida/Lodderomyces clade; Candida.
OX   NCBI_TaxID=237561 {ECO:0000312|Proteomes:UP000000559};
```

Source SHA-256: `25e1c2e406fb09fd648127e1e60780d1244490e7b9ae80cba023db5b2b691f93`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A1D8PMB8?format=txt&versions=39)  
**Locator:** `lines 70-72`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 39 / 1.  
**Retrieved:** 2026-11-02T04:24:35.627360+00:00.  

```text
CC   -!- PATHWAY: Amino-acid biosynthesis; L-methionine biosynthesis via de novo
CC       pathway; L-homoserine from L-aspartate: step 1/3.
CC       {ECO:0000250|UniProtKB:P10869}.
```

Source SHA-256: `25e1c2e406fb09fd648127e1e60780d1244490e7b9ae80cba023db5b2b691f93`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A1D8PMB8?format=txt&versions=39)  
**Locator:** `lines 73-74`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 39 / 1.  
**Retrieved:** 2026-11-02T04:24:35.627360+00:00.  

```text
CC   -!- PATHWAY: Amino-acid biosynthesis; L-threonine biosynthesis; L-threonine
CC       from L-aspartate: step 1/5. {ECO:0000250|UniProtKB:P10869}.
```

Source SHA-256: `25e1c2e406fb09fd648127e1e60780d1244490e7b9ae80cba023db5b2b691f93`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 18. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
