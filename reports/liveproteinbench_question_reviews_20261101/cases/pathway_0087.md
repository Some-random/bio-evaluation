# pathway_0087

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `pathway`  
**Author expected answer:** **C** — Amino-acid degradation. .

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MIVVVIADKEFYGWAESVPYARYDESISTSTKQIKALFCDRSFTRKMELSELINTLPAGAARNALDCAMWDLQAKQSTRPVAEILSKTSITSICAHTLSIDTPKAMQEAVLAMNSPPLVKVKLDKQDIIARMTAIANAAPHSQFIVDANEDWCFRDLEENVEALKALNVVLIEQPLPAGEDEQLINFTSPIPLCADESCHTENDLPYLQGRYQVVNIKLDKTGGLTQACSLASKAQKMGFDIMLGCMVGSSLAMAPASLLASQARYVDLDGPLLVLKDRKHHFTYADGQMSPLQSCLWGGAHNSERFFVDRLQLQ

[Multiple Choices]
A. tetrahydrofolate interconversion. .
B. chorismate biosynthesis
C. Amino-acid degradation. .
D. Metabolic intermediate biosynthesis
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

> The exact sequence matches a UniProt entry annotated as N-acetyl-D-glutamate racemase, with the pathway listed as amino-acid degradation. The annotation cites a study on a D-glutamate catabolic pathway; this supports choice C, though the study was not independently reviewed here.

Citations as saved: [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The input supplies only the sequence and choices; it gives no organism, biochemical function, or pathway context that meaningfully distinguishes these options.


**Missing item-specific fact**

> The sequence’s specific function as N-acetyl-D-glutamate racemase, and its role in amino-acid degradation, is needed to select C.


**Reason**

> Identifying this enzyme and pathway requires protein-specific functional knowledge or an external annotation; no concrete sequence-based argument available in the prompt establishes the pathway.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The matched entry’s pathway annotation specifically supports amino-acid degradation among the listed choices.


### Important caveats

- The reviewer-only database evidence matches the supplied sequence, but was not available to the evaluated model.
- The pathway annotation cites a publication; it is not an independent review of the underlying experiments.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The input supplies only the sequence and choices; it gives no organism, biochemical function, or pathway context that meaningfully distinguishes these options.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The sequence’s specific function as N-acetyl-D-glutamate racemase, and its role in amino-acid degradation, is needed to select C.",
    "reason": "Identifying this enzyme and pathway requires protein-specific functional knowledge or an external annotation; no concrete sequence-based argument available in the prompt establishes the pathway."
  },
  "case_id": "pathway_0087",
  "expected_answer_check": {
    "evidence_ids": [
      "H1",
      "H2",
      "H3",
      "C4",
      "C5",
      "C6"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry annotated as N-acetyl-D-glutamate racemase, with the pathway listed as amino-acid degradation. The annotation cites a study on a D-glutamate catabolic pathway; this supports choice C, though the study was not independently reviewed here."
  },
  "important_caveats": [
    "The reviewer-only database evidence matches the supplied sequence, but was not available to the evaluated model.",
    "The pathway annotation cites a publication; it is not an independent review of the underlying experiments."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched entry’s pathway annotation specifically supports amino-acid degradation among the listed choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0087",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry annotated as N-acetyl-D-glutamate racemase, with the pathway listed as amino-acid degradation. The annotation cites a study on a D-glutamate catabolic pathway; this supports choice C, though the study was not independently reviewed here.",
    "evidence_ids": ["H1", "H2", "H3", "C4", "C5", "C6"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The input supplies only the sequence and choices; it gives no organism, biochemical function, or pathway context that meaningfully distinguishes these options.",
    "missing_item_specific_fact": "The sequence’s specific function as N-acetyl-D-glutamate racemase, and its role in amino-acid degradation, is needed to select C.",
    "reason": "Identifying this enzyme and pathway requires protein-specific functional knowledge or an external annotation; no concrete sequence-based argument available in the prompt establishes the pathway."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched entry’s pathway annotation specifically supports amino-acid degradation among the listed choices."
  },
  "important_caveats": [
    "The reviewer-only database evidence matches the supplied sequence, but was not available to the evaluated model.",
    "The pathway annotation cites a publication; it is not an independent review of the underlying experiments."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry P0DXZ2 (N-acetyl-D-glutamate racemase, EC 5.1.1.25, from Pseudoalteromonas sp.) explicitly annotates the pathway as 'Amino-acid degradation' (evidence code ECO:0000305, derived from PubMed:36690779, Yu et al. 2023 ISME J. 17:537-548, describing a novel D-glutamate catabolic pathway). The benchmark sequence matches the canonical entry (315 AA, SHA256 confirmed). The author's key C matches the UniProt pathway annotation exactly.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence provides no clear motif or structural signature that unambiguously distinguishes 'amino-acid degradation' (C) from 'metabolic intermediate biosynthesis' (D). Racemases acting on amino acid derivatives participate in both catabolic and anabolic pathways. Without prior knowledge that this specific enzyme (N-acetyl-D-glutamate racemase, EC 5.1.1.25) functions in the recently characterized (2023) D-glutamate catabolic pathway, a model cannot reliably select C over D from sequence features alone.


**Missing item-specific fact**

> The specific identity of the protein as N-acetyl-D-glutamate racemase (DgcA) and its role in the novel D-glutamate catabolic pathway described in Yu et al. 2023 (PubMed:36690779). This is a recently characterized enzyme (UniProt entry first public 2025-04-09) whose pathway assignment depends on the specific experimental context of D-glutamate catabolism rather than on generalizable sequence motifs.


**Reason**

> Distinguishing C from D requires knowing that this racemase is specifically part of a D-glutamate degradation pathway rather than an amino-acid-derivative biosynthetic route. The sequence lacks diagnostic motifs (e.g., folate-binding domains for A, chorismate synthase features for B) that would eliminate some options, but the critical C-vs-D discrimination depends entirely on the item-specific annotation from a 2023 publication and its UniProt curation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "C",
  "D"
]
```

> Without the specific annotation, a model might argue D (metabolic intermediate biosynthesis) since N-acetyl-glutamate is a known intermediate in arginine biosynthesis, and racemases can serve biosynthetic roles. However, the UniProt annotation and primary literature clearly place this enzyme in a catabolic (degradation) pathway, making C the correct answer. The ambiguity is resolvable with the annotation but not from sequence alone.


### Important caveats

- The UniProt entry was first publicly released 2025-04-09, and the underlying publication is from 2023. This is a very recent annotation, increasing lookup dependence.
- The pathway annotation uses ECO:0000305 (curator inference from literature), not direct experimental measurement of the pathway assignment itself, though the enzyme's function was experimentally characterized.
- The identity of the protein (accession P0DXZ2) was inferred from dataset metadata and was not available to the evaluated model; the model only had the 315-aa sequence.
- Options A (tetrahydrofolate interconversion) and B (chorismate biosynthesis) are reasonably eliminable by a knowledgeable model through absence of folate-binding or chorismate-synthase motifs, but C vs D remains the critical discrimination.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence provides no clear motif or structural signature that unambiguously distinguishes 'amino-acid degradation' (C) from 'metabolic intermediate biosynthesis' (D). Racemases acting on amino acid derivatives participate in both catabolic and anabolic pathways. Without prior knowledge that this specific enzyme (N-acetyl-D-glutamate racemase, EC 5.1.1.25) functions in the recently characterized (2023) D-glutamate catabolic pathway, a model cannot reliably select C over D from sequence features alone.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific identity of the protein as N-acetyl-D-glutamate racemase (DgcA) and its role in the novel D-glutamate catabolic pathway described in Yu et al. 2023 (PubMed:36690779). This is a recently characterized enzyme (UniProt entry first public 2025-04-09) whose pathway assignment depends on the specific experimental context of D-glutamate catabolism rather than on generalizable sequence motifs.",
    "reason": "Distinguishing C from D requires knowing that this racemase is specifically part of a D-glutamate degradation pathway rather than an amino-acid-derivative biosynthetic route. The sequence lacks diagnostic motifs (e.g., folate-binding domains for A, chorismate synthase features for B) that would eliminate some options, but the critical C-vs-D discrimination depends entirely on the item-specific annotation from a 2023 publication and its UniProt curation."
  },
  "case_id": "pathway_0087",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "H1",
      "H2",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry P0DXZ2 (N-acetyl-D-glutamate racemase, EC 5.1.1.25, from Pseudoalteromonas sp.) explicitly annotates the pathway as 'Amino-acid degradation' (evidence code ECO:0000305, derived from PubMed:36690779, Yu et al. 2023 ISME J. 17:537-548, describing a novel D-glutamate catabolic pathway). The benchmark sequence matches the canonical entry (315 AA, SHA256 confirmed). The author's key C matches the UniProt pathway annotation exactly."
  },
  "important_caveats": [
    "The UniProt entry was first publicly released 2025-04-09, and the underlying publication is from 2023. This is a very recent annotation, increasing lookup dependence.",
    "The pathway annotation uses ECO:0000305 (curator inference from literature), not direct experimental measurement of the pathway assignment itself, though the enzyme's function was experimentally characterized.",
    "The identity of the protein (accession P0DXZ2) was inferred from dataset metadata and was not available to the evaluated model; the model only had the 315-aa sequence.",
    "Options A (tetrahydrofolate interconversion) and B (chorismate biosynthesis) are reasonably eliminable by a knowledgeable model through absence of folate-binding or chorismate-synthase motifs, but C vs D remains the critical discrimination."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "C",
      "D"
    ],
    "reason": "Without the specific annotation, a model might argue D (metabolic intermediate biosynthesis) since N-acetyl-glutamate is a known intermediate in arginine biosynthesis, and racemases can serve biosynthetic roles. However, the UniProt annotation and primary literature clearly place this enzyme in a catabolic (degradation) pathway, making C the correct answer. The ambiguity is resolvable with the annotation but not from sequence alone."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0087",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry P0DXZ2 (N-acetyl-D-glutamate racemase, EC 5.1.1.25, from Pseudoalteromonas sp.) explicitly annotates the pathway as 'Amino-acid degradation' (evidence code ECO:0000305, derived from PubMed:36690779, Yu et al. 2023 ISME J. 17:537-548, describing a novel D-glutamate catabolic pathway). The benchmark sequence matches the canonical entry (315 AA, SHA256 confirmed). The author's key C matches the UniProt pathway annotation exactly.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H1", "H2", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence provides no clear motif or structural signature that unambiguously distinguishes 'amino-acid degradation' (C) from 'metabolic intermediate biosynthesis' (D). Racemases acting on amino acid derivatives participate in both catabolic and anabolic pathways. Without prior knowledge that this specific enzyme (N-acetyl-D-glutamate racemase, EC 5.1.1.25) functions in the recently characterized (2023) D-glutamate catabolic pathway, a model cannot reliably select C over D from sequence features alone.",
    "missing_item_specific_fact": "The specific identity of the protein as N-acetyl-D-glutamate racemase (DgcA) and its role in the novel D-glutamate catabolic pathway described in Yu et al. 2023 (PubMed:36690779). This is a recently characterized enzyme (UniProt entry first public 2025-04-09) whose pathway assignment depends on the specific experimental context of D-glutamate catabolism rather than on generalizable sequence motifs.",
    "reason": "Distinguishing C from D requires knowing that this racemase is specifically part of a D-glutamate degradation pathway rather than an amino-acid-derivative biosynthetic route. The sequence lacks diagnostic motifs (e.g., folate-binding domains for A, chorismate synthase features for B) that would eliminate some options, but the critical C-vs-D discrimination depends entirely on the item-specific annotation from a 2023 publication and its UniProt curation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["C", "D"],
    "reason": "Without the specific annotation, a model might argue D (metabolic intermediate biosynthesis) since N-acetyl-glutamate is a known intermediate in arginine biosynthesis, and racemases can serve biosynthetic roles. However, the UniProt annotation and primary literature clearly place this enzyme in a catabolic (degradation) pathway, making C the correct answer. The ambiguity is resolvable with the annotation but not from sequence alone."
  },
  "important_caveats": [
    "The UniProt entry was first publicly released 2025-04-09, and the underlying publication is from 2023. This is a very recent annotation, increasing lookup dependence.",
    "The pathway annotation uses ECO:0000305 (curator inference from literature), not direct experimental measurement of the pathway assignment itself, though the enzyme's function was experimentally characterized.",
    "The identity of the protein (accession P0DXZ2) was inferred from dataset metadata and was not available to the evaluated model; the model only had the 315-aa sequence.",
    "Options A (tetrahydrofolate interconversion) and B (chorismate biosynthesis) are reasonably eliminable by a knowledgeable model through absence of folate-binding or chorismate-synthase motifs, but C vs D remains the critical discrimination."
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

**Accession:** `P0DXZ2` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 3. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXZ2.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:09.095372+00:00.  

```json
"P0DXZ2"
```

Source SHA-256: `ce4ce37f5eba503f3ded1200adaf39a2c1cec4022ddf9b32af66f9212c2586ea`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXZ2.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:09.095372+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"36690779","source":"PubMed"}],"value":"5.1.1.25"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"36690779","source":"PubMed"}],"value":"N-acetyl-D-glutamate racemase"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"36690779","source":"PubMed"}],"value":"N-acetyl-D-Glu racemase"}]}}
```

Source SHA-256: `ce4ce37f5eba503f3ded1200adaf39a2c1cec4022ddf9b32af66f9212c2586ea`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXZ2.json)  
**Locator:** `/comments/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:09.095372+00:00.  

```json
{"commentType":"PATHWAY","texts":[{"evidences":[{"evidenceCode":"ECO:0000305","id":"36690779","source":"PubMed"}],"value":"Amino-acid degradation"}]}
```

Source SHA-256: `ce4ce37f5eba503f3ded1200adaf39a2c1cec4022ddf9b32af66f9212c2586ea`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXZ2.json)  
**Locator:** `/references/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:09.095372+00:00.  

```json
{"citation":{"authors":["Yu Y.","Wang P.","Cao H.Y.","Teng Z.J.","Zhu Y.","Wang M.","McMinn A.","Chen Y.","Xiang H.","Zhang Y.Z.","Chen X.L.","Zhang Y.Q."],"citationCrossReferences":[{"database":"PubMed","id":"36690779"},{"database":"DOI","id":"10.1038/s41396-023-01364-6"}],"citationType":"journal article","firstPage":"537","id":"36690779","journal":"ISME J.","lastPage":"548","publicationDate":"2023","title":"Novel D-glutamate catabolic pathway in marine Proteobacteria and halophilic archaea.","volume":"17"},"referenceComments":[{"type":"STRAIN","value":"CF6-2"}],"referenceNumber":1,"referencePositions":["NUCLEOTIDE SEQUENCE [GENOMIC DNA]","FUNCTION","CATALYTIC ACTIVITY","INDUCTION","DISRUPTION PHENOTYPE"]}
```

Source SHA-256: `ce4ce37f5eba503f3ded1200adaf39a2c1cec4022ddf9b32af66f9212c2586ea`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXZ2?format=txt&versions=3)  
**Locator:** `lines 1-13`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 3 / 1.  
**Retrieved:** 2026-11-01T06:41:59.066573+00:00.  

```text
ID   DGCA_PSEAS              Reviewed;         315 AA.
AC   P0DXZ2;
DT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.
DT   09-APR-2025, sequence version 1.
DT   28-JAN-2026, entry version 3.
DE   RecName: Full=N-acetyl-D-glutamate racemase {ECO:0000303|PubMed:36690779};
DE            Short=N-acetyl-D-Glu racemase {ECO:0000303|PubMed:36690779};
DE            EC=5.1.1.25 {ECO:0000269|PubMed:36690779};
GN   Name=dgcA {ECO:0000303|PubMed:36690779};
OS   Pseudoalteromonas sp.
OC   Bacteria; Pseudomonadati; Pseudomonadota; Gammaproteobacteria;
OC   Alteromonadales; Pseudoalteromonadaceae; Pseudoalteromonas.
OX   NCBI_TaxID=53249;
```

Source SHA-256: `e4cce17ff5162859998568df20b58b36b0722c6040f9c24adb62cf5a2aed600d`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXZ2?format=txt&versions=3)  
**Locator:** `lines 14-23`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 3 / 1.  
**Retrieved:** 2026-11-01T06:41:59.066573+00:00.  

```text
RN   [1]
RP   NUCLEOTIDE SEQUENCE [GENOMIC DNA], FUNCTION, CATALYTIC ACTIVITY, INDUCTION,
RP   AND DISRUPTION PHENOTYPE.
RC   STRAIN=CF6-2;
RX   PubMed=36690779; DOI=10.1038/s41396-023-01364-6;
RA   Yu Y., Wang P., Cao H.Y., Teng Z.J., Zhu Y., Wang M., McMinn A., Chen Y.,
RA   Xiang H., Zhang Y.Z., Chen X.L., Zhang Y.Q.;
RT   "Novel D-glutamate catabolic pathway in marine Proteobacteria and
RT   halophilic archaea.";
RL   ISME J. 17:537-548(2023).
```

Source SHA-256: `e4cce17ff5162859998568df20b58b36b0722c6040f9c24adb62cf5a2aed600d`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXZ2?format=txt&versions=3)  
**Locator:** `lines 41-41`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 3 / 1.  
**Retrieved:** 2026-11-01T06:41:59.066573+00:00.  

```text
CC   -!- PATHWAY: Amino-acid degradation. {ECO:0000305|PubMed:36690779}.
```

Source SHA-256: `e4cce17ff5162859998568df20b58b36b0722c6040f9c24adb62cf5a2aed600d`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 87. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
