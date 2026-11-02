# EC_number_0002

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `EC_number`  
**Author expected answer:** **C** — 1.97.1.14

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | invalid_review |

**Paired comparison:** not comparable: one or both reviews invalid or missing. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MLKKLYFTVLSFIAIVGVISLYIRLSEGMKMSALTSYSSWGLWIVFYIYFIGLSAGSFLLSTMVYVFNMKQFERIGKLALFTAFFSLMAGLLFVLIDLGHPERFWHTLVYRQPNSILSWEIQFYLIYMLLIVAEIWFLMREEFAQRAQSTKGLTKLFNRTLTLGYKVPNSQQKLEFHREQSHKWMKILGIAGIPTAVGVHGGTGSLFGVVMAKEYWFSGLTPIIFLVSALVSGAALMLFLYSFFGGAKKNGDSLLKELGTLLTLFIGIDLLLMIAEFLIGLYNPIHHERMTFNEILFGDRWFIFWIGQIGMVIILPILLITISKGKRLLMGLAGLSVVLGIVCVRWILVIPAYVAPHFDGLDSAYNSSRLLYEYSPNLLEWSSSVGLIGIVILLFSITVQLVPVFNKQKEVHQTHGKPTPEIHIKA

[Multiple Choices]
A. 1.97.1.13
B. 1.5.1.38
C. 1.97.1.14
D. 1.14.19.80
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

> The supplied sequence exactly matches the UniProt entry for selenate reductase subunit C, annotated with EC 1.97.1.14 and a selenate-reductase reaction. The annotation cites a study describing the respiratory selenate reductase complex. This supports choice C as the assigned EC number, though it does not establish that this membrane-anchor subunit alone catalyzes the reaction.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The strongly hydrophobic sequence is consistent with a multi-pass membrane protein, but that broad feature does not identify the specific selenate-reductase complex or distinguish its exact EC number from the alternatives.


**Missing item-specific fact**

> The protein-specific annotation identifying this sequence as subunit C of the selenate reductase complex and assigning that complex EC 1.97.1.14.


**Reason**

> The exact four-part EC assignment depends on a protein-specific functional annotation or experimental identification absent from the sequence and choices. General sequence reasoning does not meaningfully resolve the close EC alternatives.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The matched sequence's database annotation supports C; no supplied evidence supports another listed EC number.


### Important caveats

- The UniProt annotation is a curated database claim citing a paper, not independent verification here of the primary experimental results.
- The EC number is assigned to the selenate-reductase activity of the complex; the sequence is annotated as its membrane-anchor subunit.
- The sequence match is exact in the reviewer evidence, but the author's original source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The strongly hydrophobic sequence is consistent with a multi-pass membrane protein, but that broad feature does not identify the specific selenate-reductase complex or distinguish its exact EC number from the alternatives.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific annotation identifying this sequence as subunit C of the selenate reductase complex and assigning that complex EC 1.97.1.14.",
    "reason": "The exact four-part EC assignment depends on a protein-specific functional annotation or experimental identification absent from the sequence and choices. General sequence reasoning does not meaningfully resolve the close EC alternatives."
  },
  "case_id": "EC_number_0002",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "H1",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the UniProt entry for selenate reductase subunit C, annotated with EC 1.97.1.14 and a selenate-reductase reaction. The annotation cites a study describing the respiratory selenate reductase complex. This supports choice C as the assigned EC number, though it does not establish that this membrane-anchor subunit alone catalyzes the reaction."
  },
  "important_caveats": [
    "The UniProt annotation is a curated database claim citing a paper, not independent verification here of the primary experimental results.",
    "The EC number is assigned to the selenate-reductase activity of the complex; the sequence is annotated as its membrane-anchor subunit.",
    "The sequence match is exact in the reviewer evidence, but the author's original source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched sequence's database annotation supports C; no supplied evidence supports another listed EC number."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0002",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the UniProt entry for selenate reductase subunit C, annotated with EC 1.97.1.14 and a selenate-reductase reaction. The annotation cites a study describing the respiratory selenate reductase complex. This supports choice C as the assigned EC number, though it does not establish that this membrane-anchor subunit alone catalyzes the reaction.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H1", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The strongly hydrophobic sequence is consistent with a multi-pass membrane protein, but that broad feature does not identify the specific selenate-reductase complex or distinguish its exact EC number from the alternatives.",
    "missing_item_specific_fact": "The protein-specific annotation identifying this sequence as subunit C of the selenate reductase complex and assigning that complex EC 1.97.1.14.",
    "reason": "The exact four-part EC assignment depends on a protein-specific functional annotation or experimental identification absent from the sequence and choices. General sequence reasoning does not meaningfully resolve the close EC alternatives."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched sequence's database annotation supports C; no supplied evidence supports another listed EC number."
  },
  "important_caveats": [
    "The UniProt annotation is a curated database claim citing a paper, not independent verification here of the primary experimental results.",
    "The EC number is assigned to the selenate-reductase activity of the complex; the sequence is annotated as its membrane-anchor subunit.",
    "The sequence match is exact in the reviewer evidence, but the author's original source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `invalid_review`.

**This result is not a valid structured review.** Any saved labels below remain the model’s original values; they are excluded from label distributions and paired agreement. No field or option ID has been repaired.

**Validation errors:** `question_ambiguity:invalid_option_ids`.

### Expected-answer support: supported

> The sequence matches UniProt entry A0A0A8X338 (SRDC_MESS1), annotated as Selenate reductase subunit C with EC 1.97.1.14. The annotation carries evidence code ECO:0000305 (inferred by similarity) referencing PubMed:21357486 (Kuroda et al. 2011, characterization of the srdBCA operon). The catalytic reaction is selenite + a quinone + H2O = selenate + a quinol. The protein is the membrane anchor subunit of the respiratory selenate reductase complex. The key is supported by reviewed Swiss-Prot annotation, though the evidence code indicates similarity-based inference rather than direct experimental characterization of this specific subunit's catalytic activity.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The extreme hydrophobicity and predicted multi-pass transmembrane topology of the 426-aa sequence could weakly argue for a quinone-dependent (membrane-associated, EC 1.97.1.14) over a ferredoxin-dependent (soluble, EC 1.97.1.13) selenate reductase, and against soluble enzymes like dihydrofolate reductase (1.5.1.38). However, this argument only applies AFTER one has already identified the protein as a selenate/selenite reductase, which cannot be determined from the sequence alone without recognizing the specific protein or its homologs.


**Missing item-specific fact**

> The identification of this protein as a subunit of the selenate reductase (srd) complex requires recognition of the specific sequence or its close homologs. No catalytic motif, cofactor-binding signature, or unique sequence feature in the provided sequence reveals selenate reductase activity de novo. The assignment to EC 1.97.1.14 specifically (rather than 1.97.1.13 or any other oxidoreductase) depends on knowing this is the membrane anchor subunit of the quinone-dependent selenate reductase complex.


**Reason**

> While the membrane-anchoring topology provides a post-hoc rationalization for choosing quinone-dependent (1.97.1.14) over ferredoxin-dependent (1.97.1.13), the fundamental task of recognizing the protein as a selenate reductase at all requires sequence-level recognition or database lookup. The sequence lacks a distinctive catalytic motif that would allow a model to infer selenate reduction from general biological principles. Selection among the four options depends on item-specific knowledge of this protein's identity.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A (1.97.1.13) and C (1.97.1.14) are both selenate/selenite reductases; without knowing the specific protein, a model cannot definitively exclude 1.97.1.13 based solely on hydrophobicity, since some ferredoxin-dependent enzymes also associate with membranes."
]
```

> The distinction between 1.97.1.13 and 1.97.1.14 rests on whether the enzyme uses quinone (membrane-bound) or ferredoxin (soluble) as electron donor. The membrane topology weakly favors 1.97.1.14, but this is not definitive without knowing the protein's identity. Options B and D are more clearly eliminable as non-membrane or unrelated enzyme classes.


### Important caveats

- The UniProt annotation uses evidence code ECO:0000305 (inferred by similarity), meaning the EC assignment for this specific subunit C is based on similarity to the characterized srd complex rather than direct in vitro activity measurement of subunit C alone.
- The protein is described as a 'membrane anchor subunit,' suggesting its role is structural/anchoring rather than catalytic; the EC number refers to the complex activity rather than necessarily the subunit's own catalytic function.
- The sequence match to A0A0A8X338 is exact (426 aa, SHA256 matched), confirming the reviewer evidence applies to the benchmark sequence.
- The reviewer evidence is not available to the evaluated model; the model must work from the raw sequence alone.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The extreme hydrophobicity and predicted multi-pass transmembrane topology of the 426-aa sequence could weakly argue for a quinone-dependent (membrane-associated, EC 1.97.1.14) over a ferredoxin-dependent (soluble, EC 1.97.1.13) selenate reductase, and against soluble enzymes like dihydrofolate reductase (1.5.1.38). However, this argument only applies AFTER one has already identified the protein as a selenate/selenite reductase, which cannot be determined from the sequence alone without recognizing the specific protein or its homologs.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The identification of this protein as a subunit of the selenate reductase (srd) complex requires recognition of the specific sequence or its close homologs. No catalytic motif, cofactor-binding signature, or unique sequence feature in the provided sequence reveals selenate reductase activity de novo. The assignment to EC 1.97.1.14 specifically (rather than 1.97.1.13 or any other oxidoreductase) depends on knowing this is the membrane anchor subunit of the quinone-dependent selenate reductase complex.",
    "reason": "While the membrane-anchoring topology provides a post-hoc rationalization for choosing quinone-dependent (1.97.1.14) over ferredoxin-dependent (1.97.1.13), the fundamental task of recognizing the protein as a selenate reductase at all requires sequence-level recognition or database lookup. The sequence lacks a distinctive catalytic motif that would allow a model to infer selenate reduction from general biological principles. Selection among the four options depends on item-specific knowledge of this protein's identity."
  },
  "case_id": "EC_number_0002",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence matches UniProt entry A0A0A8X338 (SRDC_MESS1), annotated as Selenate reductase subunit C with EC 1.97.1.14. The annotation carries evidence code ECO:0000305 (inferred by similarity) referencing PubMed:21357486 (Kuroda et al. 2011, characterization of the srdBCA operon). The catalytic reaction is selenite + a quinone + H2O = selenate + a quinol. The protein is the membrane anchor subunit of the respiratory selenate reductase complex. The key is supported by reviewed Swiss-Prot annotation, though the evidence code indicates similarity-based inference rather than direct experimental characterization of this specific subunit's catalytic activity."
  },
  "important_caveats": [
    "The UniProt annotation uses evidence code ECO:0000305 (inferred by similarity), meaning the EC assignment for this specific subunit C is based on similarity to the characterized srd complex rather than direct in vitro activity measurement of subunit C alone.",
    "The protein is described as a 'membrane anchor subunit,' suggesting its role is structural/anchoring rather than catalytic; the EC number refers to the complex activity rather than necessarily the subunit's own catalytic function.",
    "The sequence match to A0A0A8X338 is exact (426 aa, SHA256 matched), confirming the reviewer evidence applies to the benchmark sequence.",
    "The reviewer evidence is not available to the evaluated model; the model must work from the raw sequence alone."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A (1.97.1.13) and C (1.97.1.14) are both selenate/selenite reductases; without knowing the specific protein, a model cannot definitively exclude 1.97.1.13 based solely on hydrophobicity, since some ferredoxin-dependent enzymes also associate with membranes."
    ],
    "reason": "The distinction between 1.97.1.13 and 1.97.1.14 rests on whether the enzyme uses quinone (membrane-bound) or ferredoxin (soluble) as electron donor. The membrane topology weakly favors 1.97.1.14, but this is not definitive without knowing the protein's identity. Options B and D are more clearly eliminable as non-membrane or unrelated enzyme classes."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0002",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches UniProt entry A0A0A8X338 (SRDC_MESS1), annotated as Selenate reductase subunit C with EC 1.97.1.14. The annotation carries evidence code ECO:0000305 (inferred by similarity) referencing PubMed:21357486 (Kuroda et al. 2011, characterization of the srdBCA operon). The catalytic reaction is selenite + a quinone + H2O = selenate + a quinol. The protein is the membrane anchor subunit of the respiratory selenate reductase complex. The key is supported by reviewed Swiss-Prot annotation, though the evidence code indicates similarity-based inference rather than direct experimental characterization of this specific subunit's catalytic activity.",
    "evidence_ids": ["C4", "C5", "C6", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The extreme hydrophobicity and predicted multi-pass transmembrane topology of the 426-aa sequence could weakly argue for a quinone-dependent (membrane-associated, EC 1.97.1.14) over a ferredoxin-dependent (soluble, EC 1.97.1.13) selenate reductase, and against soluble enzymes like dihydrofolate reductase (1.5.1.38). However, this argument only applies AFTER one has already identified the protein as a selenate/selenite reductase, which cannot be determined from the sequence alone without recognizing the specific protein or its homologs.",
    "missing_item_specific_fact": "The identification of this protein as a subunit of the selenate reductase (srd) complex requires recognition of the specific sequence or its close homologs. No catalytic motif, cofactor-binding signature, or unique sequence feature in the provided sequence reveals selenate reductase activity de novo. The assignment to EC 1.97.1.14 specifically (rather than 1.97.1.13 or any other oxidoreductase) depends on knowing this is the membrane anchor subunit of the quinone-dependent selenate reductase complex.",
    "reason": "While the membrane-anchoring topology provides a post-hoc rationalization for choosing quinone-dependent (1.97.1.14) over ferredoxin-dependent (1.97.1.13), the fundamental task of recognizing the protein as a selenate reductase at all requires sequence-level recognition or database lookup. The sequence lacks a distinctive catalytic motif that would allow a model to infer selenate reduction from general biological principles. Selection among the four options depends on item-specific knowledge of this protein's identity."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A (1.97.1.13) and C (1.97.1.14) are both selenate/selenite reductases; without knowing the specific protein, a model cannot definitively exclude 1.97.1.13 based solely on hydrophobicity, since some ferredoxin-dependent enzymes also associate with membranes."],
    "reason": "The distinction between 1.97.1.13 and 1.97.1.14 rests on whether the enzyme uses quinone (membrane-bound) or ferredoxin (soluble) as electron donor. The membrane topology weakly favors 1.97.1.14, but this is not definitive without knowing the protein's identity. Options B and D are more clearly eliminable as non-membrane or unrelated enzyme classes."
  },
  "important_caveats": [
    "The UniProt annotation uses evidence code ECO:0000305 (inferred by similarity), meaning the EC assignment for this specific subunit C is based on similarity to the characterized srd complex rather than direct in vitro activity measurement of subunit C alone.",
    "The protein is described as a 'membrane anchor subunit,' suggesting its role is structural/anchoring rather than catalytic; the EC number refers to the complex activity rather than necessarily the subunit's own catalytic function.",
    "The sequence match to A0A0A8X338 is exact (426 aa, SHA256 matched), confirming the reviewer evidence applies to the benchmark sequence.",
    "The reviewer evidence is not available to the evaluated model; the model must work from the raw sequence alone."
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

**Accession:** `A0A0A8X338` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 26. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0A8X338.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:23:56.888485+00:00.  

```json
"A0A0A8X338"
```

Source SHA-256: `f24d48c67ebe30dab27bb776e276107f0f50c197edcf4849b2ea2624ac4d4bbe`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0A8X338.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:23:56.888485+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Selenate reductase membrane anchor subunit"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000305","id":"21357486","source":"PubMed"}],"value":"1.97.1.14"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Selenate reductase subunit C"}}}
```

Source SHA-256: `f24d48c67ebe30dab27bb776e276107f0f50c197edcf4849b2ea2624ac4d4bbe`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0A8X338.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:23:56.888485+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"1.97.1.14","evidences":[{"evidenceCode":"ECO:0000305","id":"21357486","source":"PubMed"}],"name":"selenite + a quinone + H2O = selenate + a quinol","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:51636"},{"database":"ChEBI","id":"CHEBI:15075"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:18212"},{"database":"ChEBI","id":"CHEBI:24646"},{"database":"ChEBI","id":"CHEBI:132124"}]}}
```

Source SHA-256: `f24d48c67ebe30dab27bb776e276107f0f50c197edcf4849b2ea2624ac4d4bbe`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0A8X338.json)  
**Locator:** `/references/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:23:56.888485+00:00.  

```json
{"citation":{"authors":["Kuroda M.","Yamashita M.","Miwa E.","Imao K.","Fujimoto N.","Ono H.","Nagano K.","Sei K.","Ike M."],"citationCrossReferences":[{"database":"PubMed","id":"21357486"},{"database":"DOI","id":"10.1128/jb.01197-10"}],"citationType":"journal article","firstPage":"2141","id":"21357486","journal":"J. Bacteriol.","lastPage":"2148","publicationDate":"2011","title":"Molecular cloning and characterization of the srdBCA operon, encoding the respiratory selenate reductase complex, from the selenate-reducing bacterium Bacillus selenatarsenatis SF-1.","volume":"193"},"evidences":[{"evidenceCode":"ECO:0000312","id":"BAJ83593.1","source":"EMBL"}],"referenceComments":[{"type":"STRAIN","value":"DSM 18680 / JCM 14380 / FERM P-15431 / SF-1"}],"referenceNumber":1,"referencePositions":["NUCLEOTIDE SEQUENCE [GENOMIC DNA]","FUNCTION AS A SELENATE REDUCTASE","SUBUNIT"]}
```

Source SHA-256: `f24d48c67ebe30dab27bb776e276107f0f50c197edcf4849b2ea2624ac4d4bbe`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0A8X338?format=txt&versions=26)  
**Locator:** `lines 1-15`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 26 / 1.  
**Retrieved:** 2026-11-02T04:24:00.225132+00:00.  

```text
ID   SRDC_MESS1              Reviewed;         426 AA.
AC   A0A0A8X338; E9RFD0;
DT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.
DT   04-MAR-2015, sequence version 1.
DT   28-JAN-2026, entry version 26.
DE   RecName: Full=Selenate reductase subunit C {ECO:0000305};
DE            EC=1.97.1.14 {ECO:0000305|PubMed:21357486};
DE   AltName: Full=Selenate reductase membrane anchor subunit {ECO:0000305};
GN   Name=srdC {ECO:0000303|PubMed:21357486};
GN   ORFNames=SAMD00020551_1551 {ECO:0000312|EMBL:GAM13407.1};
OS   Mesobacillus selenatarsenatis (strain DSM 18680 / JCM 14380 / FERM P-15431
OS   / SF-1).
OC   Bacteria; Bacillati; Bacillota; Bacilli; Bacillales; Bacillaceae;
OC   Mesobacillus.
OX   NCBI_TaxID=1321606;
```

Source SHA-256: `eb155874ab7c90cb9f9b357a382d734672b54b5376824079e6a394ed2c9dea57`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0A8X338?format=txt&versions=26)  
**Locator:** `lines 6-8`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 26 / 1.  
**Retrieved:** 2026-11-02T04:24:00.225132+00:00.  

```text
DE   RecName: Full=Selenate reductase subunit C {ECO:0000305};
DE            EC=1.97.1.14 {ECO:0000305|PubMed:21357486};
DE   AltName: Full=Selenate reductase membrane anchor subunit {ECO:0000305};
```

Source SHA-256: `eb155874ab7c90cb9f9b357a382d734672b54b5376824079e6a394ed2c9dea57`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0A8X338?format=txt&versions=26)  
**Locator:** `lines 43-47`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 26 / 1.  
**Retrieved:** 2026-11-02T04:24:00.225132+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=selenite + a quinone + H2O = selenate + a quinol;
CC         Xref=Rhea:RHEA:51636, ChEBI:CHEBI:15075, ChEBI:CHEBI:15377,
CC         ChEBI:CHEBI:18212, ChEBI:CHEBI:24646, ChEBI:CHEBI:132124;
CC         EC=1.97.1.14; Evidence={ECO:0000305|PubMed:21357486};
```

Source SHA-256: `eb155874ab7c90cb9f9b357a382d734672b54b5376824079e6a394ed2c9dea57`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 2. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
