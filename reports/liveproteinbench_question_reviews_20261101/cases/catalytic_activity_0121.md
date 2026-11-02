# catalytic_activity_0121

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `catalytic_activity`  
**Author expected answer:** **C** — a quinone + NADH + H(+) = a quinol + NAD(+)

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
A. a cytidine in tRNA + acetyl-CoA + ATP + H2O = an N(4)-acetylcytidine in tRNA + ADP + phosphate + CoA + H(+)
B. (19E)-geissoschizine + NADPH + H(+) = (16R,19Z)-isositsirikine + NADP(+)
C. a quinone + NADH + H(+) = a quinol + NAD(+)
D. L-dopa + H(+) = dopamine + CO2
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Enzymatic Reaction Prediction, which is to identify the specific chemical reaction catalyzed by a given enzyme. This involves understanding the enzyme's function based on its amino acid sequence and then selecting the correct transformation of substrates into products from a list of possible reactions.. The inputs provided by the user for this task include:

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

> The exact sequence matches the UniProt entry for Drosophila RTN4IP1, which annotates the NADH-dependent quinone-to-quinol reaction given in choice C. The annotation is transferred from a homolog (ECO:0000250), so this supports the key but is not direct experimental confirmation for this sequence.

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence may be consistent with an enzyme, but the supplied input gives no specific functional context or decisive motif that identifies quinone reduction rather than the other listed reactions.


**Missing item-specific fact**

> The protein-specific identification and functional annotation of this sequence as RTN4IP1, including its quinone-reductase activity, are absent from the question.


**Reason**

> Selecting C requires knowing or externally identifying this protein's specific function; general sequence reasoning alone does not meaningfully distinguish the reaction.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the listed options, C is the reaction matching the sequence-specific annotation. The annotation also lists a related NADPH-dependent reaction, but that reaction is not another offered choice.


### Important caveats

- The UniProt catalytic-activity annotation cites evidence transferred from a homolog rather than direct evidence for this exact sequence.
- A recent cited study concerns RTN4IP1/OPA10 as an oxidoreductase in coenzyme Q synthesis, but the supplied excerpts do not independently establish the exact NADH reaction experimentally for this Drosophila protein.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence may be consistent with an enzyme, but the supplied input gives no specific functional context or decisive motif that identifies quinone reduction rather than the other listed reactions.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific identification and functional annotation of this sequence as RTN4IP1, including its quinone-reductase activity, are absent from the question.",
    "reason": "Selecting C requires knowing or externally identifying this protein's specific function; general sequence reasoning alone does not meaningfully distinguish the reaction."
  },
  "case_id": "catalytic_activity_0121",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry for Drosophila RTN4IP1, which annotates the NADH-dependent quinone-to-quinol reaction given in choice C. The annotation is transferred from a homolog (ECO:0000250), so this supports the key but is not direct experimental confirmation for this sequence."
  },
  "important_caveats": [
    "The UniProt catalytic-activity annotation cites evidence transferred from a homolog rather than direct evidence for this exact sequence.",
    "A recent cited study concerns RTN4IP1/OPA10 as an oxidoreductase in coenzyme Q synthesis, but the supplied excerpts do not independently establish the exact NADH reaction experimentally for this Drosophila protein."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed options, C is the reaction matching the sequence-specific annotation. The annotation also lists a related NADPH-dependent reaction, but that reaction is not another offered choice."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0121",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry for Drosophila RTN4IP1, which annotates the NADH-dependent quinone-to-quinol reaction given in choice C. The annotation is transferred from a homolog (ECO:0000250), so this supports the key but is not direct experimental confirmation for this sequence.",
    "evidence_ids": ["C1", "C5", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence may be consistent with an enzyme, but the supplied input gives no specific functional context or decisive motif that identifies quinone reduction rather than the other listed reactions.",
    "missing_item_specific_fact": "The protein-specific identification and functional annotation of this sequence as RTN4IP1, including its quinone-reductase activity, are absent from the question.",
    "reason": "Selecting C requires knowing or externally identifying this protein's specific function; general sequence reasoning alone does not meaningfully distinguish the reaction."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed options, C is the reaction matching the sequence-specific annotation. The annotation also lists a related NADPH-dependent reaction, but that reaction is not another offered choice."
  },
  "important_caveats": [
    "The UniProt catalytic-activity annotation cites evidence transferred from a homolog rather than direct evidence for this exact sequence.",
    "A recent cited study concerns RTN4IP1/OPA10 as an oxidoreductase in coenzyme Q synthesis, but the supplied excerpts do not independently establish the exact NADH reaction experimentally for this Drosophila protein."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The supplied sequence matches UniProt Q8IPZ3 (RT4I1_DROME, NAD(P)H oxidoreductase RTN4IP1, mitochondrial; EC 1.6.5.2). The UniProt catalytic activity annotation explicitly states 'a quinone + NADH + H(+) = a quinol + NAD(+)' (evidence C5/H4), matching Choice C verbatim. The annotation evidence code is ECO:0000250 (transferred by similarity from human ortholog Q8WWV3), but a 2024 Nat. Chem. Biol. paper (PubMed:37884807) provides experimental characterization of RTN4IP1/OPA10 as an oxidoreductase in coenzyme Q synthesis. A second catalytic activity with NADPH is also annotated (C6/H5), but Choice C's NADH reaction is the primary listed activity and matches the expected answer exactly.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C7](#evidence-c7), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 413-aa sequence contains an N-terminal mitochondrial targeting signal (basic residues) and a Rossmann-like nucleotide-binding motif (GSGGVGT region), identifying it as a small mitochondrial NAD(P)H-dependent oxidoreductase. This eliminates A (tRNA acetyltransferase; no acetyl-CoA/ATP-binding motifs, wrong enzyme class) and D (PLP-dependent decarboxylase; no PLP-binding motifs, wrong enzyme class). Between B (a flavin/heme-dependent monooxygenase acting on a specific alkaloid) and C (a simple two-electron quinone reductase), the absence of heme-binding Cys-Pro-Pro-Gly motifs, P450 signatures, or large FAD-dependent monooxygenase domains, combined with the small size and simple Rossmann fold architecture, is more consistent with a quinone reductase (EC 1.6.5.2) than with a monooxygenase (EC 1.14.x.x). Quinone reduction is a common function of small mitochondrial NAD(P)H oxidoreductases.


**Missing item-specific fact**

> The specific identification of 'quinone' (particularly coenzyme Q) as the substrate, as opposed to other possible two-electron acceptors, relies on knowledge of this protein family's role in coenzyme Q biosynthesis, which is not derivable from generic sequence motifs alone.


**Reason**

> General biological knowledge of enzyme classes, cofactor requirements, and structural motifs allows meaningful elimination of A and D, and structural reasoning (small size, Rossmann fold, absence of monooxygenase features) provides a defensible preference for C over B. The positive identification of 'quinone' as the specific acceptor is the weakest inferential link but is the most parsimonious assignment for a small mitochondrial NAD(P)H oxidoreductase lacking monooxygenase features.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Choices A (tRNA modification), B (specific alkaloid monooxygenation), and D (decarboxylation) are clearly distinct enzyme classes that do not match the observed sequence features. Choice B is the closest distractor but requires monooxygenase structural features absent from this sequence. Choice C is the only remaining option consistent with a small mitochondrial NAD(P)H oxidoreductase.


### Important caveats

- The UniProt annotation for this Drosophila protein is transferred by similarity (ECO:0000250) from the human ortholog Q8WWV3, not directly experimentally determined for the fly protein, though the 2024 Nat. Chem. Biol. paper provides experimental support for the oxidoreductase function.
- The positive identification of 'quinone' as the specific substrate is the least sequence-derivable aspect; the reasoning primarily works by elimination of incompatible enzyme classes.
- The reviewer-only evidence (UniProt accession, annotation) was not available to the evaluated model; the reasoning assessment considers only what a model could infer from the sequence and general biological knowledge.
- The 2024 experimental paper characterizes RTN4IP1/OPA10 in coenzyme Q synthesis, which is consistent with but broader than the generic 'quinone' description in the EC reaction.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 413-aa sequence contains an N-terminal mitochondrial targeting signal (basic residues) and a Rossmann-like nucleotide-binding motif (GSGGVGT region), identifying it as a small mitochondrial NAD(P)H-dependent oxidoreductase. This eliminates A (tRNA acetyltransferase; no acetyl-CoA/ATP-binding motifs, wrong enzyme class) and D (PLP-dependent decarboxylase; no PLP-binding motifs, wrong enzyme class). Between B (a flavin/heme-dependent monooxygenase acting on a specific alkaloid) and C (a simple two-electron quinone reductase), the absence of heme-binding Cys-Pro-Pro-Gly motifs, P450 signatures, or large FAD-dependent monooxygenase domains, combined with the small size and simple Rossmann fold architecture, is more consistent with a quinone reductase (EC 1.6.5.2) than with a monooxygenase (EC 1.14.x.x). Quinone reduction is a common function of small mitochondrial NAD(P)H oxidoreductases.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The specific identification of 'quinone' (particularly coenzyme Q) as the substrate, as opposed to other possible two-electron acceptors, relies on knowledge of this protein family's role in coenzyme Q biosynthesis, which is not derivable from generic sequence motifs alone.",
    "reason": "General biological knowledge of enzyme classes, cofactor requirements, and structural motifs allows meaningful elimination of A and D, and structural reasoning (small size, Rossmann fold, absence of monooxygenase features) provides a defensible preference for C over B. The positive identification of 'quinone' as the specific acceptor is the weakest inferential link but is the most parsimonious assignment for a small mitochondrial NAD(P)H oxidoreductase lacking monooxygenase features."
  },
  "case_id": "catalytic_activity_0121",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C7",
      "H2",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence matches UniProt Q8IPZ3 (RT4I1_DROME, NAD(P)H oxidoreductase RTN4IP1, mitochondrial; EC 1.6.5.2). The UniProt catalytic activity annotation explicitly states 'a quinone + NADH + H(+) = a quinol + NAD(+)' (evidence C5/H4), matching Choice C verbatim. The annotation evidence code is ECO:0000250 (transferred by similarity from human ortholog Q8WWV3), but a 2024 Nat. Chem. Biol. paper (PubMed:37884807) provides experimental characterization of RTN4IP1/OPA10 as an oxidoreductase in coenzyme Q synthesis. A second catalytic activity with NADPH is also annotated (C6/H5), but Choice C's NADH reaction is the primary listed activity and matches the expected answer exactly."
  },
  "important_caveats": [
    "The UniProt annotation for this Drosophila protein is transferred by similarity (ECO:0000250) from the human ortholog Q8WWV3, not directly experimentally determined for the fly protein, though the 2024 Nat. Chem. Biol. paper provides experimental support for the oxidoreductase function.",
    "The positive identification of 'quinone' as the specific substrate is the least sequence-derivable aspect; the reasoning primarily works by elimination of incompatible enzyme classes.",
    "The reviewer-only evidence (UniProt accession, annotation) was not available to the evaluated model; the reasoning assessment considers only what a model could infer from the sequence and general biological knowledge.",
    "The 2024 experimental paper characterizes RTN4IP1/OPA10 in coenzyme Q synthesis, which is consistent with but broader than the generic 'quinone' description in the EC reaction."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Choices A (tRNA modification), B (specific alkaloid monooxygenation), and D (decarboxylation) are clearly distinct enzyme classes that do not match the observed sequence features. Choice B is the closest distractor but requires monooxygenase structural features absent from this sequence. Choice C is the only remaining option consistent with a small mitochondrial NAD(P)H oxidoreductase."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0121",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence matches UniProt Q8IPZ3 (RT4I1_DROME, NAD(P)H oxidoreductase RTN4IP1, mitochondrial; EC 1.6.5.2). The UniProt catalytic activity annotation explicitly states 'a quinone + NADH + H(+) = a quinol + NAD(+)' (evidence C5/H4), matching Choice C verbatim. The annotation evidence code is ECO:0000250 (transferred by similarity from human ortholog Q8WWV3), but a 2024 Nat. Chem. Biol. paper (PubMed:37884807) provides experimental characterization of RTN4IP1/OPA10 as an oxidoreductase in coenzyme Q synthesis. A second catalytic activity with NADPH is also annotated (C6/H5), but Choice C's NADH reaction is the primary listed activity and matches the expected answer exactly.",
    "evidence_ids": ["C4", "C5", "C7", "H2", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 413-aa sequence contains an N-terminal mitochondrial targeting signal (basic residues) and a Rossmann-like nucleotide-binding motif (GSGGVGT region), identifying it as a small mitochondrial NAD(P)H-dependent oxidoreductase. This eliminates A (tRNA acetyltransferase; no acetyl-CoA/ATP-binding motifs, wrong enzyme class) and D (PLP-dependent decarboxylase; no PLP-binding motifs, wrong enzyme class). Between B (a flavin/heme-dependent monooxygenase acting on a specific alkaloid) and C (a simple two-electron quinone reductase), the absence of heme-binding Cys-Pro-Pro-Gly motifs, P450 signatures, or large FAD-dependent monooxygenase domains, combined with the small size and simple Rossmann fold architecture, is more consistent with a quinone reductase (EC 1.6.5.2) than with a monooxygenase (EC 1.14.x.x). Quinone reduction is a common function of small mitochondrial NAD(P)H oxidoreductases.",
    "missing_item_specific_fact": "The specific identification of 'quinone' (particularly coenzyme Q) as the substrate, as opposed to other possible two-electron acceptors, relies on knowledge of this protein family's role in coenzyme Q biosynthesis, which is not derivable from generic sequence motifs alone.",
    "reason": "General biological knowledge of enzyme classes, cofactor requirements, and structural motifs allows meaningful elimination of A and D, and structural reasoning (small size, Rossmann fold, absence of monooxygenase features) provides a defensible preference for C over B. The positive identification of 'quinone' as the specific acceptor is the weakest inferential link but is the most parsimonious assignment for a small mitochondrial NAD(P)H oxidoreductase lacking monooxygenase features."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Choices A (tRNA modification), B (specific alkaloid monooxygenation), and D (decarboxylation) are clearly distinct enzyme classes that do not match the observed sequence features. Choice B is the closest distractor but requires monooxygenase structural features absent from this sequence. Choice C is the only remaining option consistent with a small mitochondrial NAD(P)H oxidoreductase."
  },
  "important_caveats": [
    "The UniProt annotation for this Drosophila protein is transferred by similarity (ECO:0000250) from the human ortholog Q8WWV3, not directly experimentally determined for the fly protein, though the 2024 Nat. Chem. Biol. paper provides experimental support for the oxidoreductase function.",
    "The positive identification of 'quinone' as the specific substrate is the least sequence-derivable aspect; the reasoning primarily works by elimination of incompatible enzyme classes.",
    "The reviewer-only evidence (UniProt accession, annotation) was not available to the evaluated model; the reasoning assessment considers only what a model could infer from the sequence and general biological knowledge.",
    "The 2024 experimental paper characterizes RTN4IP1/OPA10 in coenzyme Q synthesis, which is consistent with but broader than the generic 'quinone' description in the EC reaction."
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

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 121. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
