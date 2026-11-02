# EC_number_0172

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `EC_number`  
**Author expected answer:** **A** — 3.2.1.55

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MRFSVFTAAIAAAFSACCATASPAVNYVNSLILQRADPHIVKHTDGWYYFTATVPEYDRIVLRRAQTIQGLQSAPETVIWRRKAFGVGSGQVWAPELHYIDGRWYIYVALGVSGQWRIRAFVLEGVGANPLTASWTEKGIIQTNWDTFSLDATTFVANGTRYLVWAQQDPSRNGENSSLFIAPLQNPWTIRGPAVAISHPDLSWERIGYKVNEGPAVIQRNGRIFLTYSASATDHNYCMGLLTARADANLMNPASWVKSQQPIFVSNAATNQWGPGHNQFTVSEDGLSDILVYHDRGYRDINGDPLNDPNRRTRVQKLYWRDDGTPDFGIPVPDGPTPVRLRVAANGASSNGAYVRFYTTTGSGNLTGTAALPDTQFKLVSPGLSGGDSVSLESTSNPGTYVRRVSGSTAVQFERGTALNTAALRASASFRRVPGLSDSGGAVSFESVESPGQYLRLDPNGRLSVASVAEGTQGRSTFYLE

[Multiple Choices]
A. 3.2.1.55
B. 3.2.1.8
C. 2.7.7.80
D. 2.1.1.27
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

> The exact sequence matches a UniProt entry annotated as EC 3.2.1.55, with catalytic activity linked to experimental evidence (ECO:0000269) and a cited biochemical-characterization paper. The matching archived entry predates the stated historical cutoff.

Citations as saved: [H1](#evidence-h1), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The secretory signal and enzyme-like sequence are consistent with a fungal carbohydrate-active hydrolase, making A or B more plausible than the transferase options, but they do not establish the substrate specificity needed to choose between the two hydrolase EC numbers.


**Missing item-specific fact**

> The experimentally characterized catalytic activity—hydrolysis of terminal non-reducing alpha-L-arabinofuranoside residues—is not supplied in the question.


**Reason**

> The key is supported by sequence-matched, experimentally evidenced annotation, but selecting the complete EC number from the input requires protein-specific functional information rather than broad sequence/context reasoning.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "B"
]
```

> From the supplied sequence alone, a secreted fungal glycoside hydrolase is plausible, but the input does not provide enough substrate-specific evidence to distinguish alpha-L-arabinofuranosidase from the other glycoside hydrolase choice.


### Important caveats

- The reviewer-only UniProt annotation and publication evidence were not supplied to the evaluated model.
- The cited experimental evidence is retained as an annotation with an evidence code; the primary paper was not independently reviewed here.
- The source sequence matches the benchmark sequence exactly, but the author's precise source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The secretory signal and enzyme-like sequence are consistent with a fungal carbohydrate-active hydrolase, making A or B more plausible than the transferase options, but they do not establish the substrate specificity needed to choose between the two hydrolase EC numbers.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The experimentally characterized catalytic activity—hydrolysis of terminal non-reducing alpha-L-arabinofuranoside residues—is not supplied in the question.",
    "reason": "The key is supported by sequence-matched, experimentally evidenced annotation, but selecting the complete EC number from the input requires protein-specific functional information rather than broad sequence/context reasoning."
  },
  "case_id": "EC_number_0172",
  "expected_answer_check": {
    "evidence_ids": [
      "H1",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry annotated as EC 3.2.1.55, with catalytic activity linked to experimental evidence (ECO:0000269) and a cited biochemical-characterization paper. The matching archived entry predates the stated historical cutoff."
  },
  "important_caveats": [
    "The reviewer-only UniProt annotation and publication evidence were not supplied to the evaluated model.",
    "The cited experimental evidence is retained as an annotation with an evidence code; the primary paper was not independently reviewed here.",
    "The source sequence matches the benchmark sequence exactly, but the author's precise source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "B"
    ],
    "reason": "From the supplied sequence alone, a secreted fungal glycoside hydrolase is plausible, but the input does not provide enough substrate-specific evidence to distinguish alpha-L-arabinofuranosidase from the other glycoside hydrolase choice."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0172",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry annotated as EC 3.2.1.55, with catalytic activity linked to experimental evidence (ECO:0000269) and a cited biochemical-characterization paper. The matching archived entry predates the stated historical cutoff.",
    "evidence_ids": ["H1", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The secretory signal and enzyme-like sequence are consistent with a fungal carbohydrate-active hydrolase, making A or B more plausible than the transferase options, but they do not establish the substrate specificity needed to choose between the two hydrolase EC numbers.",
    "missing_item_specific_fact": "The experimentally characterized catalytic activity—hydrolysis of terminal non-reducing alpha-L-arabinofuranoside residues—is not supplied in the question.",
    "reason": "The key is supported by sequence-matched, experimentally evidenced annotation, but selecting the complete EC number from the input requires protein-specific functional information rather than broad sequence/context reasoning."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "B"],
    "reason": "From the supplied sequence alone, a secreted fungal glycoside hydrolase is plausible, but the input does not provide enough substrate-specific evidence to distinguish alpha-L-arabinofuranosidase from the other glycoside hydrolase choice."
  },
  "important_caveats": [
    "The reviewer-only UniProt annotation and publication evidence were not supplied to the evaluated model.",
    "The cited experimental evidence is retained as an annotation with an evidence code; the primary paper was not independently reviewed here.",
    "The source sequence matches the benchmark sequence exactly, but the author's precise source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry A0A0F6NRE2 (sequence SHA256 matched exactly) annotates this protein as Alpha-L-arabinofuranosidase 43 with EC 3.2.1.55, backed by direct experimental evidence (ECO:0000269, PubMed:25432346) reporting biochemical characterization of a GH43 alpha-arabinofuranosidase from Humicola insolens Y1. The catalytic activity comment confirms hydrolysis of terminal non-reducing alpha-L-arabinofuranoside residues.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains the GSGQW motif repeated at least twice in close proximity ('GVSGQVW' and 'GVSGQW'), which is the hallmark signature of the five-bladed β-propeller architecture characteristic of GH43 family glycoside hydrolases. GH43 enzymes are predominantly alpha-L-arabinofuranosidases (EC 3.2.1.55), whereas xylanases (EC 3.2.1.8) belong to GH10 ((β/α)8 barrel) or GH11 (β-jelly roll) families with entirely different fold signatures. Options C (nucleotidyltransferase, EC 2.7.7.x) and D (methyltransferase, EC 2.1.1.x) are eliminated immediately by the signal peptide and overall composition indicating a secreted hydrolase. The GSGQW repeat pattern thus provides a concrete structural-sequence argument distinguishing A from B.


**Missing item-specific fact**

> None strictly required; however, recognizing the GSGQW repeat as GH43-specific requires specialized knowledge of CAZy family structural signatures rather than generic biology.


**Reason**

> The repeated GSGQW motif is an identifiable sequence-level structural signature of the GH43 five-bladed β-propeller fold. A model with knowledge of protein fold families can use this to assign GH43 (arabinofuranosidase) rather than GH10/GH11 (xylanase). The elimination of C and D by EC-class mismatch is straightforward. The discrimination between A and B rests on a recognizable family-specific motif present in the supplied sequence.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options C and D are in entirely different EC classes (transferases vs. hydrolases) and are trivially eliminated. Option B (xylanase, GH10/GH11) has a fundamentally different fold from the GSGQW-repeat pattern observed. Option A is the only choice consistent with the GH43 signature in the sequence.


### Important caveats

- The GSGQW motif recognition is specialized CAZy-family knowledge; a model without training on carbohydrate-active enzyme families may not exploit this signal, making the question harder in practice even though a biological argument exists.
- The UniProt annotation carries experimental evidence (ECO:0000269), strengthening confidence in the key.
- The sequence is a precursor (signal peptide present); the mature protein lacks the N-terminal ~20 residues, but this does not affect family assignment.
- The reviewer-only evidence confirms the key but was not available to the evaluated model; the reasoning argument relies solely on features visible in the supplied sequence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains the GSGQW motif repeated at least twice in close proximity ('GVSGQVW' and 'GVSGQW'), which is the hallmark signature of the five-bladed β-propeller architecture characteristic of GH43 family glycoside hydrolases. GH43 enzymes are predominantly alpha-L-arabinofuranosidases (EC 3.2.1.55), whereas xylanases (EC 3.2.1.8) belong to GH10 ((β/α)8 barrel) or GH11 (β-jelly roll) families with entirely different fold signatures. Options C (nucleotidyltransferase, EC 2.7.7.x) and D (methyltransferase, EC 2.1.1.x) are eliminated immediately by the signal peptide and overall composition indicating a secreted hydrolase. The GSGQW repeat pattern thus provides a concrete structural-sequence argument distinguishing A from B.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None strictly required; however, recognizing the GSGQW repeat as GH43-specific requires specialized knowledge of CAZy family structural signatures rather than generic biology.",
    "reason": "The repeated GSGQW motif is an identifiable sequence-level structural signature of the GH43 five-bladed β-propeller fold. A model with knowledge of protein fold families can use this to assign GH43 (arabinofuranosidase) rather than GH10/GH11 (xylanase). The elimination of C and D by EC-class mismatch is straightforward. The discrimination between A and B rests on a recognizable family-specific motif present in the supplied sequence."
  },
  "case_id": "EC_number_0172",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "H1",
      "H2",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "UniProt entry A0A0F6NRE2 (sequence SHA256 matched exactly) annotates this protein as Alpha-L-arabinofuranosidase 43 with EC 3.2.1.55, backed by direct experimental evidence (ECO:0000269, PubMed:25432346) reporting biochemical characterization of a GH43 alpha-arabinofuranosidase from Humicola insolens Y1. The catalytic activity comment confirms hydrolysis of terminal non-reducing alpha-L-arabinofuranoside residues."
  },
  "important_caveats": [
    "The GSGQW motif recognition is specialized CAZy-family knowledge; a model without training on carbohydrate-active enzyme families may not exploit this signal, making the question harder in practice even though a biological argument exists.",
    "The UniProt annotation carries experimental evidence (ECO:0000269), strengthening confidence in the key.",
    "The sequence is a precursor (signal peptide present); the mature protein lacks the N-terminal ~20 residues, but this does not affect family assignment.",
    "The reviewer-only evidence confirms the key but was not available to the evaluated model; the reasoning argument relies solely on features visible in the supplied sequence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options C and D are in entirely different EC classes (transferases vs. hydrolases) and are trivially eliminated. Option B (xylanase, GH10/GH11) has a fundamentally different fold from the GSGQW-repeat pattern observed. Option A is the only choice consistent with the GH43 signature in the sequence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0172",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry A0A0F6NRE2 (sequence SHA256 matched exactly) annotates this protein as Alpha-L-arabinofuranosidase 43 with EC 3.2.1.55, backed by direct experimental evidence (ECO:0000269, PubMed:25432346) reporting biochemical characterization of a GH43 alpha-arabinofuranosidase from Humicola insolens Y1. The catalytic activity comment confirms hydrolysis of terminal non-reducing alpha-L-arabinofuranoside residues.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H1", "H2", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains the GSGQW motif repeated at least twice in close proximity ('GVSGQVW' and 'GVSGQW'), which is the hallmark signature of the five-bladed β-propeller architecture characteristic of GH43 family glycoside hydrolases. GH43 enzymes are predominantly alpha-L-arabinofuranosidases (EC 3.2.1.55), whereas xylanases (EC 3.2.1.8) belong to GH10 ((β/α)8 barrel) or GH11 (β-jelly roll) families with entirely different fold signatures. Options C (nucleotidyltransferase, EC 2.7.7.x) and D (methyltransferase, EC 2.1.1.x) are eliminated immediately by the signal peptide and overall composition indicating a secreted hydrolase. The GSGQW repeat pattern thus provides a concrete structural-sequence argument distinguishing A from B.",
    "missing_item_specific_fact": "None strictly required; however, recognizing the GSGQW repeat as GH43-specific requires specialized knowledge of CAZy family structural signatures rather than generic biology.",
    "reason": "The repeated GSGQW motif is an identifiable sequence-level structural signature of the GH43 five-bladed β-propeller fold. A model with knowledge of protein fold families can use this to assign GH43 (arabinofuranosidase) rather than GH10/GH11 (xylanase). The elimination of C and D by EC-class mismatch is straightforward. The discrimination between A and B rests on a recognizable family-specific motif present in the supplied sequence."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options C and D are in entirely different EC classes (transferases vs. hydrolases) and are trivially eliminated. Option B (xylanase, GH10/GH11) has a fundamentally different fold from the GSGQW-repeat pattern observed. Option A is the only choice consistent with the GH43 signature in the sequence."
  },
  "important_caveats": [
    "The GSGQW motif recognition is specialized CAZy-family knowledge; a model without training on carbohydrate-active enzyme families may not exploit this signal, making the question harder in practice even though a biological argument exists.",
    "The UniProt annotation carries experimental evidence (ECO:0000269), strengthening confidence in the key.",
    "The sequence is a precursor (signal peptide present); the mature protein lacks the N-terminal ~20 residues, but this does not affect family assignment.",
    "The reviewer-only evidence confirms the key but was not available to the evaluated model; the reasoning argument relies solely on features visible in the supplied sequence."
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

**Accession:** `A0A0F6NRE2` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 16. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0F6NRE2.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:39.416033+00:00.  

```json
"A0A0F6NRE2"
```

Source SHA-256: `1e5d7a5da3b1ff99ca8b412999f2a1323097b0d9e9e57580eff71e52a00dd55d`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0F6NRE2.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:39.416033+00:00.  

```json
{"flag":"Precursor","recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"25432346","source":"PubMed"}],"value":"3.2.1.55"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"25432346","source":"PubMed"}],"value":"Alpha-L-arabinofuranosidase 43"}}}
```

Source SHA-256: `1e5d7a5da3b1ff99ca8b412999f2a1323097b0d9e9e57580eff71e52a00dd55d`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0F6NRE2.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:39.416033+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"3.2.1.55","evidences":[{"evidenceCode":"ECO:0000269","id":"25432346","source":"PubMed"}],"name":"Hydrolysis of terminal non-reducing alpha-L-arabinofuranoside residues in alpha-L-arabinosides."}}
```

Source SHA-256: `1e5d7a5da3b1ff99ca8b412999f2a1323097b0d9e9e57580eff71e52a00dd55d`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0F6NRE2.json)  
**Locator:** `/references/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:39.416033+00:00.  

```json
{"citation":{"authors":["Yang X.","Shi P.","Ma R.","Luo H.","Huang H.","Yang P.","Yao B."],"citationCrossReferences":[{"database":"PubMed","id":"25432346"},{"database":"DOI","id":"10.1007/s12010-014-1416-y"}],"citationType":"journal article","firstPage":"1960","id":"25432346","journal":"Appl. Biochem. Biotechnol.","lastPage":"1970","publicationDate":"2015","title":"A new GH43 alpha-arabinofuranosidase from Humicola insolens Y1: biochemical characterization and synergistic action with a xylanase on xylan degradation.","volume":"175"},"referenceComments":[{"type":"STRAIN","value":"Y1"}],"referenceNumber":1,"referencePositions":["NUCLEOTIDE SEQUENCE [MRNA]","FUNCTION","CATALYTIC ACTIVITY","BIOPHYSICOCHEMICAL PROPERTIES","SUBSTRATE SPECIFICITY","ACTIVITY REGULATION","BIOTECHNOLOGY"]}
```

Source SHA-256: `1e5d7a5da3b1ff99ca8b412999f2a1323097b0d9e9e57580eff71e52a00dd55d`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0F6NRE2?format=txt&versions=16)  
**Locator:** `lines 1-13`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 16 / 1.  
**Retrieved:** 2026-11-01T06:27:19.078830+00:00.  

```text
ID   ABF43_HUMIN             Reviewed;         481 AA.
AC   A0A0F6NRE2;
DT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.
DT   22-JUL-2015, sequence version 1.
DT   28-JAN-2026, entry version 16.
DE   RecName: Full=Alpha-L-arabinofuranosidase 43 {ECO:0000303|PubMed:25432346};
DE            EC=3.2.1.55 {ECO:0000269|PubMed:25432346};
DE   Flags: Precursor;
GN   Name=Abf43 {ECO:0000303|PubMed:25432346};
OS   Humicola insolens (Soft-rot fungus).
OC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Sordariomycetes;
OC   Sordariomycetidae; Sordariales; Chaetomiaceae; Mycothermus.
OX   NCBI_TaxID=85995;
```

Source SHA-256: `2af4853fef65af58c3afa6566598fc0146a0bf2f1579d5b2b0a183cc992d117c`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0F6NRE2?format=txt&versions=16)  
**Locator:** `lines 6-8`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 16 / 1.  
**Retrieved:** 2026-11-01T06:27:19.078830+00:00.  

```text
DE   RecName: Full=Alpha-L-arabinofuranosidase 43 {ECO:0000303|PubMed:25432346};
DE            EC=3.2.1.55 {ECO:0000269|PubMed:25432346};
DE   Flags: Precursor;
```

Source SHA-256: `2af4853fef65af58c3afa6566598fc0146a0bf2f1579d5b2b0a183cc992d117c`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0F6NRE2?format=txt&versions=16)  
**Locator:** `lines 14-24`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 16 / 1.  
**Retrieved:** 2026-11-01T06:27:19.078830+00:00.  

```text
RN   [1]
RP   NUCLEOTIDE SEQUENCE [MRNA], FUNCTION, CATALYTIC ACTIVITY,
RP   BIOPHYSICOCHEMICAL PROPERTIES, SUBSTRATE SPECIFICITY, ACTIVITY REGULATION,
RP   AND BIOTECHNOLOGY.
RC   STRAIN=Y1;
RX   PubMed=25432346; DOI=10.1007/s12010-014-1416-y;
RA   Yang X., Shi P., Ma R., Luo H., Huang H., Yang P., Yao B.;
RT   "A new GH43 alpha-arabinofuranosidase from Humicola insolens Y1:
RT   biochemical characterization and synergistic action with a xylanase on
RT   xylan degradation.";
RL   Appl. Biochem. Biotechnol. 175:1960-1970(2015).
```

Source SHA-256: `2af4853fef65af58c3afa6566598fc0146a0bf2f1579d5b2b0a183cc992d117c`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0F6NRE2?format=txt&versions=16)  
**Locator:** `lines 29-32`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 16 / 1.  
**Retrieved:** 2026-11-01T06:27:19.078830+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=Hydrolysis of terminal non-reducing alpha-L-arabinofuranoside
CC         residues in alpha-L-arabinosides.; EC=3.2.1.55;
CC         Evidence={ECO:0000269|PubMed:25432346};
```

Source SHA-256: `2af4853fef65af58c3afa6566598fc0146a0bf2f1579d5b2b0a183cc992d117c`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 172. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
