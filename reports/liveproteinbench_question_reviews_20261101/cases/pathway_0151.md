# pathway_0151

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `pathway`  
**Author expected answer:** **B** — Alkaloid biosynthesis

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MAENQEALAEFYDKGVGVWDNLSREHMHFGYYAPGATATIGGHRASLVRLIDEALCFAEFPDDPEKKPRNMLDVGCGIGGTCLHVAKKYDIQCKGINISPEQVKIAQGLAAAQGLESKVSFDVGDALDMPYPDGAFDLVLSIHCIEHLQDKEKFIREMVRVAASGATIIILSHVHRDLSPSEQSLKPQEERVLRKIGSSVQAWFCPLSNYVSLLAPLPVEVIKIADWSRNIDPSSRLMLKVAFSVKGIVSNLMKGVQGWTAIKNVLPMKLLHKALHDGLVKFVVLTCRKSN

[Multiple Choices]
A. Bacterial outer membrane biogenesis
B. Alkaloid biosynthesis
C. Glycolipid biosynthesis
D. Cell wall degradation
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

> The supplied sequence exactly matches the UniProt sequence annotated as ajmaline N-methyltransferase from Rauvolfia serpentina. Its pathway annotation is alkaloid biosynthesis, specifically ajmaline biosynthesis, with experimental-evidence attribution to a cited study. This supports choice B, though the excerpts do not independently validate the underlying experiments.

Citations as saved: [C1](#evidence-c1), [C3](#evidence-c3), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence may suggest an enzyme in a methyltransferase family, but that alone does not identify its physiological substrate or distinguish alkaloid biosynthesis from the other listed pathways.


**Missing item-specific fact**

> The protein-specific functional annotation or experimental finding that this enzyme methylates an ajmaline-pathway substrate.


**Reason**

> The pathway assignment depends on a protein-specific function not established by the sequence and choices alone. Recognizing the exact protein or consulting its annotation would supply that missing fact.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The matched-sequence annotation supports B as the protein's pathway. The input alone does not meaningfully distinguish among the choices, but that lack of answerability does not make another option biologically supported.


### Important caveats

- Reviewer-only database and publication evidence was not supplied to the evaluated model.
- The exact author source snapshot is unknown; both a current entry and a historical entry checked here match the supplied sequence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence may suggest an enzyme in a methyltransferase family, but that alone does not identify its physiological substrate or distinguish alkaloid biosynthesis from the other listed pathways.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific functional annotation or experimental finding that this enzyme methylates an ajmaline-pathway substrate.",
    "reason": "The pathway assignment depends on a protein-specific function not established by the sequence and choices alone. Recognizing the exact protein or consulting its annotation would supply that missing fact."
  },
  "case_id": "pathway_0151",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C3",
      "C4",
      "C5",
      "C6",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the UniProt sequence annotated as ajmaline N-methyltransferase from Rauvolfia serpentina. Its pathway annotation is alkaloid biosynthesis, specifically ajmaline biosynthesis, with experimental-evidence attribution to a cited study. This supports choice B, though the excerpts do not independently validate the underlying experiments."
  },
  "important_caveats": [
    "Reviewer-only database and publication evidence was not supplied to the evaluated model.",
    "The exact author source snapshot is unknown; both a current entry and a historical entry checked here match the supplied sequence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched-sequence annotation supports B as the protein's pathway. The input alone does not meaningfully distinguish among the choices, but that lack of answerability does not make another option biologically supported."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0151",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the UniProt sequence annotated as ajmaline N-methyltransferase from Rauvolfia serpentina. Its pathway annotation is alkaloid biosynthesis, specifically ajmaline biosynthesis, with experimental-evidence attribution to a cited study. This supports choice B, though the excerpts do not independently validate the underlying experiments.",
    "evidence_ids": ["C1", "C3", "C4", "C5", "C6", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence may suggest an enzyme in a methyltransferase family, but that alone does not identify its physiological substrate or distinguish alkaloid biosynthesis from the other listed pathways.",
    "missing_item_specific_fact": "The protein-specific functional annotation or experimental finding that this enzyme methylates an ajmaline-pathway substrate.",
    "reason": "The pathway assignment depends on a protein-specific function not established by the sequence and choices alone. Recognizing the exact protein or consulting its annotation would supply that missing fact."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched-sequence annotation supports B as the protein's pathway. The input alone does not meaningfully distinguish among the choices, but that lack of answerability does not make another option biologically supported."
  },
  "important_caveats": [
    "Reviewer-only database and publication evidence was not supplied to the evaluated model.",
    "The exact author source snapshot is unknown; both a current entry and a historical entry checked here match the supplied sequence."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A0A075D654 (ANMT_RAUSE) explicitly annotates the pathway as 'Alkaloid biosynthesis; ajmaline biosynthesis' with experimental evidence (ECO:0000269, PubMed:27122470). The protein is Ajmaline N-methyltransferase (EC 2.1.1.393) from Rauvolfia serpentina, confirmed by exact sequence match (SHA256 identical, 291 AA). The pathway assignment is backed by a functional characterization paper.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence contains recognizable SAM-dependent methyltransferase motifs (GCGIGGT Rossmann-like SAM-binding motif, VHRDL motif), allowing identification as a methyltransferase. One could weakly argue that methyltransferases are more commonly associated with alkaloid biosynthesis than glycolipid biosynthesis (which primarily uses glycosyltransferases) or cell wall degradation (which uses hydrolases), and the eukaryotic character argues against bacterial outer membrane biogenesis. However, this statistical tendency does not definitively distinguish alkaloid biosynthesis from glycolipid biosynthesis, since plant methyltransferases participate in both (e.g., phospholipid N-methylation).


**Missing item-specific fact**

> The specific substrate specificity of this methyltransferase (N-methylation of ajmaline) and its assignment to the ajmaline biosynthetic pathway is an experimentally determined fact (PubMed:27122470). Without knowing the substrate, a plant methyltransferase could plausibly function in alkaloid biosynthesis, phospholipid/glycolipid methylation, or lignin biosynthesis. The organism (Rauvolfia serpentina, famous for indole alkaloids) is not provided to the model.


**Reason**

> While the methyltransferase fold is identifiable from sequence, the specific pathway assignment (alkaloid vs. glycolipid) requires knowledge of this particular enzyme's substrate and reaction, which is an item-specific experimental annotation. The general observation that methyltransferases are common in alkaloid pathways provides only a weak statistical prior, not a definitive biological argument distinguishing B from C.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Although glycolipid biosynthesis (C) involves some methyltransferase steps in plants, the distractors are sufficiently weak that the correct answer is unique once the substrate specificity is known. The methyltransferase identification does not make C equally defensible as B in a strict sense, but without the substrate information, a model relying only on sequence would struggle to confidently choose B over C.


### Important caveats

- The UniProt entry was first public in June 2025; the benchmark construction date is unknown. If the protein was not annotated before benchmark creation, the author may have relied on the underlying publication or transferred annotation.
- The organism name (Rauvolfia serpentina) is not provided to the evaluated model, removing a strong contextual clue (this plant is famous for indole alkaloid production).
- The methyltransferase identification from sequence is reliable, but the pathway-level assignment (alkaloid vs. lipid) depends on substrate specificity knowledge not derivable from primary sequence alone.
- Evidence code ECO:0000269 indicates direct experimental evidence for the pathway assignment.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains recognizable SAM-dependent methyltransferase motifs (GCGIGGT Rossmann-like SAM-binding motif, VHRDL motif), allowing identification as a methyltransferase. One could weakly argue that methyltransferases are more commonly associated with alkaloid biosynthesis than glycolipid biosynthesis (which primarily uses glycosyltransferases) or cell wall degradation (which uses hydrolases), and the eukaryotic character argues against bacterial outer membrane biogenesis. However, this statistical tendency does not definitively distinguish alkaloid biosynthesis from glycolipid biosynthesis, since plant methyltransferases participate in both (e.g., phospholipid N-methylation).",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific substrate specificity of this methyltransferase (N-methylation of ajmaline) and its assignment to the ajmaline biosynthetic pathway is an experimentally determined fact (PubMed:27122470). Without knowing the substrate, a plant methyltransferase could plausibly function in alkaloid biosynthesis, phospholipid/glycolipid methylation, or lignin biosynthesis. The organism (Rauvolfia serpentina, famous for indole alkaloids) is not provided to the model.",
    "reason": "While the methyltransferase fold is identifiable from sequence, the specific pathway assignment (alkaloid vs. glycolipid) requires knowledge of this particular enzyme's substrate and reaction, which is an item-specific experimental annotation. The general observation that methyltransferases are common in alkaloid pathways provides only a weak statistical prior, not a definitive biological argument distinguishing B from C."
  },
  "case_id": "pathway_0151",
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
    "reason": "The UniProt entry A0A075D654 (ANMT_RAUSE) explicitly annotates the pathway as 'Alkaloid biosynthesis; ajmaline biosynthesis' with experimental evidence (ECO:0000269, PubMed:27122470). The protein is Ajmaline N-methyltransferase (EC 2.1.1.393) from Rauvolfia serpentina, confirmed by exact sequence match (SHA256 identical, 291 AA). The pathway assignment is backed by a functional characterization paper."
  },
  "important_caveats": [
    "The UniProt entry was first public in June 2025; the benchmark construction date is unknown. If the protein was not annotated before benchmark creation, the author may have relied on the underlying publication or transferred annotation.",
    "The organism name (Rauvolfia serpentina) is not provided to the evaluated model, removing a strong contextual clue (this plant is famous for indole alkaloid production).",
    "The methyltransferase identification from sequence is reliable, but the pathway-level assignment (alkaloid vs. lipid) depends on substrate specificity knowledge not derivable from primary sequence alone.",
    "Evidence code ECO:0000269 indicates direct experimental evidence for the pathway assignment."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although glycolipid biosynthesis (C) involves some methyltransferase steps in plants, the distractors are sufficiently weak that the correct answer is unique once the substrate specificity is known. The methyltransferase identification does not make C equally defensible as B in a strict sense, but without the substrate information, a model relying only on sequence would struggle to confidently choose B over C."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0151",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A0A075D654 (ANMT_RAUSE) explicitly annotates the pathway as 'Alkaloid biosynthesis; ajmaline biosynthesis' with experimental evidence (ECO:0000269, PubMed:27122470). The protein is Ajmaline N-methyltransferase (EC 2.1.1.393) from Rauvolfia serpentina, confirmed by exact sequence match (SHA256 identical, 291 AA). The pathway assignment is backed by a functional characterization paper.",
    "evidence_ids": ["C4", "C5", "C6", "H1", "H2", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence contains recognizable SAM-dependent methyltransferase motifs (GCGIGGT Rossmann-like SAM-binding motif, VHRDL motif), allowing identification as a methyltransferase. One could weakly argue that methyltransferases are more commonly associated with alkaloid biosynthesis than glycolipid biosynthesis (which primarily uses glycosyltransferases) or cell wall degradation (which uses hydrolases), and the eukaryotic character argues against bacterial outer membrane biogenesis. However, this statistical tendency does not definitively distinguish alkaloid biosynthesis from glycolipid biosynthesis, since plant methyltransferases participate in both (e.g., phospholipid N-methylation).",
    "missing_item_specific_fact": "The specific substrate specificity of this methyltransferase (N-methylation of ajmaline) and its assignment to the ajmaline biosynthetic pathway is an experimentally determined fact (PubMed:27122470). Without knowing the substrate, a plant methyltransferase could plausibly function in alkaloid biosynthesis, phospholipid/glycolipid methylation, or lignin biosynthesis. The organism (Rauvolfia serpentina, famous for indole alkaloids) is not provided to the model.",
    "reason": "While the methyltransferase fold is identifiable from sequence, the specific pathway assignment (alkaloid vs. glycolipid) requires knowledge of this particular enzyme's substrate and reaction, which is an item-specific experimental annotation. The general observation that methyltransferases are common in alkaloid pathways provides only a weak statistical prior, not a definitive biological argument distinguishing B from C."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although glycolipid biosynthesis (C) involves some methyltransferase steps in plants, the distractors are sufficiently weak that the correct answer is unique once the substrate specificity is known. The methyltransferase identification does not make C equally defensible as B in a strict sense, but without the substrate information, a model relying only on sequence would struggle to confidently choose B over C."
  },
  "important_caveats": [
    "The UniProt entry was first public in June 2025; the benchmark construction date is unknown. If the protein was not annotated before benchmark creation, the author may have relied on the underlying publication or transferred annotation.",
    "The organism name (Rauvolfia serpentina) is not provided to the evaluated model, removing a strong contextual clue (this plant is famous for indole alkaloid production).",
    "The methyltransferase identification from sequence is reliable, but the pathway-level assignment (alkaloid vs. lipid) depends on substrate specificity knowledge not derivable from primary sequence alone.",
    "Evidence code ECO:0000269 indicates direct experimental evidence for the pathway assignment."
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

**Accession:** `A0A075D654` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 32. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A075D654.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:36.410454+00:00.  

```json
"A0A075D654"
```

Source SHA-256: `124df2385940e2e796356809e8af1e8fa6c895c01f7e6fd2fc1c87d9a5dbcf22`.

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A075D654.json)  
**Locator:** `/organism`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:36.410454+00:00.  

```json
{"commonName":"Serpentine wood","lineage":["Eukaryota","Viridiplantae","Streptophyta","Embryophyta","Tracheophyta","Spermatophyta","Magnoliopsida","eudicotyledons","Gunneridae","Pentapetalae","asterids","lamiids","Gentianales","Apocynaceae","Rauvolfioideae","Vinceae","Rauvolfiinae","Rauvolfia"],"scientificName":"Rauvolfia serpentina","synonyms":["Ophioxylon serpentinum"],"taxonId":4060}
```

Source SHA-256: `124df2385940e2e796356809e8af1e8fa6c895c01f7e6fd2fc1c87d9a5dbcf22`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A075D654.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:36.410454+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000312","id":"AHH02777.1","source":"EMBL"}],"value":"Gamma-tocopherol-like methyltransferase ANMT"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"27122470","source":"PubMed"}],"value":"2.1.1.393"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"27122470","source":"PubMed"}],"value":"Ajmaline N-methyltransferase"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"27122470","source":"PubMed"}],"value":"RsANMT"}]}}
```

Source SHA-256: `124df2385940e2e796356809e8af1e8fa6c895c01f7e6fd2fc1c87d9a5dbcf22`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A075D654.json)  
**Locator:** `/comments/4`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:36.410454+00:00.  

```json
{"commentType":"PATHWAY","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"27122470","source":"PubMed"}],"value":"Alkaloid biosynthesis; ajmaline biosynthesis"}]}
```

Source SHA-256: `124df2385940e2e796356809e8af1e8fa6c895c01f7e6fd2fc1c87d9a5dbcf22`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A075D654.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:36.410454+00:00.  

```json
{"citation":{"authors":["Cazares-Flores P.","Levac D.","De Luca V."],"citationCrossReferences":[{"database":"PubMed","id":"27122470"},{"database":"DOI","id":"10.1111/tpj.13186"}],"citationType":"journal article","firstPage":"335","id":"27122470","journal":"Plant J.","lastPage":"342","publicationDate":"2016","title":"Rauvolfia serpentina N-methyltransferases involved in ajmaline and Nbeta -methylajmaline biosynthesis belong to a gene family derived from gamma-tocopherol C-methyltransferase.","volume":"87"},"referenceNumber":2,"referencePositions":["FUNCTION","CATALYTIC ACTIVITY","BIOPHYSICOCHEMICAL PROPERTIES","PATHWAY","TISSUE SPECIFICITY"]}
```

Source SHA-256: `124df2385940e2e796356809e8af1e8fa6c895c01f7e6fd2fc1c87d9a5dbcf22`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A075D654?format=txt&versions=32)  
**Locator:** `lines 1-17`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 32 / 1.  
**Retrieved:** 2026-11-01T06:27:15.419855+00:00.  

```text
ID   ANMT_RAUSE              Reviewed;         291 AA.
AC   A0A075D654;
DT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.
DT   29-OCT-2014, sequence version 1.
DT   28-JAN-2026, entry version 32.
DE   RecName: Full=Ajmaline N-methyltransferase {ECO:0000303|PubMed:27122470};
DE            Short=RsANMT {ECO:0000303|PubMed:27122470};
DE            EC=2.1.1.393 {ECO:0000269|PubMed:27122470};
DE   AltName: Full=Gamma-tocopherol-like methyltransferase ANMT {ECO:0000312|EMBL:AHH02777.1};
GN   Name=ANMT {ECO:0000303|PubMed:27122470};
GN   Synonyms=Rs820 {ECO:0000312|EMBL:AHH02777.1};
OS   Rauvolfia serpentina (Serpentine wood) (Ophioxylon serpentinum).
OC   Eukaryota; Viridiplantae; Streptophyta; Embryophyta; Tracheophyta;
OC   Spermatophyta; Magnoliopsida; eudicotyledons; Gunneridae; Pentapetalae;
OC   asterids; lamiids; Gentianales; Apocynaceae; Rauvolfioideae; Vinceae;
OC   Rauvolfiinae; Rauvolfia.
OX   NCBI_TaxID=4060;
```

Source SHA-256: `15b1ec6a186650c4d2bc97d8a1e63645a9b1f63fb122c34f7abac877a8922eb4`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A075D654?format=txt&versions=32)  
**Locator:** `lines 26-34`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 32 / 1.  
**Retrieved:** 2026-11-01T06:27:15.419855+00:00.  

```text
RN   [2]
RP   FUNCTION, CATALYTIC ACTIVITY, BIOPHYSICOCHEMICAL PROPERTIES, PATHWAY, AND
RP   TISSUE SPECIFICITY.
RX   PubMed=27122470; DOI=10.1111/tpj.13186;
RA   Cazares-Flores P., Levac D., De Luca V.;
RT   "Rauvolfia serpentina N-methyltransferases involved in ajmaline and Nbeta
RT   -methylajmaline biosynthesis belong to a gene family derived from gamma-
RT   tocopherol C-methyltransferase.";
RL   Plant J. 87:335-342(2016).
```

Source SHA-256: `15b1ec6a186650c4d2bc97d8a1e63645a9b1f63fb122c34f7abac877a8922eb4`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A075D654?format=txt&versions=32)  
**Locator:** `lines 74-75`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 32 / 1.  
**Retrieved:** 2026-11-01T06:27:15.419855+00:00.  

```text
CC   -!- PATHWAY: Alkaloid biosynthesis; ajmaline biosynthesis.
CC       {ECO:0000269|PubMed:27122470}.
```

Source SHA-256: `15b1ec6a186650c4d2bc97d8a1e63645a9b1f63fb122c34f7abac877a8922eb4`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 151. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
