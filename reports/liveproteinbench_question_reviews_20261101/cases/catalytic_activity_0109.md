# catalytic_activity_0109

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `catalytic_activity`  
**Author expected answer:** **C** — Hydrolysis of terminal, non-reducing (1-&gt;4)-linked alpha-D-glucose residues with release of alpha-D-glucose.

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MKTFAPLLATLLLAGFGSALQWWEHGNFYQVYPRSFKDSDGNGIGDLDGVTEKLQYLKDVGMDGIWLSPIFASPMADFGYDISDFYNIQGEYGDLAAFERLSAKCKELGLRLILDFVPNHTSNQHEYFKKSVQKEDPYTNYYVWHPGVTNEDGTKSPPSNWISVFRGSAWEWNEDRQEYYLHQFLKEQPDLNYRDPALVEEMKNVLKFWLNKGVSGFRIDAVPYLFESVEVENRYVDEPLSRATDDAENPAYLIHNQTMDQPETYDMIYQWRAVLDEFTAKDNQTRIMMTEGYTSIPNVMKFFGEGEQNGAQIPFNFQMISNLRKTSTAADFARYANLWLDNLPAGRRSNWVLGNHDNNRIGSRLGEAKIDLYNIALQTLPDIAVTYYGEEIGMVDQPIPFNETVDPAGLRAGPDDYTLYSRDPARTPMQWNSDKNAGFSSADKTWLPVATNYKQLNVKAQDAAQKSHLKLFKRLTTYRKRQILTHGDLDLRTTDSNLVLYKRKVDKVGYVVVVLNFSDEPQSLAAIKQQFPGADDRLQVVASSKLVTIKDNKWINVADTELPGESAIVLQKLWGPNPVVVYEA

[Multiple Choices]
A. N-methyl-4-hydroxy-3,5-dimethoxyphenethylamine + S-adenosyl-L-methionine = N,N-dimethyl-4-hydroxy-3,5-dimethoxyphenethylamine + S-adenosyl-L-homocysteine + H(+)
B. AH2 + 2 S-adenosyl-L-methionine = 2 5'-deoxyadenosin-5'-yl radical + 2 L-methionine + A + 2 H(+)
C. Hydrolysis of terminal, non-reducing (1->4)-linked alpha-D-glucose residues with release of alpha-D-glucose.
D. beta-nicotinamide D-ribonucleotide + ATP + H(+) = diphosphate + NAD(+)
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

> The exact sequence matches UniProt entry B0XAA1, annotated as salivary alpha-glucosidase with the reaction in choice C. The catalytic-activity annotation carries experimental evidence codes linked to two publications, though those studies were not independently reviewed here.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The N-terminal signal peptide is consistent with a secreted protein and makes the cytosolic-enzyme alternatives less plausible, but it does not establish the enzyme's substrate specificity or exact reaction.


**Missing item-specific fact**

> The supplied input does not provide this protein's experimentally established alpha-glucosidase activity or an identification linking it to that catalytic annotation.


**Reason**

> Selecting the precise hydrolysis reaction requires protein-specific functional knowledge or a reliable family/annotation match. General sequence context alone does not establish hydrolysis of terminal alpha-D-glucose residues.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The choices describe distinct enzyme activities, and the sequence-matched annotation supports C.


### Important caveats

- The cited database evidence is reviewer-only and was not available to the evaluated model.
- The UniProt annotation cites experimental evidence, but the underlying papers were not independently assessed.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal signal peptide is consistent with a secreted protein and makes the cytosolic-enzyme alternatives less plausible, but it does not establish the enzyme's substrate specificity or exact reaction.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The supplied input does not provide this protein's experimentally established alpha-glucosidase activity or an identification linking it to that catalytic annotation.",
    "reason": "Selecting the precise hydrolysis reaction requires protein-specific functional knowledge or a reliable family/annotation match. General sequence context alone does not establish hydrolysis of terminal alpha-D-glucose residues."
  },
  "case_id": "catalytic_activity_0109",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches UniProt entry B0XAA1, annotated as salivary alpha-glucosidase with the reaction in choice C. The catalytic-activity annotation carries experimental evidence codes linked to two publications, though those studies were not independently reviewed here."
  },
  "important_caveats": [
    "The cited database evidence is reviewer-only and was not available to the evaluated model.",
    "The UniProt annotation cites experimental evidence, but the underlying papers were not independently assessed."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The choices describe distinct enzyme activities, and the sequence-matched annotation supports C."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0109",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches UniProt entry B0XAA1, annotated as salivary alpha-glucosidase with the reaction in choice C. The catalytic-activity annotation carries experimental evidence codes linked to two publications, though those studies were not independently reviewed here.",
    "evidence_ids": ["C1", "C4", "C5", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The N-terminal signal peptide is consistent with a secreted protein and makes the cytosolic-enzyme alternatives less plausible, but it does not establish the enzyme's substrate specificity or exact reaction.",
    "missing_item_specific_fact": "The supplied input does not provide this protein's experimentally established alpha-glucosidase activity or an identification linking it to that catalytic annotation.",
    "reason": "Selecting the precise hydrolysis reaction requires protein-specific functional knowledge or a reliable family/annotation match. General sequence context alone does not establish hydrolysis of terminal alpha-D-glucose residues."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The choices describe distinct enzyme activities, and the sequence-matched annotation supports C."
  },
  "important_caveats": [
    "The cited database evidence is reviewer-only and was not available to the evaluated model.",
    "The UniProt annotation cites experimental evidence, but the underlying papers were not independently assessed."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The protein sequence (584 aa, sha256-matched) corresponds to UniProt B0XAA1 (MALT_CULQU), Salivary alpha-glucosidase from Culex quinquefasciatus. The catalytic activity is annotated as EC 3.2.1.20: 'Hydrolysis of terminal, non-reducing (1->4)-linked alpha-D-glucose residues with release of alpha-D-glucose,' supported by experimental evidence (ECO:0000269) from PubMed:25746591 and PubMed:38428508. Choice C matches this annotation verbatim.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> Weak elimination-based reasoning is possible: the absence of a CX3CX2C motif argues against radical SAM (B); the 584-aa length and lack of NAD-synthetase active-site architecture argue against D; the absence of a canonical SAM-binding Rossmann-fold motif weakly argues against A. However, none of these negative observations positively identifies the enzyme as a GH31 alpha-glucosidase (EC 3.2.1.20) specifically, as opposed to another glycosidase, protease, or other hydrolase.


**Missing item-specific fact**

> Positive identification requires either recognition of the exact sequence (or its UniProt entry) or detailed knowledge of GH31-family catalytic motifs (e.g., the specific Glu nucleophile and Asp general-acid arrangement in the TIM-barrel active site) sufficient to assign EC 3.2.1.20 from primary sequence alone. The sequence does not contain an easily recognizable, unique catalytic signature that unambiguously distinguishes alpha-glucosidase from other glycoside hydrolases or other enzyme classes without database lookup.


**Reason**

> The four choices span radically different enzyme classes, making elimination of some distractors feasible, but the positive assignment to alpha-glucosidase (EC 3.2.1.20) from a 584-aa sequence without structural context or database access depends on item-specific knowledge of GH31 family motifs or direct recognition of this protein. General biological knowledge alone does not provide a concrete, sequence-grounded argument that uniquely selects C over, say, a generic glycosidase or another hydrolase.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four choices represent distinct enzyme classes (methyltransferase, radical SAM, glycosidase, NAD synthetase). Given the correct annotation, only C is correct. The distractors are from sufficiently different enzyme classes that they are unlikely to be confused with the true answer by a knowledgeable reader, though the positive identification of C from sequence alone is difficult.


### Important caveats

- The reviewer-only evidence confirms the annotation via experimental evidence codes (ECO:0000269), establishing the key is scientifically grounded.
- The sequence match between the benchmark input and UniProt B0XAA1 is exact (sha256 confirmed), so the annotation applies directly.
- The UniProt entry was first public in 2025-04-09; if the benchmark was constructed before that date, the annotation may not have been available in the author's source snapshot, though the underlying publications (2015, 2024) predate the entry.
- Elimination-based reasoning (removing B and D) is possible but does not constitute positive identification of alpha-glucosidase activity.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Weak elimination-based reasoning is possible: the absence of a CX3CX2C motif argues against radical SAM (B); the 584-aa length and lack of NAD-synthetase active-site architecture argue against D; the absence of a canonical SAM-binding Rossmann-fold motif weakly argues against A. However, none of these negative observations positively identifies the enzyme as a GH31 alpha-glucosidase (EC 3.2.1.20) specifically, as opposed to another glycosidase, protease, or other hydrolase.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "Positive identification requires either recognition of the exact sequence (or its UniProt entry) or detailed knowledge of GH31-family catalytic motifs (e.g., the specific Glu nucleophile and Asp general-acid arrangement in the TIM-barrel active site) sufficient to assign EC 3.2.1.20 from primary sequence alone. The sequence does not contain an easily recognizable, unique catalytic signature that unambiguously distinguishes alpha-glucosidase from other glycoside hydrolases or other enzyme classes without database lookup.",
    "reason": "The four choices span radically different enzyme classes, making elimination of some distractors feasible, but the positive assignment to alpha-glucosidase (EC 3.2.1.20) from a 584-aa sequence without structural context or database access depends on item-specific knowledge of GH31 family motifs or direct recognition of this protein. General biological knowledge alone does not provide a concrete, sequence-grounded argument that uniquely selects C over, say, a generic glycosidase or another hydrolase."
  },
  "case_id": "catalytic_activity_0109",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C7",
      "H2",
      "H3",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The protein sequence (584 aa, sha256-matched) corresponds to UniProt B0XAA1 (MALT_CULQU), Salivary alpha-glucosidase from Culex quinquefasciatus. The catalytic activity is annotated as EC 3.2.1.20: 'Hydrolysis of terminal, non-reducing (1->4)-linked alpha-D-glucose residues with release of alpha-D-glucose,' supported by experimental evidence (ECO:0000269) from PubMed:25746591 and PubMed:38428508. Choice C matches this annotation verbatim."
  },
  "important_caveats": [
    "The reviewer-only evidence confirms the annotation via experimental evidence codes (ECO:0000269), establishing the key is scientifically grounded.",
    "The sequence match between the benchmark input and UniProt B0XAA1 is exact (sha256 confirmed), so the annotation applies directly.",
    "The UniProt entry was first public in 2025-04-09; if the benchmark was constructed before that date, the annotation may not have been available in the author's source snapshot, though the underlying publications (2015, 2024) predate the entry.",
    "Elimination-based reasoning (removing B and D) is possible but does not constitute positive identification of alpha-glucosidase activity."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices represent distinct enzyme classes (methyltransferase, radical SAM, glycosidase, NAD synthetase). Given the correct annotation, only C is correct. The distractors are from sufficiently different enzyme classes that they are unlikely to be confused with the true answer by a knowledgeable reader, though the positive identification of C from sequence alone is difficult."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0109",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The protein sequence (584 aa, sha256-matched) corresponds to UniProt B0XAA1 (MALT_CULQU), Salivary alpha-glucosidase from Culex quinquefasciatus. The catalytic activity is annotated as EC 3.2.1.20: 'Hydrolysis of terminal, non-reducing (1->4)-linked alpha-D-glucose residues with release of alpha-D-glucose,' supported by experimental evidence (ECO:0000269) from PubMed:25746591 and PubMed:38428508. Choice C matches this annotation verbatim.",
    "evidence_ids": ["C4", "C5", "C6", "C7", "H2", "H3", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "Weak elimination-based reasoning is possible: the absence of a CX3CX2C motif argues against radical SAM (B); the 584-aa length and lack of NAD-synthetase active-site architecture argue against D; the absence of a canonical SAM-binding Rossmann-fold motif weakly argues against A. However, none of these negative observations positively identifies the enzyme as a GH31 alpha-glucosidase (EC 3.2.1.20) specifically, as opposed to another glycosidase, protease, or other hydrolase.",
    "missing_item_specific_fact": "Positive identification requires either recognition of the exact sequence (or its UniProt entry) or detailed knowledge of GH31-family catalytic motifs (e.g., the specific Glu nucleophile and Asp general-acid arrangement in the TIM-barrel active site) sufficient to assign EC 3.2.1.20 from primary sequence alone. The sequence does not contain an easily recognizable, unique catalytic signature that unambiguously distinguishes alpha-glucosidase from other glycoside hydrolases or other enzyme classes without database lookup.",
    "reason": "The four choices span radically different enzyme classes, making elimination of some distractors feasible, but the positive assignment to alpha-glucosidase (EC 3.2.1.20) from a 584-aa sequence without structural context or database access depends on item-specific knowledge of GH31 family motifs or direct recognition of this protein. General biological knowledge alone does not provide a concrete, sequence-grounded argument that uniquely selects C over, say, a generic glycosidase or another hydrolase."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices represent distinct enzyme classes (methyltransferase, radical SAM, glycosidase, NAD synthetase). Given the correct annotation, only C is correct. The distractors are from sufficiently different enzyme classes that they are unlikely to be confused with the true answer by a knowledgeable reader, though the positive identification of C from sequence alone is difficult."
  },
  "important_caveats": [
    "The reviewer-only evidence confirms the annotation via experimental evidence codes (ECO:0000269), establishing the key is scientifically grounded.",
    "The sequence match between the benchmark input and UniProt B0XAA1 is exact (sha256 confirmed), so the annotation applies directly.",
    "The UniProt entry was first public in 2025-04-09; if the benchmark was constructed before that date, the annotation may not have been available in the author's source snapshot, though the underlying publications (2015, 2024) predate the entry.",
    "Elimination-based reasoning (removing B and D) is possible but does not constitute positive identification of alpha-glucosidase activity."
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

**Accession:** `B0XAA1` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 92. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B0XAA1.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:15.565561+00:00.  

```json
"B0XAA1"
```

Source SHA-256: `9afccd0935d9c913183f609d3d8afcc2196f79187f5d0532d2ba6ed0e5048c10`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B0XAA1.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:15.565561+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"25746591","source":"PubMed"}],"value":"CQMalI"}}],"flag":"Precursor","recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"25746591","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"38428508","source":"PubMed"}],"value":"3.2.1.20"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"38428508","source":"PubMed"}],"value":"Salivary alpha-glucosidase"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"38428508","source":"PubMed"}],"value":"CxGluc"}]}}
```

Source SHA-256: `9afccd0935d9c913183f609d3d8afcc2196f79187f5d0532d2ba6ed0e5048c10`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B0XAA1.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:15.565561+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"3.2.1.20","evidences":[{"evidenceCode":"ECO:0000269","id":"25746591","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"38428508","source":"PubMed"}],"name":"Hydrolysis of terminal, non-reducing (1->4)-linked alpha-D-glucose residues with release of alpha-D-glucose."}}
```

Source SHA-256: `9afccd0935d9c913183f609d3d8afcc2196f79187f5d0532d2ba6ed0e5048c10`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B0XAA1.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:15.565561+00:00.  

```json
{"citation":{"authors":["Suthangkornkul R.","Sirichaiyakul P.","Sungvornyothin S.","Thepouyporn A.","Svasti J.","Arthan D."],"citationCrossReferences":[{"database":"PubMed","id":"25746591"},{"database":"DOI","id":"10.1016/j.pep.2015.02.018"}],"citationType":"journal article","firstPage":"145","id":"25746591","journal":"Protein Expr. Purif.","lastPage":"150","publicationDate":"2015","title":"Functional expression and molecular characterization of Culex quinquefasciatus salivary alpha-glucosidase (MalI).","volume":"110"},"evidences":[{"evidenceCode":"ECO:0000305"}],"referenceNumber":2,"referencePositions":["FUNCTION","CATALYTIC ACTIVITY","ACTIVITY REGULATION","BIOPHYSICOCHEMICAL PROPERTIES","GLYCOSYLATION"]}
```

Source SHA-256: `9afccd0935d9c913183f609d3d8afcc2196f79187f5d0532d2ba6ed0e5048c10`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B0XAA1.json)  
**Locator:** `/references/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:15.565561+00:00.  

```json
{"citation":{"authors":["Williams A.E.","Gittis A.G.","Botello K.","Cruz P.","Martin-Martin I.","Valenzuela Leon P.C.","Sumner B.","Bonilla B.","Calvo E."],"citationCrossReferences":[{"database":"PubMed","id":"38428508"},{"database":"DOI","id":"10.1016/j.ibmb.2024.104097"}],"citationType":"journal article","firstPage":"104097","id":"38428508","journal":"Insect Biochem. Mol. Biol.","lastPage":"104097","publicationDate":"2024","title":"Structural and functional comparisons of salivary alpha-glucosidases from the mosquito vectors Aedes aegypti, Anopheles gambiae, and Culex quinquefasciatus.","volume":"167"},"evidences":[{"evidenceCode":"ECO:0000305"}],"referenceNumber":3,"referencePositions":["FUNCTION","CATALYTIC ACTIVITY","BIOPHYSICOCHEMICAL PROPERTIES","SUBCELLULAR LOCATION","TISSUE SPECIFICITY"]}
```

Source SHA-256: `9afccd0935d9c913183f609d3d8afcc2196f79187f5d0532d2ba6ed0e5048c10`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B0XAA1?format=txt&versions=92)  
**Locator:** `lines 6-10`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 92 / 1.  
**Retrieved:** 2026-11-02T04:27:18.547256+00:00.  

```text
DE   RecName: Full=Salivary alpha-glucosidase {ECO:0000303|PubMed:38428508};
DE            Short=CxGluc {ECO:0000303|PubMed:38428508};
DE            EC=3.2.1.20 {ECO:0000269|PubMed:25746591, ECO:0000269|PubMed:38428508};
DE   AltName: Full=CQMalI {ECO:0000303|PubMed:25746591};
DE   Flags: Precursor;
```

Source SHA-256: `5fda9ac6361a740657451da46434a8060a2e37043092db9553e846bf116af583`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B0XAA1?format=txt&versions=92)  
**Locator:** `lines 32-40`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 92 / 1.  
**Retrieved:** 2026-11-02T04:27:18.547256+00:00.  

```text
RN   [2] {ECO:0000305}
RP   FUNCTION, CATALYTIC ACTIVITY, ACTIVITY REGULATION, BIOPHYSICOCHEMICAL
RP   PROPERTIES, AND GLYCOSYLATION.
RX   PubMed=25746591; DOI=10.1016/j.pep.2015.02.018;
RA   Suthangkornkul R., Sirichaiyakul P., Sungvornyothin S., Thepouyporn A.,
RA   Svasti J., Arthan D.;
RT   "Functional expression and molecular characterization of Culex
RT   quinquefasciatus salivary alpha-glucosidase (MalI).";
RL   Protein Expr. Purif. 110:145-150(2015).
```

Source SHA-256: `5fda9ac6361a740657451da46434a8060a2e37043092db9553e846bf116af583`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B0XAA1?format=txt&versions=92)  
**Locator:** `lines 41-50`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 92 / 1.  
**Retrieved:** 2026-11-02T04:27:18.547256+00:00.  

```text
RN   [3] {ECO:0000305}
RP   FUNCTION, CATALYTIC ACTIVITY, BIOPHYSICOCHEMICAL PROPERTIES, SUBCELLULAR
RP   LOCATION, AND TISSUE SPECIFICITY.
RX   PubMed=38428508; DOI=10.1016/j.ibmb.2024.104097;
RA   Williams A.E., Gittis A.G., Botello K., Cruz P., Martin-Martin I.,
RA   Valenzuela Leon P.C., Sumner B., Bonilla B., Calvo E.;
RT   "Structural and functional comparisons of salivary alpha-glucosidases from
RT   the mosquito vectors Aedes aegypti, Anopheles gambiae, and Culex
RT   quinquefasciatus.";
RL   Insect Biochem. Mol. Biol. 167:104097-104097(2024).
```

Source SHA-256: `5fda9ac6361a740657451da46434a8060a2e37043092db9553e846bf116af583`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B0XAA1?format=txt&versions=92)  
**Locator:** `lines 56-59`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 92 / 1.  
**Retrieved:** 2026-11-02T04:27:18.547256+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=Hydrolysis of terminal, non-reducing (1->4)-linked alpha-D-
CC         glucose residues with release of alpha-D-glucose.; EC=3.2.1.20;
CC         Evidence={ECO:0000269|PubMed:25746591, ECO:0000269|PubMed:38428508};
```

Source SHA-256: `5fda9ac6361a740657451da46434a8060a2e37043092db9553e846bf116af583`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 109. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
