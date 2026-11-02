# catalytic_activity_0108

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `catalytic_activity`  
**Author expected answer:** **A** — deacetylipecoside + H2O = deacetylipecoside aglycone + D-glucose

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MSSVLPTPVLPTPGRNINRGHFPDDFIFGAGTSSYQIEGAAREGGRGPSIWDTFTHTHPELIQDGSNGDTAINSYNLYKEDIKIVKLMGLDAYRFSISWPRILPGGSINAGINQEGIKYYNNLIDELLANDIVPYVTLFHWDVPQALQDQYDGFLSDKIVDDFRDFAELCFWEFGDRVKNWITINEPQSYSDFFGVAYDTPPKAHALKASRLLVPTTVARPSKPVRVFASTADPGTTTADQVYKVGHNLLLAHAAAIQVYRDKFQNTQEGTFGMALVTQWMKPLNENNPADVEAASRAFDFKFGWFMQPLITGEYPKSMRQLLGPRLREFTPDQKKLLIGSYDYVGVNYYTATYVSSAQPPHDKKKAVFHTDGNFYTTDSKDGVLIGPLAGPAWLNIVPEGIYHVLHDIKENYEDPVIYITENGVYEVNDTAKTLSEARVDTTRLHYLQDHLSKVLEARHQGVRVQGYLVWSLMDNWELRAGYTSRFGLIHVDYYNNFARYPKDSAIWFRNAFHKRLRIHVNKARPQEDDGAFDTPRKRLRKY

[Multiple Choices]
A. deacetylipecoside + H2O = deacetylipecoside aglycone + D-glucose
B. (1S,4S)-4-[(4-methoxyphenyl)methyl]-2,5-diazaspiro[bicyclo[3.2.1]octane-6,1'-cyclohexan]-4'-one + S-adenosyl-L-methionine = (1S,4S)-4-[(4-methoxyphenyl)methyl]-2-methyl-2,5-diazaspiro[bicyclo[3.2.1]octane-6,1'-cyclohexan]-4'-one + S-adenosyl-L-homocysteine + H(+)
C. O-succinyl-L-homoserine + L-cysteine = L,L-cystathionine + succinate + H(+)
D. norajmaline + S-adenosyl-L-methionine = 4-methylnorajmaline + S-adenosyl-L-homocysteine + H(+)
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

> The exact sequence matches UniProt entry B6ZKM5, annotated as ipecac alkaloid beta-glucosidase 3. Its catalytic-activity annotation gives the reaction in choice A and cites experimental evidence (ECO:0000269, PubMed 18927081).

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C7](#evidence-c7).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a conserved TENG motif characteristic of glycoside hydrolase family 1 enzymes, consistent with a beta-glucosidase. Among the choices, A is the glycoside-hydrolysis reaction; B and D are SAM-dependent methylations, and C is a cystathionine-forming reaction.


**Missing item-specific fact**

> The exact substrate specificity for deacetylipecoside is not established by the motif alone; that specific substrate assignment is protein-specific. However, the sequence-family evidence meaningfully distinguishes A from the other listed reaction classes.


**Reason**

> The choices differ in enzyme reaction class, and the sequence provides a defensible family-level basis for selecting the sole beta-glucosidase reaction. The external annotation supports the precise substrate assignment but is not necessary to distinguish A from these distractors.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Only A is consistent with a beta-glucosidase reaction among the listed choices.


### Important caveats

- The experimental support is conveyed through a UniProt annotation citing PubMed 18927081; the cited primary paper was not independently reviewed here.
- The matched entry also annotates hydrolysis of deacetylisoipecoside, a second reaction not listed among the choices.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a conserved TENG motif characteristic of glycoside hydrolase family 1 enzymes, consistent with a beta-glucosidase. Among the choices, A is the glycoside-hydrolysis reaction; B and D are SAM-dependent methylations, and C is a cystathionine-forming reaction.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The exact substrate specificity for deacetylipecoside is not established by the motif alone; that specific substrate assignment is protein-specific. However, the sequence-family evidence meaningfully distinguishes A from the other listed reaction classes.",
    "reason": "The choices differ in enzyme reaction class, and the sequence provides a defensible family-level basis for selecting the sole beta-glucosidase reaction. The external annotation supports the precise substrate assignment but is not necessary to distinguish A from these distractors."
  },
  "case_id": "catalytic_activity_0108",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C7"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches UniProt entry B6ZKM5, annotated as ipecac alkaloid beta-glucosidase 3. Its catalytic-activity annotation gives the reaction in choice A and cites experimental evidence (ECO:0000269, PubMed 18927081)."
  },
  "important_caveats": [
    "The experimental support is conveyed through a UniProt annotation citing PubMed 18927081; the cited primary paper was not independently reviewed here.",
    "The matched entry also annotates hydrolysis of deacetylisoipecoside, a second reaction not listed among the choices."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only A is consistent with a beta-glucosidase reaction among the listed choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0108",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches UniProt entry B6ZKM5, annotated as ipecac alkaloid beta-glucosidase 3. Its catalytic-activity annotation gives the reaction in choice A and cites experimental evidence (ECO:0000269, PubMed 18927081).",
    "evidence_ids": ["C1", "C4", "C5", "C7"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a conserved TENG motif characteristic of glycoside hydrolase family 1 enzymes, consistent with a beta-glucosidase. Among the choices, A is the glycoside-hydrolysis reaction; B and D are SAM-dependent methylations, and C is a cystathionine-forming reaction.",
    "missing_item_specific_fact": "The exact substrate specificity for deacetylipecoside is not established by the motif alone; that specific substrate assignment is protein-specific. However, the sequence-family evidence meaningfully distinguishes A from the other listed reaction classes.",
    "reason": "The choices differ in enzyme reaction class, and the sequence provides a defensible family-level basis for selecting the sole beta-glucosidase reaction. The external annotation supports the precise substrate assignment but is not necessary to distinguish A from these distractors."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only A is consistent with a beta-glucosidase reaction among the listed choices."
  },
  "important_caveats": [
    "The experimental support is conveyed through a UniProt annotation citing PubMed 18927081; the cited primary paper was not independently reviewed here.",
    "The matched entry also annotates hydrolysis of deacetylisoipecoside, a second reaction not listed among the choices."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProtKB entry B6ZKM5 (Ipecac alkaloid beta-glucosidase 3, IpeGLU3, EC 3.2.1.-) from Carapichea ipecacuanha explicitly annotates the catalytic activity as 'deacetylipecoside + H2O = deacetylipecoside aglycone + D-glucose' with experimental evidence (ECO:0000269, PubMed:18927081, Nomura et al. 2008 J. Biol. Chem.). The 543-aa sequence matches exactly (SHA256 confirmed). The expected answer text is verbatim from the annotation.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C7](#evidence-c7), [H1](#evidence-h1), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 543-aa sequence contains features consistent with glycoside hydrolase family 1 (GH1) beta-glucosidases: approximate length (~500-550 aa), the NEP-containing motif ('INEP' near residue ~200) indicative of the catalytic nucleophile, and overall architecture typical of the (β/α)8 TIM-barrel GH1 fold. Among the four choices, only option A is a glycoside hydrolysis reaction (substrate + H2O → aglycone + D-glucose), which is the defining reaction type of a beta-glucosidase. Options B and D are SAM-dependent methyltransferase reactions (requiring a Rossmann-like fold and entirely different catalytic mechanism), and option C is a PLP-dependent condensation (cystathionine gamma-synthase, requiring a PLP-binding fold). Thus, identifying the enzyme class from sequence features is sufficient to eliminate B, C, and D and select A.


**Missing item-specific fact**

> The exact substrate name 'deacetylipecoside' is protein-specific and not deducible from sequence alone; however, since option A is the only glucosidase reaction among the choices, this specificity is not required to answer the question.


**Reason**

> A model with knowledge of GH1/beta-glucosidase sequence motifs and enzyme-class–reaction-type correspondence can reason from the sequence to the correct answer without memorizing this particular UniProt entry. The reaction-type distinction (hydrolysis vs. methylation vs. PLP-dependent condensation) provides a concrete biological argument that separates the options.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Only option A represents a glycoside hydrolysis reaction consistent with a beta-glucosidase. Options B and D are methyltransferase reactions and option C is a PLP-dependent reaction; none of these enzyme classes share the GH1 fold or catalytic mechanism suggested by the sequence. No ambiguity among choices.


### Important caveats

- The specific substrate 'deacetylipecoside' (as opposed to other ipecoside-family glucosides) is an item-specific annotation detail; the question is answerable because it is the only glucosidase reaction listed, not because the substrate name is derivable from sequence.
- The UniProt entry also annotates a second activity (deacetylisoipecoside hydrolysis, RHEA:78887), but this does not create ambiguity among the provided choices since no option corresponds to that reaction.
- Reviewer-only evidence (UniProt annotation with experimental evidence code ECO:0000269) confirms the key; this evidence was not available to the evaluated model.
- The firstPublicDate of the UniProt entry is 2025-06-18, meaning the curated Swiss-Prot entry post-dates the likely benchmark construction; the underlying experimental data (PubMed:18927081, 2008) predates the benchmark, but the curated annotation may not have been available at construction time.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 543-aa sequence contains features consistent with glycoside hydrolase family 1 (GH1) beta-glucosidases: approximate length (~500-550 aa), the NEP-containing motif ('INEP' near residue ~200) indicative of the catalytic nucleophile, and overall architecture typical of the (β/α)8 TIM-barrel GH1 fold. Among the four choices, only option A is a glycoside hydrolysis reaction (substrate + H2O → aglycone + D-glucose), which is the defining reaction type of a beta-glucosidase. Options B and D are SAM-dependent methyltransferase reactions (requiring a Rossmann-like fold and entirely different catalytic mechanism), and option C is a PLP-dependent condensation (cystathionine gamma-synthase, requiring a PLP-binding fold). Thus, identifying the enzyme class from sequence features is sufficient to eliminate B, C, and D and select A.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The exact substrate name 'deacetylipecoside' is protein-specific and not deducible from sequence alone; however, since option A is the only glucosidase reaction among the choices, this specificity is not required to answer the question.",
    "reason": "A model with knowledge of GH1/beta-glucosidase sequence motifs and enzyme-class–reaction-type correspondence can reason from the sequence to the correct answer without memorizing this particular UniProt entry. The reaction-type distinction (hydrolysis vs. methylation vs. PLP-dependent condensation) provides a concrete biological argument that separates the options."
  },
  "case_id": "catalytic_activity_0108",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C7",
      "H1",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "UniProtKB entry B6ZKM5 (Ipecac alkaloid beta-glucosidase 3, IpeGLU3, EC 3.2.1.-) from Carapichea ipecacuanha explicitly annotates the catalytic activity as 'deacetylipecoside + H2O = deacetylipecoside aglycone + D-glucose' with experimental evidence (ECO:0000269, PubMed:18927081, Nomura et al. 2008 J. Biol. Chem.). The 543-aa sequence matches exactly (SHA256 confirmed). The expected answer text is verbatim from the annotation."
  },
  "important_caveats": [
    "The specific substrate 'deacetylipecoside' (as opposed to other ipecoside-family glucosides) is an item-specific annotation detail; the question is answerable because it is the only glucosidase reaction listed, not because the substrate name is derivable from sequence.",
    "The UniProt entry also annotates a second activity (deacetylisoipecoside hydrolysis, RHEA:78887), but this does not create ambiguity among the provided choices since no option corresponds to that reaction.",
    "Reviewer-only evidence (UniProt annotation with experimental evidence code ECO:0000269) confirms the key; this evidence was not available to the evaluated model.",
    "The firstPublicDate of the UniProt entry is 2025-06-18, meaning the curated Swiss-Prot entry post-dates the likely benchmark construction; the underlying experimental data (PubMed:18927081, 2008) predates the benchmark, but the curated annotation may not have been available at construction time."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only option A represents a glycoside hydrolysis reaction consistent with a beta-glucosidase. Options B and D are methyltransferase reactions and option C is a PLP-dependent reaction; none of these enzyme classes share the GH1 fold or catalytic mechanism suggested by the sequence. No ambiguity among choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0108",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProtKB entry B6ZKM5 (Ipecac alkaloid beta-glucosidase 3, IpeGLU3, EC 3.2.1.-) from Carapichea ipecacuanha explicitly annotates the catalytic activity as 'deacetylipecoside + H2O = deacetylipecoside aglycone + D-glucose' with experimental evidence (ECO:0000269, PubMed:18927081, Nomura et al. 2008 J. Biol. Chem.). The 543-aa sequence matches exactly (SHA256 confirmed). The expected answer text is verbatim from the annotation.",
    "evidence_ids": ["C1", "C4", "C5", "C7", "H1", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 543-aa sequence contains features consistent with glycoside hydrolase family 1 (GH1) beta-glucosidases: approximate length (~500-550 aa), the NEP-containing motif ('INEP' near residue ~200) indicative of the catalytic nucleophile, and overall architecture typical of the (β/α)8 TIM-barrel GH1 fold. Among the four choices, only option A is a glycoside hydrolysis reaction (substrate + H2O → aglycone + D-glucose), which is the defining reaction type of a beta-glucosidase. Options B and D are SAM-dependent methyltransferase reactions (requiring a Rossmann-like fold and entirely different catalytic mechanism), and option C is a PLP-dependent condensation (cystathionine gamma-synthase, requiring a PLP-binding fold). Thus, identifying the enzyme class from sequence features is sufficient to eliminate B, C, and D and select A.",
    "missing_item_specific_fact": "The exact substrate name 'deacetylipecoside' is protein-specific and not deducible from sequence alone; however, since option A is the only glucosidase reaction among the choices, this specificity is not required to answer the question.",
    "reason": "A model with knowledge of GH1/beta-glucosidase sequence motifs and enzyme-class–reaction-type correspondence can reason from the sequence to the correct answer without memorizing this particular UniProt entry. The reaction-type distinction (hydrolysis vs. methylation vs. PLP-dependent condensation) provides a concrete biological argument that separates the options."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only option A represents a glycoside hydrolysis reaction consistent with a beta-glucosidase. Options B and D are methyltransferase reactions and option C is a PLP-dependent reaction; none of these enzyme classes share the GH1 fold or catalytic mechanism suggested by the sequence. No ambiguity among choices."
  },
  "important_caveats": [
    "The specific substrate 'deacetylipecoside' (as opposed to other ipecoside-family glucosides) is an item-specific annotation detail; the question is answerable because it is the only glucosidase reaction listed, not because the substrate name is derivable from sequence.",
    "The UniProt entry also annotates a second activity (deacetylisoipecoside hydrolysis, RHEA:78887), but this does not create ambiguity among the provided choices since no option corresponds to that reaction.",
    "Reviewer-only evidence (UniProt annotation with experimental evidence code ECO:0000269) confirms the key; this evidence was not available to the evaluated model.",
    "The firstPublicDate of the UniProt entry is 2025-06-18, meaning the curated Swiss-Prot entry post-dates the likely benchmark construction; the underlying experimental data (PubMed:18927081, 2008) predates the benchmark, but the curated annotation may not have been available at construction time."
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

**Accession:** `B6ZKM5` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 51. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B6ZKM5.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:24.045505+00:00.  

```json
"B6ZKM5"
```

Source SHA-256: `9ce8751c9b282900ae1cfa7efc22995f02ca697466197dd0e4f4ff630319c00a`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B6ZKM5.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:24.045505+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"18927081","source":"PubMed"}],"value":"3.2.1.-"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"18927081","source":"PubMed"}],"value":"Ipecac alkaloid beta-glucosidase 3"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"18927081","source":"PubMed"}],"value":"IpeGLU3"}]}}
```

Source SHA-256: `9ce8751c9b282900ae1cfa7efc22995f02ca697466197dd0e4f4ff630319c00a`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B6ZKM5.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:24.045505+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000269","id":"18927081","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:78764"}}],"reaction":{"evidences":[{"evidenceCode":"ECO:0000269","id":"18927081","source":"PubMed"}],"name":"deacetylipecoside + H2O = deacetylipecoside aglycone + D-glucose","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:78763"},{"database":"ChEBI","id":"CHEBI:4167"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:58379"},{"database":"ChEBI","id":"CHEBI:229554"}]}}
```

Source SHA-256: `9ce8751c9b282900ae1cfa7efc22995f02ca697466197dd0e4f4ff630319c00a`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B6ZKM5.json)  
**Locator:** `/references/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:24.045505+00:00.  

```json
{"citation":{"authors":["Nomura T.","Quesada A.L.","Kutchan T.M."],"citationCrossReferences":[{"database":"PubMed","id":"18927081"},{"database":"DOI","id":"10.1074/jbc.m806953200"}],"citationType":"journal article","firstPage":"34650","id":"18927081","journal":"J. Biol. Chem.","lastPage":"34659","publicationDate":"2008","title":"The new beta-D-glucosidase in terpenoid-isoquinoline alkaloid biosynthesis in Psychotria ipecacuanha.","volume":"283"},"evidences":[{"evidenceCode":"ECO:0000312","id":"BAH02546.1","source":"EMBL"},{"evidenceCode":"ECO:0000312","id":"BAH02553.1","source":"EMBL"}],"referenceComments":[{"type":"TISSUE","value":"Root"},{"type":"TISSUE","value":"Shoot"}],"referenceNumber":1,"referencePositions":["NUCLEOTIDE SEQUENCE [MRNA]","FUNCTION","CATALYTIC ACTIVITY","PATHWAY"]}
```

Source SHA-256: `9ce8751c9b282900ae1cfa7efc22995f02ca697466197dd0e4f4ff630319c00a`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B6ZKM5?format=txt&versions=51)  
**Locator:** `lines 1-15`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 51 / 1.  
**Retrieved:** 2026-11-02T04:27:26.233250+00:00.  

```text
ID   GLU3_CARIP              Reviewed;         543 AA.
AC   B6ZKM5;
DT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.
DT   10-FEB-2009, sequence version 1.
DT   28-JAN-2026, entry version 51.
DE   RecName: Full=Ipecac alkaloid beta-glucosidase 3 {ECO:0000303|PubMed:18927081};
DE            Short=IpeGLU3 {ECO:0000303|PubMed:18927081};
DE            EC=3.2.1.- {ECO:0000269|PubMed:18927081};
GN   Name=GLU3 {ECO:0000303|PubMed:18927081};
OS   Carapichea ipecacuanha (Ipecac) (Callicocca ipecacuanha).
OC   Eukaryota; Viridiplantae; Streptophyta; Embryophyta; Tracheophyta;
OC   Spermatophyta; Magnoliopsida; eudicotyledons; Gunneridae; Pentapetalae;
OC   asterids; lamiids; Gentianales; Rubiaceae; Rubioideae; Palicoureeae;
OC   Carapichea.
OX   NCBI_TaxID=77880;
```

Source SHA-256: `d374cbcc14c195ce5c51c5fdab5300bf13d9a704c2f014bd237f3c23f917e6a7`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B6ZKM5?format=txt&versions=51)  
**Locator:** `lines 6-8`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 51 / 1.  
**Retrieved:** 2026-11-02T04:27:26.233250+00:00.  

```text
DE   RecName: Full=Ipecac alkaloid beta-glucosidase 3 {ECO:0000303|PubMed:18927081};
DE            Short=IpeGLU3 {ECO:0000303|PubMed:18927081};
DE            EC=3.2.1.- {ECO:0000269|PubMed:18927081};
```

Source SHA-256: `d374cbcc14c195ce5c51c5fdab5300bf13d9a704c2f014bd237f3c23f917e6a7`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B6ZKM5?format=txt&versions=51)  
**Locator:** `lines 27-33`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 51 / 1.  
**Retrieved:** 2026-11-02T04:27:26.233250+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=deacetylipecoside + H2O = deacetylipecoside aglycone + D-
CC         glucose; Xref=Rhea:RHEA:78763, ChEBI:CHEBI:4167, ChEBI:CHEBI:15377,
CC         ChEBI:CHEBI:58379, ChEBI:CHEBI:229554;
CC         Evidence={ECO:0000269|PubMed:18927081};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:78764;
CC         Evidence={ECO:0000269|PubMed:18927081};
```

Source SHA-256: `d374cbcc14c195ce5c51c5fdab5300bf13d9a704c2f014bd237f3c23f917e6a7`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 108. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
