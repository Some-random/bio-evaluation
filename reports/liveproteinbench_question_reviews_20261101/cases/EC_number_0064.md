# EC_number_0064

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `EC_number`  
**Author expected answer:** **D** — 1.2.1.11

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MASYPKKKCGVLGATGSVGQRFILLLADHPFLELHAIGASNRSAGKKYKDAVRWKQTTAMSERLSNLVLRDCRADQFSDCDLVFSGLNSDVAGEIEMEFIKAEIPVFSNAKNYRKHPLVPLVVPTVNPQHLDLIPHQRKEFGLKKGFLVCNSNCAVIGVVIPFAALQAKFGPVEEVEVFTEQAVSGAGYPGVPSMDIMDNVIPYISGEEDKLENEAQKILGSLNADATAFDEQKGLTVGATCTRVGVTDGHMAFVSLRFKNRPGPSAEEVKQAMREYQSEAQKLGCPSAPREAIKVFDEPDRPQPRLDRDISKGYTVSVGRVREAAPGSYFDLRFAALSHNTVIGAAGSSILNAEVAVIKGYI

[Multiple Choices]
A. 1.2.1.46
B. 1.1.1.195
C. 2.7.1.39
D. 1.2.1.11
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

> The supplied sequence exactly matches the UniProt entry for an Aspergillus fumigatus aspartate-semialdehyde dehydrogenase. UniProt assigns EC 1.2.1.11 and cites experimental evidence for both the enzyme annotation and its catalytic reaction. This supports choice D, while the database evidence is reviewer-only and was not available to the evaluated model.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence may permit enzyme-family inference, but the input provides no organism, pathway, substrate, or reaction context that establishes the specific catalytic activity and complete EC number.


**Missing item-specific fact**

> The protein-specific assignment to aspartate-semialdehyde dehydrogenase and its reaction corresponding to EC 1.2.1.11.


**Reason**

> Choosing among these complete EC numbers requires identifying the particular enzyme activity, a fact not stated in the input. Recognizing the sequence or using a predictor would rely on protein-specific identification rather than a biological argument supplied by the question.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The cited sequence-matched annotation supports D; the evidence provided does not support another listed option.


### Important caveats

- The annotation cites experimental evidence, but the primary papers were not independently retrieved or validated here.
- The exact source snapshot used by the question author is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence may permit enzyme-family inference, but the input provides no organism, pathway, substrate, or reaction context that establishes the specific catalytic activity and complete EC number.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific assignment to aspartate-semialdehyde dehydrogenase and its reaction corresponding to EC 1.2.1.11.",
    "reason": "Choosing among these complete EC numbers requires identifying the particular enzyme activity, a fact not stated in the input. Recognizing the sequence or using a predictor would rely on protein-specific identification rather than a biological argument supplied by the question."
  },
  "case_id": "EC_number_0064",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H2",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the UniProt entry for an Aspergillus fumigatus aspartate-semialdehyde dehydrogenase. UniProt assigns EC 1.2.1.11 and cites experimental evidence for both the enzyme annotation and its catalytic reaction. This supports choice D, while the database evidence is reviewer-only and was not available to the evaluated model."
  },
  "important_caveats": [
    "The annotation cites experimental evidence, but the primary papers were not independently retrieved or validated here.",
    "The exact source snapshot used by the question author is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The cited sequence-matched annotation supports D; the evidence provided does not support another listed option."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0064",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the UniProt entry for an Aspergillus fumigatus aspartate-semialdehyde dehydrogenase. UniProt assigns EC 1.2.1.11 and cites experimental evidence for both the enzyme annotation and its catalytic reaction. This supports choice D, while the database evidence is reviewer-only and was not available to the evaluated model.",
    "evidence_ids": ["C1", "C4", "C5", "H2", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence may permit enzyme-family inference, but the input provides no organism, pathway, substrate, or reaction context that establishes the specific catalytic activity and complete EC number.",
    "missing_item_specific_fact": "The protein-specific assignment to aspartate-semialdehyde dehydrogenase and its reaction corresponding to EC 1.2.1.11.",
    "reason": "Choosing among these complete EC numbers requires identifying the particular enzyme activity, a fact not stated in the input. Recognizing the sequence or using a predictor would rely on protein-specific identification rather than a biological argument supplied by the question."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The cited sequence-matched annotation supports D; the evidence provided does not support another listed option."
  },
  "important_caveats": [
    "The annotation cites experimental evidence, but the primary papers were not independently retrieved or validated here.",
    "The exact source snapshot used by the question author is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry Q4WWR8 (sequence exactly matched, 363 aa) is annotated as Aspartate-semialdehyde dehydrogenase, EC 1.2.1.11, with experimental evidence (ECO:0000269) from PubMed:28045392 (X-ray crystallography, PDB 5JW6) and PubMed:29608391 (enzymatic assay). The catalytic reaction (L-aspartate 4-semialdehyde + phosphate + NADP+ = 4-phospho-L-aspartate + NADPH + H+) is experimentally confirmed. Both current and archived (entry v118) records agree.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C7](#evidence-c7), [H2](#evidence-h2), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Three reasoning steps distinguish the answer: (1) The N-terminal Rossmann-fold motif 'GVLGATGSVGQ' (GxGxxG) identifies the protein as an NAD(P)-binding oxidoreductase, eliminating choice C (EC 2.7.1.39, a phosphotransferase). (2) The catalytic cysteine pair 'CNSNCA' (Cys-Asn-Ser-Asn-Cys) embedded in the sequence 'FLVCNSNCAVIG' is the hallmark catalytic dyad of aldehyde dehydrogenases, indicating an aldehyde/oxo-group substrate (EC 1.2.1.x), which eliminates choice B (EC 1.1.1.195, acting on CH-OH group). (3) The specific CNSNCA catalytic arrangement is a well-documented active-site signature unique to aspartate-semialdehyde dehydrogenase (EC 1.2.1.11) within the EC 1.2.1.x class; other EC 1.2.1.x enzymes (e.g., EC 1.2.1.46) employ different catalytic residue arrangements. Together, these sequence features support choosing D over A.


**Missing item-specific fact**

> None strictly missing. The CNSNCA motif recognition is specialized but constitutes well-established catalytic-mechanism biochemistry rather than an opaque database annotation.


**Reason**

> The sequence contains identifiable structural and catalytic motifs (Rossmann fold, catalytic Cys dyad CNSNCA) that allow a knowledgeable biochemist to narrow from four EC numbers to the correct one through general enzyme-mechanism reasoning, without needing to recall the specific UniProt entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four choices span three different EC top-level classes (1.1.1.x, 1.2.1.x, 2.7.1.x), and within EC 1.2.1.x the CNSNCA motif is specific to ASADH. No other option is defensible given the sequence features.


### Important caveats

- The CNSNCA catalytic-motif recognition is specialized biochemistry; a model without training on ASADH active-site architecture may struggle to distinguish D from A (both EC 1.2.1.x).
- The reviewer evidence is experimental (X-ray crystallography and enzymatic assays), strengthening the annotation, but this evidence was not available to the evaluated model.
- The exact identity of EC 1.2.1.46 (choice A) was not independently verified here; however, the CNSNCA motif is not a general feature of all EC 1.2.1.x enzymes, supporting the discrimination.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Three reasoning steps distinguish the answer: (1) The N-terminal Rossmann-fold motif 'GVLGATGSVGQ' (GxGxxG) identifies the protein as an NAD(P)-binding oxidoreductase, eliminating choice C (EC 2.7.1.39, a phosphotransferase). (2) The catalytic cysteine pair 'CNSNCA' (Cys-Asn-Ser-Asn-Cys) embedded in the sequence 'FLVCNSNCAVIG' is the hallmark catalytic dyad of aldehyde dehydrogenases, indicating an aldehyde/oxo-group substrate (EC 1.2.1.x), which eliminates choice B (EC 1.1.1.195, acting on CH-OH group). (3) The specific CNSNCA catalytic arrangement is a well-documented active-site signature unique to aspartate-semialdehyde dehydrogenase (EC 1.2.1.11) within the EC 1.2.1.x class; other EC 1.2.1.x enzymes (e.g., EC 1.2.1.46) employ different catalytic residue arrangements. Together, these sequence features support choosing D over A.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None strictly missing. The CNSNCA motif recognition is specialized but constitutes well-established catalytic-mechanism biochemistry rather than an opaque database annotation.",
    "reason": "The sequence contains identifiable structural and catalytic motifs (Rossmann fold, catalytic Cys dyad CNSNCA) that allow a knowledgeable biochemist to narrow from four EC numbers to the correct one through general enzyme-mechanism reasoning, without needing to recall the specific UniProt entry."
  },
  "case_id": "EC_number_0064",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C7",
      "H2",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "UniProt entry Q4WWR8 (sequence exactly matched, 363 aa) is annotated as Aspartate-semialdehyde dehydrogenase, EC 1.2.1.11, with experimental evidence (ECO:0000269) from PubMed:28045392 (X-ray crystallography, PDB 5JW6) and PubMed:29608391 (enzymatic assay). The catalytic reaction (L-aspartate 4-semialdehyde + phosphate + NADP+ = 4-phospho-L-aspartate + NADPH + H+) is experimentally confirmed. Both current and archived (entry v118) records agree."
  },
  "important_caveats": [
    "The CNSNCA catalytic-motif recognition is specialized biochemistry; a model without training on ASADH active-site architecture may struggle to distinguish D from A (both EC 1.2.1.x).",
    "The reviewer evidence is experimental (X-ray crystallography and enzymatic assays), strengthening the annotation, but this evidence was not available to the evaluated model.",
    "The exact identity of EC 1.2.1.46 (choice A) was not independently verified here; however, the CNSNCA motif is not a general feature of all EC 1.2.1.x enzymes, supporting the discrimination."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices span three different EC top-level classes (1.1.1.x, 1.2.1.x, 2.7.1.x), and within EC 1.2.1.x the CNSNCA motif is specific to ASADH. No other option is defensible given the sequence features."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0064",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry Q4WWR8 (sequence exactly matched, 363 aa) is annotated as Aspartate-semialdehyde dehydrogenase, EC 1.2.1.11, with experimental evidence (ECO:0000269) from PubMed:28045392 (X-ray crystallography, PDB 5JW6) and PubMed:29608391 (enzymatic assay). The catalytic reaction (L-aspartate 4-semialdehyde + phosphate + NADP+ = 4-phospho-L-aspartate + NADPH + H+) is experimentally confirmed. Both current and archived (entry v118) records agree.",
    "evidence_ids": ["C1", "C4", "C5", "C7", "H2", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Three reasoning steps distinguish the answer: (1) The N-terminal Rossmann-fold motif 'GVLGATGSVGQ' (GxGxxG) identifies the protein as an NAD(P)-binding oxidoreductase, eliminating choice C (EC 2.7.1.39, a phosphotransferase). (2) The catalytic cysteine pair 'CNSNCA' (Cys-Asn-Ser-Asn-Cys) embedded in the sequence 'FLVCNSNCAVIG' is the hallmark catalytic dyad of aldehyde dehydrogenases, indicating an aldehyde/oxo-group substrate (EC 1.2.1.x), which eliminates choice B (EC 1.1.1.195, acting on CH-OH group). (3) The specific CNSNCA catalytic arrangement is a well-documented active-site signature unique to aspartate-semialdehyde dehydrogenase (EC 1.2.1.11) within the EC 1.2.1.x class; other EC 1.2.1.x enzymes (e.g., EC 1.2.1.46) employ different catalytic residue arrangements. Together, these sequence features support choosing D over A.",
    "missing_item_specific_fact": "None strictly missing. The CNSNCA motif recognition is specialized but constitutes well-established catalytic-mechanism biochemistry rather than an opaque database annotation.",
    "reason": "The sequence contains identifiable structural and catalytic motifs (Rossmann fold, catalytic Cys dyad CNSNCA) that allow a knowledgeable biochemist to narrow from four EC numbers to the correct one through general enzyme-mechanism reasoning, without needing to recall the specific UniProt entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices span three different EC top-level classes (1.1.1.x, 1.2.1.x, 2.7.1.x), and within EC 1.2.1.x the CNSNCA motif is specific to ASADH. No other option is defensible given the sequence features."
  },
  "important_caveats": [
    "The CNSNCA catalytic-motif recognition is specialized biochemistry; a model without training on ASADH active-site architecture may struggle to distinguish D from A (both EC 1.2.1.x).",
    "The reviewer evidence is experimental (X-ray crystallography and enzymatic assays), strengthening the annotation, but this evidence was not available to the evaluated model.",
    "The exact identity of EC 1.2.1.46 (choice A) was not independently verified here; however, the CNSNCA motif is not a general feature of all EC 1.2.1.x enzymes, supporting the discrimination."
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

**Accession:** `Q4WWR8` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 118. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WWR8.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:55.999038+00:00.  

```json
"Q4WWR8"
```

Source SHA-256: `28ec07124002a977d699617a66669087fd52133733f4ac2a92b841504b5fe5c9`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WWR8.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:55.999038+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"28045392","source":"PubMed"}],"value":"AfASADH"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"28045392","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"29608391","source":"PubMed"}],"value":"1.2.1.11"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Aspartate-semialdehyde dehydrogenase"}}}
```

Source SHA-256: `28ec07124002a977d699617a66669087fd52133733f4ac2a92b841504b5fe5c9`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WWR8.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:55.999038+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"right-to-left","evidences":[{"evidenceCode":"ECO:0000269","id":"28045392","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"29608391","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:24286"}}],"reaction":{"ecNumber":"1.2.1.11","evidences":[{"evidenceCode":"ECO:0000269","id":"28045392","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"29608391","source":"PubMed"}],"name":"L-aspartate 4-semialdehyde + phosphate + NADP(+) = 4-phospho-L-aspartate + NADPH + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:24284"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:43474"},{"database":"ChEBI","id":"CHEBI:57535"},{"database":"ChEBI","id":"CHEBI:57783"},{"database":"ChEBI","id":"CHEBI:58349"},{"database":"ChEBI","id":"CHEBI:537519"}]}}
```

Source SHA-256: `28ec07124002a977d699617a66669087fd52133733f4ac2a92b841504b5fe5c9`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WWR8.json)  
**Locator:** `/references/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:55.999038+00:00.  

```json
{"citation":{"authors":["Dahal G.P.","Viola R.E."],"citationCrossReferences":[{"database":"PubMed","id":"28045392"},{"database":"DOI","id":"10.1107/s2053230x16020070"}],"citationType":"journal article","firstPage":"36","id":"28045392","journal":"Acta Crystallogr. F","lastPage":"44","publicationDate":"2017","title":"Structure of a fungal form of aspartate-semialdehyde dehydrogenase from Aspergillus fumigatus.","volume":"73"},"evidences":[{"evidenceCode":"ECO:0007744","id":"5JW6","source":"PDB"}],"referenceNumber":4,"referencePositions":["X-RAY CRYSTALLOGRAPHY (2.39 ANGSTROMS)","FUNCTION","CATALYTIC ACTIVITY","BIOPHYSICOCHEMICAL PROPERTIES","PATHWAY","SUBUNIT"]}
```

Source SHA-256: `28ec07124002a977d699617a66669087fd52133733f4ac2a92b841504b5fe5c9`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q4WWR8?format=txt&versions=118)  
**Locator:** `lines 6-8`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 118 / 1.  
**Retrieved:** 2026-11-02T04:31:00.563757+00:00.  

```text
DE   RecName: Full=Aspartate-semialdehyde dehydrogenase {ECO:0000305};
DE            EC=1.2.1.11 {ECO:0000269|PubMed:28045392, ECO:0000269|PubMed:29608391};
DE   AltName: Full=AfASADH {ECO:0000303|PubMed:28045392};
```

Source SHA-256: `048d52ae97c993889e1431497fcaeb51109d4ebcaca7f00814be073cab21ee35`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q4WWR8?format=txt&versions=118)  
**Locator:** `lines 57-64`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 118 / 1.  
**Retrieved:** 2026-11-02T04:31:00.563757+00:00.  

```text
RN   [4] {ECO:0007744|PDB:5JW6}
RP   X-RAY CRYSTALLOGRAPHY (2.39 ANGSTROMS), FUNCTION, CATALYTIC ACTIVITY,
RP   BIOPHYSICOCHEMICAL PROPERTIES, PATHWAY, AND SUBUNIT.
RX   PubMed=28045392; DOI=10.1107/s2053230x16020070;
RA   Dahal G.P., Viola R.E.;
RT   "Structure of a fungal form of aspartate-semialdehyde dehydrogenase from
RT   Aspergillus fumigatus.";
RL   Acta Crystallogr. F 73:36-44(2017).
```

Source SHA-256: `048d52ae97c993889e1431497fcaeb51109d4ebcaca7f00814be073cab21ee35`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q4WWR8?format=txt&versions=118)  
**Locator:** `lines 72-79`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 118 / 1.  
**Retrieved:** 2026-11-02T04:31:00.563757+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=L-aspartate 4-semialdehyde + phosphate + NADP(+) = 4-phospho-
CC         L-aspartate + NADPH + H(+); Xref=Rhea:RHEA:24284, ChEBI:CHEBI:15378,
CC         ChEBI:CHEBI:43474, ChEBI:CHEBI:57535, ChEBI:CHEBI:57783,
CC         ChEBI:CHEBI:58349, ChEBI:CHEBI:537519; EC=1.2.1.11;
CC         Evidence={ECO:0000269|PubMed:28045392, ECO:0000269|PubMed:29608391};
CC       PhysiologicalDirection=right-to-left; Xref=Rhea:RHEA:24286;
CC         Evidence={ECO:0000269|PubMed:28045392, ECO:0000269|PubMed:29608391};
```

Source SHA-256: `048d52ae97c993889e1431497fcaeb51109d4ebcaca7f00814be073cab21ee35`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 64. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
