# EC_number_0047

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `EC_number`  
**Author expected answer:** **C** — 2.7.11.24

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MAEFVRAQIFGTTFEITSRYSDLQPVGMGAFGLVCSARDQLTNQNVAVKKIMKPFSTPVLAKRTYRELKLLKHLKHENVISLSDIFISPLEDIVLRWGCSYFVTELLGTDLHRLLTSRPLEKQFIQYFLYQIMRGLKYVHSAGVVHRDLKPSNILVNENCDLKICDFGLARIQDPQMTGYVSTRYYRAPEIMLTWQKYDVEVDIWSAGCIFAEMLEGKPLFPGKDHVNQFSIITELLGTPPDDVINTIASENTLRFVKSLPKRERQSLKHKFKNADAPAIDLLESMLVFDPKKRITATNALAHEYLAPYHDPTDEPVAEEKFDWSFNDADLPVDTWKIMMYSEILDYHNVEAGVAAMEGQEFNGQ

[Multiple Choices]
A. 2.7.13.3
B. 2.7.4.9
C. 2.7.11.24
D. 2.7.8.41
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

> The supplied sequence exactly matches the UniProt entry for a HOG1 mitogen-activated protein kinase, annotated EC 2.7.11.24. The catalytic-activity annotations support serine/threonine protein kinase activity, but their evidence is transferred by similarity from UniProtKB:P32485 (ECO:0000250), not a direct experimental assay of this sequence.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H2](#evidence-h2), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains the conserved catalytic motifs of a eukaryotic protein kinase, including HRDLK, DFG, and APE-region motifs, supporting a protein serine/threonine kinase. Among the choices, 2.7.11.24 is the protein serine/threonine kinase option; the other EC classes do not fit this kinase-domain sequence.


**Missing item-specific fact**

> The exact HOG1/MAPK identity and its assignment to EC 2.7.11.24 are not stated in the prompt; the database annotation is similarity-transferred. However, the sequence motifs and the provided choices meaningfully distinguish the protein-kinase choice from the alternatives.


**Reason**

> The sequence provides a concrete kinase-family signal that distinguishes the keyed option at the level needed among these choices. The exact subtype annotation is not independently established experimentally by the supplied evidence, but it is not necessary to reject the other listed EC classes.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The options represent distinct enzyme classes, and the sequence's eukaryotic protein kinase motifs support choice C over the listed alternatives.


### Important caveats

- The sequence match and HOG1 annotation come from reviewer-only evidence and were not available to the evaluated model.
- The UniProt EC and catalytic-activity annotations cite similarity transfer from P32485; they should not be described as direct experimental confirmation for this exact protein.
- The historical and current UniProt records match the supplied sequence, but the author's precise source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains the conserved catalytic motifs of a eukaryotic protein kinase, including HRDLK, DFG, and APE-region motifs, supporting a protein serine/threonine kinase. Among the choices, 2.7.11.24 is the protein serine/threonine kinase option; the other EC classes do not fit this kinase-domain sequence.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The exact HOG1/MAPK identity and its assignment to EC 2.7.11.24 are not stated in the prompt; the database annotation is similarity-transferred. However, the sequence motifs and the provided choices meaningfully distinguish the protein-kinase choice from the alternatives.",
    "reason": "The sequence provides a concrete kinase-family signal that distinguishes the keyed option at the level needed among these choices. The exact subtype annotation is not independently established experimentally by the supplied evidence, but it is not necessary to reject the other listed EC classes."
  },
  "case_id": "EC_number_0047",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "H2",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the UniProt entry for a HOG1 mitogen-activated protein kinase, annotated EC 2.7.11.24. The catalytic-activity annotations support serine/threonine protein kinase activity, but their evidence is transferred by similarity from UniProtKB:P32485 (ECO:0000250), not a direct experimental assay of this sequence."
  },
  "important_caveats": [
    "The sequence match and HOG1 annotation come from reviewer-only evidence and were not available to the evaluated model.",
    "The UniProt EC and catalytic-activity annotations cite similarity transfer from P32485; they should not be described as direct experimental confirmation for this exact protein.",
    "The historical and current UniProt records match the supplied sequence, but the author's precise source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The options represent distinct enzyme classes, and the sequence's eukaryotic protein kinase motifs support choice C over the listed alternatives."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0047",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the UniProt entry for a HOG1 mitogen-activated protein kinase, annotated EC 2.7.11.24. The catalytic-activity annotations support serine/threonine protein kinase activity, but their evidence is transferred by similarity from UniProtKB:P32485 (ECO:0000250), not a direct experimental assay of this sequence.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H2", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains the conserved catalytic motifs of a eukaryotic protein kinase, including HRDLK, DFG, and APE-region motifs, supporting a protein serine/threonine kinase. Among the choices, 2.7.11.24 is the protein serine/threonine kinase option; the other EC classes do not fit this kinase-domain sequence.",
    "missing_item_specific_fact": "The exact HOG1/MAPK identity and its assignment to EC 2.7.11.24 are not stated in the prompt; the database annotation is similarity-transferred. However, the sequence motifs and the provided choices meaningfully distinguish the protein-kinase choice from the alternatives.",
    "reason": "The sequence provides a concrete kinase-family signal that distinguishes the keyed option at the level needed among these choices. The exact subtype annotation is not independently established experimentally by the supplied evidence, but it is not necessary to reject the other listed EC classes."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The options represent distinct enzyme classes, and the sequence's eukaryotic protein kinase motifs support choice C over the listed alternatives."
  },
  "important_caveats": [
    "The sequence match and HOG1 annotation come from reviewer-only evidence and were not available to the evaluated model.",
    "The UniProt EC and catalytic-activity annotations cite similarity transfer from P32485; they should not be described as direct experimental confirmation for this exact protein.",
    "The historical and current UniProt records match the supplied sequence, but the author's precise source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProtKB entry A0A1B5KW97 (HOG1_USTVR) annotates this 365-aa sequence as EC 2.7.11.24 (MAP kinase). The annotation is based on similarity to S. cerevisiae HOG1 (P32485, ECO:0000250), i.e., inferred by homology rather than direct in vitro assay for this specific protein. Nonetheless, the sequence contains canonical serine/threonine protein kinase motifs (HRDLKPSN catalytic loop, DFGLARI activation motif, APE segment) and the overall ~365-aa kinase-domain architecture consistent with a MAP kinase. The EC assignment is appropriate for a serine/threonine protein kinase of the MAPK family.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H2](#evidence-h2), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The supplied sequence contains hallmark eukaryotic protein kinase motifs: the HRD catalytic loop (HRDLKPSN), the DFG activation motif (DFGLARI), and the APE segment (YYRAPEIMLTWQKYDVEVDIWSAGCIFAEMLEGKPLFPGKDHVNQFSIITELLGTPPDDVINTIASENTLRFVKSLPKRERQSLKHKFKNADAPAIDLLESMLVFDPKKRITATNALAHEYLAPYHDPTDEPVAEEKFDWSFNDADLPVDTWKIMMYSEILDYHNVEAGVAAMEGQEFNGQ). These motifs are diagnostic of serine/threonine protein kinases (EC 2.7.11.x) and are absent from histidine kinases (EC 2.7.13.x, which use HisKA/HATPase_c/HisD domains), nucleoside diphosphate kinases (EC 2.7.4.x, ~150 aa, different fold), and phosphatidylcholine synthase (EC 2.7.8.41, entirely unrelated). Among the four choices, only C (2.7.11.24) falls in the serine/threonine protein kinase class, so the motif-based reasoning eliminates A, B, and D.


**Missing item-specific fact**

> None critical. Distinguishing 2.7.11.24 from other 2.7.11.x subtypes would require specific MAPK-family recognition, but only one 2.7.11.x option is offered, so the serine/threonine kinase identification suffices to select C.


**Reason**

> A knowledgeable model can identify the HRD/DFG/APE kinase motifs in the sequence, recognize the serine/threonine protein kinase fold, and eliminate the histidine kinase (A), nucleoside diphosphate kinase (B), and phosphatidylcholine synthase (D) options on structural/biochemical grounds, arriving at C without needing to memorize this specific UniProt entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options span four distinct EC subclasses (2.7.13, 2.7.4, 2.7.11, 2.7.8) with fundamentally different catalytic mechanisms and domain architectures. The sequence motifs unambiguously indicate a serine/threonine protein kinase, making C the only defensible choice.


### Important caveats

- The UniProt EC annotation for this entry carries evidence code ECO:0000250 (inferred by similarity from P32485, S. cerevisiae HOG1), not direct experimental characterization of UvHOG1's catalytic activity. The PubMed reference (27095476) documents function and disruption phenotype but the EC assignment itself is by homology.
- The reviewer-only evidence confirms sequence match (SHA-256 identical) between the benchmark input and UniProt A0A1B5KW97, but this accession was not provided to the evaluated model.
- Distinguishing 2.7.11.24 from, say, 2.7.11.22 (ERK) or 2.7.11.25 (JNK) would require more specific MAPK-subfamily knowledge; however, only one 2.7.11.x option is presented, so this granularity is not tested here.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The supplied sequence contains hallmark eukaryotic protein kinase motifs: the HRD catalytic loop (HRDLKPSN), the DFG activation motif (DFGLARI), and the APE segment (YYRAPEIMLTWQKYDVEVDIWSAGCIFAEMLEGKPLFPGKDHVNQFSIITELLGTPPDDVINTIASENTLRFVKSLPKRERQSLKHKFKNADAPAIDLLESMLVFDPKKRITATNALAHEYLAPYHDPTDEPVAEEKFDWSFNDADLPVDTWKIMMYSEILDYHNVEAGVAAMEGQEFNGQ). These motifs are diagnostic of serine/threonine protein kinases (EC 2.7.11.x) and are absent from histidine kinases (EC 2.7.13.x, which use HisKA/HATPase_c/HisD domains), nucleoside diphosphate kinases (EC 2.7.4.x, ~150 aa, different fold), and phosphatidylcholine synthase (EC 2.7.8.41, entirely unrelated). Among the four choices, only C (2.7.11.24) falls in the serine/threonine protein kinase class, so the motif-based reasoning eliminates A, B, and D.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None critical. Distinguishing 2.7.11.24 from other 2.7.11.x subtypes would require specific MAPK-family recognition, but only one 2.7.11.x option is offered, so the serine/threonine kinase identification suffices to select C.",
    "reason": "A knowledgeable model can identify the HRD/DFG/APE kinase motifs in the sequence, recognize the serine/threonine protein kinase fold, and eliminate the histidine kinase (A), nucleoside diphosphate kinase (B), and phosphatidylcholine synthase (D) options on structural/biochemical grounds, arriving at C without needing to memorize this specific UniProt entry."
  },
  "case_id": "EC_number_0047",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H2",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "UniProtKB entry A0A1B5KW97 (HOG1_USTVR) annotates this 365-aa sequence as EC 2.7.11.24 (MAP kinase). The annotation is based on similarity to S. cerevisiae HOG1 (P32485, ECO:0000250), i.e., inferred by homology rather than direct in vitro assay for this specific protein. Nonetheless, the sequence contains canonical serine/threonine protein kinase motifs (HRDLKPSN catalytic loop, DFGLARI activation motif, APE segment) and the overall ~365-aa kinase-domain architecture consistent with a MAP kinase. The EC assignment is appropriate for a serine/threonine protein kinase of the MAPK family."
  },
  "important_caveats": [
    "The UniProt EC annotation for this entry carries evidence code ECO:0000250 (inferred by similarity from P32485, S. cerevisiae HOG1), not direct experimental characterization of UvHOG1's catalytic activity. The PubMed reference (27095476) documents function and disruption phenotype but the EC assignment itself is by homology.",
    "The reviewer-only evidence confirms sequence match (SHA-256 identical) between the benchmark input and UniProt A0A1B5KW97, but this accession was not provided to the evaluated model.",
    "Distinguishing 2.7.11.24 from, say, 2.7.11.22 (ERK) or 2.7.11.25 (JNK) would require more specific MAPK-subfamily knowledge; however, only one 2.7.11.x option is presented, so this granularity is not tested here."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span four distinct EC subclasses (2.7.13, 2.7.4, 2.7.11, 2.7.8) with fundamentally different catalytic mechanisms and domain architectures. The sequence motifs unambiguously indicate a serine/threonine protein kinase, making C the only defensible choice."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0047",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProtKB entry A0A1B5KW97 (HOG1_USTVR) annotates this 365-aa sequence as EC 2.7.11.24 (MAP kinase). The annotation is based on similarity to S. cerevisiae HOG1 (P32485, ECO:0000250), i.e., inferred by homology rather than direct in vitro assay for this specific protein. Nonetheless, the sequence contains canonical serine/threonine protein kinase motifs (HRDLKPSN catalytic loop, DFGLARI activation motif, APE segment) and the overall ~365-aa kinase-domain architecture consistent with a MAP kinase. The EC assignment is appropriate for a serine/threonine protein kinase of the MAPK family.",
    "evidence_ids": ["C4", "C5", "C6", "H2", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The supplied sequence contains hallmark eukaryotic protein kinase motifs: the HRD catalytic loop (HRDLKPSN), the DFG activation motif (DFGLARI), and the APE segment (YYRAPEIMLTWQKYDVEVDIWSAGCIFAEMLEGKPLFPGKDHVNQFSIITELLGTPPDDVINTIASENTLRFVKSLPKRERQSLKHKFKNADAPAIDLLESMLVFDPKKRITATNALAHEYLAPYHDPTDEPVAEEKFDWSFNDADLPVDTWKIMMYSEILDYHNVEAGVAAMEGQEFNGQ). These motifs are diagnostic of serine/threonine protein kinases (EC 2.7.11.x) and are absent from histidine kinases (EC 2.7.13.x, which use HisKA/HATPase_c/HisD domains), nucleoside diphosphate kinases (EC 2.7.4.x, ~150 aa, different fold), and phosphatidylcholine synthase (EC 2.7.8.41, entirely unrelated). Among the four choices, only C (2.7.11.24) falls in the serine/threonine protein kinase class, so the motif-based reasoning eliminates A, B, and D.",
    "missing_item_specific_fact": "None critical. Distinguishing 2.7.11.24 from other 2.7.11.x subtypes would require specific MAPK-family recognition, but only one 2.7.11.x option is offered, so the serine/threonine kinase identification suffices to select C.",
    "reason": "A knowledgeable model can identify the HRD/DFG/APE kinase motifs in the sequence, recognize the serine/threonine protein kinase fold, and eliminate the histidine kinase (A), nucleoside diphosphate kinase (B), and phosphatidylcholine synthase (D) options on structural/biochemical grounds, arriving at C without needing to memorize this specific UniProt entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span four distinct EC subclasses (2.7.13, 2.7.4, 2.7.11, 2.7.8) with fundamentally different catalytic mechanisms and domain architectures. The sequence motifs unambiguously indicate a serine/threonine protein kinase, making C the only defensible choice."
  },
  "important_caveats": [
    "The UniProt EC annotation for this entry carries evidence code ECO:0000250 (inferred by similarity from P32485, S. cerevisiae HOG1), not direct experimental characterization of UvHOG1's catalytic activity. The PubMed reference (27095476) documents function and disruption phenotype but the EC assignment itself is by homology.",
    "The reviewer-only evidence confirms sequence match (SHA-256 identical) between the benchmark input and UniProt A0A1B5KW97, but this accession was not provided to the evaluated model.",
    "Distinguishing 2.7.11.24 from, say, 2.7.11.22 (ERK) or 2.7.11.25 (JNK) would require more specific MAPK-subfamily knowledge; however, only one 2.7.11.x option is presented, so this granularity is not tested here."
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

**Accession:** `A0A1B5KW97` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 43. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A1B5KW97.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:42.109809+00:00.  

```json
"A0A1B5KW97"
```

Source SHA-256: `7ee6e4c25404002b92bf8b8282f294219e15f290903c7b19f54e3bfde7ec7a51`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A1B5KW97.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:42.109809+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"P32485","source":"UniProtKB"}],"value":"2.7.11.24"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"27095476","source":"PubMed"}],"value":"Mitogen-activated protein kinase HOG1"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"27095476","source":"PubMed"}],"value":"MAP kinase HOG1"}]}}
```

Source SHA-256: `7ee6e4c25404002b92bf8b8282f294219e15f290903c7b19f54e3bfde7ec7a51`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A1B5KW97.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:42.109809+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000250","id":"P32485","source":"UniProtKB"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:17990"}}],"reaction":{"ecNumber":"2.7.11.24","evidences":[{"evidenceCode":"ECO:0000250","id":"P32485","source":"UniProtKB"}],"name":"L-seryl-[protein] + ATP = O-phospho-L-seryl-[protein] + ADP + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:17989"},{"database":"Rhea","id":"RHEA-COMP:9863"},{"database":"Rhea","id":"RHEA-COMP:11604"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:29999"},{"database":"ChEBI","id":"CHEBI:30616"},{"database":"ChEBI","id":"CHEBI:83421"},{"database":"ChEBI","id":"CHEBI:456216"}]}}
```

Source SHA-256: `7ee6e4c25404002b92bf8b8282f294219e15f290903c7b19f54e3bfde7ec7a51`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A1B5KW97.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:42.109809+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000250","id":"P32485","source":"UniProtKB"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:46609"}}],"reaction":{"ecNumber":"2.7.11.24","evidences":[{"evidenceCode":"ECO:0000250","id":"P32485","source":"UniProtKB"}],"name":"L-threonyl-[protein] + ATP = O-phospho-L-threonyl-[protein] + ADP + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:46608"},{"database":"Rhea","id":"RHEA-COMP:11060"},{"database":"Rhea","id":"RHEA-COMP:11605"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:30013"},{"database":"ChEBI","id":"CHEBI:30616"},{"database":"ChEBI","id":"CHEBI:61977"},{"database":"ChEBI","id":"CHEBI:456216"}]}}
```

Source SHA-256: `7ee6e4c25404002b92bf8b8282f294219e15f290903c7b19f54e3bfde7ec7a51`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A1B5KW97?format=txt&versions=43)  
**Locator:** `lines 6-8`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 43 / 1.  
**Retrieved:** 2026-11-01T06:27:24.969302+00:00.  

```text
DE   RecName: Full=Mitogen-activated protein kinase HOG1 {ECO:0000303|PubMed:27095476};
DE            Short=MAP kinase HOG1 {ECO:0000303|PubMed:27095476};
DE            EC=2.7.11.24 {ECO:0000250|UniProtKB:P32485};
```

Source SHA-256: `616d230b921cb731551080a133a0d8bf732eab80bad21c487a2e77656464c411`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A1B5KW97?format=txt&versions=43)  
**Locator:** `lines 39-46`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 43 / 1.  
**Retrieved:** 2026-11-01T06:27:24.969302+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=L-seryl-[protein] + ATP = O-phospho-L-seryl-[protein] + ADP +
CC         H(+); Xref=Rhea:RHEA:17989, Rhea:RHEA-COMP:9863, Rhea:RHEA-
CC         COMP:11604, ChEBI:CHEBI:15378, ChEBI:CHEBI:29999, ChEBI:CHEBI:30616,
CC         ChEBI:CHEBI:83421, ChEBI:CHEBI:456216; EC=2.7.11.24;
CC         Evidence={ECO:0000250|UniProtKB:P32485};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:17990;
CC         Evidence={ECO:0000250|UniProtKB:P32485};
```

Source SHA-256: `616d230b921cb731551080a133a0d8bf732eab80bad21c487a2e77656464c411`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A1B5KW97?format=txt&versions=43)  
**Locator:** `lines 47-54`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 43 / 1.  
**Retrieved:** 2026-11-01T06:27:24.969302+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=L-threonyl-[protein] + ATP = O-phospho-L-threonyl-[protein] +
CC         ADP + H(+); Xref=Rhea:RHEA:46608, Rhea:RHEA-COMP:11060, Rhea:RHEA-
CC         COMP:11605, ChEBI:CHEBI:15378, ChEBI:CHEBI:30013, ChEBI:CHEBI:30616,
CC         ChEBI:CHEBI:61977, ChEBI:CHEBI:456216; EC=2.7.11.24;
CC         Evidence={ECO:0000250|UniProtKB:P32485};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:46609;
CC         Evidence={ECO:0000250|UniProtKB:P32485};
```

Source SHA-256: `616d230b921cb731551080a133a0d8bf732eab80bad21c487a2e77656464c411`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 47. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
