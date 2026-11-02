# EC_number_0175

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `EC_number`  
**Author expected answer:** **C** — 1.14.14.154

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MGLSHSGEIVYIHPSSPVDLFTTCASLPTKPPPSFSDMPSPLFLVSGFLGVCVAYAVANIIRQLLFPNAKEPPVVFHWFPWLGSALTYGKDPYKFLFAARAKYGDVFTFVLLGRNVTVHLGVAGNDFVFNGKETHMNAEEIYGPLCNPVFGEGVVYDCPNSKLMEQKKFVKFGLTTDALKAHVRLIEHEVVNYIKSSRDFKGPSGVINVPPVMAQITIFTAAIALQGPEVRSKLTNEFASLYHDLDGGFSPINFVLPHAPFPHNIKRDRAQLKMRKIYEAIIAERRAGKIPPTTDMISHLMQCSYKNGRPIPDSEISNMMITILMAGQHNSSNIASWIMLHLANEPQLCEELYQEQLDQLADEHGNLPELELHTVEKLKLHSSVVKETLRMHNAIHSIMRLVKQPLPVPNTSWTVPPGHAVLASPGVSANSNEYFLNPTKWDPHRWDDRVIEEDDESEMVDYGYGRTSRGTKSAYLPFGGGRHRCIGEKFAYLNLEVITAVMVRNFRFKNVDGRVDVPGTDYSTMFSRPLEPAEICWERR

[Multiple Choices]
A. 1.14.14.104
B. 3.2.1.183
C. 1.14.14.154
D. 5.2.1.8
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

> The exact 540-residue sequence matches the UniProt entry annotated as sterol 14-alpha demethylase with EC 1.14.14.154, supporting choice C. The EC assignment cites a publication; the listed catalytic-reaction annotations include evidence transferred from homologs, so they should not be treated as direct experimental measurements of this exact protein.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H1](#evidence-h1), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> Sequence features may support identifying this as a cytochrome P450, which makes the P450 choices more plausible than the hydrolase or isomerase choices. But that broad family-level inference does not establish which specific P450 reaction, and thus which complete EC number, applies.


**Missing item-specific fact**

> The protein-specific identification as sterol 14-alpha demethylase (CYP51) and its associated reaction specificity are needed to distinguish EC 1.14.14.154 from another P450 option such as 1.14.14.104.


**Reason**

> The supplied sequence and choices do not provide the functional or substrate-specific annotation needed for a complete four-part EC number. Recognizing the broad enzyme family is not enough to infer the precise EC subclass.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The matched database annotation supports a unique EC assignment for this protein. The limitation is that the input does not establish that assignment, rather than that multiple EC numbers are equally correct for the protein.


### Important caveats

- The accession and database records are reviewer-only evidence, not information supplied to the evaluated model.
- The sequence match supports applying the annotation to the sequence in the question, but database annotation and homology-transferred reaction evidence are not equivalent to independent experimental validation of every listed reaction.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Sequence features may support identifying this as a cytochrome P450, which makes the P450 choices more plausible than the hydrolase or isomerase choices. But that broad family-level inference does not establish which specific P450 reaction, and thus which complete EC number, applies.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific identification as sterol 14-alpha demethylase (CYP51) and its associated reaction specificity are needed to distinguish EC 1.14.14.154 from another P450 option such as 1.14.14.104.",
    "reason": "The supplied sequence and choices do not provide the functional or substrate-specific annotation needed for a complete four-part EC number. Recognizing the broad enzyme family is not enough to infer the precise EC subclass."
  },
  "case_id": "EC_number_0175",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H1",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact 540-residue sequence matches the UniProt entry annotated as sterol 14-alpha demethylase with EC 1.14.14.154, supporting choice C. The EC assignment cites a publication; the listed catalytic-reaction annotations include evidence transferred from homologs, so they should not be treated as direct experimental measurements of this exact protein."
  },
  "important_caveats": [
    "The accession and database records are reviewer-only evidence, not information supplied to the evaluated model.",
    "The sequence match supports applying the annotation to the sequence in the question, but database annotation and homology-transferred reaction evidence are not equivalent to independent experimental validation of every listed reaction."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched database annotation supports a unique EC assignment for this protein. The limitation is that the input does not establish that assignment, rather than that multiple EC numbers are equally correct for the protein."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0175",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact 540-residue sequence matches the UniProt entry annotated as sterol 14-alpha demethylase with EC 1.14.14.154, supporting choice C. The EC assignment cites a publication; the listed catalytic-reaction annotations include evidence transferred from homologs, so they should not be treated as direct experimental measurements of this exact protein.",
    "evidence_ids": ["C1", "C4", "C5", "H1", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "Sequence features may support identifying this as a cytochrome P450, which makes the P450 choices more plausible than the hydrolase or isomerase choices. But that broad family-level inference does not establish which specific P450 reaction, and thus which complete EC number, applies.",
    "missing_item_specific_fact": "The protein-specific identification as sterol 14-alpha demethylase (CYP51) and its associated reaction specificity are needed to distinguish EC 1.14.14.154 from another P450 option such as 1.14.14.104.",
    "reason": "The supplied sequence and choices do not provide the functional or substrate-specific annotation needed for a complete four-part EC number. Recognizing the broad enzyme family is not enough to infer the precise EC subclass."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched database annotation supports a unique EC assignment for this protein. The limitation is that the input does not establish that assignment, rather than that multiple EC numbers are equally correct for the protein."
  },
  "important_caveats": [
    "The accession and database records are reviewer-only evidence, not information supplied to the evaluated model.",
    "The sequence match supports applying the annotation to the sequence in the question, but database annotation and homology-transferred reaction evidence are not equivalent to independent experimental validation of every listed reaction."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry P0DXV0 (LAN1_PYRDE) is annotated with EC 1.14.14.154 (Sterol 14-alpha demethylase), with evidence code ECO:0000305 (inferred from direct assay) linked to PubMed:33857369 (Liu et al., 2021). The benchmark sequence matches the source sequence exactly (540 AA, SHA256 confirmed). Multiple catalytic activity reactions confirm 14α-demethylation of sterols (lanosterol, eburicol, generic 14α-methyl steroids) with NADPH-hemoprotein reductase and O2, consistent with EC 1.14.14.154.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C9](#evidence-c9), [C13](#evidence-c13), [H1](#evidence-h1), [H2](#evidence-h2), [H4](#evidence-h4), [H8](#evidence-h8), [H12](#evidence-h12).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence contains a canonical P450 heme-binding motif (FGGGRHRCIGEKF with the conserved axial Cys), confirming membership in EC class 1.14.14 (P450 monooxygenases). This eliminates B (3.2.1.183, glycosidase) and D (5.2.1.8, isomerase) as they belong to entirely different EC classes. However, both A (1.14.14.104) and C (1.14.14.154) are P450 monooxygenases in the same EC subclass. Distinguishing the 4th digit (specific substrate/reaction: sterol 14α-demethylase vs. another P450 reaction) from sequence alone requires knowing which specific substrate this enzyme acts upon.


**Missing item-specific fact**

> The specific substrate identity (14α-methyl sterol demethylation vs. whatever reaction EC 1.14.14.104 catalyzes) is an item-specific annotation fact. While one might weakly argue that fungal P450s are commonly CYP51, this is a statistical prior, not a deterministic sequence-based argument. The 4th EC digit for P450s encodes the specific substrate, which cannot be reliably deduced from general sequence features without database lookup.


**Reason**

> The question reduces to identifying the correct 4th-digit EC number among two P450 monooxygenase options. Sequence features (heme-binding motif, ~540 AA length, overall P450 fold) establish the 1.14.14 class but cannot distinguish between two specific P450 reactions. Selecting 154 over 104 requires either recognizing the exact sequence as CYP51 from memorization or accessing the UniProt annotation—both are lookup-dependent operations rather than general biological reasoning.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "C"
]
```

> Both A (1.14.14.104) and C (1.14.14.154) are P450 monooxygenase EC numbers. Without the specific substrate information or CYP51-specific active-site motif knowledge, a model cannot definitively distinguish between them from sequence alone. B and D are clearly eliminable (wrong EC class), but A vs C requires item-specific knowledge.


### Important caveats

- The EC 1.14.14.154 annotation carries evidence code ECO:0000305 (inferred from direct assay), indicating experimental support from PubMed:33857369, not merely computational prediction.
- The entry was first published 2025-02-05, making it a relatively recent annotation; the benchmark author's source snapshot is unknown.
- EC 1.14.14.104's specific identity was not independently verified in the supplied evidence; its plausibility as a P450 distractor is assumed from the EC numbering scheme.
- The sequence is from a fungal organism (Pyrenophora dematioidea), which weakly supports CYP51 (essential for ergosterol biosynthesis) as the most common fungal P450, but this statistical argument does not definitively exclude EC 1.14.14.104.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a canonical P450 heme-binding motif (FGGGRHRCIGEKF with the conserved axial Cys), confirming membership in EC class 1.14.14 (P450 monooxygenases). This eliminates B (3.2.1.183, glycosidase) and D (5.2.1.8, isomerase) as they belong to entirely different EC classes. However, both A (1.14.14.104) and C (1.14.14.154) are P450 monooxygenases in the same EC subclass. Distinguishing the 4th digit (specific substrate/reaction: sterol 14α-demethylase vs. another P450 reaction) from sequence alone requires knowing which specific substrate this enzyme acts upon.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific substrate identity (14α-methyl sterol demethylation vs. whatever reaction EC 1.14.14.104 catalyzes) is an item-specific annotation fact. While one might weakly argue that fungal P450s are commonly CYP51, this is a statistical prior, not a deterministic sequence-based argument. The 4th EC digit for P450s encodes the specific substrate, which cannot be reliably deduced from general sequence features without database lookup.",
    "reason": "The question reduces to identifying the correct 4th-digit EC number among two P450 monooxygenase options. Sequence features (heme-binding motif, ~540 AA length, overall P450 fold) establish the 1.14.14 class but cannot distinguish between two specific P450 reactions. Selecting 154 over 104 requires either recognizing the exact sequence as CYP51 from memorization or accessing the UniProt annotation—both are lookup-dependent operations rather than general biological reasoning."
  },
  "case_id": "EC_number_0175",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C9",
      "C13",
      "H1",
      "H2",
      "H4",
      "H8",
      "H12"
    ],
    "judgment": "supported",
    "reason": "UniProt entry P0DXV0 (LAN1_PYRDE) is annotated with EC 1.14.14.154 (Sterol 14-alpha demethylase), with evidence code ECO:0000305 (inferred from direct assay) linked to PubMed:33857369 (Liu et al., 2021). The benchmark sequence matches the source sequence exactly (540 AA, SHA256 confirmed). Multiple catalytic activity reactions confirm 14α-demethylation of sterols (lanosterol, eburicol, generic 14α-methyl steroids) with NADPH-hemoprotein reductase and O2, consistent with EC 1.14.14.154."
  },
  "important_caveats": [
    "The EC 1.14.14.154 annotation carries evidence code ECO:0000305 (inferred from direct assay), indicating experimental support from PubMed:33857369, not merely computational prediction.",
    "The entry was first published 2025-02-05, making it a relatively recent annotation; the benchmark author's source snapshot is unknown.",
    "EC 1.14.14.104's specific identity was not independently verified in the supplied evidence; its plausibility as a P450 distractor is assumed from the EC numbering scheme.",
    "The sequence is from a fungal organism (Pyrenophora dematioidea), which weakly supports CYP51 (essential for ergosterol biosynthesis) as the most common fungal P450, but this statistical argument does not definitively exclude EC 1.14.14.104."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "C"
    ],
    "reason": "Both A (1.14.14.104) and C (1.14.14.154) are P450 monooxygenase EC numbers. Without the specific substrate information or CYP51-specific active-site motif knowledge, a model cannot definitively distinguish between them from sequence alone. B and D are clearly eliminable (wrong EC class), but A vs C requires item-specific knowledge."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0175",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry P0DXV0 (LAN1_PYRDE) is annotated with EC 1.14.14.154 (Sterol 14-alpha demethylase), with evidence code ECO:0000305 (inferred from direct assay) linked to PubMed:33857369 (Liu et al., 2021). The benchmark sequence matches the source sequence exactly (540 AA, SHA256 confirmed). Multiple catalytic activity reactions confirm 14α-demethylation of sterols (lanosterol, eburicol, generic 14α-methyl steroids) with NADPH-hemoprotein reductase and O2, consistent with EC 1.14.14.154.",
    "evidence_ids": ["C1", "C4", "C5", "C9", "C13", "H1", "H2", "H4", "H8", "H12"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence contains a canonical P450 heme-binding motif (FGGGRHRCIGEKF with the conserved axial Cys), confirming membership in EC class 1.14.14 (P450 monooxygenases). This eliminates B (3.2.1.183, glycosidase) and D (5.2.1.8, isomerase) as they belong to entirely different EC classes. However, both A (1.14.14.104) and C (1.14.14.154) are P450 monooxygenases in the same EC subclass. Distinguishing the 4th digit (specific substrate/reaction: sterol 14α-demethylase vs. another P450 reaction) from sequence alone requires knowing which specific substrate this enzyme acts upon.",
    "missing_item_specific_fact": "The specific substrate identity (14α-methyl sterol demethylation vs. whatever reaction EC 1.14.14.104 catalyzes) is an item-specific annotation fact. While one might weakly argue that fungal P450s are commonly CYP51, this is a statistical prior, not a deterministic sequence-based argument. The 4th EC digit for P450s encodes the specific substrate, which cannot be reliably deduced from general sequence features without database lookup.",
    "reason": "The question reduces to identifying the correct 4th-digit EC number among two P450 monooxygenase options. Sequence features (heme-binding motif, ~540 AA length, overall P450 fold) establish the 1.14.14 class but cannot distinguish between two specific P450 reactions. Selecting 154 over 104 requires either recognizing the exact sequence as CYP51 from memorization or accessing the UniProt annotation—both are lookup-dependent operations rather than general biological reasoning."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "C"],
    "reason": "Both A (1.14.14.104) and C (1.14.14.154) are P450 monooxygenase EC numbers. Without the specific substrate information or CYP51-specific active-site motif knowledge, a model cannot definitively distinguish between them from sequence alone. B and D are clearly eliminable (wrong EC class), but A vs C requires item-specific knowledge."
  },
  "important_caveats": [
    "The EC 1.14.14.154 annotation carries evidence code ECO:0000305 (inferred from direct assay), indicating experimental support from PubMed:33857369, not merely computational prediction.",
    "The entry was first published 2025-02-05, making it a relatively recent annotation; the benchmark author's source snapshot is unknown.",
    "EC 1.14.14.104's specific identity was not independently verified in the supplied evidence; its plausibility as a P450 distractor is assumed from the EC numbering scheme.",
    "The sequence is from a fungal organism (Pyrenophora dematioidea), which weakly supports CYP51 (essential for ergosterol biosynthesis) as the most common fungal P450, but this statistical argument does not definitively exclude EC 1.14.14.104."
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

**Accession:** `P0DXV0` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 4. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXV0.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:42.875207+00:00.  

```json
"P0DXV0"
```

Source SHA-256: `2b160263904b8131f1c8a75b02b0f4aff9b666aad2d76208024c4b4be635743d`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXV0.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:42.875207+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"33857369","source":"PubMed"}],"value":"Cytochrome P450 monooxygenase"}},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"33857369","source":"PubMed"}],"value":"Ergosterol biosynthesis protein"}},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"33857369","source":"PubMed"}],"value":"Lanomycin biosynthesis cluster protein 1"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000305","id":"33857369","source":"PubMed"}],"value":"1.14.14.154"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"33857369","source":"PubMed"}],"value":"Sterol 14-alpha demethylase"}}}
```

Source SHA-256: `2b160263904b8131f1c8a75b02b0f4aff9b666aad2d76208024c4b4be635743d`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXV0.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:42.875207+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000250","id":"Q4WNT5","source":"UniProtKB"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:54029"}}],"reaction":{"ecNumber":"1.14.14.154","evidences":[{"evidenceCode":"ECO:0000250","id":"Q4WNT5","source":"UniProtKB"}],"name":"a 14alpha-methyl steroid + 3 reduced [NADPH--hemoprotein reductase] + 3 O2 = a Delta(14) steroid + formate + 3 oxidized [NADPH--hemoprotein reductase] + 4 H2O + 4 H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:54028"},{"database":"Rhea","id":"RHEA-COMP:11964"},{"database":"Rhea","id":"RHEA-COMP:11965"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:15379"},{"database":"ChEBI","id":"CHEBI:15740"},{"database":"ChEBI","id":"CHEBI:57618"},{"database":"ChEBI","id":"CHEBI:58210"},{"database":"ChEBI","id":"CHEBI:138029"},{"database":"ChEBI","id":"CHEBI:138031"}]}}
```

Source SHA-256: `2b160263904b8131f1c8a75b02b0f4aff9b666aad2d76208024c4b4be635743d`.

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXV0.json)  
**Locator:** `/comments/5`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:42.875207+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000250","id":"Q4WNT5","source":"UniProtKB"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:25287"}}],"reaction":{"ecNumber":"1.14.14.154","evidences":[{"evidenceCode":"ECO:0000250","id":"Q4WNT5","source":"UniProtKB"}],"name":"lanosterol + 3 reduced [NADPH--hemoprotein reductase] + 3 O2 = 4,4-dimethyl-5alpha-cholesta-8,14,24-trien-3beta-ol + formate + 3 oxidized [NADPH--hemoprotein reductase] + 4 H2O + 4 H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:25286"},{"database":"Rhea","id":"RHEA-COMP:11964"},{"database":"Rhea","id":"RHEA-COMP:11965"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:15379"},{"database":"ChEBI","id":"CHEBI:15740"},{"database":"ChEBI","id":"CHEBI:16521"},{"database":"ChEBI","id":"CHEBI:17813"},{"database":"ChEBI","id":"CHEBI:57618"},{"database":"ChEBI","id":"CHEBI:58210"}]}}
```

Source SHA-256: `2b160263904b8131f1c8a75b02b0f4aff9b666aad2d76208024c4b4be635743d`.

### Evidence C13

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXV0.json)  
**Locator:** `/comments/9`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:42.875207+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000250","id":"Q4WNT5","source":"UniProtKB"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:75440"}}],"reaction":{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q4WNT5","source":"UniProtKB"}],"name":"eburicol + 3 reduced [NADPH--hemoprotein reductase] + 3 O2 = 14-demethyleburicol + formate + 3 oxidized [NADPH--hemoprotein reductase] + 4 H2O + 4 H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:75439"},{"database":"Rhea","id":"RHEA-COMP:11964"},{"database":"Rhea","id":"RHEA-COMP:11965"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:15379"},{"database":"ChEBI","id":"CHEBI:15740"},{"database":"ChEBI","id":"CHEBI:57618"},{"database":"ChEBI","id":"CHEBI:58210"},{"database":"ChEBI","id":"CHEBI:70315"},{"database":"ChEBI","id":"CHEBI:194330"}]}}
```

Source SHA-256: `2b160263904b8131f1c8a75b02b0f4aff9b666aad2d76208024c4b4be635743d`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXV0?format=txt&versions=4)  
**Locator:** `lines 1-16`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 4 / 1.  
**Retrieved:** 2026-11-02T04:29:45.056058+00:00.  

```text
ID   LAN1_PYRDE              Reviewed;         540 AA.
AC   P0DXV0;
DT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.
DT   05-FEB-2025, sequence version 1.
DT   28-JAN-2026, entry version 4.
DE   RecName: Full=Sterol 14-alpha demethylase {ECO:0000303|PubMed:33857369};
DE            EC=1.14.14.154 {ECO:0000305|PubMed:33857369};
DE   AltName: Full=Cytochrome P450 monooxygenase {ECO:0000303|PubMed:33857369};
DE   AltName: Full=Ergosterol biosynthesis protein {ECO:0000303|PubMed:33857369};
DE   AltName: Full=Lanomycin biosynthesis cluster protein 1 {ECO:0000303|PubMed:33857369};
GN   Name=ORF1 {ECO:0000303|PubMed:33857369};
OS   Pyrenophora dematioidea (Helminthosporium dematioideum).
OC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Dothideomycetes;
OC   Pleosporomycetidae; Pleosporales; Pleosporineae; Pleosporaceae;
OC   Pyrenophora.
OX   NCBI_TaxID=139229;
```

Source SHA-256: `e154cd9089aa6b8a42d60528a7ce84bec0c5a19fc8f6e92dd2125bb46b055be2`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXV0?format=txt&versions=4)  
**Locator:** `lines 6-10`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 4 / 1.  
**Retrieved:** 2026-11-02T04:29:45.056058+00:00.  

```text
DE   RecName: Full=Sterol 14-alpha demethylase {ECO:0000303|PubMed:33857369};
DE            EC=1.14.14.154 {ECO:0000305|PubMed:33857369};
DE   AltName: Full=Cytochrome P450 monooxygenase {ECO:0000303|PubMed:33857369};
DE   AltName: Full=Ergosterol biosynthesis protein {ECO:0000303|PubMed:33857369};
DE   AltName: Full=Lanomycin biosynthesis cluster protein 1 {ECO:0000303|PubMed:33857369};
```

Source SHA-256: `e154cd9089aa6b8a42d60528a7ce84bec0c5a19fc8f6e92dd2125bb46b055be2`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXV0?format=txt&versions=4)  
**Locator:** `lines 36-46`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 4 / 1.  
**Retrieved:** 2026-11-02T04:29:45.056058+00:00.  

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

Source SHA-256: `e154cd9089aa6b8a42d60528a7ce84bec0c5a19fc8f6e92dd2125bb46b055be2`.

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXV0?format=txt&versions=4)  
**Locator:** `lines 77-87`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 4 / 1.  
**Retrieved:** 2026-11-02T04:29:45.056058+00:00.  

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

Source SHA-256: `e154cd9089aa6b8a42d60528a7ce84bec0c5a19fc8f6e92dd2125bb46b055be2`.

### Evidence H12

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXV0?format=txt&versions=4)  
**Locator:** `lines 117-126`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 4 / 1.  
**Retrieved:** 2026-11-02T04:29:45.056058+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=eburicol + 3 reduced [NADPH--hemoprotein reductase] + 3 O2 =
CC         14-demethyleburicol + formate + 3 oxidized [NADPH--hemoprotein
CC         reductase] + 4 H2O + 4 H(+); Xref=Rhea:RHEA:75439, Rhea:RHEA-
CC         COMP:11964, Rhea:RHEA-COMP:11965, ChEBI:CHEBI:15377,
CC         ChEBI:CHEBI:15378, ChEBI:CHEBI:15379, ChEBI:CHEBI:15740,
CC         ChEBI:CHEBI:57618, ChEBI:CHEBI:58210, ChEBI:CHEBI:70315,
CC         ChEBI:CHEBI:194330; Evidence={ECO:0000250|UniProtKB:Q4WNT5};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:75440;
CC         Evidence={ECO:0000250|UniProtKB:Q4WNT5};
```

Source SHA-256: `e154cd9089aa6b8a42d60528a7ce84bec0c5a19fc8f6e92dd2125bb46b055be2`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 175. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
