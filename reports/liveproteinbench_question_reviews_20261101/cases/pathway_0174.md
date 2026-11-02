# pathway_0174

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `pathway`  
**Author expected answer:** **A** — Glycan degradation

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MRFSASLLLALTGSAAASPIRAEEEIRVYDLPISLFDDLQGLDAAMKAAGREYIGTSLTVRNDFQEQNIIRTEFGSITPENAQKWDATEPNRGQFTFGSADQHMDWARQNGKHVRCHTLVWYSQLPGWVSNSGFNNATLQQVMQNHINQVMGRYRGRCNHWDVVNEAPRLMAMRLQIGEAYIPIAFRMAAQADPSAKLYYNDYNLEYLGPKVEGAARIVRLVKQYGARIDGVGYQAHLVTEPTPTQSTPTPSEEDLIKALRITADLGVDVAYTEIDIRMRTPSNAQKLQQLADAYYRVARSCMKVPRCVGMTIWGVTDRYSWVPNTFRGEGDALLWDSNYQRKAAYNAFLRGIQEPVN

[Multiple Choices]
A. Glycan degradation
B. L-cystathionine from O-succinyl-L-homoserine: step 1/1. .
C. Cell wall degradation
D. L-histidine biosynthesis
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

> The exact sequence matches a UniProt entry annotated as endo-1,4-beta-xylanase B, with the pathway listed as glycan degradation (xylan degradation). The annotation cites experimental evidence, though the underlying paper was not independently reviewed here.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The N-terminal sequence is consistent with a secretion signal, which makes an extracellular degradative enzyme plausible and weighs against the biosynthetic choices. It does not identify the substrate or distinguish glycan degradation from cell wall degradation.


**Missing item-specific fact**

> The protein-specific functional identification as a xylanase and its xylan-degradation activity are needed to select the keyed pathway.


**Reason**

> The input sequence and choices alone offer no reliable way to infer this specific enzyme activity. The decisive evidence is protein-specific annotation or experimental characterization, not general sequence reasoning.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "C"
]
```

> Xylan is a glycan and a component of plant cell walls, so a xylanase can defensibly be described as involved in both glycan degradation and cell wall degradation. The cited annotation supports A specifically, but the broad option wording does not clearly exclude C.


### Important caveats

- The annotation evidence applies to an exact sequence match; it identifies the source record as Humicola insolens endo-1,4-beta-xylanase B.
- Reviewer-only database evidence supports the key but was not supplied to the evaluated model.
- The cited publication is associated with experimental annotation, but its results were not independently assessed here.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal sequence is consistent with a secretion signal, which makes an extracellular degradative enzyme plausible and weighs against the biosynthetic choices. It does not identify the substrate or distinguish glycan degradation from cell wall degradation.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific functional identification as a xylanase and its xylan-degradation activity are needed to select the keyed pathway.",
    "reason": "The input sequence and choices alone offer no reliable way to infer this specific enzyme activity. The decisive evidence is protein-specific annotation or experimental characterization, not general sequence reasoning."
  },
  "case_id": "pathway_0174",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry annotated as endo-1,4-beta-xylanase B, with the pathway listed as glycan degradation (xylan degradation). The annotation cites experimental evidence, though the underlying paper was not independently reviewed here."
  },
  "important_caveats": [
    "The annotation evidence applies to an exact sequence match; it identifies the source record as Humicola insolens endo-1,4-beta-xylanase B.",
    "Reviewer-only database evidence supports the key but was not supplied to the evaluated model.",
    "The cited publication is associated with experimental annotation, but its results were not independently assessed here."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "C"
    ],
    "reason": "Xylan is a glycan and a component of plant cell walls, so a xylanase can defensibly be described as involved in both glycan degradation and cell wall degradation. The cited annotation supports A specifically, but the broad option wording does not clearly exclude C."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0174",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry annotated as endo-1,4-beta-xylanase B, with the pathway listed as glycan degradation (xylan degradation). The annotation cites experimental evidence, though the underlying paper was not independently reviewed here.",
    "evidence_ids": ["C4", "C5", "C6", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The N-terminal sequence is consistent with a secretion signal, which makes an extracellular degradative enzyme plausible and weighs against the biosynthetic choices. It does not identify the substrate or distinguish glycan degradation from cell wall degradation.",
    "missing_item_specific_fact": "The protein-specific functional identification as a xylanase and its xylan-degradation activity are needed to select the keyed pathway.",
    "reason": "The input sequence and choices alone offer no reliable way to infer this specific enzyme activity. The decisive evidence is protein-specific annotation or experimental characterization, not general sequence reasoning."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "C"],
    "reason": "Xylan is a glycan and a component of plant cell walls, so a xylanase can defensibly be described as involved in both glycan degradation and cell wall degradation. The cited annotation supports A specifically, but the broad option wording does not clearly exclude C."
  },
  "important_caveats": [
    "The annotation evidence applies to an exact sequence match; it identifies the source record as Humicola insolens endo-1,4-beta-xylanase B.",
    "Reviewer-only database evidence supports the key but was not supplied to the evaluated model.",
    "The cited publication is associated with experimental annotation, but its results were not independently assessed here."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry for M4MLB5 (Endo-1,4-beta-xylanase B, EC 3.2.1.8) explicitly annotates the pathway as 'Glycan degradation; xylan degradation' with experimental evidence (ECO:0000269, PubMed:23306124). The protein is a GH11 family xylanase that hydrolyzes β-1,4-glycosidic bonds in xylan, a glycan. This directly supports Choice A. While xylan is a plant cell wall component (making C superficially plausible), the standard pathway classification for a glycoside hydrolase acting on a polysaccharide is 'Glycan degradation' (KEGG map00500), not 'Cell wall degradation.'

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H1](#evidence-h1), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains hallmarks of a GH11 family xylanase: an N-terminal signal peptide (MRFSASLLLALTGSAAASPIRA) indicating a secreted degradative enzyme, and the conserved 'RITAD' catalytic motif (…LRITADLGVDVAYTEIDIRMRTPSNAQKLQQLADAYYRVARSCMKVPRCVGMTIWGVTDRYSWVPNTFRGEGDALLWDSNYQRKAAYNAFLRGIQEPVN) characteristic of glycoside hydrolase family 11. A GH11 enzyme hydrolyzes β-1,4-glycosidic bonds in xylan (a glycan), so its direct biochemical pathway is glycan degradation. Options B and D (amino acid biosynthesis) are eliminable from the secreted-hydrolase character. The distinction between A and C rests on the fact that the enzyme's specific catalytic activity (EC 3.2.1.8, glycosyl bond hydrolysis) defines a glycan-degradation pathway, whereas 'cell wall degradation' is a broader ecological process involving many enzyme classes.


**Missing item-specific fact**

> None strictly required; however, the A-vs-C distinction partly relies on familiarity with pathway classification conventions (KEGG/UniProt place xylanases under 'Glycan degradation' rather than a 'Cell wall degradation' category).


**Reason**

> A model with general knowledge of glycoside hydrolase families, signal peptides, and pathway taxonomy can reason from the sequence motifs to identify this as a xylanase and assign it to glycan degradation. The distractors B and D are clearly eliminable. The A-vs-C distinction is somewhat subtle but defensible via the enzyme's direct catalytic mechanism (glycosidic bond hydrolysis = glycan degradation).


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "C"
]
```

> Xylan is a major hemicellulose component of plant cell walls, so one could argue a xylanase participates in 'cell wall degradation.' However, in standard pathway databases (KEGG, UniProt), the pathway for EC 3.2.1.8 is classified under 'Glycan degradation' (map00500), not under a 'cell wall degradation' heading. The expected answer A aligns with the canonical annotation, and C is a plausible but non-standard distractor.


### Important caveats

- The pathway annotation is supported by experimental evidence (PubMed:23306124, characterization of three thermophilic xylanases from H. insolens Y1).
- The sequence match is exact (SHA-256 confirmed) to UniProt M4MLB5, entry XYNB_HUMIN.
- The distinction between 'Glycan degradation' and 'Cell wall degradation' depends partly on pathway classification conventions rather than purely on the enzyme's biochemistry, introducing mild ambiguity.
- Reviewer-only evidence confirms the key but was not available to the evaluated model; the model must rely on sequence-based inference and general biological knowledge.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains hallmarks of a GH11 family xylanase: an N-terminal signal peptide (MRFSASLLLALTGSAAASPIRA) indicating a secreted degradative enzyme, and the conserved 'RITAD' catalytic motif (…LRITADLGVDVAYTEIDIRMRTPSNAQKLQQLADAYYRVARSCMKVPRCVGMTIWGVTDRYSWVPNTFRGEGDALLWDSNYQRKAAYNAFLRGIQEPVN) characteristic of glycoside hydrolase family 11. A GH11 enzyme hydrolyzes β-1,4-glycosidic bonds in xylan (a glycan), so its direct biochemical pathway is glycan degradation. Options B and D (amino acid biosynthesis) are eliminable from the secreted-hydrolase character. The distinction between A and C rests on the fact that the enzyme's specific catalytic activity (EC 3.2.1.8, glycosyl bond hydrolysis) defines a glycan-degradation pathway, whereas 'cell wall degradation' is a broader ecological process involving many enzyme classes.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None strictly required; however, the A-vs-C distinction partly relies on familiarity with pathway classification conventions (KEGG/UniProt place xylanases under 'Glycan degradation' rather than a 'Cell wall degradation' category).",
    "reason": "A model with general knowledge of glycoside hydrolase families, signal peptides, and pathway taxonomy can reason from the sequence motifs to identify this as a xylanase and assign it to glycan degradation. The distractors B and D are clearly eliminable. The A-vs-C distinction is somewhat subtle but defensible via the enzyme's direct catalytic mechanism (glycosidic bond hydrolysis = glycan degradation)."
  },
  "case_id": "pathway_0174",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H1",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry for M4MLB5 (Endo-1,4-beta-xylanase B, EC 3.2.1.8) explicitly annotates the pathway as 'Glycan degradation; xylan degradation' with experimental evidence (ECO:0000269, PubMed:23306124). The protein is a GH11 family xylanase that hydrolyzes β-1,4-glycosidic bonds in xylan, a glycan. This directly supports Choice A. While xylan is a plant cell wall component (making C superficially plausible), the standard pathway classification for a glycoside hydrolase acting on a polysaccharide is 'Glycan degradation' (KEGG map00500), not 'Cell wall degradation.'"
  },
  "important_caveats": [
    "The pathway annotation is supported by experimental evidence (PubMed:23306124, characterization of three thermophilic xylanases from H. insolens Y1).",
    "The sequence match is exact (SHA-256 confirmed) to UniProt M4MLB5, entry XYNB_HUMIN.",
    "The distinction between 'Glycan degradation' and 'Cell wall degradation' depends partly on pathway classification conventions rather than purely on the enzyme's biochemistry, introducing mild ambiguity.",
    "Reviewer-only evidence confirms the key but was not available to the evaluated model; the model must rely on sequence-based inference and general biological knowledge."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "C"
    ],
    "reason": "Xylan is a major hemicellulose component of plant cell walls, so one could argue a xylanase participates in 'cell wall degradation.' However, in standard pathway databases (KEGG, UniProt), the pathway for EC 3.2.1.8 is classified under 'Glycan degradation' (map00500), not under a 'cell wall degradation' heading. The expected answer A aligns with the canonical annotation, and C is a plausible but non-standard distractor."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0174",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry for M4MLB5 (Endo-1,4-beta-xylanase B, EC 3.2.1.8) explicitly annotates the pathway as 'Glycan degradation; xylan degradation' with experimental evidence (ECO:0000269, PubMed:23306124). The protein is a GH11 family xylanase that hydrolyzes β-1,4-glycosidic bonds in xylan, a glycan. This directly supports Choice A. While xylan is a plant cell wall component (making C superficially plausible), the standard pathway classification for a glycoside hydrolase acting on a polysaccharide is 'Glycan degradation' (KEGG map00500), not 'Cell wall degradation.'",
    "evidence_ids": ["C4", "C5", "H1", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains hallmarks of a GH11 family xylanase: an N-terminal signal peptide (MRFSASLLLALTGSAAASPIRA) indicating a secreted degradative enzyme, and the conserved 'RITAD' catalytic motif (…LRITADLGVDVAYTEIDIRMRTPSNAQKLQQLADAYYRVARSCMKVPRCVGMTIWGVTDRYSWVPNTFRGEGDALLWDSNYQRKAAYNAFLRGIQEPVN) characteristic of glycoside hydrolase family 11. A GH11 enzyme hydrolyzes β-1,4-glycosidic bonds in xylan (a glycan), so its direct biochemical pathway is glycan degradation. Options B and D (amino acid biosynthesis) are eliminable from the secreted-hydrolase character. The distinction between A and C rests on the fact that the enzyme's specific catalytic activity (EC 3.2.1.8, glycosyl bond hydrolysis) defines a glycan-degradation pathway, whereas 'cell wall degradation' is a broader ecological process involving many enzyme classes.",
    "missing_item_specific_fact": "None strictly required; however, the A-vs-C distinction partly relies on familiarity with pathway classification conventions (KEGG/UniProt place xylanases under 'Glycan degradation' rather than a 'Cell wall degradation' category).",
    "reason": "A model with general knowledge of glycoside hydrolase families, signal peptides, and pathway taxonomy can reason from the sequence motifs to identify this as a xylanase and assign it to glycan degradation. The distractors B and D are clearly eliminable. The A-vs-C distinction is somewhat subtle but defensible via the enzyme's direct catalytic mechanism (glycosidic bond hydrolysis = glycan degradation)."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "C"],
    "reason": "Xylan is a major hemicellulose component of plant cell walls, so one could argue a xylanase participates in 'cell wall degradation.' However, in standard pathway databases (KEGG, UniProt), the pathway for EC 3.2.1.8 is classified under 'Glycan degradation' (map00500), not under a 'cell wall degradation' heading. The expected answer A aligns with the canonical annotation, and C is a plausible but non-standard distractor."
  },
  "important_caveats": [
    "The pathway annotation is supported by experimental evidence (PubMed:23306124, characterization of three thermophilic xylanases from H. insolens Y1).",
    "The sequence match is exact (SHA-256 confirmed) to UniProt M4MLB5, entry XYNB_HUMIN.",
    "The distinction between 'Glycan degradation' and 'Cell wall degradation' depends partly on pathway classification conventions rather than purely on the enzyme's biochemistry, introducing mild ambiguity.",
    "Reviewer-only evidence confirms the key but was not available to the evaluated model; the model must rely on sequence-based inference and general biological knowledge."
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

**Accession:** `M4MLB5` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 31. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/M4MLB5.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:12.159556+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"1,4-beta-D-xylan xylanohydrolase B"}}],"flag":"Precursor","recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"23306124","source":"PubMed"}],"value":"3.2.1.8"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"23306124","source":"PubMed"}],"value":"Endo-1,4-beta-xylanase B"}}}
```

Source SHA-256: `9737e107c7508ede0abc7bd8c8f14f35fc885d5000f5778fdd13b8d4054f912f`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/M4MLB5.json)  
**Locator:** `/comments/4`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:12.159556+00:00.  

```json
{"commentType":"PATHWAY","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"23306124","source":"PubMed"}],"value":"Glycan degradation; xylan degradation"}]}
```

Source SHA-256: `9737e107c7508ede0abc7bd8c8f14f35fc885d5000f5778fdd13b8d4054f912f`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/M4MLB5.json)  
**Locator:** `/references/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:12.159556+00:00.  

```json
{"citation":{"authors":["Du Y.","Shi P.","Huang H.","Zhang X.","Luo H.","Wang Y.","Yao B."],"citationCrossReferences":[{"database":"PubMed","id":"23306124"},{"database":"DOI","id":"10.1016/j.biortech.2012.12.067"}],"citationType":"journal article","firstPage":"161","id":"23306124","journal":"Bioresour. Technol.","lastPage":"167","publicationDate":"2013","title":"Characterization of three novel thermophilic xylanases from Humicola insolens Y1 with application potentials in the brewing industry.","volume":"130"},"referenceComments":[{"type":"STRAIN","value":"Y1"}],"referenceNumber":1,"referencePositions":["NUCLEOTIDE SEQUENCE [MRNA]","FUNCTION","CATALYTIC ACTIVITY","BIOPHYSICOCHEMICAL PROPERTIES","SUBSTRATE SPECIFICITY","ACTIVITY REGULATION","BIOTECHNOLOGY"]}
```

Source SHA-256: `9737e107c7508ede0abc7bd8c8f14f35fc885d5000f5778fdd13b8d4054f912f`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/M4MLB5?format=txt&versions=31)  
**Locator:** `lines 1-14`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 31 / 1.  
**Retrieved:** 2026-11-01T06:28:16.229298+00:00.  

```text
ID   XYNB_HUMIN              Reviewed;         358 AA.
AC   M4MLB5;
DT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.
DT   29-MAY-2013, sequence version 1.
DT   28-JAN-2026, entry version 31.
DE   RecName: Full=Endo-1,4-beta-xylanase B {ECO:0000303|PubMed:23306124};
DE            EC=3.2.1.8 {ECO:0000269|PubMed:23306124};
DE   AltName: Full=1,4-beta-D-xylan xylanohydrolase B {ECO:0000305};
DE   Flags: Precursor;
GN   Name=XynB {ECO:0000303|PubMed:23306124};
OS   Humicola insolens (Soft-rot fungus).
OC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Sordariomycetes;
OC   Sordariomycetidae; Sordariales; Chaetomiaceae; Mycothermus.
OX   NCBI_TaxID=85995;
```

Source SHA-256: `8a61ff0bb76d82894c8a3570170d306b45992420e142ae76129e353039c9cab6`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/M4MLB5?format=txt&versions=31)  
**Locator:** `lines 60-61`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 31 / 1.  
**Retrieved:** 2026-11-01T06:28:16.229298+00:00.  

```text
CC   -!- PATHWAY: Glycan degradation; xylan degradation.
CC       {ECO:0000269|PubMed:23306124}.
```

Source SHA-256: `8a61ff0bb76d82894c8a3570170d306b45992420e142ae76129e353039c9cab6`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 174. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
