# catalytic_activity_0167

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `catalytic_activity`  
**Author expected answer:** **A** — 2 a Fe(II)-siderophore + NAD(+) + H(+) = 2 a Fe(III)-siderophore + NADH

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MTKIAEKSKQEYGDLLKEKDHLQDMEQLEMTIVSIQTPYPSIVRIQGKINTLQPELWQAPNLAIRLIVSNPPEGQPISRVYTVRSFNPINAQIEIDFVKHEDLSPAMEWLNSAQVGTKIGLIGPRPHFIPNFTAKKHVVMFADDTAVPALYSILKQWELGISADIFIESFEKDIASQLPELEHVKIHSFHKEHHTSQKGLLLKAAFALEHYENITIWAACERNEARALRQFFLEDQQLNKNDVRIAGYWRDGVSSSELDKLRAQHYQEHIQQGKTLNEYDDLDLAN

[Multiple Choices]
A. 2 a Fe(II)-siderophore + NAD(+) + H(+) = 2 a Fe(III)-siderophore + NADH
B. restrictinol + glycine + H(+) = restricticin + H2O
C. (19E)-geissoschizine + reduced [NADPH--hemoprotein reductase] + O2 = akuammicine + formate + oxidized [NADPH--hemoprotein reductase] + H2O + H(+)
D. N-[(R)-4-phosphopantothenoyl]-L-cysteine + H(+) = (R)-4'-phosphopantetheine + CO2
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

> The exact sequence matches the UniProt entry annotated as ferric acinetobactin reductase, and its catalytic-activity annotation gives the reaction in choice A with experimental evidence attributed to PubMed 34308084. The archived annotation available by the historical cutoff also records this reaction.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence may suggest an oxidoreductase, but it does not provide a sufficiently specific basis to identify the siderophore substrate and NAD(+) reaction over the other listed enzyme reactions.


**Missing item-specific fact**

> The protein-specific functional annotation or experimental characterization identifying this sequence as ferric acinetobactin reductase and establishing its reaction.


**Reason**

> Distinguishing the precise catalytic reaction requires a protein-specific functional fact absent from the input. Recognizing the exact sequence or retrieving its annotation would be lookup, not reasoning from the supplied information.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The reviewer-only annotation supports choice A; no other listed option is supported for this sequence.


### Important caveats

- The annotation is tied to experimental evidence in a cited publication, but the primary paper was not independently retrieved or validated here.
- The source sequence matches exactly; the author's actual source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence may suggest an oxidoreductase, but it does not provide a sufficiently specific basis to identify the siderophore substrate and NAD(+) reaction over the other listed enzyme reactions.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific functional annotation or experimental characterization identifying this sequence as ferric acinetobactin reductase and establishing its reaction.",
    "reason": "Distinguishing the precise catalytic reaction requires a protein-specific functional fact absent from the input. Recognizing the exact sequence or retrieving its annotation would be lookup, not reasoning from the supplied information."
  },
  "case_id": "catalytic_activity_0167",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry annotated as ferric acinetobactin reductase, and its catalytic-activity annotation gives the reaction in choice A with experimental evidence attributed to PubMed 34308084. The archived annotation available by the historical cutoff also records this reaction."
  },
  "important_caveats": [
    "The annotation is tied to experimental evidence in a cited publication, but the primary paper was not independently retrieved or validated here.",
    "The source sequence matches exactly; the author's actual source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The reviewer-only annotation supports choice A; no other listed option is supported for this sequence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0167",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry annotated as ferric acinetobactin reductase, and its catalytic-activity annotation gives the reaction in choice A with experimental evidence attributed to PubMed 34308084. The archived annotation available by the historical cutoff also records this reaction.",
    "evidence_ids": ["C1", "C4", "C5", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence may suggest an oxidoreductase, but it does not provide a sufficiently specific basis to identify the siderophore substrate and NAD(+) reaction over the other listed enzyme reactions.",
    "missing_item_specific_fact": "The protein-specific functional annotation or experimental characterization identifying this sequence as ferric acinetobactin reductase and establishing its reaction.",
    "reason": "Distinguishing the precise catalytic reaction requires a protein-specific functional fact absent from the input. Recognizing the exact sequence or retrieving its annotation would be lookup, not reasoning from the supplied information."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The reviewer-only annotation supports choice A; no other listed option is supported for this sequence."
  },
  "important_caveats": [
    "The annotation is tied to experimental evidence in a cited publication, but the primary paper was not independently retrieved or validated here.",
    "The source sequence matches exactly; the author's actual source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A0A1E3M8P2 (sequence exactly matched, 286 aa, Acinetobacter baumannii) annotates the catalytic activity as '2 a Fe(II)-siderophore + NAD(+) + H(+) = 2 a Fe(III)-siderophore + NADH' (EC 1.16.1.10), with ECO:0000269 (direct assay) evidence from PubMed:34308084 and a 2.85 Å X-ray structure in complex with FAD (PDB 7LRN). Choice A is a verbatim match to this annotated reaction. A second annotated reaction uses NADP(+) instead of NAD(+), but that variant is not among the choices, so no conflict arises.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C7](#evidence-c7), [H2](#evidence-h2), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains glycine-rich stretches (e.g., GKINT, GVLIG, GPRPH) consistent with a Rossmann-like FAD-binding fold, indicating a flavoprotein oxidoreductase. Among the four choices, only A is an oxidoreductase reaction involving NAD+/NADH. Choice B is an amide-bond-forming ligase (requires ATP-binding/PPi-release motifs absent here). Choice C is a cytochrome P450 monooxygenase reaction (requires a heme-binding CxxGxxG/FGAGERVCPEG motif, absent). Choice D is a PLP-dependent or cofactor-independent decarboxylase (PPCDC-type, no PLP-binding motif present). Eliminating B, C, and D by absence of their characteristic structural motifs leaves A as the only reaction type compatible with a flavoprotein oxidoreductase. The specific substrate identity (Fe-siderophore) is an additional detail, but the reaction-class discrimination is achievable through sequence analysis.


**Missing item-specific fact**

> The specific substrate 'Fe(II)-siderophore / Fe(III)-siderophore' cannot be deduced purely from sequence without prior knowledge of siderophore-interacting protein (SIP) function; however, the reaction-type elimination logic is sufficient to select A among the four provided options.


**Reason**

> The four choices span four fundamentally different reaction classes (oxidoreductase, ligase, P450 monooxygenase, decarboxylase). Sequence-level features (FAD-binding glycine-rich motifs, absence of heme/PLP/ATP-binding signatures) allow a knowledgeable biologist to eliminate B, C, and D and select A as the only oxidoreductase. This constitutes a concrete biological argument from the supplied sequence rather than pure memorization of the database entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The enzyme has two annotated catalytic activities (NAD+ and NADP+ variants), but only the NAD+ variant (Choice A) appears among the options. The other three choices represent entirely different reaction types incompatible with the sequence features. No ambiguity exists among the provided options.


### Important caveats

- The UniProt annotation includes a physiologicalDirection of 'right-to-left' for both reactions, meaning the enzyme physiologically reduces Fe(III)-siderophore using NADH. Choice A writes the reaction in the forward (oxidation) direction as listed in Rhea; this is standard UniProt convention and does not constitute an error.
- The sequence-match is exact (SHA-256 identical) between the benchmark input and both the current (v37) and archived (v35) UniProt entries, confirming the evidence applies to the supplied protein.
- The FAD-binding motifs in this sequence are somewhat degenerate; confident identification as a flavoprotein from sequence alone requires expert-level fold recognition rather than simple motif matching.
- The specific substrate 'Fe-siderophore' is an item-specific annotation detail; a model selecting A purely by recognizing this exact sequence's database entry would be relying on memorization rather than reasoning.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains glycine-rich stretches (e.g., GKINT, GVLIG, GPRPH) consistent with a Rossmann-like FAD-binding fold, indicating a flavoprotein oxidoreductase. Among the four choices, only A is an oxidoreductase reaction involving NAD+/NADH. Choice B is an amide-bond-forming ligase (requires ATP-binding/PPi-release motifs absent here). Choice C is a cytochrome P450 monooxygenase reaction (requires a heme-binding CxxGxxG/FGAGERVCPEG motif, absent). Choice D is a PLP-dependent or cofactor-independent decarboxylase (PPCDC-type, no PLP-binding motif present). Eliminating B, C, and D by absence of their characteristic structural motifs leaves A as the only reaction type compatible with a flavoprotein oxidoreductase. The specific substrate identity (Fe-siderophore) is an additional detail, but the reaction-class discrimination is achievable through sequence analysis.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The specific substrate 'Fe(II)-siderophore / Fe(III)-siderophore' cannot be deduced purely from sequence without prior knowledge of siderophore-interacting protein (SIP) function; however, the reaction-type elimination logic is sufficient to select A among the four provided options.",
    "reason": "The four choices span four fundamentally different reaction classes (oxidoreductase, ligase, P450 monooxygenase, decarboxylase). Sequence-level features (FAD-binding glycine-rich motifs, absence of heme/PLP/ATP-binding signatures) allow a knowledgeable biologist to eliminate B, C, and D and select A as the only oxidoreductase. This constitutes a concrete biological argument from the supplied sequence rather than pure memorization of the database entry."
  },
  "case_id": "catalytic_activity_0167",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C7",
      "H2",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry A0A1E3M8P2 (sequence exactly matched, 286 aa, Acinetobacter baumannii) annotates the catalytic activity as '2 a Fe(II)-siderophore + NAD(+) + H(+) = 2 a Fe(III)-siderophore + NADH' (EC 1.16.1.10), with ECO:0000269 (direct assay) evidence from PubMed:34308084 and a 2.85 Å X-ray structure in complex with FAD (PDB 7LRN). Choice A is a verbatim match to this annotated reaction. A second annotated reaction uses NADP(+) instead of NAD(+), but that variant is not among the choices, so no conflict arises."
  },
  "important_caveats": [
    "The UniProt annotation includes a physiologicalDirection of 'right-to-left' for both reactions, meaning the enzyme physiologically reduces Fe(III)-siderophore using NADH. Choice A writes the reaction in the forward (oxidation) direction as listed in Rhea; this is standard UniProt convention and does not constitute an error.",
    "The sequence-match is exact (SHA-256 identical) between the benchmark input and both the current (v37) and archived (v35) UniProt entries, confirming the evidence applies to the supplied protein.",
    "The FAD-binding motifs in this sequence are somewhat degenerate; confident identification as a flavoprotein from sequence alone requires expert-level fold recognition rather than simple motif matching.",
    "The specific substrate 'Fe-siderophore' is an item-specific annotation detail; a model selecting A purely by recognizing this exact sequence's database entry would be relying on memorization rather than reasoning."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The enzyme has two annotated catalytic activities (NAD+ and NADP+ variants), but only the NAD+ variant (Choice A) appears among the options. The other three choices represent entirely different reaction types incompatible with the sequence features. No ambiguity exists among the provided options."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0167",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A0A1E3M8P2 (sequence exactly matched, 286 aa, Acinetobacter baumannii) annotates the catalytic activity as '2 a Fe(II)-siderophore + NAD(+) + H(+) = 2 a Fe(III)-siderophore + NADH' (EC 1.16.1.10), with ECO:0000269 (direct assay) evidence from PubMed:34308084 and a 2.85 Å X-ray structure in complex with FAD (PDB 7LRN). Choice A is a verbatim match to this annotated reaction. A second annotated reaction uses NADP(+) instead of NAD(+), but that variant is not among the choices, so no conflict arises.",
    "evidence_ids": ["C4", "C5", "C7", "H2", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains glycine-rich stretches (e.g., GKINT, GVLIG, GPRPH) consistent with a Rossmann-like FAD-binding fold, indicating a flavoprotein oxidoreductase. Among the four choices, only A is an oxidoreductase reaction involving NAD+/NADH. Choice B is an amide-bond-forming ligase (requires ATP-binding/PPi-release motifs absent here). Choice C is a cytochrome P450 monooxygenase reaction (requires a heme-binding CxxGxxG/FGAGERVCPEG motif, absent). Choice D is a PLP-dependent or cofactor-independent decarboxylase (PPCDC-type, no PLP-binding motif present). Eliminating B, C, and D by absence of their characteristic structural motifs leaves A as the only reaction type compatible with a flavoprotein oxidoreductase. The specific substrate identity (Fe-siderophore) is an additional detail, but the reaction-class discrimination is achievable through sequence analysis.",
    "missing_item_specific_fact": "The specific substrate 'Fe(II)-siderophore / Fe(III)-siderophore' cannot be deduced purely from sequence without prior knowledge of siderophore-interacting protein (SIP) function; however, the reaction-type elimination logic is sufficient to select A among the four provided options.",
    "reason": "The four choices span four fundamentally different reaction classes (oxidoreductase, ligase, P450 monooxygenase, decarboxylase). Sequence-level features (FAD-binding glycine-rich motifs, absence of heme/PLP/ATP-binding signatures) allow a knowledgeable biologist to eliminate B, C, and D and select A as the only oxidoreductase. This constitutes a concrete biological argument from the supplied sequence rather than pure memorization of the database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The enzyme has two annotated catalytic activities (NAD+ and NADP+ variants), but only the NAD+ variant (Choice A) appears among the options. The other three choices represent entirely different reaction types incompatible with the sequence features. No ambiguity exists among the provided options."
  },
  "important_caveats": [
    "The UniProt annotation includes a physiologicalDirection of 'right-to-left' for both reactions, meaning the enzyme physiologically reduces Fe(III)-siderophore using NADH. Choice A writes the reaction in the forward (oxidation) direction as listed in Rhea; this is standard UniProt convention and does not constitute an error.",
    "The sequence-match is exact (SHA-256 identical) between the benchmark input and both the current (v37) and archived (v35) UniProt entries, confirming the evidence applies to the supplied protein.",
    "The FAD-binding motifs in this sequence are somewhat degenerate; confident identification as a flavoprotein from sequence alone requires expert-level fold recognition rather than simple motif matching.",
    "The specific substrate 'Fe-siderophore' is an item-specific annotation detail; a model selecting A purely by recognizing this exact sequence's database entry would be relying on memorization rather than reasoning."
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

**Accession:** `A0A1E3M8P2` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 35. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A1E3M8P2.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:33.445950+00:00.  

```json
"A0A1E3M8P2"
```

Source SHA-256: `27262ada0697001eda3da1d3769c61657664eca5dc8977cc9c5dbaec21268418`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A1E3M8P2.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:33.445950+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"34308084","source":"PubMed"}],"value":"Flavin-dependent siderophore-interacting protein"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"34308084","source":"PubMed"}],"value":"Flavin-dependent SIP"}]}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"34308084","source":"PubMed"}],"value":"1.16.1.10"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Ferric acinetobactin reductase"}}}
```

Source SHA-256: `27262ada0697001eda3da1d3769c61657664eca5dc8977cc9c5dbaec21268418`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A1E3M8P2.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:33.445950+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"right-to-left","evidences":[{"evidenceCode":"ECO:0000269","id":"34308084","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:15063"}}],"reaction":{"ecNumber":"1.16.1.10","evidences":[{"evidenceCode":"ECO:0000269","id":"34308084","source":"PubMed"}],"name":"2 a Fe(II)-siderophore + NAD(+) + H(+) = 2 a Fe(III)-siderophore + NADH","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:15061"},{"database":"Rhea","id":"RHEA-COMP:11342"},{"database":"Rhea","id":"RHEA-COMP:11344"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:29033"},{"database":"ChEBI","id":"CHEBI:29034"},{"database":"ChEBI","id":"CHEBI:57540"},{"database":"ChEBI","id":"CHEBI:57945"}]}}
```

Source SHA-256: `27262ada0697001eda3da1d3769c61657664eca5dc8977cc9c5dbaec21268418`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A1E3M8P2.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:33.445950+00:00.  

```json
{"citation":{"authors":["Valentino H.","Korasick D.A.","Bohac T.J.","Shapiro J.A.","Wencewicz T.A.","Tanner J.J.","Sobrado P."],"citationCrossReferences":[{"database":"PubMed","id":"34308084"},{"database":"DOI","id":"10.1021/acsomega.1c03047"}],"citationType":"journal article","firstPage":"18537","id":"34308084","journal":"ACS Omega","lastPage":"18547","publicationDate":"2021","title":"Structural and Biochemical Characterization of the Flavin-Dependent Siderophore-Interacting Protein from Acinetobacter baumannii.","volume":"6"},"evidences":[{"evidenceCode":"ECO:0007744","id":"7LRN","source":"PDB"}],"referenceComments":[{"type":"STRAIN","value":"ATCC 17978 / DSM 105126 / CIP 53.77 / LMG 1025 / NCDC KC755 / 5377"}],"referenceNumber":2,"referencePositions":["X-RAY CRYSTALLOGRAPHY (2.85 ANGSTROMS) IN COMPLEX WITH FAD","FUNCTION","CATALYTIC ACTIVITY","COFACTOR"]}
```

Source SHA-256: `27262ada0697001eda3da1d3769c61657664eca5dc8977cc9c5dbaec21268418`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A1E3M8P2?format=txt&versions=35)  
**Locator:** `lines 6-9`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 35 / 1.  
**Retrieved:** 2026-11-02T04:24:37.007835+00:00.  

```text
DE   RecName: Full=Ferric acinetobactin reductase {ECO:0000305};
DE            EC=1.16.1.10 {ECO:0000269|PubMed:34308084};
DE   AltName: Full=Flavin-dependent siderophore-interacting protein {ECO:0000303|PubMed:34308084};
DE            Short=Flavin-dependent SIP {ECO:0000303|PubMed:34308084};
```

Source SHA-256: `21245d159df4b708ad492dd55bbbd986a27609a5d66677beffd60475a84e1746`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A1E3M8P2?format=txt&versions=35)  
**Locator:** `lines 43-50`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 35 / 1.  
**Retrieved:** 2026-11-02T04:24:37.007835+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=2 a Fe(II)-siderophore + NAD(+) + H(+) = 2 a Fe(III)-
CC         siderophore + NADH; Xref=Rhea:RHEA:15061, Rhea:RHEA-COMP:11342,
CC         Rhea:RHEA-COMP:11344, ChEBI:CHEBI:15378, ChEBI:CHEBI:29033,
CC         ChEBI:CHEBI:29034, ChEBI:CHEBI:57540, ChEBI:CHEBI:57945;
CC         EC=1.16.1.10; Evidence={ECO:0000269|PubMed:34308084};
CC       PhysiologicalDirection=right-to-left; Xref=Rhea:RHEA:15063;
CC         Evidence={ECO:0000269|PubMed:34308084};
```

Source SHA-256: `21245d159df4b708ad492dd55bbbd986a27609a5d66677beffd60475a84e1746`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A1E3M8P2?format=txt&versions=35)  
**Locator:** `lines 51-58`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 35 / 1.  
**Retrieved:** 2026-11-02T04:24:37.007835+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=2 a Fe(II)-siderophore + NADP(+) + H(+) = 2 a Fe(III)-
CC         siderophore + NADPH; Xref=Rhea:RHEA:28795, Rhea:RHEA-COMP:11342,
CC         Rhea:RHEA-COMP:11344, ChEBI:CHEBI:15378, ChEBI:CHEBI:29033,
CC         ChEBI:CHEBI:29034, ChEBI:CHEBI:57783, ChEBI:CHEBI:58349;
CC         EC=1.16.1.10; Evidence={ECO:0000269|PubMed:34308084};
CC       PhysiologicalDirection=right-to-left; Xref=Rhea:RHEA:28797;
CC         Evidence={ECO:0000269|PubMed:34308084};
```

Source SHA-256: `21245d159df4b708ad492dd55bbbd986a27609a5d66677beffd60475a84e1746`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 167. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
