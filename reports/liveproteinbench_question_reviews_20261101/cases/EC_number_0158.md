# EC_number_0158

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `EC_number`  
**Author expected answer:** **A** — 5.2.1.8

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MPNPKVFFDMTIGGQPAGRIVMELYADVTPSTAENFRALCTGEKGAGRSGKPLHYKGSSFHRVIPNFMCQGGDFTAGNGTGGESIYGAKFADENFVKKHTGPGILSMANAGPGTNGSQFFICTTKTEWLDGKHVVFGQVVEGMDVVKEIEKVGSSSGRTAKPVVVADCGQLS

[Multiple Choices]
A. 5.2.1.8
B. 5.1.3.45
C. 1.1.1.440
D. 2.7.7.80
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

> The sequence exactly matches the UniProt entry annotated as peptidyl-prolyl cis-trans isomerase with EC 5.2.1.8. The annotation is transferred by similarity (ECO:0000250), not direct experimental evidence for this protein.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H1](#evidence-h1), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The short, compact sequence is consistent with the cyclophilin family, whose characteristic function is peptidyl-prolyl cis-trans isomerization. That function corresponds to 5.2.1.8; the other options describe different reaction classes.


**Missing item-specific fact**

> No item-specific database annotation is required for a family-level inference, although the exact protein's function is not experimentally established by the supplied input.


**Reason**

> Sequence-family recognition and the reaction classes represented by the choices provide meaningful grounds to favor the cyclophilin-associated EC number; this is more than recalling the exact sequence's database entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The listed alternatives correspond to distinct reaction classes, and the sequence supports a cyclophilin-family assignment.


### Important caveats

- The reviewer-only UniProt annotation applies to the exact sequence but assigns the EC number by similarity to another UniProt entry.
- The supplied sequence alone does not establish direct experimental characterization of this protein's catalytic activity.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The short, compact sequence is consistent with the cyclophilin family, whose characteristic function is peptidyl-prolyl cis-trans isomerization. That function corresponds to 5.2.1.8; the other options describe different reaction classes.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "No item-specific database annotation is required for a family-level inference, although the exact protein's function is not experimentally established by the supplied input.",
    "reason": "Sequence-family recognition and the reaction classes represented by the choices provide meaningful grounds to favor the cyclophilin-associated EC number; this is more than recalling the exact sequence's database entry."
  },
  "case_id": "EC_number_0158",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H1",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The sequence exactly matches the UniProt entry annotated as peptidyl-prolyl cis-trans isomerase with EC 5.2.1.8. The annotation is transferred by similarity (ECO:0000250), not direct experimental evidence for this protein."
  },
  "important_caveats": [
    "The reviewer-only UniProt annotation applies to the exact sequence but assigns the EC number by similarity to another UniProt entry.",
    "The supplied sequence alone does not establish direct experimental characterization of this protein's catalytic activity."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The listed alternatives correspond to distinct reaction classes, and the sequence supports a cyclophilin-family assignment."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0158",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence exactly matches the UniProt entry annotated as peptidyl-prolyl cis-trans isomerase with EC 5.2.1.8. The annotation is transferred by similarity (ECO:0000250), not direct experimental evidence for this protein.",
    "evidence_ids": ["C1", "C4", "C5", "H1", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The short, compact sequence is consistent with the cyclophilin family, whose characteristic function is peptidyl-prolyl cis-trans isomerization. That function corresponds to 5.2.1.8; the other options describe different reaction classes.",
    "missing_item_specific_fact": "No item-specific database annotation is required for a family-level inference, although the exact protein's function is not experimentally established by the supplied input.",
    "reason": "Sequence-family recognition and the reaction classes represented by the choices provide meaningful grounds to favor the cyclophilin-associated EC number; this is more than recalling the exact sequence's database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The listed alternatives correspond to distinct reaction classes, and the sequence supports a cyclophilin-family assignment."
  },
  "important_caveats": [
    "The reviewer-only UniProt annotation applies to the exact sequence but assigns the EC number by similarity to another UniProt entry.",
    "The supplied sequence alone does not establish direct experimental characterization of this protein's catalytic activity."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry A0A0R0H9T5 (CYP2_SOYBN, Glycine max Cyclophilin 2) is annotated with EC 5.2.1.8. The benchmark sequence (172 aa) matches the UniProt sequence exactly (SHA-256 confirmed). The annotation is transferred by similarity (ECO:0000250) from P62937 (human cyclophilin A) and O49886, which are well-characterized peptidyl-prolyl cis-trans isomerases. The catalytic activity comment (C5, H3) confirms the reaction: &#91;protein&#93;-peptidylproline (omega=180) = &#91;protein&#93;-peptidylproline (omega=0), EC 5.2.1.8. The annotation is computational/similarity-based rather than directly experimental, but the cyclophilin family assignment is robust.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains hallmark cyclophilin-domain motifs: the 'FRALCTGEKG' signature (residues ~30-39), 'FMCQGGDFT' region, and 'GILSMANAGP' motif, all diagnostic of the cyclophilin (PPIase A) fold. A knowledgeable biochemist recognizing these motifs can identify the protein as a cyclophilin-type peptidyl-prolyl cis-trans isomerase. This maps to EC class 5.2 (cis-trans isomerases), sub-subclass 5.2.1 (peptidyl-prolyl isomerases). Among the four choices, only A (5.2.1.8) falls in EC class 5.2; the distractors are from entirely different top-level classes: B (5.1.3.45, racemase/epimerase), C (1.1.1.440, oxidoreductase), D (2.7.7.80, transferase). Recognizing the cyclophilin fold from sequence motifs is a concrete structural-biology argument that eliminates all non-5.2 choices.


**Missing item-specific fact**

> Distinguishing cyclophilin-type PPIase (EC 5.2.1.8) from FKBP-type PPIase (EC 5.2.1.1) or other PPIase subtypes requires knowing the specific EC assignment for the cyclophilin family. However, since only one 5.2.x.x option is presented, this distinction is not needed to select the correct answer.


**Reason**

> The cyclophilin domain motifs are identifiable from the sequence itself, and the EC-class-level elimination of distractors (oxidoreductase, transferase, epimerase) follows from general enzyme-classification knowledge. The reasoning chain—recognize cyclophilin fold → PPIase activity → EC 5.2.x.x → only option A—is grounded in the supplied sequence and standard biochemistry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four choices span three different top-level EC classes (1, 2, 5). Only A belongs to EC class 5.2 (cis-trans isomerases), which is the correct class for peptidyl-prolyl cis-trans isomerases. No other option is defensible for a cyclophilin-domain protein.


### Important caveats

- The EC 5.2.1.8 annotation in UniProt is inferred by similarity (ECO:0000250) from human cyclophilin A (P62937) and another reference (O49886), not from direct experimental characterization of the soybean protein itself.
- The reviewer-only evidence was absent from the evaluated model input; the model must rely on sequence motif recognition and general enzymology knowledge.
- The distinction between cyclophilin-type (5.2.1.8) and FKBP-type (5.2.1.1) PPIases is not tested here because no FKBP-type option is provided.
- The annotation evidence code ECO:0000250 denotes computational transfer; no direct experimental assay on GmCYP2 is cited in the retrieved record.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains hallmark cyclophilin-domain motifs: the 'FRALCTGEKG' signature (residues ~30-39), 'FMCQGGDFT' region, and 'GILSMANAGP' motif, all diagnostic of the cyclophilin (PPIase A) fold. A knowledgeable biochemist recognizing these motifs can identify the protein as a cyclophilin-type peptidyl-prolyl cis-trans isomerase. This maps to EC class 5.2 (cis-trans isomerases), sub-subclass 5.2.1 (peptidyl-prolyl isomerases). Among the four choices, only A (5.2.1.8) falls in EC class 5.2; the distractors are from entirely different top-level classes: B (5.1.3.45, racemase/epimerase), C (1.1.1.440, oxidoreductase), D (2.7.7.80, transferase). Recognizing the cyclophilin fold from sequence motifs is a concrete structural-biology argument that eliminates all non-5.2 choices.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "Distinguishing cyclophilin-type PPIase (EC 5.2.1.8) from FKBP-type PPIase (EC 5.2.1.1) or other PPIase subtypes requires knowing the specific EC assignment for the cyclophilin family. However, since only one 5.2.x.x option is presented, this distinction is not needed to select the correct answer.",
    "reason": "The cyclophilin domain motifs are identifiable from the sequence itself, and the EC-class-level elimination of distractors (oxidoreductase, transferase, epimerase) follows from general enzyme-classification knowledge. The reasoning chain—recognize cyclophilin fold → PPIase activity → EC 5.2.x.x → only option A—is grounded in the supplied sequence and standard biochemistry."
  },
  "case_id": "EC_number_0158",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H1",
      "H2",
      "H3"
    ],
    "judgment": "supported",
    "reason": "UniProt entry A0A0R0H9T5 (CYP2_SOYBN, Glycine max Cyclophilin 2) is annotated with EC 5.2.1.8. The benchmark sequence (172 aa) matches the UniProt sequence exactly (SHA-256 confirmed). The annotation is transferred by similarity (ECO:0000250) from P62937 (human cyclophilin A) and O49886, which are well-characterized peptidyl-prolyl cis-trans isomerases. The catalytic activity comment (C5, H3) confirms the reaction: [protein]-peptidylproline (omega=180) = [protein]-peptidylproline (omega=0), EC 5.2.1.8. The annotation is computational/similarity-based rather than directly experimental, but the cyclophilin family assignment is robust."
  },
  "important_caveats": [
    "The EC 5.2.1.8 annotation in UniProt is inferred by similarity (ECO:0000250) from human cyclophilin A (P62937) and another reference (O49886), not from direct experimental characterization of the soybean protein itself.",
    "The reviewer-only evidence was absent from the evaluated model input; the model must rely on sequence motif recognition and general enzymology knowledge.",
    "The distinction between cyclophilin-type (5.2.1.8) and FKBP-type (5.2.1.1) PPIases is not tested here because no FKBP-type option is provided.",
    "The annotation evidence code ECO:0000250 denotes computational transfer; no direct experimental assay on GmCYP2 is cited in the retrieved record."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices span three different top-level EC classes (1, 2, 5). Only A belongs to EC class 5.2 (cis-trans isomerases), which is the correct class for peptidyl-prolyl cis-trans isomerases. No other option is defensible for a cyclophilin-domain protein."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0158",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry A0A0R0H9T5 (CYP2_SOYBN, Glycine max Cyclophilin 2) is annotated with EC 5.2.1.8. The benchmark sequence (172 aa) matches the UniProt sequence exactly (SHA-256 confirmed). The annotation is transferred by similarity (ECO:0000250) from P62937 (human cyclophilin A) and O49886, which are well-characterized peptidyl-prolyl cis-trans isomerases. The catalytic activity comment (C5, H3) confirms the reaction: [protein]-peptidylproline (omega=180) = [protein]-peptidylproline (omega=0), EC 5.2.1.8. The annotation is computational/similarity-based rather than directly experimental, but the cyclophilin family assignment is robust.",
    "evidence_ids": ["C4", "C5", "H1", "H2", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains hallmark cyclophilin-domain motifs: the 'FRALCTGEKG' signature (residues ~30-39), 'FMCQGGDFT' region, and 'GILSMANAGP' motif, all diagnostic of the cyclophilin (PPIase A) fold. A knowledgeable biochemist recognizing these motifs can identify the protein as a cyclophilin-type peptidyl-prolyl cis-trans isomerase. This maps to EC class 5.2 (cis-trans isomerases), sub-subclass 5.2.1 (peptidyl-prolyl isomerases). Among the four choices, only A (5.2.1.8) falls in EC class 5.2; the distractors are from entirely different top-level classes: B (5.1.3.45, racemase/epimerase), C (1.1.1.440, oxidoreductase), D (2.7.7.80, transferase). Recognizing the cyclophilin fold from sequence motifs is a concrete structural-biology argument that eliminates all non-5.2 choices.",
    "missing_item_specific_fact": "Distinguishing cyclophilin-type PPIase (EC 5.2.1.8) from FKBP-type PPIase (EC 5.2.1.1) or other PPIase subtypes requires knowing the specific EC assignment for the cyclophilin family. However, since only one 5.2.x.x option is presented, this distinction is not needed to select the correct answer.",
    "reason": "The cyclophilin domain motifs are identifiable from the sequence itself, and the EC-class-level elimination of distractors (oxidoreductase, transferase, epimerase) follows from general enzyme-classification knowledge. The reasoning chain—recognize cyclophilin fold → PPIase activity → EC 5.2.x.x → only option A—is grounded in the supplied sequence and standard biochemistry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices span three different top-level EC classes (1, 2, 5). Only A belongs to EC class 5.2 (cis-trans isomerases), which is the correct class for peptidyl-prolyl cis-trans isomerases. No other option is defensible for a cyclophilin-domain protein."
  },
  "important_caveats": [
    "The EC 5.2.1.8 annotation in UniProt is inferred by similarity (ECO:0000250) from human cyclophilin A (P62937) and another reference (O49886), not from direct experimental characterization of the soybean protein itself.",
    "The reviewer-only evidence was absent from the evaluated model input; the model must rely on sequence motif recognition and general enzymology knowledge.",
    "The distinction between cyclophilin-type (5.2.1.8) and FKBP-type (5.2.1.1) PPIases is not tested here because no FKBP-type option is provided.",
    "The annotation evidence code ECO:0000250 denotes computational transfer; no direct experimental assay on GmCYP2 is cited in the retrieved record."
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

**Accession:** `A0A0R0H9T5` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 51. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0R0H9T5.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:20.433774+00:00.  

```json
"A0A0R0H9T5"
```

Source SHA-256: `f7f163e0c9917e55f2d65f7bb18771151c70abedc4d5d7bc728cc814cefd22ba`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0R0H9T5.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:20.433774+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"Ref.2","source":"Reference"}],"value":"Cyclophilin 2"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"Ref.2","source":"Reference"}],"value":"GmCYP2"}]}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"P62937","source":"UniProtKB"}],"value":"5.2.1.8"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000250","id":"O49886","source":"UniProtKB"}],"value":"Peptidyl-prolyl cis-trans isomerase 2"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"O49886","source":"UniProtKB"}],"value":"PPIase 2"}]}}
```

Source SHA-256: `f7f163e0c9917e55f2d65f7bb18771151c70abedc4d5d7bc728cc814cefd22ba`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0R0H9T5.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:20.433774+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"5.2.1.8","evidences":[{"evidenceCode":"ECO:0000250","id":"P62937","source":"UniProtKB"}],"name":"[protein]-peptidylproline (omega=180) = [protein]-peptidylproline (omega=0)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:16237"},{"database":"Rhea","id":"RHEA-COMP:10747"},{"database":"Rhea","id":"RHEA-COMP:10748"},{"database":"ChEBI","id":"CHEBI:83833"},{"database":"ChEBI","id":"CHEBI:83834"}]}}
```

Source SHA-256: `f7f163e0c9917e55f2d65f7bb18771151c70abedc4d5d7bc728cc814cefd22ba`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0R0H9T5?format=txt&versions=51)  
**Locator:** `lines 1-19`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 51 / 1.  
**Retrieved:** 2026-11-02T04:24:22.440712+00:00.  

```text
ID   CYP2_SOYBN              Reviewed;         172 AA.
AC   A0A0R0H9T5;
DT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.
DT   20-JAN-2016, sequence version 1.
DT   28-JAN-2026, entry version 51.
DE   RecName: Full=Peptidyl-prolyl cis-trans isomerase 2 {ECO:0000250|UniProtKB:O49886};
DE            Short=PPIase 2 {ECO:0000250|UniProtKB:O49886};
DE            EC=5.2.1.8 {ECO:0000250|UniProtKB:P62937};
DE   AltName: Full=Cyclophilin 2 {ECO:0000303|Ref.2};
DE            Short=GmCYP2 {ECO:0000303|Ref.2};
GN   Name=CYP2 {ECO:0000303|Ref.2};
GN   ORFNames=GLYMA_12G024700 {ECO:0000312|EMBL:KRH24153.1};
OS   Glycine max (Soybean) (Glycine hispida).
OC   Eukaryota; Viridiplantae; Streptophyta; Embryophyta; Tracheophyta;
OC   Spermatophyta; Magnoliopsida; eudicotyledons; Gunneridae; Pentapetalae;
OC   rosids; fabids; Fabales; Fabaceae; Papilionoideae; 50 kb inversion clade;
OC   NPAAA clade; indigoferoid/millettioid clade; Phaseoleae; Glycine;
OC   Glycine subgen. Soja.
OX   NCBI_TaxID=3847;
```

Source SHA-256: `8a831b41ee7356d273422a7e40a6b035b2f08ac1f009b688f9f6f295b13e7e66`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0R0H9T5?format=txt&versions=51)  
**Locator:** `lines 6-10`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 51 / 1.  
**Retrieved:** 2026-11-02T04:24:22.440712+00:00.  

```text
DE   RecName: Full=Peptidyl-prolyl cis-trans isomerase 2 {ECO:0000250|UniProtKB:O49886};
DE            Short=PPIase 2 {ECO:0000250|UniProtKB:O49886};
DE            EC=5.2.1.8 {ECO:0000250|UniProtKB:P62937};
DE   AltName: Full=Cyclophilin 2 {ECO:0000303|Ref.2};
DE            Short=GmCYP2 {ECO:0000303|Ref.2};
```

Source SHA-256: `8a831b41ee7356d273422a7e40a6b035b2f08ac1f009b688f9f6f295b13e7e66`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0R0H9T5?format=txt&versions=51)  
**Locator:** `lines 50-55`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 51 / 1.  
**Retrieved:** 2026-11-02T04:24:22.440712+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=[protein]-peptidylproline (omega=180) = [protein]-
CC         peptidylproline (omega=0); Xref=Rhea:RHEA:16237, Rhea:RHEA-
CC         COMP:10747, Rhea:RHEA-COMP:10748, ChEBI:CHEBI:83833,
CC         ChEBI:CHEBI:83834; EC=5.2.1.8;
CC         Evidence={ECO:0000250|UniProtKB:P62937};
```

Source SHA-256: `8a831b41ee7356d273422a7e40a6b035b2f08ac1f009b688f9f6f295b13e7e66`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 158. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
