# EC_number_0168

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `EC_number`  
**Author expected answer:** **C** — 3.2.1.8

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MVSYKAFLITLAAVTRVLTYPANSSFELVDRSGTPSSTGTSGGYYYSFWTDGGADVTYTNGAGGEYKLQWSGNGNLVGGKGWNPGSAKAVTYSGTYSPNGNSYLSLYGWTTSPLIEYYVVENFGTYDPSTGATLKGTVVSDGATYKIYQTQRVNQPSIIGTATFYQYWSVRQTKRTGGTVTTGNHFNAWKALGMNMGTFDYMIVATEGYFSSGSSDITVGSSTGGGDSGSPTSAPTTSPTTSPGGTCGALYSQCGGTGFTGSQCCASGTCKYANSYYSQCL

[Multiple Choices]
A. 3.2.1.20
B. 1.14.11.65
C. 3.2.1.8
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

> The exact supplied sequence matches a UniProt entry annotated as EC 3.2.1.8, an endo-1,4-beta-xylanase. The annotation is supported by a PROSITE-ProRule computational inference, not by the cited evidence as a direct experimental measurement of this sequence's catalytic activity.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H1](#evidence-h1), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The N-terminal hydrophobic segment is consistent with a secreted fungal protein, and the sequence is compatible with a carbohydrate-active enzyme. Those clues may favor a secreted glycosidase over the other enzyme classes, but they do not establish the specific substrate linkage needed to distinguish EC 3.2.1.8 from another glycosidase option.


**Missing item-specific fact**

> The protein-specific identification as EIX1 / endo-1,4-beta-xylanase, or equivalent evidence establishing its xylan substrate specificity, is absent from the input.


**Reason**

> Selecting the precise EC number depends on protein-specific functional annotation or substrate-specific evidence; broad sequence and secretion clues do not independently establish that exact catalytic activity.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The matched database annotation supports option C; the other listed EC numbers describe different reaction classes or activities.


### Important caveats

- The supporting EC annotation is computationally assigned by PROSITE-ProRule, so it should not be represented as direct experimental validation.
- The reviewer-only sequence match and database annotation were not information supplied to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal hydrophobic segment is consistent with a secreted fungal protein, and the sequence is compatible with a carbohydrate-active enzyme. Those clues may favor a secreted glycosidase over the other enzyme classes, but they do not establish the specific substrate linkage needed to distinguish EC 3.2.1.8 from another glycosidase option.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific identification as EIX1 / endo-1,4-beta-xylanase, or equivalent evidence establishing its xylan substrate specificity, is absent from the input.",
    "reason": "Selecting the precise EC number depends on protein-specific functional annotation or substrate-specific evidence; broad sequence and secretion clues do not independently establish that exact catalytic activity."
  },
  "case_id": "EC_number_0168",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H1",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact supplied sequence matches a UniProt entry annotated as EC 3.2.1.8, an endo-1,4-beta-xylanase. The annotation is supported by a PROSITE-ProRule computational inference, not by the cited evidence as a direct experimental measurement of this sequence's catalytic activity."
  },
  "important_caveats": [
    "The supporting EC annotation is computationally assigned by PROSITE-ProRule, so it should not be represented as direct experimental validation.",
    "The reviewer-only sequence match and database annotation were not information supplied to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched database annotation supports option C; the other listed EC numbers describe different reaction classes or activities."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0168",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact supplied sequence matches a UniProt entry annotated as EC 3.2.1.8, an endo-1,4-beta-xylanase. The annotation is supported by a PROSITE-ProRule computational inference, not by the cited evidence as a direct experimental measurement of this sequence's catalytic activity.",
    "evidence_ids": ["C1", "C4", "C5", "H1", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The N-terminal hydrophobic segment is consistent with a secreted fungal protein, and the sequence is compatible with a carbohydrate-active enzyme. Those clues may favor a secreted glycosidase over the other enzyme classes, but they do not establish the specific substrate linkage needed to distinguish EC 3.2.1.8 from another glycosidase option.",
    "missing_item_specific_fact": "The protein-specific identification as EIX1 / endo-1,4-beta-xylanase, or equivalent evidence establishing its xylan substrate specificity, is absent from the input.",
    "reason": "Selecting the precise EC number depends on protein-specific functional annotation or substrate-specific evidence; broad sequence and secretion clues do not independently establish that exact catalytic activity."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched database annotation supports option C; the other listed EC numbers describe different reaction classes or activities."
  },
  "important_caveats": [
    "The supporting EC annotation is computationally assigned by PROSITE-ProRule, so it should not be represented as direct experimental validation.",
    "The reviewer-only sequence match and database annotation were not information supplied to the evaluated model."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry A0A384JXV5 (EIX1_BOTFB, 281 AA, sequence SHA256 matches) annotates this protein as Ethylene-inducing xylanase 1 with EC 3.2.1.8 (Endo-1,4-beta-xylanase). The catalytic activity is stated as 'Endohydrolysis of (1->4)-beta-D-xylosidic linkages in xylans.' However, the EC assignment carries evidence code ECO:0000255|PROSITE-ProRule:PRU01097, indicating computational rule-based inference rather than direct experimental characterization of this specific protein's catalytic activity. The cited PubMed reference (33205907) concerns perception of EIX-like proteins by plant receptors, not enzymatic assay of this protein.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The protein is a small (~281 AA) secreted fungal protein with a hydrophobic N-terminal signal peptide and multiple cysteines (disulfide bonds), consistent with a plant-pathogen cell-wall-degrading enzyme. This weakly favors a xylanase (3.2.1.8) over an intracellular alpha-glucosidase (3.2.1.20). However, distinguishing specifically between EC 3.2.1.8 (GH10 endo-xylanase) and EC 3.2.1.20 (GH31/GH13 alpha-glucosidase) from raw sequence requires recognizing the GH10 beta-sandwich fold architecture and its conserved catalytic glutamate residues, which is essentially PROSITE pattern PRU01097 matching.


**Missing item-specific fact**

> The specific PROSITE-ProRule pattern PRU01097 (GH10 family signature) that assigns this sequence to endo-1,4-beta-xylanase rather than another glycosyl hydrolase family. Without this pattern or recognition of the exact sequence as EIX1 from Botrytis cinerea, the distinction between 3.2.1.8 and 3.2.1.20 cannot be made from sequence alone with confidence.


**Reason**

> The protein is clearly a glycosyl hydrolase (EC 3.2.1.x), eliminating B (oxidoreductase) and D (transferase). However, distinguishing 3.2.1.8 from 3.2.1.20 requires either (a) recognizing the GH10 fold via PROSITE patterns, (b) identifying this exact sequence as a known xylanase, or (c) the weak heuristic that a secreted protein from a plant-pathogenic fungus is more likely a xylanase than an alpha-glucosidase. The heuristic is suggestive but not decisive; the specific family assignment depends on pattern-matching knowledge not derivable from general biology.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "C"
]
```

> Both 3.2.1.20 (alpha-glucosidase) and 3.2.1.8 (endo-xylanase) are glycosyl hydrolases (EC 3.2.1.x). Without the PROSITE GH10 pattern or database lookup, a model could reasonably consider either as a plausible glycosyl hydrolase for a fungal secreted protein. The biological context (plant-pathogenic fungus, secreted, small size) mildly favors xylanase but does not definitively exclude alpha-glucosidase based on sequence alone.


### Important caveats

- The EC 3.2.1.8 assignment is based on PROSITE-ProRule computational inference (ECO:0000255), not direct experimental enzymatic characterization of this specific protein.
- The protein was originally described as an 'ethylene-inducing' elicitor; its xylanase activity is inferred from fold homology (GH10) rather than demonstrated catalysis in the cited literature.
- The reviewer-only evidence (UniProt accession, PROSITE pattern) was not available to the evaluated model; the model must rely solely on the 281-aa sequence and general knowledge.
- The sequence matches the UniProt entry exactly (SHA256 confirmed), so the annotation applies to the exact protein presented.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The protein is a small (~281 AA) secreted fungal protein with a hydrophobic N-terminal signal peptide and multiple cysteines (disulfide bonds), consistent with a plant-pathogen cell-wall-degrading enzyme. This weakly favors a xylanase (3.2.1.8) over an intracellular alpha-glucosidase (3.2.1.20). However, distinguishing specifically between EC 3.2.1.8 (GH10 endo-xylanase) and EC 3.2.1.20 (GH31/GH13 alpha-glucosidase) from raw sequence requires recognizing the GH10 beta-sandwich fold architecture and its conserved catalytic glutamate residues, which is essentially PROSITE pattern PRU01097 matching.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific PROSITE-ProRule pattern PRU01097 (GH10 family signature) that assigns this sequence to endo-1,4-beta-xylanase rather than another glycosyl hydrolase family. Without this pattern or recognition of the exact sequence as EIX1 from Botrytis cinerea, the distinction between 3.2.1.8 and 3.2.1.20 cannot be made from sequence alone with confidence.",
    "reason": "The protein is clearly a glycosyl hydrolase (EC 3.2.1.x), eliminating B (oxidoreductase) and D (transferase). However, distinguishing 3.2.1.8 from 3.2.1.20 requires either (a) recognizing the GH10 fold via PROSITE patterns, (b) identifying this exact sequence as a known xylanase, or (c) the weak heuristic that a secreted protein from a plant-pathogenic fungus is more likely a xylanase than an alpha-glucosidase. The heuristic is suggestive but not decisive; the specific family assignment depends on pattern-matching knowledge not derivable from general biology."
  },
  "case_id": "EC_number_0168",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "UniProt entry A0A384JXV5 (EIX1_BOTFB, 281 AA, sequence SHA256 matches) annotates this protein as Ethylene-inducing xylanase 1 with EC 3.2.1.8 (Endo-1,4-beta-xylanase). The catalytic activity is stated as 'Endohydrolysis of (1->4)-beta-D-xylosidic linkages in xylans.' However, the EC assignment carries evidence code ECO:0000255|PROSITE-ProRule:PRU01097, indicating computational rule-based inference rather than direct experimental characterization of this specific protein's catalytic activity. The cited PubMed reference (33205907) concerns perception of EIX-like proteins by plant receptors, not enzymatic assay of this protein."
  },
  "important_caveats": [
    "The EC 3.2.1.8 assignment is based on PROSITE-ProRule computational inference (ECO:0000255), not direct experimental enzymatic characterization of this specific protein.",
    "The protein was originally described as an 'ethylene-inducing' elicitor; its xylanase activity is inferred from fold homology (GH10) rather than demonstrated catalysis in the cited literature.",
    "The reviewer-only evidence (UniProt accession, PROSITE pattern) was not available to the evaluated model; the model must rely solely on the 281-aa sequence and general knowledge.",
    "The sequence matches the UniProt entry exactly (SHA256 confirmed), so the annotation applies to the exact protein presented."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "C"
    ],
    "reason": "Both 3.2.1.20 (alpha-glucosidase) and 3.2.1.8 (endo-xylanase) are glycosyl hydrolases (EC 3.2.1.x). Without the PROSITE GH10 pattern or database lookup, a model could reasonably consider either as a plausible glycosyl hydrolase for a fungal secreted protein. The biological context (plant-pathogenic fungus, secreted, small size) mildly favors xylanase but does not definitively exclude alpha-glucosidase based on sequence alone."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0168",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry A0A384JXV5 (EIX1_BOTFB, 281 AA, sequence SHA256 matches) annotates this protein as Ethylene-inducing xylanase 1 with EC 3.2.1.8 (Endo-1,4-beta-xylanase). The catalytic activity is stated as 'Endohydrolysis of (1->4)-beta-D-xylosidic linkages in xylans.' However, the EC assignment carries evidence code ECO:0000255|PROSITE-ProRule:PRU01097, indicating computational rule-based inference rather than direct experimental characterization of this specific protein's catalytic activity. The cited PubMed reference (33205907) concerns perception of EIX-like proteins by plant receptors, not enzymatic assay of this protein.",
    "evidence_ids": ["C4", "C5", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The protein is a small (~281 AA) secreted fungal protein with a hydrophobic N-terminal signal peptide and multiple cysteines (disulfide bonds), consistent with a plant-pathogen cell-wall-degrading enzyme. This weakly favors a xylanase (3.2.1.8) over an intracellular alpha-glucosidase (3.2.1.20). However, distinguishing specifically between EC 3.2.1.8 (GH10 endo-xylanase) and EC 3.2.1.20 (GH31/GH13 alpha-glucosidase) from raw sequence requires recognizing the GH10 beta-sandwich fold architecture and its conserved catalytic glutamate residues, which is essentially PROSITE pattern PRU01097 matching.",
    "missing_item_specific_fact": "The specific PROSITE-ProRule pattern PRU01097 (GH10 family signature) that assigns this sequence to endo-1,4-beta-xylanase rather than another glycosyl hydrolase family. Without this pattern or recognition of the exact sequence as EIX1 from Botrytis cinerea, the distinction between 3.2.1.8 and 3.2.1.20 cannot be made from sequence alone with confidence.",
    "reason": "The protein is clearly a glycosyl hydrolase (EC 3.2.1.x), eliminating B (oxidoreductase) and D (transferase). However, distinguishing 3.2.1.8 from 3.2.1.20 requires either (a) recognizing the GH10 fold via PROSITE patterns, (b) identifying this exact sequence as a known xylanase, or (c) the weak heuristic that a secreted protein from a plant-pathogenic fungus is more likely a xylanase than an alpha-glucosidase. The heuristic is suggestive but not decisive; the specific family assignment depends on pattern-matching knowledge not derivable from general biology."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "C"],
    "reason": "Both 3.2.1.20 (alpha-glucosidase) and 3.2.1.8 (endo-xylanase) are glycosyl hydrolases (EC 3.2.1.x). Without the PROSITE GH10 pattern or database lookup, a model could reasonably consider either as a plausible glycosyl hydrolase for a fungal secreted protein. The biological context (plant-pathogenic fungus, secreted, small size) mildly favors xylanase but does not definitively exclude alpha-glucosidase based on sequence alone."
  },
  "important_caveats": [
    "The EC 3.2.1.8 assignment is based on PROSITE-ProRule computational inference (ECO:0000255), not direct experimental enzymatic characterization of this specific protein.",
    "The protein was originally described as an 'ethylene-inducing' elicitor; its xylanase activity is inferred from fold homology (GH10) rather than demonstrated catalysis in the cited literature.",
    "The reviewer-only evidence (UniProt accession, PROSITE pattern) was not available to the evaluated model; the model must rely solely on the 281-aa sequence and general knowledge.",
    "The sequence matches the UniProt entry exactly (SHA256 confirmed), so the annotation applies to the exact protein presented."
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

**Accession:** `A0A384JXV5` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 25. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A384JXV5.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:58.123065+00:00.  

```json
"A0A384JXV5"
```

Source SHA-256: `83f653c725cb3cb95996a5253b38afe4076857dad481a88855db79f7d973240a`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A384JXV5.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:58.123065+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"33205907","source":"PubMed"}],"value":"Endo-1,4-beta-xylanase EIX1"}}],"flag":"Precursor","recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000255","id":"PRU01097","source":"PROSITE-ProRule"}],"value":"3.2.1.8"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"33205907","source":"PubMed"}],"value":"Ethylene-inducing xylanase 1"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"33205907","source":"PubMed"}],"value":"EIX1"}]}}
```

Source SHA-256: `83f653c725cb3cb95996a5253b38afe4076857dad481a88855db79f7d973240a`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A384JXV5.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:58.123065+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"3.2.1.8","evidences":[{"evidenceCode":"ECO:0000255","id":"PRU01097","source":"PROSITE-ProRule"}],"name":"Endohydrolysis of (1->4)-beta-D-xylosidic linkages in xylans."}}
```

Source SHA-256: `83f653c725cb3cb95996a5253b38afe4076857dad481a88855db79f7d973240a`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A384JXV5?format=txt&versions=25)  
**Locator:** `lines 1-16`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 25 / 1.  
**Retrieved:** 2026-11-02T04:25:00.003931+00:00.  

```text
ID   EIX1_BOTFB              Reviewed;         281 AA.
AC   A0A384JXV5;
DT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.
DT   07-NOV-2018, sequence version 1.
DT   28-JAN-2026, entry version 25.
DE   RecName: Full=Ethylene-inducing xylanase 1 {ECO:0000303|PubMed:33205907};
DE            Short=EIX1 {ECO:0000303|PubMed:33205907};
DE            EC=3.2.1.8 {ECO:0000255|PROSITE-ProRule:PRU01097};
DE   AltName: Full=Endo-1,4-beta-xylanase EIX1 {ECO:0000303|PubMed:33205907};
DE   Flags: Precursor;
GN   Name=EIX1 {ECO:0000303|PubMed:33205907}; ORFNames=BCIN_12g00090;
OS   Botryotinia fuckeliana (strain B05.10) (Noble rot fungus) (Botrytis
OS   cinerea).
OC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Leotiomycetes;
OC   Helotiales; Sclerotiniaceae; Botrytis.
OX   NCBI_TaxID=332648;
```

Source SHA-256: `82b4ecbdbcc3751e49d8363b6c40353beac4055c700b46e23d74ec116b1c11ef`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A384JXV5?format=txt&versions=25)  
**Locator:** `lines 6-10`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 25 / 1.  
**Retrieved:** 2026-11-02T04:25:00.003931+00:00.  

```text
DE   RecName: Full=Ethylene-inducing xylanase 1 {ECO:0000303|PubMed:33205907};
DE            Short=EIX1 {ECO:0000303|PubMed:33205907};
DE            EC=3.2.1.8 {ECO:0000255|PROSITE-ProRule:PRU01097};
DE   AltName: Full=Endo-1,4-beta-xylanase EIX1 {ECO:0000303|PubMed:33205907};
DE   Flags: Precursor;
```

Source SHA-256: `82b4ecbdbcc3751e49d8363b6c40353beac4055c700b46e23d74ec116b1c11ef`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A384JXV5?format=txt&versions=25)  
**Locator:** `lines 67-69`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 25 / 1.  
**Retrieved:** 2026-11-02T04:25:00.003931+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=Endohydrolysis of (1->4)-beta-D-xylosidic linkages in xylans.;
CC         EC=3.2.1.8; Evidence={ECO:0000255|PROSITE-ProRule:PRU01097};
```

Source SHA-256: `82b4ecbdbcc3751e49d8363b6c40353beac4055c700b46e23d74ec116b1c11ef`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 168. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
