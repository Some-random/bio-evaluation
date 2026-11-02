# catalytic_activity_0153

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `catalytic_activity`  
**Author expected answer:** **A** — methylarsonous acid + AH2 + O2 = arsenite + methanol + A + H(+)

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MKYAHVGLNVTNLEKSIEFYSKLFGAEPVKVKPDYAKFLLESPGLNFTLNLRDEVNGNQVGHFGIQVESTEEVVAHKNRLAENGILSQYDEINTTCCYALQDKFWIHDPDGNEWEFFYTKTTVEENSTHPPTCCVNEPNVEKAECCSPTASSNKDTSNCCS

[Multiple Choices]
A. methylarsonous acid + AH2 + O2 = arsenite + methanol + A + H(+)
B. L-fucose + NAD(+) = L-fucono-1,5-lactone + NADH + H(+)
C. L-fucose + ATP = beta-L-fucose 1-phosphate + ADP + H(+)
D. dUMP + ATP = dUDP + ADP
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

> The supplied sequence exactly matches the UniProt entry for this protein, whose catalytic-activity annotation gives option A and cites experimental evidence from two publications (ECO:0000269).

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The choices describe distinct enzyme activities, but the sequence and prompt provide no biological context that meaningfully identifies this protein as an organoarsenical-cleaving enzyme rather than an enzyme for one of the other listed reactions.


**Missing item-specific fact**

> The protein's identity or experimentally established catalytic function, specifically that it catalyzes methylarsonous acid demethylation.


**Reason**

> Selecting A requires a protein-specific functional annotation or prior knowledge of this enzyme; recognizing the sequence or recalling its database entry is not reasoning from information supplied in the question.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The evidence supports option A among the listed reactions; the other choices are different transformations.


### Important caveats

- The reviewer-only evidence supports the expected answer but was not supplied to the evaluated model.
- The cited experimental evidence is represented in database annotations; the primary papers were not independently reviewed here.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The choices describe distinct enzyme activities, but the sequence and prompt provide no biological context that meaningfully identifies this protein as an organoarsenical-cleaving enzyme rather than an enzyme for one of the other listed reactions.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein's identity or experimentally established catalytic function, specifically that it catalyzes methylarsonous acid demethylation.",
    "reason": "Selecting A requires a protein-specific functional annotation or prior knowledge of this enzyme; recognizing the sequence or recalling its database entry is not reasoning from information supplied in the question."
  },
  "case_id": "catalytic_activity_0153",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the UniProt entry for this protein, whose catalytic-activity annotation gives option A and cites experimental evidence from two publications (ECO:0000269)."
  },
  "important_caveats": [
    "The reviewer-only evidence supports the expected answer but was not supplied to the evaluated model.",
    "The cited experimental evidence is represented in database annotations; the primary papers were not independently reviewed here."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The evidence supports option A among the listed reactions; the other choices are different transformations."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0153",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the UniProt entry for this protein, whose catalytic-activity annotation gives option A and cites experimental evidence from two publications (ECO:0000269).",
    "evidence_ids": ["C1", "C5", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The choices describe distinct enzyme activities, but the sequence and prompt provide no biological context that meaningfully identifies this protein as an organoarsenical-cleaving enzyme rather than an enzyme for one of the other listed reactions.",
    "missing_item_specific_fact": "The protein's identity or experimentally established catalytic function, specifically that it catalyzes methylarsonous acid demethylation.",
    "reason": "Selecting A requires a protein-specific functional annotation or prior knowledge of this enzyme; recognizing the sequence or recalling its database entry is not reasoning from information supplied in the question."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The evidence supports option A among the listed reactions; the other choices are different transformations."
  },
  "important_caveats": [
    "The reviewer-only evidence supports the expected answer but was not supplied to the evaluated model.",
    "The cited experimental evidence is represented in database annotations; the primary papers were not independently reviewed here."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The benchmark sequence (161 aa, SHA256 630a5e10…) matches UniProt entry A0A059WI14 (ARSI_BACX0) exactly in both current (v23) and historical (v22) snapshots. The entry is annotated as 'Trivalent organoarsenical cleaving enzyme' / 'C-As lyase' / 'Methylarsonous acid demethylase' (EC 1.13.11.-) with the catalytic activity 'methylarsonous acid + AH2 + O2 = arsenite + methanol + A + H(+)' supported by direct experimental evidence (ECO:0000269, PubMed 24821808 and 28936873). The expected answer A is the primary listed reaction and matches the Rhea:82323/82324 annotation verbatim.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C9](#evidence-c9), [C10](#evidence-c10), [H1](#evidence-h1), [H2](#evidence-h2), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> A weak elimination argument exists: the 161-aa sequence lacks a canonical Rossmann-fold NAD-binding motif (disfavouring option B, a dehydrogenase), and lacks a P-loop/GxGxxG kinase motif or VAIK catalytic residues (disfavouring options C and D, both ATP-dependent kinases). The cysteine-rich C-terminal region (…CCSPTASSNKDTSNCCS) is loosely consistent with a metalloenzyme/redox-active site. However, these are generic negative observations; many small or structurally unusual enzymes catalyse kinase or dehydrogenase reactions without canonical motifs.


**Missing item-specific fact**

> Positive identification of the protein as a C-As lyase (ArsI) that cleaves the methyl–arsenic bond of methylarsonous acid requires knowledge of this specific enzyme family or its sequence signature. The C-As lyase reaction is exceedingly rare and not covered in standard biochemistry curricula; no widely-taught sequence motif (e.g., a conserved catalytic tetrad or substrate-binding pocket) allows a model to positively assign 'methylarsonous acid demethylase' activity from a 161-residue sequence without database lookup or prior memorization of ArsI.


**Reason**

> While absence of kinase and dehydrogenase motifs provides weak negative reasoning to disfavour B, C, and D, the positive identification of the correct reaction (A) hinges on recognizing this particular protein or knowing the sequence hallmarks of the C-As lyase family—both item-specific facts absent from the supplied input. The question therefore depends on memorization or external annotation lookup rather than general biological reasoning.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Once the protein is identified as ArsI, option A is unambiguously correct. The three distractors (fucose dehydrogenase, fucose kinase, dUMP kinase) belong to entirely different enzyme classes and metabolic pathways with no plausible overlap with arsenic C–As bond cleavage. No ambiguity exists among the choices given the correct protein identity.


### Important caveats

- The UniProt annotation for A0A059WI14 was first publicly released on 2025-04-09; the exact author construction date is unknown, so the annotation may or may not have been available when the benchmark was assembled.
- The identity of the accession was inferred mechanically from dataset image-path metadata (reviewer-only); it was not supplied to the evaluated model.
- The C-As lyase reaction is supported by in vitro biochemical assays (ECO:0000269) from two independent publications, giving it strong experimental backing beyond computational inference.
- The EC number 1.13.11.- is still incomplete (the specific sub-subclass digits are undetermined), reflecting the novelty of this enzyme class.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "A weak elimination argument exists: the 161-aa sequence lacks a canonical Rossmann-fold NAD-binding motif (disfavouring option B, a dehydrogenase), and lacks a P-loop/GxGxxG kinase motif or VAIK catalytic residues (disfavouring options C and D, both ATP-dependent kinases). The cysteine-rich C-terminal region (…CCSPTASSNKDTSNCCS) is loosely consistent with a metalloenzyme/redox-active site. However, these are generic negative observations; many small or structurally unusual enzymes catalyse kinase or dehydrogenase reactions without canonical motifs.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "Positive identification of the protein as a C-As lyase (ArsI) that cleaves the methyl–arsenic bond of methylarsonous acid requires knowledge of this specific enzyme family or its sequence signature. The C-As lyase reaction is exceedingly rare and not covered in standard biochemistry curricula; no widely-taught sequence motif (e.g., a conserved catalytic tetrad or substrate-binding pocket) allows a model to positively assign 'methylarsonous acid demethylase' activity from a 161-residue sequence without database lookup or prior memorization of ArsI.",
    "reason": "While absence of kinase and dehydrogenase motifs provides weak negative reasoning to disfavour B, C, and D, the positive identification of the correct reaction (A) hinges on recognizing this particular protein or knowing the sequence hallmarks of the C-As lyase family—both item-specific facts absent from the supplied input. The question therefore depends on memorization or external annotation lookup rather than general biological reasoning."
  },
  "case_id": "catalytic_activity_0153",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C9",
      "C10",
      "H1",
      "H2",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The benchmark sequence (161 aa, SHA256 630a5e10…) matches UniProt entry A0A059WI14 (ARSI_BACX0) exactly in both current (v23) and historical (v22) snapshots. The entry is annotated as 'Trivalent organoarsenical cleaving enzyme' / 'C-As lyase' / 'Methylarsonous acid demethylase' (EC 1.13.11.-) with the catalytic activity 'methylarsonous acid + AH2 + O2 = arsenite + methanol + A + H(+)' supported by direct experimental evidence (ECO:0000269, PubMed 24821808 and 28936873). The expected answer A is the primary listed reaction and matches the Rhea:82323/82324 annotation verbatim."
  },
  "important_caveats": [
    "The UniProt annotation for A0A059WI14 was first publicly released on 2025-04-09; the exact author construction date is unknown, so the annotation may or may not have been available when the benchmark was assembled.",
    "The identity of the accession was inferred mechanically from dataset image-path metadata (reviewer-only); it was not supplied to the evaluated model.",
    "The C-As lyase reaction is supported by in vitro biochemical assays (ECO:0000269) from two independent publications, giving it strong experimental backing beyond computational inference.",
    "The EC number 1.13.11.- is still incomplete (the specific sub-subclass digits are undetermined), reflecting the novelty of this enzyme class."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Once the protein is identified as ArsI, option A is unambiguously correct. The three distractors (fucose dehydrogenase, fucose kinase, dUMP kinase) belong to entirely different enzyme classes and metabolic pathways with no plausible overlap with arsenic C–As bond cleavage. No ambiguity exists among the choices given the correct protein identity."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0153",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The benchmark sequence (161 aa, SHA256 630a5e10…) matches UniProt entry A0A059WI14 (ARSI_BACX0) exactly in both current (v23) and historical (v22) snapshots. The entry is annotated as 'Trivalent organoarsenical cleaving enzyme' / 'C-As lyase' / 'Methylarsonous acid demethylase' (EC 1.13.11.-) with the catalytic activity 'methylarsonous acid + AH2 + O2 = arsenite + methanol + A + H(+)' supported by direct experimental evidence (ECO:0000269, PubMed 24821808 and 28936873). The expected answer A is the primary listed reaction and matches the Rhea:82323/82324 annotation verbatim.",
    "evidence_ids": ["C1", "C4", "C5", "C9", "C10", "H1", "H2", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "A weak elimination argument exists: the 161-aa sequence lacks a canonical Rossmann-fold NAD-binding motif (disfavouring option B, a dehydrogenase), and lacks a P-loop/GxGxxG kinase motif or VAIK catalytic residues (disfavouring options C and D, both ATP-dependent kinases). The cysteine-rich C-terminal region (…CCSPTASSNKDTSNCCS) is loosely consistent with a metalloenzyme/redox-active site. However, these are generic negative observations; many small or structurally unusual enzymes catalyse kinase or dehydrogenase reactions without canonical motifs.",
    "missing_item_specific_fact": "Positive identification of the protein as a C-As lyase (ArsI) that cleaves the methyl–arsenic bond of methylarsonous acid requires knowledge of this specific enzyme family or its sequence signature. The C-As lyase reaction is exceedingly rare and not covered in standard biochemistry curricula; no widely-taught sequence motif (e.g., a conserved catalytic tetrad or substrate-binding pocket) allows a model to positively assign 'methylarsonous acid demethylase' activity from a 161-residue sequence without database lookup or prior memorization of ArsI.",
    "reason": "While absence of kinase and dehydrogenase motifs provides weak negative reasoning to disfavour B, C, and D, the positive identification of the correct reaction (A) hinges on recognizing this particular protein or knowing the sequence hallmarks of the C-As lyase family—both item-specific facts absent from the supplied input. The question therefore depends on memorization or external annotation lookup rather than general biological reasoning."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Once the protein is identified as ArsI, option A is unambiguously correct. The three distractors (fucose dehydrogenase, fucose kinase, dUMP kinase) belong to entirely different enzyme classes and metabolic pathways with no plausible overlap with arsenic C–As bond cleavage. No ambiguity exists among the choices given the correct protein identity."
  },
  "important_caveats": [
    "The UniProt annotation for A0A059WI14 was first publicly released on 2025-04-09; the exact author construction date is unknown, so the annotation may or may not have been available when the benchmark was assembled.",
    "The identity of the accession was inferred mechanically from dataset image-path metadata (reviewer-only); it was not supplied to the evaluated model.",
    "The C-As lyase reaction is supported by in vitro biochemical assays (ECO:0000269) from two independent publications, giving it strong experimental backing beyond computational inference.",
    "The EC number 1.13.11.- is still incomplete (the specific sub-subclass digits are undetermined), reflecting the novelty of this enzyme class."
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

**Accession:** `A0A059WI14` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 22. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A059WI14.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:23:54.040783+00:00.  

```json
"A0A059WI14"
```

Source SHA-256: `8f03a35522b3d82d736a708e66977d0e99c44951c0c098514a18248bc8c22f4e`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A059WI14.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:23:54.040783+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"24821808","source":"PubMed"}],"value":"Arsenic inducible gene ArsI"}},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"24821808","source":"PubMed"},{"evidenceCode":"ECO:0000303","id":"28936873","source":"PubMed"}],"value":"C-As lyase"}},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"24821808","source":"PubMed"}],"value":"Methylarsonous acid demethylase"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"24821808","source":"PubMed"}],"value":"MAs(III) demethylase"}]}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"24821808","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"28936873","source":"PubMed"}],"value":"1.13.11.-"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305","id":"24821808","source":"PubMed"}],"value":"Trivalent organoarsenical cleaving enzyme"}}}
```

Source SHA-256: `8f03a35522b3d82d736a708e66977d0e99c44951c0c098514a18248bc8c22f4e`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A059WI14.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:23:54.040783+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000269","id":"24821808","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:82324"}}],"reaction":{"evidences":[{"evidenceCode":"ECO:0000269","id":"24821808","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"28936873","source":"PubMed"}],"name":"methylarsonous acid + AH2 + O2 = arsenite + methanol + A + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:82323"},{"database":"ChEBI","id":"CHEBI:13193"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:15379"},{"database":"ChEBI","id":"CHEBI:17499"},{"database":"ChEBI","id":"CHEBI:17790"},{"database":"ChEBI","id":"CHEBI:17826"},{"database":"ChEBI","id":"CHEBI:29242"}]}}
```

Source SHA-256: `8f03a35522b3d82d736a708e66977d0e99c44951c0c098514a18248bc8c22f4e`.

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A059WI14.json)  
**Locator:** `/references/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:23:54.040783+00:00.  

```json
{"citation":{"authors":["Yoshinaga M.","Rosen B.P."],"citationCrossReferences":[{"database":"PubMed","id":"24821808"},{"database":"DOI","id":"10.1073/pnas.1403057111"}],"citationType":"journal article","firstPage":"7701","id":"24821808","journal":"Proc. Natl. Acad. Sci. U.S.A.","lastPage":"7706","publicationDate":"2014","title":"A C-As lyase for degradation of environmental organoarsenical herbicides and animal husbandry growth promoters.","volume":"111"},"referenceComments":[{"type":"STRAIN","value":"MD1"}],"referenceNumber":1,"referencePositions":["NUCLEOTIDE SEQUENCE [GENOMIC DNA]","FUNCTION","CATALYTIC ACTIVITY","COFACTOR","BIOPHYSICOCHEMICAL PROPERTIES"]}
```

Source SHA-256: `8f03a35522b3d82d736a708e66977d0e99c44951c0c098514a18248bc8c22f4e`.

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A059WI14.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:23:54.040783+00:00.  

```json
{"citation":{"authors":["Pawitwar S.S.","Nadar V.S.","Kandegedara A.","Stemmler T.L.","Rosen B.P.","Yoshinaga M."],"citationCrossReferences":[{"database":"PubMed","id":"28936873"},{"database":"DOI","id":"10.1021/acs.est.7b03180"}],"citationType":"journal article","firstPage":"11115","id":"28936873","journal":"Environ. Sci. Technol.","lastPage":"11125","publicationDate":"2017","title":"Biochemical Characterization of ArsI: A Novel C-As Lyase for Degradation of Environmental Organoarsenicals.","volume":"51"},"referenceComments":[{"type":"STRAIN","value":"MD1"}],"referenceNumber":2,"referencePositions":["FUNCTION","CATALYTIC ACTIVITY","COFACTOR","ACTIVITY REGULATION","3D-STRUCTURE MODELING","MUTAGENESIS OF HIS-5; HIS-62; 96-CYS-CYS-97 AND GLU-115"]}
```

Source SHA-256: `8f03a35522b3d82d736a708e66977d0e99c44951c0c098514a18248bc8c22f4e`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A059WI14?format=txt&versions=22)  
**Locator:** `lines 1-15`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 22 / 1.  
**Retrieved:** 2026-11-02T04:23:56.065730+00:00.  

```text
ID   ARSI_BACX0              Reviewed;         161 AA.
AC   A0A059WI14;
DT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.
DT   03-SEP-2014, sequence version 1.
DT   28-JAN-2026, entry version 22.
DE   RecName: Full=Trivalent organoarsenical cleaving enzyme {ECO:0000305|PubMed:24821808};
DE            EC=1.13.11.- {ECO:0000269|PubMed:24821808, ECO:0000269|PubMed:28936873};
DE   AltName: Full=Arsenic inducible gene ArsI {ECO:0000303|PubMed:24821808};
DE   AltName: Full=C-As lyase {ECO:0000303|PubMed:24821808, ECO:0000303|PubMed:28936873};
DE   AltName: Full=Methylarsonous acid demethylase {ECO:0000303|PubMed:24821808};
DE            Short=MAs(III) demethylase {ECO:0000303|PubMed:24821808};
GN   Name=arsI {ECO:0000303|PubMed:24821808, ECO:0000312|EMBL:AIA09488.1};
OS   Bacillus sp. (strain MD1).
OC   Bacteria; Bacillati; Bacillota; Bacilli; Bacillales; Bacillaceae; Bacillus.
OX   NCBI_TaxID=1501233;
```

Source SHA-256: `64b679b08c78f78bd0eefc397743cd9c2b8ee062794e951deec5c900823833d7`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A059WI14?format=txt&versions=22)  
**Locator:** `lines 6-11`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 22 / 1.  
**Retrieved:** 2026-11-02T04:23:56.065730+00:00.  

```text
DE   RecName: Full=Trivalent organoarsenical cleaving enzyme {ECO:0000305|PubMed:24821808};
DE            EC=1.13.11.- {ECO:0000269|PubMed:24821808, ECO:0000269|PubMed:28936873};
DE   AltName: Full=Arsenic inducible gene ArsI {ECO:0000303|PubMed:24821808};
DE   AltName: Full=C-As lyase {ECO:0000303|PubMed:24821808, ECO:0000303|PubMed:28936873};
DE   AltName: Full=Methylarsonous acid demethylase {ECO:0000303|PubMed:24821808};
DE            Short=MAs(III) demethylase {ECO:0000303|PubMed:24821808};
```

Source SHA-256: `64b679b08c78f78bd0eefc397743cd9c2b8ee062794e951deec5c900823833d7`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A059WI14?format=txt&versions=22)  
**Locator:** `lines 46-53`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 22 / 1.  
**Retrieved:** 2026-11-02T04:23:56.065730+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=methylarsonous acid + AH2 + O2 = arsenite + methanol + A +
CC         H(+); Xref=Rhea:RHEA:82323, ChEBI:CHEBI:13193, ChEBI:CHEBI:15378,
CC         ChEBI:CHEBI:15379, ChEBI:CHEBI:17499, ChEBI:CHEBI:17790,
CC         ChEBI:CHEBI:17826, ChEBI:CHEBI:29242;
CC         Evidence={ECO:0000269|PubMed:24821808, ECO:0000269|PubMed:28936873};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:82324;
CC         Evidence={ECO:0000269|PubMed:24821808};
```

Source SHA-256: `64b679b08c78f78bd0eefc397743cd9c2b8ee062794e951deec5c900823833d7`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 153. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
