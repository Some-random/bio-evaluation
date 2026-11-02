# EC_number_0181

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `EC_number`  
**Author expected answer:** **D** — 3.4.21.62

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MRTVFIYACIISLVLRTIPAHNDLMSKEKENKEKDVHKIIEDLRFLEKVDAILENSNMTIDDVKADADAYNPDEDAPKEELNKIEMEKKKAEEEAKNSKKKILERYLLDEKKKKSLRLIVSENHATSPSFFEESLIQEDFMSFIQSKGEIVNLKNLKSMIIELNSDMTDKELEAYITLLKKKGAHVESDELVGADSIYVDIIKDAVKRGDTSINFKKMQSNMLEVENKTYEKLNNNLKKSKNSYKKSFFNDEYRNLQWGLDLARLDDAQEMITTNSVETTKICVIDSGIDYNHPDLKGNIYVNLNELNGKEGIDDDNNGIIDDIYGVNYVNNTGDPWDDHNHGSHVSGIISAIGNNSIGVVGVNPSSKLVICKALDDKKLGRLGNIFKCIDYCINKKVNIINGSFSFDEYSTIFSSTIEYLARLGILFVVSSSNCSHPPSSIPDITRCDLSVNSKYPSVLSTQYDNMVVVANLKKKINGEYDISINSFYSDIYCQVSAPGANIYSTASRGSYMELSGTSMAAPHVAGIASIILSINPDLTYKQVVNILKNSVVKLSSHKNKIAWGGYIDILNAVKNAISSKNSYIRFQGIRMWKSKKRN

[Multiple Choices]
A. 3.5.2.6
B. 2.7.1.39
C. 5.1.3.45
D. 3.4.21.62
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

> The exact sequence matches the UniProt entry for Plasmodium berghei PbSUB1, which assigns EC 3.4.21.62 and describes its proteolytic activity. The annotation cites experimental evidence (ECO:0000269), though the cited primary evidence was not independently reviewed here.

Citations as saved: [C1](#evidence-c1), [C3](#evidence-c3), [C4](#evidence-c4), [C5](#evidence-c5), [H1](#evidence-h1), [H7](#evidence-h7).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is consistent with a secreted precursor containing a subtilisin-like serine protease domain; that enzyme class meaningfully favors the serine endopeptidase option D over the kinase, isomerase, and other hydrolase choices.


**Missing item-specific fact**

> Identifying the exact SUB1-specific EC subclass from sequence alone is less secure and would benefit from a protein-specific annotation or experimental characterization.


**Reason**

> The choices differ at broad enzyme-class levels, and the precursor/domain features provide a biological basis to select the protease option. The exact four-digit assignment is protein-specific, but the supplied choices allow meaningful class-level discrimination.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The options represent distinct enzyme classes, and the sequence features favor the serine protease choice.


### Important caveats

- The reviewer-only accession and annotations were not provided to the evaluated model.
- The database annotation is tied to an exact sequence match and cites experimental evidence, but the primary study was not independently validated here.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with a secreted precursor containing a subtilisin-like serine protease domain; that enzyme class meaningfully favors the serine endopeptidase option D over the kinase, isomerase, and other hydrolase choices.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "Identifying the exact SUB1-specific EC subclass from sequence alone is less secure and would benefit from a protein-specific annotation or experimental characterization.",
    "reason": "The choices differ at broad enzyme-class levels, and the precursor/domain features provide a biological basis to select the protease option. The exact four-digit assignment is protein-specific, but the supplied choices allow meaningful class-level discrimination."
  },
  "case_id": "EC_number_0181",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C3",
      "C4",
      "C5",
      "H1",
      "H7"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry for Plasmodium berghei PbSUB1, which assigns EC 3.4.21.62 and describes its proteolytic activity. The annotation cites experimental evidence (ECO:0000269), though the cited primary evidence was not independently reviewed here."
  },
  "important_caveats": [
    "The reviewer-only accession and annotations were not provided to the evaluated model.",
    "The database annotation is tied to an exact sequence match and cites experimental evidence, but the primary study was not independently validated here."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The options represent distinct enzyme classes, and the sequence features favor the serine protease choice."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0181",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry for Plasmodium berghei PbSUB1, which assigns EC 3.4.21.62 and describes its proteolytic activity. The annotation cites experimental evidence (ECO:0000269), though the cited primary evidence was not independently reviewed here.",
    "evidence_ids": ["C1", "C3", "C4", "C5", "H1", "H7"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is consistent with a secreted precursor containing a subtilisin-like serine protease domain; that enzyme class meaningfully favors the serine endopeptidase option D over the kinase, isomerase, and other hydrolase choices.",
    "missing_item_specific_fact": "Identifying the exact SUB1-specific EC subclass from sequence alone is less secure and would benefit from a protein-specific annotation or experimental characterization.",
    "reason": "The choices differ at broad enzyme-class levels, and the precursor/domain features provide a biological basis to select the protease option. The exact four-digit assignment is protein-specific, but the supplied choices allow meaningful class-level discrimination."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The options represent distinct enzyme classes, and the sequence features favor the serine protease choice."
  },
  "important_caveats": [
    "The reviewer-only accession and annotations were not provided to the evaluated model.",
    "The database annotation is tied to an exact sequence match and cites experimental evidence, but the primary study was not independently validated here."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry A0A509AM03 (SUB1_PLABA, PbSUB1) from Plasmodium berghei strain Anka is annotated with EC 3.4.21.62 (Subtilisin-like protease 1), supported by experimental evidence (ECO:0000269, PubMed:23653352). The benchmark sequence matches the UniProt sequence exactly (599 AA, SHA256 match). The catalytic activity description confirms hydrolysis of proteins with broad specificity and preference for large uncharged P1 residue, consistent with EC 3.4.21.62.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H2](#evidence-h2), [H7](#evidence-h7).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains canonical subtilisin catalytic triad motifs: 'DSG' (Asp motif, in 'ICVIDSGIDYNHPDL'), a His-containing region ('HNDL' near N-terminus), and 'GTSMA' (Ser motif, in 'GTSMAAPHVAG'). These are hallmark features of subtilisin-like serine proteases (EC 3.4.21.x). The distractors belong to entirely different enzyme classes: 3.5.2.6 (amidase, C-N bond hydrolysis), 2.7.1.39 (kinase, phosphate transfer), 5.1.3.45 (isomerase/epimerase). None of these classes involve peptide-bond hydrolysis or subtilisin motifs. General knowledge of enzyme classification and subtilisin structural motifs allows elimination of A, B, and C, leaving D as the only serine protease option.


**Missing item-specific fact**

> None critical. The specific 4th digit (62) designating Plasmodium subtilisin-like protease is a database-specific assignment, but since only one 3.4.21.x option is offered, reasoning to the enzyme class level (subtilisin-family serine protease) is sufficient to select D.


**Reason**

> The sequence displays identifiable subtilisin catalytic triad motifs (DSG, GTSMA) that are diagnostic of EC 3.4.21.x enzymes. The three distractors represent completely unrelated enzyme classes (amidase, kinase, isomerase), making them eliminable by general biochemical reasoning without needing to memorize the specific protein identity.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Only one option (D, 3.4.21.62) belongs to the serine protease class (3.4.21.x) indicated by the subtilisin motifs in the sequence. The other options are from unrelated enzyme classes and are clearly incompatible with the observed catalytic architecture.


### Important caveats

- The specific EC 4th digit (62) is a database-assigned identifier for Plasmodium subtilisin-like proteases; distinguishing 3.4.21.62 from other 3.4.21.x numbers would require memorization, but this is not needed here since only one 3.4.21.x option is provided.
- The UniProt annotation is based on experimental evidence (ECO:0000269) from PubMed:23653352, not purely computational transfer.
- The sequence match between benchmark input and UniProt entry A0A509AM03 is exact (SHA256 confirmed).

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains canonical subtilisin catalytic triad motifs: 'DSG' (Asp motif, in 'ICVIDSGIDYNHPDL'), a His-containing region ('HNDL' near N-terminus), and 'GTSMA' (Ser motif, in 'GTSMAAPHVAG'). These are hallmark features of subtilisin-like serine proteases (EC 3.4.21.x). The distractors belong to entirely different enzyme classes: 3.5.2.6 (amidase, C-N bond hydrolysis), 2.7.1.39 (kinase, phosphate transfer), 5.1.3.45 (isomerase/epimerase). None of these classes involve peptide-bond hydrolysis or subtilisin motifs. General knowledge of enzyme classification and subtilisin structural motifs allows elimination of A, B, and C, leaving D as the only serine protease option.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None critical. The specific 4th digit (62) designating Plasmodium subtilisin-like protease is a database-specific assignment, but since only one 3.4.21.x option is offered, reasoning to the enzyme class level (subtilisin-family serine protease) is sufficient to select D.",
    "reason": "The sequence displays identifiable subtilisin catalytic triad motifs (DSG, GTSMA) that are diagnostic of EC 3.4.21.x enzymes. The three distractors represent completely unrelated enzyme classes (amidase, kinase, isomerase), making them eliminable by general biochemical reasoning without needing to memorize the specific protein identity."
  },
  "case_id": "EC_number_0181",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "H1",
      "H2",
      "H7"
    ],
    "judgment": "supported",
    "reason": "UniProt entry A0A509AM03 (SUB1_PLABA, PbSUB1) from Plasmodium berghei strain Anka is annotated with EC 3.4.21.62 (Subtilisin-like protease 1), supported by experimental evidence (ECO:0000269, PubMed:23653352). The benchmark sequence matches the UniProt sequence exactly (599 AA, SHA256 match). The catalytic activity description confirms hydrolysis of proteins with broad specificity and preference for large uncharged P1 residue, consistent with EC 3.4.21.62."
  },
  "important_caveats": [
    "The specific EC 4th digit (62) is a database-assigned identifier for Plasmodium subtilisin-like proteases; distinguishing 3.4.21.62 from other 3.4.21.x numbers would require memorization, but this is not needed here since only one 3.4.21.x option is provided.",
    "The UniProt annotation is based on experimental evidence (ECO:0000269) from PubMed:23653352, not purely computational transfer.",
    "The sequence match between benchmark input and UniProt entry A0A509AM03 is exact (SHA256 confirmed)."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only one option (D, 3.4.21.62) belongs to the serine protease class (3.4.21.x) indicated by the subtilisin motifs in the sequence. The other options are from unrelated enzyme classes and are clearly incompatible with the observed catalytic architecture."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0181",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry A0A509AM03 (SUB1_PLABA, PbSUB1) from Plasmodium berghei strain Anka is annotated with EC 3.4.21.62 (Subtilisin-like protease 1), supported by experimental evidence (ECO:0000269, PubMed:23653352). The benchmark sequence matches the UniProt sequence exactly (599 AA, SHA256 match). The catalytic activity description confirms hydrolysis of proteins with broad specificity and preference for large uncharged P1 residue, consistent with EC 3.4.21.62.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H1", "H2", "H7"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains canonical subtilisin catalytic triad motifs: 'DSG' (Asp motif, in 'ICVIDSGIDYNHPDL'), a His-containing region ('HNDL' near N-terminus), and 'GTSMA' (Ser motif, in 'GTSMAAPHVAG'). These are hallmark features of subtilisin-like serine proteases (EC 3.4.21.x). The distractors belong to entirely different enzyme classes: 3.5.2.6 (amidase, C-N bond hydrolysis), 2.7.1.39 (kinase, phosphate transfer), 5.1.3.45 (isomerase/epimerase). None of these classes involve peptide-bond hydrolysis or subtilisin motifs. General knowledge of enzyme classification and subtilisin structural motifs allows elimination of A, B, and C, leaving D as the only serine protease option.",
    "missing_item_specific_fact": "None critical. The specific 4th digit (62) designating Plasmodium subtilisin-like protease is a database-specific assignment, but since only one 3.4.21.x option is offered, reasoning to the enzyme class level (subtilisin-family serine protease) is sufficient to select D.",
    "reason": "The sequence displays identifiable subtilisin catalytic triad motifs (DSG, GTSMA) that are diagnostic of EC 3.4.21.x enzymes. The three distractors represent completely unrelated enzyme classes (amidase, kinase, isomerase), making them eliminable by general biochemical reasoning without needing to memorize the specific protein identity."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only one option (D, 3.4.21.62) belongs to the serine protease class (3.4.21.x) indicated by the subtilisin motifs in the sequence. The other options are from unrelated enzyme classes and are clearly incompatible with the observed catalytic architecture."
  },
  "important_caveats": [
    "The specific EC 4th digit (62) is a database-assigned identifier for Plasmodium subtilisin-like proteases; distinguishing 3.4.21.62 from other 3.4.21.x numbers would require memorization, but this is not needed here since only one 3.4.21.x option is provided.",
    "The UniProt annotation is based on experimental evidence (ECO:0000269) from PubMed:23653352, not purely computational transfer.",
    "The sequence match between benchmark input and UniProt entry A0A509AM03 is exact (SHA256 confirmed)."
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

**Accession:** `A0A509AM03` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 30. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A509AM03.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:47.276162+00:00.  

```json
"A0A509AM03"
```

Source SHA-256: `58189b21f52a9fa91fa2e6cfc2283bebb23b54839f051ab7a55f96582d49e7b5`.

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A509AM03.json)  
**Locator:** `/organism`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:47.276162+00:00.  

```json
{"evidences":[{"evidenceCode":"ECO:0000312","id":"UP000074855","source":"Proteomes"}],"lineage":["Eukaryota","Sar","Alveolata","Apicomplexa","Aconoidasida","Haemosporida","Plasmodiidae","Plasmodium","Vinckeia"],"scientificName":"Plasmodium berghei (strain Anka)","taxonId":5823}
```

Source SHA-256: `58189b21f52a9fa91fa2e6cfc2283bebb23b54839f051ab7a55f96582d49e7b5`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A509AM03.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:47.276162+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"23653352","source":"PubMed"},{"evidenceCode":"ECO:0000303","id":"24089525","source":"PubMed"},{"evidenceCode":"ECO:0000303","id":"24348254","source":"PubMed"},{"evidenceCode":"ECO:0000303","id":"30941868","source":"PubMed"}],"value":"PbSUB1"}}],"flag":"Precursor","recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"23653352","source":"PubMed"}],"value":"3.4.21.62"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"24348254","source":"PubMed"}],"value":"Subtilisin-like protease 1"}}}
```

Source SHA-256: `58189b21f52a9fa91fa2e6cfc2283bebb23b54839f051ab7a55f96582d49e7b5`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A509AM03.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:47.276162+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"3.4.21.62","evidences":[{"evidenceCode":"ECO:0000269","id":"23653352","source":"PubMed"}],"name":"Hydrolysis of proteins with broad specificity for peptide bonds, and a preference for a large uncharged residue in P1. Hydrolyzes peptide amides."}}
```

Source SHA-256: `58189b21f52a9fa91fa2e6cfc2283bebb23b54839f051ab7a55f96582d49e7b5`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A509AM03.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:47.276162+00:00.  

```json
{"citation":{"authors":["Bouillon A.","Giganti D.","Benedet C.","Gorgette O.","Petres S.","Crublet E.","Girard-Blanc C.","Witkowski B.","Menard D.","Nilges M.","Mercereau-Puijalon O.","Stoven V.","Barale J.C."],"citationCrossReferences":[{"database":"PubMed","id":"23653352"},{"database":"DOI","id":"10.1074/jbc.m113.456764"}],"citationType":"journal article","firstPage":"18561","id":"23653352","journal":"J. Biol. Chem.","lastPage":"18573","publicationDate":"2013","title":"In Silico screening on the three-dimensional model of the Plasmodium vivax SUB1 protease leads to the validation of a novel anti-parasite compound.","volume":"288"},"evidences":[{"evidenceCode":"ECO:0000305"}],"referenceNumber":2,"referencePositions":["CATALYTIC ACTIVITY","PROTEOLYTIC CLEAVAGE","CLEAVAGE SITE"]}
```

Source SHA-256: `58189b21f52a9fa91fa2e6cfc2283bebb23b54839f051ab7a55f96582d49e7b5`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A509AM03?format=txt&versions=30)  
**Locator:** `lines 1-15`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 30 / 1.  
**Retrieved:** 2026-11-01T06:27:31.257005+00:00.  

```text
ID   SUB1_PLABA              Reviewed;         599 AA.
AC   A0A509AM03;
DT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.
DT   18-SEP-2019, sequence version 1.
DT   28-JAN-2026, entry version 30.
DE   RecName: Full=Subtilisin-like protease 1 {ECO:0000303|PubMed:24348254};
DE            EC=3.4.21.62 {ECO:0000269|PubMed:23653352};
DE   AltName: Full=PbSUB1 {ECO:0000303|PubMed:23653352, ECO:0000303|PubMed:24089525, ECO:0000303|PubMed:24348254, ECO:0000303|PubMed:30941868};
DE   Flags: Precursor;
GN   Name=SUB1 {ECO:0000305};
GN   ORFNames=PBANKA_1107100 {ECO:0000312|EMBL:VUC56494.1};
OS   Plasmodium berghei (strain Anka).
OC   Eukaryota; Sar; Alveolata; Apicomplexa; Aconoidasida; Haemosporida;
OC   Plasmodiidae; Plasmodium; Plasmodium (Vinckeia).
OX   NCBI_TaxID=5823 {ECO:0000312|Proteomes:UP000074855};
```

Source SHA-256: `c0f9a4e5e66e23741f96fa610fa30c4dfac008f0d5ae074d8b0834a351f4fc02`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A509AM03?format=txt&versions=30)  
**Locator:** `lines 6-9`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 30 / 1.  
**Retrieved:** 2026-11-01T06:27:31.257005+00:00.  

```text
DE   RecName: Full=Subtilisin-like protease 1 {ECO:0000303|PubMed:24348254};
DE            EC=3.4.21.62 {ECO:0000269|PubMed:23653352};
DE   AltName: Full=PbSUB1 {ECO:0000303|PubMed:23653352, ECO:0000303|PubMed:24089525, ECO:0000303|PubMed:24348254, ECO:0000303|PubMed:30941868};
DE   Flags: Precursor;
```

Source SHA-256: `c0f9a4e5e66e23741f96fa610fa30c4dfac008f0d5ae074d8b0834a351f4fc02`.

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A509AM03?format=txt&versions=30)  
**Locator:** `lines 73-77`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 30 / 1.  
**Retrieved:** 2026-11-01T06:27:31.257005+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=Hydrolysis of proteins with broad specificity for peptide
CC         bonds, and a preference for a large uncharged residue in P1.
CC         Hydrolyzes peptide amides.; EC=3.4.21.62;
CC         Evidence={ECO:0000269|PubMed:23653352};
```

Source SHA-256: `c0f9a4e5e66e23741f96fa610fa30c4dfac008f0d5ae074d8b0834a351f4fc02`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 181. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
