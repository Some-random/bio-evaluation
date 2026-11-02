# EC_number_0148

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `EC_number`  
**Author expected answer:** **A** — 2.7.7.80

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MSLSLNEYLRYGRQLIVPEFGLQGQISLKNSRVLVVGAGGLGCPALQYLVGAGFGTVGIVDHDTVDISNLHRQILHTSETVEMLKCESAKLQLAKLNPLVQINTHPVALSPDNSFGIFEQYDIILDCTDTPATRYLINDTAVLLGLTVISGSGLKTEGQLSILNFNNTGPCYRCFYPTPPPPSSVTACSDGGVLGPVIGIMGVMMALEAIKVVSGYYLREDVEFQPFLSLYSGYGPLQSLRTFKMRRRSPKCRVCNAGTREITRHVIETELDYAVWCGKMDYNVLEKDERVSVEQLSAQRAPYLVDVRAKEQYSIVHLPNSINIPLNALKHMDTLDVPKETMIYVICRFGNDSQLAVKHLKSIGYENCVDVIGGLTQWSRQIDPNFPIY

[Multiple Choices]
A. 2.7.7.80
B. 2.7.7.1
C. 5.6.1.1
D. 2.7.8.7
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

> The exact sequence matches the UBA4 entry, which annotates EC 2.7.7.80 for its molybdopterin-synthase adenylyltransferase activity. That assignment is transferred by similarity from UniProtKB:O95396, rather than direct experimental evidence for this sequence. The protein is also annotated with a second activity, EC 2.8.1.11, which is not among the choices.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence may suggest a multidomain enzyme with adenylation and sulfur-transfer functions, which can help distinguish it from broad alternatives such as an isomerase. But that inference does not establish the specific molybdopterin-synthase substrate or the exact EC 2.7.7.80 reaction.


**Missing item-specific fact**

> The protein-specific functional assignment that UBA4 adenylates the C-terminal Gly-Gly of the molybdopterin-synthase sulfur-carrier protein; the supplied sequence and choices do not state this substrate or activity.


**Reason**

> Choosing the precise EC requires a protein-specific substrate/function assignment. The supporting database annotation is itself transferred by similarity, and was reviewer-only rather than supplied to the evaluated model.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> A is supported among the listed options for one annotated catalytic activity. However, the wording's singular request for a complete EC number does not convey that this protein has a second annotated activity, EC 2.8.1.11, which is not offered.


### Important caveats

- The sequence match establishes applicability of the cited database record, but not direct experimental validation of either activity for this exact protein.
- The author's source snapshot is unknown; the retrieved historical entry and current entry both support EC 2.7.7.80 by similarity.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence may suggest a multidomain enzyme with adenylation and sulfur-transfer functions, which can help distinguish it from broad alternatives such as an isomerase. But that inference does not establish the specific molybdopterin-synthase substrate or the exact EC 2.7.7.80 reaction.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific functional assignment that UBA4 adenylates the C-terminal Gly-Gly of the molybdopterin-synthase sulfur-carrier protein; the supplied sequence and choices do not state this substrate or activity.",
    "reason": "Choosing the precise EC requires a protein-specific substrate/function assignment. The supporting database annotation is itself transferred by similarity, and was reviewer-only rather than supplied to the evaluated model."
  },
  "case_id": "EC_number_0148",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the UBA4 entry, which annotates EC 2.7.7.80 for its molybdopterin-synthase adenylyltransferase activity. That assignment is transferred by similarity from UniProtKB:O95396, rather than direct experimental evidence for this sequence. The protein is also annotated with a second activity, EC 2.8.1.11, which is not among the choices."
  },
  "important_caveats": [
    "The sequence match establishes applicability of the cited database record, but not direct experimental validation of either activity for this exact protein.",
    "The author's source snapshot is unknown; the retrieved historical entry and current entry both support EC 2.7.7.80 by similarity."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "A is supported among the listed options for one annotated catalytic activity. However, the wording's singular request for a complete EC number does not convey that this protein has a second annotated activity, EC 2.8.1.11, which is not offered."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0148",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the UBA4 entry, which annotates EC 2.7.7.80 for its molybdopterin-synthase adenylyltransferase activity. That assignment is transferred by similarity from UniProtKB:O95396, rather than direct experimental evidence for this sequence. The protein is also annotated with a second activity, EC 2.8.1.11, which is not among the choices.",
    "evidence_ids": ["C1", "C4", "C5", "C6"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence may suggest a multidomain enzyme with adenylation and sulfur-transfer functions, which can help distinguish it from broad alternatives such as an isomerase. But that inference does not establish the specific molybdopterin-synthase substrate or the exact EC 2.7.7.80 reaction.",
    "missing_item_specific_fact": "The protein-specific functional assignment that UBA4 adenylates the C-terminal Gly-Gly of the molybdopterin-synthase sulfur-carrier protein; the supplied sequence and choices do not state this substrate or activity.",
    "reason": "Choosing the precise EC requires a protein-specific substrate/function assignment. The supporting database annotation is itself transferred by similarity, and was reviewer-only rather than supplied to the evaluated model."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "A is supported among the listed options for one annotated catalytic activity. However, the wording's singular request for a complete EC number does not convey that this protein has a second annotated activity, EC 2.8.1.11, which is not offered."
  },
  "important_caveats": [
    "The sequence match establishes applicability of the cited database record, but not direct experimental validation of either activity for this exact protein.",
    "The author's source snapshot is unknown; the retrieved historical entry and current entry both support EC 2.7.7.80 by similarity."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry W1QET1 (UBA4_OGAPD) lists EC 2.7.7.80 (Molybdopterin-synthase adenylyltransferase) as one of two EC numbers for this protein, with catalytic activity RHEA:43616 confirmed. The annotation is transferred by similarity (ECO:0000250 to O95396, human UBA4), not direct experiment on this sequence, but it is the established database annotation. The sequence matches (389 aa, SHA-256 confirmed). Among the four choices, only 2.7.7.80 corresponds to an actual EC number for this protein. The second EC number (2.8.1.11) is not among the options, so A is the uniquely correct choice from the given set.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence contains a nucleotidyltransferase-like motif (GAGGLGCPALQYLVGAGFGTVGIVDHDT), which could help a knowledgeable model eliminate C (5.6.1.1, a chromatin-remodeling ATPase) and possibly D (2.7.8.7, CDP-diacylglycerol synthase with a different domain architecture). However, both A (2.7.7.80) and B (2.7.7.1) are nucleotidyltransferases sharing the same fold class. Distinguishing molybdopterin-synthase adenylyltransferase from DNA-directed RNA polymerase requires knowing the specific substrate (molybdopterin-synthase sulfur-carrier protein vs. RNA template), which is an item-specific fact about this protein's function in molybdenum cofactor biosynthesis.


**Missing item-specific fact**

> The identification of this sequence as UBA4, a bifunctional enzyme in the molybdenum cofactor (Moco) biosynthesis pathway that adenylylates the C-terminal Gly-Gly of MOCS2A, is required to select 2.7.7.80 over 2.7.7.1. No general sequence feature in the provided input reveals this substrate specificity.


**Reason**

> While the nucleotidyltransferase domain narrows the class to EC 2.7.x.x, the final distinction between 2.7.7.80 and 2.7.7.1 depends on knowing the protein's specific biological role (molybdenum cofactor biosynthesis) and substrate (MOCS2A sulfur-carrier protein), which is an item-specific annotation fact not derivable from the sequence alone through general reasoning.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Although the protein carries two EC numbers (2.7.7.80 and 2.8.1.11), only 2.7.7.80 appears among the four choices. The other three options (2.7.7.1, 5.6.1.1, 2.7.8.7) do not correspond to this protein's annotation. Thus the singular phrasing 'the EC number' does not create genuine ambiguity among the provided options.


### Important caveats

- The EC 2.7.7.80 annotation carries evidence code ECO:0000250 (similarity to UniProtKB:O95396, human UBA4), meaning it is transferred by homology rather than directly demonstrated on the Ogataea parapolymorpha protein.
- The protein is bifunctional (adenylyltransferase + sulfurtransferase); the question's singular 'EC number' phrasing slightly misrepresents the protein's enzymatic profile, though this does not affect answer selection given the provided choices.
- The UniProt entry was first publicly released 2025-06-18; the historical record at entry version 67 (2026-01-28) already contains the same EC annotations, so the answer is stable across the relevant snapshot window.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a nucleotidyltransferase-like motif (GAGGLGCPALQYLVGAGFGTVGIVDHDT), which could help a knowledgeable model eliminate C (5.6.1.1, a chromatin-remodeling ATPase) and possibly D (2.7.8.7, CDP-diacylglycerol synthase with a different domain architecture). However, both A (2.7.7.80) and B (2.7.7.1) are nucleotidyltransferases sharing the same fold class. Distinguishing molybdopterin-synthase adenylyltransferase from DNA-directed RNA polymerase requires knowing the specific substrate (molybdopterin-synthase sulfur-carrier protein vs. RNA template), which is an item-specific fact about this protein's function in molybdenum cofactor biosynthesis.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The identification of this sequence as UBA4, a bifunctional enzyme in the molybdenum cofactor (Moco) biosynthesis pathway that adenylylates the C-terminal Gly-Gly of MOCS2A, is required to select 2.7.7.80 over 2.7.7.1. No general sequence feature in the provided input reveals this substrate specificity.",
    "reason": "While the nucleotidyltransferase domain narrows the class to EC 2.7.x.x, the final distinction between 2.7.7.80 and 2.7.7.1 depends on knowing the protein's specific biological role (molybdenum cofactor biosynthesis) and substrate (MOCS2A sulfur-carrier protein), which is an item-specific annotation fact not derivable from the sequence alone through general reasoning."
  },
  "case_id": "EC_number_0148",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "UniProt entry W1QET1 (UBA4_OGAPD) lists EC 2.7.7.80 (Molybdopterin-synthase adenylyltransferase) as one of two EC numbers for this protein, with catalytic activity RHEA:43616 confirmed. The annotation is transferred by similarity (ECO:0000250 to O95396, human UBA4), not direct experiment on this sequence, but it is the established database annotation. The sequence matches (389 aa, SHA-256 confirmed). Among the four choices, only 2.7.7.80 corresponds to an actual EC number for this protein. The second EC number (2.8.1.11) is not among the options, so A is the uniquely correct choice from the given set."
  },
  "important_caveats": [
    "The EC 2.7.7.80 annotation carries evidence code ECO:0000250 (similarity to UniProtKB:O95396, human UBA4), meaning it is transferred by homology rather than directly demonstrated on the Ogataea parapolymorpha protein.",
    "The protein is bifunctional (adenylyltransferase + sulfurtransferase); the question's singular 'EC number' phrasing slightly misrepresents the protein's enzymatic profile, though this does not affect answer selection given the provided choices.",
    "The UniProt entry was first publicly released 2025-06-18; the historical record at entry version 67 (2026-01-28) already contains the same EC annotations, so the answer is stable across the relevant snapshot window."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although the protein carries two EC numbers (2.7.7.80 and 2.8.1.11), only 2.7.7.80 appears among the four choices. The other three options (2.7.7.1, 5.6.1.1, 2.7.8.7) do not correspond to this protein's annotation. Thus the singular phrasing 'the EC number' does not create genuine ambiguity among the provided options."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0148",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry W1QET1 (UBA4_OGAPD) lists EC 2.7.7.80 (Molybdopterin-synthase adenylyltransferase) as one of two EC numbers for this protein, with catalytic activity RHEA:43616 confirmed. The annotation is transferred by similarity (ECO:0000250 to O95396, human UBA4), not direct experiment on this sequence, but it is the established database annotation. The sequence matches (389 aa, SHA-256 confirmed). Among the four choices, only 2.7.7.80 corresponds to an actual EC number for this protein. The second EC number (2.8.1.11) is not among the options, so A is the uniquely correct choice from the given set.",
    "evidence_ids": ["C4", "C5", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence contains a nucleotidyltransferase-like motif (GAGGLGCPALQYLVGAGFGTVGIVDHDT), which could help a knowledgeable model eliminate C (5.6.1.1, a chromatin-remodeling ATPase) and possibly D (2.7.8.7, CDP-diacylglycerol synthase with a different domain architecture). However, both A (2.7.7.80) and B (2.7.7.1) are nucleotidyltransferases sharing the same fold class. Distinguishing molybdopterin-synthase adenylyltransferase from DNA-directed RNA polymerase requires knowing the specific substrate (molybdopterin-synthase sulfur-carrier protein vs. RNA template), which is an item-specific fact about this protein's function in molybdenum cofactor biosynthesis.",
    "missing_item_specific_fact": "The identification of this sequence as UBA4, a bifunctional enzyme in the molybdenum cofactor (Moco) biosynthesis pathway that adenylylates the C-terminal Gly-Gly of MOCS2A, is required to select 2.7.7.80 over 2.7.7.1. No general sequence feature in the provided input reveals this substrate specificity.",
    "reason": "While the nucleotidyltransferase domain narrows the class to EC 2.7.x.x, the final distinction between 2.7.7.80 and 2.7.7.1 depends on knowing the protein's specific biological role (molybdenum cofactor biosynthesis) and substrate (MOCS2A sulfur-carrier protein), which is an item-specific annotation fact not derivable from the sequence alone through general reasoning."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although the protein carries two EC numbers (2.7.7.80 and 2.8.1.11), only 2.7.7.80 appears among the four choices. The other three options (2.7.7.1, 5.6.1.1, 2.7.8.7) do not correspond to this protein's annotation. Thus the singular phrasing 'the EC number' does not create genuine ambiguity among the provided options."
  },
  "important_caveats": [
    "The EC 2.7.7.80 annotation carries evidence code ECO:0000250 (similarity to UniProtKB:O95396, human UBA4), meaning it is transferred by homology rather than directly demonstrated on the Ogataea parapolymorpha protein.",
    "The protein is bifunctional (adenylyltransferase + sulfurtransferase); the question's singular 'EC number' phrasing slightly misrepresents the protein's enzymatic profile, though this does not affect answer selection given the provided choices.",
    "The UniProt entry was first publicly released 2025-06-18; the historical record at entry version 67 (2026-01-28) already contains the same EC annotations, so the answer is stable across the relevant snapshot window."
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

**Accession:** `W1QET1` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 67. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/W1QET1.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:34:06.106793+00:00.  

```json
"W1QET1"
```

Source SHA-256: `958c25c940d458086b51fa46493ccb8538925f70cafe7242c4eeff6965bc6e08`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/W1QET1.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:34:06.106793+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Ubiquitin-like protein activator 4"}}],"includes":[{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Adenylyltransferase UBA4"}},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Sulfur carrier protein MOCS2A adenylyltransferase"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"O95396","source":"UniProtKB"}],"value":"2.7.7.80"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Molybdopterin-synthase adenylyltransferase"}}},{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Sulfur carrier protein MOCS2A sulfurtransferase"}},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Sulfurtransferase UBA4"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"O95396","source":"UniProtKB"}],"value":"2.8.1.11"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Molybdopterin-synthase sulfurtransferase"}}}],"recommendedName":{"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Adenylyltransferase and sulfurtransferase uba4"}}}
```

Source SHA-256: `958c25c940d458086b51fa46493ccb8538925f70cafe7242c4eeff6965bc6e08`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/W1QET1.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:34:06.106793+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"2.7.7.80","evidences":[{"evidenceCode":"ECO:0000250","id":"O95396","source":"UniProtKB"}],"name":"[molybdopterin-synthase sulfur-carrier protein]-C-terminal Gly-Gly + ATP + H(+) = [molybdopterin-synthase sulfur-carrier protein]-C-terminal Gly-Gly-AMP + diphosphate","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:43616"},{"database":"Rhea","id":"RHEA-COMP:12159"},{"database":"Rhea","id":"RHEA-COMP:12202"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:30616"},{"database":"ChEBI","id":"CHEBI:33019"},{"database":"ChEBI","id":"CHEBI:90618"},{"database":"ChEBI","id":"CHEBI:90778"}]}}
```

Source SHA-256: `958c25c940d458086b51fa46493ccb8538925f70cafe7242c4eeff6965bc6e08`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/W1QET1.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:34:06.106793+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"2.8.1.11","evidences":[{"evidenceCode":"ECO:0000250","id":"O95396","source":"UniProtKB"}],"name":"[molybdopterin-synthase sulfur-carrier protein]-C-terminal Gly-Gly-AMP + S-sulfanyl-L-cysteinyl-[cysteine desulfurase] + AH2 = [molybdopterin-synthase sulfur-carrier protein]-C-terminal-Gly-aminoethanethioate + L-cysteinyl-[cysteine desulfurase] + A + AMP + 2 H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:48612"},{"database":"Rhea","id":"RHEA-COMP:12157"},{"database":"Rhea","id":"RHEA-COMP:12158"},{"database":"Rhea","id":"RHEA-COMP:12159"},{"database":"Rhea","id":"RHEA-COMP:19907"},{"database":"ChEBI","id":"CHEBI:13193"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:17499"},{"database":"ChEBI","id":"CHEBI:29950"},{"database":"ChEBI","id":"CHEBI:61963"},{"database":"ChEBI","id":"CHEBI:90618"},{"database":"ChEBI","id":"CHEBI:232372"},{"database":"ChEBI","id":"CHEBI:456215"}]}}
```

Source SHA-256: `958c25c940d458086b51fa46493ccb8538925f70cafe7242c4eeff6965bc6e08`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/W1QET1?format=txt&versions=67)  
**Locator:** `lines 6-17`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 67 / 1.  
**Retrieved:** 2026-11-02T04:34:08.361822+00:00.  

```text
DE   RecName: Full=Adenylyltransferase and sulfurtransferase uba4 {ECO:0000305};
DE   AltName: Full=Ubiquitin-like protein activator 4 {ECO:0000305};
DE   Includes:
DE     RecName: Full=Molybdopterin-synthase adenylyltransferase {ECO:0000305};
DE              EC=2.7.7.80 {ECO:0000250|UniProtKB:O95396};
DE     AltName: Full=Adenylyltransferase UBA4 {ECO:0000305};
DE     AltName: Full=Sulfur carrier protein MOCS2A adenylyltransferase {ECO:0000305};
DE   Includes:
DE     RecName: Full=Molybdopterin-synthase sulfurtransferase {ECO:0000305};
DE              EC=2.8.1.11 {ECO:0000250|UniProtKB:O95396};
DE     AltName: Full=Sulfur carrier protein MOCS2A sulfurtransferase {ECO:0000305};
DE     AltName: Full=Sulfurtransferase UBA4 {ECO:0000305};
```

Source SHA-256: `1439891a4b0a62345927d6f7a896540071a99c07ab5153e3c7dc6126a8edc193`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/W1QET1?format=txt&versions=67)  
**Locator:** `lines 61-68`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 67 / 1.  
**Retrieved:** 2026-11-02T04:34:08.361822+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=[molybdopterin-synthase sulfur-carrier protein]-C-terminal
CC         Gly-Gly + ATP + H(+) = [molybdopterin-synthase sulfur-carrier
CC         protein]-C-terminal Gly-Gly-AMP + diphosphate; Xref=Rhea:RHEA:43616,
CC         Rhea:RHEA-COMP:12159, Rhea:RHEA-COMP:12202, ChEBI:CHEBI:15378,
CC         ChEBI:CHEBI:30616, ChEBI:CHEBI:33019, ChEBI:CHEBI:90618,
CC         ChEBI:CHEBI:90778; EC=2.7.7.80;
CC         Evidence={ECO:0000250|UniProtKB:O95396};
```

Source SHA-256: `1439891a4b0a62345927d6f7a896540071a99c07ab5153e3c7dc6126a8edc193`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 148. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
