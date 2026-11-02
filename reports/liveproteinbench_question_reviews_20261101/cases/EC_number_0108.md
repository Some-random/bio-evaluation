# EC_number_0108

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `EC_number`  
**Author expected answer:** **B** — 3.1.3.112

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MSSLLDIIYQLRQVPRWDGSFQFEKEDVSQHSFSVIAISHILCELKETLEGKKINKEKLLLYALYHDVTEVVSTHIISPVKKNSILKDPFNAFREQIKNSLFDNLPITLSDTLSTILNNNDLEIQEIVEHADHVDAYCKSCIEVHRGNKDFISIQRSLGDKLDNLTKEYPYLKEFQNLFLKDFPLENKNYRYLN

[Multiple Choices]
A. 3.1.3.2
B. 3.1.3.112
C. 1.3.1.36
D. 4.3.3.9
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

> The exact sequence matches the UniProt entry annotated as EC 3.1.3.112. The annotation reports the specific phosphatase reaction and cites experimental evidence; the historical record also carries this EC annotation.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H6](#evidence-h6).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> Sequence-level features may suggest a phosphohydrolase, helping distinguish phosphatase choices from the dehydrogenase and lyase options, but they do not establish the specific substrate reaction needed to choose between EC 3.1.3.2 and 3.1.3.112.


**Missing item-specific fact**

> The protein-specific catalytic activity: hydrolysis of 4'-phosphooxetanocin A to oxetanocin A and phosphate.


**Reason**

> The exact EC assignment depends on substrate specificity that is not supplied in the question and cannot be established merely from general sequence reasoning.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The cited annotation assigns this matched protein the specific activity corresponding to B. The sequence-only input does not provide enough information to infer that specificity, but this does not make another option correct for the protein.


### Important caveats

- The sequence match and cited experimental annotation support the key, but the primary papers were not independently reviewed here.
- The exact author data-source snapshot is unknown; the historical record checked is a sequence match from a record released by the stated cutoff.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Sequence-level features may suggest a phosphohydrolase, helping distinguish phosphatase choices from the dehydrogenase and lyase options, but they do not establish the specific substrate reaction needed to choose between EC 3.1.3.2 and 3.1.3.112.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific catalytic activity: hydrolysis of 4'-phosphooxetanocin A to oxetanocin A and phosphate.",
    "reason": "The exact EC assignment depends on substrate specificity that is not supplied in the question and cannot be established merely from general sequence reasoning."
  },
  "case_id": "EC_number_0108",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry annotated as EC 3.1.3.112. The annotation reports the specific phosphatase reaction and cites experimental evidence; the historical record also carries this EC annotation."
  },
  "important_caveats": [
    "The sequence match and cited experimental annotation support the key, but the primary papers were not independently reviewed here.",
    "The exact author data-source snapshot is unknown; the historical record checked is a sequence match from a record released by the stated cutoff."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The cited annotation assigns this matched protein the specific activity corresponding to B. The sequence-only input does not provide enough information to infer that specificity, but this does not make another option correct for the protein."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0108",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry annotated as EC 3.1.3.112. The annotation reports the specific phosphatase reaction and cites experimental evidence; the historical record also carries this EC annotation.",
    "evidence_ids": ["C4", "C5", "H2", "H6"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "Sequence-level features may suggest a phosphohydrolase, helping distinguish phosphatase choices from the dehydrogenase and lyase options, but they do not establish the specific substrate reaction needed to choose between EC 3.1.3.2 and 3.1.3.112.",
    "missing_item_specific_fact": "The protein-specific catalytic activity: hydrolysis of 4'-phosphooxetanocin A to oxetanocin A and phosphate.",
    "reason": "The exact EC assignment depends on substrate specificity that is not supplied in the question and cannot be established merely from general sequence reasoning."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The cited annotation assigns this matched protein the specific activity corresponding to B. The sequence-only input does not provide enough information to infer that specificity, but this does not make another option correct for the protein."
  },
  "important_caveats": [
    "The sequence match and cited experimental annotation support the key, but the primary papers were not independently reviewed here.",
    "The exact author data-source snapshot is unknown; the historical record checked is a sequence match from a record released by the stated cutoff."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence (194 aa) matches UniProt O24769 (OXSA_PRIMG, Priestia megaterium) exactly. The EC number 3.1.3.112 (4'-phosphooxetanocin A phosphatase) is annotated with experimental evidence codes ECO:0000269 from PubMed:27849620 (PNAS 2016, X-ray crystallography at 1.64 Å with multiple ligand complexes) and PubMed:28346939 (Nature 2017). The catalytic reaction (4'-phosphooxetanocin A + H2O = oxetanocin A + phosphate) is confirmed by Rhea (RHEA:81367/81368) and multiple PDB structures (5TK6–5TKA). The sequence contains characteristic HD-domain motifs (e.g., 'HDVTEVVST', 'HADHVDAY') consistent with the HD-domain phosphohydrolase family.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H2](#evidence-h2), [H5](#evidence-h5), [H6](#evidence-h6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 194-residue length immediately argues against EC 1.3.1.36 (dihydropyrimidine dehydrogenase, typically >1000 aa with FAD/FMN cofactor domains) and EC 4.3.3.9 (methylthioadenosine deaminase, also a substantially larger enzyme), eliminating C and D. The sequence contains recognizable HD-motif pairs (e.g., '…LYALYHDVTEVVST…' and '…IVEHADHVDAY…'), which are the signature of the HD-domain phosphohydrolase superfamily. Classic alkaline phosphatase (EC 3.1.3.2) belongs to a structurally distinct alpha/beta-sandwich fold with a binuclear Zn active site, is typically 400–500 aa, and does not carry HD motifs. Recognizing the HD domain plus the small size therefore disfavors A and points toward the HD-domain phosphohydrolase B (3.1.3.112).


**Missing item-specific fact**

> The specific substrate identity (4'-phosphooxetanocin A) and the exact 4th-digit EC assignment cannot be inferred from sequence alone; this requires knowledge of the oxetanocin biosynthetic pathway or a database lookup. However, among the four provided options, the family-level reasoning (HD-domain phosphohydrolase, small size) is sufficient to eliminate A, C, and D, leaving B as the only consistent choice.


**Reason**

> A model with general knowledge of enzyme family sizes, the HD-domain phosphohydrolase superfamily, and the structural/fold differences between HD-domain enzymes and alkaline phosphatase can construct a defensible elimination chain. The final 4th-digit specificity is lookup-dependent, but the question is answerable by reasoning given the constrained option set.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The small size and HD motifs clearly exclude C (1.3.1.36) and D (4.3.3.9). The HD-domain architecture and 194-aa length are inconsistent with classic alkaline phosphatase (3.1.3.2), which has a different fold, is much larger, and lacks HD motifs. No alternative option is genuinely defensible once these general structural/biochemical facts are applied.


### Important caveats

- The specific substrate (4'-phosphooxetanocin A) and the exact 4th-digit EC assignment are not derivable from sequence alone; a model that does not recognize the HD-domain family or the size constraints of alkaline phosphatase may struggle.
- The HD-domain superfamily contains many members with different EC 4th digits; distinguishing 3.1.3.112 from other HD-domain phosphohydrolases would require pathway or database knowledge. The question is answerable only because the distractor set is limited to four options.
- The UniProt entry was first publicly released 2025-02-05; the author's source snapshot is unknown. The sequence has been stable since 1998 (sequence version 1), so the sequence itself is not a concern.
- Evidence codes are ECO:0000269 (experimental) for the EC assignment, backed by X-ray crystallography and biochemical assays, indicating high-confidence annotation rather than computational transfer.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 194-residue length immediately argues against EC 1.3.1.36 (dihydropyrimidine dehydrogenase, typically >1000 aa with FAD/FMN cofactor domains) and EC 4.3.3.9 (methylthioadenosine deaminase, also a substantially larger enzyme), eliminating C and D. The sequence contains recognizable HD-motif pairs (e.g., '…LYALYHDVTEVVST…' and '…IVEHADHVDAY…'), which are the signature of the HD-domain phosphohydrolase superfamily. Classic alkaline phosphatase (EC 3.1.3.2) belongs to a structurally distinct alpha/beta-sandwich fold with a binuclear Zn active site, is typically 400–500 aa, and does not carry HD motifs. Recognizing the HD domain plus the small size therefore disfavors A and points toward the HD-domain phosphohydrolase B (3.1.3.112).",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The specific substrate identity (4'-phosphooxetanocin A) and the exact 4th-digit EC assignment cannot be inferred from sequence alone; this requires knowledge of the oxetanocin biosynthetic pathway or a database lookup. However, among the four provided options, the family-level reasoning (HD-domain phosphohydrolase, small size) is sufficient to eliminate A, C, and D, leaving B as the only consistent choice.",
    "reason": "A model with general knowledge of enzyme family sizes, the HD-domain phosphohydrolase superfamily, and the structural/fold differences between HD-domain enzymes and alkaline phosphatase can construct a defensible elimination chain. The final 4th-digit specificity is lookup-dependent, but the question is answerable by reasoning given the constrained option set."
  },
  "case_id": "EC_number_0108",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "C7",
      "H2",
      "H5",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The sequence (194 aa) matches UniProt O24769 (OXSA_PRIMG, Priestia megaterium) exactly. The EC number 3.1.3.112 (4'-phosphooxetanocin A phosphatase) is annotated with experimental evidence codes ECO:0000269 from PubMed:27849620 (PNAS 2016, X-ray crystallography at 1.64 Å with multiple ligand complexes) and PubMed:28346939 (Nature 2017). The catalytic reaction (4'-phosphooxetanocin A + H2O = oxetanocin A + phosphate) is confirmed by Rhea (RHEA:81367/81368) and multiple PDB structures (5TK6–5TKA). The sequence contains characteristic HD-domain motifs (e.g., 'HDVTEVVST', 'HADHVDAY') consistent with the HD-domain phosphohydrolase family."
  },
  "important_caveats": [
    "The specific substrate (4'-phosphooxetanocin A) and the exact 4th-digit EC assignment are not derivable from sequence alone; a model that does not recognize the HD-domain family or the size constraints of alkaline phosphatase may struggle.",
    "The HD-domain superfamily contains many members with different EC 4th digits; distinguishing 3.1.3.112 from other HD-domain phosphohydrolases would require pathway or database knowledge. The question is answerable only because the distractor set is limited to four options.",
    "The UniProt entry was first publicly released 2025-02-05; the author's source snapshot is unknown. The sequence has been stable since 1998 (sequence version 1), so the sequence itself is not a concern.",
    "Evidence codes are ECO:0000269 (experimental) for the EC assignment, backed by X-ray crystallography and biochemical assays, indicating high-confidence annotation rather than computational transfer."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The small size and HD motifs clearly exclude C (1.3.1.36) and D (4.3.3.9). The HD-domain architecture and 194-aa length are inconsistent with classic alkaline phosphatase (3.1.3.2), which has a different fold, is much larger, and lacks HD motifs. No alternative option is genuinely defensible once these general structural/biochemical facts are applied."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0108",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence (194 aa) matches UniProt O24769 (OXSA_PRIMG, Priestia megaterium) exactly. The EC number 3.1.3.112 (4'-phosphooxetanocin A phosphatase) is annotated with experimental evidence codes ECO:0000269 from PubMed:27849620 (PNAS 2016, X-ray crystallography at 1.64 Å with multiple ligand complexes) and PubMed:28346939 (Nature 2017). The catalytic reaction (4'-phosphooxetanocin A + H2O = oxetanocin A + phosphate) is confirmed by Rhea (RHEA:81367/81368) and multiple PDB structures (5TK6–5TKA). The sequence contains characteristic HD-domain motifs (e.g., 'HDVTEVVST', 'HADHVDAY') consistent with the HD-domain phosphohydrolase family.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "C7", "H2", "H5", "H6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 194-residue length immediately argues against EC 1.3.1.36 (dihydropyrimidine dehydrogenase, typically >1000 aa with FAD/FMN cofactor domains) and EC 4.3.3.9 (methylthioadenosine deaminase, also a substantially larger enzyme), eliminating C and D. The sequence contains recognizable HD-motif pairs (e.g., '…LYALYHDVTEVVST…' and '…IVEHADHVDAY…'), which are the signature of the HD-domain phosphohydrolase superfamily. Classic alkaline phosphatase (EC 3.1.3.2) belongs to a structurally distinct alpha/beta-sandwich fold with a binuclear Zn active site, is typically 400–500 aa, and does not carry HD motifs. Recognizing the HD domain plus the small size therefore disfavors A and points toward the HD-domain phosphohydrolase B (3.1.3.112).",
    "missing_item_specific_fact": "The specific substrate identity (4'-phosphooxetanocin A) and the exact 4th-digit EC assignment cannot be inferred from sequence alone; this requires knowledge of the oxetanocin biosynthetic pathway or a database lookup. However, among the four provided options, the family-level reasoning (HD-domain phosphohydrolase, small size) is sufficient to eliminate A, C, and D, leaving B as the only consistent choice.",
    "reason": "A model with general knowledge of enzyme family sizes, the HD-domain phosphohydrolase superfamily, and the structural/fold differences between HD-domain enzymes and alkaline phosphatase can construct a defensible elimination chain. The final 4th-digit specificity is lookup-dependent, but the question is answerable by reasoning given the constrained option set."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The small size and HD motifs clearly exclude C (1.3.1.36) and D (4.3.3.9). The HD-domain architecture and 194-aa length are inconsistent with classic alkaline phosphatase (3.1.3.2), which has a different fold, is much larger, and lacks HD motifs. No alternative option is genuinely defensible once these general structural/biochemical facts are applied."
  },
  "important_caveats": [
    "The specific substrate (4'-phosphooxetanocin A) and the exact 4th-digit EC assignment are not derivable from sequence alone; a model that does not recognize the HD-domain family or the size constraints of alkaline phosphatase may struggle.",
    "The HD-domain superfamily contains many members with different EC 4th digits; distinguishing 3.1.3.112 from other HD-domain phosphohydrolases would require pathway or database knowledge. The question is answerable only because the distractor set is limited to four options.",
    "The UniProt entry was first publicly released 2025-02-05; the author's source snapshot is unknown. The sequence has been stable since 1998 (sequence version 1), so the sequence itself is not a concern.",
    "Evidence codes are ECO:0000269 (experimental) for the EC assignment, backed by X-ray crystallography and biochemical assays, indicating high-confidence annotation rather than computational transfer."
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

**Accession:** `O24769` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 75. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O24769.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:10.548137+00:00.  

```json
"O24769"
```

Source SHA-256: `1c63e689d95c3766e652d2d5563f236adaca6c85d877b17df78572f9e47ef24b`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O24769.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:10.548137+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"28346939","source":"PubMed"}],"value":"HD-domain phosphohydrolase OxsA"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"27849620","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"28346939","source":"PubMed"}],"value":"3.1.3.112"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"4'-phosphooxetanocin A phosphatase"}}}
```

Source SHA-256: `1c63e689d95c3766e652d2d5563f236adaca6c85d877b17df78572f9e47ef24b`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O24769.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:10.548137+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000269","id":"27849620","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"28346939","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:81368"}}],"reaction":{"ecNumber":"3.1.3.112","evidences":[{"evidenceCode":"ECO:0000269","id":"27849620","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"28346939","source":"PubMed"}],"name":"4'-phosphooxetanocin A + H2O = oxetanocin A + phosphate","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:81367"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:43474"},{"database":"ChEBI","id":"CHEBI:85720"},{"database":"ChEBI","id":"CHEBI:86012"}]}}
```

Source SHA-256: `1c63e689d95c3766e652d2d5563f236adaca6c85d877b17df78572f9e47ef24b`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O24769.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:10.548137+00:00.  

```json
{"citation":{"authors":["Bridwell-Rabb J.","Zhong A.","Sun H.G.","Drennan C.L.","Liu H.W."],"citationCrossReferences":[{"database":"PubMed","id":"28346939"},{"database":"DOI","id":"10.1038/nature21689"}],"citationType":"journal article","firstPage":"322","id":"28346939","journal":"Nature","lastPage":"326","publicationDate":"2017","title":"A B12-dependent radical SAM enzyme involved in oxetanocin A biosynthesis.","volume":"544"},"referenceNumber":2,"referencePositions":["FUNCTION","CATALYTIC ACTIVITY"]}
```

Source SHA-256: `1c63e689d95c3766e652d2d5563f236adaca6c85d877b17df78572f9e47ef24b`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O24769.json)  
**Locator:** `/references/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:10.548137+00:00.  

```json
{"citation":{"authors":["Bridwell-Rabb J.","Kang G.","Zhong A.","Liu H.W.","Drennan C.L."],"citationCrossReferences":[{"database":"PubMed","id":"27849620"},{"database":"DOI","id":"10.1073/pnas.1613610113"}],"citationType":"journal article","firstPage":"13750","id":"27849620","journal":"Proc. Natl. Acad. Sci. U.S.A.","lastPage":"13755","publicationDate":"2016","title":"An HD domain phosphohydrolase active site tailored for oxetanocin-A biosynthesis.","volume":"113"},"evidences":[{"evidenceCode":"ECO:0007744","id":"5TK6","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"5TK7","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"5TK8","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"5TK9","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"5TKA","source":"PDB"}],"referenceNumber":3,"referencePositions":["X-RAY CRYSTALLOGRAPHY (1.64 ANGSTROMS) IN COMPLEXES WITH MAGNESIUM; OXETANOCIN A; OXETANOCIN A MONOPHOSPHATE; OXETANOCIN A DIPHOSPHATE AND OXETANOCIN A TRIPHOSPHATE","FUNCTION","CATALYTIC ACTIVITY","COFACTOR","BIOPHYSICOCHEMICAL PROPERTIES","SUBUNIT","DOMAIN"]}
```

Source SHA-256: `1c63e689d95c3766e652d2d5563f236adaca6c85d877b17df78572f9e47ef24b`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O24769?format=txt&versions=75)  
**Locator:** `lines 6-8`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 75 / 1.  
**Retrieved:** 2026-11-02T04:29:21.063065+00:00.  

```text
DE   RecName: Full=4'-phosphooxetanocin A phosphatase {ECO:0000305};
DE            EC=3.1.3.112 {ECO:0000269|PubMed:27849620, ECO:0000269|PubMed:28346939};
DE   AltName: Full=HD-domain phosphohydrolase OxsA {ECO:0000303|PubMed:28346939};
```

Source SHA-256: `bab6b179917835711477092cc4cbfcd87e9b1a12b22b046feb1fb9be2c17050d`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O24769?format=txt&versions=75)  
**Locator:** `lines 30-39`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 75 / 1.  
**Retrieved:** 2026-11-02T04:29:21.063065+00:00.  

```text
RN   [3] {ECO:0007744|PDB:5TK6, ECO:0007744|PDB:5TK7, ECO:0007744|PDB:5TK8, ECO:0007744|PDB:5TK9, ECO:0007744|PDB:5TKA}
RP   X-RAY CRYSTALLOGRAPHY (1.64 ANGSTROMS) IN COMPLEXES WITH MAGNESIUM;
RP   OXETANOCIN A; OXETANOCIN A MONOPHOSPHATE; OXETANOCIN A DIPHOSPHATE AND
RP   OXETANOCIN A TRIPHOSPHATE, FUNCTION, CATALYTIC ACTIVITY, COFACTOR,
RP   BIOPHYSICOCHEMICAL PROPERTIES, SUBUNIT, AND DOMAIN.
RX   PubMed=27849620; DOI=10.1073/pnas.1613610113;
RA   Bridwell-Rabb J., Kang G., Zhong A., Liu H.W., Drennan C.L.;
RT   "An HD domain phosphohydrolase active site tailored for oxetanocin-A
RT   biosynthesis.";
RL   Proc. Natl. Acad. Sci. U.S.A. 113:13750-13755(2016).
```

Source SHA-256: `bab6b179917835711477092cc4cbfcd87e9b1a12b22b046feb1fb9be2c17050d`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O24769?format=txt&versions=75)  
**Locator:** `lines 52-58`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 75 / 1.  
**Retrieved:** 2026-11-02T04:29:21.063065+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=4'-phosphooxetanocin A + H2O = oxetanocin A + phosphate;
CC         Xref=Rhea:RHEA:81367, ChEBI:CHEBI:15377, ChEBI:CHEBI:43474,
CC         ChEBI:CHEBI:85720, ChEBI:CHEBI:86012; EC=3.1.3.112;
CC         Evidence={ECO:0000269|PubMed:27849620, ECO:0000269|PubMed:28346939};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:81368;
CC         Evidence={ECO:0000269|PubMed:27849620, ECO:0000269|PubMed:28346939};
```

Source SHA-256: `bab6b179917835711477092cc4cbfcd87e9b1a12b22b046feb1fb9be2c17050d`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 108. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
