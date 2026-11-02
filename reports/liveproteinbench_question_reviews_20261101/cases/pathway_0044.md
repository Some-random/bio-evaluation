# pathway_0044

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `pathway`  
**Author expected answer:** **D** — Carotenoid biosynthesis

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MTNELSNAAGASQQGPAASSFSADTPPRTTAGGDVLVLLLIDVAPAARLWGYGRFVAGTTPALGEPGARFAKQLGTGYEGGFGLRPSATRQGLFVLFEDEAAADAFIGRSELVQTYRRNARELCIVKARPYSARGSWDGQKLRVGSPAPVDGPVAALTRASIRPSQAHRFWPNAGPSQDSLERAAGCRLAVGLGEAPFLRQATFSVWDSVAAMDAYARTGAHQRAIVASRDFFSESMFVRFVPLSIEGVWKGRRYG

[Multiple Choices]
A. Cell wall degradation
B. Carbohydrate degradation
C. Alkaloid biosynthesis. .
D. Carotenoid biosynthesis
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Protein Pathway Prediction, which is to predict the primary metabolic or signaling pathway in which a given protein functions. Biological pathways are series of chemical reactions occurring within a cell that are essential for life. Based on the protein's amino acid sequence, you should identify the most relevant pathway from the given options.. The inputs provided by the user for this task include:

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

> The supplied sequence exactly matches the 256-aa UniProt entry annotated as spheroidene monooxygenase (CrtA), with pathway annotations for carotenoid biosynthesis, including spheroidene and spirilloxanthin biosynthesis. The annotation cites published studies, although the pathway statements themselves carry ECO:0000305 evidence codes rather than being direct measurements in the excerpt.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H5](#evidence-h5), [H6](#evidence-h6).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The choices provide broad pathway categories, but the sequence alone does not offer a clear, distinctive basis to identify this protein's carotenoid-pathway role over the alternatives.


**Missing item-specific fact**

> The protein-specific identification as CrtA, a spheroidene monooxygenase/acyclic carotenoid 2-ketolase, and its carotenoid biosynthesis annotation.


**Reason**

> The key is supported by sequence-matched database and literature-linked annotations, but those protein-specific functional facts are not supplied in the question. Inferring them would require an external annotation, experimental knowledge, or prior recognition of this exact protein.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The cited pathway annotations both fall under the listed broad category of carotenoid biosynthesis, so D is the uniquely matching option.


### Important caveats

- Reviewer-only accession and annotation evidence were not available to the evaluated model.
- The current and historical records match the supplied sequence, but the author's exact source snapshot is unknown.
- The pathway annotations cite literature, but the excerpts do not independently establish the underlying experimental results.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The choices provide broad pathway categories, but the sequence alone does not offer a clear, distinctive basis to identify this protein's carotenoid-pathway role over the alternatives.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific identification as CrtA, a spheroidene monooxygenase/acyclic carotenoid 2-ketolase, and its carotenoid biosynthesis annotation.",
    "reason": "The key is supported by sequence-matched database and literature-linked annotations, but those protein-specific functional facts are not supplied in the question. Inferring them would require an external annotation, experimental knowledge, or prior recognition of this exact protein."
  },
  "case_id": "pathway_0044",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "H5",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the 256-aa UniProt entry annotated as spheroidene monooxygenase (CrtA), with pathway annotations for carotenoid biosynthesis, including spheroidene and spirilloxanthin biosynthesis. The annotation cites published studies, although the pathway statements themselves carry ECO:0000305 evidence codes rather than being direct measurements in the excerpt."
  },
  "important_caveats": [
    "Reviewer-only accession and annotation evidence were not available to the evaluated model.",
    "The current and historical records match the supplied sequence, but the author's exact source snapshot is unknown.",
    "The pathway annotations cite literature, but the excerpts do not independently establish the underlying experimental results."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The cited pathway annotations both fall under the listed broad category of carotenoid biosynthesis, so D is the uniquely matching option."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0044",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the 256-aa UniProt entry annotated as spheroidene monooxygenase (CrtA), with pathway annotations for carotenoid biosynthesis, including spheroidene and spirilloxanthin biosynthesis. The annotation cites published studies, although the pathway statements themselves carry ECO:0000305 evidence codes rather than being direct measurements in the excerpt.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H5", "H6"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The choices provide broad pathway categories, but the sequence alone does not offer a clear, distinctive basis to identify this protein's carotenoid-pathway role over the alternatives.",
    "missing_item_specific_fact": "The protein-specific identification as CrtA, a spheroidene monooxygenase/acyclic carotenoid 2-ketolase, and its carotenoid biosynthesis annotation.",
    "reason": "The key is supported by sequence-matched database and literature-linked annotations, but those protein-specific functional facts are not supplied in the question. Inferring them would require an external annotation, experimental knowledge, or prior recognition of this exact protein."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The cited pathway annotations both fall under the listed broad category of carotenoid biosynthesis, so D is the uniquely matching option."
  },
  "important_caveats": [
    "Reviewer-only accession and annotation evidence were not available to the evaluated model.",
    "The current and historical records match the supplied sequence, but the author's exact source snapshot is unknown.",
    "The pathway annotations cite literature, but the excerpts do not independently establish the underlying experimental results."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry Q83YH3 (CRTA_RUBGE) is annotated as Spheroidene monooxygenase (EC 1.14.15.9), also called Acyclic carotenoid 2-ketolase. The pathway comment explicitly states 'Carotenoid biosynthesis; spheroidene biosynthesis' and 'Carotenoid biosynthesis; spirilloxanthin biosynthesis,' supported by experimental evidence (ECO:0000305 from PubMed 12664193 and 19136077, including catalytic activity assays). The sequence matches exactly (256 aa, SHA-256 identical). The expected answer D is directly and experimentally supported.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [H1](#evidence-h1), [H5](#evidence-h5), [H6](#evidence-h6).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> A weak elimination argument exists: the 256-aa sequence lacks glycosyl hydrolase catalytic motifs (ruling out A and B) and lacks P450 heme-binding motifs or typical alkaloid-pathway enzyme domains (ruling out C). The hydrophobic N-terminal region (VLVLLLIDVAPAARL) suggests membrane association, which is broadly consistent with enzymes acting on hydrophobic carotenoid substrates. However, this does not positively identify carotenoid biosynthesis over other membrane-associated metabolic processes.


**Missing item-specific fact**

> Positive identification requires knowing that this specific 256-aa membrane-associated monooxygenase is a spheroidene monooxygenase (CrtA) in the carotenoid biosynthesis pathway. The sequence lacks a highly recognizable conserved domain (e.g., a canonical CCD, lycopene cyclase, or phytoene synthase motif) that would allow confident pathway assignment from sequence alone. The organism (Rubrivivax gelatinosus, a purple bacterium) is not provided, and knowledge of its carotenoid metabolism would be needed.


**Reason**

> While elimination of A, B, and C is partially possible through absence of expected catalytic domains, the positive assignment to carotenoid biosynthesis (D) over other unlisted membrane-associated pathways depends on recognizing this specific protein or knowing its function. The sequence does not contain a sufficiently distinctive conserved motif for confident pathway assignment without protein-specific knowledge.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the four given options, D is the only one consistent with the protein's annotation. A and B require glycosyl hydrolase/lyase domains absent from the sequence; C requires P450 or other alkaloid-specific enzyme motifs also absent. No other option is defensible given the four choices provided.


### Important caveats

- The UniProt annotation is supported by experimental evidence (catalytic activity assays, disruption phenotypes) rather than purely computational inference.
- The organism identity (Rubrivivax gelatinosus, a purple bacterium known for carotenoid metabolism) is not provided to the evaluated model, removing a potentially helpful contextual clue.
- The protein entry was first publicly released in 2025-02-05; the author's source snapshot date is unknown, though the historical version (v41) was available by the 2026-05-07 cutoff.
- The elimination-based reasoning (absence of GH/P450 motifs) is suggestive but not airtight; alkaloid biosynthesis can involve non-P450 enzymes, and carbohydrate degradation can involve non-classical mechanisms.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "A weak elimination argument exists: the 256-aa sequence lacks glycosyl hydrolase catalytic motifs (ruling out A and B) and lacks P450 heme-binding motifs or typical alkaloid-pathway enzyme domains (ruling out C). The hydrophobic N-terminal region (VLVLLLIDVAPAARL) suggests membrane association, which is broadly consistent with enzymes acting on hydrophobic carotenoid substrates. However, this does not positively identify carotenoid biosynthesis over other membrane-associated metabolic processes.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "Positive identification requires knowing that this specific 256-aa membrane-associated monooxygenase is a spheroidene monooxygenase (CrtA) in the carotenoid biosynthesis pathway. The sequence lacks a highly recognizable conserved domain (e.g., a canonical CCD, lycopene cyclase, or phytoene synthase motif) that would allow confident pathway assignment from sequence alone. The organism (Rubrivivax gelatinosus, a purple bacterium) is not provided, and knowledge of its carotenoid metabolism would be needed.",
    "reason": "While elimination of A, B, and C is partially possible through absence of expected catalytic domains, the positive assignment to carotenoid biosynthesis (D) over other unlisted membrane-associated pathways depends on recognizing this specific protein or knowing its function. The sequence does not contain a sufficiently distinctive conserved motif for confident pathway assignment without protein-specific knowledge."
  },
  "case_id": "pathway_0044",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C7",
      "C8",
      "H1",
      "H5",
      "H6"
    ],
    "judgment": "supported",
    "reason": "UniProt entry Q83YH3 (CRTA_RUBGE) is annotated as Spheroidene monooxygenase (EC 1.14.15.9), also called Acyclic carotenoid 2-ketolase. The pathway comment explicitly states 'Carotenoid biosynthesis; spheroidene biosynthesis' and 'Carotenoid biosynthesis; spirilloxanthin biosynthesis,' supported by experimental evidence (ECO:0000305 from PubMed 12664193 and 19136077, including catalytic activity assays). The sequence matches exactly (256 aa, SHA-256 identical). The expected answer D is directly and experimentally supported."
  },
  "important_caveats": [
    "The UniProt annotation is supported by experimental evidence (catalytic activity assays, disruption phenotypes) rather than purely computational inference.",
    "The organism identity (Rubrivivax gelatinosus, a purple bacterium known for carotenoid metabolism) is not provided to the evaluated model, removing a potentially helpful contextual clue.",
    "The protein entry was first publicly released in 2025-02-05; the author's source snapshot date is unknown, though the historical version (v41) was available by the 2026-05-07 cutoff.",
    "The elimination-based reasoning (absence of GH/P450 motifs) is suggestive but not airtight; alkaloid biosynthesis can involve non-P450 enzymes, and carbohydrate degradation can involve non-classical mechanisms."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the four given options, D is the only one consistent with the protein's annotation. A and B require glycosyl hydrolase/lyase domains absent from the sequence; C requires P450 or other alkaloid-specific enzyme motifs also absent. No other option is defensible given the four choices provided."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0044",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry Q83YH3 (CRTA_RUBGE) is annotated as Spheroidene monooxygenase (EC 1.14.15.9), also called Acyclic carotenoid 2-ketolase. The pathway comment explicitly states 'Carotenoid biosynthesis; spheroidene biosynthesis' and 'Carotenoid biosynthesis; spirilloxanthin biosynthesis,' supported by experimental evidence (ECO:0000305 from PubMed 12664193 and 19136077, including catalytic activity assays). The sequence matches exactly (256 aa, SHA-256 identical). The expected answer D is directly and experimentally supported.",
    "evidence_ids": ["C4", "C5", "C6", "C7", "C8", "H1", "H5", "H6"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "A weak elimination argument exists: the 256-aa sequence lacks glycosyl hydrolase catalytic motifs (ruling out A and B) and lacks P450 heme-binding motifs or typical alkaloid-pathway enzyme domains (ruling out C). The hydrophobic N-terminal region (VLVLLLIDVAPAARL) suggests membrane association, which is broadly consistent with enzymes acting on hydrophobic carotenoid substrates. However, this does not positively identify carotenoid biosynthesis over other membrane-associated metabolic processes.",
    "missing_item_specific_fact": "Positive identification requires knowing that this specific 256-aa membrane-associated monooxygenase is a spheroidene monooxygenase (CrtA) in the carotenoid biosynthesis pathway. The sequence lacks a highly recognizable conserved domain (e.g., a canonical CCD, lycopene cyclase, or phytoene synthase motif) that would allow confident pathway assignment from sequence alone. The organism (Rubrivivax gelatinosus, a purple bacterium) is not provided, and knowledge of its carotenoid metabolism would be needed.",
    "reason": "While elimination of A, B, and C is partially possible through absence of expected catalytic domains, the positive assignment to carotenoid biosynthesis (D) over other unlisted membrane-associated pathways depends on recognizing this specific protein or knowing its function. The sequence does not contain a sufficiently distinctive conserved motif for confident pathway assignment without protein-specific knowledge."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the four given options, D is the only one consistent with the protein's annotation. A and B require glycosyl hydrolase/lyase domains absent from the sequence; C requires P450 or other alkaloid-specific enzyme motifs also absent. No other option is defensible given the four choices provided."
  },
  "important_caveats": [
    "The UniProt annotation is supported by experimental evidence (catalytic activity assays, disruption phenotypes) rather than purely computational inference.",
    "The organism identity (Rubrivivax gelatinosus, a purple bacterium known for carotenoid metabolism) is not provided to the evaluated model, removing a potentially helpful contextual clue.",
    "The protein entry was first publicly released in 2025-02-05; the author's source snapshot date is unknown, though the historical version (v41) was available by the 2026-05-07 cutoff.",
    "The elimination-based reasoning (absence of GH/P450 motifs) is suggestive but not airtight; alkaloid biosynthesis can involve non-P450 enzymes, and carbohydrate degradation can involve non-classical mechanisms."
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

**Accession:** `Q83YH3` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 41. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q83YH3.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:53.398958+00:00.  

```json
"Q83YH3"
```

Source SHA-256: `415b0c5c709a9871648380468badca26797ea86b5dcd24f2ca939a756b8bbaf9`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q83YH3.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:53.398958+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"19136077","source":"PubMed"}],"value":"Acyclic carotenoid 2-ketolase"}},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Spheroidene/spirilloxanthin monooxygenase"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"19136077","source":"PubMed"}],"value":"1.14.15.9"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"12664193","source":"PubMed"}],"value":"Spheroidene monooxygenase"}}}
```

Source SHA-256: `415b0c5c709a9871648380468badca26797ea86b5dcd24f2ca939a756b8bbaf9`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q83YH3.json)  
**Locator:** `/comments/15`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:53.398958+00:00.  

```json
{"commentType":"PATHWAY","texts":[{"evidences":[{"evidenceCode":"ECO:0000305","id":"12664193","source":"PubMed"},{"evidenceCode":"ECO:0000305","id":"19136077","source":"PubMed"}],"value":"Carotenoid biosynthesis; spheroidene biosynthesis"}]}
```

Source SHA-256: `415b0c5c709a9871648380468badca26797ea86b5dcd24f2ca939a756b8bbaf9`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q83YH3.json)  
**Locator:** `/comments/16`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:53.398958+00:00.  

```json
{"commentType":"PATHWAY","texts":[{"evidences":[{"evidenceCode":"ECO:0000305","id":"12664193","source":"PubMed"},{"evidenceCode":"ECO:0000305","id":"19136077","source":"PubMed"}],"value":"Carotenoid biosynthesis; spirilloxanthin biosynthesis"}]}
```

Source SHA-256: `415b0c5c709a9871648380468badca26797ea86b5dcd24f2ca939a756b8bbaf9`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q83YH3.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:53.398958+00:00.  

```json
{"citation":{"authors":["Pinta V.","Ouchane S.","Picaud M.","Takaichi S.","Astier C.","Reiss-Husson F."],"citationCrossReferences":[{"database":"PubMed","id":"12664193"},{"database":"DOI","id":"10.1007/s00203-003-0538-3"}],"citationType":"journal article","firstPage":"354","id":"12664193","journal":"Arch. Microbiol.","lastPage":"362","publicationDate":"2003","title":"Characterization of unusual hydroxy- and ketocarotenoids in Rubrivivax gelatinosus: involvement of enzyme CrtF or CrtA.","volume":"179"},"referenceComments":[{"type":"STRAIN","value":"S1"}],"referenceNumber":2,"referencePositions":["FUNCTION","DISRUPTION PHENOTYPE"]}
```

Source SHA-256: `415b0c5c709a9871648380468badca26797ea86b5dcd24f2ca939a756b8bbaf9`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q83YH3.json)  
**Locator:** `/references/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:53.398958+00:00.  

```json
{"citation":{"authors":["Gerjets T.","Steiger S.","Sandmann G."],"citationCrossReferences":[{"database":"PubMed","id":"19136077"},{"database":"DOI","id":"10.1016/j.bbalip.2008.12.006"}],"citationType":"journal article","firstPage":"125","id":"19136077","journal":"Biochim. Biophys. Acta","lastPage":"131","publicationDate":"2009","title":"Catalytic properties of the expressed acyclic carotenoid 2-ketolases from Rhodobacter capsulatus and Rubrivivax gelatinosus.","volume":"1791"},"referenceComments":[{"type":"STRAIN","value":"S1"}],"referenceNumber":3,"referencePositions":["FUNCTION","CATALYTIC ACTIVITY","BIOPHYSICOCHEMICAL PROPERTIES"]}
```

Source SHA-256: `415b0c5c709a9871648380468badca26797ea86b5dcd24f2ca939a756b8bbaf9`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q83YH3?format=txt&versions=41)  
**Locator:** `lines 1-15`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 41 / 1.  
**Retrieved:** 2026-11-02T04:31:55.957280+00:00.  

```text
ID   CRTA_RUBGE              Reviewed;         256 AA.
AC   Q83YH3;
DT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.
DT   01-JUN-2003, sequence version 1.
DT   28-JAN-2026, entry version 41.
DE   RecName: Full=Spheroidene monooxygenase {ECO:0000303|PubMed:12664193};
DE            EC=1.14.15.9 {ECO:0000269|PubMed:19136077};
DE   AltName: Full=Acyclic carotenoid 2-ketolase {ECO:0000303|PubMed:19136077};
DE   AltName: Full=Spheroidene/spirilloxanthin monooxygenase {ECO:0000305};
GN   Name=crtA {ECO:0000303|PubMed:8999844};
OS   Rubrivivax gelatinosus (Rhodocyclus gelatinosus) (Rhodopseudomonas
OS   gelatinosa).
OC   Bacteria; Pseudomonadati; Pseudomonadota; Betaproteobacteria;
OC   Burkholderiales; Sphaerotilaceae; Rubrivivax.
OX   NCBI_TaxID=28068;
```

Source SHA-256: `4cb02fc77dffc8afd3037d666dd2cb6ddcd919a72332edbea1fb5b05014e9bc4`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q83YH3?format=txt&versions=41)  
**Locator:** `lines 174-175`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 41 / 1.  
**Retrieved:** 2026-11-02T04:31:55.957280+00:00.  

```text
CC   -!- PATHWAY: Carotenoid biosynthesis; spheroidene biosynthesis.
CC       {ECO:0000305|PubMed:12664193, ECO:0000305|PubMed:19136077}.
```

Source SHA-256: `4cb02fc77dffc8afd3037d666dd2cb6ddcd919a72332edbea1fb5b05014e9bc4`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q83YH3?format=txt&versions=41)  
**Locator:** `lines 176-177`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 41 / 1.  
**Retrieved:** 2026-11-02T04:31:55.957280+00:00.  

```text
CC   -!- PATHWAY: Carotenoid biosynthesis; spirilloxanthin biosynthesis.
CC       {ECO:0000305|PubMed:12664193, ECO:0000305|PubMed:19136077}.
```

Source SHA-256: `4cb02fc77dffc8afd3037d666dd2cb6ddcd919a72332edbea1fb5b05014e9bc4`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 44. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
