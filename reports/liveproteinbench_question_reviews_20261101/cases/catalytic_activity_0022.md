# catalytic_activity_0022

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `catalytic_activity`  
**Author expected answer:** **A** — 17-O-acetylnorajmaline + H2O = norajmaline + acetate + H(+)

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MGFAARPFHIVFSLFVLAGATQALIICPFDSIYQFGDSISDTGNYIRILPNGPAAAAANFPYGITFPGIPTGRFSDGRLIVDFIARVLGLPLLNPYLQQNASFKNGVNFAVGGATALNSSVLAAAGVQIPDIYLIPLSTQLNWFQTYLRSNCSSPTECSKKVQNSLFLIGNIGNNDVNYALPYRTIQEIEAYVPSIAKAVANATREIIRLGGRRIIVPGTFPFGCLPRNLYLFPNGDKDDLGCLRRLNDLSIYFNNLFQQALNSLRIEFPQAVIIYADYYNAFRFLLRNARALGFTSTLQSCCGIGGPYNFDLNRLCGFPGVPVCRNPREYIQWDGFHYTEAAHRHIVQYLIPDILKELKCS

[Multiple Choices]
A. 17-O-acetylnorajmaline + H2O = norajmaline + acetate + H(+)
B. a 5'-end (5'-triphosphoguanosine)-adenylyl-adenylyl-cytidylyl-adenosine in mRNA + 2 S-adenosyl-L-methionine = a 5'-end (N(7)-methyl 5'-triphosphoguanosine)-(2'-O-methyladenylyl)-adenylyl-cytidylyl-adenosine in mRNA + 2 S-adenosyl-L-homocysteine + H(+)
C. 2',2'-dihydroxy-2-oxospirilloxanthin = 2,2'-dioxospirilloxanthin + H2O
D. L-aspartate + ATP = 4-phospho-L-aspartate + ADP
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

> The supplied sequence exactly matches the annotated 362-aa protein, and both historical and current UniProt records assign it the reaction in A with ECO:0000269 evidence linked to PubMed 38212296. This supports the key, though the primary study was not independently reviewed here.

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence and choices may suggest a hydrolase rather than an RNA methyltransferase or kinase, but they do not establish the enzyme’s specific substrate or distinguish hydrolysis of 17-O-acetylnorajmaline from other possible enzyme reactions.


**Missing item-specific fact**

> The protein-specific catalytic annotation or experimental finding that this enzyme hydrolyzes 17-O-acetylnorajmaline.


**Reason**

> Identifying the precise reaction requires a protein-specific substrate/function fact not supplied in the prompt; recognizing the exact sequence from an external record would be lookup or memorization, not reasoning from the provided input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The options describe distinct reactions, and the matched annotation supports A; the input alone, however, does not establish that specific reaction.


### Important caveats

- The sequence match is exact, but the author’s precise source snapshot is unknown.
- The cited evidence code indicates experimental evidence in the database record; the underlying primary paper was not independently validated here.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence and choices may suggest a hydrolase rather than an RNA methyltransferase or kinase, but they do not establish the enzyme’s specific substrate or distinguish hydrolysis of 17-O-acetylnorajmaline from other possible enzyme reactions.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific catalytic annotation or experimental finding that this enzyme hydrolyzes 17-O-acetylnorajmaline.",
    "reason": "Identifying the precise reaction requires a protein-specific substrate/function fact not supplied in the prompt; recognizing the exact sequence from an external record would be lookup or memorization, not reasoning from the provided input."
  },
  "case_id": "catalytic_activity_0022",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the annotated 362-aa protein, and both historical and current UniProt records assign it the reaction in A with ECO:0000269 evidence linked to PubMed 38212296. This supports the key, though the primary study was not independently reviewed here."
  },
  "important_caveats": [
    "The sequence match is exact, but the author’s precise source snapshot is unknown.",
    "The cited evidence code indicates experimental evidence in the database record; the underlying primary paper was not independently validated here."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The options describe distinct reactions, and the matched annotation supports A; the input alone, however, does not establish that specific reaction."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0022",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the annotated 362-aa protein, and both historical and current UniProt records assign it the reaction in A with ECO:0000269 evidence linked to PubMed 38212296. This supports the key, though the primary study was not independently reviewed here.",
    "evidence_ids": ["C1", "C5", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence and choices may suggest a hydrolase rather than an RNA methyltransferase or kinase, but they do not establish the enzyme’s specific substrate or distinguish hydrolysis of 17-O-acetylnorajmaline from other possible enzyme reactions.",
    "missing_item_specific_fact": "The protein-specific catalytic annotation or experimental finding that this enzyme hydrolyzes 17-O-acetylnorajmaline.",
    "reason": "Identifying the precise reaction requires a protein-specific substrate/function fact not supplied in the prompt; recognizing the exact sequence from an external record would be lookup or memorization, not reasoning from the provided input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The options describe distinct reactions, and the matched annotation supports A; the input alone, however, does not establish that specific reaction."
  },
  "important_caveats": [
    "The sequence match is exact, but the author’s precise source snapshot is unknown.",
    "The cited evidence code indicates experimental evidence in the database record; the underlying primary paper was not independently validated here."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry P0DXJ5 (sequence exactly matched, 362 AA) annotates EC 3.1.1.80 'Acetylajmalan esterase 2' (RsAAE2) from Rauvolfia serpentina. The catalytic activity '17-O-acetylnorajmaline + H2O = norajmaline + acetate + H(+)' is supported by experimental evidence (ECO:0000269, PubMed:38212296, Guo et al. Nat. Commun. 2024). The expected answer matches the annotated reaction verbatim.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C7](#evidence-c7), [H1](#evidence-h1), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The four choices represent distinct enzyme classes (esterase, methyltransferase, oxidoreductase, kinase), so elimination based on absence of characteristic motifs (SAM-binding for B, FAD/NAD Rossmann fold for C, glycine-rich kinase loop for D) provides partial narrowing. However, the sequence lacks a canonical GxSxG serine hydrolase motif and does not contain an unambiguous, generalizable esterase signature that would allow confident positive identification of the enzyme class from sequence alone. The specific substrate '17-O-acetylnorajmaline' is a highly specific alkaloid biosynthetic intermediate known only from the 2024 Rauvolfia serpentina ajmaline pathway characterization.


**Missing item-specific fact**

> Recognition that this 362-aa sequence corresponds to Acetylajmalan esterase 2 (RsAAE2) in the Rauvolfia serpentina ajmaline biosynthetic pathway, and that its experimentally characterized substrate is 17-O-acetylnorajmaline (not 17-O-acetylajmaline), requires either exact sequence-to-database matching or memorization of the 2024 Nat. Commun. pathway paper. No generalizable sequence motif in the provided input unambiguously identifies this as a norajmaline-specific esterase.


**Reason**

> While the widely divergent enzyme classes among the four choices allow some elimination-based reasoning, confidently identifying the correct answer as a specific esterase acting on 17-O-acetylnorajmaline requires item-specific knowledge of the Rauvolfia serpentina alkaloid biosynthetic pathway or exact sequence lookup. The sequence itself does not present a textbook esterase motif (e.g., GxSxG) that would allow a model to reason from general biochemistry to this precise catalytic activity.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four choices span four entirely different enzyme classes (esterase/hydrolysis, methyltransferase, oxidoreductase/dehydrogenation, kinase/phosphorylation). Only one (A) is a hydrolytic esterase reaction. No other choice is biochemically plausible for this sequence, so there is no genuine ambiguity among the options.


### Important caveats

- The UniProt entry P0DXJ5 was first public in June 2025, and the supporting publication is from 2024. The sequence and annotation are very recent, making prior memorization by a model less likely but also meaning the sequence is unlikely to appear in older training corpora.
- The sequence lacks a canonical GxSxG serine hydrolase motif, making positive identification as an esterase from sequence alone non-trivial even for domain experts.
- A second catalytic activity (17-O-acetylajmaline → ajmaline) is annotated by similarity (ECO:0000250) to Q3MKY2, but this is not among the choices, so it does not create ambiguity.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The four choices represent distinct enzyme classes (esterase, methyltransferase, oxidoreductase, kinase), so elimination based on absence of characteristic motifs (SAM-binding for B, FAD/NAD Rossmann fold for C, glycine-rich kinase loop for D) provides partial narrowing. However, the sequence lacks a canonical GxSxG serine hydrolase motif and does not contain an unambiguous, generalizable esterase signature that would allow confident positive identification of the enzyme class from sequence alone. The specific substrate '17-O-acetylnorajmaline' is a highly specific alkaloid biosynthetic intermediate known only from the 2024 Rauvolfia serpentina ajmaline pathway characterization.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "Recognition that this 362-aa sequence corresponds to Acetylajmalan esterase 2 (RsAAE2) in the Rauvolfia serpentina ajmaline biosynthetic pathway, and that its experimentally characterized substrate is 17-O-acetylnorajmaline (not 17-O-acetylajmaline), requires either exact sequence-to-database matching or memorization of the 2024 Nat. Commun. pathway paper. No generalizable sequence motif in the provided input unambiguously identifies this as a norajmaline-specific esterase.",
    "reason": "While the widely divergent enzyme classes among the four choices allow some elimination-based reasoning, confidently identifying the correct answer as a specific esterase acting on 17-O-acetylnorajmaline requires item-specific knowledge of the Rauvolfia serpentina alkaloid biosynthetic pathway or exact sequence lookup. The sequence itself does not present a textbook esterase motif (e.g., GxSxG) that would allow a model to reason from general biochemistry to this precise catalytic activity."
  },
  "case_id": "catalytic_activity_0022",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C7",
      "H1",
      "H4"
    ],
    "judgment": "supported",
    "reason": "UniProt entry P0DXJ5 (sequence exactly matched, 362 AA) annotates EC 3.1.1.80 'Acetylajmalan esterase 2' (RsAAE2) from Rauvolfia serpentina. The catalytic activity '17-O-acetylnorajmaline + H2O = norajmaline + acetate + H(+)' is supported by experimental evidence (ECO:0000269, PubMed:38212296, Guo et al. Nat. Commun. 2024). The expected answer matches the annotated reaction verbatim."
  },
  "important_caveats": [
    "The UniProt entry P0DXJ5 was first public in June 2025, and the supporting publication is from 2024. The sequence and annotation are very recent, making prior memorization by a model less likely but also meaning the sequence is unlikely to appear in older training corpora.",
    "The sequence lacks a canonical GxSxG serine hydrolase motif, making positive identification as an esterase from sequence alone non-trivial even for domain experts.",
    "A second catalytic activity (17-O-acetylajmaline → ajmaline) is annotated by similarity (ECO:0000250) to Q3MKY2, but this is not among the choices, so it does not create ambiguity."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices span four entirely different enzyme classes (esterase/hydrolysis, methyltransferase, oxidoreductase/dehydrogenation, kinase/phosphorylation). Only one (A) is a hydrolytic esterase reaction. No other choice is biochemically plausible for this sequence, so there is no genuine ambiguity among the options."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0022",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry P0DXJ5 (sequence exactly matched, 362 AA) annotates EC 3.1.1.80 'Acetylajmalan esterase 2' (RsAAE2) from Rauvolfia serpentina. The catalytic activity '17-O-acetylnorajmaline + H2O = norajmaline + acetate + H(+)' is supported by experimental evidence (ECO:0000269, PubMed:38212296, Guo et al. Nat. Commun. 2024). The expected answer matches the annotated reaction verbatim.",
    "evidence_ids": ["C1", "C4", "C5", "C7", "H1", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The four choices represent distinct enzyme classes (esterase, methyltransferase, oxidoreductase, kinase), so elimination based on absence of characteristic motifs (SAM-binding for B, FAD/NAD Rossmann fold for C, glycine-rich kinase loop for D) provides partial narrowing. However, the sequence lacks a canonical GxSxG serine hydrolase motif and does not contain an unambiguous, generalizable esterase signature that would allow confident positive identification of the enzyme class from sequence alone. The specific substrate '17-O-acetylnorajmaline' is a highly specific alkaloid biosynthetic intermediate known only from the 2024 Rauvolfia serpentina ajmaline pathway characterization.",
    "missing_item_specific_fact": "Recognition that this 362-aa sequence corresponds to Acetylajmalan esterase 2 (RsAAE2) in the Rauvolfia serpentina ajmaline biosynthetic pathway, and that its experimentally characterized substrate is 17-O-acetylnorajmaline (not 17-O-acetylajmaline), requires either exact sequence-to-database matching or memorization of the 2024 Nat. Commun. pathway paper. No generalizable sequence motif in the provided input unambiguously identifies this as a norajmaline-specific esterase.",
    "reason": "While the widely divergent enzyme classes among the four choices allow some elimination-based reasoning, confidently identifying the correct answer as a specific esterase acting on 17-O-acetylnorajmaline requires item-specific knowledge of the Rauvolfia serpentina alkaloid biosynthetic pathway or exact sequence lookup. The sequence itself does not present a textbook esterase motif (e.g., GxSxG) that would allow a model to reason from general biochemistry to this precise catalytic activity."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices span four entirely different enzyme classes (esterase/hydrolysis, methyltransferase, oxidoreductase/dehydrogenation, kinase/phosphorylation). Only one (A) is a hydrolytic esterase reaction. No other choice is biochemically plausible for this sequence, so there is no genuine ambiguity among the options."
  },
  "important_caveats": [
    "The UniProt entry P0DXJ5 was first public in June 2025, and the supporting publication is from 2024. The sequence and annotation are very recent, making prior memorization by a model less likely but also meaning the sequence is unlikely to appear in older training corpora.",
    "The sequence lacks a canonical GxSxG serine hydrolase motif, making positive identification as an esterase from sequence alone non-trivial even for domain experts.",
    "A second catalytic activity (17-O-acetylajmaline → ajmaline) is annotated by similarity (ECO:0000250) to Q3MKY2, but this is not among the choices, so it does not create ambiguity."
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

**Accession:** `P0DXJ5` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 2. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXJ5.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:33.413705+00:00.  

```json
"P0DXJ5"
```

Source SHA-256: `e74045ec75b84a761a8c28c824548a403267850c5218348997bbacf67e779d70`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXJ5.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:33.413705+00:00.  

```json
{"flag":"Precursor","recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"38212296","source":"PubMed"}],"value":"3.1.1.80"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"38212296","source":"PubMed"}],"value":"Acetylajmalan esterase 2"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"38212296","source":"PubMed"}],"value":"RsAAE2"}]}}
```

Source SHA-256: `e74045ec75b84a761a8c28c824548a403267850c5218348997bbacf67e779d70`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXJ5.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:33.413705+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000269","id":"38212296","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:23797"}}],"reaction":{"ecNumber":"3.1.1.80","evidences":[{"evidenceCode":"ECO:0000269","id":"38212296","source":"PubMed"}],"name":"17-O-acetylnorajmaline + H2O = norajmaline + acetate + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:23796"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:30089"},{"database":"ChEBI","id":"CHEBI:77618"},{"database":"ChEBI","id":"CHEBI:77725"}]}}
```

Source SHA-256: `e74045ec75b84a761a8c28c824548a403267850c5218348997bbacf67e779d70`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXJ5.json)  
**Locator:** `/references/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:33.413705+00:00.  

```json
{"citation":{"authors":["Guo J.","Gao D.","Lian J.","Qu Y."],"citationCrossReferences":[{"database":"PubMed","id":"38212296"},{"database":"DOI","id":"10.1038/s41467-024-44797-z"}],"citationType":"journal article","firstPage":"457","id":"38212296","journal":"Nat. Commun.","lastPage":"457","publicationDate":"2024","title":"De novo biosynthesis of antiarrhythmic alkaloid ajmaline.","volume":"15"},"referenceNumber":1,"referencePositions":["NUCLEOTIDE SEQUENCE [MRNA]","FUNCTION","CATALYTIC ACTIVITY","PATHWAY","TISSUE SPECIFICITY","BIOTECHNOLOGY"]}
```

Source SHA-256: `e74045ec75b84a761a8c28c824548a403267850c5218348997bbacf67e779d70`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXJ5?format=txt&versions=2)  
**Locator:** `lines 1-16`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 2 / 1.  
**Retrieved:** 2026-11-02T04:29:35.241829+00:00.  

```text
ID   AAE2_RAUSE              Reviewed;         362 AA.
AC   P0DXJ5;
DT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.
DT   18-JUN-2025, sequence version 1.
DT   28-JAN-2026, entry version 2.
DE   RecName: Full=Acetylajmalan esterase 2 {ECO:0000303|PubMed:38212296};
DE            Short=RsAAE2 {ECO:0000303|PubMed:38212296};
DE            EC=3.1.1.80 {ECO:0000269|PubMed:38212296};
DE   Flags: Precursor;
GN   Name=AAE2 {ECO:0000303|PubMed:38212296};
OS   Rauvolfia serpentina (Serpentine wood) (Ophioxylon serpentinum).
OC   Eukaryota; Viridiplantae; Streptophyta; Embryophyta; Tracheophyta;
OC   Spermatophyta; Magnoliopsida; eudicotyledons; Gunneridae; Pentapetalae;
OC   asterids; lamiids; Gentianales; Apocynaceae; Rauvolfioideae; Vinceae;
OC   Rauvolfiinae; Rauvolfia.
OX   NCBI_TaxID=4060;
```

Source SHA-256: `fd05ebf51e29b1b8ffb9eabf52681e84944476cb3e9a9d3ef689fd184b6b5e95`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXJ5?format=txt&versions=2)  
**Locator:** `lines 31-37`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 2 / 1.  
**Retrieved:** 2026-11-02T04:29:35.241829+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=17-O-acetylnorajmaline + H2O = norajmaline + acetate + H(+);
CC         Xref=Rhea:RHEA:23796, ChEBI:CHEBI:15377, ChEBI:CHEBI:15378,
CC         ChEBI:CHEBI:30089, ChEBI:CHEBI:77618, ChEBI:CHEBI:77725; EC=3.1.1.80;
CC         Evidence={ECO:0000269|PubMed:38212296};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:23797;
CC         Evidence={ECO:0000269|PubMed:38212296};
```

Source SHA-256: `fd05ebf51e29b1b8ffb9eabf52681e84944476cb3e9a9d3ef689fd184b6b5e95`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 22. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
