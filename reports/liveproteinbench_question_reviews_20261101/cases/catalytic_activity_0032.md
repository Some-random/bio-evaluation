# catalytic_activity_0032

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `catalytic_activity`  
**Author expected answer:** **B** — an adenosine in mRNA + S-adenosyl-L-methionine = an N(6)-methyladenosine in mRNA + S-adenosyl-L-homocysteine + H(+)

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MNGREHRRGDEAARREARSILFQNQDRSIVLIDVPTSIEEAQASPEEVGCDAGPLRKRRRLISSEPPHLPFKTPEPKAGSGGLTESVSDLMIAAAATEALRVLQESYAGPFCLPRVTRPNPLKSAFVPKGSFFLHGTVSSERDRFAAEAPVFDLIVLDPPWPNRSARRKQRNYRVADSLGSIRETLSLIPIAAHLAPDGLLAVWITNKAGVVELLTGPRGLFAQWGLEQVDEWTWLKITTSGEPIVDVGSTWRKPWERILIARRRGSSRKPACRGRVLVSVPDLHSRKPNLRGLFEDVLVPSNKGLEIFARNLTAGWWSWGDEVLKFQQPEYWVES

[Multiple Choices]
A. FMNH2 + NADP(+) = FMN + NADPH + 2 H(+)
B. an adenosine in mRNA + S-adenosyl-L-methionine = an N(6)-methyladenosine in mRNA + S-adenosyl-L-homocysteine + H(+)
C. 2-hydroxyspheroidene + 2 reduced [2Fe-2S]-[ferredoxin] + O2 + 2 H(+) = 2,2-dihydroxyspheroidene + 2 oxidized [2Fe-2S]-[ferredoxin] + H2O
D. Endohydrolysis of (1->4)-beta-D-xylosidic linkages in xylans.
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

> The reviewer-only UniProt entry matches the supplied sequence and assigns it the N6-methyladenosine RNA methyltransferase reaction in choice B, citing experimental evidence codes linked to publications. The cited primary papers were not independently reviewed here.

Citations as saved: [C5](#evidence-c5), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a DPPW motif in a methyltransferase-like region, a recognizable feature of m6A methyltransferases. This gives a meaningful sequence-based reason to favor the SAM-dependent RNA methylation option over the flavin redox, carotenoid hydroxylation, and xylan hydrolysis options.


**Missing item-specific fact**

> The motif alone does not establish exact substrate specificity; identifying mRNA N6 methylation precisely would require further family or functional evidence.


**Reason**

> The sequence motif and domain context provide a concrete basis for distinguishing the broad reaction class among the choices, without relying solely on recognizing the exact protein or its database entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The options describe distinct reaction classes, and the sequence provides a meaningful methyltransferase-related clue favoring B.


### Important caveats

- The database annotation is matched to the sequence and cites experimental evidence, but those experiments were not independently examined.
- The DPPW motif supports a methyltransferase inference but is not, by itself, proof of the precise RNA substrate.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a DPPW motif in a methyltransferase-like region, a recognizable feature of m6A methyltransferases. This gives a meaningful sequence-based reason to favor the SAM-dependent RNA methylation option over the flavin redox, carotenoid hydroxylation, and xylan hydrolysis options.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The motif alone does not establish exact substrate specificity; identifying mRNA N6 methylation precisely would require further family or functional evidence.",
    "reason": "The sequence motif and domain context provide a concrete basis for distinguishing the broad reaction class among the choices, without relying solely on recognizing the exact protein or its database entry."
  },
  "case_id": "catalytic_activity_0032",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The reviewer-only UniProt entry matches the supplied sequence and assigns it the N6-methyladenosine RNA methyltransferase reaction in choice B, citing experimental evidence codes linked to publications. The cited primary papers were not independently reviewed here."
  },
  "important_caveats": [
    "The database annotation is matched to the sequence and cites experimental evidence, but those experiments were not independently examined.",
    "The DPPW motif supports a methyltransferase inference but is not, by itself, proof of the precise RNA substrate."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The options describe distinct reaction classes, and the sequence provides a meaningful methyltransferase-related clue favoring B."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0032",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The reviewer-only UniProt entry matches the supplied sequence and assigns it the N6-methyladenosine RNA methyltransferase reaction in choice B, citing experimental evidence codes linked to publications. The cited primary papers were not independently reviewed here.",
    "evidence_ids": ["C5", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a DPPW motif in a methyltransferase-like region, a recognizable feature of m6A methyltransferases. This gives a meaningful sequence-based reason to favor the SAM-dependent RNA methylation option over the flavin redox, carotenoid hydroxylation, and xylan hydrolysis options.",
    "missing_item_specific_fact": "The motif alone does not establish exact substrate specificity; identifying mRNA N6 methylation precisely would require further family or functional evidence.",
    "reason": "The sequence motif and domain context provide a concrete basis for distinguishing the broad reaction class among the choices, without relying solely on recognizing the exact protein or its database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The options describe distinct reaction classes, and the sequence provides a meaningful methyltransferase-related clue favoring B."
  },
  "important_caveats": [
    "The database annotation is matched to the sequence and cites experimental evidence, but those experiments were not independently examined.",
    "The DPPW motif supports a methyltransferase inference but is not, by itself, proof of the precise RNA substrate."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A0A9P5CQV5 (MTA1_CRYP1, Cryphonectria parasitica) is annotated as N6-methyladenosine RNA methyltransferase (EC 2.1.1.348) with the exact catalytic reaction matching Choice B. The evidence codes are ECO:0000269 (experimental evidence) from PubMed:39159278 and PubMed:39611846, confirming experimental validation. The benchmark sequence SHA256 matches the UniProt sequence exactly (336 AA).

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H1](#evidence-h1), [H2](#evidence-h2), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains the 'DPPW' motif (residues ~170-173: 'LDPPWPNRSARRK'), a well-known signature of the Rossmann-fold methyltransferase superfamily. Among the four choices, only B describes a methyltransferase reaction (SAM-dependent methylation); A is an oxidoreductase (FMN reductase), C is a ferredoxin-dependent hydroxylase, and D is a glycoside hydrolase (xylanase). Additionally, the C-terminal motif 'WWSWGDEVLKF' is characteristic of m6A RNA methyltransferases specifically. A model recognizing the DPPW Rossmann-fold methyltransferase signature can eliminate the three non-methyltransferase options and select B.


**Missing item-specific fact**

> None strictly required. The DPPW motif and GDEVLKF C-terminal motif are general structural-biochemical knowledge about methyltransferase families, not item-specific annotations.


**Reason**

> The sequence provides identifiable structural motifs (DPPW Rossmann-fold signature, GDEVLKF m6A-specific motif) that allow a knowledgeable model to classify the enzyme as a methyltransferase and further as an m6A writer. The four distractors span four entirely different EC classes (oxidoreductase, methyltransferase, hydroxylase, hydrolase), so identifying the enzyme class from sequence motifs is sufficient to select B. This does not require memorizing this specific protein's database entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four choices represent four distinct enzyme classes (EC 1.5.1, EC 2.1.1, EC 1.14.14, EC 3.2.1). The sequence motifs clearly indicate a methyltransferase fold, and only one option (B) is a methyltransferase reaction. No ambiguity exists among the choices.


### Important caveats

- The annotation evidence (ECO:0000269) is experimental, based on in vitro/in vivo characterization in PLoS Pathogens 2024 and MBio 2025, not merely computational prediction.
- The DPPW motif is shared across many Rossmann-fold methyltransferases; distinguishing m6A specificity from other SAM-dependent methylation requires the additional GDEVLKF motif and overall architecture, which are present in this sequence.
- The reviewer-only evidence confirms the key but was not available to the evaluated model; the model must rely on sequence motifs and general enzymology knowledge.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains the 'DPPW' motif (residues ~170-173: 'LDPPWPNRSARRK'), a well-known signature of the Rossmann-fold methyltransferase superfamily. Among the four choices, only B describes a methyltransferase reaction (SAM-dependent methylation); A is an oxidoreductase (FMN reductase), C is a ferredoxin-dependent hydroxylase, and D is a glycoside hydrolase (xylanase). Additionally, the C-terminal motif 'WWSWGDEVLKF' is characteristic of m6A RNA methyltransferases specifically. A model recognizing the DPPW Rossmann-fold methyltransferase signature can eliminate the three non-methyltransferase options and select B.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None strictly required. The DPPW motif and GDEVLKF C-terminal motif are general structural-biochemical knowledge about methyltransferase families, not item-specific annotations.",
    "reason": "The sequence provides identifiable structural motifs (DPPW Rossmann-fold signature, GDEVLKF m6A-specific motif) that allow a knowledgeable model to classify the enzyme as a methyltransferase and further as an m6A writer. The four distractors span four entirely different EC classes (oxidoreductase, methyltransferase, hydroxylase, hydrolase), so identifying the enzyme class from sequence motifs is sufficient to select B. This does not require memorizing this specific protein's database entry."
  },
  "case_id": "catalytic_activity_0032",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C7",
      "H1",
      "H2",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry A0A9P5CQV5 (MTA1_CRYP1, Cryphonectria parasitica) is annotated as N6-methyladenosine RNA methyltransferase (EC 2.1.1.348) with the exact catalytic reaction matching Choice B. The evidence codes are ECO:0000269 (experimental evidence) from PubMed:39159278 and PubMed:39611846, confirming experimental validation. The benchmark sequence SHA256 matches the UniProt sequence exactly (336 AA)."
  },
  "important_caveats": [
    "The annotation evidence (ECO:0000269) is experimental, based on in vitro/in vivo characterization in PLoS Pathogens 2024 and MBio 2025, not merely computational prediction.",
    "The DPPW motif is shared across many Rossmann-fold methyltransferases; distinguishing m6A specificity from other SAM-dependent methylation requires the additional GDEVLKF motif and overall architecture, which are present in this sequence.",
    "The reviewer-only evidence confirms the key but was not available to the evaluated model; the model must rely on sequence motifs and general enzymology knowledge."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices represent four distinct enzyme classes (EC 1.5.1, EC 2.1.1, EC 1.14.14, EC 3.2.1). The sequence motifs clearly indicate a methyltransferase fold, and only one option (B) is a methyltransferase reaction. No ambiguity exists among the choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0032",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A0A9P5CQV5 (MTA1_CRYP1, Cryphonectria parasitica) is annotated as N6-methyladenosine RNA methyltransferase (EC 2.1.1.348) with the exact catalytic reaction matching Choice B. The evidence codes are ECO:0000269 (experimental evidence) from PubMed:39159278 and PubMed:39611846, confirming experimental validation. The benchmark sequence SHA256 matches the UniProt sequence exactly (336 AA).",
    "evidence_ids": ["C4", "C5", "C6", "C7", "H1", "H2", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains the 'DPPW' motif (residues ~170-173: 'LDPPWPNRSARRK'), a well-known signature of the Rossmann-fold methyltransferase superfamily. Among the four choices, only B describes a methyltransferase reaction (SAM-dependent methylation); A is an oxidoreductase (FMN reductase), C is a ferredoxin-dependent hydroxylase, and D is a glycoside hydrolase (xylanase). Additionally, the C-terminal motif 'WWSWGDEVLKF' is characteristic of m6A RNA methyltransferases specifically. A model recognizing the DPPW Rossmann-fold methyltransferase signature can eliminate the three non-methyltransferase options and select B.",
    "missing_item_specific_fact": "None strictly required. The DPPW motif and GDEVLKF C-terminal motif are general structural-biochemical knowledge about methyltransferase families, not item-specific annotations.",
    "reason": "The sequence provides identifiable structural motifs (DPPW Rossmann-fold signature, GDEVLKF m6A-specific motif) that allow a knowledgeable model to classify the enzyme as a methyltransferase and further as an m6A writer. The four distractors span four entirely different EC classes (oxidoreductase, methyltransferase, hydroxylase, hydrolase), so identifying the enzyme class from sequence motifs is sufficient to select B. This does not require memorizing this specific protein's database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices represent four distinct enzyme classes (EC 1.5.1, EC 2.1.1, EC 1.14.14, EC 3.2.1). The sequence motifs clearly indicate a methyltransferase fold, and only one option (B) is a methyltransferase reaction. No ambiguity exists among the choices."
  },
  "important_caveats": [
    "The annotation evidence (ECO:0000269) is experimental, based on in vitro/in vivo characterization in PLoS Pathogens 2024 and MBio 2025, not merely computational prediction.",
    "The DPPW motif is shared across many Rossmann-fold methyltransferases; distinguishing m6A specificity from other SAM-dependent methylation requires the additional GDEVLKF motif and overall architecture, which are present in this sequence.",
    "The reviewer-only evidence confirms the key but was not available to the evaluated model; the model must rely on sequence motifs and general enzymology knowledge."
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

**Accession:** `A0A9P5CQV5` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 12. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9P5CQV5.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:17.608993+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"39159278","source":"PubMed"}],"value":"M6A writer MTA1"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"39159278","source":"PubMed"}],"value":"2.1.1.348"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"39159278","source":"PubMed"}],"value":"N6-methyladenosine RNA methyltransferase MTA1"}}}
```

Source SHA-256: `f80f2e398397ced5f8091de379dc036e65d2569acedc4ca68eae952f6dcf1313`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9P5CQV5.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:17.608993+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000269","id":"39159278","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"39611846","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:55585"}}],"reaction":{"ecNumber":"2.1.1.348","evidences":[{"evidenceCode":"ECO:0000269","id":"39159278","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"39611846","source":"PubMed"}],"name":"an adenosine in mRNA + S-adenosyl-L-methionine = an N(6)-methyladenosine in mRNA + S-adenosyl-L-homocysteine + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:55584"},{"database":"Rhea","id":"RHEA-COMP:12414"},{"database":"Rhea","id":"RHEA-COMP:12417"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:57856"},{"database":"ChEBI","id":"CHEBI:59789"},{"database":"ChEBI","id":"CHEBI:74411"},{"database":"ChEBI","id":"CHEBI:74449"}]}}
```

Source SHA-256: `f80f2e398397ced5f8091de379dc036e65d2569acedc4ca68eae952f6dcf1313`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9P5CQV5.json)  
**Locator:** `/references/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:17.608993+00:00.  

```json
{"citation":{"authors":["Zhao L.","Wei X.","Chen F.","Yuan L.","Chen B.","Li R."],"citationCrossReferences":[{"database":"PubMed","id":"39159278"},{"database":"DOI","id":"10.1371/journal.ppat.1012476"}],"citationType":"journal article","firstPage":"e1012476","id":"39159278","journal":"PLoS Pathog.","lastPage":"e1012476","publicationDate":"2024","title":"N6-methyladenosine RNA methyltransferase CpMTA1 mediates CpAphA mRNA stability through a YTHDF1-dependent m6A modification in the chestnut blight fungus.","volume":"20"},"referenceNumber":3,"referencePositions":["FUNCTION","CATALYTIC ACTIVITY","DISRUPTION PHENOTYPE"]}
```

Source SHA-256: `f80f2e398397ced5f8091de379dc036e65d2569acedc4ca68eae952f6dcf1313`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9P5CQV5.json)  
**Locator:** `/references/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:17.608993+00:00.  

```json
{"citation":{"authors":["Zhao L.","Wei X.","Chen F.","Chen B.","Li R."],"citationCrossReferences":[{"database":"PubMed","id":"39611846"},{"database":"DOI","id":"10.1128/mbio.01844-24"}],"citationType":"journal article","firstPage":"e0184424","id":"39611846","journal":"MBio","lastPage":"e0184424","publicationDate":"2025","title":"m6A demethylase CpALKBH regulates CpZap1 mRNA stability to modulate the development and virulence of chestnut blight fungus.","volume":"16"},"referenceNumber":4,"referencePositions":["FUNCTION","CATALYTIC ACTIVITY","DISRUPTION PHENOTYPE","SUBCELLULAR LOCATION","MUTAGENESIS OF ASP-158 AND TRP-161"]}
```

Source SHA-256: `f80f2e398397ced5f8091de379dc036e65d2569acedc4ca68eae952f6dcf1313`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A9P5CQV5?format=txt&versions=12)  
**Locator:** `lines 1-14`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 12 / 1.  
**Retrieved:** 2026-11-02T04:26:22.443513+00:00.  

```text
ID   MTA1_CRYP1              Reviewed;         336 AA.
AC   A0A9P5CQV5;
DT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.
DT   13-SEP-2023, sequence version 1.
DT   28-JAN-2026, entry version 12.
DE   RecName: Full=N6-methyladenosine RNA methyltransferase MTA1 {ECO:0000303|PubMed:39159278};
DE            EC=2.1.1.348 {ECO:0000269|PubMed:39159278};
DE   AltName: Full=M6A writer MTA1 {ECO:0000303|PubMed:39159278};
GN   Name=MTA1 {ECO:0000303|PubMed:39159278}; ORFNames=M406DRAFT_288717;
OS   Cryphonectria parasitica (strain ATCC 38755 / EP155).
OC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Sordariomycetes;
OC   Sordariomycetidae; Diaporthales; Cryphonectriaceae;
OC   Cryphonectria-Endothia species complex; Cryphonectria.
OX   NCBI_TaxID=660469;
```

Source SHA-256: `7683f1f2026d2d3f7a56a5510cd29c967cf7add9eaf84cb7e8e224b27899b8cc`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A9P5CQV5?format=txt&versions=12)  
**Locator:** `lines 6-8`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 12 / 1.  
**Retrieved:** 2026-11-02T04:26:22.443513+00:00.  

```text
DE   RecName: Full=N6-methyladenosine RNA methyltransferase MTA1 {ECO:0000303|PubMed:39159278};
DE            EC=2.1.1.348 {ECO:0000269|PubMed:39159278};
DE   AltName: Full=M6A writer MTA1 {ECO:0000303|PubMed:39159278};
```

Source SHA-256: `7683f1f2026d2d3f7a56a5510cd29c967cf7add9eaf84cb7e8e224b27899b8cc`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A9P5CQV5?format=txt&versions=12)  
**Locator:** `lines 62-70`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 12 / 1.  
**Retrieved:** 2026-11-02T04:26:22.443513+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=an adenosine in mRNA + S-adenosyl-L-methionine = an N(6)-
CC         methyladenosine in mRNA + S-adenosyl-L-homocysteine + H(+);
CC         Xref=Rhea:RHEA:55584, Rhea:RHEA-COMP:12414, Rhea:RHEA-COMP:12417,
CC         ChEBI:CHEBI:15378, ChEBI:CHEBI:57856, ChEBI:CHEBI:59789,
CC         ChEBI:CHEBI:74411, ChEBI:CHEBI:74449; EC=2.1.1.348;
CC         Evidence={ECO:0000269|PubMed:39159278, ECO:0000269|PubMed:39611846};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:55585;
CC         Evidence={ECO:0000269|PubMed:39159278, ECO:0000269|PubMed:39611846};
```

Source SHA-256: `7683f1f2026d2d3f7a56a5510cd29c967cf7add9eaf84cb7e8e224b27899b8cc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 32. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
