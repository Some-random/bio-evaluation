# catalytic_activity_0148

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `catalytic_activity`  
**Author expected answer:** **D** — 4&#x27;-phosphooxetanocin A + H2O = oxetanocin A + phosphate

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MSSLLDIIYQLRQVPRWDGSFQFEKEDVSQHSFSVIAISHILCELKETLEGKKINKEKLLLYALYHDVTEVVSTHIISPVKKNSILKDPFNAFREQIKNSLFDNLPITLSDTLSTILNNNDLEIQEIVEHADHVDAYCKSCIEVHRGNKDFISIQRSLGDKLDNLTKEYPYLKEFQNLFLKDFPLENKNYRYLN

[Multiple Choices]
A. O-phospho-L-serine + sulfite + H(+) = L-cysteate + phosphate
B. 4-nitrobenzoyl-CoA + 6 (S)-methylmalonyl-CoA + malonyl-CoA + 6 NADPH + 12 H(+) = demethyldeoxyspectinabilin + 7 CO2 + 6 NADP(+) + 8 CoA + 5 H2O
C. O-phospho-L-homoserine + L-cysteine = L,L-cystathionine + phosphate
D. 4'-phosphooxetanocin A + H2O = oxetanocin A + phosphate
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Enzymatic Reaction Prediction, which is to identify the specific chemical reaction catalyzed by a given enzyme. This involves understanding the enzyme's function based on its amino acid sequence and then selecting the correct transformation of substrates into products from a list of possible reactions.. The inputs provided by the user for this task include:

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

> The exact sequence matches the UniProt entry annotated with this phosphatase activity. Its catalytic-activity annotation cites experimental evidence (ECO:0000269) from two publications, supporting choice D; the cited primary studies were not independently reviewed here.

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [H6](#evidence-h6).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence contains histidine/aspartate-rich regions consistent with a metal-dependent HD-domain phosphohydrolase, which could favor a phosphatase reaction over the other broad reaction types. That does not identify the specific oxetanocin substrate.


**Missing item-specific fact**

> The protein's experimentally characterized substrate specificity: that it hydrolyzes 4'-phosphooxetanocin A to oxetanocin A and phosphate.


**Reason**

> Sequence features may suggest a broad phosphohydrolase class, but the exact reaction in choice D depends on protein-specific substrate and activity information absent from the question.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The choices describe distinct reaction types, and the sequence's likely broad phosphohydrolase character is consistent with D; no other option is comparably supported by the supplied sequence.


### Important caveats

- The annotation evidence is reviewer-only and was not supplied to the evaluated model.
- The sequence match is exact, but the author’s source snapshot is unknown; the historical and current annotations both support D.
- Experimental evidence codes are reported in the database record, but the primary papers were not independently validated here.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains histidine/aspartate-rich regions consistent with a metal-dependent HD-domain phosphohydrolase, which could favor a phosphatase reaction over the other broad reaction types. That does not identify the specific oxetanocin substrate.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein's experimentally characterized substrate specificity: that it hydrolyzes 4'-phosphooxetanocin A to oxetanocin A and phosphate.",
    "reason": "Sequence features may suggest a broad phosphohydrolase class, but the exact reaction in choice D depends on protein-specific substrate and activity information absent from the question."
  },
  "case_id": "catalytic_activity_0148",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry annotated with this phosphatase activity. Its catalytic-activity annotation cites experimental evidence (ECO:0000269) from two publications, supporting choice D; the cited primary studies were not independently reviewed here."
  },
  "important_caveats": [
    "The annotation evidence is reviewer-only and was not supplied to the evaluated model.",
    "The sequence match is exact, but the author’s source snapshot is unknown; the historical and current annotations both support D.",
    "Experimental evidence codes are reported in the database record, but the primary papers were not independently validated here."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The choices describe distinct reaction types, and the sequence's likely broad phosphohydrolase character is consistent with D; no other option is comparably supported by the supplied sequence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0148",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry annotated with this phosphatase activity. Its catalytic-activity annotation cites experimental evidence (ECO:0000269) from two publications, supporting choice D; the cited primary studies were not independently reviewed here.",
    "evidence_ids": ["C1", "C5", "H6"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence contains histidine/aspartate-rich regions consistent with a metal-dependent HD-domain phosphohydrolase, which could favor a phosphatase reaction over the other broad reaction types. That does not identify the specific oxetanocin substrate.",
    "missing_item_specific_fact": "The protein's experimentally characterized substrate specificity: that it hydrolyzes 4'-phosphooxetanocin A to oxetanocin A and phosphate.",
    "reason": "Sequence features may suggest a broad phosphohydrolase class, but the exact reaction in choice D depends on protein-specific substrate and activity information absent from the question."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The choices describe distinct reaction types, and the sequence's likely broad phosphohydrolase character is consistent with D; no other option is comparably supported by the supplied sequence."
  },
  "important_caveats": [
    "The annotation evidence is reviewer-only and was not supplied to the evaluated model.",
    "The sequence match is exact, but the author’s source snapshot is unknown; the historical and current annotations both support D.",
    "Experimental evidence codes are reported in the database record, but the primary papers were not independently validated here."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The protein sequence exactly matches UniProt O24769 (OXSA_PRIMG, 194 AA, SHA256 matched). The entry is experimentally annotated as '4'-phosphooxetanocin A phosphatase' (EC 3.1.3.112) with the catalytic reaction '4'-phosphooxetanocin A + H2O = oxetanocin A + phosphate' (RHEA:81367). This annotation carries ECO:0000269 (direct experimental evidence) from PubMed:27849620 and PubMed:28346939, and is corroborated by X-ray crystallography structures (PDB 5TK6–5TKA) in complexes with oxetanocin A and its phosphorylated forms. The expected answer D matches the annotated reaction verbatim.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C7](#evidence-c7), [H1](#evidence-h1), [H2](#evidence-h2), [H5](#evidence-h5), [H6](#evidence-h6).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The protein is only 194 amino acids, which could eliminate Choice B (a multi-subunit polyketide synthase reaction requiring a very large enzyme). However, distinguishing among A (phosphatase on O-phospho-L-serine), C (cystathionine gamma-synthase), and D (phosphatase on 4'-phosphooxetanocin A) from the raw sequence alone is not feasible through general reasoning. The HD-domain phosphohydrolase motif is extremely difficult to identify from a 194-residue sequence without structural or database context, and even recognizing a generic phosphatase activity would not predict the highly obscure substrate 4'-phosphooxetanocin A (a nucleoside-analog antibiotic natural product) over more common phosphoamino-acid substrates.


**Missing item-specific fact**

> The specific identity of this protein as OxsA (HD-domain phosphohydrolase from plasmid pOXT1 of Priestia megaterium) and its experimentally determined substrate 4'-phosphooxetanocin A, which is an extremely rare natural product with no obvious sequence-level predictor accessible from the 194-aa input.


**Reason**

> Correct identification requires knowing that this particular 194-residue sequence encodes OxsA, an enzyme acting on the obscure natural product 4'-phosphooxetanocin A. No general biological reasoning from the amino acid sequence allows prediction of this specific substrate. The HD-domain motif, while present, is not reliably identifiable from sequence alone, and even if identified as a phosphohydrolase, the choice between a common phosphatase substrate (phosphoserine, Choice A) and the highly specific oxetanocin substrate (Choice D) depends entirely on item-specific experimental annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "D"
]
```

> Both A and D describe phosphatase-type reactions (hydrolysis of a phosphate ester). Without knowing the specific enzyme identity, a model that identifies the protein as a generic phosphatase could reasonably consider A (O-phospho-L-serine dephosphorylation) as an alternative. The substrate 4'-phosphooxetanocin A in D is so obscure that no sequence-based reasoning would prefer it over the more biochemically common phosphoserine substrate in A.


### Important caveats

- The UniProt annotation is based on direct experimental evidence (X-ray crystallography and biochemical assays, ECO:0000269), not computational prediction.
- The sequence match is exact (194 AA, identical SHA256) between the benchmark input and UniProt O24769.
- The identity of the protein was inferred by the reviewer from dataset metadata (image-path), not from the model's input.
- The entry was first publicly released in UniProt on 2025-02-05; if the benchmark was constructed before that date, the annotation may not have been publicly available at construction time, though the underlying papers (2016, 2017) were published earlier.
- The HD-domain motif (His-Asp) is a real structural feature of this enzyme, but its identification from a raw 194-aa sequence without structural context is not a reliable reasoning pathway.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The protein is only 194 amino acids, which could eliminate Choice B (a multi-subunit polyketide synthase reaction requiring a very large enzyme). However, distinguishing among A (phosphatase on O-phospho-L-serine), C (cystathionine gamma-synthase), and D (phosphatase on 4'-phosphooxetanocin A) from the raw sequence alone is not feasible through general reasoning. The HD-domain phosphohydrolase motif is extremely difficult to identify from a 194-residue sequence without structural or database context, and even recognizing a generic phosphatase activity would not predict the highly obscure substrate 4'-phosphooxetanocin A (a nucleoside-analog antibiotic natural product) over more common phosphoamino-acid substrates.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific identity of this protein as OxsA (HD-domain phosphohydrolase from plasmid pOXT1 of Priestia megaterium) and its experimentally determined substrate 4'-phosphooxetanocin A, which is an extremely rare natural product with no obvious sequence-level predictor accessible from the 194-aa input.",
    "reason": "Correct identification requires knowing that this particular 194-residue sequence encodes OxsA, an enzyme acting on the obscure natural product 4'-phosphooxetanocin A. No general biological reasoning from the amino acid sequence allows prediction of this specific substrate. The HD-domain motif, while present, is not reliably identifiable from sequence alone, and even if identified as a phosphohydrolase, the choice between a common phosphatase substrate (phosphoserine, Choice A) and the highly specific oxetanocin substrate (Choice D) depends entirely on item-specific experimental annotation."
  },
  "case_id": "catalytic_activity_0148",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C7",
      "H1",
      "H2",
      "H5",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The protein sequence exactly matches UniProt O24769 (OXSA_PRIMG, 194 AA, SHA256 matched). The entry is experimentally annotated as '4'-phosphooxetanocin A phosphatase' (EC 3.1.3.112) with the catalytic reaction '4'-phosphooxetanocin A + H2O = oxetanocin A + phosphate' (RHEA:81367). This annotation carries ECO:0000269 (direct experimental evidence) from PubMed:27849620 and PubMed:28346939, and is corroborated by X-ray crystallography structures (PDB 5TK6–5TKA) in complexes with oxetanocin A and its phosphorylated forms. The expected answer D matches the annotated reaction verbatim."
  },
  "important_caveats": [
    "The UniProt annotation is based on direct experimental evidence (X-ray crystallography and biochemical assays, ECO:0000269), not computational prediction.",
    "The sequence match is exact (194 AA, identical SHA256) between the benchmark input and UniProt O24769.",
    "The identity of the protein was inferred by the reviewer from dataset metadata (image-path), not from the model's input.",
    "The entry was first publicly released in UniProt on 2025-02-05; if the benchmark was constructed before that date, the annotation may not have been publicly available at construction time, though the underlying papers (2016, 2017) were published earlier.",
    "The HD-domain motif (His-Asp) is a real structural feature of this enzyme, but its identification from a raw 194-aa sequence without structural context is not a reliable reasoning pathway."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "D"
    ],
    "reason": "Both A and D describe phosphatase-type reactions (hydrolysis of a phosphate ester). Without knowing the specific enzyme identity, a model that identifies the protein as a generic phosphatase could reasonably consider A (O-phospho-L-serine dephosphorylation) as an alternative. The substrate 4'-phosphooxetanocin A in D is so obscure that no sequence-based reasoning would prefer it over the more biochemically common phosphoserine substrate in A."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0148",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The protein sequence exactly matches UniProt O24769 (OXSA_PRIMG, 194 AA, SHA256 matched). The entry is experimentally annotated as '4'-phosphooxetanocin A phosphatase' (EC 3.1.3.112) with the catalytic reaction '4'-phosphooxetanocin A + H2O = oxetanocin A + phosphate' (RHEA:81367). This annotation carries ECO:0000269 (direct experimental evidence) from PubMed:27849620 and PubMed:28346939, and is corroborated by X-ray crystallography structures (PDB 5TK6–5TKA) in complexes with oxetanocin A and its phosphorylated forms. The expected answer D matches the annotated reaction verbatim.",
    "evidence_ids": ["C1", "C4", "C5", "C7", "H1", "H2", "H5", "H6"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The protein is only 194 amino acids, which could eliminate Choice B (a multi-subunit polyketide synthase reaction requiring a very large enzyme). However, distinguishing among A (phosphatase on O-phospho-L-serine), C (cystathionine gamma-synthase), and D (phosphatase on 4'-phosphooxetanocin A) from the raw sequence alone is not feasible through general reasoning. The HD-domain phosphohydrolase motif is extremely difficult to identify from a 194-residue sequence without structural or database context, and even recognizing a generic phosphatase activity would not predict the highly obscure substrate 4'-phosphooxetanocin A (a nucleoside-analog antibiotic natural product) over more common phosphoamino-acid substrates.",
    "missing_item_specific_fact": "The specific identity of this protein as OxsA (HD-domain phosphohydrolase from plasmid pOXT1 of Priestia megaterium) and its experimentally determined substrate 4'-phosphooxetanocin A, which is an extremely rare natural product with no obvious sequence-level predictor accessible from the 194-aa input.",
    "reason": "Correct identification requires knowing that this particular 194-residue sequence encodes OxsA, an enzyme acting on the obscure natural product 4'-phosphooxetanocin A. No general biological reasoning from the amino acid sequence allows prediction of this specific substrate. The HD-domain motif, while present, is not reliably identifiable from sequence alone, and even if identified as a phosphohydrolase, the choice between a common phosphatase substrate (phosphoserine, Choice A) and the highly specific oxetanocin substrate (Choice D) depends entirely on item-specific experimental annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "D"],
    "reason": "Both A and D describe phosphatase-type reactions (hydrolysis of a phosphate ester). Without knowing the specific enzyme identity, a model that identifies the protein as a generic phosphatase could reasonably consider A (O-phospho-L-serine dephosphorylation) as an alternative. The substrate 4'-phosphooxetanocin A in D is so obscure that no sequence-based reasoning would prefer it over the more biochemically common phosphoserine substrate in A."
  },
  "important_caveats": [
    "The UniProt annotation is based on direct experimental evidence (X-ray crystallography and biochemical assays, ECO:0000269), not computational prediction.",
    "The sequence match is exact (194 AA, identical SHA256) between the benchmark input and UniProt O24769.",
    "The identity of the protein was inferred by the reviewer from dataset metadata (image-path), not from the model's input.",
    "The entry was first publicly released in UniProt on 2025-02-05; if the benchmark was constructed before that date, the annotation may not have been publicly available at construction time, though the underlying papers (2016, 2017) were published earlier.",
    "The HD-domain motif (His-Asp) is a real structural feature of this enzyme, but its identification from a raw 194-aa sequence without structural context is not a reliable reasoning pathway."
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

**Accession:** `O24769` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 75. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O24769.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:10.548137+00:00.  

```json
"O24769"
```

Source SHA-256: `1c63e689d95c3766e652d2d5563f236adaca6c85d877b17df78572f9e47ef24b`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O24769.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:10.548137+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"28346939","source":"PubMed"}],"value":"HD-domain phosphohydrolase OxsA"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"27849620","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"28346939","source":"PubMed"}],"value":"3.1.3.112"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"4'-phosphooxetanocin A phosphatase"}}}
```

Source SHA-256: `1c63e689d95c3766e652d2d5563f236adaca6c85d877b17df78572f9e47ef24b`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O24769.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:10.548137+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000269","id":"27849620","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"28346939","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:81368"}}],"reaction":{"ecNumber":"3.1.3.112","evidences":[{"evidenceCode":"ECO:0000269","id":"27849620","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"28346939","source":"PubMed"}],"name":"4'-phosphooxetanocin A + H2O = oxetanocin A + phosphate","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:81367"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:43474"},{"database":"ChEBI","id":"CHEBI:85720"},{"database":"ChEBI","id":"CHEBI:86012"}]}}
```

Source SHA-256: `1c63e689d95c3766e652d2d5563f236adaca6c85d877b17df78572f9e47ef24b`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O24769.json)  
**Locator:** `/references/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:10.548137+00:00.  

```json
{"citation":{"authors":["Bridwell-Rabb J.","Kang G.","Zhong A.","Liu H.W.","Drennan C.L."],"citationCrossReferences":[{"database":"PubMed","id":"27849620"},{"database":"DOI","id":"10.1073/pnas.1613610113"}],"citationType":"journal article","firstPage":"13750","id":"27849620","journal":"Proc. Natl. Acad. Sci. U.S.A.","lastPage":"13755","publicationDate":"2016","title":"An HD domain phosphohydrolase active site tailored for oxetanocin-A biosynthesis.","volume":"113"},"evidences":[{"evidenceCode":"ECO:0007744","id":"5TK6","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"5TK7","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"5TK8","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"5TK9","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"5TKA","source":"PDB"}],"referenceNumber":3,"referencePositions":["X-RAY CRYSTALLOGRAPHY (1.64 ANGSTROMS) IN COMPLEXES WITH MAGNESIUM; OXETANOCIN A; OXETANOCIN A MONOPHOSPHATE; OXETANOCIN A DIPHOSPHATE AND OXETANOCIN A TRIPHOSPHATE","FUNCTION","CATALYTIC ACTIVITY","COFACTOR","BIOPHYSICOCHEMICAL PROPERTIES","SUBUNIT","DOMAIN"]}
```

Source SHA-256: `1c63e689d95c3766e652d2d5563f236adaca6c85d877b17df78572f9e47ef24b`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O24769?format=txt&versions=75)  
**Locator:** `lines 1-13`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 75 / 1.  
**Retrieved:** 2026-11-02T04:29:21.063065+00:00.  

```text
ID   OXSA_PRIMG              Reviewed;         194 AA.
AC   O24769;
DT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.
DT   01-JAN-1998, sequence version 1.
DT   18-JUN-2025, entry version 75.
DE   RecName: Full=4'-phosphooxetanocin A phosphatase {ECO:0000305};
DE            EC=3.1.3.112 {ECO:0000269|PubMed:27849620, ECO:0000269|PubMed:28346939};
DE   AltName: Full=HD-domain phosphohydrolase OxsA {ECO:0000303|PubMed:28346939};
GN   Name=oxsA {ECO:0000312|EMBL:BAA21630.1};
OS   Priestia megaterium (Bacillus megaterium).
OG   Plasmid pOXT1 {ECO:0000303|PubMed:10227144}.
OC   Bacteria; Bacillati; Bacillota; Bacilli; Bacillales; Bacillaceae; Priestia.
OX   NCBI_TaxID=1404;
```

Source SHA-256: `bab6b179917835711477092cc4cbfcd87e9b1a12b22b046feb1fb9be2c17050d`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O24769?format=txt&versions=75)  
**Locator:** `lines 6-8`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 75 / 1.  
**Retrieved:** 2026-11-02T04:29:21.063065+00:00.  

```text
DE   RecName: Full=4'-phosphooxetanocin A phosphatase {ECO:0000305};
DE            EC=3.1.3.112 {ECO:0000269|PubMed:27849620, ECO:0000269|PubMed:28346939};
DE   AltName: Full=HD-domain phosphohydrolase OxsA {ECO:0000303|PubMed:28346939};
```

Source SHA-256: `bab6b179917835711477092cc4cbfcd87e9b1a12b22b046feb1fb9be2c17050d`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O24769?format=txt&versions=75)  
**Locator:** `lines 30-39`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 75 / 1.  
**Retrieved:** 2026-11-02T04:29:21.063065+00:00.  

```text
RN   [3] {ECO:0007744|PDB:5TK6, ECO:0007744|PDB:5TK7, ECO:0007744|PDB:5TK8, ECO:0007744|PDB:5TK9, ECO:0007744|PDB:5TKA}
RP   X-RAY CRYSTALLOGRAPHY (1.64 ANGSTROMS) IN COMPLEXES WITH MAGNESIUM;
RP   OXETANOCIN A; OXETANOCIN A MONOPHOSPHATE; OXETANOCIN A DIPHOSPHATE AND
RP   OXETANOCIN A TRIPHOSPHATE, FUNCTION, CATALYTIC ACTIVITY, COFACTOR,
RP   BIOPHYSICOCHEMICAL PROPERTIES, SUBUNIT, AND DOMAIN.
RX   PubMed=27849620; DOI=10.1073/pnas.1613610113;
RA   Bridwell-Rabb J., Kang G., Zhong A., Liu H.W., Drennan C.L.;
RT   "An HD domain phosphohydrolase active site tailored for oxetanocin-A
RT   biosynthesis.";
RL   Proc. Natl. Acad. Sci. U.S.A. 113:13750-13755(2016).
```

Source SHA-256: `bab6b179917835711477092cc4cbfcd87e9b1a12b22b046feb1fb9be2c17050d`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O24769?format=txt&versions=75)  
**Locator:** `lines 52-58`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 75 / 1.  
**Retrieved:** 2026-11-02T04:29:21.063065+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=4'-phosphooxetanocin A + H2O = oxetanocin A + phosphate;
CC         Xref=Rhea:RHEA:81367, ChEBI:CHEBI:15377, ChEBI:CHEBI:43474,
CC         ChEBI:CHEBI:85720, ChEBI:CHEBI:86012; EC=3.1.3.112;
CC         Evidence={ECO:0000269|PubMed:27849620, ECO:0000269|PubMed:28346939};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:81368;
CC         Evidence={ECO:0000269|PubMed:27849620, ECO:0000269|PubMed:28346939};
```

Source SHA-256: `bab6b179917835711477092cc4cbfcd87e9b1a12b22b046feb1fb9be2c17050d`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 148. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
