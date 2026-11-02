# EC_number_0183

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `EC_number`  
**Author expected answer:** **B** — 1.14.14.154

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MSWPLIGAYALLAFVAIIALNVTYQFLFRLLNKTRPPLVFHWIPFIGSTIHYGMDPYGFFFSCREKYGDIFTFILLGRPTTVYLGTQGNEFILNGKLKDVNAEEVYSPLTTPVFGSDVVYDCPNSKLIEQKKFIKFGLSQTALEAHVPLIEKEVEDYLAMSPNFHGTSGEVDITAAMAEITIFTAGSALQGEEVRSKLTTEFAVLYHDLDKGFTPINFMLPWAPLPHNKKRDAAHARMRAIYIDIINKRRNAGDNVPEKLDMIGNLMQCTYKNGQPLPDKEIAHIMITLLMAGQHSSSSISSWIMLRLASQPAVVEELYQEQLANLERTGPNNSLAPLQYKDFDNLPLHQNVIRETLRLNSSIHSLMRKVKNPLPVPGTPYVIPTSHVLLSAPGVTALSDEYFPNAMAWDPHRWETQAPKENDKDDIVDYGYGAISKGTSSPYLPFGAGRHRCIGEKFAYLNLAVIVATMVRHLRFSNLDGQTGVPATDYSSLFSGPMKPARIRWERRAAKSG

[Multiple Choices]
A. 1.14.14.126
B. 1.14.14.154
C. 1.1.1.1
D. 3.4.21.90
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

> The exact sequence matches the UniProt entry for sterol 14-alpha demethylase rstn2, annotated with EC 1.14.14.154. The EC annotation cites a publication with experimental evidence code ECO:0000269; this supports the expected answer, though it does not establish that every listed catalytic reaction was directly tested on this protein.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [H1](#evidence-h1), [H2](#evidence-h2).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The N-terminal hydrophobic segment and P450-like sequence features support a membrane-associated cytochrome P450, and are consistent with sterol demethylation. They do not, by themselves, establish the specific full EC assignment rather than a closely related P450 EC.


**Missing item-specific fact**

> The protein-specific functional assignment as sterol 14-alpha demethylase rstn2, including the distinction between EC 1.14.14.154 and the related EC 1.14.14.126, is absent from the input.


**Reason**

> Recognizing the broad enzyme family from sequence does not reveal the precise reaction classification. Choosing the keyed full EC depends on protein-specific annotation or experimental characterization not supplied in the question.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "B"
]
```

> The sequence supports a sterol-related P450 family assignment but does not give the protein-specific substrate/function distinction needed to choose between the two related EC candidates. The other options are less consistent with the sequence.


### Important caveats

- Reviewer-only UniProt evidence applies to an exact sequence match but was not available to the evaluated model.
- The current and archived annotations cite experimental evidence for the EC assignment; several detailed catalytic-reaction annotations are instead transferred by similarity.
- The author's exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal hydrophobic segment and P450-like sequence features support a membrane-associated cytochrome P450, and are consistent with sterol demethylation. They do not, by themselves, establish the specific full EC assignment rather than a closely related P450 EC.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific functional assignment as sterol 14-alpha demethylase rstn2, including the distinction between EC 1.14.14.154 and the related EC 1.14.14.126, is absent from the input.",
    "reason": "Recognizing the broad enzyme family from sequence does not reveal the precise reaction classification. Choosing the keyed full EC depends on protein-specific annotation or experimental characterization not supplied in the question."
  },
  "case_id": "EC_number_0183",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "H1",
      "H2"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry for sterol 14-alpha demethylase rstn2, annotated with EC 1.14.14.154. The EC annotation cites a publication with experimental evidence code ECO:0000269; this supports the expected answer, though it does not establish that every listed catalytic reaction was directly tested on this protein."
  },
  "important_caveats": [
    "Reviewer-only UniProt evidence applies to an exact sequence match but was not available to the evaluated model.",
    "The current and archived annotations cite experimental evidence for the EC assignment; several detailed catalytic-reaction annotations are instead transferred by similarity.",
    "The author's exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "B"
    ],
    "reason": "The sequence supports a sterol-related P450 family assignment but does not give the protein-specific substrate/function distinction needed to choose between the two related EC candidates. The other options are less consistent with the sequence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0183",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry for sterol 14-alpha demethylase rstn2, annotated with EC 1.14.14.154. The EC annotation cites a publication with experimental evidence code ECO:0000269; this supports the expected answer, though it does not establish that every listed catalytic reaction was directly tested on this protein.",
    "evidence_ids": ["C1", "C4", "H1", "H2"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The N-terminal hydrophobic segment and P450-like sequence features support a membrane-associated cytochrome P450, and are consistent with sterol demethylation. They do not, by themselves, establish the specific full EC assignment rather than a closely related P450 EC.",
    "missing_item_specific_fact": "The protein-specific functional assignment as sterol 14-alpha demethylase rstn2, including the distinction between EC 1.14.14.154 and the related EC 1.14.14.126, is absent from the input.",
    "reason": "Recognizing the broad enzyme family from sequence does not reveal the precise reaction classification. Choosing the keyed full EC depends on protein-specific annotation or experimental characterization not supplied in the question."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "B"],
    "reason": "The sequence supports a sterol-related P450 family assignment but does not give the protein-specific substrate/function distinction needed to choose between the two related EC candidates. The other options are less consistent with the sequence."
  },
  "important_caveats": [
    "Reviewer-only UniProt evidence applies to an exact sequence match but was not available to the evaluated model.",
    "The current and archived annotations cite experimental evidence for the EC assignment; several detailed catalytic-reaction annotations are instead transferred by similarity.",
    "The author's exact source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry A0A0L1JEW4 (sequence exactly matched, 513 AA, SHA256 match) assigns EC 1.14.14.154 with evidence code ECO:0000269 (direct assay) from PubMed:33857369. The recommended name is 'Sterol 14-alpha demethylase rstn2' and the catalytic activity describes 14α-demethylation of lanosterol/eburicol using NADPH-hemoprotein reductase and O2, consistent with EC 1.14.14.154. The EC assignment is supported by experimental evidence, not merely computational inference.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C9](#evidence-c9), [H1](#evidence-h1), [H2](#evidence-h2), [H4](#evidence-h4), [H8](#evidence-h8).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence contains the canonical P450 heme-binding motif (FGAGRHRCIGEK), confirming it is a cytochrome P450 monooxygenase (EC 1.14.14.x). The fungal origin and ergosterol-pathway context are consistent with a sterol 14α-demethylase. This reasoning eliminates C (1.1.1.1, alcohol dehydrogenase) and D (3.4.21.90, serine protease) and narrows the class to 1.14.14.x. However, distinguishing EC 1.14.14.126 from EC 1.14.14.154 requires knowing the specific IUBMB assignment for this particular CYP51 variant (rstn2 from Aspergillus nomiae). Both are sterol 14α-demethylases; the 4th digit is assigned based on fine-grained experimental characterization of substrate preferences and reaction intermediates, not derivable from sequence motifs alone.


**Missing item-specific fact**

> The specific EC 4th-digit assignment (154 vs. 126) for this particular CYP51 enzyme variant (rstn2) is an item-specific database annotation determined by experimental characterization (PubMed:33857369). No sequence feature in the provided 513-aa input distinguishes EC 1.14.14.126 from 1.14.14.154.


**Reason**

> While the sequence supports identification as a P450 sterol demethylase (eliminating C and D), the critical discrimination between the two plausible CYP51 answers (A: 1.14.14.126 vs B: 1.14.14.154) depends entirely on knowing which specific EC number the IUBMB has assigned to this enzyme variant. This is a database lookup fact, not a conclusion derivable from general biological reasoning about the sequence.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "B"
]
```

> Both 1.14.14.126 and 1.14.14.154 are sterol 14α-demethylase EC numbers within the CYP51 family. From the sequence alone, one can identify the protein as a fungal CYP51 sterol demethylase, but cannot determine whether the specific 4th-digit assignment is 126 or 154 without database knowledge. C and D are unambiguously eliminated by EC class.


### Important caveats

- The EC 1.14.14.154 assignment carries evidence code ECO:0000269 (direct assay) from PubMed:33857369, indicating experimental determination of the catalytic activity.
- The sequence match is exact (SHA256 confirmed) between the benchmark input and UniProt A0A0L1JEW4.
- EC 1.14.14.126 is a very close distractor (same EC class, same enzyme family), making this a high-difficulty discrimination that cannot be resolved by sequence reasoning alone.
- The historical UniProt entry (version 38, first released 2026-01) already contains the EC annotation, so the answer was available in the database at the time the benchmark was likely constructed.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains the canonical P450 heme-binding motif (FGAGRHRCIGEK), confirming it is a cytochrome P450 monooxygenase (EC 1.14.14.x). The fungal origin and ergosterol-pathway context are consistent with a sterol 14α-demethylase. This reasoning eliminates C (1.1.1.1, alcohol dehydrogenase) and D (3.4.21.90, serine protease) and narrows the class to 1.14.14.x. However, distinguishing EC 1.14.14.126 from EC 1.14.14.154 requires knowing the specific IUBMB assignment for this particular CYP51 variant (rstn2 from Aspergillus nomiae). Both are sterol 14α-demethylases; the 4th digit is assigned based on fine-grained experimental characterization of substrate preferences and reaction intermediates, not derivable from sequence motifs alone.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific EC 4th-digit assignment (154 vs. 126) for this particular CYP51 enzyme variant (rstn2) is an item-specific database annotation determined by experimental characterization (PubMed:33857369). No sequence feature in the provided 513-aa input distinguishes EC 1.14.14.126 from 1.14.14.154.",
    "reason": "While the sequence supports identification as a P450 sterol demethylase (eliminating C and D), the critical discrimination between the two plausible CYP51 answers (A: 1.14.14.126 vs B: 1.14.14.154) depends entirely on knowing which specific EC number the IUBMB has assigned to this enzyme variant. This is a database lookup fact, not a conclusion derivable from general biological reasoning about the sequence."
  },
  "case_id": "EC_number_0183",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C9",
      "H1",
      "H2",
      "H4",
      "H8"
    ],
    "judgment": "supported",
    "reason": "UniProt entry A0A0L1JEW4 (sequence exactly matched, 513 AA, SHA256 match) assigns EC 1.14.14.154 with evidence code ECO:0000269 (direct assay) from PubMed:33857369. The recommended name is 'Sterol 14-alpha demethylase rstn2' and the catalytic activity describes 14α-demethylation of lanosterol/eburicol using NADPH-hemoprotein reductase and O2, consistent with EC 1.14.14.154. The EC assignment is supported by experimental evidence, not merely computational inference."
  },
  "important_caveats": [
    "The EC 1.14.14.154 assignment carries evidence code ECO:0000269 (direct assay) from PubMed:33857369, indicating experimental determination of the catalytic activity.",
    "The sequence match is exact (SHA256 confirmed) between the benchmark input and UniProt A0A0L1JEW4.",
    "EC 1.14.14.126 is a very close distractor (same EC class, same enzyme family), making this a high-difficulty discrimination that cannot be resolved by sequence reasoning alone.",
    "The historical UniProt entry (version 38, first released 2026-01) already contains the EC annotation, so the answer was available in the database at the time the benchmark was likely constructed."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "B"
    ],
    "reason": "Both 1.14.14.126 and 1.14.14.154 are sterol 14α-demethylase EC numbers within the CYP51 family. From the sequence alone, one can identify the protein as a fungal CYP51 sterol demethylase, but cannot determine whether the specific 4th-digit assignment is 126 or 154 without database knowledge. C and D are unambiguously eliminated by EC class."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0183",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry A0A0L1JEW4 (sequence exactly matched, 513 AA, SHA256 match) assigns EC 1.14.14.154 with evidence code ECO:0000269 (direct assay) from PubMed:33857369. The recommended name is 'Sterol 14-alpha demethylase rstn2' and the catalytic activity describes 14α-demethylation of lanosterol/eburicol using NADPH-hemoprotein reductase and O2, consistent with EC 1.14.14.154. The EC assignment is supported by experimental evidence, not merely computational inference.",
    "evidence_ids": ["C4", "C5", "C9", "H1", "H2", "H4", "H8"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence contains the canonical P450 heme-binding motif (FGAGRHRCIGEK), confirming it is a cytochrome P450 monooxygenase (EC 1.14.14.x). The fungal origin and ergosterol-pathway context are consistent with a sterol 14α-demethylase. This reasoning eliminates C (1.1.1.1, alcohol dehydrogenase) and D (3.4.21.90, serine protease) and narrows the class to 1.14.14.x. However, distinguishing EC 1.14.14.126 from EC 1.14.14.154 requires knowing the specific IUBMB assignment for this particular CYP51 variant (rstn2 from Aspergillus nomiae). Both are sterol 14α-demethylases; the 4th digit is assigned based on fine-grained experimental characterization of substrate preferences and reaction intermediates, not derivable from sequence motifs alone.",
    "missing_item_specific_fact": "The specific EC 4th-digit assignment (154 vs. 126) for this particular CYP51 enzyme variant (rstn2) is an item-specific database annotation determined by experimental characterization (PubMed:33857369). No sequence feature in the provided 513-aa input distinguishes EC 1.14.14.126 from 1.14.14.154.",
    "reason": "While the sequence supports identification as a P450 sterol demethylase (eliminating C and D), the critical discrimination between the two plausible CYP51 answers (A: 1.14.14.126 vs B: 1.14.14.154) depends entirely on knowing which specific EC number the IUBMB has assigned to this enzyme variant. This is a database lookup fact, not a conclusion derivable from general biological reasoning about the sequence."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "B"],
    "reason": "Both 1.14.14.126 and 1.14.14.154 are sterol 14α-demethylase EC numbers within the CYP51 family. From the sequence alone, one can identify the protein as a fungal CYP51 sterol demethylase, but cannot determine whether the specific 4th-digit assignment is 126 or 154 without database knowledge. C and D are unambiguously eliminated by EC class."
  },
  "important_caveats": [
    "The EC 1.14.14.154 assignment carries evidence code ECO:0000269 (direct assay) from PubMed:33857369, indicating experimental determination of the catalytic activity.",
    "The sequence match is exact (SHA256 confirmed) between the benchmark input and UniProt A0A0L1JEW4.",
    "EC 1.14.14.126 is a very close distractor (same EC class, same enzyme family), making this a high-difficulty discrimination that cannot be resolved by sequence reasoning alone.",
    "The historical UniProt entry (version 38, first released 2026-01) already contains the EC annotation, so the answer was available in the database at the time the benchmark was likely constructed."
  ]
}
```

</details>

## Existing project source checks of Luna’s review

The notes below were prepared for specific claims in the Luna review. They are not independent validation of Qwen’s claims, expert adjudication, or replacement verdicts.

## Project source-check notes

These project-authored, AI-assisted checks assess specific source claims. They are not expert adjudication and do not replace Luna’s saved review or the author key.

### Source check 1

**Check:** `lookup_uncertainty_not_evidence_for_multiple_actual_ec_assignments`.

> C4/H1/H2 explicitly give the keyed EC1.14.14.154 with ECO:0000269. The ambiguity rationale invokes sequence-level inability to distinguish a related P450 EC option, rather than a source assigning both activities.

**Remaining uncertainty:** Keep lookup dependence separate from evidence that both choices are actual activities. No key or model label is reassigned.

Evidence checked: [C1](#evidence-c1), [C4](#evidence-c4), [H1](#evidence-h1), [H2](#evidence-h2).

## Reviewer-only source evidence

**Both reviewers received this source evidence separately from the original question. It was not available to the original evaluated model.** Source support and reasoning from the original sequence/choices are distinct assessments.

**Accession:** `A0A0L1JEW4` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 38. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0L1JEW4.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:12.364317+00:00.  

```json
"A0A0L1JEW4"
```

Source SHA-256: `d02dbb89f818b7eb87df130d530379b150615f58a7786d959f158367f6e7dbef`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0L1JEW4.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:12.364317+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"33857369","source":"PubMed"}],"value":"Cytochrome P450 monooxygenase rstn2"}},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"33857369","source":"PubMed"}],"value":"Ergosterol biosynthesis protein rstn2"}},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"33857369","source":"PubMed"}],"value":"Restricticin biosynthesis cluster protein 2"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"33857369","source":"PubMed"}],"value":"1.14.14.154"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"33857369","source":"PubMed"}],"value":"Sterol 14-alpha demethylase rstn2"}}}
```

Source SHA-256: `d02dbb89f818b7eb87df130d530379b150615f58a7786d959f158367f6e7dbef`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0L1JEW4.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:12.364317+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000250","id":"Q4WNT5","source":"UniProtKB"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:54029"}}],"reaction":{"ecNumber":"1.14.14.154","evidences":[{"evidenceCode":"ECO:0000250","id":"Q4WNT5","source":"UniProtKB"}],"name":"a 14alpha-methyl steroid + 3 reduced [NADPH--hemoprotein reductase] + 3 O2 = a Delta(14) steroid + formate + 3 oxidized [NADPH--hemoprotein reductase] + 4 H2O + 4 H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:54028"},{"database":"Rhea","id":"RHEA-COMP:11964"},{"database":"Rhea","id":"RHEA-COMP:11965"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:15379"},{"database":"ChEBI","id":"CHEBI:15740"},{"database":"ChEBI","id":"CHEBI:57618"},{"database":"ChEBI","id":"CHEBI:58210"},{"database":"ChEBI","id":"CHEBI:138029"},{"database":"ChEBI","id":"CHEBI:138031"}]}}
```

Source SHA-256: `d02dbb89f818b7eb87df130d530379b150615f58a7786d959f158367f6e7dbef`.

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0L1JEW4.json)  
**Locator:** `/comments/5`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:12.364317+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000250","id":"Q4WNT5","source":"UniProtKB"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:25287"}}],"reaction":{"ecNumber":"1.14.14.154","evidences":[{"evidenceCode":"ECO:0000250","id":"Q4WNT5","source":"UniProtKB"}],"name":"lanosterol + 3 reduced [NADPH--hemoprotein reductase] + 3 O2 = 4,4-dimethyl-5alpha-cholesta-8,14,24-trien-3beta-ol + formate + 3 oxidized [NADPH--hemoprotein reductase] + 4 H2O + 4 H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:25286"},{"database":"Rhea","id":"RHEA-COMP:11964"},{"database":"Rhea","id":"RHEA-COMP:11965"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:15379"},{"database":"ChEBI","id":"CHEBI:15740"},{"database":"ChEBI","id":"CHEBI:16521"},{"database":"ChEBI","id":"CHEBI:17813"},{"database":"ChEBI","id":"CHEBI:57618"},{"database":"ChEBI","id":"CHEBI:58210"}]}}
```

Source SHA-256: `d02dbb89f818b7eb87df130d530379b150615f58a7786d959f158367f6e7dbef`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0L1JEW4?format=txt&versions=38)  
**Locator:** `lines 1-17`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 38 / 1.  
**Retrieved:** 2026-11-02T04:24:14.653166+00:00.  

```text
ID   RSTN2_ASPN3             Reviewed;         513 AA.
AC   A0A0L1JEW4;
DT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.
DT   11-NOV-2015, sequence version 1.
DT   28-JAN-2026, entry version 38.
DE   RecName: Full=Sterol 14-alpha demethylase rstn2 {ECO:0000303|PubMed:33857369};
DE            EC=1.14.14.154 {ECO:0000269|PubMed:33857369};
DE   AltName: Full=Cytochrome P450 monooxygenase rstn2 {ECO:0000303|PubMed:33857369};
DE   AltName: Full=Ergosterol biosynthesis protein rstn2 {ECO:0000303|PubMed:33857369};
DE   AltName: Full=Restricticin biosynthesis cluster protein 2 {ECO:0000303|PubMed:33857369};
GN   Name=rstn2 {ECO:0000303|PubMed:33857369}; ORFNames=ANOM_001443;
OS   Aspergillus nomiae NRRL (strain ATCC 15546 / NRRL 13137 / CBS 260.88 /
OS   M93).
OC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Eurotiomycetes;
OC   Eurotiomycetidae; Eurotiales; Aspergillaceae; Aspergillus;
OC   Aspergillus subgen. Circumdati.
OX   NCBI_TaxID=1509407;
```

Source SHA-256: `6c3d64c65d2f83b7569168450886015fb66b6ae6595088f32ba80d12e66f79e5`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0L1JEW4?format=txt&versions=38)  
**Locator:** `lines 6-10`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 38 / 1.  
**Retrieved:** 2026-11-02T04:24:14.653166+00:00.  

```text
DE   RecName: Full=Sterol 14-alpha demethylase rstn2 {ECO:0000303|PubMed:33857369};
DE            EC=1.14.14.154 {ECO:0000269|PubMed:33857369};
DE   AltName: Full=Cytochrome P450 monooxygenase rstn2 {ECO:0000303|PubMed:33857369};
DE   AltName: Full=Ergosterol biosynthesis protein rstn2 {ECO:0000303|PubMed:33857369};
DE   AltName: Full=Restricticin biosynthesis cluster protein 2 {ECO:0000303|PubMed:33857369};
```

Source SHA-256: `6c3d64c65d2f83b7569168450886015fb66b6ae6595088f32ba80d12e66f79e5`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0L1JEW4?format=txt&versions=38)  
**Locator:** `lines 44-54`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 38 / 1.  
**Retrieved:** 2026-11-02T04:24:14.653166+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=a 14alpha-methyl steroid + 3 reduced [NADPH--hemoprotein
CC         reductase] + 3 O2 = a Delta(14) steroid + formate + 3 oxidized
CC         [NADPH--hemoprotein reductase] + 4 H2O + 4 H(+);
CC         Xref=Rhea:RHEA:54028, Rhea:RHEA-COMP:11964, Rhea:RHEA-COMP:11965,
CC         ChEBI:CHEBI:15377, ChEBI:CHEBI:15378, ChEBI:CHEBI:15379,
CC         ChEBI:CHEBI:15740, ChEBI:CHEBI:57618, ChEBI:CHEBI:58210,
CC         ChEBI:CHEBI:138029, ChEBI:CHEBI:138031; EC=1.14.14.154;
CC         Evidence={ECO:0000250|UniProtKB:Q4WNT5};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:54029;
CC         Evidence={ECO:0000250|UniProtKB:Q4WNT5};
```

Source SHA-256: `6c3d64c65d2f83b7569168450886015fb66b6ae6595088f32ba80d12e66f79e5`.

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0L1JEW4?format=txt&versions=38)  
**Locator:** `lines 85-95`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 38 / 1.  
**Retrieved:** 2026-11-02T04:24:14.653166+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=lanosterol + 3 reduced [NADPH--hemoprotein reductase] + 3 O2 =
CC         4,4-dimethyl-5alpha-cholesta-8,14,24-trien-3beta-ol + formate + 3
CC         oxidized [NADPH--hemoprotein reductase] + 4 H2O + 4 H(+);
CC         Xref=Rhea:RHEA:25286, Rhea:RHEA-COMP:11964, Rhea:RHEA-COMP:11965,
CC         ChEBI:CHEBI:15377, ChEBI:CHEBI:15378, ChEBI:CHEBI:15379,
CC         ChEBI:CHEBI:15740, ChEBI:CHEBI:16521, ChEBI:CHEBI:17813,
CC         ChEBI:CHEBI:57618, ChEBI:CHEBI:58210; EC=1.14.14.154;
CC         Evidence={ECO:0000250|UniProtKB:Q4WNT5};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:25287;
CC         Evidence={ECO:0000250|UniProtKB:Q4WNT5};
```

Source SHA-256: `6c3d64c65d2f83b7569168450886015fb66b6ae6595088f32ba80d12e66f79e5`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 183. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
