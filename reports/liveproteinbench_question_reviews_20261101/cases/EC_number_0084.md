# EC_number_0084

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `EC_number`  
**Author expected answer:** **C** — 2.5.1.56

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MKEIKIQNIIINEEKAPLVVPEIGINHNGSLELAKIMVDAAFSAGAKIIKHQTHIVEDEMSKAAKKVIPGNAKISIYEIMQKCALDYKDELALKEYTEKLGLVYLSTPFSRAGANRLEDMGVSAFKIGSGECNNYPLIKHIAAFKKPMIVSTGMNSIESIKPTVKILLDNEIPFVLMHTTNLYPTPHNLVRLNAMLELKKEFSCMVGLSDHTTDNLACLGAVALGACVLERHFTDSMDRSGPDIVCSMDTKALKELIMQSEQMAIMRGNNESKKAAKQEQVTIDFAFASVVSIKDIKKGEVLSMDNIWVKRPGLGGISAAEFENILGKKALRDIENDTQLSYEDFA

[Multiple Choices]
A. 2.5.1.76
B. 2.7.11.24
C. 2.5.1.56
D. 2.3.1.312
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

> The supplied sequence exactly matches the UniProt sequence annotated as N-acetylneuraminate synthase, EC 2.5.1.56. The annotation links this EC and its catalytic reaction to PubMed evidence coded ECO:0000269, supporting choice C for this protein.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence identifies a protein to be functionally characterized, but the input gives no substrate, reaction, or other context that establishes which specific catalytic activity applies. General sequence reasoning alone does not reliably distinguish these exact EC assignments.


**Missing item-specific fact**

> The protein-specific assignment of this sequence to N-acetylneuraminate synthase and its experimentally supported reaction, corresponding to EC 2.5.1.56.


**Reason**

> Choosing the supported EC requires an item-specific functional annotation or experimental fact absent from the question. Recognizing the sequence or recalling its database entry would be lookup or memorization, not reasoning from the supplied evidence.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The sequence-matched annotation supports EC 2.5.1.56; the supplied evidence does not support another listed option.


### Important caveats

- The supporting UniProt annotation cites experimental evidence, but the primary paper was not independently reviewed here.
- The reviewer-only accession and annotation were not included in the evaluated model input.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence identifies a protein to be functionally characterized, but the input gives no substrate, reaction, or other context that establishes which specific catalytic activity applies. General sequence reasoning alone does not reliably distinguish these exact EC assignments.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific assignment of this sequence to N-acetylneuraminate synthase and its experimentally supported reaction, corresponding to EC 2.5.1.56.",
    "reason": "Choosing the supported EC requires an item-specific functional annotation or experimental fact absent from the question. Recognizing the sequence or recalling its database entry would be lookup or memorization, not reasoning from the supplied evidence."
  },
  "case_id": "EC_number_0084",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the UniProt sequence annotated as N-acetylneuraminate synthase, EC 2.5.1.56. The annotation links this EC and its catalytic reaction to PubMed evidence coded ECO:0000269, supporting choice C for this protein."
  },
  "important_caveats": [
    "The supporting UniProt annotation cites experimental evidence, but the primary paper was not independently reviewed here.",
    "The reviewer-only accession and annotation were not included in the evaluated model input."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence-matched annotation supports EC 2.5.1.56; the supplied evidence does not support another listed option."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0084",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the UniProt sequence annotated as N-acetylneuraminate synthase, EC 2.5.1.56. The annotation links this EC and its catalytic reaction to PubMed evidence coded ECO:0000269, supporting choice C for this protein.",
    "evidence_ids": ["C1", "C4", "C5", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence identifies a protein to be functionally characterized, but the input gives no substrate, reaction, or other context that establishes which specific catalytic activity applies. General sequence reasoning alone does not reliably distinguish these exact EC assignments.",
    "missing_item_specific_fact": "The protein-specific assignment of this sequence to N-acetylneuraminate synthase and its experimentally supported reaction, corresponding to EC 2.5.1.56.",
    "reason": "Choosing the supported EC requires an item-specific functional annotation or experimental fact absent from the question. Recognizing the sequence or recalling its database entry would be lookup or memorization, not reasoning from the supplied evidence."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence-matched annotation supports EC 2.5.1.56; the supplied evidence does not support another listed option."
  },
  "important_caveats": [
    "The supporting UniProt annotation cites experimental evidence, but the primary paper was not independently reviewed here.",
    "The reviewer-only accession and annotation were not included in the evaluated model input."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The supplied sequence (346 aa) matches UniProt entry P0DY06 (NEUAS_CAMJ8) exactly (SHA-256 confirmed). The entry is annotated with EC 2.5.1.56 (N-acetylneuraminate synthase) supported by experimental evidence (ECO:0000269, PubMed:38382015, Ghosh & Raushel, Biochemistry 2024). The catalytic reaction (N-acetyl-D-mannosamine + PEP + H2O → N-acetylneuraminate + phosphate) is experimentally confirmed. The historical UniSave record (entry version 2, first released 2026-01) also carries this annotation.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> Eliminating B (2.7.11.24, a MAPKKKK kinase) is partially feasible by noting the absence of canonical kinase motifs (P-loop, HRD, DFG). Eliminating D (2.3.1.312, an acyltransferase) is weakly supported by the absence of HAT/acyltransferase signatures. However, distinguishing C (2.5.1.56, N-acetylneuraminate synthase) from A (2.5.1.76) — both within the same EC subclass 2.5.1 (glycosyltransferases) — requires knowing the precise substrate and product of the reaction. The sequence does not encode a self-evident catalytic signature that differentiates these two specific EC numbers without either exact sequence-to-database matching or detailed knowledge of the distinct active-site architectures of these two enzymes.


**Missing item-specific fact**

> The specific catalytic residues and substrate-binding pocket geometry that distinguish EC 2.5.1.56 from EC 2.5.1.76 are not inferable from the raw sequence without alignment to characterized family members. Moreover, this protein was only experimentally characterized in 2024 (PubMed 38382015) and first annotated in UniProt in June 2025, so the EC assignment is a very recent item-specific fact not derivable from general biological reasoning about the sequence.


**Reason**

> The question requires selecting among four EC numbers, two of which (2.5.1.56 and 2.5.1.76) fall in the same EC sub-subclass. No general biological argument from the raw 346-aa sequence alone distinguishes the exact glycosyltransferase reaction catalyzed (sialic acid biosynthesis vs. whatever 2.5.1.76 catalyzes). The correct answer depends on recognizing this specific protein or knowing its experimentally determined activity, which is a database/experimental fact rather than a reasoning conclusion.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The experimental evidence (ECO:0000269) unambiguously assigns EC 2.5.1.56 to this sequence. While a model might struggle to distinguish A from C by reasoning, the ground truth is clearly C. No alternative option is supported by the evidence.


### Important caveats

- The UniProt annotation for this protein was first published on 2025-06-18, based on a 2024 paper (PubMed 38382015). This is a very recent experimental characterization, making the EC assignment highly dependent on post-2024 database knowledge.
- The identity origin (accession P0DY06) was inferred mechanically from dataset metadata and was absent from the evaluated model input; the model sees only the raw sequence.
- EC 2.5.1.76 is in the same EC sub-subclass (2.5.1) as the correct answer, making it a non-trivial distractor that cannot be eliminated by broad subclass reasoning.
- The evidence code ECO:0000269 (direct assay) confirms this is an experimentally determined EC number, not a computational or similarity-based annotation.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Eliminating B (2.7.11.24, a MAPKKKK kinase) is partially feasible by noting the absence of canonical kinase motifs (P-loop, HRD, DFG). Eliminating D (2.3.1.312, an acyltransferase) is weakly supported by the absence of HAT/acyltransferase signatures. However, distinguishing C (2.5.1.56, N-acetylneuraminate synthase) from A (2.5.1.76) — both within the same EC subclass 2.5.1 (glycosyltransferases) — requires knowing the precise substrate and product of the reaction. The sequence does not encode a self-evident catalytic signature that differentiates these two specific EC numbers without either exact sequence-to-database matching or detailed knowledge of the distinct active-site architectures of these two enzymes.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific catalytic residues and substrate-binding pocket geometry that distinguish EC 2.5.1.56 from EC 2.5.1.76 are not inferable from the raw sequence without alignment to characterized family members. Moreover, this protein was only experimentally characterized in 2024 (PubMed 38382015) and first annotated in UniProt in June 2025, so the EC assignment is a very recent item-specific fact not derivable from general biological reasoning about the sequence.",
    "reason": "The question requires selecting among four EC numbers, two of which (2.5.1.56 and 2.5.1.76) fall in the same EC sub-subclass. No general biological argument from the raw 346-aa sequence alone distinguishes the exact glycosyltransferase reaction catalyzed (sialic acid biosynthesis vs. whatever 2.5.1.76 catalyzes). The correct answer depends on recognizing this specific protein or knowing its experimentally determined activity, which is a database/experimental fact rather than a reasoning conclusion."
  },
  "case_id": "EC_number_0084",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H1",
      "H2",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence (346 aa) matches UniProt entry P0DY06 (NEUAS_CAMJ8) exactly (SHA-256 confirmed). The entry is annotated with EC 2.5.1.56 (N-acetylneuraminate synthase) supported by experimental evidence (ECO:0000269, PubMed:38382015, Ghosh & Raushel, Biochemistry 2024). The catalytic reaction (N-acetyl-D-mannosamine + PEP + H2O → N-acetylneuraminate + phosphate) is experimentally confirmed. The historical UniSave record (entry version 2, first released 2026-01) also carries this annotation."
  },
  "important_caveats": [
    "The UniProt annotation for this protein was first published on 2025-06-18, based on a 2024 paper (PubMed 38382015). This is a very recent experimental characterization, making the EC assignment highly dependent on post-2024 database knowledge.",
    "The identity origin (accession P0DY06) was inferred mechanically from dataset metadata and was absent from the evaluated model input; the model sees only the raw sequence.",
    "EC 2.5.1.76 is in the same EC sub-subclass (2.5.1) as the correct answer, making it a non-trivial distractor that cannot be eliminated by broad subclass reasoning.",
    "The evidence code ECO:0000269 (direct assay) confirms this is an experimentally determined EC number, not a computational or similarity-based annotation."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The experimental evidence (ECO:0000269) unambiguously assigns EC 2.5.1.56 to this sequence. While a model might struggle to distinguish A from C by reasoning, the ground truth is clearly C. No alternative option is supported by the evidence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0084",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence (346 aa) matches UniProt entry P0DY06 (NEUAS_CAMJ8) exactly (SHA-256 confirmed). The entry is annotated with EC 2.5.1.56 (N-acetylneuraminate synthase) supported by experimental evidence (ECO:0000269, PubMed:38382015, Ghosh & Raushel, Biochemistry 2024). The catalytic reaction (N-acetyl-D-mannosamine + PEP + H2O → N-acetylneuraminate + phosphate) is experimentally confirmed. The historical UniSave record (entry version 2, first released 2026-01) also carries this annotation.",
    "evidence_ids": ["C4", "C5", "C6", "H1", "H2", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "Eliminating B (2.7.11.24, a MAPKKKK kinase) is partially feasible by noting the absence of canonical kinase motifs (P-loop, HRD, DFG). Eliminating D (2.3.1.312, an acyltransferase) is weakly supported by the absence of HAT/acyltransferase signatures. However, distinguishing C (2.5.1.56, N-acetylneuraminate synthase) from A (2.5.1.76) — both within the same EC subclass 2.5.1 (glycosyltransferases) — requires knowing the precise substrate and product of the reaction. The sequence does not encode a self-evident catalytic signature that differentiates these two specific EC numbers without either exact sequence-to-database matching or detailed knowledge of the distinct active-site architectures of these two enzymes.",
    "missing_item_specific_fact": "The specific catalytic residues and substrate-binding pocket geometry that distinguish EC 2.5.1.56 from EC 2.5.1.76 are not inferable from the raw sequence without alignment to characterized family members. Moreover, this protein was only experimentally characterized in 2024 (PubMed 38382015) and first annotated in UniProt in June 2025, so the EC assignment is a very recent item-specific fact not derivable from general biological reasoning about the sequence.",
    "reason": "The question requires selecting among four EC numbers, two of which (2.5.1.56 and 2.5.1.76) fall in the same EC sub-subclass. No general biological argument from the raw 346-aa sequence alone distinguishes the exact glycosyltransferase reaction catalyzed (sialic acid biosynthesis vs. whatever 2.5.1.76 catalyzes). The correct answer depends on recognizing this specific protein or knowing its experimentally determined activity, which is a database/experimental fact rather than a reasoning conclusion."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The experimental evidence (ECO:0000269) unambiguously assigns EC 2.5.1.56 to this sequence. While a model might struggle to distinguish A from C by reasoning, the ground truth is clearly C. No alternative option is supported by the evidence."
  },
  "important_caveats": [
    "The UniProt annotation for this protein was first published on 2025-06-18, based on a 2024 paper (PubMed 38382015). This is a very recent experimental characterization, making the EC assignment highly dependent on post-2024 database knowledge.",
    "The identity origin (accession P0DY06) was inferred mechanically from dataset metadata and was absent from the evaluated model input; the model sees only the raw sequence.",
    "EC 2.5.1.76 is in the same EC sub-subclass (2.5.1) as the correct answer, making it a non-trivial distractor that cannot be eliminated by broad subclass reasoning.",
    "The evidence code ECO:0000269 (direct assay) confirms this is an experimentally determined EC number, not a computational or similarity-based annotation."
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

**Accession:** `P0DY06` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 2. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DY06.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:03.200320+00:00.  

```json
"P0DY06"
```

Source SHA-256: `360a6e23ffa22a96d2f530ce41b08596efad1a8a83e5e9a083cacacc7581d59a`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DY06.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:03.200320+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"38382015","source":"PubMed"}],"value":"2.5.1.56"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"38382015","source":"PubMed"}],"value":"N-acetylneuraminate synthase"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"38382015","source":"PubMed"}],"value":"Neu5Ac synthase"}]}}
```

Source SHA-256: `360a6e23ffa22a96d2f530ce41b08596efad1a8a83e5e9a083cacacc7581d59a`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DY06.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:03.200320+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000269","id":"38382015","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:19274"}}],"reaction":{"ecNumber":"2.5.1.56","evidences":[{"evidenceCode":"ECO:0000269","id":"38382015","source":"PubMed"}],"name":"N-acetyl-D-mannosamine + phosphoenolpyruvate + H2O = N-acetylneuraminate + phosphate","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:19273"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:35418"},{"database":"ChEBI","id":"CHEBI:43474"},{"database":"ChEBI","id":"CHEBI:58702"},{"database":"ChEBI","id":"CHEBI:63153"}]}}
```

Source SHA-256: `360a6e23ffa22a96d2f530ce41b08596efad1a8a83e5e9a083cacacc7581d59a`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DY06.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:03.200320+00:00.  

```json
{"citation":{"authors":["Ghosh M.K.","Raushel F.M."],"citationCrossReferences":[{"database":"PubMed","id":"38382015"},{"database":"DOI","id":"10.1021/acs.biochem.3c00664"}],"citationType":"journal article","firstPage":"688","id":"38382015","journal":"Biochemistry","lastPage":"698","publicationDate":"2024","title":"Biosynthesis of UDP-alpha-N-Acetyl-d-mannosaminuronic Acid and CMP-beta-N-Acetyl-d-neuraminic Acid for the Capsular Polysaccharides of Campylobacter jejuni.","volume":"63"},"referenceComments":[{"type":"STRAIN","value":"81116 / NCTC 11828"}],"referenceNumber":2,"referencePositions":["FUNCTION","CATALYTIC ACTIVITY","BIOPHYSICOCHEMICAL PROPERTIES","PATHWAY"]}
```

Source SHA-256: `360a6e23ffa22a96d2f530ce41b08596efad1a8a83e5e9a083cacacc7581d59a`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DY06?format=txt&versions=2)  
**Locator:** `lines 1-15`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 2 / 1.  
**Retrieved:** 2026-11-02T04:30:07.414593+00:00.  

```text
ID   NEUAS_CAMJ8             Reviewed;         346 AA.
AC   P0DY06;
DT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.
DT   18-JUN-2025, sequence version 1.
DT   28-JAN-2026, entry version 2.
DE   RecName: Full=N-acetylneuraminate synthase {ECO:0000303|PubMed:38382015};
DE            Short=Neu5Ac synthase {ECO:0000303|PubMed:38382015};
DE            EC=2.5.1.56 {ECO:0000269|PubMed:38382015};
GN   Name=HS6.11 {ECO:0000303|PubMed:38382015};
GN   OrderedLocusNames=C8J_1339 {ECO:0000312|EMBL:ABV52937.1};
OS   Campylobacter jejuni subsp. jejuni serotype O:6 (strain 81116 / NCTC
OS   11828).
OC   Bacteria; Pseudomonadati; Campylobacterota; Epsilonproteobacteria;
OC   Campylobacterales; Campylobacteraceae; Campylobacter.
OX   NCBI_TaxID=407148;
```

Source SHA-256: `7e4ab42f0bda2ecc304cdd042f2bc5a8d831d80e65982976501788f9a05ab6b0`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DY06?format=txt&versions=2)  
**Locator:** `lines 6-8`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 2 / 1.  
**Retrieved:** 2026-11-02T04:30:07.414593+00:00.  

```text
DE   RecName: Full=N-acetylneuraminate synthase {ECO:0000303|PubMed:38382015};
DE            Short=Neu5Ac synthase {ECO:0000303|PubMed:38382015};
DE            EC=2.5.1.56 {ECO:0000269|PubMed:38382015};
```

Source SHA-256: `7e4ab42f0bda2ecc304cdd042f2bc5a8d831d80e65982976501788f9a05ab6b0`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DY06?format=txt&versions=2)  
**Locator:** `lines 25-33`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 2 / 1.  
**Retrieved:** 2026-11-02T04:30:07.414593+00:00.  

```text
RN   [2]
RP   FUNCTION, CATALYTIC ACTIVITY, BIOPHYSICOCHEMICAL PROPERTIES, AND PATHWAY.
RC   STRAIN=81116 / NCTC 11828;
RX   PubMed=38382015; DOI=10.1021/acs.biochem.3c00664;
RA   Ghosh M.K., Raushel F.M.;
RT   "Biosynthesis of UDP-alpha-N-Acetyl-d-mannosaminuronic Acid and CMP-beta-N-
RT   Acetyl-d-neuraminic Acid for the Capsular Polysaccharides of Campylobacter
RT   jejuni.";
RL   Biochemistry 63:688-698(2024).
```

Source SHA-256: `7e4ab42f0bda2ecc304cdd042f2bc5a8d831d80e65982976501788f9a05ab6b0`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DY06?format=txt&versions=2)  
**Locator:** `lines 39-46`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 2 / 1.  
**Retrieved:** 2026-11-02T04:30:07.414593+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=N-acetyl-D-mannosamine + phosphoenolpyruvate + H2O = N-
CC         acetylneuraminate + phosphate; Xref=Rhea:RHEA:19273,
CC         ChEBI:CHEBI:15377, ChEBI:CHEBI:35418, ChEBI:CHEBI:43474,
CC         ChEBI:CHEBI:58702, ChEBI:CHEBI:63153; EC=2.5.1.56;
CC         Evidence={ECO:0000269|PubMed:38382015};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:19274;
CC         Evidence={ECO:0000269|PubMed:38382015};
```

Source SHA-256: `7e4ab42f0bda2ecc304cdd042f2bc5a8d831d80e65982976501788f9a05ab6b0`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 84. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
