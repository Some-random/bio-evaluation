# EC_number_0112

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `EC_number`  
**Author expected answer:** **B** — 5.6.2.4

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MDINTLLNTPDEDVLSLFTPQVARWFKEKYKVFTPPQKGAIPLIKKGKNVLVSSPTGSGKTLAAFLGILDTLIDLGYKNELNKQIYAIYISPLRALNNDMRRNLIEPLTELRNLYPDLPEISIGVRTSDTSSYEKQKMLKKPPHILITTPESFGISLVSPKFREKLSDVKWVIVDEIHELANSKRGAYLAGLLELYKSFIAKNNFVRIGLSATISPLEEVAKFLVGGNGDYEIIDARFVKPTDIQVVSPVKDLVHATEEEVNIGIYSYLVDEIKKHKTTLIFTNTRHAAERVAYKLRKMFEDQNIFDSDLVAAHHSSLSRDVRLEVEEKLKRGELKVVVSSTSLELGIDIGYIDLVTLLSSPKSVSRLLQRVGRAGHHIREVSKGRVVVVDRDDLVECTVLAKLAIDRKIDNIHVPENPLDVLTQLIVAASLITPIEKDKLYEIIKNVYNFRSLSYDEYNNVAEYLAGNYGLDSNKVYAKIRIKDGMISPKRGTRMIFFLNSGTIPDEAMIPVKMENGGYVGNLEEEFVEILAPGDIFVLAGKTYEFIRSEGNSVIVKKSEGQRPTVPSWFSEMLPLAFDSAIEIGKFRGKIAEAIMNEVPKDEVISSIMSEYNLSRFAALSIYNYVKEELLFTGGIVPTDKLLLIEVYDDDDQNRNFIFHGLYGRRTVDALSRAIAYIISKDLNMDVRIAITDNGFAITVPGKQEYEISKVFDKLEPDKMYEILSDVILRTEMIKRRFRHCAERSFMLLKRYKGRETSIDRRQINSEVLLGVVRQIEHFPVLKETVREILEDYMDIKRAIEIVEKIRNGDIKVATIGPNQVPSPFAHNILVKQYTDVVLAEDKRELLKELHNKVIEFLRNKGIDIDLEYTEAGIK

[Multiple Choices]
A. 5.6.1.1
B. 5.6.2.4
C. 3.2.2.19
D. 5.6.2.1
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

> The exact sequence matches the UniProt entry for Sulfolobus acidocaldarius Lhr-Core. That entry assigns EC 5.6.2.4 and reports ATP-coupled duplex-DNA unwinding, citing experimental evidence (PubMed 26148716). The primary paper was not independently reviewed here.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence’s nucleotide-binding/helicase features can support an ATP-dependent helicase inference and favor the helicase-class choices over unrelated enzyme classes, but they do not establish the exact EC subclass.


**Missing item-specific fact**

> The protein-specific evidence that this Lhr-Core helicase couples ATP hydrolysis to duplex-DNA unwinding, assigned EC 5.6.2.4, rather than the alternative helicase EC 5.6.2.1.


**Reason**

> The exact four-part EC choice depends on the specific substrate/activity classification, which is not supplied in the question. Recognizing the sequence or retrieving its annotation would supply that missing fact.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "D"
]
```

> Both are helicase-class EC choices; the sequence supports a helicase inference but, without protein-specific functional information, does not distinguish these precise subclasses. The reviewer-only evidence supports B for this protein.


### Important caveats

- The sequence-to-entry match is exact, but the accession and database annotation were not supplied to the evaluated model.
- The supporting annotation cites experimental evidence; the cited primary study was not independently assessed.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence’s nucleotide-binding/helicase features can support an ATP-dependent helicase inference and favor the helicase-class choices over unrelated enzyme classes, but they do not establish the exact EC subclass.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific evidence that this Lhr-Core helicase couples ATP hydrolysis to duplex-DNA unwinding, assigned EC 5.6.2.4, rather than the alternative helicase EC 5.6.2.1.",
    "reason": "The exact four-part EC choice depends on the specific substrate/activity classification, which is not supplied in the question. Recognizing the sequence or retrieving its annotation would supply that missing fact."
  },
  "case_id": "EC_number_0112",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry for Sulfolobus acidocaldarius Lhr-Core. That entry assigns EC 5.6.2.4 and reports ATP-coupled duplex-DNA unwinding, citing experimental evidence (PubMed 26148716). The primary paper was not independently reviewed here."
  },
  "important_caveats": [
    "The sequence-to-entry match is exact, but the accession and database annotation were not supplied to the evaluated model.",
    "The supporting annotation cites experimental evidence; the cited primary study was not independently assessed."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "D"
    ],
    "reason": "Both are helicase-class EC choices; the sequence supports a helicase inference but, without protein-specific functional information, does not distinguish these precise subclasses. The reviewer-only evidence supports B for this protein."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0112",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry for Sulfolobus acidocaldarius Lhr-Core. That entry assigns EC 5.6.2.4 and reports ATP-coupled duplex-DNA unwinding, citing experimental evidence (PubMed 26148716). The primary paper was not independently reviewed here.",
    "evidence_ids": ["C1", "C4", "C5", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence’s nucleotide-binding/helicase features can support an ATP-dependent helicase inference and favor the helicase-class choices over unrelated enzyme classes, but they do not establish the exact EC subclass.",
    "missing_item_specific_fact": "The protein-specific evidence that this Lhr-Core helicase couples ATP hydrolysis to duplex-DNA unwinding, assigned EC 5.6.2.4, rather than the alternative helicase EC 5.6.2.1.",
    "reason": "The exact four-part EC choice depends on the specific substrate/activity classification, which is not supplied in the question. Recognizing the sequence or retrieving its annotation would supply that missing fact."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "D"],
    "reason": "Both are helicase-class EC choices; the sequence supports a helicase inference but, without protein-specific functional information, does not distinguish these precise subclasses. The reviewer-only evidence supports B for this protein."
  },
  "important_caveats": [
    "The sequence-to-entry match is exact, but the accession and database annotation were not supplied to the evaluated model.",
    "The supporting annotation cites experimental evidence; the cited primary study was not independently assessed."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry Q4J8R1 (LHRC_SULAC) assigns EC 5.6.2.4 to this exact 876-aa sequence (SHA256 match confirmed) with evidence code ECO:0000269 (inferred from direct assay) from PubMed:26148716 (van Wolferen et al., J. Bacteriol. 2015). The catalytic activity is described as coupling ATP hydrolysis with unwinding of duplex DNA in the 3'→5' direction. The Swiss-Prot reviewed annotation and experimental evidence code strongly support the expected answer.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence contains a clear Walker A / P-loop motif (GSGKTLAAFLGILDT), which supports classification as an ATP-dependent helicase and effectively eliminates choice C (3.2.2.19, a glycosylase that lacks P-loop motifs). However, the remaining choices A (5.6.1.1, 5'→3' DNA helicase), B (5.6.2.4, 3'→5' DNA helicase of a specific subfamily), and D (5.6.2.1, 3'→5' DNA helicase of another subfamily) all describe ATP-dependent DNA helicases. Distinguishing among them requires knowing the specific helicase superfamily/subfamily assignment and translocation polarity, which is not derivable from general sequence features alone.


**Missing item-specific fact**

> The specific helicase subfamily identity (Lhr-Core, an archaeal 3'→5' DNA helicase) and the EC classification boundary between 5.6.2.1 and 5.6.2.4, which depends on knowing that this particular protein belongs to the subfamily assigned EC 5.6.2.4 rather than 5.6.2.1. This is a database annotation fact not inferable from the sequence by general biological reasoning.


**Reason**

> While the Walker A motif permits elimination of the glycosylase option (C), the critical discrimination among the three helicase EC numbers (A, B, D) depends on identifying the exact helicase subfamily and its assigned EC number. The EC 5.6.2.4 vs 5.6.2.1 distinction is a fine-grained taxonomic assignment within the 3'→5' DNA helicase class that requires item-specific database knowledge rather than general biochemical reasoning from the sequence.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Choice C is clearly eliminable by the presence of the Walker A P-loop motif. Choices A, B, and D are all helicase EC numbers but differ in directionality and subfamily assignment. Without database knowledge, a solver cannot reliably distinguish 5.6.2.4 from 5.6.2.1 or from 5.6.1.1 based on sequence alone, but the author's key is uniquely correct per the experimental annotation.


### Important caveats

- The identity of the protein (Q4J8R1, Lhr-Core) was inferred from reviewer-only metadata and was not provided to the evaluated model.
- The EC 5.6.2.4 annotation carries evidence code ECO:0000269 (direct assay), indicating experimental support rather than purely computational transfer.
- The Walker A motif provides partial reasoning (eliminating the glycosylase), but the precise 4-digit EC number assignment among helicase subfamilies remains lookup-dependent.
- EC 5.6.2.4 is a relatively recently defined EC number; its boundaries with 5.6.2.1 may reflect taxonomic curation decisions not obvious from sequence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a clear Walker A / P-loop motif (GSGKTLAAFLGILDT), which supports classification as an ATP-dependent helicase and effectively eliminates choice C (3.2.2.19, a glycosylase that lacks P-loop motifs). However, the remaining choices A (5.6.1.1, 5'→3' DNA helicase), B (5.6.2.4, 3'→5' DNA helicase of a specific subfamily), and D (5.6.2.1, 3'→5' DNA helicase of another subfamily) all describe ATP-dependent DNA helicases. Distinguishing among them requires knowing the specific helicase superfamily/subfamily assignment and translocation polarity, which is not derivable from general sequence features alone.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific helicase subfamily identity (Lhr-Core, an archaeal 3'→5' DNA helicase) and the EC classification boundary between 5.6.2.1 and 5.6.2.4, which depends on knowing that this particular protein belongs to the subfamily assigned EC 5.6.2.4 rather than 5.6.2.1. This is a database annotation fact not inferable from the sequence by general biological reasoning.",
    "reason": "While the Walker A motif permits elimination of the glycosylase option (C), the critical discrimination among the three helicase EC numbers (A, B, D) depends on identifying the exact helicase subfamily and its assigned EC number. The EC 5.6.2.4 vs 5.6.2.1 distinction is a fine-grained taxonomic assignment within the 3'→5' DNA helicase class that requires item-specific database knowledge rather than general biochemical reasoning from the sequence."
  },
  "case_id": "EC_number_0112",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C7",
      "H1",
      "H2",
      "H3",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "UniProt entry Q4J8R1 (LHRC_SULAC) assigns EC 5.6.2.4 to this exact 876-aa sequence (SHA256 match confirmed) with evidence code ECO:0000269 (inferred from direct assay) from PubMed:26148716 (van Wolferen et al., J. Bacteriol. 2015). The catalytic activity is described as coupling ATP hydrolysis with unwinding of duplex DNA in the 3'→5' direction. The Swiss-Prot reviewed annotation and experimental evidence code strongly support the expected answer."
  },
  "important_caveats": [
    "The identity of the protein (Q4J8R1, Lhr-Core) was inferred from reviewer-only metadata and was not provided to the evaluated model.",
    "The EC 5.6.2.4 annotation carries evidence code ECO:0000269 (direct assay), indicating experimental support rather than purely computational transfer.",
    "The Walker A motif provides partial reasoning (eliminating the glycosylase), but the precise 4-digit EC number assignment among helicase subfamilies remains lookup-dependent.",
    "EC 5.6.2.4 is a relatively recently defined EC number; its boundaries with 5.6.2.1 may reflect taxonomic curation decisions not obvious from sequence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Choice C is clearly eliminable by the presence of the Walker A P-loop motif. Choices A, B, and D are all helicase EC numbers but differ in directionality and subfamily assignment. Without database knowledge, a solver cannot reliably distinguish 5.6.2.4 from 5.6.2.1 or from 5.6.1.1 based on sequence alone, but the author's key is uniquely correct per the experimental annotation."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0112",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry Q4J8R1 (LHRC_SULAC) assigns EC 5.6.2.4 to this exact 876-aa sequence (SHA256 match confirmed) with evidence code ECO:0000269 (inferred from direct assay) from PubMed:26148716 (van Wolferen et al., J. Bacteriol. 2015). The catalytic activity is described as coupling ATP hydrolysis with unwinding of duplex DNA in the 3'→5' direction. The Swiss-Prot reviewed annotation and experimental evidence code strongly support the expected answer.",
    "evidence_ids": ["C4", "C5", "C6", "C7", "H1", "H2", "H3", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence contains a clear Walker A / P-loop motif (GSGKTLAAFLGILDT), which supports classification as an ATP-dependent helicase and effectively eliminates choice C (3.2.2.19, a glycosylase that lacks P-loop motifs). However, the remaining choices A (5.6.1.1, 5'→3' DNA helicase), B (5.6.2.4, 3'→5' DNA helicase of a specific subfamily), and D (5.6.2.1, 3'→5' DNA helicase of another subfamily) all describe ATP-dependent DNA helicases. Distinguishing among them requires knowing the specific helicase superfamily/subfamily assignment and translocation polarity, which is not derivable from general sequence features alone.",
    "missing_item_specific_fact": "The specific helicase subfamily identity (Lhr-Core, an archaeal 3'→5' DNA helicase) and the EC classification boundary between 5.6.2.1 and 5.6.2.4, which depends on knowing that this particular protein belongs to the subfamily assigned EC 5.6.2.4 rather than 5.6.2.1. This is a database annotation fact not inferable from the sequence by general biological reasoning.",
    "reason": "While the Walker A motif permits elimination of the glycosylase option (C), the critical discrimination among the three helicase EC numbers (A, B, D) depends on identifying the exact helicase subfamily and its assigned EC number. The EC 5.6.2.4 vs 5.6.2.1 distinction is a fine-grained taxonomic assignment within the 3'→5' DNA helicase class that requires item-specific database knowledge rather than general biochemical reasoning from the sequence."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Choice C is clearly eliminable by the presence of the Walker A P-loop motif. Choices A, B, and D are all helicase EC numbers but differ in directionality and subfamily assignment. Without database knowledge, a solver cannot reliably distinguish 5.6.2.4 from 5.6.2.1 or from 5.6.1.1 based on sequence alone, but the author's key is uniquely correct per the experimental annotation."
  },
  "important_caveats": [
    "The identity of the protein (Q4J8R1, Lhr-Core) was inferred from reviewer-only metadata and was not provided to the evaluated model.",
    "The EC 5.6.2.4 annotation carries evidence code ECO:0000269 (direct assay), indicating experimental support rather than purely computational transfer.",
    "The Walker A motif provides partial reasoning (eliminating the glycosylase), but the precise 4-digit EC number assignment among helicase subfamilies remains lookup-dependent.",
    "EC 5.6.2.4 is a relatively recently defined EC number; its boundaries with 5.6.2.1 may reflect taxonomic curation decisions not obvious from sequence."
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

**Accession:** `Q4J8R1` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 118. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4J8R1.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:21.183785+00:00.  

```json
"Q4J8R1"
```

Source SHA-256: `5ddd2fdfa837dd562dc14520d20c460d760536e004fc18e055f36fb419e215a4`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4J8R1.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:21.183785+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"DNA 3'-5' helicase Lhr-Core"}},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"26148716","source":"PubMed"}],"value":"DNA 3'-5' helicase Saci_1500"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"26148716","source":"PubMed"}],"value":"5.6.2.4"}],"fullName":{"value":"ATP-dependent helicase Lhr-Core"}}}
```

Source SHA-256: `5ddd2fdfa837dd562dc14520d20c460d760536e004fc18e055f36fb419e215a4`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4J8R1.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:21.183785+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"5.6.2.4","evidences":[{"evidenceCode":"ECO:0000269","id":"26148716","source":"PubMed"}],"name":"Couples ATP hydrolysis with the unwinding of duplex DNA by translocating in the 3'-5' direction."}}
```

Source SHA-256: `5ddd2fdfa837dd562dc14520d20c460d760536e004fc18e055f36fb419e215a4`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4J8R1.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:21.183785+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"5.6.2.4","evidences":[{"evidenceCode":"ECO:0000305","id":"26148716","source":"PubMed"}],"name":"ATP + H2O = ADP + phosphate + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:13065"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:30616"},{"database":"ChEBI","id":"CHEBI:43474"},{"database":"ChEBI","id":"CHEBI:456216"}]}}
```

Source SHA-256: `5ddd2fdfa837dd562dc14520d20c460d760536e004fc18e055f36fb419e215a4`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4J8R1.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:21.183785+00:00.  

```json
{"citation":{"authors":["van Wolferen M.","Ma X.","Albers S.V."],"citationCrossReferences":[{"database":"PubMed","id":"26148716"},{"database":"DOI","id":"10.1128/jb.00344-15"}],"citationType":"journal article","firstPage":"2941","id":"26148716","journal":"J. Bacteriol.","lastPage":"2951","publicationDate":"2015","title":"DNA Processing Proteins Involved in the UV-Induced Stress Response of Sulfolobales.","volume":"197"},"referenceComments":[{"type":"STRAIN","value":"ATCC 33909 / DSM 639 / JCM 8929 / NBRC 15157 / NCIMB 11770"}],"referenceNumber":2,"referencePositions":["FUNCTION AS A HELICASE","CATALYTIC ACTIVITY","DISRUPTION PHENOTYPE","DNA-BINDING","MUTAGENESIS OF LYS-60"]}
```

Source SHA-256: `5ddd2fdfa837dd562dc14520d20c460d760536e004fc18e055f36fb419e215a4`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q4J8R1?format=txt&versions=118)  
**Locator:** `lines 1-15`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 118 / 1.  
**Retrieved:** 2026-11-01T06:28:33.887619+00:00.  

```text
ID   LHRC_SULAC              Reviewed;         876 AA.
AC   Q4J8R1;
DT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.
DT   02-AUG-2005, sequence version 1.
DT   28-JAN-2026, entry version 118.
DE   RecName: Full=ATP-dependent helicase Lhr-Core;
DE            EC=5.6.2.4 {ECO:0000269|PubMed:26148716};
DE   AltName: Full=DNA 3'-5' helicase Lhr-Core {ECO:0000305};
DE   AltName: Full=DNA 3'-5' helicase Saci_1500 {ECO:0000303|PubMed:26148716};
GN   OrderedLocusNames=Saci_1500 {ECO:0000312|EMBL:AAY80821.1};
OS   Sulfolobus acidocaldarius (strain ATCC 33909 / DSM 639 / JCM 8929 / NBRC
OS   15157 / NCIMB 11770).
OC   Archaea; Thermoproteota; Thermoprotei; Sulfolobales; Sulfolobaceae;
OC   Sulfolobus.
OX   NCBI_TaxID=330779;
```

Source SHA-256: `e13a189773cd9bc8187d4ff73efc59a3b0cfa535f19e4a03d9e5c43501c05855`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q4J8R1?format=txt&versions=118)  
**Locator:** `lines 6-9`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 118 / 1.  
**Retrieved:** 2026-11-01T06:28:33.887619+00:00.  

```text
DE   RecName: Full=ATP-dependent helicase Lhr-Core;
DE            EC=5.6.2.4 {ECO:0000269|PubMed:26148716};
DE   AltName: Full=DNA 3'-5' helicase Lhr-Core {ECO:0000305};
DE   AltName: Full=DNA 3'-5' helicase Saci_1500 {ECO:0000303|PubMed:26148716};
```

Source SHA-256: `e13a189773cd9bc8187d4ff73efc59a3b0cfa535f19e4a03d9e5c43501c05855`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q4J8R1?format=txt&versions=118)  
**Locator:** `lines 25-33`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 118 / 1.  
**Retrieved:** 2026-11-01T06:28:33.887619+00:00.  

```text
RN   [2]
RP   FUNCTION AS A HELICASE, CATALYTIC ACTIVITY, DISRUPTION PHENOTYPE,
RP   DNA-BINDING, AND MUTAGENESIS OF LYS-60.
RC   STRAIN=ATCC 33909 / DSM 639 / JCM 8929 / NBRC 15157 / NCIMB 11770;
RX   PubMed=26148716; DOI=10.1128/jb.00344-15;
RA   van Wolferen M., Ma X., Albers S.V.;
RT   "DNA Processing Proteins Involved in the UV-Induced Stress Response of
RT   Sulfolobales.";
RL   J. Bacteriol. 197:2941-2951(2015).
```

Source SHA-256: `e13a189773cd9bc8187d4ff73efc59a3b0cfa535f19e4a03d9e5c43501c05855`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q4J8R1?format=txt&versions=118)  
**Locator:** `lines 45-48`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 118 / 1.  
**Retrieved:** 2026-11-01T06:28:33.887619+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=Couples ATP hydrolysis with the unwinding of duplex DNA by
CC         translocating in the 3'-5' direction.; EC=5.6.2.4;
CC         Evidence={ECO:0000269|PubMed:26148716};
```

Source SHA-256: `e13a189773cd9bc8187d4ff73efc59a3b0cfa535f19e4a03d9e5c43501c05855`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q4J8R1?format=txt&versions=118)  
**Locator:** `lines 49-53`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 118 / 1.  
**Retrieved:** 2026-11-01T06:28:33.887619+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=ATP + H2O = ADP + phosphate + H(+); Xref=Rhea:RHEA:13065,
CC         ChEBI:CHEBI:15377, ChEBI:CHEBI:15378, ChEBI:CHEBI:30616,
CC         ChEBI:CHEBI:43474, ChEBI:CHEBI:456216; EC=5.6.2.4;
CC         Evidence={ECO:0000305|PubMed:26148716};
```

Source SHA-256: `e13a189773cd9bc8187d4ff73efc59a3b0cfa535f19e4a03d9e5c43501c05855`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 112. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
