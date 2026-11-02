# temperature_0027

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `temperature`  
**Author expected answer:** **D** — 55

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | invalid_review |

**Paired comparison:** not comparable: one or both reviews invalid or missing. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MKPHNSEKYFVKNGQPHFLISGEVHYFRINPKLWRNHLQLLKQTGADTVSTYIPWDWHEIEEDDFDFEGKTHPARNLIRFIKLCKEENLDLIVKPGPYILAEYENQGLPSWLLKKLSKNAFALDENGNVISPDLVSYLSDEFLEYTFKWYDKVMPIISKHQKEHYGPITMMQLCNEIGVFQWLSGKSDYNPKVINLYKEFIIQRYKTIEKLNSVYSTNYNSFDDLKAPSGKIKLRSDYCAYFDFHLFFREYYNKYISILKNKIRSFGINIKLTHNIPGWIYGNASELPMLISTYSEIMKNHPDIIFGLDHIPEFVSFRNAHSDLACNKILEAMQPEAPVWAAEFQAGTREHHVKAYAKDLETFYIASLAHGIKGFNYYMFSQGINPEGKGFYGKTFYFQTALDAASNKLALYDSIKKVNRFIRKEQKDLLRTNVNSEICVGFYKPYFFTELISSQLLKEKKLNVEELGLYIDPRFLREEILFNGLLRGLQTLNYNYDVVDLENCDLKSLTAYKQLWITSAEFMDAETQNLLSEFVLNGGNLILYPAVPTLDNYLNRCEILKNNFGIEFITKDSSHKVSAFGIEDVFTAFSKKQIYNDTNSKPIAFTQENEICGIRKKIGKGELTILGFAFGYTSDEHLELIDKLVKLNKIKRELFVSDKDIQFVVRENNKSRYIFFLNYHNERKTFNYRKSSELKKKKSEEISIAPFSYKVIKENK

[Multiple Choices]
A. 79
B. 76
C. 32
D. 55
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

> The exact supplied sequence matches the referenced protein, whose UniProt annotation reports an experimentally supported optimum temperature of 55 °C.

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence alone offers no defensible way to select 55 rather than the other specific temperature values; broad sequence-based thermal tendencies would not establish an exact optimum.


**Missing item-specific fact**

> The protein-specific experimentally measured optimum temperature, reported as 55 °C.


**Reason**

> The key is supported by a protein-specific temperature measurement, but that measurement is absent from the sequence and choices.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The choices are specific temperatures rather than thermal-adaptation categories, but the reported optimum supports 55 °C.


### Important caveats

- The reviewer-only evidence reports the measurement with experimental evidence attribution to PubMed 35065074; the primary paper was not independently reviewed here.
- An optimum temperature is not identical to a general thermal-adaptation category or a complete measure of protein stability.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence alone offers no defensible way to select 55 rather than the other specific temperature values; broad sequence-based thermal tendencies would not establish an exact optimum.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific experimentally measured optimum temperature, reported as 55 °C.",
    "reason": "The key is supported by a protein-specific temperature measurement, but that measurement is absent from the sequence and choices."
  },
  "case_id": "temperature_0027",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The exact supplied sequence matches the referenced protein, whose UniProt annotation reports an experimentally supported optimum temperature of 55 °C."
  },
  "important_caveats": [
    "The reviewer-only evidence reports the measurement with experimental evidence attribution to PubMed 35065074; the primary paper was not independently reviewed here.",
    "An optimum temperature is not identical to a general thermal-adaptation category or a complete measure of protein stability."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The choices are specific temperatures rather than thermal-adaptation categories, but the reported optimum supports 55 °C."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "temperature_0027",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact supplied sequence matches the referenced protein, whose UniProt annotation reports an experimentally supported optimum temperature of 55 °C.",
    "evidence_ids": ["C1", "C5", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence alone offers no defensible way to select 55 rather than the other specific temperature values; broad sequence-based thermal tendencies would not establish an exact optimum.",
    "missing_item_specific_fact": "The protein-specific experimentally measured optimum temperature, reported as 55 °C.",
    "reason": "The key is supported by a protein-specific temperature measurement, but that measurement is absent from the sequence and choices."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The choices are specific temperatures rather than thermal-adaptation categories, but the reported optimum supports 55 °C."
  },
  "important_caveats": [
    "The reviewer-only evidence reports the measurement with experimental evidence attribution to PubMed 35065074; the primary paper was not independently reviewed here.",
    "An optimum temperature is not identical to a general thermal-adaptation category or a complete measure of protein stability."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `invalid_review`.

**This result is not a valid structured review.** Any saved labels below remain the model’s original values; they are excluded from label distributions and paired agreement. No field or option ID has been repaired.

**Validation errors:** `question_ambiguity:invalid_option_ids`.

### Expected-answer support: supported

> The UniProt entry I0AIT9 (Beta-1,2-glucosyltransferase, IaSGT from Ignavibacterium album DSM 19864) explicitly states 'Optimum temperature is 55 degrees Celsius' with experimental evidence (ECO:0000269, PubMed:35065074, Kobayashi et al. 2022, J. Biol. Chem.). The benchmark sequence matches the canonical entry exactly (716 AA, SHA256 match). The author's key of 55°C is directly supported by experimental measurement.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3), [C6](#evidence-c6), [H2](#evidence-h2).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> One could argue that Ignavibacterium album belongs to Ignavibacteriaceae, a lineage of moderately thermophilic bacteria, which would favor 55°C over the hyperthermophilic options (76°C, 79°C) and the mesophilic option (32°C). However, recognizing the organism from a raw 716-aa sequence and recalling its optimal growth temperature is organism-specific memorization, not general reasoning. Distinguishing 55°C from 76°C based on amino acid composition, salt-bridge potential, or proline content alone is not reliably achievable through general biological knowledge; the structural differences between moderate (55°C) and hyperthermophilic (76°C) proteins are too subtle for unaided sequence inspection.


**Missing item-specific fact**

> The experimentally measured optimum temperature of 55°C for this specific Beta-1,2-glucosyltransferase (PubMed:35065074), or equivalently, the known optimal growth temperature of Ignavibacterium album (~55°C), which is not derivable from the sequence alone.


**Reason**

> The question asks for a precise experimental temperature value (55 vs 76 vs 79 vs 32°C). While 32°C (mesophilic) and 79°C (extreme hyperthermophilic) can be argued against as distractors using broad biological reasoning, the critical distinction between 55°C and 76°C for this particular enzyme requires either knowledge of the source organism's growth conditions or the specific experimental measurement. General sequence-composition heuristics (charged residues, proline content, hydrophobic packing) cannot reliably separate a moderate thermophilic optimum from a hyperthermophilic one without a trained predictor or organism-specific context.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "D (55)",
  "B (76)"
]
```

> Both 55°C and 76°C represent thermophilic adaptation and could be argued from a sequence showing elevated charged-residue content and structural rigidity features. Without organism-specific knowledge or a trained predictor, a careful analyst might reasonably select 76°C as a thermophilic optimum. 32°C and 79°C are more clearly distinguishable as mesophilic and extreme-hyperthermophilic outliers, respectively.


### Important caveats

- The UniProt annotation is based on experimental characterization (ECO:0000269) from Kobayashi et al. 2022, not computational inference, lending strong support to the 55°C key.
- The protein is a glycosyltransferase (EC 2.4.1.391), not a typical thermostability benchmark enzyme; its thermal optimum reflects the organism's moderate thermophily rather than extreme adaptation.
- The system prompt frames the task as predicting from 'subtle patterns in the amino acid sequence,' but the actual distinguishing fact (55 vs 76°C) is not encoded in any sequence pattern accessible by general reasoning.
- The reviewer-only evidence confirms the accession and experimental value but was not available to the evaluated model; the model would need to either recognize the organism or rely on a trained predictor.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "One could argue that Ignavibacterium album belongs to Ignavibacteriaceae, a lineage of moderately thermophilic bacteria, which would favor 55°C over the hyperthermophilic options (76°C, 79°C) and the mesophilic option (32°C). However, recognizing the organism from a raw 716-aa sequence and recalling its optimal growth temperature is organism-specific memorization, not general reasoning. Distinguishing 55°C from 76°C based on amino acid composition, salt-bridge potential, or proline content alone is not reliably achievable through general biological knowledge; the structural differences between moderate (55°C) and hyperthermophilic (76°C) proteins are too subtle for unaided sequence inspection.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The experimentally measured optimum temperature of 55°C for this specific Beta-1,2-glucosyltransferase (PubMed:35065074), or equivalently, the known optimal growth temperature of Ignavibacterium album (~55°C), which is not derivable from the sequence alone.",
    "reason": "The question asks for a precise experimental temperature value (55 vs 76 vs 79 vs 32°C). While 32°C (mesophilic) and 79°C (extreme hyperthermophilic) can be argued against as distractors using broad biological reasoning, the critical distinction between 55°C and 76°C for this particular enzyme requires either knowledge of the source organism's growth conditions or the specific experimental measurement. General sequence-composition heuristics (charged residues, proline content, hydrophobic packing) cannot reliably separate a moderate thermophilic optimum from a hyperthermophilic one without a trained predictor or organism-specific context."
  },
  "case_id": "temperature_0027",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3",
      "C6",
      "H2"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry I0AIT9 (Beta-1,2-glucosyltransferase, IaSGT from Ignavibacterium album DSM 19864) explicitly states 'Optimum temperature is 55 degrees Celsius' with experimental evidence (ECO:0000269, PubMed:35065074, Kobayashi et al. 2022, J. Biol. Chem.). The benchmark sequence matches the canonical entry exactly (716 AA, SHA256 match). The author's key of 55°C is directly supported by experimental measurement."
  },
  "important_caveats": [
    "The UniProt annotation is based on experimental characterization (ECO:0000269) from Kobayashi et al. 2022, not computational inference, lending strong support to the 55°C key.",
    "The protein is a glycosyltransferase (EC 2.4.1.391), not a typical thermostability benchmark enzyme; its thermal optimum reflects the organism's moderate thermophily rather than extreme adaptation.",
    "The system prompt frames the task as predicting from 'subtle patterns in the amino acid sequence,' but the actual distinguishing fact (55 vs 76°C) is not encoded in any sequence pattern accessible by general reasoning.",
    "The reviewer-only evidence confirms the accession and experimental value but was not available to the evaluated model; the model would need to either recognize the organism or rely on a trained predictor."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "D (55)",
      "B (76)"
    ],
    "reason": "Both 55°C and 76°C represent thermophilic adaptation and could be argued from a sequence showing elevated charged-residue content and structural rigidity features. Without organism-specific knowledge or a trained predictor, a careful analyst might reasonably select 76°C as a thermophilic optimum. 32°C and 79°C are more clearly distinguishable as mesophilic and extreme-hyperthermophilic outliers, respectively."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "temperature_0027",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry I0AIT9 (Beta-1,2-glucosyltransferase, IaSGT from Ignavibacterium album DSM 19864) explicitly states 'Optimum temperature is 55 degrees Celsius' with experimental evidence (ECO:0000269, PubMed:35065074, Kobayashi et al. 2022, J. Biol. Chem.). The benchmark sequence matches the canonical entry exactly (716 AA, SHA256 match). The author's key of 55°C is directly supported by experimental measurement.",
    "evidence_ids": ["C5", "H3", "C6", "H2"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "One could argue that Ignavibacterium album belongs to Ignavibacteriaceae, a lineage of moderately thermophilic bacteria, which would favor 55°C over the hyperthermophilic options (76°C, 79°C) and the mesophilic option (32°C). However, recognizing the organism from a raw 716-aa sequence and recalling its optimal growth temperature is organism-specific memorization, not general reasoning. Distinguishing 55°C from 76°C based on amino acid composition, salt-bridge potential, or proline content alone is not reliably achievable through general biological knowledge; the structural differences between moderate (55°C) and hyperthermophilic (76°C) proteins are too subtle for unaided sequence inspection.",
    "missing_item_specific_fact": "The experimentally measured optimum temperature of 55°C for this specific Beta-1,2-glucosyltransferase (PubMed:35065074), or equivalently, the known optimal growth temperature of Ignavibacterium album (~55°C), which is not derivable from the sequence alone.",
    "reason": "The question asks for a precise experimental temperature value (55 vs 76 vs 79 vs 32°C). While 32°C (mesophilic) and 79°C (extreme hyperthermophilic) can be argued against as distractors using broad biological reasoning, the critical distinction between 55°C and 76°C for this particular enzyme requires either knowledge of the source organism's growth conditions or the specific experimental measurement. General sequence-composition heuristics (charged residues, proline content, hydrophobic packing) cannot reliably separate a moderate thermophilic optimum from a hyperthermophilic one without a trained predictor or organism-specific context."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["D (55)", "B (76)"],
    "reason": "Both 55°C and 76°C represent thermophilic adaptation and could be argued from a sequence showing elevated charged-residue content and structural rigidity features. Without organism-specific knowledge or a trained predictor, a careful analyst might reasonably select 76°C as a thermophilic optimum. 32°C and 79°C are more clearly distinguishable as mesophilic and extreme-hyperthermophilic outliers, respectively."
  },
  "important_caveats": [
    "The UniProt annotation is based on experimental characterization (ECO:0000269) from Kobayashi et al. 2022, not computational inference, lending strong support to the 55°C key.",
    "The protein is a glycosyltransferase (EC 2.4.1.391), not a typical thermostability benchmark enzyme; its thermal optimum reflects the organism's moderate thermophily rather than extreme adaptation.",
    "The system prompt frames the task as predicting from 'subtle patterns in the amino acid sequence,' but the actual distinguishing fact (55 vs 76°C) is not encoded in any sequence pattern accessible by general reasoning.",
    "The reviewer-only evidence confirms the accession and experimental value but was not available to the evaluated model; the model would need to either recognize the organism or rely on a trained predictor."
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

**Accession:** `I0AIT9` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 55. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/I0AIT9.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:10.515356+00:00.  

```json
"I0AIT9"
```

Source SHA-256: `0141e863e485261dd884ecaf6bc9c67a2a0434afac2c92f95f4ffba2990aa032`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/I0AIT9.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:10.515356+00:00.  

```json
{"commentType":"BIOPHYSICOCHEMICAL PROPERTIES","kineticParameters":{"michaelisConstants":[{"constant":9.6,"evidences":[{"evidenceCode":"ECO:0000269","id":"35065074","source":"PubMed"}],"substrate":"sophorose (with pNP-alpha-glucose as an acceptor)","unit":"mM"},{"constant":22.0,"evidences":[{"evidenceCode":"ECO:0000269","id":"35065074","source":"PubMed"}],"substrate":"beta-(1->2)-glucotriose (with pNP-alpha-glucose as an acceptor)","unit":"mM"},{"constant":0.2,"evidences":[{"evidenceCode":"ECO:0000269","id":"35065074","source":"PubMed"}],"substrate":"methyl-alpha-glucose","unit":"mM"},{"constant":0.044,"evidences":[{"evidenceCode":"ECO:0000269","id":"35065074","source":"PubMed"}],"substrate":"ethyl-alpha-glucose","unit":"mM"},{"constant":0.22,"evidences":[{"evidenceCode":"ECO:0000269","id":"35065074","source":"PubMed"}],"substrate":"phenyl-alpha-glucose","unit":"mM"},{"constant":0.38,"evidences":[{"evidenceCode":"ECO:0000269","id":"35065074","source":"PubMed"}],"substrate":"alpha-arbutin","unit":"mM"},{"constant":0.13,"evidences":[{"evidenceCode":"ECO:0000269","id":"35065074","source":"PubMed"}],"substrate":"pNP-alpha-glucose","unit":"mM"},{"constant":0.096,"evidences":[{"evidenceCode":"ECO:0000269","id":"35065074","source":"PubMed"}],"substrate":"benzyl-alpha-glucose","unit":"mM"},{"constant":0.15,"evidences":[{"evidenceCode":"ECO:0000269","id":"35065074","source":"PubMed"}],"substrate":"2-naphthyl-alpha-glucose","unit":"mM"},{"constant":0.13,"evidences":[{"evidenceCode":"ECO:0000269","id":"35065074","source":"PubMed"}],"substrate":"methyl-beta-glucose","unit":"mM"},{"constant":0.026,"evidences":[{"evidenceCode":"ECO:0000269","id":"35065074","source":"PubMed"}],"substrate":"beta-arbutin","unit":"mM"},{"constant":0.04,"evidences":[{"evidenceCode":"ECO:0000269","id":"35065074","source":"PubMed"}],"substrate":"pNP-beta-glucose","unit":"mM"},{"constant":0.042,"evidences":[{"evidenceCode":"ECO:0000269","id":"35065074","source":"PubMed"}],"substrate":"gastrodin","unit":"mM"},{"constant":0.021,"evidences":[{"evidenceCode":"ECO:0000269","id":"35065074","source":"PubMed"}],"substrate":"salicin","unit":"mM"},{"constant":0.045,"evidences":[{"evidenceCode":"ECO:0000269","id":"35065074","source":"PubMed"}],"substrate":"esculin","unit":"mM"},{"constant":0.15,"evidences":[{"evidenceCode":"ECO:0000269","id":"35065074","source":"PubMed"}],"substrate":"amygdalin","unit":"mM"}],"note":{"texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"35065074","source":"PubMed"}],"value":"kcat is 70 sec(-1) with sophorose as substrate. kcat is 12 sec(-1) with beta-(1->2)-glucotriose as substrate. kcat is 1.0 sec(-1) with methyl-alpha-glucose as substrate. kcat is 0.55 sec(-1) with ethyl-alpha-glucose as substrate. kcat is 1.8 sec(-1) with phenyl-alpha-glucose as substrate. kcat is 8.7 sec(-1) with alpha-arbutin as substrate. kcat is 5.0 sec(-1) with pNP-alpha-glucose as substrate. kcat is 0.86 sec(-1) with benzyl-alpha-glucose as substrate. kcat is 3.9 sec(-1) with 2-naphthyl-alpha-glucose as substrate. kcat is 1.9 sec(-1) with methyl-beta-glucose as substrate. kcat is 1.4 sec(-1) with beta-arbutin as substrate. kcat is 0.46 sec(-1) with pNP-beta-glucose as substrate. kcat is 0.49 sec(-1) with gastrodin as substrate. kcat is 0.88 sec(-1) with salicin as substrate. kcat is 1.3 sec(-1) with esculin as substrate. kcat is 0.35 sec(-1) with amygdalin as substrate."}]}},"phDependence":{"texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"35065074","source":"PubMed"}],"value":"Shows high activity at pH 5.0 to 8.0."}]},"temperatureDependence":{"texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"35065074","source":"PubMed"}],"value":"Optimum temperature is 55 degrees Celsius (PubMed:35065074). Stable up to 60 degrees Celsius after incubation for 1 hour (PubMed:35065074)."}]}}
```

Source SHA-256: `0141e863e485261dd884ecaf6bc9c67a2a0434afac2c92f95f4ffba2990aa032`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/I0AIT9.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:10.515356+00:00.  

```json
{"citation":{"authors":["Kobayashi K.","Shimizu H.","Tanaka N.","Kuramochi K.","Nakai H.","Nakajima M.","Taguchi H."],"citationCrossReferences":[{"database":"PubMed","id":"35065074"},{"database":"DOI","id":"10.1016/j.jbc.2022.101606"}],"citationType":"journal article","firstPage":"101606","id":"35065074","journal":"J. Biol. Chem.","lastPage":"101606","publicationDate":"2022","title":"Characterization and structural analyses of a novel glycosyltransferase acting on the beta-1,2-glucosidic linkages.","volume":"298"},"evidences":[{"evidenceCode":"ECO:0007744","id":"7VKW","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"7VKX","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"7VKY","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"7VKZ","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"7VL0","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"7VL1","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"7VL2","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"7VL3","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"7VL4","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"7VL5","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"7VL6","source":"PDB"}],"referenceComments":[{"type":"STRAIN","value":"DSM 19864 / JCM 16511 / NBRC 101810 / Mat9-16"}],"referenceNumber":2,"referencePositions":["X-RAY CRYSTALLOGRAPHY (1.56 ANGSTROMS) IN COMPLEXES WITH BETA-D-GLUCOSE; SOPHOROSE AND ALTERNATIVE SUBSTRATES","FUNCTION","CATALYTIC ACTIVITY","BIOPHYSICOCHEMICAL PROPERTIES","SUBUNIT","ACTIVE SITE","MUTAGENESIS OF GLU-176 AND GLU-343"]}
```

Source SHA-256: `0141e863e485261dd884ecaf6bc9c67a2a0434afac2c92f95f4ffba2990aa032`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/I0AIT9?format=txt&versions=55)  
**Locator:** `lines 25-36`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 55 / 1.  
**Retrieved:** 2026-11-01T06:28:09.687306+00:00.  

```text
RN   [2] {ECO:0007744|PDB:7VKW, ECO:0007744|PDB:7VKX, ECO:0007744|PDB:7VKY, ECO:0007744|PDB:7VKZ, ECO:0007744|PDB:7VL0, ECO:0007744|PDB:7VL1, ECO:0007744|PDB:7VL2, ECO:0007744|PDB:7VL3, ECO:0007744|PDB:7VL4, ECO:0007744|PDB:7VL5, ECO:0007744|PDB:7VL6}
RP   X-RAY CRYSTALLOGRAPHY (1.56 ANGSTROMS) IN COMPLEXES WITH BETA-D-GLUCOSE;
RP   SOPHOROSE AND ALTERNATIVE SUBSTRATES, FUNCTION, CATALYTIC ACTIVITY,
RP   BIOPHYSICOCHEMICAL PROPERTIES, SUBUNIT, ACTIVE SITE, AND MUTAGENESIS OF
RP   GLU-176 AND GLU-343.
RC   STRAIN=DSM 19864 / JCM 16511 / NBRC 101810 / Mat9-16;
RX   PubMed=35065074; DOI=10.1016/j.jbc.2022.101606;
RA   Kobayashi K., Shimizu H., Tanaka N., Kuramochi K., Nakai H., Nakajima M.,
RA   Taguchi H.;
RT   "Characterization and structural analyses of a novel glycosyltransferase
RT   acting on the beta-1,2-glucosidic linkages.";
RL   J. Biol. Chem. 298:101606-101606(2022).
```

Source SHA-256: `5021025e7fb0e4fabd17270f530d15eceb2dace998f43c4ec775fc10c6352a01`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/I0AIT9?format=txt&versions=55)  
**Locator:** `lines 52-92`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 55 / 1.  
**Retrieved:** 2026-11-01T06:28:09.687306+00:00.  

```text
CC   -!- BIOPHYSICOCHEMICAL PROPERTIES:
CC       Kinetic parameters:
CC         KM=9.6 mM for sophorose (with pNP-alpha-glucose as an acceptor)
CC         {ECO:0000269|PubMed:35065074};
CC         KM=22 mM for beta-(1->2)-glucotriose (with pNP-alpha-glucose as an
CC         acceptor) {ECO:0000269|PubMed:35065074};
CC         KM=0.20 mM for methyl-alpha-glucose {ECO:0000269|PubMed:35065074};
CC         KM=0.044 mM for ethyl-alpha-glucose {ECO:0000269|PubMed:35065074};
CC         KM=0.22 mM for phenyl-alpha-glucose {ECO:0000269|PubMed:35065074};
CC         KM=0.38 mM for alpha-arbutin {ECO:0000269|PubMed:35065074};
CC         KM=0.13 mM for pNP-alpha-glucose {ECO:0000269|PubMed:35065074};
CC         KM=0.096 mM for benzyl-alpha-glucose {ECO:0000269|PubMed:35065074};
CC         KM=0.15 mM for 2-naphthyl-alpha-glucose
CC         {ECO:0000269|PubMed:35065074};
CC         KM=0.13 mM for methyl-beta-glucose {ECO:0000269|PubMed:35065074};
CC         KM=0.026 mM for beta-arbutin {ECO:0000269|PubMed:35065074};
CC         KM=0.040 mM for pNP-beta-glucose {ECO:0000269|PubMed:35065074};
CC         KM=0.042 mM for gastrodin {ECO:0000269|PubMed:35065074};
CC         KM=0.021 mM for salicin {ECO:0000269|PubMed:35065074};
CC         KM=0.045 mM for esculin {ECO:0000269|PubMed:35065074};
CC         KM=0.15 mM for amygdalin {ECO:0000269|PubMed:35065074};
CC         Note=kcat is 70 sec(-1) with sophorose as substrate. kcat is 12 sec(-
CC         1) with beta-(1->2)-glucotriose as substrate. kcat is 1.0 sec(-1)
CC         with methyl-alpha-glucose as substrate. kcat is 0.55 sec(-1) with
CC         ethyl-alpha-glucose as substrate. kcat is 1.8 sec(-1) with phenyl-
CC         alpha-glucose as substrate. kcat is 8.7 sec(-1) with alpha-arbutin as
CC         substrate. kcat is 5.0 sec(-1) with pNP-alpha-glucose as substrate.
CC         kcat is 0.86 sec(-1) with benzyl-alpha-glucose as substrate. kcat is
CC         3.9 sec(-1) with 2-naphthyl-alpha-glucose as substrate. kcat is 1.9
CC         sec(-1) with methyl-beta-glucose as substrate. kcat is 1.4 sec(-1)
CC         with beta-arbutin as substrate. kcat is 0.46 sec(-1) with pNP-beta-
CC         glucose as substrate. kcat is 0.49 sec(-1) with gastrodin as
CC         substrate. kcat is 0.88 sec(-1) with salicin as substrate. kcat is
CC         1.3 sec(-1) with esculin as substrate. kcat is 0.35 sec(-1) with
CC         amygdalin as substrate. {ECO:0000269|PubMed:35065074};
CC       pH dependence:
CC         Shows high activity at pH 5.0 to 8.0. {ECO:0000269|PubMed:35065074};
CC       Temperature dependence:
CC         Optimum temperature is 55 degrees Celsius (PubMed:35065074). Stable
CC         up to 60 degrees Celsius after incubation for 1 hour
CC         (PubMed:35065074). {ECO:0000269|PubMed:35065074};
```

Source SHA-256: `5021025e7fb0e4fabd17270f530d15eceb2dace998f43c4ec775fc10c6352a01`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/temperature.json), zero-based source row 27. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
