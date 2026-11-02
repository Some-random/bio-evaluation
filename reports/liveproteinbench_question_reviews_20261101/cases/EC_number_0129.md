# EC_number_0129

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `EC_number`  
**Author expected answer:** **C** — 5.3.99.13

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MQTYLSTKSIEYYLKELKEIFSQIWLKPSEIEKRCEELFKRSKEFDYKRILVSGETDNTTLYVIEDSSKIHVFSPNRDLRENPLLMRWHPSWYEIESKEIYYKCFLSCEELYEHLELPTVTLVNLCVIENFPIPRLNLSTGTLSSYLRKEQLAKVELIDMQVGTTINQIIKNLLDSQPDIIGLSVNFGQKKLAFEILDLIYSHIENGDLSSIITVGNVIPSFSPEQFFERYPSLLICDKEGEYTLRDLIKMLKKELKLDEVNGISYVDESGEVKHNVAETVNFKEEVPTPSLDILGEISKFRGALTLETSRGCDYSRCTFCPRDHKLRSWRPLSVEQTLKQLDDILRAGKHFNIKPHIYMADEEFIGELPNGTEAQRIIDICEGLLKREEKIKFDFAARADSVYEPKRTKEWNVERLKMWHYCALAGADRIFIGVESGSNQQLKRYGKGTTSEQNIIALRLVSALGINLRIGFIMFDQLMKGLDNLKENLDFLERTDALMKPIDIGDMTYEELYDKLLNDKEFIEKHKTGKPVYTIVSYMLASMEILMNTPYSRMVQLTERKEEVNLIMNDGKPDMNMGRYATSFVDKTNGNLSEACQMWIDSNFGVMYTIKSLHKVANPREKKKLYSYMETHREISHFLLKYLVYNLSPDKESQIILSDFLRMHSMEHILDNSKINVGDGSKENILNVMTNWQLIMEKLLRDVEADLNKGIITDSEDHRLHNTLKRWFSDMGNWSLINAYELN

[Multiple Choices]
A. 5.3.1.8
B. 2.3.1.312
C. 5.3.99.13
D. 2.3.1.290
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

> The exact 744-aa sequence matches UniProt O24770. Its archived entry assigns EC 5.3.99.13 and cites experimental evidence for the catalytic activity; the current entry reports the same assignment. This supports choice C, while noting that the cited papers were not independently reviewed here.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H6](#evidence-h6).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence may suggest a radical-SAM enzyme, but that broad family-level inference does not establish the specific reaction or EC subclass needed to select 5.3.99.13 over the other choices.


**Missing item-specific fact**

> The protein-specific catalytic activity—dAMP conversion to 4'-phospho-dehydrooxetanocin, established by experimental annotation and cited studies—is not supplied in the question.


**Reason**

> The sequence and choices alone do not provide a sufficiently specific basis for assigning this exact EC number; selecting it depends on protein-specific functional knowledge or external annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The evidence supports one listed EC number, 5.3.99.13; no other choice is supported by the supplied reviewer evidence.


### Important caveats

- Reviewer-only database evidence establishes support for the key but was not available to the evaluated model.
- The accession was inferred by reviewers; the exact sequence match is confirmed for both the archived and current UniProt records, but the author's source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence may suggest a radical-SAM enzyme, but that broad family-level inference does not establish the specific reaction or EC subclass needed to select 5.3.99.13 over the other choices.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific catalytic activity—dAMP conversion to 4'-phospho-dehydrooxetanocin, established by experimental annotation and cited studies—is not supplied in the question.",
    "reason": "The sequence and choices alone do not provide a sufficiently specific basis for assigning this exact EC number; selecting it depends on protein-specific functional knowledge or external annotation."
  },
  "case_id": "EC_number_0129",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H2",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The exact 744-aa sequence matches UniProt O24770. Its archived entry assigns EC 5.3.99.13 and cites experimental evidence for the catalytic activity; the current entry reports the same assignment. This supports choice C, while noting that the cited papers were not independently reviewed here."
  },
  "important_caveats": [
    "Reviewer-only database evidence establishes support for the key but was not available to the evaluated model.",
    "The accession was inferred by reviewers; the exact sequence match is confirmed for both the archived and current UniProt records, but the author's source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The evidence supports one listed EC number, 5.3.99.13; no other choice is supported by the supplied reviewer evidence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0129",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact 744-aa sequence matches UniProt O24770. Its archived entry assigns EC 5.3.99.13 and cites experimental evidence for the catalytic activity; the current entry reports the same assignment. This supports choice C, while noting that the cited papers were not independently reviewed here.",
    "evidence_ids": ["C1", "C4", "C5", "H2", "H6"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence may suggest a radical-SAM enzyme, but that broad family-level inference does not establish the specific reaction or EC subclass needed to select 5.3.99.13 over the other choices.",
    "missing_item_specific_fact": "The protein-specific catalytic activity—dAMP conversion to 4'-phospho-dehydrooxetanocin, established by experimental annotation and cited studies—is not supplied in the question.",
    "reason": "The sequence and choices alone do not provide a sufficiently specific basis for assigning this exact EC number; selecting it depends on protein-specific functional knowledge or external annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The evidence supports one listed EC number, 5.3.99.13; no other choice is supported by the supplied reviewer evidence."
  },
  "important_caveats": [
    "Reviewer-only database evidence establishes support for the key but was not available to the evaluated model.",
    "The accession was inferred by reviewers; the exact sequence match is confirmed for both the archived and current UniProt records, but the author's source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence matches UniProt O24770 (OXSB_PRIMG, 4'-phospho-dehydrooxetanocin synthase / OxsB) from Priestia megaterium. The EC number 5.3.99.13 is assigned with ECO:0000269 (inferred from direct assay) evidence from PubMed:28346939 (Nature 2017, X-ray crystallography at 1.8 Å with &#91;4Fe-4S&#93; cluster, cob(II)alamin, and SAM; PDB 5UL2/5UL3/5UL4) and PubMed:33560833 (Biochemistry 2021, biochemical characterization). The catalytic reaction (dAMP → 4'-phospho-dehydrooxetanocin via oxidative ring contraction, a radical SAM/B12-dependent isomerization) is experimentally validated. The sequence is a perfect match (SHA-256 identical, 744 aa, sequence version 1).

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C9](#evidence-c9), [H1](#evidence-h1), [H2](#evidence-h2), [H5](#evidence-h5), [H6](#evidence-h6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a recognizable radical SAM CX3CX2C motif (C-D-Y-S-C-T-C at ~residues 295–301, within 'CDYSRCTFCPRDHKLRSWRPLS'), indicating a &#91;4Fe-4S&#93; cluster-binding radical SAM enzyme. Radical SAM enzymes catalyze radical-mediated bond rearrangements (isomerizations, ring contractions/expansions), not group transfers, which eliminates the two transferase options (B: 2.3.1.312 and D: 2.3.1.290). The protein is 744 aa with multiple domain insertions (B12-binding domain, extended SAM-binding region), far exceeding the ~250 aa TIM-barrel homodimer of triose-phosphate isomerase (A: 5.3.1.8), eliminating that option. The only remaining choice is C (5.3.99.13), a catch-all isomerase entry for unusual intramolecular oxidoreductases—consistent with a radical SAM-mediated ring contraction.


**Missing item-specific fact**

> None strictly required for elimination. However, positively confirming the exact EC number 5.3.99.13 (vs. any other 5.3.99.x entry) would require knowing the specific oxetanocin biosynthesis reaction, which is not derivable from sequence alone. The answer is determined here by process of elimination among the four provided choices.


**Reason**

> A knowledgeable model can identify the radical SAM motif, recognize that radical SAM enzymes are not transferases, and note the implausible size/architecture for TIM. This eliminates three of four choices through general enzymology knowledge. The reasoning is valid but somewhat contingent on the answer set construction (only one 5.3.99.x option is offered).


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options span two EC classes (isomerases 5.3.x.x vs. transferases 2.3.x.x) and include one highly recognizable enzyme (TIM). The radical SAM motif and domain architecture provide clear grounds to eliminate all but C. No other option is defensible given the sequence features.


### Important caveats

- The specific EC number 5.3.99.13 was assigned based on experimental characterization (2017 Nature, 2021 Biochemistry) of the oxetanocin A biosynthetic pathway; it is an extremely recent and obscure entry. Positive identification of this exact number from sequence alone is not feasible—only elimination from the given choices works.
- The radical SAM CX3CX2C motif identification in a 744-aa sequence requires familiarity with the superfamily and is non-trivial for a model without domain knowledge, though it is a recognized general-biology reasoning step.
- The reasoning chain 'radical SAM → not a transferase' is broadly correct but not universally true (some radical SAM enzymes have transfer-like chemistry); the elimination holds here because the specific alternatives are clearly incompatible.
- The reviewer-only evidence confirms the key but was not available to the evaluated model; the model must rely solely on sequence analysis and general knowledge.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a recognizable radical SAM CX3CX2C motif (C-D-Y-S-C-T-C at ~residues 295–301, within 'CDYSRCTFCPRDHKLRSWRPLS'), indicating a [4Fe-4S] cluster-binding radical SAM enzyme. Radical SAM enzymes catalyze radical-mediated bond rearrangements (isomerizations, ring contractions/expansions), not group transfers, which eliminates the two transferase options (B: 2.3.1.312 and D: 2.3.1.290). The protein is 744 aa with multiple domain insertions (B12-binding domain, extended SAM-binding region), far exceeding the ~250 aa TIM-barrel homodimer of triose-phosphate isomerase (A: 5.3.1.8), eliminating that option. The only remaining choice is C (5.3.99.13), a catch-all isomerase entry for unusual intramolecular oxidoreductases—consistent with a radical SAM-mediated ring contraction.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None strictly required for elimination. However, positively confirming the exact EC number 5.3.99.13 (vs. any other 5.3.99.x entry) would require knowing the specific oxetanocin biosynthesis reaction, which is not derivable from sequence alone. The answer is determined here by process of elimination among the four provided choices.",
    "reason": "A knowledgeable model can identify the radical SAM motif, recognize that radical SAM enzymes are not transferases, and note the implausible size/architecture for TIM. This eliminates three of four choices through general enzymology knowledge. The reasoning is valid but somewhat contingent on the answer set construction (only one 5.3.99.x option is offered)."
  },
  "case_id": "EC_number_0129",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C9",
      "H1",
      "H2",
      "H5",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The sequence matches UniProt O24770 (OXSB_PRIMG, 4'-phospho-dehydrooxetanocin synthase / OxsB) from Priestia megaterium. The EC number 5.3.99.13 is assigned with ECO:0000269 (inferred from direct assay) evidence from PubMed:28346939 (Nature 2017, X-ray crystallography at 1.8 Å with [4Fe-4S] cluster, cob(II)alamin, and SAM; PDB 5UL2/5UL3/5UL4) and PubMed:33560833 (Biochemistry 2021, biochemical characterization). The catalytic reaction (dAMP → 4'-phospho-dehydrooxetanocin via oxidative ring contraction, a radical SAM/B12-dependent isomerization) is experimentally validated. The sequence is a perfect match (SHA-256 identical, 744 aa, sequence version 1)."
  },
  "important_caveats": [
    "The specific EC number 5.3.99.13 was assigned based on experimental characterization (2017 Nature, 2021 Biochemistry) of the oxetanocin A biosynthetic pathway; it is an extremely recent and obscure entry. Positive identification of this exact number from sequence alone is not feasible—only elimination from the given choices works.",
    "The radical SAM CX3CX2C motif identification in a 744-aa sequence requires familiarity with the superfamily and is non-trivial for a model without domain knowledge, though it is a recognized general-biology reasoning step.",
    "The reasoning chain 'radical SAM → not a transferase' is broadly correct but not universally true (some radical SAM enzymes have transfer-like chemistry); the elimination holds here because the specific alternatives are clearly incompatible.",
    "The reviewer-only evidence confirms the key but was not available to the evaluated model; the model must rely solely on sequence analysis and general knowledge."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span two EC classes (isomerases 5.3.x.x vs. transferases 2.3.x.x) and include one highly recognizable enzyme (TIM). The radical SAM motif and domain architecture provide clear grounds to eliminate all but C. No other option is defensible given the sequence features."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0129",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches UniProt O24770 (OXSB_PRIMG, 4'-phospho-dehydrooxetanocin synthase / OxsB) from Priestia megaterium. The EC number 5.3.99.13 is assigned with ECO:0000269 (inferred from direct assay) evidence from PubMed:28346939 (Nature 2017, X-ray crystallography at 1.8 Å with [4Fe-4S] cluster, cob(II)alamin, and SAM; PDB 5UL2/5UL3/5UL4) and PubMed:33560833 (Biochemistry 2021, biochemical characterization). The catalytic reaction (dAMP → 4'-phospho-dehydrooxetanocin via oxidative ring contraction, a radical SAM/B12-dependent isomerization) is experimentally validated. The sequence is a perfect match (SHA-256 identical, 744 aa, sequence version 1).",
    "evidence_ids": ["C1", "C4", "C5", "C9", "H1", "H2", "H5", "H6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a recognizable radical SAM CX3CX2C motif (C-D-Y-S-C-T-C at ~residues 295–301, within 'CDYSRCTFCPRDHKLRSWRPLS'), indicating a [4Fe-4S] cluster-binding radical SAM enzyme. Radical SAM enzymes catalyze radical-mediated bond rearrangements (isomerizations, ring contractions/expansions), not group transfers, which eliminates the two transferase options (B: 2.3.1.312 and D: 2.3.1.290). The protein is 744 aa with multiple domain insertions (B12-binding domain, extended SAM-binding region), far exceeding the ~250 aa TIM-barrel homodimer of triose-phosphate isomerase (A: 5.3.1.8), eliminating that option. The only remaining choice is C (5.3.99.13), a catch-all isomerase entry for unusual intramolecular oxidoreductases—consistent with a radical SAM-mediated ring contraction.",
    "missing_item_specific_fact": "None strictly required for elimination. However, positively confirming the exact EC number 5.3.99.13 (vs. any other 5.3.99.x entry) would require knowing the specific oxetanocin biosynthesis reaction, which is not derivable from sequence alone. The answer is determined here by process of elimination among the four provided choices.",
    "reason": "A knowledgeable model can identify the radical SAM motif, recognize that radical SAM enzymes are not transferases, and note the implausible size/architecture for TIM. This eliminates three of four choices through general enzymology knowledge. The reasoning is valid but somewhat contingent on the answer set construction (only one 5.3.99.x option is offered)."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span two EC classes (isomerases 5.3.x.x vs. transferases 2.3.x.x) and include one highly recognizable enzyme (TIM). The radical SAM motif and domain architecture provide clear grounds to eliminate all but C. No other option is defensible given the sequence features."
  },
  "important_caveats": [
    "The specific EC number 5.3.99.13 was assigned based on experimental characterization (2017 Nature, 2021 Biochemistry) of the oxetanocin A biosynthetic pathway; it is an extremely recent and obscure entry. Positive identification of this exact number from sequence alone is not feasible—only elimination from the given choices works.",
    "The radical SAM CX3CX2C motif identification in a 744-aa sequence requires familiarity with the superfamily and is non-trivial for a model without domain knowledge, though it is a recognized general-biology reasoning step.",
    "The reasoning chain 'radical SAM → not a transferase' is broadly correct but not universally true (some radical SAM enzymes have transfer-like chemistry); the elimination holds here because the specific alternatives are clearly incompatible.",
    "The reviewer-only evidence confirms the key but was not available to the evaluated model; the model must rely solely on sequence analysis and general knowledge."
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

**Accession:** `O24770` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 90. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O24770.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:11.085784+00:00.  

```json
"O24770"
```

Source SHA-256: `0a5df96f640199749015b4999d23075d213421b74b01cf0009b796669ee43c47`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O24770.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:11.085784+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"28346939","source":"PubMed"}],"value":"Cobalamin-dependent S-adenosylmethionine radical enzyme OxsB"}},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"dAMP isomerase (4'-phospho-dehydrooxetanocin-forming)"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"28346939","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"33560833","source":"PubMed"}],"value":"5.3.99.13"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"4'-phospho-dehydrooxetanocin synthase"}}}
```

Source SHA-256: `0a5df96f640199749015b4999d23075d213421b74b01cf0009b796669ee43c47`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O24770.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:11.085784+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000269","id":"28346939","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"33560833","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:81408"}}],"reaction":{"ecNumber":"5.3.99.13","evidences":[{"evidenceCode":"ECO:0000269","id":"28346939","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"33560833","source":"PubMed"}],"name":"dAMP + S-adenosyl-L-methionine = 4'-phospho-dehydrooxetanocin + 5'-deoxyadenosine + L-methionine + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:81407"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:17319"},{"database":"ChEBI","id":"CHEBI:57844"},{"database":"ChEBI","id":"CHEBI:58245"},{"database":"ChEBI","id":"CHEBI:59789"},{"database":"ChEBI","id":"CHEBI:231877"}]}}
```

Source SHA-256: `0a5df96f640199749015b4999d23075d213421b74b01cf0009b796669ee43c47`.

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O24770.json)  
**Locator:** `/references/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:11.085784+00:00.  

```json
{"citation":{"authors":["Bridwell-Rabb J.","Zhong A.","Sun H.G.","Drennan C.L.","Liu H.W."],"citationCrossReferences":[{"database":"PubMed","id":"28346939"},{"database":"DOI","id":"10.1038/nature21689"}],"citationType":"journal article","firstPage":"322","id":"28346939","journal":"Nature","lastPage":"326","publicationDate":"2017","title":"A B12-dependent radical SAM enzyme involved in oxetanocin A biosynthesis.","volume":"544"},"evidences":[{"evidenceCode":"ECO:0007744","id":"5UL2","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"5UL3","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"5UL4","source":"PDB"}],"referenceNumber":4,"referencePositions":["X-RAY CRYSTALLOGRAPHY (1.80 ANGSTROMS) IN COMPLEXES WITH [4FE-4S] CLUSTER; COB(II)ALAMIN AND S-ADENOSYL-L-METHIONINE","FUNCTION","CATALYTIC ACTIVITY","COFACTOR","ACTIVITY REGULATION","DOMAIN"]}
```

Source SHA-256: `0a5df96f640199749015b4999d23075d213421b74b01cf0009b796669ee43c47`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O24770?format=txt&versions=90)  
**Locator:** `lines 1-14`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 90 / 1.  
**Retrieved:** 2026-11-02T04:29:15.786314+00:00.  

```text
ID   OXSB_PRIMG              Reviewed;         744 AA.
AC   O24770;
DT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.
DT   01-JAN-1998, sequence version 1.
DT   28-JAN-2026, entry version 90.
DE   RecName: Full=4'-phospho-dehydrooxetanocin synthase {ECO:0000305};
DE            EC=5.3.99.13 {ECO:0000269|PubMed:28346939, ECO:0000269|PubMed:33560833};
DE   AltName: Full=Cobalamin-dependent S-adenosylmethionine radical enzyme OxsB {ECO:0000303|PubMed:28346939};
DE   AltName: Full=dAMP isomerase (4'-phospho-dehydrooxetanocin-forming) {ECO:0000305};
GN   Name=oxsB {ECO:0000312|EMBL:BAA21631.1};
OS   Priestia megaterium (Bacillus megaterium).
OG   Plasmid pOXT1 {ECO:0000303|PubMed:10227144}.
OC   Bacteria; Bacillati; Bacillota; Bacilli; Bacillales; Bacillaceae; Priestia.
OX   NCBI_TaxID=1404;
```

Source SHA-256: `74d13584dd5e362c68994158dea31c83d3658cc87b7425d894b542313b4c08cc`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O24770?format=txt&versions=90)  
**Locator:** `lines 6-9`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 90 / 1.  
**Retrieved:** 2026-11-02T04:29:15.786314+00:00.  

```text
DE   RecName: Full=4'-phospho-dehydrooxetanocin synthase {ECO:0000305};
DE            EC=5.3.99.13 {ECO:0000269|PubMed:28346939, ECO:0000269|PubMed:33560833};
DE   AltName: Full=Cobalamin-dependent S-adenosylmethionine radical enzyme OxsB {ECO:0000303|PubMed:28346939};
DE   AltName: Full=dAMP isomerase (4'-phospho-dehydrooxetanocin-forming) {ECO:0000305};
```

Source SHA-256: `74d13584dd5e362c68994158dea31c83d3658cc87b7425d894b542313b4c08cc`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O24770?format=txt&versions=90)  
**Locator:** `lines 39-47`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 90 / 1.  
**Retrieved:** 2026-11-02T04:29:15.786314+00:00.  

```text
RN   [4] {ECO:0007744|PDB:5UL2, ECO:0007744|PDB:5UL3, ECO:0007744|PDB:5UL4}
RP   X-RAY CRYSTALLOGRAPHY (1.80 ANGSTROMS) IN COMPLEXES WITH [4FE-4S] CLUSTER;
RP   COB(II)ALAMIN AND S-ADENOSYL-L-METHIONINE, FUNCTION, CATALYTIC ACTIVITY,
RP   COFACTOR, ACTIVITY REGULATION, AND DOMAIN.
RX   PubMed=28346939; DOI=10.1038/nature21689;
RA   Bridwell-Rabb J., Zhong A., Sun H.G., Drennan C.L., Liu H.W.;
RT   "A B12-dependent radical SAM enzyme involved in oxetanocin A
RT   biosynthesis.";
RL   Nature 544:322-326(2017).
```

Source SHA-256: `74d13584dd5e362c68994158dea31c83d3658cc87b7425d894b542313b4c08cc`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O24770?format=txt&versions=90)  
**Locator:** `lines 59-67`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 90 / 1.  
**Retrieved:** 2026-11-02T04:29:15.786314+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=dAMP + S-adenosyl-L-methionine = 4'-phospho-dehydrooxetanocin
CC         + 5'-deoxyadenosine + L-methionine + H(+); Xref=Rhea:RHEA:81407,
CC         ChEBI:CHEBI:15378, ChEBI:CHEBI:17319, ChEBI:CHEBI:57844,
CC         ChEBI:CHEBI:58245, ChEBI:CHEBI:59789, ChEBI:CHEBI:231877;
CC         EC=5.3.99.13; Evidence={ECO:0000269|PubMed:28346939,
CC         ECO:0000269|PubMed:33560833};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:81408;
CC         Evidence={ECO:0000269|PubMed:28346939, ECO:0000269|PubMed:33560833};
```

Source SHA-256: `74d13584dd5e362c68994158dea31c83d3658cc87b7425d894b542313b4c08cc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 129. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
