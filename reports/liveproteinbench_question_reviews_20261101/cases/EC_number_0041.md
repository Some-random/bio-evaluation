# EC_number_0041

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `EC_number`  
**Author expected answer:** **D** — 3.2.1.8

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MITFSSLLVTFSAISTSLAIPGSILPKRSPMNFVLQRNESSLVRRATPNYEQDYTTGGDVIYTPSGSSFTVDWSTEDDFVVGLGWTTGSTNPINFSGTFGIGSGTALLSIYGWSENPLVEYYIVEDSASPPSFGTVKGSVTSDGSSYTIWENQRVNEPSIVGTATFNQYISVRSSPRKSGTVTVENHFQAWAALGMNLGTLNYQVLAVEGWGGEGAATQTVS

[Multiple Choices]
A. 3.2.1.105
B. 4.2.3.1
C. 1.14.13.238
D. 3.2.1.8
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

> The supplied sequence exactly matches a UniProt entry annotated as EC 3.2.1.8, with the reaction given as endohydrolysis of beta-D-xylosidic linkages in xylans. The cited annotation is based on a PROSITE-ProRule computational inference, not direct experimental evidence in the supplied excerpts.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H1](#evidence-h1), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The N-terminal hydrophobic region is consistent with a secreted protein, and the sequence is compatible with a fungal glycoside hydrolase, but those clues do not establish its precise substrate specificity or complete EC number.


**Missing item-specific fact**

> The protein-specific functional annotation identifying this sequence as an endo-1,4-beta-xylanase (EC 3.2.1.8), or equivalent validated substrate-specificity evidence.


**Reason**

> Choosing the exact EC requires identifying the sequence's specific enzymatic activity. The matching database annotation supports the key for this audit, but it was reviewer-only and is not information provided to the evaluated model.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The sequence alone does not resolve the exact EC, but the reviewer-only annotation assigns the matched sequence to EC 3.2.1.8; no supplied evidence supports another listed option.


### Important caveats

- The sequence match is exact, including in the archived entry, but the author's original source snapshot is unknown.
- The EC and catalytic-activity annotations cited here are attributed to PROSITE-ProRule; the excerpts do not independently establish experimental measurement of this protein's activity.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal hydrophobic region is consistent with a secreted protein, and the sequence is compatible with a fungal glycoside hydrolase, but those clues do not establish its precise substrate specificity or complete EC number.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific functional annotation identifying this sequence as an endo-1,4-beta-xylanase (EC 3.2.1.8), or equivalent validated substrate-specificity evidence.",
    "reason": "Choosing the exact EC requires identifying the sequence's specific enzymatic activity. The matching database annotation supports the key for this audit, but it was reviewer-only and is not information provided to the evaluated model."
  },
  "case_id": "EC_number_0041",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H1",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches a UniProt entry annotated as EC 3.2.1.8, with the reaction given as endohydrolysis of beta-D-xylosidic linkages in xylans. The cited annotation is based on a PROSITE-ProRule computational inference, not direct experimental evidence in the supplied excerpts."
  },
  "important_caveats": [
    "The sequence match is exact, including in the archived entry, but the author's original source snapshot is unknown.",
    "The EC and catalytic-activity annotations cited here are attributed to PROSITE-ProRule; the excerpts do not independently establish experimental measurement of this protein's activity."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence alone does not resolve the exact EC, but the reviewer-only annotation assigns the matched sequence to EC 3.2.1.8; no supplied evidence supports another listed option."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0041",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches a UniProt entry annotated as EC 3.2.1.8, with the reaction given as endohydrolysis of beta-D-xylosidic linkages in xylans. The cited annotation is based on a PROSITE-ProRule computational inference, not direct experimental evidence in the supplied excerpts.",
    "evidence_ids": ["C1", "C4", "C5", "H1", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The N-terminal hydrophobic region is consistent with a secreted protein, and the sequence is compatible with a fungal glycoside hydrolase, but those clues do not establish its precise substrate specificity or complete EC number.",
    "missing_item_specific_fact": "The protein-specific functional annotation identifying this sequence as an endo-1,4-beta-xylanase (EC 3.2.1.8), or equivalent validated substrate-specificity evidence.",
    "reason": "Choosing the exact EC requires identifying the sequence's specific enzymatic activity. The matching database annotation supports the key for this audit, but it was reviewer-only and is not information provided to the evaluated model."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence alone does not resolve the exact EC, but the reviewer-only annotation assigns the matched sequence to EC 3.2.1.8; no supplied evidence supports another listed option."
  },
  "important_caveats": [
    "The sequence match is exact, including in the archived entry, but the author's original source snapshot is unknown.",
    "The EC and catalytic-activity annotations cited here are attributed to PROSITE-ProRule; the excerpts do not independently establish experimental measurement of this protein's activity."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry A0A384K474 (sequence exact match, 222 aa) annotates this protein as Ethylene-inducing xylanase 2 (EIX2) with EC 3.2.1.8. The catalytic activity is annotated as 'Endohydrolysis of (1->4)-beta-D-xylosidic linkages in xylans.' However, the EC assignment carries evidence code ECO:0000255|PROSITE-ProRule:PRU01097, meaning it is a computational pattern-based inference rather than a direct experimental enzymatic assay. The PubMed reference (33205907) describes EIX2's role in plant-pathogen perception, not a purified-enzyme kinetic characterization. The annotation is consistent and applies to the exact supplied sequence.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence (222 aa, with an N-terminal signal peptide yielding a ~190 aa mature protein) exhibits hallmarks of glycoside hydrolase family 11 (GH11): a compact beta-jelly-roll architecture, the 'GSGT' motif (residues ~115-118: 'GSGTALLSIYGW'), the 'TGG' motif near the catalytic region (~position 50), and the overall small size typical of GH11 xylanases. These features identify the protein as a xylanase (EC 3.2.1.8). Options B (EC 4.2.3.1, a hydro-lyase) and C (EC 1.14.13.238, an oxidoreductase) belong to entirely different enzyme classes and can be eliminated by recognizing the protein as a glycosidase (EC 3 class). The remaining glycosidase option A (3.2.1.105) would require a different GH family signature; the GH11-specific motifs present here favor 3.2.1.8.


**Missing item-specific fact**

> None strictly missing; however, distinguishing EC 3.2.1.8 from EC 3.2.1.105 relies on recognizing GH11 family signature motifs, which is specialized but generalizable protein-family knowledge rather than memorization of this specific protein's database entry.


**Reason**

> The sequence contains identifiable GH11 xylanase signature motifs (GSGT, TGG, compact size, beta-jelly-roll character) that a knowledgeable model or bioinformatician could use to assign the protein to the xylanase family and thus EC 3.2.1.8. The elimination of non-glycosidase options (B, C) is straightforward from enzyme-class reasoning. The distinction between the two glycosidase options (A vs D) depends on recognizing GH11-specific features, which is specialized but constitutes generalizable protein-family pattern recognition rather than lookup of a single protein's annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options B (4.2.3.1, lyase) and C (1.14.13.238, oxidoreductase) are clearly incompatible with a glycosidase sequence. Between A (3.2.1.105) and D (3.2.1.8), the GH11 signature motifs in the sequence favor D. Without knowing the precise identity of EC 3.2.1.105, a model might hesitate, but the strong GH11 character of the sequence makes D the more defensible choice.


### Important caveats

- The UniProt EC 3.2.1.8 assignment is based on PROSITE-ProRule pattern matching (ECO:0000255), not direct experimental enzymatic assay. The protein's primary biological role (ethylene induction in plant-pathogen interaction) is distinct from its xylanase catalytic activity.
- The PubMed reference cited (33205907) concerns NbEIX2-mediated perception of an EIX-like protein in Nicotiana benthamiana, not a purified-enzyme substrate-specificity assay confirming xylanase activity.
- EC 3.2.1.105 is a relatively obscure glycosidase number; a model unfamiliar with it may default to the more well-known 3.2.1.8, which could inflate apparent reasoning performance.
- The sequence is a precursor (includes a signal peptide); the mature xylanase domain is shorter than 222 aa, which is consistent with GH11 size but means the full sequence includes non-catalytic N-terminal residues.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence (222 aa, with an N-terminal signal peptide yielding a ~190 aa mature protein) exhibits hallmarks of glycoside hydrolase family 11 (GH11): a compact beta-jelly-roll architecture, the 'GSGT' motif (residues ~115-118: 'GSGTALLSIYGW'), the 'TGG' motif near the catalytic region (~position 50), and the overall small size typical of GH11 xylanases. These features identify the protein as a xylanase (EC 3.2.1.8). Options B (EC 4.2.3.1, a hydro-lyase) and C (EC 1.14.13.238, an oxidoreductase) belong to entirely different enzyme classes and can be eliminated by recognizing the protein as a glycosidase (EC 3 class). The remaining glycosidase option A (3.2.1.105) would require a different GH family signature; the GH11-specific motifs present here favor 3.2.1.8.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None strictly missing; however, distinguishing EC 3.2.1.8 from EC 3.2.1.105 relies on recognizing GH11 family signature motifs, which is specialized but generalizable protein-family knowledge rather than memorization of this specific protein's database entry.",
    "reason": "The sequence contains identifiable GH11 xylanase signature motifs (GSGT, TGG, compact size, beta-jelly-roll character) that a knowledgeable model or bioinformatician could use to assign the protein to the xylanase family and thus EC 3.2.1.8. The elimination of non-glycosidase options (B, C) is straightforward from enzyme-class reasoning. The distinction between the two glycosidase options (A vs D) depends on recognizing GH11-specific features, which is specialized but constitutes generalizable protein-family pattern recognition rather than lookup of a single protein's annotation."
  },
  "case_id": "EC_number_0041",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "UniProt entry A0A384K474 (sequence exact match, 222 aa) annotates this protein as Ethylene-inducing xylanase 2 (EIX2) with EC 3.2.1.8. The catalytic activity is annotated as 'Endohydrolysis of (1->4)-beta-D-xylosidic linkages in xylans.' However, the EC assignment carries evidence code ECO:0000255|PROSITE-ProRule:PRU01097, meaning it is a computational pattern-based inference rather than a direct experimental enzymatic assay. The PubMed reference (33205907) describes EIX2's role in plant-pathogen perception, not a purified-enzyme kinetic characterization. The annotation is consistent and applies to the exact supplied sequence."
  },
  "important_caveats": [
    "The UniProt EC 3.2.1.8 assignment is based on PROSITE-ProRule pattern matching (ECO:0000255), not direct experimental enzymatic assay. The protein's primary biological role (ethylene induction in plant-pathogen interaction) is distinct from its xylanase catalytic activity.",
    "The PubMed reference cited (33205907) concerns NbEIX2-mediated perception of an EIX-like protein in Nicotiana benthamiana, not a purified-enzyme substrate-specificity assay confirming xylanase activity.",
    "EC 3.2.1.105 is a relatively obscure glycosidase number; a model unfamiliar with it may default to the more well-known 3.2.1.8, which could inflate apparent reasoning performance.",
    "The sequence is a precursor (includes a signal peptide); the mature xylanase domain is shorter than 222 aa, which is consistent with GH11 size but means the full sequence includes non-catalytic N-terminal residues."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options B (4.2.3.1, lyase) and C (1.14.13.238, oxidoreductase) are clearly incompatible with a glycosidase sequence. Between A (3.2.1.105) and D (3.2.1.8), the GH11 signature motifs in the sequence favor D. Without knowing the precise identity of EC 3.2.1.105, a model might hesitate, but the strong GH11 character of the sequence makes D the more defensible choice."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0041",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry A0A384K474 (sequence exact match, 222 aa) annotates this protein as Ethylene-inducing xylanase 2 (EIX2) with EC 3.2.1.8. The catalytic activity is annotated as 'Endohydrolysis of (1->4)-beta-D-xylosidic linkages in xylans.' However, the EC assignment carries evidence code ECO:0000255|PROSITE-ProRule:PRU01097, meaning it is a computational pattern-based inference rather than a direct experimental enzymatic assay. The PubMed reference (33205907) describes EIX2's role in plant-pathogen perception, not a purified-enzyme kinetic characterization. The annotation is consistent and applies to the exact supplied sequence.",
    "evidence_ids": ["C4", "C5", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence (222 aa, with an N-terminal signal peptide yielding a ~190 aa mature protein) exhibits hallmarks of glycoside hydrolase family 11 (GH11): a compact beta-jelly-roll architecture, the 'GSGT' motif (residues ~115-118: 'GSGTALLSIYGW'), the 'TGG' motif near the catalytic region (~position 50), and the overall small size typical of GH11 xylanases. These features identify the protein as a xylanase (EC 3.2.1.8). Options B (EC 4.2.3.1, a hydro-lyase) and C (EC 1.14.13.238, an oxidoreductase) belong to entirely different enzyme classes and can be eliminated by recognizing the protein as a glycosidase (EC 3 class). The remaining glycosidase option A (3.2.1.105) would require a different GH family signature; the GH11-specific motifs present here favor 3.2.1.8.",
    "missing_item_specific_fact": "None strictly missing; however, distinguishing EC 3.2.1.8 from EC 3.2.1.105 relies on recognizing GH11 family signature motifs, which is specialized but generalizable protein-family knowledge rather than memorization of this specific protein's database entry.",
    "reason": "The sequence contains identifiable GH11 xylanase signature motifs (GSGT, TGG, compact size, beta-jelly-roll character) that a knowledgeable model or bioinformatician could use to assign the protein to the xylanase family and thus EC 3.2.1.8. The elimination of non-glycosidase options (B, C) is straightforward from enzyme-class reasoning. The distinction between the two glycosidase options (A vs D) depends on recognizing GH11-specific features, which is specialized but constitutes generalizable protein-family pattern recognition rather than lookup of a single protein's annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options B (4.2.3.1, lyase) and C (1.14.13.238, oxidoreductase) are clearly incompatible with a glycosidase sequence. Between A (3.2.1.105) and D (3.2.1.8), the GH11 signature motifs in the sequence favor D. Without knowing the precise identity of EC 3.2.1.105, a model might hesitate, but the strong GH11 character of the sequence makes D the more defensible choice."
  },
  "important_caveats": [
    "The UniProt EC 3.2.1.8 assignment is based on PROSITE-ProRule pattern matching (ECO:0000255), not direct experimental enzymatic assay. The protein's primary biological role (ethylene induction in plant-pathogen interaction) is distinct from its xylanase catalytic activity.",
    "The PubMed reference cited (33205907) concerns NbEIX2-mediated perception of an EIX-like protein in Nicotiana benthamiana, not a purified-enzyme substrate-specificity assay confirming xylanase activity.",
    "EC 3.2.1.105 is a relatively obscure glycosidase number; a model unfamiliar with it may default to the more well-known 3.2.1.8, which could inflate apparent reasoning performance.",
    "The sequence is a precursor (includes a signal peptide); the mature xylanase domain is shorter than 222 aa, which is consistent with GH11 size but means the full sequence includes non-catalytic N-terminal residues."
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

**Accession:** `A0A384K474` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 25. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A384K474.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:59.392996+00:00.  

```json
"A0A384K474"
```

Source SHA-256: `55204b82bbe53c219df38fd17bb07b90d74cea40d24431f98ad10936f0fb3921`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A384K474.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:59.392996+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"33205907","source":"PubMed"}],"value":"Endo-1,4-beta-xylanase EIX2"}}],"flag":"Precursor","recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000255","id":"PRU01097","source":"PROSITE-ProRule"}],"value":"3.2.1.8"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"33205907","source":"PubMed"}],"value":"Ethylene-inducing xylanase 2"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"33205907","source":"PubMed"}],"value":"EIX21"}]}}
```

Source SHA-256: `55204b82bbe53c219df38fd17bb07b90d74cea40d24431f98ad10936f0fb3921`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A384K474.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:59.392996+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"3.2.1.8","evidences":[{"evidenceCode":"ECO:0000255","id":"PRU01097","source":"PROSITE-ProRule"}],"name":"Endohydrolysis of (1->4)-beta-D-xylosidic linkages in xylans."}}
```

Source SHA-256: `55204b82bbe53c219df38fd17bb07b90d74cea40d24431f98ad10936f0fb3921`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A384K474?format=txt&versions=25)  
**Locator:** `lines 1-16`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 25 / 1.  
**Retrieved:** 2026-11-02T04:25:01.435228+00:00.  

```text
ID   EIX2_BOTFB              Reviewed;         222 AA.
AC   A0A384K474;
DT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.
DT   07-NOV-2018, sequence version 1.
DT   28-JAN-2026, entry version 25.
DE   RecName: Full=Ethylene-inducing xylanase 2 {ECO:0000303|PubMed:33205907};
DE            Short=EIX21 {ECO:0000303|PubMed:33205907};
DE            EC=3.2.1.8 {ECO:0000255|PROSITE-ProRule:PRU01097};
DE   AltName: Full=Endo-1,4-beta-xylanase EIX2 {ECO:0000303|PubMed:33205907};
DE   Flags: Precursor;
GN   Name=EIX2 {ECO:0000303|PubMed:33205907}; ORFNames=BCIN_15g01600;
OS   Botryotinia fuckeliana (strain B05.10) (Noble rot fungus) (Botrytis
OS   cinerea).
OC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Leotiomycetes;
OC   Helotiales; Sclerotiniaceae; Botrytis.
OX   NCBI_TaxID=332648;
```

Source SHA-256: `f401e20e06f466f7611bd91f76c327c904201b29c424133348114ef2358dffba`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A384K474?format=txt&versions=25)  
**Locator:** `lines 6-10`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 25 / 1.  
**Retrieved:** 2026-11-02T04:25:01.435228+00:00.  

```text
DE   RecName: Full=Ethylene-inducing xylanase 2 {ECO:0000303|PubMed:33205907};
DE            Short=EIX21 {ECO:0000303|PubMed:33205907};
DE            EC=3.2.1.8 {ECO:0000255|PROSITE-ProRule:PRU01097};
DE   AltName: Full=Endo-1,4-beta-xylanase EIX2 {ECO:0000303|PubMed:33205907};
DE   Flags: Precursor;
```

Source SHA-256: `f401e20e06f466f7611bd91f76c327c904201b29c424133348114ef2358dffba`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A384K474?format=txt&versions=25)  
**Locator:** `lines 67-69`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 25 / 1.  
**Retrieved:** 2026-11-02T04:25:01.435228+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=Endohydrolysis of (1->4)-beta-D-xylosidic linkages in xylans.;
CC         EC=3.2.1.8; Evidence={ECO:0000255|PROSITE-ProRule:PRU01097};
```

Source SHA-256: `f401e20e06f466f7611bd91f76c327c904201b29c424133348114ef2358dffba`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 41. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
