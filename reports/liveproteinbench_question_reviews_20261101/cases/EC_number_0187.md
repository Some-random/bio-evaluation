# EC_number_0187

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `EC_number`  
**Author expected answer:** **B** — 5.1.1.24

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MDRKVQVLDFIKINPAGNITILIDNFDIYDKNIPKLSEEIMKETNLYAEQVGFIKDSHLQMMGGEFCGNASRAFASLLAFRDKDFSKQKNYNITCSGESKVLDVDVRNDGAKNKFLAKIKMPKFLSLEEINVDEYKLGLVRFSGINHFIFNIKENKETSFENIIDLVKKYLSNEEYSAFGIMFFDSDNLSMKPYVYVKEVGSGVYENSCASGTTALGYYLKKCKNLDRAKIVQPNGWLEYIIENDEMYIDGPVEIIAEGKIYIGK

[Multiple Choices]
A. 5.1.3.14
B. 5.1.1.24
C. 1.14.14.154
D. 5.1.3.45
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

> The exact supplied sequence matches the UniProt entry annotated as histidine racemase, EC 5.1.1.24. The annotation assigns experimental evidence (ECO:0000269) to the reaction L-histidine = D-histidine, and the matching archived entry also contains this assignment. This supports choice B, while retaining the qualification that the evidence is reported through the database annotation and cited study.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The choices distinguish different enzyme classes and substrate-specific reactions. General knowledge may suggest that an EC 5.1 enzyme catalyzes racemization or epimerization, but the sequence and prompt provide no concrete basis for identifying histidine as the substrate rather than the reactions represented by the other choices.


**Missing item-specific fact**

> The protein-specific catalytic assignment that this sequence encodes a histidine racemase catalyzing L-histidine = D-histidine.


**Reason**

> Selecting the exact EC number depends on a protein-specific functional annotation or experimental characterization not supplied in the input; recognizing the sequence from an external database would be lookup, not reasoning from the provided evidence.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The supported annotation specifies EC 5.1.1.24, and no competing option is supported by the supplied sequence-level evidence.


### Important caveats

- The reviewer-only source evidence was not available to the evaluated model.
- The archived database record and current record both match the supplied sequence, but the author's exact source snapshot is unknown.
- The experimental evidence is cited in the database annotation; the primary study was not independently reviewed here.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The choices distinguish different enzyme classes and substrate-specific reactions. General knowledge may suggest that an EC 5.1 enzyme catalyzes racemization or epimerization, but the sequence and prompt provide no concrete basis for identifying histidine as the substrate rather than the reactions represented by the other choices.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific catalytic assignment that this sequence encodes a histidine racemase catalyzing L-histidine = D-histidine.",
    "reason": "Selecting the exact EC number depends on a protein-specific functional annotation or experimental characterization not supplied in the input; recognizing the sequence from an external database would be lookup, not reasoning from the provided evidence."
  },
  "case_id": "EC_number_0187",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact supplied sequence matches the UniProt entry annotated as histidine racemase, EC 5.1.1.24. The annotation assigns experimental evidence (ECO:0000269) to the reaction L-histidine = D-histidine, and the matching archived entry also contains this assignment. This supports choice B, while retaining the qualification that the evidence is reported through the database annotation and cited study."
  },
  "important_caveats": [
    "The reviewer-only source evidence was not available to the evaluated model.",
    "The archived database record and current record both match the supplied sequence, but the author's exact source snapshot is unknown.",
    "The experimental evidence is cited in the database annotation; the primary study was not independently reviewed here."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supported annotation specifies EC 5.1.1.24, and no competing option is supported by the supplied sequence-level evidence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0187",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact supplied sequence matches the UniProt entry annotated as histidine racemase, EC 5.1.1.24. The annotation assigns experimental evidence (ECO:0000269) to the reaction L-histidine = D-histidine, and the matching archived entry also contains this assignment. This supports choice B, while retaining the qualification that the evidence is reported through the database annotation and cited study.",
    "evidence_ids": ["C4", "C5", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The choices distinguish different enzyme classes and substrate-specific reactions. General knowledge may suggest that an EC 5.1 enzyme catalyzes racemization or epimerization, but the sequence and prompt provide no concrete basis for identifying histidine as the substrate rather than the reactions represented by the other choices.",
    "missing_item_specific_fact": "The protein-specific catalytic assignment that this sequence encodes a histidine racemase catalyzing L-histidine = D-histidine.",
    "reason": "Selecting the exact EC number depends on a protein-specific functional annotation or experimental characterization not supplied in the input; recognizing the sequence from an external database would be lookup, not reasoning from the provided evidence."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supported annotation specifies EC 5.1.1.24, and no competing option is supported by the supplied sequence-level evidence."
  },
  "important_caveats": [
    "The reviewer-only source evidence was not available to the evaluated model.",
    "The archived database record and current record both match the supplied sequence, but the author's exact source snapshot is unknown.",
    "The experimental evidence is cited in the database annotation; the primary study was not independently reviewed here."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry Q8RI81 (HISR_FUSNN, Fusobacterium nucleatum) is annotated as Histidine racemase with EC 5.1.1.24, supported by direct experimental evidence (ECO:0000269, PubMed:39424140, a 2024 JBC paper by Lamer et al. reporting X-ray crystallography at 2.5 Å, mutagenesis, and catalytic activity assays). The catalytic reaction is L-histidine = D-histidine (Rhea:RHEA:59188). The benchmark sequence (265 aa) matches the UniProt sequence exactly (SHA256 confirmed). The annotation is experimentally verified, not merely computational.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> One could in principle note the absence of canonical PLP-binding motifs (no conserved lysine for internal aldimine) to argue against typical PLP-dependent amino acid racemases, and the overall fold might suggest the racemase/epimerase superfamily (class 5.1), which would eliminate C (1.14.14.154, an oxidoreductase). However, distinguishing 5.1.1.24 (histidine racemase, acting on free amino acids) from 5.1.3.14 or 5.1.3.45 (racemases acting on amino acids AND derivatives) requires knowing the specific substrate is free histidine. No sequence motif in this 265-aa protein uniquely identifies histidine as the substrate or the enzyme as cofactor-independent. The enzyme was only characterized in 2024 and has no well-known homologs with established specificity.


**Missing item-specific fact**

> The specific substrate identity (L-histidine) and the fact that this is a novel cofactor-independent histidine racemase, established only by experimental characterization in 2024 (Lamer et al., JBC 300:107896). Without this item-specific knowledge, the sequence alone does not reveal histidine specificity or the 5.1.1 vs 5.1.3 class distinction.


**Reason**

> The question requires identifying a specific EC number (5.1.1.24) for a novel enzyme characterized in 2024. The sequence provides no obvious motif or domain signature that uniquely points to histidine racemase activity. Distinguishing among the three racemase options (A, B, D) requires knowing the substrate is free histidine (5.1.1) rather than an amino acid derivative (5.1.3), which is not inferable from sequence alone. Recognition of this specific protein as Q8RI81/histidine racemase is essentially a database lookup or memorization task.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "B",
  "D"
]
```

> Without knowledge of the specific substrate (histidine), options A (5.1.3.14), B (5.1.1.24), and D (5.1.3.45) are all racemases/epimerases acting on amino acids or their derivatives. The 5.1.1 vs 5.1.3 distinction (free amino acid vs. derivative) cannot be resolved from sequence alone. Option C (1.14.14.154, oxidoreductase) is clearly eliminable as a different EC class, but the remaining three are not distinguishable by general reasoning from the sequence.


### Important caveats

- The histidine racemase annotation was established only in 2024 (PubMed:39424140), making this a very recent annotation unlikely to be in most training corpora.
- The enzyme is cofactor-independent, so the absence of PLP-binding motifs is consistent with the annotation but does not specifically identify histidine as the substrate.
- The UniProt entry was first released in April 2025 (entry version 81); the historical version 79 (January 2026) already contains the EC 5.1.1.24 annotation with experimental evidence.
- The reviewer evidence confirms sequence match (SHA256) between the benchmark input and UniProt Q8RI81.
- The identity of the protein (Q8RI81) was inferred from dataset metadata not available to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "One could in principle note the absence of canonical PLP-binding motifs (no conserved lysine for internal aldimine) to argue against typical PLP-dependent amino acid racemases, and the overall fold might suggest the racemase/epimerase superfamily (class 5.1), which would eliminate C (1.14.14.154, an oxidoreductase). However, distinguishing 5.1.1.24 (histidine racemase, acting on free amino acids) from 5.1.3.14 or 5.1.3.45 (racemases acting on amino acids AND derivatives) requires knowing the specific substrate is free histidine. No sequence motif in this 265-aa protein uniquely identifies histidine as the substrate or the enzyme as cofactor-independent. The enzyme was only characterized in 2024 and has no well-known homologs with established specificity.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific substrate identity (L-histidine) and the fact that this is a novel cofactor-independent histidine racemase, established only by experimental characterization in 2024 (Lamer et al., JBC 300:107896). Without this item-specific knowledge, the sequence alone does not reveal histidine specificity or the 5.1.1 vs 5.1.3 class distinction.",
    "reason": "The question requires identifying a specific EC number (5.1.1.24) for a novel enzyme characterized in 2024. The sequence provides no obvious motif or domain signature that uniquely points to histidine racemase activity. Distinguishing among the three racemase options (A, B, D) requires knowing the substrate is free histidine (5.1.1) rather than an amino acid derivative (5.1.3), which is not inferable from sequence alone. Recognition of this specific protein as Q8RI81/histidine racemase is essentially a database lookup or memorization task."
  },
  "case_id": "EC_number_0187",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H2",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "UniProt entry Q8RI81 (HISR_FUSNN, Fusobacterium nucleatum) is annotated as Histidine racemase with EC 5.1.1.24, supported by direct experimental evidence (ECO:0000269, PubMed:39424140, a 2024 JBC paper by Lamer et al. reporting X-ray crystallography at 2.5 Å, mutagenesis, and catalytic activity assays). The catalytic reaction is L-histidine = D-histidine (Rhea:RHEA:59188). The benchmark sequence (265 aa) matches the UniProt sequence exactly (SHA256 confirmed). The annotation is experimentally verified, not merely computational."
  },
  "important_caveats": [
    "The histidine racemase annotation was established only in 2024 (PubMed:39424140), making this a very recent annotation unlikely to be in most training corpora.",
    "The enzyme is cofactor-independent, so the absence of PLP-binding motifs is consistent with the annotation but does not specifically identify histidine as the substrate.",
    "The UniProt entry was first released in April 2025 (entry version 81); the historical version 79 (January 2026) already contains the EC 5.1.1.24 annotation with experimental evidence.",
    "The reviewer evidence confirms sequence match (SHA256) between the benchmark input and UniProt Q8RI81.",
    "The identity of the protein (Q8RI81) was inferred from dataset metadata not available to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "B",
      "D"
    ],
    "reason": "Without knowledge of the specific substrate (histidine), options A (5.1.3.14), B (5.1.1.24), and D (5.1.3.45) are all racemases/epimerases acting on amino acids or their derivatives. The 5.1.1 vs 5.1.3 distinction (free amino acid vs. derivative) cannot be resolved from sequence alone. Option C (1.14.14.154, oxidoreductase) is clearly eliminable as a different EC class, but the remaining three are not distinguishable by general reasoning from the sequence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0187",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry Q8RI81 (HISR_FUSNN, Fusobacterium nucleatum) is annotated as Histidine racemase with EC 5.1.1.24, supported by direct experimental evidence (ECO:0000269, PubMed:39424140, a 2024 JBC paper by Lamer et al. reporting X-ray crystallography at 2.5 Å, mutagenesis, and catalytic activity assays). The catalytic reaction is L-histidine = D-histidine (Rhea:RHEA:59188). The benchmark sequence (265 aa) matches the UniProt sequence exactly (SHA256 confirmed). The annotation is experimentally verified, not merely computational.",
    "evidence_ids": ["C4", "C5", "C6", "H2", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "One could in principle note the absence of canonical PLP-binding motifs (no conserved lysine for internal aldimine) to argue against typical PLP-dependent amino acid racemases, and the overall fold might suggest the racemase/epimerase superfamily (class 5.1), which would eliminate C (1.14.14.154, an oxidoreductase). However, distinguishing 5.1.1.24 (histidine racemase, acting on free amino acids) from 5.1.3.14 or 5.1.3.45 (racemases acting on amino acids AND derivatives) requires knowing the specific substrate is free histidine. No sequence motif in this 265-aa protein uniquely identifies histidine as the substrate or the enzyme as cofactor-independent. The enzyme was only characterized in 2024 and has no well-known homologs with established specificity.",
    "missing_item_specific_fact": "The specific substrate identity (L-histidine) and the fact that this is a novel cofactor-independent histidine racemase, established only by experimental characterization in 2024 (Lamer et al., JBC 300:107896). Without this item-specific knowledge, the sequence alone does not reveal histidine specificity or the 5.1.1 vs 5.1.3 class distinction.",
    "reason": "The question requires identifying a specific EC number (5.1.1.24) for a novel enzyme characterized in 2024. The sequence provides no obvious motif or domain signature that uniquely points to histidine racemase activity. Distinguishing among the three racemase options (A, B, D) requires knowing the substrate is free histidine (5.1.1) rather than an amino acid derivative (5.1.3), which is not inferable from sequence alone. Recognition of this specific protein as Q8RI81/histidine racemase is essentially a database lookup or memorization task."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "B", "D"],
    "reason": "Without knowledge of the specific substrate (histidine), options A (5.1.3.14), B (5.1.1.24), and D (5.1.3.45) are all racemases/epimerases acting on amino acids or their derivatives. The 5.1.1 vs 5.1.3 distinction (free amino acid vs. derivative) cannot be resolved from sequence alone. Option C (1.14.14.154, oxidoreductase) is clearly eliminable as a different EC class, but the remaining three are not distinguishable by general reasoning from the sequence."
  },
  "important_caveats": [
    "The histidine racemase annotation was established only in 2024 (PubMed:39424140), making this a very recent annotation unlikely to be in most training corpora.",
    "The enzyme is cofactor-independent, so the absence of PLP-binding motifs is consistent with the annotation but does not specifically identify histidine as the substrate.",
    "The UniProt entry was first released in April 2025 (entry version 81); the historical version 79 (January 2026) already contains the EC 5.1.1.24 annotation with experimental evidence.",
    "The reviewer evidence confirms sequence match (SHA256) between the benchmark input and UniProt Q8RI81.",
    "The identity of the protein (Q8RI81) was inferred from dataset metadata not available to the evaluated model."
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

**Accession:** `Q8RI81` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 79. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8RI81.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:25.407556+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"39424140","source":"PubMed"}],"value":"5.1.1.24"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"39424140","source":"PubMed"}],"value":"Histidine racemase"}}}
```

Source SHA-256: `0b210dc9bf403c4b7aabdf6972f59e66a6825c5dadefc8b002828f6d21b33d6b`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8RI81.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:25.407556+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"5.1.1.24","evidences":[{"evidenceCode":"ECO:0000269","id":"39424140","source":"PubMed"}],"name":"L-histidine = D-histidine","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:59188"},{"database":"ChEBI","id":"CHEBI:57595"},{"database":"ChEBI","id":"CHEBI:142967"}]}}
```

Source SHA-256: `0b210dc9bf403c4b7aabdf6972f59e66a6825c5dadefc8b002828f6d21b33d6b`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8RI81.json)  
**Locator:** `/references/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:25.407556+00:00.  

```json
{"citation":{"authors":["Lamer T.","Chen P.","Venter M.J.","van Belkum M.J.","Wijewardane A.","Wu C.","Lemieux M.J.","Vederas J.C."],"citationCrossReferences":[{"database":"PubMed","id":"39424140"},{"database":"DOI","id":"10.1016/j.jbc.2024.107896"}],"citationType":"journal article","firstPage":"107896","id":"39424140","journal":"J. Biol. Chem.","lastPage":"107896","publicationDate":"2024","title":"Discovery, characterization, and structure of a cofactor-independent histidine racemase from the oral pathogen Fusobacterium nucleatum.","volume":"300"},"evidences":[{"evidenceCode":"ECO:0007744","id":"9CR1","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"9CR6","source":"PDB"}],"referenceComments":[{"type":"STRAIN","value":"ATCC 25586 / DSM 15643 / BCRC 10681 / CIP 101130 / JCM 8532 / KCTC 2640 / LMG 13131 / VPI 4355"}],"referenceNumber":3,"referencePositions":["X-RAY CRYSTALLOGRAPHY (2.5 ANGSTROMS) OF MUTANTS SER-67 AND SER-209","FUNCTION","CATALYTIC ACTIVITY","ACTIVITY REGULATION","BIOPHYSICOCHEMICAL PROPERTIES","SUBUNIT","ACTIVE SITE","MUTAGENESIS OF CYS-67 AND CYS-209"]}
```

Source SHA-256: `0b210dc9bf403c4b7aabdf6972f59e66a6825c5dadefc8b002828f6d21b33d6b`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8RI81?format=txt&versions=79)  
**Locator:** `lines 6-7`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 79 / 1.  
**Retrieved:** 2026-11-01T06:28:41.693468+00:00.  

```text
DE   RecName: Full=Histidine racemase {ECO:0000303|PubMed:39424140};
DE            EC=5.1.1.24 {ECO:0000269|PubMed:39424140};
```

Source SHA-256: `c6b9df06883840dd205917d83d0a4b738a80a6e8becaecd06bbb78bb24df9da2`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8RI81?format=txt&versions=79)  
**Locator:** `lines 36-47`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 79 / 1.  
**Retrieved:** 2026-11-01T06:28:41.693468+00:00.  

```text
RN   [3] {ECO:0007744|PDB:9CR1, ECO:0007744|PDB:9CR6}
RP   X-RAY CRYSTALLOGRAPHY (2.5 ANGSTROMS) OF MUTANTS SER-67 AND SER-209,
RP   FUNCTION, CATALYTIC ACTIVITY, ACTIVITY REGULATION, BIOPHYSICOCHEMICAL
RP   PROPERTIES, SUBUNIT, ACTIVE SITE, AND MUTAGENESIS OF CYS-67 AND CYS-209.
RC   STRAIN=ATCC 25586 / DSM 15643 / BCRC 10681 / CIP 101130 / JCM 8532 / KCTC
RC   2640 / LMG 13131 / VPI 4355;
RX   PubMed=39424140; DOI=10.1016/j.jbc.2024.107896;
RA   Lamer T., Chen P., Venter M.J., van Belkum M.J., Wijewardane A., Wu C.,
RA   Lemieux M.J., Vederas J.C.;
RT   "Discovery, characterization, and structure of a cofactor-independent
RT   histidine racemase from the oral pathogen Fusobacterium nucleatum.";
RL   J. Biol. Chem. 300:107896-107896(2024).
```

Source SHA-256: `c6b9df06883840dd205917d83d0a4b738a80a6e8becaecd06bbb78bb24df9da2`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8RI81?format=txt&versions=79)  
**Locator:** `lines 55-58`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 79 / 1.  
**Retrieved:** 2026-11-01T06:28:41.693468+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=L-histidine = D-histidine; Xref=Rhea:RHEA:59188,
CC         ChEBI:CHEBI:57595, ChEBI:CHEBI:142967; EC=5.1.1.24;
CC         Evidence={ECO:0000269|PubMed:39424140};
```

Source SHA-256: `c6b9df06883840dd205917d83d0a4b738a80a6e8becaecd06bbb78bb24df9da2`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 187. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
