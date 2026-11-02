# EC_number_0076

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `EC_number`  
**Author expected answer:** **C** — 5.4.99.14

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | invalid_review |

**Paired comparison:** not comparable: one or both reviews invalid or missing. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MIRILYLLVKPESMSHEQFRKECVVHFQMSAGMPGLHKYEVRLVAGNPTDTHVPYLDVGRIDAIGECWFASEEQYQVYMESDIRKAWFEHGKYFIGQLKPFVTEELV

[Multiple Choices]
A. 5.3.1.16
B. 1.14.14.187
C. 5.4.99.14
D. 2.5.1.56
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

> The exact sequence match is annotated as EC 5.4.99.14, catalyzing the isomerization of 4-methylmuconolactone to 3-methylmuconolactone. The annotation cites experimental evidence from PubMed:19801657; an archived record available by the stated historical cutoff carries the same assignment. This supports choice C, though the primary paper was not independently reviewed here.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H3](#evidence-h3), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence and choices provide no clear biological context or sequence feature that meaningfully distinguishes this particular isomerase activity from the listed alternatives or establishes its complete EC number.


**Missing item-specific fact**

> The protein-specific function—4-carboxymethyl-4-methylbutenolide mutase activity, EC 5.4.99.14—is needed to select the answer and is absent from the question input.


**Reason**

> The key is supported by a sequence-matched database annotation citing experimental literature, but that annotation and protein-specific functional evidence are reviewer-only. Identifying the exact protein from its sequence and recalling its EC entry would be lookup or memorization, not reasoning from the supplied information.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The enzyme has a specific EC classification supported by the cited annotation, but the supplied sequence and choices alone do not establish which option is correct.


### Important caveats

- The current and historical UniProt records match the supplied sequence; the author's exact source snapshot is unknown.
- The annotation cites experimental evidence, but the primary paper was not comprehensively retrieved or independently validated.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence and choices provide no clear biological context or sequence feature that meaningfully distinguishes this particular isomerase activity from the listed alternatives or establishes its complete EC number.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific function—4-carboxymethyl-4-methylbutenolide mutase activity, EC 5.4.99.14—is needed to select the answer and is absent from the question input.",
    "reason": "The key is supported by a sequence-matched database annotation citing experimental literature, but that annotation and protein-specific functional evidence are reviewer-only. Identifying the exact protein from its sequence and recalling its EC entry would be lookup or memorization, not reasoning from the supplied information."
  },
  "case_id": "EC_number_0076",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H3",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The exact sequence match is annotated as EC 5.4.99.14, catalyzing the isomerization of 4-methylmuconolactone to 3-methylmuconolactone. The annotation cites experimental evidence from PubMed:19801657; an archived record available by the stated historical cutoff carries the same assignment. This supports choice C, though the primary paper was not independently reviewed here."
  },
  "important_caveats": [
    "The current and historical UniProt records match the supplied sequence; the author's exact source snapshot is unknown.",
    "The annotation cites experimental evidence, but the primary paper was not comprehensively retrieved or independently validated."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The enzyme has a specific EC classification supported by the cited annotation, but the supplied sequence and choices alone do not establish which option is correct."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0076",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence match is annotated as EC 5.4.99.14, catalyzing the isomerization of 4-methylmuconolactone to 3-methylmuconolactone. The annotation cites experimental evidence from PubMed:19801657; an archived record available by the stated historical cutoff carries the same assignment. This supports choice C, though the primary paper was not independently reviewed here.",
    "evidence_ids": ["C4", "C5", "H3", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence and choices provide no clear biological context or sequence feature that meaningfully distinguishes this particular isomerase activity from the listed alternatives or establishes its complete EC number.",
    "missing_item_specific_fact": "The protein-specific function—4-carboxymethyl-4-methylbutenolide mutase activity, EC 5.4.99.14—is needed to select the answer and is absent from the question input.",
    "reason": "The key is supported by a sequence-matched database annotation citing experimental literature, but that annotation and protein-specific functional evidence are reviewer-only. Identifying the exact protein from its sequence and recalling its EC entry would be lookup or memorization, not reasoning from the supplied information."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The enzyme has a specific EC classification supported by the cited annotation, but the supplied sequence and choices alone do not establish which option is correct."
  },
  "important_caveats": [
    "The current and historical UniProt records match the supplied sequence; the author's exact source snapshot is unknown.",
    "The annotation cites experimental evidence, but the primary paper was not comprehensively retrieved or independently validated."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `invalid_review`.

**This result is not a valid structured review.** Any saved labels below remain the model’s original values; they are excluded from label distributions and paired agreement. No field or option ID has been repaired.

**Validation errors:** `question_ambiguity:invalid_option_ids`.

### Expected-answer support: supported

> UniProt entry C5MR76 (MMLI_PSERE) for the exact 107-AA sequence carries EC 5.4.99.14 with experimental evidence (ECO:0000269, PubMed:19801657). The catalytic activity is explicitly annotated as '4-methylmuconolactone = 3-methylmuconolactone' (Rhea:RHEA:19237), confirmed by X-ray crystallography and enzymology. The sequence SHA256 matches the benchmark input exactly.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H5](#evidence-h5), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> While a model could potentially narrow the class to isomerases (EC 5) and eliminate B (oxidoreductase 1.14.14.187) and D (transferase 2.5.1.56) based on general sequence features, distinguishing EC 5.3.1.16 (aldose-ketose isomerase) from EC 5.4.99.14 (4-carboxymethyl-4-methylbutenolide mutase) from a bare 107-AA sequence requires specific knowledge of this obscure enzyme family involved in the modified 3-oxoadipate pathway for methylaromatic biodegradation in Pseudomonas reinekei. No well-known catalytic motif in the sequence uniquely identifies the 5.4.99 sub-subclass over 5.3.1.


**Missing item-specific fact**

> The specific identity of this protein as MMLI (4-methylmuconolactone methylisomerase) and its membership in a small, poorly characterized mutase family with active-site residues His-26, Tyr-39, His-52, Cys-67 that catalyzes a specific lactone ring isomerization (EC 5.4.99.14) rather than a generic aldose-ketose isomerization (EC 5.3.1.16). This is an item-specific database annotation not derivable from general biological reasoning on the sequence alone.


**Reason**

> The 107-AA sequence lacks a distinctive, widely recognized catalytic motif that would allow a model to reason from general biochemistry to the precise EC 5.4.99.14 assignment over EC 5.3.1.16. Both are intramolecular transferases (isomerases). Selection between them depends on recognizing this particular protein or knowing the specific reaction chemistry of 4-methylmuconolactone methylisomerase, which is an obscure enzyme first characterized in 2009.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A (5.3.1.16)",
  "C (5.4.99.14)"
]
```

> Both A and C are EC class 5 (isomerases/intramolecular transferases). Without specific knowledge of this enzyme's substrate and reaction mechanism, a model cannot reliably distinguish 5.3.1.16 from 5.4.99.14 from the sequence alone. Options B and D are more clearly eliminable as they belong to different EC top-level classes.


### Important caveats

- The EC annotation is backed by experimental evidence (ECO:0000269) from crystallographic and enzymological studies (PubMed:19801657), making the key scientifically well-supported.
- The protein is a relatively obscure enzyme (first characterized 2009) from Pseudomonas reinekei, not a textbook enzyme, reducing the likelihood that general biological reasoning alone suffices.
- The sequence is only 107 amino acids, limiting the amount of structural/functional information available for inference.
- The UniProt entry was first released in 2025 (Swiss-Prot review), meaning this annotation is relatively recent and less likely to be embedded in training data from older corpora.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "While a model could potentially narrow the class to isomerases (EC 5) and eliminate B (oxidoreductase 1.14.14.187) and D (transferase 2.5.1.56) based on general sequence features, distinguishing EC 5.3.1.16 (aldose-ketose isomerase) from EC 5.4.99.14 (4-carboxymethyl-4-methylbutenolide mutase) from a bare 107-AA sequence requires specific knowledge of this obscure enzyme family involved in the modified 3-oxoadipate pathway for methylaromatic biodegradation in Pseudomonas reinekei. No well-known catalytic motif in the sequence uniquely identifies the 5.4.99 sub-subclass over 5.3.1.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific identity of this protein as MMLI (4-methylmuconolactone methylisomerase) and its membership in a small, poorly characterized mutase family with active-site residues His-26, Tyr-39, His-52, Cys-67 that catalyzes a specific lactone ring isomerization (EC 5.4.99.14) rather than a generic aldose-ketose isomerization (EC 5.3.1.16). This is an item-specific database annotation not derivable from general biological reasoning on the sequence alone.",
    "reason": "The 107-AA sequence lacks a distinctive, widely recognized catalytic motif that would allow a model to reason from general biochemistry to the precise EC 5.4.99.14 assignment over EC 5.3.1.16. Both are intramolecular transferases (isomerases). Selection between them depends on recognizing this particular protein or knowing the specific reaction chemistry of 4-methylmuconolactone methylisomerase, which is an obscure enzyme first characterized in 2009."
  },
  "case_id": "EC_number_0076",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2",
      "H5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "UniProt entry C5MR76 (MMLI_PSERE) for the exact 107-AA sequence carries EC 5.4.99.14 with experimental evidence (ECO:0000269, PubMed:19801657). The catalytic activity is explicitly annotated as '4-methylmuconolactone = 3-methylmuconolactone' (Rhea:RHEA:19237), confirmed by X-ray crystallography and enzymology. The sequence SHA256 matches the benchmark input exactly."
  },
  "important_caveats": [
    "The EC annotation is backed by experimental evidence (ECO:0000269) from crystallographic and enzymological studies (PubMed:19801657), making the key scientifically well-supported.",
    "The protein is a relatively obscure enzyme (first characterized 2009) from Pseudomonas reinekei, not a textbook enzyme, reducing the likelihood that general biological reasoning alone suffices.",
    "The sequence is only 107 amino acids, limiting the amount of structural/functional information available for inference.",
    "The UniProt entry was first released in 2025 (Swiss-Prot review), meaning this annotation is relatively recent and less likely to be embedded in training data from older corpora."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A (5.3.1.16)",
      "C (5.4.99.14)"
    ],
    "reason": "Both A and C are EC class 5 (isomerases/intramolecular transferases). Without specific knowledge of this enzyme's substrate and reaction mechanism, a model cannot reliably distinguish 5.3.1.16 from 5.4.99.14 from the sequence alone. Options B and D are more clearly eliminable as they belong to different EC top-level classes."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0076",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry C5MR76 (MMLI_PSERE) for the exact 107-AA sequence carries EC 5.4.99.14 with experimental evidence (ECO:0000269, PubMed:19801657). The catalytic activity is explicitly annotated as '4-methylmuconolactone = 3-methylmuconolactone' (Rhea:RHEA:19237), confirmed by X-ray crystallography and enzymology. The sequence SHA256 matches the benchmark input exactly.",
    "evidence_ids": ["C4", "C5", "H2", "H5", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "While a model could potentially narrow the class to isomerases (EC 5) and eliminate B (oxidoreductase 1.14.14.187) and D (transferase 2.5.1.56) based on general sequence features, distinguishing EC 5.3.1.16 (aldose-ketose isomerase) from EC 5.4.99.14 (4-carboxymethyl-4-methylbutenolide mutase) from a bare 107-AA sequence requires specific knowledge of this obscure enzyme family involved in the modified 3-oxoadipate pathway for methylaromatic biodegradation in Pseudomonas reinekei. No well-known catalytic motif in the sequence uniquely identifies the 5.4.99 sub-subclass over 5.3.1.",
    "missing_item_specific_fact": "The specific identity of this protein as MMLI (4-methylmuconolactone methylisomerase) and its membership in a small, poorly characterized mutase family with active-site residues His-26, Tyr-39, His-52, Cys-67 that catalyzes a specific lactone ring isomerization (EC 5.4.99.14) rather than a generic aldose-ketose isomerization (EC 5.3.1.16). This is an item-specific database annotation not derivable from general biological reasoning on the sequence alone.",
    "reason": "The 107-AA sequence lacks a distinctive, widely recognized catalytic motif that would allow a model to reason from general biochemistry to the precise EC 5.4.99.14 assignment over EC 5.3.1.16. Both are intramolecular transferases (isomerases). Selection between them depends on recognizing this particular protein or knowing the specific reaction chemistry of 4-methylmuconolactone methylisomerase, which is an obscure enzyme first characterized in 2009."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A (5.3.1.16)", "C (5.4.99.14)"],
    "reason": "Both A and C are EC class 5 (isomerases/intramolecular transferases). Without specific knowledge of this enzyme's substrate and reaction mechanism, a model cannot reliably distinguish 5.3.1.16 from 5.4.99.14 from the sequence alone. Options B and D are more clearly eliminable as they belong to different EC top-level classes."
  },
  "important_caveats": [
    "The EC annotation is backed by experimental evidence (ECO:0000269) from crystallographic and enzymological studies (PubMed:19801657), making the key scientifically well-supported.",
    "The protein is a relatively obscure enzyme (first characterized 2009) from Pseudomonas reinekei, not a textbook enzyme, reducing the likelihood that general biological reasoning alone suffices.",
    "The sequence is only 107 amino acids, limiting the amount of structural/functional information available for inference.",
    "The UniProt entry was first released in 2025 (Swiss-Prot review), meaning this annotation is relatively recent and less likely to be embedded in training data from older corpora."
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

**Accession:** `C5MR76` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 66. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C5MR76.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:31.044476+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"19801657","source":"PubMed"}],"value":"4-methylmuconolactone methylisomerase"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"19801657","source":"PubMed"}],"value":"MLMI"}]}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"19801657","source":"PubMed"}],"value":"5.4.99.14"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"4-carboxymethyl-4-methylbutenolide mutase"}}}
```

Source SHA-256: `3d67557ecf827cb87e773519386698ecac17ac2714ab4e9390e7fdb2b8e1ed32`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C5MR76.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:31.044476+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000305","id":"19801657","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:19238"}}],"reaction":{"ecNumber":"5.4.99.14","evidences":[{"evidenceCode":"ECO:0000269","id":"19801657","source":"PubMed"}],"name":"4-methylmuconolactone = 3-methylmuconolactone","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:19237"},{"database":"ChEBI","id":"CHEBI:57883"},{"database":"ChEBI","id":"CHEBI:57888"}]}}
```

Source SHA-256: `3d67557ecf827cb87e773519386698ecac17ac2714ab4e9390e7fdb2b8e1ed32`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/C5MR76?format=txt&versions=66)  
**Locator:** `lines 6-9`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 66 / 1.  
**Retrieved:** 2026-11-02T04:27:34.227817+00:00.  

```text
DE   RecName: Full=4-carboxymethyl-4-methylbutenolide mutase {ECO:0000305};
DE            EC=5.4.99.14 {ECO:0000269|PubMed:19801657};
DE   AltName: Full=4-methylmuconolactone methylisomerase {ECO:0000303|PubMed:19801657};
DE            Short=MLMI {ECO:0000303|PubMed:19801657};
```

Source SHA-256: `813b0f1c8060cf8b4b09f12d8d6ff0f15ff7f1c1b402841ea0a11592eb3069aa`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/C5MR76?format=txt&versions=66)  
**Locator:** `lines 18-29`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 66 / 1.  
**Retrieved:** 2026-11-02T04:27:34.227817+00:00.  

```text
RN   [1] {ECO:0000312|EMBL:ACR82080.1, ECO:0007744|PDB:3HDS, ECO:0007744|PDB:3HF5, ECO:0007744|PDB:3HFK}
RP   NUCLEOTIDE SEQUENCE [GENOMIC DNA], X-RAY CRYSTALLOGRAPHY (1.40 ANGSTROMS)
RP   IN COMPLEX WITH 3-METHYLMUCONOLACTONE AND OF MUTANT ALA-52 IN COMPLEX WITH
RP   4-METHYLMUCONOLACTONE, FUNCTION, CATALYTIC ACTIVITY, PROPOSED REACTION
RP   MECHANISM, ACTIVITY REGULATION, BIOPHYSICOCHEMICAL PROPERTIES, SUBUNIT,
RP   DOMAIN, ACTIVE SITE, AND MUTAGENESIS OF HIS-26; TYR-39; HIS-52 AND CYS-67.
RC   STRAIN=DSM 18361 / CCUG 53116 / MT1;
RX   PubMed=19801657; DOI=10.1074/jbc.m109.024604;
RA   Marin M., Heinz D.W., Pieper D.H., Klink B.U.;
RT   "Crystal structure and catalytic mechanism of 4-methylmuconolactone
RT   methylisomerase.";
RL   J. Biol. Chem. 284:32709-32716(2009).
```

Source SHA-256: `813b0f1c8060cf8b4b09f12d8d6ff0f15ff7f1c1b402841ea0a11592eb3069aa`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/C5MR76?format=txt&versions=66)  
**Locator:** `lines 63-68`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 66 / 1.  
**Retrieved:** 2026-11-02T04:27:34.227817+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=4-methylmuconolactone = 3-methylmuconolactone;
CC         Xref=Rhea:RHEA:19237, ChEBI:CHEBI:57883, ChEBI:CHEBI:57888;
CC         EC=5.4.99.14; Evidence={ECO:0000269|PubMed:19801657};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:19238;
CC         Evidence={ECO:0000305|PubMed:19801657};
```

Source SHA-256: `813b0f1c8060cf8b4b09f12d8d6ff0f15ff7f1c1b402841ea0a11592eb3069aa`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 76. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
