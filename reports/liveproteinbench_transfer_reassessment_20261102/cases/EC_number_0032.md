# EC_number_0032: before and after transfer clarification

[All 1,328 cases](../README.md) · [Method](../METHOD.md) · [Summary](../SUMMARY.md) · [Exact reviewer user message](../inputs/EC_number_0032.txt)

**Task:** `EC_number`  
**Author key, unchanged:** **D** — 4.2.1.18

| Round | Reviewer | Key support | Transfer / lookup | Output usability (canonical status) |
|---|---|---|---|---|
| before | GPT-6 Luna | supported | lookup-dependent | usable output (valid_review) |
| before | Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | usable output (valid_review) |
| after | GPT-6 Luna | supported | reasoning-supported | usable output (valid_review) |
| after | Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | usable output (valid_review) |

**Usable output means format-valid review, not reasoning-supported or biologically correct.** A usable output can classify the question as reasoning-supported, lookup-dependent or uncertain. An output error is a problem with the saved model response; it does not count a defective benchmark question or wrong key. Each saved review is retained in full below. Labels from output errors are displayed as saved and excluded from label statistics. The author key and reviewer evidence were visible to reviewers; this is a review of answerability and key support, not a benchmark-solving score.

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
<summary>Complete original system instructions</summary>

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

## Four saved visible reviews

## Before: GPT-6 Luna

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

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

## Before: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

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

## After: GPT-6 Luna

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence-matched UniProt record annotates this protein as methylglutaconyl-CoA hydratase with EC 4.2.1.18 and gives the corresponding catalytic reaction. The annotation is linked to a publication, but its evidence code indicates curator inference from literature, not necessarily an independently verified enzyme assay.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has a plausible mitochondrial targeting segment at its N-terminus followed by a roughly 320-residue enzyme domain, consistent with the mitochondrial AUH/methylglutaconyl-CoA hydratase family. Family-level recognition, including the domain’s CoA-enzyme-like sequence features, gives a meaningful basis for choosing EC 4.2.1.18 over the unrelated reaction classes in B and C and the alternative hydratase in A.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The exact catalytic assignment is not proven from the sequence alone, but transferable family knowledge provides a credible probabilistic distinction among these options; the choice need not depend on recalling this protein’s database record.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The supplied options identify distinct EC assignments, and the family-level inference favors D.


### Important caveats

- The source annotation is sequence-matched, but it is a curated literature-based assignment rather than direct experimental evidence presented here.
- The sequence-based family inference is probabilistic, not a complete independent demonstration of substrate specificity.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has a plausible mitochondrial targeting segment at its N-terminus followed by a roughly 320-residue enzyme domain, consistent with the mitochondrial AUH/methylglutaconyl-CoA hydratase family. Family-level recognition, including the domain’s CoA-enzyme-like sequence features, gives a meaningful basis for choosing EC 4.2.1.18 over the unrelated reaction classes in B and C and the alternative hydratase in A.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The exact catalytic assignment is not proven from the sequence alone, but transferable family knowledge provides a credible probabilistic distinction among these options; the choice need not depend on recalling this protein’s database record."
  },
  "case_id": "EC_number_0032",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates this protein as methylglutaconyl-CoA hydratase with EC 4.2.1.18 and gives the corresponding catalytic reaction. The annotation is linked to a publication, but its evidence code indicates curator inference from literature, not necessarily an independently verified enzyme assay."
  },
  "important_caveats": [
    "The source annotation is sequence-matched, but it is a curated literature-based assignment rather than direct experimental evidence presented here.",
    "The sequence-based family inference is probabilistic, not a complete independent demonstration of substrate specificity."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied options identify distinct EC assignments, and the family-level inference favors D."
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
    "reason": "The sequence-matched UniProt record annotates this protein as methylglutaconyl-CoA hydratase with EC 4.2.1.18 and gives the corresponding catalytic reaction. The annotation is linked to a publication, but its evidence code indicates curator inference from literature, not necessarily an independently verified enzyme assay.",
    "evidence_ids": ["C4", "C5", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has a plausible mitochondrial targeting segment at its N-terminus followed by a roughly 320-residue enzyme domain, consistent with the mitochondrial AUH/methylglutaconyl-CoA hydratase family. Family-level recognition, including the domain’s CoA-enzyme-like sequence features, gives a meaningful basis for choosing EC 4.2.1.18 over the unrelated reaction classes in B and C and the alternative hydratase in A.",
    "missing_item_specific_fact": "",
    "reason": "The exact catalytic assignment is not proven from the sequence alone, but transferable family knowledge provides a credible probabilistic distinction among these options; the choice need not depend on recalling this protein’s database record."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied options identify distinct EC assignments, and the family-level inference favors D."
  },
  "important_caveats": [
    "The source annotation is sequence-matched, but it is a curated literature-based assignment rather than direct experimental evidence presented here.",
    "The sequence-based family inference is probabilistic, not a complete independent demonstration of substrate specificity."
  ]
}
```

</details>

## After: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry G4N954 (AUH1_PYRO7) annotates this protein as Methylglutaconyl-CoA hydratase 1, mitochondrial, with EC 4.2.1.18. The evidence code is ECO:0000305 (inferred by curator) based on PubMed:32431008, a 2021 paper characterizing MoAUH1 in Magnaporthe oryzae. The catalytic reaction is annotated as (3S)-3-hydroxy-3-methylglutaryl-CoA = 3-methyl-(2E)-glutaconyl-CoA + H2O. The annotation is a curator-assigned inference from published functional data rather than direct purified-enzyme kinetics, but it is a well-supported database annotation. The sequence matches the benchmark input exactly (349 AA, SHA256 confirmed).

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains recognizable crotonase-superfamily motifs: a GGG triplet ('GGGLELAL' near residue ~168) forming part of the oxyanion hole, a GAD motif ('GADLKERRGF' near residue ~117) near the catalytic center, and a GA-containing stretch ('GAEAYFLGL' near residue ~240). These are hallmark features of the enoyl-CoA hydratase / methylglutaconyl-CoA hydratase (crotonase) superfamily, which belongs to EC class 4.2 (hydro-lyases). This immediately eliminates B (EC 5.6.2.4, a protein isomerase — no isomerase-like features present) and C (EC 1.14.15.9, a copper-dependent monooxygenase — no copper-binding His-rich motifs or FAD/NAD-binding Rossmann folds present). Among the remaining hydratase options, EC 4.2.1.70 is not a currently assigned EC number in the IUBMB list (it is a non-existent or retired designation), leaving D (EC 4.2.1.18, 3-methylglutaconyl-CoA hydratase) as the only valid hydratase. Additionally, the N-terminal ~20 residues (MPPVSRILSYAPRVAIRPSSQ) are consistent with a mitochondrial targeting presequence, matching the 'Precursor' flag typical of AUH homologs. The overall 349-aa length and composition are consistent with fungal AUH orthologs (human AUH is ~317 aa mature + targeting peptide). Thus, family-level motif recognition (crotonase superfamily) plus elimination of non-existent EC numbers and wrong enzyme classes meaningfully distinguishes D from the other three choices without needing the specific UniProt record for this exact protein.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A model trained on general protein biochemistry can recognize the crotonase-superfamily GGG/GAD motifs to assign the protein to EC class 4.2, eliminating the isomerase and oxidoreductase distractors. The distinction between 4.2.1.18 and 4.2.1.70 relies on knowing that 4.2.1.70 is not a valid/assigned EC number, which is part of general enzyme classification knowledge rather than a fact specific to this exact protein. The mitochondrial presequence and overall length further corroborate the AUH assignment. This constitutes a defensible transferable inference from family-level sequence features.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> EC 4.2.1.70 appears to be an unassigned EC number, making A trivially invalid. B and C belong to entirely different EC classes with no sequence support. Only D is both a valid EC number and consistent with the crotonase-superfamily motifs in the sequence. No genuine ambiguity among the offered choices.


### Important caveats

- The UniProt annotation uses evidence code ECO:0000305 (inferred by curator from a published paper), not direct in-vitro enzyme assay. The functional assignment is well-supported but is a curator inference rather than purified-enzyme kinetics.
- EC 4.2.1.70 is assessed here as likely unassigned based on general knowledge of the IUBMB EC list; if it were in fact assigned to some obscure hydratase, the discrimination between A and D would be weaker and might require more specific substrate-binding residue analysis.
- The mitochondrial targeting sequence inference is based on general N-terminal composition patterns common to many mitochondrial proteins, not a verified cleavage-site experiment for this specific protein.
- All UniProt evidence is reviewer-only and was not available to the evaluated model; the reasoning above relies solely on the sequence and general transferable knowledge.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains recognizable crotonase-superfamily motifs: a GGG triplet ('GGGLELAL' near residue ~168) forming part of the oxyanion hole, a GAD motif ('GADLKERRGF' near residue ~117) near the catalytic center, and a GA-containing stretch ('GAEAYFLGL' near residue ~240). These are hallmark features of the enoyl-CoA hydratase / methylglutaconyl-CoA hydratase (crotonase) superfamily, which belongs to EC class 4.2 (hydro-lyases). This immediately eliminates B (EC 5.6.2.4, a protein isomerase — no isomerase-like features present) and C (EC 1.14.15.9, a copper-dependent monooxygenase — no copper-binding His-rich motifs or FAD/NAD-binding Rossmann folds present). Among the remaining hydratase options, EC 4.2.1.70 is not a currently assigned EC number in the IUBMB list (it is a non-existent or retired designation), leaving D (EC 4.2.1.18, 3-methylglutaconyl-CoA hydratase) as the only valid hydratase. Additionally, the N-terminal ~20 residues (MPPVSRILSYAPRVAIRPSSQ) are consistent with a mitochondrial targeting presequence, matching the 'Precursor' flag typical of AUH homologs. The overall 349-aa length and composition are consistent with fungal AUH orthologs (human AUH is ~317 aa mature + targeting peptide). Thus, family-level motif recognition (crotonase superfamily) plus elimination of non-existent EC numbers and wrong enzyme classes meaningfully distinguishes D from the other three choices without needing the specific UniProt record for this exact protein.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A model trained on general protein biochemistry can recognize the crotonase-superfamily GGG/GAD motifs to assign the protein to EC class 4.2, eliminating the isomerase and oxidoreductase distractors. The distinction between 4.2.1.18 and 4.2.1.70 relies on knowing that 4.2.1.70 is not a valid/assigned EC number, which is part of general enzyme classification knowledge rather than a fact specific to this exact protein. The mitochondrial presequence and overall length further corroborate the AUH assignment. This constitutes a defensible transferable inference from family-level sequence features."
  },
  "case_id": "EC_number_0032",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry G4N954 (AUH1_PYRO7) annotates this protein as Methylglutaconyl-CoA hydratase 1, mitochondrial, with EC 4.2.1.18. The evidence code is ECO:0000305 (inferred by curator) based on PubMed:32431008, a 2021 paper characterizing MoAUH1 in Magnaporthe oryzae. The catalytic reaction is annotated as (3S)-3-hydroxy-3-methylglutaryl-CoA = 3-methyl-(2E)-glutaconyl-CoA + H2O. The annotation is a curator-assigned inference from published functional data rather than direct purified-enzyme kinetics, but it is a well-supported database annotation. The sequence matches the benchmark input exactly (349 AA, SHA256 confirmed)."
  },
  "important_caveats": [
    "The UniProt annotation uses evidence code ECO:0000305 (inferred by curator from a published paper), not direct in-vitro enzyme assay. The functional assignment is well-supported but is a curator inference rather than purified-enzyme kinetics.",
    "EC 4.2.1.70 is assessed here as likely unassigned based on general knowledge of the IUBMB EC list; if it were in fact assigned to some obscure hydratase, the discrimination between A and D would be weaker and might require more specific substrate-binding residue analysis.",
    "The mitochondrial targeting sequence inference is based on general N-terminal composition patterns common to many mitochondrial proteins, not a verified cleavage-site experiment for this specific protein.",
    "All UniProt evidence is reviewer-only and was not available to the evaluated model; the reasoning above relies solely on the sequence and general transferable knowledge."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "EC 4.2.1.70 appears to be an unassigned EC number, making A trivially invalid. B and C belong to entirely different EC classes with no sequence support. Only D is both a valid EC number and consistent with the crotonase-superfamily motifs in the sequence. No genuine ambiguity among the offered choices."
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
    "reason": "The UniProt entry G4N954 (AUH1_PYRO7) annotates this protein as Methylglutaconyl-CoA hydratase 1, mitochondrial, with EC 4.2.1.18. The evidence code is ECO:0000305 (inferred by curator) based on PubMed:32431008, a 2021 paper characterizing MoAUH1 in Magnaporthe oryzae. The catalytic reaction is annotated as (3S)-3-hydroxy-3-methylglutaryl-CoA = 3-methyl-(2E)-glutaconyl-CoA + H2O. The annotation is a curator-assigned inference from published functional data rather than direct purified-enzyme kinetics, but it is a well-supported database annotation. The sequence matches the benchmark input exactly (349 AA, SHA256 confirmed).",
    "evidence_ids": ["C4", "C5", "C6", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains recognizable crotonase-superfamily motifs: a GGG triplet ('GGGLELAL' near residue ~168) forming part of the oxyanion hole, a GAD motif ('GADLKERRGF' near residue ~117) near the catalytic center, and a GA-containing stretch ('GAEAYFLGL' near residue ~240). These are hallmark features of the enoyl-CoA hydratase / methylglutaconyl-CoA hydratase (crotonase) superfamily, which belongs to EC class 4.2 (hydro-lyases). This immediately eliminates B (EC 5.6.2.4, a protein isomerase — no isomerase-like features present) and C (EC 1.14.15.9, a copper-dependent monooxygenase — no copper-binding His-rich motifs or FAD/NAD-binding Rossmann folds present). Among the remaining hydratase options, EC 4.2.1.70 is not a currently assigned EC number in the IUBMB list (it is a non-existent or retired designation), leaving D (EC 4.2.1.18, 3-methylglutaconyl-CoA hydratase) as the only valid hydratase. Additionally, the N-terminal ~20 residues (MPPVSRILSYAPRVAIRPSSQ) are consistent with a mitochondrial targeting presequence, matching the 'Precursor' flag typical of AUH homologs. The overall 349-aa length and composition are consistent with fungal AUH orthologs (human AUH is ~317 aa mature + targeting peptide). Thus, family-level motif recognition (crotonase superfamily) plus elimination of non-existent EC numbers and wrong enzyme classes meaningfully distinguishes D from the other three choices without needing the specific UniProt record for this exact protein.",
    "missing_item_specific_fact": "",
    "reason": "A model trained on general protein biochemistry can recognize the crotonase-superfamily GGG/GAD motifs to assign the protein to EC class 4.2, eliminating the isomerase and oxidoreductase distractors. The distinction between 4.2.1.18 and 4.2.1.70 relies on knowing that 4.2.1.70 is not a valid/assigned EC number, which is part of general enzyme classification knowledge rather than a fact specific to this exact protein. The mitochondrial presequence and overall length further corroborate the AUH assignment. This constitutes a defensible transferable inference from family-level sequence features."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "EC 4.2.1.70 appears to be an unassigned EC number, making A trivially invalid. B and C belong to entirely different EC classes with no sequence support. Only D is both a valid EC number and consistent with the crotonase-superfamily motifs in the sequence. No genuine ambiguity among the offered choices."
  },
  "important_caveats": [
    "The UniProt annotation uses evidence code ECO:0000305 (inferred by curator from a published paper), not direct in-vitro enzyme assay. The functional assignment is well-supported but is a curator inference rather than purified-enzyme kinetics.",
    "EC 4.2.1.70 is assessed here as likely unassigned based on general knowledge of the IUBMB EC list; if it were in fact assigned to some obscure hydratase, the discrimination between A and D would be weaker and might require more specific substrate-binding residue analysis.",
    "The mitochondrial targeting sequence inference is based on general N-terminal composition patterns common to many mitochondrial proteins, not a verified cleavage-site experiment for this specific protein.",
    "All UniProt evidence is reviewer-only and was not available to the evaluated model; the reasoning above relies solely on the sequence and general transferable knowledge."
  ]
}
```

</details>

## Existing project source checks of the old Luna review only

These unchanged notes concern the earlier Luna claims. They do not validate either new review or the old Qwen review. No new scientific adjudication was performed.

## Project source-check notes

These project-authored, AI-assisted checks assess specific source claims. They are not expert adjudication and do not replace Luna’s saved review or the author key.

No additional case-specific project note was recorded. Citation membership checks do not establish that every scientific argument is correct.

## Complete reviewer-only evidence and qualifications

All excerpts supplied in the original and revised reviewer user message follow. This material was not available to the original evaluated model. Accession identity came from dataset image-path metadata. Source support and transferable discrimination are separate judgments.

**Applicability metadata, unchanged:**

```json
{
  "requested_accession": "G4N954",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "benchmark_sequence_sha256": "5e891c748ec2835aa75f719bfdb800087960d21c8e74e2457645a7ad7fbe7243",
  "benchmark_sequence_length": 349,
  "current_status": "retrieved",
  "current_sequence_comparison": "matched",
  "current_entry_audit": {
    "entryVersion": 56,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2011-12-14",
    "sequenceVersion": 1
  },
  "current_uniprot_release": "2026_03",
  "current_record_sha256": "f1feb70a0aa6ce77a3f46c3887f39c0438ffbec8f1dda03d658acd878f87049c",
  "current_source_sequence_sha256": "5e891c748ec2835aa75f719bfdb800087960d21c8e74e2457645a7ad7fbe7243",
  "current_source_sequence_length": 349,
  "historical_status": "retrieved",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "selected_historical_entry_version": 54,
  "selected_historical_version": {
    "accession": "G4N954",
    "database": "Swiss-Prot",
    "entryVersion": 54,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "AUH1_PYRO7",
    "sequenceVersion": 1
  },
  "selected_historical_record_sha256": "0442f2ae47a56feb93ddf2851830770bbc3cdc78cf17135612d99cf022c5c856",
  "selected_historical_source_sequence_sha256": "5e891c748ec2835aa75f719bfdb800087960d21c8e74e2457645a7ad7fbe7243",
  "selected_historical_source_sequence_length": 349,
  "latest_at_cutoff_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 54,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "actual_author_source_snapshot": "unknown",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed."
}
```

**Qualifications, unchanged:**

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G4N954.json)

```json
{
  "evidence_id": "C1",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/G4N954.json",
  "source_sha256": "f1feb70a0aa6ce77a3f46c3887f39c0438ffbec8f1dda03d658acd878f87049c",
  "retrieved_utc": "2026-11-02T04:28:45.109101+00:00",
  "json_pointer": "/primaryAccession",
  "excerpt": "\"G4N954\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G4N954.json)

```json
{
  "evidence_id": "C2",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/G4N954.json",
  "source_sha256": "f1feb70a0aa6ce77a3f46c3887f39c0438ffbec8f1dda03d658acd878f87049c",
  "retrieved_utc": "2026-11-02T04:28:45.109101+00:00",
  "json_pointer": "/entryAudit",
  "excerpt": "{\"entryVersion\":56,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2011-12-14\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G4N954.json)

```json
{
  "evidence_id": "C3",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/G4N954.json",
  "source_sha256": "f1feb70a0aa6ce77a3f46c3887f39c0438ffbec8f1dda03d658acd878f87049c",
  "retrieved_utc": "2026-11-02T04:28:45.109101+00:00",
  "json_pointer": "/organism",
  "excerpt": "{\"commonName\":\"Rice blast fungus\",\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Sordariomycetes\",\"Sordariomycetidae\",\"Magnaporthales\",\"Pyriculariaceae\",\"Pyricularia\"],\"scientificName\":\"Pyricularia oryzae (strain 70-15 / ATCC MYA-4617 / FGSC 8958)\",\"synonyms\":[\"Magnaporthe oryzae\"],\"taxonId\":242507}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G4N954.json)

```json
{
  "evidence_id": "C4",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/G4N954.json",
  "source_sha256": "f1feb70a0aa6ce77a3f46c3887f39c0438ffbec8f1dda03d658acd878f87049c",
  "retrieved_utc": "2026-11-02T04:28:45.109101+00:00",
  "json_pointer": "/proteinDescription",
  "excerpt": "{\"flag\":\"Precursor\",\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"32431008\",\"source\":\"PubMed\"}],\"value\":\"4.2.1.18\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"32431008\",\"source\":\"PubMed\"}],\"value\":\"Methylglutaconyl-CoA hydratase 1, mitochondrial\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G4N954.json)

```json
{
  "evidence_id": "C5",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/G4N954.json",
  "source_sha256": "f1feb70a0aa6ce77a3f46c3887f39c0438ffbec8f1dda03d658acd878f87049c",
  "retrieved_utc": "2026-11-02T04:28:45.109101+00:00",
  "json_pointer": "/comments/1",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"ecNumber\":\"4.2.1.18\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"32431008\",\"source\":\"PubMed\"}],\"name\":\"(3S)-3-hydroxy-3-methylglutaryl-CoA = 3-methyl-(2E)-glutaconyl-CoA + H2O\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:21536\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:43074\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57346\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G4N954.json)

```json
{
  "evidence_id": "C6",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/G4N954.json",
  "source_sha256": "f1feb70a0aa6ce77a3f46c3887f39c0438ffbec8f1dda03d658acd878f87049c",
  "retrieved_utc": "2026-11-02T04:28:45.109101+00:00",
  "json_pointer": "/references/1",
  "excerpt": "{\"citation\":{\"authors\":[\"Xiao Y.\",\"Liu L.\",\"Zhang T.\",\"Zhou R.\",\"Ren Y.\",\"Li X.\",\"Shu H.\",\"Ye W.\",\"Zheng X.\",\"Zhang Z.\",\"Zhang H.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"32431008\"},{\"database\":\"DOI\",\"id\":\"10.1111/1462-2920.15088\"}],\"citationType\":\"journal article\",\"firstPage\":\"774\",\"id\":\"32431008\",\"journal\":\"Environ. Microbiol.\",\"lastPage\":\"790\",\"publicationDate\":\"2021\",\"title\":\"Transcription factor MoMsn2 targets the putative 3-methylglutaconyl-CoA hydratase-encoding gene MoAUH1 to govern infectious growth via mitochondrial fusion/fission balance in Magnaporthe oryzae.\",\"volume\":\"23\"},\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"DISRUPTION PHENOTYPE\",\"SUBCELLULAR LOCATION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G4N954?format=txt&versions=54)

```json
{
  "evidence_id": "H1",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/G4N954?format=txt&versions=54",
  "source_sha256": "0442f2ae47a56feb93ddf2851830770bbc3cdc78cf17135612d99cf022c5c856",
  "retrieved_utc": "2026-11-02T04:28:47.046190+00:00",
  "source_locator": "lines 1-14",
  "excerpt": "ID   AUH1_PYRO7              Reviewed;         349 AA.\nAC   G4N954;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   14-DEC-2011, sequence version 1.\nDT   28-JAN-2026, entry version 54.\nDE   RecName: Full=Methylglutaconyl-CoA hydratase 1, mitochondrial {ECO:0000303|PubMed:32431008};\nDE            EC=4.2.1.18 {ECO:0000305|PubMed:32431008};\nDE   Flags: Precursor;\nGN   Name=AUH1 {ECO:0000303|PubMed:32431008}; ORFNames=MGG_03335;\nOS   Pyricularia oryzae (strain 70-15 / ATCC MYA-4617 / FGSC 8958) (Rice blast\nOS   fungus) (Magnaporthe oryzae).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Sordariomycetes;\nOC   Sordariomycetidae; Magnaporthales; Pyriculariaceae; Pyricularia.\nOX   NCBI_TaxID=242507;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 54,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G4N954?format=txt&versions=54)

```json
{
  "evidence_id": "H2",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/G4N954?format=txt&versions=54",
  "source_sha256": "0442f2ae47a56feb93ddf2851830770bbc3cdc78cf17135612d99cf022c5c856",
  "retrieved_utc": "2026-11-02T04:28:47.046190+00:00",
  "source_locator": "lines 6-8",
  "excerpt": "DE   RecName: Full=Methylglutaconyl-CoA hydratase 1, mitochondrial {ECO:0000303|PubMed:32431008};\nDE            EC=4.2.1.18 {ECO:0000305|PubMed:32431008};\nDE   Flags: Precursor;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 54,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G4N954?format=txt&versions=54)

```json
{
  "evidence_id": "H3",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/G4N954?format=txt&versions=54",
  "source_sha256": "0442f2ae47a56feb93ddf2851830770bbc3cdc78cf17135612d99cf022c5c856",
  "retrieved_utc": "2026-11-02T04:28:47.046190+00:00",
  "source_locator": "lines 27-35",
  "excerpt": "RN   [2]\nRP   FUNCTION, DISRUPTION PHENOTYPE, AND SUBCELLULAR LOCATION.\nRX   PubMed=32431008; DOI=10.1111/1462-2920.15088;\nRA   Xiao Y., Liu L., Zhang T., Zhou R., Ren Y., Li X., Shu H., Ye W., Zheng X.,\nRA   Zhang Z., Zhang H.;\nRT   \"Transcription factor MoMsn2 targets the putative 3-methylglutaconyl-CoA\nRT   hydratase-encoding gene MoAUH1 to govern infectious growth via\nRT   mitochondrial fusion/fission balance in Magnaporthe oryzae.\";\nRL   Environ. Microbiol. 23:774-790(2021).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 54,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G4N954?format=txt&versions=54)

```json
{
  "evidence_id": "H4",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/G4N954?format=txt&versions=54",
  "source_sha256": "0442f2ae47a56feb93ddf2851830770bbc3cdc78cf17135612d99cf022c5c856",
  "retrieved_utc": "2026-11-02T04:28:47.046190+00:00",
  "source_locator": "lines 44-48",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=(3S)-3-hydroxy-3-methylglutaryl-CoA = 3-methyl-(2E)-\nCC         glutaconyl-CoA + H2O; Xref=Rhea:RHEA:21536, ChEBI:CHEBI:15377,\nCC         ChEBI:CHEBI:43074, ChEBI:CHEBI:57346; EC=4.2.1.18;\nCC         Evidence={ECO:0000305|PubMed:32431008};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 54,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 32. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
