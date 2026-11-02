# EC_number_0026

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `EC_number`  
**Author expected answer:** **D** — 1.6.5.2

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MTAAGFNSILCLRQLVRLNRRQYSAPAKSVLSGSQTNDQATPPPTSKSADKMRGWQLHNYGDIDELQLSEMLKIPQIRCSNECLVRIRATAVNPIDLAMLRGYGATVLNKMRCQPGDGIEFPLILGREFCGELVQTGMGVSLPLGSRVWGVVPLQATIGSHAEYVAVPSYCLAPAPKELDDYEAASVLYAGLTAWSGLYITGGLGGPCGATTASGGGAHKRVLVLGGSGGVGTLAIQILKSQKVQVLATCSENAIEMVRNLGADLVVDYNNPQAMEELCKYAPYDIVLDCAGQGGQKAAESKYDFRQYITFSSPLLANIDKQGLGVGALKNVFDLFQTNVRSVTQRGGLVKWGFFSPAPQGIQFLQKLVEQRKLMPLIDSSYGFSELPKAFEKMKSGHLRGKIVVKLREETGD

[Multiple Choices]
A. 1.5.1.38
B. 2.7.1.52
C. 3.1.1.4
D. 1.6.5.2
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

> The supplied sequence exactly matches the Drosophila RTN4IP1 entry, which is annotated with EC 1.6.5.2 and quinone-reduction reactions. The annotation is transferred by similarity from UniProtKB:Q8WWV3 (ECO:0000250), so it supports choice D but does not establish direct experimental confirmation for this exact protein.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H2](#evidence-h2), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence alone does not provide a sufficiently specific, defensible basis to identify the exact quinone-reduction EC activity among these choices.


**Missing item-specific fact**

> The protein-specific RTN4IP1 functional annotation linking this sequence to EC 1.6.5.2; the available annotation is transferred from a homolog.


**Reason**

> The reviewer-only sequence-matched database entry supports the key, but that annotation was not supplied to the evaluated model. Recognizing or retrieving the protein's identity and function is needed to distinguish the exact EC number.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The supplied evidence supports EC 1.6.5.2; it does not support any of the other listed options.


### Important caveats

- The EC annotation for the matched protein is based on evidence transferred from UniProtKB:Q8WWV3, not evidence shown here as direct measurement on this exact protein.
- The exact author data-source snapshot is unknown, although the sequence-matched historical entry also contains the EC annotation.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence alone does not provide a sufficiently specific, defensible basis to identify the exact quinone-reduction EC activity among these choices.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific RTN4IP1 functional annotation linking this sequence to EC 1.6.5.2; the available annotation is transferred from a homolog.",
    "reason": "The reviewer-only sequence-matched database entry supports the key, but that annotation was not supplied to the evaluated model. Recognizing or retrieving the protein's identity and function is needed to distinguish the exact EC number."
  },
  "case_id": "EC_number_0026",
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
    "reason": "The supplied sequence exactly matches the Drosophila RTN4IP1 entry, which is annotated with EC 1.6.5.2 and quinone-reduction reactions. The annotation is transferred by similarity from UniProtKB:Q8WWV3 (ECO:0000250), so it supports choice D but does not establish direct experimental confirmation for this exact protein."
  },
  "important_caveats": [
    "The EC annotation for the matched protein is based on evidence transferred from UniProtKB:Q8WWV3, not evidence shown here as direct measurement on this exact protein.",
    "The exact author data-source snapshot is unknown, although the sequence-matched historical entry also contains the EC annotation."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied evidence supports EC 1.6.5.2; it does not support any of the other listed options."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0026",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the Drosophila RTN4IP1 entry, which is annotated with EC 1.6.5.2 and quinone-reduction reactions. The annotation is transferred by similarity from UniProtKB:Q8WWV3 (ECO:0000250), so it supports choice D but does not establish direct experimental confirmation for this exact protein.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H2", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence alone does not provide a sufficiently specific, defensible basis to identify the exact quinone-reduction EC activity among these choices.",
    "missing_item_specific_fact": "The protein-specific RTN4IP1 functional annotation linking this sequence to EC 1.6.5.2; the available annotation is transferred from a homolog.",
    "reason": "The reviewer-only sequence-matched database entry supports the key, but that annotation was not supplied to the evaluated model. Recognizing or retrieving the protein's identity and function is needed to distinguish the exact EC number."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied evidence supports EC 1.6.5.2; it does not support any of the other listed options."
  },
  "important_caveats": [
    "The EC annotation for the matched protein is based on evidence transferred from UniProtKB:Q8WWV3, not evidence shown here as direct measurement on this exact protein.",
    "The exact author data-source snapshot is unknown, although the sequence-matched historical entry also contains the EC annotation."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry Q8IPZ3 (RT4I1_DROME) is annotated with EC 1.6.5.2 (NAD(P)H:quinone oxidoreductase). The sequence matches exactly (413 aa, SHA256 confirmed). The annotation evidence code is ECO:0000250 (similarity to Q8WWV3), but a 2024 Nature Chemical Biology paper (PubMed:37884807) provides experimental FUNCTION evidence confirming RTN4IP1/OPA10 as an oxidoreductase for coenzyme Q synthesis. Catalytic activity reactions (quinone + NAD(P)H + H+ → quinol + NAD(P)+) are consistent with EC 1.6.5.2.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a clear Rossmann-fold NAD(P)H-binding motif (GGSGGVG, consistent with GxGxxG pattern) and a recognizable FAD-binding domain (GYGATVLNKM...REFCGELVQTGMGVSLPLGSRVWGVVPLQATIGSHAEYVAVPSYCLAPAPKELDDYEAASVLYAGLTAWSGLYITGGLGG), together with an N-terminal mitochondrial targeting signal (positively charged, amphipathic helix features). These features indicate a mitochondrial FAD/NAD(P)H-dependent oxidoreductase involved in electron transport, consistent with a quinone oxidoreductase. This eliminates B (kinase, no NAD(P)H/FAD motifs) and C (hydrolase, no redox cofactor motifs). The 413-aa size with dual FAD+NAD(P)H domains eliminates A (dihydrofolate reductase is ~180 aa, lacks FAD-binding architecture, and is not mitochondrial). Among the four choices, only D (1.6.5.2, NAD(P)H:quinone oxidoreductase) matches the observed domain architecture and subcellular targeting.


**Missing item-specific fact**

> The specific quinone substrate identity (ubiquinone/coenzyme Q) and the precise EC 4-digit assignment 1.6.5.2 versus other EC 1.x.x.x oxidoreductases require knowledge that mitochondrial FAD/NAD(P)H oxidoreductases of this architecture reduce quinones in the electron transport chain. However, among the four provided options, the sequence features sufficiently narrow the choice to D.


**Reason**

> The Rossmann-fold NAD(P)H-binding motif, FAD-binding domain, mitochondrial targeting, and overall size provide concrete biological reasoning that eliminates the kinase (B), hydrolase (C), and small DHFR (A) options, leaving the quinone oxidoreductase (D) as the only consistent choice. The argument is based on general protein domain biology rather than memorization of a specific database entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options span three different EC classes (oxidoreductases, transferases, hydrolases). The sequence's NAD(P)H-binding and FAD-binding motifs, mitochondrial targeting, and 413-aa size clearly eliminate B (kinase), C (hydrolase), and A (small DHFR without FAD domain). Only D is consistent with the observed architecture.


### Important caveats

- The UniProt annotation for EC 1.6.5.2 on Q8IPZ3 is primarily by similarity (ECO:0000250 to Q8WWV3, the human ortholog), though a 2024 experimental paper supports the oxidoreductase function.
- The specific 4-digit EC assignment (1.6.5.2 vs. other EC 1.x.x.x) relies on knowledge that mitochondrial FAD/NAD(P)H oxidoreductases of this domain architecture reduce quinones; this is general biochemistry but the exact 4th digit (1.6.5.2) is a database annotation.
- The identity of the protein (Q8IPZ3, RTN4IP1) was inferred by the reviewer from metadata not provided to the model; the model must work from the sequence alone.
- The annotation was first integrated into Swiss-Prot in April 2025; the benchmark author's source snapshot date is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a clear Rossmann-fold NAD(P)H-binding motif (GGSGGVG, consistent with GxGxxG pattern) and a recognizable FAD-binding domain (GYGATVLNKM...REFCGELVQTGMGVSLPLGSRVWGVVPLQATIGSHAEYVAVPSYCLAPAPKELDDYEAASVLYAGLTAWSGLYITGGLGG), together with an N-terminal mitochondrial targeting signal (positively charged, amphipathic helix features). These features indicate a mitochondrial FAD/NAD(P)H-dependent oxidoreductase involved in electron transport, consistent with a quinone oxidoreductase. This eliminates B (kinase, no NAD(P)H/FAD motifs) and C (hydrolase, no redox cofactor motifs). The 413-aa size with dual FAD+NAD(P)H domains eliminates A (dihydrofolate reductase is ~180 aa, lacks FAD-binding architecture, and is not mitochondrial). Among the four choices, only D (1.6.5.2, NAD(P)H:quinone oxidoreductase) matches the observed domain architecture and subcellular targeting.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The specific quinone substrate identity (ubiquinone/coenzyme Q) and the precise EC 4-digit assignment 1.6.5.2 versus other EC 1.x.x.x oxidoreductases require knowledge that mitochondrial FAD/NAD(P)H oxidoreductases of this architecture reduce quinones in the electron transport chain. However, among the four provided options, the sequence features sufficiently narrow the choice to D.",
    "reason": "The Rossmann-fold NAD(P)H-binding motif, FAD-binding domain, mitochondrial targeting, and overall size provide concrete biological reasoning that eliminates the kinase (B), hydrolase (C), and small DHFR (A) options, leaving the quinone oxidoreductase (D) as the only consistent choice. The argument is based on general protein domain biology rather than memorization of a specific database entry."
  },
  "case_id": "EC_number_0026",
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
    "reason": "UniProt entry Q8IPZ3 (RT4I1_DROME) is annotated with EC 1.6.5.2 (NAD(P)H:quinone oxidoreductase). The sequence matches exactly (413 aa, SHA256 confirmed). The annotation evidence code is ECO:0000250 (similarity to Q8WWV3), but a 2024 Nature Chemical Biology paper (PubMed:37884807) provides experimental FUNCTION evidence confirming RTN4IP1/OPA10 as an oxidoreductase for coenzyme Q synthesis. Catalytic activity reactions (quinone + NAD(P)H + H+ → quinol + NAD(P)+) are consistent with EC 1.6.5.2."
  },
  "important_caveats": [
    "The UniProt annotation for EC 1.6.5.2 on Q8IPZ3 is primarily by similarity (ECO:0000250 to Q8WWV3, the human ortholog), though a 2024 experimental paper supports the oxidoreductase function.",
    "The specific 4-digit EC assignment (1.6.5.2 vs. other EC 1.x.x.x) relies on knowledge that mitochondrial FAD/NAD(P)H oxidoreductases of this domain architecture reduce quinones; this is general biochemistry but the exact 4th digit (1.6.5.2) is a database annotation.",
    "The identity of the protein (Q8IPZ3, RTN4IP1) was inferred by the reviewer from metadata not provided to the model; the model must work from the sequence alone.",
    "The annotation was first integrated into Swiss-Prot in April 2025; the benchmark author's source snapshot date is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span three different EC classes (oxidoreductases, transferases, hydrolases). The sequence's NAD(P)H-binding and FAD-binding motifs, mitochondrial targeting, and 413-aa size clearly eliminate B (kinase), C (hydrolase), and A (small DHFR without FAD domain). Only D is consistent with the observed architecture."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0026",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry Q8IPZ3 (RT4I1_DROME) is annotated with EC 1.6.5.2 (NAD(P)H:quinone oxidoreductase). The sequence matches exactly (413 aa, SHA256 confirmed). The annotation evidence code is ECO:0000250 (similarity to Q8WWV3), but a 2024 Nature Chemical Biology paper (PubMed:37884807) provides experimental FUNCTION evidence confirming RTN4IP1/OPA10 as an oxidoreductase for coenzyme Q synthesis. Catalytic activity reactions (quinone + NAD(P)H + H+ → quinol + NAD(P)+) are consistent with EC 1.6.5.2.",
    "evidence_ids": ["C4", "C5", "C6", "C7", "H2", "H3", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a clear Rossmann-fold NAD(P)H-binding motif (GGSGGVG, consistent with GxGxxG pattern) and a recognizable FAD-binding domain (GYGATVLNKM...REFCGELVQTGMGVSLPLGSRVWGVVPLQATIGSHAEYVAVPSYCLAPAPKELDDYEAASVLYAGLTAWSGLYITGGLGG), together with an N-terminal mitochondrial targeting signal (positively charged, amphipathic helix features). These features indicate a mitochondrial FAD/NAD(P)H-dependent oxidoreductase involved in electron transport, consistent with a quinone oxidoreductase. This eliminates B (kinase, no NAD(P)H/FAD motifs) and C (hydrolase, no redox cofactor motifs). The 413-aa size with dual FAD+NAD(P)H domains eliminates A (dihydrofolate reductase is ~180 aa, lacks FAD-binding architecture, and is not mitochondrial). Among the four choices, only D (1.6.5.2, NAD(P)H:quinone oxidoreductase) matches the observed domain architecture and subcellular targeting.",
    "missing_item_specific_fact": "The specific quinone substrate identity (ubiquinone/coenzyme Q) and the precise EC 4-digit assignment 1.6.5.2 versus other EC 1.x.x.x oxidoreductases require knowledge that mitochondrial FAD/NAD(P)H oxidoreductases of this architecture reduce quinones in the electron transport chain. However, among the four provided options, the sequence features sufficiently narrow the choice to D.",
    "reason": "The Rossmann-fold NAD(P)H-binding motif, FAD-binding domain, mitochondrial targeting, and overall size provide concrete biological reasoning that eliminates the kinase (B), hydrolase (C), and small DHFR (A) options, leaving the quinone oxidoreductase (D) as the only consistent choice. The argument is based on general protein domain biology rather than memorization of a specific database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span three different EC classes (oxidoreductases, transferases, hydrolases). The sequence's NAD(P)H-binding and FAD-binding motifs, mitochondrial targeting, and 413-aa size clearly eliminate B (kinase), C (hydrolase), and A (small DHFR without FAD domain). Only D is consistent with the observed architecture."
  },
  "important_caveats": [
    "The UniProt annotation for EC 1.6.5.2 on Q8IPZ3 is primarily by similarity (ECO:0000250 to Q8WWV3, the human ortholog), though a 2024 experimental paper supports the oxidoreductase function.",
    "The specific 4-digit EC assignment (1.6.5.2 vs. other EC 1.x.x.x) relies on knowledge that mitochondrial FAD/NAD(P)H oxidoreductases of this domain architecture reduce quinones; this is general biochemistry but the exact 4th digit (1.6.5.2) is a database annotation.",
    "The identity of the protein (Q8IPZ3, RTN4IP1) was inferred by the reviewer from metadata not provided to the model; the model must work from the sequence alone.",
    "The annotation was first integrated into Swiss-Prot in April 2025; the benchmark author's source snapshot date is unknown."
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

**Accession:** `Q8IPZ3` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 178. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IPZ3.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:18.576763+00:00.  

```json
"Q8IPZ3"
```

Source SHA-256: `e86069a21d68baee355342320a6ffe2ad016abdc8d4f641d55cad548579f2ea3`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IPZ3.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:18.576763+00:00.  

```json
{"alternativeNames":[{"fullName":{"value":"Reticulon-4-interacting protein 1 homolog"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"37884807","source":"PubMed"}],"value":"dRtn4ip1"}]}],"flag":"Precursor","recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q8WWV3","source":"UniProtKB"}],"value":"1.6.5.2"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"NAD(P)H oxidoreductase RTN4IP1, mitochondrial"}}}
```

Source SHA-256: `e86069a21d68baee355342320a6ffe2ad016abdc8d4f641d55cad548579f2ea3`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IPZ3.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:18.576763+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"1.6.5.2","evidences":[{"evidenceCode":"ECO:0000250","id":"Q8WWV3","source":"UniProtKB"}],"name":"a quinone + NADH + H(+) = a quinol + NAD(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:46160"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:24646"},{"database":"ChEBI","id":"CHEBI:57540"},{"database":"ChEBI","id":"CHEBI:57945"},{"database":"ChEBI","id":"CHEBI:132124"}]}}
```

Source SHA-256: `e86069a21d68baee355342320a6ffe2ad016abdc8d4f641d55cad548579f2ea3`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IPZ3.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:18.576763+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"1.6.5.2","evidences":[{"evidenceCode":"ECO:0000250","id":"Q8WWV3","source":"UniProtKB"}],"name":"a quinone + NADPH + H(+) = a quinol + NADP(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:46164"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:24646"},{"database":"ChEBI","id":"CHEBI:57783"},{"database":"ChEBI","id":"CHEBI:58349"},{"database":"ChEBI","id":"CHEBI:132124"}]}}
```

Source SHA-256: `e86069a21d68baee355342320a6ffe2ad016abdc8d4f641d55cad548579f2ea3`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IPZ3.json)  
**Locator:** `/references/4`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:18.576763+00:00.  

```json
{"citation":{"authors":["Park I.","Kim K.E.","Kim J.","Kim A.K.","Bae S.","Jung M.","Choi J.","Mishra P.K.","Kim T.M.","Kwak C.","Kang M.G.","Yoo C.M.","Mun J.Y.","Liu K.H.","Lee K.S.","Kim J.S.","Suh J.M.","Rhee H.W."],"citationCrossReferences":[{"database":"PubMed","id":"37884807"},{"database":"DOI","id":"10.1038/s41589-023-01452-w"}],"citationType":"journal article","firstPage":"221","id":"37884807","journal":"Nat. Chem. Biol.","lastPage":"233","publicationDate":"2024","title":"Mitochondrial matrix RTN4IP1/OPA10 is an oxidoreductase for coenzyme Q synthesis.","volume":"20"},"referenceNumber":5,"referencePositions":["FUNCTION","PATHWAY","DISRUPTION PHENOTYPE"]}
```

Source SHA-256: `e86069a21d68baee355342320a6ffe2ad016abdc8d4f641d55cad548579f2ea3`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IPZ3?format=txt&versions=178)  
**Locator:** `lines 6-10`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 178 / 1.  
**Retrieved:** 2026-11-02T04:32:22.972608+00:00.  

```text
DE   RecName: Full=NAD(P)H oxidoreductase RTN4IP1, mitochondrial {ECO:0000305};
DE            EC=1.6.5.2 {ECO:0000250|UniProtKB:Q8WWV3};
DE   AltName: Full=Reticulon-4-interacting protein 1 homolog;
DE            Short=dRtn4ip1 {ECO:0000303|PubMed:37884807};
DE   Flags: Precursor;
```

Source SHA-256: `c2044f60ca3ef3b11b8d9eda94d95aa716930f1e71581317ce51caed3192aef1`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IPZ3?format=txt&versions=178)  
**Locator:** `lines 85-93`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 178 / 1.  
**Retrieved:** 2026-11-02T04:32:22.972608+00:00.  

```text
RN   [5]
RP   FUNCTION, PATHWAY, AND DISRUPTION PHENOTYPE.
RX   PubMed=37884807; DOI=10.1038/s41589-023-01452-w;
RA   Park I., Kim K.E., Kim J., Kim A.K., Bae S., Jung M., Choi J., Mishra P.K.,
RA   Kim T.M., Kwak C., Kang M.G., Yoo C.M., Mun J.Y., Liu K.H., Lee K.S.,
RA   Kim J.S., Suh J.M., Rhee H.W.;
RT   "Mitochondrial matrix RTN4IP1/OPA10 is an oxidoreductase for coenzyme Q
RT   synthesis.";
RL   Nat. Chem. Biol. 20:221-233(2024).
```

Source SHA-256: `c2044f60ca3ef3b11b8d9eda94d95aa716930f1e71581317ce51caed3192aef1`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IPZ3?format=txt&versions=178)  
**Locator:** `lines 97-101`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 178 / 1.  
**Retrieved:** 2026-11-02T04:32:22.972608+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=a quinone + NADH + H(+) = a quinol + NAD(+);
CC         Xref=Rhea:RHEA:46160, ChEBI:CHEBI:15378, ChEBI:CHEBI:24646,
CC         ChEBI:CHEBI:57540, ChEBI:CHEBI:57945, ChEBI:CHEBI:132124; EC=1.6.5.2;
CC         Evidence={ECO:0000250|UniProtKB:Q8WWV3};
```

Source SHA-256: `c2044f60ca3ef3b11b8d9eda94d95aa716930f1e71581317ce51caed3192aef1`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IPZ3?format=txt&versions=178)  
**Locator:** `lines 102-106`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 178 / 1.  
**Retrieved:** 2026-11-02T04:32:22.972608+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=a quinone + NADPH + H(+) = a quinol + NADP(+);
CC         Xref=Rhea:RHEA:46164, ChEBI:CHEBI:15378, ChEBI:CHEBI:24646,
CC         ChEBI:CHEBI:57783, ChEBI:CHEBI:58349, ChEBI:CHEBI:132124; EC=1.6.5.2;
CC         Evidence={ECO:0000250|UniProtKB:Q8WWV3};
```

Source SHA-256: `c2044f60ca3ef3b11b8d9eda94d95aa716930f1e71581317ce51caed3192aef1`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 26. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
