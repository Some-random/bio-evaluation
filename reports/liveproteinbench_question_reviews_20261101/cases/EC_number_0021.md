# EC_number_0021

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `EC_number`  
**Author expected answer:** **D** — 5.4.99.14

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MIRLLYLLVKPAGMSDETFRAECLRHYEMSHDVPGLHKYEVRLVAEQPTDTHVPFFDIGHVDAIGECWFKDDAAYATYMASDIRKAWFEHGKTFIGQLKPFRTAPVAGDEPAS

[Multiple Choices]
A. 5.4.99.39
B. 3.1.1.80
C. 4.2.1.183
D. 5.4.99.14
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

> The supplied 113-aa sequence exactly matches the UniProt entry, which assigns EC 5.4.99.14 and describes the reaction as 4-methylmuconolactone = 3-methylmuconolactone. The annotation cites experimental evidence from two publications; those primary papers were not independently verified here.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The choices include two closely related mutase EC numbers, and the sequence alone supplies no defensible way to determine which specific substrate rearrangement this protein catalyzes.


**Missing item-specific fact**

> The protein-specific catalytic function—its experimentally characterized reaction or a reliable annotation identifying it as 4-carboxymethyl-4-methylbutenolide mutase—is not given in the question.


**Reason**

> Identifying the correct complete EC number requires the protein-specific function annotation or experimental reaction assignment. Recognizing the sequence or retrieving its database entry would be lookup, not reasoning from the supplied input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The matched-sequence annotation supports D; the choices are distinct EC numbers, and the supplied evidence does not support another option.


### Important caveats

- The reviewer-only database evidence was not available to the evaluated model.
- The actual author source snapshot is unknown; historical UniProt evidence also matches the sequence, but its timing does not establish which snapshot the author used.
- The EC annotation cites experimental publications, but their contents were not independently reviewed.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The choices include two closely related mutase EC numbers, and the sequence alone supplies no defensible way to determine which specific substrate rearrangement this protein catalyzes.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific catalytic function—its experimentally characterized reaction or a reliable annotation identifying it as 4-carboxymethyl-4-methylbutenolide mutase—is not given in the question.",
    "reason": "Identifying the correct complete EC number requires the protein-specific function annotation or experimental reaction assignment. Recognizing the sequence or retrieving its database entry would be lookup, not reasoning from the supplied input."
  },
  "case_id": "EC_number_0021",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "C7"
    ],
    "judgment": "supported",
    "reason": "The supplied 113-aa sequence exactly matches the UniProt entry, which assigns EC 5.4.99.14 and describes the reaction as 4-methylmuconolactone = 3-methylmuconolactone. The annotation cites experimental evidence from two publications; those primary papers were not independently verified here."
  },
  "important_caveats": [
    "The reviewer-only database evidence was not available to the evaluated model.",
    "The actual author source snapshot is unknown; historical UniProt evidence also matches the sequence, but its timing does not establish which snapshot the author used.",
    "The EC annotation cites experimental publications, but their contents were not independently reviewed."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched-sequence annotation supports D; the choices are distinct EC numbers, and the supplied evidence does not support another option."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0021",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied 113-aa sequence exactly matches the UniProt entry, which assigns EC 5.4.99.14 and describes the reaction as 4-methylmuconolactone = 3-methylmuconolactone. The annotation cites experimental evidence from two publications; those primary papers were not independently verified here.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "C7"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The choices include two closely related mutase EC numbers, and the sequence alone supplies no defensible way to determine which specific substrate rearrangement this protein catalyzes.",
    "missing_item_specific_fact": "The protein-specific catalytic function—its experimentally characterized reaction or a reliable annotation identifying it as 4-carboxymethyl-4-methylbutenolide mutase—is not given in the question.",
    "reason": "Identifying the correct complete EC number requires the protein-specific function annotation or experimental reaction assignment. Recognizing the sequence or retrieving its database entry would be lookup, not reasoning from the supplied input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched-sequence annotation supports D; the choices are distinct EC numbers, and the supplied evidence does not support another option."
  },
  "important_caveats": [
    "The reviewer-only database evidence was not available to the evaluated model.",
    "The actual author source snapshot is unknown; historical UniProt evidence also matches the sequence, but its timing does not establish which snapshot the author used.",
    "The EC annotation cites experimental publications, but their contents were not independently reviewed."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence matches UniProt entry O51799 (MMLI_CUPPJ, 4-carboxymethyl-4-methylbutenolide mutase) exactly (113 AA, SHA-256 match confirmed in both current and historical records). The EC number 5.4.99.14 is assigned with experimental evidence codes (ECO:0000269) from two independent publications (PubMed:2241929 and PubMed:9461415) describing purification, characterization, and catalytic activity (4-methylmuconolactone = 3-methylmuconolactone). The annotation is well-supported by experimental data.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H1](#evidence-h1), [H2](#evidence-h2), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> No concrete biological argument from the 113-residue sequence alone meaningfully distinguishes between the four choices. The sequence lacks a canonical serine hydrolase motif (GxSxG) that would support B (3.1.1.80), but absence of one motif does not exclude hydrolase activity given the diversity of esterase families. Similarly, no obvious lyase motif supports C (4.2.1.183). Critically, distinguishing A (5.4.99.39) from D (5.4.99.14) requires knowing the specific substrate (4-methylmuconolactone vs. whatever 5.4.99.39 acts upon), which is not inferable from sequence composition or general fold prediction without the specific protein's structural/functional annotation.


**Missing item-specific fact**

> The specific substrate identity (4-methylmuconolactone) and the structural/active-site features unique to 4-methylmuconolactone methylisomerase that would allow assignment of EC 5.4.99.14 over other isomerases in the 5.4.99 class. This is a protein-specific annotation derived from experimental characterization (PubMed:2241929, 9461415) that cannot be deduced from the raw sequence by general biological reasoning.


**Reason**

> The question provides only a raw amino acid sequence with no structural context, no active-site annotations, and no substrate information. The four choices span different EC classes (isomerase, hydrolase, lyase, isomerase) and within the isomerase class differ in specific reaction. No general sequence heuristic or biological reasoning pathway from this 113-AA sequence uniquely identifies 5.4.99.14. Selection requires recognizing the protein or recalling its database annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "D"
]
```

> Both 5.4.99.39 and 5.4.99.14 belong to the same EC subclass (5.4.99, other intramolecular transferases). From the sequence alone, a model could plausibly reason this is a small isomerase/mutase and then have no principled basis to choose between these two specific EC numbers. The distinction requires item-specific substrate knowledge not derivable from the sequence.


### Important caveats

- The sequence is very short (113 AA), limiting the availability of recognizable catalytic motifs or fold signatures.
- The EC annotation is experimentally supported (ECO:0000269), not merely computational, lending high confidence to the key.
- The identity of the protein (O51799) was inferred by the reviewer from dataset metadata, not provided to the evaluated model.
- The entry was first public in April 2025; depending on the benchmark construction date, the annotation may or may not have been available in training data.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "No concrete biological argument from the 113-residue sequence alone meaningfully distinguishes between the four choices. The sequence lacks a canonical serine hydrolase motif (GxSxG) that would support B (3.1.1.80), but absence of one motif does not exclude hydrolase activity given the diversity of esterase families. Similarly, no obvious lyase motif supports C (4.2.1.183). Critically, distinguishing A (5.4.99.39) from D (5.4.99.14) requires knowing the specific substrate (4-methylmuconolactone vs. whatever 5.4.99.39 acts upon), which is not inferable from sequence composition or general fold prediction without the specific protein's structural/functional annotation.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific substrate identity (4-methylmuconolactone) and the structural/active-site features unique to 4-methylmuconolactone methylisomerase that would allow assignment of EC 5.4.99.14 over other isomerases in the 5.4.99 class. This is a protein-specific annotation derived from experimental characterization (PubMed:2241929, 9461415) that cannot be deduced from the raw sequence by general biological reasoning.",
    "reason": "The question provides only a raw amino acid sequence with no structural context, no active-site annotations, and no substrate information. The four choices span different EC classes (isomerase, hydrolase, lyase, isomerase) and within the isomerase class differ in specific reaction. No general sequence heuristic or biological reasoning pathway from this 113-AA sequence uniquely identifies 5.4.99.14. Selection requires recognizing the protein or recalling its database annotation."
  },
  "case_id": "EC_number_0021",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C7",
      "H1",
      "H2",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The sequence matches UniProt entry O51799 (MMLI_CUPPJ, 4-carboxymethyl-4-methylbutenolide mutase) exactly (113 AA, SHA-256 match confirmed in both current and historical records). The EC number 5.4.99.14 is assigned with experimental evidence codes (ECO:0000269) from two independent publications (PubMed:2241929 and PubMed:9461415) describing purification, characterization, and catalytic activity (4-methylmuconolactone = 3-methylmuconolactone). The annotation is well-supported by experimental data."
  },
  "important_caveats": [
    "The sequence is very short (113 AA), limiting the availability of recognizable catalytic motifs or fold signatures.",
    "The EC annotation is experimentally supported (ECO:0000269), not merely computational, lending high confidence to the key.",
    "The identity of the protein (O51799) was inferred by the reviewer from dataset metadata, not provided to the evaluated model.",
    "The entry was first public in April 2025; depending on the benchmark construction date, the annotation may or may not have been available in training data."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "D"
    ],
    "reason": "Both 5.4.99.39 and 5.4.99.14 belong to the same EC subclass (5.4.99, other intramolecular transferases). From the sequence alone, a model could plausibly reason this is a small isomerase/mutase and then have no principled basis to choose between these two specific EC numbers. The distinction requires item-specific substrate knowledge not derivable from the sequence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0021",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches UniProt entry O51799 (MMLI_CUPPJ, 4-carboxymethyl-4-methylbutenolide mutase) exactly (113 AA, SHA-256 match confirmed in both current and historical records). The EC number 5.4.99.14 is assigned with experimental evidence codes (ECO:0000269) from two independent publications (PubMed:2241929 and PubMed:9461415) describing purification, characterization, and catalytic activity (4-methylmuconolactone = 3-methylmuconolactone). The annotation is well-supported by experimental data.",
    "evidence_ids": ["C4", "C5", "C6", "C7", "H1", "H2", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "No concrete biological argument from the 113-residue sequence alone meaningfully distinguishes between the four choices. The sequence lacks a canonical serine hydrolase motif (GxSxG) that would support B (3.1.1.80), but absence of one motif does not exclude hydrolase activity given the diversity of esterase families. Similarly, no obvious lyase motif supports C (4.2.1.183). Critically, distinguishing A (5.4.99.39) from D (5.4.99.14) requires knowing the specific substrate (4-methylmuconolactone vs. whatever 5.4.99.39 acts upon), which is not inferable from sequence composition or general fold prediction without the specific protein's structural/functional annotation.",
    "missing_item_specific_fact": "The specific substrate identity (4-methylmuconolactone) and the structural/active-site features unique to 4-methylmuconolactone methylisomerase that would allow assignment of EC 5.4.99.14 over other isomerases in the 5.4.99 class. This is a protein-specific annotation derived from experimental characterization (PubMed:2241929, 9461415) that cannot be deduced from the raw sequence by general biological reasoning.",
    "reason": "The question provides only a raw amino acid sequence with no structural context, no active-site annotations, and no substrate information. The four choices span different EC classes (isomerase, hydrolase, lyase, isomerase) and within the isomerase class differ in specific reaction. No general sequence heuristic or biological reasoning pathway from this 113-AA sequence uniquely identifies 5.4.99.14. Selection requires recognizing the protein or recalling its database annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "D"],
    "reason": "Both 5.4.99.39 and 5.4.99.14 belong to the same EC subclass (5.4.99, other intramolecular transferases). From the sequence alone, a model could plausibly reason this is a small isomerase/mutase and then have no principled basis to choose between these two specific EC numbers. The distinction requires item-specific substrate knowledge not derivable from the sequence."
  },
  "important_caveats": [
    "The sequence is very short (113 AA), limiting the availability of recognizable catalytic motifs or fold signatures.",
    "The EC annotation is experimentally supported (ECO:0000269), not merely computational, lending high confidence to the key.",
    "The identity of the protein (O51799) was inferred by the reviewer from dataset metadata, not provided to the evaluated model.",
    "The entry was first public in April 2025; depending on the benchmark construction date, the annotation may or may not have been available in training data."
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

**Accession:** `O51799` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 65. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O51799.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:12.163444+00:00.  

```json
"O51799"
```

Source SHA-256: `b70c681e56806aa898c9fb39f2f630921678c753acd190c1b04d04bedc7c3968`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O51799.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:12.163444+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"2241929","source":"PubMed"}],"value":"4-carboxymethyl-4-methylbut-2-en-4-olide isomerase"}},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"2241929","source":"PubMed"}],"value":"4-methyl-2-enelactone isomerase"}},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"2241929","source":"PubMed"},{"evidenceCode":"ECO:0000303","id":"9461415","source":"PubMed"}],"value":"4-methylmuconolactone methylisomerase"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"9461415","source":"PubMed"}],"value":"MLMI"}]}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"2241929","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"9461415","source":"PubMed"}],"value":"5.4.99.14"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"4-carboxymethyl-4-methylbutenolide mutase"}}}
```

Source SHA-256: `b70c681e56806aa898c9fb39f2f630921678c753acd190c1b04d04bedc7c3968`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O51799.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:12.163444+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000269","id":"2241929","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"9461415","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:19238"}}],"reaction":{"ecNumber":"5.4.99.14","evidences":[{"evidenceCode":"ECO:0000269","id":"2241929","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"9461415","source":"PubMed"}],"name":"4-methylmuconolactone = 3-methylmuconolactone","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:19237"},{"database":"ChEBI","id":"CHEBI:57883"},{"database":"ChEBI","id":"CHEBI:57888"}]}}
```

Source SHA-256: `b70c681e56806aa898c9fb39f2f630921678c753acd190c1b04d04bedc7c3968`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O51799.json)  
**Locator:** `/references/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:12.163444+00:00.  

```json
{"citation":{"authors":["Erb R.W.","Timmis K.N.","Pieper D.H."],"citationCrossReferences":[{"database":"PubMed","id":"9461415"},{"database":"DOI","id":"10.1016/s0378-1119(97)00565-9"}],"citationType":"journal article","firstPage":"53","id":"9461415","journal":"Gene","lastPage":"62","publicationDate":"1998","title":"Characterization of a gene cluster from Ralstonia eutropha JMP134 encoding metabolism of 4-methylmuconolactone.","volume":"206"},"evidences":[{"evidenceCode":"ECO:0000312","id":"CAA67958.1","source":"EMBL"}],"referenceComments":[{"type":"STRAIN","value":"JMP134 / LMG 1197"}],"referenceNumber":1,"referencePositions":["NUCLEOTIDE SEQUENCE [GENOMIC DNA]","FUNCTION","CATALYTIC ACTIVITY","SUBUNIT"]}
```

Source SHA-256: `b70c681e56806aa898c9fb39f2f630921678c753acd190c1b04d04bedc7c3968`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O51799.json)  
**Locator:** `/references/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:12.163444+00:00.  

```json
{"citation":{"authors":["Pieper D.H.","Stadler-Fritzsche K.","Knackmuss H.J.","Engesser K.H.","Bruce N.C.","Cain R.B."],"citationCrossReferences":[{"database":"PubMed","id":"2241929"},{"database":"DOI","id":"10.1042/bj2710529"}],"citationType":"journal article","firstPage":"529","id":"2241929","journal":"Biochem. J.","lastPage":"534","publicationDate":"1990","title":"Purification and characterization of 4-methylmuconolactone methylisomerase, a novel enzyme of the modified 3-oxoadipate pathway in the gram-negative bacterium Alcaligenes eutrophus JMP 134.","volume":"271"},"referenceComments":[{"type":"STRAIN","value":"JMP134 / LMG 1197"}],"referenceNumber":3,"referencePositions":["FUNCTION","CATALYTIC ACTIVITY","ACTIVITY REGULATION","BIOPHYSICOCHEMICAL PROPERTIES"]}
```

Source SHA-256: `b70c681e56806aa898c9fb39f2f630921678c753acd190c1b04d04bedc7c3968`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O51799?format=txt&versions=65)  
**Locator:** `lines 1-18`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 65 / 1.  
**Retrieved:** 2026-11-01T06:28:15.847605+00:00.  

```text
ID   MMLI_CUPPJ              Reviewed;         113 AA.
AC   O51799; Q471R3;
DT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.
DT   01-JUN-1998, sequence version 1.
DT   28-JAN-2026, entry version 65.
DE   RecName: Full=4-carboxymethyl-4-methylbutenolide mutase {ECO:0000305};
DE            EC=5.4.99.14 {ECO:0000269|PubMed:2241929, ECO:0000269|PubMed:9461415};
DE   AltName: Full=4-carboxymethyl-4-methylbut-2-en-4-olide isomerase {ECO:0000303|PubMed:2241929};
DE   AltName: Full=4-methyl-2-enelactone isomerase {ECO:0000303|PubMed:2241929};
DE   AltName: Full=4-methylmuconolactone methylisomerase {ECO:0000303|PubMed:2241929, ECO:0000303|PubMed:9461415};
DE            Short=MLMI {ECO:0000303|PubMed:9461415};
GN   Name=mmlI {ECO:0000303|PubMed:9461415};
GN   OrderedLocusNames=Reut_A1503 {ECO:0000312|EMBL:AAZ60870.1};
OS   Cupriavidus pinatubonensis (strain JMP 134 / LMG 1197) (Cupriavidus necator
OS   (strain JMP 134)).
OC   Bacteria; Pseudomonadati; Pseudomonadota; Betaproteobacteria;
OC   Burkholderiales; Burkholderiaceae; Cupriavidus.
OX   NCBI_TaxID=264198;
```

Source SHA-256: `1fb5ec02f51833bc2a3a34baeeee4fa6645485da2ba66876fa2f98e7c8ee89ac`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O51799?format=txt&versions=65)  
**Locator:** `lines 6-11`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 65 / 1.  
**Retrieved:** 2026-11-01T06:28:15.847605+00:00.  

```text
DE   RecName: Full=4-carboxymethyl-4-methylbutenolide mutase {ECO:0000305};
DE            EC=5.4.99.14 {ECO:0000269|PubMed:2241929, ECO:0000269|PubMed:9461415};
DE   AltName: Full=4-carboxymethyl-4-methylbut-2-en-4-olide isomerase {ECO:0000303|PubMed:2241929};
DE   AltName: Full=4-methyl-2-enelactone isomerase {ECO:0000303|PubMed:2241929};
DE   AltName: Full=4-methylmuconolactone methylisomerase {ECO:0000303|PubMed:2241929, ECO:0000303|PubMed:9461415};
DE            Short=MLMI {ECO:0000303|PubMed:9461415};
```

Source SHA-256: `1fb5ec02f51833bc2a3a34baeeee4fa6645485da2ba66876fa2f98e7c8ee89ac`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O51799?format=txt&versions=65)  
**Locator:** `lines 38-48`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 65 / 1.  
**Retrieved:** 2026-11-01T06:28:15.847605+00:00.  

```text
RN   [3]
RP   FUNCTION, CATALYTIC ACTIVITY, ACTIVITY REGULATION, AND BIOPHYSICOCHEMICAL
RP   PROPERTIES.
RC   STRAIN=JMP134 / LMG 1197;
RX   PubMed=2241929; DOI=10.1042/bj2710529;
RA   Pieper D.H., Stadler-Fritzsche K., Knackmuss H.J., Engesser K.H.,
RA   Bruce N.C., Cain R.B.;
RT   "Purification and characterization of 4-methylmuconolactone
RT   methylisomerase, a novel enzyme of the modified 3-oxoadipate pathway in the
RT   gram-negative bacterium Alcaligenes eutrophus JMP 134.";
RL   Biochem. J. 271:529-534(1990).
```

Source SHA-256: `1fb5ec02f51833bc2a3a34baeeee4fa6645485da2ba66876fa2f98e7c8ee89ac`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O51799?format=txt&versions=65)  
**Locator:** `lines 64-70`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 65 / 1.  
**Retrieved:** 2026-11-01T06:28:15.847605+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=4-methylmuconolactone = 3-methylmuconolactone;
CC         Xref=Rhea:RHEA:19237, ChEBI:CHEBI:57883, ChEBI:CHEBI:57888;
CC         EC=5.4.99.14; Evidence={ECO:0000269|PubMed:2241929,
CC         ECO:0000269|PubMed:9461415};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:19238;
CC         Evidence={ECO:0000269|PubMed:2241929, ECO:0000269|PubMed:9461415};
```

Source SHA-256: `1fb5ec02f51833bc2a3a34baeeee4fa6645485da2ba66876fa2f98e7c8ee89ac`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 21. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
