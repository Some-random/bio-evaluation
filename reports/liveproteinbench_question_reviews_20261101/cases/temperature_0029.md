# temperature_0029

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `temperature`  
**Author expected answer:** **C** — 80

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MHLASSLFLLATLPFGFAAGKGKGKGKDNSDVGLDVLAKKAGLKYFGAATDTPGQRERAGLEDKYPEYDRIMWHSPEFGSTTPTNGQKWLFVEPERGVFNFTEGDVVASKARQHGKLLRCHALVWHSQLAPWVEETEWTPEELRKVIVDHITAVAGHYKGQCYAWDVVNEALNEDGTYRESVFYKVLGEEYIKLAFETAAKVDPKAKLYYNDYNLEWPSAKTEGAKRIVKLLKDAKIPIHGVGLQAHLIAEQHPTLDDHIAAIRGFTQLGVEVALTELDIRLKTPATEENLALQREAYKNVVGACVQVCGCVGVTIWDFYDPFSWVPYFFEGEGAPLLWFEDFSKHPAYYGVVEALTNKTRRSKRSISDRRAKLLA

[Multiple Choices]
A. 25
B. 67
C. 80
D. 62
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Protein Thermal Adaptation Prediction, which is to predict the thermal adaptation category of a protein. This relates to the optimal temperature range in which the protein is stable and functional (e.g., cold-adapted, moderate temperature-adapted, or heat-adapted). This property is encoded by subtle patterns in the amino acid sequence that affect the protein's structural stability, such as amino acid composition and the potential for internal bonds. Based on the provided sequence, you must classify the protein into its most likely thermal category.. The inputs provided by the user for this task include:

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

> The exact sequence matches the UniProt entry for this protein, whose temperature-dependence annotation reports an optimum of 80°C and cites experimental evidence (ECO:0000269) from PubMed 23306124. This supports choice C, though the primary paper was not independently checked here.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3), [C6](#evidence-c6).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence and choices do not provide a defensible way to distinguish an exact optimum of 80°C from 67°C or 62°C. General clues suggesting a secreted fungal enzyme or possible thermal adaptation cannot establish its measured optimum.


**Missing item-specific fact**

> The protein-specific experimental temperature optimum reported for this xylanase is needed to select 80°C over the other numerical choices.


**Reason**

> The answer is supported by a protein-specific annotation tied to a cited experiment, but that annotation and measurement are absent from the model input. Inferring a broad thermal tendency is not enough to justify the precise value.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "C",
  "D"
]
```

> Without the protein-specific measurement, the supplied sequence does not distinguish among the elevated candidate temperatures 62°C, 67°C, and 80°C. The evidence supports C as the experimentally annotated value, but that fact is not derivable with confidence from the prompt alone.


### Important caveats

- The experimental evidence is represented by a UniProt annotation citing PubMed 23306124; the primary paper was not independently validated.
- The reviewer-only accession and source information were not supplied to the evaluated model. The current and archived records match the input sequence, but the author's exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence and choices do not provide a defensible way to distinguish an exact optimum of 80°C from 67°C or 62°C. General clues suggesting a secreted fungal enzyme or possible thermal adaptation cannot establish its measured optimum.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific experimental temperature optimum reported for this xylanase is needed to select 80°C over the other numerical choices.",
    "reason": "The answer is supported by a protein-specific annotation tied to a cited experiment, but that annotation and measurement are absent from the model input. Inferring a broad thermal tendency is not enough to justify the precise value."
  },
  "case_id": "temperature_0029",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3",
      "C6"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry for this protein, whose temperature-dependence annotation reports an optimum of 80°C and cites experimental evidence (ECO:0000269) from PubMed 23306124. This supports choice C, though the primary paper was not independently checked here."
  },
  "important_caveats": [
    "The experimental evidence is represented by a UniProt annotation citing PubMed 23306124; the primary paper was not independently validated.",
    "The reviewer-only accession and source information were not supplied to the evaluated model. The current and archived records match the input sequence, but the author's exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "C",
      "D"
    ],
    "reason": "Without the protein-specific measurement, the supplied sequence does not distinguish among the elevated candidate temperatures 62°C, 67°C, and 80°C. The evidence supports C as the experimentally annotated value, but that fact is not derivable with confidence from the prompt alone."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "temperature_0029",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry for this protein, whose temperature-dependence annotation reports an optimum of 80°C and cites experimental evidence (ECO:0000269) from PubMed 23306124. This supports choice C, though the primary paper was not independently checked here.",
    "evidence_ids": ["C5", "H3", "C6"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence and choices do not provide a defensible way to distinguish an exact optimum of 80°C from 67°C or 62°C. General clues suggesting a secreted fungal enzyme or possible thermal adaptation cannot establish its measured optimum.",
    "missing_item_specific_fact": "The protein-specific experimental temperature optimum reported for this xylanase is needed to select 80°C over the other numerical choices.",
    "reason": "The answer is supported by a protein-specific annotation tied to a cited experiment, but that annotation and measurement are absent from the model input. Inferring a broad thermal tendency is not enough to justify the precise value."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "C", "D"],
    "reason": "Without the protein-specific measurement, the supplied sequence does not distinguish among the elevated candidate temperatures 62°C, 67°C, and 80°C. The evidence supports C as the experimentally annotated value, but that fact is not derivable with confidence from the prompt alone."
  },
  "important_caveats": [
    "The experimental evidence is represented by a UniProt annotation citing PubMed 23306124; the primary paper was not independently validated.",
    "The reviewer-only accession and source information were not supplied to the evaluated model. The current and archived records match the input sequence, but the author's exact source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence exactly matches UniProt entry M4MGK7 (XYNA_HUMIN), Endo-1,4-beta-xylanase A from Humicola insolens (genus Mycothermus). The UniProt annotation states 'Optimum temperature is 80 degrees Celsius' with evidence code ECO:0000269 (inferred from direct assay) from PubMed:23306124 (Du et al., 2013, Bioresour. Technol. 130:161-167), which experimentally characterized three thermophilic xylanases from this strain. The expected answer of 80°C is directly supported by experimental measurement.

Citations as saved: [C1](#evidence-c1), [C3](#evidence-c3), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> One could argue that the sequence contains a signal peptide and GH10 xylanase fold features, and that elevated proportions of charged residues (K, R, D, E) and potential salt-bridge-forming pairs might hint at thermophilic adaptation, allowing elimination of 25°C (option A). However, this broad thermophilic signature cannot meaningfully distinguish 80°C from 67°C or 62°C, as all three fall within the thermophilic range and the subtle compositional differences that correlate with those specific temperatures are not reliably extractable from sequence alone.


**Missing item-specific fact**

> The specific experimentally determined optimum temperature of this particular xylanase (80°C) from Humicola insolens Y1, as reported in Du et al. 2013. Without knowing this protein's identity or its characterized thermal profile, the choices 62, 67, and 80 are indistinguishable by general sequence reasoning.


**Reason**

> While general thermophilic sequence signatures might eliminate 25°C, the remaining options (62, 67, 80) are all within the thermophilic range for fungal enzymes. Distinguishing 80 from 67 or 62 requires knowledge of this specific protein's experimental characterization, not general biological reasoning from sequence composition.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "C",
  "D"
]
```

> Options B (67°C), C (80°C), and D (62°C) are all plausible optimal temperatures for thermophilic fungal xylanases. Without identifying the specific protein and recalling its experimental characterization, a model cannot reliably distinguish among these three thermophilic values. The sequence provides no clear quantitative discriminator between 62, 67, and 80 degrees.


### Important caveats

- The UniProt annotation is based on a single experimental study (PubMed:23306124) using a specific strain (Y1) and substrate (birchwood xylan); the optimum temperature may vary with conditions.
- The organism genus 'Mycothermus' (meaning 'thermophilic fungus') and the paper title explicitly describe these as 'thermophilic xylanases,' providing strong biological context for the 80°C value, but this context is absent from the model's input.
- The benchmark sequence matches the UniProt canonical sequence exactly (SHA-256 verified), confirming the annotation applies to the supplied sequence.
- The entry was first publicly released in 2025, so the 80°C annotation may not have been available at the time the benchmark was constructed depending on the author's data source.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "One could argue that the sequence contains a signal peptide and GH10 xylanase fold features, and that elevated proportions of charged residues (K, R, D, E) and potential salt-bridge-forming pairs might hint at thermophilic adaptation, allowing elimination of 25°C (option A). However, this broad thermophilic signature cannot meaningfully distinguish 80°C from 67°C or 62°C, as all three fall within the thermophilic range and the subtle compositional differences that correlate with those specific temperatures are not reliably extractable from sequence alone.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific experimentally determined optimum temperature of this particular xylanase (80°C) from Humicola insolens Y1, as reported in Du et al. 2013. Without knowing this protein's identity or its characterized thermal profile, the choices 62, 67, and 80 are indistinguishable by general sequence reasoning.",
    "reason": "While general thermophilic sequence signatures might eliminate 25°C, the remaining options (62, 67, 80) are all within the thermophilic range for fungal enzymes. Distinguishing 80 from 67 or 62 requires knowledge of this specific protein's experimental characterization, not general biological reasoning from sequence composition."
  },
  "case_id": "temperature_0029",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C3",
      "C4",
      "C5",
      "C6",
      "H1",
      "H2",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The sequence exactly matches UniProt entry M4MGK7 (XYNA_HUMIN), Endo-1,4-beta-xylanase A from Humicola insolens (genus Mycothermus). The UniProt annotation states 'Optimum temperature is 80 degrees Celsius' with evidence code ECO:0000269 (inferred from direct assay) from PubMed:23306124 (Du et al., 2013, Bioresour. Technol. 130:161-167), which experimentally characterized three thermophilic xylanases from this strain. The expected answer of 80°C is directly supported by experimental measurement."
  },
  "important_caveats": [
    "The UniProt annotation is based on a single experimental study (PubMed:23306124) using a specific strain (Y1) and substrate (birchwood xylan); the optimum temperature may vary with conditions.",
    "The organism genus 'Mycothermus' (meaning 'thermophilic fungus') and the paper title explicitly describe these as 'thermophilic xylanases,' providing strong biological context for the 80°C value, but this context is absent from the model's input.",
    "The benchmark sequence matches the UniProt canonical sequence exactly (SHA-256 verified), confirming the annotation applies to the supplied sequence.",
    "The entry was first publicly released in 2025, so the 80°C annotation may not have been available at the time the benchmark was constructed depending on the author's data source."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "C",
      "D"
    ],
    "reason": "Options B (67°C), C (80°C), and D (62°C) are all plausible optimal temperatures for thermophilic fungal xylanases. Without identifying the specific protein and recalling its experimental characterization, a model cannot reliably distinguish among these three thermophilic values. The sequence provides no clear quantitative discriminator between 62, 67, and 80 degrees."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "temperature_0029",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence exactly matches UniProt entry M4MGK7 (XYNA_HUMIN), Endo-1,4-beta-xylanase A from Humicola insolens (genus Mycothermus). The UniProt annotation states 'Optimum temperature is 80 degrees Celsius' with evidence code ECO:0000269 (inferred from direct assay) from PubMed:23306124 (Du et al., 2013, Bioresour. Technol. 130:161-167), which experimentally characterized three thermophilic xylanases from this strain. The expected answer of 80°C is directly supported by experimental measurement.",
    "evidence_ids": ["C1", "C3", "C4", "C5", "C6", "H1", "H2", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "One could argue that the sequence contains a signal peptide and GH10 xylanase fold features, and that elevated proportions of charged residues (K, R, D, E) and potential salt-bridge-forming pairs might hint at thermophilic adaptation, allowing elimination of 25°C (option A). However, this broad thermophilic signature cannot meaningfully distinguish 80°C from 67°C or 62°C, as all three fall within the thermophilic range and the subtle compositional differences that correlate with those specific temperatures are not reliably extractable from sequence alone.",
    "missing_item_specific_fact": "The specific experimentally determined optimum temperature of this particular xylanase (80°C) from Humicola insolens Y1, as reported in Du et al. 2013. Without knowing this protein's identity or its characterized thermal profile, the choices 62, 67, and 80 are indistinguishable by general sequence reasoning.",
    "reason": "While general thermophilic sequence signatures might eliminate 25°C, the remaining options (62, 67, 80) are all within the thermophilic range for fungal enzymes. Distinguishing 80 from 67 or 62 requires knowledge of this specific protein's experimental characterization, not general biological reasoning from sequence composition."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "C", "D"],
    "reason": "Options B (67°C), C (80°C), and D (62°C) are all plausible optimal temperatures for thermophilic fungal xylanases. Without identifying the specific protein and recalling its experimental characterization, a model cannot reliably distinguish among these three thermophilic values. The sequence provides no clear quantitative discriminator between 62, 67, and 80 degrees."
  },
  "important_caveats": [
    "The UniProt annotation is based on a single experimental study (PubMed:23306124) using a specific strain (Y1) and substrate (birchwood xylan); the optimum temperature may vary with conditions.",
    "The organism genus 'Mycothermus' (meaning 'thermophilic fungus') and the paper title explicitly describe these as 'thermophilic xylanases,' providing strong biological context for the 80°C value, but this context is absent from the model's input.",
    "The benchmark sequence matches the UniProt canonical sequence exactly (SHA-256 verified), confirming the annotation applies to the supplied sequence.",
    "The entry was first publicly released in 2025, so the 80°C annotation may not have been available at the time the benchmark was constructed depending on the author's data source."
  ]
}
```

</details>

## Existing project source checks of Luna’s review

The notes below were prepared for specific claims in the Luna review. They are not independent validation of Qwen’s claims, expert adjudication, or replacement verdicts.

## Project source-check notes

These project-authored, AI-assisted checks assess specific source claims. They are not expert adjudication and do not replace Luna’s saved review or the author key.

### Source check 1

**Check:** `lookup_uncertainty_does_not_establish_multiple_actual_values`.

> The cited sequence-matched annotation reports optimum 80 degrees Celsius. The model ambiguity reason instead invokes inability to infer the measurement from sequence. That establishes a missing item-specific fact, not source evidence that the other listed numerical values are also actual optima.

**Remaining uncertainty:** The ambiguity field needs interpretation separately from lookup dependence. Preserve the model output; do not infer an alternative benchmark score from this note.

## Reviewer-only source evidence

**Both reviewers received this source evidence separately from the original question. It was not available to the original evaluated model.** Source support and reasoning from the original sequence/choices are distinct assessments.

**Accession:** `M4MGK7` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 31. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/M4MGK7.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:05.622631+00:00.  

```json
"M4MGK7"
```

Source SHA-256: `d0eb386047796a4c6d2cf2618df1e68195ff8e1f1d846dddec1115d408f18e15`.

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/M4MGK7.json)  
**Locator:** `/organism`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:05.622631+00:00.  

```json
{"commonName":"Soft-rot fungus","lineage":["Eukaryota","Fungi","Dikarya","Ascomycota","Pezizomycotina","Sordariomycetes","Sordariomycetidae","Sordariales","Chaetomiaceae","Mycothermus"],"scientificName":"Humicola insolens","taxonId":85995}
```

Source SHA-256: `d0eb386047796a4c6d2cf2618df1e68195ff8e1f1d846dddec1115d408f18e15`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/M4MGK7.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:05.622631+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"1,4-beta-D-xylan xylanohydrolase A"}}],"flag":"Precursor","recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"23306124","source":"PubMed"}],"value":"3.2.1.8"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"23306124","source":"PubMed"}],"value":"Endo-1,4-beta-xylanase A"}}}
```

Source SHA-256: `d0eb386047796a4c6d2cf2618df1e68195ff8e1f1d846dddec1115d408f18e15`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/M4MGK7.json)  
**Locator:** `/comments/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:05.622631+00:00.  

```json
{"commentType":"BIOPHYSICOCHEMICAL PROPERTIES","kineticParameters":{"maximumVelocities":[{"enzyme":"enzyme towards birchwood xylan","evidences":[{"evidenceCode":"ECO:0000269","id":"23306124","source":"PubMed"}],"unit":"umol/min/mg","velocity":974.4}],"michaelisConstants":[{"constant":1.6,"evidences":[{"evidenceCode":"ECO:0000269","id":"23306124","source":"PubMed"}],"substrate":"birchwood xylan","unit":"mM"}]},"phDependence":{"texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"23306124","source":"PubMed"}],"value":"Optimum pH is 6.0."}]},"temperatureDependence":{"texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"23306124","source":"PubMed"}],"value":"Optimum temperature is 80 degrees Celsius."}]}}
```

Source SHA-256: `d0eb386047796a4c6d2cf2618df1e68195ff8e1f1d846dddec1115d408f18e15`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/M4MGK7.json)  
**Locator:** `/references/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:05.622631+00:00.  

```json
{"citation":{"authors":["Du Y.","Shi P.","Huang H.","Zhang X.","Luo H.","Wang Y.","Yao B."],"citationCrossReferences":[{"database":"PubMed","id":"23306124"},{"database":"DOI","id":"10.1016/j.biortech.2012.12.067"}],"citationType":"journal article","firstPage":"161","id":"23306124","journal":"Bioresour. Technol.","lastPage":"167","publicationDate":"2013","title":"Characterization of three novel thermophilic xylanases from Humicola insolens Y1 with application potentials in the brewing industry.","volume":"130"},"referenceComments":[{"type":"STRAIN","value":"Y1"}],"referenceNumber":1,"referencePositions":["NUCLEOTIDE SEQUENCE [MRNA]","FUNCTION","CATALYTIC ACTIVITY","BIOPHYSICOCHEMICAL PROPERTIES","SUBSTRATE SPECIFICITY","ACTIVITY REGULATION","BIOTECHNOLOGY"]}
```

Source SHA-256: `d0eb386047796a4c6d2cf2618df1e68195ff8e1f1d846dddec1115d408f18e15`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/M4MGK7?format=txt&versions=31)  
**Locator:** `lines 1-14`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 31 / 1.  
**Retrieved:** 2026-11-02T04:29:07.720781+00:00.  

```text
ID   XYNA_HUMIN              Reviewed;         376 AA.
AC   M4MGK7;
DT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.
DT   29-MAY-2013, sequence version 1.
DT   28-JAN-2026, entry version 31.
DE   RecName: Full=Endo-1,4-beta-xylanase A {ECO:0000303|PubMed:23306124};
DE            EC=3.2.1.8 {ECO:0000269|PubMed:23306124};
DE   AltName: Full=1,4-beta-D-xylan xylanohydrolase A {ECO:0000305};
DE   Flags: Precursor;
GN   Name=XynA {ECO:0000303|PubMed:23306124};
OS   Humicola insolens (Soft-rot fungus).
OC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Sordariomycetes;
OC   Sordariomycetidae; Sordariales; Chaetomiaceae; Mycothermus.
OX   NCBI_TaxID=85995;
```

Source SHA-256: `7ec5a9552d4e5401ddcbb6f19ae0b5460a5e468847c5025d55b7f1a6cab2cd96`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/M4MGK7?format=txt&versions=31)  
**Locator:** `lines 15-24`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 31 / 1.  
**Retrieved:** 2026-11-02T04:29:07.720781+00:00.  

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

Source SHA-256: `7ec5a9552d4e5401ddcbb6f19ae0b5460a5e468847c5025d55b7f1a6cab2cd96`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/M4MGK7?format=txt&versions=31)  
**Locator:** `lines 55-64`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 31 / 1.  
**Retrieved:** 2026-11-02T04:29:07.720781+00:00.  

```text
CC   -!- BIOPHYSICOCHEMICAL PROPERTIES:
CC       Kinetic parameters:
CC         KM=1.6 mM for birchwood xylan {ECO:0000269|PubMed:23306124};
CC         Vmax=974.4 umol/min/mg enzyme towards birchwood xylan
CC         {ECO:0000269|PubMed:23306124};
CC       pH dependence:
CC         Optimum pH is 6.0. {ECO:0000269|PubMed:23306124};
CC       Temperature dependence:
CC         Optimum temperature is 80 degrees Celsius.
CC         {ECO:0000269|PubMed:23306124};
```

Source SHA-256: `7ec5a9552d4e5401ddcbb6f19ae0b5460a5e468847c5025d55b7f1a6cab2cd96`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/temperature.json), zero-based source row 29. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
