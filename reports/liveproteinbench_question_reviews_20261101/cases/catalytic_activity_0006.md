# catalytic_activity_0006

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `catalytic_activity`  
**Author expected answer:** **B** — a CDP-1,2-diacyl-sn-glycerol + a 1,2-diacyl-sn-glycero-3-phospho-(1&#x27;-sn-glycerol) = a cardiolipin + CMP + H(+)

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MASGQMAPSLLRRPITFVSSCPPALRSFGALCPPTGSTDLIGGTGRDILIAAAPARRAPLHATLPLLRSLHTSPAPQLSASHQHQAQQQQQQTKQPQQPYDPQQDQVPSTSTASSSKPAADPVYNLPNAVSVARLVSGPLIGYWLVQGHYEAATLALAVSGASDWLDGWLARRLGASSVFGSYLDPLADKVLIGCVAAALLMNGAMPGWVAGVVVGRDVLLVAGSFVFRLRGFGWRWPGAAAFFRTVDTSAAAAGAATGAANGVASGGGGGGEGVSFMRPLLISKANTVLQLLLLGGYLLRGMDGGAGLQLLLPGGGGEELIMGLELATAATTVASGLAYGTMAVQGKLFK

[Multiple Choices]
A. a (3E,5Z)-dienoyl-CoA = a (2E,4E)-(5,6-saturated)-dienoyl-CoA
B. a CDP-1,2-diacyl-sn-glycerol + a 1,2-diacyl-sn-glycero-3-phospho-(1'-sn-glycerol) = a cardiolipin + CMP + H(+)
C. (1S,4S)-4-[(4-methoxyphenyl)methyl]-2,5-diazaspiro[bicyclo[3.2.1]octane-6,1'-cyclohexan]-4'-one + S-adenosyl-L-methionine = (1S,4S)-4-[(4-methoxyphenyl)methyl]-2-methyl-2,5-diazaspiro[bicyclo[3.2.1]octane-6,1'-cyclohexan]-4'-one + S-adenosyl-L-homocysteine + H(+)
D. Hydrolysis of terminal, non-reducing (1->4)-linked alpha-D-glucose residues with release of alpha-D-glucose.
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

> The supplied sequence exactly matches the UniProt entry annotated as a CMP-forming cardiolipin synthase, whose catalytic reaction is choice B. The annotation cites a publication, but the excerpts do not independently establish the experimental details.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence is strongly hydrophobic, consistent with a membrane protein, but that broad feature does not establish its specific catalytic reaction or distinguish choice B from the alternatives.


**Missing item-specific fact**

> The protein-specific functional identification as CMP-forming cardiolipin synthase, or equivalent evidence linking this sequence to that activity, is not provided in the question.


**Reason**

> Selecting B depends on knowing the function of this particular protein; the supplied sequence and choices offer no sufficiently specific biological argument for its reaction.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The matched-sequence annotation specifies choice B; no competing reaction is supported by the supplied reviewer evidence.


### Important caveats

- The sequence match and functional annotation come from reviewer-only UniProt evidence and were not supplied to the evaluated model.
- The cited evidence code is ECO:0000305, and the excerpts do not include independent validation of the primary experimental results.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is strongly hydrophobic, consistent with a membrane protein, but that broad feature does not establish its specific catalytic reaction or distinguish choice B from the alternatives.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific functional identification as CMP-forming cardiolipin synthase, or equivalent evidence linking this sequence to that activity, is not provided in the question.",
    "reason": "Selecting B depends on knowing the function of this particular protein; the supplied sequence and choices offer no sufficiently specific biological argument for its reaction."
  },
  "case_id": "catalytic_activity_0006",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the UniProt entry annotated as a CMP-forming cardiolipin synthase, whose catalytic reaction is choice B. The annotation cites a publication, but the excerpts do not independently establish the experimental details."
  },
  "important_caveats": [
    "The sequence match and functional annotation come from reviewer-only UniProt evidence and were not supplied to the evaluated model.",
    "The cited evidence code is ECO:0000305, and the excerpts do not include independent validation of the primary experimental results."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched-sequence annotation specifies choice B; no competing reaction is supported by the supplied reviewer evidence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0006",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the UniProt entry annotated as a CMP-forming cardiolipin synthase, whose catalytic reaction is choice B. The annotation cites a publication, but the excerpts do not independently establish the experimental details.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence is strongly hydrophobic, consistent with a membrane protein, but that broad feature does not establish its specific catalytic reaction or distinguish choice B from the alternatives.",
    "missing_item_specific_fact": "The protein-specific functional identification as CMP-forming cardiolipin synthase, or equivalent evidence linking this sequence to that activity, is not provided in the question.",
    "reason": "Selecting B depends on knowing the function of this particular protein; the supplied sequence and choices offer no sufficiently specific biological argument for its reaction."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched-sequence annotation specifies choice B; no competing reaction is supported by the supplied reviewer evidence."
  },
  "important_caveats": [
    "The sequence match and functional annotation come from reviewer-only UniProt evidence and were not supplied to the evaluated model.",
    "The cited evidence code is ECO:0000305, and the excerpts do not include independent validation of the primary experimental results."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The supplied 351-residue sequence exactly matches UniProt entry A0A2K3D1C8 (CRLS1_CHLRE), annotated as Cardiolipin synthase (CMP-forming), EC 2.7.8.41. The catalytic activity annotation (C5, H4) states exactly: 'a CDP-1,2-diacyl-sn-glycerol + a 1,2-diacyl-sn-glycero-3-phospho-(1'-sn-glycerol) = a cardiolipin + CMP + H(+)', matching Choice B verbatim. The evidence code is ECO:0000305 (inferred from direct assay), supported by functional characterization in PubMed:26793177 (Hung et al., 2015, Front. Microbiol.), which identified and characterized CrCLS1 in Chlamydomonas reinhardtii. Both current (v33) and historical (v31) records confirm the match.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence is clearly polytopic membrane protein (multiple hydrophobic stretches), which weakly disfavors D (soluble glucoamylase) and C (soluble methyltransferase). One might attempt to spot a DRD-like motif (e.g., 'GRDILI' near position 55, 'GRDVLL' near position 230) suggestive of the CDP-alcohol phosphatidyltransferase superfamily, which would point toward B. However, these motifs are degenerate in this sequence and not unambiguously identifiable from the raw string without prior family knowledge. Distinguishing cardiolipin synthase (CMP-forming) from a dienoyl-CoA reductase (also membrane-bound, Choice A) requires recognizing the specific protein or its family annotation.


**Missing item-specific fact**

> Recognition of the specific protein as CrCLS1 (cardiolipin synthase) or reliable identification of the CDP-alcohol phosphatidyltransferase family signature motifs (the canonical DxxxxDR and GxxxxD motifs are present but degenerate and embedded in a long hydrophobic sequence), plus the distinction between CMP-forming and phosphatidylglycerol-forming cardiolipin synthase subtypes.


**Reason**

> While the membrane-protein character and possible DRD-like motifs provide weak hints toward a phosphatidyltransferase, the sequence does not contain a uniquely identifiable catalytic motif that a model could confidently extract and map to cardiolipin synthase without prior database knowledge or sequence recognition. The correct answer is effectively determined by recognizing the protein (or its family) rather than by deductive reasoning from general biochemical principles.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four choices span very different enzyme classes (reductase, phosphatidyltransferase, methyltransferase, hydrolase), so if the correct family is identified, only B fits. No other option is defensible for this sequence.


### Important caveats

- The annotation evidence code ECO:0000305 indicates inference from direct assay (functional characterization in the 2015 paper), not merely computational prediction, strengthening the key.
- The sequence is 351 residues with extensive hydrophobic stretches; motif identification (DRD, GxxxD) from raw sequence is unreliable without alignment to known family members.
- The distinction between CMP-forming and phosphatidylglycerol-forming cardiolipin synthase is not trivially readable from sequence; the annotation specifies the CMP-forming variant based on experimental data.
- All evidence is reviewer-only and was absent from the evaluated model's input.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is clearly polytopic membrane protein (multiple hydrophobic stretches), which weakly disfavors D (soluble glucoamylase) and C (soluble methyltransferase). One might attempt to spot a DRD-like motif (e.g., 'GRDILI' near position 55, 'GRDVLL' near position 230) suggestive of the CDP-alcohol phosphatidyltransferase superfamily, which would point toward B. However, these motifs are degenerate in this sequence and not unambiguously identifiable from the raw string without prior family knowledge. Distinguishing cardiolipin synthase (CMP-forming) from a dienoyl-CoA reductase (also membrane-bound, Choice A) requires recognizing the specific protein or its family annotation.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "Recognition of the specific protein as CrCLS1 (cardiolipin synthase) or reliable identification of the CDP-alcohol phosphatidyltransferase family signature motifs (the canonical DxxxxDR and GxxxxD motifs are present but degenerate and embedded in a long hydrophobic sequence), plus the distinction between CMP-forming and phosphatidylglycerol-forming cardiolipin synthase subtypes.",
    "reason": "While the membrane-protein character and possible DRD-like motifs provide weak hints toward a phosphatidyltransferase, the sequence does not contain a uniquely identifiable catalytic motif that a model could confidently extract and map to cardiolipin synthase without prior database knowledge or sequence recognition. The correct answer is effectively determined by recognizing the protein (or its family) rather than by deductive reasoning from general biochemical principles."
  },
  "case_id": "catalytic_activity_0006",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "H1",
      "H2",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The supplied 351-residue sequence exactly matches UniProt entry A0A2K3D1C8 (CRLS1_CHLRE), annotated as Cardiolipin synthase (CMP-forming), EC 2.7.8.41. The catalytic activity annotation (C5, H4) states exactly: 'a CDP-1,2-diacyl-sn-glycerol + a 1,2-diacyl-sn-glycero-3-phospho-(1'-sn-glycerol) = a cardiolipin + CMP + H(+)', matching Choice B verbatim. The evidence code is ECO:0000305 (inferred from direct assay), supported by functional characterization in PubMed:26793177 (Hung et al., 2015, Front. Microbiol.), which identified and characterized CrCLS1 in Chlamydomonas reinhardtii. Both current (v33) and historical (v31) records confirm the match."
  },
  "important_caveats": [
    "The annotation evidence code ECO:0000305 indicates inference from direct assay (functional characterization in the 2015 paper), not merely computational prediction, strengthening the key.",
    "The sequence is 351 residues with extensive hydrophobic stretches; motif identification (DRD, GxxxD) from raw sequence is unreliable without alignment to known family members.",
    "The distinction between CMP-forming and phosphatidylglycerol-forming cardiolipin synthase is not trivially readable from sequence; the annotation specifies the CMP-forming variant based on experimental data.",
    "All evidence is reviewer-only and was absent from the evaluated model's input."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices span very different enzyme classes (reductase, phosphatidyltransferase, methyltransferase, hydrolase), so if the correct family is identified, only B fits. No other option is defensible for this sequence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0006",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied 351-residue sequence exactly matches UniProt entry A0A2K3D1C8 (CRLS1_CHLRE), annotated as Cardiolipin synthase (CMP-forming), EC 2.7.8.41. The catalytic activity annotation (C5, H4) states exactly: 'a CDP-1,2-diacyl-sn-glycerol + a 1,2-diacyl-sn-glycero-3-phospho-(1'-sn-glycerol) = a cardiolipin + CMP + H(+)', matching Choice B verbatim. The evidence code is ECO:0000305 (inferred from direct assay), supported by functional characterization in PubMed:26793177 (Hung et al., 2015, Front. Microbiol.), which identified and characterized CrCLS1 in Chlamydomonas reinhardtii. Both current (v33) and historical (v31) records confirm the match.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H1", "H2", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence is clearly polytopic membrane protein (multiple hydrophobic stretches), which weakly disfavors D (soluble glucoamylase) and C (soluble methyltransferase). One might attempt to spot a DRD-like motif (e.g., 'GRDILI' near position 55, 'GRDVLL' near position 230) suggestive of the CDP-alcohol phosphatidyltransferase superfamily, which would point toward B. However, these motifs are degenerate in this sequence and not unambiguously identifiable from the raw string without prior family knowledge. Distinguishing cardiolipin synthase (CMP-forming) from a dienoyl-CoA reductase (also membrane-bound, Choice A) requires recognizing the specific protein or its family annotation.",
    "missing_item_specific_fact": "Recognition of the specific protein as CrCLS1 (cardiolipin synthase) or reliable identification of the CDP-alcohol phosphatidyltransferase family signature motifs (the canonical DxxxxDR and GxxxxD motifs are present but degenerate and embedded in a long hydrophobic sequence), plus the distinction between CMP-forming and phosphatidylglycerol-forming cardiolipin synthase subtypes.",
    "reason": "While the membrane-protein character and possible DRD-like motifs provide weak hints toward a phosphatidyltransferase, the sequence does not contain a uniquely identifiable catalytic motif that a model could confidently extract and map to cardiolipin synthase without prior database knowledge or sequence recognition. The correct answer is effectively determined by recognizing the protein (or its family) rather than by deductive reasoning from general biochemical principles."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices span very different enzyme classes (reductase, phosphatidyltransferase, methyltransferase, hydrolase), so if the correct family is identified, only B fits. No other option is defensible for this sequence."
  },
  "important_caveats": [
    "The annotation evidence code ECO:0000305 indicates inference from direct assay (functional characterization in the 2015 paper), not merely computational prediction, strengthening the key.",
    "The sequence is 351 residues with extensive hydrophobic stretches; motif identification (DRD, GxxxD) from raw sequence is unreliable without alignment to known family members.",
    "The distinction between CMP-forming and phosphatidylglycerol-forming cardiolipin synthase is not trivially readable from sequence; the annotation specifies the CMP-forming variant based on experimental data.",
    "All evidence is reviewer-only and was absent from the evaluated model's input."
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

**Accession:** `A0A2K3D1C8` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 31. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2K3D1C8.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:48.321314+00:00.  

```json
"A0A2K3D1C8"
```

Source SHA-256: `26e9b73e0d86ca30bf42039424c27469e24cd0f504b95de4718d0e72ea3a9a16`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2K3D1C8.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:48.321314+00:00.  

```json
{"flag":"Precursor","recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000305","id":"26793177","source":"PubMed"}],"value":"2.7.8.41"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Cardiolipin synthase (CMP-forming)"},"shortNames":[{"value":"CLS"}]}}
```

Source SHA-256: `26e9b73e0d86ca30bf42039424c27469e24cd0f504b95de4718d0e72ea3a9a16`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2K3D1C8.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:48.321314+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"2.7.8.41","evidences":[{"evidenceCode":"ECO:0000305","id":"26793177","source":"PubMed"}],"name":"a CDP-1,2-diacyl-sn-glycerol + a 1,2-diacyl-sn-glycero-3-phospho-(1'-sn-glycerol) = a cardiolipin + CMP + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:32931"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:58332"},{"database":"ChEBI","id":"CHEBI:60377"},{"database":"ChEBI","id":"CHEBI:62237"},{"database":"ChEBI","id":"CHEBI:64716"}]}}
```

Source SHA-256: `26e9b73e0d86ca30bf42039424c27469e24cd0f504b95de4718d0e72ea3a9a16`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2K3D1C8.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:48.321314+00:00.  

```json
{"citation":{"authors":["Hung C.H.","Kobayashi K.","Wada H.","Nakamura Y."],"citationCrossReferences":[{"database":"PubMed","id":"26793177"},{"database":"DOI","id":"10.3389/fmicb.2015.01542"}],"citationType":"journal article","firstPage":"1542","id":"26793177","journal":"Front. Microbiol.","lastPage":"1542","publicationDate":"2015","title":"Functional Specificity of Cardiolipin Synthase Revealed by the Identification of a Cardiolipin Synthase CrCLS1 in Chlamydomonas reinhardtii.","volume":"6"},"evidences":[{"evidenceCode":"ECO:0000305"}],"referenceNumber":2,"referencePositions":["FUNCTION","CATALYTIC ACTIVITY"]}
```

Source SHA-256: `26e9b73e0d86ca30bf42039424c27469e24cd0f504b95de4718d0e72ea3a9a16`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2K3D1C8?format=txt&versions=31)  
**Locator:** `lines 1-14`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 31 / 1.  
**Retrieved:** 2026-11-02T04:24:52.248527+00:00.  

```text
ID   CRLS1_CHLRE             Reviewed;         351 AA.
AC   A0A2K3D1C8;
DT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.
DT   28-MAR-2018, sequence version 1.
DT   28-JAN-2026, entry version 31.
DE   RecName: Full=Cardiolipin synthase (CMP-forming) {ECO:0000305};
DE            Short=CLS;
DE            EC=2.7.8.41 {ECO:0000305|PubMed:26793177};
DE   Flags: Precursor;
GN   ORFNames=CHLRE_13g604700v5 {ECO:0000312|EMBL:PNW74341.1};
OS   Chlamydomonas reinhardtii (Chlamydomonas smithii).
OC   Eukaryota; Viridiplantae; Chlorophyta; core chlorophytes; Chlorophyceae;
OC   CS clade; Chlamydomonadales; Chlamydomonadaceae; Chlamydomonas.
OX   NCBI_TaxID=3055 {ECO:0000312|Proteomes:UP000006906};
```

Source SHA-256: `59f1e23ac2c4d5a40557e3d481dab63f297277a1a4b73ab6748fe911f7d4716c`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2K3D1C8?format=txt&versions=31)  
**Locator:** `lines 6-9`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 31 / 1.  
**Retrieved:** 2026-11-02T04:24:52.248527+00:00.  

```text
DE   RecName: Full=Cardiolipin synthase (CMP-forming) {ECO:0000305};
DE            Short=CLS;
DE            EC=2.7.8.41 {ECO:0000305|PubMed:26793177};
DE   Flags: Precursor;
```

Source SHA-256: `59f1e23ac2c4d5a40557e3d481dab63f297277a1a4b73ab6748fe911f7d4716c`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2K3D1C8?format=txt&versions=31)  
**Locator:** `lines 43-50`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 31 / 1.  
**Retrieved:** 2026-11-02T04:24:52.248527+00:00.  

```text
RN   [2] {ECO:0000305}
RP   FUNCTION, AND CATALYTIC ACTIVITY.
RX   PubMed=26793177; DOI=10.3389/fmicb.2015.01542;
RA   Hung C.H., Kobayashi K., Wada H., Nakamura Y.;
RT   "Functional Specificity of Cardiolipin Synthase Revealed by the
RT   Identification of a Cardiolipin Synthase CrCLS1 in Chlamydomonas
RT   reinhardtii.";
RL   Front. Microbiol. 6:1542-1542(2015).
```

Source SHA-256: `59f1e23ac2c4d5a40557e3d481dab63f297277a1a4b73ab6748fe911f7d4716c`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2K3D1C8?format=txt&versions=31)  
**Locator:** `lines 60-65`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 31 / 1.  
**Retrieved:** 2026-11-02T04:24:52.248527+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=a CDP-1,2-diacyl-sn-glycerol + a 1,2-diacyl-sn-glycero-3-
CC         phospho-(1'-sn-glycerol) = a cardiolipin + CMP + H(+);
CC         Xref=Rhea:RHEA:32931, ChEBI:CHEBI:15378, ChEBI:CHEBI:58332,
CC         ChEBI:CHEBI:60377, ChEBI:CHEBI:62237, ChEBI:CHEBI:64716; EC=2.7.8.41;
CC         Evidence={ECO:0000305|PubMed:26793177};
```

Source SHA-256: `59f1e23ac2c4d5a40557e3d481dab63f297277a1a4b73ab6748fe911f7d4716c`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 6. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
