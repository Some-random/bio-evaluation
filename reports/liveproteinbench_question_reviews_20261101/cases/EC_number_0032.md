# EC_number_0032

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `EC_number`  
**Author expected answer:** **D** — 4.2.1.18

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MPPVSRILSYAPRVAIRPSSQLARPARAFAVGTVRYYSAEQPEEPLIRVTDLPAPNSGHIRVLELNRPKARNAISRALLASLREEVHSIARQYDAQTGEEIPTPSWNKRFGGIAGDSEKGPTRALVLASAVESSFCAGADLKERRGFTQEETNEFLANLRSTFAALDALPIPTISAISSRALGGGLELALCTHFRVLTSNAIVSLPETRLGIIPGAGGTHRLPRLIGLGRARDMIVTGRAVSGAEAYFLGLADRLVEVLPPDEQEAADTTDKDAALLSAAREAALTEAVRLASQICEGGPIGIRAALQAVQAPSQETENKMYERVIGTEDRNEALKAFAEKRKPVFKGR

[Multiple Choices]
A. 4.2.1.70
B. 5.6.2.4
C. 1.14.15.9
D. 4.2.1.18
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

> The supplied sequence exactly matches the UniProt entry annotated as methylglutaconyl-CoA hydratase with EC 4.2.1.18; the entry also specifies the corresponding catalytic reaction. This supports choice D. The cited evidence code is a curator inference from a publication, not by itself proof of a direct experimental assay.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence could support identifying an enzyme family, but the input gives no reaction, organism, or other functional context that distinguishes the specific EC assignment from the other candidate hydratases.


**Missing item-specific fact**

> The sequence-specific functional annotation identifying this protein as methylglutaconyl-CoA hydratase and assigning EC 4.2.1.18.


**Reason**

> Selecting the exact four-digit EC requires protein-specific functional information not supplied in the question. Recognizing or retrieving the matching database entry would be lookup or memorization, not reasoning from the supplied input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The reviewer evidence supports D for the exact sequence; no other listed EC is supported by the supplied evidence.


### Important caveats

- The sequence match and functional annotation are reviewer-only evidence and were not available to the evaluated model.
- The annotation cites a publication but uses ECO:0000305; the excerpts do not independently establish that the EC assignment came from a direct experimental assay.
- The historical record matches the sequence, but the author's exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence could support identifying an enzyme family, but the input gives no reaction, organism, or other functional context that distinguishes the specific EC assignment from the other candidate hydratases.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The sequence-specific functional annotation identifying this protein as methylglutaconyl-CoA hydratase and assigning EC 4.2.1.18.",
    "reason": "Selecting the exact four-digit EC requires protein-specific functional information not supplied in the question. Recognizing or retrieving the matching database entry would be lookup or memorization, not reasoning from the supplied input."
  },
  "case_id": "EC_number_0032",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the UniProt entry annotated as methylglutaconyl-CoA hydratase with EC 4.2.1.18; the entry also specifies the corresponding catalytic reaction. This supports choice D. The cited evidence code is a curator inference from a publication, not by itself proof of a direct experimental assay."
  },
  "important_caveats": [
    "The sequence match and functional annotation are reviewer-only evidence and were not available to the evaluated model.",
    "The annotation cites a publication but uses ECO:0000305; the excerpts do not independently establish that the EC assignment came from a direct experimental assay.",
    "The historical record matches the sequence, but the author's exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The reviewer evidence supports D for the exact sequence; no other listed EC is supported by the supplied evidence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0032",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the UniProt entry annotated as methylglutaconyl-CoA hydratase with EC 4.2.1.18; the entry also specifies the corresponding catalytic reaction. This supports choice D. The cited evidence code is a curator inference from a publication, not by itself proof of a direct experimental assay.",
    "evidence_ids": ["C1", "C4", "C5", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence could support identifying an enzyme family, but the input gives no reaction, organism, or other functional context that distinguishes the specific EC assignment from the other candidate hydratases.",
    "missing_item_specific_fact": "The sequence-specific functional annotation identifying this protein as methylglutaconyl-CoA hydratase and assigning EC 4.2.1.18.",
    "reason": "Selecting the exact four-digit EC requires protein-specific functional information not supplied in the question. Recognizing or retrieving the matching database entry would be lookup or memorization, not reasoning from the supplied input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The reviewer evidence supports D for the exact sequence; no other listed EC is supported by the supplied evidence."
  },
  "important_caveats": [
    "The sequence match and functional annotation are reviewer-only evidence and were not available to the evaluated model.",
    "The annotation cites a publication but uses ECO:0000305; the excerpts do not independently establish that the EC assignment came from a direct experimental assay.",
    "The historical record matches the sequence, but the author's exact source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence matches UniProt entry G4N954 (AUH1_PYRO7) exactly (SHA256 confirmed). The entry is annotated as 'Methylglutaconyl-CoA hydratase 1, mitochondrial' with EC=4.2.1.18, supported by evidence code ECO:0000305 (inferred by similarity) referencing PubMed:32431008. The catalytic activity (HMG-CoA → 3-methylglutaconyl-CoA + H₂O) is explicitly listed. Both the current entry (v56) and the historical archived entry (v54, released 2026-01-28) confirm EC=4.2.1.18. Note: the annotation is similarity-inferred, not direct experimental enzymatic assay, and the source paper uses the word 'putative' in its title.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H1](#evidence-h1), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The N-terminal region (MPPVSRILSYAPRVAIRPSSQLARPARAFAVGTVRYYSAEQPEEPLIRVTDLPAPNSGHIRVLELNRPKARNAISRALLASLREEVHSIARQYDAQTGEEIPTPSWNKRFGGIAGDSEKGPTRALVLASAVESSFCAGADLKERRGFTQEETNEFLANLRSTFAALDALPIPTISAISSRALGGGLELALCTHFRVLTSNAIVSLPETRLGIIPGAGGTHRLPRLIGLGRARDMIVTGRAVSGAEAYFLGLADRLVEVLPPDEQEAADTTDKDAALLSAAREAALTEAVRLASQICEGGPIGIRAALQAVQAPSQETENKMYERVIGTEDRNEALKAFAEKRKPVFKGR) contains a mitochondrial targeting peptide (Arg-rich, hydroxylated residues), and the core domain exhibits a crotonase-superfamily hydratase fold. This reasoning can eliminate B (isomerase, EC 5) and C (oxidoreductase, EC 1), narrowing to A (4.2.1.70) or D (4.2.1.18). However, distinguishing these two specific hydro-lyase EC numbers requires knowledge of the exact substrate (methylglutaconyl-CoA vs. whatever 4.2.1.70 acts on), which is not derivable from general biological reasoning about the fold alone.


**Missing item-specific fact**

> The specific substrate-binding pocket residues and active-site architecture that distinguish methylglutaconyl-CoA hydratase (EC 4.2.1.18) from the enzyme designated EC 4.2.1.70 within the crotonase superfamily, or direct recognition of this protein as AUH1_PYRO7 from its database entry.


**Reason**

> While the mitochondrial targeting sequence and crotonase-like fold provide meaningful reasoning to eliminate isomerase and oxidoreductase options, the final choice between two EC 4.2.1.x hydro-lyases depends on recognizing the specific protein family or knowing the substrate specificity—item-specific facts not inferable from general enzymology. The annotation itself is similarity-inferred (ECO:0000305), and the source paper labels the gene 'putative,' underscoring that even the database assignment rests on homology rather than a de novo structural/functional argument.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "D"
]
```

> Both 4.2.1.70 and 4.2.1.18 are hydro-lyases (hydratases) within the EC 4.2.1.x class. A model reasoning from the crotonase fold and mitochondrial targeting could plausibly select either without additional substrate-specific knowledge. The evidence unambiguously supports D, but the question text alone does not provide a decisive argument to exclude A over D for a model lacking memorized family-level identification.


### Important caveats

- The UniProt annotation uses evidence code ECO:0000305 (inferred by similarity), not direct experimental enzyme assay. The source paper (PubMed:32431008) describes MoAUH1 as a 'putative' methylglutaconyl-CoA hydratase.
- The accession G4N954 and its Swiss-Prot status were established from reviewer-only metadata absent from the model input; the model only saw the raw 349-aa sequence.
- EC 4.2.1.70's exact identity was not independently verified from the evidence provided; its presence as a distractor is assumed based on the multiple-choice set.
- The historical entry (v54) and current entry (v56) both confirm EC=4.2.1.18, so the annotation is stable across the relevant time window.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal region (MPPVSRILSYAPRVAIRPSSQLARPARAFAVGTVRYYSAEQPEEPLIRVTDLPAPNSGHIRVLELNRPKARNAISRALLASLREEVHSIARQYDAQTGEEIPTPSWNKRFGGIAGDSEKGPTRALVLASAVESSFCAGADLKERRGFTQEETNEFLANLRSTFAALDALPIPTISAISSRALGGGLELALCTHFRVLTSNAIVSLPETRLGIIPGAGGTHRLPRLIGLGRARDMIVTGRAVSGAEAYFLGLADRLVEVLPPDEQEAADTTDKDAALLSAAREAALTEAVRLASQICEGGPIGIRAALQAVQAPSQETENKMYERVIGTEDRNEALKAFAEKRKPVFKGR) contains a mitochondrial targeting peptide (Arg-rich, hydroxylated residues), and the core domain exhibits a crotonase-superfamily hydratase fold. This reasoning can eliminate B (isomerase, EC 5) and C (oxidoreductase, EC 1), narrowing to A (4.2.1.70) or D (4.2.1.18). However, distinguishing these two specific hydro-lyase EC numbers requires knowledge of the exact substrate (methylglutaconyl-CoA vs. whatever 4.2.1.70 acts on), which is not derivable from general biological reasoning about the fold alone.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific substrate-binding pocket residues and active-site architecture that distinguish methylglutaconyl-CoA hydratase (EC 4.2.1.18) from the enzyme designated EC 4.2.1.70 within the crotonase superfamily, or direct recognition of this protein as AUH1_PYRO7 from its database entry.",
    "reason": "While the mitochondrial targeting sequence and crotonase-like fold provide meaningful reasoning to eliminate isomerase and oxidoreductase options, the final choice between two EC 4.2.1.x hydro-lyases depends on recognizing the specific protein family or knowing the substrate specificity—item-specific facts not inferable from general enzymology. The annotation itself is similarity-inferred (ECO:0000305), and the source paper labels the gene 'putative,' underscoring that even the database assignment rests on homology rather than a de novo structural/functional argument."
  },
  "case_id": "EC_number_0032",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H1",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence matches UniProt entry G4N954 (AUH1_PYRO7) exactly (SHA256 confirmed). The entry is annotated as 'Methylglutaconyl-CoA hydratase 1, mitochondrial' with EC=4.2.1.18, supported by evidence code ECO:0000305 (inferred by similarity) referencing PubMed:32431008. The catalytic activity (HMG-CoA → 3-methylglutaconyl-CoA + H₂O) is explicitly listed. Both the current entry (v56) and the historical archived entry (v54, released 2026-01-28) confirm EC=4.2.1.18. Note: the annotation is similarity-inferred, not direct experimental enzymatic assay, and the source paper uses the word 'putative' in its title."
  },
  "important_caveats": [
    "The UniProt annotation uses evidence code ECO:0000305 (inferred by similarity), not direct experimental enzyme assay. The source paper (PubMed:32431008) describes MoAUH1 as a 'putative' methylglutaconyl-CoA hydratase.",
    "The accession G4N954 and its Swiss-Prot status were established from reviewer-only metadata absent from the model input; the model only saw the raw 349-aa sequence.",
    "EC 4.2.1.70's exact identity was not independently verified from the evidence provided; its presence as a distractor is assumed based on the multiple-choice set.",
    "The historical entry (v54) and current entry (v56) both confirm EC=4.2.1.18, so the annotation is stable across the relevant time window."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "D"
    ],
    "reason": "Both 4.2.1.70 and 4.2.1.18 are hydro-lyases (hydratases) within the EC 4.2.1.x class. A model reasoning from the crotonase fold and mitochondrial targeting could plausibly select either without additional substrate-specific knowledge. The evidence unambiguously supports D, but the question text alone does not provide a decisive argument to exclude A over D for a model lacking memorized family-level identification."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0032",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches UniProt entry G4N954 (AUH1_PYRO7) exactly (SHA256 confirmed). The entry is annotated as 'Methylglutaconyl-CoA hydratase 1, mitochondrial' with EC=4.2.1.18, supported by evidence code ECO:0000305 (inferred by similarity) referencing PubMed:32431008. The catalytic activity (HMG-CoA → 3-methylglutaconyl-CoA + H₂O) is explicitly listed. Both the current entry (v56) and the historical archived entry (v54, released 2026-01-28) confirm EC=4.2.1.18. Note: the annotation is similarity-inferred, not direct experimental enzymatic assay, and the source paper uses the word 'putative' in its title.",
    "evidence_ids": ["C1", "C4", "C5", "H1", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The N-terminal region (MPPVSRILSYAPRVAIRPSSQLARPARAFAVGTVRYYSAEQPEEPLIRVTDLPAPNSGHIRVLELNRPKARNAISRALLASLREEVHSIARQYDAQTGEEIPTPSWNKRFGGIAGDSEKGPTRALVLASAVESSFCAGADLKERRGFTQEETNEFLANLRSTFAALDALPIPTISAISSRALGGGLELALCTHFRVLTSNAIVSLPETRLGIIPGAGGTHRLPRLIGLGRARDMIVTGRAVSGAEAYFLGLADRLVEVLPPDEQEAADTTDKDAALLSAAREAALTEAVRLASQICEGGPIGIRAALQAVQAPSQETENKMYERVIGTEDRNEALKAFAEKRKPVFKGR) contains a mitochondrial targeting peptide (Arg-rich, hydroxylated residues), and the core domain exhibits a crotonase-superfamily hydratase fold. This reasoning can eliminate B (isomerase, EC 5) and C (oxidoreductase, EC 1), narrowing to A (4.2.1.70) or D (4.2.1.18). However, distinguishing these two specific hydro-lyase EC numbers requires knowledge of the exact substrate (methylglutaconyl-CoA vs. whatever 4.2.1.70 acts on), which is not derivable from general biological reasoning about the fold alone.",
    "missing_item_specific_fact": "The specific substrate-binding pocket residues and active-site architecture that distinguish methylglutaconyl-CoA hydratase (EC 4.2.1.18) from the enzyme designated EC 4.2.1.70 within the crotonase superfamily, or direct recognition of this protein as AUH1_PYRO7 from its database entry.",
    "reason": "While the mitochondrial targeting sequence and crotonase-like fold provide meaningful reasoning to eliminate isomerase and oxidoreductase options, the final choice between two EC 4.2.1.x hydro-lyases depends on recognizing the specific protein family or knowing the substrate specificity—item-specific facts not inferable from general enzymology. The annotation itself is similarity-inferred (ECO:0000305), and the source paper labels the gene 'putative,' underscoring that even the database assignment rests on homology rather than a de novo structural/functional argument."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "D"],
    "reason": "Both 4.2.1.70 and 4.2.1.18 are hydro-lyases (hydratases) within the EC 4.2.1.x class. A model reasoning from the crotonase fold and mitochondrial targeting could plausibly select either without additional substrate-specific knowledge. The evidence unambiguously supports D, but the question text alone does not provide a decisive argument to exclude A over D for a model lacking memorized family-level identification."
  },
  "important_caveats": [
    "The UniProt annotation uses evidence code ECO:0000305 (inferred by similarity), not direct experimental enzyme assay. The source paper (PubMed:32431008) describes MoAUH1 as a 'putative' methylglutaconyl-CoA hydratase.",
    "The accession G4N954 and its Swiss-Prot status were established from reviewer-only metadata absent from the model input; the model only saw the raw 349-aa sequence.",
    "EC 4.2.1.70's exact identity was not independently verified from the evidence provided; its presence as a distractor is assumed based on the multiple-choice set.",
    "The historical entry (v54) and current entry (v56) both confirm EC=4.2.1.18, so the annotation is stable across the relevant time window."
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

**Accession:** `G4N954` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 54. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G4N954.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:45.109101+00:00.  

```json
"G4N954"
```

Source SHA-256: `f1feb70a0aa6ce77a3f46c3887f39c0438ffbec8f1dda03d658acd878f87049c`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G4N954.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:45.109101+00:00.  

```json
{"flag":"Precursor","recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000305","id":"32431008","source":"PubMed"}],"value":"4.2.1.18"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"32431008","source":"PubMed"}],"value":"Methylglutaconyl-CoA hydratase 1, mitochondrial"}}}
```

Source SHA-256: `f1feb70a0aa6ce77a3f46c3887f39c0438ffbec8f1dda03d658acd878f87049c`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G4N954.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:45.109101+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"4.2.1.18","evidences":[{"evidenceCode":"ECO:0000305","id":"32431008","source":"PubMed"}],"name":"(3S)-3-hydroxy-3-methylglutaryl-CoA = 3-methyl-(2E)-glutaconyl-CoA + H2O","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:21536"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:43074"},{"database":"ChEBI","id":"CHEBI:57346"}]}}
```

Source SHA-256: `f1feb70a0aa6ce77a3f46c3887f39c0438ffbec8f1dda03d658acd878f87049c`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G4N954?format=txt&versions=54)  
**Locator:** `lines 1-14`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 54 / 1.  
**Retrieved:** 2026-11-02T04:28:47.046190+00:00.  

```text
ID   AUH1_PYRO7              Reviewed;         349 AA.
AC   G4N954;
DT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.
DT   14-DEC-2011, sequence version 1.
DT   28-JAN-2026, entry version 54.
DE   RecName: Full=Methylglutaconyl-CoA hydratase 1, mitochondrial {ECO:0000303|PubMed:32431008};
DE            EC=4.2.1.18 {ECO:0000305|PubMed:32431008};
DE   Flags: Precursor;
GN   Name=AUH1 {ECO:0000303|PubMed:32431008}; ORFNames=MGG_03335;
OS   Pyricularia oryzae (strain 70-15 / ATCC MYA-4617 / FGSC 8958) (Rice blast
OS   fungus) (Magnaporthe oryzae).
OC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Sordariomycetes;
OC   Sordariomycetidae; Magnaporthales; Pyriculariaceae; Pyricularia.
OX   NCBI_TaxID=242507;
```

Source SHA-256: `0442f2ae47a56feb93ddf2851830770bbc3cdc78cf17135612d99cf022c5c856`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G4N954?format=txt&versions=54)  
**Locator:** `lines 6-8`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 54 / 1.  
**Retrieved:** 2026-11-02T04:28:47.046190+00:00.  

```text
DE   RecName: Full=Methylglutaconyl-CoA hydratase 1, mitochondrial {ECO:0000303|PubMed:32431008};
DE            EC=4.2.1.18 {ECO:0000305|PubMed:32431008};
DE   Flags: Precursor;
```

Source SHA-256: `0442f2ae47a56feb93ddf2851830770bbc3cdc78cf17135612d99cf022c5c856`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G4N954?format=txt&versions=54)  
**Locator:** `lines 44-48`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 54 / 1.  
**Retrieved:** 2026-11-02T04:28:47.046190+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=(3S)-3-hydroxy-3-methylglutaryl-CoA = 3-methyl-(2E)-
CC         glutaconyl-CoA + H2O; Xref=Rhea:RHEA:21536, ChEBI:CHEBI:15377,
CC         ChEBI:CHEBI:43074, ChEBI:CHEBI:57346; EC=4.2.1.18;
CC         Evidence={ECO:0000305|PubMed:32431008};
```

Source SHA-256: `0442f2ae47a56feb93ddf2851830770bbc3cdc78cf17135612d99cf022c5c856`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 32. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
