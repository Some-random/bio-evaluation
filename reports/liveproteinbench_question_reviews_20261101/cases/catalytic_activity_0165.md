# catalytic_activity_0165

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
MRFSASLLLALTGSAAASPIRAEEEIRVYDLPISLFDDLQGLDAAMKAAGREYIGTSLTVRNDFQEQNIIRTEFGSITPENAQKWDATEPNRGQFTFGSADQHMDWARQNGKHVRCHTLVWYSQLPGWVSNSGFNNATLQQVMQNHINQVMGRYRGRCNHWDVVNEAPRLMAMRLQIGEAYIPIAFRMAAQADPSAKLYYNDYNLEYLGPKVEGAARIVRLVKQYGARIDGVGYQAHLVTEPTPTQSTPTPSEEDLIKALRITADLGVDVAYTEIDIRMRTPSNAQKLQQLADAYYRVARSCMKVPRCVGMTIWGVTDRYSWVPNTFRGEGDALLWDSNYQRKAAYNAFLRGIQEPVN

[Multiple Choices]
A. 3-hydroxy-4,5-dimethoxyphenethylamine + S-adenosyl-L-methionine = N-methyl-3-hydroxy-4,5-dimethoxyphenethylamine + S-adenosyl-L-homocysteine + H(+)
B. Endohydrolysis of (1->4)-beta-D-xylosidic linkages in xylans.
C. a 14alpha-hydroxymethyl steroid + reduced [NADPH--hemoprotein reductase] + O2 = a 14alpha-formyl steroid + oxidized [NADPH--hemoprotein reductase] + 2 H2O + H(+)
D. (E)-cinnamyl alcohol + NADP(+) = (E)-cinnamaldehyde + NADPH + H(+)
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

> The sequence exactly matches the UniProt entry annotated as endo-1,4-beta-xylanase B, with the catalytic activity in choice B. The activity annotation cites experimental evidence from PubMed 23306124; this supports the key, though the primary study was not independently reviewed here.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H4](#evidence-h4), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The N-terminal hydrophobic segment is consistent with a secreted protein, and the sequence does not show the characteristic heme-binding motif expected for choice C or an obvious cofactor-dependent signature for choices A or D. That makes a secreted hydrolase plausible, but does not by itself establish xylan as its substrate or the specific cleavage reaction in B.


**Missing item-specific fact**

> The protein-specific identification as an endo-1,4-beta-xylanase, or equivalent experimentally established substrate and activity information, is absent from the input.


**Reason**

> The choices permit broad class-level clues, but selecting the specific xylan hydrolysis reaction depends on identifying this particular protein or its enzyme family and activity; the supplied sequence alone does not make that substrate specificity explicit.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The options describe distinct reaction types, and the sequence-matched activity annotation supports B.


### Important caveats

- The reviewer-only database evidence was not supplied to the evaluated model.
- The cited annotation provides experimental evidence attribution, but the primary paper was not independently validated here.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal hydrophobic segment is consistent with a secreted protein, and the sequence does not show the characteristic heme-binding motif expected for choice C or an obvious cofactor-dependent signature for choices A or D. That makes a secreted hydrolase plausible, but does not by itself establish xylan as its substrate or the specific cleavage reaction in B.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific identification as an endo-1,4-beta-xylanase, or equivalent experimentally established substrate and activity information, is absent from the input.",
    "reason": "The choices permit broad class-level clues, but selecting the specific xylan hydrolysis reaction depends on identifying this particular protein or its enzyme family and activity; the supplied sequence alone does not make that substrate specificity explicit."
  },
  "case_id": "catalytic_activity_0165",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H4",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The sequence exactly matches the UniProt entry annotated as endo-1,4-beta-xylanase B, with the catalytic activity in choice B. The activity annotation cites experimental evidence from PubMed 23306124; this supports the key, though the primary study was not independently reviewed here."
  },
  "important_caveats": [
    "The reviewer-only database evidence was not supplied to the evaluated model.",
    "The cited annotation provides experimental evidence attribution, but the primary paper was not independently validated here."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The options describe distinct reaction types, and the sequence-matched activity annotation supports B."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0165",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence exactly matches the UniProt entry annotated as endo-1,4-beta-xylanase B, with the catalytic activity in choice B. The activity annotation cites experimental evidence from PubMed 23306124; this supports the key, though the primary study was not independently reviewed here.",
    "evidence_ids": ["C4", "C5", "H4", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The N-terminal hydrophobic segment is consistent with a secreted protein, and the sequence does not show the characteristic heme-binding motif expected for choice C or an obvious cofactor-dependent signature for choices A or D. That makes a secreted hydrolase plausible, but does not by itself establish xylan as its substrate or the specific cleavage reaction in B.",
    "missing_item_specific_fact": "The protein-specific identification as an endo-1,4-beta-xylanase, or equivalent experimentally established substrate and activity information, is absent from the input.",
    "reason": "The choices permit broad class-level clues, but selecting the specific xylan hydrolysis reaction depends on identifying this particular protein or its enzyme family and activity; the supplied sequence alone does not make that substrate specificity explicit."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The options describe distinct reaction types, and the sequence-matched activity annotation supports B."
  },
  "important_caveats": [
    "The reviewer-only database evidence was not supplied to the evaluated model.",
    "The cited annotation provides experimental evidence attribution, but the primary paper was not independently validated here."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence matches UniProt entry M4MLB5 (XYNB_HUMIN) exactly (SHA256 confirmed). The entry is annotated as Endo-1,4-beta-xylanase B (EC 3.2.1.8) with catalytic activity 'Endohydrolysis of (1->4)-beta-D-xylosidic linkages in xylans,' supported by experimental evidence (ECO:0000269, PubMed:23306124, Du et al. 2013, Bioresour. Technol.). This is a direct match to Choice B.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence begins with a clear signal peptide (MRFSASLLLALTGSAAASPIR), indicating a secreted protein from a fungus—consistent with plant cell wall degradation. Among the four choices, three require specific cofactor-binding structural motifs that are absent from the sequence: (C) a P450 monooxygenase requires a heme-binding FxxGxxxCxG motif (not present); (D) an oxidoreductase requires a Rossmann-fold GxGxxG motif (not present); (A) a SAM-dependent methyltransferase requires characteristic SAM-binding motifs (not present). Only (B), a glycoside hydrolase acting on xylan, is consistent with a secreted fungal enzyme lacking these cofactor motifs. Additionally, the sequence contains motifs loosely consistent with GH10 xylanase family signatures (e.g., WDSNYQR, WVPNTFRGEG regions), further supporting a glycoside hydrolase assignment. Since B is the sole glycoside hydrolase option, elimination of the other three by absent cofactor motifs is a valid reasoning path.


**Missing item-specific fact**

> None strictly required. Positive confirmation of GH10 family membership (vs. other GH families) would benefit from database lookup, but is unnecessary because B is the only glycoside hydrolase among the four choices.


**Reason**

> The four options span four distinct enzyme classes (methyltransferase, glycoside hydrolase, P450 monooxygenase, oxidoreductase). The sequence's signal peptide, fungal origin, and absence of heme-binding, Rossmann-fold, and SAM-binding motifs provide a concrete biological argument to eliminate A, C, and D, leaving B as the only viable option. This is achievable through general enzymology knowledge without memorizing this specific protein's annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four choices represent mechanistically distinct enzyme classes requiring different cofactors and structural motifs. The sequence is inconsistent with three of them, leaving only the glycoside hydrolase option viable.


### Important caveats

- The annotation is experimentally supported (ECO:0000269), not merely computational.
- The reasoning path relies on recognizing the absence of cofactor motifs for the distractor enzyme classes; a model unfamiliar with these motifs might struggle.
- Positive identification of GH10 family specifically (vs. GH11 or other GH families) would require more specialized motif knowledge, but is not needed to select among the given four options.
- The UniProt entry was first released in 2025-02-05; the author's source snapshot is unknown but the sequence matches across versions.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence begins with a clear signal peptide (MRFSASLLLALTGSAAASPIR), indicating a secreted protein from a fungus—consistent with plant cell wall degradation. Among the four choices, three require specific cofactor-binding structural motifs that are absent from the sequence: (C) a P450 monooxygenase requires a heme-binding FxxGxxxCxG motif (not present); (D) an oxidoreductase requires a Rossmann-fold GxGxxG motif (not present); (A) a SAM-dependent methyltransferase requires characteristic SAM-binding motifs (not present). Only (B), a glycoside hydrolase acting on xylan, is consistent with a secreted fungal enzyme lacking these cofactor motifs. Additionally, the sequence contains motifs loosely consistent with GH10 xylanase family signatures (e.g., WDSNYQR, WVPNTFRGEG regions), further supporting a glycoside hydrolase assignment. Since B is the sole glycoside hydrolase option, elimination of the other three by absent cofactor motifs is a valid reasoning path.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None strictly required. Positive confirmation of GH10 family membership (vs. other GH families) would benefit from database lookup, but is unnecessary because B is the only glycoside hydrolase among the four choices.",
    "reason": "The four options span four distinct enzyme classes (methyltransferase, glycoside hydrolase, P450 monooxygenase, oxidoreductase). The sequence's signal peptide, fungal origin, and absence of heme-binding, Rossmann-fold, and SAM-binding motifs provide a concrete biological argument to eliminate A, C, and D, leaving B as the only viable option. This is achievable through general enzymology knowledge without memorizing this specific protein's annotation."
  },
  "case_id": "catalytic_activity_0165",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H2",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence matches UniProt entry M4MLB5 (XYNB_HUMIN) exactly (SHA256 confirmed). The entry is annotated as Endo-1,4-beta-xylanase B (EC 3.2.1.8) with catalytic activity 'Endohydrolysis of (1->4)-beta-D-xylosidic linkages in xylans,' supported by experimental evidence (ECO:0000269, PubMed:23306124, Du et al. 2013, Bioresour. Technol.). This is a direct match to Choice B."
  },
  "important_caveats": [
    "The annotation is experimentally supported (ECO:0000269), not merely computational.",
    "The reasoning path relies on recognizing the absence of cofactor motifs for the distractor enzyme classes; a model unfamiliar with these motifs might struggle.",
    "Positive identification of GH10 family specifically (vs. GH11 or other GH families) would require more specialized motif knowledge, but is not needed to select among the given four options.",
    "The UniProt entry was first released in 2025-02-05; the author's source snapshot is unknown but the sequence matches across versions."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices represent mechanistically distinct enzyme classes requiring different cofactors and structural motifs. The sequence is inconsistent with three of them, leaving only the glycoside hydrolase option viable."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0165",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches UniProt entry M4MLB5 (XYNB_HUMIN) exactly (SHA256 confirmed). The entry is annotated as Endo-1,4-beta-xylanase B (EC 3.2.1.8) with catalytic activity 'Endohydrolysis of (1->4)-beta-D-xylosidic linkages in xylans,' supported by experimental evidence (ECO:0000269, PubMed:23306124, Du et al. 2013, Bioresour. Technol.). This is a direct match to Choice B.",
    "evidence_ids": ["C4", "C5", "C6", "H2", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence begins with a clear signal peptide (MRFSASLLLALTGSAAASPIR), indicating a secreted protein from a fungus—consistent with plant cell wall degradation. Among the four choices, three require specific cofactor-binding structural motifs that are absent from the sequence: (C) a P450 monooxygenase requires a heme-binding FxxGxxxCxG motif (not present); (D) an oxidoreductase requires a Rossmann-fold GxGxxG motif (not present); (A) a SAM-dependent methyltransferase requires characteristic SAM-binding motifs (not present). Only (B), a glycoside hydrolase acting on xylan, is consistent with a secreted fungal enzyme lacking these cofactor motifs. Additionally, the sequence contains motifs loosely consistent with GH10 xylanase family signatures (e.g., WDSNYQR, WVPNTFRGEG regions), further supporting a glycoside hydrolase assignment. Since B is the sole glycoside hydrolase option, elimination of the other three by absent cofactor motifs is a valid reasoning path.",
    "missing_item_specific_fact": "None strictly required. Positive confirmation of GH10 family membership (vs. other GH families) would benefit from database lookup, but is unnecessary because B is the only glycoside hydrolase among the four choices.",
    "reason": "The four options span four distinct enzyme classes (methyltransferase, glycoside hydrolase, P450 monooxygenase, oxidoreductase). The sequence's signal peptide, fungal origin, and absence of heme-binding, Rossmann-fold, and SAM-binding motifs provide a concrete biological argument to eliminate A, C, and D, leaving B as the only viable option. This is achievable through general enzymology knowledge without memorizing this specific protein's annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices represent mechanistically distinct enzyme classes requiring different cofactors and structural motifs. The sequence is inconsistent with three of them, leaving only the glycoside hydrolase option viable."
  },
  "important_caveats": [
    "The annotation is experimentally supported (ECO:0000269), not merely computational.",
    "The reasoning path relies on recognizing the absence of cofactor motifs for the distractor enzyme classes; a model unfamiliar with these motifs might struggle.",
    "Positive identification of GH10 family specifically (vs. GH11 or other GH families) would require more specialized motif knowledge, but is not needed to select among the given four options.",
    "The UniProt entry was first released in 2025-02-05; the author's source snapshot is unknown but the sequence matches across versions."
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

**Accession:** `M4MLB5` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 31. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/M4MLB5.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:12.159556+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"1,4-beta-D-xylan xylanohydrolase B"}}],"flag":"Precursor","recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"23306124","source":"PubMed"}],"value":"3.2.1.8"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"23306124","source":"PubMed"}],"value":"Endo-1,4-beta-xylanase B"}}}
```

Source SHA-256: `9737e107c7508ede0abc7bd8c8f14f35fc885d5000f5778fdd13b8d4054f912f`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/M4MLB5.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:12.159556+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"3.2.1.8","evidences":[{"evidenceCode":"ECO:0000269","id":"23306124","source":"PubMed"}],"name":"Endohydrolysis of (1->4)-beta-D-xylosidic linkages in xylans."}}
```

Source SHA-256: `9737e107c7508ede0abc7bd8c8f14f35fc885d5000f5778fdd13b8d4054f912f`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/M4MLB5.json)  
**Locator:** `/references/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:12.159556+00:00.  

```json
{"citation":{"authors":["Du Y.","Shi P.","Huang H.","Zhang X.","Luo H.","Wang Y.","Yao B."],"citationCrossReferences":[{"database":"PubMed","id":"23306124"},{"database":"DOI","id":"10.1016/j.biortech.2012.12.067"}],"citationType":"journal article","firstPage":"161","id":"23306124","journal":"Bioresour. Technol.","lastPage":"167","publicationDate":"2013","title":"Characterization of three novel thermophilic xylanases from Humicola insolens Y1 with application potentials in the brewing industry.","volume":"130"},"referenceComments":[{"type":"STRAIN","value":"Y1"}],"referenceNumber":1,"referencePositions":["NUCLEOTIDE SEQUENCE [MRNA]","FUNCTION","CATALYTIC ACTIVITY","BIOPHYSICOCHEMICAL PROPERTIES","SUBSTRATE SPECIFICITY","ACTIVITY REGULATION","BIOTECHNOLOGY"]}
```

Source SHA-256: `9737e107c7508ede0abc7bd8c8f14f35fc885d5000f5778fdd13b8d4054f912f`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/M4MLB5?format=txt&versions=31)  
**Locator:** `lines 6-9`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 31 / 1.  
**Retrieved:** 2026-11-01T06:28:16.229298+00:00.  

```text
DE   RecName: Full=Endo-1,4-beta-xylanase B {ECO:0000303|PubMed:23306124};
DE            EC=3.2.1.8 {ECO:0000269|PubMed:23306124};
DE   AltName: Full=1,4-beta-D-xylan xylanohydrolase B {ECO:0000305};
DE   Flags: Precursor;
```

Source SHA-256: `8a61ff0bb76d82894c8a3570170d306b45992420e142ae76129e353039c9cab6`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/M4MLB5?format=txt&versions=31)  
**Locator:** `lines 15-24`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 31 / 1.  
**Retrieved:** 2026-11-01T06:28:16.229298+00:00.  

```text
RN   [1]
RP   NUCLEOTIDE SEQUENCE [MRNA], FUNCTION, CATALYTIC ACTIVITY,
RP   BIOPHYSICOCHEMICAL PROPERTIES, SUBSTRATE SPECIFICITY, ACTIVITY REGULATION,
RP   AND BIOTECHNOLOGY.
RC   STRAIN=Y1;
RX   PubMed=23306124; DOI=10.1016/j.biortech.2012.12.067;
RA   Du Y., Shi P., Huang H., Zhang X., Luo H., Wang Y., Yao B.;
RT   "Characterization of three novel thermophilic xylanases from Humicola
RT   insolens Y1 with application potentials in the brewing industry.";
RL   Bioresour. Technol. 130:161-167(2013).
```

Source SHA-256: `8a61ff0bb76d82894c8a3570170d306b45992420e142ae76129e353039c9cab6`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/M4MLB5?format=txt&versions=31)  
**Locator:** `lines 40-42`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 31 / 1.  
**Retrieved:** 2026-11-01T06:28:16.229298+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=Endohydrolysis of (1->4)-beta-D-xylosidic linkages in xylans.;
CC         EC=3.2.1.8; Evidence={ECO:0000269|PubMed:23306124};
```

Source SHA-256: `8a61ff0bb76d82894c8a3570170d306b45992420e142ae76129e353039c9cab6`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 165. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
