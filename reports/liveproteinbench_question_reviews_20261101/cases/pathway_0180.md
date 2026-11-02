# pathway_0180

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `pathway`  
**Author expected answer:** **B** — Glycan degradation

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MVSFTTLLAGFVAVTGVLSAPTETVEVVDVEKRQTIGPGTGFNNGYYYSYWNDGHSGVTYTNGAGGSFSVNWANSGNFVGGKGWNPGSSSRVINFSGSYNPNGNSYLSVYGWSKNPLIEYYIVENFGTYNPSTGTTKLGEVTSDGSVYDIYRTQRVNQPSIIGTATFYQYWSVRRNHAPAARSRLRTTSNAWRNLGLTLGTLDYQIIAVEGYFSSGNANINVS

[Multiple Choices]
A. N(1)-(5-phospho-D-ribosyl)glycinamide from 5-phospho-alpha-D-ribose 1-diphosphate: step 1/2. .
B. Glycan degradation
C. L-threonine from L-aspartate: step 2/5. .
D. L-leucine degradation
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

> The exact sequence matches the UniProt entry annotated as an ethylene-inducing xylanase, with the pathway listed as glycan degradation, specifically xylan degradation. The annotation cites both a computational ProRule and experimental literature.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H5](#evidence-h5), [C6](#evidence-c6), [C8](#evidence-c8).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The N-terminal hydrophobic segment is consistent with secretion, and the sequence is compatible with an extracellular enzyme; these clues may suggest a role in degrading extracellular polymers but do not identify xylan or establish this specific pathway.


**Missing item-specific fact**

> The protein-specific identification as an endo-1,4-beta-xylanase, including its xylan-degrading activity, is needed to select glycan degradation over the other choices.


**Reason**

> The pathway choice depends on a specific enzyme-function annotation or prior experimental knowledge not supplied in the question. General sequence features do not meaningfully distinguish xylan degradation from other possible extracellular enzyme functions.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Given the protein’s documented xylanase function, glycan degradation is the matching listed pathway; the other choices concern unrelated metabolic steps.


### Important caveats

- The reviewer-only evidence matches the supplied sequence, but the author’s exact source snapshot is unknown.
- The pathway annotation cites both computational and experimental evidence; the cited primary studies were not independently reviewed here.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal hydrophobic segment is consistent with secretion, and the sequence is compatible with an extracellular enzyme; these clues may suggest a role in degrading extracellular polymers but do not identify xylan or establish this specific pathway.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific identification as an endo-1,4-beta-xylanase, including its xylan-degrading activity, is needed to select glycan degradation over the other choices.",
    "reason": "The pathway choice depends on a specific enzyme-function annotation or prior experimental knowledge not supplied in the question. General sequence features do not meaningfully distinguish xylan degradation from other possible extracellular enzyme functions."
  },
  "case_id": "pathway_0180",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H5",
      "C6",
      "C8"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry annotated as an ethylene-inducing xylanase, with the pathway listed as glycan degradation, specifically xylan degradation. The annotation cites both a computational ProRule and experimental literature."
  },
  "important_caveats": [
    "The reviewer-only evidence matches the supplied sequence, but the author’s exact source snapshot is unknown.",
    "The pathway annotation cites both computational and experimental evidence; the cited primary studies were not independently reviewed here."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Given the protein’s documented xylanase function, glycan degradation is the matching listed pathway; the other choices concern unrelated metabolic steps."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0180",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry annotated as an ethylene-inducing xylanase, with the pathway listed as glycan degradation, specifically xylan degradation. The annotation cites both a computational ProRule and experimental literature.",
    "evidence_ids": ["C4", "C5", "H5", "C6", "C8"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The N-terminal hydrophobic segment is consistent with secretion, and the sequence is compatible with an extracellular enzyme; these clues may suggest a role in degrading extracellular polymers but do not identify xylan or establish this specific pathway.",
    "missing_item_specific_fact": "The protein-specific identification as an endo-1,4-beta-xylanase, including its xylan-degrading activity, is needed to select glycan degradation over the other choices.",
    "reason": "The pathway choice depends on a specific enzyme-function annotation or prior experimental knowledge not supplied in the question. General sequence features do not meaningfully distinguish xylan degradation from other possible extracellular enzyme functions."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Given the protein’s documented xylanase function, glycan degradation is the matching listed pathway; the other choices concern unrelated metabolic steps."
  },
  "important_caveats": [
    "The reviewer-only evidence matches the supplied sequence, but the author’s exact source snapshot is unknown.",
    "The pathway annotation cites both computational and experimental evidence; the cited primary studies were not independently reviewed here."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt Q9UVF9 is explicitly annotated as 'Ethylene-inducing xylanase' (endo-1,4-beta-xylanase, EC 3.2.1.8) with PATHWAY: 'Glycan degradation; xylan degradation' (evidence C5, H5). The protein hydrolyzes β-1,4-glycosidic bonds in xylan, a glycan. The sequence matches the canonical entry (223 AA, SHA-256 confirmed). The annotation is supported by both PROSITE-ProRule (computational) and experimental PubMed evidence (16668223, 16666504).

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H5](#evidence-h5), [H1](#evidence-h1).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence exhibits three features that collectively point to a secreted glycoside hydrolase: (1) an N-terminal hydrophobic signal peptide (MVSFTTLLAGFVAVTGVLSAP) indicating extracellular secretion; (2) unusually high aromatic residue content (numerous Trp, Tyr, Phe) characteristic of carbohydrate-binding/cleaving enzymes that stack aromatic side chains against sugar rings; (3) a compact ~223-residue single-domain architecture consistent with a GH10/GH11-type β-jelly roll xylanase fold. All three distractors (purine biosynthesis step, threonine biosynthesis step, leucine degradation) describe intracellular metabolic enzymes that would lack signal peptides, would be larger multi-domain proteins, and would not display this aromatic-rich, small-domain secreted-enzyme signature. The combination of 'secreted + small + aromatic-rich β-fold' uniquely maps to extracellular glycan (polysaccharide) degradation among the four options.


**Missing item-specific fact**

> None critical. The reasoning relies on general protein-structure–function relationships (signal peptide → secretion; aromatic stacking → sugar binding; small β-sandwich → GH fold) rather than a specific database annotation.


**Reason**

> A knowledgeable biochemist can eliminate all three intracellular-metabolism distractors by noting the signal peptide and aromatic-rich small-domain architecture, and positively identify the protein as a secreted glycoside hydrolase, which corresponds to 'Glycan degradation.' The distractors are structurally incompatible with the observed sequence features.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The three distractors describe intracellular biosynthetic/catabolic enzymes (GAR synthetase, aspartokinase/homoserine dehydrogenase, branched-chain amino acid degradation enzymes) that are structurally and functionally incompatible with a 223-aa secreted aromatic-rich protein. Only 'Glycan degradation' is consistent with the observed sequence features.


### Important caveats

- The pathway annotation is supported by both computational (PROSITE-ProRule PRU01097) and experimental (PubMed 16668223, 16666504) evidence, lending it strong reliability.
- The protein also has elicitor/ethylene-inducing activity (signaling role), but its enzymatic pathway classification in UniProt is glycan degradation, which is what the question asks.
- The reasoning argument, while defensible, requires moderately specialized knowledge of glycoside hydrolase structural signatures; a model without this background might rely on sequence memorization.
- The accession Q9UVF9 was inferred from dataset metadata (reviewer-only); it was not provided to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence exhibits three features that collectively point to a secreted glycoside hydrolase: (1) an N-terminal hydrophobic signal peptide (MVSFTTLLAGFVAVTGVLSAP) indicating extracellular secretion; (2) unusually high aromatic residue content (numerous Trp, Tyr, Phe) characteristic of carbohydrate-binding/cleaving enzymes that stack aromatic side chains against sugar rings; (3) a compact ~223-residue single-domain architecture consistent with a GH10/GH11-type β-jelly roll xylanase fold. All three distractors (purine biosynthesis step, threonine biosynthesis step, leucine degradation) describe intracellular metabolic enzymes that would lack signal peptides, would be larger multi-domain proteins, and would not display this aromatic-rich, small-domain secreted-enzyme signature. The combination of 'secreted + small + aromatic-rich β-fold' uniquely maps to extracellular glycan (polysaccharide) degradation among the four options.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None critical. The reasoning relies on general protein-structure–function relationships (signal peptide → secretion; aromatic stacking → sugar binding; small β-sandwich → GH fold) rather than a specific database annotation.",
    "reason": "A knowledgeable biochemist can eliminate all three intracellular-metabolism distractors by noting the signal peptide and aromatic-rich small-domain architecture, and positively identify the protein as a secreted glycoside hydrolase, which corresponds to 'Glycan degradation.' The distractors are structurally incompatible with the observed sequence features."
  },
  "case_id": "pathway_0180",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H5",
      "H1"
    ],
    "judgment": "supported",
    "reason": "UniProt Q9UVF9 is explicitly annotated as 'Ethylene-inducing xylanase' (endo-1,4-beta-xylanase, EC 3.2.1.8) with PATHWAY: 'Glycan degradation; xylan degradation' (evidence C5, H5). The protein hydrolyzes β-1,4-glycosidic bonds in xylan, a glycan. The sequence matches the canonical entry (223 AA, SHA-256 confirmed). The annotation is supported by both PROSITE-ProRule (computational) and experimental PubMed evidence (16668223, 16666504)."
  },
  "important_caveats": [
    "The pathway annotation is supported by both computational (PROSITE-ProRule PRU01097) and experimental (PubMed 16668223, 16666504) evidence, lending it strong reliability.",
    "The protein also has elicitor/ethylene-inducing activity (signaling role), but its enzymatic pathway classification in UniProt is glycan degradation, which is what the question asks.",
    "The reasoning argument, while defensible, requires moderately specialized knowledge of glycoside hydrolase structural signatures; a model without this background might rely on sequence memorization.",
    "The accession Q9UVF9 was inferred from dataset metadata (reviewer-only); it was not provided to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The three distractors describe intracellular biosynthetic/catabolic enzymes (GAR synthetase, aspartokinase/homoserine dehydrogenase, branched-chain amino acid degradation enzymes) that are structurally and functionally incompatible with a 223-aa secreted aromatic-rich protein. Only 'Glycan degradation' is consistent with the observed sequence features."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0180",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt Q9UVF9 is explicitly annotated as 'Ethylene-inducing xylanase' (endo-1,4-beta-xylanase, EC 3.2.1.8) with PATHWAY: 'Glycan degradation; xylan degradation' (evidence C5, H5). The protein hydrolyzes β-1,4-glycosidic bonds in xylan, a glycan. The sequence matches the canonical entry (223 AA, SHA-256 confirmed). The annotation is supported by both PROSITE-ProRule (computational) and experimental PubMed evidence (16668223, 16666504).",
    "evidence_ids": ["C4", "C5", "H5", "H1"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence exhibits three features that collectively point to a secreted glycoside hydrolase: (1) an N-terminal hydrophobic signal peptide (MVSFTTLLAGFVAVTGVLSAP) indicating extracellular secretion; (2) unusually high aromatic residue content (numerous Trp, Tyr, Phe) characteristic of carbohydrate-binding/cleaving enzymes that stack aromatic side chains against sugar rings; (3) a compact ~223-residue single-domain architecture consistent with a GH10/GH11-type β-jelly roll xylanase fold. All three distractors (purine biosynthesis step, threonine biosynthesis step, leucine degradation) describe intracellular metabolic enzymes that would lack signal peptides, would be larger multi-domain proteins, and would not display this aromatic-rich, small-domain secreted-enzyme signature. The combination of 'secreted + small + aromatic-rich β-fold' uniquely maps to extracellular glycan (polysaccharide) degradation among the four options.",
    "missing_item_specific_fact": "None critical. The reasoning relies on general protein-structure–function relationships (signal peptide → secretion; aromatic stacking → sugar binding; small β-sandwich → GH fold) rather than a specific database annotation.",
    "reason": "A knowledgeable biochemist can eliminate all three intracellular-metabolism distractors by noting the signal peptide and aromatic-rich small-domain architecture, and positively identify the protein as a secreted glycoside hydrolase, which corresponds to 'Glycan degradation.' The distractors are structurally incompatible with the observed sequence features."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The three distractors describe intracellular biosynthetic/catabolic enzymes (GAR synthetase, aspartokinase/homoserine dehydrogenase, branched-chain amino acid degradation enzymes) that are structurally and functionally incompatible with a 223-aa secreted aromatic-rich protein. Only 'Glycan degradation' is consistent with the observed sequence features."
  },
  "important_caveats": [
    "The pathway annotation is supported by both computational (PROSITE-ProRule PRU01097) and experimental (PubMed 16668223, 16666504) evidence, lending it strong reliability.",
    "The protein also has elicitor/ethylene-inducing activity (signaling role), but its enzymatic pathway classification in UniProt is glycan degradation, which is what the question asks.",
    "The reasoning argument, while defensible, requires moderately specialized knowledge of glycoside hydrolase structural signatures; a model without this background might rely on sequence memorization.",
    "The accession Q9UVF9 was inferred from dataset metadata (reviewer-only); it was not provided to the evaluated model."
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

**Accession:** `Q9UVF9` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 91. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9UVF9.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:29.394840+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"10517825","source":"PubMed"}],"value":"Endo-1,4-beta-xylanase EIX"}},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"16666504","source":"PubMed"}],"value":"Ethylene biosynthesis-inducing factor"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"16666504","source":"PubMed"}],"value":"EIF"}]}],"flag":"Precursor","recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000255","id":"PRU01097","source":"PROSITE-ProRule"}],"value":"3.2.1.8"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"10517825","source":"PubMed"}],"value":"Ethylene-inducing xylanase"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"10517825","source":"PubMed"}],"value":"EIX"}]}}
```

Source SHA-256: `fc363fccbec97698792de8a94b84ee7388d03ddc4aa6d6a0260fbc7434c2a35c`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9UVF9.json)  
**Locator:** `/comments/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:29.394840+00:00.  

```json
{"commentType":"PATHWAY","texts":[{"evidences":[{"evidenceCode":"ECO:0000255","id":"PRU01097","source":"PROSITE-ProRule"},{"evidenceCode":"ECO:0000269","id":"16668223","source":"PubMed"}],"value":"Glycan degradation; xylan degradation"}]}
```

Source SHA-256: `fc363fccbec97698792de8a94b84ee7388d03ddc4aa6d6a0260fbc7434c2a35c`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9UVF9.json)  
**Locator:** `/references/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:29.394840+00:00.  

```json
{"citation":{"authors":["Furman-Matarasso N.","Cohen E.","Du Q.","Chejanovsky N.","Hanania U.","Avni A."],"citationCrossReferences":[{"database":"PubMed","id":"10517825"},{"database":"DOI","id":"10.1104/pp.121.2.345"}],"citationType":"journal article","firstPage":"345","id":"10517825","journal":"Plant Physiol.","lastPage":"351","publicationDate":"1999","title":"A point mutation in the ethylene-inducing xylanase elicitor inhibits the beta-1-4-endoxylanase activity but not the elicitation activity.","volume":"121"},"referenceNumber":1,"referencePositions":["NUCLEOTIDE SEQUENCE [MRNA]","FUNCTION","SUBCELLULAR LOCATION","MUTAGENESIS OF GLU-86 AND GLU-177"]}
```

Source SHA-256: `fc363fccbec97698792de8a94b84ee7388d03ddc4aa6d6a0260fbc7434c2a35c`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9UVF9.json)  
**Locator:** `/references/4`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:29.394840+00:00.  

```json
{"citation":{"authors":["Dean J.F.","Gross K.C.","Anderson J.D."],"citationCrossReferences":[{"database":"PubMed","id":"16668223"},{"database":"DOI","id":"10.1104/pp.96.2.571"}],"citationType":"journal article","firstPage":"571","id":"16668223","journal":"Plant Physiol.","lastPage":"576","publicationDate":"1991","title":"Ethylene Biosynthesis-Inducing Xylanase: III. Product Characterization.","volume":"96"},"referenceNumber":5,"referencePositions":["FUNCTION","CATALYTIC ACTIVITY","BIOPHYSICOCHEMICAL PROPERTIES"]}
```

Source SHA-256: `fc363fccbec97698792de8a94b84ee7388d03ddc4aa6d6a0260fbc7434c2a35c`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9UVF9?format=txt&versions=91)  
**Locator:** `lines 1-17`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 91 / 1.  
**Retrieved:** 2026-11-01T06:28:50.576003+00:00.  

```text
ID   EIX_HYPRU               Reviewed;         223 AA.
AC   Q9UVF9;
DT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.
DT   01-MAY-2000, sequence version 1.
DT   28-JAN-2026, entry version 91.
DE   RecName: Full=Ethylene-inducing xylanase {ECO:0000303|PubMed:10517825};
DE            Short=EIX {ECO:0000303|PubMed:10517825};
DE            EC=3.2.1.8 {ECO:0000255|PROSITE-ProRule:PRU01097};
DE   AltName: Full=Endo-1,4-beta-xylanase EIX {ECO:0000303|PubMed:10517825};
DE   AltName: Full=Ethylene biosynthesis-inducing factor {ECO:0000303|PubMed:16666504};
DE            Short=EIF {ECO:0000303|PubMed:16666504};
DE   Flags: Precursor;
GN   Name=EIX {ECO:0000303|PubMed:10517825};
OS   Hypocrea rufa (Trichoderma viride).
OC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Sordariomycetes;
OC   Hypocreomycetidae; Hypocreales; Hypocreaceae; Trichoderma.
OX   NCBI_TaxID=5547;
```

Source SHA-256: `58405d88f8ea2ef78dd2cc137a7fa2fd8d879e249b7706495d0b0eeb486f7eac`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9UVF9?format=txt&versions=91)  
**Locator:** `lines 173-174`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 91 / 1.  
**Retrieved:** 2026-11-01T06:28:50.576003+00:00.  

```text
CC   -!- PATHWAY: Glycan degradation; xylan degradation. {ECO:0000255|PROSITE-
CC       ProRule:PRU01097, ECO:0000269|PubMed:16668223}.
```

Source SHA-256: `58405d88f8ea2ef78dd2cc137a7fa2fd8d879e249b7706495d0b0eeb486f7eac`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 180. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
