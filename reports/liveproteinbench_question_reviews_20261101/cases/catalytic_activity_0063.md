# catalytic_activity_0063

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `catalytic_activity`  
**Author expected answer:** **B** — Endohydrolysis of (1-&gt;4)-beta-D-xylosidic linkages in xylans.

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MVSFSTLLTACTAITGALGTPDLDRRQNVTPNAQGTHNGYFYSWWSDGQSPVTYTNSAGGSYSVEWSSGGNLVGGKGWNPGSAKEIRYSASWQPTNNSNSYLTIYGWTRSPLVEYYIVESHGEYNPGSSAEPRGEIEAHGSIYKLYESTRVQQPSIDGTQTFQQYWAIRQTHRTSGTVTTGTFFNAWAAAGMPIGQHNYMIVATEAYNSAGRASVVVETPP

[Multiple Choices]
A. (2R)-2,3-dihydroxy-3-methylbutanoate = 3-methyl-2-oxobutanoate + H2O
B. Endohydrolysis of (1->4)-beta-D-xylosidic linkages in xylans.
C. 32-oxoeburicol + reduced [NADPH--hemoprotein reductase] + O2 = 14-demethyleburicol + formate + oxidized [NADPH--hemoprotein reductase] + H2O + 2 H(+)
D. (1S,4S)-4-[(4-methoxyphenyl)methyl]-2-methyl-2,5-diazaspiro[bicyclo[3.2.1]octane-6,1'-cyclohexan]-4'-one + 2-oxoglutarate + O2 = (2S)-3-(4-methoxyphenyl)-2-[(3S)-3-(methylamino)-8-oxo-1-azaspiro[4.5]decan-1-yl]propanal + succinate + CO2
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Enzymatic Reaction Prediction, which is to identify the specific chemical reaction catalyzed by a given enzyme. This involves understanding the enzyme's function based on its amino acid sequence and then selecting the correct transformation of substrates into products from a list of possible reactions.. The inputs provided by the user for this task include:

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

> The supplied sequence exactly matches the sequence in UniProt entries annotated as ethylene-inducing xylanase 4, with the catalytic activity in choice B. The activity annotation is supported by a PROSITE-ProRule computational inference, not by the cited reference as direct experimental evidence of catalysis.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H1](#evidence-h1), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence is compatible with a secreted fungal enzyme, but that broad context does not establish the specific substrate linkage or distinguish xylan hydrolysis from the other listed reactions.


**Missing item-specific fact**

> The protein-specific annotation or experimental characterization identifying this sequence as a xylanase with the activity in B.


**Reason**

> Choosing B requires a protein-specific function assignment absent from the input; recognizing the exact sequence or consulting its annotation would supply that fact.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The choices describe distinct reactions, and the sequence-matched annotation supports B; no alternative choice is supported by the supplied evidence.


### Important caveats

- The catalytic-activity evidence is computationally inferred from a PROSITE-ProRule; the excerpts do not independently establish direct experimental measurement of this reaction.
- The annotation source snapshot used by the benchmark author is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is compatible with a secreted fungal enzyme, but that broad context does not establish the specific substrate linkage or distinguish xylan hydrolysis from the other listed reactions.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific annotation or experimental characterization identifying this sequence as a xylanase with the activity in B.",
    "reason": "Choosing B requires a protein-specific function assignment absent from the input; recognizing the exact sequence or consulting its annotation would supply that fact."
  },
  "case_id": "catalytic_activity_0063",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H1",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the sequence in UniProt entries annotated as ethylene-inducing xylanase 4, with the catalytic activity in choice B. The activity annotation is supported by a PROSITE-ProRule computational inference, not by the cited reference as direct experimental evidence of catalysis."
  },
  "important_caveats": [
    "The catalytic-activity evidence is computationally inferred from a PROSITE-ProRule; the excerpts do not independently establish direct experimental measurement of this reaction.",
    "The annotation source snapshot used by the benchmark author is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The choices describe distinct reactions, and the sequence-matched annotation supports B; no alternative choice is supported by the supplied evidence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0063",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the sequence in UniProt entries annotated as ethylene-inducing xylanase 4, with the catalytic activity in choice B. The activity annotation is supported by a PROSITE-ProRule computational inference, not by the cited reference as direct experimental evidence of catalysis.",
    "evidence_ids": ["C1", "C4", "C5", "H1", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence is compatible with a secreted fungal enzyme, but that broad context does not establish the specific substrate linkage or distinguish xylan hydrolysis from the other listed reactions.",
    "missing_item_specific_fact": "The protein-specific annotation or experimental characterization identifying this sequence as a xylanase with the activity in B.",
    "reason": "Choosing B requires a protein-specific function assignment absent from the input; recognizing the exact sequence or consulting its annotation would supply that fact."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The choices describe distinct reactions, and the sequence-matched annotation supports B; no alternative choice is supported by the supplied evidence."
  },
  "important_caveats": [
    "The catalytic-activity evidence is computationally inferred from a PROSITE-ProRule; the excerpts do not independently establish direct experimental measurement of this reaction.",
    "The annotation source snapshot used by the benchmark author is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence matches UniProt entry G2X5X8 (EIX4_VERDV, Ethylene-inducing xylanase 4) from Verticillium dahliae. The catalytic activity is explicitly annotated as 'Endohydrolysis of (1->4)-beta-D-xylosidic linkages in xylans' with EC 3.2.1.8. The EC assignment is via PROSITE-ProRule (ECO:0000255, PRU01097), a computational profile-based annotation, but the protein name and functional context are supported by PubMed:33205907. The sequence match is exact in both current and historical (entry version 59) records.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 221-residue sequence begins with a hydrophobic N-terminal stretch (MVSFSTLLTACTAITGALGTPD) consistent with a signal peptide, indicating a secreted protein. This eliminates option A (dihydroxy-acid dehydratase, an intracellular enzyme in branched-chain amino acid biosynthesis, typically ~400+ aa) and option C (cytochrome P450, a membrane-associated enzyme with a highly conserved heme-binding motif FxxGxxxCxG that is absent here, and typically 400-600+ aa). The small size and aromatic-residue-rich composition (multiple Trp, Tyr, Phe clusters such as WWSDG, WSSGG, WPGSAKEIRYSASW, WTRSPL) are hallmarks of glycoside hydrolase family 11 xylanases. Option D (2-oxoglutarate-dependent dioxygenase acting on an extremely specific synthetic spiro-compound) lacks the characteristic HxD/E...H facial triad and the overall fold architecture. Among the four choices, only B describes a secreted glycoside hydrolase reaction, consistent with the sequence features.


**Missing item-specific fact**

> Precise recognition of GH11-specific conserved motifs (e.g., the exact catalytic Glu positions and the beta-jelly roll aromatic cleft pattern per PROSITE PRU01097) to positively confirm xylanase rather than another small secreted hydrolase (e.g., GH10, GH45) would require family-specific pattern knowledge. However, among the four provided options, elimination of A, C, and D through general protein-feature reasoning leaves B as the only viable glycoside hydrolase choice.


**Reason**

> The sequence provides sufficient general biological features (signal peptide, small size, aromatic richness, absence of P450 heme motif, absence of 2-OG dioxygenase triad, inconsistency with intracellular TIM-barrel DHAD) to meaningfully distinguish B from A, C, and D through reasoning about protein architecture and localization.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options represent distinct enzyme classes (aldolase/dehydratase, glycoside hydrolase, P450 monooxygenase, 2-oxoglutarate dioxygenase) with very different sequence signatures. The sequence features clearly favor a small secreted glycoside hydrolase, making B the uniquely defensible choice among the four.


### Important caveats

- The EC 3.2.1.8 assignment is via PROSITE-ProRule (computational profile match, ECO:0000255), not direct experimental kinetic characterization of this specific protein.
- The protein is named 'Ethylene-inducing xylanase 4' based on literature (PubMed:33205907), which primarily discusses its role as a plant immune elicitor; direct xylanase activity measurement on this specific EIX4 variant may rely on family-level inference.
- The reviewer-only evidence was not available to the evaluated model; the reasoning assessment is based solely on the sequence and choices provided in the original question.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 221-residue sequence begins with a hydrophobic N-terminal stretch (MVSFSTLLTACTAITGALGTPD) consistent with a signal peptide, indicating a secreted protein. This eliminates option A (dihydroxy-acid dehydratase, an intracellular enzyme in branched-chain amino acid biosynthesis, typically ~400+ aa) and option C (cytochrome P450, a membrane-associated enzyme with a highly conserved heme-binding motif FxxGxxxCxG that is absent here, and typically 400-600+ aa). The small size and aromatic-residue-rich composition (multiple Trp, Tyr, Phe clusters such as WWSDG, WSSGG, WPGSAKEIRYSASW, WTRSPL) are hallmarks of glycoside hydrolase family 11 xylanases. Option D (2-oxoglutarate-dependent dioxygenase acting on an extremely specific synthetic spiro-compound) lacks the characteristic HxD/E...H facial triad and the overall fold architecture. Among the four choices, only B describes a secreted glycoside hydrolase reaction, consistent with the sequence features.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "Precise recognition of GH11-specific conserved motifs (e.g., the exact catalytic Glu positions and the beta-jelly roll aromatic cleft pattern per PROSITE PRU01097) to positively confirm xylanase rather than another small secreted hydrolase (e.g., GH10, GH45) would require family-specific pattern knowledge. However, among the four provided options, elimination of A, C, and D through general protein-feature reasoning leaves B as the only viable glycoside hydrolase choice.",
    "reason": "The sequence provides sufficient general biological features (signal peptide, small size, aromatic richness, absence of P450 heme motif, absence of 2-OG dioxygenase triad, inconsistency with intracellular TIM-barrel DHAD) to meaningfully distinguish B from A, C, and D through reasoning about protein architecture and localization."
  },
  "case_id": "catalytic_activity_0063",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence matches UniProt entry G2X5X8 (EIX4_VERDV, Ethylene-inducing xylanase 4) from Verticillium dahliae. The catalytic activity is explicitly annotated as 'Endohydrolysis of (1->4)-beta-D-xylosidic linkages in xylans' with EC 3.2.1.8. The EC assignment is via PROSITE-ProRule (ECO:0000255, PRU01097), a computational profile-based annotation, but the protein name and functional context are supported by PubMed:33205907. The sequence match is exact in both current and historical (entry version 59) records."
  },
  "important_caveats": [
    "The EC 3.2.1.8 assignment is via PROSITE-ProRule (computational profile match, ECO:0000255), not direct experimental kinetic characterization of this specific protein.",
    "The protein is named 'Ethylene-inducing xylanase 4' based on literature (PubMed:33205907), which primarily discusses its role as a plant immune elicitor; direct xylanase activity measurement on this specific EIX4 variant may rely on family-level inference.",
    "The reviewer-only evidence was not available to the evaluated model; the reasoning assessment is based solely on the sequence and choices provided in the original question."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent distinct enzyme classes (aldolase/dehydratase, glycoside hydrolase, P450 monooxygenase, 2-oxoglutarate dioxygenase) with very different sequence signatures. The sequence features clearly favor a small secreted glycoside hydrolase, making B the uniquely defensible choice among the four."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0063",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches UniProt entry G2X5X8 (EIX4_VERDV, Ethylene-inducing xylanase 4) from Verticillium dahliae. The catalytic activity is explicitly annotated as 'Endohydrolysis of (1->4)-beta-D-xylosidic linkages in xylans' with EC 3.2.1.8. The EC assignment is via PROSITE-ProRule (ECO:0000255, PRU01097), a computational profile-based annotation, but the protein name and functional context are supported by PubMed:33205907. The sequence match is exact in both current and historical (entry version 59) records.",
    "evidence_ids": ["C4", "C5", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 221-residue sequence begins with a hydrophobic N-terminal stretch (MVSFSTLLTACTAITGALGTPD) consistent with a signal peptide, indicating a secreted protein. This eliminates option A (dihydroxy-acid dehydratase, an intracellular enzyme in branched-chain amino acid biosynthesis, typically ~400+ aa) and option C (cytochrome P450, a membrane-associated enzyme with a highly conserved heme-binding motif FxxGxxxCxG that is absent here, and typically 400-600+ aa). The small size and aromatic-residue-rich composition (multiple Trp, Tyr, Phe clusters such as WWSDG, WSSGG, WPGSAKEIRYSASW, WTRSPL) are hallmarks of glycoside hydrolase family 11 xylanases. Option D (2-oxoglutarate-dependent dioxygenase acting on an extremely specific synthetic spiro-compound) lacks the characteristic HxD/E...H facial triad and the overall fold architecture. Among the four choices, only B describes a secreted glycoside hydrolase reaction, consistent with the sequence features.",
    "missing_item_specific_fact": "Precise recognition of GH11-specific conserved motifs (e.g., the exact catalytic Glu positions and the beta-jelly roll aromatic cleft pattern per PROSITE PRU01097) to positively confirm xylanase rather than another small secreted hydrolase (e.g., GH10, GH45) would require family-specific pattern knowledge. However, among the four provided options, elimination of A, C, and D through general protein-feature reasoning leaves B as the only viable glycoside hydrolase choice.",
    "reason": "The sequence provides sufficient general biological features (signal peptide, small size, aromatic richness, absence of P450 heme motif, absence of 2-OG dioxygenase triad, inconsistency with intracellular TIM-barrel DHAD) to meaningfully distinguish B from A, C, and D through reasoning about protein architecture and localization."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent distinct enzyme classes (aldolase/dehydratase, glycoside hydrolase, P450 monooxygenase, 2-oxoglutarate dioxygenase) with very different sequence signatures. The sequence features clearly favor a small secreted glycoside hydrolase, making B the uniquely defensible choice among the four."
  },
  "important_caveats": [
    "The EC 3.2.1.8 assignment is via PROSITE-ProRule (computational profile match, ECO:0000255), not direct experimental kinetic characterization of this specific protein.",
    "The protein is named 'Ethylene-inducing xylanase 4' based on literature (PubMed:33205907), which primarily discusses its role as a plant immune elicitor; direct xylanase activity measurement on this specific EIX4 variant may rely on family-level inference.",
    "The reviewer-only evidence was not available to the evaluated model; the reasoning assessment is based solely on the sequence and choices provided in the original question."
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

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 63. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
