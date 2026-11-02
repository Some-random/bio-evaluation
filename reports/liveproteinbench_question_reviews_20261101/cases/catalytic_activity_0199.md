# catalytic_activity_0199

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `catalytic_activity`  
**Author expected answer:** **A** — L-lysyl-&#91;protein&#93; + 2-oxoglutarate + O2 = (3S)-3-hydroxy-L-lysyl-&#91;protein&#93; + succinate + CO2

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MSEVERALDVLLQEAEELCIGSSVVELDRIPTALEFCREFYSKNQPVVIRKALNWPAIGKWTPKYLIEALGDRSVDVAITPNGYADGLATQNGQEYFVLPLETKMKLSEVVRRLDDPTGAVHYIQKQNSNLSVDLPELAADLRVSDLDFAQQSFNKPPDAVNFWLGDERAVTSMHKDPYENVYCVISGHKDFVLIPPHQLSCVPRGIYPTGVYKTSDSGQFYIEPLRDEEGSDQFTEWVSVDPLSPDLAKYPEYARAKPLKVRVHAGDILYLPNYWFHHVSQSHKCIAVNFWYDLDYDSRYCYYRMLEQMTSARSG

[Multiple Choices]
A. L-lysyl-[protein] + 2-oxoglutarate + O2 = (3S)-3-hydroxy-L-lysyl-[protein] + succinate + CO2
B. D-glutamine + acetyl-CoA = N-acetyl-D-glutamine + CoA + H(+)
C. 4-nitrobenzoate + 2 NADH + 2 H(+) = 4-hydroxylaminobenzoate + 2 NAD(+) + H2O
D. S-ubiquitinyl-[E2 ubiquitin-conjugating enzyme]-L-cysteine + [acceptor protein]-L-lysine = [E2 ubiquitin-conjugating enzyme]-L-cysteine + N(6)-ubiquitinyl-[acceptor protein]-L-lysine.
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

> The supplied sequence exactly matches the 316-aa UniProt entry for Drosophila JMJD7. That entry assigns the lysyl hydroxylation reaction in A and cites ECO:0000269 evidence for it.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> Sequence features may support a broad 2-oxoglutarate-dependent oxygenase classification, which is consistent with A and unlike the other listed reaction classes. They do not establish the specific protein substrate or lysine-hydroxylation activity.


**Missing item-specific fact**

> The JMJD7-specific functional assignment that it hydroxylates protein-bound L-lysine to (3S)-3-hydroxy-L-lysine.


**Reason**

> The exact substrate and reaction require protein-specific functional knowledge absent from the input; a broad oxygenase-family inference does not by itself determine that specificity.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The options describe distinct reaction classes, and the matched-sequence annotation supports A.


### Important caveats

- The supporting UniProt annotation cites experimental evidence, but the cited primary study was not independently reviewed here.
- The reviewer-only accession and annotation were not supplied to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Sequence features may support a broad 2-oxoglutarate-dependent oxygenase classification, which is consistent with A and unlike the other listed reaction classes. They do not establish the specific protein substrate or lysine-hydroxylation activity.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The JMJD7-specific functional assignment that it hydroxylates protein-bound L-lysine to (3S)-3-hydroxy-L-lysine.",
    "reason": "The exact substrate and reaction require protein-specific functional knowledge absent from the input; a broad oxygenase-family inference does not by itself determine that specificity."
  },
  "case_id": "catalytic_activity_0199",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the 316-aa UniProt entry for Drosophila JMJD7. That entry assigns the lysyl hydroxylation reaction in A and cites ECO:0000269 evidence for it."
  },
  "important_caveats": [
    "The supporting UniProt annotation cites experimental evidence, but the cited primary study was not independently reviewed here.",
    "The reviewer-only accession and annotation were not supplied to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The options describe distinct reaction classes, and the matched-sequence annotation supports A."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0199",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the 316-aa UniProt entry for Drosophila JMJD7. That entry assigns the lysyl hydroxylation reaction in A and cites ECO:0000269 evidence for it.",
    "evidence_ids": ["C1", "C4", "C5", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "Sequence features may support a broad 2-oxoglutarate-dependent oxygenase classification, which is consistent with A and unlike the other listed reaction classes. They do not establish the specific protein substrate or lysine-hydroxylation activity.",
    "missing_item_specific_fact": "The JMJD7-specific functional assignment that it hydroxylates protein-bound L-lysine to (3S)-3-hydroxy-L-lysine.",
    "reason": "The exact substrate and reaction require protein-specific functional knowledge absent from the input; a broad oxygenase-family inference does not by itself determine that specificity."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The options describe distinct reaction classes, and the matched-sequence annotation supports A."
  },
  "important_caveats": [
    "The supporting UniProt annotation cites experimental evidence, but the cited primary study was not independently reviewed here.",
    "The reviewer-only accession and annotation were not supplied to the evaluated model."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The supplied sequence (316 AA, SHA256 match) corresponds to UniProt Q9VU77 (JMJD7_DROME). The UniProt entry explicitly annotates the catalytic activity as 'L-lysyl-&#91;protein&#93; + 2-oxoglutarate + O2 = (3S)-3-hydroxy-L-lysyl-&#91;protein&#93; + succinate + CO2' (EC 1.14.11.63), with experimental evidence (ECO:0000269, PubMed:35410347, X-ray crystallography of dimeric JmjC fold in complex with 2-oxoglutarate and succinate). The expected answer A is verbatim the annotated reaction.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a JmjC (Jumonji C) domain signature: the HxD/E motif (GHKD at ~residues 175-178) followed by a second conserved histidine (~50-100 residues downstream, e.g., in the VRVHAGD or WFHH regions). JmjC domains are the hallmark of Fe(II)/2-oxoglutarate-dependent dioxygenases. Among the four choices, only option A involves 2-oxoglutarate as a co-substrate and O2 as oxidant with succinate/CO2 as co-products—the defining chemistry of this enzyme class. Choices B (acetyltransferase), C (nitroreductase/oxidoreductase), and D (E3 ubiquitin ligase) involve entirely different catalytic mechanisms and cofactors that are inconsistent with a JmjC fold. Thus, recognizing the JmjC domain and its obligate 2-oxoglutarate dependence is sufficient to select A.


**Missing item-specific fact**

> None required beyond general knowledge of JmjC domain biochemistry. The specific substrate (L-lysyl vs. other residues) is not needed to discriminate among the four options since only one is a 2-oxoglutarate-dependent dioxygenase.


**Reason**

> A model with knowledge of the HxD/E...H motif and the 2-oxoglutarate dependence of JmjC dioxygenases can eliminate B, C, and D on mechanistic grounds. The discrimination relies on enzyme-class identification from sequence motifs, which is standard general biological reasoning, not a lookup of this specific protein's annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four choices span four distinct enzyme classes (2-oxoglutarate dioxygenase, acyltransferase, nitroreductase, ubiquitin ligase). The JmjC domain and 2-oxoglutarate chemistry uniquely match option A. The entry's secondary annotation (EC 3.4.-.- peptidase, transferred by similarity) does not correspond to any listed option, so no ambiguity arises.


### Important caveats

- The peptidase activity (EC 3.4.-.-) in the UniProt entry is transferred by similarity (ECO:0000250) and not experimentally confirmed for this Drosophila protein; it is irrelevant to the four options provided.
- The HxD/E...H motif recognition from raw sequence is a non-trivial pattern-matching task; not all models will reliably extract it, but the biological grounds for reasoning exist.
- The reviewer-only evidence confirms the annotation with experimental (X-ray crystallography) support, but this information was not available to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a JmjC (Jumonji C) domain signature: the HxD/E motif (GHKD at ~residues 175-178) followed by a second conserved histidine (~50-100 residues downstream, e.g., in the VRVHAGD or WFHH regions). JmjC domains are the hallmark of Fe(II)/2-oxoglutarate-dependent dioxygenases. Among the four choices, only option A involves 2-oxoglutarate as a co-substrate and O2 as oxidant with succinate/CO2 as co-products—the defining chemistry of this enzyme class. Choices B (acetyltransferase), C (nitroreductase/oxidoreductase), and D (E3 ubiquitin ligase) involve entirely different catalytic mechanisms and cofactors that are inconsistent with a JmjC fold. Thus, recognizing the JmjC domain and its obligate 2-oxoglutarate dependence is sufficient to select A.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None required beyond general knowledge of JmjC domain biochemistry. The specific substrate (L-lysyl vs. other residues) is not needed to discriminate among the four options since only one is a 2-oxoglutarate-dependent dioxygenase.",
    "reason": "A model with knowledge of the HxD/E...H motif and the 2-oxoglutarate dependence of JmjC dioxygenases can eliminate B, C, and D on mechanistic grounds. The discrimination relies on enzyme-class identification from sequence motifs, which is standard general biological reasoning, not a lookup of this specific protein's annotation."
  },
  "case_id": "catalytic_activity_0199",
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
    "reason": "The supplied sequence (316 AA, SHA256 match) corresponds to UniProt Q9VU77 (JMJD7_DROME). The UniProt entry explicitly annotates the catalytic activity as 'L-lysyl-[protein] + 2-oxoglutarate + O2 = (3S)-3-hydroxy-L-lysyl-[protein] + succinate + CO2' (EC 1.14.11.63), with experimental evidence (ECO:0000269, PubMed:35410347, X-ray crystallography of dimeric JmjC fold in complex with 2-oxoglutarate and succinate). The expected answer A is verbatim the annotated reaction."
  },
  "important_caveats": [
    "The peptidase activity (EC 3.4.-.-) in the UniProt entry is transferred by similarity (ECO:0000250) and not experimentally confirmed for this Drosophila protein; it is irrelevant to the four options provided.",
    "The HxD/E...H motif recognition from raw sequence is a non-trivial pattern-matching task; not all models will reliably extract it, but the biological grounds for reasoning exist.",
    "The reviewer-only evidence confirms the annotation with experimental (X-ray crystallography) support, but this information was not available to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices span four distinct enzyme classes (2-oxoglutarate dioxygenase, acyltransferase, nitroreductase, ubiquitin ligase). The JmjC domain and 2-oxoglutarate chemistry uniquely match option A. The entry's secondary annotation (EC 3.4.-.- peptidase, transferred by similarity) does not correspond to any listed option, so no ambiguity arises."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0199",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence (316 AA, SHA256 match) corresponds to UniProt Q9VU77 (JMJD7_DROME). The UniProt entry explicitly annotates the catalytic activity as 'L-lysyl-[protein] + 2-oxoglutarate + O2 = (3S)-3-hydroxy-L-lysyl-[protein] + succinate + CO2' (EC 1.14.11.63), with experimental evidence (ECO:0000269, PubMed:35410347, X-ray crystallography of dimeric JmjC fold in complex with 2-oxoglutarate and succinate). The expected answer A is verbatim the annotated reaction.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H1", "H2", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a JmjC (Jumonji C) domain signature: the HxD/E motif (GHKD at ~residues 175-178) followed by a second conserved histidine (~50-100 residues downstream, e.g., in the VRVHAGD or WFHH regions). JmjC domains are the hallmark of Fe(II)/2-oxoglutarate-dependent dioxygenases. Among the four choices, only option A involves 2-oxoglutarate as a co-substrate and O2 as oxidant with succinate/CO2 as co-products—the defining chemistry of this enzyme class. Choices B (acetyltransferase), C (nitroreductase/oxidoreductase), and D (E3 ubiquitin ligase) involve entirely different catalytic mechanisms and cofactors that are inconsistent with a JmjC fold. Thus, recognizing the JmjC domain and its obligate 2-oxoglutarate dependence is sufficient to select A.",
    "missing_item_specific_fact": "None required beyond general knowledge of JmjC domain biochemistry. The specific substrate (L-lysyl vs. other residues) is not needed to discriminate among the four options since only one is a 2-oxoglutarate-dependent dioxygenase.",
    "reason": "A model with knowledge of the HxD/E...H motif and the 2-oxoglutarate dependence of JmjC dioxygenases can eliminate B, C, and D on mechanistic grounds. The discrimination relies on enzyme-class identification from sequence motifs, which is standard general biological reasoning, not a lookup of this specific protein's annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices span four distinct enzyme classes (2-oxoglutarate dioxygenase, acyltransferase, nitroreductase, ubiquitin ligase). The JmjC domain and 2-oxoglutarate chemistry uniquely match option A. The entry's secondary annotation (EC 3.4.-.- peptidase, transferred by similarity) does not correspond to any listed option, so no ambiguity arises."
  },
  "important_caveats": [
    "The peptidase activity (EC 3.4.-.-) in the UniProt entry is transferred by similarity (ECO:0000250) and not experimentally confirmed for this Drosophila protein; it is irrelevant to the four options provided.",
    "The HxD/E...H motif recognition from raw sequence is a non-trivial pattern-matching task; not all models will reliably extract it, but the biological grounds for reasoning exist.",
    "The reviewer-only evidence confirms the annotation with experimental (X-ray crystallography) support, but this information was not available to the evaluated model."
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

**Accession:** `Q9VU77` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 176. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VU77.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:39.402140+00:00.  

```json
"Q9VU77"
```

Source SHA-256: `3f44f9cf8070a93f81c5ebea15797eae9345f5530025b2d6a02c1b0f107c3c0f`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VU77.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:39.402140+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000312","id":"FBgn0036366","source":"FlyBase"}],"value":"Jumonji domain containing protein 7"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"35410347","source":"PubMed"}],"value":"1.14.11.63"},{"evidences":[{"evidenceCode":"ECO:0000250","id":"P0C870","source":"UniProtKB"}],"value":"3.4.-.-"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000250","id":"P0C870","source":"UniProtKB"}],"value":"Bifunctional peptidase and (3S)-lysyl hydroxylase JMJD7"}}}
```

Source SHA-256: `3f44f9cf8070a93f81c5ebea15797eae9345f5530025b2d6a02c1b0f107c3c0f`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VU77.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:39.402140+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000269","id":"35410347","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:57153"}}],"reaction":{"ecNumber":"1.14.11.63","evidences":[{"evidenceCode":"ECO:0000269","id":"35410347","source":"PubMed"}],"name":"L-lysyl-[protein] + 2-oxoglutarate + O2 = (3S)-3-hydroxy-L-lysyl-[protein] + succinate + CO2","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:57152"},{"database":"Rhea","id":"RHEA-COMP:9752"},{"database":"Rhea","id":"RHEA-COMP:15133"},{"database":"ChEBI","id":"CHEBI:15379"},{"database":"ChEBI","id":"CHEBI:16526"},{"database":"ChEBI","id":"CHEBI:16810"},{"database":"ChEBI","id":"CHEBI:29969"},{"database":"ChEBI","id":"CHEBI:30031"},{"database":"ChEBI","id":"CHEBI:141492"}]}}
```

Source SHA-256: `3f44f9cf8070a93f81c5ebea15797eae9345f5530025b2d6a02c1b0f107c3c0f`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VU77.json)  
**Locator:** `/references/6`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:39.402140+00:00.  

```json
{"citation":{"authors":["Chowdhury R.","Abboud M.I.","Wiley J.","Tumber A.","Markolovic S.","Schofield C.J."],"citationCrossReferences":[{"database":"PubMed","id":"35410347"},{"database":"DOI","id":"10.1038/s41598-022-10028-y"}],"citationType":"journal article","firstPage":"6065","id":"35410347","journal":"Sci. Rep.","lastPage":"6065","publicationDate":"2022","title":"Conservation of the unusual dimeric JmjC fold of JMJD7 from Drosophila melanogaster to humans.","volume":"12"},"evidences":[{"evidenceCode":"ECO:0007744","id":"7YXG","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"7YXH","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"7YXI","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"7YXJ","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"7YXK","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"7YXL","source":"PDB"}],"referenceNumber":7,"referencePositions":["X-RAY CRYSTALLOGRAPHY (1.64 ANGSTROMS) IN COMPLEX WITH 2-OXOGLUTARATE; MN(2+); SUCCINATE; N-OXALYLGLYCINE; N-OXALYL-D-ALANINE; N-OXALYL-D-PHENYLALANINE AND LUTIDINIC ACID","FUNCTION","CATALYTIC ACTIVITY","COFACTOR","SUBUNIT","DISULFIDE BOND","OXIDATION AT CYS-19"]}
```

Source SHA-256: `3f44f9cf8070a93f81c5ebea15797eae9345f5530025b2d6a02c1b0f107c3c0f`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VU77?format=txt&versions=176)  
**Locator:** `lines 1-16`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 176 / 1.  
**Retrieved:** 2026-11-02T04:33:41.782034+00:00.  

```text
ID   JMJD7_DROME             Reviewed;         316 AA.
AC   Q9VU77;
DT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.
DT   01-MAY-2000, sequence version 1.
DT   28-JAN-2026, entry version 176.
DE   RecName: Full=Bifunctional peptidase and (3S)-lysyl hydroxylase JMJD7 {ECO:0000250|UniProtKB:P0C870};
DE            EC=1.14.11.63 {ECO:0000269|PubMed:35410347};
DE            EC=3.4.-.- {ECO:0000250|UniProtKB:P0C870};
DE   AltName: Full=Jumonji domain containing protein 7 {ECO:0000312|FlyBase:FBgn0036366};
GN   Name=JMJD7 {ECO:0000312|FlyBase:FBgn0036366};
GN   ORFNames=CG10133 {ECO:0000312|FlyBase:FBgn0036366};
OS   Drosophila melanogaster (Fruit fly).
OC   Eukaryota; Metazoa; Ecdysozoa; Arthropoda; Hexapoda; Insecta; Pterygota;
OC   Neoptera; Endopterygota; Diptera; Brachycera; Muscomorpha; Ephydroidea;
OC   Drosophilidae; Drosophila; Sophophora.
OX   NCBI_TaxID=7227 {ECO:0000312|Proteomes:UP000000803};
```

Source SHA-256: `a1c372e1e6cdfb62ebfb0d23f4b2ede050f6bcae06c776e1265b4e0ab02f3ff5`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VU77?format=txt&versions=176)  
**Locator:** `lines 6-9`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 176 / 1.  
**Retrieved:** 2026-11-02T04:33:41.782034+00:00.  

```text
DE   RecName: Full=Bifunctional peptidase and (3S)-lysyl hydroxylase JMJD7 {ECO:0000250|UniProtKB:P0C870};
DE            EC=1.14.11.63 {ECO:0000269|PubMed:35410347};
DE            EC=3.4.-.- {ECO:0000250|UniProtKB:P0C870};
DE   AltName: Full=Jumonji domain containing protein 7 {ECO:0000312|FlyBase:FBgn0036366};
```

Source SHA-256: `a1c372e1e6cdfb62ebfb0d23f4b2ede050f6bcae06c776e1265b4e0ab02f3ff5`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VU77?format=txt&versions=176)  
**Locator:** `lines 104-114`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 176 / 1.  
**Retrieved:** 2026-11-02T04:33:41.782034+00:00.  

```text
RN   [7] {ECO:0007744|PDB:7YXG, ECO:0007744|PDB:7YXH, ECO:0007744|PDB:7YXI, ECO:0007744|PDB:7YXJ, ECO:0007744|PDB:7YXK, ECO:0007744|PDB:7YXL}
RP   X-RAY CRYSTALLOGRAPHY (1.64 ANGSTROMS) IN COMPLEX WITH 2-OXOGLUTARATE;
RP   MN(2+); SUCCINATE; N-OXALYLGLYCINE; N-OXALYL-D-ALANINE;
RP   N-OXALYL-D-PHENYLALANINE AND LUTIDINIC ACID, FUNCTION, CATALYTIC ACTIVITY,
RP   COFACTOR, SUBUNIT, DISULFIDE BOND, AND OXIDATION AT CYS-19.
RX   PubMed=35410347; DOI=10.1038/s41598-022-10028-y;
RA   Chowdhury R., Abboud M.I., Wiley J., Tumber A., Markolovic S.,
RA   Schofield C.J.;
RT   "Conservation of the unusual dimeric JmjC fold of JMJD7 from Drosophila
RT   melanogaster to humans.";
RL   Sci. Rep. 12:6065-6065(2022).
```

Source SHA-256: `a1c372e1e6cdfb62ebfb0d23f4b2ede050f6bcae06c776e1265b4e0ab02f3ff5`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VU77?format=txt&versions=176)  
**Locator:** `lines 124-132`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 176 / 1.  
**Retrieved:** 2026-11-02T04:33:41.782034+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=L-lysyl-[protein] + 2-oxoglutarate + O2 = (3S)-3-hydroxy-L-
CC         lysyl-[protein] + succinate + CO2; Xref=Rhea:RHEA:57152, Rhea:RHEA-
CC         COMP:9752, Rhea:RHEA-COMP:15133, ChEBI:CHEBI:15379,
CC         ChEBI:CHEBI:16526, ChEBI:CHEBI:16810, ChEBI:CHEBI:29969,
CC         ChEBI:CHEBI:30031, ChEBI:CHEBI:141492; EC=1.14.11.63;
CC         Evidence={ECO:0000269|PubMed:35410347};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:57153;
CC         Evidence={ECO:0000269|PubMed:35410347};
```

Source SHA-256: `a1c372e1e6cdfb62ebfb0d23f4b2ede050f6bcae06c776e1265b4e0ab02f3ff5`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 199. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
