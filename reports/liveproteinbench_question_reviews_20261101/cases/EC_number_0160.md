# EC_number_0160

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `EC_number`  
**Author expected answer:** **B** — 1.1.1.136

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MEKEKGEEKMNDSRKITVIGLGYVGLPLAIHFAERGYNVVGLDKDKRKIERIEKGDSYIPDVSSNVLKDLVQNKQLVVYTPHTGIEEFQNSEYVIVTVPTPINKQKEPDLSALIAASHYIKQNLQAGQTFIFESSTYPGTLEEVIIPIIAQSGKEVGKDYYIGYSPERIDPANQQYTVQTIPKVISGQTERCKQQVQKLYSTIFDTVVPVSSPKVAEMCKLFENIQRLVNISLVNELNILCEKLGIDFREALEAAATKPFGFTPYWPGPGIGGHCIPVDPLYFQWKARQLGQSSQLIEVAHMINEKMPQQIVTQVKELSAPPGTVFLIGIAYKKDVNDLRESPALPIIELLVNEGYKVQYHDPYISSAKIGDKIYDSIPLKKKTLEKADCILIVTDHSNIDWNICKGMKHVIDTRGVLKKVSA

[Multiple Choices]
A. 1.1.1.122
B. 1.1.1.136
C. 1.2.1.101
D. 2.1.1.395
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

> The supplied sequence exactly matches the 423-aa UniProt entry for this protein. That entry assigns EC 1.1.1.136 and records the catalytic activity with experimental evidence (ECO:0000269) linked to PubMed 20529859, supporting choice B.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> Sequence features may suggest a dehydrogenase, which is consistent with the 1.1.1 choices, but they do not establish which substrate-specific EC number applies.


**Missing item-specific fact**

> The protein's experimentally determined substrate and catalytic reaction—UDP-N-acetyl-D-glucosamine 6-dehydrogenation—are not supplied in the question.


**Reason**

> Distinguishing among the candidate dehydrogenase EC numbers requires protein-specific functional annotation or experimental knowledge absent from the sequence-and-choices input; recognizing the sequence or recalling its database entry would be lookup or memorization.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The choices specify distinct EC classifications, and the matched protein's supported classification is 1.1.1.136. The lack of enough input to infer it is an answerability limitation, not evidence that multiple options are correct.


### Important caveats

- The functional evidence is reported in UniProt with an experimental evidence code and a literature reference; the primary paper was not independently retrieved here.
- The exact sequence match and database identity are reviewer-only evidence, not information supplied to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Sequence features may suggest a dehydrogenase, which is consistent with the 1.1.1 choices, but they do not establish which substrate-specific EC number applies.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein's experimentally determined substrate and catalytic reaction—UDP-N-acetyl-D-glucosamine 6-dehydrogenation—are not supplied in the question.",
    "reason": "Distinguishing among the candidate dehydrogenase EC numbers requires protein-specific functional annotation or experimental knowledge absent from the sequence-and-choices input; recognizing the sequence or recalling its database entry would be lookup or memorization."
  },
  "case_id": "EC_number_0160",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the 423-aa UniProt entry for this protein. That entry assigns EC 1.1.1.136 and records the catalytic activity with experimental evidence (ECO:0000269) linked to PubMed 20529859, supporting choice B."
  },
  "important_caveats": [
    "The functional evidence is reported in UniProt with an experimental evidence code and a literature reference; the primary paper was not independently retrieved here.",
    "The exact sequence match and database identity are reviewer-only evidence, not information supplied to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The choices specify distinct EC classifications, and the matched protein's supported classification is 1.1.1.136. The lack of enough input to infer it is an answerability limitation, not evidence that multiple options are correct."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0160",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the 423-aa UniProt entry for this protein. That entry assigns EC 1.1.1.136 and records the catalytic activity with experimental evidence (ECO:0000269) linked to PubMed 20529859, supporting choice B.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "Sequence features may suggest a dehydrogenase, which is consistent with the 1.1.1 choices, but they do not establish which substrate-specific EC number applies.",
    "missing_item_specific_fact": "The protein's experimentally determined substrate and catalytic reaction—UDP-N-acetyl-D-glucosamine 6-dehydrogenation—are not supplied in the question.",
    "reason": "Distinguishing among the candidate dehydrogenase EC numbers requires protein-specific functional annotation or experimental knowledge absent from the sequence-and-choices input; recognizing the sequence or recalling its database entry would be lookup or memorization."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The choices specify distinct EC classifications, and the matched protein's supported classification is 1.1.1.136. The lack of enough input to infer it is an answerability limitation, not evidence that multiple options are correct."
  },
  "important_caveats": [
    "The functional evidence is reported in UniProt with an experimental evidence code and a literature reference; the primary paper was not independently retrieved here.",
    "The exact sequence match and database identity are reviewer-only evidence, not information supplied to the evaluated model."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry A7GKX6 (sequence exactly matches the benchmark, 423 aa) annotates this protein as UDP-N-acetyl-D-glucosamine 6-dehydrogenase with EC 1.1.1.136, supported by experimental evidence (ECO:0000269, PubMed:20529859, J. Biol. Chem. 285:24825-24833, 2010). The catalytic reaction (UDP-GlcNAc + 2 NAD+ + H2O → UDP-2-acetamido-2-deoxy-α-D-glucuronate + 2 NADH + 3 H+) is confirmed. The sequence match is exact (SHA256 identical).

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The Rossmann-fold motif 'IGLGYVGLPLAIH' (GxGxxG-like) at the N-terminus is consistent with an NAD+-dependent dehydrogenase acting on a CH-OH group (EC 1.1.1.x), which provides partial reasoning support for eliminating option C (1.2.1.101, aldehyde dehydrogenase, different mechanism) and option D (2.1.1.395, methyltransferase, entirely different EC class). However, the critical distinction between option A (1.1.1.122, UDP-glucose 6-dehydrogenase) and option B (1.1.1.136, UDP-N-acetyl-D-glucosamine 6-dehydrogenase) hinges on whether the active site specifically accommodates the N-acetyl group at C2 of the sugar. Both are closely related SDR-type NAD-dependent dehydrogenases oxidizing the C6-OH of a UDP-sugar; the substrate-specificity residues that discriminate UDP-Glc from UDP-GlcNAc are protein-specific and cannot be reliably inferred from the linear sequence alone without structural or experimental knowledge.


**Missing item-specific fact**

> The precise active-site residues and substrate-binding geometry that distinguish UDP-Glc 6-dehydrogenase (1.1.1.122) from UDP-GlcNAc 6-dehydrogenase (1.1.1.136) for this particular protein. This requires knowledge of the specific enzyme's substrate specificity determined experimentally (PubMed:20529859) or by memorizing the database annotation for this sequence.


**Reason**

> While general fold recognition (Rossmann motif) can narrow the answer to 1.1.1.x, the final discrimination between the two 1.1.1.x options requires a protein-specific experimental fact about substrate specificity that is not derivable from the sequence through general biological reasoning.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "B"
]
```

> Options A (1.1.1.122) and B (1.1.1.136) are both NAD+-dependent dehydrogenases acting on the C6-OH of a UDP-sugar via a Rossmann-fold mechanism. From sequence alone, without specific active-site structural knowledge, a knowledgeable model could reasonably assign either UDP-Glc 6-DH or UDP-GlcNAc 6-DH. Options C and D are more clearly eliminable based on EC class (aldehyde dehydrogenase vs. methyltransferase).


### Important caveats

- The UniProt annotation carries experimental evidence (ECO:0000269) from a 2010 J. Biol. Chem. study, lending strong support to EC 1.1.1.136 for this specific sequence.
- The sequence-to-accession identity (A7GKX6) was inferred by the reviewer from dataset metadata; the evaluated model had no access to this identifier.
- The entry was first publicly released in Swiss-Prot on 2025-02-05, so it was not in older training corpora, reducing the likelihood of memorization from pre-2025 data.
- The Rossmann-fold reasoning for eliminating C and D is sound but does not resolve the A-vs-B distinction.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The Rossmann-fold motif 'IGLGYVGLPLAIH' (GxGxxG-like) at the N-terminus is consistent with an NAD+-dependent dehydrogenase acting on a CH-OH group (EC 1.1.1.x), which provides partial reasoning support for eliminating option C (1.2.1.101, aldehyde dehydrogenase, different mechanism) and option D (2.1.1.395, methyltransferase, entirely different EC class). However, the critical distinction between option A (1.1.1.122, UDP-glucose 6-dehydrogenase) and option B (1.1.1.136, UDP-N-acetyl-D-glucosamine 6-dehydrogenase) hinges on whether the active site specifically accommodates the N-acetyl group at C2 of the sugar. Both are closely related SDR-type NAD-dependent dehydrogenases oxidizing the C6-OH of a UDP-sugar; the substrate-specificity residues that discriminate UDP-Glc from UDP-GlcNAc are protein-specific and cannot be reliably inferred from the linear sequence alone without structural or experimental knowledge.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The precise active-site residues and substrate-binding geometry that distinguish UDP-Glc 6-dehydrogenase (1.1.1.122) from UDP-GlcNAc 6-dehydrogenase (1.1.1.136) for this particular protein. This requires knowledge of the specific enzyme's substrate specificity determined experimentally (PubMed:20529859) or by memorizing the database annotation for this sequence.",
    "reason": "While general fold recognition (Rossmann motif) can narrow the answer to 1.1.1.x, the final discrimination between the two 1.1.1.x options requires a protein-specific experimental fact about substrate specificity that is not derivable from the sequence through general biological reasoning."
  },
  "case_id": "EC_number_0160",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "UniProt entry A7GKX6 (sequence exactly matches the benchmark, 423 aa) annotates this protein as UDP-N-acetyl-D-glucosamine 6-dehydrogenase with EC 1.1.1.136, supported by experimental evidence (ECO:0000269, PubMed:20529859, J. Biol. Chem. 285:24825-24833, 2010). The catalytic reaction (UDP-GlcNAc + 2 NAD+ + H2O → UDP-2-acetamido-2-deoxy-α-D-glucuronate + 2 NADH + 3 H+) is confirmed. The sequence match is exact (SHA256 identical)."
  },
  "important_caveats": [
    "The UniProt annotation carries experimental evidence (ECO:0000269) from a 2010 J. Biol. Chem. study, lending strong support to EC 1.1.1.136 for this specific sequence.",
    "The sequence-to-accession identity (A7GKX6) was inferred by the reviewer from dataset metadata; the evaluated model had no access to this identifier.",
    "The entry was first publicly released in Swiss-Prot on 2025-02-05, so it was not in older training corpora, reducing the likelihood of memorization from pre-2025 data.",
    "The Rossmann-fold reasoning for eliminating C and D is sound but does not resolve the A-vs-B distinction."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "B"
    ],
    "reason": "Options A (1.1.1.122) and B (1.1.1.136) are both NAD+-dependent dehydrogenases acting on the C6-OH of a UDP-sugar via a Rossmann-fold mechanism. From sequence alone, without specific active-site structural knowledge, a knowledgeable model could reasonably assign either UDP-Glc 6-DH or UDP-GlcNAc 6-DH. Options C and D are more clearly eliminable based on EC class (aldehyde dehydrogenase vs. methyltransferase)."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0160",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry A7GKX6 (sequence exactly matches the benchmark, 423 aa) annotates this protein as UDP-N-acetyl-D-glucosamine 6-dehydrogenase with EC 1.1.1.136, supported by experimental evidence (ECO:0000269, PubMed:20529859, J. Biol. Chem. 285:24825-24833, 2010). The catalytic reaction (UDP-GlcNAc + 2 NAD+ + H2O → UDP-2-acetamido-2-deoxy-α-D-glucuronate + 2 NADH + 3 H+) is confirmed. The sequence match is exact (SHA256 identical).",
    "evidence_ids": ["C4", "C5", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The Rossmann-fold motif 'IGLGYVGLPLAIH' (GxGxxG-like) at the N-terminus is consistent with an NAD+-dependent dehydrogenase acting on a CH-OH group (EC 1.1.1.x), which provides partial reasoning support for eliminating option C (1.2.1.101, aldehyde dehydrogenase, different mechanism) and option D (2.1.1.395, methyltransferase, entirely different EC class). However, the critical distinction between option A (1.1.1.122, UDP-glucose 6-dehydrogenase) and option B (1.1.1.136, UDP-N-acetyl-D-glucosamine 6-dehydrogenase) hinges on whether the active site specifically accommodates the N-acetyl group at C2 of the sugar. Both are closely related SDR-type NAD-dependent dehydrogenases oxidizing the C6-OH of a UDP-sugar; the substrate-specificity residues that discriminate UDP-Glc from UDP-GlcNAc are protein-specific and cannot be reliably inferred from the linear sequence alone without structural or experimental knowledge.",
    "missing_item_specific_fact": "The precise active-site residues and substrate-binding geometry that distinguish UDP-Glc 6-dehydrogenase (1.1.1.122) from UDP-GlcNAc 6-dehydrogenase (1.1.1.136) for this particular protein. This requires knowledge of the specific enzyme's substrate specificity determined experimentally (PubMed:20529859) or by memorizing the database annotation for this sequence.",
    "reason": "While general fold recognition (Rossmann motif) can narrow the answer to 1.1.1.x, the final discrimination between the two 1.1.1.x options requires a protein-specific experimental fact about substrate specificity that is not derivable from the sequence through general biological reasoning."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "B"],
    "reason": "Options A (1.1.1.122) and B (1.1.1.136) are both NAD+-dependent dehydrogenases acting on the C6-OH of a UDP-sugar via a Rossmann-fold mechanism. From sequence alone, without specific active-site structural knowledge, a knowledgeable model could reasonably assign either UDP-Glc 6-DH or UDP-GlcNAc 6-DH. Options C and D are more clearly eliminable based on EC class (aldehyde dehydrogenase vs. methyltransferase)."
  },
  "important_caveats": [
    "The UniProt annotation carries experimental evidence (ECO:0000269) from a 2010 J. Biol. Chem. study, lending strong support to EC 1.1.1.136 for this specific sequence.",
    "The sequence-to-accession identity (A7GKX6) was inferred by the reviewer from dataset metadata; the evaluated model had no access to this identifier.",
    "The entry was first publicly released in Swiss-Prot on 2025-02-05, so it was not in older training corpora, reducing the likelihood of memorization from pre-2025 data.",
    "The Rossmann-fold reasoning for eliminating C and D is sound but does not resolve the A-vs-B distinction."
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

**Accession:** `A7GKX6` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 96. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A7GKX6.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:09.484643+00:00.  

```json
"A7GKX6"
```

Source SHA-256: `68eff0a78e5c0dadd87ed867729ca5fa907f1022d5a7d7c02ac69e250707cc4f`.

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A7GKX6.json)  
**Locator:** `/entryAudit`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:09.484643+00:00.  

```json
{"entryVersion":98,"firstPublicDate":"2025-02-05","lastAnnotationUpdateDate":"2026-09-02","lastSequenceUpdateDate":"2007-09-11","sequenceVersion":1}
```

Source SHA-256: `68eff0a78e5c0dadd87ed867729ca5fa907f1022d5a7d7c02ac69e250707cc4f`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A7GKX6.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:09.484643+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"20529859","source":"PubMed"}],"value":"1.1.1.136"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"20529859","source":"PubMed"}],"value":"UDP-N-acetyl-D-glucosamine 6-dehydrogenase"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"20529859","source":"PubMed"}],"value":"UDP-GlcNAc 6-dehydrogenase"}]}}
```

Source SHA-256: `68eff0a78e5c0dadd87ed867729ca5fa907f1022d5a7d7c02ac69e250707cc4f`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A7GKX6.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:09.484643+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000269","id":"20529859","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:13326"}}],"reaction":{"ecNumber":"1.1.1.136","evidences":[{"evidenceCode":"ECO:0000269","id":"20529859","source":"PubMed"}],"name":"UDP-N-acetyl-alpha-D-glucosamine + 2 NAD(+) + H2O = UDP-2-acetamido-2-deoxy-alpha-D-glucuronate + 2 NADH + 3 H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:13325"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:57540"},{"database":"ChEBI","id":"CHEBI:57705"},{"database":"ChEBI","id":"CHEBI:57945"},{"database":"ChEBI","id":"CHEBI:65040"}]}}
```

Source SHA-256: `68eff0a78e5c0dadd87ed867729ca5fa907f1022d5a7d7c02ac69e250707cc4f`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A7GKX6.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:09.484643+00:00.  

```json
{"citation":{"authors":["Gu X.","Glushka J.","Lee S.G.","Bar-Peled M."],"citationCrossReferences":[{"database":"PubMed","id":"20529859"},{"database":"DOI","id":"10.1074/jbc.m110.125872"}],"citationType":"journal article","firstPage":"24825","id":"20529859","journal":"J. Biol. Chem.","lastPage":"24833","publicationDate":"2010","title":"Biosynthesis of a new UDP-sugar, UDP-2-acetamido-2-deoxyxylose, in the human pathogen Bacillus cereus subspecies cytotoxis NVH 391-98.","volume":"285"},"evidences":[{"evidenceCode":"ECO:0000312","id":"ADE43879.1","source":"EMBL"}],"referenceComments":[{"type":"STRAIN","value":"DSM 22905 / CIP 110041 / 391-98 / NVH 391-98"}],"referenceNumber":2,"referencePositions":["NUCLEOTIDE SEQUENCE [GENOMIC DNA]","FUNCTION","CATALYTIC ACTIVITY"]}
```

Source SHA-256: `68eff0a78e5c0dadd87ed867729ca5fa907f1022d5a7d7c02ac69e250707cc4f`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A7GKX6?format=txt&versions=96)  
**Locator:** `lines 6-8`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 96 / 1.  
**Retrieved:** 2026-11-02T04:27:11.633421+00:00.  

```text
DE   RecName: Full=UDP-N-acetyl-D-glucosamine 6-dehydrogenase {ECO:0000303|PubMed:20529859};
DE            Short=UDP-GlcNAc 6-dehydrogenase {ECO:0000303|PubMed:20529859};
DE            EC=1.1.1.136 {ECO:0000269|PubMed:20529859};
```

Source SHA-256: `d8a31aa88fd823d2c4ea18977d36968e48e5c0bbc7cb1fe4c9e6ca7171435666`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A7GKX6?format=txt&versions=96)  
**Locator:** `lines 40-48`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 96 / 1.  
**Retrieved:** 2026-11-02T04:27:11.633421+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=UDP-N-acetyl-alpha-D-glucosamine + 2 NAD(+) + H2O = UDP-2-
CC         acetamido-2-deoxy-alpha-D-glucuronate + 2 NADH + 3 H(+);
CC         Xref=Rhea:RHEA:13325, ChEBI:CHEBI:15377, ChEBI:CHEBI:15378,
CC         ChEBI:CHEBI:57540, ChEBI:CHEBI:57705, ChEBI:CHEBI:57945,
CC         ChEBI:CHEBI:65040; EC=1.1.1.136;
CC         Evidence={ECO:0000269|PubMed:20529859};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:13326;
CC         Evidence={ECO:0000269|PubMed:20529859};
```

Source SHA-256: `d8a31aa88fd823d2c4ea18977d36968e48e5c0bbc7cb1fe4c9e6ca7171435666`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 160. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
