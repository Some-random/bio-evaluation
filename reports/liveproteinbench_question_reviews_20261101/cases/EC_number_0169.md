# EC_number_0169

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `EC_number`  
**Author expected answer:** **A** — 3.2.1.8

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MVCFSSLFVAASAIAVVFASPVDHEQLAKRQSTPSSQGTHDGYFYSWWTDGGAAATYTNLAGGEYSVSWSNGGNLVGGKGWNPGSARTITYSGTYNPNGNSYLAVYGWTRNPLVEYYVVENFGTYNPSSGATARGQVTHDGALYRLFESTRTNQPSIDGTATFQQYWAVRDVKRTGGTVNMATFFNAWTSAGMRLGTHNYQVVATEGYFSSGSARINVAGGGGSTPSPPSTPSPPTTPSPPPVTPPPSGGGSCAARWGQCGGSGWNGATCCSAGTCQAQNQWYSQCL

[Multiple Choices]
A. 3.2.1.8
B. 3.2.1.18
C. 1.1.1.336
D. 3.1.3.112
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

> The exact sequence matches the UniProt entry annotated as EC 3.2.1.8, with the catalytic activity specified as endohydrolysis of beta-D-xylosidic linkages in xylans. The annotation cites a PROSITE-ProRule computational inference, not direct experimental evidence in the supplied excerpts.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The N-terminal hydrophobic segment is consistent with secretion, and the sequence is compatible with an extracellular glycoside hydrolase. These clues do not by themselves establish xylan as the substrate or uniquely determine the complete EC number.


**Missing item-specific fact**

> A protein-specific functional or homology annotation assigning this sequence to an endo-xylanase, or experimental evidence of its substrate and reaction, is absent from the input.


**Reason**

> Choosing EC 3.2.1.8 requires identifying the sequence's particular enzyme function; the general sequence clues are not enough to distinguish that precise activity from other glycosidase activities.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The supplied sequence alone does not conclusively establish an EC number, but the choices do not provide a clearly supported alternative to the keyed xylanase activity.


### Important caveats

- The sequence-matched UniProt annotation supports the key, but its EC and catalytic-activity evidence is computational (PROSITE-ProRule), not an independently verified experimental measurement in the supplied evidence.
- The author’s exact source snapshot is unknown; the cited historical and current UniProt records both match the supplied sequence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal hydrophobic segment is consistent with secretion, and the sequence is compatible with an extracellular glycoside hydrolase. These clues do not by themselves establish xylan as the substrate or uniquely determine the complete EC number.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "A protein-specific functional or homology annotation assigning this sequence to an endo-xylanase, or experimental evidence of its substrate and reaction, is absent from the input.",
    "reason": "Choosing EC 3.2.1.8 requires identifying the sequence's particular enzyme function; the general sequence clues are not enough to distinguish that precise activity from other glycosidase activities."
  },
  "case_id": "EC_number_0169",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry annotated as EC 3.2.1.8, with the catalytic activity specified as endohydrolysis of beta-D-xylosidic linkages in xylans. The annotation cites a PROSITE-ProRule computational inference, not direct experimental evidence in the supplied excerpts."
  },
  "important_caveats": [
    "The sequence-matched UniProt annotation supports the key, but its EC and catalytic-activity evidence is computational (PROSITE-ProRule), not an independently verified experimental measurement in the supplied evidence.",
    "The author’s exact source snapshot is unknown; the cited historical and current UniProt records both match the supplied sequence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied sequence alone does not conclusively establish an EC number, but the choices do not provide a clearly supported alternative to the keyed xylanase activity."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0169",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry annotated as EC 3.2.1.8, with the catalytic activity specified as endohydrolysis of beta-D-xylosidic linkages in xylans. The annotation cites a PROSITE-ProRule computational inference, not direct experimental evidence in the supplied excerpts.",
    "evidence_ids": ["C1", "C4", "C5", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The N-terminal hydrophobic segment is consistent with secretion, and the sequence is compatible with an extracellular glycoside hydrolase. These clues do not by themselves establish xylan as the substrate or uniquely determine the complete EC number.",
    "missing_item_specific_fact": "A protein-specific functional or homology annotation assigning this sequence to an endo-xylanase, or experimental evidence of its substrate and reaction, is absent from the input.",
    "reason": "Choosing EC 3.2.1.8 requires identifying the sequence's particular enzyme function; the general sequence clues are not enough to distinguish that precise activity from other glycosidase activities."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied sequence alone does not conclusively establish an EC number, but the choices do not provide a clearly supported alternative to the keyed xylanase activity."
  },
  "important_caveats": [
    "The sequence-matched UniProt annotation supports the key, but its EC and catalytic-activity evidence is computational (PROSITE-ProRule), not an independently verified experimental measurement in the supplied evidence.",
    "The author’s exact source snapshot is unknown; the cited historical and current UniProt records both match the supplied sequence."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry A0A0G4KL96 (EIX3_VERLO, Verticillium longisporum) assigns EC 3.2.1.8 (Endo-1,4-beta-xylanase) with catalytic activity 'Endohydrolysis of (1->4)-beta-D-xylosidic linkages in xylans.' The sequence matches exactly (SHA-256 confirmed, 287 AA). However, the EC assignment carries evidence code ECO:0000255|PROSITE-ProRule:PRU01097, meaning it is based on computational pattern matching rather than direct experimental characterization of xylanase activity. The cited PubMed reference (33205907) describes the protein's elicitor function in plant defense, not its enzymatic xylanase kinetics. The annotation is consistent with the protein's name 'Endo-1,4-beta-xylanase EIX3' and its GH11-family sequence features.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H1](#evidence-h1), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains the highly conserved 'WWTDGG' motif (residues ~44-49), a hallmark of glycoside hydrolase family 11 (GH11) xylanases, which catalyze endo-1,4-beta-xylanase activity (EC 3.2.1.8). The protein is small (~287 AA precursor, ~250 AA mature), has an N-terminal secretion signal peptide (MVCFSSLFVAASAIAVVFASPVDHEQ), and is fungal in origin—all consistent with a secreted GH11 xylanase. EC 1.1.1.336 (oxidoreductase) can be excluded because no NAD(P)+-binding Rossmann-fold motif (GxGxxG) is present. EC 3.1.3.112 (phosphatase/kinase) can be excluded because no PTP-like (HCxxGxxR) or kinase catalytic motifs are present. Between A (3.2.1.8, GH11 xylanase) and B (3.2.1.18, GH53 galactanase), the WWTDGG motif and beta-jelly-roll-compatible small size specifically indicate GH11, whereas GH53 galactanases have an alpha-sandwich fold and lack this motif.


**Missing item-specific fact**

> None critical. The WWTDGG motif is a well-known family-defining feature in glycoside hydrolase biochemistry, accessible through general structural biology knowledge.


**Reason**

> A model with knowledge of glycoside hydrolase family signatures can identify the WWTDGG motif as diagnostic of GH11 (EC 3.2.1.8) and rule out GH53 (EC 3.2.1.18), oxidoreductases, and phosphatases based on absent cofactor/catalytic motifs. This constitutes a concrete biological argument from the sequence itself rather than pure database lookup.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options span three different EC top-level classes (3.2 glycosylases, 1.1 oxidoreductases, 3.1 phosphatases). The WWTDGG motif uniquely points to GH11/EC 3.2.1.8 among the choices. No other option is defensible given the sequence features.


### Important caveats

- The EC 3.2.1.8 assignment in UniProt is based on PROSITE-ProRule pattern matching (ECO:0000255), not direct experimental measurement of xylanase activity. The primary literature (PubMed 33205907) characterizes EIX3 as an elicitor protein; its xylanase activity may be inferred from sequence homology.
- The protein is annotated as a 'Precursor' (287 AA with signal peptide); the mature GH11 domain is smaller. This does not affect the EC assignment but is relevant for structural interpretation.
- The distinction between EC 3.2.1.8 and EC 3.2.1.18 requires recognizing the WWTDGG motif as GH11-specific; a model unfamiliar with glycoside hydrolase family signatures would struggle to differentiate these two glycosidase options.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains the highly conserved 'WWTDGG' motif (residues ~44-49), a hallmark of glycoside hydrolase family 11 (GH11) xylanases, which catalyze endo-1,4-beta-xylanase activity (EC 3.2.1.8). The protein is small (~287 AA precursor, ~250 AA mature), has an N-terminal secretion signal peptide (MVCFSSLFVAASAIAVVFASPVDHEQ), and is fungal in origin—all consistent with a secreted GH11 xylanase. EC 1.1.1.336 (oxidoreductase) can be excluded because no NAD(P)+-binding Rossmann-fold motif (GxGxxG) is present. EC 3.1.3.112 (phosphatase/kinase) can be excluded because no PTP-like (HCxxGxxR) or kinase catalytic motifs are present. Between A (3.2.1.8, GH11 xylanase) and B (3.2.1.18, GH53 galactanase), the WWTDGG motif and beta-jelly-roll-compatible small size specifically indicate GH11, whereas GH53 galactanases have an alpha-sandwich fold and lack this motif.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None critical. The WWTDGG motif is a well-known family-defining feature in glycoside hydrolase biochemistry, accessible through general structural biology knowledge.",
    "reason": "A model with knowledge of glycoside hydrolase family signatures can identify the WWTDGG motif as diagnostic of GH11 (EC 3.2.1.8) and rule out GH53 (EC 3.2.1.18), oxidoreductases, and phosphatases based on absent cofactor/catalytic motifs. This constitutes a concrete biological argument from the sequence itself rather than pure database lookup."
  },
  "case_id": "EC_number_0169",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H1",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "UniProt entry A0A0G4KL96 (EIX3_VERLO, Verticillium longisporum) assigns EC 3.2.1.8 (Endo-1,4-beta-xylanase) with catalytic activity 'Endohydrolysis of (1->4)-beta-D-xylosidic linkages in xylans.' The sequence matches exactly (SHA-256 confirmed, 287 AA). However, the EC assignment carries evidence code ECO:0000255|PROSITE-ProRule:PRU01097, meaning it is based on computational pattern matching rather than direct experimental characterization of xylanase activity. The cited PubMed reference (33205907) describes the protein's elicitor function in plant defense, not its enzymatic xylanase kinetics. The annotation is consistent with the protein's name 'Endo-1,4-beta-xylanase EIX3' and its GH11-family sequence features."
  },
  "important_caveats": [
    "The EC 3.2.1.8 assignment in UniProt is based on PROSITE-ProRule pattern matching (ECO:0000255), not direct experimental measurement of xylanase activity. The primary literature (PubMed 33205907) characterizes EIX3 as an elicitor protein; its xylanase activity may be inferred from sequence homology.",
    "The protein is annotated as a 'Precursor' (287 AA with signal peptide); the mature GH11 domain is smaller. This does not affect the EC assignment but is relevant for structural interpretation.",
    "The distinction between EC 3.2.1.8 and EC 3.2.1.18 requires recognizing the WWTDGG motif as GH11-specific; a model unfamiliar with glycoside hydrolase family signatures would struggle to differentiate these two glycosidase options."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span three different EC top-level classes (3.2 glycosylases, 1.1 oxidoreductases, 3.1 phosphatases). The WWTDGG motif uniquely points to GH11/EC 3.2.1.8 among the choices. No other option is defensible given the sequence features."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0169",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry A0A0G4KL96 (EIX3_VERLO, Verticillium longisporum) assigns EC 3.2.1.8 (Endo-1,4-beta-xylanase) with catalytic activity 'Endohydrolysis of (1->4)-beta-D-xylosidic linkages in xylans.' The sequence matches exactly (SHA-256 confirmed, 287 AA). However, the EC assignment carries evidence code ECO:0000255|PROSITE-ProRule:PRU01097, meaning it is based on computational pattern matching rather than direct experimental characterization of xylanase activity. The cited PubMed reference (33205907) describes the protein's elicitor function in plant defense, not its enzymatic xylanase kinetics. The annotation is consistent with the protein's name 'Endo-1,4-beta-xylanase EIX3' and its GH11-family sequence features.",
    "evidence_ids": ["C4", "C5", "H1", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains the highly conserved 'WWTDGG' motif (residues ~44-49), a hallmark of glycoside hydrolase family 11 (GH11) xylanases, which catalyze endo-1,4-beta-xylanase activity (EC 3.2.1.8). The protein is small (~287 AA precursor, ~250 AA mature), has an N-terminal secretion signal peptide (MVCFSSLFVAASAIAVVFASPVDHEQ), and is fungal in origin—all consistent with a secreted GH11 xylanase. EC 1.1.1.336 (oxidoreductase) can be excluded because no NAD(P)+-binding Rossmann-fold motif (GxGxxG) is present. EC 3.1.3.112 (phosphatase/kinase) can be excluded because no PTP-like (HCxxGxxR) or kinase catalytic motifs are present. Between A (3.2.1.8, GH11 xylanase) and B (3.2.1.18, GH53 galactanase), the WWTDGG motif and beta-jelly-roll-compatible small size specifically indicate GH11, whereas GH53 galactanases have an alpha-sandwich fold and lack this motif.",
    "missing_item_specific_fact": "None critical. The WWTDGG motif is a well-known family-defining feature in glycoside hydrolase biochemistry, accessible through general structural biology knowledge.",
    "reason": "A model with knowledge of glycoside hydrolase family signatures can identify the WWTDGG motif as diagnostic of GH11 (EC 3.2.1.8) and rule out GH53 (EC 3.2.1.18), oxidoreductases, and phosphatases based on absent cofactor/catalytic motifs. This constitutes a concrete biological argument from the sequence itself rather than pure database lookup."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span three different EC top-level classes (3.2 glycosylases, 1.1 oxidoreductases, 3.1 phosphatases). The WWTDGG motif uniquely points to GH11/EC 3.2.1.8 among the choices. No other option is defensible given the sequence features."
  },
  "important_caveats": [
    "The EC 3.2.1.8 assignment in UniProt is based on PROSITE-ProRule pattern matching (ECO:0000255), not direct experimental measurement of xylanase activity. The primary literature (PubMed 33205907) characterizes EIX3 as an elicitor protein; its xylanase activity may be inferred from sequence homology.",
    "The protein is annotated as a 'Precursor' (287 AA with signal peptide); the mature GH11 domain is smaller. This does not affect the EC assignment but is relevant for structural interpretation.",
    "The distinction between EC 3.2.1.8 and EC 3.2.1.18 requires recognizing the WWTDGG motif as GH11-specific; a model unfamiliar with glycoside hydrolase family signatures would struggle to differentiate these two glycosidase options."
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

**Accession:** `A0A0G4KL96` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 36. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0G4KL96.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:05.640284+00:00.  

```json
"A0A0G4KL96"
```

Source SHA-256: `ee5462ea538a6639e4bb2c2732a6d0e1f62813e984780d98433324fcf5b40c9b`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0G4KL96.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:05.640284+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"33205907","source":"PubMed"}],"value":"Endo-1,4-beta-xylanase EIX3"}}],"flag":"Precursor","recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000255","id":"PRU01097","source":"PROSITE-ProRule"}],"value":"3.2.1.8"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"33205907","source":"PubMed"}],"value":"Ethylene-inducing xylanase 3"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"33205907","source":"PubMed"}],"value":"EIX3"}]}}
```

Source SHA-256: `ee5462ea538a6639e4bb2c2732a6d0e1f62813e984780d98433324fcf5b40c9b`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0G4KL96.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:05.640284+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"3.2.1.8","evidences":[{"evidenceCode":"ECO:0000255","id":"PRU01097","source":"PROSITE-ProRule"}],"name":"Endohydrolysis of (1->4)-beta-D-xylosidic linkages in xylans."}}
```

Source SHA-256: `ee5462ea538a6639e4bb2c2732a6d0e1f62813e984780d98433324fcf5b40c9b`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0G4KL96?format=txt&versions=36)  
**Locator:** `lines 1-15`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 36 / 1.  
**Retrieved:** 2026-11-02T04:24:07.694004+00:00.  

```text
ID   EIX3_VERLO              Reviewed;         287 AA.
AC   A0A0G4KL96;
DT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.
DT   16-SEP-2015, sequence version 1.
DT   28-JAN-2026, entry version 36.
DE   RecName: Full=Ethylene-inducing xylanase 3 {ECO:0000303|PubMed:33205907};
DE            Short=EIX3 {ECO:0000303|PubMed:33205907};
DE            EC=3.2.1.8 {ECO:0000255|PROSITE-ProRule:PRU01097};
DE   AltName: Full=Endo-1,4-beta-xylanase EIX3 {ECO:0000303|PubMed:33205907};
DE   Flags: Precursor;
GN   Name=EIX3 {ECO:0000303|PubMed:33205907}; ORFNames=BN1708_002170;
OS   Verticillium longisporum (Verticillium dahliae var. longisporum).
OC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Sordariomycetes;
OC   Hypocreomycetidae; Glomerellales; Plectosphaerellaceae; Verticillium.
OX   NCBI_TaxID=100787;
```

Source SHA-256: `3e9ce979511ebc6beb41036187cb06c1d4ba05ea05f31964b342d98537c3251b`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0G4KL96?format=txt&versions=36)  
**Locator:** `lines 6-10`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 36 / 1.  
**Retrieved:** 2026-11-02T04:24:07.694004+00:00.  

```text
DE   RecName: Full=Ethylene-inducing xylanase 3 {ECO:0000303|PubMed:33205907};
DE            Short=EIX3 {ECO:0000303|PubMed:33205907};
DE            EC=3.2.1.8 {ECO:0000255|PROSITE-ProRule:PRU01097};
DE   AltName: Full=Endo-1,4-beta-xylanase EIX3 {ECO:0000303|PubMed:33205907};
DE   Flags: Precursor;
```

Source SHA-256: `3e9ce979511ebc6beb41036187cb06c1d4ba05ea05f31964b342d98537c3251b`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0G4KL96?format=txt&versions=36)  
**Locator:** `lines 42-44`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 36 / 1.  
**Retrieved:** 2026-11-02T04:24:07.694004+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=Endohydrolysis of (1->4)-beta-D-xylosidic linkages in xylans.;
CC         EC=3.2.1.8; Evidence={ECO:0000255|PROSITE-ProRule:PRU01097};
```

Source SHA-256: `3e9ce979511ebc6beb41036187cb06c1d4ba05ea05f31964b342d98537c3251b`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 169. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
