# EC_number_0182

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `EC_number`  
**Author expected answer:** **C** — 3.4.21.62

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MVLTRRAALLLCPWVIQLVIKRTLAGDILPNEGKKEKDDVHKIISELRFLQKVETILESSNMSVSDVEADANAYNPDRDAPKEELQKLQDQQETPSKQPNNLRNSPQKRAEKKESPGKNKKSLRLIVSENHATSPSFFEESLLQEDVVSFIQSKGKLSNLKNLKSMIIDLNSDMTDEELAEYISLLERKGALIESDKLVGADDVSLASVKDAVRRGESSVNWGKLRSTMLEVPSGESPPSHAASSGSPFDDDDDLLSEAALHREEAHLAGSKTTKGYKFNDEYRNLQWGLDLARLDETQDLINANRVSVTKICVIDSGIDYNHPDLRNNIDVNVKELHGRKGVDDDSNGVVDDVYGANFVNNSGDPMDDNYHGTHVSGIISAVGNNGIGIVGVDGHSKLVICKALDQHKLGRLGDMFKCIDYCISRQAHMINGSFSFDEYSNIFNASVEHLRSLGILFFVSASNCAHDKLSKPDIAKCDLAVNHRYPPILSKTHNNVIAVANLKRDLDESYSLSVNSFYSNIYCQLAAPGTNIYSTTPMNNYRKLNGTSMASPHVAAIASIVRSINPNLTYLQIVEILRNAIVKLPSLTERVSWGGYVDILRAVNLAIDSKAAPYIKSHSWFRWKQGSRR

[Multiple Choices]
A. 3.4.13.22
B. 1.1.1.195
C. 3.4.21.62
D. 1.97.1.13
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

> The supplied sequence exactly matches the 630-aa Plasmodium vivax SUB1 sequence in the cited UniProt records. Those records annotate it as EC 3.4.21.62, with catalytic-activity evidence attributed to publications (ECO:0000269).

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H1](#evidence-h1), [H8](#evidence-h8).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence is consistent with a large precursor containing a subtilisin-like serine protease domain, which supports a serine endopeptidase interpretation and makes the non-protease options poor fits.


**Missing item-specific fact**

> Identifying the exact EC subtype 3.4.21.62 requires the protein-specific SUB1 annotation or catalytic characterization; the sequence and choices alone do not establish that precise EC assignment.


**Reason**

> Sequence reasoning can support the broad enzyme class and may favor C over the dipeptidase option, but the requested complete EC number is more specific than those general features establish.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The reviewer evidence supports C for this sequence. The uncertainty concerns whether the input alone supports the exact subtype, not conflicting evidence for another listed option.


### Important caveats

- The sequence match and EC annotation are established from reviewer-only database evidence, which was not supplied to the evaluated model.
- The UniProt annotation cites experimental evidence codes, but the underlying primary studies were not independently reviewed here.
- The author's exact source snapshot is unknown; the sequence matches both the current entry and the retrieved historical entry.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with a large precursor containing a subtilisin-like serine protease domain, which supports a serine endopeptidase interpretation and makes the non-protease options poor fits.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "Identifying the exact EC subtype 3.4.21.62 requires the protein-specific SUB1 annotation or catalytic characterization; the sequence and choices alone do not establish that precise EC assignment.",
    "reason": "Sequence reasoning can support the broad enzyme class and may favor C over the dipeptidase option, but the requested complete EC number is more specific than those general features establish."
  },
  "case_id": "EC_number_0182",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H1",
      "H8"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the 630-aa Plasmodium vivax SUB1 sequence in the cited UniProt records. Those records annotate it as EC 3.4.21.62, with catalytic-activity evidence attributed to publications (ECO:0000269)."
  },
  "important_caveats": [
    "The sequence match and EC annotation are established from reviewer-only database evidence, which was not supplied to the evaluated model.",
    "The UniProt annotation cites experimental evidence codes, but the underlying primary studies were not independently reviewed here.",
    "The author's exact source snapshot is unknown; the sequence matches both the current entry and the retrieved historical entry."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The reviewer evidence supports C for this sequence. The uncertainty concerns whether the input alone supports the exact subtype, not conflicting evidence for another listed option."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0182",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the 630-aa Plasmodium vivax SUB1 sequence in the cited UniProt records. Those records annotate it as EC 3.4.21.62, with catalytic-activity evidence attributed to publications (ECO:0000269).",
    "evidence_ids": ["C1", "C4", "C5", "H1", "H8"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence is consistent with a large precursor containing a subtilisin-like serine protease domain, which supports a serine endopeptidase interpretation and makes the non-protease options poor fits.",
    "missing_item_specific_fact": "Identifying the exact EC subtype 3.4.21.62 requires the protein-specific SUB1 annotation or catalytic characterization; the sequence and choices alone do not establish that precise EC assignment.",
    "reason": "Sequence reasoning can support the broad enzyme class and may favor C over the dipeptidase option, but the requested complete EC number is more specific than those general features establish."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The reviewer evidence supports C for this sequence. The uncertainty concerns whether the input alone supports the exact subtype, not conflicting evidence for another listed option."
  },
  "important_caveats": [
    "The sequence match and EC annotation are established from reviewer-only database evidence, which was not supplied to the evaluated model.",
    "The UniProt annotation cites experimental evidence codes, but the underlying primary studies were not independently reviewed here.",
    "The author's exact source snapshot is unknown; the sequence matches both the current entry and the retrieved historical entry."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry E6Y8B9 (SUB1_PLAVI, Plasmodium vivax) assigns EC 3.4.21.62 with evidence code ECO:0000269 (experimental) supported by five independent publications including X-ray crystallography studies (PDB: 4TR2, 8COY, 8COZ, 8QKE, 8QKG). The catalytic activity is described as 'Hydrolysis of proteins with broad specificity for peptide bonds, and a preference for a large uncharged residue in P1. Hydrolyzes peptide amides.' The sequence matches exactly (630 AA, SHA256 confirmed). The EC assignment is experimentally validated.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C8](#evidence-c8), [H1](#evidence-h1), [H2](#evidence-h2), [H8](#evidence-h8).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> A model could reason that the sequence is unlikely to be an oxidoreductase (eliminating B: 1.1.1.195 and D: 1.97.1.13) based on the absence of cofactor-binding motifs and the presence of protease-like features. Subtilisin-family (S8) features such as the HGR motif (His of catalytic triad) and DSG motif (Asp of catalytic triad) are present in the sequence, which could narrow the choice to 3.4.21.x over 3.4.13.x (S11 D-Ala-D-Ala carboxypeptidase). However, the specific 4th digit '62' cannot be derived from general biological reasoning; it is a database-assigned identifier for this particular enzyme.


**Missing item-specific fact**

> The exact 4-digit EC number 3.4.21.62 is a database-assigned identifier that cannot be derived from sequence by general biological reasoning. While the sequence contains some subtilisin-like motifs (HGR, DSG), Plasmodium SUB1 is a highly divergent subtilisin, and the canonical GDSGS catalytic serine motif is not clearly identifiable in the sequence. Assigning the specific number .62 rather than any other 3.4.21.x entry requires knowing the exact enzyme identity from UniProt or literature.


**Reason**

> The constrained choices (only one 3.4.21.x option) partially mitigate the lookup burden, as identifying subtilisin-like features would lead to C. However, the Plasmodium SUB1 sequence is divergent from canonical subtilisins, making motif-based identification uncertain without prior knowledge of this specific protein. The final 4-digit assignment is fundamentally a database fact.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Given the four choices, only C (3.4.21.62) is consistent with a subtilisin-like serine endopeptidase. Options B and D are oxidoreductases (EC class 1), clearly incompatible with a protease. Option A (3.4.13.22) is a D-Ala-D-Ala carboxypeptidase (S11 family) with different structural motifs. No other option is defensible for this sequence.


### Important caveats

- The UniProt annotation for EC 3.4.21.62 is supported by experimental evidence (ECO:0000269) from five publications, not merely computational prediction.
- Plasmodium vivax SUB1 is a divergent subtilisin; canonical subtilisin motifs (e.g., GDSGS) may be modified, making sequence-based identification harder than for well-studied subtilisins.
- The reviewer identified the accession E6Y8B9 from dataset image-path metadata; this was not available to the evaluated model.
- The first public date of the UniProt entry is 2025-04-09, meaning the annotation was relatively recent at the time of benchmark construction.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "A model could reason that the sequence is unlikely to be an oxidoreductase (eliminating B: 1.1.1.195 and D: 1.97.1.13) based on the absence of cofactor-binding motifs and the presence of protease-like features. Subtilisin-family (S8) features such as the HGR motif (His of catalytic triad) and DSG motif (Asp of catalytic triad) are present in the sequence, which could narrow the choice to 3.4.21.x over 3.4.13.x (S11 D-Ala-D-Ala carboxypeptidase). However, the specific 4th digit '62' cannot be derived from general biological reasoning; it is a database-assigned identifier for this particular enzyme.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The exact 4-digit EC number 3.4.21.62 is a database-assigned identifier that cannot be derived from sequence by general biological reasoning. While the sequence contains some subtilisin-like motifs (HGR, DSG), Plasmodium SUB1 is a highly divergent subtilisin, and the canonical GDSGS catalytic serine motif is not clearly identifiable in the sequence. Assigning the specific number .62 rather than any other 3.4.21.x entry requires knowing the exact enzyme identity from UniProt or literature.",
    "reason": "The constrained choices (only one 3.4.21.x option) partially mitigate the lookup burden, as identifying subtilisin-like features would lead to C. However, the Plasmodium SUB1 sequence is divergent from canonical subtilisins, making motif-based identification uncertain without prior knowledge of this specific protein. The final 4-digit assignment is fundamentally a database fact."
  },
  "case_id": "EC_number_0182",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C8",
      "H1",
      "H2",
      "H8"
    ],
    "judgment": "supported",
    "reason": "UniProt entry E6Y8B9 (SUB1_PLAVI, Plasmodium vivax) assigns EC 3.4.21.62 with evidence code ECO:0000269 (experimental) supported by five independent publications including X-ray crystallography studies (PDB: 4TR2, 8COY, 8COZ, 8QKE, 8QKG). The catalytic activity is described as 'Hydrolysis of proteins with broad specificity for peptide bonds, and a preference for a large uncharged residue in P1. Hydrolyzes peptide amides.' The sequence matches exactly (630 AA, SHA256 confirmed). The EC assignment is experimentally validated."
  },
  "important_caveats": [
    "The UniProt annotation for EC 3.4.21.62 is supported by experimental evidence (ECO:0000269) from five publications, not merely computational prediction.",
    "Plasmodium vivax SUB1 is a divergent subtilisin; canonical subtilisin motifs (e.g., GDSGS) may be modified, making sequence-based identification harder than for well-studied subtilisins.",
    "The reviewer identified the accession E6Y8B9 from dataset image-path metadata; this was not available to the evaluated model.",
    "The first public date of the UniProt entry is 2025-04-09, meaning the annotation was relatively recent at the time of benchmark construction."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Given the four choices, only C (3.4.21.62) is consistent with a subtilisin-like serine endopeptidase. Options B and D are oxidoreductases (EC class 1), clearly incompatible with a protease. Option A (3.4.13.22) is a D-Ala-D-Ala carboxypeptidase (S11 family) with different structural motifs. No other option is defensible for this sequence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0182",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry E6Y8B9 (SUB1_PLAVI, Plasmodium vivax) assigns EC 3.4.21.62 with evidence code ECO:0000269 (experimental) supported by five independent publications including X-ray crystallography studies (PDB: 4TR2, 8COY, 8COZ, 8QKE, 8QKG). The catalytic activity is described as 'Hydrolysis of proteins with broad specificity for peptide bonds, and a preference for a large uncharged residue in P1. Hydrolyzes peptide amides.' The sequence matches exactly (630 AA, SHA256 confirmed). The EC assignment is experimentally validated.",
    "evidence_ids": ["C4", "C5", "C8", "H1", "H2", "H8"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "A model could reason that the sequence is unlikely to be an oxidoreductase (eliminating B: 1.1.1.195 and D: 1.97.1.13) based on the absence of cofactor-binding motifs and the presence of protease-like features. Subtilisin-family (S8) features such as the HGR motif (His of catalytic triad) and DSG motif (Asp of catalytic triad) are present in the sequence, which could narrow the choice to 3.4.21.x over 3.4.13.x (S11 D-Ala-D-Ala carboxypeptidase). However, the specific 4th digit '62' cannot be derived from general biological reasoning; it is a database-assigned identifier for this particular enzyme.",
    "missing_item_specific_fact": "The exact 4-digit EC number 3.4.21.62 is a database-assigned identifier that cannot be derived from sequence by general biological reasoning. While the sequence contains some subtilisin-like motifs (HGR, DSG), Plasmodium SUB1 is a highly divergent subtilisin, and the canonical GDSGS catalytic serine motif is not clearly identifiable in the sequence. Assigning the specific number .62 rather than any other 3.4.21.x entry requires knowing the exact enzyme identity from UniProt or literature.",
    "reason": "The constrained choices (only one 3.4.21.x option) partially mitigate the lookup burden, as identifying subtilisin-like features would lead to C. However, the Plasmodium SUB1 sequence is divergent from canonical subtilisins, making motif-based identification uncertain without prior knowledge of this specific protein. The final 4-digit assignment is fundamentally a database fact."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Given the four choices, only C (3.4.21.62) is consistent with a subtilisin-like serine endopeptidase. Options B and D are oxidoreductases (EC class 1), clearly incompatible with a protease. Option A (3.4.13.22) is a D-Ala-D-Ala carboxypeptidase (S11 family) with different structural motifs. No other option is defensible for this sequence."
  },
  "important_caveats": [
    "The UniProt annotation for EC 3.4.21.62 is supported by experimental evidence (ECO:0000269) from five publications, not merely computational prediction.",
    "Plasmodium vivax SUB1 is a divergent subtilisin; canonical subtilisin motifs (e.g., GDSGS) may be modified, making sequence-based identification harder than for well-studied subtilisins.",
    "The reviewer identified the accession E6Y8B9 from dataset image-path metadata; this was not available to the evaluated model.",
    "The first public date of the UniProt entry is 2025-04-09, meaning the annotation was relatively recent at the time of benchmark construction."
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

**Accession:** `E6Y8B9` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 78. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E6Y8B9.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:01.366318+00:00.  

```json
"E6Y8B9"
```

Source SHA-256: `e9b4af9865155585e28a933302308978b5c5a92dbbd9ce2df61bef40af1c012b`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E6Y8B9.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:01.366318+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"37428845","source":"PubMed"},{"evidenceCode":"ECO:0000303","id":"38386597","source":"PubMed"},{"evidenceCode":"ECO:0000303","id":"38503166","source":"PubMed"}],"value":"PvS1"}},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"23653352","source":"PubMed"},{"evidenceCode":"ECO:0000303","id":"25204226","source":"PubMed"}],"value":"PvSUB1"}},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"38503166","source":"PubMed"}],"value":"SUB1 protease"}},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"25204226","source":"PubMed"}],"value":"Subtilase SUB1"}}],"flag":"Precursor","recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"23653352","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"25204226","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"37428845","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"38386597","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"38503166","source":"PubMed"}],"value":"3.4.21.62"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"37428845","source":"PubMed"},{"evidenceCode":"ECO:0000303","id":"38386597","source":"PubMed"},{"evidenceCode":"ECO:0000303","id":"38503166","source":"PubMed"}],"value":"Subtilisin-like protease 1"}}}
```

Source SHA-256: `e9b4af9865155585e28a933302308978b5c5a92dbbd9ce2df61bef40af1c012b`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E6Y8B9.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:01.366318+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"3.4.21.62","evidences":[{"evidenceCode":"ECO:0000269","id":"23653352","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"25204226","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"37428845","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"38386597","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"38503166","source":"PubMed"}],"name":"Hydrolysis of proteins with broad specificity for peptide bonds, and a preference for a large uncharged residue in P1. Hydrolyzes peptide amides."}}
```

Source SHA-256: `e9b4af9865155585e28a933302308978b5c5a92dbbd9ce2df61bef40af1c012b`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E6Y8B9.json)  
**Locator:** `/references/4`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:01.366318+00:00.  

```json
{"citation":{"authors":["Giganti D.","Bouillon A.","Tawk L.","Robert F.","Martinez M.","Crublet E.","Weber P.","Girard-Blanc C.","Petres S.","Haouz A.","Hernandez J.F.","Mercereau-Puijalon O.","Alzari P.M.","Barale J.C."],"citationCrossReferences":[{"database":"PubMed","id":"25204226"},{"database":"DOI","id":"10.1038/ncomms5833"}],"citationType":"journal article","firstPage":"4833","id":"25204226","journal":"Nat. Commun.","lastPage":"4833","publicationDate":"2014","title":"A novel Plasmodium-specific prodomain fold regulates the malaria drug target SUB1 subtilase.","volume":"5"},"evidences":[{"evidenceCode":"ECO:0007744","id":"4TR2","source":"PDB"}],"referenceNumber":5,"referencePositions":["X-RAY CRYSTALLOGRAPHY (2.70 ANGSTROMS) OF 26-630 IN COMPLEX WITH CALCIUM","CATALYTIC ACTIVITY","COFACTOR","ACTIVITY REGULATION","SUBUNIT","PROTEOLYTIC CLEAVAGE","CLEAVAGE SITE","DISULFIDE BONDS"]}
```

Source SHA-256: `e9b4af9865155585e28a933302308978b5c5a92dbbd9ce2df61bef40af1c012b`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E6Y8B9?format=txt&versions=78)  
**Locator:** `lines 1-20`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 78 / 1.  
**Retrieved:** 2026-11-02T04:28:06.789132+00:00.  

```text
ID   SUB1_PLAVI              Reviewed;         630 AA.
AC   E6Y8B9;
DT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.
DT   08-MAR-2011, sequence version 1.
DT   28-JAN-2026, entry version 78.
DE   RecName: Full=Subtilisin-like protease 1 {ECO:0000303|PubMed:37428845, ECO:0000303|PubMed:38386597, ECO:0000303|PubMed:38503166};
DE            EC=3.4.21.62 {ECO:0000269|PubMed:23653352, ECO:0000269|PubMed:25204226, ECO:0000269|PubMed:37428845, ECO:0000269|PubMed:38386597, ECO:0000269|PubMed:38503166};
DE   AltName: Full=PvS1 {ECO:0000303|PubMed:37428845, ECO:0000303|PubMed:38386597, ECO:0000303|PubMed:38503166};
DE   AltName: Full=PvSUB1 {ECO:0000303|PubMed:23653352, ECO:0000303|PubMed:25204226};
DE   AltName: Full=SUB1 protease {ECO:0000303|PubMed:38503166};
DE   AltName: Full=Subtilase SUB1 {ECO:0000303|PubMed:25204226};
DE   Flags: Precursor;
GN   Name=sub1 {ECO:0000312|EMBL:ACT76164.1};
GN   ORFNames=PVC01_100035100 {ECO:0000312|EMBL:SCO73277.1},
GN   PVT01_100029100 {ECO:0000312|EMBL:SCO67822.1},
GN   PVW1_100050600 {ECO:0000312|EMBL:CAG9475055.1};
OS   Plasmodium vivax.
OC   Eukaryota; Sar; Alveolata; Apicomplexa; Aconoidasida; Haemosporida;
OC   Plasmodiidae; Plasmodium; Plasmodium (Plasmodium).
OX   NCBI_TaxID=5855 {ECO:0000312|EMBL:ACT76164.1};
```

Source SHA-256: `8339b9ac9ad20c1f768a45190d5d148406d577b6def1d323a6b83af3754d12d0`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E6Y8B9?format=txt&versions=78)  
**Locator:** `lines 6-12`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 78 / 1.  
**Retrieved:** 2026-11-02T04:28:06.789132+00:00.  

```text
DE   RecName: Full=Subtilisin-like protease 1 {ECO:0000303|PubMed:37428845, ECO:0000303|PubMed:38386597, ECO:0000303|PubMed:38503166};
DE            EC=3.4.21.62 {ECO:0000269|PubMed:23653352, ECO:0000269|PubMed:25204226, ECO:0000269|PubMed:37428845, ECO:0000269|PubMed:38386597, ECO:0000269|PubMed:38503166};
DE   AltName: Full=PvS1 {ECO:0000303|PubMed:37428845, ECO:0000303|PubMed:38386597, ECO:0000303|PubMed:38503166};
DE   AltName: Full=PvSUB1 {ECO:0000303|PubMed:23653352, ECO:0000303|PubMed:25204226};
DE   AltName: Full=SUB1 protease {ECO:0000303|PubMed:38503166};
DE   AltName: Full=Subtilase SUB1 {ECO:0000303|PubMed:25204226};
DE   Flags: Precursor;
```

Source SHA-256: `8339b9ac9ad20c1f768a45190d5d148406d577b6def1d323a6b83af3754d12d0`.

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E6Y8B9?format=txt&versions=78)  
**Locator:** `lines 91-97`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 78 / 1.  
**Retrieved:** 2026-11-02T04:28:06.789132+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=Hydrolysis of proteins with broad specificity for peptide
CC         bonds, and a preference for a large uncharged residue in P1.
CC         Hydrolyzes peptide amides.; EC=3.4.21.62;
CC         Evidence={ECO:0000269|PubMed:23653352, ECO:0000269|PubMed:25204226,
CC         ECO:0000269|PubMed:37428845, ECO:0000269|PubMed:38386597,
CC         ECO:0000269|PubMed:38503166};
```

Source SHA-256: `8339b9ac9ad20c1f768a45190d5d148406d577b6def1d323a6b83af3754d12d0`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 182. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
