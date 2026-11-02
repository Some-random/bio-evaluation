# EC_number_0098

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `EC_number`  
**Author expected answer:** **A** — 3.1.1.4

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MHALRSSVLALWLCLHVSVRAWMTYRSANGLDEYEPEDRIIFLGTKWCGNGNVAEGPEDLGPLKETDACCREHDMCPDLIAAGQSKHGLTNTASYTRLNCGCDEKFYNCLKNSAETGSGAVRFTYFTVLGTKCYRNEHPLICVKKGWFSCSKYELDKSQPKRYQWFDVSSNFAFPRMLT

[Multiple Choices]
A. 3.1.1.4
B. 3.1.3.16
C. 3.2.1.8
D. 1.5.1.32
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

> The exact sequence matches the UniProt entry annotated as phospholipase A2 with EC 3.1.1.4 in both current and archived records. The annotation is computationally supported: the EC assignment cites transfer from a related UniProt entry and a PROSITE-ProRule, not a direct enzyme assay in the supplied evidence.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The N-terminal hydrophobic signal peptide and small, cysteine-rich mature protein are consistent with a secreted, disulfide-rich venom phospholipase A2. That sequence/context gives a meaningful basis to prefer A over the listed phosphatase, glycosidase, and oxidoreductase alternatives.


**Missing item-specific fact**

> No item-specific fact is essential to distinguish these widely different choices from the sequence clues, although a direct activity assay would be needed to establish the precise catalytic activity experimentally.


**Reason**

> The sequence provides biologically relevant clues for the enzyme family and the alternatives are substantially different enzyme types. Reviewer-only database annotation corroborates the key but is not needed as input for the discrimination.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The sequence and secretion context favor phospholipase A2 among the options; no other listed choice is comparably supported.


### Important caveats

- The sequence match and database EC assignment support the expected answer, but the cited annotation evidence is computational or transferred rather than direct experimental confirmation of this protein's catalytic activity.
- The reviewer-only accession and annotations were not supplied to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal hydrophobic signal peptide and small, cysteine-rich mature protein are consistent with a secreted, disulfide-rich venom phospholipase A2. That sequence/context gives a meaningful basis to prefer A over the listed phosphatase, glycosidase, and oxidoreductase alternatives.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "No item-specific fact is essential to distinguish these widely different choices from the sequence clues, although a direct activity assay would be needed to establish the precise catalytic activity experimentally.",
    "reason": "The sequence provides biologically relevant clues for the enzyme family and the alternatives are substantially different enzyme types. Reviewer-only database annotation corroborates the key but is not needed as input for the discrimination."
  },
  "case_id": "EC_number_0098",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry annotated as phospholipase A2 with EC 3.1.1.4 in both current and archived records. The annotation is computationally supported: the EC assignment cites transfer from a related UniProt entry and a PROSITE-ProRule, not a direct enzyme assay in the supplied evidence."
  },
  "important_caveats": [
    "The sequence match and database EC assignment support the expected answer, but the cited annotation evidence is computational or transferred rather than direct experimental confirmation of this protein's catalytic activity.",
    "The reviewer-only accession and annotations were not supplied to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence and secretion context favor phospholipase A2 among the options; no other listed choice is comparably supported."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0098",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry annotated as phospholipase A2 with EC 3.1.1.4 in both current and archived records. The annotation is computationally supported: the EC assignment cites transfer from a related UniProt entry and a PROSITE-ProRule, not a direct enzyme assay in the supplied evidence.",
    "evidence_ids": ["C1", "C4", "C5", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The N-terminal hydrophobic signal peptide and small, cysteine-rich mature protein are consistent with a secreted, disulfide-rich venom phospholipase A2. That sequence/context gives a meaningful basis to prefer A over the listed phosphatase, glycosidase, and oxidoreductase alternatives.",
    "missing_item_specific_fact": "No item-specific fact is essential to distinguish these widely different choices from the sequence clues, although a direct activity assay would be needed to establish the precise catalytic activity experimentally.",
    "reason": "The sequence provides biologically relevant clues for the enzyme family and the alternatives are substantially different enzyme types. Reviewer-only database annotation corroborates the key but is not needed as input for the discrimination."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence and secretion context favor phospholipase A2 among the options; no other listed choice is comparably supported."
  },
  "important_caveats": [
    "The sequence match and database EC assignment support the expected answer, but the cited annotation evidence is computational or transferred rather than direct experimental confirmation of this protein's catalytic activity.",
    "The reviewer-only accession and annotations were not supplied to the evaluated model."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence matches UniProt P0DXZ6 (PA2_XYLAR) from Xylocopa aruana, annotated as Phospholipase A2 with EC 3.1.1.4. However, the EC annotation relies on similarity transfer (ECO:0000250|UniProtKB:P00630) and PROSITE-ProRule pattern matching (ECO:0000255|PRU10035), not direct enzymatic assay. The protein was identified by mass spectrometry from venom gland tissue (PubMed:36550366). The sequence contains canonical sPLA2 motifs (GTKCGNG at ~pos 30, NCGCDE loop, VLGTKCYRNEH region) consistent with the annotation. The expected answer is supported by database annotation of computational origin.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H1](#evidence-h1), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains multiple hallmark features of secreted phospholipase A2: (1) an N-terminal hydrophobic signal peptide indicating a secreted protein; (2) the 'GTKCGNG' motif at positions ~30-36, a well-known sPLA2 superfamily signature encompassing the catalytic calcium-binding loop; (3) a highly cysteine-rich mature domain (~12 Cys) forming the characteristic 6-7 disulfide bonds of sPLA2; (4) the conserved His-Asp catalytic dyad region (visible in 'NCGCDEKF' and 'CYRNEH' segments). These features collectively identify the enzyme as a phospholipase A2 (EC 3.1.1.4). The distractors represent entirely different enzyme classes: B (phosphoprotein phosphatase, EC 3.1.3.16) requires a different catalytic architecture; C (xylanase, EC 3.2.1.8) is a glycosyl hydrolase with unrelated folds; D (methylenetetrahydrofolate reductase, EC 1.5.1.32) is an FAD-dependent oxidoreductase. None of these classes share the small secreted cysteine-rich architecture or the GTKCGNG signature.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The PLA2 signature motif (GTKCGNG), the disulfide-rich small secreted protein architecture, and the catalytic His/Asp dyad are general biochemistry knowledge about one of the most well-characterized enzyme families. The distractors are from unrelated enzyme classes with incompatible structural features. A model with standard enzymology knowledge can distinguish the answer from the sequence without needing a specific database lookup.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Only EC 3.1.1.4 (PLA2) is consistent with the sequence's structural motifs. The other three options belong to enzyme classes (phosphatase, glycosidase, oxidoreductase) whose catalytic architectures are fundamentally incompatible with the observed cysteine-rich small secreted protein containing the GTKCGNG signature.


### Important caveats

- The UniProt EC annotation is computational: ECO:0000250 (similarity to P00630) and ECO:0000255 (PROSITE-ProRule pattern). No direct enzymatic activity assay for this specific Xylocopa aruana protein is cited in the annotation.
- The protein was identified by mass spectrometry from venom gland tissue, confirming its presence and tissue origin but not its catalytic specificity experimentally.
- The entry was first published 2025-02-05; the historical annotation at entry version 4 (released 2026-01-28) already carries the same EC assignment.
- The 'GTKCGNG' motif recognition, while well-established in biochemistry, is a specific pattern-matching step rather than pure first-principles deduction.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains multiple hallmark features of secreted phospholipase A2: (1) an N-terminal hydrophobic signal peptide indicating a secreted protein; (2) the 'GTKCGNG' motif at positions ~30-36, a well-known sPLA2 superfamily signature encompassing the catalytic calcium-binding loop; (3) a highly cysteine-rich mature domain (~12 Cys) forming the characteristic 6-7 disulfide bonds of sPLA2; (4) the conserved His-Asp catalytic dyad region (visible in 'NCGCDEKF' and 'CYRNEH' segments). These features collectively identify the enzyme as a phospholipase A2 (EC 3.1.1.4). The distractors represent entirely different enzyme classes: B (phosphoprotein phosphatase, EC 3.1.3.16) requires a different catalytic architecture; C (xylanase, EC 3.2.1.8) is a glycosyl hydrolase with unrelated folds; D (methylenetetrahydrofolate reductase, EC 1.5.1.32) is an FAD-dependent oxidoreductase. None of these classes share the small secreted cysteine-rich architecture or the GTKCGNG signature.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The PLA2 signature motif (GTKCGNG), the disulfide-rich small secreted protein architecture, and the catalytic His/Asp dyad are general biochemistry knowledge about one of the most well-characterized enzyme families. The distractors are from unrelated enzyme classes with incompatible structural features. A model with standard enzymology knowledge can distinguish the answer from the sequence without needing a specific database lookup."
  },
  "case_id": "EC_number_0098",
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
    "reason": "The sequence matches UniProt P0DXZ6 (PA2_XYLAR) from Xylocopa aruana, annotated as Phospholipase A2 with EC 3.1.1.4. However, the EC annotation relies on similarity transfer (ECO:0000250|UniProtKB:P00630) and PROSITE-ProRule pattern matching (ECO:0000255|PRU10035), not direct enzymatic assay. The protein was identified by mass spectrometry from venom gland tissue (PubMed:36550366). The sequence contains canonical sPLA2 motifs (GTKCGNG at ~pos 30, NCGCDE loop, VLGTKCYRNEH region) consistent with the annotation. The expected answer is supported by database annotation of computational origin."
  },
  "important_caveats": [
    "The UniProt EC annotation is computational: ECO:0000250 (similarity to P00630) and ECO:0000255 (PROSITE-ProRule pattern). No direct enzymatic activity assay for this specific Xylocopa aruana protein is cited in the annotation.",
    "The protein was identified by mass spectrometry from venom gland tissue, confirming its presence and tissue origin but not its catalytic specificity experimentally.",
    "The entry was first published 2025-02-05; the historical annotation at entry version 4 (released 2026-01-28) already carries the same EC assignment.",
    "The 'GTKCGNG' motif recognition, while well-established in biochemistry, is a specific pattern-matching step rather than pure first-principles deduction."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only EC 3.1.1.4 (PLA2) is consistent with the sequence's structural motifs. The other three options belong to enzyme classes (phosphatase, glycosidase, oxidoreductase) whose catalytic architectures are fundamentally incompatible with the observed cysteine-rich small secreted protein containing the GTKCGNG signature."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0098",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches UniProt P0DXZ6 (PA2_XYLAR) from Xylocopa aruana, annotated as Phospholipase A2 with EC 3.1.1.4. However, the EC annotation relies on similarity transfer (ECO:0000250|UniProtKB:P00630) and PROSITE-ProRule pattern matching (ECO:0000255|PRU10035), not direct enzymatic assay. The protein was identified by mass spectrometry from venom gland tissue (PubMed:36550366). The sequence contains canonical sPLA2 motifs (GTKCGNG at ~pos 30, NCGCDE loop, VLGTKCYRNEH region) consistent with the annotation. The expected answer is supported by database annotation of computational origin.",
    "evidence_ids": ["C1", "C4", "C5", "H1", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains multiple hallmark features of secreted phospholipase A2: (1) an N-terminal hydrophobic signal peptide indicating a secreted protein; (2) the 'GTKCGNG' motif at positions ~30-36, a well-known sPLA2 superfamily signature encompassing the catalytic calcium-binding loop; (3) a highly cysteine-rich mature domain (~12 Cys) forming the characteristic 6-7 disulfide bonds of sPLA2; (4) the conserved His-Asp catalytic dyad region (visible in 'NCGCDEKF' and 'CYRNEH' segments). These features collectively identify the enzyme as a phospholipase A2 (EC 3.1.1.4). The distractors represent entirely different enzyme classes: B (phosphoprotein phosphatase, EC 3.1.3.16) requires a different catalytic architecture; C (xylanase, EC 3.2.1.8) is a glycosyl hydrolase with unrelated folds; D (methylenetetrahydrofolate reductase, EC 1.5.1.32) is an FAD-dependent oxidoreductase. None of these classes share the small secreted cysteine-rich architecture or the GTKCGNG signature.",
    "missing_item_specific_fact": "",
    "reason": "The PLA2 signature motif (GTKCGNG), the disulfide-rich small secreted protein architecture, and the catalytic His/Asp dyad are general biochemistry knowledge about one of the most well-characterized enzyme families. The distractors are from unrelated enzyme classes with incompatible structural features. A model with standard enzymology knowledge can distinguish the answer from the sequence without needing a specific database lookup."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only EC 3.1.1.4 (PLA2) is consistent with the sequence's structural motifs. The other three options belong to enzyme classes (phosphatase, glycosidase, oxidoreductase) whose catalytic architectures are fundamentally incompatible with the observed cysteine-rich small secreted protein containing the GTKCGNG signature."
  },
  "important_caveats": [
    "The UniProt EC annotation is computational: ECO:0000250 (similarity to P00630) and ECO:0000255 (PROSITE-ProRule pattern). No direct enzymatic activity assay for this specific Xylocopa aruana protein is cited in the annotation.",
    "The protein was identified by mass spectrometry from venom gland tissue, confirming its presence and tissue origin but not its catalytic specificity experimentally.",
    "The entry was first published 2025-02-05; the historical annotation at entry version 4 (released 2026-01-28) already carries the same EC assignment.",
    "The 'GTKCGNG' motif recognition, while well-established in biochemistry, is a specific pattern-matching step rather than pure first-principles deduction."
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

**Accession:** `P0DXZ6` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 4. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXZ6.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:59.679483+00:00.  

```json
"P0DXZ6"
```

Source SHA-256: `a4a3642c25c1c2414c3d78cd3e1fc44c8a083a58364446defb8748c41e68c974`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXZ6.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:59.679483+00:00.  

```json
{"alternativeNames":[{"fullName":{"value":"Phosphatidylcholine 2-acylhydrolase"}}],"flag":"Precursor","recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"P00630","source":"UniProtKB"}],"value":"3.1.1.4"}],"fullName":{"value":"Phospholipase A2"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"PA2"},{"evidences":[{"evidenceCode":"ECO:0000303","id":"36550366","source":"PubMed"}],"value":"PLA2"}]}}
```

Source SHA-256: `a4a3642c25c1c2414c3d78cd3e1fc44c8a083a58364446defb8748c41e68c974`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXZ6.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:59.679483+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"3.1.1.4","evidences":[{"evidenceCode":"ECO:0000255","id":"PRU10035","source":"PROSITE-ProRule"}],"name":"a 1,2-diacyl-sn-glycero-3-phosphocholine + H2O = a 1-acyl-sn-glycero-3-phosphocholine + a fatty acid + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:15801"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:28868"},{"database":"ChEBI","id":"CHEBI:57643"},{"database":"ChEBI","id":"CHEBI:58168"}]}}
```

Source SHA-256: `a4a3642c25c1c2414c3d78cd3e1fc44c8a083a58364446defb8748c41e68c974`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXZ6?format=txt&versions=4)  
**Locator:** `lines 1-16`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 4 / 1.  
**Retrieved:** 2026-11-02T04:30:01.445083+00:00.  

```text
ID   PA2_XYLAR               Reviewed;         179 AA.
AC   P0DXZ6;
DT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.
DT   05-FEB-2025, sequence version 1.
DT   28-JAN-2026, entry version 4.
DE   RecName: Full=Phospholipase A2;
DE            Short=PA2 {ECO:0000305};
DE            Short=PLA2 {ECO:0000303|PubMed:36550366};
DE            EC=3.1.1.4 {ECO:0000250|UniProtKB:P00630};
DE   AltName: Full=Phosphatidylcholine 2-acylhydrolase;
DE   Flags: Precursor;
OS   Xylocopa aruana (Great carpenter bee).
OC   Eukaryota; Metazoa; Ecdysozoa; Arthropoda; Hexapoda; Insecta; Pterygota;
OC   Neoptera; Endopterygota; Hymenoptera; Apocrita; Aculeata; Apoidea;
OC   Anthophila; Apidae; Xylocopa; Koptortosoma.
OX   NCBI_TaxID=135674;
```

Source SHA-256: `ce685ee2cfb313cb4868e922c2f9afc26dee98c65065d4d9d113b9c37eab4c1a`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXZ6?format=txt&versions=4)  
**Locator:** `lines 6-11`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 4 / 1.  
**Retrieved:** 2026-11-02T04:30:01.445083+00:00.  

```text
DE   RecName: Full=Phospholipase A2;
DE            Short=PA2 {ECO:0000305};
DE            Short=PLA2 {ECO:0000303|PubMed:36550366};
DE            EC=3.1.1.4 {ECO:0000250|UniProtKB:P00630};
DE   AltName: Full=Phosphatidylcholine 2-acylhydrolase;
DE   Flags: Precursor;
```

Source SHA-256: `ce685ee2cfb313cb4868e922c2f9afc26dee98c65065d4d9d113b9c37eab4c1a`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXZ6?format=txt&versions=4)  
**Locator:** `lines 35-40`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 4 / 1.  
**Retrieved:** 2026-11-02T04:30:01.445083+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=a 1,2-diacyl-sn-glycero-3-phosphocholine + H2O = a 1-acyl-sn-
CC         glycero-3-phosphocholine + a fatty acid + H(+); Xref=Rhea:RHEA:15801,
CC         ChEBI:CHEBI:15377, ChEBI:CHEBI:15378, ChEBI:CHEBI:28868,
CC         ChEBI:CHEBI:57643, ChEBI:CHEBI:58168; EC=3.1.1.4;
CC         Evidence={ECO:0000255|PROSITE-ProRule:PRU10035};
```

Source SHA-256: `ce685ee2cfb313cb4868e922c2f9afc26dee98c65065d4d9d113b9c37eab4c1a`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 98. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
