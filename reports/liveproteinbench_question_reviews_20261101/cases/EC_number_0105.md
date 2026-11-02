# EC_number_0105

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `EC_number`  
**Author expected answer:** **D** — 2.3.1.322

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MAPILQRISKTFIKPSSPTPESLRCYNLSSSDQMITSVYISLAFFYGSPGCESSRIRQQLDNSLSRTLVYYYPFAGRLVDNDHIDCNDQGVQFVEVRIHCPISAILKQTTSYAEDLVFPRGTSACHEDSLVVVQLNRFECGGVAIAVCISHKVADGSGAIAFINDWAATARVSSHIPSPLLVADSIFPHLDNSLPVPYNLSKNCVTRRFVFPAAEIEKLKSKAVESGLQQPTRVEVVTALLYQCALLASRSTNSGLSRPSVLIQAVNLRPFLVPPLPRNSVGNIFSINFSIIEVDSLEFPELAGRLRKAKLKFQNLSQEKLYYDSQMQELGECLKQLNTGNFDVYYCSSWCRFPVYDVDFGWGKPTWVCTVKSQIKDMIVLMDSPGDEIAAFVTLEEEKMSAFQHNELLLSFASLYSAK

[Multiple Choices]
A. 2.3.1.319
B. 1.14.11.53
C. 1.14.14.154
D. 2.3.1.322
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

> The exact sequence matches the UniProt entry annotated with EC 2.3.1.322. The entry attributes this EC number and the rhazimol acetylation reaction to experimental evidence (ECO:0000269) and PubMed 36349266; the historical entry also contains the annotation. This supports choice D, though the primary study was not independently reviewed here.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> Sequence features may suggest an acyltransferase rather than an oxygenase, but choices A and D are both acyltransferase EC numbers. The sequence and choices alone do not establish the enzyme's specific substrate reaction needed to distinguish them.


**Missing item-specific fact**

> The protein-specific catalytic activity: this enzyme catalyzes acetyl transfer from acetyl-CoA to rhazimol, producing akuammiline.


**Reason**

> Identifying the exact EC number requires the enzyme's specific catalytic activity, an item-specific fact absent from the supplied input. Recognizing the sequence or recalling its database annotation would be lookup or memorization, not reasoning from the provided evidence.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The annotated, experimentally supported reaction corresponds to D; no supplied evidence supports another listed EC number for this sequence.


### Important caveats

- The supporting annotation is tied to a cited experimental publication, but that publication was not independently examined.
- The sequence match and historical annotation are established by reviewer-only evidence, not information provided to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Sequence features may suggest an acyltransferase rather than an oxygenase, but choices A and D are both acyltransferase EC numbers. The sequence and choices alone do not establish the enzyme's specific substrate reaction needed to distinguish them.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific catalytic activity: this enzyme catalyzes acetyl transfer from acetyl-CoA to rhazimol, producing akuammiline.",
    "reason": "Identifying the exact EC number requires the enzyme's specific catalytic activity, an item-specific fact absent from the supplied input. Recognizing the sequence or recalling its database annotation would be lookup or memorization, not reasoning from the provided evidence."
  },
  "case_id": "EC_number_0105",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry annotated with EC 2.3.1.322. The entry attributes this EC number and the rhazimol acetylation reaction to experimental evidence (ECO:0000269) and PubMed 36349266; the historical entry also contains the annotation. This supports choice D, though the primary study was not independently reviewed here."
  },
  "important_caveats": [
    "The supporting annotation is tied to a cited experimental publication, but that publication was not independently examined.",
    "The sequence match and historical annotation are established by reviewer-only evidence, not information provided to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The annotated, experimentally supported reaction corresponds to D; no supplied evidence supports another listed EC number for this sequence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0105",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry annotated with EC 2.3.1.322. The entry attributes this EC number and the rhazimol acetylation reaction to experimental evidence (ECO:0000269) and PubMed 36349266; the historical entry also contains the annotation. This supports choice D, though the primary study was not independently reviewed here.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "Sequence features may suggest an acyltransferase rather than an oxygenase, but choices A and D are both acyltransferase EC numbers. The sequence and choices alone do not establish the enzyme's specific substrate reaction needed to distinguish them.",
    "missing_item_specific_fact": "The protein-specific catalytic activity: this enzyme catalyzes acetyl transfer from acetyl-CoA to rhazimol, producing akuammiline.",
    "reason": "Identifying the exact EC number requires the enzyme's specific catalytic activity, an item-specific fact absent from the supplied input. Recognizing the sequence or recalling its database annotation would be lookup or memorization, not reasoning from the provided evidence."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The annotated, experimentally supported reaction corresponds to D; no supplied evidence supports another listed EC number for this sequence."
  },
  "important_caveats": [
    "The supporting annotation is tied to a cited experimental publication, but that publication was not independently examined.",
    "The sequence match and historical annotation are established by reviewer-only evidence, not information provided to the evaluated model."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The protein sequence matches UniProt entry A0A9E7S5E3 exactly (sequence_comparison: matched, SHA-256 identical). The entry is annotated as Akuammiline synthase 1 (AsAKS1) with EC 2.3.1.322, supported by experimental evidence (ECO:0000269, PubMed:36349266). The catalytic reaction (rhazimol + acetyl-CoA → akuammiline + CoA + H⁺) confirms the acyltransferase classification. Both current and historical (entry version 13) records confirm this annotation.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H1](#evidence-h1), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence contains a clear HxxDG motif (ISHKVADG) and a DPGx-like motif (SPGDE), characteristic of BAHD acyltransferases, and lacks the P450 heme-binding motif (FxxGxxxCxG) and Fe(II)/2-oxoglutarate dioxygenase motifs (HxD/E…H). The protein length (419 AA) is consistent with BAHD acyltransferases rather than P450s (~500+ AA) or 2OG-dependent oxygenases. This reasoning meaningfully rules out options B (1.14.11.53, Fe(II)/2OG-dependent dioxygenase) and C (1.14.14.154, P450 monooxygenase), narrowing to acyltransferases A (2.3.1.319) and D (2.3.1.322).


**Missing item-specific fact**

> Distinguishing EC 2.3.1.319 from EC 2.3.1.322 requires knowing the specific substrate of this enzyme (rhazimol acetylation to akuammiline vs. the substrate for 2.3.1.319). The specific active-site architecture determining substrate selectivity within the BAHD acyltransferase superfamily cannot be reliably inferred from the 419-residue sequence alone without structural data or a trained specificity predictor. This is an item-specific enzymological fact.


**Reason**

> While the broad EC class (2.3.1.x acyltransferase vs. 1.14.x.x oxidoreductase) is reasoning-supported via the HxxDG motif and absence of P450/dioxygenase signatures, the final distinction between the two acyltransferase options (A vs. D) depends on knowing the specific substrate identity of this particular enzyme, which is not derivable from sequence motifs alone.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "D"
]
```

> Both A (2.3.1.319) and D (2.3.1.322) are acyltransferases within the same EC subclass. Without specific knowledge of the enzyme's substrate (rhazimol → akuammiline), a model reasoning from sequence motifs alone cannot definitively choose between these two. The HxxDG and DPGx motifs confirm BAHD acyltransferase family membership but do not encode substrate specificity at the level of individual EC numbers.


### Important caveats

- The EC annotation is backed by experimental evidence (ECO:0000269) from a 2022 Chem. Sci. publication, not merely computational prediction.
- The protein is annotated as a BAHD acyltransferase (gene synonym BAHD3), consistent with the HxxDG motif observed.
- The distinction between ruling out B/C (reasoning-supported via motif analysis) and choosing between A/D (lookup-dependent) is the critical boundary for answerability.
- The reviewer-only evidence was not available to the evaluated model; the model must work solely from the 419-residue sequence and four EC number choices.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a clear HxxDG motif (ISHKVADG) and a DPGx-like motif (SPGDE), characteristic of BAHD acyltransferases, and lacks the P450 heme-binding motif (FxxGxxxCxG) and Fe(II)/2-oxoglutarate dioxygenase motifs (HxD/E…H). The protein length (419 AA) is consistent with BAHD acyltransferases rather than P450s (~500+ AA) or 2OG-dependent oxygenases. This reasoning meaningfully rules out options B (1.14.11.53, Fe(II)/2OG-dependent dioxygenase) and C (1.14.14.154, P450 monooxygenase), narrowing to acyltransferases A (2.3.1.319) and D (2.3.1.322).",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "Distinguishing EC 2.3.1.319 from EC 2.3.1.322 requires knowing the specific substrate of this enzyme (rhazimol acetylation to akuammiline vs. the substrate for 2.3.1.319). The specific active-site architecture determining substrate selectivity within the BAHD acyltransferase superfamily cannot be reliably inferred from the 419-residue sequence alone without structural data or a trained specificity predictor. This is an item-specific enzymological fact.",
    "reason": "While the broad EC class (2.3.1.x acyltransferase vs. 1.14.x.x oxidoreductase) is reasoning-supported via the HxxDG motif and absence of P450/dioxygenase signatures, the final distinction between the two acyltransferase options (A vs. D) depends on knowing the specific substrate identity of this particular enzyme, which is not derivable from sequence motifs alone."
  },
  "case_id": "EC_number_0105",
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
    "reason": "The protein sequence matches UniProt entry A0A9E7S5E3 exactly (sequence_comparison: matched, SHA-256 identical). The entry is annotated as Akuammiline synthase 1 (AsAKS1) with EC 2.3.1.322, supported by experimental evidence (ECO:0000269, PubMed:36349266). The catalytic reaction (rhazimol + acetyl-CoA → akuammiline + CoA + H⁺) confirms the acyltransferase classification. Both current and historical (entry version 13) records confirm this annotation."
  },
  "important_caveats": [
    "The EC annotation is backed by experimental evidence (ECO:0000269) from a 2022 Chem. Sci. publication, not merely computational prediction.",
    "The protein is annotated as a BAHD acyltransferase (gene synonym BAHD3), consistent with the HxxDG motif observed.",
    "The distinction between ruling out B/C (reasoning-supported via motif analysis) and choosing between A/D (lookup-dependent) is the critical boundary for answerability.",
    "The reviewer-only evidence was not available to the evaluated model; the model must work solely from the 419-residue sequence and four EC number choices."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "D"
    ],
    "reason": "Both A (2.3.1.319) and D (2.3.1.322) are acyltransferases within the same EC subclass. Without specific knowledge of the enzyme's substrate (rhazimol → akuammiline), a model reasoning from sequence motifs alone cannot definitively choose between these two. The HxxDG and DPGx motifs confirm BAHD acyltransferase family membership but do not encode substrate specificity at the level of individual EC numbers."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0105",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The protein sequence matches UniProt entry A0A9E7S5E3 exactly (sequence_comparison: matched, SHA-256 identical). The entry is annotated as Akuammiline synthase 1 (AsAKS1) with EC 2.3.1.322, supported by experimental evidence (ECO:0000269, PubMed:36349266). The catalytic reaction (rhazimol + acetyl-CoA → akuammiline + CoA + H⁺) confirms the acyltransferase classification. Both current and historical (entry version 13) records confirm this annotation.",
    "evidence_ids": ["C1", "C4", "C5", "H1", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence contains a clear HxxDG motif (ISHKVADG) and a DPGx-like motif (SPGDE), characteristic of BAHD acyltransferases, and lacks the P450 heme-binding motif (FxxGxxxCxG) and Fe(II)/2-oxoglutarate dioxygenase motifs (HxD/E…H). The protein length (419 AA) is consistent with BAHD acyltransferases rather than P450s (~500+ AA) or 2OG-dependent oxygenases. This reasoning meaningfully rules out options B (1.14.11.53, Fe(II)/2OG-dependent dioxygenase) and C (1.14.14.154, P450 monooxygenase), narrowing to acyltransferases A (2.3.1.319) and D (2.3.1.322).",
    "missing_item_specific_fact": "Distinguishing EC 2.3.1.319 from EC 2.3.1.322 requires knowing the specific substrate of this enzyme (rhazimol acetylation to akuammiline vs. the substrate for 2.3.1.319). The specific active-site architecture determining substrate selectivity within the BAHD acyltransferase superfamily cannot be reliably inferred from the 419-residue sequence alone without structural data or a trained specificity predictor. This is an item-specific enzymological fact.",
    "reason": "While the broad EC class (2.3.1.x acyltransferase vs. 1.14.x.x oxidoreductase) is reasoning-supported via the HxxDG motif and absence of P450/dioxygenase signatures, the final distinction between the two acyltransferase options (A vs. D) depends on knowing the specific substrate identity of this particular enzyme, which is not derivable from sequence motifs alone."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "D"],
    "reason": "Both A (2.3.1.319) and D (2.3.1.322) are acyltransferases within the same EC subclass. Without specific knowledge of the enzyme's substrate (rhazimol → akuammiline), a model reasoning from sequence motifs alone cannot definitively choose between these two. The HxxDG and DPGx motifs confirm BAHD acyltransferase family membership but do not encode substrate specificity at the level of individual EC numbers."
  },
  "important_caveats": [
    "The EC annotation is backed by experimental evidence (ECO:0000269) from a 2022 Chem. Sci. publication, not merely computational prediction.",
    "The protein is annotated as a BAHD acyltransferase (gene synonym BAHD3), consistent with the HxxDG motif observed.",
    "The distinction between ruling out B/C (reasoning-supported via motif analysis) and choosing between A/D (lookup-dependent) is the critical boundary for answerability.",
    "The reviewer-only evidence was not available to the evaluated model; the model must work solely from the 419-residue sequence and four EC number choices."
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

**Accession:** `A0A9E7S5E3` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 13. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9E7S5E3.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:54.493793+00:00.  

```json
"A0A9E7S5E3"
```

Source SHA-256: `dccc1e1f78f84ddf8a52309526ec78e3e0e822b2e5e5620c9b28bd1314fc2e3d`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9E7S5E3.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:54.493793+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"36349266","source":"PubMed"}],"value":"2.3.1.322"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"36349266","source":"PubMed"}],"value":"Akuammiline synthase 1"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"36349266","source":"PubMed"}],"value":"AsAKS1"}]}}
```

Source SHA-256: `dccc1e1f78f84ddf8a52309526ec78e3e0e822b2e5e5620c9b28bd1314fc2e3d`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9E7S5E3.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:54.493793+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000269","id":"36349266","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:79624"}}],"reaction":{"ecNumber":"2.3.1.322","evidences":[{"evidenceCode":"ECO:0000269","id":"36349266","source":"PubMed"}],"name":"rhazimol + acetyl-CoA = akuammiline + CoA + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:79623"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:57287"},{"database":"ChEBI","id":"CHEBI:57288"},{"database":"ChEBI","id":"CHEBI:141879"},{"database":"ChEBI","id":"CHEBI:230474"}]}}
```

Source SHA-256: `dccc1e1f78f84ddf8a52309526ec78e3e0e822b2e5e5620c9b28bd1314fc2e3d`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9E7S5E3.json)  
**Locator:** `/references/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:54.493793+00:00.  

```json
{"citation":{"authors":["Wang Z.","Xiao Y.","Wu S.","Chen J.","Li A.","Tatsis E.C."],"citationCrossReferences":[{"database":"PubMed","id":"36349266"},{"database":"DOI","id":"10.1039/d2sc03612f"}],"citationType":"journal article","firstPage":"12389","id":"36349266","journal":"Chem. Sci.","lastPage":"12395","publicationDate":"2022","title":"Deciphering and reprogramming the cyclization regioselectivity in bifurcation of indole alkaloid biosynthesis.","volume":"13"},"evidences":[{"evidenceCode":"ECO:0000312","id":"URS65387.1","source":"EMBL"}],"referenceNumber":1,"referencePositions":["NUCLEOTIDE SEQUENCE [MRNA]","FUNCTION","CATALYTIC ACTIVITY","PATHWAY","BIOPHYSICOCHEMICAL PROPERTIES"]}
```

Source SHA-256: `dccc1e1f78f84ddf8a52309526ec78e3e0e822b2e5e5620c9b28bd1314fc2e3d`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A9E7S5E3?format=txt&versions=13)  
**Locator:** `lines 1-16`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 13 / 1.  
**Retrieved:** 2026-11-01T06:27:37.651074+00:00.  

```text
ID   AKS1_ALSSC              Reviewed;         419 AA.
AC   A0A9E7S5E3;
DT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.
DT   03-MAY-2023, sequence version 1.
DT   28-JAN-2026, entry version 13.
DE   RecName: Full=Akuammiline synthase 1 {ECO:0000303|PubMed:36349266};
DE            Short=AsAKS1 {ECO:0000303|PubMed:36349266};
DE            EC=2.3.1.322 {ECO:0000269|PubMed:36349266};
GN   Name=AKS1 {ECO:0000303|PubMed:36349266};
GN   Synonyms=BAHD3 {ECO:0000303|PubMed:36349266};
OS   Alstonia scholaris (Dogbane) (Echites scholaris).
OC   Eukaryota; Viridiplantae; Streptophyta; Embryophyta; Tracheophyta;
OC   Spermatophyta; Magnoliopsida; eudicotyledons; Gunneridae; Pentapetalae;
OC   asterids; lamiids; Gentianales; Apocynaceae; Rauvolfioideae; Alstonieae;
OC   Alstonia.
OX   NCBI_TaxID=52822;
```

Source SHA-256: `1462d014137043d064b721b692e151871424684911f566849eb4da04580f0a54`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A9E7S5E3?format=txt&versions=13)  
**Locator:** `lines 6-8`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 13 / 1.  
**Retrieved:** 2026-11-01T06:27:37.651074+00:00.  

```text
DE   RecName: Full=Akuammiline synthase 1 {ECO:0000303|PubMed:36349266};
DE            Short=AsAKS1 {ECO:0000303|PubMed:36349266};
DE            EC=2.3.1.322 {ECO:0000269|PubMed:36349266};
```

Source SHA-256: `1462d014137043d064b721b692e151871424684911f566849eb4da04580f0a54`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A9E7S5E3?format=txt&versions=13)  
**Locator:** `lines 31-37`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 13 / 1.  
**Retrieved:** 2026-11-01T06:27:37.651074+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=rhazimol + acetyl-CoA = akuammiline + CoA + H(+);
CC         Xref=Rhea:RHEA:79623, ChEBI:CHEBI:15378, ChEBI:CHEBI:57287,
CC         ChEBI:CHEBI:57288, ChEBI:CHEBI:141879, ChEBI:CHEBI:230474;
CC         EC=2.3.1.322; Evidence={ECO:0000269|PubMed:36349266};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:79624;
CC         Evidence={ECO:0000269|PubMed:36349266};
```

Source SHA-256: `1462d014137043d064b721b692e151871424684911f566849eb4da04580f0a54`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 105. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
