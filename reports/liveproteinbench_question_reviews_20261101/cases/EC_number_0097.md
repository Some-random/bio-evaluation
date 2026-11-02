# EC_number_0097

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `EC_number`  
**Author expected answer:** **A** — 1.16.1.10

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MTKIAEKSKQEYGDLLKEKDHLQDMEQLEMTIVSIQTPYPSIVRIQGKINTLQPELWQAPNLAIRLIVSNPPEGQPISRVYTVRSFNPINAQIEIDFVKHEDLSPAMEWLNSAQVGTKIGLIGPRPHFIPNFTAKKHVVMFADDTAVPALYSILKQWELGISADIFIESFEKDIASQLPELEHVKIHSFHKEHHTSQKGLLLKAAFALEHYENITIWAACERNEARALRQFFLEDQQLNKNDVRIAGYWRDGVSSSELDKLRAQHYQEHIQQGKTLNEYDDLDLAN

[Multiple Choices]
A. 1.16.1.10
B. 1.14.19.80
C. 4.1.1.129
D. 3.6.1.5
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

> The supplied sequence exactly matches the UniProt entry for ferric acinetobactin reductase, annotated EC 1.16.1.10. The entry links this assignment and its catalytic reactions to PubMed 34308084 with experimental-evidence code ECO:0000269.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H2](#evidence-h2), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence alone does not provide a sufficiently specific basis to identify the enzyme's siderophore substrate or assign this complete four-part EC number rather than the alternatives.


**Missing item-specific fact**

> The protein-specific functional assignment as ferric acinetobactin reductase, including its experimentally characterized reactions with Fe(II)-siderophore and NAD(P)+.


**Reason**

> The key is supported by sequence-matched, evidence-coded database annotation, but that annotation and its cited experimental characterization were not supplied to the evaluated model. General sequence-based reasoning does not distinguish the exact EC number.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The available sequence-matched annotation supports A; the alternatives describe different enzyme classifications, and no evidence here supports them for this protein.


### Important caveats

- The reviewer-only database evidence was absent from the original input and supports the key without making the question reasoning-supported.
- The UniProt entry cites a biochemical characterization paper, but that primary paper was not independently retrieved or validated here.
- The exact author source snapshot is unknown; the sequence matches both the current and checked historical UniProt records.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence alone does not provide a sufficiently specific basis to identify the enzyme's siderophore substrate or assign this complete four-part EC number rather than the alternatives.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific functional assignment as ferric acinetobactin reductase, including its experimentally characterized reactions with Fe(II)-siderophore and NAD(P)+.",
    "reason": "The key is supported by sequence-matched, evidence-coded database annotation, but that annotation and its cited experimental characterization were not supplied to the evaluated model. General sequence-based reasoning does not distinguish the exact EC number."
  },
  "case_id": "EC_number_0097",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "C7",
      "H2",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the UniProt entry for ferric acinetobactin reductase, annotated EC 1.16.1.10. The entry links this assignment and its catalytic reactions to PubMed 34308084 with experimental-evidence code ECO:0000269."
  },
  "important_caveats": [
    "The reviewer-only database evidence was absent from the original input and supports the key without making the question reasoning-supported.",
    "The UniProt entry cites a biochemical characterization paper, but that primary paper was not independently retrieved or validated here.",
    "The exact author source snapshot is unknown; the sequence matches both the current and checked historical UniProt records."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The available sequence-matched annotation supports A; the alternatives describe different enzyme classifications, and no evidence here supports them for this protein."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0097",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the UniProt entry for ferric acinetobactin reductase, annotated EC 1.16.1.10. The entry links this assignment and its catalytic reactions to PubMed 34308084 with experimental-evidence code ECO:0000269.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "C7", "H2", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence alone does not provide a sufficiently specific basis to identify the enzyme's siderophore substrate or assign this complete four-part EC number rather than the alternatives.",
    "missing_item_specific_fact": "The protein-specific functional assignment as ferric acinetobactin reductase, including its experimentally characterized reactions with Fe(II)-siderophore and NAD(P)+.",
    "reason": "The key is supported by sequence-matched, evidence-coded database annotation, but that annotation and its cited experimental characterization were not supplied to the evaluated model. General sequence-based reasoning does not distinguish the exact EC number."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The available sequence-matched annotation supports A; the alternatives describe different enzyme classifications, and no evidence here supports them for this protein."
  },
  "important_caveats": [
    "The reviewer-only database evidence was absent from the original input and supports the key without making the question reasoning-supported.",
    "The UniProt entry cites a biochemical characterization paper, but that primary paper was not independently retrieved or validated here.",
    "The exact author source snapshot is unknown; the sequence matches both the current and checked historical UniProt records."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence matches UniProt entry A0A1E3M8P2 (BAUF_ACIBA), annotated as Ferric acinetobactin reductase with EC=1.16.1.10. The annotation carries evidence code ECO:0000269 (direct assay) from PubMed:34308084, supported by X-ray crystallography (PDB 7LRN) in complex with FAD. The catalytic reaction (2 Fe(II)-siderophore + NAD(P)+ + H+ = 2 Fe(III)-siderophore + NAD(P)H) is experimentally verified. This is a direct experimental annotation, not merely computational inference.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> A model might partially narrow the class: the sequence lacks the cytochrome P450 heme-binding motif (FxxGxxxCxG), potentially ruling out EC 1.14.19.80; it lacks obvious decarboxylase or ATP-diphosphohydrolase motifs, potentially ruling out EC 4.1.1.129 and 3.6.1.5. However, identifying the specific 4-digit EC number 1.16.1.10 (ferric acinetobactin reductase) from a 286-aa sequence requires recognizing it as a flavin-dependent siderophore-interacting protein specific to acinetobactin in Acinetobacter baumannii — an item-specific annotation not derivable from general sequence reasoning.


**Missing item-specific fact**

> The specific identity of this protein as BauF (ferric acinetobactin reductase) and its assignment to the narrow EC 1.16.1.10 class (acting on Fe(II)-siderophore with NAD+/NADP+ as acceptor) requires database lookup or memorization of this particular protein's experimental characterization (PubMed 34308084, PDB 7LRN). No general sequence feature uniquely encodes 'ferric acinetobactin reductase' as opposed to other flavin-dependent reductases.


**Reason**

> While broad class discrimination (oxidoreductase vs. hydrolase vs. lyase) is partially feasible from sequence, the precise 4-digit EC assignment 1.16.1.10 depends on knowing this is specifically a siderophore-interacting protein acting on Fe(II)-acinetobactin. The sequence provides no unique signature that distinguishes EC 1.16.1.10 from other flavin-dependent oxidoreductases without external annotation lookup.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The distractors span different EC top-level classes (1, 3, 4), and B is a P450 with a well-known heme motif absent from this sequence. Given the experimental evidence, only A is correct. The question is not ambiguous in terms of the correct answer, though it is difficult to resolve by reasoning alone.


### Important caveats

- The UniProt annotation is based on direct experimental evidence (ECO:0000269, direct assay; X-ray crystallography PDB 7LRN), providing high confidence in the EC assignment.
- The sequence is 286 aa and matches the canonical UniProt entry exactly (sha256 confirmed).
- The EC number 1.16.1.10 is a very specific, recently characterized enzyme class (2021 publication), making memorization-based identification even less likely for a general model.
- The identity_origin of the accession was inferred mechanically from dataset metadata and was absent from the evaluated model input.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "A model might partially narrow the class: the sequence lacks the cytochrome P450 heme-binding motif (FxxGxxxCxG), potentially ruling out EC 1.14.19.80; it lacks obvious decarboxylase or ATP-diphosphohydrolase motifs, potentially ruling out EC 4.1.1.129 and 3.6.1.5. However, identifying the specific 4-digit EC number 1.16.1.10 (ferric acinetobactin reductase) from a 286-aa sequence requires recognizing it as a flavin-dependent siderophore-interacting protein specific to acinetobactin in Acinetobacter baumannii — an item-specific annotation not derivable from general sequence reasoning.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific identity of this protein as BauF (ferric acinetobactin reductase) and its assignment to the narrow EC 1.16.1.10 class (acting on Fe(II)-siderophore with NAD+/NADP+ as acceptor) requires database lookup or memorization of this particular protein's experimental characterization (PubMed 34308084, PDB 7LRN). No general sequence feature uniquely encodes 'ferric acinetobactin reductase' as opposed to other flavin-dependent reductases.",
    "reason": "While broad class discrimination (oxidoreductase vs. hydrolase vs. lyase) is partially feasible from sequence, the precise 4-digit EC assignment 1.16.1.10 depends on knowing this is specifically a siderophore-interacting protein acting on Fe(II)-acinetobactin. The sequence provides no unique signature that distinguishes EC 1.16.1.10 from other flavin-dependent oxidoreductases without external annotation lookup."
  },
  "case_id": "EC_number_0097",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C7",
      "H2",
      "H3",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The sequence matches UniProt entry A0A1E3M8P2 (BAUF_ACIBA), annotated as Ferric acinetobactin reductase with EC=1.16.1.10. The annotation carries evidence code ECO:0000269 (direct assay) from PubMed:34308084, supported by X-ray crystallography (PDB 7LRN) in complex with FAD. The catalytic reaction (2 Fe(II)-siderophore + NAD(P)+ + H+ = 2 Fe(III)-siderophore + NAD(P)H) is experimentally verified. This is a direct experimental annotation, not merely computational inference."
  },
  "important_caveats": [
    "The UniProt annotation is based on direct experimental evidence (ECO:0000269, direct assay; X-ray crystallography PDB 7LRN), providing high confidence in the EC assignment.",
    "The sequence is 286 aa and matches the canonical UniProt entry exactly (sha256 confirmed).",
    "The EC number 1.16.1.10 is a very specific, recently characterized enzyme class (2021 publication), making memorization-based identification even less likely for a general model.",
    "The identity_origin of the accession was inferred mechanically from dataset metadata and was absent from the evaluated model input."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The distractors span different EC top-level classes (1, 3, 4), and B is a P450 with a well-known heme motif absent from this sequence. Given the experimental evidence, only A is correct. The question is not ambiguous in terms of the correct answer, though it is difficult to resolve by reasoning alone."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0097",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches UniProt entry A0A1E3M8P2 (BAUF_ACIBA), annotated as Ferric acinetobactin reductase with EC=1.16.1.10. The annotation carries evidence code ECO:0000269 (direct assay) from PubMed:34308084, supported by X-ray crystallography (PDB 7LRN) in complex with FAD. The catalytic reaction (2 Fe(II)-siderophore + NAD(P)+ + H+ = 2 Fe(III)-siderophore + NAD(P)H) is experimentally verified. This is a direct experimental annotation, not merely computational inference.",
    "evidence_ids": ["C4", "C5", "C6", "C7", "H2", "H3", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "A model might partially narrow the class: the sequence lacks the cytochrome P450 heme-binding motif (FxxGxxxCxG), potentially ruling out EC 1.14.19.80; it lacks obvious decarboxylase or ATP-diphosphohydrolase motifs, potentially ruling out EC 4.1.1.129 and 3.6.1.5. However, identifying the specific 4-digit EC number 1.16.1.10 (ferric acinetobactin reductase) from a 286-aa sequence requires recognizing it as a flavin-dependent siderophore-interacting protein specific to acinetobactin in Acinetobacter baumannii — an item-specific annotation not derivable from general sequence reasoning.",
    "missing_item_specific_fact": "The specific identity of this protein as BauF (ferric acinetobactin reductase) and its assignment to the narrow EC 1.16.1.10 class (acting on Fe(II)-siderophore with NAD+/NADP+ as acceptor) requires database lookup or memorization of this particular protein's experimental characterization (PubMed 34308084, PDB 7LRN). No general sequence feature uniquely encodes 'ferric acinetobactin reductase' as opposed to other flavin-dependent reductases.",
    "reason": "While broad class discrimination (oxidoreductase vs. hydrolase vs. lyase) is partially feasible from sequence, the precise 4-digit EC assignment 1.16.1.10 depends on knowing this is specifically a siderophore-interacting protein acting on Fe(II)-acinetobactin. The sequence provides no unique signature that distinguishes EC 1.16.1.10 from other flavin-dependent oxidoreductases without external annotation lookup."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The distractors span different EC top-level classes (1, 3, 4), and B is a P450 with a well-known heme motif absent from this sequence. Given the experimental evidence, only A is correct. The question is not ambiguous in terms of the correct answer, though it is difficult to resolve by reasoning alone."
  },
  "important_caveats": [
    "The UniProt annotation is based on direct experimental evidence (ECO:0000269, direct assay; X-ray crystallography PDB 7LRN), providing high confidence in the EC assignment.",
    "The sequence is 286 aa and matches the canonical UniProt entry exactly (sha256 confirmed).",
    "The EC number 1.16.1.10 is a very specific, recently characterized enzyme class (2021 publication), making memorization-based identification even less likely for a general model.",
    "The identity_origin of the accession was inferred mechanically from dataset metadata and was absent from the evaluated model input."
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

**Accession:** `A0A1E3M8P2` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 35. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A1E3M8P2.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:33.445950+00:00.  

```json
"A0A1E3M8P2"
```

Source SHA-256: `27262ada0697001eda3da1d3769c61657664eca5dc8977cc9c5dbaec21268418`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A1E3M8P2.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:33.445950+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"34308084","source":"PubMed"}],"value":"Flavin-dependent siderophore-interacting protein"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"34308084","source":"PubMed"}],"value":"Flavin-dependent SIP"}]}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"34308084","source":"PubMed"}],"value":"1.16.1.10"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Ferric acinetobactin reductase"}}}
```

Source SHA-256: `27262ada0697001eda3da1d3769c61657664eca5dc8977cc9c5dbaec21268418`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A1E3M8P2.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:33.445950+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"right-to-left","evidences":[{"evidenceCode":"ECO:0000269","id":"34308084","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:15063"}}],"reaction":{"ecNumber":"1.16.1.10","evidences":[{"evidenceCode":"ECO:0000269","id":"34308084","source":"PubMed"}],"name":"2 a Fe(II)-siderophore + NAD(+) + H(+) = 2 a Fe(III)-siderophore + NADH","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:15061"},{"database":"Rhea","id":"RHEA-COMP:11342"},{"database":"Rhea","id":"RHEA-COMP:11344"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:29033"},{"database":"ChEBI","id":"CHEBI:29034"},{"database":"ChEBI","id":"CHEBI:57540"},{"database":"ChEBI","id":"CHEBI:57945"}]}}
```

Source SHA-256: `27262ada0697001eda3da1d3769c61657664eca5dc8977cc9c5dbaec21268418`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A1E3M8P2.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:33.445950+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"right-to-left","evidences":[{"evidenceCode":"ECO:0000269","id":"34308084","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:28797"}}],"reaction":{"ecNumber":"1.16.1.10","evidences":[{"evidenceCode":"ECO:0000269","id":"34308084","source":"PubMed"}],"name":"2 a Fe(II)-siderophore + NADP(+) + H(+) = 2 a Fe(III)-siderophore + NADPH","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:28795"},{"database":"Rhea","id":"RHEA-COMP:11342"},{"database":"Rhea","id":"RHEA-COMP:11344"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:29033"},{"database":"ChEBI","id":"CHEBI:29034"},{"database":"ChEBI","id":"CHEBI:57783"},{"database":"ChEBI","id":"CHEBI:58349"}]}}
```

Source SHA-256: `27262ada0697001eda3da1d3769c61657664eca5dc8977cc9c5dbaec21268418`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A1E3M8P2.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:33.445950+00:00.  

```json
{"citation":{"authors":["Valentino H.","Korasick D.A.","Bohac T.J.","Shapiro J.A.","Wencewicz T.A.","Tanner J.J.","Sobrado P."],"citationCrossReferences":[{"database":"PubMed","id":"34308084"},{"database":"DOI","id":"10.1021/acsomega.1c03047"}],"citationType":"journal article","firstPage":"18537","id":"34308084","journal":"ACS Omega","lastPage":"18547","publicationDate":"2021","title":"Structural and Biochemical Characterization of the Flavin-Dependent Siderophore-Interacting Protein from Acinetobacter baumannii.","volume":"6"},"evidences":[{"evidenceCode":"ECO:0007744","id":"7LRN","source":"PDB"}],"referenceComments":[{"type":"STRAIN","value":"ATCC 17978 / DSM 105126 / CIP 53.77 / LMG 1025 / NCDC KC755 / 5377"}],"referenceNumber":2,"referencePositions":["X-RAY CRYSTALLOGRAPHY (2.85 ANGSTROMS) IN COMPLEX WITH FAD","FUNCTION","CATALYTIC ACTIVITY","COFACTOR"]}
```

Source SHA-256: `27262ada0697001eda3da1d3769c61657664eca5dc8977cc9c5dbaec21268418`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A1E3M8P2?format=txt&versions=35)  
**Locator:** `lines 6-9`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 35 / 1.  
**Retrieved:** 2026-11-02T04:24:37.007835+00:00.  

```text
DE   RecName: Full=Ferric acinetobactin reductase {ECO:0000305};
DE            EC=1.16.1.10 {ECO:0000269|PubMed:34308084};
DE   AltName: Full=Flavin-dependent siderophore-interacting protein {ECO:0000303|PubMed:34308084};
DE            Short=Flavin-dependent SIP {ECO:0000303|PubMed:34308084};
```

Source SHA-256: `21245d159df4b708ad492dd55bbbd986a27609a5d66677beffd60475a84e1746`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A1E3M8P2?format=txt&versions=35)  
**Locator:** `lines 22-31`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 35 / 1.  
**Retrieved:** 2026-11-02T04:24:37.007835+00:00.  

```text
RN   [2] {ECO:0007744|PDB:7LRN}
RP   X-RAY CRYSTALLOGRAPHY (2.85 ANGSTROMS) IN COMPLEX WITH FAD, FUNCTION,
RP   CATALYTIC ACTIVITY, AND COFACTOR.
RC   STRAIN=ATCC 17978 / DSM 105126 / CIP 53.77 / LMG 1025 / NCDC KC755 / 5377;
RX   PubMed=34308084; DOI=10.1021/acsomega.1c03047;
RA   Valentino H., Korasick D.A., Bohac T.J., Shapiro J.A., Wencewicz T.A.,
RA   Tanner J.J., Sobrado P.;
RT   "Structural and Biochemical Characterization of the Flavin-Dependent
RT   Siderophore-Interacting Protein from Acinetobacter baumannii.";
RL   ACS Omega 6:18537-18547(2021).
```

Source SHA-256: `21245d159df4b708ad492dd55bbbd986a27609a5d66677beffd60475a84e1746`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A1E3M8P2?format=txt&versions=35)  
**Locator:** `lines 43-50`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 35 / 1.  
**Retrieved:** 2026-11-02T04:24:37.007835+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=2 a Fe(II)-siderophore + NAD(+) + H(+) = 2 a Fe(III)-
CC         siderophore + NADH; Xref=Rhea:RHEA:15061, Rhea:RHEA-COMP:11342,
CC         Rhea:RHEA-COMP:11344, ChEBI:CHEBI:15378, ChEBI:CHEBI:29033,
CC         ChEBI:CHEBI:29034, ChEBI:CHEBI:57540, ChEBI:CHEBI:57945;
CC         EC=1.16.1.10; Evidence={ECO:0000269|PubMed:34308084};
CC       PhysiologicalDirection=right-to-left; Xref=Rhea:RHEA:15063;
CC         Evidence={ECO:0000269|PubMed:34308084};
```

Source SHA-256: `21245d159df4b708ad492dd55bbbd986a27609a5d66677beffd60475a84e1746`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A1E3M8P2?format=txt&versions=35)  
**Locator:** `lines 51-58`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 35 / 1.  
**Retrieved:** 2026-11-02T04:24:37.007835+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=2 a Fe(II)-siderophore + NADP(+) + H(+) = 2 a Fe(III)-
CC         siderophore + NADPH; Xref=Rhea:RHEA:28795, Rhea:RHEA-COMP:11342,
CC         Rhea:RHEA-COMP:11344, ChEBI:CHEBI:15378, ChEBI:CHEBI:29033,
CC         ChEBI:CHEBI:29034, ChEBI:CHEBI:57783, ChEBI:CHEBI:58349;
CC         EC=1.16.1.10; Evidence={ECO:0000269|PubMed:34308084};
CC       PhysiologicalDirection=right-to-left; Xref=Rhea:RHEA:28797;
CC         Evidence={ECO:0000269|PubMed:34308084};
```

Source SHA-256: `21245d159df4b708ad492dd55bbbd986a27609a5d66677beffd60475a84e1746`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 97. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
