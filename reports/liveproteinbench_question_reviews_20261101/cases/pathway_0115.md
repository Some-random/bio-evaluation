# pathway_0115

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `pathway`  
**Author expected answer:** **C** — Glycan degradation

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MITFSSLLVTFSAISTSLAIPGSILPKRSPMNFVLQRNESSLVRRATPNYEQDYTTGGDVIYTPSGSSFTVDWSTEDDFVVGLGWTTGSTNPINFSGTFGIGSGTALLSIYGWSENPLVEYYIVEDSASPPSFGTVKGSVTSDGSSYTIWENQRVNEPSIVGTATFNQYISVRSSPRKSGTVTVENHFQAWAALGMNLGTLNYQVLAVEGWGGEGAATQTVS

[Multiple Choices]
A. Cell wall degradation
B. Amino-acid degradation
C. Glycan degradation
D. Carotenoid biosynthesis
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

> The exact sequence matches a Botrytis cinerea protein annotated as an endo-1,4-beta-xylanase, EC 3.2.1.8, with the pathway assignment “Glycan degradation; xylan degradation.” This supports choice C, although the pathway annotation is attributed to a computational PROSITE rule rather than direct experimental pathway evidence.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The N-terminal sequence is consistent with a secreted protein, but secretion alone does not establish its substrate or pathway. Identifying it as a xylanase would make glycan degradation a defensible choice.


**Missing item-specific fact**

> The input does not provide the protein's xylanase identity or its substrate specificity; those protein-specific facts are needed to distinguish the pathway choices.


**Reason**

> The matching annotation supports the key, but it is reviewer-only information. The sequence and choices do not explicitly supply the enzyme identity, and recognizing the precise protein or family would rely on protein-specific knowledge rather than a clear pathway deduction from the provided context.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "C"
]
```

> Xylan is a glycan and a component of plant cell walls. A xylan-degrading enzyme can therefore be described as functioning in glycan degradation or cell wall degradation; the question does not define how to choose between those overlapping descriptions.


### Important caveats

- The sequence match is exact, but the source annotation's pathway evidence is computational (PROSITE-ProRule); the cited literature reference alone does not establish experimental validation of that pathway assignment.
- The historical source record also matches the sequence and carries the glycan-degradation annotation, but the author's exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal sequence is consistent with a secreted protein, but secretion alone does not establish its substrate or pathway. Identifying it as a xylanase would make glycan degradation a defensible choice.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The input does not provide the protein's xylanase identity or its substrate specificity; those protein-specific facts are needed to distinguish the pathway choices.",
    "reason": "The matching annotation supports the key, but it is reviewer-only information. The sequence and choices do not explicitly supply the enzyme identity, and recognizing the precise protein or family would rely on protein-specific knowledge rather than a clear pathway deduction from the provided context."
  },
  "case_id": "pathway_0115",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches a Botrytis cinerea protein annotated as an endo-1,4-beta-xylanase, EC 3.2.1.8, with the pathway assignment “Glycan degradation; xylan degradation.” This supports choice C, although the pathway annotation is attributed to a computational PROSITE rule rather than direct experimental pathway evidence."
  },
  "important_caveats": [
    "The sequence match is exact, but the source annotation's pathway evidence is computational (PROSITE-ProRule); the cited literature reference alone does not establish experimental validation of that pathway assignment.",
    "The historical source record also matches the sequence and carries the glycan-degradation annotation, but the author's exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "C"
    ],
    "reason": "Xylan is a glycan and a component of plant cell walls. A xylan-degrading enzyme can therefore be described as functioning in glycan degradation or cell wall degradation; the question does not define how to choose between those overlapping descriptions."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0115",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches a Botrytis cinerea protein annotated as an endo-1,4-beta-xylanase, EC 3.2.1.8, with the pathway assignment “Glycan degradation; xylan degradation.” This supports choice C, although the pathway annotation is attributed to a computational PROSITE rule rather than direct experimental pathway evidence.",
    "evidence_ids": ["C4", "C5", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The N-terminal sequence is consistent with a secreted protein, but secretion alone does not establish its substrate or pathway. Identifying it as a xylanase would make glycan degradation a defensible choice.",
    "missing_item_specific_fact": "The input does not provide the protein's xylanase identity or its substrate specificity; those protein-specific facts are needed to distinguish the pathway choices.",
    "reason": "The matching annotation supports the key, but it is reviewer-only information. The sequence and choices do not explicitly supply the enzyme identity, and recognizing the precise protein or family would rely on protein-specific knowledge rather than a clear pathway deduction from the provided context."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "C"],
    "reason": "Xylan is a glycan and a component of plant cell walls. A xylan-degrading enzyme can therefore be described as functioning in glycan degradation or cell wall degradation; the question does not define how to choose between those overlapping descriptions."
  },
  "important_caveats": [
    "The sequence match is exact, but the source annotation's pathway evidence is computational (PROSITE-ProRule); the cited literature reference alone does not establish experimental validation of that pathway assignment.",
    "The historical source record also matches the sequence and carries the glycan-degradation annotation, but the author's exact source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A0A384K474 (EIX2_BOTFB) for this exact 222-aa sequence annotates the protein as Ethylene-inducing xylanase 2 (EC 3.2.1.8, Endo-1,4-beta-xylanase) with the pathway 'Glycan degradation; xylan degradation' (evidence code ECO:0000255 via PROSITE-ProRule PRU01097). This directly supports choice C. The pathway assignment is based on PROSITE-ProRule motif matching (computational inference from the GH11 xylanase family signature), not a standalone experimental pathway assay, but it is a well-established family-level annotation.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H1](#evidence-h1), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence exhibits a clear N-terminal signal peptide (MITFSSLLVTFSAISTSLAIPG), indicating a secreted extracellular enzyme. The central region contains hallmark glycoside hydrolase family 11 (GH11) xylanase motifs: the conserved 'GWTTGSTNPINFSGTFGIGSGTALLSIYGWSENPLVEYY' stretch and the 'TATFNQY' / 'GWGGEGAATQTVS' C-terminal signature are well-known GH11 family signatures. Recognizing GH11 → xylanase → xylan is a glycan → glycan degradation is a defensible chain of general protein-biochemistry reasoning. Options B (amino-acid degradation) and D (carotenoid biosynthesis) are readily excluded by the secreted-hydrolase context. Option A (cell wall degradation) is biologically adjacent but the specific UniProt pathway taxonomy places xylan degradation under 'Glycan degradation,' and a xylanase's primary biochemical reaction is glycosidic-bond hydrolysis of a glycan polymer.


**Missing item-specific fact**

> The exact UniProt pathway nomenclature ('Glycan degradation; xylan degradation' vs. a hypothetical 'Cell wall degradation' label) is a taxonomic convention. However, the GH11 fold recognition and the logical step xylan = glycan provide sufficient general-knowledge grounds to prefer C over A without needing to memorize this particular entry's annotation.


**Reason**

> A model with standard protein-family knowledge can recognize the GH11 xylanase fold from the conserved motifs, infer xylanase activity, and reason that xylan is a glycan, landing on 'Glycan degradation.' The distractors B and D are clearly incompatible with a secreted hydrolase. The A-vs-C distinction is partly taxonomic but is resolvable by noting that the enzyme's catalytic mechanism (endo-β-1,4-glycosidic bond hydrolysis) is fundamentally glycan chemistry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "C"
]
```

> Xylan is a major component of plant cell walls, so 'Cell wall degradation' (A) is a biologically valid description of the enzyme's ecological role. The UniProt pathway taxonomy specifically uses 'Glycan degradation; xylan degradation,' making C the formally correct label, but a test-taker reasoning from function alone could reasonably argue for A. The question is not ambiguous enough to invalidate C as the best answer, but A is not a trivially wrong distractor.


### Important caveats

- The pathway annotation (ECO:0000255, PROSITE-ProRule) is a computational family-level inference from the GH11 signature, not a direct experimental measurement of a pathway flux in Botrytis cinerea.
- The protein is also known as an ethylene-inducing elicitor in plant-pathogen interactions, but the UniProt pathway annotation focuses on its enzymatic (xylanase) activity, which is what the question targets.
- The sequence match is confirmed across both the current (v27) and historical (v25) UniProt records; the 222-aa benchmark sequence is identical to the canonical entry.
- The accession A0A384K474 was inferred by the reviewer from dataset metadata and was not provided to the evaluated model; the model must work from the raw sequence alone.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence exhibits a clear N-terminal signal peptide (MITFSSLLVTFSAISTSLAIPG), indicating a secreted extracellular enzyme. The central region contains hallmark glycoside hydrolase family 11 (GH11) xylanase motifs: the conserved 'GWTTGSTNPINFSGTFGIGSGTALLSIYGWSENPLVEYY' stretch and the 'TATFNQY' / 'GWGGEGAATQTVS' C-terminal signature are well-known GH11 family signatures. Recognizing GH11 → xylanase → xylan is a glycan → glycan degradation is a defensible chain of general protein-biochemistry reasoning. Options B (amino-acid degradation) and D (carotenoid biosynthesis) are readily excluded by the secreted-hydrolase context. Option A (cell wall degradation) is biologically adjacent but the specific UniProt pathway taxonomy places xylan degradation under 'Glycan degradation,' and a xylanase's primary biochemical reaction is glycosidic-bond hydrolysis of a glycan polymer.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The exact UniProt pathway nomenclature ('Glycan degradation; xylan degradation' vs. a hypothetical 'Cell wall degradation' label) is a taxonomic convention. However, the GH11 fold recognition and the logical step xylan = glycan provide sufficient general-knowledge grounds to prefer C over A without needing to memorize this particular entry's annotation.",
    "reason": "A model with standard protein-family knowledge can recognize the GH11 xylanase fold from the conserved motifs, infer xylanase activity, and reason that xylan is a glycan, landing on 'Glycan degradation.' The distractors B and D are clearly incompatible with a secreted hydrolase. The A-vs-C distinction is partly taxonomic but is resolvable by noting that the enzyme's catalytic mechanism (endo-β-1,4-glycosidic bond hydrolysis) is fundamentally glycan chemistry."
  },
  "case_id": "pathway_0115",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H1",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry A0A384K474 (EIX2_BOTFB) for this exact 222-aa sequence annotates the protein as Ethylene-inducing xylanase 2 (EC 3.2.1.8, Endo-1,4-beta-xylanase) with the pathway 'Glycan degradation; xylan degradation' (evidence code ECO:0000255 via PROSITE-ProRule PRU01097). This directly supports choice C. The pathway assignment is based on PROSITE-ProRule motif matching (computational inference from the GH11 xylanase family signature), not a standalone experimental pathway assay, but it is a well-established family-level annotation."
  },
  "important_caveats": [
    "The pathway annotation (ECO:0000255, PROSITE-ProRule) is a computational family-level inference from the GH11 signature, not a direct experimental measurement of a pathway flux in Botrytis cinerea.",
    "The protein is also known as an ethylene-inducing elicitor in plant-pathogen interactions, but the UniProt pathway annotation focuses on its enzymatic (xylanase) activity, which is what the question targets.",
    "The sequence match is confirmed across both the current (v27) and historical (v25) UniProt records; the 222-aa benchmark sequence is identical to the canonical entry.",
    "The accession A0A384K474 was inferred by the reviewer from dataset metadata and was not provided to the evaluated model; the model must work from the raw sequence alone."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "C"
    ],
    "reason": "Xylan is a major component of plant cell walls, so 'Cell wall degradation' (A) is a biologically valid description of the enzyme's ecological role. The UniProt pathway taxonomy specifically uses 'Glycan degradation; xylan degradation,' making C the formally correct label, but a test-taker reasoning from function alone could reasonably argue for A. The question is not ambiguous enough to invalidate C as the best answer, but A is not a trivially wrong distractor."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0115",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A0A384K474 (EIX2_BOTFB) for this exact 222-aa sequence annotates the protein as Ethylene-inducing xylanase 2 (EC 3.2.1.8, Endo-1,4-beta-xylanase) with the pathway 'Glycan degradation; xylan degradation' (evidence code ECO:0000255 via PROSITE-ProRule PRU01097). This directly supports choice C. The pathway assignment is based on PROSITE-ProRule motif matching (computational inference from the GH11 xylanase family signature), not a standalone experimental pathway assay, but it is a well-established family-level annotation.",
    "evidence_ids": ["C4", "C5", "H1", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence exhibits a clear N-terminal signal peptide (MITFSSLLVTFSAISTSLAIPG), indicating a secreted extracellular enzyme. The central region contains hallmark glycoside hydrolase family 11 (GH11) xylanase motifs: the conserved 'GWTTGSTNPINFSGTFGIGSGTALLSIYGWSENPLVEYY' stretch and the 'TATFNQY' / 'GWGGEGAATQTVS' C-terminal signature are well-known GH11 family signatures. Recognizing GH11 → xylanase → xylan is a glycan → glycan degradation is a defensible chain of general protein-biochemistry reasoning. Options B (amino-acid degradation) and D (carotenoid biosynthesis) are readily excluded by the secreted-hydrolase context. Option A (cell wall degradation) is biologically adjacent but the specific UniProt pathway taxonomy places xylan degradation under 'Glycan degradation,' and a xylanase's primary biochemical reaction is glycosidic-bond hydrolysis of a glycan polymer.",
    "missing_item_specific_fact": "The exact UniProt pathway nomenclature ('Glycan degradation; xylan degradation' vs. a hypothetical 'Cell wall degradation' label) is a taxonomic convention. However, the GH11 fold recognition and the logical step xylan = glycan provide sufficient general-knowledge grounds to prefer C over A without needing to memorize this particular entry's annotation.",
    "reason": "A model with standard protein-family knowledge can recognize the GH11 xylanase fold from the conserved motifs, infer xylanase activity, and reason that xylan is a glycan, landing on 'Glycan degradation.' The distractors B and D are clearly incompatible with a secreted hydrolase. The A-vs-C distinction is partly taxonomic but is resolvable by noting that the enzyme's catalytic mechanism (endo-β-1,4-glycosidic bond hydrolysis) is fundamentally glycan chemistry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "C"],
    "reason": "Xylan is a major component of plant cell walls, so 'Cell wall degradation' (A) is a biologically valid description of the enzyme's ecological role. The UniProt pathway taxonomy specifically uses 'Glycan degradation; xylan degradation,' making C the formally correct label, but a test-taker reasoning from function alone could reasonably argue for A. The question is not ambiguous enough to invalidate C as the best answer, but A is not a trivially wrong distractor."
  },
  "important_caveats": [
    "The pathway annotation (ECO:0000255, PROSITE-ProRule) is a computational family-level inference from the GH11 signature, not a direct experimental measurement of a pathway flux in Botrytis cinerea.",
    "The protein is also known as an ethylene-inducing elicitor in plant-pathogen interactions, but the UniProt pathway annotation focuses on its enzymatic (xylanase) activity, which is what the question targets.",
    "The sequence match is confirmed across both the current (v27) and historical (v25) UniProt records; the 222-aa benchmark sequence is identical to the canonical entry.",
    "The accession A0A384K474 was inferred by the reviewer from dataset metadata and was not provided to the evaluated model; the model must work from the raw sequence alone."
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

**Accession:** `A0A384K474` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 25. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A384K474.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:59.392996+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"33205907","source":"PubMed"}],"value":"Endo-1,4-beta-xylanase EIX2"}}],"flag":"Precursor","recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000255","id":"PRU01097","source":"PROSITE-ProRule"}],"value":"3.2.1.8"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"33205907","source":"PubMed"}],"value":"Ethylene-inducing xylanase 2"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"33205907","source":"PubMed"}],"value":"EIX21"}]}}
```

Source SHA-256: `55204b82bbe53c219df38fd17bb07b90d74cea40d24431f98ad10936f0fb3921`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A384K474.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:59.392996+00:00.  

```json
{"commentType":"PATHWAY","texts":[{"evidences":[{"evidenceCode":"ECO:0000255","id":"PRU01097","source":"PROSITE-ProRule"}],"value":"Glycan degradation; xylan degradation"}]}
```

Source SHA-256: `55204b82bbe53c219df38fd17bb07b90d74cea40d24431f98ad10936f0fb3921`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A384K474?format=txt&versions=25)  
**Locator:** `lines 1-16`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 25 / 1.  
**Retrieved:** 2026-11-02T04:25:01.435228+00:00.  

```text
ID   EIX2_BOTFB              Reviewed;         222 AA.
AC   A0A384K474;
DT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.
DT   07-NOV-2018, sequence version 1.
DT   28-JAN-2026, entry version 25.
DE   RecName: Full=Ethylene-inducing xylanase 2 {ECO:0000303|PubMed:33205907};
DE            Short=EIX21 {ECO:0000303|PubMed:33205907};
DE            EC=3.2.1.8 {ECO:0000255|PROSITE-ProRule:PRU01097};
DE   AltName: Full=Endo-1,4-beta-xylanase EIX2 {ECO:0000303|PubMed:33205907};
DE   Flags: Precursor;
GN   Name=EIX2 {ECO:0000303|PubMed:33205907}; ORFNames=BCIN_15g01600;
OS   Botryotinia fuckeliana (strain B05.10) (Noble rot fungus) (Botrytis
OS   cinerea).
OC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Leotiomycetes;
OC   Helotiales; Sclerotiniaceae; Botrytis.
OX   NCBI_TaxID=332648;
```

Source SHA-256: `f401e20e06f466f7611bd91f76c327c904201b29c424133348114ef2358dffba`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A384K474?format=txt&versions=25)  
**Locator:** `lines 70-71`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 25 / 1.  
**Retrieved:** 2026-11-02T04:25:01.435228+00:00.  

```text
CC   -!- PATHWAY: Glycan degradation; xylan degradation. {ECO:0000255|PROSITE-
CC       ProRule:PRU01097}.
```

Source SHA-256: `f401e20e06f466f7611bd91f76c327c904201b29c424133348114ef2358dffba`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 115. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
