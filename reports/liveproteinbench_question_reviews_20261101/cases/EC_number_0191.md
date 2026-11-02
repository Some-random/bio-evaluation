# EC_number_0191

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `EC_number`  
**Author expected answer:** **C** — 3.2.1.8

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MVSFSTLLTACTAITGALGTPDLDRRQNVTPNAQGTHNGYFYSWWSDGQSPVTYTNSAGGSYSVEWSSGGNLVGGKGWNPGSAKEIRYSASWQPTNNSNSYLTIYGWTRSPLVEYYIVESHGEYNPGSSAEPRGEIEAHGSIYKLYESTRVQQPSIDGTQTFQQYWAIRQTHRTSGTVTTGTFFNAWAAAGMPIGQHNYMIVATEAYNSAGRASVVVETPP

[Multiple Choices]
A. 3.2.1.18
B. 5.2.1.8
C. 3.2.1.8
D. 2.7.13.3
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

> The exact sequence matches a UniProt entry annotated as EC 3.2.1.8, with the listed reaction of endohydrolysis of beta-D-xylosidic linkages in xylans. The EC annotation is attributed to a PROSITE-ProRule, so this supports the key as a computational annotation, not as independently established experimental evidence.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has an N-terminal secretion signal followed by a compact, aromatic-rich fungal enzyme region consistent with a secreted GH11-family xylanase; its conserved catalytic-glutamate pattern supports that family-level inference. This favors EC 3.2.1.8 over the other choices, which concern sialidase activity, peptidyl-prolyl isomerization, or histidine kinase activity.


**Missing item-specific fact**

> No direct substrate assay is supplied, so the exact catalytic activity is not experimentally demonstrated by the question input.


**Reason**

> A family-level sequence argument meaningfully distinguishes the xylanase choice; the judgment does not rely on recognizing the exact sequence or retrieving its database entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The supplied choices name distinct enzyme activities, and the sequence features favor the xylanase option.


### Important caveats

- The reviewer-only annotation matches the input sequence, but its EC evidence is computational (PROSITE-ProRule); it should not be represented as direct experimental confirmation.
- The author’s exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has an N-terminal secretion signal followed by a compact, aromatic-rich fungal enzyme region consistent with a secreted GH11-family xylanase; its conserved catalytic-glutamate pattern supports that family-level inference. This favors EC 3.2.1.8 over the other choices, which concern sialidase activity, peptidyl-prolyl isomerization, or histidine kinase activity.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "No direct substrate assay is supplied, so the exact catalytic activity is not experimentally demonstrated by the question input.",
    "reason": "A family-level sequence argument meaningfully distinguishes the xylanase choice; the judgment does not rely on recognizing the exact sequence or retrieving its database entry."
  },
  "case_id": "EC_number_0191",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry annotated as EC 3.2.1.8, with the listed reaction of endohydrolysis of beta-D-xylosidic linkages in xylans. The EC annotation is attributed to a PROSITE-ProRule, so this supports the key as a computational annotation, not as independently established experimental evidence."
  },
  "important_caveats": [
    "The reviewer-only annotation matches the input sequence, but its EC evidence is computational (PROSITE-ProRule); it should not be represented as direct experimental confirmation.",
    "The author’s exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied choices name distinct enzyme activities, and the sequence features favor the xylanase option."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0191",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry annotated as EC 3.2.1.8, with the listed reaction of endohydrolysis of beta-D-xylosidic linkages in xylans. The EC annotation is attributed to a PROSITE-ProRule, so this supports the key as a computational annotation, not as independently established experimental evidence.",
    "evidence_ids": ["C1", "C4", "C5", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has an N-terminal secretion signal followed by a compact, aromatic-rich fungal enzyme region consistent with a secreted GH11-family xylanase; its conserved catalytic-glutamate pattern supports that family-level inference. This favors EC 3.2.1.8 over the other choices, which concern sialidase activity, peptidyl-prolyl isomerization, or histidine kinase activity.",
    "missing_item_specific_fact": "No direct substrate assay is supplied, so the exact catalytic activity is not experimentally demonstrated by the question input.",
    "reason": "A family-level sequence argument meaningfully distinguishes the xylanase choice; the judgment does not rely on recognizing the exact sequence or retrieving its database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied choices name distinct enzyme activities, and the sequence features favor the xylanase option."
  },
  "important_caveats": [
    "The reviewer-only annotation matches the input sequence, but its EC evidence is computational (PROSITE-ProRule); it should not be represented as direct experimental confirmation.",
    "The author’s exact source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry G2X5X8 (EIX4_VERDV, Verticillium dahliae) annotates this protein with EC 3.2.1.8 (Endo-1,4-beta-xylanase) based on PROSITE-ProRule PRU01097 (Glycoside hydrolase family 11 signature). The catalytic activity comment states 'Endohydrolysis of (1->4)-beta-D-xylosidic linkages in xylans.' The sequence matches the benchmark sequence exactly. The annotation is computational inference (ECO:0000255, PROSITE-ProRule) rather than direct experimental assay, but the protein is named 'Ethylene-inducing xylanase 4' with alternative name 'Endo-1,4-beta-xylanase EIX4,' and the GH11 family assignment is well-supported by the sequence motifs present.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H1](#evidence-h1), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The N-terminal signal peptide (MVSFSTLLTACTAITGALGTP) indicates a secreted enzyme, effectively eliminating 2.7.13.3 (glutamate 5-kinase, an intracellular cytoplasmic enzyme) and 5.2.1.8 (retinene isomerase, a multi-pass membrane protein in the visual cycle). The mature protein (~180 residues) is small and lacks transmembrane topology, further excluding 5.2.1.8. Between the remaining glycoside hydrolases (3.2.1.18 chitinase vs. 3.2.1.8 xylanase), the sequence contains GG-rich motifs ('VEWSSGGNLVGGKGW', 'SAGGSYSVEWSSGG') and a pattern of conserved Glu/Tyr/Trp residues characteristic of the GH11 β-jelly-roll fold rather than the DXXDXDXE catalytic motif of GH18 chitinases. The overall composition and small size are consistent with secreted fungal GH11 xylanases.


**Missing item-specific fact**

> Precise recognition of GH11-specific sequence signatures (e.g., the conserved catalytic Glu positions and the 'GG' insertion loops) versus GH18 chitinase motifs requires domain-level knowledge of glycoside hydrolase families, though this is general enzyme-family knowledge rather than a single protein-specific lookup.


**Reason**

> A model with knowledge of protein family signatures can reason from the signal peptide (secreted → not kinase, not membrane isomerase), the small size, and the GG-rich GH11-like motifs to favor 3.2.1.8 over 3.2.1.18. The distinction between C and A is not trivially obvious but is grounded in identifiable sequence features of GH11 versus GH18 families, making this reasoning-supported rather than pure database lookup.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> While both A (3.2.1.18) and C (3.2.1.8) are glycoside hydrolases, the GG-rich motifs and absence of a canonical GH18 DXXDXDXE catalytic motif in the sequence favor GH11. The signal peptide and small size clearly eliminate B and D. No option is equally defensible as C given the sequence features.


### Important caveats

- The EC 3.2.1.8 annotation is based on PROSITE-ProRule computational inference (ECO:0000255), not a direct enzymatic assay. No experimental xylanase activity measurement is cited in the evidence.
- The protein is a precursor (221 AA with signal peptide); the active enzyme is the mature form after signal peptide cleavage.
- The protein is also an ethylene-inducing elicitor (EIX), meaning its biological role extends beyond xylanase catalysis, but the EC number reflects its catalytic (xylanase) activity.
- The distinction between GH11 (3.2.1.8) and GH18 (3.2.1.18) from raw sequence requires family-level motif knowledge; a model without this knowledge might find A and C difficult to separate.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal signal peptide (MVSFSTLLTACTAITGALGTP) indicates a secreted enzyme, effectively eliminating 2.7.13.3 (glutamate 5-kinase, an intracellular cytoplasmic enzyme) and 5.2.1.8 (retinene isomerase, a multi-pass membrane protein in the visual cycle). The mature protein (~180 residues) is small and lacks transmembrane topology, further excluding 5.2.1.8. Between the remaining glycoside hydrolases (3.2.1.18 chitinase vs. 3.2.1.8 xylanase), the sequence contains GG-rich motifs ('VEWSSGGNLVGGKGW', 'SAGGSYSVEWSSGG') and a pattern of conserved Glu/Tyr/Trp residues characteristic of the GH11 β-jelly-roll fold rather than the DXXDXDXE catalytic motif of GH18 chitinases. The overall composition and small size are consistent with secreted fungal GH11 xylanases.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "Precise recognition of GH11-specific sequence signatures (e.g., the conserved catalytic Glu positions and the 'GG' insertion loops) versus GH18 chitinase motifs requires domain-level knowledge of glycoside hydrolase families, though this is general enzyme-family knowledge rather than a single protein-specific lookup.",
    "reason": "A model with knowledge of protein family signatures can reason from the signal peptide (secreted → not kinase, not membrane isomerase), the small size, and the GG-rich GH11-like motifs to favor 3.2.1.8 over 3.2.1.18. The distinction between C and A is not trivially obvious but is grounded in identifiable sequence features of GH11 versus GH18 families, making this reasoning-supported rather than pure database lookup."
  },
  "case_id": "EC_number_0191",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H1",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "UniProt entry G2X5X8 (EIX4_VERDV, Verticillium dahliae) annotates this protein with EC 3.2.1.8 (Endo-1,4-beta-xylanase) based on PROSITE-ProRule PRU01097 (Glycoside hydrolase family 11 signature). The catalytic activity comment states 'Endohydrolysis of (1->4)-beta-D-xylosidic linkages in xylans.' The sequence matches the benchmark sequence exactly. The annotation is computational inference (ECO:0000255, PROSITE-ProRule) rather than direct experimental assay, but the protein is named 'Ethylene-inducing xylanase 4' with alternative name 'Endo-1,4-beta-xylanase EIX4,' and the GH11 family assignment is well-supported by the sequence motifs present."
  },
  "important_caveats": [
    "The EC 3.2.1.8 annotation is based on PROSITE-ProRule computational inference (ECO:0000255), not a direct enzymatic assay. No experimental xylanase activity measurement is cited in the evidence.",
    "The protein is a precursor (221 AA with signal peptide); the active enzyme is the mature form after signal peptide cleavage.",
    "The protein is also an ethylene-inducing elicitor (EIX), meaning its biological role extends beyond xylanase catalysis, but the EC number reflects its catalytic (xylanase) activity.",
    "The distinction between GH11 (3.2.1.8) and GH18 (3.2.1.18) from raw sequence requires family-level motif knowledge; a model without this knowledge might find A and C difficult to separate."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While both A (3.2.1.18) and C (3.2.1.8) are glycoside hydrolases, the GG-rich motifs and absence of a canonical GH18 DXXDXDXE catalytic motif in the sequence favor GH11. The signal peptide and small size clearly eliminate B and D. No option is equally defensible as C given the sequence features."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0191",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry G2X5X8 (EIX4_VERDV, Verticillium dahliae) annotates this protein with EC 3.2.1.8 (Endo-1,4-beta-xylanase) based on PROSITE-ProRule PRU01097 (Glycoside hydrolase family 11 signature). The catalytic activity comment states 'Endohydrolysis of (1->4)-beta-D-xylosidic linkages in xylans.' The sequence matches the benchmark sequence exactly. The annotation is computational inference (ECO:0000255, PROSITE-ProRule) rather than direct experimental assay, but the protein is named 'Ethylene-inducing xylanase 4' with alternative name 'Endo-1,4-beta-xylanase EIX4,' and the GH11 family assignment is well-supported by the sequence motifs present.",
    "evidence_ids": ["C4", "C5", "H1", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The N-terminal signal peptide (MVSFSTLLTACTAITGALGTP) indicates a secreted enzyme, effectively eliminating 2.7.13.3 (glutamate 5-kinase, an intracellular cytoplasmic enzyme) and 5.2.1.8 (retinene isomerase, a multi-pass membrane protein in the visual cycle). The mature protein (~180 residues) is small and lacks transmembrane topology, further excluding 5.2.1.8. Between the remaining glycoside hydrolases (3.2.1.18 chitinase vs. 3.2.1.8 xylanase), the sequence contains GG-rich motifs ('VEWSSGGNLVGGKGW', 'SAGGSYSVEWSSGG') and a pattern of conserved Glu/Tyr/Trp residues characteristic of the GH11 β-jelly-roll fold rather than the DXXDXDXE catalytic motif of GH18 chitinases. The overall composition and small size are consistent with secreted fungal GH11 xylanases.",
    "missing_item_specific_fact": "Precise recognition of GH11-specific sequence signatures (e.g., the conserved catalytic Glu positions and the 'GG' insertion loops) versus GH18 chitinase motifs requires domain-level knowledge of glycoside hydrolase families, though this is general enzyme-family knowledge rather than a single protein-specific lookup.",
    "reason": "A model with knowledge of protein family signatures can reason from the signal peptide (secreted → not kinase, not membrane isomerase), the small size, and the GG-rich GH11-like motifs to favor 3.2.1.8 over 3.2.1.18. The distinction between C and A is not trivially obvious but is grounded in identifiable sequence features of GH11 versus GH18 families, making this reasoning-supported rather than pure database lookup."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While both A (3.2.1.18) and C (3.2.1.8) are glycoside hydrolases, the GG-rich motifs and absence of a canonical GH18 DXXDXDXE catalytic motif in the sequence favor GH11. The signal peptide and small size clearly eliminate B and D. No option is equally defensible as C given the sequence features."
  },
  "important_caveats": [
    "The EC 3.2.1.8 annotation is based on PROSITE-ProRule computational inference (ECO:0000255), not a direct enzymatic assay. No experimental xylanase activity measurement is cited in the evidence.",
    "The protein is a precursor (221 AA with signal peptide); the active enzyme is the mature form after signal peptide cleavage.",
    "The protein is also an ethylene-inducing elicitor (EIX), meaning its biological role extends beyond xylanase catalysis, but the EC number reflects its catalytic (xylanase) activity.",
    "The distinction between GH11 (3.2.1.8) and GH18 (3.2.1.18) from raw sequence requires family-level motif knowledge; a model without this knowledge might find A and C difficult to separate."
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

**Accession:** `G2X5X8` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 59. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G2X5X8.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:38.390496+00:00.  

```json
"G2X5X8"
```

Source SHA-256: `0dfdc578abe73de43e82b219133109e0a8de7b7fc008becaf6f430ce76cd2012`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G2X5X8.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:38.390496+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"33205907","source":"PubMed"}],"value":"Endo-1,4-beta-xylanase EIX4"}}],"flag":"Precursor","recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000255","id":"PRU01097","source":"PROSITE-ProRule"}],"value":"3.2.1.8"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"33205907","source":"PubMed"}],"value":"Ethylene-inducing xylanase 4"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"33205907","source":"PubMed"}],"value":"EIX4"}]}}
```

Source SHA-256: `0dfdc578abe73de43e82b219133109e0a8de7b7fc008becaf6f430ce76cd2012`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G2X5X8.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:38.390496+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"3.2.1.8","evidences":[{"evidenceCode":"ECO:0000255","id":"PRU01097","source":"PROSITE-ProRule"}],"name":"Endohydrolysis of (1->4)-beta-D-xylosidic linkages in xylans."}}
```

Source SHA-256: `0dfdc578abe73de43e82b219133109e0a8de7b7fc008becaf6f430ce76cd2012`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G2X5X8?format=txt&versions=59)  
**Locator:** `lines 1-16`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 59 / 1.  
**Retrieved:** 2026-11-02T04:28:42.014577+00:00.  

```text
ID   EIX4_VERDV              Reviewed;         221 AA.
AC   G2X5X8;
DT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.
DT   16-NOV-2011, sequence version 1.
DT   28-JAN-2026, entry version 59.
DE   RecName: Full=Ethylene-inducing xylanase 4 {ECO:0000303|PubMed:33205907};
DE            Short=EIX4 {ECO:0000303|PubMed:33205907};
DE            EC=3.2.1.8 {ECO:0000255|PROSITE-ProRule:PRU01097};
DE   AltName: Full=Endo-1,4-beta-xylanase EIX4 {ECO:0000303|PubMed:33205907};
DE   Flags: Precursor;
GN   Name=EIX4 {ECO:0000303|PubMed:33205907}; ORFNames=VDAG_05294;
OS   Verticillium dahliae (strain VdLs.17 / ATCC MYA-4575 / FGSC 10137)
OS   (Verticillium wilt).
OC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Sordariomycetes;
OC   Hypocreomycetidae; Glomerellales; Plectosphaerellaceae; Verticillium.
OX   NCBI_TaxID=498257;
```

Source SHA-256: `5dd26d11f0073a6c766ef016b0c6982afb7d2092a3f2cdf64c2e3271d9576b1c`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G2X5X8?format=txt&versions=59)  
**Locator:** `lines 6-10`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 59 / 1.  
**Retrieved:** 2026-11-02T04:28:42.014577+00:00.  

```text
DE   RecName: Full=Ethylene-inducing xylanase 4 {ECO:0000303|PubMed:33205907};
DE            Short=EIX4 {ECO:0000303|PubMed:33205907};
DE            EC=3.2.1.8 {ECO:0000255|PROSITE-ProRule:PRU01097};
DE   AltName: Full=Endo-1,4-beta-xylanase EIX4 {ECO:0000303|PubMed:33205907};
DE   Flags: Precursor;
```

Source SHA-256: `5dd26d11f0073a6c766ef016b0c6982afb7d2092a3f2cdf64c2e3271d9576b1c`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G2X5X8?format=txt&versions=59)  
**Locator:** `lines 44-46`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 59 / 1.  
**Retrieved:** 2026-11-02T04:28:42.014577+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=Endohydrolysis of (1->4)-beta-D-xylosidic linkages in xylans.;
CC         EC=3.2.1.8; Evidence={ECO:0000255|PROSITE-ProRule:PRU01097};
```

Source SHA-256: `5dd26d11f0073a6c766ef016b0c6982afb7d2092a3f2cdf64c2e3271d9576b1c`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 191. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
